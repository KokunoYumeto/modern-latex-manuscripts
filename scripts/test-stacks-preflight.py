#!/usr/bin/env python3
"""Replay the empty Stacks preflight and prove bounded mutations fail closed."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
from typing import Any, Callable


TOOL = Path("scripts/stacks-preflight.py")
TEST = Path("scripts/test-stacks-preflight.py")
PIN = Path("manifests/stacks-pin.json")
REGISTRY = Path("manifests/stacks-overlay.json")
CONTRACT = Path("manifests/stacks-compose.json")
RESULT = Path("manifests/stacks-preflight.json")
ENTRY_SCHEMA = Path("manifests/stacks-entry.schema.json")
ENTRY_TOOL = Path("scripts/check-stacks-entry.py")
ENTRY_TEST = Path("scripts/test-stacks-entry.py")


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def run(root: Path, *, expect: bool = True) -> subprocess.CompletedProcess[bytes]:
    command = [sys.executable, str(root / TOOL), "--root", str(root)]
    if expect:
        command.extend(["--expect", "BLOCKED_EMPTY_OVERLAY_REGISTRY"])
    return subprocess.run(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
        timeout=30,
    )


def write_json(path: Path, value: Any) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def copy_fixture(source: Path, target: Path) -> None:
    for relative in (TOOL, TEST, PIN, REGISTRY, CONTRACT, ENTRY_SCHEMA, ENTRY_TOOL, ENTRY_TEST):
        destination = target / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source / relative, destination)


def bind_registry(root: Path) -> None:
    data = (root / REGISTRY).read_bytes()
    contract = json.loads((root / CONTRACT).read_text(encoding="utf-8"))
    contract["inputs"]["overlay_registry"]["bytes"] = len(data)
    contract["inputs"]["overlay_registry"]["sha256"] = sha256(data)
    write_json(root / CONTRACT, contract)


def bind_entry_contract(root: Path) -> None:
    registry = json.loads((root / REGISTRY).read_text(encoding="utf-8"))
    contract = json.loads((root / CONTRACT).read_text(encoding="utf-8"))
    entry = registry["entry_contract"]
    contract["inputs"]["candidate_entry_contract"] = {
        "state": entry["state"],
        "schema": entry["schema"],
        "validator": entry["validator"],
        "regression": entry["regression"],
        "candidate_manifests_accepted": entry["candidate_manifests_accepted"],
        "registered_entries": entry["registered_entries"],
        "content_bound": entry["content_bound"],
    }
    write_json(root / CONTRACT, contract)
    bind_registry(root)


def mutate_duplicate(root: Path) -> None:
    path = root / REGISTRY
    text = path.read_text(encoding="utf-8")
    path.write_text(text.replace('  "state":', '  "schema": "duplicate",\n  "state":', 1), encoding="utf-8", newline="\n")


def mutate_crlf(root: Path) -> None:
    path = root / REGISTRY
    path.write_bytes(path.read_bytes().replace(b"\n", b"\r\n"))


def mutate_tool_hash(root: Path) -> None:
    contract = json.loads((root / CONTRACT).read_text(encoding="utf-8"))
    contract["preflight_tool"]["sha256"] = "0" * 64
    write_json(root / CONTRACT, contract)


def mutate_test_hash(root: Path) -> None:
    contract = json.loads((root / CONTRACT).read_text(encoding="utf-8"))
    contract["regression"]["sha256"] = "0" * 64
    write_json(root / CONTRACT, contract)


def mutate_pin(root: Path) -> None:
    pin = json.loads((root / PIN).read_text(encoding="utf-8"))
    pin["pin"]["commit"] = "0" * 40
    write_json(root / PIN, pin)


def mutate_nonempty(root: Path) -> None:
    registry = json.loads((root / REGISTRY).read_text(encoding="utf-8"))
    registry["entries"] = [{}]
    registry["aggregate"]["registry_entries"] = 1
    write_json(root / REGISTRY, registry)
    bind_registry(root)


def mutate_numeric_bool(root: Path) -> None:
    registry = json.loads((root / REGISTRY).read_text(encoding="utf-8"))
    registry["boundaries"]["content_bearing_commons_overlay_bound"] = 0
    write_json(root / REGISTRY, registry)
    bind_registry(root)


def mutate_null_entries(root: Path) -> None:
    registry = json.loads((root / REGISTRY).read_text(encoding="utf-8"))
    registry["entries"] = None
    write_json(root / REGISTRY, registry)
    bind_registry(root)


def mutate_selection(root: Path) -> None:
    contract = json.loads((root / CONTRACT).read_text(encoding="utf-8"))
    contract["inputs"]["selected_overlay_id"] = "unapproved"
    write_json(root / CONTRACT, contract)


def mutate_entry_schema_identity(root: Path) -> None:
    registry = json.loads((root / REGISTRY).read_text(encoding="utf-8"))
    registry["entry_contract"]["schema"]["sha256"] = "0" * 64
    write_json(root / REGISTRY, registry)
    bind_entry_contract(root)


def mutate_entry_validator_identity(root: Path) -> None:
    registry = json.loads((root / REGISTRY).read_text(encoding="utf-8"))
    registry["entry_contract"]["validator"]["sha256"] = "0" * 64
    write_json(root / REGISTRY, registry)
    bind_entry_contract(root)


def mutate_entry_regression_identity(root: Path) -> None:
    registry = json.loads((root / REGISTRY).read_text(encoding="utf-8"))
    registry["entry_contract"]["regression"]["sha256"] = "0" * 64
    write_json(root / REGISTRY, registry)
    bind_entry_contract(root)


def mutate_entry_case_count(root: Path) -> None:
    registry = json.loads((root / REGISTRY).read_text(encoding="utf-8"))
    registry["entry_contract"]["regression"]["defined_cases"] = 33
    write_json(root / REGISTRY, registry)
    bind_entry_contract(root)


def mutate_entry_content_boundary(root: Path) -> None:
    registry = json.loads((root / REGISTRY).read_text(encoding="utf-8"))
    registry["entry_contract"]["content_bound"] = True
    write_json(root / REGISTRY, registry)
    bind_entry_contract(root)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".")
    args = parser.parse_args()
    source = Path(args.root).resolve(strict=True)

    valid = run(source)
    if valid.returncode != 0:
        raise RuntimeError(valid.stderr.decode("utf-8", errors="replace"))
    if valid.stderr:
        raise RuntimeError("valid preflight wrote unexpected stderr")
    if valid.stdout != (source / RESULT).read_bytes():
        raise RuntimeError("valid preflight output differs from the checked-in receipt")
    blocked = run(source, expect=False)
    if blocked.returncode != 20 or blocked.stdout != valid.stdout or blocked.stderr:
        raise RuntimeError("default invocation did not return the exact blocked result with exit 20")

    mutations: tuple[tuple[str, Callable[[Path], None]], ...] = (
        ("duplicate_json_key", mutate_duplicate),
        ("crlf_registry", mutate_crlf),
        ("tool_identity", mutate_tool_hash),
        ("regression_identity", mutate_test_hash),
        ("pin_identity", mutate_pin),
        ("nonempty_registry", mutate_nonempty),
        ("numeric_boolean", mutate_numeric_bool),
        ("null_entries", mutate_null_entries),
        ("unapproved_selection", mutate_selection),
        ("entry_schema_identity", mutate_entry_schema_identity),
        ("entry_validator_identity", mutate_entry_validator_identity),
        ("entry_regression_identity", mutate_entry_regression_identity),
        ("entry_case_count", mutate_entry_case_count),
        ("entry_content_boundary", mutate_entry_content_boundary),
    )
    rejected: list[str] = []
    for name, mutation in mutations:
        with tempfile.TemporaryDirectory(prefix="stacks-preflight-") as temporary:
            root = Path(temporary)
            copy_fixture(source, root)
            mutation(root)
            result = run(root)
            if result.returncode == 0:
                raise RuntimeError(f"mutation unexpectedly passed: {name}")
            if result.stdout:
                raise RuntimeError(f"failed mutation wrote stdout: {name}")
            diagnostic = json.loads(result.stderr.decode("utf-8"))
            if diagnostic.get("status") != "ERROR" or diagnostic.get("code") not in (10, 11, 12, 13, 14) or not diagnostic.get("error"):
                raise RuntimeError(f"mutation diagnostic is not fail-closed JSON: {name}")
            rejected.append(name)

    print(
        json.dumps(
            {
                "status": "PASS",
                "valid_cases": 2,
                "invalid_cases": len(mutations),
                "rejected": rejected,
                "network_queried": False,
                "composition_executed": False,
            },
            separators=(",", ":"),
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
