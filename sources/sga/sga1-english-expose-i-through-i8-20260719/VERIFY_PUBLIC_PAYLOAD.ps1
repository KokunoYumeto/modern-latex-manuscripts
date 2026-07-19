[CmdletBinding()]
param(
    [string] $Root = $PSScriptRoot
)

$ErrorActionPreference = 'Stop'
$failures = [Collections.Generic.List[string]]::new()

function Pass([string] $Name, [string] $Detail = '') {
    if ($Detail) { Write-Output "PASS`t$Name`t$Detail" } else { Write-Output "PASS`t$Name" }
}
function Fail([string] $Name, [string] $Detail) {
    $failures.Add("$Name :: $Detail")
    Write-Output "FAIL`t$Name`t$Detail"
}
function Sha([string] $Path) { (Get-FileHash -LiteralPath $Path -Algorithm SHA256).Hash }
function Rel([string] $Path) { $Path.Substring($Root.Length + 1).Replace('\','/') }
function Read-StrictUtf8([string] $Path) {
    $bytes = [IO.File]::ReadAllBytes($Path)
    [Text.UTF8Encoding]::new($false,$true).GetString($bytes)
}
function Read-CsvMatrix([string] $Path) {
    Add-Type -AssemblyName Microsoft.VisualBasic
    $parser = [Microsoft.VisualBasic.FileIO.TextFieldParser]::new($Path, [Text.Encoding]::UTF8, $true)
    $parser.TextFieldType = [Microsoft.VisualBasic.FileIO.FieldType]::Delimited
    $parser.SetDelimiters(',')
    $parser.HasFieldsEnclosedInQuotes = $true
    $rows = [Collections.Generic.List[object]]::new()
    try { while (-not $parser.EndOfData) { $rows.Add(@($parser.ReadFields())) } }
    finally { $parser.Close() }
    $rows
}
function Read-Jsonl([string] $Path) {
    $records = @()
    $lineNo = 0
    foreach ($line in [IO.File]::ReadAllLines($Path, [Text.UTF8Encoding]::new($false,$true))) {
        $lineNo++
        if ([string]::IsNullOrWhiteSpace($line)) { continue }
        try { $records += ($line | ConvertFrom-Json -Depth 40) }
        catch { throw "JSONL parse failure at $Path line $lineNo" }
    }
    $records
}

if (-not (Test-Path -LiteralPath $Root -PathType Container)) { throw "Payload root not found: $Root" }
$Root = (Get-Item -LiteralPath $Root).FullName.TrimEnd('\')
$expectedFileCount = [int]'96'
$expectedTexBytes = [long]'18482'
$expectedPdfBytes = [long]'539984'
$allFiles = @(Get-ChildItem -LiteralPath $Root -Recurse -File | Sort-Object FullName)
if ($allFiles.Count -eq $expectedFileCount) { Pass 'exact file count' "files=$expectedFileCount" }
else { Fail 'exact file count' "expected=$expectedFileCount actual=$($allFiles.Count)" }

$core = @{
    'SGA1_English_source_sync_workpass.tex' = @{ bytes=$expectedTexBytes; sha='55671B1DDC22770A056E23D3BB4052CAC9EDF642893B04747D7EF84376CD23C9' }
    'SGA1_English_source_sync_workpass.pdf' = @{ bytes=$expectedPdfBytes; sha='76447BE947C25C89D882AD07BE8814109C7943EA31FB2401ED0D3C6D4A597EB9' }
    'drafts/SGA1_I_8_English_source_draft.texfrag' = @{ bytes=7567; sha='4C25DB6731B4AC26CBDB65E8F5EA2B289A95CA7ADACAC7DD0464451B81F5BCA8' }
    'evidence/prior_checkpoint/SGA1_I7_r10_source_sync_workpass.tex' = @{ bytes=18547; sha='687AECC96629EF7477FF4935468ADDCD653695C708F929ACC6C0020D43C58BEA' }
    'evidence/prior_checkpoint/SGA1_I7_r10_source_sync_workpass.pdf' = @{ bytes=503370; sha='082F09C965F8D2EB365B1E7BD9C8FEBC20F934C9265AAB0DC2BBEF915DA260F9' }
}
foreach ($entry in $core.GetEnumerator()) {
    $path = Join-Path $Root $entry.Key.Replace('/','\')
    if (-not (Test-Path -LiteralPath $path -PathType Leaf)) { Fail 'core artifact' "missing=$($entry.Key)"; continue }
    $item = Get-Item -LiteralPath $path
    $hash = Sha $path
    if ($item.Length -eq [long]$entry.Value.bytes -and $hash -ceq [string]$entry.Value.sha) {
        Pass 'core artifact' "$($entry.Key) bytes=$($item.Length) sha256=$hash"
    }
    else { Fail 'core artifact' "$($entry.Key) bytes=$($item.Length) sha256=$hash" }
}

$mainText = Read-StrictUtf8 (Join-Path $Root 'SGA1_English_source_sync_workpass.tex')
$dependencies = @('I_5','I_6','I_7','I_8')
foreach ($unit in $dependencies) {
    if ($mainText -match "\\input\{drafts/SGA1_${unit}_English_source_draft\.texfrag\}") { Pass 'TeX dependency' $unit }
    else { Fail 'TeX dependency' $unit }
}
if ($mainText.Contains('lines 556--1653') -and $mainText.Contains('line 1654 begins \S\,I.9')) {
    Pass 'main boundary declaration' 'included=556-1653 excluded=1654'
}
else { Fail 'main boundary declaration' 'exact I.8 terminal cursor absent' }
$i8Text = Read-StrictUtf8 (Join-Path $Root 'drafts\SGA1_I_8_English_source_draft.texfrag')
$i8Checks = @(
    $i8Text.Contains('B\otimes_A A_0\xrightarrow{\sim}B_0'),
    $i8Text.Contains('\mathcal O_z\) is \(A\)-isomorphic to~\(B\)'),
    $i8Text.Contains('EGA, Chapter~I'),
    ($i8Text -match 'Corollary~\\ref\{I\.7\.5\}\s+in place of\s+Theorem~\\ref\{I\.7\.6\}'),
    $i8Text.Contains('alternate \(J\) and \(\mathcal J\)'),
    $i8Text.Contains('\mathcal B_m\otimes_{\mathcal O_{S_m}}\mathcal O_{S_n}'),
    -not $i8Text.Contains('Properties of permanence')
)
if (@($i8Checks | Where-Object { -not $_ }).Count -eq 0) { Pass 'I.8 controlled readings' 'all material corrections and excluded cursor retained' }
else { Fail 'I.8 controlled readings' 'one or more controlled readings absent' }

$textExtensions = @('.tex','.texfrag','.md','.csv','.log','.txt','.json','.jsonl','.ps1')
$privatePatterns = @(
    @{ name='absolute Windows path'; pattern='(?i)(?<![A-Za-z0-9])[A-Z]:[\\/]' },
    @{ name='absolute user path'; pattern='(?i)(?:^|[\s"''=])/(?:users|home)/[A-Za-z0-9._-]+/' },
    @{ name='UUID'; pattern='(?i)\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b' },
    @{ name='thread field'; pattern='(?i)\b(?:source|parent|child)[_-]?thread[_-]?id\b' },
    @{ name='upload workflow token'; pattern=('(?i)PUBLIC_[A-Z0-9_]*UPLOAD|codex_' + 'delegation|1 zenodo/' + 'github') },
    @{ name='secret assignment'; pattern='(?i)\b(?:api[_-]?key|access[_-]?token|secret|password)\s*[:=]' }
)
foreach ($file in @($allFiles | Where-Object { $_.Extension.ToLowerInvariant() -in $textExtensions })) {
    try { $content = Read-StrictUtf8 $file.FullName }
    catch { Fail 'strict UTF-8' (Rel $file.FullName); continue }
    foreach ($control in $privatePatterns) {
        if ($content -match $control.pattern) { Fail 'public privacy' "pattern=$($control.name) file=$(Rel $file.FullName)" }
    }
}
$forbiddenExtensions = @('.zip','.tar','.gz','.jpg','.jpeg','.tif','.tiff')
$forbidden = @($allFiles | Where-Object { $_.Extension.ToLowerInvariant() -in $forbiddenExtensions })
if ($forbidden.Count -eq 0) { Pass 'source and scan exclusion' 'no archive or scan-image extensions' }
else { Fail 'source and scan exclusion' (($forbidden | ForEach-Object { Rel $_.FullName }) -join ',') }

$expectedBinary = @(
    'SGA1_English_source_sync_workpass.pdf',
    'evidence/prior_checkpoint/SGA1_I7_r10_source_sync_workpass.pdf'
) + @(1..15 | ForEach-Object { "evidence/rendered_pdf/page-$_.png" })
$actualBinary = @($allFiles | Where-Object { $_.Extension.ToLowerInvariant() -in @('.pdf','.png','.jpg','.jpeg','.tif','.tiff') } | ForEach-Object { Rel $_.FullName } | Sort-Object)
if (($expectedBinary | Sort-Object) -join "`n" -ceq ($actualBinary -join "`n")) { Pass 'exact binary allowlist' 'two English PDFs and fifteen final-PDF renders' }
else { Fail 'exact binary allowlist' "expected=$($expectedBinary.Count) actual=$($actualBinary.Count)" }

$renders = @(Get-ChildItem -LiteralPath (Join-Path $Root 'evidence\rendered_pdf') -Filter '*.png' -File)
if ($renders.Count -eq 15) { Pass 'render evidence count' 'png=15' }
else { Fail 'render evidence count' "expected=15 actual=$($renders.Count)" }
$buildFiles = @(Get-ChildItem -LiteralPath (Join-Path $Root 'evidence\build') -File)
if ($buildFiles.Count -eq 6) { Pass 'build evidence count' 'files=6' }
else { Fail 'build evidence count' "expected=6 actual=$($buildFiles.Count)" }
foreach ($pass in 1..3) {
    $receiptPath = Join-Path $Root "evidence\build\BUILD_I_8_PASS${pass}_PUBLIC.log"
    $fullPath = Join-Path $Root "evidence\build\BUILD_I_8_PASS${pass}_SANITIZED_FULL.log"
    if (-not (Test-Path $receiptPath) -or -not (Test-Path $fullPath)) { Fail 'build pass' "missing pass=$pass"; continue }
    $receipt = Read-StrictUtf8 $receiptPath
    $full = Read-StrictUtf8 $fullPath
    $expectedHits = if ($pass -eq 1) { 62 } else { 0 }
    $ok = $receipt.Contains("diagnostic_hits=$expectedHits") -and
        $receipt.Contains('Output written on SGA1_English_source_sync_workpass.pdf (15 pages, 539984 bytes; SHA-256 76447BE947C25C89D882AD07BE8814109C7943EA31FB2401ED0D3C6D4A597EB9)') -and
        $full.Contains("diagnostic_hits=$expectedHits") -and
        $full.Contains('verified_output=SGA1_English_source_sync_workpass.pdf; pages=15; bytes=539984; sha256=76447BE947C25C89D882AD07BE8814109C7943EA31FB2401ED0D3C6D4A597EB9') -and
        $full.Contains('---END SANITIZED FULL COMPILER LOG---')
    if ($ok) { Pass 'build pass' "pass=$pass diagnostics=$expectedHits" }
    else { Fail 'build pass' "pass=$pass receipt or terminus mismatch" }
}

$ledgerDir = Join-Path $Root 'ledgers'
$schemaPath = Join-Path $ledgerDir 'PUBLIC_SGA1_MACHINE_LEDGER_SCHEMA_v5.json'
try { $schema = (Read-StrictUtf8 $schemaPath) | ConvertFrom-Json -Depth 40 }
catch { $schema = $null; Fail 'public schema' $_.Exception.Message }
$csvLedgers = @(Get-ChildItem -LiteralPath $ledgerDir -Filter '*.csv' -File | Sort-Object Name)
$csvRowsTotal = 0
if ($csvLedgers.Count -eq 23) { Pass 'ledger CSV file count' 'files=23' }
else { Fail 'ledger CSV file count' "expected=23 actual=$($csvLedgers.Count)" }
foreach ($csv in $csvLedgers) {
    try { $matrix = @(Read-CsvMatrix $csv.FullName) }
    catch { Fail 'CSV parse' "$(Rel $csv.FullName): $($_.Exception.Message)"; continue }
    if ($matrix.Count -lt 1) { Fail 'CSV rectangular' "$(Rel $csv.FullName): empty"; continue }
    $columns = $matrix[0].Count
    $data = @($matrix | Select-Object -Skip 1)
    $csvRowsTotal += $data.Count
    if (@($data | Where-Object { $_.Count -ne $columns }).Count -eq 0) { Pass 'CSV rectangular' "$(Rel $csv.FullName) rows=$($data.Count) columns=$columns" }
    else { Fail 'CSV rectangular' (Rel $csv.FullName) }
    $ids = @($data | ForEach-Object { [string]$_[0] })
    if (@($ids | Group-Object | Where-Object Count -gt 1).Count -eq 0 -and @($ids | Where-Object { [string]::IsNullOrWhiteSpace($_) }).Count -eq 0) {
        Pass 'CSV primary IDs' "$(Rel $csv.FullName) unique=$($ids.Count)"
    }
    else { Fail 'CSV primary IDs' (Rel $csv.FullName) }
    $unsafe = 0
    foreach ($row in $data) { foreach ($cell in $row) { if ([string]$cell -match '^[\s]*[=+@]' -or [string]$cell -match '^[\s]*-(?!\d)') { $unsafe++ } } }
    if ($unsafe -eq 0) { Pass 'CSV formula safety' (Rel $csv.FullName) }
    else { Fail 'CSV formula safety' "$(Rel $csv.FullName) unsafe=$unsafe" }
    if ($null -ne $schema -and $csv.Name -in $schema.csv_ledgers.PSObject.Properties.Name) {
        $declared = @($schema.csv_ledgers.($csv.Name))
        if (($declared -join "`n") -ceq (@($matrix[0]) -join "`n")) { Pass 'CSV declared header' $csv.Name }
        else { Fail 'CSV declared header' $csv.Name }
    }
    else { Fail 'CSV schema declaration' $csv.Name }
}
if ($csvRowsTotal -eq 400) { Pass 'CSV total rows' 'rows=400' }
else { Fail 'CSV total rows' "expected=400 actual=$csvRowsTotal" }

$jsonlFiles = @(Get-ChildItem -LiteralPath $ledgerDir -Filter '*.jsonl' -File | Sort-Object Name)
if ($jsonlFiles.Count -eq 10) { Pass 'JSONL file count' 'files=10' }
else { Fail 'JSONL file count' "expected=10 actual=$($jsonlFiles.Count)" }
$records = @()
foreach ($jsonl in $jsonlFiles) {
    try { $part = @(Read-Jsonl $jsonl.FullName); $records += $part; Pass 'JSONL parse' "$(Rel $jsonl.FullName) records=$($part.Count)" }
    catch { Fail 'JSONL parse' "$(Rel $jsonl.FullName): $($_.Exception.Message)" }
}
if ($records.Count -eq 145) { Pass 'JSONL total records' 'records=145' }
else { Fail 'JSONL total records' "expected=145 actual=$($records.Count)" }
$groups = @($records | Group-Object record_id)
if (@($groups | Where-Object Count -ne 1).Count -eq 0 -and @($records | Where-Object { [string]::IsNullOrWhiteSpace($_.record_id) }).Count -eq 0) { Pass 'JSONL unique IDs' "ids=$($records.Count)" }
else { Fail 'JSONL unique IDs' 'duplicate or blank IDs' }
$map = @{}
foreach ($record in $records) { $map[[string]$record.record_id] = $record }
$graphRequired = @('schema_version','record_id','record_type','evidence_class','authority_role','parent_id','child_ids','source_locator','target_locator','local_reference_ids','external_reference_ids','decision','status','confidence','adverse_alternatives','revision_record_id','supersedes_record_ids','superseded_by_record_id','continuation_cursor')
$difficultyRequired = @('schema_version','record_id','record_type','evidence_class','authority_role','parent_id','child_ids','source_locator','target_locator','decision','status','confidence','difficulty','adverse_alternatives','revision','supersedes_record_ids','superseded_by_record_id','closes_record_ids','closed_by_record_id','related_record_ids','continuation_cursor','revisit_condition')
$referenceFields = @('parent_id','child_ids','local_reference_ids','revision_record_id','supersedes_record_ids','superseded_by_record_id','closes_record_ids','closed_by_record_id','related_record_ids')
foreach ($record in $records) {
    $required = if ([string]$record.schema_version -eq 'sga1_evidence_graph.v1') { $graphRequired } else { $difficultyRequired }
    $missing = @($required | Where-Object { $_ -notin $record.PSObject.Properties.Name })
    if ($missing.Count) { Fail 'JSONL required fields' "$($record.record_id) missing=$($missing -join ',')" }
    foreach ($field in $referenceFields) {
        if ($field -notin $record.PSObject.Properties.Name) { continue }
        $values = @($record.$field) | Where-Object { -not [string]::IsNullOrWhiteSpace([string]$_) }
        if (@($values | Group-Object | Where-Object Count -gt 1).Count) { Fail 'JSONL duplicate references' "$($record.record_id) field=$field" }
        foreach ($value in $values) {
            $id = [string]$value
            if ($id -eq $record.record_id) { Fail 'JSONL self reference' "$($record.record_id) field=$field" }
            if ($id.StartsWith('SGA1-') -and -not $map.ContainsKey($id)) { Fail 'JSONL reference closure' "$($record.record_id) -> $id" }
        }
    }
    if (-not [string]::IsNullOrWhiteSpace([string]$record.parent_id) -and $map.ContainsKey([string]$record.parent_id)) {
        if ([string]$record.record_id -notin @($map[[string]$record.parent_id].child_ids)) { Fail 'JSONL parent-child reciprocity' "$($record.record_id) parent=$($record.parent_id)" }
    }
    foreach ($child in @($record.child_ids)) {
        if ($map.ContainsKey([string]$child) -and [string]$map[[string]$child].parent_id -ne [string]$record.record_id) { Fail 'JSONL parent-child reciprocity' "$($record.record_id) child=$child" }
    }
    if ([string]$record.status -eq 'superseded') {
        if ([string]::IsNullOrWhiteSpace([string]$record.superseded_by_record_id)) { Fail 'JSONL superseded closure' $record.record_id }
        elseif ($map.ContainsKey([string]$record.superseded_by_record_id) -and [string]$record.record_id -notin @($map[[string]$record.superseded_by_record_id].supersedes_record_ids)) { Fail 'JSONL supersession reciprocity' $record.record_id }
    }
    if (-not [string]::IsNullOrWhiteSpace([string]$record.closed_by_record_id) -and $map.ContainsKey([string]$record.closed_by_record_id)) {
        if ([string]$record.record_id -notin @($map[[string]$record.closed_by_record_id].closes_record_ids)) { Fail 'JSONL closure reciprocity' $record.record_id }
    }
    foreach ($closed in @($record.closes_record_ids)) {
        if ($map.ContainsKey([string]$closed) -and [string]$map[[string]$closed].closed_by_record_id -ne [string]$record.record_id) { Fail 'JSONL closure reciprocity' "$($record.record_id) closes=$closed" }
    }
    $target = $record.target_locator
    if ($null -ne $target) {
        if ([long]$target.bytes -le 0 -or [string]$target.sha256 -cnotmatch '^[0-9A-F]{64}$') { Fail 'JSONL target identity' $record.record_id }
        if (-not [string]::IsNullOrWhiteSpace([string]$target.relative_path)) {
            $targetPath = [IO.Path]::GetFullPath((Join-Path $Root ([string]$target.relative_path).Replace('/','\')))
            if (-not $targetPath.StartsWith($Root + '\',[StringComparison]::OrdinalIgnoreCase)) { Fail 'JSONL target path' "$($record.record_id) escapes root" }
            elseif (-not (Test-Path -LiteralPath $targetPath -PathType Leaf)) { Fail 'JSONL target path' "$($record.record_id) missing=$($target.relative_path)" }
            elseif ((Get-Item $targetPath).Length -ne [long]$target.bytes -or (Sha $targetPath) -cne [string]$target.sha256) { Fail 'JSONL target integrity' "$($record.record_id) path=$($target.relative_path)" }
        }
    }
}
$status = @{}
foreach ($g in ($records | Group-Object status)) { $status[$g.Name] = $g.Count }
if ($status['closed_corrected'] -eq 122 -and $status['rejected'] -eq 18 -and $status['superseded'] -eq 5) { Pass 'JSONL terminal statuses' 'closed_corrected=122 rejected=18 superseded=5' }
else { Fail 'JSONL terminal statuses' ($status | ConvertTo-Json -Compress) }

if ($null -ne $schema -and $schema.schema_id -eq 'sga1_public_machine_ledgers.v5' -and
    @($schema.csv_ledgers.PSObject.Properties).Count -eq 23 -and @($schema.graph_jsonl).Count -eq 5 -and
    @($schema.difficulty_jsonl).Count -eq 5 -and [long]$schema.continuation_cursor.line -eq 1654 -and $schema.continuation_cursor.excluded -eq $true) {
    Pass 'public schema' 'csv=23 jsonl=10 cursor=1654'
}
else { Fail 'public schema' 'unexpected v5 declaration or cursor' }
$machineReceipt = Join-Path $ledgerDir 'PUBLIC_MACHINE_VALIDATION_I_8.txt'
if ((Test-Path $machineReceipt) -and (Read-StrictUtf8 $machineReceipt).Contains('csv_rows=400') -and (Read-StrictUtf8 $machineReceipt).Contains('jsonl_records=145') -and (Read-StrictUtf8 $machineReceipt).Contains('failures=0')) { Pass 'public machine receipt' "sha256=$(Sha $machineReceipt)" }
else { Fail 'public machine receipt' 'missing or incomplete' }
$artifactReceipt = Join-Path $ledgerDir 'PUBLIC_CSV_ARTIFACT_VALIDATION_I_8.txt'
if ((Test-Path $artifactReceipt) -and (Read-StrictUtf8 $artifactReceipt).Contains("PASS`tARTIFACT_TOOL_TOTAL`tfiles=23`tdata_rows=400`tfailures=0")) { Pass 'CSV artifact-tool receipt' "sha256=$(Sha $artifactReceipt)" }
else { Fail 'CSV artifact-tool receipt' 'missing or incomplete' }

$shaPath = Join-Path $Root 'SHA256SUMS.csv'
try {
    $rows = @(Import-Csv -LiteralPath $shaPath)
    $expected = @($allFiles | Where-Object { (Rel $_.FullName) -ne 'SHA256SUMS.csv' } | ForEach-Object { Rel $_.FullName } | Sort-Object)
    $listed = @($rows.relative_path | Sort-Object)
    if ($rows.Count -eq ($expectedFileCount - 1) -and ($expected -join "`n") -ceq ($listed -join "`n")) { Pass 'checksum exact set' "rows=$($rows.Count)" }
    else { Fail 'checksum exact set' "rows=$($rows.Count)" }
    foreach ($row in $rows) {
        $path = Join-Path $Root $row.relative_path.Replace('/','\')
        if (-not (Test-Path $path) -or (Get-Item $path).Length -ne [long]$row.bytes -or (Sha $path) -cne $row.sha256) { Fail 'checksum row' $row.relative_path }
    }
}
catch { Fail 'checksum manifest' $_.Exception.Message }
$zenodoPath = Join-Path $Root 'ZENODO_PAYLOAD_MANIFEST.csv'
try {
    $rows = @(Import-Csv -LiteralPath $zenodoPath)
    $expected = @($allFiles | Where-Object { (Rel $_.FullName) -notin @('SHA256SUMS.csv','ZENODO_PAYLOAD_MANIFEST.csv') } | ForEach-Object { Rel $_.FullName } | Sort-Object)
    $listed = @($rows.relative_path | Sort-Object)
    if ($rows.Count -eq ($expectedFileCount - 2) -and ($expected -join "`n") -ceq ($listed -join "`n")) { Pass 'Zenodo manifest exact set' "rows=$($rows.Count)" }
    else { Fail 'Zenodo manifest exact set' "rows=$($rows.Count)" }
    foreach ($row in $rows) {
        $path = Join-Path $Root $row.relative_path.Replace('/','\')
        if (-not (Test-Path $path) -or (Get-Item $path).Length -ne [long]$row.bytes -or (Sha $path) -cne $row.sha256) { Fail 'Zenodo manifest row' $row.relative_path }
        if ($row.publication_action -cne 'PUBLISH_ONLY_AFTER_ARCHIVE_RIGHTS_SCOPE_AND_LIVE_STATE_REVIEW') { Fail 'Zenodo publication action' $row.relative_path }
    }
}
catch { Fail 'Zenodo manifest' $_.Exception.Message }
$livePath = Join-Path $Root 'ZENODO_LIVE_CONTROL.json'
try {
    $live = (Read-StrictUtf8 $livePath) | ConvertFrom-Json -Depth 20
    if ($live.concept_doi -eq '10.5281/zenodo.20410947' -and $live.archive_owner_must_recheck_before_upload -eq $true -and $live.no_upload_or_deposit_created_by_this_checkpoint_task -eq $true) { Pass 'Zenodo control' "last_observed=$($live.last_observed_version_doi)" }
    else { Fail 'Zenodo control' 'archive recheck/no-upload control absent' }
}
catch { Fail 'Zenodo control' $_.Exception.Message }

if ($failures.Count -eq 0) {
    Write-Output 'failures=0'
    Write-Output 'PUBLIC_PAYLOAD_VERIFY=PASS'
    exit 0
}
Write-Output "failures=$($failures.Count)"
foreach ($failure in $failures) { Write-Output "failure=$failure" }
Write-Output 'PUBLIC_PAYLOAD_VERIFY=FAIL'
exit 1
