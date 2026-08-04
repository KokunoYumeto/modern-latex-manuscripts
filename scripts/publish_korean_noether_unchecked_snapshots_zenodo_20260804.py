#!/usr/bin/env python3
"""Publish five bounded Korean Noether snapshots on the existing Noether concept."""

from __future__ import annotations

import argparse
import copy
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
PREDECESSOR_ID = 21699405
PREDECESSOR_DOI = "10.5281/zenodo.21699405"
CONCEPT_ID = "20412587"
CONCEPT_DOI = "10.5281/zenodo.20412587"
PREDECESSOR_VERSION_INDEX = 171
PREDECESSOR_FILES = 20
PREDECESSOR_BYTES = 583_142_749
DEFAULT_PREVIEW = "01j_Noether_R823_Full_Cumulative_English_20260722.pdf"

REPO_ROOT = Path(__file__).resolve().parents[1]
PUBLIC_ROOT = (
    REPO_ROOT
    / "sources"
    / "noether"
    / "korean-unchecked-papers-01-05-07-41-42-20260804"
)
PREDECESSOR_RECEIPT = (
    REPO_ROOT
    / "manifests"
    / "published-zenodo"
    / "20260730_noether_record_21699405_public_readback.json"
)
EXPECTED_ROOT_VALIDATION_SHA256 = (
    "87DDD1BDA6ED67A9EFC151EF377BDE80A1BD560A5D4F2D728E8480D42F18E0C3"
)
EXPECTED_ROOT_VALIDATION_BYTES = 8_649
EXPECTED_INDEX_SHA256 = (
    "C50DAAE5D373AC66F38A41E46990533A1E958F68A96DB686E4F0CDD4876FB298"
)
EXPECTED_INDEX_BYTES = 2_111
EXPECTED_README_SHA256 = (
    "1BE952DC9860E6D39A68EE39FF72793647B91134829261075532F07331AF336C"
)
EXPECTED_README_BYTES = 1_167
EXPECTED_NEW_FILES = 78
EXPECTED_RESULTING_FILES = 98

PAPERS = {
    "P01": {
        "prefix": "70a_KO_P01__",
        "zip": "P01_Korean_UNCHECKED_Public_Snapshot_20260804.zip",
        "zip_sha256": "83E6A988F1E1F7B7A4EB239C96AAC8FDEE2043D9CB59E5E50EF47158EBCD2311",
        "zip_bytes": 81_864,
        "zip_members": 35,
        "targets": 3,
        "target_dir": "ko",
        "structural": "evidence/structural_index/PRODUCER_STRUCTURAL_INDEX.jsonl",
        "difficulty": "evidence/difficulty_ledger/DIFFICULTY_LEDGER.jsonl",
    },
    "P05": {
        "prefix": "70b_KO_P05__",
        "zip": "P05_Korean_UNCHECKED_Public_Snapshot_20260804.zip",
        "zip_sha256": "0CD26F1BB25C745520B73A002E2003F515E6E73F5E3FE71C90BA3D12452AF687",
        "zip_bytes": 73_186,
        "zip_members": 29,
        "targets": 4,
        "target_dir": "targets",
        "structural": "evidence/structural_index/PRODUCER_STRUCTURAL_INDEX.jsonl",
        "difficulty": "evidence/difficulty/DIFFICULTY_LEDGER.jsonl",
    },
    "P07": {
        "prefix": "70c_KO_P07__",
        "zip": "P07_Korean_UNCHECKED_Public_Snapshot_20260804.zip",
        "zip_sha256": "10D5070AF8EEF4B2E9CE88DD591367839C174FFFB2F37AAB533BDEE70D9FE5A9",
        "zip_bytes": 95_089,
        "zip_members": 45,
        "targets": 8,
        "target_dir": "targets",
        "structural": "reproducibility/structural/STRUCTURAL_INDEX.jsonl",
        "difficulty": "reproducibility/difficulty/DIFFICULTY_LEDGER.jsonl",
    },
    "P41": {
        "prefix": "70d_KO_P41__",
        "zip": "P41_Korean_UNCHECKED_Public_Snapshot_20260804.zip",
        "zip_sha256": "0DB7DA9E85C8EE416CD10F21CB6BBBA7B299C6659A02A96CF9F1030B3F14EF87",
        "zip_bytes": 180_083,
        "zip_members": 47,
        "targets": 12,
        "target_dir": "targets",
        "structural": "evidence/structural_index/PRODUCER_STRUCTURAL_INDEX.jsonl",
        "difficulty": "evidence/difficulty/difficulty_ledger.jsonl",
    },
    "P42": {
        "prefix": "70e_KO_P42__",
        "zip": "P42_Korean_UNCHECKED_Public_Snapshot_20260804.zip",
        "zip_sha256": "73F83B2D28BB8D68B7E62DF9E08A879DCD030559E1F84C5003CBB6995ABE6772",
        "zip_bytes": 82_940,
        "zip_members": 36,
        "targets": 12,
        "target_dir": "ko",
        "structural": "evidence/structural_index/PRODUCER_STRUCTURAL_INDEX.jsonl",
        "difficulty": "evidence/difficulty_ledger/DIFFICULTY_LEDGER.jsonl",
    },
}

