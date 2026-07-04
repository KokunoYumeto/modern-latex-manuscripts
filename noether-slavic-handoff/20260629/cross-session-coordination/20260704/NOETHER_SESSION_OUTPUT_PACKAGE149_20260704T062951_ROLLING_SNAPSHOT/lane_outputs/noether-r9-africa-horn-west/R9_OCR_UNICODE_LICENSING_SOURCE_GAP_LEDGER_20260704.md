# R9 OCR, Unicode, Licensing, and Source-Gap Ledger

Generated: 2026-07-04

Scope: Hausa, Igbo, Amharic, Afar, Somali, Oromo, Tigrigna/Tigrinya, related West African/Horn rows, and adjacent AF-05/AF-06 rows that belong to this source-evidence lane.

## Boundary

This is a blocker and next-action ledger. It does not approve licenses, accept terms, claim reviewer authority, start a pilot, or authorize any regional/interlanguage bridge. All blocker rows have `promotion_allowed=false`.

## Summary

| Lane | Primary blocker | Current evidence | Next concrete artifact |
| --- | --- | --- | --- |
| Hausa | content extraction and license/reuse unknown | SS1/SS2 `Mathematics in Hausa` book/app route strengthened, but content not local | `R9_HAUSA_BOOK_CONTENT_OR_REVIEWER_RETURN_<timestamp>.md/json/csv` |
| Igbo | source-cleared textbook/glossary content missing | basic Igbo mathematics book route is metadata-only; context PDFs captured | `R9_IGBO_TEXTBOOK_CONTENT_OR_REVIEWER_RETURN_<timestamp>.md/json/csv` |
| Amharic | OCR/Unicode/font extraction failure | 48 PDFs / 588 pages; 3 exact usable Unicode rows; 44 garbled/non-Unicode rows | `R9_AMHARIC_OCR_FONTMAP_TRIAGE_<timestamp>.md/json/csv` |
| Afar | transcript/local text missing | 14 of 16 routes captured; 5 PDFs / 232 pages; 3 Qafar/Afar math-media metadata leads | `R9_AFAR_TRANSCRIPT_OR_REVIEWER_RETURN_<timestamp>.md/json/csv` |
| Somali | proof-language and reviewer/license gates | 74 PDFs / 3446 pages; 19 seed rows reconfirmed | `R9_SOMALI_PROOF_LANGUAGE_REVIEW_QUEUE_<timestamp>.md/json/csv` |
| Oromo | OCR-normalization/proof-language/reviewer gates | 83 PDFs / 3444 pages; 29 seed rows reconfirmed | `R9_OROMO_PROOF_LANGUAGE_AND_ORTHOGRAPHY_REVIEW_QUEUE_<timestamp>.md/json/csv` |
| Tigrigna/Tigrinya | Grade 8 algebra extraction and script review | 82 PDFs / 3420 pages; 53 extractable Ethiopic rows; 33 seed rows reconfirmed | `R9_TIGRIGNA_GRADE8_FONT_REPAIR_AND_SCRIPT_REVIEW_<timestamp>.md/json/csv` |
| Fulfulde/Fulani | variety and source-permission review | 20 variant-aware glossary rows | `R9_FULFULDE_VARIANT_REVIEW_QUEUE_<timestamp>.md/json/csv` |
| Mandinka/Manding | Manding-wide scope blocked | 23 Mandinka-specific glossary rows | `R9_MANDINKA_REVIEW_QUEUE_<timestamp>.md/json/csv` |
| Akan/Twi | Akan-wide scope blocked | 24 Twi glossary rows plus Akan context-only sources | `R9_TWI_AKAN_SCOPE_REVIEW_QUEUE_<timestamp>.md/json/csv` |
| Wolof | register variants and higher-math gap | 26 glossary rows from math/science witnesses | `R9_WOLOF_VARIANT_REVIEW_QUEUE_<timestamp>.md/json/csv` |
| Yoruba | dictionary-only witness | 28 Yoruba dictionary-seed rows; no school/STEM prose witness | `R9_YORUBA_SCHOOL_STEM_SOURCE_RETRY_<timestamp>.md/json/csv` |
| OER candidates | packet-specific license/attribution not rechecked | OpenStax, OpenIntro, Beezer routes only | per-packet license/source snapshot before any derivative |
| AF-05 South Sudan | reviewer/official source route missing | Dinka/Nuer/Zande packet starter and checklist only | `R9_AF05_*_REVIEWER_RETURN_LEDGER_<timestamp>.md/json` |
| AF-06 Omotic/southern non-Bantu | local-label transcription and reviewer missing | Khoekhoegowab/Juhoansi source anchors and page navigation | `R9_AF06_*_REVIEWER_QUESTION_LEDGER_<timestamp>.md/json` |

## OCR/Unicode Triage Rules

- Treat terminal mojibake as display noise only when source files contain verified codepoints.
- Treat PDF extraction mojibake, font-encoded text, or empty extraction as a blocker until page images, font maps, OCR, or human transcription are available.
- Do not normalize apostrophes, diacritics, click symbols, Ethiopic characters, or Yoruba/Twi/Wolof/Fulfulde letters away from the source. Put any normalized form in a separate search-only field.
- For Amharic and Tigrigna/Tigrinya, source-image review is required before extracting algebra/proof rows from garbled pages.

## Licensing Rules

- Schoolbook/source captures are evidence for review routing, not a reuse grant.
- OER rows must recheck exact edition, license text, attribution, trademark/title constraints, and source route at packet time.
- App-store/book metadata is not source content and cannot feed a term ledger without content permission or reviewer/source return.
- NYU/NYSED glossary rows require source/permission and attribution checks before any public packet.

## Companion CSV

The companion CSV `R9_OCR_UNICODE_LICENSING_SOURCE_GAP_LEDGER_20260704.csv` lists row-level blockers and next artifacts.

