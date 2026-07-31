#!/usr/bin/env python3
"""Publish the deduplicated SGA7 lead-opened source-crop archive."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import shutil
import subprocess
import zipfile
from pathlib import Path, PurePosixPath

import publish_sga7ii_x_xvii_source_images_zenodo_20260731 as prior


base = prior.base
PUBLICATION_DATE = "2026-07-31"
CONCEPT_DOI = "10.5281/zenodo.20410947"
PREDECESSOR_RECORD = 21_716_658
PREDECESSOR_DOI = "10.5281/zenodo.21716658"
PREDECESSOR_FILES = 78
PREDECESSOR_BYTES = 640_234_830
FINAL_FILES = 79
DEFAULT_PREVIEW = "00a_SGA1_English_Reader.pdf"
CONTROLS_NAME = "10z_SGA_Current_Release_Controls_20260730.zip"
VERSION = "2026-07-31 SGA7 lead-opened source-crop pixels"

REPO_ROOT = Path(__file__).resolve().parents[1]
PACKAGE_REL = Path("sources/sga/sga7-lead-opened-source-crops-20260731")
PACKAGE_ROOT = REPO_ROOT / PACKAGE_REL
ZIP_NAME = "10h3_SGA7I_SGA7II_LeadOpened_Source_Crops_20260731.zip"
TEMP_ROOT = REPO_ROOT / "tmp/zenodo/sga7-lead-opened-source-crops-20260731"
ZIP_PATH = TEMP_ROOT / ZIP_NAME
CONTROLS_ROOT = TEMP_ROOT / "release-controls"
CONTROLS_ZIP = TEMP_ROOT / CONTROLS_NAME
READBACK_ROOT = TEMP_ROOT / "public-readback"
STATE_PATH = TEMP_ROOT / "draft_state.json"
RECEIPT_ROOT = REPO_ROOT / "manifests/published-zenodo"
RECEIPT_TAG = "20260731_sga7_lead_opened_source_crops"
PREDECESSOR_RECEIPT = RECEIPT_ROOT / (
    "20260731_sga7ii_x_xvii_recovered_source_images_"
    "record_21716658_public_readback.json"
)
GITHUB_PACKAGE_COMMIT = "e727f3bf79201a5da7640da0b8c7e14b2a16c3f3"
GITHUB_RECEIPT_REL = Path(
    "manifests/published-github/"
    "20260731_sga7_lead_opened_source_crops_"
    "commit_e727f3bf_public_readback.json"
)

EXPECTED_PACKAGE = {
    "files": 37,
    "bytes": 6_489_877,
    "images": 29,
    "manifest_rows": 35,
    "manifest_sha256": (
        "B58033E6F7CEFE4953C140CA825808A36E55C23DF38A86BF5A9E49C28A22E745"
    ),
    "validation_sha256": (
        "8A0CBFD3B28D5342DD76A5B970D35E610E0CA26F9CE730B959E0350500A44DE7"
    ),
    "index_sha256": (
        "FBF443574495B48D9AF79FF2AD480FCF0F0EE1F5797B89EE0D14C29632F70BBF"
    ),
}
EXPECTED_ZIP = (
    6_197_740,
    "857AC1E01EAFF0EDA9C03C4887DE683FA8CA71DD715637AAD1061A1BEBD96058",
)
REPLACED_NAMES = {CONTROLS_NAME}

DESCRIPTION_ADDITION = (
    "<p><strong>Actual lead-opened SGA7 source crops:</strong> this successor "
    "adds one compact archive containing 29 scan-derived PNGs used directly "
    "during SGA7 I and SGA7 II transcription checks: 23 SGA7 I images and "
    "six SGA7 II images. They include page regions and high-detail formula, "
    "arrow, symbol, diagram, and wording crops from the publicly available "
    "parent scans. They are actual source pixels, not reconstructed-reader "
    "screenshots or metadata-only placeholders. The index records parent-scan "
    "hash, page and folio, recovered crop box and DPI, dimensions, linked TeX "
    "unit, read events, and exact image hash. Four exact pixels already in "
    "the public SGA image archives were excluded.</p>"
)
NOTES_ADDITION = (
    "<p>The lead-opened crop archive is deduplicated against 5,202 already "
    "public image hashes. Its 29 PNGs are source-adjudication evidence rather "
    "than a claim of complete transcription, translation, mathematical "
    "certification, critical edition, or blanket ownership of the underlying "
    "French works. Existing readers and their browser-preview order are "
    "unchanged.</p>"
)


def sha256(path: Path) -> str:
    return base.sha256_path(path)


def safe_member(name: str) -> bool:
    pure = PurePosixPath(name)
    return (
        name == name.replace("\\", "/")
        and not pure.is_absolute()
        and ".." not in pure.parts
        and not (len(name) > 1 and name[1] == ":")
    )


def write_csv(path: Path, rows: list[dict[str, object]], fields: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


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
    prior.PACKAGE_REL = PACKAGE_REL
    prior.PACKAGE_ROOT = PACKAGE_ROOT
    prior.TEMP_ROOT = TEMP_ROOT
    prior.CONTROLS_ROOT = CONTROLS_ROOT
    prior.CONTROLS_ZIP = CONTROLS_ZIP
    prior.READBACK_ROOT = READBACK_ROOT
    prior.STATE_PATH = STATE_PATH
    prior.RECEIPT_ROOT = RECEIPT_ROOT
    prior.RECEIPT_TAG = RECEIPT_TAG
    prior.PREDECESSOR_RECEIPT = PREDECESSOR_RECEIPT
    prior.GITHUB_PACKAGE_COMMIT = GITHUB_PACKAGE_COMMIT
    prior.GITHUB_RECEIPT_REL = GITHUB_RECEIPT_REL
    prior.REPLACED_NAMES = REPLACED_NAMES
    prior.OLD_DESCRIPTION_ADDITION = "<!-- no removed description -->"
    prior.OLD_NOTES_ADDITION = "<!-- no removed notes -->"
    prior.DESCRIPTION_ADDITION = DESCRIPTION_ADDITION
    prior.NOTES_ADDITION = NOTES_ADDITION
    prior.PDF_NAME = "00h_SGA7II_French_Source_Transcription_Working_X-XVII_20260731.pdf"
    prior.TEX_NAME = "02h_SGA7II_French_Source_Transcription_Working_X-XVII_20260731.tex"
    prior.expected_retained = expected_retained


def verify_package() -> None:
    files = sorted(path for path in PACKAGE_ROOT.rglob("*") if path.is_file())
    if (
        len(files) != EXPECTED_PACKAGE["files"]
        or sum(path.stat().st_size for path in files) != EXPECTED_PACKAGE["bytes"]
    ):
        raise RuntimeError("SGA7 crop package boundary changed")
    pngs = [path for path in files if path.suffix.lower() == ".png"]
    if len(pngs) != EXPECTED_PACKAGE["images"]:
        raise RuntimeError("SGA7 crop pixel boundary changed")
    controls = {
        "SHA256SUMS.csv": EXPECTED_PACKAGE["manifest_sha256"],
        "PACKAGE_VALIDATION.json": EXPECTED_PACKAGE["validation_sha256"],
        "SGA7_LEAD_OPENED_SOURCE_CROP_INDEX.csv": EXPECTED_PACKAGE["index_sha256"],
    }
    for name, wanted in controls.items():
        if sha256(PACKAGE_ROOT / name) != wanted:
            raise RuntimeError(f"SGA7 crop control changed: {name}")
    rows = list(
        csv.DictReader(
            (PACKAGE_ROOT / "SHA256SUMS.csv").open(
                "r", encoding="utf-8-sig", newline=""
            )
        )
    )
    expected_paths = {
        path.relative_to(PACKAGE_ROOT).as_posix()
        for path in files
        if path.name not in {"SHA256SUMS.csv", "PACKAGE_VALIDATION.json"}
    }
    if (
        len(rows) != EXPECTED_PACKAGE["manifest_rows"]
        or {row["relative_path"] for row in rows} != expected_paths
    ):
        raise RuntimeError("SGA7 crop manifest closure changed")
    for row in rows:
        path = PACKAGE_ROOT / row["relative_path"]
        if (path.stat().st_size, sha256(path)) != (
            int(row["bytes"]),
            row["sha256"].upper(),
        ):
            raise RuntimeError(f"SGA7 crop identity changed: {row['relative_path']}")
    validation = json.loads(
        (PACKAGE_ROOT / "PACKAGE_VALIDATION.json").read_text(encoding="utf-8")
    )
    if validation.get("status") != "PASS" or validation.get("errors"):
        raise RuntimeError("SGA7 crop package validation is not PASS")


def build_zip() -> dict[str, object]:
    verify_package()
    TEMP_ROOT.mkdir(parents=True, exist_ok=True)
    ZIP_PATH.unlink(missing_ok=True)
    prefix = PACKAGE_ROOT.name
    with zipfile.ZipFile(
        ZIP_PATH,
        "w",
        compression=zipfile.ZIP_DEFLATED,
        compresslevel=9,
        allowZip64=True,
    ) as archive:
        for path in sorted(
            (path for path in PACKAGE_ROOT.rglob("*") if path.is_file()),
            key=lambda path: path.relative_to(PACKAGE_ROOT).as_posix().casefold(),
        ):
            member = f"{prefix}/{path.relative_to(PACKAGE_ROOT).as_posix()}"
            info = zipfile.ZipInfo(member, date_time=(2026, 7, 31, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            info.create_system = 3
            archive.writestr(info, path.read_bytes(), compresslevel=9)
    if (ZIP_PATH.stat().st_size, sha256(ZIP_PATH)) != EXPECTED_ZIP:
        raise RuntimeError("Deterministic SGA7 crop ZIP changed")
    inventory = prior.zip_inventory(ZIP_PATH)
    if (
        int(inventory["members"]) != EXPECTED_PACKAGE["files"]
        or int(inventory["uncompressed_bytes"]) != EXPECTED_PACKAGE["bytes"]
        or len(
            [
                name
                for name in inventory["member_identities"]
                if name.lower().endswith(".png")
            ]
        )
        != EXPECTED_PACKAGE["images"]
        or not all(safe_member(name) for name in inventory["member_identities"])
    ):
        raise RuntimeError("SGA7 crop ZIP member boundary changed")
    return {
        "path": ZIP_PATH,
        "bytes": ZIP_PATH.stat().st_size,
        "sha256": sha256(ZIP_PATH),
        "md5": base.md5_path(ZIP_PATH),
        "inventory": inventory,
    }


def verify_github() -> dict[str, object]:
    receipt = json.loads((REPO_ROOT / GITHUB_RECEIPT_REL).read_text(encoding="utf-8"))
    if (
        receipt.get("status") != "PASS_GITHUB_PUBLIC_READBACK"
        or receipt.get("commit") != GITHUB_PACKAGE_COMMIT
        or receipt.get("package_path") != PACKAGE_REL.as_posix()
        or int(receipt.get("files_read_back", -1)) != EXPECTED_PACKAGE["files"]
        or int(receipt.get("bytes_read_back", -1)) != EXPECTED_PACKAGE["bytes"]
        or not all(row.get("match") for row in receipt.get("file_readback", []))
    ):
        raise RuntimeError("SGA7 crop GitHub receipt changed")
    subprocess.check_call(
        ["git", "merge-base", "--is-ancestor", GITHUB_PACKAGE_COMMIT, "HEAD"],
        cwd=REPO_ROOT,
    )
    remote = subprocess.check_output(
        ["git", "ls-remote", "github-write", "refs/heads/main"],
        cwd=REPO_ROOT,
        text=True,
    ).split()[0]
    if remote != subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=REPO_ROOT, text=True
    ).strip():
        raise RuntimeError("Local HEAD is not public GitHub main")
    return receipt


def load_predecessor_receipt() -> dict[str, object]:
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


def build_controls(
    archive: dict[str, object],
    predecessor: dict[str, object],
    github: dict[str, object],
) -> dict[str, object]:
    shutil.rmtree(CONTROLS_ROOT, ignore_errors=True)
    CONTROLS_ROOT.mkdir(parents=True)
    retained = expected_retained(predecessor)
    readme = """# Current SGA release controls

