# Build validation - SGA2-VIII-C23-POC

- Two fresh `pdflatex` passes completed successfully. The final pass contains
  no LaTeX, package, undefined-reference, overfull-box, underfull-box, fatal,
  or emergency-stop diagnostic.
- Final PDF: one unencrypted A4 page, 271312 bytes, SHA-256
  `47D12027336F93169F5CDDDF7FB7F7AD34BCF51C5E43CD02FFDFD6D3C79647DA`.
- Editable TeX: 2970 bytes, SHA-256
  `118405B69862ED1FA9E9710D100D214A1C847D0F54DB99054AB5BD8D7AAE08E2`.
- Both 24728-byte build logs have SHA-256
  `7CD1C7A0BE3DA3B5DCE798FFE578C2FD3BF3FABC4FCFFF4839C7ACD766D267FD`.
- `pdffonts` reports 20 font rows; every row is embedded, subsetted, and
  Unicode mapped.
- `pdfinfo -dests` reports exactly `Doc-Start`, `Hfootnote.1`, and `page.1`;
  the footnote destination is present and no broken destination is reported.
- Poppler inspection used byte-identical short-path copies. The target copy
  retained the final PDF hash above, and the source copy retained authority
  hash
  `41AD02C57321A8D2200FF32A929BC93ADBC3DE0D59DCD5A284D28D859FB87A90`.
- Final layout extraction is 2390 bytes, SHA-256
  `3839890FFC82615DB6C0790AE8D2856E63C322FC6942F4B4E873FFBA9321885F`,
  and contains zero forbidden control bytes.
- All builds, renders, extraction, font and destination reports were
  regenerated after the period/marker, italic-*below*, and extraction-safe
  delimiter revisions.

Build logs, auxiliary TeX products, short inspection copies, and extracted
text are local-only diagnostics and are excluded from the proposed checkpoint
manifest.

Independent closure: the exact frozen TeX was rebuilt twice in isolation;
pass 2 had zero diagnostics. The one-page independent PDF has 20 embedded,
subsetted, Unicode font rows and three destinations. See
`INDEPENDENT_BUILD_VALIDATION_20260719.md`.
