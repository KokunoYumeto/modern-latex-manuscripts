# GPU/VLM Table Cell Reader Note - 2026-06-03

This note records a local workflow experiment for dense historical mathematical and astronomical tables.

## Current Local Stack

- Hardware noted by the local al-Battani lane: NVIDIA RTX 4080 SUPER, 16 GB VRAM.
- CUDA PyTorch stack reported working: `torch 2.6.0+cu124`.
- Initial target: Carlo Alfonso Nallino's edition of al-Battani, especially the star-catalogue tables where ordinary OCR does not reliably read abjad numerals.
- Working directory reported locally: `C:\Users\Floris\Documents\CLAUDE PLEASE DONT DELETE WINDOWS 32\albattani_work\`.
- Source scan reported locally: `albattani_work\source_scan\nallino_1899_albattanisivealb00batt.pdf`.

## Intended Use

The vision-language model is an assistive witness layer, not an edition authority.

Recommended loop:

1. Render the table page locally.
2. Crop by cell or small row/column group.
3. Ask the local VLM to produce a first-pass reading of the cell.
4. Compare against scan context, known table structure, and neighbouring rows.
5. Promote only verified values into CSV/TeX.
6. Record uncertain cells explicitly instead of guessing.

This is most useful where the expensive part is repeated visual reading of small cells and where the table has a strong external structure, such as star catalogues, Cayley invariant-theory tables, or Sylvester/Cayley determinant arrays.

## Non-Use

- Do not paste VLM output directly into public TeX without source comparison.
- Do not use screenshots as the public edition layer.
- Do not treat a clean compile as proof that numerals or coefficients are correct.
- For prose-heavy pages with good `pdftotext`, use text extraction first and reserve vision for formulas, diagrams, tables, or damaged glyphs.

## Relation To Earlier Formula-Crop Work

This extends the same policy used in the Sylvester and Cayley assist packets: crops and candidate readings are localization/checking aids. Edition-grade output remains native TeX/CSV/PDF with a scan-audit note.
