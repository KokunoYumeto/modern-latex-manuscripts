# Noether German source-control mirror: v26 plus R822

This compact GitHub mirror belongs to the permanent Noether concept DOI [10.5281/zenodo.20412587](https://doi.org/10.5281/zenodo.20412587).

## Current Head

- `Noether_German_Cumulative_v26_R822integrated_20260717.pdf`: 466-page German working reader.
- `Noether_German_Cumulative_v26_R822integrated_20260717.tex`: editable current source.
- `Noether_German_Cumulative_v26_R822integrated_20260717.txt`: extracted-text comparison aid.
- `PACKAGE_BUILD_SUMMARY_v26_R822.md`: compact build and integration summary.

## R822 Integration

The current head begins with the v26/R821 source-control reader and replaces only Paper 20 with the sealed R822 Paper 20 text. R822 contributes four direct-source refinements across printed pages 26, 28, 29, and 31: a dropped footnote sentence-bridge dash, the source two-line semicolon structure of display (4), the final semicolon in display (8), and German quotation marks in footnote 10. No OCR text was promoted.

`r822_p20_integration/` contains the R821 base, sealed R822 input, guarded integration script, exact Paper 20 diff, source-facing audit tables and images, two-pass build logs, and rendered checks around output pages 218-223. The report proves that text outside Paper 20 is byte-for-byte unchanged and that integrated Paper 20 exactly matches the sealed R822 text. Pixel comparison shows changes only on output pages 218-220; pages 221-223 reconverge exactly to R821.

`r821_p20_integration/` and `historical_r819_p20_integration/` preserve the preceding compact R818-R821 evidence. `audits/`, `render_checks/`, and `source_witnesses/` preserve the v20-v26 targeted Papers 34-43 evidence inherited from the prior head. Larger raw web packages remain immutable in earlier Zenodo versions.

## Build And Status

The integrated TeX compiled twice with XeLaTeX to 466 A4 pages. The final log has zero fatal errors, zero overfull boxes, zero underfull boxes, and no unresolved-reference warnings. Output pages 218-223 were rendered and checked against both R821 and the supplied source evidence.

This is a working source-control corpus, not a critical edition, author-wide source-faithfulness certification, paper-by-paper certification, complete multilingual synchronization, or publication-grade proofreading. The retained English and multilingual readers on Zenodo predate some German repairs.
