[CmdletBinding()]
param()

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$indexDir = $PSScriptRoot
$schemaPath = Join-Path $indexDir 'PRODUCER_STRUCTURAL_INDEX.schema.json'
$builderPath = Join-Path $indexDir 'build_structural_index.ps1'
$jsonlPath = Join-Path $indexDir 'PRODUCER_STRUCTURAL_INDEX.jsonl'
$csvPath = Join-Path $indexDir 'PRODUCER_STRUCTURAL_INDEX.csv'
$notesPath = Join-Path $indexDir 'STRUCTURAL_BUILD_NOTES.md'
$reportPath = Join-Path $indexDir 'PRODUCER_STRUCTURAL_INDEX_VALIDATION_REPORT.json'
$utf8NoBom = [System.Text.UTF8Encoding]::new($false)
$errors = [System.Collections.Generic.List[string]]::new()

$sourcePath = '${PUBLIC_INTERLANGUAGE_ROOT}\03_projects\noether\07_german_canon_control\candidates\NOETH-DE-ED-0001\Noether_German_NOETH-DE-ED-0001.tex'
$sourceHashExpected = 'D1F06B311F6CBD991DD247D745DD9A72DDE326A20396DF43CFE0C8EDB1593CDB'
$paperIntervalHashExpected = 'E600FD2A19ACA22F43D54FB65C61B79172B12FE5AB09446A2C9C9B8CACD26E7D'
$pointerIdExpected = 'NOETH-DE-AUTH-v003-20260804'
$pointerHashExpected = '932FEDC1735A41A9CF71D15A6C662A468A4CAD016AE8B3DECDF9A71E8BA7F197'
$root = (Resolve-Path -LiteralPath (Join-Path $indexDir '..\..')).Path
$targets = [ordered]@{
    U01 = Join-Path $root 'targets\Noether_P03_Korean_U01_UNCHECKED.tex'
    U02 = Join-Path $root 'targets\Noether_P03_Korean_U02_UNCHECKED.tex'
    U03 = Join-Path $root 'targets\Noether_P03_Korean_U03_UNCHECKED.tex'
}
$targetHashExpected = [ordered]@{
    U01 = '057D6EAECAAB02C4D19C6908276C11E32953748726BD36B628712AB5C5E78ECB'
    U02 = 'A2A9F68B55C15EEFEAE178B4F24CB5D56222E563F6B5A126F46D1AA75BEA38B1'
    U03 = '7942126177C707C89F67444BE020F90F2139C0C5036A153297C0A7F83119F4B4'
}
$unitExpected = [ordered]@{
    U01 = [ordered]@{ record_id = 'NOE-P03-KO-U01-UNIT-001'; source_start = 3573; source_end = 3584; source_bytes = 2156; source_sha256 = 'DF50EAD7065F663901F51ADFCA37A138921063362CA449665D37B855921B496C'; target_start = 14; target_end = 25 }
    U02 = [ordered]@{ record_id = 'NOE-P03-KO-U02-UNIT-001'; source_start = 3586; source_end = 3594; source_bytes = 2975; source_sha256 = 'A7B7CA981F7B8D6B32171BF0709E27440A25B2754642BD095304E54A5A25D5C6'; target_start = 12; target_end = 20 }
    U03 = [ordered]@{ record_id = 'NOE-P03-KO-U03-UNIT-001'; source_start = 3596; source_end = 3608; source_bytes = 3144; source_sha256 = '0D110465AEE20E18EE1427577D33D435FCF97D5CA99BEF3878EF52DC341F01A5'; target_start = 14; target_end = 26 }
}
$structureTypes = @(
    'work','unit','title','author','publication_note','section_heading','subsection_heading','division_heading',
    'paragraph','closed_prose','theorem','proposition','lemma','corollary','definition','remark','example',
    'proof','proof_step','display','formula','note','footnote','bibliography_item','cross_reference','other'
)
$expectedTypeCounts = [ordered]@{
    work = 1; unit = 3; title = 1; author = 1; publication_note = 1
    section_heading = 0; subsection_heading = 0; division_heading = 0
    paragraph = 8; closed_prose = 35; theorem = 8; proposition = 0; lemma = 0; corollary = 0
    definition = 4; remark = 0; example = 0; proof = 3; proof_step = 0; display = 2; formula = 58
    note = 0; footnote = 6; bibliography_item = 6; cross_reference = 1; other = 10
}
$allowedBasis = @('source_fact','computation','producer_editorial_inference')
$allowedRelations = @('contains','embedded_in','continues','cross_reference','cites','proves','statement_of','equation_for','formula_in','note_for','bibliography_for')
$topProperties = @(
    'schema_version','record_id','work_id','unit_id','structure_type','label','parent_id','order','record_basis',
    'source_language','target_language','authority_pointer','authority_state','source_locator','target_locators','relations',
    'completion_state','review_state','publication_state','continuation_cursor','record_sha256'
)
$sourceLocatorProperties = @('path','line_start','line_end','file_sha256','slice_sha256_lf','fragment_kind','fragment_occurrence','fragment_text','fragment_sha256_utf8')
$targetLocatorProperties = @('unit_id','path','line_start','line_end','file_sha256','slice_sha256_lf','fragment_kind','fragment_occurrence','fragment_text','fragment_sha256_utf8')
$csvHeadersExpected = @(
    'schema_version','record_id','work_id','unit_id','structure_type','label','parent_id','order',
    'record_basis_json','source_language','target_language','authority_pointer_id','authority_pointer_sha256','authority_state',
    'source_path','source_line_start','source_line_end','source_file_sha256','source_slice_sha256_lf',
    'source_fragment_kind','source_fragment_occurrence','source_fragment_text','source_fragment_sha256_utf8',
    'target_locator_count','target_paths','target_file_sha256_values','target_locators_json','relations_json',
    'completion_state','review_state','publication_state','continuation_cursor','record_sha256'
)

