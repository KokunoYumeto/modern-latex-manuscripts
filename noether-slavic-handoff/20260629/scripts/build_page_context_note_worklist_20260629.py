import datetime
import hashlib
import json
import pathlib
import re
from collections import defaultdict


BASE = pathlib.Path(__file__).resolve().parents[1]
READINESS_JSON = BASE / "PAGE_INSPECTION_REVIEW_PACKET_READINESS_20260629.json"
STATUS_MANIFEST = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_MANIFEST_20260629.json"
STATUS_INDEX = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_INDEX_20260629.md"
OUT_JSON = BASE / "PAGE_CONTEXT_NOTE_WORKLIST_20260629.json"
OUT_MD = BASE / "PAGE_CONTEXT_NOTE_WORKLIST_20260629.md"


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
    old_status = by_path.get(rel, {}).get("status")
    by_path[rel] = artifact_item(path, status or old_status)
    manifest["artifacts"][group] = [by_path[key] for key in sorted(by_path)]


def action_for_ready(row: dict) -> str:
    return "add_human_page_context_note_then_populate_reviewer_packet_row"


def action_for_manual_review(row: dict) -> str:
    if row["language_lane"] in {"prs_AF", "arabic", "fa_IR"}:
        return "manual_source_review_plus_register_or_ocr_check_before_packet_population"
    if row["mathematical_domain"] in {"module_theory", "representation_theory", "noetherian"}:
        return "manual_source_review_for_specialist_term_before_packet_population"
    return "manual_source_review_before_packet_population"


def build_work_items(readiness: dict) -> list[dict]:
    items = []
    for row in readiness["ready_reviewer_packet_seed_rows"]:
        items.append(
            {
                "term_id": row["term_id"],
                "language_lane": row["language_lane"],
                "english_concept": row["english_concept"],
                "mathematical_domain": row["mathematical_domain"],
                "priority": row["priority"],
                "inspection_batch_id": row["inspection_batch_id"],
                "readiness_state": "ready_after_extraction_check_needs_human_page_context_note",
                "recommended_action": action_for_ready(row),
                "pages_checked": row["pages_checked"],
                "pages_with_exact_term_occurrence": row["pages_with_exact_term_occurrence"],
                "note_fields_to_fill": [
                    "human_page_context_note_without_source_quote",
                    "usage_scope_note",
                    "reviewer_question",
                    "packet_population_decision",
                ],
                "reviewer_packet_population_status": "blocked_until_human_page_context_note",
                "native_review_status": "not_reviewed",
                "canonical_approval_status": "not_approved",
            }
        )
    for row in readiness["manual_or_source_review_rows"]:
        items.append(
            {
                "term_id": row["term_id"],
                "language_lane": row["language_lane"],
                "english_concept": row["english_concept"],
                "mathematical_domain": row["mathematical_domain"],
                "priority": row["priority"],
                "inspection_batch_id": row["inspection_batch_id"],
                "readiness_state": "manual_or_source_review_required_before_reviewer_packet_row",
                "recommended_action": action_for_manual_review(row),
                "pages_checked": row["pages_checked"],
                "pages_with_exact_term_occurrence": row["pages_with_exact_term_occurrence"],
                "note_fields_to_fill": [
                    "manual_source_review_note_without_source_quote",
                    "extraction_mismatch_resolution",
                    "usage_scope_note",
                    "reviewer_question",
                    "packet_population_decision",
                ],
                "reviewer_packet_population_status": "blocked_until_manual_or_source_review",
                "native_review_status": "not_reviewed",
                "canonical_approval_status": "not_approved",
            }
        )
    return sorted(items, key=lambda item: (item["language_lane"], item["priority"], item["term_id"]))


def summarize(items: list[dict]) -> list[dict]:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for item in items:
        grouped[item["language_lane"]].append(item)
    rows = []
    for lane in sorted(grouped):
        lane_items = grouped[lane]
        ready = [item for item in lane_items if item["readiness_state"].startswith("ready_after")]
        manual = [item for item in lane_items if item["readiness_state"].startswith("manual_or_source")]
        rows.append(
            {
                "lane": lane,
                "work_items": len(lane_items),
                "human_page_context_notes": len(ready),
                "manual_or_source_review_notes": len(manual),
                "blocked_until_note": len(lane_items),
                "pages_checked": sum(item["pages_checked"] for item in lane_items),
            }
        )
    return rows


