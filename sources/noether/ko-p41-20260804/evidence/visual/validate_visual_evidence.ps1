$ErrorActionPreference = 'Stop'
$schemaPath = Join-Path $PSScriptRoot 'VISUAL_EVIDENCE_SCHEMA.json'
$jsonlPath = Join-Path $PSScriptRoot 'visual_evidence_index.jsonl'
$csvPath = Join-Path $PSScriptRoot 'visual_evidence_index.csv'
$errors = [System.Collections.Generic.List[string]]::new()
try { $schema = Get-Content -LiteralPath $schemaPath -Raw -Encoding UTF8 | ConvertFrom-Json } catch { $errors.Add("schema parse failure: $($_.Exception.Message)") }
$lines = @(Get-Content -LiteralPath $jsonlPath -Encoding UTF8 | Where-Object { $_.Length -gt 0 })
foreach ($line in $lines) { try { $null = $line | ConvertFrom-Json } catch { $errors.Add("JSONL parse failure: $($_.Exception.Message)") } }
$expectedHeader = 'visual_id,work_id,visual_type,parent_scan_path,parent_scan_sha256,source_page,bbox_x,bbox_y,bbox_width,bbox_height,coordinate_basis,width_px,height_px,dpi,rotation_degrees,image_path,image_sha256,linked_structural_ids,linked_tex_units,qa_state,review_state,rights_basis,publication_disposition,supersession_state,continuation_cursor'
$csvLines = @(Get-Content -LiteralPath $csvPath -Encoding UTF8)
if ($csvLines.Count -ne 1) { $errors.Add("zero-record CSV must contain exactly one header line; found $($csvLines.Count)") }
elseif ($csvLines[0] -ne $expectedHeader) { $errors.Add('CSV header mismatch') }
$report = [ordered]@{
    schema_version = '1.0.0'
    validator = 'validate_visual_evidence.ps1'
    status = $(if ($errors.Count -eq 0) { 'PASS' } else { 'FAIL' })
    record_count = $lines.Count
    image_file_count = 0
    source_image_count = 0
    target_render_count = 0
    rights_cleared_count = 0
    rights_blocked_count = 0
    publication_included_count = 0
    continuation_cursor = $null
    errors = @($errors)
    validation_scope = 'Schema parse plus explicit empty JSONL and header-only CSV inventory.'
    excluded_scope = 'No images were used or created; no visual QA, rendering, rights clearance, or publication claim.'
}
$report | ConvertTo-Json -Depth 5
if ($errors.Count -gt 0) { exit 1 }
