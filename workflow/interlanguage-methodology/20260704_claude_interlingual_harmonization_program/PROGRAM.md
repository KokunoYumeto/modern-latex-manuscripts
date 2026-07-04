# Interlingual Harmonization Program — Proposal
2026-07-04. Companion: [CORPUS_MAP.md](CORPUS_MAP.md), [STATUS.md](STATUS.md)

## The one-paragraph thesis

The corpus contains two independently-grown halves of one research program. The **theory stack** (ChatGPT/Gemini docs) formalizes bridge-language design as constrained optimization over semantic geometry: pick forms that maximize recognizability and semantic-neighborhood preservation (ILO), sit at the regularized phylogenetic barycenter, and minimize false-friend risk and acquisition cost — with multilingual-LLM latent spaces as one fallible measuring instrument. The **practice stack** (Codex construction program) already *runs* that optimization editorially, at corpus scale, without naming it: passive-recognizability vocabulary selection is the Recognizability/ILO term; the Interslavic voting machine is the weighted barycenter; false-friend curation is the FFRisk penalty; "don't construct where a natural standard already works" is the regularizer R(B); term-promotion-under-corpus-pressure is the iterative optimizer with human gates; script sidecars keep orthography out of the semantics. The program: make the correspondence explicit, compute the objective's terms from data the project already generates, use it to (a) audit and refine the live lanes and (b) *predict siting* — which families support a zonal bridge vs a controlled register vs a script bridge — and package the result for Zenodo/GitHub.

## Standardized vocabulary (adopt everywhere, per ChatGPT §1)

