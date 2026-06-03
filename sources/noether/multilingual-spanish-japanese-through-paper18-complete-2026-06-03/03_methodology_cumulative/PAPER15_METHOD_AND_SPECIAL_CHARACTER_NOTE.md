# Paper 15 method and special-character note

Scope: Paper 15, `Die Endlichkeit des Systems der ganzzahligen Invarianten binärer Formen`, complete in Spanish and Japanese.

Source basis: the Paper 15 source scan slice `Noether_Paper15_SOURCE_SCAN_pages307-325_Die_Endlichkeit_des_Systems_der_ganzzahligen_Invarianten_bin.pdf`, the paper-level German excerpt extracted from the cumulative German edition through Paper 16, and the paper-level English control excerpt extracted from the cumulative English edition through Paper 16.

Translation policy: preserve the invariant-theory distinction between integral/polynomial integral invariants, polynomial rational functions, rational integer coefficients, and algebraic-integer coefficients. The Spanish text uses `invariante entero`, `coeficientes enteros`, and `coeficientes enteros racionales` according to context. The Japanese text uses `整係数不変式`, `整数係数`, and `有理整数係数`; `代数的整数` is reserved for algebraic integers.

Mathematical structure: all numbered equations, the four special finiteness theorems, the module argument with `\frM`, `\frN`, `\frM_p`, the normalization of residue classes, and the finite-group application in §4 are preserved as editable TeX. No table or diagram occurs in this paper.

Macro policy: Paper 15 introduces local Fraktur macros `\frH`, `\frK`, `\frM`, `\frN`, `\frG`, `\frS`, and the helper `\tmod`. The standalone and cumulative TeX files define these with `\providecommand`, so they do not override earlier cumulative definitions.

Audit flags: no translation gaps are declared. The source/control text has formula-sensitive OCR-like places in the larger cumulative source, so the scan and paper-level German/English excerpts should remain in the package for Codex/Claude comparison. The render checks cover all standalone Spanish/Japanese pages and the cumulative tails containing Paper 15.
