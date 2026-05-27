[CmdletBinding()]
param(
    [int]$DepositionId = 20393489,
    [string]$ProjectRoot = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '..')).Path,
    [string]$UploadList = '',
    [string]$OutDir = ''
)

$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

if ([string]::IsNullOrWhiteSpace($UploadList)) {
    $UploadList = Join-Path $ProjectRoot 'release_candidates\web_pro_bundles\public_manifest\zenodo_public_upload_files.txt'
}
if ([string]::IsNullOrWhiteSpace($OutDir)) {
    $OutDir = Join-Path $ProjectRoot 'zenodo'
}
if (-not (Test-Path -LiteralPath $OutDir)) {
    New-Item -ItemType Directory -Force -Path $OutDir | Out-Null
}

$wrapper = Join-Path $ProjectRoot 'tools\Invoke-ZenodoHelperWithLocatedToken.ps1'
if (-not (Test-Path -LiteralPath $wrapper)) {
    throw "Missing Zenodo wrapper: $wrapper"
}
if (-not (Test-Path -LiteralPath $UploadList)) {
    throw "Missing upload list: $UploadList"
}

$remoteJson = & pwsh -NoProfile -ExecutionPolicy Bypass -File $wrapper get $DepositionId
if ($LASTEXITCODE -ne 0) {
    throw "Zenodo get failed for deposition $DepositionId"
}
$remote = $remoteJson | ConvertFrom-Json

$localFiles = Get-Content -LiteralPath $UploadList | Where-Object { -not [string]::IsNullOrWhiteSpace($_) }
$remoteByName = @{}
foreach ($file in @($remote.files)) {
    $remoteByName[[string]$file.filename] = $file
}

$rows = foreach ($localPath in $localFiles) {
    $item = Get-Item -LiteralPath $localPath
    $name = $item.Name
    $remoteFile = $remoteByName[$name]
    $localMd5 = (Get-FileHash -LiteralPath $item.FullName -Algorithm MD5).Hash.ToLowerInvariant()
    $localSha256 = (Get-FileHash -LiteralPath $item.FullName -Algorithm SHA256).Hash.ToLowerInvariant()
    $remoteChecksum = if ($remoteFile) { [string]$remoteFile.checksum } else { '' }
    [pscustomobject]@{
        filename = $name
        local_path = $item.FullName
        local_bytes = [int64]$item.Length
        remote_present = [bool]$remoteFile
        remote_bytes = if ($remoteFile) { [int64]$remoteFile.filesize } else { 0 }
        size_matches = if ($remoteFile) { [int64]$remoteFile.filesize -eq [int64]$item.Length } else { $false }
        remote_md5 = $remoteChecksum
        local_md5 = $localMd5
        md5_matches = if ($remoteChecksum) { $remoteChecksum.ToLowerInvariant() -eq $localMd5 } else { $false }
        local_sha256 = $localSha256
    }
}

$extraRemote = foreach ($file in @($remote.files)) {
    if (($localFiles | ForEach-Object { (Get-Item -LiteralPath $_).Name }) -notcontains [string]$file.filename) {
        [pscustomobject]@{
            filename = [string]$file.filename
            local_path = ''
            local_bytes = 0
            remote_present = $true
            remote_bytes = [int64]$file.filesize
            size_matches = $false
            remote_md5 = [string]$file.checksum
            local_md5 = ''
            md5_matches = $false
            local_sha256 = ''
        }
    }
}

$allRows = @($rows) + @($extraRemote)
$reportPath = Join-Path $OutDir "zenodo_draft_${DepositionId}_remote_file_check.csv"
$summaryPath = Join-Path $OutDir "zenodo_draft_${DepositionId}_remote_file_check_summary.json"
$remoteSnapshotPath = Join-Path $OutDir "zenodo_draft_${DepositionId}_remote_snapshot.json"

$allRows | Export-Csv -LiteralPath $reportPath -NoTypeInformation
$remoteJson | Set-Content -LiteralPath $remoteSnapshotPath -Encoding UTF8

$summary = [ordered]@{
    generated_at = (Get-Date).ToString('o')
    deposition_id = $DepositionId
    title = [string]$remote.title
    state = [string]$remote.state
    submitted = [bool]$remote.submitted
    draft_html = [string]$remote.links.latest_draft_html
    local_upload_file_count = @($localFiles).Count
    remote_file_count = @($remote.files).Count
    matched_remote_files = @($allRows | Where-Object { $_.remote_present -and $_.size_matches -and $_.md5_matches }).Count
    missing_remote_files = @($allRows | Where-Object { -not $_.remote_present }).Count
    extra_remote_files = @($extraRemote).Count
    mismatched_files = @($allRows | Where-Object { $_.remote_present -and (-not $_.size_matches -or -not $_.md5_matches) }).Count
    local_total_bytes = [int64](($rows | Measure-Object -Property local_bytes -Sum).Sum)
    remote_total_bytes = [int64]((@($remote.files) | Measure-Object -Property filesize -Sum).Sum)
    report = $reportPath
    remote_snapshot = $remoteSnapshotPath
}
$summary | ConvertTo-Json -Depth 4 | Set-Content -LiteralPath $summaryPath -Encoding UTF8
$summary | ConvertTo-Json -Depth 4
