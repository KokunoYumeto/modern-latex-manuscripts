param(
  [Parameter(Mandatory = $true)]
  [string]$Freeze4Root,
  [Parameter(Mandatory = $true)]
  [string]$Freeze3Root,
  [string]$OutputPath = (Join-Path (Split-Path -Parent $PSScriptRoot) "manifests\source-intake\20260723_sga3_expose_v_loop2_freeze4_independent_audit.json")
)

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest
Add-Type -AssemblyName Microsoft.VisualBasic

$expected = [ordered]@{
  files = 298
  bytes = 27920910
  manifest_rows = 296
  manifest_bytes = 93001
  manifest_sha256 = "D3E936A9AD1EAF3ECC1AD46445135030863D0B97FB9FC880868A1DDFF876199E"
  validation_bytes = 5403
  validation_sha256 = "1111BE20138BD80F9837941E05A29432C02AA487B8E6C9E93FCB78AEA5E76C75"
  pdf_bytes = 361493
  pdf_sha256 = "E4682CBED71922AF8C1C2851D8B69F2CF6A1E089CC4CC52EDF0318708F65F6F2"
  tex_bytes = 7202
  tex_sha256 = "92AB24AB2E104618AB4E97AC4A2F23554BECB741258F7E9739EC463E6B99C37E"
  freeze3_identical_files = 294
  freeze3_changed_files = 4
}

$manifestRelativePath = "ZENODO_PAYLOAD_MANIFEST.csv"
$validationRelativePath = "PUBLIC_PROJECTION_VALIDATION.json"
$pdfRelativePath = "build/SGA3_Expose_V_English_Loop2_Native_ReferenceV2_00_23.pdf"
$texRelativePath = "tex/SGA3_Expose_V_English_Loop2_Native_ReferenceV2_00_23.tex"
$errors = [System.Collections.Generic.List[string]]::new()

function Get-Sha256 {
  param([Parameter(Mandatory)][string]$Path)
  return (Get-FileHash -LiteralPath $Path -Algorithm SHA256).Hash.ToUpperInvariant()
}

