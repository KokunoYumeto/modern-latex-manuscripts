import datetime
import hashlib
import json
import pathlib
import re
from collections import defaultdict


BASE = pathlib.Path(__file__).resolve().parents[1]
STATUS_MANIFEST = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_MANIFEST_20260629.json"
STATUS_INDEX = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_INDEX_20260629.md"
WORKLIST_JSON = BASE / "PAGE_CONTEXT_NOTE_WORKLIST_20260629.json"
SCAFFOLDS_JSON = BASE / "REVIEW_PACKET_SCAFFOLDS_20260629.json"
TRIAGE_JSON = BASE / "MANUAL_SOURCE_REVIEW_TRIAGE_20260630.json"
OUT_JSON = BASE / "PAGE_CONTEXT_NOTE_CAPTURE_FORMS_20260630.json"
OUT_MD = BASE / "PAGE_CONTEXT_NOTE_CAPTURE_FORMS_20260630.md"


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


def scaffold_question_lookup(scaffolds: dict) -> dict[str, str]:
    lookup = {}
    for lane in scaffolds["lane_scaffolds"]:
        for row in lane["row_scaffolds"]:
            lookup[row["term_id"]] = row["reviewer_question_seed"]
    return lookup


def triage_lookup(triage: dict) -> dict[str, dict]:
    return {item["term_id"]: item for item in triage["triage_items"]}


def blank_values(fields: list[str]) -> dict:
    return {field: "" for field in fields}


def form_status(item: dict) -> str:
    if item["readiness_state"].startswith("manual_or_source"):
        return "blank_manual_source_review_note_form_blocked"
    return "blank_context_note_form_blocked"


def build_forms() -> dict:
    worklist = load_json(WORKLIST_JSON)
    scaffolds = load_json(SCAFFOLDS_JSON)
    triage = load_json(TRIAGE_JSON)
    question_by_id = scaffold_question_lookup(scaffolds)
    triage_by_id = triage_lookup(triage)
    forms = []
    for item in worklist["all_work_items"]:
        triage_item = triage_by_id.get(item["term_id"])
        fields = item["note_fields_to_fill"]
        forms.append(
            {
                "form_id": f"note-form-{item['term_id']}",
                "term_id": item["term_id"],
                "language_lane": item["language_lane"],
                "english_concept": item["english_concept"],
                "mathematical_domain": item["mathematical_domain"],
                "priority": item["priority"],
                "inspection_batch_id": item["inspection_batch_id"],
                "readiness_state": item["readiness_state"],
                "recommended_action": item["recommended_action"],
                "issue_class": triage_item["issue_class"] if triage_item else None,
                "pages_checked": item["pages_checked"],
                "pages_with_exact_term_occurrence": item["pages_with_exact_term_occurrence"],
                "reviewer_question_seed": question_by_id.get(item["term_id"], ""),
                "fields_to_fill": fields,
                "blank_note_values": blank_values(fields),
                "packet_population_status": "blocked_until_form_fields_are_filled",
                "form_status": form_status(item),
                "source_text_copied": False,
                "source_language_terms_copied": False,
                "native_review_status": "not_reviewed",
                "canonical_approval_status": "not_approved",
            }
        )
    return capture_document(forms)


def capture_document(forms: list[dict]) -> dict:
    by_lane: dict[str, list[dict]] = defaultdict(list)
    for form in forms:
        by_lane[form["language_lane"]].append(form)
    lane_summary = []
    for lane in sorted(by_lane):
        rows = by_lane[lane]
        manual = [row for row in rows if row["readiness_state"].startswith("manual_or_source")]
        ready = [row for row in rows if row["readiness_state"].startswith("ready_after")]
        lane_summary.append(
            {
                "lane": lane,
                "forms": len(rows),
                "ready_context_note_forms": len(ready),
                "manual_source_review_note_forms": len(manual),
                "packet_rows_blocked": len(rows),
                "forms_filled": 0,
            }
        )
    return {
        "artifact": "page_context_note_capture_forms",
        "status": "blank_note_capture_forms_not_review_result_not_packet_population",
        "generated_date": "2026-06-30",
        "generated_utc": now_utc(),
        "no_network_actions_performed": True,
        "credentials_or_tokens_copied": False,
        "source_text_copied": False,
        "source_language_terms_copied": False,
        "worklist_artifact": WORKLIST_JSON.name,
        "scaffold_artifact": SCAFFOLDS_JSON.name,
        "triage_artifact": TRIAGE_JSON.name,
        "totals": {
            "forms": len(forms),
            "ready_context_note_forms": sum(
                1 for form in forms if form["readiness_state"].startswith("ready_after")
            ),
            "manual_source_review_note_forms": sum(
                1 for form in forms if form["readiness_state"].startswith("manual_or_source")
            ),
            "forms_filled": 0,
            "packet_rows_blocked": len(forms),
            "current_approved_terms": 0,
            "current_accepted_corrections": 0,
        },
        "lane_summary": lane_summary,
        "capture_forms": sorted(forms, key=lambda row: (row["language_lane"], row["priority"], row["term_id"])),
        "next_gates": [
            "fill note values without copying long source passages",
            "resolve manual/source review forms before packet population",
            "populate reviewer packet rows only after required fields are filled",
            "record external reviewer returns separately in accepted-correction ledger",
        ],
    }