function Add-Error([string]$Message) { [void]$errors.Add($Message) }
function Get-FileSha256([string]$Path) { return (Get-FileHash -LiteralPath $Path -Algorithm SHA256).Hash }
function Get-Utf8Sha256([AllowNull()][string]$Text) {
    if ($null -eq $Text) { return $null }
    $sha = [System.Security.Cryptography.SHA256]::Create()
    try { return ([System.BitConverter]::ToString($sha.ComputeHash($utf8NoBom.GetBytes($Text)))).Replace('-', '') }
    finally { $sha.Dispose() }
}
$lineCache = @{}
function Get-PathLines([string]$Path) {
    if (-not $lineCache.ContainsKey($Path)) { $lineCache[$Path] = [System.IO.File]::ReadAllLines($Path, $utf8NoBom) }
    return $lineCache[$Path]
}
function Get-LfSliceInfo([string]$Path, [int]$Start, [int]$End) {
    $lines = @(Get-PathLines $Path)
    if ($Start -lt 1 -or $End -lt $Start -or $End -gt $lines.Count) { throw "invalid slice $Start-$End for $Path" }
    $text = [string]::Join("`n", $lines[($Start - 1)..($End - 1)]) + "`n"
    return [ordered]@{ sha256 = Get-Utf8Sha256 $text; bytes = $utf8NoBom.GetByteCount($text) }
}
function Get-InlineMathFragments([string]$Text) {
    $items = [System.Collections.Generic.List[string]]::new()
    $pattern = '\$[^$\r\n]*\$|\\\((?:(?!\\\)).)*\\\)'
    foreach ($match in [System.Text.RegularExpressions.Regex]::Matches($Text, $pattern)) { [void]$items.Add($match.Value) }
    return $items.ToArray()
}
function Compare-ExactProperties([object]$Object, [string[]]$Expected, [string]$Context) {
    $actual = @($Object.PSObject.Properties.Name)
    foreach ($name in $Expected) { if ($name -notin $actual) { Add-Error "$Context missing property $name" } }
    foreach ($name in $actual) { if ($name -notin $Expected) { Add-Error "$Context unexpected property $name" } }
}
function Validate-Locator([object]$Locator, [string]$Context, [bool]$IsTarget) {
    Compare-ExactProperties $Locator $(if ($IsTarget) { $targetLocatorProperties } else { $sourceLocatorProperties }) $Context
    if (-not (Test-Path -LiteralPath $Locator.path -PathType Leaf)) { Add-Error "$Context path missing"; return }
    if ([int]$Locator.line_start -gt [int]$Locator.line_end) { Add-Error "$Context inverted line range"; return }
    $actualFileHash = Get-FileSha256 $Locator.path
    if ($Locator.file_sha256 -ne $actualFileHash) { Add-Error "$Context file hash mismatch" }
    try { $slice = Get-LfSliceInfo $Locator.path ([int]$Locator.line_start) ([int]$Locator.line_end) }
    catch { Add-Error "$Context slice error: $($_.Exception.Message)"; return }
    if ($Locator.slice_sha256_lf -ne $slice.sha256) { Add-Error "$Context line-slice hash mismatch" }
    if ($null -eq $Locator.fragment_text) {
        if ($Locator.fragment_kind -ne 'line_slice') { Add-Error "$Context null fragment must use line_slice" }
        if ($null -ne $Locator.fragment_occurrence -or $null -ne $Locator.fragment_sha256_utf8) { Add-Error "$Context null fragment has occurrence/hash" }
    }
    else {
        if ($Locator.fragment_kind -ne 'inline_math') { Add-Error "$Context non-null fragment must use inline_math" }
        if ($null -eq $Locator.fragment_occurrence -or [int]$Locator.fragment_occurrence -lt 1) { Add-Error "$Context invalid fragment occurrence" }
        if ($Locator.fragment_sha256_utf8 -ne (Get-Utf8Sha256 ([string]$Locator.fragment_text))) { Add-Error "$Context fragment hash mismatch" }
        if ([int]$Locator.line_start -ne [int]$Locator.line_end) { Add-Error "$Context inline fragment spans multiple lines" }
        else {
            $line = (Get-PathLines $Locator.path)[[int]$Locator.line_start - 1]
            $fragments = @(Get-InlineMathFragments $line)
            $position = [int]$Locator.fragment_occurrence - 1
            if ($position -lt 0 -or $position -ge $fragments.Count) { Add-Error "$Context fragment occurrence is outside extracted list" }
            elseif ([string]$fragments[$position] -ne [string]$Locator.fragment_text) { Add-Error "$Context fragment text does not match extracted occurrence" }
        }
    }
}

