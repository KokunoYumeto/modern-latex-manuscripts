#!/usr/bin/env python3
"""Verify anonymous GitHub bytes for a Zenodo JSON upload manifest."""

from __future__ import annotations

import argparse
import hashlib
import json
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def raw_url(repository: str, commit: str, relative: str) -> str:
    encoded = "/".join(
        urllib.parse.quote(part, safe="") for part in relative.split("/")
    )
    return f"https://raw.githubusercontent.com/{repository}/{commit}/{encoded}"


def local_identity(path: Path) -> tuple[int, str]:
    data = path.read_bytes()
    return len(data), sha256_bytes(data)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--repository", default="KokunoYumeto/modern-latex-manuscripts"
    )
    parser.add_argument("--commit", required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--extra-path", action="append", default=[])
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    manifest = args.manifest.resolve()
    document = json.loads(manifest.read_text(encoding="utf-8"))
    rows = document.get("files") if isinstance(document, dict) else None
    if not isinstance(rows, list) or not rows:
        raise RuntimeError("Upload manifest has no file rows")
    expected: dict[str, dict[str, Any]] = {}
    for row in rows:
        local = (manifest.parent / str(row["path"])).resolve()
        try:
            relative = local.relative_to(REPO_ROOT).as_posix()
        except ValueError as error:
            raise RuntimeError(f"Manifest local path escaped repository: {local}") from error
        observed = local_identity(local)
        wanted = (int(row["bytes"]), str(row["sha256"]).upper())
        if observed != wanted:
            raise RuntimeError(f"Local manifest identity changed: {relative}")
        expected[relative] = {
            "manifest_name": str(row["name"]),
            "expected_bytes": wanted[0],
            "expected_sha256": wanted[1],
            "source": "upload_manifest",
        }
    for value in args.extra_path:
        local = (REPO_ROOT / value).resolve()
        try:
            relative = local.relative_to(REPO_ROOT).as_posix()
        except ValueError as error:
            raise RuntimeError(f"Extra path escaped repository: {local}") from error
        size, digest = local_identity(local)
        expected.setdefault(
            relative,
            {
                "manifest_name": None,
                "expected_bytes": size,
                "expected_sha256": digest,
                "source": "extra_release_control",
            },
        )

    errors: list[str] = []
    results: dict[str, dict[str, Any]] = {}
    for ordinal, relative in enumerate(sorted(expected), 1):
        wanted = expected[relative]
        url = raw_url(args.repository, args.commit, relative)
        print(f"READBACK {ordinal}/{len(expected)} {relative}", flush=True)
        try:
            request = urllib.request.Request(
                url, headers={"User-Agent": "archive-upload-manifest-readback/1.0"}
            )
            with urllib.request.urlopen(request, timeout=120) as response:
                data = response.read()
            observed = (len(data), sha256_bytes(data))
            match = observed == (
                wanted["expected_bytes"],
                wanted["expected_sha256"],
            )
            if not match:
                errors.append(
                    f"{relative}: expected {wanted['expected_bytes']}/"
                    f"{wanted['expected_sha256']}, received {observed[0]}/{observed[1]}"
                )
            results[relative] = {
                **wanted,
                "public_bytes": observed[0],
                "public_sha256": observed[1],
                "url": url,
                "match": match,
            }
        except Exception as error:  # noqa: BLE001 - receipt records exact failure
            errors.append(f"{relative}: {type(error).__name__}: {error}")
            results[relative] = {
                **wanted,
                "url": url,
                "error": f"{type(error).__name__}: {error}",
                "match": False,
            }

    receipt = {
        "schema": "github-upload-manifest-readback-v1",
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "checked_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "repository": args.repository,
        "commit": args.commit,
        "manifest": manifest.relative_to(REPO_ROOT).as_posix(),
        "manifest_bytes": manifest.stat().st_size,
        "manifest_sha256": sha256_bytes(manifest.read_bytes()),
        "file_count": len(results),
        "matched_file_count": sum(bool(row["match"]) for row in results.values()),
        "expected_total_bytes": sum(
            int(row["expected_bytes"]) for row in results.values()
        ),
        "public_total_bytes": sum(int(row.get("public_bytes", 0)) for row in results.values()),
        "files": results,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(receipt, ensure_ascii=True, sort_keys=True, indent=2) + "\n",
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
