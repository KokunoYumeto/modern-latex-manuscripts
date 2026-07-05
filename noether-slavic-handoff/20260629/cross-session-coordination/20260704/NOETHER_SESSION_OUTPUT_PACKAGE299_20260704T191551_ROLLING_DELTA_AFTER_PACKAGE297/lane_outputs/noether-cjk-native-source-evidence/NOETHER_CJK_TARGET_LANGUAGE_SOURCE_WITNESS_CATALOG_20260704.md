# Noether CJK Target-Language Source Witness Catalog

Generated UTC: `2026-07-04T16:41:42Z`

Status: `source-canon-witness-layer / draft / non-canonical / not native reviewed / not approved / not gate-promoted`.

This catalog makes target-language mathematical source witnesses findable for the CJK native/source-evidence lane. It records existing publications, TeX/LaTeX/source archives, PDF fallbacks, URLs, license signals, local evidence paths, hashes, and explicit gaps. It does not translate Noether text, promote glossary terms, certify native review, claim public approval, or create a pan-CJK/Korean-school bridge.

## Source Tier Policy

| Tier | Meaning | Use in this lane |
| --- | --- | --- |
| `fixed_commit_tex` | Single TeX file captured from a fixed commit/raw URL with SHA256. | Strongest target-language witness row for exact findability. |
| `source_archive_tex` | Downloaded TeX/source repository archive with local hash, local extracted root, and license signal. | Strong source shelf for native mathematical register/source support. |
| `content_confirmed_bulk_tex` | Codepoint-redo GitHub TeX downloads checked for actual term content. | Search-evidence shelf; cite the manifest rather than raw hit counts. |
| `pdf_fallback` | Downloaded public PDF with SHA256 and extraction status. | Lower tier where TeX/source is unavailable or thin. |
| `ctan_infrastructure` | CTAN language/CJK TeX package source. | Typesetting/source-infrastructure evidence only, not algebra/invariant-theory term authority. |
| `korean_route_only` | Korean source-discovery/crosswalk evidence. | Addendum routing only; no Korean Noether edition or pan-CJK claim. |

## Inputs Audited

- Evidence root: `C:\Users\memo_\Documents\Codex\2026-06-09\could-you-look-online-for-me\work\noether-slavic-canonical`
- Hard-term refresh: `logs/CJK_HARDTERM_SOURCE_REFRESH_20260703T105104Z.md/json`
- Codepoint redo: `logs/CJK_INVARIANT_REPRESENTATION_CODEPOINT_REDO_20260703T123013Z.md/json`
- Codepoint content confirmation: `logs/CJK_INVARIANT_REPRESENTATION_CODEPOINT_REDO_CONTENT_CONFIRMATION_20260703T123013Z.md/json`
- Chinese/Japanese native math shelf: `logs/CHINESE_JAPANESE_NATIVE_MATH_REGISTER_SHELF_20260628.md/json`
- Asia-wide TeX source shelf: `logs/ASIA_WIDE_TEX_SOURCE_MATH_REGISTER_SHELF_20260628T215200Z.md/json`
- Split-lane source status/routing comparator: `C:\Users\memo_\Documents\Codex\2026-07-04\noether-cjk-source-evidence-draft-lane\outputs\NOETHER_CJK_SOURCE_EVIDENCE_STATUS_20260704.md` and `NOETHER_CJK_SOURCE_WITNESS_ROUTING_FIX_PASS_05_20260704.md`
- Current source-baseline/blocker correction: `C:\Users\memo_\Documents\Codex\2026-07-04\noether-cjk-source-evidence-draft-lane\outputs\NOETHER_CJK_RETAINED_BLOCKERS_SOURCE_BASELINE_ADDENDUM_20260704.md`
- Current provenance probe: `outputs/NOETHER_CJK_SOURCE_WITNESS_PROVENANCE_PROBE_20260704.md/json`
- Fallback-format scan: `outputs/NOETHER_CJK_FALLBACK_FORMAT_PROVENANCE_SCAN_20260704.md/json`

