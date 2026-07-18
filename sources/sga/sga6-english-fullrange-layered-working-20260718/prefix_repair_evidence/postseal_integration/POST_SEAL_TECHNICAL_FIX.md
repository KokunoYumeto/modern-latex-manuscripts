# Post-seal prefix integration fix

Date: 2026-07-18.

The early and late prefix source-repair agents jointly sealed the corrected prefix at SHA-256 `6A6878FCE68050F797E1E4256D363D038A7BE0B4C8A00430195E268887391194`, 812,825 bytes. That exact state is preserved as `SGA6_prefix_sealed_before_hyperlink_fix_SHA6A6878FC.tex` in this directory. The first complete-reader build then exposed one `pdfTeX` destination warning:

    name{Hfootnote.412} has been referenced but does not exist

The warning came from source-faithful repeated/separated footnote markers restored at source-PDF pages 141--142. Two TeX-only integration changes were applied:

1. Exercise 5.7(b)'s repeated marker now uses `\textsuperscript{\thefootnote}` instead of a second linked `\footnotemark[...]`. It displays the same current footnote number without creating a nonexistent hyperlink target.
2. Lemma 5.8.2's marker and text remain attached to the displayed target `G`, but the footnote is emitted inline inside `NoHyper`. This preserves the visible marker and footnote text while preventing a link destination that pdfTeX cannot create safely inside that display.

No English prose, mathematical symbol, formula, source reading, footnote text, numbering, or page-source disposition changed. The final integrated prefix is:

- file: `SGA6_sourcePDF001_525_English_Inherited_PartiallySourceSynchronized_fragment.tex`;
- bytes: 812,834;
- SHA-256: `56891C6A3FF8190DAEBEAFE6BA6DE00AC903841270F171862E5AC950411B5406`.

After the fix, two pdfLaTeX passes are byte-stable and the final log has zero errors, warnings, undefined references, overfull boxes, or underfull boxes. The repaired English pages remain subject to the final rendered visual-QA record.
