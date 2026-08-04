$ErrorActionPreference = 'Stop'

$workspace = 'C:\Users\Floris\Documents\interlanguage\03_projects\language_management\cjk\03_working_translations\noether_paper07_zh_translation_001_20260722'
$inputs = @(
    (Join-Path $workspace 'segments\P07_STANDALONE_PREAMBLE.tex'),
    (Join-Path $workspace 'segments\zh-Hans-CN\P07_A_zh-Hans-CN.tex'),
    (Join-Path $workspace 'segments\zh-Hans-CN\P07_B_zh-Hans-CN.tex'),
    (Join-Path $workspace 'segments\zh-Hans-CN\P07_C_zh-Hans-CN.tex'),
    (Join-Path $workspace 'segments\P07_STANDALONE_POSTAMBLE.tex')
)
$output = Join-Path $workspace 'zh-Hans-CN\Noether_Paper07_Chinese_CurrentAuthority_zh-Hans-CN_v001.tex'
$utf8 = [System.Text.UTF8Encoding]::new($false)

$parts = foreach ($input in $inputs) {
    [System.IO.File]::ReadAllText($input, $utf8)
}
[System.IO.File]::WriteAllText($output, ($parts -join ''), $utf8)

function File-Metadata([string]$path) {
    $file = Get-Item -LiteralPath $path
    $hash = (Get-FileHash -Algorithm SHA256 -LiteralPath $path).Hash
    [ordered]@{
        path = $path.Substring($workspace.Length + 1).Replace('\', '/')
        bytes = $file.Length
        sha256 = $hash
    }
}

$record = [ordered]@{
    record_type = 'producer_hans_assembly'
    work_unit = 'Noether Paper 7'
    source_authority_sha256 = 'F6C923B79406542E3DE64298DCD38887FF9A52141C71B8FF2BEBE6D14625FAEA'
    inputs = @($inputs | ForEach-Object { File-Metadata $_ })
    output = File-Metadata $output
    translation_segments_in_source_order = @('A', 'B', 'C')
    producer_term_convergence = [ordered]@{
        initial_segment_a_sha256 = '56E8CB894EB8014282FF4C1CC730CC6045D02F7552643C4DDF18DF9948182B97'
        final_segment_a_sha256 = 'FF6CBF848BEE518A5E7EF4AD51C34A75A3CB53C339C71C7D562A2BFC86CF5C71'
        changed_only = '单型 -> 单式 for einförmig, to match segment B; checker review remains pending'
    }
    source_check_performed = $false
    translation_check_performed = $false
    visual_check_performed = $false
    independent_check = 'pending'
}

$recordPath = Join-Path $workspace 'qa\HANS_ASSEMBLY_RECORD.json'
[System.IO.File]::WriteAllText($recordPath, ($record | ConvertTo-Json -Depth 8), $utf8)

$record.output | ConvertTo-Json -Compress
