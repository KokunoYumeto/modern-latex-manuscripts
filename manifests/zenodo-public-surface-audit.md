# Zenodo Public Surface Audit

Generated: 2026-05-27T15:35:59.599022+00:00

Purpose: check the reader-facing Zenodo records for human titles, clean metadata, private-name leakage, and rough/internal top-level filenames. Legacy records are retained for preservation/version history but should not be treated as the preferred front door.

| Lane | Record | Status | Files | Rough Top-Level Names | Rough Metadata | Private Leak | Public Role |
|---|---:|---|---:|---:|---|---|---|
| main_landing_bulk_preservation | [20410262](https://zenodo.org/records/20410262) | OK | 100 | 100 | no | no | current front-facing |
| ega_working_translation | [20414354](https://zenodo.org/records/20414354) | OK | 13 | 0 | no | no | current front-facing |
| sga_working_translation | [20414657](https://zenodo.org/records/20414657) | OK | 24 | 0 | no | no | current front-facing |
| non_european_multilingual | [20413193](https://zenodo.org/records/20413193) | OK | 60 | 0 | no | no | current front-facing |
| heinrich_weber | [20414684](https://zenodo.org/records/20414684) | OK | 5 | 0 | no | no | current front-facing |
| emmy_noether | [20414682](https://zenodo.org/records/20414682) | OK | 4 | 0 | no | no | current front-facing |
| deligne_clean_current | [20414959](https://zenodo.org/records/20414959) | OK | 93 | 0 | no | no | current front-facing |
| classical_algebra_arithmetic | [20414788](https://zenodo.org/records/20414788) | OK | 23 | 0 | no | no | current front-facing |
| deligne_legacy_superseded | [20410854](https://zenodo.org/records/20410854) | OK | 93 | 93 | yes | no | legacy/superseded preservation |
| gauss_legacy_superseded | [20411258](https://zenodo.org/records/20411258) | OK | 9 | 9 | yes | no | legacy/superseded preservation |

## Notes

- The clean current front-facing author/corpus records are EGA, SGA, Non-European mathematics, Weber, Noether, Deligne, and Classical algebra/arithmetic.
- The main landing record intentionally still contains rough inherited top-level filenames because it is the cumulative bulk preservation surface; the metadata points readers to cleaner author/corpus records.
- The old Deligne record is superseded by the clean current Deligne record `20414959`.
- The old Gauss record is superseded for public browsing by the Classical algebra/arithmetic record `20414788`, where the Gauss PDFs use human-readable names.

## Rough Filename Examples

### main_landing_bulk_preservation (20410262)
- `80_metadata__v22_sga_batch004_reader_qc_summary.json`
- `10_artifacts__landau_vorlesungen_band1.zip`
- `10_artifacts__landau_vorlesungen_band2.zip`
- `00_pdf__weber_pages.pdf`
- `00_pdf__non_eu__brahmagupta_brahmasphutasiddhanta_pt1.pdf`
- `00_pdf__non_eu__li_ye_ceyuan_haijing_fenlei_shishu.pdf`
- `00_pdf__landau_analytische_geometrische_zahlentheorie.pdf`
- `00_pdf__non_eu__yang_hui_xiangjie_jiuzhang.pdf`
- `00_pdf__sga7_2_working_latex_compilation.pdf`
- `10_artifacts__02-hecke-vorlesungen.zip`
- `10_artifacts__kimi7_nonscan_refined_clean.zip`
- `00_pdf__non_eu__zhu_shijie_suanxue_qimeng.pdf`

### deligne_legacy_superseded (20410854)
- `00_pdf__deligne_p087_orig.pdf`
- `00_pdf__deligne_p050_orig.pdf`
- `00_pdf__deligne_p009_orig.pdf`
- `00_pdf__deligne_p043_orig.pdf`
- `00_pdf__deligne_p023_orig.pdf`
- `00_pdf__deligne_p056_orig.pdf`
- `00_pdf__deligne_p059_orig.pdf`
- `00_pdf__deligne_p030_orig.pdf`
- `00_pdf__deligne_p017_orig.pdf`
- `00_pdf__deligne_p027_orig.pdf`
- `00_pdf__deligne_english_ready_and_working_translations_combined.pdf`
- `00_pdf__deligne_p003_orig.pdf`

### gauss_legacy_superseded (20411258)
- `00_pdf__gauss_werke_band11_part1.pdf`
- `00_pdf__gauss_werke_band03.pdf`
- `00_pdf__gauss_werke_band01.pdf`
- `80_metadata__gauss_werke_summary.json`
- `00_pdf__gauss_werke_individual_papers.pdf`
- `00_pdf__gauss_werke_band07.pdf`
- `00_pdf__gauss_werke_band01_alternate.pdf`
- `00_pdf__gauss_werke_band02.pdf`
- `10_artifacts__gauss_werke_sources_audits.zip`

