"""Deterministic, offline packager for the six-file D020 release payload.

This module performs no Git, TeX, network, publication, or credential access.
The forbidden first-name token is accepted only in memory from the process
environment and is never included in output or exception text.
"""
from __future__ import annotations

import argparse
import binascii
import csv
import hashlib
import io
import json
import os
import shutil
import stat
import sys
import tempfile
import zipfile
from pathlib import Path, PurePosixPath

import d020_contract as contract


class PackagingFailure(RuntimeError):
    """A deterministic packaging contract was not satisfied."""


RELEASE_FILENAMES = (
    "Deligne_EN.pdf",
    "Deligne_FR.pdf",
    "Deligne_EN.tex",
    "Deligne_FR.tex",
    "Deligne_Source.zip",
    "DELIGNE_PROVENANCE_AUDIT_D020_GAPFILL.zip",
)
SOURCE_ARCHIVE = RELEASE_FILENAMES[4]
PROVENANCE_ARCHIVE = RELEASE_FILENAMES[5]
INHERITED_MEMBER = "inherited/DELIGNE_PROVENANCE_AUDIT_D033_GAPFILL.zip"
D020_BINDING_MEMBER = "D020/D020_COLD_AUDIT_BINDING.json"
D020_SUBJECT_MANIFEST_MEMBER = "D020/S06_math_v6_01/SUBJECT_MANIFEST.json"
D020_FINAL_AUDIT_MEMBER = "D020/S06_math_v6_01/evidence/V6_FULL_PAPER_COLD_AUDIT.json"
PROVENANCE_MANIFEST_MEMBER = "PROVENANCE_MANIFEST.tsv"
PROVENANCE_PRIVACY_MEMBER = "PUBLIC_PROVENANCE_PRIVACY.json"
SOURCE_NONREGRESSION_MEMBER = "integration_audits/SOURCE_NONREGRESSION.json"
ZIP_TIMESTAMP = (1980, 1, 1, 0, 0, 0)
ZIP_FILE_MODE = stat.S_IFREG | 0o644
ZIP_COMPRESSION = zipfile.ZIP_DEFLATED
ZIP_COMPRESSLEVEL = 9
SPLIT_THRESHOLD_BYTES = 2_147_483_648
MAX_PART_BYTES = 90_000_000
COPY_CHUNK_BYTES = 1024 * 1024
PAYLOAD_MANIFEST_NAME = "D020_RELEASE_PAYLOAD_MANIFEST.json"
SIX_FILE_MANIFEST_NAME = "SIX_FILE_RELEASE_MANIFEST.tsv"
BUILD_RECEIPT_NAME = "BUILD_RELEASE_RECEIPT.json"
GITHUB_GIT_BLOB_LIMIT_BYTES = 100 * 1024 * 1024

_FORBIDDEN_EXACT = {
    "next_integration_inputs.json",
    "next_integration_log.md",
    ".env",
    "credentials",
    ".credentials",
    "credential",
    "secrets",
    "secret",
    "tokens",
    "token",
    "new zenodo token.md",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise PackagingFailure(message)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(COPY_CHUNK_BYTES), b""):
            digest.update(block)
    return digest.hexdigest()


def identity(path: Path) -> dict[str, object]:
    md5 = hashlib.md5(usedforsecurity=False)
    sha256 = hashlib.sha256()
    size = 0
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(COPY_CHUNK_BYTES), b""):
            size += len(block)
            md5.update(block)
            sha256.update(block)
    return {"bytes": size, "md5": md5.hexdigest(), "sha256": sha256.hexdigest()}


def _safe_member_name(name: str) -> str:
    require("\\" not in name and "\x00" not in name, "unsafe archive member name")
    pure = PurePosixPath(name)
    require(
        name != ""
        and not name.startswith("/")
        and not pure.is_absolute()
        and all(part not in ("", ".", "..") for part in pure.parts),
        "unsafe archive member name",
    )
    normalized = pure.as_posix()
    require(normalized == name and not name.endswith("/"), "non-canonical archive member name")
    return normalized


