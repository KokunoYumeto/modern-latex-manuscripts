# SGA 6 French Source-Rescribe Workpass: idx684

This package freezes the active pagewise French source-rescribe workpass at
`CERT_LOG.md` entry #715, source-scan index 684, volume p. 671, Expose XIV
p. 5. The next page in the linear pass is source-scan index 685, volume p.
672, Expose XIV p. 6.

The grouped reader/source/audit package is published under the permanent SGA
concept DOI [`10.5281/zenodo.20410947`](https://doi.org/10.5281/zenodo.20410947).

## What This Update Adds

Relative to the preceding public French freeze at source index 662, this
package adds twenty-two processed source pages, indices 663--684 inclusive.
The pass completes the current Expose XIII segment and reaches Expose XIV
section 3.3. It restores source-visible clauses, citations, emphasis,
punctuation, notation, and formula content. One material correction on the
frontier page changes the inherited erroneous `A^2(Z)=Pic(Z)` to the
source-visible and mathematically correct `A^1(Z)=Pic(Z)`.

The exact interventions, open systematic repairs, source anomalies, and next
cursor are recorded in `CERT_LOG.md` and `ERRATA_SGA6.md`. The ledger is part
of the evidence, not a completion certificate. In particular, entry #715
retains explicit deferred work involving footnote structure, a parenthesis
spanning idx684--685, and one display requiring another source adjudication.

Material beyond idx684 remains inherited scaffold and is not source-checked
by its presence in the compiled reader. Reader page count is not a completion
metric because source restoration and layout reflow change pagination.

## Files

- `sga6_fr_workpass.tex` and `.pdf`: publication release snapshot.
- `sga6_fr_workpass_upstream_snapshot.tex` and `.pdf`: exact active upstream
  snapshot before three release-only TeX hygiene substitutions.
- `RELEASE_TEX_HYGIENE.patch`: the complete upstream-to-release TeX diff.
- `CERT_LOG.md`: pagewise source-comparison ledger and exact next cursor.
- `ERRATA_SGA6.md`: running book-versus-edition decisions.
- `source_witness/SGA6_source_idx663_684.pdf`: twenty-two-page high-resolution
  source delta added since the preceding public freeze.
- `source_witness/boundary_pages/`: previous public frontier, current
  frontier, and next source page.
- `render_checks/`: output pages around the current frontier and a source-to-
  output contact sheet.
- `compile_logs/`: independent two-pass release build and PDF inspection.
- `publication_pdf_text.txt`: extracted PDF text used for readback checks.
- `PACKAGE_SHA256.csv`: package integrity manifest.

## Build And Readback Notes

The release TeX was rebuilt twice with pdfLaTeX. The resulting PDF has 374 A4
pages and embedded fonts. It has no fatal errors, overfull boxes, underfull
boxes, missing-character warnings, or unresolved references. One nonfatal
duplicate-footnote destination warning remains and is disclosed in the build
log; it is not silently described as a warning-free build.

The release-only TeX substitutions replace three inconsistent spellings of
`naif` with the document's existing `\naif` macro. They do not alter wording
or mathematical content. The upstream file and a complete diff are retained.

The contact sheet aligns source idx684 / volume p. 671 with compiled reader
page 357. The adjacent output renders make the pagination boundary inspectable
without claiming that idx685 has already been processed.

## Classification

This is a substantive source-rescribe checkpoint and useful current French
working reader. It is **not** a completed SGA 6 edition, critical edition,
whole-volume source-faithfulness certification, synchronized whole-volume
translation, publication-grade proofread edition, or diagram-by-diagram
certification. SGA 5 also remains a working edition with known residual
errors. SGA 7 remains partial and caveat-heavy.
