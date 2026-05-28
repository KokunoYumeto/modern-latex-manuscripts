# SGA Translation Worklog — translation segment

## Scope

Continued SGA 4, Exposé I, `Préfaisceaux`, from the continuation point after translation segment.

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

- `02_new_translation_latex/translation segment/SGA4_Expose_I_sections_6_to_7_en.tex`
- `02_new_translation_latex/translation segment/SGA4_Expose_I_sections_6_to_7_en.pdf`
- `04_render_checks/translation segment/SGA4_Expose_I_sections_6_to_7_en_render/page-01.png` through `page-13.png`
- `05_source_extracts/translation segment/SGA4_Expose_I_sections_6_to_7_source_lines_1739_2668_fr.tex`

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

## Source editorial review notes

The following evident source slips were corrected in the English draft where the mathematics fixes the reading:


## Validation

- Built with `latexmk -pdf -interaction=nonstopmode -halt-on-error`.
- Output PDF has 13 pages.
- The final LaTeX log was checked for overfull boxes, underfull boxes, LaTeX warnings, undefined references, pdfTeX warnings, and missing glyphs; none were present.
- Rendered all pages at 140 DPI using `/home/oai/skills/pdfs/scripts/render_pdf.py`.
- Spot-checked rendered pages 1, 6, and 13 for clipping, broken glyphs, black boxes, and layout failures.

## continuation point

