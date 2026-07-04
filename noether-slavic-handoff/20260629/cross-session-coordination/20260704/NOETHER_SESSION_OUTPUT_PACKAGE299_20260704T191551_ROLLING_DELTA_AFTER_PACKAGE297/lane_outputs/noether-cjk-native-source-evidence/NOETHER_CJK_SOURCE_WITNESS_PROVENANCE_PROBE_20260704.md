# Noether CJK Source Witness Provenance Probe

Generated UTC: `2026-07-04T17:04:08Z`

Status: `source-witness-provenance-probe / draft / non-canonical / not native reviewed / not approved / not gate-promoted`.

This probe preserves current endpoint/source metadata for the source-canon witness layer. It does not translate Noether text, approve terms, claim native review, claim public signoff, or create a pan-CJK/Korean-school bridge.

## Summary

- GitHub repositories probed with authenticated `gh api`: `16`; metadata errors: `0`; successful repos without API-exposed license endpoint keys: `7`.
- Raw TeX URLs probed: `8`; HTTP successes: `8`; hash matches against recorded evidence: `8`.
- PDF fallback HEAD probes: `5`; HEAD successes: `5`.
- CTAN package JSON probes: `4`.
- arXiv exact phrase rechecks: `11`; positive total-results rows: `0`.

## Raw TeX Hash Probes

| ID | Lane | Tier | Status | Bytes | SHA256 | Matches recorded hash | URL |
| --- | --- | --- | --- | ---: | --- | --- | --- |
| `zh_fixed_ayhe123_invariant_section` | `simplified_chinese` | `fixed_commit_tex` | `ok` | 61218 | `8E87A461BACB979795FF6AF9C6CCCFA5C4E4FDF8D6C3F6250C6CE7650184D71B` | `True` | https://raw.githubusercontent.com/ayhe123/algebra-lecturenote/567dd325f245f3ec3700e0bc9d8e626ac24420e0/1-6.tex |
| `ja_fixed_t2sp_invariant_chapter` | `japanese` | `fixed_commit_tex` | `ok` | 86956 | `704F9B8272F00E6A69C6A9AFCDAB3EDE2CCBFC5DEBF41C714A0CBC51007B7CD9` | `True` | https://raw.githubusercontent.com/T2sp/rep/9950dd9fc800e0d288aaf3fcd07ec31e82ccbb6d/doc/chap6.tex |
| `ja_fixed_t2sp_rep_main` | `japanese` | `fixed_commit_tex` | `ok` | 8343 | `059D66CE9278E3A7B4EFCD74045C1E200074B30D9AC745E02BC4697CBA735C89` | `True` | https://raw.githubusercontent.com/T2sp/rep/9950dd9fc800e0d288aaf3fcd07ec31e82ccbb6d/doc/rep_main.tex |
| `ja_fixed_naoki_lie_representation` | `japanese` | `fixed_commit_tex` | `ok` | 6291 | `BD2A84223B4DF14D8B660A6E2DCE08766F773EE0243560C61663F533643E8643` | `True` | https://raw.githubusercontent.com/naoki-cpp/physics/1a3d09bb518649f9269147c208feb139f1b7ca29/mathematics/RepresentationTheory/src/rep-of-Lie-group.tex |
| `ko_modern_math_grad_math_7_default_branch` | `korean_addendum_route_only` | `korean_route_only_default_branch_probe` | `ok` | 19026 | `A4451C6FD59389FAD4957E9E84E3F03BD89954612EE30F385DE4A7225BC707EF` | `True` | https://raw.githubusercontent.com/Hacker-Code-J/Modern-Mathematics/main/grad-math/grad-math-7.tex |
| `ko_modern_math_syllabus_default_branch` | `korean_addendum_route_only` | `korean_route_only_default_branch_probe` | `ok` | 77100 | `1A5BE9A9C6086A97058FB18458C0E72F6EA94B65A1C377C5B9A94AA564460E8F` | `True` | https://raw.githubusercontent.com/Hacker-Code-J/Modern-Mathematics/main/mathematics_seminar/syllabus.tex |
| `ko_calofmijuck_algebra_chap01_default_branch` | `korean_addendum_route_only` | `korean_route_only_default_branch_probe` | `ok` | 9131 | `8655797153006A2E958D4FBF276555E8FB0A73961E0325F4038DCF90150BE7EA` | `True` | https://raw.githubusercontent.com/calofmijuck/algebra/master/chap/01/01.tex |
| `ko_younghu_rdl_unified_master_default_branch` | `korean_addendum_route_only` | `korean_route_only_default_branch_probe` | `ok` | 264890 | `159A51CCE825B07D151867F68F0DCB7B0EC136A938024BA11833387C1F0A18D6` | `True` | https://raw.githubusercontent.com/younghu-kim/rdl-resonant-detection/master/paper/source/unified_master_ko.tex |

