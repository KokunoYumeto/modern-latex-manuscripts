#!/usr/bin/env python3
"""Publish the exact Korean Noether P04 T07 tranche on the existing concept."""

from __future__ import annotations

import argparse
import json
import os
import time
import zipfile
from pathlib import Path

import publish_korean_noether_p03_snapshot_zenodo_20260804 as engine


base = engine.base
API = engine.API
MODERN = engine.MODERN
REPO_ROOT = Path(__file__).resolve().parents[1]
ROOT = REPO_ROOT / "sources" / "noether" / "korean-unchecked-paper-04-t07-20260804"
PREDECESSOR_RECEIPT = (
    REPO_ROOT
    / "manifests"
    / "published-zenodo"
    / "20260804_korean_noether_p03_p04_record_21784616_public_readback.json"
)
STATE_PATH = (
    Path(os.environ.get("LOCALAPPDATA", os.environ.get("TEMP", ".")))
    / "Temp"
    / "korean_noether_p04_t07_20260804"
    / "draft_state.json"
)

CONCEPT_ID = "20412587"
CONCEPT_DOI = "10.5281/zenodo.20412587"
PREDECESSOR_ID = 21784616
PREDECESSOR_DOI = "10.5281/zenodo.21784616"
PREDECESSOR_INDEX = 173
PREDECESSOR_FILES = 66
PREDECESSOR_BYTES = 584_767_203
RESULT_FILES = 74
DEFAULT_PREVIEW = "01j_Noether_R823_Full_Cumulative_English_20260722.pdf"
VERSION = "2026-08-04 Korean Papers 1, 3, 4 (T04-T07), 5, 7, 41, and 42 snapshots"
TITLE = "Emmy Noether: Modern LaTeX Working Corpus and Multilingual Translation Readers"

DESCRIPTION = """<h2>Emmy Noether working corpus and multilingual readers</h2>
<p>This record preserves a modern-LaTeX working corpus for Emmy Noether together with multilingual working translations, editable sources, source-control evidence, correction history, and bounded public snapshots.</p>
<p><strong>Start here:</strong> <code>01j_Noether_R823_Full_Cumulative_English_20260722.pdf</code> remains the default preview. The represented English working reader, German working source-control reader, Spanish and French cumulative translations, paired Interslavic readers, and exact source/evidence archives remain directly accessible.</p>
<p><strong>Korean bounded snapshots:</strong> Papers 1, 3, 5, 7, 41, and 42 have separately frozen public packages. Paper 4 now preserves T04-T07 / U17-U38 in two exact tranches. Across these surfaces, 64 editable Korean TeX units are preserved. Status, checker, translation-choice, source-custody, and root validation surfaces are direct; mathematical TeX and machine ledgers are organized inside each exact complete ZIP.</p>
<p>The Korean state is deliberately explicit: <strong>UNCHECKED, uncompiled, unrendered, unassembled, and unreviewed</strong>; Paper 4 is also <strong>incomplete</strong>. These are scope labels, not release holds. Archive maintenance performed no source correction, compilation, rendering, mathematical review, linguistic review, certification, or approval.</p>
<p>Forty-nine formerly direct duplicate TeX/ledger objects from the five earlier Korean snapshots remain public byte-for-byte inside their five complete ZIPs and direct in immutable version 172. This is transport organization, not content deletion. Exact producer bytes are separately frozen in private custody; public projections replace only private local path/operator tokens. P42's private coordination screenshot remains excluded with its identity recorded. The current 73-file Paper 4 producer root is privately frozen; the T07 publication selects only its exact ten-file handoff and inventories the other 63 files without deleting them.</p>
<p>These are working transcriptions, translations, and audit materials-not critical editions, native-language certifications, peer review, proof checking, mathematical certification, accessibility certification, or blanket rights grants. Corrections should be published through append-only successors with every prior generation and reversal preserved.</p>"""
NORMALIZED_DESCRIPTION = DESCRIPTION.replace("’", "'")
ADDITIONAL_NOTE = """<p><strong>2026-08-04 Korean P04 T07 closeout.</strong> T07 adds the exact ten-file / 23,476-byte handoff, six Korean TeX units, authority lines 4162-4303, blank line 4304 excluded, and next cursor 4305. Its public ZIP replays 14/14 members. The contemporaneous Paper 4 root had 73 files / 1,749,535 bytes; all 63 files outside this tranche were hash-inventoried and privately frozen. Across all admitted Korean surfaces: 236 producer files / 2,904,024 bytes and 64 target units. Privacy substitutions affect only local path/operator tokens; no compile, render, assembly, review, or release hold.</p>"""

