import datetime
import hashlib
import json
import pathlib
import re


BASE = pathlib.Path(__file__).resolve().parents[1]
STATUS_MANIFEST = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_MANIFEST_20260629.json"
STATUS_INDEX = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_INDEX_20260629.md"
SHORTLIST_JSON = BASE / "LOCAL_SOURCE_WITNESS_SHORTLIST_20260630.json"
READY_PACKET_JSON = BASE / "READY_CONTEXT_NOTE_ENTRY_PACKET_FRENCH_JAPANESE_20260630.json"
MANUAL_PACKET_JSON = BASE / "MANUAL_SOURCE_REVIEW_PACKET_BLOCKED_LANES_20260630.json"
WORKLIST_JSON = BASE / "PAGE_CONTEXT_NOTE_WORKLIST_20260629.json"
OUT_JSON = BASE / "LOCAL_SOURCE_WITNESS_SELECTION_MATRIX_20260630.json"
OUT_MD = BASE / "LOCAL_SOURCE_WITNESS_SELECTION_MATRIX_20260630.md"
SELF_PATH = pathlib.Path(__file__).resolve()

STATUS = "local_source_witness_selection_matrix_no_network_no_review_no_source_passage_copy"

READY_NOTE_LANES = {"french", "japanese"}
MANUAL_SOURCE_REVIEW_LANES = {"arabic", "fa_IR", "prs_AF", "simplified_chinese", "spanish"}
SOURCE_DISCOVERY_LANES = {"tg_Cyrl_TJ"}
CORE_WITNESS_LIMIT = 3
EXTENSION_WITNESS_LIMIT = 2

