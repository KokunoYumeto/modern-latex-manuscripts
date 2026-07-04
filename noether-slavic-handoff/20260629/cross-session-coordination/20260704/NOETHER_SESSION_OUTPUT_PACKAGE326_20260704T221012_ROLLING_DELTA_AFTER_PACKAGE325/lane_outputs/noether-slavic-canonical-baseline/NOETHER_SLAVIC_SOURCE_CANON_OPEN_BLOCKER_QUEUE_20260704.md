# Noether Slavic Source-Canon Open Blocker Queue - 2026-07-04

Scope: operational queue for the source-canon-first lane. It separates open source blockers from stable local witness watch states and records what exact event would justify promotion or rebuild work.

Boundary: no native review, canonical approval, license clearance, accepted correction, translation completion, or reader mutation is claimed.

## Summary

- Queue rows: 14
- Open source blockers: 4
- Stable witness watch-only rows: 10
- Active rebuild triggers present: 0
- Permission/review/translation claims present: 0

## Open Source Blockers

| priority | language | exact_blocker | action_route | promotion_trigger_required |
|---|---|---|---|---|
| P1_open_blocker | Bosnian | Official PMF/COBISS controls exist; third-party Scribd mirror/preview lead exists; official fulltext/source or permission-clean copy remains blocked. | official PMF Sarajevo textbook/fulltext/source route; COBISS/PMF controls are already cached; avoid third-party mirror promotion | Official PMF fulltext/source, stable source-package, or documented permission/reviewer confirmation for the 2017 textbook. |
| P1_open_blocker | Interslavic/Panslavic | Wikimedia/Incubator Algebra raw wikitext is cached; no publication/source-package authority or qualified review exists. | publication-level Interslavic/Panslavic mathematical source or qualified review route; Wikimedia web text remains scouting-only | Publication-level source, stable source package, or qualified review establishing specific terms. |
| P1_open_blocker | Sorbian Lower | WITAJ/Yumpu bibliography is cached; Lower Sorbian terminology booklet body is not locally inspected. | WITAJ/Domowina booklet or corpus body route; current evidence is bibliography/listing control only | Booklet/corpus body cached with term evidence or qualified Lower Sorbian review return. |
| P1_open_blocker | Sorbian Upper | Domowina/Sorbian Institute source-list controls are cached; booklet/corpus term body is not locally inspected. | Domowina/Sorbian Institute booklet or corpus body route; current evidence is title/source-list control only | Booklet/corpus body cached with term evidence or qualified Upper Sorbian review return. |

## Stable Witness Watch

| priority | language | current_state | rebuild_trigger_required |
|---|---|---|---|
| P2_watch_recent_promotion | Belarusian | stable_local_pdf_fulltext_witness_ocr_quality_watch | Rebuild only on PDF/OCR hash drift, cleaner OCR acceptance, official/source-package evidence, or qualified Belarusian review return. |
| P2_watch_recent_promotion | Macedonian | stable_local_fulltext_witness_recently_promoted_no_tex | Rebuild if UKIM/UCG source hash drifts, official source package appears, or accepted review/source-defect evidence lands. |
| P2_watch_recent_promotion | Montenegrin | stable_local_fulltext_witness_recently_promoted_no_tex | Rebuild if UKIM/UCG source hash drifts, official source package appears, or accepted review/source-defect evidence lands. |
| P3_watch_stable_witness | Bulgarian | stable_local_pdf_text_witnesses_no_tex | No rebuild from this matrix alone; rebuild only on hash drift, accepted correction, source defect, or new official source witness. |
| P3_watch_stable_witness | Croatian | stable_local_pdf_text_witnesses_no_tex | No rebuild from this matrix alone; rebuild only on hash drift, accepted correction, source defect, or new official source witness. |
| P3_watch_stable_witness | Czech | stable_local_pdf_text_witnesses_no_tex | No rebuild from this matrix alone; rebuild only on hash drift, accepted correction, source defect, or new official source witness. |
| P3_watch_stable_witness | Polish | stable_local_pdf_text_witnesses_no_tex | No rebuild from this matrix alone; rebuild only on hash drift, accepted correction, source defect, or new official source witness. |
| P3_watch_stable_witness | Serbian | stable_local_pdf_text_witnesses_no_tex | No rebuild from this matrix alone; rebuild only on hash drift, accepted correction, source defect, or new official source witness. |
| P3_watch_stable_witness | Slovak | stable_local_pdf_text_witnesses_no_tex | No rebuild from this matrix alone; rebuild only on hash drift, accepted correction, source defect, or new official source witness. |
| P3_watch_stable_witness | Slovenian | stable_local_pdf_text_witnesses_no_tex | No rebuild from this matrix alone; rebuild only on hash drift, accepted correction, source defect, or new official source witness. |

## No-Trigger Rule

No queue row currently has an active rebuild trigger. Do not resume translation/render/package churn from this queue. Resume only if a queue route produces new official or permission-clean source evidence, source-level TeX/e-print package evidence, accepted source defect/correction, hash drift, or qualified review return.
