[CmdletBinding()]
param()
$ErrorActionPreference = 'Stop'
if($PSVersionTable.PSVersion.Major-lt7){throw 'PowerShell 7 or later required'}
$root=$PSScriptRoot
$utf8=[Text.UTF8Encoding]::new($false)
function Sha([string]$Path){(Get-FileHash -LiteralPath $Path -Algorithm SHA256).Hash}
function Rel([string]$Root,[string]$Path){$Path.Substring($Root.Length+1).Replace('\','/')}
function Identity-Digest([string[]]$Paths){
    $lines=@($Paths|Sort-Object|ForEach-Object{$p=Join-Path $root $_.Replace('/','\');if(-not(Test-Path -LiteralPath $p -PathType Leaf)){throw "Identity input missing: $_"};"$_|$((Get-Item $p).Length)|$(Sha $p)"})
    [BitConverter]::ToString([Security.Cryptography.SHA256]::HashData($utf8.GetBytes(($lines-join[string][char]10)+[string][char]10))).Replace('-','')
}
function Inventory-Digest([string]$Root){
    $lines=@(Get-ChildItem -LiteralPath $Root -Recurse -File|Sort-Object FullName|ForEach-Object{"$(Rel $Root $_.FullName)|$($_.Length)|$(Sha $_.FullName)"})
    [BitConverter]::ToString([Security.Cryptography.SHA256]::HashData($utf8.GetBytes(($lines-join[string][char]10)+[string][char]10))).Replace('-','')
}
$expectedPaths=@(
    'BUILD_LOG_SANITIZATION.md',
    'CHECKPOINT_README.md',
    'CONTINUATION_CURSOR.md',
    'drafts/SGA1_I_5_English_source_draft.texfrag',
    'drafts/SGA1_I_6_English_source_draft.texfrag',
    'drafts/SGA1_I_7_English_source_draft.texfrag',
    'drafts/SGA1_I_8_English_source_draft.texfrag',
    'drafts/SGA1_I_9_1_English_source_draft.texfrag',
    'drafts/SGA1_I_9_2_English_source_draft.texfrag',
    'drafts/SGA1_I_9_3_English_source_draft.texfrag',
    'evidence/BUILD_SOURCE_RENDER_REVIEW_SUMMARY_LOCAL_SEAL_I_9_3.md',
    'evidence/build/COMPILE_PASS1_SANITIZED_FULL.console.txt',
    'evidence/build/COMPILE_PASS1_SANITIZED_FULL.log',
    'evidence/build/COMPILE_PASS2_SANITIZED_FULL.console.txt',
    'evidence/build/COMPILE_PASS2_SANITIZED_FULL.log',
    'evidence/build/COMPILE_PASS3_SANITIZED_FULL.console.txt',
    'evidence/build/COMPILE_PASS3_SANITIZED_FULL.log',
    'evidence/build/UNIQUE_DESTINATION_VALIDATION_I_9_3.txt',
    'evidence/LOCAL_MACHINE_LEDGER_VALIDATION_I_9_3_FINAL.txt',
    'evidence/PREDECESSOR_AND_CUMULATIVE_MACHINE_VALIDATION.txt',
    'evidence/predecessor_i9_2_r2_machine_controls/evidence/predecessor_i9_1_r2_machine_controls/evidence/predecessor_i8_r4_machine_controls/PUBLIC_ADVERSE_AND_REJECTED_CHOICES_I_8.csv',
    'evidence/predecessor_i9_2_r2_machine_controls/evidence/predecessor_i9_1_r2_machine_controls/evidence/predecessor_i8_r4_machine_controls/PUBLIC_ADVERSE_AND_REJECTED_CHOICES.csv',
    'evidence/predecessor_i9_2_r2_machine_controls/evidence/predecessor_i9_1_r2_machine_controls/evidence/predecessor_i8_r4_machine_controls/PUBLIC_AUTHORITY_AND_COVERAGE_I_8.csv',
    'evidence/predecessor_i9_2_r2_machine_controls/evidence/predecessor_i9_1_r2_machine_controls/evidence/predecessor_i8_r4_machine_controls/PUBLIC_AUTHORITY_AND_COVERAGE.csv',
    'evidence/predecessor_i9_2_r2_machine_controls/evidence/predecessor_i9_1_r2_machine_controls/evidence/predecessor_i8_r4_machine_controls/PUBLIC_CSV_ARTIFACT_VALIDATION_I_8.txt',
    'evidence/predecessor_i9_2_r2_machine_controls/evidence/predecessor_i9_1_r2_machine_controls/evidence/predecessor_i8_r4_machine_controls/PUBLIC_INDEX_RESTORATION_DEBT.csv',
    'evidence/predecessor_i9_2_r2_machine_controls/evidence/predecessor_i9_1_r2_machine_controls/evidence/predecessor_i8_r4_machine_controls/PUBLIC_MACHINE_VALIDATION_I_8.txt',
    'evidence/predecessor_i9_2_r2_machine_controls/evidence/predecessor_i9_1_r2_machine_controls/evidence/predecessor_i8_r4_machine_controls/PUBLIC_SGA1_I4_DIFFICULTY_FAILURE_REVISION.jsonl',
    'evidence/predecessor_i9_2_r2_machine_controls/evidence/predecessor_i9_1_r2_machine_controls/evidence/predecessor_i8_r4_machine_controls/PUBLIC_SGA1_I4_EVIDENCE_GRAPH.jsonl',
    'evidence/predecessor_i9_2_r2_machine_controls/evidence/predecessor_i9_1_r2_machine_controls/evidence/predecessor_i8_r4_machine_controls/PUBLIC_SGA1_I5_DIFFICULTY_FAILURE_REVISION.jsonl',
    'evidence/predecessor_i9_2_r2_machine_controls/evidence/predecessor_i9_1_r2_machine_controls/evidence/predecessor_i8_r4_machine_controls/PUBLIC_SGA1_I5_EVIDENCE_GRAPH.jsonl',
    'evidence/predecessor_i9_2_r2_machine_controls/evidence/predecessor_i9_1_r2_machine_controls/evidence/predecessor_i8_r4_machine_controls/PUBLIC_SGA1_I6_DIFFICULTY_FAILURE_REVISION.jsonl',
    'evidence/predecessor_i9_2_r2_machine_controls/evidence/predecessor_i9_1_r2_machine_controls/evidence/predecessor_i8_r4_machine_controls/PUBLIC_SGA1_I6_EVIDENCE_GRAPH.jsonl',
    'evidence/predecessor_i9_2_r2_machine_controls/evidence/predecessor_i9_1_r2_machine_controls/evidence/predecessor_i8_r4_machine_controls/PUBLIC_SGA1_I7_DIFFICULTY_FAILURE_REVISION.jsonl',
    'evidence/predecessor_i9_2_r2_machine_controls/evidence/predecessor_i9_1_r2_machine_controls/evidence/predecessor_i8_r4_machine_controls/PUBLIC_SGA1_I7_EVIDENCE_GRAPH.jsonl',
    'evidence/predecessor_i9_2_r2_machine_controls/evidence/predecessor_i9_1_r2_machine_controls/evidence/predecessor_i8_r4_machine_controls/PUBLIC_SGA1_I8_DIFFICULTY_FAILURE_REVISION.jsonl',
    'evidence/predecessor_i9_2_r2_machine_controls/evidence/predecessor_i9_1_r2_machine_controls/evidence/predecessor_i8_r4_machine_controls/PUBLIC_SGA1_I8_EVIDENCE_GRAPH.jsonl',
    'evidence/predecessor_i9_2_r2_machine_controls/evidence/predecessor_i9_1_r2_machine_controls/evidence/predecessor_i8_r4_machine_controls/PUBLIC_SGA1_MACHINE_LEDGER_SCHEMA_v5.json',
    'evidence/predecessor_i9_2_r2_machine_controls/evidence/predecessor_i9_1_r2_machine_controls/evidence/predecessor_i8_r4_machine_controls/PUBLIC_SGA1_NORMALIZATION_DELTA_I_8.csv',
    'evidence/predecessor_i9_2_r2_machine_controls/evidence/predecessor_i9_1_r2_machine_controls/evidence/predecessor_i8_r4_machine_controls/PUBLIC_SGA1_NORMALIZATION_DELTA.csv',
    'evidence/predecessor_i9_2_r2_machine_controls/evidence/predecessor_i9_1_r2_machine_controls/evidence/predecessor_i8_r4_machine_controls/PUBLIC_SOURCE_COMPARISON_I_0_1.csv',
    'evidence/predecessor_i9_2_r2_machine_controls/evidence/predecessor_i9_1_r2_machine_controls/evidence/predecessor_i8_r4_machine_controls/PUBLIC_SOURCE_COMPARISON_I_2.csv',
    'evidence/predecessor_i9_2_r2_machine_controls/evidence/predecessor_i9_1_r2_machine_controls/evidence/predecessor_i8_r4_machine_controls/PUBLIC_SOURCE_COMPARISON_I_3.csv',
    'evidence/predecessor_i9_2_r2_machine_controls/evidence/predecessor_i9_1_r2_machine_controls/evidence/predecessor_i8_r4_machine_controls/PUBLIC_SOURCE_COMPARISON_I_4.csv',
    'evidence/predecessor_i9_2_r2_machine_controls/evidence/predecessor_i9_1_r2_machine_controls/evidence/predecessor_i8_r4_machine_controls/PUBLIC_SOURCE_COMPARISON_I_5.csv',
    'evidence/predecessor_i9_2_r2_machine_controls/evidence/predecessor_i9_1_r2_machine_controls/evidence/predecessor_i8_r4_machine_controls/PUBLIC_SOURCE_COMPARISON_I_6.csv',
    'evidence/predecessor_i9_2_r2_machine_controls/evidence/predecessor_i9_1_r2_machine_controls/evidence/predecessor_i8_r4_machine_controls/PUBLIC_SOURCE_COMPARISON_I_7.csv',
    'evidence/predecessor_i9_2_r2_machine_controls/evidence/predecessor_i9_1_r2_machine_controls/evidence/predecessor_i8_r4_machine_controls/PUBLIC_SOURCE_COMPARISON_I_8.csv',
    'evidence/predecessor_i9_2_r2_machine_controls/evidence/predecessor_i9_1_r2_machine_controls/evidence/predecessor_i8_r4_machine_controls/PUBLIC_SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_0_1.csv',
    'evidence/predecessor_i9_2_r2_machine_controls/evidence/predecessor_i9_1_r2_machine_controls/evidence/predecessor_i8_r4_machine_controls/PUBLIC_SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_2.csv',
    'evidence/predecessor_i9_2_r2_machine_controls/evidence/predecessor_i9_1_r2_machine_controls/evidence/predecessor_i8_r4_machine_controls/PUBLIC_SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_3.csv',
    'evidence/predecessor_i9_2_r2_machine_controls/evidence/predecessor_i9_1_r2_machine_controls/evidence/predecessor_i8_r4_machine_controls/PUBLIC_SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_4.csv',
    'evidence/predecessor_i9_2_r2_machine_controls/evidence/predecessor_i9_1_r2_machine_controls/evidence/predecessor_i8_r4_machine_controls/PUBLIC_SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_5.csv',
    'evidence/predecessor_i9_2_r2_machine_controls/evidence/predecessor_i9_1_r2_machine_controls/evidence/predecessor_i8_r4_machine_controls/PUBLIC_SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_6.csv',
    'evidence/predecessor_i9_2_r2_machine_controls/evidence/predecessor_i9_1_r2_machine_controls/evidence/predecessor_i8_r4_machine_controls/PUBLIC_SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_7.csv',
    'evidence/predecessor_i9_2_r2_machine_controls/evidence/predecessor_i9_1_r2_machine_controls/evidence/predecessor_i8_r4_machine_controls/PUBLIC_SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_8.csv',
    'evidence/predecessor_i9_2_r2_machine_controls/evidence/predecessor_i9_1_r2_machine_controls/ledgers/ADVERSE_AND_REJECTED_CHOICES.csv',
    'evidence/predecessor_i9_2_r2_machine_controls/evidence/predecessor_i9_1_r2_machine_controls/ledgers/AUTHORITY_AND_PROVENANCE.csv',
    'evidence/predecessor_i9_2_r2_machine_controls/evidence/predecessor_i9_1_r2_machine_controls/ledgers/CANDIDATE_COVERAGE_V2.csv',
    'evidence/predecessor_i9_2_r2_machine_controls/evidence/predecessor_i9_1_r2_machine_controls/ledgers/INDEX_RESTORATION_DEBT.csv',
    'evidence/predecessor_i9_2_r2_machine_controls/evidence/predecessor_i9_1_r2_machine_controls/ledgers/PUBLIC_CSV_ARTIFACT_VALIDATION_I_9_1.txt',
    'evidence/predecessor_i9_2_r2_machine_controls/evidence/predecessor_i9_1_r2_machine_controls/ledgers/PUBLIC_MACHINE_VALIDATION_I_9_1.txt',
    'evidence/predecessor_i9_2_r2_machine_controls/evidence/predecessor_i9_1_r2_machine_controls/ledgers/SGA1_DIFFICULTY_FAILURE_REVISION.jsonl',
    'evidence/predecessor_i9_2_r2_machine_controls/evidence/predecessor_i9_1_r2_machine_controls/ledgers/SGA1_I9_1_EVIDENCE_GRAPH.jsonl',
    'evidence/predecessor_i9_2_r2_machine_controls/evidence/predecessor_i9_1_r2_machine_controls/ledgers/SGA1_MACHINE_LEDGER_SCHEMA_v1.json',
    'evidence/predecessor_i9_2_r2_machine_controls/evidence/predecessor_i9_1_r2_machine_controls/ledgers/SGA1_NORMALIZATION_DELTA.csv',
    'evidence/predecessor_i9_2_r2_machine_controls/evidence/predecessor_i9_1_r2_machine_controls/ledgers/SOURCE_COMPARISON_I_4.csv',
    'evidence/predecessor_i9_2_r2_machine_controls/evidence/predecessor_i9_1_r2_machine_controls/ledgers/SOURCE_COMPARISON_I_5.csv',
    'evidence/predecessor_i9_2_r2_machine_controls/evidence/predecessor_i9_1_r2_machine_controls/ledgers/SOURCE_COMPARISON_I_6.csv',
    'evidence/predecessor_i9_2_r2_machine_controls/evidence/predecessor_i9_1_r2_machine_controls/ledgers/SOURCE_COMPARISON_I_7.csv',
    'evidence/predecessor_i9_2_r2_machine_controls/evidence/predecessor_i9_1_r2_machine_controls/ledgers/SOURCE_COMPARISON_I_8.csv',
    'evidence/predecessor_i9_2_r2_machine_controls/evidence/predecessor_i9_1_r2_machine_controls/ledgers/SOURCE_COMPARISON_I_9_1.csv',
    'evidence/predecessor_i9_2_r2_machine_controls/evidence/predecessor_i9_1_r2_machine_controls/ledgers/SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_4.csv',
    'evidence/predecessor_i9_2_r2_machine_controls/evidence/predecessor_i9_1_r2_machine_controls/ledgers/SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_5.csv',
    'evidence/predecessor_i9_2_r2_machine_controls/evidence/predecessor_i9_1_r2_machine_controls/ledgers/SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_6.csv',
    'evidence/predecessor_i9_2_r2_machine_controls/evidence/predecessor_i9_1_r2_machine_controls/ledgers/SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_7.csv',
    'evidence/predecessor_i9_2_r2_machine_controls/evidence/predecessor_i9_1_r2_machine_controls/ledgers/SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_8.csv',
    'evidence/predecessor_i9_2_r2_machine_controls/evidence/predecessor_i9_1_r2_machine_controls/ledgers/SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_9_1.csv',
    'evidence/predecessor_i9_2_r2_machine_controls/ledgers/ADVERSE_AND_REJECTED_CHOICES.csv',
    'evidence/predecessor_i9_2_r2_machine_controls/ledgers/AUTHORITY_AND_PROVENANCE.csv',
    'evidence/predecessor_i9_2_r2_machine_controls/ledgers/CANDIDATE_COVERAGE_V2.csv',
    'evidence/predecessor_i9_2_r2_machine_controls/ledgers/INDEX_RESTORATION_DEBT.csv',
    'evidence/predecessor_i9_2_r2_machine_controls/ledgers/PUBLIC_CSV_ARTIFACT_VALIDATION_I_9_2.txt',
    'evidence/predecessor_i9_2_r2_machine_controls/ledgers/PUBLIC_MACHINE_VALIDATION_I_9_2.txt',
    'evidence/predecessor_i9_2_r2_machine_controls/ledgers/SGA1_DIFFICULTY_FAILURE_REVISION.jsonl',
    'evidence/predecessor_i9_2_r2_machine_controls/ledgers/SGA1_I9_2_EVIDENCE_GRAPH.jsonl',
    'evidence/predecessor_i9_2_r2_machine_controls/ledgers/SGA1_MACHINE_LEDGER_SCHEMA_v1.json',
    'evidence/predecessor_i9_2_r2_machine_controls/ledgers/SGA1_NORMALIZATION_DELTA.csv',
    'evidence/predecessor_i9_2_r2_machine_controls/ledgers/SOURCE_COMPARISON_I_4.csv',
    'evidence/predecessor_i9_2_r2_machine_controls/ledgers/SOURCE_COMPARISON_I_5.csv',
    'evidence/predecessor_i9_2_r2_machine_controls/ledgers/SOURCE_COMPARISON_I_6.csv',
    'evidence/predecessor_i9_2_r2_machine_controls/ledgers/SOURCE_COMPARISON_I_7.csv',
    'evidence/predecessor_i9_2_r2_machine_controls/ledgers/SOURCE_COMPARISON_I_8.csv',
    'evidence/predecessor_i9_2_r2_machine_controls/ledgers/SOURCE_COMPARISON_I_9_1.csv',
    'evidence/predecessor_i9_2_r2_machine_controls/ledgers/SOURCE_COMPARISON_I_9_2.csv',
    'evidence/predecessor_i9_2_r2_machine_controls/ledgers/SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_4.csv',
    'evidence/predecessor_i9_2_r2_machine_controls/ledgers/SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_5.csv',
    'evidence/predecessor_i9_2_r2_machine_controls/ledgers/SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_6.csv',
    'evidence/predecessor_i9_2_r2_machine_controls/ledgers/SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_7.csv',
    'evidence/predecessor_i9_2_r2_machine_controls/ledgers/SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_8.csv',
    'evidence/predecessor_i9_2_r2_machine_controls/ledgers/SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_9_1.csv',
    'evidence/predecessor_i9_2_r2_machine_controls/ledgers/SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_9_2.csv',
    'evidence/PREDECESSOR_I9_2_R2_PORTABLE_VERIFY.txt',
    'evidence/rendered_pdf/page-01.png',
    'evidence/rendered_pdf/page-02.png',
    'evidence/rendered_pdf/page-03.png',
    'evidence/rendered_pdf/page-04.png',
    'evidence/rendered_pdf/page-05.png',
    'evidence/rendered_pdf/page-06.png',
    'evidence/rendered_pdf/page-07.png',
    'evidence/rendered_pdf/page-08.png',
    'evidence/rendered_pdf/page-09.png',
    'evidence/rendered_pdf/page-10.png',
    'evidence/rendered_pdf/page-11.png',
    'evidence/rendered_pdf/page-12.png',
    'evidence/rendered_pdf/page-13.png',
    'evidence/rendered_pdf/page-14.png',
    'evidence/rendered_pdf/page-15.png',
    'evidence/rendered_pdf/page-16.png',
    'evidence/rendered_pdf/page-17.png',
    'INDEPENDENT_FINAL_AUDIT_I_9_3_20260719.md',
    'ledgers/ADVERSE_AND_REJECTED_CHOICES.csv',
    'ledgers/AUTHORITY_AND_PROVENANCE.csv',
    'ledgers/CANDIDATE_COVERAGE_V2.csv',
    'ledgers/INDEX_RESTORATION_DEBT.csv',
    'ledgers/PUBLIC_CSV_ARTIFACT_VALIDATION_I_9_3.txt',
    'ledgers/PUBLIC_MACHINE_VALIDATION_I_9_3.txt',
    'ledgers/SGA1_DIFFICULTY_FAILURE_REVISION.jsonl',
    'ledgers/SGA1_I9_3_EVIDENCE_GRAPH.jsonl',
    'ledgers/SGA1_MACHINE_LEDGER_SCHEMA_v1.json',
    'ledgers/SGA1_NORMALIZATION_DELTA.csv',
    'ledgers/SOURCE_COMPARISON_I_4.csv',
    'ledgers/SOURCE_COMPARISON_I_5.csv',
    'ledgers/SOURCE_COMPARISON_I_6.csv',
    'ledgers/SOURCE_COMPARISON_I_7.csv',
    'ledgers/SOURCE_COMPARISON_I_8.csv',
    'ledgers/SOURCE_COMPARISON_I_9_1.csv',
    'ledgers/SOURCE_COMPARISON_I_9_2.csv',
    'ledgers/SOURCE_COMPARISON_I_9_3.csv',
    'ledgers/SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_4.csv',
    'ledgers/SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_5.csv',
    'ledgers/SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_6.csv',
    'ledgers/SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_7.csv',
    'ledgers/SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_8.csv',
    'ledgers/SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_9_1.csv',
    'ledgers/SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_9_2.csv',
    'ledgers/SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_9_3.csv',
    'LICENSE_ATTRIBUTION.md',
    'PACKAGE_WIDE_PUBLIC_SAFETY_VALIDATION.txt',
    'PREDECESSOR_I9_2_R2_GITHUB_PUBLICATION_READBACK.md',
    'PUBLIC_BUILD_SOURCE_RENDER_REVIEW_SUMMARY.md',
    'PUBLIC_I9_3_REVISION_HISTORY.md',
    'PUBLIC_MACHINE_LEDGER_SUMMARY.md',
    'PUBLIC_ORIGINAL_PRINT_ADJUDICATION_I_9_3.md',
    'PUBLICATION_READINESS.md',
    'SGA1_English_source_sync_workpass.pdf',
    'SGA1_English_source_sync_workpass.tex',
    'SHA256SUMS.txt',
    'SOURCE_CHECK_AND_REVIEW_I_9_3.md',
    'SOURCE_UNIT_RECEIPT_I_9_3.md',
    'SUPERSESSION_AND_ARCHIVE_NOTE.md',
    'VALIDATE_CUMULATIVE_MACHINE_EVIDENCE.ps1',
    'VALIDATE_PUBLIC_MACHINE_CONTROLS.ps1',
    'VERIFY_PUBLIC_PAYLOAD.ps1',
    'VISUAL_QA_I_9_3_20260719.md',
    'ZENODO_PAYLOAD_MANIFEST.csv'
)
$all=@(Get-ChildItem -LiteralPath $root -Recurse -File -Force)
$actualPaths=@($all|ForEach-Object{Rel $root $_.FullName}|Sort-Object)
if($all.Count-ne166-or($actualPaths-join[string][char]10)-cne(@($expectedPaths|Sort-Object)-join[string][char]10)){throw "Pinned payload path set mismatch: $($all.Count)"}
$sumPath=Join-Path $root 'SHA256SUMS.txt'
$manifestPath=Join-Path $root 'ZENODO_PAYLOAD_MANIFEST.csv'
$sumTargets=@($all|Where-Object{$_.FullName-cne$sumPath}|Sort-Object FullName)
$sumRows=@(Get-Content -LiteralPath $sumPath|Where-Object{$_})
if($sumRows.Count-ne$sumTargets.Count){throw 'SHA exact-set count mismatch'}
$seen=[Collections.Generic.HashSet[string]]::new([StringComparer]::Ordinal)
foreach($line in $sumRows){
    if($line-notmatch'^([0-9A-F]{64})  (.+)$'){throw "Malformed SHA row: $line"}
    $expected=$Matches[1];$relative=$Matches[2]
    if(-not$seen.Add($relative)){throw "Duplicate SHA path: $relative"}
    $path=Join-Path $root $relative.Replace('/','\')
    if(-not(Test-Path -LiteralPath $path -PathType Leaf)-or(Sha $path)-cne$expected){throw "SHA mismatch: $relative"}
}
foreach($file in $sumTargets){if(-not$seen.Contains((Rel $root $file.FullName))){throw "SHA set missing: $(Rel $root $file.FullName)"}}
$manifest=@(Import-Csv -LiteralPath $manifestPath)
$manifestTargets=@($all|Where-Object{$_.FullName-cne$sumPath-and$_.FullName-cne$manifestPath}|Sort-Object FullName)
if($manifest.Count-ne$manifestTargets.Count){throw 'Zenodo manifest exact-set count mismatch'}
$manifestSeen=[Collections.Generic.HashSet[string]]::new([StringComparer]::Ordinal)
foreach($row in $manifest){
    $relative=[string]$row.file_path
    if(-not$manifestSeen.Add($relative)){throw "Duplicate manifest path: $relative"}
    $path=Join-Path $root $relative.Replace('/','\')
    if(-not(Test-Path -LiteralPath $path -PathType Leaf)-or(Get-Item $path).Length-ne[long]$row.bytes-or(Sha $path)-cne[string]$row.sha256){throw "Manifest identity mismatch: $relative"}
    if([string]$row.zenodo_concept_doi-cne'10.5281/zenodo.20410947'-or[string]$row.zenodo_last_observed_version_doi-cne'10.5281/zenodo.21435547'-or[string]$row.zenodo_last_observed_at-cne'2026-07-19T16:30:33+02:00'-or[string]$row.archive_owner_live_recheck-cne'Query https://zenodo.org/api/records/21435547/versions/latest immediately before mutation; confirm concept DOI 10.5281/zenodo.20410947; never mint a duplicate record.'-or-not([string]$row.public_caveat).Contains('never mint a duplicate record',[StringComparison]::OrdinalIgnoreCase)){throw "Manifest archive routing mismatch: $relative"}
}
foreach($file in $manifestTargets){if(-not$manifestSeen.Contains((Rel $root $file.FullName))){throw "Manifest set missing: $(Rel $root $file.FullName)"}}
$sourcePins=[ordered]@{
    'SGA1_English_source_sync_workpass.tex'=@{bytes=18781;sha='2D0C09EC8C415CA0DB6DDF355EB775A1BC492E7374F95FA43B6162F1E164A59D'}
    'drafts/SGA1_I_5_English_source_draft.texfrag'=@{bytes=8801;sha='D0959C14AEC3D333EDE96AFFBC6FA8320A223B0A5F2B482B7DCE0268868E8FF9'}
    'drafts/SGA1_I_6_English_source_draft.texfrag'=@{bytes=2168;sha='101CD6F1FC9C46E754E3AD31903863FCA2418DCF31A2E91D47637DF4815291EF'}
    'drafts/SGA1_I_7_English_source_draft.texfrag'=@{bytes=13003;sha='9158A7291A27FD6346D2678A91B359C92A4BDA71CD93D2C24BCBD16856E78F01'}
    'drafts/SGA1_I_8_English_source_draft.texfrag'=@{bytes=7567;sha='4C25DB6731B4AC26CBDB65E8F5EA2B289A95CA7ADACAC7DD0464451B81F5BCA8'}
    'drafts/SGA1_I_9_1_English_source_draft.texfrag'=@{bytes=2848;sha='BBDE49C52927FE7817B5B5D788488144B21DA1B5481CDFF8D4F5212D8098A4F8'}
    'drafts/SGA1_I_9_2_English_source_draft.texfrag'=@{bytes=1370;sha='510FB1A44CAE30C12ADDB0046EB31B232A93550493A00405CBDF4C7AF3395579'}
    'drafts/SGA1_I_9_3_English_source_draft.texfrag'=@{bytes=2272;sha='59F896BDD6FE54D0221D05891503626EEC4204A6A24B09E72833BD2F3EC46A34'}
}
if($sourcePins.Count-ne8){throw 'Editable-source pin count failed'}
foreach($entry in $sourcePins.GetEnumerator()){$path=Join-Path $root ([string]$entry.Key).Replace('/','\');if(-not(Test-Path -LiteralPath $path -PathType Leaf)-or(Get-Item $path).Length-ne[long]$entry.Value.bytes-or(Sha $path)-cne[string]$entry.Value.sha){throw "Editable-source identity failed: $($entry.Key)"}}
$driver=[IO.File]::ReadAllText((Join-Path $root 'SGA1_English_source_sync_workpass.tex'))
if($driver.Contains('I_9_4',[StringComparison]::Ordinal)-or$driver.Contains('lines 556--1775',[StringComparison]::Ordinal)){throw 'Later I.9.4 source leaked into driver'}
$csv=@(
    'ledgers/SOURCE_COMPARISON_I_4.csv','ledgers/SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_4.csv',
    'ledgers/SOURCE_COMPARISON_I_5.csv','ledgers/SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_5.csv',
    'ledgers/SOURCE_COMPARISON_I_6.csv','ledgers/SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_6.csv',
    'ledgers/SOURCE_COMPARISON_I_7.csv','ledgers/SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_7.csv',
    'ledgers/SOURCE_COMPARISON_I_8.csv','ledgers/SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_8.csv',
    'ledgers/SOURCE_COMPARISON_I_9_1.csv','ledgers/SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_9_1.csv',
    'ledgers/SOURCE_COMPARISON_I_9_2.csv','ledgers/SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_9_2.csv',
    'ledgers/SOURCE_COMPARISON_I_9_3.csv','ledgers/SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_9_3.csv',
    'ledgers/ADVERSE_AND_REJECTED_CHOICES.csv','ledgers/SGA1_NORMALIZATION_DELTA.csv',
    'ledgers/INDEX_RESTORATION_DEBT.csv','ledgers/AUTHORITY_AND_PROVENANCE.csv','ledgers/CANDIDATE_COVERAGE_V2.csv'
)
if($csv.Count-ne21-or(Identity-Digest $csv)-cne'AE2E75CF3002ADE356ADEDCF0688493B123F16180A1788B86E430CA73BCF19BF'){throw 'Deterministic public CSV projection failed'}
$schema=Join-Path $root 'ledgers\SGA1_MACHINE_LEDGER_SCHEMA_v1.json'
if((Get-Item $schema).Length-ne6274-or(Sha $schema)-cne'B3BDAB999558309A93CFE407913A73FC4CB95A447F76CB251725D087F977E998'){throw 'I.9.3 schema identity failed'}
$pred=Join-Path $root 'evidence\predecessor_i9_2_r2_machine_controls'
$predFiles=@(Get-ChildItem -LiteralPath $pred -Recurse -File)
if($predFiles.Count-ne82-or[long]($predFiles|Measure-Object Length -Sum).Sum-ne772963-or(Inventory-Digest $pred)-cne'90B466ECF7C1D834BD40E3539554683AD274BEDEA357F9F6C919388DF5E140A8'){throw 'Predecessor machine subtree failed'}
$pdf=Join-Path $root 'SGA1_English_source_sync_workpass.pdf'
if((Get-Item $pdf).Length-ne[long]'548916'-or(Sha $pdf)-cne'1DC6C5793BF15A898A0458907F9B6C00FB6965E0D609BA22486580D2DA75E7CA'){throw 'PDF identity failed'}
$pdfInfo=@(& (Get-Command pdfinfo.exe -ErrorAction Stop).Source $pdf 2>&1)-join[string][char]10
if($pdfInfo-notmatch'(?m)^Pages:\s+17\s*$'-or$pdfInfo-notmatch'(?m)^Encrypted:\s+no\s*$'-or$pdfInfo-notmatch'(?m)^Page size:.*A4'-or$pdfInfo-notmatch'(?m)^Form:\s+none\s*$'-or$pdfInfo-notmatch'(?m)^JavaScript:\s+no\s*$'-or$pdfInfo-notmatch'(?m)^Suspects:\s+no\s*$'-or$pdfInfo-notmatch'(?m)^Title:\s+SGA 1 English source-synchronization workpass: Exposé I opening through Corollary I\.9\.3 and its proof\s*$'){throw 'PDF metadata or security failed'}
$fonts=@(& (Get-Command pdffonts.exe -ErrorAction Stop).Source $pdf 2>&1|Select-Object -Skip 2)
if($fonts.Count-ne30-or@($fonts|Where-Object{$_-notmatch'\s+yes\s+yes\s+yes\s+\d+\s+\d+\s*$'}).Count-ne0){throw 'PDF font gate failed'}
$attachments=@(& (Get-Command pdfdetach.exe -ErrorAction Stop).Source -list $pdf 2>&1)-join[string][char]10
if($attachments-notmatch'(?m)^0 embedded files\s*$'){throw 'PDF embedded-file gate failed'}
$names=@(& (Get-Command mutool.exe -ErrorAction Stop).Source show -g $pdf grep 2>&1)-join[string][char]10
if(@([regex]::Matches($names,'R\(proposition\.1\.9\.3\)')).Count-ne1){throw 'Unique I.9.3 destination gate failed'}
$diag='LaTeX Warning:|Package .* Warning:|Undefined control sequence|! LaTeX Error|Overfull \\hbox|Underfull \\hbox|There were undefined references|Rerun to get|Missing character|pdfTeX warning \(ext4\)|destination with the same identifier|duplicate ignored'
foreach($pass in 2..3){foreach($suffix in @('log','console.txt')){$log=Join-Path $root ('evidence\build\COMPILE_PASS{0}_SANITIZED_FULL.{1}'-f$pass,$suffix);if(@(Select-String -LiteralPath $log -Pattern $diag -AllMatches).Count-ne0){throw "Final compiler diagnostics in pass $pass $suffix"}}}
$renders=@(Get-ChildItem -LiteralPath (Join-Path $root 'evidence\rendered_pdf') -Filter '*.png' -File|Sort-Object Name)
$renderLines=@($renders|ForEach-Object{"$($_.Name)|$($_.Length)|$(Sha $_.FullName)"})
$renderDigest=[BitConverter]::ToString([Security.Cryptography.SHA256]::HashData($utf8.GetBytes(($renderLines-join[string][char]10)+[string][char]10))).Replace('-','')
if($renders.Count-ne17-or$renderDigest-cne'54976F68334AB14C9EC3C9590B14FB807644A28C6CC5EADF5B7CC16CDF3FEBD7'){throw 'Reviewed render identity failed'}
$machine=@(& (Join-Path $root 'VALIDATE_PUBLIC_MACHINE_CONTROLS.ps1') 2>&1)
if(-not$?-or($machine-join[string][char]10)-notmatch'Machine-ledger validation total\s+csv_rows=447; jsonl_records=15; failures=0'){throw 'Portable current machine validation failed'}
$cumulative=@(& (Join-Path $root 'VALIDATE_CUMULATIVE_MACHINE_EVIDENCE.ps1') 2>&1)
if(-not$?-or($cumulative-join[string][char]10)-notmatch'CUMULATIVE_MACHINE_EVIDENCE_VERIFY=PASS'-or($cumulative-join[string][char]10)-notmatch'COMBINED_JSONL_UNIQUE_RECORDS=195'){throw 'Portable cumulative machine validation failed'}
$cursor=[IO.File]::ReadAllText((Join-Path $root 'CONTINUATION_CURSOR.md'))
if(-not$cursor.Contains('Cumulative audited units: 12',[StringComparison]::Ordinal)-or-not$cursor.Contains('First excluded source line: 1761',[StringComparison]::Ordinal)){throw 'Cursor or audited-unit count failed'}
$readback=[IO.File]::ReadAllText((Join-Path $root 'PREDECESSOR_I9_2_R2_GITHUB_PUBLICATION_READBACK.md'))
foreach($required in @('bc3024c681332f540fdd9d8713ace851122bac78','a74bb35da739f6e0dfe6ff4812e208d6dbae408e','exactly 139 files','Authenticated same-concept Zenodo replacement remains')){if(-not$readback.Contains($required,[StringComparison]::Ordinal)){throw "Predecessor publication evidence missing: $required"}}
$readiness=[IO.File]::ReadAllText((Join-Path $root 'PUBLICATION_READINESS.md'))
foreach($required in @('10.5281/zenodo.20410947','10.5281/zenodo.21435547','2026-07-19T16:30:33+02:00','https://zenodo.org/api/records/21435547/versions/latest')){if(-not$readiness.Contains($required,[StringComparison]::Ordinal)){throw "Readiness archive route missing: $required"}}
if($readiness-notmatch'(?is)never\s+mint a duplicate\s+record\.'){throw 'No-duplicate archive warning missing'}
$privatePatterns=@(
    ('C:'+'\Users'+'\'),
    ('C:'+'/Users'+'/'),
    ('Flo'+'ris'),
    ('Pap'+'ors'),
    ('source'+'_thread_id'),
    ('019f70c0'+'-aa55'),
    ('019e6361'+'-c661'),
    ('CLAUDE'+' PLEASE'),
    ('PUBLIC_'+'UPLOAD')
)
$textExt=@('.tex','.texfrag','.csv','.md','.log','.txt','.json','.jsonl','.ps1')
foreach($file in $all){if([IO.Path]::GetExtension($file.Name).ToLowerInvariant()-notin$textExt){continue};$text=[IO.File]::ReadAllText($file.FullName);foreach($pattern in $privatePatterns){if($text.Contains($pattern,[StringComparison]::OrdinalIgnoreCase)){throw "Privacy token in $(Rel $root $file.FullName)"}}}
foreach($file in $all){if((Sha $file.FullName)-in@('7898CBEABA04C4BF1DFF6D784B6366103EEA482F724BAFA594BE791AD4AEE1F6','B97308E4DA3542CDCA400FD965B59033F8E236D76D0B7102F8D76FEFB8ADB7E0','27169F809812E445C5411C732D31D98323AB09BADBA509B574802409C405452E','B7371E297F71704EF313ED188D066A8F3B74AF7299C9B6CAB81DA0C8235AB97B','FE785920C00672BC002919246E2B2AE4739B3513A02453606FBE3E1BD695CB21')){throw 'Source scan or scan derivative leaked into payload'}}
Write-Output 'PUBLIC_PAYLOAD_VERIFY=PASS'
Write-Output 'FILES=166'
Write-Output 'PDF_BYTES=548916'
Write-Output 'PDF_PAGES=17'
Write-Output 'EDITABLE_SOURCE_FILES=8'
Write-Output 'CURRENT_CSV_FILES=21'
Write-Output 'CURRENT_CSV_ROWS=447'
Write-Output 'LOCAL_SEAL_JSONL_FILES=9'
Write-Output 'LOCAL_SEAL_JSONL_RECORDS=205'
Write-Output 'PACKAGE_JSONL_FILES=16'
Write-Output 'PACKAGE_JSONL_RECORDS=195'
Write-Output 'CURSOR=smf_doc-math_3_01.tex:1761 excluded begin corollary I.9.4'