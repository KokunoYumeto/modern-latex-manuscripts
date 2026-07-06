# Interslavic weighted automaton analysis — v2

Generated 2026-07-05T23:10:05.682251Z.

## Scope

This is the full weighted evidence-automaton pass over the currently machine-readable Interslavic term ledger.

- Term rows analyzed: **1254**
- Automaton transition rows: **14258**
- Concept buckets: **97**
- Proof/register supplement rows: **532**

This is not a promotion list and does not edit corpus text. It is a weighted evidence graph for all terms.

## Automaton model

Each term row is represented by the same finite-state path:

```text
q0_START
  -> q1_SOURCE        canonical/source authority or implicit source
  -> q2_CONCEPT       concept link or route-key link
  -> q3_ISV_FORM      chosen Interslavic form
  -> q4_SUPPORT       E/W/S/I/X branch support terminals
  -> q4_ADVERSE       competitor / false-sense / trap terminal
  -> q4_GAP           missing-witness terminal
  -> q5_DECISION      recommended operational action
```

Weights use two separate semiring channels:

- **Support channel**: products along source→concept→form transitions; sums over support terminals.
- **Risk/adverse channel**: competitor-only, trap, F10 risk, and false-sense evidence are kept separate and never counted as negative support.
- **Gap channel**: missing evidence is not treated as adverse evidence.

## Branch summaries

- certified/current: E=2396.0, W=167.0, S=169.0, D1=1.581, KL=0.641
- candidate_after_review: E=2396.0, W=317.8, S=319.8, D1=1.935, KL=0.439

## F10/current flag counts

- F10-1: 961
- F10-0: 213
- F10-3: 42
- F10-2: 20
- F10-4: 18

## Recommended action counts

- MISSING_WITNESS_BACKFILL: 693
- WRITEBACK_CANDIDATE_AFTER_ROW_CHECK: 189
- REVIEW_OR_CONTEXT_CHECK: 132
- P1_REVIEW_ADVERSE_OR_COMPETITOR: 104
- ACCEPTABLE_LOW_PRIORITY: 80
- OVERCLAIM_BACKFILL_NEEDED: 20
- P0_TRAP_SENSE_AUDIT: 18
- AUTHORITY_OR_SPECIALIST_NEEDED: 18

## Top concept buckets by term count

- (unlinked): 642 rows, D1 1.499→1.499, action MISSING_WITNESS_BACKFILL:382; REVIEW_OR_CONTEXT_CHECK:125; ACCEPTABLE_LOW_PRIORITY:75; P1_REVIEW_ADVERSE_OR_COMPETITOR:28; OVERCLAIM_BACKFIL
- ideal: 70 rows, D1 2.158→2.798, action WRITEBACK_CANDIDATE_AFTER_ROW_CHECK:67; AUTHORITY_OR_SPECIALIST_NEEDED:1; ACCEPTABLE_LOW_PRIORITY:1; REVIEW_OR_CONTEXT_CHECK:1
- coefficient: 48 rows, D1 1.0→1.0, action MISSING_WITNESS_BACKFILL:48
- basis: 36 rows, D1 1.731→2.721, action WRITEBACK_CANDIDATE_AFTER_ROW_CHECK:36
- field: 36 rows, D1 1.686→2.743, action P1_REVIEW_ADVERSE_OR_COMPETITOR:36
- form: 24 rows, D1 1.0→1.0, action MISSING_WITNESS_BACKFILL:24
- folding: 21 rows, D1 1.0→1.0, action MISSING_WITNESS_BACKFILL:21
- element: 20 rows, D1 1.453→2.432, action WRITEBACK_CANDIDATE_AFTER_ROW_CHECK:13; REVIEW_OR_CONTEXT_CHECK:3; MISSING_WITNESS_BACKFILL:2; AUTHORITY_OR_SPECIALIST_NEEDED:1; P1_REVIEW_A
- covariant: 18 rows, D1 1.0→1.0, action P0_TRAP_SENSE_AUDIT:18
- module: 18 rows, D1 2.408→2.952, action WRITEBACK_CANDIDATE_AFTER_ROW_CHECK:18
- ring: 17 rows, D1 1.135→1.135, action P1_REVIEW_ADVERSE_OR_COMPETITOR:17
- determinant: 15 rows, D1 1.427→2.809, action WRITEBACK_CANDIDATE_AFTER_ROW_CHECK:14; REVIEW_OR_CONTEXT_CHECK:1
- irreducible: 12 rows, D1 1.0→1.0, action MISSING_WITNESS_BACKFILL:12
- polynomial: 12 rows, D1 2.031→2.778, action WRITEBACK_CANDIDATE_AFTER_ROW_CHECK:12
- dimension: 10 rows, D1 2.014→2.764, action WRITEBACK_CANDIDATE_AFTER_ROW_CHECK:9; AUTHORITY_OR_SPECIALIST_NEEDED:1
- group: 10 rows, D1 2.549→2.938, action WRITEBACK_CANDIDATE_AFTER_ROW_CHECK:10
- reduk: 10 rows, D1 1.761→1.761, action MISSING_WITNESS_BACKFILL:10
- corollary: 9 rows, D1 1.607→1.607, action P1_REVIEW_ADVERSE_OR_COMPETITOR:9
- modul: 9 rows, D1 2.217→2.217, action MISSING_WITNESS_BACKFILL:9
- teorem: 9 rows, D1 1.278→1.278, action MISSING_WITNESS_BACKFILL:9

## Files

- `INTERSLAVIC_WEIGHTED_AUTOMATON_TERM_LEDGER_v2_20260705.csv` — main per-term ledger.
- `INTERSLAVIC_WEIGHTED_AUTOMATON_EDGES_v2_20260705.csv` — actual weighted automaton transition table.
- `INTERSLAVIC_WEIGHTED_AUTOMATON_CONCEPT_SUMMARY_v2_20260705.csv` — concept-level aggregation.
- `INTERSLAVIC_WEIGHTED_AUTOMATON_BRANCH_SUMMARY_v2_20260705.csv` — current/candidate branch mass.
- `INTERSLAVIC_WEIGHTED_AUTOMATON_PROOF_REGISTER_v2_20260705.csv` — proof/register supplement.
- `INTERSLAVIC_WEIGHTED_AUTOMATON_ANALYSIS_v2_20260705.json` — full machine-readable object.

## Boundary

The weights are **use weights**, not truth weights. Native W/S evidence and candidate writebacks remain review-gated. Generated/internal consistency material can support discovery and consistency checking, not target-language witness certification.
