$ErrorActionPreference = 'Stop'

$root = Split-Path -Parent $PSScriptRoot
$source = Join-Path $root 'source\Noether_Paper01_CurrentGermanAuthority_interval.tex'
$expectedSourceHash = '0499985866E646747EC31533775FF31B55556F2C694F4C2608384829DE248D2F'
$actualSourceHash = (Get-FileHash -Algorithm SHA256 -LiteralPath $source).Hash
if ($actualSourceHash -ne $expectedSourceHash) { throw "Unexpected Paper 1 source hash: $actualSourceHash" }

$utf8 = [Text.UTF8Encoding]::new($false)
$text = [IO.File]::ReadAllText($source, $utf8)
$starts = [regex]::Matches($text, '(?m)^') | ForEach-Object { $_.Index }
if ($starts.Count -ne 81 -or -not $text.EndsWith("`n")) {
    throw "Expected 80 terminated source lines, found $($starts.Count) line starts."
}

$a = $text.Substring(0, $starts[24])
$b = $text.Substring($starts[24], $starts[59] - $starts[24])
$c = $text.Substring($starts[59])
if (($a + $b + $c) -cne $text) { throw 'Segment concatenation does not reproduce the source.' }

$defs = @(
    [ordered]@{ id = 'A'; lines = @(1, 24); text = $a; path = Join-Path $root 'segments\prod_segment_A_source_lines_001_024.tex' },
    [ordered]@{ id = 'B'; lines = @(25, 59); text = $b; path = Join-Path $root 'segments\prod_segment_B_source_lines_025_059.tex' },
    [ordered]@{ id = 'C'; lines = @(60, 80); text = $c; path = Join-Path $root 'segments\prod_segment_C_source_lines_060_080.tex' }
)

$records = foreach ($def in $defs) {
    [IO.File]::WriteAllText($def.path, $def.text, $utf8)
    $item = Get-Item -LiteralPath $def.path
    [ordered]@{
        segment = $def.id
        source_lines = $def.lines
        path = $def.path
        bytes = $item.Length
        sha256 = (Get-FileHash -Algorithm SHA256 -LiteralPath $def.path).Hash
    }
}

$record = [ordered]@{
    schema_version = '1.0.0'
    work_id = 'NOETHER-P01'
    operation = 'mechanical_nonoverlapping_source_segmentation'
    source_path = $source
    source_sha256 = $expectedSourceHash
    source_lines = 80
    segments = $records
    concatenation_exact = $true
    claim_limit = 'Mechanical line segmentation only; no source, translation, formula, terminology, visual, regional, human, external, publication, or certification validation.'
}
$recordPath = Join-Path $root 'qa\SOURCE_SEGMENTATION_RECORD.json'
[IO.File]::WriteAllText($recordPath, (($record | ConvertTo-Json -Depth 8) + "`n"), $utf8)
$record | ConvertTo-Json -Depth 8
