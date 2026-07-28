#!/usr/bin/env python3
"""Front the current SGA3 cumulative reader on the compact Zenodo surface."""

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
BASE_PATH = SCRIPT_DIR / "publish_sga3_expose_xiii_zenodo_20260728.py"
SPEC = importlib.util.spec_from_file_location("sga3_reader_order_base", BASE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("Unable to load the established SGA successor workflow")
workflow = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = workflow
SPEC.loader.exec_module(workflow)
base = workflow.base


PREDECESSOR_RECORD = 21647537
PREDECESSOR_DOI = "10.5281/zenodo.21647537"
CONCEPT_DOI = "10.5281/zenodo.20410947"
PUBLICATION_DATE = "2026-07-28"
VERSION = "2026-07-28 SGA3 cumulative reader ordering correction"
GITHUB_COMMIT = "bafbfe8a9f64b70b7cb8a561cb87ccf36594a9bb"
GITHUB_PACKAGE = (
    "sources/sga/"
    "sga3-english-current-progress-full-volume-integration-20260728-r1"
)

OLD_PDF_NAME = (
    "00c_SGA3_English_CurrentProgress_Cumulative_Latest_20260728.pdf"
)
OLD_TEX_NAME = (
    "02c_SGA3_English_CurrentProgress_Cumulative_Latest_20260728.tex"
)
PDF_NAME = (
    "00c00_SGA3_English_CurrentProgress_Cumulative_Latest_20260728.pdf"
)
TEX_NAME = (
    "02c00_SGA3_English_CurrentProgress_Cumulative_Latest_20260728.tex"
)
README_NAME = "09_README_CURRENT_RELEASE.md"
MANIFEST_NAME = "09a_RELEASE_FILE_MANIFEST.csv"
VALIDATION_NAME = "09b_RELEASE_VALIDATION.json"
REPLACED_NAMES = {
    OLD_PDF_NAME,
    OLD_TEX_NAME,
    README_NAME,
    MANIFEST_NAME,
    VALIDATION_NAME,
}

EXPECTED_PREDECESSOR_FILES = 92
EXPECTED_PREDECESSOR_MANIFEST_ROWS = 90
EXPECTED_FINAL_FILES = 92
EXPECTED_RETAINED_PREDECESSOR_FILES = 87
EXPECTED_UNRELATED_RETAINED_FILES = 87
EXPECTED_MANIFEST_ROWS = 90
EXPECTED_ZIP_ARCHIVES = 57
EXPECTED_ZIP_FILE_MEMBERS = 5_563
EXPECTED_ZIP_DIRECTORY_ENTRIES = 6
EXPECTED_ZIP_ALL_ENTRIES = 5_569
EXPECTED_ZIP_UNCOMPRESSED_BYTES = 444_810_625

REPO_ROOT = SCRIPT_DIR.parent
PACKAGE_ROOT = REPO_ROOT / GITHUB_PACKAGE
RECEIPT_ROOT = REPO_ROOT / "manifests" / "published-zenodo"
PREDECESSOR_RECEIPT = (
    RECEIPT_ROOT
    / "20260728_sga3_cumulative_with_x_record_21647537_public_readback.json"
)
CONTROLS_ROOT = (
    Path(os.environ["LOCALAPPDATA"])
    / "Temp"
    / "sga3_reader_order_fix_zenodo_controls"
)
READBACK_ROOT = (
    Path(os.environ["LOCALAPPDATA"])
    / "Temp"
    / "sga3_reader_order_fix_zenodo_public_readback"
)
DRAFT_STATE = (
    RECEIPT_ROOT / "20260728_sga3_reader_order_fix_zenodo_draft_state.json"
)

PRIMARY_LOCAL_PATHS = {
    PDF_NAME: PACKAGE_ROOT / PDF_NAME,
    TEX_NAME: PACKAGE_ROOT / TEX_NAME,
}
PRIMARY_EXPECTED = {
    PDF_NAME: (
        8_650_355,
        "481EEDECAA8635AEAC5CCA91492797AF651D426A80B6A2F2510BDF05EB3DD36D",
    ),
    TEX_NAME: (
        27_421,
        "89214AC97C29A65FF2DE0BF08A2B1037D39112F091EA746EC80B5EC376702087",
    ),
}
PACKAGE_MANIFEST_SHA256 = (
    "262B7E2492DAF72EC37ECA717F9C014D918DC9E9D5247EA02E75C50C173555EB"
)
PACKAGE_URL = (
    "https://github.com/KokunoYumeto/modern-latex-manuscripts/tree/"
    f"{GITHUB_COMMIT}/{GITHUB_PACKAGE}"
)

NEW_MANIFEST_ROWS = {
    PDF_NAME: {
        "role": "reader/reference PDF",
        "provenance": (
            "byte-identical rename of the preferred 1,434-page SGA3 "
            f"current-progress reader; GitHub {PACKAGE_URL}"
        ),
        "status": (
            "preferred_sga3_current_progress_reader_fronted_before_"
            "bounded_component_readers"
        ),
    },
    TEX_NAME: {
        "role": "editable TeX",
        "provenance": (
            "byte-identical rename of the directly accessible cumulative "
            f"master TeX; GitHub {PACKAGE_URL}"
        ),
        "status": "preferred_sga3_current_progress_master_tex",
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
        "This same-concept successor changes no SGA mathematics and adds no "
        "new body content. It preserves 87 predecessor files byte-identically, "
        "renames the preferred SGA3 cumulative PDF and master TeX without "
        "changing their bytes, and refreshes the three release controls."
    ),
    (
        "The explicit 00c00 filename puts the 1,434-page cumulative SGA3 "
        "reader before the smaller bounded SGA3 component readers on "
        "filename-sorted archive pages. The component readers remain directly "
        "available afterward, and older cumulative/source states remain "
        "grouped in the existing ZIP archives."
    ),
    (
        "The preferred reader still integrates the Editorial Notice, "
        "Introduction, Exposes I-XXIII and XXV-XXVI, terminal bibliography, "
        "and Tome III index. Its explicit gaps remain the four-page Tome III "
        "guide and Expose XXIV. A broader 1,492-page internal Loop-1 reader "
        "remains held and is not uploaded by this ordering correction."
    ),
    (
        "This is a working translation and current-progress reader, not a "
        "complete or critical edition of SGA3, blanket rights clearance, "
        "mathematical certification, independent human peer review, or "
        "tagged-PDF accessibility remediation. Historical versions remain "
        "immutable."
    ),
]
DESCRIPTION_HTML = "\n".join(
    f"<p>{paragraph}</p>" for paragraph in DESCRIPTION_PARAGRAPHS
)
NOTES_HTML = (
    "<p>Reader-order correction only. The byte-identical 1,434-page SGA3 "
    "cumulative reader now occupies the 00c00 front slot ahead of bounded "
    "SGA3 component PDFs. SGA1 remains the default preview.</p>"
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
    if (
        validation.get("status") != "PASS"
        or validation.get("errors") != []
        or validation.get("privacy", {}).get("hits") != []
        or validation.get("reader", {}).get("filename") != PDF_NAME
        or validation.get("reader", {}).get("pages") != 1_434
        or validation.get("master_tex", {}).get("filename") != TEX_NAME
    ):
        raise RuntimeError("GitHub package validation is not controlling PASS")
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

This is one byte-neutral ordering successor to Zenodo record
{PREDECESSOR_RECORD}. It retains 87 predecessor files byte-identically,
renames the preferred SGA3 cumulative PDF and master TeX without changing
their bytes, and refreshes three release controls. The reserved successor
record is {draft_id}. SGA1 remains the default preview.

## SGA3 reader first

`{PDF_NAME}` is the preferred 1,434-page SGA3 current-progress cumulative
reader. Its explicit `00c00` slot sorts before the smaller bounded SGA3
readers (`00c12`, `00c13`, and later), so the archive page presents the
actual reading surface first.

`{TEX_NAME}` is the byte-identical direct master TeX. Older cumulative/source
states remain grouped in the existing history ZIPs rather than appearing as
loose competing readers.

The reader contains the Editorial Notice, Introduction, Exposes I-XXIII and
XXV-XXVI, terminal bibliography, and the Tome III index. The four-page Tome
III guide and Expose XXIV remain explicit gaps. The separate 1,492-page
internal Loop-1 reader remains held and is not uploaded here.

This ordering correction makes no complete-SGA3, diagram-final, critical
edition, rights-clearance, peer-review, or accessibility-certification claim.

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
        "status": "PASS_READY_FOR_ONE_SAME_CONCEPT_ORDERING_SUCCESSOR",
        "errors": [],
        "concept_doi": CONCEPT_DOI,
        "predecessor_record": PREDECESSOR_RECORD,
        "predecessor_doi": PREDECESSOR_DOI,
        "reserved_successor_record": draft_id,
        "release_policy": (
            "one same-concept byte-neutral ordering successor; "
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
            "anonymous_readback_files": 11,
            "status": "PASS",
        },
        "ordering": {
            "preferred_sga3_pdf": PDF_NAME,
            "preferred_sga3_pdf_is_first": True,
            "old_pdf_removed_from_successor": OLD_PDF_NAME,
            "old_tex_removed_from_successor": OLD_TEX_NAME,
        },
        "reader": {
            "filename": PDF_NAME,
            "pages": 1_434,
            "bytes": primary_local[PDF_NAME]["bytes"],
            "sha256": primary_local[PDF_NAME]["sha256"],
            "content_changed": False,
            "complete_sga3_claimed": False,
            "diagram_final_claimed": False,
        },
        "master_tex": {
            "filename": TEX_NAME,
            "bytes": primary_local[TEX_NAME]["bytes"],
            "sha256": primary_local[TEX_NAME]["sha256"],
            "content_changed": False,
        },
        "held_reader": {
            "pages": 1_492,
            "uploaded": False,
            "reason": "awaiting explicit final handoff and remaining release gates",
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
