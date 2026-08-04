#!/usr/bin/env python3
"""Validate, stage, publish, and read back the existing FAC draft 21781714.

This script is deliberately unable to create a draft or concept.  It accepts
only the already-uploaded 33-file successor of FAC concept 21720996, preserves
the exact file bytes, replaces the obsolete mixed FAC/GAGA metadata, selects
the readable comparison report as the preview, and anonymously reads every
published byte back after publication.
"""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import json
import sys
import time
import zipfile
from pathlib import Path

import publish_current_reader_bundles_zenodo_20260730 as base


API = base.API
MODERN = {"Accept": "application/vnd.inveniordm.v1+json"}
DRAFT_ID = 21781714
PREDECESSOR_ID = 21764488
CONCEPT_ID = "21720996"
CONCEPT_DOI = "10.5281/zenodo.21720996"
REDUNDANT_RECORD_ID = 21779393
GAGA_RECORD_ID = 21781323
GAGA_CONCEPT_ID = "21781322"
REPORT = "00_FAC_Blind_Comparison_Readable_Report.pdf"
MANIFEST = "ZENODO_PAYLOAD_MANIFEST.csv"
VALIDATION = "PACKAGE_VALIDATION.json"
COMPLETE_ZIP = "04_FAC_Complete_Readers_Source_and_Blind_Comparison_Evidence_20260804.zip"

EXPECTED_FILES = 33
EXPECTED_BYTES = 10_503_869
EXPECTED_MANIFEST_ROWS = 31
EXPECTED_MANIFEST_BYTES = 4_772
EXPECTED_MANIFEST_SHA256 = (
    "6222C2A71509EEC564630CC62823B95DDE747F47C40AB4B6A8DEDCA9CE121BA2"
)
EXPECTED_VALIDATION_BYTES = 5_445
EXPECTED_VALIDATION_SHA256 = (
    "74973347C3A29D481CC4FDDE3DA64EFA30E8D6A8E2FFC4D108CF4A105E046630"
)
EXPECTED_ZIP_BYTES = 4_640_745
EXPECTED_ZIP_SHA256 = (
    "93DAFB1053F5383714E6EF20384B046CC67A0C33D0029E38D921F6E107A51DFC"
)
EXPECTED_ZIP_MEMBERS = 30
EXPECTED_REPORT_BYTES = 141_174
EXPECTED_REPORT_SHA256 = (
    "F1A643DDF5810DC983C78FE4F300572779F5C1C3D8D308ECC11B84F79B7EEFE1"
)

TITLE = (
    "Jean-Pierre Serre’s FAC: French transcription, English translation, "
    "and an accidental blind comparison"
)
# Zenodo normalizes the typographic apostrophe in the submitted title to ASCII.
# Accept only that exact platform normalization, not arbitrary title drift.
ZENODO_NORMALIZED_TITLE = TITLE.replace("’", "'")
PUBLICATION_DATE = "2026-08-04"
VERSION = "2026-08-04 complete FAC readers and blind comparison"

DESCRIPTION = """<h2>Why this record exists</h2>
<p>This record brings FAC into one coherent publication line. It contains a complete French working transcription, a complete English reader, and a documented comparison between two English translations.</p>
<p>The comparison happened by accident. The project coordinator did not know that a published English translation by Piotr Achinger and Marcin Krupa already existed and asked OpenAI Codex 5.6 Ultra to translate FAC from a French working transcription initially produced in the Claude Opus 5 project lane and subsequently corrected against Serre's source. The published translation was found only after that work was finished. This made a genuine blind comparison possible: 79 numbered units were reviewed one by one, with 138 findings and a 219-entry self-correction ledger. The model names are project/runtime records, not cryptographic attestations.</p>
<p>Start with 00_FAC_Blind_Comparison_Readable_Report.pdf. It gives the chronology, worked examples, evidence, limitations, and audit procedure in a 36-page report. The CSV files and logbooks preserve the complete machine-readable record. Separate files provide the French reader and TeX, the complete English reader, the pre-discovery English reader through no. 79, and the complete source/evidence projection.</p>
<p>The bounded comparison did not show indiscriminate mathematical sloppiness, but it is not a scalar score, a general benchmark, a critical edition, or a mathematician's peer review. Important passages should still be checked against Serre's French source. Rights in the underlying works remain with their holders; the authority scan and the Achinger–Krupa source are identified but not redistributed.</p>
<p>GAGA is maintained separately under concept DOI 10.5281/zenodo.21781322. The redundant FAC quality-assessment concept 10.5281/zenodo.21779392 was tombstoned as a duplicate and its useful content was folded into this FAC publication line.</p>"""

