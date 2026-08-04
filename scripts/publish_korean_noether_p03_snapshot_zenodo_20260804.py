#!/usr/bin/env python3
"""Publish Korean Noether P03 on the existing Noether concept without file loss."""

from __future__ import annotations

import argparse
import copy
import json
import os
import time
import zipfile
from pathlib import Path

import publish_korean_noether_unchecked_snapshots_zenodo_20260804 as prior


base = prior.base
API = prior.API
MODERN = prior.MODERN
CONCEPT_ID = "20412587"
CONCEPT_DOI = "10.5281/zenodo.20412587"
PREDECESSOR_ID = 21783727
PREDECESSOR_DOI = "10.5281/zenodo.21783727"
PREDECESSOR_INDEX = 172
PREDECESSOR_FILES = 98
PREDECESSOR_BYTES = 585_381_337
RESULT_FILES = 100
DEFAULT_PREVIEW = "01j_Noether_R823_Full_Cumulative_English_20260722.pdf"
PUBLICATION_DATE = "2026-08-04"
VERSION = "2026-08-04 Korean Papers 1, 3, 5, 7, 41, and 42 unchecked snapshots"
TITLE = "Emmy Noether: Modern LaTeX Working Corpus and Multilingual Translation Readers"

REPO_ROOT = Path(__file__).resolve().parents[1]
ROOT = REPO_ROOT / "sources" / "noether" / "korean-unchecked-paper-03-20260804"
PREDECESSOR_RECEIPT = (
    REPO_ROOT
    / "manifests"
    / "published-zenodo"
    / "20260804_korean_noether_p01_p05_p07_p41_p42_record_21783727_public_readback.json"
)
TEMP_ROOT = (
    Path(os.environ.get("LOCALAPPDATA", os.environ.get("TEMP", ".")))
    / "Temp"
    / "korean_noether_p03_20260804"
)
STATE_PATH = TEMP_ROOT / "draft_state.json"
EXPECTED_VALIDATION = (
    6_217,
    "063CCDA2804D1165538400C4F9229D79E95E1965394A439F240222452A7CEFA8",
)
EXPECTED_ZIP = (
    128_450,
    "AEB6810B64E5222ABBC57BE28C997FEC335D2E330C01D1321B920FCFEFB6FBD8",
    37,
)

REMOVED_DUPLICATE_LEDGERS = {
    "70a_KO_P01__20_STRUCTURAL_INDEX.jsonl": (
        "70a_KO_P01__00_COMPLETE_UNCHECKED_PUBLIC_SNAPSHOT_20260804.zip",
        "evidence/structural_index/PRODUCER_STRUCTURAL_INDEX.jsonl",
    ),
    "70a_KO_P01__21_DIFFICULTY_LEDGER.jsonl": (
        "70a_KO_P01__00_COMPLETE_UNCHECKED_PUBLIC_SNAPSHOT_20260804.zip",
        "evidence/difficulty_ledger/DIFFICULTY_LEDGER.jsonl",
    ),
    "70b_KO_P05__20_STRUCTURAL_INDEX.jsonl": (
        "70b_KO_P05__00_COMPLETE_UNCHECKED_PUBLIC_SNAPSHOT_20260804.zip",
        "evidence/structural_index/PRODUCER_STRUCTURAL_INDEX.jsonl",
    ),
    "70b_KO_P05__21_DIFFICULTY_LEDGER.jsonl": (
        "70b_KO_P05__00_COMPLETE_UNCHECKED_PUBLIC_SNAPSHOT_20260804.zip",
        "evidence/difficulty/DIFFICULTY_LEDGER.jsonl",
    ),
    "70c_KO_P07__20_STRUCTURAL_INDEX.jsonl": (
        "70c_KO_P07__00_COMPLETE_UNCHECKED_PUBLIC_SNAPSHOT_20260804.zip",
        "reproducibility/structural/STRUCTURAL_INDEX.jsonl",
    ),
    "70c_KO_P07__21_DIFFICULTY_LEDGER.jsonl": (
        "70c_KO_P07__00_COMPLETE_UNCHECKED_PUBLIC_SNAPSHOT_20260804.zip",
        "reproducibility/difficulty/DIFFICULTY_LEDGER.jsonl",
    ),
    "70d_KO_P41__20_STRUCTURAL_INDEX.jsonl": (
        "70d_KO_P41__00_COMPLETE_UNCHECKED_PUBLIC_SNAPSHOT_20260804.zip",
        "evidence/structural_index/PRODUCER_STRUCTURAL_INDEX.jsonl",
    ),
    "70d_KO_P41__21_DIFFICULTY_LEDGER.jsonl": (
        "70d_KO_P41__00_COMPLETE_UNCHECKED_PUBLIC_SNAPSHOT_20260804.zip",
        "evidence/difficulty/difficulty_ledger.jsonl",
    ),
    "70e_KO_P42__20_STRUCTURAL_INDEX.jsonl": (
        "70e_KO_P42__00_COMPLETE_UNCHECKED_PUBLIC_SNAPSHOT_20260804.zip",
        "evidence/structural_index/PRODUCER_STRUCTURAL_INDEX.jsonl",
    ),
    "70e_KO_P42__21_DIFFICULTY_LEDGER.jsonl": (
        "70e_KO_P42__00_COMPLETE_UNCHECKED_PUBLIC_SNAPSHOT_20260804.zip",
        "evidence/difficulty_ledger/DIFFICULTY_LEDGER.jsonl",
    ),
}

