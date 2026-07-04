# Noether R7 SEA/Pacific Source-Return Audit

Date: 2026-07-04

Scope: source-canon/provenance only. This audit covers the SEA/Pacific rows in the R7 source-canon witness table and adds manifest-only item/source-return candidates found during current access checks. It does not translate, approve terms, claim native review, claim canonical approval, clear licenses, promote gates, claim completion, or push Git.

Primary row table:

- `NOETHER_R7_SEA_PACIFIC_SOURCE_RETURN_AUDIT_ROWS_20260704.csv`

## Method

- Re-read `NOETHER_R7_SOURCE_CANON_MATH_CORPUS_WITNESS_ROWS_20260704.csv`.
- Rechecked `NOETHER_R7_SOURCE_RETURN_ROUTING_REFRESH_20260704.md`.
- Rechecked the B3 steward log and GitHub instruction-bus boundary.
- Audited all 22 existing SEA/Pacific rows.
- Verified local paths, SHA-256 hashes, and byte counts for all locally captured rows.
- Re-ran current URL probes. Lao Learning Passport was checked with GET because HEAD returns 405.
- Added three manifest-only source-return candidates:
  - JICA Laos Grade 1 mathematics textbook PDF route.
  - JICA Laos Grade 5 mathematics textbook PDF route.
  - Bharatavani Santali `A New Mathamatics in Olchiki` item page.

## Summary

- Audit rows: 25.
- Existing source-canon rows audited: 22.
- New manifest-only source-return candidates: 3.
- Current URL status: `200:20`, `200_GET_HEAD_405:1`, `ERR:3`, `not_url_gap_row:1`.
- Local path/hash/byte-count anchor problems: 0.
- Exact higher-algebra/proof-prose target-language rows found: 0.
- Translation-support rows promoted: 0.

## Current Source-Return Buckets

Source-package context rows:

- `SEA-SRC-PKG-01` and `SEA-SRC-PKG-02` are arXiv LaTeX source packages for BasahaCorpus and SEACrowd context. They resolve currently, and local tar hashes verify, but neither is mathematical/algebra terminology authority.

Glossary and lower-math rows:

- Filipino/Tagalog glossary rows remain glossary/source-pointer only. The Cambium Grade 10 Filipino URL currently returns 403, while the local PDF hash remains verified.
- Hmong rows remain glossary/blocker rows. The Grade 10 URL remains blocked; the Grade 4 URL currently returns 403 despite a verified local capture.
- Cebuano DepEd rows resolve and expose exact lower-grade mathematics item metadata, including Department of Education copyright/conditions text, but remain lower-math source-return rows.
- Hiligaynon remains a listing page, not item text.

Context and language-resource rows:

- Waray and Ilokano remain academic/math-instruction context only.
- Bikol, Shan, Mien/Yao, and Mon remain language-resource/context rows, not direct math sources.
- Zhuang remains a search-gap blocker.

Lao rows:

- `SEA-LAO-01` JICA Laos primary mathematics portal resolves and lists Grade 1-5 textbooks and teacher guides.
- `SEA-LAO-02` Lao Learning Passport rejects HEAD but returns 200 with GET and matches the local snapshot size.
- New manifest-only candidates `SEA-LAO-NEW-01` and `SEA-LAO-NEW-02` record JICA Grade 1 and Grade 5 textbook PDF routes. They were not downloaded; both remain primary-math route candidates, not higher-algebra proof sources.

Khmer and Santali rows:

- `SEA-KHMER-GAP-01` now returns 200 for the English-Khmer mathematics terms PDF URL, but there is still no local payload in this lane. It is a retry candidate, not evidence.
- `SEA-KHMER-01` remains a third-party book-index/listing row.
- `SEA-SANTALI-01` remains a Bharatavani textbook listing row.
- New manifest-only candidate `SEA-SANTALI-NEW-01` records the Bharatavani item page for `A New Mathamatics in Olchiki`. The item page exposes Class VI-VIII Mathematics metadata but requires login for reading, so exact text is still blocked.

## Boundary

The SEA/Pacific shelf remains source-return, context, glossary, title/listing, source-package-context, or gap evidence. No row here supplies target-language higher-algebra proof prose or term authority for Noether translation work. Title-only, comparator-only, context-only, and lower-math rows remain outside translation support.
