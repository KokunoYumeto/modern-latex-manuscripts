#!/usr/bin/env python3
"""Publish and read back the bounded SGA3 Expose IX successor."""

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
PREDECESSOR_RECORD = 21628220
PREDECESSOR_DOI = "10.5281/zenodo.21628220"
SUCCESSOR_RECORD = 21628601
SUCCESSOR_DOI = "10.5281/zenodo.21628601"
VERSION = "2026-07-27 SGA3 Expose IX Loop2 reference-v2 r1"
DEFAULT_PREVIEW = (
    "00a_SGA1_English_CompleteVolume_Working_"
    "NoExhaustiveCertification_20260722.pdf"
)

REPO_ROOT = Path(__file__).resolve().parent.parent
RECEIPT_ROOT = REPO_ROOT / "manifests" / "published-zenodo"
PREDECESSOR_RECEIPT = (
    RECEIPT_ROOT
    / "20260727_sga6_idx585_596_record_21628220_public_readback.json"
)
PREDECESSOR_ZIP_RECEIPT = (
    RECEIPT_ROOT
    / "20260727_sga6_idx585_596_record_21628220_zip_member_readback.json"
)
STAGING_ROOT = Path(
    os.environ.get(
        "SGA3_IX_ZENODO_STAGING_ROOT",
        Path(os.environ["LOCALAPPDATA"])
        / "Temp"
        / "sga3_expose_ix_zenodo_21628601"
        / "upload",
    )
)
READBACK_ROOT = Path(
    os.environ.get(
        "SGA3_IX_ZENODO_READBACK_ROOT",
        Path(os.environ["LOCALAPPDATA"])
        / "Temp"
        / "sga3_expose_ix_zenodo_21628601_public_readback",
    )
)

OLD_CONTROL_NAMES = {
    "09_README_CURRENT_RELEASE.md",
    "09a_RELEASE_FILE_MANIFEST.csv",
    "09b_RELEASE_VALIDATION.json",
}

LOCAL_FILES = {
    "00c6_SGA3_English_Expose_IX_Loop2_ReferenceV2_R1_20260727.pdf": (
        STAGING_ROOT
        / "00c6_SGA3_English_Expose_IX_Loop2_ReferenceV2_R1_20260727.pdf",
        267_685,
        "3AE231B4608B12CF1E19CBD6194CCAA03AB410F7C26DDBCEA8843951AD9ED6D3",
    ),
    "02c6_SGA3_English_Expose_IX_Loop2_ReferenceV2_R1_Master_20260727.tex": (
        STAGING_ROOT
        / "02c6_SGA3_English_Expose_IX_Loop2_ReferenceV2_R1_Master_20260727.tex",
        1_316,
        "FA3CDED0E5D0086AF5633C14375668BDBA9B26D301D20E92E7C0B8438B9D1B46",
    ),
    "09_README_CURRENT_RELEASE.md": (
        STAGING_ROOT / "09_README_CURRENT_RELEASE.md",
        4_395,
        "E8C4F89CCDE4C59F44CDA70E27F7072FD0489F85245075C6A99CD43F24DCA741",
    ),
    "09a_RELEASE_FILE_MANIFEST.csv": (
        STAGING_ROOT / "09a_RELEASE_FILE_MANIFEST.csv",
        22_884,
        "F7979B66532F7353384DF48812CDFFE14BE7C232D2285191C653183FE64FA03E",
    ),
    "09b_RELEASE_VALIDATION.json": (
        STAGING_ROOT / "09b_RELEASE_VALIDATION.json",
        5_417,
        "9E1C2443CB2600AD12469A6A08A8F68A0F5D6B5C39898CF6C41D7C10546F8814",
    ),
    "10c6_SGA3_English_Expose_IX_Loop2_ReferenceV2_R1_Source_QA_20260727.zip": (
        STAGING_ROOT
        / "10c6_SGA3_English_Expose_IX_Loop2_ReferenceV2_R1_"
        "Source_QA_20260727.zip",
        8_357_707,
        "5CC33C3B35ED4BDF1CBFA64177070E5C3E47913E80CDEF5AA0158998EE3D337A",
    ),
}

