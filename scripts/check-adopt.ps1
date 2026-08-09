[CmdletBinding()]
param(
    [string]$InputPath = 'manifests/adopt.json',
    [string]$SchemaPath = 'manifests/adopt.schema.json',
    [string]$ValidationPath = 'manifests/adopt.check.json',
    [string]$LabelPath = '.github/labels.json',
    [string]$OutputPath = 'manifests/adopt.check.json',
    [string]$ObservedDate = (Get-Date -Format 'yyyy-MM-dd'),
    [switch]$SparseCheckout
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
    & git ls-files --error-unmatch -- $relative 2>$null | Out-Null
    if ($LASTEXITCODE -ne 0) {
        Add-Error "$Context path is not tracked by Git: $Path"
        return
    }
    if (-not [IO.File]::Exists($full) -and -not $SparseCheckout) {
        Add-Error "$Context path does not exist: $Path"
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
$expectedCertificationDefault = 'no_certification_asserted'
$certificationDefaultPass = $true
if ([string]$board.item_certification_default -cne $expectedCertificationDefault) {
    Add-Error 'Board item_certification_default must be no_certification_asserted.'
    $certificationDefaultPass = $false
}
if (-not (@($schema.required) -ccontains 'item_certification_default')) {
    Add-Error 'Schema must require item_certification_default.'
    $certificationDefaultPass = $false
}
if ([string]$schema.properties.item_certification_default.const -cne $expectedCertificationDefault) {
    Add-Error 'Schema item_certification_default const is not no_certification_asserted.'
    $certificationDefaultPass = $false
}
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

$expectedOwnershipFields = [string[]]@(
    'named_owner_required_for', 'null_owner_means', 'null_owner_allowed_for',
    'unclaimed_scope_prefix', 'claims_are_nonexclusive'
)
$ownershipContractPass = $true
Test-ExactFields -Value $board.ownership_policy -Expected $expectedOwnershipFields -Context 'ownership_policy'
if ((@($board.ownership_policy.named_owner_required_for) -join "`n") -cne 'current_work') {
    Add-Error 'ownership_policy named_owner_required_for must be exactly current_work.'
    $ownershipContractPass = $false
}
if ([string]$board.ownership_policy.null_owner_means -cne 'unclaimed') {
    Add-Error 'ownership_policy null_owner_means must be unclaimed.'
    $ownershipContractPass = $false
}
if ((@($board.ownership_policy.null_owner_allowed_for) -join "`n") -cne "ready_for_adoption`nfuture") {
    Add-Error 'ownership_policy null_owner_allowed_for must be ready_for_adoption then future.'
    $ownershipContractPass = $false
}
if ([string]$board.ownership_policy.unclaimed_scope_prefix -cne 'unclaimed') {
    Add-Error 'ownership_policy unclaimed_scope_prefix must be unclaimed.'
    $ownershipContractPass = $false
}
if ([bool]$board.ownership_policy.claims_are_nonexclusive -ne $true) {
    Add-Error 'ownership_policy claims_are_nonexclusive must be true.'
    $ownershipContractPass = $false
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
$humanIndexErrorStart = $errors.Count
Test-RepoPath -Path ([string]$board.human_index) -Context 'human_index' -Required $true
$humanIndexPath = [string]$board.human_index
$humanIndexFull = [IO.Path]::GetFullPath((Join-Path $repoRoot $humanIndexPath))
$humanIndexBytes = if ([IO.File]::Exists($humanIndexFull)) { [IO.File]::ReadAllBytes($humanIndexFull) } else { [byte[]]@() }
if ($humanIndexBytes.Length -ge 3 -and
    $humanIndexBytes[0] -eq 0xEF -and
    $humanIndexBytes[1] -eq 0xBB -and
    $humanIndexBytes[2] -eq 0xBF) {
    Add-Error 'human_index contains a UTF-8 BOM.'
}
$humanIndexText = $utf8.GetString($humanIndexBytes)
if ($humanIndexText.Contains("`r")) { Add-Error 'human_index must use LF line endings.' }
$actualIndexRows = [string[]]@($humanIndexText.Split("`n") | Where-Object { $_ -cmatch '^\| `[^`]+` \|' })
$indexKeys = [Collections.Generic.List[string]]::new()
$indexRowsByKey = [Collections.Generic.Dictionary[string,string]]::new([StringComparer]::Ordinal)
$indexAuthors = [Collections.Generic.HashSet[string]]::new([StringComparer]::Ordinal)
$indexWorks = [Collections.Generic.HashSet[string]]::new([StringComparer]::Ordinal)
$indexSeries = [Collections.Generic.HashSet[string]]::new([StringComparer]::Ordinal)
$indexLanguages = [Collections.Generic.HashSet[string]]::new([StringComparer]::Ordinal)
$indexCorpora = [Collections.Generic.HashSet[string]]::new([StringComparer]::Ordinal)
foreach ($item in @($board.items)) {
    $series = if ($null -eq $item.series) { '—' } else { [string]$item.series }
    $seriesKey = if ($null -eq $item.series) { '' } else { [string]$item.series }
    $languageDisplay = (@($item.languages) | ForEach-Object { "``$([string]$_)``" }) -join ', '
    $ownerDisplay = if ($null -eq $item.owner) { 'Unclaimed' } else { [string]$item.owner }
    $key = "$( [string]$item.corpus )`t$( [string]$item.author )`t$seriesKey`t$( [string]$item.work )`t$( [string]$item.id )"
    $row = "| ``$([string]$item.corpus)`` | $([string]$item.author) | $([string]$item.work) | $series | $languageDisplay | ``$([string]$item.lane_state)`` | ``$([string]$item.priority)`` | ``$([string]$item.readiness)`` | ``$([string]$item.coverage_state)`` | $([string]$item.next_cursor) | $ownerDisplay | ``$([string]$item.id)`` |"
    $indexKeys.Add($key)
    $indexRowsByKey.Add($key, $row)
    [void]$indexAuthors.Add([string]$item.author)
    [void]$indexWorks.Add([string]$item.work)
    if ($null -ne $item.series) { [void]$indexSeries.Add([string]$item.series) }
    foreach ($language in @($item.languages)) { [void]$indexLanguages.Add([string]$language) }
    [void]$indexCorpora.Add([string]$item.corpus)
}
$sortedIndexKeys = [string[]]@($indexKeys)
[Array]::Sort($sortedIndexKeys, [StringComparer]::Ordinal)
$expectedIndexRows = [Collections.Generic.List[string]]::new()
foreach ($key in $sortedIndexKeys) { $expectedIndexRows.Add($indexRowsByKey[$key]) }
if (($actualIndexRows -join "`n") -cne ($expectedIndexRows -join "`n")) {
    Add-Error 'human_index rows do not exactly match the board dimensions and ordinal order.'
}
$expectedIndexFooter = "Rows: $(@($board.items).Count). Named current coordinators: $(@($board.items | Where-Object { $null -ne $_.owner }).Count). Deliberately unclaimed rows: $(@($board.items | Where-Object { $null -eq $_.owner }).Count). Claims and mirrors remain nonexclusive."
if (-not $humanIndexText.Contains($expectedIndexFooter)) {
    Add-Error 'human_index footer does not match board ownership totals.'
}
$humanIndexContractPass = ($errors.Count -eq $humanIndexErrorStart)
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
$queueSnapshotContractPass = $true
$queueSnapshotRows = [Collections.Generic.List[object]]::new()
$queueSnapshotBytes = [long]0
$queueSnapshot = @($board.queue_snapshot)
if ($queueSnapshot.Count -ne $queueSources.Count) {
    Add-Error 'queue_snapshot row count does not match queue_sources.'
    $queueSnapshotContractPass = $false
}
for ($index = 0; $index -lt $queueSources.Count; $index++) {
    if ($index -ge $queueSnapshot.Count) { break }
    $row = $queueSnapshot[$index]
    $context = "queue_snapshot[$index]"
    Test-ExactFields -Value $row -Expected ([string[]]@('path', 'bytes', 'sha256')) -Context $context
    $path = [string]$row.path
    if ($path -cne $queueSources[$index]) {
        Add-Error "$context path does not match queue_sources order."
        $queueSnapshotContractPass = $false
    }
    $full = [IO.Path]::GetFullPath((Join-Path $repoRoot $path))
    $bytes = if ([IO.File]::Exists($full)) { [IO.File]::ReadAllBytes($full) } else { [byte[]]@() }
    $sha256 = if ($bytes.Length -gt 0) { Get-Sha256 -Bytes $bytes } else { Get-Sha256 -Bytes ([byte[]]@()) }
    if ([long]$row.bytes -ne $bytes.Length) {
        Add-Error "$context byte length does not match the tracked queue source."
        $queueSnapshotContractPass = $false
    }
    if ([string]$row.sha256 -cne $sha256) {
        Add-Error "$context SHA-256 does not match the tracked queue source."
        $queueSnapshotContractPass = $false
    }
    $queueSnapshotBytes += $bytes.Length
    $queueSnapshotRows.Add([ordered]@{
        path = $path.Replace('\', '/')
        bytes = $bytes.Length
        sha256 = $sha256
    })
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
$consumerHelperContractPass = $true
if ([string]$board.consumer_helper -cne $expectedConsumerHelper) {
    Add-Error 'consumer_helper does not match the exact v1 helper path.'
    $consumerHelperContractPass = $false
}
Test-RepoPath -Path ([string]$board.consumer_helper) -Context 'consumer_helper' -Required $true
$expectedConsumerModes = [string[]]@('raw_github', 'local_git_object_database')
$consumerModes = [string[]]@($board.consumer_modes)
Test-UniqueStrings -Values $consumerModes -Context 'consumer_modes' -RequireNonEmpty $true
if (($consumerModes -join "`n") -cne ($expectedConsumerModes -join "`n")) {
    Add-Error 'consumer_modes does not match the exact online/offline transport contract.'
    $consumerHelperContractPass = $false
}
$consumerHelperFull = [IO.Path]::GetFullPath((Join-Path $repoRoot $expectedConsumerHelper))
if ([IO.File]::Exists($consumerHelperFull)) {
    $consumerHelperText = $utf8.GetString([IO.File]::ReadAllBytes($consumerHelperFull))
    foreach ($token in @('GitObjectSource', '--git', 'cat-file', 'GIT_NO_LAZY_FETCH', 'lazy_fetch_disabled', 'local_git_object_database', 'raw_github')) {
        if (-not $consumerHelperText.Contains($token, [StringComparison]::Ordinal)) {
            Add-Error "consumer_helper is missing required transport token: $token"
            $consumerHelperContractPass = $false
        }
    }
}
else {
    $consumerHelperContractPass = $false
}
$expectedConsumerRegression = 'scripts/test-adopt-offline.py'
$consumerRegressionContractPass = $true
if ([string]$board.consumer_regression -cne $expectedConsumerRegression) {
    Add-Error 'consumer_regression does not match the exact promisor-clone regression path.'
    $consumerRegressionContractPass = $false
}
Test-RepoPath -Path ([string]$board.consumer_regression) -Context 'consumer_regression' -Required $true
$consumerRegressionFull = [IO.Path]::GetFullPath((Join-Path $repoRoot $expectedConsumerRegression))
if ([IO.File]::Exists($consumerRegressionFull)) {
    $consumerRegressionText = $utf8.GetString([IO.File]::ReadAllBytes($consumerRegressionFull))
    foreach ($token in @('remote.origin.promisor', 'extensions.partialClone', '127.0.0.1:9', 'missing_blob_remote_attempt', 'lazy_fetch_disabled')) {
        if (-not $consumerRegressionText.Contains($token, [StringComparison]::Ordinal)) {
            Add-Error "consumer_regression is missing required promisor-test token: $token"
            $consumerRegressionContractPass = $false
        }
    }
}
else {
    $consumerRegressionContractPass = $false
}
$expectedClaimAuditor = 'scripts/check-claims.py'
$claimAuditorContractPass = $true
if ([string]$board.claim_auditor -cne $expectedClaimAuditor) {
    Add-Error 'claim_auditor does not match the exact v1 auditor path.'
    $claimAuditorContractPass = $false
}
Test-RepoPath -Path ([string]$board.claim_auditor) -Context 'claim_auditor' -Required $true
$expectedClaimBoardModes = [string[]]@('raw_github', 'local_git_object_database')
$expectedClaimIssueModes = [string[]]@('public_github_api', 'json_fixture')
$claimBoardModes = [string[]]@($board.claim_auditor_modes.board)
$claimIssueModes = [string[]]@($board.claim_auditor_modes.issues)
Test-UniqueStrings -Values $claimBoardModes -Context 'claim_auditor_modes.board' -RequireNonEmpty $true
Test-UniqueStrings -Values $claimIssueModes -Context 'claim_auditor_modes.issues' -RequireNonEmpty $true
if (($claimBoardModes -join "`n") -cne ($expectedClaimBoardModes -join "`n")) {
    Add-Error 'claim_auditor_modes.board does not match the exact transport contract.'
    $claimAuditorContractPass = $false
}
if (($claimIssueModes -join "`n") -cne ($expectedClaimIssueModes -join "`n")) {
    Add-Error 'claim_auditor_modes.issues does not match the exact transport contract.'
    $claimAuditorContractPass = $false
}
$claimAuditorFull = [IO.Path]::GetFullPath((Join-Path $repoRoot $expectedClaimAuditor))
if ([IO.File]::Exists($claimAuditorFull)) {
    $claimAuditorText = $utf8.GetString([IO.File]::ReadAllBytes($claimAuditorFull))
    foreach ($token in @('--git', '--issues-file', 'board transport is not declared', 'issue transport is not declared')) {
        if (-not $claimAuditorText.Contains($token, [StringComparison]::Ordinal)) {
            Add-Error "claim_auditor is missing required transport token: $token"
            $claimAuditorContractPass = $false
        }
    }
}
else {
    $claimAuditorContractPass = $false
}
$expectedClaimRegression = 'scripts/test-claims.py'
$claimRegressionContractPass = $true
if ([string]$board.claim_regression -cne $expectedClaimRegression) {
    Add-Error 'claim_regression does not match the exact offline fixture-regression path.'
    $claimRegressionContractPass = $false
}
Test-RepoPath -Path ([string]$board.claim_regression) -Context 'claim_regression' -Required $true
$claimRegressionFull = [IO.Path]::GetFullPath((Join-Path $repoRoot $expectedClaimRegression))
if ([IO.File]::Exists($claimRegressionFull)) {
    $claimRegressionText = $utf8.GetString([IO.File]::ReadAllBytes($claimRegressionFull))
    foreach ($token in @('valid_fixture', 'invalid_fixture', 'not-a-board-row', 'local_git_object_database', 'json_fixture', 'external_network_queried')) {
        if (-not $claimRegressionText.Contains($token, [StringComparison]::Ordinal)) {
            Add-Error "claim_regression is missing required lifecycle token: $token"
            $claimRegressionContractPass = $false
        }
    }
}
else {
    $claimRegressionContractPass = $false
}
$expectedCiWorkflow = '.github/workflows/adopt.yml'
$expectedCiEvents = [string[]]@('pull_request', 'push_main', 'workflow_dispatch')
$expectedCiChecks = [string[]]@(
    'board_schema_maps',
    'exact_local_consumer',
    'promisor_no_lazy_fetch',
    'claim_lifecycle_fixtures'
)
$continuousValidationContractPass = $true
$expectedContinuousValidationFields = [string[]]@('workflow', 'checkout', 'events', 'checks', 'pinned_actions', 'corpus_builds')
Test-ExactFields -Value $board.continuous_validation -Expected $expectedContinuousValidationFields -Context 'continuous_validation'
if ([string]$board.continuous_validation.workflow -cne $expectedCiWorkflow) {
    Add-Error 'continuous_validation workflow does not match the exact adoption workflow path.'
    $continuousValidationContractPass = $false
}
if ([string]$board.continuous_validation.checkout -cne 'blobless_sparse_metadata') {
    Add-Error 'continuous_validation checkout must remain blobless_sparse_metadata.'
    $continuousValidationContractPass = $false
}
$ciEvents = [string[]]@($board.continuous_validation.events)
$ciChecks = [string[]]@($board.continuous_validation.checks)
if (($ciEvents -join "`n") -cne ($expectedCiEvents -join "`n")) {
    Add-Error 'continuous_validation events do not match the exact pull-request/main/manual contract.'
    $continuousValidationContractPass = $false
}
if (($ciChecks -join "`n") -cne ($expectedCiChecks -join "`n")) {
    Add-Error 'continuous_validation checks do not match the exact sparse gate contract.'
    $continuousValidationContractPass = $false
}
if ($board.continuous_validation.pinned_actions -cne $true) {
    Add-Error 'continuous_validation must require SHA-pinned actions.'
    $continuousValidationContractPass = $false
}
if ($board.continuous_validation.corpus_builds -cne $false) {
    Add-Error 'continuous_validation must exclude corpus builds.'
    $continuousValidationContractPass = $false
}
Test-RepoPath -Path ([string]$board.continuous_validation.workflow) -Context 'continuous_validation.workflow' -Required $true
$ciWorkflowFull = [IO.Path]::GetFullPath((Join-Path $repoRoot $expectedCiWorkflow))
if ([IO.File]::Exists($ciWorkflowFull)) {
    $ciWorkflowText = $utf8.GetString([IO.File]::ReadAllBytes($ciWorkflowFull))
    foreach ($token in @(
        'pull_request:',
        'push:',
        'workflow_dispatch:',
        'permissions:',
        'contents: read',
        'filter: blob:none',
        'sparse-checkout-cone-mode: false',
        '-SparseCheckout',
        'fbc6f3992d24b796d5a048ff273f7fcc4a7b6c09',
        'ece7cb06caefa5fff74198d8649806c4678c61a1',
        'check-adopt.ps1',
        'get-adopt.py',
        'test-adopt-offline.py',
        'test-claims.py'
    )) {
        if (-not $ciWorkflowText.Contains($token, [StringComparison]::Ordinal)) {
            Add-Error "continuous_validation workflow is missing required sparse-gate token: $token"
            $continuousValidationContractPass = $false
        }
    }
}
else {
    $continuousValidationContractPass = $false
}

$ids = [Collections.Generic.HashSet[string]]::new([StringComparer]::Ordinal)
$stateCounts = [ordered]@{ current_work = 0; ready_for_adoption = 0; future = 0 }
$namedOwnerRows = 0
$unclaimedOwnerRows = 0
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

    if ($null -eq $item.owner) { $unclaimedOwnerRows++ } else { $namedOwnerRows++ }

    switch ([string]$item.lane_state) {
        'current_work' {
            if ([string]::IsNullOrWhiteSpace([string]$item.owner)) {
                Add-Error "$context current work requires a named owner."
                $ownershipContractPass = $false
            }
            if ([string]$item.readiness -cne 'active') { Add-Error "$context current work must have active readiness." }
            if ([string]$item.adoption_status -cne 'maintained_parallel_review_welcome') {
                Add-Error "$context current work has incompatible adoption_status."
                $ownershipContractPass = $false
            }
            if ([string]$item.owner_scope -cmatch '^unclaimed(?: |$)') {
                Add-Error "$context named-owner scope cannot be unclaimed."
                $ownershipContractPass = $false
            }
        }
        'ready_for_adoption' {
            if ([string]::IsNullOrWhiteSpace([string]$item.archive_path)) { Add-Error "$context adoption-ready work requires archive_path." }
            if ([string]$item.readiness -cin @('active', 'source_discovery_first')) { Add-Error "$context adoption-ready work has incompatible readiness." }
            if ($null -ne $item.owner) {
                Add-Error "$context adoption-ready work must have null owner meaning unclaimed."
                $ownershipContractPass = $false
            }
            if ([string]$item.adoption_status -cne 'open_parallel_mirrors_welcome') {
                Add-Error "$context adoption-ready work has incompatible adoption_status."
                $ownershipContractPass = $false
            }
            if ([string]$item.owner_scope -cnotmatch '^unclaimed(?: |$)') {
                Add-Error "$context adoption-ready owner_scope must begin with unclaimed."
                $ownershipContractPass = $false
            }
        }
        'future' {
            if ($null -ne $item.owner) {
                Add-Error "$context future work must have null owner meaning unclaimed."
                $ownershipContractPass = $false
            }
            if ([string]$item.readiness -cne 'source_discovery_first') { Add-Error "$context future work must require source discovery." }
            if ([string]$item.adoption_status -cne 'future_evidence_needed') {
                Add-Error "$context future work has incompatible adoption_status."
                $ownershipContractPass = $false
            }
            if ([string]$item.owner_scope -cnotmatch '^unclaimed(?: |$)') {
                Add-Error "$context future owner_scope must begin with unclaimed."
                $ownershipContractPass = $false
            }
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

$worktreeBaseCommit = (& git rev-parse HEAD).Trim()
if ($LASTEXITCODE -ne 0) { throw 'Could not resolve HEAD.' }
& git diff --quiet --no-ext-diff
$unstagedChanges = $LASTEXITCODE -ne 0
& git diff --cached --quiet --no-ext-diff
$stagedChanges = $LASTEXITCODE -ne 0
$worktreeDirty = $unstagedChanges -or $stagedChanges
$report = [ordered]@{
    schema = 'math-commons-adoption-check-v1'
    status = if ($errors.Count -eq 0) { 'PASS' } else { 'FAIL' }
    errors = @($errors)
    observed_date = $ObservedDate
    input_mode = if ($SparseCheckout) { 'named_worktree_files_with_sparse_tracked_path_checks' } else { 'named_worktree_files' }
    worktree_base_commit = $worktreeBaseCommit
    worktree_dirty = $worktreeDirty
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
    human_index = [ordered]@{
        path = $humanIndexPath.Replace('\', '/')
        bytes = $humanIndexBytes.Length
        sha256 = if ($humanIndexBytes.Length -gt 0) { Get-Sha256 -Bytes $humanIndexBytes } else { $null }
        rows = $actualIndexRows.Count
        authors = $indexAuthors.Count
        works = $indexWorks.Count
        series = $indexSeries.Count
        languages = $indexLanguages.Count
        corpora = $indexCorpora.Count
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
    consumer_modes = @($consumerModes)
    consumer_regression = [string]$board.consumer_regression
    claim_auditor = [string]$board.claim_auditor
    claim_auditor_modes = [ordered]@{
        board = @($claimBoardModes)
        issues = @($claimIssueModes)
    }
    claim_regression = [string]$board.claim_regression
    continuous_validation = [ordered]@{
        workflow = [string]$board.continuous_validation.workflow
        checkout = [string]$board.continuous_validation.checkout
        events = @($ciEvents)
        checks = @($ciChecks)
        pinned_actions = [bool]$board.continuous_validation.pinned_actions
        corpus_builds = [bool]$board.continuous_validation.corpus_builds
    }
    ownership_policy = [ordered]@{
        named_owner_required_for = @($board.ownership_policy.named_owner_required_for)
        null_owner_means = [string]$board.ownership_policy.null_owner_means
        null_owner_allowed_for = @($board.ownership_policy.null_owner_allowed_for)
        unclaimed_scope_prefix = [string]$board.ownership_policy.unclaimed_scope_prefix
        claims_are_nonexclusive = [bool]$board.ownership_policy.claims_are_nonexclusive
    }
    item_certification_default = [string]$board.item_certification_default
    queue_snapshot = @($queueSnapshotRows)
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
        queue_snapshot_sources = $queueSnapshotRows.Count
        queue_snapshot_bytes = $queueSnapshotBytes
        human_board_rows = $humanBoardRowIds.Count
        represented_human_board_items = $humanBoardIdSet.Count
        missing_human_board_items = $missingHumanBoardIds.Count
        unknown_human_board_ids = $unknownHumanBoardIds.Count
        duplicate_human_board_ids = $duplicateHumanBoardIds.Count
        human_index_rows = $actualIndexRows.Count
        human_index_authors = $indexAuthors.Count
        human_index_works = $indexWorks.Count
        human_index_series = $indexSeries.Count
        human_index_languages = $indexLanguages.Count
        human_index_corpora = $indexCorpora.Count
        repository_path_checks = $pathChecks
        tracked_repository_paths = $trackedPathChecks
        issue_labels = $expectedLabelRows.Count
        issue_label_templates = [int](($expectedLabelRows | ForEach-Object { @($_.templates).Count } | Measure-Object -Sum).Sum)
        consumer_modes = $consumerModes.Count
        claim_auditor_board_modes = $claimBoardModes.Count
        claim_auditor_issue_modes = $claimIssueModes.Count
        continuous_validation_checks = $ciChecks.Count
        workflow_registry = $workflowRegistryIds.Count
        workflow_tokens_used = $workflowUsedIds.Count
        unreferenced_workflows = $unreferencedWorkflowIds.Count
        named_owner_rows = $namedOwnerRows
        unclaimed_owner_rows = $unclaimedOwnerRows
        items_inheriting_certification_default = @($board.items).Count
    }
    checks = [ordered]@{
        exact_item_field_contract = -not (@($errors | Where-Object { $_ -like '*field*' }).Count)
        enum_contract = -not (@($errors | Where-Object { $_ -like '*Enum contract*' -or $_ -like '*invalid *' }).Count)
        unique_ids = ($ids.Count -eq @($board.items).Count -and $mirrorIds.Count -eq @($board.mirrors).Count)
        state_partitions_present = ($stateCounts.current_work -gt 0 -and $stateCounts.ready_for_adoption -gt 0 -and $stateCounts.future -gt 0)
        repository_paths_tracked = ($pathChecks -eq $trackedPathChecks)
        archive_layer_preserved = ([string]$board.board_role -ceq 'operational_layer')
        certification_default_contract = (
            $certificationDefaultPass -and
            [string]$board.item_certification_default -ceq $expectedCertificationDefault
        )
        required_map_contract = ($requiredMaps.Count -gt 0 -and ($requiredMaps -join "`n") -ceq ($manifestMaps -join "`n"))
        required_maps_represented = ($missingRequiredMaps.Count -eq 0 -and $representedMapSet.Count -eq $requiredMaps.Count)
        queue_source_contract = (($queueSources -join "`n") -ceq ($expectedQueueSources -join "`n"))
        queue_sources_represented = ($missingQueueSources.Count -eq 0 -and $representedQueueSourceSet.Count -eq $queueSources.Count)
        queue_snapshot_contract = (
            $queueSnapshotContractPass -and
            $queueSnapshotRows.Count -eq $queueSources.Count
        )
        human_board_complete = (
            $humanBoardRowIds.Count -eq $ids.Count -and
            $humanBoardIdSet.Count -eq $ids.Count -and
            $missingHumanBoardIds.Count -eq 0 -and
            $unknownHumanBoardIds.Count -eq 0 -and
            $duplicateHumanBoardIds.Count -eq 0
        )
        human_dimension_index_complete = (
            $humanIndexContractPass -and
            $actualIndexRows.Count -eq @($board.items).Count
        )
        consumer_helper_contract = (
            $consumerHelperContractPass -and
            [string]$board.consumer_helper -ceq $expectedConsumerHelper -and
            ($consumerModes -join "`n") -ceq ($expectedConsumerModes -join "`n")
        )
        consumer_regression_contract = (
            $consumerRegressionContractPass -and
            [string]$board.consumer_regression -ceq $expectedConsumerRegression
        )
        claim_auditor_contract = (
            $claimAuditorContractPass -and
            [string]$board.claim_auditor -ceq $expectedClaimAuditor -and
            ($claimBoardModes -join "`n") -ceq ($expectedClaimBoardModes -join "`n") -and
            ($claimIssueModes -join "`n") -ceq ($expectedClaimIssueModes -join "`n")
        )
        claim_regression_contract = (
            $claimRegressionContractPass -and
            [string]$board.claim_regression -ceq $expectedClaimRegression
        )
        continuous_validation_contract = (
            $continuousValidationContractPass -and
            [string]$board.continuous_validation.workflow -ceq $expectedCiWorkflow -and
            [string]$board.continuous_validation.checkout -ceq 'blobless_sparse_metadata' -and
            ($ciEvents -join "`n") -ceq ($expectedCiEvents -join "`n") -and
            ($ciChecks -join "`n") -ceq ($expectedCiChecks -join "`n") -and
            $board.continuous_validation.pinned_actions -ceq $true -and
            $board.continuous_validation.corpus_builds -ceq $false
        )
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
        ownership_semantics = (
            $ownershipContractPass -and
            $namedOwnerRows -eq $stateCounts.current_work -and
            $unclaimedOwnerRows -eq ($stateCounts.ready_for_adoption + $stateCounts.future)
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