foreach ($requiredFile in @($schemaPath,$builderPath,$jsonlPath,$csvPath,$notesPath)) {
    if (-not (Test-Path -LiteralPath $requiredFile -PathType Leaf)) { Add-Error "missing required file: $requiredFile" }
}

# Determinism check: the already generated pair is hashed, the builder is rerun once, and identities must remain byte-identical.
$determinismRebuildVerified = $false
$jsonBefore = if (Test-Path -LiteralPath $jsonlPath) { Get-FileSha256 $jsonlPath } else { $null }
$csvBefore = if (Test-Path -LiteralPath $csvPath) { Get-FileSha256 $csvPath } else { $null }
try { & $builderPath | Out-Null }
catch { Add-Error "deterministic rebuild failed: $($_.Exception.Message)" }
$jsonAfter = if (Test-Path -LiteralPath $jsonlPath) { Get-FileSha256 $jsonlPath } else { $null }
$csvAfter = if (Test-Path -LiteralPath $csvPath) { Get-FileSha256 $csvPath } else { $null }
if ($null -ne $jsonBefore -and $jsonBefore -eq $jsonAfter -and $null -ne $csvBefore -and $csvBefore -eq $csvAfter) { $determinismRebuildVerified = $true }
else { Add-Error 'builder rerun changed JSONL or CSV bytes' }

try { $schema = Get-Content -LiteralPath $schemaPath -Raw -Encoding utf8 | ConvertFrom-Json -Depth 100 }
catch { Add-Error "schema is not valid JSON: $($_.Exception.Message)"; $schema = $null }
if ($null -ne $schema -and $schema.title -ne 'Noether Paper 3 Korean producer structural record') { Add-Error 'unexpected schema title' }

