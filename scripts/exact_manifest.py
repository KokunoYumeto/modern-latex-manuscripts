#!/usr/bin/env python3
"""Build a deterministic path/bytes/SHA-256 manifest for one bounded root."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    root = args.root.resolve(strict=True)
    output = args.output.resolve()
    if output == root or root in output.parents:
        raise SystemExit("output must be outside the inventoried root")

    rows: list[tuple[str, int, str]] = []
    for path in sorted(
        (path for path in root.rglob("*") if path.is_file()),
        key=lambda path: path.relative_to(root).as_posix(),
    ):
        data = path.read_bytes()
        rows.append((path.relative_to(root).as_posix(), len(data), sha256(data)))

    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(("relative_path", "bytes", "sha256"))
        writer.writerows(rows)

    canonical = "\n".join(
        f"{relative_path}\t{size}\t{digest}"
        for relative_path, size, digest in rows
    ).encode("utf-8")
    output_data = output.read_bytes()
    print(
        json.dumps(
            {
                "files": len(rows),
                "bytes": sum(size for _, size, _ in rows),
                "canonical_stream_bytes": len(canonical),
                "tree_sha256": sha256(canonical),
                "manifest_bytes": len(output_data),
                "manifest_sha256": sha256(output_data),
                "output": str(output),
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
