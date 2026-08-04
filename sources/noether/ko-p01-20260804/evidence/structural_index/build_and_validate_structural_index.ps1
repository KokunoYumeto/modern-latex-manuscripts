$ErrorActionPreference = 'Stop'

$indexDir = $PSScriptRoot
$root = (Resolve-Path -LiteralPath (Join-Path $indexDir '..\..')).Path
$sourcePath = 'C:\Users\Floris\Documents\interlanguage\03_projects\language_management\cjk\03_working_translations\noether_paper01_zh_translation_001_20260722\source\Noether_Paper01_CurrentGermanAuthority_interval.tex'
$sourceFileHash = '0499985866E646747EC31533775FF31B55556F2C694F4C2608384829DE248D2F'
$unitSourceHash = @{
    U01 = '4FAFC711A18FBE0B9C328DB74E8FB8BD88D46B168F2446B84310222014409AAE'
    U02 = '52BA4686D0C7DEBF68ECF9D4811971B31DA89E86369EB4DF1C010BFEF5AF67CA'
    U03 = '5642B68567271B6E3236371ECDE02E67C514499AA53EBE728BCCDA47E5D38BF3'
}
$targets = @{
    U01 = Join-Path $root 'ko\Noether_Paper01_Korean_U01_translation_draft_v001.tex'
    U02 = Join-Path $root 'ko\Noether_Paper01_Korean_U02_translation_draft_v001.tex'
    U03 = Join-Path $root 'ko\Noether_Paper01_Korean_U03_translation_draft_v001.tex'
}
$unitSourceLines = @{
    U01 = @(1, 24)
    U02 = @(25, 59)
    U03 = @(60, 80)
}
$unitCursor = @{
    U01 = 'continue at Paper 1 snapshot line 25 / Korean U02'
    U02 = 'continue at Paper 1 snapshot line 60 / Korean U03'
    U03 = 'Paper 1 substantive snapshot exhausted; Paper 2 excluded; await independent Korean checker'
}

function Get-FileSha256([string]$Path) {
    return (Get-FileHash -LiteralPath $Path -Algorithm SHA256).Hash
}

function Get-LfSliceSha256([string]$Path, [int]$Start, [int]$End) {
    $utf8 = [System.Text.UTF8Encoding]::new($false)
    $lines = [System.IO.File]::ReadAllLines($Path, $utf8)
    if ($Start -lt 1 -or $End -lt $Start -or $End -gt $lines.Length) {
        throw "Invalid line slice $Start-$End for $Path with $($lines.Length) lines"
    }
    $slice = [string]::Join("`n", $lines[($Start - 1)..($End - 1)]) + "`n"
    $bytes = $utf8.GetBytes($slice)
    $sha = [System.Security.Cryptography.SHA256]::Create()
    try { return ([System.BitConverter]::ToString($sha.ComputeHash($bytes))).Replace('-', '') }
    finally { $sha.Dispose() }
}

function New-Spec {
    param(
        [string]$Id, [string]$Type, [string]$Label, [AllowNull()][string]$Parent,
        [int]$Order, [string]$Unit, [int]$SourceStart, [int]$SourceEnd,
        [int]$TargetStart, [int]$TargetEnd, [string[]]$Related = @()
    )
    return [pscustomobject]@{
        id = $Id; type = $Type; label = $Label; parent = $Parent; order = $Order
        unit = $Unit; source_start = $SourceStart; source_end = $SourceEnd
        target_start = $TargetStart; target_end = $TargetEnd; related = $Related
    }
}

