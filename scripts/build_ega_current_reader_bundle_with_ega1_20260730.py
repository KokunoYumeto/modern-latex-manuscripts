#!/usr/bin/env python3
"""Add the complete EGA I reader/source closure to the current EGA bundle."""

from __future__ import annotations

import csv
import hashlib
import io
import json
import re
import shutil
import zipfile
from pathlib import Path, PurePosixPath


REPO = Path(__file__).resolve().parents[1]
OUTPUT = (
    REPO
    / "sources"
    / "ega"
    / "ega-current-readers-and-buildable-tex-bundle-with-ega1-20260730"
)
BUNDLE_NAME = "00 Current_EGA_English_Readers_and_Buildable_TeX_20260730.zip"
BASE_BUNDLE = (
    REPO
    / "sources"
    / "ega"
    / "ega-current-readers-and-buildable-tex-bundle-reference-v2-20260730"
    / BUNDLE_NAME
)
EGA1_PACKAGE = (
    REPO
    / "sources"
    / "ega"
    / "checkpoints"
    / "ega1-complete-source-aligned-working-20260730"
)
EGA1_ZIP = EGA1_PACKAGE / (
    "10a_EGA1_English_Complete_SourceAligned_TeX_PDF_20260730.zip"
)
BASE_SHA256 = "6E1796CD3356CEAC4CD91CCB4ECE8358F722E59DD7FF3AA434E71FF5C05EE455"
EGA1_ZIP_SHA256 = "F647D23D98176A08C8E4CC53790C4EA0878328236B593EE0511E69F948544638"
ROOT = "EGA_Current_English_Readers_and_TeX_20260730/"
EGA1_SOURCE_ROOT = "EGA1_Complete_SourceAligned_English_20260730/"
ZIP_TIME = (2026, 7, 30, 0, 0, 0)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def safe_member(name: str) -> bool:
    pure = PurePosixPath(name)
    return (
        bool(name)
        and not pure.is_absolute()
        and ".." not in pure.parts
        and "\\" not in name
        and re.match(r"^[A-Za-z]:", name) is None
    )


def zip_info(name: str) -> zipfile.ZipInfo:
    info = zipfile.ZipInfo(name, date_time=ZIP_TIME)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.create_system = 3
    info.external_attr = 0o100644 << 16
    return info


def csv_bytes(rows: list[dict[str, object]]) -> bytes:
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(
        buffer,
        fieldnames=["relative_path", "bytes", "sha256"],
        lineterminator="\n",
    )
    writer.writeheader()
    writer.writerows(rows)
    return buffer.getvalue().encode("utf-8")


def read_zip(path: Path) -> dict[str, bytes]:
    with zipfile.ZipFile(path) as archive:
        if archive.testzip():
            raise RuntimeError(f"ZIP CRC failure: {path.name}")
        names = [row.filename for row in archive.infolist() if not row.is_dir()]
        if len(names) != len(set(names)) or not all(map(safe_member, names)):
            raise RuntimeError(f"unsafe or duplicate ZIP member: {path.name}")
        return {name: archive.read(name) for name in names}


def readme() -> bytes:
    return b"""# Current EGA English readers and buildable TeX

This bundle is the compact reader-facing entry point for the current EGA
English work preserved in the archive.

- EGA 0/III: assigned source-first Sections 8-13 working reader.
- EGA I: complete source-aligned working reader through bibliography and both
  indexes; exhaustive reference-v2 certification remains a later successor.
- EGA II: complete source-aligned reference-v2 working reader through EOF.
- EGA III: assigned source-first Sections 1-7 working reader.
- EGA IV: cumulative source-aligned Sections 1-10 working reader.

Each volume directory contains one cumulative reader PDF and its complete
buildable TeX closure. French authorities, OCR, raw logs, render trees,
private paths, and workflow material are excluded.

These are scholarly working translations, not critical editions, peer-review
or mathematical certifications, rights determinations, accessibility
remediation, or a claim that all of EGA has been translated and checked.
"""


