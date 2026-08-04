# Noether Paper 21 — Chinese producer mechanical build report

| Target | TeX SHA-256 | PDF SHA-256 | Final log SHA-256 | Pass exits | Pages |
|---|---|---|---|---|---:|
| `zh-Hans-CN` | `F4BCD4C27ED724EA4D79B1EAC0E427E370E2CB5BA1970200B1FD7A26D58E8235` | `A259BBC12868E9560D707CED9DB73E5BB48F77CB41B2688B33CC6CA1748232AB` | `108CFC5514C5218A2A5C32BB175F259D6135954337265E08DDBA9057387F876E` | `0`, `0` | 3 |
| `zh-Hant-controlled` | `09ECD8499AAF75027554FF51069E4C9D054D2D617A4176307F4E01000A81C9E4` | `66094E493F6A0C94C4A51DAF5785DCBCD91EBA7E5E8212A4C915FD57C5EDB194` | `38DA188AF8953D5220348E8AF1D6A4202681EEE9C9D88E56F8207D88D151BF09` | `0`, `0` | 3 |

Hans final-log matches: zero errors, font warnings, overfull boxes, and underfull boxes. Hant records report zero warnings, overfull boxes, and underfull boxes on both passes.

Hans assembly/build record SHA-256: `22B1F82F9F74E169A2FC81FD5FC1ECF4FAC49F8C7CFD709B1851BDBC8B6ED14C` / `723076C7B4A1CD9D5815062EE33DBD732740C8CF751AA2A91889DDE5FEBB4EE4`. OpenCC/Hant build record SHA-256: `FE7445CA1D2223DBB22DC77BBBF4FE6AD327EA5725C6B6C7FA56B3BB6967D04A` / `EC812A46AD2FE3A1C173D6F8BC21FA9C627604FB28589B3739565C8A4C47FCDF`.

Hant pass 1's engine exited `0` and created a three-page PDF, after which the wrapper rejected a byte-count-free MiKTeX page summary. Only the wrapper parser was broadened before pass 2; the TeX was unchanged. This is operational adverse evidence, not validation.

No PDF was opened or rendered. No source, formula, semantic, terminology, translation-quality, native/regional, approval, publication, archive, or certification check was performed. Compilation proves only mechanical buildability. Independent checking remains pending; SGA remains held.
