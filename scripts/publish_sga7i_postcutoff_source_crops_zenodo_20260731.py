#!/usr/bin/env python3
"""Publish actual SGA7 I post-cutoff source crops under the existing SGA concept."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import shutil
import subprocess
import zipfile
from collections import Counter
from pathlib import Path, PurePosixPath

import publish_sga7ii_x_xvii_source_images_zenodo_20260731 as prior


base = prior.base
API = prior.API
PUBLICATION_DATE = "2026-07-31"
CONCEPT_DOI = "10.5281/zenodo.20410947"
PREDECESSOR_RECORD = 21_719_186
PREDECESSOR_DOI = "10.5281/zenodo.21719186"
PREDECESSOR_FILES = 79
PREDECESSOR_BYTES = 646_432_815
FINAL_FILES = 80
DEFAULT_PREVIEW = "00a_SGA1_English_Reader.pdf"
CONTROLS_NAME = "10z_SGA_Current_Release_Controls_20260730.zip"
VERSION = "2026-07-31 SGA7 I post-cutoff high-detail source crops"

REPO_ROOT = Path(__file__).resolve().parents[1]
DELTA_ROOT = REPO_ROOT / Path(
    "sources/sga/sga7i-highdetail-source-audit-visual-evidence-20260730/"
    "post-publication-delta-20260730-225251"
)
DELTA_CSV = DELTA_ROOT / "SGA7I_POST_PUBLICATION_VISUAL_EVIDENCE_DELTA.csv"
LEAD_INDEX = (
    REPO_ROOT
    / "sources/sga/sga7-lead-opened-source-crops-20260731/"
    "SGA7_LEAD_OPENED_SOURCE_CROP_INDEX.csv"
)
PACKAGE_REL = Path("sources/sga/sga7i-postcutoff-highdetail-source-crops-20260731")
PACKAGE_ROOT = REPO_ROOT / PACKAGE_REL
ZIP_NAME = "10h4_SGA7I_PostCutoff_HighDetail_Source_Crops_20260731.zip"
ZIP_PREFIX = "SGA7I_PostCutoff_HighDetail_Source_Crops_20260731"
TEMP_ROOT = REPO_ROOT / "tmp/zenodo/sga7i-postcutoff-source-crops-20260731"
ZIP_PATH = TEMP_ROOT / ZIP_NAME
CONTROLS_ROOT = TEMP_ROOT / "release-controls"
CONTROLS_ZIP = TEMP_ROOT / CONTROLS_NAME
READBACK_ROOT = TEMP_ROOT / "public-readback"
STATE_PATH = TEMP_ROOT / "draft_state.json"
RECEIPT_ROOT = REPO_ROOT / "manifests/published-zenodo"
RECEIPT_TAG = "20260731_sga7i_postcutoff_source_crops"
PREDECESSOR_RECEIPT = RECEIPT_ROOT / (
    "20260731_sga7ii_expose_xviii_wip_source_"
    "record_21719186_public_readback.json"
)
GITHUB_RECEIPT_ROOT = REPO_ROOT / "manifests/published-github"

PARENT_SCAN_SHA256 = (
    "9CD40FF06EB1E488AF385A56899D4F492492A06A1E2E3C0ED6876B82E3E3603F"
)
FULL_PAGE_VARIANT_IDS = {
    "SGA7I-POSTCUT-VIS-00033",
    "SGA7I-POSTCUT-VIS-00045",
    "SGA7I-POSTCUT-VIS-00117",
    "SGA7I-POSTCUT-VIS-00175",
    "SGA7I-POSTCUT-VIS-00241",
}
EXPECTED = {
    "delta_rows": 274,
    "lead_overlap_rows": 9,
    "full_page_variants": 5,
    "selected_images": 260,
    "selected_bytes": 24_829_245,
    "targeted_crop": 249,
    "routine_render": 9,
    "unknown": 2,
    "zip_members": 266,
    "manifest_rows": 264,
}
REPLACED_NAMES = {CONTROLS_NAME}

DESCRIPTION_ADDITION = (
    "<p><strong>Actual SGA7 I post-cutoff source crops:</strong> this "
    "successor adds one compact archive containing 260 scan-derived PNG "
    "regions used during source transcription and adjudication. These are "
    "actual pixels from the publicly available SGA7 I scan, not screenshots "
    "of a reconstructed reader and not a metadata-only substitute. The "
    "index binds each image to the parent-scan hash, source page and folio, "
    "dimensions, linked TeX unit, exact SHA-256, and recovered generation "
    "metadata. Nine exact pixels already public were deduplicated; five "
    "redundant whole-page or stretch variants were catalogued but omitted.</p>"
)
NOTES_ADDITION = (
    "<p>The post-cutoff crop archive corrects the earlier metadata-only "
    "disposition for this tranche by preserving the useful source pixels "
    "themselves. It is source-adjudication evidence, not a complete "
    "transcription, translation, proof, critical edition, accessibility "
    "certification, or new blanket license for the underlying French work. "
    "Existing readers and their browser-preview order are unchanged.</p>"
)

INDEX_FIELDS = [
    "visual_id",
    "archive_member",
    "original_filename",
    "bytes",
    "sha256",
    "width_px",
    "height_px",
    "color_mode",
    "image_format",
    "evidence_class",
    "pixel_scope",
    "parent_scan_title",
    "parent_pdf_sha256",
    "parent_pdf_pages",
    "parent_pdf_index_0based",
    "parent_pdf_physical_page_1based",
    "book_folio",
    "page_resolution_method",
    "page_resolution_confidence",
    "expose",
    "linked_tex_file",
    "linked_tex_sha256",
    "parent_page_rotation_deg",
    "parent_scan_width_px",
    "parent_scan_height_px",
    "parent_scan_effective_dpi_x",
    "parent_scan_effective_dpi_y",
    "bbox_fx0",
    "bbox_fy0",
    "bbox_fx1",
    "bbox_fy1",
    "generator_script",
    "generator_script_sha256",
    "generator_match_method",
    "generator_source_class",
    "qa_disposition",
    "read_count",
    "duplicate_instance_count",
    "publication_disposition",
]


def sha256_path(path: Path) -> str:
    return base.sha256_path(path)


def md5_path(path: Path) -> str:
    return base.md5_path(path)


def write_csv(path: Path, rows: list[dict[str, object]], fields: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def safe_member(name: str) -> bool:
    pure = PurePosixPath(name)
    return (
        name == name.replace("\\", "/")
        and not pure.is_absolute()
        and ".." not in pure.parts
        and not (len(name) > 1 and name[1] == ":")
    )


def resolve_rows(
    claude_current: Path, claude_history: Path
) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    roots = {"claude_current": claude_current, "claude_history": claude_history}
    for name, root in roots.items():
        if not root.is_dir():
            raise RuntimeError(f"Missing required {name} source root")
    delta = read_csv(DELTA_CSV)
    lead = read_csv(LEAD_INDEX)
    if len(delta) != EXPECTED["delta_rows"]:
        raise RuntimeError("SGA7 I post-cutoff delta row count changed")
    lead_hashes = {row["sha256"].upper() for row in lead}
    overlap = [row for row in delta if row["sha256"].upper() in lead_hashes]
    if len(overlap) != EXPECTED["lead_overlap_rows"]:
        raise RuntimeError("Lead-opened deduplication boundary changed")

    selected: list[dict[str, object]] = []
    routed: list[dict[str, object]] = []
    for row in delta:
        visual_id = row["visual_id"]
        digest = row["sha256"].upper()
        source = roots[row["root_id"]] / row["relative_path"]
        if Path(row["relative_path"]).name != row["relative_path"]:
            raise RuntimeError(f"Unsafe source filename: {row['relative_path']}")
        if not source.is_file():
            raise RuntimeError(f"Missing source pixel: {visual_id}")
        if (source.stat().st_size, sha256_path(source)) != (
            int(row["bytes"]),
            digest,
        ):
            raise RuntimeError(f"Source pixel identity mismatch: {visual_id}")
        if row["parent_pdf_sha256"].upper() != PARENT_SCAN_SHA256:
            raise RuntimeError(f"Parent scan identity changed: {visual_id}")

        if digest in lead_hashes:
            routed.append(
                {
                    "visual_id": visual_id,
                    "original_filename": row["relative_path"],
                    "bytes": int(row["bytes"]),
                    "sha256": digest,
                    "disposition": "deduplicated_exact_pixel_already_public",
                    "reason": "represented_in_10h3_lead_opened_source_crop_archive",
                }
            )
            continue
        if visual_id in FULL_PAGE_VARIANT_IDS:
            routed.append(
                {
                    "visual_id": visual_id,
                    "original_filename": row["relative_path"],
                    "bytes": int(row["bytes"]),
                    "sha256": digest,
                    "disposition": "catalogued_not_repacked",
                    "reason": "redundant_whole_page_or_stretch_variant_of_parent_scan",
                }
            )
            continue

        member = f"images/{visual_id}_{row['relative_path']}"
        public = {
            "visual_id": visual_id,
            "archive_member": member,
            "original_filename": row["relative_path"],
            "bytes": int(row["bytes"]),
            "sha256": digest,
            "width_px": int(row["width_px"]),
            "height_px": int(row["height_px"]),
            "color_mode": row["color_mode"],
            "image_format": row["image_format"],
            "evidence_class": row["evidence_class"],
            "pixel_scope": row["pixel_scope"],
            "parent_scan_title": "SGA 7 I public scan",
            "parent_pdf_sha256": row["parent_pdf_sha256"].upper(),
            "parent_pdf_pages": 540,
            "parent_pdf_index_0based": row["parent_pdf_index_0based"],
            "parent_pdf_physical_page_1based": row[
                "parent_pdf_physical_page_1based"
            ],
            "book_folio": row["book_folio"],
            "page_resolution_method": row["page_resolution_method"],
            "page_resolution_confidence": row["page_resolution_confidence"],
            "expose": row["expose"],
            "linked_tex_file": row["linked_tex_file"],
            "linked_tex_sha256": row["linked_tex_sha256"].upper(),
            "parent_page_rotation_deg": row["parent_page_rotation_deg"],
            "parent_scan_width_px": row["parent_scan_width_px"],
            "parent_scan_height_px": row["parent_scan_height_px"],
            "parent_scan_effective_dpi_x": row["parent_scan_effective_dpi_x"],
            "parent_scan_effective_dpi_y": row["parent_scan_effective_dpi_y"],
            "bbox_fx0": row["bbox_fx0"],
            "bbox_fy0": row["bbox_fy0"],
            "bbox_fx1": row["bbox_fx1"],
            "bbox_fy1": row["bbox_fy1"],
            "generator_script": row["generator_script"],
            "generator_script_sha256": row["generator_script_sha256"],
            "generator_match_method": row["generator_match_method"],
            "generator_source_class": row["generator_source_class"],
            "qa_disposition": row["qa_disposition"],
            "read_count": row["read_count"],
            "duplicate_instance_count": row["duplicate_instance_count"],
            "publication_disposition": "public_actual_source_pixel",
            "_source": source,
        }
        if not safe_member(member):
            raise RuntimeError(f"Unsafe archive member: {member}")
        selected.append(public)

    selected.sort(key=lambda row: str(row["visual_id"]))
    routed.sort(key=lambda row: str(row["visual_id"]))
    classes = Counter(str(row["evidence_class"]) for row in selected)
    if (
        len(selected) != EXPECTED["selected_images"]
        or sum(int(row["bytes"]) for row in selected)
        != EXPECTED["selected_bytes"]
        or len(routed) != EXPECTED["lead_overlap_rows"]
        + EXPECTED["full_page_variants"]
        or classes
        != Counter(
            {
                "targeted_crop": EXPECTED["targeted_crop"],
                "routine_render": EXPECTED["routine_render"],
                "unknown": EXPECTED["unknown"],
            }
        )
    ):
        raise RuntimeError("SGA7 I actual-pixel selection boundary changed")
    return selected, routed


def prepare_package(claude_current: Path, claude_history: Path) -> dict[str, object]:
    selected, routed = resolve_rows(claude_current, claude_history)
    PACKAGE_ROOT.mkdir(parents=True, exist_ok=True)
    readme = """# SGA7 I post-cutoff high-detail source crops

