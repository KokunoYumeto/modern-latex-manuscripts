param(
  [string]$CanonicalRoot = "C:\Users\memo_\Documents\Codex\2026-06-09\could-you-look-online-for-me\work\noether-slavic-canonical",
  [string]$ZenodoApiUrl = "https://zenodo.org/api/records/20836874",
  [switch]$SkipZenodo
)

$ErrorActionPreference = "Stop"

$expectedPackageSha = "4F9A629F42C8292BF4CC5FB43E58EBB951EC2A383E01D0812A20E6644E0999C9"
$expectedReviewBundleSha = "A2985DA390620A8982A8BFA526CC9C5CD2EF3FEB63AF9E8E369BFC2F58550799"
$expectedZenodoVersion = "2026-07-02 R569 current source-control head; R570 no-patch checkpoint; language-lane handoff triaged"
$expectedZenodoModifiedUtc = "2026-07-02T10:25:38.360197+00:00"
$expectedZenodoFileCount = 100
$expectedReviewFormCount = 184
$expectedReviewUnitCount = 46
$expectedReviewRoleCount = 4
$expectedCumulativeManifestRel = "renders\cumulative\Noether_Papers01_45PlusBibliography_SourceCorrected_merge_manifest.json"
$expectedCumulativeReaders = @(
  @{
    language = "ukrainian"
    cumulative_pages = 601
    pdf = "renders\cumulative\Noether_Papers01_45PlusBibliography_SourceCorrected_Ukrainian_v001.pdf"
    pdf_bytes = [int64]21344846
    pdf_sha256 = "9A9E3157F70A37571F30A40EDAAD8FDAD423CFC35F55ADC823D4DFE1930E61BE"
    tex = "renders\cumulative\Noether_Papers01_45PlusBibliography_SourceCorrected_Ukrainian_v001.tex"
    tex_sha256 = "12190D3E067F2AF0C1902F3ADCD1B0389C39372AD74F2C92743FE1C05923C70A"
  },
  @{
    language = "russian"
    cumulative_pages = 626
    pdf = "renders\cumulative\Noether_Papers01_45PlusBibliography_SourceCorrected_Russian_v001.pdf"
    pdf_bytes = [int64]21245875
    pdf_sha256 = "658C5720FC28CD840A36DC47A6C133725E5C802E0D858D86DD2B9429FD39F043"
    tex = "renders\cumulative\Noether_Papers01_45PlusBibliography_SourceCorrected_Russian_v001.tex"
    tex_sha256 = "4AFACC12FBC51C91AD45DD198E41999A162732BA7EBE9E08C9317953E8E6A83C"
  },
  @{
    language = "interslavic"
    cumulative_pages = 579
    pdf = "renders\cumulative\Noether_Papers01_45PlusBibliography_SourceCorrected_Interslavic_v001.pdf"
    pdf_bytes = [int64]20399899
    pdf_sha256 = "7C17B89F2D124E37215EBB6394DDCB3AE8DE8C03A4E79045726D09EDCC65B393"
    tex = "renders\cumulative\Noether_Papers01_45PlusBibliography_SourceCorrected_Interslavic_v001.tex"
    tex_sha256 = "DE41F5C555C797EA9E37178D4AFA436AE6227C3BBA285B5FC7DB92B0BEA33FBE"
  },
  @{
    language = "interslavic_cyrillic"
    cumulative_pages = 603
    pdf = "renders\cumulative\Noether_Papers01_45PlusBibliography_SourceCorrected_Interslavic_Cyrillic_v001.pdf"
    pdf_bytes = [int64]20803787
    pdf_sha256 = "66228560ED4911E5D038FB85A7768DBC7155D16E1A4003EB6038506511DBD0CF"
    tex = "renders\cumulative\Noether_Papers01_45PlusBibliography_SourceCorrected_Interslavic_Cyrillic_v001.tex"
    tex_sha256 = "45ABB8D5C2DD49EA4429788D2A810A97E86F4376D6AD45233F5D2C567AAD2577"
  }
)
$expectedCumulativeContactSheets = @(
  @{
    path = "renders\cumulative\visual_inspection\papers01_45_plus_bibliography_ukrainian_appended_endmatter_contact_sheet.png"
    total_pages = 601
    first_appended_page = 557
    sampled_count = 45
    sha256 = "375349FB9AF744E9BB79BFCFEE5692FBD68C487FB83F5FA81007907557A01230"
  },
  @{
    path = "renders\cumulative\visual_inspection\papers01_45_plus_bibliography_russian_appended_endmatter_contact_sheet.png"
    total_pages = 626
    first_appended_page = 579
    sampled_count = 48
    sha256 = "D49109F0B388CC41448695560B0E85ED7185758365FAF3A8FA34BDB5DDE4721C"
  },
  @{
    path = "renders\cumulative\visual_inspection\papers01_45_plus_bibliography_interslavic_appended_endmatter_contact_sheet.png"
    total_pages = 579
    first_appended_page = 535
    sampled_count = 45
    sha256 = "B11670CBCC24F8487562CEBF0B74C8A16AE2DC24C99DC32E95D0343FA18422A1"
  },
  @{
    path = "renders\cumulative\visual_inspection\papers01_45_plus_bibliography_interslavic_cyrillic_appended_endmatter_contact_sheet.png"
    total_pages = 603
    first_appended_page = 559
    sampled_count = 45
    sha256 = "772190AC9923F2F274A19D8B697182D9911E981ED47BDDBAABA415BD57CA1C50"
  }
)
$expectedZenodoSourceFiles = @(
  @{ key = "01 Noether - German Source Cumulative RA20 Paper02 Display Fix.pdf"; size = [int64]2686055; checksum = "md5:ecb19a0bfd8d2b5b5529bc80e3fbbfb5" },
  @{ key = "10 Noether - German Source Current 20260612.zip"; size = [int64]45812768; checksum = "md5:6f995cccf1288e02f84184a4fa39a208" },
  @{ key = "108 Noether - German R124 plus P40 Source Repair Working Baseline 2026-06-24.zip"; size = [int64]46633532; checksum = "md5:9df3881225efebaf0be2d1a51a218e95" },
  @{ key = "109 Noether - Source Audit Status and Caveats 2026-06-24.md"; size = [int64]1745; checksum = "md5:ad9e17c6d2c797200a56b58e615c894d" },
  @{ key = "112 Noether - German R124 plus P40 Full Range Best Available Source Repair 2026-06-24.zip"; size = [int64]46709541; checksum = "md5:abf98b7bf851ff33ec104e9e9dd15caa" },
  @{ key = "113 Noether - Current Source Audit Status Addendum 2026-06-24.md"; size = [int64]1819; checksum = "md5:cb7d4aa297157e81b324740840fdb5c0" },
  @{ key = "114 Noether - R124plusP40 Survival NoNewPatch Audit Cluster 2026-06-24.zip"; size = [int64]111740974; checksum = "md5:b981b84eed227197d95fb71d4b3ff997" },
  @{ key = "115 Noether - R124plusP40 P35 P36 P38 P39 Rebased Source Repairs 2026-06-24.zip"; size = [int64]65835918; checksum = "md5:989b5da46455b72f7f3b4095b86a043f" },
  @{ key = "116 Noether - R124plusP40 P34 Hotspot Disposition NoNewPatch 2026-06-24.zip"; size = [int64]2375233; checksum = "md5:d395516811eb276ab951bdf07c741e92" },
  @{ key = "117 Noether - Slavic WorkSoFar Papers01-34sec02 PublicSafe 2026-06-24.zip"; size = [int64]260383952; checksum = "md5:b965d4eac30bb00c68edfdb27e32acc5" },
  @{ key = "118 Noether - P30 Anchor-Closed Footnote Formula Date Source Repair 2026-06-24.zip"; size = [int64]35523706; checksum = "md5:3ee63d3b1df3e1cc4be1e8baf5979566" },
  @{ key = "119 Noether - PostR124 Survival Rollup NoNewPatch Audit 2026-06-24.zip"; size = [int64]8761308; checksum = "md5:06fd6f63070f835c981787debc0e5a69" },
  @{ key = "Noether_Better_Source_Upgrade_P21_P23_GDZ_600PPI_20260623.zip"; size = [int64]27960381; checksum = "md5:c0baaeebf0f986f7c76e851f24e30755" },
  @{ key = "Noether_R122_P16_SourceAudit_WebDrop_20260624.zip"; size = [int64]17272179; checksum = "md5:70308c02a89f016a3dd117ac3dd0eb0c" },
  @{ key = "Noether_R122_P16P13_SourceAudit_WebDrop_20260624.zip"; size = [int64]10588309; checksum = "md5:623f55d38b84e0698424effcbfe336a4" },
  @{ key = "Noether_R122_P20_SourceAudit_WebDrop_20260624.zip"; size = [int64]21176648; checksum = "md5:7ae5dfeec0c773ca15b19ac04585a2f4" },
  @{ key = "Noether_R122_SourceFix_Rollup_P12_P13_P16_P20_WebDrop_20260624.zip"; size = [int64]547397; checksum = "md5:0245495346d6c13c4bf44005aab97d42" },
  @{ key = "Noether_R122_WebFix_P39_SourceFidelity_189_194_20260624.zip"; size = [int64]25682605; checksum = "md5:3bc7fb4eb3564ace3662c323829157c6" },
  @{ key = "Noether_R124plus_LocalCodex_PostR124_Consolidated_WebDrop_20260624.zip"; size = [int64]4763313; checksum = "md5:cef88c1a327e260bf1e429faa8095399" },
  @{ key = "Noether_Slavic_ZenodoDrive_Transfer_CurrentSources_20260623T1920Z.zip"; size = [int64]729578402; checksum = "md5:f171524cf0471db439144487f5680899" },
  @{ key = "source_witness_cumulative_R120.pdf"; size = [int64]259030245; checksum = "md5:a2b8769e500de1a5870d626f9ff7de9f" }
)
$expectedCanonicalGlossaryAnchor = @{
  count = 214
  total_bytes = [int64]2665586
  aggregate_sha256 = "5E5E8CFD145AD1B3CEE217F3ABB6CC99C05929FD3551FC89F673E3E2F5EA9F56"
  artifact = "NOETHER_SLAVIC_TERMINOLOGY_SIDECAR_ANCHORS_20260704.csv"
}
$expectedInterslavicCyrillicTransliterationAnchor = @{
  count = 187
  total_bytes = [int64]1502837
  aggregate_sha256 = "59931CEE832E9A2A7B709390D028AD70F2E47460E1DD1B074DC04B0CC06E0078"
  artifact = "NOETHER_SLAVIC_TERMINOLOGY_SIDECAR_ANCHORS_20260704.csv"
}
$expectedTerminologyLogAnchors = @(
  @{ path = "logs\TERMINOLOGY_RATIONALE_COVERAGE_AUDIT_20260628.json"; bytes = [int64]73283; sha256 = "1D38516CD5FE604ADF1C8DC246B130E238BADAE39564E93CD2CF991EB5F34574" },
  @{ path = "logs\TERMINOLOGY_RATIONALE_COVERAGE_AUDIT_20260628.md"; bytes = [int64]765; sha256 = "332BADE6CCA20F1D54CBAC269D1AA35A8DFAA38E2BAF197D2529A9CB60383FD1" },
  @{ path = "logs\TERMINOLOGY_DECISION_LOGBOOK.md"; bytes = [int64]468170; sha256 = "134E02E2F0E80D707D3981539E73172D8067312E4F32BC138546331F28112465" },
  @{ path = "logs\INTERSLAVIC_LOGBOOK.md"; bytes = [int64]387565; sha256 = "84D19DE8E8D85734A5CC7EAB12B4BD855EABD533A52DAC5C862C57AF93EEA5C9" }
)
$expectedTerminologyRationaleKeys = @("generated_at_utc", "scope", "repairs", "coverage", "conclusion")
$expectedBroadSlavicReferenceManifestAnchor = @{
  path = "sources\interslavic_triangulation\20260624_slavic_math_reference\slavic_math_reference_manifest.json"
  source_count = 20
  bytes = [int64]66534
  sha256 = "6BB98D9D19AA4B7D063075789F79DCAE9B42D0C95E67171C2ADFA9C2F854A145"
  languages = @("Bulgarian", "Croatian", "Czech", "Polish", "Serbian", "Slovak", "Slovenian")
}
$expectedReferenceShelfOutputAnchors = @(
  @{ path = "NOETHER_SLAVIC_BROAD_REFERENCE_REGISTER_20260704.csv"; rows = 24; bytes = [int64]7750; sha256 = "54E78E366E5352084C71BF2A0F1005B915051D0A13F19A8A2E8B7B78FC61A8FA" },
  @{ path = "NOETHER_SLAVIC_ARXIV_TEX_SOURCE_SHELF_20260704.csv"; rows = 10; bytes = [int64]3967; sha256 = "7652C7A6A96B0833A4E5EC3CB6AA0761A73BEDA2989630282607CCE54771B16C" },
  @{ path = "NOETHER_SLAVIC_UNDERREPRESENTED_BRANCH_EXTENSION_SCAN_20260704.csv"; rows = 12; bytes = [int64]5858; sha256 = "EA7DFE0F072253732A0F6A4F95EDAAB5B53B94F8716699F73ED5127DDF2CC349" },
  @{ path = "NOETHER_SLAVIC_SORBIAN_MATH_SOURCE_ACCESS_AUDIT_20260704.csv"; rows = 7; bytes = [int64]3327; sha256 = "75873CE9C226B052C4AF4874887F9CE56C3EB933079877AC1AB9DA7E2F837139" },
  @{ path = "NOETHER_INTERSLAVIC_LEGIBILITY_LEDGER_20260704.csv"; rows = 9; bytes = [int64]3151; sha256 = "CC69BE0AE2E7BD2B7180A3BB081BD7C944DA2B96777E21B5EFF14608854F7010" },
  @{ path = "NOETHER_INTERSLAVIC_LIMITED_SUPPORT_REVIEW_MICROPACKETS_20260704.csv"; rows = 3; bytes = [int64]1413; sha256 = "17566B705C716F47476E97B6AC187A6D982D0B2BFAD29806B4CE5FFE54229BDD" }
)

