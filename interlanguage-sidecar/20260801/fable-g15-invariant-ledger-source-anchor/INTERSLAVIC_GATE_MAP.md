# Interslavic Gate Map
2026-07-04. Third P0.2 deliverable per fable5_language_only_handoff.md. Sources: INTERSLAVIC_LOGBOOK.md (2884+ lines, 285 entries, read: policies + Papers 01–04 decisions + header map), glossary/*.json (95 files, 1310 records, fully machine-read), 20260703 maintenance handoff, extraction artifacts in this folder.

## A. The lane's existing gates (as actually operated)

| Gate | Rule | Evidence |
| --- | --- | --- |
| G1 Source witness | Translate from current source witness; no term without attestation or declared coinage | logbook standing principles; glossary `source_de`/`german` fields |
| G2 Term motivation | Every recurring technical term motivated: native/pan-Slavic vs international vs borrowed vs coined vs script-stability; uncertainty recorded, not normalized away | standing principles ("Do not silently normalize away uncertainty"); 222 logbook decisions with reason notes |
| G3 Term status | Statuses: solid-for-pilot / needs-reviewer-check / carried-forward(-review-needed) / stable(-provisional) / review_needed; promotion only under corpus pressure | logbook Papers 01–04; glossary status field |
| G4 Open revision | If later papers make an earlier term wrong, revise openly and rebuild cumulative outputs; revision trail is declared research value | standing principles |
| G5 Script sidecar | One language, two scripts: Latin = lexical source of truth; Cyrillic = deterministic transliteration via explicit table + validator (TeX/math/names excluded) + visual inspection; Cyrillic fixes back-propagated, never divergent | script policy section; `interslavic_cyrillic_generation` fields; Cyrillic hygiene batches |
| G6 Render gate | Cumulative renders must compile and pass visual inspection (Latin 579pp / Cyrillic 603pp current) | maintenance handoff render-integrity pass |
| G7 Canonical source-review batches | Post-hoc per-paper source-fidelity review sweeps (Papers 01–43 + endmatter, 2026-06-28 batch series) | logbook entries L3311–3508 |
| G8 Package validation | SHA-pinned zips + independent validation sidecars + file-freshness checks before publish; no rebuild without source change | 20260703 maintenance handoff (5382-entry package, validation True) |
| G9 External authority boundary | Local validation ≠ language authority; external review role packets prepared (authority packet 94KB + limited-support addendum); no canonical claim until returns accepted | external_review_role_packets_20260628; "review-ready not externally accepted" language throughout |
| G10 Non-erasure | Artifacts forkable, correctable, rejectable; Interslavic community (van Steenbergen et al.) is the authority, not the pipeline | methodology note; candidate matrix boundary sections |

## B. Audit results (2026-07-04, measured)

**B1. Witness monoculture in the term records — real, and already partially countered at shelf level (CLM-SLAV-001, refined after reading the triangulation log).**
All 1310 machine-readable term records derive via German→Ukrainian/Russian→Interslavic. Field presence: ukrainian/russian witnesses in ~1301 records; **West/South Slavic witness columns: 0**. Rationale text mentions: East-Slavic 182, West/South-Slavic 7, false friends 1.
Counterweight (2026-06-24, triggered by Floris's own flag, logged as "user brainwave"): a 20-source W/S triangulation corpus exists (cs 6, pl 6, sk 1, sl 2, sr 1, hr 2, bg 2 + archive.org supplement), a provenance-labeling rule was adopted ("state East-Slavic continuity vs W controls vs S controls vs deliberate constructed choice"), and ~5–8 flagship terms were spot-triangulated: `nekomutativno tělo` (cs/pl/bg/hr-backed), `polje` = commutative field, `jednostranno prosty ideal`, `primitivny idempotent` (cs/pl-backed), `razpadno polje` (flagged vs `rozkladno polje`).
**The confirmed dominance-drift instance is the ring term itself: lane keeps `kolco` (East-Slavic continuity) against cs/sk `okruh`, S-Slavic `prsten`, sl `kolobar` — logged as "not derivable mechanically from a majority vote", reviewer-sensitive.**
What remains undone: the per-term backfill — the 1310 records still carry no W/S witness fields and no provenance labels; the shelf and the policy exist, the data doesn't reflect them yet.

**B2. False-friend checking is effectively absent per-term** (1/1310 mentions), despite false-friend curation being a core Interslavic-project practice. The lane inherited the *language* but not the *hazard lists* as a per-term gate.

**B3. Status coverage is thin in the structured data**: 1236/1310 records carry no status value (status lives in prose or the newer files only). G3 is real but under-recorded — a promotion decision is often not machine-readable.

## C. Where model-side measurement could support or replace editorial judgment (handoff item 7)

| Editorial judgment today | Measurable support |
| --- | --- |
| "transparent to all Slavic readers" (asserted) | cross-Slavic recognizability score: attestation + form-distance across uk/ru/pl/cs/sk/hr/sr/bg/sl/mk witness forms |
| internationalism-vs-native tie-breaks (G2) | ambiguity/false-friend score per candidate vs each member language (FormSim×SemDist) |
| "avoid rough Russian" (asserted) | dominance-distance: chosen form's distance to ru vs to family barycenter (CLM-DOM-001 shift measurement after retrofit) |
| carried-forward consistency (G3) | term-usage consistency scan across cumulative corpus (mechanical) |
| Cyrillic sidecar correctness (G5) | round-trip transliteration invariant tests, INV-SCRIPT-001 style — partially exists (validator), formalize as invariant ledger rows |

## D. Recommended new gates (pre-review-packet requirements)

1. **G11 Witness breadth (fixes B1):** every promoted term row gains pl, cs, hr/sr, bg witness columns (minimum one West + one South), filled from dictionary/triangulation sources or marked explicit gap. Schema change + backfill; the triangulation logs already contain much of the material.
2. **G12 Per-term false-friend check (fixes B2):** each promoted term checked against W/S Slavic near-forms with divergent meaning; result recorded per row (clear / warned / renamed).
3. **G13 Machine-readable status (fixes B3):** every record carries an explicit status; prose-only statuses backfilled.
4. **G14 Access-gain fields:** contested rows carry the ledger fields (main_register_retention, marginal gain, dominance_penalty, …) as the world-family lanes now do — the proven lane should meet the standard its successors inherited from it.
5. **G15 Invariant ledger:** adopt the INV-* table (handoff schema) for script conversion and register operations; the existing validator becomes INV-SCRIPT-001's test.

Order of operations: G11–G13 backfill → CLM-DOM-001 shift measurement → refreshed review packet → van Steenbergen contact. The shift measurement is the scientifically interesting step: if adding W/S witnesses moves few terms, the East-Slavic-seeded choices were already family-central (the tradition worked); if it moves many, the retrofit was necessary and the magnitude is the headline number. Either way it belongs in the paper.

## E. Read-state honesty
- Fully machine-read: all 95 usable glossary files; term-decision extraction of logbook bullet-format entries (222, Papers 01–04 era).
- Read directly: standing principles, script policy, Paper 01–02 decision sections, header map of all 285 entries.
- Not yet read line-by-line: the 2026-06-24→28 triangulation/review-batch entries (L3311+) and SLAVIC_TRIANGULATION_REFERENCE_LOG.md — queued; B1's "triangulation is separate, not per-term" is from structure + field data, and the check in CLM-SLAV-001 risk_if_wrong applies.
