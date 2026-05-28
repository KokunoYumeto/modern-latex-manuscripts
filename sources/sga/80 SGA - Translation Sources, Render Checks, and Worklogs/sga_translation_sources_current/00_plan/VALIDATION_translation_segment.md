# Validation Report — translation segment

## Files checked

- `02_new_translation_latex/translation segment/SGA4_Expose_I_sections_2_to_5_en.tex`
- `02_new_translation_latex/translation segment/SGA4_Expose_I_sections_2_to_5_en.pdf`

## Compile check

Command:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error SGA4_Expose_I_sections_2_to_5_en.tex
```

Result: successful.

PDF output: 19 pages.

## Render check

Command:

```bash
python /home/oai/skills/pdfs/scripts/render_pdf.py \
  SGA4_Expose_I_sections_2_to_5_en.pdf \
  --out_dir 04_render_checks/translation segment/SGA4_Expose_I_sections_2_to_5_en_render \
  --dpi 140
```

Result: 19 page images rendered.

Spot-inspected pages: 1, 10, 19.

Observed status: readable output; no clipped text, no black squares, no missing diagrams on inspected pages.
