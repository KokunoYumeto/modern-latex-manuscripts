# Build and visual-QA record: Noether Paper 5

Date: 2026-07-17

- two `pdflatex` passes completed with exit code 0;
- final output is two A4 pages, PDF 1.5, 249067 bytes;
- meaningful final-log scan returned zero matches for Overfull, Underfull,
  LaTeX/package warnings, undefined controls, emergency stops, missing
  characters, multiply defined labels, and fatal errors;
- `pdftotext -layout` preserved the complete title and byline, all five
  page-qualified source-note markers, the three numbered basis discussions,
  the repaired coefficients-with-respect-to-the-`u` sentence, the displayed
  linear form, the value `±1`, and the final source-boundary
  question;
- final PDF rendered at 144 dpi to `render_check/paper05-1.png` and
  `render_check/paper05-2.png`;
- complete-page visual inspection passed for both pages: no clipping, overlap,
  missing glyphs, margin failure, or illegible mathematics; long source notes,
  the displayed formula, and page-qualified note labels are fully contained;
- `CORRECTION_LEDGER.csv` (23 rows),
  `TERMINOLOGY_AND_ADVERSE_LEDGER.csv` (12 rows), and
  `ZENODO_PAYLOAD_MANIFEST.csv` (2 rows) parsed through artifact-tool with
  exact header and field-count checks;
- all three spreadsheet previews were visually inspected and passed for
  readable content, wrapping, intact row/column structure, and literal-text
  handling of the mathematical and terminology corrections.

Final TeX SHA-256:
`9479CBF826CEAEEF88DE48A65BBA2D20B0D2FF7CDF71AA7D0581DD30FA8E5011`

Final PDF SHA-256:
`7D100558AF04C43617B7BF758BB99C3C01CE1AAB5AC82830F23BC933FAF96F89`

Final log SHA-256:
`650004FB99C9BE8D86C5832B8F7E1E88042D085D077F0008F9C91897B449599D`

Rendered page 1 SHA-256:
`979679DC0FCC2259C474ECFF04D3B2ACAA541DEC3445210C4BF67DD344A18725`

Rendered page 2 SHA-256:
`2422B532D25FBDE76E612BACA353E0B70D549D62D59BB361A661A4688211D579`
