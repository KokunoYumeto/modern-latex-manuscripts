# R9 P1 OCR/Unicode Repair Sample Audit

Generated: 2026-07-05T01:32:23.088813+00:00 UTC

## Boundary

This artifact performs diagnostic text-layer sampling only on representative `P1` queue rows. It records script/count diagnostics and repair actions. It saves no source text excerpts, translates nothing, approves no terms, clears no licenses, claims no review, promotes no gates, packages nothing, and pushes nothing.

## Coverage

- Sampled P1 rows: 16
- Hash mismatches against queue: 0
- Reader/extraction errors: 0
- Source text excerpts saved: 0

## Priority Counts

| priority | count |
|---|---:|
| P1A | 5 |
| P1B | 5 |
| P1C | 6 |

## Diagnostic Decisions

| decision | count |
|---|---:|
| amharic_font_garbled_or_non_unicode_confirmed | 5 |
| latin_text_layer_weak_or_mojibake_needs_repair_or_transcript | 6 |
| tigrigna_ethiopic_text_present_but_render_compare_required | 3 |
| tigrigna_text_layer_weak_or_non_unicode_needs_ocr | 2 |

## Sample Rows

| audit | priority | row | chars | Ethiopic | Latin | decision | next action |
|---|---|---|---:|---:|---:|---|---|
| R9-P1-OCR-001 | P1A | Amharic R9-LSB-0001 | 8 | 0 | 0 | amharic_font_garbled_or_non_unicode_confirmed | Render matching pages and run Amharic OCR/font-map repair; do not trust text layer until Ethiopic page comparison passes. |
| R9-P1-OCR-002 | P1A | Amharic R9-LSB-0002 | 120 | 0 | 0 | amharic_font_garbled_or_non_unicode_confirmed | Render matching pages and run Amharic OCR/font-map repair; do not trust text layer until Ethiopic page comparison passes. |
| R9-P1-OCR-003 | P1A | Amharic R9-LSB-0003 | 12 | 0 | 0 | amharic_font_garbled_or_non_unicode_confirmed | Render matching pages and run Amharic OCR/font-map repair; do not trust text layer until Ethiopic page comparison passes. |
| R9-P1-OCR-004 | P1A | Amharic R9-LSB-0004 | 12 | 0 | 0 | amharic_font_garbled_or_non_unicode_confirmed | Render matching pages and run Amharic OCR/font-map repair; do not trust text layer until Ethiopic page comparison passes. |
| R9-P1-OCR-005 | P1A | Amharic R9-LSB-0005 | 320 | 0 | 59 | amharic_font_garbled_or_non_unicode_confirmed | Render matching pages and run Amharic OCR/font-map repair; do not trust text layer until Ethiopic page comparison passes. |
| R9-P1-OCR-006 | P1B | Tigrigna/Tigrinya R9-LSB-0221 | 133 | 81 | 0 | tigrigna_ethiopic_text_present_but_render_compare_required | Render sampled pages and compare Ethiopic extraction with page images before any source-canon text use. |
| R9-P1-OCR-007 | P1B | Tigrigna/Tigrinya R9-LSB-0222 | 88 | 36 | 0 | tigrigna_ethiopic_text_present_but_render_compare_required | Render sampled pages and compare Ethiopic extraction with page images before any source-canon text use. |
| R9-P1-OCR-008 | P1B | Tigrigna/Tigrinya R9-LSB-0230 | 80 | 36 | 0 | tigrigna_ethiopic_text_present_but_render_compare_required | Render sampled pages and compare Ethiopic extraction with page images before any source-canon text use. |
| R9-P1-OCR-009 | P1B | Tigrigna/Tigrinya R9-LSB-0235 | 81 | 0 | 0 | tigrigna_text_layer_weak_or_non_unicode_needs_ocr | Render sampled pages and compare Ethiopic extraction with page images before any source-canon text use. |
| R9-P1-OCR-010 | P1B | Tigrigna/Tigrinya R9-LSB-0236 | 452 | 0 | 125 | tigrigna_text_layer_weak_or_non_unicode_needs_ocr | Render sampled pages and compare Ethiopic extraction with page images before any source-canon text use. |
| R9-P1-OCR-011 | P1C | Oromo R9-LSB-0051 | 6 | 0 | 0 | latin_text_layer_weak_or_mojibake_needs_repair_or_transcript | Compare Latin extraction to rendered pages; if weak, rerun extraction/OCR or request owner/reviewer transcript. |
| R9-P1-OCR-012 | P1C | Oromo R9-LSB-0052 | 9 | 0 | 0 | latin_text_layer_weak_or_mojibake_needs_repair_or_transcript | Compare Latin extraction to rendered pages; if weak, rerun extraction/OCR or request owner/reviewer transcript. |
| R9-P1-OCR-013 | P1C | Oromo R9-LSB-0053 | 9 | 0 | 0 | latin_text_layer_weak_or_mojibake_needs_repair_or_transcript | Compare Latin extraction to rendered pages; if weak, rerun extraction/OCR or request owner/reviewer transcript. |
| R9-P1-OCR-014 | P1C | Somali R9-LSB-0135 | 6 | 0 | 0 | latin_text_layer_weak_or_mojibake_needs_repair_or_transcript | Compare Latin extraction to rendered pages; if weak, rerun extraction/OCR or request owner/reviewer transcript. |
| R9-P1-OCR-015 | P1C | Somali R9-LSB-0136 | 9 | 0 | 0 | latin_text_layer_weak_or_mojibake_needs_repair_or_transcript | Compare Latin extraction to rendered pages; if weak, rerun extraction/OCR or request owner/reviewer transcript. |
| R9-P1-OCR-016 | P1C | Somali R9-LSB-0137 | 9 | 0 | 0 | latin_text_layer_weak_or_mojibake_needs_repair_or_transcript | Compare Latin extraction to rendered pages; if weak, rerun extraction/OCR or request owner/reviewer transcript. |

CSV: `C:\Users\memo_\Documents\Codex\2026-07-04\noether-r9-africa-horn-west\outputs\R9_P1_OCR_UNICODE_REPAIR_SAMPLE_AUDIT_20260705.csv`
