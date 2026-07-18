# Paper 37 Chinese terminology audit

## Scope and authority

This record covers the fourteen trap-prone decisions used in the bounded Paper 37 zh-Hans-CN rebase. The controlling source fact is the sealed P31 German head at:

- evidence://local-workspace/Codex/2026-06-01/we-are-currently-doing-a-massive/Noether_LocalCodex_20260718_P31_FullPaperCanonicalReaudit_WEB_DROP/1/01_current/cum_de_Local_20260718_P31.tex
- SHA-256: A48CB5CD1716974B686AC1CBA681CA4B17BC72F9043B78AD2528ACA41FCF814F
- exact local Paper 37 logical article: source/Noether_Paper37_German_P31_logical_article_exact_CRLF.tex
- local slice SHA-256: AF3B34ACF4FF8D91850AC56C4F86447ABC61E6641FF9795BEFBFDA004788585D

The inherited Chinese article is witness/locator material only:

- witness/Noether_Paper37_SimplifiedChinese_Inherited_logical_article_exact_CRLF.tex
- SHA-256: 1312DD725554A57A3A52FE780E924A5F7305C4E61E6418E393374B4D9EA1924B

The current Chinese output is zh-Hans-CN only. The PRC Mandarin-Simplified shelf dominates the available target-language evidence. It does not authorize zh-Hans-SG prose or Taiwan-, Hong Kong-, or Macao-localized Traditional Chinese. No readiness scalar is computed, and no external or human certification is claimed.

The final Hans TeX checkpoint used for this terminology package is zh-Hans-CN/Noether_Paper37_Chinese_P31Reconciled_zh-Hans-CN_v001.tex, SHA-256 A4A0A97E548840915650FE813AED8FC120D2ABE79F3FA76F9ADF35D5EDAB1B0C.

## Decision table

| ID | German source and P31 locus | Selected zh-Hans-CN form | Explicit sense window | Excluded reading / adverse form | Evidence and status |
|---|---|---|---|---|---|
| NOE-P37-HAUPTORDNUNG | Hauptordnung, lines 18623, 18635, 18642 | 整数环（极大阶）; thereafter 整数环 | Ring of integers / maximal order of the number field k | group order; inherited 主阶 | HFUT algebraic-number-theory notes pp. 9, 13 attest 整数环. Internally reviewed for this unit. |
| NOE-P37-P-ADIC-COMPLETION | p-adische Erweiterung k_p, lines 18623, 18635, 18684, 18773 | p-进完备化 | Completion of k at the place p; K_p is the corresponding scalar-extended algebra | arbitrary p-adic extension; inherited p-进扩张 | HFUT notes pp. 42, 44, 51 attest 完备化. Source construction fixes the narrower sense. |
| NOE-P37-LOCALIZATION-AT-PRIME | Quotientenring nach p, lines 18629, 18687, 18773; defining P31 locus line 20031 | 在 p 处的局部化环 | S^{-1}o with denominators prime to p | quotient R/I, residue ring, completion; inherited 商环 | AlJabr-1 chapter5 lines 365–386 distinguishes localization from lines 127–133, 209 quotient rings. |
| NOE-P37-GALOIS-MODULE | Galoismodul, lines 18627, 18629, 18657–18669, 18682 | 伽罗瓦模（带伽罗瓦群作用的模） | Module equipped with the stated Galois-group action | Galois group itself; field module without action | AlJabr-2 chapter6 lines 57, 76 and 2207 supply the G-module framework; exact compound has a bounded zero hit. |
| NOE-P37-MODULE-ISOMORPHISM | operatorisomorph, lines 18629, 18657, 18669, 18682 | 作为 [G]_o-模同构; thereafter 模同构 | Isomorphism respecting the integral group-ring action | analytic operator isomorphism; inherited 算子同构 / 算子域 | AlJabr-2 chapter6 lines 112, 144 and ECNU p. 48 support module-isomorphism language. |
| NOE-P37-SEMISIMPLE-ALGEBRA | System ohne Radikal (halbeinfach), lines 18637, 18655, 18684 | 根基为零的代数（即半单代数） | Finite-dimensional algebra whose radical is zero, hence semisimple in this context | a literal “system without roots”; inherited 无根基系统 / 半单系统 | AlJabr-2 chapter2 lines 1133, 1194 attest 半单; the source parenthesis fixes the equivalence. |
| NOE-P37-HYPERCOMPLEX-SCALAR-EXTENSION | hyperkomplexes System / Koeffizientenerweiterung, lines 18684, 18698, 18741, 18756; definition lines 16678–16685 | 有限维代数（原文“超复系统”） / 标量扩张 | Historical “hypercomplex system” means finite-dimensional algebra over the base field; coefficient extension means scalar extension | modern hypercomplex-number system; literal 扩张系数 | AlJabr-1 chapter7 lines 246, 271 supports 有限维代数; source definition is decisive. |
| NOE-P37-WURZELZAHL-RESOLVENT | Wurzelzahlen, lines 18627, 18714, 18722–18739, 18773 | 广义拉格朗日预解因子（原文 Wurzelzahlen） | Determinantal/resolvent factors D_lambda; cyclic specialization is a Lagrange resolvent sum | number of roots; inherited 广义根数 | Formula-led source reading plus AlJabr-1 chapter9 lines 954, 1155 预解式. Native 根数 occurrences are root counts and adverse. |
| NOE-P37-TRIVIAL-REPRESENTATION | Einsdarstellung / Nichteinsdarstellung, lines 18644, 18768, 18771 | 平凡表示 / 非平凡表示 | Representation sending every group element to the identity; its complement in the source product | unitary representation; inherited 单位表示 | HFUT group-representation notes pp. 8, 18, 20 attest 平凡表示. |
| NOE-P37-CONJUGATE-DUAL-REPRESENTATION | adjungierte Darstellung, lines 18743–18749 | 复共轭表示（在此等价于对偶表示） | Complex-conjugate character/representation, equivalent here to the contragredient dual for a finite group | adjoint representation Ad; categorical adjunction; inherited 伴随表示 | HFUT representation notes p. 6 attest 对偶表示; source character identity fixes the conjugate-dual relation. |
| NOE-P37-LINEAR-DISJOINT-ACCESSORY-EXTENSION | fremd / akzessorische Erweiterung, lines 18698, 18773 | 线性无交 / 辅助扩张（原文 akzessorische Erweiterung） | Field extensions with trivial tensor interaction over the base; historical accessory extension label is retained in a gloss | relatively prime integers; inherited 互素 / 附属扩张 | AlJabr-1 chapter8 lines 974–982 attests 线性无交; no exact native auxiliary-extension compound was found. |
| NOE-P37-ARTIN-CONDUCTOR | Führer / Artinscher Führer, lines 18627, 18768–18793 | 导子 / 阿廷导子 | The ideal/exponent invariant attached to the character or representation | derivation/functor language; an unrelated native 推导子图 hit | HFUT algebraic-number-theory notes pp. 89, 106 attest 导子 in the intended number-theory register. |
| NOE-P37-ABELIANIZATION | Faktorgruppe nach der Kommutatorgruppe, line 18739 | 模导出子群所得的商群（交换化） | Quotient of the group by its derived/commutator subgroup | generic factor group; the subgroup itself | AlJabr-1 chapter4 line 972 attests 导出子群 and 交换化; lines 263–266 attest 商群. |
| NOE-P37-INTEGRAL-ELEMENT | ganze Größen / ganze Elemente, line 18741 | 整元素 | Elements integral over the relevant ring of integers | “whole quantity,” integer-valued element, inherited 整量 | AlJabr-1 chapter7 lines 157, 195 and ECNU p. 44 attest 整元; 整元素 is the context-explicit running-prose form. |
| NOE-P37-TAME-RAMIFICATION | gewöhnlichen Verzweigungsstellen, opening argument, contrasted with höhere Verzweigung | 温分歧素位 | Tame/ordinary ramified prime places, precisely the branch contrasted with higher/wild ramification | generic “ordinary ramification”; inherited 普通分歧素位 | HFUT algebraic-number-theory notes extracted PDF p. 71 directly contrast 温分歧 and 野分歧; index p. 162 records 野分歧. |
| NOE-P37-PRINCIPAL-IDEAL-GENERATOR | Hasse footnote etwa mit Basis a_i / a … Basis des ursprünglichen Ideals | 由 a_i 生成 / 生成元 | A single element generating the relevant principal ideal | vector-space basis; inherited 基 | AlJabr-1 chapter5 lines 360–361 defines a principal ideal by I=Ra; the source's singular a fixes generator rather than basis. |

