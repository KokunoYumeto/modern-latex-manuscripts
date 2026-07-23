# SGA 2 R6 final visual QA — 2026-07-23

Status: **PASS**.

- The frozen 184-page R6 PDF was rendered in full at 72 dpi and compared with
  the immutable R5 PDF.  180 pages are pixel-identical.  Physical pages 42,
  47, 48, and 49 contain only 1,552 changed raster pixels in total; page 48
  accounts for 1,461.  Direct paired inspection found only imperceptible
  sub-point line-justification rounding at newly inserted hyperlink boundaries.
- `pdftotext -layout` output is byte-identical across all 184 pages, page
  geometry is identical, and no wording, line break, page-flow, equation,
  diagram, header, footer, or index layout changed.
- Sixteen 144-dpi representative pages were inspected: 1, 11, 27, 48, 53,
  57, 68, 82, 91, 115, 126, 144, 151, 154, 183, and 184.  They cover title
  matter, exposé transitions, dense prose, equations, commutative diagrams,
  footnotes, and both terminal index pages.
- No clipping, overlap, missing glyph, broken rule, malformed formula or
  diagram, or unintended blank page was found.

Representative contact sheet SHA-256:
`FC580CA62B9B21685F0C09AA6F1F14B563BFA2689759DE80B045A5F999AE58E3`.

Differing-page paired contact sheet SHA-256:
`D267AD7F69FA47B37775D8343DBE5E698CAA2CA843A159C602BD9C8CA39E993D`.