$checks = New-Object System.Collections.Generic.List[object]

function Add-Check {
  param(
    [string]$Name,
    [bool]$Pass,
    [string]$Severity,
    [string]$Message,
    [object]$Evidence = $null
  )
  $checks.Add([pscustomobject]@{
    name = $Name
    pass = $Pass
    severity = $Severity
    message = $Message
    evidence = $Evidence
  }) | Out-Null
}

function Read-JsonOrNull {
  param([string]$Path)
  if (-not (Test-Path -LiteralPath $Path)) {
    return $null
  }
  return Get-Content -Raw -LiteralPath $Path | ConvertFrom-Json
}

function Get-StringSha256 {
  param([string]$Value)
  $sha = [System.Security.Cryptography.SHA256]::Create()
  $bytes = [System.Text.Encoding]::UTF8.GetBytes($Value)
  try {
    return (($sha.ComputeHash($bytes) | ForEach-Object { $_.ToString("X2") }) -join "")
  } finally {
    $sha.Dispose()
  }
}

function Get-CanonicalRelativePath {
  param([string]$Path)
  $rootFull = [System.IO.Path]::GetFullPath($CanonicalRoot).TrimEnd([char[]]@([char]92, [char]47))
  $pathFull = [System.IO.Path]::GetFullPath($Path)
  return $pathFull.Substring($rootFull.Length + 1).Replace([string][char]92, "/")
}

