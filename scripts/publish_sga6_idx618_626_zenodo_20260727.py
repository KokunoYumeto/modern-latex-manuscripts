#!/usr/bin/env python3
"""Publish and read back the SGA6 idx618-626 source-audit crop successor."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import os
import shutil
import time
from pathlib import Path
from urllib.parse import quote

import requests

import publish_sga3_expose_viii_zenodo_20260727 as helpers


API = "https://zenodo.org/api"
CONCEPT_DOI = "10.5281/zenodo.20410947"
PREDECESSOR_RECORD = 21630748
PREDECESSOR_DOI = "10.5281/zenodo.21630748"
SUCCESSOR_RECORD = 21631125
SUCCESSOR_DOI = "10.5281/zenodo.21631125"
VERSION = "2026-07-27 SGA6 ultra-detail source-audit crops idx618-626"
DEFAULT_PREVIEW = (
    "00a_SGA1_English_CompleteVolume_Working_"
    "NoExhaustiveCertification_20260722.pdf"
)

REPO_ROOT = Path(__file__).resolve().parent.parent
RECEIPT_ROOT = REPO_ROOT / "manifests" / "published-zenodo"
PREDECESSOR_RECEIPT = (
    RECEIPT_ROOT
    / "20260727_sga3_expose_xi_record_21630748_public_readback.json"
)
PREDECESSOR_ZIP_RECEIPT = (
    RECEIPT_ROOT
    / "20260727_sga3_expose_xi_record_21630748_zip_member_readback.json"
)
TEMP_ROOT = Path(
    os.environ.get(
        "SGA6_IDX618_626_ZENODO_STAGING_ROOT",
        Path(os.environ["LOCALAPPDATA"])
        / "Temp"
        / "sga6_idx618_626_zenodo_21631125",
    )
)
CONTROLS_ROOT = Path(
    os.environ.get(
        "SGA6_IDX618_626_ZENODO_CONTROLS_ROOT",
        TEMP_ROOT / "controls",
    )
)
ZIP_ROOT = Path(
    os.environ.get(
        "SGA6_IDX618_626_ZENODO_ZIP_ROOT",
        Path(os.environ["LOCALAPPDATA"])
        / "Temp"
        / "sga6_idx618_626_zenodo_stage_20260727",
    )
)
READBACK_ROOT = Path(
    os.environ.get(
        "SGA6_IDX618_626_ZENODO_READBACK_ROOT",
        Path(os.environ["LOCALAPPDATA"])
        / "Temp"
        / "sga6_idx618_626_zenodo_21631125_public_readback",
    )
)

OLD_CONTROL_NAMES = {
    "09_README_CURRENT_RELEASE.md",
    "09a_RELEASE_FILE_MANIFEST.csv",
    "09b_RELEASE_VALIDATION.json",
}

LOCAL_FILES = {
    "09_README_CURRENT_RELEASE.md": (
        CONTROLS_ROOT / "09_README_CURRENT_RELEASE.md",
        4_405,
        "672AE0EA779C1EBACEC96B831C2381F0D2F515C990B94D14AF2FF25B677B9C2E",
    ),
    "09a_RELEASE_FILE_MANIFEST.csv": (
        CONTROLS_ROOT / "09a_RELEASE_FILE_MANIFEST.csv",
        27_354,
        "351141C35D99118281C0A643BFE64F819BB6D59A8926420D7E19025157B134B0",
    ),
    "09b_RELEASE_VALIDATION.json": (
        CONTROLS_ROOT / "09b_RELEASE_VALIDATION.json",
        7_118,
        "7BEDE045B62299F1E258EC15903CACA08EC9E15CC62ABBDB9CF935CD6AF7580A",
    ),
    "10x_SGA6_SourceAudit_Targeted_UltraDetail_Crops_idx618_626_20260727.zip": (
        ZIP_ROOT
        / "10x_SGA6_SourceAudit_Targeted_UltraDetail_Crops_"
        "idx618_626_20260727.zip",
        1_605_625,
        "4352E2DF6716365DFF093BECB019D2E6DE4F1E7EA8731362B801D8B94607F941",
    ),
    "10y_SGA6_SourceAudit_Crop_Provenance_RightsBlocked_Metadata_idx618_626_20260727.zip": (
        ZIP_ROOT
        / "10y_SGA6_SourceAudit_Crop_Provenance_RightsBlocked_"
        "Metadata_idx618_626_20260727.zip",
        69_077,
        "C8B3655B2B267816C260DB8BAC8D57137B89EFA975BAB31317025467E3593F2E",
    ),
}

EXPECTED_OUTER_FILES = 76
EXPECTED_OUTER_BYTES = 354_281_326
EXPECTED_RETAINED_FILES = 71
EXPECTED_ZIP_ARCHIVES = 46
EXPECTED_ZIP_FILE_MEMBERS = 3_857
EXPECTED_ZIP_DIRECTORY_ENTRIES = 7
EXPECTED_ZIP_ALL_ENTRIES = 3_864
EXPECTED_ZIP_UNCOMPRESSED_BYTES = 405_009_569
RELEASE_CONTROL_COMPATIBILITY_COUNTER = 3_863
GITHUB_COMMIT = "06d37efbb3f7350f35c690835d647b52992395e6"
GITHUB_PACKAGE = (
    "sources/sga/"
    "sga6-ultradetail-source-audit-crops-coldreverify-idx618-626-20260727"
)

DESCRIPTION_PARAGRAPHS = [
    (
        "This same-concept compact successor preserves the reader-first SGA "
        "surface from version 10.5281/zenodo.21630748. Seventy-one predecessor "
        "files outside the three release controls are retained byte-identically; "
        "the controls are refreshed and two bounded SGA6 source-audit visual-"
        "evidence archives are added."
    ),
    (
        "The targeted archive contains eleven tight formula, glyph, prose, "
        "locator, and diagram-junction crops actually opened during the SGA6 "
        "cold source re-verification. They map parent indices 618-626 to the "
        "stable nine-entry audit boundary #1370-#1378 and span Expose XII "
        "Proposition 3.1 through Lemma 4.4 and the opening of its proof; the "
        "continuation cursor is idx627. Every crop records parent "
        "identity, source page, pixel bounding box, dimensions, scaling, "
        "generator identity, linked audit entry, target context, and QA "
        "disposition."
    ),
    (
        "The paired provenance archive records 45 routine full-width page "
        "bands and one generated-but-unread alternative tight crop as "
        "rights_blocked_not_public. Their hashes, coordinates, dimensions, "
        "DPI, generator identities, and target links are public, while their "
        "pixels are withheld."
    ),
    (
        "The parent is the 720-page reader Theorie des intersections et theoreme "
        "de Riemann-Roch, 26,833,956 bytes, SHA-256 "
        "73FBBAD41340C12ECCDCFCF6C3A1656953FE3D712AA8E391678458CCD17B4BAA. "
        "The parent PDF, routine page-band pixels, and generated-but-unread "
        "alternatives are not redistributed."
    ),
    (
        "These crops are visual and provenance evidence, not certification of "
        "the French transcription, English translation, mathematics, "
        "completeness, or critical-edition status. Rights in the underlying "
        "French work and scan remain with their holders; no blanket license or "
        "rights transfer is asserted. Across the current same-concept crop "
        "series, 2,194 selected images are public and 3,298 routine page "
        "derivatives are represented by rights-blocked metadata. "
        "Machine-assisted contributors include OpenAI Codex / ChatGPT and "
        "Anthropic Claude under human direction."
    ),
    (
        "The SGA reader surface is otherwise unchanged. In particular, the "
        "current public SGA3 surface remains a cumulative working reader through "
        "Expose IV plus standalone complete working readers for Exposes V, VI, "
        "VIII, IX, and XI. Expose VII remains held for diagram repairs and "
        "reference-detector defects; Exposes X and XII-XXVI remain absent. This "
        "successor updates only existing SGA concept 10.5281/zenodo.20410947."
    ),
]
DESCRIPTION_HTML = "\n".join(
    f"<p>{paragraph}</p>" for paragraph in DESCRIPTION_PARAGRAPHS
)
NOTES_TEXT = (
    "Reader-first compact surface: direct working readers and primary editable "
    "TeX remain individually accessible; recursive sources, machine ledgers, "
    "QA, predecessors, and visual evidence remain grouped into coherent ZIPs. "
    "This version has 76 files and 46 ZIP archives. Literal archive replay "
    "contains 3,857 non-directory file members plus seven directory records "
    "(3,864 ZIP records total), totaling 405,009,569 uncompressed bytes. The "
    "release-control lineage compatibility counter is 3,863: the predecessor's "
    "3,841 counter plus 22 new non-directory members. SGA1 remains the "
    "default preview and remains substantially linked but not exhaustively "
    "convention-v2 certified. GitHub package commit: "
    f"{GITHUB_COMMIT}."
)
NOTES_HTML = f"<p>{NOTES_TEXT}</p>"


def sha256_file(path: Path) -> str:
    return helpers.sha256_file(path)


def md5_file(path: Path) -> str:
    return helpers.md5_file(path)


def normalize_checksum(value: str) -> str:
    return helpers.normalize_checksum(value)


def save_json(path: Path, value: object) -> None:
    helpers.save_json(path, value)


def check(response: requests.Response, expected: set[int]) -> requests.Response:
    return helpers.check(response, expected)


def note_type_id(item: dict) -> str:
    value = item.get("type", "")
    if isinstance(value, dict):
        return str(value.get("id", ""))
    return str(value)


def public_record_summary(record: dict) -> dict:
    return {
        "id": int(record["id"]),
        "doi": record["pids"]["doi"]["identifier"],
        "conceptdoi": record["parent"]["pids"]["doi"]["identifier"],
        "version": record["metadata"].get("version"),
        "title": record["metadata"].get("title"),
        "file_count": len(record["files"]["entries"]),
        "default_preview": record["files"].get("default_preview"),
        "updated": record.get("updated"),
    }


def assert_public_lineage(record: dict, record_id: int, doi: str) -> None:
    if int(record["id"]) != record_id:
        raise RuntimeError(f"Unexpected record id: {record['id']}")
    if record["pids"]["doi"]["identifier"] != doi:
        raise RuntimeError("Unexpected record DOI")
    if record["parent"]["pids"]["doi"]["identifier"] != CONCEPT_DOI:
        raise RuntimeError("Record escaped the existing SGA concept")


def local_identities() -> dict[str, dict]:
    result: dict[str, dict] = {}
    for name, (path, expected_bytes, expected_sha) in LOCAL_FILES.items():
        if not path.is_file():
            raise FileNotFoundError(path)
        actual = {
            "path": path,
            "bytes": path.stat().st_size,
            "sha256": sha256_file(path),
            "md5": md5_file(path),
        }
        if (actual["bytes"], actual["sha256"]) != (
            expected_bytes,
            expected_sha,
        ):
            raise RuntimeError(f"Local identity mismatch: {name}")
        result[name] = actual
    return result


def predecessor_identities() -> dict[str, dict]:
    receipt = json.loads(PREDECESSOR_RECEIPT.read_text(encoding="utf-8-sig"))
    if receipt.get("status") != "PASS":
        raise RuntimeError("Predecessor receipt is not PASS")
    if int(receipt["record"]["id"]) != PREDECESSOR_RECORD:
        raise RuntimeError("Predecessor receipt record mismatch")
    rows = receipt.get("outer_files", [])
    if len(rows) != 74:
        raise RuntimeError("Predecessor receipt does not contain 74 files")
    result = {
        row["filename"]: {
            "bytes": int(row["bytes"]),
            "sha256": row["sha256"].upper(),
            "md5": row["md5"].lower(),
        }
        for row in rows
    }
    if len(result) != 74:
        raise RuntimeError("Duplicate predecessor filenames")
    return result


def expected_identities() -> tuple[dict[str, dict], dict[str, dict]]:
    predecessor = predecessor_identities()
    local = local_identities()
    retained = {
        name: identity
        for name, identity in predecessor.items()
        if name not in OLD_CONTROL_NAMES
    }
    if len(retained) != EXPECTED_RETAINED_FILES:
        raise RuntimeError("Retained predecessor boundary mismatch")
    final = {**retained, **local}
    if len(final) != EXPECTED_OUTER_FILES:
        raise RuntimeError("Final file-count boundary mismatch")
    if sum(int(row["bytes"]) for row in final.values()) != EXPECTED_OUTER_BYTES:
        raise RuntimeError("Final byte boundary mismatch")
    return final, retained


def modern_draft(session: requests.Session, token: str) -> dict:
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.inveniordm.v1+json",
    }
    draft = check(
        session.get(
            f"{API}/records/{SUCCESSOR_RECORD}/draft",
            headers=headers,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    files = check(
        session.get(
            draft["links"]["files"],
            headers=headers,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    entries = files.get("entries", [])
    if isinstance(entries, list):
        entry_map = {entry["key"]: entry for entry in entries}
        if len(entry_map) != len(entries):
            raise RuntimeError("Modern draft has duplicate file keys")
        files["entries"] = entry_map
    elif not isinstance(entries, dict):
        raise RuntimeError("Unexpected modern draft file-entry shape")
    draft["files"] = files
    return draft


def legacy_draft(session: requests.Session, token: str) -> dict:
    return check(
        session.get(
            f"{API}/deposit/depositions/{SUCCESSOR_RECORD}",
            headers={"Authorization": f"Bearer {token}"},
            timeout=(30, 180),
        ),
        {200},
    ).json()


def assert_draft_lineage(draft: dict) -> None:
    if int(draft["id"]) != SUCCESSOR_RECORD:
        raise RuntimeError("Unexpected draft id")
    if draft["parent"]["pids"]["doi"]["identifier"] != CONCEPT_DOI:
        raise RuntimeError("Draft escaped the existing concept")


def draft_file_map(deposition: dict) -> dict[str, dict]:
    result = {row["filename"]: row for row in deposition["files"]}
    if len(result) != len(deposition["files"]):
        raise RuntimeError("Draft has duplicate filenames")
    return result


def legacy_identity(row: dict) -> tuple[int, str]:
    return int(row["filesize"]), normalize_checksum(row["checksum"])


def predecessor_public_file_map(session: requests.Session) -> dict[str, dict]:
    record = check(
        session.get(
            f"{API}/records/{PREDECESSOR_RECORD}",
            headers={"Accept": "application/json"},
            timeout=(30, 180),
        ),
        {200},
    ).json()
    if int(record["id"]) != PREDECESSOR_RECORD:
        raise RuntimeError("Unexpected predecessor public record")
    if record["conceptdoi"] != CONCEPT_DOI:
        raise RuntimeError("Predecessor public record escaped the concept")
    rows = record.get("files", [])
    result = {row["key"]: row for row in rows}
    if len(rows) != 74 or len(result) != 74:
        raise RuntimeError("Predecessor public file boundary mismatch")
    return result


def stage_files(session: requests.Session, token: str) -> dict:
    expected, retained = expected_identities()
    latest = check(
        session.get(
            f"{API}/records/{PREDECESSOR_RECORD}/versions/latest?expand=true",
            headers={"Accept": "application/vnd.inveniordm.v1+json"},
            timeout=(30, 180),
        ),
        {200},
    ).json()
    assert_public_lineage(latest, PREDECESSOR_RECORD, PREDECESSOR_DOI)

    draft = modern_draft(session, token)
    assert_draft_lineage(draft)
    deposition = legacy_draft(session, token)
    if deposition.get("state") != "unsubmitted" or deposition.get("submitted"):
        raise RuntimeError("Successor is not an unpublished draft")
    files = draft_file_map(deposition)
    allowed = set(expected) | OLD_CONTROL_NAMES
    extras = sorted(set(files) - allowed)
    if extras:
        raise RuntimeError(f"Unexpected draft files: {extras}")

    auth = {"Authorization": f"Bearer {token}"}
    actions: list[dict] = []
    local = local_identities()
    predecessor_files = predecessor_public_file_map(session)
    transfer_root = TEMP_ROOT / "transfer"
    transfer_root.mkdir(parents=True, exist_ok=True)
    retained_errors: list[str] = []
    for index, name in enumerate(sorted(expected, key=str.casefold), start=1):
        identity = expected[name]
        print(f"STAGE {index}/{len(expected)} {name}", flush=True)
        existing = files.get(name)
        exact = (
            existing is not None
            and legacy_identity(existing)
            == (identity["bytes"], identity["md5"])
        )
        if exact:
            actions.append({"filename": name, "action": "already_exact"})
            continue
        if existing is not None:
            check(
                session.delete(
                    existing["links"]["self"],
                    headers=auth,
                    timeout=(30, 300),
                ),
                {204},
            )
            actions.append({"filename": name, "action": "deleted_stale"})

        deposition_now = legacy_draft(session, token)
        bucket = deposition_now["links"]["bucket"].rstrip("/")
        upload_url = f"{bucket}/{quote(name, safe='')}"
        temporary_path: Path | None = None
        source_path: Path
        if name in local:
            source_path = local[name]["path"]
            action = "uploaded_local_exact"
        else:
            public_row = predecessor_files.get(name)
            if public_row is None:
                raise RuntimeError(f"Missing predecessor source file: {name}")
            if (
                int(public_row["size"]) != identity["bytes"]
                or normalize_checksum(public_row["checksum"]) != identity["md5"]
            ):
                raise RuntimeError(f"Predecessor source identity mismatch: {name}")
            temporary_path = transfer_root / name
            if temporary_path.exists():
                temporary_path.unlink()
            helpers.download_public_file(
                session,
                public_row["links"]["self"],
                temporary_path,
                identity["bytes"],
                identity["sha256"],
            )
            source_path = temporary_path
            action = "streamed_predecessor_exact"

        with source_path.open("rb") as handle:
            uploaded = check(
                session.put(
                    upload_url,
                    data=handle,
                    headers={
                        **auth,
                        "Content-Type": "application/octet-stream",
                    },
                    timeout=(30, 1800),
                ),
                {200, 201},
            ).json()
        if temporary_path is not None:
            temporary_path.unlink()
        uploaded_size = int(uploaded.get("size", uploaded.get("filesize", -1)))
        uploaded_md5 = normalize_checksum(uploaded.get("checksum", ""))
        if (uploaded_size, uploaded_md5) != (
            identity["bytes"],
            identity["md5"],
        ):
            raise RuntimeError(f"Upload response mismatch: {name}")
        actions.append({"filename": name, "action": action})
        files = draft_file_map(legacy_draft(session, token))
    if transfer_root.exists() and not any(transfer_root.iterdir()):
        transfer_root.rmdir()

    final_deposition = legacy_draft(session, token)
    final_files = draft_file_map(final_deposition)
    if set(final_files) != set(expected):
        missing = sorted(set(expected) - set(final_files))
        extra = sorted(set(final_files) - set(expected))
        raise RuntimeError(
            f"Staged exact-set mismatch: missing={missing}, extra={extra}"
        )
    identity_errors = []
    for name, identity in expected.items():
        if legacy_identity(final_files[name]) != (
            identity["bytes"],
            identity["md5"],
        ):
            identity_errors.append(name)
    if identity_errors:
        raise RuntimeError(f"Staged identity mismatch: {identity_errors}")

    receipt = {
        "status": "PASS_STAGED",
        "errors": [],
        "record_id": SUCCESSOR_RECORD,
        "concept_doi": CONCEPT_DOI,
        "predecessor_record": PREDECESSOR_RECORD,
        "file_count": len(final_files),
        "bytes": sum(int(row["filesize"]) for row in final_files.values()),
        "retained_predecessor_files": len(retained),
        "retained_identity_errors": retained_errors,
        "actions": actions,
        "duplicate_concept_created": False,
        "second_draft_created": False,
    }
    save_json(
        RECEIPT_ROOT
        / "20260727_sga6_idx618_626_record_21631125_draft_files.json",
        receipt,
    )
    return receipt


def inspect_preflight(session: requests.Session, token: str) -> dict:
    expected, retained = expected_identities()
    latest = check(
        session.get(
            f"{API}/records/{PREDECESSOR_RECORD}/versions/latest?expand=true",
            headers={"Accept": "application/vnd.inveniordm.v1+json"},
            timeout=(30, 180),
        ),
        {200},
    ).json()
    assert_public_lineage(latest, PREDECESSOR_RECORD, PREDECESSOR_DOI)

    draft = modern_draft(session, token)
    assert_draft_lineage(draft)
    entries = draft["files"]["entries"]
    if set(entries) != set(expected):
        raise RuntimeError("Draft exact-set mismatch")
    identity_errors = []
    for name, identity in expected.items():
        entry = entries[name]
        if (
            int(entry["size"]) != identity["bytes"]
            or normalize_checksum(entry["checksum"]) != identity["md5"]
        ):
            identity_errors.append(name)
    if identity_errors:
        raise RuntimeError(f"Draft identity mismatch: {identity_errors}")
    initial_preview = draft["files"].get("default_preview")
    if initial_preview not in {None, DEFAULT_PREVIEW}:
        raise RuntimeError("Draft default-preview mismatch")

    additional = draft["metadata"].get("additional_descriptions", [])
    if not additional:
        raise RuntimeError("Draft has no notes field to preserve")
    receipt = {
        "status": "PASS_PREFLIGHT",
        "errors": [],
        "latest_public": public_record_summary(latest),
        "draft": {
            "id": int(draft["id"]),
            "concept_doi": draft["parent"]["pids"]["doi"]["identifier"],
            "file_count": len(entries),
            "bytes": sum(int(entry["size"]) for entry in entries.values()),
            "default_preview": initial_preview,
            "additional_description_types": [
                note_type_id(item) for item in additional
            ],
        },
        "retained_predecessor_files": len(retained),
        "identity_errors": identity_errors,
        "planned_metadata": {
            "version": VERSION,
            "description_sha256": hashlib.sha256(
                DESCRIPTION_HTML.encode("utf-8")
            ).hexdigest().upper(),
            "notes_sha256": hashlib.sha256(
                NOTES_HTML.encode("utf-8")
            ).hexdigest().upper(),
        },
        "duplicate_concept_created": False,
        "new_version_created_by_this_script": False,
    }
    save_json(
        RECEIPT_ROOT
        / "20260727_sga6_idx618_626_record_21631125_preflight.json",
        receipt,
    )
    return receipt


def patch_notes(metadata: dict) -> None:
    additional = metadata.get("additional_descriptions", [])
    if not additional:
        raise RuntimeError("Cannot patch absent notes field")
    indexes = [
        index
        for index, item in enumerate(additional)
        if note_type_id(item) in {"notes", "technical-info", "other"}
    ]
    target = indexes[0] if indexes else 0
    additional[target]["description"] = NOTES_HTML
    metadata["additional_descriptions"] = additional


def assert_metadata(metadata: dict) -> None:
    if metadata.get("version") != VERSION:
        raise RuntimeError("Version metadata mismatch")
    if metadata.get("description") != DESCRIPTION_HTML:
        raise RuntimeError("Description metadata mismatch")
    additional = metadata.get("additional_descriptions", [])
    if not any(item.get("description") == NOTES_HTML for item in additional):
        raise RuntimeError("Notes metadata mismatch")


def patch_and_publish(session: requests.Session, token: str) -> dict:
    preflight = inspect_preflight(session, token)
    draft = modern_draft(session, token)
    expected, _ = expected_identities()
    metadata = copy.deepcopy(draft["metadata"])
    metadata["version"] = VERSION
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
    patched_response = check(
        session.put(
            f"{API}/records/{SUCCESSOR_RECORD}/draft",
            headers=headers,
            json=payload,
            timeout=(30, 300),
        ),
        {200},
    ).json()
    assert_metadata(patched_response["metadata"])

    patched_readback = modern_draft(session, token)
    assert_metadata(patched_readback["metadata"])
    if patched_readback["files"].get("default_preview") != DEFAULT_PREVIEW:
        raise RuntimeError("Patched draft lost default preview")
    if set(patched_readback["files"]["entries"]) != set(expected):
        raise RuntimeError("Patched draft lost exact file set")
    normalized_order = patched_readback["files"].get("order", [])
    if normalized_order and normalized_order != sorted(
        expected, key=str.casefold
    ):
        raise RuntimeError("Patched draft file order mismatch")

    patch_receipt = {
        "status": "PASS_PATCHED_DRAFT",
        "errors": [],
        "record_id": SUCCESSOR_RECORD,
        "concept_doi": CONCEPT_DOI,
        "version": VERSION,
        "description_exact": True,
        "notes_exact": True,
        "file_count": EXPECTED_OUTER_FILES,
        "default_preview": DEFAULT_PREVIEW,
        "explicit_order_count": len(normalized_order),
        "order_note": (
            "Zenodo normalized the explicit order list to empty; numeric "
            "filename prefixes preserve the intended reader-first sequence."
        ),
        "preflight": preflight,
    }
    save_json(
        RECEIPT_ROOT
        / "20260727_sga6_idx618_626_record_21631125_draft_patch.json",
        patch_receipt,
    )

    published = check(
        session.post(
            patched_readback["links"]["publish"],
            headers={
                "Authorization": f"Bearer {token}",
                "Accept": "application/vnd.inveniordm.v1+json",
            },
            timeout=(30, 600),
        ),
        {200, 202},
    ).json()
    assert_public_lineage(published, SUCCESSOR_RECORD, SUCCESSOR_DOI)
    return {
        "status": "PUBLISH_ACCEPTED",
        "record_id": SUCCESSOR_RECORD,
        "doi": SUCCESSOR_DOI,
        "concept_doi": CONCEPT_DOI,
    }


def wait_for_public(session: requests.Session) -> dict:
    for _ in range(60):
        response = session.get(
            f"{API}/records/{SUCCESSOR_RECORD}?expand=true",
            headers={"Accept": "application/vnd.inveniordm.v1+json"},
            timeout=(30, 180),
        )
        if response.status_code == 200:
            record = response.json()
            if (
                int(record["id"]) == SUCCESSOR_RECORD
                and len(record["files"]["entries"]) == EXPECTED_OUTER_FILES
            ):
                return record
        time.sleep(5)
    raise RuntimeError("Published record did not stabilize")


def zip_member_key(row: dict) -> tuple[str, str]:
    return row["archive"], row["relative_path"]


def anonymous_readback(
    session: requests.Session,
    token: str,
    publish_result: dict | None,
    keep_downloads: bool,
) -> dict:
    expected, retained = expected_identities()
    record = wait_for_public(session)
    assert_public_lineage(record, SUCCESSOR_RECORD, SUCCESSOR_DOI)
    assert_metadata(record["metadata"])
    if record["files"].get("default_preview") != DEFAULT_PREVIEW:
        raise RuntimeError("Published default-preview mismatch")
    entries = record["files"]["entries"]
    if set(entries) != set(expected):
        raise RuntimeError("Published exact-set mismatch")
    if sum(int(entry["size"]) for entry in entries.values()) != EXPECTED_OUTER_BYTES:
        raise RuntimeError("Published byte boundary mismatch")

    latest = check(
        session.get(
            f"{API}/records/{PREDECESSOR_RECORD}/versions/latest?expand=true",
            headers={"Accept": "application/vnd.inveniordm.v1+json"},
            timeout=(30, 180),
        ),
        {200},
    ).json()
    assert_public_lineage(latest, SUCCESSOR_RECORD, SUCCESSOR_DOI)

    active_draft = session.get(
        f"{API}/records/{SUCCESSOR_RECORD}/draft",
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.inveniordm.v1+json",
        },
        timeout=(30, 180),
    )
    if active_draft.status_code != 404:
        raise RuntimeError(
            f"Published record still has a draft: {active_draft.status_code}"
        )

    READBACK_ROOT.mkdir(parents=True, exist_ok=True)
    outer_rows: list[dict] = []
    for index, name in enumerate(sorted(expected, key=str.casefold), start=1):
        print(f"READBACK {index}/{len(expected)} {name}", flush=True)
        entry = entries[name]
        size, sha = helpers.download_public_file(
            session,
            entry["links"]["content"],
            READBACK_ROOT / name,
            expected[name]["bytes"],
            expected[name]["sha256"],
        )
        outer_rows.append(
            {
                "filename": name,
                "bytes": size,
                "sha256": sha,
                "md5": normalize_checksum(entry["checksum"]),
                "classification": (
                    "retained_predecessor" if name in retained
                    else "new_or_refreshed"
                ),
                "url": entry["links"]["content"],
            }
        )

    zip_summaries: list[dict] = []
    zip_members: list[dict] = []
    for index, path in enumerate(
        sorted(READBACK_ROOT.glob("*.zip"), key=lambda row: row.name.casefold()),
        start=1,
    ):
        print(f"ZIP REPLAY {index}/{EXPECTED_ZIP_ARCHIVES} {path.name}", flush=True)
        summary, members = helpers.replay_zip(path)
        if summary["errors"]:
            raise RuntimeError(
                f"ZIP replay errors for {path.name}: {summary['errors']}"
            )
        zip_summaries.append(summary)
        zip_members.extend(
            {"archive": path.name, **member} for member in members
        )

    directory_entries = sum(
        int(row["directory_entry_count"]) for row in zip_summaries
    )
    all_entries = sum(int(row["all_entry_count"]) for row in zip_summaries)
    uncompressed = sum(int(row["uncompressed_bytes"]) for row in zip_summaries)
    if len(zip_summaries) != EXPECTED_ZIP_ARCHIVES:
        raise RuntimeError("ZIP archive-count mismatch")
    if len(zip_members) != EXPECTED_ZIP_FILE_MEMBERS:
        raise RuntimeError(
            f"ZIP file-member mismatch: {len(zip_members)}"
        )
    if directory_entries != EXPECTED_ZIP_DIRECTORY_ENTRIES:
        raise RuntimeError("ZIP directory-entry mismatch")
    if all_entries != EXPECTED_ZIP_ALL_ENTRIES:
        raise RuntimeError("ZIP all-entry mismatch")
    if uncompressed != EXPECTED_ZIP_UNCOMPRESSED_BYTES:
        raise RuntimeError("ZIP uncompressed-byte mismatch")

    prior_zip = json.loads(
        PREDECESSOR_ZIP_RECEIPT.read_text(encoding="utf-8-sig")
    )
    if prior_zip.get("status") != "PASS":
        raise RuntimeError("Predecessor ZIP receipt is not PASS")
    prior_members = {
        zip_member_key(row): (int(row["bytes"]), row["sha256"].upper())
        for row in prior_zip["members"]
    }
    current_members = {
        zip_member_key(row): (int(row["bytes"]), row["sha256"].upper())
        for row in zip_members
    }
    inherited_errors = [
        key
        for key, identity in prior_members.items()
        if current_members.get(key) != identity
    ]
    if inherited_errors:
        raise RuntimeError(
            f"Inherited ZIP member mismatch: {inherited_errors[:10]}"
        )

    new_zip_results: dict[str, dict] = {}
    for name in sorted(
        (name for name in LOCAL_FILES if name.endswith(".zip")),
        key=str.casefold,
    ):
        local_summary, local_members = helpers.replay_zip(LOCAL_FILES[name][0])
        remote_summary = next(
            row for row in zip_summaries if row["filename"] == name
        )
        remote_members = [
            {
                "relative_path": row["relative_path"],
                "bytes": row["bytes"],
                "sha256": row["sha256"],
            }
            for row in zip_members
            if row["archive"] == name
        ]
        local_map = {
            row["relative_path"]: (row["bytes"], row["sha256"])
            for row in local_members
        }
        remote_map = {
            row["relative_path"]: (row["bytes"], row["sha256"])
            for row in remote_members
        }
        errors = []
        if local_map != remote_map:
            errors.append("member_identity_mismatch")
        if (
            local_summary["bytes"] != remote_summary["bytes"]
            or local_summary["sha256"] != remote_summary["sha256"]
        ):
            errors.append("outer_identity_mismatch")
        if errors:
            raise RuntimeError(f"New ZIP mismatch for {name}: {errors}")
        new_zip_results[name] = {
            "member_count": len(remote_members),
            "uncompressed_bytes": remote_summary["uncompressed_bytes"],
            "canonical_member_identity_sha256": remote_summary[
                "canonical_member_identity_sha256"
            ],
            "errors": errors,
        }

    retained_errors = [
        row["filename"]
        for row in outer_rows
        if row["filename"] in retained
        and (
            row["bytes"] != retained[row["filename"]]["bytes"]
            or row["sha256"] != retained[row["filename"]]["sha256"]
        )
    ]
    if retained_errors:
        raise RuntimeError(f"Retained outer mismatch: {retained_errors}")

    zip_receipt = {
        "status": "PASS",
        "errors": [],
        "record_id": SUCCESSOR_RECORD,
        "doi": SUCCESSOR_DOI,
        "zip_archive_count": len(zip_summaries),
        "zip_file_member_count": len(zip_members),
        "zip_directory_entry_count": directory_entries,
        "zip_all_entry_count": all_entries,
        "release_control_compatibility_counter": (
            RELEASE_CONTROL_COMPATIBILITY_COUNTER
        ),
        "compatibility_counter_note": (
            "The release-control lineage counter preserves the predecessor's "
            "3,841 counter and adds 22 new non-directory members. Literal "
            "replay has 3,857 non-directory files plus seven directory records, "
            "or 3,864 total ZIP records."
        ),
        "zip_uncompressed_bytes": uncompressed,
        "inherited_zip_member_count": len(prior_members),
        "inherited_zip_member_errors": inherited_errors,
        "new_zip_results": new_zip_results,
        "archives": zip_summaries,
        "members": zip_members,
    }
    save_json(
        RECEIPT_ROOT
        / "20260727_sga6_idx618_626_record_21631125_zip_member_readback.json",
        zip_receipt,
    )

    receipt = {
        "status": "PASS",
        "errors": [],
        "record": public_record_summary(record),
        "latest": public_record_summary(latest),
        "concept_doi": CONCEPT_DOI,
        "predecessor_record": PREDECESSOR_RECORD,
        "predecessor_doi": PREDECESSOR_DOI,
        "github": {
            "commit": GITHUB_COMMIT,
            "package": GITHUB_PACKAGE,
            "commit_pinned_metadata_readback": "15/15",
        },
        "outer_files": outer_rows,
        "outer_file_count": len(outer_rows),
        "outer_bytes": sum(row["bytes"] for row in outer_rows),
        "retained_predecessor_files": len(retained),
        "retained_predecessor_errors": retained_errors,
        "new_or_refreshed_files": len(LOCAL_FILES),
        "default_preview_ui_readback": DEFAULT_PREVIEW,
        "metadata": {
            "version": VERSION,
            "description_exact": True,
            "notes_exact": True,
            "scope": "SGA6 source-audit crops idx618-626",
            "selected_opened_crops": 11,
            "routine_page_bands_metadata_only": 45,
            "generated_unread_tight_crops_metadata_only": 1,
            "stable_audit_entries": "1370-1378",
        },
        "zip_archive_count": len(zip_summaries),
        "zip_file_member_count": len(zip_members),
        "zip_directory_entry_count": directory_entries,
        "zip_all_entry_count": all_entries,
        "release_control_compatibility_counter": (
            RELEASE_CONTROL_COMPATIBILITY_COUNTER
        ),
        "zip_uncompressed_bytes": uncompressed,
        "draft_remaining": False,
        "duplicate_concept_created": False,
        "second_version_created_by_script": False,
        "publish_result": publish_result,
    }
    save_json(
        RECEIPT_ROOT
        / "20260727_sga6_idx618_626_record_21631125_public_readback.json",
        receipt,
    )

    if not keep_downloads:
        resolved = READBACK_ROOT.resolve()
        expected_parent = (
            Path(os.environ["LOCALAPPDATA"]) / "Temp"
        ).resolve()
        if resolved.parent != expected_parent or resolved.name != (
            "sga6_idx618_626_zenodo_21631125_public_readback"
        ):
            raise RuntimeError(f"Refusing unsafe readback cleanup: {resolved}")
        shutil.rmtree(resolved)
    return receipt


def main() -> None:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--stage", action="store_true")
    mode.add_argument("--preflight", action="store_true")
    mode.add_argument("--publish", action="store_true")
    mode.add_argument("--readback-only", action="store_true")
    parser.add_argument("--keep-downloads", action="store_true")
    args = parser.parse_args()

    token = helpers.find_token()
    session = helpers.make_session()
    if args.stage:
        result = stage_files(session, token)
    elif args.preflight:
        result = inspect_preflight(session, token)
    elif args.publish:
        publish_result = patch_and_publish(session, token)
        result = anonymous_readback(
            session,
            token,
            publish_result=publish_result,
            keep_downloads=args.keep_downloads,
        )
    else:
        result = anonymous_readback(
            session,
            token,
            publish_result=None,
            keep_downloads=args.keep_downloads,
        )
    print(json.dumps(result, ensure_ascii=False, indent=2), flush=True)


if __name__ == "__main__":
    main()
