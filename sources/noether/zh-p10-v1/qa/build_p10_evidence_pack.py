from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE_DIR = ROOT / "evidence"

INPUTS = {
    "hans_a": (
        ROOT / "segments" / "zh-Hans-CN" / "P10_A_zh-Hans-CN.tex",
        "CDB3B17739EFE4D9C41D08E8B642CC1771E842593BDC30E5C7CB2719A2D8A59F",
    ),
    "hans_b": (
        ROOT / "segments" / "zh-Hans-CN" / "P10_B_zh-Hans-CN.tex",
        "16CA30A47CF25E28038414705157E54112D74D4AAB1E27F9649A44C681426FA6",
    ),
    "hans_c": (
        ROOT / "segments" / "zh-Hans-CN" / "P10_C_zh-Hans-CN.tex",
        "67D93BFFA16419E4A3E444C4AB9238B7E2A59E910889710A5BC36D93AA85F686",
    ),
    "return_a": (
        ROOT / "worker_returns" / "P10_A_TRANSLATOR_RETURN.md",
        "0E17810F989496410C4B1A145D3424325009854B504024ED3C66CAC193DB9F25",
    ),
    "return_b": (
        ROOT / "worker_returns" / "P10_B_TRANSLATOR_RETURN.md",
        "4CBEEEF476F04E079D0332BB1F155FC11C38CBADE283B9CFA7861BF1F07AC976",
    ),
    "return_c": (
        ROOT / "worker_returns" / "P10_C_TRANSLATOR_RETURN.md",
        "2FDCE8CB9A95CA70B7EA36E8B7BE47148464ACEEE7CE5AEE610DD35027B98020",
    ),
}

HANS_KEYS = ("hans_a", "hans_b", "hans_c")
RETURN_KEYS = ("return_a", "return_b", "return_c")

