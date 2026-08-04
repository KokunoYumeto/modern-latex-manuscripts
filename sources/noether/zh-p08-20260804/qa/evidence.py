from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE_DIR = ROOT / "evidence"

FIXED_INPUTS = {
    "sealed_source": (
        ROOT / "source" / "P08_complete_lines5957_6347_LF_terminal.tex",
        "7E5EEBEB8F569F101490D8262072027C876C8102D2841A2A57F96E0DC2708E71",
    ),
    "inherited_hans_witness": (
        ROOT / "witness" / "P08_inherited_Hans_lines6395_6842_LF_terminal.tex",
        "F1DC44C7E4FC9D55EDC7636660CC741959A06613EABA43014353B663DE7A36D3",
    ),
    "translation_notes": (
        ROOT / "TRANSLATION_NOTES.md",
        "CE0559CA059C07EC41EDEFC2B9F4BF170F25F774CFC2DB9950A8F9677058EDF9",
    ),
    "return_s01": (
        ROOT / "worker_returns" / "P08_S01_WORKER_RETURN.md",
        "85CD91322EF04611136D891C7D05A25233331FD2207CCF81F2CE0854B1CCE4F2",
    ),
    "return_s03": (
        ROOT / "worker_returns" / "P08_S03_WORKER_RETURN.md",
        "E9E14FF5BA74B5411C8A204F4B2A7774DB510E3A134A769F132B8241FF8F97D2",
    ),
}

OUTPUTS = {
    "terms": EVIDENCE_DIR / "terms.csv",
    "adverse": EVIDENCE_DIR / "adverse.csv",
    "crosswalk": EVIDENCE_DIR / "crosswalk.csv",
    "graph": EVIDENCE_DIR / "graph.json",
}

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

ALLOWED_BASINS = {
    "Sino-xenic inherited",
    "modern Sino-xenic coinage/calque",
    "global modern loan",
    "native coinage",
    "mixed/contested",
    "unresolved",
}

EVIDENCE_CLASS = (
    "producer terminology proposal grounded in the sealed Paper 8 translation unit, "
    "the inherited Simplified-Chinese translation witness, the completed S01 and S03 "
    "producer returns, and the final target paths supplied at generation time; no "
    "German-source adjudication, semantic/formula checking, independent Chinese check, "
    "external native-source validation, or Japanese/Korean authorization"
)
HANT_STATUS = (
    "controlled generic Traditional-script record only; not zh-Hant-TW/HK/MO; "
    "regional lexical localization absent"
)
REVIEW_STATE = "independent Chinese check pending; not performed"
JA_KO_STATUS = "JA and KO unconsulted, fields blank, and non-authorizing for Chinese"


@dataclass(frozen=True)
class Term:
    german: str
    variants: tuple[tuple[str, str], ...]
    locator: str
    scope: str
    sense: str
    excluded: str
    alternatives: tuple[str, ...]
    basin: str
    debt: str
    note: str


@dataclass(frozen=True)
class BoundTerm:
    term: Term
    hans: str
    hant: str


def V(hans: str, hant: str) -> tuple[tuple[str, str], ...]:
    return ((hans, hant),)


def T(
    german: str,
    variants: tuple[tuple[str, str], ...],
    locator: str,
    scope: str,
    sense: str,
    excluded: str,
    alternatives: Sequence[str],
    basin: str,
    debt: str,
    note: str,
) -> Term:
    return Term(
        german=german,
        variants=variants,
        locator=locator,
        scope=scope,
        sense=sense,
        excluded=excluded,
        alternatives=tuple(alternatives),
        basin=basin,
        debt=debt,
        note=note,
    )


