# DR14 - Dedekind GMW I, Item I, pp. 1-18

## Scope

Author/work lane: Richard Dedekind, *Gesammelte mathematische Werke*, Volume I.

New item started: I. *Über die Elemente der Theorie der Eulerschen Integrale* [Inauguraldissertation, Göttingen 1852].

This packet covers the title and Articles 1-8. The source scan slice runs over printed pp. 1-18. Article 9 begins on printed p. 18 and is the next continuation point; it is included only as a source boundary in the scan slice, not in the German/English TeX body for this round.

## Delivered files

- `01_new/de/de.tex`, `01_new/de/de.pdf` - German source-checked reader for this round.
- `01_new/en/en.tex`, `01_new/en/en.pdf` - English translation for this round.
- `01_new/src/src_p1_18.pdf` - source scan slice for printed pp. 1-18.
- `02_cum/de/cum_de.tex`, `02_cum/de/cum_de.pdf` - clean cumulative German reader for the new Volume I lane through Article 8.
- `02_cum/en/cum_en.tex`, `02_cum/en/cum_en.pdf` - clean cumulative English reader for the new Volume I lane through Article 8.

Because this is the first packet in the new Volume I lane, the cumulative content is intentionally identical in coverage to the new work. Future packets should append to these cumulative TeX files.

## Source and fidelity notes

Primary source: GMW Volume I source scan from the Dedekind aid package. The old public reader was not used as authority where the scan and reader differ.

Scan-driven corrections were applied to the known problematic first-paper formulas, including:

- the Eulerian integral of the first kind is printed and set as `B(a,b)`, not as `Pi(a,b)`;
- Article 3 uses the quotient `(1 - x^m)/(1 - x^n)` and, later, `(1 - x^mu)/(1 - x^nu)` as in the scan;
- Cauchy's Article 8 specialization is set with `(-zi)^(mu-1)/(zz+1)` and source-style `xx`, `zz` notation where printed.

No formulas, tables, or diagrams were replaced by screenshots.

## Build and validation

The four TeX builds completed successfully:

- `01_new/de/de.pdf`
- `01_new/en/en.pdf`
- `02_cum/de/cum_de.pdf`
- `02_cum/en/cum_en.pdf`

Build logs were checked for `Overfull`, `Underfull`, `Missing character`, and LaTeX warning/fatal patterns. Result: 0 reported overfull or underfull boxes in the delivered builds.

Rendered page checks were performed on German and English PDFs, including title/formula opening pages and the formula-heavy Cauchy closing pages. Render/check images and compile logs are not included in the deliverable ZIP.

## Intake gaps

No blocking Dedekind intake gap found for this continuation. The next continuation is Article 9, beginning on printed p. 18 and continuing toward the end of Item I on printed p. 26.