DESCRIPTION = """<h2>Emmy Noether working corpus and multilingual readers</h2>
<p>This record preserves a modern-LaTeX working corpus for Emmy Noether together with multilingual working translations, editable sources, source-control evidence, correction history, and bounded public snapshots.</p>
<p><strong>Start here:</strong> <code>01j_Noether_R823_Full_Cumulative_English_20260722.pdf</code> remains the default preview. The complete represented English working reader, German working source-control reader, Spanish and French cumulative translations, paired Interslavic readers, and exact source/evidence archives remain directly accessible.</p>
<p><strong>Korean bounded snapshots:</strong> Papers 1, 3, 5, 7, 41, and 42 are separately frozen privacy-clean packages. Forty-two editable Korean TeX units are direct downloads. Each paper exposes its complete ZIP, status, checker handoff, translation choices, and selected structural/difficulty ledgers. Ten older duplicate direct machine ledgers were compacted from this version only after their exact bytes were proved preserved inside the five predecessor ZIPs and in immutable version 172.</p>
<p>The Korean state is deliberately explicit: <strong>UNCHECKED, uncompiled, unrendered, unassembled, and unreviewed</strong>. Those are scope labels rather than release holds. Archive maintenance performed no source correction, compilation, rendering, mathematical review, linguistic review, certification, or approval. Exact producer bytes are separately frozen in private custody; public projections replace only private local path/operator tokens. P42’s private coordination screenshot remains excluded with its exact identity recorded; P03 has zero exclusions and no image bytes.</p>
<p>These are working transcriptions, translations, and audit materials—not critical editions, native-language certifications, peer review, proof checking, mathematical certification, accessibility certification, or blanket rights grants. Corrections should be published through append-only successors with every prior generation and reversal preserved.</p>"""
NORMALIZED_DESCRIPTION = DESCRIPTION.replace("’", "'")
ADDITIONAL_NOTE = """<p><strong>2026-08-04 Korean P03 closeout.</strong> Paper 3 adds a 33-file / 848,460-byte bounded producer root, three Korean TeX units, 148 structural records, and a 14-entry append-only difficulty/failure chain. Its public ZIP has 37/37 members, privacy substitutions affect only local path/operator tokens, exclusions0, images0, compile/render/review false. Across the six Korean snapshots: 206 producer files / 2,834,668 bytes, 42 target units, and one explicit private P42 screenshot exclusion.</p>"""


def auth(token: str) -> dict[str, str]:
    return prior.auth(token)


def auth_modern(token: str) -> dict[str, str]:
    return prior.auth_modern(token)


def modern_entries(record: dict) -> dict[str, dict]:
    entries = record.get("files", {}).get("entries", [])
    if isinstance(entries, dict):
        return entries
    return {row["key"]: row for row in entries}


def legacy_entries(record: dict) -> dict[str, dict]:
    return prior.legacy_entries(record)


def modern_identity(row: dict) -> tuple[int, str]:
    return prior.modern_identity(row)


def legacy_identity(row: dict) -> tuple[int, str]:
    return prior.legacy_identity(row)


