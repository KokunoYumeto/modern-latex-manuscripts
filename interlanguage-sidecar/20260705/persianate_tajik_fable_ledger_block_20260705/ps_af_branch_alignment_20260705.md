# ps_AF Branch Alignment

Generated: 2026-07-05

Status: generated-draft / non-canonical Fable ledger alignment. Not native reviewed. Not accepted terminology. Not canonical approval. Not gate promotion. Not source certification. Not license clearance. Not translation completion.

## Decision

The source-document table now contains `ps_AF` after Pashto Afghanistan eCampus bodies were separated from `prs_AF`. This pass aligns `languages.csv`, `source_use_ledger.csv`, `do_not_use.csv`, and branch-weight string fields with that split.

`ps_AF` is represented as an adjacent source-canon branch with current witness weight `0.0000000`; it is not part of the current Persian/Farsi, Dari, Tajik, Urdu bridge weighting and cannot authorize Dari/Persian Afghanistan rows.

## Files Updated

- `languages.csv` now includes `ps_AF`.
- `source_use_ledger.csv` is refreshed from `source_documents.csv` and includes `ps_AF` rows.
- `do_not_use.csv` includes `DNU-PTR-008` forbidding Pashto evidence from authorizing Dari/Persian rows.
- `word_weights.csv`, `branch_weight_ledger.csv`, and `marginal_intelligibility.csv` annotate `ps=0.0000(excluded-adjacent)` in branch-weight fields.
- `ps_af_branch_alignment_20260705.csv` records per-branch alignment decisions.
