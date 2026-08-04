#!/usr/bin/env python3
"""Publish the exact FAC reference-v2 R4 package on the existing FAC concept."""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import json
import os
import time
import zipfile
from pathlib import Path
from urllib.parse import quote

import publish_current_reader_bundles_zenodo_20260730 as base


API = base.API
MODERN = {"Accept": "application/vnd.inveniordm.v1+json"}
CONCEPT_ID = "21720996"
CONCEPT_DOI = "10.5281/zenodo.21720996"
KNOWN_PREDECESSOR_ID = 21781714
EXPECTED_FILES = 50
EXPECTED_BYTES = 14_827_551
DEFAULT_PREVIEW = "00_FAC_Blind_Comparison_Readable_Report.pdf"
PUBLICATION_DATE = "2026-08-04"
VERSION = "2026-08-04 FAC complete readers and reference-v2 blind comparison"
TITLE = (
    "Jean-Pierre Serre’s FAC: French transcription, English translation, "
    "and an accidental blind comparison"
)
NORMALIZED_TITLE = TITLE.replace("’", "'")

INTERLANGUAGE_ROOT = Path(
    os.environ.get(
        "INTERLANGUAGE_ROOT",
        str(Path.home() / "Documents" / "interlanguage"),
    )
)
ROOT = (
    INTERLANGUAGE_ROOT
    / "03_projects"
    / "language_management"
    / "english_germanic"
    / "06_publication_candidates"
    / "FAC_single_concept_complete_reader_blind_comparison_reference_v2_20260804_r4"
)
REPO_ROOT = Path(__file__).resolve().parents[1]
TEMP_ROOT = (
    Path(os.environ.get("LOCALAPPDATA", os.environ.get("TEMP", ".")))
    / "Temp"
    / "fac_reference_v2_r4_20260804"
)
STATE_PATH = TEMP_ROOT / "draft_state.json"
MANIFEST = "ZENODO_PAYLOAD_MANIFEST.csv"
MANIFEST_BYTES = 7_645
MANIFEST_SHA256 = "533CB568CEC683DB1FB58776BA3D52E0AD2665D89840E8E8548253A59AEDE8C5"
VALIDATION = "PACKAGE_VALIDATION.json"
VALIDATION_BYTES = 1_199
VALIDATION_SHA256 = "F9E7C37FD34365AAE4ADC4891C681B9163901B922D5DD2BB2BF9DE6726634CB7"
COMPLETE_ZIP = "04_FAC_Complete_Readers_Source_and_Blind_Comparison_Evidence_20260804.zip"
COMPLETE_ZIP_BYTES = 5_763_215
COMPLETE_ZIP_SHA256 = "1864EDB8B318112E6D4CAE32BC2929F9D67406AB7290A966A8F7B770DF9D72CA"
COMPLETE_ZIP_MEMBERS = 47
SOURCE_ZIP = "19_FAC_Project_English_and_French_TeX_Source_Layers.zip"
SOURCE_ZIP_BYTES = 546_912
SOURCE_ZIP_SHA256 = "AE8825DC99FB15010EAF1BA536B5D12E9C81833A5658F3817D281E781B17AB3B"
SOURCE_ZIP_MEMBERS = 94

