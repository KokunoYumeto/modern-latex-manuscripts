# SGA6 French Source-Rescribe Workpass: idx540

This package freezes the active pagewise French source-rescribe workpass at `CERT_LOG.md` entry #537, scan index 540, volume p. 527, Expose X p. 9. The next unchecked page is scan index 541, volume p. 528, Expose X p. 10.

The fuller source-witness, render-check, and build-log package is published at Zenodo record [`21364946`](https://doi.org/10.5281/zenodo.21364946).

## What This Update Adds

Relative to the preceding public freeze at entry #439 / scan index 442, this package adds 98 directly checked source pages, scan indexes 443-540. The linear pass finishes Expose VII, checks all of Exposes VIII and IX, and reaches Expose X p. 9.

The ledger records source-level restoration of omitted clauses and proofs, reversal of paraphrases, repair of formulas and indices, and page-local decisions about notation, arrows, punctuation, emphasis, and book errors. The current frontier repair includes the source-backed formula

`x * w in Filt_{j-i-1}(X)`

rather than the earlier incorrect filtration index. `CERT_LOG.md` is the detailed evidence trail; it is not a substitute for the corrected TeX, whose edits are already applied.

Material after scan index 540 remains inherited and unchecked scaffold. Its presence in the compiled reader is not a source-check claim. The reader page count is also not a completion metric because source restoration and layout reflow can add or remove output pages.

## Files

- `sga6_fr_workpass.tex` and `.pdf`: current French publication freeze.
- `CERT_LOG.md`: pagewise source-comparison ledger and exact next cursor.
- `ERRATA_SGA6.md`: running book-versus-edition decisions.
- `compile_logs/`: two clean short-path publication builds and the full LaTeX log.
- `source_witness/SGA6_source_idx443_540.pdf`: 98-page high-resolution source witness for this public delta.
- `source_witness/boundary_pages/`: the last two checked source pages and the next unchecked source page.
- `render_checks/`: rendered output pages around the current source boundary.
- `publication_pdf_text.txt`: extracted PDF text used for readback checks.
- `PACKAGE_SHA256.csv`: package integrity manifest.

## Build And Readback Notes

The publication copy makes only source-equivalent typesetting repairs beyond the active workpass: robust math-mode rendering of the diaeresis in `naif`, and a line break/continuation alignment in a long filtration display. These do not alter the mathematical content.

The final build was made from a short ASCII working directory to avoid stale-output failures on long Windows paths. The resulting 383-page PDF has zero fatal errors, zero overfull boxes, zero underfull boxes, and no invalid math-mode accent warning. PDF text extraction confirms the previously fragile `L'anneau A_0...` sentence and the current-boundary filtration formula are present in the rendered output.

## Classification

This is substantive source-rescribe/workpass provenance and a useful current French working reader. It is **not** a completed SGA6 edition, critical edition, whole-volume source-faithfulness certification, synchronized English edition, publication-grade proofread edition, or diagram-by-diagram certification. SGA5 remains incomplete and error-bearing. SGA7 remains partial and caveat-heavy.
