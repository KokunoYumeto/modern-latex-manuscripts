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

function Decode-Title {
  param([Parameter(Mandatory = $true)][string]$EncodedTitle)
  $title = $EncodedTitle -replace '_', '%20'
  $decoded = [Uri]::UnescapeDataString($title)
  $decoded = $decoded -replace '\s+', ' '
  return $decoded.Trim()
}

function Risk-For {
  param([string]$LexemeId)
  switch ($LexemeId) {
    'rf_codomain' { 'codomain/range ambiguity; verify declared target set vs actual image/range before use' }
    'rf_image_range' { 'image/range false-friend risk; verify actual-value set, not illustration/image sense' }
    'rf_inverse' { 'inverse function vs inverse image vs reciprocal; verify formula-neighboring role' }
    'rf_bijective' { 'bijection may be definitionally linked to inverse/cardinality; verify exact role' }
    'rf_linear_map' { 'linear map/transformation/operator register may vary by source and course level' }
    'rf_domain' { 'domain may mean mathematical domain or broader field; verify function-context usage' }
    default { 'verify source-context, formula-neighboring usage, and register before any rendering use' }
  }
}

$recoveryPath = Join-Path $ResolvedRoot 'external_wikimedia_source_recovery.csv'
if (!(Test-Path -LiteralPath $recoveryPath)) {
  throw 'Run update_olp_fable_external_wikimedia_recovery.ps1 before form extraction.'
}

$recovered = @(Import-Csv -LiteralPath $recoveryPath)
$recoveredById = @{}
foreach ($doc in $recovered) { $recoveredById[$doc.doc_id] = $doc }

$specs = @(
  @{ doc_id='src-ext-wikimedia-pl-function'; lexeme_id='rf_function'; encoded_title='Funkcja' },
  @{ doc_id='src-ext-wikimedia-pl-injective'; lexeme_id='rf_injective'; encoded_title='Funkcja%20r%C3%B3%C5%BCnowarto%C5%9Bciowa' },
  @{ doc_id='src-ext-wikimedia-pl-surjective'; lexeme_id='rf_surjective'; encoded_title='Surjekcja' },
  @{ doc_id='src-ext-wikimedia-pl-bijective'; lexeme_id='rf_bijective'; encoded_title='Funkcja%20wzajemnie%20jednoznaczna' },
  @{ doc_id='src-ext-wikimedia-pl-domain'; lexeme_id='rf_domain'; encoded_title='Dziedzina%20%28matematyka%29' },
  @{ doc_id='src-ext-wikimedia-pl-codomain'; lexeme_id='rf_codomain'; encoded_title='Przeciwdziedzina' },
  @{ doc_id='src-ext-wikimedia-pl-inverse'; lexeme_id='rf_inverse'; encoded_title='Funkcja%20odwrotna' },
  @{ doc_id='src-ext-wikimedia-pl-cardinality'; lexeme_id='rf_cardinality'; encoded_title='Moc%20zbioru' },
  @{ doc_id='src-ext-wikimedia-pl-linear-map'; lexeme_id='rf_linear_map'; encoded_title='Przekszta%C5%82cenie%20liniowe' },
  @{ doc_id='src-ext-wikimedia-pl-image'; lexeme_id='rf_image_range'; encoded_title='Obraz%20%28matematyka%29' },
  @{ doc_id='src-ext-wikimedia-uk-function'; lexeme_id='rf_function'; encoded_title='%D0%A4%D1%83%D0%BD%D0%BA%D1%86%D1%96%D1%8F%20%28%D0%BC%D0%B0%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B0%29' },
  @{ doc_id='src-ext-wikimedia-uk-injective'; lexeme_id='rf_injective'; encoded_title='%D0%86%D0%BD%27%D1%94%D0%BA%D1%86%D1%96%D1%8F_%28%D0%BC%D0%B0%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B0%29' },
  @{ doc_id='src-ext-wikimedia-uk-surjective'; lexeme_id='rf_surjective'; encoded_title='%D0%A1%D1%8E%D1%80%27%D1%94%D0%BA%D1%86%D1%96%D1%8F' },
  @{ doc_id='src-ext-wikimedia-uk-bijective'; lexeme_id='rf_bijective'; encoded_title='%D0%91%D1%96%D1%94%D0%BA%D1%86%D1%96%D1%8F' },
  @{ doc_id='src-ext-wikimedia-uk-domain'; lexeme_id='rf_domain'; encoded_title='%D0%9E%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C%20%D0%B2%D0%B8%D0%B7%D0%BD%D0%B0%D1%87%D0%B5%D0%BD%D0%BD%D1%8F' },
  @{ doc_id='src-ext-wikimedia-uk-inverse'; lexeme_id='rf_inverse'; encoded_title='%D0%9E%D0%B1%D0%B5%D1%80%D0%BD%D0%B5%D0%BD%D0%B0%20%D1%84%D1%83%D0%BD%D0%BA%D1%86%D1%96%D1%8F' },
  @{ doc_id='src-ext-wikimedia-uk-cardinality'; lexeme_id='rf_cardinality'; encoded_title='%D0%9F%D0%BE%D1%82%D1%83%D0%B6%D0%BD%D1%96%D1%81%D1%82%D1%8C%20%D0%BC%D0%BD%D0%BE%D0%B6%D0%B8%D0%BD%D0%B8' },
  @{ doc_id='src-ext-wikimedia-uk-linear-map'; lexeme_id='rf_linear_map'; encoded_title='%D0%9B%D1%96%D0%BD%D1%96%D0%B9%D0%BD%D0%B5%20%D0%B2%D1%96%D0%B4%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%BD%D1%8F' },
  @{ doc_id='src-ext-wikimedia-uk-image-range'; lexeme_id='rf_image_range'; encoded_title='%D0%9E%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C%20%D0%B7%D0%BD%D0%B0%D1%87%D0%B5%D0%BD%D1%8C' }
)

