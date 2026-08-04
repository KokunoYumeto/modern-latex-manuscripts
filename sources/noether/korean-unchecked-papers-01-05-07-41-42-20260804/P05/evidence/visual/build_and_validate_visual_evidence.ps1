$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

$visualDir = $PSScriptRoot
$jsonlPath = Join-Path $visualDir 'VISUAL_EVIDENCE.jsonl'
$csvPath = Join-Path $visualDir 'VISUAL_EVIDENCE.csv'
$reportPath = Join-Path $visualDir 'VISUAL_EVIDENCE_VALIDATION_REPORT.json'
$utf8NoBom = [System.Text.UTF8Encoding]::new($false)

function Get-FileSha256([string]$Path) {
    return (Get-FileHash -LiteralPath $Path -Algorithm SHA256).Hash
}

# No scan, crop, screenshot, render, contact sheet, segmentation image, or overlay
# was used or created in this translation-only unit. Keep the empty record set explicit.
$records = @()
$csvHeader = 'visual_id,evidence_type,parent_path,parent_file_sha256,page_number,coordinate_system,bbox_x,bbox_y,bbox_width,bbox_height,bbox_units,width_px,height_px,dpi,rotation_degrees,image_sha256,linked_structural_ids_json,linked_tex_units_json,qa_state,review_state,rights_basis,publication_disposition,supersedes_visual_id,record_sha256'

[System.IO.File]::WriteAllText($jsonlPath, '', $utf8NoBom)
[System.IO.File]::WriteAllText($csvPath, $csvHeader + [char]13 + [char]10, $utf8NoBom)

$errors = [System.Collections.Generic.List[string]]::new()
$jsonLines = @([System.IO.File]::ReadAllLines($jsonlPath, $utf8NoBom) | Where-Object { -not [string]::IsNullOrWhiteSpace($_) })
if ($jsonLines.Count -ne 0) {
    $errors.Add("expected zero JSONL records, found $($jsonLines.Count)")
}
$csvLines = [System.IO.File]::ReadAllLines($csvPath, $utf8NoBom)
if ($csvLines.Count -ne 1 -or $csvLines[0] -ne $csvHeader) {
    $errors.Add('zero-record CSV projection does not contain exactly the documented header')
}

$report = [ordered]@{
    schema = 'VISUAL_EVIDENCE.schema.json'
    builder_validator = 'build_and_validate_visual_evidence.ps1'
    status = if ($errors.Count -eq 0) { 'pass' } else { 'fail' }
    record_count = 0
    source_page_count = 0
    source_crop_count = 0
    equation_crop_count = 0
    diagram_crop_count = 0
    target_render_count = 0
    contact_sheet_count = 0
    before_after_count = 0
    segmentation_artifact_count = 0
    model_overlay_count = 0
    total_image_bytes = 0
    rights_disposition_totals = [ordered]@{
        public_safe = 0
        rights_blocked = 0
        private_excluded = 0
        pending = 0
    }
    jsonl_sha256 = Get-FileSha256 $jsonlPath
    csv_sha256 = Get-FileSha256 $csvPath
    errors = @($errors)
    continuation_cursor = 'No visual evidence exists; await independent checker without rendering in the producer lane.'
    scope_note = 'Explicit zero inventory. No visual QA, rendering, source images, or rights determination was performed.'
}
[System.IO.File]::WriteAllText($reportPath, ($report | ConvertTo-Json -Depth 8), $utf8NoBom)
if ($errors.Count -gt 0) {
    throw "Visual-evidence validation failed: $($errors -join '; ')"
}
Write-Output ($report | ConvertTo-Json -Compress -Depth 8)
