#!/usr/bin/env python3
"""Build the EGA IV r4 public artifacts and refresh the clean EGA bundle."""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import shutil
import zipfile
from pathlib import Path, PurePosixPath


REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_OLD_BUNDLE = (
    REPO_ROOT
    / "sources/ega/ega-current-readers-and-buildable-tex-bundle-20260801"
    / "00 Current_EGA_English_Readers_and_Buildable_TeX_20260801.zip"
)
DEFAULT_RELEASE_DIR = (
    REPO_ROOT / "sources/ega/ega4-complete-reference-v2-r4-20260801"
)
DEFAULT_BUNDLE_DIR = REPO_ROOT / (
    "sources/ega/ega-current-readers-and-buildable-tex-bundle-"
    "reference-v2-20260801"
)

EXPECTED_CANDIDATE_FILES = 84
EXPECTED_CANDIDATE_BYTES = 38_155_078
EXPECTED_CANDIDATE_AGGREGATE = (
    "CE9CFD708A5BBB1C21F406583DAB9ADD93D93FD936E5D98D316273C02A561209"
)
EXPECTED_MANIFEST_SHA256 = (
    "A8823F48D3FAE63AA5CED4299821E13BA01EF14B850618374EDB8B088C15D514"
)
EXPECTED_READER_SHA256 = (
    "6087FD9475DBDE908EA2025326BC7A49AF33583C7047A7D9332648D2B6387C7A"
)
EXPECTED_MASTER_SHA256 = (
    "2540AEBDC9F3339516B783AE014F3A33F94746341DC503D9E501F4DA873A5FB0"
)

READER_SOURCE = "EGA4_English_complete_reference_reader.pdf"
MASTER_SOURCE = "source/ega4.tex"
READER_PUBLIC = "EGA4_English_Complete_Reference_v2_Reader_20260801.pdf"
MASTER_PUBLIC = "EGA4_English_Complete_Reference_v2_Master_20260801.tex"
SOURCE_ZIP_PUBLIC = "EGA4_English_Complete_Reference_v2_TeX_PDF_QA_20260801.zip"
BUNDLE_PUBLIC = "00 Current_EGA_English_Readers_and_Buildable_TeX_20260801.zip"
ZIP_ROOT = "EGA4_English_Complete_Reference_v2_20260801"
BUNDLE_ROOT = "EGA_Current_English_Readers_and_TeX_20260801"
FIXED_ZIP_TIME = (2026, 8, 1, 0, 0, 0)