This archive publishes 260 actual scan-derived PNG regions created during SGA7
I source transcription and adjudication after the earlier public-inventory
cutoff. They are source pixels from the publicly available 540-page SGA7 I
scan, not screenshots of the reconstructed reader and not metadata-only
substitutes.

The package corrects the earlier metadata-only disposition for this tranche.
Nine exact pixels already present in the lead-opened public crop archive are
deduplicated. Five whole-page or stretch variants are catalogued but not
repacked because they duplicate the zoomable parent scan rather than preserve
a distinct targeted reading. Every other live pixel is included.

`SGA7I_POSTCUTOFF_SOURCE_CROP_INDEX.csv` records the exact image hash,
dimensions, parent-scan hash, source page and folio, linked TeX unit, recovered
crop/generator metadata, and QA disposition. Empty bounding-box fields mean
that the historical crop parameters were not recoverable; the exact pixel and
parent-page identity remain fixed.

These images are source-adjudication witnesses. They do not certify a complete
transcription, translation, proof, critical edition, accessibility status, or
every possible source reading.
"""
    rights = """# Provenance and rights

The PNGs are regions derived from the publicly available SGA7 I scan whose
540-page parent file has SHA-256
`9CD40FF06EB1E488AF385A56899D4F492492A06A1E2E3C0ED6876B82E3E3603F`.
They are republished as scholarly source-checking evidence with exact
page/hash provenance. They are not screenshots of a translated or recomposed
reader.

