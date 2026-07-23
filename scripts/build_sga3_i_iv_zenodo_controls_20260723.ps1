[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$PredecessorManifestCsv,

    [Parameter(Mandatory = $true)]
    [string]$PredecessorValidationJson,

    [Parameter(Mandatory = $true)]
    [string]$PackageRoot,

    [Parameter(Mandatory = $true)]
    [string]$OutputRoot,

    [long]$SuccessorRecord = 0
)

$ErrorActionPreference = 'Stop'

function Get-Identity {
    param([Parameter(Mandatory = $true)][string]$Path)

    $item = Get-Item -LiteralPath $Path
    [pscustomobject]@{
        bytes = [int64]$item.Length
        sha256 = (Get-FileHash -Algorithm SHA256 -LiteralPath $item.FullName).Hash
    }
}

function Write-Utf8NoBom {
    param(
        [Parameter(Mandatory = $true)][string]$Path,
        [Parameter(Mandatory = $true)][string]$Text
    )

    [System.IO.File]::WriteAllText(
        $Path,
        $Text,
        [System.Text.UTF8Encoding]::new($false)
    )
}

$predecessorManifest = @(Import-Csv -LiteralPath $PredecessorManifestCsv)
$predecessorValidation = Get-Content -LiteralPath $PredecessorValidationJson -Raw |
    ConvertFrom-Json
$packageManifest = @(
    Import-Csv -LiteralPath (Join-Path $PackageRoot 'SHA256SUMS.csv')
)

if ($predecessorManifest.Count -ne 34) {
    throw "Expected 34 predecessor manifest rows, found $($predecessorManifest.Count)."
}
if ($packageManifest.Count -ne 4) {
    throw "Expected 4 package manifest rows, found $($packageManifest.Count)."
}
if ([int64]$predecessorValidation.zip_member_count -ne 1124) {
    throw 'Unexpected predecessor ZIP-member count.'
}

New-Item -ItemType Directory -Force -Path $OutputRoot | Out-Null
Get-ChildItem -LiteralPath $OutputRoot -File | Remove-Item -Force

$copyMap = [ordered]@{
    'SGA3_English_Through_Expose_IV_Loop2_ReferenceV2_R2_20260723.pdf' =
        '00c1_SGA3_English_Through_Expose_IV_Loop2_ReferenceV2_R2_20260723.pdf'
    'SGA3_English_Through_Expose_IV_Loop2_ReferenceV2_R2_Master_20260723.tex' =
        '02c1_SGA3_English_Through_Expose_IV_Loop2_ReferenceV2_R2_Master_20260723.tex'
    'SGA3_English_Through_Expose_IV_Loop2_ReferenceV2_R2_Source_Ledgers_20260723.zip' =
        '10c1_SGA3_English_Through_Expose_IV_Loop2_ReferenceV2_R2_Source_Ledgers_20260723.zip'
}

foreach ($sourceName in $copyMap.Keys) {
    $sourcePath = Join-Path $PackageRoot $sourceName
    $declared = @(
        $packageManifest |
            Where-Object { $_.relative_path -eq $sourceName }
    )
    if ($declared.Count -ne 1) {
        throw "Package manifest does not identify $sourceName exactly once."
    }
    $identity = Get-Identity -Path $sourcePath
    if (
        $identity.bytes -ne [int64]$declared[0].bytes -or
        $identity.sha256 -ne $declared[0].sha256
    ) {
        throw "Package identity mismatch for $sourceName."
    }
    Copy-Item -LiteralPath $sourcePath -Destination (
        Join-Path $OutputRoot $copyMap[$sourceName]
    )
}

$readme = @'
# Current SGA compact release

This same-concept successor consolidates the current SGA 3 English progress
through complete Expose IV into one cumulative reader and source archive. It
preserves every predecessor version immutably and leaves the standalone
Expose V Loop-2 native-diagram reader unchanged.

## Reader-first order

1. English SGA 1 complete-volume working reader. Its 1,212 destinations and
   1,569 valid GoTo annotations are substantial but not exhaustively
   convention-v2 certified.
2. English SGA 2 complete archive-curated reference-linked R8 reader.
3. English SGA 3 cumulative working reader through complete Expose IV,
   followed by the standalone complete Expose V Loop-2 working reader.
   Exposes VI-XXVI are not included, so SGA 3 remains incomplete.
4. English SGA 4 proper certified reference-v2 r7 reader, covering Exposes
   I-XIX including V bis and excluding SGA 4half.
5. English SGA 5 reference-linked R9 reader.
6. English SGA 6 complete layered terminal reference-linked reader.

