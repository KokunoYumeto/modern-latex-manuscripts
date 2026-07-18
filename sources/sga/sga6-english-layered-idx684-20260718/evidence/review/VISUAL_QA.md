# Visual QA — SGA 6 idx663--684 successor checkpoint

Date: 2026-07-18  
Verdict: **PASS for the rendered successor checkpoint pages**

## Exact PDF inspected

- file: `SGA6_English_Complete_Layered_WorkingEdition.pdf`
- SHA-256: `0F8D9777F81F72174844C31A105DC5ECA277451C5E2320B04054D9FECC9CB2E8`
- extent: 377 A4 pages; all fonts embedded

The current-rescribe indices, printed source pages, source-PDF pages, and
full-reader PDF pages are distinct coordinate systems. The render evidence
below uses **full-reader PDF page numbers** only.

## Render method and coverage

Full-reader pages 349--362 were rendered from the exact PDF above at 160 dpi,
one page per process to cap memory use. These fourteen consecutive pages cover
the idx663--684 material and the paired idx685 boundary continuation. Four
50-percent contact sheets were then produced from those same PNGs.

Evidence directories:

- `controls/idx663_684_french859bd5_reconciled_20260718/render_qa/final_full_reader_pages349_362/`
- `controls/idx663_684_french859bd5_reconciled_20260718/render_qa/CONTACT_SHEET_01.png` through `CONTACT_SHEET_04.png`

All fourteen full-resolution renders and all four contact sheets were visually
inspected. The review included the Picard-functor material, Corollary 6.14,
the Hodge index formulas and Corollary 7.3, the Exposé XIV transition, the
inline Dold--Puppe isomorphism, the Riemann--Roch maps restored to source-inline
layout, formula (3.1), the topological-filtration diagrams, the Jouanolou
footnote, and the idx684/idx685 parenthesis boundary.

## Result

No clipping, overlap, missing or blank page, broken formula, replacement
glyph, corrupt raster, footer discontinuity, or unreadable line was found.
The four formulas changed from fabricated display layout back to source-inline
layout fit without collision or margin overflow. Page numbering is continuous.

The independent second-half reviewer additionally rendered seven pages from
an exact-hash test wrapper and recorded a clean result in
`independent_review/IDX674_684_POSTEDIT_REVIEW.md`.

This is a rendering verdict. It does not convert the layered full reader into
a uniformly source-audited or accessibility-tagged edition.
