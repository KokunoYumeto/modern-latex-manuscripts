# Noether R7 Active Row Source-Canon Sufficiency Classification

Generated: 2026-07-05

Purpose: classify each active row in the R7 source-canon witness table under
the GitHub-visible source-canon sufficiency transition.

Input table:

- `NOETHER_R7_SOURCE_CANON_MATH_CORPUS_WITNESS_ROWS_20260704.csv`

Output rows:

- `NOETHER_R7_ACTIVE_ROW_SOURCE_CANON_SUFFICIENCY_CLASSIFICATION_ROWS_20260705.csv`

## Result

- Witness rows classified: 59
- Source-canon sufficient for scoped draft work: 15
- Source-canon insufficient: 44

## Bucket Rule

Rows are `source-canon sufficient for scoped draft work` only when they have
target-language mathematical topic/register evidence strong enough for a
bounded draft support task:

- Indonesian proof/specialist rows `MI-ID-PROOF-*` and `MI-ID-SPEC-*` with
  extracted PDF/text algebra/proof witnesses.
- Malaysian Malay course/register rows `MI-MY-COURSE-*` and the limited Malay
  abstract/register row `MI-MY-SPEC-01`, with scope restricted to course or
  abstract register support and not full proof translation.

Rows remain `source-canon insufficient` when they are comparator-only,
title-only, route-only, lower-math, language-context, source-package context
unrelated to mathematical proof prose, download-blocked, or explicit source
gap rows.

## Boundaries

- PRPM/MABBIM and glossary rows are comparator/search/register evidence only.
- Brunei/Singapore route rows remain exact-content gaps.
- SEA/Pacific lower-math, glossary, title/listing, or blocked rows remain
  source-acquisition rows unless exact target-language higher-algebra content
  closes the source gate.
- The classification does not approve terms, claim native review, claim
  canonical approval, clear licenses, promote gates, claim completion, or push
  Git.

## Follow-On Artifacts

- Sufficient rows are expanded in
  `NOETHER_R7_ACTIVE_SUFFICIENT_ROW_DRAFT_SUPPORT_20260705.csv`.
- Insufficient rows are extracted in
  `NOETHER_R7_ACTIVE_ROW_SOURCE_CANON_INSUFFICIENT_ACQUISITION_ROWS_20260705.csv`.
