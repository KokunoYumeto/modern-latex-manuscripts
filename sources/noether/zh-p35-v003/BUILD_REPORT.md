# Chinese Noether Paper 35 — corrected producer mechanical build report

## Boundary

This report records exact correction realization, assembly, controlled script transport, compilation, and file identity. It records no producer-side German/source adjudication, translation review, semantic or formula review, terminology validation, native/regional review, PDF opening, rendering, or visual QA.

Compiler for all final passes:

- `C:/Users/Floris/AppData/Local/Programs/MiKTeX/miktex/bin/x64/xelatex.exe`.
- 1,533,440 bytes; SHA-256 `1C3628BC7C96ED4F52B1F0AB6494225FDD5EE7914D8D3DB0E13B302E258F3326`.
- `MiKTeX-XeTeX 4.18 (MiKTeX 26.5)`.
- Options: `--quiet -interaction=nonstopmode -halt-on-error -file-line-error -no-shell-escape`.
- Direct serial scheduling, two passes per target.

## Correction realization

- Checker return intake: `controls/P35_CHECKER_RETURN_INTAKE_RECEIPT.json`, 4,575 bytes, SHA-256 `2CE735B1AF5B5B1E24B8AA7FE41E8497D0ED24B4D2E33408F1EA88668662734E`.
- Corrected A/B/C segments: 11,737 / 7,451 / 10,620 bytes; SHA-256 `26A7615B9EFD825ADF20DABF9DE34673CB1F52807AC7E07A0F0118F79E8DD3EF`, `5A2EB988239E78102D18F22AC552978AD987CE299E5B6A0D738FFA87034B2424`, `5F62E3139C5528ABCD4ACB978EA6CC14AF1B052E6E3E78CBAFBB10161B5B01B3`.
- Concatenated translated body: 29,808 bytes, SHA-256 `54061274DFDE806F491EE424277886ED4C4CEEF3F7E0315DFD1039AACF69F18A`; byte-identical to checker Hans candidate lines 47--309.
- Prebuild application record: SHA-256 `60953DCEE3A9F3B77E79396884B98FE45096D560C5515271B4E20C1B86F141E2`. Its predicted 46-line preamble was wrong.
- Postbuild realization record superseding that prediction: `controls/P35_CORRECTION_APPLICATION_REALIZATION_RECORD.json`; Hans body is actually lines 46--308. The earlier record remains preserved as adverse prebuild history.

## Hans v002

- Assembly record: `controls/HANS_ASSEMBLY_RECORD_v002.json`, 2,313 bytes, SHA-256 `F89915CFE3F54EBDB4EABB14FB9C1FD69CE45AC868C189AEFF36E305452BD651`.
- Build record: `controls/HANS_MECHANICAL_BUILD_RECORD_v002.json`, 6,858 bytes, SHA-256 `20ACB9DCCCBDCA669E506B84E66BFE267C4EFB688346BA3DB37BB0624DB8001D`.
- Editable TeX: `build/zh-Hans-CN-v002/Noether_Paper35_Chinese_CurrentAuthority_zh-Hans-CN_v002.tex`, 31,328 bytes, SHA-256 `DDF7E898E706552028C2BCEAC4BBDE3D45487C6A339F7FA0A43968FF7E1F465C`.
- Final PDF: `build/zh-Hans-CN-v002/Noether_Paper35_Chinese_CurrentAuthority_zh-Hans-CN_v002.pdf`, 274,158 bytes, SHA-256 `F6626C3DC6FFB82E3CFD5C21FA3F74B99459D477E39093715802C49E91E2A18C`.
- Final engine log: 22,516 bytes, SHA-256 `53142509FFA066537B17EC9DDE24564CCF2C80EC41A395DA9D60DB1FC206479B`.
- Result: two of two passes exited `0`; six pages reported; two font-warning lines; zero matched error, overfull, or underfull box lines.
- Producer visual state: PDF not opened or rendered.

## Controlled-generic Hant v002

- Transport record: `controls/OPENCC_PRODUCER_RECORD_v002.json`, 4,232 bytes, SHA-256 `F488CFF5CB39CAEB7437329299D5B95626A80D9C01D26555D1C0FC133EBF73F1`.
- Converter: `opencc-python-reimplemented` 0.1.7, `s2t`, followed by checker-frozen F012/F014 normalizations.
- Recorded invariants: 470 recognized math spans protected and unchanged; 790 TeX control sequences unchanged.
- Translated body: 29,808 bytes, SHA-256 `E8B36BFF9AB5ABE1CB6FE1AF45370C101B11BBA8EA5A0491EAAC0B63CD05F2D0`; byte-identical to the checker controlled-Hant v002 candidate body.
- Build record: `controls/HANT_MECHANICAL_BUILD_RECORD_v002.json`, 6,971 bytes, SHA-256 `2A33C1009BF8EA8DCE6EC394053339C55F1159BD54314029FB054665A12542B2`.
- Editable TeX: `build/zh-Hant-controlled-v002/Noether_Paper35_Chinese_CurrentAuthority_zh-Hant-controlled_v002.tex`, 31,515 bytes, SHA-256 `FD16882FAC33B7FD7D0FFB882345168E40FA7F1F22FDEE83AFA2420627D1C054`.
- Final PDF: `build/zh-Hant-controlled-v002/Noether_Paper35_Chinese_CurrentAuthority_zh-Hant-controlled_v002.pdf`, 306,051 bytes, SHA-256 `8E77A4C511462C8ECF5876CE7EED0E3A9C4CAD8820A492BD8E665FB47FA50CF1`.
- Final engine log: 23,191 bytes, SHA-256 `39FD8DBE2309D9079A893BAAD1E28254190314A7177E29C1442E4C03BA924AC7`.
- Result: two of two passes exited `0`; six pages reported; two font-warning lines, one underfull-hbox line, and zero matched error or overfull-box lines.
- Producer visual state: PDF not opened or rendered.
- Localization limit: controlled generic only; explicitly not `zh-Hant-TW`, `zh-Hant-HK`, or `zh-Hant-MO` prose.

## Interpretation limit

Compilation, page counts, warning counts, hashes, body equality, and mechanical invariants do not validate source fidelity, semantics, formulas, terminology, translation quality, visual layout, native usage, or regional localization. Both targets remain independently recheck-pending.
