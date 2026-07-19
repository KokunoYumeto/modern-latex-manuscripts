# Source audit - Expose VIII Lemma 1.2 initial term and proof close

The bounded target translates corrected French lines 2618-2638. It includes
the conclusion and QED of Lemma 1.2, excludes blank line 2639 and the Section 2
heading at line 2640, and records exact printed/PDF/running locators as
88/78/70. Section 2 starts on printed page 89 on the same physical PDF page.

The independent review checked every formula layer separately:

- `E_2^{p,q}` with outer single-prime `H^p` and inner double-prime `H^q`;
- injectivity of `CA^p` for every integer `p`;
- the corrected restriction to finitely generated modules and the exact map
  `N -> F Hom(N,CA^p)`;
- the complete nested Hom expression and `H^{-q}(L')` at line 2628;
- `Ext_F` as the right-derived functor of `F` composed with `Hom`;
- `L' = Hom(L,A)` with the corrected projective-resolution branch;
- the universal identity `Ext^q(M,A) = H^q(L')` and explicit substitution of
  negative `q` to obtain the lemma; and
- the proof close, blank line, and next-heading boundary.

French line 2632 and physical page 78 print `H^q(L')` in the derived `Ext_F`
term. That input cannot follow line 2628, which already computes `H^{-q}`;
Lemma 1.2 requires `Ext^{-q}`; and line 2636 supplies the universal
`Ext^q = H^q` identity whose negative reindexing closes the proof. The target
therefore uses `H^{-q}` and labels it a transparent editorial emendation. It is
not described as a scan restoration because the direct PDF is the compiled
SMF TeX, not an independent original source. The French TeX remains unchanged.

The exact report and Claude disposition are hash-controlled in the authority
ledger. They agree on the mathematics and on the editorial-emendation label,
but remain workflow/review evidence rather than source authority.

The jcreinhold candidate notices the same sign mismatch. It is one LLM
comparison lineage and supplies no independent corroboration. Its choice to
rewrite the final universal identity directly with a negative index is
rejected; the target preserves the source's universally indexed identity and
makes the substitution explicit.

Status: independent source/formula/boundary review pass for this bounded unit.

