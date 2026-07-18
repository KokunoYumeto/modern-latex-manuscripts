# Structural index schema

`STRUCTURAL_INDEX.jsonl` is the hierarchical authority for this bounded unit. Each JSON object has a stable `unit_id`, `unit_type`, exact R823 line span, printed-page span, parent ID, ordered child IDs, outbound cross-references, target locator, and review state. `source_mapping_uncertainty` is mandatory and may be `none` only after scan inspection.

The index is append-only. An initial object has implicit `record_revision` 1 unless that field is present. A correction repeats the same stable `unit_id`, gives the next integer `record_revision`, and names the prior record as `unit_id@revision` in `supersedes`. Consumers resolve each stable ID to its highest revision before validating parent/child references. Duplicate stable IDs without this exact revision chain are invalid.
