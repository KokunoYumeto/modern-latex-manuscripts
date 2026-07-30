#!/usr/bin/env python3
"""Publish and read back the compact SGA7 visual-evidence successor.

The transaction is additive. It inherits the exact live SGA record, replaces
only the release-control ZIP, adds two compact visual-evidence archives, keeps
the SGA1 reader as the default preview, and refuses an untracked draft or a
changed predecessor boundary.
"""

from __future__ import annotations

import csv
import hashlib
import io
import json
import os
import re
import subprocess
import time
import zipfile
from pathlib import Path, PurePosixPath
from urllib.parse import quote

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


API = "https://zenodo.org/api"
PUBLICATION_DATE = "2026-07-30"
CONCEPT_DOI = "10.5281/zenodo.20410947"
PREDECESSOR_RECORD = 21_707_869
PREDECESSOR_DOI = "10.5281/zenodo.21707869"
PREDECESSOR_FILES = 71
PREDECESSOR_BYTES = 480_981_780
DEFAULT_PREVIEW = "00a_SGA1_English_Reader.pdf"
CONTROLS_NAME = "10z_SGA_Current_Release_Controls_20260730.zip"
OLD_CONTROLS = (
    21_868,
    "5766E524DF5B3AA61718445F90D7B50826AB77106022E6852066D1C9C9D01E90",
)

REPO_ROOT = Path(__file__).resolve().parents[1]
PACKAGE_REL = Path(
    "sources/sga/sga7i-highdetail-source-audit-visual-evidence-20260730"
)
PACKAGE_ROOT = REPO_ROOT / PACKAGE_REL
UPLOAD_ROOT = (
    Path(os.environ["LOCALAPPDATA"])
    / "Temp"
    / "sga7i-visual-evidence-upload-20260730"
)
TEMP_ROOT = (
    Path(os.environ["LOCALAPPDATA"])
    / "Temp"
    / "sga7i-visual-evidence-zenodo-transaction-20260730"
)
CONTROLS_ROOT = TEMP_ROOT / "release-controls"
STATE_PATH = TEMP_ROOT / "draft_state.json"
RECEIPT_ROOT = REPO_ROOT / "manifests" / "published-zenodo"
TOKEN_LOG = Path(
    os.environ.get(
        "ZENODO_TOKEN_LOG",
        Path.home() / ".codex" / ".sandbox" / "sandbox.log",
    )
)

IMAGE_ZIP = "10x_SGA7I_SourceAudit_Opened_Targeted_Crops_20260730.zip"
METADATA_ZIP = (
    "10y_SGA7I_SourceAudit_Visual_Provenance_"
    "RightsBlocked_Metadata_20260730.zip"
)
EXPECTED_UPLOADS = {
    IMAGE_ZIP: (
        1_348_411,
        "4D231B538AA7EDEC1ABF77BABC16BEC1CD8D6E084AFF3A7D21A91FB19211E8D4",
        17,
        1_358_702,
    ),
    METADATA_ZIP: (
        1_911_788,
        "33B87235BCECB8274D18FCE0B7B2952A8301AD16E1C61C3825FACDB97BDFCEC4",
        11,
        10_556_018,
    ),
}
PACKAGE_MANIFEST = (
    1_265,
    "8B1351DF70B64B3FD6B4236AD61A144CCA9E2A7BE04FB9E02F61FFBB9A07F86C",
    12,
)

README_NAME = "09_README_CURRENT_RELEASE.md"
RELEASE_MANIFEST_NAME = "09a_RELEASE_FILE_MANIFEST.csv"
RELEASE_VALIDATION_NAME = "09b_RELEASE_VALIDATION.json"
PACKED_MANIFEST_NAME = "PACKED_CONTROL_SHA256.csv"
VISUAL_VALIDATION_NAME = "09k_SGA7I_VISUAL_EVIDENCE_VALIDATION.json"
VISUAL_SUMS_NAME = "09l_SGA7I_VISUAL_EVIDENCE_SHA256SUMS.csv"
VISUAL_GITHUB_NAME = "09m_SGA7I_VISUAL_EVIDENCE_GITHUB_READBACK.json"
VISUAL_ARCHIVE_NAME = "09n_SGA7I_VISUAL_EVIDENCE_ARCHIVE_BUILD.json"
VISUAL_UPLOAD_NAME = "09o_SGA7I_VISUAL_EVIDENCE_UPLOAD_MANIFEST.csv"

