# Noether Romance Stale-Reader Reconciliation

Draft / non-canonical / not native reviewed / not approved.

This note reconciles older Romance reader-facing artifacts with the post-audit addenda. It does not alter canonical ledgers, reviewer packets, gates, approvals, or Git state.

## Why This Exists

Some earlier Romance artifacts were correct when written but now preserve a historical coverage state:

- `NOETHER_ROMANCE_CORPUS_TRANSLATION_SLICES_20260704.md` ends with a 40-covered / 6-blocked coverage statement.
- `NOETHER_ROMANCE_CORPUS_TRANSLATION_ROW_COVERAGE_20260704.csv` preserves the original 6 `term_evidence_blocked_no_german_slice` rows.
- Early run-log entries record the same historical 40 / 6 state.

Those statements are superseded for completed-reader use by:

- `NOETHER_ROMANCE_BLOCKER_RESOLUTION_ADDENDUM_20260704.md`
- `NOETHER_ROMANCE_BLOCKER_RESOLUTION_COVERAGE_ADDENDUM_20260704.csv`
- `NOETHER_ROMANCE_TENSOR_BLOCKER_NOTE_CORRECTION_20260704.md`
- `NOETHER_ROMANCE_FLAGGED_ROW_EVIDENCE_SUPPLEMENT_20260704.md`
- `NOETHER_ROMANCE_CURRENT_READER_COVERAGE_20260704.csv`

## Current Reader State

- Total active Romance row instances: 46.
- Current draft/source-note covered row instances: 44.
- Current precise blockers: 2.
- Remaining blockers:
  - `term-fr-0008`: tensor product -> `produit tensoriel`, terminology sidecar only.
  - `term-es-0010`: tensor product -> `producto tensorial`, terminology sidecar only.

Corrected tensor blocker statement:

No direct German prose hit was found for `Tensorprodukt`, `Tensor`, or lowercase `tensor`. The LocalCodex cumulative contains noisy `\otimes` hits around coordinator-cited lines `21525` and `21582`, but those notation hits do not name or explain tensor product and cannot support French or Spanish corpus prose.

## Current Consolidated Coverage CSV

Use `NOETHER_ROMANCE_CURRENT_READER_COVERAGE_20260704.csv` for the current reader-facing row state. It is a draft sidecar that combines:

- base row coverage from `NOETHER_ROMANCE_CORPUS_TRANSLATION_ROW_COVERAGE_20260704.csv`;
- source-bridge updates from `NOETHER_ROMANCE_BLOCKER_RESOLUTION_COVERAGE_ADDENDUM_20260704.csv`;
- evidence/manual-review updates from `NOETHER_ROMANCE_FLAGGED_ROW_EVIDENCE_SUPPLEMENT_20260704.csv`.

Current consolidated status counts:

- `translated_slice`: 30
- `translated_slice_with_source_note`: 8
- `translated_slice_addendum_source_bridge`: 4
- `translated_slice_evidence_gap_narrowed`: 1
- `manual_review_flag_retained`: 1
- `deepened_blocker_no_usable_tensor_anchor`: 2

All rows remain `not_reviewed` and `not_approved`.

## Completed-Reader Rule

For reader integration, treat the base corpus slices as the prose body and the addenda as required errata/updates. Do not use the old 40 / 6 statement as the current lane state. Do not infer tensor-product prose from noisy `\otimes` notation, `Kroneckerschen Produkt`, or Romance-side terminology evidence.

