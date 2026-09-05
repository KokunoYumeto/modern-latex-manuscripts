#!/usr/bin/env python3
"""Freeze the V4 repair as a new immutable cold-audit subject."""
import hashlib
import json
import pathlib
import shutil
import sys


root = pathlib.Path(sys.argv[1]).resolve()
destination = pathlib.Path(sys.argv[2]).resolve()
assert root.name == "S06_math_v4"
assert destination.name == "S06_math_v4_01"
assert not destination.exists(), "Audit subject must be new"
destination.mkdir(parents=True)
subject = destination / "state"
subject.mkdir()
(destination / "evidence").mkdir()
rows = []
for path in sorted(root.rglob("*")):
    relative = path.relative_to(root)
    if not path.is_file() or relative.parts[:2] == ("audit", "native_reader_qa"):
        continue
    assert "__pycache__" not in relative.parts and path.suffix not in (".pyc", ".pyo")
    target = subject / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(path, target)
    data = path.read_bytes()
    assert target.read_bytes() == data
    rows.append(
        {
            "path": relative.as_posix(),
            "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest().upper(),
        }
    )
manifest = {
    "schema": "d020-immutable-cold-subject-v2",
    "status": "IN_PROGRESS",
    "source_workspace": str(root),
    "subject": str(subject),
    "exclusion": "Derived native PNG cache only; independent auditor must render fresh images.",
    "files": rows,
}
manifest_path = destination / "SUBJECT_MANIFEST.json"
manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(
    json.dumps(
        {
            "subject": str(subject),
            "files": len(rows),
            "bytes": sum(row["bytes"] for row in rows),
            "manifest_sha256": hashlib.sha256(manifest_path.read_bytes()).hexdigest().upper(),
        }
    )
)
