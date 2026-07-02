import datetime
import hashlib
import json
import pathlib
import re
from collections import Counter, defaultdict


BASE = pathlib.Path(__file__).resolve().parents[1]
STATUS_MANIFEST = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_MANIFEST_20260629.json"
STATUS_INDEX = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_INDEX_20260629.md"
READY_PACKET_JSON = BASE / "READY_CONTEXT_NOTE_ENTRY_PACKET_FRENCH_JAPANESE_20260630.json"
DRAFT_PACKET_JSON = BASE / "CONTEXT_NOTE_DRAFT_PACKET_FRENCH_JAPANESE_20260630.json"
OUT_JSON = BASE / "CONTEXT_NOTE_CANDIDATE_FILLED_FORMS_FRENCH_JAPANESE_20260630.json"
OUT_MD = BASE / "CONTEXT_NOTE_CANDIDATE_FILLED_FORMS_FRENCH_JAPANESE_20260630.md"
SELF_PATH = pathlib.Path(__file__).resolve()

STATUS = "candidate_filled_context_notes_not_human_confirmed_not_reviewer_packet_population"
REQUIRED_NOTE_FIELDS = [
    "human_page_context_note_without_source_quote",
    "usage_scope_note",
    "reviewer_question",
    "packet_population_decision",
]


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


def flatten_ready_forms(packet: dict) -> list[dict]:
    rows = []
    for lane_packet in packet.get("lane_packets", []):
        rows.extend(lane_packet.get("forms_to_fill", []))
    return sorted(rows, key=lambda row: (row["language_lane"], row["priority"], row["term_id"]))


def build_candidate_rows(ready_packet: dict, draft_packet: dict) -> list[dict]:
    ready_by_form = {form["form_id"]: form for form in flatten_ready_forms(ready_packet)}
    draft_by_form = {row["form_id"]: row for row in draft_packet.get("draft_rows", [])}
    rows = []
    for form_id in sorted(ready_by_form, key=lambda key: (ready_by_form[key]["language_lane"], ready_by_form[key]["priority"], ready_by_form[key]["term_id"])):
        form = ready_by_form[form_id]
        draft = draft_by_form[form_id]
        note_values = {field: draft["draft_note_values"][field] for field in REQUIRED_NOTE_FIELDS}
        rows.append(
            {
                "candidate_form_id": f"candidate-filled-{form_id}",
                "source_form_id": form_id,
                "source_draft_id": draft["draft_id"],
                "term_id": form["term_id"],
                "language_lane": form["language_lane"],
                "english_concept": form["english_concept"],
                "mathematical_domain": form["mathematical_domain"],
                "priority": form["priority"],
                "inspection_batch_id": form["inspection_batch_id"],
                "pages_checked": form["pages_checked"],
                "pages_with_exact_term_occurrence": form["pages_with_exact_term_occurrence"],
                "required_note_fields": REQUIRED_NOTE_FIELDS,
                "candidate_note_values": note_values,
                "candidate_fields_filled": len([value for value in note_values.values() if value.strip()]),
                "candidate_application_status": "candidate_filled_not_human_confirmed_not_applied_to_source_forms",
                "human_confirmation_status": "not_confirmed",
                "source_capture_form_status_after_candidate": form["form_status"],
                "source_capture_form_packet_population_status_after_candidate": form["packet_population_status"],
                "next_gate": "human_confirm_candidate_notes_then_apply_or_revise_before_reviewer_packet_population",
                "review_packet_population_performed": False,
                "source_text_copied": False,
                "source_language_terms_copied": False,
                "native_review_status": "not_reviewed",
                "canonical_approval_status": "not_approved",
            }
        )
    return rows


def build_document() -> dict:
    ready_packet = load_json(READY_PACKET_JSON)
    draft_packet = load_json(DRAFT_PACKET_JSON)
    rows = build_candidate_rows(ready_packet, draft_packet)
    by_lane = defaultdict(list)
    for row in rows:
        by_lane[row["language_lane"]].append(row)
    lane_summary = []
    for lane in sorted(by_lane):
        lane_rows = by_lane[lane]
        lane_summary.append(
            {
                "lane": lane,
                "candidate_forms": len(lane_rows),
                "candidate_forms_human_confirmed": 0,
                "candidate_forms_applied_to_source_capture_forms": 0,
                "review_packet_rows_populated": 0,
                "pages_checked": sum(int(row["pages_checked"]) for row in lane_rows),
                "exact_match_page_hits": sum(int(row["pages_with_exact_term_occurrence"]) for row in lane_rows),
                "domains": dict(sorted(Counter(row["mathematical_domain"] for row in lane_rows).items())),
            }
        )

    return {
        "artifact": "context_note_candidate_filled_forms_french_japanese",
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
        "input_artifacts": {
            "ready_context_note_entry_packet": READY_PACKET_JSON.name,
            "context_note_draft_packet": DRAFT_PACKET_JSON.name,
        },
        "candidate_policy": {
            "candidate_values_are_filled_from_draft_packet": True,
            "source_capture_forms_modified": False,
            "review_packet_population_performed": False,
            "human_confirmation_required_before_application": True,
            "source_passage_copying_allowed": False,
            "source_language_term_copying_allowed": False,
            "canonical_approval_allowed": False,
            "included_lanes": ["french", "japanese"],
            "included_candidate_forms": len(rows),
        },
        "totals": {
            "lanes": len(lane_summary),
            "candidate_forms": len(rows),
            "candidate_forms_with_all_required_fields": sum(
                1 for row in rows if row["candidate_fields_filled"] == len(REQUIRED_NOTE_FIELDS)
            ),
            "candidate_forms_human_confirmed": 0,
            "candidate_forms_applied_to_source_capture_forms": 0,
            "source_forms_still_blank": len(rows),
            "review_packet_rows_populated": 0,
            "manual_source_review_rows_included": 0,
            "review_packet_population_performed": False,
            "current_approved_terms": 0,
            "current_accepted_corrections": 0,
        },
        "lane_summary": lane_summary,
        "candidate_forms": rows,
        "boundaries": [
            "Candidate note values are complete but not human-confirmed.",
            "Original capture forms remain blank and blocked.",
            "Reviewer packet population is not performed by this artifact.",
            "No source-language passages or source-language terms are copied.",
            "Native/external review and canonical approval remain required.",
        ],
    }


