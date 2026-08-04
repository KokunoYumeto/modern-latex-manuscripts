$ErrorActionPreference = 'Stop'
$ledgerPath = Join-Path $PSScriptRoot 'difficulty_ledger.jsonl'
$csvPath = Join-Path $PSScriptRoot 'difficulty_ledger.csv'
$lines = @(Get-Content -LiteralPath $ledgerPath -Encoding UTF8 | Where-Object { $_.Length -gt 0 })
$records = @($lines | ForEach-Object { $_ | ConvertFrom-Json })
if ($records.Count -ne 15 -or $records[-1].record_id -ne 'CJK-KO-P41-HARD-015') {
  throw "Expected 15-record predecessor ending in CJK-KO-P41-HARD-015; found $($records.Count) / $($records[-1].record_id)"
}

$obj = [ordered]@{
  schema_version='1.0.0'; record_id='CJK-KO-P41-HARD-016'; recorded_at='2026-08-04'; time_precision='day'; append_sequence=16
  previous_record_sha256=$records[-1].record_sha256; work_id='NOE-P41-KO'; unit_ids=@('U01','U02','U03','U04','U05','U06','U07','U08','U09','U10','U11','U12')
  authority=$records[0].authority; targets=@(); category='tooling_failure_recurrence'; sense_window='Producer handoff evidence inventory performed after HARD-011 had already documented the unsafe foreach-to-pipeline shape.'
  fact_classes=@('source_fact','computation'); symptom='A handoff inventory command again failed at parse time with the already-known direct foreach-to-pipeline pattern; no write occurred.'
  cause_evidence=@(
    [ordered]@{kind='source_fact';detail='The independent metadata worker reported the same parser failure while sweeping P41 evidence for the checker handoff.';path=$null;sha256=$null},
    [ordered]@{kind='computation';detail='Retrying with an explicit intermediate array succeeded, confirming recurrence of HARD-011 rather than a new source or translation issue.';path=$null;sha256=$null}
  )
  attempted_approaches=@(
    [ordered]@{approach='Pipe output directly from a foreach statement during the handoff sweep.';outcome='ParserError before any write.';status='failed'},
    [ordered]@{approach='Collect objects in an explicit array, then pipe the completed array.';outcome='Inventory succeeded.';status='accepted'}
  )
  rejected_approaches=@('Do not dismiss a repeated parser error merely because HARD-011 already described the pattern.')
  resolution_state='resolved'; resolution='Use the explicit-array command shape; cross-link this recurrence to HARD-011 in the handoff.'
  evidence=@([ordered]@{kind='worker_return';detail='P41 handoff worker reported the recurrence and confirmed no write before the successful retry.';path=$null;sha256=$null})
  residual_risk='The unsafe compact idiom remains habitual across parallel metadata workers.'; recurrence_cues=@('foreach statement followed immediately by pipe','empty pipe element or ParserError','successful retry with explicit array')
  mandarin_simplified_dominance_risk='not_applicable'; lexical_attractor_basin='not_applicable'; related_decision_ids=@('CJK-KO-P41-002','CJK-KO-P41-004'); related_structural_ids=@('NOE-P41-KO-WORK-001')
  transferable_lesson='Repeated failures are stronger methodology evidence than a one-off repair; carry the safe command shape into every worker handoff.'; review_state='producer_metadata_unchecked'; supersession_state='current'
  revisit_condition='Recur whenever another worker attempts a direct foreach-to-pipeline expression.'; record_sha256=$null
}
$placeholder=$obj | ConvertTo-Json -Compress -Depth 20
$suffix='"record_sha256":null}'
if(-not $placeholder.EndsWith($suffix)){throw 'record_sha256 is not final'}
$hash=[Convert]::ToHexString([Security.Cryptography.SHA256]::HashData([Text.Encoding]::UTF8.GetBytes($placeholder)))
$line=$placeholder.Substring(0,$placeholder.Length-$suffix.Length)+'"record_sha256":"'+$hash+'"}'
[IO.File]::AppendAllText($ledgerPath,$line+"`n",[Text.UTF8Encoding]::new($false))
$rows=@(Import-Csv -LiteralPath $csvPath -Encoding UTF8)
$rows += [pscustomobject]@{record_id=$obj.record_id;append_sequence=$obj.append_sequence;recorded_at=$obj.recorded_at;unit_ids=($obj.unit_ids -join ';');category=$obj.category;resolution_state=$obj.resolution_state;symptom=$obj.symptom;residual_risk=$obj.residual_risk;mandarin_simplified_dominance_risk=$obj.mandarin_simplified_dominance_risk;lexical_attractor_basin=$obj.lexical_attractor_basin;related_decision_ids=($obj.related_decision_ids -join ';');related_structural_ids=($obj.related_structural_ids -join ';');previous_record_sha256=$obj.previous_record_sha256;record_sha256=$hash;review_state=$obj.review_state;revisit_condition=$obj.revisit_condition}
$rows | Export-Csv -LiteralPath $csvPath -NoTypeInformation -Encoding utf8
Write-Output "appended $($obj.record_id) $hash"
