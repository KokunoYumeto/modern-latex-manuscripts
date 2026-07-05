# Malay-Indonesian Function/Domain Return Ledger Template V2

Artifact: `MALAY_INDONESIAN_OPERATOR_SLOT_FUNCTION_DOMAIN_RETURN_LEDGER_TEMPLATE_V2_20260701T091500Z`
Generated UTC: 2026-07-01T09:15:00Z

## Purpose

This is a blank V2 return ledger template for function/mapping and unique-output/domain reviewer prompts. It follows `MALAY_INDONESIAN_OPERATOR_SLOT_FUNCTION_DOMAIN_REVIEWER_PROMPTS_V2_20260701T090000Z` and gives future reviewers a structured place to answer authority, source-route, coordinate, scope, and surface-separation questions.

It does not ingest returns, update the parent ledger, copy source prose, copy definitions, select source passages, fill surface fields, accept surfaces, start translation, or claim pilot readiness.

## Ledger Rows

| Return row | Prompt row | Parent ledger rows | Expected reviewer role | Expected authority class | Status | Surface default |
| --- | --- | --- | --- | --- | --- | --- |
| `MI-FD-RET-V2-01` | `MI-FD-V2-01` | `MI-OSR-RET-08`<br>`MI-OSR-RET-09` | Domain mathematics reviewer plus source authority reviewer | official_primary_browser_verified; local_mirror_cache_proxy | pending_no_return | yes_blank_by_default |
| `MI-FD-RET-V2-02` | `MI-FD-V2-02` | `MI-OSR-RET-08` | Domain mathematics reviewer | local_mirror_cache_proxy | pending_no_return | yes_blank_by_default |
| `MI-FD-RET-V2-03` | `MI-FD-V2-03` | `MI-OSR-RET-09` | Domain mathematics reviewer | local_mirror_cache_proxy | pending_no_return | yes_blank_by_default |
| `MI-FD-RET-V2-04` | `MI-FD-V2-04` | `MI-OSR-RET-08`<br>`MI-OSR-RET-09` | Domain mathematics reviewer | supplementary_exact_cache | pending_no_return | yes_blank_by_default |
| `MI-FD-RET-V2-05` | `MI-FD-V2-05` | `MI-OSR-RET-08`<br>`MI-OSR-RET-09` | Domain mathematics reviewer | failed_route_record | pending_no_return | yes_blank_by_default |
| `MI-FD-RET-V2-06` | `MI-FD-V2-06` | `MI-OSR-RET-08`<br>`MI-OSR-RET-09`<br>`MI-OSR-RET-13` | License/attribution reviewer | local_mirror_cache_proxy; supplementary_exact_cache | pending_no_return | yes_blank_by_default |
| `MI-FD-RET-V2-07` | `MI-FD-V2-07` | `MI-OSR-RET-11`<br>`MI-OSR-RET-12` | Brunei Malay context/source reviewer and Singapore Malay context/source reviewer | local_mirror_cache_proxy; supplementary_exact_cache | pending_no_return | yes_blank_by_default |
| `MI-FD-RET-V2-08` | `MI-FD-V2-08` | `MI-OSR-RET-08`<br>`MI-OSR-RET-09` | Domain mathematics reviewer | local_mirror_cache_proxy; supplementary_exact_cache | pending_no_return | yes_blank_by_default |
| `MI-FD-RET-V2-09` | `MI-FD-V2-09` | `MI-OSR-RET-08`<br>`MI-OSR-RET-09` | Any role returning function/domain evidence | mixed_all_function_domain_replacement_rows | pending_no_return | yes_blank_by_default |

## Column Template

- `fd_return_row_id`
- `prompt_row_id`
- `parent_ledger_rows`
- `primary_parent_ledger_row`
- `parent_sheet_row_id`
- `scope`
- `reviewer_role_expected`
- `source_route_rows_prompted`
- `authority_class_expected`
- `source_evidence_class_expected`
- `coordinate_refs_prompted`
- `required_return_fields`
- `forbidden_return_content`
- `return_status`
- `reviewer_identity_or_role`
- `return_date`
- `authority_class_used`
- `source_route_rows_used`
- `term_coordinate_rows_used`
- `route_rows_rejected_or_downgraded`
- `function_mapping_scope_decision`
- `unique_output_domain_scope_decision`
- `source_class`
- `scope_limit`
- `license_or_attribution_note`
- `proposed_surface`
- `accepted_surface`
- `rejected_surface`
- `surface_fields_blank_unless_separately_justified`
- `next_required_artifact`
- `promotion_effect`

## Promotion Rules

| Rule | Text |
| --- | --- |
| `MI-FD-RET-RULE-01` | A row may move from pending_no_return only when reviewer_identity_or_role and return_date are filled from a real dated return. |
| `MI-FD-RET-RULE-02` | Authority class must be separated from source evidence class; mirror cache proxy cannot be silently upgraded to official primary. |
| `MI-FD-RET-RULE-03` | Function/mapping and unique-output/domain scope decisions must remain separate unless the reviewer explicitly links them. |
| `MI-FD-RET-RULE-04` | Surface fields remain blank by default; any proposed or accepted surface requires a separate explicit reviewer decision and provenance. |
| `MI-FD-RET-RULE-05` | No source prose or definitions may be pasted into this ledger; source passage needs a separate sidecar. |
| `MI-FD-RET-RULE-06` | Brunei/Singapore rows remain no-inheritance checks; Indonesian comparator evidence does not create local adoption. |

## Gate State

| Gate | State |
| --- | ---: |
| Ledger rows | 9 |
| Target parent ledger rows | 2 |
| Support parent ledger rows | 3 |
| Column template fields | 31 |
| Promotion rule rows | 6 |
| Reviewer returns ingested | 0 |
| Parent ledger rows updated | 0 |
| Source prose copied | 0 |
| Source definitions copied | 0 |
| Source passages selected | 0 |
| Proposed surfaces filled | 0 |
| Accepted Indonesian surfaces | 0 |
| Accepted Malaysian Malay surfaces | 0 |
| Accepted Brunei/Singapore surfaces | 0 |
| Accepted bridge/constructed surfaces | 0 |
| OLP excerpts selected | 0 |
| Translated passages | 0 |
| Translation ready | false |
| Publication ready | false |
| Constructed surface ready | false |
| Pilot ready | false |

Decision: Use as the blank V2 return ledger for function/domain reviewer prompts. It creates no return, surface, translation, or pilot state.
