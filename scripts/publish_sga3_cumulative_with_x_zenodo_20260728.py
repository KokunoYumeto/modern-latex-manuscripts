#!/usr/bin/env python3
"""Publish and read back the X-inclusive compact SGA3 cumulative successor."""

from __future__ import annotations

import copy
import argparse
import csv
import hashlib
import io
import json
import os
import re
import shutil
import time
import zipfile
from pathlib import Path, PurePosixPath
from urllib.parse import quote

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


API = "https://zenodo.org/api"
CONCEPT_DOI = "10.5281/zenodo.20410947"
PREDECESSOR_RECORD = 21632790
PREDECESSOR_DOI = "10.5281/zenodo.21632790"
PUBLICATION_DATE = "2026-07-28"
VERSION = "2026-07-28 SGA3 current-progress cumulative I-XI except XII, plus XIII"
DEFAULT_PREVIEW = (
    "00a_SGA1_English_CompleteVolume_Working_"
    "NoExhaustiveCertification_20260722.pdf"
)

GITHUB_COMMIT = "6ee7a55dd3ae2b2133b75eebd7a3e28e83703b29"
GITHUB_PACKAGE = (
    "sources/sga/"
    "sga3-english-current-progress-cumulative-through-xiii-20260728"
)

OLD_PDF = (
    "00c_SGA3_English_CurrentProgress_Cumulative_I-IX_XI_XIII_20260728.pdf"
)
OLD_TEX = (
    "02c_SGA3_English_CurrentProgress_Cumulative_I-IX_XI_XIII_20260728.tex"
)
OLD_SOURCE_ZIP = (
    "10c8_SGA3_CurrentProgress_Integration_Source_I-IX_XI_XIII_20260728.zip"
)
README_NAME = "09_README_CURRENT_RELEASE.md"
MANIFEST_NAME = "09a_RELEASE_FILE_MANIFEST.csv"
VALIDATION_NAME = "09b_RELEASE_VALIDATION.json"
REPLACED_NAMES = {
    OLD_PDF,
    OLD_TEX,
    OLD_SOURCE_ZIP,
    README_NAME,
    MANIFEST_NAME,
    VALIDATION_NAME,
}

NEW_PDF = (
    "00c_SGA3_English_CurrentProgress_Cumulative_"
    "Through_XIII_XII_Gap_20260728.pdf"
)
NEW_TEX = (
    "02c_SGA3_English_CurrentProgress_Cumulative_"
    "Through_XIII_XII_Gap_20260728.tex"
)
HISTORY_ZIP = (
    "10c_SGA3_Previous_Public_Component_Readers_and_"
    "Source_Archives_Through_XI_20260728.zip"
)
NEW_SOURCE_ZIP = (
    "10c8_SGA3_CurrentProgress_Integration_Source_"
    "Through_XIII_XII_Gap_20260728.zip"
)

EXPECTED_PREDECESSOR_FILES = 63
EXPECTED_FINAL_FILES = 63
EXPECTED_RETAINED_PREDECESSOR_FILES = 57
EXPECTED_UNRELATED_RETAINED_FILES = 56
EXPECTED_MANIFEST_ROWS = 61
EXPECTED_ZIP_ARCHIVES = 44
EXPECTED_ZIP_FILE_MEMBERS = 4_012
EXPECTED_ZIP_DIRECTORY_ENTRIES = 6
EXPECTED_ZIP_ALL_ENTRIES = 4_018
EXPECTED_ZIP_UNCOMPRESSED_BYTES = 387_990_088
EXPECTED_CURRENT_SOURCE_MEMBERS = 939
EXPECTED_CURRENT_SOURCE_UNCOMPRESSED_BYTES = 16_036_916

REPO_ROOT = Path(__file__).resolve().parent.parent
RECEIPT_ROOT = REPO_ROOT / "manifests" / "published-zenodo"
PREDECESSOR_RECEIPT = (
    RECEIPT_ROOT
    / "20260728_sga3_cumulative_record_21632790_public_readback.json"
)
RELEASE_ROOT = Path(
    os.environ.get(
        "SGA3_CUMULATIVE_RELEASE_ROOT",
        Path.home()
        / "Documents"
        / "interlanguage"
        / "03_projects"
        / "language_management"
        / "english_germanic"
        / "03_working_translations"
        / "sga3_english_current_progress_cumulative_i_vi_viii_ix_xi_20260728_r1"
        / "release",
    )
)
CONTROLS_ROOT = Path(
    os.environ.get(
        "SGA3_CUMULATIVE_X_ZENODO_CONTROLS_ROOT",
        Path(os.environ["LOCALAPPDATA"])
        / "Temp"
        / "sga3_cumulative_with_x_zenodo_controls",
    )
)
READBACK_ROOT = Path(
    os.environ.get(
        "SGA3_CUMULATIVE_X_ZENODO_READBACK_ROOT",
        Path(os.environ["LOCALAPPDATA"])
        / "Temp"
        / "sga3_cumulative_with_x_zenodo_public_readback",
    )
)
TOKEN_LOG = Path(
    os.environ.get(
        "ZENODO_TOKEN_LOG",
        Path.home() / ".codex" / ".sandbox" / "sandbox.log",
    )
)
DRAFT_STATE = (
    RECEIPT_ROOT
    / "20260728_sga3_cumulative_with_x_zenodo_draft_state.json"
)

PRIMARY_LOCAL_PATHS = {
    NEW_PDF: RELEASE_ROOT / NEW_PDF,
    NEW_TEX: RELEASE_ROOT / NEW_TEX,
    NEW_SOURCE_ZIP: RELEASE_ROOT / NEW_SOURCE_ZIP,
}