PUBLICATION_DATE = "2026-08-04"
VERSION = "2026-08-04 Korean Papers 1, 5, 7, 41, and 42 unchecked snapshots"
TITLE = "Emmy Noether: Modern LaTeX Working Corpus and Multilingual Translation Readers"
DESCRIPTION = """<h2>Emmy Noether working corpus and multilingual readers</h2>
<p>This record preserves a modern-LaTeX working corpus for Emmy Noether together with multilingual working translations, editable sources, source-control evidence, correction history, and bounded public snapshots.</p>
<p><strong>Start here:</strong> <code>01j_Noether_R823_Full_Cumulative_English_20260722.pdf</code> remains the default preview. The complete represented English working reader, German working source-control reader, Spanish and French cumulative translations, and paired Interslavic readers remain directly accessible with their exact source/evidence archives.</p>
<p><strong>Korean bounded snapshots:</strong> this version adds Papers 1, 5, 7, 41, and 42 as five separately frozen privacy-clean packages. Thirty-nine editable Korean TeX units are direct downloads. Each paper also exposes its current status, checker handoff, translation choices, structural index, and difficulty/failure ledger. The five complete ZIPs preserve all public-safe source, scripts, rejected/failure evidence, validators, source custody, decisions, and continuation surfaces.</p>
<p>The Korean state is deliberately explicit: <strong>UNCHECKED, uncompiled, unrendered, unassembled, and unreviewed</strong>. Those are scope labels rather than release holds. Archive maintenance performed no source correction, compilation, rendering, mathematical review, linguistic review, certification, or approval. Exact raw producer bytes are separately frozen in private custody; public projections replace only private local path/operator tokens. One private P42 coordination screenshot is excluded while its exact identity and exclusion rationale remain recorded.</p>
<p>These are working transcriptions, translations, and audit materials—not critical editions, native-language certifications, peer review, proof checking, mathematical certification, accessibility certification, or blanket rights grants. Corrections should be published through append-only successors with every prior generation and reversal preserved.</p>"""
ADDITIONAL_NOTE = """<p><strong>2026-08-04 Korean snapshot closeout.</strong> Five bounded producer roots contain 173 files / 1,986,208 bytes and 39 Korean TeX units. Their public projections contain five complete ZIPs (35, 29, 45, 47, and 36 members), direct targets, logbooks, structural and difficulty ledgers, the current Korean methodology/logbook controls, and the archive-wide immediate-publication/no-hold policy. P42 has one explicit private screenshot exclusion and zero mathematical image/render bytes. Publication preserves unreviewed work without representing it as reviewed.</p>"""

TEMP_ROOT = (
    Path(os.environ.get("LOCALAPPDATA", os.environ.get("TEMP", ".")))
    / "Temp"
    / "korean_noether_unchecked_20260804"
)
STATE_PATH = TEMP_ROOT / "draft_state.json"


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


def normalized_md5(value: str) -> str:
    return str(value).lower().removeprefix("md5:")


def auth(token: str) -> dict[str, str]:
    return {"Authorization": f"Bearer {token}"}


def auth_modern(token: str) -> dict[str, str]:
    return {**auth(token), **MODERN}


