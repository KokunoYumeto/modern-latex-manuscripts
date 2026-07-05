$ErrorActionPreference = 'Stop'

$Workspace = 'C:\Users\memo_\Documents\Codex\2026-07-04\noether-olp-relation-function-support'
$PackageRoot = Join-Path $Workspace 'handoff-bodies\olp-relation-function-support-20260705'
$OutRoot = Join-Path $Workspace 'interlanguage-sidecar\20260705\olp_relation_function_fable_block'
$Date = '20260705'
$HeartbeatId = 'noether-mandatory-fable-interlanguage-heartbeat-3'

if (!(Test-Path -LiteralPath $PackageRoot)) {
  throw "Missing OLP package root: $PackageRoot"
}

function Ensure-Dir {
  param([Parameter(Mandatory = $true)][string]$Path)
  if (!(Test-Path -LiteralPath $Path)) {
    New-Item -ItemType Directory -Force -Path $Path | Out-Null
  }
}

function Copy-Body {
  param(
    [Parameter(Mandatory = $true)][string]$Source,
    [Parameter(Mandatory = $true)][string]$DestRelative
  )
  if (!(Test-Path -LiteralPath $Source)) {
    throw "Missing source body for Fable block: $Source"
  }
  $Dest = Join-Path $OutRoot $DestRelative
  Ensure-Dir ([System.IO.Path]::GetDirectoryName($Dest))
  Copy-Item -LiteralPath $Source -Destination $Dest -Force
}

function Write-Utf8 {
  param(
    [Parameter(Mandatory = $true)][string]$RelativePath,
    [Parameter(Mandatory = $true)][string]$Content
  )
  $Path = Join-Path $OutRoot $RelativePath
  Ensure-Dir ([System.IO.Path]::GetDirectoryName($Path))
  Set-Content -LiteralPath $Path -Value $Content -Encoding utf8
}

function Export-CsvRows {
  param(
    [Parameter(Mandatory = $true)][string]$RelativePath,
    [Parameter(Mandatory = $true)]$Rows
  )
  $Path = Join-Path $OutRoot $RelativePath
  Ensure-Dir ([System.IO.Path]::GetDirectoryName($Path))
  $Rows | Export-Csv -LiteralPath $Path -NoTypeInformation -Encoding utf8
}

Ensure-Dir $OutRoot
Ensure-Dir (Join-Path $OutRoot 'source_bodies')
Ensure-Dir (Join-Path $OutRoot 'source_witnesses')

$GoalBlock = @'
The only controlling Noether goal is the full creation of independent interlanguage(s) in accordance with Fable 5 and ChatGPT-Pro findings from the GitHub/Zenodo-uploaded research program, plus complete translation/pre-translation into every relevant interlanguage and dominant language.

Every session must maintain a heartbeat that forces continuous work until done. The heartbeat must require: source-canon search and upload; reading and applying `FABLE_INTERLANGUAGE_PROGRAM_BLOCKING_DIRECTIVE_20260705.md`; reading the Fable/ChatGPT full mirror under `interlanguage-sidecar/20260705/fable_chatgpt_interlingua_program_full/`; applying the GitHub/Zenodo uploaded artifacts including ChatGPT-Pro and Claude/Fable v5 materials; producing pre-translation, terminology, interlinear scaffolding, branch-weight witness ledgers, marginal-intelligibility ledgers, false-friend/adverse-evidence ledgers, source-use ledgers, complete translation artifacts where your lane owns language output, manifests, hashes, and logbooks.

No stopping, no status-only completion, no blocker-only exit. If source canon is missing, search harder and record active recovery work. If you claim completion without complete real output, reject your own claim and keep working. If you remove or ignore the heartbeat, this thread is subject to archival/replacement by the dispatcher where tools permit.

For interlanguage work, implement the Fable formal object: weighted rooted-tree witness measure / branch-weight witness ledger. Produce the required ledgers: `languages.csv`, `source_documents.csv`, `lexemes.jsonl`, `forms.csv`, `word_weights.csv`, `branch_weight_ledger.csv`, `marginal_intelligibility.csv`, `do_not_use.csv`, `rules_acknowledgement.md`, plus `FABLE_REQUIREMENTS_ACKNOWLEDGED_YYYYMMDD.md` naming satisfied/unsatisfied requirements and exact file paths. Do not use Fable terms decoratively; implement them as data.

For translation/pre-translation work, keep going through every assigned paper, appendix, supplement, and post-paper material. Drafts must be labeled `generated-draft` / `non-canonical` until source-checked and reviewed. Do not claim native review, canonical approval, accepted terminology, blanket license clearance, gate promotion, source certification, final status, or translation completion unless actually proven by complete artifacts.

Stay off `main`. Push/stage only for `codex/noether-pc-20260629` or place output for the uploader with manifest/hash/logbook.
'@

