# Review packet scaffolds - 2026-06-29

This artifact groups the page-context note worklist into per-lane reviewer-packet scaffolds. It is not a populated review packet, not native review, and not a term approval ledger.

Companion machine-readable file: `REVIEW_PACKET_SCAFFOLDS_20260629.json`

## Totals

- Lanes scaffolded: 7
- Work items: 153
- Ready-row note items: 116
- Manual/source-review items: 37
- Packet rows populated: 0
- Packet rows blocked until notes: 153
- Approved terms: 0
- Accepted corrections: 0

## Lane Summary

| Lane | Work items | Ready-note items | Manual/source items | Reviewer roles | Extra checks | Status |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| arabic | 6 | 3 | 3 | 3 | 3 | scaffolded_not_populated_not_review_result |
| fa_IR | 22 | 12 | 10 | 4 | 3 | scaffolded_not_populated_not_review_result |
| french | 21 | 21 | 0 | 2 | 3 | scaffolded_not_populated_not_review_result |
| japanese | 41 | 41 | 0 | 2 | 3 | scaffolded_not_populated_not_review_result |
| prs_AF | 4 | 1 | 3 | 4 | 2 | scaffolded_not_populated_not_review_result |
| simplified_chinese | 34 | 23 | 11 | 3 | 3 | scaffolded_not_populated_not_review_result |
| spanish | 25 | 15 | 10 | 2 | 3 | scaffolded_not_populated_not_review_result |

## arabic

- Packet template key: `arabic`
- Required reviewer roles: native_arabic_mathematical_reviewer, rtl_tex_pdf_reviewer, optional_undergraduate_educator_reviewer
- Priority checks: core_algebra_and_invariant_theory_terms, modern_standard_mathematical_arabic_vs_regional_pedagogy_preferences, ocr_text_extraction_artifact_detection, rtl_rendering_punctuation_formula_embedding_labels_glossary_ordering
- Blocking concerns: ocr_derived_term_evidence_used_without_page_inspection, missing_module_or_representation_source_reinforcement, rtl_layout_changes_reading_order_or_formula_association
- Lane extra checks: rtl_render_check, ocr_provenance_flag, module_representation_reinforcement_flag

| Term ID | English concept | Domain | Priority | State | Required action |
| --- | --- | --- | --- | --- | --- |
| `term-ar-0001` | algebra | algebra_core | high | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-ar-0002` | field | field_theory | high | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-ar-0003` | Artinian | finiteness | high | manual_or_source_review_required_before_reviewer_packet_row | manual_source_review_plus_register_or_ocr_check_before_packet_population |
| `term-ar-0004` | homomorphism | morphism | high | manual_or_source_review_required_before_reviewer_packet_row | manual_source_review_plus_register_or_ocr_check_before_packet_population |
| `term-ar-0005` | isomorphism | morphism | high | manual_or_source_review_required_before_reviewer_packet_row | manual_source_review_plus_register_or_ocr_check_before_packet_population |
| `term-ar-0006` | ring | ring_theory | high | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |

## fa_IR

- Packet template key: `persian_family`
- Required reviewer roles: iranian_persian_mathematical_reviewer, dari_afghan_persian_educator_or_technical_reviewer, tajik_cyrillic_reviewer, rtl_or_script_reviewer
- Priority checks: separate_sublane_decisions, core_algebra_and_invariant_theory_terms, advanced_algebra_vs_broad_educational_source_coverage, script_directionality_numerals_punctuation_formula_alignment
- Blocking concerns: treating_fa_prs_tg_as_one_lane_without_external_rationale, tajik_cyrillic_terms_missing_from_evidence_shelf, rtl_rendering_affects_formulas_citations_or_glossary_alignment
- Lane extra checks: rtl_render_check, persian_script_punctuation_numeral_note, sublane_isolation_flag

