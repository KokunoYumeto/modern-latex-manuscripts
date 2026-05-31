# Non-European Public Surface Audit and Completion TODO

Generated: 2026-05-31T15:24:26

Purpose: give the web/pro session a precise repair queue from the public Zenodo/GitHub reader surface, based on the maintainer's visual pass plus automated page/text checks.

Main rule: do not regress clean works. If a reader is already professional-looking, leave it alone unless source-completeness is clearly incomplete.

## Highest Priority

1. `10-07 English Translation - Aryabhata - Aryabhatiya.pdf`: visible layout leakage/overflow. Repair directly against source.
2. `30-01 Arabic Translation - Li Ye - Ceyuan Haijing, vols. 1-6 and 10-12.pdf`: visible overlap/misalignment and incomplete volumes 7-9.
3. Sanskrit/Indian-script cluster (`10-08`, `10-09`, `50-01` to `50-04`): verify rendering, empty-page style, source completeness, and line breaking.
4. Partial Arabic/Chinese translations: complete or clearly mark scope for `20-04`, `30-01`, `30-02`, `30-03`.
5. Persian/Iranian source intake: start author/work-level pages for al-Biruni, Tusi, Khayyam, Kashi; Kashi is scan/transcription-first because OCR is poor.

## Flagged Current Public PDFs

### 10-07 English Translation - Aryabhata - Aryabhatiya.pdf

- Priority: P0 visual repair
- Pages: 18; median extracted text chars/page: 1703
- Visual note: User saw obvious page/layout leakage; Sanskrit/Aryabhata reader needs direct visual repair.
- Completeness/source note: No explicit source-completeness gap inferred yet.
- Recommended action: Repair before next public upload; compare against source and regenerate PDF/TeX.
- Contact sheet: `contact_sheets/10-07_English_Translation_-_Aryabhata_-_Aryabhatiya_selected_pages.jpg`

### 10-08 English Translation - Bhaskara II - Bijaganita, parts 1-3.pdf

- Priority: P1 visual verification
- Pages: 59; median extracted text chars/page: 789
- Visual note: Sanskrit/Indian-script reader may be acceptable but has sparse/uneven pages; verify completeness and page style.
- Completeness/source note: No explicit source-completeness gap inferred yet.
- Recommended action: Render-check selected pages; fix spacing/brackets/overlap if confirmed; otherwise annotate as visually checked.
- Contact sheet: `contact_sheets/10-08_English_Translation_-_Bhaskara_II_-_Bijaganita_parts_1-3_selected_pages.jpg`

### 10-09 English Translation - Bhaskara II - Lilavati.pdf

- Priority: P1 visual verification
- Pages: 23; median extracted text chars/page: 1096
- Visual note: Sanskrit/Indian-script reader may be acceptable but has sparse/uneven pages; verify completeness and page style.
- Completeness/source note: No explicit source-completeness gap inferred yet.
- Recommended action: Render-check selected pages; fix spacing/brackets/overlap if confirmed; otherwise annotate as visually checked.
- Contact sheet: `contact_sheets/10-09_English_Translation_-_Bhaskara_II_-_Lilavati_selected_pages.jpg`

### 10-11 English Translation - al-Kashi - Miftah al-Hisab.pdf

- Priority: P1 completeness/source extension
- Pages: 14; median extracted text chars/page: 2352
- Visual note: No user-visible issue, but source/scope needs clarification.
- Completeness/source note: Likely not full Miftah al-Hisab: public reader is tiny; full Kashi source intake exists and should be used for a proper edition.
- Recommended action: Decide whether to complete missing source sections now or relabel scope more clearly; prefer completion when source is available.
- Contact sheet: `contact_sheets/10-11_English_Translation_-_al-Kashi_-_Miftah_al-Hisab_selected_pages.jpg`

### 10-17 English Translation - Ruska - Oldest Arabic Algebra.pdf

