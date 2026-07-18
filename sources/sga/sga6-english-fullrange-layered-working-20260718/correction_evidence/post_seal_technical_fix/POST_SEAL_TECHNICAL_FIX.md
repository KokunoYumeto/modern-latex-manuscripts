# Post-seal prefix integration fix

Date: 2026-07-18.

The early and late prefix source-repair agents jointly sealed the corrected prefix at SHA-256 `6A6878FCE68050F797E1E4256D363D038A7BE0B4C8A00430195E268887391194`, 812,825 bytes. That exact state is preserved as `SGA6_prefix_sealed_before_hyperlink_fix_SHA6A6878FC.tex` in this directory. The first complete-reader build then exposed one `pdfTeX` destination warning:

    name{Hfootnote.412} has been referenced but does not exist

The warning came from source-faithful repeated/separated footnote markers restored at source-PDF pages 141--142. Two TeX-only integration changes were applied:

1. Exercise 5.7(b)'s repeated marker now uses `\textsuperscript{\thefootnote}` instead of a second linked `\footnotemark[...]`. It displays the same current footnote number without creating a nonexistent hyperlink target.
2. Lemma 5.8.2 cannot safely execute `\footnotemark` inside the amsmath display: amsmath evaluates the display material more than once, which advanced the counter from marker 14 to footnote text 17 in the first attempted repair. The final code advances the counter exactly once before the display with `\stepcounter{footnote}`, prints the non-mutating marker with `\textsuperscript{\thefootnote}`, and emits `\footnotetext[\value{footnote}]` inside `NoHyper` after the display. This preserves the source-visible marker and bottom-of-page text while preventing both repeated counter advancement and a dangling hyperlink destination.

No English prose, mathematical symbol, formula, source reading, footnote text, numbering, or page-source disposition changed. The final integrated prefix is:

- file: `SGA6_sourcePDF001_525_English_Inherited_PartiallySourceSynchronized_fragment.tex`;
- lines: 13,572;
- bytes: 812,912;
- SHA-256: `3FE03C89BA0662A61607CDE80DDB24BC4683FA37C30C1DA580908CFAD186F68C`.

After the fix, the reader was rebuilt in two pdfLaTeX passes from clean auxiliary state. Pass 1 completed with the expected rerun-file notice; the stabilized pass-2 log has zero errors, warnings, undefined references, overfull boxes, or underfull boxes. The resulting complete reader has SHA-256 `F8B1E15754BEB5C83CF2A47B261D6F9F907DE5B7E8A6ED4DF311C624E38C7B8E`, 381 A4 pages, and all fonts embedded. `pdftotext` and full-page rendered inspection of complete-reader page 81 confirm marker 14, footnote number 14, and the complete source-faithful note text. The repaired English pages remain subject to the final all-page rendered visual-QA record.