| Term ID | English concept | Domain | Priority | State | Required action |
| --- | --- | --- | --- | --- | --- |
| `term-fa-ir-0004` | submodule | module_theory | high | manual_or_source_review_required_before_reviewer_packet_row | manual_source_review_plus_register_or_ocr_check_before_packet_population |
| `term-fa-ir-0005` | tensor product | module_theory | high | manual_or_source_review_required_before_reviewer_packet_row | manual_source_review_plus_register_or_ocr_check_before_packet_population |
| `term-fa-ir-0006` | module | module_theory | high | manual_or_source_review_required_before_reviewer_packet_row | manual_source_review_plus_register_or_ocr_check_before_packet_population |
| `term-fa-ir-0007` | free module | module_theory | high | manual_or_source_review_required_before_reviewer_packet_row | manual_source_review_plus_register_or_ocr_check_before_packet_population |
| `term-fa-ir-0008` | right module | module_theory | high | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-fa-ir-0009` | left module | module_theory | high | manual_or_source_review_required_before_reviewer_packet_row | manual_source_review_plus_register_or_ocr_check_before_packet_population |
| `term-fa-ir-0013` | Noetherian | noetherian | high | manual_or_source_review_required_before_reviewer_packet_row | manual_source_review_plus_register_or_ocr_check_before_packet_population |
| `term-fa-ir-0014` | simple | representation_theory | high | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-fa-ir-0015` | representation | representation_theory | high | manual_or_source_review_required_before_reviewer_packet_row | manual_source_review_plus_register_or_ocr_check_before_packet_population |
| `term-fa-ir-0016` | semisimple | representation_theory | high | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-fa-ir-0003` | Artinian | finiteness | medium | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-fa-ir-0017` | ideal | ring_theory | medium | manual_or_source_review_required_before_reviewer_packet_row | manual_source_review_plus_register_or_ocr_check_before_packet_population |
| `term-fa-ir-0018` | prime ideal | ring_theory | medium | manual_or_source_review_required_before_reviewer_packet_row | manual_source_review_plus_register_or_ocr_check_before_packet_population |
| `term-fa-ir-0019` | maximal ideal | ring_theory | medium | manual_or_source_review_required_before_reviewer_packet_row | manual_source_review_plus_register_or_ocr_check_before_packet_population |
| `term-fa-ir-0020` | ring | ring_theory | medium | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-fa-ir-0021` | commutative ring | ring_theory | medium | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-fa-ir-0022` | noncommutative ring | ring_theory | medium | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-fa-ir-0001` | algebra | algebra_core | normal | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-fa-ir-0002` | field | field_theory | normal | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-fa-ir-0010` | automorphism | morphism | normal | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-fa-ir-0011` | homomorphism | morphism | normal | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-fa-ir-0012` | isomorphism | morphism | normal | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |

## french

- Packet template key: `french`
- Required reviewer roles: native_or_near_native_french_mathematical_reviewer, optional_undergraduate_educator_reviewer
- Priority checks: french_algebra_and_invariant_theory_terminology, french_convention_vs_english_calque, theorem_proof_prose_register, regional_or_institutional_style_notes
- Blocking concerns: literal_calques_not_standard_in_french, confusion_with_pan_romance_or_neolatino_research_experiment
- Lane extra checks: calque_risk, regional_or_institutional_variant_note, romance_experiment_separation_flag

| Term ID | English concept | Domain | Priority | State | Required action |
| --- | --- | --- | --- | --- | --- |
| `term-fr-0006` | module | module_theory | high | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-fr-0007` | quotient module | module_theory | high | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-fr-0008` | tensor product | module_theory | high | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-fr-0009` | submodule | module_theory | high | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-fr-0014` | Noetherian ring | noetherian | high | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-fr-0015` | Noetherian | noetherian | high | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-fr-0016` | irreducible | representation_theory | high | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-fr-0017` | representation | representation_theory | high | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-fr-0018` | ring | ring_theory | medium | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-fr-0019` | ideal | ring_theory | medium | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-fr-0020` | maximal ideal | ring_theory | medium | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-fr-0021` | prime ideal | ring_theory | medium | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-fr-0001` | algebra | algebra_core | normal | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-fr-0002` | commutative algebra | commutative_algebra | normal | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-fr-0003` | Hilbert basis | commutative_algebra | normal | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-fr-0004` | localization | commutative_algebra | normal | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-fr-0005` | field | field_theory | normal | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-fr-0010` | automorphism | morphism | normal | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-fr-0011` | endomorphism | morphism | normal | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-fr-0012` | homomorphism | morphism | normal | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-fr-0013` | isomorphism | morphism | normal | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |

## japanese

- Packet template key: `japanese`
- Required reviewer roles: native_japanese_mathematical_reviewer, japanese_tex_pdf_visual_reviewer
- Priority checks: standard_algebra_and_invariant_theory_terms, kanji_kana_balance_and_imported_terms, theorem_proof_discourse_markers_and_sentence_endings, line_breaks_around_particles_labels_and_formula_punctuation
- Blocking concerns: incorrect_script_or_term_mix, rendered_pdf_layout_breaks_japanese_mathematical_prose
- Lane extra checks: kanji_kana_balance, imported_term_naturalness, line_break_render_note

| Term ID | English concept | Domain | Priority | State | Required action |
| --- | --- | --- | --- | --- | --- |
| `term-ja-0009` | tensor product | module_theory | high | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-ja-0010` | module | module_theory | high | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-ja-0011` | simple module | module_theory | high | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-ja-0012` | free module | module_theory | high | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-ja-0013` | submodule | module_theory | high | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-ja-0018` | Noether/Noetherian | noetherian | high | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-ja-0019` | Noetherian | noetherian | high | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-ja-0020` | Noetherian/Noether | noetherian | high | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-ja-0025` | Harish-Chandra | representation_theory | high | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-ja-0026` | Lie group | representation_theory | high | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-ja-0027` | semisimple | representation_theory | high | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-ja-0028` | completely reducible | representation_theory | high | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-ja-0029` | character | representation_theory | high | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-ja-0030` | irreducible representation | representation_theory | high | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-ja-0031` | group ring/group algebra | representation_theory | high | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-ja-0032` | representation | representation_theory | high | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-ja-0033` | representation theory | representation_theory | high | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-ja-0005` | Artin/Artinian | finiteness | medium | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-ja-0006` | Artinian/Artin | finiteness | medium | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-ja-0007` | finite-dimensional | finiteness | medium | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-ja-0008` | finitely generated | finiteness | medium | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-ja-0034` | ideal | ring_theory | medium | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-ja-0035` | semisimple ring | ring_theory | medium | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-ja-0036` | principal ideal | ring_theory | medium | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-ja-0037` | commutative ring | ring_theory | medium | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-ja-0038` | quotient ring | ring_theory | medium | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-ja-0039` | maximal ideal | ring_theory | medium | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-ja-0040` | ring | ring_theory | medium | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-ja-0041` | prime ideal | ring_theory | medium | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-ja-0001` | algebra | algebra_core | normal | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-ja-0002` | basis theorem | commutative_algebra | normal | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-ja-0003` | localization | commutative_algebra | normal | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-ja-0004` | field | field_theory | normal | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-ja-0014` | isomorphism | morphism | normal | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-ja-0015` | homomorphism | morphism | normal | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-ja-0016` | automorphism | morphism | normal | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-ja-0017` | endomorphism | morphism | normal | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-ja-0021` | norm | number_theory | normal | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-ja-0022` | ring of integers | number_theory | normal | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-ja-0023` | decomposition of primes | number_theory | normal | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-ja-0024` | class number | number_theory | normal | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |

## prs_AF

- Packet template key: `persian_family`
- Required reviewer roles: iranian_persian_mathematical_reviewer, dari_afghan_persian_educator_or_technical_reviewer, tajik_cyrillic_reviewer, rtl_or_script_reviewer
- Priority checks: separate_sublane_decisions, core_algebra_and_invariant_theory_terms, advanced_algebra_vs_broad_educational_source_coverage, script_directionality_numerals_punctuation_formula_alignment
- Blocking concerns: treating_fa_prs_tg_as_one_lane_without_external_rationale, tajik_cyrillic_terms_missing_from_evidence_shelf, rtl_rendering_affects_formulas_citations_or_glossary_alignment
- Lane extra checks: dari_afghan_persian_source_reinforcement_flag, sublane_isolation_flag

| Term ID | English concept | Domain | Priority | State | Required action |
| --- | --- | --- | --- | --- | --- |
| `term-prs-af-0001` | algebra | algebra_core | high | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-prs-af-0002` | field | field_theory | high | manual_or_source_review_required_before_reviewer_packet_row | manual_source_review_plus_register_or_ocr_check_before_packet_population |
| `term-prs-af-0003` | simple | representation_theory | high | manual_or_source_review_required_before_reviewer_packet_row | manual_source_review_plus_register_or_ocr_check_before_packet_population |
| `term-prs-af-0004` | ring | ring_theory | high | manual_or_source_review_required_before_reviewer_packet_row | manual_source_review_plus_register_or_ocr_check_before_packet_population |

