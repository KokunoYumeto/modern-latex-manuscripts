#!/usr/bin/env python3
"""Build a deterministic ZIP from the frozen release manifest."""

from __future__ import annotations

import argparse
import json
import os
import sys
import tempfile
import zipfile
from pathlib import Path, PurePosixPath

sys.dont_write_bytecode = True

from pkg import MANIFEST, ROOT, PackageError, digest, inventory, parse_manifest


def add_member(archive: zipfile.ZipFile, name: str, data: bytes) -> None:
    info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
    info.compress_type = zipfile.ZIP_STORED
    info.create_system = 3
    info.external_attr = 0o100644 << 16
    info.internal_attr = 0
    info.extra = b""
    info.comment = b""
    archive.writestr(info, data)


def build(output: Path) -> dict[str, object]:
    output = output.resolve()
    if output.parent == ROOT or ROOT in output.parents:
        raise PackageError("archive output must be outside the release root")
    manifest_data = (ROOT / MANIFEST).read_bytes()
    rows = parse_manifest(manifest_data)
    snapshots = inventory(ROOT)
    expected = [(name, item.size, item.sha256) for name, item in snapshots.items()]
    if rows != expected:
        raise PackageError("live payload does not match manifest")
    version = snapshots["VERSION"].data.decode("utf-8").strip()
    prefix = f"cjk-notation-{version}"

    descriptor, temp_name = tempfile.mkstemp(prefix="cjk-archive-", suffix=".zip", dir=output.parent)
    os.close(descriptor)
    try:
        with zipfile.ZipFile(temp_name, "w", compression=zipfile.ZIP_STORED, allowZip64=True) as archive:
            archive.comment = b""
            for name, snapshot in snapshots.items():
                add_member(archive, f"{prefix}/{name}", snapshot.data)
            add_member(archive, f"{prefix}/{MANIFEST}", manifest_data)
        names_expected = [f"{prefix}/{name}" for name in snapshots] + [f"{prefix}/{MANIFEST}"]
        expected_data = {f"{prefix}/{name}": item.data for name, item in snapshots.items()}
        expected_data[f"{prefix}/{MANIFEST}"] = manifest_data
        with zipfile.ZipFile(temp_name, "r") as archive:
            infos = archive.infolist()
            names = [info.filename for info in infos]
            if names != names_expected or len(names) != len(set(names)):
                raise PackageError("archive member set/order mismatch")
            if len({name.casefold() for name in names}) != len(names):
                raise PackageError("archive casefold collision")
            for info in infos:
                path = PurePosixPath(info.filename)
                if path.is_absolute() or ".." in path.parts or info.flag_bits & 1:
                    raise PackageError(f"unsafe archive member: {info.filename}")
                if info.date_time != (1980, 1, 1, 0, 0, 0) or info.compress_type != zipfile.ZIP_STORED:
                    raise PackageError(f"nondeterministic archive metadata: {info.filename}")
                if info.extra or info.comment or (info.external_attr >> 16) != 0o100644:
                    raise PackageError(f"archive metadata mismatch: {info.filename}")
                if archive.read(info) != expected_data[info.filename]:
                    raise PackageError(f"archive payload mismatch: {info.filename}")
            if archive.testzip() is not None:
                raise PackageError("archive CRC failure")
        os.replace(temp_name, output)
    finally:
        if os.path.exists(temp_name):
            os.unlink(temp_name)
    data = output.read_bytes()
    return {
        "archive": output.name,
        "bytes": len(data),
        "sha256": digest(data),
        "members": len(names_expected),
        "manifest_sha256": digest(manifest_data),
    }


parser = argparse.ArgumentParser()
parser.add_argument("output", type=Path)
args = parser.parse_args()
try:
    result = build(args.output)
except PackageError as exc:
    raise SystemExit(f"archive failure: {exc}") from exc
print(json.dumps(result, sort_keys=True))
