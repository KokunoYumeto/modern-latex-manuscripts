$ErrorActionPreference = 'Stop'

$dir = $PSScriptRoot
$jsonl = Join-Path $dir 'VISUAL_EVIDENCE_INDEX.jsonl'
$csv = Join-Path $dir 'VISUAL_EVIDENCE_INDEX.csv'
$reportPath = Join-Path $dir 'VISUAL_EVIDENCE_INDEX_VALIDATION_REPORT.json'
$errors = [System.Collections.Generic.List[string]]::new()
$records = [System.Collections.Generic.List[object]]::new()
$lineNumber = 0
foreach ($line in [System.IO.File]::ReadAllLines($jsonl, [System.Text.UTF8Encoding]::new($false))) {
    $lineNumber++
    if ([string]::IsNullOrWhiteSpace($line)) { continue }
    try { $record = $line | ConvertFrom-Json -Depth 20 }
    catch { $errors.Add("invalid JSON at line ${lineNumber}: $($_.Exception.Message)"); continue }
    $records.Add($record)
}
$csvRows = @(Import-Csv -LiteralPath $csv)
if ($csvRows.Count -ne $records.Count) { $errors.Add("CSV data-row count $($csvRows.Count) differs from JSONL count $($records.Count)") }
if ($records.Count -ne 0) { $errors.Add('Paper 1 producer route declares zero visual evidence, but nonzero records exist') }
$report = [ordered]@{
    schema = 'VISUAL_EVIDENCE_INDEX.schema.json'; generated_at = (Get-Date -Format o)
    status = if ($errors.Count -eq 0) { 'pass' } else { 'fail' }
    record_count = $records.Count; public_include_count = 0; rights_blocked_count = 0; private_excluded_count = 0
    paper01_source_equation_diagram_render_contact_before_after_segmentation_overlay_count = 0
    jsonl_sha256 = (Get-FileHash -LiteralPath $jsonl -Algorithm SHA256).Hash
    csv_sha256 = (Get-FileHash -LiteralPath $csv -Algorithm SHA256).Hash
    errors = @($errors)
    continuation_cursor = 'await independent checker; index any later image before use; producer route created no image'
    scope_note = 'Zero-image inventory; no rendering or visual review performed or implied.'
}
[System.IO.File]::WriteAllText($reportPath, ($report | ConvertTo-Json -Depth 8), [System.Text.UTF8Encoding]::new($false))
if ($errors.Count -gt 0) { throw "Visual evidence validation failed: $($errors -join '; ')" }
Write-Output ($report | ConvertTo-Json -Compress -Depth 8)
