#!/usr/bin/env python3
"""Publish one reader-clean SGA1-6 successor, including SGA3 R17."""

from __future__ import annotations

import csv
import importlib.util
import io
import json
import os
import sys
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
BASE_PATH = (
    SCRIPT_DIR
    / "publish_sga1_6_reader_clean_presentation_zenodo_20260728.py"
)
SPEC = importlib.util.spec_from_file_location("sga_reader_clean_20260728", BASE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("Unable to load the established SGA cleanup workflow")
previous = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = previous
SPEC.loader.exec_module(previous)
base = previous.base

ORIGINAL_GENERATE_CONTROLS = previous.generate_controls


PREDECESSOR_RECORD = 21650398
PREDECESSOR_DOI = "10.5281/zenodo.21650398"
CONCEPT_DOI = "10.5281/zenodo.20410947"
PUBLICATION_DATE = "2026-07-29"
VERSION = "2026-07-29 reader-clean SGA1-6 with SGA3 R17 native update"
GITHUB_COMMIT = "af191ecec0ba547a8fb214ac45b615c713fdf9c6"
GITHUB_PACKAGE = (
    "sources/sga/"
    "sga3-english-complete-working-reader-clean-r17-native-xxii-xxiv-"
    "20260729"
)

OLD_SGA3_NAMES = {
    "00c00_SGA3_English_Complete_Working_Reader_20260728.pdf",
    "02c00_SGA3_English_Complete_Working_Reader_20260728.tex",
    (
        "10c9_SGA3_English_Complete_Working_Reader_"
        "Source_and_Predecessor_20260728.zip"
    ),
}
SGA3_PDF = (
    "00c00_SGA3_English_Complete_Reader_"
    "Native_Update_R17_20260729.pdf"
)
SGA3_TEX = (
    "02c00_SGA3_English_Complete_Reader_"
    "Native_Update_R17_20260729.tex"
)
SGA3_ZIP = (
    "10c9_SGA3_English_Complete_Reader_"
    "Source_and_History_R17_20260729.zip"
)

README_NAME = previous.README_NAME
MANIFEST_NAME = previous.MANIFEST_NAME
VALIDATION_NAME = previous.VALIDATION_NAME
REPLACED_NAMES = set(previous.REPLACED_NAMES) | OLD_SGA3_NAMES

EXPECTED_PREDECESSOR_FILES = 92
EXPECTED_FINAL_FILES = 92
EXPECTED_RETAINED_PREDECESSOR_FILES = 76
EXPECTED_UNRELATED_RETAINED_FILES = 76
EXPECTED_MANIFEST_ROWS = 90
EXPECTED_ZIP_ARCHIVES = 57
EXPECTED_ZIP_FILE_MEMBERS = 5_603
EXPECTED_ZIP_DIRECTORY_ENTRIES = 6
EXPECTED_ZIP_ALL_ENTRIES = 5_609
EXPECTED_ZIP_UNCOMPRESSED_BYTES = 455_787_707
EXPECTED_GITHUB_READBACK_FILES = 24

REPO_ROOT = SCRIPT_DIR.parent
SGA3_PACKAGE_ROOT = REPO_ROOT / GITHUB_PACKAGE
RECEIPT_ROOT = REPO_ROOT / "manifests" / "published-zenodo"
PREDECESSOR_RECEIPT = (
    RECEIPT_ROOT
    / "20260728_sga3_cumulative_with_x_record_21650398_public_readback.json"
)
CONTROLS_ROOT = (
    Path(os.environ["LOCALAPPDATA"])
    / "Temp"
    / "sga_reader_clean_complete_r17_native_zenodo_controls"
)
READBACK_ROOT = (
    Path(os.environ["LOCALAPPDATA"])
    / "Temp"
    / "sga_reader_clean_complete_r17_native_zenodo_public_readback"
)
DRAFT_STATE = (
    RECEIPT_ROOT
    / "20260728_sga1_6_reader_clean_presentation_zenodo_draft_state.json"
)

PRIMARY_LOCAL_PATHS = {
    **previous.PRIMARY_LOCAL_PATHS,
    SGA3_PDF: SGA3_PACKAGE_ROOT / SGA3_PDF,
    SGA3_TEX: SGA3_PACKAGE_ROOT / SGA3_TEX,
    SGA3_ZIP: SGA3_PACKAGE_ROOT / SGA3_ZIP,
}
PRIMARY_EXPECTED = {
    **previous.PRIMARY_EXPECTED,
    SGA3_PDF: (
        10_668_964,
        "9761E6F89988E2CF5FDE78C5B398CD96846D28F7D364B1EF2D0EEB9BFD2662C8",
    ),
    SGA3_TEX: (
        21_853,
        "9D5BA11B11E895156AB4D708A169E1BD51C19052B3A03A11A4E3BD30E0354396",
    ),
    SGA3_ZIP: (
        12_206_677,
        "F822FF7F1D5440D85B4973F443B54CF540E24D8F08D9FB534657E01A399700AF",
    ),
}

NEW_MANIFEST_ROWS = {
    **previous.NEW_MANIFEST_ROWS,
    SGA3_PDF: {
        "role": "english_reader",
        "provenance": (
            "preferred reader-clean 1472-page SGA3 R17 native cumulative; "
            "GitHub "
            f"https://github.com/KokunoYumeto/modern-latex-manuscripts/tree/"
            f"{GITHUB_COMMIT}/{GITHUB_PACKAGE}"
        ),
        "status": (
            "preferred_complete_working_reader_not_critical_edition_"
            "not_final_diagram_certification"
        ),
    },
    SGA3_TEX: {
        "role": "english_master_tex",
        "provenance": (
            "direct editable master for the reader-clean SGA3 R17 reader"
        ),
        "status": "preferred_complete_working_reader_master_tex",
    },
    SGA3_ZIP: {
        "role": "grouped_source_and_predecessor",
        "provenance": (
            "exact recursive source closure, build controls, and superseded "
            "reader grouped behind the direct SGA3 reader"
        ),
        "status": (
            "buildable_source_and_history_grouped_not_rights_or_"
            "diagram_fidelity_certification"
        ),
    },
}

DESCRIPTION_PARAGRAPHS = [
    (
        "This same-concept successor preserves 76 files from version "
        "10.5281/zenodo.21650398 byte-identically. It replaces the six direct "
        "English SGA1-6 readers, their direct master TeX files, the grouped "
        "SGA3 reader source/history archive, and three release controls. "
        "SGA1 remains the default preview."
    ),
    (
        "The direct reader PDFs omit project-facing production-status, "
        "source-status, AI, and workflow commentary. The mathematics, "
        "diagrams, labels, and internal links remain on the reading surface; "
        "provenance and technical history remain in grouped archives and "
        "release metadata."
    ),
    (
        "The preferred SGA3 object is a 1,472-page English cumulative covering "
        "the Editorial Notice, Introduction, Exposes I-XXVI, the Tome-I index, "
        "the Tome-III mathematical guide, and the terminal index. R17 adds "
        "native successors for Exposes XXII and XXIV to the earlier "
        "X/XVI/XVIII integration. Its source closure and the superseded R16 "
        "reader are grouped in one ZIP."
    ),
    (
        "These are scholarly working translations and TeX editions, not "
        "critical editions, blanket rights clearances, mathematical "
        "certifications, peer review, final diagram-fidelity certification, "
        "or tagged-PDF accessibility remediation. No new license grant is "
        "asserted and historical Zenodo versions remain immutable."
    ),
]
DESCRIPTION_HTML = "\n".join(
    f"<p>{paragraph}</p>" for paragraph in DESCRIPTION_PARAGRAPHS
)
NOTES_HTML = (
    "<p>Reader-first SGA1-6 surface. Direct PDFs contain the mathematics, "
    "diagrams, labels, and links; project process and status material is kept "
    "outside the readers. SGA1 remains the default preview.</p>"
)


def verify_manifest(root: Path, expected_sha256: str) -> None:
    manifest = root / "SHA256SUMS.csv"
    if base.sha256_file(manifest) != expected_sha256:
        raise RuntimeError(f"Package manifest mismatch: {root.name}")
    rows = list(
        csv.DictReader(
            io.StringIO(manifest.read_text(encoding="utf-8-sig"), newline="")
        )
    )
    for row in rows:
        path = root / row["filename"]
        if not path.is_file():
            raise FileNotFoundError(path)
        if (path.stat().st_size, base.sha256_file(path)) != (
            int(row["bytes"]),
            row["sha256"].upper(),
        ):
            raise RuntimeError(f"Package row mismatch: {path}")


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

    verify_manifest(previous.PACKAGE_ROOT, previous.PACKAGE_MANIFEST_SHA256)
    verify_manifest(
        SGA3_PACKAGE_ROOT,
        "30DC0330A1A69BD4B6A4CD333F45F439D2E01BFE0C21D6AF50D94E2DC59AAD56",
    )
    old_validation = json.loads(
        (previous.PACKAGE_ROOT / "PACKAGE_VALIDATION.json").read_text(
            encoding="utf-8"
        )
    )
    new_validation = json.loads(
        (SGA3_PACKAGE_ROOT / "PACKAGE_VALIDATION.json").read_text(
            encoding="utf-8"
        )
    )
    if (
        old_validation.get("status") != "PASS"
        or old_validation.get("errors") != []
        or old_validation.get("reader_facing_process_or_status_hits") != []
        or new_validation.get("status") != "PASS"
        or new_validation.get("errors") != []
        or new_validation.get("reader", {}).get("pages") != 1_472
        or new_validation.get("reader", {}).get("reader_process_term_hits") != []
        or new_validation.get("source_archive", {}).get("members") != 907
        or new_validation.get("source_archive", {}).get(
            "crc_or_identity_errors"
        )
        != []
    ):
        raise RuntimeError("Reader-clean package validation mismatch")
    return result


def readme_text(draft_id: int) -> str:
    return f"""# Current reader-first SGA release

This is one same-concept successor to Zenodo record {PREDECESSOR_RECORD}.
It replaces the direct English SGA1-6 readers and their direct master TeX
files, groups the SGA3 source and predecessor behind its direct reader, and
refreshes the release controls. The reserved successor is {draft_id}.

The direct reader PDFs contain the mathematics, diagrams, labels, and links.
Project-facing production-status, source-status, AI, and workflow commentary
is kept outside the readers.

The preferred SGA3 reader has 1,472 A4 pages and covers the Editorial Notice,
Introduction, Exposes I-XXVI, Tome-I index, Tome-III mathematical guide, and
terminal index. R17 adds the native successors for Exposes XXII and XXIV to the
earlier X/XVI/XVIII integration. Its exact recursive source closure and
superseded R16 reader are grouped in `{SGA3_ZIP}`.

These are scholarly working translations and TeX editions, not critical
editions, blanket rights clearances, mathematical certifications, peer review,
final diagram-fidelity certification, or tagged-PDF accessibility remediation.
Historical Zenodo versions remain immutable. SGA1 remains the default preview.

Current GitHub reader package:

`https://github.com/KokunoYumeto/modern-latex-manuscripts/tree/{GITHUB_COMMIT}/{GITHUB_PACKAGE}`
"""


def generate_controls(
    draft_id: int,
    predecessor_rows: list[dict[str, str]],
    predecessor_identities: dict[str, dict],
    primary_local: dict[str, dict],
) -> dict[str, dict]:
    result = ORIGINAL_GENERATE_CONTROLS(
        draft_id,
        predecessor_rows,
        predecessor_identities,
        primary_local,
    )
    path = CONTROLS_ROOT / VALIDATION_NAME
    validation = json.loads(path.read_text(encoding="utf-8"))
    validation["sga3_retained_byte_identically"] = False
    validation["sga3_replaced_with_reader_clean_r17_native_update"] = True
    validation["github"]["sga3_merge_commit"] = GITHUB_COMMIT
    validation["readers"]["SGA3"] = {
        "filename": SGA3_PDF,
        "bytes": primary_local[SGA3_PDF]["bytes"],
        "sha256": primary_local[SGA3_PDF]["sha256"],
        "pages": 1_472,
        "named_destinations": 9_487,
        "internal_goto_actions": 4_591,
        "invalid_actions": 0,
        "raster_xobjects": 128,
        "native_updated_exposes": ["X", "XVI", "XVIII", "XXII", "XXIV"],
        "reader_facing_process_notes_removed": True,
        "reader_facing_ai_notes_removed": True,
    }
    validation["direct_master_tex"]["SGA3"] = {
        "filename": SGA3_TEX,
        "bytes": primary_local[SGA3_TEX]["bytes"],
        "sha256": primary_local[SGA3_TEX]["sha256"],
        "reader_facing_process_notes_removed": True,
    }
    validation["sga3_source_history_zip"] = {
        "filename": SGA3_ZIP,
        "bytes": primary_local[SGA3_ZIP]["bytes"],
        "sha256": primary_local[SGA3_ZIP]["sha256"],
        "members": 907,
        "manifest_rows": 906,
        "identity_errors": 0,
    }
    base.save_json(path, validation)
    result[VALIDATION_NAME] = {
        "path": path,
        "bytes": path.stat().st_size,
        "sha256": base.sha256_file(path),
        "md5": base.md5_file(path),
    }
    return result


for module in (previous, base):
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
        "EXPECTED_UNRELATED_RETAINED_FILES": EXPECTED_UNRELATED_RETAINED_FILES,
        "EXPECTED_MANIFEST_ROWS": EXPECTED_MANIFEST_ROWS,
        "EXPECTED_ZIP_ARCHIVES": EXPECTED_ZIP_ARCHIVES,
        "EXPECTED_ZIP_FILE_MEMBERS": EXPECTED_ZIP_FILE_MEMBERS,
        "EXPECTED_ZIP_DIRECTORY_ENTRIES": EXPECTED_ZIP_DIRECTORY_ENTRIES,
        "EXPECTED_ZIP_ALL_ENTRIES": EXPECTED_ZIP_ALL_ENTRIES,
        "EXPECTED_ZIP_UNCOMPRESSED_BYTES": EXPECTED_ZIP_UNCOMPRESSED_BYTES,
        "EXPECTED_GITHUB_READBACK_FILES": EXPECTED_GITHUB_READBACK_FILES,
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
base.fetch_predecessor_manifest = previous.fetch_predecessor_manifest
base.create_or_resume_draft = previous.create_or_resume_draft
base.readme_text = readme_text
base.generate_controls = generate_controls


if __name__ == "__main__":
    base.main()
