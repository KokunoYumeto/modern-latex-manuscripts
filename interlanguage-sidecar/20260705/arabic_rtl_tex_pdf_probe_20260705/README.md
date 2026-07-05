# Arabic RTL Formula Render Probe 20260705

Status: generated-draft / non-canonical / visual QA support only.

This package compiles and renders Arabic formula-neighboring strings from the Arabic Fable ledger forms. It is a layout/readability probe, not source certification, native review, accepted terminology, or translation completion.

## Result

- `arabic_rtl_formula_probe_20260705.tex` compiled with XeLaTeX to PDF and rendered to PNG.
- `arabic_rtl_formula_probe_safe_20260705.tex` compiled with XeLaTeX to PDF and rendered to PNG.
- The safer variant avoids the most fragile hyphenated `A`/`R` constructions and displays long descending chains in standalone math.
- Remaining review-sensitive area: `Im*` adjacency after Arabic preposition, and English status labels inside an Arabic heading.

## Recommendation For Generated Drafts

Use prose patterns such as `جبر على \(A\)` and `حلقة على \(R\)` instead of hyphen compounds until native mathematical and TeX/PDF review. Use displayed math for long ideal/module chains. Keep every formula-neighboring string visually inspected in final page context.
