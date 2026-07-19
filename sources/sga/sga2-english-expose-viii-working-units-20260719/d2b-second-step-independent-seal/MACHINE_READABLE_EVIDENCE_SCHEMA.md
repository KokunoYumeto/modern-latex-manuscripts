# Machine-readable evidence schema

Unit namespace: `SGA2-VIII-D2B`.

CSV primary IDs are the first column in each ledger. Every CSV must be
RFC-4180-readable, rectangular, primary-ID unique, and spreadsheet
formula-trigger safe. Source, printed-page, physical-PDF-page, and running-page
locators are separate fields. Status values distinguish source authority,
corrected branch, comparison-only evidence, source oddity, and review state.

JSONL uses `schema_version`, `record_id`, `stable_id`, `record_revision`,
`supersedes`, and `superseded_by`. Stable IDs persist across revisions;
record IDs and stable-ID/revision pairs are unique. Parent, child, unit, and
cross-reference targets must close unless explicitly prefixed as outbound or
comparison edges. Revision chains must be reciprocal and contiguous.

The public hash inventory is self-excluding and must prove exact-set closure.
The independent seal is expressed by new revision records; earlier pending
states remain visible as superseded history. This schema does not turn the
bounded unit into a complete Exposé VIII or complete SGA2 volume.
