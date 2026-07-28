#!/usr/bin/env python3
"""Publish and read back one same-concept EGA source-first successor."""

from __future__ import annotations

import argparse
import copy
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
CONCEPT_DOI = "10.5281/zenodo.20414353"
PREDECESSOR_RECORD = 20_454_552
PREDECESSOR_DOI = "10.5281/zenodo.20454552"
PUBLICATION_DATE = "2026-07-28"
VERSION = "2026-07-28 EGA 0 section 11 source-first working successor"
TITLE = (
    "Elements de geometrie algebrique (EGA): French Originals, "
    "English Working Readers, and Source Archives"
)

GITHUB_COMMIT = "e0ee2228cbce038758fe7f64d480bca21e9d6c55"
GITHUB_PACKAGE = (
    "sources/ega/checkpoints/"
    "ega0-iii-source-first-through-11-10-working-20260728"
)

REPO_ROOT = Path(__file__).resolve().parent.parent
PACKAGE_ROOT = REPO_ROOT / GITHUB_PACKAGE
RECEIPT_ROOT = REPO_ROOT / "manifests" / "published-zenodo"

NEW_PDF = (
    "00a_EGA0_English_Working_Reader_"
    "SourceFirst_11_5_1_to_11_10_3_20260728.pdf"
)
NEW_TEX = (
    "02a_EGA0_III_Section11_English_"
    "SourceFirst_11_5_1_to_11_10_3_20260728.tex"
)
NEW_ZIP = (
    "10a_EGA0_English_Working_Source_"
    "with_Section11_SourceFirst_20260728.zip"
)
NEW_NOTE = "90a_EGA0_III_SourceFirst_11_5_1_to_11_10_3_Status_20260728.md"
NEW_VALIDATION = (
    "91a_EGA0_III_SourceFirst_11_5_1_to_11_10_3_Validation_20260728.json"
)
DEFAULT_PREVIEW = NEW_PDF

STATIC_LOCAL_PATHS = {
    NEW_PDF: PACKAGE_ROOT / NEW_PDF,
    NEW_TEX: PACKAGE_ROOT / NEW_TEX,
    NEW_ZIP: PACKAGE_ROOT / NEW_ZIP,
}
STATIC_EXPECTED = {
    NEW_PDF: (
        991_284,
        "DD5D2923561FD15302630869828AC549FCC370E84524F29E88A6BAEBA074D0BD",
    ),
    NEW_TEX: (
        107_199,
        "1311E0EECB318C6F3D5525D9846874B42151B8B49903E89E99BC89F4E56B54E7",
    ),
    NEW_ZIP: (
        1_324_599,
        "C8E2CA96398CC0D7989A84F36FFCFB039ACAF00E1FB611C7A96DB6185560C76A",
    ),
}

EXPECTED_PREDECESSOR_FILES = 16
EXPECTED_FINAL_FILES = 21
EXPECTED_RETAINED_FILES = 16
EXPECTED_NEW_ZIP_MEMBERS = 96
EXPECTED_NEW_ZIP_MANIFEST_ROWS = 95
EXPECTED_NEW_ZIP_UNCOMPRESSED_BYTES = 5_633_220
EXPECTED_NEW_ZIP_MANIFEST_SHA256 = (
    "5D9BD9ED2EC85BF6853E4FED4A3663FD5A5BFE3D96E0E4617FD9EEB3D9561BAB"
)

OLD_ENGLISH_PDF = "00 EGA - English Translation Working Draft.pdf"
OLD_EGA_IV_PDF = (
    "01 EGA IV - English Translation Working Draft (Sections 1-21).pdf"
)

TOKEN_LOG = Path(
    os.environ.get(
        "ZENODO_TOKEN_LOG",
        Path.home() / ".codex" / ".sandbox" / "sandbox.log",
    )
)
TEMP_ROOT = Path(os.environ["LOCALAPPDATA"]) / "Temp"
CONTROLS_ROOT = TEMP_ROOT / "ega0_iii_11_10_zenodo_controls"
READBACK_ROOT = TEMP_ROOT / "ega0_iii_11_10_zenodo_readback"
DRAFT_STATE = (
    RECEIPT_ROOT
    / "20260728_ega0_iii_section11_source_first_zenodo_draft_state.json"
)
PREDECESSOR_RECEIPT = (
    RECEIPT_ROOT
    / "20260728_ega_record_20454552_predecessor_public_readback.json"
)
PREDECESSOR_PARTIAL = (
    RECEIPT_ROOT
    / "20260728_ega_record_20454552_predecessor_public_readback.partial.json"
)