NEW_MANIFEST_ROWS = {
    NEW_PDF: {
        "role": "english_reader",
        "provenance": (
            "current-progress cumulative SGA3 English reader including "
            "Expose X Loop1; GitHub commit " + GITHUB_COMMIT
        ),
        "status": (
            "preferred_current_progress_working_reader_sga3_incomplete_"
            "i_xi_except_xii_plus_xiii"
        ),
    },
    NEW_TEX: {
        "role": "english_master_tex",
        "provenance": (
            "direct editable integration master for the X-inclusive "
            "current-progress cumulative SGA3 reader; GitHub commit "
            + GITHUB_COMMIT
        ),
        "status": (
            "current_progress_working_source_sga3_incomplete_"
            "i_xi_except_xii_plus_xiii"
        ),
    },
    NEW_SOURCE_ZIP: {
        "role": "grouped_source_and_evidence",
        "provenance": (
            "939-member privacy-clean integration source closure for the "
            "X-inclusive current-progress cumulative reader; GitHub commit "
            + GITHUB_COMMIT
        ),
        "status": (
            "current_progress_integration_source_sga3_incomplete_"
            "i_xi_except_xii_plus_xiii"
        ),
    },
    README_NAME: {
        "role": "manifest_status",
        "provenance": (
            "current compact same-concept release note for the X-inclusive "
            "cumulative SGA3 reader; GitHub commit " + GITHUB_COMMIT
        ),
        "status": "current_release_control",
    },
}

