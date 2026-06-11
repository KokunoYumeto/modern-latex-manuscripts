# Noether final audit report - numbered papers 1--43

## Scope audited

- Final cumulative English and original German TeX/PDF through complete numbered Paper 43.
- Source PDF page coverage: pages 41--724, divided into 43 source paper slices in `source_paper_slices/`.
- Front matter, editorial prefaces, title pages, and non-paper lists are not included in the numbered-paper cumulative files.

## Completion status

- Expected numbered papers: 43.
- English cumulative section headings detected: 31 distinct numbered papers.
- German cumulative section headings detected: 31 distinct numbered papers.
- Source page coverage table: `audit/SOURCE_PAGE_COVERAGE_NUMBERED_PAPERS.csv`.

## Build and TeX audit

- Both audited cumulative TeX files compile to PDF.
- Standalone Paper 34 product-table patch files compile to PDF.
- No `\includegraphics`, `.png`, `sourceplate`, or page-plate tokens are present in the audited TeX files.
- Build details are in `audit/BUILD_CHECK_FINAL_AUDITED.txt`.

## Visual-object audit

Keyword/visual sweep over source pages 41--724 found the following source indicators:

- Tabelle: pages [45, 47]
- Multiplikationstafel/Produkttafel: pages [591, 596, 626]
- Figur/Abbildung/Diagramm: pages [166, 167, 168, 171, 176, 178, 181, 182, 183, 185, 186, 188, 189, 191, 193, 228, 235, 236, 237, 238, 239, 240, 241, 242, 244, 352, 353, 355, 404, 497, 583, 584, 601, 659, 660, 663, 677, 680, 707, 711, 712, 715]

Audited visual/mathematical layout objects are itemized in `audit/VISUAL_OBJECT_AUDIT_TABLES_FIGURES_DIAGRAMS.csv`.

The audit found one omission in the prior cumulative version: the product table on source page 626 in Paper 34. It has been restored in this audited package in both English and German cumulative TeX/PDF and is also provided as a standalone patch under `patches/`.

No standalone diagrams or figures requiring vector reconstruction were found in the numbered-paper source pages during this pass. Displayed mathematics, matrices, arrays, ideal decompositions, and the explicit tables noted above are set as TeX, not as screenshots.

## Post-numbered material

The source volume continues after Paper 43 with non-numbered material. This is registered in `audit/POST_NUMBERED_MATERIAL_REGISTER.md`. It is not part of the numbered-paper cumulative files.
