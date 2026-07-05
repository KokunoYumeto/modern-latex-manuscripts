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

function Branch-Key {
  param([string]$Branch)
  if ($Branch -like 'Germanic*') { return 'Germanic' }
  if ($Branch -like 'Slavic/East*') { return 'Slavic_East' }
  if ($Branch -like 'Slavic/West*') { return 'Slavic_West' }
  if ($Branch -like 'Slavic/South*') { return 'Slavic_South' }
  if ($Branch -like 'Romance*') { return 'Romance' }
  if ($Branch -like 'Semitic*') { return 'Semitic' }
  if ($Branch -like 'CJK*') { return 'CJK' }
  if ($Branch -like 'Malayic*') { return 'Malayic' }
  return 'Other'
}

function Format-Counts {
  param([hashtable]$Counts)
  $order = @('Germanic', 'Slavic_East', 'Slavic_West', 'Slavic_South', 'Romance', 'Semitic', 'CJK', 'Malayic', 'Other')
  return (($order | ForEach-Object {
    $key = $_
    $value = 0
    if ($Counts.ContainsKey($key)) { $value = [int]$Counts[$key] }
    "${key}:$value"
  }) -join '; ')
}

function Format-NumberMap {
  param([hashtable]$Counts)
  $order = @('Germanic', 'Slavic_East', 'Slavic_West', 'Slavic_South', 'Romance', 'Semitic', 'CJK', 'Malayic', 'Other')
  return (($order | ForEach-Object {
    $key = $_
    $value = 0.0
    if ($Counts.ContainsKey($key)) { $value = [double]$Counts[$key] }
    "${key}:$([Math]::Round($value, 4))"
  }) -join '; ')
}

function Candidate-For {
  param([string]$LexemeId)
  switch ($LexemeId) {
    'rf_relation' { 'relatio' }
    'rf_function' { 'functio' }
    'rf_domain' { 'dominio' }
    'rf_codomain' { 'codominio' }
    'rf_image_range' { 'imago/rango' }
    'rf_injective' { 'injectiv' }
    'rf_surjective' { 'surjectiv' }
    'rf_bijective' { 'bijectiv' }
    'rf_equivalence_relation' { 'equivalens relatio' }
    'rf_partial_order' { 'ordo partial' }
    'rf_composition' { 'compositio' }
    'rf_inverse' { 'inversa' }
    'rf_cardinality' { 'kardinalitas/equinumeral' }
    'rf_linear_map' { 'mapa linear/homomorfismo' }
    default { 'owner-filled' }
  }
}

$lexemes = Get-Content -LiteralPath (Join-Path $ResolvedRoot 'lexemes.jsonl') |
  Where-Object { $_.Trim() -ne '' } |
  ForEach-Object { $_ | ConvertFrom-Json }
$probeRows = @(Import-Csv -LiteralPath (Join-Path $ResolvedRoot 'term_probe_counts.csv'))
$weakProbePath = Join-Path $ResolvedRoot 'weak_row_probe_counts.csv'
if (Test-Path -LiteralPath $weakProbePath) {
  $probeRows += @(Import-Csv -LiteralPath $weakProbePath)
}
$forms = @(Import-Csv -LiteralPath (Join-Path $ResolvedRoot 'forms.csv'))

$branchOrder = @('Germanic', 'Slavic_East', 'Slavic_West', 'Slavic_South', 'Romance', 'Semitic', 'CJK', 'Malayic', 'Other')
$activeTarget = @('Germanic', 'Slavic_East', 'Slavic_West', 'Slavic_South')
$pi = 1.0 / $activeTarget.Count

$detail = New-Object System.Collections.Generic.List[object]
$branchLedger = New-Object System.Collections.Generic.List[object]
$wordWeights = New-Object System.Collections.Generic.List[object]
$marginalRows = New-Object System.Collections.Generic.List[object]

