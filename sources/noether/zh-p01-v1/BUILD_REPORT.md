# Noether Paper 1 — mechanical build report

Date: 2026-07-22  
Scope: mechanical file custody, assembly, script conversion, XeLaTeX execution, and final-log counting only.

## Source and witness custody

The exact-byte custody record is `qa/SOURCE_CUSTODY_RECORD.json`, 2,447 bytes, SHA-256 `819F9077DCD2F7BF095ED5D76A882EE6488C21D9DEA55DEA6F895CA694246F8C`.

- Current authority pointer SHA-256: `FAC89D076DCE1C24B534595595B75BA1C88A8956E370EF848B307E731633EED1`.
- Current German whole-TeX SHA-256: `443EF950D7D45DC6D9E44A9B87501620C10DA873E50E5F2B253ECCAE6A946D27`.
- Paper 1 interval: authority lines 381--460, UTF-8 byte interval `[12505,20587)`.
- Local German interval: `source/Noether_Paper01_CurrentGermanAuthority_interval.tex`, 8,082 bytes, SHA-256 `0499985866E646747EC31533775FF31B55556F2C694F4C2608384829DE248D2F`.
- Local inherited Simplified-Chinese witness: `witness/Noether_Paper01_InheritedSimplifiedChinese_interval.tex`, 8,416 bytes, SHA-256 `566D05E74A03113F77EC75986115F2D7D71914E09B80C96AD5DF537D26F152E3`; drafting-witness role only.

## Mechanical assembly and script conversion

- `qa/HANS_ASSEMBLY_RECORD.json`: 3,783 bytes, SHA-256 `E2D759B3049ECB0464EB5E55C9DCE7006810238888164E4C65C0714AA0B4D278`.
- Assembled Hans TeX: `zh-Hans-CN/Noether_Paper01_Chinese_CurrentAuthority_zh-Hans-CN_v001.tex`, 8,237 bytes, SHA-256 `5C9B88F787C447E32B1CFDF6FCFC101A69C0CB87BC7B92F703AFAC9D4C618171`.
- `qa/OPENCC_PRODUCER_RECORD.json`: 3,132 bytes, SHA-256 `E4545BEA9028D74B9496994886ED3A6E5F31C28CD27B15E995DA07447483C1CF`.
- Controlled-generic Hant TeX: `zh-Hant-controlled/Noether_Paper01_Chinese_CurrentAuthority_zh-Hant-controlled_v001.tex`, 8,398 bytes, SHA-256 `3659576C350D38F9CE2B682FB0E011A5547485A62CEEC544BAB3FA997CD0A082`.

The OpenCC producer record declares `s2t` conversion followed by controlled producer normalizations. This is a controlled-generic script derivative only; it is not `zh-Hant-TW`, `zh-Hant-HK`, or `zh-Hant-MO` localization.

## XeLaTeX production

The producer build execution comprised two XeLaTeX passes for each target. The retained `.log` in each target directory is the final-pass log.

| Target | Passes | Compiler-reported pages | TeX bytes / SHA-256 | PDF bytes / SHA-256 | Final-log bytes / SHA-256 |
|---|---:|---:|---|---|---|
| `zh-Hans-CN` | 2 | 2 | 8,237 / `5C9B88F787C447E32B1CFDF6FCFC101A69C0CB87BC7B92F703AFAC9D4C618171` | 181,147 / `0B0EB73647981EB9FFC745C65A9AC29B0B4D1CE03C8F9BEB1D0D2E977E302303` | 20,889 / `F4C78F614B4395B2D0622ECCAB137A93339EDDD3C4AC5548E2834CD58E4758D7` |
| controlled-generic `zh-Hant` | 2 | 2 | 8,398 / `3659576C350D38F9CE2B682FB0E011A5547485A62CEEC544BAB3FA997CD0A082` | 188,709 / `838CBA98C6DB190C03522D1B60C39C863C18AF528D59A454984551EAC3CD6F83` | 20,963 / `98A3A99433210D8A1BCEF43342FCA5C6BBDBB8CC30EBEA1C53CA7D1135E4D729` |

## Final-log mechanical counts

Counts below are line matches in the retained final-pass logs. Error lines are lines beginning with `!`; fatal lines match `Fatal error` or `Emergency stop`; the other columns match their named TeX diagnostic prefixes.

| Target | Error | Fatal | Missing-dollar | Font warnings | Package warnings | LaTeX warnings | Overfull | Underfull | Missing characters |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `zh-Hans-CN` | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 |
| controlled-generic `zh-Hant` | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 |

For Hans, the two font-warning lines record the unavailable italic shape `TU/MicrosoftYaHei(0)/m/it` and the summary substitution warning. For Hant, they record the unavailable italic shape `TU/MicrosoftJhengHei(0)/m/it` and the corresponding summary substitution warning.

## Claims boundary

No PDF was rendered to page images or viewed for this report. No source collation, source check, translation check, formula check, terminology check, completeness review, semantic review, visual review, native-reader review, regional localization review, external review, approval, publication readiness, or certification is asserted. All independent checking remains absent and belongs to other sessions.
