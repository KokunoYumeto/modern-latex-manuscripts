#!/usr/bin/env python3
"""Publish the complete Korean P04 snapshot and repair four live privacy leaks."""

from __future__ import annotations

import argparse
import json
import os
import re
import time
from pathlib import Path

import publish_korean_noether_p03_snapshot_zenodo_20260804 as engine


base = engine.base
API = engine.API
MODERN = engine.MODERN
REPO_ROOT = Path(__file__).resolve().parents[1]
ROOT = REPO_ROOT / "sources/noether/korean-unchecked-paper-04-complete-producer-draft-20260804"
PREDECESSOR_RECEIPT = (
    REPO_ROOT
    / "manifests/published-zenodo/20260804_korean_noether_p04_t07_record_21784732_public_readback.json"
)
STATE_PATH = (
    Path(os.environ.get("LOCALAPPDATA", os.environ.get("TEMP", ".")))
    / "Temp"
    / "korean_noether_p04_complete_privacy_correction_20260804"
    / "draft_state.json"
)

CONCEPT_ID = "20412587"
CONCEPT_DOI = "10.5281/zenodo.20412587"
PREDECESSOR_ID = 21784732
PREDECESSOR_DOI = "10.5281/zenodo.21784732"
PREDECESSOR_INDEX = 174
PREDECESSOR_FILES = 74
PREDECESSOR_BYTES = 584_815_217
RESULT_FILES = 83
DEFAULT_PREVIEW = "01j_Noether_R823_Full_Cumulative_English_20260722.pdf"
VERSION = "2026-08-04 Korean Paper 4 complete producer draft and privacy-corrected archive"
TITLE = "Emmy Noether: Modern LaTeX Working Corpus and Multilingual Translation Readers"

DESCRIPTION = """<h2>Emmy Noether working corpus and multilingual readers</h2>
<p>This record preserves a modern-LaTeX working corpus for Emmy Noether together with multilingual working translations, editable sources, source-control evidence, correction history, and bounded public snapshots.</p>
<p><strong>Start here:</strong> <code>01j_Noether_R823_Full_Cumulative_English_20260722.pdf</code> remains the default preview. The represented English working reader, German working source-control reader, Spanish and French cumulative translations, paired Interslavic readers, and exact source/evidence archives remain directly accessible.</p>
<p><strong>Korean bounded snapshots:</strong> Papers 1, 3, 5, 7, 41, and 42 retain their separately frozen public packages. Paper 4 now has one coherent complete producer-draft package containing all fifty Korean TeX units for sections 1-9, the exact T08-T09 handoff, source custody, translation choices, current decision/error history, and methodology. Its structural evidence is explicitly scoped to T01-T03 only; it is not represented as whole-P04 structural evidence.</p>
<p>The Korean state is explicit: <strong>UNCHECKED, uncompiled, unrendered, unassembled, unreviewed, and uncertified</strong>. Paper 4 has complete producer-draft text coverage, but publication is not approval, linguistic validation, mathematical review, or certification. These are state labels, not release holds.</p>
<p><strong>Privacy correction:</strong> anonymous inspection of predecessor record 21784732 found four outer archive-validation JSON files with 18 serialized absolute local-path occurrences. The current version replaces those same four filenames with minimally transformed privacy-clean bytes and exposes a correction/supersession record. The mathematical TeX, evidence, reader, and package bytes were not implicated. Immutable predecessor 21784732 remains the adverse-history witness.</p>
<p>Earlier Paper 4 tranche packages remain visible as history; the complete package organizes their mathematical continuation without deleting any producer byte. Exact source bytes are separately frozen in private custody, and every public transformation is path/bytes/SHA-bound. Corrections should continue through append-only successors with prior generations and reversals preserved.</p>"""
NORMALIZED_DESCRIPTION = DESCRIPTION.replace("’", "'")
ADDITIONAL_NOTE = """<p><strong>2026-08-04 P04 completion and archive correction.</strong> Exact producer handoff: 34 files / 1,791,291 bytes. Coherent producer-root custody: 83 files / 1,770,781 bytes / 50 target units; public ZIP 96/96. Structural evidence scope T01-T03 only. Four predecessor validation files / 18 serialized private-path occurrences are superseded by same-name privacy-clean projections; record 21784732 remains immutable adverse history. Release hold false.</p>"""

