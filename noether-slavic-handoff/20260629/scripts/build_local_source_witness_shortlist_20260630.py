import datetime
import hashlib
import json
import pathlib
import re
from collections import Counter


BASE = pathlib.Path(__file__).resolve().parents[1]
STATUS_MANIFEST = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_MANIFEST_20260629.json"
STATUS_INDEX = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_INDEX_20260629.md"
INVENTORY_JSON = BASE / "LOCAL_SOURCE_EVIDENCE_SHELF_INVENTORY_20260630.json"
LANE_GATE_JSON = BASE / "NON_SLAVIC_LANE_GATE_DASHBOARD_20260630.json"
LANE_TERM_STATUS_JSON = BASE / "LANE_TERM_STATUS_SUMMARIES_20260629.json"
SOURCE_EVIDENCE_SEED_JSON = BASE / "NON_SLAVIC_SOURCE_EVIDENCE_SEED_20260629.json"
OUT_JSON = BASE / "LOCAL_SOURCE_WITNESS_SHORTLIST_20260630.json"
OUT_MD = BASE / "LOCAL_SOURCE_WITNESS_SHORTLIST_20260630.md"
SELF_PATH = pathlib.Path(__file__).resolve()

STATUS = "local_source_witness_shortlist_no_network_no_review_no_source_passage_copy"

LANE_SPECS = [
    {
        "id": "french",
        "kind": "core_language_lane",
        "label": "French",
        "markers": ["french", "romance", "pan_romance"],
        "bucket_filters": ["french_spanish_romance"],
        "edition_gate": "ready_for_page_context_note_entry_not_packet_population",
    },
    {
        "id": "spanish",
        "kind": "core_language_lane",
        "label": "Spanish",
        "markers": ["spanish", "romance", "pan_romance", "south_american", "caribbean"],
        "bucket_filters": ["french_spanish_romance"],
        "edition_gate": "mixed_ready_rows_and_manual_source_review_required",
    },
    {
        "id": "simplified_chinese",
        "kind": "core_language_lane",
        "label": "Simplified Chinese",
        "markers": ["chinese", "cjk"],
        "bucket_filters": ["simplified_chinese_japanese_cjk"],
        "edition_gate": "mixed_ready_rows_and_manual_source_review_required",
    },
    {
        "id": "japanese",
        "kind": "core_language_lane",
        "label": "Japanese",
        "markers": ["japanese", "cjk"],
        "bucket_filters": ["simplified_chinese_japanese_cjk"],
        "edition_gate": "ready_for_page_context_note_entry_not_packet_population",
    },
    {
        "id": "fa_IR",
        "kind": "core_language_lane",
        "label": "Persian/Farsi (Iran)",
        "markers": ["persian", "farsi", "persianate"],
        "bucket_filters": ["persian_family_arabic"],
        "edition_gate": "mixed_ready_rows_and_manual_source_review_required",
    },
    {
        "id": "prs_AF",
        "kind": "core_language_lane",
        "label": "Dari/Persian (Afghanistan)",
        "markers": ["dari", "afghan"],
        "bucket_filters": ["persian_family_arabic"],
        "edition_gate": "mixed_ready_rows_and_manual_source_review_required",
    },
    {
        "id": "tg_Cyrl_TJ",
        "kind": "core_language_lane",
        "label": "Tajik Cyrillic",
        "markers": ["tajik"],
        "bucket_filters": ["persian_family_arabic"],
        "edition_gate": "source_discovery_required_before_term_queue",
    },
    {
        "id": "arabic",
        "kind": "core_language_lane",
        "label": "Arabic",
        "markers": ["arabic", "arabic_script", "controlled_arabic"],
        "bucket_filters": ["persian_family_arabic"],
        "edition_gate": "mixed_ready_rows_and_manual_source_review_required",
    },
    {
        "id": "pan_turkic_adjacent",
        "kind": "extension_cohort",
        "label": "Pan-Turkic Adjacent Cohort",
        "markers": [],
        "bucket_filters": ["pan_turkic"],
        "edition_gate": "source_shelf_extension_not_edition_lane",
    },
    {
        "id": "south_asia_hindustani_indic_dravidian",
        "kind": "extension_cohort",
        "label": "South Asian / Hindustani / Indic / Dravidian Cohort",
        "markers": [],
        "bucket_filters": ["south_asia_hindustani_indic_dravidian"],
        "edition_gate": "source_shelf_extension_not_edition_lane",
    },
    {
        "id": "east_southeast_asia_pacific",
        "kind": "extension_cohort",
        "label": "East/Southeast Asia and Pacific Cohort",
        "markers": [],
        "bucket_filters": ["east_southeast_asia_pacific"],
        "edition_gate": "source_shelf_extension_not_edition_lane",
    },
    {
        "id": "africa_deep_gap",
        "kind": "extension_cohort",
        "label": "African Deep-Gap Cohort",
        "markers": [],
        "bucket_filters": ["africa_deep_gap"],
        "edition_gate": "source_shelf_extension_not_edition_lane",
    },
    {
        "id": "source_first_reference_textbooks",
        "kind": "extension_cohort",
        "label": "Source-First Reference Textbook Cohort",
        "markers": [],
        "bucket_filters": ["source_first_reference_textbooks"],
        "edition_gate": "support_corpus_not_translation_lane",
    },
    {
        "id": "methodology_interlanguage_access",
        "kind": "extension_cohort",
        "label": "Methodology / Interlanguage Access Cohort",
        "markers": [],
        "bucket_filters": ["methodology_interlanguage_access"],
        "edition_gate": "research_publication_support_corpus",
    },
]