$jsonText = [System.IO.File]::ReadAllText($jsonlPath, $utf8NoBom)
if ($jsonText.StartsWith([char]0xFEFF)) { Add-Error 'JSONL contains UTF-8 BOM' }
if ($jsonText.Contains("`r")) { Add-Error 'JSONL contains CR instead of deterministic LF line endings' }
if (-not $jsonText.EndsWith("`n")) { Add-Error 'JSONL lacks terminal LF' }
$jsonLines = @($jsonText.Split("`n", [System.StringSplitOptions]::RemoveEmptyEntries))
$records = [System.Collections.Generic.List[object]]::new()
$rawLineById = @{}
foreach ($line in $jsonLines) {
    try { $record = $line | ConvertFrom-Json -Depth 100 }
    catch { Add-Error "invalid JSONL record: $($_.Exception.Message)"; continue }
    [void]$records.Add($record)
    if ($rawLineById.ContainsKey($record.record_id)) { Add-Error "duplicate record_id $($record.record_id)" }
    else { $rawLineById[$record.record_id] = $line }
}
if ($records.Count -ne 148) { Add-Error "record count $($records.Count), expected 148" }

$ids = @($records | ForEach-Object { $_.record_id })
$idSet = [System.Collections.Generic.HashSet[string]]::new([string[]]$ids)
$typeCounts = [ordered]@{}
foreach ($type in $structureTypes) { $typeCounts[$type] = 0 }
foreach ($record in $records) {
    $context = $record.record_id
    Compare-ExactProperties $record $topProperties $context
    if ($record.schema_version -ne '1.2') { Add-Error "$context schema version mismatch" }
    if ($record.record_id -notmatch '^NOE-P03-KO-[A-Z0-9-]+$') { Add-Error "$context invalid ID" }
    if ($record.work_id -ne 'NOE-P03') { Add-Error "$context work ID mismatch" }
    if ($record.unit_id -notin @('ALL','U01','U02','U03')) { Add-Error "$context unit ID mismatch" }
    if ($record.structure_type -notin $structureTypes) { Add-Error "$context structure type not in schema" }
    else { $typeCounts[$record.structure_type]++ }
    if ([string]::IsNullOrWhiteSpace($record.label)) { Add-Error "$context blank label" }
    if ([int]$record.order -lt 1) { Add-Error "$context invalid order" }
    if (@($record.record_basis).Count -lt 1) { Add-Error "$context empty record basis" }
    foreach ($basis in @($record.record_basis)) { if ($basis -notin $allowedBasis) { Add-Error "$context invalid record basis $basis" } }
    if (@(@($record.record_basis) | Sort-Object -Unique).Count -ne @($record.record_basis).Count) { Add-Error "$context duplicate record basis" }
    if ($record.source_language -ne 'de' -or $record.target_language -ne 'ko-KR') { Add-Error "$context language mismatch" }
    if ($record.authority_pointer.pointer_id -ne $pointerIdExpected -or $record.authority_pointer.pointer_sha256 -ne $pointerHashExpected) { Add-Error "$context pointer mismatch" }
    if ($record.authority_state -ne 'current_v003_translation_input_unchecked') { Add-Error "$context authority state mismatch" }
    if ($record.completion_state -ne 'producer_draft_text_covered' -or $record.review_state -ne 'unchecked' -or $record.publication_state -ne 'private_not_for_publication') { Add-Error "$context state violation" }
    if ([string]::IsNullOrWhiteSpace($record.continuation_cursor)) { Add-Error "$context blank continuation cursor" }
    if ($record.source_locator.path -ne $sourcePath) { Add-Error "$context unexpected source path" }
    if ($record.source_locator.file_sha256 -ne $sourceHashExpected) { Add-Error "$context unexpected source file identity" }
    Validate-Locator $record.source_locator "$context source" $false
    if (@($record.target_locators).Count -lt 1) { Add-Error "$context has no target locators" }
    foreach ($locator in @($record.target_locators)) {
        if ($locator.unit_id -notin @('U01','U02','U03')) { Add-Error "$context target unit invalid" }
        elseif ($locator.path -ne $targets[$locator.unit_id]) { Add-Error "$context target path mismatch for $($locator.unit_id)" }
        elseif ($locator.file_sha256 -ne $targetHashExpected[$locator.unit_id]) { Add-Error "$context target file identity mismatch for $($locator.unit_id)" }
        Validate-Locator $locator "$context target $($locator.unit_id)" $true
    }
    if ($null -ne $record.parent_id -and -not $idSet.Contains([string]$record.parent_id)) { Add-Error "$context missing parent $($record.parent_id)" }
    foreach ($relation in @($record.relations)) {
        if ($relation.relation -notin $allowedRelations) { Add-Error "$context invalid relation $($relation.relation)" }
        if (-not $idSet.Contains([string]$relation.target_id)) { Add-Error "$context missing relation target $($relation.target_id)" }
    }
    $rawLine = $rawLineById[$record.record_id]
    $canonicalRaw = $rawLine -replace ',"record_sha256":"[A-F0-9]{64}"\}$', '}'
    if ($canonicalRaw -eq $rawLine) { Add-Error "$context record hash field is not final/canonical" }
    elseif ($record.record_sha256 -ne (Get-Utf8Sha256 $canonicalRaw)) { Add-Error "$context record hash mismatch" }
}

