# P29 U02 authority-validator failure history

This append-oriented note preserves failed validator-development approaches that were repaired before the U02 checkpoint. Exact failure-state script hashes are unavailable because the script was patched in place before hashing; no digest is invented.

1. At approximately 2026-07-18 20:54 Europe/Berlin (minute precision), the first run failed before execution with Python `SyntaxError: unterminated string literal`. Cause: a raw Windows-path string fragment ended in a backslash. Repair: use forward-slash path fragments in ordinary Python strings. The failed script-state hash is unavailable.
2. At approximately 2026-07-18 20:56 Europe/Berlin (minute precision), the second run correctly verified all pinned hashes, U02 equality with full-P29 lines 25–39, and both authority occurrences, but returned an error because it required full line 41 to equal only the item heading. In the source, the first proof sentence follows the heading on the same physical line. Repair: validate the pinned heading as a prefix while preserving the complete next-line text in the report. The failed script-state hash is unavailable.
3. The second report also exposed that Python text-mode reads normalize line endings automatically. Calling that result a raw occurrence count would be false. Repair: decode `read_bytes()` for raw ordinal comparison and normalize CRLF/CR to LF only in the explicitly named normalized comparison.

These failures concern the reproducibility validator, not the German source or Korean translation. The final script and report hashes are recorded by the U02 manifest after the successful replay.
