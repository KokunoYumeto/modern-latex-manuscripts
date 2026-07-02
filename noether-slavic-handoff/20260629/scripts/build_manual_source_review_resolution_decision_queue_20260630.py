import datetime
import hashlib
import json
import pathlib
import re
from collections import Counter, defaultdict


BASE = pathlib.Path(__file__).resolve().parents[1]
STATUS_MANIFEST = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_MANIFEST_20260629.json"
STATUS_INDEX = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_INDEX_20260629.md"
MANUAL_PACKET_JSON = BASE / "MANUAL_SOURCE_REVIEW_PACKET_BLOCKED_LANES_20260630.json"
PREFLIGHT_JSON = BASE / "REVIEW_PACKET_POPULATION_PREFLIGHT_MATRIX_20260630.json"
OUT_JSON = BASE / "MANUAL_SOURCE_REVIEW_RESOLUTION_DECISION_QUEUE_20260630.json"
OUT_MD = BASE / "MANUAL_SOURCE_REVIEW_RESOLUTION_DECISION_QUEUE_20260630.md"
SELF_PATH = pathlib.Path(__file__).resolve()

STATUS = "manual_source_review_resolution_decision_queue_pending_no_resolution_no_packet_population"


LANE_REVIEW_ROLES = {
    "arabic": [
        "native_arabic_mathematical_reviewer",
        "rtl_tex_pdf_reviewer",
    ],
    "fa_IR": [
        "iranian_persian_mathematical_reviewer",
        "rtl_or_script_reviewer",
    ],
    "prs_AF": [
        "dari_afghan_persian_educator_or_technical_reviewer",
        "rtl_or_script_reviewer",
    ],
    "simplified_chinese": [
        "native_simplified_chinese_mathematical_reviewer",
        "chinese_tex_pdf_visual_reviewer",
    ],
    "spanish": [
        "native_or_near_native_spanish_mathematical_reviewer",
        "optional_undergraduate_algebra_or_physics_educator_reviewer",
    ],
}

ISSUE_CLASS_CHECKS = {
    "rtl_register_or_extraction_variant_manual_review": [
        "inspect RTL extraction/register mismatch without copying source text",
        "record whether OCR or text extraction failed to reverify the expected anchor",
        "record script, punctuation, numeral, and formula-neighboring layout concerns",
        "route to context-note entry only after a non-quoted manual note exists",
    ],
    "specialist_term_variant_or_anchor_manual_review": [
        "inspect specialist term variant or anchor mismatch without copying source text",
        "record whether the concept should be rerouted, deferred, or kept as a candidate",
        "record whether additional page evidence or source discovery is needed",
        "route to context-note entry only after a non-quoted manual note exists",
    ],
}

