#!/usr/bin/env python3
"""Publish and read back SGA7 I English through Expose VII Theorem 3.2.5."""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import json
import shutil
import subprocess
import time
import urllib.parse
import zipfile
from pathlib import Path, PurePosixPath

import publish_sga7i_english_i_ii_vi_complete_zenodo_20260731 as previous


base = previous.base
prior = previous.prior
API = previous.API
PUBLICATION_DATE = "2026-07-31"
CONCEPT_DOI = "10.5281/zenodo.20410947"
PREDECESSOR_RECORD = 21_725_940
PREDECESSOR_DOI = "10.5281/zenodo.21725940"
PREDECESSOR_FILES = 83
PREDECESSOR_BYTES = 676_623_431
FINAL_FILES = 83
DEFAULT_PREVIEW = "00a_SGA1_English_Reader.pdf"
CONTROLS_NAME = "10z_SGA_Current_Release_Controls_20260730.zip"
VERSION = "2026-07-31 SGA7 I English through Expose VII Theorem 3.2.5"

REPO_ROOT = Path(__file__).resolve().parents[1]
PACKAGE_REL = Path(
    "sources/sga/"
    "sga7i-english-source-first-working-i-ii-vi-vii-through-3-2-5-20260731"
)
PACKAGE_ROOT = REPO_ROOT / PACKAGE_REL
TEMP_ROOT = REPO_ROOT / "tmp/zenodo/sga7i-english-vii-3-2-5-20260731"
CONTROLS_ROOT = TEMP_ROOT / "release-controls"
CONTROLS_ZIP = TEMP_ROOT / CONTROLS_NAME
READBACK_ROOT = TEMP_ROOT / "public-readback"
STATE_PATH = TEMP_ROOT / "draft_state.json"
RECEIPT_ROOT = REPO_ROOT / "manifests/published-zenodo"
RECEIPT_TAG = "20260731_sga7i_english_i_ii_vi_vii_3_2_5"
PREDECESSOR_RECEIPT = RECEIPT_ROOT / (
    "20260731_sga7i_english_i_ii_vi_complete_"
    "record_21725940_public_readback.json"
)
GITHUB_PACKAGE_COMMIT = "0d295ed2581b99b35393572002876d395b5e1d08"

OLD_PDF_NAME = "00i_SGA7I_English_Working_I_II_VI_Complete_20260731.pdf"
OLD_TEX_NAME = "02i_SGA7I_English_Working_I_II_VI_Complete_20260731.tex"
OLD_SOURCE_ZIP_NAME = (
    "10i_SGA7I_English_Working_I_II_VI_Complete_"
    "Reader_and_TeX_20260731.zip"
)
PDF_NAME = (
    "00i_SGA7I_English_Working_I_II_VI_VII_Through_3_2_5_20260731.pdf"
)
TEX_NAME = (
    "02i_SGA7I_English_Working_I_II_VI_VII_Through_3_2_5_20260731.tex"
)
SOURCE_ZIP_NAME = (
    "10i_SGA7I_English_Working_I_II_VI_VII_Through_3_2_5_"
    "Reader_and_TeX_20260731.zip"
)
REPLACED_NAMES = {
    OLD_PDF_NAME,
    OLD_TEX_NAME,
    OLD_SOURCE_ZIP_NAME,
    CONTROLS_NAME,
}

EXPECTED_PACKAGE_FILES = 94
EXPECTED_PACKAGE_BYTES = 2_509_472
EXPECTED_MANIFEST = (
    11_997,
    "0BAF3F85B4D655A074EE3743C7BD4A73C4E071B92093D2F9E1C6FE712BBA9B08",
)
EXPECTED_VALIDATION = (
    4_775,
    "74BE47CA0E1571EAA85807EFB91F106C3199EE47031501279DBFC9420D9A1FF6",
)
EXPECTED_PDF = (
    1_001_560,
    "C9E86DFBC380303C1980F7C50C8DB13FBBDAA3417574FE65A3BCA210FBD88904",
)
EXPECTED_TEX = (
    7_078,
    "AA01789CA32BBD50AE46C28B59DD933F8687E4F0F94BEE60AB1A2D88B34427ED",
)
EXPECTED_SOURCE_ZIP = (
    1_066_097,
    "A68B7D027466D509C1344D2966E7D59D5C0C2EFFA06E9092E03410CF8F649008",
)

