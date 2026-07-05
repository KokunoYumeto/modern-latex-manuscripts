# Noether Romance Flagged Row Evidence Supplement

Draft / non-canonical / not native reviewed / not approved.

This supplement follows the blocker-resolution addendum and records the evidence state for the two non-blocker Romance rows that still carried special audit flags: French Hilbert basis and Spanish semisimple. It does not promote either row, populate reviewer packets, or claim native review.

## Rows Covered

- `term-fr-0003`: French `Hilbert basis` -> draft row shorthand `base de Hilbert`, with theorem-context preference `théorème de la base de Hilbert`.
- `term-es-0021`: Spanish `semisimple` -> draft register label `semisimple`, with direct prose preserving `completamente reducible` / complete reducibility where the German says `vollständig reduzibel`.

## French Hilbert Basis Evidence

Existing corpus slices:
- `R02`: Hilbert basis / basis theorems / finiteness.
- `R07`: Hilbert module-basis theorem in polynomial rings.

German source anchors:
- Current German baseline includes Hilbert/module-basis contexts such as `L4560-L4566`, `L5511`, and `L5778-L5803`.
- The important source phrase for the French row is not merely a noun phrase `basis`, but Hilbert's theorem on module bases / basis theorems.

Local French evidence:
- Validated French TeX scan still has 0 exact hits for `base de Hilbert`.
- Supplemental local French course text has theorem-level evidence:
  - `sources/non_slavic_reference_corpus/20260628_french_spanish_native_math_register/extracted_text/added_sources/french-mourougane_acga_cours_2024_25.txt:L115`: `théorème de Hilbert`.
  - Same file `L819`: `Théorème de la base de Hilbert`.

Decision:
- Do not upgrade the row to an unflagged exact-term row because `base de Hilbert` still lacks validated French TeX hits.
- Strengthen the draft guidance: in corpus prose, prefer `théorème de la base de Hilbert` or `théorème de Hilbert sur la base de modules` when the German source context is theorem-level.
- Keep `base de Hilbert` only as the row shorthand / glossary label pending native or specialist review.

Updated draft note:

French theorem-context rendering should read:
`théorème de la base de Hilbert` where the source context names Hilbert's basis theorem, and `théorème de Hilbert sur la base de modules` where the German wording is specifically `Modulbasis`. The shorter `base de Hilbert` remains a non-canonical glossary shorthand rather than an approved corpus rendering.

## Spanish Semisimple Evidence

Existing corpus slice:
- `R13`: complete reducibility / semisimple register.

German source anchors:
- `L15846-L15850`: a ring is `vollständig reduzibel` when the zero ideal decomposition has prime components / equivalently a direct sum of fields in the stated context.
- `L16270-L16272`: representation classes and systems are `vollständig reduzibel`.
- `L17234`: `Ring ohne Radikal` is glossed as `Halbeinfacher Ring`.
- `L17776`: a representation is called `vollständig reduzibel`.
- `L17920`: a hypercomplex system without radical is completely reducible, and conversely for representations.

Local Spanish evidence:
- Existing Romance sidecar reports Spanish `semisimple` evidence as 5 target-family hits in 1 validated local file.
- A tighter local search for Spanish `anillo semisimple`, `representación semisimple`, and `completamente reducible` in the selected Spanish validated/source shelves returned no exact hit.
- Available local Spanish hits such as `álgebra de Lie semisimple` prove the Spanish adjective exists, but they do not by themselves license Noether's ring/representation-theory passage.

Decision:
- Retain the manual-review flag.
- In draft corpus prose, preserve literal source semantics with `completamente reducible` / `completa reducibilidad`.
- Use `semisimple` only as a modern-register explanatory label for the radical-free / complete-reducibility cluster, never as a silent replacement for every `vollständig reduzibel` occurrence.

Updated draft note:

Spanish direct corpus prose should prefer `completamente reducible` for `vollständig reduzibel`. The term `semisimple` may remain in an evidence note where the German also gives `Halbeinfacher Ring` or where the context explicitly connects complete reducibility and radical-free systems, but it remains `not_reviewed` and `not_approved`.

## Coverage Impact

- No row count changes.
- `term-fr-0003` remains translated with evidence gap, but the gap is now narrowed to exact shorthand `base de Hilbert`; theorem-level French evidence is available locally.
- `term-es-0021` remains translated with manual-review flag; the German source anchors are exact, but the modern Spanish register bridge remains review-sensitive.
- The whole Romance lane therefore remains at 46 active rows accounted for, with 44 corpus-prose/source-note covered row instances and 2 tensor-product blocker rows awaiting a canon German tensor-product source.

