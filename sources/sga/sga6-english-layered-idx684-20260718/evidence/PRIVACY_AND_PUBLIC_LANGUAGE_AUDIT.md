# Privacy and public-language audit

Date: 2026-07-18  
Result: **PASS after correction and re-scan**

The proposed payload was checked before handoff for the class of defect found
in the published `10.5281/zenodo.21430251` support ZIP.

## Text and wrap-aware scan

Thirty-one text-bearing files then present (`.md`, `.csv`, `.json`, `.log`,
`.tex`, and `.txt`) were scanned both as raw text and after removing line
breaks, tabs, and spaces. The scan covered user-directory forms, drive-rooted
French-control paths, application-data paths, cache/runtime paths, and the
private workspace/source-tree names identified in the predecessor defect.

The first pass found no user-directory or wrapped absolute-path leak, but it
did find one residual internal source-path fragment and several internal
assistant/baseline labels in TeX comments and provenance ledgers. Those public
copies were corrected without changing the production originals. The second
pass found:

- raw private-path matches: 0;
- wrap-reconstructed private-path matches: 0;
- internal assistant/baseline labels targeted for removal: 0.

## Reader and binary evidence

Text extracted from the exact frozen reader PDF was scanned for the same
private/internal phrases and returned zero matches. The copied PDF retained
SHA-256
`0F8D9777F81F72174844C31A105DC5ECA277451C5E2320B04054D9FECC9CB2E8`.
It has 377 pages, descriptive metadata and an XMP metadata stream, a durable
project Author field, and 41/41 embedded font rows. It is not accessibility
tagged; that limitation remains explicit.

All manifests were regenerated after the comment/ledger corrections. This
audit does not determine source or derivative redistribution rights; those
remain an archive-owner publication gate.
