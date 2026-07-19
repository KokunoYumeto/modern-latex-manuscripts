# Machine-ledger summary

- Schema: `sga1_public_machine_ledgers.v5`.
- CSV: 23 files / 400 data rows; strict UTF-8, declared headers,
  rectangularity, unique nonblank stable IDs, and formula safety pass.
- JSONL: 10 files / 145 records; parse, required fields, allowed statuses,
  unique IDs, reference closure, parent-child reciprocity, supersession,
  closure, and target bytes/SHA-256 pass.
- Terminal JSONL states: 122 `closed_corrected`, 18 `rejected`, 5
  `superseded`.
- Continuation cursor: French line 1654, excluded.
- Artifact-tool CSV gate: 23 files / 400 rows / zero failures, with imported
  tables, first/last-row inspection, formula-error scan, and rendered previews.

The separate I.8 adverse, terminology, authority/coverage, source-comparison,
and formula ledgers avoid mutating the immutable r10 cumulative ledgers. Prior
JSONL decisions that targeted the r10 driver/reader are bound to immutable
predecessor copies in `evidence/prior_checkpoint`, preventing silent target
hash drift when this cumulative successor replaces the current driver/PDF.