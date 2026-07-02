"""Build the Tajik Cyrillic source-discovery promotion ledger.

This is a local-only ledger for the tg_Cyrl_TJ lane. It records selected
witness metadata and blank source-language review checks, but it does not read
witness bodies, copy source-language terms, populate reviewer packets, or
promote any canonical terminology.
"""

from __future__ import annotations

import datetime
import hashlib
import json
import pathlib
import re


BASE = pathlib.Path(__file__).resolve().parents[1]
STATUS_MANIFEST = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_MANIFEST_20260629.json"
STATUS_INDEX = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_INDEX_20260629.md"
OUT_JSON = BASE / "TAJIK_CYRILLIC_SOURCE_DISCOVERY_PROMOTION_LEDGER_20260701.json"
OUT_MD = BASE / "TAJIK_CYRILLIC_SOURCE_DISCOVERY_PROMOTION_LEDGER_20260701.md"
SELF_PATH = pathlib.Path(__file__).resolve()

LANE_ID = "tg_Cyrl_TJ"
STATUS = "tajik_cyrillic_source_discovery_promotion_ledger_local_only_not_promoted"


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


def find_row(rows: list[dict], key: str, value: str) -> dict:
    for row in rows:
        if row.get(key) == value:
            return row
    raise KeyError(f"missing row where {key}={value}")


def selected_witness_rows(selection_row: dict, validation_slots: list[dict]) -> list[dict]:
    validation_by_rank = {row.get("selected_rank"): row for row in validation_slots}
    rows = []
    for witness in selection_row.get("selected_witnesses", []):
        rank = witness["selected_rank"]
        validation = validation_by_rank.get(rank, {})
        filesystem = validation.get("filesystem", {})
        rows.append(
            {
                "selected_rank": rank,
                "slot_id": validation.get("slot_id", f"{LANE_ID}::selected-{rank}"),
                "batch": witness["batch"],
                "bucket": witness["bucket"],
                "path": witness["path"],
                "source_core_included": witness.get("source_core_included") is True,
                "path_validation_status": validation.get("path_validation_status", "not_checked"),
                "path_exists": filesystem.get("path_exists") is True,
                "is_directory": filesystem.get("is_directory") is True,
                "files": filesystem.get("files", 0),
                "text_source_like_files": filesystem.get("text_source_like_files", 0),
                "tex_files": filesystem.get("tex_files", 0),
                "pdf_files": filesystem.get("pdf_files", 0),
                "source_core_files_from_matrix": witness.get("source_core_files", 0),
                "review_status": "blank_source_language_review_needed",
                "source_body_copied": False,
                "source_excerpt_copied": False,
                "source_language_terms_copied": False,
                "source_file_names_copied": False,
            }
        )
    return rows


def review_question_rows(witnesses: list[dict]) -> list[dict]:
    question_templates = [
        ("language_register_identity", "Confirm whether this witness is usable Tajik Cyrillic mathematical-register evidence."),
        ("topic_relevance", "Check whether the witness actually supports algebra, number theory, or adjacent technical mathematics."),
        ("advanced_term_presence", "Check whether ring, field, ideal, module, representation, or invariant-theory anchors are present."),
        ("license_and_reuse_context", "Record whether the witness can support local citation, reviewer packet use, or only metadata routing."),
    ]
    rows = []
    for witness in witnesses:
        for order, (question_id, prompt) in enumerate(question_templates, start=1):
            rows.append(
                {
                    "question_row_id": f"{witness['slot_id']}::q{order}",
                    "slot_id": witness["slot_id"],
                    "selected_rank": witness["selected_rank"],
                    "question_id": question_id,
                    "prompt": prompt,
                    "answer_status": "blank",
                    "evidence_artifact_linked": False,
                    "source_excerpt_copied": False,
                    "source_language_terms_copied": False,
                    "ready_for_term_anchor_extraction": False,
                }
            )
    return rows


