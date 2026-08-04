$ErrorActionPreference = 'Stop'

$workspace = 'C:\Users\Floris\Documents\interlanguage\03_projects\language_management\cjk\03_working_translations\noether_paper20_zh_translation_001_20260722'
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
$results += Write-ExactLineSlice $authority 12377 12588 "$workspace\source\P20_CurrentGerman_lines12377_12588.tex"
$results += Write-ExactLineSlice $authority 12377 12437 "$workspace\segments\source\P20_A_lines12377_12437.tex"
$results += Write-ExactLineSlice $authority 12438 12519 "$workspace\segments\source\P20_B_lines12438_12519.tex"
$results += Write-ExactLineSlice $authority 12520 12588 "$workspace\segments\source\P20_C_lines12520_12588.tex"

$results += Write-ExactLineSlice $witness 13142 13378 "$workspace\witness\P20_InheritedHans_content_lines13142_13378.tex"
$results += Write-ExactLineSlice $witness 13142 13213 "$workspace\segments\witness\P20_A_witness_lines13142_13213.tex"
$results += Write-ExactLineSlice $witness 13214 13306 "$workspace\segments\witness\P20_B_witness_lines13214_13306.tex"
$results += Write-ExactLineSlice $witness 13307 13378 "$workspace\segments\witness\P20_C_witness_lines13307_13378.tex"

$results | Format-Table -AutoSize
