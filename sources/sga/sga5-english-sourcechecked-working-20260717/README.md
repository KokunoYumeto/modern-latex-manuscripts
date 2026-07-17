# SGA 5 English source-checked working translation

This package contains the 309-page cumulative English SGA 5 working
translation synchronized on 2026-07-17. It covers the ten exposes represented
in this volume-level workpass (I, III, III B, V, VI, VII, VIII, X, XII, and XV)
and the cumulative index through printed page 484.

The English TeX was reconciled against the current French workpass. Ambiguous
formula signs, indices, arrows, diagrams, and source readings were checked
against the retained LNM 589 scan witness. The package includes the editable
English TeX, French and inherited-English controls, the source scan, correction
and structural ledgers, final build logs, and complete rendered visual-QA
evidence.

## Open first

1. `00_reader_pdf/SGA5_English_SourceChecked_WorkingTranslation_20260717.pdf`
2. `01_editable_tex/SGA5_English_SourceChecked_WorkingTranslation_20260717.tex`
3. `02_status/PUBLIC_STATUS.md`
4. `03_source_controls/` for the scan and control TeX files
5. `04_audit/` and `05_visual_qa/` for checking evidence

## Status

This is substantive source-aware work, not OCR output. It is nevertheless a
machine-assisted working translation and source-repair checkpoint, not an
independently human-certified critical edition. One source glyph ambiguity at
Expose I printed page 43 is explicitly retained in the terminology ledger.
The final build has three localized font warnings and nine overfull-box
diagnostics; all affected pages were rendered and checked, and no content is
cropped or lost.

Corrections are welcome through GitHub issues or pull requests:
https://github.com/KokunoYumeto/modern-latex-manuscripts
