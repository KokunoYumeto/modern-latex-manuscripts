#!/usr/bin/env python3
"""Publish the SGA3 R22 clean-reader successor on the existing SGA concept."""

from __future__ import annotations

import copy
import importlib.util
import json
import subprocess
import sys
import urllib.request
import zipfile
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
BASE_PATH = SCRIPT_DIR / "publish_sga3_reader_clean_r21_zenodo_20260729.py"
SPEC = importlib.util.spec_from_file_location("sga_reader_clean_r21_20260729", BASE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("Unable to load the established SGA3 publication workflow")
previous = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = previous
SPEC.loader.exec_module(previous)
base = previous.base


PREDECESSOR_RECORD = 21688473
PREDECESSOR_DOI = "10.5281/zenodo.21688473"
CONCEPT_DOI = "10.5281/zenodo.20410947"
PUBLICATION_DATE = "2026-07-29"
VERSION = "2026-07-29 compact SGA1-6 reader surface (SGA3 R22)"
TITLE = previous.TITLE
DEFAULT_PREVIEW = previous.DEFAULT_PREVIEW

DESCRIPTION_HTML = "\n".join(
    (
        "<p>English readers for SGA 1 through SGA 6 are listed first in "
        "numerical order. Available French texts and editable TeX masters "
        "follow; supplementary source and historical files are grouped in "
        "ZIP archives.</p>",
        "<p>The SGA3 reader has 1,459 A4 pages and contains the Editorial "
        "Notice, Introduction, Exposes I-XXVI, the Tome-I index, the Tome-III "
        "mathematical guide, and the terminal index. Exposes V, VI, VIII, IX, "
        "XI, and XV use their newer native-diagram source.</p>",
        "<p>The direct PDFs contain mathematical text, diagrams, references, "
        "and original historical editorial apparatus. Production and "
        "source-reading records are outside the reader pages and grouped "
        "with the supporting archives.</p>",
        "<p>These editions do not transfer rights in the underlying French "
        "works. Historical Zenodo versions remain immutable.</p>",
    )
)

GITHUB_COMMIT = "a261f96765619edecdfeceece1b96fd838bb5bac"
GITHUB_PACKAGE = (
    "sources/sga/sga3-english-reader-clean-r22-native-viii-ix-xi-xv-20260729"
)
GITHUB_CONTROLS_PACKAGE = (
    "sources/sga/sga-reader-clean-r22-release-controls-20260729"
)
REPO_ROOT = SCRIPT_DIR.parent
PACKAGE_ROOT = REPO_ROOT / GITHUB_PACKAGE
CONTROLS_PACKAGE_ROOT = REPO_ROOT / GITHUB_CONTROLS_PACKAGE

SGA3_PDF = "00c_SGA3_English_Reader.pdf"
OLD_SGA3_ZIP = "10c_SGA3_English_Source_and_History_R21_20260729.zip"
SGA3_ZIP = "10c_SGA3_English_Source_and_History_R22_20260729.zip"
CONTROLS_ZIP = "10z_SGA_Current_Release_Controls_20260729.zip"

README_NAME = previous.README_NAME
MANIFEST_NAME = previous.MANIFEST_NAME
VALIDATION_NAME = previous.VALIDATION_NAME
REPLACED_NAMES = {SGA3_PDF, OLD_SGA3_ZIP, CONTROLS_ZIP}

PRIMARY_LOCAL_PATHS = {
    SGA3_PDF: PACKAGE_ROOT / SGA3_PDF,
    SGA3_ZIP: PACKAGE_ROOT / SGA3_ZIP,
    CONTROLS_ZIP: CONTROLS_PACKAGE_ROOT / CONTROLS_ZIP,
}
PRIMARY_EXPECTED = {
    SGA3_PDF: (
        6_809_005,
        "911B4AC6DB00D2F9CC58BF769F84F6811CD4A15B5FB4846ABB822B154407E8F2",
    ),
    SGA3_ZIP: (
        9_855_572,
        "633C676A5A7DB45C0FFF629A9706017A5B949459E62F76096D024F10383CDBCD",
    ),
    CONTROLS_ZIP: (
        6_134,
        "5B4C100579E8B75E7D051BEFF455AA8CB98BBABCA7DF7849BF9289B78E5590F0",
    ),
}

R22_PACKAGE_MANIFEST = (
    1_195,
    "9DEFE413DB11D21C76CC94D51A0E207E452B77320A4938742718FA4F71DF355F",
)
R22_PACKAGE_VALIDATION = (
    10_785,
    "989BD58A043A4E7746CDB4773DB341426B8D61A0C3BF723CA46691C4B7D1D0F9",
)
CONTROLS_PACKAGE_MANIFEST = (
    310,
    "C6762A3A2A3FA442935A1BD541765ABC476DF76D72CE1766B52A649DCF72213E",
)
CONTROLS_PACKAGE_VALIDATION = (
    457,
    "1656E845DF35D67BC8739E1648835505D88A80F26E2FC0CF087C06BC6D646B5A",
)

R22_SOURCE_MEMBERS = 951
R22_SOURCE_MANIFEST_ROWS = 950
R22_SOURCE_UNCOMPRESSED_BYTES = 13_594_258
R22_SOURCE_MANIFEST_SHA256 = (
    "966F2DA78427877123598F4F229A35144CAFF82004363DA1EDC7B2574B99CC3B"
)
CONTROL_MEMBER_EXPECTED = {
    README_NAME: (
        1_251,
        "44C41785E6A0F8B5AA57A870A3ED604C979CA8377DD68BBC81C095394E19FD9C",
    ),
    MANIFEST_NAME: (
        14_081,
        "5FBA69BF759E858E59490DD3CAE86D2BEAC4E2D11E80867F5EFF5E6844369682",
    ),
    VALIDATION_NAME: (
        1_231,
        "F994054ED04F72FFD029D6B56E0D114FC8CB021D60D17A8FA8934905A8C2D86D",
    ),
    "PACKED_CONTROL_SHA256.csv": (
        320,
        "199997208BF74CB7FFBA070CD9660C548738CC317128C05B48ADF2E20F56DA36",
    ),
}

EXPECTED_PREDECESSOR_FILES = 66
EXPECTED_FINAL_FILES = 66
EXPECTED_RETAINED_PREDECESSOR_FILES = 63
EXPECTED_UNRELATED_RETAINED_FILES = 63
EXPECTED_MANIFEST_ROWS = 65
EXPECTED_ZIP_ARCHIVES = 50
EXPECTED_ZIP_FILE_MEMBERS = 4_283
EXPECTED_ZIP_DIRECTORY_ENTRIES = 6
EXPECTED_ZIP_ALL_ENTRIES = 4_289
EXPECTED_ZIP_UNCOMPRESSED_BYTES = 442_104_173
EXPECTED_GITHUB_READBACK_FILES = 17

RECEIPT_ROOT = REPO_ROOT / "manifests" / "published-zenodo"
PREDECESSOR_RECEIPT = (
    RECEIPT_ROOT
    / "20260728_sga3_cumulative_with_x_record_21688473_public_readback.json"
)
PREDECESSOR_ZIP_RECEIPT = (
    RECEIPT_ROOT
    / "20260728_sga3_cumulative_with_x_record_21688473_zip_member_readback.json"
)
TEMP_ROOT = previous.TEMP_ROOT
CONTROLS_ROOT = TEMP_ROOT / "sga3_reader_clean_r22_zenodo_controls"
READBACK_ROOT = TEMP_ROOT / "sga3_reader_clean_r22_zenodo_readback"
DRAFT_STATE = (
    RECEIPT_ROOT / "20260729_sga3_reader_clean_r22_zenodo_draft_state.json"
)
NEW_MANIFEST_ROWS: dict[str, dict] = {}


def git_blob_bytes(package: str, filename: str) -> bytes:
    result = subprocess.run(
        [
            "git",
            "show",
            f"{GITHUB_COMMIT}:{package}/{filename}",
        ],
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
    if previous.identity(path) != expected_identity:
        raise RuntimeError(f"Outer manifest identity mismatch: {root.name}")
    rows = previous.read_csv_bytes(path.read_bytes())
    if len(rows) != expected_rows:
        raise RuntimeError(f"Outer manifest row mismatch: {root.name}")
    for row in rows:
        data = git_blob_bytes(package, row["filename"])
        if (len(data), previous.sha256_bytes(data)) != (
            int(row["bytes"]),
            row["sha256"].upper(),
        ):
            raise RuntimeError(
                f"Outer manifest member mismatch: {root.name}/{row['filename']}"
            )


def verify_primary_local_files() -> dict[str, dict]:
    verify_github_directory(GITHUB_PACKAGE, PACKAGE_ROOT, 13)
    verify_github_directory(
        GITHUB_CONTROLS_PACKAGE,
        CONTROLS_PACKAGE_ROOT,
        4,
    )
    verify_outer_manifest(
        GITHUB_PACKAGE,
        PACKAGE_ROOT,
        R22_PACKAGE_MANIFEST,
        12,
    )
    verify_outer_manifest(
        GITHUB_CONTROLS_PACKAGE,
        CONTROLS_PACKAGE_ROOT,
        CONTROLS_PACKAGE_MANIFEST,
        3,
    )

    if previous.identity(PACKAGE_ROOT / "PACKAGE_VALIDATION.json") != (
        R22_PACKAGE_VALIDATION
    ):
        raise RuntimeError("R22 package validation identity mismatch")
    validation = json.loads(
        (PACKAGE_ROOT / "PACKAGE_VALIDATION.json").read_text(encoding="utf-8")
    )
    reader = validation.get("reader", {})
    replacements = validation.get("source_replacements", {})
    source = validation.get("source_archive", {})
    if (
        validation.get("status") != "PASS"
        or validation.get("errors") != []
        or reader.get("pages") != 1_459
        or reader.get("named_destinations") != 9_345
        or reader.get("internal_goto_actions") != 4_461
        or reader.get("invalid_actions") != 0
        or reader.get("uri_actions") != 0
        or reader.get("reader_process_term_hits") != []
        or validation.get("reader_apparatus_removals", {}).get("total") != 32
        or replacements.get("files_replayed") != 34
        or replacements.get("files_changed") != 20
        or replacements.get("exposes") != ["VIII", "IX", "XI", "XV"]
        or source.get("members") != R22_SOURCE_MEMBERS
        or source.get("manifest_rows") != R22_SOURCE_MANIFEST_ROWS
        or source.get("errors") != []
    ):
        raise RuntimeError("R22 package validation content mismatch")

    if previous.identity(
        CONTROLS_PACKAGE_ROOT / "PACKAGE_VALIDATION.json"
    ) != CONTROLS_PACKAGE_VALIDATION:
        raise RuntimeError("R22 controls validation identity mismatch")
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
        raise RuntimeError("R22 controls package validation mismatch")

    source_zip = PACKAGE_ROOT / SGA3_ZIP
    with zipfile.ZipFile(source_zip, "r") as archive:
        if archive.testzip() is not None:
            raise RuntimeError("R22 source ZIP failed CRC validation")
        infos = archive.infolist()
        if any(info.is_dir() for info in infos):
            raise RuntimeError("R22 source ZIP has directory entries")
        if (len(infos), sum(info.file_size for info in infos)) != (
            R22_SOURCE_MEMBERS,
            R22_SOURCE_UNCOMPRESSED_BYTES,
        ):
            raise RuntimeError("R22 source ZIP boundary mismatch")
        rows = previous.read_csv_bytes(archive.read("SOURCE_BUNDLE_SHA256.csv"))
        if len(rows) != R22_SOURCE_MANIFEST_ROWS:
            raise RuntimeError("R22 source ZIP manifest row mismatch")
        if (
            previous.sha256_bytes(archive.read("SOURCE_BUNDLE_SHA256.csv"))
            != R22_SOURCE_MANIFEST_SHA256
        ):
            raise RuntimeError("R22 source ZIP manifest identity mismatch")
        for row in rows:
            data = archive.read(row["relative_path"])
            if (len(data), previous.sha256_bytes(data)) != (
                int(row["bytes"]),
                row["sha256"].upper(),
            ):
                raise RuntimeError(
                    f"R22 source ZIP member mismatch: {row['relative_path']}"
                )

    controls_zip = CONTROLS_PACKAGE_ROOT / CONTROLS_ZIP
    with zipfile.ZipFile(controls_zip, "r") as archive:
        if archive.testzip() is not None:
            raise RuntimeError("R22 controls ZIP failed CRC validation")
        seen = {}
        for info in archive.infolist():
            base.safe_zip_name(info.filename)
            if info.is_dir():
                raise RuntimeError("R22 controls ZIP has a directory entry")
            data = archive.read(info)
            seen[info.filename] = (len(data), previous.sha256_bytes(data))
        packed_rows = previous.read_csv_bytes(
            archive.read("PACKED_CONTROL_SHA256.csv")
        )
    if seen != CONTROL_MEMBER_EXPECTED or len(packed_rows) != 3:
        raise RuntimeError("R22 controls ZIP member mismatch")
    for row in packed_rows:
        name = row["filename"]
        if (
            name not in {README_NAME, MANIFEST_NAME, VALIDATION_NAME}
            or (int(row["bytes"]), row["sha256"].upper())
            != CONTROL_MEMBER_EXPECTED[name]
        ):
            raise RuntimeError(f"R22 packed-control mismatch: {name}")

    result = {}
    for name, path in PRIMARY_LOCAL_PATHS.items():
        observed = previous.identity(path)
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
    if (len(data), previous.sha256_bytes(data)) != (
        int(wanted["bytes"]),
        wanted["sha256"].upper(),
    ):
        raise RuntimeError("Predecessor controls ZIP readback mismatch")
    with zipfile.ZipFile(previous.io.BytesIO(data), "r") as archive:
        if archive.testzip() is not None:
            raise RuntimeError("Predecessor controls ZIP CRC mismatch")
        rows = previous.read_csv_bytes(archive.read(MANIFEST_NAME))
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
        raise RuntimeError("R22 primary file set changed")

    expected_without_controls = {
        name: row
        for name, row in predecessor_identities.items()
        if name not in REPLACED_NAMES
    }
    expected_without_controls[SGA3_PDF] = primary_local[SGA3_PDF]
    expected_without_controls[SGA3_ZIP] = primary_local[SGA3_ZIP]
    if len(expected_without_controls) != EXPECTED_MANIFEST_ROWS:
        raise RuntimeError("Prospective release-manifest boundary mismatch")

    with zipfile.ZipFile(primary_local[CONTROLS_ZIP]["path"], "r") as archive:
        rows = previous.read_csv_bytes(archive.read(MANIFEST_NAME))
        validation = json.loads(archive.read(VALIDATION_NAME).decode("utf-8"))
    row_map = {row["filename"]: row for row in rows}
    if len(row_map) != len(rows) or set(row_map) != set(expected_without_controls):
        raise RuntimeError("R22 prospective release-manifest set mismatch")
    for name, wanted in expected_without_controls.items():
        row = row_map[name]
        if (int(row["bytes"]), row["sha256"].upper()) != (
            wanted["bytes"],
            wanted["sha256"],
        ):
            raise RuntimeError(
                f"R22 prospective release-manifest identity mismatch: {name}"
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
        raise RuntimeError("R22 packed release validation mismatch")
    return primary_local


def create_or_resume_draft(session, token: str, predecessor: dict) -> int:
    if DRAFT_STATE.is_file():
        state = json.loads(DRAFT_STATE.read_text(encoding="utf-8"))
        if state.get("published"):
            raise RuntimeError("Tracked successor is already published")
        draft_id = int(state["draft_id"])
        if (
            int(state["predecessor_record"]) != PREDECESSOR_RECORD
            or state["concept_doi"] != CONCEPT_DOI
        ):
            raise RuntimeError("Tracked successor state does not match R22")
        draft = base.modern_draft(session, token, draft_id)
        if len(draft["files"]["entries"]) != EXPECTED_PREDECESSOR_FILES:
            raise RuntimeError("Tracked successor inherited-file boundary changed")
        return draft_id
    return previous.create_or_resume_draft(session, token, predecessor)


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
    previous.assert_metadata(patched["metadata"])
    reread = base.modern_draft(session, token, draft_id)
    previous.assert_metadata(reread["metadata"])
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
        / f"20260729_sga3_reader_clean_r22_record_{draft_id}_publish_response.json",
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
base.assert_metadata = previous.assert_metadata
base.publish_draft = publish_draft


if __name__ == "__main__":
    base.main()
