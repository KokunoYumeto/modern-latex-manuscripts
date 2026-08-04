#!/usr/bin/env python3
"""Publish Korean Noether P03 and the P04 T04-T06 tranche in one successor."""

from __future__ import annotations

import argparse
import json
import os
import time
from pathlib import Path

import publish_korean_noether_p03_snapshot_zenodo_20260804 as engine


base = engine.base
API = engine.API
MODERN = engine.MODERN
REPO_ROOT = Path(__file__).resolve().parents[1]
P03_ROOT = REPO_ROOT / "sources" / "noether" / "korean-unchecked-paper-03-20260804"
P04_ROOT = REPO_ROOT / "sources" / "noether" / "korean-unchecked-paper-04-t04-t06-20260804"
STATE_PATH = (
    Path(os.environ.get("LOCALAPPDATA", os.environ.get("TEMP", ".")))
    / "Temp"
    / "korean_noether_p03_p04_20260804"
    / "draft_state.json"
)
RESULT_FILES = 66
VERSION = "2026-08-04 Korean Papers 1, 3, 4 (T04-T06), 5, 7, 41, and 42 snapshots"

DESCRIPTION = """<h2>Emmy Noether working corpus and multilingual readers</h2>
<p>This record preserves a modern-LaTeX working corpus for Emmy Noether together with multilingual working translations, editable sources, source-control evidence, correction history, and bounded public snapshots.</p>
<p><strong>Start here:</strong> <code>01j_Noether_R823_Full_Cumulative_English_20260722.pdf</code> remains the default preview. The represented English working reader, German working source-control reader, Spanish and French cumulative translations, paired Interslavic readers, and exact source/evidence archives remain directly accessible.</p>
<p><strong>Korean bounded snapshots:</strong> Papers 1, 3, 5, 7, 41, and 42 have separately frozen public packages; Paper 4 now includes the exact T04–T06 / U17–U32 tranche. Across them, 58 editable Korean TeX units are preserved. Status, checker, translation-choice, source-custody, and root validation surfaces are direct; mathematical TeX and machine ledgers are organized inside each exact complete ZIP.</p>
<p>The Korean state is deliberately explicit: <strong>UNCHECKED, uncompiled, unrendered, unassembled, and unreviewed</strong>; Paper 4 T04–T06 is also <strong>incomplete</strong>. These are scope labels, not release holds. Archive maintenance performed no source correction, compilation, rendering, mathematical review, linguistic review, certification, or approval.</p>
<p>Forty-nine formerly direct duplicate TeX/ledger objects from the five earlier Korean snapshots are still public byte-for-byte inside their five complete ZIPs and remain direct in immutable version 172. This is transport organization, not content deletion. Exact producer bytes are separately frozen in private custody; public projections replace only private local path/operator tokens. P42’s private coordination screenshot remains excluded with its identity recorded. P04’s 37 out-of-tranche files are fully inventoried and privately frozen rather than misrepresented as part of the authorized 20-file tranche.</p>
<p>These are working transcriptions, translations, and audit materials—not critical editions, native-language certifications, peer review, proof checking, mathematical certification, accessibility certification, or blanket rights grants. Corrections should be published through append-only successors with every prior generation and reversal preserved.</p>"""
NORMALIZED_DESCRIPTION = DESCRIPTION.replace("’", "'")
ADDITIONAL_NOTE = """<p><strong>2026-08-04 Korean P03/P04 closeout.</strong> P03: 33 producer files / 848,460 bytes, three TeX units, 148 structural records, 14-entry difficulty chain, public ZIP 37/37, exclusions0. P04 T04–T06: exact 20-file / 45,880-byte tranche, 16 TeX units, authority lines 3889–4161, next4162, public ZIP24/24; 37 contemporaneous out-of-tranche files are hash-inventoried and privately frozen. Across all seven Korean paper surfaces: 226 admitted producer files / 2,880,548 bytes, 58 target units, one P42 private screenshot exclusion plus 37 P04 tranche-scope exclusions. No compile, render, assembly, or review.</p>"""


def predecessor_receipt() -> dict:
    return engine.predecessor_receipt()


