param(
    [Parameter(Mandatory = $false)]
    [string]$RepoRoot = "C:\Users\Floris\Documents\Papors\modern-latex-manuscripts-github",

    [Parameter(Mandatory = $false)]
    [string]$QueueDir = "interlanguage-sidecar\20260704\latex_source_body_bundles\slavic_github_tex_queue_20260705",

    [Parameter(Mandatory = $false)]
    [string]$OutDir = "interlanguage-sidecar\20260704\latex_source_body_bundles\slavic_github_tex_queue_20260705\open_license_payload"
)

$ErrorActionPreference = "Stop"

function Convert-ToSafePathPart {
    param([string]$Text)
    if (-not $Text) {
        return "_"
    }
    return ($Text -replace '[<>:"/\\|?*]', '_' -replace '\s+', '_')
}

$queuePath = Join-Path (Join-Path $RepoRoot $QueueDir) "SLAVIC_GITHUB_TEX_OPEN_LICENSE_DOWNLOAD_QUEUE_20260705.csv"
if (-not (Test-Path -LiteralPath $queuePath)) {
    throw "Queue not found: $queuePath"
}

$outPath = Join-Path $RepoRoot $OutDir
$payloadRoot = Join-Path $outPath "payload"
New-Item -ItemType Directory -Force -Path $payloadRoot | Out-Null

$rows = Import-Csv -LiteralPath $queuePath
$manifest = New-Object System.Collections.Generic.List[object]

foreach ($row in $rows) {
    $lang = Convert-ToSafePathPart $row.language_code
    $repo = Convert-ToSafePathPart ($row.repo -replace '/', '_')
    $pathParts = $row.path -split '[\\/]'
    $safeParts = @($lang, $repo) + ($pathParts | ForEach-Object { Convert-ToSafePathPart $_ })
    $relativePayloadPath = Join-Path -Path "payload" -ChildPath (Join-Path $safeParts[0] (Join-Path $safeParts[1] ([IO.Path]::Combine($safeParts[2..($safeParts.Count - 1)]))))
    $targetPath = Join-Path $outPath $relativePayloadPath
    New-Item -ItemType Directory -Force -Path (Split-Path -Parent $targetPath) | Out-Null

    $status = "downloaded"
    $bytes = 0
    $sha256 = ""
    $errorText = ""

    try {
        $uri = $row.raw_url -replace ' ', '%20'
        Invoke-WebRequest -Uri $uri -OutFile $targetPath -UseBasicParsing | Out-Null
        $item = Get-Item -LiteralPath $targetPath
        $bytes = $item.Length
        $sha256 = (Get-FileHash -LiteralPath $targetPath -Algorithm SHA256).Hash
    } catch {
        $status = "download_failed"
        $errorText = $_.Exception.Message
        if (Test-Path -LiteralPath $targetPath) {
            Remove-Item -LiteralPath $targetPath -Force
        }
    }

    $manifest.Add([pscustomobject]@{
        status = $status
        language_code = $row.language_code
        language_name = $row.language_name
        repo = $row.repo
        path = $row.path
        payload_relative_path = $relativePayloadPath
        raw_url = $row.raw_url
        blob_url = $row.blob_url
        search_term = $row.search_term
        repo_license_spdx = $row.repo_license_spdx
        repo_license_name = $row.repo_license_name
        bytes = $bytes
        sha256 = $sha256
        error = $errorText
        public_use_boundary = "source-corpus/provenance support only; not native review, accepted terminology, translation completion, source-fidelity certification, publication readiness, reader output, or critical edition"
    })
}

$manifestPath = Join-Path $outPath "SLAVIC_GITHUB_TEX_OPEN_LICENSE_PAYLOAD_MANIFEST_20260705.csv"
$manifest | Export-Csv -LiteralPath $manifestPath -NoTypeInformation -Encoding UTF8

$readme = @'
# Slavic GitHub TeX Open-License Residue Payload, 2026-07-05

This payload downloads the small open-license residue left by the recovered Slavic GitHub TeX candidate manifests after already-admitted payload rows are removed.

Classification boundary: source-corpus/provenance support only. This is not native review, accepted terminology, translation completion, source-fidelity certification, publication readiness, reader output, or a critical edition.

The complete queue is one directory up. The queue deliberately keeps most unresolved or unclear-license rows as URL/provenance-only candidates.
'@

Set-Content -LiteralPath (Join-Path $outPath "README.md") -Value $readme -Encoding UTF8

$zipPath = Join-Path (Join-Path $RepoRoot "interlanguage-sidecar\20260704\latex_source_body_bundles") "Interlanguage_LaTeX_SourceBodies_Slavic_GitHub_OpenLicenseResidue_20260705.zip"
if (Test-Path -LiteralPath $zipPath) {
    Remove-Item -LiteralPath $zipPath -Force
}

Add-Type -AssemblyName System.IO.Compression.FileSystem
[System.IO.Compression.ZipFile]::CreateFromDirectory($outPath, $zipPath)

$summary = [pscustomobject]@{
    out_dir = $outPath
    zip_path = $zipPath
    rows = $rows.Count
    downloaded = ($manifest | Where-Object { $_.status -eq "downloaded" }).Count
    failed = ($manifest | Where-Object { $_.status -ne "downloaded" }).Count
    zip_bytes = (Get-Item -LiteralPath $zipPath).Length
    zip_sha256 = (Get-FileHash -LiteralPath $zipPath -Algorithm SHA256).Hash
}

$summary | ConvertTo-Json -Depth 4 | Set-Content -LiteralPath (Join-Path $outPath "SUMMARY.json") -Encoding UTF8
$summary