## Selected Witness Catalog

| Witness id | Lane | Topic support | Tier / format | URL or source | Local evidence / hash | License signal | Boundary |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `zh_repo_wenweili_aljabr1` | Simplified Chinese | algebra, rings, fields, ideals, modules, Noether/Noetherian register | `source_archive_tex` / GitHub TeX repository | https://github.com/wenweili/AlJabr-1 | `sources/non_slavic_reference_corpus/20260628_chinese_japanese_native_math/source_repositories/archives/wenweili__AlJabr-1__master.zip`; SHA256 `6E026C3E9B7BD1CC20335BE488BBA7A4CEE459334EAAA58684A9C60CC1EB47FB`; 19 TeX files | GitHub API: `cc-by-4.0` / Creative Commons Attribution 4.0 International | Source witness only; no term approval. |
| `zh_repo_wenweili_aljabr2` | Simplified Chinese | algebra continuation, modules, homological/advanced algebra, invariant-theory term occurrence | `source_archive_tex` / GitHub TeX repository | https://github.com/wenweili/AlJabr-2 | `sources/non_slavic_reference_corpus/20260628_chinese_japanese_native_math/source_repositories/archives/wenweili__AlJabr-2__master.zip`; SHA256 `1B4223DDCBCDD51FF813070229F01D8FA56B7EB866EE9851C42FC2AEC7CEB9E7`; 21 TeX files | GitHub API: `cc-by-4.0` / Creative Commons Attribution 4.0 International | Strong source shelf, but not dedicated invariant-theory source. |
| `zh_repo_lbwang_cinta` | Simplified Chinese | rings, fields, polynomials, isomorphism; computational/number-theory algebra | `source_archive_tex` / GitHub TeX repository | https://github.com/lbwang/CINTA-cn | `sources/non_slavic_reference_corpus/20260628_chinese_japanese_native_math/source_repositories/archives/lbwang__CINTA-cn__master.zip`; SHA256 `3941C7C70DDC1204687B5DE021612DB8F26788CFE259DF79C9773C2E35A0E540`; 31 TeX files | GitHub API: `other`; local shelf had `NOASSERTION`; no license assumption | Register support, not redistribution clearance. |
| `zh_fixed_ayhe123_invariant_section` | Simplified Chinese | invariant theory, polynomial/ring context | `fixed_commit_tex` / TeX file | https://raw.githubusercontent.com/ayhe123/algebra-lecturenote/567dd325f245f3ec3700e0bc9d8e626ac24420e0/1-6.tex | `sources/non_slavic_reference_corpus/20260703T105104Z_cjk_hardterm_source_refresh/source_files/zh_tex_ayhe123_algebra_lecturenote_invariant_section__1-6.tex`; SHA256 `8E87A461BACB979795FF6AF9C6CCCFA5C4E4FDF8D6C3F6250C6CE7650184D71B` | GitHub API for repo: `cc-by-4.0` | Strong exact source witness for `不变量理论`; no glossary promotion. |
| `zh_pdf_ecnu_commutative_algebra` | Simplified Chinese | commutative algebra, rings, ideals, modules, Noetherian terminology | `pdf_fallback` / PDF | https://math.ecnu.edu.cn/~rdu/years/ca%20book/main.pdf | `sources/non_slavic_reference_corpus/20260628_chinese_japanese_native_math/chinese/ecnu_commutative_algebra_book_main.pdf`; SHA256 `C84AC610F21076DF2EC3AB6737D0713D1C84D3A84B38D2FAC42EAFEB3760C862`; 164 pages | Public university PDF; no explicit open license found in local shelf | Lower than TeX source; internal evidence candidate only. |
| `zh_pdf_hfut_group_representation` | Simplified Chinese | group representation / representation-theory register | `pdf_fallback` / PDF | https://faculty.hfut.edu.cn/_resources/group1/M00/00/1A/rB_zR2jQEVKARzGGABDKdnVFJ60618.pdf | `sources/non_slavic_reference_corpus/20260628_chinese_japanese_native_math/chinese/hfut_group_representation_lecture.pdf`; SHA256 `01C390945C8795BF481E6B429B20579751075C6C712736669FCFE5854AB53C49`; 32 pages | Public university PDF; no explicit open license found in local shelf | PDF fallback, not publication clearance. |
| `ja_repo_seasawher_matsumura` | Japanese | commutative algebra, rings, ideals, modules, Noetherian terms | `source_archive_tex` / GitHub TeX repository | https://github.com/Seasawher/matsumura | `sources/non_slavic_reference_corpus/20260628_chinese_japanese_native_math/source_repositories/archives/Seasawher__matsumura__master.zip`; SHA256 `11AF615C02C5973C110FF9337E38B052D97F9C49498560E8A442AFFBA8535E2B`; 11 TeX files | GitHub API: `gpl-3.0` / GNU GPL v3.0 | Strong Japanese algebra source shelf; not native-review approval. |
| `ja_repo_seasawher_hartshorne` | Japanese | algebraic geometry, commutative algebra, rings, ideals, modules | `source_archive_tex` / GitHub TeX repository | https://github.com/Seasawher/hartshorne | `sources/non_slavic_reference_corpus/20260628_chinese_japanese_native_math/source_repositories/archives/Seasawher__hartshorne__master.zip`; SHA256 `A09DC6B571A0656A40001A2F14E7FAC873099CF4569815532A8DE1F46CDC4AF8`; 13 TeX files | GitHub API: `gpl-3.0` / GNU GPL v3.0 | Source shelf only; exact invariant/representation topics still need stronger TeX witnesses. |
| `ja_fixed_t2sp_invariant_chapter` | Japanese | invariant theory, invariant forms, modules, algebra context | `fixed_commit_tex` / TeX file | https://raw.githubusercontent.com/T2sp/rep/9950dd9fc800e0d288aaf3fcd07ec31e82ccbb6d/doc/chap6.tex | `sources/non_slavic_reference_corpus/20260703T105104Z_cjk_hardterm_source_refresh/source_files/ja_tex_t2sp_rep_invariant_chapter__doc__chap6.tex`; SHA256 `704F9B8272F00E6A69C6A9AFCDAB3EDE2CCBFC5DEBF41C714A0CBC51007B7CD9` | GitHub API: no license exposed; `/license` returned 404 | Strong exact source witness; license remains unresolved. |
| `ja_fixed_t2sp_rep_main` | Japanese | representation theory label/source context | `fixed_commit_tex` / TeX file | https://raw.githubusercontent.com/T2sp/rep/9950dd9fc800e0d288aaf3fcd07ec31e82ccbb6d/doc/rep_main.tex | `sources/non_slavic_reference_corpus/20260703T105104Z_cjk_hardterm_source_refresh/source_files/ja_tex_t2sp_rep_main__doc__rep_main.tex`; SHA256 `059D66CE9278E3A7B4EFCD74045C1E200074B30D9AC745E02BC4697CBA735C89` | GitHub API: no license exposed; `/license` returned 404 | Source witness only; no term authority. |
| `ja_fixed_naoki_lie_representation` | Japanese | Lie-group representation theory | `fixed_commit_tex` / TeX file | https://raw.githubusercontent.com/naoki-cpp/physics/1a3d09bb518649f9269147c208feb139f1b7ca29/mathematics/RepresentationTheory/src/rep-of-Lie-group.tex | `sources/non_slavic_reference_corpus/20260703T105104Z_cjk_hardterm_source_refresh/source_files/ja_tex_naoki_cpp_lie_group_representation__mathematics__RepresentationTheory__src__rep-of-Lie-group.tex`; SHA256 `BD2A84223B4DF14D8B660A6E2DCE08766F773EE0243560C61663F533643E8643` | GitHub API: no license exposed; `/license` returned 404 | Strong source file, but license unresolved. |
| `ja_pdf_kurims_mukai_hilbert14` | Japanese | invariant theory and Hilbert 14 | `pdf_fallback` / PDF | https://www.kurims.kyoto-u.ac.jp/~kenkyubu/kokai-koza/H16-mukai.pdf | `sources/non_slavic_reference_corpus/20260628_chinese_japanese_native_math/japanese/kurims_mukai_invariant_theory_hilbert14.pdf`; SHA256 `615FB345BB140048F2F31B0D8684B654E446ED5DEB140D63DAAF692A5BBBEF25`; 19 pages | Public institutional PDF; no explicit open license found in local shelf | Important fallback where TeX is thin. |
| `ja_pdf_nagoya_reflection_invariants` | Japanese | finite reflection groups / invariant theory | `pdf_fallback` / PDF | https://www.math.nagoya-u.ac.jp/~yanagida/edu/17S/20170601.pdf | `sources/non_slavic_reference_corpus/20260628_chinese_japanese_native_math/japanese/nagoya_invariant_theory_finite_reflection_groups.pdf`; SHA256 `3E3A5B863DC8E8F6791DA4DFB560250293259675F35417DC7FE043FB9F3C8E6E`; 4 pages | Public institutional PDF; no explicit open license found in local shelf | Fallback evidence only. |
| `ja_pdf_nagoya_finite_group_representation` | Japanese | finite group representation theory | `pdf_fallback` / PDF | https://www.math.nagoya-u.ac.jp/~yanagida/edu/25W/1009.pdf | `sources/non_slavic_reference_corpus/20260628_chinese_japanese_native_math/japanese/nagoya_finite_group_representation_2025_1009.pdf`; SHA256 `756D738627E00BDA79A39D4E1637D57FC6E85524A3054CF650806EAA64190D78`; 9 pages | Public institutional PDF; no explicit open license found in local shelf | Fallback evidence only. |
| `ko_repo_kaist_math_notes` | Korean addendum | broad Korean math TeX source shelf | `korean_route_only` / source archive | https://github.com/A-H4NU/kaist-math-notes | `sources/non_slavic_reference_corpus/20260628T215200Z_asia_wide_tex_source_register/east_asia/korean/A-H4NU_kaist-math-notes/source`; archive SHA256 `C2B6ACBB37BCED39CA88901B78D0235CB16396F7543EC8D7F1388BDCC58953F6`; 171 source files | GitHub API: no license exposed; `/license` returned 404 | Route-only Korean source shelf, not CJK bridge or edition. |
| `ko_modern_math_syllabus` | Korean addendum | rings, fields, modules, ideals, homomorphisms | `korean_route_only` / TeX files | https://github.com/Hacker-Code-J/Modern-Mathematics | `grad-math/grad-math-7.tex` SHA256 `A4451C6FD59389FAD4957E9E84E3F03BD89954612EE30F385DE4A7225BC707EF`; `mathematics_seminar/syllabus.tex` SHA256 `1A5BE9A9C6086A97058FB18458C0E72F6EA94B65A1C377C5B9A94AA564460E8F` | GitHub API: `mit` / MIT License | Low-tier source-discovery/addendum routing only. |
| `ko_calofmijuck_algebra` | Korean addendum | algebra/ring/module seed source | `korean_route_only` / TeX file | https://github.com/calofmijuck/algebra | `chap/01/01.tex` SHA256 `8655797153006A2E958D4FBF276555E8FB0A73961E0325F4038DCF90150BE7EA` | GitHub API: no license exposed; `/license` returned 404 | Low-tier addendum route only. |
| `ko_younghu_rdl_unified_master` | Korean addendum | localization and tensor-product Korean terms in a source file | `korean_route_only` / TeX file | https://github.com/younghu-kim/rdl-resonant-detection | `paper/source/unified_master_ko.tex` SHA256 `159A51CCE825B07D151867F68F0DCB7B0EC136A938024BA11833387C1F0A18D6`; recorded counts include `국소화:21`, `텐서곱:2` | GitHub API: `gpl-3.0` / GNU GPL v3.0 | Korean route-only; cannot close JP/zh-Hans tensor/localization blockers. |
| `bulk_codepoint_redo_manifest` | Simplified Chinese / Japanese | invariant theory, representation theory, Noether/ring exact-codepoint search shelf | `content_confirmed_bulk_tex` | Local GitHub code-search replay manifests under `sources/non_slavic_reference_corpus/20260703T123013Z_cjk_invariant_representation_codepoint_redo` | Effective accepted source hits `124`; downloaded TeX files `105`; content-confirmed downloads `105/105`; content-confirmed rescues `16`; cite `logs/CJK_INVARIANT_REPRESENTATION_CODEPOINT_REDO_CONTENT_CONFIRMATION_20260703T123013Z.md/json` | Per-repository licenses not normalized for all 105 files; use manifest row-by-row before redistribution | Search witness shelf; raw GitHub counts are telemetry. |
| `cjk_ctan_typesetting_infrastructure` | CJK/Japanese/Chinese/Korean infrastructure | CJK TeX implementation support, not math term authority | `ctan_infrastructure` | https://ctan.org/pkg/ctex, https://ctan.org/pkg/xecjk, https://ctan.org/pkg/luatexja, https://ctan.org/pkg/kotex-utils | Local source hashes in `logs/ASIA_WIDE_TEX_SOURCE_MATH_REGISTER_SHELF_20260628T215200Z.md/json`: `ctex` `636B6A6E...`, `xeCJK` `AA39C692...`, `LuaTeX-ja` `DDA7F946...`, `ko.TeX utilities` `288F4659...` | CTAN JSON checked 2026-07-04: `ctex` LPPL 1.3c, `xecjk` LPPL 1.3c, `luatexja` BSD, `kotex-utils` LPPL 1.3c | Typesetting/source baseline only; no algebra or translation claim. |

