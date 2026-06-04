# Source-Witness Quick Audit - 2026-06-04

Scope: latest local in-process lane packets under `C:/Users/Floris/Documents/Papors/Chatnotes/CHat translates and clean`. This is a fast structural audit, not a mathematical proofread. It checks whether current packages visibly include reader PDFs/TeX plus source scans, scan slices, page images, or source-witness PDFs.

## Promotion Outcomes

After this quick audit, the following source-checkable packets were promoted to their existing Zenodo concept records and mirrored to GitHub:

- SGA: SGA 7-I source-checked cumulative readers through source page 469. Latest record version: `10.5281/zenodo.20544089`.
- Weber: Volume II source-checked cumulative readers through section 131. Latest record version: `10.5281/zenodo.20544247`.
- Noether: Spanish/Japanese cumulative readers through Paper 43 complete, with EN/DE controls and recursive audit start. Latest record version: `10.5281/zenodo.20544550`.
- Sylvester: Volume I source-checked working edition through book page 457. Latest record version: `10.5281/zenodo.20544607`.
- Dirichlet: Werke Band II cumulative original/English readers through Papers I-XXXV. Latest record version: `10.5281/zenodo.20544678`.
- Gauss: Werke Band II source-checked cumulative original/English readers through printed page 303. Latest record version: `10.5281/zenodo.20544740`.
- Dedekind: GMW Volume I Item I complete. Latest record version: `10.5281/zenodo.20544790`.
- Deligne: forward cumulative promoted to papers 001-016 through page 30, and reverse Paper 079 promoted from partial to complete, with refreshed source-witness TeX/scan/QA packets. Latest record version: `10.5281/zenodo.20544911`.

Correction to the initial fast heuristic: Dedekind `DR15_V1I_p18_26` does include a source witness at `01_new/src/src_p18_26.pdf`; the first pass failed to count it because the folder was named `src` rather than `scan` or `source_scans`.

## Summary Table

| Lane | Latest item | PDFs | TeX | Images | Source-like files | Red flags | Verdict |
|---|---:|---:|---:|---:|---:|---:|---|
| Sylvester | `Sylvester_Vol1_pp001_440_with_scans_20260603.zip` | 8 | 3 | 38 | 40 | 0 | SOURCE-CHECKABLE PACKAGE SHAPE OK |
| deligne restart | `D016_LC_p021_030` plus `D079_090dn_p041_055_std` | 57 + 43 | 36 + 26 | 0 + 68 | 25 + 91 | 17 + 6 | SOURCE-CHECKABLE PACKAGE SHAPE OK |
| Dirichlet | `Dirichlet_R20_XXX_XXXV_20260604.zip` | 32 | 12 | 50 | 57 | 0 | SOURCE-CHECKABLE PACKAGE SHAPE OK |
| Steintz | `Steinitz_20` | 56 | 54 | 431 | 434 | 0 | SOURCE-CHECKABLE PACKAGE SHAPE OK |
| old physics | `GibbsV1_P3_p085_094.zip` | 4 | 2 | 0 | 2 | 0 | SOURCE-CHECKABLE PACKAGE SHAPE OK |
| Gauss | `gauss_r25_dedekind_de_nexu_notes_20260604.zip` | 8 | 4 | 50 | 58 | 0 | SOURCE-CHECKABLE PACKAGE SHAPE OK |
| Weber restart | `Weber_Cumulative_ThreeVolumes_Batch81_Vol2_Sections125_131_SIZE_CONTROLLED_20260604` | 13 | 8 | 38 | 46 | 0 | SOURCE-CHECKABLE PACKAGE SHAPE OK |
| cleanup multilingual | `CLAUDE_OUTPUT_SCRIPTS_AND_LESSONS` | 0 | 0 | 0 | 0 | 0 | NO PDF/TEX PAYLOAD FOUND |
| dedekind | `DR15_V1I_p18_26` | 5 | 4 | 0 | 1 | 1 | SOURCE-CHECKABLE PACKAGE SHAPE OK |
| Noether Multilingual | `Noether_Paper43_final_RA01_ES_JA_20260604.zip` | source package present | source package present | source/render package present | scan witness present | audit package present | SOURCE-CHECKABLE PACKAGE SHAPE OK |
| SGA restart | `sga7i_423_469` | 20 | 1 | 72 | 80 | 0 | SOURCE-CHECKABLE PACKAGE SHAPE OK |
| Cayley | `Cayley_V1_pp009_012_seq_repair_20260604` | 4 | 1 | 0 | 2 | 0 | SOURCE-CHECKABLE PACKAGE SHAPE OK |

