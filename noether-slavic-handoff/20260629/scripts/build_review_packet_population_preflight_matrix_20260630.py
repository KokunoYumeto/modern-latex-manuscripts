import datetime
import hashlib
import json
import pathlib
import re


BASE = pathlib.Path(__file__).resolve().parents[1]
STATUS_MANIFEST = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_MANIFEST_20260629.json"
STATUS_INDEX = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_INDEX_20260629.md"
LANE_ACTION_QUEUE_JSON = BASE / "LANE_PROMOTION_NEXT_ACTION_QUEUE_20260630.json"
AUTHORITY_FORMS_JSON = BASE / "EXTERNAL_AUTHORITY_REVIEW_PACKET_FORMS_20260630.json"
OUT_JSON = BASE / "REVIEW_PACKET_POPULATION_PREFLIGHT_MATRIX_20260630.json"
OUT_MD = BASE / "REVIEW_PACKET_POPULATION_PREFLIGHT_MATRIX_20260630.md"
SELF_PATH = pathlib.Path(__file__).resolve()

STATUS = "review_packet_population_preflight_matrix_all_packets_blocked_no_review"


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


def lane_preconditions(action_type: str) -> list[str]:
    if action_type == "fill_page_context_notes":
        return [
            "all ready-context note fields filled without source quotations",
            "note form count equals ready-context note task count",
            "external authority packet remains blank until note packet is reviewed for completeness",
        ]
    if action_type == "resolve_manual_source_review_rows":
        return [
            "all manual/source-review rows have source-review decisions",
            "manual rows are rerouted to context notes, rejected, or remain blocked with reason",
            "unresolved manual/source-review count reaches zero before packet population",
        ]
    if action_type == "promote_source_discovery_to_term_anchor_queue":
        return [
            "source-discovery candidate is promoted, rejected, or remains blocked with reason",
            "term-anchor queue is not populated without source-discovery evidence",
            "review packet remains blank before term-anchor promotion",
        ]
    return [
        "support-cohort authority note records usefulness, limits, and non-edition status",
        "cohort remains outside canonical edition claims until explicitly promoted",
        "authority note is linked to required reviewer roles",
    ]


def method_preconditions() -> list[str]:
    return [
        "methodology reviewer role or identity is recorded",
        "claim scope authorized by reviewer is recorded",
        "required revisions or remaining blockers are recorded",
        "accepted corrections are ingested before publication claims",
    ]


def lane_missing_gate(action_type: str) -> str:
    if action_type == "fill_page_context_notes":
        return "page_context_notes_blank"
    if action_type == "resolve_manual_source_review_rows":
        return "manual_source_review_rows_unresolved"
    if action_type == "promote_source_discovery_to_term_anchor_queue":
        return "source_discovery_not_promoted"
    return "support_cohort_not_promoted_to_edition_lane"


