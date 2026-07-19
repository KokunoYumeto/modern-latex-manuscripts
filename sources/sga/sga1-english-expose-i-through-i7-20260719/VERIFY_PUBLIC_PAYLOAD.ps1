[CmdletBinding()]
param(
    [string] $Root = $PSScriptRoot
)

$ErrorActionPreference = 'Stop'
$failures = [Collections.Generic.List[string]]::new()

function Pass([string] $Name, [string] $Detail = '') {
    if ($Detail) { Write-Output "PASS`t$Name`t$Detail" }
    else { Write-Output "PASS`t$Name" }
}

function Fail([string] $Name, [string] $Detail) {
    $failures.Add("$Name :: $Detail")
    Write-Output "FAIL`t$Name`t$Detail"
}

function Sha([string] $Path) {
    (Get-FileHash -LiteralPath $Path -Algorithm SHA256).Hash
}

function Rel([string] $Path) {
    $Path.Substring($Root.Length + 1).Replace('\','/')
}

function Read-StrictUtf8([string] $Path) {
    $bytes = [IO.File]::ReadAllBytes($Path)
    $decoder = [Text.UTF8Encoding]::new($false, $true)
    try { $decoder.GetString($bytes) }
    catch { throw "Invalid UTF-8: $Path" }
}

function Read-Jsonl([string] $Path) {
    $records = @()
    $lineNo = 0
    foreach ($line in [IO.File]::ReadAllLines($Path, [Text.UTF8Encoding]::new($false, $true))) {
        $lineNo++
        if ([string]::IsNullOrWhiteSpace($line)) { continue }
        try { $records += ($line | ConvertFrom-Json -Depth 40) }
        catch { throw "JSONL parse failure at $Path line $lineNo" }
    }
    $records
}

function Read-CsvMatrix([string] $Path) {
    Add-Type -AssemblyName Microsoft.VisualBasic
    $parser = [Microsoft.VisualBasic.FileIO.TextFieldParser]::new($Path, [Text.Encoding]::UTF8, $true)
    $parser.TextFieldType = [Microsoft.VisualBasic.FileIO.FieldType]::Delimited
    $parser.SetDelimiters(',')
    $parser.HasFieldsEnclosedInQuotes = $true
    $rows = [Collections.Generic.List[object]]::new()
    try {
        while (-not $parser.EndOfData) { $rows.Add(@($parser.ReadFields())) }
    }
    finally { $parser.Close() }
    $rows
}

if (-not (Test-Path -LiteralPath $Root -PathType Container)) {
    throw "Payload root not found: $Root"
}
$Root = (Get-Item -LiteralPath $Root).FullName.TrimEnd('\')
$allFiles = @(Get-ChildItem -LiteralPath $Root -Recurse -File | Sort-Object FullName)
if ($allFiles.Count -eq 79) { Pass 'exact file count' 'files=79' }
else { Fail 'exact file count' "expected=79 actual=$($allFiles.Count)" }

$expectedRelativePaths = @(
    'BUILD_LOG_SANITIZATION.md',
    'BUILD_SOURCE_RENDER_REVIEW_SUMMARY.md',
    'CHECKPOINT_README.md',
    'CONTINUATION_CURSOR.md',
    'CURSOR_METADATA_CORRECTION_I_7_R10.md',
    'LICENSE_ATTRIBUTION.md',
    'MACHINE_LEDGER_I4_TERMINAL_STATE_RECONCILIATION.md',
    'MACHINE_LEDGER_LOCATOR_CORRECTION_I_7.md',
    'MACHINE_LEDGER_SUMMARY.md',
    'MANIFEST_SCOPE.md',
    'ORIGINAL_PRINT_ADJUDICATION_I_4.md',
    'ORIGINAL_PRINT_ADJUDICATION_I_5.md',
    'ORIGINAL_PRINT_ADJUDICATION_I_6.md',
    'ORIGINAL_PRINT_ADJUDICATION_I_7.md',
    'PACKAGE_WIDE_PUBLIC_SAFETY_VALIDATION.txt',
    'PUBLICATION_READINESS.md',
    'SGA1_English_source_sync_workpass.pdf',
    'SGA1_English_source_sync_workpass.tex',
    'SHA256SUMS.csv',
    'SOURCE_CHECK_AND_REVIEW_I_5.md',
    'SOURCE_CHECK_AND_REVIEW_I_6.md',
    'SOURCE_CHECK_AND_REVIEW_I_7.md',
    'SOURCE_UNIT_RECEIPT_I_5.md',
    'SOURCE_UNIT_RECEIPT_I_6.md',
    'SOURCE_UNIT_RECEIPT_I_7.md',
    'VERIFY_PUBLIC_PAYLOAD.ps1',
    'VISUAL_QA.md',
    'ZENODO_LIVE_CONTROL.json',
    'ZENODO_PAYLOAD_MANIFEST.csv',
    'drafts/SGA1_I_5_English_source_draft.texfrag',
    'drafts/SGA1_I_6_English_source_draft.texfrag',
    'drafts/SGA1_I_7_English_source_draft.texfrag',
    'evidence/build/BUILD_I_7_PASS1_PUBLIC.log',
    'evidence/build/BUILD_I_7_PASS1_SANITIZED_FULL.log',
    'evidence/build/BUILD_I_7_PASS2_PUBLIC.log',
    'evidence/build/BUILD_I_7_PASS2_SANITIZED_FULL.log',
    'evidence/build/BUILD_I_7_PASS3_PUBLIC.log',
    'evidence/build/BUILD_I_7_PASS3_SANITIZED_FULL.log',
    'evidence/rendered_pdf/page-1.png',
    'evidence/rendered_pdf/page-2.png',
    'evidence/rendered_pdf/page-3.png',
    'evidence/rendered_pdf/page-4.png',
    'evidence/rendered_pdf/page-5.png',
    'evidence/rendered_pdf/page-6.png',
    'evidence/rendered_pdf/page-7.png',
    'evidence/rendered_pdf/page-8.png',
    'evidence/rendered_pdf/page-9.png',
    'evidence/rendered_pdf/page-10.png',
    'evidence/rendered_pdf/page-11.png',
    'evidence/rendered_pdf/page-12.png',
    'evidence/rendered_pdf/page-13.png',
    'ledgers/PUBLIC_ADVERSE_AND_REJECTED_CHOICES.csv',
    'ledgers/PUBLIC_AUTHORITY_AND_COVERAGE.csv',
    'ledgers/PUBLIC_INDEX_RESTORATION_DEBT.csv',
    'ledgers/PUBLIC_MACHINE_VALIDATION_I_7.txt',
    'ledgers/PUBLIC_SGA1_I4_DIFFICULTY_FAILURE_REVISION.jsonl',
    'ledgers/PUBLIC_SGA1_I4_EVIDENCE_GRAPH.jsonl',
    'ledgers/PUBLIC_SGA1_I5_DIFFICULTY_FAILURE_REVISION.jsonl',
    'ledgers/PUBLIC_SGA1_I5_EVIDENCE_GRAPH.jsonl',
    'ledgers/PUBLIC_SGA1_I6_DIFFICULTY_FAILURE_REVISION.jsonl',
    'ledgers/PUBLIC_SGA1_I6_EVIDENCE_GRAPH.jsonl',
    'ledgers/PUBLIC_SGA1_I7_DIFFICULTY_FAILURE_REVISION.jsonl',
    'ledgers/PUBLIC_SGA1_I7_EVIDENCE_GRAPH.jsonl',
    'ledgers/PUBLIC_SGA1_MACHINE_LEDGER_SCHEMA_v4.json',
    'ledgers/PUBLIC_SGA1_NORMALIZATION_DELTA.csv',
    'ledgers/PUBLIC_SOURCE_COMPARISON_I_0_1.csv',
    'ledgers/PUBLIC_SOURCE_COMPARISON_I_2.csv',
    'ledgers/PUBLIC_SOURCE_COMPARISON_I_3.csv',
    'ledgers/PUBLIC_SOURCE_COMPARISON_I_4.csv',
    'ledgers/PUBLIC_SOURCE_COMPARISON_I_5.csv',
    'ledgers/PUBLIC_SOURCE_COMPARISON_I_6.csv',
    'ledgers/PUBLIC_SOURCE_COMPARISON_I_7.csv',
    'ledgers/PUBLIC_SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_0_1.csv',
    'ledgers/PUBLIC_SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_2.csv',
    'ledgers/PUBLIC_SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_3.csv',
    'ledgers/PUBLIC_SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_4.csv',
    'ledgers/PUBLIC_SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_5.csv',
    'ledgers/PUBLIC_SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_6.csv',
    'ledgers/PUBLIC_SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_7.csv'
)
$actualRelativePaths = @($allFiles | ForEach-Object { Rel $_.FullName } | Sort-Object)
$expectedRelativePaths = @($expectedRelativePaths | Sort-Object)
if (($actualRelativePaths -join "`n") -ceq ($expectedRelativePaths -join "`n")) { Pass 'exact relative-path allowlist' 'paths=79' }
else {
    $missing = @($expectedRelativePaths | Where-Object { $_ -notin $actualRelativePaths })
    $extra = @($actualRelativePaths | Where-Object { $_ -notin $expectedRelativePaths })
    Fail 'exact relative-path allowlist' "missing=$($missing -join ';') extra=$($extra -join ';')"
}

$expectedCore = @{
    'SGA1_English_source_sync_workpass.tex' = @{ bytes = 18547; sha = '687AECC96629EF7477FF4935468ADDCD653695C708F929ACC6C0020D43C58BEA' }
    'drafts/SGA1_I_5_English_source_draft.texfrag' = @{ bytes = 8801; sha = 'D0959C14AEC3D333EDE96AFFBC6FA8320A223B0A5F2B482B7DCE0268868E8FF9' }
    'drafts/SGA1_I_6_English_source_draft.texfrag' = @{ bytes = 2168; sha = '101CD6F1FC9C46E754E3AD31903863FCA2418DCF31A2E91D47637DF4815291EF' }
    'drafts/SGA1_I_7_English_source_draft.texfrag' = @{ bytes = 13003; sha = '9158A7291A27FD6346D2678A91B359C92A4BDA71CD93D2C24BCBD16856E78F01' }
    'SGA1_English_source_sync_workpass.pdf' = @{ bytes = 503370; sha = '082F09C965F8D2EB365B1E7BD9C8FEBC20F934C9265AAB0DC2BBEF915DA260F9' }
    'CONTINUATION_CURSOR.md' = @{ bytes = 585; sha = '990F14E11D950BAD8E05F824BA93CF1CEB149E730B6B5460EA670AECAF251824' }
    'CURSOR_METADATA_CORRECTION_I_7_R10.md' = @{ bytes = 1412; sha = '126ABA20948BF00E269D5B50DA471500B92F06ED4D0289CF6E255A07349A0CA8' }
}
foreach ($entry in $expectedCore.GetEnumerator()) {
    $path = Join-Path $Root $entry.Key
    if (-not (Test-Path -LiteralPath $path -PathType Leaf)) {
        Fail 'core artifact' "missing=$($entry.Key)"
        continue
    }
    $item = Get-Item -LiteralPath $path
    $hash = Sha $path
    if ($item.Length -eq $entry.Value.bytes -and $hash -ceq $entry.Value.sha) {
        Pass 'core artifact' "$($entry.Key) bytes=$($item.Length) sha256=$hash"
    }
    else { Fail 'core artifact' "$($entry.Key) bytes=$($item.Length) sha256=$hash" }
}

$cursorText = Read-StrictUtf8 (Join-Path $Root 'CONTINUATION_CURSOR.md')
$cursorCorrectionText = Read-StrictUtf8 (Join-Path $Root 'CURSOR_METADATA_CORRECTION_I_7_R10.md')
$correctCursorPhrase = 'Infinitesimal lifting of étale schemes. Application to formal schemes.'
$obsoleteCursorPhrase = 'global construction of unramified and étale morphisms'
if ($cursorText.Contains($correctCursorPhrase) -and -not $cursorText.Contains($obsoleteCursorPhrase) -and
    $cursorCorrectionText.Contains($correctCursorPhrase) -and -not $cursorCorrectionText.Contains($obsoleteCursorPhrase) -and
    $cursorCorrectionText.Contains('4422B54F8D37E0E051778F6FABDA6B70B5ADBB0AA3CE376DD1B90868A6C50A57')) {
    Pass 'cursor metadata semantics' 'correct I.8 descriptor and authority-slice hash retained; obsolete descriptor absent'
}
else { Fail 'cursor metadata semantics' 'corrected descriptor or source-slice identity absent, or obsolete descriptor retained' }

$mainTexPath = Join-Path $Root 'SGA1_English_source_sync_workpass.tex'
$i5FragmentPath = Join-Path $Root 'drafts\SGA1_I_5_English_source_draft.texfrag'
$i6FragmentPath = Join-Path $Root 'drafts\SGA1_I_6_English_source_draft.texfrag'
$i7FragmentPath = Join-Path $Root 'drafts\SGA1_I_7_English_source_draft.texfrag'
$mainTexText = if (Test-Path $mainTexPath) { Read-StrictUtf8 $mainTexPath } else { '' }
if ($mainTexText -match '\\input\{drafts/SGA1_I_5_English_source_draft\.texfrag\}' -and
    $mainTexText -match '\\input\{drafts/SGA1_I_6_English_source_draft\.texfrag\}' -and
    $mainTexText -match '\\input\{drafts/SGA1_I_7_English_source_draft\.texfrag\}') {
    Pass 'TeX dependencies declared' 'I.5, I.6, and I.7 fragments'
}
if (Test-Path $i7FragmentPath) {
    $i7Text = Read-StrictUtf8 $i7FragmentPath
    $i7Checks = @(
        $i7Text.Contains('\(\mathcal O''\) has the desired'),
        $i7Text.Contains('If \(\mathcal O\) is étale'),
        $i7Text.Contains('B''=A[u]'),
        $i7Text.Contains('\mathfrak n''=\mathfrak n\cap B'''),
        $i7Text.Contains('\mathfrak n''B''_{\mathfrak n''}')
    )
    if (@($i7Checks | Where-Object { -not $_ }).Count -eq 0) {
        Pass 'I.7 source-correction controls retained' 'O-prime, conditional, subalgebra, contraction, and localization prime present'
    }
    else { Fail 'I.7 source-correction controls retained' 'one or more controlled readings absent' }
}
else { Fail 'TeX dependencies declared' 'one or both required inputs missing' }
if (Test-Path $i5FragmentPath) {
    $fragmentText = Read-StrictUtf8 $i5FragmentPath
    if ($fragmentText -match 'surjective,\s*étale,\s*and\s*radicial' -and $fragmentText -match '(?s)\\operatorname\{Spec\}\(k\).*?\\varepsilon\^2') {
        Pass 'source-defect disclosure retained' 'I.5.3 criterion and counterexample present'
    }
    else { Fail 'source-defect disclosure retained' 'required corrected criterion or disclosure absent' }
}
if (Test-Path $i6FragmentPath) {
    $i6Text = Read-StrictUtf8 $i6FragmentPath
    $i6Checks = @(
        $i6Text.Contains('R(B)=B\otimes_A k'),
        $i6Text.Contains('\operatorname{Hom}_{A\text{-alg}}(B,B'')'),
        $i6Text.Contains('\operatorname{Hom}_{k\text{-alg}}\bigl(R(B),R(B'')\bigr)'),
        $i6Text.Contains('B=A[t]/F_1A[t]')
    )
    if (@($i6Checks | Where-Object { -not $_ }).Count -eq 0) {
        Pass 'I.6 formula controls retained' 'R, Hom variance, and lifted quotient present'
    }
    else { Fail 'I.6 formula controls retained' 'one or more controlled formulas absent' }
}

$textExtensions = @('.tex','.texfrag','.md','.csv','.log','.txt','.json','.jsonl','.ps1')
$internalPatterns = @(
    @{ name='thread identifier field'; pattern='(?i)\b(?:source|parent|child)[_-]?thread[_-]?id\b' },
    @{ name='task upload control'; pattern='(?i)\bPUBLIC_[A-Z0-9_]*UPLOAD\b' },
    @{ name='workflow control tag'; pattern='(?i)<[a-z][a-z0-9]*_[a-z][a-z0-9_-]*>' },
    @{ name='hidden workflow directory'; pattern='(?i)(?<![A-Za-z0-9])_[a-z]+_[a-z]+\b' },
    @{ name='manager decision identifier'; pattern='\b[A-Z]{2,}(?:-[A-Z0-9]+){2,}-\d{8}-\d{4}\b' },
    @{ name='numbered archive task path'; pattern='(?<!\d)\d(?!\d)\s+[a-z][a-z0-9._-]{3,}/[a-z][a-z0-9._-]{3,}\b' }
)
foreach ($file in @($allFiles | Where-Object { $_.Extension.ToLowerInvariant() -in $textExtensions })) {
    try { $content = Read-StrictUtf8 $file.FullName }
    catch { Fail 'strict UTF-8' (Rel $file.FullName); continue }
    $normalizedContent = $content.Replace('\','/')
    if ($content -match '(?i)(?<![A-Za-z0-9])[A-Z]:[\\/]' -or $normalizedContent -match '(?i)(?:^|[\s"''=])/(?:users|home)/[A-Za-z0-9._-]+/') {
        Fail 'public privacy' "absolute local path in $(Rel $file.FullName)"
    }
    if ($content -match '(?i)\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b') {
        Fail 'public privacy' "UUID in $(Rel $file.FullName)"
    }
    if ($content -match '(?i)\b(?:api[_-]?key|access[_-]?token|secret|password)\s*[:=]') {
        Fail 'public privacy' "secret-like assignment in $(Rel $file.FullName)"
    }
    foreach ($control in $internalPatterns) {
        if ($content -match $control.pattern) { Fail 'public privacy' "pattern=$($control.name) file=$(Rel $file.FullName)" }
    }
}
$forbiddenExtensions = @('.zip','.tar','.gz','.jpg','.jpeg','.tif','.tiff')
$forbiddenFiles = @($allFiles | Where-Object { $_.Extension.ToLowerInvariant() -in $forbiddenExtensions })
if ($forbiddenFiles.Count -eq 0) { Pass 'source and scan exclusion' 'no archive or scan-image extensions' }
else { Fail 'source and scan exclusion' (($forbiddenFiles | ForEach-Object { Rel $_.FullName }) -join ',') }

$expectedBinaryPaths = @('SGA1_English_source_sync_workpass.pdf') + @(1..13 | ForEach-Object { "evidence/rendered_pdf/page-$_.png" })
$actualBinaryPaths = @($allFiles | Where-Object { $_.Extension.ToLowerInvariant() -in @('.pdf','.png','.jpg','.jpeg','.tif','.tiff') } | ForEach-Object { Rel $_.FullName } | Sort-Object)
$expectedBinaryPaths = @($expectedBinaryPaths | Sort-Object)
if (($actualBinaryPaths -join "`n") -ceq ($expectedBinaryPaths -join "`n")) {
    Pass 'exact binary allowlist' 'one English PDF and thirteen English-PDF page renders'
}
else {
    $missingBinary = @($expectedBinaryPaths | Where-Object { $_ -notin $actualBinaryPaths })
    $extraBinary = @($actualBinaryPaths | Where-Object { $_ -notin $expectedBinaryPaths })
    Fail 'exact binary allowlist' "missing=$($missingBinary -join ';') extra=$($extraBinary -join ';')"
}

$renderFiles = @(Get-ChildItem -LiteralPath (Join-Path $Root 'evidence\rendered_pdf') -Filter '*.png' -File -ErrorAction SilentlyContinue)
if ($renderFiles.Count -eq 13) { Pass 'render evidence count' 'png=13' }
else { Fail 'render evidence count' "expected=13 actual=$($renderFiles.Count)" }

$buildFiles = @(Get-ChildItem -LiteralPath (Join-Path $Root 'evidence\build') -File -ErrorAction SilentlyContinue)
if ($buildFiles.Count -eq 6) { Pass 'public build evidence count' 'files=6' }
else { Fail 'public build evidence count' "expected=6 actual=$($buildFiles.Count)" }
$sanitizedSuffix = '_SANITIZED' + '_FULL.log'
foreach ($log in $buildFiles) {
    $text = Read-StrictUtf8 $log.FullName
    $hits = [regex]::Matches($text, '(?mi)LaTeX Warning|Package .+ Warning|Class .+ Warning|Overfull \\hbox|Underfull \\hbox|! LaTeX Error|Fatal error|Emergency stop|Undefined control sequence').Count
    $outputEvidence = $false
    if ($log.Name -like '*_PUBLIC.log') {
        $outputEvidence = $text -match 'Output written on SGA1_English_source_sync_workpass\.pdf \(13 pages, 503370 bytes\)'
    }
    elseif ($log.Name.EndsWith($sanitizedSuffix, [StringComparison]::OrdinalIgnoreCase)) {
        $outputEvidence =
            $text -match '(?m)^verified_output=SGA1_English_source_sync_workpass\.pdf; pages=13; bytes=503370\r?$' -and
            $text -match '(?m)^---END SANITIZED FULL COMPILER LOG---\r?$'
    }
    if ($hits -eq 0 -and $outputEvidence) { Pass 'public build log' "$(Rel $log.FullName) diagnostics=0" }
    else { Fail 'public build log' "$(Rel $log.FullName) diagnostics=$hits or type-specific output evidence absent" }
}

$ledgerDir = Join-Path $Root 'ledgers'
$csvLedgers = @(Get-ChildItem -LiteralPath $ledgerDir -Filter '*.csv' -File | Sort-Object Name)
$csvRowsTotal = 0
if ($csvLedgers.Count -eq 18) { Pass 'ledger CSV file count' 'files=18' }
else { Fail 'ledger CSV file count' "expected=18 actual=$($csvLedgers.Count)" }
foreach ($csv in $csvLedgers) {
    try { $matrix = @(Read-CsvMatrix $csv.FullName) }
    catch { Fail 'CSV parse' "$(Rel $csv.FullName): $($_.Exception.Message)"; continue }
    if ($matrix.Count -lt 1) { Fail 'CSV rectangular' "$(Rel $csv.FullName): empty"; continue }
    $columns = $matrix[0].Count
    $dataRows = @($matrix | Select-Object -Skip 1)
    $csvRowsTotal += $dataRows.Count
    $badWidth = @($dataRows | Where-Object { $_.Count -ne $columns }).Count
    if ($badWidth -eq 0) { Pass 'CSV rectangular' "$(Rel $csv.FullName) rows=$($dataRows.Count) columns=$columns" }
    else { Fail 'CSV rectangular' "$(Rel $csv.FullName) bad_rows=$badWidth" }
    $ids = @($dataRows | ForEach-Object { [string]$_[0] })
    if (@($ids | Group-Object | Where-Object Count -gt 1).Count -eq 0 -and @($ids | Where-Object { [string]::IsNullOrWhiteSpace($_) }).Count -eq 0) {
        Pass 'CSV primary IDs' "$(Rel $csv.FullName) unique=$($ids.Count)"
    }
    else { Fail 'CSV primary IDs' "$(Rel $csv.FullName) duplicate or blank" }
    $unsafe = 0
    foreach ($row in $dataRows) {
        foreach ($cell in $row) {
            if ([string]$cell -match '^[\s]*[=+@]' -or [string]$cell -match '^[\s]*-(?!\d)') { $unsafe++ }
        }
    }
    if ($unsafe -eq 0) { Pass 'CSV formula safety' (Rel $csv.FullName) }
    else { Fail 'CSV formula safety' "$(Rel $csv.FullName) unsafe_cells=$unsafe" }
}
if ($csvRowsTotal -eq 344) { Pass 'CSV total rows' 'rows=344' }
else { Fail 'CSV total rows' "expected=344 actual=$csvRowsTotal" }

$jsonlFiles = @(Get-ChildItem -LiteralPath $ledgerDir -Filter '*.jsonl' -File | Sort-Object Name)
if ($jsonlFiles.Count -eq 8) { Pass 'JSONL file count' 'files=8' }
else { Fail 'JSONL file count' "expected=8 actual=$($jsonlFiles.Count)" }
$records = @()
foreach ($jsonl in $jsonlFiles) {
    try {
        $part = @(Read-Jsonl $jsonl.FullName)
        $records += $part
        Pass 'JSONL parse' "$(Rel $jsonl.FullName) records=$($part.Count)"
    }
    catch { Fail 'JSONL parse' "$(Rel $jsonl.FullName): $($_.Exception.Message)" }
}
if ($records.Count -eq 118) { Pass 'JSONL total records' 'records=118' }
else { Fail 'JSONL total records' "expected=118 actual=$($records.Count)" }
$idGroups = @($records | Group-Object record_id)
if (@($idGroups | Where-Object Count -ne 1).Count -eq 0 -and @($records | Where-Object { [string]::IsNullOrWhiteSpace($_.record_id) }).Count -eq 0) {
    Pass 'JSONL unique IDs' "ids=$($records.Count)"
}
else { Fail 'JSONL unique IDs' 'duplicate or blank record_id' }
$recordMap = @{}
foreach ($record in $records) { $recordMap[[string]$record.record_id] = $record }
$graphRequired = @('schema_version','record_id','record_type','evidence_class','authority_role','parent_id','child_ids','source_locator','target_locator','local_reference_ids','external_reference_ids','decision','status','confidence','adverse_alternatives','revision_record_id','supersedes_record_ids','superseded_by_record_id','continuation_cursor')
$difficultyRequired = @('schema_version','record_id','record_type','evidence_class','authority_role','parent_id','child_ids','source_locator','target_locator','decision','status','confidence','difficulty','adverse_alternatives','revision','supersedes_record_ids','superseded_by_record_id','closes_record_ids','closed_by_record_id','related_record_ids','continuation_cursor','revisit_condition')
$referenceFields = @('parent_id','child_ids','local_reference_ids','revision_record_id','supersedes_record_ids','superseded_by_record_id','closes_record_ids','closed_by_record_id','related_record_ids')
foreach ($record in $records) {
    $required = if ([string]$record.schema_version -eq 'sga1_evidence_graph.v1') { $graphRequired } else { $difficultyRequired }
    $missing = @($required | Where-Object { $_ -notin $record.PSObject.Properties.Name })
    if ($missing.Count -gt 0) { Fail 'JSONL required fields' "$($record.record_id) missing=$($missing -join ',')" }
    foreach ($field in $referenceFields) {
        if ($field -notin $record.PSObject.Properties.Name) { continue }
        $values = @($record.$field) | Where-Object { -not [string]::IsNullOrWhiteSpace([string]$_) }
        if (@($values | Group-Object | Where-Object Count -gt 1).Count -gt 0) { Fail 'JSONL duplicate references' "$($record.record_id) field=$field" }
        foreach ($value in $values) {
            $id = [string]$value
            if ($id -eq $record.record_id) { Fail 'JSONL self reference' "$($record.record_id) field=$field" }
            if ($id.StartsWith('SGA1-') -and -not $recordMap.ContainsKey($id)) { Fail 'JSONL reference closure' "$($record.record_id) -> $id" }
        }
    }
    if (-not [string]::IsNullOrWhiteSpace([string]$record.parent_id) -and $recordMap.ContainsKey([string]$record.parent_id)) {
        if ([string]$record.record_id -notin @($recordMap[[string]$record.parent_id].child_ids)) {
            Fail 'JSONL parent-child reciprocity' "$($record.record_id) missing from parent $($record.parent_id)"
        }
    }
    foreach ($child in @($record.child_ids)) {
        if ($recordMap.ContainsKey([string]$child) -and [string]$recordMap[[string]$child].parent_id -ne [string]$record.record_id) {
            Fail 'JSONL parent-child reciprocity' "$($record.record_id) child=$child"
        }
    }
    if ([string]$record.status -eq 'superseded') {
        if ([string]::IsNullOrWhiteSpace([string]$record.superseded_by_record_id)) {
            Fail 'JSONL superseded status closure' "$($record.record_id) has no successor"
        }
        elseif ($recordMap.ContainsKey([string]$record.superseded_by_record_id) -and [string]$record.record_id -notin @($recordMap[[string]$record.superseded_by_record_id].supersedes_record_ids)) {
            Fail 'JSONL supersession reciprocity' "$($record.record_id) -> $($record.superseded_by_record_id)"
        }
    }
    if (-not [string]::IsNullOrWhiteSpace([string]$record.closed_by_record_id) -and $recordMap.ContainsKey([string]$record.closed_by_record_id)) {
        if ([string]$record.record_id -notin @($recordMap[[string]$record.closed_by_record_id].closes_record_ids)) {
            Fail 'JSONL closure reciprocity' "$($record.record_id) -> $($record.closed_by_record_id)"
        }
    }
    foreach ($closedId in @($record.closes_record_ids)) {
        if ($recordMap.ContainsKey([string]$closedId) -and [string]$recordMap[[string]$closedId].closed_by_record_id -ne [string]$record.record_id) {
            Fail 'JSONL closure reciprocity' "$($record.record_id) closes=$closedId"
        }
    }
    $target = $record.target_locator
    if ($null -ne $target) {
        if ([long]$target.bytes -le 0 -or [string]$target.sha256 -cnotmatch '^[0-9A-F]{64}$') {
            Fail 'JSONL target identity' "$($record.record_id) requires positive bytes and uppercase SHA-256"
        }
    }
    if ($null -ne $target -and -not [string]::IsNullOrWhiteSpace([string]$target.relative_path)) {
        $targetPath = Join-Path $Root ([string]$target.relative_path).Replace('/','\')
        $resolvedRoot = [IO.Path]::GetFullPath($Root + '\')
        $resolvedTarget = [IO.Path]::GetFullPath($targetPath)
        if (-not $resolvedTarget.StartsWith($resolvedRoot, [StringComparison]::OrdinalIgnoreCase)) {
            Fail 'JSONL target path' "$($record.record_id) escapes root"
        }
        elseif (-not (Test-Path -LiteralPath $resolvedTarget -PathType Leaf)) {
            Fail 'JSONL target path' "$($record.record_id) missing=$($target.relative_path)"
        }
        else {
            $item = Get-Item -LiteralPath $resolvedTarget
            $hash = Sha $resolvedTarget
            if ($item.Length -ne [long]$target.bytes -or $hash -cne [string]$target.sha256) {
                Fail 'JSONL target integrity' "$($record.record_id) path=$($target.relative_path)"
            }
        }
    }
}
$statusGroups = @{}
foreach ($g in ($records | Group-Object status)) { $statusGroups[$g.Name] = $g.Count }
if ($statusGroups['closed_corrected'] -eq 98 -and $statusGroups['rejected'] -eq 15 -and $statusGroups['superseded'] -eq 5) {
    Pass 'JSONL terminal statuses' 'closed_corrected=98 rejected=15 superseded=5'
}
else { Fail 'JSONL terminal statuses' (($statusGroups | ConvertTo-Json -Compress)) }

$schemaPath = Join-Path $ledgerDir 'PUBLIC_SGA1_MACHINE_LEDGER_SCHEMA_v4.json'
try {
    $schema = (Read-StrictUtf8 $schemaPath) | ConvertFrom-Json -Depth 40
    if ($schema.schema_id -eq 'sga1_public_machine_ledgers.v4' -and @($schema.csv_ledgers.PSObject.Properties).Count -eq 18 -and
        @($schema.graph_jsonl).Count -eq 4 -and @($schema.difficulty_jsonl).Count -eq 4 -and
        [long]$schema.continuation_cursor.line -eq 1493 -and $schema.continuation_cursor.excluded -eq $true) {
        Pass 'public schema' "sha256=$(Sha $schemaPath) csv_ledgers=18 jsonl=8 cursor=1493"
    }
    else { Fail 'public schema' 'unexpected schema id or CSV declaration count' }
}
catch { Fail 'public schema' $_.Exception.Message }
$machineReceipt = Join-Path $ledgerDir 'PUBLIC_MACHINE_VALIDATION_I_7.txt'
if ((Test-Path $machineReceipt) -and (Read-StrictUtf8 $machineReceipt) -match 'failures=0' -and (Read-StrictUtf8 $machineReceipt) -match 'csv_rows=344' -and (Read-StrictUtf8 $machineReceipt) -match 'jsonl_records=118' -and (Read-StrictUtf8 $machineReceipt) -match 'continuation_line=1493') {
    Pass 'public machine receipt' "sha256=$(Sha $machineReceipt)"
}
else { Fail 'public machine receipt' 'missing or incomplete zero-failure receipt' }

$shaPath = Join-Path $Root 'SHA256SUMS.csv'
try {
    $shaRows = @(Import-Csv -LiteralPath $shaPath)
    if (($shaRows[0].PSObject.Properties.Name -join ',') -cne 'relative_path,bytes,sha256') { Fail 'checksum header' 'unexpected header' }
    $expectedPaths = @($allFiles | Where-Object { (Rel $_.FullName) -ne 'SHA256SUMS.csv' } | ForEach-Object { Rel $_.FullName } | Sort-Object)
    $listedPaths = @($shaRows.relative_path | Sort-Object)
    if ($shaRows.Count -eq 78 -and (($expectedPaths -join "`n") -ceq ($listedPaths -join "`n"))) { Pass 'checksum exact set' 'rows=78' }
    else { Fail 'checksum exact set' "rows=$($shaRows.Count)" }
    foreach ($row in $shaRows) {
        $path = Join-Path $Root $row.relative_path.Replace('/','\')
        if (-not (Test-Path $path) -or (Get-Item $path).Length -ne [long]$row.bytes -or (Sha $path) -cne $row.sha256) {
            Fail 'checksum row' $row.relative_path
        }
    }
}
catch { Fail 'checksum manifest' $_.Exception.Message }

$zenodoPath = Join-Path $Root 'ZENODO_PAYLOAD_MANIFEST.csv'
try {
    $zenRows = @(Import-Csv -LiteralPath $zenodoPath)
    $expectedZenPaths = @($allFiles | Where-Object { (Rel $_.FullName) -notin @('SHA256SUMS.csv','ZENODO_PAYLOAD_MANIFEST.csv') } | ForEach-Object { Rel $_.FullName } | Sort-Object)
    $listedZenPaths = @($zenRows.relative_path | Sort-Object)
    if ($zenRows.Count -eq 77 -and (($expectedZenPaths -join "`n") -ceq ($listedZenPaths -join "`n"))) { Pass 'Zenodo manifest exact set' 'rows=77' }
    else { Fail 'Zenodo manifest exact set' "rows=$($zenRows.Count)" }
    foreach ($row in $zenRows) {
        $path = Join-Path $Root $row.relative_path.Replace('/','\')
        if (-not (Test-Path $path) -or (Get-Item $path).Length -ne [long]$row.bytes -or (Sha $path) -cne $row.sha256) {
            Fail 'Zenodo manifest row' $row.relative_path
        }
        if ($row.publication_action -cne 'PUBLISH_ONLY_AFTER_ARCHIVE_RIGHTS_SCOPE_AND_LIVE_STATE_REVIEW') {
            Fail 'Zenodo publication action' $row.relative_path
        }
    }
}
catch { Fail 'Zenodo manifest' $_.Exception.Message }

$livePath = Join-Path $Root 'ZENODO_LIVE_CONTROL.json'
try {
    $live = (Read-StrictUtf8 $livePath) | ConvertFrom-Json -Depth 20
    if ($live.concept_doi -eq '10.5281/zenodo.20410947' -and $live.last_observed_version_doi -eq '10.5281/zenodo.21435547' -and $live.archive_owner_must_recheck_before_upload -eq $true -and $live.freeze_second_observation_match -eq $true) {
        Pass 'live Zenodo control' "observed=$($live.last_observed_version_doi) files=$($live.file_count)"
    }
    else { Fail 'live Zenodo control' 'unexpected DOI or recheck control' }
}
catch { Fail 'live Zenodo control' $_.Exception.Message }

if ($failures.Count -eq 0) {
    Write-Output 'failures=0'
    Write-Output 'PUBLIC_PAYLOAD_VERIFY=PASS'
    exit 0
}
Write-Output "failures=$($failures.Count)"
foreach ($failure in $failures) { Write-Output "failure=$failure" }
Write-Output 'PUBLIC_PAYLOAD_VERIFY=FAIL'
exit 1
