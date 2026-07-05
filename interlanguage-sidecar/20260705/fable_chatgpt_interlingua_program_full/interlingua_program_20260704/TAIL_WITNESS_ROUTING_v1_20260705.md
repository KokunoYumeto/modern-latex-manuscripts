# F10-1 tail witness routing v1

2026-07-05. 934 under-witnessed (East-only) retrofit rows routed against the expanded-anchor shelves.

| Route | Rows | Meaning |
| --- | --- | --- |
| A_probe_covered_concept | 516 | concept already has expanded-shelf probe hits — witness routing = reuse probe files, per-row context |
| B_intl_stem_probeable | 143 | international stem — findable by stem search across all shelves (bounded mechanical probe) |
| C_concept_linked_shelf_plausible | 189 | German key links to a ledger concept without probe hits yet — needs targeted per-concept probe |
| D_no_route_true_gap | 85 | no concept link, no international stem — true collection/curation gap |
| E_noise_or_bibliographic | 1 | dates/titles/phrase rows — workflow noise class, not witness targets |

C2-priority rows (route via a C2 spine concept): **550**

## Bounded ChatGPT probe-task spec (routable rows)
1. Input: routes A+C rows from TAIL_WITNESS_ROUTING_v1 json (term_id, route_key = concept).
2. For each concept, probe the expanded shelves per language for the NATIVE lexeme families (reuse EXPANDED_SOURCE_ANCHOR probe machinery; do NOT search the ISV form — native forms witness the concept).
3. Emit per-row: language, form, count, file_count, one KWIC window per (concept, language) — windows are mandatory (sense-audit lesson: binary form/ground form/complete system all failed on sense).
4. Route B rows: single stem-search sweep per international stem across all shelves; emit same shape.
5. NO promotions, NO bridge forms, NO summing diacritic-folded spellings; boundary text unchanged.

Route D rows stay open as true gaps; route E rows are noise-class, excluded from witness targets.