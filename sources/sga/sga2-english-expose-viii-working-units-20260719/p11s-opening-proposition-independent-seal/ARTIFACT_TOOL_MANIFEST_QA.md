# Artifact Tool manifest QA

All four final substantive CSV ledgers and the exact `UNIT_HASHES.csv` manifest
were imported with Artifact Tool as worksheets and inspected as bounded
rectangular ranges. The substantive ledgers contain 7 plus 11 plus 10 plus 3
records or 31 records total. The exact independent-seal manifest contains 25
rows. Primary IDs are populated and unique; no imported cell is a formula.

Strict byte-level validation independently checks the declared headers, CSV
rectangularity, formula-injection safety, authority bytes and SHA-256, JSONL
parse and duplicate keys, structural and revision reference closure, privacy,
and the exact manifest. All gates pass for the bounded independent seal.