foreach ($lex in $lexemes) {
  $raw = @{}
  $formSupport = @{}
  foreach ($b in $branchOrder) {
    $raw[$b] = 0
    $formSupport[$b] = 0
  }

  $lexProbeRows = @($probeRows | Where-Object { $_.lexeme_id -eq $lex.lexeme_id })
  foreach ($row in $lexProbeRows) {
    $key = Branch-Key $row.branch
    $raw[$key] = [int]$raw[$key] + [int]$row.hit_count
  }

  $lexForms = @($forms | Where-Object { $_.lexeme_id -eq $lex.lexeme_id -and $_.witness_category -like '*source-witness*' -and $_.witness_category -notlike '*generated-draft*' })
  foreach ($form in $lexForms) {
    $key = Branch-Key $form.branch
    $formSupport[$key] = [int]$formSupport[$key] + 1
    if ([int]$raw[$key] -eq 0) {
      $raw[$key] = [int]$raw[$key] + 1
    }
  }

  $capped = @{}
  $total = 0.0
  foreach ($b in $branchOrder) {
    $value = [Math]::Log(1.0 + [double]$raw[$b])
    $capped[$b] = $value
    if ($activeTarget -contains $b) {
      $total += $value
    }
  }

  $p = @{}
  $entropy = 0.0
  $kl = 0.0
  foreach ($b in $activeTarget) {
    if ($total -gt 0) {
      $p[$b] = [double]$capped[$b] / $total
    } else {
      $p[$b] = 0.0
    }
    if ($p[$b] -gt 0) {
      $entropy += -1.0 * $p[$b] * [Math]::Log($p[$b])
      $kl += $p[$b] * [Math]::Log($p[$b] / $pi)
    }
  }
  $D = if ($total -gt 0) { [Math]::Exp($entropy) } else { 0.0 }
  $nonDominantMass = [double]$capped['Slavic_East'] + [double]$capped['Slavic_West'] + [double]$capped['Slavic_South']
  $nonDominantShare = if ($total -gt 0) { $nonDominantMass / $total } else { 0.0 }
  $germanicShare = if ($total -gt 0) { [double]$capped['Germanic'] / $total } else { 0.0 }
  $activeBranches = @($activeTarget | Where-Object { [double]$capped[$_] -gt 0 }).Count
  $status = if ($activeBranches -ge 3 -and $D -ge 2.0) {
    'source-probe-balanced-enough-for-language-owner-review'
  } elseif ($activeBranches -ge 2) {
    'source-probe-present-but-not-promotable'
  } else {
    'dominant-branch-only-or-gap'
  }

  $rawString = Format-Counts $raw
  $cappedString = Format-NumberMap $capped
  $pString = Format-NumberMap $p
  $candidate = Candidate-For $lex.lexeme_id

  $detail.Add([pscustomobject]@{
    lexeme_id = $lex.lexeme_id
    gloss = $lex.gloss
    candidate_bridge_form = $candidate
    raw_witness_counts = $raw
    capped_log_counts = $capped
    active_target_branches = $activeTarget
    branch_distribution_p = $p
    effective_branch_number_D = [Math]::Round($D, 4)
    kl_skew_from_balanced_target = [Math]::Round($kl, 4)
    non_dominant_share = [Math]::Round($nonDominantShare, 4)
    germanic_share = [Math]::Round($germanicShare, 4)
    status = $status
    caveat = 'term probes are source-body evidence for audit, not native review or accepted terminology'
  }) | Out-Null

  $branchLedger.Add([pscustomobject]@{
    lexeme_id = $lex.lexeme_id
    rooted_tree_scope = 'Indo-European support tree: Germanic + Slavic East/West/South active target branches; other families kept as explicit zero/gap axes'
    raw_witness_counts = $rawString
    capped_log_counts = $cappedString
    equal_splits_or_phylogenetic_downweighting = 'current approximation uses log-capped branch mass from term_probe_counts plus fallback source-witness forms; leaf-level equal-splits unavailable for this OLP slice'
    effective_branch_number_D = [Math]::Round($D, 4)
    kl_skew_from_target = [Math]::Round($kl, 4)
    branch_distribution_p = $pString
    active_branch_count = $activeBranches
    source_basis = 'term_probe_counts.csv + forms.csv source-witness rows; generated-draft rows excluded'
    notes = "$status; no native review, no accepted terminology"
  }) | Out-Null

  $wordWeights.Add([pscustomobject]@{
    lexeme_id = $lex.lexeme_id
    candidate_bridge_form = $candidate
    supporting_forms = $rawString
    adverse_forms = 'see do_not_use.csv and adverse_evidence_ledger.csv; missing Romance/Semitic/CJK/Malayic witnesses remain gaps'
    false_friend_notes = 'not row-reviewed; term-probe contexts require language-owner false-friend check'
    branch_weights = "D=$([Math]::Round($D, 4)); KL=$([Math]::Round($kl, 4)); p={$pString}"
    marginal_intelligibility_score = [Math]::Round($nonDominantShare, 4)
    dominance_penalty = [Math]::Round($germanicShare, 4)
    final_status = $status
  }) | Out-Null

  $marginalRows.Add([pscustomobject]@{
    lexeme_id = $lex.lexeme_id
    candidate_form = $candidate
    dominant_baseline_access = "Germanic share $([Math]::Round($germanicShare, 4))"
    non_dominant_access_gain = "Slavic East/West/South capped share $([Math]::Round($nonDominantShare, 4))"
    loss_or_confusion_cost = 'not measured; formula/register context and false-friend checks still required'
    false_friend_risk = 'unknown until language-owner review; do_not_use guards bind'
    status = $status
  }) | Out-Null
}

