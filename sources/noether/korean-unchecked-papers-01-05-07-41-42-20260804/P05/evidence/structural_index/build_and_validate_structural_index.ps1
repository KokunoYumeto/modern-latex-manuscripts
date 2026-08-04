$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

$indexDir = $PSScriptRoot
$root = (Resolve-Path -LiteralPath (Join-Path $indexDir '..\..')).Path
$sourcePath = '${PUBLIC_INTERLANGUAGE_ROOT}\03_projects\noether\07_german_canon_control\candidates\NOETH-DE-ED-0001\Noether_German_NOETH-DE-ED-0001.tex'
$expectedSourceHash = 'D1F06B311F6CBD991DD247D745DD9A72DDE326A20396DF43CFE0C8EDB1593CDB'
$expectedBodyHash = '99BD68A8DBD9861EFF0CDBE26CB365C3306EDF15BD93A6C4C10B9F25419D5CAE'
$pointerId = 'NOETH-DE-AUTH-v003-20260804'
$pointerHash = '932FEDC1735A41A9CF71D15A6C662A468A4CAD016AE8B3DECDF9A71E8BA7F197'
$utf8NoBom = [System.Text.UTF8Encoding]::new($false)

$unitSourceLines = [ordered]@{
    U01 = @(4535, 4545)
    U02 = @(4547, 4557)
    U03 = @(4559, 4563)
    U04 = @(4565, 4572)
}
$expectedUnitSourceHash = [ordered]@{
    U01 = '8AB438E098574B638EB932F7E002A8D894A97DE4872EBEEE7B96EEC52A1C072C'
    U02 = '3B6528941F0DC23909DEDAE5F9C4AA0598CADE04916DA12094F188BE4983EAB2'
    U03 = '778D2BAE411E136A3760673A839EF0DB9BA79C83F0534F103CF851F5F7E4A698'
    U04 = 'FF5058094D557ECF29D2EA4A37762067EF5936EAD529E70AF5C5FA0E6B063230'
}
$expectedTargetHash = [ordered]@{
    U01 = 'EEB39C3A693410823F66A75BCE7DBB9906F35637BFFF87A55CE4A7B873A6F203'
    U02 = '62D644153874FFE07C839102D5EF222BCED55F693C1BA6E8E9FF318A670F8DEA'
    U03 = '2B7ADD81855DD9D06A1D2D17249F32F5D7BBDB458F7474E0BB7BC3F14A5FFA89'
    U04 = '8A50F7549C23A50A6A824C97763941535D12061EE08E32D2EC1D3F678FE4CA6B'
}
$unitCursor = [ordered]@{
    U01 = 'continue at whole-source line 4547 / Paper-local line 13 / Korean U02'
    U02 = 'continue at whole-source line 4559 / Paper-local line 25 / Korean U03'
    U03 = 'continue at whole-source line 4565 / Paper-local line 31 / Korean U04'
    U04 = 'Paper 5 substantive text exhausted at whole-source line 4572; line 4573 terminal blank; line 4574 clearpage excluded; await independent Korean checker'
}
$targets = [ordered]@{}
foreach ($number in 1..4) {
    $unit = 'U{0:D2}' -f $number
    $targets[$unit] = Join-Path $root ('targets\Noether_P05_Korean_{0}_UNCHECKED.tex' -f $unit)
}

function Get-FileSha256([string]$Path) {
    return (Get-FileHash -LiteralPath $Path -Algorithm SHA256).Hash
}

function Get-TextSha256([string]$Text) {
    $sha = [System.Security.Cryptography.SHA256]::Create()
    try {
        return ([System.BitConverter]::ToString($sha.ComputeHash($utf8NoBom.GetBytes($Text)))).Replace('-', '')
    }
    finally {
        $sha.Dispose()
    }
}

function Get-LfSliceSha256([string]$Path, [int]$Start, [int]$End) {
    $lines = [System.IO.File]::ReadAllLines($Path, $utf8NoBom)
    if ($Start -lt 1 -or $End -lt $Start -or $End -gt $lines.Length) {
        throw "Invalid line slice $Start-$End for $Path with $($lines.Length) lines"
    }
    $slice = [string]::Join([char]10, $lines[($Start - 1)..($End - 1)]) + [char]10
    return Get-TextSha256 $slice
}

