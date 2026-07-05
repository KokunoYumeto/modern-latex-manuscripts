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
| P1_open_blocker | Bosnian | Official PMF/current COBISS Plus/staff-page controls exist; third-party Scribd mirror/preview lead exists; official fulltext/source or permission-clean copy remains blocked. | official PMF Sarajevo textbook/fulltext/source route; current COBISS Plus and PMF controls are already cached; avoid third-party mirror promotion | Official PMF fulltext/source, stable source-package, or documented permission/reviewer confirmation for the 2017 textbook. |
| P1_open_blocker | Interslavic/Panslavic | Stable isv.wikipedia/Incubator Algebra raw wikitext, Steen dictionary controls, medzuslovjansky/slovnik dictionary source-package lexicon evidence, wiki revision/API controls, and arXiv route probes are cached; no publication-level mathematical authority, target-language TeX/e-print mathematical source, or qualified review exists. | publication-level Interslavic/Panslavic mathematical source, target-language mathematical TeX/e-print source package, or qualified review route; Wikimedia, Steen dictionary, slovnik source-package, and arXiv route evidence remain scouting-only | Publication-level mathematical source, TeX/e-print/source package for a mathematical text, or qualified review establishing specific terms. |
| P1_open_blocker | Sorbian Lower | WITAJ/BVS/eOPAC catalog-body-route controls and Sorbian Institute Hunspell source-package lexicon evidence are cached; Lower Sorbian terminology booklet body is not locally inspected. | WITAJ/Domowina/BVS booklet or corpus body route; current evidence is catalog/body-route plus Hunspell source-package lexicon control only | Booklet/corpus body cached with term evidence or qualified Lower Sorbian review return. |
| P1_open_blocker | Sorbian Upper | WITAJ/Domowina/Sorbian Institute/BVS/SorBib/soblex catalog and source-package lexicon controls are cached; booklet/corpus term body is not locally inspected. | Domowina/Sorbian Institute/BVS/SorBib/soblex booklet or corpus body route; current evidence is catalog/source-list plus source-package lexicon control only | Booklet/corpus body cached with term evidence or qualified Upper Sorbian review return. |

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
