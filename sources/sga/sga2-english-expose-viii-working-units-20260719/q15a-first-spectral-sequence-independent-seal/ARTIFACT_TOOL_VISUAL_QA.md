# Artifact Tool visual QA

`@oai/artifact-tool` imported, inspected, and rendered every CSV evidence
table. Five full-table previews and five stable-ID previews were visually
inspected at original resolution.

- `SOURCE_ALIGNMENT_COVERAGE.csv`: 12 data rows and 20 columns.
- `FORMULA_SYMBOL_NOTE_STRUCTURE_COMPARISON.csv`: 17 data rows and 21 columns.
- `TERMINOLOGY_NORMALIZATION_ADVERSE_CHOICES.csv`: 17 data rows and 17 columns.
- `AUTHORITY_ARTIFACT_HASHES.csv`: 4 data rows and 12 columns.
- `UNIT_HASHES.csv`: 31 data rows and 12 columns after the final manifest
  refresh.

Every preview has a nonblank header, populated stable-ID column, consistent
row alignment, and visible continuation/review-state fields. No blank sheet,
shifted cell, formula artifact, or missing primary ID was observed. Exact
preview and receipt hashes are recorded by the final machine validator.

Status: Artifact Tool import/inspect/render and self plus independent ledger
visual gates pass for this bounded unit.
