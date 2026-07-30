#!/usr/bin/env python3
"""Publish the compact EGA reference-v2 same-concept successor."""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import io
import json
import re
import shutil
import time
import zipfile
from pathlib import Path, PurePosixPath
from urllib.parse import quote

import publish_current_reader_bundles_zenodo_20260730 as base


API = base.API
PUBLICATION_DATE = "2026-07-30"
PREDECESSOR_RECORD = 21_708_453
PREDECESSOR_DOI = "10.5281/zenodo.21708453"
CONCEPT_DOI = "10.5281/zenodo.20414353"
EXPECTED_PREDECESSOR_FILES = 32
EXPECTED_PREDECESSOR_BYTES = 515_811_940
EXPECTED_RETAINED_FILES = 12
EXPECTED_LOCAL_FILES = 18
EXPECTED_LOCAL_BYTES = 25_069_083
EXPECTED_FINAL_FILES = 30
EXPECTED_FINAL_BYTES = 506_842_049
EXPECTED_ZIP_ARCHIVES = 9
DEFAULT_PREVIEW = (
    "00a_EGA0_English_Complete_Through_Section13_Reference_v2_20260730.pdf"
)
TITLE = (
    "Elements de geometrie algebrique (EGA): French Originals, "
    "English Working Readers, and Source Archives"
)
VERSION = "2026-07-30 compact EGA 0-I-II-III-IV reference-v2 reader release"
GITHUB_COMMIT = "f68b8c571f65b05ae33bb9c5fc986727da2abb59"

REPO_ROOT = Path(__file__).resolve().parent.parent
RELEASE_ROOT = (
    REPO_ROOT / "sources/ega/releases/ega-current-reference-v2-20260730-r2"
)
RELEASE_MANIFEST = RELEASE_ROOT / "92 EGA - Current File SHA256SUMS.csv"
RELEASE_VALIDATION = RELEASE_ROOT / "RELEASE_VALIDATION.json"
RECEIPT_ROOT = REPO_ROOT / "manifests/published-zenodo"
TEMP_ROOT = Path(base.os.environ["LOCALAPPDATA"]) / "Temp" / (
    "ega_compact_reference_v2_zenodo_20260730"
)
READBACK_ROOT = TEMP_ROOT / "public_readback"
DRAFT_STATE = RECEIPT_ROOT / (
    "20260730_ega_compact_reference_v2_zenodo_draft_state.json"
)
PREDECESSOR_RECEIPT = RECEIPT_ROOT / (
    "20260730_ega1_complete_source_aligned_record_21708453_"
    "public_readback.json"
)
ZIP_BASELINE_RECEIPT = RECEIPT_ROOT / (
    "20260730_ega1_complete_source_aligned_record_21708453_"
    "zip_member_readback.json"
)

RETAINED_NAMES = {
    "10 EGA I - French Original (NUMDAM PMIHES 4, 1960).pdf",
    "11 EGA II - French Original (NUMDAM PMIHES 8, 1961).pdf",
    "12 EGA III Part 1 - French Original (NUMDAM PMIHES 11, 1961).pdf",
    "13 EGA III Part 2 - French Original (NUMDAM PMIHES 17, 1963).pdf",
    "14 EGA IV Part 1 - French Original (NUMDAM PMIHES 20, 1964).pdf",
    "15 EGA IV Part 2 - French Original (NUMDAM PMIHES 24, 1965).pdf",
    "16 EGA IV Part 3 - French Original (NUMDAM PMIHES 28, 1966).pdf",
    "17 EGA IV Part 4 - French Original (NUMDAM PMIHES 32, 1967).pdf",
    "80 EGA - EGA 0 IV Translation TeX Supplement.zip",
    "81 EGA - Full TeX Source, French Originals, and Build Artifacts.zip",
    "82 EGA - EGA IV Main Text Translation TeX Supplement.zip",
    "83 EGA IV - Standalone Sections 1-21 TeX and PDF.zip",
}

