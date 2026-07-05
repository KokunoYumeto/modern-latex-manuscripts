import datetime
import hashlib
import json
import pathlib
import re
from collections import Counter


BASE = pathlib.Path(__file__).resolve().parents[1]
STATUS_MANIFEST = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_MANIFEST_20260629.json"
STATUS_INDEX = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_INDEX_20260629.md"
SELECTION_MATRIX_JSON = BASE / "LOCAL_SOURCE_WITNESS_SELECTION_MATRIX_20260630.json"
READY_PACKET_JSON = BASE / "READY_CONTEXT_NOTE_ENTRY_PACKET_FRENCH_JAPANESE_20260630.json"
MANUAL_PACKET_JSON = BASE / "MANUAL_SOURCE_REVIEW_PACKET_BLOCKED_LANES_20260630.json"
OUT_JSON = BASE / "SELECTED_SOURCE_WITNESS_INSPECTION_PACKET_20260630.json"
OUT_MD = BASE / "SELECTED_SOURCE_WITNESS_INSPECTION_PACKET_20260630.md"
SELF_PATH = pathlib.Path(__file__).resolve()

STATUS = "selected_source_witness_inspection_packet_no_network_no_review_no_source_passage_copy"


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


def matrix_by_lane(matrix: dict) -> dict[str, dict]:
    return {row.get("lane_or_cohort"): row for row in matrix.get("matrix_rows", [])}


def lane_packet_map(packet: dict) -> dict[str, dict]:
    return {row.get("lane"): row for row in packet.get("lane_packets", [])}


def blank_values(fields: list[str]) -> dict[str, None]:
    return {field: None for field in fields}


def witness_refs(matrix_row: dict) -> list[dict]:
    refs = []
    for witness in matrix_row.get("selected_witnesses", []):
        refs.append(
            {
                "selected_rank": witness.get("selected_rank"),
                "batch": witness.get("batch"),
                "bucket": witness.get("bucket"),
                "path": witness.get("path"),
                "candidate_status": witness.get("candidate_status"),
                "source_balance": witness.get("source_balance"),
                "source_core_included": witness.get("source_core_included"),
                "text_source_like_files": witness.get("text_source_like_files"),
                "tex_files": witness.get("tex_files"),
                "pdf_files": witness.get("pdf_files"),
                "source_core_files": witness.get("source_core_files"),
                "source_excerpt_copied": False,
                "source_text_copied": False,
                "source_language_terms_copied": False,
            }
        )
    return refs


def common_task_fields(source_row: dict, matrix_row: dict, task_kind: str, task_id: str) -> dict:
    fields = list(source_row.get("fields_to_fill") or source_row.get("note_fields_to_fill") or [])
    return {
        "task_id": task_id,
        "task_kind": task_kind,
        "task_status": "blank_not_inspected",
        "form_id": source_row.get("form_id"),
        "term_id": source_row.get("term_id"),
        "language_lane": source_row.get("language_lane"),
        "english_concept": source_row.get("english_concept"),
        "mathematical_domain": source_row.get("mathematical_domain"),
        "priority": source_row.get("priority"),
        "inspection_batch_id": source_row.get("inspection_batch_id"),
        "readiness_state": source_row.get("readiness_state"),
        "pages_checked": source_row.get("pages_checked"),
        "pages_with_exact_term_occurrence": source_row.get("pages_with_exact_term_occurrence"),
        "fields_to_fill": fields,
        "field_values_blank": blank_values(fields),
        "selected_witnesses": witness_refs(matrix_row),
        "selected_witness_count": matrix_row.get("selected_witnesses_count", 0),
        "source_gate_use": matrix_row.get("source_gate_use"),
        "next_action": matrix_row.get("next_action"),
        "authority_boundary": "selected_local_witness_inspection_task_not_review_not_approval",
        "inspection_outputs_filled": False,
        "review_packet_population_performed": False,
        "translation_or_revision_performed": False,
        "source_text_copied": False,
        "source_language_terms_copied": False,
        "native_review_status": "not_reviewed",
        "canonical_approval_status": "not_approved",
    }


def build_ready_tasks(ready_packet: dict, matrix_rows: dict[str, dict]) -> list[dict]:
    tasks = []
    for lane_packet in ready_packet.get("lane_packets", []):
        lane = lane_packet.get("lane")
        matrix_row = matrix_rows[lane]
        for form in lane_packet.get("forms_to_fill", []):
            task = common_task_fields(
                form,
                matrix_row,
                "ready_context_note_entry",
                f"ready-witness-inspection-{form.get('form_id')}",
            )
            task["ready_note_instruction"] = lane_packet.get("note_entry_instruction")
            task["manual_source_review_required_before_entry"] = False
            tasks.append(task)
    return tasks


