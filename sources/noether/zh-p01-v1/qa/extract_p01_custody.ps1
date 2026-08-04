$ErrorActionPreference = 'Stop'

$root = Split-Path -Parent $PSScriptRoot
$authority = 'C:\Users\Floris\Documents\Codex\2026-06-01\we-are-currently-doing-a-massive\Noether_P07_CurrentHead_SourceAdjudication_20260722\1\01_current\Noether_P16_IndependentSecondPass_20260722_cum_de.tex'
$pointer = 'C:\Users\Floris\Documents\Codex\2026-06-01\we-are-currently-doing-a-massive\Noether_P07_CurrentHead_SourceAdjudication_20260722\1\03_audit\NOETHER_CURRENT_AUTHORITY_POINTER_20260722.md'
$witness = 'C:\Users\Floris\Documents\interlanguage\03_projects\language_management\cjk\01_recovered_witnesses\noether_cjk_chinese_japanese_cumulative_20260702\translations\non_slavic\simplified_chinese\cumulative\source_fidelity\v001\Noether_SimplifiedChinese_Cumulative_SourceFidelity_v001.tex'

$expected = [ordered]@{
    pointer_sha256 = 'FAC89D076DCE1C24B534595595B75BA1C88A8956E370EF848B307E731633EED1'
    authority_sha256 = '443EF950D7D45DC6D9E44A9B87501620C10DA873E50E5F2B253ECCAE6A946D27'
    witness_sha256 = 'C2936EFAC3C22FBEBD3E5F418902A0A4CA3CFFD953DC3ADC827432D7529DF3F9'
    authority_slice_sha256 = '0499985866E646747EC31533775FF31B55556F2C694F4C2608384829DE248D2F'
    witness_slice_sha256 = '566D05E74A03113F77EC75986115F2D7D71914E09B80C96AD5DF537D26F152E3'
}

function Assert-Hash([string]$path, [string]$hash) {
    $actual = (Get-FileHash -Algorithm SHA256 -LiteralPath $path).Hash
    if ($actual -ne $hash) { throw "Hash mismatch for $path`: expected $hash, found $actual" }
    return $actual
}

Assert-Hash $pointer $expected.pointer_sha256 | Out-Null
Assert-Hash $authority $expected.authority_sha256 | Out-Null
Assert-Hash $witness $expected.witness_sha256 | Out-Null

$authorityBytes = [IO.File]::ReadAllBytes($authority)
$witnessBytes = [IO.File]::ReadAllBytes($witness)

$authorityStart = 12505
$authorityEnd = 20587
# The recovered cumulative witness carries a three-byte UTF-8 BOM. These are
# raw-file byte offsets, so they are three bytes above the decoded-text counts.
$witnessStart = 13119
$witnessEnd = 21535

$authoritySlice = [byte[]]::new($authorityEnd - $authorityStart)
[Array]::Copy($authorityBytes, $authorityStart, $authoritySlice, 0, $authoritySlice.Length)
$witnessSlice = [byte[]]::new($witnessEnd - $witnessStart)
[Array]::Copy($witnessBytes, $witnessStart, $witnessSlice, 0, $witnessSlice.Length)

$sourceOut = Join-Path $root 'source\Noether_Paper01_CurrentGermanAuthority_interval.tex'
$witnessOut = Join-Path $root 'witness\Noether_Paper01_InheritedSimplifiedChinese_interval.tex'
[IO.File]::WriteAllBytes($sourceOut, $authoritySlice)
[IO.File]::WriteAllBytes($witnessOut, $witnessSlice)

Assert-Hash $sourceOut $expected.authority_slice_sha256 | Out-Null
Assert-Hash $witnessOut $expected.witness_slice_sha256 | Out-Null

$utf8 = [Text.UTF8Encoding]::new($false)
$sourceText = $utf8.GetString($authoritySlice)
$witnessText = $utf8.GetString($witnessSlice)
if (-not $sourceText.StartsWith('\begin{center}')) { throw 'Unexpected Paper 1 source start.' }
if (-not $sourceText.Contains('{\Large\bfseries 1. Über die Bildung des Formensystems')) { throw 'Paper 1 source title missing.' }
if (-not $sourceText.TrimEnd().EndsWith('\end{enumerate}')) { throw 'Unexpected Paper 1 source end.' }
if (-not $witnessText.StartsWith('%<unit id="noether.p01.title.001"')) { throw 'Unexpected Paper 1 witness start.' }
if (-not $witnessText.Contains('% END imported checkpoint body:')) { throw 'Paper 1 witness end marker missing.' }

$record = [ordered]@{
    schema_version = '1.0.0'
    work_id = 'NOETHER-P01'
    operation = 'exact_byte_slice_custody_only'
    authority = [ordered]@{
        pointer_path = $pointer
        pointer_sha256 = $expected.pointer_sha256
        whole_path = $authority
        whole_sha256 = $expected.authority_sha256
        source_lines = @(381, 460)
        byte_interval = @($authorityStart, $authorityEnd)
        output_path = $sourceOut
        output_bytes = $authoritySlice.Length
        output_sha256 = $expected.authority_slice_sha256
    }
    witness = [ordered]@{
        whole_path = $witness
        whole_sha256 = $expected.witness_sha256
        source_lines = @(339, 466)
        byte_interval = @($witnessStart, $witnessEnd)
        output_path = $witnessOut
        output_bytes = $witnessSlice.Length
        output_sha256 = $expected.witness_slice_sha256
        role = 'drafting witness only'
    }
    excluded_boundary = 'Paper 2 clearpage/setup begins immediately after each slice.'
    claim_limit = 'File custody and exact byte extraction only; no source, translation, formula, terminology, visual, regional, human, external, publication, or certification validation.'
}

$recordPath = Join-Path $root 'qa\SOURCE_CUSTODY_RECORD.json'
[IO.File]::WriteAllText($recordPath, (($record | ConvertTo-Json -Depth 8) + "`n"), $utf8)
$record | ConvertTo-Json -Depth 8
