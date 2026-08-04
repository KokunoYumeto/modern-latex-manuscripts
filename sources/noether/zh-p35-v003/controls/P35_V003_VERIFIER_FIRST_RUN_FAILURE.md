# Paper 35 Chinese v003 producer verifier — first-run failure

- Failure record: `P35_V003_VERIFIER_FIRST_RUN_FAILURE.json`, 18,310 bytes, SHA-256 `D5DA71C9D126E244692BDFADBC3CFF433754079AB9F619D759C80EE0A90C4A2F`.
- Recorded by verifier: 2026-08-04T10:12:59+02:00, seconds precision from the local system clock.
- Result: 53 of 54 mechanical checks passed; `CHECKER_SELECTED_IMPORT_REPLAY` failed.
- Exact symptom: the sealed 39-member return manifest declared `intake/frozen_producer_package_v002/SHA256SUMS.txt`, 16,656 bytes, SHA-256 `733454A89830405E9D793E2565296C528BA0A5CAB1CE57177FA29C6E6EC886BD`, but the producer’s imported selected-member snapshot lacked that nested manifest.
- Classification: producer custody/import omission. It is not a source, translation, formula, terminology, build, script-completeness, PDF, or visual finding.
- Correction: copy the exact declared member from the checker-owned recheck intake into the matching producer snapshot path, verify bytes and hash, and rerun the same verifier. Do not edit any declared member.
- Consequence: dispatch remained halted. Accepted Hans, rejected Hant v002, Hant v003, both predecessor roots, German/P35 source, and SGA were unchanged.

This file and the failed JSON are append-only adverse evidence. A later all-pass run supersedes only the failed freeze gate; it does not erase this attempt.