DIRECT_READERS = tuple(
    f"00{chr(96 + index)}_SGA{index}_English_Reader.pdf"
    for index in range(1, 7)
) + ("00g_SGA7I_Fresh_Source_Transcription_I_II_VI_VII_VIII_Working.pdf",)
DIRECT_TEX = tuple(
    f"02{chr(96 + index)}_SGA{index}_English_Master.tex"
    for index in range(1, 7)
) + ("02g_SGA7I_Fresh_Source_Transcription_I_II_VI_VII_VIII_Working.tex",)
LEADING_BUNDLE = "00_Current_SGA1-6_English_Readers_and_Buildable_TeX_20260730.zip"


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


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


def normalized_md5(value: str) -> str:
    return value.lower().removeprefix("md5:")


def save_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, ensure_ascii=True, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=True, indent=2) + "\n").encode(
        "utf-8"
    )


def csv_bytes(rows: list[dict[str, object]], fields: list[str]) -> bytes:
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue().encode("utf-8")


def read_csv_bytes(data: bytes) -> list[dict[str, str]]:
    return list(csv.DictReader(io.StringIO(data.decode("utf-8-sig"))))


def safe_member(name: str) -> bool:
    pure = PurePosixPath(name)
    return (
        name == name.replace("\\", "/")
        and not pure.is_absolute()
        and ".." not in pure.parts
        and not re.match(r"^[A-Za-z]:", name)
    )


def find_token() -> str:
    direct = os.environ.get("ZENODO_TOKEN")
    if direct:
        return direct
    data = TOKEN_LOG.read_text(encoding="utf-8", errors="ignore")
    candidates = sorted(
        set(
            re.findall(
                r"(?<![A-Za-z0-9])[A-Za-z0-9]{60}(?![A-Za-z0-9])",
                data,
            )
        )
    )
    if len(candidates) != 1:
        raise RuntimeError(
            "Expected exactly one locally retained Zenodo credential; "
            f"found {len(candidates)}"
        )
    return candidates[0]


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


def check(response: requests.Response, expected: set[int]) -> requests.Response:
    if response.status_code not in expected:
        raise RuntimeError(
            f"Zenodo HTTP {response.status_code} for "
            f"{response.request.method} {response.url}: "
            f"{response.text[:2000]}"
        )
    return response


def modern_entries(record: dict) -> dict[str, dict]:
    return record["files"]["entries"]


def legacy_entries(record: dict) -> dict[str, dict]:
    return {entry["filename"]: entry for entry in record["files"]}


def git_commit() -> str:
    return subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=REPO_ROOT, text=True
    ).strip()


def replay_zip_bytes(data: bytes, expected: tuple[int, str, int, int]) -> dict:
    expected_bytes, expected_sha, expected_members, expected_uncompressed = expected
    if (len(data), sha256_bytes(data)) != (expected_bytes, expected_sha):
        raise RuntimeError("ZIP outer identity changed")
    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        infos = [item for item in archive.infolist() if not item.is_dir()]
        names = [item.filename for item in infos]
        if (
            archive.testzip() is not None
            or len(infos) != expected_members
            or sum(item.file_size for item in infos) != expected_uncompressed
            or len(names) != len(set(names))
            or not all(safe_member(name) for name in names)
        ):
            raise RuntimeError("ZIP member boundary changed")
        rows = read_csv_bytes(archive.read("ARCHIVE_MEMBER_SHA256.csv"))
        if len(rows) != len(infos) - 1:
            raise RuntimeError("ZIP member manifest boundary changed")
        identities = {}
        for row in rows:
            member = archive.read(row["archive_member_path"])
            observed = (len(member), sha256_bytes(member))
            wanted = (int(row["bytes"]), row["sha256"].upper())
            if observed != wanted:
                raise RuntimeError(
                    f"ZIP member mismatch: {row['archive_member_path']}"
                )
            identities[row["archive_member_path"]] = {
                "bytes": observed[0],
                "sha256": observed[1],
            }
        return {
            "status": "PASS",
            "members": len(infos),
            "manifest_rows": len(rows),
            "uncompressed_bytes": sum(item.file_size for item in infos),
            "member_identities": identities,
        }


