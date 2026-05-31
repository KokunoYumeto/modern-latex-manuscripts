# Fidelity note - Paper 032 corrected package

Paper: Pierre Deligne, *La conjecture de Weil. II* / *The Weil Conjecture. II*.

Status of this package: source-layer correction plus English rebuild. The French/source PDF is now the original-language source extraction from the uploaded *Collected Papers* volume, pages 1026-1141 inclusive, 116 pages. The prior 99-page French/source layer is superseded; it was a re-typeset working layer and should not have been represented as the source-complete original layer.

English layer: rebuilt from the prior complete working TeX. In this pass I corrected the visible mathematical error in Theorem (6.2.13), where an OCR-derived `1/2(n-i)` had appeared; the source condition is `n-i`. The English PDF now recompiles cleanly to 74 pages.

Verification performed:

- Source Collected Papers page count: 3300.
- Paper 032 source extraction: PDF pages 1026-1141 inclusive.
- FR/source corrected PDF page count: 116.
- English corrected PDF page count: 74.
- Boundary check against source pages: first, second, middle, and last extracted pages checked against the corresponding source pages.
- Selected render smoke check performed for first/middle/last pages of both PDFs outside the package.

This package does not include screenshots or render images.
