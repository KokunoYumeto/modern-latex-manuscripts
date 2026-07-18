# Romance corpus provenance and branch routing v6

Date: 2026-07-17. This is the current corpus/branch successor record. It preserves v2–v5 as historical snapshots; v5 is the pre-2024-Rumantsch snapshot and must not be quoted for current counts. This document is **not** the top-level acceptance gate, does not assert comprehensive Romance coverage, and does not assert that every active standard has a specialist-algebra body.

Project root: `C:\Users\Floris\Documents\interlanguage\03_projects\language_management\romance\03_redo_ultra_20260717`.

## Reproducible consolidated corpus v3

`corpus/ROMANCE_CONSOLIDATED_CORPUS_v3.csv` contains 148 representation records: 142 primary-unique records and 6 representation aliases, with no byte aliases. Sixty-six rows are counting-eligible, five source candidates are explicitly excluded, and the coverage table has nine language keys. Every record ID is unique; every counting-eligible search path exists and is hash-verified; all 148 rows remain `term_promotion_eligible=false`.

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| `corpus/ROMANCE_CONSOLIDATED_CORPUS_v3.csv` | 214,383 | `F754A4402F91DA045A222C041C52F1E7FCF993F8B983C7C6C628E6A7FC379639` |
| `corpus/ROMANCE_CONSOLIDATED_CORPUS_v3.json` | 6,154 | `B0B6C772C00449A94713AD128B091F6801AFB13E39707A09284F17A9AD308037` |
| `corpus/ROMANCE_CORPUS_LANGUAGE_DOMAIN_COVERAGE_v3.csv` | 1,611 | `27E59D6B12562C9DADC5DCDF8210081EF027D8F200272A03192A952A5D19C33D` |
| `corpus/ROMANCE_CORPUS_REJECTED_OR_EXCLUDED_v3.csv` | 844 | `AE99FF27CAC6755E10D88F3D814BFFB5AD3F7C46D184DDE110CD8F05432BC7ED` |
| `qa/CORPUS_BUILD_v3.log` | 224 | `2FD4E2ABDC054B196ED96A5756FBB7BAD58DEB875DE332A73A92D9F9C8308604` |

The counts below were recomputed from the CSV rows rather than copied from the build log.

| Language key | Records | Primary unique | Counting eligible | Counting bytes | License-unresolved primary | Coverage boundary |
|---|---:|---:|---:|---:|---:|---|
| ca | 11 | 10 | 6 | 1,102,317 | 0 | specialist mathematics present, depth not claimed comprehensive |
| es | 70 | 66 | 9 | 895,422 | 53 | mixed recovered/revision-pinned shelf |
| fr | 30 | 30 | 21 | 1,692,746 | 15 | mixed recovered/revision-pinned shelf |
| fr_es | 4 | 4 | 0 | 0 | 0 | auxiliary/generated only |
| gl | 6 | 6 | 6 | 1,261,078 | 0 | specialist mathematics present, depth not claimed comprehensive |
| it | 8 | 8 | 8 | 1,641,920 | 2 | specialist mathematics present, depth not claimed comprehensive |
| pt | 10 | 9 | 7 | 1,509,170 | 0 | specialist mathematics present, depth not claimed comprehensive |
| rm | 3 | 3 | 3 | 2,482,929 | 3 | general school mathematics only; specialist algebra zero |
| ro | 6 | 6 | 6 | 1,251,878 | 0 | specialist mathematics present, depth not claimed comprehensive |

`body_status=substantive_body_present` means that a reviewed mathematics body exists. It is not a specialist-depth certification. In particular, all three `rm` rows are school-exam bodies.

## Current official Rumantsch Grischun sources

All three active sources are preserved under the isolated `corpus/downloaded_curated/rm-rg/` tree. Their institution is the Canton of Graubünden Office for Higher Education. Public access and exact local identity are verified, but no explicit reuse grant was located; all remain `unresolved_no_explicit_reuse_grant`, access/evidence only, and term-promotion false.

