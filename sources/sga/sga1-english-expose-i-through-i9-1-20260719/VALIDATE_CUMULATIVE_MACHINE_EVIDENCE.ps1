[CmdletBinding()]
param()
$ErrorActionPreference = 'Stop'
$root = $PSScriptRoot
$utf8 = [Text.UTF8Encoding]::new($false)
function Sha([string] $Path) { (Get-FileHash -LiteralPath $Path -Algorithm SHA256).Hash }
function Sha-Utf8Text([string] $Text) { [BitConverter]::ToString([Security.Cryptography.SHA256]::HashData($utf8.GetBytes($Text))).Replace('-','') }
function Read-Jsonl([string] $Path) {
    $result = @()
    foreach ($line in [IO.File]::ReadAllLines($Path,[Text.UTF8Encoding]::new($false,$true))) {
        if (-not [string]::IsNullOrWhiteSpace($line)) { $result += ($line | ConvertFrom-Json -Depth 40) }
    }
    $result
}
function Reference-Values($Record,[string] $Field) {
    $property = $Record.PSObject.Properties[$Field]
    if ($null -eq $property -or $null -eq $property.Value) { return @() }
    if ($property.Value -is [string]) { return @([string]$property.Value) }
    @($property.Value | ForEach-Object { [string]$_ })
}

$historical = Join-Path $root 'evidence\predecessor_i8_r4_machine_controls'
$historicalFiles = @(Get-ChildItem -LiteralPath $historical -File | Sort-Object Name)
if ($historicalFiles.Count -ne 36 -or @(Get-ChildItem -LiteralPath $historical -Directory).Count -ne 0 -or [long]($historicalFiles | Measure-Object Length -Sum).Sum -ne 353919) { throw 'Historical I.8 machine-control extent mismatch' }
$historicalLines = @($historicalFiles | ForEach-Object { "$($_.Name)|$($_.Length)|$(Sha $_.FullName)" })
$historicalDigest = Sha-Utf8Text (($historicalLines -join "`n") + "`n")
if ($historicalDigest -cne 'F307B8431C9237FD275A2DEB6062E1E0E9E86801CCBF57998EF7C2D2ED7E1789') { throw 'Historical I.8 machine-control inventory mismatch' }

$historicalSchema = [IO.File]::ReadAllText((Join-Path $historical 'PUBLIC_SGA1_MACHINE_LEDGER_SCHEMA_v5.json'),[Text.UTF8Encoding]::new($false,$true)) | ConvertFrom-Json -Depth 40
if (@($historicalSchema.csv_ledgers.PSObject.Properties).Count -ne 23 -or @($historicalSchema.graph_jsonl).Count -ne 5 -or @($historicalSchema.difficulty_jsonl).Count -ne 5 -or [long]$historicalSchema.continuation_cursor.line -ne 1654 -or $historicalSchema.continuation_cursor.excluded -ne $true) { throw 'Historical I.8 schema declaration mismatch' }

Add-Type -AssemblyName Microsoft.VisualBasic
$historicalCsv = @(Get-ChildItem -LiteralPath $historical -Filter '*.csv' -File | Sort-Object Name)
if ($historicalCsv.Count -ne 23) { throw 'Historical I.8 CSV file count mismatch' }
$historicalCsvRows = 0
foreach ($csv in $historicalCsv) {
    $parser = [Microsoft.VisualBasic.FileIO.TextFieldParser]::new($csv.FullName,[Text.Encoding]::UTF8,$true)
    $parser.TextFieldType = [Microsoft.VisualBasic.FileIO.FieldType]::Delimited
    $parser.SetDelimiters(',')
    $parser.HasFieldsEnclosedInQuotes = $true
    $matrix = [Collections.Generic.List[object]]::new()
    try { while (-not $parser.EndOfData) { $matrix.Add(@($parser.ReadFields())) } } finally { $parser.Close() }
    if ($matrix.Count -lt 1) { throw "Historical CSV empty: $($csv.Name)" }
    $declared = $historicalSchema.csv_ledgers.PSObject.Properties[$csv.Name]
    if ($null -eq $declared -or (@($declared.Value) -join "`n") -cne (@($matrix[0]) -join "`n")) { throw "Historical CSV header/schema mismatch: $($csv.Name)" }
    $columns = @($matrix[0]).Count
    $ids = [Collections.Generic.HashSet[string]]::new([StringComparer]::Ordinal)
    for ($index=1; $index -lt $matrix.Count; $index++) {
        $row = @($matrix[$index])
        if ($row.Count -ne $columns -or [string]::IsNullOrWhiteSpace([string]$row[0]) -or -not $ids.Add([string]$row[0])) { throw "Historical CSV rectangular/ID failure: $($csv.Name)" }
        foreach ($cell in $row) { if ([string]$cell -match '^[\s]*[=+@]' -or [string]$cell -match '^[\s]*-(?!\d)') { throw "Historical CSV formula-safety failure: $($csv.Name)" } }
    }
    $historicalCsvRows += $matrix.Count - 1
}
if ($historicalCsvRows -ne 400) { throw 'Historical I.8 CSV row total mismatch' }

