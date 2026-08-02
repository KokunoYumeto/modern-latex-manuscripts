#!/usr/bin/env python3
"""Publish the complete SGA7 II English working reader in the SGA lineage."""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import io
import json
import shutil
import subprocess
import time
import urllib.parse
import zipfile
from pathlib import Path, PurePosixPath

import publish_sga7ii_english_expose_xxi_4_zenodo_20260802 as template


base = template.base
prior = template.prior
API = template.API
PUBLICATION_DATE = "2026-08-02"
CONCEPT_DOI = "10.5281/zenodo.20410947"
PREDECESSOR_RECORD = 21_753_102
PREDECESSOR_DOI = "10.5281/zenodo.21753102"
PREDECESSOR_FILES = 87
PREDECESSOR_BYTES = 780_139_801
FINAL_FILES = 88
DEFAULT_PREVIEW = "00a_SGA1_English_Reader.pdf"
OLD_CONTROLS_NAME = "10z_SGA_Current_Release_Controls_20260802_r7.zip"
CONTROLS_NAME = "10z_SGA_Current_Release_Controls_20260802_r8.zip"
OLD_BUNDLE_NAME = (
    "00_Current_SGA1-7_English_Readers_and_Buildable_TeX_20260801.zip"
)
BUNDLE_NAME = (
    "00_Current_SGA1-7II_English_Readers_and_Buildable_TeX_20260802.zip"
)
OLD_PDF_NAME = "00j_SGA7II_English_Through_Expose_XXI_4_Working_20260802.pdf"
OLD_SOURCE_ZIP_NAME = (
    "10g3_SGA7II_English_Through_Expose_XXI_4_Reader_and_TeX_20260802.zip"
)
PDF_NAME = "00j_SGA7II_English_Complete_Working_Reader_20260802.pdf"
TEX_NAME = "02j_SGA7II_English_Complete_Working_Master_20260802.tex"
SOURCE_ZIP_NAME = (
    "10g3_SGA7II_English_Complete_Reader_and_Buildable_TeX_20260802.zip"
)
REPLACED_NAMES = {
    OLD_BUNDLE_NAME,
    OLD_CONTROLS_NAME,
    OLD_PDF_NAME,
    OLD_SOURCE_ZIP_NAME,
}
VERSION = "2026-08-02 complete SGA7 II English working reader"

REPO_ROOT = Path(__file__).resolve().parents[1]
PACKAGE_REL = Path("sources/sga/sga7ii-english-complete-through-expose-xxii-20260802")
PACKAGE_ROOT = REPO_ROOT / PACKAGE_REL
TEMP_ROOT = REPO_ROOT / "tmp/zenodo/sga7ii-english-complete-20260802"
CONTROLS_ROOT = TEMP_ROOT / "release-controls"
CONTROLS_ZIP = TEMP_ROOT / CONTROLS_NAME
BUNDLE_PATH = TEMP_ROOT / BUNDLE_NAME
READBACK_ROOT = TEMP_ROOT / "public-readback"
STATE_PATH = TEMP_ROOT / "draft_state.json"
RECEIPT_ROOT = REPO_ROOT / "manifests/published-zenodo"
RECEIPT_TAG = "20260802_sga7ii_english_complete"
PREDECESSOR_RECEIPT = RECEIPT_ROOT / (
    "20260802_sga7ii_english_through_expose_xxi_4_"
    "record_21753102_public_readback.json"
)
GITHUB_PACKAGE_COMMIT = "22b8a4a26b65e69c141d08fe880cef688f6cc30e"

EXPECTED_PREDECESSOR_RECEIPT = (
    42_250,
    "C7391F614CA265B3BD48568CBD08020904E87D95DDAE8C2834182D2C64C73BC5",
)
EXPECTED_OLD_CONTROLS = (
    29_187,
    "49B164EE58EDB43D66F1D7C2C0AEE5F65E96763D59AF9E9993C42B86D2C04EF4",
)
EXPECTED_OLD_BUNDLE = (
    25_842_434,
    "51D93345AA12389C567AB978FFB6C400809512C4C3FFC8347B0BCD64F398D723",
    1_585,
)
EXPECTED_PACKAGE = (
    195,
    4_496_334,
    "8104368BA0D217F7008079F3AFAC7F36703ABDE8F4B26E2AD37E7771AB766075",
)
EXPECTED_MANIFEST = (
    26_555,
    "E5E1A7F81A5A6D6E5A1988ED9171BCC9DF2FBA20B247920C06517F99518D74AC",
)
EXPECTED_VALIDATION = (
    2_228,
    "60265DE8244680C38ADA2E1BF88503ED06FA3FACEFA3210EF46F9432031F7A0C",
)
EXPECTED_PDF = (
    1_785_484,
    "930446AC789F5B67C7093C02D5604AFB5A4ED1E0554B1A25CC7EEF633C9F0960",
)
EXPECTED_TEX = (
    12_130,
    "CE309601EB26AF0B83656C8CCD57D739761A553EC567104E03CCAA9C6D2A6588",
)
EXPECTED_SOURCE_ZIP = (
    1_893_617,
    "9366F847CDF99E74BB8619E46EA294363C92E2C5BC55718DCB695B549613CF83",
)
EXPECTED_SOURCE_ZIP_MEMBERS = 187
EXPECTED_SOURCE_ZIP_UNCOMPRESSED = 2_569_993
EXPECTED_SOURCE_ZIP_MANIFEST = (
    25_716,
    "75D89CEB91706CF4FAEBA530ACB5CF68AD70D2AC1B37528BFABB269D4351F9D6",
)

