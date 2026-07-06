# Interslavic weighted-automaton reconciliation v2.1

Generated: 2026-07-05.

## Verdict

`INTERSLAVIC_WEIGHTED_AUTOMATON_ANALYSIS_v2` is structurally useful as an automaton/evidence-graph layer, but its headline branch masses are not the current certified branch masses. The current certified row-level state is **state C** from `F10_AUDIT_postwriteback_20260704.json` / `BRANCH_WEIGHTING_STATE_D_20260705.json`.

## Current number to quote

| State | E | W | S | p_E | p_W | p_S | D1 | KL |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| state C authoritative row-level | 2341 | 223 | 239 | 0.835177 | 0.079558 | 0.085266 | 1.753704 | 0.536882 |

In prose: **state C = E 2341, W 223, S 239; D1 = 1.753704 effective branches out of 3.**

## Numbers not to quote as current

| State | Why not current | E | W | S | D1 |
|---|---|---:|---:|---:|---:|
| v0 baseline | frozen archaeology baseline before W/S writeback | 2395 | 64 | 59 | 1.257252 |
| automaton v2 certified/current | built on old v1 ledger / old term IDs | 2396.0 | 167.0 | 169.0 | 1.581035 |
| automaton v2 candidate-after-review | projection, not certified | 2396.0 | 317.8 | 319.8 | 1.934557 |
| state D candidate | explicitly withdrawn as headline | 3730 | 7157 | 14222 | 2.62 |

## Reconciliation of F10-1 counts

- `947` = row-level F10-1 count in `F10_AUDIT_postwriteback_20260704.json`.
- `934` = unique `term_id` count after duplicate collapse; this is why `TAIL_WITNESS_ROUTING_v1` routes 934 under-witnessed rows.
- `961` = automaton v2 F10-1 count over the old v1/1254-row ledger snapshot.

## Causes of drift

1. **Input generation drift.** Automaton v2 used `INTERSLAVIC_LEDGER_RETROFIT_v1` / `F10_v1` with 1254 rows and older `ISV-unnamed--...` IDs. State C uses `F10_AUDIT_postwriteback_20260704.json` with 1229 rows and repaired German-key IDs.
2. **Duplicate accounting.** State C has 947 row-level F10-1 entries but 934 unique F10-1 term IDs.
3. **ID normalization drift.** 416 automaton rows map to state C by unique chosen form rather than by same term ID; 9 have ambiguous-form matches.
4. **Witness-vector drift.** 85 matched rows have changed E/W/S vectors. The net row-level headline shift from automaton v2 to state C is **E -55.0, W +56.0, S +70.0**.

## Output files

- `INTERSLAVIC_AUTOMATON_STATE_RECONCILIATION_v2_1_20260705.csv`
- `INTERSLAVIC_F10_COUNT_RECONCILIATION_v2_1_20260705.csv`
- `INTERSLAVIC_AUTOMATON_ROW_DRIFT_MAP_v2_1_20260705.csv`
- `INTERSLAVIC_AUTOMATON_ROW_DRIFT_DIFFS_v2_1_20260705.csv`
- `INTERSLAVIC_AUTOMATON_STATE_C_CANONICAL_TERMS_v2_1_20260705.csv`
- `INTERSLAVIC_AUTOMATON_RECONCILIATION_v2_1_20260705.json`

## Next production rule

Rebuild any future full weighted automaton from `F10_AUDIT_postwriteback_20260704.json` plus the latest Route-A/Route-B review files, not from `INTERSLAVIC_LEDGER_RETROFIT_v1`. Keep v2 as an architecture/edge-schema artifact, not as the current measurement.
