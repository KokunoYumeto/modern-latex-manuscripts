#!/usr/bin/env python3
"""Build producer-side Paper 41 terminology evidence without checking claims."""

from pathlib import Path
import csv
import hashlib
import json


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "evidence"
OUT.mkdir(parents=True, exist_ok=True)

SOURCE_SHA = "C265058425E5E2D1A2289CC03A9DDEDDDF4803A3215DC3F173B93E7AB69D60ED"
WITNESS_SHA = "C6A2B4E40700A7E1A32AAEB76227DCD4335777616A595AAB6A4909BAB83554DB"
HANS_SHA = "97142978B30DC21C27D6C30A9CF18C0408F514C08D7A2CEF5649299D3B91E9F0"
HANT_SHA = "C5EB70BF90AA824D9B8281BB68780B0BA7269D3A8BCD3CD30A3F1BBEB2AE5F23"
EVIDENCE_CLASS = (
    "producer editorial choice plus inherited Simplified-Chinese witness; "
    "independent checking absent"
)
HANT_STATUS = "controlled generic script derivative; not zh-Hant-TW/HK/MO"
CHECK_STATUS = "independent check pending"


# id, locator, German, scope, Hans, Hant, sense, excluded, alternatives,
# basin, dominance debt, adverse trap, held alternative, producer note
TERMS = [
    ("P41-ZH-T001", "title; §1 theorem; §2 theorem", "Hauptgeschlechtssatz", "principal-genus theorem in algebraic number theory", "主属定理", "主屬定理", "The theorem about the principal genus in relative Galois number fields and its algebraic minimal analogue.", "generic main category; biological genus; principal class theorem", "主种定理; 主属定理（保留）", "modern Sino-xenic coinage/calque", "High: Mainland 主属 is the lexical base; regional acceptability is untested.", "主类别定理", "主种定理", "Kept distinct from Hauptklasse/主类."),
    ("P41-ZH-T002", "title and opening", "relativ-galoissche Zahlkörper", "number-field extension Galois over a specified base", "相对伽罗瓦数域", "相對伽羅瓦數域", "A number field considered as a Galois extension relative to its lower field.", "relative Galois numbers; an absolute Galois field", "相对 Galois 数域; 相对伽罗瓦扩张", "modern Sino-xenic coinage/calque", "Medium: Mainland transliteration and compressed 数域 phrasing may not be region-neutral.", "相对的伽罗瓦数", "相对伽罗瓦扩张", "Title form follows the producer's concise mathematical register."),
    ("P41-ZH-T003", "§1 heading and theorem", "im Minimalen", "minimal algebraic case of the theorem", "最小情形", "最小情形", "The paper's named minimal case over an arbitrary commutative field.", "minimum numerical value; local small case", "极小情形; 最小情况", "modern Sino-xenic coinage/calque", "Medium: Mainland 情形 preference may obscure alternative regional phrasing.", "在最小值中", "极小情形", "Contrast with im Kleinen is deliberately retained."),
    ("P41-ZH-T004", "opening footnote", "im Kleinen", "the historically named small/local case", "小情形", "小情形", "The 'small case' contrasted by Noether with the minimal algebraic analogue.", "minimal case; merely easy case", "小范围情形; 局部情形", "mixed/contested", "Medium: the literal Mainland-style label may not be established terminology elsewhere.", "容易情形", "局部情形", "Held separate from 最小情形."),
    ("P41-ZH-T005", "§1.1 throughout", "verschränktes Produkt", "crossed-product algebra", "交叉积", "交叉積", "The algebra generated from K and its Galois group with a factor system.", "tensor product; direct product; Cartesian product", "扭积; 交错积", "modern Sino-xenic coinage/calque", "High: 交叉积 is Mainland-dominant and could mask other CJK-derived conventions.", "普通乘积", "扭积", "Used consistently for the historical algebraic construction."),
    ("P41-ZH-T006", "§1.2 theorem forms", "verschränkte Darstellung", "crossed representation governed by a factor system", "交叉表示", "交叉表示", "A representation compatible with the crossed-product/factor-system relations.", "informal interlaced presentation; ordinary linear representation without cocycle", "射影表示; 扭表示", "modern Sino-xenic coinage/calque", "High: 交叉表示 is a producer calque, not independently established across regions.", "交错的陈述", "射影表示", "Historical scope is narrower than a generic projective representation."),
    ("P41-ZH-T007", "§1.1 equations (3)–(5); §2", "Faktorensystem", "factor set / multiplicative cocycle of the crossed product", "因子系", "因子系", "The indexed multiplicative data a_{S,T} satisfying the associativity relation.", "list of numerical factors; factorization system", "因子集; 因子组", "modern Sino-xenic coinage/calque", "High: 因子系 reflects the inherited Mainland shelf and may compete with 因子集.", "因数系统", "因子集", "Choice preserves the producer's historical register."),
    ("P41-ZH-T008", "§1.1 after equation (4)", "einfache normale Algebra", "historical term for a central simple algebra", "中心单代数", "中心單代數", "A finite-dimensional central simple algebra over the base field in this context.", "merely simple normal algebra; normal extension", "单纯正规代数; 简单正规代数", "modern Sino-xenic coinage/calque", "High: modern Mainland normalization suppresses the historical wording and needs checker review.", "简单的正规代数", "简单正规代数", "Modern structural term selected for clarity; historical equivalence remains reviewable."),
    ("P41-ZH-T009", "opening; §2 auxiliary lemma 2", "zerfallende Algebra", "split algebra", "分裂代数", "分裂代數", "An algebra split over the relevant field/place.", "decomposable algebra; algebra breaking into components", "裂代数; 可分解代数", "modern Sino-xenic coinage/calque", "Medium: 分裂 is Mainland-normalized but broadly Sino-xenic; regional prose untested.", "分解代数", "裂代数", "Kept distinct from decomposition of ideals or groups."),
    ("P41-ZH-T010", "§1.1 after equation (4)", "Zerfällungskörper", "splitting field of the algebra", "分裂域", "分裂域", "A field over which the algebra becomes split.", "field decomposition; residue field", "分解域; 裂域", "modern Sino-xenic coinage/calque", "Medium: the form is Mainland lexical base; local conventional variants were not researched.", "分解体", "裂域", "Producer kept standard modern algebraic usage."),
    ("P41-ZH-T011", "§1.1 after equation (5); §2", "Transformationsgrößen", "coboundary-type transformation quantities", "变换量", "變換量", "The quantities c_S^T c_T / c_{ST} that relate associated factor systems.", "transformation matrices; geometric coordinate transforms", "变换因子; 转换量", "modern Sino-xenic coinage/calque", "High: 变换量 follows Mainland phrasing and may invite a matrix reading.", "变换矩阵", "变换因子", "Sense window is fixed by equation (5)."),
    ("P41-ZH-T012", "§1.2 opening", "Komplexe u_S K^*", "cosets making up the extension group", "陪集", "陪集", "The cosets u_S K^* in the group extension, not complex numbers.", "complex numbers; algebraic complexes as analytic objects", "复形; 复集", "Sino-xenic inherited", "Medium: 陪集 is standard Mainland group terminology; the historical Komplexe nuance is not represented.", "复数 u_S K^*", "复集", "The producer translates the mathematical role rather than calquing Komplexe."),
    ("P41-ZH-T013", "§1.2 characterization of G*", "reguläre Elemente", "invertible elements in the algebra/group-extension context", "（可逆）元素", "（可逆）元素", "Elements invertible for the conjugation action used here.", "regular element in algebraic geometry; non-zero-divisor without invertibility", "正则元素; 非奇异元素", "mixed/contested", "High: 可逆 resolves one contextual sense but may be narrower than historical regulär.", "正则元素（不加限定）", "正则元素", "Parentheses flag the producer's contextual interpretation for checker review."),
    ("P41-ZH-T014", "§2.1", "Hauptklasse", "principal ideal class", "主类", "主類", "The distinguished principal class in an ideal-class partition.", "main category; principal genus", "首要类; 单位类", "Sino-xenic inherited", "Medium: 主类 is Mainland base and must remain distinct from 主属.", "主要类别", "单位类", "Term is paired explicitly with 主属."),
    ("P41-ZH-T015", "§2.2", "Hauptgeschlecht", "principal genus of ideal classes", "主属", "主屬", "The genus containing the class vectors whose transformation quantities lie in the induced principal class.", "principal ideal class; generic main genus", "主种; 首属", "modern Sino-xenic coinage/calque", "High: 主属 is a Mainland-oriented established attractor and not regionally validated.", "主类", "主种", "Kept distinct from Hauptklasse/主类."),
    ("P41-ZH-T016", "§2.1 definition", "induzierte Idealklasseneinteilung", "factor-system-induced ideal-class partition", "诱导理想类划分", "誘導理想類劃分", "The finer ideal-class equivalence induced by admissible factor systems.", "arbitrary taxonomy; induced module decomposition", "诱导理想类分解; 诱导理想类分类", "modern Sino-xenic coinage/calque", "High: 划分 is Mainland wording and may differ in regional expository prose.", "理想类别的分类", "诱导理想类分解", "The producer uses 划分 to emphasize equivalence classes."),
    ("P41-ZH-T017", "§2 auxiliary lemma 2", "Verzweigungsstellen", "ramified places, finite and infinite", "分歧位", "分歧位", "Places of the base/extension where ramification occurs, explicitly including finite and infinite places.", "only ramified prime ideals; branch points of a covering", "分歧处; 分歧素位", "modern Sino-xenic coinage/calque", "Medium: 位 is concise Mainland number-theory register; regional terminology was not consulted.", "分支点", "分歧处", "The wider term avoids narrowing to finite primes."),
    ("P41-ZH-T018", "§2 proof after local factor systems", "normierte zyklische Darstellung", "normalized cyclic presentation of a cyclic algebra", "规范化的循环表示", "規範化的循環表示", "The standard normalized cyclic-algebra presentation (1')–(5').", "normal representation via norm map; normalized statistical display", "标准化循环表示; 正规化循环表示", "modern Sino-xenic coinage/calque", "High: 规范化 is Mainland-dominant; regional technical preference is unknown.", "范数化循环表示", "标准化循环表示", "Normiert is read as normalized, not related to the norm map."),
    ("P41-ZH-T019", "final paragraph", "Normenrest", "number-theoretic norm residue", "范数剩余", "範數剩餘", "A residue condition expressing whether an element is locally a norm.", "elementary arithmetic remainder; residual norm value", "范数余数; 范数留数", "modern Sino-xenic coinage/calque", "High: 范数剩余 is inherited Mainland terminology and local variants remain unresearched.", "范数余数", "范数留数", "Context is local/global norm-residue theory."),
    ("P41-ZH-T020", "§2.1 opening", "Strahlklassen", "ray classes in class field theory", "射线类", "射線類", "Ray classes in the lower field, contrasted with absolute ideal classes upstairs.", "geometric rays; radiation categories", "模类; 射类", "modern Sino-xenic coinage/calque", "Medium: 射线类 is Mainland lexical base; no regional evidence was consulted.", "光线类别", "射类", "Used as the established producer-side class-field-theory term."),
]


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


