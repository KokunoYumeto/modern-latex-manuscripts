# SGA6 French Source-Rescribe Workpass: idx646

This package freezes the active pagewise French source-rescribe workpass at `CERT_LOG.md` entry #663, scan index 646, volume p. 633, Expose XIII p. 18. The next unchecked page is scan index 647, volume p. 634, Expose XIII p. 19.

The grouped reader/source/audit package is published at Zenodo record [`21416482`](https://doi.org/10.5281/zenodo.21416482), under the permanent SGA concept DOI [`10.5281/zenodo.20410947`](https://doi.org/10.5281/zenodo.20410947).

## What This Update Adds

Relative to the preceding public freeze at entry #662 / scan index 645, this package adds one directly checked source page, scan index 646. The linear pass now continues Expose XIII through p. 18.

On p. 633 the source comparison restores the exact connector and sentence structure in the proof of Proposition 3.2, including `est` and `alors`; removes an added comma after `Reciproquement`; reproduces the source's anomalous masculine `quasi-compact` rather than silently regularizing it; restores source italics in Proposition 3.2 and Definition 3.3; and underlines `Pic` only where it denotes the Picard functor. Plain `Pic` remains plain where it denotes the representing scheme. These are page-local source decisions, not global search-and-replace rules.

Material after scan index 646 remains inherited and unchecked scaffold. Output page 339 crosses the checked boundary and therefore does not certify scan index 647 or later material. Presence in the compiled reader is not a source-check claim. Reader page count is not a completion metric because source restoration and layout reflow can add or remove pages.

## English Translation Restart

`english_source_checked_restart/` contains the new English Expose X continuation through current indexes 532-537, source-PDF pp. 526-531, printed pp. 519-524. It was translated directly from scans with the current French text as a control, compiled, and visually checked. It is a source-checked continuation tranche, not a synchronized whole-volume English edition.

## Files

- `sga6_fr_workpass.tex` and `.pdf`: current French publication freeze.
- `CERT_LOG.md`: pagewise source-comparison ledger and exact next cursor.
- `ERRATA_SGA6.md`: running book-versus-edition decisions.
- `compile_logs/`: two clean short-path publication builds and the full LaTeX log.
- `source_witness/SGA6_source_idx646.pdf`: high-resolution source witness for this one-page public delta.
- `source_witness/boundary_pages/`: the last two checked source pages and next unchecked page.
- `render_checks/`: rendered output pages around the current frontier and the repaired Proposition 1.7 layout.
- `english_source_checked_restart/`: editable English tranche, source witnesses, builds, and audit files.
- `publication_pdf_text.txt`: extracted PDF text used for readback checks.
- `PACKAGE_SHA256.csv`: package integrity manifest.

## Build And Readback Notes

The publication copy repeats one presentation-only repair used in the preceding release: item (iii) in Proposition 1.7 is wrapped across continuation rows so the unchanged text and formula remain inside the A4 text block. No mathematical content was altered.

The final build is made from a short ASCII working directory to avoid stale-output failures on long Windows paths. The resulting 378-page PDF has zero fatal errors, zero overfull boxes, zero underfull boxes, no missing characters, and no unresolved references. Visual checks cover the repaired display, the current Expose XIII frontier, and the first output page crossing beyond that frontier.

## Classification

This is substantive source-rescribe/workpass provenance and a useful current French working reader. It is **not** a completed SGA6 edition, critical edition, whole-volume source-faithfulness certification, synchronized English edition, publication-grade proofread edition, or diagram-by-diagram certification. SGA5 remains incomplete and error-bearing. SGA7 remains partial and caveat-heavy.