def build_rows(queue: dict, forms: dict) -> list[dict]:
    lane_actions = {row["lane_or_cohort"]: row for row in queue.get("lane_action_rows", [])}
    method_actions = {row["source_queue_id"]: row for row in queue.get("methodology_action_rows", [])}
    rows = []
    for packet in forms.get("packet_groups_detail", []):
        if packet.get("queue_group") == "lane_authority":
            action = lane_actions.get(packet.get("lane_or_cohort"), {})
            missing_gate = lane_missing_gate(action.get("action_type"))
            rows.append(
                {
                    "packet_id": packet["packet_id"],
                    "queue_id": packet.get("queue_id"),
                    "queue_group": packet.get("queue_group"),
                    "lane_or_cohort": packet.get("lane_or_cohort"),
                    "lane_type": packet.get("lane_type"),
                    "queue_kind": packet.get("queue_kind"),
                    "upstream_action_type": action.get("action_type"),
                    "upstream_blocker_class": action.get("blocker_class"),
                    "upstream_work_units": action.get("work_units", 0),
                    "ready_context_note_tasks": action.get("ready_context_note_tasks", 0),
                    "manual_source_review_tasks": action.get("manual_source_review_tasks", 0),
                    "source_discovery_tasks": action.get("source_discovery_tasks", 0),
                    "support_cohort_tasks": action.get("support_cohort_tasks", 0),
                    "preconditions_required_before_population": lane_preconditions(action.get("action_type")),
                    "missing_gate": missing_gate,
                    "packet_population_allowed": False,
                    "send_to_review_allowed": False,
                    "preflight_status": "blocked_before_packet_population",
                    "reviewer_role_forms": packet.get("reviewer_role_forms", 0),
                    "review_packet_status": packet.get("review_packet_status"),
                    "review_fields_filled": 0,
                    "review_packet_sent": False,
                    "review_return_received": False,
                    "external_reviews_performed": 0,
                    "accepted_corrections_ingested": 0,
                    "review_packet_population_performed": False,
                    "translation_or_revision_performed": False,
                    "canonical_completion_claim": False,
                    "publication_completion_claim": False,
                    "source_text_copied": False,
                    "source_language_terms_copied": False,
                    "native_review_status": "not_reviewed",
                    "canonical_approval_status": "not_approved",
                }
            )
        else:
            action = method_actions.get(packet.get("queue_id"), {})
            rows.append(
                {
                    "packet_id": packet["packet_id"],
                    "queue_id": packet.get("queue_id"),
                    "queue_group": packet.get("queue_group"),
                    "lane_or_cohort": None,
                    "lane_type": packet.get("lane_type"),
                    "queue_kind": packet.get("queue_kind"),
                    "upstream_action_type": action.get("action_type"),
                    "upstream_blocker_class": action.get("blocker_class"),
                    "upstream_work_units": 1,
                    "ready_context_note_tasks": 0,
                    "manual_source_review_tasks": 0,
                    "source_discovery_tasks": 0,
                    "support_cohort_tasks": 0,
                    "preconditions_required_before_population": method_preconditions(),
                    "missing_gate": "methodology_authority_review_not_returned",
                    "packet_population_allowed": False,
                    "send_to_review_allowed": False,
                    "preflight_status": "blocked_before_publication_claim_review",
                    "reviewer_role_forms": packet.get("reviewer_role_forms", 0),
                    "review_packet_status": packet.get("review_packet_status"),
                    "review_fields_filled": 0,
                    "review_packet_sent": False,
                    "review_return_received": False,
                    "external_reviews_performed": 0,
                    "accepted_corrections_ingested": 0,
                    "review_packet_population_performed": False,
                    "translation_or_revision_performed": False,
                    "canonical_completion_claim": False,
                    "publication_completion_claim": False,
                    "source_text_copied": False,
                    "source_language_terms_copied": False,
                    "native_review_status": "not_reviewed",
                    "canonical_approval_status": "not_approved",
                }
            )
    return rows


def build_summary(rows: list[dict], queue: dict, forms: dict) -> dict:
    return {
        "packet_groups": len(rows),
        "lane_packet_groups": sum(1 for row in rows if row["queue_group"] == "lane_authority"),
        "methodology_packet_groups": sum(1 for row in rows if row["queue_group"] == "methodology_authority"),
        "reviewer_role_forms": sum(row["reviewer_role_forms"] for row in rows),
        "lane_reviewer_role_forms": sum(row["reviewer_role_forms"] for row in rows if row["queue_group"] == "lane_authority"),
        "methodology_reviewer_role_forms": sum(
            row["reviewer_role_forms"] for row in rows if row["queue_group"] == "methodology_authority"
        ),
        "blocked_packet_groups": sum(1 for row in rows if not row["packet_population_allowed"]),
        "packet_population_allowed_groups": sum(1 for row in rows if row["packet_population_allowed"]),
        "send_to_review_allowed_groups": sum(1 for row in rows if row["send_to_review_allowed"]),
        "ready_context_note_blocked_groups": sum(1 for row in rows if row["missing_gate"] == "page_context_notes_blank"),
        "manual_source_review_blocked_groups": sum(
            1 for row in rows if row["missing_gate"] == "manual_source_review_rows_unresolved"
        ),
        "source_discovery_blocked_groups": sum(1 for row in rows if row["missing_gate"] == "source_discovery_not_promoted"),
        "support_cohort_blocked_groups": sum(
            1 for row in rows if row["missing_gate"] == "support_cohort_not_promoted_to_edition_lane"
        ),
        "methodology_blocked_groups": sum(
            1 for row in rows if row["missing_gate"] == "methodology_authority_review_not_returned"
        ),
        "lane_work_units_blocking_population": queue.get("summary", {}).get("lane_work_units", 0),
        "methodology_actions_blocking_publication_review": queue.get("summary", {}).get("methodology_action_rows", 0),
        "review_fields_filled": forms.get("summary", {}).get("review_fields_filled", 0),
        "review_packets_sent": forms.get("summary", {}).get("review_packets_sent", 0),
        "review_returns_received": forms.get("summary", {}).get("review_returns_received", 0),
        "external_reviews_performed": forms.get("summary", {}).get("external_reviews_performed", 0),
        "accepted_corrections_ingested": forms.get("summary", {}).get("accepted_corrections_ingested", 0),
        "review_packet_population_performed": False,
        "translation_or_revision_performed": False,
        "canonical_completion_claim": False,
        "publication_completion_claim": False,
        "native_review_status": "not_reviewed",
        "current_approved_terms": 0,
        "current_accepted_corrections": 0,
    }


