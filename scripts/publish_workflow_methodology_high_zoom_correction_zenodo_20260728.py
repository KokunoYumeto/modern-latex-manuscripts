#!/usr/bin/env python3
"""Publish and read back the native-diagram methodology correction."""

from __future__ import annotations

import copy
import csv
import hashlib
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
CONCEPT_DOI = "10.5281/zenodo.20461174"
PREDECESSOR_RECORD = 21633426
PREDECESSOR_DOI = "10.5281/zenodo.21633426"
PUBLICATION_DATE = "2026-07-28"
VERSION = (
    "2026-07-28 native-TeX SGA3 diagram-fidelity correction"
)
DEFAULT_PREVIEW = (
    "00_AI_Run_Modern_LaTeX_Manuscript_Workflow_Current_20260728.pdf"
)
RETAINED_ADDENDA = (
    "01_Workflow_Docs_Addenda_Scripts_and_Cleanup_Log_20260706.zip"
)
MANIFEST = "98_WORKFLOW_RELEASE_MANIFEST.csv"
VALIDATION = "99_WORKFLOW_RELEASE_VALIDATION.json"
SOURCE_PACKET = "03_AI_Run_Modern_LaTeX_Workflow_20260728_Source_Packet.zip"
GITHUB_COMMIT = "fb697af58c15d95f3c3dd7d5f7c7e05e463fe39b"
GITHUB_PACKAGE = (
    "sources/workflow/ai-run-modern-latex-workflow-20260728"
)

REPO_ROOT = Path(__file__).resolve().parent.parent
PACKAGE_ROOT = (
    REPO_ROOT
    / "sources"
    / "workflow"
    / "ai-run-modern-latex-workflow-20260728"
)
RECEIPT_ROOT = REPO_ROOT / "manifests" / "published-zenodo"
GITHUB_RECEIPT = (
    REPO_ROOT
    / "manifests"
    / "published-github"
    / "20260728_workflow_methodology_commit_fb697af58_public_readback.json"
)
TOKEN_LOG = Path(
    os.environ.get(
        "ZENODO_TOKEN_LOG",
        Path.home() / ".codex" / ".sandbox" / "sandbox.log",
    )
)
DRAFT_STATE = (
    RECEIPT_ROOT
    / "20260728_workflow_methodology_high_zoom_zenodo_draft_state.json"
)
READBACK_ROOT = Path(
    os.environ.get(
        "WORKFLOW_METHODOLOGY_ZENODO_READBACK_ROOT",
        Path(os.environ["LOCALAPPDATA"])
        / "Temp"
        / "workflow_methodology_high_zoom_zenodo_public_readback",
    )
)

PREDECESSOR_FILES = {
    "00_AI_Run_Modern_LaTeX_Manuscript_Workflow_Current_20260728.md": (
        18_987,
        "bc0fd2ae0bfd986a2b2d8e2628eabad1",
    ),
    "00_AI_Run_Modern_LaTeX_Manuscript_Workflow_Current_20260728.pdf": (
        57_365,
        "8927b0b6098d5ef9fe3499bafacfb44f",
    ),
    RETAINED_ADDENDA: (
        209_743,
        "91cf57e6f0fc60116e5115cca91094e7",
    ),
    "01_CLAUDE_DIAGRAM_COLD_REVERIFY_METHOD_20260728.md": (
        8_535,
        "a779998bea21fd520539566ef207b37d",
    ),
    "02_SGA_TRANSLATION_RESOURCE_EFFICIENCY_INCIDENT_NOTE_20260728.md": (
        5_015,
        "90abf7d4293b76a4b88a01e29371c3c3",
    ),
    "03_AI_Run_Modern_LaTeX_Workflow_20260728_Source_Packet.zip": (
        73_392,
        "c69baa451a33e96b8a885d19aade78f6",
    ),
    "98_WORKFLOW_RELEASE_MANIFEST.csv": (
        1_594,
        "605bd97ae3b4c7d9e73390a992290158",
    ),
    "99_WORKFLOW_PUBLIC_STATUS_20260728.md": (
        3_010,
        "b3edf1642e034150a321bc45fbf417b7",
    ),
    "99_WORKFLOW_RELEASE_VALIDATION.json": (
        2_079,
        "a0d5818160367d117810a0bec6e8a4c7",
    ),
}
REPLACED_FILES: set[str] = set()