EXPECTED_VALIDATION = (
    3_071,
    "3B1A84ACA62011B58769679E33EA32F53CA4BD3060BFFBD73C00E7CDA4DE30C7",
)
EXPECTED_ZIP = (
    20_682,
    "D94F4DA845109386C327EC3DF5FCFE109353C1E3D6DA0D6E841F18025A37404D",
    14,
)


def file_row(path: Path) -> dict:
    return {
        "path": str(path),
        "bytes": path.stat().st_size,
        "sha256": engine.prior.sha256(path),
        "md5": engine.prior.md5(path),
    }


def predecessor_receipt() -> dict:
    receipt = json.loads(PREDECESSOR_RECEIPT.read_text(encoding="utf-8"))
    if (
        receipt.get("status")
        != "PASS_PUBLISHED_P03_P04_SAME_CONCEPT_AND_ANONYMOUS_RAW_READBACK"
        or int(receipt.get("record_id", 0)) != PREDECESSOR_ID
        or receipt.get("version_doi") != PREDECESSOR_DOI
        or receipt.get("concept_doi") != CONCEPT_DOI
        or int(receipt.get("version_index", 0)) != PREDECESSOR_INDEX
        or int(receipt.get("files", 0)) != PREDECESSOR_FILES
        or int(receipt.get("bytes", 0)) != PREDECESSOR_BYTES
        or receipt.get("default_preview") != DEFAULT_PREVIEW
        or len(receipt.get("configured_file_order", [])) != PREDECESSOR_FILES
    ):
        raise RuntimeError("Korean P04 T07 predecessor receipt boundary changed")
    return receipt


def local_surface() -> tuple[dict[str, dict], list[str], dict]:
    validation_path = ROOT / "SNAPSHOT_VALIDATION.json"
    if (validation_path.stat().st_size, engine.prior.sha256(validation_path)) != EXPECTED_VALIDATION:
        raise RuntimeError("P04 T07 closeout identity changed")
    validation = json.loads(validation_path.read_text(encoding="utf-8"))
    tranche = validation.get("tranche_validation", {})
    if (
        validation.get("status") != "PASS_READY_FOR_SAME_CONCEPT_PUBLICATION"
        or validation.get("errors") != []
        or tranche.get("status") != "PASS_PUBLIC_UNCHECKED_INCOMPLETE_TRANCHE"
        or tranche.get("errors") != []
        or int(tranche.get("selected_source_files", 0)) != 10
        or int(tranche.get("selected_source_bytes", 0)) != 23_476
        or int(tranche.get("target_units", 0)) != 6
        or int(tranche.get("full_producer_root_files", 0)) != 73
        or int(tranche.get("full_producer_root_bytes", 0)) != 1_749_535
        or int(tranche.get("out_of_tranche_files", 0)) != 63
        or validation.get("release_hold") is not False
    ):
        raise RuntimeError("P04 T07 validation boundary changed")

    zip_path = ROOT / "P04_T07_Korean_UNCHECKED_Public_Snapshot_20260804.zip"
    if (zip_path.stat().st_size, engine.prior.sha256(zip_path)) != EXPECTED_ZIP[:2]:
        raise RuntimeError("P04 T07 public ZIP identity changed")
    with zipfile.ZipFile(zip_path) as archive:
        members = [row for row in archive.infolist() if not row.is_dir()]
        if archive.testzip() is not None or len(members) != EXPECTED_ZIP[2]:
            raise RuntimeError("P04 T07 public ZIP replay changed")

    p04 = ROOT / "P04_T07"
    rows = [
        (
            "70_KO_CJK_DECISION_LOGBOOK_PRIVACY_CLEAN_20260804.md",
            ROOT / "70_KO_CJK_DECISION_LOGBOOK_PRIVACY_CLEAN_20260804.md",
        ),
        (
            "70_KO_NOETH_DE_AUTHORITY_POINTER_v004_20260804.json",
            ROOT / "70_KO_NOETH_DE_AUTHORITY_POINTER_v004_20260804.json",
        ),
        (
            "70h_KO_P04_T07__00_COMPLETE_UNCHECKED_PUBLIC_SNAPSHOT_20260804.zip",
            zip_path,
        ),
        ("70h_KO_P04_T07__01_STATUS.md", p04 / "STATUS_T07.md"),
        (
            "70h_KO_P04_T07__02_CHECKER_HANDOFF.md",
            p04 / "CHECKER_HANDOFF_T07_U33_U38.md",
        ),
        (
            "70h_KO_P04_T07__03_TRANSLATION_CHOICES.md",
            p04 / "TRANSLATION_CHOICES_T07.md",
        ),
        ("70h_KO_P04_T07__04_SOURCE_CUSTODY.md", p04 / "SOURCE_CUSTODY_T07.md"),
        ("70h_KO_P04_T07__90_README.md", ROOT / "README.md"),
        (
            "70h_KO_P04_T07__91_SNAPSHOT_INDEX.csv",
            ROOT / "70h_KO_P04_T07_SNAPSHOT_INDEX_20260804.csv",
        ),
        ("70h_KO_P04_T07__92_SNAPSHOT_VALIDATION.json", validation_path),
    ]
    surface = {name: file_row(path) for name, path in rows}
    if len(surface) != 10:
        raise RuntimeError("P04 T07 direct surface count changed")
    return surface, [name for name, _ in rows], validation