def build_document(manifest: dict) -> dict:
    queue = load_json(LANE_ACTION_QUEUE_JSON)
    forms = load_json(AUTHORITY_FORMS_JSON)
    rows = build_rows(queue, forms)
    return {
        "artifact": "review_packet_population_preflight_matrix",
        "generated_utc": now_utc(),
        "generated_date": "20260630",
        "status": STATUS,
        "bandwidth_mode": "local_only_no_network_actions",
        "inputs": {
            "status_manifest": STATUS_MANIFEST.name,
            "lane_promotion_next_action_queue": LANE_ACTION_QUEUE_JSON.name,
            "external_authority_review_packet_forms": AUTHORITY_FORMS_JSON.name,
        },
        "preflight_policy": {
            "packet_population_requires_completed_upstream_gate": True,
            "blank_page_context_notes_block_population": True,
            "manual_source_review_rows_block_population": True,
            "source_discovery_not_promoted_blocks_population": True,
            "support_cohorts_are_not_edition_lanes": True,
            "methodology_publication_claims_require_external_methodology_review": True,
            "local_preflight_is_not_native_authority": True,
        },
        "summary": build_summary(rows, queue, forms),
        "preflight_rows": rows,
        "boundaries": {
            "local_preflight_only": True,
            "review_packet_population_not_performed": True,
            "external_or_native_review_not_performed": True,
            "source_text_not_copied": True,
            "source_language_terms_not_copied": True,
            "credentials_or_tokens_not_copied": True,
            "no_network_actions_performed": True,
        },
        "no_network_actions_performed": True,
        "credentials_or_tokens_copied": False,
        "source_text_copied": False,
        "source_language_terms_copied": False,
        "native_review_status": "not_reviewed",
        "current_approved_terms": 0,
        "current_accepted_corrections": 0,
        "canonical_completion_claim": False,
        "publication_completion_claim": False,
        "manifest_status_at_build_time": manifest.get("status"),
    }