## simplified_chinese

- Packet template key: `simplified_chinese`
- Required reviewer roles: native_simplified_chinese_mathematical_reviewer, chinese_tex_pdf_visual_reviewer, optional_undergraduate_educator_reviewer
- Priority checks: core algebra and invariant theory terms, mainland_usage_vs_marked_or_incorrect_usage, section_headings_and_theorem_proof_transitions, formula_and_label_layout_in_chinese_text
- Blocking concerns: term choice changes mathematical scope, ocr_or_source_anchor_ambiguity_promoted_without_page_inspection, pdf layout issue affects readability
- Lane extra checks: cjk_render_check, mainland_or_other_usage_note, formula_spacing_note

| Term ID | English concept | Domain | Priority | State | Required action |
| --- | --- | --- | --- | --- | --- |
| `term-zh-hans-0011` | right module | module_theory | high | manual_or_source_review_required_before_reviewer_packet_row | manual_source_review_for_specialist_term_before_packet_population |
| `term-zh-hans-0012` | submodule | module_theory | high | manual_or_source_review_required_before_reviewer_packet_row | manual_source_review_for_specialist_term_before_packet_population |
| `term-zh-hans-0013` | tensor product | module_theory | high | manual_or_source_review_required_before_reviewer_packet_row | manual_source_review_for_specialist_term_before_packet_population |
| `term-zh-hans-0014` | module | module_theory | high | manual_or_source_review_required_before_reviewer_packet_row | manual_source_review_for_specialist_term_before_packet_population |
| `term-zh-hans-0015` | module homomorphism | module_theory | high | manual_or_source_review_required_before_reviewer_packet_row | manual_source_review_for_specialist_term_before_packet_population |
| `term-zh-hans-0020` | Noether/Noetherian | noetherian | high | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-zh-hans-0021` | Noether/Noetherian | noetherian | high | manual_or_source_review_required_before_reviewer_packet_row | manual_source_review_for_specialist_term_before_packet_population |
| `term-zh-hans-0022` | irreducible representation | representation_theory | high | manual_or_source_review_required_before_reviewer_packet_row | manual_source_review_for_specialist_term_before_packet_population |
| `term-zh-hans-0023` | semisimple | representation_theory | high | manual_or_source_review_required_before_reviewer_packet_row | manual_source_review_for_specialist_term_before_packet_population |
| `term-zh-hans-0024` | completely reducible | representation_theory | high | manual_or_source_review_required_before_reviewer_packet_row | manual_source_review_for_specialist_term_before_packet_population |
| `term-zh-hans-0025` | character | representation_theory | high | manual_or_source_review_required_before_reviewer_packet_row | manual_source_review_for_specialist_term_before_packet_population |
| `term-zh-hans-0026` | group algebra | representation_theory | high | manual_or_source_review_required_before_reviewer_packet_row | manual_source_review_for_specialist_term_before_packet_population |
| `term-zh-hans-0027` | representation | representation_theory | high | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-zh-hans-0028` | representation theory | representation_theory | high | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-zh-hans-0009` | finitely generated | finiteness | medium | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-zh-hans-0010` | finite-dimensional | finiteness | medium | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-zh-hans-0029` | principal ideal | ring_theory | medium | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-zh-hans-0030` | commutative ring | ring_theory | medium | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-zh-hans-0031` | quotient ring | ring_theory | medium | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-zh-hans-0032` | maximal ideal | ring_theory | medium | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-zh-hans-0033` | ideal | ring_theory | medium | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-zh-hans-0034` | prime ideal | ring_theory | medium | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-zh-hans-0001` | ring | algebra_core | normal | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-zh-hans-0002` | group | algebra_core | normal | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-zh-hans-0003` | basis theorem | commutative_algebra | normal | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-zh-hans-0004` | localization | commutative_algebra | normal | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-zh-hans-0005` | abstract algebra | course_scope | normal | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-zh-hans-0006` | modern algebra | course_scope | normal | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-zh-hans-0007` | field | field_theory | normal | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-zh-hans-0008` | division ring | field_theory | normal | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-zh-hans-0016` | homomorphism | morphism | normal | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-zh-hans-0017` | isomorphism | morphism | normal | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-zh-hans-0018` | endomorphism | morphism | normal | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-zh-hans-0019` | automorphism | morphism | normal | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |

