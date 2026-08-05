param(
  [string]$OutputDirectory = "./fresh_build"
)

$ErrorActionPreference = "Stop"
$sourceRoot = Join-Path $PSScriptRoot "..\source"
$output = [System.IO.Path]::GetFullPath((Join-Path $PSScriptRoot $OutputDirectory))
New-Item -ItemType Directory -Force -Path $output | Out-Null

Push-Location $sourceRoot
try {
  1..5 | ForEach-Object {
    & xelatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory="$output" ega4.tex
    if ($LASTEXITCODE -ne 0) { throw "XeLaTeX pass $_ failed" }
  }
} finally {
  Pop-Location
}