def build_document() -> dict:
    selection = load_json(BASE / "LOCAL_SOURCE_WITNESS_SELECTION_MATRIX_20260630.json")
    shortlist = load_json(BASE / "LOCAL_SOURCE_WITNESS_SHORTLIST_20260630.json")
    validation = load_json(BASE / "SELECTED_SOURCE_WITNESS_FILESYSTEM_VALIDATION_20260630.json")
    gap_note = load_json(BASE / "PERSIAN_FAMILY_DARI_TAJIK_REGISTER_GAP_20260629.json")
    dashboard = load_json(BASE / "NON_SLAVIC_LANE_GATE_DASHBOARD_20260630.json")
    integrated = load_json(BASE / "INTEGRATED_LANE_HANDOFF_READINESS_MATRIX_20260630.json")
    next_queue = load_json(BASE / "LANE_PROMOTION_NEXT_ACTION_QUEUE_20260630.json")

    selection_row = find_row(selection["matrix_rows"], "lane_or_cohort", LANE_ID)
    shortlist_row = find_row(shortlist["shortlist_rows"], "lane_or_cohort", LANE_ID)
    validation_row = find_row(validation["lane_validation_rows"], "lane_or_cohort", LANE_ID)
    validation_slots = [
        row for row in validation["selected_witness_slot_rows"] if row.get("lane_or_cohort") == LANE_ID
    ]
    dashboard_row = find_row(dashboard["lane_gates"], "lane", LANE_ID)
    integrated_row = find_row(integrated["lane_or_cohort_rows"], "lane_or_cohort", LANE_ID)
    queue_row = find_row(next_queue["lane_action_rows"], "lane_or_cohort", LANE_ID)
    context_pointers = [
        {
            "id": row["id"],
            "sublane": row["sublane"],
            "language_label": row["language_label"],
            "title": row["title"],
            "url": row["url"],
            "access_status": row["access_status"],
            "content_type": row["content_type"],
            "evidence_role": row["evidence_role"],
            "authority_note": row["authority_note"],
            "source_body_copied": False,
            "source_excerpt_copied": False,
            "source_language_terms_copied": False,
        }
        for row in gap_note["validated_candidates"]
        if row.get("sublane") == LANE_ID
    ]
    witnesses = selected_witness_rows(selection_row, validation_slots)
    questions = review_question_rows(witnesses)

    promotion_gate_checks = [
        {
            "gate": "local_candidate_shelves_exist",
            "passed": shortlist_row.get("candidate_shelves", 0) > 0,
            "evidence": "LOCAL_SOURCE_WITNESS_SHORTLIST_20260630.json",
        },
        {
            "gate": "selected_witness_paths_exist",
            "passed": validation_row.get("missing_paths") == 0 and validation_row.get("paths_existing") == 3,
            "evidence": "SELECTED_SOURCE_WITNESS_FILESYSTEM_VALIDATION_20260630.json",
        },
        {
            "gate": "source_language_review_received",
            "passed": False,
            "evidence": "no source-language review return recorded",
        },
        {
            "gate": "term_anchor_rows_available",
            "passed": False,
            "evidence": "LOCAL_SOURCE_WITNESS_SHORTLIST_20260630.json records zero Tajik term-anchor rows",
        },
        {
            "gate": "page_level_inspection_completed",
            "passed": False,
            "evidence": "no Tajik page-inspection rows exist yet",
        },
        {
            "gate": "native_or_external_authority_review_completed",
            "passed": False,
            "evidence": "native_review_status remains not_reviewed",
        },
    ]

    totals = {
        "candidate_shelves": shortlist_row["candidate_shelves"],
        "candidate_shelves_with_source_core": shortlist_row["candidate_shelves_with_source_core"],
        "candidate_text_source_like_files": shortlist_row["candidate_text_source_like_files"],
        "candidate_tex_files": shortlist_row["candidate_tex_files"],
        "candidate_pdf_files": shortlist_row["candidate_pdf_files"],
        "candidate_source_core_files": shortlist_row["candidate_source_core_files"],
        "selected_witness_slots": selection_row["selected_witnesses_count"],
        "selected_witnesses_with_source_core": selection_row["selected_witnesses_with_source_core"],
        "selected_text_source_like_files_from_matrix": selection_row["selected_text_source_like_files"],
        "validated_slot_paths_existing": validation_row["paths_existing"],
        "validated_slot_missing_paths": validation_row["missing_paths"],
        "filesystem_files": validation_row["files"],
        "filesystem_text_source_like_files": validation_row["text_source_like_files"],
        "filesystem_tex_files": validation_row["tex_files"],
        "filesystem_pdf_files": validation_row["pdf_files"],
        "context_pointers": len(context_pointers),
        "blank_review_question_rows": len(questions),
        "source_language_review_returns": 0,
        "term_anchor_rows": 0,
        "page_inspection_rows": 0,
        "source_discovery_promotions_completed": 0,
        "term_queue_rows_created": 0,
        "review_packet_rows_populated": 0,
        "canonical_rows_resolved": 0,
        "translations_created": 0,
        "source_excerpts_copied": 0,
        "source_language_terms_copied": 0,
        "network_actions": 0,
    }

    return {
        "artifact": "tajik_cyrillic_source_discovery_promotion_ledger",
        "status": STATUS,
        "generated_date": "2026-07-01",
        "generated_utc": now_utc(),
        "lane": LANE_ID,
        "label": "Tajik Cyrillic",
        "bandwidth_mode": "local_only_no_network_actions",
        "inputs": {
            "selection_matrix": "LOCAL_SOURCE_WITNESS_SELECTION_MATRIX_20260630.json",
            "shortlist": "LOCAL_SOURCE_WITNESS_SHORTLIST_20260630.json",
            "filesystem_validation": "SELECTED_SOURCE_WITNESS_FILESYSTEM_VALIDATION_20260630.json",
            "register_gap_note": "PERSIAN_FAMILY_DARI_TAJIK_REGISTER_GAP_20260629.json",
            "non_slavic_lane_gate_dashboard": "NON_SLAVIC_LANE_GATE_DASHBOARD_20260630.json",
            "integrated_lane_handoff_readiness_matrix": "INTEGRATED_LANE_HANDOFF_READINESS_MATRIX_20260630.json",
            "lane_promotion_next_action_queue": "LANE_PROMOTION_NEXT_ACTION_QUEUE_20260630.json",
        },
        "lane_state_from_inputs": {
            "dashboard_gate": dashboard_row["gate_status"],
            "integrated_gate": integrated_row["edition_gate"],
            "queue_action": queue_row["action_type"],
            "queue_blocker": queue_row["blocker_class"],
            "queue_acceptance_gate": queue_row["downstream_gate_unlocked_if_accepted"],
            "recommended_next_gate": shortlist_row["recommended_next_gate"],
            "selection_next_action": selection_row["next_action"],
        },
        "promotion_policy": {
            "metadata_only": True,
            "read_witness_file_contents": False,
            "copy_source_passages": False,
            "copy_source_language_terms": False,
            "populate_review_packets": False,
            "create_translation_or_revision": False,
            "allow_term_anchor_extraction_now": False,
            "allow_canonical_tajik_claim_now": False,
            "require_source_language_review_before_promotion": True,
            "farsi_or_arabic_cannot_substitute_for_tajik": True,
            "no_network_actions_performed": True,
        },
        "selected_witnesses": witnesses,
        "context_pointers": context_pointers,
        "blank_source_language_review_questions": questions,
        "promotion_gate_checks": promotion_gate_checks,
        "totals": totals,
        "zero_gate_boundaries": {
            "source_language_review_returns": 0,
            "term_anchor_rows": 0,
            "page_inspection_rows": 0,
            "source_discovery_promotions_completed": 0,
            "term_queue_rows_created": 0,
            "review_packet_rows_populated": 0,
            "canonical_rows_resolved": 0,
            "translations_created": 0,
            "source_excerpts_copied": 0,
            "source_language_terms_copied": 0,
            "network_actions": 0,
        },
        "boundaries": [
            "This ledger is source-discovery routing only, not a term-anchor queue.",
            "Selected local witnesses are not approved Tajik terminology sources until source-language review promotes them.",
            "Farsi, Dari, Arabic, or adjacent Arabic-script evidence cannot silently supply Tajik Cyrillic authority.",
            "No source passages, source-language terms, credentials, or tokens are copied.",
            "No reviewer packet rows are populated and no translations are created.",
        ],
    }


