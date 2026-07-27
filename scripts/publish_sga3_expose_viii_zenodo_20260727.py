#!/usr/bin/env python3
"""Patch, publish, and fully read back the SGA3 Expose VIII Zenodo successor."""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import json
import os
import re
import shutil
import time
import zipfile
from pathlib import Path, PurePosixPath

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


API = "https://zenodo.org/api"
CONCEPT_DOI = "10.5281/zenodo.20410947"
PREDECESSOR_RECORD = 21523096
PREDECESSOR_DOI = "10.5281/zenodo.21523096"
SUCCESSOR_RECORD = 21623401
SUCCESSOR_DOI = "10.5281/zenodo.21623401"
VERSION = "2026-07-27 SGA3 Expose VIII Loop2 reference-v2 r1"
DEFAULT_PREVIEW = (
    "00a_SGA1_English_CompleteVolume_Working_"
    "NoExhaustiveCertification_20260722.pdf"
)

REPO_ROOT = Path(__file__).resolve().parent.parent
RECEIPT_ROOT = REPO_ROOT / "manifests" / "published-zenodo"
PREDECESSOR_RECEIPT = (
    RECEIPT_ROOT
    / "20260724_sga6_ultradetail_source_audit_crops_idx362_378_"
    "record_21523096_public_readback.json"
)
LOCAL_TEMP = Path(os.environ["LOCALAPPDATA"]) / "Temp"
STAGING_ROOT = Path(
    os.environ.get(
        "SGA3_VIII_ZENODO_STAGING_ROOT",
        LOCAL_TEMP / "sga3_viii_zenodo_21623401" / "upload",
    )
)
READBACK_ROOT = Path(
    os.environ.get(
        "SGA3_VIII_ZENODO_READBACK_ROOT",
        LOCAL_TEMP / "sga3_viii_zenodo_21623401_public_readback",
    )
)
TOKEN_LOG = Path(
    os.environ.get(
        "ZENODO_TOKEN_LOG",
        Path.home() / ".codex" / ".sandbox" / "sandbox.log",
    )
)

OLD_CONTROL_NAMES = {
    "09_README_CURRENT_RELEASE.md",
    "09a_RELEASE_FILE_MANIFEST.csv",
    "09b_RELEASE_VALIDATION.json",
}

LOCAL_EXPECTED = {
    "00c5_SGA3_English_Expose_VIII_Loop2_ReferenceV2_R1_20260724.pdf": (
        697_649,
        "255A62C74E5A9900AC92DFCD5379A730C12B86DF7727336AF2E04282BF14D230",
    ),
    "09_README_CURRENT_RELEASE.md": (
        3_438,
        "A99B4F84BC77032BCDD1E0ACBA7652FB657E210A28F3A28675D9F8978B44320B",
    ),
    "09a_RELEASE_FILE_MANIFEST.csv": (
        20_183,
        "D98E88D1210C5BE663C6E8F0CFEB180DBDB74EA97368FE1904E171F61354A7C3",
    ),
    "09b_RELEASE_VALIDATION.json": (
        2_634,
        "E454EC1D79B89A0BAB05A6D06506EF50B02E4B129C2F26A8AFC65FC892F8E921",
    ),
    "10c5_SGA3_English_Expose_VIII_Loop2_ReferenceV2_R1_Source_QA_20260724.zip": (
        7_632_871,
        "2D3DFB6A8A167F0BA23993B1A814199A40D2E3DBD26D120C2AA22D0D5E63442B",
    ),
}

EXPECTED_OUTER_FILES = 58
EXPECTED_OUTER_BYTES = 310_428_261
EXPECTED_RETAINED_FILES = 53
EXPECTED_ZIP_FILES = 32
EXPECTED_ZIP_FILE_MEMBERS = 3_387
EXPECTED_ZIP_DIRECTORY_ENTRIES = 7
EXPECTED_ZIP_ALL_ENTRIES = 3_394
LEGACY_RELEASE_ZIP_COUNTER = 3_393
EXPECTED_ZIP_UNCOMPRESSED_BYTES = 357_369_191

