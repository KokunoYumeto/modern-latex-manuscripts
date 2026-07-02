# Visual Inspection Coverage Ledger

- Generated UTC: `2026-07-02T00:35:07Z`
- Completion claim: `False`
- Render PDFs scanned: `2115`
- Visual-inspection files found: `328`
- New visual inspection performed: `False`

## Lane Summary

| Lane | PDFs | With visual/render refs | Needing inspection | Pages counted | Unknown pages |
|---|---:|---:|---:|---:|---:|
| french | 216 | 216 | 0 | 25590 | 0 |
| interslavic_cyrillic | 429 | 429 | 0 | 4892 | 0 |
| interslavic_latin | 429 | 429 | 0 | 4684 | 0 |
| japanese | 4 | 4 | 0 | 1477 | 0 |
| other | 8 | 8 | 0 | 51 | 0 |
| russian | 429 | 429 | 0 | 5062 | 0 |
| simplified_chinese | 112 | 102 | 10 | 1533 | 0 |
| spanish | 50 | 50 | 0 | 20605 | 0 |
| ukrainian | 430 | 430 | 0 | 4888 | 0 |

## Priority Queue

- `renders/non_slavic/simplified_chinese_canonical_noto_batch_20260630/font_option_test_20260630/font_option_test.pdf` (simplified_chinese, pages `1`): needs_visual_inspection_before_promotion
- `renders/non_slavic/simplified_chinese_canonical_noto_batch_20260630/font_option_test_20260630/font_option_test_explicit.pdf` (simplified_chinese, pages `1`): needs_visual_inspection_before_promotion
- `renders/non_slavic/simplified_chinese_canonical_noto_batch_20260630/font_option_test_20260630/font_option_test_math.pdf` (simplified_chinese, pages `1`): needs_visual_inspection_before_promotion
- `renders/non_slavic/simplified_chinese_canonical_noto_batch_20260630/font_option_test_20260630/font_option_test_sc.pdf` (simplified_chinese, pages `1`): needs_visual_inspection_before_promotion
- `renders/non_slavic/simplified_chinese_paper22_through_section02_20260629/Noether_Paper22_Through_Section02_SimplifiedChinese_working_localfont.pdf` (simplified_chinese, pages `5`): needs_visual_inspection_before_promotion
- `renders/non_slavic/simplified_chinese_paper22_through_section03_20260629/Noether_Paper22_Through_Section03_SimplifiedChinese_working_localfont.pdf` (simplified_chinese, pages `7`): needs_visual_inspection_before_promotion
- `renders/non_slavic/simplified_chinese_paper22_through_section04_20260629/Noether_Paper22_Through_Section04_SimplifiedChinese_working_localfont.pdf` (simplified_chinese, pages `10`): needs_visual_inspection_before_promotion
- `renders/non_slavic/simplified_chinese_paper22_through_section05_20260629/Noether_Paper22_Through_Section05_SimplifiedChinese_working_localfont.pdf` (simplified_chinese, pages `12`): needs_visual_inspection_before_promotion
- `renders/non_slavic/simplified_chinese_paper22_through_section06_20260629/Noether_Paper22_Through_Section06_SimplifiedChinese_working_localfont.pdf` (simplified_chinese, pages `14`): needs_visual_inspection_before_promotion
- `renders/non_slavic/simplified_chinese_paper24_source_fidelity_20260629/hyperfalse_test/Noether_Paper24_SourceFidelity_SimplifiedChinese_v001_localfont_hyperfalse.pdf` (simplified_chinese, pages `14`): needs_visual_inspection_before_promotion

## Rules

- Before public promotion of any cumulative reader, require explicit visual inspection notes or contact-sheet evidence for sampled front/middle/back pages and any known dense formula/table pages.
- A successful TeX compile is not the same as visual inspection.
- A render-log reference can support continuity but does not by itself close native/external authority gates.
- When a correction changes TeX that affects layout, regenerate the PDF and refresh visual inspection evidence.
