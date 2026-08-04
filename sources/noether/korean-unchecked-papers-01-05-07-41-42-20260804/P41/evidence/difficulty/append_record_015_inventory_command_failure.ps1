$ErrorActionPreference = 'Stop'
$ledgerPath = Join-Path $PSScriptRoot 'difficulty_ledger.jsonl'
$csvPath = Join-Path $PSScriptRoot 'difficulty_ledger.csv'
$lines = @(Get-Content -LiteralPath $ledgerPath -Encoding UTF8 | Where-Object { $_.Length -gt 0 })
$records = @($lines | ForEach-Object { $_ | ConvertFrom-Json })
if ($records.Count -ne 14 -or $records[-1].record_id -ne 'CJK-KO-P41-HARD-014') {
  throw "Expected 14-record predecessor ending in CJK-KO-P41-HARD-014; found $($records.Count) / $($records[-1].record_id)"
}

$firstAuthority = $records[0].authority
$previous = $records[-1].record_sha256
$obj = [ordered]@{
  schema_version = '1.0.0'
  record_id = 'CJK-KO-P41-HARD-015'
  recorded_at = '2026-08-04'
  time_precision = 'day'
  append_sequence = 15
  previous_record_sha256 = $previous
  work_id = 'NOE-P41-KO'
  unit_ids = @('U01','U02','U03','U04','U05','U06','U07','U08','U09','U10','U11','U12')
  authority = $firstAuthority
  targets = @()
  category = 'tooling_failure'
  sense_window = 'PowerShell construction of a literal array of Join-Path calls for an evidence-identity inventory.'
  fact_classes = @('source_fact','computation')
  symptom = 'The inventory command emitted Cannot convert System.Object[] to System.String for AdditionalChildPath and returned no identities.'
  cause_evidence = @(
    [ordered]@{kind='source_fact';detail='A comma-separated set of Join-Path calls was passed inside one array expression without isolating each invocation.';path=$null;sha256=$null},
    [ordered]@{kind='computation';detail='PowerShell bound subsequent array elements to Join-Path AdditionalChildPath instead of treating them as independent array expressions.';path=$null;sha256=$null}
  )
  attempted_approaches = @(
    [ordered]@{approach='Build one array with comma-separated Join-Path invocations.';outcome='Failed during parameter binding; no files changed.';status='failed'},
    [ordered]@{approach='Use explicit full literal paths or parenthesize each independent Join-Path call before hashing.';outcome='Selected safe replacement.';status='accepted'}
  )
  rejected_approaches = @('Do not suppress the binding error or report an incomplete identity inventory.')
  resolution_state = 'resolved'
  resolution = 'Use explicit literal paths for the bounded identity inventory; preserve this failed command in the difficulty chain.'
  evidence = @(
    [ordered]@{kind='command_failure';detail='PowerShell Join-Path parameter-binding error occurred before any write.';path=$null;sha256=$null}
  )
  residual_risk = 'The same construction is easy to repeat in compact PowerShell metadata commands.'
  recurrence_cues = @('Join-Path inside @()','comma-separated command invocations','AdditionalChildPath receives Object[]')
  mandarin_simplified_dominance_risk = 'not_applicable'
  lexical_attractor_basin = 'not_applicable'
  related_decision_ids = @('CJK-KO-P41-004')
  related_structural_ids = @('NOE-P41-KO-WORK-001')
  transferable_lesson = 'In PowerShell arrays, isolate command expressions explicitly; a short failed inventory still belongs in the append-only failure history.'
  review_state = 'producer_metadata_unchecked'
  supersession_state = 'current'
  revisit_condition = 'Recur if a future evidence inventory passes multiple intended paths to one Join-Path invocation.'
  record_sha256 = $null
}

$placeholder = $obj | ConvertTo-Json -Compress -Depth 20
$suffix = '"record_sha256":null}'
if (-not $placeholder.EndsWith($suffix)) { throw 'record_sha256 is not final' }
$hash = [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData([Text.Encoding]::UTF8.GetBytes($placeholder)))
$line = $placeholder.Substring(0,$placeholder.Length-$suffix.Length) + '"record_sha256":"' + $hash + '"}'
[IO.File]::AppendAllText($ledgerPath, $line + "`n", [Text.UTF8Encoding]::new($false))

$rows = @(Import-Csv -LiteralPath $csvPath -Encoding UTF8)
$rows += [pscustomobject]@{
  record_id=$obj.record_id; append_sequence=$obj.append_sequence; recorded_at=$obj.recorded_at; unit_ids=($obj.unit_ids -join ';')
  category=$obj.category; resolution_state=$obj.resolution_state; symptom=$obj.symptom; residual_risk=$obj.residual_risk
  mandarin_simplified_dominance_risk=$obj.mandarin_simplified_dominance_risk; lexical_attractor_basin=$obj.lexical_attractor_basin
  related_decision_ids=($obj.related_decision_ids -join ';'); related_structural_ids=($obj.related_structural_ids -join ';')
  previous_record_sha256=$obj.previous_record_sha256; record_sha256=$hash; review_state=$obj.review_state; revisit_condition=$obj.revisit_condition
}
$rows | Export-Csv -LiteralPath $csvPath -NoTypeInformation -Encoding utf8
Write-Output "appended $($obj.record_id) $hash"
