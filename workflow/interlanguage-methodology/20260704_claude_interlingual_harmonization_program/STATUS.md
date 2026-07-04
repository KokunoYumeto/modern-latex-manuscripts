# Interlingual Program — STATUS
Cursor file. Update after each grind unit; resume from here in any session.

## Standing rules for this program
- Inline foreground work only. No agent fan-outs, no background jobs (Floris 2026-07-04: "don't spam agents"). Fable does the reading/synthesis itself.
- No GPU/model-load without explicit go (standing rule).
- No git push without telling Floris first.
- Never-certify: everything provisional + motivated.
- Deliverables get clickable links; final packages also land in `Documents\arxiv_latex\_zips\`.

## Done (2026-07-04)
- [x] Recon of all three strata; CORPUS_MAP.md written.
- [x] Read: ChatGPT rigor doc core (§1–4.6, §10 RQ/H1–H8, §13–15 blue/red-team/verdict); old Gemini proposal (1–140/314); new Gemini scenario (full); Obsidian seed transcript (full); Codex candidate matrix, publication draft, methodology note, bridge register (all full).
- [x] GitHub state verified: primary clone clean & in sync; interlanguage work pushed through package 160 on `origin/codex/noether-pc-20260629` (110 ahead of main); nothing local unpushed. Second clone (Papors\GitHub\...) is main, no upstream, 81 dirty files — parked.
- [x] PROGRAM.md (the proposal) written.

## Done (2026-07-04, second pass — the global synthesis)
- [x] Scope change per Floris: biology/physics analogy strands DROPPED from program (language/zonal work only). ChatGPT Pro handles its own consolidation; my job = the cross-island picture.
- [x] New extractions found in dump folder: `$germanOut` (heavy codex tree: translations/renders/sources/review_bundles), noether-pc branch checkout (through package 160), 20260609 extract. All local — no GitHub access needed.
- [x] Read: coordination index policy/status nodes (updated 20260630), ACCESS_GAIN_COHORT_METHOD (the practice-side objective function — formalized!), PAN_ROMANCE_OPTIMAL_ACCESS_HEURISTIC_INTEGRATION, 60-term source-hit table (T01–T60 structure), AI_INTERLANGUAGE_METHOD_REFERENCE_SHELF (20260703), SLAVIC_MAINTENANCE_PUBLICATION_HANDOFF (20260703), INTERSLAVIC_LOGBOOK standing principles + Paper01 term decisions.
- [x] **ISLAND_ATLAS.md written** — the deliverable: 10+ islands mapped to one ladder, 8 cross-island findings (F1 source-availability is THE gate; F2 standard+script unity decides build type; F3 one objective discovered mid-program, Slavic implements it implicitly; F4 union term spine = missing keystone; F5 zero external review returns anywhere; F6 dominance failure mode recurs on both substrates; F7 French interlock node; F8 Lean = proof-grammar endpoint), three-way correspondence table, ranked next-builds.

## Done (2026-07-04, third pass — Floris feedback + first build)
- [x] Floris feedback folded in: F10 East-Slavic seeding bias audit (NEW, pre-van-Steenbergen requirement), F11 Pan-Turkic format-artifact hypothesis, marginal-intelligibility→submodularity note (ChatGPT-sanity-check lane), review-interim = 3-AI triangulation + Floris; GitHub read OK / NO push.
- [x] **UNION_TERM_SPINE v1 built and run** ([md](UNION_TERM_SPINE_20260704.md), [json](UNION_TERM_SPINE_20260704.json), [script](scripts/build_union_spine.py)): 138 concepts, per-lane 60/60/62/60, overlap 4-lanes:17 / ≥3:32 / lane-unique:83 → **F9 spine drift is source-genre-driven** (atlas §6b).

## Next units (in order)
- [ ] Slavic ledger retrofit: mine INTERSLAVIC_LOGBOOK term decisions → access-gain fields + add Slavic column to union spine; simultaneously run the **F10 East-Slavic-skew audit** on witnesses per decision.
- [ ] Stratified core-spine proposal (proof-grammar / curriculum-algebra / Noether-corpus strata) — the fill-list per lane.
- [ ] FRAMEWORK paper draft (Zenodo-ready; no new experiments needed; now includes F9 as first measured result).
- [ ] Siting table v2 (lexicographic: source floor → build-type rule (F2) → access-gain) + F11 Pan-Turkic re-test spec.
- [ ] False-friend enumeration pilot on Romance spine rows (8 varieties of attested forms already in union json; CPU-only).
- [ ] Backup-vs-GitHub reconciliation list (which logs are backup-only).

## Open questions for Floris (non-blocking)
- Push consolidation outputs to GitHub when ready? (will prepare branch locally either way)
- API-worthiness verdict requested: see atlas §4–6 — my read is yes for the synthesis/harmonization layer, no need for grinding layers (codex handles those).
