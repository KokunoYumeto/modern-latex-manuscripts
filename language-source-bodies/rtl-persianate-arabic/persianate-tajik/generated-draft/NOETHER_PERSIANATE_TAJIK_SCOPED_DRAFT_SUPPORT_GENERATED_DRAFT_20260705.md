# Noether Persianate/Tajik Active Row Buckets And Draft Support

Generated: 2026-07-05

Status: draft/non-canonical source-canon sufficiency and translation-support sidecar. Not native reviewed. Not accepted terminology. Not canonical approval. Not gate promotion. Not license clearance. Not translation completion. Language lane does not push Git.

Supersession note 2026-07-05: `PRS-MOMAND-ALG` / Algebra-Momand is reclassified as `ps_AF` Pashto-adjacent evidence and cannot authorize `prs_AF` rows. See `prs_af_stale_pashto_witness_retirement_20260705.csv` and `pretranslation_support_packet_20260705.md` in the Fable ledger block.

## Instruction Basis

Read and applied:

- `AGENTS.md` and `.github/copilot-instructions.md` on branch `codex/noether-pc-20260629`.
- `NOETHER_OPEN_MACHINE_GITHUB_COORDINATION_RULE_20260704.md` and `.json`.
- `NOETHER_SOURCE_CANON_SUFFICIENCY_TRANSLATION_TRANSITION_20260705.md`.
- Local Persianate/Tajik witness table, row glossaries, durable log, and B3/parent steering records available in this workspace.

## Bucket Definitions

- `SOURCE_CANON_INSUFFICIENT`: no responsible target-language source baseline for the active row. Output should be source acquisition/provenance/gap work only.
- `SOURCE_CANON_SUFFICIENT_FOR_SCOPED_DRAFT_WORK`: enough target-language witness evidence exists for draft review support. This does not remove manual/source-review status, does not approve terminology, and does not authorize another sublane.

## Bucket Summary

| Sublane | Active rows | Source-canon insufficient active rows | Source-canon sufficient for scoped draft work | Notes |
| --- | ---: | ---: | ---: | --- |
| `fa_IR` Persian/Farsi (Iran) | 22 | 0 | 22 | Ten rows remain manual/source-review even though source-canon baseline is sufficient for draft support. |
| `prs_AF` Dari/Persian (Afghanistan) | 4 | 4 | 0 | Prior Momand/eCampus algebra support has been retired to `ps_AF` Pashto; active Dari algebra/field/simple/ring rows need independent source acquisition before scoped row draft support. |
| `tg_Cyrl_TJ` Tajik Cyrillic | 0 promoted active term rows | 0 active rows | 0 active rows | Source-discovery scaffolds only; no Tajik term row is created or promoted. |

## Primary Witness Abbreviations

Use full witness metadata in `NOETHER_PERSIANATE_TAJIK_SOURCE_CANON_WITNESS_TABLE_20260704.md/json`. Compact source evidence for row bucketing:

