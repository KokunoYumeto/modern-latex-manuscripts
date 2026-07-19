# Machine-readable evidence schema

Unit stable ID: `SGA2-VIII-APP31`.

The five CSV files use the first column as a unique primary ID. All rows must
parse as UTF-8, have the exact header width, remain rectangular, and contain no
spreadsheet formula-trigger cell (`=`, `+`, `-`, or `@` after leading spaces).

`STRUCTURAL_INDEX.jsonl` is an append-only hierarchy. `record_id` is unique;
`stable_id` may recur only across explicit revisions linked by `supersedes` and
`superseded_by`. Every local parent, child, and cross-reference must resolve.
Identifiers beginning `OUTBOUND:` are intentionally external dependencies.

`DIFFICULTY_REVISION_LEDGER.jsonl` is append-only evidence for source-branch,
page-system, glyph-normalization, marker, comparison, build, render, and later
revision states. No current record may claim an independent seal.

Continuation cursor: corrected French line 2888, Proposition 3.2. Blank line
2887 is excluded from the translated body.
