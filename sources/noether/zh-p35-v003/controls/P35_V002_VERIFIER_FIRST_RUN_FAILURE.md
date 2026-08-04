# P35 v002 producer verifier — preserved first-run failure

- Time: 2026-08-04 06:46 +02:00 (minute precision reconstructed from the immediate terminal sequence; no report file was written).
- Script: `controls/verify_p35_v002_producer_package.py`.
- Failed stage: replay of `controls/history/V001_SEED_SHA256SUMS.txt`.
- Error: `ValueError: not enough values to unpack (expected 2, got 1)`.
- Cause: the first implementation assumed every manifest line had `SHA256  PATH`; the actual preserved manifest begins with comment lines and uses `SHA256  BYTES  RELATIVE_PATH`.
- Correction: skip comment/blank lines, parse exactly three fields, and validate both byte count and SHA-256 for v001 and v002 manifest entries.
- Scope: verifier implementation only. No source, translation, TeX target, PDF, checker artifact, German file, registry, or SGA file changed.
- Superseding result: `controls/P35_V002_PRODUCER_VERIFICATION.json`, generated on the second run with all 11 pre-manifest mechanical checks passing.

This failure is packaging/tooling evidence, not a target or German-source defect.
