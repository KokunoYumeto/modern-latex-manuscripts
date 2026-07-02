param(
    [Parameter(Mandatory = $true)]
    [string]$CheckoutRoot,

    [string]$PayloadRoot = "C:\Users\memo_\Documents\Codex\2026-06-29\updatede-goal-text-maintain-the-noether-2\work\github-api-payloads\noether-slavic-handoff\20260629",

    [string]$PlanPath = "",

    [string]$DestinationSubdir = "noether-slavic-handoff\20260629",

    [switch]$Apply,

    [switch]$IncludeDeferredLargeMetadata
)

$ErrorActionPreference = "Stop"

function Resolve-ExistingDirectory {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Path,

        [Parameter(Mandatory = $true)]
        [string]$Label
    )

    if (-not (Test-Path -LiteralPath $Path -PathType Container)) {
        throw "$Label does not exist or is not a directory: $Path"
    }

    return [System.IO.Path]::GetFullPath((Resolve-Path -LiteralPath $Path).Path).TrimEnd('\', '/')
}

function Get-Sha256Upper {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Path
    )

    return (Get-FileHash -Algorithm SHA256 -LiteralPath $Path).Hash.ToUpperInvariant()
}

function Assert-WithinRoot {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Root,

        [Parameter(Mandatory = $true)]
        [string]$Candidate,

        [Parameter(Mandatory = $true)]
        [string]$Label
    )

    $rootWithSlash = $Root.TrimEnd('\', '/') + [System.IO.Path]::DirectorySeparatorChar
    if (-not $Candidate.StartsWith($rootWithSlash, [System.StringComparison]::OrdinalIgnoreCase)) {
        throw "$Label resolved outside expected root: $Candidate"
    }
}

$checkout = Resolve-ExistingDirectory -Path $CheckoutRoot -Label "CheckoutRoot"
$payload = Resolve-ExistingDirectory -Path $PayloadRoot -Label "PayloadRoot"

if ([string]::IsNullOrWhiteSpace($PlanPath)) {
    $PlanPath = Join-Path $payload "OFFLINE_GITHUB_COMMIT_BATCH_PLAN_20260630.json"
}

if (-not (Test-Path -LiteralPath $PlanPath -PathType Leaf)) {
    throw "PlanPath does not exist: $PlanPath"
}

$gitHead = Join-Path $checkout ".git\HEAD"
if (-not (Test-Path -LiteralPath $gitHead -PathType Leaf)) {
    throw "CheckoutRoot does not look like a valid Git checkout because .git\HEAD is missing: $CheckoutRoot"
}

$plan = Get-Content -Raw -LiteralPath $PlanPath | ConvertFrom-Json
$items = @($plan.commit_item_rows)

if ($IncludeDeferredLargeMetadata) {
    $selected = @($items | Where-Object {
        $_.exists_locally -eq $true -and
        $_.credentials_or_tokens_copied -eq $false -and
        $_.source_text_copied -eq $false -and
        $_.source_language_terms_copied -eq $false
    })
} else {
    $selected = @($items | Where-Object {
        $_.ready_for_small_text_commit -eq $true -and
        $_.deferred_until_bandwidth_window -eq $false -and
        $_.exists_locally -eq $true -and
        $_.credentials_or_tokens_copied -eq $false -and
        $_.source_text_copied -eq $false -and
        $_.source_language_terms_copied -eq $false
    })
}

$copyRows = New-Object System.Collections.Generic.List[object]
$errors = New-Object System.Collections.Generic.List[string]

foreach ($item in $selected) {
    $relativeFromPayload = $item.path -replace '^noether-slavic-handoff/20260629/', ''
    $source = [System.IO.Path]::GetFullPath((Join-Path $payload $relativeFromPayload))
    $target = [System.IO.Path]::GetFullPath((Join-Path $checkout ($item.path -replace '/', '\')))

    Assert-WithinRoot -Root $payload -Candidate $source -Label "Source path"
    Assert-WithinRoot -Root $checkout -Candidate $target -Label "Target path"

    if (-not (Test-Path -LiteralPath $source -PathType Leaf)) {
        $errors.Add("missing source: $source") | Out-Null
        continue
    }

    $sourceItem = Get-Item -LiteralPath $source
    if ([int64]$sourceItem.Length -ne [int64]$item.bytes) {
        $errors.Add("size mismatch for $source expected $($item.bytes) got $($sourceItem.Length)") | Out-Null
        continue
    }

    $hash = Get-Sha256Upper -Path $source
    if ($hash -ne [string]$item.sha256) {
        $errors.Add("sha256 mismatch for $source expected $($item.sha256) got $hash") | Out-Null
        continue
    }

    $copyRows.Add([pscustomobject]@{
        commit_batch_id = $item.commit_batch_id
        upload_class = $item.upload_class
        source = $source
        target = $target
        bytes = [int64]$item.bytes
        sha256 = $hash
    }) | Out-Null
}

if ($errors.Count -gt 0) {
    [pscustomobject]@{
        ok = $false
        apply = [bool]$Apply
        errors = @($errors)
    } | ConvertTo-Json -Depth 5
    exit 1
}

if ($Apply) {
    foreach ($row in $copyRows) {
        $targetDir = Split-Path -Parent $row.target
        if (-not (Test-Path -LiteralPath $targetDir -PathType Container)) {
            New-Item -ItemType Directory -Path $targetDir -Force | Out-Null
        }
        Copy-Item -LiteralPath $row.source -Destination $row.target -Force

        $targetItem = Get-Item -LiteralPath $row.target
        if ([int64]$targetItem.Length -ne [int64]$row.bytes) {
            throw "post-copy size mismatch for $($row.target)"
        }
        $targetHash = Get-Sha256Upper -Path $row.target
        if ($targetHash -ne $row.sha256) {
            throw "post-copy sha256 mismatch for $($row.target)"
        }
    }
}

$byBatch = @($copyRows | Group-Object commit_batch_id | Sort-Object Name | ForEach-Object {
    [pscustomobject]@{
        commit_batch_id = $_.Name
        files = $_.Count
        bytes = [int64](($_.Group | Measure-Object -Property bytes -Sum).Sum)
    }
})

$status = @()
if ($Apply) {
    $status = @(& git -C $checkout status --short -- $DestinationSubdir)
}

[pscustomobject]@{
    ok = $true
    apply = [bool]$Apply
    include_deferred_large_metadata = [bool]$IncludeDeferredLargeMetadata
    checkout_root = $checkout
    payload_root = $payload
    plan_path = [System.IO.Path]::GetFullPath($PlanPath)
    destination_subdir = $DestinationSubdir
    files_selected = $copyRows.Count
    bytes_selected = [int64](($copyRows | Measure-Object -Property bytes -Sum).Sum)
    batches = $byBatch
    git_status_short = $status
    note = "No clone, fetch, commit, push, authentication, or Zenodo action is performed by this helper."
} | ConvertTo-Json -Depth 6
