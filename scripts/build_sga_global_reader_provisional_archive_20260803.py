#!/usr/bin/env python3
"""Build and verify the deterministic provisional SGA global-reader transport ZIP."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import shutil
import zipfile
from pathlib import Path, PurePosixPath


REPO_ROOT = Path(__file__).resolve().parents[1]
PACKAGE_ROOT = (
    REPO_ROOT
    / "sources/sga/sga1-7ii-global-reader-provisional-20260803-r1"
)
MANIFEST_NAME = "10z6_SGA_1-7II_Global_Reader_PUBLIC_MANIFEST_20260803.csv"
ZIP_NAME = "10z7_SGA_1-7II_Global_Reader_PUBLIC_PACKAGE_20260803.zip"
EXPECTED_MANIFEST = (
    3_349,
    "C905A69866610D748E6E3B9907FAB4BAC882E90157E51A66ECB46346C4B37945",
)
FIXED_ZIP_TIME = (2026, 8, 3, 0, 0, 0)


def sha256_path(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def md5_path(path: Path) -> str:
    digest = hashlib.md5(usedforsecurity=False)
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().lower()


def safe_name(name: str) -> bool:
    path = PurePosixPath(name.replace("\\", "/"))
    return (
        bool(name)
        and not path.is_absolute()
        and len(path.parts) == 1
        and path.parts[0] not in {".", ".."}
        and "\\" not in name
    )


def load_manifest() -> list[dict[str, object]]:
    path = PACKAGE_ROOT / MANIFEST_NAME
    observed = (path.stat().st_size, sha256_path(path))
    if observed != EXPECTED_MANIFEST:
        raise RuntimeError(f"Public manifest identity changed: {observed}")
    with path.open(encoding="utf-8-sig", newline="") as handle:
        rows = [dict(row) for row in csv.DictReader(handle)]
    if len(rows) != 6:
        raise RuntimeError("Public manifest must contain exactly six payload rows")
    names = [str(row["remote_name"]) for row in rows]
    if len(names) != len(set(names)) or not all(map(safe_name, names)):
        raise RuntimeError("Public manifest names are duplicated or unsafe")
    for row in rows:
        path = PACKAGE_ROOT / str(row["remote_name"])
        observed = (path.stat().st_size, sha256_path(path), md5_path(path))
        expected = (
            int(row["bytes"]),
            str(row["sha256"]).upper(),
            str(row["md5"]).lower(),
        )
        if observed != expected:
            raise RuntimeError(f"Public payload identity changed: {path.name}")
        if not str(row["privacy_status"]).startswith("PASS_"):
            raise RuntimeError(f"Privacy status is not a pass: {path.name}")
    return rows


def ordered_members(rows: list[dict[str, object]]) -> list[str]:
    return [str(row["remote_name"]) for row in rows] + [MANIFEST_NAME]


def build_zip(rows: list[dict[str, object]]) -> None:
    target = PACKAGE_ROOT / ZIP_NAME
    if target.exists():
        target.unlink()
    with zipfile.ZipFile(
        target,
        mode="w",
        compression=zipfile.ZIP_DEFLATED,
        compresslevel=6,
        allowZip64=True,
    ) as archive:
        for name in ordered_members(rows):
            source = PACKAGE_ROOT / name
            info = zipfile.ZipInfo(name, date_time=FIXED_ZIP_TIME)
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            info.compress_type = (
                zipfile.ZIP_STORED
                if source.suffix.lower() == ".pdf"
                else zipfile.ZIP_DEFLATED
            )
            with source.open("rb") as input_handle, archive.open(
                info, mode="w", force_zip64=True
            ) as output_handle:
                shutil.copyfileobj(input_handle, output_handle, 1024 * 1024)


def verify_zip(rows: list[dict[str, object]]) -> dict[str, object]:
    path = PACKAGE_ROOT / ZIP_NAME
    expected_names = ordered_members(rows)
    inventory: list[dict[str, object]] = []
    with zipfile.ZipFile(path) as archive:
        names = archive.namelist()
        if names != expected_names or not all(map(safe_name, names)):
            raise RuntimeError("Transport ZIP member boundary changed")
        for name in names:
            digest = hashlib.sha256()
            size = 0
            with archive.open(name) as handle:
                for chunk in iter(lambda: handle.read(1024 * 1024), b""):
                    size += len(chunk)
                    digest.update(chunk)
            direct = PACKAGE_ROOT / name
            if (size, digest.hexdigest().upper()) != (
                direct.stat().st_size,
                sha256_path(direct),
            ):
                raise RuntimeError(f"ZIP member differs from direct file: {name}")
            inventory.append(
                {"name": name, "bytes": size, "sha256": digest.hexdigest().upper()}
            )
    canonical = json.dumps(
        inventory, ensure_ascii=True, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return {
        "status": "PASS",
        "package_root": PACKAGE_ROOT.relative_to(REPO_ROOT).as_posix(),
        "manifest": {
            "name": MANIFEST_NAME,
            "bytes": EXPECTED_MANIFEST[0],
            "sha256": EXPECTED_MANIFEST[1],
            "rows": len(rows),
            "self_excluding": True,
        },
        "zip": {
            "name": ZIP_NAME,
            "bytes": path.stat().st_size,
            "sha256": sha256_path(path),
            "md5": md5_path(path),
            "members": len(inventory),
            "uncompressed_bytes": sum(int(row["bytes"]) for row in inventory),
            "inventory_sha256": hashlib.sha256(canonical).hexdigest().upper(),
        },
        "members": inventory,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--build", action="store_true")
    args = parser.parse_args()
    rows = load_manifest()
    if args.build:
        build_zip(rows)
    print(json.dumps(verify_zip(rows), indent=2, ensure_ascii=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
