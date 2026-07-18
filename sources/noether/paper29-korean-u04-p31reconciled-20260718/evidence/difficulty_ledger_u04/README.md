# P29-KO-U04 append-only difficulty ledger

`DIFFICULTY_LEDGER.jsonl` is the canonical immutable hash-chained record of hard units, failed paths, corrections, and residual risks for U04. `DIFFICULTY_LEDGER.csv` is a generated projection. `DIFFICULTY_LEDGER.schema.json` documents the record contract. `initialize_difficulty_ledger.py` refuses to overwrite a non-identical prefix; future corrections must append a new chained record rather than rewriting history. `project_difficulty_ledger.py` rebuilds projection and metadata, and `validate_difficulty_ledger.py` verifies schema, IDs, evidence classifications, structural links, the complete SHA-256 chain, and projection parity.

The ledger deliberately retains resolved problems: unit-boundary choice, historical-term traps, generic-to-specialized parameter order, printed page-break hyphenation, a draft-only underfull box, and the authority validator's first false failure. Internal checks are not external or human review.
