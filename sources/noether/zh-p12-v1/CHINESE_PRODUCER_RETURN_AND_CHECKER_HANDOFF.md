# Chinese Noether Paper 12 producer return and independent-checker handoff

## Boundary and state

Floris's controlling instruction is: `you do not check - you translate - other sessions CHEWCK`.

This package is complete only as a Chinese producer translation and mechanical build. It is not source-checked, semantically checked, formula-checked, terminology-checked, translation-quality checked, visually inspected, regionally localized, approved, archive-ready, publication-ready, or certified. Every such state remains pending with separate sessions.

- Work unit: complete Noether Paper 12, *Invarianten beliebiger Differentialausdrücke*.
- Producer state: `translated/built; independent check pending`.
- Active scope: Noether only. SGA remains held until Floris explicitly confirms routing.
- Durable lane log: `C:/Users/Floris/Documents/interlanguage/03_projects/language_management/cjk/00_lane_control/CHINESE_DECISION_LOGBOOK_20260718.md`.
- Relevant decisions at handoff preparation: `ZH-D100` claim and `ZH-D101` compilation/script-transport repairs. Exact freeze is to be appended as `ZH-D102`; this document does not claim that append occurred before it did.

## Source and witness custody

- Current German authority: `C:/Users/Floris/Documents/Codex/2026-06-01/we-are-currently-doing-a-massive/Noether_P07_CurrentHead_SourceAdjudication_20260722/1/01_current/Noether_P16_IndependentSecondPass_20260722_cum_de.tex`.
- Whole authority SHA-256: `443EF950D7D45DC6D9E44A9B87501620C10DA873E50E5F2B253ECCAE6A946D27`.
- Exact P12 interval: lines 8071--8471; raw UTF-8 bytes `[547734,566458)`; 18,724 bytes; SHA-256 `CD538526814F2E5812FE1D8C03ACF2BBDB0FED7F45ECC7DE5802394B07E05652`.
- Exact local source snapshot: `source/P12_CurrentGerman_lines8071_8471.tex`, same SHA-256.
- The stale shared R821 pointer was not used.
- Inherited Simplified-Chinese content witness: lines 8012--8286; 17,218 bytes; SHA-256 `F608A96A0F968F0091E286FE61666AF93B9B9CA40F34990336B67F8E435D99CE`.
- Witness role: drafting witness only. The producer did not compare or audit it against current German.

Source segments A/B/C are contiguous by construction and concatenate byte-for-byte to the exact source snapshot:

- A: SHA-256 `FA2A7821AAC02EAAFF3322FB88EB3DA9937DF086619B20A52FFD307384E378BE`.
- B: SHA-256 `DBE25989E0F304058E79F33D28AAA0028856D58AF7E5F8F74469FE88DFF7C646`.
- C: SHA-256 `5DAB1E227F618B119B9C4358A9DA1005474E040D5CA33877FCBD9BC7A6BCD734`.

## Delivered Chinese targets

PRC-oriented Simplified Chinese:

- Segment A SHA-256: `65CB2373945FCC6973010CD29729E354DF892A4C4CDFC4E215D2E44755CDAF01`.
- Segment B SHA-256: `D8FEB6D63E9D837228503846D8B653954A36BFDC43443DC3CA4B379493502563`.
- Final segment C SHA-256: `23A21B0C662BA365ACC0373A5950C38C98577D06FD1059779B4F74B5AFA1DE64`.
- Editable TeX: `zh-Hans-CN/Noether_Paper12_Chinese_CurrentAuthority_zh-Hans-CN_v001.tex`, 17,444 bytes, SHA-256 `E98FC0F0B6B33D0E63C07DFBAC47A55CF9BCB601842013B22F72A2B78460BA77`.
- PDF: 226,917 bytes, SHA-256 `5D7BF4C532933491F28E0ECC80A9AA4D5D23AA621A4C5B9A006390BD2AA2BB12`.
- Final engine log: SHA-256 `E7FC3618C70EEC2E1D4F24B758F77E20678F86B4C71757947E2E8F6024BE6D7E`.

Controlled generic Traditional script:

- Editable TeX: `zh-Hant-controlled/Noether_Paper12_Chinese_CurrentAuthority_zh-Hant-controlled_v001.tex`, 17,786 bytes, SHA-256 `413FB3EDCB5E3C789137353DE670137AC2AEF4135A428E5AB6C58358DCA49CE3`.
- PDF: 244,189 bytes, SHA-256 `A3E65D85FD1FB21E6404040A31FE711E5D25BCB53E56299302414E83544FA872`.
- Final engine log: SHA-256 `82065B469A6AF78341309FB44964C7F65CCDBCBE63173986EC32D5E2D1AB4428`.
- Status: generic controlled-Hant script only, lexically based on PRC-oriented Hans. It is explicitly not Taiwan-, Hong-Kong-, or Macao-localized prose.

Each final target completed two XeLaTeX passes with exit code 0; the final logs report five pages and zero recorded error/warning/overfull/underfull pattern matches. Neither PDF was opened or rendered. Compilation is not validation.

## Append-only adverse production history

