# Noether Paper 43 — Chinese producer translation notes

State: complete producer translation and mechanical builds; independent check not performed by this lane.

## Bound inputs

- Current German Paper 43 interval: `source/Noether_Paper43_CurrentGermanAuthority_interval.tex`, SHA-256 `657799FA62D58538E6AFC810221DE2C9E1F7DC481E7DDEF2CAD76506DDEB8176`.
- Exact authority interval: source lines 20096–20906, UTF-8 bytes `[1838551,1927253)`, 88,702 bytes.
- Inherited Simplified-Chinese drafting witness: `witness/Noether_Paper43_InheritedSimplifiedChinese_interval.tex`, SHA-256 `130646F67B105205CD783EDA2928A7FC45B14840D84D93DDC1AF9E1D725005CB`.
- Full authority, witness, and exclusion custody: `SOURCE_CUSTODY.md`, SHA-256 `B4E6146CDF7AF0E2523F90E612FC11F05ACD0B96E1F7C7BFB7F7AD612ADBCE4E`.

The inherited Chinese interval was substantially shorter than the current German interval and was used only for occasional drafting cues. It was not treated as an authority, completeness guarantee, or checked translation.

## Non-overlapping producer segmentation

| Segment | German interval-local lines | Source SHA-256 | Final Hans producer segment SHA-256 |
|---|---:|---|---|
| A | 1–197 | `B8D26391C1AC7371E4778D1E78BDE37AF9C930549BF4C453E4DA8D55C76A96A3` | `0FAF9B59F278C0ADA0DB197486B5CEB4ACE6E0F209AE1BDB1D2F75AD21C08DB8` |
| B | 198–427 | `8E76626F92CF250A6E903C745131A553B700760CEE64D93C65CBC9E7FDFE9C96` | `9F7988838CC175E2CFD56E8ED151A2129FB66BF2EBB0B04AB235D7F643BA3CE9` |
| C | 428–611 | `F51B496A6D1928362F96B36F992D5062A7ABD427F41FC9D2FB5E7BC5C1DD6995` | `0FF0C73B564EE04E35A0E8490E674A978A894CAEB95AF17FB940DD186C8B9CCC` |
| D | 612–811 | `0CAC2A241CACE25013E5E765A1B4E84556DCDB9CF3CC7E93CC30297B130869C9` | `97445D1F80BAD43B4908E9AEE7500E14BD1221DA88524B3E5861AB595D00DCFE` |

Segments were independent translation assignments, not review assignments. Mechanical assembly order is preamble, A, B, C, D, postamble.

## Producer terminology choices

These are translation choices and risks, not checked or approved terms:

- `Idealdifferentiation` → `理想微分`.
- technical `Differente` → `不同`; this is deliberately marked as trap-prone because it collides with ordinary Chinese `不同`.
- `Differenzenideal` / `Differenzenquotient` / `Differentialquotient` → `差分理想` / `差分商` / `微分商`.
- `definierendes Ideal` → `定义理想`.
- `direktes Produkt` / `direkte Summenzerlegung` → `直积` / `直和分解`.
- `Koeffizientenerweiterung` → `系数域扩张`.
- `Modulbasis` / `unabhängige Modulbasis` → `模基` / `独立模基`.
- `Ordnung` / `Hauptordnung` → `阶` / `主阶`.
- `Komplementärmodul` / `Komplementärbasis` → `互补模` / `互补基`.
- `Verengungsmodul` → `收缩模`; `Umfassungskörper` → provisional `包络域`.
- `Vertauschungen` → `置换`; `absoluter Modul` → provisional `绝对模`.

The producer ledgers expose sense windows, alternatives, provisional lexical-attractor basins, qualitative Mandarin-Simplified dominance debt, Hans versus controlled-Hant status, and the absence of Japanese/Korean consultation. They are not checker findings.

## Mechanical TeX correction history

The initial segment-D producer file SHA-256 was `D43A90BA340D45B53288CCD047736367951E75C6AA9E56B52151B389B0481EC3`. Halt-on-error compilation exposed math commands and superscripts that the producer had left outside TeX math delimiters. Only those TeX syntax defects were repaired; no source, semantic, formula, or translation-quality review was performed. A Chinese full stop inside a display was also moved into `\text{}` after the compiler reported one missing glyph. The final segment-D hash is `97445D1F80BAD43B4908E9AEE7500E14BD1221DA88524B3E5861AB595D00DCFE`.

The exact repair classes, superseded hashes that were captured, adverse history, and claim limit are recorded in `qa/PRODUCER_TEX_SYNTAX_REPAIR_RECORD.md`.

## Final producer outputs

- Hans TeX SHA-256 `FDAF1A0B9F55DD5A972396E41A03F69DD966CC9BEDA8D82365B7010EBC3501D7`.
- Hans PDF SHA-256 `673088FCDC3AFB5620279ABA2667305AF95B18CB141F1608058A9E7F0DE72EE9`.
- Controlled-generic Hant TeX SHA-256 `4896BE04492C3BB5EBE2AAA7668F70E45D50A6224721EF4B873B6BB21F93156E`.
- Controlled-generic Hant PDF SHA-256 `E75110A64B5A8532347FDF92C42BEDAC4D762CAD2973ECA3773C01B4204B5B21`.
- Hant is a controlled script derivative only, not Taiwan-, Hong Kong-, or Macao-localized prose.
- Both targets completed two successful XeLaTeX passes and produced compiler-reported 17-page PDFs.
- No PDF page was rendered to an image or viewed by this lane.

## Required claim limit

Floris's controlling instruction is `you do not check - you translate - other sessions CHEWCK`. This lane translated and mechanically compiled. It did not collate scans, source-check or adjudicate the German, check its own translation or formulas, validate terminology, inspect rendered pages, perform native-reader or regional localization review, approve, archive, publish, or certify the work.
