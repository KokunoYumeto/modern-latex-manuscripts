# Validation — translation segment

## Compilation

`SGA4_Expose_I_sections_8_9_to_8_13_en.tex` was compiled twice with `pdflatex -interaction=nonstopmode -halt-on-error`.

Result: success.

Output PDF:

- `02_new_translation_latex/translation segment/SGA4_Expose_I_sections_8_9_to_8_13_en.pdf`
- Page count: 16

## Rendering

The fresh translation segment PDF was rendered to PNG at 120 dpi using the PDF skill render workflow:

- `04_render_checks/translation segment/SGA4_Expose_I_sections_8_9_to_8_13_en_render/`

A cumulative SGA 4 Exposé I PDF through Section 8.13 was produced by concatenating the prior cumulative PDF through Section 8.8 with the translation segment PDF:

- `02_new_translation_latex/cumulative/SGA4_Expose_I_sections_0_to_8_13_cumulative_en.pdf`
- Page count: 79

Sample pages from the cumulative PDF were rendered:

- page 1
- page 64, the first page of the new translation segment segment
- page 79, the final page of the cumulative PDF

## Status

The new TeX compiles, the new PDF renders, and the cumulative PDF opens and renders at sampled boundary pages. This is still a draft translation and has not been proofread line-by-line against the scanned original.
