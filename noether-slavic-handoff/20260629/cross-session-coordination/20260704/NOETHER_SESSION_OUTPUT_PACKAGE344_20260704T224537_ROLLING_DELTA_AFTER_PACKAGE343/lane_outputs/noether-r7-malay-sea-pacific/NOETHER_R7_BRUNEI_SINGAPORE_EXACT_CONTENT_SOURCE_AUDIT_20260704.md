# Noether R7 Brunei/Singapore Exact-Content Source Audit

Date: 2026-07-04

Scope: source-canon/provenance only. This audit covers the Brunei/Singapore rows in the R7 source-canon witness table and adds current manifest-only official route leads surfaced from live Brunei MOE and Singapore MOE/SEAB pages. It does not translate, approve terms, claim native review, claim canonical approval, clear licenses, promote gates, claim completion, or push Git.

Primary row table:

- `NOETHER_R7_BRUNEI_SINGAPORE_EXACT_CONTENT_SOURCE_AUDIT_ROWS_20260704.csv`

## Method

- Re-read `NOETHER_R7_SOURCE_CANON_MATH_CORPUS_WITNESS_ROWS_20260704.csv`.
- Rechecked `NOETHER_R7_EXACT_SOURCE_ACQUISITION_AND_ROUTE_QUEUE_20260704.md`.
- Audited all 12 existing Brunei/Singapore rows.
- Verified local paths, SHA-256 hashes, and byte counts for all locally captured rows.
- Re-ran current HEAD probes for every URL row.
- Searched live official route pages for Brunei/Singapore item-level mathematics source-return leads.
- Added five new official route candidates as manifest-only rows; no raw source body or new PDF payload was downloaded.

## Summary

- Audit rows: 17.
- Existing source-canon rows audited: 12.
- New manifest-only official route candidates: 5.
- Current URL rows returning HTTP 200: 15.
- Direct URL rows still blocked: 1, the Brunei DBP/MABBIM route, with SSL failure from direct tooling.
- Local path/hash/byte-count anchor problems: 0.
- Exact Brunei/Singapore Malay higher-algebra/math terminology rows found: 0.
- Translation-support rows promoted: 0.

## Existing Brunei Rows

- `R7BSSRC001`, `BS-BRUNEI-CTX-01`: Brunei language/translation context PDF, current 200, local hash verified. It is not mathematics or algebra terminology authority.
- `R7BSSRC002`, `BS-BRUNEI-CTX-02`: Brunei UBD EMI/code-switching context PDF, current 200, local hash verified. It is math-access context only, not algebra terminology authority.
- `R7BSSRC003`, `BS-BRUNEI-DBP-GAP-01`: Brunei DBP/MABBIM official route, direct tooling still fails with SSL connection error. Web search still finds the MABBIM route page, but no exact math content has been captured.
- `R7BSSRC004`, `BS-BRUNEI-MOE-01`: Brunei MOE Curriculum Development route page, current 200, local snapshot hash verified. It remains an official route/context row.
- `R7BSSRC005`, `BS-BRUNEI-MOE-02`: SPN21 English PDF, current 200, local hash verified. English-medium curriculum context only.
- `R7BSSRC006`, `BS-BRUNEI-MOE-03`: SPN21 Malay PDF, current 200, local hash verified. Malay curriculum context only; no higher-algebra or exact term rows captured.

## Existing Singapore Rows

- `R7BSSRC007`, `BS-SINGAPORE-CTX-01`: Singapore NIE mathematics-language context PDF, current 200, local hash verified. It is not Malay algebra terminology authority.
- `R7BSSRC008`, `BS-SINGAPORE-GAP-01`: explicit local gap row for current MOE/SEAB/ATL source return.
- `R7BSSRC009`, `BS-SINGAPORE-MOE-01`: Singapore MOE Approved Textbook List route page, current 200, local snapshot hash verified. Prior ATL parsing found math rows and Malay rows with zero overlap.
- `R7BSSRC010`, `BS-SINGAPORE-SEAB-01`: 2027 SEC G3 syllabus route, current 200, local hash verified. SEAB lists Malay local subjects separately from mathematics.
- `R7BSSRC011`, `BS-SINGAPORE-SEAB-02`: GCE O-Level school candidates route, current 200, local hash verified. Assessment route only.
- `R7BSSRC012`, `BS-SINGAPORE-SEAB-03`: AST sponsored workshops route, current 200, local hash verified. Training route only.

## New Manifest-Only Source-Return Candidates

- `R7BSSRC013`, `BS-BRUNEI-MOE-NEW-01`: Brunei MOE Document Downloads page. Current 200. The page lists `TfM handbook - Mathematics framework`; route candidate only.
- `R7BSSRC014`, `BS-BRUNEI-MOE-NEW-02`: Brunei MOE `TfM handbook - Mathematics framework` PDF. Current 200, content length `17535659`. Manifest-only; not downloaded; not exact Malay higher-algebra terminology under current evidence.
- `R7BSSRC015`, `BS-SINGAPORE-MOE-NEW-01`: Singapore MOE primary syllabus route. Current 200. Mathematics route remains separate from Malay language route.
- `R7BSSRC016`, `BS-SINGAPORE-MOE-NEW-02`: Singapore MOE secondary syllabus route. Current 200. Search evidence shows Malay/Special Programme and Mathematics as separate subject routes.
- `R7BSSRC017`, `BS-SINGAPORE-SEAB-NEW-01`: Singapore SEAB PSLE formats route. Current 200. It lists Malay Language with Malay medium and Mathematics with English medium as separate rows.

## Boundary

The Brunei/Singapore shelf remains official-route/context/source-return evidence. DBP/MABBIM remains blocked for exact Brunei math content; MOE/SEAB rows remain official route or separate-subject evidence; title/listing/context-only rows are not translation evidence. No source row in this audit authorizes Malay mathematical term promotion.
