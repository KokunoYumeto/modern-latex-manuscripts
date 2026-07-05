import datetime
import hashlib
import json
import pathlib
import re
from collections import defaultdict


BASE = pathlib.Path(__file__).resolve().parents[1]
STATUS_MANIFEST = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_MANIFEST_20260629.json"
STATUS_INDEX = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_INDEX_20260629.md"
CAPTURE_FORMS_JSON = BASE / "PAGE_CONTEXT_NOTE_CAPTURE_FORMS_20260630.json"
LANE_DASHBOARD_JSON = BASE / "NON_SLAVIC_LANE_GATE_DASHBOARD_20260630.json"
OUT_JSON = BASE / "READY_CONTEXT_NOTE_ENTRY_PACKET_FRENCH_JAPANESE_20260630.json"
OUT_MD = BASE / "READY_CONTEXT_NOTE_ENTRY_PACKET_FRENCH_JAPANESE_20260630.md"


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


def dashboard_ready_lanes(dashboard: dict) -> list[str]:
    return dashboard["gate_groups"]["ready_for_page_context_note_entry_not_packet_population"]


def packet_form(form: dict) -> dict:
    return {
        "form_id": form["form_id"],
        "term_id": form["term_id"],
        "language_lane": form["language_lane"],
        "english_concept": form["english_concept"],
        "mathematical_domain": form["mathematical_domain"],
        "priority": form["priority"],
        "inspection_batch_id": form["inspection_batch_id"],
        "readiness_state": form["readiness_state"],
        "pages_checked": form["pages_checked"],
        "pages_with_exact_term_occurrence": form["pages_with_exact_term_occurrence"],
        "reviewer_question_seed": form["reviewer_question_seed"],
        "fields_to_fill": form["fields_to_fill"],
        "blank_note_values": form["blank_note_values"],
        "packet_population_status": form["packet_population_status"],
        "form_status": form["form_status"],
        "source_text_copied": False,
        "source_language_terms_copied": False,
        "native_review_status": "not_reviewed",
        "canonical_approval_status": "not_approved",
    }


def build_packet() -> dict:
    capture_forms = load_json(CAPTURE_FORMS_JSON)
    dashboard = load_json(LANE_DASHBOARD_JSON)
    ready_lanes = dashboard_ready_lanes(dashboard)
    allowed_forms = [
        packet_form(form)
        for form in capture_forms["capture_forms"]
        if form["language_lane"] in ready_lanes
        and form["readiness_state"].startswith("ready_after")
        and form["form_status"] == "blank_context_note_form_blocked"
        and form["issue_class"] is None
    ]
    by_lane: dict[str, list[dict]] = defaultdict(list)
    for form in allowed_forms:
        by_lane[form["language_lane"]].append(form)

    lane_packets = []
    for lane in sorted(by_lane):
        rows = sorted(by_lane[lane], key=lambda row: (row["priority"], row["term_id"]))
        lane_packets.append(
            {
                "lane": lane,
                "forms": len(rows),
                "forms_filled": 0,
                "packet_rows_blocked": len(rows),
                "ready_for_page_context_note_entry": True,
                "manual_source_review_rows_included": 0,
                "note_entry_instruction": (
                    "Fill the blank note values from inspected local evidence without copying source-language "
                    "passages or claiming term approval; reviewer-packet rows remain blocked until notes are filled."
                ),
                "forms_to_fill": rows,
            }
        )

    return {
        "artifact": "ready_context_note_entry_packet_french_japanese",
        "status": "ready_note_entry_packet_not_review_result_not_packet_population",
        "generated_date": "2026-06-30",
        "generated_utc": now_utc(),
        "source_text_copied": False,
        "source_language_terms_copied": False,
        "native_review_status": "not_reviewed",
        "current_approved_terms": 0,
        "current_accepted_corrections": 0,
        "input_artifacts": {
            "capture_forms": CAPTURE_FORMS_JSON.name,
            "lane_gate_dashboard": LANE_DASHBOARD_JSON.name,
        },
        "selection_policy": {
            "included_gate": "ready_for_page_context_note_entry_not_packet_population",
            "included_lanes": ready_lanes,
            "excluded_manual_source_review_rows": True,
            "excluded_source_discovery_gap_rows": True,
            "forms_remain_blank": True,
            "review_packet_population_performed": False,
        },
        "totals": {
            "lanes": len(lane_packets),
            "forms": len(allowed_forms),
            "forms_filled": 0,
            "packet_rows_blocked": len(allowed_forms),
            "manual_source_review_rows_included": 0,
        },
        "lane_packets": lane_packets,
        "boundaries": [
            "This packet is for page-context note entry only.",
            "This is not native/external review.",
            "This is not a populated reviewer packet.",
            "No source-language terms or source passages are copied here.",
            "No canonical terminology approval is implied.",
        ],
    }