$branchLedger | Export-Csv -LiteralPath (Join-Path $ResolvedRoot 'branch_weight_ledger.csv') -NoTypeInformation -Encoding utf8
$wordWeights | Export-Csv -LiteralPath (Join-Path $ResolvedRoot 'word_weights.csv') -NoTypeInformation -Encoding utf8
$marginalRows | Export-Csv -LiteralPath (Join-Path $ResolvedRoot 'marginal_intelligibility.csv') -NoTypeInformation -Encoding utf8
($detail | ConvertTo-Json -Depth 8) | Set-Content -LiteralPath (Join-Path $ResolvedRoot 'weighted_rooted_tree_measure.json') -Encoding utf8

$summaryRows = @(
  [pscustomobject]@{ field='active_target_branches'; value=($activeTarget -join '; '); note='Balanced target used for KL in this OLP support slice' },
  [pscustomobject]@{ field='probe_rows'; value=$probeRows.Count; note='Rows in term_probe_counts.csv' },
  [pscustomobject]@{ field='source_forms'; value=$forms.Count; note='Rows in forms.csv after term-probe update' },
  [pscustomobject]@{ field='promotion_status'; value='none'; note='All rows remain generated-draft/source-probe only' }
)
$summaryRows | Export-Csv -LiteralPath (Join-Path $ResolvedRoot 'weighted_rooted_tree_summary.csv') -NoTypeInformation -Encoding utf8

Add-Content -LiteralPath (Join-Path $ResolvedRoot 'rules_acknowledgement.md') -Value "`n## Numeric Branch-Weight Addendum`n`nUpdated `branch_weight_ledger.csv`, `word_weights.csv`, and `marginal_intelligibility.csv` with numeric log-capped branch mass, effective branch number D, KL skew from a balanced Germanic/East-Slavic/West-Slavic/South-Slavic target, and dominance/non-dominant shares. Added `weighted_rooted_tree_measure.json` and `weighted_rooted_tree_summary.csv`. These are audit/support measures only; no term is promoted."
Add-Content -LiteralPath (Join-Path $ResolvedRoot 'FABLE_REQUIREMENTS_ACKNOWLEDGED_20260705.md') -Value "`n## Numeric Branch-Weight Addendum`n`nThe Fable rooted-tree witness measure is now implemented numerically in `branch_weight_ledger.csv` and `weighted_rooted_tree_measure.json`, using `term_probe_counts.csv` plus source-witness fallback rows from `forms.csv`. Generated-draft rows are excluded from positive witness counts. Results remain source-probe/non-canonical only."
Add-Content -LiteralPath (Join-Path $ResolvedRoot 'SESSION_LOGBOOK_20260705.md') -Value "`nNumeric branch-weight addendum: computed log-capped branch mass, effective branch number D, KL skew, non-dominant share, and dominance penalty for relation/function lexemes; updated branch_weight_ledger.csv, word_weights.csv, marginal_intelligibility.csv, weighted_rooted_tree_measure.json, and weighted_rooted_tree_summary.csv."

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
        if ($rel -match 'ledger|languages|source_documents|forms|weights|intelligibility|do_not_use|recovery|probe|candidate|measure|summary|handoff|queue|audit|contexts|acknowledgement|ACKNOWLEDGED') { 'audit-ledger' } else { 'methodology' }
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

"UPDATED_LEXEMES $($lexemes.Count)"
"MEASURE_ROWS $($detail.Count)"
"MANIFEST_ROWS $((Import-Csv -LiteralPath $manifestPath | Measure-Object).Count)"
"FILES $((Get-ChildItem -LiteralPath $ResolvedRoot -Recurse -File | Measure-Object).Count)"
