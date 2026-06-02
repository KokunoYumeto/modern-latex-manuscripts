# Local Codex build notes

Scope: Spanish/Japanese cumulative lane through Paper 08 complete.

## Spanish standalone and cumulative

```bash
pdflatex -interaction=nonstopmode -halt-on-error Noether_Papers07_08_ES.tex
pdflatex -interaction=nonstopmode -halt-on-error Noether_Cumulative_ES_through_Paper08_complete.tex
```

## Japanese standalone and cumulative

This packet builds Japanese with XeLaTeX because the local LuaHBTeX/luaotfload run did not complete reliably in this session.

```bash
xelatex -interaction=nonstopmode -halt-on-error Noether_Papers07_08_JA.tex
xelatex -interaction=nonstopmode -halt-on-error Noether_Cumulative_JA_through_Paper08_complete.tex
```

Required fonts in the tested build: `Noto Serif`, `Noto Serif CJK JP`, and `Noto Sans CJK JP`.

## Source/control excerpts

```bash
pdflatex -interaction=nonstopmode -halt-on-error Noether_Papers07_08_DE_source.tex
pdflatex -interaction=nonstopmode -halt-on-error Noether_Papers07_08_EN_control.tex
```

## Render checks

Render checks used here follow the render-first PDF workflow. The shipped package contains full standalone chunk renders for Spanish/Japanese and selected tail renders for cumulative outputs. Source/control first and final pages are also rendered for quick local verification.
