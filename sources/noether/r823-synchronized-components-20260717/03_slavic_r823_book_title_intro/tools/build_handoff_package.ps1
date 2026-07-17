param()

$ErrorActionPreference = 'Stop'

$root = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '..')).Path
$tmpRoot = [System.IO.Path]::GetFullPath((Join-Path $root 'tmp'))
$stage = [System.IO.Path]::GetFullPath((Join-Path $tmpRoot 'handoff_stage_v001'))
$extract = [System.IO.Path]::GetFullPath((Join-Path $tmpRoot 'handoff_extract_v001'))
$outputDir = Join-Path $root 'output'
$packageName = 'Noether_R823_BOOK_TITLE_INTRO_Slavic_v001_20260717.zip'
$package = Join-Path $outputDir $packageName
$manifest = Join-Path $root 'MANIFEST.csv'
$validation = Join-Path $outputDir 'Noether_R823_BOOK_TITLE_INTRO_Slavic_v001_20260717.package_validation.json'
$shaSidecar = "$package.sha256"

function Remove-VerifiedTemporaryDirectory {
    param([Parameter(Mandatory = $true)][string]$Path)

    $full = [System.IO.Path]::GetFullPath($Path)
    $requiredPrefix = $tmpRoot.TrimEnd('\') + '\'
    if (-not $full.StartsWith($requiredPrefix, [System.StringComparison]::OrdinalIgnoreCase)) {
        throw "Refusing recursive removal outside the workspace tmp directory: $full"
    }
    if ($full -eq $tmpRoot) {
        throw "Refusing recursive removal of the workspace tmp root itself."
    }
    if (Test-Path -LiteralPath $full) {
        Remove-Item -LiteralPath $full -Recurse -Force
    }
}

function Get-SHA256 {
    param([Parameter(Mandatory = $true)][string]$Path)
    return (Get-FileHash -Algorithm SHA256 -LiteralPath $Path).Hash
}

New-Item -ItemType Directory -Force -Path $tmpRoot | Out-Null
New-Item -ItemType Directory -Force -Path $outputDir | Out-Null
Remove-VerifiedTemporaryDirectory -Path $stage
Remove-VerifiedTemporaryDirectory -Path $extract
New-Item -ItemType Directory -Force -Path $stage | Out-Null

$selected = @()
$selected += Get-Item -LiteralPath (Join-Path $root 'README.md')
$selected += Get-ChildItem -LiteralPath (Join-Path $root 'authority') -File
$selected += Get-ChildItem -LiteralPath (Join-Path $root 'translations') -File -Recurse
$selected += Get-ChildItem -LiteralPath (Join-Path $root 'evidence') -File -Recurse |
    Where-Object { $_.Name -ne 'PACKAGE_VALIDATION.json' }
$selected += Get-ChildItem -LiteralPath (Join-Path $root 'output\pdf') -File
$selected += Get-ChildItem -LiteralPath (Join-Path $root 'output\logs') -File
$selected += Get-ChildItem -LiteralPath (Join-Path $root 'tools') -File
$selected = @($selected | Sort-Object FullName -Unique)

$records = foreach ($file in $selected) {
    $relative = [System.IO.Path]::GetRelativePath($root, $file.FullName).Replace('\', '/')
    [pscustomobject]@{
        relative_path = $relative
        bytes = $file.Length
        sha256 = Get-SHA256 -Path $file.FullName
    }
}
$records | Export-Csv -LiteralPath $manifest -NoTypeInformation -Encoding utf8

$selected += Get-Item -LiteralPath $manifest
foreach ($file in $selected) {
    $relative = [System.IO.Path]::GetRelativePath($root, $file.FullName)
    $destination = Join-Path $stage $relative
    $destinationDirectory = Split-Path -Parent $destination
    New-Item -ItemType Directory -Force -Path $destinationDirectory | Out-Null
    Copy-Item -LiteralPath $file.FullName -Destination $destination -Force
}

if (Test-Path -LiteralPath $package) {
    Remove-Item -LiteralPath $package -Force
}
Compress-Archive -Path (Join-Path $stage '*') -DestinationPath $package -CompressionLevel Optimal

New-Item -ItemType Directory -Force -Path $extract | Out-Null
Expand-Archive -LiteralPath $package -DestinationPath $extract -Force

$extractedManifest = Join-Path $extract 'MANIFEST.csv'
$manifestRows = Import-Csv -LiteralPath $extractedManifest
$failures = @()
foreach ($row in $manifestRows) {
    $candidate = Join-Path $extract ($row.relative_path.Replace('/', '\'))
    if (-not (Test-Path -LiteralPath $candidate)) {
        $failures += "missing:$($row.relative_path)"
        continue
    }
    $actual = Get-SHA256 -Path $candidate
    if ($actual -ne $row.sha256) {
        $failures += "hash:$($row.relative_path)"
    }
}

$packageHash = Get-SHA256 -Path $package
$zipEntryCount = (Get-ChildItem -LiteralPath $extract -File -Recurse).Count
$report = [ordered]@{
    schema = 'noether-r823-slavic-handoff-validation-v1'
    generated_at = (Get-Date).ToString('o')
    package = $package
    package_bytes = (Get-Item -LiteralPath $package).Length
    package_sha256 = $packageHash
    zip_entry_count = $zipEntryCount
    manifest_data_rows = $manifestRows.Count
    extraction_tested = $true
    missing_or_hash_failures = $failures
    pass = ($failures.Count -eq 0)
    status_limit = 'Internal handoff package; not a complete book, critical edition, or external/community certification.'
}
$report | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath $validation -Encoding utf8
"$packageHash  $packageName" | Set-Content -LiteralPath $shaSidecar -Encoding ascii

Remove-VerifiedTemporaryDirectory -Path $stage
Remove-VerifiedTemporaryDirectory -Path $extract

if (-not $report.pass) {
    throw "Package validation failed: $($failures -join ', ')"
}

$report | ConvertTo-Json -Depth 5
