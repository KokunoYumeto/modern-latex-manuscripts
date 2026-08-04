# Noether Paper 21 — Chinese producer return for independent checking

## Exact bounded return

Complete Chinese producer translation of Paper 21, `Formale Variationsrechnung und Differentialinvarianten`, keyed to current German whole SHA-256 `443EF950D7D45DC6D9E44A9B87501620C10DA873E50E5F2B253ECCAE6A946D27` and pointer SHA-256 `FAC89D076DCE1C24B534595595B75BA1C88A8956E370EF848B307E731633EED1`.

- German interval: lines 12589–12680, raw bytes `[1001524,1011526)`, 10,002 bytes, SHA-256 `C91672CA4BB8EFEB092EDD278A4F97B6E3E94AE2059144F4FFDDA524AAF7FB96`.
- Chinese drafting witness content: lines 13388–13495, 8,794 bytes, SHA-256 `75DB55DDA93F5C68C833D77C890DA0CAC6E7B22CB0769021799B5CAD335EAE41`.
- Broader marker-to-marker witness computation through line 13504, SHA-256 `F708E570AA118F71552B44225ADEF607A90381A425158A312DD2E7251DCE44AE`, includes the explicit P22 preamble and is retained only as boundary history under `ZH-D096`; the content-only correction is `ZH-D097`.
- Custody note/JSON/segmentation SHA-256: `8CA7C7E4FAE366B44ABCD9BDC8B71A0FA060830CB7E0F55798D3EB6A81C2A2E5` / `58050EBE769D7103757011E2C20E54C3968CB9673E0A8D759E0B83E81EE6528A` / `0472076FD70AFCEDA25A0AFF7E6392BB3DBB28E36A9263E681CC60AD3D8EB904`.

The stale R821 pointer and Japanese P21 package were not used as Chinese authority or evidence.

## Translation segments

| Segment | German SHA-256 | Final Hans SHA-256 |
|---|---|---|
| A | `B6653D3F08C26A60A258BD31C21E8CC7334211D2AA20C2289272BFE49C61ED8F` | `6A15D0FF60A90B84545D35EC2A228EA96F9323F3EA1C84C469ABFC6CF8B64984` |
| B | `2CC054EA3471A2CA1755BF04B23C2451F708040B9A8F60B3F3B4753E445E26AA` | `5507F296C4AE65C5CDCF7CB452B08A5E015579A0FC506B09AF33A99E23F55383` |
| C | `CA8F97A2850467896E6ECC5717605B43E22C993B2D6BDB0BD863E915A7CF27FC` | `24AD7EC3BD1AFC99798C341876AC49525F5E44F817554187635B7CC442F7BA76` |

Segment B initially used `组量` for `Reihen`, SHA-256 `DE08C37CA9387CD07F43710DED1446F38768ADB640EE3F6F0F28ABFDE79E3679`. The producer changed only that term to `变量组` for package convergence. This is a model preference, not terminology validation. Hans assembly record SHA-256 `22B1F82F9F74E169A2FC81FD5FC1ECF4FAC49F8C7CFD709B1851BDBC8B6ED14C`.

## Editable targets and mechanical builds

| Target | TeX SHA-256 | PDF SHA-256 | Final log SHA-256 | Build |
|---|---|---|---|---|
| `zh-Hans-CN` | `F4BCD4C27ED724EA4D79B1EAC0E427E370E2CB5BA1970200B1FD7A26D58E8235` | `A259BBC12868E9560D707CED9DB73E5BB48F77CB41B2688B33CC6CA1748232AB` | `108CFC5514C5218A2A5C32BB175F259D6135954337265E08DDBA9057387F876E` | exits `0`, `0`; 3 pages |
| `zh-Hant-controlled` | `09ECD8499AAF75027554FF51069E4C9D054D2D617A4176307F4E01000A81C9E4` | `66094E493F6A0C94C4A51DAF5785DCBCD91EBA7E5E8212A4C915FD57C5EDB194` | `38DA188AF8953D5220348E8AF1D6A4202681EEE9C9D88E56F8207D88D151BF09` | exits `0`, `0`; 3 pages |

