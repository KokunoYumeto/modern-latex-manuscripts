You are continuing the Gauss lane. Use the actual source TeX in `source_inventory/real_source_tex_snapshot/` and the scan-locked repair TeX in `source_inventory/repair_sources_snapshot/`. Do not use a reduced summary TeX as the source of truth.

Work for roughly one hour before reporting unless genuinely blocked. Return complete, checkable units: source TeX, translated TeX if translation is part of the task, rendered PDFs, source scan/page references, cumulative manifest, and an audit note. Do not stop every few pages.

Do not put screenshots in place of tables, diagrams, formulas, or pages in front-facing PDFs. Screenshots are permitted only in source/audit folders. If a formula or table is unclear, preserve the best TeX candidate, flag the source page, and continue around it.

Start from one of these queues:

1. Source repair queue: `source_inventory/HOLDOUTS_P0_P1.csv`. Repair P0 OCR-damaged files from scans before translating them.
2. Translation queue: grade-A less-standard works from Band II, Band III, or Einzel. Verify against source pages before declaring complete.
3. Cumulative record queue: only add units that compile and have a status note.

For each return, include:

```text
new_work_this_round/
  original_language/tex/
  original_language/pdf/
  english_translation/tex/       # if translation was done
  english_translation/pdf/       # if translation was done
  source_scans_for_checking/
  audit/STATUS.md

cumulative_current/
  original_language/tex/
  original_language/pdf/
  english_translation/tex/
  english_translation/pdf/
  manifest.csv
```

Run a PDF text leak check for `\\frac`, `\\partial`, `\\begin`, `\\end`, `\\delta`, `\\psi`, etc. Render at least the first page of every new PDF and inspect it before returning.
