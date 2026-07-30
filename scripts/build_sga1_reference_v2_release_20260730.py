#!/usr/bin/env python3
"""Build the compact SGA1 reference-v2 and refreshed SGA1-6 ZIPs."""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import shutil
import zipfile
from pathlib import Path, PurePosixPath


ROOT = "SGA_Current_English_Readers_and_TeX_20260730"
SOURCE_ZIP_ROOT = "SGA1_English_Complete_ReferenceV2_R1_20260730"
FIXED_ZIP_TIME = (2026, 7, 30, 12, 0, 0)
EXCLUDED_FROM_PACKAGE_MANIFEST = {
    "PACKAGE_VALIDATION.json",
    "ZENODO_PAYLOAD_MANIFEST.csv",
}
SGA1_READER = f"{ROOT}/SGA1/reader/SGA1_English_Reader.pdf"
SGA1_MASTER = (
    f"{ROOT}/SGA1/source/SGA1_English_source_sync_workpass.tex"
)
ROOT_MANIFEST = f"{ROOT}/SHA256SUMS.csv"


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def sha256_path(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(4 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def safe_member(name: str) -> bool:
    pure = PurePosixPath(name)
    return (
        name == name.replace("\\", "/")
        and not pure.is_absolute()
        and ".." not in pure.parts
        and not (len(name) >= 2 and name[1] == ":")
    )


def zip_info(name: str) -> zipfile.ZipInfo:
    info = zipfile.ZipInfo(name, FIXED_ZIP_TIME)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = 0o100644 << 16
    info.create_system = 3
    return info


def write_member(archive: zipfile.ZipFile, name: str, data: bytes) -> None:
    if not safe_member(name):
        raise RuntimeError(f"unsafe ZIP member path: {name}")
    archive.writestr(zip_info(name), data, compresslevel=9)


def read_manifest(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def validate_candidate(candidate: Path) -> dict:
    manifest_path = candidate / "ZENODO_PAYLOAD_MANIFEST.csv"
    validation_path = candidate / "PACKAGE_VALIDATION.json"
    rows = read_manifest(manifest_path)
    actual = {
        path.relative_to(candidate).as_posix(): path
        for path in candidate.rglob("*")
        if path.is_file()
        and path.relative_to(candidate).as_posix()
        not in EXCLUDED_FROM_PACKAGE_MANIFEST
    }
    by_path = {row["relative_path"]: row for row in rows}
    if len(rows) != 178 or len(by_path) != 178 or set(by_path) != set(actual):
        raise RuntimeError("candidate manifest exact-set closure failed")
    for name, path in actual.items():
        row = by_path[name]
        observed = (path.stat().st_size, sha256_path(path))
        expected = (int(row["bytes"]), row["sha256"].upper())
        if observed != expected:
            raise RuntimeError(f"candidate manifest mismatch: {name}")
    validation = json.loads(validation_path.read_text(encoding="utf-8-sig"))
    if validation.get("status") != "PASS" or validation.get("errors"):
        raise RuntimeError("candidate packaged validation is not PASS")
    files = sorted(
        (path for path in candidate.rglob("*") if path.is_file()),
        key=lambda path: path.relative_to(candidate).as_posix(),
    )
    canonical = hashlib.sha256()
    identities = {}
    for path in files:
        relative = path.relative_to(candidate).as_posix()
        identity = {
            "bytes": path.stat().st_size,
            "sha256": sha256_path(path),
        }
        identities[relative] = identity
        canonical.update(
            (
                f"{relative}\t{identity['bytes']}\t{identity['sha256']}\n"
            ).encode("utf-8")
        )
    return {
        "files": len(files),
        "bytes": sum(item["bytes"] for item in identities.values()),
        "canonical_identity_sha256": canonical.hexdigest().upper(),
        "manifest_rows": len(rows),
        "manifest_sha256": sha256_path(manifest_path),
        "package_validation_sha256": sha256_path(validation_path),
        "identities": identities,
    }


def build_source_zip(candidate: Path, output: Path) -> dict:
    temporary = output.with_suffix(output.suffix + ".tmp")
    temporary.parent.mkdir(parents=True, exist_ok=True)
    temporary.unlink(missing_ok=True)
    files = sorted(
        (path for path in candidate.rglob("*") if path.is_file()),
        key=lambda path: path.relative_to(candidate).as_posix(),
    )
    with zipfile.ZipFile(temporary, "w", allowZip64=True) as archive:
        for path in files:
            relative = path.relative_to(candidate).as_posix()
            write_member(
                archive,
                f"{SOURCE_ZIP_ROOT}/{relative}",
                path.read_bytes(),
            )
    with zipfile.ZipFile(temporary) as archive:
        infos = [info for info in archive.infolist() if not info.is_dir()]
        if len(infos) != len(files):
            raise RuntimeError("SGA1 source ZIP member count changed")
        for path, info in zip(files, infos, strict=True):
            data = archive.read(info.filename)
            if (
                len(data),
                sha256_bytes(data),
            ) != (path.stat().st_size, sha256_path(path)):
                raise RuntimeError(f"SGA1 source ZIP replay failed: {info.filename}")
    temporary.replace(output)
    return {
        "name": output.name,
        "bytes": output.stat().st_size,
        "sha256": sha256_path(output),
        "members": len(files),
        "uncompressed_bytes": sum(path.stat().st_size for path in files),
    }


def manifest_bytes(members: dict[str, bytes]) -> bytes:
    lines = ["relative_path,bytes,sha256\r\n"]
    for name in sorted(members, key=str.casefold):
        relative = name.removeprefix(f"{ROOT}/")
        data = members[name]
        lines.append(f'"{relative}",{len(data)},{sha256_bytes(data)}\r\n')
    return "".join(lines).encode("utf-8")


def build_current_bundle(
    existing: Path,
    candidate: Path,
    output: Path,
) -> dict:
    with zipfile.ZipFile(existing) as archive:
        infos = [info for info in archive.infolist() if not info.is_dir()]
        names = [info.filename for info in infos]
        if (
            len(names) != 1394
            or len(set(names)) != len(names)
            or ROOT_MANIFEST not in names
            or not all(map(safe_member, names))
        ):
            raise RuntimeError("existing SGA bundle boundary changed")
        members = {
            name: archive.read(name)
            for name in names
            if name != ROOT_MANIFEST
        }

    candidate_drafts = {
        path.name: path.read_bytes()
        for path in sorted((candidate / "drafts").glob("*.texfrag"))
    }
    bundled_drafts = {
        name.rsplit("/", 1)[1]: data
        for name, data in members.items()
        if name.startswith(f"{ROOT}/SGA1/source/drafts/")
    }
    if set(candidate_drafts) != set(bundled_drafts):
        raise RuntimeError("candidate and bundled SGA1 component path sets differ")
    for filename, data in candidate_drafts.items():
        members[f"{ROOT}/SGA1/source/drafts/{filename}"] = data

    members[SGA1_READER] = (
        candidate / "SGA1_English_complete_reference_reader.pdf"
    ).read_bytes()
    members[SGA1_MASTER] = (
        candidate / "SGA1_English_source_sync_workpass.tex"
    ).read_bytes()
    manifest = manifest_bytes(members)

    temporary = output.with_suffix(output.suffix + ".tmp")
    temporary.unlink(missing_ok=True)
    with zipfile.ZipFile(temporary, "w", allowZip64=True) as archive:
        for name in sorted(members, key=str.casefold):
            write_member(archive, name, members[name])
        write_member(archive, ROOT_MANIFEST, manifest)

    with zipfile.ZipFile(temporary) as archive:
        infos = [info for info in archive.infolist() if not info.is_dir()]
        names = [info.filename for info in infos]
        if len(infos) != 1394 or len(set(names)) != 1394:
            raise RuntimeError("refreshed SGA bundle member count changed")
        rows = list(
            csv.DictReader(
                io.StringIO(archive.read(ROOT_MANIFEST).decode("utf-8-sig"))
            )
        )
        if len(rows) != 1393:
            raise RuntimeError("refreshed SGA bundle manifest row count changed")
        represented = {}
        for row in rows:
            name = f"{ROOT}/{row['relative_path']}"
            data = archive.read(name)
            observed = (len(data), sha256_bytes(data))
            expected = (int(row["bytes"]), row["sha256"].upper())
            if observed != expected:
                raise RuntimeError(f"refreshed SGA bundle mismatch: {name}")
            represented[name] = observed
        if set(represented) != set(names) - {ROOT_MANIFEST}:
            raise RuntimeError("refreshed SGA bundle manifest closure failed")
        if sha256_bytes(archive.read(SGA1_READER)) != (
            "46406925C8EBBF4309A67CF4D84B493952EF99C067E1971F885F0F3AF326BA1E"
        ):
            raise RuntimeError("refreshed SGA bundle has the wrong SGA1 reader")
    temporary.replace(output)
    return {
        "name": output.name,
        "bytes": output.stat().st_size,
        "sha256": sha256_path(output),
        "members": 1394,
        "manifest_rows": 1393,
        "uncompressed_bytes": sum(len(data) for data in members.values())
        + len(manifest),
        "sga1_reader_sha256": sha256_bytes(members[SGA1_READER]),
        "sga1_master_sha256": sha256_bytes(members[SGA1_MASTER]),
    }


def save_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidate", type=Path, required=True)
    parser.add_argument("--existing-bundle", type=Path, required=True)
    parser.add_argument("--bundle-output", type=Path, required=True)
    parser.add_argument("--source-zip-output", type=Path, required=True)
    parser.add_argument("--report", type=Path, required=True)
    args = parser.parse_args()

    candidate = args.candidate.resolve()
    existing = args.existing_bundle.resolve()
    bundle_output = args.bundle_output.resolve()
    source_zip_output = args.source_zip_output.resolve()
    report = {
        "schema": "sga1-reference-v2-compact-release-build-1.0",
        "status": "PASS",
        "candidate": validate_candidate(candidate),
        "source_zip": build_source_zip(candidate, source_zip_output),
        "current_sga1_6_bundle": build_current_bundle(
            existing,
            candidate,
            bundle_output,
        ),
    }
    save_json(args.report.resolve(), report)
    print(json.dumps(report, indent=2, ensure_ascii=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
