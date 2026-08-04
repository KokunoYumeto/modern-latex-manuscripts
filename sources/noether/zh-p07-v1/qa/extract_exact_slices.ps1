$ErrorActionPreference = 'Stop'

$workspace = 'C:\Users\Floris\Documents\interlanguage\03_projects\language_management\cjk\03_working_translations\noether_paper07_zh_translation_001_20260722'
$german = 'C:\Users\Floris\Documents\Codex\2026-06-01\we-are-currently-doing-a-massive\Noether_P07_CurrentHead_SourceAdjudication_20260722\1\01_current\Noether_P16_IndependentSecondPass_20260722_cum_de.tex'
$witness = 'C:\Users\Floris\Documents\interlanguage\03_projects\language_management\cjk\01_recovered_witnesses\noether_cjk_chinese_japanese_cumulative_20260702\translations\non_slavic\simplified_chinese\cumulative\source_fidelity\v001\Noether_SimplifiedChinese_Cumulative_SourceFidelity_v001.tex'

function Write-ExactLineSlice {
    param(
        [Parameter(Mandatory = $true)][string]$InputPath,
        [Parameter(Mandatory = $true)][int]$StartLine,
        [Parameter(Mandatory = $true)][int]$NextLine,
        [Parameter(Mandatory = $true)][string]$OutputPath,
        [string]$ExpectedSha256 = ''
    )

    $bytes = [System.IO.File]::ReadAllBytes($InputPath)
    $starts = [System.Collections.Generic.List[int]]::new()
    $starts.Add(0)
    for ($index = 0; $index -lt $bytes.Length; $index++) {
        if ($bytes[$index] -eq 10) {
            $starts.Add($index + 1)
        }
    }

    $start = $starts[$StartLine - 1]
    $end = $starts[$NextLine - 1]
    $slice = [byte[]]::new($end - $start)
    [System.Array]::Copy($bytes, $start, $slice, 0, $slice.Length)
    [System.IO.File]::WriteAllBytes($OutputPath, $slice)

    $hasher = [System.Security.Cryptography.SHA256]::Create()
    try {
        $hash = [System.BitConverter]::ToString($hasher.ComputeHash($slice)).Replace('-', '')
    }
    finally {
        $hasher.Dispose()
    }

    if ($ExpectedSha256 -and $hash -ne $ExpectedSha256) {
        throw "Hash mismatch for ${OutputPath}: expected $ExpectedSha256, got $hash"
    }

    [pscustomobject]@{
        output = $OutputPath
        lines = "$StartLine-$($NextLine - 1)"
        bytes = $slice.Length
        sha256 = $hash
    }
}

$results = @(
    Write-ExactLineSlice -InputPath $german -StartLine 5819 -NextLine 5928 -OutputPath (Join-Path $workspace 'source\Noether_Paper07_German_current_exact_CRLF.tex') -ExpectedSha256 'F6C923B79406542E3DE64298DCD38887FF9A52141C71B8FF2BEBE6D14625FAEA'
    Write-ExactLineSlice -InputPath $witness -StartLine 6262 -NextLine 6396 -OutputPath (Join-Path $workspace 'witness\Noether_Paper07_SimplifiedChinese_inherited_exact_CRLF.tex') -ExpectedSha256 'BB4686153D7241CD0F8A74164B6486C31C3BF731722334CC25B5E81AA8884AF8'
    Write-ExactLineSlice -InputPath $german -StartLine 5819 -NextLine 5863 -OutputPath (Join-Path $workspace 'segments\source\P07_A_lines5819_5862.tex')
    Write-ExactLineSlice -InputPath $german -StartLine 5863 -NextLine 5907 -OutputPath (Join-Path $workspace 'segments\source\P07_B_lines5863_5906.tex')
    Write-ExactLineSlice -InputPath $german -StartLine 5907 -NextLine 5928 -OutputPath (Join-Path $workspace 'segments\source\P07_C_lines5907_5927.tex')
    Write-ExactLineSlice -InputPath $witness -StartLine 6262 -NextLine 6311 -OutputPath (Join-Path $workspace 'segments\witness\P07_A_lines6262_6310.tex')
    Write-ExactLineSlice -InputPath $witness -StartLine 6311 -NextLine 6367 -OutputPath (Join-Path $workspace 'segments\witness\P07_B_lines6311_6366.tex')
    Write-ExactLineSlice -InputPath $witness -StartLine 6367 -NextLine 6396 -OutputPath (Join-Path $workspace 'segments\witness\P07_C_lines6367_6395.tex')
)

$results | Format-Table -AutoSize
