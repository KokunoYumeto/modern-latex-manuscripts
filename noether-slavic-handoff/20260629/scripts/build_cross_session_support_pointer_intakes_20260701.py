"""Build verified pointer intakes for 2026-07-01 cross-session support notes.

The generated artifacts are pointer-only. They record local file hashes and
delegated counts without copying source prose, source excerpts, source-language
terms, credentials, or tokens into the Noether branch payload.
"""

from __future__ import annotations

import datetime
import hashlib
import json
import pathlib
import re


BASE = pathlib.Path(__file__).resolve().parents[1]
STATUS_MANIFEST = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_MANIFEST_20260629.json"
STATUS_INDEX = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_INDEX_20260629.md"
SELF_PATH = pathlib.Path(__file__).resolve()

SOURCE_AWARE_OUT_JSON = BASE / "SOURCE_AWARE_PACKET_START_OLP_POINTER_INTAKE_20260701.json"
SOURCE_AWARE_OUT_MD = BASE / "SOURCE_AWARE_PACKET_START_OLP_POINTER_INTAKE_20260701.md"
RELATION_OUT_JSON = BASE / "SEMI_CONSTRUCTED_RELATION_FUNCTION_REVIEWER_SHEET_INTAKE_20260701.json"
RELATION_OUT_MD = BASE / "SEMI_CONSTRUCTED_RELATION_FUNCTION_REVIEWER_SHEET_INTAKE_20260701.md"

SOURCE_THREAD_ID = "019f1343-5922-78d3-b58e-6584dc556a14"
SOURCE_AWARE_STATUS = "methodology_support_cohort_source_aware_olp_pointer_hash_verified_not_canonical"
RELATION_STATUS = "methodology_support_cohort_relation_function_reviewer_sheet_pointer_hash_verified_not_canonical"

SOURCE_AWARE_POINTERS = [
    {
        "pointer_id": "source_aware_translation_packet_start_queue_20260630T215341Z",
        "path": pathlib.Path(
            r"C:\Users\memo_\Documents\Codex\2026-06-29\files-mentioned-by-the-user-worked\outputs"
            r"\SOURCE_AWARE_TRANSLATION_PACKET_START_QUEUE_20260630T215341Z.md"
        ),
        "declared_role_from_delegation": "open_source_packet_start_sequencing",
    },
    {
        "pointer_id": "olp_first_proof_excerpt_candidate_sidecar_20260630T215627Z",
        "path": pathlib.Path(
            r"C:\Users\memo_\Documents\Codex\2026-06-29\files-mentioned-by-the-user-worked\outputs"
            r"\OLP_FIRST_PROOF_EXCERPT_CANDIDATE_SIDECAR_20260630T215627Z.md"
        ),
        "declared_role_from_delegation": "olp_proof_literacy_source_pointer_candidate_rows",
    },
]

RELATION_SOURCE = pathlib.Path(
    r"C:\Users\memo_\Documents\Codex\2026-06-29\files-mentioned-by-the-user-worked\outputs"
    r"\SEMI_CONSTRUCTED_RELATION_FUNCTION_SEMANTIC_SLOT_REVIEWER_SHEET_BLANK_20260701T223000Z.md"
)
RELATION_RETURN_LEDGER = pathlib.Path(
    r"C:\Users\memo_\Documents\Codex\2026-06-29\files-mentioned-by-the-user-worked\outputs"
    r"\SEMI_CONSTRUCTED_RELATION_FUNCTION_SEMANTIC_SLOT_RETURN_LEDGER_TEMPLATE_20260701T230000Z.md"
)
RELATION_SELECTOR_MAP = pathlib.Path(
    r"C:\Users\memo_\Documents\Codex\2026-06-29\files-mentioned-by-the-user-worked\outputs"
    r"\SEMI_CONSTRUCTED_RELATION_FUNCTION_SEMANTIC_SLOT_SOURCE_SHELF_SELECTOR_MAP_20260701T231500Z.md"
)
RELATION_SOURCE_REQUEST = pathlib.Path(
    r"C:\Users\memo_\Documents\Codex\2026-06-29\files-mentioned-by-the-user-worked\outputs"
    r"\SEMI_CONSTRUCTED_RELATION_FUNCTION_SEMANTIC_SLOT_SOURCE_REQUEST_PACKET_20260701T233000Z.md"
)
RELATION_DISPATCH_CHECKLIST = pathlib.Path(
    r"C:\Users\memo_\Documents\Codex\2026-06-29\files-mentioned-by-the-user-worked\outputs"
    r"\SEMI_CONSTRUCTED_RELATION_FUNCTION_SEMANTIC_SLOT_SOURCE_REQUEST_DISPATCH_READINESS_CHECKLIST_20260701T234500Z.md"
)
RELATION_BLOCKER_QUEUE = pathlib.Path(
    r"C:\Users\memo_\Documents\Codex\2026-06-29\files-mentioned-by-the-user-worked\outputs"
    r"\SEMI_CONSTRUCTED_RELATION_FUNCTION_SEMANTIC_SLOT_SOURCE_REQUEST_DISPATCH_BLOCKER_QUEUE_20260701T235800Z.md"
)
RELATION_BLOCKER_COORDINATION_NOTE = pathlib.Path(
    r"C:\Users\memo_\Documents\Codex\2026-06-29\files-mentioned-by-the-user-worked\outputs"
    r"\RELATION_FUNCTION_SEMANTIC_SLOT_SOURCE_REQUEST_DISPATCH_BLOCKER_QUEUE_COORDINATION_NOTE_20260701T235900Z.md"
)
RELATION_BLOCKER_EVIDENCE_INTAKE_LEDGER = pathlib.Path(
    r"C:\Users\memo_\Documents\Codex\2026-06-29\files-mentioned-by-the-user-worked\outputs"
    r"\SEMI_CONSTRUCTED_RELATION_FUNCTION_SEMANTIC_SLOT_SOURCE_REQUEST_DISPATCH_BLOCKER_EVIDENCE_INTAKE_LEDGER_TEMPLATE_20260702T001500Z.md"
)
RELATION_BLOCKER_EVIDENCE_COORDINATION_NOTE = pathlib.Path(
    r"C:\Users\memo_\Documents\Codex\2026-06-29\files-mentioned-by-the-user-worked\outputs"
    r"\RELATION_FUNCTION_SEMANTIC_SLOT_SOURCE_REQUEST_DISPATCH_BLOCKER_EVIDENCE_INTAKE_LEDGER_TEMPLATE_COORDINATION_NOTE_20260702T001600Z.md"
)
RELATION_EVIDENCE_CRITERIA_TAXONOMY = pathlib.Path(
    r"C:\Users\memo_\Documents\Codex\2026-06-29\files-mentioned-by-the-user-worked\outputs"
    r"\SEMI_CONSTRUCTED_RELATION_FUNCTION_SEMANTIC_SLOT_SOURCE_REQUEST_DISPATCH_EVIDENCE_CRITERIA_AND_ROUTE_LABEL_TAXONOMY_20260702T003000Z.md"
)
RELATION_EVIDENCE_CRITERIA_TAXONOMY_COORDINATION_NOTE = pathlib.Path(
    r"C:\Users\memo_\Documents\Codex\2026-06-29\files-mentioned-by-the-user-worked\outputs"
    r"\RELATION_FUNCTION_SEMANTIC_SLOT_SOURCE_REQUEST_DISPATCH_EVIDENCE_CRITERIA_ROUTE_LABEL_TAXONOMY_COORDINATION_NOTE_20260702T003100Z.md"
)
RELATION_ROUTE_EVIDENCE_DISCOVERY_LEDGER = pathlib.Path(
    r"C:\Users\memo_\Documents\Codex\2026-06-29\files-mentioned-by-the-user-worked\outputs"
    r"\SEMI_CONSTRUCTED_RELATION_FUNCTION_SEMANTIC_SLOT_SOURCE_REQUEST_ROUTE_EVIDENCE_DISCOVERY_LEDGER_20260702T004500Z.md"
)
RELATION_ROUTE_EVIDENCE_DISCOVERY_COORDINATION_NOTE = pathlib.Path(
    r"C:\Users\memo_\Documents\Codex\2026-06-29\files-mentioned-by-the-user-worked\outputs"
    r"\RELATION_FUNCTION_SEMANTIC_SLOT_SOURCE_REQUEST_ROUTE_EVIDENCE_DISCOVERY_LEDGER_COORDINATION_NOTE_20260702T004600Z.md"
)
RELATION_ROUTE_EVIDENCE_FOUND_CAPTURE = pathlib.Path(
    r"C:\Users\memo_\Documents\Codex\2026-06-29\files-mentioned-by-the-user-worked\outputs"
    r"\SEMI_CONSTRUCTED_RELATION_FUNCTION_SEMANTIC_SLOT_SOURCE_REQUEST_ROUTE_EVIDENCE_DISCOVERY_LEDGER_WITH_FOUND_EVIDENCE_20260702T011500Z.md"
)
RELATION_ROUTE_EVIDENCE_FOUND_CAPTURE_COORDINATION_NOTE = pathlib.Path(
    r"C:\Users\memo_\Documents\Codex\2026-06-29\files-mentioned-by-the-user-worked\outputs"
    r"\RELATION_FUNCTION_SEMANTIC_SLOT_SOURCE_REQUEST_ROUTE_EVIDENCE_CANDIDATE_CAPTURE_COORDINATION_NOTE_20260702T011600Z.md"
)
RELATION_OWNER_LOCAL_STANDARD_ROUTE_SEARCH = pathlib.Path(
    r"C:\Users\memo_\Documents\Codex\2026-06-29\files-mentioned-by-the-user-worked\outputs"
    r"\SEMI_CONSTRUCTED_RELATION_FUNCTION_SEMANTIC_SLOT_SOURCE_REQUEST_OWNER_AND_LOCAL_STANDARD_ROUTE_SEARCH_20260702T013000Z.md"
)
RELATION_OWNER_LOCAL_STANDARD_ROUTE_SEARCH_COORDINATION_NOTE = pathlib.Path(
    r"C:\Users\memo_\Documents\Codex\2026-06-29\files-mentioned-by-the-user-worked\outputs"
    r"\RELATION_FUNCTION_SEMANTIC_SLOT_SOURCE_REQUEST_OWNER_LOCAL_STANDARD_ROUTE_SEARCH_COORDINATION_NOTE_20260702T013100Z.md"
)
RELATION_LOCAL_STANDARD_SCOPE_SELECTOR = pathlib.Path(
    r"C:\Users\memo_\Documents\Codex\2026-06-29\files-mentioned-by-the-user-worked\outputs"
    r"\SEMI_CONSTRUCTED_RELATION_FUNCTION_SEMANTIC_SLOT_SOURCE_REQUEST_LOCAL_STANDARD_SCOPE_SELECTOR_20260702T014500Z.md"
)
RELATION_LOCAL_STANDARD_SCOPE_SELECTOR_COORDINATION_NOTE = pathlib.Path(
    r"C:\Users\memo_\Documents\Codex\2026-06-29\files-mentioned-by-the-user-worked\outputs"
    r"\RELATION_FUNCTION_SEMANTIC_SLOT_SOURCE_REQUEST_LOCAL_STANDARD_SCOPE_SELECTOR_COORDINATION_NOTE_20260702T014600Z.md"
)
RELATION_LOCAL_STANDARD_SCOPE_SOURCE_AUDIT = pathlib.Path(
    r"C:\Users\memo_\Documents\Codex\2026-06-29\files-mentioned-by-the-user-worked\outputs"
    r"\SEMI_CONSTRUCTED_RELATION_FUNCTION_SEMANTIC_SLOT_SOURCE_REQUEST_LOCAL_STANDARD_SCOPE_SOURCE_AUDIT_20260702T020000Z.md"
)
RELATION_LOCAL_STANDARD_SCOPE_SOURCE_AUDIT_COORDINATION_NOTE = pathlib.Path(
    r"C:\Users\memo_\Documents\Codex\2026-06-29\files-mentioned-by-the-user-worked\outputs"
    r"\RELATION_FUNCTION_SEMANTIC_SLOT_SOURCE_REQUEST_LOCAL_STANDARD_SCOPE_SOURCE_AUDIT_COORDINATION_NOTE_20260702T020100Z.md"
)
RELATION_LOCAL_STANDARD_SCOPE_OFFICIAL_CACHE_RETRY = pathlib.Path(
    r"C:\Users\memo_\Documents\Codex\2026-06-29\files-mentioned-by-the-user-worked\outputs"
    r"\SEMI_CONSTRUCTED_RELATION_FUNCTION_SEMANTIC_SLOT_SOURCE_REQUEST_LOCAL_STANDARD_SCOPE_OFFICIAL_CACHE_RETRY_WITH_HASHES_20260702T021500Z.md"
)
RELATION_LOCAL_STANDARD_SCOPE_OFFICIAL_CACHE_RETRY_COORDINATION_NOTE = pathlib.Path(
    r"C:\Users\memo_\Documents\Codex\2026-06-29\files-mentioned-by-the-user-worked\outputs"
    r"\RELATION_FUNCTION_SEMANTIC_SLOT_SOURCE_REQUEST_LOCAL_STANDARD_SCOPE_OFFICIAL_CACHE_RETRY_COORDINATION_NOTE_20260702T021600Z.md"
)
RELATION_LOCAL_STANDARD_SCOPE_GAP_ROUTE_SEARCH = pathlib.Path(
    r"C:\Users\memo_\Documents\Codex\2026-06-29\files-mentioned-by-the-user-worked\outputs"
    r"\SEMI_CONSTRUCTED_RELATION_FUNCTION_SEMANTIC_SLOT_SOURCE_REQUEST_LOCAL_STANDARD_SCOPE_GAP_ROUTE_SEARCH_20260702T023000Z.md"
)
RELATION_LOCAL_STANDARD_SCOPE_GAP_ROUTE_SEARCH_COORDINATION_NOTE = pathlib.Path(
    r"C:\Users\memo_\Documents\Codex\2026-06-29\files-mentioned-by-the-user-worked\outputs"
    r"\RELATION_FUNCTION_SEMANTIC_SLOT_SOURCE_REQUEST_LOCAL_STANDARD_SCOPE_GAP_ROUTE_SEARCH_COORDINATION_NOTE_20260702T023100Z.md"
)
RELATION_LOCAL_STANDARD_SCOPE_GAP_SOURCE_AUDIT = pathlib.Path(
    r"C:\Users\memo_\Documents\Codex\2026-06-29\files-mentioned-by-the-user-worked\outputs"
    r"\SEMI_CONSTRUCTED_RELATION_FUNCTION_SEMANTIC_SLOT_SOURCE_REQUEST_LOCAL_STANDARD_SCOPE_GAP_SOURCE_AUDIT_20260702T024500Z.md"
)
RELATION_LOCAL_STANDARD_SCOPE_GAP_SOURCE_AUDIT_COORDINATION_NOTE = pathlib.Path(
    r"C:\Users\memo_\Documents\Codex\2026-06-29\files-mentioned-by-the-user-worked\outputs"
    r"\RELATION_FUNCTION_SEMANTIC_SLOT_SOURCE_REQUEST_LOCAL_STANDARD_SCOPE_GAP_SOURCE_AUDIT_COORDINATION_NOTE_20260702T024600Z.md"
)
RELATION_LOCAL_STANDARD_SCOPE_FAILED_ROUTE_RETRY = pathlib.Path(
    r"C:\Users\memo_\Documents\Codex\2026-06-29\files-mentioned-by-the-user-worked\outputs"
    r"\SEMI_CONSTRUCTED_RELATION_FUNCTION_SEMANTIC_SLOT_SOURCE_REQUEST_LOCAL_STANDARD_SCOPE_FAILED_ROUTE_RETRY_20260702T030000Z.md"
)
RELATION_LOCAL_STANDARD_SCOPE_FAILED_ROUTE_RETRY_COORDINATION_NOTE = pathlib.Path(
    r"C:\Users\memo_\Documents\Codex\2026-06-29\files-mentioned-by-the-user-worked\outputs"
    r"\RELATION_FUNCTION_SEMANTIC_SLOT_SOURCE_REQUEST_LOCAL_STANDARD_SCOPE_FAILED_ROUTE_RETRY_COORDINATION_NOTE_20260702T030100Z.md"
)
RELATION_LOCAL_STANDARD_SCOPE_ALTERNATE_ROUTE_SEARCH = pathlib.Path(
    r"C:\Users\memo_\Documents\Codex\2026-06-29\files-mentioned-by-the-user-worked\outputs"
    r"\SEMI_CONSTRUCTED_RELATION_FUNCTION_SEMANTIC_SLOT_SOURCE_REQUEST_LOCAL_STANDARD_SCOPE_ALTERNATE_ROUTE_SEARCH_20260702T031500Z.md"
)
RELATION_LOCAL_STANDARD_SCOPE_ALTERNATE_ROUTE_SEARCH_COORDINATION_NOTE = pathlib.Path(
    r"C:\Users\memo_\Documents\Codex\2026-06-29\files-mentioned-by-the-user-worked\outputs"
    r"\RELATION_FUNCTION_SEMANTIC_SLOT_SOURCE_REQUEST_LOCAL_STANDARD_SCOPE_ALTERNATE_ROUTE_SEARCH_COORDINATION_NOTE_20260702T031600Z.md"
)
TOOL_REPAIR_DIR = pathlib.Path(
    r"C:\Users\memo_\Documents\Codex\2026-06-29\files-mentioned-by-the-user-worked\tools\codex_repair"
)
TOOL_REPAIR_LAUNCHERS = ["portable_node.cmd", "portable_node.ps1", "portable_npm.cmd", "portable_npm.ps1"]


