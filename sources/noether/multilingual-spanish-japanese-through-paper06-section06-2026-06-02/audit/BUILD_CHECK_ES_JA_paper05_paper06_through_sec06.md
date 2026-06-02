# Build check - Noether Paper 05 and Paper 06 through §6

Final PDF page counts:
- Spanish chunk: 12 pages
- Japanese chunk: 14 pages
- German source excerpt: 13 pages
- English control excerpt: 12 pages
- Spanish cumulative: 75 pages
- Japanese cumulative: 86 pages

Compile/assembly methods:
- Spanish standalone chunk: pdflatex, carried over from working build.
- Japanese standalone chunk: lualatex, carried over from working build.
- German source excerpt and English control excerpt: pdflatex, carried over from working build.
- Spanish cumulative: pdflatex from the cumulative TeX.
- Japanese cumulative: pdfunite assembly from previous cumulative + current standalone chunk; cumulative TeX is included.

Render checks:
- Selected pages were rendered with pdftoppm at 150 DPI.
- Rendered pages are stored under audit/render_checks/.

No declared translation gaps in the completed range.
