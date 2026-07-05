import datetime
import hashlib
import json
import pathlib
import re


BASE = pathlib.Path(__file__).resolve().parents[1]
STATUS_MANIFEST = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_MANIFEST_20260629.json"
STATUS_INDEX = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_INDEX_20260629.md"
INTEGRATED_MATRIX_JSON = BASE / "INTEGRATED_LANE_HANDOFF_READINESS_MATRIX_20260630.json"
AUTHORITY_QUEUE_JSON = BASE / "EXTERNAL_AUTHORITY_REVIEW_QUEUE_20260630.json"
AUTHORITY_FORMS_JSON = BASE / "EXTERNAL_AUTHORITY_REVIEW_PACKET_FORMS_20260630.json"
METHODOLOGY_CROSSWALK_JSON = BASE / "METHODOLOGY_PUBLICATION_CROSSWALK_20260630.json"
OUT_JSON = BASE / "LANE_PROMOTION_NEXT_ACTION_QUEUE_20260630.json"
OUT_MD = BASE / "LANE_PROMOTION_NEXT_ACTION_QUEUE_20260630.md"
SELF_PATH = pathlib.Path(__file__).resolve()

STATUS = "lane_promotion_next_action_queue_local_only_not_started"


def now_utc() -> str:
    return datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="microseconds")


def sha256(path: pathlib.Path) -> str:
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
    item = {"path": artifact_path(path), "sha256": sha256(path), "bytes": path.stat().st_size}
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
                updated["sha256"] = sha256(path)
                updated["bytes"] = path.stat().st_size
                refreshed.append(updated)
            else:
                refreshed.append(item)
        manifest["artifacts"][group] = refreshed


def queue_rank(readiness_group: str) -> int:
    ranks = {
        "ready_context_note_entry_lane": 10,
        "manual_source_review_required_lane": 20,
        "source_discovery_required_before_term_queue": 30,
        "extension_cohort_support_not_edition_lane": 40,
    }
    return ranks.get(readiness_group, 90)


def action_type(readiness_group: str) -> str:
    actions = {
        "ready_context_note_entry_lane": "fill_page_context_notes",
        "manual_source_review_required_lane": "resolve_manual_source_review_rows",
        "source_discovery_required_before_term_queue": "promote_source_discovery_to_term_anchor_queue",
        "extension_cohort_support_not_edition_lane": "draft_support_cohort_authority_note",
    }
    return actions.get(readiness_group, "inspect_unclassified_lane_gate")


def blocker_class(readiness_group: str) -> str:
    blockers = {
        "ready_context_note_entry_lane": "blank_page_context_notes",
        "manual_source_review_required_lane": "manual_or_source_review_rows_unresolved",
        "source_discovery_required_before_term_queue": "source_discovery_not_promoted_to_term_queue",
        "extension_cohort_support_not_edition_lane": "support_corpus_not_edition_lane",
    }
    return blockers.get(readiness_group, "unclassified_gate_blocker")


def input_artifacts_for(readiness_group: str) -> list[str]:
    base = [
        "INTEGRATED_LANE_HANDOFF_READINESS_MATRIX_20260630.json",
        "LOCAL_SOURCE_WITNESS_SELECTION_MATRIX_20260630.json",
        "SELECTED_SOURCE_WITNESS_INSPECTION_PACKET_20260630.json",
    ]
    if readiness_group == "ready_context_note_entry_lane":
        return base + [
            "READY_CONTEXT_NOTE_ENTRY_PACKET_FRENCH_JAPANESE_20260630.json",
            "PAGE_CONTEXT_NOTE_CAPTURE_FORMS_20260630.json",
        ]
    if readiness_group == "manual_source_review_required_lane":
        return base + [
            "MANUAL_SOURCE_REVIEW_PACKET_BLOCKED_LANES_20260630.json",
            "MANUAL_SOURCE_REVIEW_TRIAGE_20260630.json",
        ]
    if readiness_group == "source_discovery_required_before_term_queue":
        return base + [
            "PERSIAN_FAMILY_DARI_TAJIK_REGISTER_GAP_20260629.json",
            "PERSIAN_FAMILY_ARABIC_TERM_ANCHOR_SEED_20260629.json",
        ]
    return base + [
        "LOCAL_SOURCE_EVIDENCE_SHELF_INVENTORY_20260630.json",
        "EXTERNAL_AUTHORITY_REVIEW_QUEUE_20260630.json",
    ]


