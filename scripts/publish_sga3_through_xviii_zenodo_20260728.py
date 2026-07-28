#!/usr/bin/env python3
"""Publish the SGA3-through-XVIII same-concept successor."""

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


PREDECESSOR_RECORD = 21634000
PREDECESSOR_DOI = "10.5281/zenodo.21634000"
CONCEPT_DOI = "10.5281/zenodo.20410947"
PUBLICATION_DATE = "2026-07-28"
VERSION = "2026-07-28 SGA3 cumulative I-XIV, XVI, and XVIII"
GITHUB_COMMIT = "9245278d0e8fbcf5abd9f162b971f21bae17552a"
GITHUB_PACKAGE = (
    "sources/sga/"
    "sga3-english-current-progress-cumulative-through-xviii-20260728"
)

OLD_PDF = (
    "00c_SGA3_English_CurrentProgress_Cumulative_Through_XVI_20260728.pdf"
)
OLD_TEX = (
    "02c_SGA3_English_CurrentProgress_Cumulative_Through_XVI_20260728.tex"
)
OLD_SOURCE_ZIP = (
    "10c8_SGA3_CurrentProgress_Integration_Source_Through_XVI_20260728.zip"
)
NEW_PDF = "00c_SGA3_English_CurrentProgress_Cumulative_Through_XVIII_20260728.pdf"
NEW_TEX = "02c_SGA3_English_CurrentProgress_Cumulative_Through_XVIII_20260728.tex"
NEW_SOURCE_ZIP = (
    "10c8_SGA3_CurrentProgress_Integration_Source_Through_XVIII_20260728.zip"
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

EXPECTED_PREDECESSOR_FILES = 65
EXPECTED_PREDECESSOR_MANIFEST_ROWS = 63
EXPECTED_FINAL_FILES = 65
EXPECTED_RETAINED_PREDECESSOR_FILES = 59
EXPECTED_UNRELATED_RETAINED_FILES = 58
EXPECTED_MANIFEST_ROWS = 63
EXPECTED_ZIP_ARCHIVES = 46
EXPECTED_ZIP_FILE_MEMBERS = 4_229
EXPECTED_ZIP_DIRECTORY_ENTRIES = 6
EXPECTED_ZIP_ALL_ENTRIES = 4_235
EXPECTED_ZIP_UNCOMPRESSED_BYTES = 402_367_689
EXPECTED_CURRENT_SOURCE_MEMBERS = 989
EXPECTED_CURRENT_SOURCE_UNCOMPRESSED_BYTES = 16_610_078

REPO_ROOT = SCRIPT_DIR.parent
PACKAGE_ROOT = (
    REPO_ROOT
    / "sources"
    / "sga"
    / "sga3-english-current-progress-cumulative-through-xviii-20260728"
)
RECEIPT_ROOT = REPO_ROOT / "manifests" / "published-zenodo"
PREDECESSOR_RECEIPT = (
    RECEIPT_ROOT
    / "20260728_sga3_through_xvi_sga6_idx652_record_21634000_public_readback.json"
)
CONTROLS_ROOT = Path(os.environ["LOCALAPPDATA"]) / "Temp" / (
    "sga3_xviii_zenodo_controls"
)
READBACK_ROOT = Path(os.environ["LOCALAPPDATA"]) / "Temp" / (
    "sga3_xviii_zenodo_public_readback"
)
DRAFT_STATE = (
    RECEIPT_ROOT
    / "20260728_sga3_through_xviii_zenodo_draft_state.json"
)

PRIMARY_LOCAL_PATHS = {
    NEW_PDF: PACKAGE_ROOT / NEW_PDF,
    NEW_TEX: PACKAGE_ROOT / NEW_TEX,
    NEW_SOURCE_ZIP: PACKAGE_ROOT / NEW_SOURCE_ZIP,
}

PRIMARY_EXPECTED = {
    NEW_PDF: (
        6_014_746,
        "4E4EA3DABB65689EF883A93D2B91D92BFD0C9A2DECE70EB5E7C7C7910808E12F",
    ),
    NEW_TEX: (
        20_054,
        "DDC52AA84CCFA88842ED8A3D913ABB420B6531B7204E391AD855C73CFEC3F892",
    ),
    NEW_SOURCE_ZIP: (
        12_227_078,
        "220E1E61E39E460E7757F8D2C6C50EF6220099B47E1180846A19D4305EF35B9D",
    ),
}

NEW_MANIFEST_ROWS = {
    NEW_PDF: {
        "role": "english_reader",
        "provenance": (
            "current-progress cumulative SGA3 English reader through Expose "
            "XIV plus Exposes XVI and XVIII; GitHub commit " + GITHUB_COMMIT
        ),
        "status": (
            "preferred_current_progress_working_reader_sga3_incomplete_"
            "i_xiv_plus_xvi_xviii"
        ),
    },
    NEW_TEX: {
        "role": "english_master_tex",
        "provenance": (
            "direct editable integration master for the current-progress "
            "cumulative SGA3 reader through XVIII; GitHub commit " + GITHUB_COMMIT
        ),
        "status": (
            "current_progress_working_source_sga3_incomplete_"
            "i_xiv_plus_xvi_xviii"
        ),
    },
    NEW_SOURCE_ZIP: {
        "role": "grouped_source_and_evidence",
        "provenance": (
            "989-member privacy-clean integration source closure for the "
            "current-progress SGA3 reader through XVIII; GitHub commit "
            + GITHUB_COMMIT
        ),
        "status": (
            "current_progress_integration_source_sga3_incomplete_"
            "i_xiv_plus_xvi_xviii"
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
        "surface from version 10.5281/zenodo.21634000. Fifty-eight unrelated "
        "files and the SGA3 component-history ZIP are retained byte-identically. "
        "Only the preferred SGA3 reader, direct editable integration master, "
        "current integration-source ZIP, and three release controls are "
        "replaced."
    ),
    (
        "The preferred SGA3 current-progress reader has 1,008 A4 pages and "
        "contains the Editorial Notice, Introduction, Exposes I-XIV, Expose "
        "XVI, and Expose XVIII. It places explicit gap leaves for Exposes XV "
        "and XVII and ends with a terminal gap for Exposes XIX-XXVI. It is "
        "therefore "
        "a substantial working reader, not a complete SGA3 translation, "
        "critical edition, rights clearance, or mathematical certification."
    ),
    (
        "Exposes X, XII, XIII, XIV, XVI, and XVIII are included as complete "
        "readable bodies for their stated working scope. Loop-1 source-derived "
        "raster diagram witnesses remain in Exposes I-III, X, XIV, XVI, and "
        "XVIII pending later native reconstruction. "
        "Expose VII uses its latest readable repaired working body while final "
        "standalone diagram/reference certification remains tracked separately."
    ),
    (
        "The reader has 6,304 named destinations, 3,849 valid internal GoTo "
        "actions, zero broken internal actions, 62 embedded font resources, "
        "and no Type3 fonts. An isolated three-pass source-archive rebuild "
        "matched all 1,008 extracted-text pages, decompressed page-content "
        "streams, geometries, destinations, and internal actions."
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
release controls. The reserved successor record is {draft_id}.

## Preferred SGA3 reading surface

`{NEW_PDF}` is a 1,008-page current-progress English working reader containing:

- Editorial Notice and Introduction;
- Exposes I-XIV;
- Exposes XVI and XVIII;
- explicit gap leaves for Exposes XV and XVII; and
- a terminal gap for Exposes XIX-XXVI.

This is not complete SGA3, a critical edition, rights clearance, or
mathematical certification.

Exposes X, XII, XIII, XIV, XVI, and XVIII are preserved because complete
readable bodies now exist for their stated working scope. Loop-1
source-derived raster diagram witnesses remain in Exposes I-III, X, XIV, XVI,
and XVIII pending later native reconstruction. Expose VII uses the latest
readable repaired working body while final standalone diagram/reference
certification remains separate.

## Reader checks

- 1,008 A4 pages;
- 6,304 named destinations;
- 3,849 valid internal GoTo actions;
- zero broken internal GoTo actions;
- 62 embedded font resources and zero Type3 fonts; and
- isolated three-pass source-archive rebuild equality for all 1,008 extracted
  text pages, decompressed content streams, geometries, destinations, and links.

The current source ZIP has 989 exact file members and passes CRC, identity, and
privacy closure. The unchanged SGA3 history ZIP keeps older component and
predecessor objects available without crowding the reader-first surface.

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
            "package_paths": [GITHUB_PACKAGE],
            "anonymous_readback_files": 10,
            "status": "PASS",
        },
        "sga3_reader": {
            "scope": (
                "Editorial Notice, Introduction, Exposes I-XIV, XVI, and XVIII"
            ),
            "explicit_gaps": ["Expose XV", "Expose XVII", "Exposes XIX-XXVI"],
            "pages": 1_008,
            "bytes": primary_local[NEW_PDF]["bytes"],
            "sha256": primary_local[NEW_PDF]["sha256"],
            "named_destinations": 6_304,
            "valid_internal_goto": 3_849,
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