This package does not claim new ownership of the underlying French work or
grant a broader license over it. Attribution and any rights in the source work
remain with their respective holders. The project-created index, routing
ledger, and validation describe the evidence and do not alter that boundary.
"""
    (PACKAGE_ROOT / "README.md").write_text(readme, encoding="utf-8", newline="\n")
    (PACKAGE_ROOT / "RIGHTS_AND_PROVENANCE.md").write_text(
        rights, encoding="utf-8", newline="\n"
    )
    public_rows = [
        {field: row[field] for field in INDEX_FIELDS} for row in selected
    ]
    write_csv(
        PACKAGE_ROOT / "SGA7I_POSTCUTOFF_SOURCE_CROP_INDEX.csv",
        public_rows,
        INDEX_FIELDS,
    )
    routing_fields = [
        "visual_id",
        "original_filename",
        "bytes",
        "sha256",
        "disposition",
        "reason",
    ]
    write_csv(
        PACKAGE_ROOT / "DEDUPLICATION_AND_SELECTION.csv",
        routed,
        routing_fields,
    )

    member_rows: list[dict[str, object]] = []
    for row in selected:
        member_rows.append(
            {
                "relative_path": row["archive_member"],
                "bytes": row["bytes"],
                "sha256": row["sha256"],
                "release_role": "actual_source_crop_pixel",
            }
        )
    for name, role in (
        ("README.md", "scope_and_use"),
        ("RIGHTS_AND_PROVENANCE.md", "provenance_and_rights"),
        ("SGA7I_POSTCUTOFF_SOURCE_CROP_INDEX.csv", "image_index"),
        ("DEDUPLICATION_AND_SELECTION.csv", "routing_ledger"),
    ):
        path = PACKAGE_ROOT / name
        member_rows.append(
            {
                "relative_path": name,
                "bytes": path.stat().st_size,
                "sha256": sha256_path(path),
                "release_role": role,
            }
        )
    member_rows.sort(key=lambda row: str(row["relative_path"]).casefold())
    write_csv(
        PACKAGE_ROOT / "ZIP_MEMBER_SHA256SUMS.csv",
        member_rows,
        ["relative_path", "bytes", "sha256", "release_role"],
    )
    if len(member_rows) != EXPECTED["manifest_rows"]:
        raise RuntimeError("ZIP member manifest boundary changed")

    controls_to_scan = [
        PACKAGE_ROOT / "README.md",
        PACKAGE_ROOT / "RIGHTS_AND_PROVENANCE.md",
        PACKAGE_ROOT / "SGA7I_POSTCUTOFF_SOURCE_CROP_INDEX.csv",
        PACKAGE_ROOT / "DEDUPLICATION_AND_SELECTION.csv",
        PACKAGE_ROOT / "ZIP_MEMBER_SHA256SUMS.csv",
    ]
    forbidden = ("C:\\Users", "AppData\\Local\\Temp", ".codex", "thread_id")
    privacy_hits: list[str] = []
    for path in controls_to_scan:
        text = path.read_text(encoding="utf-8")
        for needle in forbidden:
            if needle.casefold() in text.casefold():
                privacy_hits.append(f"{path.name}:{needle}")
    validation = {
        "status": "PASS_READY_FOR_ACTUAL_PIXEL_PUBLICATION",
        "errors": [],
        "parent_scan_sha256": PARENT_SCAN_SHA256,
        "parent_scan_pages": 540,
        "delta_rows": len(read_csv(DELTA_CSV)),
        "selected_image_files": len(selected),
        "selected_image_bytes": sum(int(row["bytes"]) for row in selected),
        "selected_evidence_classes": dict(
            sorted(Counter(str(row["evidence_class"]) for row in selected).items())
        ),
        "deduplicated_exact_pixels_already_public": EXPECTED["lead_overlap_rows"],
        "catalogued_redundant_full_page_or_stretch_variants": EXPECTED[
            "full_page_variants"
        ],
        "zip_member_manifest_rows": len(member_rows),
        "expected_zip_members_including_manifest_and_validation": EXPECTED[
            "zip_members"
        ],
        "zip_member_manifest_sha256": sha256_path(
            PACKAGE_ROOT / "ZIP_MEMBER_SHA256SUMS.csv"
        ),
        "source_pixel_identity_errors": [],
        "privacy_hits": privacy_hits,
        "actual_source_pixels_included": True,
        "reader_pdf_screenshots_included": False,
        "metadata_only_substitution": False,
    }
    if privacy_hits:
        raise RuntimeError("Public crop controls contain private path material")
    base.save_json(PACKAGE_ROOT / "PACKAGE_VALIDATION.json", validation)
    files = sorted(path for path in PACKAGE_ROOT.iterdir() if path.is_file())
    return {
        "status": "PASS_PREPARED_GITHUB_METADATA_AND_ZENODO_MEMBER_CONTROLS",
        "package_path": PACKAGE_REL.as_posix(),
        "metadata_files": len(files),
        "metadata_bytes": sum(path.stat().st_size for path in files),
        "selected_images": len(selected),
        "selected_image_bytes": validation["selected_image_bytes"],
        "zip_members": EXPECTED["zip_members"],
        "manifest_sha256": validation["zip_member_manifest_sha256"],
        "validation_sha256": sha256_path(PACKAGE_ROOT / "PACKAGE_VALIDATION.json"),
    }


def build_zip(claude_current: Path, claude_history: Path) -> dict[str, object]:
    prepare_package(claude_current, claude_history)
    selected, _ = resolve_rows(claude_current, claude_history)
    TEMP_ROOT.mkdir(parents=True, exist_ok=True)
    ZIP_PATH.unlink(missing_ok=True)
    controls = sorted(path for path in PACKAGE_ROOT.iterdir() if path.is_file())
    with zipfile.ZipFile(
        ZIP_PATH,
        "w",
        compression=zipfile.ZIP_DEFLATED,
        compresslevel=9,
        allowZip64=True,
    ) as archive:
        for path in controls:
            member = f"{ZIP_PREFIX}/{path.name}"
            info = zipfile.ZipInfo(member, date_time=(2026, 7, 31, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            info.create_system = 3
            archive.writestr(info, path.read_bytes(), compresslevel=9)
        for row in selected:
            member = f"{ZIP_PREFIX}/{row['archive_member']}"
            info = zipfile.ZipInfo(member, date_time=(2026, 7, 31, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            info.create_system = 3
            archive.writestr(info, Path(row["_source"]).read_bytes(), compresslevel=9)
    inventory = prior.zip_inventory(ZIP_PATH)
    identities = inventory["member_identities"]
    manifest_rows = read_csv(PACKAGE_ROOT / "ZIP_MEMBER_SHA256SUMS.csv")
    manifested_names = {
        f"{ZIP_PREFIX}/{row['relative_path']}" for row in manifest_rows
    }
    self_excluded = {
        f"{ZIP_PREFIX}/ZIP_MEMBER_SHA256SUMS.csv",
        f"{ZIP_PREFIX}/PACKAGE_VALIDATION.json",
    }
    if (
        int(inventory["members"]) != EXPECTED["zip_members"]
        or len(
            [
                name
                for name in inventory["member_identities"]
                if name.lower().endswith(".png")
            ]
        )
        != EXPECTED["selected_images"]
        or not all(safe_member(name) for name in inventory["member_identities"])
        or manifested_names != set(identities) - self_excluded
    ):
        raise RuntimeError("Deterministic source-crop ZIP boundary changed")
    for row in manifest_rows:
        member = f"{ZIP_PREFIX}/{row['relative_path']}"
        if (
            int(identities[member]["bytes"]),
            str(identities[member]["sha256"]).upper(),
        ) != (int(row["bytes"]), row["sha256"].upper()):
            raise RuntimeError(f"ZIP member manifest mismatch: {member}")
    return {
        "path": ZIP_PATH,
        "bytes": ZIP_PATH.stat().st_size,
        "sha256": sha256_path(ZIP_PATH),
        "md5": md5_path(ZIP_PATH),
        "inventory": inventory,
    }


def verify_github(commit: str) -> tuple[dict[str, object], Path]:
    subprocess.check_call(
        ["git", "merge-base", "--is-ancestor", commit, "HEAD"], cwd=REPO_ROOT
    )
    remote = subprocess.check_output(
        ["git", "ls-remote", "github-write", "refs/heads/main"],
        cwd=REPO_ROOT,
        text=True,
    ).split()[0]
    if remote != commit:
        raise RuntimeError("GitHub package commit is not current public main")
    session = base.make_session()
    files = sorted(path for path in PACKAGE_ROOT.iterdir() if path.is_file())
    readback: list[dict[str, object]] = []
    for path in files:
        relative = path.relative_to(REPO_ROOT).as_posix()
        url = (
            "https://raw.githubusercontent.com/KokunoYumeto/"
            f"modern-latex-manuscripts/{commit}/{relative}"
        )
        response = base.check(session.get(url, timeout=(30, 300)), {200})
        data = response.content
        observed = (len(data), hashlib.sha256(data).hexdigest().upper())
        wanted = (path.stat().st_size, sha256_path(path))
        if observed != wanted:
            raise RuntimeError(f"GitHub raw mismatch: {relative}")
        readback.append(
            {
                "path": relative,
                "bytes": observed[0],
                "sha256": observed[1],
                "raw_url": url,
                "match": True,
            }
        )
    result = {
        "status": "PASS_GITHUB_PUBLIC_READBACK",
        "errors": [],
        "repository": "KokunoYumeto/modern-latex-manuscripts",
        "commit": commit,
        "package_path": PACKAGE_REL.as_posix(),
        "files_read_back": len(readback),
        "bytes_read_back": sum(int(row["bytes"]) for row in readback),
        "file_readback": readback,
    }
    receipt = GITHUB_RECEIPT_ROOT / (
        "20260731_sga7i_postcutoff_source_crops_"
        f"commit_{commit[:9]}_public_readback.json"
    )
    base.save_json(receipt, result)
    return result, receipt


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
    github_receipt: Path,
) -> dict[str, object]:
    shutil.rmtree(CONTROLS_ROOT, ignore_errors=True)
    CONTROLS_ROOT.mkdir(parents=True)
    retained = expected_retained(predecessor)
    readme = """# Current SGA release controls