def write_markdown(worklist: dict) -> None:
    lines = [
        "# Page-context note worklist - 2026-06-29",
        "",
        "This artifact converts completed local extraction inspections into a human note worklist for reviewer-packet preparation. It is not native review, not a populated reviewer packet, and not a term approval ledger.",
        "",
        f"Companion machine-readable file: `{OUT_JSON.name}`",
        "",
        "## Totals",
        "",
        f"- Work items: {worklist['totals']['work_items']}",
        f"- Human page-context notes for extraction-ready rows: {worklist['totals']['human_page_context_notes']}",
        f"- Manual/source review notes for extraction-mismatch rows: {worklist['totals']['manual_or_source_review_notes']}",
        f"- Reviewer-packet rows still blocked until note: {worklist['totals']['blocked_until_note']}",
        "- Approved terms: 0",
        "- Accepted corrections: 0",
        "",
        "## Lane Summary",
        "",
        "| Lane | Work items | Page-context notes | Manual/source notes | Blocked until note | Pages checked |",
        "| --- | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in worklist["lane_summary"]:
        lines.append(
            f"| {row['lane']} | {row['work_items']} | {row['human_page_context_notes']} | "
            f"{row['manual_or_source_review_notes']} | {row['blocked_until_note']} | {row['pages_checked']} |"
        )
    lines.extend(
        [
            "",
            "## Manual Or Source Review Priority Rows",
            "",
            "| Term ID | Lane | English concept | Domain | Priority | Recommended action |",
            "| --- | --- | --- | --- | --- | --- |",
        ]
    )
    for item in worklist["manual_or_source_review_items"]:
        lines.append(
            f"| `{item['term_id']}` | {item['language_lane']} | {item['english_concept']} | "
            f"{item['mathematical_domain']} | {item['priority']} | {item['recommended_action']} |"
        )
    lines.extend(
        [
            "",
            "## Boundaries",
            "",
            "- No source-language term strings or source passages are copied here.",
            "- No row is populated into a reviewer packet by this worklist.",
            "- Human notes must avoid long source quotes and should cite batch/page anchors instead.",
            "- Reviewer approval and accepted-correction ingestion remain separate later stages.",
            "",
        ]
    )
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def update_status_index(worklist: dict, manifest: dict) -> None:
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
    marker = "- Review-packet readiness after extraction:"
    note_line = (
        f"- Page-context note worklist: {worklist['totals']['human_page_context_notes']} ready-row notes / "
        f"{worklist['totals']['manual_or_source_review_notes']} manual-source-review notes"
    )
    text = re.sub(r"- Page-context note worklist: .*", note_line, text)
    if note_line not in text:
        lines = text.splitlines()
        for index, line in enumerate(lines):
            if line.startswith(marker):
                lines.insert(index + 1, note_line)
                text = "\n".join(lines) + "\n"
                break
    text = text.replace(
        "page inspection queue/batch/readiness metadata",
        "page inspection queue/batch/readiness/context-note metadata",
    )
    if "Generated UTC: " in text:
        old = text.split("Generated UTC: ", 1)[1].splitlines()[0]
        text = text.replace(old, manifest["generated_utc"], 1)
    STATUS_INDEX.write_text(text, encoding="utf-8")


def update_manifest(worklist: dict) -> None:
    manifest = load_json(STATUS_MANIFEST)
    manifest["generated_utc"] = now_utc()
    manifest["page_context_note_worklist"] = {
        "status": worklist["status"],
        "artifact_markdown": OUT_MD.name,
        "artifact_json": OUT_JSON.name,
        "work_items": worklist["totals"]["work_items"],
        "human_page_context_notes": worklist["totals"]["human_page_context_notes"],
        "manual_or_source_review_notes": worklist["totals"]["manual_or_source_review_notes"],
        "blocked_until_note": worklist["totals"]["blocked_until_note"],
        "source_text_copied": False,
        "source_language_terms_copied": False,
        "native_review_status": "not_reviewed",
        "current_approved_terms": 0,
        "current_accepted_corrections": 0,
    }
    upsert_artifact(manifest, "json", OUT_JSON, "page_context_note_worklist_not_review_packet_not_approval")
    upsert_artifact(manifest, "markdown", OUT_MD)
    upsert_artifact(manifest, "scripts", pathlib.Path(__file__))
    update_status_index(worklist, manifest)
    write_json(STATUS_MANIFEST, manifest)


def main() -> None:
    readiness = load_json(READINESS_JSON)
    items = build_work_items(readiness)
    manual_items = [item for item in items if item["readiness_state"].startswith("manual_or_source")]
    ready_items = [item for item in items if item["readiness_state"].startswith("ready_after")]
    worklist = {
        "artifact": "page_context_note_worklist",
        "status": "page_context_note_worklist_not_review_packet_not_approval",
        "generated_date": "2026-06-29",
        "generated_utc": now_utc(),
        "source_text_copied": False,
        "source_language_terms_copied": False,
        "readiness_artifact": READINESS_JSON.name,
        "totals": {
            "work_items": len(items),
            "human_page_context_notes": len(ready_items),
            "manual_or_source_review_notes": len(manual_items),
            "blocked_until_note": len(items),
            "current_approved_terms": 0,
            "current_accepted_corrections": 0,
        },
        "lane_summary": summarize(items),
        "manual_or_source_review_items": manual_items,
        "human_page_context_note_items": ready_items,
        "all_work_items": items,
        "next_gates": [
            "write human page-context notes without long source quotes",
            "resolve manual/source-review mismatch rows before reviewer packet population",
            "populate reviewer-facing glossary tables only after note fields are complete",
            "send populated packets to native/external reviewers and record returns in correction ledger",
        ],
    }
    write_json(OUT_JSON, worklist)
    write_markdown(worklist)
    update_manifest(worklist)
    print(
        json.dumps(
            {
                "worklist_json": str(OUT_JSON),
                "work_items": worklist["totals"]["work_items"],
                "human_page_context_notes": worklist["totals"]["human_page_context_notes"],
                "manual_or_source_review_notes": worklist["totals"]["manual_or_source_review_notes"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