$specs = @(
    (New-Spec 'NOE-P01-KO-WORK-001' 'work' 'Paper 1 complete preserved interval' $null 1 'U01' 1 80 1 32 @('NOE-P01-KO-U01','NOE-P01-KO-U02','NOE-P01-KO-U03'))
    (New-Spec 'NOE-P01-KO-U01' 'unit' 'Literature, goal, and finite-system method' 'NOE-P01-KO-WORK-001' 1 'U01' 1 24 1 32)
    (New-Spec 'NOE-P01-KO-U01-TITLE-001' 'title' 'Paper title' 'NOE-P01-KO-U01' 1 'U01' 1 3 9 11)
    (New-Spec 'NOE-P01-KO-U01-AUTHOR-001' 'author' 'Emmy Noether byline' 'NOE-P01-KO-U01' 2 'U01' 4 5 12 13)
    (New-Spec 'NOE-P01-KO-U01-PUBLICATION-001' 'publication_note' 'Dissertation excerpt and journal receipt' 'NOE-P01-KO-U01' 3 'U01' 6 9 14 17)
    (New-Spec 'NOE-P01-KO-U01-PARA-001' 'paragraph' 'Prior work and Gordan special form system' 'NOE-P01-KO-U01' 4 'U01' 11 11 19 20)
    (New-Spec 'NOE-P01-KO-U01-NOTE-001' 'footnote' 'Prior-work bibliography note' 'NOE-P01-KO-U01-PARA-001' 1 'U01' 11 11 19 19 @('NOE-P01-KO-U01-BIB-001','NOE-P01-KO-U01-BIB-002','NOE-P01-KO-U01-BIB-003'))
    (New-Spec 'NOE-P01-KO-U01-BIB-001' 'bibliography_item' 'P. Gordan 1880' 'NOE-P01-KO-U01-NOTE-001' 1 'U01' 11 11 19 19)
    (New-Spec 'NOE-P01-KO-U01-BIB-002' 'bibliography_item' 'G. Maisano two papers' 'NOE-P01-KO-U01-NOTE-001' 2 'U01' 11 11 19 19)
    (New-Spec 'NOE-P01-KO-U01-BIB-003' 'bibliography_item' 'E. Pascal 1905' 'NOE-P01-KO-U01-NOTE-001' 3 'U01' 11 11 19 19)
    (New-Spec 'NOE-P01-KO-U01-PARA-002' 'paragraph' 'Maisano and Pascal results and linear relations' 'NOE-P01-KO-U01' 5 'U01' 13 19 22 28)
    (New-Spec 'NOE-P01-KO-U01-NOTE-002' 'footnote' 'Ordnung and Grad sense definition' 'NOE-P01-KO-U01-PARA-002' 1 'U01' 13 13 22 22)
    (New-Spec 'NOE-P01-KO-U01-NOTE-003' 'footnote' 'Covariant and invariant dependence dispute' 'NOE-P01-KO-U01-PARA-002' 2 'U01' 13 19 22 28 @('NOE-P01-KO-U01-DISPLAY-001','NOE-P01-KO-U01-DISPLAY-002'))
    (New-Spec 'NOE-P01-KO-U01-DISPLAY-001' 'display' 'First explicit linear relation' 'NOE-P01-KO-U01-NOTE-003' 1 'U01' 14 16 23 25)
    (New-Spec 'NOE-P01-KO-U01-DISPLAY-002' 'display' 'Second explicit linear relation' 'NOE-P01-KO-U01-NOTE-003' 2 'U01' 17 19 26 28)
    (New-Spec 'NOE-P01-KO-U01-PARA-003' 'paragraph' 'Research goal and relatively complete system' 'NOE-P01-KO-U01' 6 'U01' 21 21 30 30)
    (New-Spec 'NOE-P01-KO-U01-NOTE-004' 'footnote' 'Gordan-Kerschensteiner terminology reference' 'NOE-P01-KO-U01-PARA-003' 1 'U01' 21 21 30 30 @('NOE-P01-KO-U01-BIB-004'))
    (New-Spec 'NOE-P01-KO-U01-BIB-004' 'bibliography_item' 'Gordan-Kerschensteiner invariant theory lectures' 'NOE-P01-KO-U01-NOTE-004' 1 'U01' 21 21 30 30)
    (New-Spec 'NOE-P01-KO-U01-PARA-004' 'paragraph' 'General module-chain construction and Hilbert finiteness' 'NOE-P01-KO-U01' 7 'U01' 23 23 32 32)

    (New-Spec 'NOE-P01-KO-U02' 'unit' 'Module sequence and contraction theorem' 'NOE-P01-KO-WORK-001' 2 'U02' 25 59 1 42 @('NOE-P01-KO-U01'))
    (New-Spec 'NOE-P01-KO-U02-PARA-001' 'paragraph' 'Reduction to Delta and nu modules' 'NOE-P01-KO-U02' 1 'U02' 25 36 9 20)
    (New-Spec 'NOE-P01-KO-U02-DISPLAY-001' 'display' 'Delta and nu definitions' 'NOE-P01-KO-U02-PARA-001' 1 'U02' 26 28 10 12)
    (New-Spec 'NOE-P01-KO-U02-DISPLAY-002' 'display' 'nu iteration to s form' 'NOE-P01-KO-U02-PARA-001' 2 'U02' 30 32 14 16)
    (New-Spec 'NOE-P01-KO-U02-DISPLAY-003' 'display' 'nu of s continuation' 'NOE-P01-KO-U02-PARA-001' 3 'U02' 33 35 17 19)
    (New-Spec 'NOE-P01-KO-U02-TRANSITION-001' 'transition' 'Method announcement' 'NOE-P01-KO-U02' 2 'U02' 38 38 22 22)
    (New-Spec 'NOE-P01-KO-U02-DEFINITION-001' 'definition' 'Contraction process by factor-pair replacement' 'NOE-P01-KO-U02' 3 'U02' 40 54 24 38)
    (New-Spec 'NOE-P01-KO-U02-DISPLAY-004' 'display' 'Symbolic product to contract' 'NOE-P01-KO-U02-DEFINITION-001' 1 'U02' 43 45 27 29)
    (New-Spec 'NOE-P01-KO-U02-DISPLAY-005' 'display' 'Four contraction replacement table' 'NOE-P01-KO-U02-DEFINITION-001' 2 'U02' 47 53 31 37)
    (New-Spec 'NOE-P01-KO-U02-NOTE-001' 'footnote' 'Gordan contraction reference' 'NOE-P01-KO-U02-DEFINITION-001' 3 'U02' 54 54 38 38 @('NOE-P01-KO-U02-BIB-001'))
    (New-Spec 'NOE-P01-KO-U02-BIB-001' 'bibliography_item' 'Gordan Math. Annalen XVII p.219' 'NOE-P01-KO-U02-NOTE-001' 1 'U02' 54 54 38 38)
    (New-Spec 'NOE-P01-KO-U02-PARA-002' 'paragraph' 'Vanishing substitutions and theorem setup' 'NOE-P01-KO-U02' 4 'U02' 56 56 40 40)
    (New-Spec 'NOE-P01-KO-U02-THEOREM-001' 'theorem' 'Contractions I and II generate III and IV' 'NOE-P01-KO-U02' 5 'U02' 58 58 42 42 @('NOE-P01-KO-U02-DEFINITION-001'))
    (New-Spec 'NOE-P01-KO-U02-NOTE-002' 'footnote' 'Diagonal-member exception' 'NOE-P01-KO-U02-THEOREM-001' 1 'U02' 58 58 42 42)

    (New-Spec 'NOE-P01-KO-U03' 'unit' 'Form series, reductant theorem, and reduction methods' 'NOE-P01-KO-WORK-001' 3 'U03' 60 80 1 29 @('NOE-P01-KO-U02'))
    (New-Spec 'NOE-P01-KO-U03-DEFINITION-001' 'definition' 'Form series and rectangular scheme' 'NOE-P01-KO-U03' 1 'U03' 60 60 9 9 @('NOE-P01-KO-U02-THEOREM-001'))
    (New-Spec 'NOE-P01-KO-U03-LIST-001' 'list' 'Horizontal and vertical contraction movement' 'NOE-P01-KO-U03' 2 'U03' 61 64 10 13)
    (New-Spec 'NOE-P01-KO-U03-LIST-ITEM-001' 'list_item' 'Move right by contraction I' 'NOE-P01-KO-U03-LIST-001' 1 'U03' 62 62 11 11)
    (New-Spec 'NOE-P01-KO-U03-LIST-ITEM-002' 'list_item' 'Move down by contraction II' 'NOE-P01-KO-U03-LIST-001' 2 'U03' 63 63 12 12)
    (New-Spec 'NOE-P01-KO-U03-PARA-001' 'paragraph' 'Reductant theorem setup' 'NOE-P01-KO-U03' 3 'U03' 66 70 15 19)
    (New-Spec 'NOE-P01-KO-U03-DEFINITION-002' 'definition' 'Reductant as reducible form series' 'NOE-P01-KO-U03-PARA-001' 1 'U03' 67 69 16 18)
    (New-Spec 'NOE-P01-KO-U03-THEOREM-001' 'theorem' 'Reduction of the complete form series' 'NOE-P01-KO-U03' 4 'U03' 72 74 21 23 @('NOE-P01-KO-U03-DEFINITION-001','NOE-P01-KO-U03-DEFINITION-002'))
    (New-Spec 'NOE-P01-KO-U03-TRANSITION-001' 'transition' 'Further reduction methods' 'NOE-P01-KO-U03' 5 'U03' 76 76 25 25)
    (New-Spec 'NOE-P01-KO-U03-LIST-002' 'list' 'Double reduction and contraction with decomposable forms' 'NOE-P01-KO-U03' 6 'U03' 77 80 26 29)
    (New-Spec 'NOE-P01-KO-U03-LIST-ITEM-003' 'list_item' 'Double reduction' 'NOE-P01-KO-U03-LIST-002' 1 'U03' 78 78 27 27)
    (New-Spec 'NOE-P01-KO-U03-LIST-ITEM-004' 'list_item' 'Contraction with decomposable forms' 'NOE-P01-KO-U03-LIST-002' 2 'U03' 79 79 28 28 @('NOE-P01-KO-U03-DEFINITION-002'))
)