def save_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(value, ensure_ascii=True, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    temporary.replace(path)


def load_state() -> dict | None:
    if not STATE_PATH.is_file():
        return None
    return json.loads(STATE_PATH.read_text(encoding="utf-8"))


def modern_entries(record: dict) -> dict[str, dict]:
    return record.get("files", {}).get("entries", {})


def legacy_entries(record: dict) -> dict[str, dict]:
    return {row["filename"]: row for row in record.get("files", [])}


def modern_identity(row: dict) -> tuple[int, str]:
    return int(row["size"]), normalized_md5(row["checksum"])


def legacy_identity(row: dict) -> tuple[int, str]:
    return int(row["filesize"]), normalized_md5(row["checksum"])


def file_row(path: Path) -> dict:
    return {
        "path": str(path),
        "bytes": path.stat().st_size,
        "sha256": sha256(path),
        "md5": md5(path),
    }


def predecessor_receipt() -> dict:
    receipt = json.loads(PREDECESSOR_RECEIPT.read_text(encoding="utf-8"))
    if (
        receipt.get("status") != "PASS_PUBLISHED_AND_READ_BACK"
        or int(receipt.get("record_id", 0)) != PREDECESSOR_ID
        or receipt.get("conceptdoi") != CONCEPT_DOI
        or int(receipt.get("file_count", 0)) != PREDECESSOR_FILES
        or int(receipt.get("total_bytes", 0)) != PREDECESSOR_BYTES
        or receipt.get("default_preview") != DEFAULT_PREVIEW
        or len(receipt.get("files", {})) != PREDECESSOR_FILES
    ):
        raise RuntimeError("Noether predecessor receipt boundary changed")
    return receipt


def local_surface() -> tuple[dict[str, dict], list[str], dict]:
    validation_path = PUBLIC_ROOT / "SNAPSHOT_VALIDATION.json"
    index_path = PUBLIC_ROOT / "70_KO_P01_P05_P07_P41_P42_SNAPSHOT_INDEX_20260804.csv"
    readme_path = PUBLIC_ROOT / "README.md"
    expected_controls = [
        (validation_path, EXPECTED_ROOT_VALIDATION_BYTES, EXPECTED_ROOT_VALIDATION_SHA256),
        (index_path, EXPECTED_INDEX_BYTES, EXPECTED_INDEX_SHA256),
        (readme_path, EXPECTED_README_BYTES, EXPECTED_README_SHA256),
    ]
    for path, expected_bytes, expected_sha in expected_controls:
        if path.stat().st_size != expected_bytes or sha256(path) != expected_sha:
            raise RuntimeError(f"Korean snapshot root control changed: {path.name}")
    validation = json.loads(validation_path.read_text(encoding="utf-8"))
    if (
        validation.get("status") != "PASS_READY_FOR_SAME_CONCEPT_PUBLICATION"
        or validation.get("errors") != []
        or int(validation.get("total_source_files", 0)) != 173
        or int(validation.get("total_source_bytes", 0)) != 1_986_208
        or int(validation.get("total_target_units", 0)) != 39
        or int(validation.get("total_explicit_exclusions", 0)) != 1
        or validation.get("release_hold") is not False
    ):
        raise RuntimeError("Korean snapshot validation boundary changed")

    surface: dict[str, dict] = {}
    order: list[str] = []

    def add(public_name: str, path: Path) -> None:
        if public_name in surface:
            raise RuntimeError(f"Duplicate Korean public filename: {public_name}")
        surface[public_name] = file_row(path)
        order.append(public_name)

    add(
        "70_KO_P01_P05_P07_P41_P42_READ_ME_FIRST_20260804.md",
        readme_path,
    )
    add(index_path.name, index_path)
    add(
        "70_KO_P01_P05_P07_P41_P42_SNAPSHOT_VALIDATION_20260804.json",
        validation_path,
    )
    for name in [
        "70_KO_ARCHIVE_WIDE_IMMEDIATE_PUBLICATION_NO_HOLD_POLICY_20260804.md",
        "70_KO_ARCHIVE_PUBLICATION_POLICY_RECEIPT_20260804.md",
        "70_KO_CJK_DECISION_LOGBOOK_PRIVACY_CLEAN_20260804.md",
        "70_KO_CJK_PRODUCTION_METHODOLOGY_PRIVACY_CLEAN_20260804.md",
        "70_KO_NOETH_DE_AUTHORITY_POINTER_v003_20260804.json",
        "70_KO_P41_U01_U12_BINDER_20260804.json",
    ]:
        add(name, PUBLIC_ROOT / name)

    for paper, config in PAPERS.items():
        prefix = config["prefix"]
        root = PUBLIC_ROOT / paper
        zip_path = PUBLIC_ROOT / config["zip"]
        if (
            zip_path.stat().st_size != config["zip_bytes"]
            or sha256(zip_path) != config["zip_sha256"]
        ):
            raise RuntimeError(f"Korean {paper} public ZIP identity changed")
        with zipfile.ZipFile(zip_path) as archive:
            if (
                archive.testzip() is not None
                or len([row for row in archive.infolist() if not row.is_dir()])
                != config["zip_members"]
            ):
                raise RuntimeError(f"Korean {paper} public ZIP replay changed")
        add(prefix + "00_COMPLETE_UNCHECKED_PUBLIC_SNAPSHOT_20260804.zip", zip_path)
        add(prefix + "01_STATUS.md", root / "STATUS.md")
        checker = list(root.glob("CHECKER_HANDOFF_*.md"))
        choices = list(root.glob("TRANSLATION_CHOICES_*.md"))
        targets = sorted(
            (root / config["target_dir"]).glob("*.tex"), key=lambda path: path.name
        )
        if len(checker) != 1 or len(choices) != 1 or len(targets) != config["targets"]:
            raise RuntimeError(f"Korean {paper} direct human/target boundary changed")
        add(prefix + "02_CHECKER_HANDOFF.md", checker[0])
        add(prefix + "03_TRANSLATION_CHOICES.md", choices[0])
        for index, target in enumerate(targets, start=1):
            add(prefix + f"10_U{index:02d}_UNCHECKED.tex", target)
        add(prefix + "20_STRUCTURAL_INDEX.jsonl", root / config["structural"])
        add(prefix + "21_DIFFICULTY_LEDGER.jsonl", root / config["difficulty"])
    if len(surface) != EXPECTED_NEW_FILES or len(order) != EXPECTED_NEW_FILES:
        raise RuntimeError(
            f"Korean direct surface count changed: {len(surface)} != {EXPECTED_NEW_FILES}"
        )
    return surface, order, validation


def fetch_live(session) -> dict:
    live = base.check(
        session.get(
            f"{API}/records/{PREDECESSOR_ID}/versions/latest",
            headers=MODERN,
            timeout=(30, 300),
        ),
        {200},
    ).json()
    entries = modern_entries(live)
    observed = (
        int(live["id"]),
        live.get("pids", {}).get("doi", {}).get("identifier"),
        str(live.get("parent", {}).get("id")),
        live.get("parent", {}).get("pids", {}).get("doi", {}).get("identifier"),
        int(live.get("versions", {}).get("index", 0)),
        live.get("versions", {}).get("is_latest"),
        live.get("status"),
        len(entries),
        sum(int(row["size"]) for row in entries.values()),
        live.get("files", {}).get("default_preview"),
    )
    expected = (
        PREDECESSOR_ID,
        PREDECESSOR_DOI,
        CONCEPT_ID,
        CONCEPT_DOI,
        PREDECESSOR_VERSION_INDEX,
        True,
        "published",
        PREDECESSOR_FILES,
        PREDECESSOR_BYTES,
        DEFAULT_PREVIEW,
    )
    if observed != expected:
        raise RuntimeError(f"Live Noether predecessor boundary changed: {observed!r}")
    receipt_files = predecessor_receipt()["files"]
    if set(receipt_files) != set(entries):
        raise RuntimeError("Noether live inherited file set changed")
    for name, row in receipt_files.items():
        if int(row["bytes"]) != int(entries[name]["size"]):
            raise RuntimeError(f"Noether inherited bytes changed: {name}")
    return live


def verify_active_draft(session, token: str) -> dict | None:
    state = load_state()
    probe = session.get(
        f"{API}/records/{PREDECESSOR_ID}/draft",
        headers=auth_modern(token),
        timeout=(30, 180),
    )
    if state is None:
        if probe.status_code == 200:
            raise RuntimeError("Untracked Noether successor draft exists")
        base.check(probe, {404})
        return None
    if state.get("published"):
        if probe.status_code not in {404, 410}:
            raise RuntimeError("Published Korean state conflicts with a draft")
        return state
    if probe.status_code == 200 and int(probe.json()["id"]) != int(state["draft_id"]):
        raise RuntimeError("Noether predecessor-scoped draft identity changed")
    if probe.status_code != 200:
        base.check(probe, {404})
    tracked = base.check(
        session.get(
            f"{API}/records/{int(state['draft_id'])}/draft",
            headers=auth_modern(token),
            timeout=(30, 180),
        ),
        {200},
    ).json()
    if (
        int(tracked["id"]) != int(state["draft_id"])
        or str(tracked.get("parent", {}).get("id")) != CONCEPT_ID
        or tracked.get("is_published") is not False
    ):
        raise RuntimeError("Tracked Korean Noether draft boundary changed")
    return state


def create_or_resume_draft(session, token: str, live: dict) -> tuple[int, bool]:
    state = verify_active_draft(session, token)
    if state is not None:
        if state.get("published"):
            raise RuntimeError("Korean Noether successor is already published")
        return int(state["draft_id"]), False
    predecessor = base.check(
        session.get(
            f"{API}/deposit/depositions/{PREDECESSOR_ID}",
            headers=auth(token),
            timeout=(30, 300),
        ),
        {200},
    ).json()
    if (
        predecessor.get("state") != "done"
        or not predecessor.get("submitted")
        or not predecessor.get("links", {}).get("newversion")
        or str(predecessor.get("conceptrecid")) != CONCEPT_ID
    ):
        raise RuntimeError("Noether predecessor is not a safe versioning base")
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
            created["links"]["latest_draft"],
            headers=auth(token),
            timeout=(30, 300),
        ),
        {200},
    ).json()
    draft_id = int(deposition["id"])
    if set(legacy_entries(deposition)) != set(modern_entries(live)):
        raise RuntimeError("Noether successor did not inherit every file")
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
        or modern.get("versions", {}).get("index") != PREDECESSOR_VERSION_INDEX + 1
        or modern.get("versions", {}).get("is_latest_draft") is not True
    ):
        raise RuntimeError("Created Korean Noether draft left the concept")
    save_json(
        STATE_PATH,
        {
            "status": "OPEN_TRACKED_DRAFT",
            "predecessor_record": PREDECESSOR_ID,
            "concept_id": CONCEPT_ID,
            "concept_doi": CONCEPT_DOI,
            "draft_id": draft_id,
            "published": False,
            "created_at_epoch": int(time.time()),
        },
    )
    return draft_id, True