function Convert-TargetSpec([string]$Spec) {
    $parts = $Spec.Split(':')
    if ($parts.Count -ne 3) {
        throw "Invalid target specification: $Spec"
    }
    return [pscustomobject]@{ unit = $parts[0]; line_start = [int]$parts[1]; line_end = [int]$parts[2] }
}

function Convert-RelationSpec([string]$Spec) {
    $separator = $Spec.IndexOf(':')
    if ($separator -lt 1) {
        throw "Invalid relation specification: $Spec"
    }
    return [pscustomobject]@{ relation = $Spec.Substring(0, $separator); target_id = $Spec.Substring($separator + 1) }
}

# ID | type | label | parent | order | whole start | whole end | targets | relations
$manifestText = @'
NOE-P05-KO-WORK-001|work|Paper 5 substantive translated interval||1|4535|4572|U01:12:22,U02:12:22,U03:12:16,U04:12:19|contains:NOE-P05-KO-U01,contains:NOE-P05-KO-U02,contains:NOE-P05-KO-U03,contains:NOE-P05-KO-U04
NOE-P05-KO-U01|unit|Title, publication data, and opening provenance|NOE-P05-KO-WORK-001|1|4535|4545|U01:12:22|
NOE-P05-KO-U02|unit|Function fields and rational and minimal bases|NOE-P05-KO-WORK-001|2|4547|4557|U02:12:22|continues:NOE-P05-KO-U01
NOE-P05-KO-U03|unit|Minimal-basis examples and integrity-basis definition|NOE-P05-KO-WORK-001|3|4559|4563|U03:12:16|continues:NOE-P05-KO-U02
NOE-P05-KO-U04|unit|Sufficient resultant criterion and open question|NOE-P05-KO-WORK-001|4|4565|4572|U04:12:19|continues:NOE-P05-KO-U03
NOE-P05-KO-U01-TITLE-001|title|Rational function fields|NOE-P05-KO-U01|1|4536|4536|U01:13:13|
NOE-P05-KO-U01-NOTE-001|footnote|Vienna 1913 lecture provenance|NOE-P05-KO-U01-TITLE-001|1|4536|4536|U01:13:13|note_for:NOE-P05-KO-U01-TITLE-001
NOE-P05-KO-U01-AUTHOR-001|author|Emmy Noether byline and Erlangen affiliation|NOE-P05-KO-U01|2|4538|4538|U01:15:15|
NOE-P05-KO-U01-PUBLICATION-001|publication_note|DMV journal citation|NOE-P05-KO-U01|3|4540|4540|U01:17:17|
NOE-P05-KO-U01-PARA-001|paragraph|Fischer conversations and Steinitz antecedent|NOE-P05-KO-U01|4|4545|4545|U01:22:22|
NOE-P05-KO-U01-NOTE-002|footnote|Steinitz Algebraische Theorie der Körper reference|NOE-P05-KO-U01-PARA-001|1|4545|4545|U01:22:22|note_for:NOE-P05-KO-U01-PARA-001
NOE-P05-KO-U01-BIB-001|bibliography_item|Steinitz Algebraische Theorie der Körper 1910|NOE-P05-KO-U01-NOTE-002|1|4545|4545|U01:22:22|bibliography_for:NOE-P05-KO-U01-NOTE-002
NOE-P05-KO-U02-PARA-001|paragraph|Definition and examples of rational function fields|NOE-P05-KO-U02|1|4547|4547|U02:12:12|
NOE-P05-KO-U02-DEFINITION-001|definition|Rational function field|NOE-P05-KO-U02-PARA-001|1|4547|4547|U02:12:12|defines:NOE-P05-KO-U02-PARA-001
NOE-P05-KO-U02-PARA-002|paragraph|First- and second-kind field distinction|NOE-P05-KO-U02|2|4549|4549|U02:14:14|
NOE-P05-KO-U02-PARA-003|paragraph|Three basis concepts|NOE-P05-KO-U02|3|4551|4551|U02:16:16|
NOE-P05-KO-U02-PARA-004|paragraph|Rational-basis definition and existence|NOE-P05-KO-U02|4|4553|4553|U02:18:18|
NOE-P05-KO-U02-DEFINITION-002|definition|Rational basis|NOE-P05-KO-U02-PARA-004|1|4553|4553|U02:18:18|defines:NOE-P05-KO-U02-PARA-004
NOE-P05-KO-U02-BIB-001|bibliography_item|Steinitz reference cited again for one indeterminate|NOE-P05-KO-U02-PARA-004|2|4553|4553|U02:18:18|cross_reference:NOE-P05-KO-U01-BIB-001
NOE-P05-KO-U02-PARA-005|paragraph|Minimal-basis definition and existence range|NOE-P05-KO-U02|5|4555|4555|U02:20:20|
NOE-P05-KO-U02-DEFINITION-003|definition|Minimal basis|NOE-P05-KO-U02-PARA-005|1|4555|4555|U02:20:20|defines:NOE-P05-KO-U02-PARA-005
NOE-P05-KO-U02-NOTE-001|footnote|Lüroth, Castelnuovo, and Enriques references|NOE-P05-KO-U02-PARA-005|2|4555|4555|U02:20:20|note_for:NOE-P05-KO-U02-PARA-005
NOE-P05-KO-U02-BIB-002|bibliography_item|Lüroth rational curves 1875|NOE-P05-KO-U02-NOTE-001|1|4555|4555|U02:20:20|bibliography_for:NOE-P05-KO-U02-NOTE-001
NOE-P05-KO-U02-BIB-003|bibliography_item|Castelnuovo plane involutions 1893|NOE-P05-KO-U02-NOTE-001|2|4555|4555|U02:20:20|bibliography_for:NOE-P05-KO-U02-NOTE-001
NOE-P05-KO-U02-BIB-004|bibliography_item|Enriques nonrational space involution 1912|NOE-P05-KO-U02-NOTE-001|3|4555|4555|U02:20:20|bibliography_for:NOE-P05-KO-U02-NOTE-001
NOE-P05-KO-U02-BIB-005|bibliography_item|Steinitz section 24 cited for the Lüroth function|NOE-P05-KO-U02-PARA-005|3|4555|4555|U02:20:20|cross_reference:NOE-P05-KO-U01-BIB-001
NOE-P05-KO-U02-PARA-006|paragraph|Lagrange fields and parameter construction|NOE-P05-KO-U02|6|4557|4557|U02:22:22|
NOE-P05-KO-U02-STATEMENT-001|statement|Minimal basis implies rational parameter construction|NOE-P05-KO-U02-PARA-006|1|4557|4557|U02:22:22|statement_of:NOE-P05-KO-U02-PARA-006
NOE-P05-KO-U03-PARA-001|paragraph|Symmetric-group example and Hilbert irreducibility|NOE-P05-KO-U03|1|4559|4559|U03:12:12|
NOE-P05-KO-U03-PARA-002|paragraph|Degree-three and degree-four groups and remaining question|NOE-P05-KO-U03|2|4561|4561|U03:14:14|
NOE-P05-KO-U03-PARA-003|paragraph|Integrity-basis definition and Hilbert problem 14|NOE-P05-KO-U03|3|4563|4563|U03:16:16|
NOE-P05-KO-U03-DEFINITION-001|definition|Integrity basis|NOE-P05-KO-U03-PARA-003|1|4563|4563|U03:16:16|defines:NOE-P05-KO-U03-PARA-003
NOE-P05-KO-U03-NOTE-001|footnote|Hilbert mathematical problems reference|NOE-P05-KO-U03-PARA-003|2|4563|4563|U03:16:16|note_for:NOE-P05-KO-U03-PARA-003
NOE-P05-KO-U03-BIB-001|bibliography_item|Hilbert mathematical problems, problem 14|NOE-P05-KO-U03-NOTE-001|1|4563|4563|U03:16:16|bibliography_for:NOE-P05-KO-U03-NOTE-001
NOE-P05-KO-U04-PARA-001|paragraph|Resultant criterion for an integrity basis|NOE-P05-KO-U04|1|4565|4565|U04:12:12|
NOE-P05-KO-U04-STATEMENT-001|statement|Sufficient nonzero homogeneous-resultant criterion|NOE-P05-KO-U04-PARA-001|1|4565|4565|U04:12:12|statement_of:NOE-P05-KO-U04-PARA-001
NOE-P05-KO-U04-DISPLAY-001|display|Linear-form equation|NOE-P05-KO-U04-PARA-001|2|4566|4568|U04:13:15|display_for:NOE-P05-KO-U04-PARA-001
NOE-P05-KO-U04-NOTE-001|footnote|Steinitz use of the irreducible equation|NOE-P05-KO-U04-DISPLAY-001|1|4569|4569|U04:16:16|note_for:NOE-P05-KO-U04-DISPLAY-001
NOE-P05-KO-U04-BIB-001|bibliography_item|Steinitz proof of the Lüroth theorem|NOE-P05-KO-U04-NOTE-001|1|4569|4569|U04:16:16|bibliography_for:NOE-P05-KO-U04-NOTE-001,cross_reference:NOE-P05-KO-U01-BIB-001
NOE-P05-KO-U04-PARA-002|paragraph|Unit-resultant condition and examples|NOE-P05-KO-U04|2|4570|4570|U04:17:17|
NOE-P05-KO-U04-PARA-003|paragraph|Sufficiency, nonnecessity, and open question|NOE-P05-KO-U04|3|4572|4572|U04:19:19|
'@

