#!/usr/bin/env python3
"""Build the exact GitHub and compact Zenodo surfaces for EGA II reference-v2."""

from __future__ import annotations

import csv
import hashlib
import io
import json
import shutil
import zipfile
from pathlib import Path, PurePosixPath


REPO = Path(r"C:\w\e620")
SOURCE = Path(
    r"C:\Users\Floris\Documents\interlanguage\03_projects\language_management"
    r"\english_germanic\06_publication_candidates"
    r"\EGA2_English_complete_source_aligned_reference_v2_reader_20260730_r1"
)
CHECKPOINT = (
    REPO
    / "sources/ega/checkpoints/ega2-complete-reference-v2-r1-20260730"
)
SURFACE = REPO / "sources/ega/ega2-complete-reference-v2-release-20260730"
OLD_BUNDLE = (
    REPO
    / "sources/ega/ega-current-readers-and-buildable-tex-bundle-20260730"
    / "00 Current_EGA_English_Readers_and_Buildable_TeX_20260730.zip"
)
NEW_BUNDLE_DIR = (
    REPO
    / "sources/ega/ega-current-readers-and-buildable-tex-bundle-reference-v2-20260730"
)
NEW_BUNDLE = (
    NEW_BUNDLE_DIR
    / "00 Current_EGA_English_Readers_and_Buildable_TeX_20260730.zip"
)
SOURCE_ZIP = SURFACE / "10b_EGA2_English_Source_20260730.zip"
PDF = SURFACE / "00b_EGA2_English_Reader.pdf"
TEX = SURFACE / "02b_EGA2_English_Master.tex"

ROOT = "EGA_Current_English_Readers_and_TeX_20260730"
ROOT_README = f"{ROOT}/README.md"
ROOT_MANIFEST = f"{ROOT}/SHA256SUMS.csv"
EGA2_PREFIX = f"{ROOT}/EGA2/"
ZIP_TIME = (2026, 7, 30, 16, 30, 0)