DESCRIPTION_PARAGRAPHS = [
    (
        "This same-concept compact successor preserves all reader, editable-source, "
        "grouped-source, evidence, visual-evidence, and predecessor objects from "
        "version 10.5281/zenodo.21523096. Fifty-three predecessor files outside "
        "the three release controls are retained byte-identically; the three "
        "controls are refreshed and two independently audited SGA3 Expose VIII "
        "objects are added."
    ),
    (
        "The new direct reader is the complete bounded English Expose VIII "
        "checkpoint: 31 A4 pages covering Sections 1-7, 58 numbered units, 22 "
        "equation tags, notes 0-42 plus five symbolic notes, four native diagrams, "
        "and the bibliography, with a hard stop before the first nonblank Expose "
        "IX page. It has 270 named destinations, 248 valid internal GoTo actions, "
        "28 embedded fonts, and no raster-image inclusions."
    ),
    (
        "The grouped source/QA ZIP contains 65 exact members totaling 8,833,128 "
        "uncompressed bytes: ten editable TeX files, the reader, all 31 reviewed "
        "page renders, reference-v2 graph data, translation and correction QA, "
        "independent audit receipts, provenance and rights notices, and recursive "
        "checksums. The graph contains 155 targets and 525 candidates partitioned "
        "into 188 edges and 337 positive residuals, with zero pending actions."
    ),
    (
        "This completes Expose VIII only, not SGA3. The current public SGA3 "
        "surface consists of a cumulative working reader through Expose IV plus "
        "standalone complete working readers for Exposes V, VI, and VIII; Expose "
        "VII and Exposes IX-XXVI are absent. It is not a critical edition, "
        "mathematical certification, independent human peer review, rights "
        "determination, or tagged/accessibility-remediated PDF."
    ),
    (
        "The controlling Polo-Gille Expose VIII PDF, SHA-256 "
        "06E43E0571D411CC5579975778FCC03C8ECAA67189248D1A053E61DC653AF510, "
        "is not redistributed. OCR and external English material are locator or "
        "comparison controls, not authority. Rights in the underlying French work "
        "and Polo-Gille re-edition remain with their holders; no blanket license "
        "or rights transfer is asserted. Machine-assisted contributors include "
        "OpenAI Codex / ChatGPT and Anthropic Claude under human direction. This "
        "successor updates only existing SGA concept 10.5281/zenodo.20410947."
    ),
]
DESCRIPTION_HTML = "\n".join(f"<p>{paragraph}</p>" for paragraph in DESCRIPTION_PARAGRAPHS)
NOTES_TEXT = (
    "Reader-first compact surface: direct cumulative or bounded working PDFs and "
    "primary editable TeX remain individually accessible; recursive sources, "
    "machine ledgers, QA, predecessors, and visual evidence remain grouped into "
    "coherent ZIPs. This version has 58 files and 32 ZIP archives, with 3,393 "
    "verified archive entries totaling 357,369,191 uncompressed bytes. It retains "
    "53 predecessor files exactly and adds the complete bounded SGA3 Expose VIII "
    "reader and 65-member source/QA archive. SGA1 remains the default preview and "
    "remains substantially linked but not exhaustively convention-v2 certified. "
    "GitHub package commit: c53b27a9da508cde755a3bbb176ab04dd8fb744a."
)
NOTES_HTML = f"<p>{NOTES_TEXT}</p>"


def sha256_file(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(4 * 1024 * 1024), b""):
            value.update(block)
    return value.hexdigest().upper()


def md5_file(path: Path) -> str:
    value = hashlib.md5(usedforsecurity=False)
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(4 * 1024 * 1024), b""):
            value.update(block)
    return value.hexdigest().lower()


def normalize_checksum(value: str) -> str:
    return value.lower().removeprefix("md5:")


def find_token() -> str:
    direct = os.environ.get("ZENODO_TOKEN")
    if direct:
        return direct
    valid_prefix = os.environ.get("ZENODO_TOKEN_SHA256_PREFIX")
    if not valid_prefix:
        raise RuntimeError(
            "Set ZENODO_TOKEN or ZENODO_TOKEN_SHA256_PREFIX; no credential "
            "or credential fingerprint is embedded in this script"
        )
    data = TOKEN_LOG.read_text(encoding="utf-8", errors="ignore")
    for candidate in set(re.findall(r"[A-Za-z0-9]{60}", data)):
        if hashlib.sha256(candidate.encode("ascii")).hexdigest().startswith(
            valid_prefix
        ):
            return candidate
    raise RuntimeError("Validated Zenodo token not found")


def make_session() -> requests.Session:
    session = requests.Session()
    retry = Retry(
        total=8,
        connect=8,
        read=8,
        status=8,
        backoff_factor=1.5,
        status_forcelist=(429, 500, 502, 503, 504),
        allowed_methods=frozenset({"GET", "HEAD", "PUT"}),
        raise_on_status=False,
    )
    session.mount("https://", HTTPAdapter(max_retries=retry))
    session.headers.update({"User-Agent": "modern-latex-manuscripts-archive/1.0"})
    return session


