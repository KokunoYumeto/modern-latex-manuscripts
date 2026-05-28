# Validation -- translation segment

## Compile checks

- `SGA4_Expose_XVIII_section_3_and_XIX_complete_en.tex` compiled cleanly with `pdflatex` in two passes.
- `SGA5_Expose_I_introduction_sections_1_to_2_en.tex` compiled cleanly with `pdflatex` in two passes.
- The two PDFs were joined with `pdfunite` into the 50-page batch reader.

## Render checks

- Rendered the full 50-page reader PDF to PNG at 140 DPI using `/home/oai/skills/pdfs/scripts/render_pdf.py`.
- Render folder: `04_render_checks/translation segment/SGA4_completion_and_SGA5_start_batch026_reader_render/`.
- Rendered page count: 50 PNG files.
- Sample visual checks: pages 1, 35, 36, and 50.

## Source coverage

- SGA 4, Exposé XVIII: source lines 4691--5928.
- SGA 4, Exposé XIX: source lines 1--1920.
- SGA 5, Exposé I: source lines 468--866.

## Notes

The SGA 4 portion completes the current working English LaTeX draft of SGA 4. The SGA 5 portion starts the next volume and continues past the previously delivered volume front matter.
