# SGA 1 §I.7 machine-ledger historical-locator correction

Date: 2026-07-19

Scope: machine-evidence maintenance only. No French source, English translation, formula, TeX, PDF, build, or rendered page changed.

The first final §I.7 validator run correctly failed two target checks. The historical records `SGA1-COVERAGE-REV-0002` and `SGA1-I4-PUBLIC-FAIL-0001` retained the byte counts and SHA-256 digests of earlier ledger snapshots but still named the live mutable ledger paths. Both ledgers had subsequently gained source-audited rows, so resolving those historical hashes against their current paths was necessarily false.

Correction applied:

- `SGA1-COVERAGE-REV-0002`: `target_locator.relative_path` changed from `ledgers/CANDIDATE_COVERAGE_V2.csv` to `null`; the historical snapshot remains identified by 5,420 bytes and SHA-256 `97D1ECFCA7067D68DB3889A68EA6A39A66335BA2898101581E19EAFD729997EB`.
- `SGA1-I4-PUBLIC-FAIL-0001`: `target_locator.relative_path` changed from `ledgers/AUTHORITY_AND_PROVENANCE.csv` to `null`; the historical snapshot remains identified by 8,323 bytes and SHA-256 `84C5798F8C5F8F9D1B7E05E1C41DDD55C1D3A235AA6E22EDA949ED7288E287D2`.

Both records are also moved from their obsolete `working_recheck` states to `closed_corrected` and reciprocally linked to the stable correction record `SGA1-I7-HISTORICAL-LOCATOR-CORRECTION-0001`. This records that the V2 migration and the public-safe projection control were actually validated in later checkpoints; it does not erase the original findings or rewrite their preserved snapshot hashes.

This matches the existing public-safe projection rule for historical working snapshots: retain exact size/hash evidence while declining to resolve it against a later mutable working file. The current ledgers remain separately declared and fully checked at their current sizes and hashes.

The rejected validator receipt is preserved as `machine_ledgers/MACHINE_LEDGER_VALIDATION_I_7_PRE_LOCATOR_FIX_20260719.txt` (24,135 bytes; SHA-256 `FEFCC1D623C678CC3EFB3AECF64CCF8DF32EC0279FDFF93C8BB6589487133CBC`). Its only failures are the two stale mutable-path resolutions above.

The first post-correction parse/target pass produced a 61-record difficulty/revision ledger of 106,100 bytes and SHA-256 `AA31F2A6CB86F92B47D307BFC005061DD70767352FDBDF848A9AA99610A6AB95`, with zero failures. A stable correction record is appended after this receipt and the final validator is rerun; therefore that intermediate ledger hash is evidence of the locator-edit state, not the final §I.7 ledger hash.
