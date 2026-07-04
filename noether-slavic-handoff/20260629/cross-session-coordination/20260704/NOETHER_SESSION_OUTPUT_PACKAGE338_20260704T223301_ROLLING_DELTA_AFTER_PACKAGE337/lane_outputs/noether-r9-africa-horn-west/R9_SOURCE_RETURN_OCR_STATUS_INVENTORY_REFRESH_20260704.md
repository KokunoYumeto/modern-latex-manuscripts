# R9 Source-Return OCR Status Inventory Refresh - 2026-07-04

This artifact refreshes the R9 Africa/Horn/West Africa source-return and OCR
inventory from the current local pass2 source manifests. It is source-canon
maintenance only, not translation evidence.

Boundary: this inventory does not approve translation, terminology,
native/community review, canonical status, source license clearance, gate
promotion, completion, package upload, or Git push.

Machine-readable ledger:

`R9_SOURCE_RETURN_OCR_STATUS_INVENTORY_REFRESH_20260704.csv`

## Inputs

Local source manifests under:

`C:/Users/memo_/Documents/Codex/2026-06-09/could-you-look-online-for-me/work/noether-slavic-canonical/sources/non_slavic_reference_corpus/`

Manifest roots inspected:

- `20260703T162646Z_r9_hausa_direct_math_source_return_pass2`
- `20260703T162950Z_r9_igbo_glossary_textbook_source_return_pass2`
- `20260703T164546Z_r9_amharic_pass2`
- `20260703T165443Z_r9_afar_pass2`
- `20260703T170417Z_r9_somali_oromo_pass2`
- `20260703T172503Z_r9_tigrigna_tigrinya_pass2`

No raw source bodies were copied into this artifact.

## Status Summary

| Target | Manifest Rows | Local PDF Rows | Text/OCR Status | Current Boundary |
| --- | ---: | ---: | --- | --- |
| Hausa | 11 | 0 | `none:11` | Route metadata only; no local source body. |
| Igbo | 8 | 0 | `none:8` | Commercial/context routes only; no source-cleared Igbo body. |
| Amharic | 48 | 48 | `font_garbled_or_non_unicode_extraction:44; extractable_ethiopic_text:3; empty_extraction:1` | Large PDF shelf, OCR/font-map blocked. |
| Afar | 16 | 5 | `extracted_text:5; none:11` | Context/report PDFs only; no direct Afar math corpus. |
| Oromo | 84 | 83 | `extractable_latin_text:70; weak_or_empty_text_extraction:13; none:1` | Strong PDF shelf, but proof/register and source-permission boundary remain. |
| Somali | 84 | 74 | `extractable_latin_text:62; weak_or_empty_text_extraction:12; none:10` | Strong PDF shelf, but proof/register and source-permission boundary remain. |
| Tigrigna/Tigrinya | 84 | 82 | `extractable_ethiopic_text:53; weak_or_empty_text_extraction:29; none:2` | Strong PDF shelf plus separate number/register source package; algebra/proof rows still need render/review gates. |

## Next Source-Return Work

- Hausa: obtain source-owner content or licensed source-body route for the
  Samab/Amsoshi book/app material.
- Igbo: obtain source-cleared MBIDO/book/glossary text or an explicit
  reviewer/source return.
- Amharic: prioritize OCR/font-map repair and page-render comparison for the
  44 font-garbled rows.
- Afar: search for direct Afar/Qafar math source or transcript-bearing material;
  current PDFs are context evidence only.
- Oromo and Somali: queue proof/register and source-permission review for the
  extractable Latin shelves, and isolate weak/empty extraction rows.
- Tigrigna/Tigrinya: keep source-package number/register evidence separate from
  school-PDF OCR evidence; run render/text comparison before any corpus use.
