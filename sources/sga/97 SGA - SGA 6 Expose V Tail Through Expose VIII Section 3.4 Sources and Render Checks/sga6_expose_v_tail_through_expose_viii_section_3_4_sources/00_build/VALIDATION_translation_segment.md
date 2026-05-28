# Validation working draft section

PDFs compiled:

- `SGA6_Expose_V_2_3_4_to_Expose_VI_complete_en.pdf` — 33 pages.
- `SGA6_Expose_VII_complete_en.pdf` — 13 pages.
- `SGA6_Expose_VIII_opening_to_3_4_en.pdf` — 5 pages.
- `SGA6_batch031_reader_Expose_V_tail_to_Expose_VIII_3_4_en.pdf` — 51 pages.

Render check:

- Rendered the combined reader to PNG using `pdftoppm -png -r 140`.
- Produced 51 PNG pages in `04_render_checks/working draft section/SGA6_batch031_reader_render_pdftoppm/`.
- Visually checked the opening page, Exposé VI/VII transition, Exposé VII/VIII transition, and final page.

Known compile notes:

- There are minor overfull-box warnings in long mathematical displays; no fatal errors, missing glyphs, or undefined references were detected in the final reader.