def build_manual_tasks(manual_packet: dict, matrix_rows: dict[str, dict]) -> list[dict]:
    tasks = []
    for lane_packet in manual_packet.get("lane_packets", []):
        lane = lane_packet.get("lane")
        matrix_row = matrix_rows[lane]
        for row in lane_packet.get("rows_to_review", []):
            task = common_task_fields(
                row,
                matrix_row,
                "manual_source_review_resolution",
                f"manual-witness-inspection-{row.get('form_id')}",
            )
            task["issue_class"] = row.get("issue_class")
            task["recommended_action"] = row.get("recommended_action")
            task["required_reviewer_roles"] = lane_packet.get("required_reviewer_roles", [])
            task["priority_checks"] = lane_packet.get("priority_checks", [])
            task["lane_extra_checks"] = lane_packet.get("lane_extra_checks", [])
            task["manual_review_instruction"] = lane_packet.get("manual_review_instruction")
            task["manual_source_review_required_before_entry"] = True
            tasks.append(task)
    return tasks


def build_source_discovery_tasks(matrix_rows: dict[str, dict]) -> list[dict]:
    tasks = []
    for lane, row in sorted(matrix_rows.items()):
        if row.get("source_gate_use") != "selected_for_source_discovery_promotion":
            continue
        tasks.append(
            {
                "task_id": f"source-discovery-witness-inspection-{lane}",
                "task_kind": "source_discovery_promotion",
                "task_status": "source_discovery_not_promoted",
                "lane_or_cohort": lane,
                "label": row.get("label"),
                "source_gate_use": row.get("source_gate_use"),
                "term_anchor_rows": row.get("term_anchor_rows"),
                "selected_witnesses": witness_refs(row),
                "selected_witness_count": row.get("selected_witnesses_count", 0),
                "required_before": "any_tajik_term_anchor_queue_or_translation_revision",
                "field_values_blank": {
                    "source_language_reviewer_note_without_source_quote": None,
                    "promotion_decision": None,
                    "next_term_anchor_extraction_scope": None,
                },
                "inspection_outputs_filled": False,
                "review_packet_population_performed": False,
                "translation_or_revision_performed": False,
                "source_text_copied": False,
                "source_language_terms_copied": False,
                "native_review_status": "not_reviewed",
                "canonical_approval_status": "not_approved",
            }
        )
    return tasks


def build_support_tasks(matrix_rows: dict[str, dict]) -> list[dict]:
    tasks = []
    for lane, row in sorted(matrix_rows.items()):
        if row.get("source_gate_use") != "support_only_evidence_shelf":
            continue
        tasks.append(
            {
                "task_id": f"support-witness-inspection-{lane}",
                "task_kind": "support_cohort_authority_note",
                "task_status": "support_shelf_not_promoted",
                "lane_or_cohort": lane,
                "label": row.get("label"),
                "source_gate_use": row.get("source_gate_use"),
                "selected_witnesses": witness_refs(row),
                "selected_witness_count": row.get("selected_witnesses_count", 0),
                "required_before": "promotion_to_edition_language_lane",
                "field_values_blank": {
                    "language_family_usefulness_note": None,
                    "source_authority_note": None,
                    "educational_translation_utility_note": None,
                    "anti_colonial_open_source_ownership_note": None,
                },
                "inspection_outputs_filled": False,
                "review_packet_population_performed": False,
                "translation_or_revision_performed": False,
                "source_text_copied": False,
                "source_language_terms_copied": False,
                "native_review_status": "not_reviewed",
                "canonical_approval_status": "not_approved",
            }
        )
    return tasks


def lane_summaries(tasks: list[dict]) -> list[dict]:
    by_lane: dict[str, list[dict]] = {}
    for task in tasks:
        lane = task.get("language_lane") or task.get("lane_or_cohort")
        by_lane.setdefault(lane, []).append(task)
    rows = []
    for lane in sorted(by_lane):
        lane_tasks = by_lane[lane]
        kind_counts = Counter(task["task_kind"] for task in lane_tasks)
        witness_links = sum(task.get("selected_witness_count", 0) for task in lane_tasks)
        rows.append(
            {
                "lane_or_cohort": lane,
                "inspection_tasks": len(lane_tasks),
                "task_kind_counts": dict(sorted(kind_counts.items())),
                "witness_task_links": witness_links,
                "forms_filled": 0,
                "inspection_outputs_filled": False,
                "review_packet_population_performed": False,
                "translation_or_revision_performed": False,
                "source_text_copied": False,
                "source_language_terms_copied": False,
                "native_review_status": "not_reviewed",
            }
        )
    return rows


