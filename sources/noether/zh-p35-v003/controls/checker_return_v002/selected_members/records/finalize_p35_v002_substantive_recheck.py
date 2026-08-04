#!/usr/bin/env python3
"""Freeze the substantive P35 v002 source/target and finding-disposition replay."""

from __future__ import annotations

from collections import Counter
from datetime import datetime
from hashlib import sha256
import json
from pathlib import Path


SCRIPT = Path(__file__).resolve()
RECHECK = SCRIPT.parents[1]
CHECKER_ROOT = SCRIPT.parents[3]
PAPER = CHECKER_ROOT / "paper35"
PACKAGE = RECHECK / "intake/frozen_producer_package_v002"
OUT = RECHECK / "evidence/P35_V002_SUBSTANTIVE_RECHECK_RECORD.json"
DISPOSITIONS = RECHECK / "findings/P35_V002_FINDING_DISPOSITION.jsonl"

SOURCE = PACKAGE / "source/current/Noether_P35_crosshead_LF.tex"
PRODUCER_HANS = PACKAGE / "build/zh-Hans-CN-v002/Noether_Paper35_Chinese_CurrentAuthority_zh-Hans-CN_v002.tex"
PRODUCER_HANT = PACKAGE / "build/zh-Hant-controlled-v002/Noether_Paper35_Chinese_CurrentAuthority_zh-Hant-controlled_v002.tex"
CHECKER_HANS = PAPER / "candidate/zh-Hans-CN/Noether_Paper35_Chinese_CurrentAuthority_zh-Hans-CN_checker_candidate_v001.tex"
CHECKER_HANT_V002 = PAPER / "candidate/zh-Hant-controlled/Noether_Paper35_Chinese_CurrentAuthority_zh-Hant-controlled_checker_candidate_v002.tex"
CHECKER_HANT_V003 = RECHECK / "candidate/zh-Hant-controlled/Noether_Paper35_Chinese_CurrentAuthority_zh-Hant-controlled_checker_candidate_v003.tex"
MATH_INDEX = RECHECK / "structural/P35_MATH_LOCUS_INDEX.json"
TEX_SUMMARY = RECHECK / "structural/P35_TEX_AUDIT_SUMMARY.json"
UNIT_INDEX = PAPER / "structural/P35_STRUCTURAL_UNIT_INDEX.json"
TERM_EVIDENCE = PAPER / "evidence/P35_LOCAL_CHINESE_TERMINOLOGY_EVIDENCE.json"
HANT_AUDIT = RECHECK / "evidence/P35_HANT_INDEPENDENT_AUDIT_v002.json"
HANT_CANDIDATE_RECORD = RECHECK / "evidence/P35_HANT_CHECKER_CANDIDATE_BUILD_RECORD_v003.json"
PDF_VERIFIER = RECHECK / "build/P35_V002_PDF_TEXT_METADATA_VERIFICATION.json"
BUILD_RECORD = RECHECK / "build/P35_V002_CHECKER_BUILD_RECORD.json"
RENDER_RECORD = RECHECK / "render/P35_V002_RENDER_RECORD.json"
VISUAL_LEDGER = RECHECK / "render/P35_V002_VISUAL_QA_LEDGER.jsonl"


def digest(data: bytes) -> str:
    return sha256(data).hexdigest().upper()


def fact(path: Path) -> dict[str, object]:
    data = path.read_bytes()
    return {"path": str(path), "bytes": len(data), "sha256": digest(data)}


def body(path: Path) -> bytes:
    data = path.read_bytes()
    marker = b"\\section*{35."
    close = b"\\clearpage\n\n"
    start = data.index(marker)
    end = data.rindex(close) + len(close)
    return data[start:end]


def occurrences(text: str, term: str) -> dict[str, object]:
    lines = [index for index, line in enumerate(text.splitlines(), start=1) if term in line]
    return {"term": term, "count": text.count(term), "lines": lines}


