# Noether Paper 4 §1 — source and build review

Scope: R823 lines 3591–3642, complete §1, “Bezeichnungen und Definitionen. Zusammenfassung bekannter Resultate.” The next cursor is R823 line 3644, §2. The section occupies original printed pages 122–124; page 124 then begins §2.

Authority: the original 1911 journal scan governs printed formulas, notes, typography, and ambiguity. R823 routes the editable German body. The inherited English section is comparison-only.

Checks completed:

- all six numbered formulas (1)–(6), the opening determinant display, index ranges, signs, exponents, and row families were compared with R823 and original pages 122–124;
- all six semantic source notes are represented, including the Clebsch note attached to formula (6), absent from the inherited English body;
- the compressed printed condition following the opening determinant was expanded editorially to state that the ordered indices belong to `{1,…,n}`; this is disclosed in the formula ledger and does not change the intended range;
- section and printed-page boundaries were checked visually: §1 begins on p.122 and ends on p.124 before §2;
- the first diagnostic build exposed duplicate PDF destinations caused by manual source tags; `hypertexnames=false` removes the collision while preserving printed tags;
- after correction, two pdfLaTeX passes succeeded and the PDF parses as two pages;
- the only final log match for “warning” is the loaded `infwarerr` package description; no actual warning, overfull/underfull box, fatal error, or emergency stop remains;
- both final English pages were rendered at 180 dpi and visually inspected.

Caveats: bounded working translation only, not complete Paper 4, a critical edition, peer review, mathematical certification, external scholarly validation, or a rights determination.
