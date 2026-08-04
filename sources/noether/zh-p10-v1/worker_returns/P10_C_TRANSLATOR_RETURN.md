# Paper 10 segment C — Chinese producer return

## Scope and producer boundary

- Work unit: Noether Paper 10, segment C, German authority cursor `lines 7768–7864`.
- Target: PRC-oriented Simplified Chinese (`zh-Hans-CN`) TeX.
- Controlling user boundary: `you do not check - you translate - other sessions CHEWCK`.
- Activity completed here: translation production only.
- Not performed here: source comparison, semantic audit, formula audit, terminology approval, compilation, PDF rendering or inspection, Traditional Chinese conversion/localization, certification, archive handoff, or SGA work.
- Timestamp: `2026-07-22T13:23:06+02:00` (Europe/Berlin; second precision for this return capture; individual lexical choices were made during the immediately preceding bounded translation interval and do not have separate timestamps).

## Custody and hashes

| Role | Exact artifact | Bytes | SHA-256 | Evidence class |
|---|---|---:|---|---|
| German translation authority | `C:\Users\Floris\Documents\interlanguage\03_projects\language_management\cjk\03_working_translations\noether_paper10_zh_translation_001_20260722\segments\source\P10_C_lines7768_7864.tex` | 8,493 | `E68CF6495A6E69661F55595D1FEE7487ED19B0182AC395AEC48667B235168C0B` | Source fact supplied by assignment; hash recomputed locally for custody only |
| Inherited Chinese drafting witness | `C:\Users\Floris\Documents\interlanguage\03_projects\language_management\cjk\03_working_translations\noether_paper10_zh_translation_001_20260722\segments\witness\P10_C_witness_lines7598_7714.tex` | 7,602 | `F32417AF6DC8719B732536C60EC9207F2D821B7ABE7FC56F09250CAD314163C6` | Witness/locator only; not treated as authority |
| Produced PRC Simplified Chinese TeX | `C:\Users\Floris\Documents\interlanguage\03_projects\language_management\cjk\03_working_translations\noether_paper10_zh_translation_001_20260722\segments\zh-Hans-CN\P10_C_zh-Hans-CN.tex` | 7,559 | `67D93BFFA16419E4A3E444C4AB9238B7E2A59E910889710A5BC36D93AA85F686` | Computation over the producer output |

The witness supplied drafting cues only. The producer retained the German segment's TeX environments, displayed mathematics, control sequences, and two `\srcfn` source-note positions while translating its prose and note text. This is a producer-action statement, not an independent validation result.

## Producer choices and sense windows

These are editorial translation inferences/model preferences pending independent checker review. Lexical-attractor basin labels are provisional qualitative records, not readiness scores.

### P10-C-ZH-P001 — `extrem unstetig`

