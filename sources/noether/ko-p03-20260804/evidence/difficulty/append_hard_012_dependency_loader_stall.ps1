$ErrorActionPreference='Stop'
$jsonlPath=Join-Path $PSScriptRoot 'difficulty_ledger.jsonl'
$csvPath=Join-Path $PSScriptRoot 'difficulty_ledger.csv'
$records=@(Get-Content -LiteralPath $jsonlPath -Encoding UTF8|Where-Object{$_.Length -gt 0})
$last=$records[-1]|ConvertFrom-Json
if($records.Count -ne 11 -or $last.record_id -ne 'CJK-KO-P03-HARD-011' -or $last.record_sha256 -ne '0297DFDE903E203FF9952BC21485D93B7F75FBAFBD5DC48C556B1A4D691339B8'){throw 'Unexpected append cursor.'}
$authoritySha='D1F06B311F6CBD991DD247D745DD9A72DDE326A20396DF43CFE0C8EDB1593CDB'
$record=[ordered]@{
 schema_version='1.0.0';record_id='CJK-KO-P03-HARD-012';recorded_at='2026-08-04';time_precision='day';append_sequence=12;previous_record_sha256=$last.record_sha256;work_id='NOE-P03-KO';unit_ids=@()
 authority=[ordered]@{path='C:/Users/Floris/Documents/interlanguage/03_projects/noether/07_german_canon_control/candidates/NOETH-DE-ED-0001/Noether_German_NOETH-DE-ED-0001.tex';snapshot_sha256=$authoritySha;historical_whole_source_sha256=$authoritySha;locators=@('CSV reproducibility validation dependency discovery; no source/target content access');unit_slice_sha256=[ordered]@{U01='DF50EAD7065F663901F51ADFCA37A138921063362CA449665D37B855921B496C';U02='A7B7CA981F7B8D6B32171BF0709E27440A25B2754642BD095304E54A5A25D5C6';U03='0D110465AEE20E18EE1427577D33D435FCF97D5CA99BEF3878EF52DC341F01A5'}}
 targets=@();category='tooling_failure';sense_window='Bundled workspace-dependency discovery versus prohibited guessed runtime paths.';fact_classes=@('source_fact','computation');symptom='The exact workspace dependency locator stalled on two consecutive bounded calls and returned no runtime paths.'
 cause_evidence=@([ordered]@{kind='source_fact';detail='First locator call remained running for roughly 2.5 minutes and was terminated; the bounded retry remained running for roughly 1.5 minutes and was terminated.';path=$null;sha256=$null},[ordered]@{kind='computation';detail='Neither call returned Node or node_modules identities, and neither changed any artifact.';path=$null;sha256=$null})
 attempted_approaches=@([ordered]@{approach='Wait through several bounded windows on the first locator call.';outcome='No output; terminated without file change.';status='failed'},[ordered]@{approach='Start one fresh bounded locator retry.';outcome='No output; terminated without file change.';status='failed'},[ordered]@{approach='Guess or search dependency paths.';outcome='Rejected by the spreadsheet skill.';status='rejected'})
 rejected_approaches=@('Guess a global Node path','Search package internals','Install alternate dependencies');resolution_state='held';resolution='CSV artifact-tool validation waits for an exact loader-provided runtime/dependency path; structural/difficulty/visual producers continue without rendering.'
 evidence=@([ordered]@{kind='tool_call';detail='Two terminated dependency-locator calls; no returned path and no file mutation.';path=$null;sha256=$null});residual_risk='CSV projections are not yet independently imported through the required artifact tool.'
 recurrence_cues=@('dependency locator yields no output','artifact-tool runtime unavailable');mandarin_simplified_dominance_risk='not_applicable';lexical_attractor_basin='not_applicable';related_decision_ids=@();related_structural_ids=@('NOE-P03-KO-WORK-001');transferable_lesson='Do not replace a stalled authoritative dependency locator with guessed runtime paths; preserve the stall and seek an exact supplied path.';review_state='producer_metadata_unchecked';supersession_state='current';revisit_condition='Append a resolving successor only when an exact loader-provided Node and node_modules path permits the required artifact-tool validation.';record_sha256=$null
}
$placeholder=$record|ConvertTo-Json -Depth 20 -Compress
$hash=[Convert]::ToHexString([Security.Cryptography.SHA256]::HashData([Text.Encoding]::UTF8.GetBytes($placeholder)))
$record.record_sha256=$hash
$line=$record|ConvertTo-Json -Depth 20 -Compress
[IO.File]::AppendAllText($jsonlPath,$line+[Environment]::NewLine,[Text.UTF8Encoding]::new($false))
$csv=[pscustomobject][ordered]@{record_id='CJK-KO-P03-HARD-012';append_sequence=12;recorded_at='2026-08-04';time_precision='day';category='tooling_failure';unit_ids='';source_locators='CSV reproducibility validation dependency discovery; no source/target content access';target_ids='';resolution_state='held';symptom='The exact workspace dependency locator stalled on two consecutive bounded calls and returned no runtime paths.';residual_risk='CSV projections are not yet independently imported through the required artifact tool.';recurrence_cues='dependency locator yields no output;artifact-tool runtime unavailable';related_decision_ids='';related_structural_ids='NOE-P03-KO-WORK-001';revisit_condition='Append a resolving successor only when an exact loader-provided Node and node_modules path permits the required artifact-tool validation.';record_sha256=$hash}
$csvLine=@($csv|ConvertTo-Csv -NoTypeInformation)[1]
[IO.File]::AppendAllText($csvPath,$csvLine+[Environment]::NewLine,[Text.UTF8Encoding]::new($false))
[pscustomobject]@{record_id='CJK-KO-P03-HARD-012';record_sha256=$hash}|ConvertTo-Json
