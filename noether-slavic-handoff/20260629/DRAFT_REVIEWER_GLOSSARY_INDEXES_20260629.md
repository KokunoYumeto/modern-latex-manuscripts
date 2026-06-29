# Draft reviewer glossary indexes - 2026-06-29

This artifact generates one draft reviewer-glossary index row per reserved term ID. It is intended to prepare review packets while keeping source-language terms in the original hashed term-anchor artifacts.

It is not a populated glossary, not a review result, and not a term approval ledger.

Companion machine-readable file: `DRAFT_REVIEWER_GLOSSARY_INDEXES_20260629.json`

## Counts

- Draft index rows: 153
- Source text copied into this artifact: false
- Current approved terms: 0
- Current accepted corrections: 0

## Lane Summary

| Lane / sublane | Prefix | Reserved IDs | Generated rows | Status |
| --- | --- | ---: | ---: | --- |
| simplified_chinese | `term-zh-hans` | 34 | 34 | draft_rows_generated_unreviewed |
| french | `term-fr` | 21 | 21 | draft_rows_generated_unreviewed |
| spanish | `term-es` | 25 | 25 | draft_rows_generated_unreviewed |
| japanese | `term-ja` | 41 | 41 | draft_rows_generated_unreviewed |
| fa_IR | `term-fa-ir` | 22 | 22 | draft_rows_generated_unreviewed |
| prs_AF | `term-prs-af` | 4 | 4 | draft_rows_generated_unreviewed |
| arabic | `term-ar` | 6 | 6 | draft_rows_generated_unreviewed |
| tg_Cyrl_TJ | `term-tg-cyrl-tj` | 0 | 0 | no_current_term_rows_unresolved |

## Row Shape

Each machine-readable row includes:

- `term_id`
- `language_lane`
- `english_concept`
- `mathematical_domain`
- `source_artifact` and `source_artifact_sha256`
- `row_basis` and `source_row_index_1_based`
- `observed_source_term_ref` pointing back to the original hashed term-anchor row
- source witness IDs and sample pages
- `source_context_status = automated_anchor_unreviewed`
- `project_proposed_term_status = not_populated`
- `current_decision_state = unreviewed_observed`
- `approved_for_canonical_use = false`

## Boundaries

- This file does not copy source-language term strings.
- This file does not page-inspect source contexts.
- This file does not propose translation terms.
- This file does not request or record reviewer decisions.
- This file does not approve canonical terminology.

## Immediate Next Gates

- Page-inspect source rows before populating reviewer-facing glossary packets.
- Populate project-proposed terms only in lane-specific draft glossary packets.
- Ingest reviewer decisions through the accepted-correction ledger template.