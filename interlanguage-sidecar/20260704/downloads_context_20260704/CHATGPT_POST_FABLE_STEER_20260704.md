# Post-Fable steer: interlingual programme state and next actions

Date: 2026-07-04
Scope: language/zonal-register work only; no biology/physics analogy layer.
Boundary: this is a steering and audit note over uploaded programme artifacts. It does not certify any language form and does not replace external review.

## 1. Immediate assessment

Fable's loop did the right kind of work: it converted a conceptual lane into a file-pinned programme with measured internal results. The current state is no longer merely a speculative framework; it has reproducible artifacts, frozen baselines, postwriteback deltas, a concept ledger, a C2 fill dispatch, and a framework-paper draft.

The strongest result is still the measured dominance/witness-skew story. The pre-backfill branch weighting gives East/West/South mass 2395/64/59, i.e. 95.1% East Slavic, with effective branches 1.257 of 3. The partial writeback upgraded 182 rows and moved the distribution to 83.5% / 8.0% / 8.5%, with effective branches 1.754 and KL-to-balanced 0.537. This makes a clean before/after result: the pipeline could quantify its own seeding bias, then partially correct it from already-present source shelves without silently overwriting the baseline.

The second strong result is adverse evidence. The programme now distinguishes support, absence, and adverse evidence. That distinction is not optional: the `Ränderung -> ring` and `irreducible -> reducible` failures show that wrong-sign evidence cannot be represented as low confidence. It must be a typed veto or do-not-merge relation.

The third strong result is concept-spine architecture. The union spine showed that the nominal 60-term lane spines were not commensurable; C2, the stratified core spine, is now the correct comparison object. The C2 dispatch is actionable and bounded.

## 2. What should not be blurred

### 2.1 Source authority is not the same as interlingual witness

The Noether source corpus is the authority for the canonical German mathematical text and for concept anchoring in the historical source. It is not, by itself, evidence that a target-language term is good. It should feed:

- German source-term normalization;
- concept IDs;
- source-context snippets;
- source-side disambiguation;
- paper/section/page anchors;
- historical-vs-modern concept warnings.

It should not directly feed:

- West/South Slavic witness status;
- Pan-Romance family support;
- controlled-Arabic promotion;
- Japanese/Spanish/French witness status without independent target-language source review.

### 2.2 Draft translation archives are not witnesses

The Chatnotes/Stratum-D tree is highly valuable as a triangulation database, candidate-form reservoir, register comparison surface, and error-mining corpus. But because it consists of AI-era drafts and compaction-risk material, it remains `linked/unreviewed` until independently verified. It can propose candidate concepts; it cannot certify them.

### 2.3 Linkage is not evidence

Every cross-lane table must preserve three separate statuses:

```text
linked_to_concept
witnessed_for_branch
reviewed_for_bridge_use
```

The partial Slavic writeback should not be interpreted as full review clearance. It is concept-shelf support, not per-row form verification.

## 3. Paper draft status

The draft is useful, but it still needs editorial normalization before it is treated as a paper. In the uploaded file, the Introduction and Abstract appear after the main sections rather than at the top. That is a mechanical reorder, not a conceptual problem.

Recommended paper order:

```text
Title
Abstract
1. Introduction
2. Two vocabularies, one objective
3. Objects and discipline
4. Result 1: spine drift
5. Result 2: witness monoculture
6. Result 3: backfill and F12
7. Result 4: triangulation catches concrete defects
8. Result 5: adverse evidence
9. Siting model
10. Limits
11. Availability
Appendix A. Artifact inventory
Appendix B. Flag schemas
Appendix C. C2 fill dispatch
Appendix D. Branch-weighting definitions
```

Before any external circulation, the draft should be patched for:

- abstract/introduction placement;
- exact artifact filenames;
- distinction between internal triangulation and validation;
- no claim that Interslavic forms are correct, only that the pipeline discovered and triaged review questions;
- no reliance on draft translations as witnesses;
- no hidden promotion of `prsten`, `kolco`, or any ring-term candidate before authority review.

