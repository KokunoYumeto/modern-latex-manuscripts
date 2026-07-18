# Rendered visual-QA evidence

QA date: 2026-07-18

## Scope and coordinate discipline

The English checkpoint PDF contains six physical pages. Its full source
envelope is French TeX lines 87--279 and original printed-volume pages 5--12,
including the Exposé/section headings; substantive §1 is lines 90--279 and
printed pages 6--12. The rendered French source-PDF control is physical pages
13--17. Printed pages and physical PDF pages are never treated as the same
coordinate.

## Retained renders

English full render:

- `render_check/unit_I_1_en/page-1.png` through `page-6.png`;
- `render_check/unit_I_1_en/contact_sheet.png`.

Scoped French-source render:

- `render_check/source_fr_pages_013_017/source-013.png` through
  `source-017.png`;
- `render_check/source_fr_pages_013_017/contact_sheet.png`.

The English page images are 1530 by 1980 pixels. The French control images
are 1445 by 1870 pixels. Contact sheets were assembled with ImageMagick
7.1.2-22 Q16 x64. Page images, not contact sheets alone, were used for
page-level inspection.

## English page inspection

| English PDF page | Content and locator check | Result |
|---:|---|---|
| 1 | Authority box, Exposé/section headings, printed p.6, equations (1)--(4), source-anomaly footnote | PASS |
| 2 | Printed pp.7--8, Proposition 1.1, equations (5)--(8') | PASS |
| 3 | Equation (8''), (6 bis), printed p.9, Proposition 1.2 and equation (9) | PASS |
| 4 | Printed pp.10--11, Proposition 1.3, Corollaries 1.4--1.6, Remark 1.7, equations (10)--(14) | PASS |
| 5 | Equations (15)--(17); corrected printed-p.12 marker aligned inside Proposition 1.8 proof | PASS |
| 6 | Proposition 1.10, equation (18), references, terminal whitespace | PASS |

Across all six pages, the review found no clipped text, overlapping objects,
truncated formulas, missing glyphs, broken underlines, or margin overflow.
Headers, footers, footnotes, page markers, mathematical displays, and
statement breaks remain legible.

## French source-page inspection

| French physical PDF page | Original printed pages represented | Check | Result |
|---:|---:|---|---|
| 13 | 5--7 | Exposé lead, section opening, equations (1)--(4), isolated underline anomaly at the definition of `Gamma_Z` | PASS |
| 14 | 7--8 | Proposition 1.1, equations (5)--(8''), (6 bis), editor note | PASS |
| 15 | 8--10 | Propositions 1.2--1.3 and equations (9)--(10) | PASS |
| 16 | 10--11 | Corollaries 1.4--1.6, Remark 1.7, equations (11)--(15') | PASS |
| 17 | 12 | Proposition 1.8 through Proposition 1.10, equations (16)--(18) | PASS |

The French render was used to confirm layout-dependent notation and the exact
printed-page transitions in addition to the controlling TeX. The isolated
underlined `Gamma_Z` occurrence on physical page 13 conflicts with equation
(2) and the systematic later global/sheaf distinction; the English resolves
it transparently with a translator footnote rather than silently changing it.

## Disposition

Visual QA passes for this bounded unit only. The renders are evidence for the
checkpoint; they do not turn the recovered 211-page English control PDF into
a source-aligned or publication-ready translation.
