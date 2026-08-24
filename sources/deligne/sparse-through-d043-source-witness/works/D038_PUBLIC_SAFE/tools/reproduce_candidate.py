#!/usr/bin/env python3
"""Regenerate the D038 candidate twice and prove byte reproducibility."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import pathlib
import subprocess
import sys


EXPECTED_TEX = (
    "D038_SOURCE_LANGUAGE_CANONICAL.tex",
    "D038_ENGLISH_CANONICAL.tex",
    "D038_RESTRAINED_APPARATUS.tex",
)


def sha256_file(path: pathlib.Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def inventory(candidate: pathlib.Path) -> list[dict[str, object]]:
    rows = []
    for path in sorted((item for item in candidate.rglob("*") if item.is_file()), key=lambda p: p.as_posix()):
        rows.append(
            {
                "path": path.relative_to(candidate).as_posix(),
                "bytes": path.stat().st_size,
                "sha256": sha256_file(path),
            }
        )
    return rows


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True, type=pathlib.Path)
    args = parser.parse_args()
    root = args.root.resolve()
    candidate = root / "candidate"
    generator = root / "tools/build_canonical.py"
    command = [sys.executable, str(generator), "--root", str(root)]

    run_receipts = []
    snapshots = []
    for run in ("A", "B"):
        result = subprocess.run(
            command,
            cwd=root,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            encoding="utf-8",
            errors="replace",
            check=False,
        )
        require(result.returncode == 0, f"normalization run {run} failed:\n{result.stdout}")
        require("PASS_GENERATION" in result.stdout, f"normalization run {run} lacks PASS token")
        rows = inventory(candidate)
        require(len(rows) == 63, f"normalization run {run} candidate file count is {len(rows)}, expected 63")
        paths = {row["path"] for row in rows}
        expected_paths = set(EXPECTED_TEX) | {"CONTENT_MAP.tsv", "IMAGE_FALLBACK_MANIFEST.tsv"} | {
            f"assets/authority_pages/p{page:03d}.png" for page in range(1, 59)
        }
        require(paths == expected_paths, f"normalization run {run} candidate inventory mismatch")
        for name in EXPECTED_TEX:
            text = (candidate / name).read_text(encoding="utf-8")
            require(text.count("% CANONICAL_PAGE ") == 58, f"{name} canonical marker count mismatch")
            require(text.count("Layout/math fallback asset") == 58, f"{name} fallback disclosure count mismatch")
            require(text.count(r"assets/authority\_pages/p") == 58, f"{name} fallback reference count mismatch")
        with (candidate / "CONTENT_MAP.tsv").open(encoding="utf-8", newline="") as stream:
            content_rows = list(csv.DictReader(stream, delimiter="\t"))
        with (candidate / "IMAGE_FALLBACK_MANIFEST.tsv").open(encoding="utf-8", newline="") as stream:
            fallback_rows = list(csv.DictReader(stream, delimiter="\t"))
        require(len(content_rows) == 174, "content-map row count mismatch")
        require(len(fallback_rows) == 58, "fallback-manifest row count mismatch")
        require(all(row["status"] == "VERIFIED_FROM_PACKET" for row in content_rows), "content-map status mismatch")
        require(all(row["role"] == "AUTHORITY_LAYOUT_MATH_IMAGE_FALLBACK" for row in fallback_rows), "fallback role mismatch")
        require(all(row["accepted_editorial_bytes"] == "0" for row in fallback_rows), "fallback editorial-byte boundary mismatch")
        snapshots.append(rows)
        run_receipts.append(
            {
                "run": run,
                "stdout": result.stdout.strip(),
                "candidate_files": len(rows),
                "candidate_aggregate_sha256": hashlib.sha256(
                    "\n".join(f"{row['path']}\t{row['bytes']}\t{row['sha256']}" for row in rows).encode("utf-8")
                ).hexdigest().upper(),
                "generation_receipt_sha256": sha256_file(root / "manifests/GENERATION_RECEIPT.json"),
            }
        )

    require(snapshots[0] == snapshots[1], "normalization run A/B candidate bytes differ")
    manifest = root / "manifests/CANDIDATE_MANIFEST.tsv"
    with manifest.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=("path", "bytes", "sha256"), delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(snapshots[1])

    packet_receipt = root / "state/PACKET_INTEGRITY.json"
    receipt = {
        "schema": "d038-normalization-reproducibility-v1",
        "status": "PASS",
        "method": "PACKET_ONLY_FRESH_GENERATION_TWICE",
        "inherited_exact_work": "ZERO_ACCEPTED",
        "generator": {
            "path": generator.relative_to(root).as_posix(),
            "bytes": generator.stat().st_size,
            "sha256": sha256_file(generator),
        },
        "packet_integrity_receipt_sha256": sha256_file(packet_receipt),
        "runs": run_receipts,
        "candidate_file_count": len(snapshots[1]),
        "candidate_manifest": {
            "path": manifest.relative_to(root).as_posix(),
            "bytes": manifest.stat().st_size,
            "sha256": sha256_file(manifest),
        },
        "candidate_ab_byte_identity": True,
    }
    output = root / "manifests/NORMALIZATION_REPRODUCIBILITY.json"
    output.write_text(
        json.dumps(receipt, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print("PASS_NORMALIZATION_REPRODUCIBILITY")


if __name__ == "__main__":
    main()
