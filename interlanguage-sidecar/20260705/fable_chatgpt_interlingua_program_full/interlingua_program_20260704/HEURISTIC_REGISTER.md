# Heuristic Register — computational interlinguistics program
2026-07-04. Schema per fable5_language_only_handoff.md. status: keep | translate | test | discard.
"Translate" = the raw heuristic is right but needs its clean operational form substituted everywhere.

---
heuristic_id: HEU-DENSE-BRANCH-001
raw_heuristic: "look for dense branch points" (Floris seed transcript — where family divergence concentrates is where the interlanguage potential is)
clean_form: identify concepts and forms with high family coverage, low semantic drift, and low false-friend risk; site bridges where many standards share high recognizability
measurement: coverage score (spine attestation counts), semantic drift score over cognate sets, false-friend risk score
use_in_pipeline: candidate selection; siting table
status: keep

---
heuristic_id: HEU-MARG-INT-001
raw_heuristic: "marginal intelligibility, not marginal utility" (Floris) — a term choice is judged by whether it increases intelligibility at the margin over the dominant language
clean_form: score each contested choice by marginal_inter_intelligibility_gain relative to dominant-standard-only publication; reject forms with zero marginal gain
measurement: access_gain ledger fields; later cohort-coverage function (CLM-MARG-001)
use_in_pipeline: already operational (codex access-gain ledger, 2026-06-29)
status: keep

---
heuristic_id: HEU-NONDOM-001
raw_heuristic: "make it intelligible to everybody who doesn't already speak Spanish" (Floris, Pan-Romance seeding); "avoid rough Russian/Polish/Serbian" (Interslavic standing principles)
clean_form: dominance_penalty — the bridge must not collapse into the largest member in softened spelling; regularize the family centroid away from the dominant standard
measurement: distance of chosen forms from dominant-language forms vs from family barycenter; post-retrofit shift measurement (CLM-DOM-001)
use_in_pipeline: term selection guardrail in every lane
status: keep

---
heuristic_id: HEU-GLOBAL-001
raw_heuristic: "make it global, not global-in-the-sense-of-European" (Floris, R4+ seeding)
clean_form: reject pan-family umbrellas where internal diversity is too high (no pan-CJK, no pan-Niger-Congo); build local standards, controlled registers, and crosswalks instead; Greco-Latin academic vocabulary is not "global"
measurement: build-type decision rule (CLM-SITE-002) applied per family
use_in_pipeline: siting table build-type column; already enforced in R5–R9 split policies
status: keep

---
heuristic_id: HEU-PASSIVE-001
raw_heuristic: "readers should understand without study" (zonal tradition; Interslavic design criteria)
clean_form: passive recognizability is the primary objective term; active learnability is secondary
measurement: attestation-based recognizability now; forced-choice comprehension tests later
use_in_pipeline: vocabulary selection in all bridge lanes
status: keep

---
heuristic_id: HEU-INTL-AMBIG-001
raw_heuristic: "keep mathematical internationalisms when they reduce ambiguity" (Interslavic logbook standing principles)
clean_form: prefer international term iff ambiguity_penalty(native candidates) exceeds opacity_penalty(internationalism), assessed per cohort
measurement: 179/1310 Slavic records justify by internationalism — the tradeoff is live; needs the false-friend/ambiguity scores to become non-editorial
use_in_pipeline: term selection tie-breaker
status: translate

---
heuristic_id: HEU-SRC-LATEX-001
raw_heuristic: "find LaTeX sources" (Floris seeding of source intake)
clean_form: prefer machine-readable sources when available, but never let source FORMAT gate lane viability — PDF/.doc/archive cultures (Turkic, Central Asia) need format-relaxed intake with unchanged witness discipline
measurement: F11 re-test — count Turkic hard-row fills after format relaxation
use_in_pipeline: source intake policy
status: translate (was over-applied; suspected cause of Pan-Turkic block)

---
heuristic_id: HEU-VOTE-001
raw_heuristic: Interslavic voting machine (subgroup votes, population tie-break)
clean_form: weighted regularized barycenter over family standards with fairness weights per branch, not per capita alone
measurement: reconstruct existing ISV/Neolatino choices as approximate optima (theory H3)
use_in_pipeline: bridge-form selection; Pan-Romance kernel spec
status: keep

---
heuristic_id: HEU-THRESH-001
raw_heuristic: comprehensibility threshold / "only counts when understood" (Floris seed; ZPD/i+1 lineage)
clean_form: operational readiness thresholds per lane: coverage, false-friend risk, recognizability across ≥k branches, script policy settled, governance acceptable, human tests passed — below threshold lane stays exploratory (handoff doc "threshold idea")
measurement: per-lane gate checklist; the codex start_when_clear gates are the existing instance
use_in_pipeline: pilot gates; release gates
status: keep

---
heuristic_id: HEU-INV-001
raw_heuristic: "what survives transformation is what's real" (Floris seed; handoff doc "invariance idea")
clean_form: invariant ledger — per transformation (script conversion, register shift, bridge mapping, paraphrase) declare what must be preserved, the allowed change, the test, the failure mode
measurement: round-trip transliteration checks (already exist in Cyrillic pipeline); register-shift comprehension tests
use_in_pipeline: script sidecar validation; controlled-register QA; new — adopt the handoff's INV-* table format in lane logs
status: keep

---
heuristic_id: HEU-ID-001
raw_heuristic: intrinsic dimension as register diagnostic (theory stack, language-only form)
clean_form: use representation-complexity measures only as corpus diagnostics (formulaic vs unstable text; register width) with genre/length/language controlled; never as quality scores
measurement: local ID profiles per corpus segment (gated measurement phase)
use_in_pipeline: optional diagnostics in P4; NOT in term selection
status: test

---
heuristic_id: HEU-3AI-001
raw_heuristic: "we have three different AIs all looking at it, plus me as sanity checker" (Floris)
clean_form: interim review = independent cross-system triangulation with disagreements logged as review items; never presented as external validation
measurement: disagreement count per artifact; convergence log (e.g. ChatGPT handoff vs Fable atlas: converged on strata, sequence, schemas)
use_in_pipeline: pre-review QA on all publication-facing artifacts
status: keep (with the honesty boundary explicit)

---
heuristic_id: HEU-FEWSHOT-001
raw_heuristic: "use fewer data points to reconstruct good data anyway" (Floris, on source-starved lanes)
clean_form: for thin rows, combine (a) cross-lane transfer from the union spine, (b) morphological derivation within the language's own attested patterns, (c) explicit gap rows rather than invented forms; all reconstructions flagged reconstruction_not_attestation
measurement: fraction of thin rows fillable with flagged reconstructions vs left as gaps
use_in_pipeline: Pan-Turkic and R5/R8/R9 lanes
status: test (must not erode the source-witness discipline)

---
heuristic_id: HEU-EPONYM-001
raw_heuristic: (implicit in lanes) eponyms and symbols travel; common nouns don't
clean_form: split spine rows into transfer classes — eponymic (Noetherian, Galois), international-symbolic, family-inherited, culture-bound — with different selection rules per class
measurement: per-class attestation density in union spine (Noetherian/Galois rows vs proof-connective rows show the split already)
use_in_pipeline: stratified core spine design
status: keep (new — proposed by this consolidation)
