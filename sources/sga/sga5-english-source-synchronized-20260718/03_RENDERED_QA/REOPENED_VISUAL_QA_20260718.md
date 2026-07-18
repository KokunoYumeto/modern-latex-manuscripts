# SGA 5 reopened build and visual QA

Packaging note: the complete 309-page render set and four overview sheets are
retained in the private working directory. This lean public support bundle
contains the six focused 180-DPI English-reader renders under `focused/` and
all sixteen sequential contact sheets under `contact_sheets/`, covering PDF
pages 1-309. No source-scan render is included. The bundled contact sheets were
normalized to 8-bit sRGB for viewer compatibility without changing their page
content; see `RENDER_COMPATIBILITY_NORMALIZATION.csv`.

QA date: 2026-07-18, Europe/Berlin.

## Build

Two consecutive commands completed with exit code 0 before the byte-identical
TeX/PDF copies were given their public package filenames:

`pdflatex -interaction=nonstopmode -halt-on-error -file-line-error SGA5_English_sync_workpass.tex`

Both retained logs report 309 pages, zero fatal/undefined/package/pdfTeX
warnings, zero underfull boxes, and the same nine reviewed overfull boxes. The
three pre-existing `scriptsize`-in-math font diagnostics remain in the console
transcript but are not new and occur away from the two edited loci.

- Private raw pass 1 log SHA-256:
  `F440A9CFA0A4615AD3FAD34597962C9F768AC3B2ADF19F60144CB85417E877D0`.
- Private raw pass 2 log SHA-256:
  `F440A9CFA0A4615AD3FAD34597962C9F768AC3B2ADF19F60144CB85417E877D0`.
- Each bundled path-sanitized log SHA-256:
  `4842DC57268881939F5565FCB6CC473DEBF4B245C16C500058B4C9CD95192946`.
- Repaired PDF SHA-256:
  `0455F60C9318F0080A8ACFD4F307849F67E9C321A4C5FB9BB01A21E862721290`.

## Focused source-locus review

Rebuilt PDF pages 8--10 and 26--28 were rendered at 180 DPI. Page 8 visibly
contains the p.14 note and preserves the printed defective display; page 26
visibly contains the p.43 ambiguity note and preserves the French-control
display. Both notes fit below the footnote rule without overlap, clipping, or a
page shift. PDF text extraction also finds both complete notes at those pages.

The six bundled focused renders are under `focused/`. A convenience focused
contact sheet is retained outside this lean bundle.

## Full-volume render

All 309 PDF pages were rendered in bounded 25-page chunks at 100 DPI in the
private working tree. The individual 309 renders are not duplicated in this
lean bundle; the sequential contact sheets are bundled.

- page images: 309/309;
- dimensions: every image is 850 x 1100 pixels;
- nonstandard dimensions: 0;
- suspiciously blank threshold hits: one;
- threshold hit: page 309, manually inspected and confirmed to be the expected
  sparse final index page, not blank;
- contact sheets: 16, sequentially covering pages 1--309;
- overview sheets: 4; all inspected for clipping, blank pages, severe overflow,
  malformed diagrams, or lost page regions; no new defect found.

The sixteen bundled contact sheets are under `contact_sheets/`. The four
overview sheets and 309 individual page renders remain in the private working
tree and are explicitly outside this package.

This is rendered technical QA, not independent human scholarly certification.