def write_markdown(document: dict) -> None:
    summary = document["summary"]
    lines = [
        "# Review Packet Population Preflight Matrix - 2026-06-30",
        "",
        f"Status: `{document['status']}`",
        "",
        "This matrix is a local-only gatekeeper for authority-review packet population. Every packet group is blocked until its upstream lane or methodology gate is completed and validated.",
        "",
        "## Summary",
        "",
        f"- Packet groups: {summary['packet_groups']} ({summary['lane_packet_groups']} lane, {summary['methodology_packet_groups']} methodology)",
        f"- Reviewer-role forms: {summary['reviewer_role_forms']} ({summary['lane_reviewer_role_forms']} lane, {summary['methodology_reviewer_role_forms']} methodology)",
        f"- Blocked packet groups: {summary['blocked_packet_groups']}; population allowed: {summary['packet_population_allowed_groups']}; send allowed: {summary['send_to_review_allowed_groups']}",
        f"- Lane blockers: {summary['ready_context_note_blocked_groups']} ready-note, {summary['manual_source_review_blocked_groups']} manual/source-review, {summary['source_discovery_blocked_groups']} source-discovery, {summary['support_cohort_blocked_groups']} support-cohort",
        f"- Methodology blockers: {summary['methodology_blocked_groups']}",
        "- Reviews performed: 0; corrections ingested: 0; completion claims: false",
        "",
        "## Rows",
        "",
        "| Packet | Group | Lane/type | Gate | Work units | Forms | Population |",
        "|---|---|---|---|---:|---:|---|",
    ]
    for row in document["preflight_rows"]:
        lane_or_type = row["lane_or_cohort"] or row["lane_type"]
        lines.append(
            f"| {row['packet_id']} | {row['queue_group']} | {lane_or_type} | {row['missing_gate']} | {row['upstream_work_units']} | {row['reviewer_role_forms']} | blocked |"
        )
    lines.extend(
        [
            "",
            "## Boundary Notes",
            "",
            "- This preflight does not populate or send any packet.",
            "- It records only local gate state; it is not native, external, or publication authority.",
            "- All reviewer fields remain blank until upstream gates are completed and a separate packet-population step is run.",
        ]
    )
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


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
        "- Review packet population preflight matrix: "
        f"{summary['packet_groups']} packet groups / "
        f"{summary['blocked_packet_groups']} blocked / "
        f"{summary['reviewer_role_forms']} reviewer-role forms / "
        "0 packet population"
    )
    if re.search(r"^- Review packet population preflight matrix: .*", text, flags=re.MULTILINE):
        text = re.sub(r"^- Review packet population preflight matrix: .*", line, text, flags=re.MULTILINE)
    else:
        marker = "- Lane promotion next-action queue:"
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
        "review-packet-forms/integrated-handoff-readiness metadata",
        "review-packet-forms/integrated-handoff-readiness/review-packet-population-preflight metadata",
    )
    text = text.replace("review-packet-population-preflight/review-packet-population-preflight metadata", "review-packet-population-preflight metadata")
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
    manifest["review_packet_population_preflight_matrix"] = {
        "status": document["status"],
        "artifact_markdown": OUT_MD.name,
        "artifact_json": OUT_JSON.name,
        "packet_groups": summary["packet_groups"],
        "lane_packet_groups": summary["lane_packet_groups"],
        "methodology_packet_groups": summary["methodology_packet_groups"],
        "reviewer_role_forms": summary["reviewer_role_forms"],
        "lane_reviewer_role_forms": summary["lane_reviewer_role_forms"],
        "methodology_reviewer_role_forms": summary["methodology_reviewer_role_forms"],
        "blocked_packet_groups": summary["blocked_packet_groups"],
        "packet_population_allowed_groups": summary["packet_population_allowed_groups"],
        "send_to_review_allowed_groups": summary["send_to_review_allowed_groups"],
        "ready_context_note_blocked_groups": summary["ready_context_note_blocked_groups"],
        "manual_source_review_blocked_groups": summary["manual_source_review_blocked_groups"],
        "source_discovery_blocked_groups": summary["source_discovery_blocked_groups"],
        "support_cohort_blocked_groups": summary["support_cohort_blocked_groups"],
        "methodology_blocked_groups": summary["methodology_blocked_groups"],
        "lane_work_units_blocking_population": summary["lane_work_units_blocking_population"],
        "methodology_actions_blocking_publication_review": summary["methodology_actions_blocking_publication_review"],
        "review_fields_filled": 0,
        "review_packets_sent": 0,
        "review_returns_received": 0,
        "external_reviews_performed": 0,
        "accepted_corrections_ingested": 0,
        "review_packet_population_performed": False,
        "translation_or_revision_performed": False,
        "canonical_completion_claim": False,
        "publication_completion_claim": False,
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
                "review_packet_population_preflight_json": str(OUT_JSON),
                "packet_groups": document["summary"]["packet_groups"],
                "blocked_packet_groups": document["summary"]["blocked_packet_groups"],
                "packet_population_allowed_groups": document["summary"]["packet_population_allowed_groups"],
                "reviewer_role_forms": document["summary"]["reviewer_role_forms"],
                "no_network_actions_performed": document["no_network_actions_performed"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
