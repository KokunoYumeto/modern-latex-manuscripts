# SGA Translation Worklog — Batch 003

## Scope

Continued SGA 4, Exposé I, `Préfaisceaux`, from the continuation anchor after Batch 002.

Translated source range:

- Source file: `SGA4-master-71766d9/01/01.tex`
- Source lines: 1739--2668
- Sections translated:
  - Section 6, `Foncteurs fidèles et foncteurs conservatifs`
  - Section 7, `Sous-catégories génératrices et cogénératrices`

New English title choices:

- Section 6: `Faithful functors and conservative functors`
- Section 7: `Generating and cogenerating subcategories`

## Outputs

- `02_new_translation_latex/batch_003/SGA4_Expose_I_sections_6_to_7_en.tex`
- `02_new_translation_latex/batch_003/SGA4_Expose_I_sections_6_to_7_en.pdf`
- `04_render_checks/batch_003/SGA4_Expose_I_sections_6_to_7_en_render/page-01.png` through `page-13.png`
- `05_source_extracts/batch_003/SGA4_Expose_I_sections_6_to_7_source_lines_1739_2668_fr.tex`

## Translation policy applied

The Deligne reference packet was used as a style reference: direct mathematical English, theorem/proposition numbering preserved, minimal editorial interpolation, and standard contemporary terminology.

Terminology choices:

- `foncteur fidèle` -> `faithful functor`
- `foncteur conservatif` -> `conservative functor`
- `pleinement fidèle` -> `fully faithful`
- `foncteur fibrant` -> `fibred functor`
- `sous-catégorie génératrice` -> `generating subcategory`
- `sous-catégorie cogénératrice` -> `cogenerating subcategory`
- `épimorphique stricte` -> `strictly epimorphic`
- `monomorphisme strict` -> `strict monomorphism`
- `quotient strict` -> `strict quotient`
- `limite inductive/projective` -> `inductive/projective limit`

## Source review pass notes

The following evident source slips were corrected in the English draft where the mathematics fixes the reading:

1. Definition 7.1: the source line reverses the parenthetical relation between `generating by strict epimorphisms` and `epimorphic / strictly epimorphic` families. The English uses the mathematically consistent reading: strict epimorphic for the strict version, epimorphic for the ordinary version.
2. Proposition 7.6 proof: the proof mentions `génératrice par épimorphismes stricts` although the proposition assumes generation by epimorphisms and only the ordinary epimorphic property is used. The English uses `generates by epimorphisms`.
3. Proposition 7.7: corrected minor source typos in the proof: `pouf` -> `for`; `\varphi_i(X') -> \varphi(X)` -> `\varphi_i(X') -> \varphi_i(X_\alpha)`; and the displayed fiber product is written as `\varphi_i(X_\alpha)\times_{\varphi_i(Y)}\varphi_i(Y')`.
4. Proposition 7.10 proof: the final conclusion in the source has the wrong equality sign. The English reads `hence wu \neq wv`, as required by the argument.
5. Corollary 7.11: the factorization of a double arrow is rendered in the evident consistent form: an epimorphic/effective epimorphic pair followed by a monomorphism `X' -> X`.

## Validation

- Built with `latexmk -pdf -interaction=nonstopmode -halt-on-error`.
- Output PDF has 13 pages.
- The final LaTeX log was checked for overfull boxes, underfull boxes, LaTeX warnings, undefined references, pdfTeX warnings, and missing glyphs; none were present.
- Rendered all pages at 140 DPI using `/home/oai/skills/pdfs/scripts/render_pdf.py`.
- Spot-checked rendered pages 1, 6, and 13 for clipping, broken glyphs, black boxes, and layout failures.

## Continuation anchor

Continue at SGA 4, Exposé I, Section 8: `Ind-objets et pro-objets`, source line 2669 of `SGA4-master-71766d9/01/01.tex`.
