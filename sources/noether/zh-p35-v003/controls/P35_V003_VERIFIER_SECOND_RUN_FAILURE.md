# Paper 35 Chinese v003 producer verifier — second-run failure

- Failure record: `P35_V003_VERIFIER_SECOND_RUN_FAILURE.json`, 18,310 bytes, SHA-256 `3688EFE8A07D430CBC77FA36E1D855327E379EF032FDF7C309A333550EF1E080`.
- Recorded by verifier: 2026-08-04T10:13:38+02:00, seconds precision from the local system clock.
- Result: 53 of 54 mechanical checks passed; `CHECKER_SELECTED_IMPORT_REPLAY` still reported the restored nested v002 manifest missing.
- Exact cause: the verifier helper used `excluded_names = excluded_names or {manifest.name}`. Passing an intentionally empty set therefore selected the default and excluded every file named `SHA256SUMS.txt` from the actual-member inventory, including the restored nested member.
- Classification: producer verifier tooling defect. The imported member itself was present at 16,656 bytes / SHA-256 `733454A89830405E9D793E2565296C528BA0A5CAB1CE57177FA29C6E6EC886BD`.
- Correction: distinguish `None` from an explicitly empty set, then rerun without modifying any checker-declared member or target artifact.
- Consequence: dispatch remained halted. Accepted Hans, both Hant revisions, predecessor roots, German/P35 source, and SGA were unchanged.

This file and the failed JSON are append-only adverse evidence. A later all-pass run supersedes only this verifier failure state.

