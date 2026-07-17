# Interlanguage Research Department and Automata Audit

Release date: 2026-07-17

This package preserves the current interlanguage research and management layer
used by the mathematical-translation programme. It contains the complete
21-file research department, both exact weighted-data archives on which its
audit operates, and extracted copies of those archives for direct inspection.

## Start here

1. `research_department/README.md`
2. `research_department/RESEARCH_AUTHORITY_AND_PROVENANCE.md`
3. `research_department/INTERLINGUISTIC_METHOD_SYNTHESIS.md`
4. `research_department/MATHEMATICAL_OBJECTS_AND_AUDIT.md`
5. `research_department/CLAIM_STATUS_REGISTER.json`
6. `research_department/audit_outputs/AUDIT_RESULTS.json`
7. The relevant file under `research_department/LANE_HANDOFFS/`

## Exact data packages

- `automata_archives/INTERSLAVIC_WEIGHTED_AUTOMATON_STATE_C_PLUS_W0_v3_20260705.zip`
  is the current serialized Interslavic State C evidence snapshot plus the
  unapplied W0 projection.
- `automata_archives/UNIFIED_MARKER_AUTOMATON_v6_2_20260706.zip` is a
  cross-lane routing and source-discovery graph. Its numeric readiness field is
  reproduced by the audit but rejected as a readiness or quality measure.
- `automata_extracted/` contains byte-identical extracted members for easier
  reading and reuse.

## Status boundary

The arithmetic and output-manifest checks in this release are reproducible.
The package does not certify term correctness, mutual intelligibility,
community acceptance, or any translation. State C is a reconciled serialized
dataset snapshot; W0 is a projection only. The objects retain their historical
`automaton` names for provenance, while the current methodology classifies
them operationally as typed evidence/routing graphs unless a future process
defines genuine automaton input, transition, semiring, and path semantics.

No current lane has accepted external/community review or a completed human
comprehension experiment. Generated translations never count as native-source
witnesses.

