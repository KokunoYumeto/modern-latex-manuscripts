# Accepted correction ledger template - 2026-06-29

This artifact defines the shared correction-ledger structure for review-return ingestion across the Noether multilingual canonical-edition workflow.

It is an empty template, not a ledger of accepted corrections. It does not imply that any reviewer has accepted any term, sentence, theorem rendering, script sidecar, or translation.

Companion machine-readable file: `ACCEPTED_CORRECTION_LEDGER_TEMPLATE_20260629.json`

## Purpose

Reviewer returns need to be ingested in a way that connects language authority to artifact versioning. A correction is accepted only when it has a reviewer decision, a scoped rationale, the affected artifact hash, an update target, and a validation path.

This ledger template connects:

- Review packet responses.
- Term governance states.
- TeX/source edits.
- Glossary and rationale updates.
- Visual inspection notes.
- Render/build validation.
- Manifest and handoff updates.

## Correction States

| State | Meaning |
| --- | --- |
| `submitted` | Reviewer returned a suggestion, question, or concern. |
| `triaged` | Project maintainer classified the return and assigned an owner/action. |
| `accepted_pending_edit` | Correction is accepted but not yet applied to artifacts. |
| `accepted_pending_rebuild` | Correction is applied but TeX/PDF or sidecar rebuild is not validated. |
| `accepted_rebuilt` | Correction is applied and rebuild/render validation passed. |
| `accepted_manifested` | Correction is applied, rebuilt, and recorded in manifest/handoff artifacts. |
| `rejected` | Correction is rejected with rationale. |
| `needs_reviewer_clarification` | Reviewer intent or authority scope is unclear. |
| `blocked` | Correction cannot be resolved without missing source, review, tooling, or policy evidence. |
| `superseded` | Later correction replaces this one. |

## Severity Levels

| Severity | Meaning |
| --- | --- |
| `blocker` | Mathematical meaning, language authority, render integrity, or artifact reproducibility is compromised. |
| `major` | Important terminology, idiom, structure, or layout issue but not immediately blocking all use. |
| `minor` | Local wording, style, punctuation, or presentation issue. |
| `note` | Reviewer comment without required change. |

## Issue Types

- `mathematical_correctness`
- `terminology`
- `native_idiom`
- `educational_register`
- `script_sidecar`
- `rtl_or_cjk_rendering`
- `tex_build`
- `pdf_visual`
- `source_evidence`
- `license_or_provenance`
- `manifest_or_handoff`
- `interlanguage_authority`
- `constructed_pilot_boundary`

## Required Ledger Fields

| Field | Purpose |
| --- | --- |
| `correction_id` | Stable ID, for example `corr-20260629-zh-0001`. |
| `review_packet_id` | Packet that produced the return. |
| `language_lane` | Lane or family, such as `simplified_chinese`, `french`, `fa_IR`, or `interslavic`. |
| `sublane_or_script` | Script/register when relevant. |
| `reviewer_role` | Authority role, not private identity unless approved for publication. |
| `review_date` | Date of reviewer return. |
| `artifact_hash_reviewed` | Hash of the reviewed artifact. |
| `source_artifact` | TeX/PDF/glossary/manifest/review packet file under review. |
| `location` | File/line, PDF page, section, theorem, term ID, or glossary row. |
| `issue_type` | Type from the issue list above. |
| `severity` | Severity from the severity table above. |
| `current_text_or_term` | Existing text/term, if short enough to record. |
| `recommended_change` | Reviewer recommendation. |
| `mathematical_concept` | Concept affected, if terminology or mathematical meaning is involved. |
| `term_id` | Term-governance ID if applicable. |
| `term_record_type` | Term record type before or after correction. |
| `decision_state` | Term/correction decision state. |
| `source_or_reason` | Reviewer evidence, source witness, or rationale. |
| `maintainer_decision` | Accepted, rejected, clarification requested, blocked, or superseded. |
| `files_to_update` | Explicit file list. |
| `rebuild_required` | Whether TeX/PDF/script-sidecar rebuild is required. |
| `validation_required` | Required checks after edit. |
| `manifest_update_required` | Whether manifest/index/handoff must change. |
| `follow_up_owner` | Person, role, or queue responsible for next action. |

## Ingestion Checklist

1. Confirm reviewer role and scope.
2. Confirm artifact hash reviewed.
3. Classify issue type and severity.
4. Link to term-governance record when terminology is involved.
5. Decide accepted/rejected/clarification/blocked/superseded.
6. Apply accepted edits to TeX/glossary/rationale/source manifest as needed.
7. Rebuild and visually inspect PDFs/sidecars where required.
8. Run local validators.
9. Update manifest/index and handoff pointers.
10. Preserve rejected or blocked decisions with rationale.

## Lane-Specific Notes

| Lane | Extra ingestion rule |
| --- | --- |
| Slavic sidecars | A correction touching Interslavic/Panslavic text may require Latin and Cyrillic updates plus sidecar validation. |
| Simplified Chinese | CJK line breaking and formula association must be visually checked after accepted prose edits. |
| French/Spanish | Regional variants should be recorded as variants when valid, not flattened into errors. |
| Japanese | Script mix, particles, and formula punctuation need visual inspection after edits. |
| Persian-family | `fa_IR`, `prs_AF`, and `tg_Cyrl_TJ` corrections must not transfer across sublanes without explicit authority. |
| Arabic | RTL directionality, punctuation, and formula embedding require visual checks after accepted edits. |
| Interlanguage/constructed pilot | A language-community or project-authority correction is distinct from a mathematical-register correction. |

## Empty Ledger Seed

No accepted corrections are recorded by this template. The initial machine-readable ledger contains an empty `correction_records` array.

## Immediate Next Gates

- Create lane-specific ledger files when actual reviewer packets are emitted.
- Connect accepted correction IDs to future TeX/PDF rebuild manifests.
- Promote reviewer-approved terms into the terminology governance matrix only within their reviewed scope.
