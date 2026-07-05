param(
    [Parameter(Mandatory = $false)]
    [string]$RepoRoot = "C:\Users\Floris\Documents\Papors\modern-latex-manuscripts-github",

    [Parameter(Mandatory = $false)]
    [string]$OutDir = "interlanguage-sidecar\20260704\latex_source_body_bundles\slavic_github_tex_queue_20260705",

    [Parameter(Mandatory = $false)]
    [string[]]$OpenLicenseSpdx = @(
        "MIT",
        "CC0-1.0",
        "Apache-2.0",
        "BSD-2-Clause",
        "BSD-3-Clause",
        "CC-BY-4.0",
        "CC-BY-SA-4.0",
        "GPL-2.0",
        "GPL-3.0",
        "LGPL-2.1",
        "LGPL-3.0"
    )
)

$ErrorActionPreference = "Stop"

$candidateRoots = @(
    "noether-slavic-source-canon\20260704\NOETHER_SLAVIC_SOURCE_CANON_GITHUB_TEX_20260704T192100Z\manifests",
    "noether-slavic-source-canon\20260704\NOETHER_SLAVIC_SOURCE_CANON_GITHUB_TEX_20260704T211000Z\manifests"
)

$outPath = Join-Path $RepoRoot $OutDir
New-Item -ItemType Directory -Force -Path $outPath | Out-Null

$candidateRows = New-Object System.Collections.Generic.List[object]
$payloadUrls = New-Object System.Collections.Generic.HashSet[string]

foreach ($root in $candidateRoots) {
    $manifestDir = Join-Path $RepoRoot $root
    if (-not (Test-Path -LiteralPath $manifestDir)) {
        continue
    }

    Get-ChildItem -LiteralPath $manifestDir -Filter "GITHUB_TEX_OPEN_LICENSE_PAYLOAD_MANIFEST.csv" -File | ForEach-Object {
        Import-Csv -LiteralPath $_.FullName | ForEach-Object {
            if ($_.raw_url) {
                [void]$payloadUrls.Add($_.raw_url)
            }
        }
    }

    Get-ChildItem -LiteralPath $manifestDir -Filter "GITHUB_TEX_TARGET_LANGUAGE_CANDIDATES.csv" -File | ForEach-Object {
        $sourceManifest = $_.FullName.Substring($RepoRoot.Length + 1)
        Import-Csv -LiteralPath $_.FullName | ForEach-Object {
            $license = $_.repo_license_spdx
            $inPayload = $false
            if ($_.raw_url -and $payloadUrls.Contains($_.raw_url)) {
                $inPayload = $true
            }
            $licenseIsOpen = $false
            if ($license -and ($OpenLicenseSpdx -contains $license)) {
                $licenseIsOpen = $true
            }

            $status = "url_only_candidate"
            if ($inPayload) {
                $status = "already_in_payload"
            } elseif ($licenseIsOpen) {
                $status = "open_license_download_candidate"
            } elseif (-not $license) {
                $status = "license_missing_url_only"
            } else {
                $status = "license_not_allowlisted_url_only"
            }

            $candidateRows.Add([pscustomobject]@{
                status = $status
                language_code = $_.language_code
                language_name = $_.language_name
                repo = $_.repo
                path = $_.path
                raw_url = $_.raw_url
                blob_url = $_.blob_url
                search_term = $_.search_term
                repo_license_spdx = $license
                repo_license_name = $_.repo_license_name
                source_manifest = $sourceManifest
                public_use_boundary = "source-corpus/provenance support only; not native review, accepted terminology, translation completion, source-fidelity certification, publication readiness, reader output, or critical edition"
            })
        }
    }
}

$all = $candidateRows | Sort-Object language_code, status, repo, path
$openQueue = $all | Where-Object { $_.status -eq "open_license_download_candidate" }
$urlOnly = $all | Where-Object { $_.status -in @("license_missing_url_only", "license_not_allowlisted_url_only", "url_only_candidate") }
$already = $all | Where-Object { $_.status -eq "already_in_payload" }

