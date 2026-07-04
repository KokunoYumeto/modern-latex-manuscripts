# Fable 5 language-only handoff: computational interlinguistics consolidation

## Scope

This program is strictly about language-family bridge systems, multilingual model representations, corpus organization, geography of language communities, scripts, standards, governance, and human intelligibility. Do not use the analogy strands. Do not explain the project through non-linguistic metaphors. Treat those as discarded brainstorming context.

The task is to consolidate the existing islands of work into one research map: theory documents, construction logs, glossary files, parallel corpora, language-family queues, operational gates, and proposed evaluation metrics.

## One-line thesis

The current construction pipeline is already performing an informal optimization procedure for language-family bridge design. The research task is to make that procedure explicit, measurable, and auditable: passive recognizability, source-family coverage, semantic-neighborhood preservation, false-friend avoidance, script accessibility, governance constraints, and human intelligibility become the scored terms.

## Core research objects

### 1. Bridge system types

A language-family intervention is classified as one of three objects:

1. Zonal language: a semi-constructed bridge variety for a related language family or subfamily.
2. Controlled register: a restricted, simplified, or standardized register of an existing language where a new language would be unnecessary or socially counterproductive.
3. Script bridge: an orthographic or transliteration layer that improves access without creating a new linguistic standard.

The siting question is not “what language should we invent?” It is “which intervention type is justified for this family, region, and use case?”

### 2. Candidate bridge form

For each concept `c`, a bridge candidate `b(c)` is evaluated by:

- recognizability across source languages;
- coverage across subbranches;
- cognate or inheritance support;
- semantic stability;
- false-friend risk;
- morphological regularity;
- script and orthographic accessibility;
- political and governance cost;
- corpus attestation and explainability.

### 3. Family barycenter

A bridge system is treated as a regularized center of a language family, not as a reconstruction of an ancestor and not as a majority vote alone. The relevant center balances source-family coverage, human recognizability, fairness among branches, and avoidance of misleading forms.

Informal formula:

```text
best_bridge = minimize(
    distance_to_source_languages
  + false_friend_risk
  + learning_cost
  + script_cost
  + governance_cost
  - recognizability
  - coverage
  - semantic_alignment
)
```

### 4. Semantic-neighborhood preservation

Multilingual model geometry is used as an instrument, not an oracle. For each concept, compare nearest-neighbor structure across languages and across bridge candidates. A good bridge candidate should preserve local semantic neighborhoods for many source-language speakers.

Useful model-side observables:

- Interlingual Local Overlap or nearest-neighbor overlap;
- concept-cluster stability across languages;
- local intrinsic dimension or representation complexity;
- semantic drift across cognate sets;
- mismatch between form similarity and meaning similarity.

### 5. False-friend risk

False-friend risk is a central penalty, not a side issue.

```text
false_friend_risk(candidate, concept)
  = sum over source languages and rival concepts of
    form_similarity(candidate, rival_form)
  * semantic_distance(concept, rival_concept)
  * source_language_weight
```

The goal is to prevent a bridge form from activating the wrong concept in part of the intended audience.

## Dimension idea, language-only form

Intrinsic dimension is used as a geometry-based measure of representational degrees of freedom in text and model representations. It is not treated as prediction entropy, fluency, or quality by itself.

Use it for:

1. detecting whether a corpus segment is formulaic, ordinary, specialized, creative, or unstable;
2. comparing technical text, glossaries, translations, conversational logs, and narrative material;
3. measuring whether a proposed bridge register is too narrow, too overloaded, or appropriately expressive;
4. identifying local regions where the model needs extra representational degrees of freedom, especially high-ambiguity or high-register-shift zones.

Operational caution:

- low dimension may indicate constrained technical prose or repetitive collapse;
- high dimension may indicate expressive richness or unstable mixture;
- dimension must be interpreted with genre, length, language, and model held under control.

## Noether idea, language-only form

Keep only the invariance idea. Avoid naming non-linguistic theory unless required.

A bridge system should preserve intended meaning under accepted transformations:

- translation;
- paraphrase;
- inflectional variation;
- script conversion;
- dialectal variant;
- register shift;
- controlled simplification.

Define an invariant ledger:

```text
invariant_id | transformation | should_preserve | allowed_change | test | failure_mode
```

Example:

```text
INV-SCRIPT-001 | Cyrillic-to-Latin conversion | lemma identity and pronunciation cue | minor orthographic convention | round-trip transliteration | false cognate or homograph introduced
INV-REG-004 | technical-to-controlled register | proposition content | reduced style and syntax | human comprehension test | loss of contrast or ambiguity
INV-ZONAL-012 | source-language-to-bridge mapping | intended concept | family-central surface form | forced-choice comprehension | false-friend activation
```