def output_artifacts_for(readiness_group: str, lane: str) -> list[str]:
    if readiness_group == "ready_context_note_entry_lane":
        return [
            "PAGE_CONTEXT_NOTE_CAPTURE_FORMS_20260630.json",
            "READY_CONTEXT_NOTE_ENTRY_PACKET_FRENCH_JAPANESE_20260630.json",
            "EXTERNAL_AUTHORITY_REVIEW_PACKET_FORMS_20260630.json",
        ]
    if readiness_group == "manual_source_review_required_lane":
        return [
            "MANUAL_SOURCE_REVIEW_PACKET_BLOCKED_LANES_20260630.json",
            "READY_CONTEXT_NOTE_ENTRY_PACKET_FRENCH_JAPANESE_20260630.json",
            f"{lane.upper()}_POST_MANUAL_REVIEW_CONTEXT_NOTE_PACKET_TBD.json",
        ]
    if readiness_group == "source_discovery_required_before_term_queue":
        return [
            "PERSIAN_FAMILY_DARI_TAJIK_REGISTER_GAP_20260629.json",
            "PERSIAN_FAMILY_ARABIC_TERM_ANCHOR_SEED_20260629.json",
            "TG_CYRL_TJ_TERM_ANCHOR_PROMOTION_TBD.json",
        ]
    return [
        "LOCAL_SOURCE_EVIDENCE_SHELF_INVENTORY_20260630.json",
        f"{lane.upper()}_SUPPORT_COHORT_AUTHORITY_NOTE_TBD.md",
    ]


def acceptance_evidence_for(readiness_group: str, lane: str) -> list[str]:
    common = [
        "source_text_copied remains false",
        "source_language_terms_copied remains false unless a later artifact explicitly records a reviewed term anchor rather than a passage",
        "credentials_or_tokens_copied remains false",
        "native_review_status remains not_reviewed until external review returns are ingested",
        "canonical_completion_claim remains false",
    ]
    if readiness_group == "ready_context_note_entry_lane":
        return [
            f"{lane} page-context note rows are filled without source quotations",
            f"{lane} forms_filled equals ready_context_note_tasks",
            f"{lane} reviewer packet remains blank until a separate packet-population step",
        ] + common
    if readiness_group == "manual_source_review_required_lane":
        return [
            f"{lane} manual/source-review rows have a recorded source-review decision",
            f"{lane} rows are rerouted to ready context notes, rejected, or kept blocked with reason",
            f"{lane} unresolved manual_source_review_rows reaches 0 before reviewer-packet population",
        ] + common
    if readiness_group == "source_discovery_required_before_term_queue":
        return [
            f"{lane} source-discovery candidate is promoted, rejected, or kept blocked with a reason",
            f"{lane} term-anchor queue is not populated without source-discovery evidence",
            f"{lane} review packet is not populated before term-anchor promotion",
        ] + common
    return [
        f"{lane} support-cohort note records usefulness, limits, and non-edition status",
        f"{lane} remains outside canonical edition claims until explicitly promoted",
        f"{lane} authority note is linked to the relevant reviewer roles",
    ] + common


def downstream_gate(readiness_group: str) -> str:
    if readiness_group == "ready_context_note_entry_lane":
        return "external_reviewer_packet_population"
    if readiness_group == "manual_source_review_required_lane":
        return "page_context_note_entry_or_rejection_after_manual_resolution"
    if readiness_group == "source_discovery_required_before_term_queue":
        return "term_anchor_queue_population_after_source_discovery"
    return "possible_future_lane_promotion_after_support_authority_review"


