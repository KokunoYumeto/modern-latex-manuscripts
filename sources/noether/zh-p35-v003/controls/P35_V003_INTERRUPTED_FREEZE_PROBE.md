# Paper 35 Chinese producer revision 3 — interrupted freeze probe

## Preserved probe state

This append-only record preserves the unsuccessful first freeze probe reported before the producer turn was interrupted. It is failure evidence for package sealing, not a target-language, source, formula, visual, or build defect.

- Work unit: complete Chinese Noether Paper 35, producer sibling revision v003.
- Controlling return: `ZHCHK-NOETHER-P35-V002-RETURN-001`.
- Probe result: `INCOMPLETE_FREEZE; DO_NOT DISPATCH`.
- Honest time precision: the exact probe second was not retained; it occurred on 2026-08-04 before the checker’s explicit freeze-resume instruction and after the v003 build documents were written at approximately 08:12 local time.
- Root manifest at the probe: inherited v002 `SHA256SUMS.txt`, 16,656 bytes, SHA-256 `733454A89830405E9D793E2565296C528BA0A5CAB1CE57177FA29C6E6EC886BD`, 130 entries.
- Read-only worker result: the inherited manifest still replayed its declared predecessor members, but the active v003 root had 69 then-current extra files not represented by that manifest.
- Missing freeze members at the probe: a v003-specific checker handoff, v003 freeze metadata, a v003 package verifier/report, and a v003 manifest generator.
- Correct response: halt dispatch, preserve the inherited manifest as evidence, add the missing versioned controls, regenerate the root manifest only after all in-root members are final, then replay the new manifest independently.

## Scope and supersession

The probe did not mutate accepted Hans, rejected Hant v002, the v003 Hant target, either predecessor root, checker-owned files, German source or authority, or SGA. It did not open or render a PDF and did not perform checking.

This record is never deleted or rewritten. A successful v003 freeze supersedes only its `DO NOT DISPATCH` operational state; it does not erase the failed probe or convert it into substantive validation.

