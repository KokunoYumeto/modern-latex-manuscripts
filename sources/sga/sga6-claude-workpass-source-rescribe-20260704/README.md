# SGA6 French Source-Rescribe Workpass: idx608

This stable mirror freezes the active pagewise French source-rescribe workpass at `CERT_LOG.md` entry #605, scan index 608, volume p. 595, the opening page of Expose XII. The next unchecked page is scan index 609, volume p. 596, Expose XII p. 2.

The fuller source-witness, render-check, and build-log package is published at Zenodo record [`21394244`](https://doi.org/10.5281/zenodo.21394244).

## What This Update Adds

Relative to the preceding public freeze at entry #537 / scan index 540, this package adds 68 directly checked source pages, scan indexes 541-608. The linear pass continues Expose X, completes its Grothendieck appendix and bibliography, and verifies the opening page of Expose XII.

The ledger records source-level restoration of omitted authored text, proofs, displays, and diagrams; reversal of paraphrase or condensation; repair of formulas and indices; and page-local decisions about notation, arrows, punctuation, emphasis, and book errors. `CERT_LOG.md` is the detailed evidence trail; it is not a substitute for the corrected TeX, whose edits are already applied.

Material after scan index 608 remains inherited and unchecked scaffold. Its presence in the compiled reader is not a source-check claim. The reader page count is also not a completion metric because source restoration and layout reflow can add or remove output pages.

## Files

- `sga6_fr_workpass.tex` and `.pdf`: current French publication freeze.
- `CERT_LOG.md`: pagewise source-comparison ledger and exact next cursor.
- `ERRATA_SGA6.md`: running book-versus-edition decisions.
- `_work/SGA6_source_idx541_608.pdf`: 68-page high-resolution source witness for this public delta.
- `_work/current_boundary_idx608/`: the last checked pages and the next unchecked source page.
- `_work/current_render_idx608/`: rendered output checks at the repaired layout locus and current frontier.
- `SHA256SUMS.txt`: compact mirror integrity manifest.

## Build And Readback Notes

The publication copy makes one presentation-only typesetting repair beyond the frozen live snapshot: a long Proposition 1.7 item is split across continuation rows so the unchanged text and formula remain inside the page. This does not alter the mathematical content.

The final build was made from a short ASCII working directory to avoid stale-output failures on long Windows paths. The resulting 383-page PDF has zero fatal errors, zero overfull boxes, zero underfull boxes, and no unresolved-reference warnings. Output page 201 and frontier pages 318-321 were rendered and visually checked.

## Classification

This is substantive source-rescribe/workpass provenance and a useful current French working reader. It is **not** a completed SGA6 edition, critical edition, whole-volume source-faithfulness certification, synchronized English edition, publication-grade proofread edition, or diagram-by-diagram certification. SGA5 remains incomplete and error-bearing. SGA7 remains partial and caveat-heavy.