def main() -> None:
    if not BASE_BUNDLE.is_file() or sha256(BASE_BUNDLE) != BASE_SHA256:
        raise RuntimeError("base EGA reader bundle identity changed")
    if not EGA1_ZIP.is_file() or sha256(EGA1_ZIP) != EGA1_ZIP_SHA256:
        raise RuntimeError("EGA I source ZIP identity changed")

    base = read_zip(BASE_BUNDLE)
    if len(base) != 99:
        raise RuntimeError("base EGA reader bundle member count changed")
    old_controls = {ROOT + "README.md", ROOT + "SHA256SUMS.csv"}
    if not old_controls.issubset(base):
        raise RuntimeError("base EGA reader bundle controls missing")
    retained = {name: data for name, data in base.items() if name not in old_controls}
    if len(retained) != 97:
        raise RuntimeError("base retained-member count changed")

    ega1_zip = read_zip(EGA1_ZIP)
    source_prefix = EGA1_SOURCE_ROOT + "source/"
    source_names = sorted(
        [name for name in ega1_zip if name.startswith(source_prefix)],
        key=str.casefold,
    )
    if len(source_names) != 16:
        raise RuntimeError("EGA I source closure is not 16 members")
    reader_name = EGA1_SOURCE_ROOT + "reader/" + (
        "00a_EGA1_English_Complete_SourceAligned_Working_Reader_20260730.pdf"
    )
    if reader_name not in ega1_zip:
        raise RuntimeError("EGA I source package reader missing")

    members = dict(retained)
    members[ROOT + "EGA1/reader/EGA1_English_Reader.pdf"] = ega1_zip[reader_name]
    for name in source_names:
        relative = name[len(source_prefix) :]
        members[ROOT + "EGA1/source/" + relative] = ega1_zip[name]
    members[ROOT + "README.md"] = readme()

    rows = [
        {
            "relative_path": name[len(ROOT) :],
            "bytes": len(data),
            "sha256": sha256_bytes(data),
        }
        for name, data in sorted(members.items(), key=lambda item: item[0].casefold())
    ]
    manifest_name = ROOT + "SHA256SUMS.csv"
    members[manifest_name] = csv_bytes(rows)
    if len(members) != 116 or len(rows) != 115:
        raise RuntimeError("new EGA reader bundle boundary changed")

    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    OUTPUT.mkdir(parents=True)
    destination = OUTPUT / BUNDLE_NAME
    with zipfile.ZipFile(destination, "w", allowZip64=True) as archive:
        for name, data in sorted(members.items(), key=lambda item: item[0].casefold()):
            if not safe_member(name):
                raise RuntimeError(f"unsafe new bundle member: {name}")
            archive.writestr(
                zip_info(name),
                data,
                compress_type=zipfile.ZIP_DEFLATED,
                compresslevel=9,
            )

    replay = read_zip(destination)
    if replay != members:
        raise RuntimeError("new EGA reader bundle replay mismatch")
    for name, data in retained.items():
        if replay.get(name) != data:
            raise RuntimeError(f"retained EGA bundle member changed: {name}")

    validation = {
        "schema": "ega-current-reader-bundle-with-ega1-1.0",
        "status": "PASS",
        "errors": [],
        "bytes": destination.stat().st_size,
        "sha256": sha256(destination),
        "members": len(members),
        "manifest_rows": len(rows),
        "uncompressed_bytes": sum(len(data) for data in members.values()),
        "preserved_base_members": len(retained),
        "added_ega1_members": 17,
        "required_readers": [
            ROOT + "EGA0/reader/EGA0_English_Working_Reader.pdf",
            ROOT + "EGA1/reader/EGA1_English_Reader.pdf",
            ROOT + "EGA2/reader/EGA2_English_Reader.pdf",
            ROOT + "EGA3/reader/EGA3_English_Working_Reader_Sections1_7.pdf",
            ROOT + "EGA4/reader/EGA4_English_Working_Reader_Sections1_10.pdf",
        ],
    }
    for name in validation["required_readers"]:
        if name not in replay:
            raise RuntimeError(f"required reader missing: {name}")
    (OUTPUT / "BUNDLE_VALIDATION.json").write_text(
        json.dumps(validation, indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    (OUTPUT / "README.md").write_text(
        "# Current EGA Reader Bundle with EGA I\n\n"
        f"The {len(members)}-member ZIP is {destination.stat().st_size:,} bytes "
        f"with SHA-256 `{sha256(destination)}`. It adds the complete EGA I "
        "working reader and its 16-file buildable source closure while "
        "preserving all 97 mathematical reader/source members from the "
        "preceding bundle byte-for-byte.\n",
        encoding="utf-8",
        newline="\n",
    )
    print(json.dumps(validation, indent=2))


if __name__ == "__main__":
    main()
