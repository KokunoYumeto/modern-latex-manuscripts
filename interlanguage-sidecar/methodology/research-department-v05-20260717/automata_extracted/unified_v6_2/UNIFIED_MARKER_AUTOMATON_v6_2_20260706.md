# Unified interlanguage marker automaton v6.2

Generated 2026-07-06. This pass ingests the interlanguage sidecar dump and the July-04 final handoff, including Arabic RTL, CJK, Turkic frontier, OLP support, R3 standardization ledgers, and the final Fable context/normalization logs.

## Boundary

Weights are permitted-use weights, not truth or certification. Native source-body rows can become witness candidates after row-context review; draft/generated rows only support internal consistency or discovery; do-not-use and false-sense rows stay in adverse channels.

## Counts

- Marker/evidence rows: **1522**

- Weighted graph edges: **6088**

- Concepts: **362**

- Lanes: **15**

- Source/artifact files indexed: **1715**

- Trap/adverse queue rows: **63**


## Lane summary

| lane                       |   concepts |   markers |   languages |   support_rows |   candidate_rows |   adverse_competitor_rows |   gap_rows |   support_candidate_mass |   adverse_mass |   readiness_proxy_0_100 | next_action                    |
|:---------------------------|-----------:|----------:|------------:|---------------:|-----------------:|--------------------------:|-----------:|-------------------------:|---------------:|------------------------:|:-------------------------------|
| pan_romance                |         93 |       543 |           8 |            139 |              401 |                         3 |          0 |                  244.2   |            2.7 |                    98.5 | sense_audit_and_adverse_review |
| slavic_east                |         66 |       125 |           2 |              0 |              125 |                         0 |          0 |                   34.2   |            0   |                    97.2 | sourcebody_context_review      |
| interslavic                |         79 |       117 |           2 |              0 |              117 |                         0 |          0 |                   31     |            0   |                    96.9 | sourcebody_context_review      |
| persianate                 |         62 |        62 |           1 |              0 |               62 |                         0 |          0 |                   30.4   |            0   |                    96.8 | sourcebody_context_review      |
| malay_indonesian           |         60 |        60 |           1 |              0 |               60 |                         0 |          0 |                   24.8   |            0   |                    96.1 | sourcebody_context_review      |
| interslavic_proof_register |         67 |        67 |           1 |              0 |               67 |                         0 |          0 |                   23.45  |            0   |                    95.9 | sourcebody_context_review      |
| turkic_source_canon        |          8 |        19 |           3 |             19 |                0 |                         0 |          0 |                   10.315 |            0   |                    91.2 | sourcebody_context_review      |
| controlled_arabic          |         75 |        92 |           3 |             16 |               71 |                         5 |          0 |                   47.55  |            4.5 |                    89.6 | sense_audit_and_adverse_review |
| cjk                        |         90 |       195 |           4 |              0 |              184 |                        11 |          0 |                   77.25  |            9.9 |                    87.6 | sense_audit_and_adverse_review |
| slavic_south               |         38 |        92 |           3 |             72 |                0 |                        20 |          0 |                   54     |           15   |                    77.1 | sense_audit_and_adverse_review |
| arabic_farsi_persianate    |          4 |         4 |           1 |              2 |                2 |                         0 |          0 |                    2.2   |            0   |                    68.8 | sourcebody_context_review      |
| turkic_frontier            |          5 |         9 |           5 |              4 |                0 |                         0 |          5 |                    1.4   |            0   |                    58.3 | sourcebody_context_review      |
| slavic_west                |         39 |       107 |           3 |             61 |                0 |                        46 |          0 |                   45.75  |           34.5 |                    56.3 | sense_audit_and_adverse_review |
| generic                    |         16 |        16 |           1 |              0 |                0 |                        16 |          0 |                    0     |           14.4 |                     0   | sense_audit_and_adverse_review |
| olp_source_side            |         14 |        14 |           1 |              0 |                0 |                         0 |          0 |                    0     |            0   |                     0   | source_collection_or_mapping   |


## Top review / trap rows

