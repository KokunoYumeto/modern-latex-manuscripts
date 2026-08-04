from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE_DIR = ROOT / "evidence"

SOURCE_PATH = ROOT / "source" / "Noether_Paper21_German_current_exact_CRLF.tex"
WITNESS_PATH = ROOT / "witness" / "Noether_Paper21_SimplifiedChinese_inherited_content_exact_CRLF.tex"
HANS_PATH = ROOT / "zh-Hans-CN" / "Noether_Paper21_Chinese_CurrentAuthority_zh-Hans-CN_v001.tex"
HANT_PATH = ROOT / "zh-Hant-controlled" / "Noether_Paper21_Chinese_CurrentAuthority_zh-Hant-controlled_v001.tex"

EXPECTED_SOURCE_SHA256 = "C91672CA4BB8EFEB092EDD278A4F97B6E3E94AE2059144F4FFDDA524AAF7FB96"
EXPECTED_WITNESS_SHA256 = "75DB55DDA93F5C68C833D77C890DA0CAC6E7B22CB0769021799B5CAD335EAE41"
EXPECTED_HANS_SHA256 = "F4BCD4C27ED724EA4D79B1EAC0E427E370E2CB5BA1970200B1FD7A26D58E8235"
EXPECTED_HANT_SHA256 = "09ECD8499AAF75027554FF51069E4C9D054D2D617A4176307F4E01000A81C9E4"

EVIDENCE_CLASS = (
    "supplied producer editorial choice instantiated in the assembled Hans target; "
    "inherited Simplified-Chinese drafting witness bound but not treated as authority; "
    "independent checking absent"
)
HANT_STATUS = (
    "controlled generic script derivative only; not zh-Hant-TW/HK/MO; "
    "regional lexical localization absent"
)
REVIEW_STATE = "independent check absent; pending"
JA_KO_STATUS = "JA and KO not consulted and not authorized as Chinese evidence"