def save_json(path: Path, value: object) -> None:
    prior.save_json(path, value)


def load_state() -> dict | None:
    if not STATE_PATH.exists():
        return None
    return json.loads(STATE_PATH.read_text(encoding="utf-8"))


def predecessor_receipt() -> dict:
    receipt = json.loads(PREDECESSOR_RECEIPT.read_text(encoding="utf-8"))
    if (
        receipt.get("status") != "PASS_PUBLISHED_SAME_CONCEPT_AND_ANONYMOUS_RAW_READBACK"
        or int(receipt.get("record_id", 0)) != PREDECESSOR_ID
        or receipt.get("concept_doi") != CONCEPT_DOI
        or int(receipt.get("files", 0)) != PREDECESSOR_FILES
        or int(receipt.get("bytes", 0)) != PREDECESSOR_BYTES
        or receipt.get("default_preview") != DEFAULT_PREVIEW
        or len(receipt.get("new_direct_readback", [])) != 78
    ):
        raise RuntimeError("Korean P03 predecessor receipt boundary changed")
    return receipt


def local_surface() -> tuple[dict[str, dict], list[str], dict]:
    validation_path = ROOT / "SNAPSHOT_VALIDATION.json"
    if (validation_path.stat().st_size, prior.sha256(validation_path)) != EXPECTED_VALIDATION:
        raise RuntimeError("P03 snapshot validation identity changed")
    validation = json.loads(validation_path.read_text(encoding="utf-8"))
    if validation.get("status") != "PASS_READY_FOR_SAME_CONCEPT_PUBLICATION" or validation.get("errors") != []:
        raise RuntimeError("P03 snapshot validation is not PASS/errors[]")
    if (
        validation.get("public_root_files_excluding_this_validation") != 45
        or validation.get("public_root_bytes_excluding_this_validation") != 1_763_130
        or validation.get("total_source_files") != 33
        or validation.get("total_source_bytes") != 848_460
        or validation.get("total_target_units") != 3
        or validation.get("total_explicit_exclusions") != 0
    ):
        raise RuntimeError("P03 snapshot closeout boundary changed")
    zip_path = ROOT / "P03_Korean_UNCHECKED_Public_Snapshot_20260804.zip"
    if (zip_path.stat().st_size, prior.sha256(zip_path)) != EXPECTED_ZIP[:2]:
        raise RuntimeError("P03 public ZIP identity changed")
    with zipfile.ZipFile(zip_path) as archive:
        if archive.testzip() is not None or len([x for x in archive.infolist() if not x.is_dir()]) != EXPECTED_ZIP[2]:
            raise RuntimeError("P03 public ZIP replay changed")

    p03 = ROOT / "P03"
    checker = list(p03.glob("CHECKER_HANDOFF_*.md"))
    choices = list(p03.glob("TRANSLATION_CHOICES_*.md"))
    targets = sorted((p03 / "targets").glob("*.tex"), key=lambda path: path.name)
    if len(checker) != 1 or len(choices) != 1 or len(targets) != 3:
        raise RuntimeError("P03 human/target surface changed")
    rows = [
        ("70_KO_CJK_DECISION_LOGBOOK_PRIVACY_CLEAN_20260804.md", ROOT / "70_KO_CJK_DECISION_LOGBOOK_PRIVACY_CLEAN_20260804.md"),
        ("70_KO_CJK_PRODUCTION_METHODOLOGY_PRIVACY_CLEAN_20260804.md", ROOT / "70_KO_CJK_PRODUCTION_METHODOLOGY_PRIVACY_CLEAN_20260804.md"),
        ("70f_KO_P03__00_COMPLETE_UNCHECKED_PUBLIC_SNAPSHOT_20260804.zip", zip_path),
        ("70f_KO_P03__01_STATUS.md", p03 / "STATUS.md"),
        ("70f_KO_P03__02_CHECKER_HANDOFF.md", checker[0]),
        ("70f_KO_P03__03_TRANSLATION_CHOICES.md", choices[0]),
    ]
    rows.extend(
        (f"70f_KO_P03__10_U{index:02d}_UNCHECKED.tex", path)
        for index, path in enumerate(targets, start=1)
    )
    rows.extend(
        [
            ("70f_KO_P03__20_STRUCTURAL_INDEX.jsonl", p03 / "evidence/structural_index/PRODUCER_STRUCTURAL_INDEX.jsonl"),
            ("70f_KO_P03__21_DIFFICULTY_LEDGER.jsonl", p03 / "evidence/difficulty/difficulty_ledger.jsonl"),
            ("70f_KO_P03__90_README.md", ROOT / "README.md"),
            ("70f_KO_P03__91_SNAPSHOT_INDEX.csv", ROOT / "70f_KO_P03_SNAPSHOT_INDEX_20260804.csv"),
            ("70f_KO_P03__92_SNAPSHOT_VALIDATION.json", validation_path),
        ]
    )
    surface = {
        name: {
            "path": str(path),
            "bytes": path.stat().st_size,
            "sha256": prior.sha256(path),
            "md5": prior.md5(path),
        }
        for name, path in rows
    }
    if len(surface) != 14:
        raise RuntimeError("P03 new/replacement direct surface count changed")
    order = [name for name, _ in rows]
    return surface, order, validation