def check(response: requests.Response, expected: set[int]) -> requests.Response:
    if response.status_code not in expected:
        raise RuntimeError(
            f"Zenodo HTTP {response.status_code} for {response.request.method} "
            f"{response.url}: {response.text[:2000]}"
        )
    return response


def save_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def public_record_summary(record: dict) -> dict:
    return {
        "id": int(record["id"]),
        "doi": record["pids"]["doi"]["identifier"],
        "conceptdoi": record["parent"]["pids"]["doi"]["identifier"],
        "version": record["metadata"].get("version"),
        "title": record["metadata"].get("title"),
        "file_count": len(record["files"]["entries"]),
        "default_preview": record["files"].get("default_preview"),
        "updated": record.get("updated"),
    }


def local_identities() -> dict[str, dict]:
    result: dict[str, dict] = {}
    for name, (expected_bytes, expected_sha) in LOCAL_EXPECTED.items():
        path = STAGING_ROOT / name
        if not path.is_file():
            raise FileNotFoundError(path)
        actual = {
            "bytes": path.stat().st_size,
            "sha256": sha256_file(path),
            "md5": md5_file(path),
        }
        if (actual["bytes"], actual["sha256"]) != (
            expected_bytes,
            expected_sha,
        ):
            raise RuntimeError(f"Local staging identity mismatch: {name}")
        result[name] = actual
    return result


def predecessor_identities() -> dict[str, dict]:
    receipt = json.loads(PREDECESSOR_RECEIPT.read_text(encoding="utf-8-sig"))
    if receipt.get("status") != "PASS":
        raise RuntimeError("Predecessor public receipt is not PASS")
    if int(receipt["record"]["id"]) != PREDECESSOR_RECORD:
        raise RuntimeError("Predecessor receipt record mismatch")
    rows = receipt.get("outer_files", [])
    if len(rows) != 56:
        raise RuntimeError("Predecessor receipt does not contain 56 files")
    result = {
        row["filename"]: {
            "bytes": int(row["bytes"]),
            "sha256": row["sha256"].upper(),
            "md5": row.get("md5", "").lower(),
        }
        for row in rows
    }
    if len(result) != 56:
        raise RuntimeError("Duplicate predecessor filenames")
    return result


def expected_identities() -> tuple[dict[str, dict], dict[str, dict]]:
    predecessor = predecessor_identities()
    local = local_identities()
    retained = {
        name: identity
        for name, identity in predecessor.items()
        if name not in OLD_CONTROL_NAMES
    }
    if len(retained) != EXPECTED_RETAINED_FILES:
        raise RuntimeError("Retained predecessor boundary mismatch")
    final = {**retained, **local}
    if len(final) != EXPECTED_OUTER_FILES:
        raise RuntimeError("Expected final filename collision or count mismatch")
    if sum(row["bytes"] for row in final.values()) != EXPECTED_OUTER_BYTES:
        raise RuntimeError("Expected final byte boundary mismatch")
    return final, retained


def assert_record_lineage(record: dict, expected_id: int, expected_doi: str) -> None:
    if int(record["id"]) != expected_id:
        raise RuntimeError(f"Unexpected record id: {record['id']}")
    if record["pids"]["doi"]["identifier"] != expected_doi:
        raise RuntimeError("Unexpected record DOI")
    if record["parent"]["pids"]["doi"]["identifier"] != CONCEPT_DOI:
        raise RuntimeError("Record escaped the existing SGA concept")


def note_type_id(item: dict) -> str:
    value = item.get("type", "")
    if isinstance(value, dict):
        return str(value.get("id", ""))
    return str(value)


