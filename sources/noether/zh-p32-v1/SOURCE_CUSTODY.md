# Noether Paper 32 — Chinese producer source custody

Purpose: bind the exact translation inputs and exclude Paper 33. This is file custody, not source checking.

## Current German input

- Authority pointer SHA-256: `FAC89D076DCE1C24B534595595B75BA1C88A8956E370EF848B307E731633EED1`.
- Whole current German TeX SHA-256: `443EF950D7D45DC6D9E44A9B87501620C10DA873E50E5F2B253ECCAE6A946D27`.
- Exact Paper 32 interval: source lines 16011–16179; raw UTF-8 bytes `[1442365,1465170)`.
- Start: `\section*{32. Gemeinsam mit R. Brauer: Über minimale Zerfällungskörper irreduzibler Darstellungen}`.
- End: the Paper 32 closing rule, `\clearpage`, `\setcounter{footnote}{0}`, and following blank line.
- Excluded successor: Paper 33 beginning at source line 16180.
- Exact local snapshot: `source/Noether_Paper32_German_current_exact_CRLF.tex`.
- Snapshot bytes: `22805`; lines: `169`.
- Snapshot SHA-256: `1E1C2E6AA32B606EAB5B57737F60CE7CF649610B490098511C29498BE8CC7611`.

The shared `03_projects/noether/00_current_german_authority` pointer is stale at R821 and was not used.

## Translation witness

- Inherited cumulative Simplified-Chinese TeX SHA-256: `C2936EFAC3C22FBEBD3E5F418902A0A4CA3CFFD953DC3ADC827432D7529DF3F9`.
- Exact witness interval: lines 16502–16654; raw UTF-8 bytes `[1258739,1276951)`.
- The raw offsets account for the cumulative file's three-byte UTF-8 BOM.
- Exact local snapshot: `witness/Noether_Paper32_SimplifiedChinese_inherited_exact_CRLF.tex`.
- Snapshot bytes: `18212`; lines: `153`.
- Snapshot SHA-256: `34655BF638E18A2B62C062D0D34E2CC44CB5FB1B9FC70B4CC748F5281761A813`.
- Status: drafting witness only; not authority and not independently checked.

## Segmentation

- A: current German lines 16011–16043, 33 lines, SHA-256 `C326204AA2934471D9A4D7D35A895F4C0780F2FD4E4689CD2A888B3FEDED4292`.
- B: current German lines 16044–16093, 50 lines, SHA-256 `FB7B610C768F6ED5B6341713C4A67BCAA1C044AE2AE638AB833028A24FF8700A`.
- C: current German lines 16094–16135, 42 lines, SHA-256 `A2ABFE407A23DC61E18665EB0DBA385B569FEE7F0EEA3CC0A9C23C457F049BEA`.
- D: current German lines 16136–16179, 44 lines, SHA-256 `EBE805D754C691DB177DB355906CC3DBBC29245FB8F6C402ED1161C9EBDE5D0E`.
- The four byte-preserving segments concatenate exactly to the local source snapshot.

## Producer/checker boundary

Floris's controlling instruction is: `you do not check - you translate - other sessions CHEWCK`.

This lane translates and mechanically produces Chinese files. It does not collate scans, adjudicate the German source, check its own translation, inspect rendered pages, localize controlled Hant for Taiwan/Hong Kong/Macao, or certify readiness. Independent sessions own those checks. If an independent checker identifies a precise possible source defect, it must deduplicate it and ensure that `4 -nterslav` sees it; this producer lane does not adjudicate or duplicate-route such findings.

Decision anchor: `ZH-D083`.