def build_document(manifest: dict) -> dict:
    matrix = load_json(SELECTION_MATRIX_JSON)
    ready_packet = load_json(READY_PACKET_JSON)
    manual_packet = load_json(MANUAL_PACKET_JSON)
    rows_by_lane = matrix_by_lane(matrix)
    ready_tasks = build_ready_tasks(ready_packet, rows_by_lane)
    manual_tasks = build_manual_tasks(manual_packet, rows_by_lane)
    source_discovery_tasks = build_source_discovery_tasks(rows_by_lane)
    support_tasks = build_support_tasks(rows_by_lane)
    all_tasks = ready_tasks + manual_tasks + source_discovery_tasks + support_tasks
    witness_task_links = sum(task.get("selected_witness_count", 0) for task in all_tasks)
    unique_task_lanes = sorted({task.get("language_lane") or task.get("lane_or_cohort") for task in all_tasks})
    return {
        "artifact": "selected_source_witness_inspection_packet",
        "status": STATUS,
        "generated_date": "2026-06-30",
        "generated_utc": now_utc(),
        "bandwidth_mode": "local_only_no_network_actions",
        "no_network_actions_performed": True,
        "credentials_or_tokens_copied": False,
        "source_text_copied": False,
        "source_language_terms_copied": False,
        "native_review_status": "not_reviewed",
        "current_approved_terms": 0,
        "current_accepted_corrections": 0,
        "inputs": {
            "local_source_witness_selection_matrix": SELECTION_MATRIX_JSON.name,
            "ready_context_note_entry_packet": READY_PACKET_JSON.name,
            "manual_source_review_packet": MANUAL_PACKET_JSON.name,
            "status_manifest": STATUS_MANIFEST.name,
        },
        "summary": {
            "lane_or_cohort_count": len(unique_task_lanes),
            "inspection_task_count": len(all_tasks),
            "ready_context_note_tasks": len(ready_tasks),
            "manual_source_review_tasks": len(manual_tasks),
            "source_discovery_tasks": len(source_discovery_tasks),
            "support_cohort_tasks": len(support_tasks),
            "note_or_review_rows_routed": len(ready_tasks) + len(manual_tasks),
            "witness_task_links": witness_task_links,
            "unique_selected_witness_slots_from_matrix": matrix.get("summary", {}).get("selected_witnesses", 0),
            "ready_note_entry_lanes": matrix.get("summary", {}).get("ready_note_entry_lanes", 0),
            "manual_source_review_lanes": matrix.get("summary", {}).get("manual_source_review_lanes", 0),
            "source_discovery_promotions": matrix.get("summary", {}).get("source_discovery_promotions", 0),
            "support_cohorts": matrix.get("summary", {}).get("support_cohorts", 0),
            "forms_filled": 0,
            "inspection_outputs_filled": False,
            "review_packet_population_performed": False,
            "translation_or_revision_performed": False,
            "native_review_status": "not_reviewed",
            "current_approved_terms": 0,
            "current_accepted_corrections": 0,
        },
        "lane_summaries": lane_summaries(all_tasks),
        "ready_context_note_tasks": ready_tasks,
        "manual_source_review_tasks": manual_tasks,
        "source_discovery_tasks": source_discovery_tasks,
        "support_cohort_tasks": support_tasks,
        "inspection_rules": [
            "Use selected witnesses to write page-context notes or manual review notes without source quotations.",
            "Do not populate reviewer packets until the required blank fields are filled and reviewed.",
            "Do not treat selected local witnesses as native authority or canonical terminology approval.",
            "Tajik Cyrillic remains source-discovery-only until a source-language review promotes it.",
            "Extension cohorts remain support shelves until explicit language-lane authority notes exist.",
        ],
        "boundaries": [
            "No source-language passages or source-language term strings are copied into this packet.",
            "All output fields are blank by construction.",
            "No review packet row was populated and no translation or revision was performed.",
            "No network action was performed.",
            "The active Noether multilingual goal remains open.",
        ],
    }


