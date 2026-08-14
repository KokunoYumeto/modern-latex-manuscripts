#!/usr/bin/env python3
"""Shared no-follow inventory and deterministic manifest utilities."""

from __future__ import annotations

import csv
import ctypes
import hashlib
import io
import os
import re
import stat
import tempfile
import unicodedata
from dataclasses import dataclass
from pathlib import Path

if os.name == "nt":
    import msvcrt


ROOT = Path(__file__).resolve().parent
MANIFEST = "manifest.csv"
ALLOWED_METADATA_DIR = ".git"
WINDOWS_DEVICES = {
    "CON", "PRN", "AUX", "NUL",
    *(f"COM{i}" for i in range(1, 10)),
    *(f"LPT{i}" for i in range(1, 10)),
}
SHA_RE = re.compile(r"^[A-F0-9]{64}$")


class PackageError(RuntimeError):
    pass


@dataclass(frozen=True)
class Snapshot:
    name: str
    data: bytes
    size: int
    sha256: str
    stat_key: tuple[int, ...]


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def _stat_key(info: os.stat_result) -> tuple[int, ...]:
    return (
        int(info.st_mode),
        int(info.st_size),
        int(getattr(info, "st_mtime_ns", 0)),
        int(getattr(info, "st_ctime_ns", 0)),
        int(info.st_ino),
        int(info.st_dev),
        int(info.st_nlink),
        int(getattr(info, "st_file_attributes", 0)),
    )


class _WindowsFileInfo(ctypes.Structure):
    _fields_ = [
        ("dwFileAttributes", ctypes.c_uint32),
        ("ftCreationTimeLow", ctypes.c_uint32),
        ("ftCreationTimeHigh", ctypes.c_uint32),
        ("ftLastAccessTimeLow", ctypes.c_uint32),
        ("ftLastAccessTimeHigh", ctypes.c_uint32),
        ("ftLastWriteTimeLow", ctypes.c_uint32),
        ("ftLastWriteTimeHigh", ctypes.c_uint32),
        ("dwVolumeSerialNumber", ctypes.c_uint32),
        ("nFileSizeHigh", ctypes.c_uint32),
        ("nFileSizeLow", ctypes.c_uint32),
        ("nNumberOfLinks", ctypes.c_uint32),
        ("nFileIndexHigh", ctypes.c_uint32),
        ("nFileIndexLow", ctypes.c_uint32),
    ]


def _link_count(path: Path, info: os.stat_result) -> int:
    """Return a trustworthy hard-link count even when Windows st_nlink is 0."""
    if os.name != "nt" or info.st_nlink:
        return int(info.st_nlink)
    details = _WindowsFileInfo()
    with path.open("rb") as handle:
        native_handle = msvcrt.get_osfhandle(handle.fileno())
        get_info = ctypes.windll.kernel32.GetFileInformationByHandle
        get_info.argtypes = [ctypes.c_void_p, ctypes.POINTER(_WindowsFileInfo)]
        get_info.restype = ctypes.c_int
        if not get_info(ctypes.c_void_p(native_handle), ctypes.byref(details)):
            raise PackageError(f"cannot determine hard-link count: {path.name}")
    return int(details.nNumberOfLinks)


def validate_name(name: str) -> None:
    if not name or name in {".", ".."}:
        raise PackageError(f"unsafe empty/dot path: {name!r}")
    if name != unicodedata.normalize("NFC", name):
        raise PackageError(f"non-NFC path: {name!r}")
    try:
        name.encode("utf-8", "strict")
    except UnicodeEncodeError as exc:
        raise PackageError(f"non-UTF-8 path: {name!r}") from exc
    if any(char in name for char in "/\\:") or name.endswith((" ", ".")):
        raise PackageError(f"unsafe path syntax: {name!r}")
    if any(ord(char) < 32 or ord(char) == 127 for char in name):
        raise PackageError(f"control in path: {name!r}")
    stem = name.split(".", 1)[0].upper()
    if stem in WINDOWS_DEVICES:
        raise PackageError(f"Windows device path: {name!r}")


