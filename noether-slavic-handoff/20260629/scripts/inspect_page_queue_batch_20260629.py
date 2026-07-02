import argparse
import datetime
import hashlib
import json
import pathlib
import re
import subprocess
import unicodedata
from collections import Counter


BASE = pathlib.Path(__file__).resolve().parents[1]
QUEUE_JSON = BASE / "PAGE_INSPECTION_QUEUE_20260629.json"
QUEUE_MD = BASE / "PAGE_INSPECTION_QUEUE_20260629.md"
STATUS_MANIFEST = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_MANIFEST_20260629.json"
STATUS_INDEX = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_INDEX_20260629.md"

CACHE_ROOTS = {
    "SIMPLIFIED_CHINESE_TERM_ANCHOR_SEED_20260629.json": pathlib.Path("work/source-cache/simplified_chinese_20260629"),
    "ROMANCE_FRENCH_SPANISH_TERM_ANCHOR_SEED_20260629.json": pathlib.Path("work/source-cache/romance_fr_es_20260629"),
    "JAPANESE_TERM_ANCHOR_SEED_20260629.json": pathlib.Path("work/source-cache/japanese_20260629"),
    "PERSIAN_FAMILY_ARABIC_TERM_ANCHOR_SEED_20260629.json": pathlib.Path("work/source-cache/persian_arabic_20260629"),
}

