# Noether Paper 1 — Chinese producer source custody

Purpose: bind exact translation inputs and exclude Paper 2. This is file custody, not source checking.

## Current German input

- Authority pointer SHA-256: `FAC89D076DCE1C24B534595595B75BA1C88A8956E370EF848B307E731633EED1`.
- Whole current German TeX SHA-256: `443EF950D7D45DC6D9E44A9B87501620C10DA873E50E5F2B253ECCAE6A946D27`.
- Exact Paper 1 interval: source lines 381–460; raw UTF-8 bytes `[12505,20587)`.
- Start: the title center immediately before `1. Über die Bildung des Formensystems der ternären biquadratischen Form.`.
- End: the second reduction-method enumeration and its `\end{enumerate}`.
- Excluded successor: Paper 2 `\clearpage` and setup beginning at source line 461.
- Exact local snapshot: `source/Noether_Paper01_CurrentGermanAuthority_interval.tex`.
- Snapshot bytes: `8082`.
- Snapshot SHA-256: `0499985866E646747EC31533775FF31B55556F2C694F4C2608384829DE248D2F`.

The shared `03_projects/noether/00_current_german_authority` pointer is stale at R821 and was not used.

## Translation witness

- Inherited cumulative Simplified-Chinese TeX SHA-256: `C2936EFAC3C22FBEBD3E5F418902A0A4CA3CFFD953DC3ADC827432D7529DF3F9`.
- Exact content interval: witness lines 339–466; raw UTF-8 bytes `[13119,21535)`.
- The raw offsets include the cumulative file's three-byte UTF-8 BOM; this corrects the decoded-text coordinate error recorded and superseded by `ZH-D080`.
- Exact local snapshot: `witness/Noether_Paper01_InheritedSimplifiedChinese_interval.tex`.
- Snapshot bytes: `8416`.
- Snapshot SHA-256: `566D05E74A03113F77EC75986115F2D7D71914E09B80C96AD5DF537D26F152E3`.
- Status: drafting witness only; not authority and not independently checked.

## Segmentation

- A: local source lines 1–24, SHA-256 `4FAFC711A18FBE0B9C328DB74E8FB8BD88D46B168F2446B84310222014409AAE`.
- B: local source lines 25–59, SHA-256 `52BA4686D0C7DEBF68ECF9D4811971B31DA89E86369EB4DF1C010BFEF5AF67CA`.
- C: local source lines 60–80, SHA-256 `5642B68567271B6E3236371ECDE02E67C514499AA53EBE728BCCDA47E5D38BF3`.
- The three byte-preserving segments concatenate exactly to the local source snapshot.

## Producer/checker boundary

Floris's controlling instruction is: `you do not check - you translate - other sessions CHEWCK`.

This lane translates and mechanically produces Chinese files. It does not collate scans, adjudicate the German source, check its own translation, inspect rendered pages, localize controlled Hant for Taiwan/Hong Kong/Macao, or certify readiness. Independent sessions own those checks. If an independent checker identifies a precise possible source defect, it must deduplicate it and ensure that `4 -nterslav` sees it; this producer lane does not adjudicate or duplicate-route such findings.

Decision anchors: `ZH-D079` and custody correction `ZH-D080`.
