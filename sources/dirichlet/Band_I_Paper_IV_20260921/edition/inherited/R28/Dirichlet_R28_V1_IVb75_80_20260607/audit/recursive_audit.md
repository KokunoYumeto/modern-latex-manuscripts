# Recursive audit note — Round 28

Scope: Dirichlet, Werke Band I, Paper IV continuation tranche, printed pages 75--80.

This round intentionally does not close Paper IV. It completes exactly the next scan-contiguous slice after Round 27: printed pp. 75--80, source PDF pages 92--97, witnesses `src/pages/v1-092.png` through `src/pages/v1-097.png`.

Checks performed:
- French original-language text is typed in TeX, with displayed formulae typed as TeX.
- English translation is aligned to the same unit sequence.
- Machine-readable units, formula inventory, symbol inventory, scan map, glossary, and audit ledger are present.
- `tables.csv`, `figures.csv`, and `footnotes.csv` explicitly state null content for this tranche.
- `pdfimages -list` for both reading PDFs reports no embedded images.
- XeLaTeX logs report zero overfull and zero underfull boxes.
- Cumulative PDFs append this tranche to the Round 27 cumulative records.

Open continuation:
- Paper IV printed pp. 81--98 remain open. Do not mark Paper IV complete until those pages are typed and checked.
- Prior Band II XXV and XXVII repair flags remain active in inherited cumulative QA records.