## GitHub License Metadata

| Repo | Default branch | Repo API license | License endpoint | Pushed at | Caveat |
| --- | --- | --- | --- | --- | --- |
| `wenweili/AlJabr-1` | `master` | `cc-by-4.0 / Creative Commons Attribution 4.0 International` | `cc-by-4.0 / Creative Commons Attribution 4.0 International` | `06/09/2026 11:06:27` | metadata_signal_only |
| `wenweili/AlJabr-2` | `master` | `cc-by-4.0 / Creative Commons Attribution 4.0 International` | `cc-by-4.0 / Creative Commons Attribution 4.0 International` | `07/03/2026 10:22:21` | metadata_signal_only |
| `lbwang/CINTA-cn` | `master` | `other / Other` | `other / Other` | `06/29/2026 08:56:30` | metadata_signal_only |
| `ayhe123/algebra-lecturenote` | `main` | `cc-by-4.0 / Creative Commons Attribution 4.0 International` | `cc-by-4.0 / Creative Commons Attribution 4.0 International` | `04/23/2023 13:20:30` | metadata_signal_only |
| `Seasawher/matsumura` | `master` | `gpl-3.0 / GNU General Public License v3.0` | `gpl-3.0 / GNU General Public License v3.0` | `08/25/2019 08:14:18` | metadata_signal_only |
| `Seasawher/hartshorne` | `master` | `gpl-3.0 / GNU General Public License v3.0` | `gpl-3.0 / GNU General Public License v3.0` | `05/29/2019 23:46:35` | metadata_signal_only |
| `T2sp/rep` | `main` | `none_exposed` | `none_or_error` | `03/06/2025 09:44:52` | gh: Not Found (HTTP 404)
{"message":"Not Found","documentation_url":"https://docs.github.com/rest/licenses/licenses#get-the-license-for-a-repository","status":"404"} |
| `naoki-cpp/physics` | `master` | `none_exposed` | `none_or_error` | `07/04/2026 07:10:52` | gh: Not Found (HTTP 404)
{"message":"Not Found","documentation_url":"https://docs.github.com/rest/licenses/licenses#get-the-license-for-a-repository","status":"404"} |
| `A-H4NU/kaist-math-notes` | `main` | `none_exposed` | `none_or_error` | `09/07/2025 21:42:14` | gh: Not Found (HTTP 404)
{"message":"Not Found","documentation_url":"https://docs.github.com/rest/licenses/licenses#get-the-license-for-a-repository","status":"404"} |
| `Hacker-Code-J/Modern-Mathematics` | `main` | `mit / MIT License` | `mit / MIT License` | `06/29/2026 16:05:53` | metadata_signal_only |
| `calofmijuck/algebra` | `master` | `none_exposed` | `none_or_error` | `06/16/2020 00:09:43` | gh: Not Found (HTTP 404)
{"message":"Not Found","documentation_url":"https://docs.github.com/rest/licenses/licenses#get-the-license-for-a-repository","status":"404"} |
| `younghu-kim/rdl-resonant-detection` | `master` | `gpl-3.0 / GNU General Public License v3.0` | `gpl-3.0 / GNU General Public License v3.0` | `07/02/2026 06:34:16` | metadata_signal_only |
| `EasonSYC/maths-notes` | `main` | `mit / MIT License` | `mit / MIT License` | `05/07/2024 09:59:04` | metadata_signal_only |
| `KelvinHoKaHim/undergraduate-mathematics` | `main` | `none_exposed` | `none_or_error` | `10/28/2024 04:00:58` | gh: Not Found (HTTP 404)
{"message":"Not Found","documentation_url":"https://docs.github.com/rest/licenses/licenses#get-the-license-for-a-repository","status":"404"} |
| `24dakenlo/math_remedial` | `master` | `none_exposed` | `none_or_error` | `03/21/2019 23:12:26` | gh: Not Found (HTTP 404)
{"message":"Not Found","documentation_url":"https://docs.github.com/rest/licenses/licenses#get-the-license-for-a-repository","status":"404"} |
| `masamichiIto/seminar_materials` | `master` | `none_exposed` | `none_or_error` | `06/21/2020 11:11:45` | gh: Not Found (HTTP 404)
{"message":"Not Found","documentation_url":"https://docs.github.com/rest/licenses/licenses#get-the-license-for-a-repository","status":"404"} |

