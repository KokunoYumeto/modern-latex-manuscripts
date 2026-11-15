#!/usr/bin/env python3
"""Hostile mutation tests for preregistration v002.

All mutations occur in a temporary directory. The canonical package and all
upstream inputs are read-only. The validator is invoked as a subprocess so this
harness does not import either validator or builder internals.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


DEFAULT_WORKSPACE = Path(r"C:\Users\user\Documents\interlanguage")
PACKAGE_REL = Path(
    "03_projects/language_management/slavic_interslavic/00_lane_control/"
    "marginal_intelligibility_20260811/preregistration_v002"
)
CORE = [
    "ISV_MI_PREREGISTRATION_V002.json",
    "ISV_MI_PREREGISTRATION_V002.schema.json",
    "INPUT_REPIN_AUDIT_V002.json",
    "STAGE0_DESIGN_V002.csv",
    "PROTOCOL_V002.md",
    "README.md",
    "HOSTILE_FIXTURES_V002.json",
]
SEALED_EXCEPT_MANIFEST = CORE + [
    "build_isv_mi_preregistration_v002.py",
    "validate_isv_mi_preregistration_v002.py",
    "test_isv_mi_preregistration_v002_hostile.py",
    "verify_isv_mi_preregistration_v002_reproducibility.py",
    "CONSTRUCTION_HISTORY_V002.jsonl",
    "VALIDATION_RECEIPT_V002.json",
    "HOSTILE_RECEIPT_V002.json",
    "REPRODUCIBILITY_RECEIPT_V002.json",
]


def digest(path: Path) -> tuple[int, str, int]:
    raw = path.read_bytes()
    return len(raw), hashlib.sha256(raw).hexdigest().upper(), path.stat().st_mtime_ns


def run_validator(workspace: Path, validator: Path, root: Path, sealed: bool = False) -> subprocess.CompletedProcess[str]:
    command = [sys.executable, str(validator), "--workspace-root", str(workspace), "--package-root", str(root)]
    if sealed:
        command.extend(["--require-manifest", "--exact-tree"])
    return subprocess.run(
        command,
        check=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
        timeout=120,
    )


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def write(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workspace-root", type=Path, default=DEFAULT_WORKSPACE)
    parser.add_argument("--package-root", type=Path)
    args = parser.parse_args()
    workspace = args.workspace_root.resolve(strict=True)
    canonical = (args.package_root or workspace / PACKAGE_REL).resolve(strict=True)
    validator = canonical / "validate_isv_mi_preregistration_v002.py"
    watch = {p.name: digest(p) for p in canonical.iterdir() if p.is_file()}
    cases: list[dict] = []

    def case(case_id: str, mutate, expect: str = "reject") -> None:
        with tempfile.TemporaryDirectory(prefix=f".hostile-{case_id}-", dir=canonical) as temp:
            root = Path(temp) / "package"
            root.mkdir()
            for name in CORE:
                shutil.copy2(canonical / name, root / name)
            mutate(root)
            proc = run_validator(workspace, validator, root)
            passed = proc.returncode != 0 if expect == "reject" else proc.returncode == 0
            cases.append({"case_id": case_id, "expected": expect, "result": "PASS" if passed else "FAIL", "returncode": proc.returncode, "stdout": proc.stdout.strip()[-1000:], "stderr": proc.stderr.strip()[-1000:]})

    case("HOSTILE-001-duplicate-key", lambda root: (root / "ISV_MI_PREREGISTRATION_V002.json").write_text('{"status":"x","status":"y"}\n', encoding="utf-8"))

    def path_escape(root: Path) -> None:
        data = load(root / "INPUT_REPIN_AUDIT_V002.json")
        data["pins"][0]["workspace_relative_path"] = "../escape.json"
        write(root / "INPUT_REPIN_AUDIT_V002.json", data)
    case("HOSTILE-002-path-escape", path_escape)

    def hash_drift(root: Path) -> None:
        data = load(root / "INPUT_REPIN_AUDIT_V002.json")
        data["pins"][0]["expected_sha256"] = "0" * 64
        write(root / "INPUT_REPIN_AUDIT_V002.json", data)
    case("HOSTILE-003-hash-drift", hash_drift)

    def authority_substitution(root: Path) -> None:
        data = load(root / "ISV_MI_PREREGISTRATION_V002.json")
        data["current_state"]["german_authority"]["resolved_authority_id"] = "NOETH-DE-ED-0010"
        write(root / "ISV_MI_PREREGISTRATION_V002.json", data)
    case("HOSTILE-004-authority-substitution", authority_substitution)

    def false_readiness(root: Path) -> None:
        data = load(root / "ISV_MI_PREREGISTRATION_V002.json")
        data["status"] = "launch_ready"
        data["current_state"]["human_evidence"]["participants"] = 72
        write(root / "ISV_MI_PREREGISTRATION_V002.json", data)
    case("HOSTILE-005-false-readiness", false_readiness)

    def missing_branch(root: Path) -> None:
        data = load(root / "ISV_MI_PREREGISTRATION_V002.json")
        data["stage0_design"]["leaf_sampling"]["slots"] = [row for row in data["stage0_design"]["leaf_sampling"]["slots"] if row["macrobranch"] != "south_slavic"]
        write(root / "ISV_MI_PREREGISTRATION_V002.json", data)
    case("HOSTILE-006-missing-macrobranch", missing_branch)

    def cyclic_dag(root: Path) -> None:
        data = load(root / "ISV_MI_PREREGISTRATION_V002.json")
        canonical_dag = workspace / data["evidence_model"]["workspace_relative_path"]
        dag = load(canonical_dag)
        first_edge = dag["edges"][0]
        dag["edges"].append({"id": "HOSTILE-CYCLE-EDGE", "from": first_edge["to"], "to": first_edge["from"], "type": "hostile_reverse_edge", "channel": "veto"})
        hostile_dag = root / "HOSTILE_CYCLIC_DAG.json"
        write(hostile_dag, dag)
        raw = hostile_dag.read_bytes()
        data["evidence_model"]["workspace_relative_path"] = hostile_dag.relative_to(workspace).as_posix()
        data["evidence_model"]["bytes"] = len(raw)
        data["evidence_model"]["sha256"] = hashlib.sha256(raw).hexdigest().upper()
        write(root / "ISV_MI_PREREGISTRATION_V002.json", data)
    case("HOSTILE-007-cyclic-dag-substitution", cyclic_dag)

    def make_synthetic_sealed(root: Path) -> None:
        for name in SEALED_EXCEPT_MANIFEST:
            source = canonical / name
            if source.is_file():
                shutil.copy2(source, root / name)
            elif name.endswith("_RECEIPT_V002.json"):
                (root / name).write_text('{"status":"synthetic_hostile_fixture_only"}\n', encoding="utf-8", newline="\n")
            else:
                raise RuntimeError(f"missing fixture input {name}")
        files = []
        for name in sorted(SEALED_EXCEPT_MANIFEST):
            path = root / name
            files.append({"path": name, "bytes": path.stat().st_size, "sha256": hashlib.sha256(path.read_bytes()).hexdigest().upper()})
        write(root / "PACKAGE_MANIFEST_V002.json", {"status": "sealed_internal_fail_closed_not_launch_ready", "files": files})

    def sealed_case(case_id: str, mutate) -> None:
        with tempfile.TemporaryDirectory(prefix=f".hostile-{case_id}-", dir=canonical) as temp:
            root = Path(temp) / "package"
            root.mkdir()
            make_synthetic_sealed(root)
            baseline_proc = run_validator(workspace, validator, root, sealed=True)
            if baseline_proc.returncode != 0:
                cases.append({"case_id": case_id, "expected": "reject_after_synthetic_sealed_baseline_pass", "result": "FAIL", "returncode": baseline_proc.returncode, "stdout": baseline_proc.stdout.strip()[-1000:], "stderr": baseline_proc.stderr.strip()[-1000:]})
                return
            created = mutate(root)
            proc = run_validator(workspace, validator, root, sealed=True)
            passed = proc.returncode != 0
            cases.append({"case_id": case_id, "expected": "reject", "result": "PASS" if passed else "FAIL", "returncode": proc.returncode, "stdout": proc.stdout.strip()[-1000:], "stderr": proc.stderr.strip()[-1000:], "fixture": created})

    sealed_case("HOSTILE-008-unexpected-file", lambda root: ((root / "UNEXPECTED.tmp").write_text("unexpected\n", encoding="utf-8"), "ordinary extra file")[1])

    def add_reparse(root: Path) -> str:
        target = root.parent / "reparse-target"
        target.mkdir()
        link = root / "REPARSE_MEMBER"
        try:
            os.symlink(target, link, target_is_directory=True)
            return "directory symlink"
        except OSError:
            proc = subprocess.run(["cmd", "/c", "mklink", "/J", str(link), str(target)], check=False, capture_output=True, text=True, timeout=30)
            if proc.returncode != 0:
                raise RuntimeError(f"could not create reparse fixture: {proc.stderr or proc.stdout}")
            return "directory junction"
    sealed_case("HOSTILE-009-reparse-member", add_reparse)

    baseline = run_validator(workspace, validator, canonical)
    cases.append({"case_id": "CONTROL-001-canonical-baseline", "expected": "accept", "result": "PASS" if baseline.returncode == 0 else "FAIL", "returncode": baseline.returncode, "stdout": baseline.stdout.strip()[-1000:], "stderr": baseline.stderr.strip()[-1000:]})

    after = {p.name: digest(p) for p in canonical.iterdir() if p.is_file()}
    no_write = watch == after
    cases.append({"case_id": "CONTROL-002-canonical-no-write", "expected": "accept", "result": "PASS" if no_write else "FAIL", "returncode": 0 if no_write else 1, "stdout": "canonical files unchanged" if no_write else "canonical file hash/mtime drift", "stderr": ""})

    failed = [row for row in cases if row["result"] != "PASS"]
    print(json.dumps({"status": "PASS" if not failed else "FAIL", "cases": len(cases), "hostile_rejections": 9, "canonical_no_write": no_write, "results": cases}, ensure_ascii=False, sort_keys=True))
    return 0 if not failed else 1


if __name__ == "__main__":
    raise SystemExit(main())
