# Validation -- Batch current

Scope validated:

- New English TeX/PDF: `English/SGA6_strict_current_new_pages_047_075_en.*`.
- New French reconstruction TeX/PDF: `French/SGA6_strict_current_new_pages_047_075_fr.*`.
- Cumulative English and French TeX/PDF through source scan page 75.
- Original source scan slice pages 47-75 and cumulative source scan pages 1-75.

Build checks:

- All four reader PDFs compiled successfully with `pdflatex`.
- New English and new French PDFs rendered to PNG page images for visual inspection.
- Cumulative English and French PDFs were sample-rendered at the beginning and endpoint.
- The original source slice pages 47-75 were rendered/copied as page PNGs for source verification.

Reader-surface checks:

- No `\includegraphics`, `.png`, `sourceplate`, `\plate`, or screenshot/image placeholder tokens occur in the reader TeX.
- No process-note text or local filesystem paths are included in reader TeX.
- The source scan is packaged separately; the reader PDFs do not embed source screenshots.

Log notes:

- New English and new French builds have no overfull/underfull box reports in the retained compile logs.
- Cumulative builds are successful. The cumulative French log includes only tiny inherited box warnings from previously carried material; these do not affect the new batch endpoint.
