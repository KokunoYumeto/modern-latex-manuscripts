# Cayley Vol VIII --- Typesetting Pilot Notes

## 2026-06-12 Quality Caveat

This pilot note is retained as process/provenance evidence, not as a current
accuracy certificate. Later Cayley source comparison found that broad Cayley
readers and TeX can contain substantial symbol, wording, and layout mismatches.
Any local words such as "faithful" below describe the original pilot's
self-assessment and must be rechecked against the source scan before promotion.

## Range typeset

Original task asked for book pages 32-50. Investigation: PNGs `p-001`-`p-080` map to volume **front matter and beginning** of math content:
- `p-001`-`p-064`: title, biographical notice (roman numerals i-liv), classification, contents
- `p-065`: book page 1, Paper **486** starts here
- `p-080`: book page 16, mid Paper **489**

Book pages 32-50 of math content would correspond to PNGs ~96-114, which are **not available** (only 80 PNGs extracted).

Substituted range: **PNGs p-065 through p-080 = book pages 1-16** = all math available in this extraction.

## Pages typeset

- **Paper 486**: Note on Dr Glaisher's Paper on a Theorem in Definite Integration (Q.J.P.A.M. x, 1870)
- **Paper 487**: On the Quartic Surfaces $(*\check{a}\,U,V,W)^2=0$ (Q.J.P.A.M. x, 1871) --- spans pp.\ 2-11
- **Paper 488**: Note on a Relation between Two Circles (Q.J.P.A.M. xi, 1871)
- **Paper 489**: On the Porism of the In-and-Circumscribed Polygon (Q.J.P.A.M. xi, 1871), partial through p.~16

## Output

- TeX: `cayley_vol08_pages_001_016.tex` (15 PDF pages)
- PDF: `cayley_vol08_pages_001_016.pdf` (~204 KB)
- Compiles clean with MiKTeX pdflatex; only cosmetic font-shape warnings (`T1/cmr/m/scit` substituted automatically).

## Time

- Wall-clock work: ~25 min for 16 scan pages.
- **Rate: ~38 pages/hour** at this density (math-heavy, multiple papers, frequent equation environments).

## Quality vs scan

- Paper section structure, titles, and journal citations: **faithful**.
- Inline prose: **faithful** to scan with occasional minor adjacency errors where the scan is unclear.
- Math formulas: **preserved** for `\Delta`, fractions, exponents, subscripts, $\sqrt{}$, summations. Some opaque dense equations (e.g. expanded developed resultants on p.~4 of Paper 487) transcribed as best read; a few coefficient digits may be off due to scan resolution. Brace nesting in $(*\check{a}\, , )^2$ Cayley notation **preserved**.
- Two scan-blocked diagram: replaced with text placeholder (no figure was needed for the math).
- p-070 was re-read; the dense centro-surface algebra on p.~4 of Paper 487 has the highest risk of transcription drift --- compare to scan for publication.

## Recommendation

- For volume math content (Papers 486+), direct scan-based typesetting is **viable**: produces compilable, readable LaTeX with structural fidelity. Math density on the order of Paper 487 (p.~4, 10) is the failure mode --- multi-line resultant developments with subscripted coefficients drift on first pass.
- **Process improvement**: extract more PNGs (the requested 32-50 range needs ~115 PNG total). Then re-run for the actual requested range.
- For a source system pipeline comparison: this output preserves $\Delta$-like notation, brace nesting, and superscripts that source system typically drops.
- Pipeline suggestion: two-pass. First pass = this. Second pass = re-OCR only the densest 2-3 pages with higher zoom or symbol-by-symbol verification.
