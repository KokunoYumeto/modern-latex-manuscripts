# ChatGPT Pro task spec — weighted marginal-intelligibility scoring
2026-07-04. Paste this spec + the listed input files to ChatGPT Pro. The task is bounded computation and analysis on existing data. It must not invent forms, must not promote terms, and must report weight-sensitivity rather than a single verdict.

## Task, one sentence
Compute weighted marginal-intelligibility comparisons for the 37 concepts in the comparative analysis — Floris's heuristic, operationalized: *does the current Interslavic form add passive intelligibility at the margin over each alternative, per branch cohort, under stated weights?* — and rank the review packet accordingly ("source-genre drift cancellation via weighted intelligibility").

## Inputs (all in the program folder / v1 zip)
1. `COMPARATIVE_TERM_ANALYSIS_v1_20260704.json` — per concept: current form, candidates, branch/language attestation, hit counts, files.
2. `WS_WITNESS_BACKFILL_v1_20260704.json` — raw hits (stems, kinds, per-file counts).
3. `F10_AUDIT_postwriteback_20260704.json` — per-row witness vectors.
4. `DO_NOT_USE_LEDGER_20260704.json` — typed adverse relations (vetoes are constraints, not scores).
5. `BRANCH_WEIGHTING_SPEC.md` — the dependence-corrected weighting layer you specified; use it.
6. `branch_weighting_v0_20260704.json` + `WITNESS_WRITEBACK_v0_20260704.json` — baseline and state-c statistics.

## Computation
For each concept c, candidate x (current ISV form and each attested alternative):
1. **Cohort model**: branches E/W/S at minimum; split W into cs/sk vs pl and S into hr/sr vs sl vs bg where the hit data distinguishes them. State cohort weights w_g explicitly; run THREE weightings: (a) equal-branch, (b) speaker-population-proportional (state your population figures + source), (c) dependence-corrected per the spec (equal-splits on the family tree). No single "true" weighting — report all three.
2. **Intelligibility proxy** I_g(x,c): attestation-based — 1 if cohort's language attests the lexeme family (support hit), partial credit (state it) for cognate-recognizability across the family (e.g., prsten recognizable to East readers as 'ring (jewellery)': register-shifted cognate — flag such cases, don't silently score them), 0 otherwise. Document every partial-credit rule you use.
3. **Marginal comparison**: MAG-style — Σ_g w_g (I_g(x,c) − I_g(x_current,c)), plus the concentration check (does x's gain come mostly from one cohort?). Adverse constraints from input 4 are VETOES applied before scoring (e.g., okruh×okrug collision).
4. **Outputs per concept**: ranking of candidates under each weighting; sensitivity note (does the ranking flip between weightings?); recommended packet phrasing (question form, not verdict). Special attention: ring (kolco vs prsten vs okruh vs kolobar — the memo's options A–E), quotient field, splitting field, the F12 West-calque set (theorem, corollary, trace, extension), doublet candidates (determinant, polynomial).

## Boundaries
- No new target-language wording; only forms already attested in the inputs.
- Vetoes stay vetoes; do not fold adverse evidence into scores.
- Report uncertainty: attestation-based I_g is a proxy for comprehension, not a measurement of it; say so in every summary.
- Output: `WEIGHTED_INTELLIGIBILITY_SCORES_v1.md` (rankings + sensitivity + phrasing) and `.json` (all numbers). These feed the van Steenbergen comparative packet: current vs proposed, which is better and why, under which assumptions.
