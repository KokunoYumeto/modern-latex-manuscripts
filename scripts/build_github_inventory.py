#!/usr/bin/env python3
"""Build an exact SHA256 inventory from Git's tracked and untracked file lists."""

from __future__ import annotations

import csv
import hashlib
import os
import subprocess
from pathlib import Path


OUTPUT = Path("manifests/github_file_inventory.csv")


def git_paths(*args: str) -> list[str]:
    raw = subprocess.check_output(["git", *args, "-z"])
    return [os.fsdecode(item) for item in raw.split(b"\0") if item]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> int:
    root = Path.cwd()
    paths = set(git_paths("ls-files"))
    paths.update(git_paths("ls-files", "--others", "--exclude-standard"))
    paths.discard(OUTPUT.as_posix())

    rows: list[tuple[str, int, str]] = []
    for relative in sorted(paths, key=str.casefold):
        path = root / relative
        if path.is_file():
            rows.append((relative.replace("\\", "/"), path.stat().st_size, sha256(path)))

    with OUTPUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(["path", "bytes", "sha256"])
        writer.writerows(rows)

    print(f"Wrote {len(rows)} files and {sum(row[1] for row in rows)} bytes to {OUTPUT}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
