# Manifest scope

The completed checkpoint is designed to contain exactly 79 files. `ZENODO_PAYLOAD_MANIFEST.csv` lists every proposed public file except itself and `SHA256SUMS.csv`, for 77 rows. Its rows give the exact relative path, role, bytes, SHA-256, media type, publication action, authority basis, caveat, DOI controls, and supersession statement.

`SHA256SUMS.csv` lists every package file except itself, for 78 rows, including the payload manifest and package-wide validation receipt. A valid freeze has no extra, missing, byte-mismatched, or hash-mismatched file.

The French archive and TeX, French source slices, original scan and derivatives, external English controls, failed or superseded local builds, raw private-path logs, contact sheet, independent duplicate renders, rejected prose receipts, freeze scripts, handoffs, archives, and TeX auxiliary files are outside the public payload. The cumulative driver, exactly three section fragments, exactly one PDF, exactly 13 final English-PDF page renders, six public build files, public-safe machine projections, three machine-correction disclosures, rights caveats, live-state control, and portable verifier are inside it.