DESCRIPTION = """<h2>Jean-Pierre Serre’s FAC: readers, sources, and blind comparison</h2>
<p>This record is the single FAC publication line. It contains a complete French diplomatic working transcription, a separately corrected French reader, a complete English reader with source-local and cross-unit reference navigation, editable TeX/source layers, and the full evidence for an accidentally blind translation comparison.</p>
<p>The project coordinator did not know that the published English translation by Piotr Achinger and Łukasz Krupa existed when an independent English translation was produced from the French working transcription and checked against Serre’s source. The comparator was discovered afterward. The blind-scope English through no. 79 was then frozen and all 79 units were adjudicated against the French authority, producing 138 exact findings and an append-only self-correction ledger. Nos. 80–81 are outside the blind claim.</p>
<p><strong>Start with <code>00_FAC_Blind_Comparison_Readable_Report.pdf</code>.</strong> It presents the chronology, worked examples, evidence, limitations, and audit procedure. The complete ZIP is the coherent transport; separate French and English readers, TeX, graphs, logbooks, decision records, correction/reversal history, validators, and source identities remain directly downloadable.</p>
<p>The English reference-v2 surface contains 661 targets and 1,972 adjudicated candidates: 596 active edges and 1,376 intentional residuals. This is a working transcription/translation and a bounded qualitative comparison—not a scalar score, general benchmark, critical edition, peer review, or mathematical certification. Important passages should still be checked against Serre’s French source.</p>
<p>The authority scan and the Achinger–Krupa PDF/source are identified but not redistributed. GAGA is maintained separately under concept DOI 10.5281/zenodo.21781322. The redundant FAC assessment concept 10.5281/zenodo.21779392 remains tombstoned as a duplicate; this record is the surviving FAC concept.</p>"""
NORMALIZED_DESCRIPTION = DESCRIPTION.replace("’", "'")

ADDITIONAL_NOTE = """<p>Exact R4 public projection: 50 files / 14,827,551 bytes; 48-row self-excluding manifest; package validation PASS/errors[]; complete transport ZIP 47/47 members; project source ZIP 94/94 entries; privacy scan 39 outer text files plus 148 ZIP text members, hits0. Four principal readers are 36, 78, 63, and 63 pages. The provenance surface includes the project logbook, editorial decision logbook, self-correction/reversal ledger, reference-v2 logbook/status, complete provenance ZIP, and exact graph/validation tables.</p>"""

