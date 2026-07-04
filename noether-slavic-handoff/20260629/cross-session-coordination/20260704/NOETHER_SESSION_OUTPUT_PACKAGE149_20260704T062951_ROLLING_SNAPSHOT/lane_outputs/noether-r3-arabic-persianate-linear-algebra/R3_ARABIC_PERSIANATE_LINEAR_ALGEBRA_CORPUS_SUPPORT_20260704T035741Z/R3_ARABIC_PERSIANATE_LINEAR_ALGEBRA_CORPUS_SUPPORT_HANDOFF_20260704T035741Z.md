# R3 Arabic/Persianate Linear-Algebra Corpus Support Handoff (20260704T035741Z)

Status: `corpus_support_noncanonical_no_promotion_no_native_review_claim`.

This bundle routes recovered R3 Prompt-A-3 Arabic, Persian/Farsi, Dari/Afghan Persian, Tajik, Urdu/Hindustani, and adjacent linear-algebra evidence into split downstream lanes. It is a source-evidence and draft-support artifact only.

## Deliverables

- Route ledger CSV: `R3_ARABIC_PERSIANATE_LINEAR_ALGEBRA_ROUTE_LEDGER_20260704T035741Z.csv`
- Route ledger JSON: `R3_ARABIC_PERSIANATE_LINEAR_ALGEBRA_ROUTE_LEDGER_20260704T035741Z.json`
- Validation manifest: `R3_ARABIC_PERSIANATE_LINEAR_ALGEBRA_CORPUS_SUPPORT_VALIDATION_20260704T035741Z.json`

## Boundaries

- Accepted bridge promotions: `0`.
- Term promotions: `0`.
- Native/domain-review claims: `0`.
- Git pushes: `0`.
- Arabic RTL rows may consume controlled Arabic evidence only as draft/review support.
- Persianate/Farsi rows may consume Persian/Farsi evidence only as draft/review support.
- Dari/Afghan Persian rows are source-gate only unless their independent gate closes.
- Tajik Cyrillic rows are their own review-only lane and do not inherit Farsi/Dari surfaces.
- Urdu/Hindustani and Pan-Turkic material remain separate lanes with no merge authority.

## Row Totals

- Total route rows: `218`.
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

## Consumer-Lane Distribution

- `adjacent_linear_algebra_source_lane`: `24` rows.
- `arabic_rtl_lane`: `4` rows.
- `arabic_rtl_lane; adjacent_linear_algebra_source_lane`: `30` rows.
- `arabic_rtl_lane; persianate_farsi_lane`: `19` rows.
- `arabic_rtl_lane; persianate_farsi_lane; adjacent_linear_algebra_source_lane`: `9` rows.
- `arabic_rtl_lane; persianate_farsi_lane; urdu_hindustani_separate_lane; adjacent_linear_algebra_source_lane`: `25` rows.
- `none_until_gate_closure`: `16` rows.
- `persianate_dari_gate_lane; adjacent_linear_algebra_source_lane`: `18` rows.
- `persianate_farsi_lane`: `3` rows.
- `persianate_farsi_lane; adjacent_linear_algebra_source_lane`: `36` rows.
- `tajik_cyrillic_lane; adjacent_linear_algebra_source_lane`: `12` rows.
- `urdu_hindustani_separate_lane; adjacent_linear_algebra_source_lane`: `22` rows.

## Hard Rows Preserved

- Paper01/60-term high-risk bridge placeholders remain blocked: `invariant_theory`, `covariant`, `contravariant`, `relatively_complete_system`, `absolutely_complete_system`, `modulus_not_module`, `transvection`.
- Paper01/60-term Arabic open/missing/not-in-spine rows remain visible in the CSV with `route_arabic_rtl_lane` set to an open or do-not-consume value.
- Arabic specialist invariant/covariant/binary-form direct source counts remain unclosed; secondary/current-register evidence is reviewer-prompt material only.
- Direct Dari/Afghan Persian invariant-theory and TeX/source-code closure remains absent; Dari linear/vector material in this artifact is source-gate support only.
- Eigenvalue/eigenvector rows remain a future evidence slice, not a term unlock.

## Consumption Rules

Downstream lanes should read `consumer_lane`, then the specific `route_*` columns. A row can be used only for the lane named in those route columns, only under `consumption_action`, and only while preserving `term_promotion_allowed=false` and `bridge_promotion_allowed=false`.

Surface columns are non-canonical draft/evidence surfaces copied from recovered review-only artifacts. They are not accepted lexemes.

## Source Roots

- Prompt-A-3 outputs: `C:\Users\memo_\Documents\Codex\2026-06-28\see-attached-you-do-prompt-a-3\outputs`
- Canonical tree: `C:\Users\memo_\Documents\Codex\2026-06-09\could-you-look-online-for-me\work\noether-slavic-canonical`