TERMS = (
    T(
        "ganze rationale Darstellung / ganz und rational darstellen",
        V("整有理表示", "整有理表示"),
        "source/P08_complete_lines5957_6347_LF_terminal.tex; title, introduction, and section I",
        "polynomial expression of invariants in a finite generating system",
        "The historical phrase says that the target invariant is expressed by whole rational, hence polynomial, combinations of the stated invariants.",
        "representation theory; an arbitrary rational-fraction expression; a rational map; algebraic integrality by itself",
        ("整有理表达", "多项式表示", "整式有理表示"),
        "mixed/contested",
        "The compact form 整有理表示 is inherited by the PRC-oriented shelf and can conceal the polynomial restriction; Singapore and Traditional-Chinese regional evidence are absent.",
        "The sense window, rather than the surface phrase alone, carries the polynomial restriction.",
    ),
    T(
        "Invariante",
        V("不变量", "不變量"),
        "source/P08_complete_lines5957_6347_LF_terminal.tex; title and section I throughout",
        "an invariant polynomial or form under the transformations under discussion",
        "A mathematical invariant in classical invariant theory, including the simultaneous invariants introduced in section I.",
        "an unchanged prose statement; a conserved physical quantity without the group action; an adjective meaning merely constant",
        ("不变式", "恒 invariant", "保形量"),
        "modern Sino-xenic coinage/calque",
        "不变量 is strongly normalized in Mainland mathematical prose, while 不变式 and regional historical usage were not researched.",
        "This base term does not settle every compound containing Invariant-.",
    ),
    T(
        "volles Invariantensystem / volles System",
        V("完全不变量系统", "完全不變量系統"),
        "source/P08_complete_lines5957_6347_LF_terminal.tex; introduction and section I after displays for F and A",
        "a complete finite generating system of invariants",
        "The system is complete in the stated generation sense: every relevant invariant is whole-rationally expressible through it.",
        "the literal set of every invariant; a complete metric space; a merely exhaustive bibliography; a closed dynamical system",
        ("完备不变量系统", "全不变量系", "完全系统"),
        "mixed/contested",
        "完全…系统 follows PRC-oriented completeness wording, but 完备 and shorter historical forms remain live attractors without regional evidence.",
        "The expanded form records the invariant-bearing noun even where running prose later shortens it.",
    ),
    T(
        "Simultaninvariante",
        V("同时不变量", "同時不變量"),
        "source/P08_complete_lines5957_6347_LF_terminal.tex; section I, Hilbert-conjecture paragraph and proof",
        "an invariant of several forms considered simultaneously",
        "The transformation acts on the whole displayed system of forms, and the invariant belongs to that joint action.",
        "a time-synchronous invariant; simultaneous equations; several unrelated invariants listed together",
        ("联立不变量", "联合不变量", "协同不变量"),
        "mixed/contested",
        "同时 is ordinary Mainland prose and may under-mark the historical technical compound; 联立/联合 and non-Mainland conventions remain untested.",
        "No Japanese or Korean cognate is used to authorize the Chinese selection.",
    ),
    T(
        "Reduktionssatz",
        (("归约定理", "歸約定理"), ("约化定理", "約化定理")),
        "source/P08_complete_lines5957_6347_LF_terminal.tex; introduction, sections I and II",
        "the named theorem reducing forms in arbitrarily many variable groups to polar forms using only n fixed groups",
        "The theorem is the algebraic reduction identity theta=sum PZ and its general proof, not a generic simplification step.",
        "reductio ad absurdum; reduction modulo an integer; chemical reduction; informal simplification",
        ("归约定理", "约化定理", "化归定理", "简约定理"),
        "mixed/contested",
        "The current producer segments expose a Mainland-internal 归约/约化 split; the generator refuses to freeze evidence until the final Hans and Hant targets use one corresponding pair.",
        "Final target occurrence binding resolves the surface only; independent terminology review remains pending.",
    ),
    T(
        "Form",
        V("形式", "形式"),
        "source/P08_complete_lines5957_6347_LF_terminal.tex; all three sections",
        "a homogeneous algebraic form in the classical invariant-theory sense",
        "A polynomial form with the row-wise homogeneity and degree properties stated locally.",
        "shape or visual appearance; a document form; differential form by default; a representation-theoretic module",
        ("型", "型式", "齐次多项式"),
        "mixed/contested",
        "形式 follows the inherited PRC shelf, while 型 and region-specific technical usage were not independently surveyed.",
        "The generic noun is constrained by the algebraic context at each source locus.",
    ),
    T(
        "Grundform",
        V("基本形式", "基本形式"),
        "source/P08_complete_lines5957_6347_LF_terminal.tex; title, introduction, and section I",
        "one of the base forms whose joint invariants form the object of study",
        "The forms F_i supply the initial system and their coefficients are taken as the variable groups A_i.",
        "a basic shape in geometry; a normal form; a foundational document template; a primitive differential form",
        ("基形式", "基础型", "原始形式"),
        "mixed/contested",
        "基本形式 is transparent PRC-oriented compounding but may compete with 基形式 or established regional historical terminology not present on the shelf.",
        "This record does not import the differential-form sense of 基本形式.",
    ),
    T(
        "Polarprozeß / Polarprozess",
        V("极化过程", "極化過程"),
        "source/P08_complete_lines5957_6347_LF_terminal.tex; introduction and sections I-II",
        "the displayed differential polarization operation and its finite compositions",
        "A classical invariant-theoretic differential process generated by the operators P_hk.",
        "physical polarization; political polarization; a polar-coordinate transformation; the resulting polar form itself",
        ("极化手续", "极化算子过程", "偏极化过程"),
        "modern Sino-xenic coinage/calque",
        "极化过程 is Mainland-normalized modern mathematical wording; historical and regional alternatives were not researched.",
        "The process is kept distinct from both the resulting Polare and the simple Polaroperation.",
    ),
    T(
        "Polare",
        V("极化式", "極化式"),
        "source/P08_complete_lines5957_6347_LF_terminal.tex; reduction theorem and section II",
        "a form obtained by applying polarization to another form",
        "The noun denotes the resulting polar form appearing in sums such as PZ, not the operation producing it.",
        "the polarization process; a polar set; a geometric polar line; a physical polar state",
        ("极形式", "极化形式", "偏极式"),
        "modern Sino-xenic coinage/calque",
        "极化式 is a concise PRC producer choice whose distinction from 极化形式 and regional vocabulary is not externally validated.",
        "The ledger preserves the operation/result distinction stated in the worker return.",
    ),
    T(
        "Polaroperation",
        V("极化运算", "極化運算"),
        "source/P08_complete_lines5957_6347_LF_terminal.tex; section I, product-rule argument",
        "one simple polarization operation P_hk in the finite succession making up P",
        "The local noun names an individual operation whose product rule expands products of invariants.",
        "the resulting polar form; an arbitrary algebraic operation; physical polarization; the whole composite process without distinction",
        ("极化操作", "极化算子", "偏极运算"),
        "modern Sino-xenic coinage/calque",
        "运算 is conventional Mainland operator prose, while 操作 and regional conventions were not independently sampled.",
        "The form is intentionally narrower than 极化过程.",
    ),
    T(
        "Rationalitätsbereich",
        (("有理域", "有理域"), ("有理性域", "有理性域")),
        "source/P08_complete_lines5957_6347_LF_terminal.tex; section I opening and section II definition/proof",
        "the prescribed coefficient domain K from which scalar quantities are drawn",
        "The historical Bereich is the local scalar domain containing or receiving coefficients; the source does not license one blanket modern field/ring classification at every occurrence.",
        "the field Q automatically; ordinary rationality or reasonableness; a geometric region; a probability domain",
        ("有理域", "有理性域", "有理性范围", "有理数域"),
        "mixed/contested",
        "The producer segments currently expose 有理域/有理性域 competition; both are PRC-readable, and neither supplies Singapore or Traditional regional authority.",
        "The generator requires one final Hans/Hant pair and leaves the historical algebraic typing to independent review.",
    ),
    T(
        "Koeffizientenbereich",
        V("系数域", "係數域"),
        "source/P08_complete_lines5957_6347_LF_terminal.tex; section II definition and family L",
        "the domain containing the coefficients of the forms under consideration",
        "The local coefficient domain is related to K as stated and is not silently identified with every rationality domain in the paper.",
        "a list of coefficients; a coefficient ring or field chosen without local evidence; a geometric coefficient region",
        ("系数范围", "系数体", "系数环"),
        "mixed/contested",
        "系数域 is compact Mainland algebra prose and can overstate field structure; ring/domain alternatives and regional usage remain unvalidated.",
        "This is an explicit type-risk window, not a German-source defect finding.",
    ),
    T(
        "rationale Zahlkoeffizienten / rationalzahlig",
        V("有理数系数", "有理數係數"),
        "source/P08_complete_lines5957_6347_LF_terminal.tex; section I definition of P and proof; section II families",
        "coefficients that are rational numbers",
        "The adjective specifies coefficients in Q and does not say integer-valued or integer-coefficient.",
        "integer coefficients; rational functions as coefficients; merely reasonable numerical coefficients",
        ("有理系数", "有理整数系数", "Q-系数"),
        "modern Sino-xenic coinage/calque",
        "有理数系数 makes the Q-scope explicit in PRC prose; compact forms and regional conventions were not independently checked.",
        "The inherited witness's integer-coefficient attractor is explicitly excluded.",
    ),
    T(
        "Reihe",
        V("变量组", "變量組"),
        "source/P08_complete_lines5957_6347_LF_terminal.tex; introduction and all three sections",
        "one indexed group of n variables or quantities, treated as a row-like unit",
        "Each A_k, x, y, or z is one grouped set of variables; the term is distinct from Reihenentwicklung.",
        "an infinite sequence or series; a displayed matrix row only; a column; a publication series",
        ("行", "系列", "变量列", "变量行"),
        "modern Sino-xenic coinage/calque",
        "变量组 is PRC-oriented explanatory wording; it avoids the matrix-row attractor but cannot establish Singapore usage or TW/HK/MO terminology.",
        "Controlled Hant 變量組 is script control, not a regional choice of 變量 versus 變數.",
    ),
    T(
        "Dimension einer Form in einer Reihe",
        V("次数", "次數"),
        "source/P08_complete_lines5957_6347_LF_terminal.tex; section II, definitions of the families L, S, and T",
        "the homogeneous degree of a form in one specified variable group",
        "The historical Dimension is row-wise polynomial degree, as shown by alpha, beta, p and the same-degree conditions.",
        "geometric dimension; vector-space dimension; the number of variables in the group; matrix size",
        ("维数", "分次", "关于该组的度数"),
        "mixed/contested",
        "次数 is ordinary PRC polynomial language, while 维数 is a strong literal witness attractor and regional historical usage is unknown.",
        "The short target form is interpreted only inside the explicit row-wise sense window.",
    ),
    T(
        "lineare Formenschar / lineare Schar",
        V("形式的线性族", "形式的線性族"),
        "source/P08_complete_lines5957_6347_LF_terminal.tex; section II opening and throughout",
        "a K-linear family of forms closed under the stated scalar linear combinations",
        "The family consists of forms of equal row-wise degree and is closed under c1 theta1+c2 theta2 over K.",
        "an analytic one-parameter pencil automatically; an infinite series; a family whose members are necessarily linear forms; a statistical cohort",
        ("线性形式族", "线性形式簇", "形式线性系"),
        "mixed/contested",
        "The expanded word order is PRC explanatory prose chosen to avoid reading every member as a linear form; historical Schar terminology and regional preferences remain untested.",
        "Running prose may shorten the established noun to 线性族 without changing this sense.",
    ),
    T(
        "Teilschar",
        V("子族", "子族"),
        "source/P08_complete_lines5957_6347_LF_terminal.tex; section II family comparison",
        "a subfamily contained in another linear family of forms",
        "The family T is included in L and equal rank is used to infer equality/equivalence.",
        "an algebraic subvariety; a subgroup; a subseries; a proper subset necessarily",
        ("子簇", "子形式族", "部分族"),
        "mixed/contested",
        "子族 follows the selected 族 terminology in PRC prose; 子簇 and regional mathematical conventions were not researched.",
        "No properness is implied by the compact prefix 子-.",
    ),
    T(
        "Rang",
        V("秩", "秩"),
        "source/P08_complete_lines5957_6347_LF_terminal.tex; section II definition and comparisons rho, sigma, tau",
        "the finite linear rank of a form family over the stated coefficient domain",
        "Rank counts a maximal linearly independent subfamily over K or R in the proof.",
        "polynomial degree or order; matrix rank without the family context; social rank; cardinality alone",
        ("阶", "级", "线性秩"),
        "Sino-xenic inherited",
        "秩 is entrenched PRC mathematical vocabulary but the compact graph leaves its family-over-domain arguments implicit; regional evidence is absent.",
        "The sense window excludes the neighboring degree terminology.",
    ),
    T(
        "identisch (äquivalent) / Äquivalenz",
        V("等价", "等價"),
        "source/P08_complete_lines5957_6347_LF_terminal.tex; section II preliminary fact and conclusion",
        "equality of the two linear families as systems, expressed as their equivalence in the argument",
        "The two families have the same members after inclusion and equal-rank arguments; the source parenthetically calls this equivalent.",
        "literal equality of individual formula strings; approximate equality; logical biconditional alone; isomorphism of unrelated structures",
        ("相同", "等同", "等价性"),
        "modern Sino-xenic coinage/calque",
        "等价 is normalized PRC mathematical prose and may blur the source's stronger local identity claim; regional conventions were not checked.",
        "The graph records the source pair rather than forcing one English-style relation globally.",
    ),
    T(
        "ein-eindeutiges Entsprechen",
        V("一一对应", "一一對應"),
        "source/P08_complete_lines5957_6347_LF_terminal.tex; section II, proof of Hilfssatz a",
        "a one-to-one correspondence between forms in S and forms in L",
        "The substitution map determines one corresponding form in each family and preserves the relevant relations both ways.",
        "mere injectivity; forward single-valuedness only; visual similarity; an arbitrary pairing",
        ("双射对应", "一对一对应", "唯一对应"),
        "modern Sino-xenic coinage/calque",
        "一一对应 is standard PRC prose but its bijective content can be read loosely; alternative regional formulations were not sampled.",
        "The local proof supplies the two-sided uniqueness window.",
    ),
    T(
        "Potenzprodukt",
        V("幂乘积", "冪乘積"),
        "source/P08_complete_lines5957_6347_LF_terminal.tex; section I proof and section II Hilfssatz b",
        "a monomial-like product of powers in the named invariants or differential operators",
        "The noun denotes products of powers in the displayed algebraic expansions, not arbitrary repeated multiplication prose.",
        "a power series; exponentiation alone; Cartesian product; a product measure",
        ("幂积", "单项式", "乘方积"),
        "modern Sino-xenic coinage/calque",
        "幂乘积 is explicit Mainland technical prose, while 幂积 and historical shorter forms remain unresearched outside the PRC shelf.",
        "The same surface is bounded by its local operands at each occurrence.",
    ),
    T(
        "Kongruenz modulo Delta / kongruent mod Delta",
        V("模 $\\Delta$ 的同余式", "模 $\\Delta$ 的同餘式"),
        "source/P08_complete_lines5957_6347_LF_terminal.tex; section III, equations (2) and the rank-mod-Delta argument",
        "polynomial congruence modulo the determinant Delta",
        "The relation is equality in the quotient modulo Delta and retains the source symbol \\equiv where supplied.",
        "ordinary equality; numerical congruence of integers only; geometric congruence; approximate equality",
        ("模 Delta 合同", "按 Delta 同余", "模 Delta 相等"),
        "modern Sino-xenic coinage/calque",
        "同余 is Mainland-normalized and strongly associated with integer arithmetic; the polynomial quotient sense and regional terminology require independent confirmation.",
        "This row records a target sense window, not a formula check or source correction.",
    ),
    T(
        "Determinante",
        V("行列式", "行列式"),
        "source/P08_complete_lines5957_6347_LF_terminal.tex; section III throughout",
        "the determinant Delta or determinant combinations formed from the variable groups",
        "The determinant is the alternating polynomial appearing as Delta and in the indexed determinant factors.",
        "a determining cause; matrix rank; an arbitrary scalar factor; a Jacobian unless locally specified",
        ("判别式", "定值式", "determinant"),
        "Sino-xenic inherited",
        "行列式 is shared modern CJK mathematical vocabulary but the Chinese evidence shelf is PRC-dominant and does not authorize any regional prose beyond this lexical record.",
        "Symbolic determinant notation remains source notation and is not lexical evidence by itself.",
    ),
    T(
        "Reihenentwicklung",
        V("级数展开", "級數展開"),
        "source/P08_complete_lines5957_6347_LF_terminal.tex; introduction and section III",
        "the historical invariant-theoretic algebraic development into polar and determinant terms",
        "In section III the displayed development is algebraic and finite at the stated stage; the noun does not itself assert analytic convergence.",
        "a matrix-row expansion; an ordered sequence; necessarily an infinite analytic power series; a publication series",
        ("展开", "序列展开", "行展开", "级数发展式"),
        "modern Sino-xenic coinage/calque",
        "级数 strongly attracts the modern analytic-series reading in PRC prose; historical and regional alternatives remain unvalidated.",
        "The adverse ledger keeps the analytic-convergence attractor visible for the checker.",
    ),
    T(
        "allgemeinste Reihenentwicklung",
        V("最一般级数展开", "最一般級數展開"),
        "source/P08_complete_lines5957_6347_LF_terminal.tex; section III after equation (3)",
        "the most general algebraic development of a form into polar forms with successively fewer variable groups",
        "The superlative describes the scope of the constructed invariant-theoretic expansion, not convergence maximality or a unique analytic series.",
        "the most general infinite series; a Taylor expansion; a matrix Laplace expansion; an asymptotic expansion",
        ("最一般展开", "一般展开式", "最广义级数展开"),
        "modern Sino-xenic coinage/calque",
        "The PRC surface inherits the analytic attractor of 级数 and adds a literal superlative; no regional historical corpus was consulted.",
        "This decision is separate from the base Reihenentwicklung row because the scope claim is trap-prone.",
    ),
    T(
        "Omega-Prozeß",
        V("$\\Omega$ 过程", "$\\Omega$ 過程"),
        "source/P08_complete_lines5957_6347_LF_terminal.tex; section III, Hilfssatz c and iterative expansion",
        "the specifically named Omega differential process acting on the polar forms",
        "Only the source-named Omega operation receives this label; Omega and nabla remain distinct notations and processes.",
        "a generic asymptotic big-O operation; the nabla operator; an angular frequency; any polarization process",
        ("Omega 算子", "Omega 运算", "奥米伽过程"),
        "mixed/contested",
        "The symbol-plus-过程 construction is PRC-oriented explanatory prose; spoken-name and regional operator conventions were not researched.",
        "The script does not infer mathematical equivalence between source operators.",
    ),
    T(
        "Multiplikator von Delta",
        V("乘子", "乘子"),
        "source/P08_complete_lines5957_6347_LF_terminal.tex; section III after Hilfssatz c",
        "the factor multiplying Delta in the iterative decomposition",
        "The local Multiplikator is the factor of Delta to which identity (2) is applied, not an unrestricted scalar-multiplier claim.",
        "a Lagrange multiplier automatically; a group multiplier; a numerical multiplicand only; a differential operator",
        ("乘因子", "因子", "倍乘量"),
        "Sino-xenic inherited",
        "乘子 is compact Mainland mathematical prose with strong Lagrange/group-theory attractors; the historical local term and regional preferences remain unchecked.",
        "The factor-of-Delta window is mandatory for this surface.",
    ),
    T(
        "kogrediente Variabeln",
        V("同变变量", "同變變量"),
        "source/P08_complete_lines5957_6347_LF_terminal.tex; final sentence of section III",
        "variables transforming cogrediently under the same transformation behavior",
        "The historical adjective concerns how the several variable groups transform together in the invariant-theory setting.",
        "tensor-index covariance automatically; an ordinary same-direction relation; equivariance of a map; contragredient variables",
        ("协变变量", "等变变量", "同向变量"),
        "mixed/contested",
        "同变 is a provisional PRC calque; 协变 and 等变 are strong modern attractors, and no Taiwan/Hong Kong/Macao or Singapore terminology evidence was consulted.",
        "Independent historical-mathematical review is required; the graph makes no readiness claim.",
    ),
)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def relative_to_root(path: Path) -> str:
    resolved = path.resolve()
    root = ROOT.resolve()
    try:
        return resolved.relative_to(root).as_posix()
    except ValueError as exc:
        raise RuntimeError(f"Path must remain inside the P08 root: {resolved}") from exc


