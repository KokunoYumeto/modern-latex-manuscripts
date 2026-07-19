# Machine-readable evidence schema

Unit namespace: `SGA2-VIII-P2-SETUP`.

CSV primary IDs are the first column in each ledger. Every CSV must be
RFC-4180-readable, rectangular, primary-ID unique, and spreadsheet
formula-trigger safe. Source, printed-page, physical-PDF-page, and running-page
locators are separate fields. Status values distinguish production self-gate,
independent review, comparison-only evidence, typography normalization, and
source-defect disposition.

JSONL uses `schema_version`, `record_id`, `stable_id`, `record_revision`,
`supersedes`, and `superseded_by`. Structural records additionally identify
parents, children or cross-references, source lines, state, and continuation
cursor. Difficulty records bind through `unit_id`. All record IDs and stable
IDs must be unique; parent, unit, child, and cross-reference targets must close
inside the two JSONL ledgers unless explicitly prefixed as an inbound,
outbound, or comparison edge.

The final public-file hash inventory is self-excluding: `UNIT_HASHES.csv`
lists every proposed public file except itself. `ZENODO_PAYLOAD_MANIFEST.csv`
describes the same proposed public set except the two manifest files, avoiding
self-hash recursion. Exact-set validation must prove these relationships.
