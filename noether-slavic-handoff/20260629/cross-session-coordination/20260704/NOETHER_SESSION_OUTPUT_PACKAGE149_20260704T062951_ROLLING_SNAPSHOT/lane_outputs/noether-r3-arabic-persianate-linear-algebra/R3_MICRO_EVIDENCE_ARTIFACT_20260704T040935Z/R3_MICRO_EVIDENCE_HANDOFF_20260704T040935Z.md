# R3 Micro-Evidence Artifact (20260704T040935Z)

Status: `r3_micro_evidence_noncanonical_no_bridge_no_native_review_no_git_push`.

This artifact routes controlled Arabic, Persian/Farsi, Persianate/Dari/Tajik, Pan-Turkic-adjacent, Urdu/Hindustani-separate, and adjacent linear-algebra rows into explicit evidence buckets. It is not a translation release.

## Files

- Route bucket ledger CSV: `R3_MICRO_EVIDENCE_ROUTE_BUCKET_LEDGER_20260704T040935Z.csv`
- Route bucket ledger JSON: `R3_MICRO_EVIDENCE_ROUTE_BUCKET_LEDGER_20260704T040935Z.json`
- Validation JSON: `R3_MICRO_EVIDENCE_VALIDATION_20260704T040935Z.json`

## Route Buckets

- `arabic`: `87` primary rows.
- `novel_blocked`: `59` primary rows.
- `pan_turkic`: `3` primary rows.
- `persianate_tajik`: `69` primary rows.

Rows may also have multi-bucket routing in `route_bucket` when a source row informs more than one split lane; the primary bucket is the safest downstream owner.

## Evidence Status

- Total rows: `218`.
- Rows with noncanonical micro-translation support: `168`.
- Rows recorded only as blockers/source questions: `50`.
- High-risk bridge placeholder rows preserved: `7`.

## Boundaries

- `term_promotion_allowed=false` for every row.
- `bridge_promotion_allowed=false` for every row.
- `native_review_claim=false` for every row.
- `git_push=false` for every row.
- Bridge candidates are carried only in `bridge_candidate_nonpromoted`, never as accepted surfaces.
- Urdu/Hindustani rows are separate-lane evidence, not Persianate merge evidence.
- Pan-Turkic rows are routed as Pan-Turkic/open-gate or blocker material only; no Pan-Turkic bridge is produced.

## Source Row Groups

- `arabic_msa_linear_system_microdraft`: `14` rows.
- `arabic_msa_vector_space_microdraft`: `13` rows.
- `dari_afghan_linear_system_source_gate`: `10` rows.
- `dari_afghan_vector_space_source_gate`: `8` rows.
- `eigenvalue_regional_future_slice`: `26` rows.
- `hefferon_first_slice_linear_algebra_seed`: `16` rows.
- `paper01_60_term_route_ledger`: `62` rows.
- `persian_farsi_linear_system_microdraft`: `14` rows.
- `persian_farsi_vector_space_microdraft`: `13` rows.
- `tajik_cyrillic_vector_space_microdraft`: `12` rows.
- `urdu_hindustani_linear_system_microdraft`: `11` rows.
- `urdu_hindustani_vector_space_microdraft`: `10` rows.
- `wikibooks_hefferon_crosscheck`: `9` rows.

## Consumption Rule

Use `noncanonical_micro_translation_support` only when nonempty and only for the named route bucket. Otherwise use the row as a blocker/source question. No row may be promoted without independent source and native/domain review closure.