def duplicate_names() -> set[str]:
    receipt = predecessor_receipt()
    names = {
        row["filename"]
        for row in receipt["new_direct_readback"]
        if row["filename"].startswith(("70a_", "70b_", "70c_", "70d_", "70e_"))
        and ("__10_U" in row["filename"] or "__20_" in row["filename"] or "__21_" in row["filename"])
    }
    if len(names) != 49:
        raise RuntimeError(f"Expected 49 ZIP-duplicated Korean direct objects, observed {len(names)}")
    return names


REMOVED_DUPLICATES = duplicate_names()


def file_row(path: Path) -> dict:
    return {
        "path": str(path),
        "bytes": path.stat().st_size,
        "sha256": engine.prior.sha256(path),
        "md5": engine.prior.md5(path),
    }


def local_surface() -> tuple[dict[str, dict], list[str], dict]:
    p03_validation_path = P03_ROOT / "SNAPSHOT_VALIDATION.json"
    p04_validation_path = P04_ROOT / "SNAPSHOT_VALIDATION.json"
    if (p03_validation_path.stat().st_size, engine.prior.sha256(p03_validation_path)) != (
        6_217,
        "063CCDA2804D1165538400C4F9229D79E95E1965394A439F240222452A7CEFA8",
    ):
        raise RuntimeError("P03 closeout identity changed")
    if (p04_validation_path.stat().st_size, engine.prior.sha256(p04_validation_path)) != (
        3_149,
        "0A7D64A02A2E2BE30B05A031AB0E7A7B1F8D07BFBDF96E4CA79A2B548461FBC2",
    ):
        raise RuntimeError("P04 closeout identity changed")
    p03_validation = json.loads(p03_validation_path.read_text(encoding="utf-8"))
    p04_validation = json.loads(p04_validation_path.read_text(encoding="utf-8"))
    if p03_validation.get("status") != "PASS_READY_FOR_SAME_CONCEPT_PUBLICATION" or p03_validation.get("errors") != []:
        raise RuntimeError("P03 closeout is not PASS/errors[]")
    if p04_validation.get("status") != "PASS_READY_FOR_SAME_CONCEPT_PUBLICATION" or p04_validation.get("errors") != []:
        raise RuntimeError("P04 closeout is not PASS/errors[]")
    p03_zip = P03_ROOT / "P03_Korean_UNCHECKED_Public_Snapshot_20260804.zip"
    p04_zip = P04_ROOT / "P04_T04_T06_Korean_UNCHECKED_Public_Snapshot_20260804.zip"
    if (p03_zip.stat().st_size, engine.prior.sha256(p03_zip)) != (
        128_450,
        "AEB6810B64E5222ABBC57BE28C997FEC335D2E330C01D1321B920FCFEFB6FBD8",
    ):
        raise RuntimeError("P03 public ZIP changed")
    if (p04_zip.stat().st_size, engine.prior.sha256(p04_zip)) != (
        34_424,
        "9C551879DB17790DCA1DFFE6134BA6B2999CCDEB0FE39AE55CD91A049FE933EC",
    ):
        raise RuntimeError("P04 public ZIP changed")
    p03 = P03_ROOT / "P03"
    p04 = P04_ROOT / "P04_T04_T06"
    rows = [
        ("70_KO_CJK_DECISION_LOGBOOK_PRIVACY_CLEAN_20260804.md", P04_ROOT / "70_KO_CJK_DECISION_LOGBOOK_PRIVACY_CLEAN_20260804.md"),
        ("70_KO_CJK_PRODUCTION_METHODOLOGY_PRIVACY_CLEAN_20260804.md", P03_ROOT / "70_KO_CJK_PRODUCTION_METHODOLOGY_PRIVACY_CLEAN_20260804.md"),
        ("70_KO_NOETH_DE_AUTHORITY_POINTER_v004_20260804.json", P04_ROOT / "70_KO_NOETH_DE_AUTHORITY_POINTER_v004_20260804.json"),
        ("70f_KO_P03__00_COMPLETE_UNCHECKED_PUBLIC_SNAPSHOT_20260804.zip", p03_zip),
        ("70f_KO_P03__01_STATUS.md", p03 / "STATUS.md"),
        ("70f_KO_P03__02_CHECKER_HANDOFF.md", p03 / "CHECKER_HANDOFF_U01_U03.md"),
        ("70f_KO_P03__03_TRANSLATION_CHOICES.md", p03 / "TRANSLATION_CHOICES_U01_U03.md"),
        ("70f_KO_P03__04_SOURCE_CUSTODY.md", p03 / "SOURCE_CUSTODY.md"),
        ("70f_KO_P03__90_README.md", P03_ROOT / "README.md"),
        ("70f_KO_P03__91_SNAPSHOT_INDEX.csv", P03_ROOT / "70f_KO_P03_SNAPSHOT_INDEX_20260804.csv"),
        ("70f_KO_P03__92_SNAPSHOT_VALIDATION.json", p03_validation_path),
        ("70g_KO_P04_T04_T06__00_COMPLETE_UNCHECKED_PUBLIC_SNAPSHOT_20260804.zip", p04_zip),
        ("70g_KO_P04_T04_T06__01_STATUS.md", p04 / "STATUS_T04_T06.md"),
        ("70g_KO_P04_T04_T06__02_CHECKER_HANDOFF.md", p04 / "CHECKER_HANDOFF_T04_T06_U17_U32.md"),
        ("70g_KO_P04_T04_T06__03_TRANSLATION_CHOICES.md", p04 / "TRANSLATION_CHOICES_T04_T06.md"),
        ("70g_KO_P04_T04_T06__04_SOURCE_CUSTODY.md", p04 / "SOURCE_CUSTODY_T04_T06.md"),
        ("70g_KO_P04_T04_T06__90_README.md", P04_ROOT / "README.md"),
        ("70g_KO_P04_T04_T06__91_SNAPSHOT_INDEX.csv", P04_ROOT / "70g_KO_P04_T04_T06_SNAPSHOT_INDEX_20260804.csv"),
        ("70g_KO_P04_T04_T06__92_SNAPSHOT_VALIDATION.json", p04_validation_path),
    ]
    surface = {name: file_row(path) for name, path in rows}
    if len(surface) != 19:
        raise RuntimeError("Combined P03/P04 surface count changed")
    validation = {
        "total_source_files": 53,
        "total_source_bytes": 894_340,
        "total_target_units": 19,
        "total_explicit_exclusions": 37,
        "p03_public_zip_members": 37,
        "p04_public_zip_members": 24,
        "p04_out_of_tranche_files": 37,
    }
    return surface, [name for name, _ in rows], validation


