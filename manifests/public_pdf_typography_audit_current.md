# Public PDF Typography Audit

Generated: 2026-05-29T04:15

This is a conservative mechanical audit of the current public-facing PDF surfaces. It measures extractable text span sizes and page sizes; it can flag title pages, inserted scans, reference PDFs, and section dividers even when the document is usable. Treat this as a repair queue, not as proof of bad typography.

## Summary

- PDFs checked: 370
- Reader-class PDFs checked: 344
- Reader-class PDFs with at least one typography warning: 133
- Warning counts: body-font-large: 1, body-font-small: 1, inconsistent-page-font-size: 131, mixed-page-sizes: 36, wide-font-size-spread: 7

## Warnings By Record

| Record | Warned reader PDFs |
|---|---:|
| author_cluster | 6 |
| chinese | 13 |
| classical | 17 |
| deligne | 19 |
| ega | 1 |
| gauss | 6 |
| historical_references | 5 |
| indian_sanskrit | 6 |
| islamic_arabic | 3 |
| main | 22 |
| noether | 1 |
| non_eu | 29 |
| riemann | 1 |
| sga | 2 |
| weber | 2 |

## Highest-Priority Mechanical Review Items

| Record | PDF | Pages | Median body size | Page-size/font range | Warning |
|---|---|---:|---:|---:|---|
| main | 10 Reader PDF - Aryabhata - Aryabhatiya.pdf | 22 | 12.55 | 1.2 | body-font-large |
| deligne | 10-076 Deligne - Groupes fondamentaux motivique - Original.pdf | 56 | 7.25 | 0.73 | body-font-small |
| classical | 02 Cayley - Collected Mathematical Papers, Volume X - Modern LaTeX Draft.pdf | 461 | 11.96 | 9.67 | inconsistent-page-font-size;mixed-page-sizes |
| main | 10 Reader PDF - Cayley - Collected Papers Partial Draft.pdf | 2266 | 10.91 | 9.67 | inconsistent-page-font-size;mixed-page-sizes |
| classical | 34 Gauss - Werke, Band VI - Modern LaTeX Draft.pdf | 665 | 11.96 | 9.37 | inconsistent-page-font-size;mixed-page-sizes |
| gauss | 04 Carl Friedrich Gauss - Werke, Band VI - Modern LaTeX Draft.pdf | 665 | 11.96 | 9.37 | inconsistent-page-font-size;mixed-page-sizes |
| chinese | 02 Chinese Classics - Combined Modern Chinese Renderings.pdf | 460 | 10.91 | 8.25 | inconsistent-page-font-size |
| non_eu | 02 Combined Modern Chinese Renderings.pdf | 460 | 10.91 | 8.25 | inconsistent-page-font-size |
| chinese | 20-06 Modern Chinese - Yang Hui - Xiangjie, parts 1-3.pdf | 82 | 9.96 | 7.26 | inconsistent-page-font-size;wide-font-size-spread |
| non_eu | 20-06 Modern Chinese - Yang Hui - Xiangjie, parts 1-3.pdf | 82 | 9.96 | 7.26 | inconsistent-page-font-size;wide-font-size-spread |
| classical | 04 Cayley - Collected Mathematical Papers, Volume XII - Modern LaTeX Draft.pdf | 353 | 10.91 | 5.98 | inconsistent-page-font-size |
| author_cluster | 08 Reader PDF - Hausdorff - Mengenlehre and Descriptive Set Theory Writings.pdf | 675 | 11.96 | 5.38 | inconsistent-page-font-size;mixed-page-sizes |
| main | 10 Reader PDF - Darboux - Lessons on the General Theory of Surfaces.pdf | 484 | 11.96 | 5.38 | inconsistent-page-font-size |
| main | 10 Reader PDF - Hausdorff - Set Theory.pdf | 673 | 11.96 | 5.38 | inconsistent-page-font-size;mixed-page-sizes |
| classical | 11 Dedekind - Gesammelte Mathematische Werke, Band II - Modern LaTeX Draft.pdf | 304 | 11.96 | 5.35 | inconsistent-page-font-size;wide-font-size-spread |
| main | 10 Reader PDF - Picard - Traite d analyse.pdf | 657 | 11.96 | 5.26 | inconsistent-page-font-size;mixed-page-sizes |
| indian_sanskrit | 02 Indian Classics - Combined Original-Language Drafts.pdf | 392 | 10.91 | 4.78 | inconsistent-page-font-size;wide-font-size-spread |
| non_eu | 05 Indian Originals - Modern LaTeX.pdf | 392 | 10.91 | 4.78 | inconsistent-page-font-size;wide-font-size-spread |
| classical | 01 Cayley - Collected Mathematical Papers, Volume VII - Modern LaTeX Draft.pdf | 455 | 10.91 | 3.99 | inconsistent-page-font-size;wide-font-size-spread;mixed-page-sizes |
| main | 10 Reader PDF - Brahmagupta - Brahmasphutasiddhanta Part I.pdf | 108 | 10.91 | 3.79 | inconsistent-page-font-size;wide-font-size-spread |

## Immediate Interpretation

- The SGA author/corpus record itself has stable body size for the new SGA 4/5/6/7 working readers; the warnings on SGA 2 and SGA 3 are inherited from existing snapshot PDFs, not from the new TeX builds.
- The main landing page still contains some older broad-reader PDFs whose cleaner or more current equivalents now live in focused author/corpus records. The main page should be refreshed over time so its direct PDFs mirror the cleanest current surfaces, while preserving older material in ZIPs or version history.
- Most non-European warnings are range/spread warnings caused by title pages, language/script changes, or section dividers; the current non-European Zenodo record matches the latest reviewed public-reader overlay and has no process-note or public-surface audit flags.
- The largest true typography candidates for repair are legacy/main Cayley and Gauss combined readers, selected non-European combined readers, and duplicated broad main readers that are superseded by focused records.
