#!/usr/bin/env python3
"""Publish the EGA IV printed 087-105 source-image witness ZIP."""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import io
import json
import os
import re
import shutil
import time
import zipfile
from pathlib import Path, PurePosixPath
from urllib.parse import quote

import publish_current_reader_bundles_zenodo_20260730 as base


API = base.API
PUBLICATION_DATE = "2026-07-31"
PREDECESSOR_RECORD = 21_712_025
PREDECESSOR_DOI = "10.5281/zenodo.21712025"
CONCEPT_DOI = "10.5281/zenodo.20414353"
EXPECTED_PREDECESSOR_FILES = 32
EXPECTED_PREDECESSOR_BYTES = 1_413_291_979
EXPECTED_FINAL_FILES = 33
EXPECTED_FINAL_BYTES = 1_622_065_440
EXPECTED_SOURCE_IMAGES = 76
EXPECTED_ZIP_MEMBERS = 80
DEFAULT_PREVIEW = (
    "00a_EGA0_English_Complete_Through_Section13_Reference_v2_20260730.pdf"
)
VERSION = "2026-07-31 EGA IV source-image witnesses through printed page 105"
GITHUB_COMMIT = "22b9ba82a7570a3f3f6fc891772f45436555d862"
GITHUB_PATH = (
    "sources/ega/visual-evidence/"
    "ega4-sections16-18-source-image-witnesses-printed087-105-20260731"
)

REPO_ROOT = Path(__file__).resolve().parent.parent
ZIP_ROOT = Path(os.environ["LOCALAPPDATA"]) / "Temp" / (
    "ega4_source_image_witness_p087_105_upload_20260731"
)
READBACK_ROOT = Path(os.environ["LOCALAPPDATA"]) / "Temp" / (
    "ega4_source_image_witness_p087_105_readback_20260731"
)
RECEIPT_ROOT = REPO_ROOT / "manifests" / "published-zenodo"
RECEIPT_TAG = "20260731_ega4_source_image_witness_p087_105"
PREDECESSOR_RECEIPT = RECEIPT_ROOT / (
    "20260731_ega4_source_image_witnesses_record_21712025_public_readback.json"
)
DRAFT_STATE = RECEIPT_ROOT / f"{RECEIPT_TAG}_zenodo_draft_state.json"

NEW_FILES = {
    "86 EGA IV - Source Image Witnesses Printed 087-105 (600-1800dpi) 20260731.zip": {
        "bytes": 208_773_461,
        "sha256": (
            "E89C05E3254FE335146D6E7AB8C47C59039438AF49E29CD4951127067BEC106C"
        ),
        "members": 80,
        "images": 76,
        "uncompressed_bytes": 208_750_301,
    }
}

DESCRIPTION_ADDITION = (
    "<p><strong>EGA IV source-image witnesses through printed page 105:</strong> "
    "this successor adds one ZIP containing 76 actual scan-derived PNG witnesses "
    "from the publicly available NUMDAM EGA IV Part 4 scan already downloadable "
    "on this record. It preserves one 600-dpi full page and three overlapping "
    "1800-dpi bands for each printed page 87-105. Pages 87-104 are bound to the "
    "producer alignment ledger and checkpoint r29; page 105 is explicitly marked "
    "as the active continuation rather than alignment-closed. English-reader "
    "screenshots are excluded. Every member has page, dimensions, resolution, "
    "SHA-256, linked TeX, and QA-disposition metadata.</p>"
)
DESCRIPTION_REPLACEMENTS: tuple[tuple[str, str], ...] = ()
NOTES_ADDITION = (
    "<p>Archive 86 extends the actual EGA IV source-image witness set through "
    "printed page 105. It contains source-scan evidence, not redundant screenshots "
    "of the downloadable English readers. EGA 0 remains the default browser "
    "preview.</p>"
)


def sha256_path(path: Path) -> str:
    return base.sha256_path(path)


def md5_path(path: Path) -> str:
    return base.md5_path(path)


def safe_member(name: str) -> bool:
    pure = PurePosixPath(name)
    return (
        name == name.replace("\\", "/")
        and not pure.is_absolute()
        and ".." not in pure.parts
        and not re.match(r"^[A-Za-z]:", name)
    )