## CTAN Metadata

| Package | Version | License | Topics | URL |
| --- | --- | --- | --- | --- |
| `ctex` | `2.6.1` | `"lppl1.3c"` | `class,book-pub,chinese,tagged-pdf-incompatible` | https://ctan.org/pkg/ctex |
| `xecjk` | `3.10.1` | `"lppl1.3c"` | `korean,chinese,japanese,xetex,tagged-pdf-unsupported` | https://ctan.org/pkg/xecjk |
| `luatexja` | `20260517.0` | `"bsd"` | `luatex,macro-gen,tagged-pdf-partially,class,japanese` | https://ctan.org/pkg/luatexja |
| `kotex-utils` | `2.1.0` | `"lppl1.3c"` | `index,korean` | https://ctan.org/pkg/kotex-utils |

## arXiv Exact Phrase Recheck

| ID | Phrase | Status | Total results | Entries | XML SHA256 | URL |
| --- | --- | --- | ---: | ---: | --- | --- |
| `zh_invariant_theory` | `不变量理论` | `ok` | 0 | 0 | `AFC1490DDEE8E77269E5C05D71CBE1164182804D12B2E68BA8A0645F3613F631` | https://export.arxiv.org/api/query?search_query=all%3A%22%E4%B8%8D%E5%8F%98%E9%87%8F%E7%90%86%E8%AE%BA%22&start=0&max_results=5 |
| `zh_invariant_form_theory` | `不变式理论` | `ok` | 0 | 0 | `0870DF2EF732CEA1F7C4ABEEBB7CB475B85855BC4433893423C3A6600C478559` | https://export.arxiv.org/api/query?search_query=all%3A%22%E4%B8%8D%E5%8F%98%E5%BC%8F%E7%90%86%E8%AE%BA%22&start=0&max_results=5 |
| `zh_representation_theory` | `表示论` | `ok` | 0 | 0 | `CDEBCFD40F331C392DB4DF8FD36910B5E5F97F58DDF3D7EADBFC1DBFC49EF3B5` | https://export.arxiv.org/api/query?search_query=all%3A%22%E8%A1%A8%E7%A4%BA%E8%AE%BA%22&start=0&max_results=5 |
| `zh_noether_ring` | `诺特环` | `ok` | 0 | 0 | `1754541835FE45EA755AF48DF1B60AEC03AA55128889DC142C37DD6F9F107778` | https://export.arxiv.org/api/query?search_query=all%3A%22%E8%AF%BA%E7%89%B9%E7%8E%AF%22&start=0&max_results=5 |
| `zh_commutative_algebra` | `交换代数` | `ok` | 0 | 0 | `27BEED752CD81E71547518E6BC2F71CA51735C2DDB7299FFD3961CDE21719CEA` | https://export.arxiv.org/api/query?search_query=all%3A%22%E4%BA%A4%E6%8D%A2%E4%BB%A3%E6%95%B0%22&start=0&max_results=5 |
| `ja_invariant_theory` | `不変式論` | `ok` | 0 | 0 | `4E7B0D493F779D5EEBD68B5ECD8E852B20957629A858103F4358C8AA33ABA0F0` | https://export.arxiv.org/api/query?search_query=all%3A%22%E4%B8%8D%E5%A4%89%E5%BC%8F%E8%AB%96%22&start=0&max_results=5 |
| `ja_representation_theory` | `表現論` | `ok` | 0 | 0 | `4D651D1102F91CAD3831048A435499EC35244A5689249E36BAD21934CFF5F5A9` | https://export.arxiv.org/api/query?search_query=all%3A%22%E8%A1%A8%E7%8F%BE%E8%AB%96%22&start=0&max_results=5 |
| `ja_noether_ring` | `ネーター環` | `ok` | 0 | 0 | `A9D5C0CF642266195B7FD93EBCEF80B231EE39C2894D27C88411823D95FDF1CA` | https://export.arxiv.org/api/query?search_query=all%3A%22%E3%83%8D%E3%83%BC%E3%82%BF%E3%83%BC%E7%92%B0%22&start=0&max_results=5 |
| `ja_commutative_algebra` | `可換環論` | `ok` | 0 | 0 | `4A11A83D8DA287B0456BB46D84E8141D31051DF04409148862065B88726B201E` | https://export.arxiv.org/api/query?search_query=all%3A%22%E5%8F%AF%E6%8F%9B%E7%92%B0%E8%AB%96%22&start=0&max_results=5 |
| `ko_tensor_product` | `텐서곱` | `ok` | 0 | 0 | `26C0AF0A26B6B54C6C7A533831A0AF280EE798DFEDDD55D120502DC24DA31CB2` | https://export.arxiv.org/api/query?search_query=all%3A%22%ED%85%90%EC%84%9C%EA%B3%B1%22&start=0&max_results=5 |
| `ko_localization` | `국소화` | `ok` | 0 | 0 | `9708F7145D851A48B166794D9C90342E570D775450E26649CCEB9AA038335636` | https://export.arxiv.org/api/query?search_query=all%3A%22%EA%B5%AD%EC%86%8C%ED%99%94%22&start=0&max_results=5 |