def validate_fixed_inputs() -> dict[str, dict[str, str | int]]:
    evidence: dict[str, dict[str, str | int]] = {}
    for key, (path, expected_hash) in FIXED_INPUTS.items():
        if not path.is_file():
            raise FileNotFoundError(f"Required fixed input is absent: {path}")
        actual_hash = sha256_file(path)
        if actual_hash != expected_hash:
            raise RuntimeError(
                f"Fixed-input hash mismatch for {key}: expected {expected_hash}, got {actual_hash}"
            )
        evidence[key] = {
            "path": relative_to_root(path),
            "bytes": path.stat().st_size,
            "sha256": actual_hash,
        }
    return evidence


def validate_terms() -> None:
    if len(TERMS) < 20:
        raise RuntimeError("The P08 trap-concept shelf must contain at least 20 decisions")
    german_labels: set[str] = set()
    for index, term in enumerate(TERMS, 1):
        if term.german in german_labels:
            raise RuntimeError(f"Duplicate German decision label: {term.german}")
        german_labels.add(term.german)
        if not term.variants:
            raise RuntimeError(f"Decision {index} has no Hans/Hant surface pair")
        if len(set(term.variants)) != len(term.variants):
            raise RuntimeError(f"Decision {index} repeats a Hans/Hant surface pair")
        if any(not hans or not hant for hans, hant in term.variants):
            raise RuntimeError(f"Decision {index} has an empty Hans or Hant surface")
        if not term.sense or not term.excluded or not term.alternatives:
            raise RuntimeError(f"Decision {index} lacks sense, adverse, or alternative evidence")
        if term.basin not in ALLOWED_BASINS:
            raise RuntimeError(f"Decision {index} uses invalid lexical-attractor basin {term.basin!r}")
        if not term.debt or not term.note:
            raise RuntimeError(f"Decision {index} lacks qualitative debt or producer note")