$candidateRows = New-Object System.Collections.Generic.List[object]
$reviewRows = New-Object System.Collections.Generic.List[object]
$blockerRows = New-Object System.Collections.Generic.List[object]

foreach ($spec in $specs) {
  if (-not $recoveredById.ContainsKey($spec.doc_id)) {
    $blockerRows.Add([pscustomobject]@{
      doc_id = $spec.doc_id
      lexeme_id = $spec.lexeme_id
      blocker = 'source body not recovered; cannot create title-source form candidate'
      next_action = 'recover source body or use alternate source'
    }) | Out-Null
    continue
  }
  $doc = $recoveredById[$spec.doc_id]
  $form = Decode-Title $spec.encoded_title
  $normalized = ($form -replace '\s+', ' ').Trim().ToLowerInvariant()
  $candidateRows.Add([pscustomobject]@{
    lexeme_id = $spec.lexeme_id
    language = $doc.language
    branch = $doc.branch
    script = if ($doc.language -eq 'uk') { 'Cyrillic source title' } else { 'Latin source title' }
    source_form = $form
    normalized_form = $normalized
    source_document = $doc.doc_id
    source_location = "$($doc.recovered_path); exact Wikimedia raw page title; external_wikimedia_context_windows.jsonl"
    witness_category = 'source-witness; external-wikimedia-title-source-probe; not native review; not accepted terminology'
  }) | Out-Null
  $reviewRows.Add([pscustomobject]@{
    lexeme_id = $spec.lexeme_id
    language = $doc.language
    branch = $doc.branch
    source_form = $form
    source_document = $doc.doc_id
    review_required = 'language-owner source-context check; formula-neighboring check; false-friend/adverse-evidence check'
    false_friend_or_register_risk = Risk-For $spec.lexeme_id
    current_use_allowed = 'branch-weight/source-probe support only; generated-draft handoff only'
    blocked_claims = 'native review; accepted terminology; canonical approval; source certification; translation completion'
  }) | Out-Null
}

$candidateRows | Export-Csv -LiteralPath (Join-Path $ResolvedRoot 'external_wikimedia_source_form_candidates.csv') -NoTypeInformation -Encoding utf8
$reviewRows | Export-Csv -LiteralPath (Join-Path $ResolvedRoot 'external_wikimedia_false_friend_review_slots.csv') -NoTypeInformation -Encoding utf8
$blockerRows | Export-Csv -LiteralPath (Join-Path $ResolvedRoot 'external_wikimedia_form_candidate_blockers.csv') -NoTypeInformation -Encoding utf8

$formsPath = Join-Path $ResolvedRoot 'forms.csv'
$existingForms = @(Import-Csv -LiteralPath $formsPath) | Where-Object { $_.witness_category -notlike '*external-wikimedia-title-source-probe*' }
($existingForms + $candidateRows) | Export-Csv -LiteralPath $formsPath -NoTypeInformation -Encoding utf8

$summaryRows = @(
  [pscustomobject]@{ field='candidate_form_rows'; value=$candidateRows.Count; note='Exact raw-page-title candidates appended to forms.csv as source probes only' },
  [pscustomobject]@{ field='review_slot_rows'; value=$reviewRows.Count; note='False-friend/register/context review queue' },
  [pscustomobject]@{ field='blocker_rows'; value=$blockerRows.Count; note='Missing source bodies for title-candidate extraction' },
  [pscustomobject]@{ field='claim_boundary'; value='no native review or accepted terminology'; note='Source-probe witness rows only' }
)
$summaryRows | Export-Csv -LiteralPath (Join-Path $ResolvedRoot 'external_wikimedia_form_candidate_summary.csv') -NoTypeInformation -Encoding utf8

Add-Content -LiteralPath (Join-Path $ResolvedRoot 'SESSION_LOGBOOK_20260705.md') -Value "`nExternal Wikimedia form-candidate addendum: generated external_wikimedia_source_form_candidates.csv, external_wikimedia_false_friend_review_slots.csv, external_wikimedia_form_candidate_blockers.csv, and external_wikimedia_form_candidate_summary.csv. Appended exact raw-page-title candidates to forms.csv as source-witness probes only, not native review or accepted terminology."

"EXTERNAL_FORM_CANDIDATES $($candidateRows.Count)"
"EXTERNAL_FORM_REVIEW_SLOTS $($reviewRows.Count)"
"EXTERNAL_FORM_BLOCKERS $($blockerRows.Count)"
