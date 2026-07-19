# Artifact Tool machine-ledger QA

All five substantive CSV ledgers were imported with the Artifact Tool,
inspected, and rendered as stable-ID previews after the independent-review
revision rows were added.

- 4 authority rows / 12 columns
- 10 source-alignment rows / 20 columns
- 10 formula-symbol-note-structure rows / 21 columns
- 11 terminology/adverse-choice rows / 17 columns
- 6 source-defect/emendation-state rows / 15 columns

All five imports report `inspect_ok=true`. All 41 primary IDs are visible,
unique, unclipped in the rendered previews, and free of spreadsheet formula
triggers. The five-record NDJSON receipt SHA-256 is
`52A0D258AA16DEAC43F833F631E929D3258F680D7C9227B6DD847558C3068B4A`.

The final independent machine pass also validates CSV rectangularity,
record-ID uniqueness, JSONL parsing, reference closure, and reciprocal
revision links.