SEED_LANGUAGE_MARKERS = {
    "french": ["french"],
    "spanish": ["spanish"],
    "simplified_chinese": ["simplified chinese", "chinese"],
    "japanese": ["japanese"],
    "fa_IR": ["persian/farsi", "persian", "farsi"],
    "prs_AF": ["dari"],
    "tg_Cyrl_TJ": ["tajik"],
    "arabic": ["arabic"],
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


def seed_counts_by_lane(seed: dict) -> dict[str, int]:
    counts = Counter()
    for entry in seed.get("entries", []):
        language = str(entry.get("language", "")).lower()
        for lane, markers in SEED_LANGUAGE_MARKERS.items():
            if any(marker in language for marker in markers):
                counts[lane] += 1
    return dict(counts)


def lane_gate_map(dashboard: dict) -> dict:
    return {row.get("lane"): row for row in dashboard.get("lane_gates", [])}


def lane_term_map(term_status: dict) -> dict:
    return {row.get("lane"): row for row in term_status.get("lane_summaries", [])}


def match_batch(spec: dict, batch: dict) -> bool:
    lowered = str(batch.get("batch", "")).lower()
    if batch.get("bucket") in spec.get("bucket_filters", []):
        return True
    return any(marker in lowered for marker in spec.get("markers", []))


def candidate_score(spec: dict, batch: dict) -> float:
    lowered = str(batch.get("batch", "")).lower()
    marker_hits = sum(1 for marker in spec.get("markers", []) if marker in lowered)
    bucket_hit = 1 if batch.get("bucket") in spec.get("bucket_filters", []) else 0
    score = marker_hits * 1000 + bucket_hit * 250
    score += min(int(batch.get("source_core_files") or 0), 250) * 6
    score += min(int(batch.get("text_source_like_files") or 0), 500) * 0.2
    score += min(int(batch.get("tex_files") or 0), 500) * 0.4
    score -= min(int(batch.get("pdf_files") or 0), 500) * 0.1
    return round(score, 2)


def candidate_status(batch: dict) -> str:
    if batch.get("source_core_files", 0) > 0 and batch.get("text_source_like_files", 0) > 0:
        return "source_core_text_witness_candidate"
    if batch.get("text_source_like_files", 0) > 0:
        return "local_text_witness_candidate_not_yet_in_source_core"
    if batch.get("pdf_files", 0) > 0:
        return "pdf_heavy_manual_review_candidate"
    return "local_presence_candidate_requires_file_type_review"


def source_balance(batch: dict) -> str:
    if batch.get("text_source_like_files", 0) >= max(1, batch.get("pdf_files", 0)) * 2:
        return "source_text_first"
    if batch.get("pdf_files", 0) > batch.get("text_source_like_files", 0):
        return "pdf_manual_review_heavy"
    if batch.get("source_core_files", 0) > 0:
        return "mixed_with_source_core"
    return "mixed_or_sparse"


def select_candidates(spec: dict, batches: list[dict]) -> list[dict]:
    matches = [batch for batch in batches if match_batch(spec, batch)]
    ranked = sorted(matches, key=lambda batch: (-candidate_score(spec, batch), batch.get("batch", "")))[:8]
    candidates = []
    for index, batch in enumerate(ranked, start=1):
        candidates.append(
            {
                "rank": index,
                "batch": batch.get("batch"),
                "bucket": batch.get("bucket"),
                "path": batch.get("path"),
                "candidate_status": candidate_status(batch),
                "source_balance": source_balance(batch),
                "score": candidate_score(spec, batch),
                "disk_files": batch.get("disk_files"),
                "text_source_like_files": batch.get("text_source_like_files"),
                "tex_files": batch.get("tex_files"),
                "pdf_files": batch.get("pdf_files"),
                "source_core_files": batch.get("source_core_files"),
                "source_core_included": batch.get("source_core_included"),
                "source_text_copied": False,
                "source_language_terms_copied": False,
            }
        )
    return candidates


def next_gate(spec: dict, gate: dict | None, term: dict | None, candidates: list[dict]) -> str:
    if spec["id"] == "tg_Cyrl_TJ" and candidates and not (term or {}).get("term_anchor_rows"):
        return "promote_local_tajik_shelf_to_term_anchor_extraction_only_after_source_language_review"
    gate_status = (gate or {}).get("gate_status") or spec["edition_gate"]
    if gate_status == "ready_for_page_context_note_entry_not_packet_population":
        return "fill_page_context_notes_from_shortlisted_witnesses_before_reviewer_packet_population"
    if "manual_source_review" in gate_status or "manual_or_source" in gate_status or "mixed" in gate_status:
        return "resolve_manual_source_review_rows_against_shortlisted_witnesses_before_translation_revision"
    if spec["kind"] == "extension_cohort":
        return "keep_as_evidence_shelf_until_promoted_to_language_lane_with_source_authority_notes"
    return "select_witnesses_then_prepare_page_context_notes_before_any_translation_revision"


def build_document(manifest: dict) -> dict:
    inventory = load_json(INVENTORY_JSON)
    dashboard = load_json(LANE_GATE_JSON)
    term_status = load_json(LANE_TERM_STATUS_JSON)
    seed = load_json(SOURCE_EVIDENCE_SEED_JSON)
    batches = inventory.get("batch_inventory", [])
    gate_by_lane = lane_gate_map(dashboard)
    term_by_lane = lane_term_map(term_status)
    seed_counts = seed_counts_by_lane(seed)

    rows = []
    for spec in LANE_SPECS:
        candidates = select_candidates(spec, batches)
        gate = gate_by_lane.get(spec["id"])
        term = term_by_lane.get(spec["id"])
        row = {
            "lane_or_cohort": spec["id"],
            "kind": spec["kind"],
            "label": spec["label"],
            "edition_gate": (gate or {}).get("gate_status") or spec["edition_gate"],
            "term_anchor_rows": (term or {}).get("term_anchor_rows", 0),
            "pages_analyzed": (term or {}).get("pages_analyzed", 0),
            "term_anchor_sources": (term or {}).get("sources", 0),
            "seed_evidence_entries": seed_counts.get(spec["id"], 0),
            "candidate_shelves": len(candidates),
            "candidate_shelves_with_source_core": sum(1 for candidate in candidates if candidate["source_core_files"] > 0),
            "candidate_text_source_like_files": sum(candidate["text_source_like_files"] for candidate in candidates),
            "candidate_tex_files": sum(candidate["tex_files"] for candidate in candidates),
            "candidate_pdf_files": sum(candidate["pdf_files"] for candidate in candidates),
            "candidate_source_core_files": sum(candidate["source_core_files"] for candidate in candidates),
            "recommended_next_gate": next_gate(spec, gate, term, candidates),
            "authority_boundary": "local_witness_shortlist_not_native_review_not_canonical_terminology",
            "review_packet_population_performed": False,
            "translation_or_revision_performed": False,
            "source_text_copied": False,
            "source_language_terms_copied": False,
            "native_review_status": "not_reviewed",
            "canonical_approval_status": "not_approved",
            "candidates": candidates,
        }
        rows.append(row)

    core_rows = [row for row in rows if row["kind"] == "core_language_lane"]
    extension_rows = [row for row in rows if row["kind"] == "extension_cohort"]
    return {
        "artifact": "local_source_witness_shortlist",
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
            "local_source_evidence_shelf_inventory": INVENTORY_JSON.name,
            "non_slavic_lane_gate_dashboard": LANE_GATE_JSON.name,
            "lane_term_status_summaries": LANE_TERM_STATUS_JSON.name,
            "non_slavic_source_evidence_seed": SOURCE_EVIDENCE_SEED_JSON.name,
        },
        "summary": {
            "lane_or_cohort_count": len(rows),
            "core_language_lanes": len(core_rows),
            "extension_cohorts": len(extension_rows),
            "core_lanes_with_candidate_shelves": sum(1 for row in core_rows if row["candidate_shelves"] > 0),
            "extension_cohorts_with_candidate_shelves": sum(1 for row in extension_rows if row["candidate_shelves"] > 0),
            "candidate_shelf_links": sum(row["candidate_shelves"] for row in rows),
            "candidate_shelves_with_source_core": sum(row["candidate_shelves_with_source_core"] for row in rows),
            "candidate_text_source_like_files": sum(row["candidate_text_source_like_files"] for row in rows),
            "candidate_source_core_files": sum(row["candidate_source_core_files"] for row in rows),
            "lanes_with_zero_term_anchor_rows_but_local_shelf_present": [
                row["lane_or_cohort"]
                for row in core_rows
                if row["term_anchor_rows"] == 0 and row["candidate_shelves"] > 0
            ],
        },
        "shortlist_rows": rows,
        "promotion_rules": [
            "candidate shelves are witnesses to inspect, not terminology approvals",
            "page-context notes must be filled before reviewer packet population",
            "manual/source-review rows must be resolved against source witnesses before translation or revision",
            "Tajik Cyrillic remains zero-term-row until its local witness is promoted through source-language review",
            "extension cohorts need explicit lane authority notes before becoming edition lanes",
        ],
        "boundaries": [
            "This shortlist copies no source-language passages and no source-language term strings.",
            "This is not native/external review, not reviewer packet population, and not translation/revision work.",
            "Local source witnesses are mechanical evidence shelves, not community authority.",
            "No network action was performed.",
            "The active Noether multilingual goal remains open.",
        ],
    }


