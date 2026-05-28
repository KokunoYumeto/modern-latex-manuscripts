# Validation translation segment

Fresh translation checked:

- `02_new_translation_latex/translation segment/SGA4_Expose_III_complete_en.tex`
- `02_new_translation_latex/translation segment/SGA4_Expose_III_complete_en.pdf`

Checks performed:

1. `pdflatex` was run twice on the main TeX file.
2. `pdfinfo` reports 22 pages for the fresh Exposé III PDF.
3. All 22 pages of the fresh Exposé III PDF were rendered to PNG under `04_render_checks/translation segment/SGA4_Expose_III_complete_render_pdftoppm_full/`.
4. A cumulative SGA 4 progress PDF was rebuilt by concatenating the translation segment cumulative reader through Exposé II with the fresh Exposé III PDF.
5. `pdfinfo` reports 175 pages for the cumulative SGA 4 progress reader through Exposé III.
6. PNG render checks were generated for the cumulative Exposé II/III boundary and final page under `04_render_checks/translation segment/SGA4_progress_with_Expose_III_sample_render/`.
7. Representative rendered pages of the fresh and cumulative PDFs were inspected visually for obvious clipping, overlaps, or broken glyphs.

Known status:

- The translation is a working draft intended for mathematical readability and continued revision.
- The rendered PDFs are present so typographic or mathematical display problems can be caught visually.
- SGA 1--3 remain repaired renderings of inherited existing English translations, not newly proofed editions.
