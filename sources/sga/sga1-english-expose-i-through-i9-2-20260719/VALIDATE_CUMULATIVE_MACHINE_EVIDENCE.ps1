[CmdletBinding()]
param()
$ErrorActionPreference = 'Stop'
$root = $PSScriptRoot
$utf8 = [Text.UTF8Encoding]::new($false)
function Sha([string] $Path) { (Get-FileHash -LiteralPath $Path -Algorithm SHA256).Hash }
function Rel([string] $Root,[string] $Path) { $Path.Substring($Root.Length+1).Replace('\','/') }
function Identity-Digest([string[]] $RelativePaths) {
    $lines=@($RelativePaths|Sort-Object|ForEach-Object{$p=Join-Path $root $_.Replace('/','\');if(-not(Test-Path -LiteralPath $p -PathType Leaf)){throw "Identity input missing: $_"};"$_|$((Get-Item -LiteralPath $p).Length)|$(Sha $p)"})
    [BitConverter]::ToString([Security.Cryptography.SHA256]::HashData([Text.Encoding]::UTF8.GetBytes(($lines-join"`n")+"`n"))).Replace('-','')
}
function Digest([string[]] $Lines) { [BitConverter]::ToString([Security.Cryptography.SHA256]::HashData($utf8.GetBytes(($Lines -join "`n") + "`n"))).Replace('-','') }
function Refs($Record,[string]$Field) { $p=$Record.PSObject.Properties[$Field]; if($null -eq $p -or $null -eq $p.Value){return @()}; if($p.Value -is [string]){return @([string]$p.Value)}; @($p.Value|ForEach-Object{[string]$_}) }

$historical = Join-Path $root 'evidence\predecessor_i9_1_r2_machine_controls'
$historicalFiles = @(Get-ChildItem -LiteralPath $historical -Recurse -File -Force | Sort-Object FullName)
$historicalLines = @($historicalFiles | ForEach-Object { "$(Rel $historical $_.FullName)|$($_.Length)|$(Sha $_.FullName)" })
if ($historicalFiles.Count -ne 58 -or [long]($historicalFiles|Measure-Object Length -Sum).Sum -ne 555239 -or (Digest $historicalLines) -cne 'B2EF7C9AB4CF43EB47D5BDAA7E4DB12BA96417D6331070D4802406FE5EE1BA5E') { throw 'Historical I.9.1 cumulative machine custody mismatch' }

$historicalCsv = @(Get-ChildItem -LiteralPath $historical -Recurse -Filter '*.csv' -File -Force)
$historicalCsvRows = [long]($historicalCsv | ForEach-Object { @(Import-Csv -LiteralPath $_.FullName).Count } | Measure-Object -Sum).Sum
if ($historicalCsv.Count -ne 40 -or $historicalCsvRows -ne 782) { throw 'Historical CSV extent mismatch' }
$schema = [IO.File]::ReadAllText((Join-Path $root 'ledgers\SGA1_MACHINE_LEDGER_SCHEMA_v1.json'),[Text.UTF8Encoding]::new($false,$true)) | ConvertFrom-Json -Depth 40
$currentCsv = @($schema.csv_ledgers.PSObject.Properties | ForEach-Object { Get-Item -LiteralPath (Join-Path $root ([string]$_.Name).Replace('/','\')) })
$currentCsvRows = [long]($currentCsv | ForEach-Object { @(Import-Csv -LiteralPath $_.FullName).Count } | Measure-Object -Sum).Sum
if ($currentCsv.Count -ne 19 -or $currentCsvRows -ne 405) { throw 'Current CSV extent mismatch' }

$jsonFiles = @(
    @(Get-ChildItem -LiteralPath $historical -Recurse -Filter '*.jsonl' -File -Force) +
    @(Get-Item -LiteralPath (Join-Path $root 'ledgers\SGA1_I9_2_EVIDENCE_GRAPH.jsonl')) +
    @(Get-Item -LiteralPath (Join-Path $root 'ledgers\SGA1_DIFFICULTY_FAILURE_REVISION.jsonl'))
)
if ($jsonFiles.Count -ne 14) { throw 'Combined JSONL file count mismatch' }
$records=@()
foreach($file in $jsonFiles){ foreach($line in [IO.File]::ReadAllLines($file.FullName,[Text.UTF8Encoding]::new($false,$true))){ if(-not [string]::IsNullOrWhiteSpace($line)){ $records += ($line|ConvertFrom-Json -Depth 40) } } }
$byId=@{}
foreach($record in $records){$id=[string]$record.record_id;if([string]::IsNullOrWhiteSpace($id)-or $byId.ContainsKey($id)){throw "Combined duplicate/blank JSONL ID: $id"};$byId[$id]=$record}
if($records.Count -ne 180 -or $byId.Count -ne 180){throw 'Combined JSONL record total mismatch'}
$fields=@('parent_id','child_ids','local_reference_ids','revision_record_id','supersedes_record_ids','superseded_by_record_id','closes_record_ids','closed_by_record_id','related_record_ids')
foreach($record in $records){foreach($field in $fields){foreach($ref in @(Refs $record $field)){if(-not [string]::IsNullOrWhiteSpace($ref)-and $ref.StartsWith('SGA1-',[StringComparison]::Ordinal)-and -not $byId.ContainsKey($ref)){throw "Combined reference not closed: $($record.record_id).$field -> $ref"}}}}

Write-Output 'CUMULATIVE_MACHINE_EVIDENCE_VERIFY=PASS'
Write-Output 'PREDECESSOR_MACHINE_FILES=58'
Write-Output 'PREDECESSOR_MACHINE_BYTES=555239'
Write-Output 'CURRENT_I92_CSV_FILES=19'
Write-Output 'CURRENT_I92_CSV_ROWS=405'
Write-Output 'COMBINED_CSV_FILES=59'
Write-Output 'COMBINED_CSV_ROWS=1187'
Write-Output 'COMBINED_JSONL_FILES=14'
Write-Output 'COMBINED_JSONL_UNIQUE_RECORDS=180'
Write-Output 'COMBINED_JSONL_REFERENCE_CLOSURE=PASS'
Write-Output 'PREDECESSOR_TARGET_CLOSURE=historically_verified_in_immutable_i9_1_r2_not_rebased'