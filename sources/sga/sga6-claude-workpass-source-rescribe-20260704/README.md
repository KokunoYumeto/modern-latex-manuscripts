# SGA6 French Source-Rescribe Workpass: idx442

This package freezes the active pagewise French source-rescribe workpass at `CERT_LOG.md` entry #439, scan index 442, volume p. 429, Exposé VII p. 14. The next unchecked page is scan index 443, volume p. 430, Exposé VII p. 15.

The fuller source-witness, render-check, and build-log package is published at Zenodo record [`21316718`](https://doi.org/10.5281/zenodo.21316718).

## What This Update Adds

Relative to the preceding public freeze at entry #437 / scan index 440, this package adds two directly checked pages: Exposé VII pp. 13-14.

The inherited scaffold had replaced most of Proposition 1.9's proof with a fabricated one-line summary. The source pass restores the printed statement, reference, full proof, and its continuation across the page boundary. It also restores the exact Proposition 1.10 statement and its omitted proof, then verifies the opening of section 2 and the Tor-algebra displays (2.1.1)-(2.1.3), including missing colons and source wording. Entries #438 and #439 in `CERT_LOG.md` record the exact repairs.

Material after idx442 remains inherited and unchecked. In particular, output page 232 continues below the checked source-page boundary into later scaffold material; its presence in the compiled reader is not a source-check claim for idx443 or beyond.

## Files

- `sga6_fr_workpass.tex` and `.pdf`: current French publication freeze.
- `CERT_LOG.md`: pagewise source-comparison ledger and next cursor.
- `ERRATA_SGA6.md`: running source/edition errata notes.
- `compile_logs/`: two short-path publication builds and the full LaTeX log.
- `source_crops/idx441_442/`: 180 dpi full-page source witnesses for the newly promoted pages, plus earlier representative crop evidence.
- `render_checks/`: rendered output pages around Proposition 1.7 and the changed frontier.
- `PACKAGE_SHA256.csv`: package integrity manifest.

## Build And Render Notes

The publication copy retains the layout-only line break inside Proposition 1.7 and the zero-width `\hspace{0pt}` guard before one Exposé VII sentence. These prevent a 129 pt overflow and a reproducible pdfTeX text omission without changing mathematical content.

The final build was made from a short ASCII working directory because a long Windows path had previously left a stale PDF despite a successful process exit. The final 388-page PDF has zero fatal errors, zero overfull boxes, and zero underfull boxes. Render and text-extraction checks cover output pages 201, 231, and 232.

## Classification

This is source-rescribe/workpass provenance and a useful current French working reader. It is **not** a completed SGA6 edition, critical edition, whole-volume source-faithfulness certification, English synchronization, publication-grade proofreading, or diagram-by-diagram certification. Material after scan index 442 remains inherited scaffold until directly checked. SGA5 is incomplete and error-bearing; SGA7 remains partial and caveat-heavy.