def build_lane_action_rows(matrix: dict) -> list[dict]:
    rows = []
    for source in matrix.get("lane_or_cohort_rows", []):
        readiness = source.get("readiness_group")
        lane = source["lane_or_cohort"]
        row = {
            "queue_id": "lane-promotion-" + lane.replace("_", "-").lower(),
            "queue_rank": queue_rank(readiness),
            "lane_or_cohort": lane,
            "kind": source.get("kind"),
            "label": source.get("label"),
            "action_type": action_type(readiness),
            "blocker_class": blocker_class(readiness),
            "current_handoff_readiness_status": source.get("handoff_readiness_status"),
            "next_gate_from_integrated_matrix": source.get("next_gate"),
            "downstream_gate_unlocked_if_accepted": downstream_gate(readiness),
            "work_units": source.get("inspection_tasks", 0),
            "ready_context_note_tasks": source.get("ready_context_note_tasks", 0),
            "manual_source_review_tasks": source.get("manual_source_review_tasks", 0),
            "source_discovery_tasks": source.get("source_discovery_tasks", 0),
            "support_cohort_tasks": source.get("support_cohort_tasks", 0),
            "selected_witnesses": source.get("selected_witnesses", 0),
            "selected_witnesses_with_source_core": source.get("selected_witnesses_with_source_core", 0),
            "filesystem_missing_paths": source.get("filesystem_missing_paths", 0),
            "source_core_delta_shelves": source.get("planned_delta_shelves", 0),
            "source_core_delta_text_source_like_gap_files": source.get("planned_delta_text_source_like_gap_files", 0),
            "authority_reviewer_role_forms": source.get("authority_reviewer_role_forms", 0),
            "required_reviewer_roles": source.get("required_reviewer_roles", []),
            "input_artifacts": input_artifacts_for(readiness),
            "output_artifacts_to_update_or_create": output_artifacts_for(readiness, lane),
            "acceptance_evidence_required": acceptance_evidence_for(readiness, lane),
            "current_state": "queued_not_started",
            "local_execution_allowed_without_network": True,
            "review_fields_filled": 0,
            "review_packets_sent": 0,
            "review_returns_received": 0,
            "external_reviews_performed": 0,
            "accepted_corrections_ingested": 0,
            "review_packet_population_performed": False,
            "translation_or_revision_performed": False,
            "source_text_copied": False,
            "source_language_terms_copied": False,
            "native_review_status": "not_reviewed",
            "canonical_approval_status": "not_approved",
            "canonical_completion_claim": False,
            "publication_completion_claim": False,
            "current_approved_terms": 0,
            "current_accepted_corrections": 0,
        }
        rows.append(row)
    return sorted(rows, key=lambda row: (row["queue_rank"], row["kind"], row["lane_or_cohort"]))


def build_methodology_action_rows(queue: dict, forms: dict, crosswalk: dict) -> list[dict]:
    packets = {
        group.get("queue_id"): group
        for group in forms.get("packet_groups_detail", [])
        if group.get("queue_group") == "methodology_authority"
    }
    rows = []
    for source in queue.get("methodology_authority_queue_rows", []):
        packet = packets.get(source.get("queue_id"), {})
        rows.append(
            {
                "queue_id": "publication-" + source["queue_id"].replace("_", "-").lower(),
                "source_queue_id": source.get("queue_id"),
                "lane_type": source.get("lane_type"),
                "action_type": "obtain_methodology_authority_review",
                "blocker_class": "methodology_claim_review_not_returned",
                "requirements": source.get("requirements", []),
                "claim_taxonomy_rows_relevant": source.get("claim_taxonomy_rows_relevant", 0),
                "authority_gate": source.get("authority_gate"),
                "blocked_claims": source.get("blocked_claims", []),
                "reviewer_role_forms": packet.get("reviewer_role_forms", source.get("required_reviewer_role_count", 0)),
                "required_reviewer_roles": source.get("required_reviewer_roles", []),
                "input_artifacts": [
                    "METHODOLOGY_PUBLICATION_CROSSWALK_20260630.json",
                    "EXTERNAL_AUTHORITY_REVIEW_QUEUE_20260630.json",
                    "EXTERNAL_AUTHORITY_REVIEW_PACKET_FORMS_20260630.json",
                    "INTERLANGUAGE_REVIEWER_AUTHORITY_DECISION_FRAMEWORK_20260629.json",
                ],
                "output_artifacts_to_update_or_create": [
                    "EXTERNAL_AUTHORITY_REVIEW_PACKET_FORMS_20260630.json",
                    "ACCEPTED_CORRECTION_LEDGER_TEMPLATE_20260629.json",
                    "METHODOLOGY_PUBLICATION_CROSSWALK_20260630.json",
                ],
                "acceptance_evidence_required": [
                    "methodology reviewer identity or role is recorded",
                    "claim scope authorized by reviewer is recorded",
                    "required revisions or remaining blockers are recorded",
                    "accepted corrections are ingested through the correction ledger before publication claims",
                    "publication_completion_claim remains false unless all methodology review gates clear",
                ],
                "current_state": "queued_not_started",
                "review_fields_filled": 0,
                "review_packets_sent": 0,
                "review_returns_received": 0,
                "external_reviews_performed": 0,
                "accepted_corrections_ingested": 0,
                "publication_completion_claim": False,
                "native_review_status": "not_reviewed",
                "current_approved_terms": 0,
                "current_accepted_corrections": 0,
                "crosswalk_status": crosswalk.get("status"),
            }
        )
    return rows


