import datetime
import hashlib
import json
import pathlib
import re


BASE = pathlib.Path(__file__).resolve().parents[1]
STATUS_MANIFEST = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_MANIFEST_20260629.json"
STATUS_INDEX = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_INDEX_20260629.md"
CORRECTION_LEDGER_TEMPLATE_JSON = BASE / "ACCEPTED_CORRECTION_LEDGER_TEMPLATE_20260629.json"
AUTHORITY_FORMS_JSON = BASE / "EXTERNAL_AUTHORITY_REVIEW_PACKET_FORMS_20260630.json"
PREFLIGHT_MATRIX_JSON = BASE / "REVIEW_PACKET_POPULATION_PREFLIGHT_MATRIX_20260630.json"
OUT_JSON = BASE / "REVIEW_RETURN_CORRECTION_INGESTION_PREFLIGHT_20260630.json"
OUT_MD = BASE / "REVIEW_RETURN_CORRECTION_INGESTION_PREFLIGHT_20260630.md"
SELF_PATH = pathlib.Path(__file__).resolve()

STATUS = "review_return_correction_ingestion_preflight_no_returns_no_corrections"


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


def downstream_update_scope(form: dict) -> list[str]:
    lane_type = form.get("lane_type")
    queue_group = form.get("queue_group")
    lane = form.get("lane_or_cohort")
    scope = ["accepted correction ledger", "status manifest", "handoff index"]
    if queue_group == "methodology_authority":
        return scope + ["methodology publication crosswalk", "claim taxonomy and blocked-claim state"]
    if lane in {"french", "spanish", "simplified_chinese", "japanese", "arabic"}:
        return scope + ["term anchor seed", "glossary/rationale log", "TeX/PDF visual inspection note"]
    if lane in {"fa_IR", "prs_AF", "tg_Cyrl_TJ"} or lane_type == "multi_standard_or_multi_register_family_lane":
        return scope + ["register-specific term anchor seed", "cross-register authority note", "script/render inspection note"]
    if lane_type == "low_resource_or_under_served_educational_lane":
        return scope + ["support-cohort authority note", "promotion boundary note"]
    return scope + ["lane-specific artifact update"]


def rebuild_flags(form: dict) -> dict:
    queue_group = form.get("queue_group")
    lane = form.get("lane_or_cohort")
    if queue_group == "methodology_authority":
        return {
            "tex_rebuild_may_be_required": False,
            "pdf_visual_inspection_may_be_required": False,
            "manifest_update_required": True,
            "publication_claim_review_required": True,
        }
    return {
        "tex_rebuild_may_be_required": lane not in {"africa_deep_gap", "east_southeast_asia_pacific", "methodology_interlanguage_access", "pan_turkic_adjacent", "source_first_reference_textbooks", "south_asia_hindustani_indic_dravidian"},
        "pdf_visual_inspection_may_be_required": lane in {"simplified_chinese", "japanese", "arabic", "fa_IR", "prs_AF", "tg_Cyrl_TJ"},
        "manifest_update_required": True,
        "publication_claim_review_required": False,
    }


def build_form_rows(forms: dict, ledger: dict) -> list[dict]:
    rows = []
    required_fields = ledger.get("required_fields", [])
    for packet in forms.get("packet_groups_detail", []):
        for form in packet.get("forms", []):
            blank_fields = form.get("review_fields_blank", {})
            rows.append(
                {
                    "form_id": form["form_id"],
                    "packet_id": form["packet_id"],
                    "queue_id": form.get("queue_id"),
                    "queue_group": form.get("queue_group"),
                    "lane_or_cohort": form.get("lane_or_cohort"),
                    "lane_type": form.get("lane_type"),
                    "queue_kind": form.get("queue_kind"),
                    "reviewer_role": form.get("reviewer_role"),
                    "ledger_version": ledger.get("ledger_version"),
                    "required_ledger_fields": required_fields,
                    "required_ledger_field_count": len(required_fields),
                    "review_blank_fields_count": len(blank_fields),
                    "review_return_received": False,
                    "correction_rows_received": 0,
                    "accepted_correction_rows_ingested": 0,
                    "ingestion_allowed_now": False,
                    "ingestion_blocker": "review_return_not_received",
                    "downstream_update_scope": downstream_update_scope(form),
                    "rebuild_and_manifest_flags": rebuild_flags(form),
                    "ingestion_checklist": ledger.get("ingestion_checklist", []),
                    "allowed_issue_types": ledger.get("issue_types", []),
                    "allowed_severity_levels": ledger.get("severity_levels", []),
                    "allowed_correction_states": ledger.get("correction_states", []),
                    "review_packet_population_performed": False,
                    "translation_or_revision_performed": False,
                    "external_review_performed": False,
                    "accepted_corrections_ingested": False,
                    "source_text_copied": False,
                    "source_language_terms_copied": False,
                    "native_review_status": "not_reviewed",
                    "canonical_approval_status": "not_approved",
                }
            )
    return rows


