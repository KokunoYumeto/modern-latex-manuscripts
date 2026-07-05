# Noether R7 Exact Source Acquisition and Route Queue

Generated: 2026-07-04

Status: `exact_source_acquisition_route_queue_no_translation_promotion_no_review_claim_no_git_push`

This continuation converts the existing Brunei/Singapore exact-content refresh, Singapore ATL title check, Malay-Indonesian review-packet baseline, and SEA/Pacific pass2 source records into a concrete acquisition and routing queue. It does not approve terms, draft bridges, claim native review, or treat title-only/comparator-only material as translation evidence.

## Gate Rule

A source can route into translation-support work only when it has:

1. exact content, not only a title/listing;
2. matching scope for the target lane;
3. mathematical terminology or proof prose appropriate to the row;
4. non-comparator status, unless a separate governance/adoption gate closes.

Everything else remains a source-return, source-pointer, query-seed, or blocker row.

## Malay-Indonesian Review-Packet Baseline

The review bundle remains the Malay-Indonesian baseline:

- Bundle zip: `review_bundles/Malay_Indonesian_Review_Packet_Bundle_20260629T050303Z.zip`
- Bundle SHA-256: `3ED035C9DAE2681D7206C346A73CD9AE458E3DCD784D568E321D957C65355823`
- Status: `review_packet_bundle_v0_1_no_pilot`
- Valid next artifact: returned-review ingestion or reviewer-response status ledger.

Route now: reviewer/source prompt only. No translated Noether passage is authorized.

## Brunei/Singapore Exact-Content Queue

| Source id | Status | Route now | Next action |
| --- | --- | --- | --- |
| `brunei_dbp_mabbim_institutional_page` | Download failed on SSL hostname mismatch. | Official route blocker. | Retry with browser/manual TLS handling or alternate DBP/MABBIM item URL; exact math content still absent. |
| `brunei_moe_curriculum_development_department` | Downloaded official Brunei MOE curriculum page. | Context route. | Search within MOE for item-level Malay mathematics textbook/syllabus terminology. |
| `brunei_moe_spn21_english` | Downloaded official SPN21 English PDF. | Medium/curriculum context only. | Do not use for Malay algebra/proof terms. |
| `brunei_moe_spn21_malay` | Downloaded official SPN21 Malay PDF. | General Malay curriculum context only. | Needs explicit math terminology extraction before any stronger use. |
| `singapore_moe_approved_textbook_list` | Downloaded official Singapore MOE ATL route. | Source route. | Continue only if current ATL rows expose Malay+mathematics item content. |
| `singapore_seab_2027_sec_g3_syllabuses` | Downloaded official SEAB syllabus route. | Separate subject context. | Not Malay math terminology. |
| `singapore_seab_gce_o_school_candidates` | Downloaded official GCE O-Level route. | Assessment context. | Not Malay math terminology. |
| `singapore_seab_ast_workshops` | Downloaded official training route. | Separate subject context. | Not Malay math terminology. |
| `malaysia_dbp_prpm_istilah_mabbim_math_sample` | Downloaded PRPM/MABBIM Malaysia comparator. | Comparator/query seed only. | Scope-governance/adoption gate required before reuse. |

Singapore ATL current-title check:

- Primary: 544 parsed rows, 30 math rows, 81 Malay rows, 0 overlap.
- Secondary: 506 parsed rows, 72 math rows, 112 Malay rows, 0 overlap.
- Route now: title-watch only, no translation support.

## SEA/Pacific Acquisition Queue

| Row | Source state | Route now | Next action |
| --- | --- | --- | --- |
| Filipino/Tagalog | Two glossary PDFs downloaded. | Glossary/source-pointer only. | Find native-country higher algebra/proof source. |
| Cebuano | Two DepEd lower-math landing pages downloaded. | Lower-math locator. | Item detail/PDF capture and higher math source discovery. |
| Ilokano | Math instruction context page downloaded. | Context/source locator. | Direct Ilokano math/STEM source. |
| Hiligaynon | DepEd math listing downloaded; item detail not captured. | Item-detail target. | Capture item page/PDF and inspect text. |
| Waray | Math-medium context PDF downloaded. | Context only. | Direct Waray math/STEM material. |
| Bikol | DepEd language material page downloaded. | Language context only. | Direct Bikol math/STEM material. |
| Lao | JICA official primary math page and Learning Passport course page downloaded. | Official primary source route and refresh target. | Extract/download item PDFs/course content; still not higher-algebra proof prose. |
| Shan | Language textbook context page downloaded. | Source locator only. | Direct Shan math/STEM source. |
| Zhuang | Search gap row; no download. | Gap/retry row. | Direct Zhuang math/STEM source discovery. |
| Hmong/Miao | Grade 4 glossary PDF downloaded; Grade 10 glossary blocked 403. | Glossary/source-pointer and failed-retry row. | Local/curriculum source beyond US testing glossary. |
| Mien/Yao | Language resource context downloaded. | Context only. | Direct Mien/Yao math/STEM source. |
| Khmer | Third-party Khmer math book page downloaded; terms PDF failed certificate check. | Noncanonical discovery lead. | Official/university proof source or validated exact text. |
| Mon | Language context page downloaded. | Context only. | Direct Mon math/STEM source. |
| Santali/Munda | Bharatavani Santali textbook listing downloaded. | Item-detail/PDF target. | Capture item-level text/PDF; title-only until then. |

## Interlanguage Routing Decision

No matching interlanguage evidence is routed onward in this pass because no new source-gated direct evidence closed. No novel/unmatched material is absorbed into Session G. Any future cross-family or ownerless construction must remain separate and route to the novel lane with its source/blocker evidence.

## No-Promotion State

- Accepted terms: 0.
- Draft bridge promotions: 0.
- Native/community/reviewer approval claims: 0.
- Title-only rows used as translation support: 0.
- Comparator-only rows used as translation support: 0.
- Git pushes: 0.

