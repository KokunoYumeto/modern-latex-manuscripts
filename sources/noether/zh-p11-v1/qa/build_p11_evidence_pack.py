from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE_DIR = ROOT / "evidence"

INPUTS = {
    "hans_a": (
        ROOT / "segments" / "zh-Hans-CN" / "P11_A_zh-Hans-CN.tex",
        "26DD08920E1008DA29A99BAE1D35F113F6F01FF0B766905CDC847D1BB059AFC2",
    ),
    "hans_b": (
        ROOT / "segments" / "zh-Hans-CN" / "P11_B_zh-Hans-CN.tex",
        "82FB18F5F3F28C768BEFF2027619286F853374A183A09D72A0581FA9D4FABB4C",
    ),
    "hans_c": (
        ROOT / "segments" / "zh-Hans-CN" / "P11_C_zh-Hans-CN.tex",
        "52802111D99718BE89923B90464A5F893163ABBD5AE7BB0590D3A983932FB712",
    ),
    "return_a": (
        ROOT / "worker_returns" / "P11_A_TRANSLATOR_RETURN.md",
        "15F4A6BD2A2A5A55F4568AD0A95FB43D052743C189789372C847EF684B9FBCB1",
    ),
    "return_b": (
        ROOT / "worker_returns" / "P11_B_TRANSLATOR_RETURN.md",
        "7B41F7A12CDB04FC57115EA1025EEE515E60A2362E340F5D9606FA655615BE9F",
    ),
    "return_c": (
        ROOT / "worker_returns" / "P11_C_TRANSLATOR_RETURN.md",
        "9C3B4FA3A83BB70167BC65810B087E7D651AB89D99BF8A8CC5221A7D530DBE82",
    ),
}

HANS_KEYS = ("hans_a", "hans_b", "hans_c")
RETURN_KEYS = ("return_a", "return_b", "return_c")

EVIDENCE_CLASS = (
    "producer terminology proposal extracted only from the three supplied Paper 11 "
    "PRC-oriented Hans producer segments and their three worker returns; German source "
    "and inherited witness files unconsulted in this packaging subtask; no source or "
    "witness comparison, semantic or formula checking, terminology adjudication, "
    "translation review, external validation, or Japanese/Korean consultation"
)
HANT_STATUS = (
    "controlled generic script proposal only; not zh-Hant-TW/HK/MO; "
    "regional lexical localization absent"
)
REVIEW_STATE = "independent check absent; pending"
JA_KO_STATUS = "JA and KO unconsulted, fields blank, and non-authorizing for Chinese"

ALLOWED_BASINS = {
    "Sino-xenic inherited",
    "modern Sino-xenic coinage/calque",
    "global modern loan",
    "native coinage",
    "mixed/contested",
    "unresolved",
}


def T(
    german: str,
    hans: str,
    hant: str,
    locator: str,
    scope: str,
    sense: str,
    excluded: str,
    alternatives: str,
    basin: str,
    debt: str,
    note: str,
) -> dict[str, str]:
    return {
        "german": german,
        "hans": hans,
        "hant": hant,
        "locator": locator,
        "scope": scope,
        "sense": sense,
        "excluded": excluded,
        "alternatives": alternatives,
        "basin": basin,
        "debt": debt,
        "note": note,
    }


