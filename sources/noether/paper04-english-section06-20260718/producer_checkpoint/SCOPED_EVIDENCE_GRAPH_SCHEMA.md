# Scoped evidence graph schema

Each nonblank line of `SCOPED_EVIDENCE_GRAPH.jsonl` is a UTF-8 JSON object with stable `record_id`, positive `revision`, `status`, `kind`, `parent_id`, `children`, `references`, `referenced_by`, `artifact`, `finding`, and `disposition`. Parent-child links and reference/referenced-by links must be reciprocal. Artifact receipts require exact relative paths, bytes, and SHA-256 values. The root has no parent.
