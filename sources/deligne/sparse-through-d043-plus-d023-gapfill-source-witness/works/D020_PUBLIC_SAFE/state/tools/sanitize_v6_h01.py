#!/usr/bin/env python3
"""Apply the two exact text-file H01 repairs in D020 V6."""
from __future__ import annotations

import hashlib
import json
import os
import pathlib
import re


ROOT = pathlib.Path(__file__).resolve().parent.parent


def sha256(path: pathlib.Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb", buffering=0) as handle:
        while True:
            block = handle.read(64 * 1024)
            if not block:
                break
            digest.update(block)
    return digest.hexdigest().upper()


def atomic_text(path: pathlib.Path, text: str) -> None:
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(text, encoding="utf-8", newline="\n")
    os.replace(temporary, path)


def file_identity(path: pathlib.Path) -> dict:
    return {
        "path": path.relative_to(ROOT).as_posix(),
        "bytes": path.stat().st_size,
        "sha256": sha256(path),
    }


def main() -> int:
    profile = str(pathlib.Path.home())
    postbuild = ROOT / "audit" / "V5_POSTBUILD_VERIFICATION.json"
    control = ROOT / "control" / "ZENODO_D020_ID.md"
    if not postbuild.is_file() or not control.is_file():
        raise RuntimeError("an exact H01 text target is absent")

    before = [file_identity(postbuild), file_identity(control)]
    payload = json.loads(postbuild.read_text(encoding="utf-8"))
    command = payload["production_invocation"]["command"]
    if command.casefold().count(profile.casefold()) != 1 or not command.casefold().startswith((profile + "\\").casefold()):
        raise RuntimeError("postbuild command does not have the expected single local-profile prefix")
    payload["production_invocation"]["command"] = "%USERPROFILE%" + command[len(profile) :]
    atomic_text(postbuild, json.dumps(payload, indent=2, ensure_ascii=False) + "\n")

    control_text = control.read_text(encoding="utf-8")
    if len(re.findall(re.escape(profile), control_text, flags=re.I)) != 4:
        raise RuntimeError("control note does not have the expected four local-profile prefixes")
    control_text = re.sub(re.escape(profile), "%USERPROFILE%", control_text, flags=re.I)
    atomic_text(control, control_text)

    after = [file_identity(postbuild), file_identity(control)]
    for path in (postbuild, control):
        if profile.casefold() in path.read_text(encoding="utf-8").casefold():
            raise RuntimeError("local-profile name remains after sanitation")

    receipt = {
        "schema": "D020_V6_H01_TEXT_SANITIZATION_RECEIPT_V1",
        "status": "PASS",
        "scope": ["audit/V5_POSTBUILD_VERIFICATION.json", "control/ZENODO_D020_ID.md"],
        "replacement": "local profile prefix -> %USERPROFILE%",
        "occurrences_replaced": {
            "audit/V5_POSTBUILD_VERIFICATION.json": 1,
            "control/ZENODO_D020_ID.md": 4,
        },
        "before": before,
        "after": after,
        "other_files_modified": False,
    }
    receipt_path = ROOT / "audit" / "V6_H01_TEXT_SANITIZATION_RECEIPT.json"
    atomic_text(receipt_path, json.dumps(receipt, indent=2, ensure_ascii=False) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
