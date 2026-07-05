# Noether Persianate/Tajik Source-Sufficiency Translation Transition Draft

Generated: 2026-07-05

Status: draft/non-canonical source-sufficiency and translation-review transition sidecar. Not native reviewed. Not accepted terminology. Not canonical approval. Not gate promotion. Not license clearance. Not translation completion. Language lanes do not push.

## Instruction Basis

Read and applied:

- `AGENTS.md` at branch `codex/noether-pc-20260629`, including the source-canon sufficiency transition.
- `.github/copilot-instructions.md`, including the rule that covered rows should move to draft review work once adequate source witnesses exist.
- `NOETHER_SOURCE_CANON_SUFFICIENCY_TRANSLATION_TRANSITION_20260705.md` at commit `b99286628344251e860fe889e44cc54c8ebd6f87`.
- Local steering/source-canon records and the Persianate/Tajik witness table current through the 2026-07-05 TNU Tajik ideal pass.

This packet does not replace `NOETHER_FA_IR_DRAFT_ROW_GLOSSARY_AND_SOURCE_NOTES_20260704.md`, `NOETHER_PRS_AF_DRAFT_ROW_GLOSSARY_AND_SOURCE_NOTES_20260704.md`, or the full corpus draft. It is a transition map from source-canon sufficiency into scoped row-review work.

## Sufficiency Decision By Sublane

| Sublane | Current baseline sufficiency | Covered draft work now responsible | Still uncovered/gap |
| --- | --- | --- | --- |
| `fa_IR` Persian/Farsi (Iran) | Sufficient for draft review on the 22 active algebra/ring/module/field/Galois-adjacent rows. Witnesses include IUT advanced algebra, PNU ring/module, Shahrood noncommutative prime ideals, KNTU foundations, IUT field/Galois curriculum, UI Auslander-Reiten/Gorenstein article, and two Persian TeX/XePersian linear-algebra source archives. | Carry target renderings, source-context notes, term alternatives, and formula-neighboring notes for all 22 rows. Manual rows remain draft/manual, not approved. | No exact Persian Noether/invariant-theory TeX source package; class-field-theory PDF candidates partly access-gated; manual page-extraction rows still need reviewer/RTL confirmation. |
| `prs_AF` Dari/Persian (Afghanistan) | Sufficient for scoped draft review on the 4 active rows at review-material level. Witnesses include Momand/eCampus algebra, Kabul University discrete math, eCampus 369 list, KNU OPAC records, and MoHE/eCampus curriculum bibliography. | Carry target renderings and Afghan/Dari register notes for algebra, field, simple, ring. Algebra is the only ready row; field/simple/ring remain manual/source-review. | No direct Dari invariant-theory witness; no Dari TeX/source archive; KNU `8809.PDF` route unresolved; Iranian Persian witnesses remain comparator only. |
| `tg_Cyrl_TJ` Tajik Cyrillic | Sufficient for source-discovery scaffolds only, not row translation. Stronger witnesses now include Tajik Wikipedia linear algebra, Shukurov/Tabarov linear algebra/invariant context, TNU ideal/algebraic-number-field article context, OER algebra/number theory, Zarowadk algebra/number-theory texts, and KTM course complex. | Maintain tentative non-row lexical/interlanguage notes such as `алгебра`, `ҳалқа`, `майдон`, `идеал`, `гомоморфизм`, `назарияи инвариантҳо`. | Original queue has zero promoted Tajik term rows. No Tajik TeX/source archive or reviewer-promoted term-anchor row. Do not turn source-discovery notes into term rows. |

## fa_IR Covered Row Draft Review Table

All renderings below are review material only. Source support means "candidate backed by provenance rows", not approval.

