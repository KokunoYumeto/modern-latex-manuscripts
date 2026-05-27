#!/usr/bin/env python3
"""CRC-test a folder of ZIP files and write manifest reports.

This is intentionally boring and strict: every ZIP is opened with Python's
zipfile module and testzip() is run, which reads entries and checks CRCs.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from zipfile import BadZipFile, ZipFile


def sha256_file(path: Path, chunk_size: int = 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while True:
            chunk = handle.read(chunk_size)
            if not chunk:
                break
            digest.update(chunk)
    return digest.hexdigest()


def test_zip(path: Path) -> dict[str, object]:
    started = time.monotonic()
    row: dict[str, object] = {
        "name": path.name,
        "path": str(path),
        "bytes": path.stat().st_size,
        "sha256": "",
        "entry_count": 0,
        "status": "ERROR",
        "bad_entry": "",
        "error": "",
        "elapsed_seconds": 0.0,
    }
    try:
        row["sha256"] = sha256_file(path)
        with ZipFile(path, "r") as archive:
            row["entry_count"] = len(archive.infolist())
            bad = archive.testzip()
            if bad is None:
                row["status"] = "OK"
            else:
                row["status"] = "BAD_ENTRY"
                row["bad_entry"] = bad
    except BadZipFile as exc:
        row["status"] = "BAD_ZIP"
        row["error"] = str(exc)
    except Exception as exc:  # noqa: BLE001 - manifest should capture any failure
        row["status"] = "ERROR"
        row["error"] = f"{type(exc).__name__}: {exc}"
    finally:
        row["elapsed_seconds"] = round(time.monotonic() - started, 3)
    return row


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("folder", type=Path)
    parser.add_argument("--out-dir", type=Path, required=True)
    parser.add_argument("--prefix", default="web_source_zip_integrity")
    args = parser.parse_args()

    folder = args.folder.resolve()
    out_dir = args.out_dir.resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")

    zips = sorted(folder.glob("*.zip"), key=lambda p: p.name)
    rows = [test_zip(path) for path in zips]

    csv_path = out_dir / f"{args.prefix}_{timestamp}.csv"
    json_path = out_dir / f"{args.prefix}_{timestamp}_summary.json"

    fieldnames = [
        "name",
        "path",
        "bytes",
        "sha256",
        "entry_count",
        "status",
        "bad_entry",
        "error",
        "elapsed_seconds",
    ]
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    status_counts: dict[str, int] = {}
    for row in rows:
        status = str(row["status"])
        status_counts[status] = status_counts.get(status, 0) + 1

    summary = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "folder": str(folder),
        "zip_count": len(rows),
        "total_bytes": sum(int(row["bytes"]) for row in rows),
        "status_counts": status_counts,
        "bad_files": [row for row in rows if row["status"] != "OK"],
        "csv": str(csv_path),
        "summary_json": str(json_path),
    }
    json_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))
    return 0 if not summary["bad_files"] else 2


if __name__ == "__main__":
    sys.exit(main())