| ID | Sublane | URL/local path/hash/license-access signal |
| --- | --- | --- |
| `FA-IUT-ALG` | `fa_IR` | IUT Behboodi advanced algebra PDF, URL `https://people.iut.ac.ir/sites/default/files/users/behboodi/course_files/advanced_algebra_dr._behboodi.pdf`, local `source_canon_witness_cache_20260704/fa_iut_behboodi_advanced_algebra.pdf`, SHA256 `B2BEDB1AA29693935B09445ED8D90910F27BDEEA7CA2F0BB5E3394F0150FDA40`; university-hosted PDF, no open license found. |
| `FA-PNU-RM` | `fa_IR` | PNU ring/module book preview PDF, URL `https://press.pnu.ac.ir/book_30094.pdf`, local `source_canon_witness_cache_20260704/fa_pnu_ring_module_book_30094.pdf`, SHA256 `62FC1509AA543B70F2EFB461DA1871A3978D194DD8D79DFC480319B02702ED07`; publisher preview, no open license found. |
| `FA-SHAHROOD-NC` | `fa_IR` | Shahrood noncommutative prime ideals thesis PDF, URL `https://shahroodut.ac.ir/fa/thesis/files/somefiles/sf_QA37.pdf`, local `source_canon_witness_cache_20260704/fa_shahrood_noncomm_prime_ideals_sf_QA37.pdf`, SHA256 `77C32EE8A31778858F2D2D05AC432661102B4E27A54ABA8BE0573DA299BFA335`; university thesis PDF, no open license found. |
| `FA-KNTU-ALG` | `fa_IR` | KNTU foundations of algebra course guide PDF, URL `https://kntu.ac.ir/dorsapax/userfiles/file/FoundationsofAlgebra.pdf`, local `source_canon_witness_cache_20260704/fa_kntu_foundations_of_algebra_course_guide.pdf`, SHA256 `85DF283F559FB9F81406712A12A6C164A1937E9DAAFD3C4A0AB47FDF2D49C125`; public university PDF, no open license found. |
| `FA-IUT-GAL` | `fa_IR` | IUT mathematics curriculum/Galois PDF, local `source_canon_witness_cache_20260704/fa_iut_mathematics_curriculum_field_galois_syllabus.pdf`, SHA256 `E9F77D2B8B83136980D86E3DC1CF4D70F5DD648352BA0E4DEDF150BE1D6D68C8`; public curriculum PDF, no license clearance. |
| `FA-UI-NOETH` | `fa_IR` | UI Auslander-Reiten/Gorenstein/Noetherian article PDF+HTML, page `https://math-sci.ui.ac.ir/article_26915.html`, PDF SHA256 `9F15766508A213DD273DD58E6905047B0E61A47038C472DBA5D09C379EFC8FE3`, HTML SHA256 `CD360D3B4B1AD6A065D074EC20B83D5A535ED997F182F3C1BECAA456DE3BB9BC`; page footer links CC BY 4.0 but no license clearance claimed. |
| `FA-TEX-LA` | `fa_IR` | Persian TeX/XePersian linear-algebra source archives: 3Blue1Brown ZIP SHA256 `4D93CE90754B28ECC743CE5BB1ED62F0325F99A38D52E90DECC10DD1C3FFF59C`; Gilbert Strang Persian ZIP SHA256 `1956A3821B88F2AFDA31A0DA184988DDDED44751A44E48068E6A06FCA091437B`; adjacent source-format evidence only, no license clearance. |
| `PS-MOMAND-ALG` | `ps_AF` | eCampus Afghanistan Abdullah Momand algebra PDF, URL `https://ecampus-afghanistan.org/wp-content/uploads/2021/10/Algebra-Abdullah-Momand.pdf`, package path `ps_AF/prs_af_ecampus_algebra_momand.pdf`, SHA256 `5145F1EFA0AB4275AD3CBF03C0016A3362D5D7A6EDE3444FDE512719E813D8F4`; Pashto/RTL-adjacent only, not Dari/Persian authority; no license clearance claimed. |
| `PRS-KU-DM` | `prs_AF` | Kabul University discrete mathematics PDF, URL `https://ku.edu.af/sites/default/files/2023-11/Discrete-mathematics.pdf`, PDF SHA256 `7FFE47055B54932151A862A1976D1D99AA1D30D241ED813753F6007ADD2AB3D4`, text SHA256 `3C69812198A648F1518AC47626316BC2F1C7386AA5E5D7AA7097D2A431D0A24A`; public university PDF, no open license found. |
| `PRS-KNU-LA` | `prs_AF` | KNU OPAC linear-algebra records, OPAC SHA256 `BF92AE49DE4DF72B32DD5FA36C8D447DC5B9791B229FF724373A1E1E557B46B8`, viewer SHA256 `631FFBAD8ECE45BCB10E3593831F0548D73F27AF97EC83D08A72BB624E3D4D3D`; catalog/source-routing only because PDF route unresolved. |
| `PRS-MOHE-CURR` | `prs_AF` | MoHE/eCampus curriculum PDF, URL `https://ecampus-afghanistan.org/wp-content/uploads/2023/02/Z-Curriculum-of-Inorganic-Industrial-Engineering-Department.pdf`, PDF SHA256 `B4C042861E3A91F3FBDBE6C8BC10DC21A86251C846D6F2A00A83834D4361C9B8`, text SHA256 `479D7562E7CB92D4C94EBF30FB07FE3D0E449F1970E56056D6E6BFEC74D77E6D`; official curriculum/source-routing evidence only. |
| `TG-DISCOVERY` | `tg_Cyrl_TJ` | Tajik source-discovery shelf includes Wikipedia raw, Zarowadk linear algebra and algebra/number-theory PDFs, TNU ideal/algebraic-number-field PDF, and OER/CICT algebra/number theory. These are non-row scaffolds only. |