$packagePath = Join-Path $CanonicalRoot "packages\Noether_Slavic_Post44_Papers01_45PlusBibliography_Update_20260628T203324Z.zip"
$packageValidationPath = "$packagePath.independent_validation.json"
$reviewBundlePath = Join-Path $CanonicalRoot "review_bundles\Noether_Slavic_ExternalReview_RolePackets_SelfContained_20260628T200514Z.zip"
$sourceInventoryPath = Join-Path $CanonicalRoot "sources\PAPERS_01_43_PLUS_POST_NUMBERED_SOURCE_INVENTORY_VALIDATION.json"
$cumulativeManifestPath = Join-Path $CanonicalRoot $expectedCumulativeManifestRel
$reviewStatusPath = Join-Path $CanonicalRoot "logs\external_review_returns_20260628\EXTERNAL_REVIEW_RETURN_STATUS_20260628.json"
$handoffPath = Join-Path $CanonicalRoot "logs\SLAVIC_MAINTENANCE_PUBLICATION_HANDOFF_20260703T110903Z.json"

Add-Check "canonical_root_exists" (Test-Path -LiteralPath $CanonicalRoot) "fatal" "Canonical Slavic root is readable." @{ path = $CanonicalRoot }

if (Test-Path -LiteralPath $packagePath) {
  $packageHash = (Get-FileHash -Algorithm SHA256 -LiteralPath $packagePath).Hash
  Add-Check "package_sha256_matches" ($packageHash -eq $expectedPackageSha) "fatal" "Primary Slavic package hash matches expected stable package." @{
    path = $packagePath
    expected = $expectedPackageSha
    actual = $packageHash
  }
} else {
  Add-Check "package_present" $false "fatal" "Primary Slavic package is missing." @{ path = $packagePath }
}

if (Test-Path -LiteralPath $reviewBundlePath) {
  $reviewBundleHash = (Get-FileHash -Algorithm SHA256 -LiteralPath $reviewBundlePath).Hash
  Add-Check "review_bundle_sha256_matches" ($reviewBundleHash -eq $expectedReviewBundleSha) "fatal" "External-review bundle hash matches expected stable bundle." @{
    path = $reviewBundlePath
    expected = $expectedReviewBundleSha
    actual = $reviewBundleHash
  }
} else {
  Add-Check "review_bundle_present" $false "fatal" "External-review bundle is missing." @{ path = $reviewBundlePath }
}

$packageValidation = Read-JsonOrNull $packageValidationPath
if ($null -eq $packageValidation) {
  Add-Check "package_independent_validation_present" $false "fatal" "Independent package validation JSON is missing." @{ path = $packageValidationPath }
} else {
  Add-Check "package_independent_validation_overall_pass" ([bool]$packageValidation.overall_pass) "fatal" "Independent package validation overall pass is true." @{ path = $packageValidationPath; value = $packageValidation.overall_pass }
  Add-Check "package_validation_sha_matches" ([bool]$packageValidation.validation_sha_matches) "fatal" "Validation SHA matches." @{ value = $packageValidation.validation_sha_matches }
  Add-Check "package_sha_file_matches" ([bool]$packageValidation.sha_file_matches) "fatal" "SHA sidecar matches." @{ value = $packageValidation.sha_file_matches }
  Add-Check "package_required_missing_empty" (($packageValidation.required_missing | Measure-Object).Count -eq 0) "fatal" "No required package files are missing." @{ required_missing = $packageValidation.required_missing }
  Add-Check "package_render_integrity_pass" ([bool]$packageValidation.render_integrity_overall_pass) "fatal" "Render integrity overall pass is true." @{ value = $packageValidation.render_integrity_overall_pass }
}

$sourceInventory = Read-JsonOrNull $sourceInventoryPath
if ($null -eq $sourceInventory) {
  Add-Check "source_inventory_present" $false "fatal" "Source inventory validation JSON is missing." @{ path = $sourceInventoryPath }
} else {
  Add-Check "source_inventory_missing_required_empty" (($sourceInventory.missing_required_files | Measure-Object).Count -eq 0) "trigger" "No required source-inventory files are missing." @{ missing_required_files = $sourceInventory.missing_required_files }
  Add-Check "source_inventory_scan_pdf_count_43" ($sourceInventory.scan_pdf_count_in_final_slice_directory -eq 43) "trigger" "Source inventory still records 43 scan PDFs." @{ scan_pdf_count = $sourceInventory.scan_pdf_count_in_final_slice_directory }
}

