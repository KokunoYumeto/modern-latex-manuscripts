[CmdletBinding()]
param(
    [string]$InputPath = 'manifests/adopt.json',
    [string]$SchemaPath = 'manifests/adopt.schema.json',
    [string]$ValidationPath = 'manifests/adopt.check.json',
    [string]$LabelPath = '.github/labels.json',
    [string]$OutputPath = 'manifests/adopt.check.json',
    [string]$ObservedDate = (Get-Date -Format 'yyyy-MM-dd')
)

$ErrorActionPreference = 'Stop'
$utf8 = [Text.UTF8Encoding]::new($false)
$repoRoot = [IO.Path]::GetFullPath((Get-Location).Path)
$errors = [Collections.Generic.List[string]]::new()
$pathChecks = 0
$trackedPathChecks = 0

function Get-Sha256 {
    param([byte[]]$Bytes)
    return [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($Bytes))
}

function Add-Error {
    param([string]$Message)
    $errors.Add($Message)
}

function Test-ExactFields {
    param(
        [object]$Value,
        [string[]]$Expected,
        [string]$Context
    )
    $actual = @($Value.PSObject.Properties.Name)
    foreach ($name in $Expected) {
        if (-not ($actual -ccontains $name)) {
            Add-Error "$Context missing field: $name"
        }
    }
    foreach ($name in $actual) {
        if (-not ($Expected -ccontains $name)) {
            Add-Error "$Context has unexpected field: $name"
        }
    }
}

