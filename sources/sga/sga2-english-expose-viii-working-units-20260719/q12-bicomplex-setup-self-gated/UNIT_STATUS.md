# Unit status - Expose VIII bicomplex setup equations 1.2-1.4

Status: bounded production draft translated and self-audited against the
corrected French TeX and direct compiled PDF. Build, render, extraction,
machine-ledger, and visual self-gates passed; independent source review is
pending. This is not a cumulative Expose VIII edition or a completed volume.

- Unit ID: `SGA2-VIII-Q12`.
- Authority scope: corrected French lines 2597-2609; original printed pages
  87-88; physical source-PDF page 77; recomposed running page 69.
- Continuation cursor: French source line 2611 after blank line 2610.
- Coverage: definition of `A^bullet`; injective resolution `a`; double complex
  `Q`; complete equations (1.2), (1.3), and (1.4); first spectral-sequence
  statement; definitions of `L'^bullet` and `P^bullet`.
- Excluded: blank line 2610 and the simple-complex computation from line 2611.
- Source correction: equation (1.2) uses the corrected `L^{-q}` branch printed
  in the direct PDF; the uncorrected `L^q` alternative is rejected.
- Comparison control: jcreinhold e7a259f is comparison-only. Its agreement on
  `L^{-q}` is not independent corroboration; its `C_A`, flat `F`, and code
  typography are rejected while source `CA` and underlined `F` are retained.
- Accessibility repair: ordinary parentheses in equation (1.2) replace
  extensible delimiters after the latter produced one extracted `U+0001`;
  final nonstandard-control count is zero with no visible mathematical change.
  The sole `U+000C` is the normal `pdftotext` page separator.
- TeX: 1,772 B; SHA-256
  `69EE451A6B6D18666892C87F031405B28C578F54C9CC3EC941BB545BB3EFE141`.
- PDF: 206,247 B; one unencrypted A4 page; SHA-256
  `C9EE83D3BE73281480E09AAE18C4516179AED6D7F70F6617DC8160FCB99844DF`.
- Build/render evidence: two clean `pdflatex` passes; 12 reported font rows all
  embedded/subset/Unicode; full-page and 600-dpi formula renders inspected;
  no clipping, overlap, numbering drift, or glyph loss observed.
- Machine evidence before exact-manifest import: 44 substantive CSV rows;
  13 structural JSONL records covering 11 stable IDs; 12 difficulty/revision
  JSONL records covering 11 stable IDs. Exact hashes are in the generated
  `UNIT_HASHES.csv` and `MACHINE_READABLE_VALIDATION.json`.
- Review state: self source/build/render/machine comparison complete;
  independent formula, numbering, page, boundary, and build review remains
  required before sealing or cumulative use.
