# Paper 35 Chinese producer freeze metadata — historical v001 seed

> Superseded for the active sibling revision by `controls/P35_FREEZE_METADATA_R2.md`. The content below remains as copied v001 custody history and must not be read as the current v002 freeze.

Prepared for final decision `ZH-D123` at 2026-08-04 04:28:28 +02:00. This is a producer-freeze record, not checker receipt or validation.

## Authority and custody

- Binder `NOETH-DE-BINDER-P35-20260804-001`: `source/current/CHINESE_P35_BINDER_20260804.json`, 6,520 bytes, SHA-256 `CFE2D81FB1E5C74EC1F73A1076F6D002A895D01056A5CEE26F844F882AF70CF3`.
- Published whole: Zenodo record `21699405`, concept `20412587`, 2,152,414 bytes, SHA-256 `8851AF561D7C40B2295DB5D4108684A06015756B9B6FDD7CCE67466E0F7F8134`.
- Complete selected source-native P35: 34,355 bytes, SHA-256 `2E205B2C51B9093FC61C77A9A1DF1C3399FCF098706CEC69134400F1ECC8E491`.
- LF-only source: 34,091 bytes, SHA-256 `DAED6EF21C297425F018C0AE6B23BC5BDD05C0B86984B3FC25FB5937DCBEBD6A`.
- Whole-head precedence remains separately unresolved; the bounded P35 binder is safe.

## Current translation segments

- A after syntax-only repair: 11,684 bytes, SHA-256 `4685ED7610EDFDD4E408EBE571CB28057607E070A7CDEFD06847E15FCD19D59C`.
- B: 7,382 bytes, SHA-256 `6E2AFE48F0F3C8644E1E3674E80F39B7BDD5B2B22A30239B17EE73CEDEBB4706`.
- C: 10,517 bytes, SHA-256 `B40A9628670A1A7602008487DC7080DA2706DC1BC4C539DA2BD4E4752AC642F3`.
- Original current-source worker returns A/B/C: SHA-256 `AA9E8AEAF7FD961F5B9BB07A66D4368D5DE112E808585795269802BEF0F689C7`, `E2ADBE671D945C40C67586A619A7ECA08C1C497B1F23FACC85DC43FED20F2E7B`, `837DBAA73111479A60E29FB61F598A485E6A2C009E55803D1D11456A6F7FA47B`.
- Syntax-repair record: SHA-256 `BCF670528231FD7C93FD48B9494D9290FDB3675FB8400F4B7E7EB547BF1E2B9D`.
- Old standalone-based segments and provisional controls ledgers remain preserved and superseded; they are excluded from current-source claims.

## Editable targets and mechanical builds

- Hans assembly/build records: SHA-256 `AC594108C0D7D8DC0E30AA0BF5D467F05A0EFD8081EFA2B32F79988DAA9EDAAD` / `FD665DD4CF2BD852050BE55C6AB44770602E80F8B20476291E53099AF1F773E3`.
- Hans TeX/PDF/log: SHA-256 `3281F6339E683F1649473E402EF4D48C8718AA7D49F4CBCB4D2902DF3B0D68AC` / `BCCA594ED14C3FD0519F337886663288540F3ED97CAC717A4FDF9A055A0F727B` / `57732F3DC89E22575FD637A565F043BF306BEF33EC23C49D51A731A378F55152`.
- OpenCC/Hant build records: SHA-256 `04FEC75572E3B2521D8E3F10ADA05E36B75BC715CB5ADA8DF6B0846A5B062D8D` / `99C25D31CEC56F6450B839DE3BBEE29E5E59B285CDC17EF43562FB12E5294A11`.
- Controlled-Hant TeX/PDF/log: SHA-256 `C408C100FB28166B293E1F1FD2C3A3D772F3CB2C881A55E30275921A19103698` / `6043ECF46EA042200F8E18DC65060B30A828572270DB8F003DA5B30C800A0B25` / `7757BFF788FBEC9C1ED4B01A1C214BAD0CCE1A3D0477AEACC2A1A612003AB159`.
- Hans and Hant each completed two serial XeLaTeX passes and report six pages. Neither PDF was opened or rendered by the producer.
- The initial failed Hans attempt is retained under `controls/failed_attempts/HANS_PASS1_20260804_0409/`.

