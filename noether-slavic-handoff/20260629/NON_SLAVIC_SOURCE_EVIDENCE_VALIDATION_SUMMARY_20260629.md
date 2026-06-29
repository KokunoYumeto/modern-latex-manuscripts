# Non-Slavic source evidence URL validation summary - 2026-06-29

Companion machine-readable ledger: `NON_SLAVIC_SOURCE_EVIDENCE_URL_VALIDATION_20260629.json`

This validation pass checked the 24 entries in `NON_SLAVIC_SOURCE_EVIDENCE_SEED_20260629.json` using HTTP HEAD first, then a response-header-only GET fallback. It does not download or redistribute source PDFs, and it does not validate license, mathematical adequacy, or native authority.

Follow-up: the weak Simplified Chinese shelf identified here is reinforced in `CHINESE_SOURCE_EVIDENCE_REINFORCEMENT_20260629.md` and `CHINESE_SOURCE_EVIDENCE_REINFORCEMENT_20260629.json`.

## Result

| Language | Entries | Accessible | Inaccessible |
| --- | ---: | ---: | ---: |
| French | 4 | 4 | 0 |
| Spanish | 4 | 4 | 0 |
| Simplified Chinese | 5 | 1 | 4 |
| Japanese | 4 | 4 | 0 |
| Persian/Farsi | 4 | 4 | 0 |
| Arabic | 3 | 3 | 0 |
| Total | 24 | 20 | 4 |

## Inaccessible from this PC during validation

All four inaccessible entries were Simplified Chinese university-hosted sources:

- `zh_pku_bicmr_algebra_2023`
- `zh_pku_bicmr_algebra_syllabus_2023`
- `zh_ustc_algebra_intro`
- `zh_ustc_comm_alg_notes`

These should remain in the seed shelf as search-visible/potential witnesses, but they need alternate mirrors, manual browser checks, or replacement witnesses before they can support a translation/revision decision.

## Interpretation

- French, Spanish, Japanese, Persian/Farsi, and Arabic now have at least several URL-verified seed witnesses.
- Simplified Chinese has the ongoing local Paper 34 work and at least one verified physics-adjacent witness, but the algebra/commutative-algebra source shelf needs immediate reinforcement with sources that are reachable from this PC.
- Persian/Farsi URL verification does not cover Dari or Tajik. Those must be tracked separately.

## Next gate

Before advancing any non-Slavic lane beyond evidence gathering:

- verify license/reuse status for each source,
- extract only short term/context anchors with page references,
- create a per-language terminology/rationale log,
- require native/external review status fields in the lane manifest.
