$ErrorActionPreference = 'Stop'

$Base = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$Sealed = 'evidence://local-workspace/Codex\2026-06-01\we-are-currently-doing-a-massive\Noether_LocalCodex_20260718_P31_FullPaperCanonicalReaudit_WEB_DROP\1\01_current\cum_de_Local_20260718_P31.tex'
$Witness = 'evidence://local-workspace/interlanguage\03_projects\language_management\cjk\01_recovered_witnesses\noether_cjk_chinese_japanese_cumulative_20260702\translations\non_slavic\simplified_chinese\cumulative\source_fidelity\v001\Noether_SimplifiedChinese_Cumulative_SourceFidelity_v001.tex'
$Utf8 = [Text.UTF8Encoding]::new($false)

function Get-Sha256Hex([byte[]]$Bytes) {
    return [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($Bytes))
}

function Get-ByteOffset([string]$Text, [int]$CharOffset) {
    return $Utf8.GetByteCount($Text.Substring(0, $CharOffset))
}

function Write-TextSlice {
    param(
        [string]$Label,
        [string]$InputPath,
        [string]$Text,
        [int]$StartChar,
        [int]$EndChar,
        [string]$OutputPath
    )
    $SliceText = $Text.Substring($StartChar, $EndChar - $StartChar)
    $SliceBytes = $Utf8.GetBytes($SliceText)
    [IO.File]::WriteAllBytes($OutputPath, $SliceBytes)
    $StartByte = Get-ByteOffset $Text $StartChar
    return [ordered]@{
        label = $Label
        input_path = $InputPath
        output_path = $OutputPath
        start_byte = $StartByte
        end_byte = $StartByte + $SliceBytes.Length
        byte_count = $SliceBytes.Length
        lf_delimiters = ([regex]::Matches($SliceText, "`n")).Count
        sha256 = Get-Sha256Hex $SliceBytes
    }
}

function Write-LfCopy {
    param(
        [string]$Label,
        [string]$InputPath,
        [string]$OutputPath
    )
    $Text = [IO.File]::ReadAllText($InputPath, $Utf8).Replace("`r`n", "`n")
    $Bytes = $Utf8.GetBytes($Text)
    [IO.File]::WriteAllBytes($OutputPath, $Bytes)
    return [ordered]@{
        label = $Label
        input_path = $InputPath
        output_path = $OutputPath
        byte_count = $Bytes.Length
        lf_delimiters = ([regex]::Matches($Text, "`n")).Count
        sha256 = Get-Sha256Hex $Bytes
    }
}

$SourceText = [IO.File]::ReadAllText($Sealed, $Utf8)
$SourceStart = $SourceText.IndexOf('\section*{37. Normalbasis', [StringComparison]::Ordinal)
$SourceNext = $SourceText.IndexOf('\section*{38.', $SourceStart, [StringComparison]::Ordinal)
if ($SourceStart -lt 0 -or $SourceNext -lt 0) { throw 'Paper 37 source markers not found.' }
$SourceInterval = $SourceText.Substring($SourceStart, $SourceNext - $SourceStart)
$TailClearRelative = $SourceInterval.LastIndexOf('\clearpage', [StringComparison]::Ordinal)
if ($TailClearRelative -lt 0) { throw 'Paper 37 carried Paper 38 clearpage marker not found.' }
$SourceLogicalEnd = $SourceStart + $TailClearRelative

$WitnessText = [IO.File]::ReadAllText($Witness, $Utf8)
$WitnessBeginMarker = '% BEGIN live source-fidelity unit: translations/non_slavic/simplified_chinese/paper37/source_fidelity/v001/Noether_Paper37_SourceFidelity_SimplifiedChinese_v001.tex'
$WitnessEndMarker = '% END live source-fidelity unit: translations/non_slavic/simplified_chinese/paper37/source_fidelity/v001/Noether_Paper37_SourceFidelity_SimplifiedChinese_v001.tex'
$WitnessBegin = $WitnessText.IndexOf($WitnessBeginMarker, [StringComparison]::Ordinal)
$WitnessEndMarkerStart = $WitnessText.IndexOf($WitnessEndMarker, $WitnessBegin, [StringComparison]::Ordinal)
$WitnessEndLineBreak = $WitnessText.IndexOf("`n", $WitnessEndMarkerStart, [StringComparison]::Ordinal)
$WitnessSection = $WitnessText.IndexOf('\section*{37.', $WitnessBegin, [StringComparison]::Ordinal)
if ($WitnessBegin -lt 0 -or $WitnessEndMarkerStart -lt 0 -or $WitnessEndLineBreak -lt 0 -or $WitnessSection -lt 0) { throw 'Paper 37 witness markers not found.' }
$WitnessEndAfterLine = $WitnessEndLineBreak + 1