| concept                                                                          |   lane_count |   language_count |   support_mass |   adverse_or_competitor_mass | risk_flags                                        | recommended_next_action   |
|:---------------------------------------------------------------------------------|-------------:|-----------------:|---------------:|-----------------------------:|:--------------------------------------------------|:--------------------------|
| covariant                                                                        |            4 |                5 |           2.4  |                          0   | F14_trap_candidate                                | P0_sense_audit            |
| ground form                                                                      |            5 |                8 |           1.95 |                          0.9 | has_adverse_or_competitor;F14_trap_candidate      | P0_sense_audit            |
| modulus                                                                          |            3 |                5 |           4.15 |                          0   | F14_trap_candidate                                | P0_sense_audit            |
| contravariant                                                                    |            3 |                4 |           1.75 |                          0   | F14_trap_candidate                                | P0_sense_audit            |
| binary form                                                                      |            3 |                3 |           0.4  |                          0.9 | has_adverse_or_competitor;F14_trap_candidate      | P0_sense_audit            |
| complete system                                                                  |            3 |                3 |           0.4  |                          0.9 | has_adverse_or_competitor;F14_trap_candidate      | P0_sense_audit            |
| absolutely complete system                                                       |            2 |                2 |           0.4  |                          0   | F14_trap_candidate                                | P0_sense_audit            |
| relatively complete system                                                       |            2 |                2 |           0.4  |                          0   | F14_trap_candidate                                | P0_sense_audit            |
|                                                                                  |            1 |                0 |           0    |                          0.9 | has_adverse_or_competitor;adverse_without_support | P0_sense_audit            |
| ALL                                                                              |            1 |                0 |           0    |                          0.9 | has_adverse_or_competitor;adverse_without_support | P0_sense_audit            |
| CJK-W4-LEX-artin-artinian-finiteness-d5fab98be6                                  |            1 |                0 |           0    |                          0.9 | has_adverse_or_competitor;adverse_without_support | P0_sense_audit            |
| CJK-W4-LEX-completely-reducible-representation-theory-16a17e71af                 |            1 |                0 |           0    |                          0.9 | has_adverse_or_competitor;adverse_without_support | P0_sense_audit            |
| CJK-W4-LEX-harish-chandra-representation-theory-a419b6bd13                       |            1 |                0 |           0    |                          0.9 | has_adverse_or_competitor;adverse_without_support | P0_sense_audit            |
| Korean rows are addendum/source-routing unless exact owner evidence changes that |            1 |                0 |           0    |                          0.9 | has_adverse_or_competitor;adverse_without_support | P0_sense_audit            |
| all                                                                              |            1 |                0 |           0    |                          0.9 | has_adverse_or_competitor;adverse_without_support | P0_sense_audit            |
| all ledgers                                                                      |            1 |                0 |           0    |                          0.9 | has_adverse_or_competitor;adverse_without_support | P0_sense_audit            |
| all relation/function terms                                                      |            1 |                0 |           0    |                          0.9 | has_adverse_or_competitor;adverse_without_support | P0_sense_audit            |
| ar-lex-field                                                                     |            1 |                0 |           0    |                          0.9 | has_adverse_or_competitor;adverse_without_support | P0_sense_audit            |
| ar-lex-homomorphism                                                              |            1 |                0 |           0    |                          0.9 | has_adverse_or_competitor;adverse_without_support | P0_sense_audit            |
| ar-lex-isomorphism                                                               |            1 |                0 |           0    |                          0.9 | has_adverse_or_competitor;adverse_without_support | P0_sense_audit            |
| ar-lex-ring                                                                      |            1 |                0 |           0    |                          0.9 | has_adverse_or_competitor;adverse_without_support | P0_sense_audit            |
| cross-Turkic transfer                                                            |            1 |                0 |           0    |                          0.9 | has_adverse_or_competitor;adverse_without_support | P0_sense_audit            |
| draft scaffolds are generated-draft/non-canonical review material only           |            1 |                0 |           0    |                          0.9 | has_adverse_or_competitor;adverse_without_support | P0_sense_audit            |
| function terminology                                                             |            1 |                0 |           0    |                          0.9 | has_adverse_or_competitor;adverse_without_support | P0_sense_audit            |
| generated output is not a native source witness                                  |            1 |                0 |           0    |                          0.9 | has_adverse_or_competitor;adverse_without_support | P0_sense_audit            |


## Files

- `UNIFIED_MARKER_AUTOMATON_MARKERS_v6_2_20260706.csv`
- `UNIFIED_MARKER_AUTOMATON_EDGES_v6_2_20260706.csv`
- `UNIFIED_MARKER_AUTOMATON_CONCEPT_SUMMARY_v6_2_20260706.csv`
- `UNIFIED_MARKER_AUTOMATON_LANE_SUMMARY_v6_2_20260706.csv`
- `SOURCE_BODY_AND_ARTIFACT_INDEX_v6_2_20260706.csv`
- `TRAP_ADVERSE_REVIEW_QUEUE_v6_2_20260706.csv`
- `UNIFIED_INTERLANGUAGE_WORKLIST_v6_2_20260706.csv`
- `UNIFIED_MARKER_AUTOMATON_v6_2_20260706.json`