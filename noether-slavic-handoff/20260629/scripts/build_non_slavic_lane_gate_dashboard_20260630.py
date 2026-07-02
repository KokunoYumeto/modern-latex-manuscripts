import datetime
import hashlib
import json
import pathlib
import re
from collections import defaultdict


BASE = pathlib.Path(__file__).resolve().parents[1]
STATUS_MANIFEST = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_MANIFEST_20260629.json"
STATUS_INDEX = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_INDEX_20260629.md"
READINESS_JSON = BASE / "PAGE_INSPECTION_REVIEW_PACKET_READINESS_20260629.json"
WORKLIST_JSON = BASE / "PAGE_CONTEXT_NOTE_WORKLIST_20260629.json"
TRIAGE_JSON = BASE / "MANUAL_SOURCE_REVIEW_TRIAGE_20260630.json"
SCAFFOLDS_JSON = BASE / "REVIEW_PACKET_SCAFFOLDS_20260629.json"
CAPTURE_FORMS_JSON = BASE / "PAGE_CONTEXT_NOTE_CAPTURE_FORMS_20260630.json"
OUT_JSON = BASE / "NON_SLAVIC_LANE_GATE_DASHBOARD_20260630.json"
OUT_MD = BASE / "NON_SLAVIC_LANE_GATE_DASHBOARD_20260630.md"


LANGUAGE_LABELS = {
    "arabic": "Arabic",
    "fa_IR": "Persian/Farsi (Iran)",
    "french": "French",
    "japanese": "Japanese",
    "prs_AF": "Dari/Persian (Afghanistan)",
    "simplified_chinese": "Simplified Chinese",
    "spanish": "Spanish",
    "tg_Cyrl_TJ": "Tajik Cyrillic",
}


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


def by_lane(summary_rows: list[dict], lane_key: str = "lane") -> dict[str, dict]:
    return {row[lane_key]: row for row in summary_rows}


def triage_by_lane(triage: dict) -> dict[str, dict]:
    by_summary = by_lane(triage.get("lane_summary", []))
    empty = {
        "manual_source_review_rows": 0,
        "high_priority_rows": 0,
        "medium_priority_rows": 0,
        "pages_checked": 0,
        "issue_class_counts": {},
    }
    return defaultdict(lambda: dict(empty), by_summary)


def scaffold_by_lane(scaffolds: dict) -> dict[str, dict]:
    return by_lane(scaffolds.get("lane_scaffolds", []))


def lane_gate(lane: str, readiness: dict, worklist: dict, forms: dict, triage: dict) -> tuple[str, list[str]]:
    if lane == "tg_Cyrl_TJ":
        return (
            "source_discovery_required_before_term_queue",
            [
                "locate Tajik Cyrillic mathematical register witnesses",
                "separate Tajik standard evidence from Persian/Dari assumptions",
                "seed term anchors only after source witnesses exist",
            ],
        )
    manual = triage.get("manual_source_review_rows", 0)
    ready = readiness.get("ready_after_extraction_check", 0)
    filled = forms.get("forms_filled", 0)
    total_forms = forms.get("forms", worklist.get("work_items", 0))
    actions: list[str] = []
    if ready:
        actions.append("fill blank page-context note forms for extraction-ready rows")
    if manual:
        actions.append("resolve manual/source-review rows before reviewer-packet population")
    if total_forms and filled < total_forms:
        actions.append("keep packet rows blocked until required note fields are filled")
    if lane in {"arabic", "fa_IR", "prs_AF"} and manual:
        actions.append("perform RTL/register provenance review before proposing canonical terms")
    if lane == "arabic":
        actions.append("reinforce module/representation terminology evidence before review packet population")
    if lane == "simplified_chinese" and manual:
        actions.append("resolve specialist term-variant anchors before Section 19 continuation")
    if lane == "spanish" and manual:
        actions.append("resolve specialist algebra/invariant-theory variants before Spanish reviewer packet")
    if manual == 0 and ready == total_forms and filled == 0:
        return ("ready_for_page_context_note_entry_not_packet_population", actions)
    if manual and ready:
        return ("mixed_ready_rows_and_manual_source_review_required", actions)
    if manual and not ready:
        return ("manual_source_review_required_before_context_notes", actions)
    return ("blocked_until_page_context_notes_filled", actions)


