#!/usr/bin/env python3
"""Publish the project-apparatus-free SGA reader-only successor."""

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


PREDECESSOR_RECORD = 21674998
PREDECESSOR_DOI = "10.5281/zenodo.21674998"
CONCEPT_DOI = "10.5281/zenodo.20410947"
PUBLICATION_DATE = "2026-07-29"
VERSION = "2026-07-29 clean mathematical-body SGA1-6 readers"
GITHUB_COMMIT = os.environ.get("SGA_BODY_CLEAN_GITHUB_COMMIT", "")
if not re.fullmatch(r"[0-9a-f]{40}", GITHUB_COMMIT):
    raise RuntimeError(
        "Set SGA_BODY_CLEAN_GITHUB_COMMIT to the merged 40-character "
        "GitHub commit."
    )
GITHUB_PACKAGE = (
    "sources/sga/"
    "sga1-6-reader-mathematical-body-clean-successor-20260729"
)

SGA1_PDF = (
    "00a_SGA1_English_CompleteVolume_"
    "Working_NoExhaustiveCertification_20260722.pdf"
)
SGA2_PDF = "00b_SGA2_English_Complete_ReferenceLinked_R8_20260723.pdf"
SGA3_PDF = (
    "00c00_SGA3_English_Complete_Reader_"
    "Native_Update_R18_20260729.pdf"
)
SGA5_PDF = "00e_SGA5_English_ReferenceLinked_R9_20260723.pdf"
SGA1_TEX = "02a_SGA1_English_CompleteVolume_Working_Master_20260722.tex"
SGA5_TEX = "02e_SGA5_English_ReferenceLinked_R9_Master_20260723.tex"

README_NAME = previous.README_NAME
MANIFEST_NAME = previous.MANIFEST_NAME
VALIDATION_NAME = previous.VALIDATION_NAME
PRIMARY_NAMES = {
    SGA1_PDF,
    SGA2_PDF,
    SGA3_PDF,
    SGA5_PDF,
    SGA1_TEX,
    SGA5_TEX,
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
EXPECTED_GITHUB_READBACK_FILES = 18

REPO_ROOT = SCRIPT_DIR.parent
PACKAGE_ROOT = REPO_ROOT / GITHUB_PACKAGE
RECEIPT_ROOT = REPO_ROOT / "manifests" / "published-zenodo"
PREDECESSOR_RECEIPT = (
    RECEIPT_ROOT
    / "20260728_sga3_cumulative_with_x_record_21674998_public_readback.json"
)
CONTROLS_ROOT = (
    Path(os.environ["LOCALAPPDATA"])
    / "Temp"
    / "sga_reader_mathematical_body_clean_zenodo_controls"
)
READBACK_ROOT = (
    Path(os.environ["LOCALAPPDATA"])
    / "Temp"
    / "sga_reader_mathematical_body_clean_zenodo_public_readback"
)
DRAFT_STATE = (
    RECEIPT_ROOT
    / "20260729_sga_reader_mathematical_body_clean_zenodo_draft_state.json"
)

PRIMARY_LOCAL_PATHS = {
    name: PACKAGE_ROOT / name for name in PRIMARY_NAMES
}
PRIMARY_EXPECTED = {
    SGA1_PDF: (
        2_490_530,
        "D424E4A3E98E8C80C642BE5E5B8AAD813FF3F12D946BF53E237F6508387AC53B",
    ),
    SGA2_PDF: (
        2_045_362,
        "0DD88EBC009E7CD7A5D3D709EBF95F6F3A0BFDC540C6144D299B3991619D879D",
    ),
    SGA3_PDF: (
        7_466_067,
        "75C4D962D2A49C2A9B20636400353FEDFB7213DE979318859C7BBE3D924FD8F2",
    ),
    SGA5_PDF: (
        2_431_050,
        "9BB41B09624BFEB566503EAADD3276B709F9E1AC03E2F71188E0CE7E80A00A38",
    ),
    SGA1_TEX: (
        27_322,
        "0E9B39EEF40BEDECB6CA61F5F5B2E7A7C277330BDC9E8AC7B93882B2920AA77C",
    ),
    SGA5_TEX: (
        895_768,
        "6D3CA0C9B4050C200D875011E2B4D611EC67CD80B3C88011650E272D29DCFF48",
    ),
}

PAGES = {
    SGA1_PDF: 259,
    SGA2_PDF: 179,
    SGA3_PDF: 1_460,
    SGA5_PDF: 309,
}
DESTINATIONS = {
    SGA1_PDF: 1_185,
    SGA2_PDF: 1_525,
    SGA3_PDF: 9_357,
    SGA5_PDF: 2_341,
}
GOTO_ACTIONS = {
    SGA1_PDF: 1_544,
    SGA2_PDF: 1_342,
    SGA3_PDF: 4_475,
    SGA5_PDF: 1_610,
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
        "10.5281/zenodo.21674998 byte-identically. It replaces four "
        "direct English reader PDFs, the changed SGA1 and SGA5 direct "
        "TeX sources, and three release controls. SGA1 remains the "
        "default preview."
    ),
    (
        "The direct SGA1, SGA2, SGA3, and SGA5 readers now present the "
        "mathematical body without project-facing translation-process, "
        "source-adjudication, production-status, or model commentary. "
        "SGA4 and SGA6 were already clean and remain byte-identical."
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
    "and source-edition material, while project apparatus remains only in "
    "grouped evidence and immutable history.</p>"
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
        != "003F0F889D9D2652AE947E5739433856AED7A08B4F654BD528B85C278AE074B1"
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
    if len(rows) != 17:
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
        build.get("status") != "PASS_READER_MATHEMATICAL_BODY_CLEAN"
        or build.get("errors") != []
        or build.get("removals") != 351
        or structure.get("status") != "PASS"
        or structure.get("errors") != []
        or structure.get("package_scan_hits") != {}
    ):
        raise RuntimeError("Package validation mismatch")
    for volume, filename in (
        ("SGA1", SGA1_PDF),
        ("SGA2", SGA2_PDF),
        ("SGA3", SGA3_PDF),
        ("SGA5", SGA5_PDF),
    ):
        current = structure["comparisons"][volume]["reader_only_successor"]
        if (
            current["pages"] != PAGES[filename]
            or current["named_destinations"] != DESTINATIONS[filename]
            or current["link_actions"].get("/GoTo") != GOTO_ACTIONS[filename]
            or current["invalid_named_destinations"] != []
            or current["invalid_goto_destinations"] != []
            or current["metadata_blocked_hits"] != []
        ):
            raise RuntimeError(f"PDF structure mismatch: {volume}")
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
It preserves 59 predecessor files byte-identically and replaces only four
direct reader PDFs, the two changed direct TeX sources, and three release
controls. The reserved successor is {draft_id}. SGA1 remains the default
preview.

The direct SGA1, SGA2, SGA3, and SGA5 readers now present the mathematical
body without project-facing translation-process, source-adjudication,
production-status, or model commentary. SGA4 and SGA6 were already clean and
remain byte-identical.

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
        "schema": "sga_reader_mathematical_body_clean_zenodo_v1",
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
            for name in (SGA1_PDF, SGA2_PDF, SGA3_PDF, SGA5_PDF)
        },
        "apparatus_removals": 351,
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
