#!/usr/bin/env python3
"""Publish and read back SGA7 I English through Expose IX section 3.4."""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import shutil
import time
import zipfile
from pathlib import Path

import publish_sga7i_english_i_ii_vi_vii_complete_zenodo_20260731 as template


base = template.base
prior = template.prior
API = template.API
PUBLICATION_DATE = "2026-08-01"
CONCEPT_DOI = "10.5281/zenodo.20410947"
PREDECESSOR_RECORD = 21_729_478
PREDECESSOR_DOI = "10.5281/zenodo.21729478"
PREDECESSOR_FILES = 83
PREDECESSOR_BYTES = 677_940_470
FINAL_FILES = 83
DEFAULT_PREVIEW = "00a_SGA1_English_Reader.pdf"
OLD_CONTROLS_NAME = "10z_SGA_Current_Release_Controls_20260801.zip"
CONTROLS_NAME = "10z_SGA_Current_Release_Controls_20260801_r2.zip"
VERSION = "2026-08-01 SGA7 I English through Expose IX section 3.4"

REPO_ROOT = Path(__file__).resolve().parents[1]
PACKAGE_REL = Path(
    "sources/sga/"
    "sga7i-english-source-first-working-through-expose-ix-3-4-20260801"
)
PACKAGE_ROOT = REPO_ROOT / PACKAGE_REL
TEMP_ROOT = REPO_ROOT / "tmp/zenodo/sga7i-english-ix-3-4-20260801"
CONTROLS_ROOT = TEMP_ROOT / "release-controls"
CONTROLS_ZIP = TEMP_ROOT / CONTROLS_NAME
READBACK_ROOT = TEMP_ROOT / "public-readback"
STATE_PATH = TEMP_ROOT / "draft_state.json"
RECEIPT_ROOT = REPO_ROOT / "manifests/published-zenodo"
RECEIPT_TAG = "20260801_sga7i_english_through_expose_ix_3_4"
PREDECESSOR_RECEIPT = RECEIPT_ROOT / (
    "20260801_sga7i_english_through_expose_viii_complete_"
    "record_21729478_public_readback.json"
)
GITHUB_PACKAGE_COMMIT = "a374b92e6002a32f076b3b6ac0d2a01897fbac7d"

OLD_PDF_NAME = (
    "00i_SGA7I_English_Working_Through_Expose_VIII_Complete_20260801.pdf"
)
OLD_TEX_NAME = (
    "02i_SGA7I_English_Working_Through_Expose_VIII_Complete_20260801.tex"
)
OLD_SOURCE_ZIP_NAME = (
    "10i_SGA7I_English_Working_Through_Expose_VIII_Complete_"
    "Reader_and_TeX_20260801.zip"
)
PDF_NAME = "00i_SGA7I_English_Working_Through_Expose_IX_3_4_20260801.pdf"
TEX_NAME = "02i_SGA7I_English_Working_Through_Expose_IX_3_4_20260801.tex"
SOURCE_ZIP_NAME = (
    "10i_SGA7I_English_Working_Through_Expose_IX_3_4_"
    "Reader_and_TeX_20260801.zip"
)
REPLACED_NAMES = {
    OLD_PDF_NAME,
    OLD_TEX_NAME,
    OLD_SOURCE_ZIP_NAME,
    OLD_CONTROLS_NAME,
}

