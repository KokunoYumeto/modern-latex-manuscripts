# Artifact Tool machine-ledger QA

All five CSV ledgers were imported with the Artifact Tool, inspected, and
rendered as stable-ID previews after formula-safety and rectangularity checks.

- 4 authority rows / 12 columns
- 10 alignment rows / 20 columns
- 9 formula-symbol-note-structure rows / 21 columns
- 11 terminology/adverse-choice rows / 17 columns
- 1 source-defect/emendation-state row / 15 columns

All five imports report `inspect_ok=true`; all 35 primary IDs are visible,
unique, unclipped in the final previews, and free of spreadsheet formula
triggers. The five-record NDJSON receipt SHA-256 is
`74B574F791E3EF88AB8244FCB7B5BB8088386631EF6EB157C1232D02B2A32AC1`.

The substantive ledgers passed independent review; the one-row source-defect
state added during final manifest preparation is covered by the final
exact-set/machine gate.