def inspect_preflight(session: requests.Session, token: str) -> dict:
    expected, retained = expected_identities()
    auth = {"Authorization": f"Bearer {token}"}
    vendor = {**auth, "Accept": "application/vnd.inveniordm.v1+json"}
    public_vendor = {"Accept": "application/vnd.inveniordm.v1+json"}

    latest = check(
        session.get(
            f"{API}/records/{PREDECESSOR_RECORD}/versions/latest",
            headers=public_vendor,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    assert_record_lineage(latest, PREDECESSOR_RECORD, PREDECESSOR_DOI)

    predecessor = check(
        session.get(
            f"{API}/records/{PREDECESSOR_RECORD}",
            headers=public_vendor,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    assert_record_lineage(predecessor, PREDECESSOR_RECORD, PREDECESSOR_DOI)
    predecessor_entries = predecessor["files"]["entries"]

    draft = check(
        session.get(
            f"{API}/records/{SUCCESSOR_RECORD}/draft",
            headers=vendor,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    if int(draft["id"]) != SUCCESSOR_RECORD:
        raise RuntimeError("Unexpected draft id")
    if draft["parent"]["pids"]["doi"]["identifier"] != CONCEPT_DOI:
        raise RuntimeError("Draft escaped the existing concept")
    draft_entries = draft["files"]["entries"]
    if set(draft_entries) != set(expected):
        missing = sorted(set(expected) - set(draft_entries))
        extra = sorted(set(draft_entries) - set(expected))
        raise RuntimeError(f"Draft exact-set mismatch: missing={missing}, extra={extra}")

    retained_errors: list[str] = []
    for name, identity in retained.items():
        before = predecessor_entries.get(name)
        after = draft_entries.get(name)
        if before is None or after is None:
            retained_errors.append(f"missing:{name}")
            continue
        if (
            int(before["size"]) != identity["bytes"]
            or int(after["size"]) != identity["bytes"]
            or before["checksum"] != after["checksum"]
            or normalize_checksum(before["checksum"]) != identity["md5"]
        ):
            retained_errors.append(f"identity:{name}")
    if retained_errors:
        raise RuntimeError(f"Retained draft mismatch: {retained_errors}")

    local_errors: list[str] = []
    for name in LOCAL_EXPECTED:
        entry = draft_entries[name]
        identity = expected[name]
        if (
            int(entry["size"]) != identity["bytes"]
            or normalize_checksum(entry["checksum"]) != identity["md5"]
        ):
            local_errors.append(name)
    if local_errors:
        raise RuntimeError(f"Uploaded draft file mismatch: {local_errors}")

    if draft["files"].get("default_preview") != DEFAULT_PREVIEW:
        raise RuntimeError("Draft default preview mismatch")

    additional = draft["metadata"].get("additional_descriptions", [])
    notes_rows = [
        {"index": index, "type": note_type_id(item)}
        for index, item in enumerate(additional)
    ]
    if not additional:
        raise RuntimeError("Draft has no additional-description field to preserve")

    result = {
        "status": "PASS_PREFLIGHT",
        "errors": [],
        "latest_public": public_record_summary(latest),
        "draft": {
            "id": int(draft["id"]),
            "conceptdoi": draft["parent"]["pids"]["doi"]["identifier"],
            "version_before_patch": draft["metadata"].get("version"),
            "file_count": len(draft_entries),
            "bytes": sum(int(entry["size"]) for entry in draft_entries.values()),
            "default_preview": draft["files"].get("default_preview"),
            "explicit_order_count": len(draft["files"].get("order", [])),
            "additional_descriptions": notes_rows,
        },
        "retained_predecessor_files": len(retained),
        "retained_identity_errors": retained_errors,
        "new_or_refreshed_files": {
            name: {
                "bytes": expected[name]["bytes"],
                "sha256": expected[name]["sha256"],
            }
            for name in LOCAL_EXPECTED
        },
        "planned_metadata": {
            "version": VERSION,
            "description_sha256": hashlib.sha256(
                DESCRIPTION_HTML.encode("utf-8")
            ).hexdigest().upper(),
            "notes_sha256": hashlib.sha256(
                NOTES_HTML.encode("utf-8")
            ).hexdigest().upper(),
        },
        "duplicate_concept_created": False,
        "new_version_created_by_this_script": False,
    }
    save_json(
        RECEIPT_ROOT
        / "20260727_sga3_expose_viii_record_21623401_preflight.json",
        result,
    )
    return result


def patch_notes(metadata: dict) -> None:
    additional = metadata.get("additional_descriptions", [])
    if not additional:
        raise RuntimeError("Cannot patch absent notes field")
    notes_indexes = [
        index
        for index, item in enumerate(additional)
        if note_type_id(item) in {"notes", "technical-info", "other"}
    ]
    target = notes_indexes[0] if notes_indexes else 0
    additional[target]["description"] = NOTES_HTML
    metadata["additional_descriptions"] = additional


def assert_metadata(metadata: dict) -> None:
    if metadata.get("version") != VERSION:
        raise RuntimeError("Version metadata mismatch")
    if metadata.get("description") != DESCRIPTION_HTML:
        raise RuntimeError("Description metadata mismatch")
    additional = metadata.get("additional_descriptions", [])
    if not any(item.get("description") == NOTES_HTML for item in additional):
        raise RuntimeError("Notes metadata mismatch")


def patch_and_publish(session: requests.Session, token: str) -> dict:
    preflight = inspect_preflight(session, token)
    auth = {"Authorization": f"Bearer {token}"}
    vendor = {**auth, "Accept": "application/vnd.inveniordm.v1+json"}
    json_headers = {**vendor, "Content-Type": "application/json"}

    draft = check(
        session.get(
            f"{API}/records/{SUCCESSOR_RECORD}/draft",
            headers=vendor,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    metadata = copy.deepcopy(draft["metadata"])
    metadata["version"] = VERSION
    metadata["description"] = DESCRIPTION_HTML
    patch_notes(metadata)

    files_payload = {
        "enabled": True,
        "default_preview": DEFAULT_PREVIEW,
        "order": list(draft["files"].get("order", [])),
    }
    payload = {
        "access": draft["access"],
        "files": files_payload,
        "metadata": metadata,
        "custom_fields": draft.get("custom_fields", {}),
    }
    if draft.get("pids"):
        payload["pids"] = draft["pids"]

    patched = check(
        session.put(
            f"{API}/records/{SUCCESSOR_RECORD}/draft",
            headers=json_headers,
            json=payload,
            timeout=(30, 300),
        ),
        {200},
    ).json()
    assert_metadata(patched["metadata"])
    if patched["files"].get("default_preview") != DEFAULT_PREVIEW:
        raise RuntimeError("Patched draft lost the default preview")
    if len(patched["files"]["entries"]) != EXPECTED_OUTER_FILES:
        raise RuntimeError("Patched draft lost files")

    patched_readback = check(
        session.get(
            f"{API}/records/{SUCCESSOR_RECORD}/draft",
            headers=vendor,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    assert_metadata(patched_readback["metadata"])
    if patched_readback["files"].get("default_preview") != DEFAULT_PREVIEW:
        raise RuntimeError("Draft readback lost the default preview")
    if set(patched_readback["files"]["entries"]) != set(
        expected_identities()[0]
    ):
        raise RuntimeError("Draft readback exact-set mismatch")

    patch_receipt = {
        "status": "PASS_PATCHED_DRAFT",
        "errors": [],
        "draft_id": SUCCESSOR_RECORD,
        "conceptdoi": CONCEPT_DOI,
        "version": VERSION,
        "description_exact": True,
        "notes_exact": True,
        "file_count": EXPECTED_OUTER_FILES,
        "default_preview": DEFAULT_PREVIEW,
        "preflight": preflight,
    }
    save_json(
        RECEIPT_ROOT
        / "20260727_sga3_expose_viii_record_21623401_draft_patch.json",
        patch_receipt,
    )

    published = check(
        session.post(
            patched_readback["links"]["publish"],
            headers=vendor,
            timeout=(30, 600),
        ),
        {200, 202},
    ).json()
    if int(published["id"]) != SUCCESSOR_RECORD:
        raise RuntimeError("Publish response record mismatch")
    if published["parent"]["pids"]["doi"]["identifier"] != CONCEPT_DOI:
        raise RuntimeError("Publish response concept mismatch")
    return {
        "status": "PUBLISH_ACCEPTED",
        "record_id": int(published["id"]),
        "doi": published["pids"]["doi"]["identifier"],
        "conceptdoi": published["parent"]["pids"]["doi"]["identifier"],
    }


def wait_for_public(session: requests.Session) -> dict:
    public_vendor = {"Accept": "application/vnd.inveniordm.v1+json"}
    last_status = None
    for _ in range(60):
        response = session.get(
            f"{API}/records/{SUCCESSOR_RECORD}",
            headers=public_vendor,
            timeout=(30, 180),
        )
        last_status = response.status_code
        if response.status_code == 200:
            record = response.json()
            if (
                int(record["id"]) == SUCCESSOR_RECORD
                and len(record["files"]["entries"]) == EXPECTED_OUTER_FILES
            ):
                return record
        time.sleep(5)
    raise RuntimeError(f"Published record did not stabilize; last HTTP {last_status}")


def download_public_file(
    session: requests.Session,
    url: str,
    destination: Path,
    expected_bytes: int,
    expected_sha: str,
) -> tuple[int, str]:
    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.is_file() and destination.stat().st_size == expected_bytes:
        existing_sha = sha256_file(destination)
        if existing_sha == expected_sha:
            return expected_bytes, existing_sha
        destination.unlink()
    elif destination.exists():
        destination.unlink()

    temporary = destination.with_suffix(destination.suffix + ".partial")
    if temporary.exists():
        temporary.unlink()
    value = hashlib.sha256()
    total = 0
    with check(
        session.get(url, stream=True, timeout=(30, 1800)),
        {200},
    ) as response:
        with temporary.open("wb") as handle:
            for block in response.iter_content(4 * 1024 * 1024):
                if block:
                    handle.write(block)
                    value.update(block)
                    total += len(block)
    actual_sha = value.hexdigest().upper()
    if (total, actual_sha) != (expected_bytes, expected_sha):
        temporary.unlink(missing_ok=True)
        raise RuntimeError(
            f"Anonymous readback mismatch for {destination.name}: "
            f"{total}/{actual_sha}"
        )
    temporary.replace(destination)
    return total, actual_sha


def safe_zip_name(name: str) -> bool:
    normalized = name.replace("\\", "/")
    path = PurePosixPath(normalized)
    return (
        not normalized.startswith(("/", "\\"))
        and not re.match(r"^[A-Za-z]:", normalized)
        and ".." not in path.parts
    )


def replay_zip(path: Path) -> tuple[dict, list[dict]]:
    errors: list[str] = []
    members: list[dict] = []
    seen: set[str] = set()
    aggregate_rows: list[str] = []
    with zipfile.ZipFile(path) as archive:
        all_entries = archive.infolist()
        directory_entries = [row for row in all_entries if row.is_dir()]
        for info in sorted(
            (row for row in all_entries if not row.is_dir()),
            key=lambda row: row.filename,
        ):
            if not safe_zip_name(info.filename):
                errors.append(f"unsafe:{info.filename}")
            if info.filename in seen:
                errors.append(f"duplicate:{info.filename}")
            seen.add(info.filename)
            value = hashlib.sha256()
            size = 0
            with archive.open(info) as source:
                for block in iter(lambda: source.read(4 * 1024 * 1024), b""):
                    value.update(block)
                    size += len(block)
            member_sha = value.hexdigest().upper()
            if size != info.file_size:
                errors.append(f"size:{info.filename}")
            row = {
                "relative_path": info.filename,
                "bytes": size,
                "sha256": member_sha,
            }
            members.append(row)
            aggregate_rows.append(
                f"{info.filename}\t{size}\t{member_sha}\n"
            )
    summary = {
        "filename": path.name,
        "bytes": path.stat().st_size,
        "sha256": sha256_file(path),
        "member_count": len(members),
        "directory_entry_count": len(directory_entries),
        "all_entry_count": len(members) + len(directory_entries),
        "uncompressed_bytes": sum(row["bytes"] for row in members),
        "canonical_member_identity_sha256": hashlib.sha256(
            "".join(aggregate_rows).encode("utf-8")
        ).hexdigest().upper(),
        "errors": errors,
    }
    return summary, members


def validate_new_zip_internal_manifest(
    zip_members: list[dict],
    downloaded_zip: Path,
) -> dict:
    manifest_rows: list[dict[str, str]] | None = None
    root_prefix = ""
    with zipfile.ZipFile(downloaded_zip) as archive:
        candidates = [
            info
            for info in archive.infolist()
            if not info.is_dir() and info.filename.endswith("/SHA256SUMS.csv")
        ]
        if len(candidates) != 1:
            raise RuntimeError("New ZIP internal manifest is not unique")
        root_prefix = str(PurePosixPath(candidates[0].filename).parent)
        manifest_rows = list(
            csv.DictReader(
                archive.read(candidates[0]).decode("utf-8-sig").splitlines()
            )
        )
    by_path = {}
    prefix = root_prefix.rstrip("/") + "/"
    for row in zip_members:
        relative = row["relative_path"]
        if relative.startswith(prefix):
            relative = relative[len(prefix):]
        by_path[relative] = row
    errors: list[str] = []
    for row in manifest_rows:
        relative_path = row.get("relative_path") or row.get("path")
        if not relative_path:
            errors.append("manifest_row_without_path")
            continue
        member = by_path.get(relative_path)
        if member is None:
            errors.append(f"missing:{relative_path}")
            continue
        if (
            int(row["bytes"]) != member["bytes"]
            or row["sha256"].upper() != member["sha256"]
        ):
            errors.append(f"identity:{relative_path}")
    if len(manifest_rows) != 64:
        errors.append(f"manifest_rows:{len(manifest_rows)}")
    if len(zip_members) != 65:
        errors.append(f"zip_members:{len(zip_members)}")
    return {
        "internal_manifest_rows": len(manifest_rows),
        "zip_members": len(zip_members),
        "errors": errors,
    }


def anonymous_readback(
    session: requests.Session,
    token: str,
    publish_result: dict | None,
    keep_downloads: bool,
) -> dict:
    expected, retained = expected_identities()
    record = wait_for_public(session)
    assert_record_lineage(record, SUCCESSOR_RECORD, SUCCESSOR_DOI)
    assert_metadata(record["metadata"])
    if record["files"].get("default_preview") != DEFAULT_PREVIEW:
        raise RuntimeError("Published default preview mismatch")
    entries = record["files"]["entries"]
    if set(entries) != set(expected):
        raise RuntimeError("Published exact-set mismatch")
    if sum(int(entry["size"]) for entry in entries.values()) != EXPECTED_OUTER_BYTES:
        raise RuntimeError("Published byte boundary mismatch")

    latest = check(
        session.get(
            f"{API}/records/{PREDECESSOR_RECORD}/versions/latest",
            headers={"Accept": "application/vnd.inveniordm.v1+json"},
            timeout=(30, 180),
        ),
        {200},
    ).json()
    assert_record_lineage(latest, SUCCESSOR_RECORD, SUCCESSOR_DOI)

    auth = {"Authorization": f"Bearer {token}"}
    vendor = {**auth, "Accept": "application/vnd.inveniordm.v1+json"}
    active_draft = session.get(
        f"{API}/records/{SUCCESSOR_RECORD}/draft",
        headers=vendor,
        timeout=(30, 180),
    )
    if active_draft.status_code != 404:
        raise RuntimeError(
            f"Published record still has an active draft: {active_draft.status_code}"
        )

    READBACK_ROOT.mkdir(parents=True, exist_ok=True)
    outer_rows: list[dict] = []
    for index, name in enumerate(sorted(expected), start=1):
        print(f"READBACK {index}/{len(expected)} {name}", flush=True)
        entry = entries[name]
        size, sha = download_public_file(
            session,
            entry["links"]["content"],
            READBACK_ROOT / name,
            expected[name]["bytes"],
            expected[name]["sha256"],
        )
        outer_rows.append(
            {
                "filename": name,
                "bytes": size,
                "sha256": sha,
                "md5": normalize_checksum(entry["checksum"]),
                "classification": (
                    "retained_predecessor" if name in retained
                    else "new_or_refreshed"
                ),
                "url": entry["links"]["content"],
            }
        )

    zip_summaries: list[dict] = []
    zip_members: list[dict] = []
    new_zip_members: list[dict] | None = None
    for index, path in enumerate(
        sorted(READBACK_ROOT.glob("*.zip"), key=lambda row: row.name),
        start=1,
    ):
        print(f"ZIP REPLAY {index} {path.name}", flush=True)
        summary, members = replay_zip(path)
        if summary["errors"]:
            raise RuntimeError(f"ZIP replay errors for {path.name}: {summary['errors']}")
        zip_summaries.append(summary)
        zip_members.extend(
            {"archive": path.name, **member}
            for member in members
        )
        if path.name.startswith("10c5_SGA3_English_Expose_VIII"):
            new_zip_members = members

    if len(zip_summaries) != EXPECTED_ZIP_FILES:
        raise RuntimeError("ZIP file count mismatch")
    if len(zip_members) != EXPECTED_ZIP_FILE_MEMBERS:
        raise RuntimeError(
            f"ZIP file-member count mismatch: {len(zip_members)}"
        )
    directory_entries = sum(
        row["directory_entry_count"] for row in zip_summaries
    )
    all_entries = sum(row["all_entry_count"] for row in zip_summaries)
    if directory_entries != EXPECTED_ZIP_DIRECTORY_ENTRIES:
        raise RuntimeError(
            f"ZIP directory-entry count mismatch: {directory_entries}"
        )
    if all_entries != EXPECTED_ZIP_ALL_ENTRIES:
        raise RuntimeError(f"ZIP all-entry count mismatch: {all_entries}")
    if (
        sum(row["uncompressed_bytes"] for row in zip_summaries)
        != EXPECTED_ZIP_UNCOMPRESSED_BYTES
    ):
        raise RuntimeError("ZIP uncompressed-byte boundary mismatch")
    if new_zip_members is None:
        raise RuntimeError("New SGA3 Expose VIII ZIP not found")
    new_zip_validation = validate_new_zip_internal_manifest(
        new_zip_members,
        READBACK_ROOT
        / "10c5_SGA3_English_Expose_VIII_Loop2_ReferenceV2_R1_"
        "Source_QA_20260724.zip",
    )
    if new_zip_validation["errors"]:
        raise RuntimeError(
            f"New ZIP internal-manifest replay failed: "
            f"{new_zip_validation['errors']}"
        )

    zip_member_receipt = {
        "status": "PASS",
        "errors": [],
        "record_id": SUCCESSOR_RECORD,
        "doi": SUCCESSOR_DOI,
        "zip_archive_count": len(zip_summaries),
        "zip_file_member_count": len(zip_members),
        "zip_directory_entry_count": directory_entries,
        "zip_all_entry_count": all_entries,
        "legacy_release_zip_counter": LEGACY_RELEASE_ZIP_COUNTER,
        "legacy_counter_note": (
            "The release-control lineage counter combines the predecessor's "
            "3,328 stored entries with the new archive's 65 non-directory "
            "files. Literal replay has 3,387 file members plus seven directory "
            "entries, or 3,394 total ZIP records."
        ),
        "zip_uncompressed_bytes": sum(
            row["uncompressed_bytes"] for row in zip_summaries
        ),
        "archives": zip_summaries,
        "members": zip_members,
        "new_sga3_expose_viii_zip": new_zip_validation,
    }
    save_json(
        RECEIPT_ROOT
        / "20260727_sga3_expose_viii_record_21623401_zip_member_readback.json",
        zip_member_receipt,
    )

    retained_errors = [
        row["filename"]
        for row in outer_rows
        if row["filename"] in retained
        and (
            row["bytes"] != retained[row["filename"]]["bytes"]
            or row["sha256"] != retained[row["filename"]]["sha256"]
        )
    ]
    if retained_errors:
        raise RuntimeError(f"Retained SHA readback mismatch: {retained_errors}")

    receipt = {
        "status": "PASS",
        "errors": [],
        "record": public_record_summary(record),
        "latest": public_record_summary(latest),
        "concept_doi": CONCEPT_DOI,
        "predecessor_record": PREDECESSOR_RECORD,
        "predecessor_doi": PREDECESSOR_DOI,
        "github": {
            "commit": "c53b27a9da508cde755a3bbb176ab04dd8fb744a",
            "package": (
                "sources/sga/"
                "sga3-english-expose-viii-loop2-reference-v2-r1-20260724"
            ),
            "anonymous_outer_readback": "5/5",
            "anonymous_zip_member_readback": "65/65",
        },
        "outer_files": outer_rows,
        "outer_file_count": len(outer_rows),
        "outer_bytes": sum(row["bytes"] for row in outer_rows),
        "retained_predecessor_files": len(retained),
        "retained_predecessor_errors": retained_errors,
        "new_or_refreshed_files": len(LOCAL_EXPECTED),
        "default_preview_ui_readback": DEFAULT_PREVIEW,
        "metadata": {
            "version": VERSION,
            "description_exact": True,
            "notes_exact": True,
            "sga3_complete": False,
            "scope": "complete bounded SGA3 Expose VIII",
            "excluded": "Expose VII and Exposes IX-XXVI",
        },
        "zip_archive_count": len(zip_summaries),
        "zip_file_member_count": len(zip_members),
        "zip_directory_entry_count": directory_entries,
        "zip_all_entry_count": all_entries,
        "legacy_release_zip_counter": LEGACY_RELEASE_ZIP_COUNTER,
        "zip_uncompressed_bytes": sum(
            row["uncompressed_bytes"] for row in zip_summaries
        ),
        "draft_remaining": False,
        "duplicate_concept_created": False,
        "second_version_created_by_script": False,
        "publish_result": publish_result,
    }
    save_json(
        RECEIPT_ROOT
        / "20260727_sga3_expose_viii_record_21623401_public_readback.json",
        receipt,
    )

    if not keep_downloads:
        resolved = READBACK_ROOT.resolve()
        temp_parent = (Path(os.environ["LOCALAPPDATA"]) / "Temp").resolve()
        if resolved.parent != temp_parent or resolved.name != (
            "sga3_viii_zenodo_21623401_public_readback"
        ):
            raise RuntimeError(f"Refusing unsafe readback cleanup: {resolved}")
        shutil.rmtree(resolved)

    return receipt


def main() -> None:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--preflight", action="store_true")
    mode.add_argument("--publish", action="store_true")
    mode.add_argument("--readback-only", action="store_true")
    parser.add_argument("--keep-downloads", action="store_true")
    args = parser.parse_args()

    token = find_token()
    session = make_session()
    if args.preflight:
        result = inspect_preflight(session, token)
    elif args.publish:
        publish_result = patch_and_publish(session, token)
        result = anonymous_readback(
            session,
            token,
            publish_result=publish_result,
            keep_downloads=args.keep_downloads,
        )
    else:
        result = anonymous_readback(
            session,
            token,
            publish_result=None,
            keep_downloads=args.keep_downloads,
        )
    print(json.dumps(result, ensure_ascii=False, indent=2), flush=True)


if __name__ == "__main__":
    main()
