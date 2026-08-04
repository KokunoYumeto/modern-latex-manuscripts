# Noether Paper 10 — Chinese producer translation notes

## Producer state and controlling boundary

This package contains a complete producer translation of Noether Paper 10, *Die Funktionalgleichungen der isomorphen Abbildung*, in PRC-oriented Simplified Chinese (`zh-Hans-CN`) plus a mechanically derived controlled-generic Traditional Chinese script form (`zh-Hant-controlled`). It is `translated/built; independent check pending`.

Floris's controlling instruction is retained verbatim:

> you do not check - you translate - other sessions CHEWCK

Accordingly, the producer did not source-check, compare or audit the inherited witness, semantic-check, formula-check, terminology-check, review or harmonize the translation, inspect or render either PDF, perform visual QA, regionalize Traditional Chinese, approve, archive, publish, certify, or work on SGA. Compiler success and mechanical token counts are not translation validation.

The applicable append-only lane decisions are `ZH-D112` (claim/custody) and `ZH-D113` (translation and mechanical-build completion). This note was assembled on `2026-07-22 13:29:01 +02:00` from the frozen producer records; it adds no validation.

## Source and witness custody

| Role | Exact cursor | Bytes | SHA-256 | Use in this package |
|---|---:|---:|---|---|
| Live authority pointer at claim | pointer file | — | `FAC89D076DCE1C24B534595595B75BA1C88A8956E370EF848B307E731633EED1` | Custody pointer only |
| Current German authority whole file at claim | whole file | — | `443EF950D7D45DC6D9E44A9B87501620C10DA873E50E5F2B253ECCAE6A946D27` | Source authority named by the live pointer |
| Paper 10 current-German slice | lines 7664–7864; bytes `[493872,522014)` | 28,142 | `4EDD9F5B95EE308344B11190088C6D864FB4456AC8AD20E152FA1254E5612234` | Translation authority |
| Inherited Hans slice | lines 7467–7714; bytes `[452768,477293)` | 24,525 | `D74C8B835ADF307AAF4908551BA7C21806DC9772C5A187DD84506F982FAC674C` | Drafting witness/locator only; not audited |

The stale shared R821 authority pointer was not used. The exact source-custody record is `qa/SOURCE_CUSTODY_RECORD.json`, SHA-256 `4CD4FFAAB30BEC07C435D8D3C69E0E5B8C57BD7ED2557048FBB0C228E9369A8C`; the readable custody note is `SOURCE_CUSTODY.md`, SHA-256 `6BE7F00B02208ECD28388FD6FE49BE9EA9A68B2EC9590039CC3BC290E92261E3`.

## Segment and worker binding

Segmentation was contiguous and non-overlapping by construction; that is an operational statement, not a semantic or formula check. The segmentation record `qa/SOURCE_SEGMENTATION_RECORD.json` has SHA-256 `75E945223178817956467FE7D6FA7C377A3D932A6B3D870DB9416B0F6F07F813`.

| Segment | German source cursor / SHA-256 | Drafting-witness cursor / SHA-256 | Produced Hans TeX bytes / SHA-256 | Worker-return SHA-256 |
|---|---|---|---|---|
| A | lines 7664–7710 / `1B53FD04B807320802E95D3840EB9E456704BB1EC4E02D42CD4C74DDF8AEA148` | lines 7467–7523 / `4788ABCC0BA4574ACB3DDDAF7E04D9CDB9F07305AAB3B4AF5083CC36C92C0AED` | 9,275 / `CDB3B17739EFE4D9C41D08E8B642CC1771E842593BDC30E5C7CB2719A2D8A59F` | `0E17810F989496410C4B1A145D3424325009854B504024ED3C66CAC193DB9F25` |
| B | lines 7711–7767 / `B709B6D1B8C866B43E73A17507ECCCF6F258BD5F756B90DC65D28333926DE0E1` | lines 7524–7597 / `3AD53FB36351485C5FB1D97C4CB1F8E789609F50348BC97CF329DD962B29A21D` | 7,657 / `16CA30A47CF25E28038414705157E54112D74D4AAB1E27F9649A44C681426FA6` | `4CBEEEF476F04E079D0332BB1F155FC11C38CBADE283B9CFA7861BF1F07AC976` |
| C | lines 7768–7864 / `E68CF6495A6E69661F55595D1FEE7487ED19B0182AC395AEC48667B235168C0B` | lines 7598–7714 / `F32417AF6DC8719B732536C60EC9207F2D821B7ABE7FC56F09250CAD314163C6` | 7,559 / `67D93BFFA16419E4A3E444C4AB9238B7E2A59E910889710A5BC36D93AA85F686` | `2FDCE8CB9A95CA70B7EA36E8B7BE47148464ACEEE7CE5AEE610DD35027B98020` |

No producer cross-segment harmonization or post-return content review was performed. The concatenated wording therefore preserves the three bounded producer returns for a separate checker.

## Producer terminology proposals for separate checking

Every entry below is an editorial translation proposal or model preference, not an approved term. Alternatives and adverse readings are intentionally exposed so another session can check them.