def write_markdown(document: dict) -> None:
    summary = document["summary"]
    lines = [
        "# Selected source-witness inspection packet - 2026-06-30",
        "",
        "Status: blank inspection packet only. No network action, review, translation, or source-passage copying was performed.",
        "",
        "## Summary",
        "",
        f"- Lane/cohort rows routed: {summary['lane_or_cohort_count']}",
        f"- Inspection tasks: {summary['inspection_task_count']}",
        f"- Ready context-note tasks: {summary['ready_context_note_tasks']}",
        f"- Manual/source-review tasks: {summary['manual_source_review_tasks']}",
        f"- Source-discovery tasks: {summary['source_discovery_tasks']}",
        f"- Support cohort tasks: {summary['support_cohort_tasks']}",
        f"- Witness-task links: {summary['witness_task_links']}",
        f"- Forms/outputs filled: {summary['forms_filled']}",
        f"- Network actions performed: `{str((not document['no_network_actions_performed'])).lower()}`",
        "",
        "## Lane Summary",
        "",
        "| Lane/cohort | Tasks | Witness links | Task kinds |",
        "| --- | ---: | ---: | --- |",
    ]
    for row in document["lane_summaries"]:
        kinds = ", ".join(f"{key}:{value}" for key, value in row["task_kind_counts"].items())
        lines.append(
            f"| `{row['lane_or_cohort']}` | {row['inspection_tasks']} | {row['witness_task_links']} | `{kinds}` |"
        )
    lines.extend(["", "## Inspection Rules", ""])
    lines.extend(f"- {rule}" for rule in document["inspection_rules"])
    lines.extend(["", "## Boundaries", ""])
    lines.extend(f"- {boundary}" for boundary in document["boundaries"])
    lines.append("")
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


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
        "- Selected source-witness inspection packet: "
        f"{summary['inspection_task_count']} blank inspection tasks / "
        f"{summary['witness_task_links']} witness-task links / "
        f"{summary['note_or_review_rows_routed']} note-or-review rows routed / "
        "0 network actions"
    )
    if re.search(r"^- Selected source-witness inspection packet: .*", text, flags=re.MULTILINE):
        text = re.sub(r"^- Selected source-witness inspection packet: .*", line, text, flags=re.MULTILINE)
    else:
        marker = "- Local source-witness selection matrix:"
        rows = text.splitlines()
        for offset, row in enumerate(rows):
            if row.startswith(marker):
                rows.insert(offset + 1, line)
                text = "\n".join(rows) + "\n"
                break
    text = text.replace(
        "local-source-evidence-shelf inventory/source-witness-shortlist/selection-matrix metadata",
        "local-source-evidence-shelf inventory/source-witness-shortlist/selection-matrix/inspection-packet metadata",
    )
    text = text.replace(
        "local-source-evidence-shelf inventory/source-witness-shortlist/selection-matrix/inspection-packet/inspection-packet metadata",
        "local-source-evidence-shelf inventory/source-witness-shortlist/selection-matrix/inspection-packet metadata",
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
    manifest["selected_source_witness_inspection_packet"] = {
        "status": document["status"],
        "artifact_markdown": OUT_MD.name,
        "artifact_json": OUT_JSON.name,
        "lane_or_cohort_count": summary["lane_or_cohort_count"],
        "inspection_task_count": summary["inspection_task_count"],
        "ready_context_note_tasks": summary["ready_context_note_tasks"],
        "manual_source_review_tasks": summary["manual_source_review_tasks"],
        "source_discovery_tasks": summary["source_discovery_tasks"],
        "support_cohort_tasks": summary["support_cohort_tasks"],
        "note_or_review_rows_routed": summary["note_or_review_rows_routed"],
        "witness_task_links": summary["witness_task_links"],
        "unique_selected_witness_slots_from_matrix": summary["unique_selected_witness_slots_from_matrix"],
        "forms_filled": 0,
        "inspection_outputs_filled": False,
        "review_packet_population_performed": False,
        "translation_or_revision_performed": False,
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
                "inspection_packet_json": str(OUT_JSON),
                "inspection_task_count": document["summary"]["inspection_task_count"],
                "ready_context_note_tasks": document["summary"]["ready_context_note_tasks"],
                "manual_source_review_tasks": document["summary"]["manual_source_review_tasks"],
                "source_discovery_tasks": document["summary"]["source_discovery_tasks"],
                "support_cohort_tasks": document["summary"]["support_cohort_tasks"],
                "witness_task_links": document["summary"]["witness_task_links"],
                "no_network_actions_performed": document["no_network_actions_performed"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
