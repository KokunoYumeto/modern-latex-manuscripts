import datetime
import hashlib
import json
import pathlib
import re


BASE = pathlib.Path(__file__).resolve().parents[1]
STATUS_MANIFEST = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_MANIFEST_20260629.json"
STATUS_INDEX = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_INDEX_20260629.md"
AUTHORITY_QUEUE_JSON = BASE / "EXTERNAL_AUTHORITY_REVIEW_QUEUE_20260630.json"
REVIEW_TEMPLATES_JSON = BASE / "MULTILINGUAL_REVIEW_PACKET_TEMPLATES_20260629.json"
CORRECTION_LEDGER_TEMPLATE_JSON = BASE / "ACCEPTED_CORRECTION_LEDGER_TEMPLATE_20260629.json"
REVIEW_SCAFFOLDS_JSON = BASE / "REVIEW_PACKET_SCAFFOLDS_20260629.json"
OUT_JSON = BASE / "EXTERNAL_AUTHORITY_REVIEW_PACKET_FORMS_20260630.json"
OUT_MD = BASE / "EXTERNAL_AUTHORITY_REVIEW_PACKET_FORMS_20260630.md"
SELF_PATH = pathlib.Path(__file__).resolve()

STATUS = "external_authority_review_packet_forms_blank_no_review_result"


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


def blank_review_fields() -> dict[str, None]:
    return {
        "reviewer_identity_or_role_confirmation": None,
        "review_date": None,
        "artifact_hash_reviewed": None,
        "authority_scope": None,
        "approval_decision": None,
        "required_corrections_summary": None,
        "accepted_correction_ids": None,
        "remaining_blockers": None,
    }


def packet_id(queue_row: dict) -> str:
    return "authority-packet-" + queue_row["queue_id"].replace("_", "-").replace("external-authority-", "")


def form_id(queue_row: dict, role: str, index: int) -> str:
    safe_role = re.sub(r"[^a-z0-9]+", "-", role.lower()).strip("-")
    return f"{packet_id(queue_row)}-role-{index:02d}-{safe_role}"


def build_forms_for_row(queue_row: dict, queue_group: str, ledger_required_fields: list[str]) -> list[dict]:
    forms = []
    for index, role in enumerate(queue_row.get("required_reviewer_roles", []), start=1):
        forms.append(
            {
                "form_id": form_id(queue_row, role, index),
                "packet_id": packet_id(queue_row),
                "queue_id": queue_row.get("queue_id"),
                "queue_group": queue_group,
                "lane_or_cohort": queue_row.get("lane_or_cohort"),
                "lane_type": queue_row.get("lane_type"),
                "queue_kind": queue_row.get("queue_kind"),
                "reviewer_role": role,
                "review_form_status": "blank_not_sent_not_reviewed",
                "inspection_tasks": queue_row.get("inspection_tasks", 0),
                "manual_source_review_rows": queue_row.get("manual_source_review_rows", 0),
                "authority_gate": queue_row.get("authority_gate"),
                "blocked_claims": queue_row.get("blocked_claims", []),
                "extra_checks": queue_row.get("extra_checks", []),
                "requirements": queue_row.get("requirements", []),
                "review_fields_blank": blank_review_fields(),
                "accepted_correction_ledger_required_fields": ledger_required_fields,
                "external_review_performed": False,
                "review_packet_sent": False,
                "review_return_received": False,
                "accepted_corrections_ingested": False,
                "review_packet_population_performed": False,
                "translation_or_revision_performed": False,
                "source_text_copied": False,
                "source_language_terms_copied": False,
                "native_review_status": "not_reviewed",
                "canonical_approval_status": "not_approved",
            }
        )
    return forms


