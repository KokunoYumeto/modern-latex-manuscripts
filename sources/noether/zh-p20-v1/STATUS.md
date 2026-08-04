# Noether Paper 20 Chinese producer status

Snapshot: 2026-07-22 12:43:12 +02:00.

## Producer outcome

Paper 20 has a complete PRC-oriented Simplified-Chinese producer translation, an editable assembled TeX target, a mechanically derived controlled-generic Traditional-script target, and two successful XeLaTeX passes for each target. This is producer completion only.

> you do not check - you translate - other sessions CHEWCK

All independent source, witness, semantic, formula-content, terminology, translation-quality, visual, regional, human/external, approval, publication, archive, and certification checks are pending.

## Current target custody

| Target artifact | Bytes | SHA-256 | Mechanical state |
|---|---:|---|---|
| zh-Hans-CN TeX | 20,245 | 262430D0A092818F859516F3FD5DE612D897D0BD8AAC49605BE047E389963065 | assembled from current A/B/C segments |
| zh-Hans-CN PDF | 235,218 | DF04B292EB1DDC80B8B1637406B7416EBF4CA947E06018D865F98424B72EA54D | two successful XeLaTeX passes; 5 pages |
| zh-Hans-CN final log | 21,148 | D4599B1218F1BC885E6F7CA3322BE71B5F9CAAA94D97E6C8B311917BFE884D13 | 2 font-warning lines; no overfull/underfull lines |
| controlled-generic zh-Hant TeX | 20,587 | 17EE7ECD25A298D8818144CE41273A31DEB85F3E49A02F08D5335B6815FF20C0 | protected script transport; not regionalized |
| controlled-generic zh-Hant PDF | 257,407 | 286400FD8AECE3D86AABC06855B53E9817A2C58AC1ED5952DF14086FAB7488EA | two successful XeLaTeX passes; 5 pages |
| controlled-generic zh-Hant final log | 21,222 | 12A88EA8BCD7FA0BB52AF870CF82DE475B1D65D5C054714203DEF0A8B6931999 | 2 font-warning lines; no overfull/underfull lines |

The producer did not open, render, or visually inspect either PDF.

## Current record custody

- SOURCE_CUSTODY.md SHA-256: BDB538768F7A5D5756CDF707632AA91517A834A0E7EBC27C195F967D7500F2AD.
- Source-custody JSON SHA-256: 5160E31529C3502D33406EFE9968EC8ABAE18175A907F37F3C8B80B3A721B79A.
- Segmentation JSON SHA-256: 5A786961ED8F08C90552FB8D6842509F16BB59375CECCEEB2185282328E459EF.
- Hans assembly record SHA-256: 39A4D15DEBEC4E45D3032B9554A6D83B552957031074264ECC5D3DB66A673B2D.
- Hans mechanical-build record SHA-256: 78CE6579A83531D42FBD3007042AA69BF742DCEF35D68F558234DF91F685B779.
- OpenCC producer record SHA-256: 80A7FC6B1D859A63CC4BC602CC289860098EA317BE158D32D3BEE048CD541B76.
- Hant mechanical-build record SHA-256: D71DB684736DCE854A98C1FBF5548A8CC00D173F244F95D8C9CEB8F31BEB2FF9.

## Mechanical adverse history retained

- Segment A moved append-only through B637B38DBD55BCF8BA6862F000B48D9108FC77F8D42D083762A5AE97081559FC, 51BDBA85125DC72494746B49540FD6EF5DE21D7DD2854F86558B726E06586B3F, F4317188496FE61F220343C1C941E7D6F7EF02707F463D3FA208203963BD1AC6, 80AA4F63166554C74EB29806CF1DCE77A6C98F1DB31EC181FD1BF9A372CCC4DC, and current DC694B77A78B1D12E12BC5A3DA315147538847F23F0E46772D85A7BAE9181834.
- The first three pass-1 invocations stopped with no pages at three separate un-delimited (n\ge2) literals.
- The fourth pass-1 invocation produced one page and stopped at malformed (F(x,y)\).
- Every repair restored delimiters only; no prose changed.
- The final Hans assembly SHA-256 262430D0A092818F859516F3FD5DE612D897D0BD8AAC49605BE047E389963065 completed two passes and produced the current 5-page PDF.
- Hant transport protected 220 recognized math spans and retained an ordered stream of 742 TeX control sequences.

These are mechanical production facts, not checks.

## Localization and scope

The Hant output is controlled generic and nonregional. It is not Taiwan-, Hong Kong-, or Macao-localized prose. SGA remains held; this producer state covers Noether Paper 20 only.

