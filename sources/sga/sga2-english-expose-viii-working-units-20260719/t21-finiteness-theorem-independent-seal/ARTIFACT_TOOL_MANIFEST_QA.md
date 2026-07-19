# Artifact Tool final ledger QA - SGA2-VIII-T21

Artifact Tool `Workbook.fromCSV` imported the four substantive CSV ledgers and
the independently sealed `UNIT_HASHES.csv`. Region inspection and full-sheet
rendering were run for each file after the independent review records and
evidence were frozen.

| CSV | Data rows | Columns | Result |
|---|---:|---:|---|
| `AUTHORITY_ARTIFACT_HASHES.csv` | 4 | 12 | Pass |
| `SOURCE_ALIGNMENT_COVERAGE.csv` | 10 | 20 | Pass |
| `FORMULA_SYMBOL_NOTE_STRUCTURE_COMPARISON.csv` | 8 | 21 | Pass |
| `TERMINOLOGY_NORMALIZATION_ADVERSE_CHOICES.csv` | 10 | 17 | Pass |
| `UNIT_HASHES.csv` | 34 | 6 | Pass |

Independent machine validation confirms rectangularity, unique primary IDs,
zero formula-leading cells, and exact manifest hashes for all 34 proposed
members. Artifact Tool is a second CSV parser/rendering check, not source
authority.