def prove_removed_ledgers_preserved() -> list[dict]:
    receipt = predecessor_receipt()
    direct = {
        row["filename"]: (int(row["bytes"]), row["sha256"])
        for row in receipt["new_direct_readback"]
    }
    zips = receipt["public_zip_member_replays"]
    proofs = []
    for direct_name, (zip_name, member_path) in REMOVED_DUPLICATE_LEDGERS.items():
        members = {
            row["relative_path"]: (int(row["bytes"]), row["sha256"])
            for row in zips[zip_name]["member_identities"]
        }
        if direct.get(direct_name) != members.get(member_path):
            raise RuntimeError(f"Direct-ledger-to-ZIP proof changed: {direct_name}")
        proofs.append(
            {
                "removed_direct_filename": direct_name,
                "preserved_zip": zip_name,
                "preserved_member": member_path,
                "bytes": direct[direct_name][0],
                "sha256": direct[direct_name][1],
                "prior_version": PREDECESSOR_DOI,
            }
        )
    return proofs


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
    if (
        int(live["id"]) != PREDECESSOR_ID
        or live["pids"]["doi"]["identifier"] != PREDECESSOR_DOI
        or str(live.get("parent", {}).get("id")) != CONCEPT_ID
        or live.get("parent", {}).get("pids", {}).get("doi", {}).get("identifier") != CONCEPT_DOI
        or int(live.get("versions", {}).get("index", 0)) != PREDECESSOR_INDEX
        or live.get("versions", {}).get("is_latest") is not True
        or live.get("status") != "published"
        or len(entries) != PREDECESSOR_FILES
        or sum(int(row["size"]) for row in entries.values()) != PREDECESSOR_BYTES
        or live.get("files", {}).get("default_preview") != DEFAULT_PREVIEW
    ):
        raise RuntimeError("Live Noether predecessor boundary changed before P03")
    return live


def verify_active_draft(session, token: str, live: dict) -> dict | None:
    state = load_state()
    probe = session.get(
        f"{API}/records/{PREDECESSOR_ID}/draft",
        headers=auth_modern(token),
        timeout=(30, 180),
    )
    if state is None:
        if probe.status_code == 200:
            raise RuntimeError(f"Untracked Noether draft exists: {probe.json().get('id')}")
        base.check(probe, {404, 410})
        return None
    if state.get("published"):
        if probe.status_code not in {404, 410}:
            raise RuntimeError("Published P03 state conflicts with active draft")
        return state
    draft_id = int(state["draft_id"])
    tracked = base.check(
        session.get(
            f"{API}/records/{draft_id}/draft",
            headers=auth_modern(token),
            timeout=(30, 180),
        ),
        {200},
    ).json()
    if str(tracked.get("parent", {}).get("id")) != CONCEPT_ID or tracked.get("is_published") is not False:
        raise RuntimeError("Tracked P03 draft boundary changed")
    return state


