#!/usr/bin/env python3
"""Generate the deterministic non-self P08 producer manifest."""

from __future__ import annotations

import csv
from hashlib import sha256
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "manifest.csv"


def main() -> int:
    if OUT.exists():
        raise RuntimeError(f"Refusing to overwrite manifest: {OUT}")
    paths = sorted(
        (
            path
            for path in ROOT.rglob("*")
            if path.is_file() and path != OUT and "__pycache__" not in path.parts
        ),
        key=lambda path: path.relative_to(ROOT).as_posix(),
    )
    with OUT.open("x", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(["sha256", "bytes", "path"])
        for path in paths:
            data = path.read_bytes()
            writer.writerow(
                [
                    sha256(data).hexdigest().upper(),
                    len(data),
                    path.relative_to(ROOT).as_posix(),
                ]
            )
    data = OUT.read_bytes()
    print(
        f"entries={len(paths)} bytes={len(data)} "
        f"sha256={sha256(data).hexdigest().upper()}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
