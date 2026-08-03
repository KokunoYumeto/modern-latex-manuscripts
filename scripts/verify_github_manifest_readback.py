#!/usr/bin/env python3
"""Verify anonymous GitHub raw bytes against a CSV identity manifest."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repository", required=True)
    parser.add_argument("--commit", required=True)
    parser.add_argument("--base-path", required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--bytes-column", default="public_bytes")
    parser.add_argument("--sha256-column", default="public_sha256")
    args = parser.parse_args()

    with args.manifest.open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream))
    errors: list[str] = []
    files: dict[str, dict[str, object]] = {}
    for index, row in enumerate(rows, 1):
        relative = row["relative_path"]
        expected_bytes = int(row[args.bytes_column])
        expected_sha256 = row[args.sha256_column].upper()
        encoded = "/".join(urllib.parse.quote(part, safe="") for part in relative.split("/"))
        base = args.base_path.strip("/")
        url = (
            f"https://raw.githubusercontent.com/{args.repository}/{args.commit}/"
            f"{base}/{encoded}"
        )
        print(f"READBACK {index}/{len(rows)} {relative}", flush=True)
        try:
            request = urllib.request.Request(url, headers={"User-Agent": "archive-readback"})
            with urllib.request.urlopen(request, timeout=90) as response:
                data = response.read()
        except Exception as error:  # noqa: BLE001 - receipt needs exact network error
            errors.append(f"{relative}: {type(error).__name__}: {error}")
            files[relative] = {
                "expected_bytes": expected_bytes,
                "expected_sha256": expected_sha256,
                "url": url,
                "error": f"{type(error).__name__}: {error}",
                "match": False,
            }
            continue
        digest = sha256_bytes(data)
        match = len(data) == expected_bytes and digest == expected_sha256
        if not match:
            errors.append(
                f"{relative}: expected {expected_bytes}/{expected_sha256}, "
                f"received {len(data)}/{digest}"
            )
        files[relative] = {
            "expected_bytes": expected_bytes,
            "expected_sha256": expected_sha256,
            "public_bytes": len(data),
            "public_sha256": digest,
            "url": url,
            "match": match,
        }

    receipt = {
        "schema": "github-manifest-readback-v1",
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "checked_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "repository": args.repository,
        "commit": args.commit,
        "base_path": args.base_path.strip("/"),
        "manifest": args.manifest.as_posix(),
        "manifest_bytes": args.manifest.stat().st_size,
        "manifest_sha256": sha256_bytes(args.manifest.read_bytes()),
        "file_count": len(rows),
        "matched_file_count": sum(bool(item.get("match")) for item in files.values()),
        "expected_total_bytes": sum(int(row[args.bytes_column]) for row in rows),
        "public_total_bytes": sum(int(item.get("public_bytes", 0)) for item in files.values()),
        "files": files,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(receipt, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(
        json.dumps(
            {
                "status": receipt["status"],
                "files": receipt["file_count"],
                "matches": receipt["matched_file_count"],
                "output": args.output.as_posix(),
            },
            indent=2,
        )
    )
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