def create_or_resume(session, token: str, live: dict) -> tuple[int, bool]:
    state = verify_active_draft(session, token, live)
    if state is not None:
        if state.get("published"):
            raise RuntimeError("P03 successor is already published")
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
        or str(predecessor.get("conceptrecid")) != CONCEPT_ID
        or not predecessor.get("links", {}).get("newversion")
    ):
        raise RuntimeError("Noether P03 predecessor is not a safe versioning base")
    created = base.check(
        session.post(predecessor["links"]["newversion"], headers=auth(token), timeout=(30, 600)),
        {201},
    ).json()
    deposition = base.check(
        session.get(created["links"]["latest_draft"], headers=auth(token), timeout=(30, 300)),
        {200},
    ).json()
    draft_id = int(deposition["id"])
    if set(legacy_entries(deposition)) != set(modern_entries(live)):
        raise RuntimeError("P03 successor did not inherit all predecessor files")
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


def desired_order(current: list[str], new_order: list[str]) -> list[str]:
    order = [name for name in current if name not in REMOVED_DUPLICATE_LEDGERS]
    anchor = "70e_KO_P42__10_U12_UNCHECKED.tex"
    index = order.index(anchor) + 1
    p03_additions = [name for name in new_order if name.startswith("70f_")]
    order[index:index] = p03_additions
    if len(order) != RESULT_FILES or len(order) != len(set(order)):
        raise RuntimeError("P03 resulting file order changed")
    return order


def verify_staged(draft: dict, live: dict, surface: dict[str, dict], order: list[str]) -> None:
    entries = modern_entries(draft)
    inherited = modern_entries(live)
    expected_names = (set(inherited) - set(REMOVED_DUPLICATE_LEDGERS)) | set(surface)
    if set(entries) != expected_names or len(entries) != RESULT_FILES:
        raise RuntimeError("P03 staged filename closure changed")
    errors = []
    for name in expected_names - set(surface):
        if modern_identity(entries[name]) != modern_identity(inherited[name]):
            errors.append(name)
    for name, row in surface.items():
        if modern_identity(entries[name]) != (int(row["bytes"]), row["md5"]):
            errors.append(name)
    if errors:
        raise RuntimeError(f"P03 staged identity errors: {errors}")
    metadata = draft.get("metadata", {})
    notes = metadata.get("additional_descriptions", [])
    if (
        metadata.get("title") != TITLE
        or metadata.get("publication_date") != PUBLICATION_DATE
        or metadata.get("version") != VERSION
        or metadata.get("description") not in {DESCRIPTION, NORMALIZED_DESCRIPTION}
        or len(notes) != 1
        or notes[0].get("description") != ADDITIONAL_NOTE
        or draft.get("files", {}).get("default_preview") != DEFAULT_PREVIEW
    ):
        raise RuntimeError("P03 staged metadata/default preview changed")
    observed_order = draft.get("files", {}).get("order") or []
    if observed_order not in (order, []):
        raise RuntimeError("P03 configured order changed")


