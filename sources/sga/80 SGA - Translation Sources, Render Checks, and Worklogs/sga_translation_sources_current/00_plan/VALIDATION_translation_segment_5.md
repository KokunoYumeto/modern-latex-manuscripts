# Validation translation segment

## SGA 1-3 repair validation

The old SGA 1-3 raw Markdown/plain-text preview PDFs were moved out of the reading path. Replacement PDFs were compiled with XeLaTeX and broad Unicode fonts from the existing English snapshot LaTeX.

Page counts:

- SGA1 fixed: 321 pages.
- SGA2 fixed: 211 pages.
- SGA3 fixed: 1301 pages.

Rendered sample pages:

- SGA1: pages 1, 40, 300.
- SGA2: pages 1, 100, 210.
- SGA3: pages 1, 500, 1200.

The sample render PNGs are in `04_render_checks/translation segment/fixed_sga1_3/`.

Known remaining limitation: this repair fixes the rendering layer. It does not make the existing jcreinhold SGA 1-3 translation a proofed final edition. Formula blocks inherited as fenced text blocks may still need hand-normalization in a later editorial review pass.

## New SGA 4 validation

`SGA4_Expose_I_section_9_0_to_9_13_1_en.tex` compiled with pdfLaTeX in two passes. The PDF has 8 pages. Render checks were made on pages 1, 4, and 8 in `04_render_checks/translation segment/new_sga4_9/`.
