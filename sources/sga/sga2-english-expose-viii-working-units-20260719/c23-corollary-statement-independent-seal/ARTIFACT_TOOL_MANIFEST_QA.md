# Artifact Tool ledger QA - SGA2-VIII-C23

Artifact Tool `Workbook.fromCSV` imported the four substantive CSV ledgers and
the final self-excluding `UNIT_HASHES.csv`. Region inspection and full-sheet
rendering were run for each file.

| CSV | Data rows | Columns | Result |
|---|---:|---:|---|
| `AUTHORITY_ARTIFACT_HASHES.csv` | 4 | 12 | Pass |
| `SOURCE_ALIGNMENT_COVERAGE.csv` | 10 | 20 | Pass |
| `FORMULA_SYMBOL_NOTE_STRUCTURE_COMPARISON.csv` | 12 | 21 | Pass |
| `TERMINOLOGY_NORMALIZATION_ADVERSE_CHOICES.csv` | 12 | 17 | Pass |
| `UNIT_HASHES.csv` | 21 | 6 | Pass |

Direct machine validation separately confirms rectangularity, unique primary
IDs, zero formula-leading cells, JSONL reference closure, and exact manifest
hashes. Artifact Tool is a second CSV parser and rendering check, not source
authority.