$targetHashes = @{}
foreach ($unit in $targets.Keys) { $targetHashes[$unit] = Get-FileSha256 $targets[$unit] }

$records = foreach ($spec in $specs) {
    $relations = @()
    if ($spec.parent) { $relations += [ordered]@{ relation = 'embedded_in'; target_id = $spec.parent } }
    foreach ($relatedId in $spec.related) { $relations += [ordered]@{ relation = 'cross_reference'; target_id = $relatedId } }

    $targetPath = $targets[$spec.unit]
    $baseRecord = [ordered]@{
        schema_version = '1.0'
        record_id = $spec.id
        work_id = 'NOE-P01'
        structure_type = $spec.type
        label = $spec.label
        parent_id = $spec.parent
        order = $spec.order
        source_language = 'de'
        target_language = 'ko-KR'
        authority_state = 'preserved_interval_historical_binding_pointer_pending'
        source_locator = [ordered]@{
            path = $sourcePath
            line_start = $spec.source_start
            line_end = $spec.source_end
            file_sha256 = $sourceFileHash
            slice_sha256_lf = Get-LfSliceSha256 $sourcePath $spec.source_start $spec.source_end
        }
        target_locator = [ordered]@{
            path = $targetPath
            line_start = $spec.target_start
            line_end = $spec.target_end
            file_sha256 = $targetHashes[$spec.unit]
            slice_sha256_lf = Get-LfSliceSha256 $targetPath $spec.target_start $spec.target_end
        }
        relations = $relations
        completion_state = 'producer_draft_text_covered'
        review_state = 'unchecked'
        publication_state = 'private_not_for_publication'
        continuation_cursor = $unitCursor[$spec.unit]
    }
    $canonical = $baseRecord | ConvertTo-Json -Compress -Depth 10
    $utf8 = [System.Text.UTF8Encoding]::new($false)
    $sha = [System.Security.Cryptography.SHA256]::Create()
    try { $recordHash = ([System.BitConverter]::ToString($sha.ComputeHash($utf8.GetBytes($canonical)))).Replace('-', '') }
    finally { $sha.Dispose() }
    $baseRecord.record_sha256 = $recordHash
    [pscustomobject]$baseRecord
}

