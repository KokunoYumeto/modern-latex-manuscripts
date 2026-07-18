# Machine-readable evidence schema

All CSV and JSONL files in this bounded candidate are UTF-8 public evidence. CSV header order is fixed as follows:

- `SOURCE_ALIGNMENT.csv`: `alignment_id,unit_id,r823_lines,printed_pages,physical_scan_pages,target_locator,source_status,adverse_delta`;
- `SOURCE_CONTROL_HASHES.csv`: `control_id,role,locator,sha256,bytes,authority_status,redistributed,notes`;
- `FORMULA_AND_SYMBOL_LEDGER.csv`: `comparison_id,object_type,source_locator,printed_page,target_locator,critical_controls,result,adverse_or_choice`;
- `TERMINOLOGY_AND_ADVERSE_LEDGER.csv`: `decision_id,german_term_or_delta,chosen_english,alternative_rejected,evidence_class,motivation,uncertainty,status`;
- `ZENODO_PAYLOAD_MANIFEST.csv`: `path,bytes,sha256,role`;
- `SHA256SUMS.csv`: `path,bytes,sha256`.

The first column is the unique primary ID in the four evidence ledgers. `path` is the unique primary ID in both inventories and must be a safe package-relative path. CSV cells beginning, after optional whitespace, with `=`, `+`, `-`, or `@` are invalid.

Each `STRUCTURAL_INDEX.jsonl` object requires `unit_id`, `record_revision`, `unit_type`, `r823_lines`, `printed_pages`, `parent_id`, ordered `child_ids`, `cross_references`, `target_locator`, `source_mapping_uncertainty`, `review_state`, and `supersedes`. Initial records use revision 1 and null supersession. A correction repeats the stable ID, increments the revision by one, and points `supersedes` to `unit_id@prior_revision`.

Each `DIFFICULTY_AND_FAILURE_LEDGER.jsonl` object requires `issue_id`, `record_revision`, `supersedes`, `recorded_at`, `time_precision`, `unit_id`, `locator`, `symptom`, `error_class`, `severity`, `attempts`, `rejected_approaches`, `resolution`, `residual_risk`, `recurrence_cues`, `lesson`, and `state`. Initial records use revision 1 and null supersession. Corrections follow the same consecutive revision rule. Optional `closes_issues` references must point backward; optional `artifact_sha256` keys bind a closure event to frozen artifacts.

JSON objects may not contain duplicate keys. Every package-local structural, difficulty, and alignment reference must resolve after highest-revision selection. Outbound references are permitted only when they identify a unit outside the bounded section and are not represented as local children.
