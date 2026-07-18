# P29-KO-U04 source check

The exact LF source equals full-Paper-29 lines 47–51 byte-for-byte. The authority validator reports exactly one LF-normalized occurrence in the sealed P31 head and one in the latest compiled, unsealed comparison candidate. Raw line-ending differences are modeled explicitly.

Printed evidence inspected at original available resolution:

- printed p.31, SHA-256 `024008210DE649E1A452FBB9614DA4CE8453BC2B004233C79C9A8581951728BA`: the opening of U04 through the page-break fragment `Inte-`;
- printed p.32, SHA-256 `7244CB121A9199EB1388DBEC862D6894D09F80378EAB5F6FEE143F16BDC55AB0`: continuation `gritätsbasis`, the generic replacement display, specialization argument, Hilbert note, finite fraction-field extension, final equality, and line-53 boundary.

The printed page-break hyphenation `Inte- / gritätsbasis` is correctly rejoined as `Integritätsbasis` in sealed TeX. No substantive sealed-TeX/print conflict was found in U04.

Source/target logic checked:

- the opening “infinitely many elements” is cardinality of `P`;
- `g_1,\ldots,g_t` form the source-defined algebraically independent system, not a family of irreducible polynomials;
- `\mathfrak R`, hence `\mathfrak S`, is integral over `\mathfrak T=P[g_1,\ldots,g_t]`;
- `f_1,\ldots,f_k` is the historical finite `P`-algebra generating set, not a free/vector or number-field integral basis;
- the relation `F(f_k;f_1,\ldots,f_{k-1})=0` and replacement display are unchanged;
- `t_i` are first indeterminates and only then suitably specialized to elements of infinite `P` while integrality is preserved;
- transitivity is applied across finitely many replacement steps;
- square brackets denote the polynomial ring and parentheses its fraction field;
- `\mathfrak L` is a finite-degree extension of that fraction field;
- the ring of `\mathfrak R`-integral elements and the ring of `\mathfrak T`-integral elements in `\mathfrak L` coincide.

Independent read-only source review found no mathematical, quantifier, dependency-direction, specialization, notation, citation, or final-equality defect. Independent Korean review required three explicit sense glosses; they are present in the accepted target. Neither review is human certification.
