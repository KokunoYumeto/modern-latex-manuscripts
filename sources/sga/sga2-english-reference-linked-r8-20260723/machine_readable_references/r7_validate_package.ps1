param(
    [Parameter(Mandatory = $false)]
    [string]$Root = (Split-Path -Parent $PSScriptRoot)
)

$ErrorActionPreference = 'Stop'
$rootPath = (Resolve-Path -LiteralPath $Root).Path
$managerRoot = Split-Path -Parent $rootPath
$r6Root = Join-Path $managerRoot 'sga2_full_reader_reference_retrofit_r6_exhaustive'
$errors = [System.Collections.Generic.List[string]]::new()

function Add-Error([string]$message) {
    $errors.Add($message)
}

function Hash-File([string]$path) {
    (Get-FileHash -Algorithm SHA256 -LiteralPath $path).Hash
}

function Relative([string]$path) {
    [IO.Path]::GetRelativePath($rootPath, $path).Replace('\', '/')
}

$coreRelative = @(
    'SGA2_English_Full_Reader.tex',
    'SGA2_English_Full_Reader.pdf',
    'sga2_reader_macros.tex'
)
$coreRelative += 0..14 | ForEach-Object {
    if ($_ -eq 0) { 'parts/00_introduction.tex' }
    else {
        $roman = @('', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV')[$_]
        ('parts/{0:D2}_expose_{1}.tex' -f $_, $roman)
    }
}

$coreMatches = 0
foreach ($relative in $coreRelative) {
    $r7 = Join-Path $rootPath $relative
    $r6 = Join-Path $r6Root $relative
    if (-not (Test-Path -LiteralPath $r7 -PathType Leaf)) {
        Add-Error "missing_r7_core:$relative"
        continue
    }
    if (-not (Test-Path -LiteralPath $r6 -PathType Leaf)) {
        Add-Error "missing_r6_core:$relative"
        continue
    }
    if ((Get-Item -LiteralPath $r7).Length -ne (Get-Item -LiteralPath $r6).Length -or
        (Hash-File $r7) -ne (Hash-File $r6)) {
        Add-Error "core_identity_mismatch:$relative"
    } else {
        $coreMatches++
    }
}

$activeStale = @(
    'SHA256SUMS.csv',
    'ZENODO_PAYLOAD_MANIFEST.csv',
    'machine_readable_references/DELIVERY_MANIFEST.csv',
    'machine_readable_references/DELIVERY_MANIFEST_VALIDATION.json',
    'machine_readable_references/FINAL_REFERENCE_SUMMARY.json',
    'machine_readable_references/INDEPENDENT_REFERENCE_AUDIT.md',
    'machine_readable_references/PRODUCER_SUMMARY.json'
)
foreach ($relative in $activeStale) {
    if (Test-Path -LiteralPath (Join-Path $rootPath $relative)) {
        Add-Error "stale_control_still_active:$relative"
    }
}

$forbiddenLog = Join-Path $rootPath 'evidence/SGA2_English_Full_Reader_SANITIZED.log'
if (Test-Path -LiteralPath $forbiddenLog) {
    Add-Error 'path_bearing_log_present'
}

$failReceipt = Join-Path $managerRoot 'ROOT_INDEPENDENT_SGA2_R6_REFERENCE_RETROFIT_FAIL_20260723.md'
$failReceiptExpected = '2C59A610B704FF8EAAC80EA91EBE951BB25DDCDE95D21C815103EA62424A33BA'
if (-not (Test-Path -LiteralPath $failReceipt -PathType Leaf)) {
    Add-Error 'missing_r6_fail_receipt'
} elseif ((Hash-File $failReceipt) -ne $failReceiptExpected) {
    Add-Error 'r6_fail_receipt_hash_mismatch'
}

$csvRelative = @(
    'machine_readable_references/REFERENCE_TARGETS.csv',
    'machine_readable_references/REFERENCE_EDGES.csv',
    'machine_readable_references/REFERENCE_CANDIDATES.csv',
    'machine_readable_references/LOCATOR_RESIDUAL_AUDIT.csv',
    'machine_readable_references/MANUAL_ADJUDICATION.csv',
    'machine_readable_references/R6_MANUAL_REVIEW_QUEUE.csv',
    'machine_readable_references/SOURCE_RECONSTRUCTION_ALL_15.csv',
    'machine_readable_references/R7_FORMULA_SAFETY_REPAIR.csv'
)

$formulaHits = [System.Collections.Generic.List[object]]::new()
$csvMetrics = [ordered]@{}
foreach ($relative in $csvRelative) {
    $path = Join-Path $rootPath $relative
    if (-not (Test-Path -LiteralPath $path -PathType Leaf)) {
        Add-Error "missing_csv:$relative"
        continue
    }
    $rows = @(Import-Csv -LiteralPath $path)
    $headers = @()
    if ($rows.Count -gt 0) {
        $headers = @($rows[0].PSObject.Properties.Name)
    } else {
        $firstLine = Get-Content -LiteralPath $path -TotalCount 1
        $headers = @($firstLine -split ',')
    }
    $rowIndex = 1
    foreach ($row in $rows) {
        foreach ($property in $row.PSObject.Properties) {
            $text = [string]$property.Value
            $trimmed = $text.TrimStart()
            $trigger = ($trimmed -match '^[=+@]') -or
                (($trimmed -match '^-') -and ($trimmed -notmatch '^-\d+(?:[.,]\d+)?(?:\s|$)'))
            if ($trigger) {
                $formulaHits.Add([ordered]@{
                    file = $relative
                    row = $rowIndex
                    column = $property.Name
                })
            }
        }
        $rowIndex++
    }
    $csvMetrics[$relative] = [ordered]@{
        rows = $rows.Count
        columns = $headers.Count
        bytes = (Get-Item -LiteralPath $path).Length
        sha256 = Hash-File $path
    }
}
if ($formulaHits.Count -ne 0) {
    Add-Error "formula_trigger_cells:$($formulaHits.Count)"
}

$targetRows = @(Import-Csv -LiteralPath (Join-Path $rootPath 'machine_readable_references/REFERENCE_TARGETS.csv'))
$edgeRows = @(Import-Csv -LiteralPath (Join-Path $rootPath 'machine_readable_references/REFERENCE_EDGES.csv'))
$candidateRows = @(Import-Csv -LiteralPath (Join-Path $rootPath 'machine_readable_references/REFERENCE_CANDIDATES.csv'))
$residualRows = @(Import-Csv -LiteralPath (Join-Path $rootPath 'machine_readable_references/LOCATOR_RESIDUAL_AUDIT.csv'))
$manualRows = @(Import-Csv -LiteralPath (Join-Path $rootPath 'machine_readable_references/MANUAL_ADJUDICATION.csv'))

$targetIds = [System.Collections.Generic.HashSet[string]]::new([StringComparer]::Ordinal)
$targetLabels = [System.Collections.Generic.HashSet[string]]::new([StringComparer]::Ordinal)
foreach ($row in $targetRows) {
    if (-not $targetIds.Add([string]$row.stable_id)) { Add-Error "duplicate_target_id:$($row.stable_id)" }
    if (-not $targetLabels.Add([string]$row.latex_label)) { Add-Error "duplicate_target_label:$($row.latex_label)" }
}
$edgeIds = [System.Collections.Generic.HashSet[string]]::new([StringComparer]::Ordinal)
foreach ($row in $edgeRows) {
    if (-not $edgeIds.Add([string]$row.edge_id)) { Add-Error "duplicate_edge_id:$($row.edge_id)" }
    if (-not $targetIds.Contains([string]$row.target_stable_id)) {
        Add-Error "edge_target_missing:$($row.edge_id):$($row.target_stable_id)"
    }
}

$pageCount = $null
$muToolCommand = Get-Command mutool -ErrorAction SilentlyContinue
if ($null -eq $muToolCommand) {
    Add-Error 'mutool_unavailable'
} else {
    $pageText = & $muToolCommand.Source show (Join-Path $rootPath 'SGA2_English_Full_Reader.pdf') 'trailer/Root/Pages/Count'
    if ($pageText -match '^\s*(\d+)\s*$') { $pageCount = [int]$Matches[1] }
    if ($pageCount -ne 184) { Add-Error "pdf_page_count:$pageCount" }
}

$jsonFailures = [System.Collections.Generic.List[string]]::new()
Get-ChildItem -LiteralPath (Join-Path $rootPath 'machine_readable_references') -Filter '*.json' -File |
    ForEach-Object {
        try { $null = Get-Content -Raw -LiteralPath $_.FullName | ConvertFrom-Json }
        catch { $jsonFailures.Add($_.Name) }
    }
if ($jsonFailures.Count -ne 0) {
    Add-Error "json_parse_failures:$($jsonFailures -join ';')"
}

$result = [ordered]@{
    schema = 'english-germanic-sga2-r7-producer-validation-v1'
    work = 'SGA2'
    date = '2026-07-23'
    status = if ($errors.Count -eq 0) { 'PASS' } else { 'FAIL' }
    root = Split-Path -Leaf $rootPath
    frozen_core = [ordered]@{
        compared_files = $coreRelative.Count
        exact_matches = $coreMatches
        reader_tex_sha256 = Hash-File (Join-Path $rootPath 'SGA2_English_Full_Reader.tex')
        reader_pdf_sha256 = Hash-File (Join-Path $rootPath 'SGA2_English_Full_Reader.pdf')
        reader_pdf_pages = $pageCount
    }
    graph = [ordered]@{
        targets = $targetRows.Count
        edges = $edgeRows.Count
        candidates = $candidateRows.Count
        residual_occurrences = $residualRows.Count
        manual_adjudications = $manualRows.Count
        target_ids_unique = ($targetIds.Count -eq $targetRows.Count)
        target_labels_unique = ($targetLabels.Count -eq $targetRows.Count)
        edge_ids_unique = ($edgeIds.Count -eq $edgeRows.Count)
        edge_target_closure = -not ($errors | Where-Object { $_ -like 'edge_target_missing:*' })
    }
    package_repairs = [ordered]@{
        formula_trigger_cells = $formulaHits.Count
        repair_ledger_rows = @(Import-Csv -LiteralPath (Join-Path $rootPath 'machine_readable_references/R7_FORMULA_SAFETY_REPAIR.csv')).Count
        path_bearing_log_present = (Test-Path -LiteralPath $forbiddenLog)
        stale_controls_active = @($activeStale | Where-Object { Test-Path -LiteralPath (Join-Path $rootPath $_) }).Count
        predecessor_fail_receipt_exact = ((Test-Path -LiteralPath $failReceipt) -and ((Hash-File $failReceipt) -eq $failReceiptExpected))
    }
    csv_metrics = $csvMetrics
    json_parse_failures = $jsonFailures
    errors = $errors
}

$output = Join-Path $rootPath 'machine_readable_references/R7_PRODUCER_VALIDATION.json'
$json = $result | ConvertTo-Json -Depth 12
[IO.File]::WriteAllText($output, $json + [Environment]::NewLine, [Text.UTF8Encoding]::new($false))
if ($errors.Count -ne 0) { exit 1 }
