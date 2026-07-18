# P35 metadata and Russian-summary reconciliation (working evidence)

Date: 2026-07-17  
Status: source content repaired and standalone build/visual QA passed; final cumulative hashes remain pending until the 130-file target graph is frozen.

## Authority and target

- Packaged German authority: `authority/R823/pkg_r823/Noether_R823_WebB_R822_P20p27_31_RunInDashRefine_20260717/1/01_cumulative/Noether_R823_cum_de.tex`
- Authority SHA-256: `EE8955BCF7A263917BE57DBC8F682601550CDCB5260D02CA6D486C6A6DFD4F21`
- Live French body: `working/r823_fr/tex/N35_fr_body.tex`
- French-body SHA-256 at this review cut: `95572C6EEBED2B038C3ACEBCD8EC0DED1817EA7199C1C9D209256E4C90EE0A98`

## Exact source dispositions

1. German lines 18338--18340 supply the article author/location and journal block: `Von Emmy Noether (Göttingen)` and `Rec. Soc. Math. Moscou 36 (1929), S. 65--72`. They are preserved in French at target lines 3--6 as `Emmy Noether (Göttingen)` and the corresponding journal citation.
2. German lines 18573--18593 contain the Russian-summary title, author/location, `Резюме` label, Russian prose, and `(Rec. Math. XXXVI:1; 1929)`. Target lines 183--210 preserve the Russian title, identify Emmy Noether and Göttingen, label the French rendering `Résumé (traduit du russe)`, retain the R823 primed family `f'_1,\ldots,f'_r`, and restore the terminal journal citation.
3. The stray target sentence `(Reçu le 11 novembre 1931.)` was removed: no such received-date line occurs in P35 German lines 18570--18575; it belongs to P38 at German line 19020.
4. `Integritätsbasis` is kept as the historically attested French technical term `base d'intégrité`, with an explicit first-use gloss that it is a finite generating family as a `\mathbf Z`-algebra, not a linear or module basis (target lines 20 and 68).

## Standalone build and visual check

The standalone wrapper now loads `fontspec` and was compiled with LuaLaTeX using `-interaction=nonstopmode -halt-on-error -file-line-error -recorder`. The six-page build completed with no undefined control sequence, LaTeX error, or missing-glyph report. The only warning is the harmless statement that `inputenc` is ignored by a UTF-8-native engine.

| Artifact | SHA-256 |
|---|---|
| `working/r823_fr/tex/N35_fr.tex` | `1AB0AD173CD163ED7E3770BC9B5FEC8198E3A5D1F3CEC328F9E430D213B7828E` |
| `working/build_n35_20260717/N35_fr.pdf` | `9E3A3C0FD552048F6DE68275A021213D5141255887C163E9F71047CC7E86A0AC` |
| `working/build_n35_20260717/N35_fr.log` | `2A8791951C4BE94ADF5F130A90A31FC440FD5D3DF4F6CE631CA17F66541AB763` |
| `working/build_n35_20260717/N35_fr.fls` | `BAA6842233841DA9AEF867C2751B3D0D9BDBC355790CDFCD6C4AACB0CB968F01` |
| `working/build_n35_20260717/render/page-006.png` | `D25893F7556C27C52F33271A69D06AB03194808D336781BE22FD2833FD92BF17` |

Poppler rendered the changed terminal page at 160 dpi. Original-resolution inspection found the Russian heading, French title, author/location, summary label, all four prose paragraphs, and the terminal journal citation present, legible, unclipped, and free of missing glyphs. This fragment check is not one of the three final cumulative visual-QA rows.

## Continuation cursor

When the cumulative master is released, add Unicode-font support to its preamble, rebuild the complete corpus twice with `-recorder`, and recheck P35 in the integrated pagination. At final freeze, replace this working target hash with the live P35 unit hash and whole-document hash in `R823_UNIT_RECONCILIATION_EVIDENCE_FR.csv`; cite this artifact as source-locus and fragment-QA support, not as a substitute for the final cumulative evidence.