def write_markdown(document: dict) -> None:
    totals = document["totals"]
    lines = [
        "# Context-note candidate-filled forms: French and Japanese - 2026-06-30",
        "",
        "Status: candidate-filled note forms only. The original capture forms remain blank, no reviewer packet is populated, and no term approval is claimed.",
        "",
        "## Totals",
        "",
        f"- Candidate forms: {totals['candidate_forms']}",
        f"- Candidate forms with all required fields: {totals['candidate_forms_with_all_required_fields']}",
        f"- Human-confirmed candidate forms: {totals['candidate_forms_human_confirmed']}",
        f"- Applied to source capture forms: {totals['candidate_forms_applied_to_source_capture_forms']}",
        f"- Source forms still blank: {totals['source_forms_still_blank']}",
        f"- Reviewer packet rows populated: {totals['review_packet_rows_populated']}",
        "",
        "## Lane Summary",
        "",
        "| Lane | Candidate forms | Pages checked | Exact-match page hits | Human-confirmed | Applied | Packet rows populated |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in document["lane_summary"]:
        lines.append(
            f"| {row['lane']} | {row['candidate_forms']} | {row['pages_checked']} | "
            f"{row['exact_match_page_hits']} | {row['candidate_forms_human_confirmed']} | "
            f"{row['candidate_forms_applied_to_source_capture_forms']} | {row['review_packet_rows_populated']} |"
        )
    lines.extend(
        [
            "",
            "## Next Gate",
            "",
            "- Human-confirm candidate notes.",
            "- Apply confirmed notes or revise candidates.",
            "- Re-run packet-population preflight after confirmed application.",
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
        "- Context-note candidate-filled forms: "
        f"{document['totals']['candidate_forms']} French/Japanese candidate forms / "
        "0 human-confirmed / 0 applied / 0 reviewer-packet population"
    )
    if re.search(r"^- Context-note candidate-filled forms: .*", text, flags=re.MULTILINE):
        text = re.sub(r"^- Context-note candidate-filled forms: .*", line, text, flags=re.MULTILINE)
    else:
        marker = "- Context-note draft packet:"
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
        "ready-note-entry/context-note-draft/manual-triage",
        "ready-note-entry/context-note-draft/context-note-candidate-filled/manual-triage",
    )
    text = text.replace("context-note-candidate-filled/context-note-candidate-filled", "context-note-candidate-filled")
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
    manifest["context_note_candidate_filled_forms"] = {
        "status": document["status"],
        "artifact_markdown": OUT_MD.name,
        "artifact_json": OUT_JSON.name,
        "lanes": totals["lanes"],
        "candidate_forms": totals["candidate_forms"],
        "candidate_forms_with_all_required_fields": totals["candidate_forms_with_all_required_fields"],
        "candidate_forms_human_confirmed": 0,
        "candidate_forms_applied_to_source_capture_forms": 0,
        "source_forms_still_blank": totals["source_forms_still_blank"],
        "review_packet_rows_populated": 0,
        "manual_source_review_rows_included": 0,
        "review_packet_population_performed": False,
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
    document = build_document()
    write_json(OUT_JSON, document)
    write_markdown(document)
    update_manifest(document)
    print(
        json.dumps(
            {
                "context_note_candidate_filled_forms_json": str(OUT_JSON),
                "candidate_forms": document["totals"]["candidate_forms"],
                "candidate_forms_with_all_required_fields": document["totals"][
                    "candidate_forms_with_all_required_fields"
                ],
                "human_confirmed": document["totals"]["candidate_forms_human_confirmed"],
                "review_packet_rows_populated": document["totals"]["review_packet_rows_populated"],
                "no_network_actions_performed": document["no_network_actions_performed"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
