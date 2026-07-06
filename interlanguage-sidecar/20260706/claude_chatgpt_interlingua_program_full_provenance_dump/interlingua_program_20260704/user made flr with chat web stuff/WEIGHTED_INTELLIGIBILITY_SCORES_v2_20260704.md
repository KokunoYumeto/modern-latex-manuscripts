# Weighted marginal-intelligibility scores — v2

Bounded scoring pass over the comparative Interslavic term packet. Scores are attestation proxies for passive intelligibility, not human comprehension measurements. No terms are promoted, rejected, or invented.

## Inputs and boundary

- Loaded `COMPARATIVE_TERM_ANALYSIS_v1_20260704.json`, `ws_witness_backfill_v1_20260704.json`, `BRANCH_WEIGHTING_SPEC.md`, and `DO_NOT_USE_LEDGER_20260704.json` extracted from `interlingua_program_20260704_v1.zip`.
- Do-not-use/adverse ledger: 123 entries; relation distribution `{'false_friend_or_collision': 1, 'semantic_opposite': 1, 'dominance_risk': 41, 'competitor_support': 1, 'register_mismatch': 1, 'authority_needed': 16, 'do_not_inherit_into_lane': 62}`.
- Veto/adverse evidence is not subtracted as a negative score. It is carried as a typed constraint or review note.
- Population-proxy weights are sensitivity weights only and should be replaced by a source-pinned speaker table before publication.

## Cohorts

| Cohort | Equal-splits weight | Population-proxy millions | Population-proxy weight |
|---|---:|---:|---:|
| E | 0.333 | 195.9 | 0.699 |
| W_cs_sk | 0.167 | 15.8 | 0.056 |
| W_pl | 0.167 | 38.0 | 0.136 |
| S_hr_sr | 0.111 | 19.0 | 0.068 |
| S_sl | 0.111 | 2.1 | 0.007 |
| S_bg | 0.111 | 9.4 | 0.034 |

## Priority and variant rows

| Rank | Concept | Current | Best non-current group | Mean MAG | Action | Sensitivity |
|---:|---|---|---|---:|---|---|
| 1 | ring | `kolco` | prsten / pierścień / prăsten coalition | +0.095 | review_priority | weight_sensitive |
| 2 | quotient field | `polje častnikov?` | West native quotient-field terms | -0.081 | review_priority | weight_sensitive |
| 3 | extension (field) | `razširjenje?` | W/S extension-family alternatives | -0.066 | variant_or_doublet_note | weight_sensitive |
| 4 | splitting field | `razpadno polje` | rozklad / rozkład family | -0.262 | variant_or_doublet_note | stable |
| 5 | trace | `sled?` | West native trace terms | -0.269 | variant_or_doublet_note | stable |
| 6 | corollary | `korolar?` | West native corollary terms | -0.278 | variant_or_doublet_note | stable |
| 7 | theorem | `teorema` | West native theorem terms | -0.336 | variant_or_doublet_note | stable |
| 8 | determinant | `determinanta` | pl wyznacznik | -0.616 | variant_or_doublet_note | stable |
| 9 | polynomial | `polinom` | pl wielomian | -0.616 | variant_or_doublet_note | stable |

## Concept-level review notes

### ring
Current: `kolco`. Action: `review_priority`. Sensitivity: `weight_sensitive`.
Input packet question: Current 'kolco' vs branch-attested alternatives: which serves family-central passive recognizability best, and is a doublet required for West readers?

| Candidate/group | Kind | Cohorts | Equal branch | Equal splits | Population | PD | MAG eq-branch | MAG eq-splits | MAG pop | MAG PD | Constraint/note |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| prsten / pierścień / prăsten coalition | coalition | S_bg, S_hr_sr, W_pl | 0.667 | 0.389 | 0.237 | 0.636 | +0.333 | +0.056 | -0.462 | +0.455 | branch-attested cognate family; review question, not promotion |
| kolco | current | E | 0.333 | 0.333 | 0.699 | 0.182 | +0.000 | +0.000 | +0.000 | +0.000 |  |
| okruh family | competitor | W_cs_sk | 0.333 | 0.167 | 0.056 | 0.273 | +0.000 | -0.167 | -0.643 | +0.091 | VETO/constraint; adverse/collision-sensitive: okruh may collide with East Slavic okrug/district; do-not-use ledger contains kolco dominance-risk but no direct okruh row |
| kolobar | competitor | S_sl | 0.333 | 0.111 | 0.007 | 0.273 | +0.000 | -0.222 | -0.692 | +0.091 |  |

### splitting field
Current: `razpadno polje`. Action: `variant_or_doublet_note`. Sensitivity: `stable`.
Input packet question: Confirm 'razpadno polje' (support pattern acceptable) or note preferred variant policy.

| Candidate/group | Kind | Cohorts | Equal branch | Equal splits | Population | PD | MAG eq-branch | MAG eq-splits | MAG pop | MAG PD | Constraint/note |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| razpadno polje | current | E, S_sl | 0.667 | 0.444 | 0.707 | 0.455 | +0.000 | +0.000 | +0.000 | +0.000 |  |
| rozklad / rozkład family | coalition | W_cs_sk, W_pl | 0.333 | 0.333 | 0.192 | 0.364 | -0.333 | -0.111 | -0.515 | -0.091 |  |

### determinant
Current: `determinanta`. Action: `variant_or_doublet_note`. Sensitivity: `stable`.
Input packet question: Confirm 'determinanta' (support pattern acceptable) or note preferred variant policy.

