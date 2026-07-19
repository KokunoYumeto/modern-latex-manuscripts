# Independent build validation - 2026-07-19

- Two fresh `pdflatex` passes completed with exit code 0.
- Pass 2 has zero LaTeX/package warnings, undefined references, overfull or
  underfull boxes, missing characters, and fatal diagnostics.
- Final PDF: one unencrypted A4 page; 218631 bytes; SHA-256
  `29C01219A47513327E73A3134B9465AA9A0F84EF998D35932AA545C166720AD1`.
- Final TeX: 1773 bytes; SHA-256
  `99B5FFB10DB9E8E028AD0055F72076A30872D0306F4218DBA497108427821D1A`.
- Font inspection reports 14 rows; every row is embedded, subsetted, and
  Unicode mapped.
- Extracted target text contains zero forbidden control bytes. Spatial
  extraction interleaves the vertical arrow labels, but the complete map data
  is present in linear prose and every diagram label is visually legible.

The build validates the bounded target only. It does not assert cumulative
Expose VIII or full-volume completion.
