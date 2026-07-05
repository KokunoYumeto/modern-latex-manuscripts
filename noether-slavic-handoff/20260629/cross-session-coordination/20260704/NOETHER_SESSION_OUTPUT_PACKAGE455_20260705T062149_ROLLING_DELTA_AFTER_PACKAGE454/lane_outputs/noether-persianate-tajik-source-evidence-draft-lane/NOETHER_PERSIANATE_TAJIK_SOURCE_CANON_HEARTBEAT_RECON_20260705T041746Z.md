# Noether Persianate/Tajik Source-Canon Heartbeat Recon

Generated: 2026-07-05T04:17:46Z heartbeat pass

Status: draft/non-canonical source-canon provenance note. Not native reviewed. Not a terminology approval. No license clearance. No gate promotion. No Git push.

## Scope

This pass first checked whether the newly improved `prs_AF` shelf had a cleaner direct Afghan linear-algebra source beyond the Kabul University discrete-mathematics PDF. It then rechecked source-format discovery for Persian/Farsi TeX/XePersian mathematical repositories because TeX/source archives are preferred over PDF fallback when they are real target-language witnesses.

## Searches Rechecked

| Query/channel | Observed result | Routing |
| --- | --- | --- |
| Web: `site:ku.edu.af/sites/default/files/2023-11 filetype:pdf Linear Algebra` and related Kabul University PDF searches | Returned the already-cached `Discrete-mathematics.pdf` plus unrelated English CS books and non-math Kabul University journal PDFs. | No new `prs_AF` linear-algebra row from this pass. |
| Web/GitHub: `site:github.com xepersian جبر حلقه`, `XePersian algebra حلقه میدان`, `usepackage{xepersian} جبر` | Surfaced `AlirezaKachouei/Linear-Algebra-Gilbert-Strang-Persian`, a public Persian/XePersian linear-algebra source repository. | Cached and added as an `fa_IR` Level A source-format provenance row. |
| GitHub API metadata | Repository is public, default branch `main`; no license metadata reported; updated/pushed 2025-07-28. | Access/license signal recorded; no license clearance. |

## Added Cached Witness

- `source_canon_witness_cache_20260704/fa_linear_algebra_gilbert_strang_persian_source_main.zip`
  - URL: https://github.com/AlirezaKachouei/Linear-Algebra-Gilbert-Strang-Persian
  - Download route: https://codeload.github.com/AlirezaKachouei/Linear-Algebra-Gilbert-Strang-Persian/zip/refs/heads/main
  - SHA256: `1956A3821B88F2AFDA31A0DA184988DDDED44751A44E48068E6A06FCA091437B`
  - Bytes: 1410262

## Local Evidence

ZIP inspection found 42 entries: 20 `.tex` files and 20 compiled PDFs. The TeX source scan found `xepersian` 20, `ماتریس` 941, `بردار` 447, `حاصل‌ضرب داخلی` 31, `جبر خطی` 24, `دترمینان` 14, `فضای برداری` 3, and `مقدار ویژه`/`مقادیر ویژه` 2 combined.

README signal: the repository describes itself as a Persian/Farsi translation of selected chapters from Gilbert Strang's "Linear Algebra and Its Applications", says each chapter includes `.tex` and `.pdf`, and warns that the original book is copyrighted and the project is non-commercial/educational. This is an access/license caution, not clearance.

## Current Effect

- Added `fa_linear_algebra_gilbert_strang_persian_tex_source` to the Markdown and JSON witness tables as a Level A TeX/source-archive provenance row.
- Updated the source-cache checksum sidecar with the ZIP hash.
- This strengthens `fa_IR` source-format coverage for linear-algebra register and XePersian source handling.
- It does not close the Persian Noether/invariant-theory TeX/source gap.
- It does not authorize `prs_AF` or `tg_Cyrl_TJ`.

## Boundaries

- No translation expansion.
- No accepted terminology.
- No native review or canonical approval claim.
- No license-clearance claim.
- No gate promotion.
- No Tajik row promotion.
- No Git push.
