# Noether Persianate/Tajik Source-Canon Heartbeat Recon - 2026-07-05T11:24:16Z

Status: draft/non-canonical source-corpus provenance note. Not native reviewed. Not a terminology approval. No license clearance. No gate promotion. No Git push.

## Focus

The heartbeat requested source-canon-first work for `fa_IR`, `prs_AF`, and `tg_Cyrl_TJ`. This pass targeted the still-thin `prs_AF` direct linear-algebra shelf, especially Afghan/Dari bibliographic routes for source witnesses that may later support translation or terminology review.

## New Cached Evidence

- Cached Khatam al-Nabieen University OPAC class-page HTML for QA155/linear algebra records:
  - URL: https://library.knu.edu.af/opac/index.php?cls_plan=1&id=2088&lvl=class_nbr_see
  - Local path: `source_canon_witness_cache_20260704/prs_af_knu_opac_ghori_linear_algebra_record_2088.html`
  - SHA256: `BF92AE49DE4DF72B32DD5FA36C8D447DC5B9791B229FF724373A1E1E557B46B8`
  - Size: 59592 bytes
- Cached the KNU electronic-document viewer HTML exposed through `digi_doc.php?digcopy_id=42`:
  - URL: https://library.knu.edu.af/opac/digi_doc.php?digcopy_id=42
  - Local path: `source_canon_witness_cache_20260704/prs_af_knu_ghori_linear_algebra_record_8809_viewer.html`
  - SHA256: `631FFBAD8ECE45BCB10E3593831F0548D73F27AF97EC83D08A72BB624E3D4D3D`
  - Size: 17241 bytes

## What The OPAC Shows

- The OPAC class page contains a Kabul-published Afghan/Persian linear-algebra printed record:
  - Title: `الجبر خطی (1396)`
  - Authors: `پوهاند دکتر محمد انور غوری` and `پوهندوی محمد خان حیدری`
  - Publisher line: `کابل : سعید`
  - Language: `فارسی`
  - Subject: `جبر خطی`
- The same OPAC class page also contains a separate electronic record:
  - Title: `جبر خطی`
  - Authors/translators: Hoffman/Kunze, translated by Jamshid Farshidi
  - Publisher line: Tehran university publishing context
  - Language metadata: `فارسی`, original language English
  - Electronic attachment label: `8809.PDF`
- The cached viewer HTML exposes `DEFAULT_URL = './temp/8809.pdf'`.

## Access Gap

The apparent PDF route was probed but not promoted. A HEAD request indicated a PDF response, yet the actual file retrieved in this pass was an invalid binary/null placeholder that could not be parsed by PDF tooling. That failed binary was removed from the cache. Only the OPAC HTML and viewer HTML are retained.

Result: the new row is `C/Gap` source-routing/provenance, not a source-text witness. It does not anchor terms and does not close the `prs_AF` TeX/PDF source gap.

## Additional Route Leads Not Promoted

- eCampus/MoHE curriculum PDFs surfaced as possible Afghan university bibliography routes for linear algebra, including references to Ghori/Haidari, Momand, Baqi, and Iranian Strang translations. These were not cached or promoted in this pass because the KNU OPAC route already supplied a concrete Afghan library record, and the curriculum PDFs would be bibliography/supporting context rather than direct mathematical source text.
- Aksos bookstore/product pages surfaced for Afghan linear-algebra books. These remain commercial catalog leads only; no source text or license/open-access evidence was found here.

## Updates Made

- Added `prs_af_knu_linear_algebra_opac_records` to `NOETHER_PERSIANATE_TAJIK_SOURCE_CANON_WITNESS_TABLE_20260704.md` and `.json`.
- Added the two cached KNU HTML hashes to `NOETHER_PERSIANATE_TAJIK_SOURCE_CANON_WITNESS_CACHE_20260704.sha256`.
- Updated the durable run log and artifact manifest/checksum sidecars for the new source-canon heartbeat pass.

## Boundaries

- `fa_IR`, `prs_AF`, and `tg_Cyrl_TJ` remain separate.
- The Afghan Ghori/Haidari OPAC record does not authorize Iranian Persian or Tajik terminology.
- The Iranian/Tehran Hoffman-Kunze translation record held in the KNU OPAC does not authorize Afghan Dari register.
- Tajik Cyrillic remains zero promoted term rows and source-discovery only.
- Reviewer packet population: false.
- Native review: false.
- Term approval: false.
- Translation expansion/completion claim: false.
- License clearance: false.
- Gate promotion: false.
- Git push: false.
