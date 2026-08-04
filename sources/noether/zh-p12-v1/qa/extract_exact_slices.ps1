$ErrorActionPreference = 'Stop'

$workspace = 'C:\Users\Floris\Documents\interlanguage\03_projects\language_management\cjk\03_working_translations\noether_paper12_zh_translation_001_20260722'
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
        if ($bytes[$index] -eq 10) {
            $lineStarts.Add($index + 1)
        }
    }

    if ($StartLine -lt 1 -or $EndLine -lt $StartLine -or $EndLine -gt $lineStarts.Count) {
        throw "Invalid line interval $StartLine--$EndLine for ${InputPath}"
    }

    $byteStart = $lineStarts[$StartLine - 1]
    $byteEnd = if ($EndLine -lt $lineStarts.Count) { $lineStarts[$EndLine] } else { $bytes.Length }
    $length = $byteEnd - $byteStart
    $slice = [byte[]]::new($length)
    [Array]::Copy($bytes, $byteStart, $slice, 0, $length)
    [System.IO.File]::WriteAllBytes($OutputPath, $slice)

    $sha = [System.Security.Cryptography.SHA256]::Create()
    [pscustomobject]@{
        Output = $OutputPath
        Lines = "$StartLine--$EndLine"
        ByteStart = $byteStart
        ByteEnd = $byteEnd
        Bytes = $length
        SHA256 = [Convert]::ToHexString($sha.ComputeHash($slice))
    }
}

$results = @()
$results += Write-ExactLineSlice $authority 8071 8471 "$workspace\source\P12_CurrentGerman_lines8071_8471.tex"
$results += Write-ExactLineSlice $authority 8071 8172 "$workspace\segments\source\P12_A_lines8071_8172.tex"
$results += Write-ExactLineSlice $authority 8173 8317 "$workspace\segments\source\P12_B_lines8173_8317.tex"
$results += Write-ExactLineSlice $authority 8318 8471 "$workspace\segments\source\P12_C_lines8318_8471.tex"

$results += Write-ExactLineSlice $witness 8012 8286 "$workspace\witness\P12_InheritedHans_content_lines8012_8286.tex"
$results += Write-ExactLineSlice $witness 8012 8071 "$workspace\segments\witness\P12_A_witness_lines8012_8071.tex"
$results += Write-ExactLineSlice $witness 8072 8190 "$workspace\segments\witness\P12_B_witness_lines8072_8190.tex"
$results += Write-ExactLineSlice $witness 8191 8286 "$workspace\segments\witness\P12_C_witness_lines8191_8286.tex"

$results | Format-Table -AutoSize