- Choice: `极端不连续` / `极端不连续的`.
- Sense window: the source immediately defines the property as arbitrary local approximation of any prescribed output value near every real or complex input; it is stronger than ordinary pointwise discontinuity.
- Alternatives rejected: `处处不连续` (too weak and denotes a different property); `完全不连续` (ambiguous and less transparently tied to the source's definition); `极度不连续` (possible prose, but weaker as a repeatable technical label).
- Motivation: preserve the source's superlative force and maintain a stable repeated label.
- Adverse evidence/uncertainty: the phrase is intelligible but not asserted here as a community-standard Chinese term.
- Provisional lexical-attractor basin: modern Sino-xenic coinage/calque.
- Mandarin-Simplified dominance debt: medium; a checker must not project this Hans choice onto Traditional Chinese regional prose.

### P10-C-ZH-P002 — `Unstetigkeitswerte`

- Choice: `不连续性值`.
- Sense window: output values locally approachable by `\varphi(z)` in the neighborhood under discussion, not input points at which a function is discontinuous.
- Alternatives rejected: `不连续值` (more compact but can be read without the needed “value associated with the discontinuity behavior” relation); `聚值` or `极限值` (would import a stronger modern limit/cluster-value analysis not stated by this lexical item alone).
- Motivation: keep `值` explicit while preventing confusion with `不连续点`.
- Adverse evidence/uncertainty: this is a transparent producer coinage; checker adjudication is required.
- Provisional lexical-attractor basin: modern Sino-xenic coinage/calque.
- Mandarin-Simplified dominance debt: high because regional mathematical traditions may prefer a different lexicalization.

### P10-C-ZH-P003 — `Rang vier/drei/zwei/eins`

- Choice: `秩为四/三/二/一` and, in theorem prose, `秩四/秩二`.
- Sense window: the source defines the rank by the number of linearly independent relations among `x,y,X,Y`: no relation gives rank four; one gives rank three; two give rank two; three give rank one.
- Alternatives rejected: witness-like `四秩/三秩` (unidiomatic in current PRC mathematical prose); `四阶/三阶` (risks confusion with order or degree).
- Motivation: use the conventional Chinese mathematical noun while leaving the source's own defining convention explicit.
- Adverse evidence/uncertainty: the inverse relation-count convention is unusual enough that the definition must carry the meaning; the producer has not independently audited it.
- Provisional lexical-attractor basin: modern Sino-xenic coinage/calque.
- Mandarin-Simplified dominance debt: low-to-medium.

### P10-C-ZH-P004 — `lineare Mannigfaltigkeit`

- Choice: `线性流形`.
- Sense window: the historical text describes a one- or two-dimensional linear family of attainable values determined by linear relations; the term is not silently narrowed to a modern algebraic variety.
- Alternatives rejected: `线性簇` (could suggest an algebraic variety); `线性多样体` (not the preferred PRC-oriented form for this output); `线性空间` (would erase the source term and may overstate passage through the origin).
- Motivation: retain the historical mathematical noun with a familiar PRC rendering.
- Adverse evidence/uncertainty: whether the local geometry is better described today as affine rather than linear is checker territory; the translation retains the source's adjective.
- Provisional lexical-attractor basin: modern Sino-xenic coinage/calque.
- Mandarin-Simplified dominance debt: high for any later Hant regionalization.

### P10-C-ZH-P005 — `Körper`, `Gebiet`, and `Wertsystem`

- Choice: mathematical `Körper` → `域`; `im Gebiet der ... Zahlen` → `在……域内`; `komplexe Wertsysteme` → `复数值系统`.
- Sense window: `Körper` denotes the algebraic field in the opening sentence; `Gebiet` denotes the real/complex numerical setting rather than a geometric subdomain; `Wertsystem` remains a system of complex values.
- Alternatives rejected: `体` for `Körper` (not PRC-oriented usage here); mechanically translating every `Gebiet` as `区域` (misleading in these sentences); reducing `Wertsystem` to a single `值` (loses plurality/system force).
- Motivation: distinguish the algebraic object from the broader numerical setting while keeping the source's wording visible.
- Adverse evidence/uncertainty: the opening phrase involving `\Cfield` and “all real and complex numbers” was translated as given and not adjudicated here.
- Provisional lexical-attractor basin: mixed/contested.
- Mandarin-Simplified dominance debt: high, especially for `域` versus other regional conventions.

### P10-C-ZH-P006 — `lineare Basis` and `Basiszahlen`

- Choice: `线性基`; in the source note, `Basiszahlen` → `基中元素`.
- Sense window: a Hamel-type basis over the rationals, as specified by rational linear representability and finite rational linear independence in the note.
- Alternatives rejected: bare `基数` for `Basiszahlen` because contemporary Chinese may read it as “cardinal number”; `基底数` as needlessly artificial.
- Motivation: preserve the basis concept without introducing the cardinality homonym.
- Adverse evidence/uncertainty: `基中元素` is an explanatory rendering rather than a one-word lexical match.
- Provisional lexical-attractor basin: modern Sino-xenic coinage/calque.
- Mandarin-Simplified dominance debt: medium.

### P10-C-ZH-P007 — mapping language

- Choice: `gehen ... in sich über` → `映为自身` / `对应于自身`; `es entspricht ...` → `所对应的`.
- Sense window: these phrases describe the action of `f` on real values, not mere equality detached from the mapping.
- Alternatives rejected: `保持不变` alone (would suppress the explicit mapping relation); literal `转入自身` (opaque in Chinese).
- Motivation: make the function-action sense explicit.
- Adverse evidence/uncertainty: none beyond ordinary stylistic variation.
- Provisional lexical-attractor basin: native coinage.
- Mandarin-Simplified dominance debt: low.

### P10-C-ZH-P008 — `der Faktor von f(x)`

- Choice: `乘在 \(f(x)\) 上的因子`.
- Sense window: the referent is the multiplier `1+i f(c)` in the preceding displayed identity, not `f(x)` itself as a factor.
- Alternatives rejected: `\(f(x)\) 的因子` (syntactically compact but referentially ambiguous); `系数` (could suggest a scalar coefficient in a different formal sense).
- Motivation: keep the local referent readable without changing the displayed equation.
- Adverse evidence/uncertainty: this is an editorial disambiguation from immediate syntax, not an externally validated interpretation.
- Provisional lexical-attractor basin: native coinage.
- Mandarin-Simplified dominance debt: low.

### P10-C-ZH-P009 — citation shorthand and quoted qualifiers

- Choice: `a. a. O.` → `前引文献中`; `Im allgemeinen` → `一般而言`; `nichtmeßbare` → `不可测`.
- Sense window: the first points back to a previously cited location; the latter two preserve the source's marked qualification/term through `\qtext`.
- Alternatives rejected: unexplained retention of the German abbreviation; `同上` (too mechanically local and potentially unstable after assembly); `非可测` (less idiomatic in PRC mathematical prose).
- Motivation: produce readable Chinese while retaining the source's quotation macro where present.
- Adverse evidence/uncertainty: exact bibliography linkage remains for a checker/assembler.
- Provisional lexical-attractor basin: mixed/contested.
- Mandarin-Simplified dominance debt: medium.

## Adverse-term queue for the independent checker

The following are translation-risk flags, not findings of source error and not completed checks:

1. `Unstetigkeitswerte` → `不连续性值`: verify the historical mathematical sense and preferred corpus term.
2. `lineare Mannigfaltigkeit` → `线性流形`: verify whether the historical usage warrants a different Chinese phrase while retaining “linear.”
3. `Rang`: preserve the source-defined relation-count convention; do not silently normalize it.
4. `Basiszahlen`: producer deliberately avoided `基数` because of the cardinal-number homonym.
5. `Körper \(\Cfield\)` and the opening “all real and complex numbers” wording: translated without producer adjudication.
6. `Wertsysteme`: `复数值系统` is deliberately literal and may merit corpus-level terminology adjudication.
7. `der Faktor von \(f(x)\)`: producer resolved the local Chinese referent as the multiplier of `f(x)`.
8. `a. a. O.`: rendered `前引文献中`; assembler/checker must connect it to the actual citation context.
9. Hans-only scope: `线性流形`, `域`, `不可测`, punctuation, and sentence rhythm are PRC-oriented choices and do not constitute Taiwan-, Hong Kong-, or Macao-localized prose.

## Consequences and next custody step

- Changed artifacts in this worker assignment: only the produced TeX and this return.
- No shared lane log, registry, glossary, evidence graph, or other segment was edited.
- Producer state: translation delivered, unapproved and unchecked.
- Next cursor: independent Chinese checker receives the exact output hash above and performs all comparison/audit/build/render work outside this producer return.
- Source-defect routing condition: if an independent checker identifies a precise Noether source defect, it should be deduplicated and routed to `4 -nterslav`; this producer return makes no source-defect finding.
- External/human validation: none claimed.
