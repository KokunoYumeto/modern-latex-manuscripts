# Independent build validation - 2026-07-19

The final 1,833-byte TeX, SHA-256
`A48852BD1464D78059E646A5FE5BEBDF82D2D420EEB9C01EFDC9058DFE5736F6`,
was copied into an empty short-path build directory and compiled twice with
MiKTeX pdfTeX 1.40.29 in nonstop, halt-on-error mode.

- Pass 1 completed and produced the expected first-run label/rerun notices.
- Pass 2 completed with no LaTeX warning, overfull/underfull box, fatal error,
  or duplicate-destination diagnostic.
- Final PDF: 206,053 B; SHA-256
  `A15D54373FFBA9B82D5270524C260813ABF6B10638FFC6B36BAC8CEC20EE2032`.
- PDF control: one unencrypted A4 page, PDF 1.5, no JavaScript or forms.
- Font control: all 12 reported rows are embedded, subset, and Unicode.
- Auxiliary labels: (1.2), (1.3), and (1.4) map respectively to
  `equation.2`, `equation.3`, and `equation.4`.
- PDF name tree: those three equation destinations occur once each and are
  distinct.
- Extracted-text control: no U+0000-U+0008, U+000B, U+000E-U+001F, or U+007F
  controls; the sole U+000C is the normal page separator emitted by
  `pdftotext`.

Local-only logs and extracted text are retained for review but excluded from
the proposed public manifest because build paths can be machine-specific.
