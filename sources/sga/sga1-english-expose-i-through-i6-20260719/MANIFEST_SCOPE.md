# Manifest scope

The completed checkpoint is designed to contain exactly 65 files.
`ZENODO_PAYLOAD_MANIFEST.csv` lists every proposed public file except itself
and `SHA256SUMS.csv`, for 63 rows. Its rows give the exact relative path, role,
bytes, SHA-256, media type, publication action, authority basis, caveat, DOI
controls, and supersession statement.

`SHA256SUMS.csv` lists every package file except itself, for 64 rows, including
the payload manifest and package-wide validation receipt. A valid freeze has
no extra, missing, byte-mismatched, or hash-mismatched file.

The French archive and TeX, French source slices, original scan and
derivatives, external English controls, failed or superseded local builds, raw
private-path logs, contact sheet, and internal coordination records are outside
the public payload. Both editable section fragments, all ten final page
renders, the public machine projections, rights caveats, live-state control,
and portable verifier are inside it.
