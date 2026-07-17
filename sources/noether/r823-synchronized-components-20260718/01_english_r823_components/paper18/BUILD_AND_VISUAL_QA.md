# Build and visual-QA record: Noether Paper 18

Date: 2026-07-17

- two `pdflatex` passes completed with exit code 0;
- final output is one A4 page, PDF 1.5;
- meaningful final-log scan returned zero matches for Overfull, Underfull,
  LaTeX/package warnings, undefined controls, emergency stops, and fatal errors;
- `pdftotext -layout` preserved the title, citation, complete session and talk
  headings, all prose, the corrected `R^(n)(x_n)` endpoint and congruence
  relation, the inline primary decomposition, and page number;
- final PDF rendered at 144 dpi to `render_check/paper18.png`;
- complete-page visual inspection passed: no clipping, overlap, missing
  glyphs, margin failure, or illegible mathematics; the one-line resultant
  formula is centered and fully contained;
- `CORRECTION_LEDGER.csv` (22 rows),
  `TERMINOLOGY_AND_ADVERSE_LEDGER.csv` (10 rows), and
  `ZENODO_PAYLOAD_MANIFEST.csv` (2 rows) parsed through artifact-tool with
  exact header and field-count checks;
- all three spreadsheet previews were visually inspected and passed for
  readable content, wrapping, intact row/column structure, and literal-text
  handling of the equality-versus-congruence correction.

Final TeX SHA-256:
`DE48D9D10E742D57A58FF4917DEA8C3A533CF210CDCC3986A05B721727A6D939`

Final PDF SHA-256:
`38ECF3F7E33E08AE7CD296EBFB0099CB5887D34C7FE987D237627510714BE285`

Final log SHA-256:
`4122002BDBA29079DCB4DCD2CB2222AD3383F249A051B92C789598FFBEA991C5`

Rendered-page SHA-256:
`7BF33DB08F6B57B60DCDF09BE9FC932DAAB5EB5307903E8ADC1F506FC6931F7A`