def prove_duplicates_preserved() -> list[dict]:
    receipt = predecessor_receipt()
    direct = {
        row["filename"]: (int(row["bytes"]), row["sha256"])
        for row in receipt["new_direct_readback"]
    }
    zip_replays = receipt["public_zip_member_replays"]
    proofs = []
    for name in sorted(REMOVED_DUPLICATES):
        prefix = name[:3]
        zip_name = next(key for key in zip_replays if key.startswith(prefix + "_") or key.startswith(prefix))
        matches = [
            row
            for row in zip_replays[zip_name]["member_identities"]
            if (int(row["bytes"]), row["sha256"]) == direct[name]
        ]
        if len(matches) != 1:
            raise RuntimeError(f"ZIP preservation proof is not unique for {name}")
        proofs.append(
            {
                "removed_direct_filename": name,
                "preserved_zip": zip_name,
                "preserved_member": matches[0]["relative_path"],
                "bytes": direct[name][0],
                "sha256": direct[name][1],
                "prior_version": engine.PREDECESSOR_DOI,
            }
        )
    return proofs


def desired_order(current: list[str], new_order: list[str]) -> list[str]:
    order = [name for name in current if name not in REMOVED_DUPLICATES]
    pointer_name = "70_KO_NOETH_DE_AUTHORITY_POINTER_v004_20260804.json"
    pointer_anchor = order.index("70_KO_NOETH_DE_AUTHORITY_POINTER_v003_20260804.json") + 1
    order.insert(pointer_anchor, pointer_name)
    additions = [name for name in new_order if name.startswith(("70f_", "70g_"))]
    anchor = order.index("70e_KO_P42__03_TRANSLATION_CHOICES.md") + 1
    order[anchor:anchor] = additions
    if len(order) != RESULT_FILES or len(order) != len(set(order)):
        raise RuntimeError(f"Combined P03/P04 order changed: {len(order)}")
    return order


