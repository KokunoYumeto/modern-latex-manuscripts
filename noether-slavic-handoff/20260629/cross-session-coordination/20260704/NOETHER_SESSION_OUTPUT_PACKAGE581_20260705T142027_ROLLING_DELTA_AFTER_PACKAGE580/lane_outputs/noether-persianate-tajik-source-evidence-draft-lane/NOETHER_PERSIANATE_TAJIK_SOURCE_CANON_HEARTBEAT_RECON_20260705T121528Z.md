# Noether Persianate/Tajik Source-Canon Heartbeat Recon - 2026-07-05T12:15:28Z

Status: draft/non-canonical source-corpus provenance note. Not native reviewed. Not a terminology approval. No license clearance. No gate promotion. No Git push.

## Focus

This heartbeat continued `prs_AF` source-canon work after the KNU OPAC pass. The target was official Afghan curriculum/bibliography evidence for linear-algebra source routing, not translation-slice expansion or terminology approval.

## New Cached Evidence

- Cached the Afghanistan MoHE/eCampus revised curriculum PDF for the Inorganic Industrial Engineering Department:
  - URL: https://ecampus-afghanistan.org/wp-content/uploads/2023/02/Z-Curriculum-of-Inorganic-Industrial-Engineering-Department.pdf
  - Local PDF: `source_canon_witness_cache_20260704/prs_af_ecampus_mohe_inorganic_industrial_engineering_curriculum_2023.pdf`
  - PDF SHA256: `B4C042861E3A91F3FBDBE6C8BC10DC21A86251C846D6F2A00A83834D4361C9B8`
  - PDF size: 6953645 bytes
- Created a UTF-8 `pdftotext -layout` extraction:
  - Local text: `source_canon_witness_cache_20260704/prs_af_ecampus_mohe_inorganic_industrial_engineering_curriculum_2023.pdftotext.txt`
  - Text SHA256: `479D7562E7CB92D4C94EBF30FB07FE3D0E449F1970E56056D6E6BFEC74D77E6D`
  - Text size: 1574619 bytes

## Evidence Observed

The extracted text includes an official curriculum/bibliography block with linear-algebra references:

- `استرانگ، گیلبرت ... جبر خطی و کاربرد های آن`
- `باقی، عبدالحمید (1392). الجبر خطی. کابل: عازم`
- `غوری، محمد انور و محمد خان حیدری (1396). الجبر خطی. کابل: سعید`
- `مهمند، عبدالله (1393). الجبر خطی. کابل: سعید`

Local sanity counts over the extracted text:

| Pattern | Count |
| --- | ---: |
| `الجبر خطی` | 3 |
| `جبر خطی` | 5 |
| `وکتور` | 18 |
| `ماترکس` | 1 |
| `غوری` | 4 |
| `حیدری` | 1 |
| `باقی` | 3 |
| `مهمند` | 1 |

## Classification

Added `prs_af_ecampus_mohe_inorganic_industrial_engineering_curriculum_pdf` as a Level `B/C` curriculum/source-routing witness. It is useful for Afghan university linear-algebra bibliography and course-register provenance, but it is not a Noether/invariant-theory source package, not TeX/source, and not a term anchor.

## Updates Made

- Updated `NOETHER_PERSIANATE_TAJIK_SOURCE_CANON_WITNESS_TABLE_20260704.md` and `.json`.
- Added the curriculum PDF and text hashes to `NOETHER_PERSIANATE_TAJIK_SOURCE_CANON_WITNESS_CACHE_20260704.sha256`.
- Updated the durable run log and artifact manifest/checksum sidecars.

## Boundaries

- `fa_IR`, `prs_AF`, and `tg_Cyrl_TJ` remain separate.
- The curriculum PDF does not authorize Iranian Persian or Tajik terminology.
- It does not replace direct Afghan/Dari mathematical source text or reviewer judgment.
- Tajik Cyrillic remains zero promoted term rows and source-discovery only.
- Reviewer packet population: false.
- Native review: false.
- Term approval: false.
- Translation expansion/completion claim: false.
- License clearance: false.
- Gate promotion: false.
- Git push: false.
