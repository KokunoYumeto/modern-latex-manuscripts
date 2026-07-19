# Manifest scope

`ZENODO_PAYLOAD_MANIFEST.csv` lists every proposed public file except itself
and `SHA256SUMS.csv`. `SHA256SUMS.csv` lists every package file except itself.
The portable verifier requires those exact sets, every row's byte length and
SHA-256, the machine-ledger closure, binary allowlist, build evidence, and
privacy/source-exclusion controls.

Included binaries are the current 15-page English reader, its 15 page renders,
and the prior 13-page English r10 reader retained only for historical target
closure. Excluded are all French source files/excerpts, original-print scans,
scan-derived images, external repositories/PDFs, archive files, private raw
compiler logs, and unrelated SGA payloads.