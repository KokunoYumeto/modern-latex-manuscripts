$ErrorActionPreference = 'Stop'
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$tex = Join-Path $here 'SGA6_Expose_X_idx532_537_Spanish_SourceChecked.tex'
$out = Join-Path $here 'output\pdf'
$log = Join-Path $here 'BUILD.log'
New-Item -ItemType Directory -Path $out -Force | Out-Null
Push-Location $here
try {
  & pdflatex -interaction=nonstopmode -halt-on-error -file-line-error "-output-directory=$out" $tex 2>&1 | Tee-Object -FilePath $log
  if ($LASTEXITCODE -ne 0) { throw "First pdfLaTeX pass failed: $LASTEXITCODE" }
  & pdflatex -interaction=nonstopmode -halt-on-error -file-line-error "-output-directory=$out" $tex 2>&1 | Tee-Object -FilePath $log -Append
  if ($LASTEXITCODE -ne 0) { throw "Second pdfLaTeX pass failed: $LASTEXITCODE" }
} finally {
  Pop-Location
}
