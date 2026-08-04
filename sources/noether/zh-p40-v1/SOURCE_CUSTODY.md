# Noether Paper 40 — Chinese producer source custody

Purpose: bind the supplied translation inputs. This is file custody, not source checking.

## Current German input

- Authority pointer SHA-256: `FAC89D076DCE1C24B534595595B75BA1C88A8956E370EF848B307E731633EED1`.
- Whole current German TeX SHA-256: `443EF950D7D45DC6D9E44A9B87501620C10DA873E50E5F2B253ECCAE6A946D27`.
- Marker interval: `\section*{40.` through immediately before `\section*{41.`; lines 19061–19708; UTF-8 bytes `[1704074,1787529)`.
- Exact local snapshot: `source/Noether_Paper40_CurrentGermanAuthority_interval.tex`.
- Snapshot bytes: `83455`.
- Snapshot SHA-256: `7965805D3A75C3354C85BC7A3E4725F07BF869A8833FC19D74E32BE369427937`.

The shared `03_projects/noether/00_current_german_authority` pointer is stale at R821 and was not used.

## Translation witness

- Inherited cumulative Simplified-Chinese TeX SHA-256: `C2936EFAC3C22FBEBD3E5F418902A0A4CA3CFFD953DC3ADC827432D7529DF3F9`.
- Marker interval: lines 19511–20315; UTF-8 bytes `[1478764,1547588)`.
- Exact local snapshot: `witness/Noether_Paper40_InheritedSimplifiedChinese_interval.tex`.
- Snapshot bytes: `68824`.
- Snapshot SHA-256: `3DAD18CAB878BDFA62ED4FCC634E21AF92AF22BC8E11DF8A36888088D0A608AB`.
- Status: drafting witness only; not authority and not independently checked.

## Mechanical extraction history

The first extraction invocation created only the empty workspace directories and then stopped because its function parameter reused PowerShell's automatic `$input` variable. No snapshot file was written by that failed invocation. The corrected invocation renamed the parameter and wrote the two exact marker-bounded byte slices whose sizes and hashes are recorded above. This is a tooling event, not a source-text finding.

## Producer/checker boundary

Floris's controlling instruction is: `you do not check - you translate - other sessions CHEWCK`.

This lane translates and mechanically produces Chinese files. It does not collate scans, adjudicate the German source, check its own translation, inspect rendered pages, localize controlled Hant for Taiwan/Hong Kong/Macao, or certify readiness. Independent sessions own those checks.

Decision anchor: `ZH-D073` in `C:/Users/Floris/Documents/interlanguage/03_projects/language_management/cjk/00_lane_control/CHINESE_DECISION_LOGBOOK_20260718.md`.