The reader-facing order is unchanged: the cumulative English-reader bundle is
first, the direct cumulative readers and masters follow, and SGA1 remains the
browser preview.

This successor adds one compact archive with 29 actual source-scan-derived
PNGs opened by the lead during SGA7 I and SGA7 II transcription checks. They
are source pixels, not reader screenshots or metadata-only placeholders. Four
exactly duplicate pixels already represented in the public visual archives
were excluded. The package records page, folio, crop, DPI, dimensions, linked
TeX, read events, and exact hashes.

The images are source-adjudication evidence, not a complete-transcription,
translation, mathematical-certification, critical-edition, or blanket-rights
claim.
"""
    (CONTROLS_ROOT / "09_README_CURRENT_RELEASE.md").write_text(
        readme, encoding="utf-8", newline="\n"
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
            "filename": ZIP_NAME,
            "bytes": int(archive["bytes"]),
            "sha256": str(archive["sha256"]),
            "release_role": "actual_source_image_witnesses",
            "source": PACKAGE_REL.as_posix(),
        }
    )
    rows.sort(key=lambda row: str(row["filename"]).casefold())
    write_csv(
        CONTROLS_ROOT / "09a_RELEASE_FILE_MANIFEST.csv",
        rows,
        ["filename", "bytes", "sha256", "release_role", "source"],
    )
    validation = {
        "status": "PASS_PREPARED_RELEASE_CONTROLS",
        "errors": [],
        "concept_doi": CONCEPT_DOI,
        "predecessor_record": PREDECESSOR_RECORD,
        "retained_predecessor_files": len(retained),
        "added_files": [ZIP_NAME],
        "replaced_files": sorted(REPLACED_NAMES),
        "expected_outer_files_including_controls": FINAL_FILES,
        "default_preview": DEFAULT_PREVIEW,
        "github": {
            "commit": github["commit"],
            "package_path": github["package_path"],
            "files_read_back": github["files_read_back"],
        },
        "source_crop_zip_members": EXPECTED_PACKAGE["files"],
        "source_crop_pngs": EXPECTED_PACKAGE["images"],
        "public_baseline_hashes_compared": 5_202,
        "new_image_hash_overlaps": 0,
        "actual_source_pixels_included": True,
        "target_reader_renders_included": False,
    }
    base.save_json(CONTROLS_ROOT / "09b_RELEASE_VALIDATION.json", validation)
    copies = {
        "09c_SGA7_CROP_PACKAGE_VALIDATION.json": PACKAGE_ROOT
        / "PACKAGE_VALIDATION.json",
        "09d_SGA7_CROP_PACKAGE_SHA256SUMS.csv": PACKAGE_ROOT / "SHA256SUMS.csv",
        "09e_SGA7_CROP_INDEX.csv": PACKAGE_ROOT
        / "SGA7_LEAD_OPENED_SOURCE_CROP_INDEX.csv",
        "09f_SGA7_CROP_DEDUPLICATION.csv": PACKAGE_ROOT
        / "DEDUPLICATION_AND_ROUTING.csv",
        "09g_SGA7_CROP_GITHUB_PUBLIC_READBACK.json": REPO_ROOT
        / GITHUB_RECEIPT_REL,
    }
    for name, source in copies.items():
        shutil.copyfile(source, CONTROLS_ROOT / name)
    packed = [
        {
            "filename": path.name,
            "bytes": path.stat().st_size,
            "sha256": sha256(path),
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
    ) as archive_zip:
        for path in sorted(CONTROLS_ROOT.iterdir(), key=lambda path: path.name.casefold()):
            info = zipfile.ZipInfo(path.name, date_time=(2026, 7, 31, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            info.create_system = 3
            archive_zip.writestr(info, path.read_bytes(), compresslevel=9)
    inventory = prior.zip_inventory(CONTROLS_ZIP)
    return {
        "path": CONTROLS_ZIP,
        "bytes": CONTROLS_ZIP.stat().st_size,
        "sha256": sha256(CONTROLS_ZIP),
        "md5": base.md5_path(CONTROLS_ZIP),
        "inventory": inventory,
    }


def public_readback(
    session,
    token: str,
    record_id: int,
    crop_archive: dict[str, object],
    controls: dict[str, object],
    predecessor: dict[str, object],
    github: dict[str, object],
) -> dict[str, object]:
    record = base.check(
        session.get(
            f"{base.API}/records/{record_id}?expand=true",
            headers=prior.public_headers(),
            timeout=(30, 300),
        ),
        {200},
    ).json()
    retained = expected_retained(predecessor)
    expected = {**retained, ZIP_NAME: crop_archive, CONTROLS_NAME: controls}
    entries = base.modern_entries(record)
    latest = base.check(
        session.get(
            f"{base.API}/records/{PREDECESSOR_RECORD}/versions/latest?expand=true",
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
        raise RuntimeError("Public SGA crop successor boundary changed")
    shutil.rmtree(READBACK_ROOT, ignore_errors=True)
    READBACK_ROOT.mkdir(parents=True)
    files: dict[str, dict[str, object]] = {}
    archives: dict[str, dict[str, object]] = {}
    try:
        for index, name in enumerate(sorted(entries, key=str.casefold), start=1):
            print(f"PUBLIC READBACK {index}/{len(entries)} {name}", flush=True)
            destination = (
                READBACK_ROOT / f"archive-{index:03d}.zip"
                if name in {ZIP_NAME, CONTROLS_NAME}
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
                raise RuntimeError(f"Public SGA crop mismatch: {name}")
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
        or int(archives[ZIP_NAME]["members"]) != EXPECTED_PACKAGE["files"]
        or len(
            [
                name
                for name in archives[ZIP_NAME]["member_identities"]
                if name.lower().endswith(".png")
            ]
        )
        != EXPECTED_PACKAGE["images"]
    ):
        raise RuntimeError("SGA crop successor public readback did not close")
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
        "added_files": [ZIP_NAME],
        "replaced_files": sorted(REPLACED_NAMES),
        "default_preview": record["files"].get("default_preview"),
        "latest_record": int(latest["id"]),
        "github": {
            "commit": github["commit"],
            "package_path": github["package_path"],
            "files_read_back": github["files_read_back"],
        },
        "source_crop_zip_members": EXPECTED_PACKAGE["files"],
        "source_crop_pngs": EXPECTED_PACKAGE["images"],
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
    markdown = "\n".join(
        [
            "# SGA7 lead-opened source-crop publication receipt",
            "",
            f"- Record: <https://zenodo.org/records/{record_id}>",
            f"- DOI: `{result['doi']}`",
            f"- Concept DOI: `{CONCEPT_DOI}`",
            f"- GitHub package commit: `{GITHUB_PACKAGE_COMMIT}`",
            f"- Public files: {len(files)} / {result['outer_bytes']:,} bytes",
            f"- Retained predecessor files: {len(retained)} / identity errors 0",
            f"- Source-crop ZIP: {EXPECTED_PACKAGE['files']} members, including {EXPECTED_PACKAGE['images']} PNGs / `{EXPECTED_ZIP[1]}`",
            f"- Default preview: `{DEFAULT_PREVIEW}`",
            "- Duplicate concept created: no",
            "- Active draft remaining: no",
            "",
            "The archive contains actual SGA7 I and SGA7 II scan-derived source",
            "pixels used by the lead, with page/crop/hash provenance. It does not",
            "contain target-reader screenshots or exact pixels already public.",
            "",
        ]
    )
    (RECEIPT_ROOT / f"{RECEIPT_TAG}_record_{record_id}.md").write_text(
        markdown, encoding="utf-8", newline="\n"
    )
    return result


def preflight() -> dict[str, object]:
    configure_prior()
    archive = build_zip()
    predecessor = load_predecessor_receipt()
    github = verify_github()
    controls = build_controls(archive, predecessor, github)
    token = base.find_token()
    session = base.make_session()
    prior.fetch_live(session, predecessor)
    prior.assert_no_untracked_draft(session, token)
    return {
        "status": "PASS_PREFLIGHT",
        "predecessor_record": PREDECESSOR_RECORD,
        "concept_doi": CONCEPT_DOI,
        "retained_files": len(expected_retained(predecessor)),
        "added_files": [ZIP_NAME],
        "replaced_files": sorted(REPLACED_NAMES),
        "final_files": FINAL_FILES,
        "default_preview": DEFAULT_PREVIEW,
        "github_commit": github["commit"],
        "source_crop_zip": {
            "bytes": archive["bytes"],
            "sha256": archive["sha256"],
            "members": archive["inventory"]["members"],
            "pngs": EXPECTED_PACKAGE["images"],
        },
        "controls_zip": {
            "bytes": controls["bytes"],
            "sha256": controls["sha256"],
            "members": controls["inventory"]["members"],
        },
        "duplicate_concept_created": False,
    }


def publish() -> dict[str, object]:
    configure_prior()
    archive = build_zip()
    predecessor = load_predecessor_receipt()
    github = verify_github()
    controls = build_controls(archive, predecessor, github)
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
        {ZIP_NAME: archive},
        controls,
        predecessor,
    )
    return public_readback(
        session,
        token,
        int(published["id"]),
        archive,
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