## Lane Notes

### Sylvester
- Latest item audited: `C:\Users\Floris\Documents\Papors\Chatnotes\CHat translates and clean\Sylvester\Sylvester_Vol1_pp001_440_with_scans_20260603.zip`
- Verdict: **SOURCE-CHECKABLE PACKAGE SHAPE OK**
- Counts: `8` PDFs, `3` TeX files, `38` images, `40` scan/source-like files, `4` README/manifest/audit files.
- Source-witness samples:
  - `sylv_b23/verify/new/page-01.png`
  - `sylv_b23/verify/new/page-02.png`
  - `sylv_b23/verify/new/page-03.png`
  - `sylv_b23/verify/new/page-04.png`
  - `sylv_b23/verify/new/page-05.png`
- PDF samples:
  - `sylv_b23/old/Vol1_pp001_422.pdf`
  - `sylv_b23/old/src_019_440_book001_422.pdf`
  - `sylv_b23/new/tex/Vol1_pp423_440.pdf`
  - `sylv_b23/new/pdf/Vol1_pp423_440.pdf`
  - `sylv_b23/new/scan_pdf/src_441_458_book423_440.pdf`

### deligne restart
- Latest items audited:
  - `C:\Users\Floris\Documents\Papors\Chatnotes\CHat translates and clean\deligne restart\D016_LC_p021_030`
  - `C:\Users\Floris\Documents\Papors\Chatnotes\CHat translates and clean\deligne restart\D079_090dn_p041_055_std`
- Verdict: **SOURCE-CHECKABLE PACKAGE SHAPE OK**
- Counts: forward D016 package has `57` PDFs, `36` TeX files, `0` images, `25` scan/source-like files, `17` README/manifest/audit files. Reverse D079-090 package has `43` PDFs, `26` TeX files, `68` images, `91` scan/source-like files, `6` README/manifest/audit files.
- Promotion: published to `10.5281/zenodo.20544911`.
- Page-count check before promotion:
  - Forward cumulative English: `232` pages.
  - Forward cumulative French: `233` pages.
  - Forward cumulative source scan: `342` pages.
  - Paper 079 English: `44` pages.
  - Paper 079 French: `45` pages.
  - Paper 079 source scan: `55` pages.
- Source-witness samples:
  - `C001_010/SCAN/D016_LC_001_010_SCAN.pdf`
  - `I001_010/SCAN/D016_LC_001_010_SCAN.pdf`
  - `Method/scripts/extract_scan.py`
  - `Method/scripts/render.py`
  - `SEQ_CUM/ALL_001_016p010/SCAN/ALL_001_016p010_SCAN.pdf`
- PDF samples:
  - `C001_010/PDF/D016_LC_001_010_EN.pdf`
  - `C001_010/PDF/D016_LC_001_010_FR.pdf`
  - `C001_010/SCAN/D016_LC_001_010_SCAN.pdf`
  - `I001_010/PDF/D016_LC_001_010_EN.pdf`
  - `I001_010/PDF/D016_LC_001_010_FR.pdf`

