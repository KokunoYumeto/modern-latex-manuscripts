param(
    [Parameter(Mandatory = $true)]
    [string]$SourceProjection,

    [Parameter(Mandatory = $true)]
    [string]$IndependentAudit,

    [Parameter(Mandatory = $true)]
    [string]$OutputRoot
)

$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

function Get-Sha256 {
    param([Parameter(Mandatory = $true)][string]$Path)
    return (Get-FileHash -LiteralPath $Path -Algorithm SHA256).Hash.ToUpperInvariant()
}

function Get-RelativePosixPath {
    param(
        [Parameter(Mandatory = $true)][string]$Root,
        [Parameter(Mandatory = $true)][string]$Path
    )
    return [System.IO.Path]::GetRelativePath($Root, $Path).Replace('\', '/')
}

function ConvertTo-SafeCsv {
    param([Parameter(Mandatory = $true)][object[]]$Rows)

    $lines = $Rows | ConvertTo-Csv -NoTypeInformation
    return ($lines -join "`r`n") + "`r`n"
}

function Get-ByteIdentity {
    param([Parameter(Mandatory = $true)][byte[]]$Bytes)

    $sha = [System.Security.Cryptography.SHA256]::HashData($Bytes)
    return @{
        bytes = $Bytes.Length
        sha256 = [Convert]::ToHexString($sha)
    }
}

function Add-ZipBytes {
    param(
        [Parameter(Mandatory = $true)]
        [System.IO.Compression.ZipArchive]$Archive,

        [Parameter(Mandatory = $true)]
        [string]$EntryName,

        [Parameter(Mandatory = $true)]
        [byte[]]$Bytes
    )

    $entry = $Archive.CreateEntry(
        $EntryName.Replace('\', '/'),
        [System.IO.Compression.CompressionLevel]::Optimal
    )
    $entry.LastWriteTime = [DateTimeOffset]'2026-07-23T00:00:00Z'
    $stream = $entry.Open()
    try {
        $stream.Write($Bytes, 0, $Bytes.Length)
    }
    finally {
        $stream.Dispose()
    }
}

$source = (Resolve-Path -LiteralPath $SourceProjection).Path
$auditPath = (Resolve-Path -LiteralPath $IndependentAudit).Path
$output = [System.IO.Path]::GetFullPath($OutputRoot)

if (Test-Path -LiteralPath $output) {
    throw "OutputRoot already exists: $output"
}

$producerValidationPath = Join-Path $source 'PUBLIC_PROJECTION_VALIDATION.json'
$producerManifestPath = Join-Path $source 'ZENODO_PAYLOAD_MANIFEST.csv'
$diagramLedgerPath = Join-Path $source 'controls\loop2\LOOP2_NATIVE_DIAGRAMS_R4.csv'
$pdfSourcePath = Join-Path $source 'build\SGA3_Expose_V_English_Loop2_Native_ReferenceV2_00_23.pdf'
$texSourcePath = Join-Path $source 'tex\SGA3_Expose_V_English_Loop2_Native_ReferenceV2_00_23.tex'
$publicLogPath = Join-Path $source 'build\SGA3_Expose_V_English_Loop2_Native_ReferenceV2_00_23_BUILD_PUBLIC.log'

$producerValidation = Get-Content -LiteralPath $producerValidationPath -Raw |
    ConvertFrom-Json -Depth 100
$independentAuditJson = Get-Content -LiteralPath $auditPath -Raw |
    ConvertFrom-Json -Depth 100

if ($producerValidation.status -ne 'PASS' -or @($producerValidation.errors).Count -ne 0) {
    throw 'Producer projection validation is not PASS/errors[].'
}
if ($independentAuditJson.status -ne 'PASS') {
    throw 'Independent PDF/reference/render audit is not PASS.'
}

$expected = @{
    producer_manifest_rows = 296
    producer_tree_files = 298
    master_bytes = 7202
    master_sha256 = '92AB24AB2E104618AB4E97AC4A2F23554BECB741258F7E9739EC463E6B99C37E'
    pdf_bytes = 361493
    pdf_sha256 = 'E4682CBED71922AF8C1C2851D8B69F2CF6A1E089CC4CC52EDF0318708F65F6F2'
    pdf_pages = 51
    destinations = 350
    goto_actions = 411
    targets = 273
    edges = 333
    diagrams = 66
    source_witnesses = 66
}

if ([int]$producerValidation.manifest.rows -ne $expected.producer_manifest_rows) {
    throw 'Unexpected producer manifest row count.'
}
if ([int]$producerValidation.tree.files_including_manifest_and_validation -ne $expected.producer_tree_files) {
    throw 'Unexpected producer tree file count.'
}

$producerRows = @(Import-Csv -LiteralPath $producerManifestPath)
if ($producerRows.Count -ne $expected.producer_manifest_rows) {
    throw 'Producer manifest CSV row count mismatch.'
}

$producerReplayErrors = [System.Collections.Generic.List[string]]::new()
foreach ($row in $producerRows) {
    $candidate = Join-Path $source ([string]$row.relative_path)
    if (-not (Test-Path -LiteralPath $candidate -PathType Leaf)) {
        $producerReplayErrors.Add("missing:$($row.relative_path)")
        continue
    }
    $item = Get-Item -LiteralPath $candidate
    $sha = Get-Sha256 -Path $candidate
    if ($item.Length -ne [long]$row.bytes -or $sha -ne [string]$row.sha256) {
        $producerReplayErrors.Add("identity:$($row.relative_path)")
    }
}
if ($producerReplayErrors.Count -ne 0) {
    throw "Producer manifest replay errors: $($producerReplayErrors -join ', ')"
}

$pdfItem = Get-Item -LiteralPath $pdfSourcePath
$texItem = Get-Item -LiteralPath $texSourcePath
$pdfSha = Get-Sha256 -Path $pdfSourcePath
$texSha = Get-Sha256 -Path $texSourcePath
if ($pdfItem.Length -ne $expected.pdf_bytes -or $pdfSha -ne $expected.pdf_sha256) {
    throw 'Reader PDF identity mismatch.'
}
if ($texItem.Length -ne $expected.master_bytes -or $texSha -ne $expected.master_sha256) {
    throw 'Master TeX identity mismatch.'
}
if (
    [int]$producerValidation.reader.pdf.pages -ne $expected.pdf_pages -or
    [int]$producerValidation.reader.pdf.named_destinations -ne $expected.destinations -or
    [int]$producerValidation.reader.pdf.goto_actions -ne $expected.goto_actions -or
    [int]$producerValidation.reference_v2.targets -ne $expected.targets -or
    [int]$producerValidation.reference_v2.edges -ne $expected.edges -or
    [int]$producerValidation.diagrams.inventory_rows -ne $expected.diagrams
) {
    throw 'Producer PDF/reference/diagram counts do not match the frozen release boundary.'
}
if (
    [string]$independentAuditJson.identities.delivered_pdf.sha256 -ne $expected.pdf_sha256 -or
    [string]$independentAuditJson.identities.master.sha256 -ne $expected.master_sha256 -or
    [int]$independentAuditJson.native_closure.native_files -ne $expected.diagrams -or
    [int]$independentAuditJson.pdf.image_xobjects -ne 0 -or
    [int]$independentAuditJson.reference_closure.edges_backed_by_actions -ne $expected.edges -or
    [int]$independentAuditJson.render_closure.packaged_vs_fresh_delivered_exact -ne $expected.pdf_pages
) {
    throw 'Independent audit is not bound to the expected r4 release identities.'
}

New-Item -ItemType Directory -Path $output | Out-Null

$pdfOutputName = 'SGA3_English_Expose_V_Loop2_Native_ReferenceV2_R2_20260723.pdf'
$texOutputName = 'SGA3_English_Expose_V_Loop2_Native_Master_R2_20260723.tex'
$zipOutputName = 'SGA3_English_Expose_V_Loop2_Native_Source_Evidence_R2_20260723.zip'
$rightsCsvName = 'RIGHTS_BLOCKED_SOURCE_WITNESSES.csv'
$rightsJsonlName = 'RIGHTS_BLOCKED_SOURCE_WITNESSES.jsonl'
$releaseValidationName = 'RELEASE_VALIDATION.json'
$shaManifestName = 'SHA256SUMS.csv'

Copy-Item -LiteralPath $pdfSourcePath -Destination (Join-Path $output $pdfOutputName)
Copy-Item -LiteralPath $texSourcePath -Destination (Join-Path $output $texOutputName)

$diagramRows = @(Import-Csv -LiteralPath $diagramLedgerPath)
if ($diagramRows.Count -ne $expected.diagrams) {
    throw 'Native-diagram ledger does not contain 66 rows.'
}

$rightsRows = [System.Collections.Generic.List[object]]::new()
$seenWitnesses = [System.Collections.Generic.HashSet[string]]::new(
    [System.StringComparer]::Ordinal
)
foreach ($row in $diagramRows) {
    $imageRelative = ([string]$row.image_path).Replace('\', '/')
    if (-not $imageRelative.StartsWith('figures/exp5/', [System.StringComparison]::Ordinal)) {
        throw "Unexpected image path in native-diagram ledger: $imageRelative"
    }
    $witnessRelative = 'source_png_witness/' + $imageRelative.Substring('figures/'.Length)
    $witnessPath = Join-Path $source $witnessRelative
    if (-not (Test-Path -LiteralPath $witnessPath -PathType Leaf)) {
        throw "Missing rights-held witness: $witnessRelative"
    }
    $witnessItem = Get-Item -LiteralPath $witnessPath
    $witnessSha = Get-Sha256 -Path $witnessPath
    if (
        $witnessItem.Length -ne [long]$row.image_bytes -or
        $witnessSha -ne [string]$row.image_sha256 -or
        $witnessSha -ne [string]$row.source_png_replay_sha256
    ) {
        throw "Rights-held witness identity mismatch: $witnessRelative"
    }
    if (-not $seenWitnesses.Add($witnessRelative)) {
        throw "Duplicate rights-held witness path: $witnessRelative"
    }

    $pixelParts = ([string]$row.pixels) -split 'x', 2
    if ($pixelParts.Count -ne 2) {
        throw "Invalid pixel dimensions: $($row.pixels)"
    }

    $rightsRows.Add([pscustomobject][ordered]@{
        schema_version = 'sga_visual_witness_rights_block_v1'
        witness_id = [string]$row.diagram_id
        disposition = 'rights_blocked_not_public'
        pixel_file_in_public_package = 'false'
        private_witness_relative_path = $witnessRelative
        source_image_name = [System.IO.Path]::GetFileName($witnessRelative)
        parent_pdf_name = 'Exp5-13oct24.pdf'
        parent_pdf_bytes = '439522'
        parent_pdf_pages = '41'
        parent_pdf_sha256 = '9198200633F929FE1822520371A9200DA4F8CF2513EFAB3D6A0C7E9330DB84CF'
        source_locator = [string]$row.source_locator
        width_px = $pixelParts[0]
        height_px = $pixelParts[1]
        dpi_x = 'not_recorded'
        dpi_y = 'not_recorded'
        rotation_degrees = 'not_recorded'
        crop_bbox_pixels = 'not_recorded'
        crop_bytes = [string]$row.image_bytes
        crop_sha256 = [string]$row.image_sha256
        linked_component_tex = [string]$row.component_tex
        linked_tex_line = [string]$row.tex_line
        linked_structural_unit = [string]$row.diagram_id
        content_summary = [string]$row.content_summary
        native_tex_path = [string]$row.native_tex_path
        native_tex_sha256 = [string]$row.native_tex_sha256
        source_review_status = [string]$row.agent_source_check_status
        lead_review_status = [string]$row.lead_review_status
        qa_disposition = 'metadata_public_pixels_withheld_pending_rights'
        notes = 'The source-PDF-derived pixel witness is not redistributed in this release. Hash, locator, dimensions, linked TeX, native replacement, and review disposition are preserved.'
    })
}
if ($seenWitnesses.Count -ne $expected.source_witnesses) {
    throw 'Rights-held witness set is not exactly 66 files.'
}

$rightsCsv = ConvertTo-SafeCsv -Rows $rightsRows.ToArray()
$rightsCsvPath = Join-Path $output $rightsCsvName
[System.IO.File]::WriteAllText(
    $rightsCsvPath,
    $rightsCsv,
    [System.Text.UTF8Encoding]::new($false)
)

$rightsJsonLines = foreach ($row in $rightsRows) {
    $row | ConvertTo-Json -Compress -Depth 10
}
$rightsJsonl = ($rightsJsonLines -join "`n") + "`n"
$rightsJsonlPath = Join-Path $output $rightsJsonlName
[System.IO.File]::WriteAllText(
    $rightsJsonlPath,
    $rightsJsonl,
    [System.Text.UTF8Encoding]::new($false)
)

$packageReadme = @"
# SGA 3 Expose V Loop 2 native source and evidence

This archive contains the self-contained editable Expose V Loop 2 reader,
66 native TikZ/TikZ-cd diagram sources, convention-v2 controls, public build
evidence, and project-generated render QA.

The 66 source-PDF-derived PNG witnesses are deliberately absent because
their redistribution rights are not affirmatively established. Their parent
PDF identity, source locators, dimensions, crop hashes, linked TeX units,
native replacements, and review dispositions are preserved in
RIGHTS_BLOCKED_SOURCE_WITNESSES.csv and .jsonl.

The reader is a bounded working English Expose V checkpoint, not complete
SGA 3, a critical edition, mathematical certification, independent human
peer review, blanket rights clearance, or accessibility certification.

Jacob Reinhold's jcreinhold/sga English Markdown at revision
e7a259f3f8608ad3edf9bf6eead3fd504dd2d23e was credited comparison and
drafting material under his stated CC BY 4.0 license. It is not source
authority or independent corroboration.
"@
$packageReadmeBytes = [System.Text.UTF8Encoding]::new($false).GetBytes(
    $packageReadme.Replace("`r`n", "`n")
)

$memberSources = [System.Collections.Generic.List[object]]::new()
$includeRoots = @('tex', 'native_diagrams', 'controls', 'qa')
foreach ($includeRoot in $includeRoots) {
    $absoluteRoot = Join-Path $source $includeRoot
    Get-ChildItem -LiteralPath $absoluteRoot -Recurse -File |
        ForEach-Object {
            $relative = Get-RelativePosixPath -Root $source -Path $_.FullName
            $memberSources.Add([pscustomobject]@{
                entry_name = $relative
                source_path = $_.FullName
            })
        }
}
$memberSources.Add([pscustomobject]@{
    entry_name = 'build/SGA3_Expose_V_English_Loop2_Native_ReferenceV2_00_23_BUILD_PUBLIC.log'
    source_path = $publicLogPath
})

$memberSources = @(
    $memberSources |
        Sort-Object entry_name -Unique
)
if ($memberSources | Where-Object { $_.entry_name -like 'source_png_witness/*' }) {
    throw 'Rights-held source pixels entered the archive member set.'
}

$memberRows = [System.Collections.Generic.List[object]]::new()
foreach ($member in $memberSources) {
    $item = Get-Item -LiteralPath $member.source_path
    $memberRows.Add([pscustomobject][ordered]@{
        relative_path = [string]$member.entry_name
        bytes = [string]$item.Length
        sha256 = Get-Sha256 -Path $member.source_path
        role = 'source_or_machine_evidence'
        status = 'public_rights_curated'
    })
}

foreach ($generated in @(
    @{ name = $rightsCsvName; path = $rightsCsvPath; role = 'rights_blocked_metadata' },
    @{ name = $rightsJsonlName; path = $rightsJsonlPath; role = 'rights_blocked_metadata' }
)) {
    $item = Get-Item -LiteralPath $generated.path
    $memberRows.Add([pscustomobject][ordered]@{
        relative_path = $generated.name
        bytes = [string]$item.Length
        sha256 = Get-Sha256 -Path $generated.path
        role = $generated.role
        status = 'public_metadata_pixels_withheld'
    })
}
$readmeIdentity = Get-ByteIdentity -Bytes $packageReadmeBytes
$memberRows.Add([pscustomobject][ordered]@{
    relative_path = 'ARCHIVE_PACKAGE_README.md'
    bytes = [string]$readmeIdentity.bytes
    sha256 = [string]$readmeIdentity.sha256
    role = 'documentation'
    status = 'public_rights_curated'
})

$memberRows = @($memberRows | Sort-Object relative_path)
$memberManifest = ConvertTo-SafeCsv -Rows $memberRows
$memberManifestBytes = [System.Text.UTF8Encoding]::new($false).GetBytes($memberManifest)
$memberManifestIdentity = Get-ByteIdentity -Bytes $memberManifestBytes

$packageValidation = [ordered]@{
    schema = 'sga3_expose_v_loop2_native_rights_curated_package_v1'
    status = 'PASS'
    producer_projection = [ordered]@{
        files = $expected.producer_tree_files
        manifest_rows = $expected.producer_manifest_rows
        validation_sha256 = Get-Sha256 -Path $producerValidationPath
        manifest_sha256 = Get-Sha256 -Path $producerManifestPath
        replay_errors = @()
    }
    independent_pdf_reference_render_audit = [ordered]@{
        status = [string]$independentAuditJson.status
        sha256 = Get-Sha256 -Path $auditPath
        delivered_pdf_sha256 = [string]$independentAuditJson.identities.delivered_pdf.sha256
        producer_stable_during_audit = [bool]$independentAuditJson.producer_snapshot.stable_during_final_audit
    }
    public_reader = [ordered]@{
        pdf_bytes = $pdfItem.Length
        pdf_sha256 = $pdfSha
        pages = $expected.pdf_pages
        master_bytes = $texItem.Length
        master_sha256 = $texSha
        named_destinations = $expected.destinations
        goto_actions = $expected.goto_actions
        targets = $expected.targets
        edges = $expected.edges
        native_diagrams = $expected.diagrams
        raster_image_objects = 0
    }
    rights_boundary = [ordered]@{
        source_pixel_files_public = 0
        rights_blocked_witnesses = $rightsRows.Count
        rights_metadata_rows = $rightsRows.Count
        witness_replay_errors = @()
    }
    archive_members = [ordered]@{
        represented_rows = $memberRows.Count
        manifest_sha256 = $memberManifestIdentity.sha256
        source_pixel_members = 0
    }
    errors = @()
}
$packageValidationText =
    ($packageValidation | ConvertTo-Json -Depth 20) + "`n"
$packageValidationBytes =
    [System.Text.UTF8Encoding]::new($false).GetBytes($packageValidationText)

$zipPath = Join-Path $output $zipOutputName
$zipStream = [System.IO.File]::Open(
    $zipPath,
    [System.IO.FileMode]::CreateNew,
    [System.IO.FileAccess]::ReadWrite,
    [System.IO.FileShare]::None
)
$archive = [System.IO.Compression.ZipArchive]::new(
    $zipStream,
    [System.IO.Compression.ZipArchiveMode]::Create,
    $false
)
try {
    foreach ($member in $memberSources) {
        Add-ZipBytes -Archive $archive -EntryName $member.entry_name `
            -Bytes ([System.IO.File]::ReadAllBytes($member.source_path))
    }
    Add-ZipBytes -Archive $archive -EntryName $rightsCsvName `
        -Bytes ([System.IO.File]::ReadAllBytes($rightsCsvPath))
    Add-ZipBytes -Archive $archive -EntryName $rightsJsonlName `
        -Bytes ([System.IO.File]::ReadAllBytes($rightsJsonlPath))
    Add-ZipBytes -Archive $archive -EntryName 'ARCHIVE_PACKAGE_README.md' `
        -Bytes $packageReadmeBytes
    Add-ZipBytes -Archive $archive -EntryName 'PACKAGE_MEMBER_MANIFEST.csv' `
        -Bytes $memberManifestBytes
    Add-ZipBytes -Archive $archive -EntryName 'PACKAGE_VALIDATION.json' `
        -Bytes $packageValidationBytes
}
finally {
    $archive.Dispose()
    $zipStream.Dispose()
}

$zipRead = [System.IO.Compression.ZipFile]::OpenRead($zipPath)
try {
    $zipNames = [System.Collections.Generic.HashSet[string]]::new(
        [System.StringComparer]::Ordinal
    )
    $zipErrors = [System.Collections.Generic.List[string]]::new()
    foreach ($entry in $zipRead.Entries) {
        if (
            [string]::IsNullOrWhiteSpace($entry.FullName) -or
            $entry.FullName.StartsWith('/') -or
            $entry.FullName.StartsWith('\') -or
            $entry.FullName -match '^[A-Za-z]:' -or
            ($entry.FullName -split '/') -contains '..'
        ) {
            $zipErrors.Add("unsafe:$($entry.FullName)")
        }
        if (-not $zipNames.Add($entry.FullName)) {
            $zipErrors.Add("duplicate:$($entry.FullName)")
        }
        if ($entry.FullName.StartsWith('source_png_witness/', [System.StringComparison]::Ordinal)) {
            $zipErrors.Add("rights-held-pixel:$($entry.FullName)")
        }
        $entryStream = $entry.Open()
        try {
            $sink = [System.IO.Stream]::Null
            $entryStream.CopyTo($sink)
        }
        finally {
            $entryStream.Dispose()
        }
    }
    if ($zipErrors.Count -ne 0) {
        throw "ZIP replay errors: $($zipErrors -join ', ')"
    }
}
finally {
    $zipRead.Dispose()
}

$readme = @"
# SGA 3 Expose V English Loop 2 native-diagram reader

This compact package publishes the bounded Expose V Loop 2 successor to the
earlier Loop 1 freeze3 reader. All 66 temporary diagram images have been
replaced by native TikZ/TikZ-cd sources. The reader contains no raster image
objects.

## Direct files

- `$pdfOutputName`: 51-page working reader.
- `$texOutputName`: directly editable master TeX.
- `$zipOutputName`: self-contained source, native diagrams, machine controls,
  public build evidence, and project-generated render QA.
- `$rightsCsvName` and `$rightsJsonlName`: public metadata for 66
  source-PDF-derived witnesses whose pixel files are withheld pending an
  affirmative rights decision.

## Verified surface

- 350 named destinations and 411 internal GoTo actions;
- 273/273 compiled reference targets;
- 333/333 semantic reference edges backed by PDF actions;
- 66/66 native diagram sources and invocations;
- zero direct raster includes and zero PDF image-paint operators;
- 51/51 fresh page renders and six contact sheets reviewed.

## Authority, attribution, and limits

The controlling source is Polo--Gille `Exp5-13oct24.pdf`, 439,522 bytes,
SHA-256 `9198200633F929FE1822520371A9200DA4F8CF2513EFAB3D6A0C7E9330DB84CF`.
It is identified but not redistributed.

Jacob Reinhold's public `jcreinhold/sga` English Markdown at revision
`e7a259f3f8608ad3edf9bf6eead3fd504dd2d23e` was credited comparison and
drafting material under his stated CC BY 4.0 license. It is not source
authority or independent corroboration.

This is a bounded machine-assisted working translation and reference-linked
reader. It does not complete SGA 3: Exposes VI--XXVI remain untranslated.
It is not a critical edition, mathematical certification, independent human
peer review, blanket rights determination, or accessibility certification.
"@
[System.IO.File]::WriteAllText(
    (Join-Path $output 'README.md'),
    $readme.Replace("`r`n", "`n"),
    [System.Text.UTF8Encoding]::new($false)
)

$outerValidation = [ordered]@{
    schema = 'sga3_expose_v_loop2_native_compact_release_v1'
    status = 'PASS'
    source_projection = [ordered]@{
        identity = 'producer_projection_r2_freeze2'
        files = $expected.producer_tree_files
        manifest_rows = $expected.producer_manifest_rows
        manifest_sha256 = Get-Sha256 -Path $producerManifestPath
        validation_sha256 = Get-Sha256 -Path $producerValidationPath
        replay_errors = @()
    }
    independent_audit = [ordered]@{
        status = [string]$independentAuditJson.status
        sha256 = Get-Sha256 -Path $auditPath
    }
    reader = [ordered]@{
        pdf = $pdfOutputName
        pdf_bytes = $pdfItem.Length
        pdf_sha256 = $pdfSha
        pages = $expected.pdf_pages
        tex = $texOutputName
        tex_bytes = $texItem.Length
        tex_sha256 = $texSha
    }
    rights = [ordered]@{
        source_pixels_in_release = 0
        rights_blocked_metadata_rows = $rightsRows.Count
        rights_csv_sha256 = Get-Sha256 -Path $rightsCsvPath
        rights_jsonl_sha256 = Get-Sha256 -Path $rightsJsonlPath
    }
    archive = [ordered]@{
        path = $zipOutputName
        bytes = (Get-Item -LiteralPath $zipPath).Length
        sha256 = Get-Sha256 -Path $zipPath
        members = $memberRows.Count + 2
        represented_members = $memberRows.Count
        source_pixel_members = 0
    }
    errors = @()
}
$outerValidationText = ($outerValidation | ConvertTo-Json -Depth 20) + "`n"
[System.IO.File]::WriteAllText(
    (Join-Path $output $releaseValidationName),
    $outerValidationText,
    [System.Text.UTF8Encoding]::new($false)
)

$outerFiles = @(
    Get-ChildItem -LiteralPath $output -File |
        Where-Object { $_.Name -ne $shaManifestName } |
        Sort-Object Name
)
$outerRows = foreach ($file in $outerFiles) {
    [pscustomobject][ordered]@{
        relative_path = $file.Name
        bytes = [string]$file.Length
        sha256 = Get-Sha256 -Path $file.FullName
        role = switch ($file.Name) {
            $pdfOutputName { 'reader_pdf' }
            $texOutputName { 'primary_editable_tex' }
            $zipOutputName { 'grouped_source_and_evidence' }
            $rightsCsvName { 'rights_blocked_metadata' }
            $rightsJsonlName { 'rights_blocked_metadata' }
            $releaseValidationName { 'release_validation' }
            default { 'documentation' }
        }
        scope = 'SGA3 complete Expose V Loop 2 native-diagram working checkpoint'
        status = 'bounded_working_reader_not_complete_sga3'
    }
}
$outerCsv = ConvertTo-SafeCsv -Rows @($outerRows)
[System.IO.File]::WriteAllText(
    (Join-Path $output $shaManifestName),
    $outerCsv,
    [System.Text.UTF8Encoding]::new($false)
)

$finalFiles = @(Get-ChildItem -LiteralPath $output -File | Sort-Object Name)
if ($finalFiles.Count -ne 8) {
    throw "Expected 8 compact outer files, found $($finalFiles.Count)."
}

$result = [ordered]@{
    status = 'PASS'
    output_root = $output
    outer_files = $finalFiles.Count
    outer_bytes = ($finalFiles | Measure-Object Length -Sum).Sum
    reader_pdf_sha256 = $pdfSha
    reader_tex_sha256 = $texSha
    archive_sha256 = Get-Sha256 -Path $zipPath
    archive_members = $memberRows.Count + 2
    rights_blocked_witnesses = $rightsRows.Count
    source_pixel_files_public = 0
}
$result | ConvertTo-Json -Depth 10
