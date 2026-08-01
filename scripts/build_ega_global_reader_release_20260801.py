#!/usr/bin/env python3
"""Build the complete linked EGA 0-IV reader release and compact bundle."""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import os
import tempfile
import zipfile
from pathlib import Path, PurePosixPath


REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_PRODUCER_ROOT = Path(
    r"C:\Users\Floris\Documents\interlanguage\03_projects\language_management"
    r"\english_germanic\03_working_translations"
    r"\ega_english_global_0_IV_complete_linked_reader_20260801_r1"
)
DEFAULT_BUNDLE_DIR = REPO_ROOT / (
    "sources/ega/ega-current-readers-and-buildable-tex-bundle-"
    "reference-v2-20260801"
)
DEFAULT_RELEASE_DIR = REPO_ROOT / (
    "sources/ega/ega-global-complete-linked-reader-20260801"
)

BUNDLE_NAME = "00 Current_EGA_English_Readers_and_Buildable_TeX_20260801.zip"
GLOBAL_PDF_NAME = "00_GLOBAL_EGA_0_IV_English_Complete_Linked_Reader_20260801.pdf"
GLOBAL_TEX_NAME = "01_GLOBAL_EGA_0_IV_English_Complete_Linked_Master_20260801.tex"
README_CONTROL = "90 EGA - README and Status.md"
SUMMARY_CONTROL = "91 EGA - Public Summary.json"
SUMS_CONTROL = "92 EGA - Current File SHA256SUMS.csv"

BUNDLE_ROOT = "EGA_Current_English_Readers_and_TeX_20260801"
GLOBAL_ROOT = f"{BUNDLE_ROOT}/EGA_Global_0_IV"
ROOT_README = f"{BUNDLE_ROOT}/README.md"
ROOT_SUMS = f"{BUNDLE_ROOT}/SHA256SUMS.csv"
FIXED_ZIP_TIME = (2026, 8, 1, 0, 0, 0)

EXPECTED_ROOT_FILES = 197
EXPECTED_ROOT_BYTES = 80_125_530
EXPECTED_SOURCE_ROWS = 127
EXPECTED_SOURCE_BYTES = 7_279_735
EXPECTED_SOURCE_MANIFEST_SHA256 = (
    "E5614FC0F8DF1E1CFC39EDA6C921ADC8513949BA05B4FB7875C93B619A2944F5"
)
EXPECTED_MASTER_BYTES = 1_688
EXPECTED_MASTER_SHA256 = (
    "8147C8FDB1B5EBEA69FDB02AA7C192F8267CCA9ABE887AFD3B11B179CE7A7CC1"
)
EXPECTED_READER_BYTES = 8_588_550
EXPECTED_READER_SHA256 = (
    "3B9D399515AA074C22D3DF6C6F0F7349954444D7BCF980B87CCE5CAED671928A"
)
EXPECTED_READER_PAGES = 1_356
EXPECTED_DESTINATIONS = 15_383
EXPECTED_GOTO_ACTIONS = 17_808

STANDALONE_READERS = {
    "00a_EGA0_English_Complete_Through_Section13_Reference_v2_20260730.pdf": {
        "bundle_member": f"{BUNDLE_ROOT}/EGA0/reader/00a_EGA0_English_Complete_Through_Section13_Reference_v2_20260730.pdf",
        "pages": 120,
    },
    "00b_EGA1_English_Complete_Reference_v2_Reader_20260730.pdf": {
        "bundle_member": f"{BUNDLE_ROOT}/EGA1/reader/00b_EGA1_English_Complete_Reference_v2_Reader_20260730.pdf",
        "pages": 113,
    },
    "00c_EGA2_English_Complete_Reference_v2_Reader_20260730.pdf": {
        "bundle_member": f"{BUNDLE_ROOT}/EGA2/reader/00c_EGA2_English_Complete_Reference_v2_Reader_20260730.pdf",
        "pages": 165,
    },
    "00d_EGAIII_English_Published_Text_Complete_Reference_v2_20260730.pdf": {
        "bundle_member": f"{BUNDLE_ROOT}/EGAIII/reader/00d_EGAIII_English_Published_Text_Complete_Reference_v2_20260730.pdf",
        "pages": 150,
    },
    "00e_EGAIV_English_Complete_Reference_v2_Reader_20260801.pdf": {
        "bundle_member": f"{BUNDLE_ROOT}/EGAIV/reader/EGA4_English_Complete_Reference_v2_Reader.pdf",
        "pages": 651,
    },
}

