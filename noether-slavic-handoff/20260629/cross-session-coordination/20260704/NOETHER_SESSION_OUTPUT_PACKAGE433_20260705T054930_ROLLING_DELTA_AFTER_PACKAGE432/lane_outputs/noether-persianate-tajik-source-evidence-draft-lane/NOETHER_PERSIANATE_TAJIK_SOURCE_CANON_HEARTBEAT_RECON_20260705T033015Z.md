# Noether Persianate/Tajik Source-Canon Heartbeat Recon

Generated: 2026-07-05T03:30:15Z heartbeat pass

Status: draft/non-canonical source-canon provenance note. Not native reviewed. Not a terminology approval. No license clearance. No gate promotion. No Git push.

## Scope

This pass targeted the thin `prs_AF` source shelf, prioritizing direct Dari/Afghan Persian mathematical source witnesses over translation expansion. The search focused on Afghan university PDFs for algebra, linear algebra, and adjacent algebraic/discrete-mathematics vocabulary.

## Searches Rechecked

| Query/channel | Observed result | Routing |
| --- | --- | --- |
| Web: `site:ecampus-afghanistan.org/wp-content/uploads filetype:pdf جبر دری افغانستان` | Reconfirmed the already-cached eCampus `Algebra - Abdullah Momand` direct PDF. | Existing primary `prs_AF` algebra row remains current. |
| Web: `جبر خطی افغانستان filetype:pdf` | Surfaced bibliography/catalog context and Afghan PDF hits, but not a clean new Dari linear-algebra source package. | No TeX/source or new linear-algebra row from this query alone. |
| Web: `site:ku.edu.af/sites/default/files filetype:pdf جبر خطی` / `Linear Algebra پوهنتون کابل` | Surfaced Kabul University `Discrete-mathematics.pdf`, an Afghan Arabic-script PDF with chapters on graphs, relations, partial orders/networks/lattices, matrices, and Boolean algebra. | Cached and added as a `prs_AF` Level B provenance row. |
| HTTP HEAD: Kabul University PDF | Public 200 response, `application/pdf`, `Content-Length` 5066741, `Last-Modified` Sun, 25 May 2025 14:55:12 GMT. | Access signal recorded; no open-license clearance claimed. |

## Added Cached Witness

- `source_canon_witness_cache_20260704/prs_af_kabul_university_discrete_mathematics_2023-11.pdf`
  - URL: https://ku.edu.af/sites/default/files/2023-11/Discrete-mathematics.pdf
  - SHA256: `7FFE47055B54932151A862A1976D1D99AA1D30D241ED813753F6007ADD2AB3D4`
  - Bytes: 5066741
- `source_canon_witness_cache_20260704/prs_af_kabul_university_discrete_mathematics_2023-11.pdftotext.txt`
  - SHA256: `3C69812198A648F1518AC47626316BC2F1C7386AA5E5D7AA7097D2A431D0A24A`
  - Bytes: 428878

## Local Evidence

Text extraction includes Kabul/Afghanistan context: the introduction refers to teaching in the Computer Science Faculty departments of Kabul University and other Afghan universities. Local `rg` sanity counts include `ست` 1834, `گراف` 927, `رابطه` 230, `بول` 151, `ماتريس` 99, `جبر` 68, `شبكه` 60, `هم ارزی` 7, and `پوهنتون` 3. The extraction contains bidi marks and Arabic-script variants, so counts are provenance aids, not reviewer decisions.

## Current Effect

- Added `prs_af_kabul_university_discrete_mathematics_pdf` to the Markdown and JSON witness tables as a Level B PDF/course-note provenance witness.
- Updated the source-cache checksum sidecar with the PDF and text hashes.
- This strengthens `prs_AF` source-canon coverage for relation/equivalence, lattice/network, Boolean algebra, matrix, graph, and set vocabulary.
- It does not close the `prs_AF` TeX/source-package gap or invariant-theory gap.
- It does not authorize `fa_IR` or `tg_Cyrl_TJ`.

## Boundaries

- No translation expansion.
- No accepted terminology.
- No native review or canonical approval claim.
- No license-clearance claim.
- No gate promotion.
- No Tajik row promotion.
- No Git push.
