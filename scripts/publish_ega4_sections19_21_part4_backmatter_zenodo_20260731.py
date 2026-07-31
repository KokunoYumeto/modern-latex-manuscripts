#!/usr/bin/env python3
"""Publish the EGA IV Sections 19-21, Part 4, and p333-336 witnesses."""

from __future__ import annotations

import csv
import hashlib
import io
import json
import os
import shutil
import time
import zipfile
from pathlib import Path

import publish_ega4_source_image_witness_p087_105_zenodo_20260731 as publisher


core = publisher.base

publisher.PREDECESSOR_RECORD = 21_714_901
publisher.PREDECESSOR_DOI = "10.5281/zenodo.21714901"
publisher.EXPECTED_PREDECESSOR_FILES = 41
publisher.EXPECTED_PREDECESSOR_BYTES = 3_729_694_469
publisher.EXPECTED_FINAL_FILES = 44
publisher.EXPECTED_FINAL_BYTES = 3_745_045_609
publisher.EXPECTED_SOURCE_IMAGES = 4
publisher.EXPECTED_ZIP_MEMBERS = 27
publisher.VERSION = (
    "2026-07-31 EGA IV Sections 19-21 and Part 4 backmatter working reader"
)
publisher.GITHUB_COMMIT = "bf2cb0663e30099a797ca4d2e82943cf5d874e56"
publisher.GITHUB_PATH = (
    "sources/ega/checkpoints/"
    "ega4-sections19-21-part4-backmatter-working-20260731"
)
publisher.ZIP_ROOT = Path(os.environ["LOCALAPPDATA"]) / "Temp"
publisher.READBACK_ROOT = Path(os.environ["LOCALAPPDATA"]) / "Temp" / (
    "ega4_sections19_21_part4_backmatter_readback_20260731"
)
publisher.PREDECESSOR_RECEIPT = publisher.RECEIPT_ROOT / (
    "20260731_ega4_source_image_witness_p282_332_"
    "record_21714901_public_readback.json"
)
publisher.RECEIPT_TAG = "20260731_ega4_sections19_21_part4_backmatter"
publisher.DRAFT_STATE = publisher.RECEIPT_ROOT / (
    f"{publisher.RECEIPT_TAG}_zenodo_draft_state.json"
)

REPO_ROOT = Path(__file__).resolve().parent.parent
READER_PATH = REPO_ROOT / (
    "sources/ega/checkpoints/"
    "ega4-sections19-21-part4-backmatter-working-20260731/reader/"
    "EGA4_Sections19_21_Part4_Backmatter_English_Working_20260731.pdf"
)
SOURCE_ZIP_PATH = Path(os.environ["LOCALAPPDATA"]) / "Temp" / (
    "02f_EGAIV_English_Sections19_21_Part4_Backmatter_TeX_PDF_20260731.zip"
)
IMAGE_ZIP_PATH = Path(os.environ["LOCALAPPDATA"]) / "Temp" / (
    "ega4_part4_p333_336_upload_20260731/"
    "89e EGA IV - Source Image Witnesses Printed 333-336 "
    "(1800dpi) 20260731.zip"
)

publisher.NEW_FILES = {
    "00f_EGAIV_English_Sections19_21_Part4_Backmatter_Working_20260731.pdf": {
        "kind": "pdf",
        "source": READER_PATH,
        "bytes": 861_609,
        "sha256": (
            "AC4031BDB6BA5C4AAC9FA569CD28FDDB477026FB744B04DBACC6F9DFB9F1C108"
        ),
    },
    "02f_EGAIV_English_Sections19_21_Part4_Backmatter_TeX_PDF_20260731.zip": {
        "kind": "zip",
        "source": SOURCE_ZIP_PATH,
        "bytes": 1_030_828,
        "sha256": (
            "751F59771BA5C20B1603ABB4F798873BB7A535CD8667C2C751BDAE997E9349D5"
        ),
        "members": 19,
        "uncompressed_bytes": 1_597_868,
    },
    "89e EGA IV - Source Image Witnesses Printed 333-336 "
    "(1800dpi) 20260731.zip": {
        "kind": "zip",
        "source": IMAGE_ZIP_PATH,
        "bytes": 13_458_703,
        "sha256": (
            "CA2BB33A1FBAC6541C157B3C76F45FE217E7DD0FFF57940470A0628C1CF2CE0C"
        ),
        "members": 8,
        "images": 4,
        "uncompressed_bytes": 13_456_603,
    },
}