EXPECTED_SOURCE = {
    "files": 51,
    "bytes": 8_173_871,
    "manifest_rows": 49,
    "manifest_sha256": (
        "5A173FD9FDA7DDE4B3427FC55857ACC9D48878ABC2A1D955C1E42D7E8457E0AC"
    ),
    "validation_sha256": (
        "98BF4A241A264503DF9AB0A7FE1924067D00AAD8E4174AA164ACC6CF4F616B4D"
    ),
    "pdf_bytes": 1_905_144,
    "pdf_sha256": (
        "16487005C6257BDA2FC8B2C872C153538DE73A8950CD9B26D772B6BE354FA78F"
    ),
    "master_bytes": 2_205,
    "master_sha256": (
        "D42280B6ECD1E0ECCB4812A5F902510E9DBF1BBCFB6965EEA7CED06E0199A525"
    ),
}
EXPECTED_OLD_BUNDLE = {
    "bytes": 5_802_085,
    "sha256": (
        "2CB037322063DF459EFC55CFCC9424E6F9EF4A6D59329C65FCE6F25715DAABA1"
    ),
    "members": 99,
    "manifest_rows": 98,
    "ega2_members": 15,
}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def sha256_path(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(4 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def identity(path: Path) -> dict[str, object]:
    return {
        "bytes": path.stat().st_size,
        "sha256": sha256_path(path),
    }


def safe_name(name: str) -> bool:
    path = PurePosixPath(name)
    return (
        bool(name)
        and name == name.replace("\\", "/")
        and not path.is_absolute()
        and ".." not in path.parts
        and not (path.parts and ":" in path.parts[0])
    )


def zip_info(name: str) -> zipfile.ZipInfo:
    info = zipfile.ZipInfo(name, ZIP_TIME)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = 0o100644 << 16
    info.create_system = 3
    return info


def csv_bytes(rows: list[dict[str, object]]) -> bytes:
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(
        stream,
        fieldnames=["relative_path", "bytes", "sha256"],
        lineterminator="\r\n",
    )
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue().encode("utf-8")


def rows_for_members(members: dict[str, bytes], prefix: str = "") -> bytes:
    rows = []
    for name in sorted(members, key=str.casefold):
        relative = name.removeprefix(prefix)
        data = members[name]
        rows.append(
            {
                "relative_path": relative,
                "bytes": len(data),
                "sha256": sha256_bytes(data),
            }
        )
    return csv_bytes(rows)


def source_files(root: Path) -> dict[str, Path]:
    return {
        path.relative_to(root).as_posix(): path
        for path in sorted(root.rglob("*"))
        if path.is_file()
    }


def validate_source(root: Path) -> dict[str, object]:
    files = source_files(root)
    if (len(files), sum(path.stat().st_size for path in files.values())) != (
        EXPECTED_SOURCE["files"],
        EXPECTED_SOURCE["bytes"],
    ):
        raise RuntimeError("EGA II payload boundary changed")
    manifest = root / "ZENODO_PAYLOAD_MANIFEST.csv"
    validation = root / "PACKAGE_VALIDATION.json"
    if sha256_path(manifest) != EXPECTED_SOURCE["manifest_sha256"]:
        raise RuntimeError("EGA II manifest identity changed")
    if sha256_path(validation) != EXPECTED_SOURCE["validation_sha256"]:
        raise RuntimeError("EGA II validation identity changed")
    rows = list(csv.DictReader(manifest.open(encoding="utf-8-sig", newline="")))
    represented = set(files) - {
        "ZENODO_PAYLOAD_MANIFEST.csv",
        "PACKAGE_VALIDATION.json",
    }
    if (
        len(rows) != EXPECTED_SOURCE["manifest_rows"]
        or len({row["relative_path"] for row in rows}) != len(rows)
        or {row["relative_path"] for row in rows} != represented
    ):
        raise RuntimeError("EGA II manifest exact set changed")
    for row in rows:
        path = files[row["relative_path"]]
        if (path.stat().st_size, sha256_path(path)) != (
            int(row["bytes"]),
            row["sha256"].upper(),
        ):
            raise RuntimeError(f"EGA II manifest mismatch: {row['relative_path']}")
    package = json.loads(validation.read_text(encoding="utf-8"))
    if package.get("status") != "PASS" or package.get("errors") != []:
        raise RuntimeError("EGA II package validator is not PASS")
    pdf = root / "EGA2_English_complete_reference_reader.pdf"
    master = root / "source/ega2.tex"
    if (pdf.stat().st_size, sha256_path(pdf)) != (
        EXPECTED_SOURCE["pdf_bytes"],
        EXPECTED_SOURCE["pdf_sha256"],
    ):
        raise RuntimeError("EGA II reader identity changed")
    if (master.stat().st_size, sha256_path(master)) != (
        EXPECTED_SOURCE["master_bytes"],
        EXPECTED_SOURCE["master_sha256"],
    ):
        raise RuntimeError("EGA II master identity changed")
    aggregate = hashlib.sha256()
    for name in sorted(files, key=str.casefold):
        path = files[name]
        aggregate.update(
            f"{name}\t{path.stat().st_size}\t{sha256_path(path)}\n".encode()
        )
    return {
        "files": len(files),
        "bytes": sum(path.stat().st_size for path in files.values()),
        "manifest_rows": len(rows),
        "canonical_tree_sha256": aggregate.hexdigest().upper(),
    }


def copy_checkpoint() -> None:
    if CHECKPOINT.exists():
        if validate_source(CHECKPOINT) != validate_source(SOURCE):
            raise RuntimeError("Existing GitHub checkpoint differs from payload")
        return
    CHECKPOINT.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(SOURCE, CHECKPOINT)
    if validate_source(CHECKPOINT) != validate_source(SOURCE):
        raise RuntimeError("GitHub checkpoint copy replay failed")


def build_source_zip() -> dict[str, object]:
    SURFACE.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE / "EGA2_English_complete_reference_reader.pdf", PDF)
    shutil.copyfile(SOURCE / "source/ega2.tex", TEX)
    members = source_files(SOURCE)
    temporary = SOURCE_ZIP.with_suffix(".zip.tmp")
    temporary.unlink(missing_ok=True)
    with zipfile.ZipFile(temporary, "w", allowZip64=True) as archive:
        for name in sorted(members, key=str.casefold):
            if not safe_name(name):
                raise RuntimeError(f"Unsafe EGA II member: {name}")
            archive.writestr(zip_info(name), members[name].read_bytes(), compresslevel=9)
    with zipfile.ZipFile(temporary) as archive:
        infos = [row for row in archive.infolist() if not row.is_dir()]
        if (
            len(infos) != EXPECTED_SOURCE["files"]
            or sum(row.file_size for row in infos) != EXPECTED_SOURCE["bytes"]
            or archive.testzip() is not None
        ):
            raise RuntimeError("EGA II source ZIP boundary or CRC failure")
        for name, path in members.items():
            data = archive.read(name)
            if (len(data), sha256_bytes(data)) != (
                path.stat().st_size,
                sha256_path(path),
            ):
                raise RuntimeError(f"EGA II source ZIP mismatch: {name}")
    temporary.replace(SOURCE_ZIP)
    return {
        **identity(SOURCE_ZIP),
        "members": len(members),
        "uncompressed_bytes": EXPECTED_SOURCE["bytes"],
    }


def replay_bundle(archive: zipfile.ZipFile) -> tuple[int, int]:
    infos = [row for row in archive.infolist() if not row.is_dir()]
    names = [row.filename for row in infos]
    if (
        len(names) != len(set(names))
        or not all(safe_name(name) for name in names)
        or archive.testzip() is not None
    ):
        raise RuntimeError("EGA bundle safe-path, duplicate, or CRC failure")
    rows = list(
        csv.DictReader(io.StringIO(archive.read(ROOT_MANIFEST).decode("utf-8-sig")))
    )
    represented = set(names) - {ROOT_MANIFEST}
    mapped = {f"{ROOT}/{row['relative_path']}": row for row in rows}
    if len(mapped) != len(rows) or set(mapped) != represented:
        raise RuntimeError("EGA bundle manifest exact-set failure")
    for name, row in mapped.items():
        data = archive.read(name)
        if (len(data), sha256_bytes(data)) != (
            int(row["bytes"]),
            row["sha256"].upper(),
        ):
            raise RuntimeError(f"EGA bundle member mismatch: {name}")
    return len(names), len(rows)


def build_bundle() -> dict[str, object]:
    if (OLD_BUNDLE.stat().st_size, sha256_path(OLD_BUNDLE)) != (
        EXPECTED_OLD_BUNDLE["bytes"],
        EXPECTED_OLD_BUNDLE["sha256"],
    ):
        raise RuntimeError("Current EGA bundle identity changed")
    with zipfile.ZipFile(OLD_BUNDLE) as archive:
        if replay_bundle(archive) != (
            EXPECTED_OLD_BUNDLE["members"],
            EXPECTED_OLD_BUNDLE["manifest_rows"],
        ):
            raise RuntimeError("Current EGA bundle boundary changed")
        names = [row.filename for row in archive.infolist() if not row.is_dir()]
        old_ega2 = [name for name in names if name.startswith(EGA2_PREFIX)]
        if len(old_ega2) != EXPECTED_OLD_BUNDLE["ega2_members"]:
            raise RuntimeError("Current EGA2 bundle subtree changed")
        preserved = {
            name: archive.read(name)
            for name in names
            if name not in {ROOT_README, ROOT_MANIFEST}
            and not name.startswith(EGA2_PREFIX)
        }
        preserved_hashes = {
            name: sha256_bytes(data) for name, data in preserved.items()
        }

    members = dict(preserved)
    members[f"{EGA2_PREFIX}reader/EGA2_English_Reader.pdf"] = (
        SOURCE / "EGA2_English_complete_reference_reader.pdf"
    ).read_bytes()
    for path in sorted((SOURCE / "source").rglob("*.tex")):
        relative = path.relative_to(SOURCE / "source").as_posix()
        members[f"{EGA2_PREFIX}source/{relative}"] = path.read_bytes()
    if len([name for name in members if name.startswith(EGA2_PREFIX)]) != 15:
        raise RuntimeError("New EGA2 bundle subtree does not have 15 members")
    readme = """# Current EGA English readers and buildable TeX

This one-click archive contains one cumulative English reader PDF and its
complete buildable TeX closure for every current EGA scope on the public
record: EGA 0/III Sections 8-13, complete EGA II through authority EOF, EGA
III Sections 1-7, and EGA IV Sections 1-10.

The EGA II subtree is the complete source-aligned reference-v2 successor: 165
letter pages, 1,028 stable targets, 2,078 valid internal GoTo actions, and
2,538 named destinations. The EGA 0, EGA III, and EGA IV subtrees are
byte-identical to the preceding bundle.

The archive excludes provenance archives, QA images, raw logs, authority
scans, historical releases, and project-production notes. `SHA256SUMS.csv`
covers every other member exactly.
"""
    members[ROOT_README] = readme.encode("utf-8")
    manifest_members = dict(members)
    members[ROOT_MANIFEST] = rows_for_members(
        manifest_members, prefix=f"{ROOT}/"
    )

    NEW_BUNDLE_DIR.mkdir(parents=True, exist_ok=True)
    temporary = NEW_BUNDLE.with_suffix(".zip.tmp")
    temporary.unlink(missing_ok=True)
    with zipfile.ZipFile(temporary, "w", allowZip64=True) as archive:
        for name in sorted(members, key=str.casefold):
            archive.writestr(zip_info(name), members[name], compresslevel=9)
    with zipfile.ZipFile(temporary) as archive:
        if replay_bundle(archive) != (99, 98):
            raise RuntimeError("Refreshed EGA bundle boundary changed")
        for name, wanted in preserved_hashes.items():
            if sha256_bytes(archive.read(name)) != wanted:
                raise RuntimeError(f"Preserved EGA bundle member changed: {name}")
    temporary.replace(NEW_BUNDLE)
    return {
        **identity(NEW_BUNDLE),
        "members": 99,
        "manifest_rows": 98,
        "uncompressed_bytes": sum(len(data) for data in members.values()),
        "preserved_members": len(preserved_hashes),
        "replaced_ega2_members": 15,
    }


def write_surface_controls(
    source_validation: dict[str, object],
    source_zip: dict[str, object],
    bundle: dict[str, object],
) -> dict[str, object]:
    readme = f"""# EGA II Complete Reference-v2 Release

This release surface exposes the complete 165-page source-aligned EGA II
working reader, its editable master TeX, and one exact 51-member source,
reference, build-evidence, and QA ZIP. The broader all-current EGA bundle is
maintained separately and now carries the same EGA II reader and complete
14-file buildable source closure.

Reader SHA-256: `{EXPECTED_SOURCE['pdf_sha256']}`.
Master SHA-256: `{EXPECTED_SOURCE['master_sha256']}`.
Source ZIP SHA-256: `{source_zip['sha256']}`.

The package is not a critical edition, peer review, mathematical or
accessibility certification, or rights-clearance determination. No blanket
license is asserted; rights remain with their respective holders.
"""
    (SURFACE / "README.md").write_text(readme, encoding="utf-8", newline="\n")
    validation = {
        "schema": "ega2-reference-v2-public-release-preparation-1.0",
        "status": "PASS",
        "errors": [],
        "source_payload": source_validation,
        "direct_reader": identity(PDF),
        "direct_master": identity(TEX),
        "source_zip": source_zip,
        "current_reader_bundle": bundle,
        "scope": "Complete EGA II through authority EOF",
        "reader_pages": 165,
        "targets": 1_028,
        "goto_actions": 2_078,
        "named_destinations": 2_538,
        "default_preview_unchanged": (
            "00a_EGA0_English_Working_Reader_Assigned_SourceFirst_"
            "Sections8_13_20260729.pdf"
        ),
    }
    (SURFACE / "RELEASE_VALIDATION.json").write_text(
        json.dumps(validation, ensure_ascii=True, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    represented = {
        path.name: path.read_bytes()
        for path in sorted(SURFACE.iterdir())
        if path.is_file() and path.name != "SHA256SUMS.csv"
    }
    (SURFACE / "SHA256SUMS.csv").write_bytes(rows_for_members(represented))
    return validation


def main() -> int:
    source_validation = validate_source(SOURCE)
    copy_checkpoint()
    source_zip = build_source_zip()
    bundle = build_bundle()
    validation = write_surface_controls(source_validation, source_zip, bundle)
    (NEW_BUNDLE_DIR / "BUNDLE_VALIDATION.json").write_text(
        json.dumps(bundle, indent=2) + "\n", encoding="utf-8", newline="\n"
    )
    (NEW_BUNDLE_DIR / "README.md").write_text(
        "# Current EGA Reader Bundle: EGA II Reference-v2 Refresh\n\n"
        f"The 99-member ZIP is {bundle['bytes']:,} bytes with SHA-256 "
        f"`{bundle['sha256']}`. EGA II is replaced by the complete 165-page "
        "reference-v2 successor; all 82 non-EGA-II reader/source members are "
        "byte-identical to the preceding bundle.\n",
        encoding="utf-8",
        newline="\n",
    )
    result = {
        "status": "PASS",
        "errors": [],
        "checkpoint": source_validation,
        "source_zip": source_zip,
        "bundle": bundle,
        "surface_validation": validation,
    }
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
