#!/usr/bin/env python3
"""Publish the clean SGA2 R9 reader on the existing SGA concept."""

from __future__ import annotations

import copy
import csv
import hashlib
import importlib.util
import io
import json
import subprocess
import sys
import urllib.request
import zipfile
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
BASE_PATH = SCRIPT_DIR / "publish_sga3_reader_clean_r22_zenodo_20260729.py"
SPEC = importlib.util.spec_from_file_location("sga_reader_clean_r22", BASE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("Unable to load the established SGA publication workflow")
previous = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = previous
SPEC.loader.exec_module(previous)
base = previous.base


PREDECESSOR_RECORD = 21690335
PREDECESSOR_DOI = "10.5281/zenodo.21690335"
CONCEPT_DOI = "10.5281/zenodo.20410947"
PUBLICATION_DATE = "2026-07-29"
VERSION = "2026-07-29 compact SGA1-6 reader surface (SGA2 clean R9)"
TITLE = previous.TITLE
DEFAULT_PREVIEW = previous.DEFAULT_PREVIEW

DESCRIPTION_HTML = "\n".join(
    (
        "<p>English readers for SGA 1 through SGA 6 are listed first in "
        "numerical order. Available French texts and editable TeX masters "
        "follow; supplementary source and historical files are grouped in "
        "ZIP archives.</p>",
        "<p>The SGA2 R9 direct reader preserves the mathematical body, "
        "references, and genuine historical edition apparatus while moving "
        "project correction history, source-status commentary, and "
        "production notes into its grouped source/history archive.</p>",
        "<p>Direct reader PDFs contain mathematics and historical edition "
        "apparatus. Project workflow and correction-history records are "
        "outside reader pages.</p>",
        "<p>These editions do not transfer rights in the underlying French "
        "works. Historical Zenodo versions remain immutable.</p>",
    )
)

GITHUB_COMMIT = "1501f6a02df1c111ecb2ff0d935e9c5a5eaf4621"
GITHUB_PACKAGE = (
    "sources/sga/"
    "sga2-english-reader-clean-r9-no-correction-status-notes-20260729"
)
GITHUB_CONTROLS_PACKAGE = (
    "sources/sga/sga-reader-clean-r23-sga2-r9-release-controls-20260729"
)
REPO_ROOT = SCRIPT_DIR.parent
PACKAGE_ROOT = REPO_ROOT / GITHUB_PACKAGE
CONTROLS_PACKAGE_ROOT = REPO_ROOT / GITHUB_CONTROLS_PACKAGE

SGA2_PDF = "00b_SGA2_English_Reader.pdf"
OLD_SGA2_ZIP = (
    "10b_SGA2_English_Complete_ReferenceLinked_R8_TeX_Ledgers_20260723.zip"
)
SGA2_ZIP = "10b_SGA2_English_Source_and_History_R9_20260729.zip"
CONTROLS_ZIP = "10z_SGA_Current_Release_Controls_20260729.zip"

README_NAME = previous.README_NAME
MANIFEST_NAME = previous.MANIFEST_NAME
VALIDATION_NAME = previous.VALIDATION_NAME
REPLACED_NAMES = {SGA2_PDF, OLD_SGA2_ZIP, CONTROLS_ZIP}

PRIMARY_LOCAL_PATHS = {
    SGA2_PDF: PACKAGE_ROOT / SGA2_PDF,
    SGA2_ZIP: PACKAGE_ROOT / SGA2_ZIP,
    CONTROLS_ZIP: CONTROLS_PACKAGE_ROOT / CONTROLS_ZIP,
}
PRIMARY_EXPECTED = {
    SGA2_PDF: (
        1_997_990,
        "09FCCBF53CE1AA45F80C7B3E63169D28740935F095F3E4A4350C70A41D2623A8",
    ),
    SGA2_ZIP: (
        2_407_624,
        "074FCBCA617C74E8456C9AF64666AB6E99C611955D720A8556B62A6C322856F1",
    ),
    CONTROLS_ZIP: (
        6_506,
        "F87F16D8FC7626D0B9D44302D44F71E1D794F6F7EDF7C7D540147A358C0445D2",
    ),
}

R9_PACKAGE_MANIFEST = (
    811,
    "9F82B061E296BC9248BEAF41842540A13975F636205DE2AF25F57E9829703EAC",
)
R9_PACKAGE_VALIDATION = (
    2_602,
    "0E832760D4AA6B6B51A8741300EA92FB6945A179EAEFBEFE44188D35E8D8C177",
)
CONTROLS_PACKAGE_MANIFEST = (
    310,
    "03F77217C15CE66E6ECFAD7E083AC8E43E24D19CB0250286A4720F81E6514E71",
)
CONTROLS_PACKAGE_VALIDATION = (
    465,
    "FE728414E649823B6A462ACD1CCDF2BB133E34364CBF4C46F995583DFF595CFA",
)

R9_SOURCE_MEMBERS = 47
R9_SOURCE_MANIFEST_ROWS = 46
R9_SOURCE_UNCOMPRESSED_BYTES = 5_048_871
R9_SOURCE_MANIFEST_SHA256 = (
    "15F25FDF18CDE8DAE032CD844DBCCA635FB3BF6FD5A32549269C6D0944B10B9D"
)
CONTROL_MEMBER_EXPECTED = {
    README_NAME: (
        1_299,
        "E6BE024D225D5E4527DB33D29C6D7FF90F1565DB620C5BA44D6DCF8CD59FB3E0",
    ),
    MANIFEST_NAME: (
        14_126,
        "3D85A1AAAF3B1826C0412DA80F3A4E63EEDE324ADF07BABC8FB72FE6C53A33E9",
    ),
    VALIDATION_NAME: (
        1_998,
        "878B865584C47310770F1F83C08100F990B40E445F24BFA664F9B2BE23247620",
    ),
    "PACKED_CONTROL_SHA256.csv": (
        320,
        "CE479B4BDC1A00721C2B206049175ECF0C015AB8F25653BEC102E1D1292A7441",
    ),
}

EXPECTED_PREDECESSOR_FILES = 66
EXPECTED_FINAL_FILES = 66
EXPECTED_RETAINED_PREDECESSOR_FILES = 63
EXPECTED_UNRELATED_RETAINED_FILES = 63
EXPECTED_MANIFEST_ROWS = 65
EXPECTED_ZIP_ARCHIVES = 50
EXPECTED_ZIP_FILE_MEMBERS = 4_282
EXPECTED_ZIP_DIRECTORY_ENTRIES = 6
EXPECTED_ZIP_ALL_ENTRIES = 4_288
EXPECTED_ZIP_UNCOMPRESSED_BYTES = 440_193_233
EXPECTED_GITHUB_READBACK_FILES = 13

RECEIPT_ROOT = REPO_ROOT / "manifests" / "published-zenodo"
PREDECESSOR_RECEIPT = (
    RECEIPT_ROOT
    / "20260728_sga3_cumulative_with_x_record_21690335_public_readback.json"
)
PREDECESSOR_ZIP_RECEIPT = (
    RECEIPT_ROOT
    / "20260728_sga3_cumulative_with_x_record_21690335_zip_member_readback.json"
)
TEMP_ROOT = previous.TEMP_ROOT
CONTROLS_ROOT = TEMP_ROOT / "sga2_reader_clean_r9_zenodo_controls"
READBACK_ROOT = TEMP_ROOT / "sga2_reader_clean_r9_zenodo_readback"
DRAFT_STATE = (
    RECEIPT_ROOT / "20260729_sga2_reader_clean_r9_zenodo_draft_state.json"
)
NEW_MANIFEST_ROWS: dict[str, dict] = {}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def identity(path: Path) -> tuple[int, str]:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return path.stat().st_size, digest.hexdigest().upper()


def read_csv_bytes(data: bytes) -> list[dict[str, str]]:
    return list(
        csv.DictReader(
            io.StringIO(data.decode("utf-8-sig"), newline="")
        )
    )


def git_blob_bytes(package: str, filename: str) -> bytes:
    result = subprocess.run(
        ["git", "show", f"{GITHUB_COMMIT}:{package}/{filename}"],
        cwd=REPO_ROOT,
        check=True,
        capture_output=True,
    )
    return result.stdout


def verify_github_directory(
    package: str,
    root: Path,
    expected_files: int,
) -> None:
    files = sorted(
        (path for path in root.iterdir() if path.is_file()),
        key=lambda path: path.name.casefold(),
    )
    if len(files) != expected_files:
        raise RuntimeError(f"GitHub package boundary mismatch: {package}")
    raw_root = (
        "https://raw.githubusercontent.com/"
        f"KokunoYumeto/modern-latex-manuscripts/{GITHUB_COMMIT}/{package}/"
    )
    for path in files:
        committed = git_blob_bytes(package, path.name)
        request = urllib.request.Request(
            raw_root + path.name,
            headers={"User-Agent": "modern-latex-manuscripts-readback"},
        )
        with urllib.request.urlopen(request, timeout=600) as response:
            remote = response.read()
        if remote != committed:
            raise RuntimeError(f"GitHub readback mismatch: {package}/{path.name}")


def verify_outer_manifest(
    package: str,
    root: Path,
    expected_identity: tuple[int, str],
    expected_rows: int,
) -> None:
    path = root / "SHA256SUMS.csv"
    if identity(path) != expected_identity:
        raise RuntimeError(f"Outer manifest identity mismatch: {root.name}")
    rows = read_csv_bytes(path.read_bytes())
    if len(rows) != expected_rows:
        raise RuntimeError(f"Outer manifest row mismatch: {root.name}")
    for row in rows:
        data = git_blob_bytes(package, row["filename"])
        if (len(data), sha256_bytes(data)) != (
            int(row["bytes"]),
            row["sha256"].upper(),
        ):
            raise RuntimeError(
                f"Outer manifest member mismatch: {root.name}/{row['filename']}"
            )


def verify_primary_local_files() -> dict[str, dict]:
    verify_github_directory(GITHUB_PACKAGE, PACKAGE_ROOT, 9)
    verify_github_directory(GITHUB_CONTROLS_PACKAGE, CONTROLS_PACKAGE_ROOT, 4)
    verify_outer_manifest(
        GITHUB_PACKAGE,
        PACKAGE_ROOT,
        R9_PACKAGE_MANIFEST,
        8,
    )
    verify_outer_manifest(
        GITHUB_CONTROLS_PACKAGE,
        CONTROLS_PACKAGE_ROOT,
        CONTROLS_PACKAGE_MANIFEST,
        3,
    )

    if identity(PACKAGE_ROOT / "PACKAGE_VALIDATION.json") != (
        R9_PACKAGE_VALIDATION
    ):
        raise RuntimeError("R9 package validation identity mismatch")
    validation = json.loads(
        (PACKAGE_ROOT / "PACKAGE_VALIDATION.json").read_text(encoding="utf-8")
    )
    reader = validation.get("reader", {})
    source = validation.get("source_archive", {})
    replay = validation.get("isolated_replay", {})
    removals = validation.get("reader_apparatus_removals", {})
    if (
        validation.get("status") != "PASS"
        or validation.get("errors") != []
        or reader.get("pages") != 178
        or reader.get("named_destinations") != 1_514
        or reader.get("internal_goto_actions") != 1_307
        or reader.get("invalid_actions") != 0
        or reader.get("uri_actions") != 0
        or reader.get("reader_process_term_hits") != []
        or reader.get("project_correction_phrase_hits") != []
        or reader.get("historical_serre_editorial_note_count") != 1
        or removals.get("total") != 61
        or removals.get("correction_status_rows") != 9
        or replay.get("status") != "PASS"
        or replay.get("text_pages_exact") != 178
        or replay.get("decoded_content_streams_exact") != 178
        or replay.get("normalized_destinations_exact") != 1_514
        or replay.get("internal_links_exact") != 1_307
        or replay.get("errors") != []
        or source.get("members") != R9_SOURCE_MEMBERS
        or source.get("manifest_rows") != R9_SOURCE_MANIFEST_ROWS
        or source.get("errors") != []
    ):
        raise RuntimeError("R9 package validation content mismatch")

    if identity(
        CONTROLS_PACKAGE_ROOT / "PACKAGE_VALIDATION.json"
    ) != CONTROLS_PACKAGE_VALIDATION:
        raise RuntimeError("R23 controls validation identity mismatch")
    control_validation = json.loads(
        (CONTROLS_PACKAGE_ROOT / "PACKAGE_VALIDATION.json").read_text(
            encoding="utf-8"
        )
    )
    if (
        control_validation.get("status") != "PASS"
        or control_validation.get("errors") != []
        or control_validation.get("source_record") != PREDECESSOR_RECORD
        or control_validation.get("prospective_zenodo_files")
        != EXPECTED_FINAL_FILES
        or control_validation.get("manifest_rows") != EXPECTED_MANIFEST_ROWS
    ):
        raise RuntimeError("R23 controls package validation mismatch")

    source_zip = PACKAGE_ROOT / SGA2_ZIP
    with zipfile.ZipFile(source_zip, "r") as archive:
        if archive.testzip() is not None:
            raise RuntimeError("R9 source ZIP failed CRC validation")
        infos = archive.infolist()
        if any(info.is_dir() for info in infos):
            raise RuntimeError("R9 source ZIP has directory entries")
        if (len(infos), sum(info.file_size for info in infos)) != (
            R9_SOURCE_MEMBERS,
            R9_SOURCE_UNCOMPRESSED_BYTES,
        ):
            raise RuntimeError("R9 source ZIP boundary mismatch")
        manifest_data = archive.read("SOURCE_BUNDLE_SHA256.csv")
        rows = read_csv_bytes(manifest_data)
        if len(rows) != R9_SOURCE_MANIFEST_ROWS:
            raise RuntimeError("R9 source ZIP manifest row mismatch")
        if sha256_bytes(manifest_data) != R9_SOURCE_MANIFEST_SHA256:
            raise RuntimeError("R9 source ZIP manifest identity mismatch")
        for row in rows:
            data = archive.read(row["relative_path"])
            if (len(data), sha256_bytes(data)) != (
                int(row["bytes"]),
                row["sha256"].upper(),
            ):
                raise RuntimeError(
                    f"R9 source ZIP member mismatch: {row['relative_path']}"
                )

    controls_zip = CONTROLS_PACKAGE_ROOT / CONTROLS_ZIP
    with zipfile.ZipFile(controls_zip, "r") as archive:
        if archive.testzip() is not None:
            raise RuntimeError("R23 controls ZIP failed CRC validation")
        seen = {}
        for info in archive.infolist():
            base.safe_zip_name(info.filename)
            if info.is_dir():
                raise RuntimeError("R23 controls ZIP has a directory entry")
            data = archive.read(info)
            seen[info.filename] = (len(data), sha256_bytes(data))
        packed_rows = read_csv_bytes(
            archive.read("PACKED_CONTROL_SHA256.csv")
        )
    if seen != CONTROL_MEMBER_EXPECTED or len(packed_rows) != 3:
        raise RuntimeError("R23 controls ZIP member mismatch")
    for row in packed_rows:
        name = row["filename"]
        if (
            name not in {README_NAME, MANIFEST_NAME, VALIDATION_NAME}
            or (int(row["bytes"]), row["sha256"].upper())
            != CONTROL_MEMBER_EXPECTED[name]
        ):
            raise RuntimeError(f"R23 packed-control mismatch: {name}")

    result = {}
    for name, path in PRIMARY_LOCAL_PATHS.items():
        observed = identity(path)
        if observed != PRIMARY_EXPECTED[name]:
            raise RuntimeError(f"Primary local identity mismatch: {name}")
        result[name] = {
            "path": path,
            "bytes": observed[0],
            "sha256": observed[1],
            "md5": base.md5_file(path),
        }
    return result


def fetch_predecessor_manifest(
    session,
    predecessor: dict,
    receipt: dict,
) -> list[dict[str, str]]:
    entry = base.entries_map(predecessor)[CONTROLS_ZIP]
    response = base.check(
        session.get(entry["links"]["content"], timeout=(30, 180)),
        {200},
    )
    data = response.content
    wanted = receipt["files"][CONTROLS_ZIP]
    if (len(data), sha256_bytes(data)) != (
        int(wanted["bytes"]),
        wanted["sha256"].upper(),
    ):
        raise RuntimeError("Predecessor controls ZIP readback mismatch")
    with zipfile.ZipFile(io.BytesIO(data), "r") as archive:
        if archive.testzip() is not None:
            raise RuntimeError("Predecessor controls ZIP CRC mismatch")
        rows = read_csv_bytes(archive.read(MANIFEST_NAME))
    if len(rows) != 65:
        raise RuntimeError("Predecessor packed manifest boundary mismatch")
    return rows


def generate_controls(
    draft_id: int,
    predecessor_rows: list[dict[str, str]],
    predecessor_identities: dict[str, dict],
    primary_local: dict[str, dict],
) -> dict[str, dict]:
    if draft_id <= PREDECESSOR_RECORD:
        raise RuntimeError("Reserved successor record is not newer")
    if len(predecessor_rows) != 65:
        raise RuntimeError("Predecessor packed control rows changed")
    if len(predecessor_identities) != EXPECTED_PREDECESSOR_FILES:
        raise RuntimeError("Predecessor identity boundary changed")
    if set(primary_local) != set(PRIMARY_LOCAL_PATHS):
        raise RuntimeError("R9 primary file set changed")

    expected_without_controls = {
        name: row
        for name, row in predecessor_identities.items()
        if name not in REPLACED_NAMES
    }
    expected_without_controls[SGA2_PDF] = primary_local[SGA2_PDF]
    expected_without_controls[SGA2_ZIP] = primary_local[SGA2_ZIP]
    if len(expected_without_controls) != EXPECTED_MANIFEST_ROWS:
        raise RuntimeError("Prospective release-manifest boundary mismatch")

    with zipfile.ZipFile(primary_local[CONTROLS_ZIP]["path"], "r") as archive:
        rows = read_csv_bytes(archive.read(MANIFEST_NAME))
        validation = json.loads(archive.read(VALIDATION_NAME).decode("utf-8"))
    row_map = {row["filename"]: row for row in rows}
    if len(row_map) != len(rows) or set(row_map) != set(expected_without_controls):
        raise RuntimeError("R23 prospective release-manifest set mismatch")
    for name, wanted in expected_without_controls.items():
        row = row_map[name]
        if (int(row["bytes"]), row["sha256"].upper()) != (
            wanted["bytes"],
            wanted["sha256"],
        ):
            raise RuntimeError(
                f"R23 prospective release-manifest mismatch: {name}"
            )
    if (
        validation.get("status") != "PASS"
        or validation.get("errors") != []
        or validation.get("source_record") != PREDECESSOR_RECORD
        or validation.get("prospective_files") != EXPECTED_FINAL_FILES
        or validation.get("retained_files")
        != EXPECTED_RETAINED_PREDECESSOR_FILES
        or validation.get("default_preview") != DEFAULT_PREVIEW
    ):
        raise RuntimeError("R23 packed release validation mismatch")
    return primary_local


def create_or_resume_draft(session, token: str, predecessor: dict) -> int:
    auth = {"Authorization": f"Bearer {token}"}
    vendor = {
        **auth,
        "Accept": "application/vnd.inveniordm.v1+json",
    }
    if DRAFT_STATE.is_file():
        state = json.loads(DRAFT_STATE.read_text(encoding="utf-8"))
        if state.get("published"):
            raise RuntimeError("Tracked successor is already published")
        draft_id = int(state["draft_id"])
        if (
            int(state["predecessor_record"]) != PREDECESSOR_RECORD
            or state["concept_doi"] != CONCEPT_DOI
        ):
            raise RuntimeError("Tracked successor state does not match R9")
        draft = base.modern_draft(session, token, draft_id)
        if len(draft["files"]["entries"]) != EXPECTED_PREDECESSOR_FILES:
            raise RuntimeError("Tracked successor inherited-file boundary changed")
        return draft_id
    existing = session.get(
        f"{base.API}/records/{PREDECESSOR_RECORD}/draft",
        headers=vendor,
        timeout=(30, 180),
    )
    if existing.status_code == 200:
        raise RuntimeError("An untracked successor draft already exists")
    base.check(existing, {404})

    legacy = base.check(
        session.get(
            f"{base.API}/deposit/depositions/{PREDECESSOR_RECORD}",
            headers=auth,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    if (
        legacy.get("state") != "done"
        or not legacy.get("submitted")
        or not legacy.get("links", {}).get("newversion")
    ):
        raise RuntimeError("Predecessor is not a submitted versioning base")
    created = base.check(
        session.post(
            legacy["links"]["newversion"],
            headers=auth,
            timeout=(30, 300),
        ),
        {201},
    ).json()
    deposit = base.check(
        session.get(
            created["links"]["latest_draft"],
            headers=auth,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    draft_id = int(deposit["id"])
    if set(base.legacy_file_map(deposit)) != set(base.entries_map(predecessor)):
        raise RuntimeError("Successor draft did not inherit predecessor set")
    base.save_json(
        DRAFT_STATE,
        {
            "status": "OPEN_TRACKED_DRAFT",
            "predecessor_record": PREDECESSOR_RECORD,
            "draft_id": draft_id,
            "concept_doi": CONCEPT_DOI,
            "published": False,
        },
    )
    return draft_id


def assert_metadata(metadata: dict) -> None:
    if metadata.get("title") != TITLE:
        raise RuntimeError("Title metadata mismatch")
    if metadata.get("version") != VERSION:
        raise RuntimeError("Version metadata mismatch")
    if metadata.get("publication_date") != PUBLICATION_DATE:
        raise RuntimeError("Publication-date metadata mismatch")
    if metadata.get("description") != DESCRIPTION_HTML:
        raise RuntimeError("Description metadata mismatch")
    if metadata.get("contributors"):
        raise RuntimeError("Reader-facing contributor badges are forbidden")
    if any(
        row.get("type", {}).get("id") == "notes"
        for row in (metadata.get("additional_descriptions") or [])
    ):
        raise RuntimeError("Reader-facing release notes are forbidden")


def publish_draft(
    session,
    token: str,
    draft_id: int,
    expected: dict[str, dict],
) -> dict:
    draft = base.modern_draft(session, token, draft_id)
    if set(draft["files"]["entries"]) != set(expected):
        raise RuntimeError("Cannot publish: modern draft set mismatch")

    metadata = copy.deepcopy(draft["metadata"])
    metadata["title"] = TITLE
    metadata["version"] = VERSION
    metadata["publication_date"] = PUBLICATION_DATE
    metadata["description"] = DESCRIPTION_HTML
    metadata["contributors"] = []
    metadata["additional_descriptions"] = [
        row
        for row in (metadata.get("additional_descriptions") or [])
        if row.get("type", {}).get("id") != "notes"
    ]
    payload = {
        "access": draft["access"],
        "files": {
            "enabled": True,
            "default_preview": DEFAULT_PREVIEW,
            "order": sorted(expected, key=str.casefold),
        },
        "metadata": metadata,
        "custom_fields": draft.get("custom_fields", {}),
    }
    if draft.get("pids"):
        payload["pids"] = draft["pids"]
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.inveniordm.v1+json",
        "Content-Type": "application/json",
    }
    patched = base.check(
        session.put(
            f"{base.API}/records/{draft_id}/draft",
            headers=headers,
            json=payload,
            timeout=(30, 300),
        ),
        {200},
    ).json()
    assert_metadata(patched["metadata"])
    reread = base.modern_draft(session, token, draft_id)
    assert_metadata(reread["metadata"])
    if reread["files"].get("default_preview") != DEFAULT_PREVIEW:
        raise RuntimeError("Draft default preview mismatch")
    if set(reread["files"]["entries"]) != set(expected):
        raise RuntimeError("Draft lost exact file set after metadata patch")

    published = base.check(
        session.post(
            reread["links"]["publish"],
            headers={
                "Authorization": f"Bearer {token}",
                "Accept": "application/vnd.inveniordm.v1+json",
            },
            timeout=(30, 600),
        ),
        {200, 202},
    ).json()
    if (
        int(published["id"]) != draft_id
        or base.concept_doi(published) != CONCEPT_DOI
    ):
        raise RuntimeError("Published response escaped the existing concept")
    doi = base.version_doi(published)
    state = json.loads(DRAFT_STATE.read_text(encoding="utf-8"))
    state.update({"published": True, "doi": doi})
    base.save_json(DRAFT_STATE, state)
    receipt = {
        "status": "PUBLISH_ACCEPTED",
        "errors": [],
        "record_id": draft_id,
        "doi": doi,
        "concept_doi": CONCEPT_DOI,
        "file_count": EXPECTED_FINAL_FILES,
        "default_preview": DEFAULT_PREVIEW,
        "contributors": [],
        "notes_present": False,
        "duplicate_concept_created": False,
        "second_draft_created": False,
    }
    base.save_json(
        RECEIPT_ROOT
        / f"20260729_sga2_reader_clean_r9_record_{draft_id}_publish_response.json",
        receipt,
    )
    return receipt


for name, value in {
    "CONCEPT_DOI": CONCEPT_DOI,
    "PREDECESSOR_RECORD": PREDECESSOR_RECORD,
    "PREDECESSOR_DOI": PREDECESSOR_DOI,
    "PUBLICATION_DATE": PUBLICATION_DATE,
    "VERSION": VERSION,
    "TITLE": TITLE,
    "GITHUB_COMMIT": GITHUB_COMMIT,
    "GITHUB_PACKAGE": GITHUB_PACKAGE,
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
    "EXPECTED_GITHUB_READBACK_FILES": EXPECTED_GITHUB_READBACK_FILES,
    "RECEIPT_ROOT": RECEIPT_ROOT,
    "PREDECESSOR_RECEIPT": PREDECESSOR_RECEIPT,
    "CONTROLS_ROOT": CONTROLS_ROOT,
    "READBACK_ROOT": READBACK_ROOT,
    "DRAFT_STATE": DRAFT_STATE,
    "PRIMARY_LOCAL_PATHS": PRIMARY_LOCAL_PATHS,
    "NEW_MANIFEST_ROWS": NEW_MANIFEST_ROWS,
    "DESCRIPTION_HTML": DESCRIPTION_HTML,
    "DEFAULT_PREVIEW": DEFAULT_PREVIEW,
}.items():
    setattr(previous, name, value)
    setattr(base, name, value)

base.verify_primary_local_files = verify_primary_local_files
base.fetch_predecessor_manifest = fetch_predecessor_manifest
base.create_or_resume_draft = create_or_resume_draft
base.generate_controls = generate_controls
base.assert_metadata = assert_metadata
base.publish_draft = publish_draft


if __name__ == "__main__":
    base.main()
