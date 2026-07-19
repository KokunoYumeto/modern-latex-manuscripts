# Noether German source-critical checkpoint

This checkpoint advances the live German cumulative through a direct complete-page audit of Noether Paper 2, printed pp. 42-49.

The cumulative remains a working source-critical edition, not a complete-author release. Paper 2 printed pp. 50-57 are the only remaining open body band and are assigned to Web.

## Current authority

- Editable German TeX: `01_current/cum_de_Local_20260719_P02p042_049_CurrentHeadAudit.tex`
- Compiled German PDF: `01_current/cum_de_Local_20260719_P02p042_049_CurrentHeadAudit.pdf`
- PDF pages: 466
- TeX SHA-256: `6FCBF5DB4E4378032B7074442C181E3FCFE975275319E49B284CE3B868EE0D5D`
- PDF SHA-256: `505A4966299C7292EF272FD54754BF4E5F45B14C72AFA03B487512D4EFED4136`

XeLaTeX passed twice. The pass-2 warning scan found no fatal error, emergency stop, undefined control sequence, unresolved reference, rerun request, overfull box, or underfull box. Whole-document text and same-renderer image comparisons identify exactly output pp. 13-17 as changed. Final changed pages were regenerated and visually reopened.

## Source and audit method

The authority is the original Paper 2 publication witness. Its page images are native 600 ppi CCITT scans. For pp. 42-49, each complete page and three overlapping 2x enlarged strips were opened visually. Printed p44 also received a focused enlargement of the auxiliary-variable hat. OCR was not used as authority.

The audit covered prose, every mathematical symbol, coefficient, index, exponent, sign, accent, hat boundary, underlining hierarchy, formula grouping, matrix geometry, section heading, source note, and page continuity.

## Repairs

- p42: restored the pair-wide hat over `ub^2` and source underlines on principal expressions 1)-2).
- p43: restored the pair-wide hat over `ub^2` and source underlines on principal expressions 3)-9).
- p45: restored the Section 7 source heading hierarchy.
- p47: restored formula (6.) as one continuous product by deleting a non-source comma.
- p48: restored the Section 8 and Section 9 source heading hierarchy.
- p49: restored the Section 10 source heading hierarchy.

Printed pp. 44 and 46 are complete-page no-patch dispositions. The p44 focused source witness confirms `w=x\widehat{u}b`; broadening the hat to `xub` would be wrong.

## Web intake disposition

`Web_P04_p118_143_CurrentHeadAudit_20260719_COMPLETE.zip` is corroborating evidence for eighteen P04 groups already present in this cumulative under correction-origin IDs `CO-W04-P04-001` through `CO-W04-P04-018`. Its cumulative was not imported and no duplicate ledger rows were created.

## Completion state

- Total body/source-page keys: 753
- Closed on controlling records: 745 (98.94%)
- Open: 8 (1.06%), all Paper 2 printed pp. 50-57
- Numbered papers closed: 42/43
- Active Web audit band: P02 printed pp. 50-57

See `06_author_completion/` for the controlling matrix, residual queue, narrative audit, and machine validation.

## Package map

- `01_current/`: cumulative TeX and PDF
- `02_source/`: original Paper 2 source slice, native pages, enlarged strips, focused p44 witness, and page map
- `03_audit/`: complete-page dispositions, exact repairs, hard-math/apparatus additions, containment reports, and render comparisons
- `04_renders/`: before, after, and final regenerated output pages
- `05_ledgers/`: current global page-QC, correction-origin, hard-math, source-apparatus, and publication logbooks
- `06_author_completion/`: completion matrix and residual queue
- `06_diff/`: exact predecessor-to-successor TeX diff
- `07_logs/`: two-pass XeLaTeX logs and QA provenance
- `07_provenance/`: package manifest and authority hashes
- `08_docs/`: continuation instructions, authority pointer, and publication-logbook addendum

## Continuation cursor

Adjudicate Web's P02 printed pp. 50-57 return against this exact cumulative and the original source. Merge only source-confirmed deltas, compile twice, render every changed output page, rerun whole-document containment, update every controlling ledger, and require zero open keys in the 753-key validation before any complete-author claim.

