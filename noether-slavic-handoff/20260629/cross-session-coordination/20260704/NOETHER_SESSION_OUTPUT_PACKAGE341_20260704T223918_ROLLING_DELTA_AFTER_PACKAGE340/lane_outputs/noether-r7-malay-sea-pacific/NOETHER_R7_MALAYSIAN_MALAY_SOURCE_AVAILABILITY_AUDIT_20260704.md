# Noether R7 Malaysian Malay Source-Availability Audit

Date: 2026-07-04

Scope: source-canon/provenance only. This audit covers the Malaysian Malay rows in the R7 source-canon witness table: course/catalog PDFs, one specialist JQMA article, UM terminology PDFs, and PRPM official search snapshots. It does not translate, approve terms, claim native review, claim canonical approval, clear licenses, promote gates, claim completion, or push Git.

Primary row table:

- `NOETHER_R7_MALAYSIAN_MALAY_SOURCE_AVAILABILITY_AUDIT_ROWS_20260704.csv`

## Method

- Re-read `NOETHER_R7_SOURCE_CANON_MATH_CORPUS_WITNESS_ROWS_20260704.csv`.
- Rechecked current R7 routing/acquisition ledgers and the B3 steward log before writing.
- Selected all 13 Malaysian Malay rows:
  - `MI-MY-COURSE-01` through `MI-MY-COURSE-06`.
  - `MI-MY-SPEC-01`.
  - `MI-MY-GLOS-01` and `MI-MY-GLOS-02`.
  - `MI-MY-PRPM-01` through `MI-MY-PRPM-04`.
- Verified every local PDF/HTML snapshot path, SHA-256, and byte count against the canonical local files under `C:\Users\memo_\Documents\Codex\2026-06-09\could-you-look-online-for-me\work\noether-slavic-canonical`.
- Ran current HEAD probes for every source URL.
- Ran throttled GitHub TeX/source-package searches for matching course, glossary, PRPM, and JQMA article-source candidates.

## Summary

- Audit rows: 13.
- Current source URLs returning HTTP 200: 13.
- Current PDF rows: 9.
- Current HTML snapshot rows: 4.
- Local path/hash/byte-count anchors verified: 13.
- Matching TeX/source packages found: 0.
- False-positive TeX hits: 2 query groups.
- Comparator-only rows: 6.
- Source-canon witness-not-translation-authority rows: 7.

## Source-Catalog Rows

The six course/catalog rows are current-accessible PDFs and have verified local hashes. They are useful as Malaysian Malay mathematical-program/course-register provenance, but they remain course metadata rather than full research proof prose.

- `R7MYSRC001`, `MI-MY-COURSE-01`: UKM Pusat Pengajian Sains Matematik guide, current PDF 200, no matching TeX/source package found.
- `R7MYSRC002`, `MI-MY-COURSE-02`: UMT Matematik Kewangan programme PDF, current PDF 200, no matching TeX/source package found.
- `R7MYSRC003`, `MI-MY-COURSE-03`: UPM Fakulti Sains 2024-2025 catalog, current PDF 200, no matching TeX/source package found.
- `R7MYSRC004`, `MI-MY-COURSE-04`: UPM Fakulti Sains 2025-2026 catalog, current PDF 200, no matching TeX/source package found.
- `R7MYSRC005`, `MI-MY-COURSE-05`: UKM Sains Matematik BM edited guide, current PDF 200. GitHub search returned a `pekikn/pengukuhan` TeX false positive, not a UKM catalog source package.
- `R7MYSRC006`, `MI-MY-COURSE-06`: UMT UG FSKM 2025-2026 BM guide, current PDF 200, no matching TeX/source package found.

## Specialist Row

`R7MYSRC013`, `MI-MY-SPEC-01`:

- Source: `Fully Right Pure Group Rings / Gelanggang Kumpulan Tulen Kanan Penuh`, JQMA 13(1), 2017.
- Current PDF status: 200.
- Local SHA-256: `7B2D75A33034C0A26115B42C028BD57B42AA8E9840B59AFC93510ACF1EB6E885`.
- Source-package result: no matching JQMA article TeX/source archive found.
- False-positive TeX hits: `RingsNetwork/whitepaper`, `stacks/stacks-project`, and `HoTT/book` were unrelated English source contexts.
- Boundary: specialist mathematical article with Malay abstract terminology; mostly English article, so do not overextend it as broad Malay proof-prose authority.

## Glossary And PRPM Comparator Rows

UM glossary rows:

- `R7MYSRC007`, `MI-MY-GLOS-01`: BM-to-English Mathematical and Statistical Terms PDF, current PDF 200, comparator-only.
- `R7MYSRC008`, `MI-MY-GLOS-02`: English-to-BM Mathematical and Statistical Terms PDF, current PDF 200, comparator-only.

PRPM rows:

- `R7MYSRC009`, `MI-MY-PRPM-01`: `invarian`, current HTML 200, comparator-only.
- `R7MYSRC010`, `MI-MY-PRPM-02`: `kovarian`, current HTML 200, comparator-only.
- `R7MYSRC011`, `MI-MY-PRPM-03`: `paduan`, current HTML 200, comparator-only.
- `R7MYSRC012`, `MI-MY-PRPM-04`: `unggulan`, current HTML 200, comparator-only.

These rows remain query/comparison provenance, not exact adoption evidence, not proof prose, and not translation authority.

## Boundary

This audit improves Malaysian Malay source-canon visibility by verifying current URLs, local hashes, byte counts, and source-package gaps. It does not change promotion state. No PRPM/MABBIM, title-only, glossary-only, course-catalog, or comparator-only row is treated as translation evidence.