def build_batch_groups(lane_rows: list[dict], methodology_rows: list[dict]) -> list[dict]:
    groups = []
    specs = [
        ("ready_context_note_batch", "fill_page_context_notes"),
        ("manual_source_review_resolution_batch", "resolve_manual_source_review_rows"),
        ("source_discovery_promotion_batch", "promote_source_discovery_to_term_anchor_queue"),
        ("support_cohort_authority_note_batch", "draft_support_cohort_authority_note"),
    ]
    for group_id, action in specs:
        rows = [row for row in lane_rows if row["action_type"] == action]
        groups.append(
            {
                "batch_id": group_id,
                "action_type": action,
                "lane_or_cohort_count": len(rows),
                "work_units": sum(row["work_units"] for row in rows),
                "authority_reviewer_role_forms": sum(row["authority_reviewer_role_forms"] for row in rows),
                "current_state": "queued_not_started",
                "network_required": False,
                "lane_or_cohort_ids": [row["lane_or_cohort"] for row in rows],
            }
        )
    groups.append(
        {
            "batch_id": "methodology_authority_review_batch",
            "action_type": "obtain_methodology_authority_review",
            "lane_or_cohort_count": 0,
            "methodology_queue_rows": len(methodology_rows),
            "work_units": len(methodology_rows),
            "authority_reviewer_role_forms": sum(row["reviewer_role_forms"] for row in methodology_rows),
            "current_state": "queued_not_started",
            "network_required": False,
            "methodology_queue_ids": [row["source_queue_id"] for row in methodology_rows],
        }
    )
    return groups


def build_summary(lane_rows: list[dict], methodology_rows: list[dict], matrix: dict) -> dict:
    matrix_summary = matrix.get("summary", {})
    return {
        "lane_action_rows": len(lane_rows),
        "core_language_lane_action_rows": sum(1 for row in lane_rows if row.get("kind") == "core_language_lane"),
        "extension_cohort_action_rows": sum(1 for row in lane_rows if row.get("kind") == "extension_cohort"),
        "ready_context_note_action_rows": sum(1 for row in lane_rows if row["action_type"] == "fill_page_context_notes"),
        "manual_source_review_action_rows": sum(1 for row in lane_rows if row["action_type"] == "resolve_manual_source_review_rows"),
        "source_discovery_action_rows": sum(1 for row in lane_rows if row["action_type"] == "promote_source_discovery_to_term_anchor_queue"),
        "support_cohort_action_rows": sum(1 for row in lane_rows if row["action_type"] == "draft_support_cohort_authority_note"),
        "lane_work_units": sum(row["work_units"] for row in lane_rows),
        "ready_context_note_work_units": sum(row["ready_context_note_tasks"] for row in lane_rows),
        "manual_source_review_work_units": sum(row["manual_source_review_tasks"] for row in lane_rows),
        "source_discovery_work_units": sum(row["source_discovery_tasks"] for row in lane_rows),
        "support_cohort_work_units": sum(row["support_cohort_tasks"] for row in lane_rows),
        "methodology_action_rows": len(methodology_rows),
        "methodology_reviewer_role_forms": sum(row["reviewer_role_forms"] for row in methodology_rows),
        "lane_authority_reviewer_role_forms": sum(row["authority_reviewer_role_forms"] for row in lane_rows),
        "total_authority_reviewer_role_forms": sum(row["authority_reviewer_role_forms"] for row in lane_rows)
        + sum(row["reviewer_role_forms"] for row in methodology_rows),
        "source_core_delta_shelves": matrix_summary.get("planned_delta_shelves", 0),
        "source_core_delta_text_source_like_gap_files": matrix_summary.get("planned_text_source_like_gap_files", 0),
        "source_core_delta_planned_chunks": matrix_summary.get("planned_delta_chunks", 0),
        "filesystem_missing_paths": matrix_summary.get("selected_witness_slots_missing_paths", 0),
        "queue_rows_not_started": len(lane_rows) + len(methodology_rows),
        "local_execution_rows": len(lane_rows),
        "network_actions_performed": 0,
        "review_fields_filled": 0,
        "review_packets_sent": 0,
        "review_returns_received": 0,
        "external_reviews_performed": 0,
        "accepted_corrections_ingested": 0,
        "review_packet_population_performed": False,
        "translation_or_revision_performed": False,
        "canonical_completion_claim": False,
        "publication_completion_claim": False,
        "native_review_status": "not_reviewed",
        "current_approved_terms": 0,
        "current_accepted_corrections": 0,
    }