## fa_IR Active Row Bucket Table

| Row | Concept | Bucket | Draft rendering | Source witnesses | Alternatives/register notes | Formula-neighboring usage | Interlinear/scaffold | Open acquisition or review note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `term-fa-ir-0001` | algebra | `SOURCE_CANON_SUFFICIENT_FOR_SCOPED_DRAFT_WORK` | جبر | `FA-IUT-ALG`; `FA-KNTU-ALG`; `FA-SHAHROOD-NC`; `FA-TEX-LA` | Use `ساختار جبری` when the German/English source means algebraic structure rather than an algebra object. | `جبر A`; `جبرها` in plural prose needs style review. | `Algebra -> جبر`; Tajik comparator `алгебра` remains non-row. | Ready context-note row; no source-canon gap for draft support. |
| `term-fa-ir-0002` | field | `SOURCE_CANON_SUFFICIENT_FOR_SCOPED_DRAFT_WORK` | میدان | `FA-IUT-GAL`; `FA-IUT-ALG`; `FA-KNTU-ALG` | Physics/general `میدان` ambiguity; formula context must mark algebraic field. | `میدان K`, `توسیع میدان L/K`, `میدان متناهی`. | `Körper/field -> میدان`; current Dari row requires independent source evidence and is not authorized by this fa_IR row. | Ready row; exact Noether/Galois source package still a broader acquisition gap. |
| `term-fa-ir-0003` | Artinian | `SOURCE_CANON_SUFFICIENT_FOR_SCOPED_DRAFT_WORK` | آرتینی | `FA-PNU-RM`; `FA-SHAHROOD-NC` | Adjective/ezafe behavior needs reviewer check. | `حلقه آرتینی`, `مدول آرتینی`. | `Artinian -> آرتینی`; no Tajik row. | Ready row; not approved. |
| `term-fa-ir-0004` | submodule | `SOURCE_CANON_SUFFICIENT_FOR_SCOPED_DRAFT_WORK` | زیرمدول | `FA-IUT-ALG`; `FA-PNU-RM`; `FA-SHAHROOD-NC` | Check spacing variant `زیر مدول`. | `N زیرمدولی از M است`; `N \subseteq M` should not force another term. | `submodule -> زیرمدول`; module stem `مدول`. | Manual/source-review row: exact-page recheck failed; acquire cleaner page evidence if possible. |
| `term-fa-ir-0005` | tensor product | `SOURCE_CANON_SUFFICIENT_FOR_SCOPED_DRAFT_WORK` | ضرب تانسوری | `FA-IUT-ALG`; adjacent `FA-TEX-LA` | Alternative `حاصل‌ضرب تانسوری`; reviewer to set register. | `M \otimes_R N` -> `ضرب تانسوری M و N روی R`. | `tensor product -> ضرب تانسوری`; no Dari active row. | Manual/source-review row; exact tensor phrase extraction remains blocker. |
| `term-fa-ir-0006` | module | `SOURCE_CANON_SUFFICIENT_FOR_SCOPED_DRAFT_WORK` | مدول | `FA-IUT-ALG`; `FA-PNU-RM`; `FA-SHAHROOD-NC` | Stable loanword but exact RTL normalization must be checked. | `مدول M روی حلقه R`; `R`-module -> `مدول روی R`. | `module -> مدول`; Tajik `модул` is non-promoted. | Manual/source-review row despite high seed count; extraction normalization blocker. |
| `term-fa-ir-0007` | free module | `SOURCE_CANON_SUFFICIENT_FOR_SCOPED_DRAFT_WORK` | مدول آزاد | `FA-IUT-ALG`; `FA-SHAHROOD-NC` | Check whether prose prefers `مدول آزاد روی R`. | `R^n` as `مدول آزاد` over `R` when context supplies ring. | `free module -> مدول آزاد`. | Manual/source-review row; cleaner exact page witness desired. |
| `term-fa-ir-0008` | right module | `SOURCE_CANON_SUFFICIENT_FOR_SCOPED_DRAFT_WORK` | مدول راست | `FA-IUT-ALG`; `FA-SHAHROOD-NC` | Keep independent from left-module row. | `مدول راست روی R`; order matters in noncommutative contexts. | `right module -> مدول راست`. | Ready row with low exact count; reviewer checks convention. |
| `term-fa-ir-0009` | left module | `SOURCE_CANON_SUFFICIENT_FOR_SCOPED_DRAFT_WORK` | مدول چپ | `FA-IUT-ALG`; `FA-SHAHROOD-NC` | Do not infer from right-module readiness. | `مدول چپ روی R`. | `left module -> مدول چپ`. | Manual/source-review row; exact-page confirmation still missing. |
| `term-fa-ir-0010` | automorphism | `SOURCE_CANON_SUFFICIENT_FOR_SCOPED_DRAFT_WORK` | خودریختی | `FA-SHAHROOD-NC`; `FA-KNTU-ALG` | Compare with `اتومورفیسم` only if reviewer requests. | `خودریختی \sigma` of a ring/field/group. | `automorphism -> خودریختی`. | Ready row; not approval. |
| `term-fa-ir-0011` | homomorphism | `SOURCE_CANON_SUFFICIENT_FOR_SCOPED_DRAFT_WORK` | همریختی | `FA-KNTU-ALG`; `FA-IUT-ALG`; `FA-SHAHROOD-NC` | Scope may vary by algebra/module/category context. | `همریختی f: A \to B`. | `homomorphism -> همریختی`; Tajik `гомоморфизм` non-row. | Ready row; reviewer confirms morphism register. |
| `term-fa-ir-0012` | isomorphism | `SOURCE_CANON_SUFFICIENT_FOR_SCOPED_DRAFT_WORK` | یکریختی | `FA-PNU-RM`; `FA-SHAHROOD-NC` | Keep distinct from homomorphism and automorphism. | `یکریختی A \cong B`; `تا یکریختی`. | `isomorphism -> یکریختی`. | Ready row; not approval. |
| `term-fa-ir-0013` | Noetherian | `SOURCE_CANON_SUFFICIENT_FOR_SCOPED_DRAFT_WORK` | نوتری | `FA-UI-NOETH`; `FA-PNU-RM`; `FA-SHAHROOD-NC` | Alternatives `نوتر`/`نوتریان` must not be guessed into approval. | `حلقه نوتری`, `مدول نوتری`. | `Noetherian -> نوتری`; German `noethersch` context flagged. | Manual/source-review row; high-value exact adjective behavior needs review. |
| `term-fa-ir-0014` | simple | `SOURCE_CANON_SUFFICIENT_FOR_SCOPED_DRAFT_WORK` | ساده | `FA-IUT-ALG`; `FA-PNU-RM`; `FA-SHAHROOD-NC` | Broad common word; object sense must be explicit. | `مدول ساده`, `نمایش ساده`, `حلقه ساده`. | `simple -> ساده`; current Dari row requires independent source evidence and is not authorized by this fa_IR row. | Ready row but context-sensitive. |
| `term-fa-ir-0015` | representation | `SOURCE_CANON_SUFFICIENT_FOR_SCOPED_DRAFT_WORK` | نمایش | `FA-UI-NOETH`; `FA-IUT-ALG`; `FA-SHAHROOD-NC` | Broad word; representation-theory sense needs source context. | `نمایش \rho: G \to GL(V)`. | `Darstellung/representation -> نمایش`; Tajik comparator only. | Manual/source-review row; exact sense review needed. |
| `term-fa-ir-0016` | semisimple | `SOURCE_CANON_SUFFICIENT_FOR_SCOPED_DRAFT_WORK` | نیم‌ساده | `FA-IUT-ALG`; `FA-SHAHROOD-NC` | ZWNJ/hyphen style must be reviewer-set. | `مدول نیم‌ساده`, `جبر نیم‌ساده`, `نمایش نیم‌ساده`. | `semisimple -> نیم‌ساده`. | Ready row with low exact count; keep caution visible. |
| `term-fa-ir-0017` | ideal | `SOURCE_CANON_SUFFICIENT_FOR_SCOPED_DRAFT_WORK` | ایده‌آل | `FA-SHAHROOD-NC`; `FA-PNU-RM`; `FA-KNTU-ALG` | Alternative spelling `ایدئال` possible; normalize only after review. | `ایده‌آل I در R`, `I \triangleleft R`. | `Ideal/ideal -> ایده‌آل`; Tajik `идеал` non-promoted. | Manual/source-review row; exact RTL extraction blocker. |
| `term-fa-ir-0018` | prime ideal | `SOURCE_CANON_SUFFICIENT_FOR_SCOPED_DRAFT_WORK` | ایده‌آل اول | `FA-SHAHROOD-NC`; `FA-KNTU-ALG`; `FA-IUT-ALG` | Avoid literal "first" ambiguity; prime-ideal sense must be checked. | `ایده‌آل اول \mathfrak p`. | `prime ideal -> ایده‌آل اول`. | Manual/source-review row; exact source page review needed. |
| `term-fa-ir-0019` | maximal ideal | `SOURCE_CANON_SUFFICIENT_FOR_SCOPED_DRAFT_WORK` | ایده‌آل ماکسیمال | `FA-SHAHROOD-NC`; `FA-KNTU-ALG`; `FA-IUT-ALG` | Alternative `ایده‌آل بیشینه` should be checked. | `ایده‌آل ماکسیمال \mathfrak m`. | `maximal ideal -> ایده‌آل ماکسیمال`. | Manual/source-review row; register choice unresolved. |
| `term-fa-ir-0020` | ring | `SOURCE_CANON_SUFFICIENT_FOR_SCOPED_DRAFT_WORK` | حلقه | `FA-PNU-RM`; `FA-SHAHROOD-NC`; `FA-KNTU-ALG` | Strongest fa_IR ring anchor. | `حلقه R`; add `واحددار` only when source requires unit. | `Ring/ring -> حلقه`; current Dari row requires independent source evidence and is not authorized by this fa_IR row. | Ready row. |
| `term-fa-ir-0021` | commutative ring | `SOURCE_CANON_SUFFICIENT_FOR_SCOPED_DRAFT_WORK` | حلقه جابجایی | `FA-PNU-RM`; `FA-SHAHROOD-NC`; `FA-KNTU-ALG` | Check `جابجایی`/`جابه‌جایی` spelling and ZWNJ. | Near `ab=ba`: `حلقه جابجایی R`. | `commutative ring -> حلقه جابجایی`. | Ready row; style review needed. |
| `term-fa-ir-0022` | noncommutative ring | `SOURCE_CANON_SUFFICIENT_FOR_SCOPED_DRAFT_WORK` | حلقه ناجابجایی | `FA-SHAHROOD-NC`; `FA-KNTU-ALG`; `FA-IUT-ALG` | Check `ناجابجایی`/`ناجابه‌جایی` spelling. | `حلقه ناجابجایی R`; important near left/right modules. | `noncommutative ring -> حلقه ناجابجایی`. | Ready row with lower exact count; review required. |