EXPECTED_VALIDATION = (
    5_000,
    "E8A6D6C59F4F730E3080DF4F3F611FB3BE6FB9A7FD8E3C2B3A6D630FA7A065DB",
)
EXPECTED_ZIP = (
    551_725,
    "D71421F9A7B39AC70E2E7D0E1D14E6789AF796A64F2C574F23884A8CB79FFDD4",
    96,
)
CORRECTED_VALIDATION_NAMES = (
    "70_KO_P01_P05_P07_P41_P42_SNAPSHOT_VALIDATION_20260804.json",
    "70f_KO_P03__92_SNAPSHOT_VALIDATION.json",
    "70g_KO_P04_T04_T06__92_SNAPSHOT_VALIDATION.json",
    "70h_KO_P04_T07__92_SNAPSHOT_VALIDATION.json",
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
        != "PASS_PUBLISHED_P04_T07_SAME_CONCEPT_AND_ANONYMOUS_RAW_READBACK"
        or int(receipt.get("record_id", 0)) != PREDECESSOR_ID
        or receipt.get("version_doi") != PREDECESSOR_DOI
        or receipt.get("concept_doi") != CONCEPT_DOI
        or int(receipt.get("version_index", 0)) != PREDECESSOR_INDEX
        or int(receipt.get("files", 0)) != PREDECESSOR_FILES
        or int(receipt.get("bytes", 0)) != PREDECESSOR_BYTES
        or receipt.get("default_preview") != DEFAULT_PREVIEW
        or len(receipt.get("configured_file_order", [])) != PREDECESSOR_FILES
    ):
        raise RuntimeError("P04 complete predecessor receipt boundary changed")
    return receipt


def local_surface() -> tuple[dict[str, dict], list[str], dict]:
    validation_path = ROOT / "SNAPSHOT_VALIDATION.json"
    if (validation_path.stat().st_size, engine.prior.sha256(validation_path)) != EXPECTED_VALIDATION:
        raise RuntimeError("P04 complete closeout identity changed")
    validation = json.loads(validation_path.read_text(encoding="utf-8"))
    package_validation = validation.get("package_validation", {})
    if (
        validation.get("status") != "PASS_READY_FOR_PRIVACY_CORRECTIVE_SAME_CONCEPT_PUBLICATION"
        or validation.get("errors") != []
        or package_validation.get("status") != "PASS_PUBLIC_UNCHECKED_COMPLETE_PRODUCER_DRAFT"
        or package_validation.get("errors") != []
        or int(package_validation.get("producer_handoff_files", 0)) != 34
        or int(package_validation.get("producer_handoff_bytes", 0)) != 1_791_291
        or int(package_validation.get("target_units", 0)) != 50
        or int(package_validation.get("corrected_predecessor_direct_files", 0)) != 4
        or int(package_validation.get("corrected_predecessor_private_path_occurrences", 0)) != 18
        or validation.get("release_hold") is not False
    ):
        raise RuntimeError("P04 complete validation boundary changed")
    zip_path = ROOT / "P04_Korean_Complete_Producer_Draft_UNCHECKED_20260804.zip"
    if (zip_path.stat().st_size, engine.prior.sha256(zip_path)) != EXPECTED_ZIP[:2]:
        raise RuntimeError("P04 complete public ZIP identity changed")
    replay = engine.prior.replay_downloaded_zip(zip_path, EXPECTED_ZIP[2])
    if replay.get("status") != "PASS":
        raise RuntimeError("P04 complete local ZIP replay changed")

    rows = [
        (
            "70_KO_CJK_DECISION_LOGBOOK_PRIVACY_CLEAN_20260804.md",
            ROOT / "70_KO_CJK_DECISION_LOGBOOK_PRIVACY_CLEAN_20260804.md",
        ),
        (
            "70_KO_CJK_PRODUCTION_METHODOLOGY_PRIVACY_CLEAN_20260804.md",
            ROOT / "06_CJK_PRODUCTION_METHODOLOGY_PRIVACY_CLEAN.md",
        ),
        (
            "70_KO_NOETH_DE_AUTHORITY_POINTER_v004_20260804.json",
            ROOT / "70_KO_NOETH_DE_AUTHORITY_POINTER_v004_20260804.json",
        ),
    ]
    rows.extend(
        (
            name,
            ROOT / "corrected_predecessor_validations" / name,
        )
        for name in CORRECTED_VALIDATION_NAMES
    )
    rows.extend(
        [
            (
                "70i_KO_P04_COMPLETE__00_COMPLETE_UNCHECKED_PUBLIC_SNAPSHOT_20260804.zip",
                zip_path,
            ),
            ("70i_KO_P04_COMPLETE__01_STATUS.md", ROOT / "01_STATUS_T08_T09.md"),
            (
                "70i_KO_P04_COMPLETE__02_CHECKER_HANDOFF.md",
                ROOT / "02_CHECKER_HANDOFF_T08_T09_U39_U50.md",
            ),
            (
                "70i_KO_P04_COMPLETE__03_TRANSLATION_CHOICES.md",
                ROOT / "03_TRANSLATION_CHOICES_T08_T09.md",
            ),
            (
                "70i_KO_P04_COMPLETE__04_SOURCE_CUSTODY.md",
                ROOT / "04_SOURCE_CUSTODY_T08_T09.md",
            ),
            (
                "70i_KO_P04_COMPLETE__05_PRIVACY_CORRECTION_AND_SUPERSESSION.md",
                ROOT / "05_PRIVACY_CORRECTION_AND_SUPERSESSION.md",
            ),
            ("70i_KO_P04_COMPLETE__90_README.md", ROOT / "README.md"),
            (
                "70i_KO_P04_COMPLETE__91_SNAPSHOT_INDEX.csv",
                ROOT / "70i_KO_P04_COMPLETE_SNAPSHOT_INDEX_20260804.csv",
            ),
            ("70i_KO_P04_COMPLETE__92_SNAPSHOT_VALIDATION.json", validation_path),
        ]
    )
    surface = {name: file_row(path) for name, path in rows}
    if len(surface) != 16:
        raise RuntimeError("P04 complete direct surface count changed")
    return surface, [name for name, _ in rows], validation


