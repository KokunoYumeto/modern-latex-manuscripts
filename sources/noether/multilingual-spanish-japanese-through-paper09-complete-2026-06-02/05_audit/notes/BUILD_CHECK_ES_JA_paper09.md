# Build check - Noether Paper 09 ES/JA

Scope: Paper 09 complete in Spanish and Japanese; cumulative outputs through Paper 09 complete.

Build engines:
- Spanish chunk: pdflatex, 14 pages.
- Japanese chunk: xelatex + xeCJK, 12 pages.
- German source excerpt: pdflatex, 14 pages.
- English control excerpt: pdflatex, 14 pages.
- Cumulative Spanish through Paper 09: pdflatex, 110 pages.
- Cumulative Japanese through Paper 09: xelatex + xeCJK, 102 pages.

Build result: all listed TeX files compiled successfully with halt-on-error. Render checks are included under `05_audit/render_checks/`.

Known benign warnings: Japanese XeLaTeX reports font-shape substitutions for math footnote sizes and CJK italics. One inherited Japanese cumulative overfull hbox appears in prior cumulative material; the Paper 09 chunk render checks show no clipping or broken glyphs.