## prs_AF Active Row Bucket Table

Dari/Afghan Persian evidence stands on its own. Matching Arabic-script surfaces with `fa_IR` are not cross-authorization.

| Row | Concept | Bucket | Draft rendering | Source witnesses | Alternatives/register notes | Formula-neighboring usage | Interlinear/scaffold | Open acquisition or review note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `term-prs-af-0001` | algebra | `SOURCE_CANON_INSUFFICIENT` | `[gap pending independent Dari source witness]` | `PS-MOMAND-ALG` retired to Pashto; `PRS-MOHE-CURR` routing/curriculum only | Do not use Pashto or fa_IR evidence to fill this row. | No row-level draft until independent Dari algebra body is found. | source-acquisition target: Dari algebra text/definition pages. | Ready context-note row becomes source-acquisition gap after boundary correction. |
| `term-prs-af-0002` | field | `SOURCE_CANON_INSUFFICIENT` | `[gap pending independent Dari source witness]` | `PS-MOMAND-ALG` retired to Pashto | Manual row; do not borrow fa_IR Galois evidence or Pashto eCampus evidence. | No field draft rendering until an independent Dari algebraic-field witness is located. | source-acquisition target: Dari field/Galois/source-body pages. | Manual/source-review row remains a source-acquisition gap. |
| `term-prs-af-0003` | simple | `SOURCE_CANON_INSUFFICIENT` | `[gap pending independent Dari source witness]` | `PS-MOMAND-ALG` retired to Pashto | Broad common word; no fa_IR or Pashto carryover. | No object-level draft until local Dari source context supports it. | source-acquisition target: Dari simple module/group/ring context. | Manual/source-review row remains a source-acquisition gap. |
| `term-prs-af-0004` | ring | `SOURCE_CANON_INSUFFICIENT` | `[gap pending independent Dari source witness]` | `PS-MOMAND-ALG` retired to Pashto; `PRS-KNU-LA` catalog-routing only | Reviewer must not choose `حلقه` vs `رینگ/رينگ` from Pashto or fa_IR evidence. | No ring draft rendering until a Dari ring-definition source body is found. | source-acquisition target: Dari algebra/ring definition pages. | Manual/source-review row remains a source-acquisition gap. |