$broadReferenceMismatches = New-Object System.Collections.Generic.List[object]
$broadReferenceManifestPath = Join-Path $CanonicalRoot $expectedBroadSlavicReferenceManifestAnchor.path
if (-not (Test-Path -LiteralPath $broadReferenceManifestPath)) {
  $broadReferenceMismatches.Add([pscustomobject]@{ issue = "manifest_missing"; path = $expectedBroadSlavicReferenceManifestAnchor.path }) | Out-Null
} else {
  $manifestItem = Get-Item -LiteralPath $broadReferenceManifestPath
  $manifestHash = (Get-FileHash -Algorithm SHA256 -LiteralPath $broadReferenceManifestPath).Hash
  if ([int64]$manifestItem.Length -ne [int64]$expectedBroadSlavicReferenceManifestAnchor.bytes) {
    $broadReferenceMismatches.Add([pscustomobject]@{ issue = "bytes_mismatch"; expected = $expectedBroadSlavicReferenceManifestAnchor.bytes; actual = $manifestItem.Length }) | Out-Null
  }
  if ($manifestHash -ne $expectedBroadSlavicReferenceManifestAnchor.sha256) {
    $broadReferenceMismatches.Add([pscustomobject]@{ issue = "sha_mismatch"; expected = $expectedBroadSlavicReferenceManifestAnchor.sha256; actual = $manifestHash }) | Out-Null
  }
  try {
    $broadReferenceManifest = Get-Content -Raw -LiteralPath $broadReferenceManifestPath | ConvertFrom-Json
    $broadReferenceSources = @($broadReferenceManifest.sources)
    $actualBroadReferenceLanguages = @($broadReferenceSources | Select-Object -ExpandProperty language -Unique | Sort-Object)
    $languageDiff = @(Compare-Object -ReferenceObject $expectedBroadSlavicReferenceManifestAnchor.languages -DifferenceObject $actualBroadReferenceLanguages)
    if ($broadReferenceSources.Count -ne $expectedBroadSlavicReferenceManifestAnchor.source_count) {
      $broadReferenceMismatches.Add([pscustomobject]@{ issue = "source_count_mismatch"; expected = $expectedBroadSlavicReferenceManifestAnchor.source_count; actual = $broadReferenceSources.Count }) | Out-Null
    }
    if ($languageDiff.Count -ne 0) {
      $broadReferenceMismatches.Add([pscustomobject]@{ issue = "language_set_mismatch"; expected = $expectedBroadSlavicReferenceManifestAnchor.languages; actual = $actualBroadReferenceLanguages }) | Out-Null
    }
  } catch {
    $broadReferenceMismatches.Add([pscustomobject]@{ issue = "manifest_parse_failure"; error = $_.Exception.Message }) | Out-Null
  }
}
Add-Check "broad_slavic_reference_manifest_anchor_matches" ($broadReferenceMismatches.Count -eq 0) "trigger" "Broad Slavic mathematical-reference manifest hash, source count, and language set match expected source-shelf baseline." @{
  expected_source_count = $expectedBroadSlavicReferenceManifestAnchor.source_count
  expected_languages = $expectedBroadSlavicReferenceManifestAnchor.languages
  anchor_artifact = "NOETHER_SLAVIC_REFERENCE_SHELF_BOUNDARY_ANCHORS_20260704.csv"
  mismatch_count = $broadReferenceMismatches.Count
  mismatches = $broadReferenceMismatches
}

