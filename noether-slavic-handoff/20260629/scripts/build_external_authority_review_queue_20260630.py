import datetime
import hashlib
import json
import pathlib
import re


BASE = pathlib.Path(__file__).resolve().parents[1]
STATUS_MANIFEST = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_MANIFEST_20260629.json"
STATUS_INDEX = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_INDEX_20260629.md"
INSPECTION_PACKET_JSON = BASE / "SELECTED_SOURCE_WITNESS_INSPECTION_PACKET_20260630.json"
MANUAL_PACKET_JSON = BASE / "MANUAL_SOURCE_REVIEW_PACKET_BLOCKED_LANES_20260630.json"
AUTHORITY_FRAMEWORK_JSON = BASE / "INTERLANGUAGE_REVIEWER_AUTHORITY_DECISION_FRAMEWORK_20260629.json"
METHODOLOGY_CROSSWALK_JSON = BASE / "METHODOLOGY_PUBLICATION_CROSSWALK_20260630.json"
OUT_JSON = BASE / "EXTERNAL_AUTHORITY_REVIEW_QUEUE_20260630.json"
OUT_MD = BASE / "EXTERNAL_AUTHORITY_REVIEW_QUEUE_20260630.md"
SELF_PATH = pathlib.Path(__file__).resolve()

STATUS = "external_authority_review_queue_no_review_performed_no_authority_claim"


READY_ROLES = {
    "french": [
        "native_or_near_native_french_mathematical_reviewer",
        "french_tex_pdf_visual_reviewer",
        "optional_undergraduate_algebra_or_physics_educator_reviewer",
    ],
    "japanese": [
        "native_japanese_mathematical_reviewer",
        "japanese_cjk_tex_pdf_visual_reviewer",
        "optional_undergraduate_algebra_or_physics_educator_reviewer",
    ],
}

SOURCE_DISCOVERY_ROLES = {
    "tg_Cyrl_TJ": [
        "tajik_cyrillic_mathematical_reviewer",
        "persianate_cross_register_reviewer",
        "source_language_discovery_reviewer",
    ],
}

