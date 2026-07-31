#!/usr/bin/env python3
"""Add the Expose-XVIII boundary page and its actual source crop."""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import shutil
import subprocess
import zipfile
from pathlib import Path, PurePosixPath

import publish_sga7ii_x_xvii_source_images_zenodo_20260731 as prior


base = prior.base
API = prior.API
PUBLICATION_DATE = "2026-07-31"
CONCEPT_DOI = "10.5281/zenodo.20410947"
PREDECESSOR_RECORD = 21_719_787
PREDECESSOR_DOI = "10.5281/zenodo.21719787"
PREDECESSOR_FILES = 80
PREDECESSOR_BYTES = 671_043_852
FINAL_FILES = 80
DEFAULT_PREVIEW = "00a_SGA1_English_Reader.pdf"
CONTROLS_NAME = "10z_SGA_Current_Release_Controls_20260730.zip"
VERSION = "2026-07-31 SGA7 II Expose XVIII boundary source and crop custody"

REPO_ROOT = Path(__file__).resolve().parents[1]
PACKAGE_REL = Path(
    "sources/sga/"
    "sga7ii-french-source-transcription-working-x-xvii-recovered-20260731"
)
PACKAGE_ROOT = REPO_ROOT / PACKAGE_REL
SOURCE_ZIP_NAME = (
    "10g2_SGA7II_French_Source_Transcription_Working_X-XVII_"
    "Reader_Source_and_WIP_20260731.zip"
)
TEMP_ROOT = REPO_ROOT / "tmp/zenodo/sga7ii-xviii-boundary-crop-20260731"
SOURCE_ZIP = TEMP_ROOT / SOURCE_ZIP_NAME
CONTROLS_ROOT = TEMP_ROOT / "release-controls"
CONTROLS_ZIP = TEMP_ROOT / CONTROLS_NAME
READBACK_ROOT = TEMP_ROOT / "public-readback"
STATE_PATH = TEMP_ROOT / "draft_state.json"
RECEIPT_ROOT = REPO_ROOT / "manifests/published-zenodo"
RECEIPT_TAG = "20260731_sga7ii_expose_xviii_boundary_crop"
PREDECESSOR_RECEIPT = RECEIPT_ROOT / (
    "20260731_sga7i_postcutoff_source_crops_"
    "record_21719787_public_readback.json"
)
GITHUB_PACKAGE_COMMIT = "779cb87e9b452664cf61400fb4ff85a96ae09ecf"
GITHUB_RECEIPT_REL = Path(
    "manifests/published-github/"
    "20260731_sga7ii_expose_xviii_boundary_crop_"
    "commit_779cb87e9_public_readback.json"
)

EXPECTED_PACKAGE_FILES = 33
EXPECTED_PACKAGE_BYTES = 4_647_061
EXPECTED_PACKAGE_MANIFEST = (
    4_782,
    "05BD01937C1DA607D091FD217561C9E68E5B414273AEB679AD8C36570BB7243B",
)
EXPECTED_WIP = (
    115_701,
    "647AF97E3AD0EEEF307E3C88F6AD44851B7EA604CE6D42048426A13AF1C36D5B",
)
EXPECTED_SOURCE_ZIP = (
    1_303_331,
    "4749DCB2C82DBB98F30BCF24AAACE7A86674E044092746CDB96222E1427F443C",
)
SOURCE_MEMBERS = [
    "BUILD_SUMMARY_PUBLIC.md",
    "PACKAGE_VALIDATION.json",
    "PUBLICATION_READINESS.md",
    "reader/SGA7II_French_Source_Transcription_Working_X-XVII_20260731.pdf",
    "README.md",
    "RECOVERY_AND_SCOPE.md",
    "RIGHTS_AND_PROVENANCE.md",
    "source/expose_X_body.tex",
    "source/expose_XI_body.tex",
    "source/expose_XII_body.tex",
    "source/expose_XIII_body.tex",
    "source/expose_XIV_body.tex",
    "source/expose_XV_body.tex",
    "source/expose_XVI_body.tex",
    "source/expose_XVII_body.tex",
    "source/SGA7II_French_Source_Transcription_Working_X-XVII_20260731.tex",
    "work-in-progress/expose_XVIII_partial.tex",
    "work-in-progress/README.md",
    "visual-evidence/README.md",
    "visual-evidence/VISUAL_EVIDENCE_INDEX.csv",
    "visual-evidence/detail-crops/SGA7II_idx261_folio254_exposeXVIII_title_400dpi.png",
]
REPLACED_NAMES = {SOURCE_ZIP_NAME, CONTROLS_NAME}