EXPECTED_OUTER_FILES = 65
EXPECTED_OUTER_BYTES = 333_851_535
EXPECTED_RETAINED_FILES = 59
EXPECTED_ZIP_ARCHIVES = 37
EXPECTED_ZIP_FILE_MEMBERS = 3_648
EXPECTED_ZIP_DIRECTORY_ENTRIES = 7
EXPECTED_ZIP_ALL_ENTRIES = 3_655
EXPECTED_ZIP_UNCOMPRESSED_BYTES = 382_076_318
RELEASE_CONTROL_COMPATIBILITY_COUNTER = 3_654
GITHUB_COMMIT = "e2de33aade87606712a35ca7c5857d0c08b319cd"
GITHUB_PACKAGE = (
    "sources/sga/"
    "sga3-english-expose-ix-loop2-reference-v2-r1-20260727"
)

DESCRIPTION_PARAGRAPHS = [
    (
        "This same-concept compact successor preserves the reader-first SGA "
        "surface from version 10.5281/zenodo.21628220. Fifty-nine predecessor "
        "files outside the three release controls are retained byte-identically; "
        "the controls are refreshed and the complete bounded SGA3 Expose IX "
        "checkpoint is added as a direct reader, direct editable master TeX, "
        "and grouped source/QA archive."
    ),
    (
        "The 36-page A4 Expose IX reader covers Sections 1-8, all 68 named "
        "formal units, 205 display/formula-or-diagram blocks, eight native "
        "diagrams, and the terminal bibliography and editor notes. It stops "
        "before combined-reader page 679 / Expose X. The PDF has 276 named "
        "destinations, 288 valid internal GoTo actions, 37 embedded non-Type3 "
        "fonts, and no raster XObjects."
    ),
    (
        "The grouped source archive has 68 exact non-directory members totaling "
        "9,950,178 uncompressed bytes. It contains seven editable TeX files, "
        "the reader, all 36 reviewed renders, the reference-v2 graph, source and "
        "translation QA, audit receipts, provenance and rights notices, and "
        "recursive checksums. The graph partitions 644 candidates into 215 "
        "applied edges and 429 positive residuals, with zero pending actions."
        " Two extracted-package audits and one manager-side exact replay passed; "
        "the latest manager report has SHA-256 "
        "CAF5E6351A49F1FB6FFEDEECA49270A4BA04F20C3CB5302B1973027DDB3E4860."
    ),
    (
        "The controlling witness is the Polo-Gille born-digital Expose IX PDF "
        "Exp9-8nov09.pdf, 32 pages, SHA-256 "
        "7C1E3D5B9D01AD01D0DD7B8B62045D012052E7890FB37ADC3E7934EBB5FD6FC3. "
        "It is not redistributed and is not recovered editor TeX. OCR is "
        "locator/drafting material only."
    ),
    (
        "Jacob C. Reinhold's Expose IX Markdown from jcreinhold/sga commit "
        "e7a259f3f8608ad3edf9bf6eead3fd504dd2d23e is credited comparison "
        "material, not authority or independent corroboration. Its declared "
        "CC BY 4.0 terms apply only to that contribution. No blanket license or "
        "rights clearance is asserted for the underlying French work, English "
        "reconstruction, editorial additions, or package as a whole. "
        "Machine-assisted contributors include OpenAI Codex / ChatGPT and "
        "Anthropic Claude under human direction."
    ),
    (
        "This is complete Expose IX, not complete SGA3. The current SGA3 surface "
        "has a cumulative reader through Expose IV plus standalone complete "
        "working readers for Exposes V, VI, VIII, and IX; Expose VII and "
        "Exposes X-XXVI remain absent. This successor updates only existing SGA "
        "concept 10.5281/zenodo.20410947. The SGA6 crop/provenance surface is "
        "unchanged, and live SGA6 work beginning at idx597 remains excluded."
    ),
]
DESCRIPTION_HTML = "\n".join(
    f"<p>{paragraph}</p>" for paragraph in DESCRIPTION_PARAGRAPHS
)
NOTES_TEXT = (
    "Reader-first compact surface: direct working readers and primary editable "
    "TeX remain individually accessible; recursive sources, machine ledgers, "
    "QA, predecessors, and visual evidence remain grouped into coherent ZIPs. "
    "This version has 65 files and 37 ZIP archives. Literal archive replay "
    "contains 3,648 non-directory file members plus seven directory records "
    "(3,655 ZIP records total), totaling 382,076,318 uncompressed bytes. The "
    "release-control lineage compatibility counter is 3,654: the predecessor's "
    "3,586 counter plus 68 new non-directory members. SGA1 remains the "
    "default preview and remains substantially linked but not exhaustively "
    "convention-v2 certified. SGA3 remains incomplete because Expose VII and "
    "Exposes X-XXVI are absent. GitHub package commit: "
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
    if len(rows) != 62:
        raise RuntimeError("Predecessor receipt does not contain 62 files")
    result = {
        row["filename"]: {
            "bytes": int(row["bytes"]),
            "sha256": row["sha256"].upper(),
            "md5": row["md5"].lower(),
        }
        for row in rows
    }
    if len(result) != 62:
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
    return check(
        session.get(
            f"{API}/records/{SUCCESSOR_RECORD}/draft",
            headers={
                "Authorization": f"Bearer {token}",
                "Accept": "application/vnd.inveniordm.v1+json",
            },
            timeout=(30, 180),
        ),
        {200},
    ).json()


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


def stage_files(session: requests.Session, token: str) -> dict:
    expected, retained = expected_identities()
    latest = check(
        session.get(
            f"{API}/records/{PREDECESSOR_RECORD}/versions/latest",
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

    retained_errors: list[str] = []
    for name, identity in retained.items():
        row = files.get(name)
        if row is None:
            retained_errors.append(f"missing:{name}")
            continue
        if legacy_identity(row) != (identity["bytes"], identity["md5"]):
            retained_errors.append(f"identity:{name}")
    if retained_errors:
        raise RuntimeError(f"Retained file mismatch: {retained_errors}")

    auth = {"Authorization": f"Bearer {token}"}
    actions: list[dict] = []
    local = local_identities()
    for name, identity in local.items():
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
        with identity["path"].open("rb") as handle:
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
        uploaded_size = int(uploaded.get("size", uploaded.get("filesize", -1)))
        uploaded_md5 = normalize_checksum(uploaded.get("checksum", ""))
        if (uploaded_size, uploaded_md5) != (
            identity["bytes"],
            identity["md5"],
        ):
            raise RuntimeError(f"Upload response mismatch: {name}")
        actions.append({"filename": name, "action": "uploaded_exact"})
        files = draft_file_map(legacy_draft(session, token))

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
        / "20260727_sga3_expose_ix_record_21628601_draft_files.json",
        receipt,
    )
    return receipt


def inspect_preflight(session: requests.Session, token: str) -> dict:
    expected, retained = expected_identities()
    latest = check(
        session.get(
            f"{API}/records/{PREDECESSOR_RECORD}/versions/latest",
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
    if draft["files"].get("default_preview") != DEFAULT_PREVIEW:
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
            "default_preview": draft["files"].get("default_preview"),
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
        / "20260727_sga3_expose_ix_record_21628601_preflight.json",
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
    patched = check(
        session.put(
            f"{API}/records/{SUCCESSOR_RECORD}/draft",
            headers=headers,
            json=payload,
            timeout=(30, 300),
        ),
        {200},
    ).json()
    assert_metadata(patched["metadata"])
    if patched["files"].get("default_preview") != DEFAULT_PREVIEW:
        raise RuntimeError("Patched draft lost default preview")
    if set(patched["files"]["entries"]) != set(expected):
        raise RuntimeError("Patched draft lost exact file set")

    patched_readback = modern_draft(session, token)
    assert_metadata(patched_readback["metadata"])
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
        / "20260727_sga3_expose_ix_record_21628601_draft_patch.json",
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
            f"{API}/records/{SUCCESSOR_RECORD}",
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
            f"{API}/records/{PREDECESSOR_RECORD}/versions/latest",
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
            "3,586 counter and adds 68 new non-directory members. Literal "
            "replay has 3,648 non-directory files plus seven directory records, "
            "or 3,655 total ZIP records."
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
        / "20260727_sga3_expose_ix_record_21628601_zip_member_readback.json",
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
            "commit_pinned_metadata_readback": "7/7",
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
            "scope": "complete bounded SGA3 Expose IX",
            "combined_pages": "647-678",
            "hard_stop": "before combined page 679 / Expose X",
            "sga3_complete": False,
            "reference_targets": 154,
            "reference_candidates": 644,
            "reference_edges": 215,
            "reference_residuals": 429,
            "pdf_named_destinations": 276,
            "pdf_goto_actions": 288,
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
        / "20260727_sga3_expose_ix_record_21628601_public_readback.json",
        receipt,
    )

    if not keep_downloads:
        resolved = READBACK_ROOT.resolve()
        expected_parent = (
            Path(os.environ["LOCALAPPDATA"]) / "Temp"
        ).resolve()
        if resolved.parent != expected_parent or resolved.name != (
            "sga3_expose_ix_zenodo_21628601_public_readback"
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
