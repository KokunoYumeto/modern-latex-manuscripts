#!/usr/bin/env python3
"""Verify a Zenodo record and selected ZIP members against local controls."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import tempfile
import time
import urllib.error
import urllib.request
import zipfile
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--record-id", type=int, required=True)
    parser.add_argument("--concept-doi", required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--validation", type=Path, required=True)
    parser.add_argument("--new-zip-dir", type=Path, required=True)
    parser.add_argument("--new-zip", action="append", required=True)
    parser.add_argument("--output-prefix", type=Path, required=True)
    parser.add_argument("--expected-default-preview")
    return parser.parse_args()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def get_json(url: str) -> tuple[int, object | None]:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "modern-latex-manuscripts-public-readback/20260723"},
    )
    try:
        with urllib.request.urlopen(request, timeout=120) as response:
            return response.status, json.load(response)
    except urllib.error.HTTPError as error:
        return error.code, None


def stream_remote(
    url: str,
    destination: Path | None = None,
) -> tuple[int, str]:
    last_error: Exception | None = None
    for attempt in range(5):
        digest = hashlib.sha256()
        byte_count = 0
        try:
            request = urllib.request.Request(
                url,
                headers={
                    "User-Agent": (
                        "modern-latex-manuscripts-public-readback/20260723"
                    )
                },
            )
            output = destination.open("wb") if destination is not None else None
            try:
                with urllib.request.urlopen(request, timeout=1200) as response:
                    while chunk := response.read(1024 * 1024):
                        byte_count += len(chunk)
                        digest.update(chunk)
                        if output is not None:
                            output.write(chunk)
            finally:
                if output is not None:
                    output.close()
            return byte_count, digest.hexdigest().upper()
        except Exception as error:  # pragma: no cover - network retry path
            last_error = error
            if destination is not None:
                destination.unlink(missing_ok=True)
            if attempt < 4:
                time.sleep(min(20, 2 ** (attempt + 1)))
    assert last_error is not None
    raise last_error


def unsafe_zip_name(name: str) -> bool:
    normalized = name.replace("\\", "/")
    if normalized.startswith("/") or (
        len(normalized) >= 2 and normalized[0].isalpha() and normalized[1] == ":"
    ):
        return True
    return ".." in normalized.split("/")


def zip_inventory(path: Path) -> dict[str, object]:
    members: list[dict[str, object]] = []
    unsafe_names: list[str] = []
    uncompressed_bytes = 0
    with zipfile.ZipFile(path) as archive:
        bad_member = archive.testzip()
        for info in archive.infolist():
            relative_path = info.filename.replace("\\", "/")
            if unsafe_zip_name(relative_path):
                unsafe_names.append(relative_path)
            if info.is_dir():
                members.append(
                    {
                        "relative_path": relative_path,
                        "is_directory": True,
                        "bytes": 0,
                        "sha256": None,
                    }
                )
                continue
            digest = hashlib.sha256()
            with archive.open(info) as handle:
                for chunk in iter(lambda: handle.read(1024 * 1024), b""):
                    digest.update(chunk)
            uncompressed_bytes += info.file_size
            members.append(
                {
                    "relative_path": relative_path,
                    "is_directory": False,
                    "bytes": info.file_size,
                    "sha256": digest.hexdigest().upper(),
                }
            )
    members.sort(key=lambda item: str(item["relative_path"]))
    return {
        "file_members": sum(not bool(item["is_directory"]) for item in members),
        "all_entries": len(members),
        "uncompressed_bytes": uncompressed_bytes,
        "unsafe_names": unsafe_names,
        "crc_error": bad_member,
        "members": members,
    }


def compare_zip(
    name: str,
    expected: dict[str, object],
    actual: dict[str, object],
) -> list[str]:
    errors: list[str] = []
    for field in ("file_members", "all_entries", "uncompressed_bytes"):
        if expected[field] != actual[field]:
            errors.append(
                f"{name} {field}: expected {expected[field]}, got {actual[field]}"
            )
    if actual["unsafe_names"]:
        errors.append(f"{name} unsafe names: {actual['unsafe_names']}")
    if actual["crc_error"] is not None:
        errors.append(f"{name} CRC error: {actual['crc_error']}")
    expected_map = {
        str(item["relative_path"]): item
        for item in expected["members"]  # type: ignore[index]
    }
    actual_map = {
        str(item["relative_path"]): item
        for item in actual["members"]  # type: ignore[index]
    }
    for path in sorted(set(expected_map) | set(actual_map)):
        if path not in expected_map:
            errors.append(f"{name} unexpected member: {path}")
        elif path not in actual_map:
            errors.append(f"{name} missing member: {path}")
        elif expected_map[path] != actual_map[path]:
            errors.append(f"{name} member identity mismatch: {path}")
    return errors


def main() -> int:
    args = parse_args()
    manifest = args.manifest.resolve()
    validation = args.validation.resolve()
    new_zip_dir = args.new_zip_dir.resolve()
    output_prefix = args.output_prefix.resolve()
    output_prefix.parent.mkdir(parents=True, exist_ok=True)

    rows = list(csv.DictReader(manifest.open("r", encoding="utf-8", newline="")))
    expected: dict[str, dict[str, object]] = {
        row["filename"]: {
            "bytes": int(row["bytes"]),
            "sha256": row["sha256"].upper(),
        }
        for row in rows
    }
    expected[manifest.name] = {
        "bytes": manifest.stat().st_size,
        "sha256": sha256_file(manifest),
    }
    expected[validation.name] = {
        "bytes": validation.stat().st_size,
        "sha256": sha256_file(validation),
    }

    errors: list[str] = []
    local_zip_inventories: dict[str, dict[str, object]] = {}
    for name in args.new_zip:
        local_path = new_zip_dir / name
        if name not in expected:
            errors.append(f"new ZIP absent from expected manifest: {name}")
            continue
        if not local_path.is_file():
            errors.append(f"new ZIP missing locally: {local_path}")
            continue
        local_identity = (local_path.stat().st_size, sha256_file(local_path))
        expected_identity = (
            int(expected[name]["bytes"]),
            str(expected[name]["sha256"]),
        )
        if local_identity != expected_identity:
            errors.append(f"new ZIP local identity mismatch: {name}")
            continue
        local_zip_inventories[name] = zip_inventory(local_path)

    api_url = f"https://zenodo.org/api/records/{args.record_id}"
    status, api = get_json(api_url)
    if status != 200 or not isinstance(api, dict):
        raise RuntimeError(f"record API failed with HTTP {status}")
    if int(api["id"]) != args.record_id:
        errors.append(f"record ID mismatch: {api['id']}")
    if api.get("conceptdoi") != args.concept_doi:
        errors.append(f"concept DOI mismatch: {api.get('conceptdoi')}")

    remote_files = {item["key"]: item for item in api["files"]}
    if set(remote_files) != set(expected):
        errors.append(
            "outer file set mismatch: "
            f"missing={sorted(set(expected) - set(remote_files))} "
            f"extra={sorted(set(remote_files) - set(expected))}"
        )

    outer_readback: dict[str, dict[str, object]] = {}
    zip_readback: dict[str, dict[str, object]] = {}
    with tempfile.TemporaryDirectory(prefix=f"zenodo-{args.record_id}-") as temp:
        temp_dir = Path(temp)
        for name in sorted(remote_files):
            if name not in expected:
                continue
            item = remote_files[name]
            remote_path = temp_dir / "remote.zip" if name in args.new_zip else None
            actual_bytes, actual_sha256 = stream_remote(
                item["links"]["self"],
                remote_path,
            )
            expected_identity = (
                int(expected[name]["bytes"]),
                str(expected[name]["sha256"]),
            )
            match = (actual_bytes, actual_sha256) == expected_identity
            if not match:
                errors.append(
                    f"outer identity mismatch {name}: "
                    f"expected={expected_identity}, "
                    f"actual={(actual_bytes, actual_sha256)}"
                )
            outer_readback[name] = {
                "bytes": actual_bytes,
                "sha256": actual_sha256,
                "url": item["links"]["self"],
                "match": match,
            }
            if remote_path is not None:
                actual_inventory = zip_inventory(remote_path)
                expected_inventory = local_zip_inventories[name]
                member_errors = compare_zip(
                    name,
                    expected_inventory,
                    actual_inventory,
                )
                errors.extend(member_errors)
                actual_inventory["match"] = not member_errors
                zip_readback[name] = actual_inventory
                remote_path.unlink(missing_ok=True)

    latest_status, latest = get_json(f"{api_url}/versions/latest")
    latest_record = (
        int(latest["id"])
        if latest_status == 200 and isinstance(latest, dict)
        else None
    )
    if latest_record != args.record_id:
        errors.append(f"latest record mismatch: {latest_record}")

    files_status, files_api = get_json(f"{api_url}/files")
    default_preview = None
    explicit_order: list[str] | None = None
    if files_status == 200 and isinstance(files_api, dict):
        default_preview = files_api.get("default_preview")
        explicit_order = files_api.get("order")
    else:
        errors.append(f"files API failed with HTTP {files_status}")
    if (
        args.expected_default_preview
        and default_preview != args.expected_default_preview
    ):
        errors.append(
            "default preview mismatch: "
            f"expected {args.expected_default_preview}, got {default_preview}"
        )

    draft_status, _ = get_json(f"{api_url}/draft")
    if draft_status != 404:
        errors.append(f"unauthenticated draft probe returned HTTP {draft_status}")

    public_receipt = {
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "record": args.record_id,
        "doi": api.get("doi"),
        "conceptdoi": api.get("conceptdoi"),
        "record_url": api["links"]["self_html"],
        "version": api["metadata"].get("version"),
        "file_count": len(remote_files),
        "files": outer_readback,
        "latest_record": latest_record,
        "unauthenticated_draft_probe_status": draft_status,
        "rdm_default_preview": default_preview,
        "rdm_explicit_order": explicit_order,
        "effective_order": (
            "alphanumeric_default" if explicit_order == [] else "explicit"
        ),
        "new_zip_count": len(zip_readback),
        "new_zip_member_count": sum(
            int(inventory["file_members"])
            for inventory in zip_readback.values()
        ),
        "new_zip_uncompressed_bytes": sum(
            int(inventory["uncompressed_bytes"])
            for inventory in zip_readback.values()
        ),
    }
    Path(f"{output_prefix}_public_readback.json").write_text(
        json.dumps(public_receipt, indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
    )
    Path(f"{output_prefix}_zip_member_readback.json").write_text(
        json.dumps(zip_readback, indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
    )

    summary = {
        "status": public_receipt["status"],
        "errors": errors,
        "record": args.record_id,
        "doi": api.get("doi"),
        "conceptdoi": api.get("conceptdoi"),
        "files": len(outer_readback),
        "bytes": sum(int(item["bytes"]) for item in outer_readback.values()),
        "new_zip_archives": len(zip_readback),
        "new_zip_members": public_receipt["new_zip_member_count"],
        "new_zip_uncompressed_bytes": public_receipt[
            "new_zip_uncompressed_bytes"
        ],
        "latest_record": latest_record,
        "default_preview": default_preview,
        "explicit_order": explicit_order,
    }
    print(json.dumps(summary, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