def local_preflight() -> dict:
    manifest = PACKAGE_ROOT / "SHA256SUMS.csv"
    if (manifest.stat().st_size, sha256_path(manifest)) != PACKAGE_MANIFEST[:2]:
        raise RuntimeError("SGA7 visual-evidence package manifest changed")
    rows = read_csv_bytes(manifest.read_bytes())
    if len(rows) != PACKAGE_MANIFEST[2]:
        raise RuntimeError("SGA7 visual-evidence manifest row count changed")
    if set(row["relative_path"] for row in rows) != {
        path.name for path in PACKAGE_ROOT.iterdir() if path.is_file()
    } - {"SHA256SUMS.csv"}:
        raise RuntimeError("SGA7 visual-evidence manifest closure changed")
    for row in rows:
        path = PACKAGE_ROOT / row["relative_path"]
        if (path.stat().st_size, sha256_path(path)) != (
            int(row["bytes"]),
            row["sha256"].upper(),
        ):
            raise RuntimeError(f"Package mismatch: {path.name}")
    archives = {}
    for name, expected in EXPECTED_UPLOADS.items():
        path = UPLOAD_ROOT / name
        archives[name] = replay_zip_bytes(path.read_bytes(), expected)
    return {
        "status": "PASS",
        "package_files": len(rows) + 1,
        "package_manifest_sha256": PACKAGE_MANIFEST[1],
        "archives": archives,
    }


def github_readback(commit: str) -> dict:
    base = (
        "https://raw.githubusercontent.com/KokunoYumeto/"
        f"modern-latex-manuscripts/{commit}/{PACKAGE_REL.as_posix()}"
    )
    session = make_session()
    manifest_response = check(
        session.get(f"{base}/SHA256SUMS.csv", timeout=(30, 180)), {200}
    )
    manifest_data = manifest_response.content
    if (len(manifest_data), sha256_bytes(manifest_data)) != PACKAGE_MANIFEST[:2]:
        raise RuntimeError("GitHub package manifest identity changed")
    rows = read_csv_bytes(manifest_data)
    errors = []
    for row in rows:
        url = f"{base}/{quote(row['relative_path'], safe='/')}"
        data = check(session.get(url, timeout=(30, 600)), {200}).content
        if (len(data), sha256_bytes(data)) != (
            int(row["bytes"]),
            row["sha256"].upper(),
        ):
            errors.append(row["relative_path"])
    return {
        "status": "PASS_GITHUB_PUBLIC_READBACK" if not errors else "FAIL",
        "commit": commit,
        "package_path": PACKAGE_REL.as_posix(),
        "files_read_back": len(rows) + 1,
        "manifest_rows": len(rows),
        "manifest_sha256": sha256_bytes(manifest_data),
        "errors": errors,
    }


