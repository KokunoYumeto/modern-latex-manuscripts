#!/usr/bin/env python3
"""Publish the SGA3-through-XVI and SGA6 idx632-652 same-concept successor."""

from __future__ import annotations

import copy
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


PREDECESSOR_RECORD = 21633283
PREDECESSOR_DOI = "10.5281/zenodo.21633283"
CONCEPT_DOI = "10.5281/zenodo.20410947"
PUBLICATION_DATE = "2026-07-28"
VERSION = (
    "2026-07-28 SGA3 cumulative I-XIII plus XVI; "
    "SGA6 source-audit crops idx632-652"
)
GITHUB_COMMIT = "1f2ceba15eb92859a968bb58741c19b45f37df2c"
GITHUB_PACKAGE = (
    "sources/sga/"
    "sga3-english-current-progress-cumulative-through-xvi-20260728"
)
GITHUB_CROP_PACKAGE = (
    "sources/sga/"
    "sga6-ultradetail-source-audit-crops-coldreverify-idx632-652-20260728"
)

OLD_PDF = (
    "00c_SGA3_English_CurrentProgress_Cumulative_"
    "Through_XIII_XII_Gap_20260728.pdf"
)
OLD_TEX = (
    "02c_SGA3_English_CurrentProgress_Cumulative_"
    "Through_XIII_XII_Gap_20260728.tex"
)
OLD_SOURCE_ZIP = (
    "10c8_SGA3_CurrentProgress_Integration_Source_"
    "Through_XIII_XII_Gap_20260728.zip"
)
NEW_PDF = "00c_SGA3_English_CurrentProgress_Cumulative_Through_XVI_20260728.pdf"
NEW_TEX = "02c_SGA3_English_CurrentProgress_Cumulative_Through_XVI_20260728.tex"
NEW_SOURCE_ZIP = (
    "10c8_SGA3_CurrentProgress_Integration_Source_Through_XVI_20260728.zip"
)
CROP_TARGET_ZIP = (
    "10x_SGA6_SourceAudit_Targeted_UltraDetail_Crops_"
    "idx632_652_20260728.zip"
)
CROP_METADATA_ZIP = (
    "10y_SGA6_SourceAudit_Crop_Provenance_RightsBlocked_Metadata_"
    "idx632_652_20260728.zip"
)
HISTORY_ZIP = (
    "10c_SGA3_Previous_Public_Component_Readers_and_"
    "Source_Archives_Through_XI_20260728.zip"
)

README_NAME = "09_README_CURRENT_RELEASE.md"
MANIFEST_NAME = "09a_RELEASE_FILE_MANIFEST.csv"
VALIDATION_NAME = "09b_RELEASE_VALIDATION.json"
REPLACED_NAMES = {
    OLD_PDF,
    OLD_TEX,
    OLD_SOURCE_ZIP,
    README_NAME,
    MANIFEST_NAME,
    VALIDATION_NAME,
}

EXPECTED_PREDECESSOR_FILES = 63
EXPECTED_PREDECESSOR_MANIFEST_ROWS = 61
EXPECTED_FINAL_FILES = 65
EXPECTED_RETAINED_PREDECESSOR_FILES = 57
EXPECTED_UNRELATED_RETAINED_FILES = 56
EXPECTED_MANIFEST_ROWS = 63
EXPECTED_ZIP_ARCHIVES = 46
EXPECTED_ZIP_FILE_MEMBERS = 4_191
EXPECTED_ZIP_DIRECTORY_ENTRIES = 6
EXPECTED_ZIP_ALL_ENTRIES = 4_197
EXPECTED_ZIP_UNCOMPRESSED_BYTES = 402_137_942
EXPECTED_CURRENT_SOURCE_MEMBERS = 951
EXPECTED_CURRENT_SOURCE_UNCOMPRESSED_BYTES = 16_380_331

REPO_ROOT = SCRIPT_DIR.parent
PACKAGE_ROOT = (
    REPO_ROOT
    / "sources"
    / "sga"
    / "sga3-english-current-progress-cumulative-through-xvi-20260728"
)
CROP_PACKAGE_ROOT = (
    REPO_ROOT
    / "sources"
    / "sga"
    / "sga6-ultradetail-source-audit-crops-coldreverify-idx632-652-20260728"
)
CROP_ZIP_ROOT = Path(
    os.environ.get(
        "SGA6_IDX632_652_ZIP_ROOT",
        Path(os.environ["LOCALAPPDATA"])
        / "Temp"
        / "sga6_idx632_652_zips_20260728",
    )
)
RECEIPT_ROOT = REPO_ROOT / "manifests" / "published-zenodo"
PREDECESSOR_RECEIPT = (
    RECEIPT_ROOT
    / "20260728_sga3_cumulative_with_x_record_21633283_public_readback.json"
)
CONTROLS_ROOT = Path(os.environ["LOCALAPPDATA"]) / "Temp" / (
    "sga3_xvi_sga6_idx652_zenodo_controls"
)
READBACK_ROOT = Path(os.environ["LOCALAPPDATA"]) / "Temp" / (
    "sga3_xvi_sga6_idx652_zenodo_public_readback"
)
DRAFT_STATE = (
    RECEIPT_ROOT
    / "20260728_sga3_through_xvi_sga6_idx652_zenodo_draft_state.json"
)