## Current-source producer evidence

- `evidence/TERMINOLOGY_LEDGER.csv`: 12 rows, SHA-256 `84E42C53C71EDCEEAE4BA2EF176B479CA3923DC3C4959DBDE324124736F9953E`.
- `evidence/ADVERSE_EVIDENCE_LEDGER.csv`: 12 rows, SHA-256 `4C5C4F6D9D1A17283C96F58E8FABA8CE162C50F4DD59E5087C4BCADA07E0D8C6`.
- `evidence/CJKV_CROSSWALK.csv`: 12 rows, SHA-256 `F59D6735FFA2BCC611BFBCBBA077735FB81554CBC17B84E5750C780141417BD4`.
- `evidence/CONCEPT_EVIDENCE_GRAPH.json`: 48 nodes / 48 edges / zero dangling references, SHA-256 `6B5EFFAD4E61D37DC96CB8672BF169D233CFCA51F1DCA27982AB3D18D2738B91`.
- Sense windows, exclusions, alternatives, provisional lexical-attractor basins, and qualitative Mandarin-Simplified dominance risk/debt are present. These are producer/editorial proposals, never validation or readiness scalars. Japanese/Korean are blank, unconsulted, and non-authorizing.

## Documentation and shared controls

- `TRANSLATION_NOTES.md`: SHA-256 `2F1F0873C32CC16A99A1500669D6A03F28E9F192D78D27C16F785C96F5ED0DFA`.
- `STATUS.md`: SHA-256 `9A9AC1CACDD66ABABF9472701E5686EAD10271A7B43B81AD9E1B0B181A09964F`.
- `BUILD_REPORT.md`: SHA-256 `D10E67C2F6AEB6FE82C0033E312A60DF590F60D1D147DC596992E460DA55AC2D`.
- `controls/WORKER_RETURNS_CURRENT.md`: SHA-256 `0188A99AC518F8B57677584140D8DDA63236BBE1D9FB6D98484FBA4EB72658DF`.
- `CHINESE_PRODUCER_RETURN_AND_CHECKER_HANDOFF.md`: SHA-256 `E0D822BB29BA9BBB5E6565F90CD4F8046C2D69B859D81FC1CB29E1063684B0ED`.
- Shared registry pre-append: 21,500 bytes / 24 rows / SHA-256 `621FBBC721DBF14D0C9CF8259F92168B66902B7CFC5F7F3694AD858DB438D18A`.
- Shared registry post-append: 22,898 bytes / 25 rows / SHA-256 `5755ED4CA5D1CD4CCE7A8AE9C63FE1B0DACC00FCB58851A81A7A6CB22DE89BCE`; exactly one `NOETHER-P35-ZH-PRODUCER-COMPLETE` row.
- Difficulty ledger after `CJK-HARD-20260804-002`/`003`: SHA-256 `163F95728AE80BECBE25CDA5985EBA99786CFE95876FD818FE6C3916D80D37A6`.
- Lessons retrospective after Paper-35 correction: SHA-256 `1D243A3E5E87E859AAD0C98862DAE92C9306E0313C302BD9D1570C9694E0F562`.

## Claim ceiling and next route

State is `producer complete; independent check pending`. Hans is PRC-oriented. Hant is controlled generic, lexically based on Hans, and is not Taiwan-, Hong-Kong-, or Macao-localized prose. No source, semantic, formula-content, terminology, translation-quality, visual, native/regional, human/external, approval, archive/publication, or certification validation is claimed. SGA remains held.

The deterministic workspace manifest is generated only after this metadata file is present, so its own identity is recorded in `ZH-D123` rather than recursively embedded here. A distinct Chinese checker must receive the exact handoff and manifest. Any checker-confirmed possible German-source defect goes only to canon task `019fca5c-0e73-7c72-92fb-5b507b710598`; the Chinese producer does not adjudicate it.