| Source ID and official URL | Local original | PDF bytes / pages / SHA-256 | Search text bytes / SHA-256 |
|---|---|---|---|
| `CURATED-RM-RG-GRCH-AP1G-2021-M1` — [official PDF](https://www.gr.ch/DE/institutionen/verwaltung/ekud/ahb/mittelschulen/dienstleistungen/aufnahmepruefungen/pruefung1g/pruefungsbeispiele1gym/Documents/AP21_1G_M1_RG.pdf) | `corpus/downloaded_curated/rm-rg/gr_ch_AP1G_2021/AP21_1G_M1_RG.pdf` | 1,199,558 / 15 / `388B920FC0B3D4D2B55F5157FB85ADE4A3F3B2032A9CB9D16FE1065F99B86ABE` | 15,991 / `71668E44E9F00D7D0351DABB6F66FF8DFE9F149C968C1827915558AB68FBD4F2` |
| `CURATED-RM-RG-GRCH-AP1G-2024-M1` — [official PDF](https://www.gr.ch/DE/institutionen/verwaltung/ekud/ahb/mittelschulen/dienstleistungen/aufnahmepruefungen/pruefung1g/pruefungsbeispiele1gym/Documents/AP24_1G_M1_RG.pdf) | `corpus/downloaded_curated/rm-rg/gr_ch_AP1G_2024/AP24_1G_M1_RG.pdf` | 883,275 / 15 / `71B7D02A7CAF803E434516E3C14274B4D40CBE652D165E3CD7F8794CAC6F55AA` | 15,093 / `054378CC16CDEF092407D49B93E1CF93E84DCA6570A3815A3175E7BC5904F649` |
| `CURATED-RM-RG-GRCH-AP1G-2024-M2` — [official PDF](https://www.gr.ch/DE/institutionen/verwaltung/ekud/ahb/mittelschulen/dienstleistungen/aufnahmepruefungen/pruefung1g/pruefungsbeispiele1gym/Documents/AP24_1G_M2_RG.pdf) | `corpus/downloaded_curated/rm-rg/gr_ch_AP1G_2024/AP24_1G_M2_RG.pdf` | 400,096 / 6 / `1E300CB2AC8177D09FF8A86FA06C64E2005304C4AEAF3CBC9DC1EC0405945B0D` | 9,583 / `0D789C2BCCD2DE09A8E193541DB8240210082CBD069913EC5D0DD35096C0EB35` |

The source manifest is `corpus/CURATED_EXTERNAL_SOURCE_MANIFEST_v2.csv` (3,890 bytes; SHA-256 `3870079115BC397FC765D05A41B49920FF786B795096B64912F6371F12B7C62F`). Page counts were independently read from the PDFs. The bodies cover arithmetic, fractions, geometry, measurement, number lines, exam instructions, solution register, and word problems. They are **not** abstract-algebra or specialist-algebra evidence.

## Visual and tabular QA

The 2021 QA record is `qa/RM_RG_SOURCE_VISUAL_QA_v1.md` (SHA-256 `57F21E701E42E1F34E5515A66F3576E4E32F34B765FEBC9FD0ED14A2D2B04913`), backed by four pinned 120-dpi sample renders: pages 1, 4, 8, and 13 with hashes `ED4390C3F576397F51B50DBC8859206C57379F9FC24D795DEDFA087BED63733D`, `F31DCD760846C2F74B9F9E32C44488B9843AAC8A483BBCC01AECED705A983794`, `FA766F005F31BF9748E61633DCE6F4434C2AB218F10BE6FFEC7A07F72B2F7692`, and `22C05A4CA002E5AB2EC808B0406C2C59A392F3CD1C652CF16491A87DA5510C10`.

The 2024 QA record is `qa/RM_RG_SOURCE_VISUAL_QA_v2.md` (SHA-256 `B9E8F232191AB0A73D36CA76B048F4C017B1FAF67C26B9FFFB3957E6C877B35B`). Fresh 120-dpi renders exactly reproduced the seven pinned hashes: M1 pages 1/5/10/15 `B74E514111065AC92D2B579AFF56747545B42AEE4B3B6CA16941C19142F840EC`, `CA788D6AED0977007A01EE0FF7C54AFA47BC970A8CD662AA50445013DAA47212`, `FB9EE56154FAF07AD7D680F976BFB3523214235709E45DECA242BE17A86299BB`, `98FFEB05197B6064C47791CD918565473F1DAABF6E06B1A1CE4CA716C18DE024`; M2 pages 1/3/6 `056BEBDB53943FC36DE4F1A1A699617D183EF80EC775D45B812EFBA386CCDD65`, `784ED46EFFE1FBB623320E4EAE80B80832E50C627DF239E3F6DFBAB5A49D1CD4`, and `D0BF62DF991A00849E48A6B824B36A829982D3F5664D26B2AC6C34F44B034BFB`.

All samples were inspected at original detail: title/instruction pages and bilingual/Rumantsch task pages are legible, with no clipping, corruption, or missing glyphs. The crossed final page of 2024 M1 and large whitespace on 2024 M2 page 6 are intentional exam layout. The independent workbook import/inspection render is `qa/CORPUS_BRANCH_TABULAR_QA_v1.png` (141,477 bytes; SHA-256 `155A9F5ABE611FB589BDDA4FA5448463AF517E0FC841955E70F3DD95A1DB3A0A`) with machine record `qa/CORPUS_BRANCH_TABULAR_QA_v1.json` (SHA-256 `707DF55D1E82A8D84419AADBD3696D2B9B26A8A99EED60F4BBFE8A8CC811CD7C`).

## Branch routing v2

`corpus/ROMANCE_BRANCH_ROUTING_LEDGER_v2.csv` implements 61 finite routes: 8 active and 53 explicit zero-body/gap routes. Its SHA-256 is `889A4C949D4D535F5683758A6B19614529DAA9EAFAE8D7B19FFE747C6469EDC3`; the JSON summary is SHA-256 `6E541CE057B0213582C8BCB37F259D9CAB6219C4BD0142B0E33955C17BAFFF38`. The build log is `qa/BRANCH_ROUTING_BUILD_v2.log`, SHA-256 `6BF803BA6A5E10DF3E5210642D9AB72069F452F92CAD6DB04C3E5D3476BD3168`.

Route `R008` (`rm-rg`) reports exactly three active bodies, 2,482,929 active bytes, three general-school-mathematics bodies, zero specialist-algebra bodies, zero inherited-form attestations, and `inherited_forms_are_corpus_attestation=false`. Its source IDs are exactly the three IDs listed above.

The five regional Romansh idioms remain separate zero-body routes and receive no Rumantsch Grischun proxy:

- `R009` Sursilvan (`rm-sursilvan`)
- `R010` Sutsilvan (`rm-sutsilvan`)
- `R011` Surmiran (`rm-surmiran`)
- `R012` Putèr (`rm-puter`)
- `R013` Vallader (`rm-vallader`)

Each has `current_active_body_count=0`, `current_active_bytes=0`, `inherited_form_attestation_count=0`, and `dominant_standard_not_proxy=true`.

## Quarantine and claim boundary

`corpus/WIKIMEDIA_HTML_QUERY_LOG_v1.csv` (SHA-256 `997946495C6C0C531954FC5FF571F05D1E7FAADE9DC8184202B6CDA14FD9BF9B`) alone retains the two no-article Romansh searches (`algebra matematica`, `rintg algebra`). They create no manifest rows, page/revision IDs, bytes, or downloaded counts. Four automatic-search false hits (`Biologia` twice, `Tirchia`, and `Republica Populara da la China`) remain rejected and contribute no corpus evidence. The fifth excluded candidate is a missing transfer file.

The three official Rumantsch Grischun sources establish a real general-school-mathematics shelf, not specialist terminology or human intelligibility. No inherited form, search string, orthographic score, or corpus occurrence is promoted without later sense/register review. The 53 zero-body routes and specialist-depth gaps remain visible work, not silently filled by dominant standards.

## Reproduction and audit cursor

From the project root, run:

1. `python scripts/build_consolidated_corpus_v3.py`
2. `python scripts/build_branch_routing_ledger_v2.py`
3. `python scripts/validate_corpus_branch_package_v1.py`

The independent audit and continuation cursor are `_agent_reports/corpus_v3_branch_v2_audit.md`; machine results are in `qa/CORPUS_BRANCH_PACKAGE_AUDIT_v1.json` and `qa/CORPUS_BRANCH_PACKAGE_AUDIT_v1.log`. The next acquisition priority is specialist Rumantsch Grischun algebra, followed by native mathematics bodies for the five regional idioms; none may be inferred from this package.
