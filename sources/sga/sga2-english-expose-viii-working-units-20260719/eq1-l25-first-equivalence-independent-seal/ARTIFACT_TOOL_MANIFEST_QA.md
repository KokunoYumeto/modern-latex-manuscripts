# Artifact Tool machine-ledger QA

All five CSV ledgers were imported with the Artifact Tool, inspected, and
rendered as stable-ID previews after formula-safety and rectangularity checks.

- 4 authority rows / 12 columns;
- 13 alignment rows / 20 columns;
- 12 formula-symbol-note-structure rows / 21 columns;
- 12 terminology/adverse-choice rows / 17 columns;
- 4 source-defect/emendation rows / 15 columns.

All five imports report `inspect_ok=true`; all 45 primary IDs are visible,
unique, unclipped in the five final previews, and free of spreadsheet formula
triggers. The five-record NDJSON receipt has SHA-256
`8B26346A130218CFEFC58CD85CD09E6871F4E99A56373480AEFB80CDC9308C8F`.

The rendered previews are QA evidence for the stable-ID column. They do not
replace the rectangularity, formula-safety, reference-closure, or source audit.
