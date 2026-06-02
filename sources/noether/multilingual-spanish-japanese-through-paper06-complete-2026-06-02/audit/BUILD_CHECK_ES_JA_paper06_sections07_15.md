# Build check: Noether Paper 06 §§7-15 ES/JA

## Standalone chunk builds

- Spanish chunk: `pdflatex`, 13 pages.
- Japanese chunk: `lualatex`, 14 pages.
- German source excerpt: `pdflatex`, 13 pages.
- English control excerpt: `pdflatex`, 13 pages.

## Cumulative builds

- Cumulative Spanish through Paper 06 §15: `pdflatex`, 88 pages.
- Cumulative Japanese through Paper 06 §15: `lualatex`, 100 pages.

The first Japanese cumulative LuaLaTeX pass rebuilt the LuaTeX font database and did not complete within the initial short run; subsequent passes completed successfully. The shipped Japanese cumulative PDF is the direct LuaLaTeX build from the shipped cumulative TeX, not a PDF-concatenation fallback.

## Log scan

No fatal LaTeX errors, undefined-control-sequence errors, emergency stops, or missing-glyph messages were found in the final build logs. One inherited overfull hbox is present in the cumulative Japanese log from prior cumulative material; it is not introduced by the current chunk and does not affect the checked current pages.

## Render checks

Render-check PNGs are included under:

- `audit/render_checks/spanish_chunk/`
- `audit/render_checks/japanese_chunk/`
- `audit/render_checks/german_source/`
- `audit/render_checks/english_control/`
- `audit/render_checks/spanish_cumulative_tail/`
- `audit/render_checks/japanese_cumulative_tail/`
