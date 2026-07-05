# Noether Governance and Source-Evidence Templates

Generated: 2026-07-04

Status: reusable child-lane templates. These templates create governance, source-evidence, reviewer, and decision records only. They do not approve terms, translations, bridges, pilots, or canonical editions.

## Template 1: Child-Lane Routing Intake

```text
Artifact:
Generated:
Child lane:
Session/thread:
Parent routing ID:
Route bucket:
Existing lane owner:
Novel packet owner, if any:

Recovered stream:
Source artifacts inspected:
- local_or_branch_path:
  sha256_if_known:
  role:

Construction decision, choose one:
- native_edition
- natural_language_translation_lane
- regional_standard_sublane
- multi_standard_family_lane
- script_or_orthography_bridge
- crosswalk_or_comparator
- zonal_interlanguage_research
- constructed_language_pilot_research_only
- controlled_domain_register_research_only
- computational_pivot_method_only
- reject_or_defer_source_gap

Current publication state, choose one:
- source_status_only
- research_note
- reviewer_packet_draft
- educational_pilot_candidate_not_started
- candidate_translation_lane_not_review_ready
- review_ready_edition

Evidence claim allowed:
- mechanical
- evidential
- pedagogical
- community
- canonical_edition

Highest claim currently supported:

Boundary statement:
This artifact proves:
This artifact does not prove:

No-go statements:
- No accepted bridge surfaces.
- No term approval.
- No native/community consent claim.
- No canonical translation claim.
- No gate-ledger change.
```

## Template 2: Source-Evidence Manifest

```text
Artifact:
Generated:
Lane:
Source root:
Manifest path:

Evidence state, choose one per source:
- source_backed
- page_anchor_verified
- text_extracted
- OCR_or_encoding_risk
- PDF_fallback_only
- metadata_only
- infrastructure_only
- failed_search
- explicit_source_gap
- rejected_candidate

Source table:
| source_id | language_or_standard | script | source_type | local_path_or_url | license_status | extraction_state | page_or_section_anchor | hash | use_allowed | use_not_allowed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| S001 |  |  |  |  |  |  |  |  | source evidence only | term approval or community consent |

Required checks:
- File exists or URL captured.
- Hash recorded for local files where available.
- Page/section anchor recorded when the source is cited for a term or usage claim.
- Source language/standard is not collapsed into a neighboring standard.
- Rejected candidates are preserved with rejection reason.
- Any OCR, encoding, or script risk is explicit.
```

## Template 3: Authority Decision Record

```text
ADR ID:
Generated:
Lane:
Decision subject:

Decision type, choose one:
- route_to_existing_lane
- keep_as_novel_research_packet
- keep_as_comparator_only
- defer_source_gap
- reject_as_authority
- prepare_reviewer_packet

Authority claim under review:
- mechanical
- evidential
- pedagogical
- community
- canonical_edition

Decision:

Evidence considered:
- source_artifact:
  exact_status:
  limitation:

Required external authority before stronger claim:
- native_language_reviewer:
- domain_mathematician:
- teacher_or_learner_review:
- community_or_project_authority:
- script_or_orthography_authority:

Rationale:

What this decision allows:

What this decision forbids:

Rollback or rejection path:

Open blockers:
```

## Template 4: Reviewer Packet Cover Sheet

```text
Packet:
Generated:
Lane:
Reviewer role needed:
- native_or_near_native_technical_reviewer
- mathematician_or_domain_reviewer
- teacher_or_pedagogy_reviewer
- language_project_or_community_reviewer
- script_or_orthography_reviewer

Review scope:
Review exclusions:

Items sent for review:
- source status table:
- term-governance table:
- sample text, if authorized:
- render/visual evidence, if any:
- script sidecar, if any:

Questions for reviewer:
1. Does the source evidence support the stated evidential claim?
2. Are any terms, registers, or scripts unacceptable or misleading?
3. Are any local standards or variants being collapsed incorrectly?
4. Is the artifact suitable for further review, educational pilot consideration, or rejection?

Reviewer return fields:
- reviewer_name_or_anonymous_id:
- role:
- date:
- accepted_corrections:
- rejected_items:
- required_changes:
- authority_limit:
- permission_to_cite_review:

Post-review gate:
- No term is approved until the accepted-correction ledger is ingested.
- No community claim follows from one reviewer unless that reviewer explicitly has such authority.
```

