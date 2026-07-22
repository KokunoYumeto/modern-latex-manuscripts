# Build, extraction, and render validation

The publication-facing TeX was built in three isolated pdfLaTeX passes. All
three exited successfully. The converged log contains zero TeX errors, LaTeX
or package warnings, overfull boxes, and underfull boxes.

The PDF has seven 612 x 792 pt US Letter pages. All 26 font rows are embedded,
subset, and Unicode-mapped. It is unencrypted, has no JavaScript or forms, is
untagged, and has no XMP metadata stream.

Layout-aware UTF-8 extraction contains 22,440 bytes, seven ordinary form-feed
page separators, and zero forbidden control bytes. The producer PDF contained
two U+0001 bytes because Latin Modern's `parenrightbig` glyph lacked a
ToUnicode mapping. The successor adds mappings for `parenleftbig` and
`parenrightbig`; no translation-body text or visible typesetting changed.

The producer and successor PDFs were rendered at 160 dpi. All seven
corresponding PNG files are byte-identical, and all seven pages were visually
inspected. No clipping, overlap, missing glyph, broken formula, diagram
defect, bibliography defect, terminal-note defect, or page-seam defect was
found.

The exact producer review remains
`review/INDEPENDENT_FINAL_REVIEW.md`. Its final PASS and the two disclosed
source-defect policies are present in the successor unchanged.

