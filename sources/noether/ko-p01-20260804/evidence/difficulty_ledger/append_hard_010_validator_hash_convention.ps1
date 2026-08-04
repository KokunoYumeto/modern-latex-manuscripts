$ErrorActionPreference = 'Stop'

$dir = $PSScriptRoot
$jsonl = Join-Path $dir 'DIFFICULTY_LEDGER.jsonl'
$csv = Join-Path $dir 'DIFFICULTY_LEDGER.csv'
$id = 'CJK-KO-P01-HARD-010'
$existingLines = [System.IO.File]::ReadAllLines($jsonl, [System.Text.UTF8Encoding]::new($false))
if ($existingLines -match $id) { throw "Append record already exists: $id" }
$last = $existingLines[-1] | ConvertFrom-Json -Depth 20

$record = [ordered]@{
    schema_version = '1.0'
    issue_id = $id
    recorded_at = '2026-08-04T04:25:46.8327010+02:00'
    time_precision = '100 ns-format clock string captured after failed validator report preservation; actual system precision not independently established'
    work_id = 'NOE-P01'
    unit_ids = @('U01','U02','U03')
    source_locators = @('difficulty-ledger JSONL records HARD-001 through HARD-009')
    target_locators = @('validate_difficulty_ledger.ps1 canonical hash replay; rejected_attempts/DIFFICULTY_LEDGER_VALIDATION_REPORT_failed_hash_convention_20260804.json')
    symptom = 'The first validator replay reported record hash mismatch for all nine records after the initializer had successfully written them.'
    cause_evidence = @(
        'Initializer canonicalized each ordered record with record_sha256 present as null before computing its hash.',
        'Validator initially removed record_sha256 entirely, producing a different canonical JSON byte sequence.',
        'Rejected failure report is 1,146 bytes, SHA-256 9709B0CE22BC6AD0D88ED084A351930BE3C90CE6E99587C78686E51648896037.',
        'No source or Korean TeX file changed during either validator invocation.'
    )
    attempts_and_rejections = @(
        'Rejected rewriting the existing nine JSONL records or recomputing their hashes.',
        'Preserved the failed report under rejected_attempts before changing the validator.',
        'Changed validator replay to retain record_sha256 in original property order with a null value.',
        'Appended this correction record rather than silently erasing the failed validation history.'
    )
    state = 'resolved'
    resolution_or_hold = 'Validator canonicalization now matches the initializer convention; existing chain bytes remain untouched.'
    artifact_hashes = @(
        '9709B0CE22BC6AD0D88ED084A351930BE3C90CE6E99587C78686E51648896037',
        'D49EB00C2991CA3B1B837CFD7108E1BCDE79FA35AF2E31D486E90A33B6B7BA07',
        '0499985866E646747EC31533775FF31B55556F2C694F4C2608384829DE248D2F'
    )
    tests_renders_reviews = [ordered]@{
        source_check = 'absent'; korean_review = 'absent'; formula_check = 'absent'; completeness_check = 'absent'
        compile = 'absent'; render = 'absent'; visual_review = 'absent'; human_or_external_review = 'absent'
        metadata_difficulty_validator = 'failed report preserved; corrected replay follows this append'
    }
    residual_risk = 'Any future append tool must preserve the same ordered canonical form, including a null self-hash placeholder during hashing.'
    recurrence_cues = @('all-record hash mismatch','initializer/validator canonicalization drift','null self-hash placeholder')
    related_decision_ids = @('CJK-KO-P01-003')
    related_structural_ids = @('NOE-P01-KO-WORK-001')
    transferable_lesson = 'When hashing self-describing records, specify the self-hash placeholder convention explicitly and test initializer/validator byte identity before interpreting mismatches as data corruption.'
    claim_typing = [ordered]@{
        source_fact = 'exact scripts and preserved failed report'; computation = 'record hashes, bytes, and replay behavior'
        editorial_inference = 'classification as validator-convention failure'; model_preference = 'none in Korean text'
        external_or_human_validation = 'absent'
    }
    previous_record_sha256 = $last.record_sha256
    record_sha256 = $null
}

$utf8 = [System.Text.UTF8Encoding]::new($false)
$sha = [System.Security.Cryptography.SHA256]::Create()
try { $record.record_sha256 = ([System.BitConverter]::ToString($sha.ComputeHash($utf8.GetBytes(($record | ConvertTo-Json -Compress -Depth 10))))).Replace('-', '') }
finally { $sha.Dispose() }
[System.IO.File]::AppendAllText($jsonl, (($record | ConvertTo-Json -Compress -Depth 10) + "`n"), $utf8)

$rows = @(Import-Csv -LiteralPath $csv)
$rows += [pscustomobject]@{
    issue_id = $record.issue_id; recorded_at = $record.recorded_at; work_id = $record.work_id
    unit_ids_json = ($record.unit_ids | ConvertTo-Json -Compress); source_locators_json = ($record.source_locators | ConvertTo-Json -Compress)
    target_locators_json = ($record.target_locators | ConvertTo-Json -Compress); symptom = $record.symptom
    cause_evidence_json = ($record.cause_evidence | ConvertTo-Json -Compress); attempts_and_rejections_json = ($record.attempts_and_rejections | ConvertTo-Json -Compress)
    state = $record.state; resolution_or_hold = $record.resolution_or_hold; artifact_hashes_json = ($record.artifact_hashes | ConvertTo-Json -Compress)
    residual_risk = $record.residual_risk; recurrence_cues_json = ($record.recurrence_cues | ConvertTo-Json -Compress)
    related_decision_ids_json = ($record.related_decision_ids | ConvertTo-Json -Compress)
    related_structural_ids_json = ($record.related_structural_ids | ConvertTo-Json -Compress)
    transferable_lesson = $record.transferable_lesson; previous_record_sha256 = $record.previous_record_sha256; record_sha256 = $record.record_sha256
}
$rows | Export-Csv -LiteralPath $csv -NoTypeInformation -Encoding utf8
Write-Output "appended $id with record SHA-256 $($record.record_sha256)"