## Exact Codepoint / Search Status

| Query id | Exact representation | Codepoints | Status |
| --- | --- | --- | --- |
| `zh_invariant_theory_exact` | `不变量理论` | `U+4E0D U+53D8 U+91CF U+7406 U+8BBA` | Codepoint redo accepted `11`; hard-term fixed witness `zh_fixed_ayhe123_invariant_section` captured. |
| `zh_invariant_form_theory_exact` | `不变式理论` | `U+4E0D U+53D8 U+5F0F U+7406 U+8BBA` | Accepted `0`; retained as an explicit gap. |
| `zh_invariant_form_hilbert` | `不变式` + `Hilbert` | `U+4E0D U+53D8 U+5F0F` + ASCII `Hilbert` | Accepted `0`; retained as an explicit gap. |
| `zh_invariant_form_fourteenth` | `不变式` + `第十四` | `U+4E0D U+53D8 U+5F0F` + `U+7B2C U+5341 U+56DB` | Accepted `1`; source-status only. |
| `zh_representation_theory_group` | `表示论` + `群` | `U+8868 U+793A U+8BBA` + `U+7FA4` | Accepted `20`; content-confirmation shelf cited, not raw count promotion. |
| `zh_representation_theory_lie` | `表示论` + `Lie` | `U+8868 U+793A U+8BBA` + ASCII `Lie` | Accepted `16`; content-confirmation shelf cited. |
| `zh_noether_ring` | `诺特` + `环` | `U+8BFA U+7279` + `U+73AF` | Accepted `20`; source witness only. |
| `ja_invariant_theory_exact` | `不変式論` | `U+4E0D U+5909 U+5F0F U+8AD6` | Accepted `1`; fixed witness `ja_fixed_t2sp_invariant_chapter` captured. |
| `ja_invariant_form_hilbert` | `不変式` + `Hilbert` | `U+4E0D U+5909 U+5F0F` + ASCII `Hilbert` | Accepted `7`; source-status only. |
| `ja_invariant_form_14_retry` | `不変式` + `14` | `U+4E0D U+5909 U+5F0F` + ASCII `14` | Retry accepted `8`; source-status only. |
| `ja_representation_theory_exact_retry` | `表現論` | `U+8868 U+73FE U+8AD6` | Retry raw `20`, accepted `0`; exact standalone query remains blocked in this shelf. |
| `ja_representation_theory_group_retry` | `表現論` + `群` | `U+8868 U+73FE U+8AD6` + `U+7FA4` | Retry accepted `20`; fixed/source witnesses captured for group/Lie context. |
| `ja_noether_ring_retry` | `ネーター` + `環` | `U+30CD U+30FC U+30BF U+30FC` + `U+74B0` | Retry accepted `20`; source witness only. |
| `arxiv_exact_phrase_checks` | zh/ja exact phrase set | See hard-term and codepoint-redo logs | All queried exact phrase totals were `0`; TeX/source archives remain primary. |

