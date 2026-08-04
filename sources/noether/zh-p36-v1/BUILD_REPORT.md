# Noether Paper 36 — Chinese producer mechanical build report

## Inputs and outputs

| Target | TeX SHA-256 | PDF SHA-256 | Final log SHA-256 | Pass exits | Pages reported by log |
|---|---|---|---|---|---:|
| `zh-Hans-CN` | `928C90ED8A02FA9F5BAA5E891CE780CCFF76878BB86515D84F7064E8998E6416` | `2DCF4B5A1635475AD1BA69F0EB01A877D6A4FE0A707C0EA31C1B11E286C04922` | `09E702C97DF18F1F8B9F84D0AA31EB5873EC771778C36172D6FCC2DA88829BC8` | `0`, `0` | 1 |
| `zh-Hant-controlled` | `88892EB73FEE50DBAF53C5ABA656A985479439CE41C53D88EB4A82CDCED15CBF` | `CCBD4BF5D30F2702E96A809EAFE1260890F1F6E6362E4E9A4FBF7AA4071F4CB3` | `6EB305F2AEF3E8E91AB2B7FB3863B1AACD182FFEF6F8E985A61D4228FE235B2B` | `0`, `0` | 1 |

The compiler was XeLaTeX from MiKTeX 26.5, invoked with `-interaction=nonstopmode -halt-on-error -file-line-error`. Each final log has two `LaTeX Font Warning` line matches: Microsoft YaHei's requested italic shape was unavailable and the upright shape was substituted. Mechanical error-pattern matches were zero for Hans; the Hant producer record likewise reports no TeX errors, generic warnings, overfull boxes, or underfull boxes.

## Hant generation custody

The controlled-generic Hant TeX was deterministically generated from Hans SHA-256 `928C90ED8A02FA9F5BAA5E891CE780CCFF76878BB86515D84F7064E8998E6416` with `opencc-python-reimplemented` 0.1.7 and configuration `s2t`. It is not Taiwan-, Hong Kong-, or Macao-localized prose.

- `qa/OPENCC_PRODUCER_RECORD.json`: SHA-256 `6A0DB0691756609FC92D83CF9A148F355D1AA6C14FBE947F4D05D6CB6DEEA613`.
- `qa/HANS_MECHANICAL_BUILD_RECORD.json`: SHA-256 `B5893F118B4ABA899622F44509312CD333CE5F911150AD8ACB72FFF3EA7945ED`.
- `qa/HANT_MECHANICAL_BUILD_RECORD.json`: SHA-256 `B7769360EFFFB820EAA3654F841305F96D3BA371CE23D5B6A1FFCB9EAA882968`.
- `qa/build_hant_producer.py`: SHA-256 `9F5004352261B89DC0E0F9AF6AB3480173761AAD77423C18A4B7C84B4597572E`.

## Producer boundary

No PDF was opened, rendered to images, or visually inspected. No source collation, source-defect hunt, semantic/formula/terminology/translation-quality check, native/regional validation, approval, publication, archive certification, or external/community certification was performed. Successful compilation establishes only that the TeX produced a PDF. Independent checking is pending in other sessions. SGA remains held.
