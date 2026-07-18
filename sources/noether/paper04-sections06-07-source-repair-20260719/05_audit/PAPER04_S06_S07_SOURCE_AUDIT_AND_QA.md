# Source audit and QA

The three source-defect locator notes were used as locators, then checked independently against the included original Paper 4 scan and focused page witnesses.

## German decisions

1. Printed p. 137 visibly has the compound `Schlussausdruecke`. The R823-derived editable source split the compound. The German body was corrected; the four target translations already conveyed the correct concept and were not needlessly rewritten.
2. Printed p. 142 visibly has `rho <= n` in the series-expansion setup. The later formula (54) also includes the endpoint and functions as an internal negative control. German and all four Section 7 targets were corrected at the earlier locus.
3. Printed p. 143 visibly distinguishes dotted complementary symbols from undotted and primed symbols. Four occurrences were corrected in German and in every target body. They are separately addressable as `N04-S07-SRCDEF-001` through `-004`.

## Verification

- German cumulative: two XeLaTeX passes, 466 pages, no fatal, undefined-control, rerun, overfull, or underfull flags.
- Eight target sections: two XeLaTeX passes each; no fatal, undefined-control, rerun, or overfull flags. Existing underfull notices are recorded rather than hidden.
- German output pp. 56, 58, 59, and 60 were rendered at 300 dpi and visually opened.
- All four Section 7 PDFs were rendered in full. Their changed-locus pages 1-2 were visually opened at original render detail.

This verifies the listed changes and their rendered survival. It does not upgrade the untouched remainder of Paper 4 to fresh page-by-page certification.