$errors = [System.Collections.Generic.List[string]]::new()
$ids = @($records.record_id)
if (($ids | Sort-Object -Unique).Count -ne $ids.Count) { $errors.Add('duplicate record_id') }
$idSet = [System.Collections.Generic.HashSet[string]]::new([string[]]$ids)
foreach ($record in $records) {
    if ($record.parent_id -and -not $idSet.Contains($record.parent_id)) { $errors.Add("missing parent $($record.parent_id) for $($record.record_id)") }
    if ($record.source_locator.file_sha256 -ne (Get-FileSha256 $record.source_locator.path)) { $errors.Add("source file hash mismatch for $($record.record_id)") }
    if ($record.target_locator.file_sha256 -ne (Get-FileSha256 $record.target_locator.path)) { $errors.Add("target file hash mismatch for $($record.record_id)") }
    if ($record.review_state -ne 'unchecked' -or $record.publication_state -ne 'private_not_for_publication') { $errors.Add("state violation for $($record.record_id)") }
    foreach ($relation in $record.relations) { if (-not $idSet.Contains($relation.target_id)) { $errors.Add("missing relation target $($relation.target_id) for $($record.record_id)") } }
}

$jsonlPath = Join-Path $indexDir 'PRODUCER_STRUCTURAL_INDEX.jsonl'
$csvPath = Join-Path $indexDir 'PRODUCER_STRUCTURAL_INDEX.csv'
$reportPath = Join-Path $indexDir 'PRODUCER_STRUCTURAL_INDEX_VALIDATION_REPORT.json'
$utf8NoBom = [System.Text.UTF8Encoding]::new($false)
[System.IO.File]::WriteAllLines($jsonlPath, @($records | ForEach-Object { $_ | ConvertTo-Json -Compress -Depth 10 }), $utf8NoBom)

