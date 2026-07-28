#!/usr/bin/env python3
"""Publish the reader-clean 1,469-page SGA3 working-reader successor."""

from __future__ import annotations

import csv
import importlib.util
import io
import json
import os
import shutil
import sys
import zipfile
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
BASE_PATH = SCRIPT_DIR / "publish_sga3_expose_xiii_zenodo_20260728.py"
SPEC = importlib.util.spec_from_file_location("sga3_reader_order_base", BASE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("Unable to load the established SGA successor workflow")
workflow = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = workflow
SPEC.loader.exec_module(workflow)
base = workflow.base


PREDECESSOR_RECORD = 21648705
PREDECESSOR_DOI = "10.5281/zenodo.21648705"
CONCEPT_DOI = "10.5281/zenodo.20410947"
PUBLICATION_DATE = "2026-07-28"
VERSION = "2026-07-28 SGA3 1469-page reader-clean working reader"
GITHUB_COMMIT = "f31134e68a2f24e6a1d960bf5e649cd94ed2c69b"
GITHUB_PACKAGE = (
    "sources/sga/"
    "sga3-english-complete-working-reader-clean-20260728"
)

OLD_PDF_NAME = (
    "00c00_SGA3_English_CurrentProgress_Cumulative_Latest_20260728.pdf"
)
OLD_TEX_NAME = (
    "02c00_SGA3_English_CurrentProgress_Cumulative_Latest_20260728.tex"
)
OLD_ZIP_NAME = (
    "10c9_SGA3_CurrentProgress_FullVolume_Integration_Source_20260728.zip"
)
PDF_NAME = (
    "00c00_SGA3_English_Complete_Working_Reader_20260728.pdf"
)
TEX_NAME = (
    "02c00_SGA3_English_Complete_Working_Reader_20260728.tex"
)
ZIP_NAME = (
    "10c9_SGA3_English_Complete_Working_Reader_"
    "Source_and_Predecessor_20260728.zip"
)
README_NAME = "09_README_CURRENT_RELEASE.md"
MANIFEST_NAME = "09a_RELEASE_FILE_MANIFEST.csv"
VALIDATION_NAME = "09b_RELEASE_VALIDATION.json"
REPLACED_NAMES = {
    OLD_PDF_NAME,
    OLD_TEX_NAME,
    OLD_ZIP_NAME,
    README_NAME,
    MANIFEST_NAME,
    VALIDATION_NAME,
}

EXPECTED_PREDECESSOR_FILES = 92
EXPECTED_PREDECESSOR_MANIFEST_ROWS = 90
EXPECTED_FINAL_FILES = 92
EXPECTED_RETAINED_PREDECESSOR_FILES = 86
EXPECTED_UNRELATED_RETAINED_FILES = 86
EXPECTED_MANIFEST_ROWS = 90
EXPECTED_ZIP_ARCHIVES = 57
EXPECTED_ZIP_FILE_MEMBERS = 5_597
EXPECTED_ZIP_DIRECTORY_ENTRIES = 6
EXPECTED_ZIP_ALL_ENTRIES = 5_603
EXPECTED_ZIP_UNCOMPRESSED_BYTES = 453_999_152
EXPECTED_GITHUB_READBACK_FILES = 11
EXPECTED_NEW_ZIP_MEMBERS = 901

REPO_ROOT = SCRIPT_DIR.parent
PACKAGE_ROOT = REPO_ROOT / GITHUB_PACKAGE
RECEIPT_ROOT = REPO_ROOT / "manifests" / "published-zenodo"
PREDECESSOR_RECEIPT = (
    RECEIPT_ROOT
    / "20260728_sga3_cumulative_with_x_record_21648705_public_readback.json"
)
CONTROLS_ROOT = (
    Path(os.environ["LOCALAPPDATA"])
    / "Temp"
    / "sga3_reader_clean_complete_working_zenodo_controls"
)
READBACK_ROOT = (
    Path(os.environ["LOCALAPPDATA"])
    / "Temp"
    / "sga3_reader_clean_complete_working_zenodo_public_readback"
)
DRAFT_STATE = (
    RECEIPT_ROOT
    / "20260728_sga3_reader_clean_complete_working_zenodo_draft_state.json"
)

PRIMARY_LOCAL_PATHS = {
    PDF_NAME: PACKAGE_ROOT / PDF_NAME,
    TEX_NAME: PACKAGE_ROOT / TEX_NAME,
    ZIP_NAME: PACKAGE_ROOT / ZIP_NAME,
}
PRIMARY_EXPECTED = {
    PDF_NAME: (
        11_931_836,
        "27F308094C6147ED20EBDFB48813C2D71D7C957ADDFD0656E3F1E11938E0B328",
    ),
    TEX_NAME: (
        21_434,
        "95A11E5F082F2F91F328876D020031A8D3ED2FDD5486364BE82A1EA35CA983DC",
    ),
    ZIP_NAME: (
        12_810_270,
        "6226D36DB6D1A0D6BCD370E319012B7D7B27654CECF99C56F2C0C8A692B189D9",
    ),
}
PACKAGE_MANIFEST_SHA256 = (
    "532E411993E5166B2127099665D6B2F7DCFD2F9A87F241DFAF1649C5ED3EABB2"
)
SOURCE_MANIFEST_SHA256 = (
    "685C62135292FE4EF16AF31F162C8A6D00F9FCB362601982CFA2554F38089AA2"
)
PACKAGE_URL = (
    "https://github.com/KokunoYumeto/modern-latex-manuscripts/tree/"
    f"{GITHUB_COMMIT}/{GITHUB_PACKAGE}"
)

NEW_MANIFEST_ROWS = {
    PDF_NAME: {
        "role": "english_reader",
        "provenance": (
            "preferred reader-clean 1,469-page SGA3 complete working "
            f"translation surface; GitHub {PACKAGE_URL}"
        ),
        "status": (
            "preferred_complete_working_reader_not_critical_edition_"
            "not_final_diagram_certification"
        ),
    },
    TEX_NAME: {
        "role": "english_master_tex",
        "provenance": (
            "direct editable master for the reader-clean 1,469-page "
            f"working reader; GitHub {PACKAGE_URL}"
        ),
        "status": "preferred_complete_working_reader_master_tex",
    },
    ZIP_NAME: {
        "role": "grouped_source_and_predecessor",
        "provenance": (
            "exact 901-member build closure, release controls, and "
            f"superseded cumulative reader; GitHub {PACKAGE_URL}"
        ),
        "status": (
            "buildable_source_and_history_grouped_not_rights_or_"
            "diagram_fidelity_certification"
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
        "This same-concept compact successor preserves 86 files from version "
        "10.5281/zenodo.21648705 byte-identically, replaces the preferred "
        "SGA3 cumulative PDF, direct master TeX, and grouped source ZIP, and "
        "refreshes three release controls. SGA1 remains the default preview."
    ),
    (
        "The preferred SGA3 reader now has 1,469 A4 pages and continuously "
        "integrates the Editorial Notice, Introduction, Exposes I-XXVI, the "
        "Tome III mathematical guide, and the terminal index. It is the "
        "complete current working translation surface available on 28 July "
        "2026, rather than a claim of critical-edition or final status."
    ),
    (
        "Reader-facing production commentary was removed: there is no "
        "AI/process preface, working-state box, production-boundary page, or "
        "diagram-process caption. Substantive source-reading notes remain. "
        "Required provenance and attribution are kept in the external release "
        "metadata and grouped source package."
    ),
    (
        "The PDF has 9,483 named destinations, 4,590 valid internal GoTo "
        "actions, zero invalid or external actions, 61 embedded font "
        "resources, zero Type3 fonts, and 153 raster image XObjects. The "
        "source ZIP contains 901 safe members and preserves the superseded "
        "1,434-page reader and master TeX as history."
    ),
    (
        "This is a scholarly working translation and TeX edition, not a "
        "critical edition, blanket rights clearance, final diagram-fidelity "
        "certification, mathematical certification, peer review, or "
        "tagged-PDF accessibility remediation. Some integrated diagrams still "
        "use source-derived raster witnesses. Historical versions remain "
        "immutable."
    ),
]
DESCRIPTION_HTML = "\n".join(
    f"<p>{paragraph}</p>" for paragraph in DESCRIPTION_PARAGRAPHS
)
NOTES_HTML = (
    "<p>The 1,469-page reader-clean SGA3 complete working translation is the "
    "preferred direct SGA3 reading surface. The superseded cumulative reader "
    "and source history are grouped in one ZIP. SGA1 remains the default "
    "preview.</p>"
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

    outer_manifest = PACKAGE_ROOT / "SHA256SUMS.csv"
    if base.sha256_file(outer_manifest) != PACKAGE_MANIFEST_SHA256:
        raise RuntimeError("GitHub package manifest identity mismatch")
    rows = list(
        csv.DictReader(
            io.StringIO(outer_manifest.read_text(encoding="utf-8-sig"))
        )
    )
    expected_outer = {
        path.name
        for path in PACKAGE_ROOT.iterdir()
        if path.is_file() and path.name != outer_manifest.name
    }
    if len(rows) != 10 or {row["filename"] for row in rows} != expected_outer:
        raise RuntimeError("GitHub package exact-set mismatch")
    for row in rows:
        path = PACKAGE_ROOT / row["filename"]
        if (path.stat().st_size, base.sha256_file(path)) != (
            int(row["bytes"]),
            row["sha256"].upper(),
        ):
            raise RuntimeError(f"GitHub package mismatch: {row['filename']}")

    validation = json.loads(
        (PACKAGE_ROOT / "PACKAGE_VALIDATION.json").read_text(encoding="utf-8")
    )
    reader = validation.get("reader", {})
    source_archive = validation.get("source_archive", {})
    if (
        validation.get("status") != "PASS"
        or validation.get("errors") != []
        or validation.get("privacy", {}).get("hits") != []
        or reader.get("filename") != PDF_NAME
        or reader.get("pages") != 1_469
        or reader.get("text_pages") != 1_467
        or reader.get("named_destinations") != 9_483
        or reader.get("internal_goto_actions") != 4_590
        or reader.get("invalid_actions") != 0
        or reader.get("uri_actions") != 0
        or reader.get("type3_fonts") != 0
        or reader.get("raster_xobjects") != 153
        or reader.get("reader_process_term_hits") != []
        or validation.get("master_tex", {}).get("filename") != TEX_NAME
        or source_archive.get("filename") != ZIP_NAME
        or source_archive.get("members") != EXPECTED_NEW_ZIP_MEMBERS
        or source_archive.get("manifest_rows") != 900
        or source_archive.get("manifest_sha256") != SOURCE_MANIFEST_SHA256
        or source_archive.get("crc_or_identity_errors") != []
    ):
        raise RuntimeError("GitHub package validation is not controlling PASS")

    with zipfile.ZipFile(PRIMARY_LOCAL_PATHS[ZIP_NAME], "r") as archive:
        bad = archive.testzip()
        names = archive.namelist()
        infos = archive.infolist()
        if (
            bad is not None
            or len(names) != EXPECTED_NEW_ZIP_MEMBERS
            or len(names) != len(set(names))
            or sum(info.file_size for info in infos) != 16_782_234
        ):
            raise RuntimeError("Source/history ZIP boundary or CRC mismatch")
        for name in names:
            base.safe_zip_name(name)
        internal_manifest = archive.read("SOURCE_BUNDLE_SHA256.csv")
        if (
            base.hashlib.sha256(internal_manifest).hexdigest().upper()
            != SOURCE_MANIFEST_SHA256
        ):
            raise RuntimeError("Source/history ZIP manifest mismatch")
        source_rows = list(
            csv.DictReader(
                io.StringIO(internal_manifest.decode("utf-8-sig"))
            )
        )
        expected_source = set(names) - {"SOURCE_BUNDLE_SHA256.csv"}
        if (
            len(source_rows) != 900
            or {row["relative_path"] for row in source_rows}
            != expected_source
        ):
            raise RuntimeError("Source/history ZIP manifest exact-set mismatch")
        for row in source_rows:
            data = archive.read(row["relative_path"])
            if (
                len(data),
                base.hashlib.sha256(data).hexdigest().upper(),
            ) != (
                int(row["bytes"]),
                row["sha256"].upper(),
            ):
                raise RuntimeError(
                    f"Source/history ZIP member mismatch: "
                    f"{row['relative_path']}"
                )
        embedded = json.loads(
            archive.read("SOURCE_BUNDLE_VALIDATION.json").decode("utf-8")
        )
        if embedded.get("status") != "PASS" or embedded.get("errors") != []:
            raise RuntimeError("Embedded source validation is not PASS")
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
        csv.DictReader(
            io.StringIO(content.decode("utf-8-sig"), newline="")
        )
    )
    if len(rows) != EXPECTED_PREDECESSOR_MANIFEST_ROWS:
        raise RuntimeError("Unexpected predecessor release-manifest row count")
    return rows


def readme_text(draft_id: int) -> str:
    return f"""# Current compact SGA release

This is one same-concept successor to Zenodo record {PREDECESSOR_RECORD}. It
retains 86 predecessor files byte-identically, replaces the preferred SGA3
cumulative PDF, direct master TeX, and grouped source ZIP, and refreshes three
release controls. The reserved successor record is {draft_id}. SGA1 remains
the default preview.

## Preferred SGA3 working reader

`{PDF_NAME}` is the preferred 1,469-page SGA3 complete working reader. It
contains the Editorial Notice, Introduction, Exposes I-XXVI, the Tome III
mathematical guide, and the terminal index. Its `00c00` slot sorts before the
smaller bounded SGA3 readers.

`{TEX_NAME}` is the direct editable master TeX.

`{ZIP_NAME}` contains the exact 901-member build closure, release controls,
and the superseded 1,434-page cumulative PDF and master TeX. The older
cumulative state is preserved as history without remaining a loose competing
reader.

Reader-facing process commentary was removed. Substantive source-reading
notes remain, while provenance and attribution are recorded outside the
reader.

This is a complete current working translation surface, not a critical
edition, blanket rights clearance, final diagram-fidelity certification,
peer review, or accessibility-remediated PDF. Some integrated diagrams still
use source-derived raster witnesses.

GitHub package:

`{PACKAGE_URL}`
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

    release_rows: list[dict[str, str]] = []
    for row in predecessor_rows:
        name = row["filename"]
        if name in REPLACED_NAMES:
            continue
        identity = predecessor_identities[name]
        if (int(row["bytes"]), row["sha256"].upper()) != (
            identity["bytes"],
            identity["sha256"],
        ):
            raise RuntimeError(f"Retained manifest identity mismatch: {name}")
        release_rows.append(dict(row))

    new_local = dict(primary_local)
    new_local[README_NAME] = readme_identity
    for name in sorted(new_local, key=str.casefold):
        metadata = NEW_MANIFEST_ROWS[name]
        identity = new_local[name]
        release_rows.append(
            {
                "filename": name,
                "bytes": str(identity["bytes"]),
                "sha256": identity["sha256"],
                "role": metadata["role"],
                "provenance": metadata["provenance"],
                "status": metadata["status"],
            }
        )
    release_rows.sort(key=lambda row: row["filename"].casefold())
    if len(release_rows) != EXPECTED_MANIFEST_ROWS:
        raise RuntimeError("Generated release-manifest row-count mismatch")
    if len({row["filename"] for row in release_rows}) != len(release_rows):
        raise RuntimeError("Generated release manifest has duplicate filenames")
    sga3_pdfs = sorted(
        (
            row["filename"]
            for row in release_rows
            if row["filename"].lower().endswith(".pdf")
            and row["filename"].startswith("00c")
        ),
        key=str.casefold,
    )
    if not sga3_pdfs or sga3_pdfs[0] != PDF_NAME:
        raise RuntimeError("Preferred SGA3 reader is not first by filename")

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
        writer.writerows(release_rows)
    manifest_identity = {
        "path": manifest_path,
        "bytes": manifest_path.stat().st_size,
        "sha256": base.sha256_file(manifest_path),
        "md5": base.md5_file(manifest_path),
    }

    validation = {
        "status": "PASS_READY_FOR_ONE_SAME_CONCEPT_READER_CLEAN_SUCCESSOR",
        "errors": [],
        "concept_doi": CONCEPT_DOI,
        "predecessor_record": PREDECESSOR_RECORD,
        "predecessor_doi": PREDECESSOR_DOI,
        "reserved_successor_record": draft_id,
        "release_policy": (
            "one same-concept reader-clean working-reader successor; "
            "no duplicate concept or draft"
        ),
        "retained_predecessor_files": EXPECTED_RETAINED_PREDECESSOR_FILES,
        "replaced_files": sorted(REPLACED_NAMES, key=str.casefold),
        "new_files": sorted(
            set(PRIMARY_LOCAL_PATHS)
            | {README_NAME, MANIFEST_NAME, VALIDATION_NAME},
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
            "package_root": GITHUB_PACKAGE,
            "anonymous_readback_files": EXPECTED_GITHUB_READBACK_FILES,
            "status": "PASS",
        },
        "ordering": {
            "preferred_sga3_pdf": PDF_NAME,
            "preferred_sga3_pdf_is_first": True,
            "old_pdf_removed_from_successor": OLD_PDF_NAME,
            "old_tex_removed_from_successor": OLD_TEX_NAME,
            "old_source_zip_removed_from_successor": OLD_ZIP_NAME,
        },
        "reader": {
            "filename": PDF_NAME,
            "pages": 1_469,
            "text_pages": 1_467,
            "bytes": primary_local[PDF_NAME]["bytes"],
            "sha256": primary_local[PDF_NAME]["sha256"],
            "content_changed": True,
            "complete_current_working_surface": True,
            "critical_edition_claimed": False,
            "diagram_final_claimed": False,
            "reader_facing_process_notes_removed": True,
        },
        "master_tex": {
            "filename": TEX_NAME,
            "bytes": primary_local[TEX_NAME]["bytes"],
            "sha256": primary_local[TEX_NAME]["sha256"],
            "content_changed": True,
        },
        "source_archive": {
            "filename": ZIP_NAME,
            "bytes": primary_local[ZIP_NAME]["bytes"],
            "sha256": primary_local[ZIP_NAME]["sha256"],
            "members": EXPECTED_NEW_ZIP_MEMBERS,
            "uncompressed_bytes": 16_782_234,
            "contains_predecessor_reader": True,
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


for module in (workflow, base):
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
        "EXPECTED_RETAINED_PREDECESSOR_FILES": (
            EXPECTED_RETAINED_PREDECESSOR_FILES
        ),
        "EXPECTED_UNRELATED_RETAINED_FILES": (
            EXPECTED_UNRELATED_RETAINED_FILES
        ),
        "EXPECTED_MANIFEST_ROWS": EXPECTED_MANIFEST_ROWS,
        "EXPECTED_ZIP_ARCHIVES": EXPECTED_ZIP_ARCHIVES,
        "EXPECTED_ZIP_FILE_MEMBERS": EXPECTED_ZIP_FILE_MEMBERS,
        "EXPECTED_ZIP_DIRECTORY_ENTRIES": EXPECTED_ZIP_DIRECTORY_ENTRIES,
        "EXPECTED_ZIP_ALL_ENTRIES": EXPECTED_ZIP_ALL_ENTRIES,
        "EXPECTED_ZIP_UNCOMPRESSED_BYTES": EXPECTED_ZIP_UNCOMPRESSED_BYTES,
        "EXPECTED_GITHUB_READBACK_FILES": EXPECTED_GITHUB_READBACK_FILES,
        "EXPECTED_NEW_ZIP_MEMBERS": EXPECTED_NEW_ZIP_MEMBERS,
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
        setattr(module, name, value)

base.verify_primary_local_files = verify_primary_local_files
base.fetch_predecessor_manifest = fetch_predecessor_manifest
base.readme_text = readme_text
base.generate_controls = generate_controls


if __name__ == "__main__":
    base.main()
