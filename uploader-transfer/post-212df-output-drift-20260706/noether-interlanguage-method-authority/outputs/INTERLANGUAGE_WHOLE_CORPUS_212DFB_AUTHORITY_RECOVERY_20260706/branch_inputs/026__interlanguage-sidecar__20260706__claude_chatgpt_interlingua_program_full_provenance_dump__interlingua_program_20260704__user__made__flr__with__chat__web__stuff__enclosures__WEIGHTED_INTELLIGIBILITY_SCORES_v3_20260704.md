# Weighted marginal-intelligibility scores — v3 correction

2026-07-04. Supersedes `WEIGHTED_INTELLIGIBILITY_SCORES_v2_20260704`. No term is promoted; this is a scoring/proxy review artifact only.

## What changed from v2

- Corrected **quotient field** current Interslavic form from the placeholder `polje častnikov?` to the attested internal variants `polje kvocientov` / `kvocientno polje`.

- Recomputed population-proxy scores using a source-pinned Europe native-speaker table rather than the previous unsourced rough proxy. Population weighting remains a sensitivity model, not an editorial decision rule.

- Preserved adverse/veto separation: collisions and adverse relations are constraints, not negative summands inside positive support.

## Population-proxy table used for v3

| Cohort | Count used (millions) | Composition |
|---|---:|---|
| `E` | 141.9 | Russian 106.0 + Ukrainian 32.6 + Belarusian 3.3 |
| `W_cs_sk` | 15.8 | Czech 10.6 + Slovak 5.2 |
| `W_pl` | 38.0 | Polish 38.0 |
| `S_hr_sr` | 19.0 | Serbo-Croatian aggregate 19.0 |
| `S_sl` | 2.1 | Slovene 2.1 |
| `S_bg` | 7.8 | Bulgarian 7.8 |

Normalization total: 224.6 million. Use only as provisional sensitivity weights; replace before publication if population weighting matters.

## Headline rows

| Concept | Current form | Class | Sensitivity | Equal-branch top | Population-proxy top | Dependence-corrected top | Note |
|---|---|---|---|---|---|---|---|
| ring | `kolco` | review_priority | weight_sensitive | prsten / pierścień / prăsten coalition | kolco | prsten / pierścień / prăsten coalition | review packet row; prsten coalition wins branch/dependence, kolco wins population proxy. |
| quotient field | `polje kvocientov / kvocientno polje` | review_priority | weight_sensitive | West native quotient-field terms | kvocient-family current variants | West native quotient-field terms | review packet row; current has internal word-order variance; West competitor-only, South no-hit. |
| theorem | `teorema` | variant_or_doublet_note | stable | teorema | teorema | teorema | F12 West-calque/native-pressure row; variant/doublet note, not replacement. |
| corollary | `korolar?` | variant_or_doublet_note | stable | korolar? | korolar? | korolar? | F12 West-calque/native-pressure row; variant/doublet note, not replacement. |
| trace | `sled?` | variant_or_doublet_note | stable | sled? | sled? | sled? | F12 West-calque/native-pressure row; variant/doublet note, not replacement. |
| extension (field) | `razširjenje?` | variant_or_doublet_note | weight_sensitive | W/S extension-family alternatives | razširjenje? | W/S extension-family alternatives | F12 West-calque/native-pressure row; variant/doublet note, not replacement. |
| splitting field | `razpadno polje` | variant_or_doublet_note | stable | razpadno polje | razpadno polje | razpadno polje | confirm or variant-policy row. |
| determinant | `determinanta` | variant_or_doublet_note | stable | determinanta | determinanta | determinanta | Polish native competitor, but current international form remains top under all schemes. |
| polynomial | `polinom` | variant_or_doublet_note | stable | polinom | polinom | polinom | Polish native competitor, but current international form remains top under all schemes. |

## Review-priority details

### ring

Current: `kolco`. Action: **review_priority**. Sensitivity: **weight_sensitive**.

| Candidate | Cohorts | Veto? | Equal branch | Equal splits | Population proxy | Dependence PD | Notes |
|---|---|---:|---:|---:|---:|---:|---|
| kolco | E | false | 0.333 | 0.333 | 0.632 | 0.182 |  |
| prsten / pierścień / prăsten coalition | S_bg, S_hr_sr, W_pl | false | 0.667 | 0.389 | 0.289 | 0.636 | branch-attested cognate family; review question, not promotion |
| okruh family | W_cs_sk | true | 0.333 | 0.167 | 0.070 | 0.273 | adverse/collision-sensitive: okruh may collide with East Slavic okrug/district; do-not-use ledger contains kolco dominance-risk but no direct okruh row |
| kolobar | S_sl | false | 0.333 | 0.111 | 0.009 | 0.273 |  |

### quotient field

Current: `polje kvocientov / kvocientno polje`. Action: **review_priority**. Sensitivity: **weight_sensitive**.

v3 correction: the earlier `polje častnikov?` placeholder is withdrawn. The current corpus forms are `polje kvocientov` and `kvocientno polje`; this is itself an internal-variance issue.

| Candidate | Cohorts | Veto? | Equal branch | Equal splits | Population proxy | Dependence PD | Notes |
|---|---|---:|---:|---:|---:|---:|---|
| kvocient-family current variants | E | false | 0.333 | 0.333 | 0.632 | 0.182 | v3: internal word-order inconsistency; not an external branch witness |
| West native quotient-field terms | W_cs_sk, W_pl | false | 0.333 | 0.333 | 0.240 | 0.364 | competitor-only in West; South no-hit in shelf |

## Packet recommendation

Use this file as an enclosure update to the ring/quotient-field packet. Do not replace the no-verdict framing: both hard rows are questions for Interslavic/community review. The main v3 correction is that quotient field must now be discussed as **kvocient-family internal variance plus West-native competitor evidence**, not as the erroneous `častnik` placeholder.