def write_markdown(document: dict) -> None:
    summary = document["summary"]
    lines = [
        "# Local source-witness shortlist - 2026-06-30",
        "",
        "Status: local source-witness shortlist only. No network action, no review, and no source-passage copying was performed.",
        "",
        "## Summary",
        "",
        f"- Lane/cohort rows: {summary['lane_or_cohort_count']}",
        f"- Core language lanes: {summary['core_language_lanes']}",
        f"- Extension cohorts: {summary['extension_cohorts']}",
        f"- Core lanes with candidate shelves: {summary['core_lanes_with_candidate_shelves']}",
        f"- Candidate shelf links: {summary['candidate_shelf_links']}",
        f"- Candidate shelves with source-core files: {summary['candidate_shelves_with_source_core']}",
        f"- Candidate source-like local files: {summary['candidate_text_source_like_files']}",
        f"- Candidate source-core files: {summary['candidate_source_core_files']}",
        f"- Network actions performed: `{str((not document['no_network_actions_performed'])).lower()}`",
        "",
        "## Shortlist Rows",
        "",
        "| Lane/cohort | Kind | Gate | Candidates | Source-core candidates | Term rows | Next gate |",
        "| --- | --- | --- | ---: | ---: | ---: | --- |",
    ]
    for row in document["shortlist_rows"]:
        lines.append(
            "| `{lane_or_cohort}` | `{kind}` | `{edition_gate}` | {candidate_shelves} | {candidate_shelves_with_source_core} | {term_anchor_rows} | `{recommended_next_gate}` |".format(
                **row
            )
        )
    lines.extend(["", "## Zero-Term Local-Shelf Core Lanes", ""])
    zero_rows = summary["lanes_with_zero_term_anchor_rows_but_local_shelf_present"]
    if zero_rows:
        lines.extend(f"- `{lane}`" for lane in zero_rows)
    else:
        lines.append("- None")
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
        "- Local source-witness shortlist: "
        f"{summary['lane_or_cohort_count']} lane/cohort rows / "
        f"{summary['candidate_shelf_links']} candidate shelf links / "
        f"{summary['candidate_shelves_with_source_core']} source-core-backed candidates / "
        "0 network actions"
    )
    if re.search(r"^- Local source-witness shortlist: .*", text, flags=re.MULTILINE):
        text = re.sub(r"^- Local source-witness shortlist: .*", line, text, flags=re.MULTILINE)
    else:
        marker = "- Local source-evidence shelf inventory:"
        rows = text.splitlines()
        for offset, row in enumerate(rows):
            if row.startswith(marker):
                rows.insert(offset + 1, line)
                text = "\n".join(rows) + "\n"
                break
    text = text.replace(
        "local-source-evidence-shelf inventory metadata",
        "local-source-evidence-shelf inventory/source-witness-shortlist metadata",
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
    manifest["local_source_witness_shortlist"] = {
        "status": document["status"],
        "artifact_markdown": OUT_MD.name,
        "artifact_json": OUT_JSON.name,
        "lane_or_cohort_count": summary["lane_or_cohort_count"],
        "core_language_lanes": summary["core_language_lanes"],
        "extension_cohorts": summary["extension_cohorts"],
        "core_lanes_with_candidate_shelves": summary["core_lanes_with_candidate_shelves"],
        "extension_cohorts_with_candidate_shelves": summary["extension_cohorts_with_candidate_shelves"],
        "candidate_shelf_links": summary["candidate_shelf_links"],
        "candidate_shelves_with_source_core": summary["candidate_shelves_with_source_core"],
        "candidate_text_source_like_files": summary["candidate_text_source_like_files"],
        "candidate_source_core_files": summary["candidate_source_core_files"],
        "zero_term_local_shelf_core_lanes": summary["lanes_with_zero_term_anchor_rows_but_local_shelf_present"],
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
                "shortlist_json": str(OUT_JSON),
                "lane_or_cohort_count": document["summary"]["lane_or_cohort_count"],
                "candidate_shelf_links": document["summary"]["candidate_shelf_links"],
                "candidate_shelves_with_source_core": document["summary"]["candidate_shelves_with_source_core"],
                "zero_term_local_shelf_core_lanes": document["summary"][
                    "lanes_with_zero_term_anchor_rows_but_local_shelf_present"
                ],
                "no_network_actions_performed": document["no_network_actions_performed"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
