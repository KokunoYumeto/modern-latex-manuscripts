# B3 Package Handoff 20260705

Package root:
`C:\Users\memo_\Documents\Codex\2026-07-04\noether-olp-relation-function-support\interlanguage-sidecar\20260705\olp_relation_function_fable_block`

Status: generated-draft / non-canonical / source-probe support only.

This package is prepared for B3 or the uploader to stage if desired. This lane did not push Git and did not claim native review, accepted terminology, canonical approval, source certification, gate promotion, license clearance, final status, or translation completion.

## Contents To Package

- Source bodies and witnesses: `source_bodies/`, `source_witnesses/`
- Fable required ledgers: `languages.csv`, `source_documents.csv`, `lexemes.jsonl`, `forms.csv`, `word_weights.csv`, `branch_weight_ledger.csv`, `marginal_intelligibility.csv`, `do_not_use.csv`, `rules_acknowledgement.md`, `FABLE_REQUIREMENTS_ACKNOWLEDGED_20260705.md`
- Generated-draft support: `generated-draft/relation_function_owner_handoff.md`, `pretranslation_scaffolds.csv`, `interlinear_scaffolds.jsonl`, `owner_route_queue.csv`
- Weak-row source probes: `weak_row_probe_counts.csv`, `weak_row_probe_context_windows.jsonl`, `weak_row_recovered_form_candidates.csv`, `weak_row_recovery_status.csv`
- Branch-gap routing: `branch_gap_recovery_queue.csv`, `owner_source_probe_handoff.csv`
- East/West missing-branch audit: `east_west_gap_probe_audit.csv`, `east_west_gap_probe_contexts.jsonl`
- External source-canon candidates: `source_bodies/external_wikimedia_recovery/20260705/`, `external_wikimedia_source_recovery.csv`, `external_wikimedia_candidate_coverage.csv`, `external_wikimedia_blockers.csv`, `external_wikimedia_context_counts.csv`, `external_wikimedia_context_windows.jsonl`, `external_wikimedia_context_summary.csv`, `external_wikimedia_source_form_candidates.csv`, `external_wikimedia_false_friend_review_slots.csv`
- Repeatable generators: `support-generators/`
- Integrity files: `MANIFEST.csv`, `SHA256SUMS.txt`

## Current Coverage Summary

- Relation/function lexemes: 14
- Source-probe baseline sufficient for scoped owner draft: 14 rows
- Source-probe present but branch gap remains: 0 rows
- East/West missing-branch audit rows: 21
- East/West context rows: 240
- External Wikimedia source bodies recovered: 19
- External Wikimedia candidate coverage rows: 40
- External Wikimedia context windows: 288
- External Wikimedia exact title-form candidates: 19

## Generator Order

1. `support-generators/build_olp_relation_function_fable_block.ps1`
2. `support-generators/update_olp_fable_term_probes.ps1`
3. `support-generators/update_olp_fable_weak_rows.ps1`
4. `support-generators/update_olp_fable_branch_metrics.ps1`
5. `support-generators/update_olp_fable_interlinear_scaffolds.ps1`
6. `support-generators/update_olp_fable_gap_queue.ps1`
7. `support-generators/update_olp_fable_east_west_gap_audit.ps1`
8. `support-generators/update_olp_fable_external_wikimedia_recovery.ps1`
9. `support-generators/update_olp_fable_external_wikimedia_contexts.ps1`
10. `support-generators/update_olp_fable_external_wikimedia_forms.ps1`

## Boundary

Use these outputs as source-canon, audit, and generated-draft support for language-owner work. External Wikimedia exact page-title rows are counted as source-probe witnesses in branch weights, but they remain non-canonical and require owner source-context, false-friend, and formula-neighboring review. Do not convert review-only templates, generated drafts, source probes, or candidate source bodies into reviewer returns, native review, accepted terminology, canonical approval, or completed translation.
