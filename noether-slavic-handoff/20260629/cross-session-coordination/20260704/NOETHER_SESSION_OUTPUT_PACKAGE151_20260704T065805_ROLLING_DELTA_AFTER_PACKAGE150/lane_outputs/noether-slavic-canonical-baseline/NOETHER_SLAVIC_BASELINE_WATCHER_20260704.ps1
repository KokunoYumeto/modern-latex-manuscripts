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

$packagePath = Join-Path $CanonicalRoot "packages\Noether_Slavic_Post44_Papers01_45PlusBibliography_Update_20260628T203324Z.zip"
$packageValidationPath = "$packagePath.independent_validation.json"
$reviewBundlePath = Join-Path $CanonicalRoot "review_bundles\Noether_Slavic_ExternalReview_RolePackets_SelfContained_20260628T200514Z.zip"
$sourceInventoryPath = Join-Path $CanonicalRoot "sources\PAPERS_01_43_PLUS_POST_NUMBERED_SOURCE_INVENTORY_VALIDATION.json"
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