STANDALONE_MASTERS = {
    "01a_EGA0_English_Master_20260730.tex": f"{BUNDLE_ROOT}/EGA0/source/ega0.tex",
    "01b_EGA1_English_Master_20260730.tex": f"{BUNDLE_ROOT}/EGA1/source/ega1.tex",
    "01c_EGA2_English_Master_20260730.tex": f"{BUNDLE_ROOT}/EGA2/source/ega2.tex",
    "01d_EGAIII_English_Master_20260730.tex": f"{BUNDLE_ROOT}/EGAIII/source/ega3.tex",
    "01e_EGAIV_English_Complete_Reference_v2_Master_20260801.tex": f"{BUNDLE_ROOT}/EGAIV/source/ega4.tex",
}

PRIVACY_PATTERNS = (
    b"C:" + b"\\Users\\",
    b"C:" + b"/Users/",
    b"/Users/",
    b"/home/",
    b"03_" + b"working_translations",
    b"AppData" + b"/Local/Temp",
    b"AppData" + b"\\Local\\Temp",
    b"Claude" + b"-aid",
)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def sha256_path(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(4 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def csv_bytes(header: tuple[str, ...], rows: list[tuple[object, ...]]) -> bytes:
    output = io.StringIO(newline="")
    writer = csv.writer(output, lineterminator="\n")
    writer.writerow(header)
    writer.writerows(rows)
    return output.getvalue().encode("utf-8")


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, indent=2, ensure_ascii=True) + "\n").encode("utf-8")


def validate_zip_name(name: str) -> None:
    pure = PurePosixPath(name)
    if (
        not name
        or name.startswith(("/", "\\"))
        or "\\" in name
        or pure.is_absolute()
        or ".." in pure.parts
        or (pure.parts and ":" in pure.parts[0])
    ):
        raise RuntimeError(f"Unsafe ZIP path: {name}")


def zip_info(name: str) -> zipfile.ZipInfo:
    validate_zip_name(name)
    info = zipfile.ZipInfo(name, date_time=FIXED_ZIP_TIME)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.create_system = 3
    info.external_attr = 0o100644 << 16
    return info


