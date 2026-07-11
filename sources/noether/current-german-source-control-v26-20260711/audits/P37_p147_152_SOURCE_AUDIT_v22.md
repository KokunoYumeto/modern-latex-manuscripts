# P37 source audit: printed pp. 147-152

## Scope and authority

This pass audits Emmy Noether, *Normalbasis bei Körpern ohne höhere Verzweigung*, J. reine angew. Math. 167 (1932), pp. 147-152.

The authority is the complete six-page GDZ original-journal witness. The local full-resolution images are 3792/3800 by 5789/5790 pixels, approximately 627-668 ppi depending on the page dimension. Every page was opened visually. Earlier R126/R127 ledgers and TeX slices were used only to identify prior claims and verify their survival; they were not accepted without reopening the source.

## Prior repairs rechecked

All eight earlier targeted repairs survive and agree with the source:

1. p147: the four Deuring factors are products, not quotients.
2. p148: `(einseitigen)` is parenthesized.
3. p148: the section-1 base order is lowercase `o`.
4. p149: `(isomorphen)` is parenthesized.
5. p150: `(rationalen)` is parenthesized.
6. p150: the determinant display uses a semicolon before `S,T`.
7. p151: footnote 10 uses plain `P` as the extension-field subscript.
8. p152: the explanatory prose uses generic `p` and `P`, while the displayed prime decompositions use indexed `p_i` and `P_i`.

The current `v_t` on p150 was also checked directly and is correct. The older R127 comparison slice's `v_l` is not the source reading.

## New repairs promoted in v22

1. p147: restored semicolon separators between the four Deuring factor products.
2. p148: removed the non-source `S in G` subscript from `E^(1)=1/n sum S`.
3. p148: restored `(abhängigen)` in the generator description.
4. p148: restored `(ganze oder gebrochene)` in Satz 2.
5. p150: restored the omitted qualifier `(in bezug auf (G)_k bzw. (G)_Z)` after the irreducible ideals.
6. p150: restored `bzw.` between the determinant decomposition and the corresponding group-matrix decomposition.

The last two are substantive mathematical omissions. Both old sentences remained locally plausible, which explains why the targeted audit did not expose them.

## Pages with no additional delta

- p149: all prose, maps, bases, notes 5-7, and Sätze 2-5 checked.
- p151: all action exponents, bars, determinant formulas, root-number formulas, and note 10 checked. A dedicated zoom confirms separate bars on `R` and `T` in the product.
- p152: all prime-ideal exponents, root-number exponents, conductor identity, note 11, and the received-date boundary checked.

No figure, table, or diagram occurs in this paper.

## Build and render QA

XeLaTeX passed twice and the cumulative remains 466 pages. P37 renders on cumulative PDF pp. 357-361. Same-renderer comparison against v21 changed pp. 357-359 only; pp. 360-361 are pixel-identical. All five current output pages were rendered at 250 dpi and visually inspected. No clipping, overlap, missing display, broken footnote, or unintended downstream reflow was found.

## Closure

P37 is closed at the current-head best-source mathematical-fidelity level. This is a page-by-page source closure, not a package-number inference. Later contradictory original-source evidence may reopen a locus.
