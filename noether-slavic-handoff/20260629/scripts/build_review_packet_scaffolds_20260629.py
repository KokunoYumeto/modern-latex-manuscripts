import datetime
import hashlib
import json
import pathlib
import re
from collections import defaultdict


BASE = pathlib.Path(__file__).resolve().parents[1]
WORKLIST_JSON = BASE / "PAGE_CONTEXT_NOTE_WORKLIST_20260629.json"
PACKET_TEMPLATES_JSON = BASE / "MULTILINGUAL_REVIEW_PACKET_TEMPLATES_20260629.json"
GLOSSARY_TEMPLATES_JSON = BASE / "REVIEWER_FACING_GLOSSARY_TABLE_TEMPLATES_20260629.json"
STATUS_MANIFEST = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_MANIFEST_20260629.json"
STATUS_INDEX = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_INDEX_20260629.md"
OUT_JSON = BASE / "REVIEW_PACKET_SCAFFOLDS_20260629.json"
OUT_MD = BASE / "REVIEW_PACKET_SCAFFOLDS_20260629.md"


LANE_TO_PACKET_TEMPLATE = {
    "simplified_chinese": "simplified_chinese",
    "french": "french",
    "spanish": "spanish",
    "japanese": "japanese",
    "fa_IR": "persian_family",
    "prs_AF": "persian_family",
    "arabic": "arabic",
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
    old_status = by_path.get(rel, {}).get("status")
    by_path[rel] = artifact_item(path, status or old_status)
    manifest["artifacts"][group] = [by_path[key] for key in sorted(by_path)]


def packet_templates_by_lane(packet_templates: dict) -> dict[str, dict]:
    return {item["lane"]: item for item in packet_templates["lane_templates"]}


def glossary_templates_by_lane(glossary_templates: dict) -> dict[str, dict]:
    return {item["lane"]: item for item in glossary_templates["lane_templates"]}


def reviewer_question_seed(item: dict) -> str:
    if item["readiness_state"].startswith("manual_or_source"):
        return "Resolve the extraction mismatch or source-context uncertainty before this row is populated for external review."
    if item["mathematical_domain"] in {"noetherian", "module_theory", "representation_theory"}:
        return "After the page-context note is written, ask the reviewer to confirm mathematical scope and accepted register for this specialist concept."
    return "After the page-context note is written, ask the reviewer to confirm standard usage, mathematical scope, and educational clarity."


def build_lane_scaffold(
    lane: str,
    items: list[dict],
    packet_template_lookup: dict[str, dict],
    glossary_template_lookup: dict[str, dict],
    common_columns: list[str],
) -> dict:
    template_key = LANE_TO_PACKET_TEMPLATE.get(lane)
    packet_template = packet_template_lookup.get(template_key, {})
    glossary_template = glossary_template_lookup.get(lane, {})
    ready_items = [item for item in items if item["readiness_state"].startswith("ready_after")]
    manual_items = [item for item in items if item["readiness_state"].startswith("manual_or_source")]
    row_scaffolds = []
    for item in sorted(items, key=lambda row: (row["priority"], row["term_id"])):
        row_scaffolds.append(
            {
                "term_id": item["term_id"],
                "language_lane": item["language_lane"],
                "english_concept": item["english_concept"],
                "mathematical_domain": item["mathematical_domain"],
                "priority": item["priority"],
                "inspection_batch_id": item["inspection_batch_id"],
                "readiness_state": item["readiness_state"],
                "recommended_action": item["recommended_action"],
                "note_fields_to_fill": item["note_fields_to_fill"],
                "reviewer_packet_population_status": "blocked_until_required_notes_are_filled",
                "reviewer_question_seed": reviewer_question_seed(item),
                "reviewer_decision_state": "not_reviewed",
                "canonical_approval_status": "not_approved",
            }
        )
    return {
        "lane": lane,
        "packet_template_key": template_key,
        "status": "scaffolded_not_populated_not_review_result",
        "work_items": len(items),
        "ready_row_note_items": len(ready_items),
        "manual_or_source_review_items": len(manual_items),
        "packet_rows_populated": 0,
        "packet_rows_blocked_until_notes": len(items),
        "required_reviewer_roles": packet_template.get("required_reviewer_roles", []),
        "priority_checks": packet_template.get("priority_checks", []),
        "blocking_concerns": packet_template.get("blocking_concerns", []),
        "glossary_common_columns": common_columns,
        "lane_extra_checks": glossary_template.get("extra_checks", []),
        "row_scaffolds": row_scaffolds,
    }


def build_scaffolds() -> dict:
    worklist = load_json(WORKLIST_JSON)
    packet_templates = load_json(PACKET_TEMPLATES_JSON)
    glossary_templates = load_json(GLOSSARY_TEMPLATES_JSON)
    packet_lookup = packet_templates_by_lane(packet_templates)
    glossary_lookup = glossary_templates_by_lane(glossary_templates)
    common_columns = glossary_templates["common_columns"]
    grouped: dict[str, list[dict]] = defaultdict(list)
    for item in worklist["all_work_items"]:
        grouped[item["language_lane"]].append(item)
    lane_scaffolds = [
        build_lane_scaffold(lane, grouped[lane], packet_lookup, glossary_lookup, common_columns)
        for lane in sorted(grouped)
    ]
    return {
        "artifact": "review_packet_scaffolds",
        "status": "review_packet_scaffolds_from_context_worklist_not_populated_not_review_result",
        "generated_date": "2026-06-29",
        "generated_utc": now_utc(),
        "no_network_actions_performed": True,
        "credentials_or_tokens_copied": False,
        "source_text_copied": False,
        "source_language_terms_copied": False,
        "page_context_note_worklist": WORKLIST_JSON.name,
        "packet_template_artifact": PACKET_TEMPLATES_JSON.name,
        "glossary_template_artifact": GLOSSARY_TEMPLATES_JSON.name,
        "totals": {
            "lanes": len(lane_scaffolds),
            "work_items": sum(lane["work_items"] for lane in lane_scaffolds),
            "ready_row_note_items": sum(lane["ready_row_note_items"] for lane in lane_scaffolds),
            "manual_or_source_review_items": sum(
                lane["manual_or_source_review_items"] for lane in lane_scaffolds
            ),
            "packet_rows_populated": 0,
            "packet_rows_blocked_until_notes": sum(
                lane["packet_rows_blocked_until_notes"] for lane in lane_scaffolds
            ),
            "current_approved_terms": 0,
            "current_accepted_corrections": 0,
        },
        "lane_scaffolds": lane_scaffolds,
        "global_boundaries": [
            "not_native_review",
            "not_populated_reviewer_packet",
            "not_term_approval",
            "no_source_language_term_strings_or_passages_copied",
            "blocked_until_context_or_manual_source_notes_are_filled",
        ],
        "next_gates": [
            "fill page-context note fields without long source quotes",
            "resolve manual/source-review rows before packet population",
            "populate reviewer-facing glossary packet rows after notes exist",
            "send populated lane packets to native/external reviewers",
            "ingest accepted reviewer returns into correction ledger",
        ],
    }


def write_markdown(scaffold: dict) -> None:
    lines = [
        "# Review packet scaffolds - 2026-06-29",
        "",
        "This artifact groups the page-context note worklist into per-lane reviewer-packet scaffolds. It is not a populated review packet, not native review, and not a term approval ledger.",
        "",
        f"Companion machine-readable file: `{OUT_JSON.name}`",
        "",
        "## Totals",
        "",
        f"- Lanes scaffolded: {scaffold['totals']['lanes']}",
        f"- Work items: {scaffold['totals']['work_items']}",
        f"- Ready-row note items: {scaffold['totals']['ready_row_note_items']}",
        f"- Manual/source-review items: {scaffold['totals']['manual_or_source_review_items']}",
        f"- Packet rows populated: {scaffold['totals']['packet_rows_populated']}",
        f"- Packet rows blocked until notes: {scaffold['totals']['packet_rows_blocked_until_notes']}",
        "- Approved terms: 0",
        "- Accepted corrections: 0",
        "",
        "## Lane Summary",
        "",
        "| Lane | Work items | Ready-note items | Manual/source items | Reviewer roles | Extra checks | Status |",
        "| --- | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for lane in scaffold["lane_scaffolds"]:
        lines.append(
            f"| {lane['lane']} | {lane['work_items']} | {lane['ready_row_note_items']} | "
            f"{lane['manual_or_source_review_items']} | {len(lane['required_reviewer_roles'])} | "
            f"{len(lane['lane_extra_checks'])} | {lane['status']} |"
        )
    for lane in scaffold["lane_scaffolds"]:
        lines.extend(
            [
                "",
                f"## {lane['lane']}",
                "",
                f"- Packet template key: `{lane['packet_template_key']}`",
                f"- Required reviewer roles: {', '.join(lane['required_reviewer_roles']) or 'not specified'}",
                f"- Priority checks: {', '.join(lane['priority_checks']) or 'not specified'}",
                f"- Blocking concerns: {', '.join(lane['blocking_concerns']) or 'not specified'}",
                f"- Lane extra checks: {', '.join(lane['lane_extra_checks']) or 'not specified'}",
                "",
                "| Term ID | English concept | Domain | Priority | State | Required action |",
                "| --- | --- | --- | --- | --- | --- |",
            ]
        )
        for row in lane["row_scaffolds"]:
            lines.append(
                f"| `{row['term_id']}` | {row['english_concept']} | {row['mathematical_domain']} | "
                f"{row['priority']} | {row['readiness_state']} | {row['recommended_action']} |"
            )
    lines.extend(
        [
            "",
            "## Boundaries",
            "",
            "- No source-language term strings or source passages are copied here.",
            "- No credentials or tokens are copied here.",
            "- No network action, GitHub upload, or reviewer send is performed here.",
            "- No reviewer-packet rows are populated by this scaffold.",
            "- No native/external review result is implied.",
            "- No term is approved for canonical use.",
            "- Every row remains blocked until the required context or manual/source note is filled.",
            "",
        ]
    )
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def update_status_index(scaffold: dict, manifest: dict) -> None:
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
    scaffold_line = (
        f"- Review-packet scaffolds: {scaffold['totals']['lanes']} lanes / "
        f"{scaffold['totals']['work_items']} blocked rows / 0 populated rows"
    )
    text = re.sub(r"- Review-packet scaffolds: .*", scaffold_line, text)
    if scaffold_line not in text:
        marker = "- Page-context note worklist:"
        lines = text.splitlines()
        for index, line in enumerate(lines):
            if line.startswith(marker):
                lines.insert(index + 1, scaffold_line)
                text = "\n".join(lines) + "\n"
                break
    text = text.replace(
        "page inspection queue/batch/readiness/context-note metadata",
        "page inspection queue/batch/readiness/context-note/reviewer-scaffold metadata",
    )
    if "Generated UTC: " in text:
        old = text.split("Generated UTC: ", 1)[1].splitlines()[0]
        text = text.replace(old, manifest["generated_utc"], 1)
    STATUS_INDEX.write_text(text, encoding="utf-8")


def update_manifest(scaffold: dict) -> None:
    manifest = load_json(STATUS_MANIFEST)
    manifest["generated_utc"] = now_utc()
    manifest["review_packet_scaffolds"] = {
        "status": scaffold["status"],
        "artifact_markdown": OUT_MD.name,
        "artifact_json": OUT_JSON.name,
        "lanes": scaffold["totals"]["lanes"],
        "work_items": scaffold["totals"]["work_items"],
        "packet_rows_populated": 0,
        "packet_rows_blocked_until_notes": scaffold["totals"]["packet_rows_blocked_until_notes"],
        "no_network_actions_performed": True,
        "credentials_or_tokens_copied": False,
        "source_text_copied": False,
        "source_language_terms_copied": False,
        "native_review_status": "not_reviewed",
        "current_approved_terms": 0,
        "current_accepted_corrections": 0,
    }
    upsert_artifact(
        manifest,
        "json",
        OUT_JSON,
        "review_packet_scaffolds_not_populated_not_review_result",
    )
    upsert_artifact(manifest, "markdown", OUT_MD)
    upsert_artifact(manifest, "scripts", pathlib.Path(__file__))
    update_status_index(scaffold, manifest)
    write_json(STATUS_MANIFEST, manifest)


def main() -> None:
    scaffold = build_scaffolds()
    write_json(OUT_JSON, scaffold)
    write_markdown(scaffold)
    update_manifest(scaffold)
    print(
        json.dumps(
            {
                "scaffold_json": str(OUT_JSON),
                "lanes": scaffold["totals"]["lanes"],
                "work_items": scaffold["totals"]["work_items"],
                "blocked_rows": scaffold["totals"]["packet_rows_blocked_until_notes"],
                "populated_rows": scaffold["totals"]["packet_rows_populated"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
