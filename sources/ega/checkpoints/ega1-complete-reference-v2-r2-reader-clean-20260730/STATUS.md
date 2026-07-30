# EGA I complete English reference reader - R2 status

Date: 2026-07-30

Status: **reader-clean technical PASS; extracted-package replay PASS; ready
for archive replacement**.

## Scope

- Complete EGA I through EOF: Sections 1-10.15, bibliography, notation index,
  and terminological index.
- Active editable source: 16 files / 586,386 bytes.
- Reader: 113 letter pages / 1,356,401 bytes / SHA-256
  `0DC301F1998AA4E6A97ABD92197BB94A3F7FBEE1847261CC7BB69E0F8E6D8C58`.

## Reference closure

- Stable targets: 750, all unique.
- Delivered internal GoTo edges: 1,459; resolved 1,459/1,459; broken 0.
- Named PDF destinations: 1,701.
- Source candidates: 2,431 = 649 structural targets + 1,364 applications +
  418 reviewed residuals; the partition is exact and pairwise disjoint.
- The 418 residuals remain intentional nonedges. No cross-volume target was
  guessed.

## Reader-clean correction

Held R1, PDF SHA-256
`C745C7C161AB612423A3543294693DD3FCCAAFCBCAD58E03CBE278BBBF241B2F`,
registered each backmatter index twice in the contents and expanded the reader
to 114 pages. R2 removes only those two redundant manual registrations,
regenerates all affected source-line identities, and restores the established
113-page reader pagination. R1 remains immutable audit history.

## Completed QA

- BibTeX once plus five XeLaTeX passes; passes 4 and 5 byte-identical.
- Blocking TeX diagnostics: 0.
- Fonts: 21/21 embedded and subset; Type 3: 0; raster image XObjects: 0.
- Source reconstruction: 16/16 exact after reversing the declared reference
  layer and restoring the two historical R1 contents writes.
- Direct rendered review of pages 2, 3, 19, 38, 88, 90, and 110-113: PASS.
- Contents entries for both indexes: exactly one each.
- Extracted-package replay: 45/45 files and 4,046,276 bytes exact before and
  after review; canonical replay identity
  `9AC1511D0CBF6917D865E8F5D435603B4D8CB2AF55D3FB96A741A7242CDF2300`.
- Fresh build from the copied package reproduced all 113 decoded page streams
  and extracted-text streams, all 1,701 destination signatures, all 1,459
  annotation/action signatures, and PDF metadata exactly.

This is a complete source-aligned working English reader with an exhaustive
local reference graph. It is not a critical edition, mathematical peer review,
accessibility certification, or rights-clearance decision.