EXPECTED_FINAL_FILES = 10
EXPECTED_RETAINED_FILES = 3
EXPECTED_ZIP_ARCHIVES = 2
EXPECTED_ZIP_FILE_MEMBERS = 28
EXPECTED_ZIP_DIRECTORY_ENTRIES = 0
EXPECTED_ZIP_UNCOMPRESSED_BYTES = 836_257

DESCRIPTION_PARAGRAPHS = [
    (
        "This same-concept successor publishes the controlling July 28 "
        "native-diagram correction to the AI-run Modern LaTeX Manuscript "
        "Workflow. The public surface keeps the corrected seven-page A4 PDF "
        "and Markdown directly accessible, co-publishes the exact Claude "
        "cold-reverify method, the resource-efficiency incident note, and the "
        "diagram-fidelity correction, groups the current files into one "
        "source packet, and retains the July 6 addenda/scripts ZIP "
        "byte-identically."
    ),
    (
        "Top-level sessions own disjoint whole-expose ranges and retain "
        "responsibility for mathematical translation, transcription "
        "adjudication, diagram reconstruction, reference semantics, and visual "
        "PASS decisions. Subagents are limited to bounded mechanical support "
        "or preliminary drafting. Loop 1 advances canonical text and equations; "
        "Loop 2 handles native diagrams and exhaustive reference/release work "
        "without blocking disjoint Loop-1 production."
    ),
    (
        "For scan-controlled work, the controlling source image decides. Page "
        "mapping uses printed page, running header, and folio. The method calls "
        "for five overlapping 2400-dpi text bands per page, 300-dpi page "
        "context, about 5000-dpi default diagram comparison, targeted "
        "9000-dpi crops for real ambiguities, and node-by-node and "
        "edge-by-edge review. Existing 600/1200-dpi evidence remains valid "
        "history and context; only 300-dpi-only approvals and independently "
        "identified material defects are reopened."
    ),
    (
        "Every diagram delivered in a new SGA3 reader or payload is native "
        "editable TeX. Raster crops remain private authority witnesses and "
        "are excluded from new public readers and payloads. Final successors "
        "bind disjoint top-level-session ownership and a lead-signed exact "
        "high-zoom review. Prior public checkpoints remain immutable history; "
        "material defects receive additive no-overwrite successors."
    ),
    (
        "The complete user-supplied OCR is a read-only locator and drafting "
        "witness. It must not be generated, rerun, re-extracted, or delegated. "
        "SGA1 and SGA2 are not blanket-retranscribed from images when their "
        "completed mathematical TeX transcription is already controlling. "
        "Source images are opened for genuine ambiguities, diagrams, or an "
        "explicit source-control question."
    ),
    (
        "The incident note records avoidable duplicate visual checks, repeated "
        "OCR/transcription activity, agent audit cascades, and repeated builds "
        "or manifests that did not advance the mathematical corpus. Its "
        "emissions figures are transparent scenario calculations, not metered "
        "OpenAI telemetry. Multi-ton coal-equivalent outcomes are conditional "
        "on the stated high-overhead, several-hundred-million-token assumptions; "
        "lifecycle, labor, infrastructure, and opportunity costs remain "
        "unquantified."
    ),
    (
        "This is a professional methodology and accountability publication, "
        "not a manuscript certification or new license grant. Documentation "
        "and exact release identities support production and preservation; "
        "they do not replace translation, transcription, diagram "
        "reconstruction, or public custody."
    ),
]
DESCRIPTION_HTML = "\n".join(f"<p>{value}</p>" for value in DESCRIPTION_PARAGRAPHS)
NOTES_HTML = (
    "<p>Compact ten-file workflow surface. The seven-page A4 PDF is the "
    "default preview. The source packet has seven exact members; the "
    "historical July 6 addenda/scripts ZIP is retained byte-identically. "
    "GitHub package commit: "
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


def save_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, ensure_ascii=True, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
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
    return entries


def legacy_file_map(deposition: dict) -> dict[str, dict]:
    result = {row["filename"]: row for row in deposition["files"]}
    if len(result) != len(deposition["files"]):
        raise RuntimeError("Draft contains duplicate filenames")
    return result


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
            "Workflow concept head moved; refusing a parallel successor"
        )


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
    ):
        raise RuntimeError("Workflow predecessor lineage mismatch")
    entries = entries_map(record)
    if set(entries) != set(PREDECESSOR_FILES):
        raise RuntimeError("Workflow predecessor file surface changed")
    for name, (size, md5) in PREDECESSOR_FILES.items():
        row = entries[name]
        if (
            int(row["size"]),
            normalize_checksum(row["checksum"]),
        ) != (size, md5):
            raise RuntimeError(f"Workflow predecessor identity changed: {name}")
    return record