### Dirichlet
- Latest item audited: `C:\Users\Floris\Documents\Papors\Chatnotes\CHat translates and clean\Dirichlet\Dirichlet_R20_XXX_XXXV_20260604.zip`
- Verdict: **SOURCE-CHECKABLE PACKAGE SHAPE OK**
- Counts: `32` PDFs, `12` TeX files, `50` images, `57` scan/source-like files, `2` README/manifest/audit files.
- Source-witness samples:
  - `Dirichlet_R20_XXX_XXXV_20260604/src/pages/v2_p0365.png`
  - `Dirichlet_R20_XXX_XXXV_20260604/src/pages/v2_p0366.png`
  - `Dirichlet_R20_XXX_XXXV_20260604/src/pages/v2_p0367.png`
  - `Dirichlet_R20_XXX_XXXV_20260604/src/pages/v2_p0368.png`
  - `Dirichlet_R20_XXX_XXXV_20260604/src/pages/v2_p0369.png`
- PDF samples:
  - `Dirichlet_R20_XXX_XXXV_20260604/new/orig/tex/30_indet_fr.pdf`
  - `Dirichlet_R20_XXX_XXXV_20260604/new/orig/tex/31_bernoulli_mixed.pdf`
  - `Dirichlet_R20_XXX_XXXV_20260604/new/orig/tex/32_preisfrage_de.pdf`
  - `Dirichlet_R20_XXX_XXXV_20260604/new/orig/tex/33_quadratur_de.pdf`
  - `Dirichlet_R20_XXX_XXXV_20260604/new/orig/tex/34_akadem_rede_la.pdf`

### Steintz
- Latest item audited: `C:\Users\Floris\Documents\Papors\Chatnotes\CHat translates and clean\Steintz\Steinitz_20`
- Verdict: **SOURCE-CHECKABLE PACKAGE SHAPE OK**
- Counts: `56` PDFs, `54` TeX files, `431` images, `434` scan/source-like files, `6` README/manifest/audit files.
- Source-witness samples:
  - `01_1894_dissertation/qa/de/page_first-01.png`
  - `01_1894_dissertation/qa/de/page_last-10.png`
  - `01_1894_dissertation/qa/steinitz_1894_config_construction_de_complete/first-01.png`
  - `01_1894_dissertation/qa/steinitz_1894_config_construction_de_complete/last-23.png`
  - `01_1894_dissertation/qa/steinitz_1894_config_construction_de_p021-047/first-01.png`
- PDF samples:
  - `01_1894_dissertation/de/steinitz_1894_config_construction_de_complete.pdf`
  - `01_1894_dissertation/de/steinitz_1894_config_construction_de_p001-021.pdf`
  - `01_1894_dissertation/de/steinitz_1894_config_construction_de_p021-047.pdf`
  - `01_1894_dissertation/en/steinitz_1894_config_construction_en_complete.pdf`
  - `01_1894_dissertation/en/steinitz_1894_config_construction_en_p001-021.pdf`

### old physics
- Latest item audited: `C:\Users\Floris\Documents\Papors\Chatnotes\CHat translates and clean\old physics\GibbsV1_P3_p085_094.zip`
- Verdict: **SOURCE-CHECKABLE PACKAGE SHAPE OK**
- Counts: `4` PDFs, `2` TeX files, `0` images, `2` scan/source-like files, `0` README/manifest/audit files.
- Source-witness samples:
  - `GibbsV1_P3_p085_094/Cum_p055_094/SCAN/gibbs_v1_p3_055_094_scan.pdf`
  - `GibbsV1_P3_p085_094/Inst_p085_094/SCAN/gibbs_v1_p3_085_094_scan.pdf`
- PDF samples:
  - `GibbsV1_P3_p085_094/Cum_p055_094/PDF/gibbs_v1_p3_055_094_en.pdf`
  - `GibbsV1_P3_p085_094/Cum_p055_094/SCAN/gibbs_v1_p3_055_094_scan.pdf`
  - `GibbsV1_P3_p085_094/Inst_p085_094/PDF/gibbs_v1_p3_085_094_en.pdf`
  - `GibbsV1_P3_p085_094/Inst_p085_094/SCAN/gibbs_v1_p3_085_094_scan.pdf`

