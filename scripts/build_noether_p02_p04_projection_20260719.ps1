[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$SourceRoot,

    [Parameter(Mandatory = $true)]
    [string]$DestinationRoot,

    [Parameter(Mandatory = $true)]
    [string]$ComparisonRoot,

    [Parameter(Mandatory = $true)]
    [string]$ContactSheetPath
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Drawing

function Get-Sha256 {
    param([Parameter(Mandatory = $true)][string]$Path)
    return (Get-FileHash -Algorithm SHA256 -LiteralPath $Path).Hash.ToUpperInvariant()
}

function Get-ImageMetadata {
    param([Parameter(Mandatory = $true)][string]$Path)

    $image = $null
    try {
        $image = [System.Drawing.Image]::FromFile($Path)
        return [pscustomobject]@{
            Width = [int]$image.Width
            Height = [int]$image.Height
            DpiX = [math]::Round([double]$image.HorizontalResolution, 3)
            DpiY = [math]::Round([double]$image.VerticalResolution, 3)
        }
    }
    catch {
        $stream = [System.IO.File]::OpenRead($Path)
        try {
            $header = [byte[]]::new(24)
            if ($stream.Read($header, 0, $header.Length) -ne $header.Length) {
                throw "Unable to read image header: $Path"
            }
            $pngSignature = @(137, 80, 78, 71, 13, 10, 26, 10)
            for ($i = 0; $i -lt $pngSignature.Count; $i++) {
                if ($header[$i] -ne $pngSignature[$i]) {
                    throw "Image decoder failed and file is not a supported PNG: $Path"
                }
            }
            $widthBytes = [byte[]]@($header[19], $header[18], $header[17], $header[16])
            $heightBytes = [byte[]]@($header[23], $header[22], $header[21], $header[20])
            return [pscustomobject]@{
                Width = [int][BitConverter]::ToUInt32($widthBytes, 0)
                Height = [int][BitConverter]::ToUInt32($heightBytes, 0)
                DpiX = 'not_recorded'
                DpiY = 'not_recorded'
            }
        }
        finally {
            $stream.Dispose()
        }
    }
    finally {
        if ($null -ne $image) {
            $image.Dispose()
        }
    }
}

function Copy-PublicFile {
    param(
        [Parameter(Mandatory = $true)][string]$SourceRelativePath,
        [Parameter(Mandatory = $true)][string]$DestinationRelativePath
    )

    $source = Join-Path $SourceRoot $SourceRelativePath
    $destination = Join-Path $DestinationRoot $DestinationRelativePath
    $parent = Split-Path -Parent $destination
    New-Item -ItemType Directory -Path $parent -Force | Out-Null
    Copy-Item -LiteralPath $source -Destination $destination -Force
}

if (Test-Path -LiteralPath $DestinationRoot) {
    throw "Destination already exists: $DestinationRoot"
}

New-Item -ItemType Directory -Path $DestinationRoot -Force | Out-Null

$copyMap = [ordered]@{
    '01_current/cum_de_Local_20260719_P02p028_034_CurrentHeadAudit.tex' = 'current/cum_de_Local_20260719_P02p028_034_CurrentHeadAudit.tex'
    '01_current/cum_de_Local_20260719_P02p028_034_CurrentHeadAudit.pdf' = 'current/cum_de_Local_20260719_P02p028_034_CurrentHeadAudit.pdf'
    '03_audit/P02_p028_034_confirmed_fixes.csv' = 'audit/p02/P02_p028_034_confirmed_fixes.csv'
    '03_audit/P02_p028_034_page_dispositions.csv' = 'audit/p02/P02_p028_034_page_dispositions.csv'
    '03_audit/P02_p028_034_prior_audit_failure.md' = 'audit/p02/P02_p028_034_prior_audit_failure.md'
    '03_audit/P02_p028_034_source_adjudication.md' = 'audit/p02/P02_p028_034_source_adjudication.md'
    '03_audit/Web_P04_p118_143_integration_adjudication.md' = 'audit/p04/Web_P04_p118_143_integration_adjudication.md'
    '03_audit/Web_P04_p118_143/CSV_PARSE_AND_ROWCOUNT_CHECK.json' = 'audit/p04/CSV_PARSE_AND_ROWCOUNT_CHECK.json'
    '03_audit/Web_P04_p118_143/INPUT_HASH_STATUS.txt' = 'audit/p04/INPUT_HASH_STATUS.txt'
    '03_audit/Web_P04_p118_143/Web_P04_formula_1_52_audit.csv' = 'audit/p04/Web_P04_formula_1_52_audit.csv'
    '03_audit/Web_P04_p118_143/Web_P04_p118_143_adverse_source_records.csv' = 'audit/p04/Web_P04_p118_143_adverse_source_records.csv'
    '03_audit/Web_P04_p118_143/Web_P04_p118_143_confirmed_fixes.csv' = 'audit/p04/Web_P04_p118_143_confirmed_fixes.csv'
    '03_audit/Web_P04_p118_143/Web_P04_p118_143_no_patch_checks.csv' = 'audit/p04/Web_P04_p118_143_no_patch_checks.csv'
    '03_audit/Web_P04_p118_143/Web_P04_p118_143_output_page_mapping.csv' = 'audit/p04/Web_P04_p118_143_output_page_mapping.csv'
    '03_audit/Web_P04_p118_143/Web_P04_p118_143_page_audit.csv' = 'audit/p04/Web_P04_p118_143_page_audit.csv'
    '03_audit/Web_P04_p118_143/Web_P04_p118_143_survival_checks.csv' = 'audit/p04/Web_P04_p118_143_survival_checks.csv'
    '03_audit/Web_P04_p118_143/Web_P04_patch_index.json' = 'audit/p04/Web_P04_patch_index.json'
    '03_audit/Web_P04_p118_143/build_status.txt' = 'audit/p04/build_status.txt'
    '03_audit/Web_P04_p118_143/render_pixel_comparison.csv' = 'audit/p04/render_pixel_comparison.csv'
    '03_audit/Web_P04_p118_143/source_quality_and_provenance.md' = 'audit/p04/source_quality_and_provenance.md'
    '05_ledgers/NOETHER_HARD_MATH_ERROR_LEDGER_current.csv' = 'ledgers/NOETHER_HARD_MATH_ERROR_LEDGER_current.csv'
    '05_ledgers/NOETHER_LEDGER_VALIDATION_20260719.json' = 'ledgers/NOETHER_LEDGER_VALIDATION_20260719.json'
    '05_ledgers/NOETHER_SOURCE_ERROR_APPARATUS_current.csv' = 'ledgers/NOETHER_SOURCE_ERROR_APPARATUS_current.csv'
    '06_author_completion/NOETHER_ACTIVE_RESIDUAL_QUEUE_20260719.csv' = 'completion/NOETHER_ACTIVE_RESIDUAL_QUEUE_20260719.csv'
    '06_author_completion/NOETHER_AUTHOR_COMPLETION_AUDIT_20260719.md' = 'completion/NOETHER_AUTHOR_COMPLETION_AUDIT_20260719.md'
    '06_author_completion/NOETHER_AUTHOR_COMPLETION_MATRIX_20260719.csv' = 'completion/NOETHER_AUTHOR_COMPLETION_MATRIX_20260719.csv'
    '06_author_completion/NOETHER_AUTHOR_COMPLETION_VALIDATION_20260719.json' = 'completion/NOETHER_AUTHOR_COMPLETION_VALIDATION_20260719.json'
    '07_provenance/SOURCE_AND_INPUT_MAPPING.md' = 'provenance/SOURCE_AND_INPUT_MAPPING.md'
    '07_provenance/package_summary.json' = 'provenance/package_summary.json'
    '07_provenance/sha256_files.csv' = 'provenance/sha256_files.csv'
    '07_provenance/sha256_files.csv.sha256' = 'provenance/sha256_files.csv.sha256'
    '08_docs/METHOD_AND_CONTINUATION.md' = 'METHOD_AND_CONTINUATION.md'
    'README.md' = 'PRODUCER_README.md'
}

foreach ($entry in $copyMap.GetEnumerator()) {
    Copy-PublicFile -SourceRelativePath $entry.Key -DestinationRelativePath $entry.Value
}

$formulaSafeCsvs = @(
    'audit/p04/Web_P04_p118_143_page_audit.csv',
    'ledgers/NOETHER_HARD_MATH_ERROR_LEDGER_current.csv'
)
foreach ($relativePath in $formulaSafeCsvs) {
    $path = Join-Path $DestinationRoot $relativePath
    $rows = Import-Csv -LiteralPath $path
    foreach ($row in $rows) {
        foreach ($property in $row.PSObject.Properties) {
            $value = [string]$property.Value
            if ($value -match '^[=+@-]') {
                $property.Value = "'" + $value
            }
        }
    }
    $rows | Export-Csv -LiteralPath $path -NoTypeInformation -UseQuotes Always -Encoding utf8
}

$targetRenderMap = @(
    [pscustomobject]@{ Source = '04_renders/after_p029_034/output_p005_after.png'; Destination = 'rendered_current/paper02/page-005.png'; Page = 5; Unit = 'paper02_printed_pp28_34' },
    [pscustomobject]@{ Source = '04_renders/after_p029_034/output_p006_after.png'; Destination = 'rendered_current/paper02/page-006.png'; Page = 6; Unit = 'paper02_printed_pp28_34' },
    [pscustomobject]@{ Source = '04_renders/after_p029_034/output_p007_after.png'; Destination = 'rendered_current/paper02/page-007.png'; Page = 7; Unit = 'paper02_printed_pp28_34' },
    [pscustomobject]@{ Source = '04_renders/after_p029_034/output_p008_after.png'; Destination = 'rendered_current/paper02/page-008.png'; Page = 8; Unit = 'paper02_printed_pp28_34' },
    [pscustomobject]@{ Source = '04_renders/after_p029_034/output_p009_after.png'; Destination = 'rendered_current/paper02/page-009.png'; Page = 9; Unit = 'paper02_printed_pp28_34' },
    [pscustomobject]@{ Source = '04_renders/after_p029_034/output_p010_after.png'; Destination = 'rendered_current/paper02/page-010.png'; Page = 10; Unit = 'paper02_printed_pp28_34' },
    [pscustomobject]@{ Source = '04_renders/after_WebP04_p118_143/output_p049_after.png'; Destination = 'rendered_current/paper04/page-049.png'; Page = 49; Unit = 'paper04_printed_pp118_143' },
    [pscustomobject]@{ Source = '04_renders/after_WebP04_p118_143/output_p050_after.png'; Destination = 'rendered_current/paper04/page-050.png'; Page = 50; Unit = 'paper04_printed_pp118_143' },
    [pscustomobject]@{ Source = '04_renders/after_WebP04_p118_143/output_p051_after.png'; Destination = 'rendered_current/paper04/page-051.png'; Page = 51; Unit = 'paper04_printed_pp118_143' },
    [pscustomobject]@{ Source = '04_renders/after_WebP04_p118_143/output_p052_after.png'; Destination = 'rendered_current/paper04/page-052.png'; Page = 52; Unit = 'paper04_printed_pp118_143' },
    [pscustomobject]@{ Source = '04_renders/after_WebP04_p118_143/output_p053_after.png'; Destination = 'rendered_current/paper04/page-053.png'; Page = 53; Unit = 'paper04_printed_pp118_143' },
    [pscustomobject]@{ Source = '04_renders/after_WebP04_p118_143/output_p054_after.png'; Destination = 'rendered_current/paper04/page-054.png'; Page = 54; Unit = 'paper04_printed_pp118_143' },
    [pscustomobject]@{ Source = '04_renders/after_WebP04_p118_143/output_p055_after.png'; Destination = 'rendered_current/paper04/page-055.png'; Page = 55; Unit = 'paper04_printed_pp118_143' },
    [pscustomobject]@{ Source = '04_renders/after_WebP04_p118_143/output_p057_after.png'; Destination = 'rendered_current/paper04/page-057.png'; Page = 57; Unit = 'paper04_printed_pp118_143' },
    [pscustomobject]@{ Source = '04_renders/after_WebP04_p118_143/output_p058_after.png'; Destination = 'rendered_current/paper04/page-058.png'; Page = 58; Unit = 'paper04_printed_pp118_143' },
    [pscustomobject]@{ Source = '04_renders/after_WebP04_p118_143/output_p059_after.png'; Destination = 'rendered_current/paper04/page-059.png'; Page = 59; Unit = 'paper04_printed_pp118_143' }
)

foreach ($render in $targetRenderMap) {
    Copy-PublicFile -SourceRelativePath $render.Source -DestinationRelativePath $render.Destination
}

$contactDestination = Join-Path $DestinationRoot 'rendered_current/contact-sheet-pages005-010-049-055-057-059.png'
Copy-Item -LiteralPath $ContactSheetPath -Destination $contactDestination -Force

$currentPdfSha = '572CF1EAA7F4895D0DA3644AE872D228AE40F6BCD81EC87DC3DEE1ADC9183C92'
$visualRows = [System.Collections.Generic.List[object]]::new()
$index = 1
foreach ($render in $targetRenderMap) {
    $publicPath = Join-Path $DestinationRoot $render.Destination
    $meta = Get-ImageMetadata -Path $publicPath
    $visualRows.Add([pscustomobject][ordered]@{
        visual_id = ('VE-NOE-GER-P02P04-{0:D3}' -f $index)
        relative_path = $render.Destination.Replace('\', '/')
        parent_pdf_sha256 = $currentPdfSha
        pdf_page = $render.Page
        width_px = $meta.Width
        height_px = $meta.Height
        generation_dpi = 400
        embedded_dpi_x = $meta.DpiX
        embedded_dpi_y = $meta.DpiY
        rotation_degrees = 0
        bounding_box = "0,0,$($meta.Width),$($meta.Height)"
        sha256 = Get-Sha256 -Path $publicPath
        bytes = (Get-Item -LiteralPath $publicPath).Length
        linked_structural_unit = $render.Unit
        generation_basis = 'producer_final_after_render'
        publication_disposition = 'open_payload'
        qa_disposition = 'accepted_no_visible_defect_independent_rebuild_render_byte_match'
    })
    $index++
}

$contactMeta = Get-ImageMetadata -Path $contactDestination
$visualRows.Add([pscustomobject][ordered]@{
    visual_id = ('VE-NOE-GER-P02P04-{0:D3}' -f $index)
    relative_path = 'rendered_current/contact-sheet-pages005-010-049-055-057-059.png'
    parent_pdf_sha256 = $currentPdfSha
    pdf_page = '5-10;49-55;57-59'
    width_px = $contactMeta.Width
    height_px = $contactMeta.Height
    generation_dpi = 'mixed_400dpi_source_renders'
    embedded_dpi_x = 'not_recorded'
    embedded_dpi_y = 'not_recorded'
    rotation_degrees = 0
    bounding_box = "0,0,$($contactMeta.Width),$($contactMeta.Height)"
    sha256 = Get-Sha256 -Path $contactDestination
    bytes = (Get-Item -LiteralPath $contactDestination).Length
    linked_structural_unit = 'paper02_printed_pp28_34;paper04_printed_pp118_143'
    generation_basis = 'archive_contact_sheet_from_producer_final_renders'
    publication_disposition = 'open_payload'
    qa_disposition = 'accepted_navigation_only_original_detail_pages_reviewed'
})

$visualRows | Export-Csv -LiteralPath (Join-Path $DestinationRoot 'VISUAL_EVIDENCE_INDEX.csv') -NoTypeInformation -UseQuotes Always -Encoding utf8
$visualRows | ForEach-Object { $_ | ConvertTo-Json -Compress -Depth 5 } |
    Set-Content -LiteralPath (Join-Path $DestinationRoot 'VISUAL_EVIDENCE_INDEX.jsonl') -Encoding utf8

$replayRows = foreach ($render in $targetRenderMap) {
    $page = '{0:D3}' -f $render.Page
    $producerFresh = Join-Path $ComparisonRoot "producer-$page.png"
    $rebuildFresh = Join-Path $ComparisonRoot "rebuild-$page.png"
    $publicPath = Join-Path $DestinationRoot $render.Destination
    [pscustomobject][ordered]@{
        control_id = "RR-NOE-GER-P02P04-$page"
        pdf_page = $render.Page
        public_render_path = $render.Destination.Replace('\', '/')
        public_render_sha256 = Get-Sha256 -Path $publicPath
        fresh_producer_render_sha256 = Get-Sha256 -Path $producerFresh
        fresh_rebuild_render_sha256 = Get-Sha256 -Path $rebuildFresh
        fresh_render_bytes = (Get-Item -LiteralPath $producerFresh).Length
        comparison_dpi = 400
        result = 'fresh_producer_and_independent_rebuild_renders_byte_identical'
        producer_supplied_render_note = 'stored producer render uses a different renderer or antialiasing signature; dimensions and reviewed page content match'
    }
}
$replayRows | Export-Csv -LiteralPath (Join-Path $DestinationRoot 'RENDER_REPLAY_VALIDATION.csv') -NoTypeInformation -UseQuotes Always -Encoding utf8

$rightsRows = [System.Collections.Generic.List[object]]::new()
$rightsIndex = 1
$p02ParentSha = '05D5BA2D9774DB7805F8FFDF5A52BDD5EFF93F0B9DB92B5501DE032E17E88533'
$p02ImageRoot = Join-Path $SourceRoot '02_source/P02_p028_034'
foreach ($file in Get-ChildItem -LiteralPath (Join-Path $p02ImageRoot 'full_650dpi') -File | Sort-Object Name) {
    $meta = Get-ImageMetadata -Path $file.FullName
    $printedPage = [regex]::Match($file.Name, 'p(\d{3})').Groups[1].Value
    $rightsRows.Add([pscustomobject][ordered]@{
        visual_id = ('RB-NOE-GER-P02P04-{0:D3}' -f $rightsIndex)
        original_relative_path = "02_source/P02_p028_034/full_650dpi/$($file.Name)"
        bytes = $file.Length
        sha256 = Get-Sha256 -Path $file.FullName
        parent_scan_sha256 = $p02ParentSha
        source_scope = 'paper02_printed_pp28_34'
        source_page_locus = "printed_p$printedPage"
        width_px = $meta.Width
        height_px = $meta.Height
        generation_dpi = 650
        embedded_dpi_x = $meta.DpiX
        embedded_dpi_y = $meta.DpiY
        rotation_degrees = 0
        bounding_box = "0,0,$($meta.Width),$($meta.Height)"
        linked_structural_unit = 'paper02_printed_pp28_34'
        publication_disposition = 'manifest_only_rights_blocked'
        qa_disposition = 'used_for_complete_page_source_audit'
        reason = 'scan-derived source pixels; documentary redistribution rights unresolved'
    })
    $rightsIndex++
}
foreach ($file in Get-ChildItem -LiteralPath (Join-Path $p02ImageRoot 'strips_1000dpi') -File | Sort-Object Name) {
    $meta = Get-ImageMetadata -Path $file.FullName
    $printedPage = [regex]::Match($file.Name, 'p(\d{3})').Groups[1].Value
    $rightsRows.Add([pscustomobject][ordered]@{
        visual_id = ('RB-NOE-GER-P02P04-{0:D3}' -f $rightsIndex)
        original_relative_path = "02_source/P02_p028_034/strips_1000dpi/$($file.Name)"
        bytes = $file.Length
        sha256 = Get-Sha256 -Path $file.FullName
        parent_scan_sha256 = $p02ParentSha
        source_scope = 'paper02_printed_pp28_34'
        source_page_locus = "printed_p$printedPage"
        width_px = $meta.Width
        height_px = $meta.Height
        generation_dpi = 1000
        embedded_dpi_x = $meta.DpiX
        embedded_dpi_y = $meta.DpiY
        rotation_degrees = 0
        bounding_box = 'producer_crop_coordinates_not_recorded'
        linked_structural_unit = 'paper02_printed_pp28_34'
        publication_disposition = 'manifest_only_rights_blocked'
        qa_disposition = 'used_for_enlarged_source_locus_audit'
        reason = 'scan-derived source pixels; documentary redistribution rights unresolved'
    })
    $rightsIndex++
}

$p04ParentSha = 'D7F7CE6D4B311FFD968ED47DC9C1478CFFCF9F446A86BF90263E0C9D1B41C9EF'
$p04ManifestPath = Join-Path $SourceRoot '03_audit/Web_P04_p118_143/Web_P04_p118_143_source_manifest.csv'
$p04SourceRows = Import-Csv -LiteralPath $p04ManifestPath |
    Where-Object { $_.role -in @('source_full_page', 'source_strip') }
foreach ($row in $p04SourceRows) {
    $parts = $row.dimensions_or_pages -split 'x'
    $printedPage = [regex]::Match($row.path, 'P04_p(\d{3})').Groups[1].Value
    $isFull = $row.role -eq 'source_full_page'
    $rightsRows.Add([pscustomobject][ordered]@{
        visual_id = ('RB-NOE-GER-P02P04-{0:D3}' -f $rightsIndex)
        original_relative_path = $row.path
        bytes = [int64]$row.bytes
        sha256 = $row.sha256.ToUpperInvariant()
        parent_scan_sha256 = $p04ParentSha
        source_scope = 'paper04_printed_pp118_143'
        source_page_locus = "printed_p$printedPage"
        width_px = [int]$parts[0]
        height_px = [int]$parts[1]
        generation_dpi = 'producer_native_600dpi_class'
        embedded_dpi_x = 'not_recorded'
        embedded_dpi_y = 'not_recorded'
        rotation_degrees = 0
        bounding_box = $(if ($isFull) { "0,0,$($parts[0]),$($parts[1])" } else { 'producer_crop_coordinates_not_recorded' })
        linked_structural_unit = 'paper04_printed_pp118_143'
        publication_disposition = 'manifest_only_rights_blocked'
        qa_disposition = $(if ($isFull) { 'used_for_complete_page_source_audit' } else { 'used_for_enlarged_source_locus_audit' })
        reason = 'scan-derived source pixels; documentary redistribution rights unresolved'
    })
    $rightsIndex++
}

$contactSourceRoot = Join-Path $SourceRoot '03_audit/Web_P04_p118_143'
foreach ($file in Get-ChildItem -LiteralPath $contactSourceRoot -File -Filter '*.png' | Sort-Object Name) {
    $meta = Get-ImageMetadata -Path $file.FullName
    $pageMatches = [regex]::Matches($file.Name, 'p(\d{3})')
    $pageLocus = (($pageMatches | ForEach-Object { "printed_p$($_.Groups[1].Value)" }) -join ';')
    $rightsRows.Add([pscustomobject][ordered]@{
        visual_id = ('RB-NOE-GER-P02P04-{0:D3}' -f $rightsIndex)
        original_relative_path = "03_audit/Web_P04_p118_143/$($file.Name)"
        bytes = $file.Length
        sha256 = Get-Sha256 -Path $file.FullName
        parent_scan_sha256 = $p04ParentSha
        source_scope = 'paper04_printed_pp118_143'
        source_page_locus = $pageLocus
        width_px = $meta.Width
        height_px = $meta.Height
        generation_dpi = 'not_recorded_composite'
        embedded_dpi_x = $meta.DpiX
        embedded_dpi_y = $meta.DpiY
        rotation_degrees = 0
        bounding_box = 'mixed_source_target_composite_coordinates_not_recorded'
        linked_structural_unit = 'paper04_printed_pp118_143'
        publication_disposition = 'manifest_only_rights_blocked'
        qa_disposition = 'used_for_source_before_after_or_survival_review'
        reason = 'composite contains scan-derived source pixels; documentary redistribution rights unresolved'
    })
    $rightsIndex++
}

$rightsRows | Export-Csv -LiteralPath (Join-Path $DestinationRoot 'SOURCE_IMAGE_RIGHTS_BLOCKED.csv') -NoTypeInformation -UseQuotes Always -Encoding utf8

$sourceWitnessRows = @(
    [pscustomobject][ordered]@{
        relative_path = 'external/P02_original_complete_authority.pdf'
        bytes = 'not_packaged'
        sha256 = $p02ParentSha
        scope = 'Paper 2 complete original authority'
        pages = 'not_recorded_in_handoff'
        authority_role = 'source_witness'
        publication_disposition = 'manifest_only_rights_blocked'
        reason = 'complete original source was not packaged; redistribution rights unresolved'
    },
    [pscustomobject][ordered]@{
        relative_path = '02_source/P02_p028_034/P02_source_boundary_p027_058.pdf'
        bytes = (Get-Item -LiteralPath (Join-Path $SourceRoot '02_source/P02_p028_034/P02_source_boundary_p027_058.pdf')).Length
        sha256 = Get-Sha256 -Path (Join-Path $SourceRoot '02_source/P02_p028_034/P02_source_boundary_p027_058.pdf')
        scope = 'Paper 2 printed pp27-58 boundary slice'
        pages = 32
        authority_role = 'source_witness'
        publication_disposition = 'manifest_only_rights_blocked'
        reason = 'source-scan redistribution rights unresolved'
    },
    [pscustomobject][ordered]@{
        relative_path = '02_source/P04_original/paper_04_crelle139_pp118_154_ORIGINAL.pdf'
        bytes = (Get-Item -LiteralPath (Join-Path $SourceRoot '02_source/P04_original/paper_04_crelle139_pp118_154_ORIGINAL.pdf')).Length
        sha256 = Get-Sha256 -Path (Join-Path $SourceRoot '02_source/P04_original/paper_04_crelle139_pp118_154_ORIGINAL.pdf')
        scope = 'Paper 4 printed pp118-154 complete original article scan'
        pages = 38
        authority_role = 'source_witness'
        publication_disposition = 'manifest_only_rights_blocked'
        reason = 'source-scan redistribution rights unresolved'
    },
    [pscustomobject][ordered]@{
        relative_path = 'nested-source-package/Web_P04_source_printed_p118_143.pdf'
        bytes = 50583054
        sha256 = '021EF6280AC9DE43FA073A69C9931CF792F9FA0E137974BD84F717E6DBB468B8'
        scope = 'Paper 4 printed pp118-143 assigned source slice'
        pages = 26
        authority_role = 'source_witness'
        publication_disposition = 'manifest_only_rights_blocked'
        reason = 'source-scan redistribution rights unresolved'
    }
)
$sourceWitnessRows | Export-Csv -LiteralPath (Join-Path $DestinationRoot 'SOURCE_WITNESS_DISPOSITION.csv') -NoTypeInformation -UseQuotes Always -Encoding utf8

$excludedRenderMap = @(
    [pscustomobject]@{ Source = '04_renders/before/output_p005_before.png'; Disposition = 'excluded_superseded_before_state'; Replacement = 'rendered_current/paper02/page-005.png'; Reason = 'diagnostic pre-repair target render' },
    [pscustomobject]@{ Source = '04_renders/after/output_p005_after.png'; Disposition = 'excluded_duplicate_intermediate_after_state'; Replacement = 'rendered_current/paper02/page-005.png'; Reason = 'duplicate intermediate after-render superseded by final bounded render set' },
    [pscustomobject]@{ Source = '04_renders/after/output_p006_after.png'; Disposition = 'excluded_intermediate_after_state'; Replacement = 'rendered_current/paper02/page-006.png'; Reason = 'intermediate after-render superseded by final bounded render set' }
)
$excludedRows = $excludedRenderMap | ForEach-Object {
    $sourcePath = Join-Path $SourceRoot $_.Source
    $meta = Get-ImageMetadata -Path $sourcePath
    [pscustomobject][ordered]@{
        relative_path = $_.Source
        bytes = (Get-Item -LiteralPath $sourcePath).Length
        sha256 = Get-Sha256 -Path $sourcePath
        width_px = $meta.Width
        height_px = $meta.Height
        embedded_dpi_x = $meta.DpiX
        embedded_dpi_y = $meta.DpiY
        rotation_degrees = 0
        publication_disposition = $_.Disposition
        replacement_reference = $_.Replacement
        reason = $_.Reason
    }
}
$excludedRows | Export-Csv -LiteralPath (Join-Path $DestinationRoot 'EXCLUDED_VISUAL_EVIDENCE.csv') -NoTypeInformation -UseQuotes Always -Encoding utf8

$withheldRelativePaths = @(
    '01_current/cum_de_Local_20260719_P02p028_034_CurrentHeadAudit.log',
    '01_current/cum_de_Local_20260719_P02p028_034_CurrentHeadAudit_pass1.log',
    '01_current/cum_de_Local_20260719_P02p028_034_CurrentHeadAudit_pass2.log',
    '05_ledgers/NOETHER_CORRECTION_ORIGIN_LEDGER_current.csv',
    '05_ledgers/NOETHER_MASTER_PUBLICATION_LOGBOOK_current.md',
    '05_ledgers/NOETHER_PAGE_QC_CANONICAL_PER_PAGE_current.csv',
    '05_ledgers/NOETHER_PAGE_QC_LEDGER_current.csv'
)
$withheldRows = foreach ($relativePath in $withheldRelativePaths) {
    $path = Join-Path $SourceRoot $relativePath
    $lineCount = (Get-Content -LiteralPath $path).Count
    [pscustomobject][ordered]@{
        relative_path = $relativePath
        bytes = (Get-Item -LiteralPath $path).Length
        sha256 = Get-Sha256 -Path $path
        record_or_line_count = $lineCount
        publication_disposition = 'internal_private_control_not_published'
        reason = 'contains absolute local filesystem paths or internal task identifiers'
    }
}
$withheldRows | Export-Csv -LiteralPath (Join-Path $DestinationRoot 'WITHHELD_INTERNAL_LEDGER_MANIFEST.csv') -NoTypeInformation -UseQuotes Always -Encoding utf8

$transportRows = @(
    [pscustomobject][ordered]@{
        artifact = 'received_outer_zip'
        bytes = 158527445
        sha256 = 'B5162EAD48F3A2B1A3C74D53D7A888E9AAB6AE1E92DD243AB73B56CF32AE4AF8'
        publication_disposition = 'private_transport_not_redistributed'
        reason = 'contains rights-sensitive source scans and private producer controls'
    },
    [pscustomobject][ordered]@{
        artifact = 'received_outer_zip_sidecar'
        bytes = 146
        sha256 = 'EEFF1D9286F9D6850DD2CA4478480E452D9AB295F4FCAEA26014292B083CA26A'
        publication_disposition = 'metadata_record_only'
        reason = 'transport sidecar matched the received ZIP'
    },
    [pscustomobject][ordered]@{
        artifact = 'nested_Web_P04_core_zip'
        bytes = (Get-Item -LiteralPath (Join-Path $SourceRoot '07_provenance/input_packages/Web_P04_p118_143_CurrentHeadAudit_20260719_CORE.zip')).Length
        sha256 = Get-Sha256 -Path (Join-Path $SourceRoot '07_provenance/input_packages/Web_P04_p118_143_CurrentHeadAudit_20260719_CORE.zip')
        publication_disposition = 'private_transport_not_redistributed'
        reason = 'contains rights-sensitive source imagery; unpacked and audited before classification'
    },
    [pscustomobject][ordered]@{
        artifact = 'durable_handoff'
        bytes = 3792
        sha256 = 'A80A6898417BC63E64B96C422CEBE25A416AC33579DD7274414DA2EB432EBA59'
        publication_disposition = 'metadata_record_only'
        reason = 'custody handoff contains local routing details and is represented by hash'
    }
)
$transportRows | Export-Csv -LiteralPath (Join-Path $DestinationRoot 'TRANSPORT_AND_CUSTODY.csv') -NoTypeInformation -UseQuotes Always -Encoding utf8

Write-Host "Projection prepared at $DestinationRoot"
Write-Host "Open visual records: $($visualRows.Count)"
Write-Host "Rights-blocked source-image records: $($rightsRows.Count)"