DESCRIPTION_PARAGRAPHS = [
    (
        "This same-concept compact successor preserves the reader-first SGA "
        "surface from version 10.5281/zenodo.21632790. Fifty-six unrelated "
        "files and the SGA3 component-history ZIP are retained byte-identically. "
        "Only the preferred SGA3 reader, direct editable integration master, "
        "current integration-source ZIP, and three release controls are "
        "replaced."
    ),
    (
        "The preferred SGA3 current-progress reader has 877 A4 pages and "
        "contains the Editorial Notice, Introduction, Exposes I-XI except XII, "
        "and Expose XIII. It places an explicit gap leaf for Expose XII and "
        "ends before Expose XIV; Exposes XIV-XXVI are absent. It is therefore "
        "a substantial working reader, not a complete SGA3 translation, "
        "critical edition, rights clearance, or mathematical certification."
    ),
    (
        "Expose X is now included as a complete Loop-1 English text-and-equation "
        "body covering all 44 authority pages. Four raster diagram placeholders "
        "remain for Loop 2, so this inclusion is not a native-diagram or final "
        "release-certification claim. Expose VII uses the latest readable "
        "repaired r5 body with final detector/reference closeout unfinished. "
        "Expose XIII has source, formula, and high-zoom diagram review while "
        "exhaustive reference/package closeout remains unfinished."
    ),
    (
        "The reader has 5,525 named destinations, 3,748 valid internal GoTo "
        "actions, zero broken internal GoTo actions, 191 outlines, 62 embedded "
        "font resources, and no Type3 fonts. Four XeLaTeX passes converged "
        "without hard errors, undefined references, duplicate destinations, "
        "missing glyphs, or overfull boxes. An isolated rebuild matched all "
        "877 pages in content streams, text, geometry, destinations, actions, "
        "and fonts."
    ),
    (
        "The previous loose SGA3 public component objects remain preserved "
        "byte-for-byte inside the unchanged history ZIP. The current "
        "integration-source ZIP contains 939 exact file members and has passed "
        "CRC, identity, and privacy closure. SGA1 remains the default preview; "
        "numeric filenames keep English SGA1-SGA6 readers first, followed by "
        "French readers and primary editable TeX."
    ),
    (
        "The controlling French source images and PDFs are not redistributed "
        "by the integration archive. Pre-existing user-supplied OCR is a "
        "read-only locator or drafting witness and was not regenerated. Jacob "
        "C. Reinhold's jcreinhold/sga English lineage at revision "
        "e7a259f3f8608ad3edf9bf6eead3fd504dd2d23e is credited comparison and "
        "drafting material, not source authority; its author-declared CC BY "
        "4.0 applies only to that contribution. Rights in the underlying French "
        "works and scans remain with their holders. Machine-assisted "
        "contributors include OpenAI Codex / ChatGPT and Anthropic Claude "
        "under human direction."
    ),
]
DESCRIPTION_HTML = "\n".join(f"<p>{value}</p>" for value in DESCRIPTION_PARAGRAPHS)
NOTES_HTML = (
    "<p>Compact reader-first surface with 63 public files. English readers for "
    "SGA1 through SGA6 remain directly accessible, followed by French readers "
    "and primary editable TeX; recursive sources, QA, evidence, and predecessor "
    "objects are grouped into coherent ZIP archives. GitHub package commit: "
    f"{GITHUB_COMMIT}.</p>"
)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(4 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def md5_file(path: Path) -> str:
    digest = hashlib.md5(usedforsecurity=False)
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(4 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().lower()


def normalize_checksum(value: str) -> str:
    return value.lower().removeprefix("md5:")


def write_text(path: Path, value: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(value, encoding="utf-8", newline="\n")


def save_json(path: Path, value: object) -> None:
    write_text(
        path,
        json.dumps(value, ensure_ascii=True, indent=2) + "\n",
    )


def find_token() -> str:
    direct = os.environ.get("ZENODO_TOKEN")
    if direct:
        return direct
    data = TOKEN_LOG.read_text(encoding="utf-8", errors="ignore")
    candidates = sorted(
        set(re.findall(r"(?<![A-Za-z0-9])[A-Za-z0-9]{60}(?![A-Za-z0-9])", data))
    )
    if len(candidates) != 1:
        raise RuntimeError(
            "Expected exactly one locally retained Zenodo credential, found "
            f"{len(candidates)}"
        )
    return candidates[0]


def make_session() -> requests.Session:
    session = requests.Session()
    retry = Retry(
        total=8,
        connect=8,
        read=8,
        status=8,
        backoff_factor=1.5,
        status_forcelist=(429, 500, 502, 503, 504),
        allowed_methods=frozenset({"GET", "HEAD", "PUT"}),
        raise_on_status=False,
    )
    session.mount("https://", HTTPAdapter(max_retries=retry))
    session.headers.update(
        {"User-Agent": "modern-latex-manuscripts-archive/1.0"}
    )
    return session


def check(
    response: requests.Response, expected: set[int]
) -> requests.Response:
    if response.status_code not in expected:
        raise RuntimeError(
            f"Zenodo HTTP {response.status_code} for {response.request.method} "
            f"{response.url}: {response.text[:2000]}"
        )
    return response


def concept_doi(record: dict) -> str | None:
    return record.get("conceptdoi") or (
        record.get("parent", {})
        .get("pids", {})
        .get("doi", {})
        .get("identifier")
    )


def version_doi(record: dict) -> str | None:
    return record.get("doi") or (
        record.get("pids", {}).get("doi", {}).get("identifier")
    )


def entries_map(record: dict) -> dict[str, dict]:
    entries = record.get("files", {}).get("entries", {})
    if isinstance(entries, list):
        entries = {row["key"]: row for row in entries}
    if not isinstance(entries, dict):
        raise RuntimeError("Unexpected RDM file-entry shape")
    if len(entries) != len(set(entries)):
        raise RuntimeError("Duplicate RDM file keys")
    return entries


def legacy_file_map(deposition: dict) -> dict[str, dict]:
    result = {row["filename"]: row for row in deposition["files"]}
    if len(result) != len(deposition["files"]):
        raise RuntimeError("Draft contains duplicate legacy filenames")
    return result


def predecessor_receipt() -> dict:
    result = json.loads(PREDECESSOR_RECEIPT.read_text(encoding="utf-8-sig"))
    if (
        result.get("status") != "PASS"
        or int(result.get("record", -1)) != PREDECESSOR_RECORD
        or result.get("conceptdoi") != CONCEPT_DOI
        or len(result.get("files", {})) != EXPECTED_PREDECESSOR_FILES
    ):
        raise RuntimeError("Local predecessor readback receipt is not controlling")
    for name, row in result["files"].items():
        if not row.get("match"):
            raise RuntimeError(f"Predecessor receipt has a failed identity: {name}")
    return result


def public_predecessor(session: requests.Session) -> dict:
    record = check(
        session.get(
            f"{API}/records/{PREDECESSOR_RECORD}?expand=true",
            headers={"Accept": "application/vnd.inveniordm.v1+json"},
            timeout=(30, 180),
        ),
        {200},
    ).json()
    if (
        int(record["id"]) != PREDECESSOR_RECORD
        or concept_doi(record) != CONCEPT_DOI
        or version_doi(record) != PREDECESSOR_DOI
        or len(entries_map(record)) != EXPECTED_PREDECESSOR_FILES
    ):
        raise RuntimeError("Live predecessor identity or file boundary changed")
    return record


def assert_predecessor_is_latest(session: requests.Session) -> None:
    latest = check(
        session.get(
            f"{API}/records/{PREDECESSOR_RECORD}/versions/latest?expand=true",
            headers={"Accept": "application/vnd.inveniordm.v1+json"},
            timeout=(30, 180),
        ),
        {200},
    ).json()
    if (
        int(latest["id"]) != PREDECESSOR_RECORD
        or concept_doi(latest) != CONCEPT_DOI
    ):
        raise RuntimeError(
            "SGA concept head moved; refusing to create a parallel successor"
        )


def verify_predecessor_exact(
    record: dict, receipt: dict
) -> dict[str, dict]:
    entries = entries_map(record)
    if set(entries) != set(receipt["files"]):
        raise RuntimeError("Live predecessor set differs from exact readback receipt")
    result = {}
    for name, row in entries.items():
        wanted = receipt["files"][name]
        if int(row["size"]) != int(wanted["bytes"]):
            raise RuntimeError(f"Live predecessor size mismatch: {name}")
        result[name] = {
            "bytes": int(wanted["bytes"]),
            "sha256": wanted["sha256"].upper(),
            "md5": normalize_checksum(row["checksum"]),
        }
    return result


def verify_primary_local_files() -> dict[str, dict]:
    expected = {
        NEW_PDF: (
            5_378_609,
            "79A9C3908CDD2FF39F86DD52F92C6F002CCC943B20414E385167752C1DD8F174",
        ),
        NEW_TEX: (
            16_499,
            "D7ED3AC4E2FA6B3090EAE51D6F0ACF39426CE84ABBE956CFF620A9BF490E3CD5",
        ),
        NEW_SOURCE_ZIP: (
            11_941_332,
            "1E91E5E11A402FF13B134E9DDA0C7784D4060453DBD97E9455C05FCEC5358BD0",
        ),
    }
    result = {}
    for name, path in PRIMARY_LOCAL_PATHS.items():
        if not path.is_file():
            raise FileNotFoundError(path)
        identity = {
            "path": path,
            "bytes": path.stat().st_size,
            "sha256": sha256_file(path),
            "md5": md5_file(path),
        }
        if (identity["bytes"], identity["sha256"]) != expected[name]:
            raise RuntimeError(f"Primary local identity mismatch: {name}")
        result[name] = identity

    path = PRIMARY_LOCAL_PATHS[NEW_SOURCE_ZIP]
    members = 0
    directories = 0
    uncompressed = 0
    with zipfile.ZipFile(path, "r") as archive:
        if archive.testzip() is not None:
            raise RuntimeError("Current integration-source ZIP failed CRC")
        for info in archive.infolist():
            safe_zip_name(info.filename)
            if info.is_dir():
                directories += 1
            else:
                members += 1
                uncompressed += info.file_size
    if (
        members,
        directories,
        uncompressed,
    ) != (
        EXPECTED_CURRENT_SOURCE_MEMBERS,
        0,
        EXPECTED_CURRENT_SOURCE_UNCOMPRESSED_BYTES,
    ):
        raise RuntimeError(
            "Current integration-source ZIP boundary mismatch: "
            f"{(members, directories, uncompressed)}"
        )
    return result


def fetch_predecessor_manifest(
    session: requests.Session, predecessor: dict, receipt: dict
) -> list[dict[str, str]]:
    entry = entries_map(predecessor)[MANIFEST_NAME]
    response = check(
        session.get(entry["links"]["content"], timeout=(30, 180)),
        {200},
    )
    content = response.content
    wanted = receipt["files"][MANIFEST_NAME]
    if (
        len(content),
        hashlib.sha256(content).hexdigest().upper(),
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
    if len(rows) != EXPECTED_MANIFEST_ROWS:
        raise RuntimeError("Unexpected predecessor release-manifest row count")
    return rows


def create_or_resume_draft(
    session: requests.Session, token: str, predecessor: dict
) -> int:
    auth = {"Authorization": f"Bearer {token}"}
    vendor = {
        **auth,
        "Accept": "application/vnd.inveniordm.v1+json",
    }
    existing = session.get(
        f"{API}/records/{PREDECESSOR_RECORD}/draft",
        headers=vendor,
        timeout=(30, 180),
    )
    if existing.status_code == 200:
        if not DRAFT_STATE.is_file():
            raise RuntimeError(
                "An untracked successor draft already exists; refusing a "
                "second or blind mutation"
            )
        state = json.loads(DRAFT_STATE.read_text(encoding="utf-8"))
        draft = existing.json()
        draft_id = int(draft["id"])
        if (
            draft_id != int(state["draft_id"])
            or concept_doi(draft) != CONCEPT_DOI
            or int(state["predecessor_record"]) != PREDECESSOR_RECORD
        ):
            raise RuntimeError("Existing successor draft is not the tracked draft")
        return draft_id
    check(existing, {404})

    if DRAFT_STATE.is_file():
        state = json.loads(DRAFT_STATE.read_text(encoding="utf-8"))
        if state.get("published"):
            raise RuntimeError(
                "Tracked successor is already published; use readback recovery"
            )
        raise RuntimeError("Tracked draft state exists but Zenodo draft is absent")

    legacy = check(
        session.get(
            f"{API}/deposit/depositions/{PREDECESSOR_RECORD}",
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

    created = check(
        session.post(
            legacy["links"]["newversion"],
            headers=auth,
            timeout=(30, 300),
        ),
        {201},
    ).json()
    deposit = check(
        session.get(
            created["links"]["latest_draft"],
            headers=auth,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    draft_id = int(deposit["id"])
    if set(legacy_file_map(deposit)) != set(entries_map(predecessor)):
        raise RuntimeError("New-version draft did not inherit the predecessor set")
    save_json(
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


def readme_text(draft_id: int) -> str:
    return f"""# Current compact SGA release

This is a same-concept successor to Zenodo record {PREDECESSOR_RECORD}. It
preserves all unrelated SGA files and the existing SGA3 component-history ZIP
byte-for-byte. It replaces only the preferred SGA3 cumulative reader, its
direct editable integration master, its current source ZIP, and the three
release controls. The reserved successor record is {draft_id}.

## Preferred SGA3 reading surface

`{NEW_PDF}` is an 877-page current-progress English working reader containing:

- Editorial Notice and Introduction;
- Exposes I-XI except XII;
- Expose XIII;
- an explicit gap leaf for Expose XII; and
- a visible hard boundary before Expose XIV.

Exposes XIV-XXVI are absent. This is not complete SGA3, a critical edition,
rights clearance, or mathematical certification.

Expose X is now present as a complete Loop-1 English text-and-equation body.
All 44 authority pages were reviewed by its producing top-level session, but
four raster diagram placeholders remain for Loop 2. Expose VII uses the latest
readable repaired r5 body while final detector/reference closeout remains
unfinished. Expose XIII has source, formula, and high-zoom diagram review while
exhaustive reference/package closeout remains unfinished.

## Reader checks

- 877 A4 pages;
- 5,525 named destinations;
- 3,748 valid internal GoTo actions;
- zero broken internal GoTo actions;
- 191 outlines;
- 62 embedded font resources and zero Type3 fonts;
- four converged XeLaTeX passes;
- zero hard errors, undefined references, duplicate destinations, missing
  glyphs, or overfull boxes; and
- isolated rebuild equality for all 877 content streams, extracted text,
  geometry, destinations, link actions, and fonts.

The current source ZIP has 939 exact file members and passes CRC, identity, and
privacy closure. The unchanged SGA3 history ZIP keeps every formerly loose
component object available without crowding the reader-first surface.

## Authority and rights

Polo-Gille source PDFs control the French text, formulas, numbering, notes, and
diagram appearance. They are not redistributed in the integration archive.
Pre-existing user-supplied OCR was consulted read-only as locator and drafting
assistance only; it was not regenerated. Jacob C. Reinhold's
`jcreinhold/sga` English Markdown at commit
`e7a259f3f8608ad3edf9bf6eead3fd504dd2d23e` is credited comparison and
drafting lineage, not source authority. Its stated CC BY 4.0 applies only to
that contribution. No blanket license or transfer of rights in the underlying
French works, scans, comparison sources, or package as a whole is asserted.

Machine-assisted contributors include OpenAI Codex / ChatGPT and Anthropic
Claude under human direction. GitHub custody:
`https://github.com/KokunoYumeto/modern-latex-manuscripts/tree/{GITHUB_COMMIT}/{GITHUB_PACKAGE}`.
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

    write_text(CONTROLS_ROOT / README_NAME, readme_text(draft_id))
    readme_identity = {
        "path": CONTROLS_ROOT / README_NAME,
        "bytes": (CONTROLS_ROOT / README_NAME).stat().st_size,
        "sha256": sha256_file(CONTROLS_ROOT / README_NAME),
        "md5": md5_file(CONTROLS_ROOT / README_NAME),
    }

    retained_rows = []
    seen = set()
    for row in predecessor_rows:
        name = row["filename"]
        if name in {OLD_PDF, OLD_TEX, OLD_SOURCE_ZIP, README_NAME}:
            continue
        if name in REPLACED_NAMES:
            raise RuntimeError(f"Unexpected replaced control row: {name}")
        if name not in predecessor_identities:
            raise RuntimeError(f"Manifest row absent from predecessor receipt: {name}")
        identity = predecessor_identities[name]
        if (
            int(row["bytes"]),
            row["sha256"].upper(),
        ) != (
            identity["bytes"],
            identity["sha256"],
        ):
            raise RuntimeError(f"Retained manifest identity mismatch: {name}")
        retained_rows.append(dict(row))
        seen.add(name)

    new_local = dict(primary_local)
    new_local[README_NAME] = readme_identity
    for name in sorted(new_local, key=str.casefold):
        metadata = NEW_MANIFEST_ROWS[name]
        identity = new_local[name]
        retained_rows.append(
            {
                "filename": name,
                "bytes": str(identity["bytes"]),
                "sha256": identity["sha256"],
                "role": metadata["role"],
                "provenance": metadata["provenance"],
                "status": metadata["status"],
            }
        )
    retained_rows.sort(key=lambda row: row["filename"].casefold())
    if len(retained_rows) != EXPECTED_MANIFEST_ROWS:
        raise RuntimeError(
            f"Expected {EXPECTED_MANIFEST_ROWS} release rows, "
            f"got {len(retained_rows)}"
        )
    if len({row["filename"] for row in retained_rows}) != len(retained_rows):
        raise RuntimeError("Generated release manifest has duplicate filenames")

    manifest_path = CONTROLS_ROOT / MANIFEST_NAME
    with manifest_path.open(
        "w", encoding="utf-8", newline=""
    ) as handle:
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
        writer.writerows(retained_rows)
    manifest_identity = {
        "path": manifest_path,
        "bytes": manifest_path.stat().st_size,
        "sha256": sha256_file(manifest_path),
        "md5": md5_file(manifest_path),
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
        "retained_unrelated_files": EXPECTED_UNRELATED_RETAINED_FILES,
        "replaced_files": sorted(REPLACED_NAMES, key=str.casefold),
        "new_files": sorted(
            {
                NEW_PDF,
                NEW_TEX,
                NEW_SOURCE_ZIP,
                README_NAME,
                MANIFEST_NAME,
                VALIDATION_NAME,
            },
            key=str.casefold,
        ),
        "final_public_file_count": EXPECTED_FINAL_FILES,
        "release_manifest": {
            "rows": EXPECTED_MANIFEST_ROWS,
            "bytes": manifest_identity["bytes"],
            "sha256": manifest_identity["sha256"],
        },
        "default_preview": DEFAULT_PREVIEW,
        "github": {
            "commit": GITHUB_COMMIT,
            "path": GITHUB_PACKAGE,
            "anonymous_readback_files": 9,
            "status": "PASS",
        },
        "sga3_reader": {
            "scope": (
                "Editorial Notice, Introduction, Exposes I-XI except XII, "
                "and Expose XIII"
            ),
            "explicit_gap": "Expose XII",
            "absent_after_boundary": "Exposes XIV-XXVI",
            "pages": 877,
            "bytes": primary_local[NEW_PDF]["bytes"],
            "sha256": primary_local[NEW_PDF]["sha256"],
            "named_destinations": 5_525,
            "valid_internal_goto": 3_748,
            "broken_internal_goto": 0,
            "outlines": 191,
            "embedded_font_resources": 62,
            "type3_fonts": 0,
            "build_passes": 4,
            "isolated_rebuild_content_text_geometry_links_fonts_exact": True,
        },
        "expose_x": {
            "scope": "authority-local pages 1-44 / combined pages 679-722",
            "status": "complete_loop1_text_and_equations",
            "loop2_raster_diagram_placeholders": 4,
            "release_certified": False,
        },
        "current_source_zip": {
            "filename": NEW_SOURCE_ZIP,
            "members": EXPECTED_CURRENT_SOURCE_MEMBERS,
            "uncompressed_bytes": EXPECTED_CURRENT_SOURCE_UNCOMPRESSED_BYTES,
            "sha256": primary_local[NEW_SOURCE_ZIP]["sha256"],
            "privacy_hits": 0,
        },
        "history_zip": {
            "filename": HISTORY_ZIP,
            "bytes": predecessor_identities[HISTORY_ZIP]["bytes"],
            "sha256": predecessor_identities[HISTORY_ZIP]["sha256"],
            "retained_byte_identically": True,
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
    save_json(validation_path, validation)
    validation_identity = {
        "path": validation_path,
        "bytes": validation_path.stat().st_size,
        "sha256": sha256_file(validation_path),
        "md5": md5_file(validation_path),
    }
    result = dict(new_local)
    result[MANIFEST_NAME] = manifest_identity
    result[VALIDATION_NAME] = validation_identity
    return result


def final_expected_identities(
    predecessor_identities: dict[str, dict],
    local_files: dict[str, dict],
) -> dict[str, dict]:
    retained = {
        name: dict(identity)
        for name, identity in predecessor_identities.items()
        if name not in REPLACED_NAMES
    }
    if len(retained) != EXPECTED_RETAINED_PREDECESSOR_FILES:
        raise RuntimeError("Retained predecessor boundary mismatch")
    overlap = set(retained) & set(local_files)
    if overlap:
        raise RuntimeError(f"New local filenames collide with retained files: {overlap}")
    expected = {**retained, **local_files}
    if len(expected) != EXPECTED_FINAL_FILES:
        raise RuntimeError("Final expected file boundary mismatch")
    return expected


def stage_draft(
    session: requests.Session,
    token: str,
    draft_id: int,
    expected: dict[str, dict],
    local_files: dict[str, dict],
) -> dict:
    auth = {"Authorization": f"Bearer {token}"}
    deposition = check(
        session.get(
            f"{API}/deposit/depositions/{draft_id}",
            headers=auth,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    if deposition.get("state") != "unsubmitted" or deposition.get("submitted"):
        raise RuntimeError("Tracked successor is not an unpublished draft")
    files = legacy_file_map(deposition)
    extras = set(files) - set(expected) - REPLACED_NAMES
    if extras:
        raise RuntimeError(f"Unexpected draft files: {sorted(extras)}")

    actions = []
    for name in sorted(REPLACED_NAMES, key=str.casefold):
        row = files.get(name)
        if row is None:
            actions.append({"filename": name, "action": "already_absent"})
            continue
        check(
            session.delete(
                row["links"]["self"],
                headers=auth,
                timeout=(30, 300),
            ),
            {204},
        )
        actions.append({"filename": name, "action": "deleted_stale"})

    deposition = check(
        session.get(
            f"{API}/deposit/depositions/{draft_id}",
            headers=auth,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    files = legacy_file_map(deposition)
    bucket = deposition["links"]["bucket"].rstrip("/")
    for name in sorted(local_files, key=str.casefold):
        identity = local_files[name]
        existing = files.get(name)
        if existing is not None:
            observed = (
                int(existing["filesize"]),
                normalize_checksum(existing["checksum"]),
            )
            wanted = (identity["bytes"], identity["md5"])
            if observed == wanted:
                actions.append({"filename": name, "action": "already_exact"})
                continue
            check(
                session.delete(
                    existing["links"]["self"],
                    headers=auth,
                    timeout=(30, 300),
                ),
                {204},
            )
            actions.append({"filename": name, "action": "deleted_stale_local"})

        with identity["path"].open("rb") as handle:
            uploaded = check(
                session.put(
                    f"{bucket}/{quote(name, safe='')}",
                    headers={
                        **auth,
                        "Content-Type": "application/octet-stream",
                    },
                    data=handle,
                    timeout=(30, 1800),
                ),
                {200, 201},
            ).json()
        observed = (
            int(uploaded.get("size", uploaded.get("filesize", -1))),
            normalize_checksum(uploaded.get("checksum", "")),
        )
        if observed != (identity["bytes"], identity["md5"]):
            raise RuntimeError(f"Upload response identity mismatch: {name}")
        actions.append({"filename": name, "action": "uploaded_exact"})
        deposition = check(
            session.get(
                f"{API}/deposit/depositions/{draft_id}",
                headers=auth,
                timeout=(30, 180),
            ),
            {200},
        ).json()
        files = legacy_file_map(deposition)

    final = check(
        session.get(
            f"{API}/deposit/depositions/{draft_id}",
            headers=auth,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    final_files = legacy_file_map(final)
    if set(final_files) != set(expected):
        raise RuntimeError("Staged draft does not have the exact final set")
    for name, identity in expected.items():
        row = final_files[name]
        observed = (
            int(row["filesize"]),
            normalize_checksum(row["checksum"]),
        )
        if observed != (identity["bytes"], identity["md5"]):
            raise RuntimeError(f"Staged draft identity mismatch: {name}")

    receipt = {
        "status": "PASS_STAGED",
        "errors": [],
        "predecessor_record": PREDECESSOR_RECORD,
        "draft_id": draft_id,
        "concept_doi": CONCEPT_DOI,
        "file_count": len(final_files),
        "bytes": sum(int(row["filesize"]) for row in final_files.values()),
        "retained_predecessor_files": EXPECTED_RETAINED_PREDECESSOR_FILES,
        "retained_unrelated_files": EXPECTED_UNRELATED_RETAINED_FILES,
        "local_upload_files": len(local_files),
        "actions": actions,
        "duplicate_concept_created": False,
        "second_draft_created": False,
    }
    save_json(
        RECEIPT_ROOT
        / f"20260728_sga3_cumulative_with_x_record_{draft_id}_draft_files.json",
        receipt,
    )
    return receipt


def patch_notes(metadata: dict) -> None:
    additional = [
        row
        for row in metadata.get("additional_descriptions", [])
        if row.get("type", {}).get("id") != "notes"
    ]
    additional.append(
        {
            "description": NOTES_HTML,
            "type": {"id": "notes", "title": {"en": "Notes"}},
        }
    )
    metadata["additional_descriptions"] = additional


def assert_metadata(metadata: dict) -> None:
    if metadata.get("version") != VERSION:
        raise RuntimeError("Version metadata mismatch")
    if metadata.get("publication_date") != PUBLICATION_DATE:
        raise RuntimeError("Publication-date metadata mismatch")
    if metadata.get("description") != DESCRIPTION_HTML:
        raise RuntimeError("Description metadata mismatch")
    if not any(
        row.get("description") == NOTES_HTML
        for row in metadata.get("additional_descriptions", [])
    ):
        raise RuntimeError("Release-notes metadata mismatch")


def modern_draft(
    session: requests.Session, token: str, draft_id: int
) -> dict:
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.inveniordm.v1+json",
    }
    draft = check(
        session.get(
            f"{API}/records/{draft_id}/draft",
            headers=headers,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    if int(draft["id"]) != draft_id or concept_doi(draft) != CONCEPT_DOI:
        raise RuntimeError("Draft escaped the existing SGA concept")
    files = check(
        session.get(draft["links"]["files"], headers=headers, timeout=(30, 180)),
        {200},
    ).json()
    entries = files.get("entries", {})
    if isinstance(entries, list):
        entries = {row["key"]: row for row in entries}
    files["entries"] = entries
    draft["files"] = files
    return draft


def publish_draft(
    session: requests.Session,
    token: str,
    draft_id: int,
    expected: dict[str, dict],
) -> dict:
    draft = modern_draft(session, token, draft_id)
    if set(draft["files"]["entries"]) != set(expected):
        raise RuntimeError("Cannot publish: modern draft set mismatch")

    metadata = copy.deepcopy(draft["metadata"])
    metadata["version"] = VERSION
    metadata["publication_date"] = PUBLICATION_DATE
    metadata["description"] = DESCRIPTION_HTML
    patch_notes(metadata)
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
    patched = check(
        session.put(
            f"{API}/records/{draft_id}/draft",
            headers=headers,
            json=payload,
            timeout=(30, 300),
        ),
        {200},
    ).json()
    assert_metadata(patched["metadata"])
    reread = modern_draft(session, token, draft_id)
    assert_metadata(reread["metadata"])
    if reread["files"].get("default_preview") != DEFAULT_PREVIEW:
        raise RuntimeError("Draft default preview mismatch")
    if set(reread["files"]["entries"]) != set(expected):
        raise RuntimeError("Draft lost exact file set after metadata patch")

    published = check(
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
    if int(published["id"]) != draft_id or concept_doi(published) != CONCEPT_DOI:
        raise RuntimeError("Published response escaped the existing SGA concept")
    doi = version_doi(published)
    state = json.loads(DRAFT_STATE.read_text(encoding="utf-8"))
    state.update({"published": True, "doi": doi})
    save_json(DRAFT_STATE, state)
    receipt = {
        "status": "PUBLISH_ACCEPTED",
        "errors": [],
        "record_id": draft_id,
        "doi": doi,
        "concept_doi": CONCEPT_DOI,
        "file_count": EXPECTED_FINAL_FILES,
        "default_preview": DEFAULT_PREVIEW,
        "duplicate_concept_created": False,
        "second_draft_created": False,
    }
    save_json(
        RECEIPT_ROOT
        / f"20260728_sga3_cumulative_with_x_record_{draft_id}_publish_response.json",
        receipt,
    )
    return receipt


def wait_for_public(
    session: requests.Session, record_id: int
) -> dict:
    for _ in range(120):
        response = session.get(
            f"{API}/records/{record_id}?expand=true",
            headers={"Accept": "application/vnd.inveniordm.v1+json"},
            timeout=(30, 180),
        )
        if response.status_code == 200:
            record = response.json()
            if len(entries_map(record)) == EXPECTED_FINAL_FILES:
                return record
        time.sleep(5)
    raise RuntimeError("Published successor did not stabilize")


def safe_zip_name(name: str) -> None:
    pure = PurePosixPath(name)
    if pure.is_absolute() or ".." in pure.parts or "\\" in name:
        raise RuntimeError(f"Unsafe ZIP member path: {name}")


def anonymous_readback(
    record_id: int,
    expected: dict[str, dict],
) -> tuple[dict, dict]:
    public = make_session()
    record = wait_for_public(public, record_id)
    if int(record["id"]) != record_id or concept_doi(record) != CONCEPT_DOI:
        raise RuntimeError("Public successor lineage mismatch")
    doi = version_doi(record)
    assert_metadata(record["metadata"])
    if record["files"].get("default_preview") != DEFAULT_PREVIEW:
        raise RuntimeError("Published default preview mismatch")
    entries = entries_map(record)
    if set(entries) != set(expected):
        raise RuntimeError("Published outer-file set mismatch")

    latest = check(
        public.get(
            f"{API}/records/{PREDECESSOR_RECORD}/versions/latest?expand=true",
            headers={"Accept": "application/vnd.inveniordm.v1+json"},
            timeout=(30, 180),
        ),
        {200},
    ).json()
    if int(latest["id"]) != record_id or concept_doi(latest) != CONCEPT_DOI:
        raise RuntimeError("Published successor is not the sole live concept head")

    if READBACK_ROOT.exists():
        resolved = READBACK_ROOT.resolve()
        temp_root = Path(os.environ["LOCALAPPDATA"]).resolve() / "Temp"
        if temp_root not in resolved.parents:
            raise RuntimeError("Refusing to replace readback outside local temp")
        shutil.rmtree(READBACK_ROOT)
    READBACK_ROOT.mkdir(parents=True)

    file_receipt = {}
    for index, name in enumerate(sorted(expected, key=str.casefold), start=1):
        print(f"READBACK {index}/{len(expected)} {name}", flush=True)
        entry = entries[name]
        target = READBACK_ROOT / name
        with public.get(
            entry["links"]["content"],
            stream=True,
            timeout=(30, 1800),
        ) as response:
            check(response, {200})
            with target.open("wb") as handle:
                for block in response.iter_content(4 * 1024 * 1024):
                    if block:
                        handle.write(block)
        actual = {
            "bytes": target.stat().st_size,
            "sha256": sha256_file(target),
            "url": entry["links"]["content"],
        }
        wanted = expected[name]
        actual["match"] = (
            actual["bytes"],
            actual["sha256"],
        ) == (
            wanted["bytes"],
            wanted["sha256"],
        )
        if not actual["match"]:
            raise RuntimeError(f"Anonymous public readback mismatch: {name}")
        file_receipt[name] = actual

    zip_archives = []
    zip_members = []
    total_files = 0
    total_directories = 0
    total_entries = 0
    total_uncompressed = 0
    for name in sorted(file_receipt, key=str.casefold):
        if not name.lower().endswith(".zip"):
            continue
        path = READBACK_ROOT / name
        member_identity = hashlib.sha256()
        file_count = 0
        directory_count = 0
        uncompressed = 0
        with zipfile.ZipFile(path, "r") as archive:
            if archive.testzip() is not None:
                raise RuntimeError(f"Public ZIP CRC failure: {name}")
            for info in archive.infolist():
                safe_zip_name(info.filename)
                if info.is_dir():
                    directory_count += 1
                    continue
                digest = hashlib.sha256()
                with archive.open(info, "r") as source:
                    for block in iter(
                        lambda: source.read(4 * 1024 * 1024), b""
                    ):
                        digest.update(block)
                sha = digest.hexdigest().upper()
                member_identity.update(
                    (
                        f"{info.filename}\t{info.file_size}\t{sha}\n"
                    ).encode("utf-8")
                )
                zip_members.append(
                    {
                        "archive": name,
                        "relative_path": info.filename,
                        "bytes": info.file_size,
                        "sha256": sha,
                    }
                )
                file_count += 1
                uncompressed += info.file_size
        all_entries = file_count + directory_count
        zip_archives.append(
            {
                "filename": name,
                "bytes": path.stat().st_size,
                "sha256": sha256_file(path),
                "member_count": file_count,
                "directory_entry_count": directory_count,
                "all_entry_count": all_entries,
                "uncompressed_bytes": uncompressed,
                "canonical_member_identity_sha256": (
                    member_identity.hexdigest().upper()
                ),
                "errors": [],
            }
        )
        total_files += file_count
        total_directories += directory_count
        total_entries += all_entries
        total_uncompressed += uncompressed

    observed_zip = (
        len(zip_archives),
        total_files,
        total_directories,
        total_entries,
        total_uncompressed,
    )
    expected_zip = (
        EXPECTED_ZIP_ARCHIVES,
        EXPECTED_ZIP_FILE_MEMBERS,
        EXPECTED_ZIP_DIRECTORY_ENTRIES,
        EXPECTED_ZIP_ALL_ENTRIES,
        EXPECTED_ZIP_UNCOMPRESSED_BYTES,
    )
    if observed_zip != expected_zip:
        raise RuntimeError(
            f"ZIP aggregate mismatch: observed={observed_zip}, "
            f"expected={expected_zip}"
        )

    public_receipt = {
        "status": "PASS",
        "errors": [],
        "record": record_id,
        "doi": doi,
        "conceptdoi": CONCEPT_DOI,
        "record_url": f"https://zenodo.org/records/{record_id}",
        "version": VERSION,
        "file_count": len(file_receipt),
        "bytes": sum(row["bytes"] for row in file_receipt.values()),
        "files": file_receipt,
        "latest_record": int(latest["id"]),
        "rdm_default_preview": record["files"].get("default_preview"),
        "github_commit": GITHUB_COMMIT,
        "github_package": GITHUB_PACKAGE,
        "retained_predecessor_files": EXPECTED_RETAINED_PREDECESSOR_FILES,
        "retained_unrelated_files": EXPECTED_UNRELATED_RETAINED_FILES,
        "duplicate_concept_created": False,
        "second_draft_created": False,
    }
    zip_receipt = {
        "status": "PASS",
        "errors": [],
        "record_id": record_id,
        "doi": doi,
        "zip_archive_count": len(zip_archives),
        "zip_file_member_count": total_files,
        "zip_directory_entry_count": total_directories,
        "zip_all_entry_count": total_entries,
        "zip_uncompressed_bytes": total_uncompressed,
        "archives": zip_archives,
        "members": zip_members,
    }
    save_json(
        RECEIPT_ROOT
        / f"20260728_sga3_cumulative_with_x_record_{record_id}_public_readback.json",
        public_receipt,
    )
    save_json(
        RECEIPT_ROOT
        / f"20260728_sga3_cumulative_with_x_record_{record_id}_zip_member_readback.json",
        zip_receipt,
    )
    shutil.rmtree(READBACK_ROOT)
    return public_receipt, zip_receipt


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--readback-only",
        action="store_true",
        help="Resume anonymous verification of the tracked published successor.",
    )
    args = parser.parse_args()

    if args.readback_only:
        if not DRAFT_STATE.is_file():
            raise RuntimeError("No tracked successor state is available")
        state = json.loads(DRAFT_STATE.read_text(encoding="utf-8"))
        if not state.get("published"):
            raise RuntimeError("Tracked successor has not been published")
        record_id = int(state["draft_id"])
        session = make_session()
        receipt = predecessor_receipt()
        predecessor = public_predecessor(session)
        predecessor_identities = verify_predecessor_exact(
            predecessor, receipt
        )
        primary_local = verify_primary_local_files()
        predecessor_rows = fetch_predecessor_manifest(
            session, predecessor, receipt
        )
        local_files = generate_controls(
            record_id,
            predecessor_rows,
            predecessor_identities,
            primary_local,
        )
        expected = final_expected_identities(
            predecessor_identities,
            local_files,
        )
        public, zipped = anonymous_readback(record_id, expected)
        print(
            json.dumps(
                {
                    "status": public["status"],
                    "record": public["record"],
                    "doi": public["doi"],
                    "file_count": public["file_count"],
                    "bytes": public["bytes"],
                    "zip_archives": zipped["zip_archive_count"],
                    "zip_file_members": zipped["zip_file_member_count"],
                    "zip_directory_entries": (
                        zipped["zip_directory_entry_count"]
                    ),
                    "zip_uncompressed_bytes": (
                        zipped["zip_uncompressed_bytes"]
                    ),
                },
                indent=2,
            ),
            flush=True,
        )
        return

    token = find_token()
    session = make_session()
    receipt = predecessor_receipt()
    assert_predecessor_is_latest(session)
    predecessor = public_predecessor(session)
    predecessor_identities = verify_predecessor_exact(predecessor, receipt)
    primary_local = verify_primary_local_files()
    predecessor_rows = fetch_predecessor_manifest(
        session, predecessor, receipt
    )

    draft_id = create_or_resume_draft(
        session, token, predecessor
    )
    local_files = generate_controls(
        draft_id,
        predecessor_rows,
        predecessor_identities,
        primary_local,
    )
    expected = final_expected_identities(
        predecessor_identities,
        local_files,
    )
    stage = stage_draft(
        session,
        token,
        draft_id,
        expected,
        local_files,
    )
    published = publish_draft(
        session,
        token,
        draft_id,
        expected,
    )
    public, zipped = anonymous_readback(draft_id, expected)
    print(
        json.dumps(
            {
                "stage": stage,
                "publish": published,
                "readback": {
                    "status": public["status"],
                    "record": public["record"],
                    "doi": public["doi"],
                    "file_count": public["file_count"],
                    "bytes": public["bytes"],
                    "zip_archives": zipped["zip_archive_count"],
                    "zip_file_members": zipped["zip_file_member_count"],
                    "zip_directory_entries": (
                        zipped["zip_directory_entry_count"]
                    ),
                    "zip_uncompressed_bytes": (
                        zipped["zip_uncompressed_bytes"]
                    ),
                },
            },
            indent=2,
        ),
        flush=True,
    )


if __name__ == "__main__":
    main()
