# Validation - translation segment

Fresh TeX file:

`02_new_translation_latex/expose_iv_10_14/SGA4_Expose_IV_sections_10_to_14_en.tex`

Fresh PDF:

`02_new_translation_latex/expose_iv_10_14/SGA4_Expose_IV_sections_10_to_14_en.pdf`

Checks performed:

- `pdflatex` pass 1 completed.
- `pdflatex` pass 2 completed.
- `pdfinfo` reports a 23-page PDF.
- All 23 pages were rendered to PNG at 150 dpi using the project PDF render script.
- Pages 1, 12, and 23 were visually inspected for obvious rendering failures. No black boxes, clipped text, or gross layout failure were observed.

Known limitations:

- This package is fresh-only and does not include previous cumulative PDFs.
- Section 9 is not included in this ZIP; this package covers Sections 10-14 only.
- The translation is a working draft, not final proofread typography.