function Test-RepoPath {
    param(
        [AllowNull()][string]$Path,
        [string]$Context,
        [bool]$Required
    )
    if ([string]::IsNullOrWhiteSpace($Path)) {
        if ($Required) { Add-Error "$Context requires a repository path." }
        return
    }
    $script:pathChecks++
    if ([IO.Path]::IsPathRooted($Path) -or $Path.Contains('\')) {
        Add-Error "$Context path must be repository-relative with forward slashes: $Path"
        return
    }
    $relative = $Path.Split('#')[0]
    if ([string]::IsNullOrWhiteSpace($relative)) {
        Add-Error "$Context path has no file component: $Path"
        return
    }
    $segments = @($relative.Split('/'))
    if ($segments -ccontains '..') {
        Add-Error "$Context path escapes the repository: $Path"
        return
    }
    $full = [IO.Path]::GetFullPath((Join-Path $repoRoot $relative))
    $rootPrefix = $repoRoot.TrimEnd([IO.Path]::DirectorySeparatorChar) + [IO.Path]::DirectorySeparatorChar
    if (-not $full.StartsWith($rootPrefix, [StringComparison]::OrdinalIgnoreCase)) {
        Add-Error "$Context path resolves outside the repository: $Path"
        return
    }
    if (-not [IO.File]::Exists($full)) {
        Add-Error "$Context path does not exist: $Path"
        return
    }
    & git ls-files --error-unmatch -- $relative 2>$null | Out-Null
    if ($LASTEXITCODE -ne 0) {
        Add-Error "$Context path is not tracked by Git: $Path"
        return
    }
    $script:trackedPathChecks++
}

function Test-UniqueStrings {
    param(
        [object[]]$Values,
        [string]$Context,
        [bool]$RequireNonEmpty
    )
    $seen = [Collections.Generic.HashSet[string]]::new([StringComparer]::Ordinal)
    if ($RequireNonEmpty -and $Values.Count -eq 0) {
        Add-Error "$Context must not be empty."
    }
    foreach ($value in $Values) {
        $text = [string]$value
        if ([string]::IsNullOrWhiteSpace($text)) {
            Add-Error "$Context contains an empty value."
            continue
        }
        if (-not $seen.Add($text)) {
            Add-Error "$Context contains duplicate value: $text"
        }
    }
}

function Get-IssueTemplateLabels {
    param([string]$Text)
    $values = [Collections.Generic.List[string]]::new()
    $lines = $Text.Split("`n")
    for ($index = 0; $index -lt $lines.Count; $index++) {
        if ($lines[$index] -cnotmatch '^labels:\s*(?<inline>.*)$') { continue }
        $inline = $Matches.inline.Trim()
        if ($inline.Length -gt 0) {
            foreach ($match in [regex]::Matches($inline, '[A-Za-z0-9][A-Za-z0-9_-]*')) {
                $values.Add($match.Value)
            }
        }
        else {
            for ($next = $index + 1; $next -lt $lines.Count; $next++) {
                if ($lines[$next] -cnotmatch '^\s+-\s+(?<value>[A-Za-z0-9][A-Za-z0-9_-]*)\s*$') { break }
                $values.Add($Matches.value)
            }
        }
        break
    }
    return [string[]]$values.ToArray()
}

$inputFull = [IO.Path]::GetFullPath((Join-Path $repoRoot $InputPath))
$schemaFull = [IO.Path]::GetFullPath((Join-Path $repoRoot $SchemaPath))
if (-not [IO.File]::Exists($inputFull)) { throw "Board does not exist: $InputPath" }
if (-not [IO.File]::Exists($schemaFull)) { throw "Schema does not exist: $SchemaPath" }

$inputBytes = [IO.File]::ReadAllBytes($inputFull)
$schemaBytes = [IO.File]::ReadAllBytes($schemaFull)
foreach ($pair in @(
    [pscustomobject]@{ Name = 'board'; Bytes = $inputBytes },
    [pscustomobject]@{ Name = 'schema'; Bytes = $schemaBytes }
)) {
    if ($pair.Bytes.Length -ge 3 -and
        $pair.Bytes[0] -eq 0xEF -and
        $pair.Bytes[1] -eq 0xBB -and
        $pair.Bytes[2] -eq 0xBF) {
        Add-Error "$($pair.Name) contains a UTF-8 BOM."
    }
    if ($utf8.GetString($pair.Bytes).Contains("`r")) {
        Add-Error "$($pair.Name) must use LF line endings."
    }
}

$board = $utf8.GetString($inputBytes) | ConvertFrom-Json -Depth 100 -DateKind String
$schema = $utf8.GetString($schemaBytes) | ConvertFrom-Json -Depth 100 -DateKind String

if ($board.schema -cne 'math-commons-adoption-v1') { Add-Error 'Unexpected board schema.' }
if ($board.schema_url -cne $SchemaPath.Replace('\', '/')) { Add-Error 'Board schema_url does not match SchemaPath.' }
if ($board.validation -cne $ValidationPath.Replace('\', '/')) { Add-Error 'Board validation path does not match ValidationPath.' }
if ($board.board_role -cne 'operational_layer') { Add-Error 'Board role must remain operational_layer.' }
if ($schema.'$schema' -cne 'https://json-schema.org/draft/2020-12/schema') { Add-Error 'Schema draft identity is not 2020-12.' }
if ($schema.'$id' -cne 'https://raw.githubusercontent.com/KokunoYumeto/modern-latex-manuscripts/main/manifests/adopt.schema.json') {
    Add-Error 'Schema $id is not the stable raw-main interface.'
}

$expectedFields = [string[]]@(
    'id', 'author', 'work', 'series', 'corpus', 'lane_state',
    'coverage_state', 'adoption_status', 'priority', 'readiness', 'owner',
    'owner_scope', 'languages', 'archive_path', 'related_paths',
    'source_basis', 'next_cursor', 'prerequisites', 'workflow', 'claim_url',
    'updated', 'notes'
)
$expectedMirrorFields = [string[]]@('id', 'item_id', 'owner', 'scope', 'url', 'status', 'updated')
$expectedWorkflowFields = [string[]]@(
    'id', 'purpose', 'start_when', 'inputs', 'steps', 'evidence',
    'stop_conditions', 'handback'
)
$boardFields = [string[]]@($board.fields)
$mirrorFields = [string[]]@($board.mirror_fields)
$workflowFields = [string[]]@($board.workflow_fields)
if (($boardFields -join "`n") -cne ($expectedFields -join "`n")) { Add-Error 'Item fields are not the exact v1 ordered field contract.' }
if (($mirrorFields -join "`n") -cne ($expectedMirrorFields -join "`n")) { Add-Error 'Mirror fields are not the exact v1 ordered field contract.' }
if (($workflowFields -join "`n") -cne ($expectedWorkflowFields -join "`n")) { Add-Error 'Workflow fields are not the exact v1 ordered field contract.' }

$expectedEnums = [ordered]@{
    lane_state = [string[]]@('current_work', 'ready_for_adoption', 'future')
    priority = [string[]]@('high', 'medium', 'exploratory')
    readiness = [string[]]@('active', 'exact_cursor', 'repair_ready', 'review_ready', 'expansion_ready', 'continuation_ready', 'intake_ready', 'source_discovery_first')
    adoption_status = [string[]]@('maintained_parallel_review_welcome', 'open_parallel_mirrors_welcome', 'claimed_active_parallel_mirrors_welcome', 'paused_open_for_handoff', 'future_evidence_needed')
    mirror_status = [string[]]@('declared', 'active', 'returned', 'paused', 'withdrawn')
}
foreach ($name in $expectedEnums.Keys) {
    $actual = [string[]]@($board.enums.$name)
    if (($actual -join "`n") -cne ($expectedEnums[$name] -join "`n")) {
        Add-Error "Enum contract mismatch: $name"
    }
}

Test-RepoPath -Path $board.human_board -Context 'human_board' -Required $true
$humanBoardPath = [string]$board.human_board
$humanBoardFull = [IO.Path]::GetFullPath((Join-Path $repoRoot $humanBoardPath))
$humanBoardBytes = if ([IO.File]::Exists($humanBoardFull)) { [IO.File]::ReadAllBytes($humanBoardFull) } else { [byte[]]@() }
if ($humanBoardBytes.Length -ge 3 -and
    $humanBoardBytes[0] -eq 0xEF -and
    $humanBoardBytes[1] -eq 0xBB -and
    $humanBoardBytes[2] -eq 0xBF) {
    Add-Error 'human_board contains a UTF-8 BOM.'
}
$humanBoardText = $utf8.GetString($humanBoardBytes)
if ($humanBoardText.Contains("`r")) {
    Add-Error 'human_board must use LF line endings.'
}
$humanBoardRowIds = [Collections.Generic.List[string]]::new()
foreach ($match in [regex]::Matches($humanBoardText, '(?m)^\| `(?<id>[a-z0-9]+(?:-[a-z0-9]+)*)` \|')) {
    $humanBoardRowIds.Add($match.Groups['id'].Value)
}
$workflowErrorStart = $errors.Count
$workflowRegistryIds = [Collections.Generic.HashSet[string]]::new([StringComparer]::Ordinal)
$workflowUsedIds = [Collections.Generic.HashSet[string]]::new([StringComparer]::Ordinal)
$workflowRows = @($board.workflows)
$workflowRowIds = [Collections.Generic.List[string]]::new()
foreach ($flow in $workflowRows) {
    $id = [string]$flow.id
    $context = if ([string]::IsNullOrWhiteSpace($id)) { 'workflow:<missing-id>' } else { "workflow:$id" }
    Test-ExactFields -Value $flow -Expected $expectedWorkflowFields -Context $context
    if ($id -cnotmatch '^[a-z0-9]+(?:_[a-z0-9]+)*$') { Add-Error "$context has an invalid ID." }
    if (-not $workflowRegistryIds.Add($id)) { Add-Error "Duplicate workflow ID: $id" }
    $workflowRowIds.Add($id)
    foreach ($property in @('purpose', 'start_when')) {
        if ([string]::IsNullOrWhiteSpace([string]$flow.$property)) { Add-Error "$context has empty $property." }
    }
    foreach ($property in @('inputs', 'steps', 'evidence', 'stop_conditions', 'handback')) {
        Test-UniqueStrings -Values @($flow.$property) -Context "$context $property" -RequireNonEmpty $true
    }
}
$sortedWorkflowIds = [string[]]@($workflowRowIds)
[Array]::Sort($sortedWorkflowIds, [StringComparer]::Ordinal)
if (($workflowRowIds -join "`n") -cne ($sortedWorkflowIds -join "`n")) {
    Add-Error 'Workflow registry IDs are not in ordinal order.'
}
Test-RepoPath -Path ([string]$board.human_workflows) -Context 'human_workflows' -Required $true
$humanWorkflowsPath = [string]$board.human_workflows
$humanWorkflowsFull = [IO.Path]::GetFullPath((Join-Path $repoRoot $humanWorkflowsPath))
$humanWorkflowsBytes = if ([IO.File]::Exists($humanWorkflowsFull)) { [IO.File]::ReadAllBytes($humanWorkflowsFull) } else { [byte[]]@() }
if ($humanWorkflowsBytes.Length -ge 3 -and
    $humanWorkflowsBytes[0] -eq 0xEF -and
    $humanWorkflowsBytes[1] -eq 0xBB -and
    $humanWorkflowsBytes[2] -eq 0xBF) {
    Add-Error 'human_workflows contains a UTF-8 BOM.'
}
$humanWorkflowsText = $utf8.GetString($humanWorkflowsBytes)
if ($humanWorkflowsText.Contains("`r")) { Add-Error 'human_workflows must use LF line endings.' }
$humanWorkflowIds = [Collections.Generic.List[string]]::new()
foreach ($match in [regex]::Matches($humanWorkflowsText, '(?m)^## `(?<id>[a-z0-9]+(?:_[a-z0-9]+)*)`$')) {
    $humanWorkflowIds.Add($match.Groups['id'].Value)
}
if (($humanWorkflowIds -join "`n") -cne ($workflowRowIds -join "`n")) {
    Add-Error 'human_workflows headings do not exactly match the workflow registry.'
}
$workflowContractPass = ($errors.Count -eq $workflowErrorStart)
foreach ($name in @('coverage_maps', 'reader_shelf', 'source_shelf', 'archive_history')) {
    Test-RepoPath -Path $board.archive_authority.$name -Context "archive_authority.$name" -Required $true
}
Test-RepoPath -Path $board.map_manifest -Context 'map_manifest' -Required $true
$expectedClaimInterface = 'https://github.com/KokunoYumeto/modern-latex-manuscripts/issues/new?template=adopt.yml'
$expectedHandbackInterface = 'https://github.com/KokunoYumeto/modern-latex-manuscripts/issues/new?template=handback.yml'
if ([string]$board.claim_interface -cne $expectedClaimInterface) { Add-Error 'claim_interface does not match the exact adoption form.' }
if ([string]$board.handback_interface -cne $expectedHandbackInterface) { Add-Error 'handback_interface does not match the exact handback form.' }
Test-RepoPath -Path '.github/ISSUE_TEMPLATE/adopt.yml' -Context 'claim_interface template' -Required $true
Test-RepoPath -Path '.github/ISSUE_TEMPLATE/handback.yml' -Context 'handback_interface template' -Required $true

$expectedLabelRows = @(
    [pscustomobject]@{
        name = 'adoption'
        color = '0E8A16'
        description = 'Bounded adoption, independent mirror, or result handback'
        templates = [string[]]@('.github/ISSUE_TEMPLATE/adopt.yml', '.github/ISSUE_TEMPLATE/handback.yml')
    },
    [pscustomobject]@{
        name = 'correction'
        color = 'B60205'
        description = 'Source, transcription, translation, or reader correction'
        templates = [string[]]@('.github/ISSUE_TEMPLATE/correction.yml', '.github/ISSUE_TEMPLATE/source_or_translation_correction.md')
    },
    [pscustomobject]@{
        name = 'rendering'
        color = '5319E7'
        description = 'PDF or LaTeX rendering problem'
        templates = [string[]]@('.github/ISSUE_TEMPLATE/rendering_problem.md')
    },
    [pscustomobject]@{
        name = 'source'
        color = '1D76DB'
        description = 'Source scan, missing work, or source improvement'
        templates = [string[]]@('.github/ISSUE_TEMPLATE/source-suggestion.yml')
    }
)
$issueLabelContractPass = $true
$labelContract = $null
$labelBytes = [byte[]]@()
Test-RepoPath -Path $LabelPath -Context 'issue label contract' -Required $true
$labelFull = [IO.Path]::GetFullPath((Join-Path $repoRoot $LabelPath))
if ([IO.File]::Exists($labelFull)) {
    $labelBytes = [IO.File]::ReadAllBytes($labelFull)
    if ($labelBytes.Length -ge 3 -and $labelBytes[0] -eq 0xEF -and $labelBytes[1] -eq 0xBB -and $labelBytes[2] -eq 0xBF) {
        Add-Error 'issue label contract contains a UTF-8 BOM.'
        $issueLabelContractPass = $false
    }
    $labelText = $utf8.GetString($labelBytes)
    if ($labelText.Contains("`r")) {
        Add-Error 'issue label contract must use LF line endings.'
        $issueLabelContractPass = $false
    }
    try {
        $labelContract = $labelText | ConvertFrom-Json -Depth 20 -DateKind String
    }
    catch {
        Add-Error "issue label contract is not valid JSON: $($_.Exception.Message)"
        $issueLabelContractPass = $false
    }
}
if ($null -ne $labelContract) {
    Test-ExactFields -Value $labelContract -Expected @('schema', 'repository', 'labels') -Context 'issue label contract'
    if ([string]$labelContract.schema -cne 'github-issue-label-contract-v1') {
        Add-Error 'issue label contract has an unexpected schema.'
        $issueLabelContractPass = $false
    }
    if ([string]$labelContract.repository -cne 'KokunoYumeto/modern-latex-manuscripts') {
        Add-Error 'issue label contract has an unexpected repository.'
        $issueLabelContractPass = $false
    }
    $actualLabelRows = @($labelContract.labels)
    if ($actualLabelRows.Count -ne $expectedLabelRows.Count) {
        Add-Error 'issue label contract does not contain the exact four workflow labels.'
        $issueLabelContractPass = $false
    }
    for ($index = 0; $index -lt [Math]::Min($actualLabelRows.Count, $expectedLabelRows.Count); $index++) {
        $actual = $actualLabelRows[$index]
        $expected = $expectedLabelRows[$index]
        Test-ExactFields -Value $actual -Expected @('name', 'color', 'description', 'templates') -Context "issue label:$($expected.name)"
        if ([string]$actual.name -cne $expected.name -or
            [string]$actual.color -cne $expected.color -or
            [string]$actual.description -cne $expected.description -or
            ([string[]]@($actual.templates) -join "`n") -cne ($expected.templates -join "`n")) {
            Add-Error "issue label contract row differs from the exact $($expected.name) contract."
            $issueLabelContractPass = $false
        }
        foreach ($template in $expected.templates) {
            Test-RepoPath -Path $template -Context "issue label:$($expected.name) template" -Required $true
            $templateFull = [IO.Path]::GetFullPath((Join-Path $repoRoot $template))
            if (-not [IO.File]::Exists($templateFull)) { continue }
            $declared = [string[]]@(Get-IssueTemplateLabels -Text ([IO.File]::ReadAllText($templateFull, $utf8)))
            if (($declared -join "`n") -cne $expected.name) {
                Add-Error "$template does not declare exactly the $($expected.name) label."
                $issueLabelContractPass = $false
            }
        }
    }
}

$mapManifestPath = [string]$board.map_manifest
$mapManifestFull = [IO.Path]::GetFullPath((Join-Path $repoRoot $mapManifestPath))
$mapManifestBytes = if ([IO.File]::Exists($mapManifestFull)) { [IO.File]::ReadAllBytes($mapManifestFull) } else { [byte[]]@() }
$mapManifest = $null
if ($mapManifestBytes.Length -gt 0) {
    if ($mapManifestBytes.Length -ge 3 -and
        $mapManifestBytes[0] -eq 0xEF -and
        $mapManifestBytes[1] -eq 0xBB -and
        $mapManifestBytes[2] -eq 0xBF) {
        Add-Error 'map_manifest contains a UTF-8 BOM.'
    }
    if ($utf8.GetString($mapManifestBytes).Contains("`r")) {
        Add-Error 'map_manifest must use LF line endings.'
    }
    try {
        $mapManifest = $utf8.GetString($mapManifestBytes) | ConvertFrom-Json -Depth 100 -DateKind String
    } catch {
        Add-Error "map_manifest is not valid JSON: $($_.Exception.Message)"
    }
}

$requiredMaps = [string[]]@($board.required_maps)
Test-UniqueStrings -Values $requiredMaps -Context 'required_maps' -RequireNonEmpty $true
$manifestMaps = [string[]]@()
if ($null -ne $mapManifest) {
    $manifestMaps = [string[]]@($mapManifest.current_map_set.files_exact | ForEach-Object { [string]$_.path })
    if ([int]$mapManifest.current_map_set.files -ne $manifestMaps.Count) {
        Add-Error 'map_manifest current_map_set.files does not match files_exact count.'
    }
    if (($requiredMaps -join "`n") -cne ($manifestMaps -join "`n")) {
        Add-Error 'required_maps does not exactly match map_manifest current_map_set.files_exact in ordinal order.'
    }
}
foreach ($path in $requiredMaps) {
    Test-RepoPath -Path $path -Context 'required_maps' -Required $true
}
$expectedQueueSources = [string[]]@('docs/known-gaps.md', 'docs/work-queue.md')
$queueSources = [string[]]@($board.queue_sources)
Test-UniqueStrings -Values $queueSources -Context 'queue_sources' -RequireNonEmpty $true
if (($queueSources -join "`n") -cne ($expectedQueueSources -join "`n")) {
    Add-Error 'queue_sources does not match the exact known-gaps/work-queue contract.'
}
foreach ($path in $queueSources) {
    Test-RepoPath -Path $path -Context 'queue_sources' -Required $true
}
$expectedSnapshotPaths = [string[]]@(
    $InputPath.Replace('\', '/'),
    $SchemaPath.Replace('\', '/'),
    $ValidationPath.Replace('\', '/'),
    $mapManifestPath.Replace('\', '/')
)
$expectedSnapshotChecks = [string[]]@(
    'validation_status_pass',
    'validation_errors_empty',
    'declared_bytes_sha256_match',
    'schema_validation_pass'
)
$snapshotPaths = [string[]]@($board.snapshot_policy.same_commit_paths)
$snapshotChecks = [string[]]@($board.snapshot_policy.required_checks)
if ([string]$board.snapshot_policy.stable_locator_ref -cne 'main') {
    Add-Error 'snapshot_policy stable_locator_ref must remain main.'
}
if ([string]$board.snapshot_policy.immutable_unit -cne 'human_approved_exact_commit') {
    Add-Error 'snapshot_policy immutable_unit must require a human-approved exact commit.'
}
if (($snapshotPaths -join "`n") -cne ($expectedSnapshotPaths -join "`n")) {
    Add-Error 'snapshot_policy same_commit_paths does not match the exact four-file contract.'
}
if (($snapshotChecks -join "`n") -cne ($expectedSnapshotChecks -join "`n")) {
    Add-Error 'snapshot_policy required_checks does not match the exact verification contract.'
}
if ($board.snapshot_policy.mixed_revisions_forbidden -cne $true) {
    Add-Error 'snapshot_policy must forbid mixed revisions.'
}
foreach ($path in $snapshotPaths) {
    Test-RepoPath -Path $path -Context 'snapshot_policy.same_commit_paths' -Required $true
}
$expectedConsumerHelper = 'scripts/get-adopt.py'
if ([string]$board.consumer_helper -cne $expectedConsumerHelper) {
    Add-Error 'consumer_helper does not match the exact v1 helper path.'
}
Test-RepoPath -Path ([string]$board.consumer_helper) -Context 'consumer_helper' -Required $true
$expectedClaimAuditor = 'scripts/check-claims.py'
if ([string]$board.claim_auditor -cne $expectedClaimAuditor) {
    Add-Error 'claim_auditor does not match the exact v1 auditor path.'
}
Test-RepoPath -Path ([string]$board.claim_auditor) -Context 'claim_auditor' -Required $true

$ids = [Collections.Generic.HashSet[string]]::new([StringComparer]::Ordinal)
$stateCounts = [ordered]@{ current_work = 0; ready_for_adoption = 0; future = 0 }
$requiredRowFields = $expectedFields
foreach ($item in @($board.items)) {
    $id = [string]$item.id
    $context = if ([string]::IsNullOrWhiteSpace($id)) { 'item:<missing-id>' } else { "item:$id" }
    Test-ExactFields -Value $item -Expected $requiredRowFields -Context $context
    if ($id -cnotmatch '^[a-z0-9]+(?:-[a-z0-9]+)*$') { Add-Error "$context has an invalid ID." }
    if (-not $ids.Add($id)) { Add-Error "Duplicate item ID: $id" }
    foreach ($property in @('author', 'work', 'corpus', 'coverage_state', 'owner_scope', 'source_basis', 'next_cursor', 'claim_url', 'updated', 'notes')) {
        if ([string]::IsNullOrWhiteSpace([string]$item.$property)) { Add-Error "$context has empty $property." }
    }
    foreach ($enumName in @('lane_state', 'priority', 'readiness', 'adoption_status')) {
        if (-not ($expectedEnums[$enumName] -ccontains [string]$item.$enumName)) {
            Add-Error "$context has invalid ${enumName}: $($item.$enumName)"
        }
    }
    if ($stateCounts.Contains([string]$item.lane_state)) { $stateCounts[[string]$item.lane_state]++ }
    Test-UniqueStrings -Values @($item.languages) -Context "$context languages" -RequireNonEmpty $true
    Test-UniqueStrings -Values @($item.related_paths) -Context "$context related_paths" -RequireNonEmpty $false
    Test-UniqueStrings -Values @($item.prerequisites) -Context "$context prerequisites" -RequireNonEmpty $true
    Test-UniqueStrings -Values @($item.workflow) -Context "$context workflow" -RequireNonEmpty $true
    foreach ($workflowId in @($item.workflow)) {
        $token = [string]$workflowId
        if (-not $workflowRegistryIds.Contains($token)) {
            Add-Error "$context refers to unknown workflow: $token"
            $workflowContractPass = $false
        }
        else {
            [void]$workflowUsedIds.Add($token)
        }
    }
    if ([string]$item.claim_url -cne [string]$board.claim_interface) { Add-Error "$context claim_url differs from claim_interface." }

    switch ([string]$item.lane_state) {
        'current_work' {
            if ([string]::IsNullOrWhiteSpace([string]$item.owner)) { Add-Error "$context current work requires an owner." }
            if ([string]$item.readiness -cne 'active') { Add-Error "$context current work must have active readiness." }
        }
        'ready_for_adoption' {
            if ([string]::IsNullOrWhiteSpace([string]$item.archive_path)) { Add-Error "$context adoption-ready work requires archive_path." }
            if ([string]$item.readiness -cin @('active', 'source_discovery_first')) { Add-Error "$context adoption-ready work has incompatible readiness." }
        }
        'future' {
            if ($null -ne $item.owner) { Add-Error "$context future work must have null owner." }
            if ([string]$item.readiness -cne 'source_discovery_first') { Add-Error "$context future work must require source discovery." }
            if ([string]$item.adoption_status -cne 'future_evidence_needed') { Add-Error "$context future work has incompatible adoption_status." }
        }
    }
    Test-RepoPath -Path $item.archive_path -Context "$context archive_path" -Required ([string]$item.lane_state -cne 'future')
    foreach ($path in @($item.related_paths)) {
        Test-RepoPath -Path ([string]$path) -Context "$context related_paths" -Required $true
    }
}

$unreferencedWorkflowIds = [Collections.Generic.List[string]]::new()
foreach ($workflowId in $workflowRowIds) {
    if (-not $workflowUsedIds.Contains($workflowId)) {
        $unreferencedWorkflowIds.Add($workflowId)
        Add-Error "Workflow registry entry is not used by any board row: $workflowId"
        $workflowContractPass = $false
    }
}

foreach ($state in $stateCounts.Keys) {
    if ($stateCounts[$state] -eq 0) { Add-Error "Board has no rows for lane_state $state." }
}

$humanBoardIdSet = [Collections.Generic.HashSet[string]]::new([StringComparer]::Ordinal)
$duplicateHumanBoardIds = [Collections.Generic.List[string]]::new()
$unknownHumanBoardIds = [Collections.Generic.List[string]]::new()
foreach ($id in $humanBoardRowIds) {
    if (-not $humanBoardIdSet.Add($id)) {
        $duplicateHumanBoardIds.Add($id)
        Add-Error "human_board contains duplicate Board ID row: $id"
    }
    if (-not $ids.Contains($id)) {
        $unknownHumanBoardIds.Add($id)
        Add-Error "human_board contains unknown Board ID row: $id"
    }
}
$missingHumanBoardIds = [Collections.Generic.List[string]]::new()
foreach ($id in $ids) {
    if (-not $humanBoardIdSet.Contains($id)) {
        $missingHumanBoardIds.Add($id)
        Add-Error "human_board has no row for Board ID: $id"
    }
}

$requiredMapSet = [Collections.Generic.HashSet[string]]::new([StringComparer]::Ordinal)
foreach ($path in $requiredMaps) { [void]$requiredMapSet.Add($path) }
$representedMapSet = [Collections.Generic.HashSet[string]]::new([StringComparer]::Ordinal)
foreach ($item in @($board.items)) {
    $candidatePaths = @([string]$item.archive_path) + [string[]]@($item.related_paths)
    foreach ($path in $candidatePaths) {
        if ([string]::IsNullOrWhiteSpace($path)) { continue }
        $relative = $path.Split('#')[0]
        if ($requiredMapSet.Contains($relative)) { [void]$representedMapSet.Add($relative) }
    }
}
$missingRequiredMaps = [Collections.Generic.List[string]]::new()
foreach ($path in $requiredMaps) {
    if (-not $representedMapSet.Contains($path)) {
        $missingRequiredMaps.Add($path)
        Add-Error "Required coverage map has no adoption-board item reference: $path"
    }
}
$queueSourceSet = [Collections.Generic.HashSet[string]]::new([StringComparer]::Ordinal)
foreach ($path in $queueSources) { [void]$queueSourceSet.Add($path) }
$representedQueueSourceSet = [Collections.Generic.HashSet[string]]::new([StringComparer]::Ordinal)
foreach ($item in @($board.items)) {
    $candidatePaths = @([string]$item.archive_path) + [string[]]@($item.related_paths)
    foreach ($path in $candidatePaths) {
        if ([string]::IsNullOrWhiteSpace($path)) { continue }
        $relative = $path.Split('#')[0]
        if ($queueSourceSet.Contains($relative)) { [void]$representedQueueSourceSet.Add($relative) }
    }
}
$missingQueueSources = [Collections.Generic.List[string]]::new()
foreach ($path in $queueSources) {
    if (-not $representedQueueSourceSet.Contains($path)) {
        $missingQueueSources.Add($path)
        Add-Error "Operational queue source has no adoption-board item reference: $path"
    }
}

$mirrorIds = [Collections.Generic.HashSet[string]]::new([StringComparer]::Ordinal)
foreach ($mirror in @($board.mirrors)) {
    $id = [string]$mirror.id
    $context = if ([string]::IsNullOrWhiteSpace($id)) { 'mirror:<missing-id>' } else { "mirror:$id" }
    Test-ExactFields -Value $mirror -Expected $expectedMirrorFields -Context $context
    if ($id -cnotmatch '^[a-z0-9]+(?:-[a-z0-9]+)*$') { Add-Error "$context has an invalid ID." }
    if (-not $mirrorIds.Add($id)) { Add-Error "Duplicate mirror ID: $id" }
    if (-not $ids.Contains([string]$mirror.item_id)) { Add-Error "$context refers to unknown item_id: $($mirror.item_id)" }
    if (-not ($expectedEnums.mirror_status -ccontains [string]$mirror.status)) { Add-Error "$context has invalid status: $($mirror.status)" }
    foreach ($property in @('owner', 'scope', 'url', 'updated')) {
        if ([string]::IsNullOrWhiteSpace([string]$mirror.$property)) { Add-Error "$context has empty $property." }
    }
}

$observedCommit = (& git rev-parse HEAD).Trim()
if ($LASTEXITCODE -ne 0) { throw 'Could not resolve HEAD.' }
$report = [ordered]@{
    schema = 'math-commons-adoption-check-v1'
    status = if ($errors.Count -eq 0) { 'PASS' } else { 'FAIL' }
    errors = @($errors)
    observed_date = $ObservedDate
    observed_commit = $observedCommit
    board = [ordered]@{
        path = $InputPath.Replace('\', '/')
        bytes = $inputBytes.Length
        sha256 = Get-Sha256 -Bytes $inputBytes
        schema = [string]$board.schema
    }
    schema_file = [ordered]@{
        path = $SchemaPath.Replace('\', '/')
        bytes = $schemaBytes.Length
        sha256 = Get-Sha256 -Bytes $schemaBytes
        draft = [string]$schema.'$schema'
    }
    map_manifest = [ordered]@{
        path = $mapManifestPath.Replace('\', '/')
        bytes = $mapManifestBytes.Length
        sha256 = if ($mapManifestBytes.Length -gt 0) { Get-Sha256 -Bytes $mapManifestBytes } else { $null }
        required_maps = $requiredMaps.Count
    }
    human_board = [ordered]@{
        path = $humanBoardPath.Replace('\', '/')
        bytes = $humanBoardBytes.Length
        sha256 = if ($humanBoardBytes.Length -gt 0) { Get-Sha256 -Bytes $humanBoardBytes } else { $null }
        rows = $humanBoardRowIds.Count
    }
    human_workflows = [ordered]@{
        path = $humanWorkflowsPath.Replace('\', '/')
        bytes = $humanWorkflowsBytes.Length
        sha256 = if ($humanWorkflowsBytes.Length -gt 0) { Get-Sha256 -Bytes $humanWorkflowsBytes } else { $null }
        flows = $workflowRowIds.Count
        headings = $humanWorkflowIds.Count
    }
    issue_labels = [ordered]@{
        path = $LabelPath.Replace('\', '/')
        bytes = $labelBytes.Length
        sha256 = if ($labelBytes.Length -gt 0) { Get-Sha256 -Bytes $labelBytes } else { $null }
        labels = if ($null -ne $labelContract) { @($labelContract.labels).Count } else { 0 }
        templates = [int](($expectedLabelRows | ForEach-Object { @($_.templates).Count } | Measure-Object -Sum).Sum)
    }
    snapshot_policy = [ordered]@{
        stable_locator_ref = [string]$board.snapshot_policy.stable_locator_ref
        immutable_unit = [string]$board.snapshot_policy.immutable_unit
        same_commit_paths = $snapshotPaths.Count
        required_checks = $snapshotChecks.Count
        mixed_revisions_forbidden = [bool]$board.snapshot_policy.mixed_revisions_forbidden
    }
    consumer_helper = [string]$board.consumer_helper
    claim_auditor = [string]$board.claim_auditor
    aggregate = [ordered]@{
        items = @($board.items).Count
        mirrors = @($board.mirrors).Count
        current_work = $stateCounts.current_work
        ready_for_adoption = $stateCounts.ready_for_adoption
        future = $stateCounts.future
        unique_item_ids = $ids.Count
        unique_mirror_ids = $mirrorIds.Count
        required_maps = $requiredMaps.Count
        represented_required_maps = $representedMapSet.Count
        missing_required_maps = $missingRequiredMaps.Count
        queue_sources = $queueSources.Count
        represented_queue_sources = $representedQueueSourceSet.Count
        missing_queue_sources = $missingQueueSources.Count
        human_board_rows = $humanBoardRowIds.Count
        represented_human_board_items = $humanBoardIdSet.Count
        missing_human_board_items = $missingHumanBoardIds.Count
        unknown_human_board_ids = $unknownHumanBoardIds.Count
        duplicate_human_board_ids = $duplicateHumanBoardIds.Count
        repository_path_checks = $pathChecks
        tracked_repository_paths = $trackedPathChecks
        issue_labels = $expectedLabelRows.Count
        issue_label_templates = [int](($expectedLabelRows | ForEach-Object { @($_.templates).Count } | Measure-Object -Sum).Sum)
        workflow_registry = $workflowRegistryIds.Count
        workflow_tokens_used = $workflowUsedIds.Count
        unreferenced_workflows = $unreferencedWorkflowIds.Count
    }
    checks = [ordered]@{
        exact_item_field_contract = -not (@($errors | Where-Object { $_ -like '*field*' }).Count)
        enum_contract = -not (@($errors | Where-Object { $_ -like '*Enum contract*' -or $_ -like '*invalid *' }).Count)
        unique_ids = ($ids.Count -eq @($board.items).Count -and $mirrorIds.Count -eq @($board.mirrors).Count)
        state_partitions_present = ($stateCounts.current_work -gt 0 -and $stateCounts.ready_for_adoption -gt 0 -and $stateCounts.future -gt 0)
        repository_paths_tracked = ($pathChecks -eq $trackedPathChecks)
        archive_layer_preserved = ([string]$board.board_role -ceq 'operational_layer')
        required_map_contract = ($requiredMaps.Count -gt 0 -and ($requiredMaps -join "`n") -ceq ($manifestMaps -join "`n"))
        required_maps_represented = ($missingRequiredMaps.Count -eq 0 -and $representedMapSet.Count -eq $requiredMaps.Count)
        queue_source_contract = (($queueSources -join "`n") -ceq ($expectedQueueSources -join "`n"))
        queue_sources_represented = ($missingQueueSources.Count -eq 0 -and $representedQueueSourceSet.Count -eq $queueSources.Count)
        human_board_complete = (
            $humanBoardRowIds.Count -eq $ids.Count -and
            $humanBoardIdSet.Count -eq $ids.Count -and
            $missingHumanBoardIds.Count -eq 0 -and
            $unknownHumanBoardIds.Count -eq 0 -and
            $duplicateHumanBoardIds.Count -eq 0
        )
        consumer_helper_contract = ([string]$board.consumer_helper -ceq $expectedConsumerHelper)
        claim_auditor_contract = ([string]$board.claim_auditor -ceq $expectedClaimAuditor)
        contributor_interface_contract = (
            [string]$board.claim_interface -ceq $expectedClaimInterface -and
            [string]$board.handback_interface -ceq $expectedHandbackInterface
        )
        issue_label_contract = $issueLabelContractPass
        workflow_registry_contract = (
            $workflowContractPass -and
            $workflowRegistryIds.Count -eq $workflowUsedIds.Count -and
            $workflowRowIds.Count -eq $humanWorkflowIds.Count -and
            $unreferencedWorkflowIds.Count -eq 0
        )
        snapshot_policy_contract = (
            [string]$board.snapshot_policy.stable_locator_ref -ceq 'main' -and
            [string]$board.snapshot_policy.immutable_unit -ceq 'human_approved_exact_commit' -and
            ($snapshotPaths -join "`n") -ceq ($expectedSnapshotPaths -join "`n") -and
            ($snapshotChecks -join "`n") -ceq ($expectedSnapshotChecks -join "`n") -and
            $board.snapshot_policy.mixed_revisions_forbidden -ceq $true
        )
        external_network_queried = $false
        producer_files_mutated = $false
        compile_render_or_ocr_run = $false
        global_filesystem_search = $false
    }
}

$outputFull = if ([IO.Path]::IsPathRooted($OutputPath)) {
    [IO.Path]::GetFullPath($OutputPath)
}
else {
    [IO.Path]::GetFullPath((Join-Path $repoRoot $OutputPath))
}
$outputDirectory = [IO.Path]::GetDirectoryName($outputFull)
if (-not [IO.Directory]::Exists($outputDirectory)) { throw "Output directory does not exist: $outputDirectory" }
$json = (($report | ConvertTo-Json -Depth 20).Replace("`r`n", "`n")) + "`n"
[IO.File]::WriteAllText($outputFull, $json, $utf8)

[ordered]@{
    status = $report.status
    items = $report.aggregate.items
    mirrors = $report.aggregate.mirrors
    paths = $report.aggregate.repository_path_checks
    errors = $errors.Count
    output = $OutputPath.Replace('\', '/')
} | ConvertTo-Json -Compress

if ($errors.Count -gt 0) { exit 1 }
