[CmdletBinding()]
param()
$ErrorActionPreference = 'Stop'
$root = $PSScriptRoot
$pred = Join-Path $root 'evidence\predecessor_i9_2_r2_machine_controls'
$utf8 = [Text.UTF8Encoding]::new($false)
function Sha([string] $Path) { (Get-FileHash -LiteralPath $Path -Algorithm SHA256).Hash }
function Rel([string] $Root,[string] $Path) { $Path.Substring($Root.Length+1).Replace('\','/') }
function Digest([string] $Root) {
    $lines=@(Get-ChildItem -LiteralPath $Root -Recurse -File|Sort-Object FullName|ForEach-Object{"$(Rel $Root $_.FullName)|$($_.Length)|$(Sha $_.FullName)"})
    [BitConverter]::ToString([Security.Cryptography.SHA256]::HashData($utf8.GetBytes(($lines-join[string][char]10)+[string][char]10))).Replace('-','')
}
function Read-Jsonl([string] $Path) {
    @([IO.File]::ReadAllLines($Path,[Text.UTF8Encoding]::new($false,$true))|Where-Object{-not[string]::IsNullOrWhiteSpace($_)}|ForEach-Object{$_|ConvertFrom-Json -Depth 40})
}
function Ref($Record,[string] $Field) {
    $property=$Record.PSObject.Properties[$Field]
    if($null-eq$property-or$null-eq$property.Value){return @()}
    if($property.Value-is[string]){return @([string]$property.Value)}
    @($property.Value|ForEach-Object{[string]$_})
}
function Csv-Stats([IO.FileInfo[]] $Files) {
    Add-Type -AssemblyName Microsoft.VisualBasic
    $rows=0
    foreach($file in $Files){
        $parser=[Microsoft.VisualBasic.FileIO.TextFieldParser]::new($file.FullName,[Text.Encoding]::UTF8,$true)
        $parser.TextFieldType=[Microsoft.VisualBasic.FileIO.FieldType]::Delimited
        $parser.SetDelimiters(',')
        $parser.HasFieldsEnclosedInQuotes=$true
        $matrix=[Collections.Generic.List[object]]::new()
        try{while(-not$parser.EndOfData){$matrix.Add(@($parser.ReadFields()))}}finally{$parser.Close()}
        if($matrix.Count-lt1){throw "Empty CSV: $($file.FullName)"}
        $columns=@($matrix[0]).Count
        $ids=[Collections.Generic.HashSet[string]]::new([StringComparer]::Ordinal)
        for($index=1;$index-lt$matrix.Count;$index++){
            $row=@($matrix[$index])
            if($row.Count-ne$columns-or[string]::IsNullOrWhiteSpace([string]$row[0])-or-not$ids.Add([string]$row[0])){throw "CSV rectangular or ID failure: $($file.FullName)"}
            foreach($cell in $row){$value=([string]$cell).TrimStart();if($value-match'^[=+\-@]'){throw "CSV formula-safety failure: $($file.FullName)"}}
        }
        $rows+=$matrix.Count-1
    }
    $rows
}
$predFiles=@(Get-ChildItem -LiteralPath $pred -Recurse -File)
if($predFiles.Count-ne82-or[long]($predFiles|Measure-Object Length -Sum).Sum-ne772963-or(Digest $pred)-cne'90B466ECF7C1D834BD40E3539554683AD274BEDEA357F9F6C919388DF5E140A8'){throw 'Predecessor machine subtree identity failed'}
$predCsv=@(Get-ChildItem -LiteralPath $pred -Recurse -Filter '*.csv' -File)
$currentCsv=@(Get-ChildItem -LiteralPath (Join-Path $root 'ledgers') -Filter '*.csv' -File)
$predRows=Csv-Stats $predCsv
$currentRows=Csv-Stats $currentCsv
if($predCsv.Count-ne59-or$predRows-ne1187-or$currentCsv.Count-ne21-or$currentRows-ne447){throw 'Cumulative CSV count failed'}
$predJson=@(Get-ChildItem -LiteralPath $pred -Recurse -Filter '*.jsonl' -File)
$currentJson=@(Get-ChildItem -LiteralPath (Join-Path $root 'ledgers') -Filter '*.jsonl' -File)
$records=@()
foreach($file in @($predJson+$currentJson)){$records+=@(Read-Jsonl $file.FullName)}
if($predJson.Count-ne14-or$currentJson.Count-ne2-or$records.Count-ne195){throw 'Cumulative JSONL count failed'}
$byId=@{}
foreach($record in $records){$id=[string]$record.record_id;if([string]::IsNullOrWhiteSpace($id)-or$byId.ContainsKey($id)){throw "Duplicate or blank JSONL ID: $id"};$byId[$id]=$record}
foreach($record in $records){foreach($field in @('parent_id','child_ids','local_reference_ids','revision_record_id','supersedes_record_ids','superseded_by_record_id','closes_record_ids','closed_by_record_id','related_record_ids')){foreach($reference in @(Ref $record $field)){if(-not[string]::IsNullOrWhiteSpace($reference)-and$reference.StartsWith('SGA1-',[StringComparison]::Ordinal)-and-not$byId.ContainsKey($reference)){throw "Reference not closed: $($record.record_id).$field -> $reference"}}}}
Write-Output 'CUMULATIVE_MACHINE_EVIDENCE_VERIFY=PASS'
Write-Output 'PREDECESSOR_MACHINE_FILES=82'
Write-Output 'PREDECESSOR_MACHINE_BYTES=772963'
Write-Output 'PREDECESSOR_CSV_FILES=59'
Write-Output 'PREDECESSOR_CSV_ROWS=1187'
Write-Output 'CURRENT_I93_CSV_FILES=21'
Write-Output 'CURRENT_I93_CSV_ROWS=447'
Write-Output 'COMBINED_CSV_FILES=80'
Write-Output 'COMBINED_CSV_ROWS=1634'
Write-Output 'COMBINED_JSONL_FILES=16'
Write-Output 'COMBINED_JSONL_UNIQUE_RECORDS=195'
Write-Output 'COMBINED_JSONL_REFERENCE_CLOSURE=PASS'
Write-Output 'PREDECESSOR_TARGET_CLOSURE=verified_by_immutable_i9_2_r2_portable_verifier_and_github_readback'