def build_document(manifest: dict) -> dict:
    matrix = load_json(INTEGRATED_MATRIX_JSON)
    authority_queue = load_json(AUTHORITY_QUEUE_JSON)
    authority_forms = load_json(AUTHORITY_FORMS_JSON)
    methodology_crosswalk = load_json(METHODOLOGY_CROSSWALK_JSON)
    lane_rows = build_lane_action_rows(matrix)
    methodology_rows = build_methodology_action_rows(authority_queue, authority_forms, methodology_crosswalk)
    batch_groups = build_batch_groups(lane_rows, methodology_rows)
    summary = build_summary(lane_rows, methodology_rows, matrix)
    return {
        "artifact": "lane_promotion_next_action_queue",
        "generated_utc": now_utc(),
        "generated_date": "20260630",
        "status": STATUS,
        "bandwidth_mode": "local_only_no_network_actions",
        "inputs": {
            "status_manifest": STATUS_MANIFEST.name,
            "integrated_matrix": INTEGRATED_MATRIX_JSON.name,
            "authority_queue": AUTHORITY_QUEUE_JSON.name,
            "authority_forms": AUTHORITY_FORMS_JSON.name,
            "methodology_crosswalk": METHODOLOGY_CROSSWALK_JSON.name,
        },
        "queue_policy": {
            "source_witnesses_before_translation_or_revision": True,
            "no_reviewer_packet_population_from_blank_notes": True,
            "manual_review_resolution_before_canonical_term_promotion": True,
            "external_authority_before_native_acceptability_claims": True,
            "support_cohort_is_not_edition_lane": True,
            "network_upload_push_or_download_deferred": True,
            "local_queue_is_not_completion_evidence": True,
        },
        "summary": summary,
        "batch_groups": batch_groups,
        "lane_action_rows": lane_rows,
        "methodology_action_rows": methodology_rows,
        "boundaries": {
            "local_mechanical_queue_only": True,
            "external_or_native_review_not_performed": True,
            "source_text_not_copied": True,
            "source_language_terms_not_copied": True,
            "credentials_or_tokens_not_copied": True,
            "no_network_actions_performed": True,
            "remote_upload_or_push_not_performed": True,
        },
        "no_network_actions_performed": True,
        "credentials_or_tokens_copied": False,
        "source_text_copied": False,
        "source_language_terms_copied": False,
        "native_review_status": "not_reviewed",
        "current_approved_terms": 0,
        "current_accepted_corrections": 0,
        "canonical_completion_claim": False,
        "publication_completion_claim": False,
        "manifest_status_at_build_time": manifest.get("status"),
    }


