# Claim Ledger — computational interlinguistics program
2026-07-04. Schema per fable5_language_only_handoff.md. Status vocabulary: established | supported | plausible | speculative | rejected | out_of_scope. Everything provisional; "established" means measured on this corpus, not externally reviewed.

---
claim_id: CLM-SPINE-001
claim: The four lane term-spines (Pan-Romance, controlled Arabic, Arabic/Farsi/Persianate, Malay-Indonesian) are lane-relative inventories, not one shared skeleton: 138 unique concepts, 17 in all four lanes, 32 in ≥3, 83 lane-unique; composition tracks source genre (paper-translation vs textbook vs OER vs microdraft).
status: established (measured 2026-07-04)
source_files: UNION_TERM_SPINE_20260704.json; the four lane spine files in codex backup logs/
evidence: scripts/build_union_spine.py output; singleton list inspected for alias artifacts (1 found and merged)
operational_test: rebuild after any lane update; count shared-core growth
risk_if_wrong: none material; merge code and inputs are inspectable
next_action: stratified core spine (proof-grammar / curriculum-algebra / Noether-corpus strata) + per-lane fill lists

---
claim_id: CLM-SLAV-001
claim: The Interslavic lane's machine-readable term records carry exclusively East-Slavic witnesses: 1310 records across 95 glossary files, 0 West/South Slavic witness columns, 7/1310 rationales mentioning any W/S Slavic language, 1/1310 mentioning false friends. The German→UK/RU→ISV pipeline is the sole per-term evidence path; cross-Slavic breadth exists only in separate triangulation passes, not per term.
status: established (measured 2026-07-04)
source_files: slavic_term_dataset_20260704.json; codex backup glossary/*.json; INTERSLAVIC_LOGBOOK.md
evidence: scripts/build_slavic_dataset.py output (field-presence + rationale-mention counts, rationale fields included after schema-drift fix)
operational_test: re-run after witness-column retrofit; target = every promoted term has ≥1 W and ≥1 S Slavic witness or an explicit gap row
risk_if_wrong: CHECKED 2026-07-04 — triangulation log read: a 20-source W/S shelf (cs/pl/sk/sl/sr/hr/bg) + provenance-labeling rule + ~5–8 spot-triangulated flagship terms exist (2026-06-24, prompted by Floris), but per-term backfill was never done; records still carry zero W/S fields. Claim stands, refined. Confirmed drift instance: ring = `kolco` (E-Slavic continuity) vs `okruh`/`prsten`/`kolobar` (W/S preference), logged reviewer-sensitive.
next_action: witness-column retrofit spec using the existing 20-source shelf; per-term false-friend check; provenance labels per the lane's own 2026-06-24 rule; run BEFORE van Steenbergen contact

---
claim_id: CLM-SITE-001
claim: Lane progress in the world-family program is gated by native technical source availability, not by method capacity or family relatedness (Malay-Indonesian overtook Pan-Turkic; R5/R8/R9 parked at source-locator rung).
status: supported (consistent across all lane logs; not experimentally isolated)
source_files: coordination index; CONSTRUCTIVE_BRIDGE register; R2 pan-Turkic status nodes
evidence: per-lane rung positions vs queue order
operational_test: F11 re-test — relax LaTeX-first source-format policy for Turkic; if rows fill, part of the "scarcity" was a search artifact
risk_if_wrong: siting table overweights corpus_readiness and underweights genuine intelligibility structure
next_action: Pan-Turkic format-relaxed sourcing pass spec

---
claim_id: CLM-SITE-002
claim: Build-type choice (zonal language vs controlled register vs script bridge vs local standards) is decided in practice by standard-and-script structure, not genetic closeness: Arabic and CJK were controlled/local despite family size; Slavic/Romance got bridges; Hindustani got a script bridge.
status: supported (empirical regularity of the archipelago's own decisions)
source_files: publication section draft; candidate matrix; R7 CJK local-standard decisions; R3 controlled-Arabic decisions
operational_test: encode as decision rule in siting table; check whether it re-derives every existing build-type choice
risk_if_wrong: siting table misclassifies families where sociolinguistics dominates structure
next_action: siting table v2 with build-type rule column

---
claim_id: CLM-OBJ-001
claim: The access-gain ledger (formalized 2026-06-29 in the codex program) and the theory-stack bridge-optimization objective are the same function in two vocabularies; practice adds source_strength and lingua_franca_gap terms the theory lacks; theory adds measurable versions (neighborhood overlap, form-sim×sem-dist, barycenter distance) of the editorial terms.
status: supported (term-by-term mapping documented; no measurement yet)
source_files: ACCESS_GAIN_COHORT_METHOD_EXPANSION_20260629T043800Z.md; PAN_ROMANCE_OPTIMAL_ACCESS_HEURISTIC_INTEGRATION_20260629.md; ChatGPT-Research Framework Construction.md §4, §10; ISLAND_ATLAS.md §5
operational_test: CLM-ILO-001 pilot (below) — if model-side overlap predicts nothing, the mapping is decorative
risk_if_wrong: framework paper's central table weakens to analogy
next_action: keep as framework paper core; run pilot when measurement phase opens

---
claim_id: CLM-ILO-001
claim: Nearest-neighbor semantic overlap predicts passive intelligibility better than form similarity alone for bridge-language candidates.
status: plausible (inherited from theory sidecar; untested on this corpus)
source_files: theory sidecar (ChatGPT doc H1/H5); SIGTYP 2025 ILO paper (external)
operational_test: 200-concept pilot table (= stratified core spine per CLM-SPINE-001) scored by model-side overlap vs existing Interslavic/Pan-Romance forms; later human forced-choice comprehension
risk_if_wrong: model geometry is not useful for construction decisions; program falls back to editorial + human testing only
next_action: build core spine first; measurement gated on Floris go (CPU/API first)

---
claim_id: CLM-FF-001
claim: False friends are characterized by high form similarity + high semantic distance, and can be enumerated automatically (FormSim × SemDist) at precision/recall competitive with hand-curated lists.
status: plausible (method standard in the literature; unrun here). NOTE: per CLM-SLAV-001 the per-term records barely encode false-friend checks — the automated pass has no baseline to beat inside the lane; the Interslavic project's own curated lists are the baseline.
source_files: theory sidecar §4.4; Interslavic design criteria (external); union spine (8-variety Romance forms available as input)
operational_test: Romance pilot: enumerate over union-spine rows across es/fr/pt/gl/ca/it/ro/rm; compare against interslavic.fun-style curated lists for the Slavic twin
risk_if_wrong: penalty term stays editorial
next_action: queued after core spine

---
claim_id: CLM-MARG-001
claim: RESTRICTED FORM (post ChatGPT sanity-check 2026-07-04): the BENEFIT layer of the access ledger admits a submodular-coverage model — F(S)=Σ_u w_u·max_{a∈S} q_a(u) over reader-task universe u=(cohort, concept, context, script), monotone submodular, greedy (1−1/e) guarantee — under explicit independence/non-harm assumptions. The FULL ledger is NOT submodular (false friends, dominance collapse, pair-interactions are negative interactions) and is handled as constraints/vetoes/penalties. Companion selection rule: MAG(x,c)=Σ_g w_g(I_g(x,c)−I_g(d(c),c)) − ρ·Var_g(I_g) — marginal gain over dominant baseline minus benefit-concentration penalty.
status: plausible (formalization agreed by sidecar; unmeasured)
source_files: Floris oral heuristic; ISLAND_ATLAS.md §6b; ChatGPT sidecar response 2026-07-04 (pasted); CONCORDANCE.md
operational_test: encode MAG for one contested Pan-Romance term set with attestation-proxy I_g; check ranking sanity vs the lane's editorial choices
risk_if_wrong: framing lost, nothing else
next_action: use as the formal spine of the siting/selection section in the framework paper

---
claim_id: CLM-DOM-001
claim: Dominance drift is the recurring failure mode of family-centroid estimation at every level of the program (softened Spanish, rough Russian, Indonesian-only, Euro-lexical "internationalisms", English-shaped model latent space), and CLM-SLAV-001 is its measured instance in the proven lane.
status: supported (five documented instances + one measured)
source_files: lane guardrail docs; ISLAND_ATLAS.md F6/F10; slavic_term_dataset_20260704.json
operational_test: after witness retrofit, measure whether ISV term choices shift when W/S witnesses are added — drift magnitude = the paper's headline number
risk_if_wrong: if retrofit changes nothing, ISV choices were already family-central (also a good result — the voting-machine tradition worked)
next_action: witness retrofit, then the shift measurement

---
claim_id: CLM-REV-001
claim: No lane has any accepted external review return; every intelligibility claim in the program is currently editorial. Interim substitute: triangulation across three AI systems + Floris; planned: van Steenbergen contact after 1–2 complete authors.
status: established (package manifests state zero returns)
source_files: SLAVIC_MAINTENANCE_PUBLICATION_HANDOFF_20260703T110903Z.md; external review role packets
operational_test: n/a — process fact
risk_if_wrong: n/a
next_action: CLM-SLAV-001 cleanup is the prerequisite for a credible first review packet

---
claim_id: CLM-SCOPE-001
claim: Analogy strands (thermodynamic, biological, physical) from the seed documents are out of scope for this program.
status: out_of_scope (by direction, Floris 2026-07-04; handoff doc concurs)
source_files: fable5_language_only_handoff.md; PROGRAM.md
next_action: none — enforced in all artifacts