$csvRows = $records | ForEach-Object {
    [pscustomobject]@{
        record_id = $_.record_id; work_id = $_.work_id; structure_type = $_.structure_type; label = $_.label
        parent_id = $_.parent_id; order = $_.order; source_path = $_.source_locator.path
        source_line_start = $_.source_locator.line_start; source_line_end = $_.source_locator.line_end
        source_file_sha256 = $_.source_locator.file_sha256; source_slice_sha256_lf = $_.source_locator.slice_sha256_lf
        target_path = $_.target_locator.path; target_line_start = $_.target_locator.line_start
        target_line_end = $_.target_locator.line_end; target_file_sha256 = $_.target_locator.file_sha256
        target_slice_sha256_lf = $_.target_locator.slice_sha256_lf
        relations_json = ($_.relations | ConvertTo-Json -Compress -Depth 4)
        source_language = $_.source_language; target_language = $_.target_language
        authority_state = $_.authority_state; completion_state = $_.completion_state
        review_state = $_.review_state; publication_state = $_.publication_state
        continuation_cursor = $_.continuation_cursor; record_sha256 = $_.record_sha256
    }
}
$csvRows | Export-Csv -LiteralPath $csvPath -NoTypeInformation -Encoding utf8

$typeCounts = [ordered]@{}
foreach ($group in ($records | Group-Object structure_type | Sort-Object Name)) { $typeCounts[$group.Name] = $group.Count }
$report = [ordered]@{
    schema = 'PRODUCER_STRUCTURAL_INDEX.schema.json'
    generated_at = (Get-Date -Format o)
    status = if ($errors.Count -eq 0) { 'pass' } else { 'fail' }
    record_count = $records.Count
    unique_record_count = ($ids | Sort-Object -Unique).Count
    type_counts = $typeCounts
    jsonl_sha256 = Get-FileSha256 $jsonlPath
    csv_sha256 = Get-FileSha256 $csvPath
    errors = @($errors)
    scope_note = 'Mechanical producer metadata only; no source, Korean, formula, completeness, build, render, or publication validation.'
}
[System.IO.File]::WriteAllText($reportPath, ($report | ConvertTo-Json -Depth 8), $utf8NoBom)
if ($errors.Count -gt 0) { throw "Structural index validation failed: $($errors -join '; ')" }
Write-Output ($report | ConvertTo-Json -Compress -Depth 8)
