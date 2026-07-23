[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$PredecessorManifestCsv,

    [Parameter(Mandatory = $true)]
    [string]$PredecessorValidationJson,

    [Parameter(Mandatory = $true)]
    [string]$PackageRoot,

    [Parameter(Mandatory = $true)]
    [string]$OutputRoot
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
$packageManifest = @(Import-Csv -LiteralPath (Join-Path $PackageRoot 'SHA256SUMS.csv'))

if ($predecessorManifest.Count -ne 35) {
    throw "Expected 35 predecessor manifest rows, found $($predecessorManifest.Count)."
}
if ($packageManifest.Count -ne 7) {
    throw "Expected 7 package manifest rows, found $($packageManifest.Count)."
}

New-Item -ItemType Directory -Force -Path $OutputRoot | Out-Null

$copyMap = [ordered]@{
    'SGA3_English_Expose_V_Loop2_Native_ReferenceV2_R2_20260723.pdf' =
        '00c3_SGA3_English_Expose_V_Loop2_Native_ReferenceV2_R2_20260723.pdf'
    'SGA3_English_Expose_V_Loop2_Native_Master_R2_20260723.tex' =
        '02c3_SGA3_English_Expose_V_Loop2_Native_Master_R2_20260723.tex'
    'RIGHTS_BLOCKED_SOURCE_WITNESSES.csv' =
        '09c_SGA3_Expose_V_Loop2_Rights_Blocked_Source_Witnesses_20260723.csv'
    'RIGHTS_BLOCKED_SOURCE_WITNESSES.jsonl' =
        '09d_SGA3_Expose_V_Loop2_Rights_Blocked_Source_Witnesses_20260723.jsonl'
    'SGA3_English_Expose_V_Loop2_Native_Source_Evidence_R2_20260723.zip' =
        '10c3_SGA3_English_Expose_V_Loop2_Native_Source_Evidence_R2_20260723.zip'
}

foreach ($sourceName in $copyMap.Keys) {
    $sourcePath = Join-Path $PackageRoot $sourceName
    $declared = @($packageManifest | Where-Object { $_.relative_path -eq $sourceName })
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
    ) -Force
}

$readmePath = Join-Path $OutputRoot '09_README_CURRENT_RELEASE.md'
if (-not (Test-Path -LiteralPath $readmePath)) {
    throw "Create the successor README before running this generator: $readmePath"
}

$replacedFiles = @(
    '00c3_SGA3_English_Expose_V_Working_R3_Freeze3_20260723.pdf',
    '02c3_SGA3_English_Expose_V_Master_R3_Freeze3_20260723.tex',
    '09_README_CURRENT_RELEASE.md',
    '09a_RELEASE_FILE_MANIFEST.csv',
    '09b_RELEASE_VALIDATION.json',
    '10c3_SGA3_English_Expose_V_R3_Freeze3_Source_Evidence_20260723.zip'
)