### Gauss
- Latest item audited: `C:\Users\Floris\Documents\Papors\Chatnotes\CHat translates and clean\Gauss\gauss_r25_dedekind_de_nexu_notes_20260604.zip`
- Verdict: **SOURCE-CHECKABLE PACKAGE SHAPE OK**
- Counts: `8` PDFs, `4` TeX files, `50` images, `58` scan/source-like files, `56` README/manifest/audit files.
- Source-witness samples:
  - `gauss_r25_dedekind_de_nexu_notes_20260604/audit/cum_scan.txt`
  - `gauss_r25_dedekind_de_nexu_notes_20260604/audit/new_scan.txt`
  - `gauss_r25_dedekind_de_nexu_notes_20260604/audit/renders/cum_en/p001.png`
  - `gauss_r25_dedekind_de_nexu_notes_20260604/audit/renders/cum_en/p071.png`
  - `gauss_r25_dedekind_de_nexu_notes_20260604/audit/renders/cum_en/p133.png`
- PDF samples:
  - `gauss_r25_dedekind_de_nexu_notes_20260604/cum/full_en/g_full_001_303_en.pdf`
  - `gauss_r25_dedekind_de_nexu_notes_20260604/cum/full_src/g_full_001_303_src.pdf`
  - `gauss_r25_dedekind_de_nexu_notes_20260604/cum/scans/scan_pp001_303.pdf`
  - `gauss_r25_dedekind_de_nexu_notes_20260604/new/en/g25_en.pdf`
  - `gauss_r25_dedekind_de_nexu_notes_20260604/new/scans/preview/p304_blank_p305_preview.pdf`

### Weber restart
- Latest item audited: `C:\Users\Floris\Documents\Papors\Chatnotes\CHat translates and clean\Weber restart\Weber_Cumulative_ThreeVolumes_Batch81_Vol2_Sections125_131_SIZE_CONTROLLED_20260604`
- Verdict: **SOURCE-CHECKABLE PACKAGE SHAPE OK**
- Counts: `13` PDFs, `8` TeX files, `38` images, `46` scan/source-like files, `8` README/manifest/audit files.
- Source-witness samples:
  - `01_new_work_current_batch81/volume_2_sections125_131/german/pdf/weber_vol2_batch81_sections125_131_german_source.pdf`
  - `01_new_work_current_batch81/volume_2_sections125_131/german/tex/weber_vol2_batch81_sections125_131_german_source.pdf`
  - `02_cumulative_work/volume_1_complete/german/pdf/weber_volume1_cumulative_complete_german_source.pdf`
  - `02_cumulative_work/volume_2_available/german/pdf/weber_volume2_cumulative_available_through_sections1_131_german_source.pdf`
  - `02_cumulative_work/volume_2_available/german/tex/weber_volume2_cumulative_available_through_sections1_131_german_source.pdf`
- PDF samples:
  - `01_new_work_current_batch81/volume_2_sections125_131/english/pdf/weber_vol2_batch81_sections125_131_english_translation.pdf`
  - `01_new_work_current_batch81/volume_2_sections125_131/english/tex/weber_vol2_batch81_sections125_131_english_translation.pdf`
  - `01_new_work_current_batch81/volume_2_sections125_131/german/pdf/weber_vol2_batch81_sections125_131_german_source.pdf`
  - `01_new_work_current_batch81/volume_2_sections125_131/german/tex/weber_vol2_batch81_sections125_131_german_source.pdf`
  - `02_cumulative_work/volume_1_complete/english/pdf/weber_volume1_cumulative_complete_english_translation.pdf`

### cleanup multilingual
- Latest item audited: `C:\Users\Floris\Documents\Papors\Chatnotes\CHat translates and clean\cleanup multilingual\CLAUDE_OUTPUT_SCRIPTS_AND_LESSONS`
- Verdict: **NO PDF/TEX PAYLOAD FOUND**
- Counts: `0` PDFs, `0` TeX files, `0` images, `0` scan/source-like files, `1` README/manifest/audit files.
- Source-witness samples: none obvious from filenames.

