# Interslavic full term-weight ledger — v1

Generated 2026-07-05. Scope: all 1254 Interslavic term rows from the retrofit/index layer, joined to F10 status, witness vectors, W/S support/adverse evidence where concept-linked, weighted-score rows where available, and v9/v11 writeback queues.

This is a deliverable ledger, not a certification artifact. The weights are operational triage/use weights: they say what can be trusted for which next action, not that a bridge term has been community-approved.

## Files

- `INTERSLAVIC_FULL_TERM_WEIGHT_LEDGER_v1_20260705.csv` — full row-level ledger.
- `INTERSLAVIC_FULL_TERM_WEIGHT_LEDGER_v1_20260705.json` — machine-readable full ledger + schema.
- `INTERSLAVIC_CONCEPT_WEIGHT_SUMMARY_v1_20260705.csv/json` — concept-level aggregation.
- `INTERSLAVIC_TERM_REVIEW_AND_WRITEBACK_QUEUE_v1_20260705.csv` — non-background rows sorted into review/writeback bands.
- `INTERSLAVIC_FULL_TERM_WEIGHT_LEDGER_v1_20260705.xlsx` — workbook version with README/schema/ledger/summary/queue sheets.

## Weight components

| Component | Meaning |
|---|---|
| `witness_E/W/S/I/X` | recorded witness vector; E/W/S are family branches, I=Interslavic authority, X=international |
| `effective_branch_count_D1` | Hill-number effective branch count over E/W/S |
| `branch_breadth_weight` | how many of E/W/S are present, divided by 3 |
| `branch_balance_weight` | D1 divided by 3 |
| `source_strength_weight` | saturating score from branch + I/X witness mass |
| `ws_support_score` / `ws_adverse_competitor_score` | log-scaled support vs competitor ratio from W/S shelf when concept-linked |
| `writeback_candidate_weight` | candidate evidence-readiness from v9/v11 context-review queues |
| `operational_term_weight_0_100` | combined triage score; not a truth score |

## Distributions

F10 flags: {'F10-0': 213, 'F10-1': 961, 'F10-3': 42, 'F10-2': 20, 'F10-4': 18}

Recommended action bands: {'G_currently_acceptable_or_low_priority': 211, 'F_missing_witness_backfill': 640, 'C_context_candidate_writeback': 235, 'B_candidate_witness_writeback': 62, 'A_review_adverse_or_competitor': 68, 'E_overclaim_backfill_needed': 20, 'D_authority_or_specialist_needed': 18}

Operational weight bands: {'D_underwitnessed': 753, 'B_usable_candidate_or_balanced': 95, 'A_high_support_or_apply_ready': 52, 'C_partial_or_review_needed': 121, 'E_gap_or_adverse': 233}

## Read rule

- A high score means the row is well supported or ready for candidate ledger writeback under source-use rules.
- A low score can mean true gap, East-only status, adverse competitor evidence, or specialist-review need.
- `ring`, `field`, `polynomial`, and similar competitor-channel rows deliberately do not become clean support rows merely because source hits exist.