- Priority: P1 visual verification
- Pages: 50; median extracted text chars/page: 6174
- Visual note: Oldest Arabic Algebra has a strange quotation mark/title issue; inspect title page and surface typography.
- Completeness/source note: No explicit source-completeness gap inferred yet.
- Recommended action: Render-check selected pages; fix spacing/brackets/overlap if confirmed; otherwise annotate as visually checked.
- Contact sheet: `contact_sheets/10-17_English_Translation_-_Ruska_-_Oldest_Arabic_Algebra_selected_pages.jpg`

### 10-18 English Translation - al-Muqaddasi - Ahsan al-Taqasim.pdf

- Priority: P2 scope clarification
- Pages: 15; median extracted text chars/page: 1243
- Visual note: No user-visible issue, but source/scope needs clarification.
- Completeness/source note: Reference/context translation; verify whether this is intentionally excerpted or should be complete.
- Recommended action: Clarify scope in metadata/README or convert to full work-level target.
- Contact sheet: `contact_sheets/10-18_English_Translation_-_al-Muqaddasi_-_Ahsan_al-Taqasim_selected_pages.jpg`

### 10-19 English Translation - Ibn al-Nadim - Kitab al-Fihrist.pdf

- Priority: P2 scope clarification
- Pages: 19; median extracted text chars/page: 2091
- Visual note: No user-visible issue, but source/scope needs clarification.
- Completeness/source note: Reference/context translation; verify whether this is intentionally excerpted or should be complete.
- Recommended action: Clarify scope in metadata/README or convert to full work-level target.
- Contact sheet: `contact_sheets/10-19_English_Translation_-_Ibn_al-Nadim_-_Kitab_al-Fihrist_selected_pages.jpg`

### 10-20 English Translation - Said al-Andalusi - Tabaqat al-Umam.pdf

- Priority: P2 scope clarification
- Pages: 12; median extracted text chars/page: 2190
- Visual note: No user-visible issue, but source/scope needs clarification.
- Completeness/source note: Reference/context translation; verify whether this is intentionally excerpted or should be complete.
- Recommended action: Clarify scope in metadata/README or convert to full work-level target.
- Contact sheet: `contact_sheets/10-20_English_Translation_-_Said_al-Andalusi_-_Tabaqat_al-Umam_selected_pages.jpg`

### 20-04 Modern Chinese - Qin - Shuxue Jiuzhang, fasc. 1 and 5-9.pdf

- Priority: P1 completeness/source extension
- Pages: 105; median extracted text chars/page: 872
- Visual note: No user-visible issue, but source/scope needs clarification.
- Completeness/source note: Partial by filename: modern Chinese Qin says fasc. 1 and 5-9, apparently missing fasc. 2-4.
- Recommended action: Decide whether to complete missing source sections now or relabel scope more clearly; prefer completion when source is available.
- Contact sheet: `contact_sheets/20-04_Modern_Chinese_-_Qin_-_Shuxue_Jiuzhang_fasc._1_and_5-9_selected_pages.jpg`

### 20-05 Modern Chinese - Sunzi Suanjing.pdf

- Priority: P1 visual verification
- Pages: 16; median extracted text chars/page: 730
- Visual note: Modern Chinese Sunzi may contain empty brackets or placeholder-looking marks; inspect against source.
- Completeness/source note: No explicit source-completeness gap inferred yet.
- Recommended action: Render-check selected pages; fix spacing/brackets/overlap if confirmed; otherwise annotate as visually checked.
- Contact sheet: `contact_sheets/20-05_Modern_Chinese_-_Sunzi_Suanjing_selected_pages.jpg`

### 20-06 Modern Chinese - Yang Hui - Xiangjie, parts 1-3.pdf

