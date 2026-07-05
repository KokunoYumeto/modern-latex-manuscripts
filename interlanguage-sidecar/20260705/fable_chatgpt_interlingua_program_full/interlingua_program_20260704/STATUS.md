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

## Done (2026-07-04, fourth pass — ChatGPT handoff executed: P0.2 complete)
- [x] ChatGPT handoff received (`Downloads\codex backup dump 7-4\fable5_language_only_handoff.md`) — converges with atlas (triangulation!); schemas adopted.
- [x] Interslavic logbook mined: 222 term decisions extracted ([interslavic_term_decisions_20260704.json](interslavic_term_decisions_20260704.json)); term creation was early-phase (Papers 01–04), later phases = review batches; per-paper terms live in glossary/.
- [x] Slavic dataset built: 1310 records / 95 glossary files ([slavic_term_dataset_20260704.json](slavic_term_dataset_20260704.json)).
- [x] **F10 audit RESULT: witness monoculture confirmed & quantified** (0 W/S witness columns in 1310 records; 7/1310 rationale mentions; 1/1310 false-friend mentions) — but triangulation log verified: 20-source W/S shelf + provenance rule + flagship spot-triangulations exist since 2026-06-24 (Floris's flag); per-term backfill never done. Confirmed drift case: ring `kolco` vs `okruh/prsten/kolobar`.
- [x] **Three P0.2 deliverables written**: [CLAIM_LEDGER.md](CLAIM_LEDGER.md) (11 claims, CLM-*), [HEURISTIC_REGISTER.md](HEURISTIC_REGISTER.md) (14 heuristics, HEU-*), [INTERSLAVIC_GATE_MAP.md](INTERSLAVIC_GATE_MAP.md) (G1–G10 existing + B1–B3 audit + G11–G15 recommended).

## Done (2026-07-04, fifth pass — ChatGPT build order executed steps 1–3)
- [x] **Frozen baseline** ([frozen/](frozen/)): FABLE_BLIND_ATLAS_v0, UNION_TERM_SPINE_v1_preSlavic (json+md), CHATGPT_LANGUAGE_ONLY_HANDOFF_v0 — the "AI with East-Slavic sources only" stratum locked as archaeology per Floris.
- [x] [CONCORDANCE.md](CONCORDANCE.md): blind-atlas × sidecar delta (confirmed/sharper/rejected/tensions) + CLM-001..005 entries. Adopted: C0/C1/C2/C3 spine architecture, restricted submodularity, MAG-with-variance selection rule, F10 flag schema, "internal triangulation before external review" wording.
- [x] **INTERSLAVIC_LEDGER_RETROFIT_20260704** ([json](INTERSLAVIC_LEDGER_RETROFIT_20260704.json) / [csv](INTERSLAVIC_LEDGER_RETROFIT_20260704.csv)): 1254 term-level rows from 1310 glossary records + 222 logbook decisions, hash-pinned run manifest, honest-null access-gain fields.
- [x] **F10_EAST_SLAVIC_SKEW_AUDIT_20260704** ([md](F10_EAST_SLAVIC_SKEW_AUDIT_20260704.md) / [json](F10_EAST_SLAVIC_SKEW_AUDIT_20260704.json)): F10-0 210 / F10-1 963 (76.8%, under-witnessed not wrong) / F10-2 20 / F10-3 42 (ALL = `kolco` compound family — one decision resolves 42 rows) / F10-4 19. safe-external: 210 yes / 966 review / 62 fix-first.
- [x] CLM-MARG-001 restricted to the defensible submodular-benefit + risk-constraint split.

## Done (2026-07-04, sixth pass — branch weighting + spine v2 + core spine)
- [x] Branch-weighting v0 run ([json](branch_weighting_v0_20260704.json)): witness mass East 2395 / West 64 / South 59 = 95.1/2.5/2.3%; **effective branches 1.26 of 3**; holds per rationale class (even "pan-slavic" terms ≈1.28). Third measured result. [BRANCH_WEIGHTING_SPEC.md](BRANCH_WEIGHTING_SPEC.md) written as ChatGPT math-lane handoff (weighted rooted-tree witness measure + phylogenetic down-weighting questions). NOTE: math stays in files; chat output stays linguistic (client safeguard kept switching models on math-heavy replies).
- [x] **UNION_TERM_SPINE_v2_WITH_SLAVIC** ([json](UNION_TERM_SPINE_v2_WITH_SLAVIC.json) / [csv](UNION_TERM_SPINE_v2_WITH_SLAVIC.csv)): Slavic column added — but only 40/1310 records matched (21 concepts) because the Slavic glossary is German-keyed. 1270-record remainder preserved in retrofit ledger; boundary recorded in artifact.
- [x] **STRATIFIED_CORE_SPINE_PROPOSAL_20260704** ([md](STRATIFIED_CORE_SPINE_PROPOSAL_20260704.md) / [json](STRATIFIED_CORE_SPINE_PROPOSAL_20260704.json)): C2 v1 = 67 rows (proof-grammar 22, curriculum-algebra 28, Noether-corpus 17) with witnessed|gap|not-applicable fill semantics; C0/C1/C3 architecture documented.

## Done (2026-07-04, seventh pass — interlingual concept ledger v1)
- [x] **Interlingual concept ledger v1** ([md](INTERLINGUAL_CONCEPT_LEDGER_20260704.md) / [csv](INTERLINGUAL_CONCEPT_LEDGER_20260704.csv) / [json](INTERLINGUAL_CONCEPT_LEDGER_20260704.json)) — Floris's "concept map" request realized: language-neutral concepts × (de | en | uk | ru | isv | isv_cyr), strata assigned, F10 flags carried. Curated seed: [data/concept_ledger_seed.json](data/concept_ledger_seed.json), 86 concepts incl. full classical invariant-theory vocabulary (Überschiebung→transvection, Formenreihe→form sequence, Reduzent→reducent, verschränktes Produkt→crossed product…). 56 concepts populated with data; 156 retrofit rows mapped.
- [x] Diagnosis of the mapping ceiling: **953 retrofit rows have no German key** (older glossary schemas stash it under other field names) — fix is retrofit v2 key-harvesting, not more curation; plus ~40 easy seed extensions (direkte Summe, Einheitsmatrix, Divisionsalgebra, Burnside/Dedekind-Mertens theorems…), plus workflow-note noise class.

## Done (2026-07-04, eighth pass — retrofit v2, siting table, F-map)
- [x] Retrofit v2: `source` field identified as the German key for 439 older-schema records; v1 artifacts frozen ([frozen/](frozen/)); pipeline rerun (retrofit 1229 rows; audit F10-1 947 / F10-0 203 / F10-3 41 / F10-2 19 / F10-4 19; effective branches 1.255 — stable under re-keying, good robustness sign).
- [x] Concept ledger v1.1 with phrase-containment matching: 63 concepts / 237 rows mapped; remaining tail = phrase-level translation decisions (retrofit-ledger scope, not concept scope — boundary noted).
- [x] **[SITING_TABLE_v1.md](SITING_TABLE_v1.md)**: F1–F11 findings→actions map; build-type decision rule stated (standard+script structure decides; split/combine decisions confirmed); 18-lane siting table with lexicographic source floor; **negative-weight `do_not_use` design** (Floris's point) with four reason classes, feeding on false-friend lists + warning comparators + F10-3 + rejection matrices.

## Done (2026-07-04, ninth pass — linker fix, triangulation hit, seed extension)
- [x] **Ränderung false-link CONFIRMED & FIXED** (ChatGPT predicted it sight-unseen; verified: ring←"bordering operation…"; unpredicted sibling: reducible←irreducible). Word-boundary+plural matching in both linkers; coverage honestly deflated (gloss links 28→25; spine Slavic 40→34). Logged in CONCORDANCE triangulation hit log.
- [x] Seed extended to 111 concepts (direct sum, division algebra, hypercomplex system, Burnside/Dedekind-Mertens, extension-of-first-kind…, + **Ränderung as first `do_not_use`-class row**). Ledger: 85 concepts / 267 rows via German key — the reliable route.
- [x] Three-status discipline encoded in spine v2 Slavic entries (linked_to_concept / witnessed_for_branch{east,west,south} / reviewed_for_bridge_use) — alignment can no longer inflate coverage.
- [x] Layer renamed per sidecar: dependence-corrected witness weighting (ensemble-dependence framing); 3-state measurement plan (baseline=frozen run1 / post-alignment / post-backfill).

## Done (2026-07-04, tenth pass — adverse-evidence channel + ledger routing)
- [x] **DO_NOT_USE_LEDGER_20260704** ([md](DO_NOT_USE_LEDGER_20260704.md) / [json](DO_NOT_USE_LEDGER_20260704.json)): 123 typed adverse entries — do_not_inherit_into_lane 62 (Persianate rejection lanes: the non-erasure discipline was already generating adverse evidence), dominance_risk 41 (kolco family), authority_needed 16 (Romance warning-comparator rows), + templates: Ränderung collision, irreducible polarity reversal, razpadno/rozkladno competitor, svijanje register caution. Classification-only; vetoes are relations, not scores; three-state discipline (support / absence / adverse) throughout.
- [x] **Spine v2 Slavic column now ledger-routed** (de→concept_id→en; gloss matching retired): 88 term rows on 26 spine concepts — more than double the honest coverage of gloss matching (34/19) — plus 59 ledger concepts held ledger-side (no spine row yet; future C2 growth). All entries linked_to_concept only; witness/review statuses explicit.

## Done (2026-07-04, eleventh pass — Chatnotes corpus node located)
- [x] Stratum D registered in CORPUS_MAP: `Papors\Chatnotes\CHat translates and clean\` — per-author bilingual drafts (Cayley…Weber, SGA, Noether), **ES+JA Noether papers 36–39 zip** (two new spine languages), Interlanguage-methodology bundle 20260702 (= lineage source of today's theory docs), translations/non-eu/ukrainian nodes. Compaction caveat: draft-linked material only, never witnesses without verification. Full per-author inventory queued.

## Done (2026-07-04, twelfth pass — W/S backfill v0 from LOCAL shelf)
- [x] Triangulation shelf located IN THE DUMP (`$germanOut\sources\interslavic_triangulation\...\text\`, 20 extracted texts) — Floris was right: no new collection needed. **WS_WITNESS_BACKFILL_v0** ([md](WS_WITNESS_BACKFILL_v0_20260704.md)/[json](WS_WITNESS_BACKFILL_v0_20260704.json)): 15 core concepts branch-typed. Results: **ring (kolco) = COMPETITOR-ONLY in both branches** (okruh/pierścień/prsten/kolobar attested, kolco zero) — ring memo evidence base done; **NEW review item: quotient field = COMPETITOR-ONLY West** (podílové/ułamków families), no South hits; splitting field West-competitor (rozklad-) as log predicted; internationalism policy VINDICATED for ideal/module/group/homomorphism/idempotent/basis/invariant (support both branches); doublet-policy candidates: determinant (pl wyznacznik), polynomial (pl wielomian, cs mnohočlen).
- [x] Translations tree confirmed in dump (`$germanOut\translations\paper01–…​ + non_slavic`) — ES/JA & other-language material to inventory from there (newer than Chatnotes versions).

## Done (2026-07-04, thirteenth pass — six units, no checkpointing)
- [x] **[RING_TERM_DECISION_MEMO](RING_TERM_DECISION_MEMO_20260704.md)**: options A–E with access-ledger fields; recommendation E (prsten surface + kolco doublet) with D as interim; okruh rejected on typed adverse evidence (okrug collision); community-dictionary check + 2 verifications required before packet ships. Resolves 41 F10-3 rows on acceptance.
- [x] Dump translations inventory: per-paper tree = Slavic lane; non_slavic = AR/FA expansions + Hefferon microdrafts + small japanese folder; ES lives in noether-pc branch (r1_spanish); Chatnotes ES+JA zip remains primary bilingual package. CORPUS_MAP note pending minor edit.
- [x] **[F7_FRENCH_INTERLOCK_NOTE](F7_FRENCH_INTERLOCK_NOTE_20260704.md)**: 3 lanes, cross-citation actions, sga_certified_usage field proposed, register tags, dominance boundary.
- [x] **[PAN_ROMANCE_ACCESS_LEDGER_HANDOFF](PAN_ROMANCE_ACCESS_LEDGER_HANDOFF_20260704.md)**: full row schema + priority rows + gate transition for the codex lane (its own pilot blocker).
- [x] **[FRAMEWORK_PAPER_SKELETON](FRAMEWORK_PAPER_SKELETON_20260704.md)**: 11 sections; five measured results slotted; fill-list for the draft.
- [x] **Backfill v1 run** ([md](WS_WITNESS_BACKFILL_v1_20260704.md)/[json](WS_WITNESS_BACKFILL_v1_20260704.json)): 37 concepts branch-typed. **NEW STRUCTURAL FINDING (F12): West Slavic is the calque-preferring branch** — theorem (věta/twierdzenie), corollary, trace, extension, quotient-field, splitting-field, ring all West-competitor-only, while South accepts internationalisms; ~15 concepts support-both. Consequence: doublet policy should target West cohorts specifically; "teorema" fails in cs/pl sources even for the most basic proof word.

## Done (2026-07-04, fourteenth pass — F12 landed + the before/after number exists)
- [x] F12 written into atlas §6b (West Slavic = calque-preferring branch; doublet policy targets West cohorts; Romance analog check queued for the access ledger).
- [x] **Witness write-back v0** ([json](WITNESS_WRITEBACK_v0_20260704.json); annotated audit saved as NEW file [F10_AUDIT_postwriteback](F10_AUDIT_postwriteback_20260704.json), baseline untouched): 33 rows upgraded across 12 concepts (concept_shelf level, support hits only). **Effective branches 1.255 → 1.362; KL 0.871 → 0.789.** Honest reading: even maximal shelf-level write-back leaves 1.36/3 — the monoculture is structural; the long tail needs corpus-scale witnessing, and the concept ledger's row coverage is the multiplier (seed pass 3 raises it).
- [x] Mild self-paced loop authorized by Floris; wakeups armed at 60s while units remain obvious.

## Done (2026-07-04, loop pass 15 — retrofit row-chain bugfix, big numbers move)
- [x] Diagnosed the 956-empty-source_term rows: retrofit had TWO de-key chains; row-output chain still short. Fixed; full rerun.
- [x] Coverage after fix: **ledger 654/1304 rows mapped, 104/111 concepts populated** (was 267/63); spine v2 Slavic: 371 records on 36 concepts (was 88/26); write-back: **182 rows upgraded, 20 concepts**.
- [x] **State-c number: effective branches 1.255 → 1.754 of 3 (KL 0.871 → 0.537)** via shelf-level W/S witnesses routed through the concept ledger. Reading: the core vocabulary can be family-witnessed from existing local material; residual gap = long-tail phrases + per-row verification.

## Done (2026-07-04, loop pass 16)
- [x] Skeleton §6 updated (Results 3a=F12, 3b=1.255→1.754 before/after; fill-slots pruned — only dictionary check remains for §6).
- [x] **[C2_FILL_DISPATCH](C2_FILL_DISPATCH_20260704.md)** ([json](C2_FILL_DISPATCH_20260704.json)): per-lane work orders — interslavic 40, pan_romance 39, controlled_arabic 30, malay_indonesian 25, arabic_farsi_persianate 18 missing C2 rows, grouped by stratum, witnessed|gap|NA semantics, codex-consumable.

## Done (2026-07-04, loop pass 17)
- [x] **[CHATNOTES_STRATUM_D_INVENTORY](CHATNOTES_STRATUM_D_INVENTORY_20260704.md)** ([scan json](chatnotes_stratum_d_scan_20260704.json)): 827K files / ~914GB / 37 folders scanned. Witness-language pool much wider than 4 lanes: it (Bianchi 1.8K pair), ja (Mikami/Seki/cleanup 2.6K+), zh+sa (cleanup multilingual), ar (Weber 912, Gauss 257), la (Gauss), es (multiple). Anchor-author-per-language pattern identified (F7 generalizes). ES/JA extraction plan written (term-level, via concept ledger, linked/draft only — AI translations are candidate-form donors, never native witnesses). Caveat: counts are upper bounds (renders/build trees); Noether-Multilingual 376GB needs dedup before per-file planning.

## Done (2026-07-04, loop pass 18)
- [x] **[FRAMEWORK_DRAFT](FRAMEWORK_DRAFT_20260704.md) §2–3 written** (publication prose): §2 two-vocabularies-one-objective incl. the two practice→theory contributions and the shared dominance failure mode; §3 the four intervention types + two ordering rules, three-state evidence discipline, three-status linkage discipline, the three carrying artifacts (concept ledger / stratified core spine / invariance ledger), thresholds + standing phrase.

## Done (2026-07-04, loop pass 19)
- [x] **FRAMEWORK_DRAFT §4–8 written** — all five results in publication prose with final numbers (F9 138/17/32/83 + strata; F10 monoculture 1.255 + human-catch qualification + archaeology framing; backfill/F12/before-after 1.754; Ränderung triangulation + division-of-labor point; adverse channel 123 with design principle). Draft now has §2–8 complete.

## Done (2026-07-04, loop pass 20 — DRAFT COMPLETE)
- [x] **FRAMEWORK_DRAFT §1–11 + abstract all written.** The paper is a complete v0.1: correspondence, discipline, five measured results, siting model, honest limits, availability, intro, abstract. ~4,500 words of publication prose, every claim file-pinned.

## Done (2026-07-04, pass 21 — Floris steer executed)
- [x] Zip MOVED out of `_zips` → [_claude_aid\interlingua_program_20260704_v1.zip](../interlingua_program_20260704_v1.zip) (_zips = LaTeX sources for ChatGPT only; memory updated). NOTE: zip predates passes 20–21; regenerate before any external use.
- [x] **[AUTHORSHIP.md](AUTHORSHIP.md)**: full model/human provenance (Fable 5 = synthesis+paper prose; ChatGPT Pro 5.5 = rigor sidecar+steers+Ränderung prediction; Gemini DR = seed docs; Codex = practice stack; Kimi = Stratum-D drops; Floris = direction+founding heuristics+systemic catch) + idea-provenance table + publication note. Draft §11 now carries the AI-contributions block + Zenodo pointer.
- [x] **[COMPARATIVE_TERM_ANALYSIS_v1](COMPARATIVE_TERM_ANALYSIS_v1_20260704.md)** ([json](COMPARATIVE_TERM_ANALYSIS_v1_20260704.json)): 37 concepts, current-vs-alternatives with branch coverage + evidence; coverage heuristic isolates exactly 2 review-priority rows (ring, quotient field), rest = confirm/variant questions. The "which is better and why" packet backbone.
- [x] **[CHATGPT_PRO_TASK_SPEC](CHATGPT_PRO_TASK_SPEC_20260704.md)**: bounded outsourcing spec for weighted marginal-intelligibility scoring (3 weightings incl. dependence-corrected; attestation-proxy I_g with documented partial-credit; vetoes before scores; sensitivity reporting; output schema). Ready to paste to ChatGPT Pro with the v1 zip.

## Done (2026-07-04, pass 22 — post-Fable steer Tasks A/B/C executed)
- [x] **[FRAMEWORK_DRAFT_ORDERED_20260704.md](FRAMEWORK_DRAFT_ORDERED_20260704.md)** — paper order (title/abstract/1–11) + Appendices A–D (artifact inventory / flag schemas / C2 dispatch / weighting definitions). Content = v0.1 sections, mechanical reorder. This is now the citable draft; v0.1 marked superseded in index.
- [x] **[ARTIFACT_INDEX.md](ARTIFACT_INDEX.md)** ([json](artifact_index_20260704.json)) — all 73 files: role, kind, sha256:12, cite/external flags (steer schema; superseded artifacts marked; frozen/ = archaeology).
- [x] **[SOURCE_USE_POLICY.md](SOURCE_USE_POLICY.md)** — six evidence categories with may/may-not-feed rules; provenance levels inside witness category (concept_shelf < row_verified < reviewed); stop-and-ask list bound in.
- [x] Steer's corrections adopted: ring memo = review proposal, never "solved" (already labeled; packet v0 will be no-verdict); post-writeback distribution confirmed (83.5/8.0/8.5); draft-as-witness prohibition formalized in policy.

## Done (pass 22 cont.)
- [x] **Task D: [RING_REVIEW_PACKET_v0](RING_REVIEW_PACKET_v0_20260704.md)** — memo, 5-candidate attested table, corpus-pressure facts, file-pinned W/S evidence, typed adverse relations (okruh/округ; prsten register-shift; kolco W/S opacity flag), 6 reviewer questions, enclosures list. NO verdict; the earlier decision memo is marked superseded-in-tone.

## Done (pass 23 — ChatGPT web returns merged; internal-consistency audits run)
- [x] Returns received in `user made flr with chat web stuff\`: ring occurrence audit + packet patch + **WEIGHTED_INTELLIGIBILITY_SCORES_v2** (4 weightings, MAG per candidate, vetoes as constraints; ring & quotient-field = weight-sensitive review rows; 28 concepts confirmed as-is; population weights flagged as placeholders pending source-pinned speaker table).
- [x] **Paper-25 prsten finding VERIFIED locally** (translations\paper25\interslavic\v001 L68, residue-class ring context) → ring packet updated to **v0.1**: §3a internal non-uniformity, reviewer question 7, scores + audit added to enclosures, changelog.
- [x] **[KOLCO_FAMILY_INTERNAL_CONSISTENCY_LEDGER](KOLCO_FAMILY_INTERNAL_CONSISTENCY_LEDGER_20260704.md)** ([json](KOLCO_FAMILY_INTERNAL_CONSISTENCY_LEDGER_20260704.json)): 1059 kolc* occ (= ChatGPT's count, cross-validated) / 43 forms / 19 papers; compound inventory (podkolco 39×, …).
- [x] **NEW FINDING — quotient-field internal inconsistency #2:** glossaries render Quotientenkörper as `polje kvocientov` (p06/24/30) vs `kvocientno polje` (p09). Corrects the "polje častnikov?" placeholder in comparative/scores artifacts.
- [x] ~~glossary↔text drift p24/p30~~ **RETRACTED same pass** — was my scan-path error (those papers use `working\sectionNN\` layout); full-tree grep: kvocient p24 44×, p30 30×, `polje kvocientov` in rendered text. Drift-audit CLASS retained (no confirmed instance); scan scripts to glob full per-paper trees. Honest-correction logged in ledger.

## Done (pass 23 cont.)
- [x] p09 s10 tex check: **`kvocientno polje` confirmed in rendered text (2×, with definitional footnote)** vs `polje kvocientov` (p06 tex + p24/p30 tex/glossary). Inconsistency #2 text-verified both sides → belongs in the quotient-field review row alongside the W-competitor evidence.

## Done (pass 24 — feed registered + Task E complete)
- [x] ProMode feed zip registered in CORPUS_MAP (1,912 TeX; internal-consistency shelf; README's own no-W/S + don't-let-Russian-dominate notes; 1059 cross-count = same corpus, two toolchains — validates scanners, not data).
- [x] **Task E: [dispatch/](dispatch/) per-lane C2 fill ledgers** — PAN_ROMANCE 39, CONTROLLED_ARABIC 30, ARABIC_FARSI_PERSIANATE 18, MALAY_INDONESIAN 25, INTERSLAVIC 40 rows; fillable (witnessed|gap|not_applicable), lane-specific witness rules, SOURCE_USE_POLICY bound in. Returns feed UNION_TERM_SPINE_v3.
- [x] Stale queue items cleared (F7 note, PR handoff, skeleton — done in earlier passes).

## Done (pass 25 — witness shelf packaged + paper review implemented → v0.3)
- [x] `Noether_Non_RU_UK_Slavic_Baseline_Sources_20260704.zip` verified = the local 20-source triangulation shelf, packaged (identical filenames; 24 entries). ChatGPT's independent audit (hashes check; 1,147pp; 2.69M chars) + its context-window/term-probe artifacts landed in the drop folder. Source-use category: language_family_witness after row-context review. Registered.
- [x] ChatGPT returns in drop folder: NON_RU_UK audit set, CONTEXT_WINDOWS, TERM_PROBE_COUNTS, **scores v3** (source-pinned speaker proxy), **CHATGPT_FRAMEWORK_PAPER_REVIEW** (verdict: viable as case-study methods paper).
- [x] **Paper review implemented in full → [FRAMEWORK_DRAFT_ORDERED_v0.3.md](FRAMEWORK_DRAFT_ORDERED_v0.3.md)** (v0.2 preserved): measured/interpreted/not-claimed headers on §4–8; §6+§8 internal-variance addenda (prsten, QF word-order, častnikov withdrawal); §7 failure-modes paragraph incl. the retraction as discipline evidence; §9 population-weighting = sensitivity-only statement; write-back boundary conditions spelled out; revised title + compressed abstract adopted; Appendices B–D now self-contained.

## Done (pass 26 — context merge + C2 extraction)
- [x] **Ring packet §4 upgraded to definitional-context evidence** (two independent probes; per-branch definitional passages: cs "Definice. Okruhem R rozumíme pětici…", pl "Definicja pierścienia…", sr "Definicija 1: Komutativan prsten…", sl kolobar 939 occ; kolco 0 in both probes). CONTEXT_WINDOWS added to enclosures.
- [x] **[C2_CONTEXT_WINDOWS_v1](C2_CONTEXT_WINDOWS_v1_20260704.md)** ([json](C2_CONTEXT_WINDOWS_v1_20260704.json)): **46/67 C2 rows** with native W/S context windows (curated stems, incl. proof-grammar connectives — the F12-sensitive stratum). **21 pending = almost entirely the Noether-corpus stratum** (binary/ternary/biquadratic form, complete-system family, covariant/contravariant, transvection, resultant, ground form…) — a curriculum shelf cannot witness specialist historical vocabulary; those rows need specialist sources (historical algebra texts per branch) or stay honest gaps. That asymmetry is itself a siting datum: proof-grammar + curriculum strata are witnessable from general shelves; the Noether stratum needs its own source intake.

## Done (pass 27 — THE MARKER TABLE, per Floris's original point)
- [x] **[INTERLINGUAL_MARKER_TABLE_v1](INTERLINGUAL_MARKER_TABLE_v1.md)** ([csv](INTERLINGUAL_MARKER_TABLE_v1.csv) / [json](INTERLINGUAL_MARKER_TABLE_v1.json)) — the central artifact Floris originally asked for: **138 concepts × 20 language-marker columns** (de en uk ru isv isv-cyr | cs sk pl sl hr/sr bg | es fr pt gl ca it ro rm | ar fa my/id), evidence-tagged ([S] cognate-support / [C] competitor / empty=honest gap), C2-stratum flagged, weighted where scores exist (31 rows with v3 action/sensitivity/MAG). Fill profile: Romance 30–60, ar/fa/my 60–64, Slavic W/S 21–31, East+ISV 34–36 of 138 — the sparsity map IS the fill-work list.
- [x] Ring packet + C2 context work of pass 26 feeds this table's Slavic W/S cells.

## Done (pass 28 — session open-items sweep, per Floris)
- [x] **Ring packet pre-ship reqs 1+2 CLOSED (§2a)**: community word list obtained (app+steen unreachable → medzuslovjansky/database Google-Sheet export, 8MB csv in data/): **`koljce`=ring with W/S row = prsten-family in every W/S language** + **`pŕstėnj`=ring also community-sanctioned**; no math sense marked; corpus `kolco` ≠ community citation form `koljce` (new reviewer sub-question). перстень register verified: 0 occurrences in corpus uk/ru math text (vs кільце/кольцо ≈1025/1029) — jewellery-only in East.
- [x] **[NOETHER_STRATUM_SOURCE_INTAKE_PLAN](NOETHER_STRATUM_SOURCE_INTAKE_PLAN_20260704.md)**: per-branch historical sources (Kurepa, Mostowski-Stark, Bydžovský, Obreškov…) + national digital libraries (Kramerius/Polona/dLib/NSK) for the 21 specialist rows; fetch gated on explicit go.
- [x] **Memory written**: project_interlingua_program.md + MEMORY.md line — program now survives session loss (resume: workspace STATUS.md).
- [x] ARTIFACT_INDEX regenerated (116 files); **v2 zip built** ([interlingua_program_20260704_v2.zip](../interlingua_program_20260704_v2.zip), 4.2MB, supersedes v1).
- [x] F7 SGA line-pinning: **BLOCKED-ON-PATH** — sga6_fr_workpass.tex not reachable from this machine's search paths (memory pointer belongs to the SGA session's own working dir); needs that session's cursor or Floris pointing at the file.

## Done (pass 29 — v3 adoption + repair; packet assembled; authority posture corrected)
- [x] **AUTHORITY POSTURE (Floris)**: on Slavic linguistic substance, Fable+ChatGPT+community are the authority — Floris does NOT gate linguistic decisions (he gates: spend, scope, external SENDING, pushes). Linguistic work no longer queues on his read. Standing rules updated in spirit throughout.
- [x] **ChatGPT v3 master + whole-interlanguage map received & verified**: 212 concepts, priority bands (A: ring+QF — its missing-QF catch CONFIRMED, my v1 lacked the row), source-weight ladder, lane map (12 lanes incl. french_interlock). 
- [x] **v3 label contamination caught & repaired → [v3.1 REPAIRED](INTERLINGUAL_MARKER_TABLE_v3_1_REPAIRED_20260704.csv) = MASTER TABLE** (54/45/41/42 sentence-cells moved to *_source_cue; 10–16/column lemmas restored from ledger; rest honest-blank). [Defect report for ChatGPT](V3_DEFECT_REPORT_FOR_CHATGPT_20260704.md) filed (root cause + v4 fix). CONCORDANCE hit log: mutual-catch now three-for-three (C→F Ränderung, C→F missing-QF, F→C label leak). My v1 table = superseded.
- [x] **[VAN_STEENBERGEN_PACKET_v1_INDEX](VAN_STEENBERGEN_PACKET_v1_INDEX.md) assembled** — reading order, questions summary, boundary. Sending gate = Floris + the 1–2-complete-authors sequencing.

## THE COMPLETENESS BAR (Floris, pass 30 — supersedes all packet-framing)
**"Is the word complete? Did you do the full canonical-corpus insertion of ALL the words, correctly weighted?"** Nothing is shown externally before the answer is yes. The van-Steenbergen index is an internal artifact only; STOP mentioning sending. The program goal = full-corpus insertion + weighting.

## Done (pass 30 — completeness metric defined & measured)
- [x] **[CORPUS_INSERTION_COVERAGE_v0](CORPUS_INSERTION_COVERAGE_v0_20260704.md)** ([json](CORPUS_INSERTION_COVERAGE_v0_20260704.json)): full ISV Latin corpus lexicon = **11,075 content types / 142,466 tokens** (265 dedup files; TeX+preamble stripped, stoplist-filtered). Current system covers **39.6% of types / 70.6% of tokens** (stem-matched v0; overcounts via stem collisions, undercounts via inflections — stated). Gap queue: ~6,700 types, frequency-ordered, top-500 in json.
- [x] Front-of-queue triage classes identified: (a) further stoplist (pokazuje, mora, teper), (b) **genuine proof-grammar insertions hiding in "discourse" words** (ravny=equal, nazyva=is-called, vsebuje=contains — these ARE register vocabulary), (c) inflections-of-known (formu→forma), (d) new math concepts. The insertion grind = deciding each front word into a class and inserting classes b+d into the ledger.

## Done (pass 30 cont. — insertion passes 1–2 + tooling fixes)
- [x] **Pass 1**: top-120 triage → 90+ stoplist adds; **[proof_prose_lexicon_v1](data/proof_prose_lexicon_v1.json)**: 25 register concepts inserted (ravny/equal, nazyvaje-se/is-called, vsebuje/contains, naleži/belongs, ręd/series, potęga/power, važi/holds, proběgaje/ranges-over… — corpus-attested lemmas + stems, proof-grammar stratum); eponym class (covered-by-definition: steinitz, noether…).
- [x] **Tooling fixes found by the grind itself**: (i) č/ď/ľ/ŕ missing from word-class regex — čislu was shredding to 'islu' (~900 types recovered); (ii) NFC before tokenize; (iii) vowel-stripped stem matching (formu→form-, grupu→grup-) replacing naive 6-char prefixes.
- [x] **Trajectory: tokens 70.6% → 77.6% → 82.2%; types 39.6% → 52.0%** (type base honestly GREW to 11,984 with the tokenizer fix). Distance-to-complete = the real number now: ~5,750 uncovered types, front already triaged for pass 3 (insert: tvrdženje, soglasovati, dopuščati, točno, velja, lema; stop: ješče, tada, zbog, sebe…).

## Done (pass 31 — ChatGPT's parallel insertion pass merged; over-stoplisting corrected)
- [x] ChatGPT ran the same completeness metric independently (222 strict v001 files): **78.92% tokens / 51.1% types** — within ~3 points of mine (different file selection); the metric is implementation-robust. Its artifacts: full token table, top-1000 backlog, weighted backlog (0.35 permitted-use weight, correctly NOT a truth weight), 92-row/70-lemma proof-register addendum.
- [x] **Methodological correction accepted (C→F #3): I over-stoplisted** — togda/teper/teda/imenno/mora/kromě/znovu/ješče/osoblivo etc. are proof-connective REGISTER vocabulary (the thing a controlled register standardizes), not noise. 186 variants un-stoplisted.
- [x] **[proof_prose_lexicon_v2](data/proof_prose_lexicon_v2.json)**: 93 lemma groups (68 ChatGPT + 24 Fable + merged), provenance-tagged, all `needs linguistic review`, permitted-use 0.35. Near-duplicate lemma-key dedup (naleži/naležati class) queued for v2.1.
- [x] **Coverage after merge: 85.2% tokens / 54.8% types** (denominator honestly grew with un-stoplisting). Trajectory: 70.6 → 77.6 → 82.2 → **85.2** tokens.
- [x] Next front already visible: lema, tvrdženje, soglasovati, velja, pomoću, prědpoloženje (assumption!), stati, tipa — mix of insert + inflection classes.

## Done (passes 32–33 — fronts 4+5, soft loop resumed)
- [x] Pass 4: +22 lemma groups (lema, tvrdženje, prědpoloženje/assumption, pomoću, aksiom, podtělo/subfield, eksistovati-doublet, izvodny, srav./cf., protivno…) +13 variants (tada→togda group: hr 'then' is register). **86.9%/57.1%**.
- [x] Pass 5: +3 groups (očividno, smatrjati, konec/na-koncu) +3 variant sets (suščestvuje→eksist group, inako→inače, pokazyva→pokazati); pronouns/demonstratives → stop. **87.5% tokens / 57.5% types.** Trajectory: 70.6→77.6→82.2→85.2→86.9→87.5.
- [x] Lexicon now 118 lemma groups, all provenance-tagged, needs-review status.

## Done (loop passes 34–37 — insertion fronts 6–9)
- [x] Passes 6–9 applied: +19 lemma groups (vyvesti, ostati, sohranjati, odmah, paralelno, tělo-inflections, čisto, rečeno, stojati, naravno, však/however, nahoditi-se, obhvaćati, zaměna/substitution, dodanje, ukazati, dlugost, vystupati, citovati…), variant attachments (tada→togda, musi→morati, suščestvuje→eksist, imeno→imenno, vprašanje→pytanje…), roman-numeral strip class, bibliography-token strip class, +eponyms (macaulay, lasker…). Lexicon = **140 lemma groups**.
- [x] **Trajectory: 87.5 → 88.1 → 88.4 → 89.0 → 89.4 tokens; types 57.5 → 59.7.** Deltas ≈0.3–0.6/pass — the long tail has begun.
- [x] **F13 (new finding, from the residue's shape): the corpus's proof-register carries pervasive VARIANT SCATTER** — orthographic/lexical doublets at function-word level (obće/obču/vobče/voobče; imenno/imeno; mora/musi; pytanje/vprašanje; gde/gdje; togda/tada; ješče/jošče; odnovrěmenno/odnovočasno) — the kolco/prsten inconsistency class, but pervasive in the register layer. The insertion grind IS producing the standardization worklist (each lexicon group's variants = a normalization decision for review).
- [x] Umlaut leak spotted (könig, körper, gött in gaps) = German bibliography residue passing the word-class — add to biblio strip next pass.

## Done (loop pass 38 — source-anchors zip: family tree extends)
- [x] `Interlanguage_All_Downloaded_Source_Anchors_20260704.zip` received: folder 01 = the 20-source shelf (manifest-pinned, matches local); **folder 02 = NEW underrepresented-branch shelf: Belarusian (BNT 1922 + Minsk 1993 math dictionary), Macedonian (UKIM math lexicon PDF 11.5MB), Upper Sorbian (Domowina math terminology 2008 + 1996 term corpus)** — extracted to [shelves/underrepresented_slavic/](shelves/underrepresented_slavic/), category-2 witness material (dictionary-grade!) with per-source lane_decision fields in its manifest.
- [x] **Ring row: be = кольца confirmed** (51 ring-compound entries in the 1993 dictionary; OCR б/о quirk handled) → packet §4 updated: East-branch kolco-family coherence now 3/3 standards (uk кільце, ru кольцо, be кольца); W/S remains competitor-only. Family tree gains a leaf-level witness column.
- [x] Sorbian HTMLs are tool/description pages; the terminology content is in the PDFs — **PDF text extraction queued** (mk lexicon + hsb Domowina; check pypdf availability, else defer to codex lane).

## Done (loop pass 39 — pass 10 + mk/hsb probe)
- [x] Insertion pass 10 applied (lexicon 145 groups; German biblio-strip extended): **89.7% tokens / 60.1% types.**
- [x] **mk = прстен CONFIRMED, definitional grade** (UKIM trilingual lexicon, 172 occ, legacy-font transliteration handled; extracted txt cached on shelf). **prsten coalition = 5 standards (pl+hr+sr+bg+mk).** Ring packet §4 updated.
- [x] **hsb SOURCE DEFECT**: "Domowina math terminology 2008" is a publisher's catalog, not terminology (1996 corpus PDF likewise bibliography) — mislabel flagged; hsb mathematical witnesses = open gap (soblex/Serbski institut = live leads). Honest gap, logged.
- [x] mk lexicon = major witness asset beyond ring: поле 48, теорема 57, матрица 91, идеал, полином entries — feeds C2/marker-table mk column wholesale (extraction cached, 1.48M chars).

## Done (loop pass 40 — mk column built + 90% crossed)
- [x] **[MK_COLUMN_PROBE_v1](MK_COLUMN_PROBE_v1_20260704.json): 39/43 core concepts witnessed in the UKIM lexicon, dictionary-grade** (funkcija 911, mno`estvo/множество 775, element 610, vektor 535, ravenka 547, matrica 408, grupa 393… **pole na koli~nici = quotient field, 3 entries — direct evidence for review-priority row #2**). 4 misses need manual lookup (noetherian, prime ideal, invariant, tensor product — probe-guess issue, not absence). Legacy-font decode pass (~=č {=š `=ž w=њ?) queued before clean Cyrillic lemmas enter the marker table.
- [x] Insertion pass 11 (+7 groups incl. imamo/'we have' — proof idiom, was wrongly headed to stoplist; lexicon 152): **90.1% tokens / 60.6% types.** Trajectory: …89.0 → 89.4 → 89.7 → **90.1**.
- [x] mk/be/hsb summary for ChatGPT v4 round now has all its facts (5-standard prsten coalition; 3/3 East kolco-family; hsb defect).

## Done (loop pass 41 — pass 12 + mk decode + v4 handoff)
- [x] Insertion pass 12 (+8 groups incl. korak/step, prěnesti, izvorno; +6 variant sets; lexicon **160**): **90.5% tokens / 61.5% types.**
- [x] **[MK_MARKER_COLUMN_v1](MK_MARKER_COLUMN_v1_20260704.json)**: 39 concepts decoded to clean Cyrillic (прстен, множество, количник, поле на количници…) — marker-table-ready, spot-check flagged.
- [x] **[CHATGPT_V4_HANDOFF](CHATGPT_V4_HANDOFF_20260704.md)**: one bundle — v3 label-channel fix, QF forms, over-stoplisting merge, be/mk columns + hsb defect, scores-v4 consequences (5-standard prsten coalition; be→E cohort), insertion-grind state + F13 variant-normalization proposal ask.

## Done (loop pass 42 — pass 13 + REGISTER-ROW BRANCH MATRIX)
- [x] Insertion pass 13 (+7 groups; lexicon 167): **90.9% tokens / 62.1% types.**
- [x] **[REGISTER_ROW_WS_PROBE_v1](REGISTER_ROW_WS_PROBE_v1_20260704.json) — F12 measured at the connective level (F12b):**
  - West = COMPETITOR-ONLY for 5/6 register rows: nehaj←nechť/niech; poněže←protože/ponieważ; važi←platí/zachodzi; mora←musí/trzeba; imenno←totiž/mianowicie. Only togda/teda has West support (cs tedy = cognate).
  - **poněže and imenno are competitor-only in BOTH branches** on this shelf — register-layer kolco-class rows (East-shaped connectives with zero W/S support).
  - South supports nehaj (neka), mora (мора), važi, togda — the South-tolerant/West-calque asymmetry replicates exactly in the connective layer.
  - Consequence: the controlled register's connective spine needs West-facing doublet policy MORE than its noun spine does; nehaj is community-standard ISV (so it stays), but its W-reader gloss (nechť/niech) belongs in the register documentation. Paper §6/F12 gains the register matrix.

## Done (loop pass 43 — pass 14 + F12b landed in atlas & paper)
- [x] Insertion pass 14 (+5 groups; lexicon 172): **91.2% tokens / 62.6% types.** (korolar group didn't exist → new entry queued pass 15.)
- [x] mk lookups: **invarijant ×10 + tenzor ×24 FOUND** (earlier probe boundary issue) — mk column now 41/43; noetherian + prime-ideal patterns still open.
- [x] **F12b written into atlas §6b and draft v0.3 §6** — the connective-layer branch matrix is now in the paper ("nouns lean international; connectives are pure inheritance, and inheritance is exactly where the branches split").

## Done (loop pass 44 — pass 15 + Cyrillic sync check CLEAN)
- [x] Insertion pass 15 (+8 groups incl. korolar as its own borrowed-form group; lexicon 180): **91.4% tokens / 62.8% types.**
- [x] **[CYRILLIC_SYNC_CHECK_v1](CYRILLIC_SYNC_CHECK_v1_20260704.json): the deterministic-sidecar discipline HOLDS at deliverable level** — 244/265 Latin files have Cyrillic siblings; all 21 unpaired are working fragments/_working_chunks (expected workflow state); **zero finalized v001 files lack a Cyrillic sibling**. The kolc 1059 vs колц 983 gap traces exactly to those unpaired working files — no divergence defect. G5 (script policy) validated empirically; a positive result for the paper's invariance-ledger section.

## Done (loop passes 45–46 — passes 16–17, eponym rule, 92% crossed)
- [x] Pass 16 (+8: vključenje, obraz/image, argument, vyražati, nemožno…; eponym STEM rule — steinitza/gordana inflections covered by prefix) → 91.8%/63.9%.
- [x] Pass 17 (+5: mimo, prehoditi, iskany, izhodišče, izslědovanje — the logbook's own word; variant attaches: istočasno→odnovrěmenno, **namreč→imenno [F13: sl-flavored doublet found INSIDE the corpus]**, suščstvuje, najobčejše) → **92.1% tokens / 64.5% types, lexicon 193.**
- [x] F13 tally keeps growing through the grind itself: imenno/namreč joins mora/musi, togda/tada, ješče/jošče, odnovrěmenno/istočasno/odnovočasno — the internal-doublet ledger is accumulating as a side product of coverage work, exactly as intended.

## Done (loop pass 47 — pass 18 + v2.2 dedup)
- [x] Pass 18 (+8 groups: bilinearny, bukva, prějdti, pripisovati, povezany…; slijedi→slěduje F13 attach) + **v2.2 dedup: 8 near-duplicate groups merged** (variant-overlap/5-char-head rule; provenance unioned). Lexicon = 193 clean groups. **92.3% tokens / 64.9% types.**
- [x] Clebsch → eponym list next micro-pass; dělo held un-triaged (divide-vs-work ambiguity — needs context look, not a guess).

## Done (loop pass 48 — ChatGPT v3 grind merged; holds resolved; 93% crossed)
- [x] ChatGPT v3 pass received & reconciled: unified 31-source anchor index (be/mk/hsb correctly anchor_control until context-review; consistent with my findings), TeX-artifact exclusion ledger (ADOPTED: pt/em/ann etc.), 320-type v2-delta (MERGED into coverage known-set as needs-review internal inserts), top-1500 backlog, 5.19M chars source text under one index.
- [x] **Context-check holds RESOLVED**: dělo = "Work" (paper-header term, Dělo 44) → proof_reference; **vaga = weight-of-a-form — classical invariant-theory term hiding in the noise queue** → noether_corpus stratum. Both inserted.
- [x] Pass 19 (+10 groups; lexicon 203) + delta merge: **93.1% tokens / 67.0% types.** Trajectory since bar set: 70.6 → … → 92.3 → **93.1** (types 39.6 → **67.0**).

## Done (loop pass 49 — pass 20 + mk gaps resolved as genuine)
- [x] Pass 20 (+6 groups; lexicon 209; waerden/fischer eponyms): **93.3% tokens / 67.6% types.**
- [x] mk noetherian + prime-ideal: **genuine dictionary-scope gaps** (2021 general-math lexicon; no pattern hits) — mk cells stay honest-empty on those rows; specialist-source material, same class as the Noether-stratum intake plan.

## Done (loop pass 50 — pass 21)
- [x] Pass 21 (+6 groups; teraz→teper F13 attach; lexicon 215): **93.5% tokens / 68.0% types.**

## Done (loop pass 51 — pass 22)
- [x] oběh context-check: **genitive dual "of both"** (function word → stop), not 'circulation' — third hold resolved by looking, not guessing.
- [x] Pass 22 (+8 groups incl. znamenatelj/denominator, obščnost [obći-scatter F13]; lexicon 223; schmeidler eponym): **93.7% tokens / 68.4% types.**

## Done (loop pass 52 — pass 23)
- [x] nosep = LaTeX [nosep] option leak → stripper regex fixed (optional-arg after \begin).
- [x] Pass 23 (+7 groups incl. psevdomatričny [Noether-stratum], početek, dějati-se; slućaj ć/č-scatter attach; lexicon 230): **93.8% tokens / 68.6% types.** (zovut attach missed — dedup renamed target group; re-aim by variant-membership next.)

## Done (loop pass 53 — CONSOLIDATION; loop STOPPED for strategy call)
- [x] zovut attached (variant-membership targeting); lexicon stats: 230 groups / ~950 surfaces / 67 scatter-rich groups (≥4 variants = F13 normalization queue).
- [x] **[COMPLETENESS_STATE_20260704.md](COMPLETENESS_STATE_20260704.md)** — the sprint summary: 93.8% tokens / 68.6% types; ~3,700 long-tail types remain; findings recap; the four-option strategy fork with my recommendation (d).
- [x] Program zip **v3** built ([interlingua_program_20260704_v3.zip](../interlingua_program_20260704_v3.zip), 23MB — includes shelves + all grind artifacts).
- **LOOP STOPPED** — strategy call is Floris's: (a) token-grind to 95%+ / (b) type-ranked fronts / (c) weighting+normalization layer on the 230 groups / (d) split: ChatGPT takes the tail, I take weighting. Recommendation: (d).
- [ ] **F13 write-up into atlas §6b + skeleton** (variant-scatter = register-standardization worklist; feeds the paper's internal-variance section).
- [ ] Lexicon v2.2 dedup (citation form = infinitive; naleži/naležati class).
- [ ] Cyrillic-side metric (validator cross-check).
- [ ] Register-row W/S shelf probe (weighting couples to insertions).
- [ ] ChatGPT round: v2.1 lexicon + unstoplist note + QF corrections.
- [ ] Cyrillic corpus same metric (run after Latin insertion stabilizes; transliteration validator should make it near-identical — divergence = defect signal).
- [ ] Weighting stays coupled: every inserted concept-row inherits the witness/weight machinery (branch evidence, adverse channel) — insertion without weighting doesn't count toward the bar.
- [ ] C2 fill-ledgers, specialist-source intake, ChatGPT v4 — all continue as sub-feeds of insertion coverage.
- [ ] Gated: embedding measurements (explicit go).

## Standing operating rules (Floris + sidecar convergence, 2026-07-04)
Bounded tasks proceed without asking when: (i) read-only or classification-only; (ii) no new target-language wording; (iii) CPU/local only; (iv) emits counts + source pointers; (v) preserves old artifacts (freeze, don't overwrite). Chat output stays language-side; math stays in files.

## Open questions for Floris (non-blocking)
- Push consolidation outputs to GitHub when ready? (will prepare branch locally either way)
- API-worthiness verdict requested: see atlas §4–6 — my read is yes for the synthesis/harmonization layer, no need for grinding layers (codex handles those).

## Done (2026-07-04, pass 25 — SPLIT EXECUTED: v4 intake audit + lexicon v2.4 + branch-evidence weighting layer)
- [x] ChatGPT v4 drop intake (top-1500 triage, v2.3 lexicon proposal, 67-row normalization proposals, package 344/345 source-canon intake). Package 344/345: hash-verified coordination metadata, routed to source index NOT marker table (correct); pan_romance 95 hooks = C2 fill queue for that lane (parked; Slavic lane first).
- [x] **V4 INTAKE AUDIT** ([raw](V4_AUDIT_RAW_20260704.txt), [merge log](V4_REVIEW_MERGE_LOG_20260704.json)): 4 defect classes caught (mutual-catch F->C #2..#5): D1 en-gloss channel contamination ~40+ rows (dictionary prefix-match pulled wrong headword glosses: podmodul="submarine", kongruencija="congress", posrědovati="silver-plate"...); D2 false root-prefix attaches (proizhod*->arbitrary, reducir*->ręd, suščstveno->exists, nastal/nastalo double-attached); D3 per-token entries not lemma-grouped (237 entries -> 132 groups); D4 silent attach failures (592 proposed vs 493 applied, zovut-shape). Full report: [V4_DEFECT_REPORT_AND_HANDOFF_FOR_CHATGPT_20260704.md](V4_DEFECT_REPORT_AND_HANDOFF_FOR_CHATGPT_20260704.md).
- [x] **Lexicon v2.4 merged** (data/proof_prose_lexicon_v2.json, 362 groups; v2-230 frozen at frozen/proof_prose_lexicon_v2_230_preV4.json): strips+re-homes applied, 29 attach-instead-of-new, 132 consolidated groups with corrected EN glosses, months/hamel excluded (hamel+riemann added to coverage EPONYMS), 0 cross-group duplicates verified. **COVERAGE: 95.0% tokens / 72.9% types** (was 93.8/68.6).
- [x] **WEIGHTING LAYER BUILT (lane c)**: [REGISTER_DOUBLET_BRANCH_EVIDENCE_v1](REGISTER_DOUBLET_BRANCH_EVIDENCE_v1_20260704.md) — 34 doublet groups x 9 native langs (W=cs/pl/sk shelf prose, S=sl/hr/sr/bg + mk UKIM, E=be dict pages; mechanical_probe 0.5). [NORMALIZATION_DECISION_TABLE_v1](NORMALIZATION_DECISION_TABLE_v1_20260704.md): 67 rows, 31 with branch profiles -> **14 confirmed W/S register doublets (F12b now quantified: musi W145/S0 vs mora W0/S177; totiž W9/S0 vs namreč/naime W0/S189; otázka/pytanie W vs pitanje/vprašanje S...)**, ~17 pan-root anchors. 2 mechanical pan-verdicts killed by cross-branch homographs (hr jednak=equal vs pl jednak=however; hr pripada=belongs vs cs případ=case) -> homograph check added to probe-v2 checklist. NEW METHOD LESSON: pan verdicts REQUIRE homograph audit.
- Cursor: next = (i) hand defect report + v2.4 to ChatGPT (Floris ferries), (ii) its context_review 455-row KWIC re-emit -> my bulk adjudication, (iii) probe-v2 for the un-probed doublet groups + remaining F13 rows, (iv) marker-table weight columns from decision table, (v) pan_romance C2 fill when Slavic weighting lands.

## Done (2026-07-05, pass 26 — probe-v2 + decision table v1.1 + marker v3.2 + atlas F12c)
- [x] **Probe-v2 run** (16 previously unprobed doublet groups, homograph guards at pattern level): [REGISTER_DOUBLET_BRANCH_EVIDENCE_v2_20260704.json](REGISTER_DOUBLET_BRANCH_EVIDENCE_v2_20260704.json). Headlines: ręd = NO pan root (řada cs / szereg pl / niz hr-sr / zaporedje sl four-way; ISV ręd leans E — review-critical); suma = four-way field (součet W216 / zbir S153 / vsota S119 / suma W55+S55 weakly pan); tělo W-confirmed massively (těleso 667 + ciało 360 vs S 121); obći fully split (obecn W86 / splošn sl82 / opći-obšt S33); vaga = be-attested (13) + S uses teža/težina (genre caveat: algebra prose rarely carries 'weight'); dopuščati near-absent (absence, not adverse); cel-/nul-/lež-/dava- pan.
- [x] **NORMALIZATION_DECISION_TABLE v1.1** ([md](NORMALIZATION_DECISION_TABLE_v1_20260704.md) regenerated): 47/67 rows now carry branch profiles; verdicts patched; homograph corrections integrated.
- [x] **Marker table v3.2** ([json](INTERLINGUAL_MARKER_TABLE_v3_2_20260704.json) / [csv](INTERLINGUAL_MARKER_TABLE_v3_2_20260704.csv)): register-layer weight columns (register_doublet_group / register_branch_profile / register_doublet_policy / register_evidence) on 7 concept rows (lemma, basis, power, zero, corollary, assumption, division ring/body). v3.1 remains frozen base.
- [x] **ISLAND_ATLAS updated: F12c** — the quantified W/S doublet structure (16+ zero-crossover doublets, ~17 pan anchors, ręd/suma no-pan cases, homograph-audit method lesson).
- Cursor: ferry V4_DEFECT_REPORT_AND_HANDOFF + v2.4 lexicon + decision table v1.1 to ChatGPT (Floris); await its context_review KWIC re-emit for bulk adjudication; then remaining F13 rows without profiles (20 inflectional clusters need no decision), marker weight columns for W/S language columns proper, pan_romance C2 fill queue (95 hooks) when Slavic weighting settles.

## Done (2026-07-05, pass 27 — context-review adjudication from ChatGPT's own KWIC windows)
- [x] Discovery: ChatGPT's v4 drop already contains KWIC windows for 594 tokens (ISV_LONGTAIL_CONTEXT_WINDOWS_PASS_v4) — the 455-row context_review adjudication did NOT need to wait for its next round.
- [x] **Pass A**: 62 stop_or_register_review tokens lexicalized as function_word stratum (44 fw-* groups; unstoplist policy, togda/teper precedent, dict-confirmed POS carried).
- [x] **Pass B1**: strict auto-attach vs v2.4 deliberately conservative after D2 lesson: only 3 attaches (rędam, potęga, potęgah), all verified.
- [x] **Pass B2 batch 1** (hand adjudication of n>=6 band from windows; [log](CONTEXT_REVIEW_BATCH1_LOG_20260705.json)): 21 attaches + 42 new groups + 6 exclusions. Real math register recovered: lěvy (LEFT IDEAL), adičny (p-adic), kogredientny, permutacija, točka, kvaternion, fiksovany, nerazložimy (irreducible — own group per polarity rule), varijabla (doublet of prěmenna), zadača, silny; register verbs vleče (entails), vznikaje, inducirajut, spomenuti; phrases v silě / v vidě / v dějstvitelnosti. przez = Polish residue excluded. EPONYMS extended: zermelo klajn klein roch herglotz lipschitz fokker sylow brauer.
- [x] **Lexicon now v2.5, 448 groups. COVERAGE: 95.7% tokens / 75.4% types** (from 93.8/68.6 at sprint end — +1.9/+6.8 today). Queue remaining: [CONTEXT_REVIEW_QUEUE_20260705.json](CONTEXT_REVIEW_QUEUE_20260705.json) = 365 tokens with windows (n<=5 tail + važje inconclusive).
- Cursor: batch 2 = n=5/n=4 bands from the queue file (same KWIC method); then ferry handoff bundle to ChatGPT; remaining top gaps are German/TeX residue (tamže, polynomideale, const, wissensch...) = classify-don't-force.

## Done (2026-07-05, pass 28 — KWIC adjudication batch 2: n=5/4 bands done)
- [x] **Batch 2** ([log](CONTEXT_REVIEW_BATCH2_LOG_20260705.json)): 140-token band -> 61 attaches + 41 new groups + 24 exclusions. Math register recovered: **pridruženy = ASSOCIATED (prime ideal)**, **sovršeno polje = PERFECT FIELD**, **cěp = chain (doublet of veriga — chain conditions!)**, nadpolje = overfield, dvustranny = two-sided (ideal), nevlastny = improper (polarity partner of vlastny, own group), kvaternarny, derivacija, razměr, sovokupnost; verbs vyvesti (derive), zamětiti (remark), dějstvuje (acts), vhoditi (enters). 15 eponyms added (gauss weyl wedderburn chevalley brill albert deuring ostrowski grassmann weitzenböck lagrang lorenc fišer maxwell...).
- [x] **NEW CHANNEL: consistency-notes** — E/W-flavored function-word slips found inside the ISV corpus itself (kotoroj=RU-flavored ktoroj, względom=PL względem, tymy/těmi/kažno outliers): F13-type scatter in the FUNCTION layer = corpus-repair signal for the codex transcription lane, NOT lexicon material. Routed to batch-2 log consistency section.
- [x] **Lexicon v2.6, 489 groups. COVERAGE: 96.1% tokens / 76.8% types.** Queue: 231 tokens (n<=3 tail).
- Cursor: batch 3 = n=3 band next; remaining top gaps still German/TeX residue (tamže=ibid-latinism?, polynomideale=DE, const/imal=artifacts, jesmo/vezi/idenje real ISV — catch in batch 3); then handoff bundle refresh for ChatGPT.

## Done (2026-07-05, pass 29 — batch 3 + residue honesty + HANDOFF BUNDLE; loop stopped)
- [x] **Batch 3** ([log](CONTEXT_REVIEW_BATCH3_LOG_20260705.json)): 81 attaches + 40 new groups + 43 exclusions, 0 skips. Math register: prvočislo (prime, W-flavored!), sčetny (countable), prisojediniti (ADJOIN), urędženy (ordered), preslikanje (mapping, hr), hyperkompleksny, aproksimovati, nenegativny, sumovanje. 10 eponyms (köthe lüroth castelnuovo klebš christoffel wirtinger kapferer šur/schur...).
- [x] **LIVE branch-flavoring found INSIDE the ISV corpus** (consistency-notes channel): W = totiž, poněvadže, rovny, prvočislo; S = nije, jesmo, dvije, preslikanje; E = někotore, raneje, nezvodime, kotoroj. The corpus itself carries F12b/F13 scatter in the function layer — direct repair queue for the codex transcription lane.
- [x] **Residue honesty**: 23 confirmed German/English/TeX residue types moved into the metric STOP class (polynomideale, wissensch, tracts, months, iiia...) — denominator now 11,884 types. Micro-batch: vzame/sili/izčezly attached; najdti/tekst/ikaky groups.
- [x] **Lexicon v2.7b, 532 groups. COVERAGE: 96.6% tokens / 78.5% types** (day trajectory: 70.6→96.6 tokens, 39.6→78.5 types). Queue: 74 n<=2 dust tokens (dixmuiden-class: single-occurrence names/German).
- [x] **[CHATGPT_HANDOFF_BUNDLE_20260705.zip](CHATGPT_HANDOFF_BUNDLE_20260705.zip)** built (143826 bytes, sha256 C3D042DF795B3655...): defect report D1-D4, lexicon v2.7b, decision table v1.1, branch evidence v2, marker v3.2, queue+logs, coverage. Ferry to ChatGPT web when convenient.
- **LOOP STOPPED** (planned): adjudication is at diminishing returns; next moves need either ChatGPT's next round (rebuilt backlog vs v2.7b, KWIC for dust) or Floris direction (normalization decisions from the 47-row table; pan_romance C2 fill; marker weight columns extension).