term_rows = []
adverse_rows = []
crosswalk_rows = []
nodes = []
edges = []

for index, item in enumerate(TERMS, 1):
    (decision_id, locator, german, scope, hans, hant, sense, excluded,
     alternatives, basin, debt, trap, held, note) = item
    term_rows.append({
        "decision_id": decision_id,
        "source_locator": locator,
        "exact_german_phrase": german,
        "concept_scope": scope,
        "zh_hans_cn_choice": hans,
        "sense_window": sense,
        "excluded_senses": excluded,
        "alternatives_considered": alternatives,
        "lexical_attractor_basin": basin,
        "mandarin_simplified_dominance_risk_debt": debt,
        "evidence_class": EVIDENCE_CLASS,
        "controlled_hant_form": hant,
        "controlled_hant_status": HANT_STATUS,
        "independent_check_status": CHECK_STATUS,
        "producer_note": note,
    })
    adverse_rows.append({
        "adverse_id": f"P41-ZH-A{index:03d}",
        "term_decision_id": decision_id,
        "source_locator": locator,
        "exact_german_phrase": german,
        "zh_hans_cn_producer_choice": hans,
        "trap_or_adverse_reading": trap,
        "contextual_reason_for_exclusion": sense,
        "alternative_held_for_independent_review": held,
        "lexical_attractor_basin": basin,
        "mandarin_simplified_dominance_risk_debt": debt,
        "evidence_class": EVIDENCE_CLASS,
        "controlled_hant_status": HANT_STATUS,
        "review_state": CHECK_STATUS,
    })
    crosswalk_rows.append({
        "crosswalk_id": f"P41-ZH-X{index:03d}",
        "term_decision_id": decision_id,
        "source_locator": locator,
        "exact_german_phrase": german,
        "zh_hans_cn_producer_form": hans,
        "zh_hant_controlled_form": hant,
        "zh_hant_status": HANT_STATUS,
        "ja_form": "",
        "ko_form": "",
        "ja_ko_evidence_status": "not consulted and not authorized as Chinese evidence",
        "sense_window": sense,
        "excluded_senses": excluded,
        "lexical_attractor_basin": basin,
        "mandarin_simplified_dominance_risk_debt": debt,
        "evidence_class": EVIDENCE_CLASS,
        "independent_check_status": CHECK_STATUS,
    })

    locus_id = f"P41-LOC-{index:03d}"
    concept_id = f"P41-CON-{index:03d}"
    hans_id = f"P41-HANS-{index:03d}"
    hant_id = f"P41-HANT-{index:03d}"
    choice_id = f"P41-CHOICE-{index:03d}"
    nodes.extend([
        {"id": locus_id, "type": "source_locus", "locator": locator, "exact_german_phrase": german},
        {"id": concept_id, "type": "concept", "scope": scope, "sense_window": sense, "excluded_senses": excluded},
        {"id": hans_id, "type": "form", "language_scope": "zh-Hans-CN producer", "form": hans},
        {"id": hant_id, "type": "form", "language_scope": "zh-Hant-controlled nonregional", "form": hant},
        {"id": choice_id, "type": "producer_choice", "decision_id": decision_id, "basin": basin, "dominance_risk_debt": debt, "review_state": CHECK_STATUS},
    ])
    edges.extend([
        {"id": f"P41-E{index:03d}-1", "type": "occurs_at", "from": concept_id, "to": locus_id},
        {"id": f"P41-E{index:03d}-2", "type": "decides_for", "from": choice_id, "to": concept_id},
        {"id": f"P41-E{index:03d}-3", "type": "selects_hans_form", "from": choice_id, "to": hans_id},
        {"id": f"P41-E{index:03d}-4", "type": "records_controlled_hant_form", "from": choice_id, "to": hant_id},
        {"id": f"P41-E{index:03d}-5", "type": "controlled_form_of", "from": hant_id, "to": hans_id},
    ])