def build_packet_groups(queue_rows: list[dict], queue_group: str, ledger_required_fields: list[str]) -> list[dict]:
    groups = []
    for row in queue_rows:
        forms = build_forms_for_row(row, queue_group, ledger_required_fields)
        groups.append(
            {
                "packet_id": packet_id(row),
                "queue_id": row.get("queue_id"),
                "queue_group": queue_group,
                "lane_or_cohort": row.get("lane_or_cohort"),
                "lane_type": row.get("lane_type"),
                "queue_kind": row.get("queue_kind"),
                "reviewer_role_forms": len(forms),
                "review_packet_status": "blank_not_sent_not_reviewed",
                "forms": forms,
                "review_fields_filled": 0,
                "external_reviews_performed": 0,
                "accepted_corrections_ingested": 0,
                "review_packet_sent": False,
                "review_return_received": False,
                "review_packet_population_performed": False,
                "translation_or_revision_performed": False,
                "source_text_copied": False,
                "source_language_terms_copied": False,
                "native_review_status": "not_reviewed",
                "canonical_approval_status": "not_approved",
            }
        )
    return groups


def flatten_forms(groups: list[dict]) -> list[dict]:
    return [form for group in groups for form in group.get("forms", [])]


def build_document(manifest: dict) -> dict:
    queue = load_json(AUTHORITY_QUEUE_JSON)
    templates = load_json(REVIEW_TEMPLATES_JSON)
    ledger = load_json(CORRECTION_LEDGER_TEMPLATE_JSON)
    scaffolds = load_json(REVIEW_SCAFFOLDS_JSON)
    ledger_fields = ledger.get("required_fields", [])
    lane_groups = build_packet_groups(queue.get("lane_authority_queue_rows", []), "lane_authority", ledger_fields)
    methodology_groups = build_packet_groups(
        queue.get("methodology_authority_queue_rows", []), "methodology_authority", ledger_fields
    )
    all_groups = lane_groups + methodology_groups
    all_forms = flatten_forms(all_groups)
    lane_forms = flatten_forms(lane_groups)
    methodology_forms = flatten_forms(methodology_groups)
    distinct_roles = sorted({form["reviewer_role"] for form in all_forms})
    return {
        "artifact": "external_authority_review_packet_forms",
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
            "external_authority_review_queue": AUTHORITY_QUEUE_JSON.name,
            "multilingual_review_packet_templates": REVIEW_TEMPLATES_JSON.name,
            "accepted_correction_ledger_template": CORRECTION_LEDGER_TEMPLATE_JSON.name,
            "review_packet_scaffolds": REVIEW_SCAFFOLDS_JSON.name,
            "status_manifest": STATUS_MANIFEST.name,
        },
        "template_context": {
            "common_packet_structure": templates.get("common_packet_structure", []),
            "review_return_schema": templates.get("review_return_schema", []),
            "accepted_correction_ledger_version": ledger.get("ledger_version"),
            "accepted_correction_required_fields": ledger_fields,
            "source_scaffold_work_items": scaffolds.get("totals", {}).get("work_items", 0),
            "source_scaffold_packet_rows_populated": scaffolds.get("totals", {}).get("packet_rows_populated", 0),
        },
        "summary": {
            "packet_groups": len(all_groups),
            "lane_packet_groups": len(lane_groups),
            "methodology_packet_groups": len(methodology_groups),
            "reviewer_role_forms": len(all_forms),
            "lane_reviewer_role_forms": len(lane_forms),
            "methodology_reviewer_role_forms": len(methodology_forms),
            "distinct_reviewer_roles": len(distinct_roles),
            "inspection_tasks_covered": queue.get("summary", {}).get("inspection_tasks_covered", 0),
            "manual_source_review_rows": queue.get("summary", {}).get("manual_source_review_rows", 0),
            "review_fields_filled": 0,
            "review_packets_sent": 0,
            "review_returns_received": 0,
            "external_reviews_performed": 0,
            "accepted_corrections_ingested": 0,
            "review_packet_population_performed": False,
            "translation_or_revision_performed": False,
            "canonical_completion_claim": False,
            "publication_completion_claim": False,
            "native_review_status": "not_reviewed",
            "current_approved_terms": 0,
            "current_accepted_corrections": 0,
        },
        "packet_groups_detail": all_groups,
        "distinct_reviewer_roles": distinct_roles,
        "handoff_rules": [
            "Each form is blank and must be filled by an external reviewer before authority claims change.",
            "Accepted corrections must be recorded with the accepted-correction ledger schema before edits are applied.",
            "Review packet population remains blocked where prerequisite note or manual-source-review fields are blank.",
            "Methodology authority review is separate from language-lane mathematical/native review.",
        ],
        "boundaries": [
            "No external review was performed and no packet was sent.",
            "No review-return data or accepted correction was ingested.",
            "No source-language passages or source-language term strings are copied.",
            "No translation, revision, or reviewer-packet population was performed.",
            "No network action was performed.",
        ],
    }