| German form | Producer proposal | Alternatives / adverse reading retained for checker |
|---|---|---|
| `isomorphe Abbildung` | `同构映射` | `同构映照`, `同构对应`; do not read as an arbitrary representation or nonbijective homomorphism |
| `eindeutige Zuordnung` | `单值对应` | `唯一对应`, `确定对应`; by itself it does not assert later two-sided uniqueness |
| `eineindeutig`, `umkehrbar eindeutig` | `一一对应`, `一一`, `可逆单值` | `双射`, `一对一对应`; distinguish from merely single-valued or injective |
| `Abbildungssystem` | `映射系统` | `像系统`, `值域`, `映射值集`; not the mapping function itself |
| `Funktionalgleichung` | `函数方程` | `泛函方程`; project-wide choice remains open |
| `lineare Basis` | `线性基` | `线性基底`, `Hamel 基`; source-note `Basiszahlen` was rendered `基中元素` to avoid the cardinal-number homonym `基数` |
| `rationale Basis` | `有理基` | `有理基底`, `有理函数基`; do not assume a Q-linear basis or a basis of rational numbers |
| `algebraische Basis` | `代数基` | `代数基底`, `代数无关基`, `超越基`; not an arbitrary algebra basis or a basis of algebraic numbers |
| `rational unabhängig` | `有理无关` | `有理独立`; do not silently narrow to Q-linear independence |
| `algebraisch unabhängig / abhängig` | `代数无关 / 代数相关`, locally also `代数独立于 / 代数依赖于` | Competing forms were not harmonized; exclude linear/statistical/causal readings |
| `Abschnittskörper` | `截段域` | `初段域`, `前段域`, `截域`; not a geometric section or piecewise domain |
| `Integritätsbereich` | `整环` | `整域`, `无零因子环`; not automatically integrally closed |
| `Wertsystem` | `值组`, locally `复数值系统` | `值系`, `数值组`, `值系统`; not an ethical value system or one scalar value |
| `extrem unstetig` | `极端不连续` | `极度不连续`, `完全不连续`; `处处不连续` is potentially too weak |
| `total unstetig` | `完全不连续` | Historical label; do not automatically identify with modern `处处不连续` |
| `Unstetigkeitswerte` | `不连续性值` | `不连续值`; avoid silently importing `聚值` or `极限值` |
| `Wohlordnung`, `Wohlordnungssatz` | `良序`, `良序定理` | `良序关系`, `良排序`, `良序原理`; not ordinary numerical ordering |
| `Mächtigkeit` | `势` | `基数`, `势数`; not exponentiation or physical strength |
| `Permutationen eines Körpers` | `一个域的置换` | `域的排列`, `域自同构`; historical expression must not be normalized without checking |
| `rationale Funktion` | `有理函数` | Local source note restricts coefficients to rational numbers; not a rational-valued function |
| `ganze rationale Funktion` | `整有理函数` | `整式有理函数`, `多项式`, `有理整函数`; not an entire holomorphic function or arbitrary function with poles |
| `Abbildungskörper` | `映射域` | `像域`, `映像域`; not a bare codomain or scalar range |
| `irreduzible Gleichung / Funktion` | `不可约方程 / 不可约函数` | `不可约多项式`; do not import differential-equation or generic simplification senses |
| `Nullstelle` | `根` | `零点`; local polynomial root, not automatically an ideal's common zero |
| `Adjunktion` | `添入` | `伴随`, `扩充`, `添加`; not an adjoint operator or bare set union |
| `Primkörper` | `素域` | `基本域`, `最小子域`; not a prime ideal or a field of prime numbers |
| `Induktionsschluß` | `归纳论证` | `归纳推理`, `超限归纳步骤`; not empirical induction |
| `allgemeinste Lösung / Abbildung` | `最一般的解 / 最一般同构映射` | `通解`, `最普遍的解`; not one typical example or an unstated uniqueness claim |
| `Rang vier/drei/zwei/eins` | `秩为四/三/二/一`; theorem prose `秩四/秩二` | Avoid `四阶`; retain the source-defined relation-count convention for checking |
| `lineare Mannigfaltigkeit` | `线性流形` | `线性簇`, `线性多样体`, `线性空间`; historical linear/affine sense remains open |
| algebraic `Körper`; numerical `Gebiet` | `域`; `在……域内` | Do not mechanically map every `Gebiet` to geometric `区域`; Hant regional conventions remain open |
| mapping phrases `gehen ... in sich über` | `映为自身`, `对应于自身` | `保持不变` alone can suppress the explicit mapping relation |
| `der Faktor von f(x)` | `乘在 \(f(x)\) 上的因子` | `f(x) 的因子` is referentially ambiguous; local multiplier interpretation requires checking |
| citation shorthand `a. a. O.` | `前引文献中` | `同上`; exact bibliography linkage remains checker/assembler work |

Mandarin-Simplified dominance risk is especially material for `域`, `线性流形`, `不连续性值`, `不可测`, punctuation, and sentence rhythm. These Hans choices do not authorize Taiwan-, Hong Kong-, or Macao-localized prose.

## Controlled-Hant status

The Hant artifact is a protected mechanical `s2t` transport of the Hans producer output, followed by recorded controlled normalizations. Its TeX SHA-256 is `B74A2EB8205168994F182D76A610E6B571A068F02D697E57AB9276439D5851BD`. It is labeled only `zh-Hant-controlled` and explicitly is not `zh-Hant-TW`, `zh-Hant-HK`, or `zh-Hant-MO` prose. It inherits PRC-oriented lexical choices and all unchecked producer uncertainty.

## Source-defect route and next custody step

This producer found and claims no source defect. The two missing standalone-preamble controls were packaging events, not source defects. If a separate checker identifies a precise Noether source defect, the finding must first be deduplicated against existing reports and then routed so `4 -nterslav` sees that precise checker finding.

Next custody step: a separate checking session must receive the exact frozen hashes, perform all source/semantic/formula/terminology/translation/visual checks, and return findings without rewriting this producer history. No archive, publication, approval, certification, or SGA action is authorized here.
