# Interlingual Marker Table — v3 master

Master table: all concepts presently exposed by the marker table, union spine, C2 core, concept ledger, W/S backfill, and weighted-score rows. It extends v1 from 138 to **212** concepts, adding weighted/source rows such as `quotient field` that were not in the v1 marker table.

## Totals

- Base marker concepts: **138**.
- Master concepts: **212**.
- Extra concepts added: **74**.
- Priority distribution: `{'A_review_now': 2, 'B_variant_or_backfill': 5, 'C_core_fill_or_source_intake': 24, 'D_background': 181}`.

## Evidence weights

| Channel | Weight |
| --- | ---: |
| `community_review` | 1.00 |
| `row_verified_native_witness` | 1.00 |
| `canonical_source_normalization` | 0.90 |
| `native_concept_shelf` | 0.75 |
| `mechanical_probe` | 0.50 |
| `generated_internal_consistency` | 0.35 |
| `cross_lane_spine` | 0.20 |
| `draft_triangulation` | 0.15 |
| `model_scoring` | 0.10 |

## Top priority rows

| Rank | Concept | Score | Band | Risk flags | Main source cues |
| ---: | --- | ---: | --- | --- | --- |
| 1 | `ring` | 90 | A_review_now | review_priority; WS_competitor_only_both; internal_variance | bg:bulgarian_sofia_noncommutative_body_problem.txt; cs:czech_cuni_algebra_2021.txt; hr:croatian_mathhr_algebra_structures_2024.txt; interslavic:noether_paper02_section03_terms.json; malay_indonesian:U |
| 2 | `quotient field` | 68 | A_review_now | review_priority; WS_competitor_only_one_branch; internal_variance | ws:czech_cuni_algebra_2021.txt; ws:czech_karlin_commutative_rings_fields.txt; ws:polish_impan_algebra_lecture3.txt; ws:polish_uj_algebra1_noetherian.txt |
| 3 | `corollary` | 40 | B_variant_or_backfill | variant_or_doublet_note; WS_competitor_only_one_branch | bg:bulgarian_sofia_rings_lecture7.txt; cs:czech_cuni_algebra_2021.txt; hr:croatian_mathhr_algebra_structures_2024.txt; malay_indonesian:Neliti consequence rows; UM terminology rows; pl:polish_mimuw_al |
| 4 | `theorem` | 40 | B_variant_or_backfill | variant_or_doublet_note; WS_competitor_only_one_branch | bg:bulgarian_sofia_noncommutative_body_problem.txt; cs:czech_cuni_algebra_2021.txt; hr:croatian_mathhr_algebra_structures_2024.txt; malay_indonesian:UKM theorem rows; UIN/Neliti theorem labels; pan_ro |
| 5 | `extension (field)` | 30 | B_variant_or_backfill | variant_or_doublet_note; WS_competitor_only_one_branch | ws:croatian_mathhr_algebra_structures_2024.txt; ws:croatian_pmf_split_prsteni.txt; ws:czech_cuni_algebra_2021.txt; ws:czech_cuni_noncommutative_body_thesis.txt; ws:czech_cuni_representation_idempotent |
| 6 | `splitting field` | 30 | B_variant_or_backfill | variant_or_doublet_note; WS_competitor_only_one_branch | ws:czech_cuni_algebra_2021.txt; ws:czech_cuni_noncommutative_body_thesis.txt; ws:czech_cuni_representation_idempotents.txt; ws:czech_karlin_commutative_rings_fields.txt; ws:czech_karlin_galois_splitti |
| 7 | `trace` | 30 | B_variant_or_backfill | variant_or_doublet_note; WS_competitor_only_one_branch | ws:bulgarian_sofia_noncommutative_body_problem.txt; ws:bulgarian_sofia_rings_lecture7.txt; ws:czech_cuni_representation_idempotents.txt; ws:czech_karlin_commutative_rings_fields.txt; ws:polish_mimuw_n |
| 8 | `covariant` | 22 | C_core_fill_or_source_intake | C2_pending_specialist_or_context | interslavic:noether_paper02_section19_terms.json; malay_indonesian:UM terminology covariant row |
| 9 | `determinant` | 22 | C_core_fill_or_source_intake | variant_or_doublet_note | cs:czech_cuni_algebra_2021.txt; hr:croatian_mathhr_algebra_structures_2024.txt; interslavic:noether_paper02_section01_terms.json; interslavic:noether_paper02_section03_terms.json; interslavic:noether_ |
| 10 | `polynomial` | 22 | C_core_fill_or_source_intake | variant_or_doublet_note | cs:czech_cuni_algebra_2021.txt; hr:croatian_mathhr_algebra_structures_2024.txt; malay_indonesian:UIN polynomial rows; UKM/UM terminology; pl:polish_impan_algebra_lecture3.txt; sk:slovak_abstraktna_alg |
| 11 | `absolutely complete system` | 18 | C_core_fill_or_source_intake | C2_pending_specialist_or_context; source_gap |  |
| 12 | `binary form` | 18 | C_core_fill_or_source_intake | C2_pending_specialist_or_context; source_gap |  |
| 13 | `biquadratic form` | 18 | C_core_fill_or_source_intake | C2_pending_specialist_or_context; source_gap |  |
| 14 | `complete system` | 18 | C_core_fill_or_source_intake | C2_pending_specialist_or_context; source_gap |  |
| 15 | `contravariant` | 18 | C_core_fill_or_source_intake | C2_pending_specialist_or_context; source_gap |  |
| 16 | `elementary divisor` | 18 | C_core_fill_or_source_intake | C2_pending_specialist_or_context | pan_romance:es:cum_es.tex:10174; pan_romance:fr:translations/paper22/french/v001/Noether_Paper22_Intro_Section01_French_v001.tex:69 |
| 17 | `form system` | 18 | C_core_fill_or_source_intake | C2_pending_specialist_or_context | interslavic:noether_paper02_section03_terms.json |
| 18 | `ground form` | 18 | C_core_fill_or_source_intake | C2_pending_specialist_or_context; source_gap |  |
| 19 | `invariant theory` | 18 | C_core_fill_or_source_intake | C2_pending_specialist_or_context | interslavic:noether_paper02_section01_terms.json |
| 20 | `modulus` | 18 | C_core_fill_or_source_intake | C2_pending_specialist_or_context; source_gap |  |
| 21 | `reduction` | 18 | C_core_fill_or_source_intake | C2_pending_specialist_or_context | interslavic:noether_paper02_section03_terms.json; interslavic:noether_paper02_section06_terms.json; interslavic:noether_paper02_section07_terms.json; interslavic:noether_paper02_section15_terms.json |
| 22 | `relatively complete system` | 18 | C_core_fill_or_source_intake | C2_pending_specialist_or_context | interslavic:noether_paper02_section03_terms.json; interslavic:noether_paper02_section07_terms.json |
| 23 | `resultant` | 18 | C_core_fill_or_source_intake | C2_pending_specialist_or_context | malay_indonesian:UM terminology resultant rows |
| 24 | `ternary form` | 18 | C_core_fill_or_source_intake | C2_pending_specialist_or_context; source_gap |  |
| 25 | `transvection` | 18 | C_core_fill_or_source_intake | C2_pending_specialist_or_context | interslavic:noether_paper02_section03_terms.json; interslavic:noether_paper02_section19_terms.json |
| 26 | `identity` | 14 | C_core_fill_or_source_intake | C2_pending_specialist_or_context | malay_indonesian:Indonesian algebra rows; Malay terminology; pan_romance:es:cum_es.tex:482; pan_romance:fr:french/1001.2849v1/1001.2849v1.tex:1050 |
| 27 | `invariant` | 14 | C_core_fill_or_source_intake |  | cs:czech_cuni_algebra_2021.txt; hr:croatian_mathhr_algebra_structures_2024.txt; malay_indonesian:UM terminology invariant rows; pan_romance:es:cum_es.tex:293; pan_romance:fr:cum_fr_P19s12.tex:168; ws: |
| 28 | `proposition` | 14 | C_core_fill_or_source_intake | C2_pending_specialist_or_context | malay_indonesian:UM Surabaya proposition row; UKM proof-course prose |
| 29 | `respectively` | 14 | C_core_fill_or_source_intake | C2_pending_specialist_or_context | pan_romance:es:cum_es.tex:330; pan_romance:fr:cum_fr_P19s12.tex:358 |
| 30 | `therefore` | 14 | C_core_fill_or_source_intake | C2_pending_specialist_or_context | pan_romance:es:cum_es.tex:347; pan_romance:fr:cum_fr_P19s12.tex:380 |
| 31 | `vector space` | 14 | C_core_fill_or_source_intake | C2_pending_specialist_or_context | malay_indonesian:UKM course row |
| 32 | `algebra` | 10 | D_background |  | bg:bulgarian_sofia_noncommutative_body_problem.txt; cs:czech_cuni_algebra_2021.txt; hr:croatian_mathhr_algebra_structures_2024.txt; malay_indonesian:Neliti/UIN; UKM course rows; pan_romance:es:cum_es. |
| 33 | `basis` | 10 | D_background |  | bg:bulgarian_sofia_noncommutative_body_problem.txt; malay_indonesian:UPM/UKM course rows; Indonesian sparse hit; pan_romance:es:cum_es.tex:291; pan_romance:fr:cum_fr_P19s12.tex:198; ws:bulgarian_sofia |
| 34 | `definition` | 10 | D_background |  | bg:bulgarian_sofia_rings_lecture7.txt; cs:czech_cuni_algebra_2021.txt; hr:croatian_mathhr_algebra_structures_2024.txt; malay_indonesian:Neliti/UIN definitions; UKM mentakrif; pan_romance:es:cum_es.tex |
| 35 | `dimension` | 10 | D_background |  | cs:czech_cuni_algebra_2021.txt; hr:croatian_mathhr_algebra_structures_2024.txt; malay_indonesian:UM/UPM terminology rows; pl:polish_mimuw_algebra2_galois.txt; sk:slovak_abstraktna_algebra.txt; sl:slov |