def write_markdown(document: dict) -> None:
    summary = document["summary"]
    lines = [
        "# External authority review packet forms - 2026-06-30",
        "",
        "Status: blank packet forms only. No packet was sent, no review was performed, and no source-passage copying occurred.",
        "",
        "## Summary",
        "",
        f"- Packet groups: {summary['packet_groups']}",
        f"- Lane packet groups: {summary['lane_packet_groups']}",
        f"- Methodology packet groups: {summary['methodology_packet_groups']}",
        f"- Reviewer-role form instances: {summary['reviewer_role_forms']}",
        f"- Distinct reviewer roles: {summary['distinct_reviewer_roles']}",
        f"- Inspection tasks covered: {summary['inspection_tasks_covered']}",
        f"- Review packets sent/reviews performed/corrections ingested: {summary['review_packets_sent']} / {summary['external_reviews_performed']} / {summary['accepted_corrections_ingested']}",
        "",
        "## Packet Groups",
        "",
        "| Packet | Group | Lane/type | Kind | Forms |",
        "| --- | --- | --- | --- | ---: |",
    ]
    for group in document["packet_groups_detail"]:
        lane_or_type = group.get("lane_or_cohort") or group.get("lane_type")
        lines.append(
            f"| `{group['packet_id']}` | `{group['queue_group']}` | `{lane_or_type}` | `{group['queue_kind']}` | {group['reviewer_role_forms']} |"
        )
    lines.extend(["", "## Handoff Rules", ""])
    lines.extend(f"- {rule}" for rule in document["handoff_rules"])
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
        "- External authority review packet forms: "
        f"{summary['packet_groups']} packet groups / "
        f"{summary['reviewer_role_forms']} blank reviewer-role forms / "
        f"{summary['distinct_reviewer_roles']} distinct reviewer roles / "
        "0 network actions"
    )
    if re.search(r"^- External authority review packet forms: .*", text, flags=re.MULTILINE):
        text = re.sub(r"^- External authority review packet forms: .*", line, text, flags=re.MULTILINE)
    else:
        marker = "- External authority review queue:"
        rows = text.splitlines()
        for offset, row in enumerate(rows):
            if row.startswith(marker):
                rows.insert(offset + 1, line)
                text = "\n".join(rows) + "\n"
                break
    text = text.replace(
        "external-authority-review-queue metadata",
        "external-authority-review-queue/review-packet-forms metadata",
    )
    text = text.replace("review-packet-forms/review-packet-forms metadata", "review-packet-forms metadata")
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
    manifest["external_authority_review_packet_forms"] = {
        "status": document["status"],
        "artifact_markdown": OUT_MD.name,
        "artifact_json": OUT_JSON.name,
        "packet_groups": summary["packet_groups"],
        "lane_packet_groups": summary["lane_packet_groups"],
        "methodology_packet_groups": summary["methodology_packet_groups"],
        "reviewer_role_forms": summary["reviewer_role_forms"],
        "lane_reviewer_role_forms": summary["lane_reviewer_role_forms"],
        "methodology_reviewer_role_forms": summary["methodology_reviewer_role_forms"],
        "distinct_reviewer_roles": summary["distinct_reviewer_roles"],
        "inspection_tasks_covered": summary["inspection_tasks_covered"],
        "manual_source_review_rows": summary["manual_source_review_rows"],
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
                "external_authority_review_packet_forms_json": str(OUT_JSON),
                "packet_groups": document["summary"]["packet_groups"],
                "reviewer_role_forms": document["summary"]["reviewer_role_forms"],
                "distinct_reviewer_roles": document["summary"]["distinct_reviewer_roles"],
                "review_packets_sent": document["summary"]["review_packets_sent"],
                "external_reviews_performed": document["summary"]["external_reviews_performed"],
                "no_network_actions_performed": document["no_network_actions_performed"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