def desired_order(inherited_order: list[str], new_order: list[str]) -> list[str]:
    expected_inherited = predecessor_receipt().get("configured_file_order")
    if expected_inherited is None:
        expected_inherited = inherited_order
    if set(inherited_order) != set(predecessor_receipt()["files"]):
        raise RuntimeError("Noether inherited order boundary changed")
    order = list(inherited_order)
    anchor = "60_Noether_Bounded_CJK_and_Other_Languages_20260722.zip"
    index = order.index(anchor) + 1
    order[index:index] = new_order
    if len(order) != EXPECTED_RESULTING_FILES or len(order) != len(set(order)):
        raise RuntimeError("Korean Noether resulting order changed")
    return order


def desired_metadata(current: dict) -> dict:
    metadata = copy.deepcopy(current)
    metadata["title"] = TITLE
    metadata["publication_date"] = PUBLICATION_DATE
    metadata["version"] = VERSION
    metadata["description"] = DESCRIPTION
    metadata["additional_descriptions"] = [
        {"description": ADDITIONAL_NOTE, "type": {"id": "notes"}}
    ]
    return metadata


def verify_staged(
    draft: dict,
    live: dict,
    new_surface: dict[str, dict],
    order: list[str],
) -> None:
    entries = modern_entries(draft)
    inherited = modern_entries(live)
    if set(entries) != set(inherited) | set(new_surface):
        raise RuntimeError("Korean Noether staged filename boundary changed")
    errors = []
    for name, row in inherited.items():
        if modern_identity(entries[name]) != modern_identity(row):
            errors.append(name)
    for name, row in new_surface.items():
        if modern_identity(entries[name]) != (int(row["bytes"]), row["md5"]):
            errors.append(name)
    if errors:
        raise RuntimeError(f"Korean Noether staged identity errors: {errors}")
    metadata = draft.get("metadata", {})
    notes = metadata.get("additional_descriptions", [])
    if (
        metadata.get("title") != TITLE
        or metadata.get("publication_date") != PUBLICATION_DATE
        or metadata.get("version") != VERSION
        or metadata.get("description") != DESCRIPTION
        or len(notes) != 1
        or notes[0].get("description") != ADDITIONAL_NOTE
        or draft.get("files", {}).get("default_preview") != DEFAULT_PREVIEW
    ):
        raise RuntimeError("Korean Noether staged metadata/preview changed")
    observed_order = draft.get("files", {}).get("order") or []
    if observed_order not in (order, []):
        raise RuntimeError("Korean Noether file order changed")