## Source-Canon Insufficient Active Rows

None in the current `fa_IR` or `prs_AF` active row queues after the sufficiency transition, under the limited standard "sufficient for scoped draft review material." This is not a completion or approval claim. It only means the row can receive draft support while manual/source-review and stronger-source acquisition continue.

## Remaining Source-Acquisition And Gap Rows

| Scope | Gap/blocker | Next acquisition target |
| --- | --- | --- |
| `fa_IR` Noether/invariant source package | No exact Persian Noether/invariant-theory TeX/source package found. | Search Persian university repositories, GitHub/XePersian algebra notes, journal supplemental files, and arXiv-like local source mirrors for invariant theory, Noetherian rings, representation theory, and ideals. |
| `fa_IR` class-field/Galois advanced source | UT candidate returned interstitial HTML; ResearchGate class-field PDF blocked. | Recheck official UT/public thesis repository mirrors or DOI/author pages with real PDF/source access. |
| `prs_AF` TeX/source archive | No Dari/Afghan Persian TeX/LaTeX/arXiv/source archive found. | Search Afghan university repositories, eCampus source packages, ministry textbook source deposits, and public GitHub repos using Dari spellings. |
| `prs_AF` invariant theory | No direct Dari invariant-theory witness found. | Search Dari/Persian Afghan course notes and university syllabi for invariant theory, representation theory, modules, and rings. |
| `prs_AF` KNU electronic record | OPAC viewer points to `8809.PDF`, but fetch gave invalid/null placeholder. | Recheck OPAC session routes, alternate download endpoints, or library mirrors; do not treat placeholder as source text. |
| `tg_Cyrl_TJ` active rows | Original queue has zero promoted Tajik term rows. | Route Tajik witnesses to source-language review before any row promotion; keep scaffolds non-row. |
| `tg_Cyrl_TJ` source package | No Tajik Cyrillic TeX/source archive or Noether-specific source package found. | Search Tajik university repositories, OER source exports, journal supplements, and GitHub Cyrillic math notes. |

## Non-Claim Boundary

Reviewer packet population: false. Native review: false. Accepted terminology: false. Canonical approval: false. Gate promotion: false. Translation completion claim: false. License clearance: false. Tajik term rows created: 0. Git push: false.