| Term ID | Concept | Draft fa_IR rendering | Alternatives/register flags | Formula-neighboring usage note | Source-context note |
| --- | --- | --- | --- | --- | --- |
| `term-fa-ir-0001` | algebra | جبر | Stable broad term; avoid using it to cover structure words that need `ساختار جبری`. | `جبر A` for an algebra; `جبرها` in plural prose needs reviewer style check. | Broadly supported by IUT, KNTU, Shahrood, UI, and Persian TeX linear-algebra witnesses. |
| `term-fa-ir-0002` | field | میدان | In physics contexts `میدان` is ambiguous; formula-adjacent algebraic context must carry the mathematical cue. | `میدان K`, `توسیع میدان L/K`, `میدان متناهی`. | IUT Galois curriculum strongly supports field-extension context; KNTU/IUT algebra also support. |
| `term-fa-ir-0003` | Artinian | آرتینی | Possible adjective inflection/ezafe behavior needs reviewer confirmation. | `حلقه آرتینی`, `مدول آرتینی`. | PNU/Shahrood source evidence; draft only. |
| `term-fa-ir-0004` | submodule | زیرمدول | Manual row due exact-page extraction failure; alternative spacing `زیر مدول` should be checked. | `N زیرمدولی از M است`; formula `N \subseteq M` should not force a different word. | Seed evidence strong but queue says manual/RTL extraction review still needed. |
| `term-fa-ir-0005` | tensor product | ضرب تانسوری | Alternative `حاصل‌ضرب تانسوری` likely in broader Persian math; source row currently uses `ضرب تانسوری`. | `M \otimes_R N` -> `ضرب تانسوری M و N روی R`. | Keep manual until extraction/register check confirms phrase. |
| `term-fa-ir-0006` | module | مدول | Stable loanword in algebra; manual only because exact-page recheck failed. | `مدول M روی حلقه R`; `R`-module prose may need `مدول روی R`. | High seed counts across algebra/ring witnesses; still manual in queue. |
| `term-fa-ir-0007` | free module | مدول آزاد | Check whether prose prefers `مدول آزاد روی R`. | `R^n` as `مدول آزاد` if context is module over ring. | Source-seeded; exact-page recheck unresolved. |
| `term-fa-ir-0008` | right module | مدول راست | Keep independent from left-module row. | `مدول راست روی R`; order matters around noncommutative rings. | One exact recheck plus broader seed evidence. |
| `term-fa-ir-0009` | left module | مدول چپ | Do not infer from right-module readiness. | `مدول چپ روی R`; useful near operator/order conventions. | Manual/source-review row. |
| `term-fa-ir-0010` | automorphism | خودریختی | Compare with `اتومورفیسم` only if source reviewer requests. | `خودریختی \sigma` of a ring/field/group. | Shahrood is current primary source witness. |
| `term-fa-ir-0011` | homomorphism | همریختی | Stable algebraic morphism candidate; check category-specific scope. | `همریختی f: A \to B`. | KNTU/IUT/Shahrood support. |
| `term-fa-ir-0012` | isomorphism | یکریختی | Keep separate from homomorphism and automorphism. | `یکریختی A \cong B`; `تا یکریختی`. | PNU/Shahrood support; ready context note. |
| `term-fa-ir-0013` | Noetherian | نوتری | High-value manual row; possible `نوتر`/`نوتریان` alternatives should not be guessed. | `حلقه نوتری`, `مدول نوتری`; adjective placement needs reviewer check. | UI article adds clean `نوتری` metadata; exact row remains manual. |
| `term-fa-ir-0014` | simple | ساده | Broad common word; formula context must specify module/representation/algebra sense. | `مدول ساده`, `نمایش ساده`, `حلقه ساده`. | Ready row but register-specific. |
| `term-fa-ir-0015` | representation | نمایش | Broad word; `نظریه نمایش` supported in UI article context. | `نمایش \rho: G \to GL(V)`. | Manual row due sense breadth and extraction limits. |
| `term-fa-ir-0016` | semisimple | نیم‌ساده | ZWNJ/hyphen style must be reviewer-confirmed. | `مدول نیم‌ساده`, `جبر نیم‌ساده`, `نمایش نیم‌ساده`. | Ready row with low exact count; keep caution visible. |
| `term-fa-ir-0017` | ideal | ایده‌آل | Alternative spelling `ایدئال`; source files show RTL/normalization risk. | `ایده‌آل I در R`, `I \triangleleft R`. | Strong seed evidence and Shahrood/PNU/KNTU context, but row remains manual. |
| `term-fa-ir-0018` | prime ideal | ایده‌آل اول | Alternative `ایدئال اول`; avoid literal "first" ambiguity in notes. | `ایده‌آل اول \mathfrak p`. | Manual row; source support exists but exact review pending. |
| `term-fa-ir-0019` | maximal ideal | ایده‌آل ماکسیمال | Alternative `ایده‌آل بیشینه` should be checked; current seed uses max/maximal loan register. | `ایده‌آل ماکسیمال \mathfrak m`. | Manual row; reviewer should decide local register. |
| `term-fa-ir-0020` | ring | حلقه | Strongest fa_IR ring anchor. | `حلقه R`, `حلقه واحددار` if unit matters. | Ready row with high exact hits. |
| `term-fa-ir-0021` | commutative ring | حلقه جابجایی | Alternative `حلقه جابه‌جایی`/ZWNJ spelling should be checked. | `حلقه جابجایی R`; near formulas with `ab=ba`. | Ready row, spelling/register still reviewable. |
| `term-fa-ir-0022` | noncommutative ring | حلقه ناجابجایی | Alternative with ZWNJ `ناجابجایی`/`ناجابه‌جایی` needs style review. | `حلقه ناجابجایی R`; important around left/right modules. | Ready row with lower count; keep source count visible. |

