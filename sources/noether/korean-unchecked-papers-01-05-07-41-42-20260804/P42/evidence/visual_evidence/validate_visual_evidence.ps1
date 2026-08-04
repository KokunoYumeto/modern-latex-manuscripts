param()

$ErrorActionPreference = 'Stop'
$utf8 = [System.Text.UTF8Encoding]::new($false)
$jsonlPath = Join-Path $PSScriptRoot 'VISUAL_EVIDENCE_INDEX.jsonl'
$csvPath = Join-Path $PSScriptRoot 'VISUAL_EVIDENCE_INDEX.csv'
$reportPath = Join-Path $PSScriptRoot 'VISUAL_EVIDENCE_INDEX_VALIDATION_REPORT.json'
$magick = 'C:\Program Files\ImageMagick-7.1.2-Q16\magick.exe'
$errors = [System.Collections.Generic.List[string]]::new()
$records = [System.Collections.Generic.List[object]]::new()
$lineNo = 0
foreach ($line in [System.IO.File]::ReadAllLines($jsonlPath, $utf8)) {
  $lineNo++
  if (-not $line.Trim()) { $errors.Add("blank JSONL record at line $lineNo"); continue }
  try { $record = $line | ConvertFrom-Json -Depth 20 } catch { $errors.Add("invalid JSON at line $lineNo"); continue }
  $records.Add($record)
}
$seen = @{}
foreach ($record in $records) {
  if ($seen.ContainsKey($record.visual_id)) { $errors.Add("duplicate visual id $($record.visual_id)") } else { $seen[$record.visual_id] = $true }
  if (-not (Test-Path -LiteralPath $record.path)) { $errors.Add("missing image $($record.path)"); continue }
  $item = Get-Item -LiteralPath $record.path
  $hash = (Get-FileHash -LiteralPath $record.path -Algorithm SHA256).Hash
  if ($item.Length -ne $record.bytes) { $errors.Add("byte mismatch $($record.visual_id)") }
  if ($hash -ne $record.sha256) { $errors.Add("hash mismatch $($record.visual_id)") }
  $dimensions = & $magick identify -format '%w,%h' $record.path
  $parts = $dimensions -split ','
  if ([int]$parts[0] -ne $record.dimensions_pixels.width -or [int]$parts[1] -ne $record.dimensions_pixels.height) { $errors.Add("dimension mismatch $($record.visual_id)") }
}
$projection = foreach ($record in $records) {
  [pscustomobject]@{
    visual_id = $record.visual_id
    artifact_type = $record.artifact_type
    path = $record.path
    bytes = $record.bytes
    sha256 = $record.sha256
    width = $record.dimensions_pixels.width
    height = $record.dimensions_pixels.height
    dpi_x = $record.dpi.x
    dpi_y = $record.dpi.y
    rotation_degrees = $record.rotation_degrees
    linked_structural_ids = (@($record.linked_structural_ids) -join ';')
    linked_tex_units = (@($record.linked_tex_units) -join ';')
    qa_status = $record.qa_status
    review_status = $record.review_status
    rights_basis = $record.rights_basis
    publication_disposition = $record.publication_disposition
    continuation_cursor = $record.continuation_cursor
    supersession_state = $record.supersession_state
  }
}
$csvText = $projection | ConvertTo-Csv -NoTypeInformation
[System.IO.File]::WriteAllLines($csvPath, $csvText, $utf8)
$report = [ordered]@{
  status = $(if ($errors.Count -eq 0) { 'pass' } else { 'fail' })
  record_count = $records.Count
  image_count = @($records | Where-Object artifact_type -ne $null).Count
  total_bytes = [int64](($records | Measure-Object bytes -Sum).Sum)
  paper42_mathematical_visual_count = @($records | Where-Object { @($_.linked_tex_units).Count -gt 0 -or @($_.linked_structural_ids).Count -gt 0 }).Count
  rights_disposition_totals = [ordered]@{
    user_supplied_private = @($records | Where-Object rights_basis -like 'user-supplied*').Count
    public_eligible = @($records | Where-Object publication_disposition -notlike 'exclude*').Count
    public_excluded = @($records | Where-Object publication_disposition -like 'exclude*').Count
  }
  latest_visual_id = $(if ($records.Count) { $records[-1].visual_id } else { $null })
  errors = @($errors)
  validation_scope = 'file identity and metadata projection only; no source, translation, visual-quality, rights, or publication validation'
}
[System.IO.File]::WriteAllText($reportPath, ($report | ConvertTo-Json -Depth 8), $utf8)
if ($errors.Count -gt 0) { throw "visual evidence validation failed with $($errors.Count) errors" }
$report | ConvertTo-Json -Depth 8
