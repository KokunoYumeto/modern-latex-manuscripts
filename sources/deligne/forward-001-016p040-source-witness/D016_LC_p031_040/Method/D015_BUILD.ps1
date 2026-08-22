param(
    [string]$SuccessorRoot = 'C:\Users\Floris\Documents\interlanguage\Transcription\Web_Session_Hourly_Intake\Zenodo_Maintenance\successor_D015'
)

$ErrorActionPreference = 'Stop'

$canonical = Join-Path $SuccessorRoot 'canonical_work'
$sourceTree = Join-Path $SuccessorRoot 'source_tree'
$buildRoot = Join-Path $SuccessorRoot 'build'
$receiptPath = Join-Path $SuccessorRoot 'audit\D015_BUILD_RECEIPT.json'
$authority = Join-Path $canonical 'authority\D015_IAS_Number14_300dpi.pdf'
$normalizer = Join-Path $SuccessorRoot 'normalize_pdf_deterministic.py'
$expectedAuthoritySha = '22BD33F5D00EA962BA24996703CDDF74C4DCB09BF91050F0463036B5B38803CB'

function Get-Sha256([string]$Path) {
    return (Get-FileHash -LiteralPath $Path -Algorithm SHA256).Hash.ToUpperInvariant()
}

function Get-PdfPages([string]$Path) {
    $line = (& pdfinfo $Path | Where-Object { $_ -match '^Pages:' } | Select-Object -First 1)
    if (-not $line) { throw "Unable to read PDF page count: $Path" }
    return [int](($line -replace '^Pages:\s*', '').Trim())
}

function Invoke-TexPair {
    param(
        [ValidateSet('pdflatex', 'lualatex')][string]$Engine,
        [string]$WorkingDirectory,
        [string]$TexName,
        [string]$FirstBuildDirectory,
        [string]$SecondBuildDirectory
    )

    foreach ($directory in @($FirstBuildDirectory, $SecondBuildDirectory)) {
        New-Item -ItemType Directory -Path $directory -Force | Out-Null
        Push-Location $WorkingDirectory
        try {
            & $Engine '-interaction=nonstopmode' '-halt-on-error' '-file-line-error' "-output-directory=$directory" $TexName | Out-Null
            if ($LASTEXITCODE -ne 0) { throw "$Engine failed for $TexName (pass 1)" }
            & $Engine '-interaction=nonstopmode' '-halt-on-error' '-file-line-error' "-output-directory=$directory" $TexName | Out-Null
            if ($LASTEXITCODE -ne 0) { throw "$Engine failed for $TexName (pass 2)" }
        }
        finally {
            Pop-Location
        }
        $rawPdf = Join-Path $directory ([System.IO.Path]::ChangeExtension($TexName, '.pdf'))
        $normalizedPdf = Join-Path $directory ([System.IO.Path]::ChangeExtension($TexName, '.normalized.pdf'))
        & python $normalizer $rawPdf $normalizedPdf | Out-Null
        if ($LASTEXITCODE -ne 0) { throw "Deterministic PDF normalization failed for $TexName" }
        Move-Item -LiteralPath $normalizedPdf -Destination $rawPdf -Force
    }

    $pdfName = [System.IO.Path]::ChangeExtension($TexName, '.pdf')
    $firstPdf = Join-Path $FirstBuildDirectory $pdfName
    $secondPdf = Join-Path $SecondBuildDirectory $pdfName
    $firstSha = Get-Sha256 $firstPdf
    $secondSha = Get-Sha256 $secondPdf
    if ($firstSha -ne $secondSha) {
        throw "Deterministic PDF rebuild failed for ${TexName}: $firstSha != $secondSha"
    }
    return [pscustomobject]@{
        TexName = $TexName
        Engine = $Engine
        FirstPdf = $firstPdf
        SecondPdf = $secondPdf
        PdfSha256 = $firstSha
        PdfBytes = (Get-Item -LiteralPath $firstPdf).Length
        PdfPages = Get-PdfPages $firstPdf
    }
}

if (-not (Test-Path -LiteralPath $authority -PathType Leaf)) { throw "Missing IAS authority: $authority" }
if ((Get-Sha256 $authority) -ne $expectedAuthoritySha) { throw 'IAS authority SHA-256 mismatch' }
if (-not (Test-Path -LiteralPath $normalizer -PathType Leaf)) { throw "Missing deterministic PDF normalizer: $normalizer" }
foreach ($required in @('D015_FR.tex', 'D015_EN.tex')) {
    if (-not (Test-Path -LiteralPath (Join-Path $canonical $required) -PathType Leaf)) {
        throw "Missing canonical TeX: $required"
    }
}

$assetFiles = @(Get-ChildItem -LiteralPath (Join-Path $canonical 'D015_assets') -Filter '*_presentation.png' -File)
$rawAssetFiles = @(Get-ChildItem -LiteralPath (Join-Path $canonical 'D015_assets') -Filter '*_raw_IAS.png' -File)
$allAssetFiles = @($assetFiles + $rawAssetFiles)
if ($assetFiles.Count -ne 7) { throw "Expected seven presentation assets, found $($assetFiles.Count)" }
if ($rawAssetFiles.Count -ne 7) { throw "Expected seven raw IAS assets, found $($rawAssetFiles.Count)" }