$allowedTypes = [System.Collections.Generic.HashSet[string]]::new([string[]]@(
    'work', 'unit', 'title', 'author', 'publication_note', 'paragraph',
    'footnote', 'bibliography_item', 'definition', 'statement', 'display'
))
$allowedRelations = [System.Collections.Generic.HashSet[string]]::new([string[]]@(
    'contains', 'embedded_in', 'continues', 'cross_reference', 'note_for',
    'bibliography_for', 'defines', 'statement_of', 'display_for'
))

$sourceHash = Get-FileSha256 $sourcePath
$targetHash = [ordered]@{}
foreach ($unit in $targets.Keys) {
    if (-not (Test-Path -LiteralPath $targets[$unit])) {
        throw ('Missing target file for ' + $unit + ': ' + $targets[$unit])
    }
    $targetHash[$unit] = Get-FileSha256 $targets[$unit]
}

$specs = [System.Collections.Generic.List[object]]::new()
foreach ($rawLine in $manifestText.Split([char]10, [System.StringSplitOptions]::RemoveEmptyEntries)) {
    $line = $rawLine.TrimEnd([char]13)
    $parts = $line.Split([char]'|')
    if ($parts.Count -ne 9) {
        throw "Manifest row does not have 9 columns: $line"
    }
    $targetSpecs = @($parts[7].Split([char]',', [System.StringSplitOptions]::RemoveEmptyEntries) | ForEach-Object { Convert-TargetSpec $_ })
    $relationSpecs = @($parts[8].Split([char]',', [System.StringSplitOptions]::RemoveEmptyEntries) | ForEach-Object { Convert-RelationSpec $_ })
    $specs.Add([pscustomobject]@{
        id = $parts[0]
        type = $parts[1]
        label = $parts[2]
        parent = if ([string]::IsNullOrEmpty($parts[3])) { $null } else { $parts[3] }
        order = [int]$parts[4]
        whole_start = [int]$parts[5]
        whole_end = [int]$parts[6]
        target_specs = $targetSpecs
        relation_specs = $relationSpecs
    })
}