def build_dashboard() -> dict:
    manifest = load_json(STATUS_MANIFEST)
    readiness = load_json(READINESS_JSON)
    worklist = load_json(WORKLIST_JSON)
    triage = load_json(TRIAGE_JSON)
    scaffolds = load_json(SCAFFOLDS_JSON)
    forms = load_json(CAPTURE_FORMS_JSON)

    readiness_lane = by_lane(readiness.get("lane_summary", []))
    worklist_lane = by_lane(worklist.get("lane_summary", []))
    triage_lane = triage_by_lane(triage)
    scaffold_lane = scaffold_by_lane(scaffolds)
    form_lane = by_lane(forms.get("lane_summary", []))
    manifest_lanes = manifest.get("lanes", {})

    lanes = sorted(set(readiness_lane) | set(worklist_lane) | set(form_lane) | {"tg_Cyrl_TJ"})
    lane_rows = []
    for lane in lanes:
        ready_row = readiness_lane.get(lane, {})
        work_row = worklist_lane.get(lane, {})
        triage_row = triage_lane[lane]
        scaffold_row = scaffold_lane.get(lane, {})
        form_row = form_lane.get(lane, {})
        gate, actions = lane_gate(lane, ready_row, work_row, form_row, triage_row)
        lane_rows.append(
            {
                "lane": lane,
                "label": LANGUAGE_LABELS.get(lane, lane),
                "gate_status": gate,
                "tasks": ready_row.get("tasks", 0),
                "ready_after_extraction_check": ready_row.get("ready_after_extraction_check", 0),
                "manual_or_source_review_required": ready_row.get("manual_or_source_review_required", 0),
                "page_context_note_forms": form_row.get("forms", 0),
                "forms_filled": form_row.get("forms_filled", 0),
                "packet_rows_blocked": form_row.get("packet_rows_blocked", 0),
                "pages_checked": ready_row.get("pages_checked", work_row.get("pages_checked", 0)),
                "pages_with_exact_term_occurrence": ready_row.get("pages_with_exact_term_occurrence", 0),
                "manual_triage": {
                    "rows": triage_row.get("manual_source_review_rows", 0),
                    "high_priority_rows": triage_row.get("high_priority_rows", 0),
                    "medium_priority_rows": triage_row.get("medium_priority_rows", 0),
                    "issue_class_counts": triage_row.get("issue_class_counts", {}),
                },
                "required_reviewer_roles": scaffold_row.get("required_reviewer_roles", []),
                "priority_checks": scaffold_row.get("priority_checks", []),
                "blocking_concerns": scaffold_row.get("blocking_concerns", []),
                "next_actions": actions,
                "manifest_next_gates": manifest_lanes.get(lane, {}).get("next_gates", []),
                "source_text_copied": False,
                "source_language_terms_copied": False,
                "native_review_status": "not_reviewed",
                "canonical_approval_status": "not_approved",
            }
        )

    ready_context_only = [row["lane"] for row in lane_rows if row["gate_status"] == "ready_for_page_context_note_entry_not_packet_population"]
    mixed_or_manual = [
        row["lane"]
        for row in lane_rows
        if row["gate_status"] in {"mixed_ready_rows_and_manual_source_review_required", "manual_source_review_required_before_context_notes"}
    ]
    source_discovery = [row["lane"] for row in lane_rows if row["gate_status"] == "source_discovery_required_before_term_queue"]

    return {
        "artifact": "non_slavic_lane_gate_dashboard",
        "status": "lane_gate_dashboard_not_review_packet_not_completion_claim",
        "generated_date": "2026-06-30",
        "generated_utc": now_utc(),
        "source_text_copied": False,
        "source_language_terms_copied": False,
        "native_review_status": "not_reviewed",
        "current_approved_terms": 0,
        "current_accepted_corrections": 0,
        "input_artifacts": {
            "readiness": READINESS_JSON.name,
            "worklist": WORKLIST_JSON.name,
            "manual_triage": TRIAGE_JSON.name,
            "scaffolds": SCAFFOLDS_JSON.name,
            "capture_forms": CAPTURE_FORMS_JSON.name,
        },
        "totals": {
            "lanes_tracked": len(lane_rows),
            "lanes_ready_for_page_context_note_entry": len(ready_context_only),
            "lanes_with_manual_or_source_review_required": len(mixed_or_manual),
            "lanes_requiring_source_discovery_before_term_queue": len(source_discovery),
            "tasks": readiness.get("totals", {}).get("tasks", 0),
            "ready_after_extraction_check": readiness.get("totals", {}).get("ready_after_extraction_check", 0),
            "manual_or_source_review_required": readiness.get("totals", {}).get("manual_or_source_review_required", 0),
            "capture_forms": forms.get("totals", {}).get("forms", 0),
            "forms_filled": forms.get("totals", {}).get("forms_filled", 0),
            "packet_rows_blocked": forms.get("totals", {}).get("packet_rows_blocked", 0),
        },
        "gate_groups": {
            "ready_for_page_context_note_entry_not_packet_population": ready_context_only,
            "manual_or_source_review_required": mixed_or_manual,
            "source_discovery_required_before_term_queue": source_discovery,
        },
        "lane_gates": lane_rows,
        "boundaries": [
            "This dashboard is a planning/gating artifact, not a populated review packet.",
            "No native/external reviewer acceptance is implied.",
            "No canonical terminology approval is implied.",
            "No source-language term strings or source passages are copied here.",
            "Packet population remains blocked until page-context notes and manual/source review gates are resolved.",
        ],
    }


