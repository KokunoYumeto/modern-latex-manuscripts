from __future__ import annotations

import hashlib
import json
from pathlib import Path


SCRIPT = Path(__file__).resolve()
RECHECK = SCRIPT.parents[1]
RETURN = RECHECK / "return"
SNAPSHOT = RETURN / "sealed_member_snapshots" / "ZHCHK-NOETHER-P35-V002-RETURN-001"
MANIFEST = RETURN / "SHA256SUMS.txt"
RECEIPT = RETURN / "P35_V002_CHECKER_RETURN_RECEIPT.json"
VERIFICATION = RETURN / "P35_V002_RETURN_VERIFICATION.json"
SEAL = RETURN / "P35_V002_RETURN_SEAL.json"
RECORDED_AT = "2026-08-04T07:42:00+02:00"


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def fact(path: Path) -> dict[str, object]:
    data = path.read_bytes()
    return {"path": str(path), "bytes": len(data), "sha256": digest(data)}


def write_json(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def jsonl(path: Path) -> list[dict[str, object]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def parse_manifest(path: Path) -> list[tuple[str, int, str]]:
    rows: list[tuple[str, int, str]] = []
    for raw in path.read_text(encoding="utf-8-sig").splitlines():
        if not raw or raw.startswith("#"):
            continue
        sha, size, rel = raw.split("  ", 2)
        rows.append((sha.upper(), int(size), rel))
    return rows


def check(name: str, state: bool, detail: object) -> dict[str, object]:
    return {"check": name, "pass": bool(state), "detail": detail}


def main() -> int:
    receipt = json.loads(RECEIPT.read_text(encoding="utf-8"))
    rows = parse_manifest(MANIFEST)
    failures: list[dict[str, object]] = []
    for expected_sha, expected_bytes, rel in rows:
        path = RECHECK / Path(rel)
        if not path.is_file():
            failures.append({"path": rel, "failure": "missing"})
            continue
        actual = fact(path)
        if actual["bytes"] != expected_bytes or actual["sha256"] != expected_sha:
            failures.append({"path": rel, "failure": "identity", "actual": actual})

    substantive = json.loads((RECHECK / "evidence/P35_V002_SUBSTANTIVE_RECHECK_RECORD.json").read_text(encoding="utf-8"))
    pdf_verify = json.loads((RECHECK / "build/P35_V002_PDF_TEXT_METADATA_VERIFICATION.json").read_text(encoding="utf-8"))
    build = json.loads((RECHECK / "build/P35_V002_CHECKER_BUILD_RECORD.json").read_text(encoding="utf-8"))
    render = json.loads((RECHECK / "render/P35_V002_RENDER_RECORD.json").read_text(encoding="utf-8"))
    candidate = json.loads((RECHECK / "evidence/P35_HANT_CHECKER_CANDIDATE_BUILD_RECORD_v003.json").read_text(encoding="utf-8"))
    structural_hans = json.loads((RECHECK / "structural/P35_TEX_AUDIT_SUMMARY.json").read_text(encoding="utf-8"))
    structural_hant = json.loads((RECHECK / "structural/hant_candidate_v003/P35_TEX_AUDIT_SUMMARY.json").read_text(encoding="utf-8"))
    findings = jsonl(SNAPSHOT / "P35_FINDING_LEDGER.jsonl")
    difficulties = jsonl(SNAPSHOT / "P35_DIFFICULTY_FAILURE_LEDGER.jsonl")
    visual = jsonl(RECHECK / "render/P35_V002_VISUAL_QA_LEDGER.jsonl")
    page_reviews = [r for r in visual if r.get("record_type") == "page_review"]
    visual_failures = [r for r in page_reviews if r.get("content_state") != "pass"]
    final_f015 = [r for r in findings if r.get("finding_id") == "ZHCHK-P35-F015"][-1]
    hard011_corrections = [r for r in difficulties if r.get("issue_id") == "ZHCHK-P35-HARD-011" and r.get("record_type") == "resolution"]

    checks = [
        check("manifest_entry_count", len(rows) == receipt["manifest_policy"]["selected_member_count"] == 39, len(rows)),
        check("manifest_paths_unique", len(rows) == len({r[2] for r in rows}), len({r[2] for r in rows})),
        check("manifest_declared_members_exact", not failures, failures),
        check("receipt_identity_and_state", receipt["receipt_id"] == "ZHCHK-NOETHER-P35-V002-RETURN-001" and receipt["state"] == "REJECTED_HANT_ONLY_REBUILD_AND_NEW_FROZEN_REHANDOFF_REQUIRED", receipt["state"]),
        check("custody_external_and_snapshot_replay", receipt["custody"]["external_manifest_replay"]["all_pass"] and receipt["custody"]["checker_snapshot_manifest_replay"]["all_pass"], {"external": receipt["custody"]["external_manifest_replay"]["declared_entries"], "snapshot": receipt["custody"]["checker_snapshot_manifest_replay"]["declared_entries"]}),
        check("accepted_rejected_disposition", receipt["disposition"]["zh_Hans_CN_v002"] == "accepted" and receipt["disposition"]["frozen_controlled_generic_Hant_v002"] == "rejected_ZHCHK-P35-F015" and receipt["disposition"]["package"].startswith("rejected_"), receipt["disposition"]),
        check("F015_coordinates", receipt["F015"]["target_lines"] == {"false_opener_line": 244, "false_span_end_line": 272, "visible_simplified_lines": [245, 269]} and receipt["F015"]["false_protected_span_characters"] == 2075, receipt["F015"]["target_lines"]),
        check("F015_candidate_identities", receipt["F015"]["checker_candidate_tex"]["sha256"] == "54DE9B43850376FD19306A11FC682166D8F34A4CA6D73E0940695357CE74A005" and receipt["F015"]["checker_candidate_pdf"]["sha256"] == "5595AEBC8A59247D0E87BC94D9D350B031BCEF6C071BC34642EA9F6C0E695A15" and receipt["F015"]["correction_diff"]["sha256"] == "A87F91E27B5BA0CD25BB3983A55140F4C0C7F1AE32CE6A6FE7AFF0EAB96DD8D4", receipt["F015"]),
        check("substantive_all_assertions", substantive["all_assertions_pass"] is True and substantive["result"]["hans_zh_Hans_CN"] == "accepted" and substantive["result"]["frozen_controlled_generic_hant_v002"] == "rejected_ZHCHK-P35-F015", substantive["result"]),
        check("Hans_symbolic_structure", structural_hans["source_formula_count"] == 478 and structural_hans["symbolic_missing_source_formula_count"] == 0 and structural_hans["symbolic_extra_target_formula_count"] == 9 and structural_hans["source_symbolic_formula_preservation_pass"] and structural_hans["environment_name_action_sequences_equal"] and structural_hans["structural_signatures_equal_excluding_footnote_numbers"], structural_hans),
        check("candidate_Hant_symbolic_structure", structural_hant["source_formula_count"] == 478 and structural_hant["symbolic_missing_source_formula_count"] == 0 and structural_hant["symbolic_extra_target_formula_count"] == 9 and structural_hant["source_symbolic_formula_preservation_pass"] and structural_hant["environment_name_action_sequences_equal"] and structural_hant["structural_signatures_equal_excluding_footnote_numbers"], structural_hant),
        check("candidate_scanner_streams", candidate["scanner"]["math_span_count_hans"] == candidate["scanner"]["math_span_count_hant"] == 487 and candidate["scanner"]["math_stream_equal"] and candidate["scanner"]["tex_control_count_hans"] == candidate["scanner"]["tex_control_count_hant"] == 790 and candidate["scanner"]["tex_control_stream_equal"] and candidate["scanner"]["legacy_false_display_span_count"] == 0, candidate["scanner"]),
        check("serial_builds", build["all_builds_two_serial_passes_exit_zero"] and build["all_pdfs_six_pages"] and build["no_overfull_boxes"] and build["no_missing_characters"], {k: build[k] for k in ["all_builds_two_serial_passes_exit_zero", "all_pdfs_six_pages", "no_overfull_boxes", "no_missing_characters"]}),
        check("pdf_text_metadata", pdf_verify["all_pass"] is True, pdf_verify["finding_disposition"]),
        check("fresh_renders", render["all_expected_page_counts_six"] and render["producer_checker_hans_pixel_identical"] and render["producer_checker_rejected_hant_pixel_identical"] and render["candidate_hant_pages_differing_from_rejected_hant"] == [5], render["page_counts"]),
        check("visual_page_accounting", len(page_reviews) == 30 and all(r.get("layout_state") == "pass" for r in page_reviews), {"reviews": len(page_reviews), "targets": sorted({r["target"] for r in page_reviews})}),
        check("visual_F015_only", len(visual_failures) == 2 and {(r["target"], r["page"], r["content_state"]) for r in visual_failures} == {("producer_hant_rejected", 5, "fail_ZHCHK-P35-F015"), ("checker_hant_rejected_rebuild", 5, "fail_ZHCHK-P35-F015")}, visual_failures),
        check("append_only_finding_disposition", final_f015["validation_state"] == "producer_Hant_v002_rejected; checker_candidate_v003_validated_nonregional; producer_Hant_only_rebuild_and_new_freeze_required", final_f015),
        check("HARD011_append_only_hash_correction", bool(hard011_corrections) and any("9E4CD793BC691B0B867F13CB9BA60A55A21DCC50ED5CF2D8B88F3CC33A6BEA1A" in json.dumps(r) and "AAB64439C354E503F3737050B0B0E0A8003DCC9E0A0D338819D5CDDA3FF3909F" in json.dumps(r) for r in hard011_corrections), len(hard011_corrections)),
        check("German_and_SGA_scope", receipt["scope_guards"]["German_finding_packet"] is None and receipt["scope_guards"]["German_mutated"] is False and receipt["scope_guards"]["SGA_touched"] is False, receipt["scope_guards"]),
    ]
    all_pass = all(item["pass"] for item in checks)
    verification = {
        "verification_id": "ZHCHK-NOETHER-P35-V002-RETURN-VERIFY-001",
        "record_type": "independent_checker_selected_return_manifest_verification",
        "recorded_at": RECORDED_AT,
        "manifest": fact(MANIFEST),
        "receipt": fact(RECEIPT),
        "declared_member_count": len(rows),
        "scope": "declared selected return members only; no whole-checker-tree extra-file assertion",
        "checks": checks,
        "all_pass": all_pass,
    }
    write_json(VERIFICATION, verification)
    if not all_pass:
        print(json.dumps(verification, ensure_ascii=True, indent=2))
        return 1

    seal = {
        "seal_id": "ZHCHK-NOETHER-P35-V002-RETURN-SEAL-001",
        "record_type": "hash_pinned_checker_return_seal",
        "recorded_at": RECORDED_AT,
        "state": receipt["state"],
        "summary": fact(RETURN / "P35_V002_CHECKER_RETURN_SUMMARY.md"),
        "receipt": fact(RECEIPT),
        "selected_manifest": fact(MANIFEST),
        "manifest_entries": len(rows),
        "verification": fact(VERIFICATION),
        "verification_all_pass": True,
        "accepted_hans_tex_sha256": receipt["accepted_hans"]["tex"]["sha256"],
        "accepted_hans_pdf_sha256": receipt["accepted_hans"]["pdf"]["sha256"],
        "rejected_hant_tex_sha256": receipt["rejected_hant"]["tex"]["sha256"],
        "rejected_hant_pdf_sha256": receipt["rejected_hant"]["pdf"]["sha256"],
        "validated_candidate_hant_tex_sha256": receipt["F015"]["checker_candidate_tex"]["sha256"],
        "validated_candidate_hant_pdf_sha256": receipt["F015"]["checker_candidate_pdf"]["sha256"],
        "correction_diff_sha256": receipt["F015"]["correction_diff"]["sha256"],
        "dispatch_target": "019f757c-95a5-7030-8b00-38762b5cdbfc",
        "German_dispatch": None,
        "SGA_touched": False,
    }
    write_json(SEAL, seal)
    print(json.dumps({"verification": fact(VERIFICATION), "seal": fact(SEAL), "all_pass": True}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
