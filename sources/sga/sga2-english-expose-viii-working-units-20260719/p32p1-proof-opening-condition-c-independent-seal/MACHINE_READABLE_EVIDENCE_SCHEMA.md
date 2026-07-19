# Machine-readable evidence schema

Unit stable ID: `SGA2-VIII-P32P1`.

The five substantive CSV ledgers use the first column as a unique primary ID.
Every CSV must parse as UTF-8, have the exact header width, remain rectangular,
and contain no spreadsheet formula-trigger cell (`=`, `+`, `-`, or `@` after
leading spaces). `ZENODO_PAYLOAD_MANIFEST.csv` and `UNIT_HASHES.csv` are
manifest controls and follow the same rectangularity and formula-safety rule.

`STRUCTURAL_INDEX.jsonl` is the hierarchy. Each `record_id` is unique; all
local parent, child, and cross-reference IDs must resolve. Identifiers beginning
`OUTBOUND:` are explicit external dependencies or continuation targets.

`DIFFICULTY_REVISION_LEDGER.jsonl` is append-only. Revisions sharing a
`stable_id` must have distinct revision numbers and reciprocal `supersedes` /
`superseded_by` links when both records are local. Terminal records state
production review only and may not claim an independent seal.

Continuation cursor: corrected French line 2909, the implication
`(a) => (b)`. Blank line 2908 is excluded.