### dedekind
- Latest item audited: `C:\Users\Floris\Documents\Papors\Chatnotes\CHat translates and clean\dedekind\DR15_V1I_p18_26`
- Verdict: **SOURCE-CHECKABLE PACKAGE SHAPE OK**
- Counts: `5` PDFs, `4` TeX files, `0` images, `1` scan/source-like file, `1` README/manifest/audit file.
- Source-witness samples:
  - `01_new/src/src_p18_26.pdf`
- PDF samples:
  - `01_new/de/de.pdf`
  - `01_new/en/en.pdf`
  - `01_new/src/src_p18_26.pdf`
  - `02_cum/de/cum_de.pdf`
  - `02_cum/en/cum_en.pdf`

### Noether Multilingual
- Latest item audited: `C:\Users\Floris\Documents\Papors\Chatnotes\CHat translates and clean\Noether Multilingual\Noether_Paper43_final_RA01_ES_JA_20260604.zip`
- Verdict: **SOURCE-CHECKABLE PACKAGE SHAPE OK**
- Counts: `10` PDFs, `15` TeX files, `22` images, `19` scan/source-like files, `19` README/manifest/audit files.
- Promotion: published to `10.5281/zenodo.20544550`.
- Source-witness samples:
  - `N43_RA01_ESJA/05_scan/N43_scan.pdf`
  - `N43_RA01_ESJA/06_back/p01/P01_scan.pdf`
  - `N43_RA01_ESJA/06_back/p01/P01_audit.md`
  - `N43_RA01_ESJA/07_rend/scan/sc-001.png`
  - `N43_RA01_ESJA/07_rend/scan/sc-021.png`
- PDF samples:
  - `N40_ESJA_20260604/01_work/es/N40_ES.pdf`
  - `N40_ESJA_20260604/01_work/ja/N40_JA.pdf`
  - `N40_ESJA_20260604/02_cum/es/N40_cum_ES.pdf`
  - `N40_ESJA_20260604/02_cum/ja/N40_cum_JA.pdf`
  - `N40_ESJA_20260604/04_ctrl/de/N40_DE.pdf`

### SGA restart
- Latest item audited: `C:\Users\Floris\Documents\Papors\Chatnotes\CHat translates and clean\SGA restart\sga7i_423_469`
- Verdict: **SOURCE-CHECKABLE PACKAGE SHAPE OK**
- Counts: `20` PDFs, `1` TeX files, `72` images, `80` scan/source-like files, `2` README/manifest/audit files.
- Source-witness samples:
  - `Fr/sga7i_001_469_fr_source.pdf`
  - `Fr/sga7i_398_469_fr_source.pdf`
  - `Fr/sga7i_423_469_fr_source.pdf`
  - `Meta/contact/sheet_423_430.jpg`
  - `Meta/contact/sheet_431_438.jpg`
- PDF samples:
  - `En/sga7i_001_469_en.pdf`
  - `En/sga7i_398_469_en.pdf`
  - `En/sga7i_423_469_en.pdf`
  - `Fr/sga7i_001_469_fr_source.pdf`
  - `Fr/sga7i_398_469_fr_source.pdf`

### Cayley
- Latest item audited: `C:\Users\Floris\Documents\Papors\Chatnotes\CHat translates and clean\Cayley\Cayley_V1_pp009_012_seq_repair_20260604`
- Verdict: **SOURCE-CHECKABLE PACKAGE SHAPE OK**
- Counts: `4` PDFs, `1` TeX files, `0` images, `2` scan/source-like files, `1` README/manifest/audit files.
- Source-witness samples:
  - `SCAN/source_scan_cayley_vol01_printed_pp001_012_IA.pdf`
  - `SCAN/source_scan_cayley_vol01_printed_pp009_012_IA.pdf`
- PDF samples:
  - `PDF/cayley_vol01_pp001_012_cumulative_checked_to_p012.pdf`
  - `PDF/cayley_vol01_pp009_012_source_checked.pdf`
  - `SCAN/source_scan_cayley_vol01_printed_pp001_012_IA.pdf`
  - `SCAN/source_scan_cayley_vol01_printed_pp009_012_IA.pdf`

## Immediate Interpretation

