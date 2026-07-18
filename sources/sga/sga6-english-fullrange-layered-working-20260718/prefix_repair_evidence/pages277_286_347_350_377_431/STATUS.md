# SGA 6 English prefix gate repairs: sealed status

Date: 2026-07-18  
Scope: the six pre-526 audit gates at source-PDF pages 277, 286, 347, 350, 377, and 431.  
Production file patched: `SGA6_sourcePDF001_525_English_Inherited_PartiallySourceSynchronized_fragment.tex` in the cumulative working-edition root.

## Outcome

All six gates are resolved for the next cumulative-reader build:

- source-PDF 277: exact hypotheses and stalk/cycle maps restored; Corollary 5.6 corrected from `D(X)` to `D^{-}(X)`;
- source-PDF 286: displayed definitions adjudicated clean; omitted source footnote restored;
- source-PDF 347: formulas (5.4.1) and (5.4.2) retained algebraically and their source derivations restored;
- source-PDF 350: the real symbol error `lambda^k(N'_0)=0` corrected to `gamma^k(N'_0)=0`, with suppressed proof dependencies restored;
- source-PDF 377: the physically upside-down leaf was reoriented for inspection; the missing proof of Corollary 1.4 and all of Lemma 1.5.1 were restored, and the resulting numbering/cross-references were synchronized;
- source-PDF 431: repair105 was retained without alteration and verified by an exact normalized block hash.

The patched fragment is 812,825 bytes / 13,569 lines, SHA-256 `6A6878FCE68050F797E1E4256D363D038A7BE0B4C8A00430195E268887391194`. Before this gate pass it was 809,652 bytes, SHA-256 `FDEE28678288310DD9955AB2A65144BD67F1B213C40BCA1D32BD7E44C679A3F1`.

The original repair108 witness, source scans, and French workpass were not edited. This gate closure does not relabel the rest of source-PDF 001--525 globally source-checked; it removes only the six audit gates named above.

## Build boundary

No whole-reader build was run in this subtask, by coordination with the parent manager. Static TeX checks pass: brace balance 0, minimum brace balance 0, and 0 begin/end environment mismatches across 17 environment kinds. The parent task may now rebuild the cumulative reader and attach compile/render receipts.

## Durable evidence

- `SOURCE_COMPARISON.md`
- `CORRECTION_LEDGER.csv`
- `FORMULA_AND_SYMBOL_CHECKS.csv`
- `BEFORE_AFTER_SNIPPETS.md`
- `TERMINOLOGY_REJECTED_CHOICES.csv`
- `LINE_LOCATORS.csv`
- `STATIC_TEX_CHECK.md`
- `VISUAL_QA.md`
- `HI_CLAUDE_CODEX_SGA6_NOTES_PREFIX_GATES_20260718.md`
- `source_renders/`
- `SHA256SUMS.csv`