function Get-RelativePath {
  param(
    [Parameter(Mandatory)][string]$Root,
    [Parameter(Mandatory)][string]$Path
  )
  return [System.IO.Path]::GetRelativePath($Root, $Path).Replace("\", "/")
}

function Read-CsvRows {
  param([Parameter(Mandatory)][string]$Path)
  $parser = [Microsoft.VisualBasic.FileIO.TextFieldParser]::new($Path)
  try {
    $parser.TextFieldType = [Microsoft.VisualBasic.FileIO.FieldType]::Delimited
    $parser.SetDelimiters(",")
    $parser.HasFieldsEnclosedInQuotes = $true
    $rows = [System.Collections.Generic.List[object]]::new()
    while (-not $parser.EndOfData) {
      $rows.Add(@($parser.ReadFields()))
    }
    return @($rows)
  }
  finally {
    $parser.Dispose()
  }
}

function Test-FormulaTrigger {
  param([AllowEmptyString()][string]$Value)
  if ($null -eq $Value) {
    return $false
  }
  $trimmed = $Value.TrimStart()
  return $trimmed.Length -gt 0 -and $trimmed[0] -in @("=", "+", "-", "@")
}

foreach ($root in @($Freeze4Root, $Freeze3Root)) {
  if (-not (Test-Path -LiteralPath $root -PathType Container)) {
    throw "Missing required root: $root"
  }
}

$freeze4Files = @(Get-ChildItem -LiteralPath $Freeze4Root -File -Recurse)
$freeze4Map = @{}
$totalBytes = [int64]0
foreach ($file in $freeze4Files) {
  $relativePath = Get-RelativePath -Root $Freeze4Root -Path $file.FullName
  $freeze4Map[$relativePath] = [ordered]@{
    bytes = [int64]$file.Length
    sha256 = Get-Sha256 -Path $file.FullName
  }
  $totalBytes += [int64]$file.Length
}

if ($freeze4Files.Count -ne $expected.files) {
  $errors.Add("Tree file count: expected $($expected.files), got $($freeze4Files.Count)")
}
if ($totalBytes -ne $expected.bytes) {
  $errors.Add("Tree bytes: expected $($expected.bytes), got $totalBytes")
}

$manifestPath = Join-Path $Freeze4Root $manifestRelativePath
$validationPath = Join-Path $Freeze4Root $validationRelativePath
$pdfPath = Join-Path $Freeze4Root $pdfRelativePath
$texPath = Join-Path $Freeze4Root $texRelativePath
foreach ($required in @($manifestPath, $validationPath, $pdfPath, $texPath)) {
  if (-not (Test-Path -LiteralPath $required -PathType Leaf)) {
    $errors.Add("Missing required file: $required")
  }
}

$manifestRows = @(Import-Csv -LiteralPath $manifestPath)
$manifestBytes = [int64](Get-Item -LiteralPath $manifestPath).Length
$manifestSha256 = Get-Sha256 -Path $manifestPath
$validationBytes = [int64](Get-Item -LiteralPath $validationPath).Length
$validationSha256 = Get-Sha256 -Path $validationPath

if ($manifestRows.Count -ne $expected.manifest_rows) {
  $errors.Add("Manifest rows: expected $($expected.manifest_rows), got $($manifestRows.Count)")
}
if ($manifestBytes -ne $expected.manifest_bytes -or $manifestSha256 -ne $expected.manifest_sha256) {
  $errors.Add("Manifest identity mismatch")
}
if ($validationBytes -ne $expected.validation_bytes -or $validationSha256 -ne $expected.validation_sha256) {
  $errors.Add("Validation identity mismatch")
}

$manifestPaths = @{}
$artifactIds = @{}
foreach ($row in $manifestRows) {
  $relativePath = ([string]$row.relative_path).Replace("\", "/")
  if ($manifestPaths.ContainsKey($relativePath)) {
    $errors.Add("Duplicate manifest relative_path: $relativePath")
    continue
  }
  $manifestPaths[$relativePath] = $true
  if ($artifactIds.ContainsKey([string]$row.artifact_id)) {
    $errors.Add("Duplicate manifest artifact_id: $($row.artifact_id)")
  }
  $artifactIds[[string]$row.artifact_id] = $true
  if (-not $freeze4Map.ContainsKey($relativePath)) {
    $errors.Add("Manifest file missing from tree: $relativePath")
    continue
  }
  $actual = $freeze4Map[$relativePath]
  if ([int64]$row.bytes -ne [int64]$actual.bytes) {
    $errors.Add("Manifest byte mismatch: $relativePath")
  }
  if (([string]$row.sha256).ToUpperInvariant() -ne [string]$actual.sha256) {
    $errors.Add("Manifest SHA-256 mismatch: $relativePath")
  }
}

foreach ($relativePath in $freeze4Map.Keys) {
  if ($relativePath -in @($manifestRelativePath, $validationRelativePath)) {
    continue
  }
  if (-not $manifestPaths.ContainsKey($relativePath)) {
    $errors.Add("Tree file absent from manifest: $relativePath")
  }
}

$csvFiles = @($freeze4Files | Where-Object Extension -eq ".csv")
$csvRows = [int64]0
$formulaTriggers = [System.Collections.Generic.List[string]]::new()
$csvWidthErrors = [System.Collections.Generic.List[string]]::new()
foreach ($file in $csvFiles) {
  $relativePath = Get-RelativePath -Root $Freeze4Root -Path $file.FullName
  try {
    $rows = @(Read-CsvRows -Path $file.FullName)
    if ($rows.Count -eq 0) {
      $csvWidthErrors.Add("$relativePath has no header")
      continue
    }
    $width = @($rows[0]).Count
    for ($index = 1; $index -lt $rows.Count; $index++) {
      $row = @($rows[$index])
      if ($row.Count -ne $width) {
        $csvWidthErrors.Add("$relativePath row $($index + 1): expected $width columns, got $($row.Count)")
      }
      for ($column = 0; $column -lt $row.Count; $column++) {
        if (Test-FormulaTrigger -Value ([string]$row[$column])) {
          $formulaTriggers.Add("$relativePath row $($index + 1) column $($column + 1)")
        }
      }
    }
    $csvRows += [Math]::Max(0, $rows.Count - 1)
  }
  catch {
    $csvWidthErrors.Add("$relativePath parse error: $($_.Exception.Message)")
  }
}
foreach ($csvError in $csvWidthErrors) {
  $errors.Add("CSV: $csvError")
}
foreach ($trigger in $formulaTriggers) {
  $errors.Add("CSV formula trigger: $trigger")
}

$jsonFiles = @($freeze4Files | Where-Object Extension -eq ".json")
$jsonErrors = [System.Collections.Generic.List[string]]::new()
foreach ($file in $jsonFiles) {
  try {
    Get-Content -Raw -LiteralPath $file.FullName | ConvertFrom-Json | Out-Null
  }
  catch {
    $jsonErrors.Add("$(Get-RelativePath -Root $Freeze4Root -Path $file.FullName): $($_.Exception.Message)")
  }
}
foreach ($jsonError in $jsonErrors) {
  $errors.Add("JSON: $jsonError")
}

$jsonlFiles = @($freeze4Files | Where-Object { $_.Extension -in @(".jsonl", ".ndjson") })
$jsonlRecords = [int64]0
$jsonlErrors = [System.Collections.Generic.List[string]]::new()
foreach ($file in $jsonlFiles) {
  $lineNumber = 0
  foreach ($line in (Get-Content -LiteralPath $file.FullName)) {
    $lineNumber++
    if ([string]::IsNullOrWhiteSpace($line)) {
      continue
    }
    try {
      $line | ConvertFrom-Json | Out-Null
      $jsonlRecords++
    }
    catch {
      $jsonlErrors.Add("$(Get-RelativePath -Root $Freeze4Root -Path $file.FullName) line ${lineNumber}: $($_.Exception.Message)")
    }
  }
}
foreach ($jsonlError in $jsonlErrors) {
  $errors.Add("JSONL: $jsonlError")
}

$textExtensions = @(".csv", ".json", ".jsonl", ".md", ".tex", ".log", ".txt", ".ndjson")
$privacyPatterns = [ordered]@{
  windows_user_path = "C:\Users\"
  slash_user_path = "C:/Users/"
  interlanguage_work_root = "Documents\interlanguage"
  codex_work_root = "Documents\Codex"
  papors_root = "Documents\Papors"
  chatnotes_root = "Chatnotes"
  il_github_root = "C:\IL_GitHub"
}
$privacyHits = [System.Collections.Generic.List[object]]::new()
foreach ($file in ($freeze4Files | Where-Object { $_.Extension.ToLowerInvariant() -in $textExtensions })) {
  $content = Get-Content -Raw -LiteralPath $file.FullName
  foreach ($pattern in $privacyPatterns.GetEnumerator()) {
    if ($content.Contains([string]$pattern.Value, [StringComparison]::OrdinalIgnoreCase)) {
      $privacyHits.Add([ordered]@{
        pattern = $pattern.Key
        path = Get-RelativePath -Root $Freeze4Root -Path $file.FullName
      })
    }
  }
}
foreach ($hit in $privacyHits) {
  $errors.Add("Privacy hit $($hit.pattern): $($hit.path)")
}

$freeze3Files = @(Get-ChildItem -LiteralPath $Freeze3Root -File -Recurse)
$freeze3Map = @{}
foreach ($file in $freeze3Files) {
  $relativePath = Get-RelativePath -Root $Freeze3Root -Path $file.FullName
  $freeze3Map[$relativePath] = [ordered]@{
    bytes = [int64]$file.Length
    sha256 = Get-Sha256 -Path $file.FullName
  }
}
$delta = [System.Collections.Generic.List[object]]::new()
foreach ($relativePath in @($freeze3Map.Keys + $freeze4Map.Keys | Sort-Object -Unique)) {
  if (-not $freeze3Map.ContainsKey($relativePath)) {
    $delta.Add([ordered]@{ path = $relativePath; disposition = "added" })
  }
  elseif (-not $freeze4Map.ContainsKey($relativePath)) {
    $delta.Add([ordered]@{ path = $relativePath; disposition = "removed" })
  }
  elseif ($freeze3Map[$relativePath].sha256 -ne $freeze4Map[$relativePath].sha256 -or
          $freeze3Map[$relativePath].bytes -ne $freeze4Map[$relativePath].bytes) {
    $delta.Add([ordered]@{
      path = $relativePath
      disposition = "changed"
      freeze3_sha256 = $freeze3Map[$relativePath].sha256
      freeze4_sha256 = $freeze4Map[$relativePath].sha256
    })
  }
}
$identicalFiles = $freeze4Map.Count - $delta.Count
if ($identicalFiles -ne $expected.freeze3_identical_files) {
  $errors.Add("Freeze3 identical files: expected $($expected.freeze3_identical_files), got $identicalFiles")
}
if ($delta.Count -ne $expected.freeze3_changed_files) {
  $errors.Add("Freeze3 changed files: expected $($expected.freeze3_changed_files), got $($delta.Count)")
}

$pngWitnesses = @($freeze4Files | Where-Object {
  (Get-RelativePath -Root $Freeze4Root -Path $_.FullName).StartsWith("source_png_witness/", [StringComparison]::Ordinal)
})
$licenseText = Get-Content -Raw -LiteralPath (Join-Path $Freeze4Root "LICENSE_AND_ATTRIBUTION.md")
$rightsGrantFound = $licenseText -match "(?i)permission\s+is\s+granted|licensed\s+under|public\s+domain|redistribution\s+(?:is\s+)?permitted"
$rightsCaveatFound = $licenseText -match "(?is)inherit\s+that\s+rights\s+caveat"
$rightsGate = if ($pngWitnesses.Count -gt 0 -and -not $rightsGrantFound -and $rightsCaveatFound) {
  "BLOCK_SOURCE_PIXELS_PENDING_AFFIRMATIVE_REDISTRIBUTION_RIGHTS"
}
else {
  "PASS"
}

$pdfIdentity = $freeze4Map[$pdfRelativePath]
$texIdentity = $freeze4Map[$texRelativePath]
if ($pdfIdentity.bytes -ne $expected.pdf_bytes -or $pdfIdentity.sha256 -ne $expected.pdf_sha256) {
  $errors.Add("Reader PDF identity mismatch")
}
if ($texIdentity.bytes -ne $expected.tex_bytes -or $texIdentity.sha256 -ne $expected.tex_sha256) {
  $errors.Add("Master TeX identity mismatch")
}

$validation = Get-Content -Raw -LiteralPath $validationPath | ConvertFrom-Json
if ([string]$validation.status -ne "PASS" -or @($validation.errors).Count -ne 0) {
  $errors.Add("Producer validation is not PASS/errors[]")
}

$result = [ordered]@{
  schema = "modern_latex_manuscripts.sga3_loop2_freeze4_independent_audit.v1"
  audited_at = (Get-Date).ToString("o")
  root_label = Split-Path -Leaf $Freeze4Root
  technical_status = if ($errors.Count -eq 0) { "PASS" } else { "FAIL" }
  technical_errors = @($errors)
  rights_status = $rightsGate
  publication_status = if ($errors.Count -eq 0 -and $rightsGate -eq "PASS") {
    "PASS_FOR_EXACT_PUBLICATION"
  }
  elseif ($errors.Count -eq 0) {
    "TECHNICAL_PASS_EXACT_PACKAGE_RIGHTS_BLOCKED"
  }
  else {
    "FAIL"
  }
  tree = [ordered]@{
    files = $freeze4Files.Count
    bytes = $totalBytes
    manifest_rows = $manifestRows.Count
    manifest_replay_errors = @($errors | Where-Object { $_ -like "Manifest*" -or $_ -like "Tree file*" })
  }
  machine = [ordered]@{
    csv_files = $csvFiles.Count
    csv_rows = $csvRows
    csv_rectangularity_errors = @($csvWidthErrors)
    csv_formula_triggers = @($formulaTriggers)
    json_files = $jsonFiles.Count
    json_errors = @($jsonErrors)
    jsonl_files = $jsonlFiles.Count
    jsonl_records = $jsonlRecords
    jsonl_errors = @($jsonlErrors)
  }
  privacy = [ordered]@{
    patterns = @($privacyPatterns.Keys)
    hits = @($privacyHits)
  }
  freeze3_delta = [ordered]@{
    freeze3_files = $freeze3Map.Count
    freeze4_files = $freeze4Map.Count
    identical_files = $identicalFiles
    changed_files = $delta.Count
    delta = @($delta)
  }
  reader = [ordered]@{
    pdf = $pdfIdentity
    tex = $texIdentity
  }
  rights = [ordered]@{
    source_png_witnesses = $pngWitnesses.Count
    affirmative_redistribution_grant_found = $rightsGrantFound
    inherited_rights_caveat_found = $rightsCaveatFound
    disposition = $rightsGate
  }
}

New-Item -ItemType Directory -Force -Path (Split-Path -Parent $OutputPath) | Out-Null
$result | ConvertTo-Json -Depth 12 | Set-Content -LiteralPath $OutputPath -Encoding utf8NoBOM
$result | ConvertTo-Json -Depth 12
if ($errors.Count -ne 0) {
  exit 1
}
