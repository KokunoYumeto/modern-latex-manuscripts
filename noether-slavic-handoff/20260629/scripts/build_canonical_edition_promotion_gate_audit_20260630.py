import datetime
import hashlib
import json
import pathlib
import re


BASE = pathlib.Path(__file__).resolve().parents[1]
STATUS_MANIFEST = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_MANIFEST_20260629.json"
STATUS_INDEX = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_INDEX_20260629.md"
INTEGRATED_MATRIX_JSON = BASE / "INTEGRATED_LANE_HANDOFF_READINESS_MATRIX_20260630.json"
LANE_QUEUE_JSON = BASE / "LANE_PROMOTION_NEXT_ACTION_QUEUE_20260630.json"
RENDER_PREFLIGHT_JSON = BASE / "RENDER_SCRIPT_VALIDATION_PREFLIGHT_20260630.json"
PACKET_PREFLIGHT_JSON = BASE / "REVIEW_PACKET_POPULATION_PREFLIGHT_MATRIX_20260630.json"
REVIEW_RETURN_PREFLIGHT_JSON = BASE / "REVIEW_RETURN_CORRECTION_INGESTION_PREFLIGHT_20260630.json"
SYNC_LEDGER_JSON = BASE / "GITHUB_PC_BRANCH_SYNC_LEDGER_20260630.json"
OUT_JSON = BASE / "CANONICAL_EDITION_PROMOTION_GATE_AUDIT_20260630.json"
OUT_MD = BASE / "CANONICAL_EDITION_PROMOTION_GATE_AUDIT_20260630.md"
SELF_PATH = pathlib.Path(__file__).resolve()

STATUS = "canonical_edition_promotion_gate_audit_local_only_no_promotion"

