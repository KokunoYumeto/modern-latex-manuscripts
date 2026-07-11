# P34 printed pp. 669-692 source audit (LocalCodex v20)

## Scope and authority

This pass opened every printed page from p. 669 through p. 692 against the GDZ full-resolution page image in `1/03_source_witnesses/P34_p669_692_fullres`. The current v19 TeX, inherited Web/WebB repair ledgers, and rendered cumulative were comparators; none was treated as source authority.

Together with LocalCodex v19 (pp. 641-649 and 663-668) and v18 (pp. 650-662), this establishes a continuous independent current-head visual audit for the whole P34 article, printed pp. 641-692.

## Source-backed repairs promoted

1. **p. 670, source case and emphasis.** Restored lowercase `rechts-$K$-Modul`, emphasis on `äquivalent` and `Darstellungsklasse`, and the source's bold `Multiplikation mit $K$` in footnote 15a.
2. **p. 674, source emphasis.** Restored the emphasized restriction `wobei dem Einheitselement die Einheitsmatrix zugeordnet ist.`
3. **p. 675, relation glyph.** Restored `\simeq\ml_i` in the directly indecomposable consequence. The old `\sim\ml_i` stated only the weaker relation.
4. **p. 676, omitted formula step.** Restored the intermediate matrix-unit product `=\sum c_{ik}\alpha_{ik}c_{k1}` between the expanded product and its simplified result.
5. **p. 682, relation glyph.** Restored `(und \simeq\Omega sind)` in the rank-one field statement.
6. **p. 687, multiplication operator.** Restored the explicit dot in `n\cdot\sum_i\alpha_{ii}` in the Hauptspur formula.

The four repairs on pp. 675, 676, 682, and 687 are logged as substantive hard-math or operator repairs. The p. 670 and p. 674 changes are logged separately as source typography/case repairs.

## Explicit no-patch decisions

- All other pages in the band have an explicit row in `P34_p669_692_dispositions_v20.csv`; no closure is inferred merely from package survival.
- On p. 689, the printed sentence crossed out by a later handwritten reader annotation remains in the transcription. The diplomatic edition represents the printed article; non-authorial annotation is evidence, not replacement text.
- The p. 690 matrix-ring product table was compared as a structured mathematical object. No secure symbol, row, column, or product-law delta was found.
- Previously restored Web/WebB source-style headings, short arrows, emphasis, section spacing, and P34/P35 boundary all survive. They were checked, not re-promoted under new IDs.

## Error yield

- Pages opened: 24.
- Source-certain substantive mathematical defects found and repaired: 4.
- Pages with additional source typography/case defects repaired: 2.
- Pages with no new secure delta: 18.

This yield is still too high to treat earlier package-level P34 closure claims as proof of symbol-level correctness. Independent full-page comparison found a missing algebraic step and three one-symbol semantic/operator errors after several prior Web passes.

## Evidence and reproducibility

- Full source pages: `1/03_source_witnesses/P34_p669_692_fullres/`.
- Targeted labelled crops: `1/03_source_witnesses/P34_p669_692_targeted_crops/`.
- Page dispositions: `1/02_ledgers/P34_p669_692_dispositions_v20.csv`.
- Exact cumulative diff: `1/03_audit/diff_v19_to_v20.tex.diff`.
- Before/after output renders: `1/04_renders/`.
- Build logs: `1/05_logs/`.

The author-level Noether goal remains open. This document closes the independent current-head P34 article audit, not the complete corpus.
