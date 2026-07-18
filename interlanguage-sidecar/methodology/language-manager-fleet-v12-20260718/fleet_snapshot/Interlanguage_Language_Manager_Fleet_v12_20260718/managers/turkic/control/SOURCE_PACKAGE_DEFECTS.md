# Preserved source-package defects

The canonical `pan-turkic-source-bodies-20260705/README.md` is not edited in place because its original hash is part of the package.

Observed metadata defects:

- `Package ID: $packageId` contains an unexpanded variable. The manifest supplies the correct ID: `PAN-TURKIC-SOURCE-BODIES-20260705`.
- Several `bodies/` bullets contain an embedded control character before `bodies`. The directory on disk is correctly named `bodies/`.
- `original_local_path` values in the manifest refer to the originating `C:\Users\memo_\...` machine. The current physical package target is recorded in `SOURCE_PACKAGE_REGISTRY.csv`.
- The README's early count tables describe an earlier package state, while the final manifest contains 418 rows and the physical package contains 331 files. Use the final manifest, SHA file, and physical audit rather than the stale prose counts.
- `SHA256SUMS.txt` names 330 paths but contains 325 unique content hashes because five hashes are reused by more than one path. The manager audit is therefore path-based: all 330 listed paths pass. A hash-keyed audit would incorrectly collapse five legitimate entries.

These are navigation defects, not permission to alter the preserved package or promote its linguistic claims.