def zip_inventory(path: Path) -> dict[str, object]:
    members: dict[str, dict[str, object]] = {}
    with zipfile.ZipFile(path) as archive:
        if archive.testzip() is not None:
            raise RuntimeError(f"ZIP CRC failure: {path.name}")
        infos = [row for row in archive.infolist() if not row.is_dir()]
        names = [row.filename for row in infos]
        if len(names) != len(set(names)) or not all(map(safe_member, names)):
            raise RuntimeError(f"Unsafe or duplicate ZIP member: {path.name}")
        for info in sorted(infos, key=lambda row: row.filename.casefold()):
            digest = hashlib.sha256()
            size = 0
            with archive.open(info) as handle:
                for chunk in iter(lambda: handle.read(1024 * 1024), b""):
                    digest.update(chunk)
                    size += len(chunk)
            members[info.filename] = {
                "bytes": size,
                "sha256": digest.hexdigest().upper(),
                "crc32": f"{info.CRC:08X}",
            }
    return {
        "status": "PASS",
        "filename": path.name,
        "bytes": path.stat().st_size,
        "sha256": sha256_path(path),
        "members": len(members),
        "uncompressed_bytes": sum(int(row["bytes"]) for row in members.values()),
        "member_identities": members,
    }


def validate_internal_manifest(path: Path, inventory: dict[str, object]) -> None:
    members = inventory["member_identities"]
    manifest_names = [name for name in members if name.endswith("/SHA256SUMS.csv")]
    if len(manifest_names) != 1:
        raise RuntimeError(f"ZIP manifest count changed: {path.name}")
    manifest_name = manifest_names[0]
    with zipfile.ZipFile(path) as archive:
        rows = list(
            csv.DictReader(
                io.StringIO(archive.read(manifest_name).decode("utf-8-sig"))
            )
        )
    expected_names = set(members) - {manifest_name}
    if len(rows) != len(expected_names):
        raise RuntimeError(f"ZIP manifest row count changed: {path.name}")
    for row in rows:
        name = row["path"]
        if name not in expected_names:
            raise RuntimeError(f"ZIP manifest path changed: {name}")
        observed = members[name]
        expected = (int(row["bytes"]), row["sha256"].upper())
        if (int(observed["bytes"]), str(observed["sha256"])) != expected:
            raise RuntimeError(f"ZIP manifest identity mismatch: {name}")
    if {row["path"] for row in rows} != expected_names:
        raise RuntimeError(f"ZIP manifest closure changed: {path.name}")


def verify_local() -> dict[str, dict[str, object]]:
    local: dict[str, dict[str, object]] = {}
    for name, expected in NEW_FILES.items():
        path = ZIP_ROOT / name
        observed = (path.stat().st_size, sha256_path(path))
        if observed != (int(expected["bytes"]), str(expected["sha256"])):
            raise RuntimeError(f"Local source-image ZIP changed: {name}")
        inventory = zip_inventory(path)
        if (
            int(inventory["members"]) != int(expected["members"])
            or int(inventory["uncompressed_bytes"])
            != int(expected["uncompressed_bytes"])
        ):
            raise RuntimeError(f"Local source-image ZIP inventory changed: {name}")
        validate_internal_manifest(path, inventory)
        image_members = sum(
            "/images/authority_" in member and member.endswith(".png")
            for member in inventory["member_identities"]
        )
        if image_members != int(expected["images"]):
            raise RuntimeError(f"Local source-image member count changed: {name}")
        if any(
            "english_checkpoint" in member
            for member in inventory["member_identities"]
        ):
            raise RuntimeError(f"English-reader render leaked into {name}")
        local[name] = {
            "path": path,
            "bytes": observed[0],
            "sha256": observed[1],
            "md5": md5_path(path),
            "inventory": inventory,
        }
    if sum(int(row["bytes"]) for row in local.values()) != (
        EXPECTED_FINAL_BYTES - EXPECTED_PREDECESSOR_BYTES
    ):
        raise RuntimeError("Local source-image ZIP byte boundary changed")
    return local


def load_predecessor_receipt() -> dict:
    receipt = json.loads(PREDECESSOR_RECEIPT.read_text(encoding="utf-8"))
    if (
        receipt.get("status") != "PASS_PUBLIC_READBACK"
        or int(receipt.get("record", -1)) != PREDECESSOR_RECORD
        or receipt.get("doi") != PREDECESSOR_DOI
        or receipt.get("conceptdoi") != CONCEPT_DOI
        or int(receipt.get("file_count", -1)) != EXPECTED_PREDECESSOR_FILES
        or int(receipt.get("bytes", -1)) != EXPECTED_PREDECESSOR_BYTES
        or len(receipt.get("files", {})) != EXPECTED_PREDECESSOR_FILES
    ):
        raise RuntimeError("Controlling EGA predecessor receipt changed")
    return receipt


