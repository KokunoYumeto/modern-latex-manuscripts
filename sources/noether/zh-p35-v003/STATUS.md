# Chinese Noether Paper 35 — corrected producer revision status

## Current state

`CHECKER-FROZEN CORRECTIONS REALIZED AND COMPILED; INDEPENDENT RECHECK PENDING`

This sibling revision integrates `ZHCHK-NOETHER-P35-RETURN-001`. It is a translation-producer package, not a checker acceptance, final reader component, archive handoff, publication package, or certification.

| Target | Localization record | Editable TeX | Compiled PDF | Producer visual state |
|---|---|---|---|---|
| `zh-Hans-CN` | PRC-oriented Simplified Chinese | 31,328 bytes; `DDF7E898E706552028C2BCEAC4BBDE3D45487C6A339F7FA0A43968FF7E1F465C` | 274,158 bytes; `F6626C3DC6FFB82E3CFD5C21FA3F74B99459D477E39093715802C49E91E2A18C` | Not opened or rendered |
| `zh-Hans-SG` | Singapore-specific Simplified Chinese | Not produced; evidence/localization absent | Not produced | Not applicable |
| `zh-Hant-controlled` | Controlled generic Traditional script only; not TW/HK/MO prose | 31,515 bytes; `FD16882FAC33B7FD7D0FFB882345168E40FA7F1F22FDEE83AFA2420627D1C054` | 306,051 bytes; `8E77A4C511462C8ECF5876CE7EED0E3A9C4CAD8820A492BD8E665FB47FA50CF1` | Not opened or rendered |

## Authority and correction custody

- P35 binder: `NOETH-DE-BINDER-P35-20260804-001`; local receipt 6,520 bytes, SHA-256 `CFE2D81FB1E5C74EC1F73A1076F6D002A895D01056A5CEE26F844F882AF70CF3`.
- Source-native complete P35: 34,355 bytes, SHA-256 `2E205B2C51B9093FC61C77A9A1DF1C3399FCF098706CEC69134400F1ECC8E491`.
- LF translation span: 34,091 bytes, SHA-256 `DAED6EF21C297425F018C0AE6B23BC5BDD05C0B86984B3FC25FB5937DCBEBD6A`.
- Pointer v004 is route metadata only: 16,536 bytes, SHA-256 `A1C62FDACAA34DFC1B806DC18258F2E732539F7AE9D85AA4BD9E1067B8749D9F`; it does not reopen P35.
- Checker receipt: 44,258 bytes, SHA-256 `A221CD529AE306C684F3FA6FCC4989107756112D40AF5B6E088EE0D891B776E9`.
- Operative checker verifier: 4,405 bytes, SHA-256 `AAB64439C354E503F3737050B0B0E0A8003DCC9E0A0D338819D5CDDA3FF3909F`, `all_pass=true`.

## Finding disposition

- Applied exactly from the checker return: `F001` through `F012`, plus `F014`.
- Held without action: `F013`, an unresolved German-punctuation advisory. No German packet was created and German was not changed.
- The prior v001 package remains immutable rejected evidence; its 70-entry manifest is preserved as `controls/history/V001_SEED_SHA256SUMS.txt`, SHA-256 `44A91086C3736A94D042A2D0DAEC5B5DA88F179E8AF962AB06D202EC33F5888F`.
- Hans and Hant translated bodies are byte-identical to the corresponding checker-corrected candidate bodies. Producer wrapper comments differ by design.

## Build and gate state

Both targets completed two serial XeLaTeX passes with exit code `0`; each engine log reports six pages. Hans has two font-warning lines. Hant has two font-warning lines and one underfull-hbox line. These are operational facts only.

The producer did not perform source, semantic, formula, terminology, translation-quality, PDF, rendered visual, native, or regional checking. The persistent Chinese checker task `019fca9c-f549-7e71-a314-66f7265343ca` must recompile or otherwise validate the exact frozen files, freshly render every page, inspect them, and return a second sealed receipt before P35 can be accepted.

SGA remains held until Floris explicitly routes it.
