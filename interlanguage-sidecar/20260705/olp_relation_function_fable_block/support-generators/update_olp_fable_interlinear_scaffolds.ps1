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

function Export-CsvRows {
  param(
    [Parameter(Mandatory = $true)][string]$RelativePath,
    [Parameter(Mandatory = $true)]$Rows
  )
  $Path = Join-Path $ResolvedRoot $RelativePath
  $Rows | Export-Csv -LiteralPath $Path -NoTypeInformation -Encoding utf8
}

function Get-Candidate {
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
    'rf_linear_map' { 'mapa linear / homomorfismo' }
    default { 'owner-filled' }
  }
}

function Get-FormulaNeighbors {
  param([string]$LexemeId)
  switch ($LexemeId) {
    'rf_relation' { 'R subset A x B; x R y; ordered pairs' }
    'rf_function' { 'f: A -> B; f(x)=y; uniqueness of output' }
    'rf_domain' { 'domain(f); x in A; f: A -> B' }
    'rf_codomain' { 'codomain B in f: A -> B; distinguish from image' }
    'rf_image_range' { 'im(f); f(A); range(f); f^{-1}(S)' }
    'rf_injective' { 'f(x1)=f(x2) => x1=x2' }
    'rf_surjective' { 'forall y in B exists x in A with f(x)=y' }
    'rf_bijective' { 'injective and surjective; inverse exists' }
    'rf_equivalence_relation' { 'reflexive; symmetric; transitive; equivalence classes' }
    'rf_partial_order' { 'reflexive; antisymmetric; transitive; poset' }
    'rf_composition' { 'g o f; g(f(x)); A -> B -> C' }
    'rf_inverse' { 'f^{-1}; inverse image; inverse function when bijective' }
    'rf_cardinality' { '|A|; bijection A -> B; finite/infinite' }
    'rf_linear_map' { 'T(u+v)=T(u)+T(v); T(cu)=cT(u); ker(T); im(T)' }
    default { 'owner-filled formula context' }
  }
}

function Get-Interlinear {
  param([string]$LexemeId)
  switch ($LexemeId) {
    'rf_relation' { 'OBJECT x --RELATION R--> OBJECT y; relation = allowed pair/predicate' }
    'rf_function' { 'INPUT x --FUNCTION f--> UNIQUE OUTPUT f(x)' }
    'rf_domain' { 'DOMAIN A = inputs permitted for f' }
    'rf_codomain' { 'CODOMAIN B = declared target set, not necessarily all attained values' }
    'rf_image_range' { 'IMAGE/RANGE = values actually attained by f on inputs' }
    'rf_injective' { 'INJECTIVE = same output implies same input' }
    'rf_surjective' { 'SURJECTIVE = every target value is hit by some input' }
    'rf_bijective' { 'BIJECTIVE = injective + surjective; reversible pairing' }
    'rf_equivalence_relation' { 'EQUIVALENCE = reflexive + symmetric + transitive relation' }
    'rf_partial_order' { 'PARTIAL ORDER = reflexive + antisymmetric + transitive relation' }
    'rf_composition' { 'COMPOSITION g o f = apply f first, then g' }
    'rf_inverse' { 'INVERSE reverses map/relation direction where defined' }
    'rf_cardinality' { 'CARDINALITY = count/size; same cardinality via bijection' }
    'rf_linear_map' { 'LINEAR MAP preserves addition and scalar multiplication' }
    default { 'owner-filled interlinear scaffold' }
  }
}

function Get-Route {
  param([string]$LexemeId)
  if ($LexemeId -eq 'rf_linear_map') { return 'advanced algebra owner lane; Session D if new construction method arises' }
  if ($LexemeId -in @('rf_cardinality')) { return 'set-theory/relation-function owner lanes' }
  return 'relation/function language owner lanes'
}

$lexemes = Get-Content -LiteralPath (Join-Path $ResolvedRoot 'lexemes.jsonl') |
  Where-Object { $_.Trim() -ne '' } |
  ForEach-Object { $_ | ConvertFrom-Json }
$weights = @(Import-Csv -LiteralPath (Join-Path $ResolvedRoot 'word_weights.csv'))
$branches = @(Import-Csv -LiteralPath (Join-Path $ResolvedRoot 'branch_weight_ledger.csv'))

