$ErrorActionPreference = 'Stop'
$workspace = 'C:\Users\Floris\Documents\interlanguage\03_projects\language_management\cjk\03_working_translations\noether_paper10_zh_translation_001_20260722'
$authority = 'C:\Users\Floris\Documents\Codex\2026-06-01\we-are-currently-doing-a-massive\Noether_P07_CurrentHead_SourceAdjudication_20260722\1\01_current\Noether_P16_IndependentSecondPass_20260722_cum_de.tex'
$witness = 'C:\Users\Floris\Documents\interlanguage\03_projects\language_management\cjk\01_recovered_witnesses\noether_cjk_chinese_japanese_cumulative_20260702\translations\non_slavic\simplified_chinese\cumulative\source_fidelity\v001\Noether_SimplifiedChinese_Cumulative_SourceFidelity_v001.tex'

function Write-ExactLineSlice {
    param([string]$InputPath,[int]$StartLine,[int]$EndLine,[string]$OutputPath)
    $bytes=[IO.File]::ReadAllBytes($InputPath)
    $lineStarts=[Collections.Generic.List[int]]::new();$lineStarts.Add(0)
    for($index=0;$index-lt$bytes.Length;$index++){if($bytes[$index]-eq10){$lineStarts.Add($index+1)}}
    if($StartLine-lt1-or$EndLine-lt$StartLine-or$EndLine-gt$lineStarts.Count){throw "Invalid interval $StartLine--$EndLine for ${InputPath}"}
    $byteStart=$lineStarts[$StartLine-1]
    $byteEnd=if($EndLine-lt$lineStarts.Count){$lineStarts[$EndLine]}else{$bytes.Length}
    $slice=[byte[]]::new($byteEnd-$byteStart);[Array]::Copy($bytes,$byteStart,$slice,0,$slice.Length)
    [IO.File]::WriteAllBytes($OutputPath,$slice)
    [pscustomobject]@{Output=$OutputPath;Lines="$StartLine--$EndLine";ByteStart=$byteStart;ByteEnd=$byteEnd;Bytes=$slice.Length;SHA256=[Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($slice))}
}

$results=@()
$results+=Write-ExactLineSlice $authority 7664 7864 "$workspace\source\P10_CurrentGerman_lines7664_7864.tex"
$results+=Write-ExactLineSlice $authority 7664 7710 "$workspace\segments\source\P10_A_lines7664_7710.tex"
$results+=Write-ExactLineSlice $authority 7711 7767 "$workspace\segments\source\P10_B_lines7711_7767.tex"
$results+=Write-ExactLineSlice $authority 7768 7864 "$workspace\segments\source\P10_C_lines7768_7864.tex"
$results+=Write-ExactLineSlice $witness 7467 7714 "$workspace\witness\P10_InheritedHans_content_lines7467_7714.tex"
$results+=Write-ExactLineSlice $witness 7467 7523 "$workspace\segments\witness\P10_A_witness_lines7467_7523.tex"
$results+=Write-ExactLineSlice $witness 7524 7597 "$workspace\segments\witness\P10_B_witness_lines7524_7597.tex"
$results+=Write-ExactLineSlice $witness 7598 7714 "$workspace\segments\witness\P10_C_witness_lines7598_7714.tex"
$results|Format-Table -AutoSize