DESCRIPTION_ADDITION = (
    "<p><strong>SGA7 II Expose XVIII boundary-source preservation:</strong> this "
    "successor updates only the compact SGA7 II source/WIP archive. The "
    "direct Exposes X-XVII reader and master remain byte-identical. The ZIP "
    "now preserves 48 continuous Expose-XVIII source pages, scan indices "
    "261-308 / book folios 254-301, including the title and contents page; "
    "indices 309-334 remain absent, so the Expose is explicitly incomplete "
    "and excluded from the direct reader. The exact 400-dpi scan-derived "
    "crop used for index 261 is included with parent hash, page, folio, "
    "dimensions, crop box, and crop hash. The bounded WIP compiled in "
    "isolation with zero fatal errors and one disclosed overfull box.</p>"
)
NOTES_ADDITION = (
    "<p>This source-custody update closes the omitted index-261 boundary in "
    "the partial Expose-XVIII source and preserves the actual crop pixels "
    "used for that page rather than substituting a metadata-only ledger. No "
    "direct reader, preview, existing image archive, or unrelated SGA file "
    "changed.</p>"
)


def sha256_path(path: Path) -> str:
    return base.sha256_path(path)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def write_csv(path: Path, rows: list[dict[str, object]], fields: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def safe_member(name: str) -> bool:
    pure = PurePosixPath(name)
    return (
        name == name.replace("\\", "/")
        and not pure.is_absolute()
        and ".." not in pure.parts
        and not (len(name) > 1 and name[1] == ":")
    )


def package_files() -> list[Path]:
    return sorted(
        (path for path in PACKAGE_ROOT.rglob("*") if path.is_file()),
        key=lambda path: path.relative_to(PACKAGE_ROOT).as_posix().casefold(),
    )


def verify_package() -> None:
    files = package_files()
    if (
        len(files) != EXPECTED_PACKAGE_FILES
        or sum(path.stat().st_size for path in files) != EXPECTED_PACKAGE_BYTES
    ):
        raise RuntimeError("SGA7 II package boundary changed")
    manifest = PACKAGE_ROOT / "SHA256SUMS.csv"
    if (manifest.stat().st_size, sha256_path(manifest)) != EXPECTED_PACKAGE_MANIFEST:
        raise RuntimeError("SGA7 II package manifest changed")
    rows = list(csv.DictReader(manifest.open("r", encoding="utf-8-sig", newline="")))
    expected_paths = {
        path.relative_to(PACKAGE_ROOT).as_posix()
        for path in files
        if path.name != "SHA256SUMS.csv"
    }
    if len(rows) != 32 or {row["path"] for row in rows} != expected_paths:
        raise RuntimeError("SGA7 II package manifest closure changed")
    for row in rows:
        path = PACKAGE_ROOT / row["path"]
        if (path.stat().st_size, sha256_path(path)) != (
            int(row["bytes"]),
            row["sha256"].upper(),
        ):
            raise RuntimeError(f"Package identity changed: {row['path']}")
    wip = PACKAGE_ROOT / "work-in-progress/expose_XVIII_partial.tex"
    if (wip.stat().st_size, sha256_path(wip)) != EXPECTED_WIP:
        raise RuntimeError("Expose-XVIII WIP identity changed")
    validation = json.loads(
        (PACKAGE_ROOT / "PACKAGE_VALIDATION.json").read_text(encoding="utf-8")
    )
    wip_validation = validation.get("work_in_progress", {})
    if (
        validation.get("status") != "PASS_READY_FOR_WORKING_PUBLICATION"
        or validation.get("errors")
        or wip_validation.get("source_pdf_indices_inclusive") != [261, 308]
        or wip_validation.get("source_page_markers") != 48
        or wip_validation.get("missing_indices_within_bounded_range") != []
        or wip_validation.get("remaining_source_pdf_indices") != [309, 334]
    ):
        raise RuntimeError("Expose-XVIII WIP validation changed")


def build_source_zip() -> dict[str, object]:
    verify_package()
    rows: list[dict[str, object]] = []
    for relative in SOURCE_MEMBERS:
        path = PACKAGE_ROOT / relative
        rows.append(
            {
                "path": relative,
                "bytes": path.stat().st_size,
                "sha256": sha256_path(path),
            }
        )
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(
        buffer,
        fieldnames=["path", "bytes", "sha256"],
        lineterminator="\r\n",
        quoting=csv.QUOTE_ALL,
    )
    writer.writeheader()
    writer.writerows(rows)
    manifest = buffer.getvalue().encode("utf-8")
    TEMP_ROOT.mkdir(parents=True, exist_ok=True)
    SOURCE_ZIP.unlink(missing_ok=True)
    prefix = "SGA7II_French_Source_Transcription_Working_X-XVII_20260731/"
    with zipfile.ZipFile(
        SOURCE_ZIP,
        "w",
        compression=zipfile.ZIP_DEFLATED,
        compresslevel=9,
        allowZip64=True,
    ) as archive:
        for relative in sorted(SOURCE_MEMBERS, key=str.casefold):
            info = zipfile.ZipInfo(prefix + relative, date_time=(2026, 7, 31, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            info.create_system = 3
            archive.writestr(
                info, (PACKAGE_ROOT / relative).read_bytes(), compresslevel=9
            )
        info = zipfile.ZipInfo(prefix + "SHA256SUMS.csv", date_time=(2026, 7, 31, 0, 0, 0))
        info.compress_type = zipfile.ZIP_DEFLATED
        info.external_attr = 0o100644 << 16
        info.create_system = 3
        archive.writestr(info, manifest, compresslevel=9)
    if (SOURCE_ZIP.stat().st_size, sha256_path(SOURCE_ZIP)) != EXPECTED_SOURCE_ZIP:
        raise RuntimeError("Deterministic SGA7 II source ZIP changed")
    inventory = prior.zip_inventory(SOURCE_ZIP)
    if (
        int(inventory["members"]) != 22
        or not all(safe_member(name) for name in inventory["member_identities"])
    ):
        raise RuntimeError("SGA7 II source ZIP member boundary changed")
    return {
        "path": SOURCE_ZIP,
        "bytes": SOURCE_ZIP.stat().st_size,
        "sha256": sha256_path(SOURCE_ZIP),
        "md5": base.md5_path(SOURCE_ZIP),
        "inventory": inventory,
    }


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
    receipt = json.loads((REPO_ROOT / GITHUB_RECEIPT_REL).read_text(encoding="utf-8"))
    if (
        receipt.get("status") != "PASS_GITHUB_PUBLIC_READBACK"
        or receipt.get("commit") != GITHUB_PACKAGE_COMMIT
        or receipt.get("package_path") != PACKAGE_REL.as_posix()
        or int(receipt.get("files_read_back", -1)) != EXPECTED_PACKAGE_FILES
        or int(receipt.get("bytes_read_back", -1)) != EXPECTED_PACKAGE_BYTES
        or not all(row.get("match") for row in receipt.get("file_readback", []))
    ):
        raise RuntimeError("SGA7 II GitHub receipt changed")
    subprocess.check_call(
        ["git", "merge-base", "--is-ancestor", GITHUB_PACKAGE_COMMIT, "HEAD"],
        cwd=REPO_ROOT,
    )
    remote = subprocess.check_output(
        ["git", "ls-remote", "github-write", "refs/heads/main"],
        cwd=REPO_ROOT,
        text=True,
    ).split()[0]
    head = subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=REPO_ROOT, text=True
    ).strip()
    if remote != head:
        raise RuntimeError("Local HEAD is not public GitHub main")
    return receipt


def build_controls(
    source_zip: dict[str, object],
    predecessor: dict[str, object],
    github: dict[str, object],
) -> dict[str, object]:
    shutil.rmtree(CONTROLS_ROOT, ignore_errors=True)
    CONTROLS_ROOT.mkdir(parents=True)
    retained = expected_retained(predecessor)
    (CONTROLS_ROOT / "09_README_CURRENT_RELEASE.md").write_text(
        """# Current SGA release controls

The reader-facing order and default SGA1 preview are unchanged. This successor
replaces only the compact SGA7 II source/WIP archive. Its direct X-XVII reader
and editable master remain byte-identical.

The replacement archive preserves 48 continuous Expose-XVIII source pages,
scan indices 261-308, including its title and contents page. Indices 309-334
remain absent, so the WIP is not a complete Expose and is excluded from the
direct reader. The exact index-261 source crop and provenance are included.
The WIP compiled in isolation with zero fatal errors and one disclosed
overfull box.
""",
        encoding="utf-8",
        newline="\n",
    )
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
    rows.append(
        {
            "filename": SOURCE_ZIP_NAME,
            "bytes": int(source_zip["bytes"]),
            "sha256": str(source_zip["sha256"]),
            "release_role": "portable_reader_source_and_continuous_wip",
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
            "source_zip_members": 22,
            "xviii_wip_source_indices": [261, 308],
            "xviii_wip_source_page_markers": 48,
            "xviii_boundary_crop_sha256": "3A6446FFB5E213E35B42A4EAD7934FCC542D6622D2E1B8E1C3B3B3D9F9CE77DD",
            "xviii_remaining_indices": [309, 334],
            "direct_reader_changed": False,
        },
    )
    copies = {
        "09c_SGA7II_PACKAGE_VALIDATION.json": PACKAGE_ROOT / "PACKAGE_VALIDATION.json",
        "09d_SGA7II_PACKAGE_SHA256SUMS.csv": PACKAGE_ROOT / "SHA256SUMS.csv",
        "09e_SGA7II_ZENODO_UPLOAD_MANIFEST.csv": PACKAGE_ROOT / "ZENODO_UPLOAD_MANIFEST.csv",
        "09f_SGA7II_XVIII_WIP_README.md": PACKAGE_ROOT / "work-in-progress/README.md",
        "09g_SGA7II_GITHUB_PUBLIC_READBACK.json": REPO_ROOT / GITHUB_RECEIPT_REL,
    }
    for name, source in copies.items():
        shutil.copyfile(source, CONTROLS_ROOT / name)
    packed = [
        {
            "filename": path.name,
            "bytes": path.stat().st_size,
            "sha256": sha256_path(path),
        }
        for path in sorted(CONTROLS_ROOT.iterdir(), key=lambda path: path.name.casefold())
    ]
    write_csv(
        CONTROLS_ROOT / "PACKED_CONTROL_SHA256.csv",
        packed,
        ["filename", "bytes", "sha256"],
    )
    CONTROLS_ZIP.unlink(missing_ok=True)
    with zipfile.ZipFile(
        CONTROLS_ZIP,
        "w",
        compression=zipfile.ZIP_DEFLATED,
        compresslevel=9,
        allowZip64=True,
    ) as archive:
        for path in sorted(CONTROLS_ROOT.iterdir(), key=lambda path: path.name.casefold()):
            info = zipfile.ZipInfo(path.name, date_time=(2026, 7, 31, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            info.create_system = 3
            archive.writestr(info, path.read_bytes(), compresslevel=9)
    inventory = prior.zip_inventory(CONTROLS_ZIP)
    return {
        "path": CONTROLS_ZIP,
        "bytes": CONTROLS_ZIP.stat().st_size,
        "sha256": sha256_path(CONTROLS_ZIP),
        "md5": base.md5_path(CONTROLS_ZIP),
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
    prior.OLD_DESCRIPTION_ADDITION = "<!-- no removed description -->"
    prior.OLD_NOTES_ADDITION = "<!-- no removed notes -->"
    prior.DESCRIPTION_ADDITION = DESCRIPTION_ADDITION
    prior.NOTES_ADDITION = NOTES_ADDITION
    prior.PDF_NAME = "00h_SGA7II_French_Source_Transcription_Working_X-XVII_20260731.pdf"
    prior.TEX_NAME = "02h_SGA7II_French_Source_Transcription_Working_X-XVII_20260731.tex"
    prior.expected_retained = expected_retained


def public_readback(
    session,
    token: str,
    record_id: int,
    source_zip: dict[str, object],
    controls: dict[str, object],
    predecessor: dict[str, object],
    github: dict[str, object],
) -> dict[str, object]:
    record = base.check(
        session.get(
            f"{API}/records/{record_id}?expand=true",
            headers=prior.public_headers(),
            timeout=(30, 300),
        ),
        {200},
    ).json()
    retained = expected_retained(predecessor)
    expected = {**retained, SOURCE_ZIP_NAME: source_zip, CONTROLS_NAME: controls}
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
        not record.get("is_published")
        or set(entries) != set(expected)
        or len(entries) != FINAL_FILES
        or record["parent"]["pids"]["doi"]["identifier"] != CONCEPT_DOI
        or record["files"].get("default_preview") != DEFAULT_PREVIEW
        or int(latest["id"]) != record_id
    ):
        raise RuntimeError("Public SGA7 II WIP successor boundary changed")
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
                raise RuntimeError(f"Public SGA7 II WIP mismatch: {name}")
            files[name] = {
                "bytes": observed[0],
                "sha256": observed[1],
                "md5": observed[2],
                "content_url": entries[name]["links"]["content"],
                "match": True,
                "readback_mode": "anonymous_full_download_exact_sha256",
            }
            if destination is not None:
                inventory = prior.zip_inventory(destination)
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
        or int(archives[SOURCE_ZIP_NAME]["members"]) != 22
    ):
        raise RuntimeError("SGA7 II WIP public readback did not close")
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
        "github": {
            "commit": github["commit"],
            "package_path": github["package_path"],
            "files_read_back": github["files_read_back"],
        },
        "source_zip_members": 22,
        "xviii_wip_source_indices": [261, 308],
        "xviii_wip_source_page_markers": 48,
        "xviii_boundary_crop_sha256": "3A6446FFB5E213E35B42A4EAD7934FCC542D6622D2E1B8E1C3B3B3D9F9CE77DD",
        "direct_reader_changed": False,
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
                "# SGA7 II Expose-XVIII boundary source/crop publication receipt",
                "",
                f"- Record: <https://zenodo.org/records/{record_id}>",
                f"- DOI: `{result['doi']}`",
                f"- Concept DOI: `{CONCEPT_DOI}`",
                f"- GitHub package commit: `{GITHUB_PACKAGE_COMMIT}`",
                f"- Public files: {len(files)} / {result['outer_bytes']:,} bytes",
                f"- Retained predecessor files: {len(retained)} / identity errors 0",
                f"- Replacement source ZIP: 22 members / `{EXPECTED_SOURCE_ZIP[1]}`",
                "- Expose-XVIII WIP: continuous source indices 261-308; 309-334 absent",
                "- Exact index-261 crop pixels and provenance included",
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
    dict[str, object],
    dict[str, object],
    dict[str, object],
    dict[str, object],
]:
    configure_prior()
    source_zip = build_source_zip()
    predecessor = load_predecessor()
    github = verify_github()
    controls = build_controls(source_zip, predecessor, github)
    return source_zip, predecessor, github, controls


def preflight() -> dict[str, object]:
    source_zip, predecessor, github, controls = prepare()
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
        "source_zip": {
            "bytes": source_zip["bytes"],
            "sha256": source_zip["sha256"],
            "members": source_zip["inventory"]["members"],
        },
        "controls_zip": {
            "bytes": controls["bytes"],
            "sha256": controls["sha256"],
            "members": controls["inventory"]["members"],
        },
        "duplicate_concept_created": False,
    }


def publish() -> dict[str, object]:
    source_zip, predecessor, github, controls = prepare()
    token = base.find_token()
    session = base.make_session()
    live = prior.fetch_live(session, predecessor)
    prior.assert_no_untracked_draft(session, token)
    draft_id = prior.create_or_resume_draft(session, token, live)
    published = prior.stage_and_publish(
        session,
        token,
        live,
        draft_id,
        {SOURCE_ZIP_NAME: source_zip},
        controls,
        predecessor,
    )
    return public_readback(
        session,
        token,
        int(published["id"]),
        source_zip,
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