def build_packet_rows(form_rows: list[dict]) -> list[dict]:
    packet_ids = sorted({row["packet_id"] for row in form_rows})
    rows = []
    for packet_id in packet_ids:
        packet_forms = [row for row in form_rows if row["packet_id"] == packet_id]
        first = packet_forms[0]
        rows.append(
            {
                "packet_id": packet_id,
                "queue_id": first.get("queue_id"),
                "queue_group": first.get("queue_group"),
                "lane_or_cohort": first.get("lane_or_cohort"),
                "lane_type": first.get("lane_type"),
                "queue_kind": first.get("queue_kind"),
                "reviewer_role_forms": len(packet_forms),
                "review_returns_received": 0,
                "correction_rows_received": 0,
                "accepted_correction_rows_ingested": 0,
                "ingestion_allowed_now": False,
                "ingestion_blocker": "review_return_not_received",
                "review_packet_population_performed": False,
                "external_reviews_performed": 0,
                "accepted_corrections_ingested": 0,
                "source_text_copied": False,
                "source_language_terms_copied": False,
                "native_review_status": "not_reviewed",
            }
        )
    return rows


def build_summary(form_rows: list[dict], packet_rows: list[dict], ledger: dict, forms: dict, preflight: dict) -> dict:
    return {
        "packet_groups": len(packet_rows),
        "lane_packet_groups": sum(1 for row in packet_rows if row["queue_group"] == "lane_authority"),
        "methodology_packet_groups": sum(1 for row in packet_rows if row["queue_group"] == "methodology_authority"),
        "reviewer_role_form_rows": len(form_rows),
        "lane_reviewer_role_form_rows": sum(1 for row in form_rows if row["queue_group"] == "lane_authority"),
        "methodology_reviewer_role_form_rows": sum(1 for row in form_rows if row["queue_group"] == "methodology_authority"),
        "ledger_required_fields": len(ledger.get("required_fields", [])),
        "issue_types": len(ledger.get("issue_types", [])),
        "severity_levels": len(ledger.get("severity_levels", [])),
        "correction_states": len(ledger.get("correction_states", [])),
        "ingestion_checklist_items": len(ledger.get("ingestion_checklist", [])),
        "lane_specific_ingestion_rules": len(ledger.get("lane_specific_ingestion_rules", [])),
        "review_packet_population_allowed_groups": preflight.get("summary", {}).get("packet_population_allowed_groups", 0),
        "review_packet_blocked_groups": preflight.get("summary", {}).get("blocked_packet_groups", 0),
        "review_returns_received": forms.get("summary", {}).get("review_returns_received", 0),
        "correction_rows_received": 0,
        "accepted_correction_rows_ingested": forms.get("summary", {}).get("accepted_corrections_ingested", 0),
        "ingestion_allowed_now_rows": 0,
        "ingestion_blocked_rows": len(form_rows),
        "review_fields_filled": forms.get("summary", {}).get("review_fields_filled", 0),
        "external_reviews_performed": forms.get("summary", {}).get("external_reviews_performed", 0),
        "review_packet_population_performed": False,
        "translation_or_revision_performed": False,
        "canonical_completion_claim": False,
        "publication_completion_claim": False,
        "native_review_status": "not_reviewed",
        "current_approved_terms": 0,
        "current_accepted_corrections": 0,
    }


