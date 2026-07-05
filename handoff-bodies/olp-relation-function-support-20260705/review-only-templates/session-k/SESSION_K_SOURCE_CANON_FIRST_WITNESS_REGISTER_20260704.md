# Session K Source-Canon-First Witness Register

Generated date: 2026-07-04

Status: `source_canon_first_review_only_no_mapping_no_translation_no_approval`

## Purpose

This table makes source/provenance witnesses easy to find before any review-template, mapping, or translation claim is considered. It records source packages, source archives, source URLs, license signals, local paths, hashes, topic tags, and explicit missing or blocked rows for the OLP/OpenTranslation/relation-function/proof-literacy/OpenIntro material used by this lane.

This is support infrastructure only. It does not create canonical text, native review, community consent, reviewer returns, mapping decisions, translations, approvals, selected excerpts, or package promotion.

## Source Witness Rows

| Witness | Source family | Priority | Format | URL/provenance | License signal | Local evidence and hash | Topic tags | Route/gap |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `K-SCW-001` | Open Logic Project / Open Logic Text | 1 source repo first | LaTeX Git repository | https://github.com/OpenLogicProject/OpenLogic/ and https://openlogicproject.org/download/ | CC BY 4.0 signal from repo/project page | local repo `C:\Users\memo_\Documents\Codex\2026-06-29\files-mentioned-by-the-user-worked\work\OpenLogic`; git head `9f12419d4971165f2fd4ff8cfee95c8dc8b1d019` | OLP; proof-literacy; sets; functions; relations | source pointer only; exact excerpt selection and reviewer return absent |
| `K-SCW-002` | Open Logic Project relation/function subtree | 1 source files first | local LaTeX files | https://github.com/OpenLogicProject/OpenLogic/tree/master/content/sets-functions-relations | CC BY 4.0 signal from parent repo | `sets-functions-relations.tex` sha256 `62C683BA88DF4742CBEF61369A755FBAE8DD53E2173D5F3D1B8A9FC675F27538`; `functions.tex` sha256 `CE481E97A8F301C749D1461326B4EE3D0792B4ADC15A1FCEB7C6ED3B58CECA54`; `relations.tex` sha256 `69E7B017E60673C488D1EC98C186ED0986BC1489B8554F848C95C189AF5C9E54` | sets; relations; function basics; composition; inverses | source pointer only; no source prose copied |
| `K-SCW-003` | Discrete Mathematics: An Open Introduction | 1 source archive first | PreTeXt edition branch source cache | https://github.com/oscarlevin/discrete-book/ and https://discrete.openmathbooks.org/ | CC BY-NC-SA 4.0 signal from cached DMOI license deed | cache `...\source_cache\dmoi_exact_edition_license_20260630T070010Z`; edition source commit `82336dc87d77c3f18d2cdbc8ec1e74eb3ba38799`; cache manifest sha256 `35CBCE00670E62CAC676D9ACCE6E38A6669923ABBB84DE5A40615F69D8491B79` | discrete mathematics; proof; sets; functions; relations | license reconciliation and reviewer-scope return still required |
| `K-SCW-004` | DMOI relation/function coordinate scan | 1 cached source scan first | PreTeXt source scan JSON and source files | https://github.com/oscarlevin/discrete-book/tree/edition/source | CC BY-NC-SA 4.0 signal from cached DMOI license deed | scan summary sha256 `044BDE93019E9D283B30D582ED29F3F726D02A80505C7F521D9CA116233B03E6`; scan rows sha256 `63147BEA383059E1F4214A3A1BA16E813F54DF15BD626733F376D779D8D4828C` | relations; functions; graph theory relations; intro functions | scan rows are support pointers only, not selected excerpts |
| `K-SCW-005` | OpenIntro IMS2 / OpenIntro numeracy cache | 1 source cache first | Quarto/GitHub cache plus license page cache | https://github.com/OpenIntroStat/ims and https://www.openintro.org/license/ | CC BY-SA 3.0 signal from OpenIntro license page | cache `...\source_cache\openintro_ims2`; `github_ims_index_qmd_at_b88f367a.qmd` sha256 `E0745BF7528B494B188E7E62AD86D0322A4CA8A9271A439319372652A8E52117`; license page sha256 `0308B35457E00BF873ED5BAEF6B60C5C0DB91C748042EC9DF21463DBF9B104A7` | numeracy; statistics; function-like mappings; input-output readings | share-alike attribution plan and owner acceptance missing |
| `K-SCW-006` | OpenIntro Statistics source repository | 2 external source repo | LaTeX Git repository | https://github.com/OpenIntroStat/openintro-statistics and https://www.openintro.org/license/ | CC BY-SA 3.0 signal from OpenIntro license page | not cached by Session K for this repo | statistics; numeracy; public-source support | missing local exact commit/hash; URL pointer only |
| `K-SCW-007` | A First Course in Linear Algebra | 2 source repo cache | TeX Git repository and cached metadata | https://github.com/rbeezer/fcla and https://linear.pugetsound.edu/ | GFDL signal from repo README and cached COPYING | cache `...\source_cache\fcla_gfdl_exact_commit_20260630T070951Z`; master commit `cef5ccf49497fa62205a4320b47a440642101e7d`; COPYING sha256 `A72BE10BE0249BDABDD319A3AFF491D7589876953A62FBD6521862C8D9C6D0DC` | linear algebra; linear maps; transformations | GFDL packet separation and compatibility plan required |
| `K-SCW-008` | Abstract Algebra: Theory and Applications | 3 source repo cache | PreTeXt Git repository and cached metadata | https://github.com/twjudson/aata and https://judsonbooks.org/abstract-algebra-theory-and-applications/ | GFDL signal from repo README and cached COPYING | cache `...\source_cache\aata_gfdl_exact_commit_20260630T071615Z`; master commit `8ec4c7df3d70975110143da0aefb5157bfdcf746`; COPYING sha256 `B7D47749512A424173F6A20DAEEA7B00F36B9F5EF95C25930FDBC3BD549B8983` | abstract algebra; homomorphisms; equivalence relations | GFDL packet separation and algebra-owner review required |
| `K-SCW-009` | Stacks Project | 4 external source repo | TeX Git repository | https://github.com/stacks/stacks-project and https://stacks.math.columbia.edu/contribute | GNU Free Documentation License signal from contribution page | not cached by Session K | advanced algebraic geometry; Noether-adjacent terminology | advanced reference only; exact chapter/source hash not captured locally |
| `K-SCW-010` | OpenStax college algebra bundle | 2 external source repo | content repository | https://github.com/openstax/osbooks-college-algebra-bundle and https://openstax.org/books/algebra-and-trigonometry-2e/pages/preface | CC BY-NC-SA 4.0 signal from OpenStax repo and book preface | not cached by Session K | school-to-undergraduate function bridge; algebra; trigonometry | book-specific edition/license/hash capture required |

