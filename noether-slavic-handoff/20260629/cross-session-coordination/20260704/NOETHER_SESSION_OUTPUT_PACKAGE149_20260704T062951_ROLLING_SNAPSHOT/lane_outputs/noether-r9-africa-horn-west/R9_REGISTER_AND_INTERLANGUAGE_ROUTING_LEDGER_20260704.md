# R9 Register and Interlanguage Routing Ledger

Generated: 2026-07-04

Purpose: decide when register construction belongs inside Session H and when it should be routed to Session D as novel interlanguage work.

## Boundary

This ledger does not authorize any accepted bridge, constructed register, pilot, or public-facing translation. It is a routing artifact only.

## Routing Rules

| Case | Session H owns? | Route |
| --- | --- | --- |
| Language-specific source-backed draft support for Somali, Oromo, Tigrigna/Tigrinya, Fulfulde/Fulani, Mandinka, Twi, Wolof, Yoruba, Hausa, Igbo, Amharic, Afar | yes | Keep in R9 source-evidence lane with `promotion_allowed=false` |
| OCR/Unicode repair for Amharic, Tigrigna/Tigrinya, Yoruba diacritics, Oromo apostrophes, Fulfulde/Wolof/Twi letters, Khoekhoegowab/Juhoansi click/ejective transcription | yes | Keep in R9 OCR/source-return lane |
| Reviewer-ledger questions for named local source communities/languages | yes | Keep in R9 reviewer-ledger queue |
| Pan-West-African, pan-Horn, pan-Cushitic, Ethiopian-Semitic, Manding-wide, Akan-wide, Wolof/Senegambian, pan-Omotic, Khoe/Tuu/Kx'a, or composite African technical register | no, unless a named source community supplies authority later | Route to Session D as novel/interlanguage-governance work |
| Cross-family constructed bridge with no owner and no reviewer route | no | Route to Session D as novel; do not draft surfaces in R9 |
| OER translation packet planning before term/reviewer/license gates close | no | Keep as blocked packet route; if method/governance questions arise, route those to Session D |

## Per-Lane Decision

| Lane | Register construction status | Owner | Session H action |
| --- | --- | --- | --- |
| Somali | local school-STEM register support exists, proof register open | Somali row only | Build reviewer questions and source-form support; no Somali-Oromo bridge |
| Oromo | local school-STEM register support exists, orthography/proof register open | Oromo row only | Build reviewer questions and source-form support; no Cushitic bridge |
| Tigrigna/Tigrinya | script-aware support exists, algebra extraction blocker open | Tigrigna/Tigrinya row only | Repair font/OCR and ask script/register questions; no Ethiopian-Semitic bridge |
| Fulfulde/Fulani | variant-aware glossary support exists | variety-labeled Fulfulde/Fulani/Fula/Pulaar rows only | Keep variants as columns; no collapsed register |
| Mandinka/Manding | Mandinka-specific glossary support exists | Mandinka row only | Keep Manding-wide questions blocked |
| Akan/Twi | Twi glossary support exists, Akan context separate | Twi row only unless separate Akan authority appears | Keep Akan-wide bridge blocked |
| Wolof | Wolof glossary support exists | Wolof row only | Keep variants for reviewer choice; no Senegambian bridge |
| Yoruba | dictionary support only | Yoruba dictionary/source-return row | Do not open translation lane until school/STEM source and review return |
| Hausa | metadata/source-return only | Hausa source-return row | Do not construct register; seek content/reviewer/license return |
| Igbo | metadata/context only | Igbo source-return row | Do not construct register; seek source-cleared content/reviewer return |
| Amharic | source shelf captured, extraction mostly blocked | Amharic OCR/source-return row | Repair OCR/font and ask reviewer questions; no Horn/Ethiopian bridge |
| Afar | media metadata and context only | Afar source-return row | Seek transcript/reviewer/source return; no Cushitic/Horn bridge |
| AF-05 Dinka/Nuer/Zande | reviewer packet starter only | named language rows | Keep as request/reviewer-return work only |
| AF-06 Khoekhoegowab/Juhoansi and adjacent rows | source anchors/page navigation only | named local rows | Keep exact local-label transcription and reviewer questions; no pan-Omotic or Khoe/Tuu/Kx'a bridge |

## Session D Referral Template

If a later worker finds a novel register idea with no source-community owner, create a referral with:

- `proposal_id`
- `triggering_sources`
- `affected_language_rows`
- `why_no_single_R9_owner`
- `authority_gap`
- `dominance_or_exclusion_risk`
- `recommended_session_d_question`
- `r9_boundary_note`

No Session H artifact should include invented cross-family bridge surfaces.