foreach ($entry in $expectedTypeCounts.GetEnumerator()) {
    if ($typeCounts[$entry.Key] -ne $entry.Value) { Add-Error "type count $($entry.Key)=$($typeCounts[$entry.Key]), expected $($entry.Value)" }
}

$workRecords = @($records | Where-Object structure_type -eq 'work')
if ($workRecords.Count -ne 1 -or $workRecords[0].record_id -ne 'NOE-P03-KO-WORK-001') { Add-Error 'work-root identity/count mismatch' }
elseif ($null -ne $workRecords[0].parent_id) { Add-Error 'work root must have null parent' }
foreach ($record in @($records | Where-Object structure_type -ne 'work')) { if ($null -eq $record.parent_id) { Add-Error "$($record.record_id) has null parent" } }

foreach ($siblingGroup in @($records | Where-Object { $null -ne $_.parent_id } | Group-Object parent_id)) {
    foreach ($orderGroup in @($siblingGroup.Group | Group-Object order)) {
        if ($orderGroup.Count -gt 1) { Add-Error "duplicate sibling order $($orderGroup.Name) under $($siblingGroup.Name)" }
    }
}

if ($sourceHashExpected -ne (Get-FileSha256 $sourcePath)) { Add-Error 'authority whole-file hash mismatch' }
$paperSlice = Get-LfSliceInfo $sourcePath 3573 3608
if ($paperSlice.sha256 -ne $paperIntervalHashExpected -or $paperSlice.bytes -ne 8277) { Add-Error 'Paper 3 interval identity mismatch' }
foreach ($unit in $unitExpected.Keys) {
    $expected = $unitExpected[$unit]
    $unitRecords = @($records | Where-Object record_id -eq $expected.record_id)
    if ($unitRecords.Count -ne 1) { Add-Error "$unit unit-record count mismatch"; continue }
    $record = $unitRecords[0]
    if ($record.source_locator.line_start -ne $expected.source_start -or $record.source_locator.line_end -ne $expected.source_end -or $record.source_locator.slice_sha256_lf -ne $expected.source_sha256) { Add-Error "$unit source-unit locator mismatch" }
    $unitSlice = Get-LfSliceInfo $sourcePath $expected.source_start $expected.source_end
    if ($unitSlice.sha256 -ne $expected.source_sha256 -or $unitSlice.bytes -ne $expected.source_bytes) { Add-Error "$unit source-unit identity mismatch" }
    if (@($record.target_locators).Count -ne 1 -or $record.target_locators[0].line_start -ne $expected.target_start -or $record.target_locators[0].line_end -ne $expected.target_end) { Add-Error "$unit target-unit locator mismatch" }
}

