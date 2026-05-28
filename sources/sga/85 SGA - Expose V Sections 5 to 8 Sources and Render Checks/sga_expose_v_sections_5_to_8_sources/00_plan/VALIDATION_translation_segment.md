# Validation - working draft section

## Compile

Command run from `02_new_translation_latex/working draft section/`:

```bash
pdflatex -interaction=nonstopmode -halt-on-error SGA4_Expose_V_sections_5_to_8_en.tex
pdflatex -interaction=nonstopmode -halt-on-error SGA4_Expose_V_sections_5_to_8_en.tex
```

Result: successful compilation to `SGA4_Expose_V_sections_5_to_8_en.pdf`.

## PDF

- Page count: 31 pages.
- Page size: Letter, 612 x 792 pt.
- Render-check directory contains all 31 rendered pages.

## Known warnings

- One minor overfull hbox remains in the proof around Proposition 6.10. It does not prevent rendering and no text clipping was observed in the checked renders.
- This is a working translation draft, not a final line-edited edition.
