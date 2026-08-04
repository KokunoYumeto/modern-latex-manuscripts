$ErrorActionPreference = 'Stop'

$dir = $PSScriptRoot
$jsonl = Join-Path $dir 'DIFFICULTY_LEDGER.jsonl'
$csv = Join-Path $dir 'DIFFICULTY_LEDGER.csv'
$reportPath = Join-Path $dir 'DIFFICULTY_LEDGER_VALIDATION_REPORT.json'
$required = @('schema_version','issue_id','recorded_at','time_precision','work_id','unit_ids','source_locators','target_locators','symptom','cause_evidence','attempts_and_rejections','state','resolution_or_hold','artifact_hashes','tests_renders_reviews','residual_risk','recurrence_cues','related_decision_ids','related_structural_ids','transferable_lesson','claim_typing','previous_record_sha256','record_sha256')
$errors = [System.Collections.Generic.List[string]]::new()
$records = [System.Collections.Generic.List[object]]::new()
$rawLines = [System.Collections.Generic.List[string]]::new()
$lineNumber = 0
foreach ($line in [System.IO.File]::ReadAllLines($jsonl, [System.Text.UTF8Encoding]::new($false))) {
    $lineNumber++
    if ([string]::IsNullOrWhiteSpace($line)) { continue }
    try { $record = $line | ConvertFrom-Json -Depth 20 }
    catch { $errors.Add("invalid JSON at line ${lineNumber}: $($_.Exception.Message)"); continue }
    foreach ($field in $required) { if (-not ($record.PSObject.Properties.Name -contains $field)) { $errors.Add("missing $field at line $lineNumber") } }
    $records.Add($record)
    $rawLines.Add($line)
}

$ids = @($records.issue_id)
if (($ids | Sort-Object -Unique).Count -ne $ids.Count) { $errors.Add('duplicate issue_id') }
$previous = $null
$utf8 = [System.Text.UTF8Encoding]::new($false)
$sha = [System.Security.Cryptography.SHA256]::Create()
try {
    for ($index = 0; $index -lt $records.Count; $index++) {
        $record = $records[$index]
        if ($record.previous_record_sha256 -ne $previous) { $errors.Add("chain predecessor mismatch at $($record.issue_id)") }
        $canonical = [regex]::Replace($rawLines[$index], '"record_sha256":"[A-F0-9]{64}"\}$', '"record_sha256":null}')
        if ($canonical -eq $rawLines[$index]) { $errors.Add("terminal self-hash placeholder not found at $($record.issue_id)") }
        $computed = ([System.BitConverter]::ToString($sha.ComputeHash($utf8.GetBytes($canonical)))).Replace('-', '')
        $sha.Initialize()
        if ($computed -ne $record.record_sha256) { $errors.Add("record hash mismatch at $($record.issue_id)") }
        $previous = $record.record_sha256
        if ($record.tests_renders_reviews.korean_review -ne 'absent' -or $record.tests_renders_reviews.render -ne 'absent') { $errors.Add("role-boundary state mismatch at $($record.issue_id)") }
    }
}
finally { $sha.Dispose() }

$csvRows = Import-Csv -LiteralPath $csv
if ($csvRows.Count -ne $records.Count) { $errors.Add("CSV row count $($csvRows.Count) differs from JSONL record count $($records.Count)") }
$stateCounts = [ordered]@{}
foreach ($group in ($records | Group-Object state | Sort-Object Name)) { $stateCounts[$group.Name] = $group.Count }
$report = [ordered]@{
    schema = 'DIFFICULTY_LEDGER.schema.json'; generated_at = (Get-Date -Format o)
    status = if ($errors.Count -eq 0) { 'pass' } else { 'fail' }
    record_count = $records.Count; unique_issue_count = ($ids | Sort-Object -Unique).Count
    state_counts = $stateCounts; chain_head = $previous
    jsonl_sha256 = (Get-FileHash -LiteralPath $jsonl -Algorithm SHA256).Hash
    csv_sha256 = (Get-FileHash -LiteralPath $csv -Algorithm SHA256).Hash
    errors = @($errors)
    scope_note = 'Schema/chain/projection validation only; no source, Korean, mathematics, formula, build, render, or external review.'
}
[System.IO.File]::WriteAllText($reportPath, ($report | ConvertTo-Json -Depth 8), [System.Text.UTF8Encoding]::new($false))
if ($errors.Count -gt 0) { throw "Difficulty ledger validation failed: $($errors -join '; ')" }
Write-Output ($report | ConvertTo-Json -Compress -Depth 8)
