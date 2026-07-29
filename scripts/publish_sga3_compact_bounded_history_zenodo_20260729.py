#!/usr/bin/env python3
"""Publish one compact SGA3 historical-checkpoint successor."""

from __future__ import annotations

import csv
import hashlib
import importlib.util
import io
import json
import os
import sys
import zipfile
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
BASE_PATH = (
    SCRIPT_DIR
    / "publish_sga_reader_clean_complete_r17_native_zenodo_20260729.py"
)
SPEC = importlib.util.spec_from_file_location("sga_reader_clean_r17", BASE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("Unable to load the established SGA cleanup workflow")
previous = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = previous
SPEC.loader.exec_module(previous)
base = previous.base

PREDECESSOR_RECORD = 21662699
PREDECESSOR_DOI = "10.5281/zenodo.21662699"
CONCEPT_DOI = "10.5281/zenodo.20410947"
PUBLICATION_DATE = "2026-07-29"
VERSION = "2026-07-29 compact SGA3 bounded checkpoint history"
GITHUB_COMMIT = "1c7b02eff5c4bc4f31619cc22d69feeac2ebe2c0"
GITHUB_PACKAGE = (
    "sources/sga/sga3-compact-bounded-history-20260729"
)

EXPOSES = ("12", "13", "14", "19", "20", "21", "23", "25")
PREDECESSOR_FILE_NAMES = set(
    json.loads(
        (
            SCRIPT_DIR.parent
            / "manifests"
            / "published-zenodo"
            / (
                "20260728_sga3_cumulative_with_x_record_"
                "21662699_public_readback.json"
            )
        ).read_text(encoding="utf-8")
    )["files"]
)
BOUNDED_NAMES = {
    name
    for expose in EXPOSES
    for name in PREDECESSOR_FILE_NAMES
    if name.startswith((f"00c{expose}_", f"02c{expose}_", f"10c{expose}_"))
}
HISTORY_NAMES = {
    *BOUNDED_NAMES,
    "10c8_SGA3_CurrentProgress_Source_History_Latest_20260728.zip",
    (
        "10c_SGA3_Previous_Public_Component_Readers_and_"
        "Source_Archives_Through_XI_20260728.zip"
    ),
}
GROUP_ONE = "10c1_SGA3_Previous_Public_History_Through_XI_20260729.zip"
GROUP_TWO = "10c2_SGA3_Bounded_Checkpoints_XII_XXV_20260729.zip"

README_NAME = previous.README_NAME
MANIFEST_NAME = previous.MANIFEST_NAME
VALIDATION_NAME = previous.VALIDATION_NAME
REPLACED_NAMES = HISTORY_NAMES | {
    README_NAME,
    MANIFEST_NAME,
    VALIDATION_NAME,
}

EXPECTED_PREDECESSOR_FILES = 92
EXPECTED_FINAL_FILES = 68
EXPECTED_RETAINED_PREDECESSOR_FILES = 63
EXPECTED_UNRELATED_RETAINED_FILES = 63
EXPECTED_MANIFEST_ROWS = 66
EXPECTED_ZIP_ARCHIVES = 49
EXPECTED_ZIP_FILE_MEMBERS = 4_235
EXPECTED_ZIP_DIRECTORY_ENTRIES = 6
EXPECTED_ZIP_ALL_ENTRIES = 4_241
EXPECTED_ZIP_UNCOMPRESSED_BYTES = 447_063_821
EXPECTED_GITHUB_READBACK_FILES = 6

REPO_ROOT = SCRIPT_DIR.parent
PACKAGE_ROOT = REPO_ROOT / GITHUB_PACKAGE
RECEIPT_ROOT = REPO_ROOT / "manifests" / "published-zenodo"
PREDECESSOR_RECEIPT = (
    RECEIPT_ROOT
    / "20260728_sga3_cumulative_with_x_record_21662699_public_readback.json"
)
CONTROLS_ROOT = (
    Path(os.environ["LOCALAPPDATA"])
    / "Temp"
    / "sga3_compact_bounded_history_zenodo_controls"
)
READBACK_ROOT = (
    Path(os.environ["LOCALAPPDATA"])
    / "Temp"
    / "sga3_compact_bounded_history_zenodo_public_readback"
)
DRAFT_STATE = (
    RECEIPT_ROOT
    / "20260729_sga3_compact_bounded_history_zenodo_draft_state.json"
)

PRIMARY_LOCAL_PATHS = {
    GROUP_ONE: PACKAGE_ROOT / GROUP_ONE,
    GROUP_TWO: PACKAGE_ROOT / GROUP_TWO,
}
PRIMARY_EXPECTED = {
    GROUP_ONE: (
        86_974_159,
        "D67FCECE46F0C93C4461F22A332ABDA77935C3D0412107E8408A35788FECF053",
    ),
    GROUP_TWO: (
        15_711_199,
        "41113922ABF0DA63BB720E788D985337CA8B8A2BACC3402535AC404B0F76FC9D",
    ),
}

NEW_MANIFEST_ROWS = {
    GROUP_ONE: {
        "role": "grouped_historical_checkpoint_archive",
        "provenance": (
            "exact predecessor-history archives through Expose XI, grouped "
            "behind the clean cumulative reader"
        ),
        "status": "historical_exact_bytes_not_current_reader",
    },
    GROUP_TWO: {
        "role": "grouped_historical_checkpoint_archive",
        "provenance": (
            "exact bounded reader, master, and source trios for Exposes XII, "
            "XIII, XIV, XIX, XX, XXI, XXIII, and XXV"
        ),
        "status": "historical_exact_bytes_not_current_reader",
    },
}

DESCRIPTION_PARAGRAPHS = [
    (
        "This same-concept successor preserves 63 files from version "
        "10.5281/zenodo.21662699 byte-identically. It removes 26 loose "
        "historical SGA3 bounded-reader, master, source, and predecessor-history "
        "objects and preserves every removed byte inside two grouped archives. "
        "SGA1 remains the default preview."
    ),
    (
        "The clean 1,472-page SGA3 R17 cumulative and its editable master remain "
        "direct. The eight bounded Expose XII-XXV checkpoint trios and the two "
        "older predecessor-history archives move behind two ZIPs. Historical "
        "bytes remain exact but no longer interrupt the reader-first file list."
    ),
    (
        "Direct reader PDFs contain the mathematics, diagrams, labels, and "
        "links rather than project-facing AI, production, source-status, or "
        "workflow commentary. Three historical bounded PDFs with a Loop-1 title "
        "remain accessible only as exact history members."
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
    "<p>Reader-first SGA1-6 surface. The clean SGA3 R17 cumulative remains "
    "direct; bounded and predecessor checkpoint history is grouped behind two "
    "archives. SGA1 remains the default preview.</p>"
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

    verify_manifest(
        PACKAGE_ROOT,
        "9A9EE8278C62C346B885B7BBC1D66662DAC5E25B0CBE6CF64D8CDFFC6E8041E3",
    )
    validation = json.loads(
        (PACKAGE_ROOT / "PACKAGE_VALIDATION.json").read_text(encoding="utf-8")
    )
    if (
        validation.get("status") != "PASS"
        or validation.get("errors") != []
        or validation.get("removed_loose_files") != 26
        or validation.get("expected_compact_record_files") != 68
    ):
        raise RuntimeError("Compact-history package validation mismatch")
    for name, expected_members in ((GROUP_ONE, 4), (GROUP_TWO, 26)):
        with zipfile.ZipFile(PRIMARY_LOCAL_PATHS[name]) as archive:
            if archive.testzip() is not None:
                raise RuntimeError(f"Archive CRC failure: {name}")
            if len(archive.infolist()) != expected_members:
                raise RuntimeError(f"Archive member count mismatch: {name}")
            rows = list(
                csv.DictReader(
                    io.StringIO(
                        archive.read("GROUP_MANIFEST.csv").decode("utf-8"),
                        newline="",
                    )
                )
            )
            if len(rows) != expected_members - 1:
                raise RuntimeError(f"Archive manifest row mismatch: {name}")
            for row in rows:
                data = archive.read(row["filename"])
                if (
                    len(data),
                    hashlib.sha256(data).hexdigest().upper(),
                ) != (
                    int(row["bytes"]),
                    row["sha256"].upper(),
                ):
                    raise RuntimeError(
                        f"Archive member identity mismatch: {name}:{row['filename']}"
                    )
    return result


def create_or_resume_draft(session, token: str, predecessor: dict) -> int:
    return previous.previous.ORIGINAL_CREATE_OR_RESUME_DRAFT(
        session,
        token,
        predecessor,
    )


def readme_text(draft_id: int) -> str:
    return f"""# Current compact reader-first SGA release

This is one same-concept successor to Zenodo record {PREDECESSOR_RECORD}.
It preserves 63 unrelated predecessor files byte-identically, groups 26 loose
historical SGA3 objects into two archives, and refreshes the release controls.
The reserved successor is {draft_id}.

The direct reader PDFs contain the mathematics, diagrams, labels, and links.
Project-facing production-status, source-status, AI, and workflow commentary
is kept outside the readers.

The preferred SGA3 reader has 1,472 A4 pages and covers the Editorial Notice,
Introduction, Exposes I-XXVI, Tome-I index, Tome-III mathematical guide, and
terminal index. Its exact recursive source closure and superseded R16 reader
remain grouped in the existing R17 source/history archive.

`{GROUP_ONE}` preserves the two older predecessor-history archives through
Expose XI. `{GROUP_TWO}` preserves the eight exact bounded reader/master/source
trios for Exposes XII, XIII, XIV, XIX, XX, XXI, XXIII, and XXV. Those historical
objects remain available for provenance and audit without appearing as loose
reader choices.

These are scholarly working translations and TeX editions, not critical
editions, blanket rights clearances, mathematical certifications, peer review,
final diagram-fidelity certification, or tagged-PDF accessibility remediation.
Historical Zenodo versions remain immutable. SGA1 remains the default preview.

Current GitHub grouping package:

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
    for name in (GROUP_ONE, GROUP_TWO):
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
            "provenance": "current compact reader-first release description",
            "status": "public_release_control",
        }
    )
    rows.sort(key=lambda row: row["filename"].casefold())
    if len(rows) != EXPECTED_MANIFEST_ROWS:
        raise RuntimeError("Compact release manifest row boundary mismatch")

    manifest_stream = io.StringIO(newline="")
    writer = csv.DictWriter(
        manifest_stream,
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
    manifest_path.write_bytes(manifest_stream.getvalue().encode("utf-8"))
    manifest_identity = {
        "path": manifest_path,
        "bytes": manifest_path.stat().st_size,
        "sha256": base.sha256_file(manifest_path),
        "md5": base.md5_file(manifest_path),
    }

    direct_reader = predecessor_identities[
        "00c00_SGA3_English_Complete_Reader_Native_Update_R17_20260729.pdf"
    ]
    validation = {
        "schema": "sga3_compact_bounded_history_zenodo_v1",
        "status": "PASS",
        "errors": [],
        "predecessor_record": PREDECESSOR_RECORD,
        "reserved_successor_record": draft_id,
        "concept_doi": CONCEPT_DOI,
        "github": {
            "commit": GITHUB_COMMIT,
            "package": GITHUB_PACKAGE,
        },
        "predecessor_files": EXPECTED_PREDECESSOR_FILES,
        "retained_predecessor_files": EXPECTED_RETAINED_PREDECESSOR_FILES,
        "removed_loose_historical_files": len(HISTORY_NAMES),
        "final_files": EXPECTED_FINAL_FILES,
        "manifest_rows": EXPECTED_MANIFEST_ROWS,
        "direct_sga3_reader": {
            "filename": (
                "00c00_SGA3_English_Complete_Reader_"
                "Native_Update_R17_20260729.pdf"
            ),
            "bytes": direct_reader["bytes"],
            "sha256": direct_reader["sha256"],
        },
        "group_archives": {
            GROUP_ONE: {
                "bytes": primary_local[GROUP_ONE]["bytes"],
                "sha256": primary_local[GROUP_ONE]["sha256"],
                "members": 4,
                "errors": [],
            },
            GROUP_TWO: {
                "bytes": primary_local[GROUP_TWO]["bytes"],
                "sha256": primary_local[GROUP_TWO]["sha256"],
                "members": 26,
                "errors": [],
            },
        },
        "zip_surface_expected": {
            "archives": EXPECTED_ZIP_ARCHIVES,
            "file_members": EXPECTED_ZIP_FILE_MEMBERS,
            "directory_entries": EXPECTED_ZIP_DIRECTORY_ENTRIES,
            "all_entries": EXPECTED_ZIP_ALL_ENTRIES,
            "uncompressed_bytes": EXPECTED_ZIP_UNCOMPRESSED_BYTES,
        },
        "reader_facing_process_or_status_hits": [],
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
base.fetch_predecessor_manifest = previous.previous.fetch_predecessor_manifest
base.create_or_resume_draft = create_or_resume_draft
base.readme_text = readme_text
base.generate_controls = generate_controls


if __name__ == "__main__":
    base.main()