$records = foreach ($spec in $specs) {
    $relations = [System.Collections.Generic.List[object]]::new()
    if ($null -ne $spec.parent) {
        $relations.Add([ordered]@{ relation = 'embedded_in'; target_id = $spec.parent })
    }
    foreach ($relationSpec in $spec.relation_specs) {
        $relations.Add([ordered]@{ relation = $relationSpec.relation; target_id = $relationSpec.target_id })
    }
    $targetLocators = foreach ($targetSpec in $spec.target_specs) {
        $targetPath = $targets[$targetSpec.unit]
        [ordered]@{
            unit_id = $targetSpec.unit
            path = $targetPath
            line_start = $targetSpec.line_start
            line_end = $targetSpec.line_end
            file_sha256 = $targetHash[$targetSpec.unit]
            slice_sha256_lf = Get-LfSliceSha256 $targetPath $targetSpec.line_start $targetSpec.line_end
        }
    }
    $cursorUnit = $spec.target_specs[-1].unit
    $base = [ordered]@{
        schema_version = '1.0'
        record_id = $spec.id
        work_id = 'NOE-P05'
        structure_type = $spec.type
        label = $spec.label
        parent_id = $spec.parent
        order = $spec.order
        source_language = 'de'
        target_language = 'ko-KR'
        authority_state = 'current_pointer_v003_preserved_candidate'
        source_locator = [ordered]@{
            path = $sourcePath
            whole_line_start = $spec.whole_start
            whole_line_end = $spec.whole_end
            paper_local_line_start = $spec.whole_start - 4534
            paper_local_line_end = $spec.whole_end - 4534
            file_sha256 = $sourceHash
            slice_sha256_lf = Get-LfSliceSha256 $sourcePath $spec.whole_start $spec.whole_end
        }
        target_locators = @($targetLocators)
        relations = @($relations)
        completion_state = 'producer_draft_text_covered'
        review_state = 'unchecked'
        publication_state = 'private_not_for_publication'
        continuation_cursor = $unitCursor[$cursorUnit]
    }
    $base.record_sha256 = Get-TextSha256 ($base | ConvertTo-Json -Compress -Depth 12)
    [pscustomobject]$base
}

