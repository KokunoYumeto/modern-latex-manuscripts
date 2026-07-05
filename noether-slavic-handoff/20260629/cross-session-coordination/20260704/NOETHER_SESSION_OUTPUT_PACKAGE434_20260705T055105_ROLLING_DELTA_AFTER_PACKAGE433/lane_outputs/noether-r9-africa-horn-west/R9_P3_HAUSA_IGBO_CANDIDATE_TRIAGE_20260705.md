# R9 P3 Hausa/Igbo Candidate Metadata Triage

Generated: 2026-07-05T03:50:11.287033+00:00 UTC

## Boundary

This triages only nonzero metadata rows from `R9_P3_HAUSA_IGBO_SOURCE_BODY_CANDIDATE_PROBE_20260705.csv`. It does not download source bodies, repositories, datasets, PDFs, or source text; it does not translate, approve terms, clear licenses, claim review, promote gates, package, stage, commit, or push.

## Triage Rows

| row | platform | query | decision | next action |
|---|---|---|---|---|
| Hausa | GitHub repository search API | hausa mathematics textbook | blocked_broad_repository_noise_not_source_body | Refine query toward exact Hausa math source titles, education publishers, official curricula, or known repository names; keep current row as noise. |
| Hausa | Internet Archive advancedsearch API | lissafi hausa | deferred_public_wiki_register_pdf_not_textbook_source_corpus | If useful for source discovery, capture IA item metadata/files list and exact license/attribution chain; do not treat as textbook/source-canon evidence without source-body hash and reviewer/source-owner gate. |
| Hausa | GitHub repository search API | lissafi hausa | deferred_github_repository_candidate_needs_repo_body_license_language_review | Run a repository metadata/file-list probe for FazamMV23/HausaMath before any body capture; require license file, commit hash, target-language math content, and source-owner/reviewer gate. |
| Igbo | Internet Archive advancedsearch API | igbo mathematics textbook | blocked_false_positive_not_igbo_math_source | Refine to exact Igbo terms/titles or source-owner routes; keep IA row as false positive. |
| Igbo | GitHub repository search API | igbo mathematics textbook | blocked_broad_repository_noise_not_igbo_math_source | Search exact Igbo classroom/source-owner routes or named educational publications; no source-body use from this metadata. |

All triage rows remain `source_gate_decision=not_admitted_source_gate_blocked` and `promotion_allowed=false`.

CSV: `C:\Users\memo_\Documents\Codex\2026-07-04\noether-r9-africa-horn-west\outputs\R9_P3_HAUSA_IGBO_CANDIDATE_TRIAGE_20260705.csv`
