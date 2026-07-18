# Build, source, render, and review summary

## Scope and source

This checkpoint contains one English TeX source and one four-page PDF covering
the opening of SGA 1, Exposé I, through §I.2. The sole textual authority is the
French TeX in arXiv `math/0206203v2`, lines 556--652. The newly added §I.2
slice, lines 605--652, has SHA-256
`B4AF85951DA7F743BF937FBABA0BB228655BEC769319040DE726414A262ED1F1`.

## Source and structural review

- Seven §I.2 English decisions and seven formula/structure checks recorded.
- Proposition I.2.1, conditions (i)--(iii), the quasi-finite definitions,
  EGA note, Corollary I.2.2, and closing (i)--(v) sequence pass.
- The original-print scan confirms `f^{-1}(x)` at printed p.2; the body uses
  `f^{-1}(f(x))` with an explicit source-defect note.
- The old page-2 marker is placed at its exact internal sentence boundary.
- The line-630 source index entry remains explicit cumulative-index debt.
- External English controls supplied only wording and regression candidates;
  no agreement was treated as source evidence.

## Build and render review

- Three final pdfLaTeX passes completed successfully.
- Each final log has SHA-256
  `7C5AA5EC3D42A9BEE2C495E528BBCE7515DC22D530BE1170E0893AFCBA9A3F09`.
- Zero LaTeX warning, overfull, underfull, undefined, or fatal matches.
- Final PDF: four pages, 366,529 bytes, SHA-256
  `316C4249BBC9AE4363BB69096C3EA62070E8FA4D24F14E00AF3E1B295A7B4477`.
- All four pages rendered at 180 dpi and visually inspected; no clipping,
  overlap, blank content, broken glyph, or malformed formula was found.
- Page 4 visibly contains both source-page markers, the type-correct fiber,
  readable disclosure note, both theorem labels, and all three footnotes.

## Public-package boundary

The public checkpoint includes sanitized compile records and English-reader
renders. It excludes raw build logs with private paths, French text/source,
the original scan and scan-derived images, external English bodies, inherited
English bodies, raw comparison excerpts, private paths, and task identifiers.

This is a bounded source-audited working translation, not complete SGA 1,
peer review, a critical edition, mathematical certification, independent
human review, or a rights determination.
