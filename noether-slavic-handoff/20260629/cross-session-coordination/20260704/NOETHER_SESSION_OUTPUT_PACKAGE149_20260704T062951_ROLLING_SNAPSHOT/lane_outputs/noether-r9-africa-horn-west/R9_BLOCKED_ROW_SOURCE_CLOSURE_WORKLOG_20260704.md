# R9 Blocked Row Source/OCR/Licensing Closure Worklog

Generated: 2026-07-04

Purpose: record exact closure work performed for rows where corpus translation is not yet responsible. This complements the micro-slice packet and prevents blocked rows from being mistaken for silence or idling.

## Exact Closure Checks Performed

| Row | Exact checked state | Closure decision |
| --- | --- | --- |
| Hausa | pass2 CSV has 5 rows; all `usable_for_term_ledger=false`; book/app route, weak glossary, AJOL retry, ethnomathematics context, and public register route are all non-promotable | no Hausa micro-translation; next work is content/license/reviewer return |
| Igbo | pass2 ledger strengthens basic math book route but only metadata/landing-page content is local; weak vocabulary/context routes are non-authoritative | no Igbo micro-translation; next work is source-cleared textbook/glossary or reviewer return |
| Amharic | pass2 CSV has 48 rows: 3 `extractable_ethiopic_text`, 1 `empty_extraction`, 44 `font_garbled_or_non_unicode_extraction`; extractable rows are Grade 2 Chapter 10 and Grade 6 Chapters 4 and 7 | no Amharic micro-translation; next work is OCR/font-map repair and review of the 3 extractable rows |
| Afar | pass2 CSV has 16 rows: 5 captured PDFs, 6 captured HTML, 3 captured oEmbed JSON, 2 failures; the 3 direct math-media leads all require transcript or reviewer | no Afar micro-translation; next work is transcript/audio review and source permission |
| Somali/Oromo | current pass2 CSV has 168 rows; Oromo has 83 downloaded PDFs and 70 extractable Latin-text rows; Somali has 74 downloaded PDFs and 62 extractable Latin-text rows | micro-slices allowed as source-backed support only; proof prose and hard algebra blocked |
| Tigrigna/Tigrinya | current pass2 CSV has 84 candidates: 82 downloaded PDFs, 53 extractable Ethiopic-text rows, 29 weak/empty extraction rows, 2 failures | micro-slices allowed for clean UTF-8 elementary rows only; Grade 8 algebra and hard rows blocked |
| West African glossary rows | Fulfulde/Fulani, Mandinka, Twi/Akan, Wolof, and Yoruba ledgers have concrete glossary/dictionary rows but no reviewer/source-permission clearance | reviewer-prompt micro-slices allowed; no canonical terms or prose |
| AF-05 | Dinka/Nuer/Zande ingest is backlink/request-packet only; no accepted terms | reviewer/authority return required |
| AF-06 | Khoekhoegowab/Juhoansi has 36 source-anchor/page-navigation rows; exact local-label transcription and reviewer return missing | reviewer-question ledger required |

## Direct Afar Math-Media Leads Requiring Transcript/Review

- `youtube_qafar_grade12_math_1`: `https://www.youtube.com/watch?v=t0JXbOMa0Cw`
- `youtube_qafar_grade12_math_2`: `https://www.youtube.com/watch?v=N-DlDwwiGrQ`
- `youtube_qafar_grade10_math_seenanti`: `https://www.youtube.com/watch?v=00fQ3PD1W4s`

## Amharic Extractable Rows For Review, Not Translation

- Row 14: Grade 2 in Amharic, Chapter 10, `extractable_ethiopic_text`, 217 Ethiopic characters.
- Row 45: Grade 6 in Amharic, Chapter 4, `extractable_ethiopic_text`, 4804 Ethiopic characters.
- Row 48: Grade 6 in Amharic, Chapter 7, `extractable_ethiopic_text`, 15930 Ethiopic characters.

Row 25 is `empty_extraction` and is not usable as a text witness.

## Closure Rule

A blocked row becomes draft-support eligible only after one of these exact returns exists:

- source-cleared local text/PDF with extractable text or verified transcription;
- rendered-page transcription with source page and reviewer/source basis;
- explicit reviewer or authority return with row-level decisions;
- packet-specific license/attribution snapshot for any derivative/OER use.