def now_utc() -> str:
    return datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="microseconds")


def sha256_path(path: pathlib.Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def load_json(path: pathlib.Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: pathlib.Path, data: dict) -> None:
    path.write_text(json.dumps(data, ensure_ascii=True, indent=2) + "\n", encoding="utf-8")


def artifact_path(path: pathlib.Path) -> str:
    return "noether-slavic-handoff/20260629/" + path.relative_to(BASE).as_posix()


def artifact_local_path(path_from_manifest: str) -> pathlib.Path:
    rel = path_from_manifest.split("20260629/", 1)[-1]
    return BASE / rel


def artifact_item(path: pathlib.Path, status: str | None = None) -> dict:
    item = {"path": artifact_path(path), "sha256": sha256_path(path), "bytes": path.stat().st_size}
    if status:
        item["status"] = status
    return item


def upsert_artifact(manifest: dict, group: str, path: pathlib.Path, status: str | None = None) -> None:
    by_path = {item["path"]: item for item in manifest["artifacts"][group]}
    rel = artifact_path(path)
    previous_status = by_path.get(rel, {}).get("status")
    by_path[rel] = artifact_item(path, status or previous_status)
    manifest["artifacts"][group] = [by_path[key] for key in sorted(by_path)]


def refresh_existing_artifact_hashes(manifest: dict) -> None:
    for group in ("json", "markdown", "scripts"):
        refreshed = []
        for item in manifest["artifacts"][group]:
            path = artifact_local_path(item["path"])
            if path.exists() and path.is_file():
                updated = dict(item)
                updated["sha256"] = sha256_path(path)
                updated["bytes"] = path.stat().st_size
                refreshed.append(updated)
            else:
                refreshed.append(item)
        manifest["artifacts"][group] = refreshed


def file_pointer_metadata(path: pathlib.Path) -> dict:
    exists = path.exists() and path.is_file()
    metadata = {
        "path": str(path),
        "source_note_exists": exists,
        "source_note_bytes": path.stat().st_size if exists else 0,
        "source_note_sha256": sha256_path(path) if exists else "",
        "source_note_mtime_utc": (
            datetime.datetime.fromtimestamp(path.stat().st_mtime, datetime.timezone.utc).isoformat(timespec="seconds")
            if exists
            else ""
        ),
        "source_body_copied": False,
        "source_excerpt_copied": False,
        "source_language_terms_copied": False,
    }
    metadata["hash_verified"] = bool(metadata["source_note_sha256"])
    return metadata


def build_source_aware_document() -> dict:
    pointers = []
    for pointer in SOURCE_AWARE_POINTERS:
        pointers.append(
            {
                "pointer_id": pointer["pointer_id"],
                "declared_role_from_delegation": pointer["declared_role_from_delegation"],
                **file_pointer_metadata(pointer["path"]),
            }
        )
    return {
        "artifact": "source_aware_packet_start_olp_pointer_intake",
        "status": SOURCE_AWARE_STATUS,
        "generated_date": "2026-07-01",
        "generated_utc": now_utc(),
        "source_thread_id": SOURCE_THREAD_ID,
        "bandwidth_mode": "local_only_no_network_actions",
        "source_pointers": pointers,
        "intake_policy": {
            "branch_role": "canonical_edition_lane_receiving_source_aware_olp_methodology_support_pointer",
            "methodology_support_cohort_material_only": True,
            "pointer_only": True,
            "local_hash_check_performed": True,
            "no_network_actions_performed": True,
            "source_note_body_copied": False,
            "source_note_excerpt_copied": False,
            "source_language_terms_copied": False,
            "credentials_or_tokens_copied": False,
        },
        "non_claim_boundaries": {
            "canonical_rows_resolved": False,
            "reviewer_packets_populated": False,
            "terms_confirmed": False,
            "excerpts_selected": False,
            "source_prose_copied": False,
            "translations_created": False,
            "constructed_surface_readiness_claim": False,
            "publication_readiness_claim": False,
            "pilot_readiness_claim": False,
        },
        "totals": {
            "source_pointers": len(pointers),
            "source_pointers_with_hash_verified": sum(1 for pointer in pointers if pointer["hash_verified"]),
            "canonical_rows_resolved": 0,
            "reviewer_packet_rows_populated": 0,
            "terms_confirmed": 0,
            "excerpts_selected": 0,
            "source_prose_copied": 0,
            "translations_created": 0,
            "network_actions": 0,
        },
    }


def build_relation_document() -> dict:
    source_pointers = [
        {
            "pointer_id": "semi_constructed_relation_function_semantic_slot_reviewer_sheet_blank_20260701T223000Z",
            "declared_role_from_delegation": "blank_relation_function_semantic_slot_reviewer_sheet",
            "delegated_rows": 20,
            "delegated_questions": 60,
            "package_order": 54,
            "queue_candidate_count": 166,
            **file_pointer_metadata(RELATION_SOURCE),
        },
        {
            "pointer_id": "semi_constructed_relation_function_semantic_slot_return_ledger_template_20260701T230000Z",
            "declared_role_from_delegation": "blank_relation_function_semantic_slot_return_ledger_template",
            "delegated_rows": 20,
            "delegated_questions": 0,
            "package_order": 55,
            "queue_candidate_count": 167,
            **file_pointer_metadata(RELATION_RETURN_LEDGER),
        },
        {
            "pointer_id": "semi_constructed_relation_function_semantic_slot_source_shelf_selector_map_20260701T231500Z",
            "declared_role_from_delegation": "metadata_only_relation_function_source_shelf_selector_map",
            "selector_rows": 20,
            "term_family_shelves": 8,
            "coordinate_rows": 1438,
            "source_paths_with_hits": 80,
            "package_order": 56,
            "queue_candidate_count": 168,
            **file_pointer_metadata(RELATION_SELECTOR_MAP),
        },
        {
            "pointer_id": "semi_constructed_relation_function_semantic_slot_source_request_packet_20260701T233000Z",
            "declared_role_from_delegation": "metadata_only_relation_function_source_request_packet_unsent",
            "request_rows": 20,
            "request_questions": 60,
            "source_path_slots": 120,
            "coordinate_id_slots": 200,
            "package_order": 57,
            "queue_candidate_count": 169,
            **file_pointer_metadata(RELATION_SOURCE_REQUEST),
        },
        {
            "pointer_id": "semi_constructed_relation_function_semantic_slot_source_request_dispatch_readiness_checklist_20260701T234500Z",
            "declared_role_from_delegation": "metadata_only_relation_function_source_request_dispatch_readiness_checklist",
            "checklist_rows": 20,
            "checks_total": 220,
            "metadata_checks_passed": 120,
            "dispatch_prerequisites_failed": 100,
            "ready_for_dispatch_rows": 0,
            "package_order": 58,
            "queue_candidate_count": 170,
            **file_pointer_metadata(RELATION_DISPATCH_CHECKLIST),
        },
        {
            "pointer_id": "semi_constructed_relation_function_semantic_slot_source_request_dispatch_blocker_queue_20260701T235800Z",
            "declared_role_from_delegation": "metadata_only_relation_function_source_request_dispatch_blocker_queue",
            "open_blocker_rows": 100,
            "blocker_classes": 5,
            "blockers_per_class": 20,
            "blockers_resolved": 0,
            "package_order": 59,
            "queue_candidate_count": 171,
            **file_pointer_metadata(RELATION_BLOCKER_QUEUE),
        },
        {
            "pointer_id": "relation_function_semantic_slot_source_request_dispatch_blocker_queue_coordination_note_20260701T235900Z",
            "declared_role_from_delegation": "metadata_only_relation_function_blocker_queue_coordination_note",
            "package_order": 59,
            "queue_candidate_count": 171,
            **file_pointer_metadata(RELATION_BLOCKER_COORDINATION_NOTE),
        },
        {
            "pointer_id": "semi_constructed_relation_function_semantic_slot_source_request_dispatch_blocker_evidence_intake_ledger_template_20260702T001500Z",
            "declared_role_from_delegation": "blank_relation_function_dispatch_blocker_evidence_intake_ledger_template",
            "blank_intake_rows": 100,
            "blocker_classes": 5,
            "rows_per_class": 20,
            "evidence_artifacts_linked": 0,
            "evidence_rows_filled": 0,
            "route_assignments_created": 0,
            "package_order": 60,
            "queue_candidate_count": 172,
            **file_pointer_metadata(RELATION_BLOCKER_EVIDENCE_INTAKE_LEDGER),
        },
        {
            "pointer_id": "relation_function_semantic_slot_source_request_dispatch_blocker_evidence_intake_ledger_template_coordination_note_20260702T001600Z",
            "declared_role_from_delegation": "metadata_only_relation_function_blocker_evidence_intake_ledger_coordination_note",
            "package_order": 60,
            "queue_candidate_count": 172,
            **file_pointer_metadata(RELATION_BLOCKER_EVIDENCE_COORDINATION_NOTE),
        },
        {
            "pointer_id": "semi_constructed_relation_function_semantic_slot_source_request_dispatch_evidence_criteria_and_route_label_taxonomy_20260702T003000Z",
            "declared_role_from_delegation": "metadata_only_relation_function_dispatch_evidence_criteria_route_label_taxonomy",
            "taxonomy_rows": 9,
            "criteria_rows": 100,
            "blocker_classes": 5,
            "criteria_rows_per_blocker_class": 20,
            "evidence_artifacts_linked": 0,
            "evidence_rows_filled": 0,
            "route_label_classes_applied": 0,
            "blockers_resolved": 0,
            "route_assignments_created": 0,
            "package_order": 61,
            "queue_candidate_count": 173,
            **file_pointer_metadata(RELATION_EVIDENCE_CRITERIA_TAXONOMY),
        },
        {
            "pointer_id": "relation_function_semantic_slot_source_request_dispatch_evidence_criteria_route_label_taxonomy_coordination_note_20260702T003100Z",
            "declared_role_from_delegation": "metadata_only_relation_function_evidence_criteria_route_label_taxonomy_coordination_note",
            "package_order": 61,
            "queue_candidate_count": 173,
            **file_pointer_metadata(RELATION_EVIDENCE_CRITERIA_TAXONOMY_COORDINATION_NOTE),
        },
        {
            "pointer_id": "semi_constructed_relation_function_semantic_slot_source_request_route_evidence_discovery_ledger_20260702T004500Z",
            "declared_role_from_delegation": "metadata_only_relation_function_route_evidence_discovery_ledger_no_claim",
            "discovery_rows": 20,
            "inherited_criteria_rows": 100,
            "taxonomy_rows": 9,
            "local_candidate_reference_artifacts_considered": 6,
            "sufficient_evidence_artifacts_found": 0,
            "evidence_artifacts_linked": 0,
            "evidence_rows_filled": 0,
            "route_label_classes_applied": 0,
            "blockers_resolved": 0,
            "route_assignments_created": 0,
            "package_order": 62,
            "queue_candidate_count": 174,
            **file_pointer_metadata(RELATION_ROUTE_EVIDENCE_DISCOVERY_LEDGER),
        },
        {
            "pointer_id": "relation_function_semantic_slot_source_request_route_evidence_discovery_ledger_coordination_note_20260702T004600Z",
            "declared_role_from_delegation": "metadata_only_relation_function_route_evidence_discovery_coordination_note",
            "package_order": 62,
            "queue_candidate_count": 174,
            **file_pointer_metadata(RELATION_ROUTE_EVIDENCE_DISCOVERY_COORDINATION_NOTE),
        },
        {
            "pointer_id": "semi_constructed_relation_function_semantic_slot_source_request_route_evidence_discovery_ledger_with_found_evidence_20260702T011500Z",
            "declared_role_from_delegation": "metadata_only_relation_function_route_evidence_candidate_capture_no_assignment",
            "candidate_rows": 20,
            "official_current_route_license_pointers_cached": 6,
            "source_route_candidate_rows_found": 20,
            "dispatch_medium_candidate_rows_found": 20,
            "license_context_candidate_rows_found": 20,
            "owner_addressee_candidate_rows_found": 0,
            "local_standard_route_candidate_rows_found": 0,
            "evidence_intake_rows_filled": 0,
            "evidence_artifacts_linked_to_intake_rows": 0,
            "route_label_classes_applied": 0,
            "blockers_resolved": 0,
            "route_assignments_created": 0,
            "package_order": 63,
            "queue_candidate_count": 175,
            **file_pointer_metadata(RELATION_ROUTE_EVIDENCE_FOUND_CAPTURE),
        },
        {
            "pointer_id": "relation_function_semantic_slot_source_request_route_evidence_candidate_capture_coordination_note_20260702T011600Z",
            "declared_role_from_delegation": "metadata_only_relation_function_route_evidence_candidate_capture_coordination_note",
            "package_order": 63,
            "queue_candidate_count": 175,
            **file_pointer_metadata(RELATION_ROUTE_EVIDENCE_FOUND_CAPTURE_COORDINATION_NOTE),
        },
        {
            "pointer_id": "semi_constructed_relation_function_semantic_slot_source_request_owner_and_local_standard_route_search_20260702T013000Z",
            "declared_role_from_delegation": "metadata_only_relation_function_owner_local_standard_route_search_no_assignment",
            "search_rows": 20,
            "fetched_route_sources": 9,
            "candidate_pointers": 5,
            "project_issue_template_route_candidates_found": 20,
            "project_contribution_route_candidates_found": 20,
            "addressee_owner_route_candidates_found": 20,
            "non_personal_source_owner_roles_validated": 0,
            "local_standard_route_candidate_rows_found": 0,
            "evidence_intake_rows_filled": 0,
            "evidence_artifacts_linked_to_intake_rows": 0,
            "route_label_classes_applied": 0,
            "blockers_resolved": 0,
            "route_assignments_created": 0,
            "package_order": 64,
            "queue_candidate_count": 176,
            **file_pointer_metadata(RELATION_OWNER_LOCAL_STANDARD_ROUTE_SEARCH),
        },
        {
            "pointer_id": "relation_function_semantic_slot_source_request_owner_local_standard_route_search_coordination_note_20260702T013100Z",
            "declared_role_from_delegation": "metadata_only_relation_function_owner_local_standard_route_search_coordination_note",
            "package_order": 64,
            "queue_candidate_count": 176,
            **file_pointer_metadata(RELATION_OWNER_LOCAL_STANDARD_ROUTE_SEARCH_COORDINATION_NOTE),
        },
        {
            "pointer_id": "semi_constructed_relation_function_semantic_slot_source_request_local_standard_scope_selector_20260702T014500Z",
            "declared_role_from_delegation": "metadata_only_relation_function_local_standard_scope_selector_no_confirmation",
            "selector_rows": 20,
            "cataloged_scope_shelves": 3,
            "candidate_source_audit_rows": 5,
            "gap_only_rows": 15,
            "local_standard_routes_confirmed": 0,
            "local_authorities_confirmed": 0,
            "evidence_intake_rows_filled": 0,
            "blockers_resolved": 0,
            "route_label_classes_applied": 0,
            "route_assignments_created": 0,
            "package_order": 65,
            "queue_candidate_count": 177,
            **file_pointer_metadata(RELATION_LOCAL_STANDARD_SCOPE_SELECTOR),
        },
        {
            "pointer_id": "relation_function_semantic_slot_source_request_local_standard_scope_selector_coordination_note_20260702T014600Z",
            "declared_role_from_delegation": "metadata_only_relation_function_local_standard_scope_selector_coordination_note",
            "package_order": 65,
            "queue_candidate_count": 177,
            **file_pointer_metadata(RELATION_LOCAL_STANDARD_SCOPE_SELECTOR_COORDINATION_NOTE),
        },
        {
            "pointer_id": "semi_constructed_relation_function_semantic_slot_source_request_local_standard_scope_source_audit_20260702T020000Z",
            "declared_role_from_delegation": "metadata_only_relation_function_local_standard_scope_source_audit_no_confirmation",
            "source_audit_rows": 5,
            "inventory_rows": 10,
            "cache_file_checks": 9,
            "expected_hash_mismatches": 0,
            "official_primary_cache_gaps_carried_forward": 2,
            "proxy_supplementary_cache_rows_carried_forward": 2,
            "uc12_crosswalk_boundary_rows": 1,
            "local_standard_routes_confirmed": 0,
            "local_authorities_confirmed": 0,
            "source_audit_rows_sufficient_for_evidence_intake": 0,
            "evidence_intake_rows_filled": 0,
            "blockers_resolved": 0,
            "route_label_classes_applied": 0,
            "route_assignments_created": 0,
            "package_order": 66,
            "queue_candidate_count": 178,
            **file_pointer_metadata(RELATION_LOCAL_STANDARD_SCOPE_SOURCE_AUDIT),
        },
        {
            "pointer_id": "relation_function_semantic_slot_source_request_local_standard_scope_source_audit_coordination_note_20260702T020100Z",
            "declared_role_from_delegation": "metadata_only_relation_function_local_standard_scope_source_audit_coordination_note",
            "package_order": 66,
            "queue_candidate_count": 178,
            **file_pointer_metadata(RELATION_LOCAL_STANDARD_SCOPE_SOURCE_AUDIT_COORDINATION_NOTE),
        },
        {
            "pointer_id": "semi_constructed_relation_function_semantic_slot_source_request_local_standard_scope_official_cache_retry_with_hashes_20260702T021500Z",
            "declared_role_from_delegation": "metadata_only_relation_function_local_standard_scope_official_cache_retry_failure_evidence_no_confirmation",
            "selected_source_audit_rows": 5,
            "official_download_attempts": 3,
            "successful_downloads": 0,
            "failed_downloads": 3,
            "official_hashes_added": 0,
            "local_official_cache_files_added": 0,
            "exact_official_source_hashes_verified": 0,
            "page_count_checks_against_official_files": 0,
            "term_page_metadata_from_official_files": 0,
            "local_standard_routes_confirmed": 0,
            "local_authorities_confirmed": 0,
            "evidence_intake_rows_filled": 0,
            "blockers_resolved": 0,
            "route_label_classes_applied": 0,
            "route_assignments_created": 0,
            "package_order": 67,
            "queue_candidate_count": 179,
            **file_pointer_metadata(RELATION_LOCAL_STANDARD_SCOPE_OFFICIAL_CACHE_RETRY),
        },
        {
            "pointer_id": "relation_function_semantic_slot_source_request_local_standard_scope_official_cache_retry_coordination_note_20260702T021600Z",
            "declared_role_from_delegation": "metadata_only_relation_function_local_standard_scope_official_cache_retry_coordination_note",
            "package_order": 67,
            "queue_candidate_count": 179,
            **file_pointer_metadata(RELATION_LOCAL_STANDARD_SCOPE_OFFICIAL_CACHE_RETRY_COORDINATION_NOTE),
        },
        {
            "pointer_id": "semi_constructed_relation_function_semantic_slot_source_request_local_standard_scope_gap_route_search_20260702T023000Z",
            "declared_role_from_delegation": "metadata_only_relation_function_local_standard_scope_gap_route_search_no_confirmation",
            "gap_route_search_rows": 15,
            "candidate_source_route_rows": 7,
            "attempted_source_routes": 7,
            "successful_pdf_downloads": 3,
            "failed_pdf_route_retries": 4,
            "derived_text_cache_files": 3,
            "rows_with_candidate_route_cues": 13,
            "rows_still_explicit_gap_only": 2,
            "local_standard_routes_confirmed": 0,
            "local_authorities_confirmed": 0,
            "rows_sufficient_for_evidence_intake": 0,
            "evidence_intake_rows_filled": 0,
            "blockers_resolved": 0,
            "route_label_classes_applied": 0,
            "route_assignments_created": 0,
            "source_excerpts_copied_into_artifact": 0,
            "package_order": 68,
            "queue_candidate_count": 180,
            **file_pointer_metadata(RELATION_LOCAL_STANDARD_SCOPE_GAP_ROUTE_SEARCH),
        },
        {
            "pointer_id": "relation_function_semantic_slot_source_request_local_standard_scope_gap_route_search_coordination_note_20260702T023100Z",
            "declared_role_from_delegation": "metadata_only_relation_function_local_standard_scope_gap_route_search_coordination_note",
            "package_order": 68,
            "queue_candidate_count": 180,
            **file_pointer_metadata(RELATION_LOCAL_STANDARD_SCOPE_GAP_ROUTE_SEARCH_COORDINATION_NOTE),
        },
        {
            "pointer_id": "semi_constructed_relation_function_semantic_slot_source_request_local_standard_scope_gap_source_audit_20260702T024500Z",
            "declared_role_from_delegation": "metadata_only_relation_function_local_standard_scope_gap_source_audit_no_confirmation",
            "gap_source_audit_rows": 15,
            "source_route_audit_rows": 7,
            "cached_pdf_route_audits": 3,
            "failed_route_retry_rows_retained": 4,
            "text_cache_route_audits": 3,
            "text_page_segments_audited": 97,
            "rows_with_cached_term_route_cues": 13,
            "rows_still_explicit_gaps": 2,
            "local_standard_routes_confirmed": 0,
            "local_authorities_confirmed": 0,
            "rows_sufficient_for_evidence_intake": 0,
            "evidence_intake_rows_filled": 0,
            "blockers_resolved": 0,
            "route_label_classes_applied": 0,
            "route_assignments_created": 0,
            "source_excerpts_copied_into_artifact": 0,
            "package_order": 69,
            "queue_candidate_count": 181,
            **file_pointer_metadata(RELATION_LOCAL_STANDARD_SCOPE_GAP_SOURCE_AUDIT),
        },
        {
            "pointer_id": "relation_function_semantic_slot_source_request_local_standard_scope_gap_source_audit_coordination_note_20260702T024600Z",
            "declared_role_from_delegation": "metadata_only_relation_function_local_standard_scope_gap_source_audit_coordination_note",
            "package_order": 69,
            "queue_candidate_count": 181,
            **file_pointer_metadata(RELATION_LOCAL_STANDARD_SCOPE_GAP_SOURCE_AUDIT_COORDINATION_NOTE),
        },
        {
            "pointer_id": "semi_constructed_relation_function_semantic_slot_source_request_local_standard_scope_failed_route_retry_20260702T030000Z",
            "declared_role_from_delegation": "metadata_only_relation_function_local_standard_scope_failed_route_retry_no_confirmation",
            "failed_route_retry_rows": 4,
            "affected_gap_rows": 9,
            "externally_visible_routes": 4,
            "local_download_attempts": 12,
            "successful_pdf_downloads": 0,
            "failed_pdf_download_attempts": 12,
            "routes_still_without_local_pdf_cache": 4,
            "external_visibility_as_local_hash_evidence": False,
            "local_standard_routes_confirmed": 0,
            "local_authorities_confirmed": 0,
            "evidence_intake_rows_filled": 0,
            "blockers_resolved": 0,
            "route_label_classes_applied": 0,
            "route_assignments_created": 0,
            "dispatches": 0,
            "responses_ingested": 0,
            "source_excerpts_copied_into_artifact": 0,
            "package_order": 70,
            "queue_candidate_count": 182,
            **file_pointer_metadata(RELATION_LOCAL_STANDARD_SCOPE_FAILED_ROUTE_RETRY),
        },
        {
            "pointer_id": "relation_function_semantic_slot_source_request_local_standard_scope_failed_route_retry_coordination_note_20260702T030100Z",
            "declared_role_from_delegation": "metadata_only_relation_function_local_standard_scope_failed_route_retry_coordination_note",
            "package_order": 70,
            "queue_candidate_count": 182,
            **file_pointer_metadata(RELATION_LOCAL_STANDARD_SCOPE_FAILED_ROUTE_RETRY_COORDINATION_NOTE),
        },
        {
            "pointer_id": "semi_constructed_relation_function_semantic_slot_source_request_local_standard_scope_alternate_route_search_20260702T031500Z",
            "declared_role_from_delegation": "metadata_only_relation_function_local_standard_scope_alternate_route_search_no_confirmation",
            "alternate_route_rows": 7,
            "download_attempt_rows": 6,
            "official_external_alternates_found_but_not_locally_cached": 4,
            "valid_institutional_pdf_cache_files": 1,
            "derived_text_cache_files": 1,
            "partial_invalid_pdf_files_retained": 1,
            "partial_invalid_pdf_quarantined_unusable": True,
            "text_page_segments_audited": 187,
            "affected_gap_rows": 9,
            "affected_gap_rows_with_valid_cached_alternate_cues": 4,
            "telkom_http_fallback_metadata_only_route_evidence": True,
            "telkom_http_fallback_as_local_standard": False,
            "external_official_route_visibility_as_local_hash_evidence": False,
            "local_standard_routes_confirmed": 0,
            "local_authorities_confirmed": 0,
            "evidence_intake_rows_filled": 0,
            "route_assignments_created": 0,
            "dispatches": 0,
            "responses_ingested": 0,
            "source_excerpts_copied_into_artifact": 0,
            "translations_created": 0,
            "package_order": 71,
            "queue_candidate_count": 183,
            **file_pointer_metadata(RELATION_LOCAL_STANDARD_SCOPE_ALTERNATE_ROUTE_SEARCH),
        },
        {
            "pointer_id": "relation_function_semantic_slot_source_request_local_standard_scope_alternate_route_search_coordination_note_20260702T031600Z",
            "declared_role_from_delegation": "metadata_only_relation_function_local_standard_scope_alternate_route_search_coordination_note",
            "package_order": 71,
            "queue_candidate_count": 183,
            **file_pointer_metadata(RELATION_LOCAL_STANDARD_SCOPE_ALTERNATE_ROUTE_SEARCH_COORDINATION_NOTE),
        },
    ]
    tool_items = []
    if TOOL_REPAIR_DIR.exists() and TOOL_REPAIR_DIR.is_dir():
        for item in sorted(TOOL_REPAIR_DIR.iterdir(), key=lambda row: row.name):
            tool_items.append({"name": item.name, "is_file": item.is_file(), "bytes": item.stat().st_size if item.is_file() else 0})
    return {
        "artifact": "semi_constructed_relation_function_reviewer_sheet_intake",
        "status": RELATION_STATUS,
        "generated_date": "2026-07-01",
        "generated_utc": now_utc(),
        "source_thread_id": SOURCE_THREAD_ID,
        "bandwidth_mode": "local_only_no_network_actions",
        "tool_repair_pointer": {
            "path": str(TOOL_REPAIR_DIR),
            "declared_role_from_delegation": "portable_node_v24_18_0_cmd_launchers_dependency_path_repair",
            "directory_exists": TOOL_REPAIR_DIR.exists() and TOOL_REPAIR_DIR.is_dir(),
            "item_count": len(tool_items),
            "launcher_files_observed": [name for name in TOOL_REPAIR_LAUNCHERS if (TOOL_REPAIR_DIR / name).exists()],
            "items_observed": tool_items,
            "copied_into_noether_payload": False,
            "executed_by_noether_intake": False,
        },
        "source_pointers": source_pointers,
        "delegated_counts": {
            "reviewer_sheet_blank_semantic_slot_rows": 20,
            "reviewer_sheet_questions": 60,
            "reviewer_sheet_package_order": 54,
            "reviewer_sheet_queue_candidate_count": 166,
            "return_ledger_blank_rows": 20,
            "return_ledger_package_order": 55,
            "return_ledger_queue_candidate_count": 167,
            "selector_map_rows": 20,
            "selector_map_term_family_shelves": 8,
            "selector_map_coordinate_rows": 1438,
            "selector_map_source_paths_with_hits": 80,
            "selector_map_package_order": 56,
            "selector_map_queue_candidate_count": 168,
            "source_request_rows": 20,
            "source_request_questions": 60,
            "source_request_source_path_slots": 120,
            "source_request_coordinate_id_slots": 200,
            "source_request_package_order": 57,
            "source_request_queue_candidate_count": 169,
            "dispatch_checklist_rows": 20,
            "dispatch_checklist_checks_total": 220,
            "dispatch_checklist_metadata_checks_passed": 120,
            "dispatch_checklist_prerequisites_failed": 100,
            "dispatch_checklist_ready_for_dispatch_rows": 0,
            "dispatch_checklist_package_order": 58,
            "dispatch_checklist_queue_candidate_count": 170,
            "blocker_queue_open_rows": 100,
            "blocker_queue_classes": 5,
            "blocker_queue_rows_per_class": 20,
            "blocker_queue_resolved_rows": 0,
            "blocker_queue_package_order": 59,
            "blocker_queue_queue_candidate_count": 171,
            "blocker_coordination_note_present": True,
            "evidence_intake_ledger_blank_rows": 100,
            "evidence_intake_ledger_blocker_classes": 5,
            "evidence_intake_ledger_rows_per_class": 20,
            "evidence_intake_ledger_evidence_artifacts_linked": 0,
            "evidence_intake_ledger_evidence_rows_filled": 0,
            "evidence_intake_ledger_route_assignments_created": 0,
            "evidence_intake_ledger_package_order": 60,
            "evidence_intake_ledger_queue_candidate_count": 172,
            "evidence_intake_ledger_coordination_note_present": True,
            "evidence_criteria_route_label_taxonomy_rows": 9,
            "evidence_criteria_rows": 100,
            "evidence_criteria_blocker_classes": 5,
            "evidence_criteria_rows_per_blocker_class": 20,
            "evidence_criteria_evidence_artifacts_linked": 0,
            "evidence_criteria_evidence_rows_filled": 0,
            "evidence_criteria_route_label_classes_applied": 0,
            "evidence_criteria_blockers_resolved": 0,
            "evidence_criteria_route_assignments_created": 0,
            "evidence_criteria_package_order": 61,
            "evidence_criteria_queue_candidate_count": 173,
            "evidence_criteria_coordination_note_present": True,
            "route_evidence_discovery_rows": 20,
            "route_evidence_inherited_criteria_rows": 100,
            "route_evidence_taxonomy_rows": 9,
            "route_evidence_local_candidate_reference_artifacts_considered": 6,
            "route_evidence_sufficient_evidence_artifacts_found": 0,
            "route_evidence_artifacts_linked": 0,
            "route_evidence_rows_filled": 0,
            "route_evidence_route_label_classes_applied": 0,
            "route_evidence_blockers_resolved": 0,
            "route_evidence_route_assignments_created": 0,
            "route_evidence_package_order": 62,
            "route_evidence_queue_candidate_count": 174,
            "route_evidence_coordination_note_present": True,
            "route_evidence_candidate_capture_rows": 20,
            "route_evidence_official_route_license_pointers_cached": 6,
            "route_evidence_source_route_candidate_rows_found": 20,
            "route_evidence_dispatch_medium_candidate_rows_found": 20,
            "route_evidence_license_context_candidate_rows_found": 20,
            "route_evidence_owner_addressee_candidate_rows_found": 0,
            "route_evidence_local_standard_route_candidate_rows_found": 0,
            "route_evidence_capture_evidence_intake_rows_filled": 0,
            "route_evidence_capture_evidence_artifacts_linked_to_intake_rows": 0,
            "route_evidence_capture_route_label_classes_applied": 0,
            "route_evidence_capture_blockers_resolved": 0,
            "route_evidence_capture_route_assignments_created": 0,
            "route_evidence_capture_package_order": 63,
            "route_evidence_capture_queue_candidate_count": 175,
            "route_evidence_capture_coordination_note_present": True,
            "owner_local_standard_route_search_rows": 20,
            "owner_local_standard_fetched_route_sources": 9,
            "owner_local_standard_candidate_pointers": 5,
            "owner_local_standard_project_issue_template_route_candidates_found": 20,
            "owner_local_standard_project_contribution_route_candidates_found": 20,
            "owner_local_standard_addressee_owner_route_candidates_found": 20,
            "owner_local_standard_non_personal_source_owner_roles_validated": 0,
            "owner_local_standard_route_candidate_rows_found": 0,
            "owner_local_standard_evidence_intake_rows_filled": 0,
            "owner_local_standard_evidence_artifacts_linked_to_intake_rows": 0,
            "owner_local_standard_route_label_classes_applied": 0,
            "owner_local_standard_blockers_resolved": 0,
            "owner_local_standard_route_assignments_created": 0,
            "owner_local_standard_package_order": 64,
            "owner_local_standard_queue_candidate_count": 176,
            "owner_local_standard_coordination_note_present": True,
            "local_standard_scope_selector_rows": 20,
            "local_standard_cataloged_scope_shelves": 3,
            "local_standard_candidate_source_audit_rows": 5,
            "local_standard_gap_only_rows": 15,
            "local_standard_routes_confirmed": 0,
            "local_authorities_confirmed": 0,
            "local_standard_evidence_intake_rows_filled": 0,
            "local_standard_blockers_resolved": 0,
            "local_standard_route_label_classes_applied": 0,
            "local_standard_route_assignments_created": 0,
            "local_standard_package_order": 65,
            "local_standard_queue_candidate_count": 177,
            "local_standard_coordination_note_present": True,
            "local_standard_source_audit_rows": 5,
            "local_standard_source_audit_inventory_rows": 10,
            "local_standard_source_audit_cache_file_checks": 9,
            "local_standard_source_audit_expected_hash_mismatches": 0,
            "local_standard_source_audit_official_primary_cache_gaps_carried_forward": 2,
            "local_standard_source_audit_proxy_supplementary_cache_rows_carried_forward": 2,
            "local_standard_source_audit_uc12_crosswalk_boundary_rows": 1,
            "local_standard_source_audit_rows_sufficient_for_evidence_intake": 0,
            "local_standard_source_audit_evidence_intake_rows_filled": 0,
            "local_standard_source_audit_blockers_resolved": 0,
            "local_standard_source_audit_route_label_classes_applied": 0,
            "local_standard_source_audit_route_assignments_created": 0,
            "local_standard_source_audit_package_order": 66,
            "local_standard_source_audit_queue_candidate_count": 178,
            "local_standard_source_audit_coordination_note_present": True,
            "local_standard_official_cache_retry_selected_source_audit_rows": 5,
            "local_standard_official_cache_retry_download_attempts": 3,
            "local_standard_official_cache_retry_successful_downloads": 0,
            "local_standard_official_cache_retry_failed_downloads": 3,
            "local_standard_official_cache_retry_official_hashes_added": 0,
            "local_standard_official_cache_retry_local_official_cache_files_added": 0,
            "local_standard_official_cache_retry_exact_official_source_hashes_verified": 0,
            "local_standard_official_cache_retry_page_count_checks_against_official_files": 0,
            "local_standard_official_cache_retry_term_page_metadata_from_official_files": 0,
            "local_standard_official_cache_retry_evidence_intake_rows_filled": 0,
            "local_standard_official_cache_retry_blockers_resolved": 0,
            "local_standard_official_cache_retry_route_label_classes_applied": 0,
            "local_standard_official_cache_retry_route_assignments_created": 0,
            "local_standard_official_cache_retry_package_json_artifacts_with_matching_sha_sidecars": 9,
            "local_standard_official_cache_retry_recursive_json_parse_failures": 0,
            "local_standard_official_cache_retry_package_order": 67,
            "local_standard_official_cache_retry_queue_candidate_count": 179,
            "local_standard_official_cache_retry_coordination_note_present": True,
            "local_standard_gap_route_search_rows": 15,
            "local_standard_gap_route_candidate_source_route_rows": 7,
            "local_standard_gap_route_attempted_source_routes": 7,
            "local_standard_gap_route_successful_pdf_downloads": 3,
            "local_standard_gap_route_failed_pdf_route_retries": 4,
            "local_standard_gap_route_derived_text_cache_files": 3,
            "local_standard_gap_route_rows_with_candidate_route_cues": 13,
            "local_standard_gap_route_rows_still_explicit_gap_only": 2,
            "local_standard_gap_route_rows_sufficient_for_evidence_intake": 0,
            "local_standard_gap_route_evidence_intake_rows_filled": 0,
            "local_standard_gap_route_blockers_resolved": 0,
            "local_standard_gap_route_route_label_classes_applied": 0,
            "local_standard_gap_route_route_assignments_created": 0,
            "local_standard_gap_route_source_excerpts_copied_into_artifact": 0,
            "local_standard_gap_route_package_json_artifacts_with_matching_sha_sidecars": 10,
            "local_standard_gap_route_recursive_json_parse_failures": 0,
            "local_standard_gap_route_cached_pdf_text_hashes_match": True,
            "local_standard_gap_route_package_order": 68,
            "local_standard_gap_route_queue_candidate_count": 180,
            "local_standard_gap_route_coordination_note_present": True,
            "local_standard_gap_source_audit_rows": 15,
            "local_standard_gap_source_audit_source_route_rows": 7,
            "local_standard_gap_source_audit_cached_pdf_route_audits": 3,
            "local_standard_gap_source_audit_failed_route_retry_rows_retained": 4,
            "local_standard_gap_source_audit_text_cache_route_audits": 3,
            "local_standard_gap_source_audit_text_page_segments_audited": 97,
            "local_standard_gap_source_audit_rows_with_cached_term_route_cues": 13,
            "local_standard_gap_source_audit_rows_still_explicit_gaps": 2,
            "local_standard_gap_source_audit_rows_sufficient_for_evidence_intake": 0,
            "local_standard_gap_source_audit_evidence_intake_rows_filled": 0,
            "local_standard_gap_source_audit_blockers_resolved": 0,
            "local_standard_gap_source_audit_route_label_classes_applied": 0,
            "local_standard_gap_source_audit_route_assignments_created": 0,
            "local_standard_gap_source_audit_source_excerpts_copied_into_artifact": 0,
            "local_standard_gap_source_audit_package_json_artifacts_with_matching_sha_sidecars": 10,
            "local_standard_gap_source_audit_recursive_json_parse_failures": 0,
            "local_standard_gap_source_audit_cached_pdf_text_hashes_match": True,
            "local_standard_gap_source_audit_package_order": 69,
            "local_standard_gap_source_audit_queue_candidate_count": 181,
            "local_standard_gap_source_audit_coordination_note_present": True,
            "local_standard_failed_route_retry_rows": 4,
            "local_standard_failed_route_retry_affected_gap_rows": 9,
            "local_standard_failed_route_retry_externally_visible_routes": 4,
            "local_standard_failed_route_retry_local_download_attempts": 12,
            "local_standard_failed_route_retry_successful_pdf_downloads": 0,
            "local_standard_failed_route_retry_failed_pdf_download_attempts": 12,
            "local_standard_failed_route_retry_routes_still_without_local_pdf_cache": 4,
            "local_standard_failed_route_retry_external_visibility_as_local_hash_evidence": False,
            "local_standard_failed_route_retry_evidence_intake_rows_filled": 0,
            "local_standard_failed_route_retry_blockers_resolved": 0,
            "local_standard_failed_route_retry_route_label_classes_applied": 0,
            "local_standard_failed_route_retry_route_assignments_created": 0,
            "local_standard_failed_route_retry_dispatches": 0,
            "local_standard_failed_route_retry_responses_ingested": 0,
            "local_standard_failed_route_retry_source_excerpts_copied_into_artifact": 0,
            "local_standard_failed_route_retry_package_order": 70,
            "local_standard_failed_route_retry_queue_candidate_count": 182,
            "local_standard_failed_route_retry_coordination_note_present": True,
            "local_standard_alternate_route_rows": 7,
            "local_standard_alternate_route_download_attempt_rows": 6,
            "local_standard_alternate_route_official_external_alternates_found_but_not_locally_cached": 4,
            "local_standard_alternate_route_valid_institutional_pdf_cache_files": 1,
            "local_standard_alternate_route_derived_text_cache_files": 1,
            "local_standard_alternate_route_partial_invalid_pdf_files_retained": 1,
            "local_standard_alternate_route_partial_invalid_pdf_quarantined_unusable": True,
            "local_standard_alternate_route_text_page_segments_audited": 187,
            "local_standard_alternate_route_affected_gap_rows": 9,
            "local_standard_alternate_route_affected_gap_rows_with_valid_cached_alternate_cues": 4,
            "local_standard_alternate_route_telkom_http_fallback_metadata_only_route_evidence": True,
            "local_standard_alternate_route_telkom_http_fallback_as_local_standard": False,
            "local_standard_alternate_route_external_official_route_visibility_as_local_hash_evidence": False,
            "local_standard_alternate_route_evidence_intake_rows_filled": 0,
            "local_standard_alternate_route_assignments_created": 0,
            "local_standard_alternate_route_dispatches": 0,
            "local_standard_alternate_route_responses_ingested": 0,
            "local_standard_alternate_route_source_excerpts_copied_into_artifact": 0,
            "local_standard_alternate_route_translations_created": 0,
            "local_standard_alternate_route_package_order": 71,
            "local_standard_alternate_route_queue_candidate_count": 183,
            "local_standard_alternate_route_coordination_note_present": True,
            "root_output_json_files": 257,
            "recursive_output_json_files_checked": 350,
        },
        "intake_policy": {
            "branch_role": "canonical_edition_lane_receiving_relation_function_methodology_support_pointer",
            "methodology_support_cohort_material_only": True,
            "pointer_only": True,
            "local_hash_check_performed": True,
            "no_network_actions_performed": True,
            "source_note_body_copied": False,
            "source_note_excerpt_copied": False,
            "source_language_terms_copied": False,
            "credentials_or_tokens_copied": False,
        },
        "zero_gate_boundaries": {
            "returns": 0,
            "responses": 0,
            "blockers_resolved": 0,
            "sufficient_evidence_artifacts_found": 0,
            "evidence_artifacts_linked": 0,
            "evidence_rows_filled": 0,
            "route_label_classes_applied": 0,
            "route_assignments_created": 0,
            "local_standard_routes_confirmed": 0,
            "local_authorities_confirmed": 0,
            "source_audit_rows_sufficient_for_evidence_intake": 0,
            "official_hashes_added": 0,
            "local_official_cache_files_added": 0,
            "exact_official_source_hashes_verified": 0,
            "official_page_count_checks": 0,
            "official_term_page_metadata": 0,
            "gap_route_rows_sufficient_for_evidence_intake": 0,
            "gap_source_audit_rows_sufficient_for_evidence_intake": 0,
            "failed_route_external_visibility_promoted_to_local_hash_evidence": 0,
            "failed_route_retry_rows_sufficient_for_evidence_intake": 0,
            "alternate_route_rows_sufficient_for_evidence_intake": 0,
            "alternate_route_telkom_fallback_promoted_to_local_standard": 0,
            "alternate_route_partial_invalid_pdf_used_as_evidence": 0,
            "alternate_route_external_visibility_promoted_to_local_hash_evidence": 0,
            "surfaces": 0,
            "lexemes": 0,
            "morphemes": 0,
            "grammar": 0,
            "translation": 0,
            "source_excerpts": 0,
            "dispatches": 0,
            "pilot_readiness": 0,
            "publication_readiness": 0,
            "constructed_surface_readiness": 0,
            "canonical_rows_resolved": 0,
            "terms_confirmed": 0,
            "reviewer_packet_rows_populated": 0,
            "render_readiness_claim": 0,
            "review_readiness_claim": 0,
        },
        "totals": {
            "source_pointers": len(source_pointers),
            "tool_repair_pointers": 1,
            "source_pointers_with_hash_verified": sum(1 for pointer in source_pointers if pointer["hash_verified"]),
            "reviewer_sheet_blank_semantic_slot_rows": 20,
            "return_ledger_blank_rows": 20,
            "selector_map_rows": 20,
            "selector_map_term_family_shelves": 8,
            "selector_map_coordinate_rows": 1438,
            "selector_map_source_paths_with_hits": 80,
            "source_request_rows": 20,
            "source_request_questions": 60,
            "source_request_source_path_slots": 120,
            "source_request_coordinate_id_slots": 200,
            "dispatch_checklist_rows": 20,
            "dispatch_checklist_checks_total": 220,
            "dispatch_checklist_metadata_checks_passed": 120,
            "dispatch_checklist_prerequisites_failed": 100,
            "dispatch_checklist_ready_for_dispatch_rows": 0,
            "blocker_queue_open_rows": 100,
            "blocker_queue_classes": 5,
            "blocker_queue_rows_per_class": 20,
            "blocker_queue_resolved_rows": 0,
            "evidence_intake_ledger_blank_rows": 100,
            "evidence_intake_ledger_blocker_classes": 5,
            "evidence_intake_ledger_rows_per_class": 20,
            "evidence_intake_ledger_evidence_artifacts_linked": 0,
            "evidence_intake_ledger_evidence_rows_filled": 0,
            "evidence_intake_ledger_route_assignments_created": 0,
            "evidence_criteria_route_label_taxonomy_rows": 9,
            "evidence_criteria_rows": 100,
            "evidence_criteria_blocker_classes": 5,
            "evidence_criteria_rows_per_blocker_class": 20,
            "evidence_criteria_evidence_artifacts_linked": 0,
            "evidence_criteria_evidence_rows_filled": 0,
            "evidence_criteria_route_label_classes_applied": 0,
            "evidence_criteria_blockers_resolved": 0,
            "evidence_criteria_route_assignments_created": 0,
            "route_evidence_discovery_rows": 20,
            "route_evidence_inherited_criteria_rows": 100,
            "route_evidence_taxonomy_rows": 9,
            "route_evidence_local_candidate_reference_artifacts_considered": 6,
            "route_evidence_sufficient_evidence_artifacts_found": 0,
            "route_evidence_artifacts_linked": 0,
            "route_evidence_rows_filled": 0,
            "route_evidence_route_label_classes_applied": 0,
            "route_evidence_blockers_resolved": 0,
            "route_evidence_route_assignments_created": 0,
            "route_evidence_candidate_capture_rows": 20,
            "route_evidence_official_route_license_pointers_cached": 6,
            "route_evidence_source_route_candidate_rows_found": 20,
            "route_evidence_dispatch_medium_candidate_rows_found": 20,
            "route_evidence_license_context_candidate_rows_found": 20,
            "route_evidence_owner_addressee_candidate_rows_found": 0,
            "route_evidence_local_standard_route_candidate_rows_found": 0,
            "route_evidence_capture_evidence_intake_rows_filled": 0,
            "route_evidence_capture_evidence_artifacts_linked_to_intake_rows": 0,
            "route_evidence_capture_route_label_classes_applied": 0,
            "route_evidence_capture_blockers_resolved": 0,
            "route_evidence_capture_route_assignments_created": 0,
            "owner_local_standard_route_search_rows": 20,
            "owner_local_standard_fetched_route_sources": 9,
            "owner_local_standard_candidate_pointers": 5,
            "owner_local_standard_project_issue_template_route_candidates_found": 20,
            "owner_local_standard_project_contribution_route_candidates_found": 20,
            "owner_local_standard_addressee_owner_route_candidates_found": 20,
            "owner_local_standard_non_personal_source_owner_roles_validated": 0,
            "owner_local_standard_route_candidate_rows_found": 0,
            "owner_local_standard_evidence_intake_rows_filled": 0,
            "owner_local_standard_evidence_artifacts_linked_to_intake_rows": 0,
            "owner_local_standard_route_label_classes_applied": 0,
            "owner_local_standard_blockers_resolved": 0,
            "owner_local_standard_route_assignments_created": 0,
            "local_standard_scope_selector_rows": 20,
            "local_standard_cataloged_scope_shelves": 3,
            "local_standard_candidate_source_audit_rows": 5,
            "local_standard_gap_only_rows": 15,
            "local_standard_routes_confirmed": 0,
            "local_authorities_confirmed": 0,
            "local_standard_evidence_intake_rows_filled": 0,
            "local_standard_blockers_resolved": 0,
            "local_standard_route_label_classes_applied": 0,
            "local_standard_route_assignments_created": 0,
            "local_standard_source_audit_rows": 5,
            "local_standard_source_audit_inventory_rows": 10,
            "local_standard_source_audit_cache_file_checks": 9,
            "local_standard_source_audit_expected_hash_mismatches": 0,
            "local_standard_source_audit_official_primary_cache_gaps_carried_forward": 2,
            "local_standard_source_audit_proxy_supplementary_cache_rows_carried_forward": 2,
            "local_standard_source_audit_uc12_crosswalk_boundary_rows": 1,
            "local_standard_source_audit_rows_sufficient_for_evidence_intake": 0,
            "local_standard_source_audit_evidence_intake_rows_filled": 0,
            "local_standard_source_audit_blockers_resolved": 0,
            "local_standard_source_audit_route_label_classes_applied": 0,
            "local_standard_source_audit_route_assignments_created": 0,
            "local_standard_official_cache_retry_selected_source_audit_rows": 5,
            "local_standard_official_cache_retry_download_attempts": 3,
            "local_standard_official_cache_retry_successful_downloads": 0,
            "local_standard_official_cache_retry_failed_downloads": 3,
            "local_standard_official_cache_retry_official_hashes_added": 0,
            "local_standard_official_cache_retry_local_official_cache_files_added": 0,
            "local_standard_official_cache_retry_exact_official_source_hashes_verified": 0,
            "local_standard_official_cache_retry_page_count_checks_against_official_files": 0,
            "local_standard_official_cache_retry_term_page_metadata_from_official_files": 0,
            "local_standard_official_cache_retry_evidence_intake_rows_filled": 0,
            "local_standard_official_cache_retry_blockers_resolved": 0,
            "local_standard_official_cache_retry_route_label_classes_applied": 0,
            "local_standard_official_cache_retry_route_assignments_created": 0,
            "local_standard_official_cache_retry_package_json_artifacts_with_matching_sha_sidecars": 9,
            "local_standard_official_cache_retry_recursive_json_parse_failures": 0,
            "local_standard_gap_route_search_rows": 15,
            "local_standard_gap_route_candidate_source_route_rows": 7,
            "local_standard_gap_route_attempted_source_routes": 7,
            "local_standard_gap_route_successful_pdf_downloads": 3,
            "local_standard_gap_route_failed_pdf_route_retries": 4,
            "local_standard_gap_route_derived_text_cache_files": 3,
            "local_standard_gap_route_rows_with_candidate_route_cues": 13,
            "local_standard_gap_route_rows_still_explicit_gap_only": 2,
            "local_standard_gap_route_rows_sufficient_for_evidence_intake": 0,
            "local_standard_gap_route_evidence_intake_rows_filled": 0,
            "local_standard_gap_route_blockers_resolved": 0,
            "local_standard_gap_route_route_label_classes_applied": 0,
            "local_standard_gap_route_route_assignments_created": 0,
            "local_standard_gap_route_source_excerpts_copied_into_artifact": 0,
            "local_standard_gap_route_package_json_artifacts_with_matching_sha_sidecars": 10,
            "local_standard_gap_route_recursive_json_parse_failures": 0,
            "local_standard_gap_route_cached_pdf_text_hashes_match": True,
            "local_standard_gap_source_audit_rows": 15,
            "local_standard_gap_source_audit_source_route_rows": 7,
            "local_standard_gap_source_audit_cached_pdf_route_audits": 3,
            "local_standard_gap_source_audit_failed_route_retry_rows_retained": 4,
            "local_standard_gap_source_audit_text_cache_route_audits": 3,
            "local_standard_gap_source_audit_text_page_segments_audited": 97,
            "local_standard_gap_source_audit_rows_with_cached_term_route_cues": 13,
            "local_standard_gap_source_audit_rows_still_explicit_gaps": 2,
            "local_standard_gap_source_audit_rows_sufficient_for_evidence_intake": 0,
            "local_standard_gap_source_audit_evidence_intake_rows_filled": 0,
            "local_standard_gap_source_audit_blockers_resolved": 0,
            "local_standard_gap_source_audit_route_label_classes_applied": 0,
            "local_standard_gap_source_audit_route_assignments_created": 0,
            "local_standard_gap_source_audit_source_excerpts_copied_into_artifact": 0,
            "local_standard_gap_source_audit_package_json_artifacts_with_matching_sha_sidecars": 10,
            "local_standard_gap_source_audit_recursive_json_parse_failures": 0,
            "local_standard_gap_source_audit_cached_pdf_text_hashes_match": True,
            "local_standard_failed_route_retry_rows": 4,
            "local_standard_failed_route_retry_affected_gap_rows": 9,
            "local_standard_failed_route_retry_externally_visible_routes": 4,
            "local_standard_failed_route_retry_local_download_attempts": 12,
            "local_standard_failed_route_retry_successful_pdf_downloads": 0,
            "local_standard_failed_route_retry_failed_pdf_download_attempts": 12,
            "local_standard_failed_route_retry_routes_still_without_local_pdf_cache": 4,
            "local_standard_failed_route_retry_external_visibility_as_local_hash_evidence": False,
            "local_standard_failed_route_retry_evidence_intake_rows_filled": 0,
            "local_standard_failed_route_retry_blockers_resolved": 0,
            "local_standard_failed_route_retry_route_label_classes_applied": 0,
            "local_standard_failed_route_retry_route_assignments_created": 0,
            "local_standard_failed_route_retry_dispatches": 0,
            "local_standard_failed_route_retry_responses_ingested": 0,
            "local_standard_failed_route_retry_source_excerpts_copied_into_artifact": 0,
            "local_standard_alternate_route_rows": 7,
            "local_standard_alternate_route_download_attempt_rows": 6,
            "local_standard_alternate_route_official_external_alternates_found_but_not_locally_cached": 4,
            "local_standard_alternate_route_valid_institutional_pdf_cache_files": 1,
            "local_standard_alternate_route_derived_text_cache_files": 1,
            "local_standard_alternate_route_partial_invalid_pdf_files_retained": 1,
            "local_standard_alternate_route_partial_invalid_pdf_quarantined_unusable": True,
            "local_standard_alternate_route_text_page_segments_audited": 187,
            "local_standard_alternate_route_affected_gap_rows": 9,
            "local_standard_alternate_route_affected_gap_rows_with_valid_cached_alternate_cues": 4,
            "local_standard_alternate_route_telkom_http_fallback_metadata_only_route_evidence": True,
            "local_standard_alternate_route_telkom_http_fallback_as_local_standard": False,
            "local_standard_alternate_route_external_official_route_visibility_as_local_hash_evidence": False,
            "local_standard_alternate_route_evidence_intake_rows_filled": 0,
            "local_standard_alternate_route_assignments_created": 0,
            "local_standard_alternate_route_dispatches": 0,
            "local_standard_alternate_route_responses_ingested": 0,
            "local_standard_alternate_route_source_excerpts_copied_into_artifact": 0,
            "local_standard_alternate_route_translations_created": 0,
            "questions": 60,
            "max_package_order": 71,
            "max_queue_candidate_count": 183,
            "root_output_json_files": 257,
            "recursive_output_json_files_checked": 350,
            "network_actions": 0,
        },
    }


def write_source_aware_markdown(document: dict) -> None:
    lines = [
        "# Source-aware packet start and OLP pointer intake - 2026-07-01",
        "",
        "Status: hash-verified methodology/support-cohort pointer intake. This is not a canonical-edition update, not reviewer packet population, not term confirmation, not excerpt selection, not translation, and not a publication, constructed-surface, or pilot readiness claim.",
        "",
        "## Delegation Source",
        "",
        f"- Source thread: `{document['source_thread_id']}`",
        "- Delegated material: source-aware packet-start sequencing and OLP proof-literacy source-pointer candidate rows.",
        "- Network actions performed by this intake: `0`",
        "",
        "## Source Pointers",
        "",
        "| Pointer | Path | Bytes | SHA-256 | Role |",
        "| --- | --- | ---: | --- | --- |",
    ]
    for pointer in document["source_pointers"]:
        role = pointer["declared_role_from_delegation"].replace("_", " ")
        lines.append(
            f"| `{pointer['pointer_id']}` | `{pointer['path']}` | {pointer['source_note_bytes']} | `{pointer['source_note_sha256']}` | {role} |"
        )
    lines.extend(
        [
            "",
            "## Boundaries",
            "",
            "- Source note bodies and excerpts are not copied into this branch payload.",
            "- No source-language terms are copied.",
            "- No credentials or tokens are copied.",
            "- No canonical rows are resolved.",
            "- No reviewer packets are populated.",
            "- No terms are confirmed.",
            "- No excerpts are selected.",
            "- No source prose is copied.",
            "- No translations are created.",
            "- No constructed-surface, publication, or pilot readiness is claimed.",
            "",
        ]
    )
    SOURCE_AWARE_OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def write_relation_markdown(document: dict) -> None:
    counts = document["delegated_counts"]
    tool = document["tool_repair_pointer"]
    lines = [
        "# Semi-constructed relation/function reviewer sheet intake - 2026-07-01",
        "",
        "Status: hash-verified methodology/support-cohort pointer intake. This is not a canonical-edition update, not term confirmation, not reviewer packet population, not translation, and not render, review, publication, pilot, or constructed-surface readiness.",
        "",
        "## Delegation Source",
        "",
        f"- Source thread: `{document['source_thread_id']}`",
        "- Delegated material: relation/function semi-constructed translation-access reviewer sheet.",
        "- Network actions performed by this intake: `0`",
        "",
        "## Tool Repair Pointer",
        "",
        f"- Path: `{tool['path']}`",
        "- Declared role: portable Node.js v24.18.0 CMD launchers for dependency-path repair.",
        f"- Directory exists: `{str(tool['directory_exists']).lower()}`",
        f"- Items observed: `{tool['item_count']}`",
        f"- Launcher files observed: `{', '.join(tool['launcher_files_observed'])}`",
        "- Copied into Noether payload: `false`",
        "- Executed by this Noether intake: `false`",
        "",
        "## Source Pointer",
        "",
        "| Pointer | Path | Bytes | SHA-256 | Role |",
        "| --- | --- | ---: | --- | --- |",
    ]
    for pointer in document["source_pointers"]:
        role = pointer["declared_role_from_delegation"].replace("_", " ")
        lines.append(
            f"| `{pointer['pointer_id']}` | `{pointer['path']}` | {pointer['source_note_bytes']} | "
            f"`{pointer['source_note_sha256']}` | {role} |"
        )
    lines.extend(
        [
        "",
        "## Delegated Counts",
        "",
        f"- Reviewer sheet blank semantic-slot rows: `{counts['reviewer_sheet_blank_semantic_slot_rows']}`",
        f"- Reviewer sheet questions: `{counts['reviewer_sheet_questions']}`",
        f"- Reviewer sheet package order: `{counts['reviewer_sheet_package_order']}`",
        f"- Reviewer sheet queue candidate count: `{counts['reviewer_sheet_queue_candidate_count']}`",
        f"- Return ledger blank rows: `{counts['return_ledger_blank_rows']}`",
        f"- Return ledger package order: `{counts['return_ledger_package_order']}`",
        f"- Return ledger queue candidate count: `{counts['return_ledger_queue_candidate_count']}`",
        f"- Selector map rows: `{counts['selector_map_rows']}`",
        f"- Selector map term-family shelves: `{counts['selector_map_term_family_shelves']}`",
        f"- Selector map coordinate rows: `{counts['selector_map_coordinate_rows']}`",
        f"- Selector map source paths with hits: `{counts['selector_map_source_paths_with_hits']}`",
        f"- Selector map package order: `{counts['selector_map_package_order']}`",
        f"- Selector map queue candidate count: `{counts['selector_map_queue_candidate_count']}`",
        f"- Source request rows: `{counts['source_request_rows']}`",
        f"- Source request questions: `{counts['source_request_questions']}`",
        f"- Source request source-path slots: `{counts['source_request_source_path_slots']}`",
        f"- Source request coordinate-ID slots: `{counts['source_request_coordinate_id_slots']}`",
        f"- Source request package order: `{counts['source_request_package_order']}`",
        f"- Source request queue candidate count: `{counts['source_request_queue_candidate_count']}`",
        f"- Dispatch checklist rows: `{counts['dispatch_checklist_rows']}`",
        f"- Dispatch checklist checks total: `{counts['dispatch_checklist_checks_total']}`",
        f"- Dispatch checklist metadata checks passed: `{counts['dispatch_checklist_metadata_checks_passed']}`",
        f"- Dispatch checklist prerequisites failed: `{counts['dispatch_checklist_prerequisites_failed']}`",
        f"- Dispatch checklist ready-for-dispatch rows: `{counts['dispatch_checklist_ready_for_dispatch_rows']}`",
        f"- Dispatch checklist package order: `{counts['dispatch_checklist_package_order']}`",
        f"- Dispatch checklist queue candidate count: `{counts['dispatch_checklist_queue_candidate_count']}`",
        f"- Blocker queue open rows: `{counts['blocker_queue_open_rows']}`",
        f"- Blocker queue classes: `{counts['blocker_queue_classes']}`",
        f"- Blocker queue rows per class: `{counts['blocker_queue_rows_per_class']}`",
        f"- Blocker queue resolved rows: `{counts['blocker_queue_resolved_rows']}`",
        f"- Blocker queue package order: `{counts['blocker_queue_package_order']}`",
        f"- Blocker queue queue candidate count: `{counts['blocker_queue_queue_candidate_count']}`",
        f"- Blocker coordination note present: `{str(counts['blocker_coordination_note_present']).lower()}`",
        f"- Evidence-intake ledger blank rows: `{counts['evidence_intake_ledger_blank_rows']}`",
        f"- Evidence-intake ledger blocker classes: `{counts['evidence_intake_ledger_blocker_classes']}`",
        f"- Evidence-intake ledger rows per class: `{counts['evidence_intake_ledger_rows_per_class']}`",
        f"- Evidence artifacts linked: `{counts['evidence_intake_ledger_evidence_artifacts_linked']}`",
        f"- Evidence rows filled: `{counts['evidence_intake_ledger_evidence_rows_filled']}`",
        f"- Route assignments created: `{counts['evidence_intake_ledger_route_assignments_created']}`",
        f"- Evidence-intake ledger package order: `{counts['evidence_intake_ledger_package_order']}`",
        f"- Evidence-intake ledger queue candidate count: `{counts['evidence_intake_ledger_queue_candidate_count']}`",
        f"- Evidence-intake ledger coordination note present: `{str(counts['evidence_intake_ledger_coordination_note_present']).lower()}`",
        f"- Evidence criteria route-label taxonomy rows: `{counts['evidence_criteria_route_label_taxonomy_rows']}`",
        f"- Evidence criteria rows: `{counts['evidence_criteria_rows']}`",
        f"- Evidence criteria blocker classes: `{counts['evidence_criteria_blocker_classes']}`",
        f"- Evidence criteria rows per blocker class: `{counts['evidence_criteria_rows_per_blocker_class']}`",
        f"- Evidence criteria route-label classes applied: `{counts['evidence_criteria_route_label_classes_applied']}`",
        f"- Evidence criteria blockers resolved: `{counts['evidence_criteria_blockers_resolved']}`",
        f"- Evidence criteria route assignments created: `{counts['evidence_criteria_route_assignments_created']}`",
        f"- Evidence criteria package order: `{counts['evidence_criteria_package_order']}`",
        f"- Evidence criteria queue candidate count: `{counts['evidence_criteria_queue_candidate_count']}`",
        f"- Evidence criteria coordination note present: `{str(counts['evidence_criteria_coordination_note_present']).lower()}`",
        f"- Route-evidence discovery rows: `{counts['route_evidence_discovery_rows']}`",
        f"- Route-evidence inherited criteria rows: `{counts['route_evidence_inherited_criteria_rows']}`",
        f"- Route-evidence taxonomy rows: `{counts['route_evidence_taxonomy_rows']}`",
        f"- Route-evidence local candidate reference artifacts considered: `{counts['route_evidence_local_candidate_reference_artifacts_considered']}`",
        f"- Route-evidence sufficient evidence artifacts found: `{counts['route_evidence_sufficient_evidence_artifacts_found']}`",
        f"- Route-evidence artifacts linked: `{counts['route_evidence_artifacts_linked']}`",
        f"- Route-evidence rows filled: `{counts['route_evidence_rows_filled']}`",
        f"- Route-evidence route-label classes applied: `{counts['route_evidence_route_label_classes_applied']}`",
        f"- Route-evidence blockers resolved: `{counts['route_evidence_blockers_resolved']}`",
        f"- Route-evidence route assignments created: `{counts['route_evidence_route_assignments_created']}`",
        f"- Route-evidence package order: `{counts['route_evidence_package_order']}`",
        f"- Route-evidence queue candidate count: `{counts['route_evidence_queue_candidate_count']}`",
        f"- Route-evidence coordination note present: `{str(counts['route_evidence_coordination_note_present']).lower()}`",
        f"- Route-evidence candidate-capture rows: `{counts['route_evidence_candidate_capture_rows']}`",
        f"- Route-evidence official route/license pointers cached: `{counts['route_evidence_official_route_license_pointers_cached']}`",
        f"- Route-evidence source-route candidate rows found: `{counts['route_evidence_source_route_candidate_rows_found']}`",
        f"- Route-evidence dispatch-medium candidate rows found: `{counts['route_evidence_dispatch_medium_candidate_rows_found']}`",
        f"- Route-evidence license-context candidate rows found: `{counts['route_evidence_license_context_candidate_rows_found']}`",
        f"- Route-evidence owner/addressee candidate rows found: `{counts['route_evidence_owner_addressee_candidate_rows_found']}`",
        f"- Route-evidence local-standard route candidate rows found: `{counts['route_evidence_local_standard_route_candidate_rows_found']}`",
        f"- Route-evidence capture evidence-intake rows filled: `{counts['route_evidence_capture_evidence_intake_rows_filled']}`",
        f"- Route-evidence capture evidence artifacts linked to intake rows: `{counts['route_evidence_capture_evidence_artifacts_linked_to_intake_rows']}`",
        f"- Route-evidence capture route-label classes applied: `{counts['route_evidence_capture_route_label_classes_applied']}`",
        f"- Route-evidence capture blockers resolved: `{counts['route_evidence_capture_blockers_resolved']}`",
        f"- Route-evidence capture route assignments created: `{counts['route_evidence_capture_route_assignments_created']}`",
        f"- Route-evidence capture package order: `{counts['route_evidence_capture_package_order']}`",
        f"- Route-evidence capture queue candidate count: `{counts['route_evidence_capture_queue_candidate_count']}`",
        f"- Route-evidence capture coordination note present: `{str(counts['route_evidence_capture_coordination_note_present']).lower()}`",
        f"- Owner/local-standard route search rows: `{counts['owner_local_standard_route_search_rows']}`",
        f"- Owner/local-standard fetched route sources: `{counts['owner_local_standard_fetched_route_sources']}`",
        f"- Owner/local-standard candidate pointers: `{counts['owner_local_standard_candidate_pointers']}`",
        f"- Owner/local-standard project issue-template route candidates found: `{counts['owner_local_standard_project_issue_template_route_candidates_found']}`",
        f"- Owner/local-standard project contribution route candidates found: `{counts['owner_local_standard_project_contribution_route_candidates_found']}`",
        f"- Owner/local-standard addressee/owner route candidates found: `{counts['owner_local_standard_addressee_owner_route_candidates_found']}`",
        f"- Owner/local-standard non-personal source-owner roles validated: `{counts['owner_local_standard_non_personal_source_owner_roles_validated']}`",
        f"- Owner/local-standard route candidate rows found: `{counts['owner_local_standard_route_candidate_rows_found']}`",
        f"- Owner/local-standard evidence-intake rows filled: `{counts['owner_local_standard_evidence_intake_rows_filled']}`",
        f"- Owner/local-standard evidence artifacts linked to intake rows: `{counts['owner_local_standard_evidence_artifacts_linked_to_intake_rows']}`",
        f"- Owner/local-standard route-label classes applied: `{counts['owner_local_standard_route_label_classes_applied']}`",
        f"- Owner/local-standard blockers resolved: `{counts['owner_local_standard_blockers_resolved']}`",
        f"- Owner/local-standard route assignments created: `{counts['owner_local_standard_route_assignments_created']}`",
        f"- Owner/local-standard package order: `{counts['owner_local_standard_package_order']}`",
        f"- Owner/local-standard queue candidate count: `{counts['owner_local_standard_queue_candidate_count']}`",
        f"- Owner/local-standard coordination note present: `{str(counts['owner_local_standard_coordination_note_present']).lower()}`",
        f"- Local-standard scope selector rows: `{counts['local_standard_scope_selector_rows']}`",
        f"- Local-standard cataloged scope shelves: `{counts['local_standard_cataloged_scope_shelves']}`",
        f"- Local-standard candidate source-audit rows: `{counts['local_standard_candidate_source_audit_rows']}`",
        f"- Local-standard gap-only rows: `{counts['local_standard_gap_only_rows']}`",
        f"- Local-standard routes confirmed: `{counts['local_standard_routes_confirmed']}`",
        f"- Local authorities confirmed: `{counts['local_authorities_confirmed']}`",
        f"- Local-standard evidence-intake rows filled: `{counts['local_standard_evidence_intake_rows_filled']}`",
        f"- Local-standard blockers resolved: `{counts['local_standard_blockers_resolved']}`",
        f"- Local-standard route-label classes applied: `{counts['local_standard_route_label_classes_applied']}`",
        f"- Local-standard route assignments created: `{counts['local_standard_route_assignments_created']}`",
        f"- Local-standard package order: `{counts['local_standard_package_order']}`",
        f"- Local-standard queue candidate count: `{counts['local_standard_queue_candidate_count']}`",
        f"- Local-standard coordination note present: `{str(counts['local_standard_coordination_note_present']).lower()}`",
        f"- Local-standard source-audit rows: `{counts['local_standard_source_audit_rows']}`",
        f"- Local-standard source-audit inventory rows: `{counts['local_standard_source_audit_inventory_rows']}`",
        f"- Local-standard source-audit cache-file checks: `{counts['local_standard_source_audit_cache_file_checks']}`",
        f"- Local-standard source-audit expected hash mismatches: `{counts['local_standard_source_audit_expected_hash_mismatches']}`",
        f"- Local-standard source-audit official-primary cache gaps carried forward: `{counts['local_standard_source_audit_official_primary_cache_gaps_carried_forward']}`",
        f"- Local-standard source-audit proxy/supplementary cache rows carried forward: `{counts['local_standard_source_audit_proxy_supplementary_cache_rows_carried_forward']}`",
        f"- Local-standard source-audit UC12 crosswalk boundary rows: `{counts['local_standard_source_audit_uc12_crosswalk_boundary_rows']}`",
        f"- Local-standard source-audit rows sufficient for evidence intake: `{counts['local_standard_source_audit_rows_sufficient_for_evidence_intake']}`",
        f"- Local-standard source-audit evidence-intake rows filled: `{counts['local_standard_source_audit_evidence_intake_rows_filled']}`",
        f"- Local-standard source-audit blockers resolved: `{counts['local_standard_source_audit_blockers_resolved']}`",
        f"- Local-standard source-audit route-label classes applied: `{counts['local_standard_source_audit_route_label_classes_applied']}`",
        f"- Local-standard source-audit route assignments created: `{counts['local_standard_source_audit_route_assignments_created']}`",
        f"- Local-standard source-audit package order: `{counts['local_standard_source_audit_package_order']}`",
        f"- Local-standard source-audit queue candidate count: `{counts['local_standard_source_audit_queue_candidate_count']}`",
        f"- Local-standard source-audit coordination note present: `{str(counts['local_standard_source_audit_coordination_note_present']).lower()}`",
        f"- Local-standard official-cache retry selected source-audit rows: `{counts['local_standard_official_cache_retry_selected_source_audit_rows']}`",
        f"- Local-standard official-cache retry download attempts: `{counts['local_standard_official_cache_retry_download_attempts']}`",
        f"- Local-standard official-cache retry successful downloads: `{counts['local_standard_official_cache_retry_successful_downloads']}`",
        f"- Local-standard official-cache retry failed downloads: `{counts['local_standard_official_cache_retry_failed_downloads']}`",
        f"- Local-standard official-cache retry official hashes added: `{counts['local_standard_official_cache_retry_official_hashes_added']}`",
        f"- Local-standard official-cache retry local official cache files added: `{counts['local_standard_official_cache_retry_local_official_cache_files_added']}`",
        f"- Local-standard official-cache retry exact official source hashes verified: `{counts['local_standard_official_cache_retry_exact_official_source_hashes_verified']}`",
        f"- Local-standard official-cache retry page-count checks against official files: `{counts['local_standard_official_cache_retry_page_count_checks_against_official_files']}`",
        f"- Local-standard official-cache retry term/page metadata from official files: `{counts['local_standard_official_cache_retry_term_page_metadata_from_official_files']}`",
        f"- Local-standard official-cache retry evidence-intake rows filled: `{counts['local_standard_official_cache_retry_evidence_intake_rows_filled']}`",
        f"- Local-standard official-cache retry blockers resolved: `{counts['local_standard_official_cache_retry_blockers_resolved']}`",
        f"- Local-standard official-cache retry route-label classes applied: `{counts['local_standard_official_cache_retry_route_label_classes_applied']}`",
        f"- Local-standard official-cache retry route assignments created: `{counts['local_standard_official_cache_retry_route_assignments_created']}`",
        f"- Local-standard official-cache retry package JSON artifacts with matching SHA sidecars: `{counts['local_standard_official_cache_retry_package_json_artifacts_with_matching_sha_sidecars']}`",
        f"- Local-standard official-cache retry recursive JSON parse failures: `{counts['local_standard_official_cache_retry_recursive_json_parse_failures']}`",
        f"- Local-standard official-cache retry package order: `{counts['local_standard_official_cache_retry_package_order']}`",
        f"- Local-standard official-cache retry queue candidate count: `{counts['local_standard_official_cache_retry_queue_candidate_count']}`",
        f"- Local-standard official-cache retry coordination note present: `{str(counts['local_standard_official_cache_retry_coordination_note_present']).lower()}`",
        f"- Local-standard gap-route search rows: `{counts['local_standard_gap_route_search_rows']}`",
        f"- Local-standard gap-route candidate source-route rows: `{counts['local_standard_gap_route_candidate_source_route_rows']}`",
        f"- Local-standard gap-route attempted source routes: `{counts['local_standard_gap_route_attempted_source_routes']}`",
        f"- Local-standard gap-route successful PDF downloads: `{counts['local_standard_gap_route_successful_pdf_downloads']}`",
        f"- Local-standard gap-route failed PDF-route retries: `{counts['local_standard_gap_route_failed_pdf_route_retries']}`",
        f"- Local-standard gap-route derived text-cache files: `{counts['local_standard_gap_route_derived_text_cache_files']}`",
        f"- Local-standard gap-route rows with candidate route cues: `{counts['local_standard_gap_route_rows_with_candidate_route_cues']}`",
        f"- Local-standard gap-route rows still explicit gap-only: `{counts['local_standard_gap_route_rows_still_explicit_gap_only']}`",
        f"- Local-standard gap-route rows sufficient for evidence intake: `{counts['local_standard_gap_route_rows_sufficient_for_evidence_intake']}`",
        f"- Local-standard gap-route evidence-intake rows filled: `{counts['local_standard_gap_route_evidence_intake_rows_filled']}`",
        f"- Local-standard gap-route blockers resolved: `{counts['local_standard_gap_route_blockers_resolved']}`",
        f"- Local-standard gap-route route-label classes applied: `{counts['local_standard_gap_route_route_label_classes_applied']}`",
        f"- Local-standard gap-route route assignments created: `{counts['local_standard_gap_route_route_assignments_created']}`",
        f"- Local-standard gap-route source excerpts copied into artifact: `{counts['local_standard_gap_route_source_excerpts_copied_into_artifact']}`",
        f"- Local-standard gap-route package JSON artifacts with matching SHA sidecars: `{counts['local_standard_gap_route_package_json_artifacts_with_matching_sha_sidecars']}`",
        f"- Local-standard gap-route recursive JSON parse failures: `{counts['local_standard_gap_route_recursive_json_parse_failures']}`",
        f"- Local-standard gap-route cached PDF/text hashes match: `{str(counts['local_standard_gap_route_cached_pdf_text_hashes_match']).lower()}`",
        f"- Local-standard gap-route package order: `{counts['local_standard_gap_route_package_order']}`",
        f"- Local-standard gap-route queue candidate count: `{counts['local_standard_gap_route_queue_candidate_count']}`",
        f"- Local-standard gap-route coordination note present: `{str(counts['local_standard_gap_route_coordination_note_present']).lower()}`",
        f"- Local-standard gap-source audit rows: `{counts['local_standard_gap_source_audit_rows']}`",
        f"- Local-standard gap-source audit source-route rows: `{counts['local_standard_gap_source_audit_source_route_rows']}`",
        f"- Local-standard gap-source audit cached PDF route audits: `{counts['local_standard_gap_source_audit_cached_pdf_route_audits']}`",
        f"- Local-standard gap-source audit failed route retry rows retained: `{counts['local_standard_gap_source_audit_failed_route_retry_rows_retained']}`",
        f"- Local-standard gap-source audit text-cache route audits: `{counts['local_standard_gap_source_audit_text_cache_route_audits']}`",
        f"- Local-standard gap-source audit text page segments audited: `{counts['local_standard_gap_source_audit_text_page_segments_audited']}`",
        f"- Local-standard gap-source audit rows with cached term-route cues: `{counts['local_standard_gap_source_audit_rows_with_cached_term_route_cues']}`",
        f"- Local-standard gap-source audit rows still explicit gaps: `{counts['local_standard_gap_source_audit_rows_still_explicit_gaps']}`",
        f"- Local-standard gap-source audit rows sufficient for evidence intake: `{counts['local_standard_gap_source_audit_rows_sufficient_for_evidence_intake']}`",
        f"- Local-standard gap-source audit evidence-intake rows filled: `{counts['local_standard_gap_source_audit_evidence_intake_rows_filled']}`",
        f"- Local-standard gap-source audit blockers resolved: `{counts['local_standard_gap_source_audit_blockers_resolved']}`",
        f"- Local-standard gap-source audit route-label classes applied: `{counts['local_standard_gap_source_audit_route_label_classes_applied']}`",
        f"- Local-standard gap-source audit route assignments created: `{counts['local_standard_gap_source_audit_route_assignments_created']}`",
        f"- Local-standard gap-source audit source excerpts copied into artifact: `{counts['local_standard_gap_source_audit_source_excerpts_copied_into_artifact']}`",
        f"- Local-standard gap-source audit package JSON artifacts with matching SHA sidecars: `{counts['local_standard_gap_source_audit_package_json_artifacts_with_matching_sha_sidecars']}`",
        f"- Local-standard gap-source audit recursive JSON parse failures: `{counts['local_standard_gap_source_audit_recursive_json_parse_failures']}`",
        f"- Local-standard gap-source audit cached PDF/text hashes match: `{str(counts['local_standard_gap_source_audit_cached_pdf_text_hashes_match']).lower()}`",
        f"- Local-standard gap-source audit package order: `{counts['local_standard_gap_source_audit_package_order']}`",
        f"- Local-standard gap-source audit queue candidate count: `{counts['local_standard_gap_source_audit_queue_candidate_count']}`",
        f"- Local-standard gap-source audit coordination note present: `{str(counts['local_standard_gap_source_audit_coordination_note_present']).lower()}`",
        f"- Local-standard failed-route retry rows: `{counts['local_standard_failed_route_retry_rows']}`",
        f"- Local-standard failed-route retry affected gap rows: `{counts['local_standard_failed_route_retry_affected_gap_rows']}`",
        f"- Local-standard failed-route retry externally visible routes: `{counts['local_standard_failed_route_retry_externally_visible_routes']}`",
        f"- Local-standard failed-route retry local download attempts: `{counts['local_standard_failed_route_retry_local_download_attempts']}`",
        f"- Local-standard failed-route retry successful PDF downloads: `{counts['local_standard_failed_route_retry_successful_pdf_downloads']}`",
        f"- Local-standard failed-route retry failed PDF download attempts: `{counts['local_standard_failed_route_retry_failed_pdf_download_attempts']}`",
        f"- Local-standard failed-route retry routes still without local PDF cache: `{counts['local_standard_failed_route_retry_routes_still_without_local_pdf_cache']}`",
        f"- Local-standard failed-route retry external visibility as local hash evidence: `{str(counts['local_standard_failed_route_retry_external_visibility_as_local_hash_evidence']).lower()}`",
        f"- Local-standard failed-route retry evidence-intake rows filled: `{counts['local_standard_failed_route_retry_evidence_intake_rows_filled']}`",
        f"- Local-standard failed-route retry blockers resolved: `{counts['local_standard_failed_route_retry_blockers_resolved']}`",
        f"- Local-standard failed-route retry route-label classes applied: `{counts['local_standard_failed_route_retry_route_label_classes_applied']}`",
        f"- Local-standard failed-route retry route assignments created: `{counts['local_standard_failed_route_retry_route_assignments_created']}`",
        f"- Local-standard failed-route retry dispatches: `{counts['local_standard_failed_route_retry_dispatches']}`",
        f"- Local-standard failed-route retry responses ingested: `{counts['local_standard_failed_route_retry_responses_ingested']}`",
        f"- Local-standard failed-route retry source excerpts copied into artifact: `{counts['local_standard_failed_route_retry_source_excerpts_copied_into_artifact']}`",
        f"- Local-standard failed-route retry package order: `{counts['local_standard_failed_route_retry_package_order']}`",
        f"- Local-standard failed-route retry queue candidate count: `{counts['local_standard_failed_route_retry_queue_candidate_count']}`",
        f"- Local-standard failed-route retry coordination note present: `{str(counts['local_standard_failed_route_retry_coordination_note_present']).lower()}`",
        f"- Local-standard alternate-route rows: `{counts['local_standard_alternate_route_rows']}`",
        f"- Local-standard alternate-route download attempt rows: `{counts['local_standard_alternate_route_download_attempt_rows']}`",
        f"- Local-standard alternate-route official external alternates found but not locally cached: `{counts['local_standard_alternate_route_official_external_alternates_found_but_not_locally_cached']}`",
        f"- Local-standard alternate-route valid institutional PDF cache files: `{counts['local_standard_alternate_route_valid_institutional_pdf_cache_files']}`",
        f"- Local-standard alternate-route derived text-cache files: `{counts['local_standard_alternate_route_derived_text_cache_files']}`",
        f"- Local-standard alternate-route partial invalid PDF files retained: `{counts['local_standard_alternate_route_partial_invalid_pdf_files_retained']}`",
        f"- Local-standard alternate-route partial invalid PDF quarantined unusable: `{str(counts['local_standard_alternate_route_partial_invalid_pdf_quarantined_unusable']).lower()}`",
        f"- Local-standard alternate-route text page segments audited: `{counts['local_standard_alternate_route_text_page_segments_audited']}`",
        f"- Local-standard alternate-route affected gap rows: `{counts['local_standard_alternate_route_affected_gap_rows']}`",
        f"- Local-standard alternate-route affected gap rows with valid cached alternate cues: `{counts['local_standard_alternate_route_affected_gap_rows_with_valid_cached_alternate_cues']}`",
        f"- Local-standard alternate-route Telkom HTTP fallback metadata-only route evidence: `{str(counts['local_standard_alternate_route_telkom_http_fallback_metadata_only_route_evidence']).lower()}`",
        f"- Local-standard alternate-route Telkom HTTP fallback as local standard: `{str(counts['local_standard_alternate_route_telkom_http_fallback_as_local_standard']).lower()}`",
        f"- Local-standard alternate-route external official route visibility as local hash evidence: `{str(counts['local_standard_alternate_route_external_official_route_visibility_as_local_hash_evidence']).lower()}`",
        f"- Local-standard alternate-route evidence-intake rows filled: `{counts['local_standard_alternate_route_evidence_intake_rows_filled']}`",
        f"- Local-standard alternate-route assignments created: `{counts['local_standard_alternate_route_assignments_created']}`",
        f"- Local-standard alternate-route dispatches: `{counts['local_standard_alternate_route_dispatches']}`",
        f"- Local-standard alternate-route responses ingested: `{counts['local_standard_alternate_route_responses_ingested']}`",
        f"- Local-standard alternate-route source excerpts copied into artifact: `{counts['local_standard_alternate_route_source_excerpts_copied_into_artifact']}`",
        f"- Local-standard alternate-route translations created: `{counts['local_standard_alternate_route_translations_created']}`",
        f"- Local-standard alternate-route package order: `{counts['local_standard_alternate_route_package_order']}`",
        f"- Local-standard alternate-route queue candidate count: `{counts['local_standard_alternate_route_queue_candidate_count']}`",
        f"- Local-standard alternate-route coordination note present: `{str(counts['local_standard_alternate_route_coordination_note_present']).lower()}`",
        f"- Root output JSON files: `{counts['root_output_json_files']}`",
        f"- Recursive output JSON files checked: `{counts['recursive_output_json_files_checked']}`",
        "",
        "## Zero Gates",
        "",
        "All delegated gates remain zero for returns, sufficient evidence artifacts, source-audit rows sufficient for evidence intake, gap-route rows sufficient for evidence intake, gap-source audit rows sufficient for evidence intake, failed-route retry rows sufficient for evidence intake, alternate-route rows sufficient for evidence intake, external visibility promoted to local hash evidence, Telkom fallback promoted to local standard, partial invalid PDF evidence use, official hashes, local official cache files, exact official source hash verification, official page-count checks, official term/page metadata, evidence links, evidence rows, route-label application, route assignments, local-standard route confirmations, local authority confirmations, surfaces, lexemes, morphemes, grammar, translation, source excerpts, dispatches, pilot readiness, publication readiness, constructed-surface readiness, canonical row resolution, term confirmation, reviewer packet population, render readiness, and review readiness.",
        "",
        "## Boundaries",
        "",
        "- No source note body or excerpt is copied into this branch payload.",
        "- No source-language terms are copied.",
        "- No credentials or tokens are copied.",
        "- No canonical rows are resolved.",
        "- No terms are confirmed.",
        "- No reviewer packets are populated.",
        "- No translations are created.",
        "- No render, review, publication, pilot, or constructed-surface readiness is claimed.",
        "",
        ]
    )
    RELATION_OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def update_status_index(source_doc: dict, relation_doc: dict, manifest: dict) -> None:
    text = STATUS_INDEX.read_text(encoding="utf-8")
    text = re.sub(
        r"- JSON artifacts indexed: \d+ plus this status manifest",
        f"- JSON artifacts indexed: {len(manifest['artifacts']['json'])} plus this status manifest",
        text,
    )
    text = re.sub(
        r"- Markdown artifacts indexed: \d+ plus this status index",
        f"- Markdown artifacts indexed: {len(manifest['artifacts']['markdown'])} plus this status index",
        text,
    )
    text = re.sub(
        r"- Reproducible scripts indexed: \d+",
        f"- Reproducible scripts indexed: {len(manifest['artifacts']['scripts'])}",
        text,
    )

    source_line = (
        "- Source-aware/OLP pointer intake: "
        f"{source_doc['totals']['source_pointers']} source pointers / "
        f"{source_doc['totals']['source_pointers_with_hash_verified']} hash-verified / "
        "0 excerpts / 0 translations"
    )
    relation_line = (
        "- Semi-constructed relation/function reviewer sheet intake: "
        f"{relation_doc['totals']['reviewer_sheet_blank_semantic_slot_rows']} reviewer rows / "
        f"{relation_doc['totals']['return_ledger_blank_rows']} return-ledger rows / "
        f"{relation_doc['totals']['selector_map_rows']} selector rows / "
        f"{relation_doc['totals']['source_request_rows']} request rows / "
        f"{relation_doc['totals']['dispatch_checklist_rows']} checklist rows / "
        f"{relation_doc['totals']['blocker_queue_open_rows']} blocker rows / "
        f"{relation_doc['totals']['evidence_intake_ledger_blank_rows']} evidence-intake rows / "
        f"{relation_doc['totals']['evidence_criteria_route_label_taxonomy_rows']} taxonomy rows / "
        f"{relation_doc['totals']['evidence_criteria_rows']} criteria rows / "
        f"{relation_doc['totals']['route_evidence_discovery_rows']} route-evidence rows / "
        f"{relation_doc['totals']['route_evidence_candidate_capture_rows']} route-candidate rows / "
        f"{relation_doc['totals']['owner_local_standard_route_search_rows']} owner-route rows / "
        f"{relation_doc['totals']['local_standard_scope_selector_rows']} local-standard selector rows / "
        f"{relation_doc['totals']['local_standard_source_audit_rows']} source-audit rows / "
        f"{relation_doc['totals']['local_standard_official_cache_retry_download_attempts']} official-cache retry rows / "
        f"{relation_doc['totals']['local_standard_gap_route_search_rows']} gap-route rows / "
        f"{relation_doc['totals']['local_standard_gap_source_audit_rows']} gap-source audit rows / "
        f"{relation_doc['totals']['local_standard_failed_route_retry_rows']} failed-route retry rows / "
        f"{relation_doc['totals']['local_standard_alternate_route_rows']} alternate-route rows / "
        f"{relation_doc['totals']['max_queue_candidate_count']} queue candidates / 0 readiness claims"
    )
    for line, pattern in [
        (source_line, r"^- Source-aware/OLP pointer intake: .*"),
        (relation_line, r"^- Semi-constructed relation/function reviewer sheet intake: .*"),
    ]:
        if re.search(pattern, text, flags=re.MULTILINE):
            text = re.sub(pattern, line, text, flags=re.MULTILINE)
        else:
            rows = text.splitlines()
            inserted = False
            for offset, row in enumerate(rows):
                if row.startswith("- Cross-session packet evidence threshold pattern intake:"):
                    rows.insert(offset + 1, relation_line)
                    rows.insert(offset + 1, source_line)
                    text = "\n".join(rows) + "\n"
                    inserted = True
                    break
            if not inserted:
                text = text.rstrip() + "\n" + source_line + "\n" + relation_line + "\n"
            break

    if "source-aware-olp-pointer-intake" not in text:
        text = text.replace(
            "cross-session-packet-evidence-threshold-pattern-intake/render-script-preflight",
            (
                "cross-session-packet-evidence-threshold-pattern-intake/source-aware-olp-pointer-intake/"
                "semi-constructed-relation-function-reviewer-sheet-intake/render-script-preflight"
            ),
        )
    if "Generated UTC: " in text:
        old = text.split("Generated UTC: ", 1)[1].splitlines()[0]
        text = text.replace(old, manifest["generated_utc"], 1)
    STATUS_INDEX.write_text(text, encoding="utf-8")


def update_manifest(source_doc: dict, relation_doc: dict) -> None:
    manifest = load_json(STATUS_MANIFEST)
    manifest["generated_utc"] = now_utc()
    upsert_artifact(manifest, "json", SOURCE_AWARE_OUT_JSON, source_doc["status"])
    upsert_artifact(manifest, "markdown", SOURCE_AWARE_OUT_MD)
    upsert_artifact(manifest, "json", RELATION_OUT_JSON, relation_doc["status"])
    upsert_artifact(manifest, "markdown", RELATION_OUT_MD)
    upsert_artifact(manifest, "scripts", SELF_PATH)
    refresh_existing_artifact_hashes(manifest)

    manifest["source_aware_packet_start_olp_pointer_intake"] = {
        "status": source_doc["status"],
        "artifact_markdown": SOURCE_AWARE_OUT_MD.name,
        "artifact_json": SOURCE_AWARE_OUT_JSON.name,
        "source_thread_id": source_doc["source_thread_id"],
        "source_pointers": source_doc["totals"]["source_pointers"],
        "source_pointers_with_hash_verified": source_doc["totals"]["source_pointers_with_hash_verified"],
        "canonical_rows_resolved": 0,
        "reviewer_packet_rows_populated": 0,
        "terms_confirmed": 0,
        "excerpts_selected": 0,
        "source_prose_copied": 0,
        "translations_created": 0,
        "source_note_body_copied": False,
        "source_note_excerpt_copied": False,
        "source_text_copied": False,
        "source_language_terms_copied": False,
        "credentials_or_tokens_copied": False,
        "no_network_actions_performed": True,
        "constructed_surface_readiness_claim": False,
        "publication_readiness_claim": False,
        "pilot_readiness_claim": False,
    }
    manifest["semi_constructed_relation_function_reviewer_sheet_intake"] = {
        "status": relation_doc["status"],
        "artifact_markdown": RELATION_OUT_MD.name,
        "artifact_json": RELATION_OUT_JSON.name,
        "source_thread_id": relation_doc["source_thread_id"],
        "source_pointers": relation_doc["totals"]["source_pointers"],
        "tool_repair_pointers": relation_doc["totals"]["tool_repair_pointers"],
        "source_pointers_with_hash_verified": relation_doc["totals"]["source_pointers_with_hash_verified"],
        "tool_repair_directory_exists": relation_doc["tool_repair_pointer"]["directory_exists"],
        "tool_repair_item_count": relation_doc["tool_repair_pointer"]["item_count"],
        "reviewer_sheet_blank_semantic_slot_rows": relation_doc["totals"]["reviewer_sheet_blank_semantic_slot_rows"],
        "return_ledger_blank_rows": relation_doc["totals"]["return_ledger_blank_rows"],
        "selector_map_rows": relation_doc["totals"]["selector_map_rows"],
        "selector_map_term_family_shelves": relation_doc["totals"]["selector_map_term_family_shelves"],
        "selector_map_coordinate_rows": relation_doc["totals"]["selector_map_coordinate_rows"],
        "selector_map_source_paths_with_hits": relation_doc["totals"]["selector_map_source_paths_with_hits"],
        "source_request_rows": relation_doc["totals"]["source_request_rows"],
        "source_request_questions": relation_doc["totals"]["source_request_questions"],
        "source_request_source_path_slots": relation_doc["totals"]["source_request_source_path_slots"],
        "source_request_coordinate_id_slots": relation_doc["totals"]["source_request_coordinate_id_slots"],
        "dispatch_checklist_rows": relation_doc["totals"]["dispatch_checklist_rows"],
        "dispatch_checklist_checks_total": relation_doc["totals"]["dispatch_checklist_checks_total"],
        "dispatch_checklist_metadata_checks_passed": relation_doc["totals"]["dispatch_checklist_metadata_checks_passed"],
        "dispatch_checklist_prerequisites_failed": relation_doc["totals"]["dispatch_checklist_prerequisites_failed"],
        "dispatch_checklist_ready_for_dispatch_rows": relation_doc["totals"]["dispatch_checklist_ready_for_dispatch_rows"],
        "blocker_queue_open_rows": relation_doc["totals"]["blocker_queue_open_rows"],
        "blocker_queue_classes": relation_doc["totals"]["blocker_queue_classes"],
        "blocker_queue_rows_per_class": relation_doc["totals"]["blocker_queue_rows_per_class"],
        "blocker_queue_resolved_rows": relation_doc["totals"]["blocker_queue_resolved_rows"],
        "evidence_intake_ledger_blank_rows": relation_doc["totals"]["evidence_intake_ledger_blank_rows"],
        "evidence_intake_ledger_blocker_classes": relation_doc["totals"]["evidence_intake_ledger_blocker_classes"],
        "evidence_intake_ledger_rows_per_class": relation_doc["totals"]["evidence_intake_ledger_rows_per_class"],
        "evidence_intake_ledger_evidence_artifacts_linked": relation_doc["totals"]["evidence_intake_ledger_evidence_artifacts_linked"],
        "evidence_intake_ledger_evidence_rows_filled": relation_doc["totals"]["evidence_intake_ledger_evidence_rows_filled"],
        "evidence_intake_ledger_route_assignments_created": relation_doc["totals"]["evidence_intake_ledger_route_assignments_created"],
        "evidence_criteria_route_label_taxonomy_rows": relation_doc["totals"]["evidence_criteria_route_label_taxonomy_rows"],
        "evidence_criteria_rows": relation_doc["totals"]["evidence_criteria_rows"],
        "evidence_criteria_blocker_classes": relation_doc["totals"]["evidence_criteria_blocker_classes"],
        "evidence_criteria_rows_per_blocker_class": relation_doc["totals"]["evidence_criteria_rows_per_blocker_class"],
        "evidence_criteria_evidence_artifacts_linked": relation_doc["totals"]["evidence_criteria_evidence_artifacts_linked"],
        "evidence_criteria_evidence_rows_filled": relation_doc["totals"]["evidence_criteria_evidence_rows_filled"],
        "evidence_criteria_route_label_classes_applied": relation_doc["totals"]["evidence_criteria_route_label_classes_applied"],
        "evidence_criteria_blockers_resolved": relation_doc["totals"]["evidence_criteria_blockers_resolved"],
        "evidence_criteria_route_assignments_created": relation_doc["totals"]["evidence_criteria_route_assignments_created"],
        "route_evidence_discovery_rows": relation_doc["totals"]["route_evidence_discovery_rows"],
        "route_evidence_inherited_criteria_rows": relation_doc["totals"]["route_evidence_inherited_criteria_rows"],
        "route_evidence_taxonomy_rows": relation_doc["totals"]["route_evidence_taxonomy_rows"],
        "route_evidence_local_candidate_reference_artifacts_considered": relation_doc["totals"]["route_evidence_local_candidate_reference_artifacts_considered"],
        "route_evidence_sufficient_evidence_artifacts_found": relation_doc["totals"]["route_evidence_sufficient_evidence_artifacts_found"],
        "route_evidence_artifacts_linked": relation_doc["totals"]["route_evidence_artifacts_linked"],
        "route_evidence_rows_filled": relation_doc["totals"]["route_evidence_rows_filled"],
        "route_evidence_route_label_classes_applied": relation_doc["totals"]["route_evidence_route_label_classes_applied"],
        "route_evidence_blockers_resolved": relation_doc["totals"]["route_evidence_blockers_resolved"],
        "route_evidence_route_assignments_created": relation_doc["totals"]["route_evidence_route_assignments_created"],
        "route_evidence_candidate_capture_rows": relation_doc["totals"]["route_evidence_candidate_capture_rows"],
        "route_evidence_official_route_license_pointers_cached": relation_doc["totals"]["route_evidence_official_route_license_pointers_cached"],
        "route_evidence_source_route_candidate_rows_found": relation_doc["totals"]["route_evidence_source_route_candidate_rows_found"],
        "route_evidence_dispatch_medium_candidate_rows_found": relation_doc["totals"]["route_evidence_dispatch_medium_candidate_rows_found"],
        "route_evidence_license_context_candidate_rows_found": relation_doc["totals"]["route_evidence_license_context_candidate_rows_found"],
        "route_evidence_owner_addressee_candidate_rows_found": relation_doc["totals"]["route_evidence_owner_addressee_candidate_rows_found"],
        "route_evidence_local_standard_route_candidate_rows_found": relation_doc["totals"]["route_evidence_local_standard_route_candidate_rows_found"],
        "route_evidence_capture_evidence_intake_rows_filled": relation_doc["totals"]["route_evidence_capture_evidence_intake_rows_filled"],
        "route_evidence_capture_evidence_artifacts_linked_to_intake_rows": relation_doc["totals"]["route_evidence_capture_evidence_artifacts_linked_to_intake_rows"],
        "route_evidence_capture_route_label_classes_applied": relation_doc["totals"]["route_evidence_capture_route_label_classes_applied"],
        "route_evidence_capture_blockers_resolved": relation_doc["totals"]["route_evidence_capture_blockers_resolved"],
        "route_evidence_capture_route_assignments_created": relation_doc["totals"]["route_evidence_capture_route_assignments_created"],
        "owner_local_standard_route_search_rows": relation_doc["totals"]["owner_local_standard_route_search_rows"],
        "owner_local_standard_fetched_route_sources": relation_doc["totals"]["owner_local_standard_fetched_route_sources"],
        "owner_local_standard_candidate_pointers": relation_doc["totals"]["owner_local_standard_candidate_pointers"],
        "owner_local_standard_project_issue_template_route_candidates_found": relation_doc["totals"]["owner_local_standard_project_issue_template_route_candidates_found"],
        "owner_local_standard_project_contribution_route_candidates_found": relation_doc["totals"]["owner_local_standard_project_contribution_route_candidates_found"],
        "owner_local_standard_addressee_owner_route_candidates_found": relation_doc["totals"]["owner_local_standard_addressee_owner_route_candidates_found"],
        "owner_local_standard_non_personal_source_owner_roles_validated": relation_doc["totals"]["owner_local_standard_non_personal_source_owner_roles_validated"],
        "owner_local_standard_route_candidate_rows_found": relation_doc["totals"]["owner_local_standard_route_candidate_rows_found"],
        "owner_local_standard_evidence_intake_rows_filled": relation_doc["totals"]["owner_local_standard_evidence_intake_rows_filled"],
        "owner_local_standard_evidence_artifacts_linked_to_intake_rows": relation_doc["totals"]["owner_local_standard_evidence_artifacts_linked_to_intake_rows"],
        "owner_local_standard_route_label_classes_applied": relation_doc["totals"]["owner_local_standard_route_label_classes_applied"],
        "owner_local_standard_blockers_resolved": relation_doc["totals"]["owner_local_standard_blockers_resolved"],
        "owner_local_standard_route_assignments_created": relation_doc["totals"]["owner_local_standard_route_assignments_created"],
        "local_standard_scope_selector_rows": relation_doc["totals"]["local_standard_scope_selector_rows"],
        "local_standard_cataloged_scope_shelves": relation_doc["totals"]["local_standard_cataloged_scope_shelves"],
        "local_standard_candidate_source_audit_rows": relation_doc["totals"]["local_standard_candidate_source_audit_rows"],
        "local_standard_gap_only_rows": relation_doc["totals"]["local_standard_gap_only_rows"],
        "local_standard_routes_confirmed": relation_doc["totals"]["local_standard_routes_confirmed"],
        "local_authorities_confirmed": relation_doc["totals"]["local_authorities_confirmed"],
        "local_standard_evidence_intake_rows_filled": relation_doc["totals"]["local_standard_evidence_intake_rows_filled"],
        "local_standard_blockers_resolved": relation_doc["totals"]["local_standard_blockers_resolved"],
        "local_standard_route_label_classes_applied": relation_doc["totals"]["local_standard_route_label_classes_applied"],
        "local_standard_route_assignments_created": relation_doc["totals"]["local_standard_route_assignments_created"],
        "local_standard_source_audit_rows": relation_doc["totals"]["local_standard_source_audit_rows"],
        "local_standard_source_audit_inventory_rows": relation_doc["totals"]["local_standard_source_audit_inventory_rows"],
        "local_standard_source_audit_cache_file_checks": relation_doc["totals"]["local_standard_source_audit_cache_file_checks"],
        "local_standard_source_audit_expected_hash_mismatches": relation_doc["totals"]["local_standard_source_audit_expected_hash_mismatches"],
        "local_standard_source_audit_official_primary_cache_gaps_carried_forward": relation_doc["totals"]["local_standard_source_audit_official_primary_cache_gaps_carried_forward"],
        "local_standard_source_audit_proxy_supplementary_cache_rows_carried_forward": relation_doc["totals"]["local_standard_source_audit_proxy_supplementary_cache_rows_carried_forward"],
        "local_standard_source_audit_uc12_crosswalk_boundary_rows": relation_doc["totals"]["local_standard_source_audit_uc12_crosswalk_boundary_rows"],
        "local_standard_source_audit_rows_sufficient_for_evidence_intake": relation_doc["totals"]["local_standard_source_audit_rows_sufficient_for_evidence_intake"],
        "local_standard_source_audit_evidence_intake_rows_filled": relation_doc["totals"]["local_standard_source_audit_evidence_intake_rows_filled"],
        "local_standard_source_audit_blockers_resolved": relation_doc["totals"]["local_standard_source_audit_blockers_resolved"],
        "local_standard_source_audit_route_label_classes_applied": relation_doc["totals"]["local_standard_source_audit_route_label_classes_applied"],
        "local_standard_source_audit_route_assignments_created": relation_doc["totals"]["local_standard_source_audit_route_assignments_created"],
        "local_standard_official_cache_retry_selected_source_audit_rows": relation_doc["totals"]["local_standard_official_cache_retry_selected_source_audit_rows"],
        "local_standard_official_cache_retry_download_attempts": relation_doc["totals"]["local_standard_official_cache_retry_download_attempts"],
        "local_standard_official_cache_retry_successful_downloads": relation_doc["totals"]["local_standard_official_cache_retry_successful_downloads"],
        "local_standard_official_cache_retry_failed_downloads": relation_doc["totals"]["local_standard_official_cache_retry_failed_downloads"],
        "local_standard_official_cache_retry_official_hashes_added": relation_doc["totals"]["local_standard_official_cache_retry_official_hashes_added"],
        "local_standard_official_cache_retry_local_official_cache_files_added": relation_doc["totals"]["local_standard_official_cache_retry_local_official_cache_files_added"],
        "local_standard_official_cache_retry_exact_official_source_hashes_verified": relation_doc["totals"]["local_standard_official_cache_retry_exact_official_source_hashes_verified"],
        "local_standard_official_cache_retry_page_count_checks_against_official_files": relation_doc["totals"]["local_standard_official_cache_retry_page_count_checks_against_official_files"],
        "local_standard_official_cache_retry_term_page_metadata_from_official_files": relation_doc["totals"]["local_standard_official_cache_retry_term_page_metadata_from_official_files"],
        "local_standard_official_cache_retry_evidence_intake_rows_filled": relation_doc["totals"]["local_standard_official_cache_retry_evidence_intake_rows_filled"],
        "local_standard_official_cache_retry_blockers_resolved": relation_doc["totals"]["local_standard_official_cache_retry_blockers_resolved"],
        "local_standard_official_cache_retry_route_label_classes_applied": relation_doc["totals"]["local_standard_official_cache_retry_route_label_classes_applied"],
        "local_standard_official_cache_retry_route_assignments_created": relation_doc["totals"]["local_standard_official_cache_retry_route_assignments_created"],
        "local_standard_official_cache_retry_package_json_artifacts_with_matching_sha_sidecars": relation_doc["totals"]["local_standard_official_cache_retry_package_json_artifacts_with_matching_sha_sidecars"],
        "local_standard_official_cache_retry_recursive_json_parse_failures": relation_doc["totals"]["local_standard_official_cache_retry_recursive_json_parse_failures"],
        "local_standard_gap_route_search_rows": relation_doc["totals"]["local_standard_gap_route_search_rows"],
        "local_standard_gap_route_candidate_source_route_rows": relation_doc["totals"]["local_standard_gap_route_candidate_source_route_rows"],
        "local_standard_gap_route_attempted_source_routes": relation_doc["totals"]["local_standard_gap_route_attempted_source_routes"],
        "local_standard_gap_route_successful_pdf_downloads": relation_doc["totals"]["local_standard_gap_route_successful_pdf_downloads"],
        "local_standard_gap_route_failed_pdf_route_retries": relation_doc["totals"]["local_standard_gap_route_failed_pdf_route_retries"],
        "local_standard_gap_route_derived_text_cache_files": relation_doc["totals"]["local_standard_gap_route_derived_text_cache_files"],
        "local_standard_gap_route_rows_with_candidate_route_cues": relation_doc["totals"]["local_standard_gap_route_rows_with_candidate_route_cues"],
        "local_standard_gap_route_rows_still_explicit_gap_only": relation_doc["totals"]["local_standard_gap_route_rows_still_explicit_gap_only"],
        "local_standard_gap_route_rows_sufficient_for_evidence_intake": relation_doc["totals"]["local_standard_gap_route_rows_sufficient_for_evidence_intake"],
        "local_standard_gap_route_evidence_intake_rows_filled": relation_doc["totals"]["local_standard_gap_route_evidence_intake_rows_filled"],
        "local_standard_gap_route_blockers_resolved": relation_doc["totals"]["local_standard_gap_route_blockers_resolved"],
        "local_standard_gap_route_route_label_classes_applied": relation_doc["totals"]["local_standard_gap_route_route_label_classes_applied"],
        "local_standard_gap_route_route_assignments_created": relation_doc["totals"]["local_standard_gap_route_route_assignments_created"],
        "local_standard_gap_route_source_excerpts_copied_into_artifact": relation_doc["totals"]["local_standard_gap_route_source_excerpts_copied_into_artifact"],
        "local_standard_gap_route_package_json_artifacts_with_matching_sha_sidecars": relation_doc["totals"]["local_standard_gap_route_package_json_artifacts_with_matching_sha_sidecars"],
        "local_standard_gap_route_recursive_json_parse_failures": relation_doc["totals"]["local_standard_gap_route_recursive_json_parse_failures"],
        "local_standard_gap_route_cached_pdf_text_hashes_match": relation_doc["totals"]["local_standard_gap_route_cached_pdf_text_hashes_match"],
        "local_standard_gap_source_audit_rows": relation_doc["totals"]["local_standard_gap_source_audit_rows"],
        "local_standard_gap_source_audit_source_route_rows": relation_doc["totals"]["local_standard_gap_source_audit_source_route_rows"],
        "local_standard_gap_source_audit_cached_pdf_route_audits": relation_doc["totals"]["local_standard_gap_source_audit_cached_pdf_route_audits"],
        "local_standard_gap_source_audit_failed_route_retry_rows_retained": relation_doc["totals"]["local_standard_gap_source_audit_failed_route_retry_rows_retained"],
        "local_standard_gap_source_audit_text_cache_route_audits": relation_doc["totals"]["local_standard_gap_source_audit_text_cache_route_audits"],
        "local_standard_gap_source_audit_text_page_segments_audited": relation_doc["totals"]["local_standard_gap_source_audit_text_page_segments_audited"],
        "local_standard_gap_source_audit_rows_with_cached_term_route_cues": relation_doc["totals"]["local_standard_gap_source_audit_rows_with_cached_term_route_cues"],
        "local_standard_gap_source_audit_rows_still_explicit_gaps": relation_doc["totals"]["local_standard_gap_source_audit_rows_still_explicit_gaps"],
        "local_standard_gap_source_audit_rows_sufficient_for_evidence_intake": relation_doc["totals"]["local_standard_gap_source_audit_rows_sufficient_for_evidence_intake"],
        "local_standard_gap_source_audit_evidence_intake_rows_filled": relation_doc["totals"]["local_standard_gap_source_audit_evidence_intake_rows_filled"],
        "local_standard_gap_source_audit_blockers_resolved": relation_doc["totals"]["local_standard_gap_source_audit_blockers_resolved"],
        "local_standard_gap_source_audit_route_label_classes_applied": relation_doc["totals"]["local_standard_gap_source_audit_route_label_classes_applied"],
        "local_standard_gap_source_audit_route_assignments_created": relation_doc["totals"]["local_standard_gap_source_audit_route_assignments_created"],
        "local_standard_gap_source_audit_source_excerpts_copied_into_artifact": relation_doc["totals"]["local_standard_gap_source_audit_source_excerpts_copied_into_artifact"],
        "local_standard_gap_source_audit_package_json_artifacts_with_matching_sha_sidecars": relation_doc["totals"]["local_standard_gap_source_audit_package_json_artifacts_with_matching_sha_sidecars"],
        "local_standard_gap_source_audit_recursive_json_parse_failures": relation_doc["totals"]["local_standard_gap_source_audit_recursive_json_parse_failures"],
        "local_standard_gap_source_audit_cached_pdf_text_hashes_match": relation_doc["totals"]["local_standard_gap_source_audit_cached_pdf_text_hashes_match"],
        "local_standard_failed_route_retry_rows": relation_doc["totals"]["local_standard_failed_route_retry_rows"],
        "local_standard_failed_route_retry_affected_gap_rows": relation_doc["totals"]["local_standard_failed_route_retry_affected_gap_rows"],
        "local_standard_failed_route_retry_externally_visible_routes": relation_doc["totals"]["local_standard_failed_route_retry_externally_visible_routes"],
        "local_standard_failed_route_retry_local_download_attempts": relation_doc["totals"]["local_standard_failed_route_retry_local_download_attempts"],
        "local_standard_failed_route_retry_successful_pdf_downloads": relation_doc["totals"]["local_standard_failed_route_retry_successful_pdf_downloads"],
        "local_standard_failed_route_retry_failed_pdf_download_attempts": relation_doc["totals"]["local_standard_failed_route_retry_failed_pdf_download_attempts"],
        "local_standard_failed_route_retry_routes_still_without_local_pdf_cache": relation_doc["totals"]["local_standard_failed_route_retry_routes_still_without_local_pdf_cache"],
        "local_standard_failed_route_retry_external_visibility_as_local_hash_evidence": relation_doc["totals"]["local_standard_failed_route_retry_external_visibility_as_local_hash_evidence"],
        "local_standard_failed_route_retry_evidence_intake_rows_filled": relation_doc["totals"]["local_standard_failed_route_retry_evidence_intake_rows_filled"],
        "local_standard_failed_route_retry_blockers_resolved": relation_doc["totals"]["local_standard_failed_route_retry_blockers_resolved"],
        "local_standard_failed_route_retry_route_label_classes_applied": relation_doc["totals"]["local_standard_failed_route_retry_route_label_classes_applied"],
        "local_standard_failed_route_retry_route_assignments_created": relation_doc["totals"]["local_standard_failed_route_retry_route_assignments_created"],
        "local_standard_failed_route_retry_dispatches": relation_doc["totals"]["local_standard_failed_route_retry_dispatches"],
        "local_standard_failed_route_retry_responses_ingested": relation_doc["totals"]["local_standard_failed_route_retry_responses_ingested"],
        "local_standard_failed_route_retry_source_excerpts_copied_into_artifact": relation_doc["totals"]["local_standard_failed_route_retry_source_excerpts_copied_into_artifact"],
        "local_standard_alternate_route_rows": relation_doc["totals"]["local_standard_alternate_route_rows"],
        "local_standard_alternate_route_download_attempt_rows": relation_doc["totals"]["local_standard_alternate_route_download_attempt_rows"],
        "local_standard_alternate_route_official_external_alternates_found_but_not_locally_cached": relation_doc["totals"]["local_standard_alternate_route_official_external_alternates_found_but_not_locally_cached"],
        "local_standard_alternate_route_valid_institutional_pdf_cache_files": relation_doc["totals"]["local_standard_alternate_route_valid_institutional_pdf_cache_files"],
        "local_standard_alternate_route_derived_text_cache_files": relation_doc["totals"]["local_standard_alternate_route_derived_text_cache_files"],
        "local_standard_alternate_route_partial_invalid_pdf_files_retained": relation_doc["totals"]["local_standard_alternate_route_partial_invalid_pdf_files_retained"],
        "local_standard_alternate_route_partial_invalid_pdf_quarantined_unusable": relation_doc["totals"]["local_standard_alternate_route_partial_invalid_pdf_quarantined_unusable"],
        "local_standard_alternate_route_text_page_segments_audited": relation_doc["totals"]["local_standard_alternate_route_text_page_segments_audited"],
        "local_standard_alternate_route_affected_gap_rows": relation_doc["totals"]["local_standard_alternate_route_affected_gap_rows"],
        "local_standard_alternate_route_affected_gap_rows_with_valid_cached_alternate_cues": relation_doc["totals"]["local_standard_alternate_route_affected_gap_rows_with_valid_cached_alternate_cues"],
        "local_standard_alternate_route_telkom_http_fallback_metadata_only_route_evidence": relation_doc["totals"]["local_standard_alternate_route_telkom_http_fallback_metadata_only_route_evidence"],
        "local_standard_alternate_route_telkom_http_fallback_as_local_standard": relation_doc["totals"]["local_standard_alternate_route_telkom_http_fallback_as_local_standard"],
        "local_standard_alternate_route_external_official_route_visibility_as_local_hash_evidence": relation_doc["totals"]["local_standard_alternate_route_external_official_route_visibility_as_local_hash_evidence"],
        "local_standard_alternate_route_evidence_intake_rows_filled": relation_doc["totals"]["local_standard_alternate_route_evidence_intake_rows_filled"],
        "local_standard_alternate_route_assignments_created": relation_doc["totals"]["local_standard_alternate_route_assignments_created"],
        "local_standard_alternate_route_dispatches": relation_doc["totals"]["local_standard_alternate_route_dispatches"],
        "local_standard_alternate_route_responses_ingested": relation_doc["totals"]["local_standard_alternate_route_responses_ingested"],
        "local_standard_alternate_route_source_excerpts_copied_into_artifact": relation_doc["totals"]["local_standard_alternate_route_source_excerpts_copied_into_artifact"],
        "local_standard_alternate_route_translations_created": relation_doc["totals"]["local_standard_alternate_route_translations_created"],
        "questions": relation_doc["totals"]["questions"],
        "max_package_order": relation_doc["totals"]["max_package_order"],
        "max_queue_candidate_count": relation_doc["totals"]["max_queue_candidate_count"],
        "root_output_json_files": relation_doc["totals"]["root_output_json_files"],
        "recursive_output_json_files_checked": relation_doc["totals"]["recursive_output_json_files_checked"],
        "canonical_rows_resolved": 0,
        "reviewer_packet_rows_populated": 0,
        "terms_confirmed": 0,
        "translations_created": 0,
        "source_note_body_copied": False,
        "source_note_excerpt_copied": False,
        "source_text_copied": False,
        "source_language_terms_copied": False,
        "credentials_or_tokens_copied": False,
        "no_network_actions_performed": True,
        "render_readiness_claim": False,
        "review_readiness_claim": False,
        "constructed_surface_readiness_claim": False,
        "publication_readiness_claim": False,
        "pilot_readiness_claim": False,
    }
    update_status_index(source_doc, relation_doc, manifest)
    write_json(STATUS_MANIFEST, manifest)


def main() -> None:
    source_doc = build_source_aware_document()
    relation_doc = build_relation_document()
    write_json(SOURCE_AWARE_OUT_JSON, source_doc)
    write_source_aware_markdown(source_doc)
    write_json(RELATION_OUT_JSON, relation_doc)
    write_relation_markdown(relation_doc)
    update_manifest(source_doc, relation_doc)
    print(
        json.dumps(
            {
                "source_aware_pointer_intake_json": str(SOURCE_AWARE_OUT_JSON),
                "source_aware_hash_verified": source_doc["totals"]["source_pointers_with_hash_verified"],
                "relation_reviewer_sheet_intake_json": str(RELATION_OUT_JSON),
                "relation_hash_verified": relation_doc["totals"]["source_pointers_with_hash_verified"],
                "reviewer_sheet_blank_semantic_slot_rows": relation_doc["totals"]["reviewer_sheet_blank_semantic_slot_rows"],
                "return_ledger_blank_rows": relation_doc["totals"]["return_ledger_blank_rows"],
                "selector_map_rows": relation_doc["totals"]["selector_map_rows"],
                "source_request_rows": relation_doc["totals"]["source_request_rows"],
                "dispatch_checklist_rows": relation_doc["totals"]["dispatch_checklist_rows"],
                "blocker_queue_open_rows": relation_doc["totals"]["blocker_queue_open_rows"],
                "evidence_intake_ledger_blank_rows": relation_doc["totals"]["evidence_intake_ledger_blank_rows"],
                "evidence_criteria_route_label_taxonomy_rows": relation_doc["totals"]["evidence_criteria_route_label_taxonomy_rows"],
                "evidence_criteria_rows": relation_doc["totals"]["evidence_criteria_rows"],
                "route_evidence_discovery_rows": relation_doc["totals"]["route_evidence_discovery_rows"],
                "route_evidence_candidate_capture_rows": relation_doc["totals"]["route_evidence_candidate_capture_rows"],
                "owner_local_standard_route_search_rows": relation_doc["totals"]["owner_local_standard_route_search_rows"],
                "local_standard_scope_selector_rows": relation_doc["totals"]["local_standard_scope_selector_rows"],
                "local_standard_source_audit_rows": relation_doc["totals"]["local_standard_source_audit_rows"],
                "local_standard_official_cache_retry_download_attempts": relation_doc["totals"]["local_standard_official_cache_retry_download_attempts"],
                "local_standard_gap_route_search_rows": relation_doc["totals"]["local_standard_gap_route_search_rows"],
                "local_standard_gap_source_audit_rows": relation_doc["totals"]["local_standard_gap_source_audit_rows"],
                "local_standard_failed_route_retry_rows": relation_doc["totals"]["local_standard_failed_route_retry_rows"],
                "local_standard_alternate_route_rows": relation_doc["totals"]["local_standard_alternate_route_rows"],
                "questions": relation_doc["totals"]["questions"],
                "queue_candidate_count": relation_doc["totals"]["max_queue_candidate_count"],
                "network_actions": 0,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