def read_target(path_arg: str, label: str) -> tuple[Path, str, str]:
    path = Path(path_arg)
    if not path.is_absolute():
        path = ROOT / path
    path = path.resolve()
    relative_to_root(path)
    if not path.is_file():
        raise FileNotFoundError(f"Final {label} target is absent: {path}")
    if path.suffix.lower() != ".tex":
        raise RuntimeError(f"Final {label} target must be editable TeX: {path}")
    data = path.read_bytes()
    if not data:
        raise RuntimeError(f"Final {label} target is empty: {path}")
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise RuntimeError(f"Final {label} target is not UTF-8: {path}") from exc
    return path, text, hashlib.sha256(data).hexdigest().upper()


def bind_terms(hans_text: str, hant_text: str) -> tuple[BoundTerm, ...]:
    bound: list[BoundTerm] = []
    failures: list[str] = []
    for index, term in enumerate(TERMS, 1):
        matches = [
            (hans, hant)
            for hans, hant in term.variants
            if hans in hans_text and hant in hant_text
        ]
        if len(matches) != 1:
            variants = "; ".join(f"{hans} / {hant}" for hans, hant in term.variants)
            failures.append(
                f"P08-ZH-T{index:03d}: expected exactly one corresponding final-target pair "
                f"from [{variants}], found {len(matches)}"
            )
            continue
        hans, hant = matches[0]
        bound.append(BoundTerm(term=term, hans=hans, hant=hant))
    if failures:
        raise RuntimeError("Final-target terminology binding failed:\n" + "\n".join(failures))
    return tuple(bound)


