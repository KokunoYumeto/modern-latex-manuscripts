$ErrorActionPreference = 'Stop'

$workspace = 'C:\Users\Floris\Documents\interlanguage\03_projects\language_management\cjk\03_working_translations\noether_paper12_zh_translation_001_20260722'
$inputs = @(
    (Join-Path $workspace 'segments\P12_STANDALONE_PREAMBLE.tex'),
    (Join-Path $workspace 'segments\zh-Hans-CN\P12_A_zh-Hans-CN.tex'),
    (Join-Path $workspace 'segments\zh-Hans-CN\P12_B_zh-Hans-CN.tex'),
    (Join-Path $workspace 'segments\zh-Hans-CN\P12_C_zh-Hans-CN.tex'),
    (Join-Path $workspace 'segments\P12_STANDALONE_POSTAMBLE.tex')
)
$output = Join-Path $workspace 'zh-Hans-CN\Noether_Paper12_Chinese_CurrentAuthority_zh-Hans-CN_v001.tex'
$utf8 = [System.Text.UTF8Encoding]::new($false)

foreach ($inputPath in $inputs) {
    if (-not (Test-Path -LiteralPath $inputPath)) {
        throw "Missing assembly input: $inputPath"
    }
}

$content = ($inputs | ForEach-Object { [System.IO.File]::ReadAllText($_, $utf8) }) -join ''
[System.IO.File]::WriteAllText($output, $content, $utf8)

function Get-Meta([string]$path) {
    $file = Get-Item -LiteralPath $path
    [ordered]@{
        path = $path.Substring($workspace.Length + 1).Replace('\', '/')
        bytes = $file.Length
        sha256 = (Get-FileHash -Algorithm SHA256 -LiteralPath $path).Hash
    }
}

$record = [ordered]@{
    record_type = 'producer_hans_assembly'
    work_unit = 'Noether Paper 12'
    recorded_local_time = (Get-Date -Format 'yyyy-MM-dd HH:mm:ss zzz')
    source_authority_sha256 = 'CD538526814F2E5812FE1D8C03ACF2BBDB0FED7F45ECC7DE5802394B07E05652'
    inherited_hans_witness_sha256 = 'F608A96A0F968F0091E286FE61666AF93B9B9CA40F34990336B67F8E435D99CE'
    inputs = @($inputs | ForEach-Object { Get-Meta $_ })
    output = Get-Meta $output
    source_check_performed = $false
    semantic_or_formula_check_performed = $false
    terminology_check_performed = $false
    translation_quality_check_performed = $false
    visual_check_performed = $false
    independent_check = 'pending'
}

[System.IO.File]::WriteAllText(
    (Join-Path $workspace 'qa\HANS_ASSEMBLY_RECORD.json'),
    ($record | ConvertTo-Json -Depth 8),
    $utf8
)
$record.output | ConvertTo-Json -Compress

