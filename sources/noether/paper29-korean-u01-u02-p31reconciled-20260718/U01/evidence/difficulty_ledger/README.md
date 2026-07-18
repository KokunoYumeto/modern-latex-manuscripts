# P29 Korean U01 append-only difficulty ledger

`DIFFICULTY_LEDGER.jsonl` is the canonical append-only ledger. Every line has a stable issue ID, an integer sequence, a SHA-256 of its canonical record content (all fields except `record_sha256`), and the preceding record hash. This makes silent edits or reordering detectable. A correction must be a new later line that names the prior issue in `supersedes`; historical failed and rejected approaches remain present.

`DIFFICULTY_LEDGER.csv` is a generated review projection. `DIFFICULTY_LEDGER_METADATA.json` records the expected ordered IDs, state counts, head hash, and canonical JSONL hash. Neither projection is the append authority.

`initialize_difficulty_ledger.py` creates the seven initial records only when no canonical ledger exists; it refuses to overwrite. `project_difficulty_ledger.py` may be rerun after a legitimate append because it changes only projections and metadata. `validate_difficulty_ledger.py` applies the JSON Schema, checks the hash chain, structural links, exact CSV projection, metadata, current-file hashes, held-item revisit conditions, the LF-normalized source-prefix computation, and preservation of the three rejected draft hashes from the semantic fidelity repair.

The ledger distinguishes observed evidence from editorial inference in each `cause` object and explicitly says whether any external/human validation exists. A resolved build or visual workaround is not a terminology or rights clearance.
