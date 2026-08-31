[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$OutputDirectory
)

$ErrorActionPreference = 'Stop'
$sourceDirectory = $PSScriptRoot
$resolvedOutput = [System.IO.Path]::GetFullPath($OutputDirectory)

if (Test-Path -LiteralPath $resolvedOutput) {
    $existing = @(Get-ChildItem -LiteralPath $resolvedOutput -Force)
    if ($existing.Count -ne 0) {
        throw "Output directory must be empty: $resolvedOutput"
    }
} else {
    New-Item -ItemType Directory -Path $resolvedOutput | Out-Null
}

$compiler = Get-Command lualatex -ErrorAction Stop
$priorEpoch = $env:SOURCE_DATE_EPOCH
$priorForce = $env:FORCE_SOURCE_DATE
$priorTimezone = $env:TZ

try {
    $env:SOURCE_DATE_EPOCH = '0'
    $env:FORCE_SOURCE_DATE = '1'
    $env:TZ = 'UTC'
    Push-Location -LiteralPath $sourceDirectory
    try {
        foreach ($stem in @('D022_FR', 'D022_EN', 'D022_APPARATUS')) {
            foreach ($pass in 1..2) {
                & $compiler.Source '-interaction=nonstopmode' '-halt-on-error' '-file-line-error' "-output-directory=$resolvedOutput" "$stem.tex"
                if ($LASTEXITCODE -ne 0) {
                    throw "LuaLaTeX failed for $stem on pass $pass with exit code $LASTEXITCODE"
                }
            }
            $logPath = Join-Path $resolvedOutput "$stem.log"
            $pdfPath = Join-Path $resolvedOutput "$stem.pdf"
            if (-not (Test-Path -LiteralPath $logPath) -or -not (Test-Path -LiteralPath $pdfPath)) {
                throw "Expected build products are missing for $stem"
            }
            $logText = Get-Content -LiteralPath $logPath -Raw
            if ($logText -match '(?m)^(?:Overfull|Underfull|LaTeX Warning:|Package .* Warning:|! )') {
                throw "Warning or TeX error marker found in $logPath"
            }
        }
    } finally {
        Pop-Location
    }
} finally {
    $env:SOURCE_DATE_EPOCH = $priorEpoch
    $env:FORCE_SOURCE_DATE = $priorForce
    $env:TZ = $priorTimezone
}

Get-ChildItem -LiteralPath $resolvedOutput -Filter 'D022_*.pdf' |
    Sort-Object Name |
    ForEach-Object {
        $hash = Get-FileHash -Algorithm SHA256 -LiteralPath $_.FullName
        [pscustomobject]@{
            File = $_.Name
            Bytes = $_.Length
            SHA256 = $hash.Hash
        }
    }
