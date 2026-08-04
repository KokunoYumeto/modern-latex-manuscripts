#!/usr/bin/env python3
"""Generate Paper 32 producer terminology records without asserting validation."""

from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "evidence"
EVIDENCE.mkdir(parents=True, exist_ok=True)

SOURCE_SHA = "1E1C2E6AA32B606EAB5B57737F60CE7CF649610B490098511C29498BE8CC7611"
WITNESS_SHA = "34655BF638E18A2B62C062D0D34E2CC44CB5FB1B9FC70B4CC748F5281761A813"
HANS_SHA = "762BCAC20CFB3DBCFBE000E16ADBA386DB3561A1BFC594C5C769083D53D28A06"
HANT_SHA = "2616DB5841744671F8CA611C126979DBEB46D06B25657C2FC2EC484E03151F13"
EVIDENCE_CLASS = (
    "producer editorial choice recorded in the assembled Hans target plus the inherited "
    "Simplified-Chinese drafting witness; independent checking absent"
)
HANT_STATUS = (
    "controlled generic script derivative only; not zh-Hant-TW/HK/MO; "
    "regional lexical localization absent"
)
REVIEW = "independent check absent; pending"


def term(locator: str, german: str, scope: str, hans: str, hant: str,
         window: str, excluded: str, alternatives: str, basin: str,
         debt: str, note: str) -> dict[str, str]:
    return {
        "locator": locator,
        "german": german,
        "scope": scope,
        "hans": hans,
        "hant": hant,
        "window": window,
        "excluded": excluded,
        "alternatives": alternatives,
        "basin": basin,
        "debt": debt,
        "note": note,
    }


