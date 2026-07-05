# Lane Promotion Next-Action Queue - 2026-06-30

Status: `lane_promotion_next_action_queue_local_only_not_started`

This queue turns the integrated handoff matrix into the next local actions required before any non-Slavic lane can move toward reviewer packet population, canonical terminology, translation/revision, or publication claims.

## Summary

- Lane/cohort action rows: 14 (8 core lanes, 6 extension cohorts)
- Work units: 106 (62 ready-note, 37 manual/source-review, 1 source-discovery, 6 support)
- Methodology authority actions: 6 rows / 12 reviewer-role forms
- Authority forms in queue: 55 total (43 lane, 12 methodology)
- Source-core delta remains planned only: 22 shelves / 4290 text-source-like gap files / 5 planned chunks
- Review fields filled: 0; reviews received: 0; accepted corrections: 0; network actions: 0

## Batch Groups

| Batch | Action | Rows | Work units | Authority forms | State |
|---|---|---:|---:|---:|---|
| ready_context_note_batch | fill_page_context_notes | 2 | 62 | 6 | queued_not_started |
| manual_source_review_resolution_batch | resolve_manual_source_review_rows | 5 | 37 | 16 | queued_not_started |
| source_discovery_promotion_batch | promote_source_discovery_to_term_anchor_queue | 1 | 1 | 3 | queued_not_started |
| support_cohort_authority_note_batch | draft_support_cohort_authority_note | 6 | 6 | 18 | queued_not_started |
| methodology_authority_review_batch | obtain_methodology_authority_review | 6 | 6 | 12 | queued_not_started |

## Lane Queue

| Rank | Lane/cohort | Action | Work units | Blocker | Acceptance gate |
|---:|---|---|---:|---|---|
| 10 | french | fill_page_context_notes | 21 | blank_page_context_notes | external_reviewer_packet_population |
| 10 | japanese | fill_page_context_notes | 41 | blank_page_context_notes | external_reviewer_packet_population |
| 20 | arabic | resolve_manual_source_review_rows | 3 | manual_or_source_review_rows_unresolved | page_context_note_entry_or_rejection_after_manual_resolution |
| 20 | fa_IR | resolve_manual_source_review_rows | 10 | manual_or_source_review_rows_unresolved | page_context_note_entry_or_rejection_after_manual_resolution |
| 20 | prs_AF | resolve_manual_source_review_rows | 3 | manual_or_source_review_rows_unresolved | page_context_note_entry_or_rejection_after_manual_resolution |
| 20 | simplified_chinese | resolve_manual_source_review_rows | 11 | manual_or_source_review_rows_unresolved | page_context_note_entry_or_rejection_after_manual_resolution |
| 20 | spanish | resolve_manual_source_review_rows | 10 | manual_or_source_review_rows_unresolved | page_context_note_entry_or_rejection_after_manual_resolution |
| 30 | tg_Cyrl_TJ | promote_source_discovery_to_term_anchor_queue | 1 | source_discovery_not_promoted_to_term_queue | term_anchor_queue_population_after_source_discovery |
| 40 | africa_deep_gap | draft_support_cohort_authority_note | 1 | support_corpus_not_edition_lane | possible_future_lane_promotion_after_support_authority_review |
| 40 | east_southeast_asia_pacific | draft_support_cohort_authority_note | 1 | support_corpus_not_edition_lane | possible_future_lane_promotion_after_support_authority_review |
| 40 | methodology_interlanguage_access | draft_support_cohort_authority_note | 1 | support_corpus_not_edition_lane | possible_future_lane_promotion_after_support_authority_review |
| 40 | pan_turkic_adjacent | draft_support_cohort_authority_note | 1 | support_corpus_not_edition_lane | possible_future_lane_promotion_after_support_authority_review |
| 40 | source_first_reference_textbooks | draft_support_cohort_authority_note | 1 | support_corpus_not_edition_lane | possible_future_lane_promotion_after_support_authority_review |
| 40 | south_asia_hindustani_indic_dravidian | draft_support_cohort_authority_note | 1 | support_corpus_not_edition_lane | possible_future_lane_promotion_after_support_authority_review |

## Methodology Queue

| Queue | Lane type | Reviewer forms | Authority gate | State |
|---|---|---:|---|---|
| methodology-authority-natural_language_translation_lane | natural_language_translation_lane | 2 | methodology_claim_review_required_before_publication_claim | queued_not_started |
| methodology-authority-multi_standard_or_multi_register_family_lane | multi_standard_or_multi_register_family_lane | 2 | methodology_claim_review_required_before_publication_claim | queued_not_started |
| methodology-authority-zonal_or_interlanguage_lane | zonal_or_interlanguage_lane | 2 | methodology_claim_review_required_before_publication_claim | queued_not_started |
| methodology-authority-constructed_language_pilot | constructed_language_pilot | 2 | methodology_claim_review_required_before_publication_claim | queued_not_started |
| methodology-authority-low_resource_or_under_served_educational_lane | low_resource_or_under_served_educational_lane | 2 | methodology_claim_review_required_before_publication_claim | queued_not_started |
| methodology-authority-computational_interlingua_or_mt_pivot | computational_interlingua_or_mt_pivot | 2 | methodology_claim_review_required_before_publication_claim | queued_not_started |

## Boundary Notes

- This queue is not proof of completion; it is the next-action ledger.
- It permits local work on notes, manual review resolution, source-discovery promotion, and support-cohort authority notes.
- It does not authorize remote uploads, reviewer packet population, translation/revision, native acceptability claims, or canonical completion claims.
