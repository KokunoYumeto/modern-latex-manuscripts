# Dedekind Round 05 Audit

## Source and range

Source: Richard Dedekind, *Gesammelte mathematische Werke*, Band III, printed pp. **368--391**.

The included source slice begins on p. 368 because that page is the clean physical continuation boundary after the previous packet. The new German/English TeX body begins at §8, item 119, and continues through §14, item 172, followed by the explanatory note printed on pp. 390--391.

## Content included

Round 05 transcribes and translates:

- items 119--172;
- §§8--14;
- the printed explanatory note headed `Erläuterungen zur vorstehenden Abhandlung`, signed `Noether`.

## Source-faithfulness decisions

The German source has not been silently modernized. The transcription preserves Dedekind's sectioning, numbered Satz/Erklärung/Bemerkung labels, historical spellings such as `daß`, and the source's mathematical notation as TeX.

The English translation keeps a conservative technical register: `System` is translated as `system`, `Abbildung` as `mapping`, `ähnlich` as `similar`, `unähnlich` as `non-similar`, `Anzahl` as `number`, and `w. z. b. w.` as `as was to be proved`. These choices intentionally preserve the Dedekindian terminology rather than replacing it wholesale with later set-theoretic terminology.

There are no diagrams or tables in this range requiring graphic reconstruction. All displayed formulas, induction clauses, inequalities, and composite-system notation are typed in TeX.

## Formatting changes in this round

The page layout was slightly reconsidered from earlier packets. The new files use modest paragraph spacing, clearer display treatment for induction clauses and enumerated conditions, and source/translation title blocks that state the page range and completion status. This is a formatting adjustment only, not a content modernization.

## Verification performed

- New German, new English, cumulative German, and cumulative English TeX files compile successfully with LuaLaTeX.
- Final PDF page counts: new German 17 pages; new English 17 pages; cumulative German 39 pages; cumulative English 38 pages.
- Source scan slice has 24 pages, pp. 368--391.
- Rendered spot checks include first/mid/final pages of the new German and English PDFs, final cumulative pages, and source pages near pp. 368, 390, and 391.
- The final source and English PDFs contain the printed explanatory note and Noether signature.

## Known open issues

No substantive open issue is being carried for this work. The whole of **Was sind und was sollen die Zahlen?** is now complete in the current German/English lane.
