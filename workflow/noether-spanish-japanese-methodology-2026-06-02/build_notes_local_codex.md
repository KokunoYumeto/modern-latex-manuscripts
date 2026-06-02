# Local Codex build notes

Spanish standalone and cumulative:

```bash
pdflatex -interaction=nonstopmode -halt-on-error Noether_Paper06_sections07_15_ES.tex
pdflatex -interaction=nonstopmode -halt-on-error Noether_Cumulative_ES_through_Paper06_section15.tex
```

Japanese standalone and cumulative:

```bash
lualatex -interaction=nonstopmode -halt-on-error Noether_Paper06_sections07_15_JA.tex
lualatex -interaction=nonstopmode -halt-on-error Noether_Cumulative_JA_through_Paper06_section15.tex
```

On a fresh TeX Live image the first Japanese cumulative pass may spend time rebuilding the LuaTeX font database. Retry before treating that startup delay as a document error. In this packet, the later Japanese cumulative passes completed successfully and produced the shipped 100-page PDF directly from the shipped cumulative TeX.

Render checks used here follow the render-first PDF workflow: selected first/middle/last pages for chunks and tail pages for cumulative outputs.
