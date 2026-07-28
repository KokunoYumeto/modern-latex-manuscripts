#!/usr/bin/env python3
"""Publish the bounded SGA3 Expose XIII native/reference-v2 checkpoint."""

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
BASE_PATH = (
    SCRIPT_DIR / "publish_sga3_full_volume_working_reader_zenodo_20260728.py"
)
SPEC = importlib.util.spec_from_file_location("sga3_current_release", BASE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("Unable to load the established SGA successor workflow")
current = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = current
SPEC.loader.exec_module(current)
base = current.base


PREDECESSOR_RECORD = 21645478
PREDECESSOR_DOI = "10.5281/zenodo.21645478"
CONCEPT_DOI = "10.5281/zenodo.20410947"
PUBLICATION_DATE = "2026-07-28"
VERSION = "2026-07-28 SGA3 Expose XIII native/reference-v2 checkpoint"
GITHUB_COMMIT = "9ba95cb8839258f409a06a646c87066a7c226291"
GITHUB_PACKAGE = (
    "sources/sga/sga3-expose-xiii-native-reference-v2-working-20260728"
)

PDF_NAME = (
    "00c13_SGA3_Expose_XIII_English_"
    "NativeDiagram_ReferenceV2_Working_20260728.pdf"
)
TEX_NAME = (
    "02c13_SGA3_Expose_XIII_English_"
    "NativeDiagram_ReferenceV2_Working_20260728.tex"
)
ZIP_NAME = (
    "10c13_SGA3_Expose_XIII_"
    "NativeDiagram_ReferenceV2_Source_QA_20260728.zip"
)
README_NAME = "09_README_CURRENT_RELEASE.md"
MANIFEST_NAME = "09a_RELEASE_FILE_MANIFEST.csv"
VALIDATION_NAME = "09b_RELEASE_VALIDATION.json"
REPLACED_NAMES = {README_NAME, MANIFEST_NAME, VALIDATION_NAME}

EXPECTED_PREDECESSOR_FILES = 89
EXPECTED_PREDECESSOR_MANIFEST_ROWS = 87
EXPECTED_FINAL_FILES = 92
EXPECTED_RETAINED_PREDECESSOR_FILES = 86
EXPECTED_UNRELATED_RETAINED_FILES = 86
EXPECTED_MANIFEST_ROWS = 90
EXPECTED_ZIP_ARCHIVES = 57
EXPECTED_ZIP_FILE_MEMBERS = 5_563
EXPECTED_ZIP_DIRECTORY_ENTRIES = 6
EXPECTED_ZIP_ALL_ENTRIES = 5_569
EXPECTED_ZIP_UNCOMPRESSED_BYTES = 444_810_625
EXPECTED_GITHUB_READBACK_FILES = 11
EXPECTED_NEW_ZIP_MEMBERS = 85

REPO_ROOT = SCRIPT_DIR.parent
PACKAGE_ROOT = (
    REPO_ROOT
    / "sources"
    / "sga"
    / "sga3-expose-xiii-native-reference-v2-working-20260728"
)
RECEIPT_ROOT = REPO_ROOT / "manifests" / "published-zenodo"
PREDECESSOR_RECEIPT = (
    RECEIPT_ROOT
    / "20260728_sga3_cumulative_with_x_record_21645478_public_readback.json"
)
CONTROLS_ROOT = (
    Path(os.environ["LOCALAPPDATA"])
    / "Temp"
    / "sga3_expose_xiii_zenodo_controls"
)
READBACK_ROOT = (
    Path(os.environ["LOCALAPPDATA"])
    / "Temp"
    / "sga3_expose_xiii_zenodo_public_readback"
)
DRAFT_STATE = (
    RECEIPT_ROOT / "20260728_sga3_expose_xiii_zenodo_draft_state.json"
)

PRIMARY_LOCAL_PATHS = {
    PDF_NAME: PACKAGE_ROOT / PDF_NAME,
    TEX_NAME: PACKAGE_ROOT / TEX_NAME,
    ZIP_NAME: PACKAGE_ROOT / ZIP_NAME,
}
PRIMARY_EXPECTED = {
    PDF_NAME: (
        245_982,
        "69810FAAF7FF1A502E26B2488D57F95421F4786409D03DD1842E7DFD9ED92BD9",
    ),
    TEX_NAME: (
        1_286,
        "FD0FD9EEEB719A801518CF1D3BC7126CB4E686972F06ACDD35F456118F73CF80",
    ),
    ZIP_NAME: (
        12_851_399,
        "8BA3B5299D26662BDA2F801AA2D462810C45040A8FD4B3AA1585F2A18E946D53",
    ),
}
PACKAGE_MANIFEST_SHA256 = (
    "32A2DB571F9DB6FD603CD7D8977EB5DABFD5CD55235A0E154AD8C1FA661F82C8"
)

PACKAGE_URL = (
    "https://github.com/KokunoYumeto/modern-latex-manuscripts/tree/"
    f"{GITHUB_COMMIT}/{GITHUB_PACKAGE}"
)
NEW_MANIFEST_ROWS = {
    PDF_NAME: {
        "role": "english_reader",
        "provenance": (
            "complete bounded SGA3 Expose XIII native-diagram/reference-v2 "
            f"working reader; GitHub {PACKAGE_URL}"
        ),
        "status": (
            "bounded_complete_expose_xiii_working_reader_"
            "not_complete_sga3_not_rights_clearance"
        ),
    },
    TEX_NAME: {
        "role": "english_master_tex",
        "provenance": (
            "direct editable master for bounded SGA3 Expose XIII; "
            f"GitHub {PACKAGE_URL}"
        ),
        "status": "bounded_working_source_seven_native_diagrams_no_raster",
    },
    ZIP_NAME: {
        "role": "grouped_source_and_qa",
        "provenance": (
            "exact 85-member independently replayed source and QA handoff; "
            f"GitHub {PACKAGE_URL}"
        ),
        "status": (
            "bounded_source_qa_with_target_only_5000dpi_crops_"
            "no_authority_payload_not_rights_clearance"
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
        "10.5281/zenodo.21645478 byte-identically, refreshes three release "
        "controls, and adds a complete bounded SGA3 Expose XIII checkpoint as "
        "a direct reader, direct editable master TeX, and grouped source/QA "
        "ZIP. SGA1 remains the default preview."
    ),
    (
        "The new 32-page A4 reader covers Expose XIII only: Sections 1-6 "
        "through terminal Remarks 6.6(c), corresponding to Polo-Gille local "
        "pages 1-30 / combined-reader pages 805-834, with a hard stop before "
        "Expose XIV / combined page 835. It is not a complete SGA3 reader."
    ),
    (
        "The reader has 274 named destinations, 494 valid internal GoTo "
        "actions, zero broken or external actions, 32 embedded font "
        "resources, no Type3 fonts, and no raster image XObjects. "
        "Reference-v2 R9 closes 166 targets and 899 candidates as 453 active "
        "edges plus 446 residuals, with 468 applied actions and zero "
        "remaining."
    ),
    (
        "All seven diagrams are native editable tikz-cd source. The session "
        "lead compared every current diagram directly to authority at 5000 "
        "dpi; no unresolved ambiguity required 9000-dpi escalation. The ZIP "
        "contains target-only high-zoom crops and no authority PDF or "
        "authority crop."
    ),
    (
        "Four fresh archive XeLaTeX passes completed. The producer and "
        "independent outputs match on all 32 extracted-text pages, decoded "
        "content streams, link sets and rectangles, named destinations, "
        "object counts, and 150-dpi rendered pixels. The exact 85-file handoff "
        "and its self-excluding 83-row manifest replay without error."
    ),
    (
        "The controlling witness is Polo-Gille Expo13.pdf, 30 pages, SHA-256 "
        "24735CAFA57291A71C603712C0588358977856D5971503E6E73F3F2E40A70798. "
        "It is not redistributed. Floris's pre-existing GPU OCR may be "
        "consulted read-only as locator or drafting evidence and was not "
        "regenerated. Jacob C. Reinhold's jcreinhold/sga English lineage at "
        "revision e7a259f3f8608ad3edf9bf6eead3fd504dd2d23e is credited "
        "comparison material, not source authority; its stated CC BY 4.0 "
        "applies only to that contribution."
    ),
    (
        "This package is a bounded scholarly working checkpoint, not complete "
        "SGA3, a critical edition, blanket rights clearance, mathematical "
        "certification, independent human peer review, or tagged-PDF "
        "accessibility remediation. No blanket license or transfer of "
        "underlying rights is asserted. Machine-assisted contributors include "
        "OpenAI Codex / ChatGPT and Anthropic Claude under human direction."
    ),
]
DESCRIPTION_HTML = "\n".join(
    f"<p>{paragraph}</p>" for paragraph in DESCRIPTION_PARAGRAPHS
)
NOTES_HTML = (
    "<p>Compact reader-first SGA surface with 92 public files. The current "
    "1,434-page SGA3 cumulative reader remains the preferred direct reading "
    "surface; this successor adds a direct native/reference-v2 Expose XIII "
    "checkpoint and groups its exact 85-file closure in one ZIP. GitHub "
    f"custody commit: {GITHUB_COMMIT}.</p>"
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
        raise RuntimeError("Outer package manifest identity mismatch")
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
        raise RuntimeError("Outer package manifest exact-set mismatch")
    for row in rows:
        path = PACKAGE_ROOT / row["filename"]
        if (path.stat().st_size, base.sha256_file(path)) != (
            int(row["bytes"]),
            row["sha256"].upper(),
        ):
            raise RuntimeError(f"Outer package mismatch: {row['filename']}")

    validation = json.loads(
        (PACKAGE_ROOT / "PACKAGE_VALIDATION.json").read_text(encoding="utf-8")
    )
    reader = validation.get("reader", {})
    if (
        validation.get("status") != "PASS"
        or validation.get("errors") != []
        or validation.get("privacy", {}).get("hits") != []
        or reader.get("pages") != 32
        or reader.get("named_destinations") != 274
        or reader.get("internal_goto_actions") != 494
        or reader.get("invalid_actions") != 0
        or reader.get("uri_actions") != 0
        or reader.get("raster_xobjects") != 0
    ):
        raise RuntimeError("Package validation is not controlling PASS")

    with zipfile.ZipFile(PRIMARY_LOCAL_PATHS[ZIP_NAME], "r") as archive:
        bad = archive.testzip()
        names = archive.namelist()
        if (
            bad is not None
            or len(names) != 85
            or len(names) != len(set(names))
            or sum(info.file_size for info in archive.infolist()) != 17_762_764
        ):
            raise RuntimeError("Source ZIP boundary or CRC mismatch")
        for name in names:
            base.safe_zip_name(name)
        internal_manifest = archive.read("SHA256SUMS.csv")
        if base.hashlib.sha256(internal_manifest).hexdigest().upper() != (
            "9723E97AF581C6FAE2D11C3B8C75F8DEA9DF4FFDF8DEF154D77457B8E81F4072"
        ):
            raise RuntimeError("Source ZIP manifest identity mismatch")
        source_rows = list(
            csv.DictReader(
                io.StringIO(internal_manifest.decode("utf-8-sig"))
            )
        )
        expected_source = set(names) - {
            "SHA256SUMS.csv",
            "FINAL_PACKAGE_VALIDATION.json",
        }
        if (
            len(source_rows) != 83
            or {row["relative_path"] for row in source_rows} != expected_source
        ):
            raise RuntimeError("Source ZIP manifest exact-set mismatch")
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
                    f"Source ZIP member mismatch: {row['relative_path']}"
                )
        embedded = json.loads(
            archive.read("FINAL_PACKAGE_VALIDATION.json").decode("utf-8")
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
retains 86 predecessor files byte-identically, refreshes three release
controls, and adds complete bounded SGA3 Expose XIII as a direct reader,
direct editable master TeX, and grouped source/QA ZIP. The reserved successor
record is {draft_id}. SGA1 remains the default preview.

## Current SGA3 reading surface

`00c_SGA3_English_CurrentProgress_Cumulative_Latest_20260728.pdf` remains the
preferred 1,434-page current-progress cumulative reader. It contains the
Editorial Notice, Introduction, Exposes I-XXIII and XXV-XXVI, terminal
bibliography, and the Tome III index. The Tome III guide and Expose XXIV are
explicit gaps.

The newly direct `{PDF_NAME}` is the complete bounded Expose-XIII reader:
Sections 1-6 through Remarks 6.6(c), 32 A4 pages, 274 named destinations, and
494 valid internal GoTo actions. It does not claim complete SGA3.

## Native diagrams and source

All seven Expose-XIII diagrams are native editable TeX and the public PDF has
no raster XObjects. The top-level lead compared all seven to authority at 5000
dpi. No unresolved ambiguity required 9000-dpi escalation.

`{ZIP_NAME}` contains the exact 85-file handoff: six editable TeX files,
reference-v2 and source/formula controls, all-page renders, target-only
5000-dpi crops, provenance, and exact manifests. Authority PDFs, authority
crops, OCR bodies, comparison bodies, private paths, and raw caches are
excluded.

## Authority, rights, and lineage

The controlling Polo-Gille authority is not redistributed. Floris's
pre-existing GPU OCR may be consulted read-only as locator/drafting evidence
and was not regenerated. Jacob C. Reinhold's `jcreinhold/sga` English lineage
at commit `e7a259f3f8608ad3edf9bf6eead3fd504dd2d23e` is credited comparison
material, not authority; its stated CC BY 4.0 applies only to that
contribution.

No blanket license or transfer of underlying rights is asserted.
Machine-assisted contributors include OpenAI Codex / ChatGPT and Anthropic
Claude under human direction.

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
        raise RuntimeError(
            f"Expected {EXPECTED_MANIFEST_ROWS} rows, got {len(release_rows)}"
        )
    if len({row["filename"] for row in release_rows}) != len(release_rows):
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
        writer.writerows(release_rows)
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
            "source_zip_members_read_back": EXPECTED_NEW_ZIP_MEMBERS,
            "status": "PASS",
        },
        "reader": {
            "filename": PDF_NAME,
            "scope": "complete bounded SGA3 Expose XIII only",
            "pages": 32,
            "bytes": primary_local[PDF_NAME]["bytes"],
            "sha256": primary_local[PDF_NAME]["sha256"],
            "named_destinations": 274,
            "valid_internal_goto": 494,
            "broken_or_external_actions": 0,
            "font_resources": 32,
            "type3_fonts": 0,
            "raster_xobjects": 0,
            "complete_sga3_claimed": False,
        },
        "reference_v2": {
            "targets": 166,
            "candidates": 899,
            "active_edges": 453,
            "residuals": 446,
            "applied_actions": 468,
            "remaining": 0,
        },
        "source_zip": {
            "filename": ZIP_NAME,
            "members": 85,
            "uncompressed_bytes": 17_762_764,
            "sha256": primary_local[ZIP_NAME]["sha256"],
            "editable_tex_files": 6,
            "native_diagrams": 7,
            "target_only_5000dpi_crops": 21,
            "authority_payload_members": 0,
            "privacy_hits": 0,
        },
        "independent_rebuild": {
            "passes": 4,
            "pages_exact": 32,
            "text_exact": True,
            "decoded_content_exact": True,
            "destinations_and_links_exact": True,
            "rendered_pixels_exact": True,
        },
        "diagram_rule": {
            "existing_600_1200_evidence_invalidated": False,
            "reopen_300_only_approvals": True,
            "native_tex_required_for_diagram_final_delivery": True,
            "default_review_dpi": 5000,
            "ambiguity_review_dpi": 9000,
            "xiii_diagrams_closed": 7,
            "xiii_diagrams_open": 0,
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


for module in (current, base):
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
        "EXPECTED_PREDECESSOR_MANIFEST_ROWS": (
            EXPECTED_PREDECESSOR_MANIFEST_ROWS
        ),
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
        "EXPECTED_ZIP_UNCOMPRESSED_BYTES": (
            EXPECTED_ZIP_UNCOMPRESSED_BYTES
        ),
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
