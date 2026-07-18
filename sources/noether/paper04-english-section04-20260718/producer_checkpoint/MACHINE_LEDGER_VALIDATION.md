# Machine-readable ledger validation

Validation was performed against the declared CSV and JSONL schemas and the standing machine-ledger requirement.

CSV evidence:

- `SOURCE_ALIGNMENT.csv`: 10 rows, including one append-only revision; 9 active alignments.
- `SOURCE_CONTROL_HASHES.csv`: 6 control receipts.
- `SOURCE_FORMULA_NOTE_COMPARISON.csv`: 17 rows, including one append-only revision; 16 active comparisons.
- `TERMINOLOGY_AND_REJECTED_CHOICES.csv`: 13 terminology decisions.
- `ADVERSE_WITNESS_COMPARISON.csv`: 6 adverse decisions.

Every CSV decodes as UTF-8, is rectangular, matches its declared header, has unique `(primary_id, record_revision)` keys, has valid revision links, and contains zero formula-injection trigger cells.

JSONL evidence:

- `STRUCTURAL_INDEX.jsonl`: 11 records resolving to 9 active stable units.
- `DIFFICULTY_AND_FAILURE_LEDGER.jsonl`: 7 records resolving to 6 active stable issues.

Every JSONL line decodes as exactly one JSON object with zero duplicate object keys. Composite IDs and revision links are unique and valid. Active parent/child relations are symmetric, all package-local unit references resolve, alignment units resolve to active structural units, issue closure links resolve backward, and the continuation cursor resolves to excluded section 5. Active candidate artifact receipts match exact package-relative paths, byte counts, and SHA-256 values.

Result: PASS with zero parse, schema, revision, hierarchy, closure, artifact-receipt, or bounded-coverage failures. Exact current hashes for every ledger are in `SHA256SUMS.csv` and `ZENODO_PAYLOAD_MANIFEST.csv`.
