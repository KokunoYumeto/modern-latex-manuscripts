import datetime
import hashlib
import json
import pathlib
import re
from collections import Counter, defaultdict


BASE = pathlib.Path(__file__).resolve().parents[1]
STATUS_MANIFEST = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_MANIFEST_20260629.json"
STATUS_INDEX = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_INDEX_20260629.md"
CANDIDATE_FORMS_JSON = BASE / "CONTEXT_NOTE_CANDIDATE_FILLED_FORMS_FRENCH_JAPANESE_20260630.json"
PREFLIGHT_JSON = BASE / "REVIEW_PACKET_POPULATION_PREFLIGHT_MATRIX_20260630.json"
OUT_JSON = BASE / "CONTEXT_NOTE_CONFIRMATION_APPLY_QUEUE_FRENCH_JAPANESE_20260630.json"
OUT_MD = BASE / "CONTEXT_NOTE_CONFIRMATION_APPLY_QUEUE_FRENCH_JAPANESE_20260630.md"
SELF_PATH = pathlib.Path(__file__).resolve()

STATUS = "context_note_confirmation_apply_queue_pending_no_application_no_packet_population"


LANE_CONFIRMATION_ROLES = {
    "french": [
        "native_or_near_native_french_mathematical_reviewer",
        "optional_undergraduate_algebra_or_physics_educator_reviewer",
    ],
    "japanese": [
        "native_japanese_mathematical_reviewer",
        "japanese_cjk_tex_pdf_visual_reviewer",
    ],
}

LANE_SPECIFIC_CHECKS = {
    "french": [
        "confirm standard French mathematical register",
        "flag literal calques or regional/institutional style constraints",
    ],
    "japanese": [
        "confirm standard Japanese mathematical register",
        "flag script balance, line-breaking, and CJK TeX/PDF readability constraints",
    ],
}


def now_utc() -> str:
    return datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="microseconds")


def sha256_path(path: pathlib.Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def sha256_json(data: object) -> str:
    payload = json.dumps(data, ensure_ascii=True, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest().upper()


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
        if row.get("lane_or_cohort") in {"french", "japanese"}
    }


def queue_item(candidate: dict, preflight_row: dict) -> dict:
    lane = candidate["language_lane"]
    checks = [
        "confirm the candidate context note is source-safe and contains no quotation",
        "confirm mathematical scope against the English concept and domain",
        "confirm reviewer question is answerable by the intended reviewer role",
        "confirm packet-population decision remains conservative until application",
    ] + LANE_SPECIFIC_CHECKS[lane]
    note_hash = sha256_json(candidate["candidate_note_values"])
    return {
        "queue_item_id": f"confirm-apply-{candidate['candidate_form_id']}",
        "candidate_form_id": candidate["candidate_form_id"],
        "source_form_id": candidate["source_form_id"],
        "term_id": candidate["term_id"],
        "language_lane": lane,
        "english_concept": candidate["english_concept"],
        "mathematical_domain": candidate["mathematical_domain"],
        "priority": candidate["priority"],
        "pages_checked": candidate["pages_checked"],
        "pages_with_exact_term_occurrence": candidate["pages_with_exact_term_occurrence"],
        "candidate_note_values_sha256": note_hash,
        "candidate_fields_filled": candidate["candidate_fields_filled"],
        "confirmation_status": "pending_human_confirmation",
        "confirmation_checks": checks,
        "suggested_confirmation_roles": LANE_CONFIRMATION_ROLES[lane],
        "apply_status": "blocked_until_human_confirmation",
        "application_allowed_now": False,
        "target_after_confirmation": "apply_or_revise_candidate_values_in_page_context_note_capture_forms",
        "preflight_packet_id": preflight_row.get("packet_id"),
        "preflight_missing_gate": preflight_row.get("missing_gate"),
        "preflight_packet_population_allowed": preflight_row.get("packet_population_allowed"),
        "preflight_send_to_review_allowed": preflight_row.get("send_to_review_allowed"),
        "review_packet_population_performed": False,
        "source_text_copied": False,
        "source_language_terms_copied": False,
        "native_review_status": "not_reviewed",
        "canonical_approval_status": "not_approved",
    }


def build_document() -> dict:
    candidates = load_json(CANDIDATE_FORMS_JSON)
    preflight = load_json(PREFLIGHT_JSON)
    preflight_rows = preflight_by_lane(preflight)
    rows = [
        queue_item(candidate, preflight_rows[candidate["language_lane"]])
        for candidate in candidates.get("candidate_forms", [])
    ]
    rows = sorted(rows, key=lambda row: (row["language_lane"], row["priority"], row["term_id"]))

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
                "pending_human_confirmation": len(lane_rows),
                "confirmed_items": 0,
                "application_allowed_now": 0,
                "applied_items": 0,
                "review_packet_rows_populated": 0,
                "pages_checked": sum(int(row["pages_checked"]) for row in lane_rows),
                "exact_match_page_hits": sum(int(row["pages_with_exact_term_occurrence"]) for row in lane_rows),
                "domains": dict(sorted(Counter(row["mathematical_domain"] for row in lane_rows).items())),
            }
        )

    return {
        "artifact": "context_note_confirmation_apply_queue_french_japanese",
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
            "candidate_filled_forms": CANDIDATE_FORMS_JSON.name,
            "review_packet_population_preflight": PREFLIGHT_JSON.name,
        },
        "queue_policy": {
            "candidate_note_values_referenced_by_hash": True,
            "human_confirmation_required": True,
            "application_performed": False,
            "review_packet_population_performed": False,
            "source_passage_copying_allowed": False,
            "source_language_term_copying_allowed": False,
            "native_review_claim_allowed": False,
            "canonical_approval_allowed": False,
            "included_lanes": ["french", "japanese"],
        },
        "totals": {
            "lanes": len(lane_summary),
            "queue_items": len(rows),
            "pending_human_confirmation": len(rows),
            "confirmed_items": 0,
            "application_allowed_now": 0,
            "applied_items": 0,
            "review_packet_rows_populated": 0,
            "source_forms_still_blank": len(rows),
            "review_packet_population_performed": False,
            "current_approved_terms": 0,
            "current_accepted_corrections": 0,
        },
        "lane_summary": lane_summary,
        "queue_items": rows,
        "boundaries": [
            "This queue records confirmation/application work only.",
            "Candidate note values are referenced by hash and not repeated in queue rows.",
            "No human confirmation, source capture-form application, reviewer-packet population, review send, or canonical approval is performed.",
            "No source-language passages or source-language terms are copied.",
        ],
    }