publisher.DESCRIPTION_ADDITION = (
    "<p><strong>EGA IV Sections 19-21 and Part 4 backmatter:</strong> "
    "this successor adds a directly readable 134-page working English reader "
    "covering Sections 19-21 (printed pages 185-332), the bibliography, notation "
    "and terminology indexes, contents, and Errata/Addenda List 3 (printed pages "
    "333-343 and 345-361). A compact source ZIP contains the editable TeX, build "
    "harness, reader, and public validation controls. It is a bounded reader, not "
    "a cumulative EGA IV Sections 1-21 reader; the direct cumulative EGA IV reader "
    "on this record remains the Sections 1-10 edition.</p>"
    "<p><strong>Actual source-image witnesses through printed page 336:</strong> "
    "archive 89e contains four publicly available scan-derived full-page PNG "
    "witnesses at 1800 dpi for printed pages 333-336. These are source images used "
    "for the transcription, not screenshots of the English PDF. Every image is "
    "bound to physical and printed page, dimensions, resolution, SHA-256, linked "
    "TeX units, and QA disposition. Together with archives 84-89d, the public EGA "
    "IV source-image surface contains 989 actual images and covers printed pages "
    "5-336 continuously.</p>"
)
publisher.NOTES_ADDITION = (
    "<p>Files 00f and 02f preserve the bounded Sections 19-21 and Part 4 working "
    "reader. Archive 89e preserves the actual high-detail source-scan witnesses "
    "for printed pages 333-336. EGA 0 remains the default browser preview.</p>"
)


def validate_internal_manifest(
    path: Path, inventory: dict[str, object]
) -> None:
    """Require manifest closure with either rooted or root-relative paths."""
    members = inventory["member_identities"]
    manifest_names = [name for name in members if name.endswith("/SHA256SUMS.csv")]
    if len(manifest_names) != 1:
        raise RuntimeError(f"ZIP manifest count changed: {path.name}")
    manifest_name = manifest_names[0]
    root = manifest_name.rsplit("/", 1)[0]
    with zipfile.ZipFile(path) as archive:
        rows = list(
            csv.DictReader(
                io.StringIO(archive.read(manifest_name).decode("utf-8-sig"))
            )
        )
    expected_names = set(members) - {manifest_name}
    observed_names: set[str] = set()
    for row in rows:
        supplied = row["path"]
        candidates = (supplied, f"{root}/{supplied}")
        name = next((candidate for candidate in candidates if candidate in expected_names), None)
        if name is None:
            raise RuntimeError(f"ZIP manifest path changed: {supplied}")
        observed = members[name]
        expected = (int(row["bytes"]), row["sha256"].upper())
        if (int(observed["bytes"]), str(observed["sha256"])) != expected:
            raise RuntimeError(f"ZIP manifest identity mismatch: {name}")
        observed_names.add(name)
    if len(rows) != len(expected_names) or observed_names != expected_names:
        raise RuntimeError(f"ZIP manifest closure changed: {path.name}")


def verify_local() -> dict[str, dict[str, object]]:
    """Verify the direct reader and both ZIPs before any remote mutation."""
    local: dict[str, dict[str, object]] = {}
    for name, expected in publisher.NEW_FILES.items():
        path = Path(expected["source"])
        observed = (path.stat().st_size, publisher.sha256_path(path))
        wanted = (int(expected["bytes"]), str(expected["sha256"]))
        if observed != wanted:
            raise RuntimeError(f"Local EGA IV artifact changed: {name}")
        row: dict[str, object] = {
            "path": path,
            "bytes": observed[0],
            "sha256": observed[1],
            "md5": publisher.md5_path(path),
            "kind": expected["kind"],
        }
        if expected["kind"] == "zip":
            inventory = publisher.zip_inventory(path)
            if (
                int(inventory["members"]) != int(expected["members"])
                or int(inventory["uncompressed_bytes"])
                != int(expected["uncompressed_bytes"])
            ):
                raise RuntimeError(f"Local EGA IV ZIP inventory changed: {name}")
            validate_internal_manifest(path, inventory)
            if "images" in expected:
                image_members = sum(
                    member.lower().endswith(".png")
                    for member in inventory["member_identities"]
                )
                if image_members != int(expected["images"]):
                    raise RuntimeError(f"Local EGA IV image count changed: {name}")
            row["inventory"] = inventory
        local[name] = row
    if sum(int(row["bytes"]) for row in local.values()) != (
        publisher.EXPECTED_FINAL_BYTES - publisher.EXPECTED_PREDECESSOR_BYTES
    ):
        raise RuntimeError("Local EGA IV successor byte boundary changed")
    return local


