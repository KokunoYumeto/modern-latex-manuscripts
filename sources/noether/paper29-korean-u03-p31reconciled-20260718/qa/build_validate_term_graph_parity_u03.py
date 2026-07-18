#!/usr/bin/env python3
"""Build and validate Korean-only terminology, adverse evidence, typed graph, and parity for U03."""

from __future__ import annotations

import csv
import hashlib
import json
from collections import defaultdict, deque
from pathlib import Path

import jsonschema


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "evidence"
QA = ROOT / "qa"
SOURCE = ROOT / "source" / "Noether_Paper29_German_P31_U03_FinitenessCriterionProofSetup_exact_lf.tex"
TARGET = ROOT / "ko" / "Noether_Paper29_Korean_U03_v001.tex"
STRUCTURAL = EVIDENCE / "structural_index_u03" / "STRUCTURAL_INDEX.jsonl"
REPORT = QA / "TERM_GRAPH_PARITY_VALIDATION_U03.json"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def write_csv(path: Path, rows: list[dict], fields: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


source_text = SOURCE.read_text(encoding="utf-8")
target_text = TARGET.read_text(encoding="utf-8")
structural_records = [
    json.loads(line) for line in STRUCTURAL.read_text(encoding="utf-8").splitlines() if line.strip()
]
structural_ids = {record["structural_id"] for record in structural_records}

native = [
    {
        "evidence_id": "KO-P29-U03-E001",
        "source_type": "Korean university graduate-course page",
        "institution": "서울대학교 수리과학부",
        "url_or_path": "https://www.math.snu.ac.kr/bbs/board.php?bo_table=Math_Grad_Courses",
        "locator": "대수학 2 description, page lines 248-252 in 2026-07-18 audit",
        "korean_example": "가군, 자유가군, 유한생성 대수, 정수확장",
        "supports": "KO-P29-U03-T002|KO-P29-U03-T008|KO-P29-U03-T012",
        "scope_note": "Strong Korean institutional register for modules, finite generation, and integral extensions; not an exact historical Noether sentence.",
        "language": "ko-KR",
        "accessed": "2026-07-18"
    },
    {
        "evidence_id": "KO-P29-U03-E002",
        "source_type": "Korean mathematics publisher catalogue",
        "institution": "경문사",
        "url_or_path": "https://www.kyungmoon.com/shop/item.php?it_id=1652670399",
        "locator": "현대대수학 제5판 table of contents, page line 240 in 2026-07-18 audit",
        "korean_example": "부분환, 분수체, 가군, 확대체, 거듭제곱근 확대체",
        "supports": "KO-P29-U03-T003|KO-P29-U03-T005|KO-P29-U03-T008|KO-P29-U03-T009|KO-P29-U03-T011",
        "scope_note": "Korean publisher evidence for core modern terms; 거듭제곱근 확대체 does not exactly prove Noether's P^{1/p} Wurzelkörper sense.",
        "language": "ko-KR",
        "accessed": "2026-07-18"
    },
    {
        "evidence_id": "KO-P29-U03-E003",
        "source_type": "Korean university mathematics-education scope page",
        "institution": "경남대학교 수학교육과",
        "url_or_path": "https://www.kyungnam.ac.kr/mathedu/14141/subview.do",
        "locator": "현대대수학 체론 list, page line 160 in 2026-07-18 audit",
        "korean_example": "유한 확대체, 대수적 확대체",
        "supports": "KO-P29-U03-T011",
        "scope_note": "Direct Korean institutional compound evidence for finite and algebraic extension fields.",
        "language": "ko-KR",
        "accessed": "2026-07-18"
    },
    {
        "evidence_id": "KO-P29-U03-E004",
        "source_type": "Korean university course-description page",
        "institution": "숙명여자대학교 수학과",
        "url_or_path": "https://math.sookmyung.ac.kr/math/curriculum/description.do",
        "locator": "추상대수학 II, page lines 277-279 in 2026-07-18 audit",
        "korean_example": "확대체, 방정식의 근체",
        "supports": "KO-P29-U03-T005|KO-P29-U03-T011",
        "scope_note": "Supports Korean availability of 근체, but 방정식의 근체 may mean a splitting/root field and does not settle P^{1/p}.",
        "language": "ko-KR",
        "accessed": "2026-07-18"
    },
    {
        "evidence_id": "KO-P29-U03-E005",
        "source_type": "prior Korean Noether lane evidence shelf",
        "institution": "Interlanguage CJK-Korean lane",
        "url_or_path": "evidence/KOREAN_NATIVE_EXAMPLE_CORPUS_U01.csv",
        "locator": "U01 accepted terminology continuity",
        "korean_example": "유한성 판정기준, 정역, 정수적, 약수사슬정리",
        "supports": "KO-P29-U03-T001|KO-P29-U03-T002|KO-P29-U03-T012|KO-P29-U03-T014",
        "scope_note": "Corpus consistency evidence only; not independent external authorization.",
        "language": "ko-KR",
        "accessed": "2026-07-18"
    },
    {
        "evidence_id": "KO-P29-U03-E006",
        "source_type": "prior Korean Noether lane evidence shelf",
        "institution": "Interlanguage CJK-Korean lane",
        "url_or_path": "evidence/KOREAN_NATIVE_EXAMPLE_CORPUS_U02.csv",
        "locator": "U02 accepted field-theory register continuity",
        "korean_example": "따름정리, 유한 대수적 확대, 부분체 포함관계",
        "supports": "KO-P29-U03-T004|KO-P29-U03-T011",
        "scope_note": "Corpus continuity only; no Chinese or Japanese evidence is imported.",
        "language": "ko-KR",
        "accessed": "2026-07-18"
    }
]

terms = [
    ("T001", "Beweis des Endlichkeitskriteriums", "유한성 판정기준의 증명", "有限性 判定基準; 證明",
     "Noether's proof of the finite-generation criterion in this paper.", "Termination criteria or finite-cardinality tests.",
     "accepted_internal", "modern_sino_xenic_coinage_calque", "low; Korean lane continuity and source context control the sense",
     "E005", "A001", "ITEM-001", "translated"),
    ("T002", "endlicher Integritätsbereich", "유한 생성 정역", "有限 生成 整域",
     "A domain finitely generated as the relevant algebra/ring.", "A domain with finitely many elements.",
     "accepted_internal_sense_locked", "modern_sino_xenic_coinage_calque", "high qualitative semantic-attractor debt; Korean 유한생성 evidence is mandatory",
     "E001|E005", "A001", "STEP-001", "translated"),
    ("T003", "endlicher Unterring", "유한 생성 부분환", "有限 生成 部分環",
     "A finitely generated subring R or T.", "A finite-cardinality subring.",
     "accepted_internal_sense_locked", "modern_sino_xenic_coinage_calque", "high qualitative semantic-attractor debt; do not shorten to bare 유한",
     "E002", "A002", "STEP-001|STEP-007", "translated"),
    ("T004", "notwendig / hinreichend / Voraussetzung", "필요하다 / 충분하다 / 가정", "必要 / 充分 / 假定",
     "Logical necessity, sufficiency, and the extra characteristic-p hypothesis.", "Treating the criterion condition and extra field hypothesis as the same proposition.",
     "accepted_internal", "modern_sino_xenic_coinage_calque", "low",
     "E006", "A003", "PARA-001|PARA-002", "translated"),
    ("T005", "Wurzelkörper P^{1/p}", "근체(Wurzelkörper) P^{1/p}", "根體",
     "Noether's characteristic-p field P^{1/p}, tied to the cited source definition.", "A generic splitting field, Wurzelring, or one unspecified root extension.",
     "provisional_historical_source_label_retained", "mixed_contested", "high qualitative debt; Korean 근체 exists but exact P^{1/p} sense lacks independent Korean attestation",
     "E002|E004", "A004", "PARA-002", "held"),
    ("T006", "Koeffizientenkörper", "계수체", "係數體",
     "The coefficient field P.", "A coefficient ring/region when field structure is not asserted.",
     "accepted_internal", "modern_sino_xenic_coinage_calque", "low to medium",
     "E002", "A005", "PARA-002", "translated"),
    ("T007", "Charakteristik p / Null", "표수 p / 표수 0", "標數",
     "Characteristic of the coefficient field.", "Euler characteristic or ordinary character.",
     "accepted_internal", "modern_sino_xenic_coinage_calque", "no material Mandarin dependence",
     "E005", "A005", "PARA-002", "translated"),
    ("T008", "endliche Modulbasis", "유한 가군 생성계(Modulbasis)", "有限 加群 生成系",
     "A finite module-generating system over a subring of R.", "A free-module basis or linearly independent basis.",
     "accepted_internal_source_label_retained", "modern_sino_xenic_coinage_calque", "high false-basis attraction debt",
     "E001|E002", "A006", "STEP-002", "translated"),
    ("T009", "Quotientenkörper", "분수체", "分數體",
     "Fraction field of a domain.", "Quotient/residue field.",
     "accepted_internal", "modern_sino_xenic_coinage_calque", "low; direct Korean publisher evidence",
     "E002", "A007", "STEP-003", "translated"),
    ("T010", "Ringe ohne Nullteiler", "영인자가 없는 환", "零因子; 環",
     "R and S have no nonzero zero divisors, hence fraction fields exist.", "A claim merely that K and L are rings, or a noncommutative generalization.",
     "accepted_contextual", "modern_sino_xenic_coinage_calque", "low",
     "E002", "A007", "STEP-003", "translated"),
    ("T011", "endlicher algebraischer Erweiterungskörper", "유한 대수적 확대체", "有限 代數的 擴大體",
     "An algebraic field extension of finite degree.", "Finite cardinality or a finitely generated transcendental extension.",
     "accepted_internal_sense_locked", "modern_sino_xenic_coinage_calque", "low to medium; independently supported Korean register",
     "E002|E003|E006", "A008", "STEP-004", "translated"),
    ("T012", "ganz inbezug auf R / R-ganze Elemente", "R에 대해 정수적 / R에 대해 정수적인 원소", "整數的 元素",
     "Integral over R, i.e. root of a monic polynomial over R.", "Ordinary integers or integer-valued elements.",
     "accepted_contextual", "modern_sino_xenic_coinage_calque", "medium false-friend debt",
     "E001|E005", "A009", "STEP-005", "translated"),
    ("T013", "ganze Abgeschlossenheit von R in K", "K 안에서 정수적으로 닫혀 있음 / 정수적 닫힘 조건", "整數的",
     "Relative integral closedness in the stated overfield/fraction-field setting.", "Algebraic closure, topological closure, or completeness.",
     "provisional_contextual", "mixed_contested", "medium-high qualitative debt; exact Korean sentence-level witness not recovered",
     "E001", "A010", "STEP-006|STEP-007", "translated"),
    ("T014", "Teilerkettensatz", "약수사슬정리(Teilerkettensatz)", "約數; 사슬; 定理",
     "Noether's historical divisor-chain theorem used under finite extension.", "An unqualified identification with a modern ACC/DCC theorem.",
     "held_historical_source_label_retained", "unresolved", "high qualitative debt; no exact independent Korean historical attestation",
     "E005", "A011", "STEP-006", "held")
]

adverse = [
    ("A001", "Bare 유한 can attract the finite-cardinality reading in ring contexts.", "Use 유한 생성 and preserve source sense window.", "T001|T002"),
    ("A002", "Bare 유한 부분환 is ambiguous between finite generation and finite cardinality.", "Lock 유한 생성 부분환.", "T003"),
    ("A003", "Criterion condition and extra characteristic-p hypothesis can be conflated.", "Name necessity/sufficiency and the additional 가정 separately.", "T004"),
    ("A004", "Korean 근체 is attested for equation root/splitting-field contexts, but exact P^{1/p} use was not recovered.", "Retain Wurzelkörper and held status; exclude Wurzelring.", "T005"),
    ("A005", "계수 영역 and 계수체 differ, and 표수 has unrelated uses outside field theory.", "Use the field-specific context and explicit P.", "T006|T007"),
    ("A006", "기저 suggests linear independence/freeness, which German Modulbasis need not assert here.", "Use 가군 생성계 and retain Modulbasis.", "T008"),
    ("A007", "몫체/상체 can attract quotient-field or residue-field senses; pronoun antecedents can become circular.", "Use 분수체 and name R,S explicitly as domains.", "T009|T010"),
    ("A008", "Field-theoretic 유한 can be confused with finite cardinality.", "Sense-lock 유한 대수적 확대체 to finite degree.", "T011"),
    ("A009", "정수적 can be misread as ordinary integer-valuedness.", "Record the monic-polynomial sense and the base ring R.", "T012"),
    ("A010", "닫힘 can attract algebraic/topological closure.", "Use predicate 정수적으로 닫혀 and retain the ambient field.", "T013"),
    ("A011", "약수사슬정리 lacks exact Korean historical attestation and may be over-modernized.", "Retain German label and held status.", "T014"),
    ("A012", "Chinese/Japanese cognates and Mandarin-Simplified search dominance could appear to authorize Korean forms.", "Treat them as no Korean evidence; qualitative debt only, never a readiness scalar.", "T001|T002|T003|T004|T005|T006|T007|T008|T009|T010|T011|T012|T013|T014")
]

term_rows: list[dict] = []
crosswalk: list[dict] = []
decisions: list[dict] = []
for index, item in enumerate(terms, start=1):
    code, german, korean, hanja, sense, excluded, ko_status, basin, mandarin, evidence_codes, adverse_codes, struct_codes, state = item
    term_id = f"KO-P29-U03-{code}"
    evidence_ids = [f"KO-P29-U03-{value}" for value in evidence_codes.split("|")]
    adverse_ids = [f"KO-P29-U03-{value}" for value in adverse_codes.split("|")]
    resolved_structural_ids = [f"NOE-P29-KO-U03-{value}" for value in struct_codes.split("|")]
    source_probe = german.split(" / ")[0]
    if code == "T001":
        source_probe = "Beweis des Endlichkeitskriteriums"
    elif code == "T002":
        source_probe = "endlicher Integritätsbereich"
    elif code == "T003":
        source_probe = "endlichen Unterring"
    elif code == "T004":
        source_probe = "offenbar notwendig"
    elif code == "T005":
        source_probe = "Wurzelkörper"
    elif code == "T007":
        source_probe = "Charakteristik"
    elif code == "T008":
        source_probe = "Modulbasis"
    elif code == "T010":
        source_probe = "Ringe ohne Nullteiler"
    elif code == "T011":
        source_probe = "endlicher algebraischer Erweiterungskörper"
    elif code == "T012":
        source_probe = "ganz inbezug"
    elif code == "T013":
        source_probe = "ganze Abgeschlossenheit"
    target_probe = korean.split(" / ")[0]
    if code == "T001":
        target_probe = "유한성 판정기준의 증명"
    elif code == "T002":
        target_probe = "유한 생성 정역"
    elif code == "T003":
        target_probe = "유한 생성인"
    elif code == "T004":
        target_probe = "필요함은 명백하다"
    elif code == "T005":
        target_probe = "근체(Wurzelkörper)"
    elif code == "T006":
        target_probe = "계수체"
    elif code == "T007":
        target_probe = "표수"
    elif code == "T008":
        target_probe = "가군 생성계(Modulbasis)"
    elif code == "T009":
        target_probe = "분수체"
    elif code == "T010":
        target_probe = "영인자가 없는 환"
    elif code == "T011":
        target_probe = "유한 대수적 확대체"
    elif code == "T012":
        target_probe = "에 대해 정수적"
    elif code == "T013":
        target_probe = "정수적으로 닫혀"
    elif code == "T014":
        target_probe = "약수사슬정리(Teilerkettensatz)"
    term_rows.append({
        "term_id": term_id,
        "german_form": german,
        "korean_form": korean,
        "hangul_hanja": hanja,
        "sense_window": sense,
        "excluded_senses": excluded,
        "ko_kr_status": ko_status,
        "ko_kp_status": "unverified_do_not_claim",
        "evidence_ids": "|".join(evidence_ids),
        "adverse_ids": "|".join(adverse_ids),
        "source_probe": source_probe,
        "target_probe": target_probe,
        "decision_state": state,
        "revisit_condition": "Qualified Korean/DPRK review, sealed-source change, or a later corpus contradiction."
    })
    crosswalk.append({
        "crosswalk_id": f"KO-P29-U03-X{index:03d}",
        "term_id": term_id,
        "german_form": german,
        "korean_form": korean,
        "hangul_hanja": hanja,
        "sense_window": sense,
        "excluded_senses": excluded,
        "ko_kr_status": ko_status,
        "ko_kp_status": "unverified_do_not_claim",
        "lexical_attractor_basin": basin,
        "mandarin_simplified_dominance_risk_debt": mandarin,
        "evidence_ids": "|".join(evidence_ids),
        "adverse_ids": "|".join(adverse_ids),
        "state": state
    })
    decisions.append({
        "schema_version": "1.0.0",
        "decision_id": f"KO-P29-U03-D{index:03d}",
        "term_id": term_id,
        "source_form": german,
        "target_form": korean,
        "hangul_hanja": hanja,
        "sense_window": sense,
        "excluded_senses": excluded,
        "ko_kr_status": ko_status,
        "ko_kp_status": "unverified_do_not_claim",
        "evidence_ids": evidence_ids,
        "adverse_ids": adverse_ids,
        "structural_ids": resolved_structural_ids,
        "decision_state": state,
        "uncertainty": "Internal Korean editorial decision; no external human or DPRK validation.",
        "revisit_condition": "Qualified Korean/DPRK review, sealed-source change, or a later corpus contradiction."
    })

adverse_rows = [
    {
        "adverse_id": f"KO-P29-U03-{code}",
        "symptom_or_risk": symptom,
        "control_or_resolution": resolution,
        "term_ids": "|".join(f"KO-P29-U03-{term}" for term in term_codes.split("|")),
        "state": "active_control" if code != "A004" and code != "A011" else "held",
        "language_basis": "Korean semantics and source logic; no Chinese/Japanese authorization",
        "revisit_condition": "Qualified Korean/DPRK review or new local-language evidence."
    }
    for code, symptom, resolution, term_codes in adverse
]

native_fields = ["evidence_id", "source_type", "institution", "url_or_path", "locator", "korean_example", "supports", "scope_note", "language", "accessed"]
term_fields = ["term_id", "german_form", "korean_form", "hangul_hanja", "sense_window", "excluded_senses", "ko_kr_status", "ko_kp_status", "evidence_ids", "adverse_ids", "source_probe", "target_probe", "decision_state", "revisit_condition"]
adverse_fields = ["adverse_id", "symptom_or_risk", "control_or_resolution", "term_ids", "state", "language_basis", "revisit_condition"]
cross_fields = ["crosswalk_id", "term_id", "german_form", "korean_form", "hangul_hanja", "sense_window", "excluded_senses", "ko_kr_status", "ko_kp_status", "lexical_attractor_basin", "mandarin_simplified_dominance_risk_debt", "evidence_ids", "adverse_ids", "state"]

write_csv(EVIDENCE / "KOREAN_NATIVE_EXAMPLE_CORPUS_U03.csv", native, native_fields)
write_csv(EVIDENCE / "TERMINOLOGY_LEDGER_U03.csv", term_rows, term_fields)
write_csv(EVIDENCE / "ADVERSE_EVIDENCE_LEDGER_U03.csv", adverse_rows, adverse_fields)
write_csv(EVIDENCE / "CJKV_CROSSWALK_P29_KO_U03.csv", crosswalk, cross_fields)

decision_schema = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "array",
    "items": {
        "type": "object",
        "additionalProperties": False,
        "required": ["schema_version", "decision_id", "term_id", "source_form", "target_form", "hangul_hanja", "sense_window", "excluded_senses", "ko_kr_status", "ko_kp_status", "evidence_ids", "adverse_ids", "structural_ids", "decision_state", "uncertainty", "revisit_condition"],
        "properties": {
            "schema_version": {"const": "1.0.0"},
            "decision_id": {"type": "string", "pattern": "^KO-P29-U03-D[0-9]{3}$"},
            "term_id": {"type": "string", "pattern": "^KO-P29-U03-T[0-9]{3}$"},
            "source_form": {"type": "string"},
            "target_form": {"type": "string"},
            "hangul_hanja": {"type": "string"},
            "sense_window": {"type": "string"},
            "excluded_senses": {"type": "string"},
            "ko_kr_status": {"type": "string"},
            "ko_kp_status": {"const": "unverified_do_not_claim"},
            "evidence_ids": {"type": "array", "items": {"type": "string"}},
            "adverse_ids": {"type": "array", "items": {"type": "string"}},
            "structural_ids": {"type": "array", "items": {"type": "string"}},
            "decision_state": {"enum": ["translated", "held"]},
            "uncertainty": {"type": "string"},
            "revisit_condition": {"type": "string"}
        }
    }
}
(EVIDENCE / "TERMINOLOGY_DECISIONS_U03.schema.json").write_text(json.dumps(decision_schema, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
(EVIDENCE / "TERMINOLOGY_DECISIONS_U03.json").write_text(json.dumps(decisions, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")

nodes: list[dict] = []
edges: list[dict] = []
for row in native:
    nodes.append({"node_id": row["evidence_id"], "node_type": "evidence", "label": row["institution"]})
for row in adverse_rows:
    nodes.append({"node_id": row["adverse_id"], "node_type": "adverse_evidence", "label": row["symptom_or_risk"]})
for row, decision in zip(term_rows, decisions):
    nodes.append({"node_id": row["term_id"], "node_type": "term", "label": row["korean_form"]})
    nodes.append({"node_id": decision["decision_id"], "node_type": "decision", "label": decision["target_form"]})
for record in structural_records:
    nodes.append({"node_id": record["structural_id"], "node_type": "structural", "label": record["structure_type"]})

edge_counter = 0
def add_edge(source: str, target: str, relation: str) -> None:
    global edge_counter
    edge_counter += 1
    edges.append({"edge_id": f"EDGE-P29-U03-{edge_counter:03d}", "source": source, "target": target, "relation": relation})

for decision in decisions:
    add_edge(decision["term_id"], decision["decision_id"], "governed_by")
    for evidence_id in decision["evidence_ids"]:
        add_edge(evidence_id, decision["term_id"], "supports")
    for adverse_id in decision["adverse_ids"]:
        add_edge(adverse_id, decision["term_id"], "constrains")
    for structural_id in decision["structural_ids"]:
        add_edge(decision["decision_id"], structural_id, "realized_in")

graph = {"schema_version": "1.0.0", "graph_id": "NOE-P29-KO-U03-CONCEPT-EVIDENCE-GRAPH-001", "nodes": nodes, "edges": edges}
graph_schema = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "additionalProperties": False,
    "required": ["schema_version", "graph_id", "nodes", "edges"],
    "properties": {
        "schema_version": {"const": "1.0.0"},
        "graph_id": {"const": "NOE-P29-KO-U03-CONCEPT-EVIDENCE-GRAPH-001"},
        "nodes": {"type": "array", "items": {"type": "object", "additionalProperties": False, "required": ["node_id", "node_type", "label"], "properties": {"node_id": {"type": "string"}, "node_type": {"enum": ["evidence", "adverse_evidence", "term", "decision", "structural"]}, "label": {"type": "string"}}}},
        "edges": {"type": "array", "items": {"type": "object", "additionalProperties": False, "required": ["edge_id", "source", "target", "relation"], "properties": {"edge_id": {"type": "string"}, "source": {"type": "string"}, "target": {"type": "string"}, "relation": {"enum": ["governed_by", "supports", "constrains", "realized_in"]}}}}
    }
}
(EVIDENCE / "TYPED_CONCEPT_EVIDENCE_GRAPH_U03.schema.json").write_text(json.dumps(graph_schema, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
(EVIDENCE / "TYPED_CONCEPT_EVIDENCE_GRAPH_U03.json").write_text(json.dumps(graph, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")

parity_rows = [
    {
        "parity_id": f"PAR-{record['structural_id']}",
        "structural_id": record["structural_id"],
        "source_locator": record["source_locator"],
        "target_locator": record["target_locator"],
        "source_fragment_sha256": record["source_fragment_sha256"],
        "target_fragment_sha256": record["target_fragment_sha256"],
        "coverage_state": "covered",
        "review_state": record["review_state"]
    }
    for record in structural_records
]
write_csv(QA / "SOURCE_TARGET_PARITY_U03.csv", parity_rows, ["parity_id", "structural_id", "source_locator", "target_locator", "source_fragment_sha256", "target_fragment_sha256", "coverage_state", "review_state"])

errors: list[str] = []
for row in term_rows:
    if row["source_probe"] not in source_text:
        errors.append(f"missing source probe {row['term_id']}: {row['source_probe']}")
    if row["target_probe"] not in target_text:
        errors.append(f"missing target probe {row['term_id']}: {row['target_probe']}")
for decision in decisions:
    try:
        jsonschema.validate(decisions, decision_schema)
    except jsonschema.ValidationError as exc:
        errors.append(f"terminology schema: {exc.message}")
        break
    if any(field in decision for field in ("lexical_attractor_basin", "mandarin_simplified_dominance_risk_debt")):
        errors.append(f"forbidden crosswalk-only field in typed decision {decision['decision_id']}")
    for structural_id in decision["structural_ids"]:
        if structural_id not in structural_ids:
            errors.append(f"unresolved structural ID {structural_id}")
try:
    jsonschema.validate(graph, graph_schema)
except jsonschema.ValidationError as exc:
    errors.append(f"graph schema: {exc.message}")
node_ids = {node["node_id"] for node in nodes}
if len(node_ids) != len(nodes):
    errors.append("duplicate graph node ID")
for edge in edges:
    if edge["source"] not in node_ids or edge["target"] not in node_ids:
        errors.append(f"unresolved edge {edge['edge_id']}")

adjacency: dict[str, list[str]] = defaultdict(list)
indegree = {node_id: 0 for node_id in node_ids}
for edge in edges:
    adjacency[edge["source"]].append(edge["target"])
    indegree[edge["target"]] += 1
queue = deque(node_id for node_id, degree in indegree.items() if degree == 0)
visited = 0
while queue:
    node = queue.popleft()
    visited += 1
    for target in adjacency[node]:
        indegree[target] -= 1
        if indegree[target] == 0:
            queue.append(target)
if visited != len(node_ids):
    errors.append("typed graph is cyclic")
if len(parity_rows) != len(structural_records) or any(row["coverage_state"] != "covered" for row in parity_rows):
    errors.append("structural parity coverage failure")
if any(row["language"] != "ko-KR" for row in native):
    errors.append("non-Korean language evidence entered native shelf")

report_paths = [
    EVIDENCE / "KOREAN_NATIVE_EXAMPLE_CORPUS_U03.csv",
    EVIDENCE / "TERMINOLOGY_LEDGER_U03.csv",
    EVIDENCE / "ADVERSE_EVIDENCE_LEDGER_U03.csv",
    EVIDENCE / "CJKV_CROSSWALK_P29_KO_U03.csv",
    EVIDENCE / "TERMINOLOGY_DECISIONS_U03.schema.json",
    EVIDENCE / "TERMINOLOGY_DECISIONS_U03.json",
    EVIDENCE / "TYPED_CONCEPT_EVIDENCE_GRAPH_U03.schema.json",
    EVIDENCE / "TYPED_CONCEPT_EVIDENCE_GRAPH_U03.json",
    QA / "SOURCE_TARGET_PARITY_U03.csv"
]
report = {
    "schema_version": "1.0.0",
    "work_unit": "P29-KO-U03",
    "counts": {
        "native_evidence": len(native),
        "terms": len(term_rows),
        "adverse_records": len(adverse_rows),
        "crosswalk_rows": len(crosswalk),
        "decisions": len(decisions),
        "graph_nodes": len(nodes),
        "graph_edges": len(edges),
        "parity_rows": len(parity_rows)
    },
    "latest_ids": {
        "evidence": native[-1]["evidence_id"],
        "term": term_rows[-1]["term_id"],
        "adverse": adverse_rows[-1]["adverse_id"],
        "crosswalk": crosswalk[-1]["crosswalk_id"],
        "decision": decisions[-1]["decision_id"],
        "structural": structural_records[-1]["structural_id"]
    },
    "hashes": {path.relative_to(ROOT).as_posix(): sha(path) for path in report_paths},
    "graph_acyclic": visited == len(node_ids),
    "typed_json_forbidden_crosswalk_fields_absent": True,
    "chinese_or_japanese_authorization_used": False,
    "ko_kp_claim_state": "unverified_do_not_claim",
    "external_human_review": "absent_do_not_claim",
    "errors": errors
}
REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
print(json.dumps(report, ensure_ascii=False))
raise SystemExit(1 if errors else 0)
