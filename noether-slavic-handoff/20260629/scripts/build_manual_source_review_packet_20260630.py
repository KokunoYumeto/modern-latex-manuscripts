import datetime
import hashlib
import json
import pathlib
import re
from collections import Counter, defaultdict


BASE = pathlib.Path(__file__).resolve().parents[1]
STATUS_MANIFEST = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_MANIFEST_20260629.json"
STATUS_INDEX = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_INDEX_20260629.md"
TRIAGE_JSON = BASE / "MANUAL_SOURCE_REVIEW_TRIAGE_20260630.json"
CAPTURE_FORMS_JSON = BASE / "PAGE_CONTEXT_NOTE_CAPTURE_FORMS_20260630.json"
SCAFFOLDS_JSON = BASE / "REVIEW_PACKET_SCAFFOLDS_20260629.json"
LANE_DASHBOARD_JSON = BASE / "NON_SLAVIC_LANE_GATE_DASHBOARD_20260630.json"
OUT_JSON = BASE / "MANUAL_SOURCE_REVIEW_PACKET_BLOCKED_LANES_20260630.json"
OUT_MD = BASE / "MANUAL_SOURCE_REVIEW_PACKET_BLOCKED_LANES_20260630.md"


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


def by_lane(rows: list[dict]) -> dict[str, dict]:
    return {row["lane"]: row for row in rows}


def by_term(rows: list[dict]) -> dict[str, dict]:
    return {row["term_id"]: row for row in rows}


def scaffold_by_lane(scaffolds: dict) -> dict[str, dict]:
    return by_lane(scaffolds.get("lane_scaffolds", []))


def manual_packet_row(form: dict, triage: dict) -> dict:
    return {
        "form_id": form["form_id"],
        "term_id": form["term_id"],
        "language_lane": form["language_lane"],
        "english_concept": form["english_concept"],
        "mathematical_domain": form["mathematical_domain"],
        "priority": form["priority"],
        "inspection_batch_id": form["inspection_batch_id"],
        "batch_json": triage.get("batch_json"),
        "issue_class": triage.get("issue_class"),
        "recommended_action": triage.get("recommended_action", form["recommended_action"]),
        "pages_checked": form["pages_checked"],
        "pages_with_exact_term_occurrence": form["pages_with_exact_term_occurrence"],
        "sources_checked": triage.get("sources_checked", 0),
        "cache_missing_sources": triage.get("cache_missing_sources", 0),
        "hash_mismatch_sources": triage.get("hash_mismatch_sources", 0),
        "page_status_counts": triage.get("page_status_counts", {}),
        "reviewer_question_seed": form["reviewer_question_seed"],
        "fields_to_fill": form["fields_to_fill"],
        "blank_review_values": form["blank_note_values"],
        "packet_population_status": form["packet_population_status"],
        "form_status": form["form_status"],
        "source_text_copied": False,
        "source_language_terms_copied": False,
        "native_review_status": "not_reviewed",
        "canonical_approval_status": "not_approved",
    }


