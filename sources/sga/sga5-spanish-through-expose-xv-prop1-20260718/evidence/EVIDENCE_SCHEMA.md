# SGA 5 Spanish working evidence

This directory records reproducible evidence for the growing Spanish workpass. It is not a claim that the whole volume is complete.

- `SOURCE_MANIFEST.csv` freezes the authority chain and its rights/status constraints.
- `UNIT_PARITY.csv` records source spans, production units, review state, and unit-specific bilingual evidence.
- `UNIT_HASHES_CURRENT.csv` is regenerated from the parity ledger. A source-unit hash covers the inclusive French line span joined with LF and terminated by one LF; a target-unit hash covers the raw target file.
- `TARGET_DOCUMENT_CURRENT.json` hashes the recursively expanded master after normalizing all TeX input text to LF and encoding it as UTF-8 without a BOM. This binds every unit in master input order.
- `BUILD_CURRENT.json` binds the clean `latexmk` PDF/log/FLS to that expanded-target hash and fails on warnings, box diagnostics, missing glyphs, undefined commands, or fatal errors.
- `VISUAL_QA_WORKING.csv` binds inspected working renders to an exact PDF and expanded-target hash. Final-volume visual certification will be regenerated against the frozen complete PDF.

Run `build.ps1` from the workspace root to regenerate hash and build evidence.
