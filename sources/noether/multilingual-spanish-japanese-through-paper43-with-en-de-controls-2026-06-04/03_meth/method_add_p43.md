# Paper 43 methodology addition

Paper 43 completes the numbered Noether corpus in this branch. The main terminology decision is to keep `Differente` as the algebraic-number-theory different/different ideal: Spanish `diferente`, Japanese `ディファレント`. `Differenzenideal` and `Differenzenquotient` remain ordinary difference-ideal / difference-quotient language, so they are not collapsed into the technical `Differente`.

The invariant construction is rendered consistently as direct-product/coefficient-extension language. `direktes Produkt` is Spanish `producto directo` and Japanese `直積`; `Erweiterung des Koeffizientenbereichs` is Spanish `extensión del dominio de coeficientes` and Japanese `係数領域の拡大`.

`Ergänzungsmodul` and `Ergänzungsbasis` are treated as complementary-module/complementary-basis terminology tied to Dedekind's different definition: Spanish `módulo complementario`, `base complementaria`; Japanese `補加群`, `補基底`.

The next phase is a recursive source-audit pass from Paper 01 forward. Pass R01 begins in this package with Paper 01; later passes should compare source scan, German witness, English control, and ES/JA cumulative body, then apply wording-only or content-restoration fixes to the cumulative branch when they are genuinely justified by the source.
