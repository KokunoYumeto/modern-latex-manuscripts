# Build check

## Page counts

- Spanish standalone Papers 36--39: 9 pages.
- Japanese standalone Papers 36--39: 8 pages.
- German source/control Papers 36--39: 9 pages.
- English control Papers 36--39: 9 pages.
- Source scan witness: 19 pages.
- Cumulative Spanish through Paper 39: 356 pages.
- Cumulative Japanese through Paper 39: 318 pages.
- Layout-cleaned cumulative English through Paper 39: 339 pages.
- Layout-cleaned cumulative German through Paper 39: 346 pages.

## Engines

- Spanish standalone and cumulative: `pdflatex`.
- Japanese standalone and cumulative: `xelatex`.
- German/English controls and cleaned cumulatives: `pdflatex`.

## Log diagnostics

All current Spanish/Japanese/German/English standalone and cumulative logs report zero overfull and zero underfull boxes.  Japanese logs contain normal CJK/font-shape substitutions only.

## Render checks

Rendered checks are included in `07_rend/`:
- standalone first/last pages for Spanish and Japanese;
- cumulative first, table pages 39--40, and tail pages for Spanish/Japanese;
- cleaned cumulative English/German table pages 39--40 and tail pages;
- source scan first/last pages.