def upload_file(session, token: str, bucket: str, name: str, path: Path) -> None:
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
    new_surface, new_order, validation = local_surface()
    live = fetch_live(session)
    state = verify_active_draft(session, token)
    order = desired_order(live["files"].get("order") or list(modern_entries(live)), new_order)
    return {
        "status": "PASS_READY_FOR_ONE_SAME_CONCEPT_SUCCESSOR",
        "concept_id": CONCEPT_ID,
        "concept_doi": CONCEPT_DOI,
        "predecessor_record_id": PREDECESSOR_ID,
        "predecessor_version_doi": PREDECESSOR_DOI,
        "predecessor_version_index": live["versions"]["index"],
        "predecessor_files_preserved": len(modern_entries(live)),
        "predecessor_bytes_preserved": sum(
            int(row["size"]) for row in modern_entries(live).values()
        ),
        "active_draft": state is not None and not state.get("published", False),
        "tracked_draft_id": None if state is None else state.get("draft_id"),
        "new_direct_files": len(new_surface),
        "new_direct_bytes": sum(int(row["bytes"]) for row in new_surface.values()),
        "resulting_files": len(order),
        "source_files": validation["total_source_files"],
        "source_bytes": validation["total_source_bytes"],
        "target_units": validation["total_target_units"],
        "explicit_exclusions": validation["total_explicit_exclusions"],
        "default_preview_retained": DEFAULT_PREVIEW,
        "duplicate_concept_created": False,
        "release_hold": False,
    }


