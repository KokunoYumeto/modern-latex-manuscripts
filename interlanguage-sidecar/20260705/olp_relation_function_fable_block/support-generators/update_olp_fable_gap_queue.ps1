$ErrorActionPreference = 'Stop'

$Root = 'C:\Users\memo_\Documents\Codex\2026-07-04\noether-olp-relation-function-support\interlanguage-sidecar\20260705\olp_relation_function_fable_block'
$ResolvedRoot = [System.IO.Path]::GetFullPath($Root)
if (!(Test-Path -LiteralPath $ResolvedRoot)) {
  throw "Missing Fable block root: $ResolvedRoot"
}

function RelPath {
  param([Parameter(Mandatory = $true)][string]$Path)
  return ([System.IO.Path]::GetFullPath($Path).Substring($ResolvedRoot.Length).TrimStart('\') -replace '\\', '/')
}

function Ensure-Dir {
  param([Parameter(Mandatory = $true)][string]$Path)
  if (!(Test-Path -LiteralPath $Path)) {
    New-Item -ItemType Directory -Force -Path $Path | Out-Null
  }
}

function Export-CsvRows {
  param(
    [Parameter(Mandatory = $true)][string]$RelativePath,
    [Parameter(Mandatory = $true)]$Rows
  )
  $Path = Join-Path $ResolvedRoot $RelativePath
  Ensure-Dir ([System.IO.Path]::GetDirectoryName($Path))
  $items = @()
  foreach ($row in $Rows) { $items += $row }
  $items | Export-Csv -LiteralPath $Path -NoTypeInformation -Encoding utf8
}

function Parse-Counts {
  param([string]$CountString)
  $map = @{}
  foreach ($part in ($CountString -split ';')) {
    $trim = $part.Trim()
    if ($trim -match '^([^:]+):(.+)$') {
      $map[$Matches[1].Trim()] = [int]([double]$Matches[2].Trim())
    }
  }
  return $map
}

function Query-Hints {
  param([string]$LexemeId)
  switch ($LexemeId) {
    'rf_relation' { 'relation; relacija; odnos; relacyja; vidnoshennya' }
    'rf_function' { 'function; funkcija; funkcyja; funktsiya' }
    'rf_domain' { 'domain; domen; definiciono mnozestvo; oblast' }
    'rf_codomain' { 'codomain; kodomen; codominio; target set' }
    'rf_image_range' { 'image; range; obraz; slika; opseg' }
    'rf_injective' { 'injective; injektiv; one-to-one; ednoznachno' }
    'rf_surjective' { 'surjective; surjektiv; onto; na' }
    'rf_bijective' { 'bijective; bijektiv; biekcija; one-to-one correspondence' }
    'rf_equivalence_relation' { 'equivalence relation; relacija na ekvivalencija; equivalence class' }
    'rf_partial_order' { 'partial order; parcijalen red; poset' }
    'rf_composition' { 'composition; compose; sostav; sostavuvanje; kompozicija' }
    'rf_inverse' { 'inverse; inverse image; inverzna; obratna; reciprocal' }
    'rf_cardinality' { 'cardinality; kardinal; cardinal number; same size' }
    'rf_linear_map' { 'linear map; linear transformation; homomorphism; linearen operator' }
    default { 'owner-filled query hints required' }
  }
}

function Source-Targets {
  param([string[]]$MissingBranches)
  $targets = New-Object System.Collections.Generic.List[string]
  foreach ($branch in $MissingBranches) {
    switch ($branch) {
      'Slavic_East' { $targets.Add('Slavic East: be/ru/uk source-level relation-function contexts, preferably TeX/HTML/text with formulas') | Out-Null }
      'Slavic_West' { $targets.Add('Slavic West: hsb/pl/cs source-level relation-function contexts, not only general glossary hits') | Out-Null }
      'Slavic_South' { $targets.Add('Slavic South: mk/hr/sr source-level relation-function contexts with formula neighbors') | Out-Null }
      'Germanic' { $targets.Add('Germanic: verify English/German source context if current count is zero') | Out-Null }
      default { $targets.Add("${branch}: source-level witness needed") | Out-Null }
    }
  }
  return ($targets -join ' | ')
}

$activeTarget = @('Germanic', 'Slavic_East', 'Slavic_West', 'Slavic_South')
$branchRows = @(Import-Csv -LiteralPath (Join-Path $ResolvedRoot 'branch_weight_ledger.csv'))
$pretranslationRows = @(Import-Csv -LiteralPath (Join-Path $ResolvedRoot 'pretranslation_scaffolds.csv'))
$formsRows = @(Import-Csv -LiteralPath (Join-Path $ResolvedRoot 'forms.csv'))

$gapRows = New-Object System.Collections.Generic.List[object]
$handoffRows = New-Object System.Collections.Generic.List[object]

foreach ($row in $branchRows) {
  $counts = Parse-Counts $row.raw_witness_counts
  $positive = @($activeTarget | Where-Object { $counts.ContainsKey($_) -and [int]$counts[$_] -gt 0 })
  $missing = @($activeTarget | Where-Object { -not ($counts.ContainsKey($_) -and [int]$counts[$_] -gt 0) })
  $D = [double]$row.effective_branch_number_D
  $activeCount = [int]$row.active_branch_count
  $bucket = if ($activeCount -ge 3 -and $D -ge 2.0) {
    'source-probe-baseline-sufficient-for-scoped-owner-draft'
  } elseif ($activeCount -ge 2) {
    'source-probe-present-but-branch-gap-remains'
  } else {
    'source-acquisition-priority'
  }
  $pt = $pretranslationRows | Where-Object { $_.lexeme_id -eq $row.lexeme_id } | Select-Object -First 1
  $forms = @($formsRows | Where-Object { $_.lexeme_id -eq $row.lexeme_id -and $_.witness_category -like '*source-witness*' -and $_.witness_category -notlike '*generated-draft*' })
  $langs = @($forms | Select-Object -ExpandProperty language -Unique)

  $gapRows.Add([pscustomobject]@{
    lexeme_id = $row.lexeme_id
    coverage_bucket = $bucket
    active_branch_count = $activeCount
    effective_branch_number_D = $row.effective_branch_number_D
    current_positive_branches = ($positive -join '; ')
    missing_active_branches = ($missing -join '; ')
    raw_witness_counts = $row.raw_witness_counts
    query_hints = Query-Hints $row.lexeme_id
    next_source_canon_targets = Source-Targets $missing
    owner_review_use = if ($bucket -like 'source-probe-baseline*') { 'scoped generated-draft review support allowed; still non-canonical' } else { 'use only as gap-aware scaffold until missing branches have source witnesses' }
    claim_boundary = 'no native review; no accepted terminology; no source certification; no translation completion'
  }) | Out-Null

  $handoffRows.Add([pscustomobject]@{
    lexeme_id = $row.lexeme_id
    source_probe_languages = ($langs -join '; ')
    coverage_bucket = $bucket
    generated_interlanguage_control = if ($pt) { $pt.generated_interlanguage_control } else { '' }
    formula_neighboring_usage_note = if ($pt) { $pt.formula_neighboring_usage_note } else { '' }
    macedonian_probe = if ($pt) { $pt.macedonian_probe } else { '' }
    upper_sorbian_probe = if ($pt.PSObject.Properties.Name -contains 'upper_sorbian_probe') { $pt.upper_sorbian_probe } else { '' }
    handoff_action = if ($bucket -like 'source-probe-baseline*') { 'language owner may start bounded draft rendering with source-context notes and caveats' } else { 'language owner should prioritize source-canon acquisition for missing branches before relying on rendering' }
    required_review_before_use = 'source context check; formula-neighboring check; false-friend/adverse-evidence check; native review if available'
    source_use_label = 'generated-draft/non-canonical owner handoff'
  }) | Out-Null
}

Export-CsvRows 'branch_gap_recovery_queue.csv' $gapRows
Export-CsvRows 'owner_source_probe_handoff.csv' $handoffRows

$ready = @($gapRows | Where-Object { $_.coverage_bucket -eq 'source-probe-baseline-sufficient-for-scoped-owner-draft' })
$partial = @($gapRows | Where-Object { $_.coverage_bucket -eq 'source-probe-present-but-branch-gap-remains' })
$priority = @($gapRows | Where-Object { $_.coverage_bucket -eq 'source-acquisition-priority' })

$md = @"
# Relation/Function Owner Handoff

Status: generated-draft / non-canonical support only.

This handoff summarizes branch-weight source-probe coverage for OLP relation/function terms. It is designed for language owners and Session B packaging. It does not claim native review, accepted terminology, source certification, gate promotion, license clearance, approval, final status, or translation completion.

## Coverage Buckets

- Source-probe baseline sufficient for scoped owner draft: $($ready.Count)
- Source-probe present but branch gap remains: $($partial.Count)
- Source-acquisition priority: $($priority.Count)

## Source-Probe Baseline Sufficient For Scoped Owner Draft

$((@($ready | ForEach-Object { "- `$($_.lexeme_id)`: $($_.current_positive_branches); missing $($_.missing_active_branches)" }) -join "`n"))

## Branch Gap Rows

$((@($partial | ForEach-Object { "- `$($_.lexeme_id)`: $($_.current_positive_branches); missing $($_.missing_active_branches); next: $($_.next_source_canon_targets)" }) -join "`n"))

## Source-Acquisition Priority Rows

$((@($priority | ForEach-Object { "- `$($_.lexeme_id)`: $($_.next_source_canon_targets)" }) -join "`n"))

Use `branch_gap_recovery_queue.csv` for source-canon acquisition targets and `owner_source_probe_handoff.csv` for row-level generated-draft handoff. Keep all outputs non-canonical until source-checked and reviewed.
"@
Set-Content -LiteralPath (Join-Path $ResolvedRoot 'generated-draft\relation_function_owner_handoff.md') -Value $md -Encoding utf8

Add-Content -LiteralPath (Join-Path $ResolvedRoot 'SESSION_LOGBOOK_20260705.md') -Value "`nBranch-gap queue addendum: generated branch_gap_recovery_queue.csv, owner_source_probe_handoff.csv, and generated-draft/relation_function_owner_handoff.md from current branch weights. Rows are bucketed as scoped owner draft support, branch-gap support, or source-acquisition priority without promotion claims."

# Rebuild manifest excluding itself and SHA; SHA includes manifest.
$manifestPath = Join-Path $ResolvedRoot 'MANIFEST.csv'
$sumPath = Join-Path $ResolvedRoot 'SHA256SUMS.txt'
$manifestRows = Get-ChildItem -LiteralPath $ResolvedRoot -Recurse -File |
  Where-Object { $_.FullName -notin @($manifestPath, $sumPath) } |
  Sort-Object FullName |
  ForEach-Object {
    $rel = RelPath $_.FullName
    $top = ($rel -split '/')[0]
    $label = switch ($top) {
      'source_bodies' { 'source-witness' }
      'source_witnesses' { 'source-witness' }
      'generated-draft' { 'generated-draft' }
      'support-generators' { 'support-generator' }
      default {
        if ($rel -match 'ledger|languages|source_documents|forms|weights|intelligibility|do_not_use|recovery|probe|candidate|measure|summary|scaffold|route|handoff|queue|audit|contexts|PRETRANSLATION|acknowledgement|ACKNOWLEDGED') { 'audit-ledger' } else { 'methodology' }
      }
    }
    [pscustomobject]@{
      relative_path = $rel
      bytes = $_.Length
      sha256 = (Get-FileHash -Algorithm SHA256 -LiteralPath $_.FullName).Hash.ToLowerInvariant()
      source_use_label = $label
      note = 'Fable OLP relation/function block; no approval or completion claim'
    }
  }
$manifestRows | Export-Csv -LiteralPath $manifestPath -NoTypeInformation -Encoding utf8

$sumLines = Get-ChildItem -LiteralPath $ResolvedRoot -Recurse -File |
  Where-Object { $_.FullName -ne $sumPath } |
  Sort-Object FullName |
  ForEach-Object {
    $rel = RelPath $_.FullName
    $hash = (Get-FileHash -Algorithm SHA256 -LiteralPath $_.FullName).Hash.ToLowerInvariant()
    "$hash  $rel"
  }
Set-Content -LiteralPath $sumPath -Value $sumLines -Encoding ascii

"BRANCH_GAP_ROWS $($gapRows.Count)"
"OWNER_HANDOFF_ROWS $($handoffRows.Count)"
"READY_ROWS $($ready.Count)"
"PARTIAL_ROWS $($partial.Count)"
"PRIORITY_ROWS $($priority.Count)"
"MANIFEST_ROWS $((Import-Csv -LiteralPath $manifestPath | Measure-Object).Count)"
