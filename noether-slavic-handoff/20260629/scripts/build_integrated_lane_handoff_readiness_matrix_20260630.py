import datetime
import hashlib
import json
import pathlib
import re


BASE = pathlib.Path(__file__).resolve().parents[1]
STATUS_MANIFEST = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_MANIFEST_20260629.json"
STATUS_INDEX = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_INDEX_20260629.md"
GATE_DASHBOARD_JSON = BASE / "NON_SLAVIC_LANE_GATE_DASHBOARD_20260630.json"
SELECTION_MATRIX_JSON = BASE / "LOCAL_SOURCE_WITNESS_SELECTION_MATRIX_20260630.json"
INSPECTION_PACKET_JSON = BASE / "SELECTED_SOURCE_WITNESS_INSPECTION_PACKET_20260630.json"
FILESYSTEM_VALIDATION_JSON = BASE / "SELECTED_SOURCE_WITNESS_FILESYSTEM_VALIDATION_20260630.json"
SOURCE_CORE_GAP_JSON = BASE / "SELECTED_SOURCE_WITNESS_SOURCE_CORE_COVERAGE_GAP_20260630.json"
DELTA_STAGING_JSON = BASE / "SELECTED_SOURCE_WITNESS_TEXT_TEX_DELTA_STAGING_PLAN_20260630.json"
AUTHORITY_QUEUE_JSON = BASE / "EXTERNAL_AUTHORITY_REVIEW_QUEUE_20260630.json"
AUTHORITY_FORMS_JSON = BASE / "EXTERNAL_AUTHORITY_REVIEW_PACKET_FORMS_20260630.json"
METHODOLOGY_CROSSWALK_JSON = BASE / "METHODOLOGY_PUBLICATION_CROSSWALK_20260630.json"
OUT_JSON = BASE / "INTEGRATED_LANE_HANDOFF_READINESS_MATRIX_20260630.json"
OUT_MD = BASE / "INTEGRATED_LANE_HANDOFF_READINESS_MATRIX_20260630.md"
SELF_PATH = pathlib.Path(__file__).resolve()

STATUS = "integrated_lane_handoff_readiness_matrix_no_review_no_completion_claim"


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


def by_lane(rows: list[dict]) -> dict[str, dict]:
    return {row["lane_or_cohort"]: row for row in rows if row.get("lane_or_cohort")}


def task_count(row: dict, task_kind: str) -> int:
    return int(row.get("task_kind_counts", {}).get(task_kind, 0))


def readiness_status(selection_row: dict) -> str:
    group = selection_row.get("readiness_group")
    if group == "ready_context_note_entry_lane":
        return "blocked_pending_page_context_notes_and_external_review"
    if group == "manual_source_review_required_lane":
        return "blocked_pending_manual_source_review_and_external_authority"
    if group == "source_discovery_required_before_term_queue":
        return "blocked_pending_source_discovery_promotion"
    return "support_shelf_not_edition_lane_pending_authority_notes"


def next_gate(selection_row: dict) -> str:
    group = selection_row.get("readiness_group")
    if group == "ready_context_note_entry_lane":
        return "fill_page_context_notes_then_populate_external_review_packet"
    if group == "manual_source_review_required_lane":
        return "resolve_manual_source_review_rows_before_context_notes_or_review_packet_population"
    if group == "source_discovery_required_before_term_queue":
        return "promote_source_discovery_into_term_anchor_queue_before_any_canonical_lane_claim"
    return "keep_as_support_source_shelf_until_edition_lane_is_explicitly_promoted_and_reviewed"


