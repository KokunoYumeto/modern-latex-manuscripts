# Machine-readable evidence schema

This bounded unit implements the English/Germanic standing ledger requirement identified by SHA-256 `BDD49D7A237D9C17255E05309CC07DAF519D1C59038D83257D57B542235B1F0E`.

## CSV declarations

All CSVs are UTF-8, comma-delimited, quoted, rectangular snapshots. Initial rows use `record_revision=1` and an empty `supersedes_id`. A later correction must append a row with the same primary ID, increment `record_revision`, and set `supersedes_id` to `primary_id@prior_revision`; consumers resolve to the highest valid revision. Primary IDs and declared headers are:

- `SOURCE_ALIGNMENT.csv` — primary ID `alignment_id`; header `alignment_id,record_revision,supersedes_id,evidence_class,unit_id,r823_lines,printed_pages,physical_scan_pages,target_locator,status,confidence,adverse_delta`.
- `SOURCE_CONTROL_HASHES.csv` — primary ID `control_id`; header `control_id,record_revision,supersedes_id,evidence_class,role,locator,sha256,bytes,authority_status,confidence,notes`.
- `SOURCE_FORMULA_NOTE_COMPARISON.csv` — primary ID `comparison_id`; header `comparison_id,record_revision,supersedes_id,evidence_class,object_type,source_locator,printed_page,target_locator,critical_controls,status,confidence,notes`.
- `TERMINOLOGY_AND_REJECTED_CHOICES.csv` — primary ID `term_id`; header `term_id,record_revision,supersedes_id,evidence_class,german,source_locator,adopted_english,target_locator,rejected_choice,decision_reason,status,confidence`.
- `ADVERSE_WITNESS_COMPARISON.csv` — primary ID `adverse_id`; header `adverse_id,record_revision,supersedes_id,evidence_class,source_locator,target_locator,authority_reading,comparison_reading,target_disposition,classification,status,confidence,propagation`.

No cell may begin with `=`, `+`, `-`, or `@`. SHA-256 values are uppercase hexadecimal; byte counts and revisions are positive base-10 integers.

## JSONL declarations

- `STRUCTURAL_INDEX.jsonl` follows `STRUCTURAL_INDEX_SCHEMA.md`; primary ID `unit_id` plus `record_revision`.
- `DIFFICULTY_AND_FAILURE_LEDGER.jsonl` follows `DIFFICULTY_AND_FAILURE_LEDGER_SCHEMA.md`; primary ID `issue_id` plus `record_revision`.

Every nonblank line must decode to exactly one JSON object with no duplicate object keys. Local child, parent, closure, English-scope-resolution, revision, and artifact-receipt links must validate. Source coordinates and target locators must be nonempty. Internal scan renders and raw build logs remain internal.
