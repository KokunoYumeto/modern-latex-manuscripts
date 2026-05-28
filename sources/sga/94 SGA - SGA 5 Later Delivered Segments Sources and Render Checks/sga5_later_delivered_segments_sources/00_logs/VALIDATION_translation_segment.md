# Validation -- working draft section

LaTeX validation:

- The bridge TeX file was compiled with `pdflatex` in two passes.
- The continuation TeX file was compiled with `pdflatex` in two passes.
- The bridge PDF reports 39 pages via `pdfinfo`.
- The continuation PDF reports 42 pages via `pdfinfo`.
- The combined reader PDF reports 81 pages via `pdfinfo`.

Render validation:

- The combined 81-page reader PDF was rendered page-by-page to PNG at 72 DPI with `pdftoppm`.
- Rendered PNG count: 81.
- Spot checks were performed on the opening page, the bridge/continuation boundary pages, and the final page.

Known packaging note:

- The package is fresh-only and does not include prior SGA 4 or earlier SGA 5 material.
- It includes source extracts for auditability.
