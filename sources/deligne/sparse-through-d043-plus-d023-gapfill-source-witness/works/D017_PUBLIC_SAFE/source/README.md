# D017 — Formes modulaires et représentations de GL(2)

P. Deligne. Complete authority scope: physical pages 1–51, printed pages 55–105.

The French and standalone English readers are mathematical TeX editions, each
with one editorial cover followed by 51 authority-anchored pages. The apparatus
records source anomalies and source-faithful restorations, and supplies 11
unaltered image fallbacks. Source running identifiers and folios are excluded
from the reader bodies but retained in the complete authority witness.

This is PAPER_COMPLETE, not a session-only or partial result. The new independent
gate is in D017_CORPUS_GATE.json. The inherited web-session PASS and every older
branch remain ZERO_ACCEPTED: they are preserved evidence, not the basis for
accepting the repaired editions.

## Editable sources and reconstruction

Extract D017_Source.zip. Its sources/ directory contains the three TeX files,
two complete page-indexed editable NDJSON layers, and all fallback assets. Run:

    python rebuild_readers.py --source sources --output build

XeLaTeX and the standard packages listed in the preambles are required. Shell
escape is disabled. Two independent clean-directory builds reproduced both
language PDFs byte-for-byte. The apparatus containers differed in serialization,
but all 17 page rasters and extracted text were identical. The distributed
PDF bytes are fixed by the packet manifest.

For exact repair replay, extract the full-state ZIP found inside
D017_Public_Provenance.zip under original_final_trio/. Set D017_INPUT_ROOT to that
extracted directory and D017_OUTPUT_ROOT to a fresh output directory, then run
repair/build_repaired_d017.py. Every old/new repair and field identity is retained
under repair/. The repaired files do not overwrite any inherited source.

## Preservation chain

D017_Public_Provenance.zip is a literal-account-name-only derivative of the
returned rigorous audit ZIP. It retains all cumulative state, prior-work
witnesses, rigorous audit material and web proof; only that name string and
the surrounding archive containers are changed. Every authority image and
mathematical source payload remains exact. The immutable original archive is
retained privately, identified by SHA-256. The transformation receipt maps
each changed member's original and public size and hash. Historical manifests
and content-addressed filenames inside the carrier describe original bytes,
not reissued acceptance certificates. The complete 51-page authority PDF is
also supplied directly.

SHA-256 identities, member byte counts, archive CRC replay, deterministic ZIP
rebuild identity, and public-surface checks are recorded in the accompanying
JSON receipts. No publication transaction is claimed by this local packet.
