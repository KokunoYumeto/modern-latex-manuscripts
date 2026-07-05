import datetime
import hashlib
import json
import pathlib
import re


BASE = pathlib.Path(__file__).resolve().parents[1]
STATUS_MANIFEST = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_MANIFEST_20260629.json"
STATUS_INDEX = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_INDEX_20260629.md"
RENDER_PREFLIGHT_JSON = BASE / "RENDER_SCRIPT_VALIDATION_PREFLIGHT_20260630.json"
PROMOTION_AUDIT_JSON = BASE / "CANONICAL_EDITION_PROMOTION_GATE_AUDIT_20260630.json"
OUT_JSON = BASE / "RENDER_SCRIPT_VALIDATION_EXECUTION_QUEUE_20260630.json"
OUT_MD = BASE / "RENDER_SCRIPT_VALIDATION_EXECUTION_QUEUE_20260630.md"
SELF_PATH = pathlib.Path(__file__).resolve()

STATUS = "render_script_validation_execution_queue_blocked_local_only"


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


def task_id(lane: str, task_type: str, index: int) -> str:
    return f"render-script-task-{lane.replace('_', '-')}-{task_type}-{index:02d}"


def make_task(lane_row: dict, gate_row: dict, task_type: str, check_name: str, index: int) -> dict:
    first_blocker = gate_row.get("first_blocking_gate")
    return {
        "task_id": task_id(lane_row["lane_or_cohort"], task_type, index),
        "lane_or_cohort": lane_row["lane_or_cohort"],
        "kind": lane_row["kind"],
        "label": lane_row["label"],
        "task_type": task_type,
        "check_name": check_name,
        "render_script_profile": lane_row["render_script_profile"],
        "writing_direction": lane_row["writing_direction"],
        "first_blocking_gate": first_blocker,
        "execution_state": "blocked_not_started",
        "blocked_until": first_blocker,
        "execution_allowed_now": False,
        "expected_evidence_after_execution": [
            "render_or_script_validation_record",
            "artifact_hash_or_log_pointer",
            "visual_or_script_reviewer_scope_when_required",
        ],
        "source_artifacts": [
            "RENDER_SCRIPT_VALIDATION_PREFLIGHT_20260630.json",
            "CANONICAL_EDITION_PROMOTION_GATE_AUDIT_20260630.json",
        ],
        "render_job_started": False,
        "pdf_created": False,
        "visual_inspection_completed": False,
        "script_sidecar_validation_completed": False,
        "review_packet_population_performed": False,
        "external_review_performed": False,
        "accepted_correction_ingested": False,
        "source_text_copied": False,
        "source_language_terms_copied": False,
        "native_review_status": "not_reviewed",
        "canonical_approval_status": "not_approved",
        "canonical_completion_claim": False,
        "publication_completion_claim": False,
    }


