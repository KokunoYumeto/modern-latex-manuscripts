# Noether Paper 38 — Chinese producer translation notes

## Scope

Complete Paper 38 was translated from the exact current German interval at lines 18750–18970, SHA-256 `ECEC3909998D3E1BD891597D2494C5A13E7E719F1B2A6CAF802515F8EEB492AC`. The inherited Simplified-Chinese interval, SHA-256 `EE420CD898E71EDE96ABADE3448ECF3CDE78ABF27A81D8381422F253FDC43E3E`, was used only as a drafting witness. Previously recorded source-apparatus/footnote-restoration history was not adjudicated; the producer followed the routed current bytes.

Three non-overlapping translated segments were assembled in order. Final PRC-oriented Hans TeX SHA-256 is `330053BA55A857F1BA7CE43D6D8F97DE97EC3B1E350D59C21FD2F74702E8E973`. The controlled-generic Hant derivative was mechanically generated with OpenCC `s2t` plus recorded normalizations; its TeX SHA-256 is `3FD73D3BCBFDCC2B2C1C83C473092E20E60AEF633ABD85716C910DE448F1FAC8`.

## Producer lexical choices

Recorded choices include `正规除代数`, `循环`, `Dickson 型`, `处处分裂代数`, `正规单代数`, Brauer-class `相似性`, `p-进扩张`, `p-次数`, `p-指标`, `可解分裂域`, `Sylow 域`, `因子系`, `Hasse 范数定理`, `范数剩余符号`, `指数` for Exponent versus `指标` for Index, `基本理想`, `（约化）不同`, `素位`, `未分歧域`, `复合域`, `分歧指数`, `R. Brauer 的群`, `分解定理`, `唯一性与序定理`, `圆分域`, and `半单代数`.

These are producer editorial choices, not validated terminology. The 27-row terminology/adverse/CJKV ledgers record a sense window, excluded attractors, alternatives, a provisional lexical-attractor basin, and qualitative Mandarin-Simplified dominance debt for each term. Japanese and Korean evidence were not consulted and do not authorize Chinese choices.

## Adverse production evidence for another session

- `Exponent` and `Index` are deliberately separated as `指数` and `指标`; Chinese algebra shelves vary and this requires independent review.
- The assembled target uses `分歧指数` in theorem 3 and later `分歧阶` in theorem 6. This variation is left explicit for a checker rather than silently harmonized.
- `正规单代数` competes with modern `中心单代数`; `正规除代数` carries the same historical/modern tension.
- `相似性` is Brauer similarity, not ordinary matrix conjugacy.
- `处处分裂` quantifies over prime places and completions; `素位` must remain distinct from `素理想` and `素因子`.
- `基本理想` and `（约化）不同` are historically trap-prone; the source itself includes a terminology warning.
- `圆分域` competes with `分圆域` and other regional forms.
- Controlled Hant is generic script conversion of PRC-oriented prose, explicitly not Taiwan-, Hong Kong-, or Macao-localized language.

## Mechanical syntax repair

The first Hans compile failed because segment A had transported the source title line break `\\[0.5em]` as `\[0.5em]`, opening display math. Only that TeX escape was repaired. Initial and repaired hashes and the compiler error are recorded in `qa/PRODUCER_TEX_SYNTAX_REPAIR_RECORD.md`, SHA-256 `F0BD0335EE18A8FA8CBC4653C140F0F3863306482119B695BD8D5452863D14D2`. No Chinese wording, formula, source byte, citation, or label changed.

## Role boundary

Floris's controlling instruction is: `you do not check - you translate - other sessions CHEWCK`.

This package records translation and mechanical compilation only. It does not claim source/apparatus collation, source correctness, semantic/formula/terminology correctness, native-reader review, visual QA, regional localization, approval, publication, or certification. If an independent checker identifies a precise possible Noether-source defect, it must deduplicate it and ensure that `4 -nterslav` sees it; this producer made and adjudicated no source-defect claim.

SGA remains held pending explicit Floris confirmation.
