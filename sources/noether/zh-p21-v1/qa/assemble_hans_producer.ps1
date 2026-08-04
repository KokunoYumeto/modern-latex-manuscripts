$ErrorActionPreference = 'Stop'
$workspace = 'C:\Users\Floris\Documents\interlanguage\03_projects\language_management\cjk\03_working_translations\noether_paper21_zh_translation_001_20260722'
$inputs = @(
    (Join-Path $workspace 'segments\P21_STANDALONE_PREAMBLE.tex'),
    (Join-Path $workspace 'segments\zh-Hans-CN\P21_A_zh-Hans-CN.tex'),
    (Join-Path $workspace 'segments\zh-Hans-CN\P21_B_zh-Hans-CN.tex'),
    (Join-Path $workspace 'segments\zh-Hans-CN\P21_C_zh-Hans-CN.tex'),
    (Join-Path $workspace 'segments\P21_STANDALONE_POSTAMBLE.tex')
)
$output = Join-Path $workspace 'zh-Hans-CN\Noether_Paper21_Chinese_CurrentAuthority_zh-Hans-CN_v001.tex'
$utf8 = [System.Text.UTF8Encoding]::new($false)
[System.IO.File]::WriteAllText($output, (($inputs | ForEach-Object { [System.IO.File]::ReadAllText($_, $utf8) }) -join ''), $utf8)

function Meta([string]$path) {
    $file = Get-Item -LiteralPath $path
    [ordered]@{path=$path.Substring($workspace.Length+1).Replace('\','/');bytes=$file.Length;sha256=(Get-FileHash -Algorithm SHA256 -LiteralPath $path).Hash}
}
$record = [ordered]@{
    record_type='producer_hans_assembly'
    work_unit='Noether Paper 21'
    source_authority_sha256='C91672CA4BB8EFEB092EDD278A4F97B6E3E94AE2059144F4FFDDA524AAF7FB96'
    inputs=@($inputs|ForEach-Object {Meta $_})
    output=Meta $output
    producer_term_convergence=[ordered]@{
        initial_segment_b_sha256='DE08C37CA9387CD07F43710DED1446F38768ADB640EE3F6F0F28ABFDE79E3679'
        final_segment_b_sha256='5507F296C4AE65C5CDCF7CB452B08A5E015579A0FC506B09AF33A99E23F55383'
        changed_only='组量 -> 变量组 for Reihen; independent terminology check pending'
    }
    source_check_performed=$false
    translation_check_performed=$false
    visual_check_performed=$false
    independent_check='pending'
}
[System.IO.File]::WriteAllText((Join-Path $workspace 'qa\HANS_ASSEMBLY_RECORD.json'), ($record|ConvertTo-Json -Depth 8), $utf8)
$record.output|ConvertTo-Json -Compress