$errors = [System.Collections.Generic.List[string]]::new()
if ($sourceHash -ne $expectedSourceHash) {
    $errors.Add("authority hash mismatch: expected $expectedSourceHash got $sourceHash")
}
$bodyHash = Get-LfSliceSha256 $sourcePath 4535 4573
if ($bodyHash -ne $expectedBodyHash) {
    $errors.Add("Paper 5 body hash mismatch: expected $expectedBodyHash got $bodyHash")
}
foreach ($unit in $unitSourceLines.Keys) {
    $range = $unitSourceLines[$unit]
    $actualSource = Get-LfSliceSha256 $sourcePath $range[0] $range[1]
    if ($actualSource -ne $expectedUnitSourceHash[$unit]) {
        $errors.Add(('unit source hash mismatch for ' + $unit + ': expected ' + $expectedUnitSourceHash[$unit] + ' got ' + $actualSource))
    }
    if ($targetHash[$unit] -ne $expectedTargetHash[$unit]) {
        $errors.Add(('target hash mismatch for ' + $unit + ': expected ' + $expectedTargetHash[$unit] + ' got ' + $targetHash[$unit]))
    }
}

$ids = @($records.record_id)
if (($ids | Sort-Object -Unique).Count -ne $ids.Count) {
    $errors.Add('duplicate record_id')
}
$idSet = [System.Collections.Generic.HashSet[string]]::new([string[]]$ids)
foreach ($record in $records) {
    if (-not $allowedTypes.Contains($record.structure_type)) {
        $errors.Add("invalid type $($record.structure_type) for $($record.record_id)")
    }
    if ($record.parent_id -and -not $idSet.Contains($record.parent_id)) {
        $errors.Add("missing parent $($record.parent_id) for $($record.record_id)")
    }
    if ((Get-LfSliceSha256 $record.source_locator.path $record.source_locator.whole_line_start $record.source_locator.whole_line_end) -ne $record.source_locator.slice_sha256_lf) {
        $errors.Add("source slice mismatch for $($record.record_id)")
    }
    foreach ($locator in $record.target_locators) {
        if ((Get-FileSha256 $locator.path) -ne $locator.file_sha256) {
            $errors.Add("target file mismatch for $($record.record_id) / $($locator.unit_id)")
        }
        if ((Get-LfSliceSha256 $locator.path $locator.line_start $locator.line_end) -ne $locator.slice_sha256_lf) {
            $errors.Add("target slice mismatch for $($record.record_id) / $($locator.unit_id)")
        }
    }
    foreach ($relation in $record.relations) {
        if (-not $allowedRelations.Contains($relation.relation)) {
            $errors.Add("invalid relation $($relation.relation) for $($record.record_id)")
        }
        if (-not $idSet.Contains($relation.target_id)) {
            $errors.Add("missing relation target $($relation.target_id) for $($record.record_id)")
        }
    }
    if ($record.review_state -ne 'unchecked' -or $record.publication_state -ne 'private_not_for_publication') {
        $errors.Add("state violation for $($record.record_id)")
    }
}