$cumulativeManifest = Read-JsonOrNull $cumulativeManifestPath
if ($null -eq $cumulativeManifest) {
  Add-Check "cumulative_merge_manifest_present" $false "trigger" "Cumulative merge manifest is missing." @{ path = $cumulativeManifestPath }
} else {
  $readerRecords = @($cumulativeManifest.records)
  $contactSheetRecords = @($cumulativeManifest.contact_sheets)
  Add-Check "cumulative_merge_manifest_record_count_4" ($readerRecords.Count -eq 4) "trigger" "Cumulative merge manifest still has 4 reader records." @{ expected = 4; actual = $readerRecords.Count }
  Add-Check "cumulative_merge_manifest_contact_sheet_count_4" ($contactSheetRecords.Count -eq 4) "trigger" "Cumulative merge manifest still has 4 contact-sheet records." @{ expected = 4; actual = $contactSheetRecords.Count }

  $readerRecordsByLanguage = @{}
  foreach ($record in $readerRecords) {
    $readerRecordsByLanguage[$record.language] = $record
  }
  $readerMismatches = New-Object System.Collections.Generic.List[object]
  foreach ($expectedReader in $expectedCumulativeReaders) {
    if (-not $readerRecordsByLanguage.ContainsKey($expectedReader.language)) {
      $readerMismatches.Add([pscustomobject]@{ language = $expectedReader.language; issue = "missing_manifest_record" }) | Out-Null
      continue
    }

    $record = $readerRecordsByLanguage[$expectedReader.language]
    if (-not [bool]$record.page_count_ok) {
      $readerMismatches.Add([pscustomobject]@{ language = $expectedReader.language; issue = "manifest_page_count_not_ok"; actual = $record.page_count_ok }) | Out-Null
    }
    if ([int]$record.cumulative_pages -ne [int]$expectedReader.cumulative_pages) {
      $readerMismatches.Add([pscustomobject]@{ language = $expectedReader.language; issue = "manifest_cumulative_pages_mismatch"; expected = $expectedReader.cumulative_pages; actual = $record.cumulative_pages }) | Out-Null
    }
    if ($record.cumulative_pdf -ne ($expectedReader.pdf -replace "\\", "/")) {
      $readerMismatches.Add([pscustomobject]@{ language = $expectedReader.language; issue = "manifest_pdf_path_mismatch"; expected = $expectedReader.pdf; actual = $record.cumulative_pdf }) | Out-Null
    }
    if ($record.cumulative_tex -ne ($expectedReader.tex -replace "\\", "/")) {
      $readerMismatches.Add([pscustomobject]@{ language = $expectedReader.language; issue = "manifest_tex_path_mismatch"; expected = $expectedReader.tex; actual = $record.cumulative_tex }) | Out-Null
    }
    if ([int64]$record.cumulative_pdf_bytes -ne [int64]$expectedReader.pdf_bytes) {
      $readerMismatches.Add([pscustomobject]@{ language = $expectedReader.language; issue = "manifest_pdf_bytes_mismatch"; expected = $expectedReader.pdf_bytes; actual = $record.cumulative_pdf_bytes }) | Out-Null
    }
    if ($record.cumulative_pdf_sha256 -ne $expectedReader.pdf_sha256) {
      $readerMismatches.Add([pscustomobject]@{ language = $expectedReader.language; issue = "manifest_pdf_sha_mismatch"; expected = $expectedReader.pdf_sha256; actual = $record.cumulative_pdf_sha256 }) | Out-Null
    }
    if ($record.cumulative_tex_sha256 -ne $expectedReader.tex_sha256) {
      $readerMismatches.Add([pscustomobject]@{ language = $expectedReader.language; issue = "manifest_tex_sha_mismatch"; expected = $expectedReader.tex_sha256; actual = $record.cumulative_tex_sha256 }) | Out-Null
    }

    $pdfPath = Join-Path $CanonicalRoot $expectedReader.pdf
    if (-not (Test-Path -LiteralPath $pdfPath)) {
      $readerMismatches.Add([pscustomobject]@{ language = $expectedReader.language; issue = "pdf_missing"; path = $pdfPath }) | Out-Null
    } else {
      $pdfItem = Get-Item -LiteralPath $pdfPath
      $pdfHash = (Get-FileHash -Algorithm SHA256 -LiteralPath $pdfPath).Hash
      if ([int64]$pdfItem.Length -ne [int64]$expectedReader.pdf_bytes) {
        $readerMismatches.Add([pscustomobject]@{ language = $expectedReader.language; issue = "pdf_bytes_mismatch"; expected = $expectedReader.pdf_bytes; actual = $pdfItem.Length }) | Out-Null
      }
      if ($pdfHash -ne $expectedReader.pdf_sha256) {
        $readerMismatches.Add([pscustomobject]@{ language = $expectedReader.language; issue = "pdf_sha_mismatch"; expected = $expectedReader.pdf_sha256; actual = $pdfHash }) | Out-Null
      }
    }

    $texPath = Join-Path $CanonicalRoot $expectedReader.tex
    if (-not (Test-Path -LiteralPath $texPath)) {
      $readerMismatches.Add([pscustomobject]@{ language = $expectedReader.language; issue = "tex_missing"; path = $texPath }) | Out-Null
    } else {
      $texHash = (Get-FileHash -Algorithm SHA256 -LiteralPath $texPath).Hash
      if ($texHash -ne $expectedReader.tex_sha256) {
        $readerMismatches.Add([pscustomobject]@{ language = $expectedReader.language; issue = "tex_sha_mismatch"; expected = $expectedReader.tex_sha256; actual = $texHash }) | Out-Null
      }
    }
  }
  Add-Check "cumulative_reader_streams_match_expected" ($readerMismatches.Count -eq 0) "trigger" "Cumulative Slavic reader PDF/TEX hashes and manifest anchors match expected baseline." @{
    expected_reader_count = $expectedCumulativeReaders.Count
    mismatch_count = $readerMismatches.Count
    mismatches = $readerMismatches
  }

  $contactSheetRecordsByPath = @{}
  foreach ($record in $contactSheetRecords) {
    $contactSheetRecordsByPath[$record.path] = $record
  }
  $contactSheetMismatches = New-Object System.Collections.Generic.List[object]
  foreach ($expectedContactSheet in $expectedCumulativeContactSheets) {
    $manifestPathStyle = $expectedContactSheet.path -replace "\\", "/"
    if (-not $contactSheetRecordsByPath.ContainsKey($manifestPathStyle)) {
      $contactSheetMismatches.Add([pscustomobject]@{ path = $expectedContactSheet.path; issue = "missing_manifest_record" }) | Out-Null
      continue
    }
    $record = $contactSheetRecordsByPath[$manifestPathStyle]
    if ([int]$record.total_pages -ne [int]$expectedContactSheet.total_pages) {
      $contactSheetMismatches.Add([pscustomobject]@{ path = $expectedContactSheet.path; issue = "manifest_total_pages_mismatch"; expected = $expectedContactSheet.total_pages; actual = $record.total_pages }) | Out-Null
    }
    if ([int]$record.first_appended_page -ne [int]$expectedContactSheet.first_appended_page) {
      $contactSheetMismatches.Add([pscustomobject]@{ path = $expectedContactSheet.path; issue = "manifest_first_appended_page_mismatch"; expected = $expectedContactSheet.first_appended_page; actual = $record.first_appended_page }) | Out-Null
    }
    if (@($record.pages_sampled).Count -ne [int]$expectedContactSheet.sampled_count) {
      $contactSheetMismatches.Add([pscustomobject]@{ path = $expectedContactSheet.path; issue = "manifest_sampled_count_mismatch"; expected = $expectedContactSheet.sampled_count; actual = @($record.pages_sampled).Count }) | Out-Null
    }
    if ($record.sha256 -ne $expectedContactSheet.sha256) {
      $contactSheetMismatches.Add([pscustomobject]@{ path = $expectedContactSheet.path; issue = "manifest_sha_mismatch"; expected = $expectedContactSheet.sha256; actual = $record.sha256 }) | Out-Null
    }

    $contactSheetPath = Join-Path $CanonicalRoot $expectedContactSheet.path
    if (-not (Test-Path -LiteralPath $contactSheetPath)) {
      $contactSheetMismatches.Add([pscustomobject]@{ path = $expectedContactSheet.path; issue = "file_missing"; absolute_path = $contactSheetPath }) | Out-Null
    } else {
      $contactSheetHash = (Get-FileHash -Algorithm SHA256 -LiteralPath $contactSheetPath).Hash
      if ($contactSheetHash -ne $expectedContactSheet.sha256) {
        $contactSheetMismatches.Add([pscustomobject]@{ path = $expectedContactSheet.path; issue = "file_sha_mismatch"; expected = $expectedContactSheet.sha256; actual = $contactSheetHash }) | Out-Null
      }
    }
  }
  Add-Check "cumulative_contact_sheets_match_expected" ($contactSheetMismatches.Count -eq 0) "trigger" "Cumulative Slavic contact-sheet hashes and manifest anchors match expected baseline." @{
    expected_contact_sheet_count = $expectedCumulativeContactSheets.Count
    mismatch_count = $contactSheetMismatches.Count
    mismatches = $contactSheetMismatches
  }
}

