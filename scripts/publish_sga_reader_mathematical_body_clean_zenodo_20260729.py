#!/usr/bin/env python3
"""Publish the second project-apparatus-free SGA reader successor."""

from __future__ import annotations

import csv
import hashlib
import importlib.util
import io
import json
import os
import re
import sys
import urllib.request
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
BASE_PATH = (
    SCRIPT_DIR
    / "publish_sga_reader_clean_complete_r18_native_zenodo_20260729.py"
)
SPEC = importlib.util.spec_from_file_location("sga_r18_20260729", BASE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("Unable to load the established SGA workflow")
previous = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = previous
SPEC.loader.exec_module(previous)
base = previous.base


PREDECESSOR_RECORD = 21677179
PREDECESSOR_DOI = "10.5281/zenodo.21677179"
CONCEPT_DOI = "10.5281/zenodo.20410947"
PUBLICATION_DATE = "2026-07-29"
VERSION = "2026-07-29 mathematical-body SGA reader cleanup v2"
GITHUB_COMMIT = os.environ.get("SGA_BODY_CLEAN_V2_GITHUB_COMMIT", "")
if not re.fullmatch(r"[0-9a-f]{40}", GITHUB_COMMIT):
    raise RuntimeError(
        "Set SGA_BODY_CLEAN_V2_GITHUB_COMMIT to the merged 40-character "
        "GitHub commit."
    )
GITHUB_PACKAGE = (
    "sources/sga/"
    "sga1-6-reader-mathematical-body-clean-successor-v2-20260729"
)

SGA2_PDF = "00b_SGA2_English_Complete_ReferenceLinked_R8_20260723.pdf"
SGA3_PDF = (
    "00c00_SGA3_English_Complete_Reader_"
    "Native_Update_R18_20260729.pdf"
)
SGA6_PDF = "00f_SGA6_English_Complete_ReferenceLinked_20260723.pdf"
SGA2_TEX = "02b_SGA2_English_Complete_ReferenceLinked_R8_Master_20260723.tex"
SGA3_TEX = (
    "02c00_SGA3_English_Complete_Reader_"
    "Native_Update_R18_20260729.tex"
)
SGA6_TEX = "02f_SGA6_English_Complete_ReferenceLinked_Master_20260723.tex"

README_NAME = previous.README_NAME
MANIFEST_NAME = previous.MANIFEST_NAME
VALIDATION_NAME = previous.VALIDATION_NAME
PRIMARY_NAMES = {
    SGA2_PDF,
    SGA3_PDF,
    SGA6_PDF,
    SGA2_TEX,
    SGA3_TEX,
    SGA6_TEX,
}
REPLACED_NAMES = PRIMARY_NAMES | {
    README_NAME,
    MANIFEST_NAME,
    VALIDATION_NAME,
}

EXPECTED_PREDECESSOR_FILES = 68
EXPECTED_FINAL_FILES = 68
EXPECTED_RETAINED_PREDECESSOR_FILES = 59
EXPECTED_UNRELATED_RETAINED_FILES = 59
EXPECTED_MANIFEST_ROWS = 66
EXPECTED_ZIP_ARCHIVES = 49
EXPECTED_ZIP_FILE_MEMBERS = 4_235
EXPECTED_ZIP_DIRECTORY_ENTRIES = 6
EXPECTED_ZIP_ALL_ENTRIES = 4_241
EXPECTED_ZIP_UNCOMPRESSED_BYTES = 445_624_376
EXPECTED_GITHUB_READBACK_FILES = 15

REPO_ROOT = SCRIPT_DIR.parent
PACKAGE_ROOT = REPO_ROOT / GITHUB_PACKAGE
RECEIPT_ROOT = REPO_ROOT / "manifests" / "published-zenodo"
PREDECESSOR_RECEIPT = (
    RECEIPT_ROOT
    / "20260728_sga3_cumulative_with_x_record_21677179_public_readback.json"
)
CONTROLS_ROOT = (
    Path(os.environ["LOCALAPPDATA"])
    / "Temp"
    / "sga_reader_mathematical_body_clean_v2_zenodo_controls"
)
READBACK_ROOT = (
    Path(os.environ["LOCALAPPDATA"])
    / "Temp"
    / "sga_reader_mathematical_body_clean_v2_zenodo_public_readback"
)
DRAFT_STATE = (
    RECEIPT_ROOT
    / "20260729_sga_reader_mathematical_body_clean_v2_zenodo_draft_state.json"
)

PRIMARY_LOCAL_PATHS = {
    name: PACKAGE_ROOT / name for name in PRIMARY_NAMES
}
PRIMARY_EXPECTED = {
    SGA2_PDF: (
        2_001_862,
        "AA8663D393CAE37D0D917E16E911F12D64AD90B90829CFCE601557AD759DEDFA",
    ),
    SGA3_PDF: (
        7_466_667,
        "4FA2DC35A71AFE9841BEE3112FCBD985A5FC029BA3D991B408D1064F3AA864D2",
    ),
    SGA6_PDF: (
        3_189_902,
        "E14FF6F4F2AD65BBCAA8410B9DF7DBD480D193A6CA97AF5F4428E7AB6B60B2FE",
    ),
    SGA2_TEX: (
        4_745,
        "33645D4A8481F6ADAE8CD9F17AE156D21A76C6BF9427E1AF348C28CAC23B0382",
    ),
    SGA3_TEX: (
        21_853,
        "9D5BA11B11E895156AB4D708A169E1BD51C19052B3A03A11A4E3BD30E0354396",
    ),
    SGA6_TEX: (
        3_348,
        "6CBD2794D46CB233AB9336C4C57AB7FCBEBDCE828B062FBE794EB7DE3E868ABD",
    ),
}

PAGES = {
    SGA2_PDF: 178,
    SGA3_PDF: 1_462,
    SGA6_PDF: 376,
}
DESTINATIONS = {
    SGA2_PDF: 1_515,
    SGA3_PDF: 9_351,
    SGA6_PDF: 3_424,
}
GOTO_ACTIONS = {
    SGA2_PDF: 1_318,
    SGA3_PDF: 4_467,
    SGA6_PDF: 2_300,
}


def manifest_row(name: str) -> dict[str, str]:
    if name.endswith(".pdf"):
        role = "english_reader"
        status = "preferred_reader_mathematical_body_clean"
    else:
        role = "english_master_tex"
        status = "preferred_reader_source_mathematical_body_clean"
    return {
        "role": role,
        "provenance": (
            "reader-only mathematical-body successor; GitHub "
            "https://github.com/KokunoYumeto/modern-latex-manuscripts/tree/"
            f"{GITHUB_COMMIT}/{GITHUB_PACKAGE}"
        ),
        "status": status,
    }


NEW_MANIFEST_ROWS = {name: manifest_row(name) for name in PRIMARY_NAMES}

DESCRIPTION_PARAGRAPHS = [
    (
        "This same-concept successor preserves 59 files from version "
        "10.5281/zenodo.21677179 byte-identically. It replaces the direct "
        "SGA2, SGA3, and SGA6 English reader PDFs and master TeX files, "
        "plus three release controls. SGA1 remains the default preview."
    ),
    (
        "This second pass removes 34 additional reader-facing project "
        "source-adjudication, production-status, and model/process notes "
        "missed by the first cleanup. The all-six direct English-reader "
        "text scan is clean. SGA1, SGA4, and SGA5 remain byte-identical."
    ),
    (
        "Historical editor-authored notes belonging to the source editions "
        "remain part of the scholarly text. The annotated source/evidence "
        "archives and all immutable predecessor versions remain available "
        "as provenance rather than being placed in the reading surface."
    ),
    (
        "These are scholarly working translations and TeX editions, not "
        "critical editions, blanket rights clearances, mathematical "
        "certifications, peer review, final diagram-fidelity certification, "
        "or tagged-PDF accessibility remediation. No new license grant is "
        "asserted."
    ),
]
DESCRIPTION_HTML = "\n".join(
    f"<p>{paragraph}</p>" for paragraph in DESCRIPTION_PARAGRAPHS
)
NOTES_HTML = (
    "<p>Reader-first SGA1-6 surface. Direct readers contain mathematics "
    "and genuine source-edition material. Project apparatus remains only "
    "in grouped evidence and immutable history.</p>"
)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def verify_github_readback() -> None:
    raw_root = (
        "https://raw.githubusercontent.com/"
        f"KokunoYumeto/modern-latex-manuscripts/{GITHUB_COMMIT}/"
        f"{GITHUB_PACKAGE}/"
    )
    local_files = sorted(
        (path for path in PACKAGE_ROOT.iterdir() if path.is_file()),
        key=lambda path: path.name.casefold(),
    )
    if len(local_files) != EXPECTED_GITHUB_READBACK_FILES:
        raise RuntimeError("GitHub package file boundary mismatch")
    for path in local_files:
        request = urllib.request.Request(
            raw_root + path.name,
            headers={"User-Agent": "modern-latex-manuscripts-readback"},
        )
        with urllib.request.urlopen(request, timeout=180) as response:
            data = response.read()
        if (len(data), sha256_bytes(data)) != (
            path.stat().st_size,
            base.sha256_file(path),
        ):
            raise RuntimeError(f"GitHub readback mismatch: {path.name}")


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
            raise RuntimeError(f"Primary identity mismatch: {name}")
        result[name] = identity

    manifest = PACKAGE_ROOT / "SHA256SUMS.csv"
    if (
        base.sha256_file(manifest)
        != "CDA8D2182ECC393A4ADF85CE21EA55436658EA905871FFAD344C13B19A6F4729"
    ):
        raise RuntimeError("GitHub package manifest mismatch")
    rows = list(
        csv.DictReader(
            io.StringIO(
                manifest.read_text(encoding="utf-8-sig"),
                newline="",
            ),
        )
    )
    if len(rows) != 14:
        raise RuntimeError("GitHub package manifest row mismatch")
    for row in rows:
        path = PACKAGE_ROOT / row["filename"]
        if not path.is_file():
            raise FileNotFoundError(path)
        if (path.stat().st_size, base.sha256_file(path)) != (
            int(row["bytes"]),
            row["sha256"].upper(),
        ):
            raise RuntimeError(f"GitHub package row mismatch: {path.name}")

    build = json.loads(
        (PACKAGE_ROOT / "BUILD_AND_TEXT_VALIDATION.json").read_text(
            encoding="utf-8"
        )
    )
    structure = json.loads(
        (PACKAGE_ROOT / "PDF_STRUCTURE_VALIDATION.json").read_text(
            encoding="utf-8"
        )
    )
    if (
        build.get("status") != "PASS_READER_MATHEMATICAL_BODY_CLEAN_V2"
        or build.get("errors") != []
        or build.get("removals") != 234
        or structure.get("status") != "PASS"
        or structure.get("errors") != []
        or structure.get("package_scan_hits") != {}
    ):
        raise RuntimeError("Package validation mismatch")
    for volume, filename in (
        ("SGA2", SGA2_PDF),
        ("SGA3", SGA3_PDF),
        ("SGA6", SGA6_PDF),
    ):
        current = structure["comparisons"][volume]["reader_facing_current"]
        if (
            current["pages"] != PAGES[filename]
            or current["named_destinations"] != DESTINATIONS[filename]
            or current["link_actions"].get("/GoTo") != GOTO_ACTIONS[filename]
            or current["invalid_named_destinations"] != []
            or current["invalid_goto_destinations"] != []
            or current["metadata_blocked_hits"] != []
        ):
            raise RuntimeError(f"PDF structure mismatch: {volume}")
    for volume in ("SGA1", "SGA2", "SGA3", "SGA4", "SGA5", "SGA6"):
        if structure["reader_text_scan"][volume]["blocked_hits"] != []:
            raise RuntimeError(f"Reader text scan mismatch: {volume}")
    verify_github_readback()
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
    if (len(content), sha256_bytes(content)) != (
        int(wanted["bytes"]),
        wanted["sha256"].upper(),
    ):
        raise RuntimeError("Predecessor release-manifest mismatch")
    rows = list(
        csv.DictReader(
            io.StringIO(content.decode("utf-8-sig"), newline="")
        )
    )
    if len(rows) != EXPECTED_MANIFEST_ROWS:
        raise RuntimeError("Predecessor release-manifest row mismatch")
    return rows


def create_or_resume_draft(session, token: str, predecessor: dict) -> int:
    return previous.create_or_resume_draft(
        session,
        token,
        predecessor,
    )


def readme_text(draft_id: int) -> str:
    return f"""# Current reader-first SGA release

This is one same-concept successor to Zenodo record {PREDECESSOR_RECORD}.
It preserves 59 predecessor files byte-identically and replaces only the
direct SGA2, SGA3, and SGA6 reader PDFs and master TeX files, plus three
release controls. The reserved successor is {draft_id}. SGA1 remains the
default preview.

This second cleanup removes 34 additional project-authored source-
adjudication, production-status, and model/process notes missed by the first
pass. The direct English-reader text scan is clean across SGA1 through SGA6.
SGA1, SGA4, and SGA5 remain byte-identical.

Historical editor-authored notes belonging to the source editions remain in
the scholarly text. Annotated source/evidence archives and immutable
predecessors remain available as provenance rather than appearing in the
reading surface.

These are scholarly working translations and TeX editions, not critical
editions, blanket rights clearances, mathematical certifications, peer review,
final diagram-fidelity certification, or tagged-PDF accessibility remediation.
No new license grant is asserted.

Current GitHub package:

`https://github.com/KokunoYumeto/modern-latex-manuscripts/tree/{GITHUB_COMMIT}/{GITHUB_PACKAGE}`
"""


def generate_controls(
    draft_id: int,
    predecessor_rows: list[dict[str, str]],
    predecessor_identities: dict[str, dict],
    primary_local: dict[str, dict],
) -> dict[str, dict]:
    CONTROLS_ROOT.mkdir(parents=True, exist_ok=True)

    readme_path = CONTROLS_ROOT / README_NAME
    readme_path.write_text(readme_text(draft_id), encoding="utf-8")
    readme_identity = {
        "path": readme_path,
        "bytes": readme_path.stat().st_size,
        "sha256": base.sha256_file(readme_path),
        "md5": base.md5_file(readme_path),
    }

    rows = [
        dict(row)
        for row in predecessor_rows
        if row["filename"] not in REPLACED_NAMES
    ]
    for name in sorted(PRIMARY_NAMES, key=str.casefold):
        identity = primary_local[name]
        metadata = NEW_MANIFEST_ROWS[name]
        rows.append(
            {
                "filename": name,
                "bytes": str(identity["bytes"]),
                "sha256": identity["sha256"],
                "role": metadata["role"],
                "provenance": metadata["provenance"],
                "status": metadata["status"],
            }
        )
    rows.append(
        {
            "filename": README_NAME,
            "bytes": str(readme_identity["bytes"]),
            "sha256": readme_identity["sha256"],
            "role": "release_readme",
            "provenance": "current reader-first release description",
            "status": "public_release_control",
        }
    )
    rows.sort(key=lambda row: row["filename"].casefold())
    if len(rows) != EXPECTED_MANIFEST_ROWS:
        raise RuntimeError("Release manifest row boundary mismatch")

    stream = io.StringIO(newline="")
    writer = csv.DictWriter(
        stream,
        fieldnames=(
            "filename",
            "bytes",
            "sha256",
            "role",
            "provenance",
            "status",
        ),
        lineterminator="\r\n",
    )
    writer.writeheader()
    writer.writerows(rows)
    manifest_path = CONTROLS_ROOT / MANIFEST_NAME
    manifest_path.write_bytes(stream.getvalue().encode("utf-8"))
    manifest_identity = {
        "path": manifest_path,
        "bytes": manifest_path.stat().st_size,
        "sha256": base.sha256_file(manifest_path),
        "md5": base.md5_file(manifest_path),
    }

    validation = {
        "schema": "sga_reader_mathematical_body_clean_zenodo_v2",
        "status": "PASS",
        "errors": [],
        "predecessor_record": PREDECESSOR_RECORD,
        "reserved_successor_record": draft_id,
        "concept_doi": CONCEPT_DOI,
        "github": {
            "commit": GITHUB_COMMIT,
            "package": GITHUB_PACKAGE,
            "anonymous_readback_files": EXPECTED_GITHUB_READBACK_FILES,
            "anonymous_readback_errors": [],
        },
        "predecessor_files": EXPECTED_PREDECESSOR_FILES,
        "retained_predecessor_files": EXPECTED_RETAINED_PREDECESSOR_FILES,
        "replaced_files": sorted(REPLACED_NAMES),
        "final_files": EXPECTED_FINAL_FILES,
        "manifest_rows": EXPECTED_MANIFEST_ROWS,
        "direct_readers": {
            name: {
                "bytes": primary_local[name]["bytes"],
                "sha256": primary_local[name]["sha256"],
                "pages": PAGES[name],
                "named_destinations": DESTINATIONS[name],
                "internal_goto_actions": GOTO_ACTIONS[name],
            }
            for name in (SGA2_PDF, SGA3_PDF, SGA6_PDF)
        },
        "additional_apparatus_removals": 34,
        "cumulative_apparatus_removals": 385,
        "cleaner_source_units_this_build": 234,
        "reader_facing_project_or_model_hits": [],
        "historical_source_editor_notes_preserved": True,
        "annotated_archives_preserved": True,
        "zip_surface_expected": {
            "archives": EXPECTED_ZIP_ARCHIVES,
            "file_members": EXPECTED_ZIP_FILE_MEMBERS,
            "directory_entries": EXPECTED_ZIP_DIRECTORY_ENTRIES,
            "all_entries": EXPECTED_ZIP_ALL_ENTRIES,
            "uncompressed_bytes": EXPECTED_ZIP_UNCOMPRESSED_BYTES,
        },
        "duplicate_concept_created": False,
        "second_draft_created": False,
        "critical_edition_claimed": False,
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

    result = dict(primary_local)
    result[README_NAME] = readme_identity
    result[MANIFEST_NAME] = manifest_identity
    result[VALIDATION_NAME] = validation_identity
    return result


for module in (previous, previous.previous, previous.previous.previous, base):
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
base.fetch_predecessor_manifest = fetch_predecessor_manifest
base.create_or_resume_draft = create_or_resume_draft
base.readme_text = readme_text
base.generate_controls = generate_controls


if __name__ == "__main__":
    base.main()
