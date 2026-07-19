# Artifact Tool manifest QA

The four substantive CSV ledgers contain 44 data rows: 3 authority artifacts,
11 source-alignment records, 17 formula/symbol/structure comparisons, and 13
terminology/adverse-choice decisions. The exact artifact manifest contains 21
additional rows, for 65 CSV data rows overall.

All CSVs were imported over their complete used ranges and reconciled with
strict UTF-8 parsing. Rectangularity, stable-ID uniqueness, formula-injection
safety, exact path/hash/byte agreement, and required-field checks passed.

Status: machine-readable manifest self-QA passed; independent review remains
pending.
