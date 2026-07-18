# Typed evidence graph

`EVIDENCE_NODES.csv` and `EVIDENCE_EDGES.csv` are the active provenance/routing graph. Nodes are typed as source witnesses, concepts, language-specific candidate forms, or operational decisions. Edges state their relation and one of the separated evidence channels. An edge that supports “witness found” does not support accepted terminology.

The graph intentionally has no scalar readiness field, branch weight, or automatic decision rule. Dependence and breadth live separately in `FAMILY_COHORT_TREE.csv`, which is provisional, unweighted, and has no declared edge lengths. The graph and tree must not be collapsed into one score.

The initial graph covers the recovered polynomial-ring and Noetherian-ring rows whose inherited source status changed. File-level recovery provenance remains in `RECOVERY_COPY_LEDGER.csv`; exact duplicates and deliberate exclusions remain in their own ledgers.