$pretranslationRows = New-Object System.Collections.Generic.List[object]
$interlinearRows = New-Object System.Collections.Generic.List[object]
$routeRows = New-Object System.Collections.Generic.List[object]

foreach ($lex in $lexemes) {
  $weight = $weights | Where-Object { $_.lexeme_id -eq $lex.lexeme_id } | Select-Object -First 1
  $branch = $branches | Where-Object { $_.lexeme_id -eq $lex.lexeme_id } | Select-Object -First 1
  $candidate = Get-Candidate $lex.lexeme_id
  $formula = Get-FormulaNeighbors $lex.lexeme_id
  $interlinear = Get-Interlinear $lex.lexeme_id
  $route = Get-Route $lex.lexeme_id
  $status = if ($branch) { $branch.notes } else { 'unmeasured; generated-draft only' }

  $pretranslationRows.Add([pscustomobject]@{
    lexeme_id = $lex.lexeme_id
    gloss = $lex.gloss
    source_spine = $lex.source_spine
    formula_neighboring_usage_note = $formula
    generated_interlanguage_control = $candidate
    english_control = $lex.gloss
    spanish_slot = 'owner-filled generated-draft slot; require Spanish lane source witness'
    french_slot = 'owner-filled generated-draft slot; require French lane source witness'
    german_slot = 'owner-filled generated-draft slot; require German lane source witness'
    russian_slot = 'owner-filled generated-draft slot; require Russian lane source witness'
    ukrainian_slot = 'owner-filled generated-draft slot; require Ukrainian lane source witness'
    interslavic_slot = 'owner-filled generated-draft slot; require Fable/Interslavic owner review'
    macedonian_probe = if ($lex.lexeme_id -in @('rf_function','rf_relation','rf_domain','rf_bijective','rf_cardinality','rf_codomain','rf_composition','rf_inverse')) { 'source-probe present in recovered Macedonian lexicon; not approval' } else { 'no explicit Macedonian form probe in this package' }
    upper_sorbian_probe = if ($lex.lexeme_id -eq 'rf_composition') { 'general Kompozicije source probe present; weak topic fit; not approval' } else { 'no explicit Upper Sorbian form probe in this package' }
    branch_metric_status = $status
    source_use_label = 'generated-draft/non-canonical pretranslation scaffold'
    owner_route = $route
  }) | Out-Null

  $interlinearRows.Add([pscustomobject]@{
    lexeme_id = $lex.lexeme_id
    gloss = $lex.gloss
    candidate_bridge_form = $candidate
    interlinear_scaffold = $interlinear
    formula_neighbors = $formula
    branch_D = if ($branch) { $branch.effective_branch_number_D } else { '' }
    marginal_score = if ($weight) { $weight.marginal_intelligibility_score } else { '' }
    dominance_penalty = if ($weight) { $weight.dominance_penalty } else { '' }
    status = 'generated-draft/non-canonical; use for owner review only'
  }) | Out-Null

  $routeRows.Add([pscustomobject]@{
    lexeme_id = $lex.lexeme_id
    route = $route
    needed_next_evidence = 'target-language source witness plus false-friend check plus owner review'
    can_be_used_now = 'pretranslation/interlinear scaffold only'
    blocked_claims = 'native review; accepted terminology; source certification; translation completion'
  }) | Out-Null
}

Export-CsvRows 'pretranslation_scaffolds.csv' $pretranslationRows
Export-CsvRows 'owner_route_queue.csv' $routeRows
$jsonl = foreach ($row in $interlinearRows) { $row | ConvertTo-Json -Compress }
Set-Content -LiteralPath (Join-Path $ResolvedRoot 'interlinear_scaffolds.jsonl') -Value $jsonl -Encoding utf8

