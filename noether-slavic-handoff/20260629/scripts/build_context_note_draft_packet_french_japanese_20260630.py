import datetime
import hashlib
import json
import pathlib
import re
from collections import Counter, defaultdict


BASE = pathlib.Path(__file__).resolve().parents[1]
STATUS_MANIFEST = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_MANIFEST_20260629.json"
STATUS_INDEX = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_INDEX_20260629.md"
READY_PACKET_JSON = BASE / "READY_CONTEXT_NOTE_ENTRY_PACKET_FRENCH_JAPANESE_20260630.json"
OUT_JSON = BASE / "CONTEXT_NOTE_DRAFT_PACKET_FRENCH_JAPANESE_20260630.json"
OUT_MD = BASE / "CONTEXT_NOTE_DRAFT_PACKET_FRENCH_JAPANESE_20260630.md"
SELF_PATH = pathlib.Path(__file__).resolve()

STATUS = "source_safe_context_note_drafts_not_applied_not_review_packet_population"


DOMAIN_SCOPE = {
    "algebra_core": "core algebra usage and undergraduate-to-graduate continuity",
    "field_theory": "field-theoretic usage in algebraic examples and constructions",
    "finiteness": "finiteness-condition usage and comparison with Noetherian/Artinian contexts",
    "ideal_theory": "ideal-theoretic usage in ring and algebra arguments",
    "invariant_theory": "invariant-theory usage and algebraic transformation contexts",
    "module_theory": "module-theoretic usage in definitions, quotients, tensor constructions, and morphisms",
    "morphism": "structure-preserving map usage across algebraic objects",
    "noetherian": "Noetherian-condition usage in ring, module, and chain-condition contexts",
    "ring_theory": "ring-theoretic usage in algebraic definitions and examples",
    "representation_theory": "representation-theoretic usage where the selected evidence supports it",
}

LANE_REVIEW_FOCUS = {
    "french": "standard French mathematical register, avoiding literal calques where established French usage differs",
    "japanese": "standard Japanese mathematical register, including script balance, proof prose, and TeX/PDF readability",
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


def source_density(row: dict) -> str:
    checked = int(row.get("pages_checked") or 0)
    exact = int(row.get("pages_with_exact_term_occurrence") or 0)
    if checked == 0:
        return "no inspected page count is available"
    if exact == checked:
        return "all inspected pages in the row had exact extraction matches"
    if exact == 0:
        return "the row has no exact extraction match and should not be in this draft packet"
    return "the row had partial exact extraction matches and needs a careful reviewer question"


def draft_values(form: dict) -> dict:
    lane = form["language_lane"]
    concept = form["english_concept"]
    domain = form["mathematical_domain"]
    domain_scope = DOMAIN_SCOPE.get(domain, f"{domain} usage")
    focus = LANE_REVIEW_FOCUS.get(lane, "native mathematical register and educational clarity")
    checked = form["pages_checked"]
    exact = form["pages_with_exact_term_occurrence"]
    density = source_density(form)

    return {
        "human_page_context_note_without_source_quote": (
            f"Draft note: local extraction evidence for {concept} in the {lane} lane was inspected across "
            f"{checked} pages, with {exact} exact-match page hits recorded. Treat this as a source-supported "
            "candidate context note for reviewer preparation only; it does not approve a term or copy source text."
        ),
        "usage_scope_note": (
            f"Use this row to ask about {domain_scope}. The draft should be checked for {focus}; "
            f"evidence density note: {density}."
        ),
        "reviewer_question": (
            f"Please confirm whether the proposed handling of the concept '{concept}' is natural in the target "
            f"mathematical register, whether its scope in {domain} is correct, and whether any alternate register "
            "or educational phrasing should be recorded before canonical promotion."
        ),
        "packet_population_decision": "draft_available_for_human_confirmation_not_applied_to_reviewer_packet",
    }


def flatten_ready_forms(packet: dict) -> list[dict]:
    rows = []
    for lane_packet in packet.get("lane_packets", []):
        for form in lane_packet.get("forms_to_fill", []):
            rows.append(form)
    return sorted(rows, key=lambda row: (row["language_lane"], row["priority"], row["term_id"]))


def build_document() -> dict:
    ready_packet = load_json(READY_PACKET_JSON)
    source_forms = flatten_ready_forms(ready_packet)
    draft_rows = []
    for form in source_forms:
        draft_rows.append(
            {
                "draft_id": f"draft-{form['form_id']}",
                "form_id": form["form_id"],
                "term_id": form["term_id"],
                "language_lane": form["language_lane"],
                "english_concept": form["english_concept"],
                "mathematical_domain": form["mathematical_domain"],
                "priority": form["priority"],
                "inspection_batch_id": form["inspection_batch_id"],
                "pages_checked": form["pages_checked"],
                "pages_with_exact_term_occurrence": form["pages_with_exact_term_occurrence"],
                "source_readiness_state": form["readiness_state"],
                "source_form_status": form["form_status"],
                "source_packet_population_status": form["packet_population_status"],
                "draft_note_values": draft_values(form),
                "draft_application_status": "proposed_not_applied",
                "packet_population_status_after_draft": "blocked_until_human_confirmation_and_form_application",
                "review_packet_population_performed": False,
                "source_text_copied": False,
                "source_language_terms_copied": False,
                "native_review_status": "not_reviewed",
                "canonical_approval_status": "not_approved",
            }
        )

    by_lane = defaultdict(list)
    for row in draft_rows:
        by_lane[row["language_lane"]].append(row)
    lane_summary = []
    for lane in sorted(by_lane):
        rows = by_lane[lane]
        lane_summary.append(
            {
                "lane": lane,
                "draft_rows": len(rows),
                "drafts_applied": 0,
                "packet_rows_populated": 0,
                "pages_checked": sum(int(row["pages_checked"]) for row in rows),
                "exact_match_page_hits": sum(int(row["pages_with_exact_term_occurrence"]) for row in rows),
                "domains": dict(sorted(Counter(row["mathematical_domain"] for row in rows).items())),
            }
        )

    return {
        "artifact": "context_note_draft_packet_french_japanese",
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
            "ready_context_note_entry_packet": READY_PACKET_JSON.name,
        },
        "draft_policy": {
            "draft_values_are_proposals_only": True,
            "ready_packet_forms_remain_blank": True,
            "review_packet_population_performed": False,
            "source_passage_copying_allowed": False,
            "source_language_term_copying_allowed": False,
            "canonical_approval_allowed": False,
            "included_lanes": ["french", "japanese"],
            "included_ready_packet_rows": len(source_forms),
        },
        "totals": {
            "lanes": len(lane_summary),
            "draft_rows": len(draft_rows),
            "drafts_applied": 0,
            "packet_rows_populated": 0,
            "source_forms_referenced": len(source_forms),
            "manual_source_review_rows_included": 0,
            "review_packet_population_performed": False,
            "current_approved_terms": 0,
            "current_accepted_corrections": 0,
        },
        "lane_summary": lane_summary,
        "draft_rows": draft_rows,
        "boundaries": [
            "Draft values are proposed note text only and are not applied to the blank capture forms.",
            "This artifact does not copy source-language passages or source-language terms.",
            "This artifact does not populate reviewer packets, send reviews, ingest returns, approve terms, or promote canonical editions.",
            "Native/external authority review remains required.",
        ],
    }


