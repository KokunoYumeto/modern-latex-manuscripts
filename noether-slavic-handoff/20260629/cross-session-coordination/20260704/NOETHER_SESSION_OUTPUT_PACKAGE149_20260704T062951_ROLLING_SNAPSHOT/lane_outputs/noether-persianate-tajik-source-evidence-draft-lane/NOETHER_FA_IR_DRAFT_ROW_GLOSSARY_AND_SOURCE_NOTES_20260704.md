# Noether fa_IR Draft Row Glossary And Source Notes

Generated: 2026-07-04

Status: draft, non-canonical, not native reviewed. This sidecar does not populate reviewer packets, does not resolve gate ledgers, does not approve terms, and does not authorize Persian/Farsi evidence for Dari or Tajik.

## Baseline And Scope

- Lane: `fa_IR`, Persian/Farsi (Iran).
- Active queue rows: 22.
- Ready context-note rows: 12.
- Manual/source-review rows: 10.
- German baseline used as the on-disk source spine: `C:\Users\memo_\Documents\Codex\2026-06-09\could-you-look-online-for-me\work\noether-slavic-canonical\tmp\zenodo_20836874_inspect\localcodex\Noether_R124plus_LocalCodex_PostR124_Consolidated_WebDrop_20260624\tex\cum_de_R124plus_localcodex_current_candidate_20260624.tex`.
- German anchor areas verified locally: title and aim around lines 383-408, form/modulus sequence around lines 603, 810-844, module reduction around lines 938-983 and 1116-1151, and later reduction/system sections around lines 2453-2487.

## Evidence Inputs

- Queue: `PAGE_CONTEXT_NOTE_WORKLIST_20260629.json`.
- Manual queue: `MANUAL_SOURCE_REVIEW_RESOLUTION_DECISION_QUEUE_20260630.json`.
- Page inspection readiness: `PAGE_INSPECTION_REVIEW_PACKET_READINESS_20260629.json`.
- Row seed: `PERSIAN_FAMILY_ARABIC_TERM_ANCHOR_SEED_20260629.json` from the branch/API payload shelf.
- Source split and guardrails: `ARABIC_PERSIANATE_EVIDENCE_SPLIT_INDEX_20260629T013531Z.md`, `PERSIANATE_SCRIPT_AND_STANDARD_POLICY_20260628T222119Z.md`, `ARABIC_SCRIPT_NON_ERASURE_GUARDRAIL_20260629.md`.
- Current status: `ARABIC_PERSIANATE_CURRENT_STATUS_HANDOFF_20260703T110057Z.md`.

## Primary fa_IR Source Witnesses

| Witness ID | Role | URL | Local extraction status |
| --- | --- | --- | --- |
| `fa_iut_behboodi_advanced_algebra` | Advanced algebra terminology seed | https://people.iut.ac.ir/sites/default/files/users/behboodi/course_files/advanced_algebra_dr._behboodi.pdf | 186 pages, all text-nonempty, SHA256 `B2BEDB1AA29693935B09445ED8D90910F27BDEEA7CA2F0BB5E3394F0150FDA40` |
| `fa_pnu_ring_module_book_preview` | Ring/module register, license review needed | https://press.pnu.ac.ir/book_30094.pdf | 21 pages, 20 text-nonempty, SHA256 `62FC1509AA543B70F2EFB461DA1871A3978D194DD8D79DFC480319B02702ED07` |
| `fa_shahrood_noncomm_prime_ideals` | Research register, noncommutative rings | https://shahroodut.ac.ir/fa/thesis/files/somefiles/sf_QA37.pdf | 100 pages, all text-nonempty, SHA256 `77C32EE8A31778858F2D2D05AC432661102B4E27A54ABA8BE0573DA299BFA335` |

## Draft Row Table

Counts are seed aggregate term counts unless marked as page-inspection exact counts. Page inspection status is evidence metadata only, not a reviewer decision.