def preflight(session, token: str) -> dict:
    surface, new_order, validation = local_surface()
    proofs = prove_removed_ledgers_preserved()
    live = fetch_live(session)
    state = verify_active_draft(session, token, live)
    order = desired_order(predecessor_receipt()["configured_file_order"], new_order)
    return {
        "status": "PASS_READY_FOR_ONE_P03_SAME_CONCEPT_SUCCESSOR",
        "concept_id": CONCEPT_ID,
        "concept_doi": CONCEPT_DOI,
        "predecessor_record_id": PREDECESSOR_ID,
        "predecessor_version_doi": PREDECESSOR_DOI,
        "predecessor_version_index": PREDECESSOR_INDEX,
        "predecessor_files": PREDECESSOR_FILES,
        "active_draft": state is not None and not state.get("published", False),
        "tracked_draft_id": None if state is None else state.get("draft_id"),
        "new_or_replaced_direct_files": len(surface),
        "deduplicated_direct_ledgers": len(proofs),
        "deduplicated_bytes_preserved_in_zip": sum(int(row["bytes"]) for row in proofs),
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
    surface, new_order, _ = local_surface()
    proofs = prove_removed_ledgers_preserved()
    live = fetch_live(session)
    order = desired_order(predecessor_receipt()["configured_file_order"], new_order)
    draft_id, created = create_or_resume(session, token, live)
    deposition = base.check(
        session.get(f"{API}/deposit/depositions/{draft_id}", headers=auth(token), timeout=(30, 300)),
        {200},
    ).json()
    remote = legacy_entries(deposition)
    deleted = []
    for name, row in list(remote.items()):
        wanted = surface.get(name)
        if name not in REMOVED_DUPLICATE_LEDGERS and (
            wanted is None or legacy_identity(row) == (int(wanted["bytes"]), wanted["md5"])
        ):
            continue
        base.check(session.delete(row["links"]["self"], headers=auth(token), timeout=(30, 300)), {204})
        deleted.append(name)
    deposition = base.check(
        session.get(f"{API}/deposit/depositions/{draft_id}", headers=auth(token), timeout=(30, 300)),
        {200},
    ).json()
    remote = legacy_entries(deposition)
    uploaded = []
    for name in new_order:
        row = surface[name]
        if name in remote:
            continue
        prior.upload_file(session, token, deposition["links"]["bucket"], name, Path(row["path"]))
        uploaded.append(name)
    draft = base.check(
        session.get(f"{API}/records/{draft_id}/draft", headers=auth_modern(token), timeout=(30, 600)),
        {200},
    ).json()
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
    verify_staged(patched, live, surface, order)
    state = load_state()
    state.update({"status": "STAGED_EXACT_READY_FOR_EXPLICIT_PUBLISH", "staged": True, "staged_at_epoch": int(time.time())})
    save_json(STATE_PATH, state)
    return {
        "status": "STAGED_EXACT_READY_FOR_EXPLICIT_PUBLISH",
        "draft_id": draft_id,
        "draft_url": patched.get("links", {}).get("self_html"),
        "concept_doi": CONCEPT_DOI,
        "predecessor_record_id": PREDECESSOR_ID,
        "created_new_same_concept_draft": created,
        "deleted_files": deleted,
        "uploaded_files": uploaded,
        "deduplicated_direct_ledgers": len(proofs),
        "files": RESULT_FILES,
        "bytes": sum(int(row["size"]) for row in modern_entries(patched).values()),
        "default_preview": DEFAULT_PREVIEW,
        "duplicate_concept_created": False,
        "release_hold": False,
    }


def publish_and_readback(session, token: str, confirm: str, receipt_dir: Path) -> dict:
    surface, new_order, validation = local_surface()
    proofs = prove_removed_ledgers_preserved()
    live = fetch_live(session)
    order = desired_order(predecessor_receipt()["configured_file_order"], new_order)
    state = verify_active_draft(session, token, live)
    if state is None or state.get("published") or not state.get("staged"):
        raise RuntimeError("No exact staged P03 draft is tracked")
    draft_id = int(state["draft_id"])
    if confirm != str(draft_id):
        raise RuntimeError(f"Publishing requires --confirm-publish {draft_id}")
    draft = base.check(
        session.get(f"{API}/records/{draft_id}/draft", headers=auth_modern(token), timeout=(30, 600)),
        {200},
    ).json()
    verify_staged(draft, live, surface, order)
    if int(draft.get("versions", {}).get("index", 0)) != PREDECESSOR_INDEX + 1:
        raise RuntimeError("P03 staged version index changed")
    response = base.check(
        session.post(draft["links"]["publish"], headers=auth_modern(token), timeout=(30, 1200)),
        {200, 202},
    )
    try:
        record_id = int(response.json().get("id", draft_id))
    except Exception:
        record_id = draft_id
    anonymous = base.make_session()
    record = None
    for _ in range(60):
        probe = anonymous.get(f"{API}/records/{record_id}", headers=MODERN, timeout=(30, 300))
        if probe.status_code == 200 and probe.json().get("status") == "published":
            record = probe.json()
            break
        time.sleep(2)
    if record is None:
        raise RuntimeError("P03 successor did not become public")
    verify_staged(record, live, surface, order)
    if (
        str(record.get("parent", {}).get("id")) != CONCEPT_ID
        or record.get("versions", {}).get("is_latest") is not True
        or int(record.get("versions", {}).get("index", 0)) != PREDECESSOR_INDEX + 1
    ):
        raise RuntimeError("Published P03 lineage changed")
    entries = modern_entries(record)
    readback = []
    errors = []
    temp_zip = TEMP_ROOT / "P03_public_readback.zip"
    temp_zip.parent.mkdir(parents=True, exist_ok=True)
    zip_name = "70f_KO_P03__00_COMPLETE_UNCHECKED_PUBLIC_SNAPSHOT_20260804.zip"
    for index, name in enumerate(new_order, start=1):
        print(f"READBACK {index}/{len(new_order)} {name}", flush=True)
        destination = temp_zip if name == zip_name else None
        observed = prior.stream_identity(anonymous, entries[name]["links"]["content"], destination)
        expected = (int(surface[name]["bytes"]), surface[name]["sha256"])
        match = observed == expected
        if not match:
            errors.append(name)
        readback.append({"filename": name, "bytes": observed[0], "sha256": observed[1], "match": match, "content_url": entries[name]["links"]["content"]})
    zip_replay = prior.replay_downloaded_zip(temp_zip, EXPECTED_ZIP[2])
    temp_zip.unlink()
    if zip_replay["status"] != "PASS":
        errors.append(zip_name + ":member_replay")
    inherited_errors = []
    inherited = modern_entries(live)
    for name in (set(entries) - set(surface)):
        if modern_identity(entries[name]) != modern_identity(inherited[name]):
            inherited_errors.append(name)
    if inherited_errors:
        errors.extend(inherited_errors)
    if errors:
        raise RuntimeError(f"P03 public readback errors: {errors}")
    active = session.get(f"{API}/records/{PREDECESSOR_ID}/draft", headers=auth_modern(token), timeout=(30, 180))
    if active.status_code not in {404, 410}:
        raise RuntimeError("Noether active draft remains after P03 publication")
    result = {
        "status": "PASS_PUBLISHED_P03_SAME_CONCEPT_AND_ANONYMOUS_RAW_READBACK",
        "errors": [],
        "record_id": record_id,
        "record_url": record["links"]["self_html"],
        "version_doi": record["pids"]["doi"]["identifier"],
        "concept_id": CONCEPT_ID,
        "concept_doi": CONCEPT_DOI,
        "predecessor_record_id": PREDECESSOR_ID,
        "predecessor_version_doi": PREDECESSOR_DOI,
        "version_index": int(record["versions"]["index"]),
        "title": record["metadata"]["title"],
        "publication_date": record["metadata"]["publication_date"],
        "version": record["metadata"]["version"],
        "default_preview": record["files"]["default_preview"],
        "files": len(entries),
        "bytes": sum(int(row["size"]) for row in entries.values()),
        "retained_predecessor_direct_files": len(entries) - len(surface),
        "retained_predecessor_identity_mismatches": 0,
        "new_or_replaced_direct_files": len(surface),
        "new_or_replaced_raw_readback_matches": len(readback),
        "new_or_replaced_raw_readback_mismatches": 0,
        "p03_public_zip_members": zip_replay["members"],
        "p03_public_zip_member_errors": [],
        "deduplicated_direct_ledger_proofs": proofs,
        "source_files": validation["total_source_files"],
        "source_bytes": validation["total_source_bytes"],
        "target_units": validation["total_target_units"],
        "explicit_exclusions": validation["total_explicit_exclusions"],
        "state_labels": ["UNCHECKED", "uncompiled", "unrendered", "unassembled", "unreviewed"],
        "active_draft": False,
        "duplicate_concept_created": False,
        "release_hold": False,
        "readback": readback,
        "p03_public_zip_member_replay": zip_replay,
        "configured_file_order": order,
        "api_file_order": record["files"].get("order") or [],
    }
    receipt_path = receipt_dir / f"20260804_korean_noether_p03_record_{record_id}_public_readback.json"
    save_json(receipt_path, result)
    result["receipt_path"] = str(receipt_path)
    result["receipt_bytes"] = receipt_path.stat().st_size
    result["receipt_sha256"] = prior.sha256(receipt_path)
    state.update({"status": "PASS_PUBLISHED_AND_ANONYMOUS_READBACK", "published": True, "record_id": record_id, "doi": result["version_doi"], "receipt_path": str(receipt_path), "completed_at_epoch": int(time.time())})
    save_json(STATE_PATH, state)
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=("preflight", "stage", "publish"))
    parser.add_argument("--confirm-publish")
    parser.add_argument("--receipt-dir", type=Path, default=REPO_ROOT / "manifests" / "published-zenodo")
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
        result = publish_and_readback(session, token, args.confirm_publish, args.receipt_dir.resolve())
    summary = {key: value for key, value in result.items() if key not in {"readback", "p03_public_zip_member_replay", "configured_file_order", "api_file_order", "deduplicated_direct_ledger_proofs", "deleted_files", "uploaded_files"}}
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
