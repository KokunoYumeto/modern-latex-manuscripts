# Noether R7 Indonesian Publication Source-Availability Audit

Date: 2026-07-04

Scope: source-canon/provenance only. This audit covers eight high-value Indonesian mathematical proof/specialist witnesses that already have local PDF captures in the R7 source-canon table. It asks whether a source-level TeX/LaTeX/archive package can be identified for the same publication. It does not translate, approve terms, claim native review, claim canonical approval, clear licenses, promote gates, claim completion, or push Git.

Primary row table:

- `NOETHER_R7_INDONESIAN_PUBLICATION_SOURCE_AVAILABILITY_AUDIT_ROWS_20260704.csv`

## Method

- Re-read `NOETHER_R7_SOURCE_CANON_MATH_CORPUS_WITNESS_ROWS_20260704.csv`.
- Selected eight strongest Indonesian proof/specialist rows:
  - `MI-ID-PROOF-01` through `MI-ID-PROOF-05`.
  - `MI-ID-SPEC-01` through `MI-ID-SPEC-03`.
- Verified every local PDF path, SHA-256, and byte count against the canonical local files under `C:\Users\memo_\Documents\Codex\2026-06-09\could-you-look-online-for-me\work\noether-slavic-canonical`.
- Queried article/source pages for DOI, host, and license/access signals where the pages resolved.
- Ran throttled exact-title GitHub TeX searches for each publication-title cluster.
- Kept source-package results separate from adjacent source context.

## Summary

- Audit rows: 8.
- Local PDF anchors verified: 8.
- Local hash mismatches: 0.
- Local byte-count mismatches after correction: 0.
- Matching TeX/source packages found for the audited publications: 0.
- Adjacent TeX context found: 1 row, `MI-ID-PROOF-04`, pointing back to previously captured ONMIPA TeX candidates `R7GH003` and `R7GH004`.
- Current HTTP 403 access blockers: Neliti page/PDF and Unipasby page/PDF returned 403 in direct probes.
- All rows retain non-claim boundaries.

## Publication-Level Findings

`R7PUBSRC001`, `MI-ID-PROOF-01`:

- Publication: `Aljabar Weyl, Contoh Gelanggang Noether dan Prim`.
- Local PDF SHA-256: `BBC6D32ACEC9BE1F0CDB72B02BF16B0AC52DD87C4BD6BA1ECDDABCCEDB26140D`.
- Source-package result: no matching TeX/source archive found.
- Blocker: direct Neliti page/PDF probe returned HTTP 403; Garuda/Neliti metadata remains provenance, not license clearance.

`R7PUBSRC002`, `MI-ID-PROOF-02`:

- Publication: `Struktur Aljabar - Teori Ring`.
- Local PDF SHA-256: `A827A870E62C7EBB5EA1CEDA21FB36581E8252ECB6EAD205F17C6D8E07A5CC31`.
- Source-package result: no matching book TeX/source archive found.
- Page signal: UIN Alauddin repository page resolves with book item, PDF, subject `512 Aljabar`, ISBN, and official URL.

`R7PUBSRC003`, `MI-ID-PROOF-03`:

- Publication: `Hubungan antara Daerah Ideal Utama, Daerah Faktorisasi Tunggal dan Gelanggang Noetherian`.
- Local PDF SHA-256: `9ACB315B58FFFF952A1F409CA7AE4CDC4EEE395CD665AC682F2628E541F08541`.
- Source-package result: no matching TeX/source archive found.
- Page signal: MUST article page resolves with DOI `10.30651/must.v4i1.2319` and CC BY-NC 4.0 license text.

`R7PUBSRC004`, `MI-ID-PROOF-04`:

- Publication: `Ideal Prima dan Ideal Maksimal pada Gelanggang Polinomial`.
- Local PDF SHA-256: `18CFDBE1D8CAD27EDA19A6DAB1E9D258EF4F7874407D3746A8CBD6BFBBDEF16A`.
- Source-package result: no matching article source package found.
- Adjacent context: exact-title/topic GitHub search surfaced ONMIPA TeX rows already recorded as `R7GH003` and `R7GH004`; those remain adjacent problem-source context, not this article's source archive.
- Page signal: UNHAS JMSK article page resolves with DOI `10.20956/jmsk.v11i1.3431` and CC BY 4.0 license text.

`R7PUBSRC005`, `MI-ID-PROOF-05`:

- Publication: `Ideal, Homomorfisma dan Gelanggang Faktor Pada Gelanggang Artin`.
- Local PDF SHA-256: `04D26A349D7DDCEFBC4CF83F9D8B10E5A79BDFA68A023ADE6AA6CE26A05046E9`.
- Source-package result: no matching TeX/source archive found.
- Page signal: Walisongo Square article page resolves with DOI `10.21580/square.2023.5.2.17610`, CC BY-SA 4.0 license text, and separate publisher copyright-assignment language.

`R7PUBSRC006`, `MI-ID-SPEC-01`:

- Publication: `Gelanggang S-Prima Penuh`.
- Local PDF SHA-256: `B6D2CCBA134E19715D6B8907F2DC48FE562BF3580E737C0039A03CE1F5009788`.
- Source-package result: no matching TeX/source archive found.
- Blocker: current direct Unipasby page/PDF probe returned HTTP 403. Prior local capture records a CC-BY-SA text signal, but this audit makes no license-clearance claim.

`R7PUBSRC007`, `MI-ID-SPEC-02`:

- Publication: `Ring Prima dan Ring Semiprima`.
- Local PDF SHA-256: `24B389157A2440A7464280DC66CDE66D0A43E3B98297003F130AEC99C5F195BD`.
- Source-package result: no matching target-article TeX/source archive found; GitHub exact-title search returned non-target/English algebra TeX false positives.
- Page signal: Garuda metadata gives BAREKENG 7(1), DOI `10.30598/barekengvol7iss1pp1-4`, and original-source/download pointers.

`R7PUBSRC008`, `MI-ID-SPEC-03`:

- Publication: `Eksplorasi Modul Noetherian`.
- Local PDF SHA-256: `5EAE5820AFA39D1BC042277ED6C271D123746492942C85F4B2832625DF949F70`.
- Source-package result: no matching TeX/source archive found.
- Page signal: Semeton article page resolves with DOI `10.29303/semeton.v2i1.263` and CC BY-SA 4.0 license text.

## Boundary

This audit strengthens source-canon/provenance coverage for the strongest Indonesian mathematical witnesses, but it does not convert any row into translation authority. PRPM/MABBIM/title-only/comparator-only material remains outside translation support. The source package status is still blocked for the audited publications except for adjacent ONMIPA TeX context already marked as non-article-source context.
