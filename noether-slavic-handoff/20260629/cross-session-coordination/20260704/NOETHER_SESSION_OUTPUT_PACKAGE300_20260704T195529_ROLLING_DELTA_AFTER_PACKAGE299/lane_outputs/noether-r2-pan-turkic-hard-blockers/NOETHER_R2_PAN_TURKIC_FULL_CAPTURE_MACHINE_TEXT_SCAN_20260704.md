# R2 Pan-Turkic Full-Capture Machine-Text Scan

Prepared: 2026-07-04

Scope: machine-text extraction and exact phrase scan across the R2 Pan-Turkic source-canon corpus for Tatar (`tt`), Kyrgyz (`ky`), Turkmen (`tk`), and Uyghur (`ug`). This artifact extends the exact hard-row closure by scanning all current captured PDFs after `pdftotext` extraction, current HTML captures, and the older local source-canon witness files referenced by the main source-canon table.

This is source-corpus/provenance bookkeeping only. It does not promote translations, glossary terms, bridge forms, pilots, reviewer status, native/community review, or canonical approval.

Machine-readable files:

- Variant scan table: `outputs/NOETHER_R2_PAN_TURKIC_FULL_CAPTURE_MACHINE_TEXT_SCAN_20260704.csv`
- PDF extraction inventory: `outputs/NOETHER_R2_PAN_TURKIC_FULL_CAPTURE_PDF_TEXT_EXTRACTION_INVENTORY_20260704.csv`
- Derived-text checksum list: `outputs/NOETHER_R2_PAN_TURKIC_FULL_CAPTURE_MACHINE_TEXT_SCAN_SHA256_20260704.txt`

Derived text directory:

`outputs\sources\full_capture_machine_text_scan_20260704`

## Extraction Scope

PDF text extraction:

- Captured PDFs scanned: `12`
- `pdftotext` extraction files produced: `12`
- Derived text files plus inventory/stderr files checksummed: `14`
- One extraction produced stderr but still yielded substantial text: `GCS-TK-002_kitaphana_book_13_download.pdf`
- Two PDFs produced only thin machine text and remain OCR-gated:
  - `CWS-KY-002_daramet_algebra_8_klass.pdf`: 104 bytes of extracted text
  - `GCS-KY-002_okuma_math_reference_dictionary.pdf`: 102 bytes of extracted text

OCR/tool note:

- `pdftotext` is available and was used.
- `tesseract` is available, but installed language packs do not include Tatar, Kyrgyz, or Turkmen.
- `ocrmypdf` is not available.
- Therefore this artifact is a machine-text scan over extractable PDF text and captured HTML, not a complete image-PDF OCR proof.

## Scan Scope

Files included in exact phrase scan:

- `12` derived PDF text files
- `12` current HTML captures from `outputs\sources`
- `14` older local source-canon witness files referenced by `NOETHER_R2_PAN_TURKIC_SOURCE_CANON_WITNESS_TABLE_20260704.csv`
- Total scanned files: `38`

Exact phrase variants scanned:

- Tatar Noetherian ring: 3 variants
- Tatar polynomial ring: 4 variants
- Kyrgyz Noetherian ring: 3 variants
- Kyrgyz polynomial ring: 5 variants
- Turkmen Noetherian ring: 4 variants
- Turkmen polynomial ring: 5 variants
- Uyghur Noetherian ring: 1 exact phrase
- Uyghur polynomial ring: 1 exact phrase

Full variant-level rows are in the CSV.

## Scan Result Summary

| Language | Hard row | Variants scanned | Total hits | Hit files | Status |
|---|---:|---:|---:|---:|---|
| Tatar | Noetherian ring | 3 | 0 | 0 | Still blocked: no exact machine-text hit in the scanned corpus. |
| Tatar | Polynomial ring | 4 | 0 | 0 | Still blocked: no exact machine-text hit in the scanned corpus. |
| Kyrgyz | Noetherian ring | 3 | 0 | 0 | Still blocked: no exact machine-text hit in the scanned corpus. |
| Kyrgyz | Polynomial ring | 5 | 0 | 0 | Still blocked: no exact machine-text hit in the scanned corpus. |
| Turkmen | Noetherian ring | 4 | 0 | 0 | Still blocked: no exact machine-text hit in the scanned corpus. |
| Turkmen | Polynomial ring | 5 | 0 | 0 | Still blocked: no exact machine-text hit in the scanned corpus. |
| Uyghur | Noetherian ring | 1 | 4 | 2 | Candidate-only exact source-corpus hits; no promotion. |
| Uyghur | Polynomial ring | 1 | 2 | 1 | Candidate-only exact source-corpus hit; no promotion. |

## Nonzero Exact Hits

| ID | Language | Hard row | Exact phrase | Hits | Hit files | Status |
|---|---|---|---|---:|---:|---|
| MTS-UG-NR-001 | Uyghur | Noetherian ring | `نوئېتېر ھالقىسى` | 4 | 2 | Candidate-only source-corpus hits. Authority/license/native-domain review remains open. |
| MTS-UG-PR-001 | Uyghur | Polynomial ring | `كۆپ ئەزالىق ھالقا` | 2 | 1 | Candidate-only source-corpus hit. Authority/license/native-domain review remains open. |

The first Uyghur Noetherian-ring hit is in:

`C:\Users\memo_\Documents\Codex\2026-06-28\see-attached-you-do-prompt-d\outputs\sources\non_slavic_reference_corpus\20260701t234000z_pan_turkic_exact_hard_row_paced_retry\web_candidate_pages\ug_uygur_com_noetherian_ring_noeter_halqisi.html`

The first Uyghur polynomial-ring hit is in:

`C:\Users\memo_\Documents\Codex\2026-06-28\see-attached-you-do-prompt-d\outputs\sources\non_slavic_reference_corpus\20260701t234000z_pan_turkic_exact_hard_row_paced_retry\web_candidate_pages\ug_uygur_com_polynomial_ring_kop_ezaliq_halqa.html`

## Remaining Gates

| Gate | Current evidence | Next gate |
|---|---|---|
| Tatar exact Noetherian-ring / polynomial-ring rows | Zero exact phrase hits across widened machine-text scan. | Exact source row, reviewer return, or OCR-capable scan of relevant image-heavy sources. |
| Kyrgyz exact Noetherian-ring / polynomial-ring rows | Zero exact phrase hits across widened machine-text scan; two Kyrgyz PDFs remain thin-text/OCR-gated. | Exact source row, reviewer return, or Kyrgyz-capable OCR/source package. |
| Turkmen exact Noetherian-ring / polynomial-ring rows | Zero exact phrase hits across widened machine-text scan. | Exact source row, reviewer return, or Turkmen-capable OCR/source package. |
| Uyghur exact hard rows | Exact dictionary/source-corpus hits exist. | Authority/license/native-domain review or reviewer return before downstream use. |
| Target-cluster TeX/source package | No target-cluster TeX/LaTeX/arXiv/e-print/source archive found in prior source-package gate slice. | Continue source-package search; any future package must be captured, hashed, and target-language-specific. |

## Handling Rules

- Treat this artifact as exact machine-text scan evidence only.
- Do not infer exact hard-row terms from adjacent polynomial, ring, module, group, or algebra witnesses.
- Do not use candidate-only Uyghur hits as translation output, glossary authority, bridge construction, pilot support, native-review evidence, or canonical approval.
