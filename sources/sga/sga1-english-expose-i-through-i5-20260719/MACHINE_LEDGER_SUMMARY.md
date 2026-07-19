# Machine-readable evidence summary

The excluded local working gate validated 189 CSV rows and 68 unique JSONL
records with zero failures. The included public projection contains 14 CSV
files with 252 rows and four JSONL files with 55 records. Public projections
retain stable IDs, source/target locators, statuses, adverse choices, revision
links, and the exact continuation cursor.

Section I.5 contributes:

- 13 source-comparison rows;
- 13 formula/structure rows;
- 12 adverse/rejected-choice rows;
- 9 normalization-delta rows;
- 3 index-restoration-debt rows;
- 13 hierarchical evidence-graph records;
- 11 difficulty/failure/revision records, including the final verification
  record and the two excluded historical build states.

CSV controls must remain rectangular, have unique primary IDs, and be safe
against spreadsheet formula injection. JSONL controls must parse one object per
line, satisfy the included schema, have unique IDs, close every local
reference, preserve parent-child reciprocity, and match each included target's
bytes and SHA-256. The package verifier reruns these checks.
