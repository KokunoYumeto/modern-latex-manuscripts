# Independent corpus v3 / branch v2 audit

Status: **PASS** — 30 direct checks, 0 failures. This audit reads the frozen outputs, source files, PDFs, search derivatives, QA images, and routing rows directly. It imports neither builder and does not build or claim the top-level v8 gate.

## Acceptance result

- Corpus: **148** records, **142** primary unique, **6** representation aliases, **66** counting eligible, **5** excluded candidates, and **9** coverage rows.
- Branch routing: **61** routes, **8** active and **53** explicit zero-body/gap routes.
- Rumantsch Grischun: exactly **3** active/counting bodies, all official general-school admissions mathematics; **3** general-school-math, **0** specialist algebra, **0** inherited-form attestations.
- Regional Romansh idioms: Sursilvan, Sutsilvan, Surmiran, Putèr, and Vallader remain five separate zero-body routes; Rumantsch Grischun is not counted as their proxy.
- Evidence boundary: every corpus row is term-promotion false. No human intelligibility claim is made. `substantive_body_present` means a reviewed mathematics body exists, not that every standard has specialist depth.

## Independently recomputed coverage

| Key | Records | Primary unique | Counting eligible | Counting bytes | Status |
|---|---:|---:|---:|---:|---|
| ca | 11 | 10 | 6 | 1102317 | substantive_body_present |
| es | 70 | 66 | 9 | 895422 | substantive_body_present |
| fr | 30 | 30 | 21 | 1692746 | substantive_body_present |
| fr_es | 4 | 4 | 0 | 0 | auxiliary_or_generated_only |
| gl | 6 | 6 | 6 | 1261078 | substantive_body_present |
| it | 8 | 8 | 8 | 1641920 | substantive_body_present |
| pt | 10 | 9 | 7 | 1509170 | substantive_body_present |
| rm | 3 | 3 | 3 | 2482929 | substantive_body_present |
| ro | 6 | 6 | 6 | 1251878 | substantive_body_present |

The RM row is 3/3/3 with 2,482,929 counting bytes, all `mathematics_education` / `secondary_school_admissions_exam`. Its reviewed tags are school arithmetic, fractions, geometry, measurement, number-line/instruction/solution-register, and word-problem tags; no abstract-, field-, group-, module-, ring-, or specialist-algebra tag occurs.

## Source identity and visual evidence

| Source | Year | Pages | PDF bytes | PDF SHA-256 | Search-text SHA-256 |
|---|---:|---:|---:|---|---|
| `CURATED-RM-RG-GRCH-AP1G-2021-M1` | 2021 | 15 | 1199558 | `388B920FC0B3D4D2B55F5157FB85ADE4A3F3B2032A9CB9D16FE1065F99B86ABE` | `71668E44E9F00D7D0351DABB6F66FF8DFE9F149C968C1827915558AB68FBD4F2` |
| `CURATED-RM-RG-GRCH-AP1G-2024-M1` | 2024 | 15 | 883275 | `71B7D02A7CAF803E434516E3C14274B4D40CBE652D165E3CD7F8794CAC6F55AA` | `054378CC16CDEF092407D49B93E1CF93E84DCA6570A3815A3175E7BC5904F649` |
| `CURATED-RM-RG-GRCH-AP1G-2024-M2` | 2024 | 6 | 400096 | `1E300CB2AC8177D09FF8A86FA06C64E2005304C4AEAF3CBC9DC1EC0405945B0D` | `0D789C2BCCD2DE09A8E193541DB8240210082CBD069913EC5D0DD35096C0EB35` |

All three URLs resolve to the recorded official `gr.ch` paths in `CURATED_EXTERNAL_SOURCE_MANIFEST_v2.csv`. Page counts were independently read from the PDFs; local PDF and text bytes/hashes match the manifest and corpus rows. Public access is verified, but no explicit reuse grant was located, so all three remain `unresolved_no_explicit_reuse_grant` and term-promotion false.

The eleven pinned 120-dpi sample PNGs hash-match their QA records. During this audit, the seven 2024 samples were freshly rendered and exactly reproduced the pinned hashes, then inspected at original detail: titles/instructions and task pages were legible, with no clipping, corruption, or missing glyphs. The crossed 2024 M1 scratch page and whitespace on 2024 M2 page 6 are intentional. The imported coverage table was separately rendered through the spreadsheet workbook engine as `qa/CORPUS_BRANCH_TABULAR_QA_v1.png` (SHA-256 `155A9F5ABE611FB589BDDA4FA5448463AF517E0FC841955E70F3DD95A1DB3A0A`) and visually inspected; all nine rows and the RM 3/3 counts are readable.

## Provenance and routing successor

Current narrative successor: `corpus/CORPUS_PROVENANCE_AND_BRANCH_ROUTING_v6.md`, SHA-256 `ADA474FF273D22BAE1FFF306AB1CEB5EC73E9998E21FF3F6DEF7262727C13B1C`. It preserves v2–v5, records exact official URLs, file/text hashes and sizes, page counts, license caveats, visual-QA hashes, v3 corpus hashes/counts, and v2 routing. It explicitly denies specialist-depth equivalence and keeps all five regional idioms at zero body.

Current frozen product hashes:

- `ROMANCE_CONSOLIDATED_CORPUS_v3.csv`: `F754A4402F91DA045A222C041C52F1E7FCF993F8B983C7C6C628E6A7FC379639`
- `ROMANCE_CORPUS_LANGUAGE_DOMAIN_COVERAGE_v3.csv`: `27E59D6B12562C9DADC5DCDF8210081EF027D8F200272A03192A952A5D19C33D`
- `ROMANCE_BRANCH_ROUTING_LEDGER_v2.csv`: `889A4C949D4D535F5683758A6B19614529DAA9EAFAE8D7B19FFE747C6469EDC3`
- `CURATED_EXTERNAL_SOURCE_MANIFEST_v2.csv`: `3870079115BC397FC765D05A41B49920FF786B795096B64912F6371F12B7C62F`

The two no-article Romansh searches remain only in `WIKIMEDIA_HTML_QUERY_LOG_v1.csv`; the current Wikimedia source manifest has 42 identifiable rows, no blank titles, no zero page/revision IDs, and no active RM rows after the four non-mathematics false hits were quarantined.

## Continuation cursor

This corpus/branch package is accepted for integration by the parent task; it is not the top-level gate. Next acquisition priority is a source-licensed specialist Rumantsch Grischun algebra body. After that, acquire and review native mathematics bodies separately for Sursilvan, Sutsilvan, Surmiran, Putèr, and Vallader. Keep every route at zero until its own native body is locally preserved, hash-verified, licensed/status-marked, and content-reviewed; inherited forms remain non-attestations.

Machine evidence: `qa/CORPUS_BRANCH_PACKAGE_AUDIT_v1.json`; concise log: `qa/CORPUS_BRANCH_PACKAGE_AUDIT_v1.log`.
