#!/usr/bin/env python3
"""Publish clean reader-facing SGA1, SGA2, SGA4, SGA5, and SGA6 PDFs."""

from __future__ import annotations

import csv
import importlib.util
import io
import json
import os
import shutil
import sys
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
BASE_PATH = (
    SCRIPT_DIR
    / "publish_sga3_reader_clean_complete_working_zenodo_20260728.py"
)
SPEC = importlib.util.spec_from_file_location("sga_reader_clean_base", BASE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("Unable to load the established SGA successor workflow")
workflow = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = workflow
SPEC.loader.exec_module(workflow)
base = workflow.base


PREDECESSOR_RECORD = 21650398
PREDECESSOR_DOI = "10.5281/zenodo.21650398"
CONCEPT_DOI = "10.5281/zenodo.20410947"
PUBLICATION_DATE = "2026-07-28"
VERSION = "2026-07-28 clean reader-facing SGA1-6 presentation"
GITHUB_COMMIT = "02828b25a6112e7d50c7ee499b473d3d2bb43abe"
GITHUB_PACKAGE = (
    "sources/sga/sga1-6-reader-clean-presentation-successor-20260728"
)

PDF_NAMES = {
    "SGA1": (
        "00a_SGA1_English_CompleteVolume_"
        "Working_NoExhaustiveCertification_20260722.pdf"
    ),
    "SGA2": "00b_SGA2_English_Complete_ReferenceLinked_R8_20260723.pdf",
    "SGA4": (
        "00d_SGA4_English_Proper_Exposes_I_XIX_including_Vbis_"
        "ReferenceV2_R7_20260723.pdf"
    ),
    "SGA5": "00e_SGA5_English_ReferenceLinked_R9_20260723.pdf",
    "SGA6": "00f_SGA6_English_Complete_ReferenceLinked_20260723.pdf",
}
TEX_NAMES = {
    "SGA1": "02a_SGA1_English_CompleteVolume_Working_Master_20260722.tex",
    "SGA2": "02b_SGA2_English_Complete_ReferenceLinked_R8_Master_20260723.tex",
    "SGA4": "02d_SGA4_English_Proper_Master_ReferenceV2_R7_20260723.tex",
    "SGA5": "02e_SGA5_English_ReferenceLinked_R9_Master_20260723.tex",
    "SGA6": "02f_SGA6_English_Complete_ReferenceLinked_Master_20260723.tex",
}
README_NAME = "09_README_CURRENT_RELEASE.md"
MANIFEST_NAME = "09a_RELEASE_FILE_MANIFEST.csv"
VALIDATION_NAME = "09b_RELEASE_VALIDATION.json"
REPLACED_NAMES = (
    set(PDF_NAMES.values())
    | set(TEX_NAMES.values())
    | {README_NAME, MANIFEST_NAME, VALIDATION_NAME}
)

EXPECTED_PREDECESSOR_FILES = 92
EXPECTED_PREDECESSOR_MANIFEST_ROWS = 90
EXPECTED_FINAL_FILES = 92
EXPECTED_RETAINED_PREDECESSOR_FILES = 79
EXPECTED_UNRELATED_RETAINED_FILES = 79
EXPECTED_MANIFEST_ROWS = 90
EXPECTED_ZIP_ARCHIVES = 57
EXPECTED_ZIP_FILE_MEMBERS = 5_597
EXPECTED_ZIP_DIRECTORY_ENTRIES = 6
EXPECTED_ZIP_ALL_ENTRIES = 5_603
EXPECTED_ZIP_UNCOMPRESSED_BYTES = 453_999_152
EXPECTED_GITHUB_READBACK_FILES = 13

REPO_ROOT = SCRIPT_DIR.parent
PACKAGE_ROOT = REPO_ROOT / GITHUB_PACKAGE
RECEIPT_ROOT = REPO_ROOT / "manifests" / "published-zenodo"
PREDECESSOR_RECEIPT = (
    RECEIPT_ROOT
    / "20260728_sga3_cumulative_with_x_record_21650398_public_readback.json"
)
CONTROLS_ROOT = (
    Path(os.environ["LOCALAPPDATA"])
    / "Temp"
    / "sga1_6_reader_clean_presentation_zenodo_controls"
)
READBACK_ROOT = (
    Path(os.environ["LOCALAPPDATA"])
    / "Temp"
    / "sga1_6_reader_clean_presentation_zenodo_public_readback"
)
DRAFT_STATE = (
    RECEIPT_ROOT
    / "20260728_sga1_6_reader_clean_presentation_zenodo_draft_state.json"
)

PRIMARY_LOCAL_PATHS = {
    name: PACKAGE_ROOT / name
    for name in list(PDF_NAMES.values()) + list(TEX_NAMES.values())
}
PRIMARY_EXPECTED = {
    PDF_NAMES["SGA1"]: (
        2_539_383,
        "9A0AD352AFA42CEEDB703BE5F6ACC2048389ED42D875697225EE12B806EA7BFE",
    ),
    PDF_NAMES["SGA2"]: (
        2_107_514,
        "B6C4D720C9EA6E3DA210AC6FC22381F9C51C277A6DE25F598989D66C19E4CD89",
    ),
    PDF_NAMES["SGA4"]: (
        4_420_366,
        "982DB88559FE4239CF3381D664792C2262658D511FA0A8A06FE99A1A68512BA5",
    ),
    PDF_NAMES["SGA5"]: (
        2_435_223,
        "7ED9D631479AC044A93D8B08CC63D71E635B3C33C11E549DB7B4AFA6DEF22CAB",
    ),
    PDF_NAMES["SGA6"]: (
        3_219_824,
        "82F5D80F88CBA36F8A1843C37039105895442F45DA94773966E8A9FF797BAAF5",
    ),
    TEX_NAMES["SGA1"]: (
        28_554,
        "8928BB6D12AE79BC9D404908841ADD5ED63B1E0382B061AD0B9805DE1C0C0056",
    ),
    TEX_NAMES["SGA2"]: (
        4_745,
        "33645D4A8481F6ADAE8CD9F17AE156D21A76C6BF9427E1AF348C28CAC23B0382",
    ),
    TEX_NAMES["SGA4"]: (
        3_024,
        "CD3923F791412525A04004F7EADA9F8A088751BC6E82F254900BFFE957413658",
    ),
    TEX_NAMES["SGA5"]: (
        896_688,
        "B4CFF66411FDC91155529823C4AD3B5EA0FFC0AED8AA84FC9750EA3F178C0DFF",
    ),
    TEX_NAMES["SGA6"]: (
        3_348,
        "6CBD2794D46CB233AB9336C4C57AB7FCBEBDCE828B062FBE794EB7DE3E868ABD",
    ),
}
PACKAGE_MANIFEST_SHA256 = (
    "83F8262313B2DEFFDEA3D66CE8BD75936BA357D16D5AA44320A9E0FB356FC45B"
)
PACKAGE_URL = (
    "https://github.com/KokunoYumeto/modern-latex-manuscripts/tree/"
    f"{GITHUB_COMMIT}/{GITHUB_PACKAGE}"
)

READER_METRICS = {
    "SGA1": {
        "pages": 261,
        "named_destinations": 1_210,
        "internal_goto_actions": 1_568,
        "page_format": "A4",
    },
    "SGA2": {
        "pages": 184,
        "named_destinations": 1_536,
        "internal_goto_actions": 1_382,
        "page_format": "A4",
    },
    "SGA4": {
        "pages": 864,
        "named_destinations": 9_421,
        "internal_goto_actions": 6_800,
        "page_format": "A4",
    },
    "SGA5": {
        "pages": 309,
        "named_destinations": 2_343,
        "internal_goto_actions": 1_614,
        "page_format": "US Letter",
    },
    "SGA6": {
        "pages": 377,
        "named_destinations": 3_426,
        "internal_goto_actions": 2_302,
        "page_format": "A4",
    },
}

NEW_MANIFEST_ROWS: dict[str, dict[str, str]] = {}
for sga, name in PDF_NAMES.items():
    status = "preferred_clean_reader"
    if sga == "SGA1":
        status += "_not_exhaustive_reference_v2_certified"
    NEW_MANIFEST_ROWS[name] = {
        "role": "english_reader",
        "provenance": (
            f"reader-facing clean {sga} successor; GitHub {PACKAGE_URL}"
        ),
        "status": status,
    }
for sga, name in TEX_NAMES.items():
    NEW_MANIFEST_ROWS[name] = {
        "role": "english_master_tex",
        "provenance": (
            f"direct editable master for the reader-facing clean {sga} "
            f"successor; GitHub {PACKAGE_URL}"
        ),
        "status": "preferred_clean_reader_master_tex",
    }
NEW_MANIFEST_ROWS[README_NAME] = {
    "role": "manifest_status",
    "provenance": (
        "current compact same-concept release note; GitHub commit "
        + GITHUB_COMMIT
    ),
    "status": "current_release_control",
}

DESCRIPTION_PARAGRAPHS = [
    (
        "This same-concept successor preserves 79 files from version "
        "10.5281/zenodo.21650398 byte-identically, replaces the five direct "
        "SGA1, SGA2, SGA4, SGA5, and SGA6 English readers and their direct "
        "master TeX files, and refreshes three release controls. SGA1 remains "
        "the default preview."
    ),
    (
        "The direct SGA1-6 English readers are reading editions: production "
        "status pages, workflow commentary, internal defect identifiers, and "
        "similar project-facing material have been removed from the reading "
        "surface. Mathematical bodies, original-edition prefaces, diagrams, "
        "labels, and internal links are preserved. The already-clean SGA3 "
        "complete working reader is retained byte-identically."
    ),
    (
        "The five replacement PDFs contain 1,995 pages, 17,936 named "
        "destinations, and 13,666 internal GoTo actions, with zero invalid "
        "actions. SGA1 remains substantially linked but is not claimed to "
        "have exhaustive convention-v2 reference certification."
    ),
    (
        "Provenance, rights, release history, and technical evidence remain "
        "available in the external metadata and grouped archives. Historical "
        "Zenodo versions remain immutable."
    ),
    (
        "These are scholarly working translations and TeX editions, not "
        "critical editions, blanket rights clearances, mathematical "
        "certifications, peer review, or tagged-PDF accessibility "
        "remediation. No new license grant is asserted."
    ),
]
DESCRIPTION_HTML = "\n".join(
    f"<p>{paragraph}</p>" for paragraph in DESCRIPTION_PARAGRAPHS
)
NOTES_HTML = (
    "<p>The direct SGA1-6 English PDFs are now reader-facing editions without "
    "project status pages or workflow commentary. Provenance and technical "
    "history remain in the external release controls and grouped archives. "
    "SGA1 remains the default preview.</p>"
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
    expected_outer = set(PRIMARY_LOCAL_PATHS) | {"README.md"}
    if len(rows) != 11 or {row["filename"] for row in rows} != expected_outer:
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
    if (
        validation.get("status") != "PASS"
        or validation.get("errors") != []
        or validation.get("reader_facing_process_or_status_hits") != []
        or validation.get("critical_edition_claimed") is not False
        or validation.get("new_license_grant") is not False
        or validation.get("manifest", {}).get("sha256")
        != PACKAGE_MANIFEST_SHA256
    ):
        raise RuntimeError("GitHub package validation is not controlling PASS")
    for sga, metrics in READER_METRICS.items():
        reader = validation.get("readers", {}).get(sga, {})
        if (
            reader.get("filename") != PDF_NAMES[sga]
            or reader.get("pages") != metrics["pages"]
            or reader.get("named_destinations")
            != metrics["named_destinations"]
            or reader.get("internal_goto_actions")
            != metrics["internal_goto_actions"]
            or reader.get("expected_page_format") != metrics["page_format"]
            or reader.get("invalid_actions") != 0
            or reader.get("disallowed_pdf_text_hits") != []
            or reader.get("disallowed_pdf_metadata_hits") != []
            or reader.get("direct_master_tex", {}).get("filename")
            != TEX_NAMES[sga]
            or reader.get("direct_master_tex", {}).get("disallowed_hits")
            != []
        ):
            raise RuntimeError(f"Reader validation mismatch: {sga}")
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
retains 79 predecessor files byte-identically, replaces the direct SGA1,
SGA2, SGA4, SGA5, and SGA6 English readers and their direct master TeX
files, and refreshes three release controls. The reserved successor record is
{draft_id}. SGA1 remains the default preview.

## Reader-facing English editions

The direct SGA1-6 English PDFs are reading editions. Project status pages,
workflow commentary, internal defect identifiers, and similar production
material have been removed from the reading surface. Mathematical bodies,
original-edition prefaces, diagrams, labels, and internal links are preserved.

The SGA3 complete working reader was already reader-clean and is retained
byte-identically.

Provenance, rights, release history, and technical evidence remain in the
external metadata and grouped archives. Historical Zenodo versions remain
immutable.

These are scholarly working translations and TeX editions, not critical
editions, blanket rights clearances, mathematical certifications, peer review,
or accessibility-remediated PDFs. SGA1 remains substantially linked but is
not claimed to have exhaustive convention-v2 reference certification.

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
            "one same-concept reader-facing cleanup successor; "
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
        "readers": {
            sga: {
                "filename": PDF_NAMES[sga],
                "bytes": primary_local[PDF_NAMES[sga]]["bytes"],
                "sha256": primary_local[PDF_NAMES[sga]]["sha256"],
                **metrics,
                "invalid_actions": 0,
                "reader_facing_process_notes_removed": True,
            }
            for sga, metrics in READER_METRICS.items()
        },
        "direct_master_tex": {
            sga: {
                "filename": TEX_NAMES[sga],
                "bytes": primary_local[TEX_NAMES[sga]]["bytes"],
                "sha256": primary_local[TEX_NAMES[sga]]["sha256"],
                "reader_facing_process_notes_removed": True,
            }
            for sga in TEX_NAMES
        },
        "sga3_retained_byte_identically": True,
        "zip_surface_expected": {
            "archives": EXPECTED_ZIP_ARCHIVES,
            "file_members": EXPECTED_ZIP_FILE_MEMBERS,
            "directory_entries": EXPECTED_ZIP_DIRECTORY_ENTRIES,
            "all_entries": EXPECTED_ZIP_ALL_ENTRIES,
            "uncompressed_bytes": EXPECTED_ZIP_UNCOMPRESSED_BYTES,
        },
        "reader_facing_process_or_status_hits": [],
        "privacy_hits": [],
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
