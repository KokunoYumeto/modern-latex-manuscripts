# Noether Paper 43 completion plus recursive audit start

Scope completed in this package:

- Paper 43 complete: `Idealdifferentiation und Differente`.
- Spanish and Japanese standalone translations.
- Spanish and Japanese cumulative PDFs/TeX now through Paper 43, completing the numbered Noether corpus in this branch.
- English and German cumulative PDFs/TeX carried forward through Paper 43 with the Paper 02 A4 table cleanup preserved.
- Recursive source-audit pass started from Paper 01; the first audit note is under `06_back/p01/P01_audit.md`.

Package policy: one ZIP, one root folder, then subfolders only. Internal path names are deliberately short for Windows/local Codex path safety.

Main outputs:

- `01_work/es/N43_ES.pdf` and `.tex`
- `01_work/ja/N43_JA.pdf` and `.tex`
- `02_cum/es/N43_cum_ES.pdf` and `.tex`
- `02_cum/ja/N43_cum_JA.pdf` and `.tex`
- `04_ctrl/cum_en/N43_cum_EN.pdf` and `.tex`
- `04_ctrl/cum_de/N43_cum_DE.pdf` and `.tex`

The English standalone control `04_ctrl/en/N43_EN.tex` is a source-aligned checked control. The original source-provided English control is preserved as `04_ctrl/en/N43_EN_src_orig.tex`.