## prs_AF Covered Row Draft Review Table

Dari/Afghan Persian evidence must stand on its own. Matching surfaces with fa_IR are not cross-authorization.

| Term ID | Concept | Draft prs_AF rendering | Alternatives/register flags | Formula-neighboring usage note | Source-context note |
| --- | --- | --- | --- | --- | --- |
| `term-prs-af-0001` | algebra | جبر | Ready row. Surface matches fa_IR, but evidence is Afghan Momand/eCampus. | `جبر A`; in course prose, keep Afghan punctuation/spacing from source context. | Momand algebra gives direct support; eCampus/MoHE sources add bibliography context. |
| `term-prs-af-0002` | field | میدان | Manual row; do not borrow fa_IR Galois usage. | `میدان K`; flag algebraic-field sense for Dari reviewer. | Momand seed exists; exact page recheck failed. |
| `term-prs-af-0003` | simple | ساده | Low-count manual row; broad common word. | `مدول ساده` or `گروپ ساده` only if local source context supports the object. | Needs Dari technical reviewer; fa_IR representation usage is comparator only. |
| `term-prs-af-0004` | ring | حلقه | Manual row; source text also has high `رينگ` counts, so `حلقه` vs `رینگ/رينگ` needs review. | `حلقه R`; for classroom notes, record if source uses `رينگ` in definitions. | Momand/eCampus algebra is direct Afghan witness; not source-closed for approval. |

## Interlanguage/Script Scaffolds For Review

These scaffolds help reviewers compare registers. They are not bridges, promotions, or approvals.

| Concept | German/English anchor | fa_IR draft | prs_AF draft | tg_Cyrl_TJ non-promoted note | Boundary |
| --- | --- | --- | --- | --- | --- |
| ring | `Ring`, ring | حلقه | حلقه / review `رينگ` source variant | ҳалқа | Tajik is source-discovery only; Afghan variant must be reviewer-set. |
| field | `Körper`, field | میدان | میدان | майдон | Tajik `майдон` remains high-risk non-row. |
| ideal | `Ideal`, ideal | ایده‌آل | no active prs_AF row | идеал | TNU supports Tajik source-discovery, not row promotion. |
| Galois theory | `Galoistheorie`, Galois theory | نظریه گالوا | no active prs_AF row | open / source-discovery not row-backed | fa_IR IUT curriculum supports source routing; no prs_AF/Tajik row. |
| homomorphism | `Homomorphismus`, homomorphism | همریختی | no active prs_AF row | гомоморфизм | Tajik source-discovery only. |
| representation | `Darstellung`, representation | نمایش | no active prs_AF row | намойиш / review spelling | fa_IR manual row; Tajik not promoted. |
| linear algebra | `lineare Algebra`, linear algebra | جبر خطی | الجبر خطی / جبر خطی in Afghan bibliography | алгебраи хаттӣ | Strong source routing in all three, but no automatic term approval. |

## Covered vs Gap Routing

Covered for draft review now:

- `fa_IR`: all 22 active rows may carry draft renderings and source-context notes as review material. Ten rows stay manual/source-review and must not be represented as resolved.
- `prs_AF`: all 4 active rows may carry draft renderings and source-context notes as review material. Only `algebra` is ready; `field`, `simple`, and `ring` stay manual/source-review.
- `tg_Cyrl_TJ`: no term rows are covered because the queue has zero promoted Tajik rows. Source-discovery notes and non-row scaffolds are allowed.

Still in source acquisition/gap status:

- Exact target-language Noether/invariant-theory TeX/source packages for `fa_IR`, `prs_AF`, and `tg_Cyrl_TJ`.
- Direct Dari/Afghan Persian invariant-theory source.
- Tajik promoted term rows and Tajik Noether-specific source package.
- Any license-clearance or redistribution decision for public PDFs.

## Gate Statement

Reviewer packet population: false. Native review: false. Accepted terminology: false. Canonical approval: false. Gate promotion: false. Translation completion claim: false. License clearance: false. Tajik term rows created: 0. Git push: false.
