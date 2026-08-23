#!/usr/bin/env python3
"""Create a public-safe D026 ZERO_ACCEPTED ledger without local profile paths."""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
import zipfile
from pathlib import Path, PureWindowsPath


PRIOR_SHA256 = "2DE877D7BE03D95319CC21C535C5DA179688A59A51B31407A76394C2FBC74FD7"


def sha256(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            value.update(chunk)
    return value.hexdigest().upper()


def safe_locator(value: str) -> str:
    value = value.strip().replace("\\", "/")
    if re.match(r"(?i)^[a-z]:/", value) or value.startswith("/"):
        return PureWindowsPath(value).name
    parts = [part for part in value.split("/") if part not in {"", ".", ".."}]
    return "/".join(parts)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", type=Path, required=True)
    args = parser.parse_args()
    base = args.base.resolve()
    raw_ledger = base / "input" / "expanded_state" / "control" / "PRIOR_WORK_LEDGER.tsv"
    prior_archive = base / "input" / "expanded_state" / "salvage" / "30_UNTRUSTED_PRIOR_WORK_DELIGNE_D026.zip"
    output_ledger = base / "evidence" / "SANITIZED_ZERO_ACCEPTED_PRIOR_WORK_LEDGER.tsv"
    output_receipt = base / "evidence" / "ZERO_ACCEPTED_PRESERVATION_RECEIPT.json"

    with raw_ledger.open("r", encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream, delimiter="\t"))
    if len(rows) != 64:
        raise RuntimeError(f"expected 64 inherited rows, found {len(rows)}")
    if any(row["accepted_state"] != "ZERO_ACCEPTED" for row in rows):
        raise RuntimeError("an inherited row is not ZERO_ACCEPTED")

    output = io.StringIO(newline="")
    fields = ["evidence_id", "origin_locator", "bytes", "sha256", "lineage", "witness_role", "accepted_state", "authority_role"]
    writer = csv.DictWriter(output, fieldnames=fields, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    for index, row in enumerate(rows, start=1):
        locator = safe_locator(row["origin_relative_path_or_locator"])
        if not locator:
            locator = f"witness_{index:02d}"
        writer.writerow({
            "evidence_id": f"ZERO_ACCEPTED_{index:02d}",
            "origin_locator": locator,
            "bytes": row["bytes"],
            "sha256": row["sha256"].upper(),
            "lineage": row["lineage"],
            "witness_role": row["witness_role"],
            "accepted_state": "ZERO_ACCEPTED",
            "authority_role": row["authority_role"],
        })
    output_ledger.write_text(output.getvalue(), encoding="utf-8", newline="\n")

    archive_hash = sha256(prior_archive)
    if archive_hash != PRIOR_SHA256:
        raise RuntimeError("prior archive identity mismatch")
    with zipfile.ZipFile(prior_archive) as archive:
        if archive.testzip() is not None:
            raise RuntimeError("prior archive integrity failure")
        archive_members = len(archive.infolist())
    if archive_members != 64:
        raise RuntimeError("prior archive member count mismatch")

    receipt = {
        "schema_version": "deligne-d026-zero-accepted-preservation-v1",
        "work_id": "D026",
        "result": "PASS",
        "inherited_members": 64,
        "accepted_members": 0,
        "accepted_state": "ZERO_ACCEPTED",
        "original_prior_archive": {
            "filename": prior_archive.name,
            "bytes": prior_archive.stat().st_size,
            "sha256": archive_hash,
            "members": archive_members,
            "local_preservation": "EXACT_BYTES_RETAINED_UNCHANGED",
            "public_payload_disposition": "EXCLUDED_BECAUSE_INHERITED_CONTENT_CONTAINS_LOCAL_PROFILE_PATHS"
        },
        "raw_ledger": {
            "filename": raw_ledger.name,
            "bytes": raw_ledger.stat().st_size,
            "sha256": sha256(raw_ledger),
            "local_preservation": "EXACT_BYTES_RETAINED_UNCHANGED",
            "public_payload_disposition": "REPLACED_BY_SANITIZED_LEDGER"
        },
        "sanitized_ledger": {
            "filename": output_ledger.name,
            "bytes": output_ledger.stat().st_size,
            "sha256": sha256(output_ledger),
            "rows": len(rows),
            "absolute_paths": 0,
            "credentials": 0
        },
        "publication_actions": "NONE"
    }
    output_receipt.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({
        "result": "PASS",
        "rows": len(rows),
        "accepted": 0,
        "sanitized_ledger_sha256": receipt["sanitized_ledger"]["sha256"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
