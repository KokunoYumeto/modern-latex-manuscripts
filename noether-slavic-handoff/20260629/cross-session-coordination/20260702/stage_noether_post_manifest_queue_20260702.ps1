param(
    [Parameter(Mandatory = $true)]
    [string]$CheckoutRoot,

    [string]$QueuePath = "C:\Users\memo_\Documents\Codex\2026-06-29\files-mentioned-by-the-user-worked\outputs\NOETHER_POST_MANIFEST_COORDINATION_UPLOAD_QUEUE_20260702.json",

    [string]$SourceRoot = "C:\Users\memo_\Documents\Codex\2026-06-29\files-mentioned-by-the-user-worked\outputs",

    [string]$DestinationSubdir = "",

    [switch]$Apply
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

function Resolve-ExistingFile {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Path,

        [Parameter(Mandatory = $true)]
        [string]$Label
    )

    if (-not (Test-Path -LiteralPath $Path -PathType Leaf)) {
        throw "$Label does not exist or is not a file: $Path"
    }

    return [System.IO.Path]::GetFullPath((Resolve-Path -LiteralPath $Path).Path)
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
$sourceRootResolved = Resolve-ExistingDirectory -Path $SourceRoot -Label "SourceRoot"
$queueResolved = Resolve-ExistingFile -Path $QueuePath -Label "QueuePath"

$gitHead = Join-Path $checkout ".git\HEAD"
if (-not (Test-Path -LiteralPath $gitHead -PathType Leaf)) {
    throw "CheckoutRoot does not look like a valid Git checkout because .git\HEAD is missing: $CheckoutRoot"
}

$queue = Get-Content -Raw -LiteralPath $queueResolved | ConvertFrom-Json
if ([string]::IsNullOrWhiteSpace($DestinationSubdir)) {
    $DestinationSubdir = $queue.recommended_destination_in_checkout
}
if ([string]::IsNullOrWhiteSpace($DestinationSubdir)) {
    throw "DestinationSubdir is empty and queue has no recommended destination."
}

if ($queue.credentials_or_tokens_copied -ne $false) {
    throw "Queue is not safe to stage: credentials_or_tokens_copied is not false."
}
if ($queue.source_text_copied -ne $false) {
    throw "Queue is not safe to stage: source_text_copied is not false."
}
if ($queue.source_language_terms_copied -ne $false) {
    throw "Queue is not safe to stage: source_language_terms_copied is not false."
}
if ([int64]$queue.summary.raw_token_files -ne 0) {
    throw "Queue is not safe to stage: raw_token_files is not zero."
}
if ([int64]$queue.summary.source_pdf_files -ne 0 -or [int64]$queue.summary.source_image_files -ne 0) {
    throw "Queue is not safe to stage: source PDF/image files are present."
}
if ([int64]$queue.summary.source_text_or_excerpt_files -ne 0) {
    throw "Queue is not safe to stage: source_text_or_excerpt_files is not zero."
}

$copyRows = New-Object System.Collections.Generic.List[object]
$errors = New-Object System.Collections.Generic.List[string]
$destinationNormalized = $DestinationSubdir -replace '/', '\'

foreach ($item in @($queue.queued_items)) {
    $filename = [string]$item.filename
    if ([string]::IsNullOrWhiteSpace($filename)) {
        $errors.Add("queued item has empty filename") | Out-Null
        continue
    }
    if ($filename.IndexOfAny([char[]]@('\', '/', ':')) -ge 0) {
        $errors.Add("queued filename is not a plain basename: $filename") | Out-Null
        continue
    }

    $source = [System.IO.Path]::GetFullPath((Join-Path $sourceRootResolved $filename))
    $target = [System.IO.Path]::GetFullPath((Join-Path $checkout (Join-Path $destinationNormalized $filename)))

    Assert-WithinRoot -Root $sourceRootResolved -Candidate $source -Label "Source path"
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
    if ($hash -ne ([string]$item.sha256).ToUpperInvariant()) {
        $errors.Add("sha256 mismatch for $source expected $($item.sha256) got $hash") | Out-Null
        continue
    }

    $copyRows.Add([pscustomobject]@{
        upload_class = [string]$item.class
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
        note = "No clone, fetch, commit, push, authentication, or Zenodo action is performed by this helper."
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

$byClass = @($copyRows | Group-Object upload_class | Sort-Object Name | ForEach-Object {
    [pscustomobject]@{
        upload_class = $_.Name
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
    checkout_root = $checkout
    source_root = $sourceRootResolved
    queue_path = $queueResolved
    destination_subdir = $DestinationSubdir
    files_selected = $copyRows.Count
    bytes_selected = [int64](($copyRows | Measure-Object -Property bytes -Sum).Sum)
    classes = $byClass
    git_status_short = $status
    note = "No clone, fetch, commit, push, authentication, or Zenodo action is performed by this helper."
} | ConvertTo-Json -Depth 6
