#!/usr/bin/env python3
"""Publish and read back the SGA7 II X-XXI partial source successor."""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import shutil
import subprocess
import time
import zipfile
from pathlib import Path, PurePosixPath

import publish_sga7ii_expose_xviii_boundary_crop_zenodo_20260731 as boundary
import publish_sga7ii_expose_xviii_wip_source_zenodo_20260731 as wip
import publish_sga7ii_x_xvii_source_images_zenodo_20260731 as prior


base = prior.base
API = prior.API
PUBLICATION_DATE = "2026-07-31"
CONCEPT_DOI = "10.5281/zenodo.20410947"
PREDECESSOR_RECORD = 21_720_340
PREDECESSOR_DOI = "10.5281/zenodo.21720340"
PREDECESSOR_FILES = 80
PREDECESSOR_BYTES = 671_216_941
FINAL_FILES = 80
DEFAULT_PREVIEW = "00a_SGA1_English_Reader.pdf"
CONTROLS_NAME = "10z_SGA_Current_Release_Controls_20260730.zip"
VERSION = "2026-07-31 SGA7 II working French transcription X-XXI partial"

REPO_ROOT = Path(__file__).resolve().parents[1]
PACKAGE_REL = Path(
    "sources/sga/"
    "sga7ii-french-source-transcription-working-x-xxi-partial-20260731"
)
PACKAGE_ROOT = REPO_ROOT / PACKAGE_REL
TEMP_ROOT = REPO_ROOT / "tmp/zenodo/sga7ii-x-xxi-partial-20260731"
CONTROLS_ROOT = TEMP_ROOT / "release-controls"
CONTROLS_ZIP = TEMP_ROOT / CONTROLS_NAME
READBACK_ROOT = TEMP_ROOT / "public-readback"
STATE_PATH = TEMP_ROOT / "draft_state.json"
RECEIPT_ROOT = REPO_ROOT / "manifests/published-zenodo"
RECEIPT_TAG = "20260731_sga7ii_x_xxi_partial"
PREDECESSOR_RECEIPT = RECEIPT_ROOT / (
    "20260731_sga7ii_expose_xviii_boundary_crop_"
    "record_21720340_public_readback.json"
)
GITHUB_PACKAGE_COMMIT = "907fe2b4d6a2dd32eec114518dadb777de2ab053"

OLD_PDF_NAME = "00h_SGA7II_French_Source_Transcription_Working_X-XVII_20260731.pdf"
OLD_TEX_NAME = "02h_SGA7II_French_Source_Transcription_Working_X-XVII_20260731.tex"
OLD_SOURCE_ZIP_NAME = (
    "10g2_SGA7II_French_Source_Transcription_Working_X-XVII_"
    "Reader_Source_and_WIP_20260731.zip"
)
PDF_NAME = "00h_SGA7II_French_Source_Transcription_Working_X-XXI_Partial_20260731.pdf"
TEX_NAME = "02h_SGA7II_French_Source_Transcription_Working_X-XXI_Partial_20260731.tex"
SOURCE_ZIP_NAME = (
    "10g2_SGA7II_French_Source_Transcription_Working_X-XXI_Partial_"
    "Reader_Source_and_Evidence_20260731.zip"
)
SOURCE_ZIP = REPO_ROOT / "tmp/zenodo-upload-sga7ii-x-xxi" / SOURCE_ZIP_NAME
REPLACED_NAMES = {
    OLD_PDF_NAME,
    OLD_TEX_NAME,
    OLD_SOURCE_ZIP_NAME,
    CONTROLS_NAME,
}

EXPECTED_PACKAGE_FILES = 25
EXPECTED_PACKAGE_BYTES = 5_941_537
EXPECTED_MANIFEST = (
    3_325,
    "8757ECC1FA93C65C8189BC282F1F658F1DFC172B009228FCD55531003772327C",
)
EXPECTED_VALIDATION = (
    5_402,
    "94BC3C3D9FE61F5116DB0B332880AA00CA81D070E8A491A4E74F0FB84963DB40",
)
EXPECTED_PDF = (
    1_378_858,
    "6A4569194DBECC1475C46FE6896D01379C637603ABD6FB940B8DAB661EBE1646",
)
EXPECTED_TEX = (
    4_458,
    "E37D5E1FF74D0DE2B24C6CEA9A7E07EC3CF8135C36070D953B191158210EC071",
)
EXPECTED_SOURCE_ZIP = (
    4_614_750,
    "F3B0BB21B47C052F8A722854549E03768857C03715E81F12A0FE5960E9C63041",
)

