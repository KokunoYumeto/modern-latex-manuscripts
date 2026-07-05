# Pan-Romance Term-Level Access Ledger — handoff spec
2026-07-04. For the codex Pan-Romance lane (R1). This is the artifact its own pilot gate declares missing: "optimal-access/new-inter-intelligibility ledger for contested terms and proof grammar, citing source evidence and naming access-gain cohorts" (PAN_ROMANCE_OPTIMAL_ACCESS_HEURISTIC_INTEGRATION_20260629). Status without it: `source_or_policy_partial_no_pilot`.

## Row schema (one row per contested term/spelling/proof-phrase decision)

```text
term_id:                      T01..T60 spine id or new
concept:                      english concept label (concept-ledger id when available)
candidate_forms:              [surface candidates with language-of-origin tags]
es_fr_tier0_evidence:         file:line pointers (already exist in source-hit table)
fallback_row_evidence:        pt/gl/ca/it/ro/rm attested forms (already exist in fallback review)
sga_certified_usage:          French register witness where applicable (see F7 note)
comparator_layer:             interlingua/esperanto/etc hits — evidence floor ONLY, never authority
support:                      per cohort: which readers gain (named, not "Romance readers")
adverse:                      typed — false_friend_or_collision | dominance_risk(es/fr/it) |
                              register_mismatch | script_or_standard_confusion | competitor_support
main_register_retention:      does the es/fr/it/pt main reader still parse it?
marginal_gain_over_spanish:   the lane's own founding heuristic, per cohort
variant_policy:               single form | doublet | gloss | crosswalk | unpromoted
decision:                     promoted_seed | doublet | deferred | unpromoted
reviewer_need:                yes/no + which community
source_pointers:              all of the above, file-pinned
```

## Priority rows (from existing lane evidence)
1. The 8 partial + 6 sparse fallback rows (fallback summary: PT 52/60 … RM 30/60) — these are where a single form most likely loses a cohort.
2. High-pressure terms the lane itself lists: ring, field, proof, group, homomorphism, module, ideal, Noetherian, Artinian.
3. Every row whose only promoted-register support is warning-comparator hits (16 rows — enumerated in DO_NOT_USE_LEDGER as authority_needed).
4. Doublet-policy candidates surfaced by cross-lane analogy with Slavic backfill: determinant-type rows where one major standard uses a native lexeme (watch: RO/RM often have both Latinate and Slavic-influenced doublets).

## Rules carried over (already lane policy, restated for the ledger)
- Spanish is Tier-0 evidence, not hidden authority; a Spanish-looking form needs cross-Romance recognizability to be kept (dominance_penalty).
- Comparators can block invented forms; they cannot outrank native evidence.
- If no single form preserves both retention and new gain → doublet/crosswalk, never a forced pan-form.
- Thin evidence → row stays unpromoted (three-state discipline: support / absence / adverse).

## Deliverable + gate
`PAN_ROMANCE_ACCESS_LEDGER_v1.{md,json}` in the lane's logs, rows for priority classes 1–3 minimum. When present and internally reviewed, lane status may move from `source_or_policy_partial_no_pilot` to `ledger_present_review_pending` (still no pilot claim — external Romance review remains the gate, per non-erasure boundary).