def write_markdown(document: dict) -> None:
    summary = document["summary"]
    lines = [
        "# Lane Promotion Next-Action Queue - 2026-06-30",
        "",
        f"Status: `{document['status']}`",
        "",
        "This queue turns the integrated handoff matrix into the next local actions required before any non-Slavic lane can move toward reviewer packet population, canonical terminology, translation/revision, or publication claims.",
        "",
        "## Summary",
        "",
        f"- Lane/cohort action rows: {summary['lane_action_rows']} ({summary['core_language_lane_action_rows']} core lanes, {summary['extension_cohort_action_rows']} extension cohorts)",
        f"- Work units: {summary['lane_work_units']} ({summary['ready_context_note_work_units']} ready-note, {summary['manual_source_review_work_units']} manual/source-review, {summary['source_discovery_work_units']} source-discovery, {summary['support_cohort_work_units']} support)",
        f"- Methodology authority actions: {summary['methodology_action_rows']} rows / {summary['methodology_reviewer_role_forms']} reviewer-role forms",
        f"- Authority forms in queue: {summary['total_authority_reviewer_role_forms']} total ({summary['lane_authority_reviewer_role_forms']} lane, {summary['methodology_reviewer_role_forms']} methodology)",
        f"- Source-core delta remains planned only: {summary['source_core_delta_shelves']} shelves / {summary['source_core_delta_text_source_like_gap_files']} text-source-like gap files / {summary['source_core_delta_planned_chunks']} planned chunks",
        "- Review fields filled: 0; reviews received: 0; accepted corrections: 0; network actions: 0",
        "",
        "## Batch Groups",
        "",
        "| Batch | Action | Rows | Work units | Authority forms | State |",
        "|---|---|---:|---:|---:|---|",
    ]
    for batch in document["batch_groups"]:
        rows = batch.get("lane_or_cohort_count", batch.get("methodology_queue_rows", 0))
        if batch["batch_id"] == "methodology_authority_review_batch":
            rows = batch.get("methodology_queue_rows", 0)
        lines.append(
            f"| {batch['batch_id']} | {batch['action_type']} | {rows} | {batch['work_units']} | {batch['authority_reviewer_role_forms']} | {batch['current_state']} |"
        )
    lines.extend(
        [
            "",
            "## Lane Queue",
            "",
            "| Rank | Lane/cohort | Action | Work units | Blocker | Acceptance gate |",
            "|---:|---|---|---:|---|---|",
        ]
    )
    for row in document["lane_action_rows"]:
        lines.append(
            f"| {row['queue_rank']} | {row['lane_or_cohort']} | {row['action_type']} | {row['work_units']} | {row['blocker_class']} | {row['downstream_gate_unlocked_if_accepted']} |"
        )
    lines.extend(
        [
            "",
            "## Methodology Queue",
            "",
            "| Queue | Lane type | Reviewer forms | Authority gate | State |",
            "|---|---|---:|---|---|",
        ]
    )
    for row in document["methodology_action_rows"]:
        lines.append(
            f"| {row['source_queue_id']} | {row['lane_type']} | {row['reviewer_role_forms']} | {row['authority_gate']} | {row['current_state']} |"
        )
    lines.extend(
        [
            "",
            "## Boundary Notes",
            "",
            "- This queue is not proof of completion; it is the next-action ledger.",
            "- It permits local work on notes, manual review resolution, source-discovery promotion, and support-cohort authority notes.",
            "- It does not authorize remote uploads, reviewer packet population, translation/revision, native acceptability claims, or canonical completion claims.",
        ]
    )
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def update_status_index(document: dict, manifest: dict) -> None:
    text = STATUS_INDEX.read_text(encoding="utf-8")
    counts = {
        "json": len(manifest["artifacts"]["json"]),
        "markdown": len(manifest["artifacts"]["markdown"]),
        "scripts": len(manifest["artifacts"]["scripts"]),
    }
    text = re.sub(
        r"- JSON artifacts indexed: \d+ plus this status manifest",
        f"- JSON artifacts indexed: {counts['json']} plus this status manifest",
        text,
    )
    text = re.sub(
        r"- Markdown artifacts indexed: \d+ plus this status index",
        f"- Markdown artifacts indexed: {counts['markdown']} plus this status index",
        text,
    )
    text = re.sub(
        r"- Reproducible scripts indexed: \d+",
        f"- Reproducible scripts indexed: {counts['scripts']}",
        text,
    )
    summary = document["summary"]
    line = (
        "- Lane promotion next-action queue: "
        f"{summary['lane_action_rows']} lane/cohort actions / "
        f"{summary['lane_work_units']} lane work units / "
        f"{summary['methodology_action_rows']} methodology actions / "
        "0 network actions"
    )
    if re.search(r"^- Lane promotion next-action queue: .*", text, flags=re.MULTILINE):
        text = re.sub(r"^- Lane promotion next-action queue: .*", line, text, flags=re.MULTILINE)
    else:
        marker = "- Integrated lane handoff readiness matrix:"
        rows = text.splitlines()
        inserted = False
        for offset, row in enumerate(rows):
            if row.startswith(marker):
                rows.insert(offset + 1, line)
                text = "\n".join(rows) + "\n"
                inserted = True
                break
        if not inserted:
            text = text.rstrip() + "\n" + line + "\n"
    text = text.replace(
        "integrated-handoff-readiness metadata",
        "integrated-handoff-readiness/lane-promotion-next-action metadata",
    )
    text = text.replace(
        "lane-promotion-next-action/lane-promotion-next-action metadata",
        "lane-promotion-next-action metadata",
    )
    if "Generated UTC: " in text:
        old = text.split("Generated UTC: ", 1)[1].splitlines()[0]
        text = text.replace(old, manifest["generated_utc"], 1)
    STATUS_INDEX.write_text(text, encoding="utf-8")


