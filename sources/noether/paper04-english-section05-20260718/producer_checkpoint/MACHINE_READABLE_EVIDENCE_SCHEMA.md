# Machine-readable evidence schema

This bounded unit implements the English/Germanic standing ledger requirement identified by SHA-256 `BDD49D7A237D9C17255E05309CC07DAF519D1C59038D83257D57B542235B1F0E`.

## CSV declarations

All CSVs are UTF-8, comma-delimited, quoted, and rectangular. Initial rows use `record_revision=1` and an empty `supersedes_id`. A correction appends a row with the same primary ID, the next revision, and `primary_id@prior_revision` in `supersedes_id`. Consumers select the highest valid revision.

- `SOURCE_ALIGNMENT.csv`: primary ID `alignment_id`; 12 declared columns.
- `SOURCE_CONTROL_HASHES.csv`: primary ID `control_id`; 11 declared columns.
- `SOURCE_FORMULA_NOTE_COMPARISON.csv`: primary ID `comparison_id`; 12 declared columns.
- `TERMINOLOGY_AND_REJECTED_CHOICES.csv`: primary ID `term_id`; 12 declared columns.
- `ADVERSE_WITNESS_COMPARISON.csv`: primary ID `adverse_id`; 13 declared columns.

No cell may begin with `=`, `+`, `-`, or `@`. SHA-256 values are uppercase hexadecimal; byte counts and revisions are positive base-10 integers.

`WORKING_UNIT_PRIMARY_ARTIFACT_HASHES.csv` is a final six-column snapshot inventory rather than an append-only evidence ledger. It contains one row for each declared primary working-unit artifact, excludes itself to avoid a self-hash cycle, and must be regenerated whenever any listed artifact changes.

## JSONL declarations

- `STRUCTURAL_INDEX.jsonl` follows `STRUCTURAL_INDEX_SCHEMA.md`; primary ID `unit_id` plus `record_revision`.
- `DIFFICULTY_AND_FAILURE_LEDGER.jsonl` follows `DIFFICULTY_AND_FAILURE_LEDGER_SCHEMA.md`; primary ID `issue_id` plus `record_revision`.

Each nonblank line must decode to exactly one JSON object without duplicate keys. Local child, parent, revision, closure, source-span, continuation-cursor, and artifact-receipt links must validate. Internal print renders and raw build logs remain internal working evidence.
