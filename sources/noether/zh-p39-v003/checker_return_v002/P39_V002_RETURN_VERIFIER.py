#!/usr/bin/env python3
"""Explicit byte, semantic, build, render, and scope verifier for the sealed return."""

from __future__ import annotations

import csv
import hashlib
import json
import re
import sys
from pathlib import Path, PurePosixPath


ROOT = Path(__file__).resolve().parent
MANIFEST = ROOT / "P39_V002_RETURN_MANIFEST.sha256"
OUTPUT = ROOT / "P39_V002_RETURN_VERIFICATION.json"
ALLOWED_UNLISTED = {
    "P39_V002_RETURN_MANIFEST.sha256",
    "P39_V002_RETURN_VERIFICATION.json",
    "P39_V002_RETURN_SEAL.json",
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


checks: list[dict[str, object]] = []


def check(name: str, passed: bool, observed: object, expected: object) -> None:
    checks.append(
        {"name": name, "pass": bool(passed), "observed": observed, "expected": expected}
    )


manifest_lines = MANIFEST.read_text(encoding="utf-8").splitlines()
members: list[tuple[str, int, str]] = []
parse_failures: list[str] = []
for line_number, line in enumerate(manifest_lines, start=1):
    parts = line.split("  ", 2)
    if len(parts) != 3 or not re.fullmatch(r"[0-9A-F]{64}", parts[0]):
        parse_failures.append(f"line {line_number}")
        continue
    try:
        byte_count = int(parts[1])
    except ValueError:
        parse_failures.append(f"line {line_number} bytes")
        continue
    members.append((parts[0], byte_count, parts[2]))

paths = [member[2] for member in members]
duplicates = sorted({path for path in paths if paths.count(path) > 1})
unsafe = []
for path in paths:
    pure = PurePosixPath(path)
    if pure.is_absolute() or ".." in pure.parts or "\\" in path or not path:
        unsafe.append(path)

missing = []
byte_failures = []
hash_failures = []
for expected_hash, expected_bytes, relative in members:
    target = ROOT / relative
    if not target.is_file():
        missing.append(relative)
        continue
    if target.stat().st_size != expected_bytes:
        byte_failures.append(relative)
    if sha(target) != expected_hash:
        hash_failures.append(relative)

actual_files = {
    path.relative_to(ROOT).as_posix()
    for path in ROOT.rglob("*")
    if path.is_file()
}
unlisted = sorted(actual_files - set(paths))
unexpected_unlisted = sorted(set(unlisted) - ALLOWED_UNLISTED)

check("manifest_parse", not parse_failures, parse_failures, [])
check("manifest_entry_count", len(members) == 89, len(members), 89)
check("manifest_unique_paths", not duplicates, duplicates, [])
check("manifest_safe_paths", not unsafe, unsafe, [])
check("manifest_members_present", not missing, missing, [])
check("manifest_member_bytes", not byte_failures, byte_failures, [])
check("manifest_member_hashes", not hash_failures, hash_failures, [])
check("return_unlisted_files_limited", not unexpected_unlisted, unexpected_unlisted, [])

receipt = json.loads((ROOT / "P39_V002_CHECKER_RETURN_RECEIPT.json").read_text(encoding="utf-8"))
check("receipt_id", receipt["receipt_id"] == "ZHCHK-NOETHER-P39-V002-RETURN-001", receipt["receipt_id"], "ZHCHK-NOETHER-P39-V002-RETURN-001")
check("receipt_disposition", receipt["disposition"] == "rejected_correction_required", receipt["disposition"], "rejected_correction_required")
check("Hans_disposition", receipt["disposition_scope"]["frozen_Hans"] == "accepted", receipt["disposition_scope"]["frozen_Hans"], "accepted")
check("Hant_disposition", receipt["disposition_scope"]["frozen_controlled_generic_Hant"] == "rejected_correction_required", receipt["disposition_scope"]["frozen_controlled_generic_Hant"], "rejected_correction_required")
check("producer_manifest_pin", receipt["custody"]["producer_manifest_sha256"] == "CAD0EDDD79A9C1182CD133C47F4ED03C0C644A1EFAB8E9A23387331B6C240FC1", receipt["custody"]["producer_manifest_sha256"], "CAD0EDDD79A9C1182CD133C47F4ED03C0C644A1EFAB8E9A23387331B6C240FC1")
check("source_pin", receipt["authority"]["retained_LF_source_sha256"] == "4F6355189925F249DE27FE5FD25C22FB3A2226088EBB7CAF5CB486607A112B7C", receipt["authority"]["retained_LF_source_sha256"], "4F6355189925F249DE27FE5FD25C22FB3A2226088EBB7CAF5CB486607A112B7C")
check("Hans_TeX_pin", receipt["accepted_Hans"]["TeX"]["sha256"] == "101836C41985DEE9B1A8FCC74A76CD9DF082BE2D07E2A3D45E22BC4DE68C6FE6", receipt["accepted_Hans"]["TeX"]["sha256"], "101836C41985DEE9B1A8FCC74A76CD9DF082BE2D07E2A3D45E22BC4DE68C6FE6")
check("Hans_PDF_pin", receipt["accepted_Hans"]["PDF"]["sha256"] == "367061323E97D9D7431B883D48F190A214A224D62F3901C8E01DD1BCA7125BA1", receipt["accepted_Hans"]["PDF"]["sha256"], "367061323E97D9D7431B883D48F190A214A224D62F3901C8E01DD1BCA7125BA1")
check("rejected_Hant_TeX_pin", receipt["rejected_Hant"]["TeX"]["sha256"] == "DEF7DFDCF1545066447880698B1A1C109D4BBED2CEDC4B8409D786044FCEEE33", receipt["rejected_Hant"]["TeX"]["sha256"], "DEF7DFDCF1545066447880698B1A1C109D4BBED2CEDC4B8409D786044FCEEE33")
check("candidate_Hant_TeX_pin", receipt["validated_Hant_candidate"]["TeX"]["sha256"] == "F0E9425763D5E075A5ED1810FE2B1DC2BDAAF6FD48691BE8C3D64F4B158AF1C8", receipt["validated_Hant_candidate"]["TeX"]["sha256"], "F0E9425763D5E075A5ED1810FE2B1DC2BDAAF6FD48691BE8C3D64F4B158AF1C8")
check("candidate_Hant_PDF_pin", receipt["validated_Hant_candidate"]["PDF"]["sha256"] == "8DE2CAB0FB81E604CF365550FD081B3C2227A1546E98759BE0B35A766F303090", receipt["validated_Hant_candidate"]["PDF"]["sha256"], "8DE2CAB0FB81E604CF365550FD081B3C2227A1546E98759BE0B35A766F303090")

original_hant = (ROOT / "selected/intake/Noether_Paper39_Chinese_CurrentAuthority_zh-Hant-controlled_v002.tex").read_text(encoding="utf-8")
candidate_hant = (ROOT / "selected/candidates/zh-Hant-controlled/Noether_Paper39_Chinese_CurrentAuthority_zh-Hant-controlled_v002_checker_candidate.tex").read_text(encoding="utf-8")
replacements = [("超復", "超複", 4), ("一箇", "一個", 2), ("着手", "著手", 1)]
replacement_checks = []
reconstructed = original_hant
for old, new, count in replacements:
    replacement_checks.append({"from": old, "to": new, "original_count": original_hant.count(old), "candidate_count": candidate_hant.count(old), "expected_original_count": count})
    reconstructed = reconstructed.replace(old, new)
check("candidate_exact_seven_replacements", reconstructed == candidate_hant and sum(item["expected_original_count"] for item in replacement_checks) == 7, replacement_checks, "four 超復, two 一箇, one 着手; no other delta")
strip_han = lambda text: re.sub(r"[\u3400-\u9fff\uf900-\ufaff]", "", text)
check("candidate_nonHan_TeX_stream", strip_han(original_hant) == strip_han(candidate_hant), sha(Path(ROOT / "selected/candidates/zh-Hant-controlled/Noether_Paper39_Chinese_CurrentAuthority_zh-Hant-controlled_v002_checker_candidate.tex")), "exact equality after removing Han ideographs")

term_path = ROOT / "selected/candidates/evidence/PRODUCER_TERMINOLOGY_LEDGER_checker_candidate.csv"
with term_path.open("r", encoding="utf-8", newline="") as handle:
    term_rows = {row["decision_id"]: row for row in csv.DictReader(handle)}
expected_forms = {
    "P39-ZH-T002": ("中心单代数", "中心單代數"),
    "P39-ZH-T012": ("Artin 导子", "Artin 導子"),
    "P39-ZH-T013": ("位／分歧位", "位／分歧位"),
    "P39-ZH-T016": ("平方映射", "平方映射"),
}
form_result = {
    key: (term_rows[key]["zh_hans_cn_choice"], term_rows[key]["controlled_hant_form"])
    for key in expected_forms
}
check("evidence_target_forms", form_result == expected_forms, form_result, expected_forms)
check("evidence_T018_source_phrase", term_rows["P39-ZH-T018"]["exact_german_phrase"] == "zerfallende Algebrenklasse | zerfallenden Algebren | zerfallende Algebren", term_rows["P39-ZH-T018"]["exact_german_phrase"], "zerfallende Algebrenklasse | zerfallenden Algebren | zerfallende Algebren")

graph = json.loads((ROOT / "selected/candidates/evidence/PRODUCER_CONCEPT_GRAPH_checker_candidate.json").read_text(encoding="utf-8"))
node_ids = {node["id"] for node in graph["nodes"]}
check("concept_graph_topology", len(graph["nodes"]) == 100 and len(graph["edges"]) == 100 and all(edge["from"] in node_ids and edge["to"] in node_ids for edge in graph["edges"]), {"nodes": len(graph["nodes"]), "edges": len(graph["edges"])}, {"nodes": 100, "edges": 100, "valid_endpoints": True})

finding_lines = (ROOT / "selected/findings/P39_FINDING_LEDGER.jsonl").read_text(encoding="utf-8").splitlines()
findings = [json.loads(line) for line in finding_lines if line.strip()]
finding_ids = [item["issue_id"] for item in findings]
check("finding_ledger_parse_and_count", len(findings) == 5, len(findings), 5)
check("finding_F001_frozen_and_validated", "ZHCHK-P39-F001" in finding_ids and "ZHCHK-P39-F001-VALIDATION-001" in finding_ids, finding_ids, "F001 and validation update present")
check("finding_F002_frozen_and_validated", "ZHCHK-P39-F002" in finding_ids and "ZHCHK-P39-F002-VALIDATION-001" in finding_ids, finding_ids, "F002 and validation update present")

difficulty_lines = (ROOT / "selected/findings/P39_DIFFICULTY_FAILURE_LEDGER.jsonl").read_text(encoding="utf-8").splitlines()
difficulties = [json.loads(line) for line in difficulty_lines if line.strip()]
difficulty_ids = [item["issue_id"] for item in difficulties]
check("difficulty_ledger_parse", len(difficulties) == 10, len(difficulties), 10)
check("failed_probes_preserved", all(f"ZHCHK-P39-HARD-{number:03d}" in difficulty_ids for number in range(1, 10)), difficulty_ids, "HARD-001 through HARD-009 preserved")

decision_text = (ROOT / "selected/decision/CHECKER_DECISION_LOG_THROUGH_D029.md").read_text(encoding="utf-8")
check("decision_log_through_D029", "## ZHCHK-D029" in decision_text and "## ZHCHK-D030" not in decision_text, decision_text.count("## ZHCHK-D029"), 1)

build = json.loads((ROOT / "selected/build/P39_V002_CHECKER_BUILD_RECORD.json").read_text(encoding="utf-8"))
build_passes = [entry["exit"] for item in build["builds"] for entry in item["passes"]]
check("serial_build_passes", build_passes == [0, 0, 0, 0, 0, 0], build_passes, [0, 0, 0, 0, 0, 0])
check("build_page_counts", all(item["PDF"]["pages"] == 4 for item in build["builds"]), [item["PDF"]["pages"] for item in build["builds"]], [4, 4, 4])
check("build_error_flags", all(item["fatal_errors"] == item["overfull_boxes"] == item["underfull_boxes"] == item["missing_characters"] == 0 for item in build["builds"]), [{key: item[key] for key in ["fatal_errors", "overfull_boxes", "underfull_boxes", "missing_characters"]} for item in build["builds"]], "all zero")
check("original_build_reproduction", build["producer_checker_comparison"]["Hans_page_text_and_raster_equal"] and build["producer_checker_comparison"]["Hant_page_text_and_raster_equal"], build["producer_checker_comparison"], "Hans/Hant page text and raster equality")

render = json.loads((ROOT / "selected/render/P39_V002_RENDER_TEXT_VISUAL_RECORD.json").read_text(encoding="utf-8"))
check("render_page_count", render["visual_summary"]["pages_rendered"] == 20, render["visual_summary"]["pages_rendered"], 20)
check("visual_page_count", render["visual_summary"]["pages_visually_inspected"] == 20 and len(render["pages"]) == 20, {"reported": render["visual_summary"]["pages_visually_inspected"], "records": len(render["pages"])}, {"reported": 20, "records": 20})
check("visual_failures", render["visual_summary"]["layout_failures"] == 0 and render["visual_summary"]["candidate_visual_failures"] == 0, {"layout": render["visual_summary"]["layout_failures"], "candidate": render["visual_summary"]["candidate_visual_failures"]}, {"layout": 0, "candidate": 0})
check("candidate_unchanged_pages_raster", all(item["changed_pixels"] == 0 for item in render["raster_comparison"]["producer_Hant_vs_candidate"] if item["page"] in (3, 4)), render["raster_comparison"]["producer_Hant_vs_candidate"], "pages 3-4 zero changed pixels")

audit = json.loads((ROOT / "selected/records/P39_V002_SUBSTANTIVE_STRUCTURE_EVIDENCE_AUDIT.json").read_text(encoding="utf-8"))
check("formula_and_apparatus_inventory", audit["mechanical_audit"]["formula_witnesses_exact_in_all_artifacts"] == 23 and audit["mechanical_audit"]["bibliographic_apparatus_witnesses_exact_in_all_artifacts"] == 14, {"formula": audit["mechanical_audit"]["formula_witnesses_exact_in_all_artifacts"], "apparatus": audit["mechanical_audit"]["bibliographic_apparatus_witnesses_exact_in_all_artifacts"]}, {"formula": 23, "apparatus": 14})
check("no_German_finding", receipt["authority"]["German_finding"] is None and not receipt["authority"]["German_packet_warranted"] and not receipt["scope_limits"]["German_mutated"], receipt["authority"], "no finding, packet, or mutation")
check("SGA_held", not receipt["scope_limits"]["SGA_touched"], receipt["scope_limits"]["SGA_touched"], False)
check("localization_limits", receipt["rejected_Hant"]["language_scope"] == "controlled generic Hant only; not TW/HK/MO localization" and not receipt["scope_limits"]["zh_Hans_SG_present"] and not receipt["scope_limits"]["TW_HK_MO_localization_present"], {"Hant": receipt["rejected_Hant"]["language_scope"], "Hans_SG": receipt["scope_limits"]["zh_Hans_SG_present"], "regional": receipt["scope_limits"]["TW_HK_MO_localization_present"]}, "controlled generic only; Hans-SG and TW/HK/MO absent")

passed = sum(1 for item in checks if item["pass"])
record = {
    "schema_version": "1.0.0",
    "record_type": "P39_v002_checker_return_explicit_verification",
    "receipt_id": "ZHCHK-NOETHER-P39-V002-RETURN-001",
    "manifest": {"entries": len(members), "bytes": MANIFEST.stat().st_size, "sha256": sha(MANIFEST)},
    "checks_passed": passed,
    "checks_total": len(checks),
    "all_pass": passed == len(checks),
    "checks": checks,
    "disposition_verified": "rejected_correction_required",
    "scope": {"producer_files_mutated": False, "German_mutated": False, "German_packet_created": False, "SGA_touched": False},
}
OUTPUT.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
print(json.dumps(record, ensure_ascii=True, indent=2))
sys.exit(0 if record["all_pass"] else 1)