$allPath = Join-Path $outPath "SLAVIC_GITHUB_TEX_ALL_CANDIDATES_QUEUE_20260705.csv"
$openPath = Join-Path $outPath "SLAVIC_GITHUB_TEX_OPEN_LICENSE_DOWNLOAD_QUEUE_20260705.csv"
$urlPath = Join-Path $outPath "SLAVIC_GITHUB_TEX_URL_ONLY_QUEUE_20260705.csv"
$alreadyPath = Join-Path $outPath "SLAVIC_GITHUB_TEX_ALREADY_PAYLOAD_QUEUE_20260705.csv"
$summaryPath = Join-Path $outPath "SLAVIC_GITHUB_TEX_QUEUE_BY_LANGUAGE_20260705.csv"

$all | Export-Csv -LiteralPath $allPath -NoTypeInformation -Encoding UTF8
$openQueue | Export-Csv -LiteralPath $openPath -NoTypeInformation -Encoding UTF8
$urlOnly | Export-Csv -LiteralPath $urlPath -NoTypeInformation -Encoding UTF8
$already | Export-Csv -LiteralPath $alreadyPath -NoTypeInformation -Encoding UTF8

$summary = $all |
    Group-Object language_code |
    Sort-Object Name |
    ForEach-Object {
        $group = $_.Group
        [pscustomobject]@{
            language_code = $_.Name
            language_name = ($group | Select-Object -First 1).language_name
            total_candidates = $group.Count
            already_in_payload = ($group | Where-Object { $_.status -eq "already_in_payload" }).Count
            open_license_download_candidates = ($group | Where-Object { $_.status -eq "open_license_download_candidate" }).Count
            url_only_or_unclear_license_candidates = ($group | Where-Object { $_.status -ne "already_in_payload" -and $_.status -ne "open_license_download_candidate" }).Count
            status = "below_hundreds_per_language_target"
        }
    }

$summary | Export-Csv -LiteralPath $summaryPath -NoTypeInformation -Encoding UTF8

$readme = @'
# Slavic GitHub TeX Queue, 2026-07-05

This directory is a repeatable queue built from the recovered Slavic GitHub TeX candidate manifests.

It separates:

- `SLAVIC_GITHUB_TEX_ALREADY_PAYLOAD_QUEUE_20260705.csv`: candidate rows whose raw URL is already present in an admitted payload manifest.
- `SLAVIC_GITHUB_TEX_OPEN_LICENSE_DOWNLOAD_QUEUE_20260705.csv`: candidate rows with an allowlisted repository license and no matching admitted payload row yet.
- `SLAVIC_GITHUB_TEX_URL_ONLY_QUEUE_20260705.csv`: candidate rows with missing or non-allowlisted license metadata. Keep these as source anchors/provenance until a human or later collector decides how to handle them.
- `SLAVIC_GITHUB_TEX_QUEUE_BY_LANGUAGE_20260705.csv`: conservative by-language counts.

Classification boundary: this is source-corpus/provenance support for Web/Pro/Codex language-register work. It is not native review, accepted terminology, translation completion, source-fidelity certification, publication readiness, reader output, or a critical edition.

Current open target: non-Russian/non-Ukrainian Slavic native mathematical TeX is still below the hundreds-per-language target. The queue makes that gap explicit and gives the next collector a clean continuation point.

Generated by:

```powershell
pwsh -File scripts\source_intake\build_slavic_github_tex_queue.ps1
```
'@

Set-Content -LiteralPath (Join-Path $outPath "README.md") -Value $readme -Encoding UTF8

$result = [pscustomobject]@{
    out_dir = $outPath
    total_candidates = $all.Count
    already_in_payload = $already.Count
    open_license_download_candidates = $openQueue.Count
    url_only_or_unclear_license_candidates = $urlOnly.Count
}

$result | ConvertTo-Json -Depth 4 | Set-Content -LiteralPath (Join-Path $outPath "SUMMARY.json") -Encoding UTF8
$result