def prove_removed_ledgers_preserved() -> list[dict]:
    return []


def desired_order(current: list[str], new_order: list[str]) -> list[str]:
    order = list(current)
    additions = [name for name in new_order if name.startswith("70h_")]
    anchor = order.index("70g_KO_P04_T04_T06__92_SNAPSHOT_VALIDATION.json") + 1
    order[anchor:anchor] = additions
    if len(order) != RESULT_FILES or len(order) != len(set(order)):
        raise RuntimeError(f"P04 T07 resulting order changed: {len(order)}")
    return order


def configure_engine() -> None:
    engine.CONCEPT_ID = CONCEPT_ID
    engine.CONCEPT_DOI = CONCEPT_DOI
    engine.PREDECESSOR_ID = PREDECESSOR_ID
    engine.PREDECESSOR_DOI = PREDECESSOR_DOI
    engine.PREDECESSOR_INDEX = PREDECESSOR_INDEX
    engine.PREDECESSOR_FILES = PREDECESSOR_FILES
    engine.PREDECESSOR_BYTES = PREDECESSOR_BYTES
    engine.RESULT_FILES = RESULT_FILES
    engine.DEFAULT_PREVIEW = DEFAULT_PREVIEW
    engine.PUBLICATION_DATE = "2026-08-04"
    engine.VERSION = VERSION
    engine.TITLE = TITLE
    engine.DESCRIPTION = DESCRIPTION
    engine.NORMALIZED_DESCRIPTION = NORMALIZED_DESCRIPTION
    engine.ADDITIONAL_NOTE = ADDITIONAL_NOTE
    engine.PREDECESSOR_RECEIPT = PREDECESSOR_RECEIPT
    engine.STATE_PATH = STATE_PATH
    engine.REMOVED_DUPLICATE_LEDGERS = {}
    engine.predecessor_receipt = predecessor_receipt
    engine.local_surface = local_surface
    engine.prove_removed_ledgers_preserved = prove_removed_ledgers_preserved
    engine.desired_order = desired_order


def preflight(session, token: str) -> dict:
    surface, new_order, validation = local_surface()
    live = engine.fetch_live(session)
    state = engine.verify_active_draft(session, token, live)
    order = desired_order(predecessor_receipt()["configured_file_order"], new_order)
    return {
        "status": "PASS_READY_FOR_ONE_P04_T07_SAME_CONCEPT_SUCCESSOR",
        "concept_id": CONCEPT_ID,
        "concept_doi": CONCEPT_DOI,
        "predecessor_record_id": PREDECESSOR_ID,
        "predecessor_version_doi": PREDECESSOR_DOI,
        "predecessor_version_index": PREDECESSOR_INDEX,
        "predecessor_files": PREDECESSOR_FILES,
        "predecessor_bytes": PREDECESSOR_BYTES,
        "active_draft": state is not None and not state.get("published", False),
        "tracked_draft_id": None if state is None else state.get("draft_id"),
        "new_or_replaced_direct_files": len(surface),
        "new_direct_filenames": len(set(surface) - set(engine.modern_entries(live))),
        "resulting_files": len(order),
        "selected_source_files": validation["tranche_validation"]["selected_source_files"],
        "selected_source_bytes": validation["tranche_validation"]["selected_source_bytes"],
        "target_units": validation["tranche_validation"]["target_units"],
        "out_of_tranche_files": validation["tranche_validation"]["out_of_tranche_files"],
        "default_preview_retained": DEFAULT_PREVIEW,
        "duplicate_concept_created": False,
        "release_hold": False,
    }