def main() -> int:
    recorded_at = datetime.now().astimezone().isoformat()
    source = SOURCE.read_text(encoding="utf-8")
    hans = PRODUCER_HANS.read_text(encoding="utf-8")
    hant = PRODUCER_HANT.read_text(encoding="utf-8")
    hant_v003 = CHECKER_HANT_V003.read_text(encoding="utf-8")

    hans_body = body(PRODUCER_HANS)
    prior_hans_body = body(CHECKER_HANS)
    hant_body = body(PRODUCER_HANT)
    prior_hant_body = body(CHECKER_HANT_V002)

    math_index = json.loads(MATH_INDEX.read_text(encoding="utf-8"))
    tex_summary = json.loads(TEX_SUMMARY.read_text(encoding="utf-8"))
    unit_index = json.loads(UNIT_INDEX.read_text(encoding="utf-8"))
    pdf_verifier = json.loads(PDF_VERIFIER.read_text(encoding="utf-8"))
    build_record = json.loads(BUILD_RECORD.read_text(encoding="utf-8"))
    render_record = json.loads(RENDER_RECORD.read_text(encoding="utf-8"))

    symbolic_extra = math_index["symbolic_formula_inventory_excluding_localized_text_macros"]["extra_target_formulas"]
    symbolic_extra_counter = Counter(item["raw"] for item in symbolic_extra)
    expected_symbolic_extra = Counter(
        {
            "$\\mathfrak{M}$": 1,
            "$f_i(x)$": 1,
            "$\\mathfrak{c}_p$": 2,
            "$\\mathfrak{a}_p$": 1,
            "$\\mathfrak{Z}$": 1,
            "$\\lambda_i$": 1,
            "$\\mathfrak{I}$": 2,
        }
    )

    hans_required_terms = [
        "极大整环",
        "给定整环",
        "多项式环",
        "系数环",
        "整性基（即有限代数生成组）",
        "代数无关系统",
        "雅可比矩阵",
        "雅可比行列式",
        "包含于 $\\mathfrak{c}_p$",
        "非整代数数",
        "使每个 $\\lambda_i$",
        "生成元",
        "在第2点的附加假设下",
        "\\hbox{在 }\\mathfrak{I}\\hbox{ 中}",
        "\\hbox{在 }\\mathfrak{o}\\hbox{ 中}",
    ]
    hans_forbidden_terms = [
        "极大域",
        "给定域",
        "多项式域",
        "整环基",
        "函数矩阵",
        "函数行列式",
        "d.h.",
        "bezw.",
        "z.B.",
        "mod. p",
        "倍理想",
        "分数代数数",
        "每个整数均",
        "基元素",
        "商。--- 在",
    ]
    producer_hant_corrected_terms = ["這只會", "並", "代數無關系統"]
    producer_hant_prior_bad_terms = ["這隻會", "幷", "無關係統"]
    mixed_script_witnesses = ["数学问题", "众所周知", "消去理论", "代数量的算术理论"]
    corrected_script_witnesses = ["數學問題", "眾所周知", "消去理論", "代數量的算術理論"]

    term_checks = {
        "hans_required": [occurrences(hans, term) for term in hans_required_terms],
        "hans_forbidden": [occurrences(hans, term) for term in hans_forbidden_terms],
        "producer_hant_F012_F014_required": [occurrences(hant, term) for term in producer_hant_corrected_terms],
        "producer_hant_F012_F014_prior_bad_forms": [occurrences(hant, term) for term in producer_hant_prior_bad_terms],
        "producer_hant_F015_mixed_script_witnesses": [occurrences(hant, term) for term in mixed_script_witnesses],
        "candidate_hant_v003_mixed_script_witnesses": [occurrences(hant_v003, term) for term in mixed_script_witnesses],
        "candidate_hant_v003_corrected_script_witnesses": [occurrences(hant_v003, term) for term in corrected_script_witnesses],
        "candidate_hant_v003_rejected_forms": [
            occurrences(hant_v003, term) for term in ["于", "隻", "幷", "無關係統"]
        ],
    }

    assertions = {
        "source_identity": fact(SOURCE)["sha256"] == "DAED6EF21C297425F018C0AE6B23BC5BDD05C0B86984B3FC25FB5937DCBEBD6A",
        "producer_hans_body_bytes": len(hans_body) == 29808,
        "producer_hans_body_sha256": digest(hans_body) == "54061274DFDE806F491EE424277886ED4C4CEEF3F7E0315DFD1039AACF69F18A",
        "producer_hans_body_byte_identical_to_validated_checker_candidate": hans_body == prior_hans_body,
        "producer_hant_body_bytes": len(hant_body) == 29808,
        "producer_hant_body_sha256": digest(hant_body) == "E8B36BFF9AB5ABE1CB6FE1AF45370C101B11BBA8EA5A0491EAAC0B63CD05F2D0",
        "producer_hant_body_byte_identical_to_prior_checker_candidate_v002": hant_body == prior_hant_body,
        "all_42_structural_units_transfer_by_exact_source_and_candidate_body_identity": (
            unit_index["completeness_result"]["unit_count"] == 42
            and unit_index["completeness_result"]["source_target_presence_pass"] is True
            and not unit_index["completeness_result"]["missing_units"]
            and not unit_index["completeness_result"]["duplicate_units"]
            and hans_body == prior_hans_body
        ),
        "formula_parser_errors_zero": tex_summary["parser_error_count"] == 0,
        "source_formula_count_478": tex_summary["source_formula_count"] == 478,
        "source_symbolic_formula_preservation_pass": tex_summary["source_symbolic_formula_preservation_pass"] is True,
        "symbolic_missing_source_formula_count_zero": tex_summary["symbolic_missing_source_formula_count"] == 0,
        "nine_symbolic_target_extras_are_the_previously_reviewed_explicit_repeats": symbolic_extra_counter == expected_symbolic_extra,
        "environment_sequence_equal": tex_summary["environment_name_action_sequences_equal"] is True,
        "structural_signature_equal": tex_summary["structural_signatures_equal_excluding_footnote_numbers"] is True,
        "all_hans_required_terms_present": all(row["count"] > 0 for row in term_checks["hans_required"]),
        "all_hans_rejected_terms_absent": all(row["count"] == 0 for row in term_checks["hans_forbidden"]),
        "producer_hant_exact_F012_F014_forms_present": all(row["count"] > 0 for row in term_checks["producer_hant_F012_F014_required"]),
        "producer_hant_prior_F012_F014_forms_absent": all(row["count"] == 0 for row in term_checks["producer_hant_F012_F014_prior_bad_forms"]),
        "producer_hant_mixed_script_F015_confirmed": all(row["count"] > 0 for row in term_checks["producer_hant_F015_mixed_script_witnesses"]),
        "candidate_hant_v003_mixed_script_witnesses_absent": all(row["count"] == 0 for row in term_checks["candidate_hant_v003_mixed_script_witnesses"]),
        "candidate_hant_v003_corrected_script_witnesses_present": all(row["count"] > 0 for row in term_checks["candidate_hant_v003_corrected_script_witnesses"]),
        "candidate_hant_v003_rejected_forms_absent": all(row["count"] == 0 for row in term_checks["candidate_hant_v003_rejected_forms"]),
        "pdf_verifier_all_pass": pdf_verifier["all_pass"] is True,
        "serial_builds_all_pass": build_record["all_builds_two_serial_passes_exit_zero"] is True,
        "all_pdfs_six_pages": build_record["all_pdfs_six_pages"] is True,
        "all_render_sets_six_pages": render_record["all_expected_page_counts_six"] is True,
        "producer_checker_hans_rasters_equal": render_record["producer_checker_hans_pixel_identical"] is True,
        "producer_checker_rejected_hant_rasters_equal": render_record["producer_checker_rejected_hant_pixel_identical"] is True,
        "candidate_hant_only_page5_changed": render_record["candidate_hant_pages_differing_from_rejected_hant"] == [5],
    }

    finding_dispositions: dict[str, dict[str, object]] = {}
    for index in range(1, 12):
        finding_id = f"ZHCHK-P35-F{index:03d}"
        finding_dispositions[finding_id] = {
            "class": "target_translation_defect",
            "producer_v002_state": "resolved_in_exact_hans_body",
            "checker_validation": "pass",
            "evidence": [
                "producer Hans body byte-identical to previously validated checker candidate",
                "fresh formula/structure/term/PDF/build/render replay",
            ],
        }
    finding_dispositions["ZHCHK-P35-F012"] = {
        "class": "tooling_defect",
        "producer_v002_state": "exact isolated loci resolved; four other Simplified 于 occurrences belong to distinct F015 false-protection span",
        "checker_validation": "pass_for_F012_loci; frozen Hant still rejected under F015",
    }
    finding_dispositions["ZHCHK-P35-F013"] = {
        "class": "unresolved_question",
        "producer_v002_state": "held_no_action",
        "checker_validation": "remains unresolved advisory; no German packet; no German mutation",
    }
    finding_dispositions["ZHCHK-P35-F014"] = {
        "class": "tooling_defect",
        "producer_v002_state": "five known 無關係統 loci resolved",
        "checker_validation": "pass_for_F014_loci; frozen Hant still rejected under F015",
    }
    finding_dispositions["ZHCHK-P35-F015"] = {
        "class": "tooling_defect",
        "producer_v002_state": "confirmed_major_mixed_script_defect",
        "checker_validation": "producer Hant rejected; checker candidate v003 text/structure/build/render/visual pass; producer integration required",
    }

    all_assertions_pass = all(assertions.values())
    record = {
        "record_id": "ZHCHK-P35-V002-SUBSTANTIVE-001",
        "record_type": "independent_checker_substantive_recheck",
        "recorded_at": recorded_at,
        "authority": {
            "binder_id": "NOETH-DE-BINDER-P35-20260804-001",
            "source_native_sha256": "2E205B2C51B9093FC61C77A9A1DF1C3399FCF098706CEC69134400F1ECC8E491",
            "source_lf_sha256": "DAED6EF21C297425F018C0AE6B23BC5BDD05C0B86984B3FC25FB5937DCBEBD6A",
            "pointer_v004_route_metadata_only": True,
        },
        "files": {
            "source": fact(SOURCE),
            "producer_hans": fact(PRODUCER_HANS),
            "producer_hant_rejected": fact(PRODUCER_HANT),
            "prior_checker_hans_candidate": fact(CHECKER_HANS),
            "prior_checker_hant_candidate_v002": fact(CHECKER_HANT_V002),
            "checker_hant_candidate_v003": fact(CHECKER_HANT_V003),
            "unit_index": fact(UNIT_INDEX),
            "terminology_evidence": fact(TERM_EVIDENCE),
            "math_index": fact(MATH_INDEX),
            "tex_summary": fact(TEX_SUMMARY),
            "hant_audit": fact(HANT_AUDIT),
            "hant_candidate_record": fact(HANT_CANDIDATE_RECORD),
            "pdf_verifier": fact(PDF_VERIFIER),
            "build_record": fact(BUILD_RECORD),
            "render_record": fact(RENDER_RECORD),
            "visual_ledger": fact(VISUAL_LEDGER),
        },
        "body_transfer": {
            "hans": {"bytes": len(hans_body), "sha256": digest(hans_body), "prior_candidate_equal": hans_body == prior_hans_body},
            "hant_rejected": {"bytes": len(hant_body), "sha256": digest(hant_body), "prior_candidate_v002_equal": hant_body == prior_hant_body},
            "epistemic_effect": "Exact body identity transfers the earlier complete semantic and PRC-terminology validation to producer Hans; it also proves F015 was inherited from the prior checker Hant candidate rather than introduced by a producer body deviation.",
        },
        "formula_and_structure": {
            "source_formula_count": tex_summary["source_formula_count"],
            "target_formula_count": tex_summary["target_formula_count"],
            "source_symbolic_formula_preservation_pass": tex_summary["source_symbolic_formula_preservation_pass"],
            "symbolic_missing_source_formula_count": tex_summary["symbolic_missing_source_formula_count"],
            "symbolic_extra_target_formula_count": tex_summary["symbolic_extra_target_formula_count"],
            "symbolic_extra_inventory": dict(symbolic_extra_counter),
            "environment_sequence_equal": tex_summary["environment_name_action_sequences_equal"],
            "structural_signature_equal": tex_summary["structural_signatures_equal_excluding_footnote_numbers"],
            "structural_unit_count": unit_index["completeness_result"]["unit_count"],
        },
        "term_checks": term_checks,
        "assertions": assertions,
        "all_assertions_pass": all_assertions_pass,
        "finding_dispositions": finding_dispositions,
        "result": {
            "hans_zh_Hans_CN": "accepted",
            "frozen_controlled_generic_hant_v002": "rejected_ZHCHK-P35-F015",
            "checker_controlled_generic_hant_candidate_v003": "validated_correction_candidate_nonregional",
            "package": "rejected_target_only_Hant_rebuild_and_new_frozen_rehandoff_required",
            "new_findings": ["ZHCHK-P35-F015"],
            "german_finding_packet": None,
            "german_mutated": False,
            "sga_touched": False,
        },
        "claim_limits": {
            "hans": "PRC-oriented Simplified Chinese; no zh-Hans-SG target exists",
            "hant": "controlled generic Traditional script transport only; not TW/HK/MO localization",
        },
    }
    if not all_assertions_pass:
        failed = [name for name, value in assertions.items() if not value]
        raise RuntimeError(f"Substantive assertions failed: {failed}")
    OUT.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")

    rows: list[dict[str, object]] = [
        {
            "record_type": "ledger_init",
            "recorded_at": recorded_at,
            "paper_id": "NOETHER-P35",
            "recheck_id": "ZHCHK-P35-V002-SUBSTANTIVE-001",
            "state": record["result"]["package"],
        }
    ]
    for finding_id, disposition in finding_dispositions.items():
        rows.append(
            {
                "record_type": "finding_recheck_disposition",
                "recorded_at": recorded_at,
                "paper_id": "NOETHER-P35",
                "finding_id": finding_id,
                **disposition,
            }
        )
    DISPOSITIONS.write_text(
        "".join(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n" for row in rows),
        encoding="utf-8",
        newline="\n",
    )

    print(
        json.dumps(
            {
                "record": fact(OUT),
                "dispositions": fact(DISPOSITIONS),
                "all_assertions_pass": all_assertions_pass,
                "result": record["result"],
            },
            ensure_ascii=True,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
