# Noether R823 — Slavic book reconciliation

This workspace resumes the existing Slavic/Interslavic manager lane. It does not create a new task and does not narrow the manager's standing responsibility for translating every work into its target languages.

## Current production result

The first genuinely missing R823 lecture-book unit, `BOOK_TITLE_INTRO`, has been translated directly from the exact German R823 authority into:

- Ukrainian;
- Russian;
- Interslavic Latin;
- deterministic Interslavic Cyrillic (a reader script of the same Interslavic translation).

Each target has a compiled three-page PDF. All four builds pass the structural/log/font audit, and all twelve rendered pages were visually inspected. This is internal source/build/visual QA, not external or community certification.

The completed unit is 1 of 32 core lecture-book units (`BOOK_TITLE_INTRO` plus `BOOK_S01` through `BOOK_S31`). `BOOK_REVIEWS` is a separate terminal source unit. The next cursor is `BOOK_S01`.

## Why the older Post44 files were not promoted

The surviving four-lane Post44 translations and cumulative readers are real prior work, but their German witness is not source-equivalent to R823. Its opening material is mostly a short synopsis, omits §17 from the visible section map, and only becomes long-form chiefly in §§22–31. They are retained as translation memory and control witnesses, not treated as complete R823 translations.

See `evidence/OLD_POST44_VS_R823_RECONCILIATION.md` for hashes and disposition.

## Fable 5 state

Fable Tranche 001 was a Paper 06 orthography-only pilot: line-wide, TeX-aware, idempotent `vzet-→vzęt-`, `obšč-→obć-`, `dlugost-→dolgost-`, and `vobče/voobče→obće`, followed by same-run Cyrillic regeneration and PDF checks. That work was already completed on 2026-07-16: 9 changed files, 17 replacements, 16 Latin plus 16 Cyrillic successful builds, visual checks, and a hashed handoff ZIP.

Tranche 002 remains gated. The ring family, `ręd`, `jednako`, `važiti`, and `slučaj` wording remain held. This R823 unit therefore keeps corpus-primary `kolco` and does not apply the gated citation switches.

See `evidence/FABLE_TRANCHE001_STATUS.md` and `evidence/TERMINOLOGY_LEDGER.csv`.

## Research-method correction applied

Provenance and routing are represented in `evidence/TYPED_EVIDENCE_GRAPH.json`. Slavic dependence and breadth are represented in `evidence/FAMILY_COHORT_TREE.json`. No scalar score is allowed to auto-select terminology, infer missing branch support, or claim community certification. W0 is a projection and unified v6.2 readiness is rejected.

## Continuation

The next source unit is R823 lines 21061–21088, `BOOK_S01`, SHA-256 `0F1710DAE06E6F55E55E84904AD8D5FA0789C3C56A057E9FBB43F955A34A3A04`. Continue all four target artifacts from the same exact authority; regenerate Cyrillic from Latin and compile all PDFs before accepting the tranche.
