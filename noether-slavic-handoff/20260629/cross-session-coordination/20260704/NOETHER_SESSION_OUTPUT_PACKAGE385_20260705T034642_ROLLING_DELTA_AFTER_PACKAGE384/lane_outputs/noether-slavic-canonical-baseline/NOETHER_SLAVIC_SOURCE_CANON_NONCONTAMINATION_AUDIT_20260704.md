# Noether Slavic Source-Canon Non-Contamination Audit - 2026-07-04

Scope: guardrail audit for canonical Slavic source-canon artifacts. It checks that the main witness table, URL snapshot, cache inventory, and cache filenames remain scoped to Slavic target-language evidence and that broad noncanonical/non-Slavic probe noise is explicitly quarantined.

Boundary: this audit does not claim native review, canonical approval, license clearance, accepted correction, or translation completion.

Checks total: 6. Non-pass checks: 0.

| check_id | status | observed_count | offending_values | action |
|---|---|---:|---|---|
| main_witness_language_scope | pass | 14 |  | none |
| source_cache_prefix_scope | pass | 41 |  | none |
| main_witness_non_slavic_keyword_scan | pass | 0 |  | none |
| broad_probe_quarantine_documented | pass | 2 |  | none |
| url_reachability_language_scope | pass | 49 |  | none |
| cache_inventory_language_scope | pass | 41 |  | none |

## Decision

Canonical Slavic source-canon outputs pass this non-contamination audit. Non-Slavic/German/English broad-probe noise remains quarantined in the TeX/source-package probe addendum and is not promoted into canonical Slavic witness rows.

## Allowed Languages

- Belarusian
- Bosnian
- Bulgarian
- Croatian
- Czech
- Interslavic/Panslavic
- Macedonian
- Montenegrin
- Polish
- Serbian
- Slovak
- Slovenian
- Sorbian Lower
- Sorbian Upper
