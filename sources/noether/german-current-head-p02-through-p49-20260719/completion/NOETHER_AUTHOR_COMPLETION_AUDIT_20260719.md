# Noether author-completion audit, 2026-07-19

## Controlling result

The represented edition scope contains 753 unique body/source-page keys: 686 numbered-paper body keys after excluding four Paper 2 next-article boundary controls, plus 67 collected-volume tail pages, pp. 711-777.

- 745/753 page keys (98.94%) are closed on a controlling current-head record.
- 8/753 page keys (1.06%) remain genuinely open: Paper 2 printed pp. 50-57.
- Forty-two of 43 numbered papers are closed. Paper 2 is the sole partial paper.
- The 67-page collected-volume tail is closed.
- Web has the non-overlapping final P02 assignment, printed pp. 50-57.

The live TeX is SHA-256 `6FCBF5DB4E4378032B7074442C181E3FCFE975275319E49B284CE3B868EE0D5D`; the live 466-page PDF is SHA-256 `505A4966299C7292EF272FD54754BF4E5F45B14C72AFA03B487512D4EFED4136`.

## This checkpoint

### Paper 2, printed pp. 42-49

LocalCodex opened all eight complete native 600 ppi source pages, plus three overlapping 2x enlarged strips per page. The audit covered every prose line, formula, coefficient, index, exponent, sign, accent, hat boundary, underlining hierarchy, section heading, source note, matrix, and page boundary.

Six grouped repairs close these pages:

- p42: restored the pair-wide hat over `ub^2` and the source underlines on principal expressions 1)-2).
- p43: restored the corresponding pair-wide hat and underlines on principal expressions 3)-9).
- p45: restored the source Section 7 heading hierarchy.
- p47: removed a non-source comma that split formula (6.) into a stray expression plus an equation; the source has one continuous product.
- p48: restored the source Section 8 and Section 9 heading hierarchy.
- p49: restored the source Section 10 heading hierarchy.

Printed pp. 44 and 46 required no patch after complete-page source comparison. A focused p44 enlargement establishes the negative control `w=x\widehat{u}b`: the hat is narrowly over `u`, not over `xub`.

### Web P04 duplicate intake

The newly attached `Web_P04_p118_143_CurrentHeadAudit_20260719` package was compared by content. Its eighteen grouped repairs are already present in this authority line and already represented by correction-origin IDs `CO-W04-P04-001` through `CO-W04-P04-018`. Its stale cumulative was not imported and no duplicate fix rows were created.

## Build and containment evidence

XeLaTeX passed twice and the cumulative remains 466 pages. Final compile-log scanning found no fatal error, emergency stop, undefined reference, rerun warning, overfull box, or underfull box; only pre-existing font substitutions remain.

Output pages 11-22 were rendered before and after. Pages 13-17 changed and were opened visually at original detail; pages 11-12 and 18-22 are pixel-identical. Exact reconvergence at output p18 bounds all reflow. No clipping, overlap, broken glyph, unresolved reference, or page-boundary defect was found.

## Ledger state

- Correction-origin ledger: 514 rows, unique action IDs.
- Hard-math ledger: 180 rows; no known live hard-math repair awaits integration.
- Detailed page-QC ledger: 1,325 rows.
- Canonical page/control index: 758 rows, no duplicate paper/page keys.
- Source-error apparatus: 85 rows, unique apparatus IDs.

The canonical rows for P02 pp. 42-49 now contain complete current-head source audits. The only still-open body rows are P02 pp. 50-57.

## Remaining work

1. Receive Web's complete-page source audit for Paper 2 printed pp. 50-57.
2. Adjudicate every proposed delta against the original source and current head by content, not by package revision name.
3. Merge only source-confirmed changes, compile twice, render every changed page, and rerun whole-document containment.
4. Replace the final eight open canonical rows with complete-page dispositions.
5. Rerun the whole-author 753-key validation and require zero open or superseded-only body rows before any complete-author claim.

Full page coverage is necessary but does not by itself authorize a complete-author release until final integration, ledger validation, build, render, and package integrity checks all pass.