## PDF Fallback HEAD Probes

| ID | Status | Content-Type | Content-Length | Last-Modified | Local SHA256 | URL |
| --- | --- | --- | ---: | --- | --- | --- |
| `zh_pdf_ecnu_commutative_algebra` | `head_ok` | `application/pdf` | 1990891 | `Fri, 16 Jun 2023 01:02:54 GMT` | `C84AC610F21076DF2EC3AB6737D0713D1C84D3A84B38D2FAC42EAFEB3760C862` | https://math.ecnu.edu.cn/~rdu/years/ca%20book/main.pdf |
| `zh_pdf_hfut_group_representation` | `head_ok` | `application/pdf` | 1100406 | `Sun, 21 Sep 2025 14:53:06 GMT` | `01C390945C8795BF481E6B429B20579751075C6C712736669FCFE5854AB53C49` | https://faculty.hfut.edu.cn/_resources/group1/M00/00/1A/rB_zR2jQEVKARzGGABDKdnVFJ60618.pdf |
| `ja_pdf_kurims_mukai_hilbert14` | `head_ok` | `application/pdf` | 1506397 | `Mon, 13 Sep 2010 05:03:28 GMT` | `615FB345BB140048F2F31B0D8684B654E446ED5DEB140D63DAAF692A5BBBEF25` | https://www.kurims.kyoto-u.ac.jp/~kenkyubu/kokai-koza/H16-mukai.pdf |
| `ja_pdf_nagoya_reflection_invariants` | `head_ok` | `application/pdf` | 47952 | `Wed, 31 May 2017 09:31:58 GMT` | `3E3A5B863DC8E8F6791DA4DFB560250293259675F35417DC7FE043FB9F3C8E6E` | https://www.math.nagoya-u.ac.jp/~yanagida/edu/17S/20170601.pdf |
| `ja_pdf_nagoya_finite_group_representation` | `head_ok` | `application/pdf` | 178281 | `Wed, 08 Oct 2025 15:45:19 GMT` | `756D738627E00BDA79A39D4E1637D57FC6E85524A3054CF650806EAA64190D78` | https://www.math.nagoya-u.ac.jp/~yanagida/edu/25W/1009.pdf |

## Decisions And Boundaries

- Fixed-commit TeX witness URLs were re-fetched and hash-compared where available.
- Korean addendum default-branch raw TeX URLs were probed as route-only provenance, not edition evidence.
- GitHub and CTAN license signals are endpoint metadata only, not redistribution clearance or native/public approval.
- arXiv exact-phrase rechecks remain source-discovery telemetry and do not override local TeX/source shelves.
- PDF HEAD checks verify endpoint/provenance only; local SHA256 remains the evidence hash.
- Unresolved: Repositories with no GitHub API license remain license-review blockers.
- Unresolved: Any raw default-branch Korean hash mismatch requires pinning an exact commit before stronger evidence use.
- Unresolved: PDF rows remain fallback/internal provenance until explicit license/access clearance is recorded.
- Unresolved: No probe closes tensor product, localization, Harish-Chandra, abstract algebra, modern algebra, native review, or glossary gates.
