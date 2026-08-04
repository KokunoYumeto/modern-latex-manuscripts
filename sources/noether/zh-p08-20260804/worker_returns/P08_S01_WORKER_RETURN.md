# Paper 8 S01 Chinese producer return

- Return ID: `P08-S01-ZH-PRODUCER-RETURN-001`
- Recorded at: `2026-08-04T12:03:26+02:00` (wall-clock precision: one second)
- Work unit: Paper 8, S01, introduction plus section I
- State: **UNCHECKED producer draft**
- Target: PRC-oriented `zh-Hans-CN`

## Pinned inputs and output

- Supplied German source segment: `segments/source/P08_S01_INTRO_I_source_LF.tex`
  - 5,921 bytes
  - SHA-256 `2FFAD37FC535DBCAC04D8A6D41A8E7397A44FFD151FB5920A2DAC9E5CCF5F161`
- Inherited Simplified-Chinese witness: `segments/witness/P08_S01_INTRO_I_inherited_Hans_LF.tex`
  - 5,276 bytes
  - SHA-256 `05EE2E841E51706C8F3B09234E6F7F03707F905CE7313335BEC5BA08D8BA2421`
- Produced target: `segments/zh-Hans-CN/P08_S01_INTRO_I_zh-Hans-CN_v001.tex`
  - 5,304 bytes
  - SHA-256 `271BDC09B73C7A66798D5B17CB559D7592D9CA94C6A7D2E35716269715074EDB`
  - UTF-8, LF-only, terminal LF present

The inherited Chinese file was used only as translation evidence. The supplied source segment contains a second centered title/author block absent from that witness; the target restores that supplied structure. No German-source defect is asserted.

## Producer decisions

- `Reihe(n)` is rendered `变量组`, not bare `行`, in the sense “a group of the variables indexed by one (A_k).” This avoids the spreadsheet/matrix-row attractor while keeping the index structure explicit.
- `Form` / `Grundform` is rendered `形式` / `基本形式`, following the inherited Chinese shelf and article title. A sibling segment proposed the alternative `型`; this is an assembly-time consistency question, not a settled independent validation.
- `ganze rationale Darstellung` and related phrases are rendered `整有理表示`; the sense window is polynomial expression in the stated invariants, not an arbitrary rational-fraction expression.
- `rationalen Zahlkoeffizienten` and `rationalzahlig` are rendered `有理数系数`. The inherited witness’s `有理整数系数` was rejected because it can falsely attract the integer-coefficient sense.
- `Polar`, `Polarprozeß`, and `Polaroperation` are distinguished as `极化式`, `极化过程`, and `极化运算` where their grammatical roles differ.
- `volle(s) Invariantensystem` is rendered `完全不变量系统` / `完全系统`; `Simultaninvariante` is rendered `同时不变量`.
- `Reihenentwicklung` is rendered `级数展开` in its historical invariant-theoretic sense; this wording does not by itself assert analytic convergence.
- The supplied source-note macros remain `\NoetherSrcNote{*)}{...}`. Bibliographic titles are retained in their original languages while connective prose is translated.

## Mechanical producer evidence

- Inline-math sequence: 59 source spans / 59 target spans, byte-exact and order-exact.
- Display/equation sequence: 8 source spans / 8 target spans, byte-exact and order-exact.
- Environment openings/closings: 3/3 in each file.
- Equation tags: 1 in each file.
- `\NoetherSrcNote{*)}` occurrences: 2 in each file.

These are mechanical preservation checks only. They are not semantic checking, independent checking, source adjudication, or approval.

## Uncertainty and adverse evidence

- `Rationalitätsbereich` is provisionally rendered `有理域`. An independent Chinese checker may prefer a more historically specific `有理性域`; no claim of settled terminology is made.
- `autographierten` in the Capelli bibliography is provisionally rendered `摹写印行的`; the exact historical production medium remains a bibliographic nuance for independent review.
- The `形式` versus `型` choice must be normalized once the producer assembles all Paper 8 segments; this return records the competing attractor instead of hiding it.
- No PRC native review, terminology review, source review, formula review, or independent Chinese check has occurred.

## Explicit exclusions

No source/scan adjudication, German patching, Hant conversion, compilation, PDF build, rendering, visual QA, package assembly, certification, approval, SGA work, or work outside S01 was performed.