DESCRIPTION_PARAGRAPHS = [
    (
        "This same-concept successor retains all 16 files from version "
        "10.5281/zenodo.20454552 byte-for-byte and adds a compact EGA 0 "
        "source-first working checkpoint: one direct reader, one direct "
        "editable section-11 TeX file, one grouped source ZIP, and two concise "
        "release controls."
    ),
    (
        "The new 93-page US-letter reader is a cumulative EGA 0 working "
        "container covering sections 1.0 through 14.3.6. The source-first "
        "successor verified in this release is strictly sections 11.5.1 "
        "through Corollary 11.10.3, corresponding to EGA III Part 1 authority "
        "PDF pages 32-46 and printed pages 35-49. Surrounding sections are "
        "retained inherited English context and are not newly source-certified "
        "by this checkpoint."
    ),
    (
        "The reader has 288 named destinations and 637 valid internal GoTo "
        "links. An isolated six-pass pdfLaTeX plus BibTeX rebuild matched all "
        "93 extracted-text pages, page geometry, destination count, and link "
        "summary. Six inherited cross-volume or earlier-range references remain "
        "unresolved and are explicitly listed in the public build summary."
    ),
    (
        "The controlling authority is EGA III Part 1, NUMDAM PMIHES 11 "
        "(1961), already retained on this concept, SHA-256 "
        "3ED59FE81DA07F1AB685DDC54A93128A364419D4DDAFBC7AFFCD8ABC8B401605. "
        "The new source ZIP does not duplicate that authority PDF. Existing "
        "user-supplied OCR and comparison translations were consulted read-only "
        "as locator or drafting witnesses; no OCR was generated or rerun."
    ),
    (
        "This is a machine-assisted scholarly working translation checkpoint, "
        "not completion of EGA 0, EGA III, or EGA as a whole; not a critical "
        "edition, source certification of the inherited surrounding text, "
        "peer review, rights determination, exhaustive-reference certification, "
        "or tagged-PDF accessibility remediation. No new license grant or "
        "transfer of underlying rights is asserted."
    ),
]
DESCRIPTION_HTML = "\n".join(
    f"<p>{paragraph}</p>" for paragraph in DESCRIPTION_PARAGRAPHS
)
NOTES_HTML = (
    "<p>The preferred preview is the new EGA 0 working reader. Its source-first "
    "verification is bounded to sections 11.5.1-11.10.3; the 93-page reader "
    "retains inherited surrounding sections 1.0-11.5 and 12.1-14.3.6 as useful "
    "working context. GitHub custody commit: "
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
    path.write_text(value.rstrip() + "\n", encoding="utf-8", newline="\n")


def save_json(path: Path, value: object) -> None:
    write_text(path, json.dumps(value, ensure_ascii=True, indent=2))


def find_token() -> str:
    direct = os.environ.get("ZENODO_TOKEN")
    if direct:
        return direct
    data = TOKEN_LOG.read_text(encoding="utf-8", errors="ignore")
    candidates = sorted(
        set(
            re.findall(
                r"(?<![A-Za-z0-9])[A-Za-z0-9]{60}(?![A-Za-z0-9])",
                data,
            )
        )
    )
    if len(candidates) != 1:
        raise RuntimeError(
            "Expected one locally retained Zenodo credential, found "
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
        {
            "User-Agent": "modern-latex-manuscripts-archive/1.0",
            "Connection": "close",
        }
    )
    return session


def check(
    response: requests.Response, expected: set[int]
) -> requests.Response:
    if response.status_code not in expected:
        raise RuntimeError(
            f"Zenodo HTTP {response.status_code} for "
            f"{response.request.method} {response.url}: "
            f"{response.text[:2000]}"
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
        raise RuntimeError("Duplicate legacy deposition filenames")
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
        raise RuntimeError("Live EGA predecessor identity changed")
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
            "EGA concept head moved; refusing a parallel successor"
        )


def clean_temp(path: Path) -> None:
    if not path.exists():
        return
    resolved = path.resolve()
    allowed = TEMP_ROOT.resolve()
    if allowed not in resolved.parents:
        raise RuntimeError(f"Refusing cleanup outside {allowed}")
    shutil.rmtree(path)


def safe_zip_name(name: str) -> None:
    pure = PurePosixPath(name)
    if (
        pure.is_absolute()
        or ".." in pure.parts
        or "\\" in name
        or (len(name) >= 2 and name[1] == ":")
    ):
        raise RuntimeError(f"Unsafe ZIP member path: {name}")


def inspect_zip(path: Path, *, include_members: bool) -> dict:
    member_rows = []
    identity = hashlib.sha256()
    with zipfile.ZipFile(path) as archive:
        crc_error = archive.testzip()
        if crc_error is not None:
            raise RuntimeError(f"ZIP CRC failure in {path.name}: {crc_error}")
        infos = archive.infolist()
        names = [info.filename for info in infos]
        if len(names) != len(set(names)):
            raise RuntimeError(f"Duplicate ZIP paths in {path.name}")
        file_infos = sorted(
            (info for info in infos if not info.is_dir()),
            key=lambda info: info.filename,
        )
        directory_count = sum(info.is_dir() for info in infos)
        for info in infos:
            safe_zip_name(info.filename)
        for info in file_infos:
            digest = hashlib.sha256()
            with archive.open(info) as source:
                for block in iter(
                    lambda: source.read(4 * 1024 * 1024), b""
                ):
                    digest.update(block)
            sha = digest.hexdigest().upper()
            identity.update(
                f"{info.filename}\t{info.file_size}\t{sha}\n".encode("utf-8")
            )
            if include_members:
                member_rows.append(
                    {
                        "relative_path": info.filename,
                        "bytes": info.file_size,
                        "sha256": sha,
                    }
                )
        result = {
            "file_members": len(file_infos),
            "directory_entries": directory_count,
            "all_entries": len(infos),
            "uncompressed_bytes": sum(
                info.file_size for info in file_infos
            ),
            "canonical_member_identity_sha256": (
                identity.hexdigest().upper()
            ),
            "crc_error": None,
            "safe_paths": True,
        }
        if include_members:
            result["members"] = member_rows
        if "SOURCE_BUNDLE_SHA256.csv" in names:
            manifest_bytes = archive.read("SOURCE_BUNDLE_SHA256.csv")
            rows = list(
                csv.DictReader(
                    io.StringIO(manifest_bytes.decode("utf-8-sig"))
                )
            )
            errors = []
            for row in rows:
                data = archive.read(row["relative_path"])
                if (
                    len(data) != int(row["bytes"])
                    or hashlib.sha256(data).hexdigest().upper()
                    != row["sha256"].upper()
                ):
                    errors.append(row["relative_path"])
            result["internal_manifest"] = {
                "rows": len(rows),
                "bytes": len(manifest_bytes),
                "sha256": hashlib.sha256(
                    manifest_bytes
                ).hexdigest().upper(),
                "errors": errors,
            }
    return result


def download_file(
    session: requests.Session, url: str, destination: Path
) -> tuple[int, str, str]:
    destination.parent.mkdir(parents=True, exist_ok=True)
    sha = hashlib.sha256()
    md5 = hashlib.md5(usedforsecurity=False)
    size = 0
    with session.get(url, stream=True, timeout=(30, 90)) as response:
        check(response, {200})
        with destination.open("wb") as handle:
            for block in response.iter_content(4 * 1024 * 1024):
                if not block:
                    continue
                handle.write(block)
                sha.update(block)
                md5.update(block)
                size += len(block)
    return size, sha.hexdigest().upper(), md5.hexdigest().lower()


def predecessor_readback(
    session: requests.Session, predecessor: dict
) -> dict[str, dict]:
    entries = entries_map(predecessor)
    if PREDECESSOR_PARTIAL.is_file():
        partial = json.loads(
            PREDECESSOR_PARTIAL.read_text(encoding="utf-8")
        )
        if (
            int(partial.get("record", -1)) != PREDECESSOR_RECORD
            or partial.get("conceptdoi") != CONCEPT_DOI
        ):
            raise RuntimeError("Stale EGA predecessor partial receipt")
        identities = partial.get("files", {})
        zip_summaries = partial.get("zip_summaries", {})
    else:
        identities = {}
        zip_summaries = {}
    clean_temp(READBACK_ROOT)
    READBACK_ROOT.mkdir(parents=True)
    try:
        for index, name in enumerate(
            sorted(entries, key=str.casefold), start=1
        ):
            entry = entries[name]
            expected_size = int(entry["size"])
            expected_md5 = normalize_checksum(entry["checksum"])
            existing = identities.get(name)
            if existing is not None:
                if (
                    int(existing["bytes"]),
                    existing["md5"].lower(),
                ) != (
                    expected_size,
                    expected_md5,
                ):
                    raise RuntimeError(
                        f"Partial predecessor identity drift: {name}"
                    )
                print(
                    f"PREDECESSOR READBACK {index}/{len(entries)} "
                    f"{name} (resume exact)",
                    flush=True,
                )
                continue
            print(
                f"PREDECESSOR READBACK {index}/{len(entries)} {name}",
                flush=True,
            )
            target = READBACK_ROOT / f"predecessor-{index:02d}"
            size, sha, md5 = download_file(
                session, entry["links"]["content"], target
            )
            if (size, md5) != (expected_size, expected_md5):
                raise RuntimeError(
                    f"Predecessor public identity mismatch: {name}"
                )
            identities[name] = {
                "bytes": size,
                "sha256": sha,
                "md5": md5,
            }
            if name.lower().endswith(".zip"):
                zip_summaries[name] = inspect_zip(
                    target, include_members=False
                )
            target.unlink()
            save_json(
                PREDECESSOR_PARTIAL,
                {
                    "status": "PARTIAL",
                    "record": PREDECESSOR_RECORD,
                    "conceptdoi": CONCEPT_DOI,
                    "files": identities,
                    "zip_summaries": zip_summaries,
                },
            )
    finally:
        clean_temp(READBACK_ROOT)

    receipt = {
        "status": "PASS",
        "errors": [],
        "record": PREDECESSOR_RECORD,
        "doi": PREDECESSOR_DOI,
        "conceptdoi": CONCEPT_DOI,
        "file_count": len(identities),
        "bytes": sum(row["bytes"] for row in identities.values()),
        "files": identities,
        "zip_summaries": zip_summaries,
    }
    save_json(PREDECESSOR_RECEIPT, receipt)
    PREDECESSOR_PARTIAL.unlink(missing_ok=True)
    return identities


def verify_static_local_files() -> dict[str, dict]:
    result = {}
    for name, path in STATIC_LOCAL_PATHS.items():
        if not path.is_file():
            raise RuntimeError(f"Missing local EGA release file: {path}")
        actual = (path.stat().st_size, sha256_file(path))
        if actual != STATIC_EXPECTED[name]:
            raise RuntimeError(f"Local EGA release identity mismatch: {name}")
        result[name] = {
            "path": path,
            "bytes": actual[0],
            "sha256": actual[1],
            "md5": md5_file(path),
        }
    zip_check = inspect_zip(
        STATIC_LOCAL_PATHS[NEW_ZIP], include_members=False
    )
    manifest = zip_check.get("internal_manifest", {})
    if (
        zip_check["file_members"] != EXPECTED_NEW_ZIP_MEMBERS
        or zip_check["uncompressed_bytes"]
        != EXPECTED_NEW_ZIP_UNCOMPRESSED_BYTES
        or manifest.get("rows") != EXPECTED_NEW_ZIP_MANIFEST_ROWS
        or manifest.get("sha256") != EXPECTED_NEW_ZIP_MANIFEST_SHA256
        or manifest.get("errors")
    ):
        raise RuntimeError("Local EGA source ZIP closure mismatch")
    return result


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
                "Untracked EGA successor draft exists; refusing blind mutation"
            )
        state = json.loads(DRAFT_STATE.read_text(encoding="utf-8"))
        draft = existing.json()
        draft_id = int(draft["id"])
        if (
            draft_id != int(state["draft_id"])
            or int(state["predecessor_record"]) != PREDECESSOR_RECORD
            or concept_doi(draft) != CONCEPT_DOI
        ):
            raise RuntimeError("Existing EGA draft is not the tracked draft")
        return draft_id
    check(existing, {404})

    if DRAFT_STATE.is_file():
        state = json.loads(DRAFT_STATE.read_text(encoding="utf-8"))
        if state.get("published"):
            raise RuntimeError(
                "Tracked EGA successor is published; use --readback-only"
            )
        raise RuntimeError("Tracked EGA draft state exists but draft is absent")

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
        raise RuntimeError("EGA predecessor is not a versioning base")
    created = check(
        session.post(
            legacy["links"]["newversion"],
            headers=auth,
            timeout=(30, 300),
        ),
        {201},
    ).json()
    draft = check(
        session.get(
            created["links"]["latest_draft"],
            headers=auth,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    draft_id = int(draft["id"])
    if (
        concept_doi(draft) != CONCEPT_DOI
        or set(legacy_file_map(draft)) != set(entries_map(predecessor))
    ):
        raise RuntimeError("New EGA version did not inherit exact predecessor")
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


def release_note(draft_id: int) -> str:
    github_url = (
        "https://github.com/KokunoYumeto/modern-latex-manuscripts/tree/"
        f"{GITHUB_COMMIT}/{GITHUB_PACKAGE}"
    )
    return f"""# EGA 0 section-11 source-first working successor

This is one same-concept successor to Zenodo record {PREDECESSOR_RECORD}.
It retains all 16 predecessor files byte-for-byte and reserves record
{draft_id} in the existing EGA concept.

## Reading surface

`{NEW_PDF}` is a 93-page US-letter EGA 0 working reader. It contains inherited
English context for sections 1.0-11.5 and 12.1-14.3.6. The source-first range
verified by this checkpoint is strictly sections 11.5.1-11.10.3, against EGA
III Part 1 authority PDF pages 32-46 / printed pages 35-49. The next
source-first unit is section 12.1.1.

The direct TeX is the complete section-11 component; its source-first successor
span begins at 11.5.1. The grouped source ZIP contains 96 safe members,
including a 95-row internal identity manifest, and rebuilds the 93-page reader.

## Checks and caveats

- 288 named destinations and 637 valid internal GoTo links;
- six pdfLaTeX passes plus BibTeX in an isolated rebuild;
- 93/93 extracted-text and geometry pages match the candidate;
- zero hard build diagnostics;
- six disclosed inherited unresolved cross-volume or earlier-range references;
- public-source ZIP CRC, safe-path, manifest, and privacy closure PASS; and
- visual inspection of pages 1, 80, 87, and 93 in archive curation, in addition
  to the producer's section 11.8-11.10 page review.

This is a bounded machine-assisted working checkpoint, not completion of EGA,
a critical edition, certification of surrounding inherited prose, peer review,
rights clearance, exhaustive reference closure, or tagged-PDF accessibility
remediation. Existing user-supplied OCR was consulted read-only and was not
generated or rerun. No new license grant is asserted.

GitHub custody: `{github_url}`.
"""


def generate_controls(
    draft_id: int,
    static_local: dict[str, dict],
    predecessor_identities: dict[str, dict],
) -> dict[str, dict]:
    clean_temp(CONTROLS_ROOT)
    CONTROLS_ROOT.mkdir(parents=True)
    note_path = CONTROLS_ROOT / NEW_NOTE
    write_text(note_path, release_note(draft_id))
    note_identity = {
        "path": note_path,
        "bytes": note_path.stat().st_size,
        "sha256": sha256_file(note_path),
        "md5": md5_file(note_path),
    }

    new_without_validation = {
        **static_local,
        NEW_NOTE: note_identity,
    }
    validation = {
        "schema": "ega0_iii_11_10_zenodo_successor_validation.v1",
        "status": "PASS_READY_FOR_ONE_SAME_CONCEPT_SUCCESSOR",
        "errors": [],
        "concept_doi": CONCEPT_DOI,
        "predecessor_record": PREDECESSOR_RECORD,
        "predecessor_doi": PREDECESSOR_DOI,
        "reserved_successor_record": draft_id,
        "retained_predecessor_files": EXPECTED_RETAINED_FILES,
        "new_files_excluding_this_validation": {
            name: {
                "bytes": identity["bytes"],
                "sha256": identity["sha256"],
            }
            for name, identity in sorted(
                new_without_validation.items(), key=lambda row: row[0].casefold()
            )
        },
        "final_file_count": EXPECTED_FINAL_FILES,
        "default_preview": DEFAULT_PREVIEW,
        "github": {
            "commit": GITHUB_COMMIT,
            "package": GITHUB_PACKAGE,
            "outer_files_read_back": 9,
            "zip_members_read_back": 96,
            "status": "PASS",
        },
        "scope": {
            "reader_container": "EGA 0 sections 1.0-14.3.6",
            "source_first_verified": "sections 11.5.1-11.10.3",
            "next_source_first_unit": "section 12.1.1",
            "surrounding_context_source_certified_here": False,
            "whole_ega_complete": False,
        },
        "reader": {
            "pages": 93,
            "page_size": "US letter",
            "named_destinations": 288,
            "internal_goto": 637,
            "uri_or_other_actions": 0,
        },
        "source_zip": {
            "members": EXPECTED_NEW_ZIP_MEMBERS,
            "manifest_rows": EXPECTED_NEW_ZIP_MANIFEST_ROWS,
            "manifest_sha256": EXPECTED_NEW_ZIP_MANIFEST_SHA256,
            "uncompressed_bytes": EXPECTED_NEW_ZIP_UNCOMPRESSED_BYTES,
        },
        "retained_predecessor_bytes": sum(
            row["bytes"] for row in predecessor_identities.values()
        ),
        "ocr_generated_or_rerun": False,
        "duplicate_concept_created": False,
        "second_draft_created": False,
    }
    validation_path = CONTROLS_ROOT / NEW_VALIDATION
    save_json(validation_path, validation)
    validation_identity = {
        "path": validation_path,
        "bytes": validation_path.stat().st_size,
        "sha256": sha256_file(validation_path),
        "md5": md5_file(validation_path),
    }
    return {
        **new_without_validation,
        NEW_VALIDATION: validation_identity,
    }


def final_expected(
    predecessor_identities: dict[str, dict],
    local_files: dict[str, dict],
) -> dict[str, dict]:
    if len(predecessor_identities) != EXPECTED_RETAINED_FILES:
        raise RuntimeError("Unexpected EGA predecessor identity boundary")
    overlap = set(predecessor_identities) & set(local_files)
    if overlap:
        raise RuntimeError(f"New filenames collide with predecessor: {overlap}")
    expected = {**predecessor_identities, **local_files}
    if len(expected) != EXPECTED_FINAL_FILES:
        raise RuntimeError("Unexpected final EGA file boundary")
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
        raise RuntimeError("Tracked EGA successor is not an unpublished draft")
    files = legacy_file_map(deposition)
    extras = set(files) - set(expected)
    if extras:
        raise RuntimeError(f"Unexpected EGA draft files: {sorted(extras)}")

    actions = []
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
            raise RuntimeError(f"EGA upload response mismatch: {name}")
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
        raise RuntimeError("Staged EGA draft file set mismatch")
    for name, identity in expected.items():
        observed = (
            int(final_files[name]["filesize"]),
            normalize_checksum(final_files[name]["checksum"]),
        )
        if observed != (identity["bytes"], identity["md5"]):
            raise RuntimeError(f"Staged EGA identity mismatch: {name}")

    receipt = {
        "status": "PASS_STAGED",
        "errors": [],
        "predecessor_record": PREDECESSOR_RECORD,
        "draft_id": draft_id,
        "concept_doi": CONCEPT_DOI,
        "file_count": len(final_files),
        "bytes": sum(int(row["filesize"]) for row in final_files.values()),
        "retained_predecessor_files": EXPECTED_RETAINED_FILES,
        "new_files": len(local_files),
        "actions": actions,
        "duplicate_concept_created": False,
        "second_draft_created": False,
    }
    save_json(
        RECEIPT_ROOT
        / f"20260728_ega0_iii_section11_record_{draft_id}_draft_files.json",
        receipt,
    )
    return receipt


def patch_notes(metadata: dict) -> None:
    descriptions = [
        row
        for row in metadata.get("additional_descriptions", [])
        if row.get("type", {}).get("id") != "notes"
    ]
    descriptions.append(
        {
            "description": NOTES_HTML,
            "type": {"id": "notes", "title": {"en": "Notes"}},
        }
    )
    metadata["additional_descriptions"] = descriptions


def assert_metadata(metadata: dict) -> None:
    if metadata.get("title") != TITLE:
        raise RuntimeError("EGA title metadata mismatch")
    if metadata.get("version") != VERSION:
        raise RuntimeError("EGA version metadata mismatch")
    if metadata.get("publication_date") != PUBLICATION_DATE:
        raise RuntimeError("EGA publication-date metadata mismatch")
    if metadata.get("description") != DESCRIPTION_HTML:
        raise RuntimeError("EGA description metadata mismatch")
    if not any(
        row.get("description") == NOTES_HTML
        for row in metadata.get("additional_descriptions", [])
    ):
        raise RuntimeError("EGA notes metadata mismatch")


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
        raise RuntimeError("EGA draft escaped the existing concept")
    files = check(
        session.get(
            draft["links"]["files"], headers=headers, timeout=(30, 180)
        ),
        {200},
    ).json()
    entries = files.get("entries", {})
    if isinstance(entries, list):
        entries = {row["key"]: row for row in entries}
    files["entries"] = entries
    draft["files"] = files
    return draft


def ordered_names(expected: dict[str, dict]) -> list[str]:
    priority = [NEW_PDF, OLD_ENGLISH_PDF, NEW_TEX, OLD_EGA_IV_PDF]
    result = [name for name in priority if name in expected]
    result.extend(
        name
        for name in sorted(expected, key=str.casefold)
        if name not in result
    )
    if len(result) != len(expected):
        raise RuntimeError("EGA file-order construction failed")
    return result


def publish_draft(
    session: requests.Session,
    token: str,
    draft_id: int,
    expected: dict[str, dict],
) -> dict:
    draft = modern_draft(session, token, draft_id)
    if set(draft["files"]["entries"]) != set(expected):
        raise RuntimeError("Cannot publish EGA draft: file set mismatch")

    metadata = copy.deepcopy(draft["metadata"])
    metadata["title"] = TITLE
    metadata["version"] = VERSION
    metadata["publication_date"] = PUBLICATION_DATE
    metadata["description"] = DESCRIPTION_HTML
    patch_notes(metadata)
    payload = {
        "access": draft["access"],
        "files": {
            "enabled": True,
            "default_preview": DEFAULT_PREVIEW,
            "order": ordered_names(expected),
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
    if (
        reread["files"].get("default_preview") != DEFAULT_PREVIEW
        or set(reread["files"]["entries"]) != set(expected)
    ):
        raise RuntimeError("EGA draft changed after metadata patch")

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
        raise RuntimeError("Published EGA response escaped the concept")
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
        / f"20260728_ega0_iii_section11_record_{draft_id}_publish_response.json",
        receipt,
    )
    return receipt


def wait_for_public(session: requests.Session, record_id: int) -> dict:
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
    raise RuntimeError("Published EGA successor did not stabilize")


def anonymous_readback(
    record_id: int,
    expected: dict[str, dict],
    predecessor_receipt: dict,
) -> tuple[dict, dict]:
    session = make_session()
    record = wait_for_public(session, record_id)
    if int(record["id"]) != record_id or concept_doi(record) != CONCEPT_DOI:
        raise RuntimeError("Public EGA successor lineage mismatch")
    assert_metadata(record["metadata"])
    if record["files"].get("default_preview") != DEFAULT_PREVIEW:
        raise RuntimeError("Public EGA default preview mismatch")
    entries = entries_map(record)
    if set(entries) != set(expected):
        raise RuntimeError("Public EGA outer-file set mismatch")

    latest = check(
        session.get(
            f"{API}/records/{PREDECESSOR_RECORD}/versions/latest?expand=true",
            headers={"Accept": "application/vnd.inveniordm.v1+json"},
            timeout=(30, 180),
        ),
        {200},
    ).json()
    if int(latest["id"]) != record_id or concept_doi(latest) != CONCEPT_DOI:
        raise RuntimeError("Public EGA successor is not the concept head")

    clean_temp(READBACK_ROOT)
    READBACK_ROOT.mkdir(parents=True)
    file_receipt = {}
    zip_receipt = {}
    try:
        for index, name in enumerate(
            sorted(entries, key=str.casefold), start=1
        ):
            print(
                f"PUBLIC READBACK {index}/{len(entries)} {name}",
                flush=True,
            )
            entry = entries[name]
            target = READBACK_ROOT / f"public-{index:02d}"
            size, sha, md5 = download_file(
                session, entry["links"]["content"], target
            )
            wanted = expected[name]
            match = (
                size,
                sha,
                md5,
            ) == (
                wanted["bytes"],
                wanted["sha256"],
                wanted["md5"],
            )
            if not match:
                raise RuntimeError(f"Public EGA readback mismatch: {name}")
            file_receipt[name] = {
                "bytes": size,
                "sha256": sha,
                "md5": md5,
                "url": entry["links"]["content"],
                "match": True,
            }
            if name.lower().endswith(".zip"):
                summary = inspect_zip(target, include_members=True)
                if name == NEW_ZIP:
                    manifest = summary.get("internal_manifest", {})
                    if (
                        summary["file_members"] != EXPECTED_NEW_ZIP_MEMBERS
                        or summary["uncompressed_bytes"]
                        != EXPECTED_NEW_ZIP_UNCOMPRESSED_BYTES
                        or manifest.get("rows")
                        != EXPECTED_NEW_ZIP_MANIFEST_ROWS
                        or manifest.get("sha256")
                        != EXPECTED_NEW_ZIP_MANIFEST_SHA256
                        or manifest.get("errors")
                    ):
                        raise RuntimeError(
                            "Public new EGA source ZIP closure mismatch"
                        )
                else:
                    prior = predecessor_receipt["zip_summaries"].get(name)
                    if prior is None:
                        raise RuntimeError(
                            f"Retained ZIP lacks predecessor control: {name}"
                        )
                    current_core = {
                        key: summary[key]
                        for key in (
                            "file_members",
                            "directory_entries",
                            "all_entries",
                            "uncompressed_bytes",
                            "canonical_member_identity_sha256",
                            "crc_error",
                            "safe_paths",
                        )
                    }
                    if current_core != prior:
                        raise RuntimeError(
                            f"Retained ZIP member readback changed: {name}"
                        )
                zip_receipt[name] = summary
            target.unlink()
    finally:
        clean_temp(READBACK_ROOT)

    retained_matches = sum(
        file_receipt[name]["match"]
        for name in predecessor_receipt["files"]
    )
    if retained_matches != EXPECTED_RETAINED_FILES:
        raise RuntimeError("Not all EGA predecessor files were retained")
    public_receipt = {
        "status": "PASS",
        "errors": [],
        "record": record_id,
        "doi": version_doi(record),
        "conceptdoi": CONCEPT_DOI,
        "record_url": f"https://zenodo.org/records/{record_id}",
        "version": VERSION,
        "file_count": len(file_receipt),
        "bytes": sum(row["bytes"] for row in file_receipt.values()),
        "files": file_receipt,
        "latest_record": int(latest["id"]),
        "rdm_default_preview": record["files"].get("default_preview"),
        "rdm_file_order": record["files"].get("order", []),
        "github_commit": GITHUB_COMMIT,
        "github_package": GITHUB_PACKAGE,
        "retained_predecessor_files": retained_matches,
        "new_files": len(file_receipt) - retained_matches,
        "duplicate_concept_created": False,
        "second_draft_created": False,
    }
    zipped = {
        "status": "PASS",
        "errors": [],
        "record": record_id,
        "doi": version_doi(record),
        "zip_archive_count": len(zip_receipt),
        "archives": zip_receipt,
    }
    save_json(
        RECEIPT_ROOT
        / f"20260728_ega0_iii_section11_record_{record_id}_public_readback.json",
        public_receipt,
    )
    save_json(
        RECEIPT_ROOT
        / f"20260728_ega0_iii_section11_record_{record_id}_zip_member_readback.json",
        zipped,
    )
    return public_receipt, zipped


def load_predecessor_receipt() -> dict:
    if not PREDECESSOR_RECEIPT.is_file():
        raise RuntimeError("Missing EGA predecessor readback receipt")
    receipt = json.loads(PREDECESSOR_RECEIPT.read_text(encoding="utf-8"))
    if (
        receipt.get("status") != "PASS"
        or int(receipt.get("record", -1)) != PREDECESSOR_RECORD
        or receipt.get("conceptdoi") != CONCEPT_DOI
        or len(receipt.get("files", {})) != EXPECTED_PREDECESSOR_FILES
    ):
        raise RuntimeError("EGA predecessor receipt is not controlling")
    return receipt


def receipt_identities(receipt: dict) -> dict[str, dict]:
    return {
        name: {
            "bytes": int(row["bytes"]),
            "sha256": row["sha256"].upper(),
            "md5": row["md5"].lower(),
        }
        for name, row in receipt["files"].items()
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--readback-only", action="store_true")
    args = parser.parse_args()

    static_local = verify_static_local_files()
    if args.readback_only:
        state = json.loads(DRAFT_STATE.read_text(encoding="utf-8"))
        if not state.get("published"):
            raise RuntimeError("Tracked EGA successor is not published")
        predecessor_receipt = load_predecessor_receipt()
        predecessor_identities = receipt_identities(predecessor_receipt)
        local_files = generate_controls(
            int(state["draft_id"]),
            static_local,
            predecessor_identities,
        )
        expected = final_expected(predecessor_identities, local_files)
        public, zipped = anonymous_readback(
            int(state["draft_id"]), expected, predecessor_receipt
        )
        print(
            json.dumps(
                {
                    "status": public["status"],
                    "record": public["record"],
                    "doi": public["doi"],
                    "files": public["file_count"],
                    "bytes": public["bytes"],
                    "zip_archives": zipped["zip_archive_count"],
                },
                indent=2,
            ),
            flush=True,
        )
        return

    token = find_token()
    session = make_session()
    assert_predecessor_is_latest(session)
    predecessor = public_predecessor(session)
    predecessor_identities = predecessor_readback(session, predecessor)
    predecessor_receipt = load_predecessor_receipt()
    draft_id = create_or_resume_draft(session, token, predecessor)
    local_files = generate_controls(
        draft_id, static_local, predecessor_identities
    )
    expected = final_expected(predecessor_identities, local_files)
    stage = stage_draft(
        session, token, draft_id, expected, local_files
    )
    publish = publish_draft(
        session, token, draft_id, expected
    )
    public, zipped = anonymous_readback(
        draft_id, expected, predecessor_receipt
    )
    print(
        json.dumps(
            {
                "stage": stage,
                "publish": publish,
                "readback": {
                    "status": public["status"],
                    "record": public["record"],
                    "doi": public["doi"],
                    "files": public["file_count"],
                    "bytes": public["bytes"],
                    "zip_archives": zipped["zip_archive_count"],
                },
            },
            indent=2,
        ),
        flush=True,
    )


if __name__ == "__main__":
    main()
