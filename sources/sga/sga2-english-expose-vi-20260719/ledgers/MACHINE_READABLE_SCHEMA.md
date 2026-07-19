# Machine-readable evidence schema — SGA 2 Exposé VI cumulative checkpoint

All CSV files are UTF-8 rectangular tables with one header row. Their first column is the stable primary record ID. `record_revision` is numeric; `supersedes` is blank unless a prior record is replaced. Cells that could trigger spreadsheet formulas must be apostrophe-protected; the final validator rejects unprotected cells beginning with `=`, `+`, `-`, or `@` after whitespace.

The seven cumulative CSV ledgers are:

- `COMPONENT_UNIT_INTEGRATION.csv`: six sealed source units; exact TeX/PDF/seal bytes and hashes; normalized mathematical-body hash; cumulative target locator.
- `AUTHORITY_ARTIFACT_HASHES.csv`: corrected French TeX authority; direct French PDF page control; jcreinhold comparison-only Markdown.
- `SOURCE_ALIGNMENT_COVERAGE.csv`: sixteen source-to-target blocks with French lines and distinct printed/physical/running page fields.
- `FORMULA_SYMBOL_NOTE_STRUCTURE_COMPARISON.csv`: thirty critical formula, symbol, note, sequence, and structure checks.
- `TERMINOLOGY_NORMALIZATION_ADVERSE_CHOICES.csv`: twenty accepted conventions, adverse deltas, and rejected alternatives.
- `BUILD_RENDER_EVIDENCE.csv`: final TeX/PDF, sanitized logs, PDF/font reports, target renders, local-only source renders, and gates.
- `INDEPENDENT_PACKAGE_REVIEW.csv`: seventeen independent cumulative audit checks.

`STRUCTURAL_INDEX.jsonl` is a closed root-to-six-component hierarchy. Each line is one JSON object with `record_id`, `stable_id`, revision links, parent/child/cross-reference links, all three source page coordinate systems, target locator, status, cursor, and closure ID.

`DIFFICULTY_REVISION_LEDGER.jsonl` records review-state correction and remaining publication/rights/metadata decisions. Each object has `event_id`, `stable_id`, `record_revision`, reciprocal `supersedes`/`closed_by` links where revised, source/target locators, resolution, residual risk, status, confidence, continuation cursor, revisit condition, and closure ID.

Authority order is strict: corrected French TeX controls translation; direct French PDF controls page and visual readings; jcreinhold `e7a259f` is one comparison lineage only. Source-page PNGs and raw local logs are local-only and excluded from the proposed public payload.
