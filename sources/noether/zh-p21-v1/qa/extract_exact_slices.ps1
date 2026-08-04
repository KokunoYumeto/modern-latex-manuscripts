$ErrorActionPreference = 'Stop'
$workspace = 'C:\Users\Floris\Documents\interlanguage\03_projects\language_management\cjk\03_working_translations\noether_paper21_zh_translation_001_20260722'
$german = 'C:\Users\Floris\Documents\Codex\2026-06-01\we-are-currently-doing-a-massive\Noether_P07_CurrentHead_SourceAdjudication_20260722\1\01_current\Noether_P16_IndependentSecondPass_20260722_cum_de.tex'
$witness = 'C:\Users\Floris\Documents\interlanguage\03_projects\language_management\cjk\01_recovered_witnesses\noether_cjk_chinese_japanese_cumulative_20260702\translations\non_slavic\simplified_chinese\cumulative\source_fidelity\v001\Noether_SimplifiedChinese_Cumulative_SourceFidelity_v001.tex'

function Write-Slice([string]$inputPath, [int]$startLine, [int]$nextLine, [string]$relativeOutput, [string]$expected = '') {
    $bytes = [System.IO.File]::ReadAllBytes($inputPath)
    $starts = [System.Collections.Generic.List[int]]::new()
    $starts.Add(0)
    for ($index = 0; $index -lt $bytes.Length; $index++) { if ($bytes[$index] -eq 10) { $starts.Add($index + 1) } }
    $start = $starts[$startLine - 1]
    $end = $starts[$nextLine - 1]
    $slice = [byte[]]::new($end - $start)
    [System.Array]::Copy($bytes, $start, $slice, 0, $slice.Length)
    $output = Join-Path $workspace $relativeOutput
    [System.IO.File]::WriteAllBytes($output, $slice)
    $hash = (Get-FileHash -Algorithm SHA256 -LiteralPath $output).Hash
    if ($expected -and $hash -ne $expected) { throw "Hash mismatch for ${output}: expected $expected, got $hash" }
    [pscustomobject]@{ path = $relativeOutput; lines = "$startLine-$($nextLine - 1)"; bytes = $slice.Length; sha256 = $hash }
}

@(
    Write-Slice $german 12589 12681 'source\Noether_Paper21_German_current_exact_CRLF.tex' 'C91672CA4BB8EFEB092EDD278A4F97B6E3E94AE2059144F4FFDDA524AAF7FB96'
    Write-Slice $witness 13388 13496 'witness\Noether_Paper21_SimplifiedChinese_inherited_content_exact_CRLF.tex' '75DB55DDA93F5C68C833D77C890DA0CAC6E7B22CB0769021799B5CAD335EAE41'
    Write-Slice $german 12589 12646 'segments\source\P21_A_lines12589_12645.tex' 'B6653D3F08C26A60A258BD31C21E8CC7334211D2AA20C2289272BFE49C61ED8F'
    Write-Slice $german 12646 12668 'segments\source\P21_B_lines12646_12667.tex' '2CC054EA3471A2CA1755BF04B23C2451F708040B9A8F60B3F3B4753E445E26AA'
    Write-Slice $german 12668 12681 'segments\source\P21_C_lines12668_12680.tex' 'CA8F97A2850467896E6ECC5717605B43E22C993B2D6BDB0BD863E915A7CF27FC'
    Write-Slice $witness 13388 13452 'segments\witness\P21_A_lines13388_13451.tex' 'C79F6D540EE5274545D580BC4426E18EAE8AFAF2877B26F65B34CDFB4A493D3B'
    Write-Slice $witness 13452 13484 'segments\witness\P21_B_lines13452_13483.tex' '3D96BDEB519CCEBBED2783C96A785A8095FEDF02322FB306C2979A9A91DE9FB3'
    Write-Slice $witness 13484 13496 'segments\witness\P21_C_lines13484_13495.tex' 'AE26DFF8AC4FAFCBD7DCADA7C6A6FDDA559E9ADBFC3163A54916559A0D350137'
) | Format-Table -AutoSize
