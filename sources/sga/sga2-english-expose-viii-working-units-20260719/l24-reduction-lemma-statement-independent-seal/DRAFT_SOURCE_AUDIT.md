# Draft source audit - Expose VIII Lemma 2.4 reductions and statement

## Scope and locators

- Unit ID: `SGA2-VIII-L24`.
- Included: corrected French lines 2715-2721, comprising the regular-ambient
  reduction, regular/affine and associated-module reduction, lead-in, and
  complete Lemma 2.4 statement.
- Original printed page: 90.
- Physical source-PDF page: 80.
- Re-composed running page shown in the header: 72.
- Excluded: blank line 2722, layout command line 2723, blank line 2724, and
  the proof beginning at line 2725.
- Raw TeX cursor: French line 2723, `\setcounter{equation}{1}`, assigned to the
  outbound continuation.
- Substantive prose cursor: French line 2725 after blank line 2724.

The two cursors are intentionally distinct. Line 2723 has no visible prose on
physical page 80 but changes source layout state and must precede the next
cumulative proof unit.

## Source controls

The corrected arXiv French TeX is the textual and layout authority. Its direct
compiled SMF reader is the page and visual control for the same edition; it is
not an independent original-typescript scan. jcreinhold e7a259f is a
comparison-only LLM lineage and supplies neither authority nor independent
corroboration.

## Geometry, notation, statement, and register controls

The target retains the covering by open subsets embeddable in a regular
prescheme, `X` closed in a regular `X'`, and the immediate reduction to `X'`.
The second reduction is causal rather than temporal: `X` may be assumed
regular, and even affine, by covering it with affine open subsets. The lead-in
retains `F=tilde M` and finite projective dimension of `M`.

Lemma 2.4 retains a regular Noetherian prescheme `X`, a coherent
`O_X`-module `F`, and the assertion that the function assigning to each
`x in X` the projective dimension of `F_x` is bounded above. Ordinary English
`module` is lowercase, consistently with the preceding Corollary 2.3 unit.

The first pre-freeze draft introduced an operator `pd` and a displayed map
that do not occur in the French source. Root review caught this before freeze;
both were removed and the prose structure was restored. Root review also
replaced temporal `after covering` with source-faithful `by covering`.

## Comparison disposition

The external candidate is close in its main prose, but its rendered heading is
unnumbered, it copies source-capitalized `Module`, uses `upper-bounded`, and
does not expose the equation-counter reset at raw line 2723. Every accepted
phrase was independently checked against the French authority and compiled
page.