This is the clean version of the symmetry idea: identify what must remain stable under transformations and test whether it remains stable.

## Threshold idea, language-only form

Treat thresholds as operational readiness thresholds, not as a claim about cognition.

A bridge lane becomes viable only after enough independent constraints align:

- corpus coverage exceeds a minimum threshold;
- false-friend risk is below threshold;
- recognizability is above threshold across several source branches;
- orthography and script policy are settled;
- governance risk is acceptable;
- human intelligibility tests pass above threshold;
- model-side alignment metrics stop changing under reasonable corpus additions.

Below threshold, the lane is exploratory. Near threshold, it is unstable and should not be public-standardized. Above threshold, it can enter a release gate.

## Corpus map

The corpus should be documented as three strata.

### Theory stack

Purpose: defines the measurable framework.

Expected contents:

- computational interlinguistics framework;
- bridge-language barycenter model;
- false-friend risk model;
- semantic-neighborhood preservation metrics;
- intrinsic-dimension diagnostics;
- governance and non-erasure principles.

### Practice stack

Purpose: records actual construction decisions.

Expected contents:

- Interslavic gate logs;
- Pan-Romance kernel drafts;
- language-family priority queue;
- controlled-register and script-bridge decisions;
- rejected forms with rationales;
- release gates and operational criteria.

### Data stack

Purpose: supplies evidence and alignment material.

Expected contents:

- term-rationale glossaries;
- source-language tables;
- parallel corpora;
- Noether multilingual math corpus;
- Interslavic both-script material;
- translation variants and rejected alternatives;
- false-friend lists.

## Claim ledger schema

Every substantive claim should be entered into a claim ledger.

```text
claim_id:
claim:
status: established | supported | plausible | speculative | rejected | out_of_scope
source_files:
evidence:
operational_test:
risk_if_wrong:
next_action:
```

Example:

```text
claim_id: CLM-ILO-001
claim: Nearest-neighbor semantic overlap predicts passive intelligibility better than form similarity alone for some bridge-language candidates.
status: plausible
source_files: theory sidecar; multilingual representation papers; Interslavic logs
operational_test: compare model-side overlap scores against human forced-choice comprehension data
risk_if_wrong: model geometry is not useful for construction decisions
next_action: build a 200-concept pilot table and test against existing Interslavic forms
```

## Heuristic register schema

Heuristics should be retained only if they become operational.

```text
heuristic_id:
raw_heuristic:
clean_form:
measurement:
use_in_pipeline:
status:
```

Example:

```text
heuristic_id: HEU-DENSE-BRANCH-001
raw_heuristic: look for dense branch points
clean_form: identify concepts and forms with high family coverage, low drift, and low false-friend risk
measurement: coverage score, semantic drift score, false-friend risk score
use_in_pipeline: candidate selection and siting table
status: keep
```

## Siting table schema

The siting table decides whether a family/region deserves a zonal language, controlled register, script bridge, or no intervention.

```text
lane_id:
family_or_region:
intervention_type: zonal_language | controlled_register | script_bridge | none | mixed
coverage_score:
mutual_intelligibility_score:
standard_language_presence:
script_fragmentation_score:
false_friend_risk:
governance_risk:
corpus_readiness:
recommended_next_step:
```

## Priority sequence

Recommended immediate sequence:

1. Deep-read the Interslavic logbook and extract all explicit construction rationales.
2. Build a claim ledger from the theory sidecar and logbook.
3. Build a heuristic register and mark every heuristic as keep, translate, test, or discard.
4. Create the first siting table for current queue items.
5. Feed the results back into the Interslavic gate.
6. Use the same schema for the Pan-Romance kernel.
7. Only after the corpus and ledgers are clean, run optional embedding measurements.

## Safe operating prompt

Use this as a working instruction:

> Work only on computational interlinguistics, multilingual representation analysis, zonal auxiliary languages, controlled registers, script bridges, corpus organization, and governance. Ignore all discarded analogy strands. Consolidate the existing corpus into a claim ledger, heuristic register, corpus map, and siting table. Preserve construction details. Do not invent new research claims without marking them as hypotheses. Make the bridge between theory and practice explicit: recognizability, coverage, semantic-neighborhood preservation, false-friend avoidance, script accessibility, governance cost, and human intelligibility.

## Immediate P0.2 task

Deep-read the Interslavic logbook. Extract:

1. every term-rationale decision;
2. every rejected alternative and reason;
3. every false-friend warning;
4. every script or orthography policy;
5. every governance or non-erasure rule;
6. every implicit metric already being used;
7. every place where a model-side measurement could replace or support an editorial judgment.

Output three files:

1. `CLAIM_LEDGER.md`
2. `HEURISTIC_REGISTER.md`
3. `INTERSLAVIC_GATE_MAP.md`
