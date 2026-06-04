# Example commands

Render source pages 1--10 of a per-paper PDF:

```bash
python scripts/render_pdf_pages.py 06_Formes_modulaires_et_representations_l_adiques.pdf renders/p001_010 --from-page 1 --to-page 10 --dpi 220
```

Extract the scan sidecar:

```bash
python scripts/extract_scan_pages.py 06_Formes_modulaires_et_representations_l_adiques.pdf SCAN/Deligne_006_p001_010_SCAN.pdf --from-page 1 --to-page 10
```

Compile TeX:

```bash
python scripts/compile_latex_twice.py TEX/Deligne_006_p001_010_EN.tex
python scripts/compile_latex_twice.py TEX/Deligne_006_p001_010_FR.tex
```

Audit a clean package folder:

```bash
python scripts/audit_tex_pdf_package.py Deligne_006_Formes_modulaires_l_adiques_p001_010_with_cumulative
```
