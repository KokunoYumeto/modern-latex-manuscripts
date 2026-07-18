$ErrorActionPreference = 'Stop'
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$source = Join-Path $here 'source_control\SGA6_Expose_X_CurrentCheckedFrench_through_2_4.tex'
$target = Join-Path $here 'SGA6_Expose_X_idx532_537_Spanish_SourceChecked.tex'
$builtPdf = Join-Path $here 'output\pdf\SGA6_Expose_X_idx532_537_Spanish_SourceChecked.pdf'
$publishedPdf = Join-Path $here 'SGA6_Expose_X_idx532_537_Spanish_SourceChecked.pdf'
$pdf = if (Test-Path -LiteralPath $builtPdf) { $builtPdf } else { $publishedPdf }
$builtLog = Join-Path $here 'output\pdf\SGA6_Expose_X_idx532_537_Spanish_SourceChecked.log'
$publishedLog = Join-Path $here 'BUILD.log'
$engineLog = if (Test-Path -LiteralPath $builtLog) { $builtLog } else { $publishedLog }
$bundledPdfInfo = 'C:\Users\Floris\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdfinfo.exe'
$pdfInfoExe = if (Test-Path -LiteralPath $bundledPdfInfo) {
  $bundledPdfInfo
} else {
  (Get-Command pdfinfo -ErrorAction SilentlyContinue).Source
}
if (-not $pdfInfoExe) { throw 'pdfinfo was not found on PATH or in the bundled Codex runtime.' }

$sourceHead = (Get-Content -LiteralPath $source | Select-Object -First 142) -join "`n"
$targetText = Get-Content -Raw -LiteralPath $target
$tagPattern = '\\tag\{([^}]+)\}'
$sourceTags = [regex]::Matches($sourceHead, $tagPattern) | ForEach-Object { $_.Groups[1].Value }
$targetTags = [regex]::Matches($targetText, $tagPattern) | ForEach-Object { $_.Groups[1].Value }
$issuePattern = '^!|^Overfull|^Underfull|LaTeX Warning:|Package .* Warning:|Undefined control sequence|Emergency stop|Fatal error'
$logText = Get-Content -Raw -LiteralPath $engineLog
if ($engineLog -eq $publishedLog) {
  $passes = [regex]::Split($logText, '(?m)^This is pdfTeX')
  $logText = $passes[-1]
}
$issues = @(($logText -split "`r?`n") | Select-String -Pattern $issuePattern)
$placeholders = @([regex]::Matches($targetText, 'TODO|TBD|PLACEHOLDER|XXX|\[\?\]'))
$pdfInfo = & $pdfInfoExe $pdf
$pageMatch = $pdfInfo | Select-String '^Pages:\s+(\d+)$'
$pages = if ($pageMatch) { [int]$pageMatch.Matches[0].Groups[1].Value } else { 0 }
$witnessCount = @(Get-ChildItem -LiteralPath (Join-Path $here 'source_witness') -Filter 'page-*.png' -File).Count
$renderCount = @(Get-ChildItem -LiteralPath (Join-Path $here 'render_check') -Filter 'page-*.png' -File).Count

$checks = [ordered]@{
  source_formula_tags_equal = (($sourceTags -join '|') -eq ($targetTags -join '|'))
  source_formula_tag_count = $sourceTags.Count
  target_formula_tag_count = $targetTags.Count
  source_witness_page_count = $witnessCount
  source_witness_qa_exists = (Test-Path -LiteralPath (Join-Path $here 'SOURCE_WITNESS_QA.md'))
  output_pdf_exists = (Test-Path -LiteralPath $pdf)
  output_pdf_pages = $pages
  render_page_count = $renderCount
  final_log_issue_count = $issues.Count
  placeholder_count = $placeholders.Count
  source_typo_not_propagated = ($targetText -notmatch '\\mathcal C_X')
}
$pass = $checks.source_formula_tags_equal -and
  ($checks.source_formula_tag_count -eq 13) -and
  ($checks.source_witness_page_count -eq 6) -and
  $checks.source_witness_qa_exists -and
  $checks.output_pdf_exists -and
  ($checks.output_pdf_pages -eq 4) -and
  ($checks.render_page_count -eq 4) -and
  ($checks.final_log_issue_count -eq 0) -and
  ($checks.placeholder_count -eq 0) -and
  $checks.source_typo_not_propagated
$result = [ordered]@{
  schema_version = '1.0'
  tranche = 'SGA6_X_ES_T001'
  checked_at = (Get-Date).ToString('o')
  pass = $pass
  checks = $checks
  status = if ($pass) { 'pass_internal_structural_build_visual_bundle' } else { 'fail' }
  external_review = $false
  native_review = $false
}
$result | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath (Join-Path $here 'QA_VALIDATION_CURRENT.json') -Encoding utf8
$result | ConvertTo-Json -Depth 5
if (-not $pass) { exit 1 }
