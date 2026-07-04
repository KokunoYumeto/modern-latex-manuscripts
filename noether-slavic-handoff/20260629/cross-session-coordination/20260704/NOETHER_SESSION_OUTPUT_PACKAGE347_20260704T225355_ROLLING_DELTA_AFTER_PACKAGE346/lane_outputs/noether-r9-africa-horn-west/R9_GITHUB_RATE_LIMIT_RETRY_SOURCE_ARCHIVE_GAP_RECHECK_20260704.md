# R9 GitHub Rate-Limit Retry Source-Archive Gap Recheck - 2026-07-04

This continuation rechecked the three GitHub repository-search rows that were blocked by `HTTP 403 rate limit exceeded` in the round-2 multi-archive metadata probe.

The retry first captured `https://api.github.com/rate_limit` metadata under `work/source_canon_witnesses/20260704_r9_github_rate_limit_retry/`. The GitHub search resource reported `remaining=10` before the retry, so the three searches were rerun as live metadata checks rather than carried forward as rate-limit blockers.

## Retry Results

| row | target | query | HTTP status | result count | source-gate decision |
|---|---|---|---:|---:|---|
| `R9-GH-RETRY-001` | Akan/Twi | `twi mathematics dataset` | 200 | 0 | explicit zero-result metadata gap |
| `R9-GH-RETRY-002` | Fulfulde/Fulani | `fulfulde mathematics fulani` | 200 | 0 | explicit zero-result metadata gap |
| `R9-GH-RETRY-003` | Mandinka/Manding | `mandinka mathematics manding` | 200 | 0 | explicit zero-result metadata gap |

Each retry row has a saved metadata JSON file, a saved header JSON file, SHA-256 hashes, the original prior probe id, URL, target-language/topic tags, and `promotion_allowed=false` in the companion CSV.

## Source-Canon Result

The earlier GitHub rate-limit blocker is closed for these exact query strings. It is replaced by exact zero-result metadata gaps for Akan/Twi, Fulfulde/Fulani, and Mandinka/Manding source-archive searches.

No repository archive, code body, dataset body, source package, PDF, or raw source file was downloaded. These rows do not prove absence of all possible GitHub evidence; they only preserve exact negative results for the queried strings.

## Next Work

Future acquisition should try narrower repository-owner, orthographic, language-endonym, school-source, and glossary-source query forms, and should still require URL, hashable source body, topic/language tag, license/access signal, and source-gate review before any source-canon use.

Boundary: no translation, accepted term, native/community review, canonical approval, license clearance, gate promotion, completion claim, package upload, or Git push is made.
