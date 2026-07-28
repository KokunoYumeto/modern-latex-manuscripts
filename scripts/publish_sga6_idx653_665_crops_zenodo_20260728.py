#!/usr/bin/env python3
"""Add the SGA6 idx653-665 crop tranche to the existing compact SGA record."""

from __future__ import annotations

import csv
import importlib.util
import io
import json
import os
import shutil
import zipfile
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
BASE_PATH = SCRIPT_DIR / "publish_sga3_cumulative_with_x_zenodo_20260728.py"
SPEC = importlib.util.spec_from_file_location("sga_successor_base", BASE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("Unable to load the established SGA successor workflow")
base = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(base)


PREDECESSOR_RECORD = 21635827
PREDECESSOR_DOI = "10.5281/zenodo.21635827"
CONCEPT_DOI = "10.5281/zenodo.20410947"
PUBLICATION_DATE = "2026-07-28"
VERSION = (
    "2026-07-28 SGA3 current-progress cumulative through XXII snapshot; "
    "SGA6 source-audit crops through idx665"
)
GITHUB_COMMIT = "24dac3eb60a10052f843014aab0bf934df24e79e"
GITHUB_PACKAGE = (
    "sources/sga/"
    "sga6-ultradetail-source-audit-crops-coldreverify-idx653-665-20260728"
)

CROP_TARGET_ZIP = (
    "10x_SGA6_SourceAudit_Targeted_UltraDetail_Crops_"
    "idx653_665_20260728.zip"
)
CROP_METADATA_ZIP = (
    "10y_SGA6_SourceAudit_Crop_Provenance_RightsBlocked_Metadata_"
    "idx653_665_20260728.zip"
)
README_NAME = "09_README_CURRENT_RELEASE.md"
MANIFEST_NAME = "09a_RELEASE_FILE_MANIFEST.csv"
VALIDATION_NAME = "09b_RELEASE_VALIDATION.json"
REPLACED_NAMES = {README_NAME, MANIFEST_NAME, VALIDATION_NAME}

EXPECTED_PREDECESSOR_FILES = 65
EXPECTED_PREDECESSOR_MANIFEST_ROWS = 63
EXPECTED_FINAL_FILES = 67
EXPECTED_RETAINED_PREDECESSOR_FILES = 62
EXPECTED_UNRELATED_RETAINED_FILES = 62
EXPECTED_MANIFEST_ROWS = 65
EXPECTED_ZIP_ARCHIVES = 48
EXPECTED_ZIP_FILE_MEMBERS = 4_319
EXPECTED_ZIP_DIRECTORY_ENTRIES = 6
EXPECTED_ZIP_ALL_ENTRIES = 4_325
EXPECTED_ZIP_UNCOMPRESSED_BYTES = 407_126_465

REPO_ROOT = SCRIPT_DIR.parent
CROP_PACKAGE_ROOT = (
    REPO_ROOT
    / "sources"
    / "sga"
    / "sga6-ultradetail-source-audit-crops-coldreverify-idx653-665-20260728"
)
CROP_ZIP_ROOT = Path(
    os.environ.get(
        "SGA6_IDX653_665_ZIP_ROOT",
        Path(os.environ["LOCALAPPDATA"])
        / "Temp"
        / "sga6_idx653_665_release_zips_20260728",
    )
)
RECEIPT_ROOT = REPO_ROOT / "manifests" / "published-zenodo"
PREDECESSOR_RECEIPT = (
    RECEIPT_ROOT
    / "20260728_sga3_cumulative_with_x_record_21635827_public_readback.json"
)
CONTROLS_ROOT = (
    Path(os.environ["LOCALAPPDATA"])
    / "Temp"
    / "sga6_idx653_665_zenodo_controls"
)
READBACK_ROOT = (
    Path(os.environ["LOCALAPPDATA"])
    / "Temp"
    / "sga6_idx653_665_zenodo_public_readback"
)
DRAFT_STATE = (
    RECEIPT_ROOT
    / "20260728_sga6_idx653_665_zenodo_draft_state.json"
)

PRIMARY_LOCAL_PATHS = {
    CROP_TARGET_ZIP: CROP_ZIP_ROOT / CROP_TARGET_ZIP,
    CROP_METADATA_ZIP: CROP_ZIP_ROOT / CROP_METADATA_ZIP,
}
PRIMARY_EXPECTED = {
    CROP_TARGET_ZIP: (
        3_274_639,
        "4387449B9612FBB7FF670B3BF01C05A7626D70A662E06098A813F744A5983C34",
    ),
    CROP_METADATA_ZIP: (
        163_153,
        "A3A21B442991B3FD8822A2B76DF5A6D10EEED354E0C58FC253F65FDA81D231E7",
    ),
}
NEW_MANIFEST_ROWS = {
    CROP_TARGET_ZIP: {
        "role": "visual_evidence",
        "provenance": (
            "68 high-detail source-audit crops actually opened during SGA6 "
            "cold re-verification, parent idx653-665; GitHub controls commit "
            + GITHUB_COMMIT
        ),
        "status": (
            "sparse_targeted_source_audit_evidence_no_translation_"
            "certification_no_license_grant"
        ),
    },
    CROP_METADATA_ZIP: {
        "role": "provenance_and_rights_blocked_metadata",
        "provenance": (
            "metadata for 68 selected crops, 13 generated unread tight "
            "alternatives, and 65 rights-blocked routine page bands; "
            "GitHub controls commit "
            + GITHUB_COMMIT
        ),
        "status": (
            "public_provenance_metadata_with_routine_scan_pixels_withheld"
        ),
    },
    README_NAME: {
        "role": "manifest_status",
        "provenance": (
            "current compact same-concept release note; GitHub commit "
            + GITHUB_COMMIT
        ),
        "status": "current_release_control",
    },
}

DESCRIPTION_PARAGRAPHS = [
    (
        "This same-concept compact successor preserves all 62 non-control "
        "files from version 10.5281/zenodo.21635827 byte-identically, including "
        "the preferred 1,100-page SGA3 current-progress cumulative reader. It "
        "adds two SGA6 source-audit evidence archives and refreshes only the "
        "three release controls."
    ),
    (
        "The targeted archive contains 68 symbol-, formula-, punctuation-, "
        "prime-mark-, overline-, diagram-label-, and emphasis-level crops "
        "actually opened during the SGA6 cold source re-verification for "
        "parent indices 653-665. Every selected source PNG is correlated to "
        "the viewer attachment returned for its recorded inspection event. "
        "A separate replay independently verified all 68 dimensions."
    ),
    (
        "The companion metadata archive records the selected crops plus 13 "
        "generated-but-unread tight alternatives and 65 routine full-width "
        "page bands whose pixels are withheld. It binds the parent hash, "
        "page, fractional bounding box, dimensions, computational DPI, "
        "processing profile, linked TeX object, audit entry, and QA "
        "disposition. The parent scan is not redistributed."
    ),
    (
        "This is sparse visual provenance and QA evidence, not certification "
        "of the French transcription, English translation, mathematics, "
        "completeness, rights, or critical-edition status. Rights in the "
        "underlying French work and scan remain with their holders. "
        "Machine-assisted contributors include OpenAI Codex / ChatGPT and "
        "Anthropic Claude under human direction."
    ),
]
DESCRIPTION_HTML = "\n".join(f"<p>{value}</p>" for value in DESCRIPTION_PARAGRAPHS)
NOTES_HTML = (
    "<p>Compact reader-first surface with 67 public files. The preferred SGA3 "
    "reader and all other non-control predecessor files remain byte-identical. "
    "The new SGA6 evidence is grouped into two ZIPs rather than exposed as "
    "loose files. GitHub custody commit: "
    f"{GITHUB_COMMIT}.</p>"
)


def verify_zip(
    path: Path,
    expected_files: int,
    expected_dirs: int,
    expected_bytes: int,
) -> None:
    files = 0
    directories = 0
    uncompressed = 0
    with zipfile.ZipFile(path, "r") as archive:
        bad = archive.testzip()
        if bad is not None:
            raise RuntimeError(f"ZIP CRC failure {path.name}: {bad}")
        names = archive.namelist()
        if len(names) != len(set(names)):
            raise RuntimeError(f"Duplicate ZIP member: {path.name}")
        for info in archive.infolist():
            base.safe_zip_name(info.filename)
            if info.is_dir():
                directories += 1
            else:
                files += 1
                uncompressed += info.file_size
    observed = (files, directories, uncompressed)
    expected = (expected_files, expected_dirs, expected_bytes)
    if observed != expected:
        raise RuntimeError(
            f"ZIP boundary mismatch {path.name}: {observed} != {expected}"
        )


def verify_primary_local_files() -> dict[str, dict]:
    result: dict[str, dict] = {}
    for name, path in PRIMARY_LOCAL_PATHS.items():
        if not path.is_file():
            raise FileNotFoundError(path)
        identity = {
            "path": path,
            "bytes": path.stat().st_size,
            "sha256": base.sha256_file(path),
            "md5": base.md5_file(path),
        }
        if (identity["bytes"], identity["sha256"]) != PRIMARY_EXPECTED[name]:
            raise RuntimeError(f"Primary local identity mismatch: {name}")
        result[name] = identity
    verify_zip(PRIMARY_LOCAL_PATHS[CROP_TARGET_ZIP], 73, 0, 3_262_409)
    verify_zip(PRIMARY_LOCAL_PATHS[CROP_METADATA_ZIP], 6, 0, 161_805)
    return result


def fetch_predecessor_manifest(
    session, predecessor: dict, receipt: dict
) -> list[dict[str, str]]:
    entry = base.entries_map(predecessor)[MANIFEST_NAME]
    response = base.check(
        session.get(entry["links"]["content"], timeout=(30, 180)),
        {200},
    )
    content = response.content
    wanted = receipt["files"][MANIFEST_NAME]
    if (
        len(content),
        base.hashlib.sha256(content).hexdigest().upper(),
    ) != (
        int(wanted["bytes"]),
        wanted["sha256"].upper(),
    ):
        raise RuntimeError("Predecessor release-manifest readback mismatch")
    rows = list(
        csv.DictReader(io.StringIO(content.decode("utf-8-sig"), newline=""))
    )
    if len(rows) != EXPECTED_PREDECESSOR_MANIFEST_ROWS:
        raise RuntimeError("Unexpected predecessor release-manifest row count")
    return rows


def readme_text(draft_id: int) -> str:
    return f"""# Current compact SGA release

This is a same-concept successor to Zenodo record {PREDECESSOR_RECORD}. It
preserves all 62 non-control predecessor files byte-for-byte, including the
preferred SGA3 current-progress cumulative reader through the XXII snapshot.
Only the three release controls are replaced. The reserved successor record is
{draft_id}.

## SGA6 source-audit evidence through idx665

`{CROP_TARGET_ZIP}` contains 68 high-detail crops actually opened during the
SGA6 cold source re-verification for parent indices 653-665 / audit entries
1405-1417. These are the symbol-, formula-, punctuation-, prime-mark-,
overline-, diagram-label-, and emphasis-level crops used to resolve source
readings, not redundant page renders.

`{CROP_METADATA_ZIP}` records exact provenance for those selected crops plus
13 generated-but-unread alternatives and 65 routine full-width page bands.
The routine pixels are rights-blocked and withheld; their hashes, dimensions,
page mappings, bounding boxes, render profiles, linked TeX object, and QA
dispositions remain public. The parent scan is not bundled.

Every selected crop has one recorded viewer-open event and an exact attachment
correlation. Controlled replay recovered all dynamic generator coordinates;
all 30 replayed generator outputs matched the original source crops exactly.
An independent release replay confirmed 68/68 dimensions, all ZIP members, all
metadata-only source identities, the 13-row audit boundary, and zero public
privacy hits.

## Claim boundary

This is sparse visual provenance and QA evidence. It does not certify the
French transcription, English translation, mathematics, completeness,
critical-edition status, or rights. Rights in the underlying French work and
scan remain with their holders; no blanket license or rights transfer is
asserted.

Machine-assisted contributors include OpenAI Codex / ChatGPT and Anthropic
Claude under human direction. GitHub custody:

`https://github.com/KokunoYumeto/modern-latex-manuscripts/tree/{GITHUB_COMMIT}/{GITHUB_PACKAGE}`
"""


def generate_controls(
    draft_id: int,
    predecessor_rows: list[dict[str, str]],
    predecessor_identities: dict[str, dict],
    primary_local: dict[str, dict],
) -> dict[str, dict]:
    if CONTROLS_ROOT.exists():
        resolved = CONTROLS_ROOT.resolve()
        temp_root = Path(os.environ["LOCALAPPDATA"]).resolve() / "Temp"
        if temp_root not in resolved.parents:
            raise RuntimeError("Refusing to replace controls outside local temp")
        shutil.rmtree(CONTROLS_ROOT)
    CONTROLS_ROOT.mkdir(parents=True)

    readme_path = CONTROLS_ROOT / README_NAME
    base.write_text(readme_path, readme_text(draft_id))
    readme_identity = {
        "path": readme_path,
        "bytes": readme_path.stat().st_size,
        "sha256": base.sha256_file(readme_path),
        "md5": base.md5_file(readme_path),
    }

    retained_rows: list[dict[str, str]] = []
    for row in predecessor_rows:
        name = row["filename"]
        if name == README_NAME:
            continue
        if name in REPLACED_NAMES:
            raise RuntimeError(f"Unexpected replaced control row: {name}")
        identity = predecessor_identities[name]
        if (int(row["bytes"]), row["sha256"].upper()) != (
            identity["bytes"],
            identity["sha256"],
        ):
            raise RuntimeError(f"Retained manifest identity mismatch: {name}")
        retained_rows.append(dict(row))

    new_local = dict(primary_local)
    new_local[README_NAME] = readme_identity
    for name in sorted(new_local, key=str.casefold):
        metadata = NEW_MANIFEST_ROWS[name]
        identity = new_local[name]
        retained_rows.append(
            {
                "filename": name,
                "bytes": str(identity["bytes"]),
                "sha256": identity["sha256"],
                "role": metadata["role"],
                "provenance": metadata["provenance"],
                "status": metadata["status"],
            }
        )
    retained_rows.sort(key=lambda row: row["filename"].casefold())
    if len(retained_rows) != EXPECTED_MANIFEST_ROWS:
        raise RuntimeError(
            f"Expected {EXPECTED_MANIFEST_ROWS} rows, got {len(retained_rows)}"
        )
    if len({row["filename"] for row in retained_rows}) != len(retained_rows):
        raise RuntimeError("Generated release manifest has duplicate filenames")

    manifest_path = CONTROLS_ROOT / MANIFEST_NAME
    with manifest_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=(
                "filename",
                "bytes",
                "sha256",
                "role",
                "provenance",
                "status",
            ),
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(retained_rows)
    manifest_identity = {
        "path": manifest_path,
        "bytes": manifest_path.stat().st_size,
        "sha256": base.sha256_file(manifest_path),
        "md5": base.md5_file(manifest_path),
    }

    validation = {
        "status": "PASS_READY_FOR_ONE_SAME_CONCEPT_SUCCESSOR",
        "errors": [],
        "concept_doi": CONCEPT_DOI,
        "predecessor_record": PREDECESSOR_RECORD,
        "predecessor_doi": PREDECESSOR_DOI,
        "reserved_successor_record": draft_id,
        "release_policy": (
            "one same-concept compact successor; no duplicate concept or draft"
        ),
        "retained_predecessor_files": EXPECTED_RETAINED_PREDECESSOR_FILES,
        "retained_unrelated_files": EXPECTED_UNRELATED_RETAINED_FILES,
        "replaced_files": sorted(REPLACED_NAMES, key=str.casefold),
        "new_files": [CROP_TARGET_ZIP, CROP_METADATA_ZIP],
        "final_public_file_count": EXPECTED_FINAL_FILES,
        "release_manifest": {
            "rows": EXPECTED_MANIFEST_ROWS,
            "bytes": manifest_identity["bytes"],
            "sha256": manifest_identity["sha256"],
        },
        "default_preview": base.DEFAULT_PREVIEW,
        "github": {
            "commit": GITHUB_COMMIT,
            "package_path": GITHUB_PACKAGE,
            "status": "PASS",
        },
        "sga6_crop_tranche": {
            "parent_indices": "653-665",
            "audit_entries": "1405-1417",
            "selected_opened_images": 68,
            "selected_image_bytes": 3_148_724,
            "generated_unread_metadata_rows": 13,
            "rights_blocked_page_band_rows": 65,
            "rights_blocked_page_band_bytes": 14_631_063,
            "viewer_attachment_correlations_pass": 68,
            "runtime_replayed_generator_outputs_exact": 30,
            "target_zip_sha256": primary_local[CROP_TARGET_ZIP]["sha256"],
            "metadata_zip_sha256": primary_local[CROP_METADATA_ZIP]["sha256"],
        },
        "zip_surface_expected": {
            "archives": EXPECTED_ZIP_ARCHIVES,
            "file_members": EXPECTED_ZIP_FILE_MEMBERS,
            "directory_entries": EXPECTED_ZIP_DIRECTORY_ENTRIES,
            "all_entries": EXPECTED_ZIP_ALL_ENTRIES,
            "uncompressed_bytes": EXPECTED_ZIP_UNCOMPRESSED_BYTES,
        },
        "privacy_hits": [],
        "new_license_grant": False,
    }
    validation_path = CONTROLS_ROOT / VALIDATION_NAME
    base.save_json(validation_path, validation)
    validation_identity = {
        "path": validation_path,
        "bytes": validation_path.stat().st_size,
        "sha256": base.sha256_file(validation_path),
        "md5": base.md5_file(validation_path),
    }
    result = dict(new_local)
    result[MANIFEST_NAME] = manifest_identity
    result[VALIDATION_NAME] = validation_identity
    return result


for name, value in {
    "CONCEPT_DOI": CONCEPT_DOI,
    "PREDECESSOR_RECORD": PREDECESSOR_RECORD,
    "PREDECESSOR_DOI": PREDECESSOR_DOI,
    "PUBLICATION_DATE": PUBLICATION_DATE,
    "VERSION": VERSION,
    "GITHUB_COMMIT": GITHUB_COMMIT,
    "GITHUB_PACKAGE": GITHUB_PACKAGE,
    "README_NAME": README_NAME,
    "MANIFEST_NAME": MANIFEST_NAME,
    "VALIDATION_NAME": VALIDATION_NAME,
    "REPLACED_NAMES": REPLACED_NAMES,
    "EXPECTED_PREDECESSOR_FILES": EXPECTED_PREDECESSOR_FILES,
    "EXPECTED_FINAL_FILES": EXPECTED_FINAL_FILES,
    "EXPECTED_RETAINED_PREDECESSOR_FILES": EXPECTED_RETAINED_PREDECESSOR_FILES,
    "EXPECTED_UNRELATED_RETAINED_FILES": EXPECTED_UNRELATED_RETAINED_FILES,
    "EXPECTED_MANIFEST_ROWS": EXPECTED_MANIFEST_ROWS,
    "EXPECTED_ZIP_ARCHIVES": EXPECTED_ZIP_ARCHIVES,
    "EXPECTED_ZIP_FILE_MEMBERS": EXPECTED_ZIP_FILE_MEMBERS,
    "EXPECTED_ZIP_DIRECTORY_ENTRIES": EXPECTED_ZIP_DIRECTORY_ENTRIES,
    "EXPECTED_ZIP_ALL_ENTRIES": EXPECTED_ZIP_ALL_ENTRIES,
    "EXPECTED_ZIP_UNCOMPRESSED_BYTES": EXPECTED_ZIP_UNCOMPRESSED_BYTES,
    "RECEIPT_ROOT": RECEIPT_ROOT,
    "PREDECESSOR_RECEIPT": PREDECESSOR_RECEIPT,
    "CONTROLS_ROOT": CONTROLS_ROOT,
    "READBACK_ROOT": READBACK_ROOT,
    "DRAFT_STATE": DRAFT_STATE,
    "PRIMARY_LOCAL_PATHS": PRIMARY_LOCAL_PATHS,
    "NEW_MANIFEST_ROWS": NEW_MANIFEST_ROWS,
    "DESCRIPTION_HTML": DESCRIPTION_HTML,
    "NOTES_HTML": NOTES_HTML,
}.items():
    setattr(base, name, value)

base.verify_primary_local_files = verify_primary_local_files
base.fetch_predecessor_manifest = fetch_predecessor_manifest
base.readme_text = readme_text
base.generate_controls = generate_controls


if __name__ == "__main__":
    base.main()