def prove_removed_ledgers_preserved() -> list[dict]:
    return []


def desired_order(current: list[str], new_order: list[str]) -> list[str]:
    order = list(current)
    additions = [name for name in new_order if name.startswith("70i_")]
    anchor = order.index("70h_KO_P04_T07__92_SNAPSHOT_VALIDATION.json") + 1
    order[anchor:anchor] = additions
    if len(order) != RESULT_FILES or len(order) != len(set(order)):
        raise RuntimeError(f"P04 complete resulting order changed: {len(order)}")
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


def direct_text_privacy_scan(session, entries: dict[str, dict]) -> dict:
    extensions = (".md", ".json", ".jsonl", ".csv", ".tex", ".txt", ".mjs", ".ps1")
    patterns = {
        "windows_user_path": re.compile(rb"(?i)[A-Z]:\\Users\\"),
        "escaped_windows_user_path": re.compile(rb"(?i)[A-Z]:\\\\Users\\\\"),
        "posix_user_path": re.compile(rb"(?i)(?:/home/|/Users/)[^/\r\n]+"),
        "operator_name": re.compile(
            rb"\b" + re.escape(Path.home().name.encode("utf-8")) + rb"\b",
            re.IGNORECASE,
        ),
    }
    files = 0
    total = 0
    hits = []
    for name, row in entries.items():
        if not name.lower().endswith(extensions) or int(row["size"]) > 10_000_000:
            continue
        response = base.check(session.get(row["links"]["content"], timeout=(30, 300)), {200})
        data = response.content
        files += 1
        total += len(data)
        observed = {label: len(pattern.findall(data)) for label, pattern in patterns.items()}
        observed = {label: count for label, count in observed.items() if count}
        if observed:
            hits.append({"filename": name, "hits": observed})
    return {
        "status": "PASS" if not hits else "FAIL",
        "files": files,
        "bytes": total,
        "hits": hits,
    }


