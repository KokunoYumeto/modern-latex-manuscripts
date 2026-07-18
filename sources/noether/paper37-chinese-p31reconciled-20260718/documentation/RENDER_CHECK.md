# Render check - pass

The final render set contains exactly 13 PNGs at 180 dpi under the curated paths below. Every page is 1489 by 2105 pixels.

| Path | SHA-256 |
|---|---|
| `renders/final/source-control/page-1.png` | `D652E11A14CE998A2365D827ED43515DCC2F15713CCE0C6E8F2680C4322CA6C5` |
| `renders/final/source-control/page-2.png` | `757F040811CCE97F82D547EF66B0970EFBDAC9DF1C2651E1AAE6DD62D64B0167` |
| `renders/final/source-control/page-3.png` | `6D594A234BD4216DFDB71F2A378D8E410B7EBCF88CC12D98DEFE319F968B8BB8` |
| `renders/final/source-control/page-4.png` | `5E8F7C4A7A1FA17DAB24217BCDD8AD40919542B48E84D44B2823CD0707E45B8B` |
| `renders/final/source-control/page-5.png` | `4EBC06841E76F5A5E1E1EAE1AE166C15B6C44B4C854BD05C6C447F270DC47E94` |
| `renders/final/zh-Hans-CN/page-1.png` | `F95A40135A30F87DD96490873D55477BC243F38355E0BBB20D136CF79B2D293D` |
| `renders/final/zh-Hans-CN/page-2.png` | `3AD234BDBE5AAFF86726CC54402FC782BEE1182FBF8184E21AE8B1E468906FF8` |
| `renders/final/zh-Hans-CN/page-3.png` | `04354B2E225DDC98B50CF7D420B5177666D55B400309E3A7002EE5AAEDC799B8` |
| `renders/final/zh-Hans-CN/page-4.png` | `A26FA90DF1CC659526C5295E78B5F68284F3FD72EE5450CD0C259279FA118357` |
| `renders/final/zh-Hant-controlled/page-1.png` | `F7E7E9E8E4690FA29C690584F7E0B0DC61579EE89675E06621C03154A9A3B583` |
| `renders/final/zh-Hant-controlled/page-2.png` | `689A64B37853C811334EA1EB606017832A377CD21D7B74A77D638B87C57D6510` |
| `renders/final/zh-Hant-controlled/page-3.png` | `D3BD33A1F69CD38B7A2BFCB85BEA654A7B835F3C1E5201892574F478D89E626D` |
| `renders/final/zh-Hant-controlled/page-4.png` | `387C5A257212E47E737D79187A7B9BD920F930BD161F276C7E47BEF328EC2EE9` |

Every page was individually inspected after its accepted PDF build for clipping, overlap, missing glyphs, blank or duplicate pages, displaced formulas, broken hierarchy, unreadable footnotes, and page-number collisions. No such defect was observed. `qa/RENDER_VALIDATION_REPORT.json`, SHA-256 `032A21BA82155B4FD1E8B3182D2FBEFF70F137311CF62A0C9F885C8F535B1AE7`, binds every inspected PNG by path, byte length, dimensions, and SHA-256.

This pass is internal model visual QA only. It is not an external reader, regional-language, community, or human-expert review. In particular, controlled generic Hant is not Taiwan-, Hong Kong-, or Macao-localized prose.