def public_headers() -> dict[str, str]:
    return {"Accept": "application/vnd.inveniordm.v1+json"}


def auth_headers(token: str) -> dict[str, str]:
    return {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.inveniordm.v1+json",
    }


def fetch_live(session, predecessor: dict) -> dict:
    live = base.check(
        session.get(
            f"{API}/records/{PREDECESSOR_RECORD}?expand=true",
            headers=public_headers(),
            timeout=(30, 180),
        ),
        {200},
    ).json()
    entries = base.modern_entries(live)
    expected = predecessor["files"]
    if (
        int(live["id"]) != PREDECESSOR_RECORD
        or live["pids"]["doi"]["identifier"] != PREDECESSOR_DOI
        or live["parent"]["pids"]["doi"]["identifier"] != CONCEPT_DOI
        or len(entries) != EXPECTED_PREDECESSOR_FILES
        or sum(int(row["size"]) for row in entries.values())
        != EXPECTED_PREDECESSOR_BYTES
        or set(entries) != set(expected)
        or live["files"].get("default_preview") != DEFAULT_PREVIEW
    ):
        raise RuntimeError("Live EGA predecessor boundary changed")
    for name, row in expected.items():
        observed = (
            int(entries[name]["size"]),
            base.normalized_md5(entries[name]["checksum"]),
        )
        wanted = (int(row["bytes"]), row["md5"].lower())
        if observed != wanted:
            raise RuntimeError(f"Live EGA predecessor drift: {name}")
    latest = base.check(
        session.get(
            f"{API}/records/{PREDECESSOR_RECORD}/versions/latest?expand=true",
            headers=public_headers(),
            timeout=(30, 180),
        ),
        {200},
    ).json()
    if int(latest["id"]) != PREDECESSOR_RECORD:
        raise RuntimeError("EGA concept head moved; refusing parallel successor")
    return live


def assert_no_untracked_draft(session, token: str) -> None:
    headers = auth_headers(token)
    if DRAFT_STATE.is_file():
        state = json.loads(DRAFT_STATE.read_text(encoding="utf-8"))
        if state.get("published"):
            raise RuntimeError("Tracked EGA source-image successor is already published")
        base.check(
            session.get(
                f"{API}/records/{int(state['draft_id'])}/draft",
                headers=headers,
                timeout=(30, 60),
            ),
            {200},
        )
        return
    response = session.get(
        f"{API}/records/{PREDECESSOR_RECORD}/draft",
        headers=headers,
        timeout=(30, 60),
    )
    if response.status_code == 200:
        raise RuntimeError("Untracked active EGA successor draft exists")
    base.check(response, {404})


