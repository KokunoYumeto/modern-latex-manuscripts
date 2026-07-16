# SGA6 Expose X English restart through idx537

## Promoted range

- Expose X, printed volume pages 519-524.
- Source-PDF pages 526-531 in the imported witness packet.
- Current rescribe indices 532-537.
- Content: title; Sections 1.1 and 1.2; Section 1.3 through the opening equality in Case I of the proof of Theorem 1.3.2.

## Authority and method

The English text was checked against all six source-scan pages and the current French source-rescribe. The older English Expose X file was used only as a translation control. It was not promoted wholesale because a full comparison against the current French rescribe shows substantive mathematical differences later in the expose.

Direct inspection of printed page 523 also caught one remaining current-French rescribe typo: the source reads coherent `\mathcal O_X`-module, while the idx608 French TeX currently says `\mathcal C_X` at that location. The English tranche follows the scan. The finding is recorded in `SOURCE_CORRECTION_LEDGER.csv`.

## Status

This is a source-checked working translation tranche, not a critical edition and not a declaration that Expose X or SGA6 English is complete. The next continuation point is printed page 525 / source-PDF page 532 / current rescribe index 538, continuing Case I of the proof of Theorem 1.3.2.

## Build and visual QA

The English TeX compiles to three A4 pages with pdfLaTeX. The final log has zero TeX errors, zero overfull boxes, and zero underfull boxes. All three rendered pages were visually checked for clipping, formula overflow, and missing glyphs. The build and page-render checks are recorded in `BUILD.log` and `render_check/`. See `MANIFEST.csv` and `SHA256SUMS.csv` for the package contents.