def write_markdown(document: dict) -> None:
    totals = document["totals"]
    lines = [
        "# Tajik Cyrillic source-discovery promotion ledger - 2026-07-01",
        "",
        "Status: local-only source-discovery ledger. This is not a term-anchor queue, not a populated reviewer packet, not native/external review, not a translation, and not a canonical Tajik terminology claim.",
        "",
        "## Summary",
        "",
        f"- Candidate shelves: `{totals['candidate_shelves']}`",
        f"- Candidate shelves with source-core support: `{totals['candidate_shelves_with_source_core']}`",
        f"- Selected witness slots: `{totals['selected_witness_slots']}`",
        f"- Validated selected paths existing: `{totals['validated_slot_paths_existing']}`",
        f"- Missing selected paths: `{totals['validated_slot_missing_paths']}`",
        f"- Context pointers from Dari/Tajik register gap note: `{totals['context_pointers']}`",
        f"- Blank source-language review questions: `{totals['blank_review_question_rows']}`",
        f"- Term-anchor rows created: `{totals['term_anchor_rows']}`",
        f"- Source-discovery promotions completed: `{totals['source_discovery_promotions_completed']}`",
        f"- Network actions: `{totals['network_actions']}`",
        "",
        "## Selected Witness Slots",
        "",
        "| Rank | Batch | Path exists | Text-like files | TeX files | PDF files | Review status |",
        "| ---: | --- | --- | ---: | ---: | ---: | --- |",
    ]
    for row in document["selected_witnesses"]:
        lines.append(
            f"| {row['selected_rank']} | `{row['batch']}` | `{str(row['path_exists']).lower()}` | "
            f"{row['text_source_like_files']} | {row['tex_files']} | {row['pdf_files']} | `{row['review_status']}` |"
        )
    lines.extend(
        [
            "",
            "## Promotion Gate",
            "",
            "| Gate | Passed | Evidence |",
            "| --- | --- | --- |",
        ]
    )
    for row in document["promotion_gate_checks"]:
        lines.append(f"| `{row['gate']}` | `{str(row['passed']).lower()}` | {row['evidence']} |")
    lines.extend(
        [
            "",
            "## Boundary",
            "",
            "- Source-language review is still required before term-anchor extraction.",
            "- Farsi, Dari, Arabic, or adjacent Arabic-script evidence cannot substitute for Tajik Cyrillic authority.",
            "- No source passages, source-language terms, credentials, or tokens are copied.",
            "- No reviewer packet rows are populated.",
            "- No translation, source-discovery promotion, term approval, or canonical-readiness claim is made.",
            "",
        ]
    )
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
    totals = document["totals"]
    line = (
        "- Tajik Cyrillic source-discovery promotion ledger: "
        f"{totals['selected_witness_slots']} selected witness slots / "
        f"{totals['candidate_shelves']} candidate shelves / "
        f"{totals['context_pointers']} context pointers / "
        f"{totals['blank_review_question_rows']} blank review questions / 0 promotions"
    )
    pattern = r"^- Tajik Cyrillic source-discovery promotion ledger: .*"
    if re.search(pattern, text, flags=re.MULTILINE):
        text = re.sub(pattern, line, text, flags=re.MULTILINE)
    else:
        anchor = "- Non-Slavic lane gate dashboard:"
        rows = text.splitlines()
        for index, row in enumerate(rows):
            if row.startswith(anchor):
                rows.insert(index + 1, line)
                text = "\n".join(rows) + "\n"
                break
        else:
            text = text.rstrip() + "\n" + line + "\n"

    if "tajik-cyrillic-source-discovery-promotion-ledger" not in text:
        text = text.replace(
            "cross-session-output-shelf-metadata-snapshot/render-script-preflight",
            (
                "cross-session-output-shelf-metadata-snapshot/"
                "tajik-cyrillic-source-discovery-promotion-ledger/render-script-preflight"
            ),
        )
    if "Generated UTC: " in text:
        old = text.split("Generated UTC: ", 1)[1].splitlines()[0]
        text = text.replace(old, manifest["generated_utc"], 1)
    STATUS_INDEX.write_text(text, encoding="utf-8")


