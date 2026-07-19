[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'
$workpass = $PSScriptRoot
$schemaPath = Join-Path $workpass 'ledgers\SGA1_MACHINE_LEDGER_SCHEMA_v1.json'
$graphPaths = @(
    (Join-Path $workpass 'ledgers\SGA1_I9_1_EVIDENCE_GRAPH.jsonl')
)
$difficultyPath = Join-Path $workpass 'ledgers\SGA1_DIFFICULTY_FAILURE_REVISION.jsonl'
$candidateRoot = $workpass
$script:failures = 0

function Report([string] $kind, [string] $label, [string] $detail) {
    Write-Output "$kind`t$label`t$detail"
    if ($kind -eq 'FAIL') { $script:failures++ }
}

function Read-StrictUtf8([string] $path) {
    $bytes = [IO.File]::ReadAllBytes($path)
    $encoding = [Text.UTF8Encoding]::new($false, $true)
    return $encoding.GetString($bytes)
}

function Check-JsonElementKeys(
    [System.Text.Json.JsonElement] $element,
    [string] $where
) {
    if ($element.ValueKind -eq [System.Text.Json.JsonValueKind]::Object) {
        $seen = [Collections.Generic.HashSet[string]]::new(
            [StringComparer]::Ordinal
        )
        foreach ($property in $element.EnumerateObject()) {
            if (-not $seen.Add($property.Name)) {
                Report 'FAIL' 'Duplicate JSON object key' "$where::$($property.Name)"
            }
            Check-JsonElementKeys $property.Value "$where.$($property.Name)"
        }
    }
    elseif ($element.ValueKind -eq [System.Text.Json.JsonValueKind]::Array) {
        $index = 0
        foreach ($item in $element.EnumerateArray()) {
            Check-JsonElementKeys $item "$where[$index]"
            $index++
        }
    }
}

function Get-ReferenceValues($record, [string] $fieldName) {
    $property = $record.PSObject.Properties[$fieldName]
    if ($null -eq $property -or $null -eq $property.Value) { return @() }
    if ($property.Value -is [string]) { return @([string] $property.Value) }
    return @($property.Value | ForEach-Object { [string] $_ })
}

function Resolve-RecordedArtifact([string] $relativePath) {
    if ([string]::IsNullOrWhiteSpace($relativePath)) { return $null }
    if ([IO.Path]::IsPathRooted($relativePath)) { return $null }
    $normalized = $relativePath.Replace('/', '\')
    if ($normalized.StartsWith('SGA1_English_Expose_I_', [StringComparison]::Ordinal)) {
        return Join-Path $candidateRoot $normalized
    }
    return Join-Path $workpass $normalized
}

$schemaText = Read-StrictUtf8 $schemaPath
$schema = $schemaText | ConvertFrom-Json -Depth 20
Report 'PASS' 'Schema UTF-8 and JSON parse' "sha256=$((Get-FileHash -LiteralPath $schemaPath -Algorithm SHA256).Hash)"

Add-Type -AssemblyName Microsoft.VisualBasic
$csvTotalRows = 0
foreach ($declaration in $schema.csv_ledgers.PSObject.Properties) {
    $relative = $declaration.Name
    $expectedHeader = @($declaration.Value | ForEach-Object { [string] $_ })
    $path = Join-Path $workpass $relative.Replace('/', '\')
    if (-not (Test-Path -LiteralPath $path -PathType Leaf)) {
        Report 'FAIL' 'CSV exists' $relative
        continue
    }
    try {
        $null = Read-StrictUtf8 $path
        Report 'PASS' 'CSV strict UTF-8' $relative
    }
    catch {
        Report 'FAIL' 'CSV strict UTF-8' "$relative :: $($_.Exception.Message)"
        continue
    }

    $parser = [Microsoft.VisualBasic.FileIO.TextFieldParser]::new(
        $path,
        [Text.Encoding]::UTF8,
        $true
    )
    $parser.TextFieldType = [Microsoft.VisualBasic.FileIO.FieldType]::Delimited
    $parser.SetDelimiters(',')
    $parser.HasFieldsEnclosedInQuotes = $true
    $physicalRows = [Collections.Generic.List[object]]::new()
    try {
        while (-not $parser.EndOfData) {
            $physicalRows.Add(@($parser.ReadFields()))
        }
    }
    catch {
        Report 'FAIL' 'CSV parse' "$relative :: $($_.Exception.Message)"
    }
    finally {
        $parser.Close()
    }
    if ($physicalRows.Count -eq 0) {
        Report 'FAIL' 'CSV nonempty' $relative
        continue
    }

    $header = @($physicalRows[0])
    $headerExact = $header.Count -eq $expectedHeader.Count
    if ($headerExact) {
        for ($i = 0; $i -lt $header.Count; $i++) {
            if ($header[$i] -cne $expectedHeader[$i]) { $headerExact = $false }
        }
    }
    Report ($headerExact ? 'PASS' : 'FAIL') 'CSV declared header' "$relative :: columns=$($header.Count)"

    $rectangular = $true
    $formulaSafe = $true
    $ids = [Collections.Generic.HashSet[string]]::new([StringComparer]::Ordinal)
    $idsUnique = $true
    for ($rowIndex = 1; $rowIndex -lt $physicalRows.Count; $rowIndex++) {
        $fields = @($physicalRows[$rowIndex])
        if ($fields.Count -ne $header.Count) { $rectangular = $false }
        if ($fields.Count -gt 0) {
            $id = [string] $fields[0]
            if ([string]::IsNullOrWhiteSpace($id) -or -not $ids.Add($id)) {
                $idsUnique = $false
            }
        }
        foreach ($field in $fields) {
            $value = ([string] $field).TrimStart()
            if ($value -match '^[=+\-@]') { $formulaSafe = $false }
        }
    }
    $dataRows = [Math]::Max(0, $physicalRows.Count - 1)
    $csvTotalRows += $dataRows
    Report ($rectangular ? 'PASS' : 'FAIL') 'CSV rectangular' "$relative :: rows=$dataRows; columns=$($header.Count)"
    Report ($idsUnique ? 'PASS' : 'FAIL') 'CSV primary IDs unique' "$relative :: ids=$($ids.Count)"
    Report ($formulaSafe ? 'PASS' : 'FAIL') 'CSV formula-injection safe' $relative
    Report 'PASS' 'CSV hash' "$relative :: bytes=$((Get-Item -LiteralPath $path).Length); sha256=$((Get-FileHash -LiteralPath $path -Algorithm SHA256).Hash)"
}

$allRecords = [Collections.Generic.List[object]]::new()
$recordsById = @{}
$jsonFiles = @()
foreach ($graphPath in $graphPaths) {
    $jsonFiles += @{
        Path = $graphPath
        Version = [string] $schema.graph_schema_version
        Required = @($schema.graph_required_fields)
        Types = @($schema.graph_record_types)
    }
}
$jsonFiles += @{
    Path = $difficultyPath
    Version = [string] $schema.difficulty_schema_version
    Required = @($schema.difficulty_required_fields)
    Types = @($schema.difficulty_record_types)
}

foreach ($spec in $jsonFiles) {
    $text = Read-StrictUtf8 $spec.Path
    $lineNumber = 0
    $recordCount = 0
    foreach ($line in ($text -split '\r?\n')) {
        $lineNumber++
        if ([string]::IsNullOrWhiteSpace($line)) { continue }
        $recordCount++
        try {
            $document = [System.Text.Json.JsonDocument]::Parse($line)
            Check-JsonElementKeys $document.RootElement "$(Split-Path $spec.Path -Leaf):$lineNumber"
            $document.Dispose()
            $record = $line | ConvertFrom-Json -Depth 30
        }
        catch {
            Report 'FAIL' 'JSONL parse' "$(Split-Path $spec.Path -Leaf):$lineNumber :: $($_.Exception.Message)"
            continue
        }

        $names = @($record.PSObject.Properties.Name)
        foreach ($required in $spec.Required) {
            if ($required -notin $names) {
                Report 'FAIL' 'JSONL required field' "$($record.record_id) :: missing $required"
            }
        }
        if ($record.schema_version -cne $spec.Version) {
            Report 'FAIL' 'JSONL schema version' "$($record.record_id) :: $($record.schema_version)"
        }
        if ($record.record_type -notin $spec.Types) {
            Report 'FAIL' 'JSONL record type' "$($record.record_id) :: $($record.record_type)"
        }
        if ($record.status -notin @($schema.allowed_statuses)) {
            Report 'FAIL' 'JSONL status enum' "$($record.record_id) :: $($record.status)"
        }
        $id = [string] $record.record_id
        if ([string]::IsNullOrWhiteSpace($id) -or $recordsById.ContainsKey($id)) {
            Report 'FAIL' 'JSONL unique record ID' $id
        }
        else {
            $recordsById[$id] = $record
            $allRecords.Add($record)
        }

        $target = $record.target_locator
        if ($null -ne $target -and $null -ne $target.sha256) {
            if ([string] $target.sha256 -cnotmatch $schema.sha256_pattern) {
                Report 'FAIL' 'JSONL target SHA-256 syntax' $id
            }
            if ([int64] $target.bytes -lt 0) {
                Report 'FAIL' 'JSONL target byte count' $id
            }
            $artifact = Resolve-RecordedArtifact ([string] $target.relative_path)
            if ($null -ne $artifact) {
                if (-not (Test-Path -LiteralPath $artifact -PathType Leaf)) {
                    Report 'FAIL' 'JSONL target artifact exists' "$id :: $artifact"
                }
                else {
                    $actualBytes = (Get-Item -LiteralPath $artifact).Length
                    $actualHash = (Get-FileHash -LiteralPath $artifact -Algorithm SHA256).Hash
                    Report (($actualBytes -eq [int64] $target.bytes -and $actualHash -ceq [string] $target.sha256) ? 'PASS' : 'FAIL') 'JSONL target bytes/hash' "$id :: bytes=$actualBytes; sha256=$actualHash"
                }
            }
        }
        if ($null -ne $record.source_locator.slice_sha256 -and [string] $record.source_locator.slice_sha256 -cnotmatch $schema.sha256_pattern) {
            Report 'FAIL' 'JSONL source-slice SHA-256 syntax' $id
        }
        if ($record.schema_version -eq $schema.difficulty_schema_version -and $record.difficulty.automatic_effect -ne $false) {
            Report 'FAIL' 'Difficulty has no automatic decision effect' $id
        }
    }
    Report 'PASS' 'JSONL file parse count' "$(Split-Path $spec.Path -Leaf) :: records=$recordCount; bytes=$((Get-Item -LiteralPath $spec.Path).Length); sha256=$((Get-FileHash -LiteralPath $spec.Path -Algorithm SHA256).Hash)"
}

foreach ($record in $allRecords) {
    foreach ($field in @($schema.reference_fields)) {
        foreach ($reference in @(Get-ReferenceValues $record ([string] $field))) {
            if ([string]::IsNullOrWhiteSpace($reference)) { continue }
            if (-not $recordsById.ContainsKey($reference)) {
                Report 'FAIL' 'JSONL reference closure' "$($record.record_id).$field -> $reference"
            }
        }
    }
}

foreach ($record in $allRecords) {
    if ($null -ne $record.parent_id) {
        $parent = $recordsById[[string] $record.parent_id]
        if ($null -ne $parent -and [string] $record.record_id -notin @($parent.child_ids)) {
            Report 'FAIL' 'Parent/child reciprocity' "$($record.record_id) missing from $($parent.record_id).child_ids"
        }
    }
    foreach ($childId in @($record.child_ids)) {
        $child = $recordsById[[string] $childId]
        if ($null -ne $child -and [string] $child.parent_id -cne [string] $record.record_id) {
            Report 'FAIL' 'Child/parent reciprocity' "$($record.record_id) -> $childId"
        }
    }
    foreach ($oldId in @($record.supersedes_record_ids)) {
        $old = $recordsById[[string] $oldId]
        if ($null -ne $old -and [string] $old.superseded_by_record_id -cne [string] $record.record_id) {
            Report 'FAIL' 'Supersession reciprocity' "$($record.record_id) supersedes $oldId"
        }
    }
    if ([string] $record.status -ceq 'superseded') {
        if ([string]::IsNullOrWhiteSpace([string] $record.superseded_by_record_id)) {
            Report 'FAIL' 'Superseded status has successor' "$($record.record_id)"
        }
        else {
            $successor = $recordsById[[string] $record.superseded_by_record_id]
            if ($null -ne $successor -and [string] $record.record_id -notin @($successor.supersedes_record_ids)) {
                Report 'FAIL' 'Successor supersession reciprocity' "$($record.record_id) -> $($record.superseded_by_record_id)"
            }
        }
    }
    foreach ($closedId in @($record.closes_record_ids)) {
        $closed = $recordsById[[string] $closedId]
        if ($null -ne $closed -and [string] $closed.closed_by_record_id -cne [string] $record.record_id) {
            Report 'FAIL' 'Closure reciprocity' "$($record.record_id) closes $closedId"
        }
    }
    if (-not [string]::IsNullOrWhiteSpace([string] $record.closed_by_record_id)) {
        $closer = $recordsById[[string] $record.closed_by_record_id]
        if ($null -ne $closer -and [string] $record.record_id -notin @($closer.closes_record_ids)) {
            Report 'FAIL' 'Closer/closure reciprocity' "$($record.record_id) -> $($record.closed_by_record_id)"
        }
    }
}

Report 'PASS' 'JSONL unique IDs' "records=$($recordsById.Count)"
Report ($script:failures -eq 0 ? 'PASS' : 'FAIL') 'Machine-ledger validation total' "csv_rows=$csvTotalRows; jsonl_records=$($recordsById.Count); failures=$script:failures"
if ($script:failures -ne 0) { exit 1 }
