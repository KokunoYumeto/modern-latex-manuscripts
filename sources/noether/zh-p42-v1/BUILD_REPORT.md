# Noether Paper 42 — mechanical build report

Claim class: **computation only**. Compiler execution and file custody are recorded here; no source, semantic, formula, terminology, visual, regional, human, or publication validation is claimed.

## Compiler

- Engine: XeTeX/XeLaTeX `3.141592653-2.6-0.999998`, MiKTeX `26.5`.
- Invocation: `xelatex -interaction=nonstopmode -halt-on-error <target.tex>`.
- Passes: two successful passes per target.
- Result: every invocation returned exit code `0`; each final transcript reports five pages.

## zh-Hans-CN

- TeX SHA-256: `B326FA4696A29D4B6393E85651FDF07EF072C452CAB3BDD93A9BB271285E6625`.
- PDF SHA-256: `D27ABE145A7FCD5F3BF6BF80245E7560A2FB6CDDC5889D72D5F834BB9174A7BC`.
- Log SHA-256: `E5015EF3A5CCE298DF38333C0FAB7A4B145C86E0EDE2953A1B94393F650E5635`.
- Final transcript: one unavailable italic font-shape warning plus the summary substitution warning; no fatal error and no undefined control sequence.

## controlled-generic zh-Hant

- TeX SHA-256: `8D8EE8B75EB83D90B03BD646E8453D6C0E0CBCF72B08452005185A482C131F57`.
- PDF SHA-256: `1263EC5E734E700C3B63D301582BF97C2F5EB9B333FED0FC4DB63F08B9F54A12`.
- Log SHA-256: `BC600AE0E1DF4CD4EE74F29CC83964714B279D70FC9CC87AEC02AF09411B6142`.
- Final transcript: one unavailable italic font-shape warning plus the summary substitution warning; no fatal error and no undefined control sequence.

The Hant artifact is controlled generic only and is not `zh-Hant-TW`, `zh-Hant-HK`, or `zh-Hant-MO` localization.

## Hant production custody

- Producer script SHA-256: `4796DAFADFFE4CC426D1EF79E54173829A3C55D09697883E1F7FE5E43A0CFD1F`.
- OpenCC producer record SHA-256: `36C8AC62CEDE3EE4D9C37A340B6A7DDC9BB22CAD78D77A564BE4A16AA351D70C`.
- Converter: `opencc-python-reimplemented` `0.1.7`, `s2t`, followed by recorded controlled normalizations.

## Evidence transport formatting

The evidence producer emitted one extra terminal blank record in each CSV. `qa/normalize_evidence_csv_newline.py` removed only those terminal blank records and wrote `qa/EVIDENCE_CSV_NEWLINE_RECORD.json`. No terminology cell was changed. Final CSV parsing reports 20 rectangular data rows in each ledger.

## Required independent work

No PDF page was rendered or viewed by this translation lane. Independent source, translation, formula, terminology, visual, and regional checking remains pending.