TERMS = [
    T(
        "Gleichungen mit vorgeschriebener Gruppe",
        "具有给定群的方程",
        "具有給定群的方程",
        "segments/zh-Hans-CN/P11_A_zh-Hans-CN.tex title; worker_returns/P11_A_TRANSLATOR_RETURN.md row 具有给定群的方程",
        "equations constructed with the group attached to the equation prescribed in advance",
        "The named group is the equation's Galois-theoretic group in the producer framing.",
        "a generic collection; an administrative group; a group merely mentioned but not prescribed; group order alone",
        "具有指定群的方程; 具有预定群的方程; 具有规定群的方程",
        "modern Sino-xenic coinage/calque",
        "Qualitative debt: 给定 is strongly normalized in Mainland mathematical prose, while regional and historical preferences were not consulted; this is not a readiness score.",
        "The title form is a producer choice, not an independently certified project standard.",
    ),
    T(
        "irrationale / rationale Richtung",
        "无理方向 / 有理方向",
        "無理方向 / 有理方向",
        "segments/zh-Hans-CN/P11_A_zh-Hans-CN.tex opening paragraphs; worker_returns/P11_A_TRANSLATOR_RETURN.md row irrationale / rationale Richtung",
        "the root-characterizing and coefficient-characterizing approaches contrasted in the introduction",
        "无理 labels the root-oriented approach and 有理 labels the coefficient-oriented algebraic approach.",
        "philosophical irrationality or rationality; irrational real numbers alone; a moral or cognitive contrast",
        "根方向 / 系数方向; 根刻画方向 / 系数刻画方向",
        "mixed/contested",
        "Qualitative debt: the compact Mainland-readable calque depends on the explanatory prose to avoid ordinary-language attraction, and no regional evidence was consulted; this is not a readiness score.",
        "The paired labels remain bounded by the producer's explicit explanatory phrases.",
    ),
    T(
        "Rationalitätsbereich",
        "有理性域",
        "有理性域",
        "segments/zh-Hans-CN/P11_A_zh-Hans-CN.tex and P11_C_zh-Hans-CN.tex; worker_returns/P11_A_TRANSLATOR_RETURN.md and P11_C_TRANSLATOR_RETURN.md rows Rationalitätsbereich",
        "the coefficient or rationality domain relative to which the equation and parameter construction are considered",
        "A historical algebraic field/domain of rationality, broader than the rational-number field in the producer prose.",
        "a numerical range consisting only of rational numbers; ordinary-language rationality; a geometric region without field operations",
        "有理域; 基础域; 有理性范围",
        "mixed/contested",
        "Qualitative debt: 有理性域 is a Mainland-readable contextual narrowing of Bereich, but 域/体 and regional historical usage were not researched; this is not a readiness score.",
        "The repeated producer form is indexed without adjudicating a corpus-wide historical equivalent.",
    ),
    T(
        "Kreiskörper",
        "分圆域",
        "分圓域",
        "segments/zh-Hans-CN/P11_A_zh-Hans-CN.tex and P11_C_zh-Hans-CN.tex; worker_returns/P11_A_TRANSLATOR_RETURN.md and P11_C_TRANSLATOR_RETURN.md rows Kreiskörper",
        "the cyclotomic field in the Kronecker statement and the later group-character discussion",
        "A number field generated by roots of unity in the two producer contexts.",
        "a circular geometric region; a cyclic group; a generic splitting field; 循环域",
        "圆分域; 圆分体; cyclotomic field",
        "modern Sino-xenic coinage/calque",
        "Qualitative debt: 分圆域 is strongly Mainland-normalized, while 圆分域 and regional forms remain unresearched; this is not a readiness score.",
        "The two producer occurrences are grouped as one open terminology proposal.",
    ),
    T(
        "relativ-Abelscher Körper",
        "相对阿贝尔域",
        "相對阿貝爾域",
        "segments/zh-Hans-CN/P11_A_zh-Hans-CN.tex introduction; worker_returns/P11_A_TRANSLATOR_RETURN.md row relativ-Abelscher Körper",
        "a field Abelian relative to the named quadratic number field",
        "The relative relation is field-theoretic and base-dependent.",
        "an absolutely Abelian field without a base; a generic Abelian group; a relative object in category theory",
        "相对阿贝尔扩张; 相对 Abel 域; 相对交换域",
        "modern Sino-xenic coinage/calque",
        "Qualitative debt: the producer uses Mainland 域 and transliterated 阿贝尔, but whether the corpus should foreground 扩张 and how regions name Abel were not researched; this is not a readiness score.",
        "The proposal retains the producer's field-object wording and its alternatives.",
    ),
    T(
        "Parameterdarstellung",
        "参数表示",
        "參數表示",
        "segments/zh-Hans-CN/P11_A_zh-Hans-CN.tex and P11_B_zh-Hans-CN.tex; worker_returns/P11_A_TRANSLATOR_RETURN.md row Parameterdarstellung",
        "a parametrized representation intended to generate coefficient systems and equation families",
        "A representation by independent parameters in the construction, including supplementary representations for exceptional cases.",
        "a mere coordinate choice; a numerical table of parameters; representation theory of a group; one isolated formula",
        "参数化表示; 参数表达式; 参数表示式",
        "modern Sino-xenic coinage/calque",
        "Qualitative debt: 参数表示 follows current Mainland technical prose, but 表示/表达式 granularity and regional preferences remain untested; this is not a readiness score.",
        "The row packages the repeated producer choice without claiming validation.",
    ),
    T(
        "Lagrangescher Gattungsbereich",
        "Lagrange 属域",
        "Lagrange 屬域",
        "segments/zh-Hans-CN/P11_A_zh-Hans-CN.tex and P11_B_zh-Hans-CN.tex; worker_returns/P11_A_TRANSLATOR_RETURN.md and P11_B_TRANSLATOR_RETURN.md rows Lagrangescher Gattungsbereich",
        "the historically named field of root functions associated with the prescribed group",
        "The passage identifies it with the invariant field attached to the group.",
        "a class field in modern class-field theory; biological genus; geometric genus; an ordinary region; a Lagrange multiplier domain",
        "Lagrange 型域; Lagrange 种域; Lagrange 类别域; 保留 Gattungsbereich",
        "mixed/contested",
        "Qualitative debt: 属域 is a Mainland producer choice with strong class-field and regional lexical competition, and no local-language historical evidence was consulted; this is not a readiness score.",
        "Segment B uses 型域 while segment A uses 属域; the variation is retained rather than silently reconciled.",
    ),
    T(
        "Invariantenkörper",
        "不变量域",
        "不變量域",
        "segments/zh-Hans-CN/P11_A_zh-Hans-CN.tex invariant-field paragraph; worker_returns/P11_A_TRANSLATOR_RETURN.md row Invariantenkörper",
        "the field formed by rational functions invariant under the stated group action",
        "A function field of group invariants, locally equated with the Lagrange domain.",
        "one invariant element; a fixed numerical constant; a geometric invariant set; a body or physical object",
        "不变域; 不变式域; 不变量体",
        "modern Sino-xenic coinage/calque",
        "Qualitative debt: 不变量域 is Mainland-standard-looking, while 不变域 and 域/体 choices were not independently researched; this is not a readiness score.",
        "The producer keeps the object noun 不变量 explicit.",
    ),
    T(
        "Minimalbasis",
        "最小基",
        "最小基",
        "segments/zh-Hans-CN/P11_A_zh-Hans-CN.tex, P11_B_zh-Hans-CN.tex, and P11_C_zh-Hans-CN.tex; all three worker returns rows Minimalbasis",
        "a minimal basis for the rational function-field construction used to obtain the parameter representation",
        "A generating basis of the historical Lagrange domain/function field in this paper.",
        "a shortest vector basis; an arbitrary linear-algebra basis; basis functions in approximation theory; minimum cardinality without the function-field context",
        "极小基; 最小基底; 最简基",
        "mixed/contested",
        "Qualitative debt: 最小基 is repeated across Mainland-oriented producer segments, but 基/基底 and minimal-versus-minimum distinctions lack regional evidence; this is not a readiness score.",
        "All three producer returns flag the term, so the graph treats it as one cross-segment proposal.",
    ),
    T(
        "natürliche zur Gruppe gehörige Irrationalitäten",
        "属于该群的自然无理量",
        "屬於該群的自然無理量",
        "segments/zh-Hans-CN/P11_A_zh-Hans-CN.tex and P11_B_zh-Hans-CN.tex; worker_returns/P11_A_TRANSLATOR_RETURN.md and P11_B_TRANSLATOR_RETURN.md rows natürliche Irrationalitäten",
        "historically named root functions or quantities naturally attached to the group",
        "Functions of roots viewed as indeterminates that specialize into the stated number field in the producer account.",
        "irrational real numbers only; random irrational constants; natural numbers; a philosophical irrational object",
        "自然无理量; 自然无理元; 自然非有理量; 群的自然无理式",
        "mixed/contested",
        "Qualitative debt: 无理量 is a transparent Mainland calque but carries a powerful elementary-number attractor and no regional historical evidence was consulted; this is not a readiness score.",
        "The longer segment-A form and shorter segment-B form are represented by one bounded sense window.",
    ),
    T(
        "Teiler eines Körpers",
        "子域",
        "子域",
        "segments/zh-Hans-CN/P11_A_zh-Hans-CN.tex field-containment paragraph; worker_returns/P11_A_TRANSLATOR_RETURN.md row Teiler eines Körpers",
        "a field contained in another field in the historical containment argument",
        "Subfield containment, not arithmetic division.",
        "an integer divisor; a quotient field; a factor in a polynomial product; a divisor in algebraic geometry",
        "部分域; 子体; 保留 Teiler",
        "modern Sino-xenic coinage/calque",
        "Qualitative debt: 子域 is the Mainland contextual interpretation, while historical Teiler usage and regional 域/体 forms were not checked; this is not a readiness score.",
        "The proposal makes the producer's contextual narrowing visible.",
    ),
    T(
        "Wertsystem",
        "值组",
        "值組",
        "segments/zh-Hans-CN/P11_A_zh-Hans-CN.tex and P11_B_zh-Hans-CN.tex; worker_returns/P11_A_TRANSLATOR_RETURN.md and P11_B_TRANSLATOR_RETURN.md rows Wertsystem",
        "a simultaneous assignment of values to the displayed parameters or coefficients",
        "A grouped coefficient or parameter-value assignment in the nonlinear system and specialization argument.",
        "an ethical value system; one scalar value; an adjudicated ordered tuple structure not stated by the producer",
        "值系; 数值组; 值系统",
        "mixed/contested",
        "Qualitative debt: 值组 is concise Mainland prose, but 值系/数值组 and regional conventions were not researched; this is not a readiness score.",
        "The repeated producer choice is recorded without asserting tuple topology.",
    ),
    T(
        "singuläres Wertsystem",
        "奇异值组",
        "奇異值組",
        "segments/zh-Hans-CN/P11_A_zh-Hans-CN.tex and P11_B_zh-Hans-CN.tex exceptional-value passages; worker_returns/P11_B_TRANSLATOR_RETURN.md row singuläres Wertsystem",
        "a coefficient or parameter value assignment at which the displayed parameter representation degenerates",
        "The exceptional value system for which the producer account says the representation can become 0=0 or fail.",
        "singular values in matrix decomposition; an arbitrary geometric singular point; any exceptional value; denominator behavior not tied to the displayed construction",
        "奇异值系; 退化值组; 例外值组",
        "mixed/contested",
        "Qualitative debt: 奇异值组 is Mainland-readable but strongly attracts the matrix singular-value sense, and regional evidence is absent; this is not a readiness score.",
        "The adverse ledger keeps the matrix-analysis collision explicit.",
    ),
    T(
        "Ergänzungsdarstellung",
        "补充表示",
        "補充表示",
        "segments/zh-Hans-CN/P11_A_zh-Hans-CN.tex, P11_B_zh-Hans-CN.tex, and P11_C_zh-Hans-CN.tex; all three worker returns rows Ergänzungsdarstellung",
        "an additional parameter representation supplied for exceptional singular cases",
        "A supplementary parametrization, not a representation of a group.",
        "a complementary representation in modern representation theory; a set complement; a proof appendix; decorative supplementary display",
        "补足表示; 补充参数表示; 附加表示",
        "modern Sino-xenic coinage/calque",
        "Qualitative debt: 补充表示 is a general Mainland phrase whose technical scope depends on context, and no regional terminology was consulted; this is not a readiness score.",
        "The three segment proposals converge in surface form but remain unvalidated.",
    ),
    T(
        "algebraische Unabhängigkeit",
        "代数无关性",
        "代數無關性",
        "segments/zh-Hans-CN/P11_A_zh-Hans-CN.tex and P11_B_zh-Hans-CN.tex; worker_returns/P11_B_TRANSLATOR_RETURN.md row algebraische Unabhängigkeit",
        "algebraic independence of the displayed functions or parameters",
        "No nonzero polynomial relation over the stated coefficient field, as bounded by the producer context.",
        "linear independence; statistical independence; functional distinctness; numerical noncorrelation",
        "代数独立性; 代数无关",
        "modern Sino-xenic coinage/calque",
        "Qualitative debt: 代数无关性 is established Mainland wording, but 独立性 is a strong alternate and regional conventions were not consulted; this is not a readiness score.",
        "The entry packages the producer's exact surface form only.",
    ),
    T(
        "in bezug auf einen Körper die Gruppe Γ besitzen",
        "相对于某域具有群 Γ",
        "相對於某域具有群 Γ",
        "segments/zh-Hans-CN/P11_A_zh-Hans-CN.tex and P11_B_zh-Hans-CN.tex group-relative clauses; worker_returns/P11_B_TRANSLATOR_RETURN.md matching row",
        "the equation has the named group relative to the stated base field",
        "A field-relative group assertion in the equation construction.",
        "possession of an arbitrary abstract group; symmetry group without the field qualification; group order; a group action on the field itself",
        "在某域上以 Γ 为群; 关于某域的群为 Γ; 相对于某域的群为 Γ",
        "mixed/contested",
        "Qualitative debt: the literal Mainland producer syntax may be less idiomatic than 在某域上, while regional mathematical syntax was not researched; this is not a readiness score.",
        "The phrase-level row preserves the field qualifier as part of the concept.",
    ),
    T(
        "Reduktion der Gruppe",
        "群约化",
        "群約化",
        "segments/zh-Hans-CN/P11_A_zh-Hans-CN.tex and P11_B_zh-Hans-CN.tex specialization passages; worker_returns/P11_B_TRANSLATOR_RETURN.md row Reduktion der Gruppe",
        "specialization reduces the equation's group from the prescribed group to a smaller one",
        "A reduction in the attached group caused by parameter specialization.",
        "quotient-group formation automatically; a proof simplification; numerical lowering of group order alone; reduction modulo an ideal",
        "群降低; 群缩减; 群退化",
        "modern Sino-xenic coinage/calque",
        "Qualitative debt: 群约化 follows Mainland algebraic calque patterns, while 群降低 is plainer and regional usage was not consulted; this is not a readiness score.",
        "The producer segments also use 群缩小, so surface variation remains open.",
    ),
    T(
        "Wurzelsystem",
        "根组",
        "根組",
        "segments/zh-Hans-CN/P11_B_zh-Hans-CN.tex denominator argument; worker_returns/P11_B_TRANSLATOR_RETURN.md row Wurzelsystem",
        "the collection or tuple of polynomial roots used in the substitution",
        "A group of roots α_1,...,α_n in the displayed specialization.",
        "a root system in Lie theory; a system of radical expressions; a single root; a tree root hierarchy",
        "根系; 根值组; 根元组",
        "mixed/contested",
        "Qualitative debt: 根组 avoids the dominant Lie-theoretic 根系 attractor in Mainland usage, but tuple and regional conventions were not researched; this is not a readiness score.",
        "The adverse collision with Lie root systems is intentionally explicit.",
    ),
    T(
        "Mannigfaltigkeit",
        "流形 / 参数流形",
        "流形 / 參數流形",
        "segments/zh-Hans-CN/P11_B_zh-Hans-CN.tex and P11_C_zh-Hans-CN.tex closing comparisons; worker_returns/P11_B_TRANSLATOR_RETURN.md and P11_C_TRANSLATOR_RETURN.md rows Mannigfaltigkeit",
        "historical parameter-family or geometric-family language in the dimensional comparison",
        "The family of equations or parameters whose dimension is compared in the producer text.",
        "a modern smooth manifold with an asserted differentiable structure; mere multiplicity; set cardinality; a fully adjudicated algebraic variety",
        "参数簇; 簇; 多样体; 参数自由度",
        "mixed/contested",
        "Qualitative debt: 流形 is a powerful modern Mainland attractor that may over-specify historical structure, and no regional or historical evidence was consulted; this is not a readiness score.",
        "Segments B and C expose slightly different producer granularity and remain unreconciled.",
    ),
    T(
        "Affekt / affektlos",
        "特约 / 无附加约束",
        "特約 / 無附加約束",
        "segments/zh-Hans-CN/P11_A_zh-Hans-CN.tex, P11_B_zh-Hans-CN.tex, and P11_C_zh-Hans-CN.tex; all three worker returns Affekt rows",
        "historical vocabulary for an extra relation or constraint associated with prescribing the group",
        "A provisional label for constrained versus unconstrained equation families in this paper.",
        "emotional affect; grammatical mood; unaffected or separable equations automatically; an externally validated modern technical term",
        "带约束 / 无约束; 附加关系 / 无附加关系; 保留 Affekt / affektlos",
        "unresolved",
        "Qualitative debt: the three Mainland-oriented producer segments diverge on 特约, 带约束, and 无附加约束, and no historical or regional Chinese evidence was consulted; this is not a readiness score.",
        "This is the highest-uncertainty producer entry and explicitly preserves internal variation.",
    ),
    T(
        "Tschirnhausentransformation",
        "Tschirnhaus 变换",
        "Tschirnhaus 變換",
        "segments/zh-Hans-CN/P11_C_zh-Hans-CN.tex opening reduction; worker_returns/P11_C_TRANSLATOR_RETURN.md row Tschirnhausentransformation",
        "the named transformation used here to remove the next-to-leading coefficient",
        "A Tschirnhaus transformation with the elimination role stated in the producer segment.",
        "any linear change of variables; a Fourier transform; an unnamed substitution; a person's theorem unrelated to coefficient elimination",
        "契尔恩豪斯变换; 齐恩豪斯变换; Tschirnhaus 代换",
        "global modern loan",
        "Qualitative debt: the producer retains the Latin name beside Mainland 变换, while Chinese transliteration and regional name standards were not researched; this is not a readiness score.",
        "Latin-name retention is a producer convention, not a certified name standard.",
    ),
    T(
        "Dimension einer Form",
        "形式的次数",
        "形式的次數",
        "segments/zh-Hans-CN/P11_C_zh-Hans-CN.tex first reduction; worker_returns/P11_C_TRANSLATOR_RETURN.md row Dimension einer Form",
        "the degree of a homogeneous form lowered in the iterative decomposition",
        "Polynomial degree in the local form context, despite the historical surface word Dimension.",
        "vector-space dimension; manifold dimension; matrix size; rank; the number of variables automatically",
        "维数; 阶数; 形式的度数",
        "mixed/contested",
        "Qualitative debt: 次数 is Mainland polynomial language but represents a producer contextual choice against the source surface and lacks regional evidence; this is not a readiness score.",
        "The row flags the dimension/degree collision for checker-owned adjudication.",
    ),
    T(
        "homogen-gebrochene Funktion",
        "齐次分式函数",
        "齊次分式函數",
        "segments/zh-Hans-CN/P11_C_zh-Hans-CN.tex second reduction; worker_returns/P11_C_TRANSLATOR_RETURN.md row homogen-gebrochene Funktion",
        "a homogeneous rational or fractional function in the displayed variables",
        "A quotient of homogeneous expressions with the degree behavior used in the reduction.",
        "coefficient rationality alone; a broken function; a piecewise function; an arbitrary rational function without homogeneity",
        "齐次有理函数; 分式齐次函数; 齐次分数函数",
        "modern Sino-xenic coinage/calque",
        "Qualitative debt: 齐次分式函数 is Mainland-readable but 分式/有理函数 competition and regional practice were not researched; this is not a readiness score.",
        "The producer alternative 齐次有理函数 remains live.",
    ),
    T(
        "Vierergruppe",
        "四元群",
        "四元群",
        "segments/zh-Hans-CN/P11_C_zh-Hans-CN.tex explicit u,v,w basis example; worker_returns/P11_C_TRANSLATOR_RETURN.md row Vierergruppe",
        "the order-four group in the displayed basis-function construction",
        "The group of four elements used in the degree-four discussion.",
        "the quaternion group; a four-dimensional group; four unrelated groups; a four-variable set",
        "Klein 四元群; 克莱因四元群; 四阶群",
        "mixed/contested",
        "Qualitative debt: 四元群 is familiar Mainland terminology but can attract 四元数群, while whether Klein should be explicit and regional standards were not researched; this is not a readiness score.",
        "The adverse quaternion-group collision is carried forward explicitly.",
    ),
    T(
        "Achtergruppe",
        "八阶群",
        "八階群",
        "segments/zh-Hans-CN/P11_C_zh-Hans-CN.tex group reduction example; worker_returns/P11_C_TRANSLATOR_RETURN.md row Achtergruppe",
        "a group of order eight in the stated reduction",
        "Any group having eight elements in the producer sentence, without a separately established isomorphism type.",
        "the dihedral group automatically; an eighth-degree equation; eight unrelated groups; an eight-dimensional group",
        "八元群; 八元素群; 保留 Achtergruppe",
        "native coinage",
        "Qualitative debt: 八阶群 is transparent Mainland wording but 阶 can suggest degree or order and regional conventions were not researched; this is not a readiness score.",
        "The producer deliberately does not infer a specific order-eight group type.",
    ),
    T(
        "Körper der dritten Einheitswurzeln",
        "三次单位根域",
        "三次單位根域",
        "segments/zh-Hans-CN/P11_B_zh-Hans-CN.tex and P11_C_zh-Hans-CN.tex exceptional cases; worker_returns/P11_B_TRANSLATOR_RETURN.md row Körper der dritten Einheitswurzeln",
        "the number field containing the cube roots of unity",
        "The field generated by or containing third roots of unity in the exceptional alternating-group case.",
        "the finite field with three elements; a field with three unrelated polynomial roots; generic cubic-root extraction; one root alone",
        "三阶单位根域; 立方单位根域; 三次本原单位根域",
        "modern Sino-xenic coinage/calque",
        "Qualitative debt: 三次单位根域 is Mainland-readable, but 三阶/立方 and primitive-root granularity plus regional forms were not researched; this is not a readiness score.",
        "The producer context does not independently certify the strongest primitive-root wording.",
    ),
]