def public_readback(
    session,
    record_id: int,
    local: dict[str, dict[str, object]],
    predecessor: dict,
) -> dict:
    """Stream-hash all outer files and replay every new ZIP member."""
    record = None
    for _ in range(120):
        response = session.get(
            f"{publisher.API}/records/{record_id}?expand=true",
            headers=publisher.public_headers(),
            timeout=(30, 180),
        )
        if response.status_code == 200 and response.json().get("is_published"):
            candidate = response.json()
            if len(core.modern_entries(candidate)) == publisher.EXPECTED_FINAL_FILES:
                record = candidate
                break
        time.sleep(2)
    if record is None:
        raise RuntimeError("Published EGA IV successor did not become public")
    entries = core.modern_entries(record)
    expected_names = set(predecessor["files"]) | set(publisher.NEW_FILES)
    if (
        set(entries) != expected_names
        or record["parent"]["pids"]["doi"]["identifier"]
        != publisher.CONCEPT_DOI
        or record["files"].get("default_preview") != publisher.DEFAULT_PREVIEW
        or record["metadata"].get("version") != publisher.VERSION
    ):
        raise RuntimeError("Public EGA IV successor boundary changed")
    latest = core.check(
        session.get(
            f"{publisher.API}/records/{publisher.PREDECESSOR_RECORD}/versions/latest"
            "?expand=true",
            headers=publisher.public_headers(),
            timeout=(30, 180),
        ),
        {200},
    ).json()
    if int(latest["id"]) != record_id:
        raise RuntimeError("Published EGA IV successor is not concept head")

    shutil.rmtree(publisher.READBACK_ROOT, ignore_errors=True)
    publisher.READBACK_ROOT.mkdir(parents=True)
    files: dict[str, dict[str, object]] = {}
    archives: dict[str, dict[str, object]] = {}
    try:
        for index, name in enumerate(sorted(entries, key=str.casefold), start=1):
            print(f"PUBLIC READBACK {index}/{len(entries)} {name}", flush=True)
            destination = None
            if name in local and local[name]["kind"] == "zip":
                digest = hashlib.sha256(name.encode("utf-8")).hexdigest()[:16]
                destination = publisher.READBACK_ROOT / f"{digest}.zip"
            observed = publisher.stream_download(
                session, entries[name]["links"]["content"], destination
            )
            expected = local.get(name, predecessor["files"].get(name))
            wanted = (
                int(expected["bytes"]),
                str(expected["sha256"]).upper(),
                str(expected["md5"]).lower(),
            )
            if observed != wanted:
                raise RuntimeError(f"Public EGA IV artifact mismatch: {name}")
            files[name] = {
                "bytes": observed[0],
                "sha256": observed[1],
                "md5": observed[2],
                "url": entries[name]["links"]["content"],
                "match": True,
                "readback_mode": "anonymous_full_download_exact_sha256",
            }
            if destination is not None:
                summary = publisher.zip_inventory(destination)
                if summary["member_identities"] != local[name]["inventory"][
                    "member_identities"
                ]:
                    raise RuntimeError(f"Public EGA IV ZIP member drift: {name}")
                summary["match"] = True
                archives[name] = summary
                destination.unlink()
    finally:
        shutil.rmtree(publisher.READBACK_ROOT, ignore_errors=True)
    if (
        len(files) != publisher.EXPECTED_FINAL_FILES
        or sum(int(row["bytes"]) for row in files.values())
        != publisher.EXPECTED_FINAL_BYTES
        or len(archives) != 2
        or sum(int(row["members"]) for row in archives.values())
        != publisher.EXPECTED_ZIP_MEMBERS
    ):
        raise RuntimeError("EGA IV public readback did not close")

    result = {
        "status": "PASS_PUBLIC_READBACK",
        "errors": [],
        "record": record_id,
        "record_url": record["links"]["self_html"],
        "doi": record["pids"]["doi"]["identifier"],
        "conceptdoi": publisher.CONCEPT_DOI,
        "predecessor_record": publisher.PREDECESSOR_RECORD,
        "version": publisher.VERSION,
        "file_count": len(files),
        "bytes": sum(int(row["bytes"]) for row in files.values()),
        "files": files,
        "latest_record": int(latest["id"]),
        "rdm_default_preview": record["files"].get("default_preview"),
        "rdm_file_order": record["files"].get("order"),
        "effective_order": "alphanumeric_default",
        "github_commit": publisher.GITHUB_COMMIT,
        "github_path": publisher.GITHUB_PATH,
        "retained_predecessor_files": publisher.EXPECTED_PREDECESSOR_FILES,
        "added_artifacts": len(publisher.NEW_FILES),
        "added_source_images": publisher.EXPECTED_SOURCE_IMAGES,
        "added_zip_members": publisher.EXPECTED_ZIP_MEMBERS,
        "duplicate_concept_created": False,
        "second_draft_created": False,
    }
    zipped = {
        "status": "PASS",
        "errors": [],
        "record": record_id,
        "doi": record["pids"]["doi"]["identifier"],
        "zip_archive_count": len(archives),
        "zip_member_count": sum(int(row["members"]) for row in archives.values()),
        "archives": archives,
    }
    core.save_json(
        publisher.RECEIPT_ROOT
        / f"{publisher.RECEIPT_TAG}_record_{record_id}_public_readback.json",
        result,
    )
    core.save_json(
        publisher.RECEIPT_ROOT
        / f"{publisher.RECEIPT_TAG}_record_{record_id}_zip_member_readback.json",
        zipped,
    )
    return result


publisher.verify_local = verify_local
publisher.public_readback = public_readback


if __name__ == "__main__":
    raise SystemExit(publisher.main())