Available French workpasses and primary editable TeX follow the English
readers. Recursive source, reference ledgers, QA, bounded checkpoints, and
predecessor maps remain grouped into coherent ZIP archives.

## SGA 3 through Expose IV

The 266-page cumulative reader covers the Editorial Notice, Introduction,
and complete Exposes I-IV. It has 1,519 named destinations and 1,062 linked
internal rectangles. Its machine-readable graph records 411 targets, 1,157
candidate occurrences, 611 linked edges, and one disposition for every
candidate.

This independently sealed public checkpoint is the deterministic successor
to the earlier cumulative I-IV build in predecessor version
10.5281/zenodo.21512082. Its 199-member grouped ZIP is the exact audited
payload: 56 editable TeX files, 128 required PNG assets, the 266-page reader,
rights and provenance notices, convention-v2 machine data, and complete
identity controls. Every PNG is byte-identical to an already public I-IV
asset, so this successor introduces no new source-pixel class.

The earlier cumulative I-IV build and all split I-III/IV predecessors remain
immutable in their historical versions.

## SGA 3 Expose V

The unchanged 51-page Expose V Loop-2 successor replaces all 66 temporary
source-PDF-derived Loop-1 diagram PNGs with native TeX constructions. Its
public package contains no source-page pixels; public CSV and JSONL metadata
preserve the rights-blocked witness identities and QA dispositions.

## Authority and claim boundary

SGA 3 uses current Polo-Gille PDFs as controlling witnesses; OCR is locator
material only. Jacob C. Reinhold's jcreinhold/sga snapshot
e7a259f3f8608ad3edf9bf6eead3fd504dd2d23e is credited comparison and
drafting lineage, not authority. Reinhold states that his translation
contribution is CC BY 4.0; that statement does not license the underlying
French work, source-derived visual witnesses, or unrelated contributions.

SGA 4 proper uses the frozen Orgogozo TeX snapshot at commit 71766d9 as its
French authority. No new license grant is asserted. Rights remain with their
respective holders.

Machine-assisted contributors include OpenAI Codex / ChatGPT and Anthropic
Claude under human direction. These are modern working editions and
translations, not critical editions, mathematical certifications, independent
human peer review, blanket rights determinations, or accessibility
certifications.

The SGA 1 working reader is the initial preview; SGA 2 follows second.

Existing concept DOI: 10.5281/zenodo.20410947.
'@
$readmePath = Join-Path $OutputRoot '09_README_CURRENT_RELEASE.md'
Write-Utf8NoBom -Path $readmePath -Text ($readme -replace "`r`n", "`n")

$replacedFiles = @(
    '00c1_SGA3_English_Through_Expose_IV_Loop2_ReferenceV2_R2_20260723.pdf',
    '02c1_SGA3_English_Through_Expose_IV_Loop2_ReferenceV2_R2_Master_20260723.tex',
    '09_README_CURRENT_RELEASE.md',
    '09a_RELEASE_FILE_MANIFEST.csv',
    '09b_RELEASE_VALIDATION.json',
    '10c1_SGA3_English_Through_Expose_IV_Loop2_ReferenceV2_R2_Source_Ledgers_20260723.zip'
)

$retainedRows = @(
    $predecessorManifest |
        Where-Object { $_.filename -notin $replacedFiles } |
        Sort-Object filename
)
if ($retainedRows.Count -ne 30) {
    throw "Expected 30 retained predecessor rows, found $($retainedRows.Count)."
}

$newRows = [System.Collections.Generic.List[object]]::new()

function Add-NewRow {
    param(
        [Parameter(Mandatory = $true)][string]$Filename,
        [Parameter(Mandatory = $true)][string]$Role,
        [Parameter(Mandatory = $true)][string]$Provenance,
        [Parameter(Mandatory = $true)][string]$Status
    )

    $identity = Get-Identity -Path (Join-Path $OutputRoot $Filename)
    $newRows.Add([pscustomobject][ordered]@{
        filename = $Filename
        bytes = $identity.bytes
        sha256 = $identity.sha256
        role = $Role
        provenance = $Provenance
        status = $Status
    })
}

Add-NewRow `
    -Filename '00c1_SGA3_English_Through_Expose_IV_Loop2_ReferenceV2_R2_20260723.pdf' `
    -Role 'english_reader' `
    -Provenance 'independently sealed SGA3 cumulative English working checkpoint through complete Expose IV; exact GitHub package commit eb32f49d00b32099548685f53b8c6e5eda49b7a1' `
    -Status 'cumulative_working_reader_sga3_incomplete_through_expose_iv'

