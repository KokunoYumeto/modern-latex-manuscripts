# Append-only difficulty ledger contract

DIFFICULTY_LEDGER.jsonl is authoritative and append-only. Existing records must never be rewritten to correct later understanding; corrections and supersessions are new records. Every record stores the previous record hash and its own hash.

Record hashing rule: serialize the record as one compact JSON line with record_sha256 set to null, hash those UTF-8 bytes with SHA-256, then place the uppercase digest in record_sha256. The next record copies that digest into previous_record_sha256.

The initializer refuses to run when the ledger already exists. The append utility adds one new record and does not rewrite prior lines. The CSV is only a replaceable projection of the immutable JSONL. The validator checks chain hashes, IDs, required evidence distinctions, structural references, state, and CSV row count.

This initial P07 ledger records actual hard controls and terminology risks. No P07 target-write or tool failure occurred before initialization, so no failure event or failed-file hash was invented. Lack of an independent review is preserved as adverse evidence, not mistaken for validation.