$glossaryDir = Join-Path $CanonicalRoot "glossary"
$glossaryMismatches = New-Object System.Collections.Generic.List[object]
if (-not (Test-Path -LiteralPath $glossaryDir)) {
  $glossaryMismatches.Add([pscustomobject]@{ issue = "glossary_dir_missing"; path = $glossaryDir }) | Out-Null
} else {
  $glossaryRows = @(Get-ChildItem -LiteralPath $glossaryDir -File -Filter "*.json" |
    Where-Object { $_.Name -like "noether_*_terms.json" -and $_.Name -notlike "*before_section09*" -and $_.Name -notlike "*working*" } |
    ForEach-Object {
      [pscustomobject]@{
        path = Get-CanonicalRelativePath $_.FullName
        bytes = [int64]$_.Length
        sha256 = (Get-FileHash -Algorithm SHA256 -LiteralPath $_.FullName).Hash
      }
    } | Sort-Object path)
  $glossaryTotalBytes = [int64](($glossaryRows | Measure-Object bytes -Sum).Sum)
  $glossaryAggregateText = ($glossaryRows | ForEach-Object { "$($_.path)|$($_.bytes)|$($_.sha256)" }) -join "`n"
  $glossaryAggregateSha = Get-StringSha256 $glossaryAggregateText
  if ($glossaryRows.Count -ne $expectedCanonicalGlossaryAnchor.count) {
    $glossaryMismatches.Add([pscustomobject]@{ issue = "count_mismatch"; expected = $expectedCanonicalGlossaryAnchor.count; actual = $glossaryRows.Count }) | Out-Null
  }
  if ($glossaryTotalBytes -ne $expectedCanonicalGlossaryAnchor.total_bytes) {
    $glossaryMismatches.Add([pscustomobject]@{ issue = "total_bytes_mismatch"; expected = $expectedCanonicalGlossaryAnchor.total_bytes; actual = $glossaryTotalBytes }) | Out-Null
  }
  if ($glossaryAggregateSha -ne $expectedCanonicalGlossaryAnchor.aggregate_sha256) {
    $glossaryMismatches.Add([pscustomobject]@{ issue = "aggregate_sha_mismatch"; expected = $expectedCanonicalGlossaryAnchor.aggregate_sha256; actual = $glossaryAggregateSha }) | Out-Null
  }
}
Add-Check "canonical_glossary_sidecar_anchor_matches" ($glossaryMismatches.Count -eq 0) "trigger" "Canonical Slavic glossary sidecar count, bytes, and aggregate hash match expected baseline." @{
  expected_count = $expectedCanonicalGlossaryAnchor.count
  expected_total_bytes = $expectedCanonicalGlossaryAnchor.total_bytes
  expected_aggregate_sha256 = $expectedCanonicalGlossaryAnchor.aggregate_sha256
  anchor_artifact = $expectedCanonicalGlossaryAnchor.artifact
  mismatch_count = $glossaryMismatches.Count
  mismatches = $glossaryMismatches
}

$terminologyLogMismatches = New-Object System.Collections.Generic.List[object]
foreach ($expectedLog in $expectedTerminologyLogAnchors) {
  $logPath = Join-Path $CanonicalRoot $expectedLog.path
  if (-not (Test-Path -LiteralPath $logPath)) {
    $terminologyLogMismatches.Add([pscustomobject]@{ path = $expectedLog.path; issue = "missing" }) | Out-Null
    continue
  }
  $logItem = Get-Item -LiteralPath $logPath
  $logHash = (Get-FileHash -Algorithm SHA256 -LiteralPath $logPath).Hash
  if ([int64]$logItem.Length -ne [int64]$expectedLog.bytes) {
    $terminologyLogMismatches.Add([pscustomobject]@{ path = $expectedLog.path; issue = "bytes_mismatch"; expected = $expectedLog.bytes; actual = $logItem.Length }) | Out-Null
  }
  if ($logHash -ne $expectedLog.sha256) {
    $terminologyLogMismatches.Add([pscustomobject]@{ path = $expectedLog.path; issue = "sha_mismatch"; expected = $expectedLog.sha256; actual = $logHash }) | Out-Null
  }
}
Add-Check "terminology_log_sidecar_hashes_match" ($terminologyLogMismatches.Count -eq 0) "trigger" "Terminology rationale and Interslavic logbook sidecar hashes match expected baseline." @{
  expected_log_count = $expectedTerminologyLogAnchors.Count
  anchor_artifact = "NOETHER_SLAVIC_TERMINOLOGY_SIDECAR_ANCHORS_20260704.csv"
  mismatch_count = $terminologyLogMismatches.Count
  mismatches = $terminologyLogMismatches
}

$terminologyRationaleJsonPath = Join-Path $CanonicalRoot "logs\TERMINOLOGY_RATIONALE_COVERAGE_AUDIT_20260628.json"
$terminologyRationaleJson = Read-JsonOrNull $terminologyRationaleJsonPath
if ($null -eq $terminologyRationaleJson) {
  Add-Check "terminology_rationale_audit_schema_keys_present" $false "trigger" "Terminology rationale coverage JSON is missing or unreadable." @{ path = $terminologyRationaleJsonPath }
} else {
  $actualRationaleKeys = @($terminologyRationaleJson.PSObject.Properties.Name)
  $missingRationaleKeys = @($expectedTerminologyRationaleKeys | Where-Object { $_ -notin $actualRationaleKeys })
  Add-Check "terminology_rationale_audit_schema_keys_present" ($missingRationaleKeys.Count -eq 0) "trigger" "Terminology rationale coverage JSON retains required schema keys." @{
    expected_keys = $expectedTerminologyRationaleKeys
    actual_keys = $actualRationaleKeys
    missing_keys = $missingRationaleKeys
  }
}