## 4. The `ring` memo: recommended framing

The ring family is the flagship review row, but the paper should not present it as "Fable solved ring." The right statement is:

> The audit found that the status quo `kolco` family has high internal corpus pressure and high East-Slavic continuity, but the West/South shelf supplies competitor-only evidence. The row is therefore the highest-leverage authority-review item.

If the memo recommends `prsten` as a running surface with `kolco` as a doublet, that must be labelled as a review proposal, not a project decision. The key value is that one review question could settle or reclassify roughly the whole F10-3 cluster.

## 5. Next obvious tasks

### Task A. Patch the framework draft into paper order

This is mechanical and should happen before more mining. It produces the first clean readable object.

Deliverable:

```text
FRAMEWORK_DRAFT_ORDERED_20260704.md
```

### Task B. Build `ARTIFACT_INDEX.md`

The programme now has enough files that the next useful artifact is an index, not another analysis essay.

Schema:

```text
artifact_name
role
stratum
source_or_derived
input_files
output_files
hashes_if_known
status
safe_to_cite_in_paper: yes/no
safe_to_show_external: yes/no
notes
```

### Task C. Write `SOURCE_USE_POLICY.md`

This should formalize how the Noether source files, Chatnotes drafts, W/S shelf, lane spines, and external-review packets differ.

Core categories:

```text
canonical_source_authority
language_family_witness
draft_translation_triangulation
candidate_form_source
adverse_evidence_source
external_authority_review
```

### Task D. Produce `RING_REVIEW_PACKET_v0`

Do not change terms. Produce a compact reviewer packet:

```text
one-page memo
candidate table
current corpus pressure
W/S competitor evidence
known adverse relation for okruh with East округ/district risk
questions for reviewer
no verdict
```

### Task E. Finish C2 dispatch before broad siting

C2 is the worklist. Each lane needs `witnessed | gap | not_applicable`, not invented filler. The dispatch already gives missing counts by lane; now the pipeline should produce lane-specific fill ledgers rather than another global map.

## 6. Safe loop rule for Fable/Codex

Fable can continue without asking when the next task is all of the following:

```text
read-only or classification-only
no new target-language forms
CPU/local only
emits source pointers/counts
preserves previous artifacts rather than overwriting them
moves a declared gate forward
```

Fable should stop and ask before:

```text
promoting a bridge-language form
renaming an established candidate
pushing to GitHub or Zenodo
contacting external reviewers
using draft translations as witnesses
running model/embedding/GPU work
creating another zip when the package cap is already reached
```

## 7. Current paper-grade claims

These are the claims that are currently strong enough to write around:

1. The programme is one production system, not many isolated translation projects.
2. The access-gain ledger is the operational form of the theory-side bridge objective.
3. The nominal lane spines drift by source genre; a stratified core is required.
4. The initial Interslavic machine-readable evidence base was effectively one-branch.
5. Witness backfill from already-present W/S sources measurably improves branch balance.
6. The ring family is the highest-leverage review cluster, not a settled term correction.
7. Adverse evidence requires typed relations, not negative scalar weights.
8. Internal triangulation catches real defects but is not external validation.
9. Source floor and build type must precede optimization.
10. Draft multilingual translation shelves are triangulation material, not witness material.

## 8. Immediate instruction block for Fable

```text
Continue linguistics-only.

Next unit:
1. Reorder FRAMEWORK_DRAFT_20260704.md into paper order as FRAMEWORK_DRAFT_ORDERED_20260704.md.
2. Create ARTIFACT_INDEX.md for every file in the interlingua_program_20260704_v1 package.
3. Create SOURCE_USE_POLICY.md distinguishing canonical source authority, language-family witness, draft triangulation, candidate source, adverse evidence, and external authority review.

Do not add new target-language wording.
Do not promote or reject any term.
Do not create a new zip unless consolidation removes or supersedes an older package.
```
