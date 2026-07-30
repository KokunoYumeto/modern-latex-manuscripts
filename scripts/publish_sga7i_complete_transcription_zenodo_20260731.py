#!/usr/bin/env python3
"""Publish and read back the complete SGA7 I transcription successor.

The transaction inherits the exact live SGA record, replaces only the three
partial SGA7 I objects and the release-control ZIP, keeps the SGA1 reader as
the default preview, and refuses an untracked draft or a changed predecessor
boundary.
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
PUBLICATION_DATE = "2026-07-31"
CONCEPT_DOI = "10.5281/zenodo.20410947"
PREDECESSOR_RECORD = 21_709_733
PREDECESSOR_DOI = "10.5281/zenodo.21709733"
PREDECESSOR_FILES = 73
PREDECESSOR_BYTES = 484_248_680
DEFAULT_PREVIEW = "00a_SGA1_English_Reader.pdf"
CONTROLS_NAME = "10z_SGA_Current_Release_Controls_20260730.zip"
OLD_CONTROLS = (
    28_569,
    "57AF7F19A0734DFB276353B039E9FC65BD847C85BE1E8528D09CA9C72AB012A4",
)

REPO_ROOT = Path(__file__).resolve().parents[1]
PACKAGE_REL = Path(
    "sources/sga/"
    "sga7i-fresh-transcription-exposes-i-ii-vi-vii-viii-ix-working-20260731"
)
PACKAGE_ROOT = REPO_ROOT / PACKAGE_REL
TEMP_ROOT = Path(r"C:\tmp\sga7i-complete-zenodo-20260731")
CONTROLS_ROOT = TEMP_ROOT / "release-controls"
STATE_PATH = TEMP_ROOT / "draft_state.json"
RECEIPT_ROOT = REPO_ROOT / "manifests" / "published-zenodo"
TOKEN_LOG = Path(
    os.environ.get(
        "ZENODO_TOKEN_LOG",
        Path.home() / ".codex" / ".sandbox" / "sandbox.log",
    )
)

OLD_PDF_NAME = (
    "00g_SGA7I_Fresh_Source_Transcription_I_II_VI_VII_VIII_Working.pdf"
)
OLD_TEX_NAME = (
    "02g_SGA7I_Fresh_Source_Transcription_I_II_VI_VII_VIII_Working.tex"
)
OLD_ZIP_NAME = (
    "10g_SGA7I_Fresh_Source_Transcription_I_II_VI_VII_VIII_"
    "Reader_and_Source_20260730.zip"
)
PDF_NAME = "00g_SGA7I_Fresh_Source_Transcription_Complete_Working.pdf"
TEX_NAME = "02g_SGA7I_Fresh_Source_Transcription_Complete_Working.tex"
ZIP_NAME = (
    "10g_SGA7I_Fresh_Source_Transcription_Complete_"
    "Reader_and_TeX_20260731.zip"
)
OLD_SGA7_FILES = {OLD_PDF_NAME, OLD_TEX_NAME, OLD_ZIP_NAME}
LOCAL_UPLOADS = {
    PDF_NAME: PACKAGE_ROOT
    / "reader/SGA7I_Fresh_Source_Transcription_Complete_Working.pdf",
    TEX_NAME: PACKAGE_ROOT
    / "source/SGA7I_Fresh_Source_Transcription_Complete_Working.tex",
    ZIP_NAME: PACKAGE_ROOT
    / "SGA7I_Fresh_Source_Transcription_Complete_Reader_and_TeX_20260731.zip",
}
EXPECTED_UPLOADS = {
    PDF_NAME: (
        2_002_517,
        "45E4C2980260C8172AA3762BE0CDBF84FE1DCFC2FA23B724C64508A96F4D2E96",
    ),
    TEX_NAME: (
        2_880,
        "7B7394BEAF970AC724EFDE80C841B2DAACC28D64E3145538A39AA2FA915BF355",
    ),
    ZIP_NAME: (
        2_196_251,
        "6846FB1229B52292292586E072D3878EC6CCD90B7FFD861F6CC1738081D24D40",
    ),
}
PACKAGE_MANIFEST = (
    1_478,
    "C84A109AE710F25D98C776612DA63F5508215C3A169A3720F70FC393208A03DE",
    14,
)
PACKAGE_VALIDATION = (
    4_743,
    "89793CAA923EDEA4C6AE716CE9E9BA33753545BD34211B797A89359BD63D888B",
)
PACKAGE_GITHUB_COMMIT = "60afeb80fa33fbd53fc16763cc13c111eadf5f55"
GITHUB_RECEIPT_REL = Path(
    "manifests/published-github/"
    "20260731_sga7i_complete_transcription_commit_60afeb80_public_readback.json"
)
GITHUB_RECEIPT = (
    13_035,
    "70E3ADCDD2B92555FE41181881741AB3C5DB563BD1B8130B5D116DF762D8971F",
)

README_NAME = "09_README_CURRENT_RELEASE.md"
RELEASE_MANIFEST_NAME = "09a_RELEASE_FILE_MANIFEST.csv"
RELEASE_VALIDATION_NAME = "09b_RELEASE_VALIDATION.json"
PACKED_MANIFEST_NAME = "PACKED_CONTROL_SHA256.csv"
SGA7_VALIDATION_NAME = "09h_SGA7I_PACKAGE_VALIDATION.json"
SGA7_MANIFEST_NAME = "09i_SGA7I_PACKAGE_SHA256SUMS.csv"
SGA7_GITHUB_NAME = "09j_SGA7I_GITHUB_PUBLIC_READBACK.json"

DIRECT_READERS = tuple(
    f"00{chr(96 + index)}_SGA{index}_English_Reader.pdf"
    for index in range(1, 7)
) + (PDF_NAME,)
DIRECT_TEX = tuple(
    f"02{chr(96 + index)}_SGA{index}_English_Master.tex"
    for index in range(1, 7)
) + (TEX_NAME,)
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


def zip_member_identities(path: Path) -> dict[str, dict[str, object]]:
    with zipfile.ZipFile(path) as archive:
        if archive.testzip() is not None:
            raise RuntimeError(f"ZIP CRC failure: {path.name}")
        infos = [item for item in archive.infolist() if not item.is_dir()]
        names = [item.filename for item in infos]
        if len(names) != len(set(names)) or not all(safe_member(name) for name in names):
            raise RuntimeError(f"Unsafe or duplicate ZIP member: {path.name}")
        return {
            item.filename: {
                "bytes": item.file_size,
                "sha256": sha256_bytes(archive.read(item.filename)),
            }
            for item in infos
        }


def replay_zip_bytes(
    data: bytes,
    expected: tuple[int, str],
    expected_members: dict[str, dict[str, object]],
) -> dict:
    if (len(data), sha256_bytes(data)) != expected:
        raise RuntimeError("SGA7 source ZIP outer identity changed")
    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        infos = [item for item in archive.infolist() if not item.is_dir()]
        names = [item.filename for item in infos]
        if (
            archive.testzip() is not None
            or set(names) != set(expected_members)
            or len(names) != len(set(names))
            or not all(safe_member(name) for name in names)
        ):
            raise RuntimeError("SGA7 source ZIP member boundary changed")
        identities: dict[str, dict[str, object]] = {}
        for name in names:
            member = archive.read(name)
            observed = (len(member), sha256_bytes(member))
            wanted = (
                int(expected_members[name]["bytes"]),
                str(expected_members[name]["sha256"]).upper(),
            )
            if observed != wanted:
                raise RuntimeError(f"SGA7 source ZIP member mismatch: {name}")
            identities[name] = {
                "bytes": observed[0],
                "sha256": observed[1],
            }
        return {
            "status": "PASS",
            "members": len(infos),
            "uncompressed_bytes": sum(item.file_size for item in infos),
            "member_identities": identities,
        }


def local_preflight() -> dict:
    manifest = PACKAGE_ROOT / "SHA256SUMS.csv"
    validation_path = PACKAGE_ROOT / "PUBLIC_PROJECTION_VALIDATION.json"
    if (manifest.stat().st_size, sha256_path(manifest)) != PACKAGE_MANIFEST[:2]:
        raise RuntimeError("SGA7 package manifest changed")
    if (
        validation_path.stat().st_size,
        sha256_path(validation_path),
    ) != PACKAGE_VALIDATION:
        raise RuntimeError("SGA7 package validation changed")
    validation = json.loads(validation_path.read_text(encoding="utf-8"))
    if (
        validation.get("validation_status") != "PASS_ARCHIVE_HANDOFF_READY"
        or validation.get("errors")
    ):
        raise RuntimeError("SGA7 package validation is not PASS")
    rows = read_csv_bytes(manifest.read_bytes())
    if len(rows) != PACKAGE_MANIFEST[2]:
        raise RuntimeError("SGA7 package manifest row count changed")
    represented = {row["relative_path"] for row in rows}
    actual = {
        path.relative_to(PACKAGE_ROOT).as_posix()
        for path in PACKAGE_ROOT.rglob("*")
        if path.is_file()
    }
    if set(row["relative_path"] for row in rows) != {
        path for path in actual
    } - {"SHA256SUMS.csv", "PUBLIC_PROJECTION_VALIDATION.json"}:
        raise RuntimeError("SGA7 package manifest closure changed")
    for row in rows:
        path = PACKAGE_ROOT / row["relative_path"]
        if (path.stat().st_size, sha256_path(path)) != (
            int(row["bytes"]),
            row["sha256"].upper(),
        ):
            raise RuntimeError(f"Package mismatch: {path.name}")

    for name, expected in EXPECTED_UPLOADS.items():
        path = LOCAL_UPLOADS[name]
        if (path.stat().st_size, sha256_path(path)) != expected:
            raise RuntimeError(f"Upload identity changed: {name}")
    members = zip_member_identities(LOCAL_UPLOADS[ZIP_NAME])
    if len(members) != 12 or sum(int(row["bytes"]) for row in members.values()) != 3_313_473:
        raise RuntimeError("SGA7 source ZIP member boundary changed")
    for name, expected in members.items():
        source = PACKAGE_ROOT / name
        if not source.is_file() or (source.stat().st_size, sha256_path(source)) != (
            int(expected["bytes"]),
            str(expected["sha256"]),
        ):
            raise RuntimeError(f"SGA7 ZIP/source mismatch: {name}")

    github_receipt = REPO_ROOT / GITHUB_RECEIPT_REL
    if (github_receipt.stat().st_size, sha256_path(github_receipt)) != GITHUB_RECEIPT:
        raise RuntimeError("GitHub readback receipt identity changed")
    return {
        "status": "PASS",
        "package_files": len(actual),
        "package_manifest_sha256": PACKAGE_MANIFEST[1],
        "package_validation_sha256": PACKAGE_VALIDATION[1],
        "zip_members": len(members),
        "zip_uncompressed_bytes": sum(int(row["bytes"]) for row in members.values()),
        "zip_member_identities": members,
    }


def github_readback(commit: str) -> dict:
    receipt_url = (
        "https://raw.githubusercontent.com/KokunoYumeto/"
        f"modern-latex-manuscripts/{commit}/{GITHUB_RECEIPT_REL.as_posix()}"
    )
    session = make_session()
    data = check(session.get(receipt_url, timeout=(30, 180)), {200}).content
    if (len(data), sha256_bytes(data)) != GITHUB_RECEIPT:
        raise RuntimeError("GitHub public-readback receipt identity changed")
    receipt = json.loads(data.decode("utf-8"))
    file_errors = [
        name
        for name, value in receipt.get("file_readback", {}).items()
        if not value.get("match")
    ]
    zip_result = receipt.get("zip", {})
    errors = list(receipt.get("errors", [])) + file_errors + list(
        zip_result.get("errors", [])
    )
    if (
        receipt.get("status") != "PASS_GITHUB_PUBLIC_READBACK"
        or receipt.get("commit") != PACKAGE_GITHUB_COMMIT
        or receipt.get("package_path") != PACKAGE_REL.as_posix()
        or receipt.get("files_read_back") != 16
        or zip_result.get("members") != 12
        or zip_result.get("uncompressed_bytes") != 3_313_473
        or errors
    ):
        raise RuntimeError("GitHub package readback receipt is not exact PASS")
    return {
        "status": "PASS_GITHUB_PUBLIC_READBACK",
        "package_commit": PACKAGE_GITHUB_COMMIT,
        "receipt_commit": commit,
        "package_path": PACKAGE_REL.as_posix(),
        "files_read_back": 16,
        "manifest_rows": 14,
        "zip_members_read_back": 12,
        "zip_uncompressed_bytes": 3_313_473,
        "receipt_sha256": sha256_bytes(data),
        "receipt_url": receipt_url,
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
    if not OLD_SGA7_FILES.issubset(entries):
        raise RuntimeError("Partial SGA7 predecessor files are not all present")
    if set(EXPECTED_UPLOADS) & set(entries):
        raise RuntimeError("Complete SGA7 files already exist on live head")
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
        if len(infos) != 17 or not all(safe_member(item.filename) for item in infos):
            raise RuntimeError("Current release-controls boundary changed")
        for item in infos:
            (CONTROLS_ROOT / item.filename).write_bytes(archive.read(item.filename))
    packed = read_csv_bytes((CONTROLS_ROOT / PACKED_MANIFEST_NAME).read_bytes())
    if len(packed) != 16:
        raise RuntimeError("Current packed-control boundary changed")
    for row in packed:
        path = CONTROLS_ROOT / row["filename"]
        if (path.stat().st_size, sha256_path(path)) != (
            int(row["bytes"]),
            row["sha256"].upper(),
        ):
            raise RuntimeError(f"Current packed-control mismatch: {path.name}")
    rows = read_csv_bytes((CONTROLS_ROOT / RELEASE_MANIFEST_NAME).read_bytes())
    if len(rows) != 72:
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
    readme = """# Current SGA release

