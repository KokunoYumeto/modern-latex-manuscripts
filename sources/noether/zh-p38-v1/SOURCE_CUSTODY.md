# Noether Paper 38 — Chinese producer source custody

Purpose: bind the exact translation inputs and exclude Paper 39. This is file custody, not source checking or apparatus adjudication.

## Current German input

- Authority pointer SHA-256: `FAC89D076DCE1C24B534595595B75BA1C88A8956E370EF848B307E731633EED1`.
- Whole current German TeX SHA-256: `443EF950D7D45DC6D9E44A9B87501620C10DA873E50E5F2B253ECCAE6A946D27`.
- Exact Paper 38 interval: lines 18750–18970; raw UTF-8 bytes `[1658422,1685350)`.
- Start: `\section*{38. Gemeinsam mit R. Brauer und H. Hasse: Beweis eines Hauptsatzes in der Theorie der Algebren}`.
- End: closing receipt line, `\clearpage`, `\setcounter{footnote}{0}`, and following blank line.
- Excluded successor: Paper 39 beginning at source line 18971.
- Local snapshot: `source/Noether_Paper38_German_current_exact_CRLF.tex`.
- Snapshot bytes: `26928`; lines: `221`; SHA-256 `ECEC3909998D3E1BD891597D2494C5A13E7E719F1B2A6CAF802515F8EEB492AC`.

The shared `03_projects/noether/00_current_german_authority` pointer is stale at R821 and was not used. Previously recorded Paper-38 apparatus/footnote-restoration history is checker/source-owner context; this producer follows the exact supplied current interval without adjudicating that history.

## Translation witness

- Inherited cumulative Simplified-Chinese whole SHA-256: `C2936EFAC3C22FBEBD3E5F418902A0A4CA3CFFD953DC3ADC827432D7529DF3F9`.
- Exact witness interval: lines 19173–19392; raw UTF-8 bytes `[1441281,1463224)`.
- Raw offsets account for the cumulative file's three-byte UTF-8 BOM.
- Local snapshot: `witness/Noether_Paper38_SimplifiedChinese_inherited_exact_CRLF.tex`.
- Snapshot bytes: `21943`; lines: `220`; SHA-256 `EE420CD898E71EDE96ABADE3448ECF3CDE78ABF27A81D8381422F253FDC43E3E`.
- Status: drafting witness only; not authority and not independently checked.

## Segmentation

- A: current German lines 18750–18825, 76 lines, SHA-256 `53562ECCBE8611BBC65EA0BB49E761153CDEC49CAADB84554EC040BA6B6DA279`.
- B: current German lines 18826–18906, 81 lines, SHA-256 `BF22F4D02E802EF855D4C2BAADA8CD805F55A81D9A19E4FB482896C5DCF515FC`.
- C: current German lines 18907–18970, 64 lines, SHA-256 `543A4014BA6934306F5AED2810BD37412FF62D87741EE6B28A2C1D180B283165`.
- The three byte-preserving source segments concatenate exactly to the local source snapshot.

## Producer/checker boundary

Floris's controlling instruction is: `you do not check - you translate - other sessions CHEWCK`.

This lane translates and mechanically produces Chinese files. It does not collate scans or branches, adjudicate the German source/apparatus, check its own translation, inspect rendered pages, localize controlled Hant for Taiwan/Hong Kong/Macao, or certify readiness. Independent sessions own those checks. If a separate checker identifies a precise possible source defect, it must deduplicate it and ensure that `4 -nterslav` sees it; this producer lane does not adjudicate or duplicate-route findings.

Decision anchor: `ZH-D086`.