## Evidence classification

- Source fact: the German wording, formulas, cross-references, and defining loci above come from the exact P31 authority and its byte-preserved local slice.
- Computation: exact-string searches covered 71 Chinese TeX files in the recovered CINTA-cn, AlJabr-1, and AlJabr-2 roots. Zeros are bounded absence results only; they do not establish non-use in Chinese generally.
- Editorial inference: the selected Chinese forms and historical glosses are internal lane decisions constrained by the source sense and the cited PRC mathematical contexts.
- Model preference: where more than one adequate surface form remained, the lane preferred the form that exposed the operative mathematical relation and minimized false-friend risk.
- External or human validation: none. Regional localization and comprehension gates remain pending.

## Bounded exact-search results

The exact 71-file Chinese TeX scope returned zero hits for 主阶, p-进完备化, p-进扩张, 局部化环, 伽罗瓦模, 算子同构, 半单代数, 无根基系统, 超复系统, 标量扩张, 广义根数, 单位表示, 伴随表示 as a compound, 附属扩张, 辅助扩张, 阿廷导子, 换位子群, 整元素, and 整系数群环. Positive controls included 整数环 (26 lines / 9 files), 完备化 (69 / 7), 局部化 (105 / 10), 模同构 (12 / 6), 半单 (33 / 4), 有限维代数 (4 / 2), 预解式 (2 / 1), 线性无交 (4 / 1), 导出子群 (5 / 3), 交换化 (5 / 3), 整元 (5 / 1), 群环 (14 / 4), and 正规基 (10 / 2). The tame/wild ramification control and principal-ideal generator control came from page- and line-checked evidence, not from an exact-compound zero hit.

No German source defect was identified in these terminology decisions. Translation-witness defects and false-friend collisions are recorded in evidence/CHINESE_ADVERSE_EVIDENCE_LEDGER.csv. If a later source defect is found, it must be routed to the shared source-defect / Interslav review channel rather than silently normalized in this lane.
