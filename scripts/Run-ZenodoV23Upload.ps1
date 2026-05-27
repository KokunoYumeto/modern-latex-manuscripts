param(
    [Parameter(Mandatory=$true)]
    [int]$DepositionId
)

$ErrorActionPreference = 'Stop'
$ProjectRoot = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$uploadList = Join-Path $ProjectRoot 'release_candidates\zenodo_v23_kimi7_nonscan_artifacts\reports\zenodo_v23_upload_files.txt'
$logDir = Join-Path $ProjectRoot 'zenodo\v23_kimi7_nonscan_artifacts_publish'
New-Item -ItemType Directory -Force -Path $logDir | Out-Null

$files = Get-Content -LiteralPath $uploadList | Where-Object { $_.Trim() }
if (-not $files -or $files.Count -eq 0) {
    throw "No files listed in $uploadList"
}

$stamp = Get-Date -Format o
"[$stamp] Starting v23 replace upload for deposition $DepositionId with $($files.Count) files." |
    Tee-Object -FilePath (Join-Path $logDir 'upload_progress.log') -Append

& (Join-Path $ProjectRoot 'tools\Invoke-ZenodoHelperWithLocatedToken.ps1') upload $DepositionId @files --replace |
    Tee-Object -FilePath (Join-Path $logDir 'zenodo_v23_upload_result.json')

$stamp = Get-Date -Format o
"[$stamp] Finished v23 replace upload for deposition $DepositionId." |
    Tee-Object -FilePath (Join-Path $logDir 'upload_progress.log') -Append
