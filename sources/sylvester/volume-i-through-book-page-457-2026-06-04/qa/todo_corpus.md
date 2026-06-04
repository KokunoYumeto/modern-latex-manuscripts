# Sylvester corpus-level to-do overview

Current endpoint in this package: Volume I book p. 440.

Immediate continuation:
- Continue Volume I from book p. 441. The next pages are in Paper 57 and contain dense compound-determinant formulae; handle as source-driven TeX, not OCR promotion.
- Keep using the Volume I future-aid package for source PNG witnesses and page mapping through the end of Volume I.
- Preserve short folder names (`cum`, `new`, `old`, `qa`, `aid`, `verify`) for Windows/Codex path safety.

Volume-level reconstruction work still open:
- Finish Volume I from book pp. 441--658.
- Then process Volume II, Volume III, and Volume IV as separate cumulative volumes using their OCR/witness aid packages.
- For every batch: original-language TeX, rendered PDF, TXT, source scan PDF, one PNG witness per new page, and a coverage audit.

Corpus QA before publication/update:
- Check that every paper in each volume has source-page coverage.
- Check that every figure is redrawn as editable TeX/TikZ or otherwise encoded as a faithful diagram, not a screenshot.
- Check that every determinant, table, array, formula, marginal note, footnote, and multilingual section is represented.
- Build final volume-level paper indexes and a corpus-level manifest mapping paper number, title, original publication, book pages, source PDF pages, and output file paths.
- Run a final compile/render pass for each volume and package all final TeX/PDF/TXT/source-scan materials with checksums.

Intake status:
- No current source-search gap is open for Sylvester: future-aid/intake material covers Volume I from p. 269 onward and provides full witnessed packages for Volumes II-IV. The remaining work is transcription/reconstruction plus QA.
