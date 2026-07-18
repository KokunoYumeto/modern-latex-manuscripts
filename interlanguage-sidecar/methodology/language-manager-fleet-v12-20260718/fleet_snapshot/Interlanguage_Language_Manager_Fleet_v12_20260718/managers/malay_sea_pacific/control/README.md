# Malay / Southeast Asia / Pacific lane control

This directory is the durable control surface for the Malay, Southeast Asia, and Pacific language manager. It is one manager lane across all works, not a separate manager per work or language.

## Current state

- Reconstruction date: 2026-07-17.
- Historical R7 result: substantial source/reference collection and routing scaffolding; no completed target-language translation was found.
- Current production authority: translate every work into the lane's target languages, while keeping each language, standard, script, and register distinct.
- First defensible production target: a complete Indonesian working translation of the one-page Noether Paper 36, directly from the current R823 German authority, followed by a separately evidenced Malaysian Malay version.

## Controlling files

- `RECONSTRUCTION_20260717.md` — evidence-backed account of what earlier Codex work actually produced.
- `RECONSTRUCTION_ARTIFACT_LEDGER_20260717.csv` — machine-readable artifact classification.
- `CURRENT_CURSOR.md` — next production cursor and its evidence constraints.
- `EVIDENCE_GRAPH.json` — typed, channel-separated provenance and decision-routing graph.
- `COHORT_TREE.json` — declared administrative/family/cohort dependence tree.
- `../../../../00_governance/USER_VERBATIM_THREAD_BRIEF_20260717.md` — user-verbatim authority.
- `../../../../01_methodology/research_department/README.md` — shared research reconciliation.
- `../../../../01_methodology/research_department/LANE_HANDOFFS/MALAY_SEA_PACIFIC.md` — lane-specific research handoff.

## Non-negotiable method boundaries

1. Use `EVIDENCE_GRAPH.json` for typed provenance and routing; never collapse support, candidate, competitor, adverse, absence, and veto evidence.
2. Use a declared family/cohort tree for dependence and breadth. The manager grouping is administrative, not a claim that Malay, Southeast Asian, and Pacific languages form one linguistic unit.
3. Keep Indonesian and Malaysian Malay as separate target standards with an explicit crosswalk. Do not inherit either one's evidence into Brunei, Singapore, or unrelated SEA/Pacific languages without target-specific evidence.
4. Treat old `source_gated_draft_support_body` labels as archaeological. They are candidates until an exact-sense source passage is checked for the actual translation decision.
5. Reject scalar readiness claims from unified v6.2. Its 96.1 Malay/Indonesian value was computed with zero support rows and sixty candidate rows.
6. Working translations may proceed under the user's current authority, but uncertain terminology must remain flagged and no native review, community certification, or finality may be claimed without evidence.
7. A production tranche is not complete without translated TeX, a compiled PDF, a build record, and rendered-page visual QA.

## Production completed in this reconstruction pass

- Complete Noether Paper 36 Indonesian working translation: `../03_working_translations/noether/paper36/tranche_001_id_20260717/`.
- Build: two XeLaTeX passes, one A4 page, no warnings/errors/box problems/missing glyphs.
- Visual QA: one of one pages rendered and inspected; pass.
- Next cursor: the same complete work in Malaysian Malay as a separate target, with its own evidence decisions.
