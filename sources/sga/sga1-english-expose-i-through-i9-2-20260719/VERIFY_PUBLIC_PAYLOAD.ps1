[CmdletBinding()]
param()
$ErrorActionPreference = 'Stop'
$root = $PSScriptRoot
function Sha([string] $Path) { (Get-FileHash -LiteralPath $Path -Algorithm SHA256).Hash }
function Rel([string] $Root,[string] $Path) { $Path.Substring($Root.Length+1).Replace('\','/') }
function Identity-Digest([string[]] $RelativePaths) {
    $lines=@($RelativePaths|Sort-Object|ForEach-Object{$p=Join-Path $root $_.Replace('/','\');if(-not(Test-Path -LiteralPath $p -PathType Leaf)){throw "Identity input missing: $_"};"$_|$((Get-Item -LiteralPath $p).Length)|$(Sha $p)"})
    [BitConverter]::ToString([Security.Cryptography.SHA256]::HashData([Text.Encoding]::UTF8.GetBytes(($lines-join"`n")+"`n"))).Replace('-','')
}

$sumPath = Join-Path $root 'SHA256SUMS.txt'
$manifestPath = Join-Path $root 'ZENODO_PAYLOAD_MANIFEST.csv'
if (-not (Test-Path -LiteralPath $sumPath) -or -not (Test-Path -LiteralPath $manifestPath)) { throw 'Manifest files missing' }
$all = @(Get-ChildItem -LiteralPath $root -Recurse -File -Force)
$expectedPaths = @(
    'BUILD_LOG_SANITIZATION.md',
    'CHECKPOINT_README.md',
    'CONTINUATION_CURSOR.md',
    'drafts/SGA1_I_5_English_source_draft.texfrag',
    'drafts/SGA1_I_6_English_source_draft.texfrag',
    'drafts/SGA1_I_7_English_source_draft.texfrag',
    'drafts/SGA1_I_8_English_source_draft.texfrag',
    'drafts/SGA1_I_9_1_English_source_draft.texfrag',
    'drafts/SGA1_I_9_2_English_source_draft.texfrag',
    'evidence/BUILD_SOURCE_RENDER_REVIEW_SUMMARY_LOCAL_SEAL_I_9_2.md',
    'evidence/build/COMPILE_PASS1_SANITIZED_FULL.console.txt',
    'evidence/build/COMPILE_PASS1_SANITIZED_FULL.log',
    'evidence/build/COMPILE_PASS2_SANITIZED_FULL.console.txt',
    'evidence/build/COMPILE_PASS2_SANITIZED_FULL.log',
    'evidence/build/COMPILE_PASS3_SANITIZED_FULL.console.txt',
    'evidence/build/COMPILE_PASS3_SANITIZED_FULL.log',
    'evidence/build/DISTINCT_DESTINATION_VALIDATION.txt',
    'evidence/LOCAL_MACHINE_LEDGER_VALIDATION_I_9_2_FINAL.txt',
    'evidence/PREDECESSOR_AND_CUMULATIVE_MACHINE_VALIDATION.txt',
    'evidence/predecessor_i9_1_r2_machine_controls/evidence/predecessor_i8_r4_machine_controls/PUBLIC_ADVERSE_AND_REJECTED_CHOICES_I_8.csv',
    'evidence/predecessor_i9_1_r2_machine_controls/evidence/predecessor_i8_r4_machine_controls/PUBLIC_ADVERSE_AND_REJECTED_CHOICES.csv',
    'evidence/predecessor_i9_1_r2_machine_controls/evidence/predecessor_i8_r4_machine_controls/PUBLIC_AUTHORITY_AND_COVERAGE_I_8.csv',
    'evidence/predecessor_i9_1_r2_machine_controls/evidence/predecessor_i8_r4_machine_controls/PUBLIC_AUTHORITY_AND_COVERAGE.csv',
    'evidence/predecessor_i9_1_r2_machine_controls/evidence/predecessor_i8_r4_machine_controls/PUBLIC_CSV_ARTIFACT_VALIDATION_I_8.txt',
    'evidence/predecessor_i9_1_r2_machine_controls/evidence/predecessor_i8_r4_machine_controls/PUBLIC_INDEX_RESTORATION_DEBT.csv',
    'evidence/predecessor_i9_1_r2_machine_controls/evidence/predecessor_i8_r4_machine_controls/PUBLIC_MACHINE_VALIDATION_I_8.txt',
    'evidence/predecessor_i9_1_r2_machine_controls/evidence/predecessor_i8_r4_machine_controls/PUBLIC_SGA1_I4_DIFFICULTY_FAILURE_REVISION.jsonl',
    'evidence/predecessor_i9_1_r2_machine_controls/evidence/predecessor_i8_r4_machine_controls/PUBLIC_SGA1_I4_EVIDENCE_GRAPH.jsonl',
    'evidence/predecessor_i9_1_r2_machine_controls/evidence/predecessor_i8_r4_machine_controls/PUBLIC_SGA1_I5_DIFFICULTY_FAILURE_REVISION.jsonl',
    'evidence/predecessor_i9_1_r2_machine_controls/evidence/predecessor_i8_r4_machine_controls/PUBLIC_SGA1_I5_EVIDENCE_GRAPH.jsonl',
    'evidence/predecessor_i9_1_r2_machine_controls/evidence/predecessor_i8_r4_machine_controls/PUBLIC_SGA1_I6_DIFFICULTY_FAILURE_REVISION.jsonl',
    'evidence/predecessor_i9_1_r2_machine_controls/evidence/predecessor_i8_r4_machine_controls/PUBLIC_SGA1_I6_EVIDENCE_GRAPH.jsonl',
    'evidence/predecessor_i9_1_r2_machine_controls/evidence/predecessor_i8_r4_machine_controls/PUBLIC_SGA1_I7_DIFFICULTY_FAILURE_REVISION.jsonl',
    'evidence/predecessor_i9_1_r2_machine_controls/evidence/predecessor_i8_r4_machine_controls/PUBLIC_SGA1_I7_EVIDENCE_GRAPH.jsonl',
    'evidence/predecessor_i9_1_r2_machine_controls/evidence/predecessor_i8_r4_machine_controls/PUBLIC_SGA1_I8_DIFFICULTY_FAILURE_REVISION.jsonl',
    'evidence/predecessor_i9_1_r2_machine_controls/evidence/predecessor_i8_r4_machine_controls/PUBLIC_SGA1_I8_EVIDENCE_GRAPH.jsonl',
    'evidence/predecessor_i9_1_r2_machine_controls/evidence/predecessor_i8_r4_machine_controls/PUBLIC_SGA1_MACHINE_LEDGER_SCHEMA_v5.json',
    'evidence/predecessor_i9_1_r2_machine_controls/evidence/predecessor_i8_r4_machine_controls/PUBLIC_SGA1_NORMALIZATION_DELTA_I_8.csv',
    'evidence/predecessor_i9_1_r2_machine_controls/evidence/predecessor_i8_r4_machine_controls/PUBLIC_SGA1_NORMALIZATION_DELTA.csv',
    'evidence/predecessor_i9_1_r2_machine_controls/evidence/predecessor_i8_r4_machine_controls/PUBLIC_SOURCE_COMPARISON_I_0_1.csv',
    'evidence/predecessor_i9_1_r2_machine_controls/evidence/predecessor_i8_r4_machine_controls/PUBLIC_SOURCE_COMPARISON_I_2.csv',
    'evidence/predecessor_i9_1_r2_machine_controls/evidence/predecessor_i8_r4_machine_controls/PUBLIC_SOURCE_COMPARISON_I_3.csv',
    'evidence/predecessor_i9_1_r2_machine_controls/evidence/predecessor_i8_r4_machine_controls/PUBLIC_SOURCE_COMPARISON_I_4.csv',
    'evidence/predecessor_i9_1_r2_machine_controls/evidence/predecessor_i8_r4_machine_controls/PUBLIC_SOURCE_COMPARISON_I_5.csv',
    'evidence/predecessor_i9_1_r2_machine_controls/evidence/predecessor_i8_r4_machine_controls/PUBLIC_SOURCE_COMPARISON_I_6.csv',
    'evidence/predecessor_i9_1_r2_machine_controls/evidence/predecessor_i8_r4_machine_controls/PUBLIC_SOURCE_COMPARISON_I_7.csv',
    'evidence/predecessor_i9_1_r2_machine_controls/evidence/predecessor_i8_r4_machine_controls/PUBLIC_SOURCE_COMPARISON_I_8.csv',
    'evidence/predecessor_i9_1_r2_machine_controls/evidence/predecessor_i8_r4_machine_controls/PUBLIC_SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_0_1.csv',
    'evidence/predecessor_i9_1_r2_machine_controls/evidence/predecessor_i8_r4_machine_controls/PUBLIC_SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_2.csv',
    'evidence/predecessor_i9_1_r2_machine_controls/evidence/predecessor_i8_r4_machine_controls/PUBLIC_SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_3.csv',
    'evidence/predecessor_i9_1_r2_machine_controls/evidence/predecessor_i8_r4_machine_controls/PUBLIC_SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_4.csv',
    'evidence/predecessor_i9_1_r2_machine_controls/evidence/predecessor_i8_r4_machine_controls/PUBLIC_SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_5.csv',
    'evidence/predecessor_i9_1_r2_machine_controls/evidence/predecessor_i8_r4_machine_controls/PUBLIC_SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_6.csv',
    'evidence/predecessor_i9_1_r2_machine_controls/evidence/predecessor_i8_r4_machine_controls/PUBLIC_SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_7.csv',
    'evidence/predecessor_i9_1_r2_machine_controls/evidence/predecessor_i8_r4_machine_controls/PUBLIC_SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_8.csv',
    'evidence/predecessor_i9_1_r2_machine_controls/ledgers/ADVERSE_AND_REJECTED_CHOICES.csv',
    'evidence/predecessor_i9_1_r2_machine_controls/ledgers/AUTHORITY_AND_PROVENANCE.csv',
    'evidence/predecessor_i9_1_r2_machine_controls/ledgers/CANDIDATE_COVERAGE_V2.csv',
    'evidence/predecessor_i9_1_r2_machine_controls/ledgers/INDEX_RESTORATION_DEBT.csv',
    'evidence/predecessor_i9_1_r2_machine_controls/ledgers/PUBLIC_CSV_ARTIFACT_VALIDATION_I_9_1.txt',
    'evidence/predecessor_i9_1_r2_machine_controls/ledgers/PUBLIC_MACHINE_VALIDATION_I_9_1.txt',
    'evidence/predecessor_i9_1_r2_machine_controls/ledgers/SGA1_DIFFICULTY_FAILURE_REVISION.jsonl',
    'evidence/predecessor_i9_1_r2_machine_controls/ledgers/SGA1_I9_1_EVIDENCE_GRAPH.jsonl',
    'evidence/predecessor_i9_1_r2_machine_controls/ledgers/SGA1_MACHINE_LEDGER_SCHEMA_v1.json',
    'evidence/predecessor_i9_1_r2_machine_controls/ledgers/SGA1_NORMALIZATION_DELTA.csv',
    'evidence/predecessor_i9_1_r2_machine_controls/ledgers/SOURCE_COMPARISON_I_4.csv',
    'evidence/predecessor_i9_1_r2_machine_controls/ledgers/SOURCE_COMPARISON_I_5.csv',
    'evidence/predecessor_i9_1_r2_machine_controls/ledgers/SOURCE_COMPARISON_I_6.csv',
    'evidence/predecessor_i9_1_r2_machine_controls/ledgers/SOURCE_COMPARISON_I_7.csv',
    'evidence/predecessor_i9_1_r2_machine_controls/ledgers/SOURCE_COMPARISON_I_8.csv',
    'evidence/predecessor_i9_1_r2_machine_controls/ledgers/SOURCE_COMPARISON_I_9_1.csv',
    'evidence/predecessor_i9_1_r2_machine_controls/ledgers/SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_4.csv',
    'evidence/predecessor_i9_1_r2_machine_controls/ledgers/SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_5.csv',
    'evidence/predecessor_i9_1_r2_machine_controls/ledgers/SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_6.csv',
    'evidence/predecessor_i9_1_r2_machine_controls/ledgers/SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_7.csv',
    'evidence/predecessor_i9_1_r2_machine_controls/ledgers/SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_8.csv',
    'evidence/predecessor_i9_1_r2_machine_controls/ledgers/SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_9_1.csv',
    'evidence/PREDECESSOR_I9_1_R2_PORTABLE_VERIFY.txt',
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
    'INDEPENDENT_FINAL_AUDIT_I_9_2_R4_20260719.md',
    'ledgers/ADVERSE_AND_REJECTED_CHOICES.csv',
    'ledgers/AUTHORITY_AND_PROVENANCE.csv',
    'ledgers/CANDIDATE_COVERAGE_V2.csv',
    'ledgers/INDEX_RESTORATION_DEBT.csv',
    'ledgers/PUBLIC_CSV_ARTIFACT_VALIDATION_I_9_2.txt',
    'ledgers/PUBLIC_MACHINE_VALIDATION_I_9_2.txt',
    'ledgers/SGA1_DIFFICULTY_FAILURE_REVISION.jsonl',
    'ledgers/SGA1_I9_2_EVIDENCE_GRAPH.jsonl',
    'ledgers/SGA1_MACHINE_LEDGER_SCHEMA_v1.json',
    'ledgers/SGA1_NORMALIZATION_DELTA.csv',
    'ledgers/SOURCE_COMPARISON_I_4.csv',
    'ledgers/SOURCE_COMPARISON_I_5.csv',
    'ledgers/SOURCE_COMPARISON_I_6.csv',
    'ledgers/SOURCE_COMPARISON_I_7.csv',
    'ledgers/SOURCE_COMPARISON_I_8.csv',
    'ledgers/SOURCE_COMPARISON_I_9_1.csv',
    'ledgers/SOURCE_COMPARISON_I_9_2.csv',
    'ledgers/SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_4.csv',
    'ledgers/SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_5.csv',
    'ledgers/SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_6.csv',
    'ledgers/SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_7.csv',
    'ledgers/SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_8.csv',
    'ledgers/SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_9_1.csv',
    'ledgers/SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_9_2.csv',
    'LICENSE_ATTRIBUTION.md',
    'PACKAGE_WIDE_PUBLIC_SAFETY_VALIDATION.txt',
    'PUBLIC_BUILD_SOURCE_RENDER_REVIEW_SUMMARY.md',
    'PUBLIC_I9_2_REVISION_HISTORY.md',
    'PUBLIC_MACHINE_LEDGER_SUMMARY.md',
    'PUBLIC_ORIGINAL_PRINT_ADJUDICATION_I_9_2.md',
    'PUBLICATION_READINESS.md',
    'REJECTED_PUBLIC_CHECKPOINT_I_9_2_R1_NONPUBLICATION_HOLD_20260719.md',
    'REJECTED_PUBLIC_R2_ATTEMPT1_PREFREEZE_VERIFIER_PHRASE_WRAP_20260719.md',
    'SGA1_English_source_sync_workpass.pdf',
    'SGA1_English_source_sync_workpass.tex',
    'SHA256SUMS.txt',
    'SOURCE_CHECK_AND_REVIEW_I_9_2.md',
    'SOURCE_UNIT_RECEIPT_I_9_2.md',
    'SUPERSESSION_AND_ARCHIVE_NOTE.md',
    'VALIDATE_CUMULATIVE_MACHINE_EVIDENCE.ps1',
    'VALIDATE_PUBLIC_MACHINE_CONTROLS.ps1',
    'VERIFY_PUBLIC_PAYLOAD.ps1',
    'VISUAL_QA_I_9_2_20260719.md',
    'ZENODO_PAYLOAD_MANIFEST.csv'
)
$actualPaths = @($all | ForEach-Object { Rel $root $_.FullName } | Sort-Object)
if ($all.Count -ne 139 -or ($actualPaths -join "`n") -cne (@($expectedPaths | Sort-Object) -join "`n")) { throw "Pinned payload path set mismatch: expected=139 actual=$($all.Count)" }
$sumTargets = @($all | Where-Object { $_.FullName -cne $sumPath } | Sort-Object FullName)
$sumRows = @(Get-Content -LiteralPath $sumPath | Where-Object { $_ })
if ($sumRows.Count -ne $sumTargets.Count) { throw "SHA exact-set count mismatch" }
$seen = [Collections.Generic.HashSet[string]]::new([StringComparer]::Ordinal)
foreach ($line in $sumRows) {
    if ($line -notmatch '^([0-9A-F]{64})  (.+)$') { throw "Malformed SHA row: $line" }
    $expected=$Matches[1]; $relative=$Matches[2]
    if (-not $seen.Add($relative)) { throw "Duplicate SHA path: $relative" }
    $path=Join-Path $root $relative.Replace('/','\')
    if (-not (Test-Path -LiteralPath $path -PathType Leaf) -or (Sha $path) -cne $expected) { throw "SHA mismatch: $relative" }
}
foreach ($file in $sumTargets) { if (-not $seen.Contains((Rel $root $file.FullName))) { throw "SHA set missing: $(Rel $root $file.FullName)" } }

$manifest = @(Import-Csv -LiteralPath $manifestPath)
$manifestTargets = @($all | Where-Object { $_.FullName -cne $sumPath -and $_.FullName -cne $manifestPath } | Sort-Object FullName)
if ($manifest.Count -ne $manifestTargets.Count) { throw 'Zenodo manifest exact-set count mismatch' }
$manifestSeen = [Collections.Generic.HashSet[string]]::new([StringComparer]::Ordinal)
foreach ($row in $manifest) {
    $relative=[string]$row.file_path
    if (-not $manifestSeen.Add($relative)) { throw "Duplicate manifest path: $relative" }
    $path=Join-Path $root $relative.Replace('/','\')
    if (-not (Test-Path -LiteralPath $path -PathType Leaf)) { throw "Manifest path missing: $relative" }
    if ((Get-Item $path).Length -ne [long]$row.bytes -or (Sha $path) -cne [string]$row.sha256) { throw "Manifest identity mismatch: $relative" }
    if ([string]$row.zenodo_concept_doi -cne '10.5281/zenodo.20410947' -or
        [string]$row.zenodo_last_observed_version_doi -cne '10.5281/zenodo.21435547' -or
        [string]$row.zenodo_last_observed_at -cne '2026-07-19 approximately 13:20 Europe/Berlin (UTC+02:00)' -or
        [string]$row.archive_owner_live_recheck -cne 'Query https://zenodo.org/api/records/21435547/versions/latest immediately before mutation; confirm concept DOI 10.5281/zenodo.20410947; never mint a duplicate record.' -or
        -not ([string]$row.public_caveat).Contains('never mint a duplicate record',[StringComparison]::OrdinalIgnoreCase)) {
        throw "Manifest Zenodo routing/caveat mismatch: $relative"
    }
}
foreach ($file in $manifestTargets) { if (-not $manifestSeen.Contains((Rel $root $file.FullName))) { throw "Manifest set missing: $(Rel $root $file.FullName)" } }

$editableSourcePins=[ordered]@{
    'SGA1_English_source_sync_workpass.tex'=@{bytes=18833;sha='7C7FD36084FF4891F943508620D20A91BCDE669114C3C149FADF99E1B95F23B2'}
    'drafts/SGA1_I_5_English_source_draft.texfrag'=@{bytes=8801;sha='D0959C14AEC3D333EDE96AFFBC6FA8320A223B0A5F2B482B7DCE0268868E8FF9'}
    'drafts/SGA1_I_6_English_source_draft.texfrag'=@{bytes=2168;sha='101CD6F1FC9C46E754E3AD31903863FCA2418DCF31A2E91D47637DF4815291EF'}
    'drafts/SGA1_I_7_English_source_draft.texfrag'=@{bytes=13003;sha='9158A7291A27FD6346D2678A91B359C92A4BDA71CD93D2C24BCBD16856E78F01'}
    'drafts/SGA1_I_8_English_source_draft.texfrag'=@{bytes=7567;sha='4C25DB6731B4AC26CBDB65E8F5EA2B289A95CA7ADACAC7DD0464451B81F5BCA8'}
    'drafts/SGA1_I_9_1_English_source_draft.texfrag'=@{bytes=2848;sha='BBDE49C52927FE7817B5B5D788488144B21DA1B5481CDFF8D4F5212D8098A4F8'}
    'drafts/SGA1_I_9_2_English_source_draft.texfrag'=@{bytes=1370;sha='510FB1A44CAE30C12ADDB0046EB31B232A93550493A00405CBDF4C7AF3395579'}
}
if($editableSourcePins.Count-ne 7){throw 'Editable-source pin count failed'}
foreach($entry in $editableSourcePins.GetEnumerator()){$p=Join-Path $root ([string]$entry.Key).Replace('/','\');if(-not(Test-Path -LiteralPath $p -PathType Leaf)-or(Get-Item -LiteralPath $p).Length-ne[long]$entry.Value.bytes-or(Sha $p)-cne[string]$entry.Value.sha){throw "Editable-source identity failed: $($entry.Key)"}}
$publicCsvRelative=@(
    'ledgers/SOURCE_COMPARISON_I_4.csv','ledgers/SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_4.csv','ledgers/SOURCE_COMPARISON_I_5.csv','ledgers/SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_5.csv','ledgers/SOURCE_COMPARISON_I_6.csv','ledgers/SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_6.csv','ledgers/SOURCE_COMPARISON_I_7.csv','ledgers/SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_7.csv','ledgers/SOURCE_COMPARISON_I_8.csv','ledgers/SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_8.csv','ledgers/SOURCE_COMPARISON_I_9_1.csv','ledgers/SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_9_1.csv','ledgers/SOURCE_COMPARISON_I_9_2.csv','ledgers/SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_9_2.csv','ledgers/ADVERSE_AND_REJECTED_CHOICES.csv','ledgers/SGA1_NORMALIZATION_DELTA.csv','ledgers/INDEX_RESTORATION_DEBT.csv','ledgers/AUTHORITY_AND_PROVENANCE.csv','ledgers/CANDIDATE_COVERAGE_V2.csv'
)
if($publicCsvRelative.Count-ne 19-or(Identity-Digest $publicCsvRelative)-cne'D914AD96B9C3A37064269B705A4261B5D8CAC1F07BDB0695A207EEECC9AF8B8F'){throw 'Deterministic public CSV projection identity failed'}
$pdf=Join-Path $root 'SGA1_English_source_sync_workpass.pdf'
if ((Get-Item $pdf).Length -ne 545957 -or (Sha $pdf) -cne '91D5B5F502239FC77DF6773D858AFF81525380240E1286DAC19520E5DE43C550') { throw 'PDF identity failed' }
$pdfInfo=@(& (Get-Command pdfinfo.exe -ErrorAction Stop).Source $pdf 2>&1) -join "`n"
if ($pdfInfo -notmatch '(?m)^Pages:\s+16\s*$' -or $pdfInfo -notmatch '(?m)^Encrypted:\s+no\s*$' -or $pdfInfo -notmatch '(?m)^Page size:.*A4' -or $pdfInfo -notmatch '(?m)^Form:\s+none\s*$' -or $pdfInfo -notmatch '(?m)^JavaScript:\s+no\s*$' -or $pdfInfo -notmatch '(?m)^Suspects:\s+no\s*$' -or $pdfInfo -notmatch '(?m)^Title:\s+SGA 1 English source-synchronization workpass: Exposé I opening through Proposition I\.9\.2\s*$') { throw 'PDF metadata/security failed' }
$fonts=@(& (Get-Command pdffonts.exe -ErrorAction Stop).Source $pdf 2>&1 | Select-Object -Skip 2)
if ($fonts.Count -ne 30 -or @($fonts | Where-Object { $_ -notmatch '\s+yes\s+yes\s+yes\s+\d+\s+\d+\s*$' }).Count -ne 0) { throw 'PDF font gate failed' }
$attachments=@(& (Get-Command pdfdetach.exe -ErrorAction Stop).Source -list $pdf 2>&1) -join "`n"
if($attachments -notmatch '(?m)^0 embedded files\s*$'){throw 'PDF embedded-file gate failed'}
$names=@(& (Get-Command mutool.exe -ErrorAction Stop).Source show -g $pdf grep 2>&1) -join "`n"
if(-not $names.Contains('R(proposition.1.9.2)') -or -not $names.Contains('R(proposition.1.9.2.second)')){throw 'Distinct PDF destination gate failed'}

$diag='LaTeX Warning:|Package .* Warning:|Undefined control sequence|! LaTeX Error|Overfull \\hbox|Underfull \\hbox|There were undefined references|Rerun to get|Missing character|pdfTeX warning \(ext4\)|destination with the same identifier|duplicate ignored'
foreach ($pass in 2..3) {
    foreach($suffix in @('log','console.txt')){
        $log=Join-Path $root "evidence\build\COMPILE_PASS${pass}_SANITIZED_FULL.$suffix"
        if (@(Select-String -LiteralPath $log -Pattern $diag -AllMatches).Count -ne 0) { throw "Final compiler diagnostics in pass $pass $suffix" }
    }
}
$renders=@(Get-ChildItem -LiteralPath (Join-Path $root 'evidence\rendered_pdf') -Filter '*.png' -File -Force | Sort-Object Name)
if ($renders.Count -ne 16) { throw 'Rendered-page count failed' }
$renderLines=@($renders|ForEach-Object{"$($_.Name)|$($_.Length)|$(Sha $_.FullName)"})
$renderDigest=[BitConverter]::ToString([Security.Cryptography.SHA256]::HashData([Text.Encoding]::UTF8.GetBytes(($renderLines-join"`n")+"`n"))).Replace('-','')
if($renderDigest -cne '0DC7C1D8473EAF69860CF6C12F173CBE11D44078DE1C05B154A300A18339BB3B'){throw 'Reviewed render identity failed'}

$machine=@(& (Join-Path $root 'VALIDATE_PUBLIC_MACHINE_CONTROLS.ps1') 2>&1)
if (-not $? -or ($machine -join "`n") -notmatch 'Machine-ledger validation total\s+csv_rows=405; jsonl_records=17; failures=0') { throw 'Portable machine validation failed' }
$cumulativeMachine=@(& (Join-Path $root 'VALIDATE_CUMULATIVE_MACHINE_EVIDENCE.ps1') 2>&1)
if (-not $? -or ($cumulativeMachine -join "`n") -notmatch 'CUMULATIVE_MACHINE_EVIDENCE_VERIFY=PASS' -or ($cumulativeMachine -join "`n") -notmatch 'COMBINED_JSONL_UNIQUE_RECORDS=180') { throw 'Portable cumulative machine-evidence validation failed' }

$cursorText=[IO.File]::ReadAllText((Join-Path $root 'CONTINUATION_CURSOR.md'))
if(-not $cursorText.Contains('Cumulative audited units: 11',[StringComparison]::Ordinal)-or-not $cursorText.Contains('2B2401E5DB83FE1A8B394590F7C914741834E8F4C296F26DC2C6873432020B12',[StringComparison]::Ordinal)){throw 'Cumulative audited-unit justification failed'}
$r1HoldText=[IO.File]::ReadAllText((Join-Path $root 'REJECTED_PUBLIC_CHECKPOINT_I_9_2_R1_NONPUBLICATION_HOLD_20260719.md'))
if(-not $r1HoldText.Contains('REJECTED / NONPUBLICATION HOLD',[StringComparison]::Ordinal)-or-not $r1HoldText.Contains('2F4347737B09AAA2E0456CCC607DE2C905E65CD2FC23176CCAEACADB6870D5BA',[StringComparison]::Ordinal)){throw 'Held r1 rejection identity failed'}
$attempt1Text=[IO.File]::ReadAllText((Join-Path $root 'REJECTED_PUBLIC_R2_ATTEMPT1_PREFREEZE_VERIFIER_PHRASE_WRAP_20260719.md'))
foreach($required in @('Publication-readiness DOI/recheck text missing: never mint a duplicate record.','3F1484AB7FFFE303619EFDAB5841F43BA368AB1B209796504E7AFA231686FCA6','7BCDB1CCCC393374C576E38C4F4786402479328A72A86C4CB954E3FA671ED80B','Status: REJECTED and deliberately unclosed.')){if(-not $attempt1Text.Contains($required,[StringComparison]::Ordinal)){throw "Attempt1 rejection evidence missing: $required"}}
$difficultyRecords=@([IO.File]::ReadAllLines((Join-Path $root 'ledgers\SGA1_DIFFICULTY_FAILURE_REVISION.jsonl'),[Text.UTF8Encoding]::new($false,$true))|Where-Object{-not[string]::IsNullOrWhiteSpace($_)}|ForEach-Object{$_|ConvertFrom-Json -Depth 40})
$attempt1Records=@($difficultyRecords|Where-Object{[string]$_.record_id -ceq 'SGA1-I92-PACKAGE-R2-ATTEMPT1-PREFREEZE-VERIFY-FAIL-0001'})
if($attempt1Records.Count-ne 1-or[string]$attempt1Records[0].status-cne'rejected'-or-not[string]::IsNullOrWhiteSpace([string]$attempt1Records[0].closed_by_record_id)-or-not[string]::IsNullOrWhiteSpace([string]$attempt1Records[0].superseded_by_record_id)){throw 'Attempt1 failure record is not uniquely rejected and unclosed'}
$readinessText=[IO.File]::ReadAllText((Join-Path $root 'PUBLICATION_READINESS.md'))
foreach($required in @('10.5281/zenodo.20410947','10.5281/zenodo.21435547','2026-07-19 approximately 13:20 Europe/Berlin (UTC+02:00)','https://zenodo.org/api/records/21435547/versions/latest')){if(-not $readinessText.Contains($required,[StringComparison]::Ordinal)){throw "Publication-readiness DOI/recheck text missing: $required"}}
if($readinessText -notmatch '(?is)never\s+mint a duplicate record\.') { throw 'Publication-readiness no-duplicate warning missing' }

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
foreach ($file in $all) {
    if ([IO.Path]::GetExtension($file.Name).ToLowerInvariant() -notin $textExt) { continue }
    $text=[IO.File]::ReadAllText($file.FullName)
    foreach ($pattern in $privatePatterns) { if ($text.Contains($pattern,[StringComparison]::OrdinalIgnoreCase)) { throw "Privacy token in $(Rel $root $file.FullName)" } }
}
foreach ($file in $all) {
    if ((Sha $file.FullName) -in @('7898CBEABA04C4BF1DFF6D784B6366103EEA482F724BAFA594BE791AD4AEE1F6','B97308E4DA3542CDCA400FD965B59033F8E236D76D0B7102F8D76FEFB8ADB7E0','27169F809812E445C5411C732D31D98323AB09BADBA509B574802409C405452E','B7371E297F71704EF313ED188D066A8F3B74AF7299C9B6CAB81DA0C8235AB97B','FE785920C00672BC002919246E2B2AE4739B3513A02453606FBE3E1BD695CB21')) { throw 'Source scan or scan derivative leaked into payload' }
}
Write-Output 'PUBLIC_PAYLOAD_VERIFY=PASS'
Write-Output "FILES=$($all.Count)"
Write-Output "PDF_BYTES=545957"
Write-Output 'PDF_PAGES=16'
Write-Output 'EDITABLE_SOURCE_FILES=7'
Write-Output 'CSV_FILES=59'
Write-Output 'CSV_ROWS=1187'
Write-Output 'JSONL_FILES=14'
Write-Output 'CURRENT_JSONL_RECORDS=17'
Write-Output 'JSONL_RECORDS=180'
Write-Output "CURSOR=smf_doc-math_3_01.tex:1722 excluded Cela \'equivaut au"