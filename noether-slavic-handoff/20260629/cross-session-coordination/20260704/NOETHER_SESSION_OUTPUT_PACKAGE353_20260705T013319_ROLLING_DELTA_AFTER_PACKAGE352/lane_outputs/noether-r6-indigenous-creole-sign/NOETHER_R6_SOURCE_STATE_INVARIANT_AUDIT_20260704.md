# NOETHER R6 Source-State Invariant Audit

Status: source_state_invariant_audit_no_promotion_no_completion_claim

Generated: 2026-07-04

Lane: Session I / R6 Indigenous, Creole, and Sign Access

Purpose: make the current R6 source-canon guardrails testable across the core witness, gap, transition, candidate, guardrail, non-strict route, crosswalk, B3, gate, and reader-manifest artifacts. This audit verifies the shape of source-canon support metadata. It does not promote sources, close gaps, claim review/approval/clearance, authorize terms/signs/translations, create visual inventories or pilots, mark completion, or push Git.

## Output

| Artifact | Rows | Result |
|---|---:|---|
| `NOETHER_R6_SOURCE_STATE_INVARIANT_AUDIT_20260704.csv` | 14 | 14 pass, 0 fail. |

## Invariant Coverage

| Invariant | Scope | Result |
|---|---|---|
| `R6-INV-001` | Strict provenance row count | Pass |
| `R6-INV-002` | Strict provenance required fields | Pass |
| `R6-INV-003` | Strict local path/hash replay | Pass |
| `R6-INV-004` | Strict URL reachability/access status | Pass |
| `R6-INV-005` | Strict license/access package policy fields | Pass |
| `R6-INV-006` | Explicit gap required blocker fields | Pass |
| `R6-INV-007` | Gap transition requirements remain non-movable/non-promotional | Pass |
| `R6-INV-008` | Candidate route has metadata hash and blank source-body fields | Pass |
| `R6-INV-009` | International Sign guardrails remain non-source rows | Pass |
| `R6-INV-010` | Non-strict DGS route remains non-strict while metadata hash replays | Pass |
| `R6-INV-011` | Target coverage crosswalk rows have states and boundaries | Pass |
| `R6-INV-012` | B3 package-boundary rows replay hashes and stay metadata-only | Pass |
| `R6-INV-013` | Machine-readable gate counts remain zero | Pass |
| `R6-INV-014` | Reader/package manifest gate text avoids promotion language | Pass |

## Key Counts

| Check | Count |
|---|---:|
| Strict provenance rows | 82 |
| Explicit gap rows | 78 |
| Gap transition rows allowed to move now | 0 |
| Gap transition rows allowed to promote now | 0 |
| Candidate source-body path/hash violations | 0 |
| Guardrail source-witness violations | 0 |
| Crosswalk incomplete rows | 0 |
| B3 package-boundary violations or hash mismatches | 0 |
| Nonzero gate-count fields | 0 |
| Promoted reader-manifest gate texts | 0 |

## Boundary

This audit is evidence hygiene only. A pass means the current source-canon support metadata is internally consistent with R6 guardrails. It does not mean any language/access target is approved, complete, licensed for reuse, ready for translation, ready for term/sign movement, ready for visual inventory, ready for pilot work, or pushed to Git.
