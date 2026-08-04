# Noether Paper 7 — Chinese producer return for independent checking

## Exact bounded return

This package contains the complete Chinese producer translation of Paper 7, `Der Endlichkeitssatz der Invarianten endlicher Gruppen`, keyed to current German whole SHA-256 `443EF950D7D45DC6D9E44A9B87501620C10DA873E50E5F2B253ECCAE6A946D27` and authority-pointer SHA-256 `FAC89D076DCE1C24B534595595B75BA1C88A8956E370EF848B307E731633EED1`.

- German interval: lines 5819–5927, raw UTF-8 bytes `[381601,390259)`, 8,658 bytes, SHA-256 `F6C923B79406542E3DE64298DCD38887FF9A52141C71B8FF2BEBE6D14625FAEA`.
- Inherited Simplified-Chinese drafting witness: lines 6262–6395, raw bytes `[352874,360595)`, 7,721 bytes, SHA-256 `BB4686153D7241CD0F8A74164B6486C31C3BF731722334CC25B5E81AA8884AF8`; witness only.
- Source custody note/JSON SHA-256: `4C52596E38028554B223DA2F58AF1D715AF3826905EB1C1EBA85238872F928B1` / `1EC0A366587B6F2DB89743B23FD11B82A71E1971F6C865E548C7083F4B2D6D31`.
- Source segmentation record SHA-256: `5FCA68A806653B4175DAE5D27322F2D48B59E4DA8BAA6C075236E6ADC1045E62`.

The stale shared R821 pointer was not used.

## Source-keyed translation segments

| Segment | German SHA-256 | Final Hans SHA-256 |
|---|---|---|
| A | `171A565C8BFFCB0BF1AE63405BD0C68E43F7A6898B1544C8CCAC63A48CB2EBAD` | `FF6CBF848BEE518A5E7EF4AD51C34A75A3CB53C339C71C7D562A2BFC86CF5C71` |
| B | `540329352DF80393946DB81EF6EFFA6CF3F282725AE6170AF2B02F584507209B` | `7C8DF21A7D4AA0FFADE22784FEFF8838160B9D09423679FFE2446647F1EBA24A` |
| C | `35E48B0249F3C25E7E90467B4682A029C21E4C5B4202DCD63BEE277D745F4BB6` | `EDC85CFD45A3EB597DEEA836874396713E224C56D73E689121A5D6D13D86B2AE` |

Segment A initially used `单型` for `einförmig`, SHA-256 `56E8CB894EB8014282FF4C1CC730CC6045D02F7552643C4DDF18DF9948182B97`. The producer changed only that term to `单式` for cross-segment convergence; this is a model preference and remains an independent-checker question. Hans assembly record SHA-256 is `69AC60F1D41297BE2CB7FD625F9D971ED8AD7ACD0061B1FDB977E4BD5711AB8E`.

## Editable targets and mechanical builds

| Target | Editable TeX SHA-256 | PDF SHA-256 | Final log SHA-256 | Build |
|---|---|---|---|---|
| PRC-oriented `zh-Hans-CN` | `B121BC5D5649F63904444A25179FB4D882F55EF9435A5C81C1689414639BE8F4` | `EDFD8832E5EE780723B95B3643EB1DACCED22317C052214AE39F4F575E46D4C7` | `C23A69005813BD447B42ABC57A5EF41FEF6CA842467836537A3A7D5F28C03E2D` | XeLaTeX exits `0`, `0`; 3 pages reported |
| Controlled-generic `zh-Hant-controlled` | `36648843726340B02C9B7FF31EEC28008AC3CD66594F469F7769540E29DEFC79` | `A238D9E25FBC44D8D4506D63C66E0CE576F1157F753292B741A3BA9CFA401159` | `DE6DE61142697728DB6E40B421B975AB53FF82CF6E361E7A250CBE7478DCD1B0` | XeLaTeX exits `0`, `0`; 3 pages reported |

