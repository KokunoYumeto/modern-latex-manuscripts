#!/usr/bin/env python3
"""Split the combined SGA3 XX/XXI GitHub readback into durable receipts."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


REPOSITORY = "KokunoYumeto/modern-latex-manuscripts"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("combined_receipt", type=Path)
    parser.add_argument("outer_receipt", type=Path)
    parser.add_argument("zip_receipt", type=Path)
    args = parser.parse_args()

    combined = json.loads(args.combined_receipt.read_text(encoding="utf-8"))
    commit = combined["commit"]
    packages = combined["packages"]
    errors = list(combined.get("errors", []))

    outer_files: dict[str, dict[str, object]] = {}
    zip_rows: dict[str, dict[str, object]] = {}
    total_members = 0
    total_uncompressed = 0

    for package_path, package in packages.items():
        errors.extend(package.get("errors", []))
        for relative_name, row in package["files"].items():
            full_path = f"{package_path}/{relative_name}"
            outer_files[full_path] = {
                "bytes": row["bytes"],
                "sha256": row["sha256"],
                "url": row["url"],
                "match": row["exact"],
            }

        zip_names = [
            name for name in package["files"] if name.lower().endswith(".zip")
        ]
        if len(zip_names) != 1:
            errors.append(
                f"{package_path}: expected one ZIP outer file, found {len(zip_names)}"
            )
            continue

        zip_name = zip_names[0]
        zip_file = package["files"][zip_name]
        summary = package["zip_summary"]
        members = {
            name: {
                "bytes": row["bytes"],
                "sha256": row["sha256"],
                "match": True,
            }
            for name, row in package["zip_members"].items()
        }
        member_count = len(members)
        if member_count != summary["members"]:
            errors.append(
                f"{package_path}: ZIP member count {member_count} != "
                f"{summary['members']}"
            )
        if summary.get("crc_error"):
            errors.append(
                f"{package_path}: ZIP CRC error {summary['crc_error']}"
            )

        full_zip_path = f"{package_path}/{zip_name}"
        zip_rows[full_zip_path] = {
            "status": "PASS" if not summary.get("crc_error") else "FAIL",
            "errors": [] if not summary.get("crc_error") else [summary["crc_error"]],
            "zip_bytes": zip_file["bytes"],
            "zip_sha256": zip_file["sha256"],
            "members": member_count,
            "file_members": member_count,
            "uncompressed_bytes": summary["uncompressed_bytes"],
            "member_rows": members,
        }
        total_members += member_count
        total_uncompressed += summary["uncompressed_bytes"]

    outer = {
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "repository": REPOSITORY,
        "commit": commit,
        "comparison_basis": "remote raw bytes versus exact local package bytes",
        "changed_file_count": len(outer_files),
        "read_back_count": sum(1 for row in outer_files.values() if row["match"]),
        "files": outer_files,
    }
    zipped = {
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "repository": REPOSITORY,
        "commit": commit,
        "zip_count": len(zip_rows),
        "zip_file_members": total_members,
        "zip_uncompressed_bytes": total_uncompressed,
        "zips": zip_rows,
    }

    args.outer_receipt.parent.mkdir(parents=True, exist_ok=True)
    args.zip_receipt.parent.mkdir(parents=True, exist_ok=True)
    args.outer_receipt.write_text(
        json.dumps(outer, ensure_ascii=True, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    args.zip_receipt.write_text(
        json.dumps(zipped, ensure_ascii=True, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )

    print(
        json.dumps(
            {
                "status": outer["status"],
                "outer_files": len(outer_files),
                "zip_count": len(zip_rows),
                "zip_members": total_members,
                "zip_uncompressed_bytes": total_uncompressed,
                "outer_receipt_sha256": sha256(args.outer_receipt),
                "zip_receipt_sha256": sha256(args.zip_receipt),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