def configure_engine() -> None:
    engine.STATE_PATH = STATE_PATH
    engine.RESULT_FILES = RESULT_FILES
    engine.VERSION = VERSION
    engine.DESCRIPTION = DESCRIPTION
    engine.NORMALIZED_DESCRIPTION = NORMALIZED_DESCRIPTION
    engine.ADDITIONAL_NOTE = ADDITIONAL_NOTE
    engine.REMOVED_DUPLICATE_LEDGERS = REMOVED_DUPLICATES
    engine.local_surface = local_surface
    engine.prove_removed_ledgers_preserved = prove_duplicates_preserved
    engine.desired_order = desired_order


def preflight(session, token: str) -> dict:
    surface, new_order, validation = local_surface()
    proofs = prove_duplicates_preserved()
    live = engine.fetch_live(session)
    state = engine.verify_active_draft(session, token, live)
    order = desired_order(predecessor_receipt()["configured_file_order"], new_order)
    return {
        "status": "PASS_READY_FOR_ONE_COMBINED_P03_P04_SAME_CONCEPT_SUCCESSOR",
        "concept_id": engine.CONCEPT_ID,
        "concept_doi": engine.CONCEPT_DOI,
        "predecessor_record_id": engine.PREDECESSOR_ID,
        "predecessor_version_doi": engine.PREDECESSOR_DOI,
        "predecessor_version_index": engine.PREDECESSOR_INDEX,
        "predecessor_files": engine.PREDECESSOR_FILES,
        "active_draft": state is not None and not state.get("published", False),
        "tracked_draft_id": None if state is None else state.get("draft_id"),
        "new_or_replaced_direct_files": len(surface),
        "zip_duplicate_direct_files_removed": len(proofs),
        "zip_duplicate_bytes_preserved": sum(int(row["bytes"]) for row in proofs),
        "resulting_files": len(order),
        "admitted_source_files": validation["total_source_files"],
        "admitted_source_bytes": validation["total_source_bytes"],
        "target_units": validation["total_target_units"],
        "p04_out_of_tranche_files": validation["p04_out_of_tranche_files"],
        "default_preview_retained": engine.DEFAULT_PREVIEW,
        "duplicate_concept_created": False,
        "release_hold": False,
    }


