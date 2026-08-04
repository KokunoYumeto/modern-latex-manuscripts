$ErrorActionPreference = 'Stop'
$ledgerPath = Join-Path $PSScriptRoot 'difficulty_ledger.jsonl'
$csvPath = Join-Path $PSScriptRoot 'difficulty_ledger.csv'
$schemaPath = Join-Path $PSScriptRoot 'DIFFICULTY_LEDGER_SCHEMA.json'
$errors = [System.Collections.Generic.List[string]]::new()
$required = @('schema_version','record_id','recorded_at','time_precision','append_sequence','previous_record_sha256','work_id','unit_ids','authority','targets','category','sense_window','fact_classes','symptom','cause_evidence','attempted_approaches','rejected_approaches','resolution_state','resolution','evidence','residual_risk','recurrence_cues','mandarin_simplified_dominance_risk','lexical_attractor_basin','related_decision_ids','related_structural_ids','transferable_lesson','review_state','supersession_state','revisit_condition','record_sha256')
$validTimePrecision = @('day','minute','second')
$validFactClasses = @('source_fact','computation','editorial_inference','model_preference','external_or_human_validation')
$validResolutionStates = @('held','active_control','resolved')
$validDominanceStates = @('not_applicable','active_qualitative_control','evidence_debt')
$validLexicalBasins = @('Sino-xenic inherited','modern Sino-xenic coinage/calque','global modern loan','native coinage','mixed/contested','unresolved','not_applicable')
$validSupersessionStates = @('current','superseded_by_append')

try { $null = Get-Content -LiteralPath $schemaPath -Raw -Encoding UTF8 | ConvertFrom-Json } catch { $errors.Add("schema parse failure: $($_.Exception.Message)") }
$lines = @(Get-Content -LiteralPath $ledgerPath -Encoding UTF8 | Where-Object { $_.Length -gt 0 })
$records = @()
$previous = $null
$seen = @{}
for ($i = 0; $i -lt $lines.Count; $i++) {
    $line = $lines[$i]
    try { $record = $line | ConvertFrom-Json } catch { $errors.Add("line $($i+1) JSON parse failure: $($_.Exception.Message)"); continue }
    $records += $record
    foreach ($field in $required) { if (-not ($record.PSObject.Properties.Name -contains $field)) { $errors.Add("line $($i+1) missing $field") } }
    $expectedId = 'CJK-KO-P03-HARD-{0:D3}' -f ($i + 1)
    if ($record.record_id -ne $expectedId) { $errors.Add("line $($i+1) id $($record.record_id) != $expectedId") }
    if ($seen.ContainsKey($record.record_id)) { $errors.Add("duplicate id $($record.record_id)") } else { $seen[$record.record_id] = $true }
    if ([int]$record.append_sequence -ne ($i + 1)) { $errors.Add("$($record.record_id) append_sequence mismatch") }
    if ($i -eq 0) { if ($null -ne $record.previous_record_sha256) { $errors.Add("first record previous hash must be null") } }
    elseif ($record.previous_record_sha256 -ne $previous) { $errors.Add("$($record.record_id) previous hash mismatch") }
    if ($record.schema_version -ne '1.0.0') { $errors.Add("$($record.record_id) schema_version mismatch") }
    if ($record.work_id -ne 'NOE-P03-KO') { $errors.Add("$($record.record_id) work_id mismatch") }
    if ($record.review_state -ne 'producer_metadata_unchecked') { $errors.Add("$($record.record_id) review_state mismatch") }
    if ($record.recorded_at -notmatch '^[0-9]{4}-[0-9]{2}-[0-9]{2}$') { $errors.Add("$($record.record_id) recorded_at malformed") }
    if ($validTimePrecision -notcontains $record.time_precision) { $errors.Add("$($record.record_id) time_precision outside controlled values") }
    if ($validResolutionStates -notcontains $record.resolution_state) { $errors.Add("$($record.record_id) resolution_state outside controlled values") }
    if ($validSupersessionStates -notcontains $record.supersession_state) { $errors.Add("$($record.record_id) supersession_state outside controlled values") }
    foreach ($factClass in @($record.fact_classes)) {
        if ($validFactClasses -notcontains $factClass) { $errors.Add("$($record.record_id) fact_class outside controlled values: $factClass") }
    }
    if ($record.record_id -eq 'CJK-KO-P03-HARD-011') {
        if ($record.mandarin_simplified_dominance_risk -ne 'interpolation' -or $record.lexical_attractor_basin -ne 'syntax. -RecurrenceCues @(JavaScript') {
            $errors.Add('HARD-011 does not match its exact documented historical-malformation witness')
        }
    }
    else {
        if ($validDominanceStates -notcontains $record.mandarin_simplified_dominance_risk) { $errors.Add("$($record.record_id) Mandarin-Simplified dominance field outside controlled values") }
        if ($validLexicalBasins -notcontains $record.lexical_attractor_basin) { $errors.Add("$($record.record_id) lexical-attractor basin outside controlled values") }
    }
    if ($record.authority.snapshot_sha256 -notmatch '^[A-F0-9]{64}$') { $errors.Add("$($record.record_id) authority snapshot hash malformed") }
    foreach ($target in @($record.targets)) { if ($null -ne $target.sha256 -and $target.sha256 -notmatch '^[A-F0-9]{64}$') { $errors.Add("$($record.record_id) target hash malformed: $($target.artifact_id)") } }
    if ($line -notmatch '"record_sha256":"[A-F0-9]{64}"\}$') { $errors.Add("$($record.record_id) record_sha256 is not final property") }
    else {
        $placeholder = $line -replace '"record_sha256":"[A-F0-9]{64}"\}$','"record_sha256":null}'
        $bytes = [Text.Encoding]::UTF8.GetBytes($placeholder)
        $actual = [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($bytes))
        if ($actual -ne $record.record_sha256) { $errors.Add("$($record.record_id) self hash mismatch") }
    }
    $previous = $record.record_sha256
}

