# Draft source audit - Expose VIII Corollary 2.2

## Scope and locators

- Unit ID: `SGA2-VIII-C22`.
- Included: corrected French lines 2661-2668, the complete statement of
  Corollary 2.2 and its editor's note.
- Original printed page: 89. The `\pageoriginale` at line 2641 begins printed
  page 89; the next marker, at line 2685, begins printed page 90 below this
  unit. An initially supplied page-90 locator was rejected and superseded.
- Physical source-PDF page: 79.
- Re-composed running page printed in the PDF header: 71.
- Excluded: blank line 2669 and Corollary 2.3 beginning at line 2670.
- Exact next cursor: French source line 2670 after blank line 2669.

## Source decisions

The visible Corollary 2.2 number, attachment of editor's note (3), equivalence
with condition a), condition c), every quantifier, `c(x)=1`, and
`H^{i-1}(F_x)=0` were checked directly against corrected French TeX and its
compiled PDF. The full note preserves the asymmetry of the proof: c) implies
a) tautologically, while the converse uses the proof; it also preserves the
dual chain c') implies d) implies a', the `Spec(A)` reduction, finite
projective dimension, the below/infra pointer, and the reference following
2.4. The source's contextual phrase `question d)` is rendered as the
mathematically intended `condition d)` and recorded as a normalization choice.
Independent review accepted this disclosed correction because the same French
authority explicitly introduces `une condition d)` at line 2733 and labels
`Voici la condition d)` at line 2759 before proving the cited implication
chain.

The external jcreinhold e7a259f English Markdown was used only as one
comparison lineage. Its note is broadly faithful, but it drops the visible
2.2 numeral from the heading and uses plain `F`; those layout and notation
choices are rejected. Its wording was not treated as corroboration.

## Caveats

The direct compiled PDF comes from the same corrected French edition and is
not an independent original-typescript scan. This bounded unit is an
independently reviewed working English translation, not an Expose VIII or
volume completion, a critical edition, or an independently original-scan-
certified artifact.

## Independent closure

An independent source, structure, formula, boundary, isolated-build, render,
extraction, and machine-evidence pass found no substantive target defect. The
unit is sealed at French source line 2670 after excluded blank line 2669.