## Provenance Probe Refresh

Artifact: `outputs/NOETHER_CJK_SOURCE_WITNESS_PROVENANCE_PROBE_20260704.md/json`.

Current probe result:

- GitHub repositories probed with authenticated `gh api`: `16`; metadata errors: `0`; successful repositories without API-exposed license endpoint keys: `7`.
- Raw TeX URLs probed: `8`; HTTP successes: `8`; hash matches against recorded evidence: `8`.
- PDF fallback HEAD probes: `5`; CTAN package JSON probes: `4`.
- arXiv exact phrase rechecks: `11`; positive total-results rows: `0`.

Use this probe as endpoint/source provenance only. It does not close license clearance, native-review, glossary, or retained corpus blockers.

## Fallback Format Scan

Artifact: `outputs/NOETHER_CJK_FALLBACK_FORMAT_PROVENANCE_SCAN_20260704.md/json`.

Result:

- Audited roots scanned: `4`.
- TeX/source-like files across those roots: `503`.
- PDF files: `51`, all in the Chinese/Japanese native math shelf.
- DOC/DOCX files: `0`.
- Text/README/RST files: `44`; treated as source-package support/provenance files, not primary mathematical witnesses.

## Korean Addendum Routing

Korean source evidence is useful as route-only addendum material, especially the `younghu-kim/rdl-resonant-detection` source file that contains `국소화` and `텐서곱`. It does not close Japanese or Simplified Chinese retained blockers, does not authorize Korean corpus prose, and does not create a pan-CJK or Korean-school interlanguage project.

