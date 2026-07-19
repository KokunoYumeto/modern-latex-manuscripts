# Machine-readable evidence schema - SGA2-VIII-L24

Unit stable ID: `SGA2-VIII-L24`.

- Raw TeX cursor: French line 2723, equation-counter reset after blank 2722.
- Substantive prose cursor: French line 2725 after blank line 2724.

The compact `continuation_cursor` field in every CSV/JSONL record carries both
values in that order. Structural and difficulty JSONL records additionally
carry separate `raw_tex_cursor` and `substantive_prose_cursor` keys.

The four substantive CSV ledgers are UTF-8 rectangular tables. Each row has a
stable unique primary ID, unit ID, authority role, source and target locators,
status, confidence, revision, cursor, and revisit trigger. Parsed cell values
must not begin with an Excel formula sigil (`=`, `+`, `-`, or `@`).

`STRUCTURAL_INDEX.jsonl` uses `record_id = stable_id@record_revision`.
Internal parent, child, cross-reference, revision, supersession, and closure
links must resolve. External links are explicitly prefixed `INBOUND:`,
`OUTBOUND:`, or `COMPARISON:`.

`DIFFICULTY_REVISION_LEDGER.jsonl` uses unique event IDs and stable object IDs
shared with the structural ledger. A revision names the exact prior event in
`supersedes`; the prior event reciprocally names its closer in `closed_by`.

Validation requires exact authority hashes, rectangular and formula-safe CSV,
unique primary IDs, JSONL parse and reference closure, exact page/cursor
distinctions, clean two-pass build, source/target 300 and 600 dpi review,
extraction, font and destination checks, privacy scan, and an exact
self-excluding SHA-256 manifest.