$hard013 = @($records | Where-Object { $_.record_id -eq 'CJK-KO-P03-HARD-013' })
if ($hard013.Count -ne 1 -or $hard013[0].category -ne 'metadata_integrity_failure' -or $hard013[0].resolution -notmatch 'corrects HARD-011 by append') {
    $errors.Add('Missing or malformed append-only HARD-013 correction for the HARD-011 historical witness')
}
$hard014 = @($records | Where-Object { $_.record_id -eq 'CJK-KO-P03-HARD-014' })
if ($hard014.Count -ne 1 -or $hard014[0].resolution_state -ne 'resolved' -or $hard014[0].symptom -notmatch 'HARD-012') {
    $errors.Add('Missing or malformed HARD-014 resolution successor for HARD-012')
}

$csvRows = @(Import-Csv -LiteralPath $csvPath -Encoding UTF8)
if ($csvRows.Count -ne $records.Count) { $errors.Add("CSV row count $($csvRows.Count) != JSONL record count $($records.Count)") }
for ($i = 0; $i -lt [Math]::Min($csvRows.Count,$records.Count); $i++) {
    if ($csvRows[$i].record_id -ne $records[$i].record_id) { $errors.Add("CSV record_id mismatch at row $($i+1)") }
    if ($csvRows[$i].record_sha256 -ne $records[$i].record_sha256) { $errors.Add("CSV record_sha256 mismatch at row $($i+1)") }
}

$report = [ordered]@{
    schema_version = '1.0.0'
    validator = 'validate_difficulty_ledger.ps1'
    status = $(if ($errors.Count -eq 0) { 'PASS' } else { 'FAIL' })
    record_count = $records.Count
    latest_record_id = $(if ($records.Count) { $records[-1].record_id } else { $null })
    chain_head_sha256 = $(if ($records.Count) { $records[-1].record_sha256 } else { $null })
    csv_row_count = $csvRows.Count
    errors = @($errors)
    validation_scope = 'schema parse; required fields; stable ID and append sequence; exact raw-line self hashes and previous-hash chain; authority/target hash forms; controlled time, fact, resolution, supersession, dominance-risk, and lexical-basin values; exact documented HARD-011 historical exception plus HARD-013 correction and HARD-014 resolution; CSV identity projection'
    excluded_scope = 'No source, Korean, formula, compilation, rendering, publication, or rights review.'
}
$report | ConvertTo-Json -Depth 6
if ($errors.Count -gt 0) { exit 1 }
