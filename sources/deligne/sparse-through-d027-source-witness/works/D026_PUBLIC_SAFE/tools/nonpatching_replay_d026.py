#!/usr/bin/env python3
"""Run D026 cold audit in a fresh process and prove candidate bytes unchanged."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path


def digest(path: Path) -> dict[str, object]:
    value = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            value.update(chunk)
    return {"bytes": path.stat().st_size, "sha256": value.hexdigest().upper()}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", type=Path, required=True)
    args = parser.parse_args()
    base = args.base.resolve()

    fixed = [
        "input/selected/DELIGNE_D026_LOCAL_CONSTANTS_ARTIN_ORTHOGONAL_FINAL_CANON_FULL_STATE_BUNDLE.zip",
        "input/expanded_return/04_EXACT_S03_FULL_STATE_TRIO/DELIGNE_D026_LOCAL_CONSTANTS_ARTIN_ORTHOGONAL_S03_CUMULATIVE_FULL_STATE.zip",
        "input/expanded_state/source/20_AUTHORITY_DELIGNE_D026_LOCAL_CONSTANTS_ARTIN_ORTHOGONAL_18PP_IAS_300DPI.pdf",
        "input/expanded_state/source/21_COMPARATOR_DELIGNE_D026_LOCAL_CONSTANTS_ARTIN_ORTHOGONAL_18PP_COLLECTED_SPLIT.pdf",
        "input/expanded_state/salvage/30_UNTRUSTED_PRIOR_WORK_DELIGNE_D026.zip",
        "input/expanded_state/edition/source_language.ndjson",
        "input/expanded_state/edition/english_standalone.ndjson",
        "input/expanded_state/edition/apparatus.ndjson",
        "input/expanded_state/control/PAGE_MAP.tsv",
        "input/expanded_state/control/PRIOR_WORK_LEDGER.tsv",
        "source/Deligne_D026_FR.tex",
        "source/Deligne_D026_EN.tex",
        "source/Deligne_D026_APPARATUS.tex",
        "source/README.md",
        "source/ASSET_LEDGER.tsv",
        "output/pdf/Deligne_D026_FR.pdf",
        "output/pdf/Deligne_D026_EN.pdf",
        "output/pdf/Deligne_D026_FR.log",
        "output/pdf/Deligne_D026_EN.log",
        "qa/cold_audit/MANUAL_VISUAL_COLD_AUDIT.tsv",
        "tools/build_d026_editions.py",
        "tools/cold_audit_d026.py",
    ]
    render_paths = []
    for kind, prefix in (("authority", "authority"), ("fr", "page"), ("en", "page")):
        render_paths.extend(
            str(path.relative_to(base)).replace("\\", "/")
            for path in sorted((base / "qa" / "rendered" / kind).glob(f"{prefix}-*.png"))
        )
    paths = [base / relative for relative in fixed + render_paths]
    if len(render_paths) != 54 or not all(path.is_file() for path in paths):
        raise RuntimeError("cold-audit input set is incomplete")

    before = {str(path.relative_to(base)).replace("\\", "/"): digest(path) for path in paths}
    replay_report = base / "qa" / "cold_audit" / "FRESH_NONPATCHING_REPLAY_REPORT.json"
    subprocess.run(
        [sys.executable, str(base / "tools" / "cold_audit_d026.py"), "--base", str(base), "--report", str(replay_report)],
        check=True,
    )
    after = {str(path.relative_to(base)).replace("\\", "/"): digest(path) for path in paths}
    if before != after:
        changed = sorted(path for path in before if before[path] != after[path])
        raise RuntimeError(f"cold audit changed candidate inputs: {changed}")

    main_report = base / "qa" / "cold_audit" / "COLD_AUDIT_REPORT.json"
    if digest(main_report) != digest(replay_report):
        raise RuntimeError("fresh cold-audit report differs from the accepted report")

    receipt = {
        "schema_version": "deligne-d026-nonpatching-replay-v1",
        "work_id": "D026",
        "result": "PASS",
        "mode": "FRESH_PROCESS_NONPATCHING_REPLAY",
        "candidate_input_files": len(paths),
        "candidate_hashes_before_after_identical": True,
        "candidate_inputs": before,
        "cold_audit_report": {
            "path": str(replay_report.relative_to(base)).replace("\\", "/"),
            **digest(replay_report),
            "byte_identical_to": str(main_report.relative_to(base)).replace("\\", "/"),
        },
        "authorized_outputs_created": [
            str(replay_report.relative_to(base)).replace("\\", "/"),
            "qa/cold_audit/NONPATCHING_REPLAY_RECEIPT.json",
        ],
        "publication_actions": "NONE",
    }
    receipt_path = base / "qa" / "cold_audit" / "NONPATCHING_REPLAY_RECEIPT.json"
    receipt_path.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({
        "result": "PASS",
        "candidate_input_files": len(paths),
        "unchanged": True,
        "replay_report_sha256": receipt["cold_audit_report"]["sha256"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