def write_markdown(document: dict) -> None:
    totals = document["totals"]
    lines = [
        "# Context-note draft packet: French and Japanese - 2026-06-30",
        "",
        "Status: source-safe draft notes only. These drafts are not applied to capture forms, not reviewer-packet population, and not term approval.",
        "",
        "## Totals",
        "",
        f"- Draft rows: {totals['draft_rows']}",
        f"- Source forms referenced: {totals['source_forms_referenced']}",
        f"- Drafts applied: {totals['drafts_applied']}",
        f"- Reviewer packet rows populated: {totals['packet_rows_populated']}",
        f"- Manual/source-review rows included: {totals['manual_source_review_rows_included']}",
        f"- Network actions: {0 if document['no_network_actions_performed'] else 'unknown'}",
        "",
        "## Lane Summary",
        "",
        "| Lane | Draft rows | Pages checked | Exact-match page hits | Drafts applied | Packet rows populated |",
        "| --- | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in document["lane_summary"]:
        lines.append(
            f"| {row['lane']} | {row['draft_rows']} | {row['pages_checked']} | "
            f"{row['exact_match_page_hits']} | {row['drafts_applied']} | {row['packet_rows_populated']} |"
        )
    lines.extend(
        [
            "",
            "## Draft Fields",
            "",
            "- `human_page_context_note_without_source_quote`",
            "- `usage_scope_note`",
            "- `reviewer_question`",
            "- `packet_population_decision`",
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
        "- Context-note draft packet: "
        f"{document['totals']['draft_rows']} French/Japanese draft rows / "
        "0 applied / 0 reviewer-packet population"
    )
    if re.search(r"^- Context-note draft packet: .*", text, flags=re.MULTILINE):
        text = re.sub(r"^- Context-note draft packet: .*", line, text, flags=re.MULTILINE)
    else:
        marker = "- Ready context-note entry packet:"
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
        "page inspection queue/batch/readiness/context-note/capture-form/lane-gate-dashboard/ready-note-entry/manual-triage",
        "page inspection queue/batch/readiness/context-note/capture-form/lane-gate-dashboard/ready-note-entry/context-note-draft/manual-triage",
    )
    text = text.replace("context-note-draft/context-note-draft", "context-note-draft")
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
    manifest["context_note_draft_packet"] = {
        "status": document["status"],
        "artifact_markdown": OUT_MD.name,
        "artifact_json": OUT_JSON.name,
        "lanes": totals["lanes"],
        "draft_rows": totals["draft_rows"],
        "source_forms_referenced": totals["source_forms_referenced"],
        "drafts_applied": 0,
        "packet_rows_populated": 0,
        "manual_source_review_rows_included": 0,
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
                "context_note_draft_packet_json": str(OUT_JSON),
                "draft_rows": document["totals"]["draft_rows"],
                "drafts_applied": document["totals"]["drafts_applied"],
                "packet_rows_populated": document["totals"]["packet_rows_populated"],
                "no_network_actions_performed": document["no_network_actions_performed"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