New-Item -ItemType Directory -Path $buildRoot,(Split-Path -Parent $receiptPath) -Force | Out-Null
$priorSourceDateEpoch = $env:SOURCE_DATE_EPOCH
$priorForceSourceDate = $env:FORCE_SOURCE_DATE
$priorTaskTimezone = $env:TZ
$env:SOURCE_DATE_EPOCH = '1787356800'
$env:FORCE_SOURCE_DATE = '1'
$env:TZ = 'UTC'
try {
    $standalone = @()
    foreach ($language in @('FR', 'EN')) {
        $tex = "D015_$language.tex"
        $standalone += Invoke-TexPair -Engine pdflatex -WorkingDirectory $canonical -TexName $tex `
            -FirstBuildDirectory (Join-Path $buildRoot "standalone_${language}_A") `
            -SecondBuildDirectory (Join-Path $buildRoot "standalone_${language}_B")
    }

    $works = Join-Path $sourceTree 'works'
    $sourceAssets = Join-Path $works 'D015_assets'
    New-Item -ItemType Directory -Path $works,$sourceAssets -Force | Out-Null
    foreach ($item in $standalone) {
        $language = if ($item.TexName -match '_FR') { 'FR' } else { 'EN' }
        $texDestination = Join-Path $works "D015_$language.tex"
        $pdfDestination = Join-Path $works "D015_$language.pdf"
        if (Test-Path -LiteralPath $texDestination -PathType Container) {
            throw "Source-tree destination is unexpectedly a directory: $texDestination"
        }
        if (Test-Path -LiteralPath $pdfDestination -PathType Container) {
            throw "Source-tree destination is unexpectedly a directory: $pdfDestination"
        }
        Copy-Item -LiteralPath (Join-Path $canonical $item.TexName) -Destination $texDestination -Force
        Copy-Item -LiteralPath $item.FirstPdf -Destination $pdfDestination -Force
        Copy-Item -LiteralPath $item.FirstPdf -Destination (Join-Path $canonical "D015_$language.pdf") -Force
    }
    foreach ($asset in $allAssetFiles) {
        Copy-Item -LiteralPath $asset.FullName -Destination (Join-Path $sourceAssets $asset.Name) -Force
    }
    $apparatus = Join-Path $canonical 'D015_APPARATUS.md'
    if (-not (Test-Path -LiteralPath $apparatus -PathType Leaf)) {
        throw "Missing restrained apparatus: $apparatus"
    }
    Copy-Item -LiteralPath $apparatus -Destination (Join-Path $works 'D015_APPARATUS.md') -Force

    $cumulative = @()
    foreach ($language in @('FR', 'EN')) {
        $tex = "Deligne_$language.tex"
        $cumulative += Invoke-TexPair -Engine lualatex -WorkingDirectory $sourceTree -TexName $tex `
            -FirstBuildDirectory (Join-Path $buildRoot "cumulative_${language}_A") `
            -SecondBuildDirectory (Join-Path $buildRoot "cumulative_${language}_B")
    }
    foreach ($item in $cumulative) {
        Copy-Item -LiteralPath $item.FirstPdf -Destination (Join-Path $sourceTree ([System.IO.Path]::GetFileName($item.FirstPdf))) -Force
    }
}
finally {
    if ($null -eq $priorSourceDateEpoch) { Remove-Item Env:SOURCE_DATE_EPOCH -ErrorAction SilentlyContinue } else { $env:SOURCE_DATE_EPOCH = $priorSourceDateEpoch }
    if ($null -eq $priorForceSourceDate) { Remove-Item Env:FORCE_SOURCE_DATE -ErrorAction SilentlyContinue } else { $env:FORCE_SOURCE_DATE = $priorForceSourceDate }
    if ($null -eq $priorTaskTimezone) { Remove-Item Env:TZ -ErrorAction SilentlyContinue } else { $env:TZ = $priorTaskTimezone }
}

$receipt = [ordered]@{
    schema = 'deligne-d015-deterministic-build-v1'
    status = 'PASS'
    authority = [ordered]@{
        path = $authority
        bytes = (Get-Item -LiteralPath $authority).Length
        sha256 = Get-Sha256 $authority
        pages = Get-PdfPages $authority
    }
    standalone = @($standalone | ForEach-Object {
        [ordered]@{ tex = $_.TexName; engine = $_.Engine; pdf_bytes = $_.PdfBytes; pdf_pages = $_.PdfPages; pdf_sha256 = $_.PdfSha256; deterministic_rebuild = 'PASS' }
    })
    cumulative = @($cumulative | ForEach-Object {
        [ordered]@{ tex = $_.TexName; engine = $_.Engine; pdf_bytes = $_.PdfBytes; pdf_pages = $_.PdfPages; pdf_sha256 = $_.PdfSha256; deterministic_rebuild = 'PASS' }
    })
    presentation_assets = @($assetFiles | Sort-Object Name | ForEach-Object {
        [ordered]@{ name = $_.Name; bytes = $_.Length; sha256 = Get-Sha256 $_.FullName }
    })
    raw_authority_assets = @($rawAssetFiles | Sort-Object Name | ForEach-Object {
        [ordered]@{ name = $_.Name; bytes = $_.Length; sha256 = Get-Sha256 $_.FullName }
    })
}
$receipt | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath $receiptPath -Encoding utf8
$receipt | ConvertTo-Json -Depth 8