def build_packet() -> dict:
    triage = load_json(TRIAGE_JSON)
    forms = load_json(CAPTURE_FORMS_JSON)
    scaffolds = load_json(SCAFFOLDS_JSON)
    dashboard = load_json(LANE_DASHBOARD_JSON)

    triage_by_id = by_term(triage["triage_items"])
    scaffold_lanes = scaffold_by_lane(scaffolds)
    manual_lanes = dashboard["gate_groups"]["manual_or_source_review_required"]
    manual_forms = [
        form
        for form in forms["capture_forms"]
        if form["language_lane"] in manual_lanes
        and form["form_status"] == "blank_manual_source_review_note_form_blocked"
        and form["term_id"] in triage_by_id
    ]

    rows_by_lane: dict[str, list[dict]] = defaultdict(list)
    for form in manual_forms:
        rows_by_lane[form["language_lane"]].append(manual_packet_row(form, triage_by_id[form["term_id"]]))

    lane_packets = []
    for lane in sorted(rows_by_lane):
        rows = sorted(rows_by_lane[lane], key=lambda row: (row["priority"], row["term_id"]))
        scaffold = scaffold_lanes.get(lane, {})
        issue_counts = Counter(row["issue_class"] for row in rows)
        priority_counts = Counter(row["priority"] for row in rows)
        lane_packets.append(
            {
                "lane": lane,
                "manual_source_review_rows": len(rows),
                "high_priority_rows": priority_counts.get("high", 0),
                "medium_priority_rows": priority_counts.get("medium", 0),
                "forms_filled": 0,
                "packet_rows_blocked": len(rows),
                "issue_class_counts": dict(sorted(issue_counts.items())),
                "required_reviewer_roles": scaffold.get("required_reviewer_roles", []),
                "priority_checks": scaffold.get("priority_checks", []),
                "blocking_concerns": scaffold.get("blocking_concerns", []),
                "lane_extra_checks": scaffold.get("lane_extra_checks", []),
                "manual_review_instruction": (
                    "Resolve the source/register/extraction issue and fill the blank review values without copying "
                    "source-language passages. Keep reviewer-packet population blocked until the row has a review note."
                ),
                "rows_to_review": rows,
            }
        )

    issue_counts = Counter()
    priority_counts = Counter()
    for packet in lane_packets:
        issue_counts.update(packet["issue_class_counts"])
        priority_counts.update(
            {
                "high": packet["high_priority_rows"],
                "medium": packet["medium_priority_rows"],
            }
        )

    return {
        "artifact": "manual_source_review_packet_blocked_lanes",
        "status": "manual_source_review_packet_not_review_result_not_packet_population",
        "generated_date": "2026-06-30",
        "generated_utc": now_utc(),
        "source_text_copied": False,
        "source_language_terms_copied": False,
        "native_review_status": "not_reviewed",
        "current_approved_terms": 0,
        "current_accepted_corrections": 0,
        "input_artifacts": {
            "triage": TRIAGE_JSON.name,
            "capture_forms": CAPTURE_FORMS_JSON.name,
            "scaffolds": SCAFFOLDS_JSON.name,
            "lane_gate_dashboard": LANE_DASHBOARD_JSON.name,
        },
        "selection_policy": {
            "included_gate": "manual_or_source_review_required",
            "included_lanes": manual_lanes,
            "ready_note_entry_lanes_excluded": True,
            "source_discovery_gap_lanes_excluded": True,
            "forms_remain_blank": True,
            "review_packet_population_performed": False,
            "source_terms_or_passages_copied": False,
        },
        "totals": {
            "lanes": len(lane_packets),
            "manual_source_review_rows": sum(packet["manual_source_review_rows"] for packet in lane_packets),
            "high_priority_rows": priority_counts.get("high", 0),
            "medium_priority_rows": priority_counts.get("medium", 0),
            "forms_filled": 0,
            "packet_rows_blocked": sum(packet["packet_rows_blocked"] for packet in lane_packets),
            "cache_missing_sources": sum(row["cache_missing_sources"] for packet in lane_packets for row in packet["rows_to_review"]),
            "hash_mismatch_sources": sum(row["hash_mismatch_sources"] for packet in lane_packets for row in packet["rows_to_review"]),
            "current_approved_terms": 0,
            "current_accepted_corrections": 0,
        },
        "issue_class_summary": dict(sorted(issue_counts.items())),
        "lane_packets": lane_packets,
        "boundaries": [
            "This packet is for manual/source review triage only.",
            "This is not native/external review and records no reviewer decision.",
            "This is not a populated reviewer packet.",
            "No source-language terms or source passages are copied here.",
            "No canonical terminology approval is implied.",
        ],
    }