$Records = [System.Collections.Generic.List[object]]::new()
$SourceIntervalPath = Join-Path $Base 'source\Noether_Paper37_German_P31_section_interval_exact_CRLF.tex'
$SourceLogicalPath = Join-Path $Base 'source\Noether_Paper37_German_P31_logical_article_exact_CRLF.tex'
$SourceLogicalLfPath = Join-Path $Base 'source\Noether_Paper37_German_P31_logical_article_LF.tex'
$WitnessBlockPath = Join-Path $Base 'witness\Noether_Paper37_SimplifiedChinese_Inherited_declared_block_exact_CRLF.tex'
$WitnessPreEndPath = Join-Path $Base 'witness\Noether_Paper37_SimplifiedChinese_BEGIN_to_before_END_exact_CRLF.tex'
$WitnessLogicalPath = Join-Path $Base 'witness\Noether_Paper37_SimplifiedChinese_Inherited_logical_article_exact_CRLF.tex'
$WitnessLogicalLfPath = Join-Path $Base 'witness\Noether_Paper37_SimplifiedChinese_Inherited_logical_article_LF.tex'

$Records.Add((Write-TextSlice 'sealed_p31_section_interval' $Sealed $SourceText $SourceStart $SourceNext $SourceIntervalPath))
$Records.Add((Write-TextSlice 'sealed_p31_logical_article' $Sealed $SourceText $SourceStart $SourceLogicalEnd $SourceLogicalPath))
$Records.Add((Write-LfCopy 'sealed_p31_logical_article_lf' $SourceLogicalPath $SourceLogicalLfPath))
$Records.Add((Write-TextSlice 'inherited_declared_block' $Witness $WitnessText $WitnessBegin $WitnessEndAfterLine $WitnessBlockPath))
$Records.Add((Write-TextSlice 'inherited_begin_to_before_end' $Witness $WitnessText $WitnessBegin $WitnessEndMarkerStart $WitnessPreEndPath))
$Records.Add((Write-TextSlice 'inherited_logical_article' $Witness $WitnessText $WitnessSection $WitnessEndMarkerStart $WitnessLogicalPath))
$Records.Add((Write-LfCopy 'inherited_logical_article_lf' $WitnessLogicalPath $WitnessLogicalLfPath))

$Expected = [ordered]@{
    sealed_p31_cumulative_sha256 = 'A48CB5CD1716974B686AC1CBA681CA4B17BC72F9043B78AD2528ACA41FCF814F'
    sealed_p31_section_interval_sha256 = 'AF2993A83530352893CABA50D196BDE9A17965C0E531297CA1A9E5AEB2D1B00A'
    sealed_p31_logical_article_sha256 = 'AF3B34ACF4FF8D91850AC56C4F86447ABC61E6641FF9795BEFBFDA004788585D'
    sealed_p31_logical_article_lf_sha256 = '68C72173E0C060BC68CB3651AF078ACE82B4D5806C8A41584632AA2BB4A9B27B'
}
$WholeSourceHash = (Get-FileHash -Algorithm SHA256 -LiteralPath $Sealed).Hash
$ByLabel = @{}
foreach ($Record in $Records) { $ByLabel[$Record.label] = $Record }
$Checks = [ordered]@{
    whole_source_matches = $WholeSourceHash -eq $Expected.sealed_p31_cumulative_sha256
    interval_matches = $ByLabel.sealed_p31_section_interval.sha256 -eq $Expected.sealed_p31_section_interval_sha256
    logical_matches = $ByLabel.sealed_p31_logical_article.sha256 -eq $Expected.sealed_p31_logical_article_sha256
    logical_lf_matches = $ByLabel.sealed_p31_logical_article_lf.sha256 -eq $Expected.sealed_p31_logical_article_lf_sha256
}
if ($Checks.Values -contains $false) { throw "A source custody assertion failed: $($Checks | ConvertTo-Json -Compress)" }

$Custody = [ordered]@{
    generated_at = (Get-Date -Format 'yyyy-MM-ddTHH:mm:sszzz')
    sealed_source_path = $Sealed
    inherited_witness_path = $Witness
    expected = $Expected
    checks = $Checks
    records = $Records
    boundary_finding = 'The ordinary section-to-section interval carries 68 bytes of Paper 38 setup: clearpage plus two footnote resets. The logical Paper 37 article stops immediately before that clearpage; its standalone wrapper must supply the preceding footnote reset.'
}
$CustodyPath = Join-Path $Base 'SOURCE_CUSTODY.json'
[IO.File]::WriteAllText($CustodyPath, (($Custody | ConvertTo-Json -Depth 8) + "`n"), $Utf8)
Write-Output $CustodyPath
Write-Output ((Get-FileHash -Algorithm SHA256 -LiteralPath $CustodyPath).Hash)
$Records | ForEach-Object { "{0}`t{1}`t{2}" -f $_.label, $_.sha256, $_.byte_count }
