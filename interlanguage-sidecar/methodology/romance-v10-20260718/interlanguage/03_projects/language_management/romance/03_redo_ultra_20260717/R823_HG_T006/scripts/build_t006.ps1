$ErrorActionPreference = 'Stop'
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$tranche = Split-Path -Parent $here
if ((Split-Path -Leaf $tranche) -ne 'R823_HG_T006') { throw "Unexpected tranche path: $tranche" }
$repo = (Resolve-Path (Join-Path $tranche '..\..\..\..\..')).Path
$tex = Join-Path $tranche 'tex\R823_HG_T006_romance.tex'
$build = Join-Path $tranche 'build'
$qa = Join-Path $tranche 'qa'
$render = Join-Path $qa 'rendered'
$final = Join-Path $repo 'output\pdf'
$poppler = 'C:\Users\Floris\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin'
$pdftotext = (Get-Command pdftotext -ErrorAction Stop).Source
New-Item -ItemType Directory -Force -Path $build, $qa, $render, $final | Out-Null

Get-ChildItem -LiteralPath $build -File -ErrorAction SilentlyContinue | Remove-Item -Force
Get-ChildItem -LiteralPath $render -File -Filter 'R823_HG_T006_page-*.png' -ErrorAction SilentlyContinue | Remove-Item -Force

$console = Join-Path $build 'R823_HG_T006_lualatex_console.log'
$passone = Join-Path $build 'R823_HG_T006_lualatex_pass1.log'
Push-Location (Split-Path $tex)
try {
  & lualatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory="$build" (Split-Path $tex -Leaf) *> $passone
  if ($LASTEXITCODE -ne 0) { throw "LuaLaTeX pass 1 failed ($LASTEXITCODE)" }
  & lualatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory="$build" (Split-Path $tex -Leaf) *> $console
  if ($LASTEXITCODE -ne 0) { throw "LuaLaTeX pass 2 failed ($LASTEXITCODE)" }
}
finally { Pop-Location }

$pdf = Join-Path $build 'R823_HG_T006_romance.pdf'
$texlog = Join-Path $build 'R823_HG_T006_romance.log'
$warningPattern = 'Overfull|Underfull|Missing character|LaTeX Warning|Package .* Warning|Undefined control sequence|Emergency stop|Fatal error'
$warnings = Select-String -LiteralPath $texlog -Pattern $warningPattern -CaseSensitive:$false
if ($warnings) { throw "Final LuaLaTeX warning/error scan failed: $($warnings.Count) hit(s)" }

& (Join-Path $poppler 'pdfinfo.exe') $pdf | Set-Content -Encoding utf8 (Join-Path $qa 'R823_HG_T006_pdfinfo.txt')
if ($LASTEXITCODE -ne 0) { throw 'pdfinfo failed' }
& $pdftotext -layout $pdf (Join-Path $qa 'R823_HG_T006_extracted.txt')
if ($LASTEXITCODE -ne 0) { throw 'pdftotext failed' }
& (Join-Path $poppler 'pdftoppm.exe') -png -r 150 $pdf (Join-Path $render 'R823_HG_T006_page') | Out-Null
if ($LASTEXITCODE -ne 0) { throw 'pdftoppm failed' }
Copy-Item -LiteralPath $pdf -Destination (Join-Path $final 'R823_HG_T006_controlled_romance.pdf') -Force
Write-Output "PASS build: $pdf"
