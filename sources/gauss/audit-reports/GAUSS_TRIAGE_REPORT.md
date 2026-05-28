# Gauss Werke Triage Report

**Generated:** 2026-05-27 12:55 Europe/Berlin
**Source:** Gauss source packet from the current transcription corpus (1,074 MB)
**Auditor:** Local automated triage pass

## Executive Summary

**118 TeX files, 118 PDFs, 10 Gauss volumes, 3,675 total pages.**

The current refinement round did substantial work. 100 of 118 TeX files score grade A (good LaTeX). The remaining 18 are split between grade C (needs repair, 6 files) and grade D (OCR dump, 12 files). The D-grade files are concentrated in **Band 06** (6 of 18 chapters) and **Band 04/05** (2 each).

**Blocking compile issue:** All files using `\usepackage{microtype}` fail on the local TeX install. Fix is trivial — remove or guard the microtype import. With that fix, all 5 test files compiled successfully.

## Volume-by-Volume Assessment

| Band | Chapters | Grade A | Grade C | Grade D | Avg Score | Verdict |
|------|----------|---------|---------|---------|-----------|---------|
| **Band 01** | 10 | 10 | 0 | 0 | 89.1 | READY — clean LaTeX, proper math |
| **Band 01 alt** | 11 | 10 | 1 | 0 | 80.9 | READY — one minor chapter needs review |
| **Band 02** | 11 | 10 | 0 | 1 | 75.9 | READY minus ch10 (81 MB oversized, likely scan-embedded) |
| **Band 03** | 11 | 11 | 0 | 0 | 88.1 | READY — all clean, best quality band |
| **Band 04** | 9 | 5 | 2 | 2 | -45.9 | MIXED — 5 ready, 4 need OCR repair |
| **Band 05** | 14 | 10 | 2 | 2 | -8.9 | MOSTLY READY — 10 clean, 4 rough |
| **Band 06** | 18 | 11 | 1 | 6 | -256.2 | WORST BAND — 11 clean but 7 are OCR dumps |
| **Band 07** | 14 | 13 | 0 | 1 | -9.2 | NEARLY READY — one OCR holdout |
| **Band 11 Abt1** | 10 | 10 | 0 | 0 | 86.5 | READY — all clean |
| **Einzel** | 10 | 10 | 0 | 0 | 96.1 | READY — highest quality, all clean |

## Recommended Action Plan

### Phase 1: Ship what's ready (6 volumes, ~70 chapters)
These can go to Zenodo as combined per-band PDFs after the microtype fix:
- Band 01 (10 ch, 304 pages)
- Band 03 (11 ch, 321 pages)  
- Band 07 (13 clean ch, ~430 pages)
- Band 11 Abt1 (10 ch, 326 pages)
- Einzel (10 ch, 247 pages)
- Band 01 alt (10 clean ch, ~260 pages)

**Estimated clean output: ~1,888 pages across 6 volumes.**

### Phase 2: Ship mostly-clean volumes minus holdouts
- Band 02: 10 of 11 chapters clean. Hold ch10 (oversized scan blob).
- Band 05: 10 of 14 chapters clean. Hold 4 OCR-damaged chapters.
- Band 04: 5 of 9 chapters clean. Hold 4 OCR-damaged chapters.

**Estimated additional: ~700 pages from clean chapters.**

### Phase 3: Fix the OCR dumps (18 chapters)
These need real work: either re-OCR and retypeset from scans, or significant manual repair:
- Band 06: ch7-ch13 and section2-5 (7 files, the worst offenders)
- Band 04: ch3, ch4_raw_backup (2 files)
- Band 05: ch3, ch5 (2 files)  
- Band 07: one holdout
- Band 02: ch10 (oversized)
- Plus a few scattered C-grade files

### Global fix needed first
Strip or guard `\usepackage{microtype}` in all 118 files. This is a 30-second sed/regex job.

## Specific Problem Chapters

| File | Issue | Severity |
|------|-------|----------|
| gauss_b02_ch10 | 81 MB PDF — likely embedded scans, not generated LaTeX | HIGH — remove scans from PDF or rebuild |
| gauss_b06_ch7-ch13 | OCR text dumps with `\textasciicircum{}` artifacts, ALL CAPS headers, no real math markup | HIGH — needs retypesetting |
| gauss_b06_section2-5 | Small loose section files, possibly fragments | LOW — may be duplicates |
| gauss_b04_ch3 | OCR damage, raw prose ratio high | MEDIUM |
| gauss_b05_ch3, ch5 | OCR damage | MEDIUM |
| 25_Gauss_Werke_Band01/temp_pages/extracted.pdf | 3.7 MB temp file with no TeX pair | JUNK — exclude |

## Files Created

- `gauss_pdf_audit.csv` — per-PDF audit (pages, text chars, pdfinfo/pdftotext status, flags)
- `gauss_audit_summary.json` — per-band PDF summary
- `gauss_tex_quality.csv` — per-TeX quality classification (grade, score, OCR indicators, math density)
- `gauss_tex_quality_summary.json` — per-band TeX quality summary
- `extracted_gauss/` — all 236 Gauss TeX+PDF files extracted from the source packet
- `compile_tests/` — test compilations of 5 representative files
- `audit_gauss_pdfs.py` — reusable PDF audit script
- `classify_gauss_tex.py` — reusable TeX quality classifier