write_csv(
    OUT / "PRODUCER_TERMINOLOGY_LEDGER.csv",
    ["decision_id", "source_locator", "exact_german_phrase", "concept_scope",
     "zh_hans_cn_choice", "sense_window", "excluded_senses", "alternatives_considered",
     "lexical_attractor_basin", "mandarin_simplified_dominance_risk_debt",
     "evidence_class", "controlled_hant_form", "controlled_hant_status",
     "independent_check_status", "producer_note"],
    term_rows,
)
write_csv(
    OUT / "ADVERSE_SENSE_LEDGER.csv",
    ["adverse_id", "term_decision_id", "source_locator", "exact_german_phrase",
     "zh_hans_cn_producer_choice", "trap_or_adverse_reading",
     "contextual_reason_for_exclusion", "alternative_held_for_independent_review",
     "lexical_attractor_basin", "mandarin_simplified_dominance_risk_debt",
     "evidence_class", "controlled_hant_status", "review_state"],
    adverse_rows,
)
write_csv(
    OUT / "CJKV_CROSSWALK_P41_ZH.csv",
    ["crosswalk_id", "term_decision_id", "source_locator", "exact_german_phrase",
     "zh_hans_cn_producer_form", "zh_hant_controlled_form", "zh_hant_status",
     "ja_form", "ko_form", "ja_ko_evidence_status", "sense_window", "excluded_senses",
     "lexical_attractor_basin", "mandarin_simplified_dominance_risk_debt",
     "evidence_class", "independent_check_status"],
    crosswalk_rows,
)