TERMS = [
    {
        "german": "formale Variationsrechnung",
        "hans": "形式变分法",
        "hant": "形式變分法",
        "locator": "source snapshot lines 1, 9, and 11; segment A",
        "scope": "formal calculus-of-variations method used to organize the stated invariant constructions",
        "sense": "A formal method of variational calculus in the paper's mathematical discussion, including formal variation and integration-by-parts operations.",
        "excluded": "informal variation; typographical variants; numerical perturbation alone; bookkeeping calculation unrelated to variational calculus",
        "alternatives": "形式变分演算; 形式变分计算; 形式变分学",
        "basin": "modern Sino-xenic coinage/calque",
        "debt": "Medium: 形式变分法 follows compact PRC mathematical compounding, while 演算 and 计算 are competing renderings and non-Mainland historical usage is untested.",
        "note": "The supplied producer form is recorded as a bounded Hans choice, not validated as a uniquely correct or regionally neutral term.",
    },
    {
        "german": "Differentialinvariante",
        "hans": "微分不变量",
        "hant": "微分不變量",
        "locator": "source snapshot lines 1, 3, 9, 11, and 80; segments A and C",
        "scope": "invariant formed from differential data under the transformations discussed in the paper",
        "sense": "A mathematical invariant involving differential expressions and the transformation framework of the paper.",
        "excluded": "an ordinary differential; a constant of integration; a derivative that happens not to vary; a generic invariant with no differential structure",
        "alternatives": "微分不变式; 微分恒量; differential invariant",
        "basin": "modern Sino-xenic coinage/calque",
        "debt": "Medium: 不变量 is strongly normalized in Mainland mathematical prose, while 不变式 remains a live attractor and regional historical preferences were not researched.",
        "note": "The record distinguishes the supplied noun from ordinary differentials and makes no external terminology-certification claim.",
    },
    {
        "german": "Variationsproblem",
        "hans": "变分问题",
        "hant": "變分問題",
        "locator": "source snapshot lines 17, 80, 82, and 84; segments A and C",
        "scope": "problem posed through variation of an integral or differential expression in the stated formal framework",
        "sense": "A calculus-of-variations problem whose extremal or invariance structure is under discussion.",
        "excluded": "statistical variance; textual variation; a generic change-management problem; arbitrary optimization without variational structure",
        "alternatives": "变分课题; 泛函极值问题; 变分原理问题",
        "basin": "modern Sino-xenic coinage/calque",
        "debt": "Low-to-medium: 变分问题 is conventional PRC mathematical wording but its register and competing terminology outside Mainland usage were not researched.",
        "note": "The supplied compact compound is preserved without treating it as evidence for any Traditional-Chinese regional standard.",
    },
    {
        "german": "Lagrangescher Ausdruck",
        "hans": "Lagrange 表达式",
        "hant": "Lagrange 表達式",
        "locator": "source snapshot line 24, with plural inflection; segment A",
        "scope": "the named expressions psi_i occurring in the formal variational identity",
        "sense": "The Lagrange-associated expressions denoted by psi_i in the paper's variational equations.",
        "excluded": "the Lagrangian function itself; Lagrange multipliers; Lagrange interpolation; any algebraic expression merely written by Lagrange",
        "alternatives": "拉格朗日表达式; Lagrange 式; 欧拉—拉格朗日表达式",
        "basin": "mixed/contested",
        "debt": "High: the Latin surname plus 表达式 format is Mainland-oriented mixed notation; 拉格朗日 and more specific Euler–Lagrange labels are competing attractors, and regional naming was not researched.",
        "note": "The supplied form is recorded exactly; whether a longer historical name is preferable is left to independent review.",
    },
    {
        "german": "kontragredient",
        "hans": "逆变",
        "hant": "逆變",
        "locator": "source snapshot lines 24 and 47; segment A",
        "scope": "contragredient transformation behavior assigned to the relevant expressions or vectors",
        "sense": "Transformation in the contragredient manner relative to the differential variables named in context.",
        "excluded": "an inverse function; an arbitrary reversal; matrix inversion by itself; a merely opposite change",
        "alternatives": "反变; 逆协变; 对偶变换",
        "basin": "modern Sino-xenic coinage/calque",
        "debt": "High: 逆变 is a terse Mainland technical form and can attract the broader tensor sense of contravariance; 反变 and fuller phrases were not regionally investigated.",
        "note": "The graph records only the supplied producer choice and its sense boundary, not a judgment between tensor-era terminologies.",
    },
    {
        "german": "kogredient",
        "hans": "协变",
        "hant": "協變",
        "locator": "source snapshot lines 35, 52, and 58; segments A and B",
        "scope": "cogredient transformation behavior assigned to the indicated differential operator or vector",
        "sense": "Transformation in the same or cogredient manner in the paper's paired transformation language.",
        "excluded": "statistical covariance; collaboration or coordinated change; covariant differentiation itself; mere simultaneous variation",
        "alternatives": "共变; 同变; 协同变换",
        "basin": "modern Sino-xenic coinage/calque",
        "debt": "High: 协变 is entrenched in Mainland tensor vocabulary and may collapse the historical kogredient/covariant distinction; 共变 and 同变 remain untested alternatives.",
        "note": "No semantic adjudication of the historical transformation pair is made in this packaging subtask.",
    },
    {
        "german": "Lagrangesche Zentralgleichung",
        "hans": "Lagrange 中心方程",
        "hant": "Lagrange 中心方程",
        "locator": "source snapshot lines 24 and 68; segment A and segment B",
        "scope": "the named central equation or identity used to define and generalize the formal expressions",
        "sense": "The historically named Lagrange central equation in the paper's formal variational construction.",
        "excluded": "a central-force equation; the central limit theorem; an arbitrary equation placed centrally on the page; the Euler–Lagrange equation without the historical label",
        "alternatives": "拉格朗日中心方程; Lagrange 中心恒等式; 拉格朗日中心等式",
        "basin": "mixed/contested",
        "debt": "High: the mixed Latin-name construction and literal 中心方程 are Mainland-oriented producer wording; whether 恒等式 better fits the local use and how regions name it remain unchecked.",
        "note": "The supplied form is preserved as a decision record, with the equation-versus-identity attractor left explicit.",
    },
    {
        "german": "geodätische Linie",
        "hans": "测地线",
        "hant": "測地線",
        "locator": "source snapshot lines 56, 80, and 82, with plural inflection; segments A and C",
        "scope": "geodesic curves arising from the displayed differential equations and coordinate construction",
        "sense": "A geodesic line or curve in the differential-geometric setting of the paper.",
        "excluded": "a surveying line on the Earth's surface alone; any visually shortest segment; a straight line in Euclidean coordinates without the geometric structure",
        "alternatives": "测地曲线; 短程线; 测地线路",
        "basin": "modern Sino-xenic coinage/calque",
        "debt": "Medium: 测地线 is Mainland-standard modern geometry vocabulary; 測地線 is only a generic script derivative here and regional historical choices were not researched.",
        "note": "The record does not claim that the generic Hant script form establishes Taiwan, Hong Kong, or Macao usage.",
    },
    {
        "german": "kovariante Ableitung",
        "hans": "协变导数",
        "hant": "協變導數",
        "locator": "source snapshot lines 58, 62, 68, 78, and 80; segments B and C",
        "scope": "covariant derivative constructed by eliminating higher differentials as described",
        "sense": "The differential-geometric covariant derivative operation applied to the forms in the paper.",
        "excluded": "ordinary derivative; statistical covariance derivative; a derivative that is merely coordinate-independent; cogredient behavior without differentiation",
        "alternatives": "共变导数; 协变微分; 共变微分",
        "basin": "modern Sino-xenic coinage/calque",
        "debt": "High: 协变导数 is strongly Mainland-normalized terminology; 共变 and 微分 variants are known lexical attractors, and no regional evidence shelf was consulted.",
        "note": "The supplied producer choice is recorded without independently checking its historical or regional register.",
    },
    {
        "german": "Krümmungsform",
        "hans": "曲率形式",
        "hant": "曲率形式",
        "locator": "source snapshot lines 64, 78, and 80; segments B and C",
        "scope": "the curvature form K/Omega construction described in the variational development",
        "sense": "A curvature-associated mathematical form produced by the stated invariant construction.",
        "excluded": "scalar curvature alone; the visual shape of a curve; a generic differential form unrelated to curvature; a curvature formula as prose",
        "alternatives": "曲率型; 曲率二次型; 曲率张量形式",
        "basin": "modern Sino-xenic coinage/calque",
        "debt": "High: 曲率形式 is a literal Mainland-compatible compound whose technical granularity is underdetermined; 型 and 二次型 are competing attractors and regional usage is untested.",
        "note": "Packaging does not adjudicate whether 形式 or a more specific algebraic-form label is preferable.",
    },
    {
        "german": "zweite Variation",
        "hans": "第二变分",
        "hant": "第二變分",
        "locator": "source snapshot lines 64–68, with inflected source wording; segment B",
        "scope": "second variation appearing in the named normal-form construction",
        "sense": "The second variation in calculus of variations, as represented by the displayed second-variation expression.",
        "excluded": "second finite difference; a second textual variant; repeated informal change; second derivative without variational meaning",
        "alternatives": "二次变分; 第二次变分; 二阶变分",
        "basin": "modern Sino-xenic coinage/calque",
        "debt": "Medium: 第二变分 is transparent in Mainland variational prose but competes with 二次 and 二阶 compounds; regional conventions were not researched.",
        "note": "The supplied form is bound to the producer target while the ordinal-versus-order alternatives remain open.",
    },
    {
        "german": "Normalform",
        "hans": "正规形式",
        "hant": "正規形式",
        "locator": "source snapshot line 64; segment B",
        "scope": "the stated normal form of the second variation",
        "sense": "A mathematically normalized or canonical form for the second-variation expression in context.",
        "excluded": "normal distribution; ordinary formatting; normal subgroup; normalized coordinates; social or procedural regularity",
        "alternatives": "标准形; 典范形式; 正规型",
        "basin": "mixed/contested",
        "debt": "High: 正规形式 is a Mainland-oriented choice with 标准形, 典范形式, and 正规型 as strong discipline- and region-sensitive attractors.",
        "note": "No claim is made that one Chinese normal-form convention dominates across fields or regions.",
    },
    {
        "german": "Reduktionssatz",
        "hans": "约化定理",
        "hant": "約化定理",
        "locator": "source snapshot lines 80 and 82; segment C",
        "scope": "the theorem reducing invariant construction or equivalence to the stated homogeneous-component problem",
        "sense": "A mathematical reduction theorem in the paper's invariant-theoretic argument.",
        "excluded": "reductio ad absurdum; reduction modulo an integer; informal simplification; chemical reduction",
        "alternatives": "化归定理; 简约定理; 归约定理",
        "basin": "mixed/contested",
        "debt": "High: 约化 is a PRC technical attractor but 化归 and 归约 compete across mathematical subfields; no regional or historical Chinese evidence was consulted.",
        "note": "The producer form is logged with the reduction-family terminology debt left unresolved for checkers.",
    },
    {
        "german": "Äquivalenz",
        "hans": "等价",
        "hant": "等價",
        "locator": "source snapshot lines 80 and 82; segment C",
        "scope": "equivalence of the relevant differential forms under the transformation relation discussed",
        "sense": "Mathematical equivalence under the specified transformation framework, including the equivalence question for forms.",
        "excluded": "literal equality; approximate numerical equality; logical biconditional without the transformation relation; equal economic value",
        "alternatives": "等价性; 等值; 等价关系",
        "basin": "modern Sino-xenic coinage/calque",
        "debt": "Low-to-medium: 等价 is highly conventional in Mainland mathematics but its unqualified use may hide the operative transformation relation; regional lexical evidence is absent.",
        "note": "The bounded sense window carries the transformation context that the short Chinese form does not itself expose.",
    },
    {
        "german": "Normalkoordinaten",
        "hans": "正规坐标",
        "hant": "正規坐標",
        "locator": "source snapshot line 80; segment C",
        "scope": "Riemannian normal coordinates used in the reduction argument",
        "sense": "Normal coordinates in differential geometry, centered at a point and associated with the geodesic construction discussed.",
        "excluded": "normalized data coordinates; ordinary Cartesian coordinates; normal vectors used as coordinates; coordinate standardization",
        "alternatives": "法坐标; 标准坐标; 正规座标",
        "basin": "mixed/contested",
        "debt": "High: 正规坐标 is Mainland-oriented; 法坐标, 标准坐标, and the glyph choice 坐标/座標 form a region-sensitive attractor set not investigated here.",
        "note": "The Hant form is a controlled script derivative only and is not evidence for any regional 坐標/座標 convention.",
    },
    {
        "german": "Parallelverschiebung",
        "hans": "平行移动",
        "hant": "平行移動",
        "locator": "source snapshot line 82; segment C",
        "scope": "geometric parallel transport of a vector in the Levi-Civita interpretation",
        "sense": "Parallel transport of a vector in the differential-geometric sense stated in the paper.",
        "excluded": "literal motion along a parallel line; Euclidean translation of a figure; moving two objects in parallel; a parallel shift of a graph alone",
        "alternatives": "平行输运; 平行传递; 平行移位",
        "basin": "mixed/contested",
        "debt": "High: 平行移动 is a literal Mainland-readable phrase but 平行输运 is a powerful modern geometry attractor; historical and regional preferences were not researched.",
        "note": "The supplied historical-style wording is recorded without deciding between 移动 and modern 输运 terminology.",
    },
    {
        "german": "invariantes Variationsproblem",
        "hans": "不变变分问题",
        "hant": "不變變分問題",
        "locator": "source snapshot line 84, with plural inflection; segment C",
        "scope": "a variational problem whose integral is invariant under a Lie-type group",
        "sense": "A calculus-of-variations problem equipped with the group invariance stated in the closing discussion.",
        "excluded": "a variational problem with an unchanged answer; a fixed optimization problem; an invariant function outside variational calculus; a generic symmetry problem",
        "alternatives": "不变的变分问题; 群不变变分问题; 不变变分原理",
        "basin": "modern Sino-xenic coinage/calque",
        "debt": "Medium: the stacked compound 不变变分问题 is characteristic of compact Mainland technical prose and may be syntactically dense; regional phrasing was not tested.",
        "note": "The sense window supplies the group-invariance relation omitted by the compact Chinese surface form.",
    },
    {
        "german": "Divergenz",
        "hans": "散度",
        "hant": "散度",
        "locator": "source snapshot line 84, with plural inflection; segment C",
        "scope": "divergence expressions corresponding to finite-parameter group invariance in the concluding Noether-theorem statement",
        "sense": "A mathematical divergence expression in the symmetry/invariance correspondence described at the end of the paper.",
        "excluded": "informal disagreement; divergence of a numerical series; unqualified vector-field divergence detached from the stated correspondence; mere nonconvergence",
        "alternatives": "发散; 散度式; 散度项",
        "basin": "modern Sino-xenic coinage/calque",
        "debt": "High: 散度 is Mainland-standard vector-calculus terminology but can under-specify the divergence-expression role here; 发散 is an adverse attractor and regional vocabulary was not researched.",
        "note": "The supplied form is recorded without source-theorem adjudication or a claim about the optimal explanatory expansion.",
    },
    {
        "german": "relative Invariante",
        "hans": "相对不变量",
        "hant": "相對不變量",
        "locator": "source snapshot line 84, parenthetical source wording and plural inflection; segment C",
        "scope": "relative invariant status attributed to the Lagrange expressions under the group",
        "sense": "An invariant that transforms relatively, rather than absolutely, in the group-theoretic setting described.",
        "excluded": "an invariant of merely relative importance; an absolute invariant; a relation between two arbitrary invariants; a quantity constant only approximately",
        "alternatives": "相对不变式; 关系不变量; 相对 invariant",
        "basin": "modern Sino-xenic coinage/calque",
        "debt": "Medium: 相对不变量 is Mainland-compatible but 不变式 competes, and the transformation-factor sense is not overt in the compact form; regional evidence is absent.",
        "note": "The relative-versus-absolute distinction is retained in the sense window for independent review.",
    },
    {
        "german": "Reihen",
        "hans": "变量组",
        "hant": "變量組",
        "locator": "source snapshot lines 58 and 62; segment B",
        "scope": "the two or more families of differential variables occurring as arguments of a form",
        "sense": "Ordered variable families such as dx and delta x, and further differential-variable families, in the local description of a form's arguments.",
        "excluded": "an infinite series; a power series; numerical convergence sequence; a row of a matrix without the variable-family role; a queue or rank",
        "alternatives": "变量列; 变量系列; 变量族",
        "basin": "mixed/contested",
        "debt": "High: 变量组 is a Mainland-readable editorial disambiguation rather than a surface calque of Reihen; 列, 系列, and 族 are strong attractors, and no regional evidence was consulted.",
        "note": "Because this packaging subtask does not adjudicate translation, the supplied producer form and its explicit excluded series-sense are both retained.",
    },
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


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def validate_inputs() -> dict[str, str]:
    expected = {
        "source": (SOURCE_PATH, EXPECTED_SOURCE_SHA256),
        "witness": (WITNESS_PATH, EXPECTED_WITNESS_SHA256),
        "hans": (HANS_PATH, EXPECTED_HANS_SHA256),
    }
    actual: dict[str, str] = {}
    for key, (path, expected_sha) in expected.items():
        if not path.is_file():
            raise FileNotFoundError(f"Required input absent: {path}")
        actual_sha = sha256(path)
        if actual_sha != expected_sha:
            raise RuntimeError(f"{key} SHA mismatch: expected {expected_sha}, got {actual_sha}")
        actual[key] = actual_sha
    if not HANT_PATH.is_file():
        raise FileNotFoundError(
            "Final controlled-Hant target is not present; wait for the producer build before the final evidence-pack rerun: "
            + str(HANT_PATH)
        )
    actual["hant"] = sha256(HANT_PATH)
    if actual["hant"] != EXPECTED_HANT_SHA256:
        raise RuntimeError(
            f"hant SHA mismatch: expected {EXPECTED_HANT_SHA256}, got {actual['hant']}"
        )
    actual["generator"] = sha256(Path(__file__))
    return actual


def write_csv(path: Path, headers: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=headers, quoting=csv.QUOTE_ALL, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def make_term_rows() -> list[dict[str, str]]:
    rows = []
    for index, term in enumerate(TERMS, 1):
        rows.append(
            {
                "decision_id": f"P21-ZH-T{index:03d}",
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
                "adverse_id": f"P21-ZH-A{index:03d}",
                "term_decision_id": f"P21-ZH-T{index:03d}",
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
                "crosswalk_id": f"P21-ZH-X{index:03d}",
                "term_decision_id": f"P21-ZH-T{index:03d}",
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
        locus_id = f"P21-LOC-{suffix}"
        concept_id = f"P21-CON-{suffix}"
        hans_id = f"P21-HANS-{suffix}"
        hant_id = f"P21-HANT-{suffix}"
        choice_id = f"P21-CHOICE-{suffix}"
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
                    "language_scope": "zh-Hant-controlled nonregional producer record",
                    "form": term["hant"],
                    "status": HANT_STATUS,
                },
                {
                    "id": choice_id,
                    "type": "producer_choice",
                    "decision_id": f"P21-ZH-T{suffix}",
                    "dominance_risk_debt": term["debt"],
                    "evidence_class": EVIDENCE_CLASS,
                    "review_state": REVIEW_STATE,
                },
            ]
        )
        edges.extend(
            [
                {"id": f"P21-E{suffix}-1", "type": "occurs_at", "from": concept_id, "to": locus_id},
                {"id": f"P21-E{suffix}-2", "type": "decides_for", "from": choice_id, "to": concept_id},
                {"id": f"P21-E{suffix}-3", "type": "selects_hans_form", "from": choice_id, "to": hans_id},
                {"id": f"P21-E{suffix}-4", "type": "records_controlled_hant_form", "from": choice_id, "to": hant_id},
                {"id": f"P21-E{suffix}-5", "type": "controlled_form_of", "from": hant_id, "to": hans_id},
            ]
        )

    return {
        "graph_id": "NOE-P21-ZH-PRODUCER-CONCEPT-GRAPH-001",
        "work_unit": "Noether Paper 21 Chinese producer translation",
        "graph_status": {
            "purpose": "producer-side translation-decision evidence packaging only",
            "decision_count": len(TERMS),
            "independent_check": "absent",
            "external_native_source_research": "not performed",
            "japanese_or_korean_evidence": "not consulted or used",
            "scan_inspection": "not performed",
            "source_branch_comparison": "not performed",
            "compilation_or_rendering": "not performed by this evidence-packaging subtask; rendered pages not inspected",
            "controlled_hant_scope": HANT_STATUS,
            "translation_validation_or_readiness_claim": "none",
        },
        "provenance": {
            "german_snapshot": {
                "path": "source/Noether_Paper21_German_current_exact_CRLF.tex",
                "sha256": hashes["source"],
                "use": "supplied translation-source wording and locator only; no source/apparatus check",
            },
            "inherited_hans_witness": {
                "path": "witness/Noether_Paper21_SimplifiedChinese_inherited_content_exact_CRLF.tex",
                "sha256": hashes["witness"],
                "use": "drafting witness only; not authority",
            },
            "hans_target": {
                "path": "zh-Hans-CN/Noether_Paper21_Chinese_CurrentAuthority_zh-Hans-CN_v001.tex",
                "sha256": hashes["hans"],
                "use": "supplied producer choice record; independent check absent",
            },
            "controlled_hant_target": {
                "path": "zh-Hant-controlled/Noether_Paper21_Chinese_CurrentAuthority_zh-Hant-controlled_v001.tex",
                "sha256": hashes["hant"],
                "use": HANT_STATUS,
            },
            "evidence_generator": {
                "path": "qa/build_p21_evidence_pack.py",
                "sha256": hashes["generator"],
                "use": "deterministic packaging of the supplied producer decisions into the established CSV and typed-graph shapes",
            },
            "evidence_class": EVIDENCE_CLASS,
        },
        "node_type_definitions": {
            "source_locus": "Locator and phrase in the supplied German fragment; not a source-validation assertion.",
            "concept": "Producer's bounded sense window and excluded lexical attractors.",
            "form": "Supplied Chinese form with explicit Hans or nonregional controlled-Hant scope.",
            "producer_choice": "Supplied editorial selection with qualitative Mandarin-Simplified dominance debt and open review state; lexical-attractor basin is recorded only in the CSV ledgers.",
        },
        "edge_type_definitions": {
            "occurs_at": "Concept to supplied-source locator.",
            "decides_for": "Producer choice to concept.",
            "selects_hans_form": "Producer choice to Hans form.",
            "records_controlled_hant_form": "Producer choice to nonregional controlled-Hant form.",
            "controlled_form_of": "Controlled-Hant script form to Hans lexical base without Taiwan/Hong Kong/Macao equivalence claim.",
        },
        "nodes": nodes,
        "edges": edges,
    }


def main() -> None:
    hashes = validate_inputs()
    EVIDENCE_DIR.mkdir(parents=True, exist_ok=True)
    write_csv(EVIDENCE_DIR / "TERMINOLOGY_LEDGER.csv", TERM_HEADERS, make_term_rows())
    write_csv(EVIDENCE_DIR / "ADVERSE_EVIDENCE_LEDGER.csv", ADVERSE_HEADERS, make_adverse_rows())
    write_csv(EVIDENCE_DIR / "CJKV_CROSSWALK.csv", CROSSWALK_HEADERS, make_crosswalk_rows())
    graph_path = EVIDENCE_DIR / "CONCEPT_EVIDENCE_GRAPH.json"
    graph_path.write_text(json.dumps(make_graph(hashes), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"rows_each_csv": len(TERMS), "nodes": len(TERMS) * 5, "edges": len(TERMS) * 5, **hashes}, indent=2))


if __name__ == "__main__":
    main()
