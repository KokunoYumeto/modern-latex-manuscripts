#!/usr/bin/env python3
"""Build an exact SHA256 inventory of blob bytes included in the Git index."""

from __future__ import annotations

import csv
import os
import subprocess
from pathlib import Path


OUTPUT = Path("manifests/github_file_inventory.csv")


def index_entries() -> list[tuple[str, str]]:
    raw = subprocess.check_output(["git", "ls-files", "--stage", "-z"])
    entries: list[tuple[str, str]] = []
    for item in raw.split(b"\0"):
        if not item:
            continue
        metadata, raw_path = item.split(b"\t", 1)
        _mode, object_id, stage = metadata.decode("ascii").split()
        if stage == "0":
            entries.append((os.fsdecode(raw_path), object_id))
    return entries


def blob_metadata(object_ids: list[str]) -> dict[str, tuple[int, str]]:
    """Return size and SHA256 for index blobs without checkout conversion."""
    import hashlib

    process = subprocess.Popen(
        ["git", "cat-file", "--batch"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
    )
    assert process.stdin is not None
    assert process.stdout is not None

    result: dict[str, tuple[int, str]] = {}
    for object_id in dict.fromkeys(object_ids):
        process.stdin.write(f"{object_id}\n".encode("ascii"))
        process.stdin.flush()
        header = process.stdout.readline().decode("ascii").strip().split()
        if len(header) != 3 or header[1] != "blob":
            raise RuntimeError(f"Unexpected cat-file response for {object_id}: {header}")
        size = int(header[2])
        remaining = size
        digest = hashlib.sha256()
        while remaining:
            block = process.stdout.read(min(1024 * 1024, remaining))
            if not block:
                raise RuntimeError(f"Unexpected EOF while reading {object_id}")
            digest.update(block)
            remaining -= len(block)
        if process.stdout.read(1) != b"\n":
            raise RuntimeError(f"Missing cat-file delimiter after {object_id}")
        result[object_id] = (size, digest.hexdigest())

    process.stdin.close()
    if process.wait() != 0:
        raise RuntimeError("git cat-file --batch failed")
    return result


def main() -> int:
    # Run after staging a release. Untracked work-in-progress files must not be
    # advertised by the public inventory before they are selected for commit.
    entries = [
        (path, object_id)
        for path, object_id in index_entries()
        if path.replace("\\", "/") != OUTPUT.as_posix()
    ]
    metadata = blob_metadata([object_id for _, object_id in entries])

    rows: list[tuple[str, int, str]] = []
    for relative, object_id in sorted(entries, key=lambda item: item[0].casefold()):
        size, digest = metadata[object_id]
        rows.append((relative.replace("\\", "/"), size, digest))

    with OUTPUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(["path", "bytes", "sha256"])
        writer.writerows(rows)

    print(f"Wrote {len(rows)} files and {sum(row[1] for row in rows)} bytes to {OUTPUT}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