$TopHeartbeat = Join-Path $Workspace 'HEARTBEAT_20260705.md'
$TopLogbook = Join-Path $Workspace 'SESSION_LOGBOOK_20260705.md'
$TopHeartbeatContent = "# HEARTBEAT 20260705`n`nHeartbeat id: $HeartbeatId`n`nBEGIN ACTIVE GOAL`n$GoalBlock`nEND ACTIVE GOAL"
$TopLogbookContent = "# SESSION LOGBOOK 20260705`n`nActive goal set with goal tool and mirrored here for durability.`n`nHeartbeat id: $HeartbeatId`n`nBEGIN ACTIVE GOAL`n$GoalBlock`nEND ACTIVE GOAL"
Set-Content -LiteralPath $TopHeartbeat -Value $TopHeartbeatContent -Encoding utf8
Set-Content -LiteralPath $TopLogbook -Value $TopLogbookContent -Encoding utf8

$bodyCopies = @(
  @{ src = Join-Path $PackageRoot 'native-source-bodies\openlogic-olp\sets-functions-relations.tex'; dest = 'source_bodies/openlogic/sets-functions-relations.tex' },
  @{ src = Join-Path $PackageRoot 'native-source-bodies\openlogic-olp\sets-functions-relations-complete.tex'; dest = 'source_bodies/openlogic/sets-functions-relations-complete.tex' },
  @{ src = Join-Path $PackageRoot 'native-source-bodies\dmoi\edition_source_82336dc87d77c3f18d2cdbc8ec1e74eb3ba38799\source_files\sec_structures-sets.ptx'; dest = 'source_bodies/dmoi/sec_structures-sets.ptx' },
  @{ src = Join-Path $PackageRoot 'native-source-bodies\dmoi\edition_source_82336dc87d77c3f18d2cdbc8ec1e74eb3ba38799\source_files\sec_structures-relations.ptx'; dest = 'source_bodies/dmoi/sec_structures-relations.ptx' },
  @{ src = Join-Path $PackageRoot 'native-source-bodies\dmoi\edition_source_82336dc87d77c3f18d2cdbc8ec1e74eb3ba38799\source_files\sec_structures-functions.ptx'; dest = 'source_bodies/dmoi/sec_structures-functions.ptx' },
  @{ src = Join-Path $PackageRoot 'native-source-bodies\openintro\github_ims_index_qmd_at_b88f367a.qmd'; dest = 'source_bodies/openintro/github_ims_index_qmd_at_b88f367a.qmd' },
  @{ src = Join-Path $PackageRoot 'native-source-bodies\aata\project_ptx_at_master.ptx'; dest = 'source_bodies/aata/project_ptx_at_master.ptx' },
  @{ src = Join-Path $PackageRoot 'source-witnesses\openlogic-olp\LICENSE.md'; dest = 'source_witnesses/openlogic/LICENSE.md' },
  @{ src = Join-Path $PackageRoot 'source-witnesses\dmoi\github_LICENSE_at_main.txt'; dest = 'source_witnesses/dmoi/github_LICENSE_at_main.txt' },
  @{ src = Join-Path $PackageRoot 'source-witnesses\openintro\openintro_license_page.html'; dest = 'source_witnesses/openintro/openintro_license_page.html' },
  @{ src = Join-Path $PackageRoot 'source-witnesses\aata\COPYING_at_master.txt'; dest = 'source_witnesses/aata/COPYING_at_master.txt' }
)

foreach ($copy in $bodyCopies) {
  Copy-Body $copy.src $copy.dest
}

$languages = @(
  [pscustomobject]@{ language_code='en'; name='English'; family='Indo-European'; branch='Germanic/West Germanic'; script='Latin'; region='global academic'; source_count=7; tex_count=2; pdf_count=0; native_source_status='source-witness present for English control/source bodies; not target-language approval' },
  [pscustomobject]@{ language_code='x-math-symbolic'; name='mathematical symbolic register'; family='non-family axis'; branch='X/symbolic'; script='symbols/Latin'; region='mathematical notation'; source_count=5; tex_count=0; pdf_count=0; native_source_status='formula-neighbor witness axis, not a language community' },
  [pscustomobject]@{ language_code='x-il-draft'; name='generated interlanguage draft scaffold'; family='constructed/noncanonical'; branch='generated-draft'; script='Latin'; region='support lane'; source_count=0; tex_count=0; pdf_count=0; native_source_status='generated-draft only; not native witness' },
  [pscustomobject]@{ language_code='ru'; name='Russian'; family='Indo-European'; branch='Slavic/East'; script='Cyrillic'; region='East Slavic'; source_count=0; tex_count=0; pdf_count=0; native_source_status='source-acquisition gap in this OLP block' },
  [pscustomobject]@{ language_code='uk'; name='Ukrainian'; family='Indo-European'; branch='Slavic/East'; script='Cyrillic'; region='East Slavic'; source_count=0; tex_count=0; pdf_count=0; native_source_status='source-acquisition gap in this OLP block' },
  [pscustomobject]@{ language_code='pl'; name='Polish'; family='Indo-European'; branch='Slavic/West'; script='Latin'; region='West Slavic'; source_count=0; tex_count=0; pdf_count=0; native_source_status='source-acquisition gap in this OLP block' },
  [pscustomobject]@{ language_code='cs'; name='Czech'; family='Indo-European'; branch='Slavic/West'; script='Latin'; region='West Slavic'; source_count=0; tex_count=0; pdf_count=0; native_source_status='source-acquisition gap in this OLP block' },
  [pscustomobject]@{ language_code='hr'; name='Croatian'; family='Indo-European'; branch='Slavic/South'; script='Latin'; region='South Slavic'; source_count=0; tex_count=0; pdf_count=0; native_source_status='source-acquisition gap in this OLP block' },
  [pscustomobject]@{ language_code='sr'; name='Serbian'; family='Indo-European'; branch='Slavic/South'; script='Cyrillic/Latin'; region='South Slavic'; source_count=0; tex_count=0; pdf_count=0; native_source_status='source-acquisition gap in this OLP block' },
  [pscustomobject]@{ language_code='es'; name='Spanish'; family='Indo-European'; branch='Romance/Ibero-Romance'; script='Latin'; region='Romance baseline'; source_count=0; tex_count=0; pdf_count=0; native_source_status='source-acquisition gap in this OLP block' },
  [pscustomobject]@{ language_code='fr'; name='French'; family='Indo-European'; branch='Romance/Gallo-Romance'; script='Latin'; region='Romance baseline'; source_count=0; tex_count=0; pdf_count=0; native_source_status='source-acquisition gap in this OLP block' },
  [pscustomobject]@{ language_code='de'; name='German'; family='Indo-European'; branch='Germanic/West Germanic'; script='Latin'; region='Germanic baseline'; source_count=0; tex_count=0; pdf_count=0; native_source_status='source-acquisition gap in this OLP block' }
)
Export-CsvRows 'languages.csv' $languages