graph = {
    "graph_id": "NOE-P41-ZH-PRODUCER-CONCEPT-GRAPH-001",
    "work_unit": "Noether Paper 41 Chinese producer translation",
    "graph_status": {
        "purpose": "producer-side translation-decision evidence only",
        "independent_check": "absent",
        "external_native_source_research": "not performed",
        "japanese_or_korean_evidence": "not consulted or used",
        "scan_inspection": "not performed",
        "source_branch_comparison": "not performed",
        "translation_validation_or_readiness_claim": "none",
    },
    "provenance": {
        "german_snapshot": {"path": "source/Noether_Paper41_CurrentGermanAuthority_interval.tex", "sha256": SOURCE_SHA, "use": "translation source wording and locator only; no source check"},
        "inherited_hans_witness": {"path": "witness/Noether_Paper41_InheritedSimplifiedChinese_interval.tex", "sha256": WITNESS_SHA, "use": "drafting witness only; not authority"},
        "hans_target": {"path": "zh-Hans-CN/Noether_Paper41_Chinese_CurrentAuthority_zh-Hans-CN_v001.tex", "sha256": HANS_SHA, "use": "producer choice record; independent check pending"},
        "controlled_hant_target": {"path": "zh-Hant-controlled/Noether_Paper41_Chinese_CurrentAuthority_zh-Hant-controlled_v001.tex", "sha256": HANT_SHA, "use": "nonregional script derivative; independent check pending"},
        "evidence_class": EVIDENCE_CLASS,
    },
    "node_type_definitions": {
        "source_locus": "Locator and phrase in the supplied source snapshot; not a source-validation assertion.",
        "concept": "Producer's bounded sense window and excluded attractors.",
        "form": "Proposed Chinese form with explicit script/language scope.",
        "producer_choice": "Editorial selection with basin, dominance debt, and open review state.",
    },
    "edge_type_definitions": {
        "occurs_at": "Concept to supplied-source locator.",
        "decides_for": "Producer choice to concept.",
        "selects_hans_form": "Producer choice to Hans form.",
        "records_controlled_hant_form": "Producer choice to nonregional Hant form.",
        "controlled_form_of": "Hant script form to Hans lexical base without regional equivalence claim.",
    },
    "nodes": nodes,
    "edges": edges,
}
(OUT / "PRODUCER_CONCEPT_GRAPH.json").write_text(
    json.dumps(graph, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
)


def sha_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


report = {
    path.name: {"sha256": sha_file(path), "bytes": path.stat().st_size}
    for path in sorted(OUT.iterdir()) if path.is_file()
}
print(json.dumps({"rows": len(TERMS), "nodes": len(nodes), "edges": len(edges), "files": report}, indent=2))
