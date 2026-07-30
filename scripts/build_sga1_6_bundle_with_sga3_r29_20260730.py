#!/usr/bin/env python3
"""Refresh only the SGA3 subtree in the current SGA1-6 reader bundle."""

from __future__ import annotations

import csv
import hashlib
import io
import json
import zipfile
from pathlib import Path, PurePosixPath


REPO = Path(r"C:\w\e620")
BUNDLE_DIR = REPO / "sources/sga/sga1-6-current-readers-and-buildable-tex-bundle-20260730"
BUNDLE = BUNDLE_DIR / "00_Current_SGA1-6_English_Readers_and_Buildable_TeX_20260730.zip"
SGA3_DIR = REPO / "sources/sga/sga3-english-reader-clean-r29-complete-native-reference-v2-20260730"
SGA3_SOURCE_ZIP = SGA3_DIR / "10c_SGA3_English_Reader_and_Buildable_TeX_R29_20260730.zip"
ROOT = "SGA_Current_English_Readers_and_TeX_20260730"
ROOT_MANIFEST = f"{ROOT}/SHA256SUMS.csv"
ROOT_README = f"{ROOT}/README.md"
SGA3_PREFIX = f"{ROOT}/SGA3/"
ZIP_TIME = (2026, 7, 30, 15, 0, 0)
EXPECTED = {
    "old_members": 1_394,
    "old_sga3_members": 915,
    "new_sga3_members": 915,
    "reader_sha256": "FE7211BA4288E66430E64C574E808E9BAD596E99366777D2DDC2349CB9BD427C",
    "master_sha256": "B0106C64F7D3FB63F78A2F18C2684B27E14FDAD0D51B923EBA61F2A1980AF988",
}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def sha256_path(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(4 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def safe_member(name: str) -> bool:
    path = PurePosixPath(name)
    return (
        bool(name)
        and name == name.replace("\\", "/")
        and not path.is_absolute()
        and ".." not in path.parts
        and not (len(name) >= 2 and name[1] == ":")
    )


def zip_info(name: str) -> zipfile.ZipInfo:
    info = zipfile.ZipInfo(name, ZIP_TIME)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = 0o100644 << 16
    info.create_system = 3
    return info


def manifest_bytes(members: dict[str, bytes]) -> bytes:
    rows = ["relative_path,bytes,sha256\r\n"]
    for name in sorted(members, key=str.casefold):
        relative = name.removeprefix(f"{ROOT}/")
        data = members[name]
        rows.append(f'"{relative}",{len(data)},{sha256_bytes(data)}\r\n')
    return "".join(rows).encode("utf-8")


def replay_manifest(archive: zipfile.ZipFile) -> tuple[int, int]:
    infos = [info for info in archive.infolist() if not info.is_dir()]
    names = [info.filename for info in infos]
    if len(names) != len(set(names)) or not all(safe_member(name) for name in names):
        raise RuntimeError("bundle member boundary or safe-path check failed")
    if archive.testzip() is not None:
        raise RuntimeError("bundle CRC replay failed")
    rows = list(
        csv.DictReader(io.StringIO(archive.read(ROOT_MANIFEST).decode("utf-8-sig")))
    )
    by_name = {f"{ROOT}/{row['relative_path']}": row for row in rows}
    represented = set(names) - {ROOT_MANIFEST}
    if len(by_name) != len(rows) or set(by_name) != represented:
        raise RuntimeError("bundle manifest exact-set closure failed")
    for name in sorted(represented):
        data = archive.read(name)
        row = by_name[name]
        if (len(data), sha256_bytes(data)) != (
            int(row["bytes"]),
            row["sha256"].upper(),
        ):
            raise RuntimeError(f"bundle member identity mismatch: {name}")
    return len(names), len(rows)


def source_members() -> dict[str, bytes]:
    members: dict[str, bytes] = {}
    with zipfile.ZipFile(SGA3_SOURCE_ZIP) as archive:
        names = [info.filename for info in archive.infolist() if not info.is_dir()]
        if len(names) != 918 or archive.testzip() is not None:
            raise RuntimeError("SGA3 source ZIP boundary changed")
        for name in names:
            if name == "reader/SGA3_English_Reader.pdf":
                target = f"{SGA3_PREFIX}reader/SGA3_English_Reader.pdf"
            elif name == "source/SGA3_English_Master.tex":
                target = f"{SGA3_PREFIX}source/02c_SGA3_English_Master.tex"
            elif name.startswith("source/inputs/"):
                target = f"{SGA3_PREFIX}{name}"
            else:
                continue
            members[target] = archive.read(name)
    if len(members) != EXPECTED["new_sga3_members"]:
        raise RuntimeError("new SGA3 subtree member count changed")
    if sha256_bytes(members[f"{SGA3_PREFIX}reader/SGA3_English_Reader.pdf"]) != EXPECTED["reader_sha256"]:
        raise RuntimeError("new SGA3 reader identity changed")
    if sha256_bytes(members[f"{SGA3_PREFIX}source/02c_SGA3_English_Master.tex"]) != EXPECTED["master_sha256"]:
        raise RuntimeError("new SGA3 master identity changed")
    return members


def main() -> int:
    with zipfile.ZipFile(BUNDLE) as archive:
        old_member_count, old_manifest_rows = replay_manifest(archive)
        if old_member_count != EXPECTED["old_members"] or old_manifest_rows != 1_393:
            raise RuntimeError("existing bundle boundary changed")
        names = [info.filename for info in archive.infolist() if not info.is_dir()]
        old_sga3 = [name for name in names if name.startswith(SGA3_PREFIX)]
        if len(old_sga3) != EXPECTED["old_sga3_members"]:
            raise RuntimeError("existing SGA3 subtree boundary changed")
        members = {
            name: archive.read(name)
            for name in names
            if name not in {ROOT_MANIFEST, ROOT_README}
            and not name.startswith(SGA3_PREFIX)
        }
        preserved_subtrees = {
            number: {
                name: sha256_bytes(archive.read(name))
                for name in names
                if name.startswith(f"{ROOT}/SGA{number}/")
            }
            for number in (1, 2, 4, 5, 6)
        }

    members.update(source_members())
    inner_readme = """# Current SGA 1-6 English readers and buildable TeX

This one-click archive contains one cumulative English reader PDF and its
complete buildable TeX closure for each of SGA 1 through SGA 6. It omits
provenance archives, QA images, raw logs, historical releases, source scans,
and internal project notes.

The SGA3 subtree is the clean R29 complete reader: 1,470 A4 pages, native TeX
diagrams, 13,119 named destinations, and 12,337 valid internal GoTo actions.
The other five SGA subtrees are byte-identical to the preceding bundle.

Each subtree carries a direct cumulative PDF under `reader/` and a buildable
master plus recursive inputs under `source/`. `SHA256SUMS.csv` covers every
other archive member exactly.
"""
    members[ROOT_README] = inner_readme.encode("utf-8")
    members[ROOT_MANIFEST] = manifest_bytes(members)

    temporary = BUNDLE.with_suffix(BUNDLE.suffix + ".tmp")
    temporary.unlink(missing_ok=True)
    with zipfile.ZipFile(temporary, "w", allowZip64=True) as archive:
        for name in sorted(members, key=str.casefold):
            if not safe_member(name):
                raise RuntimeError(f"unsafe member: {name}")
            archive.writestr(zip_info(name), members[name], compresslevel=9)
    with zipfile.ZipFile(temporary) as archive:
        member_count, manifest_rows = replay_manifest(archive)
        if member_count != 1_394 or manifest_rows != 1_393:
            raise RuntimeError("refreshed bundle boundary changed")
        for number, identities in preserved_subtrees.items():
            observed = {
                name: sha256_bytes(archive.read(name)) for name in identities
            }
            if observed != identities:
                raise RuntimeError(f"SGA{number} subtree changed")
    temporary.replace(BUNDLE)

    result = {
        "schema": "sga1_6_current_bundle_sga3_r29_refresh_v1",
        "status": "PASS",
        "errors": [],
        "bundle": {
            "bytes": BUNDLE.stat().st_size,
            "sha256": sha256_path(BUNDLE),
            "members": member_count,
            "manifest_rows": manifest_rows,
        },
        "sga3": {
            "members": EXPECTED["new_sga3_members"],
            "reader_sha256": EXPECTED["reader_sha256"],
            "master_sha256": EXPECTED["master_sha256"],
            "pages": 1_470,
            "destinations": 13_119,
            "goto_actions": 12_337,
        },
        "preserved_byte_identically": {
            f"SGA{number}": len(identities)
            for number, identities in preserved_subtrees.items()
        },
    }
    (BUNDLE_DIR / "BUNDLE_VALIDATION.json").write_text(
        json.dumps(result, indent=2) + "\n", encoding="utf-8", newline="\n"
    )
    readme = f"""# SGA 1-6 Current English Reader Bundle

Public file:

- `00_Current_SGA1-6_English_Readers_and_Buildable_TeX_20260730.zip`
- {BUNDLE.stat().st_size:,} bytes
- SHA-256 `{sha256_path(BUNDLE)}`

The ZIP contains the current cumulative English reader PDFs and complete
build-source closures for SGA 1 through SGA 6. It has {member_count:,} readable
members: {manifest_rows:,} self-excluded manifest rows plus `SHA256SUMS.csv`.

The SGA3 subtree is the clean complete R29 reader: 1,470 A4 pages, native TeX
diagrams, 13,119 named destinations, 12,337 valid internal GoTo actions, and a
914-file buildable TeX closure. Its reader SHA-256 is
`{EXPECTED['reader_sha256']}`. SGA1, SGA2, SGA4, SGA5, and SGA6 remain
byte-identical to the preceding bundle.

The archive deliberately excludes provenance archives, QA imagery, machine
ledgers, build logs, historical releases, authority scans, and internal
project notes. Those remain separately preserved in the archive.

The refreshed ZIP replayed member by member with zero unsafe paths, CRC
failures, byte mismatches, or SHA-256 mismatches. On Zenodo this ZIP is
intended to sort first while a direct reader PDF remains the default preview.
"""
    (BUNDLE_DIR / "README.md").write_text(readme, encoding="utf-8", newline="\n")
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
