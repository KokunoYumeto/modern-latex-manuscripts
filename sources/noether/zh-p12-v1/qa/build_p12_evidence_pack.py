from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE_DIR = ROOT / "evidence"

INPUTS = {
    "source_a": (
        ROOT / "segments" / "source" / "P12_A_lines8071_8172.tex",
        "FA2A7821AAC02EAAFF3322FB88EB3DA9937DF086619B20A52FFD307384E378BE",
    ),
    "source_b": (
        ROOT / "segments" / "source" / "P12_B_lines8173_8317.tex",
        "DBE25989E0F304058E79F33D28AAA0028856D58AF7E5F8F74469FE88DFF7C646",
    ),
    "source_c": (
        ROOT / "segments" / "source" / "P12_C_lines8318_8471.tex",
        "5DAB1E227F618B119B9C4358A9DA1005474E040D5CA33877FCBD9BC7A6BCD734",
    ),
    "hans_a": (
        ROOT / "segments" / "zh-Hans-CN" / "P12_A_zh-Hans-CN.tex",
        "65CB2373945FCC6973010CD29729E354DF892A4C4CDFC4E215D2E44755CDAF01",
    ),
    "hans_b": (
        ROOT / "segments" / "zh-Hans-CN" / "P12_B_zh-Hans-CN.tex",
        "D8FEB6D63E9D837228503846D8B653954A36BFDC43443DC3CA4B379493502563",
    ),
    "hans_c": (
        ROOT / "segments" / "zh-Hans-CN" / "P12_C_zh-Hans-CN.tex",
        "23A21B0C662BA365ACC0373A5950C38C98577D06FD1059779B4F74B5AFA1DE64",
    ),
    "return_a": (
        ROOT / "worker_returns" / "P12_A_TRANSLATOR_RETURN.md",
        "D40AAAAF16CFE8F289FDAA3F938CB4B348D1B8F61E1B7494147726356EEB1207",
    ),
    "return_b": (
        ROOT / "worker_returns" / "P12_B_TRANSLATOR_RETURN.md",
        "F61D88A1A95B9B2556D2B92C0FCCA0483EEEA2CCEF8E05F843834807BBF5E2EB",
    ),
    "return_c": (
        ROOT / "worker_returns" / "P12_C_TRANSLATOR_RETURN.md",
        "0EEDDFF35D391E49D3E51CCD2887DB7D2D65A60AC7A7532C3C1BA19C95F48C00",
    ),
}

SOURCE_KEYS = ("source_a", "source_b", "source_c")
HANS_KEYS = ("hans_a", "hans_b", "hans_c")
RETURN_KEYS = ("return_a", "return_b", "return_c")

EVIDENCE_CLASS = (
    "producer terminology proposal extracted from the supplied Paper 12 German fragments, "
    "PRC-oriented Hans producer segments, and worker returns; inherited Chinese witness "
    "unconsulted; independent checking absent"
)
HANT_STATUS = (
    "controlled generic script record only; not zh-Hant-TW/HK/MO; "
    "regional lexical localization absent"
)
REVIEW_STATE = "independent check absent; pending"
JA_KO_STATUS = "JA and KO unconsulted and non-authorizing for Chinese"

ALLOWED_BASINS = {
    "Sino-xenic inherited",
    "modern Sino-xenic coinage/calque",
    "global modern loan",
    "native coinage",
    "mixed/contested",
    "unresolved",
}