def write_markdown(document: dict) -> None:
    totals = document["totals"]
    lines = [
        "# Non-Slavic lane gate dashboard - 2026-06-30",
        "",
        "Status: planning/gating dashboard only. This is not a populated review packet, not native review, and not a completion claim.",
        "",
        "## Totals",
        "",
        f"- Lanes tracked: {totals['lanes_tracked']}",
        f"- Ready for page-context note entry: {totals['lanes_ready_for_page_context_note_entry']}",
        f"- Lanes with manual/source review required: {totals['lanes_with_manual_or_source_review_required']}",
        f"- Source-discovery gaps before term queue: {totals['lanes_requiring_source_discovery_before_term_queue']}",
        f"- Tasks: {totals['tasks']}",
        f"- Ready after extraction check: {totals['ready_after_extraction_check']}",
        f"- Manual/source review required: {totals['manual_or_source_review_required']}",
        f"- Capture forms filled: {totals['forms_filled']}",
        f"- Packet rows blocked: {totals['packet_rows_blocked']}",
        "",
        "## Lane Gates",
        "",
        "| Lane | Gate | Ready | Manual/source | Forms filled | Blocked rows | Next action |",
        "| --- | --- | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in document["lane_gates"]:
        next_action = row["next_actions"][0] if row["next_actions"] else "hold until upstream gate changes"
        lines.append(
            f"| {row['label']} | `{row['gate_status']}` | {row['ready_after_extraction_check']} | "
            f"{row['manual_or_source_review_required']} | {row['forms_filled']} | "
            f"{row['packet_rows_blocked']} | {next_action} |"
        )
    lines.extend(["", "## Boundaries", ""])
    lines.extend(f"- {boundary}" for boundary in document["boundaries"])
    lines.append("")
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def update_status_index(document: dict, manifest: dict) -> None:
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
    line = (
        "- Non-Slavic lane gate dashboard: "
        f"{document['totals']['lanes_tracked']} lanes / "
        f"{document['totals']['lanes_ready_for_page_context_note_entry']} ready for note entry / "
        f"{document['totals']['lanes_with_manual_or_source_review_required']} manual-source-review lanes / "
        f"{document['totals']['lanes_requiring_source_discovery_before_term_queue']} source-discovery gaps"
    )
    text = re.sub(r"- Non-Slavic lane gate dashboard: .*", line, text)
    if line not in text:
        marker = "- Page-context note capture forms:"
        rows = text.splitlines()
        for offset, row in enumerate(rows):
            if row.startswith(marker):
                rows.insert(offset + 1, line)
                text = "\n".join(rows) + "\n"
                break
    text = text.replace(
        "page inspection queue/batch/readiness/context-note/capture-form/manual-triage",
        "page inspection queue/batch/readiness/context-note/capture-form/lane-gate-dashboard/manual-triage",
    )
    if "Generated UTC: " in text:
        old = text.split("Generated UTC: ", 1)[1].splitlines()[0]
        text = text.replace(old, manifest["generated_utc"], 1)
    STATUS_INDEX.write_text(text, encoding="utf-8")


def update_manifest(document: dict) -> None:
    manifest = load_json(STATUS_MANIFEST)
    manifest["generated_utc"] = now_utc()
    manifest["non_slavic_lane_gate_dashboard"] = {
        "status": document["status"],
        "artifact_markdown": OUT_MD.name,
        "artifact_json": OUT_JSON.name,
        "lanes_tracked": document["totals"]["lanes_tracked"],
        "lanes_ready_for_page_context_note_entry": document["totals"]["lanes_ready_for_page_context_note_entry"],
        "lanes_with_manual_or_source_review_required": document["totals"]["lanes_with_manual_or_source_review_required"],
        "lanes_requiring_source_discovery_before_term_queue": document["totals"]["lanes_requiring_source_discovery_before_term_queue"],
        "forms_filled": document["totals"]["forms_filled"],
        "packet_rows_blocked": document["totals"]["packet_rows_blocked"],
        "source_text_copied": False,
        "source_language_terms_copied": False,
        "native_review_status": "not_reviewed",
        "current_approved_terms": 0,
        "current_accepted_corrections": 0,
    }
    upsert_artifact(manifest, "json", OUT_JSON, "lane_gate_dashboard_not_review_packet_not_completion_claim")
    upsert_artifact(manifest, "markdown", OUT_MD)
    upsert_artifact(manifest, "scripts", pathlib.Path(__file__))
    update_status_index(document, manifest)
    write_json(STATUS_MANIFEST, manifest)


def main() -> None:
    document = build_dashboard()
    write_json(OUT_JSON, document)
    write_markdown(document)
    update_manifest(document)
    print(
        json.dumps(
            {
                "dashboard_json": str(OUT_JSON),
                "lanes_tracked": document["totals"]["lanes_tracked"],
                "ready_for_note_entry": document["totals"]["lanes_ready_for_page_context_note_entry"],
                "manual_source_review_lanes": document["totals"]["lanes_with_manual_or_source_review_required"],
                "source_discovery_gaps": document["totals"]["lanes_requiring_source_discovery_before_term_queue"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
