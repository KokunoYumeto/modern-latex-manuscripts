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

function Get-IssueTemplateIds {
    param([string]$Text)
    $values = [Collections.Generic.List[string]]::new()
    foreach ($match in [regex]::Matches($Text, '(?m)^    id: (?<value>[a-z][a-z0-9_]*)\s*$')) {
        $values.Add($match.Groups['value'].Value)
    }
    return [string[]]$values.ToArray()
}

function Get-IssueTemplateMappingErrors {
    param(
        [string]$Text,
        [string]$Context
    )
    $problems = [Collections.Generic.List[string]]::new()
    foreach ($key in @('title', 'description', 'labels', 'body')) {
        $count = @([regex]::Matches($Text, "(?m)^$([regex]::Escape($key)):")).Count
        if ($count -ne 1) {
            $problems.Add("$Context must contain exactly one top-level $key key; observed $count.")
        }
    }
    $typeBlocks = @([regex]::Matches($Text, '(?ms)^  - type: (?<type>[a-z]+)\n(?<body>.*?)(?=^  - type: |\z)'))
    foreach ($blockMatch in $typeBlocks) {
        $type = $blockMatch.Groups['type'].Value
        $body = $blockMatch.Groups['body'].Value
        $ids = @([regex]::Matches($body, '(?m)^    id: (?<value>[a-z][a-z0-9_]*)$'))
        $expectedIds = if ($type -ceq 'markdown') { 0 } else { 1 }
        if ($ids.Count -ne $expectedIds) {
            $problems.Add("$Context $type block must contain exactly $expectedIds id key(s); observed $($ids.Count).")
        }
        foreach ($key in @('attributes', 'validations')) {
            $count = @([regex]::Matches($body, "(?m)^    $([regex]::Escape($key)):")).Count
            if ($count -gt 1) {
                $problems.Add("$Context $type block contains duplicate $key keys.")
            }
        }
        foreach ($key in @('label', 'description', 'placeholder', 'value', 'options', 'default', 'multiple', 'required')) {
            $count = @([regex]::Matches($body, "(?m)^      $([regex]::Escape($key)):")).Count
            if ($count -gt 1) {
                $problems.Add("$Context $type block contains duplicate $key keys at one mapping level.")
            }
        }
        $optionBlocks = @([regex]::Matches($body, '(?ms)^        - label: .+\n(?<option>.*?)(?=^        - label: |\z)'))
        foreach ($optionBlock in $optionBlocks) {
            $requiredCount = @([regex]::Matches($optionBlock.Groups['option'].Value, '(?m)^          required:')).Count
            if ($requiredCount -gt 1) {
                $problems.Add("$Context $type checkbox option contains duplicate required keys.")
            }
        }
    }
    return [string[]]$problems.ToArray()
}

$duplicateMappingProbe = @'
title: "[Probe] "
title: "[Conflicting] "
description: Probe
labels:
  - adoption
body:
  - type: input
    id: probe
    attributes:
      label: First
      label: Conflicting
