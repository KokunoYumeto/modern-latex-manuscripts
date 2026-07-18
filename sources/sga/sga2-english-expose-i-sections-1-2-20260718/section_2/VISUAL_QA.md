# Visual QA: Exposé I, §2

QA date: 2026-07-18

## English target render

The final five-page PDF was rendered page by page to PNG and assembled into a
contact sheet. The proposed public evidence is:

- `evidence/rendered_english/page-1.png` through `page-5.png`;
- `evidence/rendered_english/contact_sheet.png`.

Every page was inspected at readable resolution. Results:

- page count and order: PASS;
- all text within the page box: PASS;
- no clipping, overlap, blank page, or missing region: PASS;
- display equations and their printed labels legible: PASS;
- underlined sheaf-valued functors visually distinguishable: PASS;
- superscript stars, primes, closure bars, subscripts, and arrows legible:
  PASS;
- marginal printed-page locators 13--18 visible at the correct boundaries:
  PASS;
- four source/editorial notes legible without colliding with body text or
  footnotes: PASS;
- bibliography and final Gysin display on page 5: PASS.

The contact sheet was additionally re-opened from the assembled payload and
visually checked.

## French control render

The controlling French PDF physical pages 18--22 were rendered locally and
inspected against corrected French TeX lines 280--503. The local controls are:

`render_check/source_fr_pages_018_022/source-018.png` through
`source-022.png`, plus `contact_sheet.png`.

The inspection confirmed:

- original printed-page transitions 13--18;
- statement order and plural `Remarques 2.7`;
- labels (19)--(32), including (21 bis), (23 bis), and (24 bis);
- corrected-branch notes and both original/corrected reference occurrences;
- the four declared source anomalies at their stated locations; and
- the terminal bibliography.

French renders are source-control evidence retained locally and are not
redistributed in this public checkpoint.

## Cross-render conclusion

The English pagination is not required to reproduce the French layout. The
gate is source order, locator accuracy, mathematical legibility, and absence
of rendering defects. That gate passes for all five English pages. Visual QA
does not extend beyond this bounded unit.
