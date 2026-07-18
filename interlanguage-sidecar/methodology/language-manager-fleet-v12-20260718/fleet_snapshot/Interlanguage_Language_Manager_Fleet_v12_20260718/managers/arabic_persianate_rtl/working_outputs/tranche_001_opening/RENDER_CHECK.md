# Render check

- Rendered both final PDFs at 180 dpi with Poppler `pdftoppm`.
- Inspected every page (one Arabic page and one Iranian-Persian page).
- First render defect: working-status metadata appeared above the scholarly
  footnote at the bottom of the page.
- Repair: moved status metadata beneath the title and rebuilt twice.
- Final result: no clipping, overlap, missing glyphs, broken joining, reversed
  Latin identifiers, or bidi footnote defect observed.
- Code-point audit found no Persian yeh/keheh in the Arabic source and no
  Arabic yeh/kaf in the Persian source; the Persian source retains 34 ZWNJ
  join controls.
- After adding `P06-S0005`, both documents were rebuilt twice and every final
  page was rendered and inspected again. Both remain one-page A4 documents.
- TeX logs contain no LaTeX/package warnings, missing-character reports,
  overfull boxes, or underfull boxes after the final two-pass builds.
- Detailed invariant results: `BIDI_INVARIANTS.md`.
