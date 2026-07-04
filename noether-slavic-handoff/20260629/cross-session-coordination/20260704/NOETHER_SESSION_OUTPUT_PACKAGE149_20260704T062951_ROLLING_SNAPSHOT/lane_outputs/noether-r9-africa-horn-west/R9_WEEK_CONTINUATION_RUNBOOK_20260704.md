# R9 Week Continuation Runbook

Generated: 2026-07-04

Purpose: allow the R9 Africa/Horn/West Africa lane to continue for a week without pause or state loss.

## Non-Negotiable Rules

- Do not push Git. Session B packages/pushes.
- Do not claim accepted terms, pilot readiness, native/community review, or license approval.
- Append new work to `R9_DURABLE_RUN_LOG_20260704.md` or a dated successor.
- Keep every row either `draft_support`, `reviewer_prompt_only`, or `blocked_exact_closure`.
- Route novel cross-family register ideas to Session D instead of inventing bridge surfaces here.

## Day-Scale Work Order

| Priority | Work slice | Inputs | Output to create | Done when |
| --- | --- | --- | --- | --- |
| 1 | Amharic OCR/font-map triage | `R9_AMHARIC_FULL_SHELF_SOURCE_RETURN_PASS2_20260703T164546Z.csv`; PDFs for rows 14, 45, 48 and sample garbled rows | `R9_AMHARIC_OCR_FONTMAP_TRIAGE_<timestamp>.md/json/csv` | each tested row is classified as Unicode-good, OCR-needed, font-map-needed, or page-transcription-needed |
| 2 | Tigrigna Grade 8 algebra repair | `R9_TIGRIGNA_TIGRINYA_SCRIPT_AWARE_STEM_LEDGER_20260703T142919Z.*`; Grade 8 source PDF/text | `R9_TIGRIGNA_GRADE8_FONT_REPAIR_AND_SCRIPT_REVIEW_<timestamp>.md/json/csv` | algebra/equation/variable pages are either repaired or explicitly page-review blocked |
| 3 | Afar transcript/source return | `R9_AFAR_USABLE_MATH_STEM_SOURCE_RETURN_PASS2_20260703T165443Z.csv`; three YouTube/oEmbed leads | `R9_AFAR_TRANSCRIPT_OR_REVIEWER_RETURN_<timestamp>.md/json/csv` | each media lead has transcript status, source permission note, and reviewer question |
| 4 | Hausa/Igbo content closure | Hausa and Igbo pass2 ledgers | `R9_HAUSA_BOOK_CONTENT_OR_REVIEWER_RETURN_<timestamp>` and `R9_IGBO_TEXTBOOK_CONTENT_OR_REVIEWER_RETURN_<timestamp>` | book/app/metadata routes have exact content availability and license/reuse status |
| 5 | Somali/Oromo proof-language packet | Somali/Oromo ledgers and pass2 shelf | `R9_SOMALI_OROMO_PROOF_LANGUAGE_REVIEW_PACKET_<timestamp>.md/json/csv` | definition/theorem/proof alternatives are reviewer-facing, source-linked, and non-promoted |
| 6 | West African reviewer packets | Fulfulde, Mandinka, Twi, Wolof, Yoruba ledgers | `R9_WEST_AFRICAN_GLOSSARY_REVIEW_PACKET_<timestamp>.md/json/csv` | variant/scope/proof/hard-row questions are split by language and source |
| 7 | AF-05/AF-06 closure | AF-05 and AF-06 ingests | `R9_AF05_REVIEWER_RETURN_QUEUE_<timestamp>` and `R9_AF06_REVIEWER_QUESTION_LEDGER_<timestamp>` | Dinka/Nuer/Zande and Khoekhoegowab/Juhoansi rows have exact source/reviewer fields |

## Reader Integration/Fix Pass Rule

R9 can be called "complete as far as responsible" only if:

1. every named row in `R9_WHOLE_LANE_COVERAGE_MANIFEST_20260704.json` has either draft support or exact blockers;
2. the durable run log records the source, OCR/licensing choice, motivation, reviewer question, and blocker for that row;
3. no unresolved local source evidence is ignored merely because it is inconvenient.

After that proof, a worker may move to a completed-reader integration/fix pass such as Zenodo/package hygiene or another reader lane. Before moving, append a run-log entry stating:

- why R9 is complete as far as responsible;
- which reader/integration pass is next;
- which R9 artifacts Session B should package or reference;
- which R9 rows remain blocked for future reviewer/source return.

