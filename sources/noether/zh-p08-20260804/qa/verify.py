#!/usr/bin/env python3
"""Replay the deterministic P08 producer manifest without writing files."""

from __future__ import annotations

import csv
from hashlib import sha256
import json
from pathlib import Path, PurePosixPath


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "manifest.csv"


def main() -> int:
    failures: list[dict[str, object]] = []
    seen: set[str] = set()
    with MANIFEST.open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    for index, row in enumerate(rows, start=2):
        relative = row.get("path", "")
        pure = PurePosixPath(relative)
        if not relative or pure.is_absolute() or ".." in pure.parts or relative in seen:
            failures.append({"line": index, "path": relative, "reason": "unsafe_or_duplicate"})
            continue
        seen.add(relative)
        path = ROOT.joinpath(*pure.parts)
        if not path.is_file():
            failures.append({"line": index, "path": relative, "reason": "missing"})
            continue
        data = path.read_bytes()
        observed = {"bytes": len(data), "sha256": sha256(data).hexdigest().upper()}
        expected = {"bytes": int(row["bytes"]), "sha256": row["sha256"]}
        if observed != expected:
            failures.append(
                {
                    "line": index,
                    "path": relative,
                    "reason": "identity",
                    "expected": expected,
                    "observed": observed,
                }
            )
    all_files = {
        path.relative_to(ROOT).as_posix()
        for path in ROOT.rglob("*")
        if path.is_file() and path != MANIFEST and "__pycache__" not in path.parts
    }
    missing_from_manifest = sorted(all_files - seen)
    extra_in_manifest = sorted(seen - all_files)
    result = {
        "manifest": str(MANIFEST),
        "manifest_bytes": MANIFEST.stat().st_size,
        "manifest_sha256": sha256(MANIFEST.read_bytes()).hexdigest().upper(),
        "entries": len(rows),
        "unique_paths": len(seen),
        "non_self_files": len(all_files),
        "failures": failures,
        "missing_from_manifest": missing_from_manifest,
        "extra_in_manifest": extra_in_manifest,
        "all_pass": not failures and not missing_from_manifest and not extra_in_manifest,
    }
    print(json.dumps(result, ensure_ascii=True, indent=2))
    return 0 if result["all_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