TERM_HEADERS = [
    "decision_id",
    "source_locator",
    "exact_german_phrase",
    "concept_scope",
    "zh_hans_cn_choice",
    "sense_window",
    "excluded_senses",
    "alternatives_considered",
    "lexical_attractor_basin",
    "mandarin_simplified_dominance_risk_debt",
    "evidence_class",
    "controlled_hant_form",
    "controlled_hant_status",
    "independent_check_status",
    "producer_note",
]

ADVERSE_HEADERS = [
    "adverse_id",
    "term_decision_id",
    "source_locator",
    "exact_german_phrase",
    "zh_hans_cn_producer_choice",
    "trap_or_adverse_reading",
    "contextual_reason_for_exclusion",
    "alternative_held_for_independent_review",
    "lexical_attractor_basin",
    "mandarin_simplified_dominance_risk_debt",
    "evidence_class",
    "controlled_hant_status",
    "review_state",
]

CROSSWALK_HEADERS = [
    "crosswalk_id",
    "term_decision_id",
    "source_locator",
    "exact_german_phrase",
    "zh_hans_cn_producer_form",
    "zh_hant_controlled_form",
    "zh_hant_status",
    "ja_form",
    "ko_form",
    "ja_ko_evidence_status",
    "sense_window",
    "excluded_senses",
    "lexical_attractor_basin",
    "mandarin_simplified_dominance_risk_debt",
    "evidence_class",
    "independent_check_status",
]