def update_manifest(document: dict) -> None:
    manifest = load_json(STATUS_MANIFEST)
    manifest["generated_utc"] = now_utc()
    upsert_artifact(manifest, "json", OUT_JSON, STATUS)
    upsert_artifact(manifest, "markdown", OUT_MD)
    upsert_artifact(manifest, "scripts", SELF_PATH)
    refresh_existing_artifact_hashes(manifest)
    summary = document["summary"]
    manifest["lane_promotion_next_action_queue"] = {
        "status": document["status"],
        "artifact_markdown": OUT_MD.name,
        "artifact_json": OUT_JSON.name,
        "lane_action_rows": summary["lane_action_rows"],
        "core_language_lane_action_rows": summary["core_language_lane_action_rows"],
        "extension_cohort_action_rows": summary["extension_cohort_action_rows"],
        "ready_context_note_action_rows": summary["ready_context_note_action_rows"],
        "manual_source_review_action_rows": summary["manual_source_review_action_rows"],
        "source_discovery_action_rows": summary["source_discovery_action_rows"],
        "support_cohort_action_rows": summary["support_cohort_action_rows"],
        "lane_work_units": summary["lane_work_units"],
        "ready_context_note_work_units": summary["ready_context_note_work_units"],
        "manual_source_review_work_units": summary["manual_source_review_work_units"],
        "source_discovery_work_units": summary["source_discovery_work_units"],
        "support_cohort_work_units": summary["support_cohort_work_units"],
        "methodology_action_rows": summary["methodology_action_rows"],
        "methodology_reviewer_role_forms": summary["methodology_reviewer_role_forms"],
        "lane_authority_reviewer_role_forms": summary["lane_authority_reviewer_role_forms"],
        "total_authority_reviewer_role_forms": summary["total_authority_reviewer_role_forms"],
        "source_core_delta_shelves": summary["source_core_delta_shelves"],
        "source_core_delta_text_source_like_gap_files": summary["source_core_delta_text_source_like_gap_files"],
        "source_core_delta_planned_chunks": summary["source_core_delta_planned_chunks"],
        "queue_rows_not_started": summary["queue_rows_not_started"],
        "network_actions_performed": 0,
        "review_fields_filled": 0,
        "review_packets_sent": 0,
        "review_returns_received": 0,
        "external_reviews_performed": 0,
        "accepted_corrections_ingested": 0,
        "review_packet_population_performed": False,
        "translation_or_revision_performed": False,
        "canonical_completion_claim": False,
        "publication_completion_claim": False,
        "no_network_actions_performed": True,
        "credentials_or_tokens_copied": False,
        "source_text_copied": False,
        "source_language_terms_copied": False,
        "native_review_status": "not_reviewed",
        "current_approved_terms": 0,
        "current_accepted_corrections": 0,
    }
    write_json(OUT_JSON, document)
    write_markdown(document)
    upsert_artifact(manifest, "json", OUT_JSON, STATUS)
    upsert_artifact(manifest, "markdown", OUT_MD)
    upsert_artifact(manifest, "scripts", SELF_PATH)
    refresh_existing_artifact_hashes(manifest)
    update_status_index(document, manifest)
    write_json(STATUS_MANIFEST, manifest)


def main() -> None:
    manifest = load_json(STATUS_MANIFEST)
    document = build_document(manifest)
    write_json(OUT_JSON, document)
    write_markdown(document)
    update_manifest(document)
    print(
        json.dumps(
            {
                "lane_promotion_next_action_queue_json": str(OUT_JSON),
                "lane_action_rows": document["summary"]["lane_action_rows"],
                "lane_work_units": document["summary"]["lane_work_units"],
                "methodology_action_rows": document["summary"]["methodology_action_rows"],
                "total_authority_reviewer_role_forms": document["summary"]["total_authority_reviewer_role_forms"],
                "network_actions_performed": document["summary"]["network_actions_performed"],
                "no_network_actions_performed": document["no_network_actions_performed"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
