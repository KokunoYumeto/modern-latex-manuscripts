# Surface repair actual-fixed cumulative delta (no source scans)

This is an incremental uploadable delta. It does not claim the whole corpus is clean or complete.

Use `cumulative-actually-fixed/replacement-pdfs/` as the current uploadable folder. Anything outside that folder remains unclaimed.

New/updated since round 9: 13 PDFs.

## New/updated PDFs in this delta

- 10-03 English Translation - Qin - Shuxue Jiuzhang, fasc. 1-9.pdf
- 10-06 English Translation - Zhu Shijie - Suanxue Qimeng, parts 1-2.pdf
- 10-07 English Translation - Aryabhata - Aryabhatiya.pdf
- 10-09 English Translation - Bhaskara II - Lilavati.pdf
- 20-04 Modern Chinese - Qin - Shuxue Jiuzhang, fasc. 1 and 5-9.pdf
- 40-03 Chinese Original - Li Ye - Ceyuan Haijing Fenlei Shishu.pdf
- 40-05 Chinese Original - Qin - Shuxue Jiuzhang, fasc. 1-9.pdf
- 40-06 Chinese Original - Sunzi Suanjing.pdf
- 40-07 Chinese Original - Yang Hui - Xiangjie, parts 1-3.pdf
- 40-08 Chinese Original - Zhu Shijie - Suanxue Qimeng, parts 1-2.pdf
- 50-01 Indian Original - Aryabhata - Aryabhatiya.pdf
- 50-03 Indian Original - Bhaskara II - Lilavati.pdf
- 60-05 Islamic Original - Ruska - Oldest Arabic Algebra (1917).pdf

## Empty Contents page prune

The generated reader layer had empty `Contents` pages: visually near-blank pages with only a running header and the word `Contents`, not actual tables of contents. These were removed from the cumulative files below:

- 10-03 English Translation - Qin - Shuxue Jiuzhang, fasc. 1-9.pdf: removed original page(s) 2
- 10-06 English Translation - Zhu Shijie - Suanxue Qimeng, parts 1-2.pdf: removed original page(s) 2
- 20-04 Modern Chinese - Qin - Shuxue Jiuzhang, fasc. 1 and 5-9.pdf: removed original page(s) 3
- 40-03 Chinese Original - Li Ye - Ceyuan Haijing Fenlei Shishu.pdf: removed original page(s) 3,38,81
- 40-05 Chinese Original - Qin - Shuxue Jiuzhang, fasc. 1-9.pdf: removed original page(s) 2,27,47,71,92
- 40-06 Chinese Original - Sunzi Suanjing.pdf: removed original page(s) 2
- 40-07 Chinese Original - Yang Hui - Xiangjie, parts 1-3.pdf: removed original page(s) 2,22,63
- 40-08 Chinese Original - Zhu Shijie - Suanxue Qimeng, parts 1-2.pdf: removed original page(s) 2,20

The Li Ye issue noted by review is included here: `40-03 Chinese Original - Li Ye - Ceyuan Haijing Fenlei Shishu.pdf` was pruned from 119 pages to 116 pages by removing original pages 3, 38, and 81.

## Cumulative status

Cumulative actually-fixed folder: 38 PDFs / 1447 pages.

Reports:
- `reports/surface-repair_empty_contents_prune_report.csv`
- `reports/surface-repair_new_updated_files_audit.csv`
- `reports/surface-repair_cumulative_audit.csv`
- `reports/surface-repair_cumulative_actual_fixed_manifest.csv`
- `reports/surface-repair_empty_contents_before_contact_sheet.jpg`
- `reports/surface-repair_empty_contents_after_contact_sheet.jpg`
- `reports/surface-repair_new_updated_render_contact_sheet.jpg`

Audit note: the current cumulative audit specifically checks for remaining empty generated Contents pages, hard process-text leaks, replacement/square characters in the text layer, blank pages, and sampled right-edge overflow. It is a surface/layout audit, not a full scholarly verification of every line.

Current audit hard-blocker files: 0. See `reports/surface-repair_cumulative_audit.csv` for details.