- Correction after drill-down: `cleanup multilingual` latest item in the table is only the Claude scripts/lessons folder. The real adjacent payloads were `CLAUDE_OUTPUT_ARABIC_CHINESE_MATH` and `CLAUDE_OUTPUT_ALBATTANI`; both were inspected separately and have already been promoted into the Chinese classics and al-Battani Zenodo/GitHub records.
- Correction after drill-down: `dedekind/DR15_V1I_p18_26` does include a source witness PDF at `01_new/src/src_p18_26.pdf`; the quick filename heuristic missed it because the file uses `src` rather than `source` or `scan`.
- Packages with both TeX/PDF and explicit source scans or source-witness slices are structurally safe to consider for GitHub/Zenodo sweep after ordinary render/text checks.
- Packages lacking obvious source witnesses should stay as drafts or source-intake TODOs until the source PDF/page-slice is added or located.
- Packages with screenshot/placeholder markers need visual inspection before front-facing promotion. Screenshots can be useful as witnesses, but not as substitutes for editable TeX or source scans.
- This audit does not validate translation fidelity, theorem numbering, formulas, or diagram correctness; it only prevents the worst failure mode: publishing a polished-looking package with no source witness trail.

## Second Sweep and Promotions

### SGA restart
- Latest item audited: `C:\Users\Floris\Documents\Papors\Chatnotes\CHat translates and clean\SGA restart\sga7i_470_504`
- Verdict: **SOURCE-CHECKABLE PACKAGE SHAPE OK**
- Source witnesses: `Src\sga7i_src_001_504.pdf`, `Src\sga7i_src_470_504.pdf`, plus full SGA 7-I / 7-II reference scans.
- Reader surface staged/published: SGA 7-I cumulative English/French readers through source page 504 and matching source-scan witness.
- Promotion: published to `10.5281/zenodo.20545214`.
- Next anchor from package README: source page 505, Expose IX section 14.

### Dirichlet
- Latest item audited: `C:\Users\Floris\Documents\Papors\Chatnotes\CHat translates and clean\Dirichlet\Dirichlet_R21_XXXVI_Gauss_20260604`
- Verdict: **SOURCE-CHECKABLE PACKAGE SHAPE OK**
- Source witnesses: `src\scans\36_gauss_letters_scan.pdf` and page PNGs `src\pages\v2_p0386.png` through `v2_p0400.png`.
- Reader surface staged/published: Werke Band II Papers I-XXXVI cumulative original-language and English PDFs.
- Promotion: published to `10.5281/zenodo.20545251`.

### Steinitz
- Latest item audited: `C:\Users\Floris\Documents\Papors\Chatnotes\CHat translates and clean\Steintz\Steinitz_20`
- Verdict: **SOURCE-CHECKABLE PACKAGE SHAPE OK, BUT NOT COMPLETE**
- Source witnesses: per-work source PDFs/scans; newly relevant `09_1912_rectII\source\rectII_source_p297-345.pdf`.
- Reader surface staged/published: 1910 field theory through sections 1-24; 1912 Rectangular Systems II partial German/English readers for printed pages 297-315; full 1912 source slice pp. 297-345 retained.
- Promotion: published to `10.5281/zenodo.20545258`.
- Remaining source-intake follow-up from package notes: 1906 Euler polyhedron-relations note and 1908 `Beitrage zur Analysis Situs`.

### Old Physics / Gibbs
- Latest item audited: `C:\Users\Floris\Documents\Papors\Chatnotes\CHat translates and clean\old physics\GibbsV1_P3_p085_094`
- Verdict: **SOURCE-CHECKABLE PACKAGE SHAPE OK, STAGED ONLY**
- Source witnesses: `Cum_p055_094\SCAN\...` and `Inst_p085_094\SCAN\...`.
- Reader surface found: Gibbs Volume I cumulative p055-094 and instant p085-094 TeX/PDF/SCAN.
- Action: held for now because no dedicated old-physics/Gibbs Zenodo helper/DOI is wired yet; avoid creating a stray DOI before the record strategy is clear.