def build_lane_rows(inputs: dict) -> list[dict]:
    gate_by_lane = by_lane(inputs["gate_dashboard"].get("lane_gates", []))
    selection_rows = inputs["selection_matrix"].get("matrix_rows", [])
    inspection_by_lane = by_lane(inputs["inspection_packet"].get("lane_summaries", []))
    validation_by_lane = by_lane(inputs["filesystem_validation"].get("lane_validation_rows", []))
    coverage_by_lane = by_lane(inputs["source_core_gap"].get("lane_coverage_rows", []))
    delta_by_lane = by_lane(inputs["delta_staging"].get("lane_delta_rows", []))
    authority_by_lane = by_lane(inputs["authority_queue"].get("lane_authority_queue_rows", []))
    packet_by_lane = by_lane(
        [
            group
            for group in inputs["authority_forms"].get("packet_groups_detail", [])
            if group.get("queue_group") == "lane_authority"
        ]
    )

    rows = []
    for selection in selection_rows:
        lane = selection["lane_or_cohort"]
        gate = gate_by_lane.get(lane, {})
        inspection = inspection_by_lane.get(lane, {})
        validation = validation_by_lane.get(lane, {})
        coverage = coverage_by_lane.get(lane, {})
        delta = delta_by_lane.get(lane, {})
        authority = authority_by_lane.get(lane, {})
        packet = packet_by_lane.get(lane, {})
        required_roles = authority.get("required_reviewer_roles", [])

        row = {
            "lane_or_cohort": lane,
            "kind": selection.get("kind"),
            "label": selection.get("label", gate.get("label", lane)),
            "edition_gate": selection.get("edition_gate"),
            "source_gate_use": selection.get("source_gate_use"),
            "readiness_group": selection.get("readiness_group"),
            "handoff_readiness_status": readiness_status(selection),
            "next_gate": next_gate(selection),
            "selected_witnesses": selection.get("selected_witnesses_count", 0),
            "selected_witnesses_with_source_core": selection.get("selected_witnesses_with_source_core", 0),
            "selected_text_source_like_files": selection.get("selected_text_source_like_files", 0),
            "selected_tex_files": selection.get("selected_tex_files", 0),
            "selected_pdf_files_counted_not_packaged": selection.get("selected_pdf_files", 0),
            "selected_source_core_files": selection.get("selected_source_core_files", 0),
            "filesystem_paths_existing": validation.get("paths_existing", 0),
            "filesystem_missing_paths": validation.get("missing_paths", 0),
            "unique_witness_shelves": validation.get("unique_witness_shelves", 0),
            "filesystem_files_counted": validation.get("files", 0),
            "filesystem_text_source_like_files": validation.get("text_source_like_files", 0),
            "filesystem_tex_files": validation.get("tex_files", 0),
            "source_core_gap_shelves": coverage.get("local_only_gap_shelves", 0),
            "partial_source_core_text_coverage_shelves": coverage.get("partial_coverage_shelves", 0),
            "source_core_text_like_gap_files": coverage.get("source_core_text_like_gap_estimate", 0),
            "planned_delta_shelves": delta.get("planned_delta_shelves", 0),
            "planned_delta_text_source_like_gap_files": delta.get("text_source_like_gap_files", 0),
            "planned_delta_tex_files_on_shelves": delta.get("tex_files_on_shelves", 0),
            "planned_delta_estimated_uncompressed_bytes": delta.get("estimated_uncompressed_bytes", 0),
            "planned_delta_status": "planned_only_no_file_list_no_archive_no_upload",
            "inspection_tasks": inspection.get("inspection_tasks", 0),
            "ready_context_note_tasks": task_count(inspection, "ready_context_note_entry"),
            "manual_source_review_tasks": task_count(inspection, "manual_source_review_resolution"),
            "source_discovery_tasks": task_count(inspection, "source_discovery_promotion"),
            "support_cohort_tasks": task_count(inspection, "support_cohort_authority_note"),
            "witness_task_links": inspection.get("witness_task_links", 0),
            "ready_context_note_forms": selection.get("ready_context_note_forms", 0),
            "manual_source_review_rows": selection.get("manual_source_review_rows", 0),
            "gate_dashboard_status": gate.get("gate_status"),
            "gate_dashboard_tasks": gate.get("tasks", 0),
            "gate_dashboard_ready_after_extraction_check": gate.get("ready_after_extraction_check", 0),
            "gate_dashboard_manual_or_source_review_required": gate.get("manual_or_source_review_required", 0),
            "authority_queue_kind": authority.get("queue_kind"),
            "authority_gate": authority.get("authority_gate"),
            "authority_packet_groups": 1 if packet else 0,
            "authority_reviewer_role_forms": packet.get("reviewer_role_forms", len(required_roles)),
            "authority_distinct_reviewer_roles": len(set(required_roles)),
            "required_reviewer_roles": required_roles,
            "review_fields_filled": packet.get("review_fields_filled", 0),
            "review_packets_sent": 1 if packet.get("review_packet_sent") is True else 0,
            "review_returns_received": 1 if packet.get("review_return_received") is True else 0,
            "external_reviews_performed": packet.get("external_reviews_performed", 0),
            "accepted_corrections_ingested": packet.get("accepted_corrections_ingested", 0),
            "forms_filled": selection.get("forms_filled", 0),
            "inspection_outputs_filled": inspection.get("inspection_outputs_filled", False),
            "review_packet_population_performed": False,
            "translation_or_revision_performed": False,
            "actual_delta_archive_created": delta.get("actual_delta_archive_created", False),
            "actual_remote_upload_performed": delta.get("actual_remote_upload_performed", False),
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
    return rows


def build_methodology_summary(inputs: dict) -> dict:
    crosswalk = inputs["methodology_crosswalk"]
    queue = inputs["authority_queue"]
    forms = inputs["authority_forms"]
    methodology_groups = [
        group
        for group in forms.get("packet_groups_detail", [])
        if group.get("queue_group") == "methodology_authority"
    ]
    methodology_roles = [form["reviewer_role"] for group in methodology_groups for form in group.get("forms", [])]
    return {
        "status": "research_publication_lane_active_no_external_authority_claim",
        "working_titles": crosswalk.get("summary", {}).get("working_titles", 0),
        "case_study_lanes": crosswalk.get("summary", {}).get("case_study_lanes", 0),
        "method_sections": crosswalk.get("summary", {}).get("method_sections", 0),
        "claim_taxonomy_rows": crosswalk.get("summary", {}).get("claim_taxonomy_rows", 0),
        "review_authority_checklists": crosswalk.get("summary", {}).get("review_authority_checklists", 0),
        "claims_allowed_now": crosswalk.get("summary", {}).get("claims_allowed_now", 0),
        "claims_not_allowed_yet": crosswalk.get("summary", {}).get("claims_not_allowed_yet", 0),
        "methodology_authority_queue_rows": len(queue.get("methodology_authority_queue_rows", [])),
        "methodology_packet_groups": len(methodology_groups),
        "methodology_reviewer_role_forms": len(methodology_roles),
        "methodology_distinct_reviewer_roles": len(set(methodology_roles)),
        "review_fields_filled": 0,
        "review_packets_sent": 0,
        "review_returns_received": 0,
        "external_reviews_performed": 0,
        "accepted_corrections_ingested": 0,
        "canonical_completion_claim": False,
        "publication_completion_claim": False,
        "native_review_status": "not_reviewed",
        "current_approved_terms": 0,
        "current_accepted_corrections": 0,
    }


def build_summary(rows: list[dict], inputs: dict, methodology_summary: dict) -> dict:
    forms_summary = inputs["authority_forms"].get("summary", {})
    inspection_summary = inputs["inspection_packet"].get("summary", {})
    validation_summary = inputs["filesystem_validation"].get("summary", {})
    delta_summary = inputs["delta_staging"].get("summary", {})
    queue = inputs["authority_queue"]
    return {
        "lane_or_cohort_rows": len(rows),
        "core_language_lanes": sum(1 for row in rows if row.get("kind") == "core_language_lane"),
        "extension_cohorts": sum(1 for row in rows if row.get("kind") == "extension_cohort"),
        "selected_witnesses": sum(row["selected_witnesses"] for row in rows),
        "selected_witnesses_with_source_core": sum(row["selected_witnesses_with_source_core"] for row in rows),
        "selected_witness_slots_missing_paths": validation_summary.get("slot_missing_paths", 0),
        "unique_witness_shelves": validation_summary.get("unique_witness_shelves", 0),
        "unique_witness_shelves_missing_paths": validation_summary.get("unique_missing_paths", 0),
        "inspection_tasks": inspection_summary.get("inspection_task_count", sum(row["inspection_tasks"] for row in rows)),
        "ready_context_note_tasks": inspection_summary.get("ready_context_note_tasks", 0),
        "manual_source_review_tasks": inspection_summary.get("manual_source_review_tasks", 0),
        "source_discovery_tasks": inspection_summary.get("source_discovery_tasks", 0),
        "support_cohort_tasks": inspection_summary.get("support_cohort_tasks", 0),
        "ready_context_note_forms": sum(row["ready_context_note_forms"] for row in rows),
        "manual_source_review_rows": sum(row["manual_source_review_rows"] for row in rows),
        "lane_authority_queue_rows": len(queue.get("lane_authority_queue_rows", [])),
        "lane_authority_packet_groups": forms_summary.get("lane_packet_groups", 0),
        "lane_reviewer_role_forms": forms_summary.get("lane_reviewer_role_forms", 0),
        "total_authority_packet_groups": forms_summary.get("packet_groups", 0),
        "total_reviewer_role_forms": forms_summary.get("reviewer_role_forms", 0),
        "distinct_reviewer_roles": forms_summary.get("distinct_reviewer_roles", 0),
        "methodology_authority_queue_rows": methodology_summary["methodology_authority_queue_rows"],
        "methodology_packet_groups": methodology_summary["methodology_packet_groups"],
        "methodology_reviewer_role_forms": methodology_summary["methodology_reviewer_role_forms"],
        "planned_delta_shelves": delta_summary.get("planned_delta_shelves", 0),
        "planned_text_source_like_gap_files": delta_summary.get("planned_text_source_like_gap_files", 0),
        "planned_delta_chunks": delta_summary.get("planned_chunks", 0),
        "planned_delta_estimated_compressed_bytes": delta_summary.get("estimated_compressed_bytes", 0),
        "review_fields_filled": 0,
        "review_packets_sent": 0,
        "review_returns_received": 0,
        "external_reviews_performed": 0,
        "accepted_corrections_ingested": 0,
        "forms_filled": 0,
        "inspection_outputs_filled": False,
        "review_packet_population_performed": False,
        "translation_or_revision_performed": False,
        "canonical_completion_claim": False,
        "publication_completion_claim": False,
        "native_review_status": "not_reviewed",
        "current_approved_terms": 0,
        "current_accepted_corrections": 0,
    }


def build_document(manifest: dict) -> dict:
    inputs = {
        "gate_dashboard": load_json(GATE_DASHBOARD_JSON),
        "selection_matrix": load_json(SELECTION_MATRIX_JSON),
        "inspection_packet": load_json(INSPECTION_PACKET_JSON),
        "filesystem_validation": load_json(FILESYSTEM_VALIDATION_JSON),
        "source_core_gap": load_json(SOURCE_CORE_GAP_JSON),
        "delta_staging": load_json(DELTA_STAGING_JSON),
        "authority_queue": load_json(AUTHORITY_QUEUE_JSON),
        "authority_forms": load_json(AUTHORITY_FORMS_JSON),
        "methodology_crosswalk": load_json(METHODOLOGY_CROSSWALK_JSON),
    }
    rows = build_lane_rows(inputs)
    methodology_summary = build_methodology_summary(inputs)
    summary = build_summary(rows, inputs, methodology_summary)
    return {
        "artifact": "integrated_lane_handoff_readiness_matrix",
        "generated_utc": now_utc(),
        "generated_date": "20260630",
        "status": STATUS,
        "bandwidth_mode": "local_only_no_network_actions",
        "inputs": {
            "status_manifest": STATUS_MANIFEST.name,
            "gate_dashboard": GATE_DASHBOARD_JSON.name,
            "selection_matrix": SELECTION_MATRIX_JSON.name,
            "inspection_packet": INSPECTION_PACKET_JSON.name,
            "filesystem_validation": FILESYSTEM_VALIDATION_JSON.name,
            "source_core_gap": SOURCE_CORE_GAP_JSON.name,
            "delta_staging": DELTA_STAGING_JSON.name,
            "authority_queue": AUTHORITY_QUEUE_JSON.name,
            "authority_forms": AUTHORITY_FORMS_JSON.name,
            "methodology_crosswalk": METHODOLOGY_CROSSWALK_JSON.name,
        },
        "handoff_rules": {
            "source_witnesses_must_be_used_before_translation_or_revision": True,
            "blank_context_notes_do_not_authorize_reviewer_packet_population": True,
            "manual_source_review_rows_block_canonical_term_promotion": True,
            "external_authority_review_required_before_native_acceptability_claims": True,
            "support_cohorts_are_not_edition_lanes_until_explicitly_promoted": True,
            "local_validation_is_mechanical_not_native_authority": True,
        },
        "summary": summary,
        "lane_or_cohort_rows": rows,
        "methodology_publication_summary": methodology_summary,
        "boundaries": {
            "local_mechanical_validation_only": True,
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
        "# Integrated Lane Handoff Readiness Matrix - 2026-06-30",
        "",
        f"Status: `{document['status']}`",
        "",
        "This is a local-only consolidation of the non-Slavic lane/cohort gates. It records what is ready for handoff, what is blocked, and which authority/review step is next. It does not copy source passages, source-language terms, credentials, or review results.",
        "",
        "## Summary",
        "",
        f"- Lane/cohort rows: {summary['lane_or_cohort_rows']} ({summary['core_language_lanes']} core language lanes, {summary['extension_cohorts']} extension cohorts)",
        f"- Selected witnesses: {summary['selected_witnesses']} ({summary['selected_witnesses_with_source_core']} source-core-backed), missing paths: {summary['selected_witness_slots_missing_paths']}",
        f"- Inspection tasks: {summary['inspection_tasks']} ({summary['ready_context_note_tasks']} ready-note, {summary['manual_source_review_tasks']} manual/source-review, {summary['source_discovery_tasks']} source-discovery, {summary['support_cohort_tasks']} support)",
        f"- Authority forms: {summary['total_authority_packet_groups']} packet groups / {summary['total_reviewer_role_forms']} reviewer-role forms; lane-only forms: {summary['lane_reviewer_role_forms']}; methodology forms: {summary['methodology_reviewer_role_forms']}",
        f"- Planned text/TeX delta: {summary['planned_delta_shelves']} shelves / {summary['planned_text_source_like_gap_files']} text-source-like gap files / {summary['planned_delta_chunks']} planned chunks",
        "- Review fields filled: 0; packets sent: 0; external reviews: 0; accepted corrections: 0",
        "- Network actions: 0; uploads/pushes/downloads: 0",
        "",
        "## Lane Matrix",
        "",
        "| Lane/cohort | Kind | Gate | Witnesses | Tasks | Authority forms | Delta gap files | Handoff status | Next gate |",
        "|---|---:|---|---:|---:|---:|---:|---|---|",
    ]
    for row in document["lane_or_cohort_rows"]:
        lines.append(
            "| {lane} | {kind} | {gate} | {witnesses} | {tasks} | {forms} | {gap} | {status} | {next_gate} |".format(
                lane=row["lane_or_cohort"],
                kind=row["kind"],
                gate=row["edition_gate"],
                witnesses=row["selected_witnesses"],
                tasks=row["inspection_tasks"],
                forms=row["authority_reviewer_role_forms"],
                gap=row["planned_delta_text_source_like_gap_files"],
                status=row["handoff_readiness_status"],
                next_gate=row["next_gate"],
            )
        )
    methodology = document["methodology_publication_summary"]
    lines.extend(
        [
            "",
            "## Methodology Publication Lane",
            "",
            f"- Status: `{methodology['status']}`",
            f"- Working titles: {methodology['working_titles']}; case-study lanes: {methodology['case_study_lanes']}; method sections: {methodology['method_sections']}",
            f"- Claim taxonomy rows: {methodology['claim_taxonomy_rows']}; claims allowed now: {methodology['claims_allowed_now']}; claims not allowed yet: {methodology['claims_not_allowed_yet']}",
            f"- Authority queue rows: {methodology['methodology_authority_queue_rows']}; packet groups: {methodology['methodology_packet_groups']}; reviewer-role forms: {methodology['methodology_reviewer_role_forms']}",
            "- Publication completion claim: false; native/external authority review: not reviewed",
            "",
            "## Boundary Notes",
            "",
            "- Local validation here means filesystem, manifest, packet, and count consistency only.",
            "- Ready-note lanes remain blocked until page-context notes are filled and then externally reviewed.",
            "- Manual/source-review lanes remain blocked until the manual evidence rows are resolved.",
            "- Extension cohorts remain support shelves, not canonical edition lanes, until explicitly promoted and reviewed.",
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
        "- Integrated lane handoff readiness matrix: "
        f"{summary['lane_or_cohort_rows']} rows / "
        f"{summary['inspection_tasks']} inspection tasks / "
        f"{summary['total_reviewer_role_forms']} authority forms / "
        "0 network actions"
    )
    if re.search(r"^- Integrated lane handoff readiness matrix: .*", text, flags=re.MULTILINE):
        text = re.sub(r"^- Integrated lane handoff readiness matrix: .*", line, text, flags=re.MULTILINE)
    else:
        marker = "- External authority review packet forms:"
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
        "external-authority-review-queue/review-packet-forms metadata",
        "external-authority-review-queue/review-packet-forms/integrated-handoff-readiness metadata",
    )
    text = text.replace(
        "integrated-handoff-readiness/integrated-handoff-readiness metadata",
        "integrated-handoff-readiness metadata",
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
    manifest["integrated_lane_handoff_readiness_matrix"] = {
        "status": document["status"],
        "artifact_markdown": OUT_MD.name,
        "artifact_json": OUT_JSON.name,
        "lane_or_cohort_rows": summary["lane_or_cohort_rows"],
        "core_language_lanes": summary["core_language_lanes"],
        "extension_cohorts": summary["extension_cohorts"],
        "selected_witnesses": summary["selected_witnesses"],
        "selected_witnesses_with_source_core": summary["selected_witnesses_with_source_core"],
        "selected_witness_slots_missing_paths": summary["selected_witness_slots_missing_paths"],
        "inspection_tasks": summary["inspection_tasks"],
        "ready_context_note_tasks": summary["ready_context_note_tasks"],
        "manual_source_review_tasks": summary["manual_source_review_tasks"],
        "source_discovery_tasks": summary["source_discovery_tasks"],
        "support_cohort_tasks": summary["support_cohort_tasks"],
        "lane_authority_queue_rows": summary["lane_authority_queue_rows"],
        "lane_authority_packet_groups": summary["lane_authority_packet_groups"],
        "lane_reviewer_role_forms": summary["lane_reviewer_role_forms"],
        "methodology_authority_queue_rows": summary["methodology_authority_queue_rows"],
        "methodology_reviewer_role_forms": summary["methodology_reviewer_role_forms"],
        "total_authority_packet_groups": summary["total_authority_packet_groups"],
        "total_reviewer_role_forms": summary["total_reviewer_role_forms"],
        "planned_delta_shelves": summary["planned_delta_shelves"],
        "planned_text_source_like_gap_files": summary["planned_text_source_like_gap_files"],
        "planned_delta_chunks": summary["planned_delta_chunks"],
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
                "integrated_lane_handoff_readiness_matrix_json": str(OUT_JSON),
                "lane_or_cohort_rows": document["summary"]["lane_or_cohort_rows"],
                "inspection_tasks": document["summary"]["inspection_tasks"],
                "total_reviewer_role_forms": document["summary"]["total_reviewer_role_forms"],
                "planned_delta_shelves": document["summary"]["planned_delta_shelves"],
                "review_fields_filled": document["summary"]["review_fields_filled"],
                "no_network_actions_performed": document["no_network_actions_performed"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
