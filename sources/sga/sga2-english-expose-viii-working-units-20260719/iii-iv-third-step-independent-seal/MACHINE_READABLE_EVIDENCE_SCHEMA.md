# Machine-readable evidence schema

Unit namespace: `SGA2-VIII-III-IV`.

CSV primary IDs are the first column in each ledger. Every CSV must be
RFC-4180-readable, rectangular, primary-ID unique, and spreadsheet
formula-trigger safe. Corrected French lines, printed pages, physical PDF
pages, running pages, source markers, and the continuation cursor occupy
separate fields.

JSONL uses `schema_version`, `record_id`, `stable_id`, `record_revision`,
`supersedes`, and `superseded_by`. Stable IDs persist across revisions.
Parent, child, unit, cross-reference, and outbound-label edges must close or
carry an explicit `OUTBOUND:` prefix. Revision chains must be reciprocal and
contiguous.

The independent seal is expressed by new revision records; earlier pending
states remain visible as superseded history. The public hash inventory is
self-excluding and must prove exact-set closure. This schema does not turn the
bounded unit into a complete Exposé VIII or complete SGA2 volume.