ADDITIONAL_NOTE = """<p>Package validation PASS/errors[]. Public projection: 30-member complete ZIP, 31-row self-excluding manifest, four verified PDFs (36, 63, 78, 74 pages), 79 unit reviews, 138 findings, 219 self-corrections, privacy hits0, GAGA files0. Readable report has embedded non-Type3 fonts and broken named links0.</p>"""

ADDED_SUBJECTS = [
    "blind translation comparison",
    "comparative translation",
    "AI-assisted translation",
    "translation quality assessment",
    "provenance",
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def md5(path: Path) -> str:
    digest = hashlib.md5()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().lower()


def local_surface(root: Path) -> dict[str, dict[str, object]]:
    if not root.is_dir():
        raise RuntimeError(f"FAC package root is not a directory: {root}")
    paths = sorted((p for p in root.iterdir() if p.is_file()), key=lambda p: p.name.casefold())
    if len(paths) != EXPECTED_FILES or sum(p.stat().st_size for p in paths) != EXPECTED_BYTES:
        raise RuntimeError("FAC top-level file count or byte total changed")

    fixed = {
        MANIFEST: (EXPECTED_MANIFEST_BYTES, EXPECTED_MANIFEST_SHA256),
        VALIDATION: (EXPECTED_VALIDATION_BYTES, EXPECTED_VALIDATION_SHA256),
        COMPLETE_ZIP: (EXPECTED_ZIP_BYTES, EXPECTED_ZIP_SHA256),
        REPORT: (EXPECTED_REPORT_BYTES, EXPECTED_REPORT_SHA256),
    }
    for name, identity in fixed.items():
        path = root / name
        if (path.stat().st_size, sha256(path)) != identity:
            raise RuntimeError(f"Fixed FAC identity changed: {name}")

    validation = json.loads((root / VALIDATION).read_text(encoding="utf-8"))
    if validation.get("status") != "PASS" or validation.get("errors") != []:
        raise RuntimeError("FAC package validation is not PASS/errors[]")

    with (root / MANIFEST).open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    if len(rows) != EXPECTED_MANIFEST_ROWS:
        raise RuntimeError("FAC manifest row count changed")
    represented = set()
    for row in rows:
        name = row["path"]
        path = root / name
        represented.add(name)
        if not path.is_file():
            raise RuntimeError(f"FAC manifest member missing: {name}")
        if path.stat().st_size != int(row["bytes"]) or sha256(path) != row["sha256"].upper():
            raise RuntimeError(f"FAC manifest replay changed: {name}")
    if set(p.name for p in paths) - represented != {MANIFEST, VALIDATION}:
        raise RuntimeError("FAC self-excluding manifest boundary changed")

    with zipfile.ZipFile(root / COMPLETE_ZIP) as archive:
        infos = archive.infolist()
        if len(infos) != EXPECTED_ZIP_MEMBERS or archive.testzip() is not None:
            raise RuntimeError("FAC complete ZIP member count or CRC changed")
        for info in infos:
            parts = Path(info.filename.replace("\\", "/")).parts
            if info.filename.startswith(("/", "\\")) or ".." in parts:
                raise RuntimeError(f"Unsafe FAC ZIP member: {info.filename}")

    surface = {
        path.name: {
            "path": path,
            "bytes": path.stat().st_size,
            "md5": md5(path),
            "sha256": sha256(path),
        }
        for path in paths
    }
    private_patterns = [b"C:\\Users\\Floris", b"/Users/Floris", b".codex/"]
    privacy_hits = []
    for path in paths:
        data = path.read_bytes()
        for pattern in private_patterns:
            if pattern.lower() in data.lower():
                privacy_hits.append({"file": path.name, "pattern": pattern.decode("ascii")})
    if privacy_hits:
        raise RuntimeError(f"FAC privacy scan changed: {privacy_hits}")
    return surface


def auth(token: str) -> dict[str, str]:
    return {"Authorization": f"Bearer {token}"}


def auth_modern(token: str) -> dict[str, str]:
    return {**MODERN, **auth(token)}


def check_tombstone_and_gaga(session) -> dict[str, object]:
    tombstone = session.get(
        f"{API}/records/{REDUNDANT_RECORD_ID}", headers=MODERN, timeout=(30, 180)
    )
    if tombstone.status_code != 410:
        raise RuntimeError("Redundant FAC record is not tombstoned")
    tombstone_json = tombstone.json()
    if tombstone_json.get("tombstone", {}).get("removal_reason", {}).get("id") != "duplicate":
        raise RuntimeError("Redundant FAC tombstone reason changed")
    gaga = base.check(
        session.get(f"{API}/records/{GAGA_RECORD_ID}", headers=MODERN, timeout=(30, 180)),
        {200},
    ).json()
    if str(gaga.get("parent", {}).get("id")) != GAGA_CONCEPT_ID or gaga.get("status") != "published":
        raise RuntimeError("Separate GAGA lineage changed")
    return {
        "redundant_fac_record": REDUNDANT_RECORD_ID,
        "redundant_fac_status": 410,
        "redundant_fac_removal_reason": "duplicate",
        "gaga_record": GAGA_RECORD_ID,
        "gaga_concept": GAGA_CONCEPT_ID,
        "gaga_status": "published",
    }


def fetch_draft(session, token: str) -> tuple[dict, dict]:
    legacy = base.check(
        session.get(
            f"{API}/deposit/depositions/{DRAFT_ID}",
            headers=auth(token),
            timeout=(30, 180),
        ),
        {200},
    ).json()
    modern = base.check(
        session.get(
            f"{API}/records/{DRAFT_ID}/draft?expand=true",
            headers=auth_modern(token),
            timeout=(30, 180),
        ),
        {200},
    ).json()
    if (
        int(legacy.get("id", -1)) != DRAFT_ID
        or legacy.get("submitted") is not False
        or legacy.get("state") != "unsubmitted"
        or str(legacy.get("conceptrecid")) != CONCEPT_ID
        or str(modern.get("parent", {}).get("id")) != CONCEPT_ID
        or modern.get("parent", {}).get("pids", {}).get("doi", {}).get("identifier") != CONCEPT_DOI
        or modern.get("status") != "new_version_draft"
        or modern.get("is_published") is not False
        or modern.get("versions", {}).get("index") != 5
        or modern.get("versions", {}).get("is_latest_draft") is not True
    ):
        raise RuntimeError("FAC draft identity, lineage, or state changed")
    return legacy, modern


def verify_remote_files(legacy: dict, surface: dict[str, dict[str, object]]) -> None:
    remote = {
        row["filename"]: {
            "bytes": int(row["filesize"]),
            "md5": str(row["checksum"]).removeprefix("md5:").lower(),
        }
        for row in legacy.get("files", [])
    }
    expected = {
        name: {"bytes": int(row["bytes"]), "md5": str(row["md5"])}
        for name, row in surface.items()
    }
    if remote != expected:
        raise RuntimeError("FAC server/local file boundary or identity changed")
    if any("gaga" in name.casefold() for name in remote):
        raise RuntimeError("A GAGA filename remains in the FAC draft")


def desired_metadata(current: dict) -> dict:
    metadata = copy.deepcopy(current)
    metadata["resource_type"] = {"id": "dataset"}
    metadata["title"] = TITLE
    metadata["publication_date"] = PUBLICATION_DATE
    metadata["version"] = VERSION
    metadata["languages"] = [{"id": "fra"}, {"id": "eng"}]
    subjects = []
    seen = set()
    for row in current.get("subjects", []):
        value = str(row.get("subject", "")).strip()
        if not value or value.casefold() == "gaga" or value.casefold() in seen:
            continue
        seen.add(value.casefold())
        subjects.append({"subject": value})
    for value in ADDED_SUBJECTS:
        if value.casefold() not in seen:
            subjects.append({"subject": value})
            seen.add(value.casefold())
    metadata["subjects"] = subjects
    metadata["description"] = DESCRIPTION
    metadata["additional_descriptions"] = [
        {"description": ADDITIONAL_NOTE, "type": {"id": "notes"}}
    ]
    return metadata


def verify_staged_metadata(draft: dict) -> None:
    metadata = draft.get("metadata", {})
    subject_values = [str(row.get("subject", "")) for row in metadata.get("subjects", [])]
    language_ids = [str(row.get("id")) for row in metadata.get("languages", [])]
    notes = metadata.get("additional_descriptions", [])
    if (
        metadata.get("title") not in {TITLE, ZENODO_NORMALIZED_TITLE}
        or metadata.get("publication_date") != PUBLICATION_DATE
        or metadata.get("version") != VERSION
        or metadata.get("resource_type", {}).get("id") != "dataset"
        or language_ids != ["fra", "eng"]
        or metadata.get("description") != DESCRIPTION
        or len(notes) != 1
        or notes[0].get("description") != ADDITIONAL_NOTE
        or notes[0].get("type", {}).get("id") != "notes"
        or any(value.casefold() == "gaga" for value in subject_values)
        or not all(value in subject_values for value in ADDED_SUBJECTS)
        or draft.get("files", {}).get("default_preview") != REPORT
    ):
        raise RuntimeError("FAC staged metadata or preview changed")


def preflight(session, token: str, root: Path) -> dict[str, object]:
    surface = local_surface(root)
    legacy, draft = fetch_draft(session, token)
    verify_remote_files(legacy, surface)
    related = check_tombstone_and_gaga(session)
    return {
        "status": "PASS_EXISTING_DRAFT_READY_FOR_METADATA_STAGE",
        "draft_id": DRAFT_ID,
        "concept_id": CONCEPT_ID,
        "concept_doi": CONCEPT_DOI,
        "predecessor_id": PREDECESSOR_ID,
        "version_index": draft["versions"]["index"],
        "files": len(surface),
        "bytes": sum(int(row["bytes"]) for row in surface.values()),
        "identity_mismatches": 0,
        "gaga_filenames": 0,
        "current_default_preview": draft.get("files", {}).get("default_preview"),
        "required_default_preview": REPORT,
        **related,
    }


def stage(session, token: str, root: Path) -> dict[str, object]:
    surface = local_surface(root)
    legacy, draft = fetch_draft(session, token)
    verify_remote_files(legacy, surface)
    check_tombstone_and_gaga(session)
    order = [REPORT] + sorted((name for name in surface if name != REPORT), key=str.casefold)
    payload = {
        "access": draft["access"],
        "files": {"enabled": True, "default_preview": REPORT, "order": order},
        "metadata": desired_metadata(draft["metadata"]),
        "custom_fields": draft.get("custom_fields", {}),
    }
    if draft.get("pids"):
        payload["pids"] = draft["pids"]
    patched = base.check(
        session.put(
            f"{API}/records/{DRAFT_ID}/draft",
            headers={**auth_modern(token), "Content-Type": "application/json"},
            json=payload,
            timeout=(30, 600),
        ),
        {200},
    ).json()
    verify_staged_metadata(patched)
    if set(patched.get("files", {}).get("entries", {})) != set(surface):
        raise RuntimeError("FAC file set changed while staging metadata")
    observed_order = patched.get("files", {}).get("order") or []
    if observed_order not in (order, []):
        raise RuntimeError("FAC file order changed unexpectedly")
    return {
        "status": "STAGED_EXISTING_DRAFT_VALIDATED",
        "draft_id": DRAFT_ID,
        "concept_doi": CONCEPT_DOI,
        "files": len(surface),
        "bytes": sum(int(row["bytes"]) for row in surface.values()),
        "default_preview": patched["files"]["default_preview"],
        "title": patched["metadata"]["title"],
        "publication_date": patched["metadata"]["publication_date"],
        "version": patched["metadata"]["version"],
        "languages": [row["id"] for row in patched["metadata"]["languages"]],
        "subjects": [row["subject"] for row in patched["metadata"]["subjects"]],
        "gaga_filenames": 0,
        "gaga_subjects": 0,
    }


def stream_identity(session, url: str) -> tuple[int, str]:
    response = base.check(session.get(url, stream=True, timeout=(30, 600)), {200})
    digest = hashlib.sha256()
    total = 0
    with response:
        for block in response.iter_content(1024 * 1024):
            if block:
                digest.update(block)
                total += len(block)
    return total, digest.hexdigest().upper()


def publish_and_readback(
    session,
    token: str,
    root: Path,
    receipt_path: Path | None,
) -> dict[str, object]:
    surface = local_surface(root)
    legacy, draft = fetch_draft(session, token)
    verify_remote_files(legacy, surface)
    verify_staged_metadata(draft)
    related = check_tombstone_and_gaga(session)
    published_response = base.check(
        session.post(
            draft["links"]["publish"],
            headers=auth_modern(token),
            timeout=(30, 1200),
        ),
        {200, 202},
    )
    try:
        published_id = int(published_response.json().get("id", DRAFT_ID))
    except Exception:
        published_id = DRAFT_ID
    if published_id != DRAFT_ID:
        raise RuntimeError("FAC publication returned an unexpected record ID")

    record = None
    for _ in range(30):
        probe = session.get(f"{API}/records/{DRAFT_ID}", headers=MODERN, timeout=(30, 180))
        if probe.status_code == 200 and probe.json().get("status") == "published":
            record = probe.json()
            break
        time.sleep(2)
    if record is None:
        raise RuntimeError("FAC record did not become anonymously public")

    if (
        str(record.get("parent", {}).get("id")) != CONCEPT_ID
        or record.get("parent", {}).get("pids", {}).get("doi", {}).get("identifier") != CONCEPT_DOI
        or record.get("versions", {}).get("index") != 5
        or record.get("versions", {}).get("is_latest") is not True
    ):
        raise RuntimeError("Published FAC concept/version identity changed")
    verify_staged_metadata(record)
    entries = record.get("files", {}).get("entries", {})
    if set(entries) != set(surface) or any("gaga" in name.casefold() for name in entries):
        raise RuntimeError("Published FAC file boundary changed")

    anonymous = base.make_session()
    readback_rows = []
    errors = []
    for index, name in enumerate(sorted(surface, key=str.casefold), start=1):
        print(f"READBACK {index}/{len(surface)} {name}", flush=True)
        observed_bytes, observed_sha = stream_identity(
            anonymous, entries[name]["links"]["content"]
        )
        expected = surface[name]
        match = (
            observed_bytes == int(expected["bytes"])
            and observed_sha == str(expected["sha256"])
        )
        if not match:
            errors.append(name)
        readback_rows.append(
            {
                "filename": name,
                "bytes": observed_bytes,
                "sha256": observed_sha,
                "match": match,
                "content_url": entries[name]["links"]["content"],
            }
        )
    if errors:
        raise RuntimeError(f"FAC anonymous readback mismatches: {errors}")

    draft_probe = session.get(
        f"{API}/records/{DRAFT_ID}/draft",
        headers=auth_modern(token),
        timeout=(30, 180),
    )
    if draft_probe.status_code not in {404, 410}:
        raise RuntimeError("FAC active draft remains after publication")

    result = {
        "status": "PASS_PUBLISHED_EXISTING_FAC_CONCEPT_AND_ANONYMOUS_RAW_READBACK",
        "errors": [],
        "record_id": DRAFT_ID,
        "record_url": record["links"]["self_html"],
        "version_doi": record["pids"]["doi"]["identifier"],
        "concept_id": CONCEPT_ID,
        "concept_doi": CONCEPT_DOI,
        "predecessor_record_id": PREDECESSOR_ID,
        "version_index": record["versions"]["index"],
        "title": record["metadata"]["title"],
        "publication_date": record["metadata"]["publication_date"],
        "version": record["metadata"]["version"],
        "resource_type": record["metadata"]["resource_type"]["id"],
        "languages": [row["id"] for row in record["metadata"]["languages"]],
        "subjects": [row["subject"] for row in record["metadata"]["subjects"]],
        "default_preview": record["files"]["default_preview"],
        "files": len(readback_rows),
        "bytes": sum(row["bytes"] for row in readback_rows),
        "readback_matches": sum(1 for row in readback_rows if row["match"]),
        "readback_mismatches": 0,
        "gaga_filenames": 0,
        "gaga_subjects": 0,
        "active_draft": False,
        "duplicate_concept_created": False,
        "complete_zip": {
            "filename": COMPLETE_ZIP,
            "bytes": EXPECTED_ZIP_BYTES,
            "sha256": EXPECTED_ZIP_SHA256,
            "members": EXPECTED_ZIP_MEMBERS,
            "crc": "PASS",
        },
        "manifest": {
            "filename": MANIFEST,
            "bytes": EXPECTED_MANIFEST_BYTES,
            "sha256": EXPECTED_MANIFEST_SHA256,
            "represented_rows": EXPECTED_MANIFEST_ROWS,
        },
        "package_validation": {
            "filename": VALIDATION,
            "bytes": EXPECTED_VALIDATION_BYTES,
            "sha256": EXPECTED_VALIDATION_SHA256,
            "status": "PASS",
            "errors": [],
        },
        "readback": readback_rows,
        **related,
    }
    if receipt_path is not None:
        receipt_path.parent.mkdir(parents=True, exist_ok=True)
        receipt_path.write_text(
            json.dumps(result, ensure_ascii=True, indent=2) + "\n",
            encoding="utf-8",
            newline="\n",
        )
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=["preflight", "stage", "publish"])
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--receipt", type=Path)
    parser.add_argument("--confirm-publish")
    args = parser.parse_args()
    session = base.make_session()
    token = base.find_token()
    root = args.root.resolve()
    if args.action == "preflight":
        result = preflight(session, token, root)
    elif args.action == "stage":
        result = stage(session, token, root)
    else:
        if args.confirm_publish != str(DRAFT_ID):
            raise RuntimeError(f"Publishing requires --confirm-publish {DRAFT_ID}")
        result = publish_and_readback(session, token, root, args.receipt)
    print(json.dumps(result, ensure_ascii=True, indent=2), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
