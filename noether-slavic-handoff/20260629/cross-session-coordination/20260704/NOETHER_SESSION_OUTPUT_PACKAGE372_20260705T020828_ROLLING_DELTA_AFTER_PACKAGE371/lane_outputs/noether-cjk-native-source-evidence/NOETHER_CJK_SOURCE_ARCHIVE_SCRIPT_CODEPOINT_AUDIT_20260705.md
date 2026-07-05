# Noether CJK Source-Archive Script/Codepoint Audit

Generated: 2026-07-05T02:07:10+02:00

Purpose: attach exact script/codepoint evidence to the CJK source-archive frontier rows. This checks representation only; it does not translate, promote terminology, or claim native/public approval.

## Summary

- Source frontier rows audited: 15.
- Input CSV SHA-256: `5E70020686C0C67BB0A968856D750B5AFDB5BC6AE94816234994A0F9498057E8`.

| Target/access | Repository/title | Script decision | Sample codepoints |
| --- | --- | --- | --- |
| Japanese | homuralove/linear-algebra | Japanese script evidence present via kana plus Han/codepoint context. | 線 U+7DDA, 形 U+5F62, 代 U+4EE3, 数 U+6570, ま U+307E, と U+3068, め U+3081 |
| Japanese | HideakiHosaka/2015_linear_algebra | Japanese script evidence present via kana plus Han/codepoint context. | 年 U+5E74, 夏 U+590F, 学 U+5B66, 期 U+671F, の U+306E, 数 U+6570, 理 U+7406, 科 U+79D1, 基 U+57FA, 礎 U+790E |
| Japanese | t-higashida/linear_algebra | Japanese row has Han/CJK evidence but no kana in sampled metadata; retain source row while marking exact Japanese abstract/modern algebra gap separately. | 線 U+7DDA, 形 U+5F62, 代 U+4EE3, 数 U+6570 |
| Japanese | rsato64/relativisticQM | Japanese script evidence present via kana plus Han/codepoint context. | 相 U+76F8, 対 U+5BFE, 論 U+8AD6, 的 U+7684, 量 U+91CF, 子 U+5B50, 力 U+529B, 学 U+5B66, の U+306E, 講 U+8B1B |
| Simplified Chinese | zhcosin/algebra-notes | Han script evidence present; Simplified Chinese assignment rests on repository description/search context and source paths, not codepoint-only distinction. | 代 U+4EE3, 数 U+6570, 学 U+5B66, 笔 U+7B14, 记 U+8BB0, ， U+FF0C, 包 U+5305, 含 U+542B, 线 U+7EBF, 性 U+6027 |
| Simplified Chinese | Kfj2006/Algebra_notes | Han script evidence present; Simplified Chinese assignment rests on repository description/search context and source paths, not codepoint-only distinction. | 代 U+4EE3, 数 U+6570, 学 U+5B66, 讲 U+8BB2, 义 U+4E49, ， U+FF0C, 目 U+76EE, 前 U+524D, 仅 U+4EC5, 有 U+6709 |
| Simplified Chinese | ayhe123/algebra-lecturenote | Han script evidence present; Simplified Chinese assignment rests on repository description/search context and source paths, not codepoint-only distinction. | 柯 U+67EF, 斯 U+65AF, 特 U+7279, 利 U+5229, 金 U+91D1, 《 U+300A, 代 U+4EE3, 数 U+6570, 学 U+5B66, 引 U+5F15 |
| Simplified Chinese | GooduckZ/Linear-Algebra-for-ZJUCKC | Han script evidence present; Simplified Chinese assignment rests on repository description/search context and source paths, not codepoint-only distinction. | 浙 U+6D59, 江 U+6C5F, 大 U+5927, 学 U+5B66, 竺 U+7AFA, 可 U+53EF, 桢 U+6862, 院 U+9662, 荣 U+8363, 誉 U+8A89 |
| Simplified Chinese | yhwu-is/Linear-Algebra-Left-Undone | Han script evidence present; Simplified Chinese assignment rests on repository description/search context and source paths, not codepoint-only distinction. | 线 U+7EBF, 性 U+6027, 代 U+4EE3, 数 U+6570, ： U+FF1A, 未 U+672A, 竟 U+7ADF, 之 U+4E4B, 美 U+7F8E, 讲 U+8BB2 |
| Simplified Chinese | DolveKD/Advanced-Algebra-Notes | Han script evidence present; Simplified Chinese assignment rests on repository description/search context and source paths, not codepoint-only distinction. | 高 U+9AD8, 等 U+7B49, 代 U+4EE3, 数 U+6570, 学 U+5B66, 个 U+4E2A, 人 U+4EBA, 习 U+4E60, 笔 U+7B14, 记 U+8BB0 |
| Simplified Chinese | arshtyi/Advanced-Algebra | Han script evidence present; Simplified Chinese assignment rests on repository description/search context and source paths, not codepoint-only distinction. | 高 U+9AD8, 等 U+7B49, 代 U+4EE3, 数 U+6570, 笔 U+7B14, 记 U+8BB0 |
| Korean addendum/source routing | gshstexsociety/examples | Hangul evidence present; route as Korean addendum/source evidence, not Korean native-edition authority. | 경 U+ACBD, 기 U+AE30, 과 U+ACFC, 학 U+D559, 고 U+ACE0, 생 U+C0DD, 교 U+AD50, 사 U+C0AC, 作 U+4F5C, 텍 U+D14D |
| Korean addendum/source routing | alstn2468/category-theory-for-programmers | Korean-routing row has weak Hangul evidence in sampled metadata; route as adjacent/source lead only. | 🚧 U+1F6A7, 📚 U+1F4DA |
| Korean addendum/source routing | Korean modern/abstract algebra source-level TeX recheck | Explicit Korean source gap row retained; no script witness attached. |  |
| Japanese | Japanese exact abstract/modern algebra source-level TeX recheck | Japanese target row has weak script evidence in sampled metadata; keep as gap/lead only. |  |

## Boundaries

- Simplified Chinese/Japanese distinctions are not inferred from Han codepoints alone; repository language evidence and source paths remain part of the witness record.
- Korean rows remain addendum/source-routing only unless owner lanes provide exact Korean target-language source-canon witnesses.
- This audit does not approve reuse, clear licenses, assert canonical terminology, or merge CJK/Japonic/Koreanic into a pan-CJK bridge.