SUBJECTS = [
    "blind translation comparison",
    "comparative translation",
    "AI-assisted translation",
    "translation quality assessment",
    "provenance",
    "French transcription",
    "English translation",
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(4 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def md5(path: Path) -> str:
    digest = hashlib.md5(usedforsecurity=False)
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(4 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().lower()


def auth(token: str) -> dict[str, str]:
    return {"Authorization": f"Bearer {token}"}


def auth_modern(token: str) -> dict[str, str]:
    return {**auth(token), **MODERN}


def save_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def load_state() -> dict | None:
    if not STATE_PATH.exists():
        return None
    return json.loads(STATE_PATH.read_text(encoding="utf-8"))


def modern_entries(record: dict) -> dict[str, dict]:
    entries = record.get("files", {}).get("entries", [])
    if isinstance(entries, dict):
        return entries
    return {row["key"]: row for row in entries}


def legacy_entries(record: dict) -> dict[str, dict]:
    return {row["filename"]: row for row in record.get("files", [])}


def normalized_md5(value: str) -> str:
    return value.lower().removeprefix("md5:")


def modern_identity(row: dict) -> tuple[int, str]:
    return int(row["size"]), normalized_md5(row["checksum"])


def legacy_identity(row: dict) -> tuple[int, str]:
    return int(row["filesize"]), normalized_md5(row["checksum"])


def zip_rows(path: Path) -> list[dict]:
    rows = []
    with zipfile.ZipFile(path) as archive:
        bad = archive.testzip()
        if bad is not None:
            raise RuntimeError(f"ZIP CRC failure {path.name}: {bad}")
        for info in archive.infolist():
            if info.is_dir():
                continue
            digest = hashlib.sha256()
            with archive.open(info) as handle:
                for block in iter(lambda: handle.read(4 * 1024 * 1024), b""):
                    digest.update(block)
            rows.append(
                {
                    "path": info.filename,
                    "bytes": int(info.file_size),
                    "sha256": digest.hexdigest().upper(),
                }
            )
    return rows


def local_surface() -> tuple[dict[str, dict], list[str], dict[str, list[dict]]]:
    if not ROOT.is_dir():
        raise RuntimeError(f"FAC R4 root missing: {ROOT}")
    recursive = [path for path in ROOT.rglob("*") if path.is_file()]
    if any(path.parent != ROOT for path in recursive):
        raise RuntimeError("FAC R4 public root unexpectedly contains nested files")
    if len(recursive) != EXPECTED_FILES or sum(path.stat().st_size for path in recursive) != EXPECTED_BYTES:
        raise RuntimeError("FAC R4 root count/byte boundary changed")
    exact = {
        MANIFEST: (MANIFEST_BYTES, MANIFEST_SHA256),
        VALIDATION: (VALIDATION_BYTES, VALIDATION_SHA256),
        COMPLETE_ZIP: (COMPLETE_ZIP_BYTES, COMPLETE_ZIP_SHA256),
        SOURCE_ZIP: (SOURCE_ZIP_BYTES, SOURCE_ZIP_SHA256),
        DEFAULT_PREVIEW: (
            141_174,
            "F1A643DDF5810DC983C78FE4F300572779F5C1C3D8D308ECC11B84F79B7EEFE1",
        ),
        "01_FAC_English_Complete_Reader.pdf": (
            515_735,
            "0FCF262B2F9B9BE4269EFA82DA84346D4AF061B320CFA118E4EA4BCB3507303C",
        ),
        "00b_FAC_French_Diplomatic_Reader.pdf": (
            633_611,
            "DF916FDEFF9DBF4D47DF529DCDBD25116412DA254A247436587B7A7848279359",
        ),
        "00c_FAC_French_Corrected_Reader.pdf": (
            633_971,
            "4578A764F9C9DC72F29F40A678C45E3AB8C67BFFAE5476CEB51308498C41531E",
        ),
    }
    for name, expected in exact.items():
        path = ROOT / name
        observed = (path.stat().st_size, sha256(path))
        if observed != expected:
            raise RuntimeError(f"FAC R4 exact identity changed: {name}: {observed!r}")
    validation = json.loads((ROOT / VALIDATION).read_text(encoding="utf-8"))
    if validation.get("status") != "PASS_READY_FOR_SAME_CONCEPT_ARCHIVE_HANDOFF" or validation.get("errors") != []:
        raise RuntimeError("FAC R4 package validation is not PASS/errors[]")
    with (ROOT / MANIFEST).open("r", encoding="utf-8-sig", newline="") as handle:
        manifest_rows = list(csv.DictReader(handle))
    if len(manifest_rows) != 48:
        raise RuntimeError("FAC R4 manifest row count changed")
    expected_manifest_names = {path.name for path in recursive} - {MANIFEST, VALIDATION}
    if {row["path"] for row in manifest_rows} != expected_manifest_names:
        raise RuntimeError("FAC R4 manifest filename closure changed")
    for row in manifest_rows:
        path = ROOT / row["path"]
        if (path.stat().st_size, sha256(path)) != (int(row["bytes"]), row["sha256"].upper()):
            raise RuntimeError(f"FAC R4 manifest replay changed: {row['path']}")
    zip_replays = {}
    for path in sorted((p for p in recursive if p.suffix.lower() == ".zip"), key=lambda p: p.name.casefold()):
        zip_replays[path.name] = zip_rows(path)
    if len(zip_replays[COMPLETE_ZIP]) != COMPLETE_ZIP_MEMBERS:
        raise RuntimeError("FAC complete ZIP member count changed")
    if len(zip_replays[SOURCE_ZIP]) != SOURCE_ZIP_MEMBERS:
        raise RuntimeError("FAC source ZIP member count changed")
    surface = {
        path.name: {
            "path": str(path),
            "bytes": path.stat().st_size,
            "sha256": sha256(path),
            "md5": md5(path),
        }
        for path in recursive
    }
    front = [
        COMPLETE_ZIP,
        DEFAULT_PREVIEW,
        "01_FAC_English_Complete_Reader.pdf",
        "00b_FAC_French_Diplomatic_Reader.pdf",
        "00c_FAC_French_Corrected_Reader.pdf",
        "05_READ_ME_FIRST.md",
        "13_FAC_Editorial_Decision_Logbook.md",
        "14_FAC_Self_Correction_Ledger.csv",
        "15_FAC_Project_Logbook.md",
    ]
    order = front + sorted(set(surface) - set(front), key=str.casefold)
    if len(order) != EXPECTED_FILES or len(order) != len(set(order)):
        raise RuntimeError("FAC R4 file order boundary changed")
    return surface, order, zip_replays


def fetch_live(session) -> dict:
    live = base.check(
        session.get(
            f"{API}/records/{KNOWN_PREDECESSOR_ID}/versions/latest",
            headers=MODERN,
            timeout=(30, 300),
        ),
        {200},
    ).json()
    if (
        str(live.get("parent", {}).get("id")) != CONCEPT_ID
        or live.get("parent", {}).get("pids", {}).get("doi", {}).get("identifier") != CONCEPT_DOI
        or live.get("status") != "published"
        or live.get("versions", {}).get("is_latest") is not True
    ):
        raise RuntimeError("Live FAC same-concept boundary changed")
    return live


def verify_draft_state(session, token: str, live: dict) -> dict | None:
    state = load_state()
    probe = session.get(
        f"{API}/records/{int(live['id'])}/draft",
        headers=auth_modern(token),
        timeout=(30, 180),
    )
    if state is None:
        if probe.status_code == 200:
            raise RuntimeError(f"Untracked FAC successor draft exists: {probe.json().get('id')}")
        base.check(probe, {404, 410})
        return None
    if state.get("published"):
        if probe.status_code not in {404, 410}:
            raise RuntimeError("Published FAC state conflicts with active draft")
        return state
    if int(state.get("predecessor_record", 0)) != int(live["id"]):
        raise RuntimeError("Tracked FAC predecessor changed")
    tracked_id = int(state["draft_id"])
    tracked = base.check(
        session.get(
            f"{API}/records/{tracked_id}/draft",
            headers=auth_modern(token),
            timeout=(30, 180),
        ),
        {200},
    ).json()
    if str(tracked.get("parent", {}).get("id")) != CONCEPT_ID or tracked.get("is_published") is not False:
        raise RuntimeError("Tracked FAC draft left the concept")
    return state


def create_or_resume(session, token: str, live: dict) -> tuple[int, bool]:
    state = verify_draft_state(session, token, live)
    if state is not None:
        if state.get("published"):
            raise RuntimeError("FAC R4 successor is already published")
        return int(state["draft_id"]), False
    predecessor_id = int(live["id"])
    predecessor = base.check(
        session.get(
            f"{API}/deposit/depositions/{predecessor_id}",
            headers=auth(token),
            timeout=(30, 300),
        ),
        {200},
    ).json()
    if (
        predecessor.get("state") != "done"
        or not predecessor.get("submitted")
        or str(predecessor.get("conceptrecid")) != CONCEPT_ID
        or not predecessor.get("links", {}).get("newversion")
    ):
        raise RuntimeError("FAC predecessor is not a safe same-concept versioning base")
    created = base.check(
        session.post(
            predecessor["links"]["newversion"],
            headers=auth(token),
            timeout=(30, 600),
        ),
        {201},
    ).json()
    deposition = base.check(
        session.get(
            created["links"]["latest_draft"], headers=auth(token), timeout=(30, 300)
        ),
        {200},
    ).json()
    draft_id = int(deposition["id"])
    if set(legacy_entries(deposition)) != set(modern_entries(live)):
        raise RuntimeError("FAC successor failed to inherit predecessor file set")
    modern = base.check(
        session.get(
            f"{API}/records/{draft_id}/draft",
            headers=auth_modern(token),
            timeout=(30, 180),
        ),
        {200},
    ).json()
    if (
        str(modern.get("parent", {}).get("id")) != CONCEPT_ID
        or modern.get("versions", {}).get("index") != int(live["versions"]["index"]) + 1
    ):
        raise RuntimeError("Created FAC draft lineage changed")
    save_json(
        STATE_PATH,
        {
            "status": "OPEN_TRACKED_DRAFT",
            "predecessor_record": predecessor_id,
            "predecessor_doi": live["pids"]["doi"]["identifier"],
            "predecessor_version_index": int(live["versions"]["index"]),
            "concept_id": CONCEPT_ID,
            "concept_doi": CONCEPT_DOI,
            "draft_id": draft_id,
            "published": False,
            "created_at_epoch": int(time.time()),
        },
    )
    return draft_id, True


def desired_metadata(current: dict) -> dict:
    metadata = copy.deepcopy(current)
    metadata["resource_type"] = {"id": "dataset"}
    metadata["title"] = TITLE
    metadata["publication_date"] = PUBLICATION_DATE
    metadata["version"] = VERSION
    metadata["languages"] = [{"id": "fra"}, {"id": "eng"}]
    existing = []
    seen = set()
    for row in current.get("subjects", []):
        value = str(row.get("subject", "")).strip()
        if not value or value.casefold() == "gaga" or value.casefold() in seen:
            continue
        existing.append({"subject": value})
        seen.add(value.casefold())
    for value in SUBJECTS:
        if value.casefold() not in seen:
            existing.append({"subject": value})
            seen.add(value.casefold())
    metadata["subjects"] = existing
    metadata["description"] = DESCRIPTION
    metadata["additional_descriptions"] = [
        {"description": ADDITIONAL_NOTE, "type": {"id": "notes"}}
    ]
    return metadata


def verify_exact_draft(draft: dict, surface: dict[str, dict], order: list[str]) -> None:
    entries = modern_entries(draft)
    if set(entries) != set(surface) or len(entries) != EXPECTED_FILES:
        raise RuntimeError("FAC R4 staged filename closure changed")
    errors = [
        name
        for name, row in surface.items()
        if modern_identity(entries[name]) != (int(row["bytes"]), row["md5"])
    ]
    if errors:
        raise RuntimeError(f"FAC R4 staged file identities changed: {errors}")
    metadata = draft.get("metadata", {})
    language_ids = [row.get("id") for row in metadata.get("languages", [])]
    subjects = [str(row.get("subject", "")) for row in metadata.get("subjects", [])]
    notes = metadata.get("additional_descriptions", [])
    if (
        metadata.get("title") not in {TITLE, NORMALIZED_TITLE}
        or metadata.get("publication_date") != PUBLICATION_DATE
        or metadata.get("version") != VERSION
        or metadata.get("resource_type", {}).get("id") != "dataset"
        or language_ids != ["fra", "eng"]
        or metadata.get("description") not in {DESCRIPTION, NORMALIZED_DESCRIPTION}
        or len(notes) != 1
        or notes[0].get("description") != ADDITIONAL_NOTE
        or any(value.casefold() == "gaga" for value in subjects)
        or draft.get("files", {}).get("default_preview") != DEFAULT_PREVIEW
    ):
        raise RuntimeError("FAC R4 staged metadata/default preview changed")
    observed_order = draft.get("files", {}).get("order") or []
    if observed_order not in (order, []):
        raise RuntimeError("FAC R4 configured file order changed")


def upload(session, token: str, bucket: str, name: str, path: Path) -> None:
    print(f"UPLOAD {name} ({path.stat().st_size} bytes)", flush=True)
    with path.open("rb") as handle:
        base.check(
            session.put(
                f"{bucket.rstrip('/')}/{quote(name, safe='')}",
                headers={**auth(token), "Content-Type": "application/octet-stream"},
                data=handle,
                timeout=(30, 3600),
            ),
            {200, 201},
        )


def preflight(session, token: str) -> dict:
    surface, order, zip_replays = local_surface()
    live = fetch_live(session)
    state = verify_draft_state(session, token, live)
    return {
        "status": "PASS_READY_FOR_ONE_FAC_SAME_CONCEPT_SUCCESSOR",
        "concept_id": CONCEPT_ID,
        "concept_doi": CONCEPT_DOI,
        "live_record_id": int(live["id"]),
        "live_version_doi": live["pids"]["doi"]["identifier"],
        "live_version_index": int(live["versions"]["index"]),
        "live_files": len(modern_entries(live)),
        "live_bytes": sum(int(row["size"]) for row in modern_entries(live).values()),
        "active_draft": state is not None and not state.get("published", False),
        "tracked_draft_id": None if state is None else state.get("draft_id"),
        "replacement_files": len(surface),
        "replacement_bytes": sum(int(row["bytes"]) for row in surface.values()),
        "complete_zip_members": len(zip_replays[COMPLETE_ZIP]),
        "source_zip_members": len(zip_replays[SOURCE_ZIP]),
        "default_preview": DEFAULT_PREVIEW,
        "duplicate_concept_created": False,
        "gaga_mutated": False,
    }


def stage(session, token: str) -> dict:
    surface, order, _ = local_surface()
    live = fetch_live(session)
    draft_id, created = create_or_resume(session, token, live)
    deposition = base.check(
        session.get(
            f"{API}/deposit/depositions/{draft_id}",
            headers=auth(token),
            timeout=(30, 300),
        ),
        {200},
    ).json()
    remote = legacy_entries(deposition)
    deleted = []
    retained_exact = []
    for name, row in list(remote.items()):
        wanted = surface.get(name)
        if wanted is not None and legacy_identity(row) == (int(wanted["bytes"]), wanted["md5"]):
            retained_exact.append(name)
            continue
        base.check(
            session.delete(row["links"]["self"], headers=auth(token), timeout=(30, 300)),
            {204},
        )
        deleted.append(name)
    deposition = base.check(
        session.get(
            f"{API}/deposit/depositions/{draft_id}",
            headers=auth(token),
            timeout=(30, 300),
        ),
        {200},
    ).json()
    remote = legacy_entries(deposition)
    bucket = deposition["links"]["bucket"]
    uploaded = []
    for name in order:
        if name in remote:
            continue
        upload(session, token, bucket, name, Path(surface[name]["path"]))
        uploaded.append(name)
    draft = base.check(
        session.get(
            f"{API}/records/{draft_id}/draft",
            headers=auth_modern(token),
            timeout=(30, 600),
        ),
        {200},
    ).json()
    if set(modern_entries(draft)) != set(surface):
        raise RuntimeError("FAC R4 draft file set incomplete after upload")
    payload = {
        "access": draft["access"],
        "files": {"enabled": True, "default_preview": DEFAULT_PREVIEW, "order": order},
        "metadata": desired_metadata(draft["metadata"]),
        "custom_fields": draft.get("custom_fields", {}),
    }
    if draft.get("pids"):
        payload["pids"] = draft["pids"]
    patched = base.check(
        session.put(
            f"{API}/records/{draft_id}/draft",
            headers={**auth_modern(token), "Content-Type": "application/json"},
            json=payload,
            timeout=(30, 600),
        ),
        {200},
    ).json()
    verify_exact_draft(patched, surface, order)
    state = load_state()
    if state is None or int(state["draft_id"]) != draft_id:
        raise RuntimeError("Tracked FAC R4 state disappeared")
    state.update(
        {
            "status": "STAGED_EXACT_READY_FOR_EXPLICIT_PUBLISH",
            "staged": True,
            "staged_at_epoch": int(time.time()),
        }
    )
    save_json(STATE_PATH, state)
    return {
        "status": "STAGED_EXACT_READY_FOR_EXPLICIT_PUBLISH",
        "draft_id": draft_id,
        "draft_url": patched.get("links", {}).get("self_html"),
        "concept_id": CONCEPT_ID,
        "concept_doi": CONCEPT_DOI,
        "predecessor_record_id": int(live["id"]),
        "created_new_same_concept_draft": created,
        "deleted_or_replaced_inherited_files": len(deleted),
        "retained_exact_inherited_files": len(retained_exact),
        "uploaded_files": len(uploaded),
        "files": len(surface),
        "bytes": sum(int(row["bytes"]) for row in surface.values()),
        "default_preview": DEFAULT_PREVIEW,
        "duplicate_concept_created": False,
        "gaga_mutated": False,
    }


def stream_identity(session, url: str, destination: Path | None = None) -> tuple[int, str]:
    digest = hashlib.sha256()
    total = 0
    response = base.check(session.get(url, stream=True, timeout=(30, 3600)), {200})
    try:
        handle = None if destination is None else destination.open("wb")
        try:
            for block in response.iter_content(4 * 1024 * 1024):
                if not block:
                    continue
                if handle is not None:
                    handle.write(block)
                digest.update(block)
                total += len(block)
        finally:
            if handle is not None:
                handle.close()
    finally:
        response.close()
    return total, digest.hexdigest().upper()


def publish_and_readback(session, token: str, confirm: str, receipt_dir: Path) -> dict:
    surface, order, local_zip_rows = local_surface()
    live = fetch_live(session)
    state = verify_draft_state(session, token, live)
    if state is None or state.get("published") or not state.get("staged"):
        raise RuntimeError("No exact staged FAC R4 draft is tracked")
    draft_id = int(state["draft_id"])
    if confirm != str(draft_id):
        raise RuntimeError(f"Publishing requires --confirm-publish {draft_id}")
    draft = base.check(
        session.get(
            f"{API}/records/{draft_id}/draft",
            headers=auth_modern(token),
            timeout=(30, 600),
        ),
        {200},
    ).json()
    verify_exact_draft(draft, surface, order)
    if (
        str(draft.get("parent", {}).get("id")) != CONCEPT_ID
        or int(draft.get("versions", {}).get("index", 0)) != int(live["versions"]["index"]) + 1
    ):
        raise RuntimeError("FAC R4 staged lineage changed")
    response = base.check(
        session.post(
            draft["links"]["publish"],
            headers=auth_modern(token),
            timeout=(30, 1200),
        ),
        {200, 202},
    )
    try:
        record_id = int(response.json().get("id", draft_id))
    except Exception:
        record_id = draft_id
    record = None
    anonymous = base.make_session()
    for _ in range(60):
        probe = anonymous.get(
            f"{API}/records/{record_id}", headers=MODERN, timeout=(30, 300)
        )
        if probe.status_code == 200 and probe.json().get("status") == "published":
            record = probe.json()
            break
        time.sleep(2)
    if record is None:
        raise RuntimeError("FAC R4 successor did not become public")
    if (
        str(record.get("parent", {}).get("id")) != CONCEPT_ID
        or record.get("parent", {}).get("pids", {}).get("doi", {}).get("identifier") != CONCEPT_DOI
        or record.get("versions", {}).get("is_latest") is not True
        or int(record.get("versions", {}).get("index", 0)) != int(live["versions"]["index"]) + 1
    ):
        raise RuntimeError("Published FAC R4 lineage changed")
    verify_exact_draft(record, surface, order)
    entries = modern_entries(record)
    temp_downloads = TEMP_ROOT / "public_readback"
    temp_downloads.mkdir(parents=True, exist_ok=True)
    readback = []
    zip_replays = {}
    errors = []
    for index, name in enumerate(order, start=1):
        print(f"READBACK {index}/{len(order)} {name}", flush=True)
        destination = temp_downloads / name if name.lower().endswith(".zip") else None
        observed = stream_identity(anonymous, entries[name]["links"]["content"], destination)
        expected = (int(surface[name]["bytes"]), surface[name]["sha256"])
        match = observed == expected
        if not match:
            errors.append(name)
        readback.append(
            {
                "filename": name,
                "bytes": observed[0],
                "sha256": observed[1],
                "match": match,
                "content_url": entries[name]["links"]["content"],
            }
        )
        if destination is not None:
            downloaded_rows = zip_rows(destination)
            zip_match = downloaded_rows == local_zip_rows[name]
            if not zip_match:
                errors.append(name + ":zip_members")
            zip_replays[name] = {
                "members": len(downloaded_rows),
                "match": zip_match,
                "member_identities": downloaded_rows,
            }
            destination.unlink()
    if errors:
        raise RuntimeError(f"FAC R4 public readback errors: {errors}")
    active = session.get(
        f"{API}/records/{int(live['id'])}/draft",
        headers=auth_modern(token),
        timeout=(30, 180),
    )
    if active.status_code not in {404, 410}:
        raise RuntimeError("FAC active draft remains after publication")
    result = {
        "status": "PASS_PUBLISHED_FAC_R4_SAME_CONCEPT_AND_ANONYMOUS_RAW_READBACK",
        "errors": [],
        "record_id": record_id,
        "record_url": record["links"]["self_html"],
        "version_doi": record["pids"]["doi"]["identifier"],
        "concept_id": CONCEPT_ID,
        "concept_doi": CONCEPT_DOI,
        "predecessor_record_id": int(live["id"]),
        "predecessor_version_doi": live["pids"]["doi"]["identifier"],
        "version_index": int(record["versions"]["index"]),
        "title": record["metadata"]["title"],
        "publication_date": record["metadata"]["publication_date"],
        "version": record["metadata"]["version"],
        "default_preview": record["files"]["default_preview"],
        "files": len(entries),
        "bytes": sum(int(row["size"]) for row in entries.values()),
        "raw_readback_matches": len(readback),
        "raw_readback_mismatches": 0,
        "zip_replays": zip_replays,
        "active_draft": False,
        "duplicate_concept_created": False,
        "gaga_mutated": False,
        "readback": readback,
        "configured_file_order": order,
        "api_file_order": record["files"].get("order") or [],
    }
    receipt_path = receipt_dir / f"20260804_fac_reference_v2_r4_record_{record_id}_public_readback.json"
    save_json(receipt_path, result)
    result["receipt_path"] = str(receipt_path)
    result["receipt_bytes"] = receipt_path.stat().st_size
    result["receipt_sha256"] = sha256(receipt_path)
    state.update(
        {
            "status": "PASS_PUBLISHED_AND_ANONYMOUS_READBACK",
            "published": True,
            "record_id": record_id,
            "doi": result["version_doi"],
            "receipt_path": str(receipt_path),
            "completed_at_epoch": int(time.time()),
        }
    )
    save_json(STATE_PATH, state)
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=("preflight", "stage", "publish"))
    parser.add_argument("--confirm-publish")
    parser.add_argument(
        "--receipt-dir",
        type=Path,
        default=REPO_ROOT / "manifests" / "published-zenodo",
    )
    args = parser.parse_args()
    session = base.make_session()
    token = base.find_token()
    if args.action == "preflight":
        result = preflight(session, token)
    elif args.action == "stage":
        result = stage(session, token)
    else:
        if not args.confirm_publish:
            raise RuntimeError("Publishing requires --confirm-publish DRAFT_ID")
        result = publish_and_readback(
            session, token, args.confirm_publish, args.receipt_dir.resolve()
        )
    summary = {
        key: value
        for key, value in result.items()
        if key not in {"readback", "zip_replays", "configured_file_order", "api_file_order"}
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
