# Manifest scope

`ZENODO_PAYLOAD_MANIFEST.csv` lists every proposed public file except itself
and `SHA256SUMS.csv`. Its rows give the exact relative path, role, bytes,
SHA-256, media type, publication action, authority basis, caveat, DOI controls,
and supersession statement.

`SHA256SUMS.csv` lists every package file except itself, including the payload
manifest and the package-wide validation receipt. A valid freeze has no extra,
missing, byte-mismatched, or hash-mismatched file.

The French archive and TeX, source slice, original scan and derivatives,
external English controls, failed or superseded local builds, private paths,
and internal coordination records are outside the public payload.
