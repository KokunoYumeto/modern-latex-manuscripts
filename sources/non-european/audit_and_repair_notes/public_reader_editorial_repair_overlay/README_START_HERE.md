# Non-European Mathematics Corpus - Round 3 clean public readers

This package is the no-source-scan public-reader bundle. It is intentionally much smaller than the previous source-inclusive package.

Contents:

- `public-readers/`: 66 cleaned public reader PDFs.
- `reports/round3_public_manifest.csv` and `.json`: page counts, byte sizes, and SHA-256 hashes.
- `reports/round3_text_sweep.json`: final text-layer sweep. The remaining hits are classified as false positives: ordinary phrases such as "no image" in translated text, Sanskrit/transliteration strings, and bibliographic uses of "Codex".
- `reports/round3_trim_report.json`: wrapper/front-matter pages removed from the previous public PDFs.
- `reports/round3_zhu_facsimile_patch.json`: facsimile boxes repaired in the Zhu Shijie reader using pages from the second source-scan ZIP.
- `reports/source_scans_pdf2_inventory.csv` and `.json`: source-scan inventory for `pdf2.zip`; no source PDFs are included here.
- `reports/round3_render_smoke_contact_sheet.jpg`: rendered smoke-check samples from the final PDFs.

Main editorial repair actions in this round:

1. Removed public-facing wrapper pages of the form "About this reader / source TeX and support material" from work-level readers.
2. Removed the generated "Translator's Preface" page from the Bhaskara II Bijaganita reader.
3. Rebuilt all seven combined readers from the cleaned component PDFs.
4. Replaced stale/process-heavy index text with a clean reader index.
5. Patched Zhu Shijie's `Suanxue Qimeng` facsimile placeholders by inserting the corresponding page images from the second source-scan ZIP.
6. Re-ran text and render smoke checks after rebuilding.

Source scans are deliberately omitted. Use the separately supplied `pdfs1.zip` and `pdf2.zip` for scan-level verification.
