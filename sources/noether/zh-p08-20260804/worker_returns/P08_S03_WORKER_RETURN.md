# Noether Paper 8 — Chinese producer return, S03 (III)

- Return ID: `NOETH-P08-ZH-S03-WORKER-RETURN-001`
- Recorded at: `2026-08-04T12:08:02+02:00` (second precision; Europe/Berlin)
- Work unit: complete bounded segment `P08_S03_III`
- Role: translation-only producer
- State: **UNCHECKED PRODUCER DRAFT — NOT ACCEPTED, NOT FINAL**

## Exact custody

- German source segment: `segments/source/P08_S03_III_source_LF.tex`
  - 7,112 bytes; 114 physical lines
  - SHA-256 `9DE743A4238F62E16002032BCFBE2F20A4EC12005959B2BE5393D0122AA219FA`
- Inherited Simplified-Chinese witness: `segments/witness/P08_S03_III_inherited_Hans_LF.tex`
  - 6,790 bytes; 127 physical lines
  - SHA-256 `4D068CEE4723111487E80B135D9826BC0CAE6A08A9655FE045E95E2D1B743124`
  - Used only as translation evidence; it is not an authority and was not treated as checked text.
- New PRC-oriented Simplified-Chinese producer segment: `segments/zh-Hans-CN/P08_S03_III_zh-Hans-CN_v001.tex`
  - 6,720 bytes; 114 physical lines
  - SHA-256 `BADC55B6C32EE8F7C7DC69595A4FF124F79920A25517FB3A440BF678DA0F3BC8`

The target covers the complete source segment from `\subsection*{III.}` through the Erlangen date line. The source and target each contain 106 mechanically delimited math spans. Their TeX-command multisets are equal; the only math-span byte differences after whitespace removal are the translated prose inside `\text{...}` in the four-row determinant display and equation (5). This is producer copy accounting only, not formula checking or independent validation.

## Translation choices and sense windows

- `Reihe(n)` is `变量组`. Here it denotes each ordered group/set of variables or quantities used as one determinant row, not an infinite sequence and not `Reihenentwicklung`. Rejected alternatives: bare `行` (too easily read as only a displayed matrix row), `系列` (collides with the development/series sense), and `变量列` (suggests a column). Provisional attractor basin: modern Sino-xenic coinage/calque; regional/native status remains unvalidated.
- `Reihenentwicklung` is `级数展开`. In this section it is the finite invariant-theoretic algebraic development displayed in (3)--(5), not an analytic convergence claim or necessarily an infinite power series. Rejected alternatives: `行展开` (wrongly ties the term to matrix rows), `序列展开` (too literal and nonstandard here), and generic `展开` (loses the historical technical term). Provisional attractor basin: modern Sino-xenic coinage/calque. Adverse evidence: `级数` can attract the modern analytic-series reading, so an independent historical-mathematical checker should revisit it.
- `Form` is harmonized as `形式`, not `型`, following the whole-P08 producer decision. The first `lineare Formenscharen` reference is `形式的线性族`, thereafter `线性族`, so it cannot be misread as “a family of linear forms.” `型` remains a viable rejected alternative pending independent checking. Basin: mixed/contested.
- `Polare`, `Polarisation`, and established `Polarprozeß` senses remain `极化形式`, `极化`, and `极化过程`; the source’s shortened `Prozesse P` is rendered `过程 P` without inventing a new operation. Basin: modern Sino-xenic coinage/calque.
- Congruence is explicitly `模 $\Delta$ 的同余式`, and the source relation symbols `\equiv` are retained. `=` was not allowed to attract the congruence sense. `Determinante` is `行列式`. Basins: modern Sino-xenic mathematical coinage/calque.
- `\Omega` and `\nabla` remain distinct source operators/process notations. The target calls only the source-named `\Omega` operation an `\Omega` process and does not replace either notation with a lexical synonym. Symbolic notation is not lexical evidence.
- `kogredient` is provisionally `同变`, with the sense window “the variables transform cogrediently under the same transformation behavior.” It is not asserted to be tensor-index covariance, an ordinary same-direction relation, or identical with every use of `协变`. Alternatives `协变` and `等变` are held for an independent Chinese mathematical checker. Basin: modern Sino-xenic calque / mixed and contested.
- `Multiplikator` is provisionally `乘子`; the local sense is the factor multiplying `\Delta` in the iterative decomposition, not a general scalar multiplier claim. Alternative `乘因子` remains available. Basin: Sino-xenic inherited lexeme with a modern mathematical sense.

## Witness divergences resolved in the producer draft

These are divergences of the inherited Chinese witness from the pinned source segment, not German-source findings:

1. In equation (2), the witness has `Z=\sum PH \pmod{\Delta}`; the source and new target retain `Z\equiv\sum PH \pmod{\Delta}`.
2. In the subsequent `f` display, the witness again substitutes `=` for the source `\equiv`; the new target retains `\equiv`.
3. In lemma c), the witness replaces the source differential equation with a shorter different display, omitting the second differential term. The new target preserves the complete source display.
4. The witness compresses and relocates source note `*)`, dropping most of its displayed operator formula. The new target preserves `\srcfnmark{*)}`, `\srcfntext{*)}{...}`, and the complete formula in source order.
5. The witness changes several source formula argument spellings and punctuation placements; the new target follows the pinned source TeX rather than the witness.

## Uncertainty and adverse evidence

- No Chinese native-speaker, historical-invariant-theory, terminology, formula, source, or regional review has occurred.
- `级数展开`, `同变`, `变量组`, `形式的线性族`, and `乘子` are the highest-priority lexical review points.
- The Chinese word order in the subscript of equation (5) is constrained by preserving the source symbol order `A_1\cdots A_N`; the resulting `\text{由变量组构成的行列式 }A_1\cdots A_N` should receive a readability check without moving or changing the symbols.
- The lemma-c argument and its differential identities were translated and copied as given. No mathematical correctness inference, source adjudication, or German defect claim was made.
- The output is PRC-oriented `zh-Hans-CN` only. No `zh-Hans-SG`, controlled `zh-Hant`, Taiwan, Hong Kong, or Macao localization is supplied or implied.
- Mandarin-Simplified dominance debt is explicit: the evidence and producer wording are PRC-oriented, and cannot authorize Singapore Simplified Chinese or any Traditional-Chinese regional standard.

## Explicit non-actions and next cursor

No scan/OCR/VLM inspection, German comparison or adjudication, source checking, independent Chinese checking, Hant generation, compilation, PDF production, rendering, visual inspection, assembly, manifesting, publication, certification, or SGA work occurred. No German defect packet is warranted from this producer return.

Next cursor: parent producer may assemble this exact hash with the other P08 segments, generate the separately controlled Hant derivative, build and freeze the complete producer package, and route it to the persistent independent Chinese checker. Any correction to this segment must supersede this return explicitly and refresh the target hash; it must not silently rewrite this record.
