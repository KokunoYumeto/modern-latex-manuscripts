# Page inspection queue - 2026-06-29

This artifact turns draft reviewer glossary index rows into concrete page-inspection tasks. It is part of the Noether multilingual review-preparation workflow.

It is not an inspection result, not a populated glossary, and not a term approval ledger.

Companion machine-readable file: `PAGE_INSPECTION_QUEUE_20260629.json`

## Counts

- Inspection tasks: 153
- Source index rows: 153
- Source text copied into this artifact: false
- Completed extraction inspections: 24
- Current approved terms: 0
- Current accepted corrections: 0

## Priority Summary

- High priority: 69
- Medium priority: 36
- Normal priority: 48

## Lane Summary

| Lane / sublane | Tasks | High | Medium | Normal | Not started | Completed extraction inspections |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| simplified_chinese | 34 | 14 | 8 | 12 | 20 | 14 |
| french | 21 | 8 | 4 | 9 | 13 | 8 |
| spanish | 25 | 10 | 5 | 10 | 23 | 2 |
| japanese | 41 | 17 | 12 | 12 | 41 | 0 |
| fa_IR | 22 | 10 | 7 | 5 | 22 | 0 |
| prs_AF | 4 | 4 | 0 | 0 | 4 | 0 |
| arabic | 6 | 6 | 0 | 0 | 6 | 0 |
| tg_Cyrl_TJ | 0 | 0 | 0 | 0 | 0 | 0 |

## Task Shape

Each machine-readable task includes:

- `inspection_task_id`
- `term_id`
- `language_lane` and optional `sublane_or_script`
- `english_concept` and `mathematical_domain`
- priority and priority reason
- hashed source artifact pointer
- `observed_source_term_ref` back to the draft glossary index/source artifact row
- source witness IDs and sample pages
- required checks and output fields to fill

## Boundaries

- A completed extraction inspection does not approve a term.
- This queue does not copy source-language term strings.
- This queue does not populate project-proposed terms.
- Reviewer approval must still flow through review packets and accepted-correction ledgers.
- Long source quotes must not be copied into handoff artifacts.

## Immediate Next Gates

- Add human page-context notes for extraction-inspected ready rows.
- Manually revisit rows where exact occurrence was not reverified by extraction.
- Continue high-priority page inspection queue.
- Preserve the unresolved Tajik Cyrillic gap until sources exist.