PROMOTION_SEQUENCE = [
    "source_witness_gate",
    "term_anchor_or_source_discovery_gate",
    "page_context_or_manual_source_review_gate",
    "render_script_validation_gate",
    "external_review_packet_population_gate",
    "review_return_gate",
    "accepted_correction_ingestion_gate",
    "rebuild_and_manifest_gate",
    "github_or_release_handoff_gate",
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


def first_blocker_for_packet_missing_gate(missing_gate: str | None) -> str:
    mapping = {
        "page_context_notes_blank": "page_context_notes_not_filled",
        "manual_source_review_rows_unresolved": "manual_source_review_rows_unresolved",
        "source_discovery_not_promoted": "source_discovery_not_promoted_to_term_queue",
        "support_cohort_not_promoted_to_edition_lane": "support_cohort_not_edition_lane",
    }
    return mapping.get(missing_gate or "", "upstream_gate_not_cleared")


def build_edition_row(
    render_row: dict,
    integrated_by_id: dict[str, dict],
    packet_by_lane: dict[str, dict],
    return_by_lane: dict[str, dict],
    sync_summary: dict,
) -> dict:
    lane = render_row["lane_or_cohort"]
    integrated = integrated_by_id.get(lane, {})
    packet = packet_by_lane.get(lane, {})
    review_return = return_by_lane.get(lane, {})
    if lane == "slavic_reference":
        first_blocker = "prior_review_ready_lane_maintained_by_pointer_not_rebuilt_in_this_pc_branch"
        source_gate = "prior_checkpoint_pointer_available"
        term_gate = "prior_slavic_package_pointers_not_recomputed_here"
        page_or_manual_gate = "review_returns_or_new_source_corrections_only_if_received"
        packet_gate = "not_populated_in_this_pc_branch"
        review_return_gate = "ingest_future_returns_if_received"
    else:
        first_blocker = first_blocker_for_packet_missing_gate(packet.get("missing_gate"))
        source_gate = "selected_witnesses_present" if integrated.get("selected_witnesses", 0) > 0 else "source_witness_missing"
        if packet.get("missing_gate") == "source_discovery_not_promoted":
            term_gate = "source_discovery_required_before_term_anchor_queue"
        elif integrated.get("readiness_group") == "extension_cohort_support_not_edition_lane":
            term_gate = "support_cohort_evidence_only_not_term_anchor_lane"
        else:
            term_gate = "term_anchor_or_page_inspection_seed_present_not_approved"
        page_or_manual_gate = packet.get("missing_gate", "upstream_gate_not_cleared")
        packet_gate = "blocked_before_packet_population"
        review_return_gate = review_return.get("ingestion_blocker", "review_return_not_received")

    return {
        "gate_row_id": f"canonical-promotion-{lane.replace('_', '-')}",
        "lane_or_cohort": lane,
        "kind": render_row.get("kind"),
        "label": render_row.get("label"),
        "readiness_group": render_row.get("readiness_group"),
        "canonical_promotion_status": "blocked_or_maintenance_only_no_promotion",
        "canonical_promotion_allowed_now": False,
        "first_blocking_gate": first_blocker,
        "source_witness_gate": source_gate,
        "term_anchor_or_source_discovery_gate": term_gate,
        "page_context_or_manual_source_review_gate": page_or_manual_gate,
        "render_script_validation_gate": render_row.get("render_validation_status"),
        "external_review_packet_population_gate": packet_gate,
        "review_return_gate": review_return_gate,
        "accepted_correction_ingestion_gate": "accepted_corrections_zero",
        "rebuild_and_manifest_gate": "blocked_until_upstream_review_and_corrections_are_ingested",
        "github_or_release_handoff_gate": "local_sync_ledger_ready_no_remote_update",
        "render_script_profile": render_row.get("render_script_profile"),
        "writing_direction": render_row.get("writing_direction"),
        "selected_witnesses": render_row.get("selected_witnesses", 0),
        "selected_witnesses_with_source_core": render_row.get("selected_witnesses_with_source_core", 0),
        "authority_reviewer_role_forms": render_row.get("authority_reviewer_role_forms", 0),
        "visual_or_script_reviewer_roles": render_row.get("visual_or_script_reviewer_roles", []),
        "packet_population_allowed": packet.get("packet_population_allowed", False),
        "send_to_review_allowed": packet.get("send_to_review_allowed", False),
        "review_returns_received": review_return.get("review_returns_received", 0),
        "accepted_correction_rows_ingested": review_return.get("accepted_correction_rows_ingested", 0),
        "sync_payload_items_excluding_ledger": sync_summary.get("payload_items_excluding_this_ledger"),
        "promotion_sequence": PROMOTION_SEQUENCE,
        "render_jobs_started": 0,
        "pdfs_created": 0,
        "review_packet_population_performed": False,
        "review_packets_sent": 0,
        "review_returns_ingested": 0,
        "external_reviews_performed": 0,
        "accepted_corrections_ingested": 0,
        "translation_or_revision_performed": False,
        "source_text_copied": False,
        "source_language_terms_copied": False,
        "native_review_status": "not_reviewed",
        "canonical_approval_status": "not_approved",
        "canonical_completion_claim": False,
        "publication_completion_claim": False,
        "current_approved_terms": 0,
        "current_accepted_corrections": 0,
    }


def build_methodology_row(row: dict) -> dict:
    lane_type = row.get("lane_type")
    return {
        "gate_row_id": f"methodology-publication-{lane_type.replace('_', '-')}",
        "lane_type": lane_type,
        "queue_kind": row.get("queue_kind"),
        "publication_promotion_status": "blocked_no_authority_review_return",
        "publication_claim_allowed_now": False,
        "first_blocking_gate": row.get("missing_gate"),
        "methodology_authority_review_gate": row.get("missing_gate"),
        "review_return_gate": "review_return_not_received",
        "accepted_correction_ingestion_gate": "accepted_corrections_zero",
        "publication_completion_claim": False,
        "reviewer_role_forms": row.get("reviewer_role_forms", 0),
        "review_fields_filled": 0,
        "review_packets_sent": 0,
        "review_returns_received": 0,
        "external_reviews_performed": 0,
        "accepted_corrections_ingested": 0,
        "source_text_copied": False,
        "source_language_terms_copied": False,
        "native_review_status": "not_reviewed",
        "current_approved_terms": 0,
        "current_accepted_corrections": 0,
    }


def build_document() -> dict:
    manifest = load_json(STATUS_MANIFEST)
    integrated = load_json(INTEGRATED_MATRIX_JSON)
    lane_queue = load_json(LANE_QUEUE_JSON)
    render = load_json(RENDER_PREFLIGHT_JSON)
    packet_preflight = load_json(PACKET_PREFLIGHT_JSON)
    review_return = load_json(REVIEW_RETURN_PREFLIGHT_JSON)
    sync_ledger = load_json(SYNC_LEDGER_JSON)

    integrated_by_id = {row["lane_or_cohort"]: row for row in integrated["lane_or_cohort_rows"]}
    packet_by_lane = {
        row["lane_or_cohort"]: row
        for row in packet_preflight["preflight_rows"]
        if row.get("queue_group") == "lane_authority" and row.get("lane_or_cohort") is not None
    }
    return_by_lane = {
        row["lane_or_cohort"]: row
        for row in review_return["packet_ingestion_rows"]
        if row.get("lane_or_cohort") is not None
    }
    edition_rows = [
        build_edition_row(row, integrated_by_id, packet_by_lane, return_by_lane, sync_ledger)
        for row in render["preflight_rows"]
    ]
    methodology_rows = [
        build_methodology_row(row)
        for row in packet_preflight["preflight_rows"]
        if row.get("queue_group") == "methodology_authority"
    ]

    first_blockers: dict[str, int] = {}
    for row in edition_rows:
        key = row["first_blocking_gate"]
        first_blockers[key] = first_blockers.get(key, 0) + 1

    summary = {
        "edition_gate_rows": len(edition_rows),
        "slavic_reference_rows": sum(1 for row in edition_rows if row["lane_or_cohort"] == "slavic_reference"),
        "core_language_lane_rows": sum(1 for row in edition_rows if row.get("kind") == "core_language_lane"),
        "extension_cohort_rows": sum(1 for row in edition_rows if row.get("kind") == "extension_cohort"),
        "methodology_publication_gate_rows": len(methodology_rows),
        "canonical_promotion_allowed_rows": sum(1 for row in edition_rows if row["canonical_promotion_allowed_now"]),
        "publication_claim_allowed_rows": sum(1 for row in methodology_rows if row["publication_claim_allowed_now"]),
        "blocked_or_maintenance_rows": len(edition_rows),
        "first_blocking_gate_counts": first_blockers,
        "render_jobs_started": 0,
        "pdfs_created": 0,
        "review_packet_population_performed": False,
        "review_packets_sent": 0,
        "review_returns_received": 0,
        "external_reviews_performed": 0,
        "accepted_corrections_ingested": 0,
        "network_actions_performed": 0,
        "remote_pushes_performed": 0,
        "canonical_completion_claim": False,
        "publication_completion_claim": False,
        "native_review_status": "not_reviewed",
        "current_approved_terms": 0,
        "current_accepted_corrections": 0,
    }

    return {
        "artifact": "canonical_edition_promotion_gate_audit",
        "status": STATUS,
        "generated_date": "2026-06-30",
        "generated_utc": now_utc(),
        "bandwidth_mode": "local_only_no_network_actions",
        "inputs": {
            "status_manifest": STATUS_MANIFEST.name,
            "integrated_lane_handoff_readiness_matrix": INTEGRATED_MATRIX_JSON.name,
            "lane_promotion_next_action_queue": LANE_QUEUE_JSON.name,
            "render_script_validation_preflight": RENDER_PREFLIGHT_JSON.name,
            "review_packet_population_preflight": PACKET_PREFLIGHT_JSON.name,
            "review_return_correction_ingestion_preflight": REVIEW_RETURN_PREFLIGHT_JSON.name,
            "github_pc_branch_sync_ledger": SYNC_LEDGER_JSON.name,
        },
        "policy": {
            "source_witnesses_before_translation_or_revision": True,
            "term_anchors_are_not_term_approvals": True,
            "render_validation_before_canonical_pdf_claim": True,
            "external_review_before_native_acceptability_claim": True,
            "accepted_correction_ingestion_before_rebuild_or_completion_claim": True,
            "support_cohorts_are_not_edition_lanes_until_promoted": True,
            "local_sync_ledger_is_not_remote_push": True,
        },
        "summary": summary,
        "edition_gate_rows": edition_rows,
        "methodology_publication_gate_rows": methodology_rows,
        "boundaries": [
            "This audit records promotion blockers only; it does not promote any lane.",
            "The Slavic reference row is maintained by prior checkpoint pointers, not rebuilt or newly completed here.",
            "No review packet population, review return ingestion, accepted correction ingestion, render job, remote push, or publication claim was performed.",
            "It copies no source-language passages and no source-language term strings.",
            "No network action was performed.",
        ],
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
        "# Canonical Edition Promotion Gate Audit - 2026-06-30",
        "",
        "This local audit consolidates the current blockers before any lane can be promoted toward a canonical edition or publication claim. It is not a completion claim.",
        "",
        "## Summary",
        "",
        f"- Edition gate rows: {summary['edition_gate_rows']}",
        f"- Methodology publication gate rows: {summary['methodology_publication_gate_rows']}",
        f"- Canonical promotion allowed now: {summary['canonical_promotion_allowed_rows']}",
        f"- Publication claims allowed now: {summary['publication_claim_allowed_rows']}",
        "- Review packets sent: 0",
        "- Review returns received: 0",
        "- Accepted corrections ingested: 0",
        "- Render jobs started: 0",
        "- Remote pushes performed: 0",
        "",
        "## Edition Gates",
        "",
        "| Lane/cohort | Kind | First blocking gate | Render gate | Packet gate | Return gate |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for row in document["edition_gate_rows"]:
        lines.append(
            f"| {row['label']} | {row['kind']} | {row['first_blocking_gate']} | "
            f"{row['render_script_validation_gate']} | {row['external_review_packet_population_gate']} | "
            f"{row['review_return_gate']} |"
        )
    lines.extend(
        [
            "",
            "## Methodology Publication Gates",
            "",
            "| Lane type | First blocking gate | Reviewer forms |",
            "| --- | --- | --- |",
        ]
    )
    for row in document["methodology_publication_gate_rows"]:
        lines.append(f"| {row['lane_type']} | {row['first_blocking_gate']} | {row['reviewer_role_forms']} |")
    lines.extend(
        [
            "",
            "## Boundaries",
            "",
            "- This artifact does not populate review packets or ingest review returns.",
            "- Support cohorts remain outside canonical edition claims until explicitly promoted and reviewed.",
            "- Slavic work is maintained by prior checkpoint pointers in this local package.",
            "- No source text, source-language term strings, credentials, reviewer returns, or accepted corrections are copied here.",
            "- No network action was performed.",
            "",
        ]
    )
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def update_status_index(document: dict, manifest: dict) -> None:
    text = STATUS_INDEX.read_text(encoding="utf-8")
    summary = document["summary"]
    line = (
        "- Canonical edition promotion gate audit: "
        f"{summary['edition_gate_rows']} edition rows / "
        f"{summary['methodology_publication_gate_rows']} methodology rows / "
        "0 promotions"
    )
    if re.search(r"^- Canonical edition promotion gate audit: .*", text, flags=re.MULTILINE):
        text = re.sub(r"^- Canonical edition promotion gate audit: .*", line, text, flags=re.MULTILINE)
    else:
        marker = "- Render/script validation preflight:"
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
        "integrated-handoff-readiness/lane-promotion-next-action/support-cohort-authority-note/render-script-preflight metadata",
        "integrated-handoff-readiness/lane-promotion-next-action/support-cohort-authority-note/render-script-preflight/canonical-promotion-gate metadata",
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
    summary = document["summary"]
    manifest["canonical_edition_promotion_gate_audit"] = {
        "status": document["status"],
        "artifact_markdown": OUT_MD.name,
        "artifact_json": OUT_JSON.name,
        "edition_gate_rows": summary["edition_gate_rows"],
        "slavic_reference_rows": summary["slavic_reference_rows"],
        "core_language_lane_rows": summary["core_language_lane_rows"],
        "extension_cohort_rows": summary["extension_cohort_rows"],
        "methodology_publication_gate_rows": summary["methodology_publication_gate_rows"],
        "canonical_promotion_allowed_rows": summary["canonical_promotion_allowed_rows"],
        "publication_claim_allowed_rows": summary["publication_claim_allowed_rows"],
        "blocked_or_maintenance_rows": summary["blocked_or_maintenance_rows"],
        "render_jobs_started": 0,
        "pdfs_created": 0,
        "review_packet_population_performed": False,
        "review_packets_sent": 0,
        "review_returns_received": 0,
        "external_reviews_performed": 0,
        "accepted_corrections_ingested": 0,
        "network_actions_performed": 0,
        "remote_pushes_performed": 0,
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
    update_status_index(document, manifest)
    refresh_existing_artifact_hashes(manifest)
    write_json(STATUS_MANIFEST, manifest)


def main() -> None:
    document = build_document()
    write_json(OUT_JSON, document)
    write_markdown(document)
    update_manifest(document)
    print(
        json.dumps(
            {
                "canonical_edition_promotion_gate_audit_json": str(OUT_JSON),
                "edition_gate_rows": document["summary"]["edition_gate_rows"],
                "methodology_publication_gate_rows": document["summary"]["methodology_publication_gate_rows"],
                "canonical_promotion_allowed_rows": document["summary"]["canonical_promotion_allowed_rows"],
                "network_actions_performed": document["summary"]["network_actions_performed"],
                "no_network_actions_performed": document["no_network_actions_performed"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
