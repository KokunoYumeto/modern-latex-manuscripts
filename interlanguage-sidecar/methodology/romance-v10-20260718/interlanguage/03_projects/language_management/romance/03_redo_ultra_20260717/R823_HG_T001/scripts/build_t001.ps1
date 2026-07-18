$ErrorActionPreference='Stop'
$here=Split-Path -Parent $MyInvocation.MyCommand.Path
$tranche=Split-Path -Parent $here
$repo=(Resolve-Path (Join-Path $tranche '..\..\..\..\..')).Path
$tex=Join-Path $tranche 'tex\R823_HG_T001_romance.tex'
$build=Join-Path $tranche 'build'
$qa=Join-Path $tranche 'qa'
$render=Join-Path $qa 'rendered'
$final=Join-Path $repo 'output\pdf'
$poppler='C:\Users\Floris\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin'
New-Item -ItemType Directory -Force -Path $build,$qa,$render,$final|Out-Null

$console=Join-Path $build 'R823_HG_T001_lualatex_console.log'
Push-Location (Split-Path $tex)
try{
  & lualatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory="$build" (Split-Path $tex -Leaf) *> $console
  if($LASTEXITCODE -ne 0){throw "LuaLaTeX pass 1 failed ($LASTEXITCODE)"}
  & lualatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory="$build" (Split-Path $tex -Leaf) *>> $console
  if($LASTEXITCODE -ne 0){throw "LuaLaTeX pass 2 failed ($LASTEXITCODE)"}
}finally{Pop-Location}

$pdf=Join-Path $build 'R823_HG_T001_romance.pdf'
& (Join-Path $poppler 'pdfinfo.exe') $pdf | Set-Content -Encoding utf8 (Join-Path $qa 'R823_HG_T001_pdfinfo.txt')
if($LASTEXITCODE -ne 0){throw 'pdfinfo failed'}
& pdftotext -layout $pdf (Join-Path $qa 'R823_HG_T001_extracted.txt')
if($LASTEXITCODE -ne 0){throw 'pdftotext failed'}
& (Join-Path $poppler 'pdftoppm.exe') -png -r 150 $pdf (Join-Path $render 'R823_HG_T001_page') | Out-Null
if($LASTEXITCODE -ne 0){throw 'pdftoppm failed'}
Copy-Item -LiteralPath $pdf -Destination (Join-Path $final 'R823_HG_T001_controlled_romance.pdf') -Force
Write-Output "PASS build: $pdf"
