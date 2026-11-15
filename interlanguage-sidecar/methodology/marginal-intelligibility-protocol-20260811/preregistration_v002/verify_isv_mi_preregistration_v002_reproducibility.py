#!/usr/bin/env python3
"""Rebuild preregistration-v002 core in isolation and compare exact bytes."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path


DEFAULT_WORKSPACE = Path(r"C:\Users\user\Documents\interlanguage")
PACKAGE_REL = Path("03_projects/language_management/slavic_interslavic/00_lane_control/marginal_intelligibility_20260811/preregistration_v002")
CORE = ["ISV_MI_PREREGISTRATION_V002.json", "ISV_MI_PREREGISTRATION_V002.schema.json", "INPUT_REPIN_AUDIT_V002.json", "STAGE0_DESIGN_V002.csv", "PROTOCOL_V002.md", "README.md", "HOSTILE_FIXTURES_V002.json"]


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workspace-root", type=Path, default=DEFAULT_WORKSPACE)
    parser.add_argument("--package-root", type=Path)
    args = parser.parse_args()
    workspace = args.workspace_root.resolve(strict=True)
    root = (args.package_root or workspace / PACKAGE_REL).resolve(strict=True)
    builder = root / "build_isv_mi_preregistration_v002.py"
    with tempfile.TemporaryDirectory(prefix="slisv-prereg2-repro-") as temp:
        out = Path(temp) / "rebuilt"
        proc = subprocess.run([sys.executable, str(builder), "--workspace-root", str(workspace), "--output-root", str(out), "--write"], check=False, capture_output=True, text=True, encoding="utf-8", timeout=120)
        comparisons = []
        for name in CORE:
            canonical = root / name
            rebuilt = out / name
            same = rebuilt.is_file() and canonical.read_bytes() == rebuilt.read_bytes()
            comparisons.append({"path": name, "identical": same, "canonical_sha256": sha(canonical), "rebuilt_sha256": sha(rebuilt) if rebuilt.is_file() else None})
        ok = proc.returncode == 0 and all(row["identical"] for row in comparisons)
    print(json.dumps({"status": "PASS" if ok else "FAIL", "builder_returncode": proc.returncode, "core_files": len(CORE), "identical_files": sum(row["identical"] for row in comparisons), "comparisons": comparisons, "stdout": proc.stdout.strip(), "stderr": proc.stderr.strip()}, sort_keys=True))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