def create_or_resume_draft(session, token: str, live: dict) -> int:
    headers = {"Authorization": f"Bearer {token}"}
    if DRAFT_STATE.is_file():
        state = json.loads(DRAFT_STATE.read_text(encoding="utf-8"))
        draft_id = int(state["draft_id"])
        base.check(
            session.get(
                f"{API}/records/{draft_id}/draft",
                headers=auth_headers(token),
                timeout=(30, 60),
            ),
            {200},
        )
        return draft_id
    predecessor = base.check(
        session.get(
            f"{API}/deposit/depositions/{PREDECESSOR_RECORD}",
            headers=headers,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    if (
        predecessor.get("state") != "done"
        or not predecessor.get("submitted")
        or not predecessor.get("links", {}).get("newversion")
    ):
        raise RuntimeError("Live EGA predecessor is not a versioning base")
    created = base.check(
        session.post(
            predecessor["links"]["newversion"],
            headers=headers,
            timeout=(30, 300),
        ),
        {201},
    ).json()
    deposition = base.check(
        session.get(
            created["links"]["latest_draft"],
            headers=headers,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    if set(base.legacy_entries(deposition)) != set(base.modern_entries(live)):
        raise RuntimeError("EGA successor did not inherit predecessor exactly")
    draft_id = int(deposition["id"])
    base.save_json(
        DRAFT_STATE,
        {
            "status": "OPEN_TRACKED_DRAFT",
            "predecessor_record": PREDECESSOR_RECORD,
            "draft_id": draft_id,
            "concept_doi": CONCEPT_DOI,
            "published": False,
        },
    )
    return draft_id


def upload_file(session, token: str, bucket: str, name: str, path: Path) -> None:
    with path.open("rb") as handle:
        base.check(
            session.put(
                f"{bucket.rstrip('/')}/{quote(name, safe='')}",
                headers={
                    "Authorization": f"Bearer {token}",
                    "Content-Type": "application/octet-stream",
                },
                data=handle,
                timeout=(30, 3600),
            ),
            {200, 201},
        )


def stage_and_publish(
    session,
    token: str,
    live: dict,
    draft_id: int,
    local: dict[str, dict[str, object]],
    predecessor: dict,
) -> dict:
    legacy_headers = {"Authorization": f"Bearer {token}"}
    deposition = base.check(
        session.get(
            f"{API}/deposit/depositions/{draft_id}",
            headers=legacy_headers,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    files = base.legacy_entries(deposition)
    if set(files) != set(predecessor["files"]):
        raise RuntimeError("Tracked EGA draft inherited file set changed")
    bucket = deposition["links"]["bucket"]
    for index, name in enumerate(NEW_FILES, start=1):
        print(f"UPLOAD {index}/{len(NEW_FILES)} {name}", flush=True)
        upload_file(session, token, bucket, name, local[name]["path"])

    headers = auth_headers(token)
    draft = base.check(
        session.get(
            f"{API}/records/{draft_id}/draft?expand=true",
            headers=headers,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    entries = base.modern_entries(draft)
    expected_names = set(predecessor["files"]) | set(NEW_FILES)
    if set(entries) != expected_names or len(entries) != EXPECTED_FINAL_FILES:
        raise RuntimeError("Staged EGA source-image file set changed")
    for name, entry in entries.items():
        expected = local.get(name, predecessor["files"].get(name))
        observed = (
            int(entry["size"]),
            base.normalized_md5(entry["checksum"]),
        )
        wanted = (int(expected["bytes"]), str(expected["md5"]).lower())
        if observed != wanted:
            raise RuntimeError(f"Staged EGA source-image identity changed: {name}")

    metadata = copy.deepcopy(draft["metadata"])
    metadata["version"] = VERSION
    metadata["publication_date"] = PUBLICATION_DATE
    description = metadata.get("description", "")
    for old, new in DESCRIPTION_REPLACEMENTS:
        if old not in description:
            raise RuntimeError("Expected predecessor description text is absent")
        description = description.replace(old, new, 1)
    if DESCRIPTION_ADDITION not in description:
        description += "\n" + DESCRIPTION_ADDITION
    metadata["description"] = description
    subjects = metadata.setdefault("subjects", [])
    existing_subjects = {row.get("subject") for row in subjects}
    for subject in (
        "EGA IV source-image witnesses",
        "high-detail mathematical source crops",
    ):
        if subject not in existing_subjects:
            subjects.append({"subject": subject})
    additions = metadata.get("additional_descriptions", [])
    note_rows = [row for row in additions if row.get("type", {}).get("id") != "notes"]
    previous_notes = " ".join(
        row.get("description", "")
        for row in additions
        if row.get("type", {}).get("id") == "notes"
    )
    note_rows.append(
        {
            "description": previous_notes + NOTES_ADDITION,
            "type": {"id": "notes", "title": {"en": "Notes"}},
        }
    )
    metadata["additional_descriptions"] = note_rows
    payload = {
        "access": draft["access"],
        "files": {
            "enabled": True,
            "default_preview": DEFAULT_PREVIEW,
            "order": [],
        },
        "metadata": metadata,
        "custom_fields": draft.get("custom_fields", {}),
    }
    if draft.get("pids"):
        payload["pids"] = draft["pids"]
    patched = base.check(
        session.put(
            f"{API}/records/{draft_id}/draft",
            headers={**headers, "Content-Type": "application/json"},
            json=payload,
            timeout=(30, 300),
        ),
        {200},
    ).json()
    if (
        set(base.modern_entries(patched)) != expected_names
        or patched["files"].get("default_preview") != DEFAULT_PREVIEW
        or patched["metadata"].get("version") != VERSION
    ):
        raise RuntimeError("Patched EGA source-image draft controls changed")
    base.save_json(
        RECEIPT_ROOT
        / f"{RECEIPT_TAG}_record_{draft_id}_draft_files.json",
        {
            "status": "PASS_STAGED",
            "errors": [],
            "predecessor_record": PREDECESSOR_RECORD,
            "draft_id": draft_id,
            "concept_doi": CONCEPT_DOI,
            "files": len(entries),
            "retained_files": EXPECTED_PREDECESSOR_FILES,
            "added_files": len(NEW_FILES),
            "default_preview": DEFAULT_PREVIEW,
            "duplicate_concept_created": False,
            "second_draft_created": False,
        },
    )
    published = base.check(
        session.post(
            patched["links"]["publish"],
            headers=headers,
            timeout=(30, 900),
        ),
        {200, 202},
    ).json()
    if (
        int(published["id"]) != draft_id
        or published["parent"]["pids"]["doi"]["identifier"] != CONCEPT_DOI
    ):
        raise RuntimeError("Published EGA source-image response escaped the concept")
    state = json.loads(DRAFT_STATE.read_text(encoding="utf-8"))
    state.update(
        {
            "status": "PUBLISHED_TRACKED_SUCCESSOR",
            "published": True,
            "record_id": draft_id,
            "doi": published["pids"]["doi"]["identifier"],
        }
    )
    base.save_json(DRAFT_STATE, state)
    base.save_json(
        RECEIPT_ROOT
        / f"{RECEIPT_TAG}_record_{draft_id}_publish_response.json",
        {
            "status": "PUBLISH_ACCEPTED",
            "errors": [],
            "record_id": draft_id,
            "doi": published["pids"]["doi"]["identifier"],
            "concept_doi": CONCEPT_DOI,
        },
    )
    return published


def stream_download(session, url: str, destination: Path | None) -> tuple[int, str, str]:
    sha = hashlib.sha256()
    md5 = hashlib.md5(usedforsecurity=False)
    size = 0
    output = destination.open("wb") if destination is not None else None
    try:
        with base.check(session.get(url, stream=True, timeout=(30, 3600)), {200}) as response:
            for block in response.iter_content(4 * 1024 * 1024):
                if not block:
                    continue
                sha.update(block)
                md5.update(block)
                size += len(block)
                if output is not None:
                    output.write(block)
    finally:
        if output is not None:
            output.close()
    return size, sha.hexdigest().upper(), md5.hexdigest().lower()


def public_readback(
    session,
    record_id: int,
    local: dict[str, dict[str, object]],
    predecessor: dict,
) -> dict:
    record = None
    for _ in range(120):
        response = session.get(
            f"{API}/records/{record_id}?expand=true",
            headers=public_headers(),
            timeout=(30, 180),
        )
        if response.status_code == 200 and response.json().get("is_published"):
            candidate = response.json()
            if len(base.modern_entries(candidate)) == EXPECTED_FINAL_FILES:
                record = candidate
                break
        time.sleep(2)
    if record is None:
        raise RuntimeError("Published EGA source-image successor did not become public")
    entries = base.modern_entries(record)
    expected_names = set(predecessor["files"]) | set(NEW_FILES)
    if (
        set(entries) != expected_names
        or record["parent"]["pids"]["doi"]["identifier"] != CONCEPT_DOI
        or record["files"].get("default_preview") != DEFAULT_PREVIEW
        or record["metadata"].get("version") != VERSION
    ):
        raise RuntimeError("Public EGA source-image successor boundary changed")
    latest = base.check(
        session.get(
            f"{API}/records/{PREDECESSOR_RECORD}/versions/latest?expand=true",
            headers=public_headers(),
            timeout=(30, 180),
        ),
        {200},
    ).json()
    if int(latest["id"]) != record_id:
        raise RuntimeError("Published EGA source-image successor is not concept head")

    shutil.rmtree(READBACK_ROOT, ignore_errors=True)
    READBACK_ROOT.mkdir(parents=True)
    files: dict[str, dict[str, object]] = {}
    archives: dict[str, dict[str, object]] = {}
    try:
        for index, name in enumerate(sorted(entries, key=str.casefold), start=1):
            print(f"PUBLIC READBACK {index}/{len(entries)} {name}", flush=True)
            destination = READBACK_ROOT / "remote.zip" if name in local else None
            observed = stream_download(session, entries[name]["links"]["content"], destination)
            expected = local.get(name, predecessor["files"].get(name))
            wanted = (
                int(expected["bytes"]),
                str(expected["sha256"]).upper(),
                str(expected["md5"]).lower(),
            )
            if observed != wanted:
                raise RuntimeError(f"Public EGA source-image mismatch: {name}")
            files[name] = {
                "bytes": observed[0],
                "sha256": observed[1],
                "md5": observed[2],
                "url": entries[name]["links"]["content"],
                "match": True,
                "readback_mode": "anonymous_full_download_exact_sha256",
            }
            if destination is not None:
                summary = zip_inventory(destination)
                expected_members = local[name]["inventory"]["member_identities"]
                if summary["member_identities"] != expected_members:
                    raise RuntimeError(f"Public EGA ZIP member drift: {name}")
                summary["match"] = True
                archives[name] = summary
                destination.unlink()
    finally:
        shutil.rmtree(READBACK_ROOT, ignore_errors=True)
    if (
        len(files) != EXPECTED_FINAL_FILES
        or sum(int(row["bytes"]) for row in files.values()) != EXPECTED_FINAL_BYTES
        or len(archives) != len(NEW_FILES)
        or sum(int(row["members"]) for row in archives.values())
        != EXPECTED_ZIP_MEMBERS
    ):
        raise RuntimeError("EGA source-image public readback did not close")

    result = {
        "status": "PASS_PUBLIC_READBACK",
        "errors": [],
        "record": record_id,
        "record_url": record["links"]["self_html"],
        "doi": record["pids"]["doi"]["identifier"],
        "conceptdoi": CONCEPT_DOI,
        "predecessor_record": PREDECESSOR_RECORD,
        "version": VERSION,
        "file_count": len(files),
        "bytes": sum(int(row["bytes"]) for row in files.values()),
        "files": files,
        "latest_record": int(latest["id"]),
        "rdm_default_preview": record["files"].get("default_preview"),
        "rdm_file_order": record["files"].get("order"),
        "effective_order": "alphanumeric_default",
        "github_commit": GITHUB_COMMIT,
        "github_path": GITHUB_PATH,
        "retained_predecessor_files": EXPECTED_PREDECESSOR_FILES,
        "added_source_image_archives": len(NEW_FILES),
        "added_source_images": EXPECTED_SOURCE_IMAGES,
        "added_zip_members": EXPECTED_ZIP_MEMBERS,
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
    base.save_json(
        RECEIPT_ROOT
        / f"{RECEIPT_TAG}_record_{record_id}_public_readback.json",
        result,
    )
    base.save_json(
        RECEIPT_ROOT
        / f"{RECEIPT_TAG}_record_{record_id}_zip_member_readback.json",
        zipped,
    )
    return result


def preflight() -> dict:
    local = verify_local()
    predecessor = load_predecessor_receipt()
    token = base.find_token()
    session = base.make_session()
    fetch_live(session, predecessor)
    assert_no_untracked_draft(session, token)
    return {
        "status": "PASS_PREFLIGHT",
        "predecessor_record": PREDECESSOR_RECORD,
        "concept_doi": CONCEPT_DOI,
        "retained_files": EXPECTED_PREDECESSOR_FILES,
        "added_files": len(local),
        "added_source_images": EXPECTED_SOURCE_IMAGES,
        "added_zip_members": EXPECTED_ZIP_MEMBERS,
        "final_files": EXPECTED_FINAL_FILES,
        "final_bytes": EXPECTED_FINAL_BYTES,
        "default_preview": DEFAULT_PREVIEW,
        "github_commit": GITHUB_COMMIT,
        "duplicate_concept_created": False,
    }


def publish() -> dict:
    local = verify_local()
    predecessor = load_predecessor_receipt()
    token = base.find_token()
    session = base.make_session()
    live = fetch_live(session, predecessor)
    assert_no_untracked_draft(session, token)
    draft_id = create_or_resume_draft(session, token, live)
    published = stage_and_publish(
        session, token, live, draft_id, local, predecessor
    )
    return public_readback(session, int(published["id"]), local, predecessor)


def readback_only() -> dict:
    local = verify_local()
    predecessor = load_predecessor_receipt()
    state = json.loads(DRAFT_STATE.read_text(encoding="utf-8"))
    if not state.get("published"):
        raise RuntimeError("Tracked EGA source-image successor is not published")
    return public_readback(
        base.make_session(), int(state["record_id"]), local, predecessor
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--preflight", action="store_true")
    parser.add_argument("--readback-only", action="store_true")
    args = parser.parse_args()
    if args.preflight:
        result = preflight()
    elif args.readback_only:
        result = readback_only()
    else:
        result = publish()
    print(json.dumps(result, ensure_ascii=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