OLD_DESCRIPTION = template.DESCRIPTION
OLD_NOTES = template.NOTES
DESCRIPTION = (
    "<p><strong>Start here:</strong> the first ZIP collects the current English "
    "reader PDFs and buildable TeX closures for SGA 1 through SGA 7 II. The "
    "same readers and master TeX files remain direct; SGA1 remains the browser "
    "preview. This is not yet one cross-volume SGA 1-7.2 PDF.</p>"
    "<p><strong>SGA3:</strong> the current cumulative English reader is the clean "
    "1,470-page R29 reader covering the Introduction, Exposes I-XXVI, indexes, "
    "and guide.</p>"
    "<p><strong>SGA7:</strong> SGA7 I has a complete 287-page English working "
    "reader for all written Exposes I, II, VI, VII, VIII, and IX. SGA7 II now "
    "has a complete 264-page English working reader containing Exposes X-XXII "
    "through volume EOF, with its master TeX direct and its exact 183-component "
    "buildable source in one compact ZIP. The separately available French SGA7 "
    "II working transcription remains partial and is not represented as complete." 
    "</p>"
    "<p>These are working scholarly translations, editions, or transcriptions, "
    "not critical editions, peer review, exhaustive reference certification, "
    "accessibility certification, rights determinations, or mathematical "
    "certification.</p>"
)
NOTES = (
    "<p>Reader PDFs open directly on mathematical content. Buildable source, "
    "provenance, and release controls are separate downloads.</p>"
)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def sha256_path(path: Path) -> str:
    return base.sha256_path(path)


def md5_path(path: Path) -> str:
    return base.md5_path(path)


def metadata_notes(metadata: dict[str, object]) -> list[str]:
    return template.metadata_notes(metadata)


def safe_member(name: str) -> bool:
    pure = PurePosixPath(name)
    return (
        name == name.replace("\\", "/")
        and not pure.is_absolute()
        and ".." not in pure.parts
        and not (len(name) > 1 and name[1] == ":")
    )


def package_files() -> list[Path]:
    return sorted(
        (path for path in PACKAGE_ROOT.rglob("*") if path.is_file()),
        key=lambda path: path.relative_to(PACKAGE_ROOT).as_posix().casefold(),
    )


def package_snapshot(files: list[Path]) -> tuple[int, int, str]:
    digest = hashlib.sha256()
    for path in files:
        relative = path.relative_to(PACKAGE_ROOT).as_posix()
        digest.update(
            f"{relative}\t{path.stat().st_size}\t{sha256_path(path)}\n".encode()
        )
    return len(files), sum(path.stat().st_size for path in files), digest.hexdigest().upper()


def zip_inventory_from_bytes(data: bytes) -> dict[str, object]:
    identities: dict[str, dict[str, object]] = {}
    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        infos = [row for row in archive.infolist() if not row.is_dir()]
        if (
            archive.testzip() is not None
            or len(infos) != len({row.filename for row in infos})
            or not all(safe_member(row.filename) for row in infos)
        ):
            raise RuntimeError("ZIP safety or CRC boundary changed")
        for row in infos:
            member = archive.read(row.filename)
            identities[row.filename] = {
                "bytes": len(member),
                "sha256": sha256_bytes(member),
                "crc32": f"{row.CRC:08X}",
            }
        return {
            "members": len(infos),
            "uncompressed_bytes": sum(row.file_size for row in infos),
            "member_identities": identities,
            "safe_names": True,
            "crc_errors": 0,
        }


def verify_source_zip(path: Path) -> dict[str, object]:
    data = path.read_bytes()
    inventory = zip_inventory_from_bytes(data)
    if (
        (len(data), sha256_bytes(data)) != EXPECTED_SOURCE_ZIP
        or int(inventory["members"]) != EXPECTED_SOURCE_ZIP_MEMBERS
        or int(inventory["uncompressed_bytes"]) != EXPECTED_SOURCE_ZIP_UNCOMPRESSED
    ):
        raise RuntimeError("SGA7 II source ZIP identity changed")
    manifest_name = "ZIP_MEMBER_SHA256SUMS.csv"
    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        manifest_data = archive.read(manifest_name)
        rows = list(csv.DictReader(io.StringIO(manifest_data.decode("utf-8-sig"))))
        if (
            (len(manifest_data), sha256_bytes(manifest_data))
            != EXPECTED_SOURCE_ZIP_MANIFEST
            or len(rows) != EXPECTED_SOURCE_ZIP_MEMBERS - 1
        ):
            raise RuntimeError("SGA7 II source ZIP manifest changed")
        for row in rows:
            member = archive.read(row["path"])
            if (len(member), sha256_bytes(member)) != (
                int(row["bytes"]),
                row["sha256"].upper(),
            ):
                raise RuntimeError(f"SGA7 II ZIP member changed: {row['path']}")
    return inventory


def verify_package() -> dict[str, object]:
    files = package_files()
    if package_snapshot(files) != EXPECTED_PACKAGE:
        raise RuntimeError("SGA7 II package boundary changed")
    manifest = PACKAGE_ROOT / "SHA256SUMS.csv"
    validation_path = PACKAGE_ROOT / "PACKAGE_VALIDATION.json"
    if (manifest.stat().st_size, sha256_path(manifest)) != EXPECTED_MANIFEST:
        raise RuntimeError("SGA7 II outer manifest changed")
    if (validation_path.stat().st_size, sha256_path(validation_path)) != EXPECTED_VALIDATION:
        raise RuntimeError("SGA7 II package validation changed")
    validation = json.loads(validation_path.read_text(encoding="utf-8"))
    if (
        validation.get("status") != "PASS_COMPLETE_WORKING_READER"
        or validation.get("errors")
        or not validation["scope"].get("complete_sga7ii_working_translation")
        or int(validation["reader"]["pages"]) != 264
        or int(validation["source"]["tex_files"]) != 184
        or int(validation["source"]["components"]) != 183
        or int(validation["privacy"]["occurrences"]) != 0
    ):
        raise RuntimeError("SGA7 II validation boundary changed")
    rows = list(csv.DictReader(manifest.open("r", encoding="utf-8", newline="")))
    represented = {
        path.relative_to(PACKAGE_ROOT).as_posix(): path
        for path in files
        if path.name != "SHA256SUMS.csv"
    }
    if len(rows) != 194 or {row["path"] for row in rows} != set(represented):
        raise RuntimeError("SGA7 II manifest closure changed")
    for row in rows:
        path = represented[row["path"]]
        if (path.stat().st_size, sha256_path(path)) != (
            int(row["bytes"]),
            row["sha256"].upper(),
        ):
            raise RuntimeError(f"SGA7 II package identity changed: {row['path']}")
    pdf = PACKAGE_ROOT / "reader/SGA7II_English_Complete_Through_Expose_XXII_20260802.pdf"
    tex = PACKAGE_ROOT / "source/SGA7II_English_Complete_Through_Expose_XXII_20260802.tex"
    source_zip = PACKAGE_ROOT / "SGA7II_English_Complete_Reader_and_Buildable_TeX_20260802.zip"
    if (pdf.stat().st_size, sha256_path(pdf)) != EXPECTED_PDF:
        raise RuntimeError("SGA7 II PDF identity changed")
    if (tex.stat().st_size, sha256_path(tex)) != EXPECTED_TEX:
        raise RuntimeError("SGA7 II master identity changed")
    inventory = verify_source_zip(source_zip)
    return {"pdf": pdf, "tex": tex, "source_zip": source_zip, "source_zip_inventory": inventory}


