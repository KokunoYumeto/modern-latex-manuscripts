[CmdletBinding()]
param()
$ErrorActionPreference = 'Stop'
$root = $PSScriptRoot
function Sha([string] $Path) { (Get-FileHash -LiteralPath $Path -Algorithm SHA256).Hash }
function Rel([string] $Root,[string] $Path) { $Path.Substring($Root.Length+1).Replace('\','/') }

$sumPath = Join-Path $root 'SHA256SUMS.txt'
$manifestPath = Join-Path $root 'ZENODO_PAYLOAD_MANIFEST.csv'
if (-not (Test-Path -LiteralPath $sumPath) -or -not (Test-Path -LiteralPath $manifestPath)) { throw 'Manifest files missing' }
$all = @(Get-ChildItem -LiteralPath $root -Recurse -File)
$expectedPaths = @(
    'BUILD_LOG_SANITIZATION.md',
    'CHECKPOINT_README.md',
    'CONTINUATION_CURSOR.md',
    'drafts/SGA1_I_5_English_source_draft.texfrag',
    'drafts/SGA1_I_6_English_source_draft.texfrag',
    'drafts/SGA1_I_7_English_source_draft.texfrag',
    'drafts/SGA1_I_8_English_source_draft.texfrag',
    'drafts/SGA1_I_9_1_English_source_draft.texfrag',
    'evidence/BUILD_SOURCE_RENDER_REVIEW_SUMMARY_LOCAL_SEAL_I_9_1.md',
    'evidence/build/COMPILE_PASS1_SANITIZED_FULL.console.txt',
    'evidence/build/COMPILE_PASS1_SANITIZED_FULL.log',
    'evidence/build/COMPILE_PASS2_SANITIZED_FULL.console.txt',
    'evidence/build/COMPILE_PASS2_SANITIZED_FULL.log',
    'evidence/build/COMPILE_PASS3_SANITIZED_FULL.console.txt',
    'evidence/build/COMPILE_PASS3_SANITIZED_FULL.log',
    'evidence/PREDECESSOR_AND_CUMULATIVE_MACHINE_VALIDATION.txt',
    'evidence/predecessor_i8_r4_machine_controls/PUBLIC_ADVERSE_AND_REJECTED_CHOICES_I_8.csv',
    'evidence/predecessor_i8_r4_machine_controls/PUBLIC_ADVERSE_AND_REJECTED_CHOICES.csv',
    'evidence/predecessor_i8_r4_machine_controls/PUBLIC_AUTHORITY_AND_COVERAGE_I_8.csv',
    'evidence/predecessor_i8_r4_machine_controls/PUBLIC_AUTHORITY_AND_COVERAGE.csv',
    'evidence/predecessor_i8_r4_machine_controls/PUBLIC_CSV_ARTIFACT_VALIDATION_I_8.txt',
    'evidence/predecessor_i8_r4_machine_controls/PUBLIC_INDEX_RESTORATION_DEBT.csv',
    'evidence/predecessor_i8_r4_machine_controls/PUBLIC_MACHINE_VALIDATION_I_8.txt',
    'evidence/predecessor_i8_r4_machine_controls/PUBLIC_SGA1_I4_DIFFICULTY_FAILURE_REVISION.jsonl',
    'evidence/predecessor_i8_r4_machine_controls/PUBLIC_SGA1_I4_EVIDENCE_GRAPH.jsonl',
    'evidence/predecessor_i8_r4_machine_controls/PUBLIC_SGA1_I5_DIFFICULTY_FAILURE_REVISION.jsonl',
    'evidence/predecessor_i8_r4_machine_controls/PUBLIC_SGA1_I5_EVIDENCE_GRAPH.jsonl',
    'evidence/predecessor_i8_r4_machine_controls/PUBLIC_SGA1_I6_DIFFICULTY_FAILURE_REVISION.jsonl',
    'evidence/predecessor_i8_r4_machine_controls/PUBLIC_SGA1_I6_EVIDENCE_GRAPH.jsonl',
    'evidence/predecessor_i8_r4_machine_controls/PUBLIC_SGA1_I7_DIFFICULTY_FAILURE_REVISION.jsonl',
    'evidence/predecessor_i8_r4_machine_controls/PUBLIC_SGA1_I7_EVIDENCE_GRAPH.jsonl',
    'evidence/predecessor_i8_r4_machine_controls/PUBLIC_SGA1_I8_DIFFICULTY_FAILURE_REVISION.jsonl',
    'evidence/predecessor_i8_r4_machine_controls/PUBLIC_SGA1_I8_EVIDENCE_GRAPH.jsonl',
    'evidence/predecessor_i8_r4_machine_controls/PUBLIC_SGA1_MACHINE_LEDGER_SCHEMA_v5.json',
    'evidence/predecessor_i8_r4_machine_controls/PUBLIC_SGA1_NORMALIZATION_DELTA_I_8.csv',
    'evidence/predecessor_i8_r4_machine_controls/PUBLIC_SGA1_NORMALIZATION_DELTA.csv',
    'evidence/predecessor_i8_r4_machine_controls/PUBLIC_SOURCE_COMPARISON_I_0_1.csv',
    'evidence/predecessor_i8_r4_machine_controls/PUBLIC_SOURCE_COMPARISON_I_2.csv',
    'evidence/predecessor_i8_r4_machine_controls/PUBLIC_SOURCE_COMPARISON_I_3.csv',
    'evidence/predecessor_i8_r4_machine_controls/PUBLIC_SOURCE_COMPARISON_I_4.csv',
    'evidence/predecessor_i8_r4_machine_controls/PUBLIC_SOURCE_COMPARISON_I_5.csv',
    'evidence/predecessor_i8_r4_machine_controls/PUBLIC_SOURCE_COMPARISON_I_6.csv',
    'evidence/predecessor_i8_r4_machine_controls/PUBLIC_SOURCE_COMPARISON_I_7.csv',
    'evidence/predecessor_i8_r4_machine_controls/PUBLIC_SOURCE_COMPARISON_I_8.csv',
    'evidence/predecessor_i8_r4_machine_controls/PUBLIC_SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_0_1.csv',
    'evidence/predecessor_i8_r4_machine_controls/PUBLIC_SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_2.csv',
    'evidence/predecessor_i8_r4_machine_controls/PUBLIC_SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_3.csv',
    'evidence/predecessor_i8_r4_machine_controls/PUBLIC_SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_4.csv',
    'evidence/predecessor_i8_r4_machine_controls/PUBLIC_SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_5.csv',
    'evidence/predecessor_i8_r4_machine_controls/PUBLIC_SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_6.csv',
    'evidence/predecessor_i8_r4_machine_controls/PUBLIC_SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_7.csv',
    'evidence/predecessor_i8_r4_machine_controls/PUBLIC_SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_8.csv',
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
    'INDEPENDENT_SOURCE_REVIEW_I_9_1_20260719.md',
    'ledgers/ADVERSE_AND_REJECTED_CHOICES.csv',
    'ledgers/AUTHORITY_AND_PROVENANCE.csv',
    'ledgers/CANDIDATE_COVERAGE_V2.csv',
    'ledgers/INDEX_RESTORATION_DEBT.csv',
    'ledgers/PUBLIC_CSV_ARTIFACT_VALIDATION_I_9_1.txt',
    'ledgers/PUBLIC_MACHINE_VALIDATION_I_9_1.txt',
    'ledgers/SGA1_DIFFICULTY_FAILURE_REVISION.jsonl',
    'ledgers/SGA1_I9_1_EVIDENCE_GRAPH.jsonl',
    'ledgers/SGA1_MACHINE_LEDGER_SCHEMA_v1.json',
    'ledgers/SGA1_NORMALIZATION_DELTA.csv',
    'ledgers/SOURCE_COMPARISON_I_4.csv',
    'ledgers/SOURCE_COMPARISON_I_5.csv',
    'ledgers/SOURCE_COMPARISON_I_6.csv',
    'ledgers/SOURCE_COMPARISON_I_7.csv',
    'ledgers/SOURCE_COMPARISON_I_8.csv',
    'ledgers/SOURCE_COMPARISON_I_9_1.csv',
    'ledgers/SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_4.csv',
    'ledgers/SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_5.csv',
    'ledgers/SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_6.csv',
    'ledgers/SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_7.csv',
    'ledgers/SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_8.csv',
    'ledgers/SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_9_1.csv',
    'LICENSE_ATTRIBUTION.md',
    'ORIGINAL_PRINT_ADJUDICATION_I_9_1_20260719.md',
    'PACKAGE_WIDE_PUBLIC_SAFETY_VALIDATION.txt',
    'PUBLIC_BUILD_SOURCE_RENDER_REVIEW_SUMMARY.md',
    'PUBLIC_I9_1_REVISION_HISTORY.md',
    'PUBLIC_MACHINE_LEDGER_SUMMARY.md',
    'PUBLICATION_READINESS.md',
    'REJECTED_CHECKPOINT_I_9_1_R1_CSV_PRIMARY_ID_ACCESSOR_20260719.md',
    'SGA1_English_source_sync_workpass.pdf',
    'SGA1_English_source_sync_workpass.tex',
    'SHA256SUMS.txt',
    'SOURCE_CHECK_AND_REVIEW_I_9_1.md',
    'SOURCE_UNIT_RECEIPT_I_9_1.md',
    'SUPERSESSION_AND_ARCHIVE_NOTE.md',
    'VALIDATE_CUMULATIVE_MACHINE_EVIDENCE.ps1',
    'VALIDATE_PUBLIC_MACHINE_CONTROLS.ps1',
    'VERIFY_PUBLIC_PAYLOAD.ps1',
    'VISUAL_QA_I_9_1_20260719.md',
    'ZENODO_PAYLOAD_MANIFEST.csv'
)
$actualPaths = @($all | ForEach-Object { Rel $root $_.FullName } | Sort-Object)
if ($all.Count -ne 110 -or ($actualPaths -join "`n") -cne (@($expectedPaths | Sort-Object) -join "`n")) { throw "Pinned payload path set mismatch: expected=110 actual=$($all.Count)" }
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
}
foreach ($file in $manifestTargets) { if (-not $manifestSeen.Contains((Rel $root $file.FullName))) { throw "Manifest set missing: $(Rel $root $file.FullName)" } }

$tex=Join-Path $root 'SGA1_English_source_sync_workpass.tex'
$fragment=Join-Path $root 'drafts\SGA1_I_9_1_English_source_draft.texfrag'
$pdf=Join-Path $root 'SGA1_English_source_sync_workpass.pdf'
if ((Get-Item $tex).Length -ne 18709 -or (Sha $tex) -cne 'C6B9C7BF1F204E706E7B06889414651A8510B9E376CD6099599467A4E911C2B1') { throw 'TeX identity failed' }
if ((Get-Item $fragment).Length -ne 2848 -or (Sha $fragment) -cne 'BBDE49C52927FE7817B5B5D788488144B21DA1B5481CDFF8D4F5212D8098A4F8') { throw 'I.9.1 fragment identity failed' }
if ((Get-Item $pdf).Length -ne 544941 -or (Sha $pdf) -cne 'F49C1FD1A051717E50AD4A67EFE4C144B38B7C62EC86F75F09F439BC3E379499') { throw 'PDF identity failed' }
$pdfInfo=@(& (Get-Command pdfinfo.exe -ErrorAction Stop).Source $pdf 2>&1) -join "`n"
if ($pdfInfo -notmatch '(?m)^Pages:\s+16\s*$' -or $pdfInfo -notmatch '(?m)^Encrypted:\s+no\s*$' -or $pdfInfo -notmatch '(?m)^Form:\s+none\s*$' -or $pdfInfo -notmatch '(?m)^JavaScript:\s+no\s*$' -or $pdfInfo -notmatch '(?m)^Suspects:\s+no\s*$' -or $pdfInfo -notmatch '(?m)^Title:\s+SGA 1 English source-synchronization workpass: Exposé I opening through I\.9\.1\s*$') { throw 'PDF metadata/security failed' }
$fonts=@(& (Get-Command pdffonts.exe -ErrorAction Stop).Source $pdf 2>&1 | Select-Object -Skip 2)
if ($fonts.Count -ne 30 -or @($fonts | Where-Object { $_ -notmatch '\s+yes\s+yes\s+yes\s+\d+\s+\d+\s*$' }).Count -ne 0) { throw 'PDF font gate failed' }

$diag='LaTeX Warning:|Package .* Warning:|Undefined control sequence|! LaTeX Error|Overfull \\hbox|Underfull \\hbox|There were undefined references|Rerun to get|Missing character'
foreach ($pass in 2..3) {
    $log=Join-Path $root "evidence\build\COMPILE_PASS${pass}_SANITIZED_FULL.log"
    if (@(Select-String -LiteralPath $log -Pattern $diag -AllMatches).Count -ne 0) { throw "Final compiler diagnostics in pass $pass" }
}
$renders=@(Get-ChildItem -LiteralPath (Join-Path $root 'evidence\rendered_pdf') -Filter '*.png' -File)
if ($renders.Count -ne 16) { throw 'Rendered-page count failed' }

$machine=@(& (Join-Path $root 'VALIDATE_PUBLIC_MACHINE_CONTROLS.ps1') 2>&1)
if (-not $? -or ($machine -join "`n") -notmatch 'Machine-ledger validation total\s+csv_rows=382; jsonl_records=18; failures=0') { throw 'Portable machine validation failed' }
$cumulativeMachine=@(& (Join-Path $root 'VALIDATE_CUMULATIVE_MACHINE_EVIDENCE.ps1') 2>&1)
if (-not $? -or ($cumulativeMachine -join "`n") -notmatch 'CUMULATIVE_MACHINE_EVIDENCE_VERIFY=PASS' -or ($cumulativeMachine -join "`n") -notmatch 'COMBINED_JSONL_UNIQUE_RECORDS=163') { throw 'Portable cumulative machine-evidence validation failed' }

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
    if ((Sha $file.FullName) -ceq '7898CBEABA04C4BF1DFF6D784B6366103EEA482F724BAFA594BE791AD4AEE1F6') { throw 'Original scan leaked into payload' }
}
Write-Output 'PUBLIC_PAYLOAD_VERIFY=PASS'
Write-Output "FILES=$($all.Count)"
Write-Output "PDF_BYTES=544941"
Write-Output 'PDF_PAGES=16'
Write-Output 'EDITABLE_SOURCE_FILES=6'
Write-Output 'CSV_FILES=40'
Write-Output 'CSV_ROWS=782'
Write-Output 'JSONL_FILES=12'
Write-Output 'JSONL_RECORDS=163'
Write-Output 'CURSOR=smf_doc-math_3_01.tex:1704 excluded begin corollary'