def expected_identities(predecessor: dict) -> tuple[dict, dict]:
    if not GITHUB_RECEIPT.is_file():
        raise FileNotFoundError(GITHUB_RECEIPT)
    github = json.loads(GITHUB_RECEIPT.read_text(encoding="utf-8"))
    if (
        github.get("status") != "PASS"
        or github.get("commit") != GITHUB_COMMIT
        or int(github.get("file_count", -1)) != EXPECTED_FINAL_FILES
    ):
        raise RuntimeError("GitHub package readback receipt is not controlling")

    manifest_path = PACKAGE_ROOT / MANIFEST
    with manifest_path.open(
        "r", encoding="utf-8-sig", newline=""
    ) as handle:
        rows = list(csv.DictReader(handle))
    if len(rows) != 8:
        raise RuntimeError("Expected eight outer-manifest rows")
    expected = {}
    for row in rows:
        name = row["filename"]
        expected[name] = {
            "bytes": int(row["bytes"]),
            "sha256": row["sha256"].upper(),
        }
    for name in (MANIFEST, VALIDATION):
        path = PACKAGE_ROOT / name
        expected[name] = {
            "bytes": path.stat().st_size,
            "sha256": sha256_file(path),
        }
    if len(expected) != EXPECTED_FINAL_FILES:
        raise RuntimeError("Expected ten final workflow files")

    local = {}
    for name, wanted in expected.items():
        path = PACKAGE_ROOT / name
        observed = {
            "path": path,
            "bytes": path.stat().st_size,
            "sha256": sha256_file(path),
            "md5": md5_file(path),
        }
        if (
            observed["bytes"],
            observed["sha256"],
        ) != (
            wanted["bytes"],
            wanted["sha256"],
        ):
            raise RuntimeError(f"Local package identity mismatch: {name}")
        if name != RETAINED_ADDENDA:
            local[name] = observed
        wanted["md5"] = observed["md5"]

    predecessor_entry = entries_map(predecessor)[RETAINED_ADDENDA]
    if (
        expected[RETAINED_ADDENDA]["bytes"],
        expected[RETAINED_ADDENDA]["md5"],
    ) != (
        int(predecessor_entry["size"]),
        normalize_checksum(predecessor_entry["checksum"]),
    ):
        raise RuntimeError("Retained addenda does not match predecessor")
    return expected, local


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
            raise RuntimeError("Untracked workflow successor draft already exists")
        state = json.loads(DRAFT_STATE.read_text(encoding="utf-8"))
        draft = existing.json()
        draft_id = int(draft["id"])
        if (
            draft_id != int(state["draft_id"])
            or concept_doi(draft) != CONCEPT_DOI
        ):
            raise RuntimeError("Existing workflow draft is not the tracked draft")
        return draft_id
    check(existing, {404})
    if DRAFT_STATE.is_file():
        state = json.loads(DRAFT_STATE.read_text(encoding="utf-8"))
        if state.get("published"):
            raise RuntimeError("Tracked workflow successor is already published")
        raise RuntimeError("Tracked workflow draft state exists but draft is absent")

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
        raise RuntimeError("Workflow predecessor is not a versioning base")
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
        raise RuntimeError("Workflow successor did not inherit predecessor set")
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