def write_zip(path: Path, members: dict[str, bytes]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp_name = tempfile.mkstemp(prefix=path.name + ".", suffix=".tmp", dir=path.parent)
    os.close(fd)
    temp = Path(temp_name)
    try:
        with zipfile.ZipFile(temp, "w") as archive:
            for name in sorted(members, key=str.casefold):
                archive.writestr(
                    zip_info(name),
                    members[name],
                    compress_type=zipfile.ZIP_DEFLATED,
                    compresslevel=9,
                )
        replay_zip(temp, members)
        temp.replace(path)
    finally:
        temp.unlink(missing_ok=True)


def replay_zip(path: Path, expected: dict[str, bytes]) -> dict[str, object]:
    with zipfile.ZipFile(path) as archive:
        infos = [info for info in archive.infolist() if not info.is_dir()]
        names = [info.filename for info in infos]
        for name in names:
            validate_zip_name(name)
        if len(names) != len(set(names)):
            raise RuntimeError(f"Duplicate ZIP paths: {path}")
        if set(names) != set(expected):
            raise RuntimeError(f"ZIP member set mismatch: {path}")
        if archive.testzip() is not None:
            raise RuntimeError(f"ZIP CRC failure: {path}")
        mismatches = [name for name in names if archive.read(name) != expected[name]]
        if mismatches:
            raise RuntimeError(f"ZIP byte mismatch: {mismatches[:3]}")
        return {
            "members": len(infos),
            "uncompressed_bytes": sum(info.file_size for info in infos),
            "unsafe_paths": 0,
            "duplicate_paths": 0,
            "member_mismatches": 0,
        }


def read_zip(path: Path) -> dict[str, bytes]:
    with zipfile.ZipFile(path) as archive:
        infos = [info for info in archive.infolist() if not info.is_dir()]
        names = [info.filename for info in infos]
        for name in names:
            validate_zip_name(name)
        if len(names) != len(set(names)) or archive.testzip() is not None:
            raise RuntimeError("Existing EGA bundle is not replay-safe")
        return {name: archive.read(name) for name in names}


def privacy_hits(files: dict[str, bytes]) -> list[dict[str, object]]:
    hits: list[dict[str, object]] = []
    for name, data in sorted(files.items(), key=lambda row: row[0].casefold()):
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


def producer_files(root: Path) -> tuple[dict[str, bytes], dict[str, bytes]]:
    all_files = {
        path.relative_to(root).as_posix(): path.read_bytes()
        for path in root.rglob("*")
        if path.is_file()
    }
    if len(all_files) != EXPECTED_ROOT_FILES or sum(map(len, all_files.values())) != EXPECTED_ROOT_BYTES:
        raise RuntimeError("Frozen EGA global root changed")

    manifest_name = "controls/ACTIVE_SOURCE_SHA256.csv"
    manifest = all_files[manifest_name]
    if len(manifest) != 13_797 or sha256_bytes(manifest) != EXPECTED_SOURCE_MANIFEST_SHA256:
        raise RuntimeError("Frozen EGA active-source manifest changed")
    rows = list(csv.DictReader(io.StringIO(manifest.decode("utf-8-sig"))))
    if len(rows) != EXPECTED_SOURCE_ROWS:
        raise RuntimeError("Frozen EGA source row count changed")
    source: dict[str, bytes] = {}
    for row in rows:
        name = row["path"]
        data = all_files.get(name)
        if data is None:
            raise RuntimeError(f"Missing EGA source member: {name}")
        if int(row["bytes"]) != len(data) or row["sha256"].upper() != sha256_bytes(data):
            raise RuntimeError(f"EGA source identity mismatch: {name}")
        source[name] = data
    if sum(map(len, source.values())) != EXPECTED_SOURCE_BYTES:
        raise RuntimeError("Frozen EGA source byte boundary changed")
    if privacy_hits(source):
        raise RuntimeError("Frozen EGA active source has a private-path hit")

    master = source["source/EGA_English_Global_0_IV.tex"]
    reader = all_files["build/EGA_English_Global_0_IV.pdf"]
    if (len(master), sha256_bytes(master)) != (EXPECTED_MASTER_BYTES, EXPECTED_MASTER_SHA256):
        raise RuntimeError("Frozen EGA global master changed")
    if (len(reader), sha256_bytes(reader)) != (EXPECTED_READER_BYTES, EXPECTED_READER_SHA256):
        raise RuntimeError("Frozen EGA global reader changed")
    if privacy_hits({"reader.pdf": reader}):
        raise RuntimeError("Frozen EGA global PDF has a private-path hit")
    return all_files, source


def build_bundle(
    source: dict[str, bytes], reader: bytes, old_bundle: Path, bundle_dir: Path
) -> tuple[dict[str, object], dict[str, bytes]]:
    old = read_zip(old_bundle)
    if len(old) != 135:
        raise RuntimeError("Existing EGA compact bundle boundary changed")
    retained = {name: data for name, data in old.items() if name not in {ROOT_README, ROOT_SUMS}}
    if len(retained) != 133:
        raise RuntimeError("Existing EGA compact bundle control boundary changed")

    members = dict(retained)
    members[f"{GLOBAL_ROOT}/reader/EGA_English_Global_0_IV_Complete_Linked_Reader_20260801.pdf"] = reader
    for name, data in source.items():
        members[f"{GLOBAL_ROOT}/{name}"] = data
    members[f"{GLOBAL_ROOT}/SOURCE_SHA256SUMS.csv"] = csv_bytes(
        ("relative_path", "bytes", "sha256"),
        [
            (name, len(data), sha256_bytes(data))
            for name, data in sorted(source.items(), key=lambda row: row[0].casefold())
        ],
    )
    members[f"{GLOBAL_ROOT}/README.md"] = (
        "# EGA 0-IV complete linked English reader\n\n"
        "Open the PDF in `reader/` for one continuous EGA 0-IV reader. The\n"
        "`source/` directory is its complete buildable TeX closure. Internal\n"
        "links work within and across the five volumes.\n\n"
        "This is a working English reader, not a critical edition or a new\n"
        "rights grant.\n"
    ).encode("ascii")
    members[ROOT_README] = (
        "# Current EGA English readers and buildable TeX\n\n"
        "Start with `EGA_Global_0_IV/reader/` for one continuous EGA 0-IV PDF.\n"
        "The EGA0, EGA1, EGA2, EGAIII, and EGAIV directories contain the five\n"
        "standalone readers. Every reader has its complete buildable TeX here.\n\n"
        "These are working English readers, not critical editions or new\n"
        "rights grants.\n"
    ).encode("ascii")
    root_rows = [
        (name, len(data), sha256_bytes(data))
        for name, data in sorted(members.items(), key=lambda row: row[0].casefold())
    ]
    members[ROOT_SUMS] = csv_bytes(("relative_path", "bytes", "sha256"), root_rows)
    if len(members) != 265:
        raise RuntimeError(f"Expected 265 EGA bundle members, found {len(members)}")
    hits = privacy_hits(members)
    if hits:
        raise RuntimeError(f"EGA compact bundle privacy hits: {hits[:3]}")

    bundle_path = bundle_dir / BUNDLE_NAME
    write_zip(bundle_path, members)
    replay = replay_zip(bundle_path, members)
    retained_errors = [name for name, data in retained.items() if old[name] != data]
    if retained_errors:
        raise RuntimeError("Existing standalone EGA bundle member drift")

    ledger_rows = [
        (name, len(data), sha256_bytes(data))
        for name, data in sorted(members.items(), key=lambda row: row[0].casefold())
    ]
    ledger = csv_bytes(("zip_member_path", "bytes", "sha256"), ledger_rows)
    (bundle_dir / "ZIP_MEMBER_SHA256SUMS.csv").write_bytes(ledger)
    validation = {
        "schema": "ega_current_reader_bundle_validation/v2",
        "status": "PASS",
        "errors": [],
        "zip": {
            "name": BUNDLE_NAME,
            "bytes": bundle_path.stat().st_size,
            "sha256": sha256_path(bundle_path),
            **replay,
            "member_ledger_rows": len(ledger_rows),
            "member_ledger_sha256": sha256_bytes(ledger),
        },
        "global_reader": {
            "pages": EXPECTED_READER_PAGES,
            "bytes": EXPECTED_READER_BYTES,
            "sha256": EXPECTED_READER_SHA256,
            "source_files": EXPECTED_SOURCE_ROWS,
            "source_bytes": EXPECTED_SOURCE_BYTES,
            "source_manifest_sha256": EXPECTED_SOURCE_MANIFEST_SHA256,
        },
        "standalone_reader_members_retained_exact": 5,
        "predecessor_members_retained_exact": len(retained),
        "privacy_hits": [],
    }
    (bundle_dir / "BUNDLE_VALIDATION.json").write_bytes(json_bytes(validation))
    (bundle_dir / "README.md").write_text(
        "# Current EGA English readers and buildable TeX\n\n"
        "One ZIP containing the complete linked EGA 0-IV reader, the five\n"
        "standalone readers, and the buildable TeX for all six reader surfaces.\n",
        encoding="ascii",
        newline="\n",
    )
    (bundle_dir / ".gitattributes").write_text("* -text\n", encoding="ascii", newline="\n")
    return validation, members


def build_release(
    source: dict[str, bytes], reader: bytes, bundle_dir: Path, release_dir: Path, bundle_members: dict[str, bytes]
) -> dict[str, object]:
    if release_dir.exists():
        raise RuntimeError(f"Refusing to overwrite release directory: {release_dir}")
    release_dir.mkdir(parents=True)
    (release_dir / ".gitattributes").write_text("* -text\n", encoding="ascii", newline="\n")
    (release_dir / GLOBAL_PDF_NAME).write_bytes(reader)
    master = source["source/EGA_English_Global_0_IV.tex"]
    (release_dir / GLOBAL_TEX_NAME).write_bytes(master)

    standalone_reader_rows = []
    for public_name, spec in STANDALONE_READERS.items():
        data = bundle_members[str(spec["bundle_member"])]
        standalone_reader_rows.append(
            {
                "name": public_name,
                "pages": int(spec["pages"]),
                "bytes": len(data),
                "sha256": sha256_bytes(data),
            }
        )
    standalone_master_rows = []
    for public_name, member in STANDALONE_MASTERS.items():
        data = bundle_members[member]
        standalone_master_rows.append(
            {"name": public_name, "bytes": len(data), "sha256": sha256_bytes(data)}
        )

    readme = (
        "# EGA English readers\n\n"
        "Open `00_GLOBAL_EGA_0_IV_English_Complete_Linked_Reader_20260801.pdf`\n"
        "for one continuous, internally linked EGA 0-IV reader. The five\n"
        "standalone volume readers remain directly available. Download\n"
        "`00 Current_EGA_English_Readers_and_Buildable_TeX_20260801.zip` for\n"
        "all six readers and their complete buildable TeX.\n\n"
        "Coverage: EGA 0 through Section 13; EGA I and II through EOF; the\n"
        "published EGA III text through 7.9.14; and EGA IV Sections 1-21\n"
        "through EOF. These are working English readers, not critical editions\n"
        "or new rights grants.\n"
    ).encode("ascii")
    (release_dir / README_CONTROL).write_bytes(readme)

    bundle_path = bundle_dir / BUNDLE_NAME
    summary = {
        "schema": "ega_public_reader_summary/v3",
        "date": "2026-08-01",
        "status": "CURRENT_COMPLETE_ENGLISH_READER_SURFACE",
        "global_reader": {
            "name": GLOBAL_PDF_NAME,
            "default_preview": True,
            "scope": "EGA 0, I, II, III, and IV",
            "pages": EXPECTED_READER_PAGES,
            "bytes": EXPECTED_READER_BYTES,
            "sha256": EXPECTED_READER_SHA256,
            "named_destinations": EXPECTED_DESTINATIONS,
            "goto_actions": EXPECTED_GOTO_ACTIONS,
            "broken_actions": 0,
        },
        "standalone_readers": standalone_reader_rows,
        "bundle": {
            "name": BUNDLE_NAME,
            "bytes": bundle_path.stat().st_size,
            "sha256": sha256_path(bundle_path),
            "members": len(bundle_members),
            "uncompressed_bytes": sum(map(len, bundle_members.values())),
            "contains": "global reader, five standalone readers, and complete buildable TeX",
        },
        "rights": "Working English readers; no blanket license or critical-edition claim.",
    }
    (release_dir / SUMMARY_CONTROL).write_bytes(json_bytes(summary))

    current_rows: list[tuple[object, ...]] = [
        (BUNDLE_NAME, bundle_path.stat().st_size, sha256_path(bundle_path), "current_reader_and_tex_bundle"),
        (GLOBAL_PDF_NAME, len(reader), sha256_bytes(reader), "default_global_reader"),
        (GLOBAL_TEX_NAME, len(master), sha256_bytes(master), "global_master_tex"),
    ]
    for row in standalone_reader_rows:
        current_rows.append((row["name"], row["bytes"], row["sha256"], "standalone_reader"))
    for row in standalone_master_rows:
        current_rows.append((row["name"], row["bytes"], row["sha256"], "standalone_master_tex"))
    sums = csv_bytes(("filename", "bytes", "sha256", "role"), current_rows)
    (release_dir / SUMS_CONTROL).write_bytes(sums)

    (release_dir / "README.md").write_bytes(readme)
    outer_names = [
        "README.md",
        GLOBAL_PDF_NAME,
        GLOBAL_TEX_NAME,
        README_CONTROL,
        SUMMARY_CONTROL,
        SUMS_CONTROL,
    ]
    outer_rows = []
    for name in outer_names:
        data = (release_dir / name).read_bytes()
        outer_rows.append((name, len(data), sha256_bytes(data)))
    outer = csv_bytes(("relative_path", "bytes", "sha256"), outer_rows)
    (release_dir / "SHA256SUMS.csv").write_bytes(outer)

    zenodo_paths = {
        BUNDLE_NAME: bundle_path,
        GLOBAL_PDF_NAME: release_dir / GLOBAL_PDF_NAME,
        GLOBAL_TEX_NAME: release_dir / GLOBAL_TEX_NAME,
        README_CONTROL: release_dir / README_CONTROL,
        SUMMARY_CONTROL: release_dir / SUMMARY_CONTROL,
        SUMS_CONTROL: release_dir / SUMS_CONTROL,
    }
    zenodo_rows = [
        (name, path.stat().st_size, sha256_path(path), "replace" if name in {BUNDLE_NAME, README_CONTROL, SUMMARY_CONTROL, SUMS_CONTROL} else "add")
        for name, path in zenodo_paths.items()
    ]
    zenodo_manifest = csv_bytes(("filename", "bytes", "sha256", "action"), zenodo_rows)
    (release_dir / "ZENODO_UPLOAD_MANIFEST.csv").write_bytes(zenodo_manifest)

    validation = {
        "schema": "ega_global_complete_linked_reader_release/v1",
        "status": "PASS",
        "errors": [],
        "producer_freeze": {
            "root_files": EXPECTED_ROOT_FILES,
            "root_bytes": EXPECTED_ROOT_BYTES,
            "source_files": EXPECTED_SOURCE_ROWS,
            "source_bytes": EXPECTED_SOURCE_BYTES,
            "source_manifest_sha256": EXPECTED_SOURCE_MANIFEST_SHA256,
        },
        "global_reader": summary["global_reader"],
        "global_master": {
            "bytes": len(master),
            "sha256": sha256_bytes(master),
        },
        "bundle": summary["bundle"],
        "standalone_readers": standalone_reader_rows,
        "standalone_masters": standalone_master_rows,
        "outer_manifest": {
            "rows": len(outer_rows),
            "bytes": len(outer),
            "sha256": sha256_bytes(outer),
        },
        "zenodo_upload_manifest": {
            "rows": len(zenodo_rows),
            "bytes": len(zenodo_manifest),
            "sha256": sha256_bytes(zenodo_manifest),
            "replacements": 4,
            "additions": 2,
            "expected_final_files": 42,
        },
        "privacy_hits": [],
    }
    (release_dir / "PACKAGE_VALIDATION.json").write_bytes(json_bytes(validation))
    return validation


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--producer-root", type=Path, default=DEFAULT_PRODUCER_ROOT)
    parser.add_argument("--bundle-dir", type=Path, default=DEFAULT_BUNDLE_DIR)
    parser.add_argument("--release-dir", type=Path, default=DEFAULT_RELEASE_DIR)
    args = parser.parse_args()

    root = args.producer_root.resolve()
    bundle_dir = args.bundle_dir.resolve()
    release_dir = args.release_dir.resolve()
    old_bundle = bundle_dir / BUNDLE_NAME
    all_files, source = producer_files(root)
    reader = all_files["build/EGA_English_Global_0_IV.pdf"]
    bundle_validation, bundle_members = build_bundle(
        source, reader, old_bundle, bundle_dir
    )
    release_validation = build_release(
        source, reader, bundle_dir, release_dir, bundle_members
    )
    print(json.dumps({"bundle": bundle_validation, "release": release_validation}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