DECISION_OPTIONS = [
    "resolve_to_context_note_entry_after_nonquoted_manual_note",
    "defer_pending_additional_source_or_ocr_review",
    "reject_or_demote_anchor_candidate_with_reason",
    "keep_blocked_with_specific_remaining_blocker",
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


def preflight_by_lane(preflight: dict) -> dict[str, dict]:
    return {
        row["lane_or_cohort"]: row
        for row in preflight.get("preflight_rows", [])
        if row.get("lane_or_cohort") in {"arabic", "fa_IR", "prs_AF", "simplified_chinese", "spanish"}
    }


def flatten_manual_rows(packet: dict) -> list[dict]:
    rows = []
    for lane_packet in packet.get("lane_packets", []):
        lane = lane_packet.get("lane")
        for row in lane_packet.get("rows_to_review", []):
            enriched = dict(row)
            enriched["lane_required_reviewer_roles"] = lane_packet.get("required_reviewer_roles", [])
            enriched["lane_extra_checks"] = lane_packet.get("lane_extra_checks", [])
            enriched["lane_packet"] = lane
            rows.append(enriched)
    return sorted(rows, key=lambda row: (row["language_lane"], row["priority"], row["term_id"]))


def queue_row(row: dict, preflight_row: dict) -> dict:
    issue_class = row["issue_class"]
    lane = row["language_lane"]
    checks = ISSUE_CLASS_CHECKS[issue_class] + row.get("lane_extra_checks", [])
    return {
        "queue_item_id": f"manual-resolution-{row['form_id']}",
        "form_id": row["form_id"],
        "term_id": row["term_id"],
        "language_lane": lane,
        "english_concept": row["english_concept"],
        "mathematical_domain": row["mathematical_domain"],
        "priority": row["priority"],
        "inspection_batch_id": row["inspection_batch_id"],
        "batch_json": row["batch_json"],
        "issue_class": issue_class,
        "recommended_action": row["recommended_action"],
        "pages_checked": row["pages_checked"],
        "pages_with_exact_term_occurrence": row["pages_with_exact_term_occurrence"],
        "sources_checked": row["sources_checked"],
        "cache_missing_sources": row["cache_missing_sources"],
        "hash_mismatch_sources": row["hash_mismatch_sources"],
        "decision_status": "pending_manual_source_review_decision",
        "allowed_resolution_decisions": DECISION_OPTIONS,
        "required_resolution_checks": checks,
        "suggested_reviewer_roles": LANE_REVIEW_ROLES[lane],
        "manual_note_fields_required": row["fields_to_fill"],
        "manual_note_values_status": "blank_not_filled",
        "source_capture_form_status": row["form_status"],
        "packet_population_status": row["packet_population_status"],
        "preflight_packet_id": preflight_row.get("packet_id"),
        "preflight_missing_gate": preflight_row.get("missing_gate"),
        "preflight_packet_population_allowed": preflight_row.get("packet_population_allowed"),
        "preflight_send_to_review_allowed": preflight_row.get("send_to_review_allowed"),
        "resolution_performed": False,
        "manual_note_filled": False,
        "rerouted_to_context_note_entry": False,
        "review_packet_population_performed": False,
        "source_text_copied": False,
        "source_language_terms_copied": False,
        "native_review_status": "not_reviewed",
        "canonical_approval_status": "not_approved",
    }


def build_document() -> dict:
    manual_packet = load_json(MANUAL_PACKET_JSON)
    preflight = load_json(PREFLIGHT_JSON)
    preflight_rows = preflight_by_lane(preflight)
    rows = [
        queue_row(row, preflight_rows[row["language_lane"]])
        for row in flatten_manual_rows(manual_packet)
    ]

    by_lane = defaultdict(list)
    for row in rows:
        by_lane[row["language_lane"]].append(row)
    lane_summary = []
    for lane in sorted(by_lane):
        lane_rows = by_lane[lane]
        lane_summary.append(
            {
                "lane": lane,
                "queue_items": len(lane_rows),
                "pending_decisions": len(lane_rows),
                "resolved_items": 0,
                "manual_notes_filled": 0,
                "rerouted_to_context_note_entry": 0,
                "review_packet_rows_populated": 0,
                "pages_checked": sum(int(row["pages_checked"]) for row in lane_rows),
                "issue_class_counts": dict(sorted(Counter(row["issue_class"] for row in lane_rows).items())),
                "domains": dict(sorted(Counter(row["mathematical_domain"] for row in lane_rows).items())),
            }
        )

    return {
        "artifact": "manual_source_review_resolution_decision_queue",
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
            "manual_source_review_packet": MANUAL_PACKET_JSON.name,
            "review_packet_population_preflight": PREFLIGHT_JSON.name,
        },
        "queue_policy": {
            "resolution_decisions_are_pending": True,
            "manual_notes_are_blank": True,
            "review_packet_population_performed": False,
            "source_passage_copying_allowed": False,
            "source_language_term_copying_allowed": False,
            "native_review_claim_allowed": False,
            "canonical_approval_allowed": False,
            "included_lanes": ["arabic", "fa_IR", "prs_AF", "simplified_chinese", "spanish"],
        },
        "totals": {
            "lanes": len(lane_summary),
            "queue_items": len(rows),
            "pending_decisions": len(rows),
            "resolved_items": 0,
            "manual_notes_filled": 0,
            "rerouted_to_context_note_entry": 0,
            "review_packet_rows_populated": 0,
            "cache_missing_sources": sum(int(row["cache_missing_sources"]) for row in rows),
            "hash_mismatch_sources": sum(int(row["hash_mismatch_sources"]) for row in rows),
            "review_packet_population_performed": False,
            "current_approved_terms": 0,
            "current_accepted_corrections": 0,
        },
        "lane_summary": lane_summary,
        "queue_items": rows,
        "boundaries": [
            "This queue records required manual/source-review decisions only.",
            "No manual/source-review decision is performed here.",
            "Manual note values remain blank and source capture forms remain blocked.",
            "No reviewer packet population, review send, accepted correction ingestion, or canonical approval is performed.",
            "No source-language passages or source-language terms are copied.",
        ],
    }