def preflight(session, token: str) -> dict:
    surface, new_order, validation = local_surface()
    live = engine.fetch_live(session)
    state = engine.verify_active_draft(session, token, live)
    order = desired_order(predecessor_receipt()["configured_file_order"], new_order)
    return {
        "status": "PASS_READY_FOR_ONE_P04_COMPLETE_PRIVACY_CORRECTIVE_SUCCESSOR",
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
        "producer_handoff_files": validation["package_validation"]["producer_handoff_files"],
        "producer_handoff_bytes": validation["package_validation"]["producer_handoff_bytes"],
        "target_units": validation["package_validation"]["target_units"],
        "corrected_predecessor_direct_files": 4,
        "corrected_predecessor_private_path_occurrences": 18,
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
        raise RuntimeError("No exact staged P04 complete draft is tracked")
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
        raise RuntimeError("P04 complete staged version index changed")
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
        raise RuntimeError("P04 complete successor did not become public")
    engine.verify_staged(record, live, surface, order)
    if (
        str(record.get("parent", {}).get("id")) != CONCEPT_ID
        or record.get("versions", {}).get("is_latest") is not True
        or int(record.get("versions", {}).get("index", 0)) != PREDECESSOR_INDEX + 1
    ):
        raise RuntimeError("Published P04 complete lineage changed")

    entries = engine.modern_entries(record)
    zip_name = "70i_KO_P04_COMPLETE__00_COMPLETE_UNCHECKED_PUBLIC_SNAPSHOT_20260804.zip"
    download_root = STATE_PATH.parent / "public_zip_readback"
    download_root.mkdir(parents=True, exist_ok=True)
    readback = []
    errors = []
    zip_replay = None
    for index, name in enumerate(new_order, start=1):
        print(f"READBACK {index}/{len(new_order)} {name}", flush=True)
        destination = download_root / name if name == zip_name else None
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
            zip_replay = engine.prior.replay_downloaded_zip(destination, EXPECTED_ZIP[2])
            if zip_replay.get("status") != "PASS":
                errors.append(name + ":member_replay")
            destination.unlink()
    inherited = engine.modern_entries(live)
    inherited_errors = [
        name
        for name in (set(entries) - set(surface))
        if engine.modern_identity(entries[name]) != engine.modern_identity(inherited[name])
    ]
    errors.extend(inherited_errors)
    privacy_scan = direct_text_privacy_scan(anonymous, entries)
    if privacy_scan["status"] != "PASS":
        errors.append("live_direct_text_privacy_scan")
    if zip_replay is None:
        errors.append("missing_zip_replay")
    if errors:
        raise RuntimeError(f"P04 complete public readback errors: {errors}")
    active = session.get(
        f"{API}/records/{PREDECESSOR_ID}/draft",
        headers=engine.auth_modern(token),
        timeout=(30, 180),
    )
    if active.status_code not in {404, 410}:
        raise RuntimeError("Noether active draft remains after P04 complete publication")

    package_validation = validation["package_validation"]
    result = {
        "status": "PASS_PUBLISHED_P04_COMPLETE_PRIVACY_CORRECTED_AND_ANONYMOUS_RAW_READBACK",
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
        "producer_root_files": package_validation["producer_root_files"],
        "producer_root_bytes": package_validation["producer_root_bytes"],
        "producer_root_tree_sha256": package_validation["producer_root_tree_sha256"],
        "producer_handoff_files": package_validation["producer_handoff_files"],
        "producer_handoff_bytes": package_validation["producer_handoff_bytes"],
        "target_units": package_validation["target_units"],
        "evidence_structural_scope": package_validation["evidence_structural_scope"],
        "corrected_predecessor_direct_files": validation["corrected_remote_validations"],
        "live_direct_text_privacy_scan": privacy_scan,
        "state_labels": package_validation["state_labels"],
        "active_draft": False,
        "duplicate_concept_created": False,
        "release_hold": False,
        "readback": readback,
        "configured_file_order": order,
        "api_file_order": record["files"].get("order") or [],
    }
    receipt_path = (
        receipt_dir
        / f"20260804_korean_noether_p04_complete_record_{record_id}_public_readback.json"
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
            "public_zip_member_replay",
            "configured_file_order",
            "api_file_order",
            "deleted_files",
            "uploaded_files",
            "corrected_predecessor_direct_files",
        }
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