def alternatives_for(bound: BoundTerm) -> str:
    pool = list(bound.term.alternatives)
    for hans, _ in bound.term.variants:
        if hans != bound.hans and hans not in pool:
            pool.append(hans)
    return "; ".join(item for item in pool if item != bound.hans)


def make_term_rows(bound_terms: Sequence[BoundTerm]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for index, bound in enumerate(bound_terms, 1):
        term = bound.term
        rows.append(
            {
                "decision_id": f"P08-ZH-T{index:03d}",
                "source_locator": term.locator,
                "exact_german_phrase": term.german,
                "concept_scope": term.scope,
                "zh_hans_cn_choice": bound.hans,
                "sense_window": term.sense,
                "excluded_senses": term.excluded,
                "alternatives_considered": alternatives_for(bound),
                "lexical_attractor_basin": term.basin,
                "mandarin_simplified_dominance_risk_debt": term.debt,
                "evidence_class": EVIDENCE_CLASS,
                "controlled_hant_form": bound.hant,
                "controlled_hant_status": HANT_STATUS,
                "independent_check_status": REVIEW_STATE,
                "producer_note": term.note,
            }
        )
    return rows


def make_adverse_rows(bound_terms: Sequence[BoundTerm]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for index, bound in enumerate(bound_terms, 1):
        term = bound.term
        rows.append(
            {
                "adverse_id": f"P08-ZH-A{index:03d}",
                "term_decision_id": f"P08-ZH-T{index:03d}",
                "source_locator": term.locator,
                "exact_german_phrase": term.german,
                "zh_hans_cn_producer_choice": bound.hans,
                "trap_or_adverse_reading": term.excluded,
                "contextual_reason_for_exclusion": term.sense,
                "alternative_held_for_independent_review": alternatives_for(bound),
                "lexical_attractor_basin": term.basin,
                "mandarin_simplified_dominance_risk_debt": term.debt,
                "evidence_class": EVIDENCE_CLASS,
                "controlled_hant_status": HANT_STATUS,
                "review_state": REVIEW_STATE,
            }
        )
    return rows


def make_crosswalk_rows(bound_terms: Sequence[BoundTerm]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for index, bound in enumerate(bound_terms, 1):
        term = bound.term
        rows.append(
            {
                "crosswalk_id": f"P08-ZH-X{index:03d}",
                "term_decision_id": f"P08-ZH-T{index:03d}",
                "source_locator": term.locator,
                "exact_german_phrase": term.german,
                "zh_hans_cn_producer_form": bound.hans,
                "zh_hant_controlled_form": bound.hant,
                "zh_hant_status": HANT_STATUS,
                "ja_form": "",
                "ko_form": "",
                "ja_ko_evidence_status": JA_KO_STATUS,
                "sense_window": term.sense,
                "excluded_senses": term.excluded,
                "lexical_attractor_basin": term.basin,
                "mandarin_simplified_dominance_risk_debt": term.debt,
                "evidence_class": EVIDENCE_CLASS,
                "independent_check_status": REVIEW_STATE,
            }
        )
    return rows


def make_graph(
    bound_terms: Sequence[BoundTerm],
    fixed: dict[str, dict[str, str | int]],
    hans_path: Path,
    hans_hash: str,
    hant_path: Path,
    hant_hash: str,
) -> dict:
    nodes: list[dict] = []
    edges: list[dict[str, str]] = []
    source_file = fixed["sealed_source"]["path"]
    for index, bound in enumerate(bound_terms, 1):
        suffix = f"{index:03d}"
        locus_id = f"P08-LOC-{suffix}"
        concept_id = f"P08-CON-{suffix}"
        hans_id = f"P08-HANS-{suffix}"
        hant_id = f"P08-HANT-{suffix}"
        choice_id = f"P08-CHOICE-{suffix}"
        nodes.extend(
            [
                {
                    "id": locus_id,
                    "type": "source_locus",
                    "locator": bound.term.locator,
                    "exact_german_phrase": bound.term.german,
                    "source_file": source_file,
                },
                {
                    "id": concept_id,
                    "type": "concept",
                    "scope": bound.term.scope,
                    "sense_window": bound.term.sense,
                    "excluded_senses": bound.term.excluded,
                },
                {
                    "id": hans_id,
                    "type": "form",
                    "language_scope": "zh-Hans-CN PRC-oriented producer",
                    "form": bound.hans,
                    "status": REVIEW_STATE,
                },
                {
                    "id": hant_id,
                    "type": "form",
                    "language_scope": "zh-Hant-controlled nonregional producer record",
                    "form": bound.hant,
                    "status": HANT_STATUS,
                },
                {
                    "id": choice_id,
                    "type": "producer_choice",
                    "decision_id": f"P08-ZH-T{suffix}",
                    "alternatives_considered": alternatives_for(bound).split("; "),
                    "lexical_attractor_basin": bound.term.basin,
                    "mandarin_simplified_dominance_risk_debt": bound.term.debt,
                    "evidence_class": EVIDENCE_CLASS,
                    "review_state": REVIEW_STATE,
                },
            ]
        )
        edges.extend(
            [
                {"id": f"P08-E{suffix}-1", "type": "occurs_at", "from": concept_id, "to": locus_id},
                {"id": f"P08-E{suffix}-2", "type": "decides_for", "from": choice_id, "to": concept_id},
                {"id": f"P08-E{suffix}-3", "type": "selects_hans_form", "from": choice_id, "to": hans_id},
                {
                    "id": f"P08-E{suffix}-4",
                    "type": "records_controlled_hant_form",
                    "from": choice_id,
                    "to": hant_id,
                },
                {"id": f"P08-E{suffix}-5", "type": "controlled_form_of", "from": hant_id, "to": hans_id},
            ]
        )

    generator_hash = sha256_file(Path(__file__))
    return {
        "graph_id": "NOE-P08-ZH-PRODUCER-CONCEPT-GRAPH-001",
        "work_unit": "Noether Paper 8 Chinese producer translation",
        "graph_status": {
            "purpose": "producer-side translation-decision evidence packaging only",
            "decision_count": len(bound_terms),
            "independent_check": REVIEW_STATE,
            "external_native_source_research": "not performed",
            "japanese_or_korean_evidence": JA_KO_STATUS,
            "scan_inspection": "not performed",
            "source_branch_comparison_or_german_adjudication": "not performed",
            "semantic_formula_or_terminology_checking": "not performed",
            "compilation_or_rendering": "not performed by this evidence generator",
            "controlled_hant_scope": HANT_STATUS,
            "zh_hans_sg_scope": "absent; not produced or authorized",
            "regional_localization_scope": "zh-Hant-TW/HK/MO absent; no regional prose claim",
            "translation_validation_or_readiness_claim": "none",
        },
        "provenance": {
            "sealed_translation_source": {
                **fixed["sealed_source"],
                "use": "translation-source terminology and locators only; no German-source adjudication",
            },
            "inherited_hans_witness": {
                **fixed["inherited_hans_witness"],
                "use": "translation witness and adverse evidence only; not authority",
            },
            "translation_notes": {
                **fixed["translation_notes"],
                "use": "producer trap-concept routing and explicit review debt",
            },
            "completed_worker_returns": {
                "paths": [fixed["return_s01"]["path"], fixed["return_s03"]["path"]],
                "sha256": [fixed["return_s01"]["sha256"], fixed["return_s03"]["sha256"]],
                "use": "producer choices, alternatives, sense windows, and adverse attractors only",
            },
            "hans_target": {
                "path": relative_to_root(hans_path),
                "bytes": hans_path.stat().st_size,
                "sha256": hans_hash,
                "use": "final PRC-oriented producer target supplied at generation time; independent check pending",
            },
            "controlled_hant_target": {
                "path": relative_to_root(hant_path),
                "bytes": hant_path.stat().st_size,
                "sha256": hant_hash,
                "use": HANT_STATUS,
            },
            "evidence_generator": {
                "path": "qa/evidence.py",
                "bytes": Path(__file__).stat().st_size,
                "sha256": generator_hash,
                "use": "deterministic packaging into the established 15/13/16-field CSV and typed-graph shapes",
            },
            "evidence_class": EVIDENCE_CLASS,
        },
        "node_type_definitions": {
            "source_locus": "Locator and German phrase in the sealed translation unit; not a German-source validation assertion.",
            "concept": "Producer's explicit bounded sense window and excluded lexical attractors.",
            "form": "Producer Chinese form with explicit PRC-oriented Hans or nonregional controlled-Hant scope.",
            "producer_choice": "Producer selection with alternatives, provisional lexical-attractor basin, qualitative Mandarin-Simplified dominance debt, and open independent-review state.",
        },
        "edge_type_definitions": {
            "occurs_at": "Concept to sealed translation-source locator.",
            "decides_for": "Producer choice to concept.",
            "selects_hans_form": "Producer choice to PRC-oriented Hans form.",
            "records_controlled_hant_form": "Producer choice to nonregional controlled-Hant form.",
            "controlled_form_of": "Controlled-Hant script form to Hans lexical base without Taiwan/Hong Kong/Macao equivalence claim.",
        },
        "nodes": nodes,
        "edges": edges,
    }


NODE_KEYS = {
    "source_locus": {"id", "type", "locator", "exact_german_phrase", "source_file"},
    "concept": {"id", "type", "scope", "sense_window", "excluded_senses"},
    "form": {"id", "type", "language_scope", "form", "status"},
    "producer_choice": {
        "id",
        "type",
        "decision_id",
        "alternatives_considered",
        "lexical_attractor_basin",
        "mandarin_simplified_dominance_risk_debt",
        "evidence_class",
        "review_state",
    },
}
EDGE_KEYS = {"id", "type", "from", "to"}
GRAPH_KEYS = {
    "graph_id",
    "work_unit",
    "graph_status",
    "provenance",
    "node_type_definitions",
    "edge_type_definitions",
    "nodes",
    "edges",
}


def validate_rows(headers: Sequence[str], rows: Sequence[dict[str, str]], label: str) -> None:
    expected = set(headers)
    for index, row in enumerate(rows, 1):
        if list(row.keys()) != list(headers):
            raise RuntimeError(f"{label} row {index} does not preserve the established field order")
        if set(row) != expected:
            raise RuntimeError(f"{label} row {index} has invalid fields")


def validate_graph(graph: dict, decision_count: int) -> dict[str, int | bool]:
    if set(graph) != GRAPH_KEYS:
        raise RuntimeError(f"Graph top-level fields differ from the established shape: {set(graph)}")
    nodes = graph["nodes"]
    edges = graph["edges"]
    if len(nodes) != decision_count * 5 or len(edges) != decision_count * 5:
        raise RuntimeError("Graph must contain exactly five nodes and five edges per decision")
    node_ids: list[str] = []
    for node in nodes:
        node_type = node.get("type")
        if node_type not in NODE_KEYS:
            raise RuntimeError(f"Unknown node type: {node_type!r}")
        if set(node) != NODE_KEYS[node_type]:
            raise RuntimeError(f"Invalid fields for {node_type} node {node.get('id')}: {set(node)}")
        node_ids.append(node["id"])
    edge_ids: list[str] = []
    for edge in edges:
        if set(edge) != EDGE_KEYS:
            raise RuntimeError(f"Invalid edge fields for {edge.get('id')}: {set(edge)}")
        if edge["type"] not in graph["edge_type_definitions"]:
            raise RuntimeError(f"Unknown edge type in {edge['id']}: {edge['type']}")
        edge_ids.append(edge["id"])
    if len(node_ids) != len(set(node_ids)):
        raise RuntimeError("Duplicate graph node ID")
    if len(edge_ids) != len(set(edge_ids)):
        raise RuntimeError("Duplicate graph edge ID")
    node_id_set = set(node_ids)
    dangling = [
        edge["id"]
        for edge in edges
        if edge["from"] not in node_id_set or edge["to"] not in node_id_set
    ]
    if dangling:
        raise RuntimeError(f"Dangling graph references: {dangling}")
    for index in range(1, decision_count + 1):
        suffix = f"{index:03d}"
        node_prefixes = {
            f"P08-LOC-{suffix}",
            f"P08-CON-{suffix}",
            f"P08-HANS-{suffix}",
            f"P08-HANT-{suffix}",
            f"P08-CHOICE-{suffix}",
        }
        if not node_prefixes.issubset(node_id_set):
            raise RuntimeError(f"Incomplete five-node group for decision {suffix}")
        group_edges = [edge for edge in edges if edge["id"].startswith(f"P08-E{suffix}-")]
        if len(group_edges) != 5:
            raise RuntimeError(f"Incomplete five-edge group for decision {suffix}")
    return {
        "unique_node_ids": True,
        "unique_edge_ids": True,
        "dangling_references": 0,
        "nodes": len(nodes),
        "edges": len(edges),
    }


def csv_bytes(headers: Sequence[str], rows: Sequence[dict[str, str]]) -> bytes:
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=headers, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return buffer.getvalue().encode("utf-8")


def json_bytes(value: dict) -> bytes:
    return (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def atomic_write(path: Path, data: bytes) -> None:
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_bytes(data)
    temporary.replace(path)


def output_receipt(paths: Iterable[Path]) -> dict[str, dict[str, str | int]]:
    receipt: dict[str, dict[str, str | int]] = {}
    for path in paths:
        receipt[relative_to_root(path)] = {
            "bytes": path.stat().st_size,
            "sha256": sha256_file(path),
        }
    return receipt


def validation_only_report(fixed: dict[str, dict[str, str | int]]) -> dict:
    synthetic = tuple(BoundTerm(term=term, hans=term.variants[0][0], hant=term.variants[0][1]) for term in TERMS)
    term_rows = make_term_rows(synthetic)
    adverse_rows = make_adverse_rows(synthetic)
    crosswalk_rows = make_crosswalk_rows(synthetic)
    validate_rows(TERM_HEADERS, term_rows, "terms")
    validate_rows(ADVERSE_HEADERS, adverse_rows, "adverse")
    validate_rows(CROSSWALK_HEADERS, crosswalk_rows, "crosswalk")
    dummy_target = FIXED_INPUTS["sealed_source"][0]
    graph = make_graph(
        synthetic,
        fixed,
        dummy_target,
        str(fixed["sealed_source"]["sha256"]),
        dummy_target,
        str(fixed["sealed_source"]["sha256"]),
    )
    graph_metrics = validate_graph(graph, len(TERMS))
    return {
        "mode": "validation-only",
        "decision_count": len(TERMS),
        "term_fields": len(TERM_HEADERS),
        "adverse_fields": len(ADVERSE_HEADERS),
        "crosswalk_fields": len(CROSSWALK_HEADERS),
        "expected_nodes": len(TERMS) * 5,
        "expected_edges": len(TERMS) * 5,
        "graph_metrics": graph_metrics,
        "fixed_inputs": fixed,
        "required_generation_arguments": ["--hans", "--hant"],
        "planned_outputs": [relative_to_root(path) for path in OUTPUTS.values()],
        "files_written": [],
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Generate the Paper 8 producer terminology, adverse-sense, CJKV crosswalk, "
            "and typed concept-graph evidence after final Hans and Hant TeX paths exist."
        )
    )
    parser.add_argument("--hans", help="Final zh-Hans-CN TeX path, absolute or relative to the P08 root")
    parser.add_argument("--hant", help="Final controlled-generic zh-Hant TeX path, absolute or relative to the P08 root")
    parser.add_argument(
        "--validate-only",
        action="store_true",
        help="Validate fixed inputs, decision data, and CSV field shapes without creating evidence outputs",
    )
    args = parser.parse_args()
    if args.validate_only:
        if args.hans or args.hant:
            parser.error("--validate-only cannot be combined with --hans or --hant")
    elif not args.hans or not args.hant:
        parser.error("generation requires both --hans and --hant; use --validate-only before targets exist")
    return args


def main() -> None:
    args = parse_args()
    validate_terms()
    fixed = validate_fixed_inputs()
    if args.validate_only:
        # This path deliberately creates no final evidence artifact while targets are absent.
        report = validation_only_report(fixed)
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return

    hans_path, hans_text, hans_hash = read_target(args.hans, "Hans")
    hant_path, hant_text, hant_hash = read_target(args.hant, "Hant")
    if hans_path == hant_path:
        raise RuntimeError("Hans and Hant targets must be distinct files")
    bound_terms = bind_terms(hans_text, hant_text)

    term_rows = make_term_rows(bound_terms)
    adverse_rows = make_adverse_rows(bound_terms)
    crosswalk_rows = make_crosswalk_rows(bound_terms)
    graph = make_graph(bound_terms, fixed, hans_path, hans_hash, hant_path, hant_hash)

    validate_rows(TERM_HEADERS, term_rows, "terms")
    validate_rows(ADVERSE_HEADERS, adverse_rows, "adverse")
    validate_rows(CROSSWALK_HEADERS, crosswalk_rows, "crosswalk")
    graph_metrics = validate_graph(graph, len(bound_terms))

    payloads = {
        OUTPUTS["terms"]: csv_bytes(TERM_HEADERS, term_rows),
        OUTPUTS["adverse"]: csv_bytes(ADVERSE_HEADERS, adverse_rows),
        OUTPUTS["crosswalk"]: csv_bytes(CROSSWALK_HEADERS, crosswalk_rows),
        OUTPUTS["graph"]: json_bytes(graph),
    }
    EVIDENCE_DIR.mkdir(parents=True, exist_ok=True)
    for path, data in payloads.items():
        atomic_write(path, data)

    print(
        json.dumps(
            {
                "mode": "generated",
                "decision_count": len(bound_terms),
                "rows_each_csv": len(bound_terms),
                **graph_metrics,
                "hans_target": {
                    "path": relative_to_root(hans_path),
                    "bytes": hans_path.stat().st_size,
                    "sha256": hans_hash,
                },
                "hant_target": {
                    "path": relative_to_root(hant_path),
                    "bytes": hant_path.stat().st_size,
                    "sha256": hant_hash,
                },
                "outputs": output_receipt(OUTPUTS.values()),
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