SUPPORT_ROLES = {
    "africa_deep_gap": [
        "local_language_community_or_educator_reviewer",
        "care_trust_ethics_reviewer",
        "mathematical_register_reviewer",
    ],
    "east_southeast_asia_pacific": [
        "regional_language_family_reviewer",
        "mathematical_register_reviewer",
        "optional_undergraduate_educator_reviewer",
    ],
    "methodology_interlanguage_access": [
        "interlinguistics_research_reviewer",
        "constructed_language_methodology_reviewer",
        "open_source_handoff_ethics_reviewer",
    ],
    "pan_turkic_adjacent": [
        "turkic_language_family_reviewer",
        "script_standardization_reviewer",
        "mathematical_register_reviewer",
    ],
    "source_first_reference_textbooks": [
        "undergraduate_math_or_physics_educator_reviewer",
        "source_quality_reviewer",
        "open_educational_resources_reviewer",
    ],
    "south_asia_hindustani_indic_dravidian": [
        "south_asia_register_reviewer",
        "indic_dravidian_or_hindustani_language_reviewer",
        "mathematical_register_reviewer",
    ],
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


def manual_role_map(manual_packet: dict) -> dict[str, dict]:
    return {row.get("lane"): row for row in manual_packet.get("lane_packets", [])}


def queue_type(lane: str, kind_counts: dict) -> str:
    if "ready_context_note_entry" in kind_counts:
        return "ready_context_note_external_review_after_notes"
    if "manual_source_review_resolution" in kind_counts:
        return "manual_source_review_external_authority"
    if "source_discovery_promotion" in kind_counts:
        return "source_discovery_external_authority"
    if "support_cohort_authority_note" in kind_counts:
        return "support_cohort_authority_review"
    return "unclassified_external_authority_review"


def lane_type_for_queue(lane: str, queue_kind: str) -> str:
    if lane in {"fa_IR", "prs_AF", "tg_Cyrl_TJ"}:
        return "multi_standard_or_multi_register_family_lane"
    if queue_kind == "support_cohort_authority_review":
        return "low_resource_or_under_served_educational_lane"
    return "natural_language_translation_lane"


def roles_for_lane(lane: str, queue_kind: str, manual_by_lane: dict) -> list[str]:
    if lane in manual_by_lane:
        return list(manual_by_lane[lane].get("required_reviewer_roles", []))
    if lane in READY_ROLES:
        return READY_ROLES[lane]
    if lane in SOURCE_DISCOVERY_ROLES:
        return SOURCE_DISCOVERY_ROLES[lane]
    if lane in SUPPORT_ROLES:
        return SUPPORT_ROLES[lane]
    return ["external_language_or_methodology_reviewer"]


def build_lane_queue_rows(inspection: dict, manual_packet: dict) -> list[dict]:
    manual_by_lane = manual_role_map(manual_packet)
    rows = []
    for lane_summary in inspection.get("lane_summaries", []):
        lane = lane_summary.get("lane_or_cohort")
        kind_counts = lane_summary.get("task_kind_counts", {})
        queue_kind = queue_type(lane, kind_counts)
        manual_info = manual_by_lane.get(lane, {})
        roles = roles_for_lane(lane, queue_kind, manual_by_lane)
        rows.append(
            {
                "queue_id": f"external-authority-{lane}",
                "lane_or_cohort": lane,
                "queue_kind": queue_kind,
                "lane_type": lane_type_for_queue(lane, queue_kind),
                "inspection_tasks": lane_summary.get("inspection_tasks", 0),
                "witness_task_links": lane_summary.get("witness_task_links", 0),
                "manual_source_review_rows": manual_info.get("manual_source_review_rows", 0),
                "task_kind_counts": kind_counts,
                "required_reviewer_roles": roles,
                "required_reviewer_role_count": len(roles),
                "extra_checks": manual_info.get("lane_extra_checks", []),
                "authority_gate": "external_review_required_before_stronger_claims",
                "blocked_claims": [
                    "native_acceptability",
                    "canonical_terminology_approval",
                    "canonical_edition_completion",
                    "learner_facing_publication_without_review",
                ],
                "review_fields_blank": {
                    "external_reviewer_identity_or_role": None,
                    "review_date": None,
                    "authority_scope": None,
                    "accepted_corrections_ledger_pointer": None,
                    "remaining_blockers": None,
                },
                "external_review_performed": False,
                "accepted_corrections_ingested": False,
                "review_packet_population_performed": False,
                "translation_or_revision_performed": False,
                "source_text_copied": False,
                "source_language_terms_copied": False,
                "native_review_status": "not_reviewed",
                "canonical_approval_status": "not_approved",
            }
        )
    return rows


def build_methodology_rows(authority: dict, crosswalk: dict) -> list[dict]:
    rows = []
    for checklist in authority.get("review_authority_checklists", []):
        lane_type = checklist.get("lane_type")
        rows.append(
            {
                "queue_id": f"methodology-authority-{lane_type}",
                "lane_type": lane_type,
                "queue_kind": "methodology_publication_authority_review",
                "requirements": checklist.get("requirements", []),
                "required_reviewer_roles": methodology_roles(lane_type),
                "required_reviewer_role_count": len(methodology_roles(lane_type)),
                "claim_taxonomy_rows_relevant": crosswalk.get("summary", {}).get("claim_taxonomy_rows", 0),
                "authority_gate": "methodology_claim_review_required_before_publication_claim",
                "blocked_claims": [
                    "publication_completion",
                    "authority_model_sufficiency",
                    "community_consent_or_ownership_claim",
                ],
                "review_fields_blank": {
                    "external_methodology_reviewer": None,
                    "review_date": None,
                    "claim_scope_authorized": None,
                    "required_revisions": None,
                },
                "external_review_performed": False,
                "accepted_corrections_ingested": False,
                "publication_completion_claim": False,
                "source_text_copied": False,
                "source_language_terms_copied": False,
                "native_review_status": "not_reviewed",
            }
        )
    return rows


def methodology_roles(lane_type: str) -> list[str]:
    if lane_type == "natural_language_translation_lane":
        return ["translation_studies_reviewer", "technical_mathematics_reviewer"]
    if lane_type == "multi_standard_or_multi_register_family_lane":
        return ["language_policy_reviewer", "multi_register_language_family_reviewer"]
    if lane_type == "zonal_or_interlanguage_lane":
        return ["interlinguistics_reviewer", "language_community_or_project_authority_reviewer"]
    if lane_type == "constructed_language_pilot":
        return ["constructed_language_pedagogy_reviewer", "ethics_and_opt_in_deployment_reviewer"]
    if lane_type == "low_resource_or_under_served_educational_lane":
        return ["care_trust_ethics_reviewer", "local_education_context_reviewer"]
    if lane_type == "computational_interlingua_or_mt_pivot":
        return ["nlp_evaluation_reviewer", "human_facing_text_review_reviewer"]
    return ["methodology_reviewer"]


def role_summary(rows: list[dict]) -> list[dict]:
    counts: dict[str, dict[str, int]] = {}
    for row in rows:
        for role in row.get("required_reviewer_roles", []):
            bucket = counts.setdefault(role, {"queue_rows": 0, "inspection_tasks": 0})
            bucket["queue_rows"] += 1
            bucket["inspection_tasks"] += int(row.get("inspection_tasks") or 0)
    return [
        {"role": role, "queue_rows": counts[role]["queue_rows"], "inspection_tasks": counts[role]["inspection_tasks"]}
        for role in sorted(counts)
    ]


def build_document(manifest: dict) -> dict:
    inspection = load_json(INSPECTION_PACKET_JSON)
    manual_packet = load_json(MANUAL_PACKET_JSON)
    authority = load_json(AUTHORITY_FRAMEWORK_JSON)
    crosswalk = load_json(METHODOLOGY_CROSSWALK_JSON)
    lane_rows = build_lane_queue_rows(inspection, manual_packet)
    methodology_rows = build_methodology_rows(authority, crosswalk)
    all_rows = lane_rows + methodology_rows
    roles = role_summary(all_rows)
    return {
        "artifact": "external_authority_review_queue",
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
            "selected_witness_inspection_packet": INSPECTION_PACKET_JSON.name,
            "manual_source_review_packet": MANUAL_PACKET_JSON.name,
            "interlanguage_reviewer_authority_framework": AUTHORITY_FRAMEWORK_JSON.name,
            "methodology_publication_crosswalk": METHODOLOGY_CROSSWALK_JSON.name,
            "status_manifest": STATUS_MANIFEST.name,
        },
        "summary": {
            "lane_authority_queue_rows": len(lane_rows),
            "methodology_authority_queue_rows": len(methodology_rows),
            "total_authority_queue_rows": len(all_rows),
            "inspection_tasks_covered": inspection.get("summary", {}).get("inspection_task_count", 0),
            "ready_context_note_tasks": inspection.get("summary", {}).get("ready_context_note_tasks", 0),
            "manual_source_review_tasks": inspection.get("summary", {}).get("manual_source_review_tasks", 0),
            "source_discovery_tasks": inspection.get("summary", {}).get("source_discovery_tasks", 0),
            "support_cohort_tasks": inspection.get("summary", {}).get("support_cohort_tasks", 0),
            "manual_source_review_rows": manual_packet.get("totals", {}).get("manual_source_review_rows", 0),
            "required_reviewer_role_rows": len(roles),
            "review_fields_filled": 0,
            "external_reviews_performed": 0,
            "accepted_corrections_ingested": 0,
            "canonical_completion_claim": False,
            "publication_completion_claim": False,
            "review_packet_population_performed": False,
            "translation_or_revision_performed": False,
            "native_review_status": "not_reviewed",
            "current_approved_terms": 0,
            "current_accepted_corrections": 0,
        },
        "lane_authority_queue_rows": lane_rows,
        "methodology_authority_queue_rows": methodology_rows,
        "required_reviewer_role_summary": roles,
        "queue_rules": [
            "External authority review is required before stronger language, pedagogy, or canonical-edition claims.",
            "Blank inspection tasks are not completed review.",
            "Accepted corrections must be ingested into ledgers before status promotion.",
            "Constructed and semi-constructed language work remains methodology or pilot work without explicit authority review.",
        ],
        "boundaries": [
            "This queue copies no source-language passages and no source-language term strings.",
            "No external review was performed and no review fields were filled.",
            "No accepted corrections were ingested.",
            "No translation, revision, or reviewer-packet population was performed.",
            "No network action was performed.",
        ],
    }