$translationsDir = Join-Path $CanonicalRoot "translations"
$transliterationMismatches = New-Object System.Collections.Generic.List[object]
if (-not (Test-Path -LiteralPath $translationsDir)) {
  $transliterationMismatches.Add([pscustomobject]@{ issue = "translations_dir_missing"; path = $translationsDir }) | Out-Null
} else {
  $transliterationRows = @(Get-ChildItem -LiteralPath $translationsDir -Recurse -File -Filter "*transliteration_report.json" |
    Where-Object { $_.FullName -match "\\interslavic-cyrillic\\" } |
    ForEach-Object {
      [pscustomobject]@{
        path = Get-CanonicalRelativePath $_.FullName
        bytes = [int64]$_.Length
        sha256 = (Get-FileHash -Algorithm SHA256 -LiteralPath $_.FullName).Hash
      }
    } | Sort-Object path)
  $transliterationTotalBytes = [int64](($transliterationRows | Measure-Object bytes -Sum).Sum)
  $transliterationAggregateText = ($transliterationRows | ForEach-Object { "$($_.path)|$($_.bytes)|$($_.sha256)" }) -join "`n"
  $transliterationAggregateSha = Get-StringSha256 $transliterationAggregateText
  if ($transliterationRows.Count -ne $expectedInterslavicCyrillicTransliterationAnchor.count) {
    $transliterationMismatches.Add([pscustomobject]@{ issue = "count_mismatch"; expected = $expectedInterslavicCyrillicTransliterationAnchor.count; actual = $transliterationRows.Count }) | Out-Null
  }
  if ($transliterationTotalBytes -ne $expectedInterslavicCyrillicTransliterationAnchor.total_bytes) {
    $transliterationMismatches.Add([pscustomobject]@{ issue = "total_bytes_mismatch"; expected = $expectedInterslavicCyrillicTransliterationAnchor.total_bytes; actual = $transliterationTotalBytes }) | Out-Null
  }
  if ($transliterationAggregateSha -ne $expectedInterslavicCyrillicTransliterationAnchor.aggregate_sha256) {
    $transliterationMismatches.Add([pscustomobject]@{ issue = "aggregate_sha_mismatch"; expected = $expectedInterslavicCyrillicTransliterationAnchor.aggregate_sha256; actual = $transliterationAggregateSha }) | Out-Null
  }
}
Add-Check "interslavic_cyrillic_transliteration_sidecar_anchor_matches" ($transliterationMismatches.Count -eq 0) "trigger" "Interslavic Cyrillic transliteration sidecar count, bytes, and aggregate hash match expected baseline." @{
  expected_count = $expectedInterslavicCyrillicTransliterationAnchor.count
  expected_total_bytes = $expectedInterslavicCyrillicTransliterationAnchor.total_bytes
  expected_aggregate_sha256 = $expectedInterslavicCyrillicTransliterationAnchor.aggregate_sha256
  anchor_artifact = $expectedInterslavicCyrillicTransliterationAnchor.artifact
  mismatch_count = $transliterationMismatches.Count
  mismatches = $transliterationMismatches
}

$outputRoot = if ($PSScriptRoot) { $PSScriptRoot } else { Split-Path -Parent $MyInvocation.MyCommand.Path }
$referenceShelfOutputMismatches = New-Object System.Collections.Generic.List[object]
foreach ($expectedReferenceArtifact in $expectedReferenceShelfOutputAnchors) {
  $referenceArtifactPath = Join-Path $outputRoot $expectedReferenceArtifact.path
  if (-not (Test-Path -LiteralPath $referenceArtifactPath)) {
    $referenceShelfOutputMismatches.Add([pscustomobject]@{ path = $expectedReferenceArtifact.path; issue = "missing" }) | Out-Null
    continue
  }
  $referenceArtifactItem = Get-Item -LiteralPath $referenceArtifactPath
  $referenceArtifactHash = (Get-FileHash -Algorithm SHA256 -LiteralPath $referenceArtifactPath).Hash
  if ([int64]$referenceArtifactItem.Length -ne [int64]$expectedReferenceArtifact.bytes) {
    $referenceShelfOutputMismatches.Add([pscustomobject]@{ path = $expectedReferenceArtifact.path; issue = "bytes_mismatch"; expected = $expectedReferenceArtifact.bytes; actual = $referenceArtifactItem.Length }) | Out-Null
  }
  if ($referenceArtifactHash -ne $expectedReferenceArtifact.sha256) {
    $referenceShelfOutputMismatches.Add([pscustomobject]@{ path = $expectedReferenceArtifact.path; issue = "sha_mismatch"; expected = $expectedReferenceArtifact.sha256; actual = $referenceArtifactHash }) | Out-Null
  }
  try {
    $referenceArtifactRows = @(Import-Csv -LiteralPath $referenceArtifactPath)
    if ($referenceArtifactRows.Count -ne $expectedReferenceArtifact.rows) {
      $referenceShelfOutputMismatches.Add([pscustomobject]@{ path = $expectedReferenceArtifact.path; issue = "row_count_mismatch"; expected = $expectedReferenceArtifact.rows; actual = $referenceArtifactRows.Count }) | Out-Null
    }
  } catch {
    $referenceShelfOutputMismatches.Add([pscustomobject]@{ path = $expectedReferenceArtifact.path; issue = "csv_parse_failure"; error = $_.Exception.Message }) | Out-Null
  }
}
Add-Check "reference_shelf_output_artifact_anchors_match" ($referenceShelfOutputMismatches.Count -eq 0) "trigger" "Broad Slavic/arXiv/reference-shelf output artifacts match expected row counts and hashes." @{
  expected_artifact_count = $expectedReferenceShelfOutputAnchors.Count
  anchor_artifact = "NOETHER_SLAVIC_REFERENCE_SHELF_BOUNDARY_ANCHORS_20260704.csv"
  mismatch_count = $referenceShelfOutputMismatches.Count
  mismatches = $referenceShelfOutputMismatches
}

$reviewStatus = Read-JsonOrNull $reviewStatusPath
if ($null -eq $reviewStatus) {
  Add-Check "external_review_status_present" $false "fatal" "External review return status JSON is missing." @{ path = $reviewStatusPath }
} else {
  $listedReviewFormCount = ($reviewStatus.expected_unit_role_forms | Measure-Object).Count
  $uniqueReviewUnitCount = ($reviewStatus.expected_unit_role_forms | Select-Object -ExpandProperty unit -Unique | Measure-Object).Count
  $uniqueReviewRoleCount = ($reviewStatus.expected_unit_role_forms | Select-Object -ExpandProperty role_id -Unique | Measure-Object).Count
  $returnFilesListedCount = ($reviewStatus.return_files | Measure-Object).Count

  Add-Check "external_review_expected_form_count_184" ($reviewStatus.expected_form_count -eq $expectedReviewFormCount) "trigger" "External review status still expects 184 forms." @{ expected = $expectedReviewFormCount; actual = $reviewStatus.expected_form_count }
  Add-Check "external_review_expected_form_list_count_184" ($listedReviewFormCount -eq $expectedReviewFormCount) "trigger" "External review status lists 184 expected unit-role forms." @{ expected = $expectedReviewFormCount; actual = $listedReviewFormCount }
  Add-Check "external_review_expected_unit_count_46" ($uniqueReviewUnitCount -eq $expectedReviewUnitCount) "trigger" "External review status spans 46 units." @{ expected = $expectedReviewUnitCount; actual = $uniqueReviewUnitCount }
  Add-Check "external_review_expected_role_count_4" ($uniqueReviewRoleCount -eq $expectedReviewRoleCount) "trigger" "External review status spans 4 reviewer roles." @{ expected = $expectedReviewRoleCount; actual = $uniqueReviewRoleCount }
  Add-Check "external_review_return_count_zero" ($reviewStatus.return_file_count -eq 0) "trigger" "No external/native review return files are present." @{ return_file_count = $reviewStatus.return_file_count; expected_form_count = $reviewStatus.expected_form_count }
  Add-Check "external_review_return_files_list_empty" ($returnFilesListedCount -eq 0) "trigger" "External review return file list is empty." @{ return_files_list_count = $returnFilesListedCount }
  Add-Check "external_review_schema_valid_count_zero" ($reviewStatus.schema_valid_return_file_count -eq 0) "trigger" "No schema-valid review returns are present." @{ schema_valid_return_file_count = $reviewStatus.schema_valid_return_file_count }
  Add-Check "accepted_review_pair_count_zero" ($reviewStatus.accepted_pair_count -eq 0) "trigger" "No accepted review correction pairs are present." @{ accepted_pair_count = $reviewStatus.accepted_pair_count }
  Add-Check "external_review_blocking_issue_count_zero" ($reviewStatus.blocking_issue_count -eq 0) "info" "No blocking issues are recorded because no returns have been ingested." @{ blocking_issue_count = $reviewStatus.blocking_issue_count }
  Add-Check "external_review_not_complete" (-not [bool]$reviewStatus.complete_for_all_units) "info" "External/native authority review remains incomplete." @{ complete_for_all_units = $reviewStatus.complete_for_all_units }
}

