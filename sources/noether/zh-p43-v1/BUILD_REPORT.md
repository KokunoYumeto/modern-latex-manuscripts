# Noether Paper 43 — Chinese mechanical build report

Build state: complete mechanical production; independent checking and visual inspection absent.

Compiler: MiKTeX-XeTeX 4.18 (MiKTeX 26.5). Each current target was compiled twice with `--quiet -interaction=nonstopmode -halt-on-error -file-line-error -no-shell-escape`.

## Final Hans target

- TeX: `zh-Hans-CN/Noether_Paper43_Chinese_CurrentAuthority_zh-Hans-CN_v001.tex`
  - bytes: `80951`
  - SHA-256: `FDAF1A0B9F55DD5A972396E41A03F69DD966CC9BEDA8D82365B7010EBC3501D7`
- PDF: `zh-Hans-CN/Noether_Paper43_Chinese_CurrentAuthority_zh-Hans-CN_v001.pdf`
  - bytes: `389170`
  - SHA-256: `673088FCDC3AFB5620279ABA2667305AF95B18CB141F1608058A9E7F0DE72EE9`
- Final compiler log: `zh-Hans-CN/Noether_Paper43_Chinese_CurrentAuthority_zh-Hans-CN_v001.log`
  - bytes: `21162`
  - SHA-256: `D58CA102FE30A81D987DCF21F7DC916CBCCFA4707F03306CE3C782F76FF869AE`
- XeLaTeX exit code: `0` on both final passes; compiler-reported pages: `17`.
- Final-log mechanical counts: errors/fatal/missing-dollar `0`; package warnings `0`; ordinary LaTeX warnings `0`; overfull boxes `0`; underfull boxes `0`; missing characters `0`; `LaTeX Font Warning` matches `2` (the unavailable `TU/MicrosoftYaHei(0)/m/it` shape and summary occurrence).

## Final controlled-generic Hant target

- TeX: `zh-Hant-controlled/Noether_Paper43_Chinese_CurrentAuthority_zh-Hant-controlled_v001.tex`
  - bytes: `81112`
  - SHA-256: `4896BE04492C3BB5EBE2AAA7668F70E45D50A6224721EF4B873B6BB21F93156E`
- PDF: `zh-Hant-controlled/Noether_Paper43_Chinese_CurrentAuthority_zh-Hant-controlled_v001.pdf`
  - bytes: `405561`
  - SHA-256: `E75110A64B5A8532347FDF92C42BEDAC4D762CAD2973ECA3773C01B4204B5B21`
- Final compiler log: `zh-Hant-controlled/Noether_Paper43_Chinese_CurrentAuthority_zh-Hant-controlled_v001.log`
  - bytes: `21236`
  - SHA-256: `9BB0272A00377BC2369EFFB890B917D7C6C2627983E1E234EB3CA3AB886A63BC`
- XeLaTeX exit code: `0` on both final passes; compiler-reported pages: `17`.
- Final-log mechanical counts: errors/fatal/missing-dollar `0`; package warnings `0`; ordinary LaTeX warnings `0`; overfull boxes `0`; underfull boxes `0`; missing characters `0`; `LaTeX Font Warning` matches `2` (the unavailable `TU/MicrosoftJhengHei(0)/m/it` shape and summary occurrence).

## Assembly and controlled-Hant custody

- Mechanical Hans assembly record SHA-256: `EBD8BFEDD4646FDC514517EC55698540A97EE5A95FE1FAD3B6270C57BBA2BEBB`.
- Controlled-Hant OpenCC producer record SHA-256: `C4A9D30486624794AFDC1D13412A4B2B3781B9564D1FB1C43FD2ABBE18D3C3DB`.
- OpenCC configuration: `s2t`, `opencc-python-reimplemented 0.1.7`; Hant remains controlled generic and nonregional.
- Producer TeX syntax-repair record: `qa/PRODUCER_TEX_SYNTAX_REPAIR_RECORD.md`.

## Superseded failed compile attempts

Before the final successful generation, halt-on-error builds stopped at producer-created TeX math-delimiter errors in segment D. The partial PDFs and logs were overwritten during repair and are not current deliverables. Captured superseded assembled Hans TeX hashes include `6B20F310AA6EBE4902C7F6E411694B5BBD1A8433EE7AF744C7B86D899DD55E71`, `A7A019BF7D933984616D07550E8CBBD7E6D6EBA01D8B269373DBD2A9B4A61CA7`, and `0BF64D6764117F7EEC5B6529851BDDF6A152BF7104E1D624A2212BBAC77DED29`. Captured superseded controlled-Hant TeX hashes include `4610FC0904E1116C4582A1EBD7A3BAB1D60C99718F396B07D7945B4341271A41`, `BD73B1AD7C5E007878EB3BF14E5660325CE1C9F562D7E3FC98E84B03C17B668F`, and `A6307CD6C5E929E734D867C07A7CB0362B453E2EC89AACC6D88632E5678808F0`. These are historical adverse production evidence only.

## Claim limit

Compilation success, hashes, log counts, and compiler-reported page counts are mechanical facts only. This lane did not compare scans, source-check, validate translation or formulas, inspect rendered pages, localize regional Hant prose, obtain human/native review, approve, archive, publish, or certify these outputs. Floris's controlling instruction remains: `you do not check - you translate - other sessions CHEWCK`.