def write_markdown(document: dict) -> None:
    totals = document["totals"]
    lines = [
        "# Ready context-note entry packet: French and Japanese - 2026-06-30",
        "",
        "Status: ready note-entry packet only. It is not native review, not a populated reviewer packet, and not a term approval ledger.",
        "",
        "## Totals",
        "",
        f"- Lanes: {totals['lanes']}",
        f"- Forms: {totals['forms']}",
        f"- Forms filled: {totals['forms_filled']}",
        f"- Packet rows blocked: {totals['packet_rows_blocked']}",
        f"- Manual/source-review rows included: {totals['manual_source_review_rows_included']}",
        "",
        "## Lane Packets",
        "",
        "| Lane | Forms | Forms filled | Blocked rows |",
        "| --- | ---: | ---: | ---: |",
    ]
    for lane in document["lane_packets"]:
        lines.append(f"| {lane['lane']} | {lane['forms']} | {lane['forms_filled']} | {lane['packet_rows_blocked']} |")
    lines.extend(
        [
            "",
            "## Fill Fields",
            "",
            "- `human_page_context_note_without_source_quote`",
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
        "- Ready context-note entry packet: "
        f"{document['totals']['forms']} French/Japanese forms / "
        "0 filled / 0 manual-source-review rows included"
    )
    text = re.sub(r"- Ready context-note entry packet: .*", line, text)
    if line not in text:
        marker = "- Non-Slavic lane gate dashboard:"
        rows = text.splitlines()
        for offset, row in enumerate(rows):
            if row.startswith(marker):
                rows.insert(offset + 1, line)
                text = "\n".join(rows) + "\n"
                break
    text = text.replace(
        "page inspection queue/batch/readiness/context-note/capture-form/lane-gate-dashboard/manual-triage",
        "page inspection queue/batch/readiness/context-note/capture-form/lane-gate-dashboard/ready-note-entry/manual-triage",
    )
    if "Generated UTC: " in text:
        old = text.split("Generated UTC: ", 1)[1].splitlines()[0]
        text = text.replace(old, manifest["generated_utc"], 1)
    STATUS_INDEX.write_text(text, encoding="utf-8")


def update_manifest(document: dict) -> None:
    manifest = load_json(STATUS_MANIFEST)
    manifest["generated_utc"] = now_utc()
    manifest["ready_context_note_entry_packet"] = {
        "status": document["status"],
        "artifact_markdown": OUT_MD.name,
        "artifact_json": OUT_JSON.name,
        "lanes": document["totals"]["lanes"],
        "forms": document["totals"]["forms"],
        "forms_filled": 0,
        "packet_rows_blocked": document["totals"]["packet_rows_blocked"],
        "manual_source_review_rows_included": 0,
        "review_packet_population_performed": False,
        "source_text_copied": False,
        "source_language_terms_copied": False,
        "native_review_status": "not_reviewed",
        "current_approved_terms": 0,
        "current_accepted_corrections": 0,
    }
    upsert_artifact(manifest, "json", OUT_JSON, "ready_note_entry_packet_not_review_result_not_packet_population")
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
                "forms": document["totals"]["forms"],
                "forms_filled": document["totals"]["forms_filled"],
                "manual_source_review_rows_included": document["totals"]["manual_source_review_rows_included"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
