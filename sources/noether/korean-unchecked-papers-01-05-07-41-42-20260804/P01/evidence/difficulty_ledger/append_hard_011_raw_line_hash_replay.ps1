$ErrorActionPreference = 'Stop'

$dir = $PSScriptRoot
$jsonl = Join-Path $dir 'DIFFICULTY_LEDGER.jsonl'
$csv = Join-Path $dir 'DIFFICULTY_LEDGER.csv'
$id = 'CJK-KO-P01-HARD-011'
$existingLines = [System.IO.File]::ReadAllLines($jsonl, [System.Text.UTF8Encoding]::new($false))
if ($existingLines -match $id) { throw "Append record already exists: $id" }
$last = $existingLines[-1] | ConvertFrom-Json -Depth 20

$record = [ordered]@{
    schema_version = '1.0'
    issue_id = $id
    recorded_at = '2026-08-04T04:26:56.0029631+02:00'
    time_precision = '100 ns-format clock string captured after second failed validator report preservation; actual system precision not independently established'
    work_id = 'NOE-P01'
    unit_ids = @('U01','U02','U03')
    source_locators = @('difficulty-ledger raw JSONL line bytes through HARD-010')
    target_locators = @('validate_difficulty_ledger.ps1 raw-line replay; rejected_attempts/DIFFICULTY_LEDGER_VALIDATION_REPORT_failed_reserialization_edge_20260804.json')
    symptom = 'The first canonicalization repair validated HARD-001 through HARD-009 but still reported a record hash mismatch for newly appended HARD-010.'
    cause_evidence = @(
        'The second failed report is 732 bytes, SHA-256 5169E6C2963EDEC3635AB7DB03C72E238FD4B225584D9BCADCD0D7A2A03EA0F0.',
        'Parse-and-reserialize replay is not guaranteed to reproduce the exact JSON bytes emitted by the append tool.',
        'The ledger convention is byte-level: hash the emitted ordered JSON with only the terminal self-hash value represented as null.',
        'No source or Korean TeX file changed.'
    )
    attempts_and_rejections = @(
        'Rejected rewriting HARD-010 or normalizing the entire ledger.',
        'Preserved the second failed report before modifying the validator.',
        'Replaced object reserialization with exact raw-line replay and a terminal self-hash-to-null substitution.',
        'Appended this second correction so both failed validator approaches remain visible.'
    )
    state = 'resolved'
    resolution_or_hold = 'Validator now hashes exact emitted line bytes with the terminal record_sha256 replaced by null; all earlier JSONL bytes remain unchanged.'
    artifact_hashes = @(
        '5169E6C2963EDEC3635AB7DB03C72E238FD4B225584D9BCADCD0D7A2A03EA0F0',
        'FB5ADA95D0805765F16C4D248699F41C09DD755F9D739EC3E0661E21441F3312',
        '9709B0CE22BC6AD0D88ED084A351930BE3C90CE6E99587C78686E51648896037'
    )
    tests_renders_reviews = [ordered]@{
        source_check = 'absent'; korean_review = 'absent'; formula_check = 'absent'; completeness_check = 'absent'
        compile = 'absent'; render = 'absent'; visual_review = 'absent'; human_or_external_review = 'absent'
        metadata_difficulty_validator = 'two failed reports preserved; exact raw-line replay follows this append'
    }
    residual_risk = 'Append tools must keep record_sha256 as the terminal property and hash the same raw UTF-8 no-BOM JSON convention.'
    recurrence_cues = @('single new record mismatch after prior records pass','parse-reserialize byte drift','terminal self-hash convention')
    related_decision_ids = @('CJK-KO-P01-003')
    related_structural_ids = @('NOE-P01-KO-WORK-001')
    transferable_lesson = 'For append-only evidence chains, validate the exact persisted bytes rather than a semantically equivalent object reserialization; canonical JSON needs an explicit byte-level specification.'
    claim_typing = [ordered]@{
        source_fact = 'exact persisted JSONL and rejected reports'; computation = 'raw-line SHA-256 replay and chain comparison'
        editorial_inference = 'classification as serialization-byte drift'; model_preference = 'none in Korean text'
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
