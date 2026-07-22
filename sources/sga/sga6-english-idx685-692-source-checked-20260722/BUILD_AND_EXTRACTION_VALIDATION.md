# Build, extraction, and render validation

The publication-facing TeX was built in three isolated pdfLaTeX passes. All
three exited successfully. The converged log contains zero TeX errors, LaTeX or
package warnings, overfull boxes, and underfull boxes.

The PDF has seven 612 x 792 pt US Letter pages. All 27 font rows are embedded,
subset, and Unicode-mapped. It is unencrypted, has no JavaScript, forms, or
attachments, is untagged, and has no XMP metadata stream.

Layout-aware UTF-8 extraction contains 23,374 bytes, seven ordinary form-feed
page separators, and zero forbidden control bytes. The producer PDF contained
two U+0001 bytes because the Latin Modern `parenrightbig` glyph lacked a
ToUnicode mapping. The successor adds mappings for `parenleftbig` and
`parenrightbig`; no translation-body text or visible typesetting changed.

The producer and successor PDFs were independently rendered at 200 dpi. All
seven corresponding PNG files are byte-identical, and all seven pages were
visually inspected. No clipping, overlap, missing glyph, broken formula,
diagram defect, or page-seam defect was found.

The exact producer review remains `review/INDEPENDENT_FINAL_REVIEW.md`. Its
three source-fidelity corrections are present in the successor unchanged.

