# Noether R7 Source-Canon Follow-Up Discovery Probe

Generated UTC: `2026-07-04T21:09:50Z`

Mode: `source_canon_first_manifest_only`

Primary row table:

- `NOETHER_R7_SOURCE_CANON_FOLLOWUP_DISCOVERY_ROWS_20260704.csv`

This pass continues the R7 Malay-Indonesian/SEA-Pacific source-canon lane after the consolidated coverage index. It targets the highest-value open gaps: Indonesian article/book source-package absence, Malaysian Malay specialist/course source routes, and Brunei/Singapore exact-content route proof.

It does not translate, approve terms, claim native review, claim canonical approval, clear licenses, promote gates, claim completion, or push Git.

## Rechecked Before Work

- Repo-visible `AGENTS.md` and `.github/copilot-instructions.md` on branch `codex/noether-pc-20260629`.
- Parent consolidation ledger and source-canon steering record.
- B3 steward log and package boundary: B3 pushed package `348`; any package `349+` drift remains B3-owned.
- Current R7 coverage index and audit rows in this output folder.
- Slavic source-canon status/weak-language supplement patterns for manifest-only candidate and blocked-row handling.

## Search And Probe Summary

- Follow-up rows: 16.
- Strict quoted GitHub TeX query clusters: 8 query clusters, 0 TeX hits.
- GitHub repository-level query clusters: 9 query clusters, 0 repository hits.
- Broad GitHub false-positive controls: 3 non-target English Noetherian TeX metadata hits.
- Already-captured GitHub source lead repeated: 1 ONMIPA Wilayah TeX metadata row, already present as `R7GH004`.
- New remote-hashed Malaysian Malay JQMA routes: 3 rows.
- New/renewed remote-hashed Malaysian Malay UPM course routes: 2 rows plus 1 current 503 blocker.
- New/renewed remote-hashed Brunei/Singapore official routes: 3 rows.
- Raw source/PDF/HTML payload files written to `outputs`: 0.

## New Candidate Evidence

The strongest new candidate is a Malaysian Malay JQMA ring-theory route:

- Issue page: `https://www.ukm.my/jqma/jqma21-2/`
- Abstract PDF: `https://www.ukm.my/jqma/wp-content/uploads/2025/06/Abstract_11.pdf`
- Full paper PDF: `https://www.ukm.my/jqma/wp-content/uploads/2025/06/Paper_11.pdf`
- Article title: `Perfect Codes in Graph Theory: A Ring-Theoretic Perspective`
- Malay parallel title: `Kod-kod Sempurna dalam Teori Graf: Perspektif Teori Gelanggang`
- Authors: Nurhidayah Zaid, Nor Haniza Sarmin, Sanhan Muhammad Salih Khasraw, and Ibrahim Gambo.

Remote hash snapshot, in-memory only:

| Route | Status | Type | Bytes | SHA-256 |
| --- | ---: | --- | ---: | --- |
| JQMA issue page | 200 | `text/html; charset=UTF-8` | 49791 | `817C5CF32C6364CED5534ED996D9BEEAB3563D56ED37645F8BE9DBCAA5EF6439` |
| Abstract_11 PDF | 200 | `application/pdf` | 87845 | `72C98A51F4F6157995F9E6C0419E856327D9F9898CADC63CCEC0762EA0C7C565` |
| Paper_11 PDF | 200 | `application/pdf` | 326549 | `72CFA07DBC482140F28B639CA942A523AF05814CB81BC563F603BD8C3A8E1CB5` |

This is a source-canon candidate only. It is not source-level TeX, not a license-cleared payload, and not translation authority. A later pass should normalize article metadata and search for author/source repositories before adding it to the master witness table.

## Malaysian Malay Course Routes

Two UPM archived course pages were remote-hashed as current source-route candidates:

