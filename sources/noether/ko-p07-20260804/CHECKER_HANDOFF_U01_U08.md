# Independent-checker handoff — Noether Paper 7 Korean U01--U08

Handoff state: UNCHECKED producer drafts. Receipt by a checker does not itself change review state.

## Exact authority

- Pointer: NOETH-DE-AUTH-v003-20260804
- Pointer SHA-256: 932FEDC1735A41A9CF71D15A6C662A468A4CAD016AE8B3DECDF9A71E8BA7F197
- Authority path: C:\Users\Floris\Documents\interlanguage\03_projects\noether\07_german_canon_control\candidates\NOETH-DE-ED-0001\Noether_German_NOETH-DE-ED-0001.tex
- Authority bytes / SHA-256: 2,153,565 / D1F06B311F6CBD991DD247D745DD9A72DDE326A20396DF43CFE0C8EDB1593CDB
- Paper interval: whole lines 5842--5954 / local lines 1--113
- Interval bytes / SHA-256: 8,511 / 8C5D6E8DDF24B33C5AF719F59C4CEFA0B9CEABB61960E2AC30F888CB1206AFBC
- Excluded: blank whole line 5955 and clearpage whole line 5956

## Producer targets

| Unit | Target filename | Target bytes | Target SHA-256 |
|---|---|---:|---|
| U01 | targets\Noether_P07_Korean_U01_UNCHECKED.tex | 1,891 | 96327E3C4C558450D56D62F2433EACFD8CD4ACFBBB8F648506BE939B01105507 |
| U02 | targets\Noether_P07_Korean_U02_UNCHECKED.tex | 2,136 | 813E2586E4FE975C51E21C74F8399CEEEA60139A9FDD833FF2C44888A6649177 |
| U03 | targets\Noether_P07_Korean_U03_UNCHECKED.tex | 2,498 | 7E12CEC2A1FB8A73AD5D9ADBD025B7B142B575FA064FC5671ED24E3C43F994A5 |
| U04 | targets\Noether_P07_Korean_U04_UNCHECKED.tex | 1,978 | 5387865AFD79A4C0B46930896944B0F8AD425715A177274EF51EA160CD2DC377 |
| U05 | targets\Noether_P07_Korean_U05_UNCHECKED.tex | 2,344 | A1B345CAD00CD9FC8BCB8A443A0917FFCDFA9707E006A5417B136822820F24CA |
| U06 | targets\Noether_P07_Korean_U06_UNCHECKED.tex | 1,599 | 896E625D41FEE52847CABFE77CE7426ADFE18CB8169EE8CB463D0765B5AA4AB3 |
| U07 | targets\Noether_P07_Korean_U07_UNCHECKED.tex | 2,986 | B0AE4C26E0AE0C79111820868B09049AF18A894944CCD46EF098197A9E9BCA9C |
| U08 | targets\Noether_P07_Korean_U08_UNCHECKED.tex | 2,320 | DE8AD783FF83DC27A2568D4DD47A42DA55127A912F8FDEC57BF0F50DBDE38971 |

## Required independent checks

1. Check German-to-Korean semantic completeness and detect omissions, additions, or scope shifts at each exact unit locator.
2. Check all formula tokens, delimiters, indices, equation tags, and prose references. The producer performed no formula review.
3. Check every NoetherSrcNote boundary and its bibliographic or argumentative role.
4. Adjudicate all terminology and sense windows in TRANSLATION_CHOICES_U01_U08.md using Korean-language evidence.
5. Decide Hangul/Hanja policy and ko-KR terminology; keep any ko-KP decision independently evidenced and explicitly separate.
6. Check the historical contrast between ganze rationale and rationale in U02--U08.
7. Check whether 완전계 / 완전 불변식계, 단일형, 변수열, 갈루아 레졸벤트, and 가군 기저 are acceptable and internally consistent.
8. Return stable checker finding IDs, exact unit/source/target locators, evidence class, uncertainty, and disposition.

If a checker identifies a possible German defect, the checker must not patch this producer target or the German source. The lane owner must route a precise, deduplicated, checker-confirmed defect package to the sole German-canon owner. No German defect is claimed in this handoff.

Compilation, rendering, assembly, packaging, certification, approval, and publication remain outside this producer handoff.

## Producer-metadata table integrity

The structural, difficulty, and visual CSV projections were imported through the bundled @oai/artifact-tool using the exact supplied validator. The report is:

C:\Users\Floris\Documents\interlanguage\03_projects\language_management\cjk\03_working_translations\noether_paper07_ko_translation_001_20260804\reproducibility\csv_artifact_validation\CSV_PROJECTIONS_ARTIFACT_TOOL_VALIDATION_REPORT.json

- Bytes: 2,728
- SHA-256: B2D87D6880252915EDD42B29E1F4B608CE5DE53F66109964F5804A6E46A11DC1
- Status: pass
- Structural projection: 59 data rows, 27 columns, rectangular, no blank or duplicate headers
- Difficulty projection: 14 data rows, 17 columns, rectangular, no blank or duplicate headers
- Visual projection: 0 data rows, 26 columns, rectangular header-only inventory, no blank or duplicate headers
- Render: deliberately not performed

This is producer-metadata table integrity only. It does not check or approve any German source reading, Korean wording, mathematical formula, citation content, TeX compilation, visual layout, completeness, or publication state. The independent checker must not treat this report as linguistic or mathematical review evidence.

The dependency-locator stall and bounded recovery are retained at NOE-P07-KO-HARD-014; no target TeX byte changed.