$handoff = Read-JsonOrNull $handoffPath
if ($null -eq $handoff) {
  Add-Check "maintenance_handoff_present" $false "trigger" "Maintenance handoff JSON is missing." @{ path = $handoffPath }
} else {
  Add-Check "maintenance_gate_no_source_replacement" (-not [bool]$handoff.gate.source_replacement_required) "trigger" "Maintenance gate says no source replacement is required." @{ value = $handoff.gate.source_replacement_required }
  Add-Check "maintenance_gate_no_slavic_rebuild" (-not [bool]$handoff.gate.slavic_rebuild_required_now) "trigger" "Maintenance gate says no Slavic rebuild is required now." @{ value = $handoff.gate.slavic_rebuild_required_now }
  Add-Check "maintenance_gate_external_review_incomplete" (-not [bool]$handoff.gate.external_review_complete) "info" "Maintenance gate does not claim external review complete." @{ value = $handoff.gate.external_review_complete }
}

$zenodoEvidence = $null
if ($SkipZenodo) {
  Add-Check "zenodo_live_check_skipped" $true "info" "Zenodo live check was skipped by caller." $null
} else {
  try {
    $zenodo = Invoke-RestMethod -Uri $ZenodoApiUrl -TimeoutSec 30
    $zenodoEvidence = [pscustomobject]@{
      id = $zenodo.id
      doi = $zenodo.doi
      conceptdoi = $zenodo.conceptdoi
      modified = $zenodo.modified
      version = $zenodo.metadata.version
      title = $zenodo.metadata.title
      file_count = $zenodo.files.Count
    }
    Add-Check "zenodo_file_count_matches_expected" ($zenodo.files.Count -eq $expectedZenodoFileCount) "trigger" "Zenodo live file count matches expected source baseline." $zenodoEvidence
    Add-Check "zenodo_version_matches_expected" ($zenodo.metadata.version -eq $expectedZenodoVersion) "trigger" "Zenodo live version string matches expected source baseline." $zenodoEvidence
    Add-Check "zenodo_modified_matches_expected" ($zenodo.modified -eq $expectedZenodoModifiedUtc) "trigger" "Zenodo live modified timestamp matches expected source baseline." $zenodoEvidence

    $zenodoFilesByKey = @{}
    foreach ($file in $zenodo.files) {
      $zenodoFilesByKey[$file.key] = $file
    }
    $sourceFingerprintMismatches = New-Object System.Collections.Generic.List[object]
    foreach ($expectedFile in $expectedZenodoSourceFiles) {
      if (-not $zenodoFilesByKey.ContainsKey($expectedFile.key)) {
        $sourceFingerprintMismatches.Add([pscustomobject]@{
          key = $expectedFile.key
          issue = "missing"
          expected_size = $expectedFile.size
          actual_size = $null
          expected_checksum = $expectedFile.checksum
          actual_checksum = $null
        }) | Out-Null
        continue
      }

      $actualFile = $zenodoFilesByKey[$expectedFile.key]
      $actualSize = [int64]$actualFile.size
      if (($actualSize -ne [int64]$expectedFile.size) -or ($actualFile.checksum -ne $expectedFile.checksum)) {
        $sourceFingerprintMismatches.Add([pscustomobject]@{
          key = $expectedFile.key
          issue = "size_or_checksum_mismatch"
          expected_size = $expectedFile.size
          actual_size = $actualSize
          expected_checksum = $expectedFile.checksum
          actual_checksum = $actualFile.checksum
        }) | Out-Null
      }
    }
    Add-Check "zenodo_source_file_fingerprints_match" ($sourceFingerprintMismatches.Count -eq 0) "trigger" "Zenodo source-like file key/size/checksum fingerprints match expected baseline." @{
      expected_source_file_count = $expectedZenodoSourceFiles.Count
      mismatch_count = $sourceFingerprintMismatches.Count
      fingerprint_artifact = "NOETHER_SLAVIC_ZENODO_SOURCE_FILE_FINGERPRINT_20260704.csv"
      mismatches = $sourceFingerprintMismatches
    }
  } catch {
    Add-Check "zenodo_live_check_available" $false "trigger" "Zenodo live check failed; source freshness cannot be proven." @{ error = $_.Exception.Message; url = $ZenodoApiUrl }
  }
}

$fatalFailures = @($checks | Where-Object { -not $_.pass -and $_.severity -eq "fatal" })
$triggerFailures = @($checks | Where-Object { -not $_.pass -and $_.severity -eq "trigger" })
$rebuildTriggerNow = ($triggerFailures.Count -gt 0)
$localStable = ($fatalFailures.Count -eq 0 -and $triggerFailures.Count -eq 0)

$result = [pscustomobject]@{
  generated_at_local = (Get-Date).ToString("o")
  canonical_root = $CanonicalRoot
  zenodo_api_url = $ZenodoApiUrl
  local_slavic_baseline_stable = $localStable
  rebuild_trigger_now = $rebuildTriggerNow
  native_review_completion_claim_allowed = $false
  external_review_complete = $false
  fatal_failure_count = $fatalFailures.Count
  trigger_failure_count = $triggerFailures.Count
  checks = $checks
  zenodo_live_evidence = $zenodoEvidence
  exit_code_meaning = @{
    "0" = "No local rebuild trigger detected and stable local anchors pass."
    "1" = "Fatal local evidence failure."
    "2" = "Rebuild/source/review trigger requires human inspection."
  }
}

$result | ConvertTo-Json -Depth 12

if ($fatalFailures.Count -gt 0) {
  exit 1
}
if ($triggerFailures.Count -gt 0) {
  exit 2
}
exit 0
