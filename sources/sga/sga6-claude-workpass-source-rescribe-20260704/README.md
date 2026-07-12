# SGA6 French Source-Rescribe Workpass: idx440

This compact GitHub mirror freezes the active pagewise French source-rescribe workpass at `CERT_LOG.md` entry #437, scan index 440, volume p. 427, Exposé VII p. 12. The next unchecked page is scan index 441, volume p. 428, Exposé VII p. 13. The fuller source-crop/render-check package is on Zenodo at record `21316248`.

## What This Update Adds

Relative to the preceding public freeze at entry #435 / scan index 438, this package adds two directly checked pages: Exposé VII pp. 11-12. The work is narrow but substantive. The inherited scaffold had converted numerous inline formulas to displays, dropped a complete sentence and several smaller phrases, changed proof labels and references, altered capitalization, removed product dots and parentheticals, and changed source punctuation and wording. Entries #436 and #437 in `CERT_LOG.md` record the exact repairs.

An unfinished local start on idx441 was not promoted. The public TeX takes the verified source through the end of idx440 and then resumes the prior clean scaffold. Material after idx440 therefore remains inherited and unchecked regardless of whether later local work had begun touching it.

## Files

- `sga6_fr_workpass.tex` and `.pdf`: current French publication freeze.
- `CERT_LOG.md`: pagewise source-comparison ledger and next cursor.
- `ERRATA_SGA6.md`: running source/edition errata notes.
- `sga6_fr_workpass.log`: full final LaTeX log.
- `SHA256SUMS.txt`: integrity manifest for this compact mirror.
- Zenodo file `04_SGA6_TeX_SourceRescribe_Audit_NotCertified_idx440_20260712.zip`: two short-path publication-build logs, 300 dpi source witnesses for the newly promoted pages, rendered output checks, and a package-level checksum manifest.

## Build And Render Notes

The publication copy retains the earlier layout-only line break inside Proposition 1.7. It also places a zero-width `\hspace{0pt}` before one Exposé VII sentence. Without that guard, pdfTeX silently omitted the middle of the sentence even though the source was present and the compiler reported no error; the guarded build renders and extracts the full sentence. Neither layout intervention changes mathematical text.

Publication fix 1 removes a stray minus introduced beside the Proposition 1.7 continuation line during the first idx440 freeze merge. The corrected output page was rebuilt and visually checked before the replacement Zenodo version was published.

The final build was made from a short ASCII working directory because a long Windows working path had left a stale PDF in place despite a successful process exit. The final 387-page PDF has zero fatal errors, zero overfull boxes, and zero underfull boxes. Render and text-extraction checks confirm the previously omitted sentence is present.

## Classification

This is source-rescribe/workpass provenance and a useful current French working reader. It is **not** a completed SGA6 edition, critical edition, whole-volume source-faithfulness certification, English synchronization, publication-grade proofreading, or diagram-by-diagram certification. Material after scan index 440 remains inherited scaffold until directly checked. SGA5 is incomplete and error-bearing; SGA7 remains partial and caveat-heavy.