PRIMARY_LOCAL_PATHS = {
    NEW_PDF: PACKAGE_ROOT / NEW_PDF,
    NEW_TEX: PACKAGE_ROOT / NEW_TEX,
    NEW_SOURCE_ZIP: PACKAGE_ROOT / NEW_SOURCE_ZIP,
    CROP_TARGET_ZIP: CROP_ZIP_ROOT / CROP_TARGET_ZIP,
    CROP_METADATA_ZIP: CROP_ZIP_ROOT / CROP_METADATA_ZIP,
}

PRIMARY_EXPECTED = {
    NEW_PDF: (
        5_760_459,
        "8D1DC78CDE64F22B76AD89150BEE73C48A1934EAECE0738B50AA413670CDDEAA",
    ),
    NEW_TEX: (
        18_526,
        "150F5D72C0F64CCB8DCCA32F24991CBDAF49F1867287BF5306934DB96C9300CA",
    ),
    NEW_SOURCE_ZIP: (
        12_112_999,
        "1C3F32FD6A6C9EB8D9EA5197B8D0FB08B35408DCCDF5291248012823B736741C",
    ),
    CROP_TARGET_ZIP: (
        13_542_194,
        "CBEB82308CD2AABE4AF64D4716C78A4709574EA9A1E7079D924FBCE6400B681A",
    ),
    CROP_METADATA_ZIP: (
        290_013,
        "C564791EC3B9104CA5D7D02065605B5D0968DB6F9857971B22F06C8E4924EE38",
    ),
}

