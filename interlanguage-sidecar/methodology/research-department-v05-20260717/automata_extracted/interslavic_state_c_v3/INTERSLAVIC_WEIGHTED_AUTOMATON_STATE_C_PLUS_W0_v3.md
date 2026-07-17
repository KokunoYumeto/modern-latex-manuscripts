# Interslavic weighted automaton — State C + W0 filtered projection v3

Generated 2026-07-05.

## Boundary

This is a current-state evidence automaton, not a certification pass.

- **State C** is the current certified measurement layer after postwriteback reconciliation.
- **W0 projection** applies only the 182 filtered W0 candidates as a *candidate-after-source-row-context-check* projection.
- The 52 failed W0 rows are held in a separate targeted-review queue.
- No production text is changed.
- No bridge form is promoted.

## Counts

| Object | Count |
|---|---:|
| State C term rows | 1,229 |
| Unique term IDs | 1,215 |
| Rows sharing duplicate term IDs | 27 |
| Concept buckets | 100 |
| Automaton transition edges | 9,124 |
| Filtered W0 candidate rows | 183 |
| Filtered W0 rows adding new W/S support in projection | 110 |
| W0 rows held for targeted review | 52 |

## Branch summary

| state                                                 |    E |   W |   S |   total_family_mass |   share_E |   share_W |   share_S |   effective_branches_D1 |   KL_to_balanced |
|:------------------------------------------------------|-----:|----:|----:|--------------------:|----------:|----------:|----------:|------------------------:|-----------------:|
| state_C_current_certified                             | 2341 | 223 | 239 |                2803 |  0.835177 | 0.0795576 | 0.0852658 |                 1.7537  |         0.536882 |
| state_C_plus_W0_filtered_projection_after_row_context | 2341 | 333 | 348 |                3022 |  0.774653 | 0.110192  | 0.115156  |                 1.99319 |         0.408875 |

## Action-band counts

| v3_action_band                                 |   rows |
|:-----------------------------------------------|-------:|
| MISSING_WITNESS_continue_tail_routing          |    785 |
| CURRENT_low_priority_or_document               |    203 |
| CANDIDATE_W0_filtered_add_WS_after_row_context |    110 |
| HOLD_targeted_review_not_writeback             |     52 |
| ADVERSE_or_dominance_review_packet             |     41 |
| OVERCLAIM_backfill_needed                      |     19 |
| AUTHORITY_or_specialist_review                 |     19 |

## Automaton shape

```text
q0_START
  -> q1_SOURCE
  -> q2_CONCEPT
  -> q3_ISV_FORM
  -> q4_SUPPORT_E/W/S/I/X
  -> q4_GAP_W/S
  -> q4_ADVERSE_COMPETITOR_OR_FLAG
  -> q4_CANDIDATE_SUPPORT_W/S
  -> q5_DECISION
```

Support, adverse, gap, and candidate channels remain separated. Candidate W0 support is not added to the certified State C number; it appears only in the projection columns.

## Current quotable branch number

The current quotable number remains State C:

```text
E = 2341
W = 223
S = 239
D1 = 1.753704
KL = 0.536882
distribution = 83.52% / 7.96% / 8.53%
```

## Candidate W0 projection

If the filtered W0 rows are accepted after source-row context check, the projected mass becomes:

```text
E = 2341
W = 333
S = 348
D1 = 1.993192
KL = 0.408875
distribution = 77.47% / 11.02% / 11.52%
```

This is a projection only. It is useful for planning the writeback pass; it is not the current measurement.

## Files

- `INTERSLAVIC_WEIGHTED_AUTOMATON_STATE_C_PLUS_W0_TERM_LEDGER_v3.csv`
- `INTERSLAVIC_WEIGHTED_AUTOMATON_STATE_C_PLUS_W0_EDGES_v3.csv`
- `INTERSLAVIC_BRANCH_SUMMARY_STATE_C_PLUS_W0_v3.csv`
- `INTERSLAVIC_CONCEPT_SUMMARY_STATE_C_PLUS_W0_v3.csv`
- `INTERSLAVIC_ROW_UID_DUPLICATE_ID_MAP_v3.csv`
- `INTERSLAVIC_W0_FILTERED_PROJECTION_QUEUE_v3.csv`
- `INTERSLAVIC_W0_HOLD_TARGETED_REVIEW_v3.csv`
