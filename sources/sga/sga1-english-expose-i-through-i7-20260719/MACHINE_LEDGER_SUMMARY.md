# Machine-readable evidence summary

The excluded local pre-freeze gate validates 284 CSV rows and 132 unique JSONL records with zero failures. Its r10 receipt is 26,199 bytes, SHA-256 `D49F4C115E21897DC98E692855643262644959BE57FA609175E758919639B5E0`. The included public-safe projection contains 18 CSV files with 344 rows and eight JSONL files with 118 records: 98 closed/corrected, 15 rejected, and five superseded.

Section I.7 adds 15 source-comparison rows, 17 formula/structure rows, 13 adverse/rejected-choice rows, 11 normalization rows, one index-debt row, six authority/coverage rows, 24 hierarchy records, 27 difficulty/revision/failure records, and the two historical coverage-revision records needed for reference closure. Stable source and target locators, statuses, adverse choices, supersession/revision links, and the excluded cursor at line 1493 are retained. Private paths and excluded artifacts are removed or represented by size/hash-only historical locators.

The expected public JSONL status distribution is 98 `closed_corrected`, 15 `rejected`, and five `superseded` records. CSV controls must remain rectangular, have unique primary IDs, and be safe against spreadsheet formula injection. JSONL controls must parse one object per line, satisfy the included v4 public schema, have unique IDs, close every local reference, preserve reciprocal parent/child, supersession, and closure links, and resolve every declared target by exact bytes and SHA-256. `ledgers/PUBLIC_MACHINE_VALIDATION_I_7.txt` records the freeze-time result.

The public projections are evidence controls, not source authority, publication proof, or mathematical certification.
