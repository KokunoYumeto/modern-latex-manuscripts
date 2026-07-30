#!/usr/bin/env python3
"""Publish the Noether Slavic repair-survivor same-concept successor."""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import os
import shutil
import time
import zipfile
from pathlib import Path, PurePosixPath
from urllib.parse import quote

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


API = "https://zenodo.org/api"
REPOSITORY = "KokunoYumeto/modern-latex-manuscripts"
GITHUB_COMMIT = "b32701da350e9f406a5bd5c1fb69d9c32fab0789"
PREDECESSOR_RECORD = 21_499_660
PREDECESSOR_DOI = "10.5281/zenodo.21499660"
CONCEPT_DOI = "10.5281/zenodo.20412587"
EXPECTED_PREDECESSOR_FILES = 20
EXPECTED_PREDECESSOR_BYTES = 580_769_810
DEFAULT_PREVIEW = "01j_Noether_R823_Full_Cumulative_English_20260722.pdf"
OLD_ARCHIVE = "61_Noether_Current_Source_Audit_and_Repair_Evidence_20260722.zip"
NEW_ARCHIVE = (
    "61_Noether_Current_Source_Audit_and_Slavic_Repair_Evidence_20260730.zip"
)
NEW_VERSION = "2026-07-30 Slavic source-repair survivor custody update"
DESCRIPTION_MARKER = "2026-07-30 Slavic source-repair survivor custody update"
DESCRIPTION_APPEND = (
    "<p><strong>2026-07-30 Slavic source-repair survivor custody "
    "update:</strong> this same-concept successor preserves 19 unrelated "
    "reader-first files byte-identically and replaces grouped source-audit "
    "archive 61 with a 132-member successor. The replacement retains the 20 "
    "prior English/German source-audit objects and adds exact post-repair "
    "TeX/PDF bodies plus immediate preimages for Noether Paper 4 "
    "Introduction/Sections 2-5 and Paper 37 in Latin Interslavic, Cyrillic "
    "Interslavic, Russian, and Ukrainian. Source-scan pixels remain "
    "rights-blocked metadata-only; redundant target-PDF renders, private "
    "paths, raw logs, scripts, and model/workflow notes are excluded. This "
    "is bounded repair custody, not native/community certification, "
    "whole-paper certification, proof checking, or a critical edition.</p>"
)

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
PACKAGE_ROOT = (
    REPO_ROOT / "sources" / "noether" / "slavic-source-repair-survivors-20260730"
)
WORK_ROOT = Path(
    os.environ.get(
        "NOETHER_SLAVIC_ZENODO_WORK_ROOT",
        Path(os.environ["LOCALAPPDATA"])
        / "Temp"
        / "noether_slavic_repair_zenodo_20260730",
    )
)
NEW_ARCHIVE_PATH = WORK_ROOT / NEW_ARCHIVE
RECEIPT_ROOT = REPO_ROOT / "manifests" / "published-zenodo"
DRAFT_STATE = (
    RECEIPT_ROOT / "20260730_noether_slavic_repair_zenodo_draft_state.json"
)
EXPECTED_PACKAGE_FILES = 110
EXPECTED_PACKAGE_BYTES = 3_573_722
EXPECTED_PACKAGE_TREE_SHA256 = (
    "409304EB707663BF870831B810C4F5F741862DFDF7F4BF620B93EE483D51E10A"
)
EXPECTED_PACKAGE_MANIFEST_SHA256 = (
    "8CC5E841C3A872ACF198DC97661914C8D880499E704D5DFD454A2C9F262CC0E6"
)
EXPECTED_OLD_ARCHIVE_BYTES = 118_247_131
EXPECTED_OLD_ARCHIVE_SHA256 = (
    "116AF09E5DDF8F6BEBC3A2DF59FBD4981FF6DB87E19F5B0CA209CFD2CFCA36BF"
)
EXPECTED_OLD_ARCHIVE_MEMBERS = 22
EXPECTED_OLD_CONTENT_MEMBERS = 20
EXPECTED_NEW_ARCHIVE_MEMBERS = 132
EXPECTED_NEW_ARCHIVE_MANIFEST_ROWS = 131


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest().upper()