PRIVACY_PATTERNS = (
    b"C:" + b"\\Users\\",
    b"C:" + b"/Users/",
    b"/Users/",
    b"/home/",
    b"03_" + b"working_translations",
    b"AppData" + b"/Local/Temp",
    b"AppData" + b"\\Local\\Temp",
)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def sha256_path(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(4 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def csv_payload(header: tuple[str, ...], rows: list[tuple[object, ...]]) -> bytes:
    output = io.StringIO(newline="")
    writer = csv.writer(output, lineterminator="\n")
    writer.writerow(header)
    writer.writerows(rows)
    return output.getvalue().encode("utf-8")


def json_payload(value: object) -> bytes:
    return (json.dumps(value, indent=2, ensure_ascii=True) + "\n").encode("utf-8")


def validate_member_name(name: str) -> None:
    path = PurePosixPath(name)
    if (
        not name
        or name.startswith(("/", "\\"))
        or "\\" in name
        or path.is_absolute()
        or ".." in path.parts
        or (path.parts and ":" in path.parts[0])
    ):
        raise RuntimeError(f"Unsafe ZIP path: {name}")


def zip_info(name: str) -> zipfile.ZipInfo:
    validate_member_name(name)
    info = zipfile.ZipInfo(name, date_time=FIXED_ZIP_TIME)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.create_system = 3
    info.external_attr = 0o100644 << 16
    return info


def write_zip(path: Path, members: dict[str, bytes]) -> None:
    if path.exists():
        raise RuntimeError(f"Refusing to overwrite {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(path, "w") as archive:
        for name in sorted(members, key=str.casefold):
            archive.writestr(
                zip_info(name),
                members[name],
                compress_type=zipfile.ZIP_DEFLATED,
                compresslevel=9,
            )


def replay_zip(path: Path, expected: dict[str, bytes]) -> dict[str, object]:
    with zipfile.ZipFile(path) as archive:
        infos = archive.infolist()
        names = [info.filename for info in infos]
        for name in names:
            validate_member_name(name)
        if len(names) != len(set(names)):
            raise RuntimeError(f"Duplicate ZIP paths in {path}")
        if set(names) != set(expected):
            raise RuntimeError(f"ZIP member set mismatch in {path}")
        archive.testzip()
        mismatches = [name for name in names if archive.read(name) != expected[name]]
        if mismatches:
            raise RuntimeError(f"ZIP member mismatch in {path}: {mismatches[:3]}")
        return {
            "members": len(infos),
            "uncompressed_bytes": sum(info.file_size for info in infos),
            "unsafe_paths": 0,
            "duplicate_paths": 0,
            "member_mismatches": 0,
        }


def privacy_hits(members: dict[str, bytes]) -> list[dict[str, object]]:
    hits: list[dict[str, object]] = []
    for name, data in sorted(members.items(), key=lambda row: row[0].casefold()):
        for pattern in PRIVACY_PATTERNS:
            count = data.count(pattern)
            if count:
                hits.append(
                    {
                        "path": name,
                        "pattern": pattern.decode("ascii"),
                        "occurrences": count,
                    }
                )
    return hits


def candidate_files(root: Path) -> dict[str, bytes]:
    files = {
        path.relative_to(root).as_posix(): path.read_bytes()
        for path in root.rglob("*")
        if path.is_file()
    }
    if len(files) != EXPECTED_CANDIDATE_FILES:
        raise RuntimeError("EGA IV candidate file count changed")
    if sum(len(data) for data in files.values()) != EXPECTED_CANDIDATE_BYTES:
        raise RuntimeError("EGA IV candidate byte count changed")

    aggregate = hashlib.sha256()
    for name in sorted(files, key=str.casefold):
        data = files[name]
        aggregate.update(
            f"{name}\t{len(data)}\t{sha256_bytes(data)}\n".encode("utf-8")
        )
    if aggregate.hexdigest().upper() != EXPECTED_CANDIDATE_AGGREGATE:
        raise RuntimeError("EGA IV candidate aggregate changed")

    manifest_name = "ZENODO_PAYLOAD_MANIFEST.csv"
    if sha256_bytes(files[manifest_name]) != EXPECTED_MANIFEST_SHA256:
        raise RuntimeError("EGA IV candidate manifest changed")
    rows = list(csv.DictReader(io.StringIO(files[manifest_name].decode("utf-8-sig"))))
    listed = {row["relative_path"] for row in rows}
    if listed != set(files) - {manifest_name}:
        raise RuntimeError("EGA IV candidate manifest set mismatch")
    for row in rows:
        data = files[row["relative_path"]]
        if int(row["bytes"]) != len(data) or row["sha256"] != sha256_bytes(data):
            raise RuntimeError(f"EGA IV candidate identity mismatch: {row['relative_path']}")
    if sha256_bytes(files[READER_SOURCE]) != EXPECTED_READER_SHA256:
        raise RuntimeError("EGA IV reader identity changed")
    if sha256_bytes(files[MASTER_SOURCE]) != EXPECTED_MASTER_SHA256:
        raise RuntimeError("EGA IV master identity changed")
    hits = privacy_hits(files)
    if hits:
        raise RuntimeError(f"EGA IV candidate privacy hits: {hits[:3]}")
    return files


def build_source_release(
    candidate: dict[str, bytes], release_dir: Path
) -> dict[str, object]:
    reader_path = release_dir / READER_PUBLIC
    master_path = release_dir / MASTER_PUBLIC
    source_zip_path = release_dir / SOURCE_ZIP_PUBLIC
    for path in (reader_path, master_path, source_zip_path):
        if path.exists():
            raise RuntimeError(f"Refusing to overwrite {path}")
    reader_path.write_bytes(candidate[READER_SOURCE])
    master_path.write_bytes(candidate[MASTER_SOURCE])

    source_members = {f"{ZIP_ROOT}/{name}": data for name, data in candidate.items()}
    write_zip(source_zip_path, source_members)
    source_replay = replay_zip(source_zip_path, source_members)

    public_names = [
        "README.md",
        "INDEPENDENT_ARCHIVE_REPLAY.md",
        READER_PUBLIC,
        MASTER_PUBLIC,
        SOURCE_ZIP_PUBLIC,
    ]
    public_rows = []
    public_files = {}
    for name in public_names:
        data = (release_dir / name).read_bytes()
        public_files[name] = data
        public_rows.append((name, len(data), sha256_bytes(data)))
    outer_manifest = csv_payload(
        ("relative_path", "bytes", "sha256"), public_rows
    )
    (release_dir / "SHA256SUMS.csv").write_bytes(outer_manifest)

    validation = {
        "schema": "ega4_complete_reference_v2_release/v1",
        "status": "PASS",
        "errors": [],
        "candidate": {
            "files": EXPECTED_CANDIDATE_FILES,
            "bytes": EXPECTED_CANDIDATE_BYTES,
            "canonical_aggregate_sha256": EXPECTED_CANDIDATE_AGGREGATE,
            "manifest_rows": 83,
            "manifest_sha256": EXPECTED_MANIFEST_SHA256,
        },
        "reader": {
            "name": READER_PUBLIC,
            "bytes": len(candidate[READER_SOURCE]),
            "sha256": EXPECTED_READER_SHA256,
            "pages": 651,
            "named_destinations": 5_911,
            "goto_actions": 7_374,
            "broken_actions": 0,
        },
        "master": {
            "name": MASTER_PUBLIC,
            "bytes": len(candidate[MASTER_SOURCE]),
            "sha256": EXPECTED_MASTER_SHA256,
        },
        "source_zip": {
            "name": SOURCE_ZIP_PUBLIC,
            "bytes": source_zip_path.stat().st_size,
            "sha256": sha256_path(source_zip_path),
            **source_replay,
        },
        "outer_manifest": {
            "rows": len(public_rows),
            "bytes": len(outer_manifest),
            "sha256": sha256_bytes(outer_manifest),
        },
        "privacy_hits": [],
    }
    (release_dir / "PACKAGE_VALIDATION.json").write_bytes(json_payload(validation))
    return validation


def old_bundle_members(path: Path) -> dict[str, bytes]:
    with zipfile.ZipFile(path) as archive:
        infos = archive.infolist()
        names = [info.filename for info in infos]
        if len(names) != len(set(names)):
            raise RuntimeError("Existing EGA bundle has duplicate members")
        for name in names:
            validate_member_name(name)
        archive.testzip()
        return {name: archive.read(name) for name in names}


def build_current_bundle(
    candidate: dict[str, bytes], old_bundle: Path, bundle_dir: Path
) -> dict[str, object]:
    old = old_bundle_members(old_bundle)
    ega4_prefix = f"{BUNDLE_ROOT}/EGAIV/"
    root_readme = f"{BUNDLE_ROOT}/README.md"
    root_sums = f"{BUNDLE_ROOT}/SHA256SUMS.csv"
    retained = {
        name: data
        for name, data in old.items()
        if not name.startswith(ega4_prefix) and name not in {root_readme, root_sums}
    }
    if len(retained) != 72:
        raise RuntimeError(f"Expected 72 retained bundle members, found {len(retained)}")

    members = dict(retained)
    reader_member = f"{ega4_prefix}reader/EGA4_English_Complete_Reference_v2_Reader.pdf"
    members[reader_member] = candidate[READER_SOURCE]
    ega4_readme = """# EGA IV complete English reference-v2 reader

The reader covers Sections 1-21 and all backmatter through EOF. Its source
directory contains the complete 59-file TeX closure. Cross-volume references
remain visible nonlinks; all 7,374 local GoTo actions resolve.

This is a source-aligned working translation, not a critical edition or a new
rights grant.
""".encode("utf-8")
    members[f"{ega4_prefix}README.md"] = ega4_readme

    tex_names = sorted(
        name for name in candidate if name.startswith("source/") and name.endswith(".tex")
    )
    if len(tex_names) != 59:
        raise RuntimeError(f"Expected 59 EGA IV TeX files, found {len(tex_names)}")
    for name in tex_names:
        members[f"{ega4_prefix}source/{name.removeprefix('source/')}"] = candidate[name]

    members[root_readme] = """# Current EGA English readers and TeX

This one-click bundle contains cumulative English working readers and complete
buildable TeX for EGA 0, I, II, the published EGA III text, and EGA IV through
EOF. EGA IV is the 651-page complete reference-v2 successor.

These are working translations, not critical editions or new rights grants.
""".encode("utf-8")

    internal_rows = [
        (name, len(data), sha256_bytes(data))
        for name, data in sorted(members.items(), key=lambda row: row[0].casefold())
    ]
    members[root_sums] = csv_payload(
        ("relative_path", "bytes", "sha256"), internal_rows
    )
    if len(members) != 135:
        raise RuntimeError(f"Expected 135 current-bundle members, found {len(members)}")
    hits = privacy_hits(members)
    if hits:
        raise RuntimeError(f"Current EGA bundle privacy hits: {hits[:3]}")

    bundle_path = bundle_dir / BUNDLE_PUBLIC
    write_zip(bundle_path, members)
    replay = replay_zip(bundle_path, members)
    retained_errors = [name for name, data in retained.items() if old[name] != data]
    if retained_errors:
        raise RuntimeError("Retained EGA bundle identities changed")

    external_rows = [
        (name, len(data), sha256_bytes(data))
        for name, data in sorted(members.items(), key=lambda row: row[0].casefold())
    ]
    ledger = csv_payload(("zip_member_path", "bytes", "sha256"), external_rows)
    (bundle_dir / "ZIP_MEMBER_SHA256SUMS.csv").write_bytes(ledger)
    validation = {
        "schema": "ega_current_reader_bundle_validation/v1",
        "status": "PASS",
        "errors": [],
        "zip": {
            "name": BUNDLE_PUBLIC,
            "bytes": bundle_path.stat().st_size,
            "sha256": sha256_path(bundle_path),
            **replay,
            "member_ledger_rows": len(external_rows),
            "member_ledger_sha256": sha256_bytes(ledger),
        },
        "preserved_predecessor": {
            "volumes": ["EGA0", "EGA1", "EGA2", "EGAIII"],
            "members": len(retained),
            "identity_errors": 0,
        },
        "ega4": {
            "reader_sha256": EXPECTED_READER_SHA256,
            "master_sha256": EXPECTED_MASTER_SHA256,
            "tex_files": len(tex_names),
            "members": 61,
        },
        "privacy": {"private_path_hits": 0},
    }
    (bundle_dir / "BUNDLE_VALIDATION.json").write_bytes(json_payload(validation))
    return validation


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidate-root", type=Path, required=True)
    parser.add_argument("--old-bundle", type=Path, default=DEFAULT_OLD_BUNDLE)
    parser.add_argument("--release-dir", type=Path, default=DEFAULT_RELEASE_DIR)
    parser.add_argument("--bundle-dir", type=Path, default=DEFAULT_BUNDLE_DIR)
    args = parser.parse_args()

    candidate = candidate_files(args.candidate_root.resolve())
    release = build_source_release(candidate, args.release_dir.resolve())
    bundle = build_current_bundle(
        candidate, args.old_bundle.resolve(), args.bundle_dir.resolve()
    )
    print(json.dumps({"release": release, "bundle": bundle}, indent=2))


if __name__ == "__main__":
    main()
