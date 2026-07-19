# Build validation - SGA2-VIII-C23

- Two fresh `pdflatex` passes completed successfully. The final pass contains
  no LaTeX, package, undefined-reference, overfull-box, underfull-box, fatal,
  or emergency-stop diagnostic.
- Final PDF: one unencrypted A4 page, 279208 bytes, SHA-256
  `9D53EFB7BFE7063F05E466BE618103FBCCAEA39DF5783A4D3F0CE53E405AF9BB`.
- Editable TeX: 2320 bytes, SHA-256
  `45FE67183432E18ADC78B72962A997AB03BEFD4A227F4F873DE13306BB93940F`.
- `pdffonts` reports 17 font rows; every row is embedded, subsetted, and
  Unicode mapped.
- Poppler could not open the very long working-directory path directly. The
  target PDF and source PDF were copied byte-for-byte to the short inspection
  directory `tmp/pdfs/sga2_c23`; exact SHA-256 equality was verified before
  inspection. The target copy retained the final PDF hash above, and the
  source copy retained authority hash
  `41AD02C57321A8D2200FF32A929BC93ADBC3DE0D59DCD5A284D28D859FB87A90`.
- The final two passes and renders were regenerated after root pre-seal review
  normalized the ordinary English noun to lowercase `O_X-module`; formulas,
  numbering, locators, and note content were unchanged.
- Layout extraction contains all four conditions and note (4), with zero
  forbidden control bytes. The PDF has the named destination `VIII.2.3`.

Build logs and extracted text are local-only diagnostics and are excluded from
the proposed checkpoint manifest.