- Priority: P1 visual verification
- Pages: 77; median extracted text chars/page: 668
- Visual note: Modern Chinese Yang Hui may have bracket/spacing artifacts; inspect against source.
- Completeness/source note: No explicit source-completeness gap inferred yet.
- Recommended action: Render-check selected pages; fix spacing/brackets/overlap if confirmed; otherwise annotate as visually checked.
- Contact sheet: `contact_sheets/20-06_Modern_Chinese_-_Yang_Hui_-_Xiangjie_parts_1-3_selected_pages.jpg`

### 20-07 Modern Chinese - Zhu Shijie - Suanxue Qimeng, parts 1-2.pdf

- Priority: P1 visual verification
- Pages: 38; median extracted text chars/page: 1349
- Visual note: Possible wide spacing between Chinese characters; verify if this is acceptable style or bad CJK typesetting.
- Completeness/source note: No explicit source-completeness gap inferred yet.
- Recommended action: Render-check selected pages; fix spacing/brackets/overlap if confirmed; otherwise annotate as visually checked.
- Contact sheet: `contact_sheets/20-07_Modern_Chinese_-_Zhu_Shijie_-_Suanxue_Qimeng_parts_1-2_selected_pages.jpg`

### 30-01 Arabic Translation - Li Ye - Ceyuan Haijing, vols. 1-6 and 10-12.pdf

- Priority: P0 visual repair
- Pages: 83; median extracted text chars/page: 1946
- Visual note: Arabic Li Ye definitely looked wrong to user: missing/overlapping parts and text in strange places.
- Completeness/source note: Partial by filename: Arabic Li Ye says vols. 1-6 and 10-12, missing vols. 7-9.
- Recommended action: Repair before next public upload; compare against source and regenerate PDF/TeX.
- Contact sheet: `contact_sheets/30-01_Arabic_Translation_-_Li_Ye_-_Ceyuan_Haijing_vols._1-6_and_10-12_selected_pages.jpg`

### 30-02 Arabic Translation - Qin - Shuxue Jiuzhang, fasc. 1 and 4.pdf

- Priority: P1 completeness/source extension
- Pages: 26; median extracted text chars/page: 3478
- Visual note: Arabic Qin might have alignment issues; inspect visually and against source.
- Completeness/source note: Partial by filename: Arabic Qin says fasc. 1 and 4 only, missing most fascicles.
- Recommended action: Decide whether to complete missing source sections now or relabel scope more clearly; prefer completion when source is available.
- Contact sheet: `contact_sheets/30-02_Arabic_Translation_-_Qin_-_Shuxue_Jiuzhang_fasc._1_and_4_selected_pages.jpg`

### 30-03 Arabic Translation - Yang Hui - Xiangjie, part 1.pdf

- Priority: P1 completeness/source extension
- Pages: 27; median extracted text chars/page: 1366
- Visual note: Arabic Yang Hui might have alignment/completeness issues; inspect visually and against source.
- Completeness/source note: Partial by filename: Arabic Yang Hui says part 1 only, missing parts 2-3.
- Recommended action: Decide whether to complete missing source sections now or relabel scope more clearly; prefer completion when source is available.
- Contact sheet: `contact_sheets/30-03_Arabic_Translation_-_Yang_Hui_-_Xiangjie_part_1_selected_pages.jpg`

### 30-04 Arabic Translation - al-Kashi - Miftah al-Hisab.pdf

- Priority: P1 completeness/source extension
- Pages: 29; median extracted text chars/page: 834
- Visual note: No user-visible issue, but source/scope needs clarification.
- Completeness/source note: Likely not full Miftah al-Hisab: Arabic translation reader is tiny; full Kashi source intake exists and OCR is weak.
- Recommended action: Decide whether to complete missing source sections now or relabel scope more clearly; prefer completion when source is available.
- Contact sheet: `contact_sheets/30-04_Arabic_Translation_-_al-Kashi_-_Miftah_al-Hisab_selected_pages.jpg`

### 50-01 Indian Original - Aryabhata - Aryabhatiya.pdf