## spanish

- Packet template key: `spanish`
- Required reviewer roles: native_or_near_native_spanish_mathematical_reviewer, optional_undergraduate_algebra_or_physics_educator_reviewer
- Priority checks: spanish_algebra_and_invariant_theory_terminology, regional_variants_recorded_as_variants_or_errors, article_and_preposition_choices_in_mathematical_noun_phrases, learner_facing_clarity_vs_compact_specialist_style
- Blocking concerns: unlabeled_regional_terms_for_wide_readership, mixing_spanish_natural_language_evidence_with_romance_interlanguage_proposals
- Lane extra checks: regional_variant_note, article_preposition_check, learner_facing_clarity_note

| Term ID | English concept | Domain | Priority | State | Required action |
| --- | --- | --- | --- | --- | --- |
| `term-es-0008` | module | module_theory | high | manual_or_source_review_required_before_reviewer_packet_row | manual_source_review_for_specialist_term_before_packet_population |
| `term-es-0009` | quotient module | module_theory | high | manual_or_source_review_required_before_reviewer_packet_row | manual_source_review_for_specialist_term_before_packet_population |
| `term-es-0010` | tensor product | module_theory | high | manual_or_source_review_required_before_reviewer_packet_row | manual_source_review_for_specialist_term_before_packet_population |
| `term-es-0011` | submodule | module_theory | high | manual_or_source_review_required_before_reviewer_packet_row | manual_source_review_for_specialist_term_before_packet_population |
| `term-es-0016` | Noetherian ring | noetherian | high | manual_or_source_review_required_before_reviewer_packet_row | manual_source_review_for_specialist_term_before_packet_population |
| `term-es-0017` | Noetherian | noetherian | high | manual_or_source_review_required_before_reviewer_packet_row | manual_source_review_for_specialist_term_before_packet_population |
| `term-es-0018` | irreducible | representation_theory | high | manual_or_source_review_required_before_reviewer_packet_row | manual_source_review_for_specialist_term_before_packet_population |
| `term-es-0019` | representation | representation_theory | high | manual_or_source_review_required_before_reviewer_packet_row | manual_source_review_for_specialist_term_before_packet_population |
| `term-es-0020` | irreducible representation | representation_theory | high | manual_or_source_review_required_before_reviewer_packet_row | manual_source_review_for_specialist_term_before_packet_population |
| `term-es-0021` | semisimple | representation_theory | high | manual_or_source_review_required_before_reviewer_packet_row | manual_source_review_for_specialist_term_before_packet_population |
| `term-es-0007` | finitely generated | finiteness | medium | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-es-0022` | ring | ring_theory | medium | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-es-0023` | ideal | ring_theory | medium | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-es-0024` | maximal ideal | ring_theory | medium | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-es-0025` | prime ideal | ring_theory | medium | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-es-0001` | algebra | algebra_core | normal | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-es-0002` | Hilbert basis | commutative_algebra | normal | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-es-0003` | localization | commutative_algebra | normal | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-es-0004` | Hilbert basis theorem | commutative_algebra | normal | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-es-0005` | commutative algebra | commutative_algebra | normal | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-es-0006` | field | field_theory | normal | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-es-0012` | automorphism | morphism | normal | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-es-0013` | endomorphism | morphism | normal | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-es-0014` | homomorphism | morphism | normal | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |
| `term-es-0015` | isomorphism | morphism | normal | ready_after_extraction_check_needs_human_page_context_note | add_human_page_context_note_then_populate_reviewer_packet_row |

## Boundaries

- No source-language term strings or source passages are copied here.
- No credentials or tokens are copied here.
- No network action, GitHub upload, or reviewer send is performed here.
- No reviewer-packet rows are populated by this scaffold.
- No native/external review result is implied.
- No term is approved for canonical use.
- Every row remains blocked until the required context or manual/source note is filled.