def publish_and_readback(session, token: str, confirm: str, receipt_dir: Path) -> dict:
    surface, new_order, validation = local_surface()
    proofs = prove_duplicates_preserved()
    live = engine.fetch_live(session)
    order = desired_order(predecessor_receipt()["configured_file_order"], new_order)
    state = engine.verify_active_draft(session, token, live)
    if state is None or state.get("published") or not state.get("staged"):
        raise RuntimeError("No exact staged combined P03/P04 draft is tracked")
    draft_id = int(state["draft_id"])
    if confirm != str(draft_id):
        raise RuntimeError(f"Publishing requires --confirm-publish {draft_id}")
    draft = base.check(
        session.get(f"{API}/records/{draft_id}/draft", headers=engine.auth_modern(token), timeout=(30, 600)),
        {200},
    ).json()
    engine.verify_staged(draft, live, surface, order)
    if int(draft.get("versions", {}).get("index", 0)) != engine.PREDECESSOR_INDEX + 1:
        raise RuntimeError("Combined P03/P04 staged version index changed")
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
        raise RuntimeError("Combined P03/P04 successor did not become public")
    engine.verify_staged(record, live, surface, order)
    if (
        str(record.get("parent", {}).get("id")) != engine.CONCEPT_ID
        or record.get("versions", {}).get("is_latest") is not True
        or int(record.get("versions", {}).get("index", 0)) != engine.PREDECESSOR_INDEX + 1
    ):
        raise RuntimeError("Published combined P03/P04 lineage changed")
    entries = engine.modern_entries(record)
    zip_expectations = {
        "70f_KO_P03__00_COMPLETE_UNCHECKED_PUBLIC_SNAPSHOT_20260804.zip": 37,
        "70g_KO_P04_T04_T06__00_COMPLETE_UNCHECKED_PUBLIC_SNAPSHOT_20260804.zip": 24,
    }
    download_root = STATE_PATH.parent / "public_zip_readback"
    download_root.mkdir(parents=True, exist_ok=True)
    readback = []
    zip_replays = {}
    errors = []
    for index, name in enumerate(new_order, start=1):
        print(f"READBACK {index}/{len(new_order)} {name}", flush=True)
        destination = download_root / name if name in zip_expectations else None
        observed = engine.prior.stream_identity(anonymous, entries[name]["links"]["content"], destination)
        expected = (int(surface[name]["bytes"]), surface[name]["sha256"])
        match = observed == expected
        if not match:
            errors.append(name)
        readback.append({"filename": name, "bytes": observed[0], "sha256": observed[1], "match": match, "content_url": entries[name]["links"]["content"]})
        if destination is not None:
            replay = engine.prior.replay_downloaded_zip(destination, zip_expectations[name])
            if replay["status"] != "PASS":
                errors.append(name + ":member_replay")
            zip_replays[name] = replay
            destination.unlink()
    inherited = engine.modern_entries(live)
    inherited_errors = [
        name
        for name in (set(entries) - set(surface))
        if engine.modern_identity(entries[name]) != engine.modern_identity(inherited[name])
    ]
    errors.extend(inherited_errors)
    if errors:
        raise RuntimeError(f"Combined P03/P04 public readback errors: {errors}")
    active = session.get(f"{API}/records/{engine.PREDECESSOR_ID}/draft", headers=engine.auth_modern(token), timeout=(30, 180))
    if active.status_code not in {404, 410}:
        raise RuntimeError("Noether active draft remains after combined P03/P04 publication")
    result = {
        "status": "PASS_PUBLISHED_P03_P04_SAME_CONCEPT_AND_ANONYMOUS_RAW_READBACK",
        "errors": [],
        "record_id": record_id,
        "record_url": record["links"]["self_html"],
        "version_doi": record["pids"]["doi"]["identifier"],
        "concept_id": engine.CONCEPT_ID,
        "concept_doi": engine.CONCEPT_DOI,
        "predecessor_record_id": engine.PREDECESSOR_ID,
        "predecessor_version_doi": engine.PREDECESSOR_DOI,
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
        "public_zip_replays": zip_replays,
        "zip_duplicate_direct_proofs": proofs,
        "p03_source_files": 33,
        "p03_source_bytes": 848_460,
        "p03_targets": 3,
        "p03_exclusions": 0,
        "p04_selected_files": 20,
        "p04_selected_bytes": 45_880,
        "p04_targets": 16,
        "p04_out_of_tranche_files": validation["p04_out_of_tranche_files"],
        "state_labels": ["UNCHECKED", "incomplete(P04)", "uncompiled", "unrendered", "unassembled", "unreviewed"],
        "active_draft": False,
        "duplicate_concept_created": False,
        "release_hold": False,
        "readback": readback,
        "configured_file_order": order,
        "api_file_order": record["files"].get("order") or [],
    }
    receipt_path = receipt_dir / f"20260804_korean_noether_p03_p04_record_{record_id}_public_readback.json"
    engine.save_json(receipt_path, result)
    result["receipt_path"] = str(receipt_path)
    result["receipt_bytes"] = receipt_path.stat().st_size
    result["receipt_sha256"] = engine.prior.sha256(receipt_path)
    state.update({"status": "PASS_PUBLISHED_AND_ANONYMOUS_READBACK", "published": True, "record_id": record_id, "doi": result["version_doi"], "receipt_path": str(receipt_path), "completed_at_epoch": int(time.time())})
    engine.save_json(STATE_PATH, state)
    return result


def main() -> int:
    configure_engine()
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
        result = engine.stage(session, token)
    else:
        if not args.confirm_publish:
            raise RuntimeError("Publishing requires --confirm-publish DRAFT_ID")
        result = publish_and_readback(session, token, args.confirm_publish, args.receipt_dir.resolve())
    summary = {key: value for key, value in result.items() if key not in {"readback", "public_zip_replays", "configured_file_order", "api_file_order", "zip_duplicate_direct_proofs", "deleted_files", "uploaded_files"}}
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