def write_markdown(document: dict) -> None:
    totals = document["totals"]
    lines = [
        "# Context-note confirmation/apply queue: French and Japanese - 2026-06-30",
        "",
        "Status: confirmation/apply queue only. Candidate note values are referenced by hash; no application or reviewer-packet population is performed.",
        "",
        "## Totals",
        "",
        f"- Queue items: {totals['queue_items']}",
        f"- Pending human confirmation: {totals['pending_human_confirmation']}",
        f"- Confirmed items: {totals['confirmed_items']}",
        f"- Application allowed now: {totals['application_allowed_now']}",
        f"- Applied items: {totals['applied_items']}",
        f"- Reviewer packet rows populated: {totals['review_packet_rows_populated']}",
        "",
        "## Lane Summary",
        "",
        "| Lane | Queue items | Pending | Confirmed | Application allowed | Applied | Packet rows populated |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in document["lane_summary"]:
        lines.append(
            f"| {row['lane']} | {row['queue_items']} | {row['pending_human_confirmation']} | "
            f"{row['confirmed_items']} | {row['application_allowed_now']} | {row['applied_items']} | "
            f"{row['review_packet_rows_populated']} |"
        )
    lines.extend(
        [
            "",
            "## Apply Gate",
            "",
            "- Confirm candidate context notes.",
            "- Revise candidates where needed.",
            "- Apply confirmed note values to the capture forms in a separate tracked step.",
            "- Re-run reviewer-packet preflight only after application is tracked.",
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
        "- Context-note confirmation/apply queue: "
        f"{document['totals']['queue_items']} French/Japanese queue items / "
        "0 confirmed / 0 applied / reviewer packets still blocked"
    )
    if re.search(r"^- Context-note confirmation/apply queue: .*", text, flags=re.MULTILINE):
        text = re.sub(r"^- Context-note confirmation/apply queue: .*", line, text, flags=re.MULTILINE)
    else:
        marker = "- Context-note candidate-filled forms:"
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
        "ready-note-entry/context-note-draft/context-note-candidate-filled/manual-triage",
        "ready-note-entry/context-note-draft/context-note-candidate-filled/context-note-confirmation-apply/manual-triage",
    )
    text = text.replace(
        "context-note-confirmation-apply/context-note-confirmation-apply",
        "context-note-confirmation-apply",
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
    manifest["context_note_confirmation_apply_queue"] = {
        "status": document["status"],
        "artifact_markdown": OUT_MD.name,
        "artifact_json": OUT_JSON.name,
        "lanes": totals["lanes"],
        "queue_items": totals["queue_items"],
        "pending_human_confirmation": totals["pending_human_confirmation"],
        "confirmed_items": 0,
        "application_allowed_now": 0,
        "applied_items": 0,
        "review_packet_rows_populated": 0,
        "source_forms_still_blank": totals["source_forms_still_blank"],
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
                "context_note_confirmation_apply_queue_json": str(OUT_JSON),
                "queue_items": document["totals"]["queue_items"],
                "pending_human_confirmation": document["totals"]["pending_human_confirmation"],
                "confirmed_items": document["totals"]["confirmed_items"],
                "applied_items": document["totals"]["applied_items"],
                "review_packet_rows_populated": document["totals"]["review_packet_rows_populated"],
                "no_network_actions_performed": document["no_network_actions_performed"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