TERM_KEYS = {
    "german",
    "hans",
    "hant",
    "locator",
    "scope",
    "sense",
    "excluded",
    "alternatives",
    "basin",
    "debt",
    "note",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def manifest_sha(keys: tuple[str, ...], hashes: dict[str, str]) -> str:
    payload = "\n".join(f"{key}|{hashes[key]}" for key in keys).encode("utf-8")
    return hashlib.sha256(payload).hexdigest().upper()


def validate_terms() -> None:
    if not 22 <= len(TERMS) <= 26:
        raise RuntimeError(f"Expected 22–26 terms, got {len(TERMS)}")
    for index, term in enumerate(TERMS, 1):
        if set(term) != TERM_KEYS:
            raise RuntimeError(
                f"Term {index} has invalid shape: missing={TERM_KEYS - set(term)}, "
                f"extra={set(term) - TERM_KEYS}"
            )
        if term["basin"] not in ALLOWED_BASINS:
            raise RuntimeError(f"Term {index} has invalid basin: {term['basin']}")
        for key in TERM_KEYS:
            if not term[key].strip():
                raise RuntimeError(f"Term {index} has empty required field: {key}")
        if not term["debt"].startswith("Qualitative debt:"):
            raise RuntimeError(f"Term {index} dominance debt is not explicitly qualitative")
        if "not a readiness score" not in term["debt"]:
            raise RuntimeError(f"Term {index} debt lacks readiness-scalar exclusion")


def validate_inputs() -> dict[str, str]:
    actual: dict[str, str] = {}
    for key, (path, expected_sha) in INPUTS.items():
        if not path.is_file():
            raise FileNotFoundError(f"Required producer input absent: {path}")
        actual_sha = sha256(path)
        if actual_sha != expected_sha:
            raise RuntimeError(f"{key} SHA mismatch: expected {expected_sha}, got {actual_sha}")
        actual[key] = actual_sha
    actual["hans_manifest"] = manifest_sha(HANS_KEYS, actual)
    actual["return_manifest"] = manifest_sha(RETURN_KEYS, actual)
    actual["generator"] = sha256(Path(__file__))
    return actual


def write_csv(path: Path, headers: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=headers,
            quoting=csv.QUOTE_ALL,
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)


def make_term_rows() -> list[dict[str, str]]:
    rows = []
    for index, term in enumerate(TERMS, 1):
        rows.append(
            {
                "decision_id": f"P11-ZH-T{index:03d}",
                "source_locator": term["locator"],
                "exact_german_phrase": term["german"],
                "concept_scope": term["scope"],
                "zh_hans_cn_choice": term["hans"],
                "sense_window": term["sense"],
                "excluded_senses": term["excluded"],
                "alternatives_considered": term["alternatives"],
                "lexical_attractor_basin": term["basin"],
                "mandarin_simplified_dominance_risk_debt": term["debt"],
                "evidence_class": EVIDENCE_CLASS,
                "controlled_hant_form": term["hant"],
                "controlled_hant_status": HANT_STATUS,
                "independent_check_status": REVIEW_STATE,
                "producer_note": term["note"],
            }
        )
    return rows


def make_adverse_rows() -> list[dict[str, str]]:
    rows = []
    for index, term in enumerate(TERMS, 1):
        rows.append(
            {
                "adverse_id": f"P11-ZH-A{index:03d}",
                "term_decision_id": f"P11-ZH-T{index:03d}",
                "source_locator": term["locator"],
                "exact_german_phrase": term["german"],
                "zh_hans_cn_producer_choice": term["hans"],
                "trap_or_adverse_reading": term["excluded"],
                "contextual_reason_for_exclusion": term["sense"],
                "alternative_held_for_independent_review": term["alternatives"],
                "lexical_attractor_basin": term["basin"],
                "mandarin_simplified_dominance_risk_debt": term["debt"],
                "evidence_class": EVIDENCE_CLASS,
                "controlled_hant_status": HANT_STATUS,
                "review_state": REVIEW_STATE,
            }
        )
    return rows


def make_crosswalk_rows() -> list[dict[str, str]]:
    rows = []
    for index, term in enumerate(TERMS, 1):
        rows.append(
            {
                "crosswalk_id": f"P11-ZH-X{index:03d}",
                "term_decision_id": f"P11-ZH-T{index:03d}",
                "source_locator": term["locator"],
                "exact_german_phrase": term["german"],
                "zh_hans_cn_producer_form": term["hans"],
                "zh_hant_controlled_form": term["hant"],
                "zh_hant_status": HANT_STATUS,
                "ja_form": "",
                "ko_form": "",
                "ja_ko_evidence_status": JA_KO_STATUS,
                "sense_window": term["sense"],
                "excluded_senses": term["excluded"],
                "lexical_attractor_basin": term["basin"],
                "mandarin_simplified_dominance_risk_debt": term["debt"],
                "evidence_class": EVIDENCE_CLASS,
                "independent_check_status": REVIEW_STATE,
            }
        )
    return rows


def make_graph(hashes: dict[str, str]) -> dict:
    nodes = []
    edges = []
    for index, term in enumerate(TERMS, 1):
        suffix = f"{index:03d}"
        locus_id = f"P11-LOC-{suffix}"
        concept_id = f"P11-CON-{suffix}"
        hans_id = f"P11-HANS-{suffix}"
        hant_id = f"P11-HANT-{suffix}"
        choice_id = f"P11-CHOICE-{suffix}"
        nodes.extend(
            [
                {
                    "id": locus_id,
                    "type": "source_locus",
                    "locator": term["locator"],
                    "exact_german_phrase": term["german"],
                },
                {
                    "id": concept_id,
                    "type": "concept",
                    "scope": term["scope"],
                    "sense_window": term["sense"],
                    "excluded_senses": term["excluded"],
                },
                {
                    "id": hans_id,
                    "type": "form",
                    "language_scope": "zh-Hans-CN producer",
                    "form": term["hans"],
                },
                {
                    "id": hant_id,
                    "type": "form",
                    "language_scope": "zh-Hant-controlled nonregional producer proposal",
                    "form": term["hant"],
                    "status": HANT_STATUS,
                },
                {
                    "id": choice_id,
                    "type": "producer_choice",
                    "decision_id": f"P11-ZH-T{suffix}",
                    "lexical_attractor_basin": term["basin"],
                    "dominance_risk_debt": term["debt"],
                    "evidence_class": EVIDENCE_CLASS,
                    "review_state": REVIEW_STATE,
                },
            ]
        )
        edges.extend(
            [
                {"id": f"P11-E{suffix}-1", "type": "occurs_at", "from": concept_id, "to": locus_id},
                {"id": f"P11-E{suffix}-2", "type": "decides_for", "from": choice_id, "to": concept_id},
                {"id": f"P11-E{suffix}-3", "type": "selects_hans_form", "from": choice_id, "to": hans_id},
                {
                    "id": f"P11-E{suffix}-4",
                    "type": "records_controlled_hant_form",
                    "from": choice_id,
                    "to": hant_id,
                },
                {"id": f"P11-E{suffix}-5", "type": "controlled_form_of", "from": hant_id, "to": hans_id},
            ]
        )

    hans_hashes = "; ".join(f"{key}={hashes[key]}" for key in HANS_KEYS)
    return_hashes = "; ".join(f"{key}={hashes[key]}" for key in RETURN_KEYS)
    return {
        "graph_id": "NOE-P11-ZH-PRODUCER-CONCEPT-GRAPH-001",
        "work_unit": "Noether Paper 11 Chinese producer translation",
        "graph_status": {
            "purpose": "producer-side translation-decision proposal packaging only",
            "decision_count": len(TERMS),
            "independent_check": "absent",
            "german_source_files_consulted": "no",
            "inherited_witness_files_consulted": "no",
            "semantic_formula_or_terminology_checking": "not performed",
            "external_native_source_research": "not performed",
            "japanese_or_korean_evidence": "not consulted or used; fields blank and non-authorizing for Chinese",
            "compilation_or_rendering": "not performed",
            "controlled_hant_scope": HANT_STATUS,
            "translation_validation_or_readiness_claim": "none",
        },
        "provenance": {
            "permitted_hans_segments": {
                "path": (
                    "segments/zh-Hans-CN/P11_A_zh-Hans-CN.tex; "
                    "segments/zh-Hans-CN/P11_B_zh-Hans-CN.tex; "
                    "segments/zh-Hans-CN/P11_C_zh-Hans-CN.tex"
                ),
                "sha256": f"manifest={hashes['hans_manifest']}; {hans_hashes}",
                "use": "producer Chinese forms and local translated-context locators only; no translation validation",
            },
            "permitted_worker_returns": {
                "path": (
                    "worker_returns/P11_A_TRANSLATOR_RETURN.md; "
                    "worker_returns/P11_B_TRANSLATOR_RETURN.md; "
                    "worker_returns/P11_C_TRANSLATOR_RETURN.md"
                ),
                "sha256": f"manifest={hashes['return_manifest']}; {return_hashes}",
                "use": "German phrase labels, producer alternatives, sense windows, and adverse attractors only",
            },
            "german_source_and_inherited_witness": {
                "path": "not consulted in this evidence-packaging subtask",
                "sha256": "not computed",
                "use": "explicitly excluded from the permitted input set; no comparison or audit",
            },
            "controlled_hant_forms": {
                "path": "embedded producer crosswalk proposals in this generator",
                "sha256": "bound by evidence-generator hash",
                "use": (
                    "controlled generic script proposal only; not derived from JA/KO and not "
                    "Taiwan/Hong Kong/Macao localization or terminology validation"
                ),
            },
            "evidence_generator": {
                "path": "qa/build_p11_evidence_pack.py",
                "sha256": hashes["generator"],
                "use": "deterministic packaging into the adjacent Paper 20 CSV and typed-graph schemas",
            },
            "evidence_class": EVIDENCE_CLASS,
        },
        "node_type_definitions": {
            "source_locus": (
                "Locator and German phrase label in a permitted producer segment or worker return; "
                "not a German-source validation assertion."
            ),
            "concept": "Producer's bounded sense window and excluded lexical attractors.",
            "form": "Producer Chinese form with explicit Hans or nonregional controlled-Hant scope.",
            "producer_choice": (
                "Producer proposal with lexical-attractor basin, qualitative Mandarin-Simplified "
                "dominance debt, and open review state."
            ),
        },
        "edge_type_definitions": {
            "occurs_at": "Concept to permitted producer-artifact locator.",
            "decides_for": "Producer choice to concept.",
            "selects_hans_form": "Producer choice to Hans form.",
            "records_controlled_hant_form": "Producer choice to nonregional controlled-Hant proposal.",
            "controlled_form_of": (
                "Controlled-Hant script proposal to Hans lexical base without regional equivalence claim."
            ),
        },
        "nodes": nodes,
        "edges": edges,
    }


def validate_graph(graph: dict) -> dict[str, int | bool]:
    node_ids = [node["id"] for node in graph["nodes"]]
    edge_ids = [edge["id"] for edge in graph["edges"]]
    unique_node_ids = len(node_ids) == len(set(node_ids))
    unique_edge_ids = len(edge_ids) == len(set(edge_ids))
    if not unique_node_ids:
        raise RuntimeError("Duplicate graph node ID")
    if not unique_edge_ids:
        raise RuntimeError("Duplicate graph edge ID")
    node_id_set = set(node_ids)
    dangling = [
        edge["id"]
        for edge in graph["edges"]
        if edge["from"] not in node_id_set or edge["to"] not in node_id_set
    ]
    if dangling:
        raise RuntimeError(f"Dangling graph references: {dangling}")
    return {
        "unique_node_ids": unique_node_ids,
        "unique_edge_ids": unique_edge_ids,
        "dangling_references": len(dangling),
    }


def main() -> None:
    validate_terms()
    hashes = validate_inputs()
    term_rows = make_term_rows()
    adverse_rows = make_adverse_rows()
    crosswalk_rows = make_crosswalk_rows()
    graph = make_graph(hashes)
    graph_metrics = validate_graph(graph)
    EVIDENCE_DIR.mkdir(parents=True, exist_ok=True)
    write_csv(EVIDENCE_DIR / "TERMINOLOGY_LEDGER.csv", TERM_HEADERS, term_rows)
    write_csv(EVIDENCE_DIR / "ADVERSE_EVIDENCE_LEDGER.csv", ADVERSE_HEADERS, adverse_rows)
    write_csv(EVIDENCE_DIR / "CJKV_CROSSWALK.csv", CROSSWALK_HEADERS, crosswalk_rows)
    graph_path = EVIDENCE_DIR / "CONCEPT_EVIDENCE_GRAPH.json"
    graph_path.write_text(
        json.dumps(graph, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "rows": {
                    "TERMINOLOGY_LEDGER.csv": len(term_rows),
                    "ADVERSE_EVIDENCE_LEDGER.csv": len(adverse_rows),
                    "CJKV_CROSSWALK.csv": len(crosswalk_rows),
                },
                "nodes": len(graph["nodes"]),
                "edges": len(graph["edges"]),
                **graph_metrics,
                **hashes,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