def stage(session, token: str) -> dict:
    new_surface, new_order, validation = local_surface()
    live = fetch_live(session)
    inherited = modern_entries(live)
    order = desired_order(live["files"].get("order") or list(inherited), new_order)
    draft_id, created = create_or_resume_draft(session, token, live)
    deposition = base.check(
        session.get(
            f"{API}/deposit/depositions/{draft_id}",
            headers=auth(token),
            timeout=(30, 300),
        ),
        {200},
    ).json()
    remote = legacy_entries(deposition)
    if set(remote) != set(inherited):
        raise RuntimeError("Tracked Noether draft inherited boundary changed")
    for name, row in inherited.items():
        if legacy_identity(remote[name]) != modern_identity(row):
            raise RuntimeError(f"Inherited Noether file changed in draft: {name}")
    bucket = deposition["links"]["bucket"]
    uploaded = []
    for name in new_order:
        row = new_surface[name]
        upload_file(session, token, bucket, name, Path(row["path"]))
        uploaded.append(name)
    draft = base.check(
        session.get(
            f"{API}/records/{draft_id}/draft",
            headers=auth_modern(token),
            timeout=(30, 600),
        ),
        {200},
    ).json()
    if set(modern_entries(draft)) != set(inherited) | set(new_surface):
        raise RuntimeError("Korean Noether draft incomplete after upload")
    payload = {
        "access": draft["access"],
        "files": {
            "enabled": True,
            "default_preview": DEFAULT_PREVIEW,
            "order": order,
        },
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
    verify_staged(patched, live, new_surface, order)
    state = load_state()
    if state is None or int(state["draft_id"]) != draft_id:
        raise RuntimeError("Tracked Korean Noether state disappeared")
    state.update(
        {
            "status": "STAGED_EXACT_READY_FOR_EXPLICIT_PUBLISH",
            "staged": True,
            "staged_files": len(order),
            "new_files": len(new_surface),
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
        "predecessor_record_id": PREDECESSOR_ID,
        "created_new_same_concept_draft": created,
        "duplicate_concept_created": False,
        "inherited_files_preserved": len(inherited),
        "new_files": len(new_surface),
        "files": len(order),
        "bytes": sum(int(row["size"]) for row in inherited.values())
        + sum(int(row["bytes"]) for row in new_surface.values()),
        "default_preview": DEFAULT_PREVIEW,
        "uploaded_now": uploaded,
        "release_hold": False,
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


def replay_downloaded_zip(path: Path, expected_members: int) -> dict:
    rows = []
    errors = []
    with zipfile.ZipFile(path) as archive:
        bad = archive.testzip()
        if bad is not None:
            errors.append(f"crc:{bad}")
        infos = [row for row in archive.infolist() if not row.is_dir()]
        if len(infos) != expected_members:
            errors.append("member_count")
        for info in infos:
            digest = hashlib.sha256()
            with archive.open(info) as handle:
                for block in iter(lambda: handle.read(4 * 1024 * 1024), b""):
                    digest.update(block)
            rows.append(
                {
                    "relative_path": info.filename,
                    "bytes": info.file_size,
                    "sha256": digest.hexdigest().upper(),
                }
            )
    return {
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "members": len(rows),
        "member_identities": rows,
    }


def publish_and_readback(
    session,
    token: str,
    confirm_draft_id: str,
    receipt_dir: Path,
) -> dict:
    new_surface, new_order, validation = local_surface()
    live = fetch_live(session)
    order = desired_order(live["files"].get("order") or list(modern_entries(live)), new_order)
    state = verify_active_draft(session, token)
    if state is None or state.get("published") or not state.get("staged"):
        raise RuntimeError("No exact staged Korean Noether draft is tracked")
    draft_id = int(state["draft_id"])
    if confirm_draft_id != str(draft_id):
        raise RuntimeError(f"Publishing requires --confirm-publish {draft_id}")
    draft = base.check(
        session.get(
            f"{API}/records/{draft_id}/draft",
            headers=auth_modern(token),
            timeout=(30, 600),
        ),
        {200},
    ).json()
    verify_staged(draft, live, new_surface, order)
    if (
        str(draft.get("parent", {}).get("id")) != CONCEPT_ID
        or draft.get("versions", {}).get("index") != PREDECESSOR_VERSION_INDEX + 1
    ):
        raise RuntimeError("Korean Noether staged lineage changed")
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
    if record_id != draft_id:
        raise RuntimeError("Korean Noether publication returned another record id")
    state.update(
        {
            "status": "PUBLISHED_AWAITING_ANONYMOUS_READBACK",
            "published": True,
            "record_id": record_id,
            "published_at_epoch": int(time.time()),
        }
    )
    save_json(STATE_PATH, state)

    anonymous = base.make_session()
    record = None
    for _ in range(60):
        probe = anonymous.get(
            f"{API}/records/{record_id}", headers=MODERN, timeout=(30, 300)
        )
        if probe.status_code == 200 and probe.json().get("status") == "published":
            record = probe.json()
            break
        time.sleep(2)
    if record is None:
        raise RuntimeError("Korean Noether successor did not become public")
    if (
        str(record.get("parent", {}).get("id")) != CONCEPT_ID
        or record.get("parent", {}).get("pids", {}).get("doi", {}).get("identifier")
        != CONCEPT_DOI
        or record.get("versions", {}).get("index") != PREDECESSOR_VERSION_INDEX + 1
        or record.get("versions", {}).get("is_latest") is not True
    ):
        raise RuntimeError("Published Korean Noether lineage changed")
    verify_staged(record, live, new_surface, order)

    entries = modern_entries(record)
    readback_rows = []
    zip_replays = {}
    errors = []
    temp_downloads = TEMP_ROOT / "public_zip_readback"
    temp_downloads.mkdir(parents=True, exist_ok=True)
    zip_expectations = {
        config["prefix"] + "00_COMPLETE_UNCHECKED_PUBLIC_SNAPSHOT_20260804.zip": config["zip_members"]
        for config in PAPERS.values()
    }
    for index, name in enumerate(new_order, start=1):
        print(f"READBACK {index}/{len(new_order)} {name}", flush=True)
        destination = temp_downloads / name if name in zip_expectations else None
        observed = stream_identity(
            anonymous, entries[name]["links"]["content"], destination
        )
        expected = (int(new_surface[name]["bytes"]), new_surface[name]["sha256"])
        match = observed == expected
        if not match:
            errors.append(name)
        readback_rows.append(
            {
                "filename": name,
                "bytes": observed[0],
                "sha256": observed[1],
                "match": match,
                "content_url": entries[name]["links"]["content"],
            }
        )
        if destination is not None:
            replay = replay_downloaded_zip(destination, zip_expectations[name])
            if replay["status"] != "PASS":
                errors.append(name + ":zip_member_replay")
            zip_replays[name] = replay
            destination.unlink()
    if errors:
        raise RuntimeError(f"Korean Noether public readback errors: {errors}")

    inherited_errors = []
    for name, prior in modern_entries(live).items():
        if modern_identity(entries[name]) != modern_identity(prior):
            inherited_errors.append(name)
    if inherited_errors:
        raise RuntimeError(f"Korean Noether inherited identities changed: {inherited_errors}")
    active = session.get(
        f"{API}/records/{PREDECESSOR_ID}/draft",
        headers=auth_modern(token),
        timeout=(30, 180),
    )
    if active.status_code not in {404, 410}:
        raise RuntimeError("Noether active draft remains after publication")
    result = {
        "status": "PASS_PUBLISHED_SAME_CONCEPT_AND_ANONYMOUS_RAW_READBACK",
        "errors": [],
        "record_id": record_id,
        "record_url": record["links"]["self_html"],
        "version_doi": record["pids"]["doi"]["identifier"],
        "concept_id": CONCEPT_ID,
        "concept_doi": CONCEPT_DOI,
        "predecessor_record_id": PREDECESSOR_ID,
        "predecessor_version_doi": PREDECESSOR_DOI,
        "version_index": record["versions"]["index"],
        "title": record["metadata"]["title"],
        "publication_date": record["metadata"]["publication_date"],
        "version": record["metadata"]["version"],
        "default_preview": record["files"]["default_preview"],
        "files": len(entries),
        "bytes": sum(int(row["size"]) for row in entries.values()),
        "retained_predecessor_files": PREDECESSOR_FILES,
        "retained_predecessor_identity_mismatches": 0,
        "new_direct_files": len(new_surface),
        "new_direct_raw_readback_matches": len(readback_rows),
        "new_direct_raw_readback_mismatches": 0,
        "source_files": validation["total_source_files"],
        "source_bytes": validation["total_source_bytes"],
        "target_units": validation["total_target_units"],
        "explicit_exclusions": validation["total_explicit_exclusions"],
        "state_labels": [
            "UNCHECKED",
            "uncompiled",
            "unrendered",
            "unassembled",
            "unreviewed",
        ],
        "active_draft": False,
        "duplicate_concept_created": False,
        "release_hold": False,
        "new_direct_readback": readback_rows,
        "public_zip_member_replays": zip_replays,
        "configured_file_order": order,
        "api_file_order": record["files"].get("order") or [],
    }
    receipt_path = (
        receipt_dir
        / f"20260804_korean_noether_p01_p05_p07_p41_p42_record_{record_id}_public_readback.json"
    )
    save_json(receipt_path, result)
    result["receipt_path"] = str(receipt_path)
    result["receipt_bytes"] = receipt_path.stat().st_size
    result["receipt_sha256"] = sha256(receipt_path)
    state.update(
        {
            "status": "PASS_PUBLISHED_AND_ANONYMOUS_READBACK",
            "doi": result["version_doi"],
            "record_url": result["record_url"],
            "readback_matches": result["new_direct_raw_readback_matches"],
            "receipt_path": str(receipt_path),
            "readback_completed_at_epoch": int(time.time()),
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
        if key
        not in {
            "new_direct_readback",
            "public_zip_member_replays",
            "configured_file_order",
            "api_file_order",
            "uploaded_now",
        }
    }
    print(json.dumps(summary, ensure_ascii=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