def load_predecessor(latest_record: int = PREDECESSOR_RECORD) -> dict[str, object]:
    if (PREDECESSOR_RECEIPT.stat().st_size, sha256_path(PREDECESSOR_RECEIPT)) != EXPECTED_PREDECESSOR_RECEIPT:
        raise RuntimeError("SGA predecessor receipt changed")
    compact = json.loads(PREDECESSOR_RECEIPT.read_text(encoding="utf-8"))
    if (
        compact.get("status") != "PASS_PUBLIC_READBACK"
        or compact.get("errors")
        or int(compact.get("record_id", -1)) != PREDECESSOR_RECORD
        or compact.get("doi") != PREDECESSOR_DOI
        or compact.get("concept_doi") != CONCEPT_DOI
        or int(compact.get("outer_files", -1)) != PREDECESSOR_FILES
        or int(compact.get("outer_bytes", -1)) != PREDECESSOR_BYTES
        or compact.get("default_preview") != DEFAULT_PREVIEW
        or compact.get("duplicate_concept_created") is not False
        or compact.get("active_draft_remaining") is not False
    ):
        raise RuntimeError("SGA predecessor receipt boundary changed")
    session = base.make_session()
    latest = base.check(
        session.get(
            f"{API}/records/{PREDECESSOR_RECORD}/versions/latest?expand=true",
            headers=prior.public_headers(), timeout=(30, 180)
        ), {200}
    ).json()
    if int(latest["id"]) != latest_record:
        raise RuntimeError("SGA concept head moved before successor preparation")
    record = base.check(
        session.get(
            f"{API}/records/{PREDECESSOR_RECORD}?expand=true",
            headers=prior.public_headers(), timeout=(30, 180)
        ), {200}
    ).json()
    entries = base.modern_entries(record)
    if (
        not record.get("is_published")
        or record["pids"]["doi"]["identifier"] != PREDECESSOR_DOI
        or record["parent"]["pids"]["doi"]["identifier"] != CONCEPT_DOI
        or len(entries) != PREDECESSOR_FILES
        or sum(int(row["size"]) for row in entries.values()) != PREDECESSOR_BYTES
        or record["files"].get("default_preview") != DEFAULT_PREVIEW
        or record["metadata"].get("version") != compact.get("version")
        or record["metadata"].get("description", "").strip() != OLD_DESCRIPTION
        or metadata_notes(record["metadata"]) != [OLD_NOTES]
    ):
        raise RuntimeError("Live SGA predecessor boundary changed")
    receipt_files = compact.get("outer_file_readback", {})
    if set(receipt_files) != set(entries):
        raise RuntimeError("SGA predecessor receipt does not close")
    files: dict[str, dict[str, object]] = {}
    for name, entry in entries.items():
        row = receipt_files[name]
        observed = int(entry["size"]), base.normalized_md5(entry["checksum"])
        wanted = int(row["bytes"]), str(row["md5"]).lower()
        if observed != wanted or row.get("match") is not True:
            raise RuntimeError(f"SGA predecessor identity changed: {name}")
        files[name] = {
            "bytes": int(row["bytes"]), "sha256": str(row["sha256"]).upper(),
            "md5": observed[1], "content_url": entry["links"]["content"], "match": True,
        }
    controls = base.check(
        session.get(entries[OLD_CONTROLS_NAME]["links"]["content"], timeout=(30, 300)), {200}
    ).content
    if (len(controls), sha256_bytes(controls)) != EXPECTED_OLD_CONTROLS:
        raise RuntimeError("Current SGA release controls changed")
    with zipfile.ZipFile(io.BytesIO(controls)) as archive:
        if archive.testzip() is not None:
            raise RuntimeError("Current SGA release controls failed CRC")
        rows = list(csv.DictReader(io.StringIO(archive.read("09a_RELEASE_FILE_MANIFEST.csv").decode("utf-8"))))
    manifest = {row["filename"]: (int(row["bytes"]), row["sha256"].upper()) for row in rows}
    expected_names = set(entries) - {OLD_CONTROLS_NAME}
    if len(rows) != PREDECESSOR_FILES - 1 or set(manifest) != expected_names:
        raise RuntimeError("Current SGA release manifest boundary changed")
    for name in expected_names:
        if manifest[name] != (int(files[name]["bytes"]), str(files[name]["sha256"]).upper()):
            raise RuntimeError(f"Current SGA control identity changed: {name}")
    return {
        "status": "PASS_PUBLIC_READBACK", "errors": [], "record_id": PREDECESSOR_RECORD,
        "doi": PREDECESSOR_DOI, "concept_doi": CONCEPT_DOI,
        "outer_files": len(files), "outer_bytes": sum(int(row["bytes"]) for row in files.values()),
        "outer_file_readback": files, "default_preview": DEFAULT_PREVIEW,
        "version": record["metadata"]["version"], "active_draft_remaining": False,
    }


