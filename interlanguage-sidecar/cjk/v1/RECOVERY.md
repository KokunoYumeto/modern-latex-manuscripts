# Recovery and maintenance

This release is operationally self-contained as a standard, schema, ledger, manifest, and integrity verifier. It does not contain or own any Chinese, Japanese, or Korean translation corpus. Independent replay of a `hash_only` finding requires separately obtaining the exact cited artifact.

To verify a checkout or archive:

1. use Python 3.11 or newer;
2. install the exact verifier dependencies with `python -m pip install --require-hashes -r requirements.txt`;
3. run `python -B verify.py` from the release root and write any receipt outside that root;
4. require every reported check to pass and repeat in a fresh process, requiring byte-identical receipts;
5. compare every payload file listed in `manifest.csv` by byte count and SHA-256;
6. treat `evidence.jsonl` source identities as locators for independently obtained project artifacts, not bundled source material.

`manifest.csv` intentionally does not list itself: a file cannot contain its own final cryptographic hash. Its root of trust is the deterministic archive, then the exact Git commit and containing Zenodo-version download identity recorded by the publication receipts. The archive contains both the payload and manifest and is built twice byte-identically before release.

An adopting lane records the seven independent conformance states in `report.schema.json` and runs the applicable `tests.json` fixtures. A single aggregate readiness score is not a recovery substitute.

For an update, preserve the previous component and containing DOI version, add or supersede evidence records with stable IDs, update the adverse ledger, increment `VERSION`, rebuild `manifest.csv`, and run the verifier twice. Build the archive twice, compare it byte-for-byte, extract each copy into a fresh directory, and rerun the verifier there. Never silently rewrite an old release or let one locale authorize another.

The human standard, schema, evidence ledger, and verifier are read-only inputs for language lanes. Each lane remains the sole writer of its translation and locale profile.