The reader-facing order is unchanged: the one-click current-reader bundle is
first, cumulative English readers and masters follow, and SGA1 remains the
browser preview.

This successor adds one compact archive with 260 actual SGA7 I scan-derived
source crops created after the earlier public visual-inventory cutoff. Nine
exact pixels already public were deduplicated. Five redundant whole-page or
stretch variants remain catalogued but are not repacked. The actual useful
pixels are present; they are not replaced by a rights-blocked metadata ledger.

The archive is source-adjudication evidence, not a complete-transcription,
translation, mathematical-certification, critical-edition, accessibility, or
blanket-rights claim.
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
            "release_role": "actual_source_crop_pixels",
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
        "source_crop_zip_members": archive["inventory"]["members"],
        "source_crop_pngs": EXPECTED["selected_images"],
        "selected_source_pixel_bytes": EXPECTED["selected_bytes"],
        "actual_source_pixels_included": True,
        "metadata_only_substitution": False,
        "reader_pdf_screenshots_included": False,
    }
    base.save_json(CONTROLS_ROOT / "09b_RELEASE_VALIDATION.json", validation)
    copies = {
        "09c_SGA7I_CROP_PACKAGE_VALIDATION.json": PACKAGE_ROOT
        / "PACKAGE_VALIDATION.json",
        "09d_SGA7I_CROP_ZIP_MEMBER_SHA256SUMS.csv": PACKAGE_ROOT
        / "ZIP_MEMBER_SHA256SUMS.csv",
        "09e_SGA7I_POSTCUTOFF_SOURCE_CROP_INDEX.csv": PACKAGE_ROOT
        / "SGA7I_POSTCUTOFF_SOURCE_CROP_INDEX.csv",
        "09f_SGA7I_CROP_DEDUPLICATION_AND_SELECTION.csv": PACKAGE_ROOT
        / "DEDUPLICATION_AND_SELECTION.csv",
        "09g_SGA7I_CROP_GITHUB_PUBLIC_READBACK.json": github_receipt,
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
    archive: dict[str, object],
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
    expected = {**retained, ZIP_NAME: archive, CONTROLS_NAME: controls}
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
        or int(archives[ZIP_NAME]["members"]) != EXPECTED["zip_members"]
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
        "source_crop_zip_members": EXPECTED["zip_members"],
        "source_crop_pngs": EXPECTED["selected_images"],
        "source_crop_png_bytes": EXPECTED["selected_bytes"],
        "actual_source_pixels_included": True,
        "metadata_only_substitution": False,
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
            "# SGA7 I post-cutoff source-crop publication receipt",
            "",
            f"- Record: <https://zenodo.org/records/{record_id}>",
            f"- DOI: `{result['doi']}`",
            f"- Concept DOI: `{CONCEPT_DOI}`",
            f"- GitHub package commit: `{github['commit']}`",
            f"- Public files: {len(files)} / {result['outer_bytes']:,} bytes",
            f"- Retained predecessor files: {len(retained)} / identity errors 0",
            f"- Source-crop ZIP: {EXPECTED['zip_members']} members, including {EXPECTED['selected_images']} actual PNGs / `{archive['sha256']}`",
            f"- Actual source pixels: {EXPECTED['selected_bytes']:,} bytes",
            f"- Default preview: `{DEFAULT_PREVIEW}`",
            "- Duplicate concept created: no",
            "- Active draft remaining: no",
            "",
        ]
    )
    (RECEIPT_ROOT / f"{RECEIPT_TAG}_record_{record_id}.md").write_text(
        markdown, encoding="utf-8", newline="\n"
    )
    return result