TERMS = [
    term("segments A-D, governing term", "Zerfällungskörper", "field that makes the indicated representation or division algebra split", "分裂域", "分裂域", "A field extension over which the relevant irreducible representation or associated noncommutative division algebra splits in the paper's representation-theoretic sense.", "a splitting field of one polynomial only; a decomposition field in algebraic number theory without the representation-theoretic role; a physical fracture region", "分解域; 劈裂域", "modern Sino-xenic coinage/calque", "High: 分裂域 is dominant on the Mandarin-Simplified producer shelf, while regional usage and the competing 分解域/劈裂域 traditions are untested.", "Applied as the paper's central term; no readiness claim."),
    term("segment A title; segments A-D", "minimaler Zerfällungskörper", "splitting field none of whose proper subfields is a splitting field", "极小分裂域", "極小分裂域", "A splitting field minimal under inclusion, exactly as defined in the article; it need not have the smallest degree among all splitting fields.", "a splitting field of globally minimum degree; a minimal polynomial's splitting field; merely a small field", "最小分裂域; 极小分解域", "modern Sino-xenic coinage/calque", "High: 极小/最小 is a Mandarin trap because the article distinguishes inclusion-minimal from least degree; regional mathematical wording is untested.", "Producer uses 极小 for inclusion-minimal and 次数最小 for least-degree."),
    term("segments A-B", "Zahlkörper", "finite algebraic number field in the article", "数域", "數域", "An algebraic number field occurring as a candidate splitting field or subfield in the arithmetic discussion.", "an arbitrary field of numbers; a numeric domain in computing; a finite field", "代数数域; 数体", "Sino-xenic inherited", "Medium: 数域 is standard-looking in Mandarin but may under-specify algebraicity and differs from regional preferences such as 数体.", "The surrounding prose supplies algebraic-number-field scope."),
    term("segments A and D", "Grundkörper", "base field relative to which representations and degrees are taken", "基域", "基域", "The coefficient/base field over which the hypercomplex system, extension degrees, or relative norm is considered.", "a geometric base space; an underlying set; a computer database domain", "基础域; 底域", "modern Sino-xenic coinage/calque", "Medium: 基域 reflects Mainland algebra usage; cross-regional preference between 基域/底域/基础域 is untested.", "Kept distinct from characteristic fields and extension fields."),
    term("title and segments A-C", "irreduzible Darstellung", "representation with no proper invariant reduction in the article's sense", "不可约表示", "不可約表示", "A group or hypercomplex-system representation that is irreducible over the stated coefficient field.", "an indecomposable but reducible representation; a representation that cannot be simplified computationally; a literary depiction", "既约表示; 不可分解表示", "modern Sino-xenic coinage/calque", "Medium: 不可约表示 follows current Mandarin convention, but older and regional shelves can prefer 既约 or distinguish indecomposable language differently.", "Used throughout without claiming regional equivalence."),
    term("segment A opening", "absolut irreduzibler Bestandteil", "absolutely irreducible constituent after scalar extension", "绝对不可约分量", "絕對不可約分量", "A constituent remaining irreducible after all relevant field extensions, counted in Schur's result.", "an absolute value component; a direct-sum component lacking the scalar-extension condition; a physical constituent", "绝对不可约组成部分; 绝对既约分量", "modern Sino-xenic coinage/calque", "High: 分量 is concise Mandarin terminology, but the inherited witness used 组成部分 and regional/older representation-theory practice is untested.", "Segment A consistently uses 分量 in the opening statement."),
    term("segment A opening and characterization theorem", "Charakter", "character of a representation", "特征标", "特徵標", "The trace character associated with the representation and its corresponding field, not a scalar characteristic.", "characteristic of a field; an eigenvalue; a personality trait; a printed character", "特征; 表示特征", "modern Sino-xenic coinage/calque", "High: 特征标 disambiguates Mandarin mathematical senses but its regional Traditional-Chinese lexical acceptance is untested.", "Kept distinct from field characteristic."),
    term("segments A-D", "Schurscher Index; Index", "Schur index governing degrees and splitting", "Schur 指数", "Schur 指數", "The Schur index attached to the character or division algebra, used as the divisor of splitting-field degrees.", "an array index; a book index; a subgroup index unless explicitly related; an economic index", "舒尔指数; Schur 示性数", "global modern loan", "Medium: retaining the personal name in Latin script follows the producer shelf and avoids name-transliteration variation, but regional typography is untested.", "Bare 指数 is used only where the local discourse has already fixed the Schur-index sense."),
    term("segment A program and theorem", "nichtkommutativer Körper", "finite-dimensional noncommutative division algebra over its center", "非交换除环", "非交換除環", "The associated skew field/division ring whose nonzero elements are invertible; the historical German Körper is not being rendered as an ordinary field.", "a noncommutative ordinary field; any noncommutative ring; a physical body", "非交换体; 斜域; 非可换除环", "mixed/contested", "High: 非交换除环 is an explicit Mandarin disambiguation; historical and regional shelves may prefer 斜域 or 非交换体.", "Major historical sense trap; producer choice is unvalidated."),
    term("segment A characterization", "zweiseitig einfacher Ring", "ring simple as a two-sided ring", "双侧单环", "雙側單環", "A ring with no nontrivial two-sided ideals in the article's structure-theoretic discussion.", "a ring that is simple on both visual sides; a one-sided simple module; a principal ideal ring", "双边单环; 二侧单环", "modern Sino-xenic coinage/calque", "Medium: 双侧 follows Mandarin module terminology; regional preference for 双边 or other forms is untested.", "Used for the rings invariantly attached to the division algebra."),
    term("segment A definitions; segment B", "hyperkomplexes System", "historical finite-dimensional algebraic system", "超复系统", "超複系統", "The historical hypercomplex algebra/system carrying representations, including group rings and quaternion algebras.", "a modern hypercomplex dynamical system; hypercomplex analysis only; a generic complicated system", "超复数系; 超复代数; 超复数系统", "modern Sino-xenic coinage/calque", "High: 超复系统 follows the inherited Mainland-oriented shelf but is historically opaque and regionally untested.", "Historical terminology retained rather than silently modernized to algebra."),
    term("segment A definitions", "Darstellungsklasse", "similarity/equivalence class of representations", "表示类", "表示類", "A representation together with all its transforms $P^{-1}\\Gamma P$, and later the corresponding irreducible class.", "a school class; a programming class; a class function; one individual representation", "表示的等价类; 表示类别", "modern Sino-xenic coinage/calque", "Medium: 表示类 is concise Mainland mathematical prose; the explicit equivalence-class form may be preferred elsewhere.", "The local definition fixes the class relation."),
    term("segments A-B", "vollständig reduzibel", "completely reducible/semisimple representation-theoretic condition", "完全可约", "完全可約", "A representation or system whose representation classes decompose completely into irreducible constituents.", "merely reducible; computationally simplified; a fully reduced fraction; an Artinian condition by itself", "全可约; 半单", "modern Sino-xenic coinage/calque", "Medium: 完全可约 follows Mandarin terminology; identifying it unconditionally with 半单 would introduce modern terminology not checked here.", "Historical wording preserved without modernization."),
    term("segment A theorem", "größter kommutativer Unterkörper", "maximal commutative subfield of the division algebra or matrix ring", "极大交换子域", "極大交換子域", "A commutative subfield maximal by inclusion inside the specified noncommutative algebra.", "a commutative subfield of greatest numerical size; a maximum-degree field without the inclusion condition; a center", "最大交换子域; 极大可换子域", "modern Sino-xenic coinage/calque", "High: 极大 versus 最大 is a Mandarin sense trap parallel to minimal/maximal order language; regional wording is untested.", "Producer uses 极大 for inclusion-maximal."),
    term("segment A general characterization", "regulärer Fall", "the explicitly defined field-extension availability condition", "正则情形", "正則情形", "The article's named case in which every finite commutative extension admits further commutative extensions of arbitrary degree.", "a regular representation; a regular local ring; a smooth geometric point; merely the generic case", "正规情形; 常规情形", "mixed/contested", "High: 正则 has many modern Mandarin mathematical attractors; the article's local definition controls this occurrence, and regional terminology is untested.", "Sense must remain confined to the displayed definition."),
    term("segments A-C", "Quaternionenkörper", "Hamilton quaternion division algebra over the rationals", "四元数除环", "四元數除環", "The quaternion skew field/division algebra used as the example, considered as a hypercomplex system over the rational field.", "the quaternion group; all quaternion numbers without division-algebra emphasis; a four-element field", "四元数体; 四元数代数; Hamilton 四元数域", "mixed/contested", "High: 四元数除环 makes the algebraic structure explicit, but segment C's section heading also contains 四元数体; this unadjudicated producer variation is left for independent checking.", "The assembled draft contains both 四元数除环 and a section-heading 四元数体; producer does not self-adjudicate."),
    term("segment B characterization", "idempotentes Element", "nontrivial idempotent producing a decomposition", "幂等元素", "冪等元素", "An element $r$ satisfying $r^2=r$, specifically nonzero and nonunit in the splitting criterion.", "a nilpotent element; an identity element; an idempotent operation on functions without an algebra element", "幂等元; 等幂元素", "modern Sino-xenic coinage/calque", "Medium: 幂等元素 is Mainland-standard-looking; regional preference between 元素 and 元 is untested.", "The defining equation is retained adjacent to the term."),
    term("segment B ideal decomposition", "primitives idempotentes Element", "primitive idempotent corresponding to a simple one-sided ideal", "本原幂等元素", "本原冪等元素", "An idempotent that cannot be further decomposed in the relevant direct-sum decomposition and yields a simple ideal component.", "a primitive root; merely an initial idempotent; a central idempotent without primitivity", "原始幂等元; 本原幂等元", "modern Sino-xenic coinage/calque", "High: 本原 is a Mandarin choice shared with root terminology and can attract the wrong algebraic sense; regional usage is untested.", "Quotation marks from the source are retained around 本原."),
    term("segment B ideal account", "einseitig einfaches Ideal", "simple one-sided ideal generating an irreducible representation", "单侧单理想", "單側單理想", "A left- or right-sided ideal simple as a one-sided module, used to generate an irreducible representation.", "a two-sided simple ideal; a principal ideal; an ideal lying only on one geometric side", "单边单理想; 一侧单理想", "modern Sino-xenic coinage/calque", "High: 单侧单理想 compresses two distinct uses of 单 and is easy to misparse; regional terminology is untested.", "Producer keeps the historical one-sided formulation explicit."),
    term("segment C elementary treatment", "rationale Darstellung", "representation realizable over the stated field $K$", "有理表示", "有理表示", "A representation whose matrix entries lie in $K$, i.e. rational over $K$ in the historical field-of-definition sense.", "a representation over the rational numbers only; a logically reasonable representation; a rational function", "K-有理表示; 定义于 K 的表示", "mixed/contested", "High: 有理 can misleadingly suggest coefficients in $\\mathbb{Q}$; the local phrase 在域 K 上 controls the intended field-of-definition sense.", "The checker should consider whether explicit K-有理 wording is preferable."),
    term("segments A and C", "Faktorensystem", "factor set/cocycle used to construct the division algebra", "因子系", "因子系", "The multiplication factor system in projective representation and noncommutative-division-algebra construction.", "a system of numerical factors; a factorization algorithm; a quotient system without cocycle structure", "因子系统; 乘法因子集; 2-余循环", "modern Sino-xenic coinage/calque", "High: 因子系 is the inherited Mainland-oriented historical term and may be opaque or collide with generic factor systems; regional evidence is absent.", "Historical register retained; no modernization to cohomology language."),
    term("segment D norm argument", "Relativnorm", "field norm from $P(\\varepsilon,i)$ to $P(\\varepsilon)$", "相对范数", "相對範數", "The relative field norm for the quadratic extension used to express $-1$ as a sum of two squares.", "a vector norm relative to another norm; a normalized ratio; a quaternion norm in the earlier paragraph", "域范数; 相对域范数", "modern Sino-xenic coinage/calque", "Medium: 相对范数 is standard Mainland algebra wording but can attract analytic-norm senses; regional usage is untested.", "The source and target fields are named in the surrounding sentence."),
    term("segment D cyclotomic argument", "primitive p-te Einheitswurzel", "primitive $p$-th root of unity", "本原 $p$ 次单位根", "本原 $p$ 次單位根", "A root of unity of exact order $p$, denoted $\\varepsilon$ in the cyclotomic construction.", "a primitive polynomial root; the number one; a unit of a ring without root-of-unity status", "原始 $p$ 次单位根; 本原 $p$ 次根", "modern Sino-xenic coinage/calque", "Medium: 本原 is Mainland-standard-looking but competes with 原始 in some shelves and also appears in 本原幂等元; regional usage is untested.", "Exact order is supplied by the mathematical phrase."),
    term("segment D closing footnote", "Kreisteilungskörper", "cyclotomic field containing the selected cyclic subfield", "分圆域", "分圓域", "A field generated by roots of unity, here the ambient field from which a cyclic splitting subfield is chosen.", "a circular geometric domain; an arbitrary cyclic extension; a field quotient", "圆分域; 分圆体; cyclotomic 域", "modern Sino-xenic coinage/calque", "High: 分圆域 is Mainland-dominant terminology; Traditional regional shelves may prefer 圓分體/圓分域, which has not been researched here.", "Controlled Hant is generic script only and does not localize this lexical choice."),
]


