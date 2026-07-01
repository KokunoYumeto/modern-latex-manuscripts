# Noether R524 P24 p234 formula (4) source-style fix

Date registered: 2026-07-02

Local package:

`C:\Users\Floris\Documents\Papors\Chatnotes\CHat translates and clean\Noether Multilingual\Noether_R524_LocalCodex_R523_P24p234_Formula4_SourceStyle_20260702.zip`

SHA256:

`2812DAB7273605E0BCA866C0912C1953254A61B1F2D90230D8E5AD4475489A19`

Size: 157,133,762 bytes.

ZIP entries inspected: 145.

Classification: current clean packaged local TeX-changing Noether source-control candidate after R523.

## Scope

This package continues the Paper 24 raw-JP2 audit from the beginning of the paper. The new source-backed repair is on Paper 24 printed p. 234, formula (4): the current cumulative had four congruence signs in the Elementarteilerform/Norm display, while the source page visibly prints plain equality signs before the parenthesized ideals.

Confirmed repair:

1. Paper 24 p234 formula (4): four occurrences of `\equiv0(...)` become source-style `=0(...)`.

Build: XeLaTeX passed twice; cumulative German PDF remains 471 pages.

Main internal evidence:

- `README_R524.md`
- `audit/summary_R524.json`
- `audit/confirmed_fixes_R524.csv`
- `audit/visual_dispositions_R524.csv`
- `audit/diff_R523_to_R524.diff`
- `audit/source_quality_R524.csv`
- `cum/cum_de_R524_p24p234_formula4_sourcefix.tex`
- `cum/cum_de_R524_p24p234_formula4_sourcefix.pdf`
- `source_evidence/P24_p234_formula4/`

## Source quality caveat

The source witness is an IA original JP2 page staged locally at about 400 ppi. This is below the preferred 650+ dpi audit rule. Enlarged PNGs in the package are readability renders only, not added optical detail. The tight crop is visually decisive for equality versus congruence in formula (4).

## Public claim boundary

R524 is source-control material only. It is not a reader release, not Paper 24 certification, not Noether closure, not whole-corpus source certification, not multilingual synchronization, and not a critical edition.
