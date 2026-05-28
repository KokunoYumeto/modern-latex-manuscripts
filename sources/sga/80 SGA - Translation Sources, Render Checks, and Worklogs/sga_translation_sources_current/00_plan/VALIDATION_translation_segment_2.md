# Validation Report — translation segment

Artifact validated: `SGA4_Expose_I_sections_6_to_7_en.pdf`

## Compile

Command:

```bash
cd /mnt/data/sga_work/output/02_new_translation_latex/translation segment
latexmk -pdf -interaction=nonstopmode -halt-on-error SGA4_Expose_I_sections_6_to_7_en.tex
```

Result: successful.

PDF metadata:

- Pages: 13
- Page size: letter, 612 x 792 pt
- Producer: pdfTeX-1.40.26

Log scan:

```bash
grep -E 'Overfull|Underfull|Undefined|LaTeX Warning|Package .*Warning|pdfTeX warning|Missing character' SGA4_Expose_I_sections_6_to_7_en.log
```

Result: no matches.

## Render check

Command:

```bash
python /home/oai/skills/pdfs/scripts/render_pdf.py \
  /mnt/data/sga_work/output/02_new_translation_latex/translation segment/SGA4_Expose_I_sections_6_to_7_en.pdf \
  --out_dir /mnt/data/sga_work/output/04_render_checks/translation segment/SGA4_Expose_I_sections_6_to_7_en_render \
  --dpi 140
```

Result: 13 pages rendered.

Spot-inspected pages:

- page-01.png: title and Section 6 opening, no clipping or missing glyphs.
- page-06.png: Proposition 7.2 implication display, readable and not clipped.
- page-13.png: final Examples 7.13 page and closing continuation paragraph, no clipping or missing glyphs.
