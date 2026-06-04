# RA03 recursive source audit - Papers 07-12

Date: 2026-06-04

Scope: continue the post-completion recursive audit in the requested order: German scan witness first, then German TeX/control, then English, Spanish, and Japanese propagation. This tranche covers Papers 07-12 and carries forward the RA02 Paper 02 hat-nu correction, the RA02 Paper 06 involution-form restoration, and the all-language Paper 02 table-page repair.

Workflow rules preserved: no summary substitution, no screenshot substitution, no silent omission of difficult tables/formulas/footnotes. Package layout is one ZIP, one root folder, then subfolders only, with short path names.

## Results by paper

- P07: clean. Formula tag (1) and six source-visible footnotes are present in DE/EN/ES/JA.
- P08: clean. Formula tags (1)-(5) and five source-visible footnotes are present in DE/EN/ES/JA.
- P09: patched. German scan/source has 42 source-visible footnotes. English had 41 and lacked the recursive-definition note in §7; Spanish/Japanese had 37 and lacked five source-visible notes. RA03 restores these omissions. Formula tags remain unchanged.
- P10: patched in English. German/Spanish/Japanese have sixteen source-visible footnotes; English had fifteen and lacked the Hamel linear-basis definition note. RA03 restores it.
- P11: clean. Formula tags (1)-(12) and fifteen source-visible footnotes are present in all branches.
- P12: clean. Formula tags (1)-(14) and two source-visible footnotes are present in all branches.

## Applied corrections

P09 EN: restored the source-visible footnote: `As the induction argument shows, such a recursive definition is possible.`

P09 ES/JA: restored five source-visible notes: the §5 reference to §7, the rational-function coefficient convention, the ordering-dependence note for rational bases, the Zermelo §1 reference, and the recursive-definition note.

P10 EN: restored the source-visible footnote defining the linear basis of all real numbers used in the Hamel discontinuity argument.

## Build matrix

| branch | pages | overfull | underfull |
|---|---:|---:|---:|
| de | 381 | 0 | 0 |
| en | 373 | 0 | 0 |
| es | 391 | 0 | 0 |
| ja | 349 | 0 | 0 |

The current patched cumulative PDFs are in `04_cum/`. Diffs from the prior RA02 cumulative branch are in `05_diff/`. Scan witnesses and pdftotext scan extracts are included under `01_scan/` and `06_data/`. Render checks include Paper 02 table pages 39-40 for all four branches, patched pages for P09/P10, and source-scan witness pages P09 pp. 13, 14, 16 plus P10 p. 7.

## Next recursive target

Continue with Papers 13-18, again in the order scan -> German -> English -> Spanish/Japanese. The next pass should pay special attention to formula-tag parity and footnote parity, because RA02 and RA03 both found substantive omissions through that route.
