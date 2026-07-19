# Unit status - Expose VIII bicomplex setup equations 1.2-1.4

Status: this bounded unit is independently source-reviewed and sealed for its
stated scope. It is not a cumulative Expose VIII edition or a completed SGA 2
translation; cumulative integration remains pending.

- Unit ID: `SGA2-VIII-Q12`.
- Included authority scope: corrected French lines 2597-2609, wholly on
  original printed page 87; physical source-PDF page 77; recomposed running
  page 69.
- Continuation cursor: French source line 2611 after blank line 2610.
- Boundary caveat: original printed page 88 begins only inside excluded line
  2611. Earlier records that gave pages 87-88 as the included body are retained
  as superseded history and corrected by revision-2 locator records.
- Coverage: definition of `A^bullet`; injective resolution `a`; double complex
  `Q`; equations (1.2), (1.3), and (1.4); the first spectral-sequence statement;
  definitions of `L'^bullet` and `P^bullet`.
- Excluded: blank line 2610 and the simple-complex computation from line 2611.
- Source correction: equation (1.2) uses the corrected `L^{-q}` branch printed
  in the direct PDF; the uncorrected `L^q` alternative is rejected.
- Comparison control: jcreinhold e7a259f is comparison-only. Its agreement on
  `L^{-q}` is not independent corroboration; its `C_A`, flat `F`, and code
  typography are rejected while source `CA` and underlined `F` are retained.
- Target repairs: ordinary parentheses remove one nonstandard extracted
  control without visible mathematical change. Source-matching automatic
  equation counters preserve labels (1.2)-(1.4) and create distinct PDF
  destinations `equation.2`, `equation.3`, and `equation.4`.
- TeX: 1,833 B; SHA-256
  `A48852BD1464D78059E646A5FE5BEBDF82D2D420EEB9C01EFDC9058DFE5736F6`.
- PDF: 206,053 B; one unencrypted A4 page; SHA-256
  `A15D54373FFBA9B82D5270524C260813ABF6B10638FFC6B36BAC8CEC20EE2032`.
- Build/render evidence: a fresh isolated two-pass `pdflatex` build; clean
  pass-2 log; 12/12 reported font rows embedded, subset, and Unicode; direct
  source and target pages inspected at 300 and 600 dpi; no clipping, overlap,
  numbering drift, or glyph loss observed.
- Machine evidence before exact-manifest import: 53 substantive CSV rows; 25
  structural JSONL records across 13 stable IDs; 16 difficulty/revision JSONL
  records across 12 stable IDs. Supersession, hierarchy, and cross-file
  references are revalidated in `MACHINE_READABLE_VALIDATION.json`.
- Review state: bounded source/formula/notation/page/boundary/build/render/
  extraction/machine review passed. Reopen on authority replacement, source
  repagination, cumulative integration conflict, or target-toolchain reflow.