$sourceDocs = @(
  [pscustomobject]@{ doc_id='src-openlogic-sfr'; path='source_bodies/openlogic/sets-functions-relations.tex'; language='en'; branch='Germanic/West Germanic'; file_type='tex'; provenance_url_or_path='packaged from handoff-bodies/olp-relation-function-support-20260705/native-source-bodies/openlogic-olp/sets-functions-relations.tex'; sha256=''; license_or_availability_note='OpenLogic license signal copied in source_witnesses/openlogic/LICENSE.md; no license-clearance claim'; witness_category='source-witness' },
  [pscustomobject]@{ doc_id='src-openlogic-sfr-complete'; path='source_bodies/openlogic/sets-functions-relations-complete.tex'; language='en'; branch='Germanic/West Germanic'; file_type='tex'; provenance_url_or_path='packaged from OLP source-body package'; sha256=''; license_or_availability_note='OpenLogic license signal copied; no license-clearance claim'; witness_category='source-witness' },
  [pscustomobject]@{ doc_id='src-dmoi-sets'; path='source_bodies/dmoi/sec_structures-sets.ptx'; language='en'; branch='Germanic/West Germanic'; file_type='ptx'; provenance_url_or_path='packaged from DMOI edition source cache'; sha256=''; license_or_availability_note='DMOI license signal copied; no license-clearance claim'; witness_category='source-witness' },
  [pscustomobject]@{ doc_id='src-dmoi-relations'; path='source_bodies/dmoi/sec_structures-relations.ptx'; language='en'; branch='Germanic/West Germanic'; file_type='ptx'; provenance_url_or_path='packaged from DMOI edition source cache'; sha256=''; license_or_availability_note='DMOI license signal copied; no license-clearance claim'; witness_category='source-witness' },
  [pscustomobject]@{ doc_id='src-dmoi-functions'; path='source_bodies/dmoi/sec_structures-functions.ptx'; language='en'; branch='Germanic/West Germanic'; file_type='ptx'; provenance_url_or_path='packaged from DMOI edition source cache'; sha256=''; license_or_availability_note='DMOI license signal copied; no license-clearance claim'; witness_category='source-witness' },
  [pscustomobject]@{ doc_id='src-openintro-ims'; path='source_bodies/openintro/github_ims_index_qmd_at_b88f367a.qmd'; language='en'; branch='Germanic/West Germanic'; file_type='qmd'; provenance_url_or_path='packaged from OpenIntro IMS source witness cache'; sha256=''; license_or_availability_note='OpenIntro license page copied; no license-clearance claim'; witness_category='source-witness' },
  [pscustomobject]@{ doc_id='src-aata-project'; path='source_bodies/aata/project_ptx_at_master.ptx'; language='en'; branch='Germanic/West Germanic'; file_type='ptx'; provenance_url_or_path='packaged from AATA source witness cache'; sha256=''; license_or_availability_note='GFDL signal copied in source_witnesses/aata/COPYING_at_master.txt; no license-clearance claim'; witness_category='source-witness' },
  [pscustomobject]@{ doc_id='draft-olp-il-scaffold'; path='generated-draft/NONCANONICAL_INTERLANGUAGE_RELATION_FUNCTION_SCAFFOLDS.csv'; language='x-il-draft'; branch='generated-draft'; file_type='csv'; provenance_url_or_path='handoff-bodies generated-draft scaffold, copied as derived support by this package'; sha256=''; license_or_availability_note='project-generated draft; not source witness'; witness_category='generated-draft' }
)

