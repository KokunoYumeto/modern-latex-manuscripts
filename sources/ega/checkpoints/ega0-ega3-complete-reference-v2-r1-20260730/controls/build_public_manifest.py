#!/usr/bin/env python3
"""Write a deterministic self-excluding manifest for a public package."""

from __future__ import annotations

import csv
import hashlib
import mimetypes
import sys
from pathlib import Path


OUTPUT_NAME = "ZENODO_PAYLOAD_MANIFEST.csv"


def file_sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def role(relpath: str) -> str:
    if relpath.startswith("readers/"):
        return "reader_pdf"
    if relpath.startswith("source/"):
        return "editable_source"
    if relpath.startswith("controls/"):
        return "machine_control"
    if relpath.startswith("metadata/"):
        return "credit_metadata"
    if relpath.endswith(".md"):
        return "documentation"
    return "package_file"


def main() -> int:
    if len(sys.argv) != 2:
        raise SystemExit("usage: build_public_manifest.py PACKAGE_ROOT")
    root = Path(sys.argv[1]).resolve()
    output = root / OUTPUT_NAME
    files = sorted(
        path for path in root.rglob("*")
        if path.is_file() and path != output
    )
    rows = []
    for path in files:
        relpath = path.relative_to(root).as_posix()
        media_type = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
        rows.append(
            {
                "relpath": relpath,
                "bytes": path.stat().st_size,
                "sha256": file_sha(path),
                "role": role(relpath),
                "media_type": media_type,
            }
        )
    with output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=("relpath", "bytes", "sha256", "role", "media_type"),
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)
    print(f"rows={len(rows)}")
    print(f"bytes={output.stat().st_size}")
    print(f"sha256={file_sha(output)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
