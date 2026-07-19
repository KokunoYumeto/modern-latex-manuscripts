# Machine-readable evidence schema - SGA2-VIII-C23-POC

Unit stable ID: `SGA2-VIII-C23-POC`. Continuation cursor: French source line
2715 after blank line 2714.

The four substantive CSV ledgers are UTF-8 rectangular tables. Each row has a
stable unique primary ID, unit ID, authority role, source and target locators,
status, confidence, revision, cursor, and revisit trigger. Parsed cell values
must not begin with an Excel formula sigil (`=`, `+`, `-`, or `@`).

`STRUCTURAL_INDEX.jsonl` uses `record_id = stable_id@record_revision`.
Internal parent, child, cross-reference, revision, supersession, and closure
links must resolve. External links are explicitly prefixed `INBOUND:`,
`OUTBOUND:`, or `COMPARISON:`. Root and QA objects retain append-only revision
histories.

`DIFFICULTY_REVISION_LEDGER.jsonl` uses unique event IDs and stable object IDs
shared with the structural ledger. A revision names the exact prior event in
`supersedes`; the prior event reciprocally names its closer in `closed_by`.

Validation requires exact authority hashes, rectangular and formula-safe CSV,
unique primary IDs, JSONL parse and reference closure, exact page distinctions,
clean two-pass build, source/target 300 and 600 dpi review, extraction, font and
destination checks, privacy scan, and an exact self-excluding SHA-256 manifest.
The final root and QA revisions close the self-gate with independent structure,
formula, note, boundary, build, render, and machine evidence. `UNIT_HASHES.csv`
and `MACHINE_READABLE_VALIDATION.json` are excluded from the manifest rows to
avoid hash cycles; handoff cardinality is manifest rows plus those two files.