TERM_FIELDS = [
    "decision_id", "source_locator", "exact_german_phrase", "concept_scope",
    "zh_hans_cn_choice", "sense_window", "excluded_senses", "alternatives_considered",
    "lexical_attractor_basin", "mandarin_simplified_dominance_risk_debt",
    "evidence_class", "controlled_hant_form", "controlled_hant_status",
    "independent_check_status", "producer_note",
]
ADVERSE_FIELDS = [
    "adverse_id", "term_decision_id", "source_locator", "exact_german_phrase",
    "zh_hans_cn_producer_choice", "trap_or_adverse_reading", "contextual_reason_for_exclusion",
    "alternative_held_for_independent_review", "lexical_attractor_basin",
    "mandarin_simplified_dominance_risk_debt", "evidence_class",
    "controlled_hant_status", "review_state",
]
CROSS_FIELDS = [
    "crosswalk_id", "term_decision_id", "source_locator", "exact_german_phrase",
    "zh_hans_cn_producer_form", "zh_hant_controlled_form", "zh_hant_status",
    "ja_form", "ko_form", "ja_ko_evidence_status", "sense_window", "excluded_senses",
    "lexical_attractor_basin", "mandarin_simplified_dominance_risk_debt",
    "evidence_class", "independent_check_status",
]


