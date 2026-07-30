# RA08 scan-first recursive audit: Paper 37 restoration

Scope: Paper 37, `Normalbasis bei Körpern ohne höhere Verzweigung`, with actual scan witness checked first. The package continues the corrected protocol: scan -> German transcription -> English/Spanish/Japanese propagation. Page-number agreement was not treated as evidence of correctness.

## Result

Paper 37 had a substantive source-level gap in the cumulative branch. The German cumulative text was an abridged recasting rather than a complete scan-faithful transcription. English, Spanish, and Japanese inherited the same omission pattern. This package restores Paper 37 across all four languages.

The restored German branch now follows the scan-visible structure:

- title and journal line;
- the full opening theorem on existence of normal bases at places whose prime does not divide the degree;
- all source-visible footnotes, including the Speiser, Artin, Hasse, Deuring, Noether, Hilbert, and Klein/Speiser notes;
- the Deuring example in the former `2a` source note;
- §§1--3 in full;
- the direct-sum enlargement formula involving `E^{(1)}`;
- the module action formula;
- the operator-isomorphism mapping and vector representation display;
- the group determinant formula `D=|w^{ST^{-1}}|`;
- the `M_lambda`, `D_lambda`, `Delta_lambda`, and root-number ideal formulas;
- the received line, `Eingegangen 24. August 1931.`

English, Spanish, and Japanese were retranslated from the restored German/source structure rather than merely patched against the prior abbreviated text.

## Build status

Standalone Paper 37 builds: DE 4 pages, EN 4 pages, ES 5 pages, JA 4 pages.

Cumulative builds after restoration: DE 383 pages, EN 376 pages, ES 392 pages, JA 350 pages.

All current standalone and cumulative logs report zero overfull and zero underfull hboxes. Japanese has only normal font-shape substitutions.

## Layout carry-forward

The earlier Paper 02 table cleanup remains carried forward. Cumulative pages 39--40 were rendered again for all four languages and remain standard A4 portrait pages with editable TeX tables.

## Open recursive targets found, not hidden

Granular scan inspection of the next files found that Papers 38 and 39 also require real source restoration. Their scans contain source-visible footnotes and citation blocks, while the current cumulative Paper 38 and Paper 39 segments have zero LaTeX footnotes in the German branch and therefore cannot be treated as complete source transcriptions. These are recorded as the next immediate targets.

Paper 40--43 were not declared clean in this package; they remain in the continuing scan-first queue after Papers 38--39.

## Package contents

- `01_scan/`: Paper 37 scan and OCR witness, plus OCR witnesses for Papers 38--39 as next-target evidence.
- `02_seg/`: restored standalone Paper 37 TeX/PDF for DE/EN/ES/JA.
- `03_cum/`: rebuilt cumulative TeX/PDF for DE/EN/ES/JA.
- `04_diff/`: old-vs-restored Paper 37 segment diffs and cumulative diffs.
- `05_rend/`: render checks for standalone Paper 37 and selected cumulative pages, including table pages 39--40.
- `06_log/`: LaTeX logs and run logs.
- `07_data/`: build matrix, structural counts, and SHA256 manifest.
- `08_meth/`: methodology note, including the updated scan-first audit rule.