def _reject_forbidden_path(relative: str) -> None:
    parts = [part.casefold() for part in PurePosixPath(relative).parts]
    for part in parts:
        require(part != "private_preservation", "private preservation path is forbidden")
        require(part not in _FORBIDDEN_EXACT, "credential or task-control path is forbidden")
        require("credential" not in part, "credential path is forbidden")
        require(not part.endswith((".pem", ".key", ".p12", ".pfx")), "credential file is forbidden")


def _validate_distinct_names(names: list[str]) -> None:
    normalized = [_safe_member_name(name) for name in names]
    require(len(normalized) == len(set(normalized)), "duplicate archive member name")
    folded = [name.casefold() for name in normalized]
    require(len(folded) == len(set(folded)), "case-colliding archive member name")


def _assert_regular_file(path: Path) -> None:
    info = path.lstat()
    require(stat.S_ISREG(info.st_mode), "only regular files may be packaged")
    require(not path.is_symlink(), "symbolic links may not be packaged")
    require(not (getattr(info, "st_file_attributes", 0) & 0x400), "reparse points may not be packaged")


def inventory_tree(root: Path) -> list[tuple[str, Path]]:
    root = root.resolve()
    require(root.is_dir(), "archive input tree is missing")
    root_info = root.lstat()
    require(not root.is_symlink() and not (getattr(root_info, "st_file_attributes", 0) & 0x400), "archive root is a link or reparse point")
    members: list[tuple[str, Path]] = []
    for current, directories, filenames in os.walk(root, topdown=True, followlinks=False):
        current_path = Path(current)
        directories.sort(key=lambda value: (value.casefold(), value))
        filenames.sort(key=lambda value: (value.casefold(), value))
        for directory in directories:
            candidate = current_path / directory
            info = candidate.lstat()
            require(not candidate.is_symlink() and not (getattr(info, "st_file_attributes", 0) & 0x400), "linked directory may not be packaged")
        for filename in filenames:
            path = current_path / filename
            _assert_regular_file(path)
            relative = path.relative_to(root).as_posix()
            _safe_member_name(relative)
            _reject_forbidden_path(relative)
            members.append((relative, path))
    members.sort(key=lambda item: item[0])
    require(len(members) <= 10_000, "archive member cap exceeded")
    require(all(len(name.encode("utf-8")) <= 1024 for name, _ in members), "archive member path cap exceeded")
    _validate_distinct_names([name for name, _ in members])
    require(members, "archive input tree is empty")
    return members


def _zip_info(name: str) -> zipfile.ZipInfo:
    info = zipfile.ZipInfo(name, date_time=ZIP_TIMESTAMP)
    info.create_system = 3
    info.external_attr = ZIP_FILE_MODE << 16
    info.compress_type = ZIP_COMPRESSION
    info.flag_bits = 0x800
    return info


def write_deterministic_zip(destination: Path, members: list[tuple[str, Path]]) -> None:
    _validate_distinct_names([name for name, _ in members])
    require([name for name, _ in members] == sorted(name for name, _ in members), "archive members are not sorted")
    with zipfile.ZipFile(
        destination,
        "x",
        compression=ZIP_COMPRESSION,
        compresslevel=ZIP_COMPRESSLEVEL,
        allowZip64=True,
        strict_timestamps=True,
    ) as archive:
        for name, source in members:
            _assert_regular_file(source)
            with source.open("rb") as reader, archive.open(_zip_info(name), "w", force_zip64=True) as writer:
                shutil.copyfileobj(reader, writer, COPY_CHUNK_BYTES)


