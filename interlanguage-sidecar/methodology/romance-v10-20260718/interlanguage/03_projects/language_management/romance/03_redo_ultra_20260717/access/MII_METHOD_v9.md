# Marginal-access implementation v9

The v9 implementation now exists. `PAN_ROMANCE_WORDWEB_v9` retains 60 core concepts, 106 explicit senses, and 39 C2 nodes. `PAN_ROMANCE_ACCESS_LEDGER_v9` contains exactly 106 × 9 = 954 unique sense/cohort rows. The canonical topology remains `00_lane_control/ROMANCE_FAMILY_COHORT_TREE_v2.json`, and its cohort IDs equal the access-ledger cohort IDs in order and without duplication.

The nine cohorts are standard Spanish, standard French, standard Portuguese, standard Galician, standard Catalan, standard Italian, standard Romanian, Rumantsch Grischun, and readers primarily literate in a regional Romansh idiom. The last cohort must later be stratified as Sursilvan, Sutsilvan, Surmiran, Putèr, or Vallader; the five source-provenance routes remain distinct.

## Evidence linkage

The 120 inherited ES/FR core records remain unresolved and have zero source quotations. The reviewed semantic layer contains all 679 unique IDs from the frozen occurrence-v1 table plus the three reviewed RM-2024 delta IDs, for 682 distinct occurrences. T01–T60 review is contiguous and each occurrence ID is integrated exactly once. Together the inherited and reviewed layers contain exactly 802 evidence records.

Primary review dispositions are 510 accepted, 127 rejected, and 45 held. Multi-sense and adverse-event links remain nonexclusive: the review layer has 515 support-sense links, 129 adverse-sense links, 50 held-sense links, and 20 form-admission adverse events. Accepted support reaches 73/106 senses; 33 senses remain explicit gaps. Accepted support, rejection, held state, lexical-only context, running-body context, form-admission adverse evidence, cross-sense adverse evidence, and correlated evidence-family status remain separate fields. Multi-sense support does not multiply an occurrence.

## Empirical claim boundary

Empirical MII remains at **zero human observations**. All seven human-result fields are null in JSON and empty in CSV on all 954 rows; every row has `pilot_eligible=false`; no form is promoted. No MII result feeds a vocabulary or grammar decision.

The populated numeric values are pre-human orthographic design diagnostics. They use deterministic normalization and normalized Levenshtein similarity against inherited cohort forms plus Spanish and French dominance carriers. These diagnostics do not measure intelligibility, comprehension, acceptability, pronunciation, semantic transparency, processing time, or marginal gain. Ninety-six rows may satisfy the stored orthographic comparison predicate, but that predicate is not a human result.

A future human protocol must record cohort and, where applicable, regional Romansh idiom; mathematical-literacy band; cross-Romance exposure; randomized/blinded item order; responses, errors, and abstentions; latency; confidence; uncertainty; consent; and review state. Until those observations exist, no scalar readiness, pilot, empirical MII, or form-promotion claim is authorized.

## Structural integrity

Core forms, definitions, derivations, relations, C2 extension nodes, sense semantics, and candidate decision surfaces are inherited from v8 without promotion. The relation inventory remains 402 descriptive records: 27 valid target-ID edges, 375 records without target IDs, and zero invalid nonempty targets. Together with 106 concept-to-sense memberships this yields 133 ID-resolved references.

The exact sense-label contract remains:

- T51: `function_domain`, `integral_domain`, `generic_domain_or_region`, `coefficient_domain_linkage`.
- T60: `neutral_or_identity_element`, `identity_map`, `algebraic_identity`, `unit_or_invertible_element`.

The reproducible builder is `scripts/build_wordweb_and_access_v9.py`. The independent validator is `scripts/validate_romance_tranche_v9.py`. Validation rejects structural drift, a missing or duplicate occurrence ID, evidence counts other than 120 + 682 = 802, JSON/CSV access mismatch, any nonnull human-result field, any pilot flag, or any form-promotion flag.
