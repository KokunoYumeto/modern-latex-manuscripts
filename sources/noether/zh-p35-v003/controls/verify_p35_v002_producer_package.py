#!/usr/bin/env python3
"""Mechanical producer-package verifier for Noether P35 Chinese revision 2.

This verifies syntax, custody, hashes, body identity, build-record fields, and the
root checksum manifest. It performs no source, linguistic, semantic, formula,
terminology, visual, native, regional, publication, archive, or certification
check and never opens or renders a PDF.
"""

from __future__ import annotations

import argparse
from datetime import datetime
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "controls/P35_V002_PRODUCER_VERIFICATION.json"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def check(condition: bool, check_id: str, detail: str, checks: list[dict[str, object]]) -> None:
    checks.append({"id": check_id, "pass": bool(condition), "detail": detail})


def expected_file(checks: list[dict[str, object]], check_id: str, rel: str, size: int, digest: str) -> None:
    path = ROOT / rel
    ok = path.is_file() and path.stat().st_size == size and sha(path) == digest
    actual = "missing" if not path.is_file() else f"{path.stat().st_size} bytes / {sha(path)}"
    check(ok, check_id, f"{rel}: expected {size} bytes / {digest}; actual {actual}", checks)


def parse_json_and_jsonl(checks: list[dict[str, object]]) -> None:
    json_count = 0
    jsonl_records = 0
    failures: list[str] = []
    for path in sorted(ROOT.rglob("*.json")):
        try:
            json.loads(path.read_text(encoding="utf-8"))
            json_count += 1
        except Exception as exc:  # pragma: no cover - evidence path
            failures.append(f"{path.relative_to(ROOT)}: {exc}")
    for path in sorted(ROOT.rglob("*.jsonl")):
        for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip():
                continue
            try:
                json.loads(line)
                jsonl_records += 1
            except Exception as exc:  # pragma: no cover - evidence path
                failures.append(f"{path.relative_to(ROOT)}:{lineno}: {exc}")
    check(not failures, "JSON_JSONL_PARSE", f"json_files={json_count}; jsonl_records={jsonl_records}; failures={failures}", checks)


def verify_graph(checks: list[dict[str, object]]) -> None:
    path = ROOT / "evidence/revision2/P35_CORRECTION_CONCEPT_EVIDENCE_GRAPH_R2.json"
    graph = json.loads(path.read_text(encoding="utf-8"))
    ids = [node["id"] for node in graph["nodes"]]
    missing = [
        edge["id"]
        for edge in graph["edges"]
        if edge["from"] not in ids or edge["to"] not in ids
    ]
    check(len(ids) == len(set(ids)) and not missing, "TYPED_GRAPH", f"nodes={len(ids)}; edges={len(graph['edges'])}; dangling={missing}", checks)


def verify_v001_seed(checks: list[dict[str, object]]) -> None:
    v001 = ROOT.parent / "noether_paper35_zh_translation_001_20260804"
    manifest = ROOT / "controls/history/V001_SEED_SHA256SUMS.txt"
    entries = []
    failures = []
    for line in manifest.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        digest, size_text, rel = line.split("  ", 2)
        path = v001 / rel.replace("/", "\\")
        entries.append(rel)
        if not path.is_file() or path.stat().st_size != int(size_text) or sha(path) != digest.upper():
            failures.append(rel)
    extras = sorted(
        str(path.relative_to(v001)).replace("\\", "/")
        for path in v001.rglob("*")
        if path.is_file() and path.name != "SHA256SUMS.txt" and str(path.relative_to(v001)).replace("\\", "/") not in entries
    )
    check(len(entries) == 70 and not failures and not extras, "V001_SEED_REPLAY", f"entries={len(entries)}; failures={failures}; extras={extras}", checks)


def verify_bodies(checks: list[dict[str, object]]) -> None:
    hans_parts = [
        ROOT / "translation/corrected_segments_v002/P35_A_zh-Hans-CN_v002.tex",
        ROOT / "translation/corrected_segments_v002/P35_B_zh-Hans-CN_v002.tex",
        ROOT / "translation/corrected_segments_v002/P35_C_zh-Hans-CN_v002.tex",
    ]
    hans_body = b"".join(path.read_bytes() for path in hans_parts)
    hans_target = (ROOT / "build/zh-Hans-CN-v002/Noether_Paper35_Chinese_CurrentAuthority_zh-Hans-CN_v002.tex").read_bytes()
    hans_checker = (ROOT / "controls/checker_return_001/CHECKER_HANS_CANDIDATE.tex").read_bytes()
    check(
        len(hans_body) == 29808
        and hashlib.sha256(hans_body).hexdigest().upper() == "54061274DFDE806F491EE424277886ED4C4CEEF3F7E0315DFD1039AACF69F18A"
        and hans_target.count(hans_body) == 1
        and hans_checker.count(hans_body) == 1,
        "HANS_BODY_IDENTITY",
        f"bytes={len(hans_body)}; sha256={hashlib.sha256(hans_body).hexdigest().upper()}; target_occurrences={hans_target.count(hans_body)}; checker_occurrences={hans_checker.count(hans_body)}",
        checks,
    )

    marker = bytes([92]) + b"section*{"
    end = bytes([92]) + b"end{document}"
    hant_target = (ROOT / "build/zh-Hant-controlled-v002/Noether_Paper35_Chinese_CurrentAuthority_zh-Hant-controlled_v002.tex").read_bytes()
    hant_checker = (ROOT / "controls/checker_return_001/CHECKER_HANT_CANDIDATE_v002.tex").read_bytes()
    target_body = hant_target[hant_target.find(marker):hant_target.rfind(end)]
    checker_body = hant_checker[hant_checker.find(marker):hant_checker.rfind(end)]
    check(
        target_body == checker_body
        and len(target_body) == 29808
        and hashlib.sha256(target_body).hexdigest().upper() == "E8B36BFF9AB5ABE1CB6FE1AF45370C101B11BBA8EA5A0491EAAC0B63CD05F2D0",
        "HANT_BODY_IDENTITY",
        f"bytes={len(target_body)}; sha256={hashlib.sha256(target_body).hexdigest().upper()}; equal={target_body == checker_body}",
        checks,
    )


