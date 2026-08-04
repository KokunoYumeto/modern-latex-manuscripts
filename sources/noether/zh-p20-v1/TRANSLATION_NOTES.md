# Noether Paper 20 Chinese producer translation notes

## Scope and boundary

Work unit: complete Noether Paper 20, “Ein algebraisches Kriterium für absolute Irreduzibilität”.

Controlling user boundary:

> you do not check - you translate - other sessions CHEWCK

This workspace records PRC-oriented Simplified-Chinese translation production, controlled-generic Traditional-script transport, and mechanical compilation only. No source/witness comparison, source check, semantic or formula-content check, terminology adjudication, translation-quality review, PDF opening or rendering, Taiwan/Hong Kong/Macao localization, approval, publication, archive action, external or human validation, or certification was performed. All independent checks remain pending.

## Source custody

- Current German authority whole SHA-256: 443EF950D7D45DC6D9E44A9B87501620C10DA873E50E5F2B253ECCAE6A946D27.
- Paper 20 exact source cursor: lines 12377--12588, raw UTF-8 bytes [980360,1001524), 21,164 bytes.
- Exact source snapshot: source\P20_CurrentGerman_lines12377_12588.tex; SHA-256 CBC9E9CF34E6475F4256C935A58378FCDBF85A09ACC0E592FC64F3FCFDF8744D.
- Exact inherited Hans drafting-witness cursor: lines 13142--13378, raw UTF-8 bytes [896162,914175), 18,013 bytes.
- Inherited Hans snapshot: witness\P20_InheritedHans_content_lines13142_13378.tex; SHA-256 B7DA9DBB83BC2B9793263987F14D7E67C91324EE83FEA26FBCDC82979FE5F97C.
- Witness role: drafting witness only; it was not compared with or audited against the German source.
- The stale shared R821 pointer was not used.
- Durable producer claim: ZH-D104.

## Segment production

| Segment | Exact German source | German SHA-256 | Current Hans output SHA-256 | Current worker-return SHA-256 |
|---|---|---|---|---|
| A | lines 12377--12437; 8,182 bytes | DFD92DE298F422E2D993CC3162E3B031D41E4ECB67E32CB967FE0A1FD6CF237E | DC694B77A78B1D12E12BC5A3DA315147538847F23F0E46772D85A7BAE9181834 | 94E5A487D08A67BD692D4BC283F1C8770231D5A96F6553B8FEECD43658AD0662 |
| B | lines 12438--12519; 6,929 bytes | 25D5BCDA8B4A35D789A8A33D256BC08FB779E057567A1673761FD7D7F97AD81E | 143C7386FCB9DDA7159C2F7D9A2C9547530D9AED786648A85ACD488D14A8A491 | 4E924E588A08B14806DC5D3812D852DEAA67F23F2E8A516A1FFB7D30C9FB1816 |
| C | lines 12520--12588; 6,053 bytes | D7B2FC4C6FB95125109A83F5F856F27B319FE25F4ABF13B3AAE6D33A99D5C2C1 | 8972FC4AA515FF93047D0F686DFD9CCB4003287E2F815313F02BAC079ED9D734 | E0C5631F520867B2BB37E78E8593453091447573AC5ECECE96A60EAE615D8520 |

## Append-only compile-driven delimiter history

Segment A was first returned at SHA-256 B637B38DBD55BCF8BA6862F000B48D9108FC77F8D42D083762A5AE97081559FC. Three successive pass-1 invocations stopped with no pages at three separate literals (n\ge2). Restoring only their inline-math delimiters produced, in order, SHA-256 51BDBA85125DC72494746B49540FD6EF5DE21D7DD2854F86558B726E06586B3F, F4317188496FE61F220343C1C941E7D6F7EF02707F463D3FA208203963BD1AC6, and 80AA4F63166554C74EB29806CF1DCE77A6C98F1DB31EC181FD1BF9A372CCC4DC. The next pass-1 invocation produced one page and then stopped at malformed (F(x,y)\). Restoring only that delimiter produced current A SHA-256 DC694B77A78B1D12E12BC5A3DA315147538847F23F0E46772D85A7BAE9181834.

These changes restored TeX delimiters only; no prose was changed. Compiler stops are mechanical triggers, not source, semantic, formula-content, terminology, translation-quality, or visual checks.

## Producer lexical uncertainty shelf

Worker returns retain unresolved producer alternatives, including:

- absolut irreduzibel → 绝对不可约.
- Reduzibilitätsform → 可约性形式; alternatives 可约形式 / 可约判别形式.
- Koeffizientenbereich → 系数域; alternative 系数范围.
- Primideal → 素理想; Basispolynome → 基多项式 / 基底多项式.
- irreduzibles algebraisches Gebilde → 不可约代数构形; alternative 不可约代数簇.
- Kroneckersche Substitution → Kronecker 代换; possible later 克罗内克代换.
- ein-eindeutig → 一一对应; alternative 双射.
- induzierte Exponenten → 诱导指数; Lücken → 空缺 / 缺项.
- ganze ganzzahlige Funktion → 整系数整函数; alternative 整系数多项式.
- Wertsystem → 值组; alternatives 数值组 / 特化值系 according to context.
- Gradzahlen / Grad / Graderniedrigung → 次数 / 次数降低; alternatives 度数 / 降次.
- Erweiterungskörper → 扩张域; zerfallen → 分解, with 分裂 held as an alternative where field extension is foregrounded.
- Ostrowski was rendered 奥斯特罗夫斯基 in segment C while other proper names remain largely Latin; name-standard adjudication is pending.
- algebraisch gebrochene Zahlen → 代数分数; its historical scope remains pending.

These are producer choices and uncertainties, not terminology decisions or recommendations.

## Current targets

- Assembled zh-Hans-CN TeX: 20,245 bytes; SHA-256 262430D0A092818F859516F3FD5DE612D897D0BD8AAC49605BE047E389963065.
- Controlled-generic zh-Hant TeX: 20,587 bytes; SHA-256 17EE7ECD25A298D8818144CE41273A31DEB85F3E49A02F08D5335B6815FF20C0.
- Hans assembly record SHA-256: 39A4D15DEBEC4E45D3032B9554A6D83B552957031074264ECC5D3DB66A673B2D.
- OpenCC producer record SHA-256: 80A7FC6B1D859A63CC4BC602CC289860098EA317BE158D32D3BEE048CD541B76.

The Hant target is controlled generic Traditional script only. Its lexical base is the Hans producer translation. It is explicitly not zh-Hant-TW, zh-Hant-HK, or zh-Hant-MO prose.

