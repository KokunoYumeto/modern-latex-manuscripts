# Build and visual-QA record: Noether Paper 27

Date: 2026-07-17

- two `pdflatex` passes completed with exit code 0;
- final output is one A4 page, PDF 1.5;
- meaningful final-log scan returned zero matches for Overfull, Underfull,
  LaTeX/package warnings, undefined controls, emergency stops, and fatal errors;
- `pdftotext -layout` preserved the title, citation, opening dash, small-cap
  author, complete notice, plain italic `q,p` quotient chain, superscripts, and
  page number;
- final PDF rendered at 144 dpi to `render_check/paper27.png`;
- complete-page visual inspection passed: no clipping, overlap, missing
  glyphs, margin failure, or illegible mathematics; the opening dash, small
  capitals, plain italic letters, and `q/p^i` to `q/p^{i-1}` direction render
  correctly;
- `CORRECTION_LEDGER.csv` (14 rows),
  `TERMINOLOGY_AND_ADVERSE_LEDGER.csv` (8 rows), and
  `ZENODO_PAYLOAD_MANIFEST.csv` (2 rows) parsed through artifact-tool with
  exact header and field-count checks;
- all three spreadsheet previews were visually inspected and passed for
  readable content, wrapping, and intact row/column structure.

Final TeX SHA-256:
`84CD25B4BC35BC471DA6B094F626880D5AE9B7A69928EC08F45D614B0709166E`

Final PDF SHA-256:
`F8C54DD8AEB3991607225B2EF955A73E5B7CDB3FD89E23E4B9A4C980B9B81299`

Final log SHA-256:
`D73556A225580E1110E45FC7CE3F02F44BEB02E469B011BA522D272D4D2E8759`

Rendered-page SHA-256:
`CB93AAAD7E7B31E35EEFA08C35D51316E7C30AEC0F5BD52C08DF4E44E77F48F0`