## Template 5: Term-Governance Matrix

Use this table for term governance without writing accepted surfaces unless the child lane already has authority to record them.

```text
| row_id | concept_id | concept_definition_source | observed_source_anchor | proposed_project_usage | status | reviewer_needed | rejected_alternatives | rationale | approval_state |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| T001 |  |  |  | blank_until_authorized | source_gap | native/domain |  |  | not_approved |
```

Allowed `status` values:

- source_gap
- observed_anchor_needs_review
- source_backed_seed_not_approved
- reviewer_question
- rejected_candidate
- accepted_by_reviewer_not_yet_ingested
- approved_after_gate_closure

Required invariant:

`approved_after_gate_closure` must remain unused unless the child lane records the exact reviewer/source gate closure and accepted-correction ingestion.

## Template 6: Script and Orthography Policy Record

```text
Artifact:
Generated:
Lane:
Scripts/orthographies affected:

Policy question:

Evidence:
- project_or_institutional_source:
- local usage source:
- render/encoding source:
- reviewer source:

Decision state:
- undecided
- source_status_only
- deterministic_sidecar_allowed
- parallel_authority_facing_scripts_required
- comparator_only
- rejected

Protected zones:
- TeX commands
- math environments
- labels and refs
- bibliography
- proper names
- quoted source titles
- reviewer annotations

Validation required:
- script conversion check
- font/render check
- text extraction check
- visual sample/contact sheet
- reviewer check

Boundary:
Script handling is not cosmetic when script choice affects accessibility, authority, or identity.
```

## Template 7: Novel Interlanguage Construction/Source-Evidence Packet

```text
Packet ID:
Generated:
Novel stream:
Status: non-canonical/research-only

Object type:
- zonal_interlanguage_project
- global_auxiliary_or_worldlang_comparator
- controlled_domain_register
- computational_interlingua_or_mt_pivot
- cross_family_access_method

Why no existing lane owns it cleanly:

Known project/community/institutional sources:
| source_id | title | URL or local path | source role | authority limitation |
| --- | --- | --- | --- | --- |

Mathematical-register evidence:
| evidence_id | source | source_type | extraction_state | math_register_relevance | limitation |
| --- | --- | --- | --- | --- | --- |

Governance questions:
- Who can reject the proposal?
- Who can fork or correct it?
- Who can approve educational use?
- Who can approve community/project language use?
- Who can approve mathematical terminology?

Construction fields:
- grammar_policy:
- morphology_policy:
- lexicon_policy:
- script_policy:
- proof_prose_policy:
- notation_policy:
- source_fidelity_policy:

Allowed outputs:
- source shelf
- authority map
- comparator note
- reviewer-question list
- method publication note

Forbidden outputs:
- accepted bridge surfaces
- learner-facing pilot
- canonical edition
- community-consent claim
- replacement of native-language lane
```

## Template 8: Gate-Closure Checklist

```text
Gate:
Lane:
Attempted closure date:

Required evidence:
- source shelf complete:
- source anchors page/section verified:
- local files hashed:
- rejected candidates logged:
- render/visual validation complete, if applicable:
- reviewer packet sent:
- reviewer return received:
- accepted-correction ledger ingested:
- authority scope stated:
- rollback path recorded:

Result:
- remains_open
- closed_for_mechanical_claim_only
- closed_for_evidential_claim_only
- closed_for_reviewer_packet_readiness
- closed_for_review_ready_edition

Reason:

Claims still forbidden:
```

## Child-Lane Minimum Handoff Bundle

Every child lane receiving a routed interlanguage stream should receive, at minimum:

- Template 1, filled as route intake.
- Template 2, filled as source-evidence manifest.
- Template 3, filled as authority decision record.
- Template 5, included blank unless term surfaces are already authorized elsewhere.
- Template 8, included with result set to `remains_open` unless gate closure is already documented.

For script-sensitive lanes, include Template 6.

For reviewer-bound lanes, include Template 4.

For novel Session D streams, use Template 7 and keep the status line `non-canonical/research-only`.