DESCRIPTION_ADDITION = (
    "<p><strong>Start here:</strong> the first ZIP contains the current cumulative "
    "English reader PDF and buildable TeX for each of SGA 1 through SGA 6. "
    "Those reader PDFs and master TeX files are also directly accessible; SGA1 "
    "remains the browser preview.</p>"
    "<p><strong>SGA3:</strong> the current cumulative English reader is the clean "
    "1,470-page R29 reader covering the Introduction, Exposes I-XXVI, and its "
    "indexes and guide. Its source and QA controls are grouped separately.</p>"
    "<p><strong>SGA7:</strong> the record includes the complete SGA7 I French "
    "working transcription, the current partial SGA7 II French transcription, "
    "and a 120-page SGA7 I English working reader containing complete Exposes "
    "I, II, and VI plus Expose VII through Theorem 3.2.5. The next English "
    "cursor is Expose VII Section 3.3, authority line 1246, scan index 197, "
    "source folio 186. The direct master and 91-member ZIP contain its exact 85 "
    "components.</p>"
    "<p>These are working scholarly translations, editions, or transcriptions, "
    "not critical editions, peer review, accessibility certification, rights "
    "determinations, or mathematical certification. They transfer no rights in "
    "the underlying works.</p>"
)
NOTES_ADDITION = (
    "<p>Reader PDFs contain mathematical text only. Build sources, provenance, "
    "and release controls are separate downloadable files.</p>"
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
        and not (len(name) > 1 and name[1] == ":")
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
        for info in infos:
            data = archive.read(info)
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


def package_files() -> list[Path]:
    return sorted(
        (path for path in PACKAGE_ROOT.rglob("*") if path.is_file()),
        key=lambda path: path.relative_to(PACKAGE_ROOT).as_posix().casefold(),
    )


def verify_package() -> dict[str, object]:
    files = package_files()
    if (
        len(files) != EXPECTED_PACKAGE_FILES
        or sum(path.stat().st_size for path in files) != EXPECTED_PACKAGE_BYTES
    ):
        raise RuntimeError("SGA7 I English package boundary changed")
    manifest = PACKAGE_ROOT / "SHA256SUMS.csv"
    validation_path = PACKAGE_ROOT / "PACKAGE_VALIDATION.json"
    if (manifest.stat().st_size, sha256_path(manifest)) != EXPECTED_MANIFEST:
        raise RuntimeError("SGA7 I English manifest changed")
    if (
        validation_path.stat().st_size,
        sha256_path(validation_path),
    ) != EXPECTED_VALIDATION:
        raise RuntimeError("SGA7 I English validation changed")
    validation = json.loads(validation_path.read_text(encoding="utf-8"))
    if validation.get("status") != "PASS_PUBLIC_WORKING_CHECKPOINT" or validation.get(
        "errors"
    ):
        raise RuntimeError("SGA7 I English package is not validated")
    rows = list(csv.DictReader(manifest.open("r", encoding="utf-8", newline="")))
    represented = {
        path.relative_to(PACKAGE_ROOT).as_posix(): path
        for path in files
        if path.name != "SHA256SUMS.csv"
    }
    if len(rows) != 93 or {row["path"] for row in rows} != set(represented):
        raise RuntimeError("SGA7 I English manifest closure changed")
    for row in rows:
        path = represented[row["path"]]
        if (path.stat().st_size, sha256_path(path)) != (
            int(row["bytes"]),
            row["sha256"].upper(),
        ):
            raise RuntimeError(f"SGA7 I English identity changed: {row['path']}")
    source_zip = PACKAGE_ROOT / SOURCE_ZIP_NAME.replace("10i_", "")
    if not source_zip.is_file():
        source_zip = PACKAGE_ROOT / (
            "SGA7I_English_SourceFirst_Working_I_II_VI_VII_Through_3_2_5_"
            "Reader_and_TeX_20260731.zip"
        )
    if (source_zip.stat().st_size, sha256_path(source_zip)) != EXPECTED_SOURCE_ZIP:
        raise RuntimeError("SGA7 I English source ZIP changed")
    inventory = zip_inventory(source_zip)
    if int(inventory["members"]) != 91:
        raise RuntimeError("SGA7 I English source ZIP boundary changed")
    with zipfile.ZipFile(source_zip) as archive:
        embedded_manifest = list(
            csv.DictReader(
                archive.read("ZIP_MEMBER_SHA256SUMS.csv")
                .decode("utf-8")
                .splitlines()
            )
        )
        if len(embedded_manifest) != 90:
            raise RuntimeError("SGA7 I English embedded manifest changed")
        for row in embedded_manifest:
            data = archive.read(row["path"])
            observed = (len(data), hashlib.sha256(data).hexdigest().upper())
            wanted = (int(row["bytes"]), row["sha256"].upper())
            if observed != wanted:
                raise RuntimeError(f"SGA7 I ZIP member changed: {row['path']}")
    return inventory


def local_uploads() -> dict[str, dict[str, object]]:
    inventory = verify_package()
    paths = {
        PDF_NAME: PACKAGE_ROOT
        / (
            "reader/SGA7I_English_SourceFirst_Working_I_II_VI_VII_"
            "Through_3_2_5_20260731.pdf"
        ),
        TEX_NAME: PACKAGE_ROOT
        / (
            "source/SGA7I_English_SourceFirst_Working_I_II_VI_VII_"
            "Through_3_2_5_20260731.tex"
        ),
        SOURCE_ZIP_NAME: PACKAGE_ROOT
        / (
            "SGA7I_English_SourceFirst_Working_I_II_VI_VII_Through_3_2_5_"
            "Reader_and_TeX_20260731.zip"
        ),
    }
    expected = {
        PDF_NAME: EXPECTED_PDF,
        TEX_NAME: EXPECTED_TEX,
        SOURCE_ZIP_NAME: EXPECTED_SOURCE_ZIP,
    }
    result: dict[str, dict[str, object]] = {}
    for name, path in paths.items():
        if (path.stat().st_size, sha256_path(path)) != expected[name]:
            raise RuntimeError(f"SGA7 I English upload identity changed: {name}")
        result[name] = {
            "path": path,
            "bytes": path.stat().st_size,
            "sha256": sha256_path(path),
            "md5": md5_path(path),
        }
    result[SOURCE_ZIP_NAME]["inventory"] = inventory
    return result


def load_predecessor() -> dict[str, object]:
    receipt = json.loads(PREDECESSOR_RECEIPT.read_text(encoding="utf-8"))
    if (
        receipt.get("status") != "PASS_PUBLIC_READBACK"
        or int(receipt.get("record_id", -1)) != PREDECESSOR_RECORD
        or receipt.get("doi") != PREDECESSOR_DOI
        or receipt.get("concept_doi") != CONCEPT_DOI
        or int(receipt.get("outer_files", -1)) != PREDECESSOR_FILES
        or int(receipt.get("outer_bytes", -1)) != PREDECESSOR_BYTES
        or len(receipt.get("outer_file_readback", {})) != PREDECESSOR_FILES
    ):
        raise RuntimeError("Controlling SGA predecessor receipt changed")
    return receipt


def expected_retained(predecessor: dict[str, object]) -> dict[str, dict[str, object]]:
    return {
        name: row
        for name, row in predecessor["outer_file_readback"].items()
        if name not in REPLACED_NAMES
    }


def verify_github() -> dict[str, object]:
    subprocess.check_call(
        ["git", "merge-base", "--is-ancestor", GITHUB_PACKAGE_COMMIT, "HEAD"],
        cwd=REPO_ROOT,
    )
    remote = subprocess.check_output(
        ["git", "ls-remote", "github-write", "refs/heads/main"],
        cwd=REPO_ROOT,
        text=True,
    ).split()[0]
    subprocess.check_call(
        ["git", "merge-base", "--is-ancestor", GITHUB_PACKAGE_COMMIT, remote],
        cwd=REPO_ROOT,
    )
    session = base.make_session()
    url_root = (
        "https://raw.githubusercontent.com/KokunoYumeto/modern-latex-manuscripts/"
        f"{GITHUB_PACKAGE_COMMIT}/{PACKAGE_REL.as_posix()}"
    )
    readback: dict[str, dict[str, object]] = {}
    for path in package_files():
        relative = path.relative_to(PACKAGE_ROOT).as_posix()
        url = f"{url_root}/{urllib.parse.quote(relative, safe='/')}"
        data = base.check(session.get(url, timeout=(30, 300)), {200}).content
        observed = (len(data), hashlib.sha256(data).hexdigest().upper())
        wanted = (path.stat().st_size, sha256_path(path))
        if observed != wanted:
            raise RuntimeError(f"GitHub SGA7 I readback changed: {relative}")
        readback[relative] = {
            "bytes": observed[0],
            "sha256": observed[1],
            "url": url,
            "match": True,
        }
    return {
        "status": "PASS_GITHUB_PUBLIC_READBACK",
        "errors": [],
        "commit": GITHUB_PACKAGE_COMMIT,
        "public_main": remote,
        "package_path": PACKAGE_REL.as_posix(),
        "files_read_back": len(readback),
        "bytes_read_back": sum(int(row["bytes"]) for row in readback.values()),
        "file_readback": readback,
    }


def write_csv(path: Path, rows: list[dict[str, object]], fields: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def build_controls(
    local: dict[str, dict[str, object]],
    predecessor: dict[str, object],
    github: dict[str, object],
) -> dict[str, object]:
    shutil.rmtree(CONTROLS_ROOT, ignore_errors=True)
    CONTROLS_ROOT.mkdir(parents=True, exist_ok=True)
    retained = expected_retained(predecessor)
    (CONTROLS_ROOT / "09_README_CURRENT_RELEASE.md").write_text(
        """# Current SGA release controls

The cumulative English readers remain first and SGA1 remains the browser
preview. This successor adds a bounded SGA7 I English reader containing
complete Exposes I, II, and VI plus Expose VII through Theorem 3.2.5.

The exact continuation is Expose VII Section 3.3 at authority line 1246,
zero-based scan index 197, source folio 186. Expose VII after that point and
Exposes VIII-IX are absent.
The reader is current-progress source-aligned English, not a complete SGA7 I
volume, critical edition, peer review, accessibility certification, or
rights-clearance decision.
""",
        encoding="utf-8",
        newline="\n",
    )
    roles = {
        PDF_NAME: "direct_bounded_english_reader",
        TEX_NAME: "direct_editable_master",
        SOURCE_ZIP_NAME: "reader_and_buildable_tex_archive",
    }
    rows = [
        {
            "filename": name,
            "bytes": int(row["bytes"]),
            "sha256": str(row["sha256"]).upper(),
            "release_role": "retained_predecessor_file",
            "source": f"zenodo_record_{PREDECESSOR_RECORD}",
        }
        for name, row in retained.items()
    ]
    for name, row in local.items():
        rows.append(
            {
                "filename": name,
                "bytes": int(row["bytes"]),
                "sha256": str(row["sha256"]),
                "release_role": roles[name],
                "source": PACKAGE_REL.as_posix(),
            }
        )
    rows.sort(key=lambda row: str(row["filename"]).casefold())
    write_csv(
        CONTROLS_ROOT / "09a_RELEASE_FILE_MANIFEST.csv",
        rows,
        ["filename", "bytes", "sha256", "release_role", "source"],
    )
    base.save_json(
        CONTROLS_ROOT / "09b_RELEASE_VALIDATION.json",
        {
            "status": "PASS_PREPARED_RELEASE_CONTROLS",
            "errors": [],
            "concept_doi": CONCEPT_DOI,
            "predecessor_record": PREDECESSOR_RECORD,
            "retained_predecessor_files": len(retained),
            "added_files": len(local),
            "replaced_files": sorted(REPLACED_NAMES),
            "expected_outer_files_including_controls": FINAL_FILES,
            "default_preview": DEFAULT_PREVIEW,
            "github": {
                "commit": github["commit"],
                "package_path": github["package_path"],
                "files_read_back": github["files_read_back"],
            },
            "reader_pages": 120,
            "editable_tex_files": 86,
            "continuation": {
                "unit": "Expose VII Section 3.3",
                "authority_line": 1246,
                "scan_index_zero_based": 197,
                "source_folio": 186,
            },
            "source_zip_members": 91,
            "complete_sga7i_claim": False,
            "reader_process_preface_pages": 0,
        },
    )
    shutil.copyfile(
        PACKAGE_ROOT / "PACKAGE_VALIDATION.json",
        CONTROLS_ROOT / "09c_SGA7I_PACKAGE_VALIDATION.json",
    )
    shutil.copyfile(
        PACKAGE_ROOT / "SHA256SUMS.csv",
        CONTROLS_ROOT / "09d_SGA7I_PACKAGE_SHA256SUMS.csv",
    )
    base.save_json(
        CONTROLS_ROOT / "09e_SGA7I_GITHUB_PUBLIC_READBACK.json", github
    )
    inventory = local[SOURCE_ZIP_NAME]["inventory"]
    base.save_json(
        CONTROLS_ROOT / "09f_SGA7I_SOURCE_ZIP_VALIDATION.json",
        {
            "status": "PASS",
            "errors": [],
            "filename": SOURCE_ZIP_NAME,
            "bytes": inventory["bytes"],
            "sha256": inventory["sha256"],
            "members": inventory["members"],
            "uncompressed_bytes": inventory["uncompressed_bytes"],
            "member_readback": "91/91 exact",
        },
    )
    packed = [
        {
            "filename": path.name,
            "bytes": path.stat().st_size,
            "sha256": sha256_path(path),
        }
        for path in sorted(CONTROLS_ROOT.iterdir(), key=lambda p: p.name.casefold())
    ]
    write_csv(
        CONTROLS_ROOT / "PACKED_CONTROL_SHA256.csv",
        packed,
        ["filename", "bytes", "sha256"],
    )
    CONTROLS_ZIP.parent.mkdir(parents=True, exist_ok=True)
    CONTROLS_ZIP.unlink(missing_ok=True)
    with zipfile.ZipFile(
        CONTROLS_ZIP,
        "w",
        compression=zipfile.ZIP_DEFLATED,
        compresslevel=9,
        allowZip64=True,
    ) as archive:
        for path in sorted(CONTROLS_ROOT.iterdir(), key=lambda p: p.name.casefold()):
            info = zipfile.ZipInfo(path.name, date_time=(2026, 7, 31, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            info.create_system = 3
            archive.writestr(info, path.read_bytes(), compresslevel=9)
    controls_inventory = zip_inventory(CONTROLS_ZIP)
    if int(controls_inventory["members"]) != len(packed) + 1:
        raise RuntimeError("Release-control ZIP boundary changed")
    return {
        "path": CONTROLS_ZIP,
        "bytes": CONTROLS_ZIP.stat().st_size,
        "sha256": sha256_path(CONTROLS_ZIP),
        "md5": md5_path(CONTROLS_ZIP),
        "inventory": controls_inventory,
    }


def ordered_names(names: set[str]) -> list[str]:
    bundle = "00_Current_SGA1-6_English_Readers_and_Buildable_TeX_20260730.zip"
    english_readers = [
        f"00{chr(96 + index)}_SGA{index}_English_Reader.pdf"
        for index in range(1, 7)
    ] + [PDF_NAME]
    french_sga7 = [
        "00g_SGA7I_Fresh_Source_Transcription_Complete_Working.pdf",
        "00h_SGA7II_French_Source_Transcription_Working_X-XXI_Partial_20260731.pdf",
    ]
    english_tex = [
        f"02{chr(96 + index)}_SGA{index}_English_Master.tex"
        for index in range(1, 7)
    ] + [TEX_NAME]
    french_sga7_tex = [
        "02g_SGA7I_Fresh_Source_Transcription_Complete_Working.tex",
        "02h_SGA7II_French_Source_Transcription_Working_X-XXI_Partial_20260731.tex",
    ]
    preferred = [bundle, *english_readers, *french_sga7, *english_tex, *french_sga7_tex]
    if not set(preferred).issubset(names):
        missing = sorted(set(preferred) - names)
        raise RuntimeError(f"Direct SGA reader/source surface changed: {missing}")
    remainder = names - set(preferred)
    other_pdfs = sorted(
        (name for name in remainder if name.lower().endswith(".pdf")),
        key=str.casefold,
    )
    other_tex = sorted(
        (name for name in remainder if name.lower().endswith(".tex")),
        key=str.casefold,
    )
    archival = sorted(remainder - set(other_pdfs) - set(other_tex), key=str.casefold)
    return [*preferred, *other_pdfs, *other_tex, *archival]


def configure_prior() -> None:
    prior.PUBLICATION_DATE = PUBLICATION_DATE
    prior.CONCEPT_DOI = CONCEPT_DOI
    prior.PREDECESSOR_RECORD = PREDECESSOR_RECORD
    prior.PREDECESSOR_DOI = PREDECESSOR_DOI
    prior.PREDECESSOR_FILES = PREDECESSOR_FILES
    prior.PREDECESSOR_BYTES = PREDECESSOR_BYTES
    prior.FINAL_FILES = FINAL_FILES
    prior.DEFAULT_PREVIEW = DEFAULT_PREVIEW
    prior.CONTROLS_NAME = CONTROLS_NAME
    prior.VERSION = VERSION
    prior.TEMP_ROOT = TEMP_ROOT
    prior.CONTROLS_ROOT = CONTROLS_ROOT
    prior.CONTROLS_ZIP = CONTROLS_ZIP
    prior.READBACK_ROOT = READBACK_ROOT
    prior.STATE_PATH = STATE_PATH
    prior.RECEIPT_ROOT = RECEIPT_ROOT
    prior.RECEIPT_TAG = RECEIPT_TAG
    prior.PREDECESSOR_RECEIPT = PREDECESSOR_RECEIPT
    prior.REPLACED_NAMES = REPLACED_NAMES
    prior.OLD_DESCRIPTION_ADDITION = ""
    prior.OLD_NOTES_ADDITION = NOTES_ADDITION
    prior.DESCRIPTION_ADDITION = DESCRIPTION_ADDITION
    prior.NOTES_ADDITION = NOTES_ADDITION
    prior.PDF_NAME = PDF_NAME
    prior.TEX_NAME = TEX_NAME
    prior.SOURCE_ZIP_NAME = SOURCE_ZIP_NAME
    prior.expected_retained = expected_retained
    prior.ordered_names = ordered_names


def ensure_subject(session, token: str, draft_id: int) -> None:
    headers = prior.auth_headers(token)
    draft = base.check(
        session.get(
            f"{API}/records/{draft_id}/draft?expand=true",
            headers=headers,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    metadata = copy.deepcopy(draft["metadata"])
    metadata["description"] = DESCRIPTION_ADDITION
    metadata["additional_descriptions"] = [
        row
        for row in metadata.get("additional_descriptions", [])
        if row.get("type", {}).get("id") != "notes"
    ] + [
        {
            "description": NOTES_ADDITION,
            "type": {"id": "notes", "title": {"en": "Notes"}},
        }
    ]
    subjects = metadata.setdefault("subjects", [])
    if "SGA7 I English translation" not in {row.get("subject") for row in subjects}:
        subjects.append({"subject": "SGA7 I English translation"})
    payload = {
        "access": draft["access"],
        "files": {
            "enabled": True,
            "default_preview": draft["files"].get("default_preview"),
            "order": draft["files"].get("order", []),
        },
        "metadata": metadata,
        "custom_fields": draft.get("custom_fields", {}),
    }
    if draft.get("pids"):
        payload["pids"] = draft["pids"]
    base.check(
        session.put(
            f"{API}/records/{draft_id}/draft",
            headers={**headers, "Content-Type": "application/json"},
            json=payload,
            timeout=(30, 300),
        ),
        {200},
    )


def public_readback(
    session,
    token: str,
    record_id: int,
    local: dict[str, dict[str, object]],
    controls: dict[str, object],
    predecessor: dict[str, object],
    github: dict[str, object],
) -> dict[str, object]:
    record = None
    for _ in range(120):
        response = session.get(
            f"{API}/records/{record_id}?expand=true",
            headers=prior.public_headers(),
            timeout=(30, 180),
        )
        if response.status_code == 200:
            record = response.json()
            if record.get("is_published"):
                break
        time.sleep(2)
    if record is None or not record.get("is_published"):
        raise RuntimeError("Published SGA successor did not become public")
    retained = expected_retained(predecessor)
    expected = {**retained, **local, CONTROLS_NAME: controls}
    entries = base.modern_entries(record)
    latest = base.check(
        session.get(
            f"{API}/records/{PREDECESSOR_RECORD}/versions/latest?expand=true",
            headers=prior.public_headers(),
            timeout=(30, 180),
        ),
        {200},
    ).json()
    if (
        set(entries) != set(expected)
        or len(entries) != FINAL_FILES
        or record["parent"]["pids"]["doi"]["identifier"] != CONCEPT_DOI
        or record["files"].get("default_preview") != DEFAULT_PREVIEW
        or int(latest["id"]) != record_id
    ):
        raise RuntimeError("Public SGA successor boundary changed")
    description = record.get("metadata", {}).get("description", "").strip()
    notes = [
        row.get("description", "")
        for row in record.get("metadata", {}).get("additional_descriptions", [])
        if row.get("type", {}).get("id") == "notes"
    ]
    if description != DESCRIPTION_ADDITION or notes != [NOTES_ADDITION]:
        raise RuntimeError("Public SGA reader-first metadata changed")
    shutil.rmtree(READBACK_ROOT, ignore_errors=True)
    READBACK_ROOT.mkdir(parents=True)
    files: dict[str, dict[str, object]] = {}
    archives: dict[str, dict[str, object]] = {}
    try:
        for index, name in enumerate(sorted(entries, key=str.casefold), start=1):
            print(f"PUBLIC READBACK {index}/{len(entries)} {name}", flush=True)
            destination = (
                READBACK_ROOT / f"archive-{index:03d}.zip"
                if name in {SOURCE_ZIP_NAME, CONTROLS_NAME}
                else None
            )
            observed = prior.stream_download(
                session, entries[name]["links"]["content"], destination
            )
            wanted = (
                int(expected[name]["bytes"]),
                str(expected[name]["sha256"]).upper(),
                str(expected[name]["md5"]).lower(),
            )
            if observed != wanted:
                raise RuntimeError(f"Public SGA mismatch: {name}")
            files[name] = {
                "bytes": observed[0],
                "sha256": observed[1],
                "md5": observed[2],
                "content_url": entries[name]["links"]["content"],
                "match": True,
                "readback_mode": "anonymous_full_download_exact_sha256",
            }
            if destination is not None:
                inventory = zip_inventory(destination)
                if (
                    inventory["member_identities"]
                    != expected[name]["inventory"]["member_identities"]
                ):
                    raise RuntimeError(f"Public ZIP member drift: {name}")
                inventory["match"] = True
                archives[name] = inventory
    finally:
        shutil.rmtree(READBACK_ROOT, ignore_errors=True)
    retained_errors = [
        name
        for name in retained
        if files[name]["sha256"] != str(retained[name]["sha256"]).upper()
    ]
    if (
        len(files) != FINAL_FILES
        or retained_errors
        or int(archives[SOURCE_ZIP_NAME]["members"]) != 91
    ):
        raise RuntimeError("SGA public readback did not close")
    prior.assert_no_open_draft(session, token, record_id)
    result = {
        "status": "PASS_PUBLIC_READBACK",
        "errors": [],
        "record_id": record_id,
        "record_url": record["links"]["self_html"],
        "doi": record["pids"]["doi"]["identifier"],
        "concept_doi": CONCEPT_DOI,
        "predecessor_record": PREDECESSOR_RECORD,
        "version": VERSION,
        "outer_files": len(files),
        "outer_bytes": sum(int(row["bytes"]) for row in files.values()),
        "outer_file_readback": files,
        "retained_predecessor_files": len(retained),
        "retained_predecessor_identity_errors": retained_errors,
        "replaced_files": sorted(REPLACED_NAMES),
        "added_files": sorted(local),
        "default_preview": record["files"].get("default_preview"),
        "latest_record": int(latest["id"]),
        "github": github,
        "source_zip_members": 91,
        "continuation": {
            "unit": "Expose VII Section 3.3",
            "authority_line": 1246,
            "scan_index_zero_based": 197,
            "source_folio": 186,
        },
        "reader_first_metadata": True,
        "description_bytes": len(DESCRIPTION_ADDITION.encode("utf-8")),
        "notes_rows": len(notes),
        "complete_sga7i_claim": False,
        "duplicate_concept_created": False,
        "active_draft_remaining": False,
    }
    zip_result = {
        "status": "PASS",
        "errors": [],
        "record_id": record_id,
        "doi": result["doi"],
        "zip_archive_count": len(archives),
        "zip_member_count": sum(int(row["members"]) for row in archives.values()),
        "archives": archives,
    }
    base.save_json(
        RECEIPT_ROOT / f"{RECEIPT_TAG}_record_{record_id}_public_readback.json",
        result,
    )
    base.save_json(
        RECEIPT_ROOT / f"{RECEIPT_TAG}_record_{record_id}_zip_member_readback.json",
        zip_result,
    )
    (RECEIPT_ROOT / f"{RECEIPT_TAG}_record_{record_id}.md").write_text(
        "\n".join(
            [
                "# SGA7 I English through Expose VII Theorem 3.2.5 publication receipt",
                "",
                f"- Record: <https://zenodo.org/records/{record_id}>",
                f"- DOI: `{result['doi']}`",
                f"- Concept DOI: `{CONCEPT_DOI}`",
                f"- GitHub package commit: `{GITHUB_PACKAGE_COMMIT}`",
                f"- Public files: {len(files)} / {result['outer_bytes']:,} bytes",
                f"- Retained predecessor files: {len(retained)} / identity errors 0",
                f"- Reader SHA-256: `{EXPECTED_PDF[1]}`",
                f"- Reader/source ZIP: 91 members / `{EXPECTED_SOURCE_ZIP[1]}`",
                "- Scope: Exposes I, II, and VI complete; Expose VII through Theorem 3.2.5",
                "- Continuation: Expose VII Section 3.3 / authority line 1246 / scan index 197 / source folio 186",
                "- Landing metadata: concise reader-first description / one short note",
                f"- Default preview: `{DEFAULT_PREVIEW}`",
                "- Duplicate concept created: no",
                "- Active draft remaining: no",
                "",
            ]
        ),
        encoding="utf-8",
        newline="\n",
    )
    return result


def prepare() -> tuple[
    dict[str, dict[str, object]],
    dict[str, object],
    dict[str, object],
    dict[str, object],
]:
    configure_prior()
    local = local_uploads()
    predecessor = load_predecessor()
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
        "status": "PASS_PREFLIGHT",
        "predecessor_record": PREDECESSOR_RECORD,
        "concept_doi": CONCEPT_DOI,
        "retained_files": len(expected_retained(predecessor)),
        "replaced_files": sorted(REPLACED_NAMES),
        "added_files": sorted(local),
        "final_files": FINAL_FILES,
        "default_preview": DEFAULT_PREVIEW,
        "github_commit": github["commit"],
        "uploads": {
            name: {"bytes": row["bytes"], "sha256": row["sha256"]}
            for name, row in local.items()
        },
        "controls_zip": {
            "bytes": controls["bytes"],
            "sha256": controls["sha256"],
            "members": controls["inventory"]["members"],
        },
        "duplicate_concept_created": False,
    }


def resumable_predecessor(
    session,
    token: str,
    draft_id: int,
    predecessor: dict[str, object],
    local: dict[str, dict[str, object]],
    controls: dict[str, object],
) -> dict[str, object]:
    """Describe the one tracked draft as a safe resume base after interruption."""
    deposition = base.check(
        session.get(
            f"{API}/deposit/depositions/{draft_id}",
            headers={"Authorization": f"Bearer {token}"},
            timeout=(30, 180),
        ),
        {200},
    ).json()
    names = set(base.legacy_entries(deposition))
    original = predecessor["outer_file_readback"]
    retained = expected_retained(predecessor)
    permitted = set(original) | set(local) | {CONTROLS_NAME}
    if not set(retained).issubset(names) or not names.issubset(permitted):
        raise RuntimeError("Tracked SGA draft is not a resumable successor subset")
    rows: dict[str, dict[str, object]] = {}
    for name in names:
        if name in original:
            rows[name] = original[name]
        elif name in local:
            rows[name] = local[name]
        elif name == CONTROLS_NAME:
            rows[name] = controls
        else:
            raise RuntimeError(f"Unexpected tracked SGA draft file: {name}")
    shadow = copy.deepcopy(predecessor)
    shadow["outer_file_readback"] = rows
    return shadow


def publish() -> dict[str, object]:
    local, predecessor, github, controls = prepare()
    token = base.find_token()
    session = base.make_session()
    live = prior.fetch_live(session, predecessor)
    prior.assert_no_untracked_draft(session, token)
    draft_id = prior.create_or_resume_draft(session, token, live)
    ensure_subject(session, token, draft_id)
    stage_base = resumable_predecessor(
        session, token, draft_id, predecessor, local, controls
    )
    published = prior.stage_and_publish(
        session,
        token,
        live,
        draft_id,
        local,
        controls,
        stage_base,
    )
    return public_readback(
        session,
        token,
        int(published["id"]),
        local,
        controls,
        predecessor,
        github,
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--preflight", action="store_true")
    args = parser.parse_args()
    result = preflight() if args.preflight else publish()
    print(json.dumps(result, indent=2, ensure_ascii=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
