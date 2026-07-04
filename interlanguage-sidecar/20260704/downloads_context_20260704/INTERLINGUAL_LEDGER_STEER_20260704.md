# Interlingual Ledger Steer — negative evidence, concept maps, and F1–F8 implications

Date: 2026-07-04

## 1. Core correction: adverse evidence is not zero evidence

A term row must distinguish four states:

1. `support`: the source branch attests or strongly supports the candidate for the intended concept.
2. `absence`: no usable source witness has yet been recorded.
3. `competitor`: the source branch uses a different form for the same concept, which weakens the candidate for family-central use.
4. `collision`: the candidate resembles a form in a source branch that means something else, creating false-friend or concept-link risk.

This is the operational version of “some words have positive weights and some have negative weights.” Do not encode all non-support as zero.

Preferred implementation: two-channel ledger.

```text
positive_support_mass(candidate, concept, branch)
adverse_mass(candidate, concept, branch)
```

`adverse_mass` includes same-concept competitors, false-friend collisions, wrong-register evidence, and script-confusion evidence. It should not be silently folded into the positive witness count, because absence, competition, and harm have different review consequences.

## 2. Concept-ledger row schema

```text
concept_id:
concept_label_en:
concept_label_de:
concept_gloss:
stratum: proof_grammar | curriculum_algebra | noether_corpus | outer_union
status: active | gap | not_applicable | linked_unreviewed

labels:
  de:
  en:
  uk:
  ru:
  isv_latin:
  isv_cyrillic:
  fr:
  es:
  pt:
  it:
  ca:
  gl:
  ro:
  ar:
  fa:
  my_id:

candidate_evidence:
  support:
    east_slavic: []
    west_slavic: []
    south_slavic: []
    interslavic_authority: []
    international_math: []
  adverse:
    competitors: []
    false_friends: []
    concept_collisions: []
    wrong_register: []
    script_confusions: []

scores_or_diagnostics:
  raw_branch_distribution:
  effective_branches_D1:
  KL_to_target:
  dominance_flag:
  reviewer_need:

review_question:
external_packet_status: show | show_with_definition | review | no_fix_first
```

## 3. German-to-English normalization gates

The German-to-English table should not be a flat glossary. Each German key must be classified:

```text
exact_concept_match
near_concept_match
historical_Noether_specific
compound_or_phrase
not_in_current_spine
ambiguous_requires_context
false_friend_or_collision_risk
```

Critical distinction:

```text
linked_to_concept        = the German row can be associated with a concept row.
witnessed_for_branch     = a source branch actually supports a candidate for that concept.
reviewed_for_bridge_use  = the row is safe to use as bridge-language evidence.
```

Do not let concept linking silently inflate Slavic witness coverage.

## 4. F1–F8 implications for the next build units

F1. Source availability is the first gate.
Action: build a source-floor table before scoring any new lane. Machine-readable source is preferred, not required.

F2. Standard-and-script structure decides build type.
Action: every family gets one of four outputs: zonal bridge, controlled technical register, script bridge, or local-standard crosswalk. “Do not construct” is a valid result.

F3. The access-gain ledger is the unifying objective.
Action: migrate lane rationales into typed fields, but keep it as a decision ledger, not a calibrated scalar model.

F4. The union term spine is the keystone.
Action: keep C0/C1/C2/C3 separated. The real core is C2, the stratified core spine with fill-list semantics.

F5. External review is still zero.
Action: say “internal triangulation before external review”; do not call anything validated until a human/community return is accepted.

F6. Dominance collapse is a repeated failure mode.
Action: preserve pre-backfill archaeology, run post-backfill diffs, and report the shift. Do not silently repair.

F7. French is an interlock node.
Action: use French as a control/pivot for Romance and Noether alignment, not as authority. It helps detect when the concept ledger is drifting by corpus genre.

F8. Lean/proof grammar is an endpoint, not the current lane.
Action: proof-grammar rows should be shaped so later formalization is possible, but current priority is source witnessing and concept alignment.

## 5. Immediate Fable prompt

```text
Next unit: build the interlingual concept ledger, not merely a German-English list.

Tasks:
1. Harvest all German-key field variants across old/new glossary schemas.
2. Create concept rows with German, English, Ukrainian, Russian, Interslavic Latin, Interslavic Cyrillic labels.
3. For each German key, classify match_type as exact / near / Noether-specific / compound / not-in-spine / ambiguous / collision-risk.
4. Add support and adverse evidence fields. Competitor evidence and false-friend/collision evidence are active negative evidence, not zeros.
5. Rebuild Slavic links into the union spine only as linked_to_concept. Do not mark witnessed_for_branch unless branch witness exists.
6. Keep all term promotion frozen. This is a concept-normalization and audit layer only.
```
