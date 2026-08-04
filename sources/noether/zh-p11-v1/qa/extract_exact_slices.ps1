$ErrorActionPreference = 'Stop'

$workspace = 'C:\Users\Floris\Documents\interlanguage\03_projects\language_management\cjk\03_working_translations\noether_paper11_zh_translation_001_20260722'
$authority = 'C:\Users\Floris\Documents\Codex\2026-06-01\we-are-currently-doing-a-massive\Noether_P07_CurrentHead_SourceAdjudication_20260722\1\01_current\Noether_P16_IndependentSecondPass_20260722_cum_de.tex'
$witness = 'C:\Users\Floris\Documents\interlanguage\03_projects\language_management\cjk\01_recovered_witnesses\noether_cjk_chinese_japanese_cumulative_20260702\translations\non_slavic\simplified_chinese\cumulative\source_fidelity\v001\Noether_SimplifiedChinese_Cumulative_SourceFidelity_v001.tex'

function Write-ExactLineSlice {
    param(
        [Parameter(Mandatory = $true)][string]$InputPath,
        [Parameter(Mandatory = $true)][int]$StartLine,
        [Parameter(Mandatory = $true)][int]$EndLine,
        [Parameter(Mandatory = $true)][string]$OutputPath
    )

    $bytes = [System.IO.File]::ReadAllBytes($InputPath)
    $lineStarts = [System.Collections.Generic.List[int]]::new()
    $lineStarts.Add(0)
    for ($index = 0; $index -lt $bytes.Length; $index++) {
        if ($bytes[$index] -eq 10) { $lineStarts.Add($index + 1) }
    }
    if ($StartLine -lt 1 -or $EndLine -lt $StartLine -or $EndLine -gt $lineStarts.Count) {
        throw "Invalid interval $StartLine--$EndLine for ${InputPath}"
    }
    $byteStart = $lineStarts[$StartLine - 1]
    $byteEnd = if ($EndLine -lt $lineStarts.Count) { $lineStarts[$EndLine] } else { $bytes.Length }
    $slice = [byte[]]::new($byteEnd - $byteStart)
    [Array]::Copy($bytes, $byteStart, $slice, 0, $slice.Length)
    [System.IO.File]::WriteAllBytes($OutputPath, $slice)
    $sha = [System.Security.Cryptography.SHA256]::Create()
    [pscustomobject]@{Output=$OutputPath;Lines="$StartLine--$EndLine";ByteStart=$byteStart;ByteEnd=$byteEnd;Bytes=$slice.Length;SHA256=[Convert]::ToHexString($sha.ComputeHash($slice))}
}

$results = @()
$results += Write-ExactLineSlice $authority 7865 8070 "$workspace\source\P11_CurrentGerman_lines7865_8070.tex"
$results += Write-ExactLineSlice $authority 7865 7938 "$workspace\segments\source\P11_A_lines7865_7938.tex"
$results += Write-ExactLineSlice $authority 7939 8001 "$workspace\segments\source\P11_B_lines7939_8001.tex"
$results += Write-ExactLineSlice $authority 8002 8070 "$workspace\segments\source\P11_C_lines8002_8070.tex"

$results += Write-ExactLineSlice $witness 7718 8007 "$workspace\witness\P11_InheritedHans_content_lines7718_8007.tex"
$results += Write-ExactLineSlice $witness 7718 7822 "$workspace\segments\witness\P11_A_witness_lines7718_7822.tex"
$results += Write-ExactLineSlice $witness 7823 7912 "$workspace\segments\witness\P11_B_witness_lines7823_7912.tex"
$results += Write-ExactLineSlice $witness 7913 8007 "$workspace\segments\witness\P11_C_witness_lines7913_8007.tex"

$results | Format-Table -AutoSize
