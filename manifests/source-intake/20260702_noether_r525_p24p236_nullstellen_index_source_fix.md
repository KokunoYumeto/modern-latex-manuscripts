# Noether R525 P24 p236 Nullstellen index source fix

Date registered: 2026-07-02

Local package:

`C:\Users\Floris\Documents\Papors\Chatnotes\CHat translates and clean\Noether Multilingual\Noether_R525_LocalCodex_R524_P24p236_NullstellenIndex_SourceFix_20260702.zip`

SHA256:

`678D9B3FF41754728B9241DBEAD1ADE4D750026D8667FEB4CA21CF66EF37AEC2`

Size: 179,944,637 bytes.

ZIP entries inspected: 171.

Classification: current clean packaged local TeX-changing Noether source-control candidate after R524.

## Scope

This package continues the Paper 24 raw-JP2 audit from the beginning of the paper. Paper 24 printed p. 235 was checked with no source-certain patch promoted. The new source-backed repair is on Paper 24 printed p. 236, formula (5): the current cumulative had the root-family index as `\nu`, while the source display and following explanatory tuple visibly use `r`.

Confirmed repair:

1. Paper 24 p236 formula (5): `\prod_\nu`, root coordinates indexed by `\nu`, `\lambda_\nu`, and the following explanatory tuple become source-style `\prod_r`, root coordinates indexed by `r`, `\lambda_r`, and tuple indexed by `r`.

Build: XeLaTeX passed twice; cumulative German PDF remains 471 pages.

Main internal evidence:

- `README_R525.md`
- `README.md`
- `audit/summary_R525.json`
- `audit/confirmed_fixes_R525.csv`
- `audit/visual_dispositions_R525.csv`
- `audit/diff_R524_to_R525.diff`
- `audit/source_quality_R525.csv`
- `cum/cum_de_R525_p24p236_nullstellenindex_sourcefix.tex`
- `cum/cum_de_R525_p24p236_nullstellenindex_sourcefix.pdf`
- `source_evidence/P24_p235_nopatch/`
- `source_evidence/P24_p236_formula5/`

## Source quality caveat

The source witnesses are IA original JP2 pages staged locally at about 400 ppi. This is below the preferred 650+ dpi audit rule. Enlarged PNGs in the package are readability renders only, not added optical detail. The formula (5) `r` index is visually supported by both the display and the following explanatory root tuple.

## Public claim boundary

R525 is source-control material only. It is not a reader release, not Paper 24 certification, not Noether closure, not whole-corpus source certification, not multilingual synchronization, and not a critical edition.
