param(
    [string]$OutputPath = (Join-Path $PSScriptRoot 'CHECKPOINT_IDENTITIES.csv')
)

$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $PSScriptRoot

$relativePaths = [System.Collections.Generic.List[string]]::new()
$relativePaths.Add('english_source_first_workpass/source/Serre_FAC_English_source_aligned_workpass.tex')
Get-ChildItem -LiteralPath (Join-Path $root 'english_source_first_workpass\source\components') -File -Filter '*.tex' |
    Sort-Object Name |
    ForEach-Object { $relativePaths.Add('english_source_first_workpass/source/components/' + $_.Name) }

@(
    'english_source_first_workpass/build_checkpoint_II_3_43_r2/Serre_FAC_English_source_aligned_workpass.pdf',
    'english_source_first_workpass/build_checkpoint_II_3_43_r2/Serre_FAC_English_source_aligned_workpass.log',
    'french_source_diplomatic_canon/source/fac.tex',
    'french_source_diplomatic_canon/source/fac_body.tex',
    'french_source_diplomatic_canon/build_checkpoint_T0024_r1/fac.pdf',
    'french_source_diplomatic_canon/build_checkpoint_T0024_r1/fac.log',
    'french_source_corrected_workpass/source/fac.tex',
    'french_source_corrected_workpass/source/fac_body.tex',
    'french_source_corrected_workpass/build_checkpoint_C0027_T0024_r1/fac.pdf',
    'french_source_corrected_workpass/build_checkpoint_C0027_T0024_r1/fac.log',
    'controls/SOURCE_INPUTS.csv',
    'controls/TRANSLATION_LINEAGES.csv',
    'controls/TRANSLATION_PROGRESS.csv',
    'controls/FRENCH_CORRECTIONS.csv',
    'controls/FRENCH_TRANSCRIPTION_REPAIRS.csv',
    'controls/EDITORIAL_SELF_CORRECTION_LEDGER.csv',
    'controls/ENGLISH_NORMALIZATION_OCCURRENCES.csv',
    'controls/generate_english_normalization_occurrences.ps1',
    'controls/generate_checkpoint_identities.ps1',
    'EDITORIAL_DECISION_LOGBOOK.md',
    'STATUS.md',
    'LOGBOOK.md'
) | ForEach-Object { $relativePaths.Add($_) }

$duplicates = $relativePaths | Group-Object | Where-Object Count -ne 1
if ($duplicates) {
    throw 'Duplicate path in checkpoint identity input set.'
}

$rows = foreach ($relative in $relativePaths) {
    $absolute = Join-Path $root ($relative -replace '/', '\')
    if (-not (Test-Path -LiteralPath $absolute -PathType Leaf)) {
        throw "Missing checkpoint input: $relative"
    }
    $item = Get-Item -LiteralPath $absolute
    [pscustomobject][ordered]@{
        path = $relative
        bytes = $item.Length
        sha256 = (Get-FileHash -LiteralPath $absolute -Algorithm SHA256).Hash
    }
}

$rows | Export-Csv -LiteralPath $OutputPath -NoTypeInformation -Encoding utf8

[pscustomobject]@{
    output = $OutputPath
    rows = $rows.Count
    total_bytes = ($rows | Measure-Object bytes -Sum).Sum
}
