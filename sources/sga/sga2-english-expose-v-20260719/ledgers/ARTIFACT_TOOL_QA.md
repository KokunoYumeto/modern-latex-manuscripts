# Artifact Tool QA — SGA 2 Exposé V independently audited checkpoint

Status: **PASS after independent package audit.**

All seven current CSVs were independently parsed with Workbook.fromCSV, inspected across their complete used ranges with values and formulas included, and rendered as bounded header-plus-first-25-record previews at scale 0.5. Every preview was inspected at original rendered resolution. Long fields are intentionally abbreviated only in previews; complete programmatic inspections cover every cell.

| CSV | Records | Columns | Full range | Preview range | Preview SHA-256 |
|---|---:|---:|---|---|---|
| SOURCE_ALIGNMENT_COVERAGE.csv | 139 | 23 | A1:W140 | A1:W26 | BD7072482C1391E8D1418356EBF8910B7E6E93D38A0B3816A45B2CED6B4C7E45 |
| FORMULA_SYMBOL_NOTE_STRUCTURE_COMPARISON.csv | 211 | 25 | A1:Y212 | A1:Y26 | 1E06086B944EFEBBC48F97F6942B0CDA0190EF1A0FC7847FFDF8B9A14BECD8E0 |
| TERMINOLOGY_NORMALIZATION_ADVERSE_CHOICES.csv | 173 | 27 | A1:AA174 | A1:AA26 | 0DED979E4E4D92A2E13F41E779BC03926923BDF2ED02EDF3CB12E130787D0862 |
| AUTHORITY_ARTIFACT_HASHES.csv | 3 | 14 | A1:N4 | A1:N4 | 5FB33089BBE079BD3B53494B1E45B6D899A2C46A41A1EC39D6A9497E6CF3A626 |
| COMPONENT_UNIT_INTEGRATION.csv | 14 | 25 | A1:Y15 | A1:Y15 | AA3157B0AE54F133657162BDDEA233956916A982A128A6D959B0F1136DF21EE5 |
| BUILD_RENDER_EVIDENCE.csv | 28 | 18 | A1:R29 | A1:R26 | 3E2F19E4B7DD24629FB5F6AD77BFBBEDE301BF4F0C0F98E4457E586ADA6411B6 |
| INDEPENDENT_PACKAGE_REVIEW.csv | 17 | 18 | A1:R18 | A1:R18 | 8951A160D181FB5E3075FB1BCEED92C6BF2CD2F673016099EF73D8551AF27427 |

The six cumulative evidence ledgers contain 568 records; INDEPENDENT_PACKAGE_REVIEW.csv adds 17 audit records. All seven are UTF-8 without BOM, rectangular, unique on their declared primary IDs, and free of unescaped spreadsheet-formula trigger cells.
