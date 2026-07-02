import datetime
import hashlib
import json
import pathlib
import re
from collections import Counter, defaultdict


BASE = pathlib.Path(__file__).resolve().parents[1]
STATUS_MANIFEST = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_MANIFEST_20260629.json"
STATUS_INDEX = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_INDEX_20260629.md"
QUEUE_JSON = BASE / "MANUAL_SOURCE_REVIEW_RESOLUTION_DECISION_QUEUE_20260630.json"
OUT_JSON = BASE / "MANUAL_SOURCE_REVIEW_DECISION_LEDGER_TEMPLATE_20260630.json"
OUT_MD = BASE / "MANUAL_SOURCE_REVIEW_DECISION_LEDGER_TEMPLATE_20260630.md"
SELF_PATH = pathlib.Path(__file__).resolve()

STATUS = "manual_source_review_decision_ledger_template_blank_no_decisions_no_packet_population"

LEDGER_FIELDS = [
    "decision",
    "manual_source_review_note_without_source_quote",
    "extraction_or_anchor_resolution",
    "usage_scope_note",
    "reviewer_question_or_followup",
    "packet_population_decision",
    "reviewer_identity_or_role",
    "decision_date",
    "remaining_blocker",
]


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


def build_document() -> dict:
    queue = load_json(QUEUE_JSON)
    rows = []
    for item in queue.get("queue_items", []):
        rows.append(
            {
                "ledger_row_id": f"decision-ledger-{item['form_id']}",
                "source_queue_item_id": item["queue_item_id"],
                "form_id": item["form_id"],
                "term_id": item["term_id"],
                "language_lane": item["language_lane"],
                "english_concept": item["english_concept"],
                "mathematical_domain": item["mathematical_domain"],
                "priority": item["priority"],
                "issue_class": item["issue_class"],
                "recommended_action": item["recommended_action"],
                "allowed_resolution_decisions": item["allowed_resolution_decisions"],
                "required_resolution_checks": item["required_resolution_checks"],
                "suggested_reviewer_roles": item["suggested_reviewer_roles"],
                "ledger_required_fields": LEDGER_FIELDS,
                "blank_decision_values": {field: "" for field in LEDGER_FIELDS},
                "decision_status": "blank_not_recorded",
                "resolution_performed": False,
                "manual_note_filled": False,
                "review_packet_population_performed": False,
                "send_to_review_allowed": False,
                "review_return_received": False,
                "accepted_correction_ingested": False,
                "source_text_copied": False,
                "source_language_terms_copied": False,
                "native_review_status": "not_reviewed",
                "canonical_approval_status": "not_approved",
            }
        )

    by_lane = defaultdict(list)
    for row in rows:
        by_lane[row["language_lane"]].append(row)

    lane_summary = []
    for lane in sorted(by_lane):
        lane_rows = by_lane[lane]
        lane_summary.append(
            {
                "lane": lane,
                "ledger_rows": len(lane_rows),
                "blank_rows": len(lane_rows),
                "decisions_recorded": 0,
                "manual_notes_filled": 0,
                "packet_rows_populated": 0,
                "issue_class_counts": dict(sorted(Counter(row["issue_class"] for row in lane_rows).items())),
            }
        )

    return {
        "artifact": "manual_source_review_decision_ledger_template",
        "status": STATUS,
        "generated_date": "2026-06-30",
        "generated_utc": now_utc(),
        "bandwidth_mode": "local_only_no_network_actions",
        "no_network_actions_performed": True,
        "credentials_or_tokens_copied": False,
        "source_text_copied": False,
        "source_language_terms_copied": False,
        "native_review_status": "not_reviewed",
        "input_artifact": QUEUE_JSON.name,
        "ledger_policy": {
            "template_only": True,
            "decisions_are_blank": True,
            "manual_notes_are_blank": True,
            "source_quotes_allowed": False,
            "source_language_terms_allowed": False,
            "review_packet_population_performed": False,
            "canonical_approval_allowed": False,
        },
        "ledger_required_fields": LEDGER_FIELDS,
        "totals": {
            "lanes": len(lane_summary),
            "ledger_rows": len(rows),
            "blank_rows": len(rows),
            "decisions_recorded": 0,
            "manual_notes_filled": 0,
            "packet_rows_populated": 0,
            "review_returns_received": 0,
            "accepted_corrections_ingested": 0,
            "current_approved_terms": 0,
            "current_accepted_corrections": 0,
        },
        "lane_summary": lane_summary,
        "ledger_rows": rows,
        "boundaries": [
            "This is a blank decision ledger template, not a manual/source-review result.",
            "All decision and note fields remain blank.",
            "No source-language terms, source passages, credentials, or tokens are copied.",
            "No reviewer-packet population, review return, accepted correction ingestion, or canonical approval is performed.",
        ],
    }


