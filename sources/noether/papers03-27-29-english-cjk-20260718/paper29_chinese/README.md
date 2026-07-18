# Chinese Noether Paper 29 P31 rebase

This tranche contains the complete Paper 29 checkpoint for the persistent Chinese Noether lane. It is keyed to the exact sealed P31 German authority and includes editable `zh-Hans-CN` and controlled, non-localized `zh-Hant` TeX, compiled PDFs, native/adverse terminology evidence, typed decisions, source cursors, complete rendered QA, and hashes.

This is a completed bounded production unit toward the complete Chinese Noether corpus. It is not completion of the full corpus. SGA was not opened.

## Primary deliverables

| Variant | Editable source | PDF | Internal state |
|---|---|---|---|
| PRC-oriented Simplified Chinese | `zh-Hans-CN/Noether_Paper29_Chinese_P31Reconciled_zh-Hans-CN_v001.tex` | matching four-page A4 PDF | source/build/render QA pass |
| Controlled Traditional script | `zh-Hant-controlled/Noether_Paper29_Chinese_P31Reconciled_zh-Hant-controlled_v001.tex` | matching four-page A4 PDF | source/build/render QA pass; no regional-localization claim |
| German source control | `source/Noether_Paper29_German_P31_Sealed_control.tex` | five-page A4 control PDF | build/render QA pass |

`zh-Hans-SG`, `zh-Hant-TW`, `zh-Hant-HK`, and `zh-Hant-MO` remain held because no independent local-standard evidence or reviewer return exists.

## Authority

The controlling source is the sealed P31 cumulative German TeX, SHA-256 `A48CB5CD1716974B686AC1CBA681CA4B17BC72F9043B78AD2528ACA41FCF814F`. The exact raw Paper 29 slice is frozen at SHA-256 `904488A1630B36E12352A3313B16CC9283B345E28E5363E48B7E4757B388128F`.

The shared `03_projects/noether/00_current_german_authority` pointer is stale at R821 and was not used as current authority. The inherited Simplified Chinese unit is retained under `witness/` as translation witness only.

## Evidence and QA map

- `SOURCE_USE.md` and `qa/source_version_cursor.json`: exact source authority, recheck, witness roles, and pointer debt.
- `TERMINOLOGY.md`, `evidence/`, and `decisions/`: native/adverse evidence, sense windows, dominance debt, lexical-attractor basins, and schema-valid decisions.
- `BUILD_REPORT.md` and `qa/BUILD_LOG.json`: two-pass XeLaTeX builds, page counts, diagnostics, extraction, and PDF hashes.
- `RENDER_CHECK.md` and `visual_inspection/`: all 13 page renders plus contact sheets and the final visual result.
- `qa/source_alignment_checks.json`: formula, emphasis, footnote, author, and correction invariants.
- `qa/HANS_HANT_SCRIPT_DIFF_REPORT.json` and `qa/OPENCC_CONVERSION_RECORD.json`: script-derivative controls and non-localization boundary.
- `MANIFEST.csv` and `SHA256SUMS.txt`: aggregate artifact inventory and hashes; neither file hashes itself.

No external Chinese domain/community certification or controlled human-comprehension evidence is claimed.