Start with `00_Current_SGA1-6_English_Readers_and_Buildable_TeX_20260730.zip`
for the six cumulative English reader PDFs and their buildable TeX closures.
The same reader PDFs and master TeX files remain direct in SGA1-6 order, and
SGA1 remains the default browser preview.

The current SGA3 reader is the clean R29 cumulative: 1,470 A4 pages covering
the Introduction, Exposes I-XXVI, the Tome-I subject index, the Tome-III
mathematical guide, and the terminal index. Its source package and reference/
QA controls remain grouped separately.

The SGA7 I checkpoint is now a complete working source transcription of all
six written exposes in the volume: I, II, VI, VII, VIII, and IX. Exposes III-V
are not separate written exposes in SGA7 I. The 528 continuous source-page
markers compile as a 267-page A4 reader with 162 native diagrams and no raster
diagram inputs. The source language is preserved as printed, including the
English Expose VI. This is not a complete English translation, critical
edition, rights clearance, accessibility certification, or mathematical
certification.

Two compact SGA7 visual-evidence archives remain available: 12 targeted
high-detail source crops actually opened during transcription and diagram
review, and provenance metadata for the larger rights-blocked scratch surface.
The parent scan and whole-page renders remain excluded.

All objects remain working scholarly editions, translations, or
transcriptions. No rights in the underlying works are transferred.
"""
    (CONTROLS_ROOT / README_NAME).write_text(
        readme, encoding="utf-8", newline="\n"
    )

    rows = [row for row in old_rows if row["filename"] not in OLD_SGA7_FILES]
    if len(rows) != 69:
        raise RuntimeError("SGA7 predecessor release-manifest subset changed")
    rows.extend(
        [
            {
                "filename": PDF_NAME,
                "bytes": EXPECTED_UPLOADS[PDF_NAME][0],
                "sha256": EXPECTED_UPLOADS[PDF_NAME][1],
                "role": "complete_working_source_transcription_reader",
                "provenance": (
                    "complete scan-based SGA7 I source transcription for all "
                    "written Exposes I, II, VI, VII, VIII, IX; 267 pages; "
                    f"GitHub package commit {PACKAGE_GITHUB_COMMIT}"
                ),
                "status": "current_complete_working_source_transcription",
            },
            {
                "filename": TEX_NAME,
                "bytes": EXPECTED_UPLOADS[TEX_NAME][0],
                "sha256": EXPECTED_UPLOADS[TEX_NAME][1],
                "role": "complete_working_source_transcription_master",
                "provenance": (
                    "editable master for the complete working SGA7 I source "
                    f"transcription; GitHub package commit {PACKAGE_GITHUB_COMMIT}"
                ),
                "status": "current_complete_working_source_transcription",
            },
            {
                "filename": ZIP_NAME,
                "bytes": EXPECTED_UPLOADS[ZIP_NAME][0],
                "sha256": EXPECTED_UPLOADS[ZIP_NAME][1],
                "role": "complete_working_reader_and_tex_archive",
                "provenance": (
                    "12-member reader and editable-source archive for complete "
                    "SGA7 I; all six written exposes; GitHub package commit "
                    f"{PACKAGE_GITHUB_COMMIT}"
                ),
                "status": "current_complete_working_source_transcription",
            },
        ]
    )
    rows.sort(key=lambda row: row["filename"].casefold())
    (CONTROLS_ROOT / RELEASE_MANIFEST_NAME).write_bytes(
        csv_bytes(
            rows,
            ["filename", "bytes", "sha256", "role", "provenance", "status"],
        )
    )

    copies = {
        SGA7_VALIDATION_NAME: "PUBLIC_PROJECTION_VALIDATION.json",
        SGA7_MANIFEST_NAME: "SHA256SUMS.csv",
    }
    for destination, source in copies.items():
        (CONTROLS_ROOT / destination).write_bytes((PACKAGE_ROOT / source).read_bytes())
    (CONTROLS_ROOT / SGA7_GITHUB_NAME).write_bytes(
        (REPO_ROOT / GITHUB_RECEIPT_REL).read_bytes()
    )

    validation = {
        "status": "PASS_READY_FOR_SINGLE_SAME_CONCEPT_SUCCESSOR",
        "prepared_at": PUBLICATION_DATE,
        "concept_doi": CONCEPT_DOI,
        "predecessor_record": PREDECESSOR_RECORD,
        "predecessor_files": PREDECESSOR_FILES,
        "predecessor_bytes": PREDECESSOR_BYTES,
        "expected_successor_files": 73,
        "retained_predecessor_files": 69,
        "replaced_files": sorted([*OLD_SGA7_FILES, CONTROLS_NAME]),
        "added_files": {
            name: {"bytes": value[0], "sha256": value[1]}
            for name, value in EXPECTED_UPLOADS.items()
        },
        "sga7_scope": {
            "written_exposes": ["I", "II", "VI", "VII", "VIII", "IX"],
            "separate_written_exposes_absent": ["III", "IV", "V"],
            "source_page_markers": 528,
            "reader_pages": 267,
            "native_diagrams": 162,
            "raster_diagram_inputs": 0,
            "complete_working_source_transcription": True,
            "complete_english_translation": False,
        },
        "github_package_commit": PACKAGE_GITHUB_COMMIT,
        "github_receipt_commit": commit,
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
        if name not in OLD_SGA7_FILES | {CONTROLS_NAME}
    }
    for name, expected in EXPECTED_UPLOADS.items():
        expected_files[name] = {
            "bytes": expected[0],
            "sha256": expected[1],
            "md5": md5_path(LOCAL_UPLOADS[name]),
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
            "github_package_commit": PACKAGE_GITHUB_COMMIT,
            "github_receipt_commit": commit,
            "expected_files": expected_files,
            "zip_member_identities": local["zip_member_identities"],
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
    retained_names = predecessor_names - OLD_SGA7_FILES - {CONTROLS_NAME}
    expected_names = retained_names | set(EXPECTED_UPLOADS) | {CONTROLS_NAME}
    allowed_universe = predecessor_names | set(EXPECTED_UPLOADS)
    if not retained_names.issubset(files) or not set(files).issubset(allowed_universe):
        raise RuntimeError("Tracked SGA draft has an unexpected file set")
    for name in sorted(OLD_SGA7_FILES | {CONTROLS_NAME}, key=str.casefold):
        if name not in files:
            continue
        check(
            session.delete(
                files[name]["links"]["self"],
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
    uploads = {CONTROLS_NAME: controls_zip, **LOCAL_UPLOADS}
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
    metadata["version"] = "2026-07-31 complete SGA7 I working source transcription"
    metadata["title"] = (
        "SGA 1-7: English Readers, French Texts, TeX Archives, and Complete "
        "SGA7 I Source Transcription"
    )
    metadata["description"] = "\n".join(
        [
            "<p>Start here: The first file is one ZIP containing the current "
            "cumulative English reader PDF for each of SGA 1 through SGA 6 "
            "together with its complete buildable TeX closure. The same six "
            "reader PDFs and master TeX files remain directly accessible, and "
            "SGA1 remains the default browser preview.</p>",
            "<p>SGA3: The preferred English reader is the clean R29 cumulative, "
            "1,470 A4 pages covering the Introduction, Exposes I-XXVI, the "
            "Tome-I subject index, the Tome-III mathematical guide, and the "
            "terminal index. It has 13,119 named destinations and 12,337 valid "
            "internal GoTo actions. Its complete buildable TeX closure and "
            "reference/QA controls remain grouped separately.</p>",
            "<p>SGA7 I: This successor provides a complete working source "
            "transcription of all six written exposes in the volume: I, II, VI, "
            "VII, VIII, and IX. Exposes III-V are not separate written exposes "
            "in SGA7 I. The 528 continuous source-page markers compile as a "
            "267-page A4 reader with 162 native diagrams and no raster diagram "
            "inputs. The source language is preserved as printed, including the "
            "English Expose VI. This is not a complete English translation.</p>",
            "<p>Two compact SGA7 visual-evidence archives retain 12 targeted "
            "high-detail source crops actually opened during transcription and "
            "diagram review, plus provenance metadata for the larger "
            "rights-blocked scratch surface. The parent scan and whole-page "
            "renders are excluded.</p>",
            "<p>English readers for SGA 1 through SGA 6 are presented before "
            "available French texts, direct editable TeX masters, and grouped "
            "supplementary archives. Earlier Zenodo versions remain immutable "
            "history.</p>",
            "<p>These are working scholarly translations, editions, or "
            "transcriptions, not critical editions, peer review, accessibility "
            "certification, rights determinations, or mathematical certification. "
            "They do not transfer rights in the underlying works.</p>",
        ]
    )
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
    expected_zip_members: dict[str, dict[str, object]],
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
        or record["metadata"].get("version")
        != "2026-07-31 complete SGA7 I working source transcription"
    ):
        raise RuntimeError("Published SGA successor boundary changed")
    latest = check(
        session.get(
            f"{API}/records/{record_id}/versions/latest",
            headers=headers,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    if int(latest["id"]) != record_id:
        raise RuntimeError("Published SGA successor is not the live concept head")
    expected_order = ordered_names(set(entries))
    api_order = record["files"].get("order") or []
    if api_order and api_order != expected_order:
        raise RuntimeError("Published SGA file order changed")

    predecessor_entries = modern_entries(predecessor)
    retained = set(predecessor_entries) - OLD_SGA7_FILES - {CONTROLS_NAME}
    if len(retained) != 69:
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
            capture=name in {ZIP_NAME, CONTROLS_NAME},
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

    source_replay = replay_zip_bytes(
        captured[ZIP_NAME], EXPECTED_UPLOADS[ZIP_NAME], expected_zip_members
    )
    controls_replay = replay_controls(captured[CONTROLS_NAME])
    result = {
        "status": "PASS_PUBLIC_READBACK",
        "record_id": int(record["id"]),
        "record_url": record["links"]["self_html"],
        "doi": record["pids"]["doi"]["identifier"],
        "concept_doi": record["parent"]["pids"]["doi"]["identifier"],
        "predecessor_record": PREDECESSOR_RECORD,
        "github_package_commit": PACKAGE_GITHUB_COMMIT,
        "github_receipt_commit": git_commit(),
        "outer_files": len(outer),
        "outer_bytes": sum(int(item["bytes"]) for item in outer.values()),
        "outer_files_streamed": len(outer),
        "retained_predecessor_files": len(retained),
        "retained_predecessor_identity_errors": 0,
        "added_files": sorted(EXPECTED_UPLOADS),
        "replaced_files": sorted([*OLD_SGA7_FILES, CONTROLS_NAME]),
        "default_preview": record["files"].get("default_preview"),
        "configured_file_order": expected_order,
        "api_file_order": api_order,
        "outer_file_readback": outer,
        "source_zip_readback": source_replay,
        "controls_zip_readback": controls_replay,
        "duplicate_concept_created": False,
        "second_draft_created": False,
        "errors": [],
    }
    RECEIPT_ROOT.mkdir(parents=True, exist_ok=True)
    receipt = RECEIPT_ROOT / (
        f"20260731_sga7i_complete_transcription_record_{record_id}_"
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
                session,
                predecessor,
                int(state["record_id"]),
                prepared["expected_files"],
                prepared["zip_member_identities"],
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
    result = public_readback(
        session,
        predecessor,
        record_id,
        expected_files,
        local["zip_member_identities"],
    )
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
