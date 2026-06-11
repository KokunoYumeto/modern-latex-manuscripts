# Gauss Workstart Round 01 - 2026-06-01

This packet starts the Gauss lane from the actual source material present in the attached starter packet. It does **not** use a reduced or summary TeX substitute as the working source. The full TeX snapshot from `source_tex_and_component_pdfs/` is included under `source_inventory/real_source_tex_snapshot/`, and the scan-locked repair TeX from the current cumulative rebuild is included under `source_inventory/repair_sources_snapshot/`.

## What is new in this packet

1. Two small but real Band II source passages were promoted into a first working batch:
   - `Theorematis arithmetici demonstratio nova`, Articles 5-7.
   - The Seeber ternary-quadratic-form identity passage, Werke II p. 193.
2. For both passages this packet contains:
   - original-language/source TeX;
   - rendered source PDF;
   - English translation TeX;
   - rendered English PDF;
   - PDF text-leak check results;
   - rendered-page PNGs for visual check.
3. The packet includes a source inventory, priority queue, and P0/P1 holdout list for continuing Gauss without rediscovering the triage.

## Directory map

```text
new_work_this_round/
  original_language/tex/     source-locked TeX for the two completed passages
  original_language/pdf/     rendered source PDFs and compile logs
  english_translation/tex/   English translation TeX
  english_translation/pdf/   rendered English PDFs and compile logs
  source_scans_for_checking/ source-page references; actual scan packets 02/03 still needed
  audit/                     status note and source references

cumulative_current/
  original_language/tex/     cumulative seed through this round for promoted source passages

source_inventory/
  real_source_tex_snapshot/  all 118 actual Gauss source TeX files from the starter packet
  repair_sources_snapshot/   current public rebuild repair-source TeX/raw text/scripts
  REAL_SOURCE_TEX_INVENTORY.csv
  GAUSS_PRIORITY_QUEUE.csv
  HOLDOUTS_P0_P1.csv

audit/
  GAUSS_TRIAGE_REPORT.md
  gauss_tex_quality.csv
  gauss_tex_quality_summary.json
  gauss_pdf_audit.csv
  pdf_text_leak_check.json
  pdf_renders/

tools/
  check_pdf_text_leaks.py
  make_gauss_inventory.py
  make_manifest.py
```

## Continuation rule

Do not start by retranscribing the famous complete `Disquisitiones Arithmeticae` unless a specific broken page is being repaired. The best next actions are:

1. P0 repair: use source scans to fix OCR-damaged Band VI/Band IV/Band V holdouts listed in `source_inventory/HOLDOUTS_P0_P1.csv`.
2. Translation: translate less-standard, high-quality source TeX from Band II/Band III/Einzel after verifying against source scan pages.
3. Front-facing output: every completed unit must return TeX, PDF, source page references/scans, and a status note.