| Route | Status | Topic | Bytes | SHA-256 |
| --- | ---: | --- | ---: | --- |
| `https://learninghub.upm.edu.my/blastarc/blastdk/19202/course/info.php?id=2558` | 200 | `MTH4201-1: ALJABAR NISKALA (ABSTRACT ALGEBRA)` | 61425 | `C8FB8F08F5230D6B640673502B675B1B5EFE16EC751B7BE5C39DF2E3BD3A7B66` |
| `https://learninghub.upm.edu.my/blastarc/blastdk/20211/course/info.php?id=1902` | 200 | `MTH4205-1: KRIPTOGRAFI BERMATEMATIK (MATHEMATICAL CRYPTOGRAPHY)` | 61767 | `F88ABAA8246C99680588D3332BCEA10E9B7DADD4B299554CDC8C5383BB4C8154` |

The alternate `MTH4201` route at `https://learninghub.upm.edu.my/blastarc/blastdk/22232/course/info.php?id=3727` returned HTTP 503 during this pass. These rows are course/register evidence only, not proof-prose or TeX/source-package evidence.

## Brunei/Singapore Official Routes

Three official route pages were remote-hashed to strengthen exact-content gap records:

| Route | Status | Current use | Bytes | SHA-256 |
| --- | ---: | --- | ---: | --- |
| `https://www.moe.gov.bn/SitePages/Department%20of%20Curriculum%20Development.aspx` | 200 | Brunei route page listing Mathematics Unit and Malay Language/Literature Unit separately. | 136519 | `8C543CFD6642985E730CE1790ADC9AF83B73BB28CEFA1ED161BAFDA3530194CB` |
| `https://www.moe.gov.sg/primary/curriculum/syllabus` | 200 | Singapore MOE route page with separate Malay Language and Mathematics syllabus routes. | 122245 | `7852C70040F74E03C9A47801A1D7328368578CAA6A5D2C61B747D159C392AF55` |
| `https://www.seab.gov.sg/psle/psle-formats-examined-in-2026/` | 200 | SEAB route page showing Mathematics with English medium and Malay Language with Malay medium. | 518753 | `1DDFA7AA370237D8A1BFF967CD502F565EFB3B7038849E8B959A160261DEF22B` |

These official route pages strengthen the Brunei/Singapore blocker record: current evidence still has no exact Malay higher-algebra mathematics content. Route/context rows remain outside translation support.

## Source-Package Gaps Reaffirmed

Strict quoted GitHub TeX searches returned zero hits for the core Indonesian title/source clusters:

- `"modul" "Noetherian"`
- `"gelanggang" "ideal"`
- `"gelanggang" "polinomial"`
- `"homomorfisma" "gelanggang"`
- `"teori ring" "gelanggang"`
- `"Gelanggang S-Prima"`
- `"Eksplorasi Modul Noetherian"`
- `"Daerah Ideal Utama" "Gelanggang"`

Repository-level GitHub searches also returned zero hits for nine Malay-Indonesian/Brunei/Singapore source-package query clusters. A broad unquoted `modul Noetherian` query produced English false positives only. A broad `homomorfisma gelanggang` query repeated the existing ONMIPA Wilayah source lead already captured as `R7GH004`.

## Web Search Notes

Web search surfaced secondary or fallback routes:

- ResearchGate mirrors for Indonesian articles, including `Eksplorasi Modul Noetherian` and the PID/UFD/Noetherian article. These are secondary metadata/discovery pointers, not source packages.
- A MUST issue-level PDF route containing the PID/UFD/Noetherian article. This is fallback PDF provenance, not source TeX.
- A Scribd mirror for the UNHAS polynomial-ring article. This is non-authoritative mirror evidence and should not be used as source-canon authority.

## Boundary

Every row in the CSV carries:

```text
not translation evidence; not term approval; no native review;
no canonical approval; no license clearance; no gate promotion;
no completion claim
```

No raw source bodies, TeX files, archives, PDFs, or HTML payloads were written to `outputs`.