TERMS = [
    {
        "german": "Differentialausdruck",
        "hans": "微分表达式",
        "hant": "微分表達式",
        "locator": "segments/source/P12_A_lines8071_8172.tex; source lines 8071, 8073, and 8087",
        "scope": "the paper's function of variables and their differentials, treated as the object whose invariants are constructed",
        "sense": "A mathematical differential expression in the paper's defined function-of-variables-and-differentials sense.",
        "excluded": "a differential operator by itself; an infinitesimal quantity alone; an arbitrary displayed formula; a differential equation as such",
        "alternatives": "微分式; 微分量表达式; differential expression",
        "basin": "modern Sino-xenic coinage/calque",
        "debt": "Medium: 微分表达式 is transparent PRC technical prose, while 微分式 is a strong shorter attractor and historical non-Mainland preferences were not researched.",
        "note": "The compact producer noun is recorded without certifying it against an external Chinese terminology source.",
    },
    {
        "german": "simultanes System",
        "hans": "联立系统",
        "hant": "聯立系統",
        "locator": "segments/source/P12_A_lines8071_8172.tex lines 8127–8136; segment C line 8425",
        "scope": "a collection of differential expressions considered jointly for simultaneous invariant construction",
        "sense": "The jointly treated system of differential expressions in the paper's invariant-theoretic construction.",
        "excluded": "a simultaneous-equation system specifically; a time-synchronized system; a merely adjacent list; a coupled dynamical system without the invariant context",
        "alternatives": "同时系统; 联合系统; 伴随系统",
        "basin": "mixed/contested",
        "debt": "High: 联立系统 is Mainland-readable but strongly attracts the narrower simultaneous-equations sense; 同时系统 and 联合系统 remain live alternatives and regional evidence is absent.",
        "note": "The evidence record keeps the jointly-considered-system sense explicit and leaves naming to independent review.",
    },
    {
        "german": "projektive Invariante",
        "hans": "射影不变量",
        "hant": "射影不變量",
        "locator": "segment A source lines 8135 and 8140–8141; segment B line 8177; segment C lines 8408–8410",
        "scope": "an invariant under the stated linear transformation group of the differential arguments",
        "sense": "A projective invariant in the paper's reduction of the differential-invariant problem to linear invariant theory.",
        "excluded": "a projected numerical quantity; a projection operator invariant; a generic invariant of projective geometry without the local simultaneous system; an absolute invariant with no transformation qualification",
        "alternatives": "射影不变式; 投影不变量; projective invariant",
        "basin": "modern Sino-xenic coinage/calque",
        "debt": "High: 射影不变量 is strongly Mainland-normalized, while 不变式 and 投影 are competing attractors and no Traditional-Chinese regional terminology shelf was consulted.",
        "note": "The controlled-Hant glyph form does not establish Taiwan, Hong Kong, or Macao terminology.",
    },
    {
        "german": "Äquivalenz",
        "hans": "等价性",
        "hant": "等價性",
        "locator": "segment A source line 8142; segment C heading line 8319 and lines 8383–8384 and 8430–8432",
        "scope": "equivalence of differential expressions or associated function systems under the transformations under discussion",
        "sense": "Mathematical equivalence relative to the specified transformation action, not literal equality.",
        "excluded": "literal equality; approximate numerical equality; logical biconditional without the transformation relation; equal economic value",
        "alternatives": "等价; 等值性; 等价关系",
        "basin": "modern Sino-xenic coinage/calque",
        "debt": "Low-to-medium: 等价性 is conventional PRC mathematical wording, but the short form hides the operative transformation relation and regional lexical evidence was not consulted.",
        "note": "The sense window supplies the relation that the compact producer form leaves implicit.",
    },
    {
        "german": "Reduktionssatz",
        "hans": "约化定理",
        "hant": "約化定理",
        "locator": "segment A source lines 8144, 8150, 8155, and 8163–8164; segment C heading line 8319 and line 8435",
        "scope": "the named theorem reducing the differential-invariant and equivalence questions to linear invariant theory",
        "sense": "The paper's mathematical reduction theorem for the invariant systems it constructs.",
        "excluded": "reductio ad absurdum; reduction modulo an integer; informal simplification; chemical reduction",
        "alternatives": "归约定理; 化归定理; 简约定理",
        "basin": "mixed/contested",
        "debt": "High: 约化 is a PRC technical attractor, while 归约 and 化归 compete across mathematical subfields; no historical or regional Chinese evidence was researched.",
        "note": "This is the producer's selected reduction-family term, not an adjudicated standard.",
    },
    {
        "german": "invariante Bildungen",
        "hans": "不变量构造",
        "hant": "不變量構造",
        "locator": "segments/source/P12_A_lines8071_8172.tex; source lines 8140 and 8152–8157",
        "scope": "the mathematical constructions that generate the invariant forms in the proposed complete system",
        "sense": "Invariant-producing mathematical constructions or formations in the paper's algorithmic discussion.",
        "excluded": "education or cultivation; image formation; a finished invariant form only; a generic construction unrelated to invariant generation",
        "alternatives": "不变构造; 不变量形成式; 不变式构造",
        "basin": "mixed/contested",
        "debt": "High: 构造 is an editorially explicit Mainland choice for the broad historical Bildung, while 形式 and 形成 are competing local attractors and regional usage is untested.",
        "note": "The producer used 构造 to expose process; the historical noun's granularity remains open.",
    },
    {
        "german": "Normalkoordinaten",
        "hans": "正规坐标",
        "hant": "正規坐標",
        "locator": "segment A source lines 8164–8165; segment C heading line 8319 and lines 8322, 8362, and 8366",
        "scope": "Riemannian normal coordinates centered at the chosen point and defined through the extremal construction",
        "sense": "Normal coordinates in the differential-geometric construction described in the paper.",
        "excluded": "normalized data coordinates; ordinary Cartesian coordinates; a normal vector used as a coordinate; coordinate standardization",
        "alternatives": "法坐标; 标准坐标; 正规座标",
        "basin": "mixed/contested",
        "debt": "High: 正规坐标 is Mainland-oriented; 法坐标 and 标准坐标 compete, while 坐标/座標 is region-sensitive and was not researched.",
        "note": "The Hant form is generic script control only and does not choose a regional 坐標/座標 convention.",
    },
    {
        "german": "Extremale",
        "hans": "极值曲线",
        "hant": "極值曲線",
        "locator": "segment A source line 8166; segment C source lines 8354 and 8363",
        "scope": "an extremal curve solving the associated variational problem and used to construct normal coordinates",
        "sense": "A curve extremizing the relevant variational functional in the local geometric construction.",
        "excluded": "a scalar maximum or minimum; an extremist person; an endpoint of an interval; any shortest-looking line without the variational problem",
        "alternatives": "极值线; 极值轨线; 极端曲线",
        "basin": "mixed/contested",
        "debt": "High: 极值曲线 is explanatory PRC wording rather than a one-morpheme historical calque; 极值线 remains a strong attractor and regional convention is untested.",
        "note": "The producer's curve-explicit form is recorded without external terminology validation.",
    },
    {
        "german": "Variationsproblem",
        "hans": "变分问题",
        "hant": "變分問題",
        "locator": "segment A source line 8166; segment B line 8243; segment C lines 8322–8323",
        "scope": "the calculus-of-variations problem whose extremals and invariant equations are under discussion",
        "sense": "A problem in the calculus of variations associated with the displayed differential expression.",
        "excluded": "statistical variance; textual variation; a generic change-management problem; arbitrary optimization without variational structure",
        "alternatives": "泛函极值问题; 变分课题; 变分原理问题",
        "basin": "modern Sino-xenic coinage/calque",
        "debt": "Low-to-medium: 变分问题 is conventional PRC mathematical wording, but non-Mainland historical register and fuller explanatory alternatives were not researched.",
        "note": "The compact producer compound remains explicitly bounded to calculus of variations.",
    },
    {
        "german": "Polare",
        "hans": "极化式",
        "hant": "極化式",
        "locator": "segments/source/P12_B_lines8173_8317.tex; source lines 8177–8178 and 8198",
        "scope": "the polar forms obtained by expanding the differential expression in the auxiliary parameter",
        "sense": "A polarization-derived form in invariant theory, as instantiated by the parameter expansion in the paper.",
        "excluded": "polar coordinates; a geometric polar line by itself; electrical polarity; a pole or polar region; a generic polarized object",
        "alternatives": "极式; 偏极式; 极化形式",
        "basin": "mixed/contested",
        "debt": "High: 极化式 is a Mainland-readable interpretive compound, while 极式 is a historically compact attractor and no regional terminology evidence was consulted.",
        "note": "The worker return explicitly marks 极式 as an unresolved producer alternative.",
    },
    {
        "german": "Variationsprozess",
        "hans": "变分过程",
        "hant": "變分過程",
        "locator": "segment A source line 8157; segment B source line 8198",
        "scope": "the formal variation process applied repeatedly to generate further invariants",
        "sense": "An operation of formal variation in the paper's invariant-generating procedure.",
        "excluded": "statistical variance computation; textual variant production; informal change; a physical time evolution without variation calculus",
        "alternatives": "变分运算; 变分操作; 变易过程",
        "basin": "modern Sino-xenic coinage/calque",
        "debt": "Medium: 变分过程 is natural PRC prose, while 运算 and 操作 may better expose the algorithmic role and regional historical usage is unknown.",
        "note": "The record describes a producer wording proposal, not a checked operator taxonomy.",
    },
    {
        "german": "Normalform der rho-ten Variation",
        "hans": "第 rho 次变分的正规形式",
        "hant": "第 rho 次變分的正規形式",
        "locator": "segments/source/P12_B_lines8173_8317.tex; source lines 8215–8219",
        "scope": "the displayed normal form obtained from a linear combination of the rho-th variation invariants",
        "sense": "A normalized mathematical form for the rho-th variation in the local construction.",
        "excluded": "normal distribution; ordinary document formatting; a normal subgroup; normal coordinates; an arbitrary standard-looking expression",
        "alternatives": "第 rho 次变分的标准形; rho 阶变分正规型; 第 rho 变分的典范形式",
        "basin": "mixed/contested",
        "debt": "High: 正规形式 is Mainland-oriented and competes with 标准形, 典范形式, and 正规型; ordinal wording and regional conventions remain unresearched.",
        "note": "The Latin placeholder rho records the lexical proposal without adding TeX to the CSV field.",
    },
    {
        "german": "Grundfunktion",
        "hans": "基本函数",
        "hant": "基本函數",
        "locator": "segment B source lines 8233–8236 and 8280–8289; segment C lines 8388–8389 and 8417–8418",
        "scope": "an invariant containing only first differentials and serving as a generator in the complete system",
        "sense": "The paper's specially named first-differential invariant function used to build the full invariant system.",
        "excluded": "an elementary function; a basis function in approximation theory; a fundamental solution; any function called basic informally",
        "alternatives": "基础函数; 基础不变量; 基函数",
        "basin": "modern Sino-xenic coinage/calque",
        "debt": "High: 基本函数 is broad in Mainland mathematics and can attract basis-function or elementary-function senses; the more specific alternatives and regional terminology were not researched.",
        "note": "The sense window carries the paper-specific invariant role that the short Chinese compound does not expose.",
    },
    {
        "german": "Lagrangesche Gleichungen",
        "hans": "Lagrange 方程",
        "hant": "Lagrange 方程",
        "locator": "segments/source/P12_B_lines8173_8317.tex; source lines 8240–8247",
        "scope": "the equations of the associated variational problem obtained from the displayed first variation",
        "sense": "The Lagrange-associated variational equations named in the source passage.",
        "excluded": "Lagrange interpolation; Lagrange multiplier equations generically; a formula merely written by Lagrange; an unqualified mechanical equation",
        "alternatives": "拉格朗日方程; Euler--Lagrange 方程; 欧拉--拉格朗日方程",
        "basin": "mixed/contested",
        "debt": "High: the mixed Latin-name form follows the segment producer's deliberate name posture; full transliteration and the more specific Euler--Lagrange label are strong attractors, with regional naming unresearched.",
        "note": "Personal-name expansion was intentionally left pending in the worker return.",
    },
    {
        "german": "invariantes Gleichungssystem",
        "hans": "不变方程组",
        "hant": "不變方程組",
        "locator": "segments/source/P12_B_lines8173_8317.tex; source lines 8264–8267 and 8279–8281",
        "scope": "a system of equations invariant under the transformation framework and used to eliminate higher differentials",
        "sense": "A transformation-invariant equation system in the paper's differential elimination construction.",
        "excluded": "a system whose displayed text is unchanged; a constant-coefficient system; an invariant scalar equation alone; an arbitrary system of simultaneous equations",
        "alternatives": "不变的方程组; 不变量方程组; 协变方程组",
        "basin": "modern Sino-xenic coinage/calque",
        "debt": "Medium: 不变方程组 is compact Mainland technical syntax and may obscure whether the equations or their solution set carry invariance; regional phrasing is untested.",
        "note": "The group-action relation remains explicit in the sense window for later checking.",
    },
    {
        "german": "kovariante Ableitung",
        "hans": "协变导数",
        "hant": "協變導數",
        "locator": "segment B source lines 8285–8288; segment C source line 8426",
        "scope": "the covariant derivative of a basic function produced by the stated differential-and-elimination procedure",
        "sense": "A covariant derivative operation in the paper's differential-geometric invariant construction.",
        "excluded": "ordinary derivative; statistical covariance derivative; cogredient behavior without differentiation; a derivative merely independent of coordinates",
        "alternatives": "共变导数; 协变微分; 共变微分",
        "basin": "modern Sino-xenic coinage/calque",
        "debt": "High: 协变导数 is strongly Mainland-normalized, while 共变 and 微分 variants are live attractors and no regional evidence shelf was consulted.",
        "note": "The supplied producer choice is recorded without historical or regional certification.",
    },
    {
        "german": "kogredient",
        "hans": "同变",
        "hant": "同變",
        "locator": "segment B source lines 8302–8306; segment C source line 8411",
        "scope": "quantities subject to the same linear transformations as the first differentials",
        "sense": "Cogredient transformation behavior, made explicit in the source parenthesis as undergoing the same linear transformations.",
        "excluded": "statistical covariance; simultaneous numerical change; ordinary agreement; covariant differentiation; equality of quantities",
        "alternatives": "协同变换; 共变; 同步变换",
        "basin": "mixed/contested",
        "debt": "High: 同变 is a terse producer disambiguation in PRC prose, while 共变 and 协同变换 attract overlapping modern senses; historical and regional choices were not researched.",
        "note": "The parenthetical same-transformation gloss is part of the producer sense record, not an adjudication.",
    },
    {
        "german": "vollständiges System",
        "hans": "完备系统",
        "hant": "完備系統",
        "locator": "segment A source lines 8144 and 8152; segment B line 8316; segment C lines 8388, 8417, and 8448",
        "scope": "a system asserted in the paper to exhaust the relevant invariant or basic-function constructions",
        "sense": "A complete system in the local invariant-theoretic sense of supplying the required family.",
        "excluded": "metric completeness; a fully implemented software system; a closed dynamical system; a merely finished list",
        "alternatives": "完全系统; 完整系统; 全备系统",
        "basin": "mixed/contested",
        "debt": "High: the three Hans producer segments instantiate 完全系统, 完整系统, and 完备系统; this record selects the segment-C proposal for evidence indexing only and does not resolve the competing Mainland forms.",
        "note": "Multiple producer surface forms are preserved as alternatives; convergence belongs to independent checking.",
    },
    {
        "german": "Formen pter Dimension",
        "hans": "p 次形式",
        "hant": "p 次形式",
        "locator": "segments/source/P12_C_lines8318_8471.tex; source lines 8451–8452 and 8458",
        "scope": "the class of forms indexed by p in the closing generalization beyond quadratic forms",
        "sense": "The locally p-indexed forms instantiated by the producer as p 次形式; the historical degree-versus-dimension convention is not adjudicated here.",
        "excluded": "a p-dimensional vector space automatically; a differential p-form automatically; matrix dimension p; the p-th item in an arbitrary list",
        "alternatives": "p 维形式; p 阶形式; p 次型",
        "basin": "unresolved",
        "debt": "High: p 次形式 is a PRC-oriented producer inference, while p 维形式 closely attracts the source surface wording and differential-form senses may interfere; the historical convention and regional usage remain unresolved.",
        "note": "This entry deliberately records unresolved sense debt instead of validating either 次 or 维.",
    },
    {
        "german": "Integrabilitätsbedingungen",
        "hans": "可积性条件",
        "hant": "可積性條件",
        "locator": "segments/source/P12_C_lines8318_8471.tex; source line 8433",
        "scope": "additional integrability conditions whose absence is noted in the equivalence reduction",
        "sense": "Mathematical conditions for integrability in the local differential-equation or differential-geometric argument.",
        "excluded": "numerical integrability alone; economic integration; software compatibility; a condition for finite summability without the differential context",
        "alternatives": "可积分条件; 积分可能性条件; 可整合性条件",
        "basin": "modern Sino-xenic coinage/calque",
        "debt": "Low-to-medium: 可积性条件 is conventional Mainland mathematical vocabulary, but its exact subfield register and regional equivalents were not researched.",
        "note": "The entry is a terminology proposal record only and does not assess whether such conditions are mathematically required.",
    },
    {
        "german": "affine Gruppe",
        "hans": "仿射群",
        "hant": "仿射群",
        "locator": "segments/source/P12_C_lines8318_8471.tex; source lines 8443–8447",
        "scope": "the affine transformation group to which the inhomogeneous case is reduced by homogenization",
        "sense": "The affine group in the mathematical transformation-group sense used in the closing reduction.",
        "excluded": "a social affinity group; an affine space alone; linear group with no translations; visual similarity",
        "alternatives": "仿射变换群; 阿芬群; affine 群",
        "basin": "modern Sino-xenic coinage/calque",
        "debt": "Low-to-medium: 仿射群 is strongly established in Mainland mathematics, but the fuller 仿射变换群 and non-Mainland historical labels were not researched.",
        "note": "No external terminology shelf was used to elevate the proposal to validated status.",
    },
    {
        "german": "Riemannsche Krümmungsform",
        "hans": "黎曼曲率形式",
        "hant": "黎曼曲率形式",
        "locator": "segments/source/P12_C_lines8318_8471.tex; source lines 8455–8456",
        "scope": "the distinguished curvature form represented by Omega_2 for quadratic forms",
        "sense": "Riemann's curvature-associated form in the paper's invariant-system construction.",
        "excluded": "scalar curvature alone; the Riemann curvature tensor automatically; a generic formula for curvature; the visual shape of a curve",
        "alternatives": "黎曼曲率型; Riemann 曲率形式; 黎曼曲率二次型",
        "basin": "mixed/contested",
        "debt": "High: 黎曼曲率形式 is Mainland-readable but may attract the modern tensor or differential-form sense; 形式, 型, and 二次型 granularity and regional naming were not researched.",
        "note": "The evidence record preserves the producer phrase without identifying it with a modern curvature object.",
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
    if not 20 <= len(TERMS) <= 24:
        raise RuntimeError(f"Expected 20–24 terms, got {len(TERMS)}")
    for index, term in enumerate(TERMS, 1):
        if set(term) != TERM_KEYS:
            raise RuntimeError(
                f"Term {index} has invalid shape: missing={TERM_KEYS - set(term)}, extra={set(term) - TERM_KEYS}"
            )
        if term["basin"] not in ALLOWED_BASINS:
            raise RuntimeError(f"Term {index} has invalid basin: {term['basin']}")
        for key in TERM_KEYS:
            if not term[key].strip():
                raise RuntimeError(f"Term {index} has empty required field: {key}")


def validate_inputs() -> dict[str, str]:
    actual: dict[str, str] = {}
    for key, (path, expected_sha) in INPUTS.items():
        if not path.is_file():
            raise FileNotFoundError(f"Required input absent: {path}")
        actual_sha = sha256(path)
        if actual_sha != expected_sha:
            raise RuntimeError(f"{key} SHA mismatch: expected {expected_sha}, got {actual_sha}")
        actual[key] = actual_sha
    actual["source_manifest"] = manifest_sha(SOURCE_KEYS, actual)
    actual["hans_manifest"] = manifest_sha(HANS_KEYS, actual)
    actual["return_manifest"] = manifest_sha(RETURN_KEYS, actual)
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
                "decision_id": f"P12-ZH-T{index:03d}",
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
                "adverse_id": f"P12-ZH-A{index:03d}",
                "term_decision_id": f"P12-ZH-T{index:03d}",
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
                "crosswalk_id": f"P12-ZH-X{index:03d}",
                "term_decision_id": f"P12-ZH-T{index:03d}",
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
        locus_id = f"P12-LOC-{suffix}"
        concept_id = f"P12-CON-{suffix}"
        hans_id = f"P12-HANS-{suffix}"
        hant_id = f"P12-HANT-{suffix}"
        choice_id = f"P12-CHOICE-{suffix}"
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
                    "decision_id": f"P12-ZH-T{suffix}",
                    "dominance_risk_debt": term["debt"],
                    "evidence_class": EVIDENCE_CLASS,
                    "review_state": REVIEW_STATE,
                },
            ]
        )
        edges.extend(
            [
                {"id": f"P12-E{suffix}-1", "type": "occurs_at", "from": concept_id, "to": locus_id},
                {"id": f"P12-E{suffix}-2", "type": "decides_for", "from": choice_id, "to": concept_id},
                {"id": f"P12-E{suffix}-3", "type": "selects_hans_form", "from": choice_id, "to": hans_id},
                {"id": f"P12-E{suffix}-4", "type": "records_controlled_hant_form", "from": choice_id, "to": hant_id},
                {"id": f"P12-E{suffix}-5", "type": "controlled_form_of", "from": hant_id, "to": hans_id},
            ]
        )

    source_hashes = "; ".join(f"{key}={hashes[key]}" for key in SOURCE_KEYS)
    hans_hashes = "; ".join(f"{key}={hashes[key]}" for key in HANS_KEYS)
    return_hashes = "; ".join(f"{key}={hashes[key]}" for key in RETURN_KEYS)
    return {
        "graph_id": "NOE-P12-ZH-PRODUCER-CONCEPT-GRAPH-001",
        "work_unit": "Noether Paper 12 Chinese producer translation",
        "graph_status": {
            "purpose": "producer-side translation-decision evidence packaging only",
            "decision_count": len(TERMS),
            "independent_check": "absent",
            "external_native_source_research": "not performed",
            "japanese_or_korean_evidence": "not consulted or used; non-authorizing for Chinese",
            "scan_inspection": "not performed",
            "source_branch_comparison": "not performed",
            "compilation_or_rendering": "not performed by this evidence-packaging subtask; rendered pages not inspected",
            "controlled_hant_scope": HANT_STATUS,
            "translation_validation_or_readiness_claim": "none",
        },
        "provenance": {
            "german_snapshot": {
                "path": "segments/source/P12_A_lines8071_8172.tex; segments/source/P12_B_lines8173_8317.tex; segments/source/P12_C_lines8318_8471.tex",
                "sha256": f"manifest={hashes['source_manifest']}; {source_hashes}",
                "use": "supplied translation-source terminology and locators only; no source/apparatus check or branch comparison",
            },
            "inherited_hans_witness": {
                "path": "not consulted in this evidence-packaging subtask",
                "sha256": "not computed",
                "use": "explicitly excluded from the permitted input set; no witness comparison or audit",
            },
            "hans_target": {
                "path": "segments/zh-Hans-CN/P12_A_zh-Hans-CN.tex; segments/zh-Hans-CN/P12_B_zh-Hans-CN.tex; segments/zh-Hans-CN/P12_C_zh-Hans-CN.tex",
                "sha256": f"manifest={hashes['hans_manifest']}; {hans_hashes}",
                "use": f"supplied producer proposal record; worker-return manifest={hashes['return_manifest']}; {return_hashes}; independent check absent",
            },
            "controlled_hant_target": {
                "path": "not consulted; controlled forms are nonregional evidence records only",
                "sha256": "not computed",
                "use": HANT_STATUS,
            },
            "evidence_generator": {
                "path": "qa/build_p12_evidence_pack.py",
                "sha256": hashes["generator"],
                "use": "deterministic packaging of producer terminology proposals into the established CSV and typed-graph shapes",
            },
            "evidence_class": EVIDENCE_CLASS,
        },
        "node_type_definitions": {
            "source_locus": "Locator and phrase in the supplied German fragment; not a source-validation assertion.",
            "concept": "Producer's bounded sense window and excluded lexical attractors.",
            "form": "Supplied Chinese form with explicit Hans or nonregional controlled-Hant scope.",
            "producer_choice": "Supplied editorial proposal with qualitative Mandarin-Simplified dominance debt and open review state; lexical-attractor basin is recorded only in the CSV ledgers.",
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
    validate_terms()
    hashes = validate_inputs()
    EVIDENCE_DIR.mkdir(parents=True, exist_ok=True)
    write_csv(EVIDENCE_DIR / "TERMINOLOGY_LEDGER.csv", TERM_HEADERS, make_term_rows())
    write_csv(EVIDENCE_DIR / "ADVERSE_EVIDENCE_LEDGER.csv", ADVERSE_HEADERS, make_adverse_rows())
    write_csv(EVIDENCE_DIR / "CJKV_CROSSWALK.csv", CROSSWALK_HEADERS, make_crosswalk_rows())
    graph_path = EVIDENCE_DIR / "CONCEPT_EVIDENCE_GRAPH.json"
    graph_path.write_text(json.dumps(make_graph(hashes), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "rows_each_csv": len(TERMS),
                "nodes": len(TERMS) * 5,
                "edges": len(TERMS) * 5,
                **hashes,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
