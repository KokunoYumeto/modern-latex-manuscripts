# R9 Endonym GitHub Retry Candidate Triage

Generated: 2026-07-04T21:30:04.541988+00:00 UTC

## Boundary

This artifact triages only the nonzero metadata rows from `R9_ENDONYM_GITHUB_QUOTA_RETRY_SKIPPED_ROWS_20260704.csv`. It is not a source-corpus admission, translation artifact, license clearance, native/community review, canonical approval, gate promotion, package action, or Git action.

## Triage

| row | count | decision | blocker | next action |
|---|---:|---|---|---|
| AF05 South Sudan access target | 74 | blocked_broad_query_noise_not_target_language_math_source | Top GitHub metadata is broad/general software or unrelated repositories; no named Dinka/Nuer/Zande or other South Sudan target-language mathematical source body is evidenced. MIT on one unrelated repository is only a metadata signal for that repository, not R9 source-canon clearance. | Retry with named language/community rows and known education/source-owner domains; require hashable target-language math source body, stable URL, source-owner/authority route, and license/access signal before any source-canon use. |
| AF06 Omotic/Southern Non-Bantu access target | 1 | blocked_dictionary_context_only_not_math_source_corpus | The single GitHub metadata hit is dictionaria/sidaama, a language/dictionary-style repository with CC-BY-4.0 metadata. It is not a mathematical publication/source package, does not close the Omotic/Southern Non-Bantu math-source body gate, and cannot be treated as license clearance for R9 math corpus use. | Use only as possible language-resource context after scope review; continue exact Omotic/southern non-Bantu source-owner or school-math corpus acquisition with topic, language/variety, source-body hash, and access/license evidence. |

All triage rows remain `promotion_allowed=false` and `source_gate_decision=not_admitted_source_gate_blocked`.
