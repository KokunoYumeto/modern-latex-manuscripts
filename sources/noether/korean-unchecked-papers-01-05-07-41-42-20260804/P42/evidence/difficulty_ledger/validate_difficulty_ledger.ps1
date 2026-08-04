param()

$ErrorActionPreference = 'Stop'
$utf8 = [System.Text.UTF8Encoding]::new($false)
$jsonlPath = Join-Path $PSScriptRoot 'DIFFICULTY_LEDGER.jsonl'
$csvPath = Join-Path $PSScriptRoot 'DIFFICULTY_LEDGER.csv'
$reportPath = Join-Path $PSScriptRoot 'DIFFICULTY_LEDGER_VALIDATION_REPORT.json'
$errors = [System.Collections.Generic.List[string]]::new()
$records = [System.Collections.Generic.List[object]]::new()
$lineNumber = 0
foreach ($line in [System.IO.File]::ReadAllLines($jsonlPath, $utf8)) {
  $lineNumber++
  if (-not $line.Trim()) { $errors.Add("blank JSONL record at line $lineNumber"); continue }
  try { $record = $line | ConvertFrom-Json -Depth 20 } catch { $errors.Add("invalid JSON at line ${lineNumber}: $($_.Exception.Message)"); continue }
  $records.Add($record)
}
$required = @('difficulty_id','recorded_at','time_precision','work_unit','authority','exact_locators','symptom','claim_types','cause_evidence','attempted_approaches','state','resolution_or_hold','evidence_artifacts','residual_risk','recurrence_cues','related_decision_ids','related_structural_ids','transferable_lesson','review_state')
$seen = @{}
foreach ($record in $records) {
  foreach ($field in $required) { if (-not ($record.PSObject.Properties.Name -contains $field)) { $errors.Add("$($record.difficulty_id) missing $field") } }
  if ($record.difficulty_id -notmatch '^CJK-KO-P42-HARD-[0-9]{3}$') { $errors.Add("bad id $($record.difficulty_id)") }
  if ($seen.ContainsKey($record.difficulty_id)) { $errors.Add("duplicate id $($record.difficulty_id)") } else { $seen[$record.difficulty_id] = $true }
  if ($record.review_state -ne 'producer_record_unreviewed') { $errors.Add("bad review state $($record.difficulty_id)") }
  if ($record.authority.snapshot_sha256 -ne 'B6BB3A6267BA8495FC19914A72768351E4923B13374634701AF3CBDE659883CC') { $errors.Add("bad authority hash $($record.difficulty_id)") }
  if (@($record.exact_locators).Count -lt 1 -or @($record.cause_evidence).Count -lt 1 -or @($record.attempted_approaches).Count -lt 1) { $errors.Add("empty required evidence array $($record.difficulty_id)") }
}
$projection = foreach ($record in $records) {
  [pscustomobject]@{
    difficulty_id = $record.difficulty_id
    recorded_at = $record.recorded_at
    work_unit = $record.work_unit
    state = $record.state
    symptom = $record.symptom
    resolution_or_hold = $record.resolution_or_hold
    residual_risk = $record.residual_risk
    related_decision_ids = (@($record.related_decision_ids) -join ';')
    related_structural_ids = (@($record.related_structural_ids) -join ';')
    review_state = $record.review_state
  }
}
$csvText = $projection | ConvertTo-Csv -NoTypeInformation
[System.IO.File]::WriteAllLines($csvPath, $csvText, $utf8)
$report = [ordered]@{
  status = $(if ($errors.Count -eq 0) { 'pass' } else { 'fail' })
  record_count = $records.Count
  unique_id_count = ($records.difficulty_id | Sort-Object -Unique).Count
  latest_difficulty_id = $(if ($records.Count) { $records[-1].difficulty_id } else { $null })
  states = [ordered]@{
    resolved = @($records | Where-Object state -eq 'resolved').Count
    held = @($records | Where-Object state -eq 'held').Count
    active_control = @($records | Where-Object state -eq 'active_control').Count
  }
  errors = @($errors)
  validation_scope = 'ledger syntax, required fields, identity, and projection integrity only; no source, Korean, build, render, or external validation'
}
[System.IO.File]::WriteAllText($reportPath, ($report | ConvertTo-Json -Depth 8), $utf8)
if ($errors.Count -gt 0) { throw "difficulty ledger validation failed with $($errors.Count) errors" }
$report | ConvertTo-Json -Depth 8
