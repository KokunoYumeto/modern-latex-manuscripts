#!/usr/bin/env python3
"""Build and validate Korean terminology, evidence, graph, and parity for P29 U02."""

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
SOURCE = ROOT / "source" / "Noether_Paper29_German_P31_U02_Rationalbasis_exact_lf.tex"
TARGET = ROOT / "ko" / "Noether_Paper29_Korean_U02_v001.tex"
STRUCTURE = EVIDENCE / "structural_index_u02" / "STRUCTURAL_INDEX.jsonl"
REPORT = QA / "TERM_GRAPH_PARITY_VALIDATION_U02.json"

SOURCE_SHA = "B7EF88537BCD90D0408B3D1942DA410410FE45E79DD457B2DF6DFA2D4929DCAC"
TARGET_SHA = "B694D05E57B58E1B0373D976356E6B3B3F4883D7CC9398081DB12111877B6A7C"
STRUCTURE_SHA = "F6954C84D72F3E5C02DAEF3B7B1BFF239587A1ECEEA6D7472B8A6EC00C96B60A"
U01_CORPUS_SHA = "094DC30AE83FFD9F461BABDF03135D7CCBF9587D09B0B73958C293144F2B7B89"

ALLOWED_BASINS = {
    "Sino-xenic inherited",
    "modern Sino-xenic coinage/calque",
    "global modern loan",
    "native coinage",
    "mixed/contested",
    "unresolved",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def write_csv(path: Path, rows: list[dict], fields: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


evidence_rows = [
    {
        "evidence_id": "KO-P29-U02-E001",
        "language": "ko",
        "standard": "ko-KR",
        "source_title": "조선대학교 기관저장소 학위논문: 합성 Hurwitz 다항식환 h(Z,Q)의 고차 기약 다항식 분류",
        "source_url": "https://oak.chosun.ac.kr/bitstream/2020.oak/17751/2/%ED%95%A9%EC%84%B1%20Hurwitz%20%EB%8B%A4%ED%95%AD%EC%8B%9D%ED%99%98%20h%28Z%2CQ%29%EC%9D%98%20%EA%B3%A0%EC%B0%A8%20%EA%B8%B0%EC%95%BD%20%EB%8B%A4%ED%95%AD%EC%8B%9D%20%EB%B6%84%EB%A5%98.pdf",
        "source_class": "institutional_repository_thesis",
        "observed_terms": "표수|정역|계수|다항식",
        "observation": "Korean algebra prose uses 표수, 정역, 계수, and 다항식 in their mathematical senses.",
        "accessed": "2026-07-18",
        "scope_limit": "Does not attest Noether's historical Rationalbasis or Steinitz's irreduzibles System.",
        "provenance": f"Carried forward from U01 Korean shelf {U01_CORPUS_SHA}; page binary not archived by this lane.",
    },
    {
        "evidence_id": "KO-P29-U02-E002",
        "language": "ko",
        "standard": "ko-KR",
        "source_title": "목원대학교 KOCW 현대대수학 강의계획",
        "source_url": "https://www.kocw.net/home/search/kemView.do?kemId=1160129",
        "source_class": "university_open_course",
        "observed_terms": "환|정역|표수|분수체|체|아이디얼",
        "observation": "The university course outline confirms the core Korean algebra register 체, 정역, 표수, and 분수체.",
        "accessed": "2026-07-18",
        "scope_limit": "Syllabus evidence; it does not settle the historical compounds in U02.",
        "provenance": f"Carried forward from U01 Korean shelf {U01_CORPUS_SHA}; page binary not archived by this lane.",
    },
    {
        "evidence_id": "KO-P29-U02-E003",
        "language": "ko",
        "standard": "ko-KR",
        "source_title": "경문사 현대대수학 제5판 공식 도서정보",
        "source_url": "https://www.kyungmoon.com/shop/item.php?it_id=1652670399",
        "source_class": "academic_publisher_catalog",
        "observed_terms": "부분환|분수체|정역|가군|체|확대체|분해체",
        "observation": "An academic publisher's official contents confirm 체, 확대체, and related modern Korean algebra headwords.",
        "accessed": "2026-07-18",
        "scope_limit": "Contents do not define transcendence degree or the exact historical compounds.",
        "provenance": f"Carried forward from U01 Korean shelf {U01_CORPUS_SHA}; page binary not archived by this lane.",
    },
    {
        "evidence_id": "KO-P29-U02-E004",
        "language": "ko",
        "standard": "ko-KR",
        "source_title": "경문사 현대대수학 제8판 공식 도서정보",
        "source_url": "https://www.kyungmoon.com/shop/item.php?it_id=1652670287",
        "source_class": "academic_publisher_catalog",
        "observed_terms": "부분환|정역|분수체|표수|유한군|갈루아",
        "observation": "Independent textbook contents corroborate the modern Korean core algebra register.",
        "accessed": "2026-07-18",
        "scope_limit": "Does not establish U02 field-extension compounds verbatim.",
        "provenance": f"Carried forward from U01 Korean shelf {U01_CORPUS_SHA}; page binary not archived by this lane.",
    },
    {
        "evidence_id": "KO-P29-U02-E005",
        "language": "ko",
        "standard": "ko-KR",
        "source_title": "서울대학교 수리과학부 대학원 대수학 2 교과목 개요",
        "source_url": "https://www.math.snu.ac.kr/bbs/board.php?bo_table=Math_Grad_Courses",
        "source_class": "official_university_course_catalog",
        "observed_terms": "가군|유한생성 대수|정수확장",
        "observation": "The official course description supports finite-generation and extension language and blocks a finite-cardinality reading of Noether's endlich.",
        "accessed": "2026-07-18",
        "scope_limit": "Does not attest Rationalbasis, Transzendenzgrad, or Vereinigungskörper verbatim.",
        "provenance": f"Carried forward from U01 Korean shelf {U01_CORPUS_SHA}; page binary not archived by this lane.",
    },
    {
        "evidence_id": "KO-P29-U02-E006",
        "language": "ko",
        "standard": "ko-KR",
        "source_title": "경문사 현대대수학 공식 연습문제 해답 PDF",
        "source_url": "https://www.kyungmoon.com/data/item/1652669905/file/982985700_Qz2Feb1v_380da3ca574a9e83f826456fc747b1383af0e56e.pdf",
        "source_class": "academic_publisher_official_supplement",
        "observed_terms": "중간체|유한 정규확대체|갈루아확대체|따름정리|계수",
        "observation": "Publisher-hosted algebra solutions use 중간체, finite/normal extension compounds, 따름정리, and 계수 in field-theory arguments.",
        "accessed": "2026-07-18",
        "scope_limit": "Modern solution manual; not historical Noether/Steinitz terminology and not an exact witness for every U02 compound.",
        "provenance": "New Korean-local evidence for U02; inspected web PDF lines 8945-9004; page binary not copied into the lane.",
    },
    {
        "evidence_id": "KO-P29-U02-E007",
        "language": "ko",
        "standard": "ko-KR",
        "source_title": "신라대학교 수학교육 임용시험 자료 PDF",
        "source_url": "https://mathedu1.silla.ac.kr/mathedu1/index.php?idx=496&mode=fdn&num=1&pCode=SUB3000004&pg=2",
        "source_class": "official_university_exam_material",
        "observed_terms": "중간체(intermediate field)|유한체|분해체|갈루아 군",
        "observation": "The university-hosted exam explicitly pairs 중간체 with intermediate field in a Galois-theory problem.",
        "accessed": "2026-07-18",
        "scope_limit": "Exam usage supports the headword 중간체 only; it does not certify the full U02 translation.",
        "provenance": "New Korean-local evidence for U02; inspected web PDF lines 404-417; page binary not copied into the lane.",
    },
    {
        "evidence_id": "KO-P29-U02-E008",
        "language": "ko",
        "standard": "ko-KR",
        "source_title": "조선대학교 기관저장소: 합성체를 이용한 유한체의 역원 계산 알고리즘 구현",
        "source_url": "https://oak.chosun.ac.kr/handle/2020.oak/14524",
        "source_class": "institutional_repository_thesis_metadata",
        "observed_terms": "합성체(Composite Fields)|유한체",
        "observation": "The repository records 합성체 in a finite-field hardware context, proving local form availability but not exact equivalence to Noether's Vereinigungskörper.",
        "accessed": "2026-07-18",
        "scope_limit": "Potential false friend: composite-field hardware construction is not by itself an attestation of the compositum of two fields.",
        "provenance": "New Korean-local adverse/supporting witness for U02; page binary not copied into the lane.",
    },
]


terms = [
    {
        "term_id": "KO-P29-U02-T001", "decision_id": "KO-P29-U02-D001", "german_source": "Endlichkeitskriterium",
        "korean_rendering": "유한성 판정기준", "hanja_record": "有限性 判定基準", "source_probe": "Endlichkeitskriterium", "target_probe": "유한성 판정기준",
        "sense_window": "Criterion whose finiteness conclusion is finite generation, not finite cardinality.", "excluded_senses": "A criterion that the ring or field has finitely many elements.",
        "evidence_ids": ["KO-P29-U02-E005"], "confidence": "medium", "decision_state": "accepted_with_sense_window", "ko_kr_state": "accepted_internal", "running_text_policy": "Hangul; proposition-level finite-generation sense remains explicit",
        "basin": "modern Sino-xenic coinage/calque", "dominance": "Qualitative debt: a cognate CJK label could attract wording, but no Mandarin evidence is admitted; Korean finite-generation evidence controls the sense.",
        "source_locator": "U02 source line 1", "target_locator": "Korean TeX line 12", "structural_id": "NOE-P29-KO-U02-SEC-001",
        "choice": "유한성 판정기준", "alternatives": ["유한 판정법", "유한성 기준"], "motivation": "Matches U01 title usage while the running theorem states the finite-generation content.",
    },
    {
        "term_id": "KO-P29-U02-T002", "decision_id": "KO-P29-U02-D002", "german_source": "Rationalbasis",
        "korean_rendering": "유리 기저", "hanja_record": "有理 基底", "source_probe": "Rationalbasis", "target_probe": "유리 기저",
        "sense_window": "Finite rational generating basis for a system of rational functions or an intermediate field.", "excluded_senses": "A vector-space basis over the rational numbers or a claim of linear independence.",
        "evidence_ids": [], "confidence": "low", "decision_state": "held_for_human_review", "ko_kr_state": "provisional_historical", "running_text_policy": "Hangul plus German source label on first occurrence",
        "basin": "mixed/contested", "dominance": "Qualitative high-attractor debt: cognate CJK calques are tempting, but Chinese/Japanese are excluded and no exact Korean historical witness was found.",
        "source_locator": "U02 source lines 3, 7, 13, 15", "target_locator": "Korean TeX lines 14, 18, 34, 40", "structural_id": "NOE-P29-KO-U02-THM-001",
        "choice": "유리 기저", "alternatives": ["유리함수 생성기저", "유리 생성계"], "motivation": "Keeps continuity with U01 while definition and source label prevent a false linear-basis reading.",
    },
    {
        "term_id": "KO-P29-U02-T003", "decision_id": "KO-P29-U02-D003", "german_source": "Jedes System S",
        "korean_rendering": "임의의 계 S", "hanja_record": "任意의 系", "source_probe": "Jedes System $S$", "target_probe": "임의의 계 $S$",
        "sense_window": "Universal quantification over each arbitrary system S of rational functions.", "excluded_senses": "A single totality called all systems, or an existentially selected system.",
        "evidence_ids": [], "confidence": "high", "decision_state": "accepted_internal", "ko_kr_state": "accepted_internal", "running_text_policy": "Hangul-first mathematical quantifier phrase",
        "basin": "modern Sino-xenic coinage/calque", "dominance": "No Mandarin evidence used; the German universal quantifier and Korean proposition structure determine the wording.",
        "source_locator": "U02 source line 3", "target_locator": "Korean TeX line 14", "structural_id": "NOE-P29-KO-U02-FORM-001",
        "choice": "임의의 계 S", "alternatives": ["유리함수의 모든 계 S"], "motivation": "Independent review found the explicit universal quantifier clearer and less structurally ambiguous.",
    },
    {
        "term_id": "KO-P29-U02-T004", "decision_id": "KO-P29-U02-D004", "german_source": "Körper",
        "korean_rendering": "체", "hanja_record": "體", "source_probe": "Körper $P$", "target_probe": "체 $P$",
        "sense_window": "Algebraic field used as coefficient field.", "excluded_senses": "Physical body, style, or generic set without field operations.",
        "evidence_ids": ["KO-P29-U02-E002", "KO-P29-U02-E003", "KO-P29-U02-E004"], "confidence": "high", "decision_state": "accepted_internal", "ko_kr_state": "accepted_internal", "running_text_policy": "Hangul only",
        "basin": "Sino-xenic inherited", "dominance": "Korean institutional and publisher evidence is independent; no Mandarin support enters the shelf.",
        "source_locator": "U02 source line 3", "target_locator": "Korean TeX line 14", "structural_id": "NOE-P29-KO-U02-FORM-001",
        "choice": "체", "alternatives": ["필드"], "motivation": "Established Korean algebra headword.",
    },
    {
        "term_id": "KO-P29-U02-T005", "decision_id": "KO-P29-U02-D005", "german_source": "Zwischenkörper",
        "korean_rendering": "중간체", "hanja_record": "中間體", "source_probe": "Zwischenkörper", "target_probe": "중간체",
        "sense_window": "Intermediate field lying between two specified fields.", "excluded_senses": "Chemical intermediate, intermediate object, or mere subset.",
        "evidence_ids": ["KO-P29-U02-E006", "KO-P29-U02-E007"], "confidence": "high", "decision_state": "accepted_internal", "ko_kr_state": "accepted_internal", "running_text_policy": "Hangul only",
        "basin": "modern Sino-xenic coinage/calque", "dominance": "Direct Korean publisher and university evidence is present; Chinese P29 remains excluded.",
        "source_locator": "U02 source lines 5, 7, 9, 11, 13", "target_locator": "Korean TeX lines 16, 18, 20, 22, 38", "structural_id": "NOE-P29-KO-U02-FORM-002",
        "choice": "중간체", "alternatives": ["중간 부분체"], "motivation": "Direct local evidence pairs 중간체 with intermediate field.",
    },
    {
        "term_id": "KO-P29-U02-T006", "decision_id": "KO-P29-U02-D006", "german_source": "Transzendenzgrad",
        "korean_rendering": "초월 차수", "hanja_record": "超越 次數", "source_probe": "Transzendenzgrad", "target_probe": "초월 차수",
        "sense_window": "Cardinality/number of an algebraically independent transcendence basis over the specified field.", "excluded_senses": "Polynomial degree, extension degree, or philosophical transcendence.",
        "evidence_ids": [], "confidence": "medium", "decision_state": "provisional_context_checked", "ko_kr_state": "provisional_compositional", "running_text_policy": "Hangul only; revisit exact spacing and specialist headword",
        "basin": "modern Sino-xenic coinage/calque", "dominance": "Qualitative debt: the compositional cognate is plausible but no exact independent Korean institutional witness was recovered; Mandarin evidence is not used.",
        "source_locator": "U02 source lines 5, 7, 9, 13", "target_locator": "Korean TeX lines 16, 18, 20, 34", "structural_id": "NOE-P29-KO-U02-FORM-002",
        "choice": "초월 차수", "alternatives": ["초월도"], "motivation": "Transparent modern Korean compositional term, held below external-certification level.",
    },
    {
        "term_id": "KO-P29-U02-T007", "decision_id": "KO-P29-U02-D007", "german_source": "irreduzibles System",
        "korean_rendering": "기약계", "hanja_record": "旣約系", "source_probe": "irreduzibles System", "target_probe": "기약계(irreduzibles System)",
        "sense_window": "Steinitz's historical system of algebraically independent functions, as defined in the source note.", "excluded_senses": "A system of irreducible polynomials, reduced fractions, or an irreducible representation.",
        "evidence_ids": [], "confidence": "low", "decision_state": "held_for_human_review", "ko_kr_state": "provisional_historical", "running_text_policy": "Hangul plus exact German label and source definition",
        "basin": "mixed/contested", "dominance": "Qualitative high-attractor debt: cognate characters suggest a false modern irreducibility sense; no neighboring CJK form authorizes Korean.",
        "source_locator": "U02 source line 5 and note", "target_locator": "Korean TeX line 16 and footnote", "structural_id": "NOE-P29-KO-U02-NOTE-001",
        "choice": "기약계", "alternatives": ["대수적 독립계", "비가약계"], "motivation": "Preserves the historical label while the footnote supplies the actual algebraic-independence sense.",
    },
    {
        "term_id": "KO-P29-U02-T008", "decision_id": "KO-P29-U02-D008", "german_source": "algebraisch unabhängig",
        "korean_rendering": "대수적으로 독립", "hanja_record": "代數的 獨立", "source_probe": "algebraisch unabhängigen", "target_probe": "대수적으로 독립",
        "sense_window": "No nonzero polynomial relation over the stated base field.", "excluded_senses": "Linear independence or probabilistic independence.",
        "evidence_ids": [], "confidence": "high", "decision_state": "accepted_contextual", "ko_kr_state": "accepted_internal", "running_text_policy": "Hangul only; always name the base field when needed",
        "basin": "modern Sino-xenic coinage/calque", "dominance": "No Mandarin evidence used; source definition and Korean algebraic syntax fix the sense, while exact corpus attestation remains a review debt.",
        "source_locator": "U02 source note and line 11", "target_locator": "Korean TeX footnote line 16 and line 22", "structural_id": "NOE-P29-KO-U02-STEP-002",
        "choice": "대수적으로 독립", "alternatives": ["대수 독립"], "motivation": "Makes the relation predicative and preserves the source's base-field dependence.",
    },
    {
        "term_id": "KO-P29-U02-T009", "decision_id": "KO-P29-U02-D009", "german_source": "algebraisch abhängig",
        "korean_rendering": "대수적으로 종속", "hanja_record": "代數的 從屬", "source_probe": "algebraisch abhängig", "target_probe": "대수적 종속성",
        "sense_window": "Existence of a polynomial relation over the named base field; individual elements are algebraic in the one-element case.", "excluded_senses": "Linear dependence, causal dependence, or containment alone.",
        "evidence_ids": [], "confidence": "high", "decision_state": "accepted_contextual", "ko_kr_state": "accepted_internal", "running_text_policy": "Hangul only; base field stated explicitly where the source inference requires it",
        "basin": "modern Sino-xenic coinage/calque", "dominance": "No Mandarin evidence used; the German proof and mathematical relation control the Korean syntax.",
        "source_locator": "U02 source lines 7, 11, 13, 15", "target_locator": "Korean TeX lines 18, 22, 38, 40", "structural_id": "NOE-P29-KO-U02-PARA-001",
        "choice": "대수적으로 종속 / 위에서 대수적", "alternatives": ["대수적으로 의존"], "motivation": "Uses standard relation wording and the single-element algebraic specialization accurately.",
    },
    {
        "term_id": "KO-P29-U02-T010", "decision_id": "KO-P29-U02-D010", "german_source": "endliche algebraische Erweiterung",
        "korean_rendering": "유한 대수적 확대", "hanja_record": "有限 代數的 擴大", "source_probe": "endliche algebraische Erweiterung", "target_probe": "유한 대수적 확대",
        "sense_window": "Algebraic field extension of finite degree generated by finitely many algebraic elements.", "excluded_senses": "A field with finitely many elements or merely a finitely generated transcendental extension.",
        "evidence_ids": ["KO-P29-U02-E003", "KO-P29-U02-E006"], "confidence": "high", "decision_state": "accepted_with_sense_window", "ko_kr_state": "accepted_internal", "running_text_policy": "Hangul only",
        "basin": "modern Sino-xenic coinage/calque", "dominance": "Korean publisher evidence supports 확대체 and finite extension compounds; Mandarin evidence is excluded.",
        "source_locator": "U02 source lines 5, 7, 9, 15", "target_locator": "Korean TeX lines 16, 18, 20, 40", "structural_id": "NOE-P29-KO-U02-FORM-002",
        "choice": "유한 대수적 확대", "alternatives": ["유한 대수 확대", "유한차수 대수확대체"], "motivation": "Preserves the predicative field-extension relation used throughout the proof.",
    },
    {
        "term_id": "KO-P29-U02-T011", "decision_id": "KO-P29-U02-D011", "german_source": "rein transzendente Erweiterung",
        "korean_rendering": "순수 초월 확대", "hanja_record": "純粹 超越 擴大", "source_probe": "rein transzendente Erweiterung", "target_probe": "순수 초월 확대",
        "sense_window": "Field extension generated by an algebraically independent set, with no algebraic generators added.", "excluded_senses": "Purely algebraic extension or philosophical/spiritual transcendence.",
        "evidence_ids": [], "confidence": "medium", "decision_state": "provisional_context_checked", "ko_kr_state": "provisional_compositional", "running_text_policy": "Hangul only",
        "basin": "modern Sino-xenic coinage/calque", "dominance": "Qualitative debt: exact Korean institutional attestation was not recovered; CJK cognates are not evidence.",
        "source_locator": "U02 source line 11", "target_locator": "Korean TeX line 28", "structural_id": "NOE-P29-KO-U02-STEP-002",
        "choice": "순수 초월 확대", "alternatives": ["순수초월확대체"], "motivation": "Compositional modern field-theory rendering, held for specialist review.",
    },
    {
        "term_id": "KO-P29-U02-T012", "decision_id": "KO-P29-U02-D012", "german_source": "Koeffizientenbereich",
        "korean_rendering": "계수 영역", "hanja_record": "係數 領域", "source_probe": "Koeffizientenbereich", "target_probe": "계수 영역",
        "sense_window": "The field or domain chosen as coefficient base in the argument.", "excluded_senses": "A geometric coordinate region or an assertion that the base is an integral domain in a stronger sense.",
        "evidence_ids": ["KO-P29-U02-E001", "KO-P29-U02-E006"], "confidence": "medium", "decision_state": "provisional_context_checked", "ko_kr_state": "provisional_compositional", "running_text_policy": "Hangul only",
        "basin": "mixed/contested", "dominance": "Korean evidence supports 계수, but the exact compound remains editorial; no Mandarin evidence is used.",
        "source_locator": "U02 source line 13", "target_locator": "Korean TeX lines 30, 34", "structural_id": "NOE-P29-KO-U02-STEP-003",
        "choice": "계수 영역", "alternatives": ["계수체", "계수역"], "motivation": "Matches U01 wording without silently strengthening Bereich to a particular modern category.",
    },
    {
        "term_id": "KO-P29-U02-T013", "decision_id": "KO-P29-U02-D013", "german_source": "Vereinigungskörper",
        "korean_rendering": "합성체", "hanja_record": "合成體", "source_probe": "Vereinigungskörper", "target_probe": "합성체(Vereinigungskörper)",
        "sense_window": "Compositum: the smallest field containing both specified fields inside a common overfield.", "excluded_senses": "Composite finite-field hardware representation, chemical composite, or arbitrary union of sets.",
        "evidence_ids": ["KO-P29-U02-E008"], "confidence": "low", "decision_state": "held_for_human_review", "ko_kr_state": "provisional_historical", "running_text_policy": "Hangul plus German source label on first occurrence",
        "basin": "mixed/contested", "dominance": "Qualitative debt: local 합성체 evidence is a nearby hardware sense, not exact compositum evidence; Chinese/Japanese cognates remain excluded.",
        "source_locator": "U02 source line 13", "target_locator": "Korean TeX line 34", "structural_id": "NOE-P29-KO-U02-STEP-003",
        "choice": "합성체", "alternatives": ["합동체", "포합체"], "motivation": "Working modern form with source label and an explicit adverse-evidence boundary.",
    },
    {
        "term_id": "KO-P29-U02-T014", "decision_id": "KO-P29-U02-D014", "german_source": "Unterkörper",
        "korean_rendering": "부분체", "hanja_record": "部分體", "source_probe": "Unterkörper", "target_probe": "부분체",
        "sense_window": "Subfield contained in a field and closed under field operations.", "excluded_senses": "Arbitrary subset or proper class.",
        "evidence_ids": ["KO-P29-U02-E006", "KO-P29-U02-E007"], "confidence": "high", "decision_state": "accepted_internal", "ko_kr_state": "accepted_internal", "running_text_policy": "Hangul only",
        "basin": "modern Sino-xenic coinage/calque", "dominance": "Korean Galois-theory evidence supports the local field hierarchy; no Mandarin support is used.",
        "source_locator": "U02 source line 13 footnote", "target_locator": "Korean TeX line 30 footnote", "structural_id": "NOE-P29-KO-U02-NOTE-002",
        "choice": "부분체", "alternatives": ["부분 필드"], "motivation": "Established Korean algebraic containment term.",
    },
    {
        "term_id": "KO-P29-U02-T015", "decision_id": "KO-P29-U02-D015", "german_source": "Folgerung",
        "korean_rendering": "따름정리", "hanja_record": "따름定理 (따름은 고유어)", "source_probe": "Folgerung", "target_probe": "따름정리",
        "sense_window": "A corollary deduced immediately from the preceding theorem.", "excluded_senses": "An informal consequence without theorem status or a later independent proposition.",
        "evidence_ids": ["KO-P29-U02-E006"], "confidence": "high", "decision_state": "accepted_internal", "ko_kr_state": "accepted_internal", "running_text_policy": "Hangul-first theorem label",
        "basin": "mixed/contested", "dominance": "Direct Korean publisher evidence uses 따름정리; no Mandarin evidence enters the choice.",
        "source_locator": "U02 source line 15", "target_locator": "Korean TeX line 40", "structural_id": "NOE-P29-KO-U02-COR-001",
        "choice": "따름정리", "alternatives": ["계", "추론"], "motivation": "Locally evidenced Korean theorem-structure label.",
    },
    {
        "term_id": "KO-P29-U02-T016", "decision_id": "KO-P29-U02-D016", "german_source": "transitives Gesetz der algebraischen Abhängigkeit",
        "korean_rendering": "대수적 종속성의 추이법칙", "hanja_record": "代數的 從屬性 推移法則", "source_probe": "transitiven Gesetz der algebraischen Abhängigkeit", "target_probe": "대수적 종속성의 추이법칙",
        "sense_window": "Transitivity principle used with the explicit premise that K is algebraic over the smaller base.", "excluded_senses": "Transitivity of ordinary set inclusion alone or linear dependence.",
        "evidence_ids": [], "confidence": "medium", "decision_state": "provisional_context_checked", "ko_kr_state": "provisional_compositional", "running_text_policy": "Hangul only; retain the explicit algebraicity premise in prose",
        "basin": "modern Sino-xenic coinage/calque", "dominance": "No Mandarin evidence used; the German proof and explicit premise constrain the Korean relation.",
        "source_locator": "U02 source line 11", "target_locator": "Korean TeX line 22", "structural_id": "NOE-P29-KO-U02-STEP-002",
        "choice": "대수적 종속성의 추이법칙", "alternatives": ["대수적 의존의 추이성"], "motivation": "Preserves the named inferential role and prevents the proof premise from remaining implicit.",
    },
]


adverse_rows = [
    {"adverse_id": "KO-P29-U02-A001", "term_ids": "KO-P29-U02-T001|KO-P29-U02-T010", "locator": "source lines 1, 5-15", "symptom_or_risk": "endlich can be misread as finite cardinality", "evidence_or_search_result": "The theorem and proof concern finite generation or finite extension; SNU uses 유한생성 대수.", "editorial_disposition": "Retain conventional 유한성 label but make finite-generation/finite-extension predicates explicit.", "residual_risk": "The heading alone may still attract cardinality.", "revisit_condition": "Korean algebra specialist review or later same-work contradiction."},
    {"adverse_id": "KO-P29-U02-A002", "term_ids": "KO-P29-U02-T002", "locator": "source lines 3, 7, 13, 15", "symptom_or_risk": "기저 may falsely assert linear independence", "evidence_or_search_result": "The source definition only requires rational generation by finitely many functions.", "editorial_disposition": "Keep German Rationalbasis at first occurrence and the defining sentence; hold the Korean compound.", "residual_risk": "Readers may import a modern vector-basis sense.", "revisit_condition": "Independent Korean historical invariant/field-theory source."},
    {"adverse_id": "KO-P29-U02-A003", "term_ids": "KO-P29-U02-T007", "locator": "source line 5 note", "symptom_or_risk": "irreduzibles System can be mistaken for irreducible polynomials", "evidence_or_search_result": "The source footnote defines it as a system of algebraically independent functions.", "editorial_disposition": "Retain German label and reproduce the definition; do not normalize silently.", "residual_risk": "기약계 remains historically nontransparent.", "revisit_condition": "Korean Steinitz-era terminology source or specialist review."},
    {"adverse_id": "KO-P29-U02-A004", "term_ids": "KO-P29-U02-T006|KO-P29-U02-T008|KO-P29-U02-T009|KO-P29-U02-T011|KO-P29-U02-T016", "locator": "source lines 5-13", "symptom_or_risk": "Exact Korean transcendence/dependence compounds lack independent local attestation", "evidence_or_search_result": "Bounded Korean institutional/publisher shelf confirmed adjacent field vocabulary but not all exact compounds.", "editorial_disposition": "Use context-controlled compositional forms and keep review debt explicit.", "residual_risk": "Spacing or preferred specialist headwords may differ.", "revisit_condition": "Qualified Korean field-theory review or direct local source."},
    {"adverse_id": "KO-P29-U02-A005", "term_ids": "KO-P29-U02-T012", "locator": "source line 13", "symptom_or_risk": "Bereich may attract an over-specific modern algebraic category", "evidence_or_search_result": "The proof uses P-bar as the coefficient base; the source does not need a stronger standalone category claim.", "editorial_disposition": "Use 계수 영역 and keep alternatives open.", "residual_risk": "계수체 may be preferred by a modern reviewer.", "revisit_condition": "Later Paper 29 consistency audit or Korean specialist review."},
    {"adverse_id": "KO-P29-U02-A006", "term_ids": "KO-P29-U02-T013", "locator": "source line 13", "symptom_or_risk": "합성체 has a nearby composite-field hardware sense", "evidence_or_search_result": "Chosun repository E008 uses 합성체(Composite Fields) in finite-field hardware, not an exact compositum definition.", "editorial_disposition": "Keep Vereinigungskörper label and treat E008 as adverse/weak evidence only.", "residual_risk": "The selected Korean form may not be the historical specialist preference.", "revisit_condition": "Direct Korean field-compositum source or human review."},
    {"adverse_id": "KO-P29-U02-A007", "term_ids": "ALL", "locator": "U02 Korean standard boundary", "symptom_or_risk": "DPRK/North-Korean terminology is absent", "evidence_or_search_result": "No ko-KP corpus or reviewer was recovered or consulted.", "editorial_disposition": "Declare ko-KR only and keep every ko-KP state unverified_do_not_claim.", "residual_risk": "South-Korean choices may not transfer.", "revisit_condition": "Documented DPRK source and qualified reviewer."},
    {"adverse_id": "KO-P29-U02-A008", "term_ids": "ALL", "locator": "CJK comparison boundary", "symptom_or_risk": "Mandarin-Simplified dominance could bias the evidence shelf", "evidence_or_search_result": "A Chinese P29 tranche exists but was not used as Korean lexical evidence.", "editorial_disposition": "Record qualitative debt in CSV controls; never use it as a readiness scalar or Korean authorization.", "residual_risk": "Future workers may copy convenient cognate compounds.", "revisit_condition": "Reaudit before every terminology promotion."},
    {"adverse_id": "KO-P29-U02-A009", "term_ids": "KO-P29-U02-T005|KO-P29-U02-T014", "locator": "target displays lines 23-37", "symptom_or_risk": "Plain-text extraction drops overbars", "evidence_or_search_result": "PDF extraction shows unbarred symbols where the rendered PDF visibly distinguishes barred fields.", "editorial_disposition": "Treat render inspection as mandatory notation evidence and do not infer equality from extraction.", "residual_risk": "Automated term/parity consumers may collapse barred and unbarred objects.", "revisit_condition": "Every later field-theory unit and any extractor change."},
    {"adverse_id": "KO-P29-U02-A010", "term_ids": "KO-P29-U02-T003", "locator": "first formulation source line 3", "symptom_or_risk": "A Korean phrase can obscure the universal quantifier", "evidence_or_search_result": "Independent internal review preferred 임의의 계 S over 유리함수의 모든 계 S.", "editorial_disposition": "Use the explicit arbitrary-system quantifier and preserve the prior hash in difficulty/visual evidence.", "residual_risk": "Later stylistic edits may weaken the quantifier again.", "revisit_condition": "Any edit to the first theorem formulation."},
]


def main() -> int:
    errors: list[str] = []
    source_text = SOURCE.read_text(encoding="utf-8")
    target_text = TARGET.read_text(encoding="utf-8")
    if sha256(SOURCE) != SOURCE_SHA:
        errors.append("source hash mismatch")
    if sha256(TARGET) != TARGET_SHA:
        errors.append("target hash mismatch")
    if sha256(STRUCTURE) != STRUCTURE_SHA:
        errors.append("structural index hash mismatch")

    evidence_ids = {row["evidence_id"] for row in evidence_rows}
    term_ids = {term["term_id"] for term in terms}
    decision_ids = {term["decision_id"] for term in terms}
    if len(term_ids) != len(terms) or len(decision_ids) != len(terms):
        errors.append("duplicate term or decision ID")

    for term in terms:
        if term["source_probe"] not in source_text:
            errors.append(f"source probe absent: {term['term_id']}: {term['source_probe']}")
        if term["target_probe"] not in target_text:
            errors.append(f"target probe absent: {term['term_id']}: {term['target_probe']}")
        missing = sorted(set(term["evidence_ids"]) - evidence_ids)
        if missing:
            errors.append(f"missing evidence IDs for {term['term_id']}: {missing}")
        if not term["sense_window"] or not term["excluded_senses"]:
            errors.append(f"missing sense control: {term['term_id']}")
        if term["basin"] not in ALLOWED_BASINS:
            errors.append(f"invalid attractor basin: {term['term_id']}: {term['basin']}")
        if not term["dominance"] or term["dominance"].strip().replace(".", "", 1).isdigit():
            errors.append(f"dominance debt is absent or scalar: {term['term_id']}")

    evidence_path = EVIDENCE / "KOREAN_NATIVE_EXAMPLE_CORPUS_U02.csv"
    write_csv(evidence_path, evidence_rows, list(evidence_rows[0]))

    ledger_rows = []
    for term in terms:
        ledger_rows.append({
            "term_id": term["term_id"],
            "german_source": term["german_source"],
            "korean_rendering": term["korean_rendering"],
            "hanja_record": term["hanja_record"],
            "running_text_policy": term["running_text_policy"],
            "ko_kr_state": term["ko_kr_state"],
            "ko_kp_state": "unverified_do_not_claim",
            "sense_window": term["sense_window"],
            "excluded_senses": term["excluded_senses"],
            "evidence_ids": "|".join(term["evidence_ids"]),
            "confidence": term["confidence"],
            "decision_state": term["decision_state"],
            "lexical_attractor_basin": term["basin"],
            "mandarin_simplified_dominance_risk_debt": term["dominance"],
        })
    ledger_path = EVIDENCE / "TERMINOLOGY_LEDGER_U02.csv"
    write_csv(ledger_path, ledger_rows, list(ledger_rows[0]))

    adverse_path = EVIDENCE / "ADVERSE_EVIDENCE_LEDGER_U02.csv"
    write_csv(adverse_path, adverse_rows, list(adverse_rows[0]))

    crosswalk_rows = []
    for index, term in enumerate(terms, 1):
        crosswalk_rows.append({
            "crosswalk_id": f"KO-P29-U02-X{index:03d}",
            "term_id": term["term_id"],
            "german_term": term["german_source"],
            "korean_form": term["korean_rendering"],
            "sense_window": term["sense_window"],
            "excluded_senses": term["excluded_senses"],
            "ko_kr_state": term["ko_kr_state"],
            "ko_kp_state": "unverified_do_not_claim",
            "lexical_attractor_basin": term["basin"],
            "mandarin_simplified_dominance_risk_debt": term["dominance"],
            "evidence_ids": "|".join(term["evidence_ids"]),
            "decision_state": term["decision_state"],
        })
    crosswalk_path = EVIDENCE / "CJKV_CROSSWALK_P29_KO_U02.csv"
    write_csv(crosswalk_path, crosswalk_rows, list(crosswalk_rows[0]))

    decision_schema = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": "urn:interlanguage:noether:p29:ko:u02:terminology-decisions:1.0.0",
        "type": "object",
        "additionalProperties": False,
        "required": ["schema_version", "work_unit", "authority", "review_boundary", "evidence_catalog", "decisions"],
        "properties": {
            "schema_version": {"const": "1.0.0"},
            "work_unit": {"const": "P29-KO-U02"},
            "authority": {
                "type": "object", "additionalProperties": False,
                "required": ["sealed_sha256", "source_sha256", "target_sha256", "source_cursor", "next_cursor"],
                "properties": {
                    "sealed_sha256": {"pattern": "^[A-F0-9]{64}$"}, "source_sha256": {"pattern": "^[A-F0-9]{64}$"},
                    "target_sha256": {"pattern": "^[A-F0-9]{64}$"}, "source_cursor": {"type": "string", "minLength": 1},
                    "next_cursor": {"type": "string", "minLength": 1},
                },
            },
            "review_boundary": {
                "type": "object", "additionalProperties": False,
                "required": ["internal", "external_human", "dprk"],
                "properties": {"internal": {"type": "string"}, "external_human": {"const": "absent_do_not_claim"}, "dprk": {"const": "unverified_do_not_claim"}},
            },
            "evidence_catalog": {"type": "array", "items": {"type": "object", "required": ["evidence_id", "language", "source_title", "source_url", "scope_limit"], "additionalProperties": True}},
            "decisions": {
                "type": "array", "minItems": 1,
                "items": {
                    "type": "object", "additionalProperties": False,
                    "required": ["decision_id", "term_id", "source_form", "target_form", "hanja_record", "source_probe", "target_probe", "sense_window", "excluded_senses", "choice", "alternatives", "evidence_ids", "confidence", "decision_state", "ko_kr_state", "ko_kp_state", "source_locator", "target_locator", "structural_id", "motivation", "claim_type", "uncertainty", "revisit_condition"],
                    "properties": {
                        "decision_id": {"pattern": "^KO-P29-U02-D[0-9]{3}$"}, "term_id": {"pattern": "^KO-P29-U02-T[0-9]{3}$"},
                        "source_form": {"type": "string", "minLength": 1}, "target_form": {"type": "string", "minLength": 1},
                        "hanja_record": {"type": "string", "minLength": 1}, "source_probe": {"type": "string", "minLength": 1},
                        "target_probe": {"type": "string", "minLength": 1}, "sense_window": {"type": "string", "minLength": 1},
                        "excluded_senses": {"type": "string", "minLength": 1}, "choice": {"type": "string", "minLength": 1},
                        "alternatives": {"type": "array", "items": {"type": "string"}}, "evidence_ids": {"type": "array", "items": {"pattern": "^KO-P29-U02-E[0-9]{3}$"}},
                        "confidence": {"enum": ["high", "medium", "low"]},
                        "decision_state": {"enum": ["accepted_internal", "accepted_contextual", "accepted_with_sense_window", "provisional_context_checked", "held_for_human_review"]},
                        "ko_kr_state": {"type": "string", "minLength": 1}, "ko_kp_state": {"const": "unverified_do_not_claim"},
                        "source_locator": {"type": "string", "minLength": 1}, "target_locator": {"type": "string", "minLength": 1},
                        "structural_id": {"pattern": "^NOE-P29-KO-U02-"}, "motivation": {"type": "string", "minLength": 1},
                        "claim_type": {"enum": ["editorial_inference", "model_preference"]}, "uncertainty": {"type": "string", "minLength": 1},
                        "revisit_condition": {"type": "string", "minLength": 1},
                    },
                },
            },
        },
    }
    decision_schema_path = EVIDENCE / "TERMINOLOGY_DECISIONS_U02.schema.json"
    decision_schema_path.write_text(json.dumps(decision_schema, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")

    decision_records = []
    for term in terms:
        decision_records.append({
            "decision_id": term["decision_id"], "term_id": term["term_id"], "source_form": term["german_source"],
            "target_form": term["korean_rendering"], "hanja_record": term["hanja_record"], "source_probe": term["source_probe"],
            "target_probe": term["target_probe"], "sense_window": term["sense_window"], "excluded_senses": term["excluded_senses"],
            "choice": term["choice"], "alternatives": term["alternatives"], "evidence_ids": term["evidence_ids"],
            "confidence": term["confidence"], "decision_state": term["decision_state"], "ko_kr_state": term["ko_kr_state"],
            "ko_kp_state": "unverified_do_not_claim", "source_locator": term["source_locator"], "target_locator": term["target_locator"],
            "structural_id": term["structural_id"], "motivation": term["motivation"], "claim_type": "editorial_inference",
            "uncertainty": "Internal working decision; exact historical Korean attestation or external human review remains absent where the ledger says provisional or held.",
            "revisit_condition": "Append a superseding decision on independent Korean specialist evidence, DPRK evidence, or a sealed-source/reviewer finding; never overwrite this record.",
        })
    decisions = {
        "schema_version": "1.0.0", "work_unit": "P29-KO-U02",
        "authority": {"sealed_sha256": "A48CB5CD1716974B686AC1CBA681CA4B17BC72F9043B78AD2528ACA41FCF814F", "source_sha256": SOURCE_SHA, "target_sha256": TARGET_SHA, "source_cursor": "full-P29 lines 25-39", "next_cursor": "full-P29 line 41; line 40 blank"},
        "review_boundary": {"internal": "source_checked_build_render_and_independent_model_fidelity_review", "external_human": "absent_do_not_claim", "dprk": "unverified_do_not_claim"},
        "evidence_catalog": evidence_rows, "decisions": decision_records,
    }
    decisions_path = EVIDENCE / "TERMINOLOGY_DECISIONS_U02.json"
    decisions_path.write_text(json.dumps(decisions, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    try:
        jsonschema.Draft202012Validator(decision_schema).validate(decisions)
    except jsonschema.ValidationError as exc:
        errors.append(f"terminology JSON schema error: {exc.message}")

    structures = [json.loads(line) for line in STRUCTURE.read_text(encoding="utf-8").splitlines() if line.strip()]
    structural_ids = {record["structural_id"] for record in structures}
    for term in terms:
        if term["structural_id"] not in structural_ids:
            errors.append(f"missing structural anchor: {term['term_id']}: {term['structural_id']}")

    nodes = [
        {"id": "SRC-P29-U02", "type": "source_unit", "label": "Pinned German P29 U02", "value": SOURCE_SHA, "claim_class": "source_fact"},
        {"id": "TGT-P29-U02", "type": "target_unit", "label": "Final Korean P29 U02", "value": TARGET_SHA, "claim_class": "computation"},
    ]
    for row in evidence_rows:
        nodes.append({"id": row["evidence_id"], "type": "korean_external_evidence", "label": row["source_title"], "value": row["observed_terms"], "claim_class": "external_source_evidence"})
    for row in adverse_rows:
        nodes.append({"id": row["adverse_id"], "type": "adverse_evidence", "label": row["symptom_or_risk"], "value": row["residual_risk"], "claim_class": "editorial_inference"})
    for record in structures:
        nodes.append({"id": record["structural_id"], "type": "structural_unit", "label": record["unit_type"], "value": record["target"]["fragment_sha256"], "claim_class": "computation"})
    for term in terms:
        nodes.append({"id": f"CON-{term['term_id']}", "type": "concept", "label": term["german_source"], "value": term["sense_window"], "claim_class": "source_fact"})
        nodes.append({"id": term["decision_id"], "type": "terminology_decision", "label": f"{term['german_source']} → {term['korean_rendering']}", "value": term["decision_state"], "claim_class": "editorial_inference"})

    edges = []
    edge_index = 1
    def add_edge(source: str, target: str, predicate: str, evidence_class: str) -> None:
        nonlocal edge_index
        edges.append({"id": f"EDGE-P29-U02-{edge_index:03d}", "source": source, "target": target, "predicate": predicate, "evidence_class": evidence_class})
        edge_index += 1

    adverse_by_term: dict[str, list[str]] = defaultdict(list)
    for row in adverse_rows:
        affected = term_ids if row["term_ids"] == "ALL" else set(row["term_ids"].split("|"))
        for term_id in affected:
            adverse_by_term[term_id].append(row["adverse_id"])
    for term in terms:
        concept = f"CON-{term['term_id']}"
        add_edge("SRC-P29-U02", concept, "contains_concept", "source_fact")
        add_edge(concept, term["decision_id"], "interpreted_as", "editorial_inference")
        add_edge(term["decision_id"], "TGT-P29-U02", "realized_in", "computation")
        add_edge(term["decision_id"], term["structural_id"], "anchored_in", "computation")
        for evidence_id in term["evidence_ids"]:
            add_edge(evidence_id, term["decision_id"], "supports_or_bounds", "external_source_evidence")
        for adverse_id in sorted(adverse_by_term[term["term_id"]]):
            add_edge(adverse_id, term["decision_id"], "qualifies", "editorial_inference")

    graph_schema = {
        "$schema": "https://json-schema.org/draft/2020-12/schema", "$id": "urn:interlanguage:noether:p29:ko:u02:typed-graph:1.0.0",
        "type": "object", "additionalProperties": False, "required": ["schema_version", "work_unit", "dag", "nodes", "edges", "human_validation"],
        "properties": {
            "schema_version": {"const": "1.0.0"}, "work_unit": {"const": "P29-KO-U02"}, "dag": {"const": True},
            "human_validation": {"const": "absent_do_not_claim"},
            "nodes": {"type": "array", "items": {"type": "object", "additionalProperties": False, "required": ["id", "type", "label", "value", "claim_class"], "properties": {
                "id": {"type": "string", "minLength": 1}, "type": {"enum": ["source_unit", "target_unit", "korean_external_evidence", "adverse_evidence", "structural_unit", "concept", "terminology_decision"]},
                "label": {"type": "string"}, "value": {"type": "string"}, "claim_class": {"enum": ["source_fact", "computation", "editorial_inference", "external_source_evidence"]},
            }}},
            "edges": {"type": "array", "items": {"type": "object", "additionalProperties": False, "required": ["id", "source", "target", "predicate", "evidence_class"], "properties": {
                "id": {"pattern": "^EDGE-P29-U02-[0-9]{3}$"}, "source": {"type": "string"}, "target": {"type": "string"},
                "predicate": {"enum": ["contains_concept", "interpreted_as", "realized_in", "anchored_in", "supports_or_bounds", "qualifies"]},
                "evidence_class": {"enum": ["source_fact", "computation", "editorial_inference", "external_source_evidence"]},
            }}},
        },
    }
    graph_schema_path = EVIDENCE / "TYPED_CONCEPT_EVIDENCE_GRAPH_U02.schema.json"
    graph_schema_path.write_text(json.dumps(graph_schema, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    graph = {"schema_version": "1.0.0", "work_unit": "P29-KO-U02", "dag": True, "nodes": nodes, "edges": edges, "human_validation": "absent_do_not_claim"}
    graph_path = EVIDENCE / "TYPED_CONCEPT_EVIDENCE_GRAPH_U02.json"
    graph_path.write_text(json.dumps(graph, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    try:
        jsonschema.Draft202012Validator(graph_schema).validate(graph)
    except jsonschema.ValidationError as exc:
        errors.append(f"graph JSON schema error: {exc.message}")

    node_ids = [node["id"] for node in nodes]
    if len(node_ids) != len(set(node_ids)):
        errors.append("duplicate graph node ID")
    node_set = set(node_ids)
    for edge in edges:
        if edge["source"] not in node_set or edge["target"] not in node_set:
            errors.append(f"unresolved graph edge: {edge['id']}")
    adjacency: dict[str, list[str]] = defaultdict(list)
    indegree = {node_id: 0 for node_id in node_set}
    for edge in edges:
        adjacency[edge["source"]].append(edge["target"])
        indegree[edge["target"]] += 1
    queue = deque(sorted(node for node, degree in indegree.items() if degree == 0))
    visited = 0
    while queue:
        current = queue.popleft(); visited += 1
        for target in adjacency[current]:
            indegree[target] -= 1
            if indegree[target] == 0:
                queue.append(target)
    if visited != len(node_set):
        errors.append("typed evidence graph contains a cycle")

    forbidden_json_fields = {"lexical_attractor_basin", "mandarin_simplified_dominance_risk_debt"}
    def find_forbidden(value) -> list[str]:
        hits: list[str] = []
        if isinstance(value, dict):
            for key, nested in value.items():
                if key in forbidden_json_fields:
                    hits.append(key)
                hits.extend(find_forbidden(nested))
        elif isinstance(value, list):
            for nested in value:
                hits.extend(find_forbidden(nested))
        return hits
    if find_forbidden(decisions) or find_forbidden(graph):
        errors.append("crosswalk-only attractor/dominance fields leaked into typed JSON")

    parity_rows = []
    for record in structures:
        parity_rows.append({
            "parity_id": f"PAR-{record['structural_id']}", "structural_id": record["structural_id"], "unit_type": record["unit_type"],
            "parent_id": record["parent_id"] or "", "order_index": record["order_index"],
            "source_path": record["source"]["artifact_path"], "source_sha256": record["source"]["artifact_sha256"],
            "source_line_start": record["source"]["locator"]["line_start"] or "", "source_line_end": record["source"]["locator"]["line_end"] or "",
            "source_fragment_sha256": record["source"]["fragment_sha256"], "target_path": record["target"]["artifact_path"],
            "target_sha256": record["target"]["artifact_sha256"], "target_line_start": record["target"]["locator"]["line_start"] or "",
            "target_line_end": record["target"]["locator"]["line_end"] or "", "target_fragment_sha256": record["target"]["fragment_sha256"],
            "completion_state": record["completion_state"], "review_state": record["review_state"], "publication_state": record["publication_state"],
            "continuation_cursor": record["continuation_cursor"],
        })
    parity_path = QA / "SOURCE_TARGET_PARITY_U02.csv"
    write_csv(parity_path, parity_rows, list(parity_rows[0]))
    if len(parity_rows) != 16 or {row["structural_id"] for row in parity_rows} != structural_ids:
        errors.append("source-target parity does not cover all 16 structural IDs")

    output_paths = [evidence_path, ledger_path, adverse_path, crosswalk_path, decision_schema_path, decisions_path, graph_schema_path, graph_path, parity_path]
    output_hashes = {path.relative_to(ROOT).as_posix(): {"bytes": path.stat().st_size, "sha256": sha256(path)} for path in output_paths}
    report = {
        "work_unit": "P29-KO-U02", "authority_sha256": "A48CB5CD1716974B686AC1CBA681CA4B17BC72F9043B78AD2528ACA41FCF814F",
        "source_sha256": SOURCE_SHA, "target_sha256": TARGET_SHA, "structural_index_sha256": STRUCTURE_SHA,
        "counts": {"evidence_records": len(evidence_rows), "term_decisions": len(terms), "adverse_records": len(adverse_rows), "crosswalk_rows": len(crosswalk_rows), "graph_nodes": len(nodes), "graph_edges": len(edges), "parity_rows": len(parity_rows)},
        "latest_ids": {"evidence": evidence_rows[-1]["evidence_id"], "term": terms[-1]["term_id"], "decision": terms[-1]["decision_id"], "adverse": adverse_rows[-1]["adverse_id"], "crosswalk": crosswalk_rows[-1]["crosswalk_id"]},
        "crosswalk_controls": {"allowed_lexical_attractor_basins": sorted(ALLOWED_BASINS), "mandarin_simplified_dominance_debt": "qualitative_only_never_readiness_scalar", "typed_json_field_separation": "pass" if not find_forbidden(decisions) and not find_forbidden(graph) else "fail"},
        "review_boundary": {"internal_source_term_graph_parity": "pass" if not errors else "fail", "external_human_korean_domain": "absent_do_not_claim", "dprk": "unverified_do_not_claim", "cjk_cross_authorization": "prohibited_and_not_used"},
        "outputs": output_hashes, "errors": errors,
    }
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({"counts": report["counts"], "errors": errors}, ensure_ascii=False))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
