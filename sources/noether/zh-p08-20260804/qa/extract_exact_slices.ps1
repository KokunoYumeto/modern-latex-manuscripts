[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $PSScriptRoot
$sourcePath = Join-Path $root 'source\P08_complete_lines5957_6347_LF_terminal.tex'
$witnessWholePath = 'C:\Users\Floris\Documents\interlanguage\03_projects\language_management\cjk\01_recovered_witnesses\noether_cjk_chinese_japanese_cumulative_20260702\translations\non_slavic\simplified_chinese\cumulative\source_fidelity\v001\Noether_SimplifiedChinese_Cumulative_SourceFidelity_v001.tex'
$utf8NoBom = [System.Text.UTF8Encoding]::new($false)

function Get-Sha256([string]$Path) {
  return (Get-FileHash -LiteralPath $Path -Algorithm SHA256).Hash
}

function Write-Utf8LfSlice([string[]]$Lines, [int]$StartInclusive, [int]$EndInclusive, [string]$Path) {
  $slice = $Lines[($StartInclusive - 1)..($EndInclusive - 1)]
  $text = [string]::Join("`n", $slice) + "`n"
  [System.IO.File]::WriteAllText($Path, $text, $utf8NoBom)
}

if ((Get-Sha256 $sourcePath) -ne '7E5EEBEB8F569F101490D8262072027C876C8102D2841A2A57F96E0DC2708E71') {
  throw 'Controlling LF source identity mismatch.'
}
if ((Get-Item -LiteralPath $witnessWholePath).Length -ne 1741015 -or
    (Get-Sha256 $witnessWholePath) -ne 'C2936EFAC3C22FBEBD3E5F418902A0A4CA3CFFD953DC3ADC827432D7529DF3F9') {
  throw 'Inherited cumulative Hans witness identity mismatch.'
}

$wholeBytes = [System.IO.File]::ReadAllBytes($witnessWholePath)
$rawStart = 360564
$rawEnd = 385021
$rawLength = $rawEnd - $rawStart
$rawSlice = [byte[]]::new($rawLength)
[System.Buffer]::BlockCopy($wholeBytes, $rawStart, $rawSlice, 0, $rawLength)
$rawWitnessPath = Join-Path $root 'witness\P08_inherited_Hans_lines6395_6842_source_native_CRLF.tex'
[System.IO.File]::WriteAllBytes($rawWitnessPath, $rawSlice)
if ((Get-Item -LiteralPath $rawWitnessPath).Length -ne 24457 -or
    (Get-Sha256 $rawWitnessPath) -ne '3CCE30053C8022BAE80E68C5776F5AD340C03744ACA6A651219746272F8E55C9') {
  throw 'Raw inherited Paper 8 witness slice mismatch.'
}

$rawText = $utf8NoBom.GetString($rawSlice)
$lfText = $rawText.Replace("`r`n", "`n").Replace("`r", "`n")
$lfWitnessPath = Join-Path $root 'witness\P08_inherited_Hans_lines6395_6842_LF_terminal.tex'
[System.IO.File]::WriteAllText($lfWitnessPath, $lfText, $utf8NoBom)
if ((Get-Item -LiteralPath $lfWitnessPath).Length -ne 24009 -or
    (Get-Sha256 $lfWitnessPath) -ne 'F1DC44C7E4FC9D55EDC7636660CC741959A06613EABA43014353B663DE7A36D3') {
  throw 'LF inherited Paper 8 witness slice mismatch.'
}

$sourceLines = [System.IO.File]::ReadAllLines($sourcePath, $utf8NoBom)
$witnessLines = [System.IO.File]::ReadAllLines($lfWitnessPath, $utf8NoBom)
if ($sourceLines.Count -ne 391) { throw "Expected 391 source lines, found $($sourceLines.Count)." }
if ($witnessLines.Count -ne 448) { throw "Expected 448 witness lines, found $($witnessLines.Count)." }

Write-Utf8LfSlice $sourceLines 1 70 (Join-Path $root 'segments\source\P08_S01_INTRO_I_source_LF.tex')
Write-Utf8LfSlice $sourceLines 71 271 (Join-Path $root 'segments\source\P08_S02_II_source_LF.tex')
Write-Utf8LfSlice $sourceLines 272 385 (Join-Path $root 'segments\source\P08_S03_III_source_LF.tex')
Write-Utf8LfSlice $sourceLines 386 391 (Join-Path $root 'segments\source\P08_S04_TRAILING_CONTROLS_source_LF.tex')

Write-Utf8LfSlice $witnessLines 1 78 (Join-Path $root 'segments\witness\P08_S01_INTRO_I_inherited_Hans_LF.tex')
Write-Utf8LfSlice $witnessLines 79 321 (Join-Path $root 'segments\witness\P08_S02_II_inherited_Hans_LF.tex')
Write-Utf8LfSlice $witnessLines 322 448 (Join-Path $root 'segments\witness\P08_S03_III_inherited_Hans_LF.tex')

$created = Get-ChildItem -LiteralPath (Join-Path $root 'segments') -File -Recurse |
  Sort-Object FullName |
  ForEach-Object {
    [pscustomobject]@{
      path = $_.FullName
      bytes = $_.Length
      sha256 = Get-Sha256 $_.FullName
    }
  }
$created | Format-Table -AutoSize