| Term ID | English concept | Draft fa_IR rendering | Evidence basis | Page-inspection state | Draft note |
| --- | --- | --- | --- | --- | --- |
| `term-fa-ir-0001` | algebra | جبر | 46 seed hits across 3 fa_IR witnesses | ready, 5 exact hits reverified on 28 checked pages | Context note can say the algebra anchor is broadly attested across advanced algebra, ring/module, and noncommutative-ring witnesses. |
| `term-fa-ir-0002` | field | میدان | 58 seed hits across 3 fa_IR witnesses | ready, 11 exact hits reverified on 35 checked pages | Context note should ask reviewer to confirm algebraic field sense in Noether source contexts. |
| `term-fa-ir-0003` | Artinian | آرتینی | 24 seed hits across PNU and Shahrood witnesses | ready, 23 exact hits reverified on 15 checked pages | Use as draft finiteness-register rendering only; no native approval implied. |
| `term-fa-ir-0004` | submodule | زیرمدول | 355 seed hits across 3 fa_IR witnesses | manual, 0 exact hits reverified on 42 checked pages | Manual note: strong seed evidence exists, but local page extraction did not reverify exact form; review RTL extraction, ZWNJ/spacing, and page context before packet use. |
| `term-fa-ir-0005` | tensor product | ضرب تانسوری | 37 seed hits in IUT witness | manual, 0 exact hits reverified on 17 checked pages | Manual note: keep blocked until reviewer checks whether the expected tensor-product phrase is extraction-stable and register-appropriate. |
| `term-fa-ir-0006` | module | مدول | 1922 seed hits across 3 fa_IR witnesses | manual, 0 exact hits reverified on 51 checked pages | Manual note: high-volume seed evidence conflicts with exact-page recheck; likely extraction/normalization issue, but do not resolve without manual page review. |
| `term-fa-ir-0007` | free module | مدول آزاد | 65 seed hits across IUT and Shahrood witnesses | manual, 0 exact hits reverified on 23 checked pages | Manual note: phrase is plausible and source-seeded, but page-level confirmation failed in the queue audit. |
| `term-fa-ir-0008` | right module | مدول راست | 62 seed hits across IUT and Shahrood witnesses | ready, 1 exact hit reverified on 32 checked pages | Context note should mention one exact local recheck plus broader seed counts; reviewer should verify left/right convention. |
| `term-fa-ir-0009` | left module | مدول چپ | 354 seed hits across IUT and Shahrood witnesses | manual, 0 exact hits reverified on 22 checked pages | Manual note: do not infer from right-module readiness; left/right must be checked independently. |
| `term-fa-ir-0010` | automorphism | خودریختی | 14 seed hits in Shahrood witness | ready, 7 exact hits reverified on 7 checked pages | Context note can cite Shahrood as the current primary witness; still needs native/domain review. |
| `term-fa-ir-0011` | homomorphism | همریختی | 353 seed hits across 3 fa_IR witnesses | ready, 10 exact hits reverified on 30 checked pages | Context note should ask reviewer to confirm morphism-register scope across algebra/module settings. |
| `term-fa-ir-0012` | isomorphism | یکریختی | 34 seed hits across PNU and Shahrood witnesses | ready, 7 exact hits reverified on 14 checked pages | Context note should keep isomorphism separate from homomorphism and automorphism. |
| `term-fa-ir-0013` | Noetherian | نوتری | 303 seed hits across 3 fa_IR witnesses | manual, 0 exact hits reverified on 38 checked pages | Manual note: high-value Noether row; keep blocked until the exact Noetherian form and adjective behavior are manually checked. |
| `term-fa-ir-0014` | simple | ساده | 233 seed hits across 3 fa_IR witnesses | ready, 12 exact hits reverified on 44 checked pages | Context note should specify representation/module sense where needed; the surface is general-purpose. |
| `term-fa-ir-0015` | representation | نمایش | 108 seed hits across 3 fa_IR witnesses | manual, 0 exact hits reverified on 41 checked pages | Manual note: seed evidence exists, but representation-theory sense needs review because the surface can be broad. |
| `term-fa-ir-0016` | semisimple | نیم‌ساده | 94 seed hits across IUT and Shahrood witnesses | ready, 1 exact hit reverified on 28 checked pages | Context note should ask reviewer to confirm hyphen/ZWNJ handling and algebraic sense. |
| `term-fa-ir-0017` | ideal | ایده‌آل | 377 seed hits across 3 fa_IR witnesses | manual, 0 exact hits reverified on 41 checked pages | Manual note: strong source seed, but queue says sample pages did not reverify exact term; keep blocked pending RTL extraction review. |
| `term-fa-ir-0018` | prime ideal | ایده‌آل اول | 104 seed hits across IUT and Shahrood witnesses | manual, 0 exact hits reverified on 23 checked pages | Manual note: review whether phrase covers prime ideal, not merely first/primary wording in another register. |
| `term-fa-ir-0019` | maximal ideal | ایده‌آل ماکسیمال | 28 seed hits across IUT and Shahrood witnesses | manual, 0 exact hits reverified on 18 checked pages | Manual note: max/maximal loan-form should be explicitly checked against Persian algebra usage. |
| `term-fa-ir-0020` | ring | حلقه | 614 seed hits across 3 fa_IR witnesses | ready, 76 exact hits reverified on 58 checked pages | Context note can treat this as the strongest fa_IR ring-theory anchor in the row set. |
| `term-fa-ir-0021` | commutative ring | حلقه جابجایی | 70 seed hits across 3 fa_IR witnesses | ready, 18 exact hits reverified on 38 checked pages | Context note should ask reviewer about ZWNJ/ezafe preference if running prose needs it. |
| `term-fa-ir-0022` | noncommutative ring | حلقه ناجابجایی | 7 seed hits across IUT and Shahrood witnesses | ready, 3 exact hits reverified on 5 checked pages | Context note should keep the lower count visible and ask for reviewer confirmation. |

## Manual-Resolution Notes To Carry Forward

- `term-fa-ir-0004`, `0005`, `0006`, `0007`, `0009`, `0013`, `0015`, `0017`, `0018`, and `0019` remain manual/source-review rows in the canonical queue.
- This sidecar recommends `defer_pending_additional_source_or_ocr_review` or `resolve_to_context_note_entry_after_nonquoted_manual_note` only after a human/manual RTL extraction note is actually made.
- The draft renderings above are not approvals. They are row-facing working forms to support review.
- Iranian Persian/Farsi evidence here is not Dari/Afghan Persian authority and not Tajik Cyrillic authority.

## Gate Statement

Reviewer packet population: false. Native review: false. Term approval: false. Translation promotion: false. Canonical public edition claim: false.