def build_document() -> dict:
    manifest = load_json(STATUS_MANIFEST)
    render = load_json(RENDER_PREFLIGHT_JSON)
    promotion = load_json(PROMOTION_AUDIT_JSON)
    gate_by_lane = {row["lane_or_cohort"]: row for row in promotion["edition_gate_rows"]}

    lane_rows = []
    task_rows = []
    for lane_row in render["preflight_rows"]:
        gate_row = gate_by_lane[lane_row["lane_or_cohort"]]
        checks_by_type = {
            "render_check": lane_row["required_render_checks"],
            "math_layout_check": lane_row["math_layout_risks"],
            "script_governance_check": lane_row["required_script_governance_checks"],
        }
        task_counts = {name: len(values) for name, values in checks_by_type.items()}
        lane_task_rows = []
        for task_type, checks in checks_by_type.items():
            for index, check_name in enumerate(checks, start=1):
                task = make_task(lane_row, gate_row, task_type, check_name, index)
                task_rows.append(task)
                lane_task_rows.append(task["task_id"])
        lane_rows.append(
            {
                "lane_or_cohort": lane_row["lane_or_cohort"],
                "kind": lane_row["kind"],
                "label": lane_row["label"],
                "render_script_profile": lane_row["render_script_profile"],
                "writing_direction": lane_row["writing_direction"],
                "first_blocking_gate": gate_row["first_blocking_gate"],
                "execution_state": "blocked_not_started",
                "execution_allowed_now": False,
                "render_check_tasks": task_counts["render_check"],
                "math_layout_check_tasks": task_counts["math_layout_check"],
                "script_governance_check_tasks": task_counts["script_governance_check"],
                "total_task_rows": sum(task_counts.values()),
                "task_ids": lane_task_rows,
                "visual_or_script_reviewer_roles": lane_row["visual_or_script_reviewer_roles"],
                "render_jobs_started": 0,
                "pdfs_created": 0,
                "visual_inspections_completed": 0,
                "script_sidecar_validations_completed": 0,
                "review_packet_population_performed": False,
                "translation_or_revision_performed": False,
                "canonical_completion_claim": False,
                "publication_completion_claim": False,
            }
        )

    summary = {
        "lane_queue_rows": len(lane_rows),
        "task_rows": len(task_rows),
        "render_check_tasks": sum(1 for row in task_rows if row["task_type"] == "render_check"),
        "math_layout_check_tasks": sum(1 for row in task_rows if row["task_type"] == "math_layout_check"),
        "script_governance_check_tasks": sum(1 for row in task_rows if row["task_type"] == "script_governance_check"),
        "blocked_task_rows": sum(1 for row in task_rows if row["execution_state"] == "blocked_not_started"),
        "execution_allowed_now_rows": sum(1 for row in task_rows if row["execution_allowed_now"]),
        "cjk_lane_rows": render["summary"]["cjk_rows"],
        "rtl_lane_rows": render["summary"]["rtl_rows"],
        "latin_lane_rows": render["summary"]["latin_rows"],
        "cyrillic_or_sidecar_lane_rows": render["summary"]["cyrillic_or_sidecar_rows"],
        "mixed_or_tbd_lane_rows": render["summary"]["mixed_or_tbd_rows"],
        "render_jobs_started": 0,
        "pdfs_created": 0,
        "visual_inspections_completed": 0,
        "script_sidecar_validations_completed": 0,
        "review_packet_population_performed": False,
        "translation_or_revision_performed": False,
        "external_reviews_performed": 0,
        "accepted_corrections_ingested": 0,
        "network_actions_performed": 0,
        "canonical_completion_claim": False,
        "publication_completion_claim": False,
        "native_review_status": "not_reviewed",
        "current_approved_terms": 0,
        "current_accepted_corrections": 0,
    }

    return {
        "artifact": "render_script_validation_execution_queue",
        "status": STATUS,
        "generated_date": "2026-06-30",
        "generated_utc": now_utc(),
        "bandwidth_mode": "local_only_no_network_actions",
        "inputs": {
            "status_manifest": STATUS_MANIFEST.name,
            "render_script_validation_preflight": RENDER_PREFLIGHT_JSON.name,
            "canonical_edition_promotion_gate_audit": PROMOTION_AUDIT_JSON.name,
        },
        "policy": {
            "queue_only_no_render_jobs": True,
            "execution_requires_upstream_gate_clearance": True,
            "render_logs_required_before_canonical_pdf_claim": True,
            "script_sidecar_logs_required_before_sidecar_equivalence_claim": True,
            "local_queue_is_not_visual_or_native_review": True,
            "no_network_upload_or_download_performed": True,
        },
        "summary": summary,
        "lane_queue_rows": lane_rows,
        "task_rows": task_rows,
        "boundaries": [
            "This queue materializes render/script validation tasks, but executes none of them.",
            "Every task is blocked by the current canonical promotion gate audit.",
            "No TeX build, PDF render, visual inspection, sidecar validation, review packet population, or external review was performed.",
            "It copies no source-language passages and no source-language term strings.",
            "No network action was performed.",
        ],
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
        "# Render/Script Validation Execution Queue - 2026-06-30",
        "",
        "This local queue turns the render/script preflight into blocked validation work units. It is not a render log and does not execute any task.",
        "",
        "## Summary",
        "",
        f"- Lane queue rows: {summary['lane_queue_rows']}",
        f"- Task rows: {summary['task_rows']}",
        f"- Render-check tasks: {summary['render_check_tasks']}",
        f"- Math-layout-check tasks: {summary['math_layout_check_tasks']}",
        f"- Script-governance-check tasks: {summary['script_governance_check_tasks']}",
        f"- Execution allowed now: {summary['execution_allowed_now_rows']}",
        "- Render jobs started: 0",
        "- PDFs created: 0",
        "- Visual inspections completed: 0",
        "- Script-sidecar validations completed: 0",
        "- Network actions performed: 0",
        "",
        "## Lane Queue",
        "",
        "| Lane/cohort | Profile | First blocking gate | Tasks |",
        "| --- | --- | --- | --- |",
    ]
    for row in document["lane_queue_rows"]:
        lines.append(
            f"| {row['label']} | `{row['render_script_profile']}` | {row['first_blocking_gate']} | {row['total_task_rows']} |"
        )
    lines.extend(
        [
            "",
            "## Boundaries",
            "",
            "- No task in this queue is executable until upstream gate clearance is recorded.",
            "- This queue does not create PDFs or render logs.",
            "- Local queueing does not replace visual, script, native, educator, or external review.",
            "- No source text, source-language term strings, credentials, reviewer returns, or accepted corrections are copied here.",
            "- No network action was performed.",
            "",
        ]
    )
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def update_status_index(document: dict, manifest: dict) -> None:
    text = STATUS_INDEX.read_text(encoding="utf-8")
    summary = document["summary"]
    line = (
        "- Render/script validation execution queue: "
        f"{summary['task_rows']} task rows / "
        f"{summary['lane_queue_rows']} lane rows / "
        f"{summary['execution_allowed_now_rows']} runnable / 0 renders"
    )
    if re.search(r"^- Render/script validation execution queue: .*", text, flags=re.MULTILINE):
        text = re.sub(r"^- Render/script validation execution queue: .*", line, text, flags=re.MULTILINE)
    else:
        marker = "- Canonical edition promotion gate audit:"
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
        "integrated-handoff-readiness/lane-promotion-next-action/support-cohort-authority-note/render-script-preflight/canonical-promotion-gate metadata",
        "integrated-handoff-readiness/lane-promotion-next-action/support-cohort-authority-note/render-script-preflight/canonical-promotion-gate/render-script-execution-queue metadata",
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
    summary = document["summary"]
    manifest["render_script_validation_execution_queue"] = {
        "status": document["status"],
        "artifact_markdown": OUT_MD.name,
        "artifact_json": OUT_JSON.name,
        "lane_queue_rows": summary["lane_queue_rows"],
        "task_rows": summary["task_rows"],
        "render_check_tasks": summary["render_check_tasks"],
        "math_layout_check_tasks": summary["math_layout_check_tasks"],
        "script_governance_check_tasks": summary["script_governance_check_tasks"],
        "blocked_task_rows": summary["blocked_task_rows"],
        "execution_allowed_now_rows": summary["execution_allowed_now_rows"],
        "cjk_lane_rows": summary["cjk_lane_rows"],
        "rtl_lane_rows": summary["rtl_lane_rows"],
        "latin_lane_rows": summary["latin_lane_rows"],
        "cyrillic_or_sidecar_lane_rows": summary["cyrillic_or_sidecar_lane_rows"],
        "mixed_or_tbd_lane_rows": summary["mixed_or_tbd_lane_rows"],
        "render_jobs_started": 0,
        "pdfs_created": 0,
        "visual_inspections_completed": 0,
        "script_sidecar_validations_completed": 0,
        "review_packet_population_performed": False,
        "translation_or_revision_performed": False,
        "external_reviews_performed": 0,
        "accepted_corrections_ingested": 0,
        "network_actions_performed": 0,
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
    update_status_index(document, manifest)
    refresh_existing_artifact_hashes(manifest)
    write_json(STATUS_MANIFEST, manifest)


def main() -> None:
    document = build_document()
    write_json(OUT_JSON, document)
    write_markdown(document)
    update_manifest(document)
    print(
        json.dumps(
            {
                "render_script_validation_execution_queue_json": str(OUT_JSON),
                "lane_queue_rows": document["summary"]["lane_queue_rows"],
                "task_rows": document["summary"]["task_rows"],
                "execution_allowed_now_rows": document["summary"]["execution_allowed_now_rows"],
                "render_jobs_started": document["summary"]["render_jobs_started"],
                "no_network_actions_performed": document["no_network_actions_performed"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