$formulaRecords = @($records | Where-Object structure_type -eq 'formula')
$sourceInlineFormulaCount = @($formulaRecords | Where-Object { $null -ne $_.source_locator.fragment_text }).Count
$targetInlineFormulaCount = @($formulaRecords | Where-Object { $null -ne $_.target_locators[0].fragment_text }).Count
$lineFormulaCount = @($formulaRecords | Where-Object { $null -eq $_.source_locator.fragment_text -and $null -eq $_.target_locators[0].fragment_text }).Count
$targetOnlyFormulaRecords = @($formulaRecords | Where-Object { $null -eq $_.source_locator.fragment_text -and $null -ne $_.target_locators[0].fragment_text })
$sourceOnlyFormulaRecords = @($formulaRecords | Where-Object { $null -ne $_.source_locator.fragment_text -and $null -eq $_.target_locators[0].fragment_text })
if ($sourceInlineFormulaCount -ne 52) { Add-Error "source inline-formula count $sourceInlineFormulaCount, expected 52" }
if ($targetInlineFormulaCount -ne 53) { Add-Error "target inline-formula count $targetInlineFormulaCount, expected 53" }
if ($lineFormulaCount -ne 5) { Add-Error "display line-formula count $lineFormulaCount, expected 5" }
if ($targetOnlyFormulaRecords.Count -ne 1 -or $targetOnlyFormulaRecords[0].record_id -ne 'NOE-P03-KO-U02-FORMULA-028') { Add-Error 'target-only formula occurrence identity mismatch' }
if ($sourceOnlyFormulaRecords.Count -ne 0) { Add-Error 'unexpected source-only formula occurrence' }

$csvText = [System.IO.File]::ReadAllText($csvPath, $utf8NoBom)
if ($csvText.StartsWith([char]0xFEFF)) { Add-Error 'CSV contains UTF-8 BOM' }
if ($csvText.Contains("`r")) { Add-Error 'CSV contains CR instead of deterministic LF line endings' }
if (-not $csvText.EndsWith("`n")) { Add-Error 'CSV lacks terminal LF' }
if ($csvText -match '#REF!|#DIV/0!|#VALUE!|#NAME\?|#N/A') { Add-Error 'CSV contains spreadsheet formula-error token' }
$csvRows = @(Import-Csv -LiteralPath $csvPath -Encoding utf8)
if ($csvRows.Count -ne $records.Count) { Add-Error "CSV row count $($csvRows.Count), expected $($records.Count)" }
if ($csvRows.Count -gt 0) {
    $actualHeaders = @($csvRows[0].PSObject.Properties.Name)
    if ([string]::Join('|', $actualHeaders) -ne [string]::Join('|', $csvHeadersExpected)) { Add-Error 'CSV header mismatch' }
}
$csvIds = @($csvRows | ForEach-Object record_id)
if (($csvIds | Sort-Object -Unique).Count -ne $csvIds.Count) { Add-Error 'CSV duplicate record IDs' }
foreach ($row in $csvRows) {
    if (-not $rawLineById.ContainsKey($row.record_id)) { Add-Error "CSV record not in JSONL: $($row.record_id)"; continue }
    $jsonRecord = $records | Where-Object record_id -eq $row.record_id | Select-Object -First 1
    if ($row.record_sha256 -ne $jsonRecord.record_sha256) { Add-Error "CSV record hash mismatch for $($row.record_id)" }
    try { $targetProjection = $row.target_locators_json | ConvertFrom-Json -Depth 100 }
    catch { Add-Error "CSV target_locators_json invalid for $($row.record_id)"; continue }
    if (@($targetProjection).Count -ne [int]$row.target_locator_count) { Add-Error "CSV target locator count mismatch for $($row.record_id)" }
    try { $null = $row.relations_json | ConvertFrom-Json -Depth 100 }
    catch { Add-Error "CSV relations_json invalid for $($row.record_id)" }
    try { $null = $row.record_basis_json | ConvertFrom-Json -Depth 100 }
    catch { Add-Error "CSV record_basis_json invalid for $($row.record_id)" }
}

$latestRecordId = if ($records.Count -gt 0) { $records[$records.Count - 1].record_id } else { $null }
if ($latestRecordId -ne 'NOE-P03-KO-U03-FORMULA-014') { Add-Error "latest record ID mismatch: $latestRecordId" }

