# Noether R6 Source-Canon Field Completeness Audit

Generated: 2026-07-04

Lane: Session I / R6 Indigenous, Creole, and Sign Access

Status: source-canon/provenance quality audit only. It records no translation, term/sign approval, source-authority promotion, native review, canonical approval, license-clearance record, media-reuse permission, gate promotion, lane completion, Git staging, commit, or push.

## Reason For This Audit

The whole-program source-canon instructions require source witnesses with exact URLs, hashes, local paths, license/access signals, language/topic tags, and explicit gaps. A continuation audit found that the broad R6 source-canon table contained 10 International Sign comparator policy/question rows without source URL, local path, or hash, plus one DGS route metadata row with a placeholder URL. Those rows are useful guardrails or route metadata, but they are not strict exact-URL source witnesses.

## Resulting Split

| Artifact | Rows | Field status | Use |
|---|---:|---|---|
| `NOETHER_R6_SOURCE_CANON_WITNESS_TABLE_20260704.csv` | 93 | Broad source-plus-guardrail table from prior pass. | Historical/detail table; do not treat every row as a strict source witness. |
| `NOETHER_R6_SOURCE_CANON_STRICT_PROVENANCE_WITNESS_TABLE_20260704.csv` | 82 | Every row has exact source URL, local path, SHA-256 hash, license/access signal, and tags. | Preferred strict source-canon witness table for B3/package metadata and future source maintenance. |
| `NOETHER_R6_SOURCE_CANON_REQUIRED_FIELD_MIRROR_20260704.csv` | 82 | Normalized to the current source-canon steering field shape, with zero missing required provenance fields. | Preferred normalized mirror. |
| `NOETHER_R6_NON_SOURCE_GUARDRAIL_ROWS_20260704.csv` | 10 | Explicitly marked as non-source International Sign comparator guardrail rows. | Policy/question guardrails only; not source-canon witnesses. |
| `NOETHER_R6_NON_STRICT_ROUTE_METADATA_ROWS_20260704.csv` | 1 | DGS route metadata with local hash but placeholder live URL. | Route metadata only until exact URL is resolved. |
| `NOETHER_R6_SOURCE_CANON_EXPLICIT_GAP_LEDGER_20260704.csv` | 78 | Explicit gap rows, including three GitHub/source-repository gap rows and six URL/access gap rows. | Missing source/source-archive/reviewer/authority/live-access gates. |

## Strict Mirror Counts

| Check | Count |
|---|---:|
| Strict source-canon provenance rows | 82 |
| Rows with missing URL/local path/hash/license/tags in normalized mirror | 0 |
| Source-level TeX/LaTeX/arXiv/e-print/GitHub/source-archive rows | 0 |
| PDF/HTML/text-style fallback or source-route rows | 50 |
| Video/dynamic signed-language route rows | 32 |
| Target/source access route rows that still lack authority | 68 |
| Candidate/context rows that still lack exact math authority | 11 |
| Comparator-only strict source rows | 4 |
| Non-source comparator guardrail rows split out | 10 |
| Non-strict placeholder-URL route metadata rows split out | 1 |

## Added GitHub / Source-Repository Gaps

The gap ledger now explicitly records that recovered R6 evidence contains no validated target-language mathematical GitHub repository, CTAN-style package, open source-code/source-file archive, or signed-language source repository usable as sign authority:

| Gap row | Family | Missing source type |
|---|---|---|
| `R6-GITHUB-GAP-001` | Indigenous Americas | Target-language mathematical GitHub repository, CTAN-style package, or open source-code/source-file archive. |
| `R6-GITHUB-GAP-002` | Creole/contact | Named-language mathematical GitHub repository, CTAN-style package, or open source-code/source-file archive. |
| `R6-GITHUB-GAP-003` | Signed language | Signed-language mathematical GitHub/source repository usable as sign-language authority. |

These gap rows do not authorize source inference, terms, signs, translation, media reuse, or pilot work. They only make the missing GitHub/source-repository evidence findable for future source acquisition.

## Added URL / Access Gaps

The gap ledger also records six URL/access gaps:

| Gap rows | Scope |
|---|---|
| `R6-URL-GAP-001` through `R6-URL-GAP-003` | Aymara, Quechua Central, and Quechua Chanka Minedu DSpace handles returned `403 Forbidden` to headers-only audit; local PDF/hash provenance remains intact. |
| `R6-URL-GAP-004` and `R6-URL-GAP-005` | DGS Sign2MINT API/CDN routes returned `403 Forbidden` to headers-only audit; media/reuse/sign-authority gates remain closed. |
| `R6-URL-GAP-006` | DGS route row had a placeholder URL and was split into non-strict route metadata. |

## Maintenance Rule

Future R6 source-canon updates should add rows to the strict provenance table only when an exact non-placeholder source URL, local path or manifest path, hash, license/access signal, language/topic tags, and ethics/authority note are available. Guardrail-only rows belong in the non-source guardrail table. Placeholder-url route rows belong in the non-strict route metadata table or gap ledger until repaired.