def write_csv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, quoting=csv.QUOTE_ALL, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


term_rows: list[dict[str, str]] = []
adverse_rows: list[dict[str, str]] = []
cross_rows: list[dict[str, str]] = []
nodes: list[dict[str, str]] = []
edges: list[dict[str, str]] = []

for index, item in enumerate(TERMS, 1):
    num = f"{index:03d}"
    decision = f"P32-ZH-T{num}"
    term_rows.append({
        "decision_id": decision,
        "source_locator": item["locator"],
        "exact_german_phrase": item["german"],
        "concept_scope": item["scope"],
        "zh_hans_cn_choice": item["hans"],
        "sense_window": item["window"],
        "excluded_senses": item["excluded"],
        "alternatives_considered": item["alternatives"],
        "lexical_attractor_basin": item["basin"],
        "mandarin_simplified_dominance_risk_debt": item["debt"],
        "evidence_class": EVIDENCE_CLASS,
        "controlled_hant_form": item["hant"],
        "controlled_hant_status": HANT_STATUS,
        "independent_check_status": REVIEW,
        "producer_note": item["note"],
    })
    adverse_rows.append({
        "adverse_id": f"P32-ZH-A{num}",
        "term_decision_id": decision,
        "source_locator": item["locator"],
        "exact_german_phrase": item["german"],
        "zh_hans_cn_producer_choice": item["hans"],
        "trap_or_adverse_reading": item["excluded"],
        "contextual_reason_for_exclusion": item["window"],
        "alternative_held_for_independent_review": item["alternatives"],
        "lexical_attractor_basin": item["basin"],
        "mandarin_simplified_dominance_risk_debt": item["debt"],
        "evidence_class": EVIDENCE_CLASS,
        "controlled_hant_status": HANT_STATUS,
        "review_state": REVIEW,
    })
    cross_rows.append({
        "crosswalk_id": f"P32-ZH-X{num}",
        "term_decision_id": decision,
        "source_locator": item["locator"],
        "exact_german_phrase": item["german"],
        "zh_hans_cn_producer_form": item["hans"],
        "zh_hant_controlled_form": item["hant"],
        "zh_hant_status": HANT_STATUS,
        "ja_form": "",
        "ko_form": "",
        "ja_ko_evidence_status": "JA and KO not consulted and not authorized as Chinese evidence",
        "sense_window": item["window"],
        "excluded_senses": item["excluded"],
        "lexical_attractor_basin": item["basin"],
        "mandarin_simplified_dominance_risk_debt": item["debt"],
        "evidence_class": EVIDENCE_CLASS,
        "independent_check_status": REVIEW,
    })

    loc = f"P32-LOC-{num}"
    concept = f"P32-CON-{num}"
    hans = f"P32-HANS-{num}"
    hant = f"P32-HANT-{num}"
    choice = f"P32-CHOICE-{num}"
    nodes.extend([
        {"id": loc, "type": "source_locus", "locator": item["locator"], "exact_german_phrase": item["german"]},
        {"id": concept, "type": "concept", "scope": item["scope"], "sense_window": item["window"], "excluded_senses": item["excluded"]},
        {"id": hans, "type": "form", "language_scope": "zh-Hans-CN producer", "form": item["hans"]},
        {"id": hant, "type": "form", "language_scope": "zh-Hant-controlled nonregional producer record", "form": item["hant"], "status": HANT_STATUS},
        {"id": choice, "type": "producer_choice", "decision_id": decision, "dominance_risk_debt": item["debt"], "evidence_class": EVIDENCE_CLASS, "review_state": REVIEW},
    ])
    edges.extend([
        {"id": f"P32-E{num}-1", "type": "occurs_at", "from": concept, "to": loc},
        {"id": f"P32-E{num}-2", "type": "decides_for", "from": choice, "to": concept},
        {"id": f"P32-E{num}-3", "type": "selects_hans_form", "from": choice, "to": hans},
        {"id": f"P32-E{num}-4", "type": "records_controlled_hant_form", "from": choice, "to": hant},
        {"id": f"P32-E{num}-5", "type": "controlled_form_of", "from": hant, "to": hans},
    ])