EVIDENCE_CLASS = (
    "producer terminology proposal extracted only from the three supplied Paper 10 "
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
        "isomorphe Abbildung",
        "同构映射",
        "同構映射",
        "segments/zh-Hans-CN/P10_A_zh-Hans-CN.tex title and definition; worker_returns/P10_A_TRANSLATOR_RETURN.md row isomorphe Abbildung",
        "a field map preserving the displayed rational operations and bijective onto its image field",
        "The map preserves addition, subtraction, multiplication, and division and is later shown reversible onto the image field.",
        "an arbitrary image; a geometric mapping; a nonbijective homomorphism; a representation of a group",
        "同构映照; 同构对应; 保留 Isomorphismus",
        "modern Sino-xenic coinage/calque",
        "Qualitative debt: 同构映射 is strongly Mainland-normalized, while 映射/映照 and regional conventions were not researched; this is not a readiness score.",
        "The title and definition use one producer form without independent certification.",
    ),
    T(
        "eindeutige Zuordnung",
        "单值对应",
        "單值對應",
        "segments/zh-Hans-CN/P10_A_zh-Hans-CN.tex definition; worker_returns/P10_A_TRANSLATOR_RETURN.md row eindeutige Zuordnung",
        "each source element has exactly one assigned image element",
        "Forward single-valuedness in the initial definition, before reverse uniqueness is established.",
        "two-sided bijection automatically; unique existence in both directions; an arbitrary deterministic rule",
        "唯一对应; 确定对应; 单一对应",
        "mixed/contested",
        "Qualitative debt: 单值 is common Mainland function language but may under-express the historical wording, and regional usage is absent; this is not a readiness score.",
        "The sense window separates this row from the later eineindeutig claim.",
    ),
    T(
        "eineindeutig / umkehrbar eindeutig",
        "一一对应 / 可逆单值",
        "一一對應 / 可逆單值",
        "segments/zh-Hans-CN/P10_A_zh-Hans-CN.tex section 1; worker_returns/P10_A_TRANSLATOR_RETURN.md row eineindeutig / umkehrbar eindeutig",
        "two-sided uniqueness or a bijection between the field and its image field",
        "Every image value corresponds to exactly one source value and the inverse map is defined.",
        "mere injectivity; mere single-valuedness; surjectivity onto an unrelated codomain",
        "双射; 一对一对应; 可逆的一一函数",
        "mixed/contested",
        "Qualitative debt: the producer uses both 一一 and 可逆单值 in Mainland prose, while a single corpus form and regional equivalents remain unresearched; this is not a readiness score.",
        "Internal surface variation is retained for checker-owned convergence.",
    ),
    T(
        "Abbildungssystem",
        "映射系统",
        "映射系統",
        "segments/zh-Hans-CN/P10_A_zh-Hans-CN.tex section 1; worker_returns/P10_A_TRANSLATOR_RETURN.md row Abbildungssystem",
        "the system of all image values f(z), shown to form a field",
        "The image-value collection equipped with the transported field operations.",
        "a software mapping system; the mapping function itself; a bare codomain with no field operations",
        "像系统; 值域; 映射值集",
        "mixed/contested",
        "Qualitative debt: 映射系统 is a literal Mainland-readable choice but 像域/值域 attract strongly and regional usage was not consulted; this is not a readiness score.",
        "The producer keeps the historical system noun visible.",
    ),
    T(
        "Funktionalgleichung",
        "函数方程",
        "函數方程",
        "segments/zh-Hans-CN/P10_A_zh-Hans-CN.tex throughout; worker_returns/P10_A_TRANSLATOR_RETURN.md row Funktionalgleichung",
        "equations constraining a function under field operations",
        "The displayed equations for f(x+y), f(x-y), f(xy), and f(x/y).",
        "a differential equation; an ordinary algebraic equation in values only; a generic functional identity with no displayed operations",
        "泛函方程; 函数等式",
        "mixed/contested",
        "Qualitative debt: 函数方程 is Mainland-readable while 泛函方程 is a strong modern alternate and regional evidence is absent; this is not a readiness score.",
        "The producer does not adjudicate the corpus-wide 函数/泛函 choice.",
    ),
    T(
        "lineare Basis",
        "线性基",
        "線性基",
        "segments/zh-Hans-CN/P10_A_zh-Hans-CN.tex and P10_C_zh-Hans-CN.tex; worker_returns/P10_A_TRANSLATOR_RETURN.md and P10_C_TRANSLATOR_RETURN.md lineare Basis entries",
        "a Hamel-type basis over the rational numbers in the additive functional-equation construction",
        "Rational linear representability with finite rational linear independence, as the producer note states.",
        "an arbitrary finite-dimensional basis; a basis over the complex numbers; a merely ordered list",
        "线性基底; Hamel 基; 哈梅尔基",
        "modern Sino-xenic coinage/calque",
        "Qualitative debt: 线性基 is normalized Mainland prose but can hide the Hamel scope, and name/regional standards were not researched; this is not a readiness score.",
        "The C return avoids 基数 for basis elements because of the cardinal-number homonym.",
    ),
    T(
        "rationale Basis",
        "有理基",
        "有理基",
        "segments/zh-Hans-CN/P10_A_zh-Hans-CN.tex and P10_B_zh-Hans-CN.tex; worker_returns/P10_A_TRANSLATOR_RETURN.md and P10_B_TRANSLATOR_RETURN.md rationale Basis rows",
        "the well-ordered basis through which field elements are represented by rational functions",
        "A basis for rational expression with rational-number coefficients, not automatically a Q-linear basis.",
        "a basis whose elements are rational numbers; a Hamel basis by default; ordinary rational reasoning",
        "有理基底; 有理函数基; 有理表示基",
        "mixed/contested",
        "Qualitative debt: 有理基 is a compact Mainland calque with a strong Q-linear attractor and no regional historical evidence; this is not a readiness score.",
        "The sense window follows the producer returns rather than an external terminology source.",
    ),
    T(
        "algebraische Basis",
        "代数基",
        "代數基",
        "segments/zh-Hans-CN/P10_A_zh-Hans-CN.tex and P10_B_zh-Hans-CN.tex; worker_returns/P10_A_TRANSLATOR_RETURN.md and P10_B_TRANSLATOR_RETURN.md algebraische Basis rows",
        "a basis permitting algebraic expression of all numbers while its members have no algebraic relations",
        "The field-theoretic algebraic-independence basis H or Z in the producer construction.",
        "a vector-space basis of an algebra; a basis consisting only of algebraic numbers; a polynomial basis",
        "代数基底; 超越基; 代数无关基",
        "mixed/contested",
        "Qualitative debt: 代数基 is Mainland-readable but may obscure the transcendence-basis sense, and regional terminology was not consulted; this is not a readiness score.",
        "The competing producer alternative 超越基 remains open.",
    ),
    T(
        "rational unabhängig",
        "有理无关",
        "有理無關",
        "segments/zh-Hans-CN/P10_A_zh-Hans-CN.tex well-order construction; worker_returns/P10_A_TRANSLATOR_RETURN.md row rational unabhängig",
        "independence from predecessors under rational expression",
        "No rational-function expression from finitely many preceding basis elements in the stated well-order.",
        "linear independence over Q only; statistical independence; ordinary logical independence",
        "有理独立; 关于有理函数无关; 有理表示无关",
        "mixed/contested",
        "Qualitative debt: 有理无关 is a literal Mainland producer form whose exact historical convention and regional alternatives were not researched; this is not a readiness score.",
        "The row explicitly excludes automatic Q-linear interpretation.",
    ),
    T(
        "algebraisch unabhängig / abhängig",
        "代数无关 / 代数相关",
        "代數無關 / 代數相關",
        "segments/zh-Hans-CN/P10_A_zh-Hans-CN.tex and P10_B_zh-Hans-CN.tex; all A/B return dependence rows",
        "algebraic independence or dependence over the preceding initial-segment field",
        "Polynomial-relation dependence in the field-extension induction.",
        "linear dependence; statistical dependence; causal dependence; functional similarity without a polynomial relation",
        "代数独立 / 代数依赖; 代数无关于 / 代数依赖于",
        "modern Sino-xenic coinage/calque",
        "Qualitative debt: 无关/相关 and 独立/依赖 compete in Mainland terminology, and regional choices were not consulted; this is not a readiness score.",
        "A and B use slightly different producer syntax, preserved here as alternatives.",
    ),
    T(
        "Abschnittskörper",
        "截段域",
        "截段域",
        "segments/zh-Hans-CN/P10_A_zh-Hans-CN.tex and P10_B_zh-Hans-CN.tex; worker_returns/P10_A_TRANSLATOR_RETURN.md and P10_B_TRANSLATOR_RETURN.md rows Abschnittskörper",
        "the field generated by rational combinations of basis elements preceding a fixed element in the well-order",
        "A well-order initial-segment field in the induction.",
        "a geometric section field; a piecewise domain; an arbitrary subfield unrelated to the well-order",
        "初段域; 前段域; 截域",
        "mixed/contested",
        "Qualitative debt: 截段域 is a transparent Mainland coinage without external historical evidence, while 初段域 is a strong alternate; this is not a readiness score.",
        "The repeated producer choice is not claimed as established terminology.",
    ),
    T(
        "Integritätsbereich",
        "整环",
        "整環",
        "segments/zh-Hans-CN/P10_A_zh-Hans-CN.tex section 1; worker_returns/P10_A_TRANSLATOR_RETURN.md row Integritätsbereich",
        "an integral domain contrasted with a field because quotients need not remain inside it",
        "A commutative domain without zero divisors in the local mapping definition.",
        "an integrally closed domain; a complete ring; an integer-only domain; a field automatically",
        "整域; 无零因子环; 完整域",
        "modern Sino-xenic coinage/calque",
        "Qualitative debt: 整环 is Mainland-standard-looking, while 整域 and regional 环/環 conventions were not independently researched; this is not a readiness score.",
        "The producer intentionally chose 整环 over the drafting witness's 整域.",
    ),
    T(
        "Wertsystem",
        "值组 / 值系统",
        "值組 / 值系統",
        "segments/zh-Hans-CN/P10_A_zh-Hans-CN.tex and P10_C_zh-Hans-CN.tex; worker_returns/P10_A_TRANSLATOR_RETURN.md and P10_C_TRANSLATOR_RETURN.md Wertsystem entries",
        "a grouped assignment or system of function values",
        "Plural or organized values in the basis construction and complex-value discussion.",
        "an ethical value system; one scalar value; an independently adjudicated tuple structure",
        "值系; 数值组; 复数值组",
        "mixed/contested",
        "Qualitative debt: A and C diverge between 值组 and 值系统 in Mainland prose, while regional practice is absent; this is not a readiness score.",
        "The internal producer variation remains explicit.",
    ),
    T(
        "extrem unstetig / total unstetig",
        "极端不连续 / 完全不连续",
        "極端不連續 / 完全不連續",
        "segments/zh-Hans-CN/P10_A_zh-Hans-CN.tex and P10_C_zh-Hans-CN.tex; worker_returns/P10_A_TRANSLATOR_RETURN.md and P10_C_TRANSLATOR_RETURN.md discontinuity entries",
        "historical labels for a locally dense-output property and a differently used literature term",
        "极端不连续 is locally defined by arbitrary approximation of prescribed output values near every input.",
        "ordinary pointwise discontinuity; 处处不连续 automatically; identification of extrem and total without the source distinction",
        "极度不连续; 处处不连续; 全不连续",
        "mixed/contested",
        "Qualitative debt: the producer calques are intelligible in Mainland prose but are not asserted as community-standard labels, and regional evidence is absent; this is not a readiness score.",
        "The source-defined distinction is retained as an adverse-control pair.",
    ),
    T(
        "Wohlordnung / Wohlordnungssatz",
        "良序 / 良序定理",
        "良序 / 良序定理",
        "segments/zh-Hans-CN/P10_A_zh-Hans-CN.tex and P10_B_zh-Hans-CN.tex; worker_returns/P10_A_TRANSLATOR_RETURN.md and P10_B_TRANSLATOR_RETURN.md Wohlordnung rows",
        "a well-order and the theorem used to select and construct bases",
        "A total order in which every nonempty subset has a least element, used in the producer's transfinite construction.",
        "a merely convenient or aesthetically good ordering; ordinary ascending numerical order",
        "良序关系; 良排序; 良序原理",
        "modern Sino-xenic coinage/calque",
        "Qualitative debt: 良序 is strongly Mainland-normalized, while theorem naming and regional forms were not consulted; this is not a readiness score.",
        "The producer files use a stable surface form.",
    ),
    T(
        "Mächtigkeit",
        "势",
        "勢",
        "segments/zh-Hans-CN/P10_A_zh-Hans-CN.tex and P10_B_zh-Hans-CN.tex; worker_returns/P10_A_TRANSLATOR_RETURN.md and P10_B_TRANSLATOR_RETURN.md Mächtigkeit rows",
        "set-theoretic cardinality of the bases and the continuum",
        "Cardinality, including equality with the cardinality of the continuum.",
        "algebraic power or exponent; physical strength; analytic magnitude; measure",
        "基数; 势数; 集合势",
        "mixed/contested",
        "Qualitative debt: 势 is established Mainland set-theory shorthand but collides with ordinary meanings and regional 基數 preferences were not consulted; this is not a readiness score.",
        "The cardinality sense is made explicit in every evidence row.",
    ),
    T(
        "rationale Funktion",
        "有理函数",
        "有理函數",
        "segments/zh-Hans-CN/P10_A_zh-Hans-CN.tex note defining coefficients; worker_returns/P10_A_TRANSLATOR_RETURN.md row rationale Funktion",
        "a rational function whose coefficients are also rational numbers in the local convention",
        "A quotient of polynomials with rational-number coefficients, as the producer note states.",
        "a function taking only rational values; ordinary-language rational behavior; any rational function over an unstated coefficient field",
        "有理数系数有理函数; 分式函数; 有理式",
        "modern Sino-xenic coinage/calque",
        "Qualitative debt: 有理函数 is standard Mainland wording but hides the local coefficient restriction, and regional evidence is absent; this is not a readiness score.",
        "The sense window carries the source-note restriction recorded by the producer.",
    ),
    T(
        "ganze rationale Funktion",
        "整有理函数",
        "整有理函數",
        "segments/zh-Hans-CN/P10_B_zh-Hans-CN.tex relation argument; worker_returns/P10_B_TRANSLATOR_RETURN.md row ganze rationale Funktion",
        "a historical rational expression with no effective denominator in the local identity argument",
        "The polynomial-like numerator functions H used to transport vanishing and nonvanishing relations.",
        "an entire holomorphic function; any rational function with poles; an integer-valued function",
        "整式有理函数; 多项式; 有理整函数",
        "mixed/contested",
        "Qualitative debt: 整有理函数 is a literal Mainland producer form with serious entire-function and polynomial attractors, and regional evidence is absent; this is not a readiness score.",
        "The B return explicitly marks the historical class as open.",
    ),
    T(
        "Abbildungskörper",
        "映射域",
        "映射域",
        "segments/zh-Hans-CN/P10_A_zh-Hans-CN.tex and P10_B_zh-Hans-CN.tex; worker_returns/P10_B_TRANSLATOR_RETURN.md row Abbildungskörper",
        "the image field corresponding to a source or initial-segment field under the map",
        "A field of images with transported operations.",
        "a bare codomain; scalar range; a geometric image; the mapping function itself",
        "像域; 映像域; 映射体",
        "mixed/contested",
        "Qualitative debt: 映射域 is Mainland-readable but 像域 may be more idiomatic and regional standards were not researched; this is not a readiness score.",
        "The row is distinct from Abbildungssystem but leaves possible convergence open.",
    ),
    T(
        "irreduzible Gleichung / Funktion",
        "不可约方程 / 不可约函数",
        "不可約方程 / 不可約函數",
        "segments/zh-Hans-CN/P10_A_zh-Hans-CN.tex and P10_B_zh-Hans-CN.tex; worker_returns/P10_B_TRANSLATOR_RETURN.md irreduzible row",
        "the irreducible polynomial relation over the stated initial-segment field and its transported counterpart",
        "Polynomial irreducibility in the local field-extension induction.",
        "an irreducible differential equation; an arbitrary unsimplifiable function; prime numbers; topological connectedness",
        "不可约多项式; 既约不可分解式; 不可分解方程",
        "mixed/contested",
        "Qualitative debt: 不可约 is Mainland-standard-looking, while 方程/函数 reflects historical nouns and requires checker attention; this is not a readiness score.",
        "The producer does not normalize the historical Funktion to 多项式 silently.",
    ),
    T(
        "Nullstelle",
        "根",
        "根",
        "segments/zh-Hans-CN/P10_B_zh-Hans-CN.tex clauses defining f(vartheta); worker_returns/P10_B_TRANSLATOR_RETURN.md row Nullstelle",
        "a value annihilating the displayed irreducible polynomial relation",
        "A root of the one displayed polynomial relation in the construction.",
        "a zero coefficient; the origin; a common zero of an ideal; an empty position",
        "零点; 方程根; 零根",
        "Sino-xenic inherited",
        "Qualitative debt: 根 is deeply normalized in Mainland algebra but 零点 and regional context choices were not consulted; this is not a readiness score.",
        "The producer prefers the equation-root reading over a literal zero-place calque.",
    ),
    T(
        "Adjunktion",
        "添入",
        "添入",
        "segments/zh-Hans-CN/P10_B_zh-Hans-CN.tex concluding induction; worker_returns/P10_B_TRANSLATOR_RETURN.md row Adjunktion",
        "adjoining a basis element to an isomorphic initial-segment field",
        "Field adjunction with closure under the relevant field operations.",
        "an adjoint operator; grammatical adjunct; bare set union; informal addition with no generated field",
        "伴随; 扩充; 添加; 添元",
        "mixed/contested",
        "Qualitative debt: 添入 is plain Mainland producer prose rather than a fixed technical noun, and 添元/adjunction regional practice was not researched; this is not a readiness score.",
        "The action-oriented form follows the translated segment.",
    ),
    T(
        "Primkörper",
        "素域",
        "素域",
        "segments/zh-Hans-CN/P10_B_zh-Hans-CN.tex final abstract-field paragraph; worker_returns/P10_B_TRANSLATOR_RETURN.md row Primkörper",
        "the prime subfield generated from the unit by field operations",
        "The smallest subfield of the abstract field in the producer explanation.",
        "a prime ideal; a field consisting of prime numbers; any initially chosen coefficient field",
        "基本域; 最小子域; prime field",
        "modern Sino-xenic coinage/calque",
        "Qualitative debt: 素域 is standard-looking Mainland terminology but can attract prime-ideal senses and regional 体/域 choices were not consulted; this is not a readiness score.",
        "The sense window binds 素 to the prime-subfield construction.",
    ),
    T(
        "Induktionsschluß",
        "归纳论证",
        "歸納論證",
        "segments/zh-Hans-CN/P10_A_zh-Hans-CN.tex and P10_B_zh-Hans-CN.tex well-order induction; worker_returns/P10_B_TRANSLATOR_RETURN.md row Induktionsschluß",
        "the induction along the well-order propagating isomorphism of successive initial-segment fields",
        "A possibly transfinite induction step tied to the well-order construction.",
        "empirical induction; finite induction on polynomial degree automatically; a mere concluding inference",
        "归纳推理; 超限归纳步骤; 归纳法",
        "modern Sino-xenic coinage/calque",
        "Qualitative debt: 归纳论证 is neutral Mainland prose but may understate transfinite structure, and regional terminology was not consulted; this is not a readiness score.",
        "The alternatives retain the stronger 超限 cue for checker review.",
    ),
    T(
        "Unstetigkeitswerte",
        "不连续性值",
        "不連續性值",
        "segments/zh-Hans-CN/P10_C_zh-Hans-CN.tex rank discussion; worker_returns/P10_C_TRANSLATOR_RETURN.md proposal P10-C-ZH-P002",
        "output values locally approachable by the function near the input under discussion",
        "Attainable or approximable output values associated with the source-defined extreme discontinuity.",
        "input discontinuity points; ordinary function values; cluster values with an imported modern limit-theory definition",
        "不连续值; 聚值; 极限值",
        "modern Sino-xenic coinage/calque",
        "Qualitative debt: 不连续性值 is a transparent Mainland producer coinage with no community or regional validation; this is not a readiness score.",
        "The row explicitly distinguishes values from points of discontinuity.",
    ),
    T(
        "Rang vier/drei/zwei/eins",
        "秩为四/三/二/一",
        "秩為四/三/二/一",
        "segments/zh-Hans-CN/P10_C_zh-Hans-CN.tex numbered rank cases; worker_returns/P10_C_TRANSLATOR_RETURN.md proposal P10-C-ZH-P003",
        "the source-defined rank determined inversely by the number of independent linear relations among x,y,X,Y",
        "No relation gives rank four; one, two, or three relations give rank three, two, or one.",
        "matrix rank without the local definition; group order; polynomial degree; 四阶/三阶",
        "四秩/三秩; 四阶/三阶; rank 4/rank 3",
        "modern Sino-xenic coinage/calque",
        "Qualitative debt: 秩 is standard Mainland linear-algebra vocabulary, but the unusual local convention and regional phrasing require independent review; this is not a readiness score.",
        "The graph keeps the source-defined relation count in the sense node.",
    ),
    T(
        "lineare Mannigfaltigkeit",
        "线性流形",
        "線性流形",
        "segments/zh-Hans-CN/P10_C_zh-Hans-CN.tex rank-four and rank-three cases; worker_returns/P10_C_TRANSLATOR_RETURN.md proposal P10-C-ZH-P004",
        "a one- or two-dimensional historical linear family of locally approachable values",
        "The family determined by the displayed real linear relations; modern affine-versus-linear refinement remains open.",
        "a modern smooth manifold with asserted differentiable structure; an algebraic variety automatically; a vector space necessarily through the origin",
        "线性簇; 线性多样体; 线性空间; 仿射流形",
        "mixed/contested",
        "Qualitative debt: 线性流形 is a Mainland-oriented historical calque that may over-specify modern structure and has no regional validation; this is not a readiness score.",
        "The C return explicitly leaves affine-versus-linear modernization to a checker.",
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
    if not 24 <= len(TERMS) <= 28:
        raise RuntimeError(f"Expected 24–28 terms, got {len(TERMS)}")
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
                "decision_id": f"P10-ZH-T{index:03d}",
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
                "adverse_id": f"P10-ZH-A{index:03d}",
                "term_decision_id": f"P10-ZH-T{index:03d}",
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
                "crosswalk_id": f"P10-ZH-X{index:03d}",
                "term_decision_id": f"P10-ZH-T{index:03d}",
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
        locus_id = f"P10-LOC-{suffix}"
        concept_id = f"P10-CON-{suffix}"
        hans_id = f"P10-HANS-{suffix}"
        hant_id = f"P10-HANT-{suffix}"
        choice_id = f"P10-CHOICE-{suffix}"
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
                    "decision_id": f"P10-ZH-T{suffix}",
                    "lexical_attractor_basin": term["basin"],
                    "dominance_risk_debt": term["debt"],
                    "evidence_class": EVIDENCE_CLASS,
                    "review_state": REVIEW_STATE,
                },
            ]
        )
        edges.extend(
            [
                {"id": f"P10-E{suffix}-1", "type": "occurs_at", "from": concept_id, "to": locus_id},
                {"id": f"P10-E{suffix}-2", "type": "decides_for", "from": choice_id, "to": concept_id},
                {"id": f"P10-E{suffix}-3", "type": "selects_hans_form", "from": choice_id, "to": hans_id},
                {
                    "id": f"P10-E{suffix}-4",
                    "type": "records_controlled_hant_form",
                    "from": choice_id,
                    "to": hant_id,
                },
                {"id": f"P10-E{suffix}-5", "type": "controlled_form_of", "from": hant_id, "to": hans_id},
            ]
        )

    hans_hashes = "; ".join(f"{key}={hashes[key]}" for key in HANS_KEYS)
    return_hashes = "; ".join(f"{key}={hashes[key]}" for key in RETURN_KEYS)
    return {
        "graph_id": "NOE-P10-ZH-PRODUCER-CONCEPT-GRAPH-001",
        "work_unit": "Noether Paper 10 Chinese producer translation",
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
                    "segments/zh-Hans-CN/P10_A_zh-Hans-CN.tex; "
                    "segments/zh-Hans-CN/P10_B_zh-Hans-CN.tex; "
                    "segments/zh-Hans-CN/P10_C_zh-Hans-CN.tex"
                ),
                "sha256": f"manifest={hashes['hans_manifest']}; {hans_hashes}",
                "use": "producer Chinese forms and translated-context locators only; no translation validation",
            },
            "permitted_worker_returns": {
                "path": (
                    "worker_returns/P10_A_TRANSLATOR_RETURN.md; "
                    "worker_returns/P10_B_TRANSLATOR_RETURN.md; "
                    "worker_returns/P10_C_TRANSLATOR_RETURN.md"
                ),
                "sha256": f"manifest={hashes['return_manifest']}; {return_hashes}",
                "use": "German phrase labels, alternatives, sense windows, and adverse attractors only",
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
                "path": "qa/build_p10_evidence_pack.py",
                "sha256": hashes["generator"],
                "use": "deterministic packaging into the adjacent Paper 11 CSV and typed-graph schemas",
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
