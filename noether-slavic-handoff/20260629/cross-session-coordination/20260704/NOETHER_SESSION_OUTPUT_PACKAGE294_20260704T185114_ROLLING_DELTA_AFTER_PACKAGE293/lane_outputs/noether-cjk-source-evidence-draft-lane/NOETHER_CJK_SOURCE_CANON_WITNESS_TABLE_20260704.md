# Noether CJK Source-Canon Witness Table

Status: **draft/non-canonical/not native reviewed/not approved/not gate-promoted**.

Generated UTC: `2026-07-04T16:45:41+00:00`.

Purpose: source canon first. Translation-slice/glossary expansion is paused unless it directly serves source-corpus/provenance.

Corpus-slice effect: none. This table does not alter the counted CJK corpus rollup.

Retained blockers unchanged: tensor product; localization; Harish-Chandra; abstract algebra; modern algebra; Noetherian-ring/Noether.

## Language Summary

| Language | Rows | Verified TeX/source packages | PDF/HTML witnesses | Gap/weak leads |
| --- | ---: | ---: | ---: | ---: |
| zh-Hans | 2 | 2 | 0 | 0 |
| ja | 5 | 1 | 4 | 0 |
| ko | 2 | 0 | 0 | 2 |

## Witness Table

| ID | Lang | Witness | Type | Status | License Signal | Cached Hash Signals | Gaps |
| --- | --- | --- | --- | --- | --- | --- | --- |
| zh-Hans-src-001 | zh-Hans | [代数学方法 第一卷](https://github.com/wenweili/AlJabr-1) | TeX/LaTeX source repository | verified_source_package_cached | Repository README/About lists CC-BY-4.0; LICENSE present. | `github_commit_api_json` `F016ADF3BE1EB193...`; `commit_pinned_github_zip_archive` `A9C48A33CA900C2D...` | This witness is source-canon/provenance evidence only; it does not approve any Noether row rendering.<br>No direct German baseline row blocker is closed by this source package alone. |
| zh-Hans-src-002 | zh-Hans | [代数学方法 第二卷](https://github.com/wenweili/AlJabr-2) | TeX/LaTeX source repository | verified_source_package_cached | Repository README/About lists CC-BY-4.0; LICENSE present. | `github_commit_api_json` `4730C7CB4F6FDBE6...`; `commit_pinned_github_zip_archive` `0E92CA613A9CE875...` | This witness is source-canon/provenance evidence only; it does not approve any Noether row rendering.<br>No Chinese invariant-theory source archive was verified in this pass. |
| ja-src-001 | ja | [松村英之『可換環論』ノート](https://github.com/Seasawher/matsumura) | TeX/LaTeX source repository | verified_source_package_cached | Repository page lists GPL-3.0; LICENSE present; repository archived/read-only. | `github_commit_api_json` `D2AE98DD80CEE257...`; `commit_pinned_github_zip_archive` `BE714EDE5D12EB0F...` | This is a secondary Japanese source witness, not a native review or canonical glossary.<br>No retained German blocker is closed from the source package without direct row-anchor mapping. |
| ja-pdf-002 | ja | [Tetsuya Ando 代数学 lecture notes](https://www.math.s.chiba-u.ac.jp/~ando/LectureNote.html) | Japanese PDF lecture-note witness set | pdf_html_cached_no_tex_source_found | Lecture-note page says the notes may be used freely unless distributed for a fee; no formal SPDX-style license found. | `html_page` `B1D2D8E8944F3AF5...`; `pdf` `78203FDE040CAB1A...`; `pdf` `57DE472260FE549E...`; `pdf` `EB66C5BFA2081E22...`; `pdf` `04848BC4F6820BEE...` | No TeX source archive located.<br>Permission statement is not a formal open-source license signal. |
| ja-pdf-003 | ja | [古典不変式論ハンドブック](https://www.mathsoc.jp/section/algebra/algsymp_past/algsymp12_files/nagai.pdf) | Japanese PDF publication witness | pdf_cached_no_tex_source_found | No explicit license found in cached PDF/page context. | `pdf` `910AFA5992C953C1...` | No TeX/source package located.<br>License unknown; source-canon row is evidence-only and not a reuse grant. |
| ja-pdf-004 | ja | [可換環論](https://ryoya9826.github.io/files/note/ring.pdf) | Japanese PDF lecture/book witness | pdf_cached_no_tex_source_found | Cached PDF text states CC-BY-SA 3.0. | `pdf` `30946107B13F379C...` | No matching source archive located in this pass.<br>This source does not close Noetherian-ring blocker in the German-corpus lane without row-anchor review. |
| ja-html-005 | ja | [Akira Masuoka lecture notes page](https://sites.google.com/site/akira298math/home/lecture-notes) | Japanese HTML source-routing witness | html_cached_link_index_no_tex_source_found | No explicit license found on cached page. | `html_page` `859C47AC7F812269...` | No TeX/source archive or direct PDF hash opened from this source lead in this pass.<br>License unknown. |
| ko-gap-001 | ko | [한국어 대수학 source-package search audit](generated:github_api_search_audit) | Korean gap/audit record | gap_no_verified_tex_source_package | No reusable Korean algebra source package verified. | `generated_search_audit_json` `246B3879206CD87A...` | No Korean row-level corpus queue is opened.<br>No Korean TeX/LaTeX/arXiv/source archive verified.<br>Course/catalog/web-note leads require separate source opening and licensing review before use. |
| ko-lead-002 | ko | [현대대수학1 KOCW course page](https://kocw.net/home/cview.do?ar=relateCourse&kemId=1165165&mty=p) | Korean weak course-resource lead | weak_lead_not_source_package | No TeX/source-package license verified in cached page. | `html_page` `DCCA6AF38D9BDE43...` | No concrete PDF/TeX payload was verified from this lead in this pass.<br>No Korean corpus prose should be drafted from this row alone. |

## Notes

- The zh-Hans source-package rows are the strongest source-canon candidates in this pass because they are commit-pinned TeX repositories with explicit CC-BY-4.0 signals.
- The Japanese set combines one cached TeX repository with PDF/HTML witnesses for commutative algebra, algebra lecture notes, and invariant theory where TeX source was not verified.
- The Korean addendum is a gap ledger, not a translation lane opening: no verified Korean algebra/invariant-theory TeX/source package was found in the targeted search audit.
- All CJK codepoint/script notes are provenance notes only; none are native review or canonical approval.

