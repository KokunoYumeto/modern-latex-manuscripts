#!/usr/bin/env python3
"""Freeze the exact D038 candidate inventory without modifying candidate bytes."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import pathlib


def sha256(path: pathlib.Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True, type=pathlib.Path)
    args = parser.parse_args()
    root = args.root.resolve()
    candidate = root / "candidate"
    expected = {
        "CONTENT_MAP.tsv",
        "IMAGE_FALLBACK_MANIFEST.tsv",
        "D038_SOURCE_LANGUAGE_CANONICAL.tex",
        "D038_ENGLISH_CANONICAL.tex",
        "D038_RESTRAINED_APPARATUS.tex",
        "D038_SOURCE_LANGUAGE_CANONICAL.pdf",
        "D038_ENGLISH_CANONICAL.pdf",
        "D038_RESTRAINED_APPARATUS.pdf",
    } | {f"assets/authority_pages/p{page:03d}.png" for page in range(1, 59)}
    files = sorted((p for p in candidate.rglob("*") if p.is_file()), key=lambda p: p.as_posix())
    paths = {p.relative_to(candidate).as_posix() for p in files}
    if paths != expected:
        raise RuntimeError(f"candidate inventory mismatch: missing={sorted(expected-paths)}, extra={sorted(paths-expected)}")
    rows = [
        {
            "path": p.relative_to(root).as_posix(),
            "bytes": p.stat().st_size,
            "sha256": sha256(p),
        }
        for p in files
    ]
    manifest = root / "manifests/FROZEN_CANDIDATE_MANIFEST.tsv"
    with manifest.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=("path", "bytes", "sha256"), delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    aggregate = hashlib.sha256(
        "\n".join(f"{row['path']}\t{row['bytes']}\t{row['sha256']}" for row in rows).encode("utf-8")
    ).hexdigest().upper()
    receipt = {
        "schema": "d038-frozen-candidate-v1",
        "status": "FROZEN",
        "candidate_files": len(rows),
        "candidate_bytes": sum(int(row["bytes"]) for row in rows),
        "candidate_aggregate_sha256": aggregate,
        "manifest": {
            "path": manifest.relative_to(root).as_posix(),
            "bytes": manifest.stat().st_size,
            "sha256": sha256(manifest),
        },
        "candidate_mutation_after_freeze_permitted": False,
    }
    output = root / "manifests/FREEZE_RECEIPT.json"
    output.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    print("PASS_CANDIDATE_FREEZE", aggregate)


if __name__ == "__main__":
    main()