def write_markdown(document: dict) -> None:
    summary = document["summary"]
    lines = [
        "# External authority review queue - 2026-06-30",
        "",
        "Status: blank authority-review queue only. No external review, correction ingestion, translation, or source-passage copying was performed.",
        "",
        "## Summary",
        "",
        f"- Lane authority queue rows: {summary['lane_authority_queue_rows']}",
        f"- Methodology authority queue rows: {summary['methodology_authority_queue_rows']}",
        f"- Inspection tasks covered: {summary['inspection_tasks_covered']}",
        f"- Manual/source-review rows: {summary['manual_source_review_rows']}",
        f"- Required reviewer role rows: {summary['required_reviewer_role_rows']}",
        f"- External reviews performed: {summary['external_reviews_performed']}",
        f"- Accepted corrections ingested: {summary['accepted_corrections_ingested']}",
        "",
        "## Lane Queue",
        "",
        "| Lane/cohort | Queue kind | Tasks | Manual rows | Roles |",
        "| --- | --- | ---: | ---: | ---: |",
    ]
    for row in document["lane_authority_queue_rows"]:
        lines.append(
            f"| `{row['lane_or_cohort']}` | `{row['queue_kind']}` | {row['inspection_tasks']} | {row['manual_source_review_rows']} | {row['required_reviewer_role_count']} |"
        )
    lines.extend(["", "## Methodology Queue", ""])
    lines.extend(
        f"- `{row['lane_type']}`: {row['required_reviewer_role_count']} reviewer roles / completion claim `{str(row.get('publication_completion_claim', False)).lower()}`"
        for row in document["methodology_authority_queue_rows"]
    )
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
        "- External authority review queue: "
        f"{summary['lane_authority_queue_rows']} lane rows / "
        f"{summary['methodology_authority_queue_rows']} methodology rows / "
        f"{summary['required_reviewer_role_rows']} reviewer role rows / "
        "0 network actions"
    )
    if re.search(r"^- External authority review queue: .*", text, flags=re.MULTILINE):
        text = re.sub(r"^- External authority review queue: .*", line, text, flags=re.MULTILINE)
    else:
        marker = "- Methodology publication crosswalk:"
        rows = text.splitlines()
        for offset, row in enumerate(rows):
            if row.startswith(marker):
                rows.insert(offset + 1, line)
                text = "\n".join(rows) + "\n"
                break
    text = text.replace(
        "methodology-publication-crosswalk metadata",
        "methodology-publication-crosswalk/external-authority-review-queue metadata",
    )
    text = text.replace(
        "external-authority-review-queue/external-authority-review-queue metadata",
        "external-authority-review-queue metadata",
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
    manifest["external_authority_review_queue"] = {
        "status": document["status"],
        "artifact_markdown": OUT_MD.name,
        "artifact_json": OUT_JSON.name,
        "lane_authority_queue_rows": summary["lane_authority_queue_rows"],
        "methodology_authority_queue_rows": summary["methodology_authority_queue_rows"],
        "total_authority_queue_rows": summary["total_authority_queue_rows"],
        "inspection_tasks_covered": summary["inspection_tasks_covered"],
        "ready_context_note_tasks": summary["ready_context_note_tasks"],
        "manual_source_review_tasks": summary["manual_source_review_tasks"],
        "source_discovery_tasks": summary["source_discovery_tasks"],
        "support_cohort_tasks": summary["support_cohort_tasks"],
        "manual_source_review_rows": summary["manual_source_review_rows"],
        "required_reviewer_role_rows": summary["required_reviewer_role_rows"],
        "review_fields_filled": 0,
        "external_reviews_performed": 0,
        "accepted_corrections_ingested": 0,
        "canonical_completion_claim": False,
        "publication_completion_claim": False,
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
                "external_authority_review_queue_json": str(OUT_JSON),
                "lane_authority_queue_rows": document["summary"]["lane_authority_queue_rows"],
                "methodology_authority_queue_rows": document["summary"]["methodology_authority_queue_rows"],
                "inspection_tasks_covered": document["summary"]["inspection_tasks_covered"],
                "required_reviewer_role_rows": document["summary"]["required_reviewer_role_rows"],
                "external_reviews_performed": document["summary"]["external_reviews_performed"],
                "no_network_actions_performed": document["no_network_actions_performed"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