NEW_MANIFEST_ROWS = {
    NEW_PDF: {
        "role": "english_reader",
        "provenance": (
            "current-progress cumulative SGA3 English reader through Expose "
            "XIII plus Expose XVI; GitHub commit " + GITHUB_COMMIT
        ),
        "status": (
            "preferred_current_progress_working_reader_sga3_incomplete_"
            "i_xiii_plus_xvi"
        ),
    },
    NEW_TEX: {
        "role": "english_master_tex",
        "provenance": (
            "direct editable integration master for the current-progress "
            "cumulative SGA3 reader through XVI; GitHub commit " + GITHUB_COMMIT
        ),
        "status": (
            "current_progress_working_source_sga3_incomplete_i_xiii_plus_xvi"
        ),
    },
    NEW_SOURCE_ZIP: {
        "role": "grouped_source_and_evidence",
        "provenance": (
            "951-member privacy-clean integration source closure for the "
            "current-progress SGA3 reader through XVI; GitHub commit "
            + GITHUB_COMMIT
        ),
        "status": (
            "current_progress_integration_source_sga3_incomplete_"
            "i_xiii_plus_xvi"
        ),
    },
    CROP_TARGET_ZIP: {
        "role": "visual_evidence",
        "provenance": (
            "156 high-detail source-audit crops actually opened during SGA6 "
            "cold re-verification, parent idx632-652; GitHub controls commit "
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
            "metadata for 156 selected crops, 11 generated unread tight "
            "alternatives, and 105 rights-blocked routine page bands; "
            "GitHub controls commit " + GITHUB_COMMIT
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
        "This same-concept compact successor preserves the reader-first SGA "
        "surface from version 10.5281/zenodo.21633283. Fifty-six unrelated "
        "files and the SGA3 component-history ZIP are retained byte-identically. "
        "Only the preferred SGA3 reader, direct editable integration master, "
        "current integration-source ZIP, and three release controls are "
        "replaced; two additive SGA6 source-audit crop archives are added."
    ),
    (
        "The preferred SGA3 current-progress reader has 950 A4 pages and "
        "contains the Editorial Notice, Introduction, Exposes I-XIII, and "
        "Expose XVI. It places an explicit gap leaf for Exposes XIV-XV and "
        "ends before Expose XVII. Exposes XVII-XXVI are absent. It is therefore "
        "a substantial working reader, not a complete SGA3 translation, "
        "critical edition, rights clearance, or mathematical certification."
    ),
    (
        "Exposes X, XII, XIII, and XVI are included as complete readable "
        "Loop-1 text-and-equation bodies. Four Expose-X and three Expose-XVI "
        "source-derived raster diagram placeholders remain for native Loop 2. "
        "Expose VII uses its latest readable repaired working body while final "
        "standalone diagram/reference certification remains tracked separately."
    ),
    (
        "The reader has 5,923 named destinations, 3,792 valid internal GoTo "
        "actions, zero broken internal actions, 62 embedded font resources, "
        "and no Type3 fonts. An isolated four-pass source-archive rebuild "
        "matched all 950 extracted-text pages, decompressed page-content "
        "streams, geometries, destinations, and internal actions."
    ),
    (
        "The additive SGA6 visual-evidence tranche contains 156 high-detail "
        "symbol, formula, punctuation, and diagram crops actually opened during "
        "cold source re-verification for parent indices 632-652. Eleven "
        "generated-but-unread tight alternatives and 105 routine page bands "
        "are represented by exact metadata only. The parent scan is not "
        "bundled. All 156 viewer-attachment correlations pass; three fresh "
        "replays disclose renderer-version geometry drift rather than claiming "
        "false pixel exactness."
    ),
    (
        "The controlling French source images and PDFs are not redistributed "
        "by the SGA3 integration archive. Pre-existing user-supplied OCR is a "
        "read-only locator or drafting witness and was not regenerated. Jacob "
        "C. Reinhold's jcreinhold/sga English lineage at revision "
        "e7a259f3f8608ad3edf9bf6eead3fd504dd2d23e is credited comparison and "
        "drafting material, not source authority; its author-declared CC BY "
        "4.0 applies only to that contribution. Rights in the underlying "
        "French works and scans remain with their holders. Machine-assisted "
        "contributors include OpenAI Codex / ChatGPT and Anthropic Claude "
        "under human direction."
    ),
]
DESCRIPTION_HTML = "\n".join(f"<p>{value}</p>" for value in DESCRIPTION_PARAGRAPHS)
NOTES_HTML = (
    "<p>Compact reader-first surface with 65 public files. English readers for "
    "SGA1 through SGA6 remain directly accessible, followed by French readers "
    "and primary editable TeX; recursive sources, QA, evidence, and predecessor "
    "objects are grouped into coherent ZIP archives. GitHub custody commit: "
    f"{GITHUB_COMMIT}.</p>"
)


def verify_zip(path: Path, expected_files: int, expected_dirs: int, expected_bytes: int) -> None:
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

    verify_zip(
        PRIMARY_LOCAL_PATHS[NEW_SOURCE_ZIP],
        EXPECTED_CURRENT_SOURCE_MEMBERS,
        0,
        EXPECTED_CURRENT_SOURCE_UNCOMPRESSED_BYTES,
    )
    verify_zip(PRIMARY_LOCAL_PATHS[CROP_TARGET_ZIP], 161, 0, 13_515_774)
    verify_zip(PRIMARY_LOCAL_PATHS[CROP_METADATA_ZIP], 6, 0, 288_665)
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
preserves all unrelated SGA files and the existing SGA3 component-history ZIP
byte-for-byte. It replaces only the preferred SGA3 cumulative reader, its
direct editable integration master, its current source ZIP, and the three
release controls. It adds one targeted SGA6 crop ZIP and one provenance/rights
metadata ZIP. The reserved successor record is {draft_id}.

## Preferred SGA3 reading surface

`{NEW_PDF}` is a 950-page current-progress English working reader containing:

- Editorial Notice and Introduction;
- Exposes I-XIII;
- complete current Loop-1 Expose XVI;
- an explicit gap leaf for Exposes XIV-XV; and
- a visible hard boundary before Expose XVII.

Exposes XVII-XXVI are absent. This is not complete SGA3, a critical edition,
rights clearance, or mathematical certification.

Exposes X, XII, XIII, and XVI are preserved because their complete readable
Loop-1 bodies now exist. Four Expose-X and three Expose-XVI raster diagram
placeholders remain for native Loop 2. Expose VII uses the latest readable
repaired working body while final standalone diagram/reference certification
remains separate.

## Reader checks

- 950 A4 pages;
- 5,923 named destinations;
- 3,792 valid internal GoTo actions;
- zero broken internal GoTo actions;
- 62 embedded font resources and zero Type3 fonts; and
- isolated four-pass source-archive rebuild equality for all 950 extracted
  text pages, decompressed content streams, geometries, destinations, and links.

The current source ZIP has 951 exact file members and passes CRC, identity, and
privacy closure. The unchanged SGA3 history ZIP keeps older component and
predecessor objects available without crowding the reader-first surface.

## SGA6 source-audit crops

`{CROP_TARGET_ZIP}` contains 156 high-detail crops actually opened during SGA6
cold source re-verification for parent indices 632-652. The companion metadata
ZIP records those selected crops plus 11 generated-but-unread alternatives and
105 rights-blocked routine page bands. The parent scan and routine band pixels
are not bundled. This is sparse provenance and QA evidence, not transcription,
translation, mathematical, completeness, or critical-edition certification.

## Authority and rights

Polo-Gille source PDFs control SGA3 French text, formulas, numbering, notes, and
diagram appearance. They are not redistributed in the integration archive.
Pre-existing user-supplied OCR was consulted read-only as locator and drafting
assistance only; it was not regenerated. Jacob C. Reinhold's
`jcreinhold/sga` English Markdown at commit
`e7a259f3f8608ad3edf9bf6eead3fd504dd2d23e` is credited comparison and drafting
lineage, not source authority. Its stated CC BY 4.0 applies only to that
contribution. No blanket license or transfer of rights in the underlying
French works, scans, comparison sources, or package as a whole is asserted.

Machine-assisted contributors include OpenAI Codex / ChatGPT and Anthropic
Claude under human direction. GitHub custody:

- `https://github.com/KokunoYumeto/modern-latex-manuscripts/tree/{GITHUB_COMMIT}/{GITHUB_PACKAGE}`
- `https://github.com/KokunoYumeto/modern-latex-manuscripts/tree/{GITHUB_COMMIT}/{GITHUB_CROP_PACKAGE}`
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
        if name in {OLD_PDF, OLD_TEX, OLD_SOURCE_ZIP, README_NAME}:
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
        "new_or_replacement_files": sorted(
            {
                NEW_PDF,
                NEW_TEX,
                NEW_SOURCE_ZIP,
                CROP_TARGET_ZIP,
                CROP_METADATA_ZIP,
                README_NAME,
                MANIFEST_NAME,
                VALIDATION_NAME,
            },
            key=str.casefold,
        ),
        "final_public_file_count": EXPECTED_FINAL_FILES,
        "release_manifest": {
            "rows": EXPECTED_MANIFEST_ROWS,
            "bytes": manifest_identity["bytes"],
            "sha256": manifest_identity["sha256"],
        },
        "default_preview": base.DEFAULT_PREVIEW,
        "github": {
            "commit": GITHUB_COMMIT,
            "package_paths": [GITHUB_PACKAGE, GITHUB_CROP_PACKAGE],
            "anonymous_readback_files": 24,
            "status": "PASS",
        },
        "sga3_reader": {
            "scope": (
                "Editorial Notice, Introduction, Exposes I-XIII, and Expose XVI"
            ),
            "explicit_gap": "Exposes XIV-XV",
            "absent_after_boundary": "Exposes XVII-XXVI",
            "pages": 950,
            "bytes": primary_local[NEW_PDF]["bytes"],
            "sha256": primary_local[NEW_PDF]["sha256"],
            "named_destinations": 5_923,
            "valid_internal_goto": 3_792,
            "broken_internal_goto": 0,
            "embedded_font_resources": 62,
            "type3_fonts": 0,
            "isolated_rebuild_text_content_geometry_links_exact": True,
        },
        "current_source_zip": {
            "filename": NEW_SOURCE_ZIP,
            "members": EXPECTED_CURRENT_SOURCE_MEMBERS,
            "uncompressed_bytes": EXPECTED_CURRENT_SOURCE_UNCOMPRESSED_BYTES,
            "sha256": primary_local[NEW_SOURCE_ZIP]["sha256"],
            "privacy_hits": 0,
        },
        "sga6_crop_tranche": {
            "parent_indices": "632-652",
            "audit_entries": "1384-1404",
            "selected_opened_images": 156,
            "selected_image_bytes": 13_304_384,
            "generated_unread_metadata_rows": 11,
            "rights_blocked_page_band_rows": 105,
            "viewer_attachment_correlations_pass": 156,
            "target_zip_sha256": primary_local[CROP_TARGET_ZIP]["sha256"],
            "metadata_zip_sha256": primary_local[CROP_METADATA_ZIP]["sha256"],
        },
        "history_zip": {
            "filename": HISTORY_ZIP,
            "bytes": predecessor_identities[HISTORY_ZIP]["bytes"],
            "sha256": predecessor_identities[HISTORY_ZIP]["sha256"],
            "retained_byte_identically": True,
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
    "OLD_PDF": OLD_PDF,
    "OLD_TEX": OLD_TEX,
    "OLD_SOURCE_ZIP": OLD_SOURCE_ZIP,
    "NEW_PDF": NEW_PDF,
    "NEW_TEX": NEW_TEX,
    "NEW_SOURCE_ZIP": NEW_SOURCE_ZIP,
    "HISTORY_ZIP": HISTORY_ZIP,
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
    "EXPECTED_CURRENT_SOURCE_MEMBERS": EXPECTED_CURRENT_SOURCE_MEMBERS,
    "EXPECTED_CURRENT_SOURCE_UNCOMPRESSED_BYTES": (
        EXPECTED_CURRENT_SOURCE_UNCOMPRESSED_BYTES
    ),
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
