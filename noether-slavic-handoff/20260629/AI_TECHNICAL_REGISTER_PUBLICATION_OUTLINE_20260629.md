# AI-assisted technical-register construction publication outline - 2026-06-29

This artifact turns the Noether multilingual workflow into a publishable research/report outline. It covers AI-assisted technical-register construction, multilingual mathematical translation, interlanguage methodology, educational utility, open-source handoff, and authority boundaries.

It is not a claim that any new language lane is complete. It is a manuscript scaffold and claim-control document for research publication.

Companion machine-readable file: `AI_TECHNICAL_REGISTER_PUBLICATION_OUTLINE_20260629.json`

## Working Titles

- Auditable AI-assisted technical-register construction for multilingual mathematics
- Source shelves before translation: a reproducible workflow for mathematical register transfer
- Interlanguage authority and open-source handoff in AI-assisted technical translation

## Core Thesis

AI-assisted translation can be useful in high-register mathematical contexts only when it is embedded in a workflow that separates mechanical validation, source evidence, terminology governance, render validation, educational usefulness, and native/community authority.

The Noether workflow is a case study in making that separation explicit through source shelves, term anchors, TeX/PDF builds, manifests, review packets, correction ledgers, and open handoff.

## Contributions

- A workflow model for evidence-first technical translation across natural-language, multi-register, zonal/interlanguage, and constructed-pilot lanes.
- A machine-readable artifact discipline: source shelves, term-anchor seeds, glossary/rationale logs, manifests, validation scripts, review packet templates, and accepted-correction ledgers.
- A claim taxonomy separating mechanical, evidential, pedagogical, community, and canonical-edition claims.
- A terminology-governance model that distinguishes observed native terms, project proposals, reviewer-approved terms, script sidecars, interlanguage proposals, and constructed-pilot terms.
- A method for treating open-source handoff as inspectable and forkable without mistaking it for community consent.
- A research framing for semi-constructed and interlanguage work under the translation header without collapsing it into canonical publication claims.

## Case Study Lanes

| Lane | Research role | Current evidence state | Publication caution |
| --- | --- | --- | --- |
| Ukrainian/Russian/Interslavic-Panslavic | Mature Slavic lane and dual-script sidecar precedent | Review-ready lane maintained by prior checkpoint pointers | Still requires review-return ingestion and source corrections if new returns arrive. |
| Simplified Chinese | Natural-language lane with ongoing Paper34 translation checkpoint | Source reinforcement and term-anchor seed; Paper34 through Section 18 checkpoint recorded | Native review and page-inspected glossary required before final claims. |
| French/Spanish | Mature Romance natural-language lanes and contrast set for any later Romance bridge work | Source shelves and term-anchor seed | Must not be conflated with Pan-Romance or Neolatino experiments. |
| Japanese | Natural-language lane with strong ring/module evidence | Source shelf and term-anchor seed | Needs page-inspected Noetherian phrasing and native review. |
| Persian-family registers | Multi-standard/register family problem | `fa_IR` strong seed; `prs_AF` broad only; `tg_Cyrl_TJ` unresolved | Sublanes must remain separate without external cross-register authority. |
| Arabic | RTL and OCR/provenance stress test | Reinforced evidence shelf but module/representation gaps remain | Needs native review, OCR source inspection, and RTL render validation. |
| Interlanguage / constructed pilot | Methodology and authority boundary lane | Bibliography, authority matrix, reviewer framework, review packet templates | Research/pilot only unless language-community and mathematical review support more. |

## Method Sections

### 1. Source Shelves Before Translation

Define a source shelf as a curated set of native-register mathematical witnesses. Explain why source shelves precede translation: they reveal terminology, syntax, register, typography, and educational norms before an AI system proposes text.

Evidence examples:

- Open university PDFs and TeX where available.
- Algebra, invariant theory, number theory, fields/rings/ideals/modules/representations.
- Undergraduate math/physics sources when advanced algebra sources are thin.
- Local cache metadata without redistributing source PDFs unless licensing permits.

### 2. Term Anchors Are Not Term Approvals

Define a term anchor as an observed match from a source witness. A term anchor can justify further inspection but cannot approve project terminology by itself.

Required distinction:

- Observed source anchor.
- Proposed project term.
- Page-inspected term.
- Reviewer-approved term.
- Accepted correction.
- Deprecated or rejected term.

### 3. Mechanical Validation

Describe local validation:

