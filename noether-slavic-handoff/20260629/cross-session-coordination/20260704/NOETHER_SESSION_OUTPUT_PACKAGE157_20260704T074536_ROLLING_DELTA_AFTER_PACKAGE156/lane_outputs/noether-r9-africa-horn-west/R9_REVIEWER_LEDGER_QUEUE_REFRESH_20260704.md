# R9 Reviewer Ledger Queue Refresh

Generated: 2026-07-04

Lane: Session H - Africa/Horn/West Africa source-return.

Purpose: refresh the reviewer/source-return queue after the Amharic and Tigrigna/Tigrinya OCR continuations. This artifact keeps the queue source-gated: usable evidence can support non-canonical reviewer/corpus work only after source/OCR/licensing checks; blocked rows remain blockers.

## Boundary

- No accepted term ledger.
- No pilot or readiness claim.
- No native/community-review claim.
- No license approval.
- No Git push, upload, or package publication.
- Every row in the companion CSV has `promotion_allowed=false`.

## Refreshed Queue

| Queue | Lane | Source gate | Current status | Required return |
| --- | --- | --- | --- | --- |
| R9-RL-001 | Hausa | content and license return | SS1/SS2 Hausa math metadata exists, but local content and reuse status remain absent. | Source owner or reviewer return with content availability, license note, exact wording, and remaining blockers. |
| R9-RL-002 | Igbo | content and license return | Basic Igbo math/textbook route exists, but local source-cleared text is absent. | Source-cleared textbook/glossary text or named reviewer return. |
| R9-RL-003 | Amharic | OCR/font-map repair | Rows 001 and 025 visibly contain Ethiopic/Amharic pages but unusable or empty text layers; rows 045/048 are best clean-text audit candidates. | OCR/font specialist return with corrected Unicode and page-level reviewer verification. |
| R9-RL-004 | Afar | transcript and permission return | Qafar/Afar math media leads exist as metadata/context only; no transcript or direct wording is cleared. | Transcript, source permission status, and reviewer/source-owner decision. |
| R9-RL-005 | Somali | proof/register and attribution return | Latin source extraction supports school-STEM source work, but proof-language and reuse/attribution remain open. | Reviewer alternatives for definition/theorem/proof frames plus source permission/attribution status. |
| R9-RL-006 | Oromo | orthography and proof return | Latin extraction is usable, but apostrophe/source spelling and proof sentence frames need page/reviewer verification. | Page-image verification of spelling plus reviewer decision on proof/definition frames. |
| R9-RL-007 | Tigrigna/Tigrinya | script OCR and label return | Rows 004/007 are small clean-text candidates; row 003 is ASCII-heavy/noisy; weak rows need OCR/transcription. | Render/text comparison, script label decision, and reviewer verification before any corpus prompt. |
| R9-RL-008 | Fulfulde/Fulani | variety return | Glossary rows are useful prompts, but Fulfulde/Fulani/Fula/Pulaar variety labels remain unresolved. | Variety label, preferred form, rejected form, and source rationale. |
| R9-RL-009 | Mandinka/Manding | scope return | Mandinka-specific source rows exist; Manding-wide extension is not authorized. | Mandinka-specific reviewer return and explicit Manding scope note. |
| R9-RL-010 | Akan/Twi | scope return | Twi source rows exist; Akan-wide bridge remains context-only. | Twi decision and separate Akan-scope decision if available. |
| R9-RL-011 | Wolof | register return | Glossary rows exist across math/science; variants and proof-language register remain open. | Chosen form, rejected variants, and proof/register note. |
| R9-RL-012 | Yoruba | source-type and extraction return | Dictionary-seed rows exist; school/STEM prose and damaged extraction checks remain open. | Rendered-page check, school/STEM witness, and reviewer decision. |
| R9-RL-013 | AF-05 South Sudan | reviewer/authority return | Dinka/Nuer/Zande packet is only a starter/control checklist. | Named reviewer/authority, orthography/dialect label, local wording, and decision. |
| R9-RL-014 | AF-06 Omotic/southern non-Bantu | transcription and font return | Khoekhoegowab/Juhoansi anchors need exact labels, click/ejective notation checks, and reviewer/source-font confirmation. | Source page, exact local label, transcription status, and reviewer return. |

## Routing Rule

Somali, Oromo, Tigrigna/Tigrinya, Fulfulde/Fulani, Mandinka/Manding, Akan/Twi, Wolof, and Yoruba can remain in non-canonical corpus-support lanes only where the cited source row is usable and the reviewer question is explicit. Hausa, Igbo, Amharic, Afar, AF-05, and AF-06 remain source/OCR/licensing/reviewer blocked unless the required return fields are supplied. Cross-family or novel constructions without a source-community owner must be routed to Session D, not accepted inside R9.