Hans/Hant build-record SHA-256 values are `96C2A1E5AAC3A283AA7FEB09FF05D1B9D9343C4D3D3676487D2D53613581BB8C` / `BCF4F5EBFF57542503BA55713368CCEEC06649FD4197CCACC566DBE54FF349E1`. OpenCC producer record SHA-256 is `CEA04C7FDD18C70E9CE31990610243441317CEB454AF041071B42A3C8CB9049A`. Controlled Hant is a generic `s2t` derivative of the Hans lexical base, not Taiwan-, Hong Kong-, or Macao-localized prose.

Each final log records two font-warning lines for unavailable italic Microsoft YaHei shape and upright substitution. Neither PDF was opened, rendered to images, or visually inspected by the producer.

## Producer terminology/evidence for checker use

- Terminology ledger: 18 rows, SHA-256 `7A6A4716E0913F8822ABAEB3F9BF5DF8C0ADE28190F809C868D3D1C772E2F839`.
- Adverse-evidence ledger: 18 rows, SHA-256 `C24B31DD65F5FA1857A1B99A7688F227263B69FA775DD10AC3BCB80F1F366D0B`.
- CJKV crosswalk: 18 rows, SHA-256 `E10E9D090BFED48879D70EDBAEC1BB4A9BB01A31E5C2158C036D17DEAEB9D940`; Japanese and Korean were not consulted.
- Typed concept/evidence graph: 90 nodes and 90 edges, SHA-256 `C7DAAD65A6B3009B5D3EDBFDE7FA3335102592374219D5A1102F5339A896EA35`.

Producer proposals include `有限性定理`, `不变量`, `模基`, `整有理不变量`, `绝对不变量`, `变量组`, `单式情形`, `Galois 预解式`, `完整不变量系`, `幂和`, `有理表示`, `相对不变量`, `次数`, and `群的阶`. These are not checked conclusions. Independent sessions should decide source fidelity, completeness, formulas, historical terminology, punctuation, typography, and rendered layout, especially `einförmig`/`单式`, `Größenreihe`/`变量组`, `Galoissche Resolvente`/`Galois 预解式`, and `volles Invariantensystem`/`完整不变量系`.

## Operational adverse evidence and durable state

The first exact-slice script invocation stopped at PowerShell parse time before writing outputs because `$OutputPath:` needed `${OutputPath}:`; the repair changed only the script's error-message interpolation. Repair record SHA-256 `5D783F402B6AE0269F104A4DEE5649651CF661D15204D7BDAEC39D97DB3A398C`.

- `TRANSLATION_NOTES.md`: SHA-256 `04D01DE44C3CBF9C13CA8AB47C3A8346D5516F098908360C529335897321EE3E`.
- `STATUS.md`: SHA-256 `6F4F44117A21A95D528AA0446162FE76D6ACC006CC976F3061CD8C5E7AF28498`.
- `BUILD_REPORT.md`: SHA-256 `09A2D21BB835EA9EC3B6036C3F39222298C09B63CDCCD490F6F142FE16EB21B1`.
- `qa/WORKER_RETURNS.md`: SHA-256 `A1A527FB4B28FC71D943B27654FE01A6D50B6542AF9E045FA268FA8204591853`.
- Shared registry row: `NOETHER-P07-ZH-PRODUCER-COMPLETE`; post-append registry SHA-256 `03477E8D7FF882945D58E63D614ACEC132B29D118DF0CAC0B1CD7B67D3009763`.
- Durable append-only lane log: `C:\Users\Floris\Documents\interlanguage\03_projects\language_management\cjk\00_lane_control\CHINESE_DECISION_LOGBOOK_20260718.md`; relevant decisions `ZH-D093` and producer freeze `ZH-D094`.

## Mandatory role boundary

Floris's controlling wording is: `you do not check - you translate - other sessions CHEWCK`.

This package is only `translated/built; independent check pending`. The producer performed no source checking/collation/adjudication, semantic/formula/terminology/translation-quality check, PDF viewing/rendered visual QA, native/regional validation, approval, publication, archive certification, or external/community certification. Successful compilation is not validation.

No Noether source defect is asserted here. If a separate checker finds a precise possible source defect, it must deduplicate the finding and ensure `4 -nterslav` sees it; the producer must not adjudicate or duplicate-route it. SGA remains held pending explicit Floris confirmation.