'@
$duplicateProbeErrors = [string[]]@(Get-IssueTemplateMappingErrors -Text $duplicateMappingProbe -Context 'duplicate-key probe')
$issueTemplateDuplicateKeyContractPass = $true
if (-not ($duplicateProbeErrors | Where-Object { $_.Contains('top-level title', [StringComparison]::Ordinal) }) -or
    -not ($duplicateProbeErrors | Where-Object { $_.Contains('duplicate label', [StringComparison]::Ordinal) })) {
    Add-Error 'Issue-template duplicate-key detector regression failed.'
    $issueTemplateDuplicateKeyContractPass = $false
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

if ($board.schema -cne 'math-commons-adoption-v2') { Add-Error 'Unexpected board schema.' }
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
    'coverage_state', 'coverage_class', 'adoption_status', 'priority', 'readiness', 'owner',
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
if (($boardFields -join "`n") -cne ($expectedFields -join "`n")) { Add-Error 'Item fields are not the exact v2 ordered field contract.' }
if (($mirrorFields -join "`n") -cne ($expectedMirrorFields -join "`n")) { Add-Error 'Mirror fields are not the exact v1 ordered field contract.' }
if (($workflowFields -join "`n") -cne ($expectedWorkflowFields -join "`n")) { Add-Error 'Workflow fields are not the exact v1 ordered field contract.' }

$expectedEnums = [ordered]@{
    lane_state = [string[]]@('current_work', 'ready_for_adoption', 'future')
    coverage_class = [string[]]@('complete', 'active', 'partial', 'scattered', 'weak', 'source_only', 'unworked')
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
    'unclaimed_scope_prefix', 'claims_are_nonexclusive',
    'ready_for_adoption_reason', 'future_reason', 'absence_inference_forbidden'
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
if ([string]$board.ownership_policy.ready_for_adoption_reason -cne 'current_project_compute_not_allocated') {
    Add-Error 'ownership_policy ready_for_adoption_reason must preserve the explicit compute-capacity reason.'
    $ownershipContractPass = $false
}
if ([string]$board.ownership_policy.future_reason -cne 'source_or_cursor_evidence_not_yet_bound') {
    Add-Error 'ownership_policy future_reason must preserve the evidence gate.'
    $ownershipContractPass = $false
}
if ([bool]$board.ownership_policy.absence_inference_forbidden -ne $true) {
    Add-Error 'ownership_policy must forbid inferring corpus absence from board state.'
    $ownershipContractPass = $false
}

$stacksReferenceLayerContractPass = $true
$stacksErrorStart = $errors.Count
$stacks = $board.stacks_reference_layer
$expectedStacksFields = [string[]]@(
    'status', 'human_spec', 'intake_form', 'governance', 'upstream', 'layer_order',
    'overlay_contents', 'modified_edition', 'compatibility_targets',
    'public_evidence', 'write_boundary'
)
Test-ExactFields -Value $stacks -Expected $expectedStacksFields -Context 'stacks_reference_layer'
$expectedStacksUpstreamFields = [string[]]@('role', 'repository_binding', 'pin_status', 'acceptance_dependency', 'endorsement_implied')
$expectedStacksModifiedEditionFields = [string[]]@('optional', 'license', 'distinct_title_required', 'attribution_required', 'license_and_history_notices_required', 'upstream_endorsement_forbidden')
$expectedStacksEvidenceFields = [string[]]@('repository_binding', 'pull_requests', 'state', 'same_timestamp', 'public_comments', 'public_reviews', 'motive_inference')
Test-ExactFields -Value $stacks.upstream -Expected $expectedStacksUpstreamFields -Context 'stacks_reference_layer.upstream'
Test-ExactFields -Value $stacks.modified_edition -Expected $expectedStacksModifiedEditionFields -Context 'stacks_reference_layer.modified_edition'
Test-ExactFields -Value $stacks.public_evidence -Expected $expectedStacksEvidenceFields -Context 'stacks_reference_layer.public_evidence'
if ([string]$stacks.status -cne 'architecture_adopted_no_overlay_bytes') { Add-Error 'Stacks layer status must remain architecture-only until exact implementation bytes are bound.'; $stacksReferenceLayerContractPass = $false }
if ([string]$stacks.intake_form -cne 'https://github.com/KokunoYumeto/modern-latex-manuscripts/issues/new?template=stacks.yml') { Add-Error 'Stacks intake form differs from the dedicated exact-binding route.'; $stacksReferenceLayerContractPass = $false }
if ([string]$stacks.governance -cne 'mathematics_commons_independent') { Add-Error 'Stacks layer governance must remain independent under Mathematics Commons.'; $stacksReferenceLayerContractPass = $false }
if ([string]$stacks.upstream.role -cne 'respected_pinned_read_only_source_and_sync_target') { Add-Error 'Stacks upstream role must remain pinned and read-only.'; $stacksReferenceLayerContractPass = $false }
if ([string]$stacks.upstream.repository_binding -cne 'not_supplied_do_not_infer' -or [string]$stacks.upstream.pin_status -cne 'required_not_yet_bound') { Add-Error 'Stacks upstream repository and pin must remain explicitly unbound until exact intake.'; $stacksReferenceLayerContractPass = $false }
if ($stacks.upstream.acceptance_dependency -cne $false -or $stacks.upstream.endorsement_implied -cne $false) { Add-Error 'Stacks upstream acceptance or endorsement cannot gate the Commons layer.'; $stacksReferenceLayerContractPass = $false }
$expectedStacksLayers = [string[]]@('upstream_pin', 'commons_overlay', 'composed_build', 'optional_modified_edition', 'periodic_upstream_sync')
if ((@($stacks.layer_order) -join "`n") -cne ($expectedStacksLayers -join "`n")) { Add-Error 'Stacks layer order differs from the five-layer architecture.'; $stacksReferenceLayerContractPass = $false }
$expectedOverlayContents = [string[]]@('original additions', 'historical-source mappings', 'provenance', 'corrections', 'multilingual semantic links', 'stable Commons IDs', 'tests', 'review receipts')
if ((@($stacks.overlay_contents) -join "`n") -cne ($expectedOverlayContents -join "`n")) { Add-Error 'Stacks overlay content contract is incomplete or reordered.'; $stacksReferenceLayerContractPass = $false }
if ($stacks.modified_edition.optional -cne $true -or [string]$stacks.modified_edition.license -cne 'GFDL_compliant' -or $stacks.modified_edition.distinct_title_required -cne $true -or $stacks.modified_edition.attribution_required -cne $true -or $stacks.modified_edition.license_and_history_notices_required -cne $true -or $stacks.modified_edition.upstream_endorsement_forbidden -cne $true) { Add-Error 'Stacks optional modified-edition contract is incomplete.'; $stacksReferenceLayerContractPass = $false }
$expectedCompatibility = [string[]]@('sTeX/MMT', 'Lean Blueprint', 'formal-proof exports')
if ((@($stacks.compatibility_targets) -join "`n") -cne ($expectedCompatibility -join "`n")) { Add-Error 'Stacks compatibility targets differ from the architectural decision.'; $stacksReferenceLayerContractPass = $false }
if ([string]$stacks.public_evidence.repository_binding -cne 'not_supplied_do_not_infer' -or (@($stacks.public_evidence.pull_requests) -join ',') -cne '196,197' -or [string]$stacks.public_evidence.state -cne 'closed_unmerged' -or $stacks.public_evidence.same_timestamp -cne $true -or [int]$stacks.public_evidence.public_comments -ne 0 -or [int]$stacks.public_evidence.public_reviews -ne 0 -or [string]$stacks.public_evidence.motive_inference -cne 'forbidden') { Add-Error 'Stacks public-evidence boundary differs from the controlling handoff.'; $stacksReferenceLayerContractPass = $false }
if ([string]$stacks.write_boundary -cne 'commons_owned_namespaces_only') { Add-Error 'Stacks writes must remain inside Commons-owned namespaces.'; $stacksReferenceLayerContractPass = $false }
Test-RepoPath -Path ([string]$stacks.human_spec) -Context 'stacks_reference_layer.human_spec' -Required $true
Test-RepoPath -Path '.github/ISSUE_TEMPLATE/stacks.yml' -Context 'stacks_reference_layer.intake_form template' -Required $true
if ($errors.Count -ne $stacksErrorStart) { $stacksReferenceLayerContractPass = $false }

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
$humanIndexLines = [string[]]@($humanIndexText.Split("`n"))
$expectedIndexHeader = '| Corpus | Author | Work | Series | Languages | Lane | Priority | Readiness | Class | Coverage state | Next cursor | Owner | Allowed workflows | Board ID |'
$expectedIndexDelimiter = '|---|---|---|---|---|---|---|---|---|---|---|---|---|---|'
if (-not $humanIndexText.Contains("$expectedIndexHeader`n$expectedIndexDelimiter`n")) {
    Add-Error 'human_index header and delimiter are not the exact fourteen-column contract.'
}
$indexHeaderWidth = @($expectedIndexHeader.Substring(1, $expectedIndexHeader.Length - 2).Split('|')).Count
$indexDelimiterWidth = @($expectedIndexDelimiter.Substring(1, $expectedIndexDelimiter.Length - 2).Split('|')).Count
if ($indexHeaderWidth -ne 14 -or $indexDelimiterWidth -ne $indexHeaderWidth) {
    Add-Error 'human_index header/delimiter width contract is invalid.'
}
$actualIndexRows = [string[]]@($humanIndexText.Split("`n") | Where-Object { $_ -cmatch '^\| `[^`]+` \|' })
foreach ($row in $actualIndexRows) {
    $rowWidth = @($row.Substring(1, $row.Length - 2).Split('|')).Count
    if ($rowWidth -ne $indexHeaderWidth) {
        Add-Error "human_index row width $rowWidth differs from header width $indexHeaderWidth."
    }
}
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
    $workflowDisplay = (@($item.workflow) | ForEach-Object { "``$([string]$_)``" }) -join ', '
    $ownerDisplay = if ($null -eq $item.owner) { 'Unclaimed' } else { [string]$item.owner }
    $key = "$( [string]$item.corpus )`t$( [string]$item.author )`t$seriesKey`t$( [string]$item.work )`t$( [string]$item.id )"
    $row = "| ``$([string]$item.corpus)`` | $([string]$item.author) | $([string]$item.work) | $series | $languageDisplay | ``$([string]$item.lane_state)`` | ``$([string]$item.priority)`` | ``$([string]$item.readiness)`` | ``$([string]$item.coverage_class)`` | ``$([string]$item.coverage_state)`` | $([string]$item.next_cursor) | $ownerDisplay | $workflowDisplay | ``$([string]$item.id)`` |"
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
        templates = [string[]]@('.github/ISSUE_TEMPLATE/adopt.yml', '.github/ISSUE_TEMPLATE/handback.yml', '.github/ISSUE_TEMPLATE/stacks.yml')
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

$claimTemplateContractPass = $true
$claimTemplatePath = '.github/ISSUE_TEMPLATE/adopt.yml'
$claimTemplateFull = [IO.Path]::GetFullPath((Join-Path $repoRoot $claimTemplatePath))
$expectedClaimTemplateIds = [string[]]@(
    'board_id', 'intent', 'workflow', 'scope', 'inputs', 'mirror', 'checks', 'agreement'
)
if (-not [IO.File]::Exists($claimTemplateFull)) {
    Add-Error 'Adoption intake template is missing.'
    $claimTemplateContractPass = $false
}
else {
    $claimTemplateBytes = [IO.File]::ReadAllBytes($claimTemplateFull)
    if ($claimTemplateBytes.Length -ge 3 -and $claimTemplateBytes[0] -eq 0xEF -and $claimTemplateBytes[1] -eq 0xBB -and $claimTemplateBytes[2] -eq 0xBF) {
        Add-Error 'Adoption intake template contains a UTF-8 BOM.'
        $claimTemplateContractPass = $false
    }
    $claimTemplateText = $utf8.GetString($claimTemplateBytes)
    if ($claimTemplateText.Contains("`r")) {
        Add-Error 'Adoption intake template must use LF line endings.'
        $claimTemplateContractPass = $false
    }
    foreach ($mappingError in @(Get-IssueTemplateMappingErrors -Text $claimTemplateText -Context 'Adoption intake template')) {
        Add-Error $mappingError
        $claimTemplateContractPass = $false
        $issueTemplateDuplicateKeyContractPass = $false
    }
    $actualClaimTemplateIds = [string[]]@(Get-IssueTemplateIds -Text $claimTemplateText)
    if (($actualClaimTemplateIds -join "`n") -cne ($expectedClaimTemplateIds -join "`n")) {
        Add-Error 'Adoption intake template field IDs differ from the exact binding contract.'
        $claimTemplateContractPass = $false
    }
    $expectedClaimTemplateTypes = [ordered]@{
        board_id = 'input'; intent = 'dropdown'; workflow = 'dropdown'; scope = 'textarea'
        inputs = 'textarea'; mirror = 'input'; checks = 'textarea'; agreement = 'checkboxes'
    }
    $claimTemplateBlocks = @{}
    $claimTypeBlocks = @([regex]::Matches($claimTemplateText, '(?ms)^  - type: (?<type>[a-z]+)\n(?<body>.*?)(?=^  - type: |\z)'))
    foreach ($blockMatch in $claimTypeBlocks) {
        $blockBody = $blockMatch.Groups['body'].Value
        $idMatch = [regex]::Match($blockBody, '(?m)^    id: (?<id>[a-z][a-z0-9_]*)$')
        if ($idMatch.Success) {
            $claimTemplateBlocks[$idMatch.Groups['id'].Value] = [pscustomobject]@{
                type = $blockMatch.Groups['type'].Value
                body = $blockBody
            }
        }
    }
    if ($claimTypeBlocks.Count -ne 9 -or $claimTemplateBlocks.Count -ne 8) {
        Add-Error 'Adoption intake template must contain one markdown block and exactly eight identified field blocks.'
        $claimTemplateContractPass = $false
    }
    foreach ($fieldId in $expectedClaimTemplateTypes.Keys) {
        if (-not $claimTemplateBlocks.ContainsKey($fieldId) -or [string]$claimTemplateBlocks[$fieldId].type -cne [string]$expectedClaimTemplateTypes[$fieldId]) {
            Add-Error "Adoption intake field type differs for: $fieldId"
            $claimTemplateContractPass = $false
        }
    }
    $expectedClaimTemplateLabels = [ordered]@{
        board_id = 'Board ID'; intent = 'Intent'; workflow = 'Workflow token'; scope = 'Exact scope'
        inputs = 'Starting evidence'; mirror = 'Mirror or result URL'; checks = 'Planned or completed checks'; agreement = 'Traceability'
    }
    foreach ($fieldId in $expectedClaimTemplateLabels.Keys) {
        $expectedLabel = [regex]::Escape([string]$expectedClaimTemplateLabels[$fieldId])
        if (-not $claimTemplateBlocks.ContainsKey($fieldId) -or -not [regex]::IsMatch([string]$claimTemplateBlocks[$fieldId].body, "(?m)^      label: $expectedLabel`$")) {
            Add-Error "Adoption intake field label differs for: $fieldId"
            $claimTemplateContractPass = $false
        }
    }
    if (-not [regex]::IsMatch($claimTemplateText, '(?m)^title: "\[Adopt\] "$')) {
        Add-Error 'Adoption intake title prefix differs from the exact auditor route.'
        $claimTemplateContractPass = $false
    }
    foreach ($fieldId in @('board_id', 'intent', 'workflow', 'scope', 'inputs')) {
        if (-not $claimTemplateBlocks.ContainsKey($fieldId) -or -not [regex]::IsMatch([string]$claimTemplateBlocks[$fieldId].body, '(?m)^    validations:\n      required: true$')) {
            Add-Error "Adoption intake field is not fail-closed required: $fieldId"
            $claimTemplateContractPass = $false
        }
    }
    if ($claimTemplateBlocks.ContainsKey('workflow')) {
        $claimWorkflowOptions = [string[]]@([regex]::Matches([string]$claimTemplateBlocks['workflow'].body, '(?m)^        - (?<value>[a-z0-9]+(?:_[a-z0-9]+)*)$') | ForEach-Object { $_.Groups['value'].Value })
        if (($claimWorkflowOptions -join "`n") -cne ($workflowRowIds -join "`n")) {
            Add-Error 'Adoption intake Workflow token options do not exactly match the registered workflows.'
            $claimTemplateContractPass = $false
        }
        if ([regex]::IsMatch([string]$claimTemplateBlocks['workflow'].body, '(?m)^      (?:default|multiple):')) {
            Add-Error 'Adoption intake Workflow token must be an explicit single choice with no default.'
            $claimTemplateContractPass = $false
        }
    }
    $requiredClaimAgreementChecks = if ($claimTemplateBlocks.ContainsKey('agreement')) { @([regex]::Matches([string]$claimTemplateBlocks['agreement'].body, '(?m)^          required: true$')).Count } else { 0 }
    if ($requiredClaimAgreementChecks -ne 2) {
        Add-Error 'Both adoption traceability statements must remain required checkboxes.'
        $claimTemplateContractPass = $false
    }
    $expectedClaimAgreementLabels = [string[]]@(
        'I will preserve predecessors and declare overlap rather than silently overwriting existing work.',
        'I understand that opening this issue does not reserve the scope exclusively.'
    )
    $actualClaimAgreementLabels = if ($claimTemplateBlocks.ContainsKey('agreement')) {
        [string[]]@([regex]::Matches([string]$claimTemplateBlocks['agreement'].body, '(?m)^        - label: (?<value>.+)$') | ForEach-Object { $_.Groups['value'].Value })
    }
    else { [string[]]@() }
    if (($actualClaimAgreementLabels -join "`n") -cne ($expectedClaimAgreementLabels -join "`n")) {
        Add-Error 'Adoption traceability checkbox labels differ from the exact auditor contract.'
        $claimTemplateContractPass = $false
    }
}

$stacksIntakeContractPass = $true
$stacksTemplatePath = '.github/ISSUE_TEMPLATE/stacks.yml'
$stacksTemplateFull = [IO.Path]::GetFullPath((Join-Path $repoRoot $stacksTemplatePath))
$expectedStacksTemplateIds = [string[]]@(
    'board_id', 'intent', 'workflow', 'scope', 'inputs', 'writer', 'upstream_repo',
    'upstream_license', 'upstream_commit', 'overlay_namespace', 'composition',
    'tests', 'sync_cursor', 'mirror', 'agreement'
)
if (-not [IO.File]::Exists($stacksTemplateFull)) {
    Add-Error 'Stacks intake template is missing.'
    $stacksIntakeContractPass = $false
}
else {
    $stacksTemplateBytes = [IO.File]::ReadAllBytes($stacksTemplateFull)
    if ($stacksTemplateBytes.Length -ge 3 -and $stacksTemplateBytes[0] -eq 0xEF -and $stacksTemplateBytes[1] -eq 0xBB -and $stacksTemplateBytes[2] -eq 0xBF) {
        Add-Error 'Stacks intake template contains a UTF-8 BOM.'
        $stacksIntakeContractPass = $false
    }
    $stacksTemplateText = $utf8.GetString($stacksTemplateBytes)
    if ($stacksTemplateText.Contains("`r")) {
        Add-Error 'Stacks intake template must use LF line endings.'
        $stacksIntakeContractPass = $false
    }
    foreach ($mappingError in @(Get-IssueTemplateMappingErrors -Text $stacksTemplateText -Context 'Stacks intake template')) {
        Add-Error $mappingError
        $stacksIntakeContractPass = $false
        $issueTemplateDuplicateKeyContractPass = $false
    }
    $actualStacksTemplateIds = [string[]]@(Get-IssueTemplateIds -Text $stacksTemplateText)
    if (($actualStacksTemplateIds -join "`n") -cne ($expectedStacksTemplateIds -join "`n")) {
        Add-Error 'Stacks intake template field IDs differ from the exact binding contract.'
        $stacksIntakeContractPass = $false
    }
    $expectedStacksTemplateTypes = [ordered]@{
        board_id = 'dropdown'; intent = 'dropdown'; workflow = 'dropdown'; scope = 'textarea'; inputs = 'textarea'
        writer = 'input'; upstream_repo = 'input'; upstream_license = 'input'; upstream_commit = 'input'
        overlay_namespace = 'input'; composition = 'textarea'; tests = 'textarea'; sync_cursor = 'textarea'
        mirror = 'input'; agreement = 'checkboxes'
    }
    $stacksTemplateBlocks = @{}
    $stacksTypeBlocks = @([regex]::Matches($stacksTemplateText, '(?ms)^  - type: (?<type>[a-z]+)\n(?<body>.*?)(?=^  - type: |\z)'))
    foreach ($blockMatch in $stacksTypeBlocks) {
        $blockBody = $blockMatch.Groups['body'].Value
        $idMatch = [regex]::Match($blockBody, '(?m)^    id: (?<id>[a-z][a-z0-9_]*)$')
        if ($idMatch.Success) {
            $stacksTemplateBlocks[$idMatch.Groups['id'].Value] = [pscustomobject]@{
                type = $blockMatch.Groups['type'].Value
                body = $blockBody
            }
        }
    }
    if ($stacksTypeBlocks.Count -ne 16 -or $stacksTemplateBlocks.Count -ne 15) {
        Add-Error 'Stacks intake template must contain one markdown block and exactly fifteen identified field blocks.'
        $stacksIntakeContractPass = $false
    }
    foreach ($fieldId in $expectedStacksTemplateTypes.Keys) {
        if (-not $stacksTemplateBlocks.ContainsKey($fieldId) -or [string]$stacksTemplateBlocks[$fieldId].type -cne [string]$expectedStacksTemplateTypes[$fieldId]) {
            Add-Error "Stacks intake field type differs for: $fieldId"
            $stacksIntakeContractPass = $false
        }
    }
    $expectedStacksTemplateLabels = [ordered]@{
        board_id = 'Board ID'; intent = 'Intent'; workflow = 'Workflow token'; scope = 'Exact scope'; inputs = 'Starting evidence'
        writer = 'Commons writer identity'; upstream_repo = 'Exact upstream repository URL'; upstream_license = 'Applicable upstream license identity'
        upstream_commit = 'Exact upstream commit'; overlay_namespace = 'Commons overlay namespace'; composition = 'Deterministic composition'
        tests = 'Tests and review plan'; sync_cursor = 'Starting synchronization cursor'; mirror = 'Mirror or result URL'; agreement = 'Traceability'
    }
    foreach ($fieldId in $expectedStacksTemplateLabels.Keys) {
        $expectedLabel = [regex]::Escape([string]$expectedStacksTemplateLabels[$fieldId])
        if (-not $stacksTemplateBlocks.ContainsKey($fieldId) -or -not [regex]::IsMatch([string]$stacksTemplateBlocks[$fieldId].body, "(?m)^      label: $expectedLabel`$")) {
            Add-Error "Stacks intake field label differs for: $fieldId"
            $stacksIntakeContractPass = $false
        }
    }
    $requiredStacksFieldIds = [string[]]@(
        'board_id', 'intent', 'workflow', 'scope', 'inputs', 'writer', 'upstream_repo',
        'upstream_license', 'upstream_commit', 'overlay_namespace', 'composition',
        'tests', 'sync_cursor'
    )
    foreach ($fieldId in $requiredStacksFieldIds) {
        if (-not $stacksTemplateBlocks.ContainsKey($fieldId) -or -not [regex]::IsMatch([string]$stacksTemplateBlocks[$fieldId].body, '(?m)^    validations:\n      required: true$')) {
            Add-Error "Stacks intake field is not fail-closed required: $fieldId"
            $stacksIntakeContractPass = $false
        }
    }
    if ($stacksTemplateBlocks.ContainsKey('mirror') -and [regex]::IsMatch([string]$stacksTemplateBlocks['mirror'].body, '(?m)^    validations:\n      required: true$')) {
        Add-Error 'Stacks mirror/result URL must remain optional at intake.'
        $stacksIntakeContractPass = $false
    }
    $requiredAgreementChecks = if ($stacksTemplateBlocks.ContainsKey('agreement')) { @([regex]::Matches([string]$stacksTemplateBlocks['agreement'].body, '(?m)^          required: true$')).Count } else { 0 }
    if ($requiredAgreementChecks -ne 5) {
        Add-Error 'All five Stacks traceability statements must remain required checkboxes.'
        $stacksIntakeContractPass = $false
    }
    $expectedStacksAgreementLabels = [string[]]@(
        'I will write only to the declared Commons-owned namespace and will not edit upstream or another task''s files.',
        'I will preserve exact upstream and predecessor identities, conflicts, failures, corrections, and reversals.',
        'I will not imply upstream acceptance, approval, endorsement, or a motive for prior contribution outcomes.',
        'Any public modified edition will be distinctly titled and will preserve applicable attribution, license, and history notices.',
        'I understand that opening this issue does not reserve the scope exclusively.'
    )
    $actualStacksAgreementLabels = if ($stacksTemplateBlocks.ContainsKey('agreement')) {
        [string[]]@([regex]::Matches([string]$stacksTemplateBlocks['agreement'].body, '(?m)^        - label: (?<value>.+)$') | ForEach-Object { $_.Groups['value'].Value })
    }
    else { [string[]]@() }
    if (($actualStacksAgreementLabels -join "`n") -cne ($expectedStacksAgreementLabels -join "`n")) {
        Add-Error 'Stacks traceability checkbox labels differ from the exact auditor contract.'
        $stacksIntakeContractPass = $false
    }
    if ($stacksTemplateBlocks.ContainsKey('board_id')) {
        $actualStacksBoardOptions = [string[]]@([regex]::Matches([string]$stacksTemplateBlocks['board_id'].body, '(?m)^        - (?<value>[a-z0-9]+(?:-[a-z0-9]+)*)$') | ForEach-Object { $_.Groups['value'].Value })
        if (($actualStacksBoardOptions -join "`n") -cne 'stacks-commons-layer' -or [regex]::IsMatch([string]$stacksTemplateBlocks['board_id'].body, '(?m)^      (?:default|multiple):')) {
            Add-Error 'Stacks Board ID must be a one-option explicit dropdown fixed to stacks-commons-layer.'
            $stacksIntakeContractPass = $false
        }
    }
    if ($stacksTemplateBlocks.ContainsKey('intent')) {
        $expectedStacksIntentOptions = [string[]]@(
            'Bind the first exact upstream pin and Commons overlay',
            'Independently mirror or check an existing Commons overlay',
            'Propose a deterministic composition and test fixture',
            'Return source or license evidence only'
        )
        $actualStacksIntentOptions = [string[]]@([regex]::Matches([string]$stacksTemplateBlocks['intent'].body, '(?m)^        - (?<value>.+)$') | ForEach-Object { $_.Groups['value'].Value })
        if (($actualStacksIntentOptions -join "`n") -cne ($expectedStacksIntentOptions -join "`n") -or [regex]::IsMatch([string]$stacksTemplateBlocks['intent'].body, '(?m)^      (?:default|multiple):')) {
            Add-Error 'Stacks Intent must expose the exact four explicit choices with no default.'
            $stacksIntakeContractPass = $false
        }
    }
    if ($stacksTemplateBlocks.ContainsKey('workflow')) {
        $expectedStacksWorkflowOptions = [string[]]@(($board.items | Where-Object { [string]$_.id -ceq 'stacks-commons-layer' } | Select-Object -First 1).workflow)
        $actualStacksWorkflowOptions = [string[]]@([regex]::Matches([string]$stacksTemplateBlocks['workflow'].body, '(?m)^        - (?<value>[a-z0-9]+(?:_[a-z0-9]+)*)$') | ForEach-Object { $_.Groups['value'].Value })
        if (($actualStacksWorkflowOptions -join "`n") -cne ($expectedStacksWorkflowOptions -join "`n")) {
            Add-Error 'Stacks intake Workflow token options do not exactly match the Stacks board row.'
            $stacksIntakeContractPass = $false
        }
        if ([regex]::IsMatch([string]$stacksTemplateBlocks['workflow'].body, '(?m)^      (?:default|multiple):')) {
            Add-Error 'Stacks intake Workflow token must be an explicit single choice with no default.'
            $stacksIntakeContractPass = $false
        }
    }
    $requiredStacksTemplateTokens = [string[]]@(
        'title: "[Adopt] Stacks Commons layer — "',
        "labels:`n  - adoption",
        '- stacks-commons-layer',
        'Full immutable commit hash; a branch or floating tag is not sufficient.',
        'One lowercase slash-delimited token; each segment starts alphanumeric and does not end in a dot. Use owner/repository for a repository identity, never a URL or an upstream-owned or producer-owned tree.',
        'I will write only to the declared Commons-owned namespace and will not edit upstream or another task''s files.',
        'I will not imply upstream acceptance, approval, endorsement, or a motive for prior contribution outcomes.'
    )
    foreach ($token in $requiredStacksTemplateTokens) {
        if (-not $stacksTemplateText.Contains($token, [StringComparison]::Ordinal)) {
            Add-Error "Stacks intake template is missing required token: $token"
            $stacksIntakeContractPass = $false
        }
    }
}

$handbackTemplateContractPass = $true
$handbackTemplatePath = '.github/ISSUE_TEMPLATE/handback.yml'
$handbackTemplateFull = [IO.Path]::GetFullPath((Join-Path $repoRoot $handbackTemplatePath))
$expectedHandbackTemplateIds = [string[]]@(
    'board_id', 'claim', 'state', 'scope', 'result', 'manifest', 'checks', 'cursor', 'method', 'agreement'
)
if (-not [IO.File]::Exists($handbackTemplateFull)) {
    Add-Error 'Handback template is missing.'
    $handbackTemplateContractPass = $false
}
else {
    $handbackTemplateBytes = [IO.File]::ReadAllBytes($handbackTemplateFull)
    if ($handbackTemplateBytes.Length -ge 3 -and $handbackTemplateBytes[0] -eq 0xEF -and $handbackTemplateBytes[1] -eq 0xBB -and $handbackTemplateBytes[2] -eq 0xBF) {
        Add-Error 'Handback template contains a UTF-8 BOM.'
        $handbackTemplateContractPass = $false
    }
    $handbackTemplateText = $utf8.GetString($handbackTemplateBytes)
    if ($handbackTemplateText.Contains("`r")) {
        Add-Error 'Handback template must use LF line endings.'
        $handbackTemplateContractPass = $false
    }
    foreach ($mappingError in @(Get-IssueTemplateMappingErrors -Text $handbackTemplateText -Context 'Handback template')) {
        Add-Error $mappingError
        $handbackTemplateContractPass = $false
        $issueTemplateDuplicateKeyContractPass = $false
    }
    $actualHandbackTemplateIds = [string[]]@(Get-IssueTemplateIds -Text $handbackTemplateText)
    if (($actualHandbackTemplateIds -join "`n") -cne ($expectedHandbackTemplateIds -join "`n")) {
        Add-Error 'Handback template field IDs differ from the exact binding contract.'
        $handbackTemplateContractPass = $false
    }
    $expectedHandbackTemplateTypes = [ordered]@{
        board_id = 'input'; claim = 'input'; state = 'dropdown'; scope = 'textarea'; result = 'textarea'
        manifest = 'textarea'; checks = 'textarea'; cursor = 'textarea'; method = 'textarea'; agreement = 'checkboxes'
    }
    $handbackTemplateBlocks = @{}
    $handbackTypeBlocks = @([regex]::Matches($handbackTemplateText, '(?ms)^  - type: (?<type>[a-z]+)\n(?<body>.*?)(?=^  - type: |\z)'))
    foreach ($blockMatch in $handbackTypeBlocks) {
        $blockBody = $blockMatch.Groups['body'].Value
        $idMatch = [regex]::Match($blockBody, '(?m)^    id: (?<id>[a-z][a-z0-9_]*)$')
        if ($idMatch.Success) {
            $handbackTemplateBlocks[$idMatch.Groups['id'].Value] = [pscustomobject]@{
                type = $blockMatch.Groups['type'].Value
                body = $blockBody
            }
        }
    }
    if ($handbackTypeBlocks.Count -ne 11 -or $handbackTemplateBlocks.Count -ne 10) {
        Add-Error 'Handback template must contain one markdown block and exactly ten identified field blocks.'
        $handbackTemplateContractPass = $false
    }
    foreach ($fieldId in $expectedHandbackTemplateTypes.Keys) {
        if (-not $handbackTemplateBlocks.ContainsKey($fieldId) -or [string]$handbackTemplateBlocks[$fieldId].type -cne [string]$expectedHandbackTemplateTypes[$fieldId]) {
            Add-Error "Handback field type differs for: $fieldId"
            $handbackTemplateContractPass = $false
        }
    }
    $expectedHandbackTemplateLabels = [ordered]@{
        board_id = 'Board ID'; claim = 'Adoption issue URL'; state = 'Handback state'; scope = 'Exact achieved scope'
        result = 'Inspectable result'; manifest = 'Manifest and identities'; checks = 'Checks, failures, and reversals'
        cursor = 'Continuation cursor'; method = 'Reusable workflow findings'; agreement = 'Preservation and status'
    }
    foreach ($fieldId in $expectedHandbackTemplateLabels.Keys) {
        $expectedLabel = [regex]::Escape([string]$expectedHandbackTemplateLabels[$fieldId])
        if (-not $handbackTemplateBlocks.ContainsKey($fieldId) -or -not [regex]::IsMatch([string]$handbackTemplateBlocks[$fieldId].body, "(?m)^      label: $expectedLabel`$")) {
            Add-Error "Handback field label differs for: $fieldId"
            $handbackTemplateContractPass = $false
        }
    }
    if (-not [regex]::IsMatch($handbackTemplateText, '(?m)^title: "\[Handback\] "$')) {
        Add-Error 'Handback title prefix differs from the exact auditor route.'
        $handbackTemplateContractPass = $false
    }
    foreach ($fieldId in @('board_id', 'claim', 'state', 'scope', 'result', 'manifest', 'checks', 'cursor', 'method')) {
        if (-not $handbackTemplateBlocks.ContainsKey($fieldId) -or -not [regex]::IsMatch([string]$handbackTemplateBlocks[$fieldId].body, '(?m)^    validations:\n      required: true$')) {
            Add-Error "Handback field is not fail-closed required: $fieldId"
            $handbackTemplateContractPass = $false
        }
    }
    $expectedHandbackAgreementLabels = [string[]]@(
        'I preserved the starting generation and did not silently overwrite contradictory or superseded evidence.',
        'I kept quality/review state explicit and made no unsupported completion or certification claim.',
        'I understand that archive maps change only after the returned bytes or exact external identity are inspectable.'
    )
    $actualHandbackAgreementLabels = if ($handbackTemplateBlocks.ContainsKey('agreement')) {
        [string[]]@([regex]::Matches([string]$handbackTemplateBlocks['agreement'].body, '(?m)^        - label: (?<value>.+)$') | ForEach-Object { $_.Groups['value'].Value })
    }
    else { [string[]]@() }
    $requiredHandbackAgreementChecks = if ($handbackTemplateBlocks.ContainsKey('agreement')) { @([regex]::Matches([string]$handbackTemplateBlocks['agreement'].body, '(?m)^          required: true$')).Count } else { 0 }
    if (($actualHandbackAgreementLabels -join "`n") -cne ($expectedHandbackAgreementLabels -join "`n") -or $requiredHandbackAgreementChecks -ne 3) {
        Add-Error 'Handback preservation statements differ from the exact required checkbox contract.'
        $handbackTemplateContractPass = $false
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
    foreach ($token in @(
        '--git', '--issues-file', 'board transport is not declared', 'issue transport is not declared',
        'Workflow token', 'not allowed for Board ID', 'workflow_ids', 'approved_executable_drift_check',
        'stacks_namespace_single_writer', 'STACKS_INTENT_WORKFLOW', 'HANDBACK_PRESERVATION_REQUIRED',
        'approved board repository mismatch', 'does not match the human-approved commit',
        'private_exact_commit_blob', 'drift_detection_not_trust_root'
    )) {
        if (-not $claimAuditorText.Contains($token, [StringComparison]::Ordinal)) {
            Add-Error "claim_auditor is missing required transport token: $token"
            $claimAuditorContractPass = $false
        }
    }
}
else {
    $claimAuditorContractPass = $false
}
$claimExecutionContractPass = $true
$expectedClaimExecutionFields = [string[]]@(
    'ingestion_snapshot_files', 'executable_paths', 'same_commit_required',
    'human_approved_checker_required', 'helper_materialization',
    'local_script_comparison_role', 'offline_git_requirement'
)
Test-ExactFields -Value $board.claim_execution -Expected $expectedClaimExecutionFields -Context 'claim_execution'
$expectedClaimExecutionPaths = [string[]]@('scripts/get-adopt.py', 'scripts/check-claims.py')
$claimExecutionPaths = [string[]]@($board.claim_execution.executable_paths)
if ([int]$board.claim_execution.ingestion_snapshot_files -ne 4) {
    Add-Error 'claim_execution must keep the four-file ingestion snapshot distinct from executable materialization.'
    $claimExecutionContractPass = $false
}
if (($claimExecutionPaths -join "`n") -cne ($expectedClaimExecutionPaths -join "`n")) {
    Add-Error 'claim_execution executable_paths differ from the exact two-blob contract.'
    $claimExecutionContractPass = $false
}
if ($board.claim_execution.same_commit_required -cne $true -or $board.claim_execution.human_approved_checker_required -cne $true) {
    Add-Error 'claim_execution must require one human-approved commit for board and executables.'
    $claimExecutionContractPass = $false
}
if ([string]$board.claim_execution.helper_materialization -cne 'private_exact_commit_blob' -or
    [string]$board.claim_execution.local_script_comparison_role -cne 'drift_detection_not_trust_root' -or
    [string]$board.claim_execution.offline_git_requirement -cne 'fully_materialized_objects_with_lazy_fetch_disabled_or_network_isolation') {
    Add-Error 'claim_execution trust and offline boundaries differ from the exact contract.'
    $claimExecutionContractPass = $false
}
foreach ($path in $claimExecutionPaths) {
    Test-RepoPath -Path $path -Context 'claim_execution.executable_paths' -Required $true
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
    foreach ($token in @(
        'valid_fixture', 'invalid_fixture', 'not-a-board-row', 'new:workflow-contract-fixture',
        'row-incompatible workflow', 'unknown workflow', 'missing workflow',
        'local_git_object_database', 'json_fixture', 'external_network_queried',
        'repository_mismatch_exit', 'checker_mismatch_exit', 'helper_mismatch_exit', 'namespace writer A',
        'mismatched intent', 'malformed link and preservation', 'parent-child namespace',
        'uppercase_checkbox', 'suffixed_checkbox', 'missing_execution_blob_exit',
        'missing_execution_blob_remote_attempt', 'materialized_execution_blobs'
    )) {
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
$coverageClassCounts = [ordered]@{ complete = 0; active = 0; partial = 0; scattered = 0; weak = 0; source_only = 0; unworked = 0 }
$namedOwnerRows = 0
$unclaimedOwnerRows = 0
$weberFrontierContractPass = $false
$steinitz1906FrontierContractPass = $false
$stacksItemContractPass = $false
$genericClaimRouteRows = 0
$stacksClaimRouteRows = 0
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
    foreach ($enumName in @('lane_state', 'coverage_class', 'priority', 'readiness', 'adoption_status')) {
        if (-not ($expectedEnums[$enumName] -ccontains [string]$item.$enumName)) {
            Add-Error "$context has invalid ${enumName}: $($item.$enumName)"
        }
    }
    if ($stateCounts.Contains([string]$item.lane_state)) { $stateCounts[[string]$item.lane_state]++ }
    if ($coverageClassCounts.Contains([string]$item.coverage_class)) { $coverageClassCounts[[string]$item.coverage_class]++ }
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
    $expectedItemClaimUrl = if ($id -ceq 'stacks-commons-layer') { [string]$stacks.intake_form } else { [string]$board.claim_interface }
    if ([string]$item.claim_url -cne $expectedItemClaimUrl) {
        Add-Error "$context claim_url differs from its exact intake route."
    }
    elseif ($id -ceq 'stacks-commons-layer') { $stacksClaimRouteRows++ }
    else { $genericClaimRouteRows++ }

    if ($null -eq $item.owner) { $unclaimedOwnerRows++ } else { $namedOwnerRows++ }

    if ($id -ceq 'weber-algebra') {
        $cursor = [string]$item.next_cursor
        $requiredCursorTokens = [string[]]@(
            'choose the volume and language explicitly',
            'German Volume I',
            'printed p.125',
            'English Volume I',
            'Section 143',
            'Section 176',
            'source p.643'
        )
        $cursorPass = $true
        foreach ($token in $requiredCursorTokens) {
            if (-not $cursor.Contains($token, [StringComparison]::Ordinal)) {
                Add-Error "item:weber-algebra next_cursor is missing required frontier token: $token"
                $cursorPass = $false
            }
        }
        $requiredPrerequisite = 'for Volume II beyond Section 143, locate and immutably bind the separately reported public CURRENT Section-176 German and English bytes'
        if (-not (@($item.prerequisites) -ccontains $requiredPrerequisite)) {
            Add-Error 'item:weber-algebra must require the separately reported public Section-176 bytes before Volume II continuation.'
            $cursorPass = $false
        }
        $sourceBasis = [string]$item.source_basis
        foreach ($token in @('Volume III has no proved cursor', 'known-gaps snapshot', 'Section 176')) {
            if (-not $sourceBasis.Contains($token, [StringComparison]::Ordinal)) {
                Add-Error "item:weber-algebra source_basis is missing required frontier token: $token"
                $cursorPass = $false
            }
        }
        $weberFrontierContractPass = $cursorPass
    }

    if ($id -ceq 'steinitz-1906-euler') {
        $cursor = [string]$item.next_cursor
        $requiredCursorTokens = [string[]]@(
            'bind and bibliographically compare',
            'dedicated-record 1906 German/English packet',
            'mapped Euler-polyhedron note',
            'if identical',
            'do not retranscribe',
            'only if proved distinct'
        )
        $cursorPass = $true
        foreach ($token in $requiredCursorTokens) {
            if (-not $cursor.Contains($token, [StringComparison]::Ordinal)) {
                Add-Error "item:steinitz-1906-euler next_cursor is missing required frontier token: $token"
                $cursorPass = $false
            }
        }
        $requiredPrerequisite = 'locate and bind the dedicated-record 1906 German/English packet'
        if (-not (@($item.prerequisites) -ccontains $requiredPrerequisite)) {
            Add-Error 'item:steinitz-1906-euler must require the public 1906 packet before transcription.'
            $cursorPass = $false
        }
        $sourceBasis = [string]$item.source_basis
        if (-not $sourceBasis.Contains('dedicated-record', [StringComparison]::Ordinal)) {
            Add-Error 'item:steinitz-1906-euler source_basis must name the dedicated-record surface.'
            $cursorPass = $false
        }
        $steinitz1906FrontierContractPass = $cursorPass
    }

    if ($id -ceq 'stacks-commons-layer') {
        $cursor = [string]$item.next_cursor
        $requiredCursorTokens = [string[]]@('coordinate one Commons namespace writer', 'bind the exact upstream repository', 'applicable license', 'commit in a read-only mirror', 'first namespaced overlay manifest')
        $cursorPass = $true
        foreach ($token in $requiredCursorTokens) {
            if (-not $cursor.Contains($token, [StringComparison]::Ordinal)) {
                Add-Error "item:stacks-commons-layer next_cursor is missing required architecture token: $token"
                $cursorPass = $false
            }
        }
        if ([string]$item.coverage_state -cne 'architecture_adopted_no_upstream_pin_or_overlay_bytes') { Add-Error 'item:stacks-commons-layer must not claim implementation bytes.'; $cursorPass = $false }
        if ([string]$item.owner -cne 'Mathematics Commons') { Add-Error 'item:stacks-commons-layer must name Mathematics Commons governance.'; $cursorPass = $false }
        if (-not (@($item.workflow) -ccontains 'upstream_overlay_sync')) { Add-Error 'item:stacks-commons-layer must use upstream_overlay_sync.'; $cursorPass = $false }
        $stacksItemContractPass = $cursorPass
    }

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
foreach ($class in $coverageClassCounts.Keys) {
    if ($coverageClassCounts[$class] -eq 0) { Add-Error "Board has no rows for coverage_class $class." }
}
if (-not $weberFrontierContractPass) {
    Add-Error 'Weber frontier contract did not pass.'
}
if (-not $steinitz1906FrontierContractPass) {
    Add-Error 'Steinitz 1906 frontier contract did not pass.'
}
if (-not $stacksReferenceLayerContractPass -or -not $stacksItemContractPass) {
    Add-Error 'Commons Stacks reference-layer contract did not pass.'
}
if ($stacksClaimRouteRows -ne 1 -or $genericClaimRouteRows -ne (@($board.items).Count - 1)) {
    Add-Error 'Claim routes must contain exactly one dedicated Stacks route and generic routes for every other row.'
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
    schema = 'math-commons-adoption-check-v2'
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
    claim_execution = [ordered]@{
        ingestion_snapshot_files = [int]$board.claim_execution.ingestion_snapshot_files
        executable_paths = @($claimExecutionPaths)
        same_commit_required = [bool]$board.claim_execution.same_commit_required
        human_approved_checker_required = [bool]$board.claim_execution.human_approved_checker_required
        helper_materialization = [string]$board.claim_execution.helper_materialization
        local_script_comparison_role = [string]$board.claim_execution.local_script_comparison_role
        offline_git_requirement = [string]$board.claim_execution.offline_git_requirement
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
        ready_for_adoption_reason = [string]$board.ownership_policy.ready_for_adoption_reason
        future_reason = [string]$board.ownership_policy.future_reason
        absence_inference_forbidden = [bool]$board.ownership_policy.absence_inference_forbidden
    }
    stacks_reference_layer = [ordered]@{
        status = [string]$stacks.status
        human_spec = [string]$stacks.human_spec
        intake_form = [string]$stacks.intake_form
        governance = [string]$stacks.governance
        upstream_repository_binding = [string]$stacks.upstream.repository_binding
        upstream_pin_status = [string]$stacks.upstream.pin_status
        upstream_acceptance_dependency = [bool]$stacks.upstream.acceptance_dependency
        layers = @($stacks.layer_order).Count
        overlay_contents = @($stacks.overlay_contents).Count
        compatibility_targets = @($stacks.compatibility_targets).Count
        public_evidence_prs = @($stacks.public_evidence.pull_requests).Count
        motive_inference = [string]$stacks.public_evidence.motive_inference
        write_boundary = [string]$stacks.write_boundary
    }
    item_certification_default = [string]$board.item_certification_default
    queue_snapshot = @($queueSnapshotRows)
    aggregate = [ordered]@{
        items = @($board.items).Count
        mirrors = @($board.mirrors).Count
        current_work = $stateCounts.current_work
        ready_for_adoption = $stateCounts.ready_for_adoption
        future = $stateCounts.future
        coverage_class_counts = $coverageClassCounts
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
        claim_intake_fields = $expectedClaimTemplateIds.Count
        handback_intake_fields = $expectedHandbackTemplateIds.Count
        consumer_modes = $consumerModes.Count
        claim_auditor_board_modes = $claimBoardModes.Count
        claim_auditor_issue_modes = $claimIssueModes.Count
        claim_execution_blobs = $claimExecutionPaths.Count
        continuous_validation_checks = $ciChecks.Count
        workflow_registry = $workflowRegistryIds.Count
        workflow_tokens_used = $workflowUsedIds.Count
        unreferenced_workflows = $unreferencedWorkflowIds.Count
        named_owner_rows = $namedOwnerRows
        unclaimed_owner_rows = $unclaimedOwnerRows
        items_inheriting_certification_default = @($board.items).Count
        stacks_architecture_layers = @($stacks.layer_order).Count
        stacks_intake_fields = $expectedStacksTemplateIds.Count
        generic_claim_routes = $genericClaimRouteRows
        stacks_claim_routes = $stacksClaimRouteRows
    }
    checks = [ordered]@{
        exact_item_field_contract = -not (@($errors | Where-Object { $_ -like '*field*' }).Count)
        enum_contract = -not (@($errors | Where-Object { $_ -like '*Enum contract*' -or $_ -like '*invalid *' }).Count)
        unique_ids = ($ids.Count -eq @($board.items).Count -and $mirrorIds.Count -eq @($board.mirrors).Count)
        state_partitions_present = ($stateCounts.current_work -gt 0 -and $stateCounts.ready_for_adoption -gt 0 -and $stateCounts.future -gt 0)
        coverage_classes_present = (@($coverageClassCounts.Values | Where-Object { $_ -gt 0 }).Count -eq $coverageClassCounts.Count)
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
        weber_frontier_contract = $weberFrontierContractPass
        steinitz_1906_frontier_contract = $steinitz1906FrontierContractPass
        stacks_reference_layer_contract = ($stacksReferenceLayerContractPass -and $stacksItemContractPass -and $stacksIntakeContractPass)
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
            ($claimIssueModes -join "`n") -ceq ($expectedClaimIssueModes -join "`n") -and
            $claimExecutionContractPass -and
            ($claimExecutionPaths -join "`n") -ceq ($expectedClaimExecutionPaths -join "`n")
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
            [string]$board.handback_interface -ceq $expectedHandbackInterface -and
            $claimTemplateContractPass -and
            $handbackTemplateContractPass -and
            $stacksIntakeContractPass
        )
        issue_label_contract = $issueLabelContractPass
        issue_template_duplicate_key_contract = $issueTemplateDuplicateKeyContractPass
        claim_template_contract = $claimTemplateContractPass
        handback_template_contract = $handbackTemplateContractPass
        claim_route_contract = (
            $stacksClaimRouteRows -eq 1 -and
            $genericClaimRouteRows -eq (@($board.items).Count - 1)
        )
        workflow_registry_contract = (
            $workflowContractPass -and
            $workflowRegistryIds.Count -eq $workflowUsedIds.Count -and
            $workflowRowIds.Count -eq $humanWorkflowIds.Count -and
            $unreferencedWorkflowIds.Count -eq 0
        )
        ownership_semantics = (
            $ownershipContractPass -and
            $namedOwnerRows -eq $stateCounts.current_work -and
            $unclaimedOwnerRows -eq ($stateCounts.ready_for_adoption + $stateCounts.future) -and
            [string]$board.ownership_policy.ready_for_adoption_reason -ceq 'current_project_compute_not_allocated' -and
            [string]$board.ownership_policy.future_reason -ceq 'source_or_cursor_evidence_not_yet_bound' -and
            [bool]$board.ownership_policy.absence_inference_forbidden -eq $true
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
exit 0