- Segment C initially had SHA-256 `7D2F1043466CCD6CA303D3CC257C02821F418CED70928C0F727C3F49C02D14DF`. A Hans pass-1 invocation exited 1 on an un-delimited inline TeX expression and left an incomplete two-page PDF.
- Root restored only two missing inline delimiters, intermediate segment-C SHA-256 `2022CF8A46B94849908793733D7629E9867972DEBC4CB7B197C734C550AEF591`. The next pass-1 invocation exited 1 on another un-delimited inline expression and left an incomplete three-page PDF.
- The segment translator mechanically restored the remaining intended inline delimiters without changing prose, producing the final segment-C hash above. The final Hans assembly then completed two passes.
- The initial Hans build-record page parser stored a null count because MiKTeX wrapped its summary. A metadata-only reparse recorded five pages without recompilation or viewing. Current build-record SHA-256 `C2BB357A8D4581A4C2DF7CD26CF28F766874BBA59653A78CE25A5E7A2F002AEF`.
- The first Hant wrapper invocation stopped before writing a target or record because unrestricted `s2t` changed recognized math spans. The final producer script protects 130 recognized math spans from conversion and preserves them plus 901 TeX control sequences. OpenCC record SHA-256 `E02D19A85D86D8032461619D219D242B0140374F12DBBF724E2EF060129A1756`; Hant build-record SHA-256 `C746B22F073B1FB0D18C0D6D4E9250DBF8177F65826658B52DB5C1F0D5A79497`.
- These repairs establish only compilability and mechanical transport; they do not establish formula fidelity or translation correctness.

## Producer evidence pack

- `evidence/TERMINOLOGY_LEDGER.csv`: 22 rows, SHA-256 `DE709DEB888DB41A08F112009C4A526BAF00F744B57806BB89A356C60045AE1E`.
- `evidence/ADVERSE_EVIDENCE_LEDGER.csv`: 22 rows, SHA-256 `BFE84AACB5A8833BF4C4F2AF7D5F111C1F39B3E98B9413E2F419F07F09B57759`.
- `evidence/CJKV_CROSSWALK.csv`: 22 rows, SHA-256 `32BAE501427674EDAB8D037A2359DC2AF66411F74E00A17038C2D767C79E0427`.
- `evidence/CONCEPT_EVIDENCE_GRAPH.json`: 110 nodes and 110 edges, no dangling references, SHA-256 `6C87995F66C915EB9431ECF9DA7FA48A97627506FBD22344CFEE02C2D2FE2242`.
- Deterministic generator SHA-256: `F0DC3855975EECDC84F3C9E0E3F56B8F55E7D31F65A13FA2274B0B453B074A68`.

Every row records a sense window, excluded senses, alternatives, provisional lexical-attractor basin, and qualitative Mandarin-Simplified dominance risk/debt. That risk field is not a readiness scalar. Japanese and Korean were not consulted and do not authorize Chinese.

## Independent checker queue

Separate sessions should check the exact current German against the Chinese targets, all equations/macros/numbering/footnotes, translation completeness and quality, rendered Hans/Hant PDFs, and controlled-Hant behavior. High-priority producer choices include:

- `Differentialausdruck` → `微分表达式`;
- `simultanes System` → `联立系统`;
- `Reduktionssatz` → `约化定理`;
- `Normalkoordinaten` → `正规坐标`;
- `Extremale` → `极值曲线`;
- `Polare` → `极化式`;
- `Grundfunktion` → `基本函数`;
- `Lagrangesche Gleichungen` → `Lagrange 方程`;
- `kogredient` → `同变`;
- `Formen pter Dimension` → `p 次形式`;
- `vollständiges System` → `完备系统`;
- `Riemannsche Krümmungsform` → `黎曼曲率形式`.

No producer source-defect claim exists. If a separate checker identifies a precise possible Noether source defect, deduplicate it against existing reports and ensure `4 -nterslav` sees it; this producer does not adjudicate or duplicate-route defects.

## Supporting records

- `SOURCE_CUSTODY.md` SHA-256 `16D698F5AA82441726F81F5CAECC166B415BC1469A08D2BCB6660100E7346EEA`.
- `TRANSLATION_NOTES.md` SHA-256 `DF5903993D28D9611BB02FC5871B84A254BED09CE6E68602C4BA65B1D5F2CB34`.
- `STATUS.md` SHA-256 `0439A0D43001D36D1AC04264CE6ACEC92F7F4BEF6B377C616DA1C533A0221F11`.
- `BUILD_REPORT.md` SHA-256 `789FA89D5E34983C1B796765A4FEA0058023F173CEED2E82B12A64027B2C3B27`.
- `qa/WORKER_RETURNS.md` SHA-256 `03E231D43D550FADB6960D68DCDD80680C50BC3A314350495C15C90248BBDA63`.
- `qa/HANS_COMPILE_SYNTAX_REPAIR_RECORD.md` SHA-256 `DEBC35F61C643289016C08B6D0BE8B486AB4D39AEB3FF42F3340923AE9F2AD6F`.
- `qa/HANT_MATH_PROTECTION_REPAIR_RECORD.md` SHA-256 `462C8998D2068C861741B8FB5E49A7FF95DB372558E9F2EB88EAE8FB67F6C588`.

This handoff requests independent checking only. It does not request producer self-review, promotion, publication, archive intake, or SGA work.