$report = [ordered]@{
    schema = 'PRODUCER_STRUCTURAL_INDEX.schema.json'
    schema_sha256 = Get-FileSha256 $schemaPath
    builder = 'build_structural_index.ps1'
    builder_sha256 = Get-FileSha256 $builderPath
    validator = 'validate_structural_index.ps1'
    evidence_date = '2026-08-04'
    status = if ($errors.Count -eq 0) { 'pass' } else { 'fail' }
    deterministic_rebuild_verified = $determinismRebuildVerified
    record_count = $records.Count
    unique_record_count = ($ids | Sort-Object -Unique).Count
    latest_record_id = $latestRecordId
    type_counts_including_zero = $typeCounts
    authority = [ordered]@{
        pointer_id = $pointerIdExpected
        pointer_sha256 = $pointerHashExpected
        path = $sourcePath
        file_bytes = (Get-Item -LiteralPath $sourcePath).Length
        file_sha256 = Get-FileSha256 $sourcePath
        paper_interval_lines = '3573--3608'
        paper_interval_lf_utf8_bytes = $paperSlice.bytes
        paper_interval_sha256_lf = $paperSlice.sha256
    }
    source_unit_hashes_verified = [ordered]@{
        U01 = $unitExpected.U01.source_sha256
        U02 = $unitExpected.U02.source_sha256
        U03 = $unitExpected.U03.source_sha256
    }
    target_file_hashes_verified = [ordered]@{
        U01 = Get-FileSha256 $targets.U01
        U02 = Get-FileSha256 $targets.U02
        U03 = Get-FileSha256 $targets.U03
    }
    formula_inventory = [ordered]@{
        formula_record_count = $formulaRecords.Count
        source_inline_math_occurrences = $sourceInlineFormulaCount
        target_inline_math_occurrences = $targetInlineFormulaCount
        paired_display_line_formulas = $lineFormulaCount
        target_only_inline_occurrence_record_ids = @($targetOnlyFormulaRecords | ForEach-Object record_id)
        source_only_inline_occurrence_record_ids = @($sourceOnlyFormulaRecords | ForEach-Object record_id)
        pairing_basis = 'same-line occurrence order only; producer structural inference; unchecked'
    }
    jsonl_bytes = (Get-Item -LiteralPath $jsonlPath).Length
    jsonl_sha256 = Get-FileSha256 $jsonlPath
    csv_bytes = (Get-Item -LiteralPath $csvPath).Length
    csv_sha256 = Get-FileSha256 $csvPath
    build_notes_sha256 = Get-FileSha256 $notesPath
    observed_failures = @(
        [ordered]@{
            failure_id = 'CJK-KO-P03-STRUCT-FAIL-001'
            stage = 'spreadsheet runtime dependency discovery'
            state = 'resolved_by_exact_loader_path_from_root_session'
            artifact_effect = 'none'
            note_path = $notesPath
        }
        [ordered]@{
            failure_id = 'CJK-KO-P03-STRUCT-FAIL-002'
            stage = 'first structural validator run'
            state = 'resolved_by_lower_and_upper_fragment_bounds_guard'
            artifact_effect = 'validator_and_notes_only'
            note_path = $notesPath
        }
        [ordered]@{
            failure_id = 'CJK-KO-P03-STRUCT-FAIL-003'
            stage = 'second structural validator run'
            state = 'resolved_by_array_wrapping_unique_pipeline_result'
            artifact_effect = 'validator_and_notes_only'
            note_path = $notesPath
        }
        [ordered]@{
            failure_id = 'CJK-KO-P03-STRUCT-FAIL-004'
            stage = 'first completed machine FAIL report'
            state = 'resolved_by_preserving_null_optional_values'
            artifact_effect = 'builder_jsonl_csv_validator_notes'
            note_path = $notesPath
        }
    )
    errors = @($errors)
    continuation_cursor = 'Paper 3 interval exhausted after whole-authority line 3608; lines 3609--3610 excluded; await independent Korean checker'
    scope_note = 'Mechanical producer structure metadata only. No source, Korean, formula, completeness, compile, render, checker, certification, packaging, or publication validation.'
}
$reportJson = ($report | ConvertTo-Json -Depth 30) -replace "`r`n", "`n"
[System.IO.File]::WriteAllText($reportPath, ($reportJson.TrimEnd("`n") + "`n"), $utf8NoBom)
Write-Output ($report | ConvertTo-Json -Compress -Depth 30)
if ($errors.Count -gt 0) { exit 1 }