EXPECTED_EXTENSION_COHORTS = {
    "africa_deep_gap",
    "east_southeast_asia_pacific",
    "methodology_interlanguage_access",
    "pan_turkic_adjacent",
    "source_first_reference_textbooks",
    "south_asia_hindustani_indic_dravidian",
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


def lane_packet_map(packet: dict) -> dict[str, dict]:
    return {row.get("lane"): row for row in packet.get("lane_packets", [])}


def worklist_lane_map(worklist: dict) -> dict[str, dict]:
    return {row.get("lane"): row for row in worklist.get("lane_summary", [])}


def source_gate_use(row_id: str, kind: str) -> str:
    if row_id in READY_NOTE_LANES:
        return "selected_for_page_context_note_entry"
    if row_id in MANUAL_SOURCE_REVIEW_LANES:
        return "selected_for_manual_source_review_resolution"
    if row_id in SOURCE_DISCOVERY_LANES:
        return "selected_for_source_discovery_promotion"
    if kind == "extension_cohort":
        return "support_only_evidence_shelf"
    return "needs_lane_gate_review_before_selection_use"


def readiness_group(row_id: str, kind: str) -> str:
    if row_id in READY_NOTE_LANES:
        return "ready_context_note_entry_lane"
    if row_id in MANUAL_SOURCE_REVIEW_LANES:
        return "manual_source_review_required_lane"
    if row_id in SOURCE_DISCOVERY_LANES:
        return "source_discovery_required_before_term_queue"
    if kind == "extension_cohort":
        return "extension_cohort_support_not_edition_lane"
    return "unclassified_lane_gate"


def next_action(row_id: str, kind: str) -> str:
    if row_id in READY_NOTE_LANES:
        return "write_page_context_notes_without_source_quotes_before_reviewer_packet_population"
    if row_id in MANUAL_SOURCE_REVIEW_LANES:
        return "resolve_manual_source_review_rows_against_selected_witnesses_without_source_quotes"
    if row_id in SOURCE_DISCOVERY_LANES:
        return "promote_tajik_shelf_only_after_source_language_review_then_extract_term_anchors"
    if kind == "extension_cohort":
        return "keep_as_support_shelf_until_language_lane_authority_notes_exist"
    return "inspect_lane_gate_before_translation_revision"


def witness_limit(kind: str) -> int:
    if kind == "extension_cohort":
        return EXTENSION_WITNESS_LIMIT
    return CORE_WITNESS_LIMIT


def selection_reason(use: str, witness: dict) -> str:
    status = witness.get("candidate_status")
    if use == "selected_for_page_context_note_entry":
        return "highest_ranked_local_text_witness_for_blank_page_context_notes"
    if use == "selected_for_manual_source_review_resolution":
        if status == "pdf_heavy_manual_review_candidate":
            return "manual_review_backup_witness_pdf_heavy_use_without_copying_passages"
        return "highest_ranked_local_witness_for_manual_source_review_resolution"
    if use == "selected_for_source_discovery_promotion":
        return "local_tajik_witness_for_source_discovery_before_any_term_queue"
    return "supporting_evidence_shelf_for_future_lane_authority_notes"


def select_witnesses(row: dict) -> list[dict]:
    use = source_gate_use(row["lane_or_cohort"], row["kind"])
    selected = []
    for rank, witness in enumerate(row.get("candidates", [])[: witness_limit(row["kind"])], start=1):
        selected.append(
            {
                "selected_rank": rank,
                "source_shortlist_rank": witness.get("rank"),
                "batch": witness.get("batch"),
                "bucket": witness.get("bucket"),
                "path": witness.get("path"),
                "candidate_status": witness.get("candidate_status"),
                "source_balance": witness.get("source_balance"),
                "score": witness.get("score"),
                "disk_files": witness.get("disk_files"),
                "text_source_like_files": witness.get("text_source_like_files"),
                "tex_files": witness.get("tex_files"),
                "pdf_files": witness.get("pdf_files"),
                "source_core_files": witness.get("source_core_files"),
                "source_core_included": witness.get("source_core_included"),
                "selection_reason": selection_reason(use, witness),
                "use_before": next_action(row["lane_or_cohort"], row["kind"]),
                "source_excerpt_copied": False,
                "source_text_copied": False,
                "source_language_terms_copied": False,
            }
        )
    return selected


def build_matrix_row(row: dict, ready_by_lane: dict, manual_by_lane: dict, worklist_by_lane: dict) -> dict:
    row_id = row["lane_or_cohort"]
    kind = row["kind"]
    ready = ready_by_lane.get(row_id, {})
    manual = manual_by_lane.get(row_id, {})
    work = worklist_by_lane.get(row_id, {})
    selected = select_witnesses(row)
    gate_use = source_gate_use(row_id, kind)
    manual_rows = int(manual.get("manual_source_review_rows") or work.get("manual_or_source_review_notes") or 0)
    ready_forms = int(ready.get("forms") or 0)
    work_items = int(work.get("work_items") or 0)
    human_notes = int(work.get("human_page_context_notes") or 0)
    return {
        "lane_or_cohort": row_id,
        "kind": kind,
        "label": row.get("label"),
        "edition_gate": row.get("edition_gate"),
        "source_gate_use": gate_use,
        "readiness_group": readiness_group(row_id, kind),
        "term_anchor_rows": row.get("term_anchor_rows", 0),
        "pages_analyzed": row.get("pages_analyzed", 0),
        "candidate_shelves_available": row.get("candidate_shelves", 0),
        "selected_witnesses_count": len(selected),
        "selected_witnesses_with_source_core": sum(1 for witness in selected if (witness.get("source_core_files") or 0) > 0),
        "selected_text_source_like_files": sum(int(witness.get("text_source_like_files") or 0) for witness in selected),
        "selected_tex_files": sum(int(witness.get("tex_files") or 0) for witness in selected),
        "selected_pdf_files": sum(int(witness.get("pdf_files") or 0) for witness in selected),
        "selected_source_core_files": sum(int(witness.get("source_core_files") or 0) for witness in selected),
        "page_context_work_items": work_items,
        "page_context_human_note_count": human_notes,
        "ready_context_note_forms": ready_forms,
        "manual_source_review_rows": manual_rows,
        "forms_filled": int(ready.get("forms_filled") or manual.get("forms_filled") or 0),
        "packet_rows_blocked": int(
            ready.get("packet_rows_blocked") or manual.get("packet_rows_blocked") or work.get("blocked_until_note") or 0
        ),
        "source_discovery_required": row_id in SOURCE_DISCOVERY_LANES,
        "next_action": next_action(row_id, kind),
        "authority_boundary": "local_selection_matrix_not_native_review_not_canonical_terminology",
        "review_packet_population_performed": False,
        "translation_or_revision_performed": False,
        "source_text_copied": False,
        "source_language_terms_copied": False,
        "native_review_status": "not_reviewed",
        "canonical_approval_status": "not_approved",
        "selected_witnesses": selected,
    }


def build_document(manifest: dict) -> dict:
    shortlist = load_json(SHORTLIST_JSON)
    ready_packet = load_json(READY_PACKET_JSON)
    manual_packet = load_json(MANUAL_PACKET_JSON)
    worklist = load_json(WORKLIST_JSON)
    ready_by_lane = lane_packet_map(ready_packet)
    manual_by_lane = lane_packet_map(manual_packet)
    worklist_by_lane = worklist_lane_map(worklist)
    rows = [
        build_matrix_row(row, ready_by_lane, manual_by_lane, worklist_by_lane)
        for row in shortlist.get("shortlist_rows", [])
    ]
    core_rows = [row for row in rows if row["kind"] == "core_language_lane"]
    extension_rows = [row for row in rows if row["kind"] == "extension_cohort"]
    selected_witnesses = sum(row["selected_witnesses_count"] for row in rows)
    return {
        "artifact": "local_source_witness_selection_matrix",
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
        "inputs": {
            "local_source_witness_shortlist": SHORTLIST_JSON.name,
            "ready_context_note_entry_packet": READY_PACKET_JSON.name,
            "manual_source_review_packet": MANUAL_PACKET_JSON.name,
            "page_context_note_worklist": WORKLIST_JSON.name,
            "status_manifest": STATUS_MANIFEST.name,
        },
        "selection_policy": {
            "ready_note_lanes": sorted(READY_NOTE_LANES),
            "manual_source_review_lanes": sorted(MANUAL_SOURCE_REVIEW_LANES),
            "source_discovery_lanes": sorted(SOURCE_DISCOVERY_LANES),
            "extension_cohorts": sorted(EXPECTED_EXTENSION_COHORTS),
            "max_core_witnesses_per_lane": CORE_WITNESS_LIMIT,
            "max_extension_witnesses_per_cohort": EXTENSION_WITNESS_LIMIT,
            "copy_source_passages": False,
            "copy_source_language_terms": False,
            "fill_review_or_translation_fields": False,
        },
        "summary": {
            "lane_or_cohort_count": len(rows),
            "core_language_lanes": len(core_rows),
            "extension_cohorts": len(extension_rows),
            "selected_witnesses": selected_witnesses,
            "selected_source_core_backed_witnesses": sum(row["selected_witnesses_with_source_core"] for row in rows),
            "selected_text_source_like_files": sum(row["selected_text_source_like_files"] for row in rows),
            "selected_tex_files": sum(row["selected_tex_files"] for row in rows),
            "selected_pdf_files": sum(row["selected_pdf_files"] for row in rows),
            "selected_source_core_files": sum(row["selected_source_core_files"] for row in rows),
            "ready_note_entry_lanes": len(READY_NOTE_LANES),
            "ready_note_forms": ready_packet.get("totals", {}).get("forms", 0),
            "manual_source_review_lanes": len(MANUAL_SOURCE_REVIEW_LANES),
            "manual_source_review_rows": manual_packet.get("totals", {}).get("manual_source_review_rows", 0),
            "source_discovery_promotions": len(SOURCE_DISCOVERY_LANES),
            "support_cohorts": len(extension_rows),
            "forms_filled": ready_packet.get("totals", {}).get("forms_filled", 0)
            + manual_packet.get("totals", {}).get("forms_filled", 0),
            "review_packet_population_performed": False,
            "translation_or_revision_performed": False,
            "native_review_status": "not_reviewed",
            "current_approved_terms": 0,
            "current_accepted_corrections": 0,
        },
        "matrix_rows": rows,
        "promotion_rules": [
            "selected witnesses are inspection targets, not approved terminology sources",
            "French and Japanese selected witnesses feed blank page-context note entry only",
            "Arabic, Persian/Farsi, Dari, Simplified Chinese, and Spanish selected witnesses feed manual/source-review resolution",
            "Tajik Cyrillic remains source-discovery-only until a source-language review promotes it to term-anchor extraction",
            "extension cohorts remain support shelves until explicit language-lane authority notes exist",
        ],
        "boundaries": [
            "No source-language passages or source-language term strings are copied into this matrix.",
            "No review packet row was populated and no translation or revision was performed.",
            "Local witness selection is mechanical evidence routing, not native/external authority.",
            "No network action was performed.",
            "The active Noether multilingual goal remains open.",
        ],
    }


def md_cell(value: object) -> str:
    return str(value).replace("|", "/").replace("\n", " ")


def write_markdown(document: dict) -> None:
    summary = document["summary"]
    lines = [
        "# Local source-witness selection matrix - 2026-06-30",
        "",
        "Status: selection matrix only. No network action, review, translation, or source-passage copying was performed.",
        "",
        "## Summary",
        "",
        f"- Lane/cohort rows: {summary['lane_or_cohort_count']}",
        f"- Core language lanes: {summary['core_language_lanes']}",
        f"- Extension cohorts: {summary['extension_cohorts']}",
        f"- Selected witness shelves: {summary['selected_witnesses']}",
        f"- Selected source-core-backed witnesses: {summary['selected_source_core_backed_witnesses']}",
        f"- Ready note-entry lanes/forms: {summary['ready_note_entry_lanes']} / {summary['ready_note_forms']}",
        f"- Manual/source-review lanes/rows: {summary['manual_source_review_lanes']} / {summary['manual_source_review_rows']}",
        f"- Source-discovery promotions: {summary['source_discovery_promotions']}",
        f"- Support cohorts: {summary['support_cohorts']}",
        f"- Network actions performed: `{str((not document['no_network_actions_performed'])).lower()}`",
        "",
        "## Matrix",
        "",
        "| Lane/cohort | Use | Selected | Source-core | Candidates | Work items | Manual rows | Next action |",
        "| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in document["matrix_rows"]:
        lines.append(
            "| `{lane}` | `{use}` | {selected} | {source_core} | {candidates} | {work_items} | {manual_rows} | `{next_action}` |".format(
                lane=md_cell(row["lane_or_cohort"]),
                use=md_cell(row["source_gate_use"]),
                selected=row["selected_witnesses_count"],
                source_core=row["selected_witnesses_with_source_core"],
                candidates=row["candidate_shelves_available"],
                work_items=row["page_context_work_items"],
                manual_rows=row["manual_source_review_rows"],
                next_action=md_cell(row["next_action"]),
            )
        )
    lines.extend(["", "## Promotion Rules", ""])
    lines.extend(f"- {rule}" for rule in document["promotion_rules"])
    lines.extend(["", "## Boundaries", ""])
    lines.extend(f"- {boundary}" for boundary in document["boundaries"])
    lines.append("")
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def update_status_index(document: dict, manifest: dict) -> None:
    text = STATUS_INDEX.read_text(encoding="utf-8")
    counts = {
        "json": len(manifest["artifacts"]["json"]),
        "markdown": len(manifest["artifacts"]["markdown"]),
        "scripts": len(manifest["artifacts"]["scripts"]),
    }
    text = re.sub(
        r"- JSON artifacts indexed: \d+ plus this status manifest",
        f"- JSON artifacts indexed: {counts['json']} plus this status manifest",
        text,
    )
    text = re.sub(
        r"- Markdown artifacts indexed: \d+ plus this status index",
        f"- Markdown artifacts indexed: {counts['markdown']} plus this status index",
        text,
    )
    text = re.sub(
        r"- Reproducible scripts indexed: \d+",
        f"- Reproducible scripts indexed: {counts['scripts']}",
        text,
    )
    summary = document["summary"]
    line = (
        "- Local source-witness selection matrix: "
        f"{summary['lane_or_cohort_count']} lane/cohort rows / "
        f"{summary['selected_witnesses']} selected witness shelves / "
        f"{summary['manual_source_review_rows']} manual/source-review rows routed / "
        "0 network actions"
    )
    if re.search(r"^- Local source-witness selection matrix: .*", text, flags=re.MULTILINE):
        text = re.sub(r"^- Local source-witness selection matrix: .*", line, text, flags=re.MULTILINE)
    else:
        marker = "- Local source-witness shortlist:"
        rows = text.splitlines()
        for offset, row in enumerate(rows):
            if row.startswith(marker):
                rows.insert(offset + 1, line)
                text = "\n".join(rows) + "\n"
                break
    text = text.replace(
        "local-source-evidence-shelf inventory/source-witness-shortlist metadata",
        "local-source-evidence-shelf inventory/source-witness-shortlist/selection-matrix metadata",
    )
    text = text.replace(
        "local-source-evidence-shelf inventory/source-witness-shortlist/selection-matrix/selection-matrix metadata",
        "local-source-evidence-shelf inventory/source-witness-shortlist/selection-matrix metadata",
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
    summary = document["summary"]
    manifest["local_source_witness_selection_matrix"] = {
        "status": document["status"],
        "artifact_markdown": OUT_MD.name,
        "artifact_json": OUT_JSON.name,
        "lane_or_cohort_count": summary["lane_or_cohort_count"],
        "core_language_lanes": summary["core_language_lanes"],
        "extension_cohorts": summary["extension_cohorts"],
        "selected_witnesses": summary["selected_witnesses"],
        "selected_source_core_backed_witnesses": summary["selected_source_core_backed_witnesses"],
        "selected_text_source_like_files": summary["selected_text_source_like_files"],
        "selected_source_core_files": summary["selected_source_core_files"],
        "ready_note_entry_lanes": summary["ready_note_entry_lanes"],
        "ready_note_forms": summary["ready_note_forms"],
        "manual_source_review_lanes": summary["manual_source_review_lanes"],
        "manual_source_review_rows": summary["manual_source_review_rows"],
        "source_discovery_promotions": summary["source_discovery_promotions"],
        "support_cohorts": summary["support_cohorts"],
        "forms_filled": summary["forms_filled"],
        "review_packet_population_performed": False,
        "translation_or_revision_performed": False,
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
    manifest = load_json(STATUS_MANIFEST)
    document = build_document(manifest)
    write_json(OUT_JSON, document)
    write_markdown(document)
    update_manifest(document)
    print(
        json.dumps(
            {
                "selection_matrix_json": str(OUT_JSON),
                "lane_or_cohort_count": document["summary"]["lane_or_cohort_count"],
                "selected_witnesses": document["summary"]["selected_witnesses"],
                "selected_source_core_backed_witnesses": document["summary"][
                    "selected_source_core_backed_witnesses"
                ],
                "manual_source_review_rows": document["summary"]["manual_source_review_rows"],
                "ready_note_forms": document["summary"]["ready_note_forms"],
                "no_network_actions_performed": document["no_network_actions_performed"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
