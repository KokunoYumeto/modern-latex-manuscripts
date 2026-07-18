$ErrorActionPreference = 'Stop'
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$tex = Join-Path $here 'SGA6_English_FullRange_Layered_WorkingReader.tex'
$job = 'SGA6_English_FullRange_Layered_WorkingReader'
Push-Location $here
try {
  & pdflatex -interaction=nonstopmode -halt-on-error -file-line-error "-jobname=$job" $tex
  if ($LASTEXITCODE -ne 0) { throw "First pdfLaTeX pass failed: $LASTEXITCODE" }
  & pdflatex -interaction=nonstopmode -halt-on-error -file-line-error "-jobname=$job" $tex
  if ($LASTEXITCODE -ne 0) { throw "Second pdfLaTeX pass failed: $LASTEXITCODE" }
} finally {
  Pop-Location
}
