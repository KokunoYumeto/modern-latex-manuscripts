#!/usr/bin/env python3
"""Publish and publicly replay the complete linked EGA 0-IV reader."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
import shutil
import time
import zipfile
from pathlib import Path, PurePosixPath
from urllib.parse import quote

import publish_current_reader_bundles_zenodo_20260730 as base


API = base.API
PREDECESSOR_RECORD = 21_740_145
PREDECESSOR_DOI = "10.5281/zenodo.21740145"
CONCEPT_DOI = "10.5281/zenodo.20414353"
PREDECESSOR_FILES = 40
PREDECESSOR_BYTES = 3_752_670_964
PREDECESSOR_FILE_AGGREGATE = (
    "84DE079EF75742CEB2AE2A807E67B601194560FFBA6B8291A7B85DE9C9D0AE9F"
)
FINAL_FILES = 42
FINAL_BYTES = 3_771_391_044
DEFAULT_PREVIEW = "00_GLOBAL_EGA_0_IV_English_Complete_Linked_Reader_20260801.pdf"
VERSION = "2026-08-01 complete linked EGA 0-IV reader"
PUBLICATION_DATE = "2026-08-01"
GITHUB_PR = 226
GITHUB_SOURCE_COMMIT = "78f76376e367f09f58aa618b418a45fb18cfb826"
GITHUB_MERGE_COMMIT = "28d373916554bd26fa0661f9905eb2277b7eeca7"

REPO_ROOT = Path(__file__).resolve().parent.parent
RELEASE_ROOT = REPO_ROOT / "sources/ega/ega-global-complete-linked-reader-20260801"
BUNDLE_ROOT = REPO_ROOT / (
    "sources/ega/ega-current-readers-and-buildable-tex-bundle-"
    "reference-v2-20260801"
)
RECEIPT_ROOT = REPO_ROOT / "manifests/published-zenodo"
STATE_PATH = RECEIPT_ROOT / "20260801_ega_global_reader_zenodo_state.json"
TEMP_ROOT = Path(base.os.environ["LOCALAPPDATA"]) / "Temp" / (
    "ega_global_reader_zenodo_20260801"
)

BUNDLE_NAME = "00 Current_EGA_English_Readers_and_Buildable_TeX_20260801.zip"
GLOBAL_PDF_NAME = "00_GLOBAL_EGA_0_IV_English_Complete_Linked_Reader_20260801.pdf"
GLOBAL_TEX_NAME = "01_GLOBAL_EGA_0_IV_English_Complete_Linked_Master_20260801.tex"
README_CONTROL = "90 EGA - README and Status.md"
SUMMARY_CONTROL = "91 EGA - Public Summary.json"
SUMS_CONTROL = "92 EGA - Current File SHA256SUMS.csv"

OLD_NAMES = {
    BUNDLE_NAME: (9_618_706, "de6145332fe7a1b11984bdfaf15958eb"),
    README_CONTROL: (1_031, "ce9f845cc0b133e04d21c7efa2e6ca91"),
    SUMMARY_CONTROL: (51_149, "2536d0aa6f3fbca44981830e738e5084"),
    SUMS_CONTROL: (2_107, "4565275eacc6f73ce80b84ce7a94ebcb"),
}

LOCAL_SPECS = {
    BUNDLE_NAME: {
        "path": BUNDLE_ROOT / BUNDLE_NAME,
        "bytes": 19_798_264,
        "sha256": "F4FF53966222741FC5750DF140AA3691D2DA66393347AA8E03BBD9EE3D6E2F21",
        "members": 265,
        "uncompressed_bytes": 32_503_979,
    },
    GLOBAL_PDF_NAME: {
        "path": RELEASE_ROOT / GLOBAL_PDF_NAME,
        "bytes": 8_588_550,
        "sha256": "3B9D399515AA074C22D3DF6C6F0F7349954444D7BCF980B87CCE5CAED671928A",
    },
    GLOBAL_TEX_NAME: {
        "path": RELEASE_ROOT / GLOBAL_TEX_NAME,
        "bytes": 1_688,
        "sha256": "8147C8FDB1B5EBEA69FDB02AA7C192F8267CCA9ABE887AFD3B11B179CE7A7CC1",
    },
    README_CONTROL: {
        "path": RELEASE_ROOT / README_CONTROL,
        "bytes": 560,
        "sha256": "4C07DCFF4FC11289D552644E80C507757634504F19218C2BFD203D0989767925",
    },
    SUMMARY_CONTROL: {
        "path": RELEASE_ROOT / SUMMARY_CONTROL,
        "bytes": 2_068,
        "sha256": "DBFE92A7A0EB1E0FF28176C8E74F424D6EC3AADE04FC07F817AA09445347A5A6",
    },
    SUMS_CONTROL: {
        "path": RELEASE_ROOT / SUMS_CONTROL,
        "bytes": 1_943,
        "sha256": "DFBE83CC9AAAADF8A2CDFE69851A9BDDFDEB89EFCE09B9C6F0B222BA10FBA223",
    },
}

DESCRIPTION_HTML = "\n".join(
    (
        "<p><strong>Read EGA:</strong> open <code>00_GLOBAL_EGA_0_IV_English_"
        "Complete_Linked_Reader_20260801.pdf</code> for one continuous EGA 0-IV "
        "reader. It is the default preview.</p>",
        "<p>Download <code>00 Current_EGA_English_Readers_and_Buildable_TeX_"
        "20260801.zip</code> for the global reader, the five standalone readers, "
        "and complete buildable TeX for all six reader surfaces.</p>",
        "<p><strong>Coverage:</strong> EGA 0 through Section 13; EGA I and II "
        "through EOF; the published EGA III text through 7.9.14; and EGA IV "
        "Sections 1-21 through EOF. The 1,356-page global reader has 15,383 "
        "destinations and 17,808 resolved internal links.</p>",
        "<p>These are working English readers, not critical editions or new "
        "rights grants.</p>",
    )
)


def sha256_path(path: Path) -> str:
    return base.sha256_path(path)


def md5_path(path: Path) -> str:
    return base.md5_path(path)


def normalized_md5(value: str) -> str:
    return base.normalized_md5(value)


def public_headers() -> dict[str, str]:
    return {"Accept": "application/vnd.inveniordm.v1+json"}


def auth_headers(token: str) -> dict[str, str]:
    return {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.inveniordm.v1+json",
    }


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
        "bytes": path.stat().st_size,
        "sha256": sha256_path(path),
        "members": len(members),
        "uncompressed_bytes": sum(int(row["bytes"]) for row in members.values()),
        "member_identities": members,
    }


def file_aggregate(entries: dict[str, dict]) -> str:
    text = "".join(
        f"{name}\t{int(row['size'])}\t{normalized_md5(row['checksum'])}\n"
        for name, row in sorted(entries.items(), key=lambda item: item[0].casefold())
    )
    return hashlib.sha256(text.encode("utf-8")).hexdigest().upper()


def verify_local() -> dict[str, dict[str, object]]:
    result: dict[str, dict[str, object]] = {}
    for name, spec in LOCAL_SPECS.items():
        path = Path(spec["path"])
        observed = (path.stat().st_size, sha256_path(path))
        expected = (int(spec["bytes"]), str(spec["sha256"]).upper())
        if observed != expected:
            raise RuntimeError(f"Local EGA global release object changed: {name}")
        row = dict(spec)
        row["md5"] = md5_path(path)
        if name.lower().endswith(".zip"):
            inventory = zip_inventory(path)
            if (
                inventory["members"] != int(spec["members"])
                or inventory["uncompressed_bytes"] != int(spec["uncompressed_bytes"])
            ):
                raise RuntimeError(f"Local EGA global ZIP boundary changed: {name}")
            row["zip_inventory"] = inventory
        result[name] = row
    if sum(int(row["bytes"]) for row in result.values()) != 28_393_073:
        raise RuntimeError("Local EGA global upload byte boundary changed")
    return result


def fetch_record(session, record_id: int) -> dict:
    return base.check(
        session.get(
            f"{API}/records/{record_id}?expand=true",
            headers=public_headers(),
            timeout=(30, 180),
        ),
        {200},
    ).json()


def fetch_predecessor(session) -> dict:
    live = fetch_record(session, PREDECESSOR_RECORD)
    entries = base.modern_entries(live)
    if (
        int(live["id"]) != PREDECESSOR_RECORD
        or live["pids"]["doi"]["identifier"] != PREDECESSOR_DOI
        or live["parent"]["pids"]["doi"]["identifier"] != CONCEPT_DOI
        or len(entries) != PREDECESSOR_FILES
        or sum(int(row["size"]) for row in entries.values()) != PREDECESSOR_BYTES
        or file_aggregate(entries) != PREDECESSOR_FILE_AGGREGATE
    ):
        raise RuntimeError("Live EGA predecessor boundary changed")
    for name, expected in OLD_NAMES.items():
        row = entries.get(name)
        if row is None or (int(row["size"]), normalized_md5(row["checksum"])) != expected:
            raise RuntimeError(f"Live EGA replacement base changed: {name}")
    latest = base.check(
        session.get(
            f"{API}/records/{PREDECESSOR_RECORD}/versions/latest?expand=true",
            headers=public_headers(),
            timeout=(30, 180),
        ),
        {200},
    ).json()
    if int(latest["id"]) != PREDECESSOR_RECORD:
        raise RuntimeError("EGA concept head moved; refusing a parallel successor")
    return live


def active_draft(session, token: str, record_id: int) -> dict | None:
    response = session.get(
        f"{API}/records/{record_id}/draft",
        headers=auth_headers(token),
        timeout=(30, 60),
    )
    if response.status_code == 404:
        return None
    return base.check(response, {200}).json()


def create_or_resume_draft(session, token: str, live: dict) -> int:
    if STATE_PATH.is_file():
        state = json.loads(STATE_PATH.read_text(encoding="utf-8"))
        if state.get("published"):
            return int(state["record_id"])
        draft_id = int(state["draft_id"])
        if active_draft(session, token, draft_id) is None:
            raise RuntimeError("Tracked EGA global successor draft disappeared")
        return draft_id
    if active_draft(session, token, PREDECESSOR_RECORD) is not None:
        raise RuntimeError("Untracked active EGA successor draft exists")
    legacy_headers = {"Authorization": f"Bearer {token}"}
    predecessor = base.check(
        session.get(
            f"{API}/deposit/depositions/{PREDECESSOR_RECORD}",
            headers=legacy_headers,
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
            headers=legacy_headers,
            timeout=(30, 300),
        ),
        {201},
    ).json()
    deposition = base.check(
        session.get(
            created["links"]["latest_draft"],
            headers=legacy_headers,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    if set(base.legacy_entries(deposition)) != set(base.modern_entries(live)):
        raise RuntimeError("EGA global successor did not inherit predecessor exactly")
    draft_id = int(deposition["id"])
    base.save_json(
        STATE_PATH,
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


def final_order(names: set[str]) -> list[str]:
    preferred = [
        BUNDLE_NAME,
        GLOBAL_PDF_NAME,
        "00a_EGA0_English_Complete_Through_Section13_Reference_v2_20260730.pdf",
        "00b_EGA1_English_Complete_Reference_v2_Reader_20260730.pdf",
        "00c_EGA2_English_Complete_Reference_v2_Reader_20260730.pdf",
        "00d_EGAIII_English_Published_Text_Complete_Reference_v2_20260730.pdf",
        "00e_EGAIV_English_Complete_Reference_v2_Reader_20260801.pdf",
        GLOBAL_TEX_NAME,
        "01a_EGA0_English_Master_20260730.tex",
        "01b_EGA1_English_Master_20260730.tex",
        "01c_EGA2_English_Master_20260730.tex",
        "01d_EGAIII_English_Master_20260730.tex",
        "01e_EGAIV_English_Complete_Reference_v2_Master_20260801.tex",
        "02a_EGA0_EGAIII_English_Reference_v2_TeX_PDF_QA_20260730.zip",
        "02b_EGA1_English_Reference_v2_TeX_PDF_QA_20260730.zip",
        "02c_EGA2_English_Reference_v2_TeX_PDF_QA_20260730.zip",
        "02d_EGAIV_English_Complete_Reference_v2_TeX_PDF_QA_20260801.zip",
    ]
    order = [name for name in preferred if name in names]
    order.extend(sorted(names - set(order), key=lambda name: (name.casefold(), name)))
    return order


def stage_and_publish(session, token: str, live: dict, draft_id: int, local: dict[str, dict]) -> dict:
    if STATE_PATH.is_file():
        state = json.loads(STATE_PATH.read_text(encoding="utf-8"))
        if state.get("published"):
            return fetch_record(session, int(state["record_id"]))
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
    predecessor_names = set(base.modern_entries(live))
    if set(files) != predecessor_names:
        raise RuntimeError("Tracked EGA global draft file set changed")
    for name in OLD_NAMES:
        base.check(
            session.delete(files[name]["links"]["self"], headers=legacy_headers, timeout=(30, 300)),
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
    remaining = base.legacy_entries(deposition)
    retained_names = predecessor_names - set(OLD_NAMES)
    if set(remaining) != retained_names or len(remaining) != 36:
        raise RuntimeError("EGA global retained draft boundary changed")
    bucket = deposition["links"]["bucket"]
    for index, (name, row) in enumerate(local.items(), start=1):
        print(f"UPLOAD {index}/{len(local)} {name}", flush=True)
        upload_file(session, token, bucket, name, Path(row["path"]))

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
    expected_names = retained_names | set(local)
    if (
        set(entries) != expected_names
        or len(entries) != FINAL_FILES
        or sum(int(row["size"]) for row in entries.values()) != FINAL_BYTES
    ):
        raise RuntimeError("Staged EGA global successor boundary changed")
    predecessor_entries = base.modern_entries(live)
    for name, row in entries.items():
        if name in local:
            expected = (int(local[name]["bytes"]), str(local[name]["md5"]))
        else:
            old = predecessor_entries[name]
            expected = (int(old["size"]), normalized_md5(old["checksum"]))
        observed = (int(row["size"]), normalized_md5(row["checksum"]))
        if observed != expected:
            raise RuntimeError(f"Staged EGA global identity mismatch: {name}")

    metadata = copy.deepcopy(draft["metadata"])
    metadata["version"] = VERSION
    metadata["publication_date"] = PUBLICATION_DATE
    metadata["description"] = DESCRIPTION_HTML
    metadata["additional_descriptions"] = []
    metadata["rights"] = [{"id": "notspecified"}]
    metadata["subjects"] = [
        {"subject": "algebraic geometry"},
        {"subject": "EGA"},
        {"subject": "English working translations"},
        {"subject": "complete linked EGA 0-IV reader"},
        {"subject": "buildable TeX"},
    ]
    order = final_order(set(entries))
    payload = {
        "access": draft["access"],
        "files": {"enabled": True, "default_preview": DEFAULT_PREVIEW, "order": order},
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
        or patched["metadata"].get("description") != DESCRIPTION_HTML
        or patched["metadata"].get("additional_descriptions", []) != []
    ):
        raise RuntimeError("Patched EGA global successor controls changed")
    published = base.check(
        session.post(patched["links"]["publish"], headers=headers, timeout=(30, 600)),
        {200, 202},
    ).json()
    if published["parent"]["pids"]["doi"]["identifier"] != CONCEPT_DOI:
        raise RuntimeError("Published EGA global successor escaped the concept")
    state = json.loads(STATE_PATH.read_text(encoding="utf-8"))
    state.update(
        {
            "status": "PUBLISHED_TRACKED_SUCCESSOR",
            "published": True,
            "record_id": int(published["id"]),
            "doi": published["pids"]["doi"]["identifier"],
        }
    )
    base.save_json(STATE_PATH, state)
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


def public_readback(session, token: str, predecessor: dict, record_id: int, local: dict[str, dict]) -> dict:
    record = None
    for _ in range(90):
        response = session.get(
            f"{API}/records/{record_id}?expand=true",
            headers=public_headers(),
            timeout=(30, 180),
        )
        if response.status_code == 200 and response.json().get("is_published"):
            candidate = response.json()
            if len(base.modern_entries(candidate)) == FINAL_FILES:
                record = candidate
                break
        time.sleep(2)
    if record is None:
        raise RuntimeError("Published EGA global successor did not become public")
    entries = base.modern_entries(record)
    predecessor_entries = base.modern_entries(predecessor)
    retained_names = set(predecessor_entries) - set(OLD_NAMES)
    expected_names = retained_names | set(local)
    if (
        set(entries) != expected_names
        or record["parent"]["pids"]["doi"]["identifier"] != CONCEPT_DOI
        or record["files"].get("default_preview") != DEFAULT_PREVIEW
        or record["metadata"].get("description") != DESCRIPTION_HTML
        or record["metadata"].get("additional_descriptions", []) != []
    ):
        raise RuntimeError("Public EGA global successor boundary changed")
    latest = base.check(
        session.get(
            f"{API}/records/{record_id}/versions/latest?expand=true",
            headers=public_headers(),
            timeout=(30, 180),
        ),
        {200},
    ).json()
    if int(latest["id"]) != record_id:
        raise RuntimeError("Published EGA global successor is not concept head")

    retained: dict[str, dict[str, object]] = {}
    for name in sorted(retained_names, key=str.casefold):
        old = predecessor_entries[name]
        new = entries[name]
        observed = (int(new["size"]), normalized_md5(new["checksum"]))
        expected = (int(old["size"]), normalized_md5(old["checksum"]))
        if observed != expected:
            raise RuntimeError(f"Retained EGA identity drift: {name}")
        retained[name] = {"bytes": observed[0], "md5": observed[1], "match_predecessor": True}

    replacements: dict[str, dict[str, object]] = {}
    archives: dict[str, dict[str, object]] = {}
    shutil.rmtree(TEMP_ROOT, ignore_errors=True)
    TEMP_ROOT.mkdir(parents=True)
    try:
        for index, (name, spec) in enumerate(local.items(), start=1):
            print(f"PUBLIC READBACK {index}/{len(local)} {name}", flush=True)
            destination = TEMP_ROOT / f"{index:02d}-{Path(name).name}"
            observed = stream_download(session, entries[name]["links"]["content"], destination)
            expected = (int(spec["bytes"]), str(spec["sha256"]).upper(), str(spec["md5"]).lower())
            if observed != expected:
                raise RuntimeError(f"Public EGA global SHA-256 mismatch: {name}")
            replacements[name] = {
                "bytes": observed[0],
                "sha256": observed[1],
                "md5": observed[2],
                "public_url": entries[name]["links"]["content"],
                "match": True,
            }
            if name.lower().endswith(".zip"):
                downloaded = zip_inventory(destination)
                local_zip = spec["zip_inventory"]
                if downloaded["member_identities"] != local_zip["member_identities"]:
                    raise RuntimeError(f"Public EGA global ZIP member drift: {name}")
                archives[name] = {
                    "members": downloaded["members"],
                    "uncompressed_bytes": downloaded["uncompressed_bytes"],
                    "member_identities": downloaded["member_identities"],
                }
            destination.unlink()
    finally:
        shutil.rmtree(TEMP_ROOT, ignore_errors=True)

    if active_draft(session, token, PREDECESSOR_RECORD) is not None:
        raise RuntimeError("Predecessor unexpectedly retains an active draft")
    if active_draft(session, token, record_id) is not None:
        raise RuntimeError("Published successor unexpectedly retains an active draft")
    if (
        len(retained) != 36
        or len(replacements) != 6
        or sum(int(row["size"]) for row in entries.values()) != FINAL_BYTES
        or sum(int(row["members"]) for row in archives.values()) != 265
    ):
        raise RuntimeError("EGA global public readback did not close")

    result = {
        "status": "PASS_PUBLIC_READBACK",
        "errors": [],
        "record": record_id,
        "record_url": record["links"]["self_html"],
        "doi": record["pids"]["doi"]["identifier"],
        "concept_doi": CONCEPT_DOI,
        "predecessor_record": PREDECESSOR_RECORD,
        "version": VERSION,
        "file_count": len(entries),
        "bytes": sum(int(row["size"]) for row in entries.values()),
        "retained_files": retained,
        "replacement_files": replacements,
        "zip_archives": archives,
        "zip_member_count": sum(int(row["members"]) for row in archives.values()),
        "default_preview": record["files"].get("default_preview"),
        "file_order": record["files"].get("order", []),
        "description_sha256": hashlib.sha256(DESCRIPTION_HTML.encode("utf-8")).hexdigest().upper(),
        "additional_descriptions": len(record["metadata"].get("additional_descriptions", [])),
        "github_pr": GITHUB_PR,
        "github_source_commit": GITHUB_SOURCE_COMMIT,
        "github_merge_commit": GITHUB_MERGE_COMMIT,
        "duplicate_concept_created": False,
        "second_draft_created": False,
    }
    receipt = RECEIPT_ROOT / (
        f"20260801_ega_global_complete_linked_reader_record_{record_id}_public_readback.json"
    )
    base.save_json(receipt, result)
    return result


def preflight() -> dict:
    local = verify_local()
    token = base.find_token()
    session = base.make_session()
    live = fetch_predecessor(session)
    if active_draft(session, token, PREDECESSOR_RECORD) is not None:
        raise RuntimeError("Untracked active EGA successor draft exists")
    return {
        "status": "PASS_PREFLIGHT",
        "predecessor_record": PREDECESSOR_RECORD,
        "concept_doi": CONCEPT_DOI,
        "predecessor_files": len(base.modern_entries(live)),
        "retained_files": 36,
        "replacement_files": len(local),
        "final_files": FINAL_FILES,
        "final_bytes": FINAL_BYTES,
        "zip_member_readback": 265,
        "default_preview": DEFAULT_PREVIEW,
    }


def publish() -> dict:
    local = verify_local()
    token = base.find_token()
    session = base.make_session()
    live = fetch_predecessor(session)
    draft_id = create_or_resume_draft(session, token, live)
    published = stage_and_publish(session, token, live, draft_id, local)
    return public_readback(session, token, live, int(published["id"]), local)


def readback_only() -> dict:
    if not STATE_PATH.is_file():
        raise RuntimeError("No tracked EGA global successor state exists")
    state = json.loads(STATE_PATH.read_text(encoding="utf-8"))
    if not state.get("published"):
        raise RuntimeError("Tracked EGA global successor is not published")
    local = verify_local()
    token = base.find_token()
    session = base.make_session()
    predecessor = fetch_record(session, PREDECESSOR_RECORD)
    return public_readback(session, token, predecessor, int(state["record_id"]), local)


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
