$ErrorActionPreference = 'Stop'
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$pdf = Join-Path $here 'SGA6_English_FullRange_Layered_WorkingReader.pdf'
$log = Join-Path $here 'SGA6_English_FullRange_Layered_WorkingReader.log'
$tex = Join-Path $here 'SGA6_English_FullRange_Layered_WorkingReader.tex'
$pdfinfo = 'C:\Users\Floris\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdfinfo.exe'
$pdffonts = 'C:\Users\Floris\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdffonts.exe'
$pdftotext = 'C:\Users\Floris\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftotext.exe'
if (-not (Test-Path -LiteralPath $pdfinfo)) { $pdfinfo = (Get-Command pdfinfo -ErrorAction Stop).Source }
if (-not (Test-Path -LiteralPath $pdffonts)) { $pdffonts = (Get-Command pdffonts -ErrorAction Stop).Source }
if (-not (Test-Path -LiteralPath $pdftotext)) { $pdftotext = (Get-Command pdftotext -ErrorAction Stop).Source }
$info = & $pdfinfo $pdf
$pages = [int](($info | Select-String '^Pages:\s+(\d+)$').Matches[0].Groups[1].Value)
$issues = @(Select-String -LiteralPath $log -Pattern '^!|^Overfull|^Underfull|LaTeX Warning:|Package .* Warning:|Undefined control sequence|Emergency stop|Fatal error')
$fonts = & $pdffonts $pdf | Select-Object -Skip 2
$notEmbedded = @($fonts | Where-Object { $_ -notmatch '\s+yes\s+yes\s' })
$text = Get-Content -Raw -LiteralPath $tex
$page81 = (& $pdftotext -f 81 -l 81 -layout $pdf -) -join "`n"
$footnote14Present = $page81 -match 'We write S for the final object of the topos S' -and $page81 -match 'constant sheaf with value Z'
$pass = ($pages -eq 381) -and ($issues.Count -eq 0) -and ($notEmbedded.Count -eq 0) -and $footnote14Present -and ($text -match 'idx532') -and ($text -match 'idx662') -and ($text -match 'idx702')
[ordered]@{pass=$pass; pages=$pages; diagnostic_count=$issues.Count; nonembedded_font_count=$notEmbedded.Count; lemma_5_8_2_footnote_14_present=$footnote14Present; checked_at=(Get-Date).ToString('o')} | ConvertTo-Json
if (-not $pass) { exit 1 }
