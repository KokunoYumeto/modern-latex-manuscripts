# Build and visual-QA record: Noether Paper 36

Date: 2026-07-17

- two `pdflatex` passes completed with exit code 0;
- final output is one A4 page, PDF 1.5;
- meaningful final-log scan returned zero matches for Overfull, Underfull,
  LaTeX/package warnings, undefined controls, emergency stops, and fatal errors;
- `pdftotext -layout` preserved the title, citation, item number, author line,
  complete notice, and page number;
- final PDF rendered at 144 dpi to `render_check/paper36-1.png`;
- complete-page visual inspection passed: no clipping, overlap, missing glyphs,
  margin failure, or illegible emphasis; item number and small capitals render
  correctly.
- `CORRECTION_LEDGER.csv` (8 rows), `TERMINOLOGY_AND_ADVERSE_LEDGER.csv`
  (4 rows), and `ZENODO_PAYLOAD_MANIFEST.csv` (2 rows) parsed through
  artifact-tool with exact header and field-count checks;
- all three spreadsheet previews were visually inspected and passed for
  readable content, wrapping, and intact row/column structure.

Final TeX SHA-256:
`6606AD33AC9262305417BA2C6A2ABEE2B4DB3E8BEF9343B09FA5628713CDC8A0`

Final PDF SHA-256:
`02A488B5EC92C84A5FF7F0E82D4A4499F0694E56BDB56AD4A359A68E8637E94C`

Final log SHA-256:
`C321E5F353DB6818BFD88427B52F22783AA795B85B3CDF2D1CF3DA26D61A8D17`

Rendered-page SHA-256:
`49A462A45AA80EC0C4CA92E054B1DA60186CC274ECF9AB9E66FE75911071AB1B`