def build_document(manifest: dict) -> dict:
    ledger = load_json(CORRECTION_LEDGER_TEMPLATE_JSON)
    forms = load_json(AUTHORITY_FORMS_JSON)
    preflight = load_json(PREFLIGHT_MATRIX_JSON)
    form_rows = build_form_rows(forms, ledger)
    packet_rows = build_packet_rows(form_rows)
    return {
        "artifact": "review_return_correction_ingestion_preflight",
        "generated_utc": now_utc(),
        "generated_date": "20260630",
        "status": STATUS,
        "bandwidth_mode": "local_only_no_network_actions",
        "inputs": {
            "status_manifest": STATUS_MANIFEST.name,
            "accepted_correction_ledger_template": CORRECTION_LEDGER_TEMPLATE_JSON.name,
            "external_authority_review_packet_forms": AUTHORITY_FORMS_JSON.name,
            "review_packet_population_preflight_matrix": PREFLIGHT_MATRIX_JSON.name,
        },
        "ingestion_policy": {
            "review_return_required_before_correction_ingestion": True,
            "ledger_required_fields_must_be_complete": True,
            "accepted_edits_require_rebuild_when_flagged": True,
            "manifest_update_required_for_accepted_corrections": True,
            "local_preflight_is_not_external_review": True,
            "rejected_or_blocked_decisions_preserved_with_rationale": True,
        },
        "summary": build_summary(form_rows, packet_rows, ledger, forms, preflight),
        "ledger_schema": {
            "ledger_version": ledger.get("ledger_version"),
            "required_fields": ledger.get("required_fields", []),
            "issue_types": ledger.get("issue_types", []),
            "severity_levels": ledger.get("severity_levels", []),
            "correction_states": ledger.get("correction_states", []),
            "ingestion_checklist": ledger.get("ingestion_checklist", []),
            "lane_specific_ingestion_rules": ledger.get("lane_specific_ingestion_rules", []),
        },
        "packet_ingestion_rows": packet_rows,
        "form_ingestion_rows": form_rows,
        "boundaries": {
            "local_ingestion_preflight_only": True,
            "review_returns_not_received": True,
            "accepted_corrections_not_ingested": True,
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
        "# Review-Return Correction Ingestion Preflight - 2026-06-30",
        "",
        f"Status: `{document['status']}`",
        "",
        "This preflight maps every blank reviewer-role form to the accepted-correction ledger schema and downstream rebuild/manifest gates. It records no review return and ingests no correction.",
        "",
        "## Summary",
        "",
        f"- Packet groups: {summary['packet_groups']} ({summary['lane_packet_groups']} lane, {summary['methodology_packet_groups']} methodology)",
        f"- Reviewer-role form rows: {summary['reviewer_role_form_rows']} ({summary['lane_reviewer_role_form_rows']} lane, {summary['methodology_reviewer_role_form_rows']} methodology)",
        f"- Ledger required fields: {summary['ledger_required_fields']}; issue types: {summary['issue_types']}; correction states: {summary['correction_states']}",
        f"- Review returns received: {summary['review_returns_received']}; accepted corrections ingested: {summary['accepted_correction_rows_ingested']}",
        f"- Ingestion blocked rows: {summary['ingestion_blocked_rows']}; allowed now: {summary['ingestion_allowed_now_rows']}",
        "- Review packet population: false; external review: not reviewed; completion claims: false",
        "",
        "## Packet Rows",
        "",
        "| Packet | Group | Lane/type | Forms | Ingestion | Blocker |",
        "|---|---|---|---:|---|---|",
    ]
    for row in document["packet_ingestion_rows"]:
        lane_or_type = row["lane_or_cohort"] or row["lane_type"]
        lines.append(
            f"| {row['packet_id']} | {row['queue_group']} | {lane_or_type} | {row['reviewer_role_forms']} | blocked | {row['ingestion_blocker']} |"
        )
    lines.extend(
        [
            "",
            "## Boundary Notes",
            "",
            "- This is not a review result and not an accepted-correction ledger.",
            "- It only states what must be present before a future review return can be ingested.",
            "- All current correction counts remain zero.",
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
        "- Review-return correction ingestion preflight: "
        f"{summary['reviewer_role_form_rows']} form rows / "
        f"{summary['ledger_required_fields']} ledger fields / "
        f"{summary['ingestion_blocked_rows']} blocked / "
        "0 corrections ingested"
    )
    if re.search(r"^- Review-return correction ingestion preflight: .*", text, flags=re.MULTILINE):
        text = re.sub(r"^- Review-return correction ingestion preflight: .*", line, text, flags=re.MULTILINE)
    else:
        marker = "- Review packet population preflight matrix:"
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
        "review-packet-population-preflight metadata",
        "review-packet-population-preflight/review-return-correction-ingestion-preflight metadata",
    )
    text = text.replace("review-return-correction-ingestion-preflight/review-return-correction-ingestion-preflight metadata", "review-return-correction-ingestion-preflight metadata")
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
    manifest["review_return_correction_ingestion_preflight"] = {
        "status": document["status"],
        "artifact_markdown": OUT_MD.name,
        "artifact_json": OUT_JSON.name,
        "packet_groups": summary["packet_groups"],
        "lane_packet_groups": summary["lane_packet_groups"],
        "methodology_packet_groups": summary["methodology_packet_groups"],
        "reviewer_role_form_rows": summary["reviewer_role_form_rows"],
        "lane_reviewer_role_form_rows": summary["lane_reviewer_role_form_rows"],
        "methodology_reviewer_role_form_rows": summary["methodology_reviewer_role_form_rows"],
        "ledger_required_fields": summary["ledger_required_fields"],
        "issue_types": summary["issue_types"],
        "severity_levels": summary["severity_levels"],
        "correction_states": summary["correction_states"],
        "ingestion_checklist_items": summary["ingestion_checklist_items"],
        "lane_specific_ingestion_rules": summary["lane_specific_ingestion_rules"],
        "review_packet_population_allowed_groups": summary["review_packet_population_allowed_groups"],
        "review_packet_blocked_groups": summary["review_packet_blocked_groups"],
        "review_returns_received": 0,
        "correction_rows_received": 0,
        "accepted_correction_rows_ingested": 0,
        "ingestion_allowed_now_rows": 0,
        "ingestion_blocked_rows": summary["ingestion_blocked_rows"],
        "review_fields_filled": 0,
        "external_reviews_performed": 0,
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
                "review_return_correction_ingestion_preflight_json": str(OUT_JSON),
                "reviewer_role_form_rows": document["summary"]["reviewer_role_form_rows"],
                "ledger_required_fields": document["summary"]["ledger_required_fields"],
                "ingestion_blocked_rows": document["summary"]["ingestion_blocked_rows"],
                "accepted_correction_rows_ingested": document["summary"]["accepted_correction_rows_ingested"],
                "no_network_actions_performed": document["no_network_actions_performed"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
