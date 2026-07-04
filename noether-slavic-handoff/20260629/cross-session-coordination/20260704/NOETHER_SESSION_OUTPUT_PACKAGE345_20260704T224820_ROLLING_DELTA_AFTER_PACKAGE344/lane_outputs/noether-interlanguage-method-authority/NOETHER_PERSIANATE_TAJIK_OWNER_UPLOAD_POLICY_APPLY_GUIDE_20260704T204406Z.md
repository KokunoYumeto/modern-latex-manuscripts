# Persianate/Tajik Owner Upload Policy Apply Guide

Generated UTC: 2026-07-04T20:44:06Z

Status: Session D coordination guide for `D-FIELD-REPAIR-001`. This is not an owner-lane edit, not owner-lane acceptance, not Git push authority, not source-license clearance, not payload eligibility, not native review, not community consent, not canonical approval, not term approval, not bridge approval, not gate promotion, and not completion.

Owner lane: `noether-persianate-tajik-source-evidence-draft-lane`

Recommended field to add per row: `upload_policy`

Optional companion field: `upload_policy_rationale`

Allowed conservative values used here:

- `manifest_only_no_payload_until_license_or_B3_review`
- `conditional_payload_requires_B3_license_attribution_review`
- `blocked_not_uploaded_failed_fetch`
- `gap_only_no_payload`

Source table inspected:

- `NOETHER_PERSIANATE_TAJIK_SOURCE_CANON_WITNESS_TABLE_20260704.json`, SHA-256 `C75EF869F9AF82C920975A4F0F3FB80C362178E8055C40E7EA007A6DDC7B14BB`
- `NOETHER_PERSIANATE_TAJIK_SOURCE_CANON_WITNESS_TABLE_20260704.md`, SHA-256 `2AE8A8288EA2227AD293F4F38CB9A1CFE4C7CBF3ACFF339AC6B447DDB085EB87`

## Row-Level Apply Guide

| Row | Lane | Source title | Source type | URL or gap | Hash or gap | License/access signal | Proposed `upload_policy` |
| ---: | --- | --- | --- | --- | --- | --- | --- |
| 1 | `fa_IR` | Advanced Algebra course PDF | `pdf` | `https://people.iut.ac.ir/sites/default/files/users/behboodi/course_files/advanced_algebra_dr._behboodi.pdf` | `B2BEDB1AA29693935B09445ED8D90910F27BDEEA7CA2F0BB5E3394F0150FDA40` | university-hosted PDF; no open license found | `manifest_only_no_payload_until_license_or_B3_review` |
| 2 | `fa_IR` | PNU ring/module book preview | `pdf` | `https://press.pnu.ac.ir/book_30094.pdf` | `62FC1509AA543B70F2EFB461DA1871A3978D194DD8D79DFC480319B02702ED07` | publisher PDF/preview; no open license found | `manifest_only_no_payload_until_license_or_B3_review` |
| 3 | `fa_IR` | Noncommutative prime ideals thesis PDF | `pdf` | `https://shahroodut.ac.ir/fa/thesis/files/somefiles/sf_QA37.pdf` | `77C32EE8A31778858F2D2D05AC432661102B4E27A54ABA8BE0573DA299BFA335` | university thesis PDF; no open license found | `manifest_only_no_payload_until_license_or_B3_review` |
| 4 | `fa_IR` | Persian linear algebra 3Blue1Brown notes | `zip_source_archive` | `https://github.com/SireJeff/linear-algebra-3blue1brown-notes` | `4D93CE90754B28ECC743CE5BB1ED62F0325F99A38D52E90DECC10DD1C3FFF59C` | no standard open license found | `manifest_only_no_payload_until_license_or_B3_review` |
| 5 | `fa_IR` | Persian Noether-topic TeX/arXiv source package | `gap` | explicit gap: no Persian-language TeX/arXiv/source archive found | explicit gap: no hash | not applicable | `gap_only_no_payload` |
| 6 | `prs_AF` | Algebra - Abdullah Momand | `pdf` | `https://ecampus-afghanistan.org/wp-content/uploads/2021/10/Algebra-Abdullah-Momand.pdf` | `5145F1EFA0AB4275AD3CBF03C0016A3362D5D7A6EDE3444FDE512719E813D8F4` | eCampus textbook PDF; no open license found | `manifest_only_no_payload_until_license_or_B3_review` |
| 7 | `prs_AF` | eCampus 369 Afghan university textbook list | `html` | `https://ecampus-afghanistan.org/list-of-369-published-textbooks-for-afghan-universities/` | `E78A9FC816B597DA04F6817F93A77E3A6DDDBBD7A6F884BDBFDD4D8DEFAFAFAA` | page footer copyright; no open license found | `manifest_only_no_payload_until_license_or_B3_review` |
| 8 | `prs_AF` | Dari TeX/arXiv/invariant-theory source packages | `gap` | explicit gap: no Dari/Afghan Persian TeX/source archive found | explicit gap: no hash | not applicable | `gap_only_no_payload` |
| 9 | `tg_Cyrl_TJ` | Алгебраи хаттӣ | `mediawiki_raw_wikitext` | `https://tg.wikipedia.org/wiki/Алгебраи_хаттӣ` | `FBF1074CC8AFEAA2681E5D548AB4CACEACED30A85D34F5072F4AF8F690C355A3` | CC BY-SA per Wikimedia page/footer terms | `conditional_payload_requires_B3_license_attribution_review` |
| 10 | `tg_Cyrl_TJ` | TNU 2017 conference proceedings | `pdf` | `https://tnu.tj/ilm/mater2017.pdf` | `073D7CFEF645FF8F5482AE069141EAE8EC0405BB6FE6BB3E5F395C73D0535810` | university PDF; no open license found | `manifest_only_no_payload_until_license_or_B3_review` |
| 11 | `tg_Cyrl_TJ` | TGPU ring/field PDF candidate | `failed_pdf_fetch_404_html` | `https://vestnik.tgpu.tj/Content/files/JournalsPDF/a5b992cf-3aca-4997-9e59-11bd0e34dc3d.pdf` | `12EAFE6435F4C02A65306F1CF02F26798F9A46C3074608F51B51014C07FA6580` | failed fetch; no usable license/source | `blocked_not_uploaded_failed_fetch` |
| 12 | `tg_Cyrl_TJ` | Tajik abstract algebra / TeX source package | `gap` | explicit gap: no reliable Tajik Cyrillic source package isolated | explicit gap: no hash | not applicable | `gap_only_no_payload` |

## Apply Requirements

The owner lane should add the policy field in both Markdown and JSON, or publish a superseding witness table that contains equivalent policy fields.

Minimum owner-lane acceptance evidence:

- Each of the 12 rows has an explicit upload/distribution policy.
- Policy values distinguish manifest-only records, conditional B3 license/attribution review, failed-fetch blocked records, and source gaps.
- The repaired table preserves existing source URLs, local paths, hashes, topic tags, language evidence, license/access signals, and non-claim boundaries.
- The repaired table clearly says that policy values do not create source-license clearance, payload eligibility, native review, community consent, canonical approval, term approval, bridge approval, gate promotion, or translation completion.

Until that owner-lane artifact exists, Session D should treat all 12 rows as incomplete for source-canon publication-policy coverage, even though many rows have useful provenance evidence.
