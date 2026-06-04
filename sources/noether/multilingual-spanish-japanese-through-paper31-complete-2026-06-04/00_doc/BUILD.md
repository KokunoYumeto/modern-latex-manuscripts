# Build check

Page counts:
- Spanish standalone: 13 pages.
- Japanese standalone: 11 pages.
- German source/control: 13 pages.
- English control: 12 pages.
- Source scan witness: 23 pages.
- Cumulative Spanish through Paper 31: 304 pages.
- Cumulative Japanese through Paper 31: 272 pages.

Compile commands used:
- `pdflatex -interaction=nonstopmode -halt-on-error N31_ES.tex`
- `xelatex -interaction=nonstopmode -halt-on-error N31_JA.tex`
- `pdflatex -interaction=nonstopmode -halt-on-error N31_DE.tex`
- `pdflatex -interaction=nonstopmode -halt-on-error N31_EN.tex`
- `pdflatex -interaction=nonstopmode -halt-on-error N31_cum_ES.tex`
- `xelatex -interaction=nonstopmode -halt-on-error N31_cum_JA.tex`

Log scan: current translation/cumulative logs report no overfull or underfull hboxes. Japanese logs contain only normal font-substitution warnings for small math/CJK italic shapes.