def current_predecessor(session: requests.Session) -> dict:
    headers = {"Accept": "application/vnd.inveniordm.v1+json"}
    record = check(
        session.get(
            f"{API}/records/{PREDECESSOR_RECORD}/versions/latest",
            headers=headers,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    entries = modern_entries(record)
    observed = (
        int(record["id"]),
        record["pids"]["doi"]["identifier"],
        record["parent"]["pids"]["doi"]["identifier"],
        len(entries),
        sum(int(entry["size"]) for entry in entries.values()),
        record["files"].get("default_preview"),
    )
    expected = (
        PREDECESSOR_RECORD,
        PREDECESSOR_DOI,
        CONCEPT_DOI,
        PREDECESSOR_FILES,
        PREDECESSOR_BYTES,
        DEFAULT_PREVIEW,
    )
    if observed != expected:
        raise RuntimeError(f"Live SGA predecessor boundary changed: {observed!r}")
    if set(EXPECTED_UPLOADS) & set(entries):
        raise RuntimeError("Visual-evidence archive already exists on live head")
    return record


def unpack_current_controls(session: requests.Session, record: dict) -> list[dict[str, str]]:
    if CONTROLS_ROOT.exists():
        for path in CONTROLS_ROOT.iterdir():
            if path.is_file():
                path.unlink()
    CONTROLS_ROOT.mkdir(parents=True, exist_ok=True)
    entry = modern_entries(record)[CONTROLS_NAME]
    data = check(
        session.get(entry["links"]["content"], timeout=(30, 300)), {200}
    ).content
    if (len(data), sha256_bytes(data)) != OLD_CONTROLS:
        raise RuntimeError("Current release-controls identity changed")
    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        if archive.testzip() is not None:
            raise RuntimeError("Current release-controls CRC failed")
        infos = [item for item in archive.infolist() if not item.is_dir()]
        if len(infos) != 12 or not all(safe_member(item.filename) for item in infos):
            raise RuntimeError("Current release-controls boundary changed")
        for item in infos:
            (CONTROLS_ROOT / item.filename).write_bytes(archive.read(item.filename))
    packed = read_csv_bytes((CONTROLS_ROOT / PACKED_MANIFEST_NAME).read_bytes())
    if len(packed) != 11:
        raise RuntimeError("Current packed-control boundary changed")
    for row in packed:
        path = CONTROLS_ROOT / row["filename"]
        if (path.stat().st_size, sha256_path(path)) != (
            int(row["bytes"]),
            row["sha256"].upper(),
        ):
            raise RuntimeError(f"Current packed-control mismatch: {path.name}")
    rows = read_csv_bytes((CONTROLS_ROOT / RELEASE_MANIFEST_NAME).read_bytes())
    if len(rows) != 70:
        raise RuntimeError("Current release-manifest boundary changed")
    if {row["filename"] for row in rows} != set(modern_entries(record)) - {
        CONTROLS_NAME
    }:
        raise RuntimeError("Current release-manifest closure changed")
    return rows


def prepare_controls(
    session: requests.Session,
    predecessor: dict,
    commit: str,
    github: dict,
    local: dict,
) -> tuple[Path, dict[str, dict[str, object]]]:
    old_rows = unpack_current_controls(session, predecessor)
    readme = (CONTROLS_ROOT / README_NAME).read_text(encoding="utf-8")
    addition = """

## SGA7 source-audit visual evidence

Two compact archives add 12 high-detail source crops that were actually opened
during SGA7 transcription and diagram review, plus provenance metadata for the
larger generated scratch surface whose pixels remain withheld. Whole-page
renders and the parent scan are excluded. This evidence does not change or
certify any reader, transcription, translation, mathematics, or source rights.
"""
    if "## SGA7 source-audit visual evidence" not in readme:
        (CONTROLS_ROOT / README_NAME).write_text(
            readme.rstrip() + addition + "\n",
            encoding="utf-8",
            newline="\n",
        )

    additions = {
        IMAGE_ZIP: {
            "filename": IMAGE_ZIP,
            "bytes": EXPECTED_UPLOADS[IMAGE_ZIP][0],
            "sha256": EXPECTED_UPLOADS[IMAGE_ZIP][1],
            "role": "opened_targeted_source_audit_crops",
            "provenance": (
                "12 actually opened targeted SGA7 source-audit crops from six "
                f"parent pages; GitHub commit {commit}"
            ),
            "status": "current_sparse_visual_evidence",
        },
        METADATA_ZIP: {
            "filename": METADATA_ZIP,
            "bytes": EXPECTED_UPLOADS[METADATA_ZIP][0],
            "sha256": EXPECTED_UPLOADS[METADATA_ZIP][1],
            "role": "visual_provenance_and_rights_blocked_metadata",
            "provenance": (
                "provenance index for 14,744 unique SGA7 scratch images, with "
                f"14,732 pixel-withheld dispositions; GitHub commit {commit}"
            ),
            "status": "current_visual_provenance_metadata",
        },
    }
    rows = old_rows + list(additions.values())
    rows.sort(key=lambda row: row["filename"].casefold())
    (CONTROLS_ROOT / RELEASE_MANIFEST_NAME).write_bytes(
        csv_bytes(
            rows,
            ["filename", "bytes", "sha256", "role", "provenance", "status"],
        )
    )

    copies = {
        VISUAL_VALIDATION_NAME: "SGA7I_VISUAL_EVIDENCE_VALIDATION.json",
        VISUAL_SUMS_NAME: "SHA256SUMS.csv",
        VISUAL_ARCHIVE_NAME: "SGA7I_ARCHIVE_BUILD_VALIDATION.json",
        VISUAL_UPLOAD_NAME: "SGA7I_ZENODO_UPLOAD_MANIFEST.csv",
    }
    for destination, source in copies.items():
        (CONTROLS_ROOT / destination).write_bytes((PACKAGE_ROOT / source).read_bytes())
    (CONTROLS_ROOT / VISUAL_GITHUB_NAME).write_bytes(json_bytes(github))

    validation = {
        "status": "PASS_READY_FOR_SINGLE_SAME_CONCEPT_SUCCESSOR",
        "prepared_at": PUBLICATION_DATE,
        "concept_doi": CONCEPT_DOI,
        "predecessor_record": PREDECESSOR_RECORD,
        "predecessor_files": PREDECESSOR_FILES,
        "predecessor_bytes": PREDECESSOR_BYTES,
        "expected_successor_files": 73,
        "retained_predecessor_files": 70,
        "replaced_files": [CONTROLS_NAME],
        "added_files": {
            name: {"bytes": value[0], "sha256": value[1]}
            for name, value in EXPECTED_UPLOADS.items()
        },
        "visual_evidence_scope": {
            "opened_targeted_crops": 12,
            "parent_pages": 6,
            "unique_indexed_images": 14_744,
            "withheld_pixel_images": 14_732,
            "whole_page_images_published": 0,
            "parent_scan_published": False,
            "reader_changed": False,
        },
        "github_commit": commit,
        "github_readback": github,
        "local_archive_replay": local,
        "default_preview_expected": DEFAULT_PREVIEW,
        "duplicate_concept_created": False,
        "second_draft_created": False,
        "errors": [],
    }
    (CONTROLS_ROOT / RELEASE_VALIDATION_NAME).write_bytes(json_bytes(validation))

    packed_rows = []
    for path in sorted(CONTROLS_ROOT.iterdir(), key=lambda item: item.name.casefold()):
        if path.name == PACKED_MANIFEST_NAME:
            continue
        packed_rows.append(
            {
                "filename": path.name,
                "bytes": path.stat().st_size,
                "sha256": sha256_path(path),
            }
        )
    (CONTROLS_ROOT / PACKED_MANIFEST_NAME).write_bytes(
        csv_bytes(packed_rows, ["filename", "bytes", "sha256"])
    )
    controls_zip = TEMP_ROOT / CONTROLS_NAME
    with zipfile.ZipFile(
        controls_zip, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9
    ) as archive:
        for path in sorted(CONTROLS_ROOT.iterdir(), key=lambda item: item.name.casefold()):
            info = zipfile.ZipInfo(path.name, (1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            archive.writestr(info, path.read_bytes())

    expected_files = {
        name: {
            "bytes": int(entry["size"]),
            "md5": normalized_md5(entry["checksum"]),
        }
        for name, entry in modern_entries(predecessor).items()
        if name != CONTROLS_NAME
    }
    for name, expected in EXPECTED_UPLOADS.items():
        expected_files[name] = {
            "bytes": expected[0],
            "sha256": expected[1],
            "md5": md5_path(UPLOAD_ROOT / name),
        }
    expected_files[CONTROLS_NAME] = {
        "bytes": controls_zip.stat().st_size,
        "sha256": sha256_path(controls_zip),
        "md5": md5_path(controls_zip),
    }
    if len(expected_files) != 73:
        raise RuntimeError("Prepared successor file boundary changed")
    save_json(
        TEMP_ROOT / "prepare_result.json",
        {
            "status": "PASS_PREPARED",
            "github_commit": commit,
            "expected_files": expected_files,
            "controls_members": len(packed_rows) + 1,
            "controls_manifest_rows": len(packed_rows),
        },
    )
    return controls_zip, expected_files


def create_or_resume_draft(
    session: requests.Session, token: str, predecessor: dict
) -> int:
    auth = {"Authorization": f"Bearer {token}"}
    vendor = {**auth, "Accept": "application/vnd.inveniordm.v1+json"}
    if STATE_PATH.is_file():
        state = json.loads(STATE_PATH.read_text(encoding="utf-8"))
        if state.get("published"):
            return int(state["record_id"])
        draft_id = int(state["draft_id"])
        check(
            session.get(
                f"{API}/records/{draft_id}/draft",
                headers=vendor,
                timeout=(30, 120),
            ),
            {200},
        )
        return draft_id
    active = session.get(
        f"{API}/records/{PREDECESSOR_RECORD}/draft",
        headers=vendor,
        timeout=(30, 120),
    )
    if active.status_code == 200:
        raise RuntimeError("Untracked SGA successor draft exists")
    check(active, {404})
    deposition = check(
        session.get(
            f"{API}/deposit/depositions/{PREDECESSOR_RECORD}",
            headers=auth,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    if deposition.get("state") != "done" or not deposition.get("submitted"):
        raise RuntimeError("SGA predecessor is not a valid versioning base")
    created = check(
        session.post(
            deposition["links"]["newversion"],
            headers=auth,
            timeout=(30, 300),
        ),
        {201},
    ).json()
    draft = check(
        session.get(created["links"]["latest_draft"], headers=auth, timeout=(30, 180)),
        {200},
    ).json()
    if set(legacy_entries(draft)) != set(modern_entries(predecessor)):
        raise RuntimeError("New SGA draft did not inherit exact predecessor files")
    draft_id = int(draft["id"])
    save_json(
        STATE_PATH,
        {
            "status": "OPEN_TRACKED_DRAFT",
            "predecessor_record": PREDECESSOR_RECORD,
            "draft_id": draft_id,
            "published": False,
        },
    )
    return draft_id


def ordered_names(names: set[str]) -> list[str]:
    direct = {LEADING_BUNDLE, *DIRECT_READERS, *DIRECT_TEX}
    if not direct.issubset(names):
        raise RuntimeError("Current direct SGA reader surface is incomplete")
    remainder = names - direct
    other_pdfs = sorted(
        (name for name in remainder if name.lower().endswith(".pdf")),
        key=str.casefold,
    )
    other_tex = sorted(
        (name for name in remainder if name.lower().endswith(".tex")),
        key=str.casefold,
    )
    archival = sorted(
        remainder - set(other_pdfs) - set(other_tex), key=str.casefold
    )
    return [LEADING_BUNDLE, *DIRECT_READERS, *DIRECT_TEX, *other_pdfs, *other_tex, *archival]


def stage_and_publish(
    session: requests.Session,
    token: str,
    predecessor: dict,
    draft_id: int,
    controls_zip: Path,
) -> int:
    if STATE_PATH.is_file():
        state = json.loads(STATE_PATH.read_text(encoding="utf-8"))
        if state.get("published"):
            return int(state["record_id"])
    auth = {"Authorization": f"Bearer {token}"}
    vendor = {**auth, "Accept": "application/vnd.inveniordm.v1+json"}
    json_headers = {**vendor, "Content-Type": "application/json"}
    deposition = check(
        session.get(
            f"{API}/deposit/depositions/{draft_id}",
            headers=auth,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    files = legacy_entries(deposition)
    predecessor_names = set(modern_entries(predecessor))
    expected_names = predecessor_names | set(EXPECTED_UPLOADS)
    allowed = (predecessor_names, expected_names)
    if set(files) not in allowed:
        raise RuntimeError("Tracked SGA draft has an unexpected file set")
    if CONTROLS_NAME in files:
        check(
            session.delete(
                files[CONTROLS_NAME]["links"]["self"],
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
        files = legacy_entries(deposition)
    uploads = {
        CONTROLS_NAME: controls_zip,
        IMAGE_ZIP: UPLOAD_ROOT / IMAGE_ZIP,
        METADATA_ZIP: UPLOAD_ROOT / METADATA_ZIP,
    }
    bucket = deposition["links"]["bucket"].rstrip("/")
    for name, path in uploads.items():
        existing = files.get(name)
        wanted = (path.stat().st_size, md5_path(path))
        if existing is not None:
            observed = (
                int(existing["filesize"]),
                normalized_md5(existing["checksum"]),
            )
            if observed != wanted:
                raise RuntimeError(f"Staged upload identity changed: {name}")
            continue
        with path.open("rb") as handle:
            check(
                session.put(
                    f"{bucket}/{quote(name, safe='')}",
                    headers={**auth, "Content-Type": "application/octet-stream"},
                    data=handle,
                    timeout=(30, 1800),
                ),
                {200, 201},
            )
        files[name] = {"filesize": wanted[0], "checksum": f"md5:{wanted[1]}"}

    draft = check(
        session.get(
            f"{API}/records/{draft_id}/draft",
            headers=vendor,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    entries = modern_entries(draft)
    if set(entries) != expected_names or len(entries) != 73:
        raise RuntimeError("Staged SGA file set is not exact")
    order = ordered_names(expected_names)
    metadata = draft["metadata"]
    metadata["publication_date"] = PUBLICATION_DATE
    metadata["version"] = "2026-07-30 SGA7 targeted source-audit visual evidence"
    paragraph = (
        "<p><strong>SGA7 source-audit visual evidence:</strong> two compact "
        "archives add 12 targeted high-detail crops actually opened during "
        "transcription and diagram review, plus provenance metadata for the "
        "larger rights-blocked image surface. The parent scan and whole-page "
        "renders are excluded. No reader file changes in this version.</p>"
    )
    description = metadata.get("description", "")
    if paragraph not in description:
        metadata["description"] = paragraph + "\n" + description
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
        set(modern_entries(patched)) != expected_names
        or patched["files"].get("default_preview") != DEFAULT_PREVIEW
    ):
        raise RuntimeError("Patched SGA draft controls changed")
    returned_order = patched["files"].get("order") or []
    if returned_order and returned_order != order:
        raise RuntimeError("Patched SGA file order changed")
    published = check(
        session.post(patched["links"]["publish"], headers=vendor, timeout=(30, 300)),
        {202},
    ).json()
    record_id = int(published["id"])
    state = json.loads(STATE_PATH.read_text(encoding="utf-8"))
    state.update(
        {
            "status": "PUBLISHED_PENDING_READBACK",
            "published": True,
            "record_id": record_id,
            "doi": published["pids"]["doi"]["identifier"],
        }
    )
    save_json(STATE_PATH, state)
    return record_id


def stream_identity(
    session: requests.Session, url: str, capture: bool = False
) -> tuple[dict[str, object], bytes | None]:
    digest = hashlib.sha256()
    md5 = hashlib.md5(usedforsecurity=False)
    total = 0
    captured = io.BytesIO() if capture else None
    with check(session.get(url, stream=True, timeout=(30, 1800)), {200}) as response:
        for block in response.iter_content(4 * 1024 * 1024):
            if not block:
                continue
            digest.update(block)
            md5.update(block)
            total += len(block)
            if captured is not None:
                captured.write(block)
    return (
        {
            "bytes": total,
            "sha256": digest.hexdigest().upper(),
            "md5": md5.hexdigest().lower(),
            "content_url": url,
        },
        captured.getvalue() if captured is not None else None,
    )


def replay_controls(data: bytes) -> dict:
    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        if archive.testzip() is not None:
            raise RuntimeError("Published release-controls CRC failed")
        infos = [item for item in archive.infolist() if not item.is_dir()]
        rows = read_csv_bytes(archive.read(PACKED_MANIFEST_NAME))
        if len(rows) != len(infos) - 1:
            raise RuntimeError("Published release-controls boundary changed")
        for row in rows:
            member = archive.read(row["filename"])
            if (len(member), sha256_bytes(member)) != (
                int(row["bytes"]),
                row["sha256"].upper(),
            ):
                raise RuntimeError(f"Published control mismatch: {row['filename']}")
        release_rows = read_csv_bytes(archive.read(RELEASE_MANIFEST_NAME))
        if len(release_rows) != 72:
            raise RuntimeError("Published release manifest row boundary changed")
        return {
            "status": "PASS",
            "members": len(infos),
            "manifest_rows": len(rows),
            "release_manifest_rows": len(release_rows),
            "uncompressed_bytes": sum(item.file_size for item in infos),
        }


def public_readback(
    session: requests.Session,
    predecessor: dict,
    record_id: int,
    expected_files: dict[str, dict[str, object]],
) -> dict:
    headers = {"Accept": "application/vnd.inveniordm.v1+json"}
    record = None
    for _ in range(60):
        response = session.get(
            f"{API}/records/{record_id}", headers=headers, timeout=(30, 180)
        )
        if response.status_code == 200 and response.json().get("is_published"):
            record = response.json()
            break
        time.sleep(2)
    if record is None:
        raise RuntimeError("Published SGA successor did not become readable")
    entries = modern_entries(record)
    if (
        set(entries) != set(expected_files)
        or len(entries) != 73
        or record["parent"]["pids"]["doi"]["identifier"] != CONCEPT_DOI
        or record["files"].get("default_preview") != DEFAULT_PREVIEW
    ):
        raise RuntimeError("Published SGA successor boundary changed")
    expected_order = ordered_names(set(entries))
    api_order = record["files"].get("order") or []
    if api_order and api_order != expected_order:
        raise RuntimeError("Published SGA file order changed")

    predecessor_entries = modern_entries(predecessor)
    retained = set(predecessor_entries) - {CONTROLS_NAME}
    if len(retained) != 70:
        raise RuntimeError("Retained predecessor boundary changed")
    for name in retained:
        old = predecessor_entries[name]
        new = entries[name]
        if (int(new["size"]), normalized_md5(new["checksum"])) != (
            int(old["size"]),
            normalized_md5(old["checksum"]),
        ):
            raise RuntimeError(f"Retained predecessor changed: {name}")

    outer = {}
    captured = {}
    for index, name in enumerate(sorted(entries, key=str.casefold), start=1):
        result, data = stream_identity(
            session,
            entries[name]["links"]["content"],
            capture=name in {IMAGE_ZIP, METADATA_ZIP, CONTROLS_NAME},
        )
        if result["bytes"] != int(entries[name]["size"]) or result["md5"] != normalized_md5(
            entries[name]["checksum"]
        ):
            raise RuntimeError(f"Public outer-file mismatch: {name}")
        expected = expected_files[name]
        if "sha256" in expected and result["sha256"] != expected["sha256"]:
            raise RuntimeError(f"Public SHA-256 mismatch: {name}")
        outer[name] = {**result, "readback_ordinal": index}
        if data is not None:
            captured[name] = data

    image_replay = replay_zip_bytes(captured[IMAGE_ZIP], EXPECTED_UPLOADS[IMAGE_ZIP])
    metadata_replay = replay_zip_bytes(
        captured[METADATA_ZIP], EXPECTED_UPLOADS[METADATA_ZIP]
    )
    controls_replay = replay_controls(captured[CONTROLS_NAME])
    result = {
        "status": "PASS_PUBLIC_READBACK",
        "record_id": int(record["id"]),
        "record_url": record["links"]["self_html"],
        "doi": record["pids"]["doi"]["identifier"],
        "concept_doi": record["parent"]["pids"]["doi"]["identifier"],
        "predecessor_record": PREDECESSOR_RECORD,
        "github_commit": git_commit(),
        "outer_files": len(outer),
        "outer_bytes": sum(int(item["bytes"]) for item in outer.values()),
        "outer_files_streamed": len(outer),
        "retained_predecessor_files": len(retained),
        "retained_predecessor_identity_errors": 0,
        "added_files": [IMAGE_ZIP, METADATA_ZIP],
        "replaced_files": [CONTROLS_NAME],
        "default_preview": record["files"].get("default_preview"),
        "configured_file_order": expected_order,
        "api_file_order": api_order,
        "outer_file_readback": outer,
        "image_zip_readback": image_replay,
        "metadata_zip_readback": metadata_replay,
        "controls_zip_readback": controls_replay,
        "duplicate_concept_created": False,
        "second_draft_created": False,
        "errors": [],
    }
    RECEIPT_ROOT.mkdir(parents=True, exist_ok=True)
    receipt = RECEIPT_ROOT / (
        f"20260730_sga7i_highdetail_visual_evidence_record_{record_id}_"
        "public_readback.json"
    )
    save_json(receipt, result)
    result["receipt_path"] = str(receipt)
    return result


def main() -> int:
    token = find_token()
    session = make_session()
    if STATE_PATH.is_file():
        state = json.loads(STATE_PATH.read_text(encoding="utf-8"))
        if state.get("published"):
            predecessor = check(
                session.get(
                    f"{API}/records/{PREDECESSOR_RECORD}",
                    headers={"Accept": "application/vnd.inveniordm.v1+json"},
                    timeout=(30, 180),
                ),
                {200},
            ).json()
            prepared = json.loads((TEMP_ROOT / "prepare_result.json").read_text())
            result = public_readback(
                session, predecessor, int(state["record_id"]), prepared["expected_files"]
            )
            print(json.dumps(result, indent=2))
            return 0

    local = local_preflight()
    commit = git_commit()
    github = github_readback(commit)
    if github["status"] != "PASS_GITHUB_PUBLIC_READBACK":
        raise RuntimeError("GitHub public readback failed")
    predecessor = current_predecessor(session)
    controls_zip, expected_files = prepare_controls(
        session, predecessor, commit, github, local
    )
    draft_id = create_or_resume_draft(session, token, predecessor)
    record_id = stage_and_publish(
        session, token, predecessor, draft_id, controls_zip
    )
    result = public_readback(session, predecessor, record_id, expected_files)
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
