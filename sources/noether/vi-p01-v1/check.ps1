$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$target = Get-Content -LiteralPath (Join-Path $root 'p01.tex')
$sourcePath = 'C:\Users\Floris\Documents\interlanguage\03_projects\language_management\cjk\03_working_translations\noether_paper01_zh_translation_001_20260722\source\Noether_Paper01_CurrentGermanAuthority_interval.tex'
$source = Get-Content -LiteralPath $sourcePath
$utf8 = [System.Text.UTF8Encoding]::new($false)

function Get-LineHash([object[]]$lines, [string]$locator) {
    $a, $b = $locator.Split('-') | ForEach-Object { [int]$_ }
    $text = $lines[($a - 1)..($b - 1)] -join "`n"
    $sha = [System.Security.Cryptography.SHA256]::Create()
    ([BitConverter]::ToString($sha.ComputeHash($utf8.GetBytes($text)))).Replace('-', '')
}

$records = @(Get-Content -LiteralPath (Join-Path $root 'index.jsonl') | ForEach-Object { $_ | ConvertFrom-Json })
$required = @('id','type','parent_id','order','source_authority','source_relative_lines','source_authority_lines','source_sha256','target_path','target_lines','target_sha256','language','completion_state','review_state','publication_state','next_cursor')
$errors = [System.Collections.Generic.List[string]]::new()
$seen = @{}
foreach ($record in $records) {
    foreach ($field in $required) {
        if (-not $record.PSObject.Properties.Name.Contains($field)) { $errors.Add("$($record.id): missing $field") }
    }
    if ($seen.ContainsKey($record.id)) { $errors.Add("duplicate id $($record.id)") } else { $seen[$record.id] = $true }
    if ((Get-LineHash $source $record.source_relative_lines) -ne $record.source_sha256) { $errors.Add("$($record.id): source hash mismatch") }
    if ((Get-LineHash $target $record.target_lines) -ne $record.target_sha256) { $errors.Add("$($record.id): target hash mismatch") }
}
if ($errors.Count -gt 0) {
    $errors | ForEach-Object { Write-Error $_ }
    exit 1
}
Write-Output "PASS: $($records.Count) unique structural records; source and target locator hashes replay."