Add-NewRow `
    -Filename '02c1_SGA3_English_Through_Expose_IV_Loop2_ReferenceV2_R2_Master_20260723.tex' `
    -Role 'english_master_tex' `
    -Provenance 'primary editable cumulative master for the SGA3 English working reader through complete Expose IV' `
    -Status 'cumulative_working_source_sga3_incomplete_through_expose_iv'

Add-NewRow `
    -Filename '09_README_CURRENT_RELEASE.md' `
    -Role 'release_control' `
    -Provenance 'current compact same-concept release note for cumulative SGA3 English progress through Expose IV' `
    -Status 'current_release_control'

Add-NewRow `
    -Filename '10c1_SGA3_English_Through_Expose_IV_Loop2_ReferenceV2_R2_Source_Ledgers_20260723.zip' `
    -Role 'grouped_source_and_evidence' `
    -Provenance '199-member exact independently sealed public checkpoint with 56 editable TeX files, 128 required PNG assets, reader, reference ledgers, audit receipts, and identity controls; no new source-pixel class relative to predecessor' `
    -Status 'cumulative_working_package_sga3_incomplete_through_expose_iv'

$manifestRows = @($retainedRows + $newRows | Sort-Object filename)
if ($manifestRows.Count -ne 34) {
    throw "Expected 34 successor manifest rows, found $($manifestRows.Count)."
}

foreach ($row in $manifestRows) {
    foreach ($property in $row.PSObject.Properties) {
        if ([string]$property.Value -match '^[=+\-@]') {
            throw "Formula-unsafe manifest value in $($row.filename): $($property.Name)"
        }
    }
}

$manifestText = (($manifestRows | ConvertTo-Csv -NoTypeInformation) -join "`r`n") +
    "`r`n"
$manifestPath = Join-Path $OutputRoot '09a_RELEASE_FILE_MANIFEST.csv'
Write-Utf8NoBom -Path $manifestPath -Text $manifestText
$manifestIdentity = Get-Identity -Path $manifestPath