| Candidate/group | Kind | Cohorts | Equal branch | Equal splits | Population | PD | MAG eq-branch | MAG eq-splits | MAG pop | MAG PD | Constraint/note |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| determinanta | current | E, S_hr_sr, S_sl, W_cs_sk | 1.000 | 0.722 | 0.831 | 0.818 | +0.000 | +0.000 | +0.000 | +0.000 |  |
| pl wyznacznik | competitor | W_pl | 0.333 | 0.167 | 0.136 | 0.273 | -0.667 | -0.556 | -0.695 | -0.545 |  |

### polynomial
Current: `polinom`. Action: `variant_or_doublet_note`. Sensitivity: `stable`.
Input packet question: Confirm 'polinom' (support pattern acceptable) or note preferred variant policy.

| Candidate/group | Kind | Cohorts | Equal branch | Equal splits | Population | PD | MAG eq-branch | MAG eq-splits | MAG pop | MAG PD | Constraint/note |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| polinom | current | E, S_hr_sr, S_sl, W_cs_sk | 1.000 | 0.722 | 0.831 | 0.818 | +0.000 | +0.000 | +0.000 | +0.000 |  |
| pl wielomian | competitor | W_pl | 0.333 | 0.167 | 0.136 | 0.273 | -0.667 | -0.556 | -0.695 | -0.545 |  |

### quotient field
Current: `polje častnikov?`. Action: `review_priority`. Sensitivity: `weight_sensitive`.
Input packet question: Current 'polje častnikov?' vs branch-attested alternatives: which serves family-central passive recognizability best, and is a doublet required for West readers?

| Candidate/group | Kind | Cohorts | Equal branch | Equal splits | Population | PD | MAG eq-branch | MAG eq-splits | MAG pop | MAG PD | Constraint/note |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| West native quotient-field terms | coalition | W_cs_sk, W_pl | 0.333 | 0.333 | 0.192 | 0.364 | +0.000 | +0.000 | -0.507 | +0.182 | competitor-only in West; South no-hit in shelf |
| polje častnikov? | current | E | 0.333 | 0.333 | 0.699 | 0.182 | +0.000 | +0.000 | +0.000 | +0.000 |  |

### theorem
Current: `teorema`. Action: `variant_or_doublet_note`. Sensitivity: `stable`.
Input packet question: Confirm 'teorema' (support pattern acceptable) or note preferred variant policy.

| Candidate/group | Kind | Cohorts | Equal branch | Equal splits | Population | PD | MAG eq-branch | MAG eq-splits | MAG pop | MAG PD | Constraint/note |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| teorema | current | E, S_bg, S_hr_sr | 0.667 | 0.556 | 0.800 | 0.545 | +0.000 | +0.000 | +0.000 | +0.000 |  |
| West native theorem terms | coalition | W_cs_sk, W_pl | 0.333 | 0.333 | 0.192 | 0.364 | -0.333 | -0.222 | -0.608 | -0.182 |  |

### corollary
Current: `korolar?`. Action: `variant_or_doublet_note`. Sensitivity: `stable`.
Input packet question: Confirm 'korolar?' (support pattern acceptable) or note preferred variant policy.

| Candidate/group | Kind | Cohorts | Equal branch | Equal splits | Population | PD | MAG eq-branch | MAG eq-splits | MAG pop | MAG PD | Constraint/note |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| korolar? | current | E, S_hr_sr | 0.667 | 0.444 | 0.767 | 0.455 | +0.000 | +0.000 | +0.000 | +0.000 |  |
| West native corollary terms | coalition | W_cs_sk, W_pl | 0.333 | 0.333 | 0.192 | 0.364 | -0.333 | -0.111 | -0.575 | -0.091 |  |
| South native consequence terms | coalition | S_bg, S_hr_sr | 0.333 | 0.222 | 0.101 | 0.364 | -0.333 | -0.222 | -0.666 | -0.091 |  |

### trace
Current: `sled?`. Action: `variant_or_doublet_note`. Sensitivity: `stable`.
Input packet question: Confirm 'sled?' (support pattern acceptable) or note preferred variant policy.

| Candidate/group | Kind | Cohorts | Equal branch | Equal splits | Population | PD | MAG eq-branch | MAG eq-splits | MAG pop | MAG PD | Constraint/note |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| sled? | current | E, S_bg | 0.667 | 0.444 | 0.733 | 0.455 | +0.000 | +0.000 | +0.000 | +0.000 |  |
| West native trace terms | coalition | W_cs_sk, W_pl | 0.333 | 0.333 | 0.192 | 0.364 | -0.333 | -0.111 | -0.541 | -0.091 |  |

### extension (field)
Current: `razširjenje?`. Action: `variant_or_doublet_note`. Sensitivity: `weight_sensitive`.
Input packet question: Confirm 'razširjenje?' (support pattern acceptable) or note preferred variant policy.

| Candidate/group | Kind | Cohorts | Equal branch | Equal splits | Population | PD | MAG eq-branch | MAG eq-splits | MAG pop | MAG PD | Constraint/note |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| W/S extension-family alternatives | coalition | S_hr_sr, W_cs_sk, W_pl | 0.667 | 0.444 | 0.260 | 0.636 | +0.000 | +0.000 | -0.447 | +0.182 | visible cognate relation to razširjenje; typed as competitor by shelf, so review as variant/crosswalk |
| razširjenje? | current | E, S_sl | 0.667 | 0.444 | 0.707 | 0.455 | +0.000 | +0.000 | +0.000 | +0.000 |  |

## Confirmation rows
Under this conservative exact-attestation proxy, the current form remains the highest-coverage packet default for: field, division ring / body, ideal, module, group, noetherian, homomorphism, idempotent, basis, invariant, proof, lemma, definition, example, set, element, subset, isomorphism, automorphism, representation, matrix, vector, dimension, kernel, norm, center, prime ideal, algebra (structure).