LANE_ORDER = [
    "simplified_chinese",
    "french",
    "spanish",
    "japanese",
    "fa_IR",
    "prs_AF",
    "arabic",
    "tg_Cyrl_TJ",
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


def rel_artifact_path(path: pathlib.Path) -> str:
    return "noether-slavic-handoff/20260629/" + path.relative_to(BASE).as_posix()


def normalize_text(text: str) -> str:
    return unicodedata.normalize("NFC", text).casefold()


def text_page(pdf: pathlib.Path, page: int) -> str:
    proc = subprocess.run(
        ["pdftotext", "-enc", "UTF-8", "-f", str(page), "-l", str(page), str(pdf), "-"],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=60,
        check=False,
    )
    return proc.stdout or ""


def source_row_for_task(task: dict, source_artifact: dict) -> tuple[dict, str, int]:
    ref = task["observed_source_term_ref"]
    match = re.search(r"::(?P<basis>[^#]+)#(?P<index>\d+)$", ref)
    if not match:
        raise ValueError(f"cannot parse observed_source_term_ref: {ref}")
    basis = match.group("basis")
    row_index = int(match.group("index"))
    rows = source_artifact["aggregate_term_hits"]

    if basis.startswith("aggregate_term_hits_rows_filtered_language_"):
        language = basis.removeprefix("aggregate_term_hits_rows_filtered_language_")
        selected = [row for row in rows if row.get("language") == language]
    elif basis.startswith("aggregate_term_hits_rows_filtered_sublane_"):
        sublane = basis.removeprefix("aggregate_term_hits_rows_filtered_sublane_")
        selected = [row for row in rows if row.get("sublane") == sublane]
    elif basis == "aggregate_term_hits_row_order":
        selected = rows
    else:
        raise ValueError(f"unsupported row basis: {basis}")

    if row_index < 1 or row_index > len(selected):
        raise IndexError(f"row index {row_index} outside {basis} length {len(selected)}")
    return selected[row_index - 1], basis, row_index


def source_maps(source_artifact: dict) -> dict[str, dict]:
    return {source["id"]: source for source in source_artifact.get("sources_analyzed", [])}


def inspect_task(task: dict, source_artifacts: dict[str, dict]) -> dict:
    source_name = task["source_artifact"]
    source_artifact = source_artifacts[source_name]
    source_row, row_basis, row_index = source_row_for_task(task, source_artifact)
    term = source_row["term"]
    term_norm = normalize_text(term)
    sources_by_id = source_maps(source_artifact)
    cache_root = CACHE_ROOTS[source_name]

    source_outcomes = []
    pages_checked = 0
    pages_with_nonempty_text = 0
    pages_with_exact_term_occurrence = 0
    exact_term_occurrences_total = 0

    for ref in task.get("source_refs", []):
        source_id = ref["source_witness_id"]
        source_info = sources_by_id.get(source_id)
        pdf = cache_root / f"{source_id}.pdf"
        outcome = {
            "source_witness_id": source_id,
            "pdf_cache_present": pdf.exists(),
            "pdf_sha256": sha256(pdf) if pdf.exists() else None,
            "expected_sha256": source_info.get("local_cache_sha256") if source_info else None,
            "pdf_hash_match": bool(
                pdf.exists()
                and source_info
                and sha256(pdf) == source_info.get("local_cache_sha256")
            ),
            "pdf_bytes": pdf.stat().st_size if pdf.exists() else None,
            "expected_bytes": source_info.get("local_cache_bytes") if source_info else None,
            "pages_requested": ref.get("sample_pages", []),
            "pages_checked": 0,
            "page_outcomes": [],
        }

        if not pdf.exists():
            outcome["status"] = "local_pdf_cache_missing"
            source_outcomes.append(outcome)
            continue

        for page in ref.get("sample_pages", []):
            page_result = {"page": page}
            try:
                text = text_page(pdf, page)
            except Exception as exc:  # noqa: BLE001
                page_result.update(
                    {
                        "text_chars": 0,
                        "exact_term_occurrences": 0,
                        "status": "pdftotext_page_extraction_error",
                        "error": str(exc),
                    }
                )
                outcome["page_outcomes"].append(page_result)
                continue

            text_norm = normalize_text(text)
            occurrences = text_norm.count(term_norm)
            page_result.update(
                {
                    "text_chars": len(text),
                    "exact_term_occurrences": occurrences,
                    "status": (
                        "exact_term_reverified_in_extracted_text"
                        if occurrences
                        else (
                            "page_text_nonempty_exact_term_not_reverified"
                            if text.strip()
                            else "page_text_empty_exact_term_not_reverified"
                        )
                    ),
                }
            )
            outcome["page_outcomes"].append(page_result)
            outcome["pages_checked"] += 1
            pages_checked += 1
            exact_term_occurrences_total += occurrences
            if text.strip():
                pages_with_nonempty_text += 1
            if occurrences:
                pages_with_exact_term_occurrence += 1

        source_outcomes.append(outcome)

    source_status = (
        "exact_term_reverified_in_local_text_extraction"
        if exact_term_occurrences_total
        else "sample_pages_checked_exact_term_not_reverified"
    )
    ready = bool(exact_term_occurrences_total)
    return {
        "inspection_task_id": task["inspection_task_id"],
        "term_id": task["term_id"],
        "language_lane": task["language_lane"],
        "english_concept": task["english_concept"],
        "mathematical_domain": task["mathematical_domain"],
        "priority": task["priority"],
        "inspection_method": "local_pdf_hash_and_pdftotext_page_extraction_exact_term_check_no_source_text_copied",
        "source_artifact": source_name,
        "source_artifact_sha256": task["source_artifact_sha256"],
        "observed_source_term_ref": task["observed_source_term_ref"],
        "row_basis": row_basis,
        "source_row_index_1_based": row_index,
        "pages_checked": pages_checked,
        "pages_with_nonempty_text": pages_with_nonempty_text,
        "pages_with_exact_term_occurrence": pages_with_exact_term_occurrence,
        "exact_term_occurrences_total": exact_term_occurrences_total,
        "source_context_status_after": source_status,
        "ready_for_reviewer_packet_after_extraction_check": ready,
        "reviewer_approval_status": "not_reviewed",
        "canonical_approval_status": "not_approved",
        "source_outcomes": source_outcomes,
        "context_note_without_quote": (
            "Local cached source pages were checked and at least one exact source-term occurrence "
            "was reverified in extracted text; human page-context note still required before reviewer packet population."
            if ready
            else "Local cached source pages were checked, but the exact source-term occurrence was not reverified in extracted text; manual source review is required before reviewer packet population."
        ),
    }


def next_batch_number() -> int:
    numbers = []
    for path in BASE.glob("PAGE_INSPECTION_BATCH*_*.json"):
        match = re.search(r"BATCH(\d+)", path.name)
        if match:
            numbers.append(int(match.group(1)))
    return (max(numbers) + 1) if numbers else 1


def selected_tasks(queue: dict, priority: str, batch_size: int) -> list[dict]:
    return [
        task
        for task in queue["tasks"]
        if task.get("priority") == priority and task.get("inspection_status") == "not_started"
    ][:batch_size]


def summarize_queue(queue: dict) -> None:
    tasks = queue["tasks"]
    queue["inspection_tasks"] = len(tasks)
    queue["priority_summary"] = {
        "high": sum(1 for task in tasks if task.get("priority") == "high"),
        "medium": sum(1 for task in tasks if task.get("priority") == "medium"),
        "normal": sum(1 for task in tasks if task.get("priority") == "normal"),
    }
    lane_summaries = []
    for lane in LANE_ORDER:
        lane_tasks = [task for task in tasks if task.get("language_lane") == lane]
        lane_summaries.append(
            {
                "lane": lane,
                "tasks": len(lane_tasks),
                "high_priority": sum(1 for task in lane_tasks if task.get("priority") == "high"),
                "medium_priority": sum(1 for task in lane_tasks if task.get("priority") == "medium"),
                "normal_priority": sum(1 for task in lane_tasks if task.get("priority") == "normal"),
                "not_started": sum(1 for task in lane_tasks if task.get("inspection_status") == "not_started"),
                "completed_extraction_inspections": sum(
                    1 for task in lane_tasks if task.get("inspection_status") != "not_started"
                ),
            }
        )
    queue["lane_summaries"] = lane_summaries
    queue["current_completed_inspections"] = sum(
        1 for task in tasks if task.get("inspection_status") != "not_started"
    )
    queue["current_approved_terms"] = 0
    queue["current_accepted_corrections"] = 0


def write_queue_markdown(queue: dict) -> None:
    priority = queue["priority_summary"]
    lines = [
        "# Page inspection queue - 2026-06-29",
        "",
        "This artifact turns draft reviewer glossary index rows into concrete page-inspection tasks. It is part of the Noether multilingual review-preparation workflow.",
        "",
        "It is not an inspection result, not a populated glossary, and not a term approval ledger.",
        "",
        "Companion machine-readable file: `PAGE_INSPECTION_QUEUE_20260629.json`",
        "",
        "## Counts",
        "",
        f"- Inspection tasks: {queue['inspection_tasks']}",
        f"- Source index rows: {queue['source_index_rows']}",
        f"- Source text copied into this artifact: {str(queue['source_text_copied']).lower()}",
        f"- Completed extraction inspections: {queue['current_completed_inspections']}",
        f"- Current approved terms: {queue['current_approved_terms']}",
        f"- Current accepted corrections: {queue['current_accepted_corrections']}",
        "",
        "## Priority Summary",
        "",
        f"- High priority: {priority['high']}",
        f"- Medium priority: {priority['medium']}",
        f"- Normal priority: {priority['normal']}",
        "",
        "## Lane Summary",
        "",
        "| Lane / sublane | Tasks | High | Medium | Normal | Not started | Completed extraction inspections |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for lane in queue["lane_summaries"]:
        lines.append(
            f"| {lane['lane']} | {lane['tasks']} | {lane['high_priority']} | {lane['medium_priority']} | "
            f"{lane['normal_priority']} | {lane['not_started']} | {lane['completed_extraction_inspections']} |"
        )
    lines.extend(
        [
            "",
            "## Task Shape",
            "",
            "Each machine-readable task includes:",
            "",
            "- `inspection_task_id`",
            "- `term_id`",
            "- `language_lane` and optional `sublane_or_script`",
            "- `english_concept` and `mathematical_domain`",
            "- priority and priority reason",
            "- hashed source artifact pointer",
            "- `observed_source_term_ref` back to the draft glossary index/source artifact row",
            "- source witness IDs and sample pages",
            "- required checks and output fields to fill",
            "",
            "## Boundaries",
            "",
            "- A completed extraction inspection does not approve a term.",
            "- This queue does not copy source-language term strings.",
            "- This queue does not populate project-proposed terms.",
            "- Reviewer approval must still flow through review packets and accepted-correction ledgers.",
            "- Long source quotes must not be copied into handoff artifacts.",
            "",
            "## Immediate Next Gates",
            "",
            "- Add human page-context notes for extraction-inspected ready rows.",
            "- Manually revisit rows where exact occurrence was not reverified by extraction.",
            (
                "- Page-inspection queue is closed; build reviewer-packet rows from ready extraction checks."
                if remaining_priority(queue, "normal") == 0
                else
                "- Continue normal-priority page inspection queue."
                if remaining_priority(queue, "medium") == 0
                else "- Continue remaining medium-priority, then normal-priority, page inspection queue."
            ),
            "- Preserve the unresolved Tajik Cyrillic gap until sources exist.",
            "",
        ]
    )
    QUEUE_MD.write_text("\n".join(lines), encoding="utf-8")


def write_batch_markdown(batch: dict, path: pathlib.Path) -> None:
    scope = batch["batch_scope"]
    summary = batch["summary"]
    lines = [
        f"# Page inspection batch {batch['batch_number']:02d} - {scope['priority']} priority - 2026-06-29",
        "",
        "This artifact records a local extraction inspection batch for the Noether multilingual review-preparation workflow.",
        "",
        "It is not native review, not a populated glossary, and not a term approval ledger. It copies no source-language term strings and no source passages.",
        "",
        f"Companion machine-readable file: `{path.with_suffix('.json').name}`",
        "",
        "## Scope",
        "",
        f"- Queue artifact: `{batch['queue_artifact']}`",
        f"- Batch ID: `{batch['inspection_batch_id']}`",
        f"- Language lanes: {', '.join(scope['language_lanes'])}",
        f"- Priority: {scope['selection_rule']}",
        "- Method: local PDF hash verification plus `pdftotext` page extraction exact-term check",
        "",
        "## Summary",
        "",
        f"- Tasks inspected: {summary['tasks_inspected']}",
        f"- Pages checked: {summary['pages_checked']}",
        f"- Pages with nonempty extracted text: {summary['pages_with_nonempty_text']}",
        f"- Pages with exact source-term occurrence reverified: {summary['pages_with_exact_term_occurrence']}",
        f"- Tasks ready for reviewer-packet population after extraction check: {summary['ready_for_reviewer_packet_after_extraction_check']}",
        f"- Tasks still needing human/source review before packet population: {summary['tasks_needing_human_or_source_review']}",
        "- Approved terms: 0",
        "- Accepted corrections: 0",
        "",
        "## Records",
        "",
        "| Term ID | Lane | English concept | Domain | Pages checked | Pages with exact hit | Status after extraction check | Ready after extraction check |",
        "| --- | --- | --- | --- | ---: | ---: | --- | --- |",
    ]
    for record in batch["inspection_records"]:
        lines.append(
            f"| `{record['term_id']}` | {record['language_lane']} | {record['english_concept']} | "
            f"{record['mathematical_domain']} | {record['pages_checked']} | "
            f"{record['pages_with_exact_term_occurrence']} | {record['source_context_status_after']} | "
            f"{record['ready_for_reviewer_packet_after_extraction_check']} |"
        )
    lines.extend(
        [
            "",
            "## Boundaries",
            "",
            "- Exact-term extraction recheck is not native review.",
            "- A ready extraction check still needs a human page-context note before reviewer packet population.",
            "- No source-language term strings or source passages are copied into this handoff artifact.",
            "- No term is approved for canonical use by this batch.",
            "",
            "## Next Gates",
            "",
            "- Add human page-context notes for ready rows.",
            "- Manually revisit rows where exact occurrence was not reverified by extraction.",
            "- Continue the next open queue tier if any; when no queue tasks remain, proceed to reviewer-packet population.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def artifact_item(path: pathlib.Path, status: str | None = None) -> dict:
    item = {"path": rel_artifact_path(path), "sha256": sha256(path), "bytes": path.stat().st_size}
    if status:
        item["status"] = status
    return item


def upsert_artifact(manifest: dict, group: str, path: pathlib.Path, status: str | None = None) -> None:
    rel_path = rel_artifact_path(path)
    by_path = {item["path"]: item for item in manifest["artifacts"][group]}
    existing_status = by_path.get(rel_path, {}).get("status")
    by_path[rel_path] = artifact_item(path, status or existing_status)
    manifest["artifacts"][group] = [by_path[key] for key in sorted(by_path)]


def batch_files() -> list[pathlib.Path]:
    return sorted(BASE.glob("PAGE_INSPECTION_BATCH*.json"), key=batch_number_for_path)


def batch_number_for_path(path: pathlib.Path) -> int:
    match = re.search(r"BATCH(\d+)", path.name)
    return int(match.group(1)) if match else 0


def batch_scope_for_batch(path: pathlib.Path, batch: dict) -> dict:
    if batch.get("batch_scope"):
        return batch["batch_scope"]
    records = batch.get("inspection_records", [])
    priority = records[0].get("priority", "unknown") if records else "unknown"
    lanes = sorted({record.get("language_lane", "unknown") for record in records})
    return {
        "priority": priority,
        "selection_rule": f"legacy batch file {path.name}",
        "language_lanes": lanes,
    }


def latest_batch_number() -> int:
    numbers = [batch_number_for_path(path) for path in batch_files()]
    return max(numbers) if numbers else 0


def remaining_priority(queue: dict, priority: str) -> int:
    return sum(
        1
        for task in queue["tasks"]
        if task.get("priority") == priority and task.get("inspection_status") == "not_started"
    )


def medium_state_label(queue: dict) -> str:
    return "completed" if remaining_priority(queue, "medium") == 0 else "continued"


def normal_state_label(queue: dict) -> str:
    normal_remaining = remaining_priority(queue, "normal")
    normal_total = sum(1 for task in queue["tasks"] if task.get("priority") == "normal")
    normal_done = normal_total - normal_remaining
    if normal_remaining == 0:
        return "completed"
    if normal_done:
        return "started"
    return "not_started"


def queue_status_label(queue: dict) -> str:
    latest = latest_batch_number()
    return (
        f"inspection_queue_batches01_through{latest:02d}_high_priority_completed_"
        f"medium_{medium_state_label(queue)}_normal_{normal_state_label(queue)}_not_review_result"
    )


def update_page_batch_manifest(manifest: dict) -> None:
    paths = batch_files()
    block = {
        "status": "batches01_through%02d_recorded_high_priority_completed_medium_continued_not_native_review_not_term_approval"
        % len(paths),
        "batches": len(paths),
    }
    total_tasks = 0
    total_pages = 0
    total_ready = 0
    for path in paths:
        batch = load_json(path)
        number = batch.get("batch_number") or batch_number_for_path(path)
        prefix = f"batch{number:02d}"
        summary = batch["summary"]
        block[f"{prefix}_markdown"] = batch.get("markdown_artifact") or path.with_suffix(".md").name
        block[f"{prefix}_json"] = batch.get("json_artifact") or path.name
        block[f"{prefix}_tasks_inspected"] = summary["tasks_inspected"]
        block[f"{prefix}_pages_checked"] = summary["pages_checked"]
        block[f"{prefix}_pages_with_nonempty_text"] = summary["pages_with_nonempty_text"]
        block[f"{prefix}_pages_with_exact_term_occurrence"] = summary["pages_with_exact_term_occurrence"]
        block[f"{prefix}_tasks_ready_after_extraction_check"] = summary[
            "ready_for_reviewer_packet_after_extraction_check"
        ]
        block[f"{prefix}_tasks_needing_human_or_source_review"] = summary.get(
            "tasks_needing_human_or_source_review",
            summary["tasks_inspected"] - summary["ready_for_reviewer_packet_after_extraction_check"],
        )
        total_tasks += summary["tasks_inspected"]
        total_pages += summary["pages_checked"]
        total_ready += summary["ready_for_reviewer_packet_after_extraction_check"]
    block.update(
        {
            "total_tasks_inspected": total_tasks,
            "total_pages_checked": total_pages,
            "total_tasks_ready_after_extraction_check": total_ready,
            "source_text_copied": False,
            "source_language_terms_copied": False,
            "current_approved_terms": 0,
            "current_accepted_corrections": 0,
            "native_review_status": "not_reviewed",
        }
    )
    manifest["page_inspection_batches"] = block


def update_lane_manifest(manifest: dict, queue: dict) -> None:
    completed = {item["lane"]: item["completed_extraction_inspections"] for item in queue["lane_summaries"]}
    latest = latest_batch_number()
    medium_state = medium_state_label(queue)
    normal_state = normal_state_label(queue)
    manifest["lanes"]["simplified_chinese"]["completed_extraction_inspections"] = completed["simplified_chinese"]
    manifest["lanes"]["french_spanish"]["completed_extraction_inspections"] = completed["french"] + completed["spanish"]
    manifest["lanes"]["japanese"]["completed_extraction_inspections"] = completed["japanese"]
    manifest["lanes"]["persian_family_arabic"]["completed_extraction_inspections"] = (
        completed["fa_IR"] + completed["prs_AF"] + completed["arabic"]
    )
    manifest["lanes"]["french_spanish"][
        "status"
    ] = "validated source shelves and term-anchor seed for natural-language lanes; French/Spanish queue rows extraction-inspected across high, medium, and normal batches; not a Romance interlanguage claim"
    manifest["lanes"]["simplified_chinese"][
        "status"
    ] = "evidence_shelf_reinforced_and_term_anchor_seeded; Paper34 through Section18 checkpoint recorded; Simplified Chinese queue rows extraction-inspected across high, medium, and normal batches"
    manifest["lanes"]["japanese"][
        "status"
    ] = f"validated source shelf and term-anchor seed with strong ring/module evidence; Japanese queue rows extraction-inspected through batch{latest:02d}"
    if completed["fa_IR"] > 10:
        manifest["lanes"]["persian_family_arabic"][
            "status"
        ] = f"Persian-family/Arabic seeded queue rows extraction-inspected through batch{latest:02d}; fa_IR has manual/source-review rows; ar reinforced but still needs module/representation expansion and OCR/provenance work; tg_Cyrl_TJ unresolved"
    manifest["lanes"]["interlanguage_methodology"][
        "status"
    ] = f"publication_outline_terminology_governance_authority_frameworks_review_templates_correction_ingestion_term_id_draft_glossary_page_inspection_queue_batches01_through{latest:02d}_medium_{medium_state}_normal_{normal_state}_not_completion_claim"


def update_status_index(manifest: dict, queue: dict) -> None:
    paths = batch_files()
    batch_total = manifest["page_inspection_batches"]
    latest = latest_batch_number()
    medium_state = medium_state_label(queue)
    normal_state = normal_state_label(queue)
    high_remaining = sum(
        1 for task in queue["tasks"] if task.get("priority") == "high" and task.get("inspection_status") == "not_started"
    )
    medium_remaining = sum(
        1
        for task in queue["tasks"]
        if task.get("priority") == "medium" and task.get("inspection_status") == "not_started"
    )
    normal_remaining = sum(
        1
        for task in queue["tasks"]
        if task.get("priority") == "normal" and task.get("inspection_status") == "not_started"
    )
    current_counts = [
        "## Current Counts",
        "",
        f"- Source seed entries: {manifest['source_evidence']['source_seed_entries']}",
        "- URL validation: 20 accessible / 24 total",
        f"- Term-anchor rows: {manifest['term_anchor_totals']['total_term_anchor_rows']}",
        f"- Pages analyzed for term anchors: {manifest['source_pages_analyzed']['total_pages_analyzed_for_term_anchors']}",
        f"- JSON artifacts indexed: {len(manifest['artifacts']['json'])} plus this status manifest",
        f"- Markdown artifacts indexed: {len(manifest['artifacts']['markdown'])} plus this status index",
        f"- Reproducible scripts indexed: {len(manifest['artifacts']['scripts'])}",
        f"- Page inspection queue: {queue['inspection_tasks']} tasks, {queue['current_completed_inspections']} extraction-inspected, 69 high priority",
    ]
    for path in paths:
        batch = load_json(path)
        scope = batch_scope_for_batch(path, batch)
        lanes = ", ".join(scope["language_lanes"])
        summary = batch["summary"]
        current_counts.append(
            f"- Page inspection batch {batch.get('batch_number') or batch_number_for_path(path):02d}: {summary['tasks_inspected']} "
            f"{scope['priority']}-priority tasks across {lanes}, {summary['pages_checked']} pages checked, "
            f"{summary['ready_for_reviewer_packet_after_extraction_check']} ready after extraction check, 0 approved terms"
        )
    current_counts.extend(
        [
            f"- Page inspection batches total: {batch_total['total_tasks_inspected']} tasks, {batch_total['total_pages_checked']} pages checked, {batch_total['total_tasks_ready_after_extraction_check']} ready after extraction check",
            f"- Remaining high-priority queue tasks: {high_remaining}",
            f"- Remaining medium-priority queue tasks: {medium_remaining}",
            f"- Remaining normal-priority queue tasks: {normal_remaining}",
            "- Review packet templates seeded: 8 lane/template groups, 13 ledger fields",
            "- Term ID registry seeded: 8 ranges, 153 reserved IDs, 0 approved terms, 0 accepted corrections",
            "",
        ]
    )

    lane_lines = [
        "## Lane Status",
        "",
        "| Lane | Status | Key counts | Next gate |",
        "| --- | --- | --- | --- |",
        "| Slavic | review_ready_lane_maintained_by_prior_checkpoint_not_rebuilt_in_this_pc_branch_manifest | prior checkpoint maintained by pointer | review returns / new source corrections |",
        "| Simplified Chinese | evidence_shelf_reinforced_and_term_anchor_seeded; Paper34 through Section18 checkpoint recorded; Simplified Chinese queue rows extraction-inspected across high, medium, and normal batches | 34 term rows, 787 pages; %d extraction-inspected queue tasks | human page-context notes / Section 19 continuation plus page-inspected glossary |"
        % manifest["lanes"]["simplified_chinese"]["completed_extraction_inspections"],
        "| French/Spanish | validated source shelves and term-anchor seed for natural-language lanes; French/Spanish queue rows extraction-inspected across high, medium, and normal batches; not a Romance interlanguage claim | 46 term rows, 1283 pages; %d extraction-inspected queue tasks | page-inspected per-language glossary |"
        % manifest["lanes"]["french_spanish"]["completed_extraction_inspections"],
        "| Japanese | validated source shelf and term-anchor seed with strong ring/module evidence; Japanese queue rows extraction-inspected through batch%02d | 41 term rows, 242 pages; %d extraction-inspected queue tasks | page-inspected Japanese glossary / Noetherian phrasing inspection |"
        % (latest, manifest["lanes"]["japanese"]["completed_extraction_inspections"]),
        "| Persian-family/Arabic | Persian-family/Arabic seeded queue rows extraction-inspected through batch%02d; fa_IR has manual/source-review rows; ar reinforced but still needs module/representation expansion and OCR/provenance work; tg_Cyrl_TJ unresolved | 32 term rows, 1630 pages; %d extraction-inspected queue tasks | Tajik + Arabic module/representation reinforcement |"
        % (latest, manifest["lanes"]["persian_family_arabic"]["completed_extraction_inspections"]),
        "| Interlanguage method / research publication | publication_outline_terminology_governance_authority_frameworks_review_templates_correction_ingestion_term_id_draft_glossary_page_inspection_queue_batches01_through%02d_medium_%s_normal_%s_not_completion_claim | page inspection batches, publication outline, terminology governance, correction ledger template, lane term summaries, glossary templates, term ID registry, draft glossary indexes, authority matrix, reviewer framework, and review templates indexed | human page-context notes / populated lane packets / review-return ingestion |"
        % (latest, medium_state, normal_state),
        "",
    ]

    text = STATUS_INDEX.read_text(encoding="utf-8")
    text = re.sub(r"Head before this manifest commit: `[^`]+`", "Last successfully pushed head before local-only batch/source-core work: `db7ffc6ca62116d9f8dd8c5ba156e7e2c7c953a2`", text)
    text = text.split("## Current Counts", 1)[0] + "\n".join(current_counts) + "\n"
    text += "\n".join(lane_lines) + "\n"
    source_tail = STATUS_INDEX.read_text(encoding="utf-8").split("## Source-Core Snapshot", 1)[1]
    text += "## Source-Core Snapshot" + source_tail
    text = re.sub(
        r"Page inspection batches 01-\d+ copy no source-language term strings and no source passages\.",
        f"Page inspection batches 01-{latest:02d} copy no source-language term strings and no source passages.",
        text,
    )
    if "Generated UTC: " in text:
        old = text.split("Generated UTC: ", 1)[1].splitlines()[0]
        text = text.replace(old, manifest["generated_utc"], 1)
    STATUS_INDEX.write_text(text, encoding="utf-8")


def update_manifest_and_index(queue: dict, batch_json: pathlib.Path, batch_md: pathlib.Path) -> None:
    manifest = load_json(STATUS_MANIFEST)
    manifest["generated_utc"] = now_utc()
    queue_status = queue_status_label(queue)
    manifest["page_inspection_queue"].update(
        {
            "status": queue_status,
            "inspection_tasks": queue["inspection_tasks"],
            "high_priority": queue["priority_summary"]["high"],
            "medium_priority": queue["priority_summary"]["medium"],
            "normal_priority": queue["priority_summary"]["normal"],
            "lane_summaries": len(queue["lane_summaries"]),
            "source_text_copied": False,
            "current_completed_inspections": queue["current_completed_inspections"],
            "current_approved_terms": 0,
            "current_accepted_corrections": 0,
        }
    )
    update_lane_manifest(manifest, queue)
    update_page_batch_manifest(manifest)
    manifest["page_inspection_batches"][
        "status"
    ] = f"batches01_through{latest_batch_number():02d}_recorded_high_priority_completed_medium_{medium_state_label(queue)}_normal_{normal_state_label(queue)}_not_native_review_not_term_approval"

    upsert_artifact(
        manifest,
        "json",
        batch_json,
        "local_extraction_inspection_batch_not_native_review_not_term_approval",
    )
    upsert_artifact(manifest, "markdown", batch_md)
    upsert_artifact(manifest, "json", QUEUE_JSON, queue_status)
    upsert_artifact(manifest, "markdown", QUEUE_MD)
    upsert_artifact(manifest, "scripts", pathlib.Path(__file__))

    update_status_index(manifest, queue)

    write_json(STATUS_MANIFEST, manifest)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--priority", default="medium", choices=["high", "medium", "normal"])
    parser.add_argument("--batch-size", type=int, default=12)
    parser.add_argument("--batch-number", type=int, default=None)
    args = parser.parse_args()

    queue = load_json(QUEUE_JSON)
    batch_number = args.batch_number or next_batch_number()
    tasks = selected_tasks(queue, args.priority, args.batch_size)
    if not tasks:
        raise SystemExit(f"no not-started {args.priority} tasks available")

    source_artifacts = {name: load_json(BASE / name) for name in sorted({task["source_artifact"] for task in tasks})}
    records = []
    batch_id = f"page-inspection-batch{batch_number:02d}-{args.priority}-priority-20260629"

    for task in tasks:
        record = inspect_task(task, source_artifacts)
        record["inspection_batch_id"] = batch_id
        records.append(record)
        task["inspection_status"] = f"extraction_inspected_batch{batch_number:02d}_not_reviewed"
        task["inspection_batch_id"] = batch_id
        task["source_context_status_after"] = record["source_context_status_after"]
        task["ready_for_reviewer_packet_after_extraction_check"] = record[
            "ready_for_reviewer_packet_after_extraction_check"
        ]
        task["reviewer_approval_status"] = "not_reviewed"
        task["canonical_approval_status"] = "not_approved"

    summary = {
        "tasks_inspected": len(records),
        "ready_for_reviewer_packet_after_extraction_check": sum(
            1 for record in records if record["ready_for_reviewer_packet_after_extraction_check"]
        ),
        "exact_term_reverified": sum(1 for record in records if record["exact_term_occurrences_total"]),
        "exact_term_not_reverified": sum(1 for record in records if not record["exact_term_occurrences_total"]),
        "pages_checked": sum(record["pages_checked"] for record in records),
        "pages_with_nonempty_text": sum(record["pages_with_nonempty_text"] for record in records),
        "pages_with_exact_term_occurrence": sum(record["pages_with_exact_term_occurrence"] for record in records),
    }
    summary["tasks_needing_human_or_source_review"] = len(records) - summary[
        "ready_for_reviewer_packet_after_extraction_check"
    ]
    if summary["pages_checked"] == 0:
        raise SystemExit(
            "selected batch produced zero checked pages; verify CACHE_ROOTS before updating queue artifacts"
        )

    lanes = sorted({record["language_lane"] for record in records})
    batch_json = BASE / f"PAGE_INSPECTION_BATCH{batch_number:02d}_{args.priority.upper()}_PRIORITY_20260629.json"
    batch_md = batch_json.with_suffix(".md")
    batch = {
        "artifact": f"page_inspection_batch{batch_number:02d}_{args.priority}_priority",
        "status": "local_extraction_inspection_batch_not_native_review_not_term_approval",
        "purpose": "Record a local extraction inspection batch for Noether multilingual glossary rows.",
        "generated_date": "2026-06-29",
        "generated_utc": now_utc(),
        "batch_number": batch_number,
        "inspection_batch_id": batch_id,
        "queue_artifact": QUEUE_JSON.name,
        "json_artifact": batch_json.name,
        "markdown_artifact": batch_md.name,
        "batch_scope": {
            "priority": args.priority,
            "selection_rule": f"first {len(records)} not-started {args.priority}-priority queue tasks",
            "language_lanes": lanes,
        },
        "no_network_actions_performed": True,
        "credentials_or_tokens_copied": False,
        "source_text_copied": False,
        "source_language_terms_copied": False,
        "tasks_inspected": len(records),
        "summary": summary,
        "inspection_records": records,
        "current_approved_terms": 0,
        "current_accepted_corrections": 0,
        "native_review_status": "not_reviewed",
    }
    write_json(batch_json, batch)
    write_batch_markdown(batch, batch_md)

    summarize_queue(queue)
    queue["generated_utc"] = batch["generated_utc"]
    queue["status"] = queue_status_label(queue)
    write_json(QUEUE_JSON, queue)
    write_queue_markdown(queue)
    update_manifest_and_index(queue, batch_json, batch_md)

    print(
        json.dumps(
            {
                "batch": batch_json.name,
                "tasks_inspected": summary["tasks_inspected"],
                "language_lanes": lanes,
                "pages_checked": summary["pages_checked"],
                "ready_after_extraction_check": summary["ready_for_reviewer_packet_after_extraction_check"],
                "queue_completed_extraction_inspections": queue["current_completed_inspections"],
                "remaining_medium": sum(
                    1
                    for task in queue["tasks"]
                    if task.get("priority") == "medium" and task.get("inspection_status") == "not_started"
                ),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