def write_markdown(document: dict) -> None:
    totals = document["totals"]
    lines = [
        "# Manual/source-review decision ledger template - 2026-06-30",
        "",
        "Status: blank reviewer/source-review ledger template only. No decisions, notes, packet population, review returns, accepted corrections, or canonical approvals are recorded.",
        "",
        "## Totals",
        "",
        f"- Ledger rows: {totals['ledger_rows']}",
        f"- Blank rows: {totals['blank_rows']}",
        f"- Decisions recorded: {totals['decisions_recorded']}",
        f"- Manual notes filled: {totals['manual_notes_filled']}",
        f"- Packet rows populated: {totals['packet_rows_populated']}",
        "",
        "## Required Fields",
        "",
    ]
    for field in document["ledger_required_fields"]:
        lines.append(f"- `{field}`")
    lines.extend(
        [
            "",
            "## Lane Summary",
            "",
            "| Lane | Ledger rows | Blank rows | Decisions | Notes | Packet rows |",
            "| --- | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in document["lane_summary"]:
        lines.append(
            f"| {row['lane']} | {row['ledger_rows']} | {row['blank_rows']} | "
            f"{row['decisions_recorded']} | {row['manual_notes_filled']} | {row['packet_rows_populated']} |"
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
        "- Manual/source-review decision ledger template: "
        f"{document['totals']['ledger_rows']} blank rows / "
        "0 decisions / 0 notes / 0 packet rows"
    )
    if re.search(r"^- Manual/source-review decision ledger template: .*", text, flags=re.MULTILINE):
        text = re.sub(r"^- Manual/source-review decision ledger template: .*", line, text, flags=re.MULTILINE)
    else:
        rows = text.splitlines()
        inserted = False
        for offset, row in enumerate(rows):
            if row.startswith("- Manual/source-review resolution decision queue:"):
                rows.insert(offset + 1, line)
                text = "\n".join(rows) + "\n"
                inserted = True
                break
        if not inserted:
            text = text.rstrip() + "\n" + line + "\n"
    if "manual-source-decision-ledger-template" not in text:
        text = text.replace(
            "manual-source-resolution-decision/reviewer-scaffold",
            "manual-source-resolution-decision/manual-source-decision-ledger-template/reviewer-scaffold",
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
    totals = document["totals"]
    manifest["manual_source_review_decision_ledger_template"] = {
        "status": document["status"],
        "artifact_markdown": OUT_MD.name,
        "artifact_json": OUT_JSON.name,
        "lanes": totals["lanes"],
        "ledger_rows": totals["ledger_rows"],
        "blank_rows": totals["blank_rows"],
        "decisions_recorded": 0,
        "manual_notes_filled": 0,
        "packet_rows_populated": 0,
        "review_returns_received": 0,
        "accepted_corrections_ingested": 0,
        "current_approved_terms": 0,
        "current_accepted_corrections": 0,
        "no_network_actions_performed": True,
        "credentials_or_tokens_copied": False,
        "source_text_copied": False,
        "source_language_terms_copied": False,
        "native_review_status": "not_reviewed",
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
    document = build_document()
    write_json(OUT_JSON, document)
    write_markdown(document)
    update_manifest(document)
    print(
        json.dumps(
            {
                "manual_source_review_decision_ledger_template_json": str(OUT_JSON),
                "ledger_rows": document["totals"]["ledger_rows"],
                "decisions_recorded": document["totals"]["decisions_recorded"],
                "manual_notes_filled": document["totals"]["manual_notes_filled"],
                "packet_rows_populated": document["totals"]["packet_rows_populated"],
                "no_network_actions_performed": document["no_network_actions_performed"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
