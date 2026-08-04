# Chinese Noether Paper 35 — corrected producer return and checker re-handoff

## Address and state

Receiving persistent Chinese checker task: `019fca9c-f549-7e71-a314-66f7265343ca`.

Producer state: `CORRECTED V002 BUILD COMPLETE; EXACT INDEPENDENT RECHECK REQUIRED`.

This is not checker acceptance, final reader assembly, archive intake, publication handoff, or certification. It asks the same checker to validate the producer-generated revision that implements return `ZHCHK-NOETHER-P35-RETURN-001`.

Exact package root:

`C:\Users\Floris\Documents\interlanguage\03_projects\language_management\cjk\03_working_translations\noether_paper35_zh_translation_002_20260804`

The deterministic root manifest is `SHA256SUMS.txt`. It is generated last and excludes only itself; the transport message and decision `ZH-D133` pin its final byte/hash identity.

## Source and control authority

- Immutable P35 binder: `NOETH-DE-BINDER-P35-20260804-001`.
- Binder custody: `source/current/CHINESE_P35_BINDER_20260804.json`, 6,520 bytes, SHA-256 `CFE2D81FB1E5C74EC1F73A1076F6D002A895D01056A5CEE26F844F882AF70CF3`.
- Source-native complete P35: 34,355 bytes, SHA-256 `2E205B2C51B9093FC61C77A9A1DF1C3399FCF098706CEC69134400F1ECC8E491`.
- LF translation source: 34,091 bytes, SHA-256 `DAED6EF21C297425F018C0AE6B23BC5BDD05C0B86984B3FC25FB5937DCBEBD6A`.
- Current global pointer v004: 16,536 bytes, SHA-256 `A1C62FDACAA34DFC1B806DC18258F2E732539F7AE9D85AA4BD9E1067B8749D9F`; route metadata only, with no P35 rebase or reopening.
- Checker receipt: `controls/checker_return_001/P35_CHECKER_RETURN_RECEIPT.json`, 44,258 bytes, SHA-256 `A221CD529AE306C684F3FA6FCC4989107756112D40AF5B6E088EE0D891B776E9`.
- Operative verifier: `controls/checker_return_001/P35_RETURN_VERIFICATION_v002.json`, 4,405 bytes, SHA-256 `AAB64439C354E503F3737050B0B0E0A8003DCC9E0A0D338819D5CDDA3FF3909F`, `all_pass=true`.
- Post-seal metadata correction: SHA-256 `BE8247A05A3BB94786D83FD60DEF1A0AB26FFC5790E62767654D3E21AC993DB2`; it fixes only the earlier truncated Hant candidate hash.

Do not use the retained failed unsuffixed/v001 checker verifiers as operative. Do not reopen the P35 binder because of pointer v004.

## Exact corrected producer outputs

| Target | Editable TeX | Compiled PDF | Producer claim |
|---|---|---|---|
| PRC-oriented `zh-Hans-CN` | `build/zh-Hans-CN-v002/Noether_Paper35_Chinese_CurrentAuthority_zh-Hans-CN_v002.tex`; 31,328 bytes; `DDF7E898E706552028C2BCEAC4BBDE3D45487C6A339F7FA0A43968FF7E1F465C` | `build/zh-Hans-CN-v002/Noether_Paper35_Chinese_CurrentAuthority_zh-Hans-CN_v002.pdf`; 274,158 bytes; `F6626C3DC6FFB82E3CFD5C21FA3F74B99459D477E39093715802C49E91E2A18C` | Corrected, compiled, independent recheck pending |
| Controlled-generic `zh-Hant-controlled` | `build/zh-Hant-controlled-v002/Noether_Paper35_Chinese_CurrentAuthority_zh-Hant-controlled_v002.tex`; 31,515 bytes; `FD16882FAC33B7FD7D0FFB882345168E40FA7F1F22FDEE83AFA2420627D1C054` | `build/zh-Hant-controlled-v002/Noether_Paper35_Chinese_CurrentAuthority_zh-Hant-controlled_v002.pdf`; 306,051 bytes; `8E77A4C511462C8ECF5876CE7EED0E3A9C4CAD8820A492BD8E665FB47FA50CF1` | Corrected script transport, compiled, independent recheck pending, nonregional |

No `zh-Hans-SG`, `zh-Hant-TW`, `zh-Hant-HK`, or `zh-Hant-MO` target exists.

## Correction realization

- Applied: `ZHCHK-P35-F001`--`F012` and `F014`.
- Held: `F013`; unresolved advisory, no German packet, no German mutation.
- Corrected Hans A/B/C body: 29,808 bytes, SHA-256 `54061274DFDE806F491EE424277886ED4C4CEEF3F7E0315DFD1039AACF69F18A`; byte-identical to the checker Hans candidate body.
- Controlled-Hant body: 29,808 bytes, SHA-256 `E8B36BFF9AB5ABE1CB6FE1AF45370C101B11BBA8EA5A0491EAAC0B63CD05F2D0`; byte-identical to the checker Hant v002 candidate body.
- Realization record: `controls/P35_CORRECTION_APPLICATION_REALIZATION_RECORD.json`.
- Finding dispositions and corrected evidence overlays: `evidence/revision2/`.

The original v001 root remains unchanged. Its 70-entry manifest identity is `44A91086C3736A94D042A2D0DAEC5B5DA88F179E8AF962AB06D202EC33F5888F`; the copied seed manifest is preserved under `controls/history/`.

## Mechanical build evidence

- Hans assembly record: 2,313 bytes, SHA-256 `F89915CFE3F54EBDB4EABB14FB9C1FD69CE45AC868C189AEFF36E305452BD651`.
- Hans build record: 6,858 bytes, SHA-256 `20ACB9DCCCBDCA669E506B84E66BFE267C4EFB688346BA3DB37BB0624DB8001D`.
- Hant transport record: 4,232 bytes, SHA-256 `F488CFF5CB39CAEB7437329299D5B95626A80D9C01D26555D1C0FC133EBF73F1`.
- Hant build record: 6,971 bytes, SHA-256 `2A33C1009BF8EA8DCE6EC394053339C55F1159BD54314029FB054665A12542B2`.
- Both targets completed two serial XeLaTeX passes and report six pages.
- Hans logs contain two font-warning lines. Hant logs contain two font-warning lines and one underfull-hbox line.
- The producer did not open or render either PDF.

## Required independent recheck

Please perform an exact independent recheck of this v002 package, including:

1. Confirm every frozen correction `F001`--`F012` and `F014` in the producer files; confirm `F013` remains nonactioned and no German claim was introduced.
2. Re-run source/coverage, semantic, mathematical/formula, terminology, punctuation/note, and target-language checks as needed against the unchanged binder source.
3. Compile the exact producer TeX files or otherwise validate their retained build evidence.
4. Freshly render every page of both producer PDFs/builds and inspect typography, glyphs, clipping, overlap, line breaks, and the recorded Hant underfull line.
5. Validate native PRC-oriented Hans only within its claim. Validate Hant only as controlled-generic script transport unless separately authorized regional evidence exists.
6. Return a new sealed receipt with exact hashes and a clear accepted/rejected state.

If a possible German defect is independently confirmed, route a schema-complete packet only to canon task `019fca5c-0e73-7c72-92fb-5b507b710598`. Do not ask this producer to inspect/adjudicate German, and do not use the retired oversized manager or `4 -nterslav` route.

SGA is outside scope and remains held.