def write_markdown(document: dict) -> None:
    lines = [
        "# Page-context note capture forms - 2026-06-30",
        "",
        "This artifact provides blank, source-safe note capture forms for rows blocked before reviewer-packet population. It is not native review, not a populated packet, and not a term approval ledger.",
        "",
        f"Companion machine-readable file: `{OUT_JSON.name}`",
        "",
        "## Totals",
        "",
        f"- Forms: {document['totals']['forms']}",
        f"- Ready context-note forms: {document['totals']['ready_context_note_forms']}",
        f"- Manual/source-review note forms: {document['totals']['manual_source_review_note_forms']}",
        f"- Forms filled: {document['totals']['forms_filled']}",
        f"- Packet rows blocked: {document['totals']['packet_rows_blocked']}",
        "- Approved terms: 0",
        "- Accepted corrections: 0",
        "",
        "## Lane Summary",
        "",
        "| Lane | Forms | Ready-note forms | Manual/source forms | Filled | Blocked packet rows |",
        "| --- | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in document["lane_summary"]:
        lines.append(
            f"| {row['lane']} | {row['forms']} | {row['ready_context_note_forms']} | "
            f"{row['manual_source_review_note_forms']} | {row['forms_filled']} | {row['packet_rows_blocked']} |"
        )
    lines.extend(
        [
            "",
            "## Capture Columns",
            "",
            "- `form_id`",
            "- `term_id`",
            "- `language_lane`",
            "- `english_concept`",
            "- `mathematical_domain`",
            "- `readiness_state`",
            "- `issue_class` when present",
            "- `reviewer_question_seed`",
            "- `blank_note_values`",
            "- `packet_population_status`",
            "",
            "## Boundaries",
            "",
            "- No source-language term strings or source passages are copied here.",
            "- No credentials or tokens are copied here.",
            "- No network action, GitHub upload, or reviewer send is performed here.",
            "- All note values are blank; no human/context review has been performed.",
            "- Packet rows remain blocked until required note values are filled.",
            "- No reviewer decision or canonical approval is implied.",
            "",
        ]
    )
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
        f"- Page-context note capture forms: {document['totals']['forms']} blank forms / "
        f"0 filled / {document['totals']['packet_rows_blocked']} blocked rows"
    )
    text = re.sub(r"- Page-context note capture forms: .*", line, text)
    if line not in text:
        marker = "- Page-context note worklist:"
        rows = text.splitlines()
        for offset, row in enumerate(rows):
            if row.startswith(marker):
                rows.insert(offset + 1, line)
                text = "\n".join(rows) + "\n"
                break
    text = text.replace(
        "page inspection queue/batch/readiness/context-note/manual-triage/reviewer-scaffold/local-handoff metadata",
        "page inspection queue/batch/readiness/context-note/capture-form/manual-triage/reviewer-scaffold/local-handoff metadata",
    )
    if "Generated UTC: " in text:
        old = text.split("Generated UTC: ", 1)[1].splitlines()[0]
        text = text.replace(old, manifest["generated_utc"], 1)
    STATUS_INDEX.write_text(text, encoding="utf-8")


def update_manifest(document: dict) -> None:
    manifest = load_json(STATUS_MANIFEST)
    manifest["generated_utc"] = now_utc()
    manifest["page_context_note_capture_forms"] = {
        "status": document["status"],
        "artifact_markdown": OUT_MD.name,
        "artifact_json": OUT_JSON.name,
        "forms": document["totals"]["forms"],
        "ready_context_note_forms": document["totals"]["ready_context_note_forms"],
        "manual_source_review_note_forms": document["totals"]["manual_source_review_note_forms"],
        "forms_filled": 0,
        "packet_rows_blocked": document["totals"]["packet_rows_blocked"],
        "no_network_actions_performed": True,
        "credentials_or_tokens_copied": False,
        "source_text_copied": False,
        "source_language_terms_copied": False,
        "native_review_status": "not_reviewed",
        "current_approved_terms": 0,
        "current_accepted_corrections": 0,
    }
    upsert_artifact(manifest, "json", OUT_JSON, "blank_note_capture_forms_not_review_result_not_packet_population")
    upsert_artifact(manifest, "markdown", OUT_MD)
    upsert_artifact(manifest, "scripts", pathlib.Path(__file__))
    update_status_index(document, manifest)
    write_json(STATUS_MANIFEST, manifest)


def main() -> None:
    document = build_forms()
    write_json(OUT_JSON, document)
    write_markdown(document)
    update_manifest(document)
    print(
        json.dumps(
            {
                "capture_forms_json": str(OUT_JSON),
                "forms": document["totals"]["forms"],
                "forms_filled": document["totals"]["forms_filled"],
                "packet_rows_blocked": document["totals"]["packet_rows_blocked"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