STALE_DESCRIPTION_PARAGRAPHS = (
    prior.DESCRIPTION_ADDITION,
    wip.DESCRIPTION_ADDITION,
    boundary.DESCRIPTION_ADDITION,
)
STALE_NOTE_PARAGRAPHS = (
    prior.NOTES_ADDITION,
    wip.NOTES_ADDITION,
    boundary.NOTES_ADDITION,
)

DESCRIPTION_ADDITION = (
    "<p><strong>SGA7 II working French source transcription:</strong> this "
    "successor extends the direct reader through scan index 406: complete "
    "Exposes X-XX and the first 37 of 39 source pages of Expose XXI, in one "
    "201-page A4 reader. The editable master and a compact 25-member archive "
    "contain the twelve expose bodies, exact package controls, and five "
    "600-dpi authority-page witnesses used to settle formulas and a diagram. "
    "Indices 407-408 finish Expose XXI and 409-445 comprise Expose XXII; those "
    "39 pages remain absent. This is a partial working source transcription, "
    "not an English translation, complete SGA7 II volume, critical edition, "
    "or mathematical certification.</p>"
)
NOTES_ADDITION = (
    "<p>The SGA7 II X-XXI partial reader starts directly with the volume text "
    "and contains no project preface or workflow-status pages. Its 399 source "
    "markers are continuous from index 8 through 406. The four-pass build "
    "converged exactly; all 201 pages contain text, all 22 font resources are "
    "embedded, and five inherited Type 3 resources remain. SGA1 remains the "
    "default browser preview.</p>"
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
        raise RuntimeError("SGA7 II package boundary changed")
    manifest = PACKAGE_ROOT / "SHA256SUMS.csv"
    validation_path = PACKAGE_ROOT / "PACKAGE_VALIDATION.json"
    if (manifest.stat().st_size, sha256_path(manifest)) != EXPECTED_MANIFEST:
        raise RuntimeError("SGA7 II manifest changed")
    if (
        validation_path.stat().st_size,
        sha256_path(validation_path),
    ) != EXPECTED_VALIDATION:
        raise RuntimeError("SGA7 II package validation changed")
    validation = json.loads(validation_path.read_text(encoding="utf-8"))
    if validation.get("status") != "PASS_ARCHIVE_HANDOFF_READY" or validation.get("errors"):
        raise RuntimeError("SGA7 II package is not validated")
    rows = list(csv.DictReader(manifest.open("r", encoding="utf-8-sig", newline="")))
    represented = {
        path.relative_to(PACKAGE_ROOT).as_posix(): path
        for path in files
        if path.name != "SHA256SUMS.csv"
    }
    if len(rows) != 24 or {row["relative_path"] for row in rows} != set(represented):
        raise RuntimeError("SGA7 II manifest closure changed")
    for row in rows:
        path = represented[row["relative_path"]]
        if (path.stat().st_size, sha256_path(path)) != (
            int(row["bytes"]),
            row["sha256"].upper(),
        ):
            raise RuntimeError(f"SGA7 II identity changed: {row['relative_path']}")
    if (SOURCE_ZIP.stat().st_size, sha256_path(SOURCE_ZIP)) != EXPECTED_SOURCE_ZIP:
        raise RuntimeError("SGA7 II deterministic source ZIP changed")
    inventory = zip_inventory(SOURCE_ZIP)
    if int(inventory["members"]) != 25:
        raise RuntimeError("SGA7 II source ZIP member boundary changed")
    with zipfile.ZipFile(SOURCE_ZIP) as archive:
        for path in files:
            relative = path.relative_to(PACKAGE_ROOT).as_posix()
            if archive.read(relative) != path.read_bytes():
                raise RuntimeError(f"SGA7 II ZIP member changed: {relative}")
    return inventory


def local_uploads() -> dict[str, dict[str, object]]:
    inventory = verify_package()
    paths = {
        PDF_NAME: PACKAGE_ROOT
        / "reader/SGA7II_French_Source_Transcription_Working_X-XXI_Partial_20260731.pdf",
        TEX_NAME: PACKAGE_ROOT
        / "source/SGA7II_French_Source_Transcription_Working_X-XXI_Partial_20260731.tex",
        SOURCE_ZIP_NAME: SOURCE_ZIP,
    }
    expected = {
        PDF_NAME: EXPECTED_PDF,
        TEX_NAME: EXPECTED_TEX,
        SOURCE_ZIP_NAME: EXPECTED_SOURCE_ZIP,
    }
    result: dict[str, dict[str, object]] = {}
    for name, path in paths.items():
        if (path.stat().st_size, sha256_path(path)) != expected[name]:
            raise RuntimeError(f"SGA7 II upload identity changed: {name}")
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
    if remote != GITHUB_PACKAGE_COMMIT:
        raise RuntimeError("SGA7 II GitHub commit is not current public main")
    session = base.make_session()
    url_root = (
        "https://raw.githubusercontent.com/KokunoYumeto/modern-latex-manuscripts/"
        f"{GITHUB_PACKAGE_COMMIT}/{PACKAGE_REL.as_posix()}"
    )
    manifest_data = base.check(
        session.get(f"{url_root}/SHA256SUMS.csv", timeout=(30, 180)), {200}
    ).content
    if hashlib.sha256(manifest_data).hexdigest().upper() != EXPECTED_MANIFEST[1]:
        raise RuntimeError("GitHub SGA7 II manifest readback changed")
    rows = list(csv.DictReader(io.StringIO(manifest_data.decode("utf-8-sig"))))
    readback: list[dict[str, object]] = []
    for row in rows:
        data = base.check(
            session.get(f"{url_root}/{row['relative_path']}", timeout=(30, 300)),
            {200},
        ).content
        observed = (len(data), hashlib.sha256(data).hexdigest().upper())
        wanted = (int(row["bytes"]), row["sha256"].upper())
        if observed != wanted:
            raise RuntimeError(f"GitHub SGA7 II readback changed: {row['relative_path']}")
        readback.append(
            {
                "relative_path": row["relative_path"],
                "bytes": observed[0],
                "sha256": observed[1],
                "url": f"{url_root}/{row['relative_path']}",
                "match": True,
            }
        )
    return {
        "status": "PASS_GITHUB_PUBLIC_READBACK",
        "commit": GITHUB_PACKAGE_COMMIT,
        "package_path": PACKAGE_REL.as_posix(),
        "files_read_back": len(readback) + 1,
        "represented_files_read_back": len(readback),
        "manifest_sha256": EXPECTED_MANIFEST[1],
        "file_readback": readback,
        "errors": [],
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
preview. This successor replaces only the SGA7 II direct PDF, editable master,
compact reader/source/evidence archive, and these release controls.

The SGA7 II reader covers continuous source indices 8-406: complete Exposes
X-XX and 37 of 39 pages of Expose XXI. Indices 407-445 remain absent. Five
600-dpi source leaves used for formula and diagram adjudication are included in
the compact archive. No complete-volume, English-translation, critical-edition,
accessibility, or mathematical-certification claim is made.
""",
        encoding="utf-8",
        newline="\n",
    )
    roles = {
        PDF_NAME: "direct_working_french_source_reader",
        TEX_NAME: "direct_editable_master",
        SOURCE_ZIP_NAME: "reader_source_controls_and_source_page_evidence",
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
            "replaced_files": sorted(REPLACED_NAMES),
            "expected_outer_files_including_controls": FINAL_FILES,
            "default_preview": DEFAULT_PREVIEW,
            "github": {
                "commit": github["commit"],
                "package_path": github["package_path"],
                "files_read_back": github["files_read_back"],
            },
            "reader_pages": 201,
            "source_marker_range": [8, 406],
            "source_marker_count": 399,
            "continuation_source_index": 407,
            "source_zip_members": 25,
            "source_page_evidence_files": 5,
            "reader_preface_or_status_pages": 0,
            "complete_sga7ii_claim": False,
        },
    )
    shutil.copyfile(
        PACKAGE_ROOT / "PACKAGE_VALIDATION.json",
        CONTROLS_ROOT / "09c_SGA7II_PACKAGE_VALIDATION.json",
    )
    shutil.copyfile(
        PACKAGE_ROOT / "SHA256SUMS.csv",
        CONTROLS_ROOT / "09d_SGA7II_PACKAGE_SHA256SUMS.csv",
    )
    base.save_json(
        CONTROLS_ROOT / "09e_SGA7II_GITHUB_PUBLIC_READBACK.json", github
    )
    source_inventory = local[SOURCE_ZIP_NAME]["inventory"]
    base.save_json(
        CONTROLS_ROOT / "09f_SGA7II_SOURCE_ZIP_VALIDATION.json",
        {
            "status": "PASS",
            "errors": [],
            "filename": SOURCE_ZIP_NAME,
            "bytes": source_inventory["bytes"],
            "sha256": source_inventory["sha256"],
            "members": source_inventory["members"],
            "uncompressed_bytes": source_inventory["uncompressed_bytes"],
            "member_readback": "25/25 exact",
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
    inventory = zip_inventory(CONTROLS_ZIP)
    if int(inventory["members"]) != len(packed) + 1:
        raise RuntimeError("Release-control ZIP boundary changed")
    return {
        "path": CONTROLS_ZIP,
        "bytes": CONTROLS_ZIP.stat().st_size,
        "sha256": sha256_path(CONTROLS_ZIP),
        "md5": md5_path(CONTROLS_ZIP),
        "inventory": inventory,
    }


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
    prior.OLD_DESCRIPTION_ADDITION = "<!-- metadata already consolidated -->"
    prior.OLD_NOTES_ADDITION = "<!-- metadata already consolidated -->"
    prior.DESCRIPTION_ADDITION = DESCRIPTION_ADDITION
    prior.NOTES_ADDITION = NOTES_ADDITION
    prior.PDF_NAME = PDF_NAME
    prior.TEX_NAME = TEX_NAME
    prior.SOURCE_ZIP_NAME = SOURCE_ZIP_NAME
    prior.expected_retained = expected_retained


def remove_stale_metadata(session, token: str, draft_id: int) -> None:
    headers = prior.auth_headers(token)
    draft = base.check(
        session.get(
            f"{API}/records/{draft_id}/draft?expand=true",
            headers=headers,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    metadata = draft["metadata"]
    description = metadata.get("description", "")
    for paragraph in STALE_DESCRIPTION_PARAGRAPHS:
        description = description.replace(paragraph, "")
    metadata["description"] = description
    additions = metadata.get("additional_descriptions", [])
    for row in additions:
        if row.get("type", {}).get("id") == "notes":
            text = row.get("description", "")
            for paragraph in STALE_NOTE_PARAGRAPHS:
                text = text.replace(paragraph, "")
            row["description"] = text
    metadata["additional_descriptions"] = additions
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
    cleaned = base.check(
        session.put(
            f"{API}/records/{draft_id}/draft",
            headers={**headers, "Content-Type": "application/json"},
            json=payload,
            timeout=(30, 300),
        ),
        {200},
    ).json()
    surface = cleaned["metadata"].get("description", "") + " ".join(
        row.get("description", "")
        for row in cleaned["metadata"].get("additional_descriptions", [])
    )
    if any(paragraph in surface for paragraph in (*STALE_DESCRIPTION_PARAGRAPHS, *STALE_NOTE_PARAGRAPHS)):
        raise RuntimeError("Stale SGA7 II metadata remains in draft")


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
                if inventory["member_identities"] != expected[name]["inventory"]["member_identities"]:
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
        or int(archives[SOURCE_ZIP_NAME]["members"]) != 25
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
        "default_preview": record["files"].get("default_preview"),
        "latest_record": int(latest["id"]),
        "github": github,
        "source_zip_members": 25,
        "source_marker_range": [8, 406],
        "source_marker_count": 399,
        "continuation_source_index": 407,
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
                "# SGA7 II X-XXI partial publication receipt",
                "",
                f"- Record: <https://zenodo.org/records/{record_id}>",
                f"- DOI: `{result['doi']}`",
                f"- Concept DOI: `{CONCEPT_DOI}`",
                f"- GitHub package commit: `{GITHUB_PACKAGE_COMMIT}`",
                f"- Public files: {len(files)} / {result['outer_bytes']:,} bytes",
                f"- Retained predecessor files: {len(retained)} / identity errors 0",
                f"- Replacement source ZIP: 25 members / `{EXPECTED_SOURCE_ZIP[1]}`",
                "- SGA7 II scope: continuous source indices 8-406; cursor 407",
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


def publish() -> dict[str, object]:
    local, predecessor, github, controls = prepare()
    token = base.find_token()
    session = base.make_session()
    live = prior.fetch_live(session, predecessor)
    prior.assert_no_untracked_draft(session, token)
    draft_id = prior.create_or_resume_draft(session, token, live)
    remove_stale_metadata(session, token, draft_id)
    published = prior.stage_and_publish(
        session,
        token,
        live,
        draft_id,
        local,
        controls,
        predecessor,
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