$scaffoldSource = Join-Path $PackageRoot 'generated-draft\NONCANONICAL_INTERLANGUAGE_RELATION_FUNCTION_SCAFFOLDS.csv'
Copy-Body $scaffoldSource 'generated-draft/NONCANONICAL_INTERLANGUAGE_RELATION_FUNCTION_SCAFFOLDS.csv'
foreach ($doc in $sourceDocs) {
  $docPath = Join-Path $OutRoot ($doc.path -replace '/', '\')
  $doc.sha256 = (Get-FileHash -Algorithm SHA256 -LiteralPath $docPath).Hash.ToLowerInvariant()
}
Export-CsvRows 'source_documents.csv' $sourceDocs

$lexemes = @(
  @{ lexeme_id='rf_relation'; gloss='relation as subset/predicate between objects'; domain='relation-function'; source_spine='OpenLogic sets-functions-relations; DMOI relations'; target_bridge_lane='OLP relation/function generated-draft support' },
  @{ lexeme_id='rf_function'; gloss='function as unique-output map'; domain='relation-function'; source_spine='OpenLogic sets-functions-relations; DMOI functions'; target_bridge_lane='OLP relation/function generated-draft support' },
  @{ lexeme_id='rf_domain'; gloss='domain/input set of a function'; domain='relation-function'; source_spine='OpenLogic and DMOI functions'; target_bridge_lane='OLP relation/function generated-draft support' },
  @{ lexeme_id='rf_codomain'; gloss='declared target set/codomain'; domain='relation-function'; source_spine='OpenLogic and DMOI functions'; target_bridge_lane='OLP relation/function generated-draft support' },
  @{ lexeme_id='rf_image_range'; gloss='image/range as attained values'; domain='relation-function'; source_spine='OpenLogic and DMOI functions'; target_bridge_lane='OLP relation/function generated-draft support' },
  @{ lexeme_id='rf_injective'; gloss='injective/one-to-one property'; domain='relation-function'; source_spine='OpenLogic and DMOI functions'; target_bridge_lane='OLP relation/function generated-draft support' },
  @{ lexeme_id='rf_surjective'; gloss='surjective/onto property'; domain='relation-function'; source_spine='OpenLogic and DMOI functions'; target_bridge_lane='OLP relation/function generated-draft support' },
  @{ lexeme_id='rf_bijective'; gloss='bijective property'; domain='relation-function'; source_spine='OpenLogic and DMOI functions'; target_bridge_lane='OLP relation/function generated-draft support' },
  @{ lexeme_id='rf_equivalence_relation'; gloss='equivalence relation from reflexive/symmetric/transitive'; domain='relation-function'; source_spine='OpenLogic and DMOI relations'; target_bridge_lane='OLP relation/function generated-draft support' },
  @{ lexeme_id='rf_partial_order'; gloss='partial order from reflexive/antisymmetric/transitive'; domain='relation-function'; source_spine='OpenLogic and DMOI relations'; target_bridge_lane='OLP relation/function generated-draft support' },
  @{ lexeme_id='rf_composition'; gloss='function composition'; domain='relation-function'; source_spine='OpenLogic and DMOI functions'; target_bridge_lane='OLP relation/function generated-draft support' },
  @{ lexeme_id='rf_inverse'; gloss='inverse function/relation notation'; domain='relation-function'; source_spine='OpenLogic and DMOI functions'; target_bridge_lane='OLP relation/function generated-draft support' },
  @{ lexeme_id='rf_cardinality'; gloss='finite/infinite/equinumerosity/cardinality'; domain='sets-functions'; source_spine='OpenLogic sets-functions-relations; DMOI sets'; target_bridge_lane='OLP relation/function generated-draft support' },
  @{ lexeme_id='rf_linear_map'; gloss='linear map/homomorphism bridge extension'; domain='abstract-algebra-extension'; source_spine='AATA/FCLA witness plus OLP support'; target_bridge_lane='advanced algebra owner route' }
)
$jsonl = foreach ($lex in $lexemes) { $lex | ConvertTo-Json -Compress }
Write-Utf8 'lexemes.jsonl' ($jsonl -join "`n")

$forms = @(
  [pscustomobject]@{ lexeme_id='rf_relation'; language='en'; branch='Germanic'; script='Latin'; source_form='relation'; normalized_form='relation'; source_document='src-openlogic-sfr; src-dmoi-relations'; source_location='sets/functions/relations sections'; witness_category='source-witness' },
  [pscustomobject]@{ lexeme_id='rf_relation'; language='x-il-draft'; branch='generated-draft'; script='Latin'; source_form='relatio'; normalized_form='relatio'; source_document='draft-olp-il-scaffold'; source_location='K-IL-003'; witness_category='generated-draft' },
  [pscustomobject]@{ lexeme_id='rf_function'; language='en'; branch='Germanic'; script='Latin'; source_form='function'; normalized_form='function'; source_document='src-openlogic-sfr; src-dmoi-functions'; source_location='function sections'; witness_category='source-witness' },
  [pscustomobject]@{ lexeme_id='rf_function'; language='x-il-draft'; branch='generated-draft'; script='Latin'; source_form='functio'; normalized_form='functio'; source_document='draft-olp-il-scaffold'; source_location='K-IL-003'; witness_category='generated-draft' },
  [pscustomobject]@{ lexeme_id='rf_domain'; language='en'; branch='Germanic'; script='Latin'; source_form='domain'; normalized_form='domain'; source_document='src-openlogic-sfr-complete; src-dmoi-functions'; source_location='domain/codomain rows'; witness_category='source-witness' },
  [pscustomobject]@{ lexeme_id='rf_domain'; language='x-il-draft'; branch='generated-draft'; script='Latin'; source_form='dominio'; normalized_form='dominio'; source_document='draft-olp-il-scaffold'; source_location='K-IL-004'; witness_category='generated-draft' },
  [pscustomobject]@{ lexeme_id='rf_codomain'; language='en'; branch='Germanic'; script='Latin'; source_form='codomain'; normalized_form='codomain'; source_document='src-openlogic-sfr-complete; src-dmoi-functions'; source_location='domain/codomain rows'; witness_category='source-witness' },
  [pscustomobject]@{ lexeme_id='rf_codomain'; language='x-il-draft'; branch='generated-draft'; script='Latin'; source_form='codominio'; normalized_form='codominio'; source_document='draft-olp-il-scaffold'; source_location='K-IL-004'; witness_category='generated-draft' },
  [pscustomobject]@{ lexeme_id='rf_image_range'; language='en'; branch='Germanic'; script='Latin'; source_form='image/range'; normalized_form='image range'; source_document='src-openlogic-sfr-complete; src-dmoi-functions'; source_location='image/range rows'; witness_category='source-witness' },
  [pscustomobject]@{ lexeme_id='rf_image_range'; language='x-il-draft'; branch='generated-draft'; script='Latin'; source_form='imago/rango'; normalized_form='imago rango'; source_document='draft-olp-il-scaffold'; source_location='K-IL-004'; witness_category='generated-draft' },
  [pscustomobject]@{ lexeme_id='rf_injective'; language='en'; branch='Germanic'; script='Latin'; source_form='injective/one-to-one'; normalized_form='injective one-to-one'; source_document='src-openlogic-sfr; src-dmoi-functions'; source_location='property rows'; witness_category='source-witness' },
  [pscustomobject]@{ lexeme_id='rf_surjective'; language='en'; branch='Germanic'; script='Latin'; source_form='surjective/onto'; normalized_form='surjective onto'; source_document='src-openlogic-sfr; src-dmoi-functions'; source_location='property rows'; witness_category='source-witness' },
  [pscustomobject]@{ lexeme_id='rf_bijective'; language='en'; branch='Germanic'; script='Latin'; source_form='bijective/bijection'; normalized_form='bijective bijection'; source_document='src-openlogic-sfr; src-dmoi-functions'; source_location='property rows'; witness_category='source-witness' },
  [pscustomobject]@{ lexeme_id='rf_equivalence_relation'; language='en'; branch='Germanic'; script='Latin'; source_form='equivalence relation'; normalized_form='equivalence relation'; source_document='src-openlogic-sfr; src-dmoi-relations'; source_location='relation property rows'; witness_category='source-witness' },
  [pscustomobject]@{ lexeme_id='rf_partial_order'; language='en'; branch='Germanic'; script='Latin'; source_form='partial order'; normalized_form='partial order'; source_document='src-openlogic-sfr; src-dmoi-relations'; source_location='relation property rows'; witness_category='source-witness' },
  [pscustomobject]@{ lexeme_id='rf_composition'; language='en'; branch='Germanic'; script='Latin'; source_form='composition'; normalized_form='composition'; source_document='src-openlogic-sfr; src-dmoi-functions'; source_location='composition rows'; witness_category='source-witness' },
  [pscustomobject]@{ lexeme_id='rf_inverse'; language='en'; branch='Germanic'; script='Latin'; source_form='inverse'; normalized_form='inverse'; source_document='src-openlogic-sfr; src-dmoi-functions'; source_location='inverse rows'; witness_category='source-witness' },
  [pscustomobject]@{ lexeme_id='rf_cardinality'; language='en'; branch='Germanic'; script='Latin'; source_form='cardinality/same size/bijection'; normalized_form='cardinality same size bijection'; source_document='src-openlogic-sfr-complete; src-dmoi-sets'; source_location='sets/cardinality rows'; witness_category='source-witness' },
  [pscustomobject]@{ lexeme_id='rf_linear_map'; language='en'; branch='Germanic'; script='Latin'; source_form='linear map/homomorphism'; normalized_form='linear map homomorphism'; source_document='src-aata-project'; source_location='project source witness'; witness_category='source-witness' }
)
Export-CsvRows 'forms.csv' $forms

$weightRows = @()
foreach ($lex in $lexemes) {
  $candidate = switch ($lex.lexeme_id) {
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
  $weightRows += [pscustomobject]@{
    lexeme_id = $lex.lexeme_id
    candidate_bridge_form = $candidate
    supporting_forms = 'English source witness plus formula-neighbor scaffold; generated interlanguage draft is not positive native evidence'
    adverse_forms = 'none row-verified in this lane; non-English branch source witnesses are missing'
    false_friend_notes = 'unscored; must be checked by language owners before promotion'
    branch_weights = 'Germanic/en=1.0 source-witness; X-symbolic=0.25 support axis; Slavic/Romance/Semitic/CJK/Malayic=0 source gap'
    marginal_intelligibility_score = 'exploratory_uncomputed'
    dominance_penalty = 'high: English/Germanic source concentration; generated candidate not promotable'
    final_status = 'generated-draft/non-canonical; source-acquisition required'
  }
}
Export-CsvRows 'word_weights.csv' $weightRows

$branchRows = foreach ($lex in $lexemes) {
  [pscustomobject]@{
    lexeme_id = $lex.lexeme_id
    rooted_tree_scope = 'Indo-European depth-1 plus non-family X/generated axes'
    raw_witness_counts = 'Germanic:1; Romance:0; Slavic_East:0; Slavic_West:0; Slavic_South:0; Semitic:0; CJK:0; Malayic:0; X_symbolic:partial'
    capped_log_counts = 'Germanic:1; all other linguistic branches:0'
    equal_splits_or_phylogenetic_downweighting = 'English leaf gets Germanic mass 1.0; no sibling/non-dominant branch witnesses in this OLP block'
    effective_branch_number_D = '1.00 linguistic branches; below promotion threshold'
    kl_skew_from_target = 'high_skew_from_balanced_target'
    notes = 'This ledger implements Fable object for this support lane and records the source-canon gap rather than hiding it.'
  }
}
Export-CsvRows 'branch_weight_ledger.csv' $branchRows

$margRows = foreach ($lex in $lexemes) {
  [pscustomobject]@{
    lexeme_id = $lex.lexeme_id
    candidate_form = ($weightRows | Where-Object { $_.lexeme_id -eq $lex.lexeme_id }).candidate_bridge_form
    dominant_baseline_access = 'English/Germanic source control only'
    non_dominant_access_gain = 'not established; no non-English native witnesses packaged in this Fable block'
    loss_or_confusion_cost = 'possible international opacity and branch mismatch; owner review required'
    false_friend_risk = 'unknown; adverse-evidence ledger blocks promotion'
    status = 'review_or_reject_for_promotion; keep as generated-draft scaffold only'
  }
}
Export-CsvRows 'marginal_intelligibility.csv' $margRows

$doNotUse = @(
  [pscustomobject]@{ id='OLP-DNU-001'; candidate='English source form as bridge proof'; relation='draft_as_witness_error'; blocked_scope='all relation/function terms'; action='do_not_count_English_control_as_target_language_witness' },
  [pscustomobject]@{ id='OLP-DNU-002'; candidate='relatio/functio/domino-style draft forms'; relation='authority_needed'; blocked_scope='public or accepted terminology'; action='keep_generated_draft_until branch witnesses and review exist' },
  [pscustomobject]@{ id='OLP-DNU-003'; candidate='domain/codomain/range collapse'; relation='semantic_collision'; blocked_scope='function terminology'; action='keep declared target and attained values separate' },
  [pscustomobject]@{ id='OLP-DNU-004'; candidate='relation/function merge'; relation='semantic_collision'; blocked_scope='relation-function boundary'; action='keep relation as general predicate/subset and function as unique-output map' },
  [pscustomobject]@{ id='OLP-DNU-005'; candidate='source-pointer-only canon'; relation='source_channel_error'; blocked_scope='all ledgers'; action='attach actual bodies or mark source-acquisition gap' },
  [pscustomobject]@{ id='OLP-DNU-006'; candidate='dominant-language softened form'; relation='dominance_risk'; blocked_scope='interlanguage candidates'; action='require branch-weight and marginal-intelligibility check before promotion' }
)
Export-CsvRows 'do_not_use.csv' $doNotUse

$adverse = @(
  [pscustomobject]@{ evidence_id='ADV-OLP-001'; lexeme_id='all'; evidence_type='missing_non_dominant_witness'; source='languages.csv/source_documents.csv'; effect='branch_weight_D remains 1.00; no promotion' },
  [pscustomobject]@{ evidence_id='ADV-OLP-002'; lexeme_id='rf_image_range'; evidence_type='register_instability'; source='OLP/DMOI source context'; effect='range/image convention must be owner-checked' },
  [pscustomobject]@{ evidence_id='ADV-OLP-003'; lexeme_id='rf_domain;rf_codomain'; evidence_type='semantic_collision'; source='function context'; effect='do not merge domain/codomain/range in target scaffold' },
  [pscustomobject]@{ evidence_id='ADV-OLP-004'; lexeme_id='rf_relation;rf_function'; evidence_type='semantic_collision'; source='relation/function source sections'; effect='do not translate relation and function as interchangeable map words' },
  [pscustomobject]@{ evidence_id='ADV-OLP-005'; lexeme_id='rf_linear_map'; evidence_type='owner_route'; source='AATA/FCLA support witness only'; effect='route advanced algebra register to owner lane' }
)
Export-CsvRows 'adverse_evidence_ledger.csv' $adverse

$sourceUse = @(
  [pscustomobject]@{ category='source-witness'; files='source_bodies/openlogic/*; source_bodies/dmoi/*; source_bodies/openintro/*; source_bodies/aata/*'; allowed_use='source-context anchors and English control terminology'; prohibited_use='native target-language approval or accepted bridge terms' },
  [pscustomobject]@{ category='generated-draft'; files='generated-draft/NONCANONICAL_INTERLANGUAGE_RELATION_FUNCTION_SCAFFOLDS.csv'; allowed_use='pre-translation scaffold for language owners'; prohibited_use='witness status or promotion argument' },
  [pscustomobject]@{ category='audit-ledger'; files='languages.csv; source_documents.csv; branch_weight_ledger.csv; marginal_intelligibility.csv; do_not_use.csv; adverse_evidence_ledger.csv'; allowed_use='Fable data implementation and blocker tracking'; prohibited_use='completion or approval claim' },
  [pscustomobject]@{ category='methodology'; files='rules_acknowledgement.md; FABLE_REQUIREMENTS_ACKNOWLEDGED_20260705.md'; allowed_use='requirement traceability'; prohibited_use='substitute for source bodies' }
)
Export-CsvRows 'source_use_ledger.csv' $sourceUse

$rules = @'
# Rules Acknowledgement

Date: 2026-07-05
Lane: OLP/OpenTranslation/relation-function support
Status: generated-draft/non-canonical support package with actual source bodies and Fable ledgers.

## Done With Paths

- Read blocking directive: `FABLE_INTERLANGUAGE_PROGRAM_BLOCKING_DIRECTIVE_20260705.md` from `origin/codex/noether-pc-20260629`.
- Read mirror index and key method files: `interlanguage-sidecar/20260705/fable_chatgpt_interlingua_program_full/README.md`, mirror manifest, `BRANCH_WEIGHTING_SPEC.md`, `SOURCE_USE_POLICY.md`, `HEURISTIC_REGISTER.md`, `CHATGPT_PRO_TASK_SPEC_20260704.md`, `DO_NOT_USE_LEDGER_20260704.md`, and `INTERSLAVIC_GATE_MAP.md`.
- Implemented required ledgers in this package: `languages.csv`, `source_documents.csv`, `lexemes.jsonl`, `forms.csv`, `word_weights.csv`, `branch_weight_ledger.csv`, `marginal_intelligibility.csv`, `do_not_use.csv`, `source_use_ledger.csv`, `adverse_evidence_ledger.csv`.
- Copied literal source bodies into `source_bodies/` and source/license witnesses into `source_witnesses/`.
- Added manifest and checksum files: `MANIFEST.csv`, `SHA256SUMS.txt`.

## Not Done / Unsatisfied

- No complete interlanguage or dominant-language translation is claimed by this support lane.
- No native review, accepted terminology, license clearance, gate promotion, source certification, final status, or translation completion is claimed.
- Non-English relation/function native source witnesses are not present in this OLP Fable block; they are recorded as source-acquisition gaps in `languages.csv`, `branch_weight_ledger.csv`, and `marginal_intelligibility.csv`.
- Marginal intelligibility scores are not promoted as measured comprehension; rows remain exploratory because cohort witnesses are incomplete.
'@
Write-Utf8 'rules_acknowledgement.md' $rules

$ack = @'
# FABLE REQUIREMENTS ACKNOWLEDGED 20260705

This package is an OLP/OpenTranslation/relation-function support-lane implementation of the Fable data requirements. It is not a completed interlanguage, not a native review return, not accepted terminology, not source certification, not license clearance, and not translation completion.

## Satisfied In This Package

- Heartbeat recreated: `noether-mandatory-fable-interlanguage-heartbeat-3`.
- Active goal set with the goal tool and mirrored to local durability files: `HEARTBEAT_20260705.md` and `SESSION_LOGBOOK_20260705.md`.
- Literal source bodies copied under `source_bodies/`.
- Source/license witnesses copied under `source_witnesses/`.
- Required Fable ledgers produced:
  - `languages.csv`
  - `source_documents.csv`
  - `lexemes.jsonl`
  - `forms.csv`
  - `word_weights.csv`
  - `branch_weight_ledger.csv`
  - `marginal_intelligibility.csv`
  - `do_not_use.csv`
  - `rules_acknowledgement.md`
- Additional support ledgers produced: `source_use_ledger.csv`, `adverse_evidence_ledger.csv`.
- Package audit files produced: `MANIFEST.csv`, `SHA256SUMS.txt`, `README.md`, `SESSION_LOGBOOK_20260705.md`.

## Unsatisfied / Gaps

- Complete translation/pre-translation into every interlanguage and dominant language is outside this support-lane artifact and remains active program work.
- Relation/function target-language native witnesses beyond English were not present in this OLP support body set; rows are marked source-acquisition gaps.
- The Fable marginal-intelligibility numeric model is represented as ledger fields here, but not promoted to measured comprehension because cohort evidence is incomplete.
- External/native/community review remains zero for this package.

## Exact Output Path

`C:\Users\memo_\Documents\Codex\2026-07-04\noether-olp-relation-function-support\interlanguage-sidecar\20260705\olp_relation_function_fable_block`
'@
Write-Utf8 "FABLE_REQUIREMENTS_ACKNOWLEDGED_$Date.md" $ack

$readme = @'
# OLP Relation/Function Fable Block

Generated: 2026-07-05 Europe/Amsterdam
Lane: OLP/OpenTranslation/relation-function support
Status: generated-draft / non-canonical support only

This package implements the Fable formal object for the OLP relation/function support slice as data. It contains copied source bodies, source witnesses, required Fable ledgers, source-use/adverse ledgers, manifest, hashes, and logbook. It does not claim native review, accepted terminology, license clearance, gate promotion, source certification, final status, or translation completion.

The branch-weight ledger intentionally records a skewed source state: this support slice has English source bodies and formula-neighboring symbolic scaffolds, but no non-English native relation/function witnesses. The correct Fable action is to keep candidate interlanguage forms as generated-draft/non-canonical and record source-acquisition gaps.
'@
Write-Utf8 'README.md' $readme

$log = @"
# Session Logbook 20260705

Timestamp: 2026-07-05 Europe/Amsterdam
Lane: OLP/OpenTranslation/relation-function support
Heartbeat id: $HeartbeatId

Read/applied:
- origin/codex/noether-pc-20260629:FABLE_INTERLANGUAGE_PROGRAM_BLOCKING_DIRECTIVE_20260705.md
- interlanguage-sidecar/20260705/fable_chatgpt_interlingua_program_full/README.md
- mirror manifest
- BRANCH_WEIGHTING_SPEC.md
- SOURCE_USE_POLICY.md
- HEURISTIC_REGISTER.md
- CHATGPT_PRO_TASK_SPEC_20260704.md
- DO_NOT_USE_LEDGER_20260704.md
- INTERSLAVIC_GATE_MAP.md

Local paths read:
- $PackageRoot

Local paths written:
- $OutRoot
- $TopHeartbeat
- $TopLogbook

Concrete output:
- Required Fable ledgers, source bodies, source witnesses, source-use ledger, adverse evidence ledger, manifest, checksum file, and Fable acknowledgement.

Boundary:
No native review, accepted terminology, license clearance, gate promotion, source certification, final status, or translation completion claimed.
"@
Write-Utf8 'SESSION_LOGBOOK_20260705.md' $log

# Manifest and checksums.
$manifestRows = New-Object System.Collections.Generic.List[object]
$sumPath = Join-Path $OutRoot 'SHA256SUMS.txt'
Get-ChildItem -LiteralPath $OutRoot -Recurse -File |
  Where-Object { $_.FullName -ne $sumPath } |
  Sort-Object FullName |
  ForEach-Object {
    $rel = $_.FullName.Substring($OutRoot.Length).TrimStart('\') -replace '\\', '/'
    $top = ($rel -split '/')[0]
    $label = switch ($top) {
      'source_bodies' { 'source-witness' }
      'source_witnesses' { 'source-witness' }
      'generated-draft' { 'generated-draft' }
      default { if ($rel -match 'ledger|languages|source_documents|forms|weights|intelligibility|do_not_use|MANIFEST|SHA256|acknowledgement|ACKNOWLEDGED') { 'audit-ledger' } else { 'methodology' } }
    }
    $manifestRows.Add([pscustomobject]@{
      relative_path = $rel
      bytes = $_.Length
      sha256 = (Get-FileHash -Algorithm SHA256 -LiteralPath $_.FullName).Hash.ToLowerInvariant()
      source_use_label = $label
      note = 'Fable OLP relation/function block; no approval or completion claim'
    }) | Out-Null
  }
$manifestRows | Export-Csv -LiteralPath (Join-Path $OutRoot 'MANIFEST.csv') -NoTypeInformation -Encoding utf8

$sumLines = Get-ChildItem -LiteralPath $OutRoot -Recurse -File |
  Where-Object { $_.FullName -ne $sumPath } |
  Sort-Object FullName |
  ForEach-Object {
    $rel = $_.FullName.Substring($OutRoot.Length).TrimStart('\') -replace '\\', '/'
    $hash = (Get-FileHash -Algorithm SHA256 -LiteralPath $_.FullName).Hash.ToLowerInvariant()
    "$hash  $rel"
  }
Set-Content -LiteralPath $sumPath -Value $sumLines -Encoding ascii

"OUT_ROOT $OutRoot"
"FILES $((Get-ChildItem -LiteralPath $OutRoot -Recurse -File | Measure-Object).Count)"
"MANIFEST_ROWS $((Import-Csv -LiteralPath (Join-Path $OutRoot 'MANIFEST.csv') | Measure-Object).Count)"
