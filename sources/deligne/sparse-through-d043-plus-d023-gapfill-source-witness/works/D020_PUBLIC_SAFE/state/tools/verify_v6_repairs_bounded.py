#!/usr/bin/env python3
"""Bounded static verification of the exact D020 V6 hygiene repair."""
from __future__ import annotations

import json
import pathlib

from bounded_streaming_audit import count_term_streaming, stream_sha256, write_json_atomic


ROOT = pathlib.Path(__file__).resolve().parent.parent
D020 = ROOT.parents[1]
V5_AUDIT = D020 / "audit_cold" / "S06_math_v5_01"
MANIFEST = V5_AUDIT / "SUBJECT_MANIFEST.json"
CHUNK_BYTES = 64 * 1024
EXCLUDED = {
    "tools/vendor/bin/l2m.exe",
    "tools/vendor/bin/latex2mathml.exe",
}
TEXT_REPAIRED = {
    "README.md",
    "audit/V5_POSTBUILD_VERIFICATION.json",
    "control/ZENODO_D020_ID.md",
}


def main() -> int:
    if stream_sha256(MANIFEST) != "905DB30253DC8C5159E983115B51236512C8825FFF2DCE7D7D0B212AFC7B2C25":
        raise RuntimeError("frozen V5 manifest identity changed")
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    rows = {row["path"]: row for row in manifest["files"]}
    assert len(rows) == 317 and sum(row["bytes"] for row in rows.values()) == 106_718_848

    mismatches = []
    protected_members = 0
    protected_bytes = 0
    for relative, row in sorted(rows.items()):
        target = ROOT / pathlib.PurePosixPath(relative)
        if relative in EXCLUDED:
            if target.exists():
                mismatches.append({"path": relative, "problem": "excluded_path_present"})
            continue
        if relative in TEXT_REPAIRED:
            if not target.is_file():
                mismatches.append({"path": relative, "problem": "text_repair_target_missing"})
            continue
        protected_members += 1
        protected_bytes += row["bytes"]
        if not target.is_file():
            mismatches.append({"path": relative, "problem": "missing"})
            continue
        observed_bytes = target.stat().st_size
        observed_sha256 = stream_sha256(target, CHUNK_BYTES)
        if observed_bytes != row["bytes"] or observed_sha256 != row["sha256"]:
            mismatches.append(
                {
                    "path": relative,
                    "problem": "identity_mismatch",
                    "expected_bytes": row["bytes"],
                    "observed_bytes": observed_bytes,
                    "expected_sha256": row["sha256"],
                    "observed_sha256": observed_sha256,
                }
            )
    assert protected_members == 312 and protected_bytes == 106_487_435 and not mismatches

    profile_term = pathlib.Path.home().name
    ascii_term = profile_term.encode("utf-8")
    utf16_term = profile_term.encode("utf-16le")
    identity_hits = []
    for path in sorted(path for path in ROOT.rglob("*") if path.is_file()):
        relative = path.relative_to(ROOT).as_posix()
        if relative.startswith("build/"):
            continue
        ascii_count = count_term_streaming(
            path,
            ascii_term,
            case_insensitive_ascii=True,
            chunk_bytes=CHUNK_BYTES,
        )
        utf16_count = count_term_streaming(
            path,
            utf16_term,
            case_insensitive_ascii=True,
            chunk_bytes=CHUNK_BYTES,
        )
        if ascii_count or utf16_count:
            identity_hits.append(
                {
                    "path": relative,
                    "occurrences": ascii_count + utf16_count,
                }
            )
    assert not identity_hits

    postbuild = json.loads((ROOT / "audit" / "V5_POSTBUILD_VERIFICATION.json").read_text(encoding="utf-8"))
    assert postbuild["production_invocation"]["command"].startswith("%USERPROFILE%\\")
    control = (ROOT / "control" / "ZENODO_D020_ID.md").read_text(encoding="utf-8")
    assert control.count("%USERPROFILE%") == 4
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "inherited V4 bytes" not in readme
    assert "until one rebuild is performed" not in readme
    assert "audit/FINAL_SOURCE_FREEZE_V7.tsv" in readme
    assert "verified promoted V5 outputs" in readme
    assert "268,435,456-byte memory limit" in readme

    bounded_tool = ROOT / "tools" / "bounded_streaming_audit.py"
    guard_tool = ROOT / "tools" / "run_low_memory_guard.py"
    for term in (b"difflib", b"SequenceMatcher"):
        assert count_term_streaming(bounded_tool, term, case_insensitive_ascii=True) == 0
        assert count_term_streaming(guard_tool, term, case_insensitive_ascii=True) == 0
    self_test = json.loads((ROOT / "audit" / "V6_BOUNDED_TOOL_SELFTEST.json").read_text(encoding="utf-8"))
    self_test_guard = json.loads((ROOT / "audit" / "V6_BOUNDED_TOOL_SELFTEST_JOB_GUARD.json").read_text(encoding="utf-8"))
    assert self_test["status"] == self_test_guard["status"] == "PASS"
    assert self_test["tested_tools"]["bounded_streaming_audit.py"] == stream_sha256(bounded_tool)
    assert self_test["tested_tools"]["run_low_memory_guard.py"] == stream_sha256(guard_tool)
    assert self_test_guard["result"]["tree_empty"]
    assert self_test_guard["result"]["peak_job_memory_used_bytes"] < 268_435_456

    sanitation = json.loads((ROOT / "audit" / "V6_H01_TEXT_SANITIZATION_RECEIPT.json").read_text(encoding="utf-8"))
    sanitation_guard = json.loads((ROOT / "audit" / "V6_H01_SANITIZE_JOB_GUARD.json").read_text(encoding="utf-8"))
    assert sanitation["status"] == sanitation_guard["status"] == "PASS"
    assert sanitation_guard["result"]["tree_empty"]

    payload = {
        "schema": "D020_V6_BOUNDED_STATIC_REPAIR_PROOF_V1",
        "status": "PASS_REPAIRS_READY_FOR_FUTURE_INDEPENDENT_COLD_AUDIT",
        "scope": "No PDF render, page visual review, TeX engine, or full-paper cold audit was run.",
        "streaming_contract": {
            "chunk_bytes": CHUNK_BYTES,
            "maximum_chunk_bytes": 1_048_576,
            "whole_large_file_reads": False,
            "quadratic_document_comparison": False,
        },
        "frozen_v5_source_manifest": {
            "bytes": MANIFEST.stat().st_size,
            "sha256": stream_sha256(MANIFEST),
            "members": len(rows),
            "member_bytes": sum(row["bytes"] for row in rows.values()),
        },
        "protected_v5_members": {
            "expected_and_matching": protected_members,
            "bytes": protected_bytes,
            "mismatches": mismatches,
        },
        "exact_exclusions_absent": sorted(EXCLUDED),
        "text_repairs": {
            "targets": sorted(TEXT_REPAIRED),
            "candidate_surface_local_account_name_hits": identity_hits,
            "postbuild_command_sanitized": True,
            "control_profile_prefixes_sanitized": 4,
            "readme_h02_corrected": True,
        },
        "bounded_tools": {
            "bounded_streaming_audit.py": {
                "bytes": bounded_tool.stat().st_size,
                "sha256": stream_sha256(bounded_tool),
            },
            "run_low_memory_guard.py": {
                "bytes": guard_tool.stat().st_size,
                "sha256": stream_sha256(guard_tool),
            },
            "self_test_status": self_test["status"],
            "self_test_guard_cap_bytes": self_test_guard["contract"]["aggregate_job_memory_limit_bytes"],
            "self_test_peak_job_memory_used_bytes": self_test_guard["result"]["peak_job_memory_used_bytes"],
            "self_test_tree_empty": self_test_guard["result"]["tree_empty"],
        },
        "tex_asset_html_pdf_inputs_changed": False,
        "tex_rebuild_required": False,
        "full_142_page_audit_authorized_or_run": False,
    }
    write_json_atomic(ROOT / "audit" / "V6_BOUNDED_STATIC_REPAIR_PROOF.json", payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
