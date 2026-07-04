# Noether Source-Evidence and Authority Minimum Templates V3

Generated: 2026-07-04

Status: reusable minimum templates for routed child lanes and NOVEL/OWNERLESS Session D packets. These templates are intentionally non-promotional.

## Minimum Source-Evidence Manifest

```text
Manifest ID:
Generated:
Receiving owner:
Route ID:
Stream:

Evidence state:
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

Source rows:
| source_id | language_or_standard | script | source_type | path_or_url | local_hash | page_or_section_anchor | license_state | extraction_state | allowed_use | forbidden_use |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| S001 |  |  |  |  |  |  |  |  | source evidence only | term approval or community consent |

Rejected candidates:
| candidate_id | path_or_url | reason_rejected | preserved_for_audit |
| --- | --- | --- | --- |

Boundary:
This source manifest supports only the claim explicitly stated in the lane handoff card.
```

## Minimum Authority Decision Record

```text
ADR ID:
Generated:
Receiving owner:
Route ID:
Decision subject:

Decision:
- route_to_existing_lane
- keep_as_NOVEL_OWNERLESS_research_only
- comparator_only
- defer_source_gap
- reject_as_authority
- prepare_reviewer_packet

Authority claim evaluated:
- mechanical
- evidential
- pedagogical
- community
- canonical_edition

Highest supported claim:

Evidence considered:
| artifact | status | limitation |
| --- | --- | --- |

Required before stronger claim:
- native/near-native reviewer:
- domain mathematician:
- teacher/learner reviewer:
- language project/community authority:
- script/orthography authority:

Allows:

Forbids:

Rollback/rejection path:

Gate result:
remains_open
```

## Minimum Term-Governance Matrix

```text
Matrix ID:
Generated:
Receiving owner:
Route ID:

| row_id | concept_id | source_definition | observed_anchor_status | project_usage_field | reviewer_needed | rejected_alternatives | approval_state |
| --- | --- | --- | --- | --- | --- | --- | --- |
| T001 |  |  | source_gap | blank_until_authorized | native/domain |  | not_approved |
```

Allowed approval states:

- not_approved
- source_gap
- observed_anchor_needs_review
- source_backed_seed_not_approved
- rejected_candidate
- accepted_by_reviewer_not_yet_ingested
- approved_after_gate_closure

Invariant:

`approved_after_gate_closure` is forbidden unless a separate child-lane gate record identifies the reviewer/source closure and accepted-correction ingestion.

## Minimum Reviewer Return Ingestion Stub

```text
Return ID:
Generated:
Receiving owner:
Route ID:
Reviewer role:
Reviewer identity policy:

Return received:
- yes
- no

If yes:
- date:
- permission_to_cite:
- authority_scope:
- accepted_corrections_count:
- rejected_items_count:
- unresolved_questions_count:

Ingestion result:
- no_return
- return_received_not_ingested
- ingested_for_mechanical_note_only
- ingested_for_evidential_note_only
- ingested_for_term_review_not_approval
- ingested_for_gate_closure

Boundary:
One reviewer return does not imply community consent unless the reviewer explicitly has and states that authority.
```

## Minimum Gate-Closure Checklist

```text
Gate ID:
Generated:
Receiving owner:
Route ID:

Required:
- source shelf complete:
- source anchors verified:
- local hashes recorded:
- rejected candidates logged:
- OCR/script risks logged:
- render/visual checks complete, if applicable:
- reviewer packet sent:
- reviewer return received:
- accepted-correction ledger ingested:
- authority scope recorded:
- rollback/rejection path recorded:

Result:
- remains_open
- closed_for_mechanical_claim_only
- closed_for_evidential_claim_only
- closed_for_reviewer_packet_readiness
- closed_for_review_ready_edition

Claims still forbidden:
```
