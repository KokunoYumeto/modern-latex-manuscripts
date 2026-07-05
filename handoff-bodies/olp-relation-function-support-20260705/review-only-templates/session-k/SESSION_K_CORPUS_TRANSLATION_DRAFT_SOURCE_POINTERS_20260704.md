# Session K Corpus Translation Draft Source Pointers

Generated date: 2026-07-04

Status: `draft_source_pointers_tied_to_parent_shelf_no_source_text_no_mapping_no_translation_no_approval`

## Purpose

Convert the route-verified open relation/function candidate shelf into direct draft source pointers that corpus translation lanes can consume. These rows are not source excerpts and not source-text captures. They tell a lane which source family to route through, which sidecar must exist next, and which owner lane must handle language-specific work.

Parent artifact: `OPEN_RELATION_FUNCTION_TRANSLATION_SOURCE_CANDIDATE_SHELF_20260702T131500Z`

## Draft Source Pointer Rows

| Pointer | Parent row | Source family | Priority | Packet family | Required next sidecar |
| --- | --- | --- | ---: | --- | --- |
| `K-DSP-001` | `ORF-SRC-01` | Open Logic Project / Open Logic Text | 1 | proof_and_set_function_primer | exact-file attribution sidecar plus no-prose source-pointer table |
| `K-DSP-002` | `ORF-SRC-02` | Discrete Mathematics: An Open Introduction | 1 | proof_and_set_function_primer | license reconciliation and reviewer-scope return sidecar |
| `K-DSP-003` | `ORF-SRC-03` | OpenStax Precalculus 2e | 2 | function_language_school_to_undergraduate_bridge | book-specific edition/license capture sidecar |
| `K-DSP-004` | `ORF-SRC-04` | OpenStax Algebra and Trigonometry 2e | 2 | function_language_school_to_undergraduate_bridge | book-specific edition/license capture sidecar |
| `K-DSP-005` | `ORF-SRC-05` | A First Course in Linear Algebra | 2 | linear_map_and_abstract_algebra_extension | GFDL-only packet plan or FCLA compatibility table |
| `K-DSP-006` | `ORF-SRC-06` | Abstract Algebra: Theory and Applications | 3 | linear_map_and_abstract_algebra_extension | GFDL-only packet plan or AATA compatibility table |
| `K-DSP-007` | `ORF-SRC-07` | OpenIntro Statistics resources | 3 | public_numeracy_to_function_bridge | share-alike attribution plan and local numeracy reviewer packet |
| `K-DSP-008` | `ORF-SRC-08` | Stacks Project | 4 | advanced_noether_reference | advanced-reference sidecar and exact chapter/license capture |

## Consumption Rules

- Use these rows as draft source pointers only.
- Do not copy source prose, examples, passages, tables, figures, datasets, or URLs into language packets from this artifact.
- Route any local terminology or translation choice to the language owner.
- Route ownerless construction-method disputes to Session D.
- Session B may package this as an ordinary support sidecar because it contains no source text and no large files.

## Zero Gates

| Gate | Count |
| --- | ---: |
| source_text_or_excerpt_files | 0 |
| exact_editions_captured_here | 0 |
| source_files_cached_here | 0 |
| mapping_decisions | 0 |
| translations_created | 0 |
| approvals_recorded | 0 |
| readiness_claims | 0 |

Boundary: draft source-pointer support only. No language content is accepted here.
