# Paper 35 Chinese v003 producer — first manifest attempt superseded

- Exact first attempt: `P35_V003_FIRST_MANIFEST_ATTEMPT.txt`, 211 entries, 29,304 bytes, SHA-256 `952364985F93C5159563D27C847D6893AD36D6EB84D437017D5510D3D4B60196`.
- Honest time precision: generated on 2026-08-04 after the 10:13 local verifier repairs and before any external freeze receipt or dispatch; the exact generation second was not retained in the manifest.
- State: `SUPERSEDED BEFORE DISPATCH`.
- Reason: pre-replay inspection found that the verifier’s actual-file inventory excluded every file whose basename was `SHA256SUMS.txt`. The v003 package intentionally contains nested checker-custody manifests, so that name-wide exclusion could not prove the root manifest complete.
- Correction: preserve this manifest, change the helper to exclude only the exact root self-reference by relative path, rerun the full producer verifier, then regenerate the root manifest last and replay it without writing inside the root.
- Scope: verifier/freeze custody only. No accepted Hans, Hant v002, Hant v003, source, binder, German authority, PDF build, checker-owned file, or SGA artifact changed.

This record and the exact first manifest are append-only adverse evidence. The later final manifest supersedes only this attempted freeze identity.