def write_markdown(document: dict) -> None:
    totals = document["totals"]
    lines = [
        "# Manual/source-review resolution decision queue - 2026-06-30",
        "",
        "Status: decision queue only. No manual review decision, note filling, reviewer-packet population, or term approval is performed.",
        "",
        "## Totals",
        "",
        f"- Queue items: {totals['queue_items']}",
        f"- Pending decisions: {totals['pending_decisions']}",
        f"- Resolved items: {totals['resolved_items']}",
        f"- Manual notes filled: {totals['manual_notes_filled']}",
        f"- Rerouted to context-note entry: {totals['rerouted_to_context_note_entry']}",
        f"- Reviewer packet rows populated: {totals['review_packet_rows_populated']}",
        "",
        "## Lane Summary",
        "",
        "| Lane | Queue items | Pending | Resolved | Notes filled | Rerouted | Packet rows populated |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in document["lane_summary"]:
        lines.append(
            f"| {row['lane']} | {row['queue_items']} | {row['pending_decisions']} | {row['resolved_items']} | "
            f"{row['manual_notes_filled']} | {row['rerouted_to_context_note_entry']} | "
            f"{row['review_packet_rows_populated']} |"
        )
    lines.extend(
        [
            "",
            "## Resolution Options",
            "",
        ]
    )
    for option in DECISION_OPTIONS:
        lines.append(f"- `{option}`")
    lines.extend(
        [
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
        "- Manual/source-review resolution decision queue: "
        f"{document['totals']['queue_items']} queue items / "
        "0 resolved / 0 notes filled / reviewer packets still blocked"
    )
    if re.search(r"^- Manual/source-review resolution decision queue: .*", text, flags=re.MULTILINE):
        text = re.sub(r"^- Manual/source-review resolution decision queue: .*", line, text, flags=re.MULTILINE)
    else:
        marker = "- Manual/source-review work packet:"
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
        "ready-note-entry/context-note-draft/context-note-candidate-filled/context-note-confirmation-apply/manual-triage/reviewer-scaffold",
        "ready-note-entry/context-note-draft/context-note-candidate-filled/context-note-confirmation-apply/manual-triage/manual-source-resolution-decision/reviewer-scaffold",
    )
    text = text.replace(
        "ready-note-entry/manual-source-review-packet/manual-triage/reviewer-scaffold",
        "ready-note-entry/manual-source-review-packet/manual-triage/manual-source-resolution-decision/reviewer-scaffold",
    )
    text = text.replace(
        "manual-source-resolution-decision/manual-source-resolution-decision",
        "manual-source-resolution-decision",
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
    manifest["manual_source_review_resolution_decision_queue"] = {
        "status": document["status"],
        "artifact_markdown": OUT_MD.name,
        "artifact_json": OUT_JSON.name,
        "lanes": totals["lanes"],
        "queue_items": totals["queue_items"],
        "pending_decisions": totals["pending_decisions"],
        "resolved_items": 0,
        "manual_notes_filled": 0,
        "rerouted_to_context_note_entry": 0,
        "review_packet_rows_populated": 0,
        "cache_missing_sources": totals["cache_missing_sources"],
        "hash_mismatch_sources": totals["hash_mismatch_sources"],
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
                "manual_source_review_resolution_decision_queue_json": str(OUT_JSON),
                "queue_items": document["totals"]["queue_items"],
                "pending_decisions": document["totals"]["pending_decisions"],
                "resolved_items": document["totals"]["resolved_items"],
                "manual_notes_filled": document["totals"]["manual_notes_filled"],
                "review_packet_rows_populated": document["totals"]["review_packet_rows_populated"],
                "no_network_actions_performed": document["no_network_actions_performed"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
