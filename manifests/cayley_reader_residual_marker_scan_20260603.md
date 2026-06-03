# Cayley Reader Residual Marker Scan — 2026-06-03

This scan lists reader-visible residual marker language after the 2026-06-03 Cayley repair passes through Git commit `27c2dc03`. It searches front-facing Cayley reader PDFs for figure/table placeholder phrases such as `[Figure:]`, `too dense`, `unreadable`, and `reader is referred to the original`.

It is a triage list, not a claim that every listed item has equal severity. Several hits are honest notices for very large tables or plates that need a dedicated table/diagram reconstruction pass rather than a quick TikZ replacement.

Found **21** reader-visible residual hits.

| Volume Reader | Reader Page | Marker | Notes |
|---|---:|---|---|
| Volume IV | 37 | `reader is referred to the original` | by the developments. (These large determinantal arrays are reproduced verbatim from the scan ; the reader is referred to the original page for the explicit numerical entries.) The  |
| Volume IV | 243 | `reader is referred to the original` | se matrix-style typesetting in the original, the table is reproduced here only in summary form; the reader is referred to the original page for the complete listing.) |
| Volume IV | 250 | `reader is referred to the original` | ry dense layout of the original printed table, only the principal entries are reproduced above; the reader is referred to the original page 253 of the memoir for the complete six-c |
| Volume IV | 252 | `too dense` | e last column (θ0, 3125×), which has the bottom total ±128505. The exact body of these two pages is too dense and too pictorial in its typographic layout to be set in line; the rea |
| Volume IV | 272 | `reader is referred to the original` | ns giving the full enumeration of monomials of degree ≤the column index in the letters e, f, g. The reader is referred to the original page 274 for the complete tabular display.] |
| Volume IV | 287 | `too dense` | 2 −540 ab3cd2e +1196 abc2d3 −840 ab3cd3 +1080 ab4cd3 +672240 and so on, · · · [the full table being too dense to set in line; the reader is referred to the original printed page 28 |
| Volume IV | 373 | `[Figure:` | \| y, 1)4 = 0, où l'on a (table dense en monomes T i 0T j 1 T k 2 avec coe cients en a, b, c, d, e): [Figure: large multi-column coe cient table for C, D, E in monomes of T0, T1, T2 |
| Volume IV | 375 | `[Figure:` | T0 + (ax2 + bx + 1 2c) T1 + (ax3 + bx2 + cx + 1 4d) T2 est la suivante (1, 0, C, D, E \| y, 1)4 = 0. [Figure: large multi-column tables giving C, D, E as explicit polynomials in T0, |
| Volume IV | 376 | `[Figure:` | 0 Cayley  Collected Papers, Vol. IV 374 deuxième note sur la transformation de tschirnhausen. [274 [Figure: continuation of the multi-column coe cient tables for E. Each column ca |
| Volume IV | 380 | `[Figure:` | , D = 1 27  (a2d −3abc + 2b3) B3 + (3abd + 3b2c) B2C + (6b2d + 6acd) BC2 + (ad2 + 3bcd + 3) C3  . [Figure: Cayley's column-table for the coe cients C and D. The columns are heade |
| Volume IX | 231 | `not reproduced here` | (4), carbon-, &c., atoms; and so on. [Plate  see scan: of trees follows in the original printing; not reproduced here.] 5 |
| Volume V | 339 | `[Figure:` | but this is a subject which I do not enter upon in the present Memoir. Cambridge, February 8, 1864. [Figure: Plate III, illustrating the Hyperbolas A Defective discussed in Arts. 7 |
| Volume V | 384 | `[Figure:` | its form in such wise as to exhibit the node and two cusps, the curve has therefore two real nodes. [Figure: composite plot of the secondary caustic curves for the various values o |
| Volume V | 432 | `[Figure:` |  135◦ −1 √ 2, 1 √ 2 −1 √ 2 1 √ 2 0 1 √ 2(−i + j) Axial System of the Dodecahedron and Icosahedron. [Figure: extensive tabular listing across two pages (pp. 534535 in original) of |
| Volume X | 349 | `[Figure:` | , showing the congregates determined by these several syzygies, and the deg-orders of the syzygies: [Figure: Annexed diagram showing the congregates determined by the irreducible s |
| Volume X | 396 | `unreadable` | comprising S0, S1, S2, S3 occupy printed pages 397398 in seven columns. As the entries are partly unreadable in the scan (typesetter has compressed and broken many fraction-bars), |
| Volume XI | 72 | `[Figure:` | p. 120 89 −20 −19 −13 −11 7 5 5 7 −3 −4 −5 −8 p. 151 97 −22 −16 −17 −19 10 5 5 5 −3 −4 9 −4 p. 187 [Figure: large table of computed values, transcribed above.] |
| Volume XI | 73 | `[Figure:` | 101125 Cayley  Collected Papers, Vol. XI Table of the Powers of Reuschle's Selected Prime Roots. [Figure: a large arithmetical table 65 columns wide listing powers gk (mod p) for |
| Volume XI | 74 | `[Figure:` | Pages 101125 Cayley  Collected Papers, Vol. XI Table (continued). [Figure: continuation of the table of powers of Reuschle's selected prime roots, spanning further values of the  |
| Volume XIII | 263 | `[Figure:` | n fact formed the squares for the weights 11 to 16, not in this manner but by the MacMahon linkage. [Figure: Square diagrams for weights w = 2 through w = 10. Each diagram lists po |
| Volume XIII | 267 | `[Figure:` | ce to subsequent investigations, a table of these conjugate forms up to the degree 6 and weight 15. [Figure: a stepped, page-wide Table of Conjugates giving capital-letter and sm |

Immediate policy: do small scan-faithful native diagrams directly; route dense coefficient tables, rotated tables, plates, and tree/axis enumerations through a cropped table/diagram workflow. Do not replace dense tables with plausible generated summaries.
