# Machine-readable evidence summary

The excluded local working gate validated 217 CSV rows and 77 unique JSONL
records with zero failures. Its sealed receipt is 17,181 bytes, SHA-256
`AB341EFB62BC6DFAE98485864FDDD046B8CF8224F541EF060D5A91EA66A16492`.
The included public projection contains 16 CSV
files with 281 rows and six JSONL files with 64 records. Public projections
retain stable IDs, source/target locators, statuses, adverse choices, revision
and supersession links, and the exact continuation cursor.

Section I.6 adds to the sealed opening-through-I.5 projection:

- 7 source-comparison rows;
- 7 formula and structure rows;
- 7 adverse and rejected-choice rows;
- 7 normalization-delta rows;
- 1 authority and coverage row;
- 7 hierarchical evidence-graph records;
- 2 difficulty, revision, and verification records.

The final public JSONL status distribution is 57 `closed_corrected`, 5
`rejected`, and 2 `superseded` records. CSV controls must remain rectangular,
have unique primary IDs, and be safe against spreadsheet formula injection.
JSONL controls must parse one object per line, satisfy the included v3 public
schema, have unique IDs, close every local reference, preserve parent-child,
revision, closure, and supersession reciprocity, and match each included
target's bytes and SHA-256. The portable package verifier reruns these checks
and requires continuation line 1217 to remain excluded.

The promoted I.6 source-comparison input is 4,386 bytes at SHA-256
`097D362D41D57143609DFBEC7DFA11FED3E3EB79381877AF3129CC4F97ABF1FB`;
the formula/structure input is 2,383 bytes at SHA-256
`40B650EE723CA7723BD66EB2A7E469C7ED90A28963904E0B497D121F1559764B`.
The six substantive rows in each public projection use terminal status
`closed_source_checked_independent_pass`; each cursor row remains
`cursor_fixed_independent_pass`.
