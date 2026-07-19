# Artifact Tool manifest QA

All four substantive CSV ledgers and the exact `UNIT_HASHES.csv` manifest are
imported with Artifact Tool as worksheets and inspected as bounded rectangular
ranges. The substantive ledgers contain 8 plus 13 plus 12 plus 3 records, or 36
records total. The exact manifest contains 30 rows. Primary IDs are populated
and unique; no imported cell is a formula.

Strict byte-level validation independently checks declared headers, CSV
rectangularity, formula-injection safety, authority bytes and SHA-256, JSONL
parse and duplicate keys, structural and revision reference closure, privacy,
and exact manifest closure.