def verify_build_records(checks: list[dict[str, object]]) -> None:
    for target, rel in (
        ("hans", "controls/HANS_MECHANICAL_BUILD_RECORD_v002.json"),
        ("hant", "controls/HANT_MECHANICAL_BUILD_RECORD_v002.json"),
    ):
        record = json.loads((ROOT / rel).read_text(encoding="utf-8"))
        ok = (
            record["successful_passes"] == 2
            and all(item["exit_code"] == 0 for item in record["passes"])
            and record["final_pdf"]["pages_reported_by_log"] == 6
            and record["final_pdf"]["opened_or_rendered_by_producer"] is False
            and record["epistemic_boundary"]["visual_check_performed"] is False
        )
        check(ok, f"{target.upper()}_BUILD_RECORD", f"successful_passes={record['successful_passes']}; pages={record['final_pdf']['pages_reported_by_log']}; opened_or_rendered={record['final_pdf']['opened_or_rendered_by_producer']}", checks)


def verify_expected_files(checks: list[dict[str, object]]) -> None:
    expected_file(checks, "HANS_TEX", "build/zh-Hans-CN-v002/Noether_Paper35_Chinese_CurrentAuthority_zh-Hans-CN_v002.tex", 31328, "DDF7E898E706552028C2BCEAC4BBDE3D45487C6A339F7FA0A43968FF7E1F465C")
    expected_file(checks, "HANS_PDF", "build/zh-Hans-CN-v002/Noether_Paper35_Chinese_CurrentAuthority_zh-Hans-CN_v002.pdf", 274158, "F6626C3DC6FFB82E3CFD5C21FA3F74B99459D477E39093715802C49E91E2A18C")
    expected_file(checks, "HANT_TEX", "build/zh-Hant-controlled-v002/Noether_Paper35_Chinese_CurrentAuthority_zh-Hant-controlled_v002.tex", 31515, "FD16882FAC33B7FD7D0FFB882345168E40FA7F1F22FDEE83AFA2420627D1C054")
    expected_file(checks, "HANT_PDF", "build/zh-Hant-controlled-v002/Noether_Paper35_Chinese_CurrentAuthority_zh-Hant-controlled_v002.pdf", 306051, "8E77A4C511462C8ECF5876CE7EED0E3A9C4CAD8820A492BD8E665FB47FA50CF1")


def verify_manifest(checks: list[dict[str, object]]) -> None:
    manifest = ROOT / "SHA256SUMS.txt"
    entries = []
    failures = []
    for line in manifest.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        digest, size_text, rel = line.split("  ", 2)
        path = ROOT / rel.replace("/", "\\")
        entries.append(rel)
        if not path.is_file() or path.stat().st_size != int(size_text) or sha(path) != digest.upper():
            failures.append(rel)
    actual = sorted(
        str(path.relative_to(ROOT)).replace("\\", "/")
        for path in ROOT.rglob("*")
        if path.is_file() and path.name != "SHA256SUMS.txt"
    )
    extras = sorted(set(actual) - set(entries))
    missing = sorted(set(entries) - set(actual))
    check(not failures and not extras and not missing and len(entries) == len(set(entries)), "ROOT_MANIFEST", f"entries={len(entries)}; failures={failures}; extras={extras}; missing={missing}", checks)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check-manifest", action="store_true")
    parser.add_argument("--stdout-only", action="store_true")
    args = parser.parse_args()

    checks: list[dict[str, object]] = []
    parse_json_and_jsonl(checks)
    verify_graph(checks)
    verify_v001_seed(checks)
    verify_bodies(checks)
    verify_build_records(checks)
    verify_expected_files(checks)
    if args.check_manifest:
        verify_manifest(checks)

    report = {
        "schema_version": "1.0.0",
        "record_type": "producer_mechanical_package_verification",
        "recorded_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "work_id": "NOETHER-P35-ZH",
        "revision": "v002",
        "decision_id": "ZH-D132",
        "checks": checks,
        "check_count": len(checks),
        "all_pass": all(item["pass"] for item in checks),
        "manifest_checked": args.check_manifest,
        "producer_render_or_visual_check": False,
        "claim_limit": "Mechanical syntax, custody, hash, body identity, build-record, and manifest checks only; no substantive or visual validation."
    }
    text = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if not args.stdout_only:
        REPORT.write_text(text, encoding="utf-8", newline="\n")
    print(text, end="")
    return 0 if report["all_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