$zipPath = Join-Path $OutputRoot (
    '10c1_SGA3_English_Through_Expose_IV_Loop2_ReferenceV2_R2_Source_Ledgers_20260723.zip'
)
$zipArchive = [System.IO.Compression.ZipFile]::OpenRead($zipPath)
try {
    $zipEntries = @(
        $zipArchive.Entries |
            Where-Object { -not [string]::IsNullOrEmpty($_.Name) }
    )
    $zipUncompressed = [int64](
        $zipEntries | Measure-Object -Property Length -Sum
    ).Sum
    $unsafeEntries = @(
        $zipEntries | Where-Object {
            $_.FullName -match '^[A-Za-z]:' -or
            $_.FullName.StartsWith('/') -or
            $_.FullName.StartsWith('\') -or
            $_.FullName -match '(^|[\\/])\.\.([\\/]|$)'
        }
    )
}
finally {
    $zipArchive.Dispose()
}
if ($zipEntries.Count -ne 199) {
    throw "Expected 199 ZIP members, found $($zipEntries.Count)."
}
if ($unsafeEntries.Count -ne 0) {
    throw "Found $($unsafeEntries.Count) unsafe ZIP member names."
}

$zipArchives = [ordered]@{}
foreach ($property in $predecessorValidation.zip_archives.PSObject.Properties) {
    if (
        $property.Name -ne
            '10c1_SGA3_English_Through_Expose_IV_Loop2_ReferenceV2_R2_Source_Ledgers_20260723.zip'
    ) {
        $zipArchives[$property.Name] = $property.Value
    }
}
$zipArchives[
    '10c1_SGA3_English_Through_Expose_IV_Loop2_ReferenceV2_R2_Source_Ledgers_20260723.zip'
] = [ordered]@{
    file_members = 199
    all_entries = 199
    uncompressed_bytes = $zipUncompressed
}
if ($zipArchives.Count -ne 13) {
    throw "Expected 13 final ZIP archives, found $($zipArchives.Count)."
}

$validation = [ordered]@{
    status = 'PASS'
    errors = @()
    concept_doi = '10.5281/zenodo.20410947'
    predecessor_record = 21512082
    predecessor_doi = '10.5281/zenodo.21512082'
    reserved_successor_record = if ($SuccessorRecord -gt 0) {
        $SuccessorRecord
    }
    else {
        $null
    }
    same_concept_only = $true
    duplicate_concept_authorized = $false
    retained_predecessor_files = 30
    replaced_files = $replacedFiles
    new_sga3_i_iv_files = @(
        '00c1_SGA3_English_Through_Expose_IV_Loop2_ReferenceV2_R2_20260723.pdf',
        '02c1_SGA3_English_Through_Expose_IV_Loop2_ReferenceV2_R2_Master_20260723.tex',
        '10c1_SGA3_English_Through_Expose_IV_Loop2_ReferenceV2_R2_Source_Ledgers_20260723.zip'
    )
    content_manifest_rows = 34
    release_manifest_file = '09a_RELEASE_FILE_MANIFEST.csv'
    release_manifest_bytes = $manifestIdentity.bytes
    release_manifest_sha256 = $manifestIdentity.sha256
    final_upload_file_count = 36
    final_upload_bytes = 0
    default_preview = '00a_SGA1_English_CompleteVolume_Working_NoExhaustiveCertification_20260722.pdf'
    github = [ordered]@{
        commit = 'eb32f49d00b32099548685f53b8c6e5eda49b7a1'
        package = 'sources/sga/sga3-english-through-expose-iv-loop2-reference-v2-r2-20260723'
        outer_files = 6
        zip_members = 199
        readback_errors = @()
    }
    sga3_i_iv = [ordered]@{
        scope = 'cumulative SGA3 English working reader through complete Expose IV'
        sga3_complete = $false
        untranslated_exposes = 'VI-XXVI'
        reader_pages = 266
        reader_sha256 = 'B717DC08C2C77546638274C7F05266F5F24C1562999117ACF4D1874AFD79EA1D'
        pdf_named_destinations = 1519
        pdf_linked_rectangles = 1062
        reference_targets = 411
        reference_candidates = 1157
        reference_edges = 611
        public_checkpoint_files = 199
        source_stage_tex_dependencies = 56
        source_stage_pngs = 128
        build_required_pngs = 128
        new_source_pixel_class = $false
        expose_iv_native_diagrams = $true
    }
    rights = [ordered]@{
        new_license_grant = $false
        new_source_pixel_class = $false
        predecessor_identical_pngs = 128
        reinhold_comparison_lineage_attributed = $true
        disposition = 'existing_public_pixel_class_repacked_in_exact_independently_sealed_checkpoint'
    }
    zip_archives = $zipArchives
    zip_archive_count = $zipArchives.Count
    zip_member_count = (
        [int64]$predecessorValidation.zip_member_count - 200 + 199
    )
    zip_uncompressed_bytes = (
        [int64]$predecessorValidation.zip_uncompressed_bytes -
        5259929 +
        $zipUncompressed
    )
    contributors = @(
        'OpenAI Codex / ChatGPT',
        'Anthropic Claude'
    )
    privacy_hits = @()
}
if ([int64]$validation.zip_member_count -ne 1123) {
    throw 'Final ZIP-member count is not the expected value 1123.'
}

$validationPath = Join-Path $OutputRoot '09b_RELEASE_VALIDATION.json'
$manifestContentBytes = [int64](
    $manifestRows | Measure-Object -Property bytes -Sum
).Sum + $manifestIdentity.bytes

for ($attempt = 0; $attempt -lt 8; $attempt++) {
    $json = ($validation | ConvertTo-Json -Depth 12) -replace "`r`n", "`n"
    $json += "`n"
    $jsonBytes = [System.Text.UTF8Encoding]::new($false).GetByteCount($json)
    $totalBytes = $manifestContentBytes + $jsonBytes
    if ($validation.final_upload_bytes -eq $totalBytes) {
        break
    }
    $validation.final_upload_bytes = $totalBytes
}
Write-Utf8NoBom -Path $validationPath -Text $json

$finalFiles = @(Get-ChildItem -LiteralPath $OutputRoot -File)
if ($finalFiles.Count -ne 6) {
    throw "Expected 6 successor staging files, found $($finalFiles.Count)."
}

$finalReleaseBytes = $manifestContentBytes +
    (Get-Item -LiteralPath $validationPath).Length
if ($finalReleaseBytes -ne $validation.final_upload_bytes) {
    throw 'Validation final release byte count mismatch.'
}

[pscustomobject]@{
    status = 'PASS'
    output_files = $finalFiles.Count
    output_bytes = [int64](
        $finalFiles | Measure-Object -Property Length -Sum
    ).Sum
    retained_files = $retainedRows.Count
    final_zenodo_files = 36
    final_zenodo_bytes = $finalReleaseBytes
    manifest_rows = $manifestRows.Count
    manifest_sha256 = $manifestIdentity.sha256
    validation_sha256 = (
        Get-FileHash -Algorithm SHA256 -LiteralPath $validationPath
    ).Hash
    zip_archives = $zipArchives.Count
    zip_members = $validation.zip_member_count
    zip_uncompressed_bytes = $validation.zip_uncompressed_bytes
} | ConvertTo-Json -Depth 4