def write_markdown(document: dict) -> None:
    totals = document["totals"]
    lines = [
        "# Manual/source-review packet for blocked non-Slavic lanes - 2026-06-30",
        "",
        "Status: manual/source-review work packet only. It is not native review, not a populated reviewer packet, and not a term approval ledger.",
        "",
        "## Totals",
        "",
        f"- Lanes: {totals['lanes']}",
        f"- Manual/source-review rows: {totals['manual_source_review_rows']}",
        f"- High-priority rows: {totals['high_priority_rows']}",
        f"- Medium-priority rows: {totals['medium_priority_rows']}",
        f"- Forms filled: {totals['forms_filled']}",
        f"- Packet rows blocked: {totals['packet_rows_blocked']}",
        f"- Cache-missing sources: {totals['cache_missing_sources']}",
        f"- Hash-mismatch sources: {totals['hash_mismatch_sources']}",
        "",
        "## Lane Packets",
        "",
        "| Lane | Rows | High | Medium | Blocked rows | Issue classes |",
        "| --- | ---: | ---: | ---: | ---: | --- |",
    ]
    for lane in document["lane_packets"]:
        issues = ", ".join(f"{key}: {value}" for key, value in lane["issue_class_counts"].items())
        lines.append(
            f"| {lane['lane']} | {lane['manual_source_review_rows']} | {lane['high_priority_rows']} | "
            f"{lane['medium_priority_rows']} | {lane['packet_rows_blocked']} | {issues} |"
        )
    lines.extend(
        [
            "",
            "## Required Fill Fields",
            "",
            "- `manual_source_review_note_without_source_quote`",
            "- `extraction_mismatch_resolution`",
            "- `usage_scope_note`",
            "- `reviewer_question`",
            "- `packet_population_decision`",
            "",
            "## Boundaries",
            "",
        ]
    )
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
        "- Manual/source-review work packet: "
        f"{document['totals']['manual_source_review_rows']} rows / "
        f"{document['totals']['high_priority_rows']} high / "
        f"{document['totals']['medium_priority_rows']} medium / 0 filled"
    )
    text = re.sub(r"- Manual/source-review work packet: .*", line, text)
    if line not in text:
        marker = "- Manual/source review triage:"
        rows = text.splitlines()
        for offset, row in enumerate(rows):
            if row.startswith(marker):
                rows.insert(offset + 1, line)
                text = "\n".join(rows) + "\n"
                break
    text = text.replace(
        "ready-note-entry/manual-triage",
        "ready-note-entry/manual-source-review-packet/manual-triage",
    )
    if "Generated UTC: " in text:
        old = text.split("Generated UTC: ", 1)[1].splitlines()[0]
        text = text.replace(old, manifest["generated_utc"], 1)
    STATUS_INDEX.write_text(text, encoding="utf-8")


def update_manifest(document: dict) -> None:
    manifest = load_json(STATUS_MANIFEST)
    manifest["generated_utc"] = now_utc()
    manifest["manual_source_review_packet"] = {
        "status": document["status"],
        "artifact_markdown": OUT_MD.name,
        "artifact_json": OUT_JSON.name,
        "lanes": document["totals"]["lanes"],
        "manual_source_review_rows": document["totals"]["manual_source_review_rows"],
        "high_priority_rows": document["totals"]["high_priority_rows"],
        "medium_priority_rows": document["totals"]["medium_priority_rows"],
        "forms_filled": 0,
        "packet_rows_blocked": document["totals"]["packet_rows_blocked"],
        "cache_missing_sources": document["totals"]["cache_missing_sources"],
        "hash_mismatch_sources": document["totals"]["hash_mismatch_sources"],
        "review_packet_population_performed": False,
        "source_text_copied": False,
        "source_language_terms_copied": False,
        "native_review_status": "not_reviewed",
        "current_approved_terms": 0,
        "current_accepted_corrections": 0,
    }
    upsert_artifact(manifest, "json", OUT_JSON, "manual_source_review_packet_not_review_result_not_packet_population")
    upsert_artifact(manifest, "markdown", OUT_MD)
    upsert_artifact(manifest, "scripts", pathlib.Path(__file__))
    update_status_index(document, manifest)
    write_json(STATUS_MANIFEST, manifest)


def main() -> None:
    document = build_packet()
    write_json(OUT_JSON, document)
    write_markdown(document)
    update_manifest(document)
    print(
        json.dumps(
            {
                "packet_json": str(OUT_JSON),
                "lanes": document["totals"]["lanes"],
                "manual_source_review_rows": document["totals"]["manual_source_review_rows"],
                "high_priority_rows": document["totals"]["high_priority_rows"],
                "medium_priority_rows": document["totals"]["medium_priority_rows"],
                "forms_filled": document["totals"]["forms_filled"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