$invariants = @(
  [pscustomobject]@{ invariant_id='INV-SCRIPT-001'; scope='script conversion/transliteration'; must_preserve='lexeme identity, formulas, proper names, TeX/math tokens'; allowed_change='script-specific orthography only'; test='round-trip or deterministic transliteration check by language lane'; failure_mode='generated spelling drift treated as term evidence'; status='required before target-lane use' },
  [pscustomobject]@{ invariant_id='INV-FORMULA-001'; scope='formula-neighboring translation'; must_preserve='role of variables, function arrows, quantifiers, inverse/composition order'; allowed_change='local prose order around unchanged formula'; test='compare formula_neighboring_usage_note to target draft'; failure_mode='translation swaps domain/codomain, relation/function, or composition order'; status='required before source-check' },
  [pscustomobject]@{ invariant_id='INV-REGISTER-001'; scope='register shift between proof literacy and advanced algebra'; must_preserve='concept class and mathematical dependency'; allowed_change='teaching gloss vs formal term clearly labeled'; test='owner route queue and source-use label check'; failure_mode='OpenIntro/proof-literacy term promoted as advanced algebra term'; status='required before owner handoff' },
  [pscustomobject]@{ invariant_id='INV-SOURCEUSE-001'; scope='source-use category discipline'; must_preserve='source-witness/generated-draft/audit-ledger boundaries'; allowed_change='additional witnesses may upgrade evidence only when copied and hashed'; test='source_documents.csv and MANIFEST.csv agree'; failure_mode='pointer-only or generated-draft treated as witness'; status='active' },
  [pscustomobject]@{ invariant_id='INV-FABLE-001'; scope='branch-weight witness measure'; must_preserve='positive witness counts exclude generated-draft rows'; allowed_change='new source witnesses can change D/KL after re-run'; test='branch_weight_ledger.csv source_basis column and weighted_rooted_tree_measure.json'; failure_mode='decorative Fable language without data'; status='active' },
  [pscustomobject]@{ invariant_id='INV-CLAIM-001'; scope='public/package claims'; must_preserve='no native review, accepted terminology, license clearance, gate promotion, source certification, final status, or translation completion claims'; allowed_change='none without direct evidence'; test='README/FABLE acknowledgement boundary text'; failure_mode='support scaffold mistaken for completed translation'; status='active' }
)
Export-CsvRows 'invariant_ledger.csv' $invariants

$notes = @'
# Translation / Pretranslation Boundary Notes

This OLP/relation-function support block provides generated-draft pretranslation and interlinear scaffolds only. It does not own final language output for Spanish, French, German, Russian, Ukrainian, Interslavic, Macedonian, Belarusian, Upper Sorbian, or any other target language.

Use `pretranslation_scaffolds.csv` and `interlinear_scaffolds.jsonl` as source-context support for language owners. Use `owner_route_queue.csv` to route rows needing target-language witnesses and false-friend checks.

No row here is native-reviewed, accepted terminology, source-certified, publication-ready, or translation-complete.
'@
Set-Content -LiteralPath (Join-Path $ResolvedRoot 'PRETRANSLATION_BOUNDARY_NOTES.md') -Value $notes -Encoding utf8

Add-Content -LiteralPath (Join-Path $ResolvedRoot 'rules_acknowledgement.md') -Value "`n## Pretranslation / Invariant Addendum`n`nAdded `pretranslation_scaffolds.csv`, `interlinear_scaffolds.jsonl`, `owner_route_queue.csv`, `invariant_ledger.csv`, and `PRETRANSLATION_BOUNDARY_NOTES.md`. These support language owners and enforce G15-style invariants without claiming completed translation."
Add-Content -LiteralPath (Join-Path $ResolvedRoot 'FABLE_REQUIREMENTS_ACKNOWLEDGED_20260705.md') -Value "`n## Pretranslation / Invariant Addendum`n`nThe OLP block now includes generated-draft pretranslation slots, interlinear scaffolds, owner routing, and invariant ledgers. Target-language fields remain owner-filled or source-probe only; no native review, accepted terminology, or completion is claimed."
Add-Content -LiteralPath (Join-Path $ResolvedRoot 'SESSION_LOGBOOK_20260705.md') -Value "`nPretranslation/invariant addendum: generated pretranslation_scaffolds.csv, interlinear_scaffolds.jsonl, owner_route_queue.csv, invariant_ledger.csv, and PRETRANSLATION_BOUNDARY_NOTES.md from existing lexeme/weight/branch ledgers."

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

"PRETRANSLATION_ROWS $($pretranslationRows.Count)"
"INTERLINEAR_ROWS $($interlinearRows.Count)"
"INVARIANT_ROWS $($invariants.Count)"
"MANIFEST_ROWS $((Import-Csv -LiteralPath $manifestPath | Measure-Object).Count)"
"FILES $((Get-ChildItem -LiteralPath $ResolvedRoot -Recurse -File | Measure-Object).Count)"