- Priority: P1 visual verification
- Pages: 18; median extracted text chars/page: 1657
- Visual note: Indian original seems acceptable but very short/sparse; verify source completeness and typography.
- Completeness/source note: No explicit source-completeness gap inferred yet.
- Recommended action: Render-check selected pages; fix spacing/brackets/overlap if confirmed; otherwise annotate as visually checked.
- Contact sheet: `contact_sheets/50-01_Indian_Original_-_Aryabhata_-_Aryabhatiya_selected_pages.jpg`

### 50-02 Indian Original - Bhaskara II - Bijaganita, parts 1-3.pdf

- Priority: P1 visual verification
- Pages: 59; median extracted text chars/page: 789
- Visual note: Indian original has sparse pages; likely style/script issue but should be checked.
- Completeness/source note: No explicit source-completeness gap inferred yet.
- Recommended action: Render-check selected pages; fix spacing/brackets/overlap if confirmed; otherwise annotate as visually checked.
- Contact sheet: `contact_sheets/50-02_Indian_Original_-_Bhaskara_II_-_Bijaganita_parts_1-3_selected_pages.jpg`

### 50-03 Indian Original - Bhaskara II - Lilavati.pdf

- Priority: P1 visual verification
- Pages: 16; median extracted text chars/page: 1887
- Visual note: Indian original has sparse pages; likely style/script issue but should be checked.
- Completeness/source note: No explicit source-completeness gap inferred yet.
- Recommended action: Render-check selected pages; fix spacing/brackets/overlap if confirmed; otherwise annotate as visually checked.
- Contact sheet: `contact_sheets/50-03_Indian_Original_-_Bhaskara_II_-_Lilavati_selected_pages.jpg`

### 50-04 Indian Original - Brahmagupta - Brahmasphutasiddhanta.pdf

- Priority: P1 visual verification
- Pages: 279; median extracted text chars/page: 1134
- Visual note: Brahmagupta/Sanskrit material is a known hard lane; verify source-backed completeness and rendering.
- Completeness/source note: No explicit source-completeness gap inferred yet.
- Recommended action: Render-check selected pages; fix spacing/brackets/overlap if confirmed; otherwise annotate as visually checked.
- Contact sheet: `contact_sheets/50-04_Indian_Original_-_Brahmagupta_-_Brahmasphutasiddhanta_selected_pages.jpg`

### 60-01 Islamic Original - al-Kashi - Miftah al-Hisab.pdf

- Priority: P1 completeness/source extension
- Pages: 27; median extracted text chars/page: 1289
- Visual note: No user-visible issue, but source/scope needs clarification.
- Completeness/source note: Likely not full Miftah al-Hisab: original reader is tiny relative to full source; transcription-first source work needed.
- Recommended action: Decide whether to complete missing source sections now or relabel scope more clearly; prefer completion when source is available.
- Contact sheet: `contact_sheets/60-01_Islamic_Original_-_al-Kashi_-_Miftah_al-Hisab_selected_pages.jpg`

### 60-05 Islamic Original - Ruska - Oldest Arabic Algebra (1917).pdf

- Priority: P0 visual repair
- Pages: 60; median extracted text chars/page: 3612
- Visual note: Ruska / Oldest Arabic Algebra original looks weird on device; needs formatting/title audit.
- Completeness/source note: No explicit source-completeness gap inferred yet.
- Recommended action: Repair before next public upload; compare against source and regenerate PDF/TeX.
- Contact sheet: `contact_sheets/60-05_Islamic_Original_-_Ruska_-_Oldest_Arabic_Algebra_(1917)_selected_pages.jpg`

### 60-08 Islamic and Arabic Work - al-Battani - Opus Astronomicum, Segments 1-5.pdf

