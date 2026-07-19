# Artifact Tool machine-ledger QA

All five substantive CSV ledgers were imported with the Artifact Tool,
inspected, and rendered as stable-ID previews after independent-review
revision rows were added.

- 4 authority rows / 12 columns
- 11 source-alignment rows / 20 columns
- 12 formula-symbol-note-structure rows / 21 columns
- 12 terminology/adverse-choice rows / 17 columns
- 5 source-defect/emendation-state rows / 15 columns

All five imports report `inspect_ok=true`. All 44 primary IDs are unique,
visible in the rendered previews, and free of spreadsheet formula triggers.
The five-record NDJSON receipt SHA-256 is
`744ADB7FCADBB1664277C03B2A2A827BDC03182ADEABE520889E42652E201416`.

The final independent machine pass must also validate CSV rectangularity,
record-ID uniqueness, JSONL parsing, parent/reference closure, and reciprocal
revision links.
