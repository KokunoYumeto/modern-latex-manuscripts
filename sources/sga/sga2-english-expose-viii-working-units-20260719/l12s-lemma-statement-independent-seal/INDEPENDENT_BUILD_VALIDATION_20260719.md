# Independent build validation - 2026-07-19

- Two fresh `pdflatex` passes completed with exit code 0.
- Pass 2 has zero LaTeX/package warnings, undefined references, overfull or
  underfull boxes, missing characters, and fatal diagnostics.
- Final PDF: one unencrypted A4 page; 234774 bytes; SHA-256
  `2397DEA97C66AC3D378A3AA1CD63E8519F249F6E8D622B80E46D0CDAAC7B8690`.
- Final TeX: 1810 bytes; SHA-256
  `0022D33C2E47D85FB286B82728D3B05EA0DCF8D29F46D1356B84F2FB4F17FF61`.
- Font inspection reports 14 rows; every row is embedded, subsetted, and
  Unicode mapped.
- Extracted target text contains zero forbidden control bytes. Every closing
  parenthesis remains searchable after the existing ordinary-delimiter repair.

The build validates the bounded target only. It does not assert cumulative
Expose VIII or full-volume completion.