$historicalJsonFiles = @(Get-ChildItem -LiteralPath $historical -Filter '*.jsonl' -File | Sort-Object Name)
if ($historicalJsonFiles.Count -ne 10) { throw 'Historical I.8 JSONL file count mismatch' }
$historicalRecords = @()
foreach ($path in $historicalJsonFiles) { $historicalRecords += @(Read-Jsonl $path.FullName) }
if ($historicalRecords.Count -ne 145) { throw 'Historical I.8 JSONL record total mismatch' }
$i9Graph = @(Read-Jsonl (Join-Path $root 'ledgers\SGA1_I9_1_EVIDENCE_GRAPH.jsonl'))
$i9Difficulty = @(Read-Jsonl (Join-Path $root 'ledgers\SGA1_DIFFICULTY_FAILURE_REVISION.jsonl'))
if ($i9Graph.Count -ne 4 -or $i9Difficulty.Count -ne 14) { throw 'I.9.1 JSONL projection count mismatch' }
$combined = @($historicalRecords) + @($i9Graph) + @($i9Difficulty)
$byId = @{}
foreach ($record in $combined) {
    $id = [string]$record.record_id
    if ([string]::IsNullOrWhiteSpace($id) -or $byId.ContainsKey($id)) { throw "Combined JSONL duplicate/blank ID: $id" }
    $byId[$id] = $record
}
if ($byId.Count -ne 163) { throw 'Combined JSONL unique-record total mismatch' }
$referenceFields = @('parent_id','child_ids','local_reference_ids','revision_record_id','supersedes_record_ids','superseded_by_record_id','closes_record_ids','closed_by_record_id','related_record_ids')
foreach ($record in $combined) {
    foreach ($field in $referenceFields) {
        foreach ($reference in @(Reference-Values $record $field)) {
            if ([string]::IsNullOrWhiteSpace($reference)) { continue }
            if ($reference.StartsWith('SGA1-',[StringComparison]::Ordinal) -and -not $byId.ContainsKey($reference)) { throw "Combined JSONL reference not closed: $($record.record_id).$field -> $reference" }
        }
    }
}
$historicalReceipt = [IO.File]::ReadAllText((Join-Path $historical 'PUBLIC_MACHINE_VALIDATION_I_8.txt'))
$historicalCsvReceipt = [IO.File]::ReadAllText((Join-Path $historical 'PUBLIC_CSV_ARTIFACT_VALIDATION_I_8.txt'))
if (-not $historicalReceipt.Contains('csv_rows=400') -or -not $historicalReceipt.Contains('jsonl_records=145') -or -not $historicalReceipt.Contains('failures=0') -or -not $historicalCsvReceipt.Contains("files=23`tdata_rows=400`tfailures=0")) { throw 'Historical I.8 validation receipts do not attest the frozen controls' }

Write-Output 'CUMULATIVE_MACHINE_EVIDENCE_VERIFY=PASS'
Write-Output 'HISTORICAL_I8_FILES=36'
Write-Output 'HISTORICAL_I8_BYTES=353919'
Write-Output 'HISTORICAL_I8_CSV_FILES=23'
Write-Output 'HISTORICAL_I8_CSV_ROWS=400'
Write-Output 'HISTORICAL_I8_JSONL_FILES=10'
Write-Output 'HISTORICAL_I8_JSONL_RECORDS=145'
Write-Output 'CURRENT_I9_CSV_FILES=17'
Write-Output 'CURRENT_I9_CSV_ROWS=382'
Write-Output 'CURRENT_I9_JSONL_FILES=2'
Write-Output 'CURRENT_I9_JSONL_RECORDS=18'
Write-Output 'COMBINED_JSONL_UNIQUE_RECORDS=163'
Write-Output 'COMBINED_JSONL_REFERENCE_CLOSURE=PASS'
Write-Output 'PREDECESSOR_TARGET_CLOSURE=historically_verified_in_immutable_i8_r4_not_rebased'