- **zonal auxiliary language** (not "interlanguage" — that's an SLA term)
- **neural interlingual representation(s)** — plural; never "the universal language of thought"
- **controlled technical register**, **script/standard bridge** — the other two build types (Codex typology)
- **passive recognizability**, **term spine**, **term promotion**, **source witness**, **non-erasure boundary** — keep the Codex operational vocabulary as-is; it's good
- Tier-3 metaphors (FEP-as-mechanism, DNA-of-concepts, language-as-gravity, holography/ER=EPR) are **out of scope entirely** (Floris 2026-07-04): the program is language/zonal-register work only. The biology/physics analogy strands in the seed docs were heuristic scaffolding; nothing downstream depends on them.

## The correspondence table (core of the framework paper)

| Practice heuristic (Codex, operational) | Theory term (formal) | Measurable by |
| --- | --- | --- |
| Passive recognizability selection | Recognizability(x,c) + mean ILO(B, Lᵢ) | kNN-overlap of aligned concepts across family embeddings; human cloze tests |
| Interslavic voting machine (6 subgroups, split votes, population tiebreak) | argmin Σ wᵢ D(B,Lᵢ)² + λR(B) — regularized barycenter | reconstruct actual Interslavic choices as approximate optima (H3) |
| False-friend curation lists | FFRisk = Σ wᵢ FormSim(b(c), xᵢ(c′)) · SemDist(c,c′) | automated enumeration over cognate DBs + embeddings; predicts comprehension errors (H2) |
| "Controlled register where a standard exists" (Arabic, Chinese) | regularizer R(B) dominates: HumanCost + political-acceptability term | siting model axes (below) |
| Term promotion under corpus pressure | iterative optimization with human accept/reject gates | glossary/ term-rationale ledgers = the audit trail |
| Script sidecars (Latin/Cyrillic; Perso-Arabic/Devanagari) | orthographic transform layer, separate from semantic objective | deterministic converters + render gates (already built) |
| Semantic drift / hard rows | branch-sensitive lexical instability zones (not branching markers) | diachronic-embedding divergence over cognate sets (H4) |
| ZPD / comprehensible-input threshold (Floris's heuristic) | update-eligible input (H7) | scaffolded vs opaque input experiments — later, human-subject tier |

## Phases (grind units; cursor in STATUS.md; all inline, no agents, no GPU without explicit go)

**P0 — Consolidation (this week).**
1. ~~Corpus map~~ (done, CORPUS_MAP.md).
2. Deep-read the pending Stratum-B files (INTERSLAVIC_LOGBOOK first) and extract two registers:
   - `CLAIM_LEDGER.md` — every load-bearing claim across all strata, with source pointer and rigor tier (established / testable-Hn / quarantined).
   - `HEURISTIC_REGISTER.md` — every operational rule from the practice stack, stated crisply, with its formal counterpart from the correspondence table (or "no counterpart yet" — those are the interesting ones).
3. Backup-vs-GitHub reconciliation: which interlanguage logs exist only in the backup dump → list for a consolidation commit (no push without go).

**P1 — Framework synthesis.**
Write `FRAMEWORK.md` → LaTeX: "Zonal auxiliary language construction as measurable optimization: harmonizing an operational AI translation pipeline with cross-lingual representation geometry." Structure: the two stacks; the correspondence table; the standardized vocabulary; the three rigor tiers; the governance model (non-erasure, forkable/rejectable — this is a genuine contribution, keep it central); honest-limits section (never-certify style). The ChatGPT doc's H1–H8 + red-team become the hypotheses/limits sections nearly verbatim (it's Floris's own steered output — cite the workflow, per open-source-workflow policy).

**P2 — Siting model v1 ("prediction of good places").**
Operationalize the axes, no GPU needed for v1:
- cognate density & drift hazard (comparative-linguistics data: cognacy DBs, Swadesh/NorthEuraLex-type lists)
- false-friend load between major members (form-sim × sem-dist over shared lexicon)
- script fragmentation (count + convertibility)
- existing-standard coverage (does a natural written standard already solve access?)
- education/population utility (speakers split across standards, OER availability)
- authority landscape (is there a community project to defer to — Interslavic-portal analog?)
Score the Codex priority queue (Pan-Romance, Pan-Turkic, controlled Arabic, Persianate, Hindustani, Malay-Indonesian, Swahili, Indic, Dravidian, Berber…) → `SITING_TABLE.md`. Agreement with the queue validates the editorial heuristics; disagreement is a finding. Both publishable.

**P3 — Feedback into live lanes.**
- Interslavic: restate the term-promotion gate as an explicit criterion (recognizability estimate + FFRisk check) the ledgers can log per term.
- Pan-Romance kernel spec: apply the objective to the next lane before it scales — vocabulary rule = barycenter over PT/ES/CA/FR/IT/RO witnesses with FFRisk veto; deliberately non-Spanish regularizer (the Codex draft's own requirement, now formalized).
- Persianate/Turkic: siting-model verdicts feed the start/block gates already defined in the bridge register.

**P4 — Measurement (optional, gated).**
Embedding experiments on the family corpora: ILO/kNN-overlap for Slavic set vs Romance set; latent-pivot (English-bias) audit; automated false-friend enumeration vs the hand-curated lists (precision/recall of the heuristic). Uses the Noether parallel corpus (unique asset: concept-aligned de/en/fr/isv±ar/fa). CPU/API-first; local GPU only with explicit go, one foreground job, VRAM cap.

**P5 — Packaging.**
Zenodo record: framework paper + claim ledger + heuristic register + siting table + data pointers; zip copy to `Documents\arxiv_latex\_zips\`; commit to a `claude/interlingua-harmonization-20260704` branch (push only on go); handoff note in the repo's cross-session-coordination pattern so the other machine's Codex picks it up.

## Publishable units (Zenodo track)

1. **Framework/position paper** (P1) — publishable soon; novelty is the practice↔theory correspondence + the governance model, both grounded in a real operating pipeline (nobody else has an operational zonal-register production line to formalize).
2. **Siting table + methodology** (P2) — research-level artifact; the "where should bridge registers exist" question answered with explicit, criticizable scoring.
3. **Empirical note** (P4, if run) — do the editorial heuristics agree with representation-geometry measurements on the project's own corpus?

## Honest-limits (standing, never-certify)

- No claim that LLMs have "a" universal interlingua; representations are plural, layer-dependent, English-biased — always run/report the latent-pivot audit.
- No claim of community authority: all outputs review-ready, forkable, rejectable (Codex boundary stands).
- Tier-3 metaphors stay quarantined; the red-team's safe versions are the ceiling of what gets asserted.
- Siting scores are decision support for where to spend construction effort, not verdicts on languages or communities.
