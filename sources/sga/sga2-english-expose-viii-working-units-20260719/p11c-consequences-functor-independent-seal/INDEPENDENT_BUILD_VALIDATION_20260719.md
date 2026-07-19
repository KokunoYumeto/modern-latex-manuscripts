# Independent build validation - 2026-07-19

- Two fresh `pdflatex` passes completed with exit code 0.
- Pass 2 has zero LaTeX/package warnings, undefined references, overfull or
  underfull boxes, missing characters, and fatal diagnostics.
- Final PDF: one unencrypted A4 page; 245199 bytes; SHA-256
  `3ADFA9902AF3F4216EF279C67A4B38B96150AA5ADFDCBA6B811E3BA5F562C007`.
- Final TeX: 2849 bytes; SHA-256
  `756FC12C7AF42D5729BC259DAE5E03E6DD975E8A86DC54B52730936A5DCDDFF8`.
- Font inspection reports 16 rows; every row is embedded, subsetted, and
  Unicode mapped.
- Extracted target text contains no forbidden control byte after replacing
  unnecessary extensible parentheses in the final one-line formula.

The build validates the bounded target only. It does not assert cumulative
Expose VIII or full-volume completion.