def expected_retained(predecessor: dict[str, object]) -> dict[str, dict[str, object]]:
    return {
        name: row for name, row in predecessor["outer_file_readback"].items()
        if name not in REPLACED_NAMES
    }


def write_zip(path: Path, members: dict[str, bytes]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.unlink(missing_ok=True)
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9, allowZip64=True) as archive:
        for name in sorted(members, key=str.casefold):
            info = zipfile.ZipInfo(name, date_time=(2026, 8, 2, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            info.create_system = 3
            archive.writestr(info, members[name], compresslevel=9)


def build_current_bundle(predecessor: dict[str, object], verified: dict[str, object]) -> dict[str, object]:
    row = predecessor["outer_file_readback"][OLD_BUNDLE_NAME]
    session = base.make_session()
    old_data = base.check(session.get(row["content_url"], timeout=(30, 600)), {200}).content
    if (len(old_data), sha256_bytes(old_data)) != EXPECTED_OLD_BUNDLE[:2]:
        raise RuntimeError("Current SGA bundle identity changed")
    old_inventory = zip_inventory_from_bytes(old_data)
    if int(old_inventory["members"]) != EXPECTED_OLD_BUNDLE[2]:
        raise RuntimeError("Current SGA bundle member boundary changed")
    old_root = "SGA_Current_English_Readers_and_TeX_20260801/"
    new_root = "SGA_Current_English_Readers_and_TeX_20260802/"
    content: dict[str, bytes] = {}
    with zipfile.ZipFile(io.BytesIO(old_data)) as archive:
        old_manifest = archive.read(old_root + "SHA256SUMS.csv")
        rows = list(csv.DictReader(io.StringIO(old_manifest.decode("utf-8-sig"))))
        if len(rows) != EXPECTED_OLD_BUNDLE[2] - 1:
            raise RuntimeError("Current SGA bundle manifest boundary changed")
        for manifest_row in rows:
            relative = manifest_row["relative_path"]
            member = archive.read(old_root + relative)
            if (len(member), sha256_bytes(member)) != (
                int(manifest_row["bytes"]), manifest_row["sha256"].upper()
            ):
                raise RuntimeError(f"Current SGA bundle member changed: {relative}")
            if relative != "README.md":
                content[relative] = member
    content["README.md"] = (
        "# Current SGA English readers and buildable TeX\n\n"
        "This compact bundle contains the current standalone English reader PDFs "
        "and their buildable TeX closures for SGA 1 through SGA 7 II. SGA7 II "
        "is complete through Expose XXII and volume EOF. The bundle is not one "
        "cross-volume PDF and does not claim critical-edition, mathematical, "
        "accessibility, or exhaustive-reference certification.\n"
    ).encode("utf-8")
    content["SGA7II/reader/SGA7II_English_Complete_Working_Reader_20260802.pdf"] = verified["pdf"].read_bytes()
    source_root = PACKAGE_ROOT / "source"
    for path in sorted(source_root.rglob("*"), key=lambda item: item.as_posix().casefold()):
        if path.is_file():
            relative = path.relative_to(source_root).as_posix()
            content[f"SGA7II/source/{relative}"] = path.read_bytes()
    manifest_buffer = io.StringIO(newline="")
    writer = csv.DictWriter(
        manifest_buffer, fieldnames=["relative_path", "bytes", "sha256"],
        lineterminator="\n", quoting=csv.QUOTE_MINIMAL,
    )
    writer.writeheader()
    for name in sorted(content, key=str.casefold):
        data = content[name]
        writer.writerow({"relative_path": name, "bytes": len(data), "sha256": sha256_bytes(data)})
    content["SHA256SUMS.csv"] = manifest_buffer.getvalue().encode("utf-8")
    members = {new_root + name: data for name, data in content.items()}
    write_zip(BUNDLE_PATH, members)
    replay = BUNDLE_PATH.with_name("bundle-replay.zip")
    write_zip(replay, members)
    try:
        if BUNDLE_PATH.read_bytes() != replay.read_bytes():
            raise RuntimeError("Current SGA bundle is not deterministic")
    finally:
        replay.unlink(missing_ok=True)
    inventory = zip_inventory_from_bytes(BUNDLE_PATH.read_bytes())
    if (
        int(inventory["members"]) != EXPECTED_OLD_BUNDLE[2] + 185
        or set(inventory["member_identities"]) != set(members)
    ):
        raise RuntimeError("Current SGA bundle successor boundary changed")
    return {
        "path": BUNDLE_PATH, "bytes": BUNDLE_PATH.stat().st_size,
        "sha256": sha256_path(BUNDLE_PATH), "md5": md5_path(BUNDLE_PATH),
        "inventory": inventory,
    }


def local_uploads(predecessor: dict[str, object]) -> dict[str, dict[str, object]]:
    verified = verify_package()
    paths = {PDF_NAME: verified["pdf"], TEX_NAME: verified["tex"], SOURCE_ZIP_NAME: verified["source_zip"]}
    result: dict[str, dict[str, object]] = {}
    for name, path in paths.items():
        result[name] = {
            "path": path, "bytes": path.stat().st_size,
            "sha256": sha256_path(path), "md5": md5_path(path),
        }
    result[SOURCE_ZIP_NAME]["inventory"] = verified["source_zip_inventory"]
    result[BUNDLE_NAME] = build_current_bundle(predecessor, verified)
    return result


def verify_github() -> dict[str, object]:
    subprocess.check_call(["git", "fetch", "--no-tags", "origin", "main"], cwd=REPO_ROOT)
    remote = subprocess.check_output(
        ["git", "ls-remote", "origin", "refs/heads/main"], cwd=REPO_ROOT, text=True
    ).split()[0]
    subprocess.check_call(["git", "merge-base", "--is-ancestor", GITHUB_PACKAGE_COMMIT, remote], cwd=REPO_ROOT)
    session = base.make_session()
    readback: dict[str, dict[str, object]] = {}
    root = (
        "https://raw.githubusercontent.com/KokunoYumeto/modern-latex-manuscripts/"
        f"{GITHUB_PACKAGE_COMMIT}/{PACKAGE_REL.as_posix()}"
    )
    for path in package_files():
        relative = path.relative_to(PACKAGE_ROOT).as_posix()
        url = f"{root}/{urllib.parse.quote(relative, safe='/')}"
        data = base.check(session.get(url, timeout=(30, 300)), {200}).content
        if (len(data), sha256_bytes(data)) != (path.stat().st_size, sha256_path(path)):
            raise RuntimeError(f"GitHub SGA7 II readback changed: {relative}")
        readback[relative] = {"bytes": len(data), "sha256": sha256_bytes(data), "url": url, "match": True}
    return {
        "status": "PASS_GITHUB_PUBLIC_READBACK", "errors": [],
        "commit": GITHUB_PACKAGE_COMMIT, "public_main": remote,
        "package_path": PACKAGE_REL.as_posix(), "files_read_back": len(readback),
        "bytes_read_back": sum(int(row["bytes"]) for row in readback.values()),
        "file_readback": readback,
    }


def write_csv(path: Path, rows: list[dict[str, object]], fields: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def build_controls(
    local: dict[str, dict[str, object]], predecessor: dict[str, object], github: dict[str, object]
) -> dict[str, object]:
    resolved = TEMP_ROOT.resolve()
    if not resolved.is_relative_to((REPO_ROOT / "tmp").resolve()):
        raise RuntimeError("Refusing release controls outside repository tmp")
    shutil.rmtree(CONTROLS_ROOT, ignore_errors=True)
    CONTROLS_ROOT.mkdir(parents=True)
    retained = expected_retained(predecessor)
    (CONTROLS_ROOT / "09_README_CURRENT_RELEASE.md").write_text(
        "# Current SGA release controls\n\n"
        "This successor replaces the partial SGA7 II English reader with the complete "
        "264-page working reader through Expose XXII and volume EOF. The master TeX "
        "is direct, the complete 183-component buildable closure is in one compact ZIP, "
        "and the leading all-current-readers bundle now includes SGA7 II. SGA1 remains "
        "the browser preview until a genuine internally linked SGA 1-7.2 reader exists.\n",
        encoding="utf-8", newline="\n",
    )
    roles = {
        BUNDLE_NAME: "current_english_reader_and_buildable_tex_bundle",
        PDF_NAME: "direct_complete_working_reader",
        TEX_NAME: "direct_complete_editable_master",
        SOURCE_ZIP_NAME: "compact_reader_and_buildable_tex_archive",
    }
    rows = [
        {"filename": name, "bytes": int(row["bytes"]), "sha256": str(row["sha256"]).upper(),
         "release_role": "retained_predecessor_file", "source": f"zenodo_record_{PREDECESSOR_RECORD}"}
        for name, row in retained.items()
    ]
    for name, row in local.items():
        rows.append({
            "filename": name, "bytes": int(row["bytes"]), "sha256": str(row["sha256"]).upper(),
            "release_role": roles[name], "source": PACKAGE_REL.as_posix(),
        })
    rows.sort(key=lambda row: str(row["filename"]).casefold())
    write_csv(CONTROLS_ROOT / "09a_RELEASE_FILE_MANIFEST.csv", rows,
              ["filename", "bytes", "sha256", "release_role", "source"])
    base.save_json(CONTROLS_ROOT / "09b_RELEASE_VALIDATION.json", {
        "status": "PASS_PREPARED_RELEASE_CONTROLS", "errors": [],
        "concept_doi": CONCEPT_DOI, "predecessor_record": PREDECESSOR_RECORD,
        "retained_predecessor_files": len(retained), "added_files": len(local),
        "replaced_files": sorted(REPLACED_NAMES),
        "expected_outer_files_including_controls": FINAL_FILES,
        "default_preview": DEFAULT_PREVIEW,
        "github": {key: github[key] for key in ("commit", "public_main", "package_path", "files_read_back", "bytes_read_back")},
        "reader_pages": 264, "reader_sha256": EXPECTED_PDF[1],
        "editable_tex_files": 184, "component_files": 183,
        "source_zip_members": EXPECTED_SOURCE_ZIP_MEMBERS,
        "current_bundle_members": int(local[BUNDLE_NAME]["inventory"]["members"]),
        "complete_sga7ii_working_translation": True,
        "complete_cross_sga_reader_claim": False, "exhaustive_reference_claim": False,
        "reader_process_preface_pages": 0,
    })
    copies = {
        "09c_SGA7II_PACKAGE_VALIDATION.json": PACKAGE_ROOT / "PACKAGE_VALIDATION.json",
        "09d_SGA7II_PACKAGE_SHA256SUMS.csv": PACKAGE_ROOT / "SHA256SUMS.csv",
        "09e_SGA7II_ZENODO_UPLOAD_MANIFEST.csv": PACKAGE_ROOT / "ZENODO_UPLOAD_MANIFEST.csv",
        "09f_SGA7II_BUILD_AND_QA_SUMMARY.md": PACKAGE_ROOT / "BUILD_AND_QA_SUMMARY.md",
        "09g_SGA7II_FINAL_VISUAL_QA.md": PACKAGE_ROOT / "FINAL_VISUAL_QA.md",
        "09h_SGA7II_RIGHTS_AND_PROVENANCE.md": PACKAGE_ROOT / "RIGHTS_AND_PROVENANCE.md",
    }
    for name, source in copies.items():
        shutil.copyfile(source, CONTROLS_ROOT / name)
    base.save_json(CONTROLS_ROOT / "09i_SGA7II_GITHUB_PUBLIC_READBACK_SUMMARY.json", {
        "status": github["status"], "errors": github["errors"], "commit": github["commit"],
        "public_main": github["public_main"], "package_path": github["package_path"],
        "files_read_back": github["files_read_back"], "bytes_read_back": github["bytes_read_back"],
    })
    for control_name, upload_name in (
        ("09j_SGA7II_SOURCE_ZIP_VALIDATION.json", SOURCE_ZIP_NAME),
        ("09k_CURRENT_READER_BUNDLE_VALIDATION.json", BUNDLE_NAME),
    ):
        inventory = local[upload_name]["inventory"]
        base.save_json(CONTROLS_ROOT / control_name, {
            "status": "PASS", "errors": [], "filename": upload_name,
            "bytes": local[upload_name]["bytes"], "sha256": local[upload_name]["sha256"],
            "members": inventory["members"], "uncompressed_bytes": inventory["uncompressed_bytes"],
            "member_readback": f"{inventory['members']}/{inventory['members']} exact",
        })
    packed = [
        {"filename": path.name, "bytes": path.stat().st_size, "sha256": sha256_path(path)}
        for path in sorted(CONTROLS_ROOT.iterdir(), key=lambda path: path.name.casefold())
    ]
    write_csv(CONTROLS_ROOT / "PACKED_CONTROL_SHA256.csv", packed, ["filename", "bytes", "sha256"])
    write_zip(CONTROLS_ZIP, {path.name: path.read_bytes() for path in CONTROLS_ROOT.iterdir()})
    inventory = zip_inventory_from_bytes(CONTROLS_ZIP.read_bytes())
    return {
        "path": CONTROLS_ZIP, "bytes": CONTROLS_ZIP.stat().st_size,
        "sha256": sha256_path(CONTROLS_ZIP), "md5": md5_path(CONTROLS_ZIP),
        "inventory": inventory,
    }


def ordered_names(names: set[str]) -> list[str]:
    english = [
        "00a_SGA1_English_Reader.pdf", "00b_SGA2_English_Reader.pdf",
        "00c_SGA3_English_Reader.pdf", "00d_SGA4_English_Reader.pdf",
        "00e_SGA5_English_Reader.pdf", "00f_SGA6_English_Reader.pdf",
        "00i_SGA7I_English_Complete_Working_Reader_20260801.pdf", PDF_NAME,
    ]
    french = [
        "00g_SGA7I_Fresh_Source_Transcription_Complete_Working.pdf",
        "00h_SGA7II_French_Source_Transcription_Working_X-XXI_Partial_20260731.pdf",
        "01e_SGA5_French_Reader.pdf", "01f_SGA6_French_Reader.pdf",
    ]
    english_tex = [
        "02a_SGA1_English_Master.tex", "02b_SGA2_English_Master.tex",
        "02c_SGA3_English_Master.tex", "02d_SGA4_English_Master.tex",
        "02e_SGA5_English_Master.tex", "02f_SGA6_English_Master.tex",
        "02i_SGA7I_English_Complete_Working_Master_20260801.tex", TEX_NAME,
    ]
    french_tex = [
        "02g_SGA7I_Fresh_Source_Transcription_Complete_Working.tex",
        "02h_SGA7II_French_Source_Transcription_Working_X-XXI_Partial_20260731.tex",
        "03e_SGA5_French_Master.tex", "03f_SGA6_French_Master.tex",
    ]
    preferred = [BUNDLE_NAME, *english, *french, *english_tex, *french_tex]
    if not set(preferred).issubset(names):
        raise RuntimeError(f"Direct SGA shelf changed: {sorted(set(preferred) - names)}")
    remainder = names - set(preferred)
    other_pdfs = sorted((name for name in remainder if name.lower().endswith(".pdf")), key=str.casefold)
    other_tex = sorted((name for name in remainder if name.lower().endswith(".tex")), key=str.casefold)
    archives = sorted(remainder - set(other_pdfs) - set(other_tex), key=str.casefold)
    return [*preferred, *other_pdfs, *other_tex, *archives]


def configure_prior() -> None:
    values = {
        "PUBLICATION_DATE": PUBLICATION_DATE, "CONCEPT_DOI": CONCEPT_DOI,
        "PREDECESSOR_RECORD": PREDECESSOR_RECORD, "PREDECESSOR_DOI": PREDECESSOR_DOI,
        "PREDECESSOR_FILES": PREDECESSOR_FILES, "PREDECESSOR_BYTES": PREDECESSOR_BYTES,
        "FINAL_FILES": FINAL_FILES, "DEFAULT_PREVIEW": DEFAULT_PREVIEW,
        "CONTROLS_NAME": CONTROLS_NAME, "VERSION": VERSION,
        "TEMP_ROOT": TEMP_ROOT, "CONTROLS_ROOT": CONTROLS_ROOT,
        "CONTROLS_ZIP": CONTROLS_ZIP, "READBACK_ROOT": READBACK_ROOT,
        "STATE_PATH": STATE_PATH, "RECEIPT_ROOT": RECEIPT_ROOT,
        "RECEIPT_TAG": RECEIPT_TAG, "PREDECESSOR_RECEIPT": PREDECESSOR_RECEIPT,
        "REPLACED_NAMES": REPLACED_NAMES, "OLD_DESCRIPTION_ADDITION": OLD_DESCRIPTION,
        "DESCRIPTION_ADDITION": DESCRIPTION, "OLD_NOTES_ADDITION": OLD_NOTES,
        "NOTES_ADDITION": NOTES, "PDF_NAME": PDF_NAME, "TEX_NAME": TEX_NAME,
        "SOURCE_ZIP_NAME": SOURCE_ZIP_NAME, "IMAGE_ZIP_NAME": BUNDLE_NAME,
        "expected_retained": expected_retained, "ordered_names": ordered_names,
    }
    for name, value in values.items():
        setattr(prior, name, value)


def ensure_subject(session, token: str, draft_id: int) -> None:
    headers = prior.auth_headers(token)
    draft = base.check(session.get(
        f"{API}/records/{draft_id}/draft?expand=true", headers=headers, timeout=(30, 180)
    ), {200}).json()
    metadata = copy.deepcopy(draft["metadata"])
    subjects = metadata.setdefault("subjects", [])
    existing = {row.get("subject") for row in subjects}
    for subject in ("SGA7 II English translation", "complete SGA7 II working reader"):
        if subject not in existing:
            subjects.append({"subject": subject})
    payload = {
        "access": draft["access"],
        "files": {"enabled": True, "default_preview": draft["files"].get("default_preview"), "order": draft["files"].get("order", [])},
        "metadata": metadata, "custom_fields": draft.get("custom_fields", {}),
    }
    if draft.get("pids"):
        payload["pids"] = draft["pids"]
    base.check(session.put(
        f"{API}/records/{draft_id}/draft", headers={**headers, "Content-Type": "application/json"},
        json=payload, timeout=(30, 300)
    ), {200})


def resumable_predecessor(
    session, token: str, draft_id: int, predecessor: dict[str, object],
    local: dict[str, dict[str, object]], controls: dict[str, object],
) -> dict[str, object]:
    deposition = base.check(session.get(
        f"{API}/deposit/depositions/{draft_id}", headers={"Authorization": f"Bearer {token}"}, timeout=(30, 180)
    ), {200}).json()
    files = base.legacy_entries(deposition)
    predecessor_files = predecessor["outer_file_readback"]
    full_names = set(predecessor_files)
    retained = expected_retained(predecessor)
    allowed = full_names | set(local) | {CONTROLS_NAME}
    current_names = set(files)
    if not set(retained).issubset(current_names):
        raise RuntimeError("Interrupted SGA draft lost a retained predecessor file")
    if not current_names.issubset(allowed):
        raise RuntimeError("Interrupted SGA draft contains an unexpected file")
    if not (full_names - current_names).issubset(REPLACED_NAMES):
        raise RuntimeError("Interrupted SGA draft lost an unreplaced predecessor file")
    staged = {**local, CONTROLS_NAME: controls}
    for name in current_names & set(staged):
        observed = int(files[name]["filesize"]), base.normalized_md5(files[name]["checksum"])
        wanted = int(staged[name]["bytes"]), str(staged[name]["md5"]).lower()
        if observed != wanted:
            raise RuntimeError(f"Interrupted SGA staged identity changed: {name}")
    if full_names.issubset(current_names):
        return predecessor
    if CONTROLS_NAME in current_names:
        raise RuntimeError("Interrupted SGA draft already staged controls")
    resumed = copy.deepcopy(predecessor)
    resumed["outer_file_readback"] = {name: predecessor_files[name] for name in retained}
    return resumed


def public_readback(
    session, token: str, record_id: int, local: dict[str, dict[str, object]],
    controls: dict[str, object], predecessor: dict[str, object], github: dict[str, object],
) -> dict[str, object]:
    record = None
    for _ in range(120):
        response = session.get(
            f"{API}/records/{record_id}?expand=true", headers=prior.public_headers(), timeout=(30, 180)
        )
        if response.status_code == 200 and response.json().get("is_published"):
            candidate = response.json()
            if len(base.modern_entries(candidate)) == FINAL_FILES:
                record = candidate
                break
        time.sleep(2)
    if record is None:
        raise RuntimeError("Published SGA successor did not become public")
    retained = expected_retained(predecessor)
    expected = {**retained, **local, CONTROLS_NAME: controls}
    entries = base.modern_entries(record)
    latest = base.check(session.get(
        f"{API}/records/{PREDECESSOR_RECORD}/versions/latest?expand=true",
        headers=prior.public_headers(), timeout=(30, 180)
    ), {200}).json()
    if (
        set(entries) != set(expected) or len(entries) != FINAL_FILES
        or record["parent"]["pids"]["doi"]["identifier"] != CONCEPT_DOI
        or record["files"].get("default_preview") != DEFAULT_PREVIEW
        or record["files"].get("order") != ordered_names(set(expected))
        or record["metadata"].get("version") != VERSION
        or record["metadata"].get("description", "").strip() != DESCRIPTION
        or metadata_notes(record["metadata"]) != [NOTES]
        or int(latest["id"]) != record_id
    ):
        raise RuntimeError("Public SGA successor boundary changed")
    resolved = READBACK_ROOT.resolve()
    if not resolved.is_relative_to((REPO_ROOT / "tmp").resolve()):
        raise RuntimeError("Refusing public readback outside repository tmp")
    shutil.rmtree(READBACK_ROOT, ignore_errors=True)
    READBACK_ROOT.mkdir(parents=True)
    files: dict[str, dict[str, object]] = {}
    archives: dict[str, dict[str, object]] = {}
    archive_names = {BUNDLE_NAME, SOURCE_ZIP_NAME, CONTROLS_NAME}
    try:
        for index, name in enumerate(sorted(entries, key=str.casefold), start=1):
            print(f"PUBLIC READBACK {index}/{len(entries)} {name}", flush=True)
            destination = READBACK_ROOT / f"archive-{index:03d}.zip" if name in archive_names else None
            observed = prior.stream_download(session, entries[name]["links"]["content"], destination)
            wanted = int(expected[name]["bytes"]), str(expected[name]["sha256"]).upper(), str(expected[name]["md5"]).lower()
            if observed != wanted:
                raise RuntimeError(f"Public SGA mismatch: {name}")
            files[name] = {
                "bytes": observed[0], "sha256": observed[1], "md5": observed[2],
                "content_url": entries[name]["links"]["content"], "match": True,
                "readback_mode": "anonymous_full_download_exact_sha256",
            }
            if destination is not None:
                inventory = prior.zip_inventory(destination)
                if inventory["member_identities"] != expected[name]["inventory"]["member_identities"]:
                    raise RuntimeError(f"Public ZIP member drift: {name}")
                inventory["match"] = True
                archives[name] = inventory
    finally:
        shutil.rmtree(READBACK_ROOT, ignore_errors=True)
    retained_errors = [name for name in retained if files[name]["sha256"] != str(retained[name]["sha256"]).upper()]
    if (
        len(files) != FINAL_FILES or retained_errors
        or int(archives[SOURCE_ZIP_NAME]["members"]) != EXPECTED_SOURCE_ZIP_MEMBERS
        or int(archives[BUNDLE_NAME]["members"]) != int(local[BUNDLE_NAME]["inventory"]["members"])
    ):
        raise RuntimeError("SGA public readback did not close")
    prior.assert_no_open_draft(session, token, record_id)
    result = {
        "status": "PASS_PUBLIC_READBACK", "errors": [], "record_id": record_id,
        "record_url": record["links"]["self_html"], "doi": record["pids"]["doi"]["identifier"],
        "concept_doi": CONCEPT_DOI, "predecessor_record": PREDECESSOR_RECORD,
        "version": VERSION, "outer_files": len(files),
        "outer_bytes": sum(int(row["bytes"]) for row in files.values()),
        "outer_file_readback": files, "retained_predecessor_files": len(retained),
        "retained_predecessor_identity_errors": retained_errors,
        "replaced_files": sorted(REPLACED_NAMES), "added_files": sorted(local),
        "default_preview": record["files"].get("default_preview"), "latest_record": int(latest["id"]),
        "github": {"commit": github["commit"], "package_path": github["package_path"],
                   "files_read_back": github["files_read_back"], "bytes_read_back": github["bytes_read_back"]},
        "reader_pages": 264, "reader_sha256": EXPECTED_PDF[1],
        "source_zip_members": EXPECTED_SOURCE_ZIP_MEMBERS,
        "current_bundle_members": int(archives[BUNDLE_NAME]["members"]),
        "scope": "complete SGA7 II English working reader, Exposes X-XXII through volume EOF",
        "complete_sga7ii_working_translation": True, "complete_cross_sga_reader_claim": False,
        "exhaustive_reference_claim": False, "duplicate_concept_created": False,
        "active_draft_remaining": False,
    }
    zip_result = {
        "status": "PASS", "errors": [], "record_id": record_id, "doi": result["doi"],
        "zip_archive_count": len(archives),
        "zip_member_count": sum(int(row["members"]) for row in archives.values()),
        "archives": archives,
    }
    base.save_json(RECEIPT_ROOT / f"{RECEIPT_TAG}_record_{record_id}_public_readback.json", result)
    base.save_json(RECEIPT_ROOT / f"{RECEIPT_TAG}_record_{record_id}_zip_member_readback.json", zip_result)
    (RECEIPT_ROOT / f"{RECEIPT_TAG}_record_{record_id}.md").write_text("\n".join([
        "# Complete SGA7 II English publication receipt", "",
        f"- Record: <https://zenodo.org/records/{record_id}>", f"- DOI: `{result['doi']}`",
        f"- Concept DOI: `{CONCEPT_DOI}`", f"- GitHub package commit: `{GITHUB_PACKAGE_COMMIT}`",
        f"- Public files: {len(files)} / {result['outer_bytes']:,} bytes",
        f"- Retained predecessor files: {len(retained)} / identity errors 0",
        f"- Reader: 264 pages / SHA-256 `{EXPECTED_PDF[1]}`",
        f"- Reader/source ZIP: {EXPECTED_SOURCE_ZIP_MEMBERS} members / SHA-256 `{EXPECTED_SOURCE_ZIP[1]}`",
        f"- All-current-reader bundle: {archives[BUNDLE_NAME]['members']} members / SHA-256 `{local[BUNDLE_NAME]['sha256']}`",
        "- Scope: Exposes X-XXII through volume EOF; complete SGA7 II working translation",
        "- No cumulative cross-SGA or exhaustive-reference claim",
        f"- Default preview: `{DEFAULT_PREVIEW}`", "- Duplicate concept created: no",
        "- Active draft remaining: no", "",
    ]), encoding="utf-8", newline="\n")
    return result


def prepare(latest_record: int = PREDECESSOR_RECORD):
    configure_prior()
    predecessor = load_predecessor(latest_record)
    local = local_uploads(predecessor)
    github = verify_github()
    controls = build_controls(local, predecessor, github)
    return local, predecessor, github, controls


def preflight() -> dict[str, object]:
    local, predecessor, github, controls = prepare()
    token = base.find_token()
    session = base.make_session()
    prior.fetch_live(session, predecessor)
    prior.assert_no_untracked_draft(session, token)
    return {
        "status": "PASS_PREFLIGHT", "predecessor_record": PREDECESSOR_RECORD,
        "concept_doi": CONCEPT_DOI, "retained_files": len(expected_retained(predecessor)),
        "replaced_files": sorted(REPLACED_NAMES), "added_files": sorted(local),
        "final_files": FINAL_FILES, "default_preview": DEFAULT_PREVIEW,
        "github_commit": github["commit"],
        "uploads": {name: {"bytes": row["bytes"], "sha256": row["sha256"]} for name, row in local.items()},
        "controls_zip": {"bytes": controls["bytes"], "sha256": controls["sha256"], "members": controls["inventory"]["members"]},
        "duplicate_concept_created": False,
    }


def publish() -> dict[str, object]:
    local, predecessor, github, controls = prepare()
    token = base.find_token()
    session = base.make_session()
    live = prior.fetch_live(session, predecessor)
    prior.assert_no_untracked_draft(session, token)
    draft_id = prior.create_or_resume_draft(session, token, live)
    ensure_subject(session, token, draft_id)
    staged_predecessor = resumable_predecessor(session, token, draft_id, predecessor, local, controls)
    published = prior.stage_and_publish(session, token, live, draft_id, local, controls, staged_predecessor)
    return public_readback(session, token, int(published["id"]), local, controls, predecessor, github)


def readback(record_id: int) -> dict[str, object]:
    local, predecessor, github, controls = prepare(record_id)
    token = base.find_token()
    session = base.make_session()
    return public_readback(session, token, record_id, local, controls, predecessor, github)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--preflight", action="store_true")
    parser.add_argument("--readback-record", type=int)
    args = parser.parse_args()
    if args.preflight and args.readback_record is not None:
        parser.error("--preflight and --readback-record are mutually exclusive")
    result = preflight() if args.preflight else (
        readback(args.readback_record) if args.readback_record is not None else publish()
    )
    print(json.dumps(result, indent=2, ensure_ascii=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