DESCRIPTION_HTML = "\n".join(
    f"<p>{paragraph}</p>"
    for paragraph in (
        (
            "<strong>Start here:</strong> the first file is one compact ZIP "
            "containing the five current cumulative English reader PDFs and "
            "their complete buildable TeX closures. The same five readers "
            "and their master TeX files are directly accessible immediately "
            "afterward."
        ),
        (
            "This same-concept successor presents current reference-v2 "
            "readers for complete EGA 0 through Section 13, complete EGA I, "
            "complete EGA II, and the complete published EGA III text through "
            "Section 7.9.14. EGA IV remains an explicitly partial working "
            "reader through Sections 1-10."
        ),
        (
            "The direct master TeX files are followed by four coherent "
            "source/QA ZIP archives, concise status and identity controls, "
            "the NUMDAM French originals, and four retained historical source "
            "archives. Stale loose readers and superseded per-reader packages "
            "remain available in immutable predecessor versions rather than "
            "cluttering this current landing surface."
        ),
        (
            "These are scholarly working and custody materials, not critical "
            "editions, peer-review or mathematical certifications, rights "
            "determinations, whole-EGA completion claims, or tagged-PDF "
            "accessibility remediation. No blanket license or transfer of "
            "underlying rights is asserted."
        ),
    )
)
NOTES_HTML = (
    "<p>The first ZIP is the one-click current reader and buildable-TeX "
    "bundle. The default preview is the complete EGA 0 reference-v2 reader. "
    "EGA I and II are complete reference-v2 working readers; EGA III covers "
    "the complete published text through Section 7.9.14; EGA IV is partial "
    "through Sections 1-10. Earlier versions preserve superseded direct "
    "readers and detailed historical presentation states.</p>"
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
            data = archive.read(info.filename)
            members[info.filename] = {
                "bytes": len(data),
                "sha256": hashlib.sha256(data).hexdigest().upper(),
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


def compact_member_map(value: object) -> dict[str, tuple[int, str]]:
    if isinstance(value, dict):
        return {
            name: (int(row["bytes"]), str(row["sha256"]).upper())
            for name, row in value.items()
        }
    if isinstance(value, list):
        return {
            str(row["relative_path"]): (
                int(row["bytes"]),
                str(row["sha256"]).upper(),
            )
            for row in value
        }
    raise RuntimeError("Unsupported ZIP-member receipt schema")


def release_order() -> list[str]:
    rows = list(
        csv.DictReader(
            RELEASE_MANIFEST.open("r", encoding="utf-8-sig", newline="")
        )
    )
    names = [row["relative_path"] for row in rows]
    names.append(RELEASE_MANIFEST.name)
    return names


def retained_order() -> list[str]:
    return [
        "10 EGA I - French Original (NUMDAM PMIHES 4, 1960).pdf",
        "11 EGA II - French Original (NUMDAM PMIHES 8, 1961).pdf",
        "12 EGA III Part 1 - French Original (NUMDAM PMIHES 11, 1961).pdf",
        "13 EGA III Part 2 - French Original (NUMDAM PMIHES 17, 1963).pdf",
        "14 EGA IV Part 1 - French Original (NUMDAM PMIHES 20, 1964).pdf",
        "15 EGA IV Part 2 - French Original (NUMDAM PMIHES 24, 1965).pdf",
        "16 EGA IV Part 3 - French Original (NUMDAM PMIHES 28, 1966).pdf",
        "17 EGA IV Part 4 - French Original (NUMDAM PMIHES 32, 1967).pdf",
        "80 EGA - EGA 0 IV Translation TeX Supplement.zip",
        "81 EGA - Full TeX Source, French Originals, and Build Artifacts.zip",
        "82 EGA - EGA IV Main Text Translation TeX Supplement.zip",
        "83 EGA IV - Standalone Sections 1-21 TeX and PDF.zip",
    ]


def ordered_names(names: set[str]) -> list[str]:
    order = release_order() + retained_order()
    if len(order) != len(names) or set(order) != names:
        raise RuntimeError("EGA compact file order is not an exact permutation")
    return order


def load_receipts() -> tuple[dict, dict]:
    predecessor = json.loads(PREDECESSOR_RECEIPT.read_text(encoding="utf-8"))
    zip_baseline = json.loads(ZIP_BASELINE_RECEIPT.read_text(encoding="utf-8"))
    if (
        predecessor.get("status") != "PASS_PUBLIC_READBACK"
        or int(predecessor.get("record", -1)) != PREDECESSOR_RECORD
        or predecessor.get("conceptdoi") != CONCEPT_DOI
        or int(predecessor.get("file_count", -1)) != EXPECTED_PREDECESSOR_FILES
        or int(predecessor.get("bytes", -1)) != EXPECTED_PREDECESSOR_BYTES
        or zip_baseline.get("status") != "PASS"
    ):
        raise RuntimeError("Controlling EGA predecessor receipts changed")
    return predecessor, zip_baseline


def verify_local() -> dict[str, dict[str, object]]:
    validation = json.loads(RELEASE_VALIDATION.read_text(encoding="utf-8"))
    if (
        validation.get("status") != "PASS"
        or validation.get("errors") != []
        or int(validation.get("upload_files", -1)) != EXPECTED_LOCAL_FILES
        or int(validation.get("upload_bytes", -1)) != EXPECTED_LOCAL_BYTES
        or validation.get("privacy_hits") != []
    ):
        raise RuntimeError("Compact EGA release validation changed")
    rows = list(
        csv.DictReader(
            RELEASE_MANIFEST.open("r", encoding="utf-8-sig", newline="")
        )
    )
    if len(rows) != EXPECTED_LOCAL_FILES - 1:
        raise RuntimeError("Compact EGA release manifest row count changed")
    local: dict[str, dict[str, object]] = {}
    for row in rows:
        name = row["relative_path"]
        path = RELEASE_ROOT / name
        observed = (path.stat().st_size, sha256_path(path))
        expected = (int(row["bytes"]), row["sha256"].upper())
        if observed != expected:
            raise RuntimeError(f"Compact EGA release changed: {name}")
        local[name] = {
            "path": path,
            "bytes": observed[0],
            "sha256": observed[1],
            "md5": md5_path(path),
        }
    manifest_identity = (
        RELEASE_MANIFEST.stat().st_size,
        sha256_path(RELEASE_MANIFEST),
    )
    if manifest_identity != (
        2_107,
        "3025A578EEDD9A77918142547BC21B4328D3FCA4BBA597432DD41DF72725D505",
    ):
        raise RuntimeError("Compact EGA release manifest identity changed")
    local[RELEASE_MANIFEST.name] = {
        "path": RELEASE_MANIFEST,
        "bytes": manifest_identity[0],
        "sha256": manifest_identity[1],
        "md5": md5_path(RELEASE_MANIFEST),
    }
    if len(local) != EXPECTED_LOCAL_FILES or sum(
        int(row["bytes"]) for row in local.values()
    ) != EXPECTED_LOCAL_BYTES:
        raise RuntimeError("Compact EGA local file boundary changed")
    expected_zips = {
        details["filename"]: details
        for details in validation["source_packages"].values()
    }
    bundle = validation["bundle"]
    expected_zips[bundle["filename"]] = bundle
    for name, expected in expected_zips.items():
        observed = zip_inventory(RELEASE_ROOT / name)
        if (
            observed["bytes"] != int(expected["bytes"])
            or observed["sha256"] != expected["sha256"]
            or observed["members"] != int(expected["members"])
        ):
            raise RuntimeError(f"Compact EGA ZIP changed: {name}")
    json.loads((RELEASE_ROOT / "91 EGA - Public Summary.json").read_text(encoding="utf-8"))
    return local


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
            return
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
    headers = auth_headers(token)
    if DRAFT_STATE.is_file():
        state = json.loads(DRAFT_STATE.read_text(encoding="utf-8"))
        if state.get("published"):
            raise RuntimeError("Tracked EGA successor is already published")
        draft_id = int(state["draft_id"])
        base.check(
            session.get(
                f"{API}/records/{draft_id}/draft",
                headers=headers,
                timeout=(30, 60),
            ),
            {200},
        )
        return draft_id
    predecessor = base.check(
        session.get(
            f"{API}/deposit/depositions/{PREDECESSOR_RECORD}",
            headers={"Authorization": f"Bearer {token}"},
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
            headers={"Authorization": f"Bearer {token}"},
            timeout=(30, 300),
        ),
        {201},
    ).json()
    deposition = base.check(
        session.get(
            created["links"]["latest_draft"],
            headers={"Authorization": f"Bearer {token}"},
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
                timeout=(30, 1800),
            ),
            {200, 201},
        )


def stage_and_publish(session, token: str, live: dict, draft_id: int, local: dict) -> dict:
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
    if set(files) != set(base.modern_entries(live)):
        raise RuntimeError("Tracked EGA draft file set changed")
    for name in sorted(set(files) - RETAINED_NAMES, key=str.casefold):
        base.check(
            session.delete(
                files[name]["links"]["self"],
                headers=legacy_headers,
                timeout=(30, 300),
            ),
            {204},
        )
    deposition = base.check(
        session.get(
            f"{API}/deposit/depositions/{draft_id}",
            headers=legacy_headers,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    files = base.legacy_entries(deposition)
    if set(files) != RETAINED_NAMES:
        raise RuntimeError("EGA retained draft boundary changed")
    bucket = deposition["links"]["bucket"]
    for index, name in enumerate(release_order(), start=1):
        print(f"UPLOAD {index}/{EXPECTED_LOCAL_FILES} {name}", flush=True)
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
    expected_names = RETAINED_NAMES | set(local)
    if set(entries) != expected_names or len(entries) != EXPECTED_FINAL_FILES:
        raise RuntimeError("Staged compact EGA successor file set changed")
    predecessor_entries = base.modern_entries(live)
    for name, entry in entries.items():
        if name in local:
            expected = (local[name]["bytes"], local[name]["md5"])
        else:
            old = predecessor_entries[name]
            expected = (
                int(old["size"]),
                base.normalized_md5(old["checksum"]),
            )
        observed = (
            int(entry["size"]),
            base.normalized_md5(entry["checksum"]),
        )
        if observed != expected:
            raise RuntimeError(f"Staged compact EGA identity changed: {name}")

    metadata = copy.deepcopy(draft["metadata"])
    metadata["title"] = TITLE
    metadata["version"] = VERSION
    metadata["publication_date"] = PUBLICATION_DATE
    metadata["description"] = DESCRIPTION_HTML
    metadata["rights"] = [{"id": "notspecified"}]
    stale_subjects = {
        "complete EGA I",
        "current cumulative reader bundle",
        "source-aligned working reader",
    }
    metadata["subjects"] = [
        row
        for row in metadata.get("subjects", [])
        if row.get("subject") not in stale_subjects
    ]
    existing_subjects = {row.get("subject") for row in metadata["subjects"]}
    for subject in (
        "compact current reader surface",
        "reference-v2 working readers",
        "complete EGA 0",
        "complete EGA I",
        "complete EGA II",
        "complete published EGA III text",
        "partial EGA IV Sections 1-10",
    ):
        if subject not in existing_subjects:
            metadata["subjects"].append({"subject": subject})
    metadata["additional_descriptions"] = [
        row
        for row in metadata.get("additional_descriptions", [])
        if row.get("type", {}).get("id") != "notes"
    ] + [{"description": NOTES_HTML, "type": {"id": "notes", "title": {"en": "Notes"}}}]
    order = ordered_names(set(entries))
    payload = {
        "access": draft["access"],
        "files": {
            "enabled": True,
            "default_preview": DEFAULT_PREVIEW,
            "order": order,
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
        set(base.modern_entries(patched)) != set(entries)
        or patched["files"].get("default_preview") != DEFAULT_PREVIEW
        or patched["metadata"].get("version") != VERSION
        or [row.get("id") for row in patched["metadata"].get("rights", [])]
        != ["notspecified"]
    ):
        raise RuntimeError("Patched compact EGA draft controls changed")
    api_order = patched["files"].get("order") or []
    if api_order and api_order != order:
        raise RuntimeError("Zenodo returned a conflicting compact EGA file order")
    base.save_json(
        RECEIPT_ROOT
        / f"20260730_ega_compact_reference_v2_record_{draft_id}_draft_files.json",
        {
            "status": "PASS_STAGED",
            "errors": [],
            "predecessor_record": PREDECESSOR_RECORD,
            "draft_id": draft_id,
            "concept_doi": CONCEPT_DOI,
            "files": len(entries),
            "retained_files": len(RETAINED_NAMES),
            "replacement_files": len(local),
            "default_preview": DEFAULT_PREVIEW,
            "license": "notspecified",
            "duplicate_concept_created": False,
            "second_draft_created": False,
        },
    )
    published = base.check(
        session.post(
            patched["links"]["publish"],
            headers=headers,
            timeout=(30, 600),
        ),
        {200, 202},
    ).json()
    if (
        int(published["id"]) != draft_id
        or published["parent"]["pids"]["doi"]["identifier"] != CONCEPT_DOI
    ):
        raise RuntimeError("Published compact EGA response escaped the concept")
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
        / f"20260730_ega_compact_reference_v2_record_{draft_id}_publish_response.json",
        {
            "status": "PUBLISH_ACCEPTED",
            "errors": [],
            "record_id": draft_id,
            "doi": published["pids"]["doi"]["identifier"],
            "concept_doi": CONCEPT_DOI,
        },
    )
    return published


def stream_download(session, url: str, destination: Path) -> tuple[int, str, str]:
    destination.parent.mkdir(parents=True, exist_ok=True)
    sha = hashlib.sha256()
    md5 = hashlib.md5(usedforsecurity=False)
    size = 0
    with base.check(session.get(url, stream=True, timeout=(30, 1800)), {200}) as response:
        with destination.open("wb") as handle:
            for block in response.iter_content(4 * 1024 * 1024):
                if not block:
                    continue
                handle.write(block)
                sha.update(block)
                md5.update(block)
                size += len(block)
    return size, sha.hexdigest().upper(), md5.hexdigest().lower()


def public_readback(session, live: dict, record_id: int, local: dict, predecessor: dict, zip_baseline: dict) -> dict:
    record = None
    for _ in range(90):
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
        raise RuntimeError("Published compact EGA successor did not become public")
    entries = base.modern_entries(record)
    expected_names = RETAINED_NAMES | set(local)
    if (
        set(entries) != expected_names
        or record["parent"]["pids"]["doi"]["identifier"] != CONCEPT_DOI
        or record["files"].get("default_preview") != DEFAULT_PREVIEW
        or record["metadata"].get("version") != VERSION
        or [row.get("id") for row in record["metadata"].get("rights", [])]
        != ["notspecified"]
    ):
        raise RuntimeError("Public compact EGA successor boundary changed")
    expected_order = ordered_names(set(entries))
    api_order = record["files"].get("order") or []
    if api_order and api_order != expected_order:
        raise RuntimeError("Public compact EGA file order changed")
    latest = base.check(
        session.get(
            f"{API}/records/{PREDECESSOR_RECORD}/versions/latest?expand=true",
            headers=public_headers(),
            timeout=(30, 180),
        ),
        {200},
    ).json()
    if int(latest["id"]) != record_id:
        raise RuntimeError("Published compact EGA successor is not concept head")

    predecessor_files = predecessor["files"]
    shutil.rmtree(READBACK_ROOT, ignore_errors=True)
    READBACK_ROOT.mkdir(parents=True)
    files: dict[str, dict[str, object]] = {}
    archives: dict[str, dict[str, object]] = {}
    try:
        for index, name in enumerate(expected_order, start=1):
            print(f"PUBLIC READBACK {index}/{len(expected_order)} {name}", flush=True)
            destination = READBACK_ROOT / f"{index:02d}-{Path(name).name}"
            observed = stream_download(session, entries[name]["links"]["content"], destination)
            if name in local:
                expected = (
                    int(local[name]["bytes"]),
                    str(local[name]["sha256"]).upper(),
                    str(local[name]["md5"]).lower(),
                )
                mode = "anonymous_full_download_exact_local_sha256"
            else:
                prior = predecessor_files[name]
                expected = (
                    int(prior["bytes"]),
                    prior["sha256"].upper(),
                    prior["md5"].lower(),
                )
                mode = "anonymous_full_download_exact_predecessor_sha256"
            if observed != expected:
                raise RuntimeError(f"Public compact EGA SHA-256 mismatch: {name}")
            files[name] = {
                "bytes": observed[0],
                "sha256": observed[1],
                "md5": observed[2],
                "url": entries[name]["links"]["content"],
                "match": True,
                "readback_mode": mode,
            }
            if name.lower().endswith(".zip"):
                summary = zip_inventory(destination)
                if name in local:
                    expected_members = compact_member_map(
                        zip_inventory(local[name]["path"])["member_identities"]
                    )
                else:
                    prior_zip = zip_baseline["archives"].get(name)
                    if prior_zip is None:
                        raise RuntimeError(f"Missing retained ZIP receipt: {name}")
                    expected_members = compact_member_map(
                        prior_zip.get("member_identities", prior_zip.get("members"))
                    )
                observed_members = compact_member_map(summary["member_identities"])
                if observed_members != expected_members:
                    raise RuntimeError(f"Public ZIP member drift: {name}")
                archives[name] = summary
            destination.unlink()
    finally:
        shutil.rmtree(READBACK_ROOT, ignore_errors=True)
    if (
        len(files) != EXPECTED_FINAL_FILES
        or sum(int(row["bytes"]) for row in files.values()) != EXPECTED_FINAL_BYTES
        or len(archives) != EXPECTED_ZIP_ARCHIVES
    ):
        raise RuntimeError("Compact EGA public readback did not close")
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
        "rdm_file_order": api_order,
        "requested_file_order": expected_order,
        "github_commit": GITHUB_COMMIT,
        "retained_predecessor_files": len(RETAINED_NAMES),
        "replacement_files": len(local),
        "license": "notspecified",
        "zip_archive_count": len(archives),
        "duplicate_concept_created": False,
        "second_draft_created": False,
    }
    zipped = {
        "status": "PASS",
        "errors": [],
        "record": record_id,
        "doi": record["pids"]["doi"]["identifier"],
        "zip_archive_count": len(archives),
        "archives": archives,
    }
    base.save_json(
        RECEIPT_ROOT
        / f"20260730_ega_compact_reference_v2_record_{record_id}_public_readback.json",
        result,
    )
    base.save_json(
        RECEIPT_ROOT
        / f"20260730_ega_compact_reference_v2_record_{record_id}_zip_member_readback.json",
        zipped,
    )
    return result


def preflight() -> dict:
    local = verify_local()
    predecessor, zip_baseline = load_receipts()
    token = base.find_token()
    session = base.make_session()
    live = fetch_live(session, predecessor)
    assert_no_untracked_draft(session, token)
    if (
        not RETAINED_NAMES.issubset(predecessor["files"])
        or any(name not in zip_baseline["archives"] for name in RETAINED_NAMES if name.endswith(".zip"))
    ):
        raise RuntimeError("Compact EGA retained predecessor boundary changed")
    return {
        "status": "PASS_PREFLIGHT",
        "predecessor_record": PREDECESSOR_RECORD,
        "concept_doi": CONCEPT_DOI,
        "retained_files": len(RETAINED_NAMES),
        "replacement_files": len(local),
        "final_files": EXPECTED_FINAL_FILES,
        "final_bytes": EXPECTED_FINAL_BYTES,
        "reader_bundle_members": 125,
        "all_new_zip_member_reads": 331,
        "final_zip_archives": EXPECTED_ZIP_ARCHIVES,
        "github_commit": GITHUB_COMMIT,
        "default_preview": DEFAULT_PREVIEW,
        "license": "notspecified",
    }


def publish() -> dict:
    local = verify_local()
    predecessor, zip_baseline = load_receipts()
    token = base.find_token()
    session = base.make_session()
    live = fetch_live(session, predecessor)
    assert_no_untracked_draft(session, token)
    draft_id = create_or_resume_draft(session, token, live)
    published = stage_and_publish(session, token, live, draft_id, local)
    return public_readback(
        session,
        live,
        int(published["id"]),
        local,
        predecessor,
        zip_baseline,
    )


def readback_only() -> dict:
    local = verify_local()
    predecessor, zip_baseline = load_receipts()
    state = json.loads(DRAFT_STATE.read_text(encoding="utf-8"))
    if not state.get("published"):
        raise RuntimeError("Tracked compact EGA successor is not published")
    session = base.make_session()
    live = base.check(
        session.get(
            f"{API}/records/{PREDECESSOR_RECORD}?expand=true",
            headers=public_headers(),
            timeout=(30, 180),
        ),
        {200},
    ).json()
    return public_readback(
        session,
        live,
        int(state["record_id"]),
        local,
        predecessor,
        zip_baseline,
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