def execute(
    claude_current: Path,
    claude_history: Path,
    github_commit: str,
    publish: bool,
) -> dict[str, object]:
    configure_prior()
    archive = build_zip(claude_current, claude_history)
    github, github_receipt = verify_github(github_commit)
    predecessor = load_predecessor_receipt()
    controls = build_controls(archive, predecessor, github, github_receipt)
    token = base.find_token()
    session = base.make_session()
    live = prior.fetch_live(session, predecessor)
    prior.assert_no_untracked_draft(session, token)
    if not publish:
        return {
            "status": "PASS_PREFLIGHT",
            "predecessor_record": PREDECESSOR_RECORD,
            "concept_doi": CONCEPT_DOI,
            "retained_files": len(expected_retained(predecessor)),
            "added_files": [ZIP_NAME],
            "replaced_files": sorted(REPLACED_NAMES),
            "final_files": FINAL_FILES,
            "default_preview": DEFAULT_PREVIEW,
            "github_commit": github_commit,
            "source_crop_zip": {
                "bytes": archive["bytes"],
                "sha256": archive["sha256"],
                "members": archive["inventory"]["members"],
                "pngs": EXPECTED["selected_images"],
            },
            "controls_zip": {
                "bytes": controls["bytes"],
                "sha256": controls["sha256"],
                "members": controls["inventory"]["members"],
            },
            "duplicate_concept_created": False,
        }
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
    result = public_readback(
        session,
        token,
        int(published["id"]),
        archive,
        controls,
        predecessor,
        github,
    )
    shutil.rmtree(TEMP_ROOT, ignore_errors=True)
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--claude-current-root", type=Path, required=True)
    parser.add_argument("--claude-history-root", type=Path, required=True)
    parser.add_argument("--prepare", action="store_true")
    parser.add_argument("--preflight", action="store_true")
    parser.add_argument("--github-commit")
    args = parser.parse_args()
    if args.prepare:
        result = prepare_package(args.claude_current_root, args.claude_history_root)
    else:
        if not args.github_commit:
            parser.error("--github-commit is required for preflight/publication")
        result = execute(
            args.claude_current_root,
            args.claude_history_root,
            args.github_commit,
            publish=not args.preflight,
        )
    print(json.dumps(result, indent=2, ensure_ascii=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
