# Source-audit evidence map

This directory preserves tranche-time audit reports and machine ledgers used to
produce the frozen SGA 5 English cumulative. Reports are intentionally retained
as historical snapshots: a statement such as “not yet current” or “not yet
applied” describes the pre-repair file inspected by that tranche, not the final
workpass.

Final disposition is controlled by the package-root files
`SOURCE_CORRECTION_FINAL_RESOLUTION.csv`,
`SOURCE_CRITICAL_ADDITIONAL_REPAIRS.csv`,
`STRUCTURAL_PARITY_REPRESENTATION_REVIEW.csv`,
`TERMINOLOGY_REJECTED_CHOICES.csv`, `CONTINUATION_CURSOR.md`, and
`INDEPENDENT_REVIEW.md`. Those controls connect every retained snapshot to its
applied/rejected outcome and the frozen TeX/PDF hashes.

The original LNM 589 scan is not copied here and is excluded from the proposed
publication payload. Its pinned SHA-256 and audit-only role are recorded in
`../STATUS.md` and `../LICENSE_ATTRIBUTION.md`.
