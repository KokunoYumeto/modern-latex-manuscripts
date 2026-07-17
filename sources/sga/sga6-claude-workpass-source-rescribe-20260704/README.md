# SGA6 French Source-Rescribe Workpass: idx662

This package freezes the active pagewise French source-rescribe workpass at
`CERT_LOG.md` entry #679, scan index 662, volume p. 649, Expose XIII p. 34.
The next unchecked page is scan index 663, volume p. 650, Expose XIII p. 35.

The grouped reader/source/audit package is published under the permanent SGA
concept DOI [`10.5281/zenodo.20410947`](https://doi.org/10.5281/zenodo.20410947).

## What This Update Adds

Relative to the preceding public freeze at entry #663 / scan index 646, this
package adds sixteen directly checked source pages, scan indices 647--662. The
linear pass continues Expose XIII from p. 19 through p. 34.

The pagewise comparison restores source-visible theorem structure, complete
parenthetical clauses, Picard-functor versus representing-scheme notation,
inline mathematical arrangements, cross-references, punctuation, and source
typography. It also records source anomalies instead of silently replacing
them with normalized prose. Every decision is documented in `CERT_LOG.md` and
`ERRATA_SGA6.md`.

Material after scan index 662 remains inherited and unchecked scaffold.
Output page 346 crosses the checked boundary and therefore does not certify
scan index 663 or later material. Presence in the compiled reader is not a
source-check claim. Reader page count is not a completion metric because
source restoration and layout reflow can add or remove pages.

## Retained English Restart

`english_source_checked_restart/` retains the previously published English
Expose X continuation through current indices 532--537, source-PDF pp.
526--531, printed pp. 519--524. It is a source-checked continuation tranche,
not a synchronized whole-volume English edition. A newer local English
workpass exists, but its release metadata and manifests were still changing
when this freeze was made, so it is not promoted here.

## Files

- `sga6_fr_workpass.tex` and `.pdf`: current French publication freeze.
- `CERT_LOG.md`: pagewise source-comparison ledger and exact next cursor.
- `ERRATA_SGA6.md`: running book-versus-edition decisions.
- `compile_logs/`: two fresh clean publication builds and the final LaTeX log.
- `source_witness/SGA6_source_idx647_662.pdf`: sixteen-page high-resolution
  source delta.
- `source_witness/boundary_pages/`: previous checked, last checked, and next
  unchecked source pages.
- `render_checks/`: rendered output pages around the current frontier and a
  combined output/source contact sheet.
- `english_source_checked_restart/`: retained English restart evidence.
- `publication_pdf_text.txt`: extracted PDF text used for readback checks.
- `PACKAGE_SHA256.csv`: package integrity manifest.

## Build And Readback Notes

The frozen TeX was rebuilt twice with pdfLaTeX from a short ASCII working
directory. The resulting 377-page A4 PDF has zero fatal errors, zero overfull
boxes, zero underfull boxes, no missing characters, and no unresolved
references. The boundary render shows the checked p. 649 text on output page
346 and makes the first unchecked p. 650 continuation visible as a boundary,
not as certified content.

Independent release validation caught and repaired one presentation-only
overfull array in the inherited Proposition 1.7 material. The prior
continuation-row layout was restored without changing any words or formulas;
`render_checks/output_page_201_layout_fix.png` records the final page. The two
final build logs are the post-repair logs and contain no overfull-box warning.

## Classification

This is substantive source-rescribe/workpass provenance and a useful current
French working reader. It is **not** a completed SGA6 edition, critical
edition, whole-volume source-faithfulness certification, synchronized English
edition, publication-grade proofread edition, or diagram-by-diagram
certification. SGA5 remains incomplete and error-bearing. SGA7 remains partial
and caveat-heavy.