Hans/Hant build-record SHA-256: `723076C7B4A1CD9D5815062EE33DBD732740C8CF751AA2A91889DDE5FEBB4EE4` / `EC812A46AD2FE3A1C173D6F8BC21FA9C627604FB28589B3739565C8A4C47FCDF`. OpenCC producer record SHA-256 `FE7445CA1D2223DBB22DC77BBBF4FE6AD327EA5725C6B6C7FA56B3BB6967D04A`. All final matched warning/error/overfull/underfull counts are zero.

Hant pass 1's engine exited `0` and created a three-page PDF, after which the wrapper rejected a byte-count-free MiKTeX page summary. Only the wrapper parser was broadened; Hant TeX did not change. Parser-repair record SHA-256 `DE78E972F9F0B285A48E6DFD85405F4046A8A437A8B384BD562CE5B5BA8E457D`.

Neither PDF was opened or rendered. Controlled Hant is generic/nonregional and not Taiwan-, Hong Kong-, or Macao-localized prose.

## Producer evidence and checker priorities

- Terminology/adverse/CJKV ledgers: 20 rows each, SHA-256 `679184B13B168A580424E2ADF4A6F247A68A3BB92E3FCE0FBF5300697A81FDFF`, `924CFA1EC5E80E0115800F87BF4E65A4FC99E6AACE024FC8CE1E92D36AF990E8`, `00564117245C0D188DF98E01FE9FF15BB0C013F640FA7AE979DF7EE846E0776B`.
- Typed graph: 100 nodes / 100 edges, SHA-256 `D5F863120E65F360A44A1FB95800A800DD74ED6AE2C0171A6B51F389DAA10AA8`.
- Evidence generator: SHA-256 `4C909C173FFBBB5F4D3BFCDE85FD984B1B40EA81BC1C37A41BE40D9E58B21CA2`; deterministic rerun stable; Japanese and Korean unconsulted.

Producer proposals include `形式变分法`, `微分不变量`, `变分问题`, `Lagrange 表达式`, `逆变`, `协变`, `Lagrange 中心方程`, `测地线`, `协变导数`, `曲率形式`, `第二变分`, `正规形式`, `约化定理`, `等价`, `正规坐标`, `平行移动`, `不变变分问题`, `散度`, `相对不变量`, and `变量组`. Independent sessions must decide formula/source fidelity, historical terminology, footnote/citation topology, punctuation, Hant effects, and rendered layout—especially the paired `kontragredient`/`kogredient`, `Reihen`, `Parallelverschiebung`, and `Divergenzen` senses.

## Durable state

- Translation notes/status/build report SHA-256: `E6B927649919129379195E1DF4F44888CA5CA30B617341F2469BC4BAEEDBCB82` / `41C395BEFAB90A0B3D2B17046D61888AC3960FC743765421C0029107046FC062` / `0F64361A3C75E51F6D3552C1E7B97703CCE04720B2B56B2E85153ACDC065F665`.
- Worker returns SHA-256: `A1835AA4407547DE8351BC455D6DD2CE91F156B545683940523662D201002733`.
- Registry row `NOETHER-P21-ZH-PRODUCER-COMPLETE`; post-append registry SHA-256 `A31FD9E7AC98E3B9B0A0745AE2B40EE62B998DE12CBA629BA2B7D31222106232`.
- Durable lane log: `C:\Users\Floris\Documents\interlanguage\03_projects\language_management\cjk\00_lane_control\CHINESE_DECISION_LOGBOOK_20260718.md`; relevant decisions `ZH-D096`, `ZH-D097`, and producer freeze `ZH-D098`.

## Mandatory boundary

Floris's instruction is `you do not check - you translate - other sessions CHEWCK`. This return is only `translated/built; independent check pending`. The producer performed no source, formula, semantic, terminology, translation-quality, visual, native/regional, approval, publication, archive, or certification check. Compilation is not validation.

No source defect is asserted. If a separate checker finds a precise possible Noether source defect, it must deduplicate it and ensure `4 -nterslav` sees it. This producer does not adjudicate or duplicate-route. SGA remains held.
