# Noether Paper 7 — Chinese producer mechanical build report

## Targets

| Target | TeX SHA-256 | PDF SHA-256 | Final log SHA-256 | Pass exits | Pages reported by log |
|---|---|---|---|---|---:|
| `zh-Hans-CN` | `B121BC5D5649F63904444A25179FB4D882F55EF9435A5C81C1689414639BE8F4` | `EDFD8832E5EE780723B95B3643EB1DACCED22317C052214AE39F4F575E46D4C7` | `C23A69005813BD447B42ABC57A5EF41FEF6CA842467836537A3A7D5F28C03E2D` | `0`, `0` | 3 |
| `zh-Hant-controlled` | `36648843726340B02C9B7FF31EEC28008AC3CD66594F469F7769540E29DEFC79` | `A238D9E25FBC44D8D4506D63C66E0CE576F1157F753292B741A3BA9CFA401159` | `DE6DE61142697728DB6E40B421B975AB53FF82CF6E361E7A250CBE7478DCD1B0` | `0`, `0` | 3 |

XeLaTeX from MiKTeX 26.5 was invoked with `-interaction=nonstopmode -halt-on-error -file-line-error`. Hans final-log mechanical error-pattern matches were zero. Each Hans/Hant final log has two `LaTeX Font Warning` line matches for an unavailable italic Microsoft YaHei shape and upright substitution. The Hant build record reports zero overfull, underfull, and missing-character matches.

## Assembly and Hant custody

- Hans assembly record: SHA-256 `69AC60F1D41297BE2CB7FD625F9D971ED8AD7ACD0061B1FDB977E4BD5711AB8E`.
- Hans mechanical build record: SHA-256 `96C2A1E5AAC3A283AA7FEB09FF05D1B9D9343C4D3D3676487D2D53613581BB8C`.
- OpenCC producer script/record: SHA-256 `77F518BCB25B6685026546D8EEE927300283E45D3EB129D450FEAC804D354820` / `CEA04C7FDD18C70E9CE31990610243441317CEB454AF041071B42A3C8CB9049A`.
- Hant build record: SHA-256 `BCF4F5EBFF57542503BA55713368CCEEC06649FD4197CCACC566DBE54FF349E1`.
- Controlled Hant uses OpenCC `s2t` 0.1.7 and is bound to Hans SHA-256 `B121BC5D5649F63904444A25179FB4D882F55EF9435A5C81C1689414639BE8F4`.

## Producer boundary

No PDF was opened, rendered to images, or visually inspected. No source collation, source-defect hunt, semantic/formula/terminology/translation-quality check, native/regional validation, approval, publication, archive certification, or external/community certification was performed. Compilation establishes only that the supplied TeX produced PDFs. Independent checking remains pending; SGA remains held.