## Explicit Gaps And Blockers

- `zh_invariant_form_theory_exact`: no accepted source hits for exact `不变式理论`; `不变式 + Hilbert` also accepted `0`.
- `ja_representation_theory_exact_retry`: raw retry returned `20`, but accepted source hits were `0` for standalone `表現論`; group-context query is usable instead.
- `tensor product`: retained blocker for Japanese/Simplified Chinese corpus prose. No direct German `Tensor`, `Tensorprodukt`, or lowercase `tensor` prose anchor; noisy `\otimes` and Kronecker/product contexts are insufficient.
- `localization`: retained blocker for Japanese/Simplified Chinese corpus prose. Quotient-ring/product/local/prime/quotient-field contexts and `Idealquotienten` are not `Lokalisierung`.
- `Harish-Chandra`: Japanese source-shelf/proper-name evidence only; no German corpus anchor.
- `abstract algebra`: Simplified Chinese source-shelf/register evidence only; no German `abstrakte Algebra` course/category anchor.
- `modern algebra`: Simplified Chinese `近世代数`/`现代代数` shelf evidence only; `Moderne Algebra II` is bibliographic/title evidence only.
- Licenses: several GitHub repositories expose no license through the GitHub API (`T2sp/rep`, `naoki-cpp/physics`, `A-H4NU/kaist-math-notes`, `calofmijuck/algebra`, and others). Treat those rows as source-discovery evidence until license review is done.
- PDFs: public institutional PDFs are lower-tier fallback witnesses. Several have no explicit open-license signal; use internally unless clearance is established.
- Native/public review: no source row in this catalog is a native-review return, glossary approval, or publication authorization.

## Packaging Decision

This catalog supersedes earlier checkpoint-only source-support language for the immediate source-canon task. The CJK lane now has a findable witness layer for Japanese, Simplified Chinese, and Korean addendum routing, while retained blockers and license/native-review gaps remain open.
