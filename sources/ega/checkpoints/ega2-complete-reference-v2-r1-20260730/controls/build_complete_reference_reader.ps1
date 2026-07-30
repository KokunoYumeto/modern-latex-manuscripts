param(
    [Parameter(Mandatory = $true)]
    [string]$OutputDirectory,

    [string]$SourceDateEpoch = "1785420850"
)

$ErrorActionPreference = "Stop"
$scriptDirectory = Split-Path -Parent $MyInvocation.MyCommand.Path
$packageRoot = Split-Path -Parent $scriptDirectory
$sourceRoot = Join-Path $packageRoot "source"
$master = Join-Path $sourceRoot "ega2.tex"
$targets = Join-Path $scriptDirectory "REFERENCE_TARGETS.csv"
$overlayScript = Join-Path $scriptDirectory "apply_stable_target_aliases.py"

if (-not [System.IO.Path]::IsPathRooted($OutputDirectory)) {
    $OutputDirectory = Join-Path $packageRoot $OutputDirectory
}
$OutputDirectory = [System.IO.Path]::GetFullPath($OutputDirectory)
if (Test-Path -LiteralPath $OutputDirectory) {
    throw "Refusing to reuse existing output directory: $OutputDirectory"
}

$texBuild = Join-Path $OutputDirectory "tex_build"
New-Item -ItemType Directory -Path $texBuild -Force | Out-Null
$previousSourceDateEpoch = $env:SOURCE_DATE_EPOCH
$previousForceSourceDate = $env:FORCE_SOURCE_DATE
$env:SOURCE_DATE_EPOCH = $SourceDateEpoch
$env:FORCE_SOURCE_DATE = "1"

try {
    Push-Location $sourceRoot
    try {
        foreach ($pass in 1..4) {
            $consolePath = Join-Path $OutputDirectory "pass${pass}_console.txt"
            & xelatex `
                -interaction=nonstopmode `
                -halt-on-error `
                -file-line-error `
                "-output-directory=$texBuild" `
                $master 2>&1 | Out-File -LiteralPath $consolePath -Encoding utf8
            if ($LASTEXITCODE -ne 0) {
                throw "XeLaTeX pass $pass failed with exit code $LASTEXITCODE"
            }
        }
    }
    finally {
        Pop-Location
    }

    $pass3Hash = (Get-FileHash -Algorithm SHA256 -LiteralPath `
        (Join-Path $OutputDirectory "pass3_console.txt")).Hash
    $pass4Hash = (Get-FileHash -Algorithm SHA256 -LiteralPath `
        (Join-Path $OutputDirectory "pass4_console.txt")).Hash
    if ($pass3Hash -ne $pass4Hash) {
        throw "Pass 3 and pass 4 console logs are not byte-identical"
    }

    $finalLog = Join-Path $texBuild "ega2.log"
    $fatalPatterns = @(
        "undefined references",
        "multiply defined",
        "duplicate destination",
        "has been referenced but does not exist",
        "Fatal error",
        "Emergency stop",
        "Missing character",
        "Rerun to get cross-references right",
        "Label(s) may have changed"
    )
    $diagnostics = Select-String -LiteralPath $finalLog `
        -Pattern $fatalPatterns -CaseSensitive:$false
    if ($diagnostics) {
        throw "Final TeX log contains release-blocking diagnostics"
    }

    $compiledPdf = Join-Path $texBuild "ega2.pdf"
    $finalPdf = Join-Path $OutputDirectory "EGA2_English_complete_reference_reader.pdf"
    & python $overlayScript $compiledPdf $targets $finalPdf
    if ($LASTEXITCODE -ne 0) {
        throw "Stable-reference overlay failed"
    }

    $result = [ordered]@{
        schema = "ega2-complete-reference-reader-build-result-1.0"
        status = "PASS"
        source_date_epoch = $SourceDateEpoch
        passes = 4
        pass3_pass4_console_byte_identical = $true
        pass3_console_sha256 = $pass3Hash
        pass4_console_sha256 = $pass4Hash
        compiled_pdf_bytes = (Get-Item -LiteralPath $compiledPdf).Length
        compiled_pdf_sha256 = (Get-FileHash -Algorithm SHA256 -LiteralPath $compiledPdf).Hash
        final_pdf_bytes = (Get-Item -LiteralPath $finalPdf).Length
        final_pdf_sha256 = (Get-FileHash -Algorithm SHA256 -LiteralPath $finalPdf).Hash
    }
    $result | ConvertTo-Json -Depth 4 | Set-Content `
        -LiteralPath (Join-Path $OutputDirectory "BUILD_RESULT.json") `
        -Encoding utf8
    $result | ConvertTo-Json -Depth 4
}
finally {
    $env:SOURCE_DATE_EPOCH = $previousSourceDateEpoch
    $env:FORCE_SOURCE_DATE = $previousForceSourceDate
}
