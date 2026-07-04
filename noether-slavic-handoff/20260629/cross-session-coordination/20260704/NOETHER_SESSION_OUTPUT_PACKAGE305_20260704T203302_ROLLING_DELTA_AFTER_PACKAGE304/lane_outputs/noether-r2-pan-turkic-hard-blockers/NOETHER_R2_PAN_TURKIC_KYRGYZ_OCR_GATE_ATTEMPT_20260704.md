# R2 Pan-Turkic Kyrgyz OCR Gate Attempt

Prepared: 2026-07-04

Status: source-canon OCR/provenance gate only. This artifact does not create translation output, does not promote a glossary term, does not create a Pan-Turkic bridge or pilot, does not claim native/community review, and does not claim canonical approval.

## Purpose

The full-capture machine-text scan left two Kyrgyz PDF witnesses as thin-text/OCR-gated sources:

- `CWS-KY-002`: Kaldybaev S.K. `Algebra 8 klass`, captured from `https://daramet.tm.kg/wp-content/uploads/2017/11/Kaldybaev-S.K.Algebra-8-klass.pdf`.
- `GCS-KY-002`: `Математикалык маалыматтама сөздүк`, captured from `https://www.okuma.kg/read/web/books/%D0%9C%D0%B0%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B0%D0%BB%D1%8B%D0%BA%20%D0%BC%D0%B0%D0%B0%D0%BB%D1%8B%D0%BC%D0%B0%D1%82%D1%82%D0%B0%D0%BC%D0%B0%20%D1%81%D3%A9%D0%B7%D0%B4%D2%AF%D0%BA%28okuma.kg%29_%D0%9C%D0%B0%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B0%2C%20%D0%9B%D0%BE%D0%B3%D0%B8%D0%BA%D0%B082.pdf`.

This slice attacks only that OCR gate, using source-level/provenance evidence and exact phrase scans. The earlier installed-language fallback OCR attempt with `rus+tgk+eng` timed out after 900 seconds and is rejected as partial; it is not used as evidence here.

## OCR Inputs And Outputs

Kyrgyz Tesseract data was not present in the installed OCR language stack, so a lane-local copy of official `tessdata_fast` Kyrgyz traineddata was downloaded and hashed:

| Asset | URL / local path | SHA-256 | Status |
|---|---|---|---|
| `kir.traineddata` | `https://raw.githubusercontent.com/tesseract-ocr/tessdata_fast/main/kir.traineddata`; `C:\Users\memo_\Documents\Codex\2026-07-04\noether-r2-pan-turkic-hard-blockers\outputs\tools\tessdata_20260704\kir.traineddata` | `9777956300900B528D26932CF80693F95E75143433FB851D567194BCC38A31AE` | Tooling/provenance asset only; no term authority claim. |
| `OCR-KY-CWS-002` OCR text | `C:\Users\memo_\Documents\Codex\2026-07-04\noether-r2-pan-turkic-hard-blockers\outputs\sources\kyrgyz_ocr_kir_fast_20260704\OCR-KY-CWS-002_daramet_algebra_8_klass_kir_fast_psm6_150dpi_ocr.txt` | `D4DB3471E8BEFC6E1BD0EF96429617C15F71B61B7B1E583935F6E002CCEA600A` | 104/104 pages OCRed with `kir`, `--psm 6`, 150 dpi. |
| `OCR-KY-GCS-002` OCR text | `C:\Users\memo_\Documents\Codex\2026-07-04\noether-r2-pan-turkic-hard-blockers\outputs\sources\kyrgyz_ocr_kir_fast_20260704\OCR-KY-GCS-002_okuma_math_reference_dictionary_kir_fast_psm6_150dpi_ocr.txt` | `8C71AC103322144A85771FA1090B7E72C7013241BACFEF7E509BD075CF447405` | 102/102 pages OCRed with `kir`, `--psm 6`, 150 dpi. |
| OCR inventory | `C:\Users\memo_\Documents\Codex\2026-07-04\noether-r2-pan-turkic-hard-blockers\outputs\sources\kyrgyz_ocr_kir_fast_20260704\kyrgyz_ocr_kir_fast_inventory_20260704.csv` | `726C99FA88BFF5894A207B48C5C2547B63C2E70A9940EDBFF2D68381638C6942` | Machine-readable OCR source/output inventory. |

Pages completed: `206/206`.

Machine-readable mirror: `outputs/NOETHER_R2_PAN_TURKIC_KYRGYZ_OCR_GATE_ATTEMPT_20260704.csv`

Capture hashes: `outputs/NOETHER_R2_PAN_TURKIC_KYRGYZ_OCR_GATE_CAPTURE_SHA256_20260704.txt`

## Exact Hard-Row Scan Result

The OCR text was scanned with exact raw matching and whitespace-normalized phrase matching. Exact hard-row hits remained zero.

| Source | Hard row | Variants scanned | Raw exact hits | Whitespace-normalized hits | Status |
|---|---|---:|---:|---:|---|
| `OCR-KY-CWS-002` | Kyrgyz Noetherian ring | 3 | 0 | 0 | No exact source row; blocker remains. |
| `OCR-KY-CWS-002` | Kyrgyz polynomial ring | 5 | 0 | 0 | No exact source row; blocker remains. |
| `OCR-KY-GCS-002` | Kyrgyz Noetherian ring | 3 | 0 | 0 | No exact source row; blocker remains. |
| `OCR-KY-GCS-002` | Kyrgyz polynomial ring | 5 | 0 | 0 | No exact source row; blocker remains. |

Exact variants scanned:

- Noetherian-ring variants: `Нётер шакеги`, `Нетер шакеги`, `Нөтер шакеги`.
- Polynomial-ring variants: `көп мүчөлөр шакеги`, `көп мүчөлөр алкагы`, `көп мүчө шакеги`, `полиномдор шакеги`, `полиномдор алкагы`.

## Context-Only Findings

The OCR text does contain Kyrgyz mathematical context, but context-only hits are not hard-row support:

| Source | Context phrase | Raw exact hits | Whitespace-normalized hits | Example |
|---|---|---:|---:|---|
| `OCR-KY-CWS-002` | `көп мүчө` | 9 | 9 | `L160: |2 Түшүнүктү | Бир мүчө жана көп мүчө|+}+ + +` |
| `OCR-KY-GCS-002` | `көп мүчө` | 16 | 18 | `L535: Безу теорема — Безу теоремасы. [(х) көп мүчөсүн` |
| `OCR-KY-GCS-002` | `алгебра` | 40 | 40 | `L77: А. т.— алгебралык туюнтма` |
| `OCR-KY-GCS-002` | `модуль` | 3 | 3 | `L151: Абсолютная величина (модуль) — абсолюттук чондук` |

No `шакек`, `идеал`, `Нётер`, or `Нетер` context-only hits were found in these two OCR outputs.

## Remaining Blockers

| Row | OCR-gate outcome | Next gate |
|---|---|---|
| Kyrgyz Noetherian ring | No exact OCR hit in the two thin-text Kyrgyz PDFs. | Exact local source row, reviewer return, TeX/source package, or another source-gated Kyrgyz corpus witness. |
| Kyrgyz polynomial ring | Polynomial base context exists, but no exact polynomial-ring OCR hit in the two thin-text Kyrgyz PDFs. | Exact local source row, reviewer return, TeX/source package, or another source-gated Kyrgyz corpus witness. |

This closes the specific two-PDF Kyrgyz OCR gate under current evidence; it does not close the whole Kyrgyz source-canon search and does not permit downstream term or translation use.

