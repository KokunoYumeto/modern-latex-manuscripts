#!/usr/bin/env python3
"""Publish the reader-clean SGA1-6 successor containing SGA3 R19."""

from __future__ import annotations

import csv
import hashlib
import importlib.util
import io
import json
import os
import sys
import urllib.request
import zipfile
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
BASE_PATH = (
    SCRIPT_DIR
    / "publish_sga3_compact_bounded_history_zenodo_20260729.py"
)
SPEC = importlib.util.spec_from_file_location("sga_compact_20260729", BASE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("Unable to load the established compact SGA workflow")
previous = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = previous
SPEC.loader.exec_module(previous)
base = previous.base


PREDECESSOR_RECORD = 21680585
PREDECESSOR_DOI = "10.5281/zenodo.21680585"
CONCEPT_DOI = "10.5281/zenodo.20410947"
PUBLICATION_DATE = "2026-07-29"
VERSION = "2026-07-29 reader-clean SGA1-6 with SGA3 R19 native Expose III"
GITHUB_COMMIT = "660650676f0aea58533f9d7692179db9c61e4a0f"
GITHUB_PACKAGE = (
    "sources/sga/"
    "sga3-english-complete-working-reader-clean-r19-native-expose-iii-"
    "20260729"
)

OLD_SGA3_NAMES = {
    "00c00_SGA3_English_Complete_Reader_Native_Update_R18_20260729.pdf",
    "02c00_SGA3_English_Complete_Reader_Native_Update_R18_20260729.tex",
    (
        "10c9_SGA3_English_Complete_Reader_"
        "Source_and_History_R18_20260729.zip"
    ),
}
SGA3_PDF = (
    "00c00_SGA3_English_Complete_Reader_"
    "Native_Update_R19_20260729.pdf"
)
SGA3_TEX = (
    "02c00_SGA3_English_Complete_Reader_"
    "Native_Update_R19_20260729.tex"
)
SGA3_ZIP = (
    "10c9_SGA3_English_Complete_Reader_"
    "Source_and_History_R19_20260729.zip"
)

README_NAME = previous.README_NAME
MANIFEST_NAME = previous.MANIFEST_NAME
VALIDATION_NAME = previous.VALIDATION_NAME
REPLACED_NAMES = OLD_SGA3_NAMES | {
    README_NAME,
    MANIFEST_NAME,
    VALIDATION_NAME,
}

EXPECTED_PREDECESSOR_FILES = 68
EXPECTED_FINAL_FILES = 68
EXPECTED_RETAINED_PREDECESSOR_FILES = 62
EXPECTED_UNRELATED_RETAINED_FILES = 62
EXPECTED_MANIFEST_ROWS = 66
EXPECTED_ZIP_ARCHIVES = 49
EXPECTED_ZIP_FILE_MEMBERS = 4_235
EXPECTED_ZIP_DIRECTORY_ENTRIES = 6
EXPECTED_ZIP_ALL_ENTRIES = 4_241
EXPECTED_ZIP_UNCOMPRESSED_BYTES = 441_759_952
EXPECTED_GITHUB_READBACK_FILES = 12

REPO_ROOT = SCRIPT_DIR.parent
PACKAGE_ROOT = REPO_ROOT / GITHUB_PACKAGE
RECEIPT_ROOT = REPO_ROOT / "manifests" / "published-zenodo"
PREDECESSOR_RECEIPT = (
    RECEIPT_ROOT
    / "20260728_sga3_cumulative_with_x_record_21680585_public_readback.json"
)
CONTROLS_ROOT = (
    Path(os.environ["LOCALAPPDATA"])
    / "Temp"
    / "sga_reader_clean_complete_r19_native_iii_zenodo_controls"
)
READBACK_ROOT = (
    Path(os.environ["LOCALAPPDATA"])
    / "Temp"
    / "sga_reader_clean_complete_r19_native_iii_zenodo_public_readback"
)
DRAFT_STATE = (
    RECEIPT_ROOT
    / "20260729_sga_reader_clean_complete_r19_native_iii_zenodo_draft_state.json"
)

PRIMARY_LOCAL_PATHS = {
    SGA3_PDF: PACKAGE_ROOT / SGA3_PDF,
    SGA3_TEX: PACKAGE_ROOT / SGA3_TEX,
    SGA3_ZIP: PACKAGE_ROOT / SGA3_ZIP,
}
PRIMARY_EXPECTED = {
    SGA3_PDF: (
        6_810_409,
        "4AFBD373859E1B703537E2788F33C64410D7A262FC2485AF8EFA91469856057D",
    ),
    SGA3_TEX: (
        22_203,
        "7E4EE9653AEB052F820841DA58D6659DED35DF0DB7655839CD06CADF2088EA73",
    ),
    SGA3_ZIP: (
        9_737_631,
        "9D5834C3249670B499ECC56B963BE707FCC573DF178EE7A8F92CDE230044F8A4",
    ),
}

NEW_MANIFEST_ROWS = {
    SGA3_PDF: {
        "role": "english_reader",
        "provenance": (
            "preferred reader-clean 1459-page SGA3 R19 native cumulative; "
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
            "direct editable master for the reader-clean SGA3 R19 reader"
        ),
        "status": "preferred_complete_working_reader_master_tex",
    },
    SGA3_ZIP: {
        "role": "grouped_source_and_predecessor",
        "provenance": (
            "exact recursive source closure, build controls, and superseded "
            "R18 reader grouped behind the direct SGA3 reader"
        ),
        "status": (
            "buildable_source_and_history_grouped_not_rights_or_"
            "diagram_fidelity_certification"
        ),
    },
}

DESCRIPTION_PARAGRAPHS = [
    (
        "This same-concept successor preserves 62 files from version "
        "10.5281/zenodo.21680585 byte-identically. It replaces only the "
        "direct SGA3 R18 reader, its direct master TeX, its grouped "
        "source/history archive, and three release controls. SGA1 remains "
        "the default preview."
    ),
    (
        "The preferred SGA3 object is a 1,459-page English cumulative covering "
        "the Editorial Notice, Introduction, Exposes I-XXVI, the Tome-I index, "
        "the Tome-III mathematical guide, and the terminal index. R19 replaces "
        "all 62 Expose-III raster diagrams with lead-reviewed native TeX while "
        "preserving 4,467 valid internal GoTo actions."
    ),
    (
        "The direct reader contains the mathematics, diagrams, labels, and "
        "links rather than project-facing AI, production, source-status, or "
        "workflow commentary. The exact recursive source closure and the "
        "superseded R18 reader remain grouped in one ZIP."
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
    "<p>Reader-first SGA1-6 surface. SGA3 R19 is the direct current-progress "
    "reader; R18 remains in grouped history. SGA1 remains the default "
    "preview.</p>"
)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def verify_manifest(root: Path, expected_sha256: str) -> None:
    manifest = root / "SHA256SUMS.csv"
    if base.sha256_file(manifest) != expected_sha256:
        raise RuntimeError("R19 package manifest mismatch")
    rows = list(
        csv.DictReader(
            io.StringIO(manifest.read_text(encoding="utf-8-sig"), newline="")
        )
    )
    if len(rows) != 11:
        raise RuntimeError("R19 package manifest row boundary mismatch")
    for row in rows:
        path = root / row["filename"]
        if not path.is_file():
            raise FileNotFoundError(path)
        if (path.stat().st_size, base.sha256_file(path)) != (
            int(row["bytes"]),
            row["sha256"].upper(),
        ):
            raise RuntimeError(f"R19 package row mismatch: {path.name}")


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
        raise RuntimeError("R19 GitHub readback file boundary mismatch")
    remote_zip: bytes | None = None
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
            raise RuntimeError(f"R19 GitHub readback mismatch: {path.name}")
        if path.name == SGA3_ZIP:
            remote_zip = data
    if remote_zip is None:
        raise RuntimeError("R19 GitHub archive readback missing")
    with zipfile.ZipFile(io.BytesIO(remote_zip)) as archive:
        if archive.testzip() is not None or len(archive.infolist()) != 907:
            raise RuntimeError("R19 GitHub archive CRC/member mismatch")
        rows = list(
            csv.DictReader(
                io.StringIO(
                    archive.read("SOURCE_BUNDLE_SHA256.csv").decode("utf-8"),
                    newline="",
                )
            )
        )
        if len(rows) != 906:
            raise RuntimeError("R19 GitHub archive manifest boundary mismatch")
        for row in rows:
            data = archive.read(row["relative_path"])
            if (len(data), sha256_bytes(data)) != (
                int(row["bytes"]),
                row["sha256"].upper(),
            ):
                raise RuntimeError(
                    f"R19 GitHub archive member mismatch: "
                    f"{row['relative_path']}"
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
            raise RuntimeError(f"R19 primary identity mismatch: {name}")
        result[name] = identity

    verify_manifest(
        PACKAGE_ROOT,
        "1E4FFFF07A5C11DBFD4FD9075309AEF9E16679A1BE382E3F7F3341B34E57F29F",
    )
    validation = json.loads(
        (PACKAGE_ROOT / "PACKAGE_VALIDATION.json").read_text(encoding="utf-8")
    )
    reader = validation.get("reader", {})
    source = validation.get("source_archive", {})
    if (
        validation.get("status") != "PASS"
        or validation.get("errors") != []
        or reader.get("pages") != 1_459
        or reader.get("named_destinations") != 9_350
        or reader.get("internal_goto_actions") != 4_467
        or reader.get("invalid_actions") != 0
        or reader.get("uri_actions") != 0
        or reader.get("raster_xobjects") != 41
        or reader.get("reader_process_term_hits") != []
        or source.get("members") != 907
        or source.get("manifest_rows") != 906
        or source.get("errors") != []
    ):
        raise RuntimeError("R19 package validation mismatch")
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
    if (
        len(content),
        sha256_bytes(content),
    ) != (
        int(wanted["bytes"]),
        wanted["sha256"].upper(),
    ):
        raise RuntimeError("R19 predecessor release-manifest mismatch")
    rows = list(
        csv.DictReader(
            io.StringIO(content.decode("utf-8-sig"), newline="")
        )
    )
    if len(rows) != 66:
        raise RuntimeError("R19 predecessor release-manifest row mismatch")
    return rows


def create_or_resume_draft(session, token: str, predecessor: dict) -> int:
    return previous.create_or_resume_draft(
        session,
        token,
        predecessor,
    )


def readme_text(draft_id: int) -> str:
    return f"""# Current compact reader-first SGA release

This is one same-concept successor to Zenodo record {PREDECESSOR_RECORD}.
It preserves 62 predecessor files byte-identically and replaces only the SGA3
R18 direct reader/master/source trio plus the three release controls. The
reserved successor is {draft_id}. SGA1 remains the default preview.

The direct reader PDFs contain the mathematics, diagrams, labels, and links.
Project-facing production-status, source-status, AI, and workflow commentary
is kept outside the readers.

The preferred SGA3 reader has 1,459 A4 pages and covers the Editorial Notice,
Introduction, Exposes I-XXVI, Tome-I index, Tome-III mathematical guide, and
terminal index. R19 replaces all 62 Expose-III raster diagrams with native TeX
reviewed against the authority at 5,000 dpi while preserving all 4,467 valid
internal GoTo actions. Its exact recursive source closure and the superseded
R18 reader are grouped in one ZIP.

These are scholarly working translations and TeX editions, not critical
editions, blanket rights clearances, mathematical certifications, peer review,
final diagram-fidelity certification, or tagged-PDF accessibility remediation.
Historical Zenodo versions remain immutable.

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
    for name in (SGA3_PDF, SGA3_TEX, SGA3_ZIP):
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
        raise RuntimeError("R19 release manifest row boundary mismatch")

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
        "schema": "sga_reader_clean_complete_r19_native_iii_zenodo_v1",
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
        "replaced_sga3_files": sorted(OLD_SGA3_NAMES),
        "final_files": EXPECTED_FINAL_FILES,
        "manifest_rows": EXPECTED_MANIFEST_ROWS,
        "direct_sga3_reader": {
            "filename": SGA3_PDF,
            "bytes": primary_local[SGA3_PDF]["bytes"],
            "sha256": primary_local[SGA3_PDF]["sha256"],
            "pages": 1_459,
            "named_destinations": 9_350,
            "internal_goto_actions": 4_467,
            "raster_xobjects": 41,
            "reader_process_term_hits": [],
        },
        "direct_sga3_master": {
            "filename": SGA3_TEX,
            "bytes": primary_local[SGA3_TEX]["bytes"],
            "sha256": primary_local[SGA3_TEX]["sha256"],
        },
        "sga3_source_archive": {
            "filename": SGA3_ZIP,
            "bytes": primary_local[SGA3_ZIP]["bytes"],
            "sha256": primary_local[SGA3_ZIP]["sha256"],
            "members": 907,
            "manifest_rows": 906,
            "contains_predecessor_r18_reader": True,
            "errors": [],
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
