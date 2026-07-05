# OPEN_TRANSLATION_PROOF_LITERACY_SOURCE_COORDINATE_POLICY_SHEET_20260703T084500Z

Generated UTC: `2026-07-03T08:45:00Z`

Status: `proof_literacy_source_coordinate_policy_sheet_no_policy_returns_no_scans_no_source_text_no_excerpts_no_translation_no_pilot`

## Purpose

Classify package 153 proof-literacy metadata inventory summaries into source-coordinate policy rows for OLP and Book of Proof, distinguishing future scan candidates from support-only, permission-gated, asset/derived, and excluded routes without authorizing scans, copying source text, selecting excerpts, or starting translation.

## Counts

- Source-coordinate policy rows: `28`
- OLP extension policy rows: `14`
- OLP top-level policy rows: `9`
- Book of Proof route policy rows: `5`
- Coordinate-scan candidate-after-review rows: `3`
- Permission/license gate required rows: `5`
- Blank policy-review cells: `280`

## Policy Classes

| Row | Policy class | Rows | Candidate-after-review rows | Permission-gated rows |
| --- | --- | ---: | ---: | ---: |
| PL-SCP-CLASS-06 | repository_support_metadata_only | 7 | 0 | 0 |
| PL-SCP-CLASS-02 | build_or_configuration_support_only | 6 | 0 | 0 |
| PL-SCP-CLASS-03 | asset_or_derived_output_support_only | 4 | 0 | 0 |
| PL-SCP-CLASS-08 | permission_and_route_support_metadata_only | 3 | 0 | 3 |
| PL-SCP-CLASS-04 | support_metadata_only | 3 | 0 | 0 |
| PL-SCP-CLASS-07 | course_assembly_support_only | 1 | 0 | 0 |
| PL-SCP-CLASS-10 | excluded_failed_or_unavailable_route | 1 | 0 | 1 |
| PL-SCP-CLASS-09 | permission_gate_before_pdf_coordinate_scan | 1 | 1 | 1 |
| PL-SCP-CLASS-05 | primary_content_coordinate_candidate | 1 | 1 | 0 |
| PL-SCP-CLASS-01 | primary_text_source_coordinate_candidate | 1 | 1 | 0 |

## OLP Extension Policies

| Row | Extension | Policy class | Metadata file rows | Candidate after review |
| --- | --- | --- | ---: | --- |
| PL-SCP-OLP-EXT-001 | .tex | primary_text_source_coordinate_candidate | 729 | true |
| PL-SCP-OLP-EXT-002 | .sty | build_or_configuration_support_only | 17 | false |
| PL-SCP-OLP-EXT-003 | .pdf | asset_or_derived_output_support_only | 9 | false |
| PL-SCP-OLP-EXT-004 | .tikz | asset_or_derived_output_support_only | 9 | false |
| PL-SCP-OLP-EXT-005 | .eps | asset_or_derived_output_support_only | 7 | false |
| PL-SCP-OLP-EXT-006 | [none] | build_or_configuration_support_only | 7 | false |
| PL-SCP-OLP-EXT-007 | .md | support_metadata_only | 4 | false |
| PL-SCP-OLP-EXT-008 | .png | asset_or_derived_output_support_only | 2 | false |
| PL-SCP-OLP-EXT-009 | .bib | support_metadata_only | 1 | false |
| PL-SCP-OLP-EXT-010 | .bst | build_or_configuration_support_only | 1 | false |
| PL-SCP-OLP-EXT-011 | .cls | build_or_configuration_support_only | 1 | false |
| PL-SCP-OLP-EXT-012 | .html | build_or_configuration_support_only | 1 | false |
| PL-SCP-OLP-EXT-013 | .pcr | build_or_configuration_support_only | 1 | false |
| PL-SCP-OLP-EXT-014 | .yml | support_metadata_only | 1 | false |

## OLP Top-Level Policies

| Row | Top-level group | Policy class | Metadata file rows | Candidate after review |
| --- | --- | --- | ---: | --- |
| PL-SCP-OLP-TOP-001 | content | primary_content_coordinate_candidate | 723 | true |
| PL-SCP-OLP-TOP-002 | assets | repository_support_metadata_only | 27 | false |
| PL-SCP-OLP-TOP-003 | sty | repository_support_metadata_only | 12 | false |
| PL-SCP-OLP-TOP-004 | [root] | repository_support_metadata_only | 10 | false |
| PL-SCP-OLP-TOP-005 | courses | course_assembly_support_only | 8 | false |
| PL-SCP-OLP-TOP-006 | include | repository_support_metadata_only | 3 | false |
| PL-SCP-OLP-TOP-007 | misc | repository_support_metadata_only | 3 | false |
| PL-SCP-OLP-TOP-008 | .github | repository_support_metadata_only | 2 | false |
| PL-SCP-OLP-TOP-009 | bib | repository_support_metadata_only | 2 | false |

## Book of Proof Route Policies

| Row | Source class | Route status | Policy class | Permission gate |
| --- | --- | --- | --- | --- |
| PL-SCP-BOP-ROUTE-001 | official_landing_page | cached | permission_and_route_support_metadata_only | true |
| PL-SCP-BOP-ROUTE-002 | official_pdf | cached | permission_gate_before_pdf_coordinate_scan | true |
| PL-SCP-BOP-ROUTE-003 | license_deed | cached | permission_and_route_support_metadata_only | true |
| PL-SCP-BOP-ROUTE-004 | legacy_or_adjacent_route | error | excluded_failed_or_unavailable_route | true |
| PL-SCP-BOP-ROUTE-005 | external_approval_route | cached | permission_and_route_support_metadata_only | true |

## Zero Gates

- Policy reviews completed: `0`
- Coordinate scans / source-text capture / excerpt selections authorized: `0 / 0 / 0`
- Source text/excerpt files: `0`
- Source text/definitions/examples copied: `0 / 0 / 0`
- Source passages selected: `0`
- Exact spans / candidate line ranges: `0 / 0`
- Translated passages: `0`
- Proposed bridge lexemes / morphemes / syntax / displays: `0 / 0 / 0 / 0`
- Accepted bridge surfaces / local-language terms: `0 / 0`
- Reviewer returns / license rechecks completed: `0 / 0`
- Readiness: `publication=false, translation=false, constructed_surface=false, pilot=false`

Boundary: policy classes only. This artifact authorizes no coordinate scan, source-text capture, excerpt selection, translation, constructed form, or readiness claim.
