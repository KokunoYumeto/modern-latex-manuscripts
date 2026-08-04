# Paper 12 segment C — Chinese producer return

## Frozen input

- Work unit: Noether Paper 12, segment C, current-source lines 8318--8471.
- German input: `C:\Users\Floris\Documents\interlanguage\03_projects\language_management\cjk\03_working_translations\noether_paper12_zh_translation_001_20260722\segments\source\P12_C_lines8318_8471.tex`
- German input SHA-256: `5DAB1E227F618B119B9C4358A9DA1005474E040D5CA33877FCBD9BC7A6BCD734`
- German input size at translation time: 7,676 bytes; 154 physical lines as reported by PowerShell.
- Drafting witness made available without comparison or audit: `C:\Users\Floris\Documents\interlanguage\03_projects\language_management\cjk\03_working_translations\noether_paper12_zh_translation_001_20260722\segments\witness\P12_C_witness_lines8191_8286.tex`
- Drafting-witness SHA-256: `32A288F33FF3F6C4D5E1F654D55A98E282C791425ED1A4BDAE9AD4A568773CB3`

## Producer output

- Output: `C:\Users\Floris\Documents\interlanguage\03_projects\language_management\cjk\03_working_translations\noether_paper12_zh_translation_001_20260722\segments\zh-Hans-CN\P12_C_zh-Hans-CN.tex`
- Output SHA-256: `7D2F1043466CCD6CA303D3CC257C02821F418CED70928C0F727C3F49C02D14DF`
- Output size at return time: 6,279 bytes; 119 physical lines as reported by PowerShell.
- Locale posture: PRC-oriented Simplified Chinese (`zh-Hans-CN`) producer wording.

## Producer lexical choices and uncertainties

- `Normalkoordinaten` → “正规坐标”; `Reduktionssatz` → “约化定理”.
- `Extremale` → “极值曲线”; `Grundfunktionen` → “基本函数”; `vollständiges System` → “完备系统”.
- `projektive Invariante` → “射影不变量”; `kovariante Ableitung` → “协变导数”; `kogredient` → “同变”.
- `simultanes System` → “联立系统”.
- `Formen pter Dimension` was rendered as “\(p\) 次形式”. “\(p\) 维形式” remains a possible checker-adjudicated alternative.
- `Clebsch-Gordanschen Reihenentwicklung` was rendered as “克莱布施--戈丹级数展开”; transliteration and dash styling remain checker decisions.
- `Math. Annalen` was rendered as “《数学年刊》”; retaining the German journal title parenthetically remains a possible checker decision.
- Current-source equations, macros, notation, `\srcnumdisplay` wrappers, final `\clearpage`, and footnote-counter reset were carried into the translation without producer adjudication.

## Status boundary

This is a translation-only producer return. I did **not** source-check, collate, audit, compare source and witness, semantically review, formula-check, terminology-check, compile, render, inspect a PDF, regionalize Traditional Chinese, approve, publish, archive, or certify this segment. All checking and adjudication belong to separate sessions.

## Append-only syntax-repair return — 2026-07-22 12:12:08 +02:00

- Trigger: a separate session reported a XeLaTeX pass-1 stop caused by missing inline-math delimiters in this producer segment.
- Historical producer-output SHA-256 remains recorded above as `7D2F1043466CCD6CA303D3CC257C02821F418CED70928C0F727C3F49C02D14DF`.
- Parent-supplied pre-repair segment state, including its first two delimiter repairs, was preserved at SHA-256 `2022CF8A46B94849908793733D7629E9867972DEBC4CB7B197C734C550AEF591`.
- Mechanical action: restored `\(...\)` only around this translation's intended inline mathematical expressions. No prose choice was changed.
- Resulting segment SHA-256: `23A21B0C662BA365ACC0373A5950C38C98577D06FD1059779B4F74B5AFA1DE64`.
- Status boundary: this worker did not compile, render, inspect, source-check, compare/audit, semantically review, formula-check, terminology-check, or adjudicate the repaired segment. The edit is a compile-driven TeX-syntax repair only.