write_csv(EVIDENCE / "TERMINOLOGY_LEDGER.csv", TERM_FIELDS, term_rows)
write_csv(EVIDENCE / "ADVERSE_EVIDENCE_LEDGER.csv", ADVERSE_FIELDS, adverse_rows)
write_csv(EVIDENCE / "CJKV_CROSSWALK.csv", CROSS_FIELDS, cross_rows)

graph = {
    "graph_id": "NOE-P32-ZH-PRODUCER-CONCEPT-GRAPH-001",
    "work_unit": "Noether Paper 32 Chinese producer translation",
    "graph_status": {
        "purpose": "producer-side translation-decision evidence only",
        "decision_count": len(TERMS),
        "independent_check": "absent",
        "external_native_source_research": "not performed",
        "japanese_or_korean_evidence": "not consulted or used",
        "scan_inspection": "not performed",
        "source_branch_comparison": "not performed",
        "compilation_or_rendering": "mechanical XeLaTeX completed; rendered pages not inspected",
        "controlled_hant_scope": HANT_STATUS,
        "translation_validation_or_readiness_claim": "none",
    },
    "provenance": {
        "german_snapshot": {"path": "source/Noether_Paper32_German_current_exact_CRLF.tex", "sha256": SOURCE_SHA, "use": "translation source wording and locator only; no source check"},
        "inherited_hans_witness": {"path": "witness/Noether_Paper32_SimplifiedChinese_inherited_exact_CRLF.tex", "sha256": WITNESS_SHA, "use": "drafting witness only; not authority"},
        "hans_target": {"path": "zh-Hans-CN/Noether_Paper32_Chinese_CurrentAuthority_zh-Hans-CN_v001.tex", "sha256": HANS_SHA, "use": "producer choice record; independent check absent"},
        "controlled_hant_target": {"path": "zh-Hant-controlled/Noether_Paper32_Chinese_CurrentAuthority_zh-Hant-controlled_v001.tex", "sha256": HANT_SHA, "use": HANT_STATUS},
        "evidence_class": EVIDENCE_CLASS,
    },
    "node_type_definitions": {
        "source_locus": "Locator and phrase in the supplied German fragments; not a source-validation assertion.",
        "concept": "Producer's bounded sense window and excluded lexical attractors.",
        "form": "Proposed Chinese form with explicit Hans or nonregional controlled-Hant scope.",
        "producer_choice": "Editorial selection with qualitative Mandarin-Simplified dominance debt and open review state; lexical-attractor basin is recorded only in the CSV ledgers.",
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
(EVIDENCE / "CONCEPT_EVIDENCE_GRAPH.json").write_text(
    json.dumps(graph, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


summary = {
    "term_rows": len(term_rows),
    "adverse_rows": len(adverse_rows),
    "crosswalk_rows": len(cross_rows),
    "graph_nodes": len(nodes),
    "graph_edges": len(edges),
    "hashes": {path.name: sha(path) for path in sorted(EVIDENCE.iterdir()) if path.is_file()},
    "claim_limit": "Producer decision recording only; no independent checking or readiness claim.",
}
print(json.dumps(summary, ensure_ascii=False, indent=2))
