# Noether Persianate/Tajik Source-Canon Heartbeat Recon - 2026-07-05T12:59:11Z

Status: draft/non-canonical source-corpus provenance note. Not native reviewed. Not a terminology approval. No license clearance. No gate promotion. No Git push.

## Focus

This heartbeat targeted the `fa_IR` field/Galois source-canon gap. The Persianate/Tajik translation corpus already contains Galois/extension material, while the source-canon table had stronger ring/module and representation witnesses than explicit field/Galois routing.

## Candidate Checks

- University of Tehran Science Faculty candidate for formal Lubin-Tate groups/local class field theory:
  - URL: https://science.ut.ac.ir/documents/438200/728178/Mohammad%2BMasoud%2BAhmadi-Ghadermarzi.Math.pdf/eb85c7ac-fb73-14fd-8a3b-5773d1de7feb?download=true&t=1710087617244
  - Result: fetch returned a 6078-byte HTML transfer/interstitial, not a PDF.
  - Local marker: `source_canon_witness_cache_20260704/fa_ut_formal_lubin_tate_local_class_field_theory_candidate_interstitial.html`
  - SHA256: `E0FFB943400D7875FE72F72ACC3AF0A19658B5C930B790A610C5A49341B23586`
- ResearchGate candidate for `نظریه میدان‌های رده‌ای`:
  - URL: https://www.researchgate.net/profile/Arash-Rastegar/publication/376714350_nzryh_mydanhay_rdh_ay/links/65845c4e6f6e450f198d79b5/nzryh-mydanhay-rdh-ay.pdf
  - Result: direct fetch blocked with access code 1020; no local file retained.

These are recorded as access gaps only, not source-text evidence.

## New Cached Witness

- Cached Isfahan University of Technology Mathematics Department curriculum PDF:
  - URL: https://mathdept.iut.ac.ir/sites/mathdept/files/Site/%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D9%87%20%D8%B3%D9%87%20%D9%81%D8%B5%D9%84%DB%8C%20%D8%AF%D8%A7%D9%86%D8%B4%DA%A9%D8%AF%D9%87%D9%94%20%D8%B1%DB%8C%D8%A7%D8%B6%DB%8C_2.pdf
  - Local PDF: `source_canon_witness_cache_20260704/fa_iut_mathematics_curriculum_field_galois_syllabus.pdf`
  - PDF SHA256: `E9F77D2B8B83136980D86E3DC1CF4D70F5DD648352BA0E4DEDF150BE1D6D68C8`
  - PDF size: 4052966 bytes
- Created UTF-8 `pdftotext -layout` extraction:
  - Local text: `source_canon_witness_cache_20260704/fa_iut_mathematics_curriculum_field_galois_syllabus.pdftotext.txt`
  - Text SHA256: `0C9DDD45EDABB82285882DFBF617B085BC5CDAED7FBD80D126F2A24A98610E66`
  - Text size: 782283 bytes

## Evidence Observed

The extraction has explicit syllabus language for `نظریه گالوا`, finite fields, field extensions, Galois groups, splitting fields, normal extensions, separable extensions, radical extensions, rings, polynomial rings, ideals, and fields.

Local sanity counts:

| Pattern | Count |
| --- | ---: |
| `نظریه گالوا` | 6 |
| `گالوا` | 9 |
| `نظریه میدان` | 5 |
| `میدان` | 167 |
| `توسیع` | 12 |
| `حلقه` | 61 |
| `دامنه صحیح` | 3 |
| `رادیکال` | 2 |
| `شکافنده` | 1 |

## Updates Made

- Added `fa_iut_mathematics_curriculum_field_galois_syllabus_pdf` to the Markdown/JSON witness tables as Level `B/C` fa_IR curriculum/source-routing provenance.
- Added `fa_class_field_theory_pdf_access_gap` as an explicit advanced field/Galois PDF access gap.
- Added IUT PDF/text and UT interstitial hashes to the cache checksum sidecar.
- Updated the durable run log and artifact manifest/checksum sidecars.

## Boundaries

- The IUT curriculum PDF is source-routing/curriculum provenance only, not a source textbook/archive or term approval.
- The UT and ResearchGate class-field-theory candidates remain access gaps, not evidence.
- `fa_IR`, `prs_AF`, and `tg_Cyrl_TJ` remain separate.
- Tajik Cyrillic remains zero promoted term rows and source-discovery only.
- Reviewer packet population: false.
- Native review: false.
- Term approval: false.
- Translation expansion/completion claim: false.
- License clearance: false.
- Gate promotion: false.
- Git push: false.