def inventory(root: Path = ROOT) -> dict[str, Snapshot]:
    root = root.resolve(strict=True)
    snapshots: dict[str, Snapshot] = {}
    seen_casefold: dict[str, str] = {}
    initial_entries: dict[str, tuple[int, ...]] = {}

    with os.scandir(root) as entries:
        for entry in entries:
            validate_name(entry.name)
            info = entry.stat(follow_symlinks=False)
            attrs = int(getattr(info, "st_file_attributes", 0))
            if entry.is_symlink() or attrs & int(getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400)):
                raise PackageError(f"symlink/reparse entry: {entry.name}")
            if entry.name == ALLOWED_METADATA_DIR:
                if not stat.S_ISDIR(info.st_mode):
                    raise PackageError(".git is not a directory")
                continue
            if stat.S_ISDIR(info.st_mode):
                raise PackageError(f"unexpected directory: {entry.name}")
            if not stat.S_ISREG(info.st_mode):
                raise PackageError(f"non-regular entry: {entry.name}")
            path = root / entry.name
            link_count = _link_count(path, info)
            if link_count != 1:
                raise PackageError(f"unexpected hard-link count: {entry.name}:{link_count}")
            folded = unicodedata.normalize("NFC", entry.name).casefold()
            if folded in seen_casefold:
                raise PackageError(f"casefold collision: {seen_casefold[folded]} / {entry.name}")
            seen_casefold[folded] = entry.name
            initial_entries[entry.name] = _stat_key(info)
            if entry.name == MANIFEST:
                continue
            before = path.stat(follow_symlinks=False)
            data = path.read_bytes()
            after = path.stat(follow_symlinks=False)
            if _stat_key(before) != _stat_key(after) or len(data) != before.st_size:
                raise PackageError(f"concurrent file mutation: {entry.name}")
            snapshots[entry.name] = Snapshot(
                name=entry.name,
                data=data,
                size=len(data),
                sha256=digest(data),
                stat_key=_stat_key(after),
            )

    final_entries: dict[str, tuple[int, ...]] = {}
    with os.scandir(root) as entries:
        for entry in entries:
            if entry.name == ALLOWED_METADATA_DIR:
                continue
            final_entries[entry.name] = _stat_key(entry.stat(follow_symlinks=False))
    if final_entries != initial_entries:
        raise PackageError("release tree changed during inventory")
    return dict(sorted(snapshots.items()))


def manifest_rows(snapshots: dict[str, Snapshot]) -> list[tuple[str, int, str]]:
    return [(name, item.size, item.sha256) for name, item in sorted(snapshots.items())]


def canonical_manifest_bytes(rows: list[tuple[str, int, str]]) -> bytes:
    stream = io.StringIO(newline="")
    writer = csv.writer(stream, lineterminator="\n")
    writer.writerow(("path", "bytes", "sha256"))
    writer.writerows(rows)
    return stream.getvalue().encode("utf-8")


def parse_manifest(data: bytes) -> list[tuple[str, int, str]]:
    try:
        text = data.decode("utf-8", "strict")
    except UnicodeDecodeError as exc:
        raise PackageError("manifest is not UTF-8") from exc
    if not text.endswith("\n") or text.endswith("\n\n") or "\r" in text:
        raise PackageError("manifest line endings are not canonical")
    reader = csv.reader(io.StringIO(text, newline=""))
    rows = list(reader)
    if not rows or rows[0] != ["path", "bytes", "sha256"]:
        raise PackageError("manifest header mismatch")
    parsed: list[tuple[str, int, str]] = []
    for index, row in enumerate(rows[1:], 2):
        if len(row) != 3:
            raise PackageError(f"manifest row {index} width")
        name, size_text, sha256 = row
        validate_name(name)
        if not size_text.isascii() or not size_text.isdecimal() or (size_text.startswith("0") and size_text != "0"):
            raise PackageError(f"manifest row {index} size")
        if not SHA_RE.fullmatch(sha256):
            raise PackageError(f"manifest row {index} SHA-256")
        parsed.append((name, int(size_text), sha256))
    names = [row[0] for row in parsed]
    if names != sorted(names) or len(names) != len(set(names)):
        raise PackageError("manifest paths are unsorted or duplicated")
    if len({unicodedata.normalize("NFC", name).casefold() for name in names}) != len(names):
        raise PackageError("manifest paths have a casefold collision")
    if canonical_manifest_bytes(parsed) != data:
        raise PackageError("manifest serialization is not canonical")
    return parsed


def write_manifest(root: Path = ROOT) -> tuple[int, int, str]:
    snapshots = inventory(root)
    payload = canonical_manifest_bytes(manifest_rows(snapshots))
    descriptor, temp_name = tempfile.mkstemp(prefix="cjk-manifest-", suffix=".tmp", dir=root.parent)
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temp_name, root / MANIFEST)
    finally:
        if os.path.exists(temp_name):
            os.unlink(temp_name)
    return len(snapshots), sum(item.size for item in snapshots.values()), digest(payload)
