# Noether Corpus Translation Lane Review and Governance Scaffolds

Generated: 2026-07-04

Status: reusable scaffolds for Sessions L, Romance split lane, E, F, G, H, I, J, and K. These forms support corpus translation/source lanes directly. They do not approve terms, translations, pilots, or canonical gates.

## Scaffold 1: Corpus Source-Evidence Intake

```text
Intake ID:
Generated:
Receiving lane:
Route ID:
Corpus segment or stream:

Source evidence class:
- native_register_source
- source_fidelity_witness
- comparator_only
- script_or_orthography_source
- reviewer_return
- rejected_candidate
- source_gap

Source row:
| source_id | language/standard | script | source type | local path or URL | hash | page/section anchor | extraction state | license state | allowed use | forbidden use |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Required lane action:
- capture_source
- inspect_page
- extract_text
- render_check
- reviewer_question
- reject_candidate
- defer_source_gap

Boundary:
The source row supports evidential review only. It does not approve target wording.
```

## Scaffold 2: Corpus Reviewer Packet Cover

```text
Packet ID:
Generated:
Receiving lane:
Route ID:
Reviewer role:
- native/near-native technical reviewer
- mathematician/domain reviewer
- language project/community reviewer
- script/orthography reviewer
- teacher/learner reviewer
- accessibility reviewer

Review scope:
Review exclusions:

Materials included:
- source manifest:
- term-governance matrix:
- render/visual sample:
- script policy:
- rejected candidate list:
- questions:

Questions:
1. Does the evidence support the stated claim?
2. Are any standards, scripts, or variants collapsed incorrectly?
3. Are any source anchors weak, OCR-risked, or rejected?
4. Which items should be accepted, rejected, corrected, or deferred?
5. What is the reviewer's authority limit?

Return fields:
- reviewer_id:
- role:
- date:
- authority_scope:
- accepted_corrections:
- rejected_items:
- unresolved_items:
- permission_to_cite:

Boundary:
No reviewer return changes a gate until it is ingested in a separate ledger.
```

## Scaffold 3: Authority Claim Crosswalk

```text
Crosswalk ID:
Receiving lane:
Route ID:

Claim class:
- mechanical
- evidential
- pedagogical
- community
- canonical_edition

Evidence required:
| claim class | required evidence | local validation enough? | external authority required |
| --- | --- | --- | --- |
| mechanical | build, hash, render, extraction, script checks | yes | no |
| evidential | source shelf, page anchors, rejected candidates | partly | source reviewer may be needed |
| pedagogical | teacher/learner review, classroom context | no | yes |
| community | language/project/community acceptance | no | yes |
| canonical_edition | full artifact set plus accepted review returns | no | yes |

Highest claim allowed now:

Claims forbidden now:
```

## Scaffold 4: No-Approval Default Ledger

Use this when handing work to a child lane that must keep every approval count at zero.

```text
Ledger ID:
Generated:
Receiving lane:
Route ID:

Counts:
- accepted_terms: 0
- accepted_bridge_surfaces: 0
- reviewer_returns_ingested: 0
- community_consent_claims: 0
- pilot_ready_units: 0
- canonical_translation_units: 0

Reason counts remain zero:

Allowed next work:

Forbidden next work:
```

## Scaffold 5: Review Return Ingestion Ledger

```text
Ingestion ID:
Generated:
Receiving lane:
Route ID:
Reviewer packet:
Return received:
- yes
- no

If yes:
Reviewer role:
Authority scope:
Accepted corrections:
Rejected items:
Required changes:
Items still open:

Ingestion result:
- no_gate_change
- mechanical_note_only
- evidential_note_only
- term_review_not_approval
- gate_closure_candidate
- gate_closed

Gate closed?
- no
- yes, with evidence path:

Boundary:
Reviewer feedback is not community consent unless explicitly and validly scoped that way.
```

## Scaffold 6: Script, Orthography, and Render Governance

```text
Record ID:
Generated:
Receiving lane:
Route ID:
Scripts/orthographies:

Decision state:
- source_status_only
- deterministic_sidecar_allowed
- parallel_authority_facing_scripts_required
- comparator_only
- rejected

Protected zones:
- TeX commands
- math environments
- labels/refs
- bibliography
- proper names
- quoted source titles
- reviewer annotations

Checks:
- font coverage:
- text extraction:
- visual sample:
- script conversion:
- reviewer route:

Boundary:
Script handling is not cosmetic when script choice affects access, identity, or authority.
```

## Scaffold 7: Term Governance Without Surfaces

Use this when the lane needs to track concepts but is not authorized to write or approve term surfaces.

```text
Matrix ID:
Receiving lane:
Route ID:

| row_id | concept_id | source concept anchor | target-surface field | current status | reviewer needed | approval state |
| --- | --- | --- | --- | --- | --- | --- |
| T001 |  |  | blank_until_authorized | source_gap | native/domain | not_approved |

Allowed statuses:
- source_gap
- source_backed_seed_not_approved
- observed_anchor_needs_review
- rejected_candidate
- accepted_by_reviewer_not_yet_ingested

Forbidden status unless gate closed:
- approved_after_gate_closure
```

## Scaffold 8: Child-Lane Handoff Manifest

```text
Manifest ID:
Generated:
Receiving lane:
Route IDs:

Files included:
- routing card:
- source manifest:
- authority ADR:
- reviewer packet cover:
- no-approval ledger:
- term-governance matrix:
- gate checklist:
- script policy, if applicable:

No-go block copied:
- no accepted bridge surfaces
- no term promotion
- no community-consent claim
- no canonical edition claim
- no GitHub push from this lane

Receiving lane next action:
```

## Owner-Specific Notes

| Owner | Required scaffold emphasis |
| --- | --- |
| Session L | Script-sidecar governance and Interslavic authority limits |
| Romance split lane | Row-level fallback review and source-control separation |
| Session E | Native-edition source baseline and Korean-adjacent addendum boundary |
| Session F Arabic | RTL/script non-erasure, exact-source evidence, reviewer route |
| Session F Persianate | Per-standard split, cross-register ADR, no Farsi/Dari/Tajik collapse |
| Session G | Exact content capture, review returns, no title-only authority |
| Session H | OCR/Unicode triage, source-return ledgers, no family bridge |
| Session I | Access ethics, source/reviewer maps, no pilot |
| Session J | Hard-blocker source retry and script-standardization boundary |
| Session K | Slot returns, relation/function review forms, zero approvals |
