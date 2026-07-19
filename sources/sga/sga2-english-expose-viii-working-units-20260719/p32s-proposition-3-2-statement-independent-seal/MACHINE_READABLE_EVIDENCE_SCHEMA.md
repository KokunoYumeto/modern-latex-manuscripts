# Machine-readable evidence schema

Unit stable ID: `SGA2-VIII-P32S`.

The five CSV files use the first column as a unique primary ID. Every file must
parse as UTF-8, have the exact header width, remain rectangular, and contain no
spreadsheet formula-trigger cell (`=`, `+`, `-`, or `@` after leading spaces).

`STRUCTURAL_INDEX.jsonl` is the hierarchy. Each `record_id` is unique; local
parent, child, and cross-reference IDs must resolve. Identifiers beginning
`OUTBOUND:` are intentional external dependencies.

`DIFFICULTY_REVISION_LEDGER.jsonl` is append-only. Revisions of the same
`stable_id` must link through `supersedes` and `superseded_by`; both referenced
record IDs must exist. The overline reading has an explicit two-record history.
No current record may claim an independent seal.

Continuation cursor: corrected French line 2901, proof of Proposition 3.2.
Blank line 2900 and the proof are excluded from the translated body.