$jsonlPath = Join-Path $indexDir 'PRODUCER_STRUCTURAL_INDEX.jsonl'
$csvPath = Join-Path $indexDir 'PRODUCER_STRUCTURAL_INDEX.csv'
$reportPath = Join-Path $indexDir 'PRODUCER_STRUCTURAL_INDEX_VALIDATION_REPORT.json'
[System.IO.File]::WriteAllLines($jsonlPath, @($records | ForEach-Object { $_ | ConvertTo-Json -Compress -Depth 12 }), $utf8NoBom)

$csvRows = $records | ForEach-Object {
    [pscustomobject]@{
        record_id = $_.record_id
        work_id = $_.work_id
        structure_type = $_.structure_type
        label = $_.label
        parent_id = $_.parent_id
        order = $_.order
        source_path = $_.source_locator.path
        whole_line_start = $_.source_locator.whole_line_start
        whole_line_end = $_.source_locator.whole_line_end
        paper_local_line_start = $_.source_locator.paper_local_line_start
        paper_local_line_end = $_.source_locator.paper_local_line_end
        source_file_sha256 = $_.source_locator.file_sha256
        source_slice_sha256_lf = $_.source_locator.slice_sha256_lf
        target_units = (($_.target_locators | ForEach-Object { $_.unit_id }) -join ';')
        target_locators_json = ($_.target_locators | ConvertTo-Json -Compress -Depth 6)
        relations_json = ($_.relations | ConvertTo-Json -Compress -Depth 6)
        source_language = $_.source_language
        target_language = $_.target_language
        authority_state = $_.authority_state
        completion_state = $_.completion_state
        review_state = $_.review_state
        publication_state = $_.publication_state
        continuation_cursor = $_.continuation_cursor
        record_sha256 = $_.record_sha256
    }
}
$csvRows | Export-Csv -LiteralPath $csvPath -NoTypeInformation -Encoding utf8

$written = [System.IO.File]::ReadAllLines($jsonlPath, $utf8NoBom)
if ($written.Count -ne $records.Count) {
    $errors.Add("JSONL count mismatch: expected $($records.Count) got $($written.Count)")
}
foreach ($line in $written) {
    $parsed = $line | ConvertFrom-Json -Depth 20
    $baseLine = $line -replace ',"record_sha256":"[A-F0-9]{64}"}$', '}'
    if ((Get-TextSha256 $baseLine) -ne $parsed.record_sha256) {
        $errors.Add("record self-hash mismatch for $($parsed.record_id)")
    }
}
$csvReplay = @(Import-Csv -LiteralPath $csvPath)
if ($csvReplay.Count -ne $records.Count) {
    $errors.Add("CSV count mismatch: expected $($records.Count) got $($csvReplay.Count)")
}

$typeCounts = [ordered]@{}
foreach ($group in ($records | Group-Object structure_type | Sort-Object Name)) {
    $typeCounts[$group.Name] = $group.Count
}
$report = [ordered]@{
    schema = 'PRODUCER_STRUCTURAL_INDEX.schema.json'
    builder = 'build_and_validate_structural_index.ps1'
    status = if ($errors.Count -eq 0) { 'pass' } else { 'fail' }
    record_count = $records.Count
    unique_record_count = ($ids | Sort-Object -Unique).Count
    latest_record_id = $records[-1].record_id
    type_counts = $typeCounts
    pointer_id = $pointerId
    pointer_sha256 = $pointerHash
    authority_sha256 = $sourceHash
    body_slice_sha256_lf = $bodyHash
    unit_source_hashes_verified = $expectedUnitSourceHash
    target_file_sha256 = $targetHash
    jsonl_sha256 = Get-FileSha256 $jsonlPath
    csv_sha256 = Get-FileSha256 $csvPath
    errors = @($errors)
    continuation_cursor = $unitCursor.U04
    scope_note = 'Producer structural metadata only; pairing and labels are editorial inference. No source, Korean, formula, compile, render, checker, certification, or publication validation.'
}
[System.IO.File]::WriteAllText($reportPath, ($report | ConvertTo-Json -Depth 12), $utf8NoBom)
if ($errors.Count -gt 0) {
    throw "Structural index validation failed: $($errors -join '; ')"
}
Write-Output ($report | ConvertTo-Json -Compress -Depth 12)
