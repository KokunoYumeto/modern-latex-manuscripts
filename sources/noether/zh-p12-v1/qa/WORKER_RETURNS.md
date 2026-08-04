# Paper 12 Chinese producer worker-return manifest

Snapshot: 2026-07-22 12:16:30 +02:00.

Controlling user boundary:

> you do not check - you translate - other sessions CHEWCK

All three segment workers returned translation production only. This manifest records file custody and producer uncertainties; it does not review, reconcile, or validate their translations.

## Return custody

| Segment | Worker return | Return bytes | Return SHA-256 | Current output | Current output SHA-256 |
|---|---|---:|---|---|---|
| A | worker_returns\P12_A_TRANSLATOR_RETURN.md | 1,587 | D40AAAAF16CFE8F289FDAA3F938CB4B348D1B8F61E1B7494147726356EEB1207 | segments\zh-Hans-CN\P12_A_zh-Hans-CN.tex | 65CB2373945FCC6973010CD29729E354DF892A4C4CDFC4E215D2E44755CDAF01 |
| B | worker_returns\P12_B_TRANSLATOR_RETURN.md | 2,649 | F61D88A1A95B9B2556D2B92C0FCCA0483EEEA2CCEF8E05F843834807BBF5E2EB | segments\zh-Hans-CN\P12_B_zh-Hans-CN.tex | D8FEB6D63E9D837228503846D8B653954A36BFDC43443DC3CA4B379493502563 |
| C | worker_returns\P12_C_TRANSLATOR_RETURN.md | 3,787 | 0EEDDFF35D391E49D3E51CCD2887DB7D2D65A60AC7A7532C3C1BA19C95F48C00 | segments\zh-Hans-CN\P12_C_zh-Hans-CN.tex | 23A21B0C662BA365ACC0373A5950C38C98577D06FD1059779B4F74B5AFA1DE64 |

## Input custody recorded by returns

| Segment | Source cursor | Source SHA-256 | Drafting-witness SHA-256 |
|---|---|---|---|
| A | German lines 8071--8172 | FA2A7821AAC02EAAFF3322FB88EB3DA9937DF086619B20A52FFD307384E378BE | FF46FE9CE1D521CA1FB86F5C391F66DBF29DDE5E6D1046C24389B6F79D2D880A |
| B | German lines 8173--8317 | DBE25989E0F304058E79F33D28AAA0028856D58AF7E5F8F74469FE88DFF7C646 | 5B3D56A701C397FA720EB3D41206104AC016840086C43176B757F5161CC07B48 |
| C | German lines 8318--8471 | 5DAB1E227F618B119B9C4358A9DA1005474E040D5CA33877FCBD9BC7A6BCD734 | 32A288F33FF3F6C4D5E1F654D55A98E282C791425ED1A4BDAE9AD4A568773CB3 |

The inherited Chinese files were drafting witnesses only. No worker comparison or audit is claimed.

## Segment C append-only repair return

The C return preserves the translation-time output SHA-256 7D2F1043466CCD6CA303D3CC257C02821F418CED70928C0F727C3F49C02D14DF. After compile failure, the parent restored only two intended inline-math delimiters, producing SHA-256 2022CF8A46B94849908793733D7629E9867972DEBC4CB7B197C734C550AEF591. The translator then mechanically restored the remaining intended inline delimiters without changing prose, producing the current SHA-256 23A21B0C662BA365ACC0373A5950C38C98577D06FD1059779B4F74B5AFA1DE64.

This history is a TeX-syntax repair record. It is not formula adjudication, semantic review, or translation checking.

## Producer-only lexical uncertainty shelf

The returns expose alternatives for later independent adjudication, including:

- 微分表达式 / 微分式
- 约化定理 / 归约定理
- 联立系统 / 同时系统
- 正规坐标 / 法坐标
- 极值曲线 / 极值线
- 极化式 / 极式
- 基本函数 / 基础函数
- 同变 / 协同变换
- 正规形式 / 标准形
- \(p\) 次形式 / \(p\) 维形式
- Chinese transliteration and dash styling for Clebsch--Gordan
- whether to translate or retain Math. Annalen
- whether to retain Latin personal names or adopt a later name standard

These are worker-reported producer alternatives, not recommendations or resolved terminology.

## Explicit no-check status

This manifest performs no source/witness comparison, source check, semantic or formula-content check, terminology adjudication, translation-quality review, PDF opening/rendering, Hant regional localization, approval, archive/publication action, external or human validation, or certification. Separate sessions must check the work.

