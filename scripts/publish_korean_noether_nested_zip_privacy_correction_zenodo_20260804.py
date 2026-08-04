#!/usr/bin/env python3
"""Publish the six Korean nested-ZIP privacy corrections on the Noether line."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import time
import zipfile
from pathlib import Path

import publish_korean_noether_p03_snapshot_zenodo_20260804 as engine
import publish_korean_noether_p04_complete_privacy_correction_zenodo_20260804 as completepub
import build_korean_noether_nested_zip_privacy_correction_20260804 as correction


base = engine.base
API = engine.API
MODERN = engine.MODERN
REPO_ROOT = Path(__file__).resolve().parents[1]
ROOT = REPO_ROOT / "sources/noether/korean-nested-zip-privacy-correction-20260804-r2"
PREDECESSOR_RECEIPT = (
    REPO_ROOT
    / "manifests/published-zenodo/20260804_korean_noether_p04_complete_record_21785396_public_readback.json"
)
STATE_PATH = (
    Path(os.environ.get("LOCALAPPDATA", os.environ.get("TEMP", ".")))
    / "Temp"
    / "korean_noether_nested_zip_privacy_correction_20260804"
    / "draft_state.json"
)

CONCEPT_ID = "20412587"
CONCEPT_DOI = "10.5281/zenodo.20412587"
PREDECESSOR_ID = 21785396
PREDECESSOR_DOI = "10.5281/zenodo.21785396"
PREDECESSOR_INDEX = 175
PREDECESSOR_FILES = 83
PREDECESSOR_BYTES = 585_440_667
RESULT_FILES = 88
DEFAULT_PREVIEW = "01j_Noether_R823_Full_Cumulative_English_20260722.pdf"
VERSION = "2026-08-04 Korean nested-ZIP privacy correction and complete Paper 4 archive"
TITLE = "Emmy Noether: Modern LaTeX Working Corpus and Multilingual Translation Readers"

DESCRIPTION = """<h2>Emmy Noether working corpus and multilingual readers</h2>
<p>This record preserves a modern-LaTeX working corpus for Emmy Noether together with multilingual working translations, editable sources, source-control evidence, correction history, and bounded public snapshots.</p>
<p><strong>Start here:</strong> <code>01j_Noether_R823_Full_Cumulative_English_20260722.pdf</code> remains the default preview. The represented English working reader, German working source-control reader, Spanish and French cumulative translations, paired Interslavic readers, and exact source/evidence archives remain directly accessible.</p>
<p><strong>Korean snapshots:</strong> Papers 1, 3, 5, 7, 41, and 42 retain separately frozen packages. Paper 4 has one coherent complete producer-draft package with all fifty Korean TeX units for sections 1-9. Paper 4 structural evidence is scoped to T01-T03 only.</p>
<p>The Korean state is explicit: <strong>UNCHECKED, uncompiled, unrendered, unassembled, unreviewed, and uncertified</strong>. Complete producer-draft coverage is not linguistic validation, mathematical review, or approval. These labels are not release holds.</p>
<p><strong>Privacy correction:</strong> the preceding version corrected four direct outer validation JSON files with 18 serialized local-path occurrences. A deeper ZIP-member audit then found 1,461 path/operator occurrences inside seventeen members of six older Korean snapshot ZIPs. This version replaces those same six ZIP filenames with deterministic privacy-clean successors, preserves all 229 members, and exposes exact source/successor/member/transformation manifests. The mathematical and translation content was retained; immutable predecessors remain adverse-history witnesses.</p>
<p>Every public transformation is path/bytes/SHA-bound. Earlier tranche packages and corrections remain versioned history, not deleted work. Future corrections should continue append-only with source, rationale, error, and reversal evidence preserved.</p>"""
NORMALIZED_DESCRIPTION = DESCRIPTION.replace("’", "'")
ADDITIONAL_NOTE = """<p><strong>2026-08-04 nested-ZIP archive correction.</strong> Six ZIPs, 229/229 members, 17 affected members, and 1,461 serialized local-path/operator occurrences were corrected; raw public ZIP and member replay is mandatory. Together with the immediately preceding four-file correction, the Korean archive correction covers 1,479 occurrences. No mathematical/source-state claim changed; release hold false.</p>"""

EXPECTED_VALIDATION = (
    4_275,
    "01B98DE1D833705455E1A07DC709C17F64A0DDA3DB6E5F779D66A4ADC2A043FB",
)
ZIP_MEMBERS = {
    name: int(values[3]) for name, values in correction.SOURCES.items()
}
ALL_KOREAN_ZIP_MEMBERS = {
    **ZIP_MEMBERS,
    "70g_KO_P04_T04_T06__00_COMPLETE_UNCHECKED_PUBLIC_SNAPSHOT_20260804.zip": 24,
    "70h_KO_P04_T07__00_COMPLETE_UNCHECKED_PUBLIC_SNAPSHOT_20260804.zip": 14,
    "70i_KO_P04_COMPLETE__00_COMPLETE_UNCHECKED_PUBLIC_SNAPSHOT_20260804.zip": 96,
}


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
        != "PASS_PUBLISHED_P04_COMPLETE_PRIVACY_CORRECTED_AND_ANONYMOUS_RAW_READBACK"
        or int(receipt.get("record_id", 0)) != PREDECESSOR_ID
        or receipt.get("version_doi") != PREDECESSOR_DOI
        or receipt.get("concept_doi") != CONCEPT_DOI
        or int(receipt.get("version_index", 0)) != PREDECESSOR_INDEX
        or int(receipt.get("files", 0)) != PREDECESSOR_FILES
        or int(receipt.get("bytes", 0)) != PREDECESSOR_BYTES
        or receipt.get("default_preview") != DEFAULT_PREVIEW
        or len(receipt.get("configured_file_order", [])) != PREDECESSOR_FILES
    ):
        raise RuntimeError("Nested-ZIP correction predecessor receipt boundary changed")
    return receipt


def local_surface() -> tuple[dict[str, dict], list[str], dict]:
    validation_path = ROOT / "VALIDATION.json"
    if (validation_path.stat().st_size, engine.prior.sha256(validation_path)) != EXPECTED_VALIDATION:
        raise RuntimeError("Nested-ZIP correction validation identity changed")
    validation = json.loads(validation_path.read_text(encoding="utf-8"))
    if (
        validation.get("status") != "PASS_READY_FOR_SAME_CONCEPT_PRIVACY_CORRECTION"
        or validation.get("errors") != []
        or int(validation.get("affected_zip_files", 0)) != 6
        or int(validation.get("total_members", 0)) != 229
        or int(validation.get("private_path_occurrences", 0)) != 1_461
        or validation.get("release_hold") is not False
    ):
        raise RuntimeError("Nested-ZIP correction validation boundary changed")
    rows = [(name, ROOT / name) for name in ZIP_MEMBERS]
    rows.extend(
        [
            ("70j_KO_PRIVACY_CORRECTION__01_README.md", ROOT / "README.md"),
            (
                "70j_KO_PRIVACY_CORRECTION__90_ZIP_CORRECTION_MANIFEST.csv",
                ROOT / "NESTED_ZIP_PRIVACY_CORRECTION_MANIFEST.csv",
            ),
            (
                "70j_KO_PRIVACY_CORRECTION__91_MEMBER_TRANSFORMATIONS.csv",
                ROOT / "NESTED_ZIP_MEMBER_TRANSFORMATIONS.csv",
            ),
            (
                "70j_KO_PRIVACY_CORRECTION__92_MEMBER_MANIFEST.csv",
                ROOT / "NESTED_ZIP_MEMBER_MANIFEST.csv",
            ),
            ("70j_KO_PRIVACY_CORRECTION__99_VALIDATION.json", validation_path),
        ]
    )
    surface = {name: file_row(path) for name, path in rows}
    if len(surface) != 11:
        raise RuntimeError("Nested-ZIP correction direct surface count changed")
    return surface, [name for name, _ in rows], validation


def prove_removed_ledgers_preserved() -> list[dict]:
    return []


def desired_order(current: list[str], new_order: list[str]) -> list[str]:
    order = list(current)
    additions = [name for name in new_order if name.startswith("70j_")]
    anchor = order.index("70i_KO_P04_COMPLETE__92_SNAPSHOT_VALIDATION.json") + 1
    order[anchor:anchor] = additions
    if len(order) != RESULT_FILES or len(order) != len(set(order)):
        raise RuntimeError(f"Nested-ZIP correction resulting order changed: {len(order)}")
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


def replay_and_scan_zip(path: Path, expected_members: int) -> dict:
    rows = []
    errors = []
    with zipfile.ZipFile(path) as package:
        infos = [row for row in package.infolist() if not row.is_dir()]
        if len(infos) != expected_members or package.testzip() is not None:
            errors.append("member_count_or_crc")
        for info in infos:
            data = package.read(info)
            hits = correction.privacy_hits(data)
            if hits:
                errors.append(info.filename)
            rows.append(
                {
                    "member_path": info.filename,
                    "bytes": len(data),
                    "sha256": hashlib.sha256(data).hexdigest().upper(),
                    "privacy_hits": hits,
                }
            )
    return {
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "members": len(rows),
        "privacy_hit_members": sum(1 for row in rows if row["privacy_hits"]),
        "member_identities": rows,
    }


def fetch_published_predecessor(session) -> dict:
    record = base.check(
        session.get(f"{API}/records/{PREDECESSOR_ID}", headers=MODERN, timeout=(30, 300)),
        {200},
    ).json()
    entries = engine.modern_entries(record)
    if (
        int(record["id"]) != PREDECESSOR_ID
        or record["pids"]["doi"]["identifier"] != PREDECESSOR_DOI
        or str(record.get("parent", {}).get("id")) != CONCEPT_ID
        or int(record.get("versions", {}).get("index", 0)) != PREDECESSOR_INDEX
        or record.get("status") != "published"
        or len(entries) != PREDECESSOR_FILES
        or sum(int(row["size"]) for row in entries.values()) != PREDECESSOR_BYTES
        or record.get("files", {}).get("default_preview") != DEFAULT_PREVIEW
    ):
        raise RuntimeError("Published predecessor recovery boundary changed")
    return record


def preflight(session, token: str) -> dict:
    surface, new_order, validation = local_surface()
    live = engine.fetch_live(session)
    state = engine.verify_active_draft(session, token, live)
    order = desired_order(predecessor_receipt()["configured_file_order"], new_order)
    return {
        "status": "PASS_READY_FOR_ONE_NESTED_ZIP_PRIVACY_CORRECTIVE_SUCCESSOR",
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
        "affected_zips": validation["affected_zip_files"],
        "total_members": validation["total_members"],
        "private_path_occurrences": validation["private_path_occurrences"],
        "default_preview_retained": DEFAULT_PREVIEW,
        "duplicate_concept_created": False,
        "release_hold": False,
    }


def publish_and_readback(session, token: str, confirm: str, receipt_dir: Path) -> dict:
    surface, new_order, validation = local_surface()
    order = desired_order(predecessor_receipt()["configured_file_order"], new_order)
    state = engine.load_state()
    if state is None or not state.get("staged"):
        raise RuntimeError("No exact staged nested-ZIP correction state is tracked")
    draft_id = int(state["draft_id"])
    if confirm != str(draft_id):
        raise RuntimeError(f"Publishing requires --confirm-publish {draft_id}")
    public_probe = session.get(f"{API}/records/{draft_id}", headers=MODERN, timeout=(30, 300))
    already_published = public_probe.status_code == 200 and public_probe.json().get("status") == "published"
    if already_published:
        live = fetch_published_predecessor(session)
        record_id = draft_id
    else:
        live = engine.fetch_live(session)
        tracked = engine.verify_active_draft(session, token, live)
        if tracked is None or tracked.get("published") or not tracked.get("staged"):
            raise RuntimeError("No exact staged nested-ZIP correction draft is tracked")
        draft = base.check(
            session.get(f"{API}/records/{draft_id}/draft", headers=engine.auth_modern(token), timeout=(30, 600)),
            {200},
        ).json()
        engine.verify_staged(draft, live, surface, order)
        if int(draft.get("versions", {}).get("index", 0)) != PREDECESSOR_INDEX + 1:
            raise RuntimeError("Nested-ZIP correction staged version index changed")
        response = base.check(
            session.post(draft["links"]["publish"], headers=engine.auth_modern(token), timeout=(30, 1200)),
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
        raise RuntimeError("Nested-ZIP correction successor did not become public")
    engine.verify_staged(record, live, surface, order)
    if (
        str(record.get("parent", {}).get("id")) != CONCEPT_ID
        or record.get("versions", {}).get("is_latest") is not True
        or int(record.get("versions", {}).get("index", 0)) != PREDECESSOR_INDEX + 1
    ):
        raise RuntimeError("Published nested-ZIP correction lineage changed")

    entries = engine.modern_entries(record)
    download_root = STATE_PATH.parent / "public_readback"
    download_root.mkdir(parents=True, exist_ok=True)
    readback = []
    zip_replays = {}
    errors = []
    for index, name in enumerate(new_order, start=1):
        print(f"READBACK {index}/{len(new_order)} {name}", flush=True)
        destination = download_root / name if name in ZIP_MEMBERS else None
        observed = engine.prior.stream_identity(anonymous, entries[name]["links"]["content"], destination)
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
            replay = replay_and_scan_zip(destination, ZIP_MEMBERS[name])
            zip_replays[name] = replay
            if replay["status"] != "PASS":
                errors.append(name + ":member_replay")
            destination.unlink()
    inherited = engine.modern_entries(live)
    inherited_errors = [
        name
        for name in (set(entries) - set(surface))
        if engine.modern_identity(entries[name]) != engine.modern_identity(inherited[name])
    ]
    errors.extend(inherited_errors)
    direct_privacy = completepub.direct_text_privacy_scan(anonymous, entries)
    if direct_privacy["status"] != "PASS":
        errors.append("live_direct_text_privacy_scan")

    all_zip_replays = {}
    for index, (name, members) in enumerate(ALL_KOREAN_ZIP_MEMBERS.items(), start=1):
        print(f"FULL KOREAN ZIP PRIVACY REPLAY {index}/9 {name}", flush=True)
        destination = download_root / ("full_" + name)
        engine.prior.stream_identity(anonymous, entries[name]["links"]["content"], destination)
        replay = replay_and_scan_zip(destination, members)
        all_zip_replays[name] = replay
        if replay["status"] != "PASS":
            errors.append(name + ":full_live_nested_privacy")
        destination.unlink()
    if errors:
        raise RuntimeError(f"Nested-ZIP correction public readback errors: {errors}")
    active = session.get(
        f"{API}/records/{PREDECESSOR_ID}/draft",
        headers=engine.auth_modern(token),
        timeout=(30, 180),
    )
    if active.status_code not in {404, 410}:
        raise RuntimeError("Noether active draft remains after nested-ZIP correction")

    result = {
        "status": "PASS_PUBLISHED_NESTED_ZIP_PRIVACY_CORRECTED_AND_ANONYMOUS_RAW_READBACK",
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
        "corrected_zip_replays": zip_replays,
        "all_nine_korean_zip_privacy_replays": all_zip_replays,
        "all_nine_korean_zip_members": sum(ALL_KOREAN_ZIP_MEMBERS.values()),
        "all_nine_korean_zip_privacy_hit_members": 0,
        "live_direct_text_privacy_scan": direct_privacy,
        "affected_zip_files": validation["affected_zip_files"],
        "corrected_members": validation["total_members"],
        "private_path_occurrences": validation["private_path_occurrences"],
        "state_labels": validation["state_labels_unchanged"],
        "active_draft": False,
        "duplicate_concept_created": False,
        "release_hold": False,
        "readback": readback,
        "configured_file_order": order,
        "api_file_order": record["files"].get("order") or [],
    }
    receipt_path = (
        receipt_dir
        / f"20260804_korean_noether_nested_zip_privacy_record_{record_id}_public_readback.json"
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
        default=REPO_ROOT / "manifests/published-zenodo",
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
        result = publish_and_readback(session, token, args.confirm_publish, args.receipt_dir.resolve())
    summary = {
        key: value
        for key, value in result.items()
        if key
        not in {
            "readback",
            "corrected_zip_replays",
            "all_nine_korean_zip_privacy_replays",
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