def sha256_path(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(4 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def md5_path(path: Path) -> str:
    digest = hashlib.md5(usedforsecurity=False)
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(4 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().lower()


def save_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, ensure_ascii=True, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def safe_zip_name(name: str) -> bool:
    normalized = name.replace("\\", "/")
    path = PurePosixPath(normalized)
    return not (
        normalized.startswith("/")
        or path.is_absolute()
        or ".." in path.parts
        or (path.parts and ":" in path.parts[0])
    )


def zip_info(name: str) -> zipfile.ZipInfo:
    info = zipfile.ZipInfo(name, date_time=(2026, 7, 30, 0, 0, 0))
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = 0o100644 << 16
    info.create_system = 3
    return info


def write_stream(
    archive: zipfile.ZipFile,
    name: str,
    source,
) -> None:
    with archive.open(zip_info(name), "w", force_zip64=True) as output:
        shutil.copyfileobj(source, output, length=4 * 1024 * 1024)


def package_identity() -> tuple[list[dict[str, object]], str]:
    if not PACKAGE_ROOT.is_dir():
        raise RuntimeError(f"Missing GitHub package root: {PACKAGE_ROOT}")
    rows: list[dict[str, object]] = []
    aggregate = hashlib.sha256()
    total = 0
    for path in sorted(
        (item for item in PACKAGE_ROOT.rglob("*") if item.is_file()),
        key=lambda item: item.relative_to(PACKAGE_ROOT).as_posix(),
    ):
        relative = path.relative_to(PACKAGE_ROOT).as_posix()
        size = path.stat().st_size
        digest = sha256_path(path)
        rows.append(
            {"relative_path": relative, "bytes": size, "sha256": digest}
        )
        aggregate.update(f"{relative}\t{size}\t{digest}\n".encode("utf-8"))
        total += size
    observed = (
        len(rows),
        total,
        aggregate.hexdigest().upper(),
        sha256_path(PACKAGE_ROOT / "controls" / "SHA256SUMS.csv"),
    )
    expected = (
        EXPECTED_PACKAGE_FILES,
        EXPECTED_PACKAGE_BYTES,
        EXPECTED_PACKAGE_TREE_SHA256,
        EXPECTED_PACKAGE_MANIFEST_SHA256,
    )
    if observed != expected:
        raise RuntimeError(
            f"GitHub package identity changed: {observed!r} != {expected!r}"
        )
    return rows, observed[2]


def validate_old_archive(
    path: Path,
) -> list[dict[str, object]]:
    observed = (path.stat().st_size, sha256_path(path))
    expected = (EXPECTED_OLD_ARCHIVE_BYTES, EXPECTED_OLD_ARCHIVE_SHA256)
    if observed != expected:
        raise RuntimeError(f"Old archive identity changed: {observed!r}")
    with zipfile.ZipFile(path) as archive:
        infos = archive.infolist()
        if len(infos) != EXPECTED_OLD_ARCHIVE_MEMBERS:
            raise RuntimeError("Old archive member count changed")
        if archive.testzip() is not None:
            raise RuntimeError("Old archive CRC check failed")
        if any(not safe_zip_name(info.filename) for info in infos):
            raise RuntimeError("Old archive has an unsafe member path")
        manifest = list(
            csv.DictReader(
                io.StringIO(archive.read("MANIFEST.csv").decode("utf-8-sig"))
            )
        )
        by_name = {row["relative_path"]: row for row in manifest}
        content = sorted(
            info.filename
            for info in infos
            if info.filename not in {"README.md", "MANIFEST.csv"}
        )
        if (
            len(content) != EXPECTED_OLD_CONTENT_MEMBERS
            or set(content) != set(by_name) - {"README.md"}
        ):
            raise RuntimeError("Old archive content/manifest boundary changed")
        rows: list[dict[str, object]] = []
        for name in content:
            digest = hashlib.sha256()
            total = 0
            with archive.open(name) as source:
                for block in iter(
                    lambda: source.read(4 * 1024 * 1024),
                    b"",
                ):
                    digest.update(block)
                    total += len(block)
            row = by_name[name]
            if (
                total,
                digest.hexdigest().upper(),
            ) != (
                int(row["bytes"]),
                row["sha256"].upper(),
            ):
                raise RuntimeError(f"Old archive member mismatch: {name}")
            rows.append(
                {
                    "relative_path": name,
                    "bytes": total,
                    "sha256": digest.hexdigest().upper(),
                }
            )
    return rows


def build_replacement_archive(
    old_archive: Path,
) -> dict[str, object]:
    package_rows, package_tree = package_identity()
    old_rows = validate_old_archive(old_archive)
    readme = (
        "# Noether current source-audit and Slavic repair evidence\n\n"
        "This grouped archive retains the 20 English/German source-audit "
        "objects from Noether version 10.5281/zenodo.21499660 and adds the "
        "privacy-clean Slavic repair-survivor package mirrored at GitHub "
        f"commit {GITHUB_COMMIT}.\n\n"
        "The additive package contains exact post-repair TeX/PDF bodies and "
        "immediate preimages for Paper 4 Introduction/Sections 2-5 and "
        "Paper 37 in Latin Interslavic, Cyrillic Interslavic, Russian, and "
        "Ukrainian. Source-scan pixels remain rights-blocked metadata-only. "
        "Redundant target-PDF renders, private paths, raw logs/scripts, and "
        "model/workflow notes are excluded.\n\n"
        "This is bounded source-repair custody, not native/community "
        "certification, whole-paper source certification, proof checking, "
        "or a critical edition.\n"
    ).encode("utf-8")
    manifest_rows: list[dict[str, object]] = [
        {
            "relative_path": "README.md",
            "bytes": len(readme),
            "sha256": sha256_bytes(readme),
        }
    ]
    manifest_rows.extend(old_rows)
    manifest_rows.extend(
        {
            "relative_path": (
                "slavic-source-repair-survivors-20260730/"
                + str(row["relative_path"])
            ),
            "bytes": row["bytes"],
            "sha256": row["sha256"],
        }
        for row in package_rows
    )
    manifest_rows.sort(key=lambda row: str(row["relative_path"]))
    output = io.StringIO(newline="")
    writer = csv.DictWriter(
        output,
        fieldnames=("relative_path", "bytes", "sha256"),
        lineterminator="\n",
    )
    writer.writeheader()
    writer.writerows(manifest_rows)
    manifest = output.getvalue().encode("utf-8")

    WORK_ROOT.mkdir(parents=True, exist_ok=True)
    partial = NEW_ARCHIVE_PATH.with_suffix(".zip.partial")
    if partial.exists():
        partial.unlink()
    with zipfile.ZipFile(
        partial,
        "w",
        compression=zipfile.ZIP_DEFLATED,
        compresslevel=9,
        allowZip64=True,
    ) as target:
        target.writestr(zip_info("README.md"), readme)
        target.writestr(zip_info("MANIFEST.csv"), manifest)
        with zipfile.ZipFile(old_archive) as source_archive:
            for row in old_rows:
                name = str(row["relative_path"])
                with source_archive.open(name) as source:
                    write_stream(target, name, source)
        for row in package_rows:
            source_path = PACKAGE_ROOT / str(row["relative_path"])
            target_name = (
                "slavic-source-repair-survivors-20260730/"
                + str(row["relative_path"])
            )
            with source_path.open("rb") as source:
                write_stream(target, target_name, source)
    partial.replace(NEW_ARCHIVE_PATH)
    validation = validate_replacement_archive(NEW_ARCHIVE_PATH)
    if validation["manifest_rows"] != EXPECTED_NEW_ARCHIVE_MANIFEST_ROWS:
        raise RuntimeError("Replacement archive manifest row count changed")
    validation.update(
        {
            "package_tree_sha256": package_tree,
            "github_commit": GITHUB_COMMIT,
        }
    )
    save_json(WORK_ROOT / "replacement_archive_validation.json", validation)
    return validation


def validate_replacement_archive(path: Path) -> dict[str, object]:
    with zipfile.ZipFile(path) as archive:
        infos = archive.infolist()
        if len(infos) != EXPECTED_NEW_ARCHIVE_MEMBERS:
            raise RuntimeError(
                f"Replacement archive has {len(infos)} members"
            )
        if archive.testzip() is not None:
            raise RuntimeError("Replacement archive CRC check failed")
        if any(not safe_zip_name(info.filename) for info in infos):
            raise RuntimeError("Replacement archive has an unsafe member path")
        rows = list(
            csv.DictReader(
                io.StringIO(archive.read("MANIFEST.csv").decode("utf-8-sig"))
            )
        )
        expected_names = {
            info.filename for info in infos if info.filename != "MANIFEST.csv"
        }
        if set(row["relative_path"] for row in rows) != expected_names:
            raise RuntimeError("Replacement archive manifest/set mismatch")
        errors = []
        for row in rows:
            name = row["relative_path"]
            digest = hashlib.sha256()
            total = 0
            with archive.open(name) as source:
                for block in iter(
                    lambda: source.read(4 * 1024 * 1024),
                    b"",
                ):
                    digest.update(block)
                    total += len(block)
            if (
                total,
                digest.hexdigest().upper(),
            ) != (
                int(row["bytes"]),
                row["sha256"].upper(),
            ):
                errors.append(name)
        if errors:
            raise RuntimeError(
                f"Replacement archive member mismatches: {errors[:10]}"
            )
        return {
            "status": "PASS",
            "errors": [],
            "filename": path.name,
            "bytes": path.stat().st_size,
            "sha256": sha256_path(path),
            "members": len(infos),
            "manifest_rows": len(rows),
            "uncompressed_bytes": sum(info.file_size for info in infos),
            "manifest_bytes": len(archive.read("MANIFEST.csv")),
            "manifest_sha256": sha256_bytes(archive.read("MANIFEST.csv")),
            "old_content_members": EXPECTED_OLD_CONTENT_MEMBERS,
            "slavic_package_members": EXPECTED_PACKAGE_FILES,
        }


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
    session.headers.update(
        {
            "User-Agent": "modern-latex-manuscripts-archive/1.0",
            "Connection": "close",
        }
    )
    return session


def check(
    response: requests.Response,
    expected: set[int],
) -> requests.Response:
    if response.status_code not in expected:
        raise RuntimeError(
            f"Zenodo HTTP {response.status_code} for "
            f"{response.request.method} {response.url}: "
            f"{response.text[:2000]}"
        )
    return response


def find_token() -> str:
    direct = os.environ.get("ZENODO_TOKEN")
    if direct:
        return direct
    raise RuntimeError("Set ZENODO_TOKEN before publishing")


def normalize_md5(value: str) -> str:
    return value.lower().removeprefix("md5:")


def legacy_file_map(deposition: dict) -> dict[str, dict]:
    return {item["filename"]: item for item in deposition["files"]}


def modern_entries(record: dict) -> dict[str, dict]:
    return record["files"]["entries"]


def public_preflight(
    session: requests.Session,
    token: str,
    previous_readback: dict[str, dict],
) -> dict:
    public_headers = {"Accept": "application/vnd.inveniordm.v1+json"}
    live = check(
        session.get(
            f"{API}/records/{PREDECESSOR_RECORD}/versions/latest",
            headers=public_headers,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    entries = modern_entries(live)
    observed = (
        int(live["id"]),
        live["pids"]["doi"]["identifier"],
        live["parent"]["pids"]["doi"]["identifier"],
        len(entries),
        sum(int(entry["size"]) for entry in entries.values()),
        live["files"].get("default_preview"),
    )
    expected = (
        PREDECESSOR_RECORD,
        PREDECESSOR_DOI,
        CONCEPT_DOI,
        EXPECTED_PREDECESSOR_FILES,
        EXPECTED_PREDECESSOR_BYTES,
        DEFAULT_PREVIEW,
    )
    if observed != expected:
        raise RuntimeError(
            f"Noether live-head boundary changed: {observed!r}"
        )
    if set(entries) != set(previous_readback):
        raise RuntimeError("Previous readback and live file sets differ")
    for name, expected_file in previous_readback.items():
        if int(entries[name]["size"]) != int(expected_file["bytes"]):
            raise RuntimeError(f"Live predecessor byte count changed: {name}")

    vendor = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.inveniordm.v1+json",
    }
    active = session.get(
        f"{API}/records/{PREDECESSOR_RECORD}/draft",
        headers=vendor,
        timeout=(30, 60),
    )
    if active.status_code == 200:
        if not DRAFT_STATE.is_file():
            raise RuntimeError("Untracked Noether successor draft exists")
        state = json.loads(DRAFT_STATE.read_text(encoding="utf-8"))
        if int(active.json()["id"]) != int(state["draft_id"]):
            raise RuntimeError("Tracked Noether draft identity changed")
    else:
        check(active, {404})
    return live


def create_or_resume_draft(
    session: requests.Session,
    token: str,
    live: dict,
) -> int:
    auth = {"Authorization": f"Bearer {token}"}
    vendor = {
        **auth,
        "Accept": "application/vnd.inveniordm.v1+json",
    }
    active = session.get(
        f"{API}/records/{PREDECESSOR_RECORD}/draft",
        headers=vendor,
        timeout=(30, 60),
    )
    if active.status_code == 200:
        state = json.loads(DRAFT_STATE.read_text(encoding="utf-8"))
        draft_id = int(active.json()["id"])
        if (
            draft_id != int(state["draft_id"])
            or int(state["predecessor_record"]) != PREDECESSOR_RECORD
        ):
            raise RuntimeError("Existing draft is not the tracked draft")
        return draft_id
    check(active, {404})
    if DRAFT_STATE.is_file():
        state = json.loads(DRAFT_STATE.read_text(encoding="utf-8"))
        if state.get("published"):
            raise RuntimeError("Tracked Noether successor is already published")
        raise RuntimeError("Tracked Noether draft state exists but draft is absent")

    predecessor = check(
        session.get(
            f"{API}/deposit/depositions/{PREDECESSOR_RECORD}",
            headers=auth,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    if (
        predecessor.get("state") != "done"
        or not predecessor.get("submitted")
        or not predecessor.get("links", {}).get("newversion")
    ):
        raise RuntimeError("Noether predecessor is not a versioning base")
    created = check(
        session.post(
            predecessor["links"]["newversion"],
            headers=auth,
            timeout=(30, 300),
        ),
        {201},
    ).json()
    draft = check(
        session.get(
            created["links"]["latest_draft"],
            headers=auth,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    draft_id = int(draft["id"])
    if set(legacy_file_map(draft)) != set(modern_entries(live)):
        raise RuntimeError("New Noether version did not inherit predecessor")
    save_json(
        DRAFT_STATE,
        {
            "status": "OPEN_TRACKED_DRAFT",
            "predecessor_record": PREDECESSOR_RECORD,
            "draft_id": draft_id,
            "conceptdoi": CONCEPT_DOI,
            "published": False,
        },
    )
    return draft_id


def stage_and_publish(
    session: requests.Session,
    token: str,
    draft_id: int,
    live: dict,
    replacement: dict[str, object],
) -> int:
    auth = {"Authorization": f"Bearer {token}"}
    vendor = {
        **auth,
        "Accept": "application/vnd.inveniordm.v1+json",
    }
    json_headers = {**vendor, "Content-Type": "application/json"}
    deposition = check(
        session.get(
            f"{API}/deposit/depositions/{draft_id}",
            headers=auth,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    files = legacy_file_map(deposition)
    predecessor_names = set(modern_entries(live))
    staged_names = predecessor_names - {OLD_ARCHIVE} | {NEW_ARCHIVE}
    if set(files) != predecessor_names and set(files) != staged_names:
        raise RuntimeError("Tracked draft has an unexpected file set")

    if OLD_ARCHIVE in files:
        check(
            session.delete(
                files[OLD_ARCHIVE]["links"]["self"],
                headers=auth,
                timeout=(30, 300),
            ),
            {204},
        )
    deposition = check(
        session.get(
            f"{API}/deposit/depositions/{draft_id}",
            headers=auth,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    files = legacy_file_map(deposition)
    existing = files.get(NEW_ARCHIVE)
    wanted_md5 = md5_path(NEW_ARCHIVE_PATH)
    if existing is not None:
        observed = (
            int(existing["filesize"]),
            normalize_md5(existing["checksum"]),
        )
        if observed != (int(replacement["bytes"]), wanted_md5):
            check(
                session.delete(
                    existing["links"]["self"],
                    headers=auth,
                    timeout=(30, 300),
                ),
                {204},
            )
            existing = None
    if existing is None:
        bucket = deposition["links"]["bucket"].rstrip("/")
        with NEW_ARCHIVE_PATH.open("rb") as handle:
            check(
                session.put(
                    f"{bucket}/{quote(NEW_ARCHIVE, safe='')}",
                    headers={
                        **auth,
                        "Content-Type": "application/octet-stream",
                    },
                    data=handle,
                    timeout=(30, 1800),
                ),
                {200, 201},
            )

    draft = check(
        session.get(
            f"{API}/records/{draft_id}/draft",
            headers=vendor,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    expected_names = predecessor_names - {OLD_ARCHIVE} | {NEW_ARCHIVE}
    if set(modern_entries(draft)) != expected_names:
        raise RuntimeError("Staged Noether file set is not exactly 20 files")
    entry = modern_entries(draft)[NEW_ARCHIVE]
    if (
        int(entry["size"]),
        normalize_md5(entry["checksum"]),
    ) != (
        int(replacement["bytes"]),
        wanted_md5,
    ):
        raise RuntimeError("Staged replacement archive identity mismatch")

    metadata = draft["metadata"]
    metadata["version"] = NEW_VERSION
    description = metadata.get("description", "")
    if DESCRIPTION_MARKER not in description:
        metadata["description"] = description + DESCRIPTION_APPEND
    note = (
        "Grouped archive 61 now retains the earlier source-audit set and "
        "adds privacy-clean Slavic repair survivors; direct reader ordering "
        "and default preview are unchanged. "
    )
    if not metadata.get("notes", "").startswith(note):
        metadata["notes"] = note + metadata.get("notes", "")

    old_order = list(live["files"].get("order") or modern_entries(live))
    order = [
        NEW_ARCHIVE if name == OLD_ARCHIVE else name for name in old_order
    ]
    if set(order) != expected_names or len(order) != EXPECTED_PREDECESSOR_FILES:
        raise RuntimeError("Noether file order replacement failed")
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
    patched = check(
        session.put(
            f"{API}/records/{draft_id}/draft",
            headers=json_headers,
            json=payload,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    if (
        len(modern_entries(patched)) != EXPECTED_PREDECESSOR_FILES
        or patched["files"].get("default_preview") != DEFAULT_PREVIEW
    ):
        raise RuntimeError("Patched Noether draft boundary changed")
    published = check(
        session.post(
            patched["links"]["publish"],
            headers=vendor,
            timeout=(30, 300),
        ),
        {202},
    ).json()
    record_id = int(published["id"])
    state = json.loads(DRAFT_STATE.read_text(encoding="utf-8"))
    state.update(
        {
            "published": True,
            "record_id": record_id,
            "doi": published["pids"]["doi"]["identifier"],
        }
    )
    save_json(DRAFT_STATE, state)
    return record_id


def stream_readback(
    session: requests.Session,
    url: str,
    destination: Path | None = None,
) -> tuple[int, str]:
    digest = hashlib.sha256()
    total = 0
    output = None
    if destination is not None:
        destination.parent.mkdir(parents=True, exist_ok=True)
        output = destination.open("wb")
    try:
        with check(
            session.get(url, stream=True, timeout=(30, 1800)),
            {200},
        ) as response:
            for block in response.iter_content(4 * 1024 * 1024):
                if block:
                    digest.update(block)
                    total += len(block)
                    if output is not None:
                        output.write(block)
    finally:
        if output is not None:
            output.close()
    return total, digest.hexdigest().upper()


def public_readback(
    session: requests.Session,
    token: str,
    record_id: int,
    previous_readback: dict[str, dict],
    replacement: dict[str, object],
) -> dict:
    public_headers = {"Accept": "application/vnd.inveniordm.v1+json"}
    live = None
    expected_names = set(previous_readback) - {OLD_ARCHIVE} | {NEW_ARCHIVE}
    for _ in range(36):
        response = session.get(
            f"{API}/records/{record_id}",
            headers=public_headers,
            timeout=(30, 180),
        )
        if response.status_code == 200:
            candidate = response.json()
            if set(modern_entries(candidate)) == expected_names:
                live = candidate
                break
        time.sleep(5)
    if live is None:
        raise RuntimeError("Published Noether successor did not become public")
    if (
        live["parent"]["pids"]["doi"]["identifier"] != CONCEPT_DOI
        or live["files"].get("default_preview") != DEFAULT_PREVIEW
        or len(modern_entries(live)) != EXPECTED_PREDECESSOR_FILES
    ):
        raise RuntimeError("Published Noether successor metadata is wrong")

    expected = {
        name: {
            "bytes": int(value["bytes"]),
            "sha256": value["sha256"].upper(),
        }
        for name, value in previous_readback.items()
        if name != OLD_ARCHIVE
    }
    expected[NEW_ARCHIVE] = {
        "bytes": int(replacement["bytes"]),
        "sha256": str(replacement["sha256"]),
    }
    remote_zip = WORK_ROOT / "remote_readback" / NEW_ARCHIVE
    readback = {}
    for index, name in enumerate(
        live["files"].get("order") or modern_entries(live),
        start=1,
    ):
        print(
            f"READBACK {index}/{EXPECTED_PREDECESSOR_FILES} {name}",
            flush=True,
        )
        destination = remote_zip if name == NEW_ARCHIVE else None
        observed = stream_readback(
            session,
            modern_entries(live)[name]["links"]["content"],
            destination,
        )
        wanted = (expected[name]["bytes"], expected[name]["sha256"])
        if observed != wanted:
            raise RuntimeError(
                f"Remote readback mismatch: {name}: {observed!r}"
            )
        readback[name] = {
            "bytes": observed[0],
            "sha256": observed[1],
            "url": modern_entries(live)[name]["links"]["content"],
        }
    remote_validation = validate_replacement_archive(remote_zip)
    if (
        remote_validation["sha256"] != replacement["sha256"]
        or remote_validation["members"] != EXPECTED_NEW_ARCHIVE_MEMBERS
    ):
        raise RuntimeError("Remote replacement archive member replay failed")

    latest = check(
        session.get(
            live["links"]["latest"],
            headers=public_headers,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    if int(latest["id"]) != record_id:
        raise RuntimeError("Noether latest route does not resolve to successor")
    predecessor = check(
        session.get(
            f"{API}/records/{PREDECESSOR_RECORD}",
            headers=public_headers,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    if len(modern_entries(predecessor)) != EXPECTED_PREDECESSOR_FILES:
        raise RuntimeError("Immutable Noether predecessor changed")

    vendor = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.inveniordm.v1+json",
    }
    active = session.get(
        f"{API}/records/{record_id}/draft",
        headers=vendor,
        timeout=(30, 60),
    )
    check(active, {404})

    receipt = {
        "status": "PASS_PUBLISHED_AND_READ_BACK",
        "errors": [],
        "record_id": record_id,
        "doi": live["pids"]["doi"]["identifier"],
        "conceptdoi": live["parent"]["pids"]["doi"]["identifier"],
        "version": live["metadata"]["version"],
        "file_count": len(modern_entries(live)),
        "total_bytes": sum(
            int(entry["size"]) for entry in modern_entries(live).values()
        ),
        "default_preview": live["files"]["default_preview"],
        "predecessor_record": PREDECESSOR_RECORD,
        "predecessor_doi": PREDECESSOR_DOI,
        "retained_files_exact": len(expected) - 1,
        "replacement_archive": remote_validation,
        "github": {
            "repository": REPOSITORY,
            "commit": GITHUB_COMMIT,
            "package": (
                "sources/noether/"
                "slavic-source-repair-survivors-20260730"
            ),
            "files_read_back_exact": EXPECTED_PACKAGE_FILES,
            "canonical_tree_sha256": EXPECTED_PACKAGE_TREE_SHA256,
        },
        "same_concept_latest_record": int(latest["id"]),
        "active_draft_after_publish": False,
        "duplicate_concept_created": False,
        "second_draft_created": False,
        "files": readback,
    }
    save_json(
        RECEIPT_ROOT
        / f"20260730_noether_record_{record_id}_public_readback.json",
        receipt,
    )
    save_json(
        RECEIPT_ROOT
        / f"20260730_noether_record_{record_id}_zip_member_readback.json",
        remote_validation,
    )
    if remote_zip.parent.is_dir():
        shutil.rmtree(remote_zip.parent)
    if NEW_ARCHIVE_PATH.is_file():
        NEW_ARCHIVE_PATH.unlink()
    return receipt


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--old-archive",
        type=Path,
        required=True,
    )
    parser.add_argument(
        "--previous-readback",
        type=Path,
        required=True,
    )
    parser.add_argument("--preflight", action="store_true")
    parser.add_argument("--publish", action="store_true")
    args = parser.parse_args()
    if not args.preflight and not args.publish:
        parser.error("Choose --preflight or --publish")
    previous = json.loads(args.previous_readback.read_text(encoding="utf-8"))
    replacement = build_replacement_archive(args.old_archive)
    token = find_token()
    session = make_session()
    live = public_preflight(session, token, previous)
    preflight = {
        "status": "PASS_PREFLIGHT",
        "errors": [],
        "predecessor_record": PREDECESSOR_RECORD,
        "predecessor_doi": PREDECESSOR_DOI,
        "conceptdoi": CONCEPT_DOI,
        "predecessor_files": len(modern_entries(live)),
        "predecessor_bytes": sum(
            int(entry["size"]) for entry in modern_entries(live).values()
        ),
        "default_preview": live["files"]["default_preview"],
        "replacement_archive": replacement,
    }
    save_json(WORK_ROOT / "zenodo_preflight.json", preflight)
    print(json.dumps(preflight, ensure_ascii=True, indent=2), flush=True)
    if args.preflight:
        return
    draft_id = create_or_resume_draft(session, token, live)
    record_id = stage_and_publish(
        session,
        token,
        draft_id,
        live,
        replacement,
    )
    result = public_readback(
        session,
        token,
        record_id,
        previous,
        replacement,
    )
    print(json.dumps(result, ensure_ascii=True, indent=2), flush=True)


if __name__ == "__main__":
    main()
