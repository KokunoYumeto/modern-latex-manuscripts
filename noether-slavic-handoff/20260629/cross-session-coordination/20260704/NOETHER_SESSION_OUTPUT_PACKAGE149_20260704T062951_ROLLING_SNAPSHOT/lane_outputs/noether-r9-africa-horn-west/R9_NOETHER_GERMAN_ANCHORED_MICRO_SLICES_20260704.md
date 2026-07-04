# R9 Noether/German-Anchored Non-Canonical Micro-Slices

Generated: 2026-07-04

Goal: move beyond general source ledgers into concrete corpus-support slices anchored to Noether/German concept work. These slices are non-canonical reviewer/corpus support only. They are not term approvals, not native/community review, not pilot material, and not public translation evidence.

## Slice Boundary

- `promotion_allowed=false` for every row.
- `micro_slice_text` is a reviewer-facing support note or draft sidebar candidate, not target prose.
- Source rows may support search, reviewer packets, side-by-side concept tables, and OCR/source closure.
- Hard Noether concepts remain blocked unless direct local higher-math evidence or reviewer/source returns exist.

## German/Noether Concept Anchors Used

| Anchor group | German anchor | English control | Current R9 behavior |
| --- | --- | --- | --- |
| School arithmetic | `Mathematik`, `Zahl`, `Addition`, `Subtraktion`, `Multiplikation`, `Division`, `Bruch` | mathematics, number, operations, fraction | usable support in Somali, Oromo, Tigrigna/Tigrinya; glossary/dictionary support in several West African rows |
| Elementary set/algebra | `Menge`, `Variable`, `Gleichung`, `Funktion` | set, variable, equation, function | usable as reviewer support in Somali/Oromo and glossary support in Fulfulde/Mandinka/Twi/Wolof/Yoruba; Tigrigna Grade 8 algebra still OCR-blocked |
| Proof language | `Definition`, `Satz`, `Beweis` | definition, theorem, proof | reviewer-facing only; no continuous Noether prose |
| Noether hard rows | `Ring`, `Körper`, `Modul`, `Ideal`, `Invariante`, `Noetherscher Ring` | ring, field, module, ideal, invariant, Noetherian ring | blocked across R9 |

## Coverage Result

The companion CSV `R9_NOETHER_GERMAN_ANCHORED_MICRO_SLICES_20260704.csv` contains:

- source-supported micro-slices for Somali, Oromo, Tigrigna/Tigrinya, Fulfulde/Fulani, Mandinka/Manding, Akan/Twi, Wolof, and Yoruba;
- exact blocker/closure slices for Hausa, Igbo, Amharic, Afar, AF-05 South Sudan, and AF-06 Omotic/southern non-Bantu;
- hard-row blocker slices for the Noether algebra anchors.

## How to Use

1. Use `source_backed_micro_support` rows as side-table evidence or reviewer prompt material.
2. Use `reviewer_prompt_only` rows to ask questions; do not draft final prose.
3. Use `blocked_exact_closure` rows as work orders for source/OCR/licensing closure.
4. Do not combine forms across language rows to create a bridge.

