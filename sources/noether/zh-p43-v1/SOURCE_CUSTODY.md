# Noether Paper 43 — Chinese producer source custody

Purpose: bind the supplied translation inputs and exclude later endmatter. This is file custody, not source checking.

## Current German input

- Authority pointer SHA-256: `FAC89D076DCE1C24B534595595B75BA1C88A8956E370EF848B307E731633EED1`.
- Whole current German TeX SHA-256: `443EF950D7D45DC6D9E44A9B87501620C10DA873E50E5F2B253ECCAE6A946D27`.
- Exact article interval: source lines 20096–20906; UTF-8 bytes `[1838551,1927253)`.
- Start: `\section*{43. Idealdifferentiation und Differente.}`.
- End: the closing receipt `Eingegangen 25. Oktober 1949.` and its center environment, followed by three blank lines.
- Excluded successor: Post44 typographic/frontmatter setup beginning at source line 20907, before the later `\section*{Einleitung}`.
- Exact local snapshot: `source/Noether_Paper43_CurrentGermanAuthority_interval.tex`.
- Snapshot bytes: `88702`.
- Snapshot SHA-256: `657799FA62D58538E6AFC810221DE2C9E1F7DC481E7DDEF2CAD76506DDEB8176`.

The shared `03_projects/noether/00_current_german_authority` pointer is stale at R821 and was not used.

## Translation witness

- Inherited cumulative Simplified-Chinese TeX SHA-256: `C2936EFAC3C22FBEBD3E5F418902A0A4CA3CFFD953DC3ADC827432D7529DF3F9`.
- Exact content interval: witness lines 20827–21280; UTF-8 bytes `[1581855,1608659)`.
- End: the declared Paper 43 `END live source-fidelity unit` comment.
- Excluded successor: Post44 `\clearpage` and `BEGIN live source-fidelity unit` at witness line 21281.
- Exact local snapshot: `witness/Noether_Paper43_InheritedSimplifiedChinese_interval.tex`.
- Snapshot bytes: `26804`.
- Snapshot SHA-256: `130646F67B105205CD783EDA2928A7FC45B14840D84D93DDC1AF9E1D725005CB`.
- Status: drafting witness only; not authority and not independently checked. Its substantial compression relative to the German source is adverse producer evidence, not a completeness finding.

## Producer/checker boundary

Floris's controlling instruction is: `you do not check - you translate - other sessions CHEWCK`.

This lane translates and mechanically produces Chinese files. It does not collate scans, adjudicate the German source, check its own translation, inspect rendered pages, localize controlled Hant for Taiwan/Hong Kong/Macao, or certify readiness. Independent sessions own those checks. If an independent checker identifies a precise possible source defect, it must deduplicate it and ensure that `4 -nterslav` sees it; this producer lane does not adjudicate or duplicate-route such findings.

Decision anchor: `ZH-D076` in `C:/Users/Floris/Documents/interlanguage/03_projects/language_management/cjk/00_lane_control/CHINESE_DECISION_LOGBOOK_20260718.md`.
