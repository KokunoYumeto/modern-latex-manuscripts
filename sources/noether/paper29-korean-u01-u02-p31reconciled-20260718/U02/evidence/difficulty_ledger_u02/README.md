# P29 Korean U02 append-only difficulty ledger

`DIFFICULTY_LEDGER.jsonl` is the canonical append-only SHA-256 chain; CSV and metadata are generated projections. Each record hash covers canonical sorted-key JSON excluding `record_sha256`, and each line names the preceding record hash. Corrections append new IDs and cite `supersedes`.

The initial chain preserves the exact U02 source/cursor boundary, the stranded-footnote repair (including an explicit unavailable-hash record for the overwritten pre-hash state), the nearly blank second German control page and compacting repair, the independently reviewed Korean intermediate hashes and final refinements, unresolved Korean historical terminology evidence debt, and the non-one-to-one inline-source/display-target structural mapping.

`initialize_difficulty_ledger.py` refuses to overwrite an existing chain. `project_difficulty_ledger.py` regenerates only CSV and metadata after legitimate appends. `validate_difficulty_ledger.py` applies the JSON Schema, verifies the chain and structural links, recomputes all current-file hashes, checks historical/unavailable evidence syntax, reproduces the line-41 cursor and display/note parity, checks the superseded PDF/render/target hash sets, verifies zero target build-warning patterns, and compares the CSV exactly with the JSONL.