- TeX build status.
- PDF presence and page counts.
- Hashes and manifests.
- Script-sidecar checks.
- JSON/schema validation.
- No source PDFs committed to Git handoff payload.

State the limit: mechanical validation proves reproducibility and consistency, not native acceptability.

### 4. Render and Typography Validation

Render validation is part of language quality for mathematical documents. This includes CJK line breaking, RTL directionality, Latin/Cyrillic sidecar equivalence, formula association, labels, punctuation, and glossary ordering.

### 5. External Authority and Review

Authority is role-specific:

- Native technical reviewer for idiom and mathematical convention.
- Educator reviewer for learner-facing utility.
- Community or project reviewer for interlanguage authority.
- Linguist/interlinguistics reviewer for constructed or zonal language claims.
- Script/tooling reviewer for sidecars and transliteration.

### 6. Interlanguage and Constructed-Language Method

Treat interlanguage work as an object of research and governance. Existing projects are communities and institutions, not empty design spaces. Constructed pilots can be methodologically useful without being canonical editions.

### 7. Open-Source Handoff and Anti-Extractive Framing

Open source means inspectable, modifiable, and forkable. It does not mean accepted, authorized, or culturally safe. Pair FAIR-style reproducibility with CARE/TRUST-style authority and responsibility.

### 8. Review-Return Ingestion

Accepted corrections should become ledgers, terminology updates, TeX/PDF rebuilds, manifest revisions, and handoff notes. Rejected or uncertain corrections should remain visible with rationale.

## Figure and Table Plan

| Item | Purpose |
| --- | --- |
| Workflow diagram | Source shelf -> term anchor -> draft -> render -> review packet -> correction ledger -> rebuild -> handoff. |
| Claim taxonomy table | Mechanical, evidential, pedagogical, community, and canonical-edition claims. |
| Lane status table | Current state and next gate for each language lane. |
| Term lifecycle table | Observed, proposed, page-inspected, reviewer-approved, accepted, deprecated. |
| Authority matrix | Which reviewer role can validate which claim. |
| Artifact manifest example | Machine-readable hashes, counts, and status flags. |

## Claims Allowed Now

- The PC branch contains reproducible handoff artifacts for source shelves, term anchors, research methodology, reviewer frameworks, and status manifests.
- The workflow has machine-readable validation for artifact hashes, counts, and no-PDF handoff boundaries.
- The research lane has enough structure to support a paper/report outline on AI-assisted technical-register construction and authority boundaries.
- The non-Slavic lanes have seed evidence and terminology anchors, not finished canonical editions.

## Claims Not Allowed Yet

- That any non-Slavic lane is complete.
- That term-anchor rows are approved terminology.
- That open-source availability is community consent.
- That constructed or semi-constructed language pilots are canonical Noether editions.
- That local validation replaces native, educator, community, or external technical review.

## Reproducibility Package Expectations

Minimum package for a publishable workflow checkpoint:

- Machine-readable manifest.
- Source shelf records with URLs and access status.
- Term-anchor seed with source identifiers and page references.
- Glossary/rationale log.
- TeX/PDF artifact hashes or handoff pointers.
- Visual inspection note.
- Review packet template or completed review packet.
- Accepted-correction ledger.
- Script list and validator output.
- GitHub, Drive, Zenodo, or release pointers as appropriate.

## Article Outline

1. Introduction: technical-register translation as an authority-sensitive problem.
2. Related work: interlinguistics, language planning, constructed-language pedagogy, OER, FAIR, CARE, TRUST, and open source.
3. Workflow: evidence shelves, term anchors, rendering, manifests, review packets, ledgers.
4. Case study: Noether multilingual lanes and why each lane has different authority gates.
5. Terminology governance: observed terms, proposed terms, approved terms, sidecars, and pilots.
6. Interlanguage methodology: useful bridges, risks, and canonical-edition limits.
7. Educational and open-source handoff: local ownership, forkability, and review boundaries.
8. Results to date: artifact counts, validation state, and unresolved gaps.
9. Limitations: source bias, OCR, licensing, external review, local authority.
10. Conclusion: AI can help build auditable workflows, but cannot confer language authority by itself.

## Immediate Next Gates

- Build a terminology-governance matrix for all lane types.
- Convert current review packet templates into per-lane packets once artifacts are ready.
- Add completed review-return ledger templates.
- Continue language-lane work toward page-inspected glossaries and native review packets.