## Review-Only, Missing, And Blocked Rows

| Witness | Material | Status | Local/provenance pointer | Owner route | Blocker |
| --- | --- | --- | --- | --- | --- |
| `K-SCW-011` | OpenTranslation review-only source-coordinate router | review-only infrastructure | parent output `OPEN_TRANSLATION_REVIEW_ONLY_SOURCE_COORDINATE_SCAN_ROUTER_20260703T081500Z`; bound by `K-BIND-005` and `K-POG-006` | source/evidence owner lane by router row | scan results and owner acceptance absent; not a reviewer return |
| `K-SCW-012` | Proof-literacy source-coordinate policy sheet | review-only infrastructure | parent output `OPEN_TRANSLATION_PROOF_LITERACY_SOURCE_COORDINATE_POLICY_SHEET_20260703T084500Z`; bound by `K-BIND-006` and `K-POG-001` | proof-literacy/source-policy owner | dated source-policy return naming exact edition/license/attribution absent |
| `K-SCW-013` | Package 148 blank relation/function slot-return shell | review-only infrastructure | local `SESSION_K_REVIEW_ONLY_SLOT_RETURN_LEDGER_TEMPLATE_20260704.csv`; bound by `K-BIND-010` and `K-POG-007` | requesting corpus translation lane plus language owner; Session D for ownerless method issue | blank rows are not returns and cannot promote gates |
| `K-SCW-014` | French/Japanese context-note confirmation shell | review-only language-owner route | parent output `CONTEXT_NOTE_CONFIRMATION_RETURN_LEDGER_TEMPLATE_FRENCH_JAPANESE_20260703`; bound by `K-BIND-002` | French lane and Japanese lane | 62 blank rows are not reviewer returns; source canon must be supplied by owners |
| `K-SCW-015` | Non-Slavic frontier language cluster | review-only language-owner route | parent output `NOETHER_NON_SLAVIC_INTERLANGUAGE_FRONTIER_AUDIT_20260703`; bound by `K-BIND-001` | Session C and named language owners | source-canon evidence and language-specific returns remain owner-lane work |
| `K-SCW-016` | Malay-Indonesian operator/function-domain route | review-only language-owner route | local route-precheck cache `...\source_cache\relation_function_local_standard_scope_reviewer_route_precheck_20260702T034500Z`; bound by `K-BIND-009` | Session G / Malay-Indonesian lane | contact/route cache is not reviewer consent and not source-term evidence |
| `K-SCW-017` | Reviewer return intake template family | review-only infrastructure | local `SESSION_K_REVIEWER_RETURN_INTAKE_TEMPLATE_20260704.csv`; bound by `K-POG-008` | responsible owner lane by future row | blank intake rows do not count as returns or approvals |

## Zero-Gate Ledger

| Gate | Count |
| --- | ---: |
| mapping_decisions | 0 |
| translations_created | 0 |
| approvals_recorded | 0 |
| reviewer_returns_ingested | 0 |
| source_text_or_excerpt_files | 0 |
| source_text_copied | 0 |
| excerpts_selected | 0 |
| accepted_local_terms | 0 |
| accepted_bridge_surfaces | 0 |
| readiness_claims | 0 |

Boundary: source/provenance witness metadata only. This register is not canonical text, a reviewer return, a translation, an approval, a native review assertion, a community consent assertion, or a gate promotion.