def archive_inventory(
    path: Path,
    *,
    require_deterministic_metadata: bool = True,
    require_sorted_names: bool = True,
) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    with zipfile.ZipFile(path, "r") as archive:
        infos = archive.infolist()
        names = [item.filename for item in infos]
        _validate_distinct_names(names)
        if require_sorted_names:
            require(names == sorted(names), "archive member order is not sorted")
        for item in infos:
            require(not item.is_dir(), "directory entries are forbidden in deterministic archives")
            mode = (item.external_attr >> 16) & 0xFFFF
            if require_deterministic_metadata:
                require(item.date_time == ZIP_TIMESTAMP, "archive timestamp is not deterministic")
                require(mode == ZIP_FILE_MODE, "archive mode is not deterministic")
                require(item.compress_type == ZIP_COMPRESSION, "archive compression method is not deterministic")
            digest = hashlib.sha256()
            crc = 0
            size = 0
            with archive.open(item, "r") as reader:
                for block in iter(lambda: reader.read(COPY_CHUNK_BYTES), b""):
                    size += len(block)
                    crc = binascii.crc32(block, crc)
                    digest.update(block)
            require(size == item.file_size, "archive member size replay failed")
            require((crc & 0xFFFFFFFF) == item.CRC, "archive member CRC replay failed")
            rows.append(
                {
                    "name": item.filename,
                    "size": size,
                    "sha256": digest.hexdigest(),
                    "crc32": f"{item.CRC:08x}",
                }
            )
    return rows


def _token_bytes(token: str) -> bytes:
    require(isinstance(token, str) and token != "", "forbidden first-name token is unavailable")
    require(token.isascii() and token.isprintable(), "forbidden first-name token is invalid")
    require(not any(character in token for character in "/\\\r\n\t"), "forbidden first-name token is invalid")
    return token.encode("ascii").lower()


def privacy_scan_file(path: Path, token: str, public_name: str | None = None) -> None:
    """Perform the bounded public-surface policy: name plus raw file bytes.

    Archive files are intentionally opaque here. Their own raw bytes and their
    candidate public names are searched, but they are never recursively opened
    for privacy purposes. Archive structure and CRC/hash integrity are enforced
    separately by the deterministic archive replay functions.
    """
    try:
        needle = _token_bytes(token)
        name = public_name or path.name
        _safe_member_name(name)
        _reject_forbidden_path(name)
        require(needle not in name.encode("utf-8").lower(), "forbidden first-name token detected in public payload")
        _assert_regular_file(path)
        with path.open("rb") as stream:
            overlap = max(0, len(needle) - 1)
            tail = b""
            for block in iter(lambda: stream.read(COPY_CHUNK_BYTES), b""):
                haystack = (tail + block).lower()
                require(needle not in haystack, "forbidden first-name token detected in public payload")
                tail = haystack[-overlap:] if overlap else b""
    except PackagingFailure:
        raise
    except (OSError, EOFError, RuntimeError, zipfile.BadZipFile):
        # OS and ZIP exceptions can embed local scratch/input paths. Keep the
        # fail-closed signal while preventing path or token disclosure.
        raise PackagingFailure("public payload privacy scan could not be completed") from None


def privacy_scan_inventory(members: list[tuple[str, Path]], token: str) -> None:
    for public_name, path in members:
        privacy_scan_file(path, token, public_name)


def verify_provenance_manifest(members: list[tuple[str, Path]]) -> dict[str, object]:
    """Replay the finalizer's sorted, self-excluding provenance seal."""
    by_name = dict(members)
    require(PROVENANCE_MANIFEST_MEMBER in by_name, "provenance manifest is missing")
    manifest_path = by_name[PROVENANCE_MANIFEST_MEMBER]
    require(manifest_path.stat().st_size <= 16 * 1024 * 1024, "provenance manifest exceeds bounded size")
    raw = manifest_path.read_bytes()
    require(
        raw.startswith(b"path\tbytes\tsha256\n") and b"\r\n" not in raw,
        "provenance manifest serialization differs",
    )
    try:
        reader = csv.DictReader(io.StringIO(raw.decode("utf-8"), newline=""), delimiter="\t")
        require(reader.fieldnames == ["path", "bytes", "sha256"], "provenance manifest columns differ")
        rows = list(reader)
        names = [row["path"] for row in rows]
        require(names == sorted(names), "provenance manifest is not sorted")
        _validate_distinct_names(names)
        require(PROVENANCE_MANIFEST_MEMBER not in names, "provenance manifest includes itself")
        expected_names = sorted(set(by_name) - {PROVENANCE_MANIFEST_MEMBER})
        require(names == expected_names, "provenance manifest coverage differs from live tree")
        for row in rows:
            require(row["bytes"].isdigit(), "provenance manifest byte count is malformed")
            require(
                len(row["sha256"]) == 64
                and all(character in "0123456789abcdefABCDEF" for character in row["sha256"]),
                "provenance manifest hash is malformed",
            )
            actual = identity(by_name[row["path"]])
            require(
                int(row["bytes"]) == actual["bytes"]
                and row["sha256"].casefold() == actual["sha256"].casefold(),
                "provenance manifest member replay failed",
            )
    except (UnicodeError, ValueError, TypeError, KeyError) as exc:
        raise PackagingFailure("provenance manifest parse failed") from exc
    return {"name": PROVENANCE_MANIFEST_MEMBER, **identity(manifest_path), "members_replayed": len(rows)}