def publish_and_readback(session, token: str, confirm: str, receipt_dir: Path) -> dict:
    surface, new_order, validation = local_surface()
    live = engine.fetch_live(session)
    order = desired_order(predecessor_receipt()["configured_file_order"], new_order)
    state = engine.verify_active_draft(session, token, live)
    if state is None or state.get("published") or not state.get("staged"):
        raise RuntimeError("No exact staged P04 T07 draft is tracked")
    draft_id = int(state["draft_id"])
    if confirm != str(draft_id):
        raise RuntimeError(f"Publishing requires --confirm-publish {draft_id}")
    draft = base.check(
        session.get(
            f"{API}/records/{draft_id}/draft",
            headers=engine.auth_modern(token),
            timeout=(30, 600),
        ),
        {200},
    ).json()
    engine.verify_staged(draft, live, surface, order)
    if int(draft.get("versions", {}).get("index", 0)) != PREDECESSOR_INDEX + 1:
        raise RuntimeError("P04 T07 staged version index changed")

    response = base.check(
        session.post(
            draft["links"]["publish"],
            headers=engine.auth_modern(token),
            timeout=(30, 1200),
        ),
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
        raise RuntimeError("P04 T07 successor did not become public")
    engine.verify_staged(record, live, surface, order)
    if (
        str(record.get("parent", {}).get("id")) != CONCEPT_ID
        or record.get("versions", {}).get("is_latest") is not True
        or int(record.get("versions", {}).get("index", 0)) != PREDECESSOR_INDEX + 1
    ):
        raise RuntimeError("Published P04 T07 lineage changed")

    entries = engine.modern_entries(record)
    zip_name = "70h_KO_P04_T07__00_COMPLETE_UNCHECKED_PUBLIC_SNAPSHOT_20260804.zip"
    download_root = STATE_PATH.parent / "public_zip_readback"
    download_root.mkdir(parents=True, exist_ok=True)
    readback = []
    errors = []
    zip_replay = None
    for index, name in enumerate(new_order, start=1):
        print(f"READBACK {index}/{len(new_order)} {name}", flush=True)
        destination = download_root / name if name == zip_name else None
        observed = engine.prior.stream_identity(
            anonymous, entries[name]["links"]["content"], destination
        )
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
            zip_replay = engine.prior.replay_downloaded_zip(destination, EXPECTED_ZIP[2])
            if zip_replay["status"] != "PASS":
                errors.append(name + ":member_replay")
            destination.unlink()

    inherited = engine.modern_entries(live)
    inherited_errors = [
        name
        for name in (set(entries) - set(surface))
        if engine.modern_identity(entries[name]) != engine.modern_identity(inherited[name])
    ]
    errors.extend(inherited_errors)
    if zip_replay is None:
        errors.append("missing_zip_replay")
    if errors:
        raise RuntimeError(f"P04 T07 public readback errors: {errors}")

    active = session.get(
        f"{API}/records/{PREDECESSOR_ID}/draft",
        headers=engine.auth_modern(token),
        timeout=(30, 180),
    )
    if active.status_code not in {404, 410}:
        raise RuntimeError("Noether active draft remains after P04 T07 publication")

    tranche = validation["tranche_validation"]
    result = {
        "status": "PASS_PUBLISHED_P04_T07_SAME_CONCEPT_AND_ANONYMOUS_RAW_READBACK",
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
        "retained_predecessor_direct_files": len(entries) - len(set(surface) - set(inherited)),
        "retained_predecessor_identity_mismatches": 0,
        "new_or_replaced_direct_files": len(surface),
        "new_or_replaced_raw_readback_matches": len(readback),
        "new_or_replaced_raw_readback_mismatches": 0,
        "public_zip_member_replay": zip_replay,
        "selected_source_files": tranche["selected_source_files"],
        "selected_source_bytes": tranche["selected_source_bytes"],
        "target_units": tranche["target_units"],
        "authority_lines": tranche["authority_lines"],
        "excluded_blank_line": tranche["excluded_blank_line"],
        "next_line": tranche["next_line"],
        "full_producer_root_files": tranche["full_producer_root_files"],
        "full_producer_root_bytes": tranche["full_producer_root_bytes"],
        "full_producer_root_tree_sha256": tranche["full_producer_root_tree_sha256"],
        "out_of_tranche_files": tranche["out_of_tranche_files"],
        "state_labels": [
            "UNCHECKED",
            "incomplete(P04)",
            "uncompiled",
            "unrendered",
            "unassembled",
            "unreviewed",
        ],
        "active_draft": False,
        "duplicate_concept_created": False,
        "release_hold": False,
        "readback": readback,
        "configured_file_order": order,
        "api_file_order": record["files"].get("order") or [],
    }
    receipt_path = (
        receipt_dir
        / f"20260804_korean_noether_p04_t07_record_{record_id}_public_readback.json"
    )
    engine.save_json(receipt_path, result)
    result["receipt_path"] = str(receipt_path)
    result["receipt_bytes"] = receipt_path.stat().st_size
    result["receipt_sha256"] = engine.prior.sha256(receipt_path)
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
    engine.save_json(STATE_PATH, state)
    return result


def main() -> int:
    configure_engine()
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
        result = engine.stage(session, token)
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
            "readback",
            "public_zip_member_replay",
            "configured_file_order",
            "api_file_order",
            "deleted_files",
            "uploaded_files",
        }
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
