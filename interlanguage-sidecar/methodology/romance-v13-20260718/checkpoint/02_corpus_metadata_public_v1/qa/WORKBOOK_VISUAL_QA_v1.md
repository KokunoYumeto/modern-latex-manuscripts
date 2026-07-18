# Romance corpus metadata workbook visual QA v1

Date: 2026-07-18. Workbook: `ROMANCE_CORPUS_METADATA_v1.xlsx`.

## Completed inspection

All six worksheets were rendered and inspected at the original preview resolution after the final formatting pass:

| Sheet | Inspected range | Preview SHA-256 | Result |
|---|---|---|---|
| Overview | `A1:H16` | `44D7176DD3C8A3429CF58E23BB2EA21A66D8F8B320A47CBA62A3370165B1F1B4` | PASS |
| Corpus | `A1:H12` | `F2150A27EE7DB748150C57A2204CFBB2B953BF948FD94A1A996761A0C969BC39` | PASS |
| Routes | `A1:L15` | `2ABB09C2D84A6C41B83D9CCCBDE8DDE4796877DC451AE4AAA54B0057BB4E86E7` | PASS |
| Language Coverage | `A1:L10` | `C71D2AF9EE0DB67BF295801567FB7BFCD8005890561A0E3054DD416A26C9FFC9` | PASS |
| Variety Coverage | `A1:L14` | `0BAE4484C66C2347DE3DB1977AD32BC8C68930326CC9188567D106F2D24AD0A4` | PASS |
| Rejected Evidence | `A1:D10` | `4776833C85945790DC60FFA75D8024178E907FD01E673404A083A0BAEDA0BDF8` | PASS |

The final visual pass found no clipped key headers, overlapping fields, blank default sheet, broken table, unreadable color contrast, or formula error. Long identifiers, locators, and adverse-evidence reasons wrap within enlarged columns/rows. The workbook contains six named tables, filters, frozen header rows, and a formula-driven Overview.

## Formula and count reconciliation

The machine inspection found zero spreadsheet error tokens. Overview formulas recompute the published source data as 153 records, 147 primary unique, 6 representation aliases, 71 counting eligible, 70 active bodies, 61 routes, 11 active routes, and 50 zero-body routes. `qa/WORKBOOK_MACHINE_QA_v1.ndjson` has SHA-256 `D25DD399B644EEB5B033838EEBB2AC2884C6E3E3190106D29E5DC5F2FF0ED43F`.

## Rebuild boundary

The six rendered PNGs and inspected formula/value surface were byte-stable across two consecutive final builder runs. The `artifact-tool` XLSX export itself emitted different container bytes across those runs even after fixed ZIP timestamps (`AFAAA118...` then current `1CCE305A...`), so byte-identical XLSX rebuild is **not claimed**. The current proposed workbook is pinned at SHA-256 `1CCE305A8C8268BF79F45B0C59B21A8D9E445ED22546254A41860AB65F8E0B3D`; reproducibility is asserted for source CSVs, formulas/values, sheet topology, and all six visual renders, not for the XLSX container identity.

This is spreadsheet usability and render QA, not source-language, rights, native-speaker, intelligibility, or lane-completion validation.