def update_manifest(document: dict) -> None:
    manifest = load_json(STATUS_MANIFEST)
    manifest["generated_utc"] = now_utc()
    upsert_artifact(manifest, "json", OUT_JSON, document["status"])
    upsert_artifact(manifest, "markdown", OUT_MD)
    upsert_artifact(manifest, "scripts", SELF_PATH)
    refresh_existing_artifact_hashes(manifest)

    totals = document["totals"]
    manifest["tajik_cyrillic_source_discovery_promotion_ledger"] = {
        "status": document["status"],
        "artifact_markdown": OUT_MD.name,
        "artifact_json": OUT_JSON.name,
        "lane": LANE_ID,
        "candidate_shelves": totals["candidate_shelves"],
        "candidate_shelves_with_source_core": totals["candidate_shelves_with_source_core"],
        "selected_witness_slots": totals["selected_witness_slots"],
        "validated_slot_paths_existing": totals["validated_slot_paths_existing"],
        "validated_slot_missing_paths": totals["validated_slot_missing_paths"],
        "context_pointers": totals["context_pointers"],
        "blank_review_question_rows": totals["blank_review_question_rows"],
        "source_language_review_returns": 0,
        "term_anchor_rows": 0,
        "page_inspection_rows": 0,
        "source_discovery_promotions_completed": 0,
        "term_queue_rows_created": 0,
        "review_packet_rows_populated": 0,
        "canonical_rows_resolved": 0,
        "translations_created": 0,
        "source_excerpts_copied": 0,
        "source_language_terms_copied": 0,
        "source_text_copied": False,
        "credentials_or_tokens_copied": False,
        "no_network_actions_performed": True,
        "review_packet_population_performed": False,
        "translation_or_revision_performed": False,
        "native_review_status": "not_reviewed",
        "canonical_approval_status": "not_approved",
        "promotion_to_term_anchor_extraction_allowed": False,
    }
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
                "tajik_ledger_json": str(OUT_JSON),
                "selected_witness_slots": document["totals"]["selected_witness_slots"],
                "candidate_shelves": document["totals"]["candidate_shelves"],
                "context_pointers": document["totals"]["context_pointers"],
                "blank_review_question_rows": document["totals"]["blank_review_question_rows"],
                "promotions_completed": 0,
                "network_actions": 0,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