def stage(
    session: requests.Session,
    token: str,
    draft_id: int,
    expected: dict,
    local: dict,
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
        raise RuntimeError("Workflow successor is not an unpublished draft")
    files = legacy_file_map(deposition)
    extras = set(files) - set(expected) - REPLACED_FILES
    if extras:
        raise RuntimeError(f"Unexpected workflow draft files: {sorted(extras)}")

    actions = []
    for name in sorted(REPLACED_FILES, key=str.casefold):
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
    for name in sorted(local, key=str.casefold):
        identity = local[name]
        existing = files.get(name)
        if existing is not None:
            observed = (
                int(existing["filesize"]),
                normalize_checksum(existing["checksum"]),
            )
            if observed == (identity["bytes"], identity["md5"]):
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
        if (
            int(uploaded.get("size", uploaded.get("filesize", -1))),
            normalize_checksum(uploaded.get("checksum", "")),
        ) != (
            identity["bytes"],
            identity["md5"],
        ):
            raise RuntimeError(f"Workflow upload response mismatch: {name}")
        actions.append({"filename": name, "action": "uploaded_exact"})

    final = check(
        session.get(
            f"{API}/deposit/depositions/{draft_id}",
            headers=auth,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    files = legacy_file_map(final)
    if set(files) != set(expected):
        raise RuntimeError("Workflow draft final set mismatch")
    for name, identity in expected.items():
        row = files[name]
        if (
            int(row["filesize"]),
            normalize_checksum(row["checksum"]),
        ) != (
            identity["bytes"],
            identity["md5"],
        ):
            raise RuntimeError(f"Workflow staged identity mismatch: {name}")
    result = {
        "status": "PASS_STAGED",
        "errors": [],
        "record_id": draft_id,
        "concept_doi": CONCEPT_DOI,
        "file_count": len(files),
        "bytes": sum(int(row["filesize"]) for row in files.values()),
        "retained_predecessor_files": EXPECTED_RETAINED_FILES,
        "local_upload_files": len(local),
        "actions": actions,
        "duplicate_concept_created": False,
        "second_draft_created": False,
    }
    save_json(
        RECEIPT_ROOT
        / (
            "20260728_workflow_methodology_high_zoom_record_"
            f"{draft_id}_draft_files.json"
        ),
        result,
    )
    return result


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
        raise RuntimeError("Workflow draft escaped its existing concept")
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
        raise RuntimeError("Workflow version metadata mismatch")
    if metadata.get("publication_date") != PUBLICATION_DATE:
        raise RuntimeError("Workflow publication-date mismatch")
    if metadata.get("description") != DESCRIPTION_HTML:
        raise RuntimeError("Workflow description metadata mismatch")
    if not any(
        row.get("description") == NOTES_HTML
        for row in metadata.get("additional_descriptions", [])
    ):
        raise RuntimeError("Workflow notes metadata mismatch")


def publish(
    session: requests.Session,
    token: str,
    draft_id: int,
    expected: dict,
) -> dict:
    draft = modern_draft(session, token, draft_id)
    if set(draft["files"]["entries"]) != set(expected):
        raise RuntimeError("Cannot publish workflow draft: file set mismatch")
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
        raise RuntimeError("Workflow draft default preview mismatch")
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
        raise RuntimeError("Workflow publication escaped its concept")
    state = json.loads(DRAFT_STATE.read_text(encoding="utf-8"))
    state.update({"published": True, "doi": version_doi(published)})
    save_json(DRAFT_STATE, state)
    result = {
        "status": "PUBLISH_ACCEPTED",
        "errors": [],
        "record_id": draft_id,
        "doi": version_doi(published),
        "concept_doi": CONCEPT_DOI,
        "file_count": EXPECTED_FINAL_FILES,
        "default_preview": DEFAULT_PREVIEW,
        "duplicate_concept_created": False,
        "second_draft_created": False,
    }
    save_json(
        RECEIPT_ROOT
        / (
            "20260728_workflow_methodology_high_zoom_record_"
            f"{draft_id}_publish_response.json"
        ),
        result,
    )
    return result


def wait_public(session: requests.Session, record_id: int) -> dict:
    for _ in range(90):
        response = session.get(
            f"{API}/records/{record_id}?expand=true",
            headers={"Accept": "application/vnd.inveniordm.v1+json"},
            timeout=(30, 180),
        )
        if response.status_code == 200:
            record = response.json()
            if len(entries_map(record)) == EXPECTED_FINAL_FILES:
                return record
        time.sleep(3)
    raise RuntimeError("Workflow successor did not stabilize")


def safe_zip_name(name: str) -> None:
    path = PurePosixPath(name)
    if path.is_absolute() or ".." in path.parts or "\\" in name:
        raise RuntimeError(f"Unsafe workflow ZIP member: {name}")


def readback(record_id: int, expected: dict) -> tuple[dict, dict]:
    session = make_session()
    record = wait_public(session, record_id)
    if int(record["id"]) != record_id or concept_doi(record) != CONCEPT_DOI:
        raise RuntimeError("Public workflow successor lineage mismatch")
    assert_metadata(record["metadata"])
    if record["files"].get("default_preview") != DEFAULT_PREVIEW:
        raise RuntimeError("Public workflow default preview mismatch")
    entries = entries_map(record)
    if set(entries) != set(expected):
        raise RuntimeError("Public workflow file set mismatch")
    latest = check(
        session.get(
            f"{API}/records/{PREDECESSOR_RECORD}/versions/latest?expand=true",
            headers={"Accept": "application/vnd.inveniordm.v1+json"},
            timeout=(30, 180),
        ),
        {200},
    ).json()
    if int(latest["id"]) != record_id or concept_doi(latest) != CONCEPT_DOI:
        raise RuntimeError("Workflow successor is not the sole concept head")

    if READBACK_ROOT.exists():
        resolved = READBACK_ROOT.resolve()
        temp = Path(os.environ["LOCALAPPDATA"]).resolve() / "Temp"
        if temp not in resolved.parents:
            raise RuntimeError("Refusing to replace readback outside temp")
        shutil.rmtree(READBACK_ROOT)
    READBACK_ROOT.mkdir(parents=True)
    files = {}
    for index, name in enumerate(sorted(expected, key=str.casefold), start=1):
        print(f"READBACK {index}/{len(expected)} {name}", flush=True)
        entry = entries[name]
        target = READBACK_ROOT / name
        with session.get(
            entry["links"]["content"],
            stream=True,
            timeout=(30, 600),
        ) as response:
            check(response, {200})
            with target.open("wb") as handle:
                for block in response.iter_content(1024 * 1024):
                    if block:
                        handle.write(block)
        observed = {
            "bytes": target.stat().st_size,
            "sha256": sha256_file(target),
            "url": entry["links"]["content"],
        }
        wanted = expected[name]
        observed["match"] = (
            observed["bytes"],
            observed["sha256"],
        ) == (
            wanted["bytes"],
            wanted["sha256"],
        )
        if not observed["match"]:
            raise RuntimeError(f"Workflow readback mismatch: {name}")
        files[name] = observed

    archives = []
    members = []
    file_members = 0
    directory_entries = 0
    uncompressed = 0
    for name in sorted(files, key=str.casefold):
        if not name.lower().endswith(".zip"):
            continue
        path = READBACK_ROOT / name
        archive_files = 0
        archive_directories = 0
        archive_bytes = 0
        canonical = hashlib.sha256()
        with zipfile.ZipFile(path, "r") as archive:
            if archive.testzip() is not None:
                raise RuntimeError(f"Workflow ZIP CRC failure: {name}")
            for info in archive.infolist():
                safe_zip_name(info.filename)
                if info.is_dir():
                    archive_directories += 1
                    continue
                digest = hashlib.sha256()
                with archive.open(info) as source:
                    for block in iter(
                        lambda: source.read(1024 * 1024), b""
                    ):
                        digest.update(block)
                sha = digest.hexdigest().upper()
                canonical.update(
                    (
                        f"{info.filename}\t{info.file_size}\t{sha}\n"
                    ).encode("utf-8")
                )
                members.append(
                    {
                        "archive": name,
                        "relative_path": info.filename,
                        "bytes": info.file_size,
                        "sha256": sha,
                    }
                )
                archive_files += 1
                archive_bytes += info.file_size
        archives.append(
            {
                "filename": name,
                "bytes": path.stat().st_size,
                "sha256": sha256_file(path),
                "member_count": archive_files,
                "directory_entry_count": archive_directories,
                "all_entry_count": archive_files + archive_directories,
                "uncompressed_bytes": archive_bytes,
                "canonical_member_identity_sha256": (
                    canonical.hexdigest().upper()
                ),
                "errors": [],
            }
        )
        file_members += archive_files
        directory_entries += archive_directories
        uncompressed += archive_bytes
    observed_zip = (
        len(archives),
        file_members,
        directory_entries,
        uncompressed,
    )
    expected_zip = (
        EXPECTED_ZIP_ARCHIVES,
        EXPECTED_ZIP_FILE_MEMBERS,
        EXPECTED_ZIP_DIRECTORY_ENTRIES,
        EXPECTED_ZIP_UNCOMPRESSED_BYTES,
    )
    if observed_zip != expected_zip:
        raise RuntimeError(
            f"Workflow ZIP aggregate mismatch: observed={observed_zip}, "
            f"expected={expected_zip}"
        )

    public_receipt = {
        "status": "PASS",
        "errors": [],
        "record": record_id,
        "doi": version_doi(record),
        "conceptdoi": CONCEPT_DOI,
        "record_url": f"https://zenodo.org/records/{record_id}",
        "version": VERSION,
        "file_count": len(files),
        "bytes": sum(row["bytes"] for row in files.values()),
        "files": files,
        "latest_record": int(latest["id"]),
        "rdm_default_preview": record["files"].get("default_preview"),
        "github_commit": GITHUB_COMMIT,
        "github_package": GITHUB_PACKAGE,
        "retained_predecessor_files": EXPECTED_RETAINED_FILES,
        "duplicate_concept_created": False,
        "second_draft_created": False,
    }
    zip_receipt = {
        "status": "PASS",
        "errors": [],
        "record_id": record_id,
        "doi": version_doi(record),
        "zip_archive_count": len(archives),
        "zip_file_member_count": file_members,
        "zip_directory_entry_count": directory_entries,
        "zip_all_entry_count": file_members + directory_entries,
        "zip_uncompressed_bytes": uncompressed,
        "archives": archives,
        "members": members,
    }
    save_json(
        RECEIPT_ROOT
        / (
            "20260728_workflow_methodology_high_zoom_record_"
            f"{record_id}_public_readback.json"
        ),
        public_receipt,
    )
    save_json(
        RECEIPT_ROOT
        / (
            "20260728_workflow_methodology_high_zoom_record_"
            f"{record_id}_zip_member_readback.json"
        ),
        zip_receipt,
    )
    shutil.rmtree(READBACK_ROOT)
    return public_receipt, zip_receipt


def main() -> None:
    token = find_token()
    session = make_session()
    assert_predecessor_is_latest(session)
    predecessor = public_predecessor(session)
    expected, local = expected_identities(predecessor)
    draft_id = create_or_resume_draft(
        session, token, predecessor
    )
    staged = stage(
        session, token, draft_id, expected, local
    )
    published = publish(
        session, token, draft_id, expected
    )
    public, zipped = readback(draft_id, expected)
    print(
        json.dumps(
            {
                "stage": staged,
                "publish": published,
                "readback": {
                    "status": public["status"],
                    "record": public["record"],
                    "doi": public["doi"],
                    "file_count": public["file_count"],
                    "bytes": public["bytes"],
                    "zip_archives": zipped["zip_archive_count"],
                    "zip_file_members": zipped["zip_file_member_count"],
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
