$ErrorActionPreference = 'Stop'
$workspace = 'C:\Users\Floris\Documents\interlanguage\03_projects\language_management\cjk\03_working_translations\noether_paper11_zh_translation_001_20260722'
$inputs = @(
    (Join-Path $workspace 'segments\P11_STANDALONE_PREAMBLE.tex'),
    (Join-Path $workspace 'segments\zh-Hans-CN\P11_A_zh-Hans-CN.tex'),
    (Join-Path $workspace 'segments\zh-Hans-CN\P11_B_zh-Hans-CN.tex'),
    (Join-Path $workspace 'segments\zh-Hans-CN\P11_C_zh-Hans-CN.tex'),
    (Join-Path $workspace 'segments\P11_STANDALONE_POSTAMBLE.tex')
)
$output = Join-Path $workspace 'zh-Hans-CN\Noether_Paper11_Chinese_CurrentAuthority_zh-Hans-CN_v001.tex'
$utf8 = [System.Text.UTF8Encoding]::new($false)
foreach ($path in $inputs) { if (-not (Test-Path -LiteralPath $path)) { throw "Missing assembly input: $path" } }
[System.IO.File]::WriteAllText($output, (($inputs | ForEach-Object {[System.IO.File]::ReadAllText($_,$utf8)}) -join ''), $utf8)
function Meta([string]$path) { $f=Get-Item -LiteralPath $path; [ordered]@{path=$path.Substring($workspace.Length+1).Replace('\','/');bytes=$f.Length;sha256=(Get-FileHash -Algorithm SHA256 -LiteralPath $path).Hash} }
$record=[ordered]@{
  record_type='producer_hans_assembly';work_unit='Noether Paper 11';recorded_local_time=(Get-Date -Format 'yyyy-MM-dd HH:mm:ss zzz');
  source_authority_sha256='DE540AFFE512CF39871019A946F7CEBA9FFF04ADFB54FA1D531E5A40ADA5CBA1';
  inherited_hans_witness_sha256='D0737F8288235A705A1E2371BCD9F535CB5375212BBEC983324B7077014A23DD';
  inputs=@($inputs|ForEach-Object {Meta $_});output=Meta $output;
  source_check_performed=$false;semantic_or_formula_check_performed=$false;terminology_check_performed=$false;translation_quality_check_performed=$false;visual_check_performed=$false;independent_check='pending'
}
[System.IO.File]::WriteAllText((Join-Path $workspace 'qa\HANS_ASSEMBLY_RECORD.json'),($record|ConvertTo-Json -Depth 8),$utf8)
$record.output|ConvertTo-Json -Compress
