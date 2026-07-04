# Noether R522 P24 pp239-240 source fix

Date registered: 2026-07-02

Local package:

`C:\Users\Floris\Documents\Papors\Chatnotes\CHat translates and clean\Noether Multilingual\Noether_R522_LocalCodex_R521_P24p239_p240_SourceFix_20260702.zip`

SHA256:

`9B36DC9E633915EBB8712CB21413E62DCD9EB17C62A10DBD1022E6CD6686DF5B`

Size: 109,897,552 bytes.

ZIP entries inspected: 105.

Classification: current clean packaged local TeX-changing Noether source-control candidate after R521.

## Scope

This package closes the previously skipped Paper 24 printed pp. 239-240 gap in the raw-JP2 audit. It applies five source-backed German cumulative TeX repairs from the best staged IA raw JP2 witnesses.

Confirmed repairs:

1. Paper 24 p239: restored source `\varkappa` in the primary-ideal condition and in the `b(x)^\varkappa` phrase.
2. Paper 24 p239: restored source `\varkappa` in the derived coefficient-ideal paragraph while preserving the distinct following `\lambda`.
3. Paper 24 p239: restored terminal index `\alpha` in Hilfssatz II component lists.
4. Paper 24 p239: restored source-style `u_{\mu\nu}`, bare `\sum U_i\bar f_i(y)`, and `\frakq_\alpha` in the proof paragraph.
5. Paper 24 p240: restored vertical norm separator `N(\frakg_i\mid\frakg_{i+1})`.

Build: XeLaTeX passed twice; cumulative German PDF remains 471 pages.

Main internal evidence:

- `README_R522.md`
- `audit/summary_R522.json`
- `audit/confirmed_fixes_R522.csv`
- `audit/diff_R521_to_R522.diff`
- `audit/source_quality_R522.csv`
- `cum/cum_de_R522_p24p239_p240_sourcefix.tex`
- `cum/cum_de_R522_p24p239_p240_sourcefix.pdf`
- `source_evidence/P24_p239_p240/`
- `rendered_check/changed_pages/`

## Source quality caveat

The source witnesses are IA original JP2 pages staged locally at about 400 ppi. This is below the preferred 650+ dpi audit rule, but the accepted loci are visually unambiguous and the raw JP2 witnesses are better than derivative PDF/OCR routes. Enlarged PNGs in the package are readability renders only, not added optical detail.

## Public claim boundary

R522 is source-control material only. It is not a reader release, not Paper 24 certification, not Noether closure, not whole-corpus source certification, not multilingual synchronization, and not a critical edition.
