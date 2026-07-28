#!/usr/bin/env python3
"""Publish the SGA3-through-XXII snapshot as one same-concept successor."""

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


PREDECESSOR_RECORD = 21634836
PREDECESSOR_DOI = "10.5281/zenodo.21634836"
CONCEPT_DOI = "10.5281/zenodo.20410947"
PUBLICATION_DATE = "2026-07-28"
VERSION = "2026-07-28 SGA3 current-progress cumulative through XXII snapshot"
GITHUB_COMMIT = "bd1e8c8ea0ac2a7bd23672cc1918e20fa52e08c3"
GITHUB_PACKAGE = (
    "sources/sga/"
    "sga3-english-current-progress-cumulative-through-xxii-snapshot-20260728"
)

OLD_PDF = (
    "00c_SGA3_English_CurrentProgress_Cumulative_Through_XVIII_20260728.pdf"
)
OLD_TEX = (
    "02c_SGA3_English_CurrentProgress_Cumulative_Through_XVIII_20260728.tex"
)
OLD_SOURCE_ZIP = (
    "10c8_SGA3_CurrentProgress_Integration_Source_Through_XVIII_20260728.zip"
)
NEW_PDF = (
    "00c_SGA3_English_CurrentProgress_Cumulative_Through_XXII_"
    "Snapshot_20260728.pdf"
)
NEW_TEX = (
    "02c_SGA3_English_CurrentProgress_Cumulative_Through_XXII_"
    "Snapshot_20260728.tex"
)
NEW_SOURCE_ZIP = (
    "10c8_SGA3_CurrentProgress_Source_History_Through_XXII_"
    "Snapshot_20260728.zip"
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
EXPECTED_ZIP_FILE_MEMBERS = 4_240
EXPECTED_ZIP_DIRECTORY_ENTRIES = 6
EXPECTED_ZIP_ALL_ENTRIES = 4_246
EXPECTED_ZIP_UNCOMPRESSED_BYTES = 403_702_251
EXPECTED_CURRENT_SOURCE_MEMBERS = 1_000
EXPECTED_CURRENT_SOURCE_UNCOMPRESSED_BYTES = 17_944_640

REPO_ROOT = SCRIPT_DIR.parent
PACKAGE_ROOT = (
    REPO_ROOT
    / "sources"
    / "sga"
    / "sga3-english-current-progress-cumulative-through-xxii-snapshot-20260728"
)
RECEIPT_ROOT = REPO_ROOT / "manifests" / "published-zenodo"
PREDECESSOR_RECEIPT = (
    RECEIPT_ROOT
    / "20260728_sga3_cumulative_with_x_record_21634836_public_readback.json"
)
CONTROLS_ROOT = Path(os.environ["LOCALAPPDATA"]) / "Temp" / (
    "sga3_xxii_snapshot_zenodo_controls"
)
READBACK_ROOT = Path(os.environ["LOCALAPPDATA"]) / "Temp" / (
    "sga3_xxii_snapshot_zenodo_public_readback"
)
DRAFT_STATE = (
    RECEIPT_ROOT
    / "20260728_sga3_through_xxii_snapshot_zenodo_draft_state.json"
)

PRIMARY_LOCAL_PATHS = {
    NEW_PDF: PACKAGE_ROOT / NEW_PDF,
    NEW_TEX: PACKAGE_ROOT / NEW_TEX,
    NEW_SOURCE_ZIP: PACKAGE_ROOT / NEW_SOURCE_ZIP,
}

PRIMARY_EXPECTED = {
    NEW_PDF: (
        6_863_204,
        "E401297F71F030C8EBD26F321B7F91B03799A628462A06EFF9DC4C5ADB47E739",
    ),
    NEW_TEX: (
        25_386,
        "A7391ADB079C97B8B6FD04D7D7DC953EB924F44281D737B05D400F0C8CBCA4D1",
    ),
    NEW_SOURCE_ZIP: (
        13_552_765,
        "866FA17BDABA537C67504F514F5544F2D08998F876F43C92312A389D89D1FC79",
    ),
}

NEW_MANIFEST_ROWS = {
    NEW_PDF: {
        "role": "english_reader",
        "provenance": (
            "current-progress cumulative SGA3 English reader with complete "
            "working scopes I-XVI and XVIII plus partial XVII, XX, and XXII; "
            "GitHub commit " + GITHUB_COMMIT
        ),
        "status": (
            "preferred_current_progress_working_reader_sga3_incomplete_"
            "through_xxii_snapshot"
        ),
    },
    NEW_TEX: {
        "role": "english_master_tex",
        "provenance": (
            "direct editable integration master for the current-progress "
            "cumulative SGA3 reader through XXII snapshot; GitHub commit "
            + GITHUB_COMMIT
        ),
        "status": (
            "current_progress_working_source_sga3_incomplete_"
            "through_xxii_snapshot"
        ),
    },
    NEW_SOURCE_ZIP: {
        "role": "grouped_source_and_evidence",
        "provenance": (
            "1000-member privacy-clean source, bounded-reader, control, and "
            "predecessor-history archive for the through-XXII snapshot; "
            "GitHub commit "
            + GITHUB_COMMIT
        ),
        "status": (
            "current_progress_source_history_sga3_incomplete_"
            "through_xxii_snapshot"
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
        "surface from version 10.5281/zenodo.21634836. Fifty-eight unrelated "
        "files and the SGA3 component-history ZIP are retained byte-identically. "
        "Only the preferred SGA3 reader, direct editable integration master, "
        "current integration-source ZIP, and three release controls are "
        "replaced."
    ),
    (
        "The preferred SGA3 current-progress reader has 1,100 A4 pages. It "
        "contains complete current working bodies for the Editorial Notice, "
        "Introduction, Exposes I-XVI, and Expose XVIII; partial bodies for "
        "Exposes XVII, XX, and XXII; and explicit gap leaves for Exposes XIX, "
        "XXI, and XXIII-XXVI. It is therefore "
        "a substantial working reader, not a complete SGA3 translation, "
        "critical edition, rights clearance, or mathematical certification."
    ),
    (
        "Expose X is present as its complete 44-authority-page Loop-1 body. "
        "Expose XVII reaches Definition 3.6 on authority page 8; Expose XX "
        "reaches the proof of 1.10 on authority page 7; and Expose XXII reaches "
        "Proposition 4.1.2 on authority page 10. Loop-1 source-derived raster "
        "diagram witnesses remain in several included scopes pending later "
        "native reconstruction. "
        "Expose VII uses its latest readable repaired working body while final "
        "standalone diagram/reference certification remains tracked separately."
    ),
    (
        "The reader has 6,805 named destinations, 3,917 valid internal GoTo "
        "actions, zero broken internal actions, 63 embedded font resources, "
        "and no Type3 fonts. An isolated three-pass source-archive rebuild "
        "matched all 1,100 extracted-text pages, decompressed page-content "
        "streams, geometries, destinations, internal actions, and 72-dpi "
        "decoded rasters."
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
    "objects are grouped into coherent ZIP archives. The current SGA3 source "
    "archive contains 1,000 files instead of exposing them loose. GitHub "
    "custody commit: "
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

`{NEW_PDF}` is a 1,100-page current-progress English working reader containing:

- Editorial Notice and Introduction;
- complete current working bodies for Exposes I-XVI and XVIII;
- Expose XVII through Definition 3.6 on authority page 8;
- Expose XX through the proof of 1.10 on authority page 7;
- Expose XXII through Proposition 4.1.2 on authority page 10; and
- explicit gap leaves for Exposes XIX, XXI, and XXIII-XXVI.

This is not complete SGA3, a critical edition, rights clearance, or
mathematical certification.

Expose X is the complete 44-authority-page Loop-1 body, not an older gap or
fragment. Loop-1 source-derived raster diagram witnesses remain in several
included scopes pending later native reconstruction. Expose VII uses the
latest readable repaired working body while final standalone
diagram/reference certification remains separate. The partial Exposes XVII,
XX, and XXII end at visible continuation boundaries.

## Reader checks

- 1,100 A4 pages;
- 6,805 named destinations;
- 3,917 valid internal GoTo actions;
- zero broken internal GoTo actions;
- 63 embedded font resources and zero Type3 fonts; and
- isolated three-pass source-archive rebuild equality for all 1,100 extracted
  text pages, decompressed content streams, geometries, destinations, links,
  and 72-dpi decoded rasters.

The current source/history ZIP has 1,000 exact file members and passes CRC,
identity, privacy, extraction, and independent rebuild closure. It includes
the immediately preceding cumulative reader so older current-progress material
remains available without crowding the reader-first surface.

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
                "Editorial Notice, Introduction, complete current working "
                "bodies I-XVI and XVIII, plus partial XVII, XX, and XXII"
            ),
            "partial_scopes": {
                "Expose XVII": "authority pages 1-8 through Definition 3.6",
                "Expose XX": "authority pages 1-7 through proof 1.10",
                "Expose XXII": (
                    "authority pages 1-10 through Proposition 4.1.2"
                ),
            },
            "explicit_gaps": [
                "Expose XIX",
                "Expose XXI",
                "Exposes XXIII-XXVI",
            ],
            "pages": 1_100,
            "bytes": primary_local[NEW_PDF]["bytes"],
            "sha256": primary_local[NEW_PDF]["sha256"],
            "named_destinations": 6_805,
            "valid_internal_goto": 3_917,
            "broken_internal_goto": 0,
            "embedded_font_resources": 63,
            "type3_fonts": 0,
            "isolated_rebuild_text_content_geometry_links_raster_exact": True,
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
