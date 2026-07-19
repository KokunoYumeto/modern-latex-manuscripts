# Artifact Tool ledger QA - independent seal

Artifact Tool 2.8.6+ imported the four final substantive evidence CSVs and the
final `UNIT_HASHES.csv` as CSV workbooks. Compact workbook/table inspection
returned the following exact record/column counts:

- authority/control hashes: 4 records / 12 columns;
- formula, symbol, note, and structure comparison: 13 / 21;
- source alignment and coverage: 14 / 20;
- terminology, normalization, and adverse choices: 13 / 17; and
- exact self-excluding unit manifest: 33 / 6.

Every import completed without an Artifact Tool error. The full table and its
primary-ID column were rendered for each CSV. The generated previews and
NDJSON receipt live under `_artifact_tool_csv_previews` as local QA support;
they are not proposed public artifacts and are excluded from `UNIT_HASHES.csv`.

Status: final Artifact Tool import, inspection, and render pass.
