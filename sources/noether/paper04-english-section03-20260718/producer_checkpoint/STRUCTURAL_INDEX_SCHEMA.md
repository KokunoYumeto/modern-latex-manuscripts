# Structural index schema

`STRUCTURAL_INDEX.jsonl` is the hierarchical authority for this bounded unit. Each JSON object has a stable `unit_id`, a `unit_type`, an exact R823 line span, a printed-page span, a parent ID, ordered child IDs, outbound cross-references, a target locator, a mandatory source-mapping uncertainty statement, and a review state.

The index is append-only. An initial object explicitly has `record_revision` 1 and `supersedes: null`. A correction repeats the same stable `unit_id`, gives the next integer `record_revision`, names the prior record as `unit_id@revision` in `supersedes`, and explains the correction. Consumers resolve each stable ID to its highest revision before validating parent/child references. Duplicate stable IDs without this exact revision chain are invalid.
