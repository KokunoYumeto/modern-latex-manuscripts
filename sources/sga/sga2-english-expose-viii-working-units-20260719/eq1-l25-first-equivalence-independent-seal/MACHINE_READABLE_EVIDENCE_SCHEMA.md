# Machine-readable evidence schema

Unit namespace: `SGA2-VIII-EQ1-L25`.

CSV primary IDs are the first column in each ledger. Every CSV must be
RFC-4180-readable, rectangular, primary-ID unique, and spreadsheet
formula-trigger safe. Source, printed-page, physical-PDF-page, and running-page
locators are separate fields. Status values distinguish production self-gate,
independent review, comparison-only evidence, normalization, and source-branch
disposition.

JSONL uses `schema_version`, `record_id`, `stable_id`, `record_revision`,
`supersedes`, and `superseded_by`. A stable ID persists across revisions;
`record_id` is the unique `stable_id@record_revision` identity. Structural records identify parents,
children or cross-references, source lines, state, and continuation cursor.
Difficulty records bind through `unit_id`. Record IDs and stable-ID/revision
pairs must be unique; supersession chains must be reciprocal and contiguous.
Parent, unit, child, and cross-reference targets must close inside the
two JSONL ledgers unless explicitly prefixed as an inbound, outbound, or
comparison edge.

The final public-file hash inventory will be self-excluding: `UNIT_HASHES.csv`
will list every proposed public file except itself. `ZENODO_PAYLOAD_MANIFEST.csv`
will describe the same proposed public set except the two manifest files, which
avoids self-hash recursion. Exact-set validation must prove these relationships.