EXPECTED_PACKAGE_FILES = 147
EXPECTED_PACKAGE_BYTES = 4_018_145
EXPECTED_MANIFEST = (
    19_162,
    "FDD57CB5BD3ADF97076F6A2193175459D12415902E2663B0405035903F614269",
)
EXPECTED_VALIDATION = (
    4_614,
    "B009189FA588D4917009D7D2B1D3C6CB62A27F75335BD7523898338EEA6B2D32",
)
EXPECTED_PDF = (
    1_551_833,
    "BF474B377BBFF5BECB561A0FBDBF8E426842F70FDE3043572687D159F864395F",
)
EXPECTED_TEX = (
    10_181,
    "71F2D7A16CCEABEDC4E2E3E1F0612B2CA1895583751EB43C7361C6949CBEC2A4",
)
EXPECTED_SOURCE_ZIP = (
    1_696_799,
    "8D8517565AECB2FD3CCF8244499FD64D257570A5C4842C0B807A97919EE49933",
)
EXPECTED_PREDECESSOR_RECEIPT = (
    105_798,
    "726E622749473666B79EF55DE960F196D7E5E6D3FD4DE186057C8EA30077A438",
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
    "and a 198-page SGA7 I English working reader containing complete Exposes "
    "I, II, VI, VII, and VIII plus Expose IX through section 3.4. Its compact "
    "141-member archive contains that reader and the exact 137-component "
    "buildable TeX closure. The next English cursor is Expose IX Proposition "
    "3.5, authority line 880, scan index 361, source folio 350.</p>"
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
        raise RuntimeError("SGA7 I through-Expose-IX-3.4 package boundary changed")
    manifest = PACKAGE_ROOT / "SHA256SUMS.csv"
    validation_path = PACKAGE_ROOT / "PACKAGE_VALIDATION.json"
    if (manifest.stat().st_size, sha256_path(manifest)) != EXPECTED_MANIFEST:
        raise RuntimeError("SGA7 I package manifest changed")
    if (validation_path.stat().st_size, sha256_path(validation_path)) != EXPECTED_VALIDATION:
        raise RuntimeError("SGA7 I package validation changed")
    validation = json.loads(validation_path.read_text(encoding="utf-8"))
    if validation.get("status") != "PASS_PUBLIC_WORKING_CHECKPOINT" or validation.get("errors"):
        raise RuntimeError("SGA7 I package is not validated")
    rows = list(csv.DictReader(manifest.open("r", encoding="utf-8", newline="")))
    represented = {
        path.relative_to(PACKAGE_ROOT).as_posix(): path
        for path in files
        if path.name != "SHA256SUMS.csv"
    }
    if len(rows) != 146 or {row["path"] for row in rows} != set(represented):
        raise RuntimeError("SGA7 I package manifest closure changed")
    for row in rows:
        path = represented[row["path"]]
        observed = (path.stat().st_size, sha256_path(path))
        wanted = (int(row["bytes"]), row["sha256"].upper())
        if observed != wanted:
            raise RuntimeError(f"SGA7 I package identity changed: {row['path']}")
    source_zip = PACKAGE_ROOT / (
        "SGA7I_English_Working_Through_Expose_IX_3_4_"
        "Reader_and_TeX_20260801.zip"
    )
    if (source_zip.stat().st_size, sha256_path(source_zip)) != EXPECTED_SOURCE_ZIP:
        raise RuntimeError("SGA7 I source ZIP changed")
    inventory = template.zip_inventory(source_zip)
    if int(inventory["members"]) != 141:
        raise RuntimeError("SGA7 I source ZIP boundary changed")
    with zipfile.ZipFile(source_zip) as archive:
        embedded_rows = list(
            csv.DictReader(
                io.StringIO(
                    archive.read("ZIP_MEMBER_SHA256SUMS.csv").decode("utf-8")
                )
            )
        )
        if len(embedded_rows) != 140:
            raise RuntimeError("SGA7 I embedded ZIP manifest changed")
        for row in embedded_rows:
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
        / "reader/SGA7I_English_Working_Through_Expose_IX_3_4_20260801.pdf",
        TEX_NAME: PACKAGE_ROOT
        / "source/SGA7I_English_Working_Through_Expose_IX_3_4_20260801.tex",
        SOURCE_ZIP_NAME: PACKAGE_ROOT
        / (
            "SGA7I_English_Working_Through_Expose_IX_3_4_"
            "Reader_and_TeX_20260801.zip"
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
            raise RuntimeError(f"SGA7 I upload identity changed: {name}")
        result[name] = {
            "path": path,
            "bytes": path.stat().st_size,
            "sha256": sha256_path(path),
            "md5": md5_path(path),
        }
    result[SOURCE_ZIP_NAME]["inventory"] = inventory
    return result


def load_predecessor() -> dict[str, object]:
    if (
        PREDECESSOR_RECEIPT.stat().st_size,
        sha256_path(PREDECESSOR_RECEIPT),
    ) != EXPECTED_PREDECESSOR_RECEIPT:
        raise RuntimeError("Compact SGA predecessor receipt changed")
    receipt = json.loads(PREDECESSOR_RECEIPT.read_text(encoding="utf-8"))
    if (
        receipt.get("status") != "PASS_PUBLIC_READBACK"
        or int(receipt.get("record_id", -1)) != PREDECESSOR_RECORD
        or receipt.get("doi") != PREDECESSOR_DOI
        or receipt.get("concept_doi") != CONCEPT_DOI
        or int(receipt.get("outer_files", -1)) != PREDECESSOR_FILES
        or int(receipt.get("outer_bytes", -1)) != PREDECESSOR_BYTES
        or receipt.get("active_draft_remaining") is not False
    ):
        raise RuntimeError("Compact SGA predecessor receipt boundary changed")

    session = base.make_session()
    record = base.check(
        session.get(
            f"{API}/records/{PREDECESSOR_RECORD}?expand=true",
            headers=prior.public_headers(),
            timeout=(30, 180),
        ),
        {200},
    ).json()
    entries = base.modern_entries(record)
    if (
        int(record["id"]) != PREDECESSOR_RECORD
        or record["pids"]["doi"]["identifier"] != PREDECESSOR_DOI
        or record["parent"]["pids"]["doi"]["identifier"] != CONCEPT_DOI
        or len(entries) != PREDECESSOR_FILES
        or sum(int(row["size"]) for row in entries.values()) != PREDECESSOR_BYTES
        or record["files"].get("default_preview") != DEFAULT_PREVIEW
    ):
        raise RuntimeError("Live SGA predecessor boundary changed")

    controls_row = receipt["outer_file_readback"].get(OLD_CONTROLS_NAME)
    controls_entry = entries.get(OLD_CONTROLS_NAME)
    if controls_row is None or controls_entry is None:
        raise RuntimeError("Current release controls are missing")
    controls_data = base.check(
        session.get(controls_entry["links"]["content"], timeout=(30, 300)),
        {200},
    ).content
    controls_identity = (
        len(controls_data),
        hashlib.sha256(controls_data).hexdigest().upper(),
        hashlib.md5(controls_data, usedforsecurity=False).hexdigest().lower(),
    )
    wanted_controls = (
        int(controls_row["bytes"]),
        str(controls_row["sha256"]).upper(),
        str(controls_row["md5"]).lower(),
    )
    if controls_identity != wanted_controls:
        raise RuntimeError("Current public release-control ZIP changed")
    with zipfile.ZipFile(io.BytesIO(controls_data)) as archive:
        if archive.testzip() is not None:
            raise RuntimeError("Current public release-control ZIP failed CRC")
        release_rows = list(
            csv.DictReader(
                io.StringIO(
                    archive.read("09a_RELEASE_FILE_MANIFEST.csv").decode("utf-8")
                )
            )
        )
    identities = {
        row["filename"]: {
            "bytes": int(row["bytes"]),
            "sha256": row["sha256"].upper(),
        }
        for row in release_rows
    }
    identities[OLD_CONTROLS_NAME] = {
        "bytes": int(controls_row["bytes"]),
        "sha256": str(controls_row["sha256"]).upper(),
    }
    if len(release_rows) != 82 or set(identities) != set(entries):
        raise RuntimeError("Current public release manifest closure changed")
    files: dict[str, dict[str, object]] = {}
    for name, entry in entries.items():
        row = identities[name]
        if int(entry["size"]) != int(row["bytes"]):
            raise RuntimeError(f"Current predecessor size changed: {name}")
        files[name] = {
            "bytes": int(row["bytes"]),
            "sha256": str(row["sha256"]),
            "md5": base.normalized_md5(entry["checksum"]),
            "content_url": entry["links"]["content"],
            "match": True,
        }
    return {
        "status": "PASS_PUBLIC_READBACK",
        "errors": [],
        "record_id": PREDECESSOR_RECORD,
        "doi": PREDECESSOR_DOI,
        "concept_doi": CONCEPT_DOI,
        "outer_files": len(files),
        "outer_bytes": sum(int(row["bytes"]) for row in files.values()),
        "outer_file_readback": files,
        "default_preview": DEFAULT_PREVIEW,
        "version": receipt["version"],
    }


def build_controls(
    local: dict[str, dict[str, object]],
    predecessor: dict[str, object],
    github: dict[str, object],
) -> dict[str, object]:
    resolved_temp = TEMP_ROOT.resolve()
    if not resolved_temp.is_relative_to((REPO_ROOT / "tmp").resolve()):
        raise RuntimeError("Refusing to rebuild controls outside repository tmp")
    shutil.rmtree(CONTROLS_ROOT, ignore_errors=True)
    CONTROLS_ROOT.mkdir(parents=True, exist_ok=True)
    retained = template.expected_retained(predecessor)
    (CONTROLS_ROOT / "09_README_CURRENT_RELEASE.md").write_text(
        """# Current SGA release controls

The cumulative English readers remain first and SGA1 remains the browser
preview. This successor adds a bounded 198-page SGA7 I English reader
containing complete Exposes I, II, VI, VII, and VIII plus Expose IX through
section 3.4.

The exact continuation is Expose IX, Proposition 3.5, authority line 880,
zero-based scan index 361, source folio 350. Proposition 3.5 and later are
absent. The reader is current-progress source-aligned English, not a complete
SGA7 I volume, critical edition, peer review, accessibility certification, or
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
                "sha256": str(row["sha256"]).upper(),
                "release_role": roles[name],
                "source": PACKAGE_REL.as_posix(),
            }
        )
    rows.sort(key=lambda row: str(row["filename"]).casefold())
    template.write_csv(
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
            "reader_pages": 198,
            "editable_tex_files": 138,
            "component_files": 137,
            "continuation": {
                "unit": "Expose IX, Proposition 3.5",
                "authority_line": 880,
                "scan_index_zero_based": 361,
                "source_folio": 350,
                "physical_pdf_page": 362,
            },
            "source_zip_members": 141,
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
            "member_readback": "141/141 exact",
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
    template.write_csv(
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
            info = zipfile.ZipInfo(path.name, date_time=(2026, 8, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            info.create_system = 3
            archive.writestr(info, path.read_bytes(), compresslevel=9)
    controls_inventory = template.zip_inventory(CONTROLS_ZIP)
    if int(controls_inventory["members"]) != len(packed) + 1:
        raise RuntimeError("Release-control ZIP boundary changed")
    return {
        "path": CONTROLS_ZIP,
        "bytes": CONTROLS_ZIP.stat().st_size,
        "sha256": sha256_path(CONTROLS_ZIP),
        "md5": md5_path(CONTROLS_ZIP),
        "inventory": controls_inventory,
    }


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
    retained = template.expected_retained(predecessor)
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
    resolved_readback = READBACK_ROOT.resolve()
    if not resolved_readback.is_relative_to((REPO_ROOT / "tmp").resolve()):
        raise RuntimeError("Refusing readback outside repository tmp")
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
                inventory = template.zip_inventory(destination)
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
        or int(archives[SOURCE_ZIP_NAME]["members"]) != 141
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
        "source_zip_members": 141,
        "continuation": {
            "unit": "Expose IX, Proposition 3.5",
            "authority_line": 880,
            "scan_index_zero_based": 361,
            "source_folio": 350,
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
                "# SGA7 I English through Expose IX section 3.4 publication receipt",
                "",
                f"- Record: <https://zenodo.org/records/{record_id}>",
                f"- DOI: `{result['doi']}`",
                f"- Concept DOI: `{CONCEPT_DOI}`",
                f"- GitHub package commit: `{GITHUB_PACKAGE_COMMIT}`",
                f"- Public files: {len(files)} / {result['outer_bytes']:,} bytes",
                f"- Retained predecessor files: {len(retained)} / identity errors 0",
                f"- Reader SHA-256: `{EXPECTED_PDF[1]}`",
                f"- Reader/source ZIP: 141 members / `{EXPECTED_SOURCE_ZIP[1]}`",
                "- Scope: Exposes I, II, VI, VII, and VIII complete; Expose IX through section 3.4",
                "- Continuation: Expose IX Proposition 3.5 / authority line 880 / scan index 361 / source folio 350",
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


def configure_template() -> None:
    values = {
        "PUBLICATION_DATE": PUBLICATION_DATE,
        "CONCEPT_DOI": CONCEPT_DOI,
        "PREDECESSOR_RECORD": PREDECESSOR_RECORD,
        "PREDECESSOR_DOI": PREDECESSOR_DOI,
        "PREDECESSOR_FILES": PREDECESSOR_FILES,
        "PREDECESSOR_BYTES": PREDECESSOR_BYTES,
        "FINAL_FILES": FINAL_FILES,
        "DEFAULT_PREVIEW": DEFAULT_PREVIEW,
        "CONTROLS_NAME": CONTROLS_NAME,
        "VERSION": VERSION,
        "PACKAGE_REL": PACKAGE_REL,
        "PACKAGE_ROOT": PACKAGE_ROOT,
        "TEMP_ROOT": TEMP_ROOT,
        "CONTROLS_ROOT": CONTROLS_ROOT,
        "CONTROLS_ZIP": CONTROLS_ZIP,
        "READBACK_ROOT": READBACK_ROOT,
        "STATE_PATH": STATE_PATH,
        "RECEIPT_ROOT": RECEIPT_ROOT,
        "RECEIPT_TAG": RECEIPT_TAG,
        "PREDECESSOR_RECEIPT": PREDECESSOR_RECEIPT,
        "GITHUB_PACKAGE_COMMIT": GITHUB_PACKAGE_COMMIT,
        "PDF_NAME": PDF_NAME,
        "TEX_NAME": TEX_NAME,
        "SOURCE_ZIP_NAME": SOURCE_ZIP_NAME,
        "REPLACED_NAMES": REPLACED_NAMES,
        "EXPECTED_PACKAGE_FILES": EXPECTED_PACKAGE_FILES,
        "EXPECTED_PACKAGE_BYTES": EXPECTED_PACKAGE_BYTES,
        "EXPECTED_MANIFEST": EXPECTED_MANIFEST,
        "EXPECTED_VALIDATION": EXPECTED_VALIDATION,
        "EXPECTED_PDF": EXPECTED_PDF,
        "EXPECTED_TEX": EXPECTED_TEX,
        "EXPECTED_SOURCE_ZIP": EXPECTED_SOURCE_ZIP,
        "DESCRIPTION_ADDITION": DESCRIPTION_ADDITION,
        "NOTES_ADDITION": NOTES_ADDITION,
    }
    for name, value in values.items():
        setattr(template, name, value)
    template.package_files = package_files
    template.verify_package = verify_package
    template.local_uploads = local_uploads
    template.load_predecessor = load_predecessor
    template.build_controls = build_controls
    template.public_readback = public_readback


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--preflight", action="store_true")
    args = parser.parse_args()
    configure_template()
    result = template.preflight() if args.preflight else template.publish()
    print(json.dumps(result, indent=2, ensure_ascii=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
