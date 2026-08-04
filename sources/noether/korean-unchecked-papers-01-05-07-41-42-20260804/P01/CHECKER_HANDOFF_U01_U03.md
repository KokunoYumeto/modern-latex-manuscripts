# Noether Paper 1 Korean U01--U03 — unchecked checker handoff

## Exact producer return

- Output root: `${PUBLIC_INTERLANGUAGE_ROOT}\03_projects\language_management\cjk\03_working_translations\noether_paper01_ko_translation_001_20260804`.
- German snapshot: `${PUBLIC_INTERLANGUAGE_ROOT}\03_projects\language_management\cjk\03_working_translations\noether_paper01_zh_translation_001_20260722\source\Noether_Paper01_CurrentGermanAuthority_interval.tex`.
- German snapshot: 8,082 bytes; SHA-256 `0499985866E646747EC31533775FF31B55556F2C694F4C2608384829DE248D2F`.
- Historical whole-source coordinates: lines 381--460 / bytes `[12505,20587)`; historical whole SHA-256 `443EF950D7D45DC6D9E44A9B87501620C10DA873E50E5F2B253ECCAE6A946D27`.
- Present current-pointer lineage: pending from canon task `019fca5c-0e73-7c72-92fb-5b507b710598`; no defect claim.
- Scope: all substantive Paper 1 snapshot text, exactly source lines 1--80. Paper 2 is excluded.

## Unit map

| Unit | Exact source locator | Source-unit SHA-256 | Editable Korean TeX | State |
|---|---|---|---|---|
| U01 | snapshot lines 1--24 | `4FAFC711A18FBE0B9C328DB74E8FB8BD88D46B168F2446B84310222014409AAE` | `ko\Noether_Paper01_Korean_U01_translation_draft_v001.tex` | producer draft; unchecked |
| U02 | snapshot lines 25--59 | `52BA4686D0C7DEBF68ECF9D4811971B31DA89E86369EB4DF1C010BFEF5AF67CA` | `ko\Noether_Paper01_Korean_U02_translation_draft_v001.tex` | producer draft; unchecked |
| U03 | snapshot lines 60--80 | `5642B68567271B6E3236371ECDE02E67C514499AA53EBE728BCCDA47E5D38BF3` | `ko\Noether_Paper01_Korean_U03_translation_draft_v001.tex` | producer draft; unchecked |

## Producer target identities

| Unit | Target bytes | Target lines | Target SHA-256 |
|---|---:|---:|---|
| U01 | 4,452 | 32 | `48961F41A3C178968A5D2157F6FD5E756DAC7817555CAD07208C61E5A6643BE7` |
| U02 | 2,879 | 42 | `52C02759CC6D08AA102DA366F7F148A4D148EC1066E2F81DE929CEE43A46DDDF` |
| U03 | 2,111 | 29 | `ECEE0AB9E9D8C89D6A9B4FBBA63128FBE1990764847E01038AB894EF66C9DF54` |

These mechanical identities freeze the initial producer drafts. They are not evidence of source fidelity, Korean correctness, completeness, compilability, or review.

## Reproducibility authorities

- Structural JSONL: `evidence\structural_index\PRODUCER_STRUCTURAL_INDEX.jsonl`, 45 records, SHA-256 `CAB2B7FF157B86AE9CD288A65FBF1B3F5149A19F540FB549A37B56761CCAF8F4`; latest record `NOE-P01-KO-U03-LIST-ITEM-004`.
- Structural schema/builder/report SHA-256: `E5761352D61341139AB23321420817E125371DB97E2E9C9F73516739D3D1CC12` / `C4DBC59A0378AFEA4C19407564293BD0AC51F850DB2C7B384CAAE757808E59DD` / `DB2535C47F5D1B6ABBF16FF9BD1E3D633AA43153B70C1744A874FC6F05B3B429`; report status pass, errors `[]`.
- Difficulty JSONL: `evidence\difficulty_ledger\DIFFICULTY_LEDGER.jsonl`, 11 chained append-only records, SHA-256 `4B725D15BA858889C07E543FF29C2F12B22E24D03A846282CB8BB1E1E0C28D1E`; latest `CJK-KO-P01-HARD-011`; chain head `719892AD000C564729CF2B7856B210DDDD97C31FB26BD30390F0F3A35E2C71A0`.
- Difficulty schema/validator/report SHA-256: `78C206B311DF7833E643989C731BDCF0605FA791D34C5601CAEE93E02C8A4DA0` / `45C62376F67054942C9256BE2BF15D9E33C0C87F6DD7B94403570F2EFF4A6548` / `A58C41377BAC6BF5C979A3F048B7843F1223EC6BF3554BC6199CDE1EA346C59D`; report status pass, errors `[]`. The failed initializer and two failed hash-replay approaches remain in `HARD-009`--`011` and in `evidence\difficulty_ledger\rejected_attempts`.
- Visual JSONL: `evidence\visual_evidence\VISUAL_EVIDENCE_INDEX.jsonl`, zero records, empty-file SHA-256 `E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855`; validation report SHA-256 `4D12FBECEF4FD3AA4B5E89A51B2C5474927B83DF50FFCAD909273FE9E7C496E2`, pass/errors `[]`. No Paper 1 visual was used or created.
- CSV projections were imported and boundedly inspected with the bundled spreadsheet artifact runtime. `evidence\csv_artifact_validation\CSV_PROJECTIONS_ARTIFACT_TOOL_VALIDATION_REPORT.json`, SHA-256 `5D058E8CF0CA1DA452D2FBE2283061F9971355462EA3ED6C7F5ADEFAC5A0A9D7`, reports all three projections rectangular with unique nonblank headers and no formula-error matches. Spreadsheet rendering was deliberately skipped because the controlling translation-only role forbids rendering; no visual approval is inferred.

## Required independent checks

An independent Korean checker must check source/target completeness, mathematical sense, formulas and notation, bibliography/footnotes, terminology, Hangul/Hanja policy, and South-/North-Korean claim boundaries. Any suspected German defect must not be patched here. Only a precise checker-confirmed defect packet may go to the sole canon task, with stable finding ID, exact work/unit/cursor, authority path/bytes/SHA-256, affected reading, proposed correction and alternatives, evidence, defect class, uncertainty, checker identity/status, and dedup state.

## Explicitly absent

No source or scan check, Korean review, formula check, completeness check, compilation, rendering, visual inspection, assembly, packaging, certification, approval, human validation, community validation, canon adjudication, or publication action was performed by this producer lane. Validator/hash operations, if later recorded, prove only mechanical metadata state.

SGA remains outside scope.