$retainedRows = @(
    $predecessorManifest |
        Where-Object { $_.filename -notin $replacedFiles } |
        Sort-Object filename
)
if ($retainedRows.Count -ne 31) {
    throw "Expected 31 retained predecessor rows, found $($retainedRows.Count)."
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
    -Filename '00c3_SGA3_English_Expose_V_Loop2_Native_ReferenceV2_R2_20260723.pdf' `
    -Role 'english_reader' `
    -Provenance 'SGA3 Expose V Loop2 native-diagram/reference-v2 R2 freeze2; exact GitHub package commit 8af7a27f3ffbdf32f34fd9f6e4134c2477eb80fb' `
    -Status 'bounded_working_reader_sga3_incomplete_native_diagrams_complete'

Add-NewRow `
    -Filename '02c3_SGA3_English_Expose_V_Loop2_Native_Master_R2_20260723.tex' `
    -Role 'english_master_tex' `
    -Provenance 'primary editable master for the SGA3 Expose V Loop2 native-diagram/reference-v2 R2 freeze2 reader' `
    -Status 'bounded_working_source_sga3_incomplete_native_diagrams_complete'

Add-NewRow `
    -Filename '09_README_CURRENT_RELEASE.md' `
    -Role 'release_control' `
    -Provenance 'current compact same-concept release note for SGA3 Expose V Loop2 native-diagram successor' `
    -Status 'current_release_control'

Add-NewRow `
    -Filename '09c_SGA3_Expose_V_Loop2_Rights_Blocked_Source_Witnesses_20260723.csv' `
    -Role 'rights_blocked_visual_witness_metadata' `
    -Provenance '66 source-PDF-derived visual witnesses withheld as pixels; public locator, hash, dimensions, target linkage, native replacement, and QA metadata' `
    -Status 'source_pixels_withheld_metadata_public'

Add-NewRow `
    -Filename '09d_SGA3_Expose_V_Loop2_Rights_Blocked_Source_Witnesses_20260723.jsonl' `
    -Role 'rights_blocked_visual_witness_metadata' `
    -Provenance '66 source-PDF-derived visual witnesses withheld as pixels; public locator, hash, dimensions, target linkage, native replacement, and QA metadata' `
    -Status 'source_pixels_withheld_metadata_public'

Add-NewRow `
    -Filename '10c3_SGA3_English_Expose_V_Loop2_Native_Source_Evidence_R2_20260723.zip' `
    -Role 'grouped_source_and_evidence' `
    -Provenance '229-member privacy-clean source, native-diagram, reference, build, and QA archive; source pixels excluded' `
    -Status 'bounded_working_package_sga3_incomplete_native_diagrams_complete'

$manifestRows = @($retainedRows + $newRows | Sort-Object filename)
if ($manifestRows.Count -ne 37) {
    throw "Expected 37 successor manifest rows, found $($manifestRows.Count)."
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
    '10c3_SGA3_English_Expose_V_Loop2_Native_Source_Evidence_R2_20260723.zip'
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
}
finally {
    $zipArchive.Dispose()
}
if ($zipEntries.Count -ne 229) {
    throw "Expected 229 ZIP members, found $($zipEntries.Count)."
}

$zipArchives = [ordered]@{}
foreach ($property in $predecessorValidation.zip_archives.PSObject.Properties) {
    if (
        $property.Name -ne
        '10c3_SGA3_English_Expose_V_R3_Freeze3_Source_Evidence_20260723.zip'
    ) {
        $zipArchives[$property.Name] = $property.Value
    }
}
$zipArchives[
    '10c3_SGA3_English_Expose_V_Loop2_Native_Source_Evidence_R2_20260723.zip'
] = [ordered]@{
    file_members = 229
    all_entries = 229
    uncompressed_bytes = $zipUncompressed
}

$validation = [ordered]@{
    status = 'PASS'
    errors = @()
    concept_doi = '10.5281/zenodo.20410947'
    predecessor_record = 21510120
    predecessor_doi = '10.5281/zenodo.21510120'
    reserved_successor_record = 21511144
    same_concept_only = $true
    duplicate_concept_authorized = $false
    retained_predecessor_files = 31
    replaced_files = $replacedFiles
    new_sga3_loop2_files = @(
        '00c3_SGA3_English_Expose_V_Loop2_Native_ReferenceV2_R2_20260723.pdf',
        '02c3_SGA3_English_Expose_V_Loop2_Native_Master_R2_20260723.tex',
        '09c_SGA3_Expose_V_Loop2_Rights_Blocked_Source_Witnesses_20260723.csv',
        '09d_SGA3_Expose_V_Loop2_Rights_Blocked_Source_Witnesses_20260723.jsonl',
        '10c3_SGA3_English_Expose_V_Loop2_Native_Source_Evidence_R2_20260723.zip'
    )
    content_manifest_rows = 37
    release_manifest_file = '09a_RELEASE_FILE_MANIFEST.csv'
    release_manifest_bytes = $manifestIdentity.bytes
    release_manifest_sha256 = $manifestIdentity.sha256
    final_upload_file_count = 39
    final_upload_bytes = 0
    default_preview = '00b_SGA2_English_Complete_ReferenceLinked_R8_20260723.pdf'
    github = [ordered]@{
        commit = '8af7a27f3ffbdf32f34fd9f6e4134c2477eb80fb'
        package = 'sources/sga/sga3-english-expose-v-loop2-native-r2-freeze2-20260723'
        outer_files = 8
        outer_bytes = 14643306
        zip_members = 229
        readback_errors = @()
    }
    sga3_expose_v_loop2 = [ordered]@{
        scope = 'complete SGA3 Expose V bounded working reader'
        sga3_complete = $false
        untranslated_exposes = 'VI-XXVI'
        reader_pages = 51
        reader_sha256 = 'E4682CBED71922AF8C1C2851D8B69F2CF6A1E089CC4CC52EDF0318708F65F6F2'
        native_diagrams = 66
        source_pixel_members = 0
        pdf_image_xobjects = 0
        pdf_destinations = 350
        pdf_goto_actions = 411
        reference_targets = 273
        reference_edges = 333
        isolated_rebuild_raster_equal_pages = 51
    }
    rights = [ordered]@{
        new_license_grant = $false
        source_pixels_public = 0
        source_witness_metadata_rows = 66
        disposition = 'rights_blocked_pixels_withheld_metadata_public'
    }
    zip_archives = $zipArchives
    zip_archive_count = $zipArchives.Count
    zip_member_count = (
        [int64]$predecessorValidation.zip_member_count - 268 + 229
    )
    zip_uncompressed_bytes = (
        [int64]$predecessorValidation.zip_uncompressed_bytes -
        33932472 +
        $zipUncompressed
    )
    contributors_planned = @(
        'OpenAI Codex / ChatGPT',
        'Anthropic Claude'
    )
    privacy_hits = @()
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
if ($finalFiles.Count -ne 8) {
    throw "Expected 8 successor staging files, found $($finalFiles.Count)."
}

$stagingBytes = [int64]($finalFiles | Measure-Object -Property Length -Sum).Sum
$newContentBytes = [int64](
    $newRows | Measure-Object -Property bytes -Sum
).Sum
$expectedStagingBytes = $newContentBytes +
    $manifestIdentity.bytes +
    (Get-Item -LiteralPath $validationPath).Length
if ($stagingBytes -ne $expectedStagingBytes) {
    throw "Final staging byte count mismatch: $stagingBytes != $expectedStagingBytes."
}
$finalReleaseBytes = $manifestContentBytes +
    (Get-Item -LiteralPath $validationPath).Length
if ($finalReleaseBytes -ne $validation.final_upload_bytes) {
    throw "Validation final release byte count mismatch."
}

[pscustomobject]@{
    status = 'PASS'
    output_files = $finalFiles.Count
    output_bytes = $stagingBytes
    retained_files = $retainedRows.Count
    final_zenodo_files = 39
    final_zenodo_bytes = $finalReleaseBytes
    manifest_rows = $manifestRows.Count
    manifest_sha256 = $manifestIdentity.sha256
    validation_sha256 = (
        Get-FileHash -Algorithm SHA256 -LiteralPath $validationPath
    ).Hash
    zip_members = $zipEntries.Count
    zip_uncompressed_bytes = $zipUncompressed
} | ConvertTo-Json -Depth 4