- Priority: P1 completeness/source extension
- Pages: 59; median extracted text chars/page: 1888
- Visual note: No user-visible issue, but source/scope needs clarification.
- Completeness/source note: Partial but intentionally current: al-Battani Opus Astronomicum only segments 1-5 so far.
- Recommended action: Decide whether to complete missing source sections now or relabel scope more clearly; prefer completion when source is available.
- Contact sheet: `contact_sheets/60-08_Islamic_and_Arabic_Work_-_al-Battani_-_Opus_Astronomicum_Segments_1-5_selected_pages.jpg`

### 70-01 Reference Text - Said al-Andalusi - Tabaqat al-Umam.pdf

- Priority: P2 scope clarification
- Pages: 15; median extracted text chars/page: 2108
- Visual note: No user-visible issue, but source/scope needs clarification.
- Completeness/source note: Reference/context reader, not a complete critical mathematical work unless source scope is explicitly expanded.
- Recommended action: Clarify scope in metadata/README or convert to full work-level target.
- Contact sheet: `contact_sheets/70-01_Reference_Text_-_Said_al-Andalusi_-_Tabaqat_al-Umam_selected_pages.jpg`

### 70-02 Reference Text - al-Muqaddasi - Ahsan al-Taqasim.pdf

- Priority: P2 scope clarification
- Pages: 10; median extracted text chars/page: 2271
- Visual note: No user-visible issue, but source/scope needs clarification.
- Completeness/source note: Reference/context reader, not a complete critical mathematical work unless source scope is explicitly expanded.
- Recommended action: Clarify scope in metadata/README or convert to full work-level target.
- Contact sheet: `contact_sheets/70-02_Reference_Text_-_al-Muqaddasi_-_Ahsan_al-Taqasim_selected_pages.jpg`

### 70-03 Reference Text - Ibn al-Nadim - Kitab al-Fihrist.pdf

- Priority: P2 scope clarification
- Pages: 11; median extracted text chars/page: 1727
- Visual note: No user-visible issue, but source/scope needs clarification.
- Completeness/source note: Reference/context reader, not a complete critical mathematical work unless source scope is explicitly expanded.
- Recommended action: Clarify scope in metadata/README or convert to full work-level target.
- Contact sheet: `contact_sheets/70-03_Reference_Text_-_Ibn_al-Nadim_-_Kitab_al-Fihrist_selected_pages.jpg`

### 70-04 Reference Text - Ibn al-Qifti - Tarikh al-Hukama.pdf

- Priority: P2 scope clarification
- Pages: 10; median extracted text chars/page: 2330
- Visual note: No user-visible issue, but source/scope needs clarification.
- Completeness/source note: Reference/context reader, not a complete critical mathematical work unless source scope is explicitly expanded.
- Recommended action: Clarify scope in metadata/README or convert to full work-level target.
- Contact sheet: `contact_sheets/70-04_Reference_Text_-_Ibn_al-Qifti_-_Tarikh_al-Hukama_selected_pages.jpg`

## Source Intake / Completion Lane

These are not just formatting defects; they are places where a complete work-level archive needs additional source-backed work.

- Persian/Iranian lane: al-Biruni, al-Qanun al-Masudi. Core downloads packet exists; large source, OCR/XML/scandata available.
- Persian/Iranian lane: Tusi, Tahrir Euclid. Core downloads packet exists; good first web-session target.
- Persian/Iranian lane: Khayyam algebra. Core downloads packet exists; compare against current reader and repair fidelity.
- Persian/Iranian lane: Kashi, Miftah al-Hisab. Core downloads packet exists; OCR is very weak, use scans/images for transcription.
- Arabic astronomy: al-Battani, Opus Astronomicum. Segments 1-5 public; continue segment-by-segment toward full work.

## Files in this packet

- `non_eu_public_surface_audit_rows.csv`: machine-readable audit rows.
- `contact_sheets/`: selected-page render checks for every flagged PDF.
- `web_session_prompt_non_eu_public_surface_repair.md`: paste this into the repair session.
- `persian_iranian_source_targets.csv` when available: Persian/Iranian intake targets.