def validate_provenance_tree(members: list[tuple[str, Path]], inherited_archive: Path) -> dict[str, object]:
    by_name = dict(members)
    required = {
        INHERITED_MEMBER,
        D020_BINDING_MEMBER,
        D020_SUBJECT_MANIFEST_MEMBER,
        D020_FINAL_AUDIT_MEMBER,
        PROVENANCE_MANIFEST_MEMBER,
        PROVENANCE_PRIVACY_MEMBER,
        SOURCE_NONREGRESSION_MEMBER,
    }
    require(required <= set(by_name), "provenance tree lacks required inherited or D020 members")
    require(any(name.startswith("D020/S06_math_v6_01/evidence/") for name in by_name), "provenance tree lacks D020 cold-audit evidence")
    manifest = verify_provenance_manifest(members)
    try:
        privacy = json.loads(by_name[PROVENANCE_PRIVACY_MEMBER].read_text(encoding="utf-8"))
        nonregression = json.loads(by_name[SOURCE_NONREGRESSION_MEMBER].read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise PackagingFailure("final provenance receipt is unreadable") from exc
    require(
        privacy.get("schema") == "d020-public-provenance-privacy-v1"
        and privacy.get("status") == "PASS"
        and privacy.get("findings") == []
        and privacy.get("credential_findings") == []
        and privacy.get("recursive_archive_privacy_scan") is False,
        "provenance privacy receipt is not final PASS",
    )
    require(
        nonregression.get("schema") == "d020-source-nonregression-v1"
        and nonregression.get("status") == "PASS"
        and nonregression.get("all_predecessor_paths_retained") is True
        and nonregression.get("removed_paths") == []
        and nonregression.get("packaging_performed") is False,
        "source nonregression receipt is not final PASS",
    )
    _assert_regular_file(inherited_archive)
    _reject_forbidden_path(inherited_archive.name)
    inherited_identity = identity(inherited_archive)
    require(identity(by_name[INHERITED_MEMBER]) == inherited_identity, "inherited D033 provenance bytes differ")
    final_audit = json.loads(by_name[D020_FINAL_AUDIT_MEMBER].read_text(encoding="utf-8"))
    require(final_audit.get("terminal_status") == "PASS_PAPER_COMPLETE" and final_audit.get("publication_ready") is True, "D020 final cold audit is not publication-ready PASS")
    return {
        "provenance_manifest": manifest,
        "public_provenance_privacy": {
            "name": PROVENANCE_PRIVACY_MEMBER,
            **identity(by_name[PROVENANCE_PRIVACY_MEMBER]),
            "direct_check_only": True,
            "recursive_archive_privacy_scan": False,
        },
        "source_nonregression": {
            "name": SOURCE_NONREGRESSION_MEMBER,
            **identity(by_name[SOURCE_NONREGRESSION_MEMBER]),
        },
        "inherited_public_carrier": {
            "name": INHERITED_MEMBER,
            **inherited_identity,
            "policy": "OPAQUE_ALREADY_PUBLIC_BYTE_IDENTICAL",
            "recursive_open_performed": False,
        },
        "d020_final_cold_audit": {"name": D020_FINAL_AUDIT_MEMBER, **identity(by_name[D020_FINAL_AUDIT_MEMBER])},
        "d020_subject_manifest": {"name": D020_SUBJECT_MANIFEST_MEMBER, **identity(by_name[D020_SUBJECT_MANIFEST_MEMBER])},
    }


def _copy_exact(source: Path, destination: Path) -> None:
    _assert_regular_file(source)
    with source.open("rb") as reader, destination.open("xb") as writer:
        shutil.copyfileobj(reader, writer, COPY_CHUNK_BYTES)
    require(identity(source) == identity(destination), "exact file copy replay failed")


def _build_and_verify_twins(destination: Path, members: list[tuple[str, Path]]) -> list[dict[str, object]]:
    twin = destination.with_name(destination.name + ".determinism-twin")
    write_deterministic_zip(destination, members)
    try:
        write_deterministic_zip(twin, members)
        require(identity(destination) == identity(twin), "deterministic archive twins differ")
        first = archive_inventory(destination)
        second = archive_inventory(twin)
        require(first == second, "archive member replay differs between twins")
        return first
    finally:
        twin.unlink(missing_ok=True)


def split_required(actual_archive_size: int) -> bool:
    require(actual_archive_size >= 0, "invalid archive size")
    return actual_archive_size >= SPLIT_THRESHOLD_BYTES


def split_large_archive(archive: Path, parts_directory: Path) -> list[Path]:
    """Split only a qualifying actual archive; the unsplit six-file payload remains intact."""
    actual_size = archive.stat().st_size
    if not split_required(actual_size):
        return []
    parts_directory.mkdir(parents=True, exist_ok=False)
    parts: list[Path] = []
    with archive.open("rb") as source:
        index = 1
        while True:
            part = parts_directory / f"{archive.name}.part{index:04d}"
            written = 0
            with part.open("xb") as target:
                while written < MAX_PART_BYTES:
                    block = source.read(min(COPY_CHUNK_BYTES, MAX_PART_BYTES - written))
                    if not block:
                        break
                    target.write(block)
                    written += len(block)
            if written == 0:
                part.unlink(missing_ok=True)
                break
            require(written <= MAX_PART_BYTES, "split part exceeds maximum size")
            parts.append(part)
            index += 1
    require(sum(part.stat().st_size for part in parts) == actual_size, "split byte count replay failed")
    digest = hashlib.sha256()
    for part in parts:
        with part.open("rb") as stream:
            for block in iter(lambda: stream.read(COPY_CHUNK_BYTES), b""):
                digest.update(block)
    require(digest.hexdigest() == sha256_file(archive), "split byte identity replay failed")
    return parts


def github_release_asset_contract(files: list[dict[str, object]]) -> dict[str, object]:
    require([row["name"] for row in files] == list(RELEASE_FILENAMES), "release-asset inventory differs from six-file contract")
    assets = [
        {key: row[key] for key in ("name", "staged_path", "bytes", "md5", "sha256")}
        for row in files
    ]
    return {
        "schema": "d020-github-release-assets-v1",
        "transport": "GITHUB_RELEASE_ASSETS_ONLY",
        "tracked_git_blobs": False,
        "git_blob_limit_bytes": GITHUB_GIT_BLOB_LIMIT_BYTES,
        "assets": assets,
        "assets_over_git_blob_limit": [
            row["name"] for row in assets if row["bytes"] > GITHUB_GIT_BLOB_LIMIT_BYTES
        ],
        "tracked_tree_mapping_owner": "SEPARATE_GITHUB_ADAPTER",
    }


def _staged_part_path(part: Path, build_root: Path) -> str:
    try:
        relative = part.resolve().relative_to(build_root.resolve()).as_posix()
    except ValueError as exc:
        raise PackagingFailure("split part is outside the cumulative build root") from exc
    return _safe_member_name(relative)


def _write_manifest(
    manifest_path: Path,
    release_directory: Path,
    archive_members: dict[str, list[dict[str, object]]],
    provenance_validation: dict[str, object],
    split_parts: list[Path],
) -> dict[str, object]:
    outputs = []
    for name in RELEASE_FILENAMES:
        path = release_directory / name
        outputs.append(
            {
                "name": name,
                "staged_path": f"release/{name}",
                **identity(path),
            }
        )
    result = {
        "schema": "d020-release-payload-manifest-v1",
        "status": "PASS",
        "release_top_level_filenames": list(RELEASE_FILENAMES),
        "files": outputs,
        "archives": archive_members,
        "provenance_validation": provenance_validation,
        "github_release_assets": github_release_asset_contract(outputs),
        "split_policy": {
            "threshold_bytes_inclusive": SPLIT_THRESHOLD_BYTES,
            "maximum_part_bytes": MAX_PART_BYTES,
            "parts": [
                {"name": path.name, "staged_path": _staged_part_path(path, release_directory.parent), **identity(path)}
                for path in sorted(split_parts)
            ],
        },
    }
    data = (json.dumps(result, ensure_ascii=True, indent=2, sort_keys=True) + "\n").encode("utf-8")
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    with manifest_path.open("xb") as stream:
        stream.write(data)
    return result


def _write_release_metadata(
    build_root: Path,
    manifest_path: Path,
    manifest: dict[str, object],
) -> None:
    tsv_path = build_root / SIX_FILE_MANIFEST_NAME
    receipt_path = build_root / BUILD_RECEIPT_NAME
    lines = ["name\tbytes\tmd5\tsha256"]
    for row in manifest["files"]:
        lines.append(f'{row["name"]}\t{row["bytes"]}\t{row["md5"]}\t{row["sha256"]}')
    with tsv_path.open("xb") as stream:
        stream.write(("\n".join(lines) + "\n").encode("ascii"))
    receipt = {
        "schema": "d020-build-release-receipt-v1",
        "status": "PASS",
        "release_directory": "release",
        "files": manifest["files"],
        "payload_manifest": {"name": PAYLOAD_MANIFEST_NAME, **identity(manifest_path)},
        "six_file_release_manifest": {"name": SIX_FILE_MANIFEST_NAME, **identity(tsv_path)},
        "archive_replay_in_payload_manifest": True,
    }
    with receipt_path.open("xb") as stream:
        stream.write((json.dumps(receipt, ensure_ascii=True, indent=2, sort_keys=True) + "\n").encode("utf-8"))


def package_release(
    source_tree: Path,
    provenance_tree: Path,
    inherited_d033_provenance: Path,
    release_directory: Path,
    manifest_path: Path,
    forbidden_first_name: str,
    parts_root: Path | None = None,
) -> dict[str, object]:
    """Create, replay, privacy-scan, and atomically expose the D020 payload."""
    _token_bytes(forbidden_first_name)
    source_tree = source_tree.resolve()
    provenance_tree = provenance_tree.resolve()
    release_directory = release_directory.resolve()
    manifest_path = manifest_path.resolve()
    build_root = release_directory.parent
    tsv_path = build_root / SIX_FILE_MANIFEST_NAME
    receipt_path = build_root / BUILD_RECEIPT_NAME
    require(release_directory.name == "release", "release destination must be the cumulative release directory")
    require(manifest_path == build_root / PAYLOAD_MANIFEST_NAME, "payload manifest must use the cumulative final-layout path")
    require(
        source_tree.parent == build_root and provenance_tree.parent == build_root,
        "source, provenance, and release trees must share the cumulative build root",
    )
    require(not release_directory.exists(), "release destination already exists")
    require(not manifest_path.exists(), "payload manifest already exists")
    require(not tsv_path.exists() and not receipt_path.exists(), "release metadata already exists")
    require(source_tree != provenance_tree, "source and provenance trees must differ")
    for public_root in (source_tree, provenance_tree):
        _reject_forbidden_path(public_root.name)
        require(release_directory not in public_root.parents and public_root not in release_directory.parents, "release destination overlaps an input tree")

    try:
        source_manifest_rows = contract.verify_source_manifest(
            source_tree, source_tree / contract.SOURCE_MANIFEST_NAME
        )
    except (OSError, ValueError, contract.Failure) as exc:
        raise PackagingFailure("source manifest replay failed") from exc
    source_members = inventory_tree(source_tree)
    require(
        len(source_manifest_rows) + 1 == len(source_members),
        "source manifest self-exclusion accounting failed",
    )
    provenance_members = inventory_tree(provenance_tree)
    provenance_validation = validate_provenance_tree(provenance_members, inherited_d033_provenance.resolve())
    privacy_scan_inventory(source_members, forbidden_first_name)
    privacy_scan_inventory(provenance_members, forbidden_first_name)
    for name in RELEASE_FILENAMES[:4]:
        require((source_tree / name).is_file(), "source tree lacks a canonical top-level release file")

    release_directory.parent.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(prefix=".d020-package-", dir=release_directory.parent))
    split_parts: list[Path] = []
    archive_members: dict[str, list[dict[str, object]]] = {}
    parts_root = (parts_root or release_directory.with_name(release_directory.name + ".split_parts")).resolve()
    require(parts_root.parent == build_root, "split-parts destination must stay in the cumulative build root")
    require(not parts_root.exists(), "split-parts destination already exists")
    release_exposed = False
    try:
        for name in RELEASE_FILENAMES[:4]:
            _copy_exact(source_tree / name, staging / name)
        archive_members[SOURCE_ARCHIVE] = _build_and_verify_twins(staging / SOURCE_ARCHIVE, source_members)
        archive_members[PROVENANCE_ARCHIVE] = _build_and_verify_twins(staging / PROVENANCE_ARCHIVE, provenance_members)
        require(sorted(path.name for path in staging.iterdir()) == sorted(RELEASE_FILENAMES), "release staging does not contain exactly six filenames")
        for name in RELEASE_FILENAMES:
            privacy_scan_file(staging / name, forbidden_first_name)
        os.replace(staging, release_directory)
        release_exposed = True
        for archive_name in (SOURCE_ARCHIVE, PROVENANCE_ARCHIVE):
            archive = release_directory / archive_name
            if split_required(archive.stat().st_size):
                archive_parts_dir = parts_root / archive_name
                if not parts_root.exists():
                    parts_root.mkdir(parents=True)
                split_parts.extend(split_large_archive(archive, archive_parts_dir))
        require(sorted(path.name for path in release_directory.iterdir()) == sorted(RELEASE_FILENAMES), "release directory does not contain exactly six filenames")
        result = _write_manifest(
            manifest_path,
            release_directory,
            archive_members,
            provenance_validation,
            split_parts,
        )
        _write_release_metadata(build_root, manifest_path, result)
        return result
    except Exception:
        if staging.exists():
            shutil.rmtree(staging)
        if release_exposed and release_directory.exists():
            shutil.rmtree(release_directory)
        if parts_root.exists():
            shutil.rmtree(parts_root)
        manifest_path.unlink(missing_ok=True)
        tsv_path.unlink(missing_ok=True)
        receipt_path.unlink(missing_ok=True)
        raise


def _read_secret_from_environment() -> str:
    value = os.environ.get("USERNAME", "")
    require(value and value.isascii(), "forbidden first-name token is unavailable")
    return value


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-tree", type=Path, required=True)
    parser.add_argument("--provenance-tree", type=Path, required=True)
    parser.add_argument("--inherited-d033-provenance", type=Path, required=True)
    parser.add_argument("--release-directory", type=Path, required=True)
    parser.add_argument("--payload-manifest", type=Path, required=True)
    parser.add_argument("--parts-root", type=Path)
    args = parser.parse_args()
    result = package_release(
        source_tree=args.source_tree,
        provenance_tree=args.provenance_tree,
        inherited_d033_provenance=args.inherited_d033_provenance,
        release_directory=args.release_directory,
        manifest_path=args.payload_manifest,
        forbidden_first_name=_read_secret_from_environment(),
        parts_root=args.parts_root,
    )
    print(json.dumps({"status": result["status"]}, sort_keys=True))


if __name__ == "__main__":
    main()
