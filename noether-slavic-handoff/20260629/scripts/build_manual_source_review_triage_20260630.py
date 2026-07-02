import datetime
import hashlib
import json
import pathlib
import re
from collections import Counter, defaultdict


BASE = pathlib.Path(__file__).resolve().parents[1]
STATUS_MANIFEST = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_MANIFEST_20260629.json"
STATUS_INDEX = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_INDEX_20260629.md"
READINESS_JSON = BASE / "PAGE_INSPECTION_REVIEW_PACKET_READINESS_20260629.json"
OUT_JSON = BASE / "MANUAL_SOURCE_REVIEW_TRIAGE_20260630.json"
OUT_MD = BASE / "MANUAL_SOURCE_REVIEW_TRIAGE_20260630.md"


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


def batch_number(path: pathlib.Path) -> int:
    match = re.search(r"BATCH(\d+)", path.name)
    return int(match.group(1)) if match else 0


def batch_records_by_term_id() -> dict[str, dict]:
    records = {}
    for path in sorted(BASE.glob("PAGE_INSPECTION_BATCH*.json"), key=batch_number):
        batch = load_json(path)
        for record in batch.get("inspection_records", []):
            record = dict(record)
            record["batch_json"] = path.name
            records[record["term_id"]] = record
    return records


def page_status_counts(record: dict) -> Counter:
    counts: Counter = Counter()
    for source in record.get("source_outcomes", []):
        if not source.get("pdf_cache_present"):
            counts["local_pdf_cache_missing"] += 1
        if source.get("pdf_cache_present") and not source.get("pdf_hash_match"):
            counts["pdf_hash_mismatch"] += 1
        for page in source.get("page_outcomes", []):
            counts[page.get("status", "unknown_page_status")] += 1
    return counts


def classify(row: dict, full_record: dict, counts: Counter) -> str:
    if counts.get("local_pdf_cache_missing"):
        return "cache_missing_before_manual_review"
    if counts.get("pdf_hash_mismatch"):
        return "pdf_hash_mismatch_before_manual_review"
    if counts.get("page_text_empty_exact_term_not_reverified"):
        return "ocr_or_text_layer_absent_for_some_pages"
    if row["language_lane"] in {"fa_IR", "prs_AF", "arabic"}:
        return "rtl_register_or_extraction_variant_manual_review"
    if row["mathematical_domain"] in {"module_theory", "representation_theory", "noetherian"}:
        return "specialist_term_variant_or_anchor_manual_review"
    return "exact_term_not_reverified_in_nonempty_text_manual_review"


def action_for(row: dict, issue_class: str) -> str:
    if issue_class in {"cache_missing_before_manual_review", "pdf_hash_mismatch_before_manual_review"}:
        return "repair_local_cache_or_hash_pointer_before_context_review"
    if issue_class == "ocr_or_text_layer_absent_for_some_pages":
        return "use_visual_pdf_page_check_or_ocr_before_packet_population"
    if row["language_lane"] in {"fa_IR", "prs_AF", "arabic"}:
        return "perform_rtl_register_manual_review_and_record_context_note_without_source_quote"
    if row["mathematical_domain"] in {"module_theory", "representation_theory", "noetherian"}:
        return "perform_specialist_term_manual_review_and_record_context_note_without_source_quote"
    return "perform_manual_source_context_review_without_source_quote"


def build_triage() -> dict:
    readiness = load_json(READINESS_JSON)
    full_records = batch_records_by_term_id()
    items = []
    for row in readiness["manual_or_source_review_rows"]:
        full = full_records[row["term_id"]]
        counts = page_status_counts(full)
        issue_class = classify(row, full, counts)
        source_count = len(full.get("source_outcomes", []))
        cache_missing_sources = sum(1 for source in full.get("source_outcomes", []) if not source.get("pdf_cache_present"))
        hash_mismatch_sources = sum(
            1
            for source in full.get("source_outcomes", [])
            if source.get("pdf_cache_present") and not source.get("pdf_hash_match")
        )
        items.append(
            {
                "term_id": row["term_id"],
                "language_lane": row["language_lane"],
                "english_concept": row["english_concept"],
                "mathematical_domain": row["mathematical_domain"],
                "priority": row["priority"],
                "inspection_batch_id": row["inspection_batch_id"],
                "batch_json": full["batch_json"],
                "pages_checked": row["pages_checked"],
                "sources_checked": source_count,
                "cache_missing_sources": cache_missing_sources,
                "hash_mismatch_sources": hash_mismatch_sources,
                "page_status_counts": dict(sorted(counts.items())),
                "issue_class": issue_class,
                "recommended_action": action_for(row, issue_class),
                "packet_population_status": "blocked_until_manual_source_review_note",
                "source_text_copied": False,
                "source_language_terms_copied": False,
                "native_review_status": "not_reviewed",
                "canonical_approval_status": "not_approved",
            }
        )
    return triage_document(items)


def triage_document(items: list[dict]) -> dict:
    lane_summary = []
    by_lane: dict[str, list[dict]] = defaultdict(list)
    for item in items:
        by_lane[item["language_lane"]].append(item)
    for lane in sorted(by_lane):
        lane_items = by_lane[lane]
        issue_counts = Counter(item["issue_class"] for item in lane_items)
        lane_summary.append(
            {
                "lane": lane,
                "manual_source_review_rows": len(lane_items),
                "high_priority_rows": sum(1 for item in lane_items if item["priority"] == "high"),
                "medium_priority_rows": sum(1 for item in lane_items if item["priority"] == "medium"),
                "pages_checked": sum(item["pages_checked"] for item in lane_items),
                "issue_class_counts": dict(sorted(issue_counts.items())),
            }
        )
    issue_summary = Counter(item["issue_class"] for item in items)
    domain_summary = Counter(item["mathematical_domain"] for item in items)
    return {
        "artifact": "manual_source_review_triage",
        "status": "manual_source_review_triage_not_review_result_not_approval",
        "generated_date": "2026-06-30",
        "generated_utc": now_utc(),
        "no_network_actions_performed": True,
        "credentials_or_tokens_copied": False,
        "source_text_copied": False,
        "source_language_terms_copied": False,
        "readiness_artifact": READINESS_JSON.name,
        "totals": {
            "manual_source_review_rows": len(items),
            "high_priority_rows": sum(1 for item in items if item["priority"] == "high"),
            "medium_priority_rows": sum(1 for item in items if item["priority"] == "medium"),
            "pages_checked": sum(item["pages_checked"] for item in items),
            "cache_missing_sources": sum(item["cache_missing_sources"] for item in items),
            "hash_mismatch_sources": sum(item["hash_mismatch_sources"] for item in items),
            "current_approved_terms": 0,
            "current_accepted_corrections": 0,
        },
        "issue_class_summary": dict(sorted(issue_summary.items())),
        "domain_summary": dict(sorted(domain_summary.items())),
        "lane_summary": lane_summary,
        "triage_items": items,
        "next_gates": [
            "perform manual source-context checks without copying source passages",
            "record context notes or extraction-mismatch resolutions",
            "populate reviewer-packet rows only after manual/source review is resolved",
            "keep native/external reviewer approval separate from local triage",
        ],
    }


def write_markdown(triage: dict) -> None:
    lines = [
        "# Manual/source review triage - 2026-06-30",
        "",
        "This artifact triages extraction-mismatch rows that remain blocked before reviewer-packet population. It is not native review, not a populated packet, and not a term approval ledger.",
        "",
        f"Companion machine-readable file: `{OUT_JSON.name}`",
        "",
        "## Totals",
        "",
        f"- Manual/source-review rows: {triage['totals']['manual_source_review_rows']}",
        f"- High-priority rows: {triage['totals']['high_priority_rows']}",
        f"- Medium-priority rows: {triage['totals']['medium_priority_rows']}",
        f"- Pages checked in blocked rows: {triage['totals']['pages_checked']}",
        f"- Cache-missing source records: {triage['totals']['cache_missing_sources']}",
        f"- Hash-mismatch source records: {triage['totals']['hash_mismatch_sources']}",
        "- Approved terms: 0",
        "- Accepted corrections: 0",
        "",
        "## Issue Classes",
        "",
        "| Issue class | Rows |",
        "| --- | ---: |",
    ]
    for issue_class, count in triage["issue_class_summary"].items():
        lines.append(f"| {issue_class} | {count} |")
    lines.extend(["", "## Lane Summary", "", "| Lane | Rows | High | Medium | Pages checked | Issue classes |", "| --- | ---: | ---: | ---: | ---: | --- |"])
    for row in triage["lane_summary"]:
        issue_bits = ", ".join(f"{key}:{value}" for key, value in row["issue_class_counts"].items())
        lines.append(
            f"| {row['lane']} | {row['manual_source_review_rows']} | {row['high_priority_rows']} | "
            f"{row['medium_priority_rows']} | {row['pages_checked']} | {issue_bits} |"
        )
    lines.extend(
        [
            "",
            "## Triage Rows",
            "",
            "| Term ID | Lane | English concept | Domain | Priority | Pages | Issue class | Recommended action |",
            "| --- | --- | --- | --- | --- | ---: | --- | --- |",
        ]
    )
    for item in triage["triage_items"]:
        lines.append(
            f"| `{item['term_id']}` | {item['language_lane']} | {item['english_concept']} | "
            f"{item['mathematical_domain']} | {item['priority']} | {item['pages_checked']} | "
            f"{item['issue_class']} | {item['recommended_action']} |"
        )
    lines.extend(
        [
            "",
            "## Boundaries",
            "",
            "- No source-language term strings or source passages are copied here.",
            "- No credentials or tokens are copied here.",
            "- No network action, GitHub upload, or reviewer send is performed here.",
            "- Triage classes are local workflow labels, not reviewer decisions.",
            "- Rows remain blocked until manual/source review notes are recorded.",
            "- No term is approved for canonical use by this artifact.",
            "",
        ]
    )
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def update_status_index(triage: dict, manifest: dict) -> None:
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
        f"- Manual/source review triage: {triage['totals']['manual_source_review_rows']} rows / "
        f"{triage['totals']['cache_missing_sources']} cache-missing / "
        f"{triage['totals']['hash_mismatch_sources']} hash-mismatch"
    )
    text = re.sub(r"- Manual/source review triage: .*", line, text)
    if line not in text:
        marker = "- Page-context note worklist:"
        rows = text.splitlines()
        for offset, row in enumerate(rows):
            if row.startswith(marker):
                rows.insert(offset + 1, line)
                text = "\n".join(rows) + "\n"
                break
    text = text.replace(
        "page inspection queue/batch/readiness/context-note/reviewer-scaffold/local-handoff metadata",
        "page inspection queue/batch/readiness/context-note/manual-triage/reviewer-scaffold/local-handoff metadata",
    )
    if "Generated UTC: " in text:
        old = text.split("Generated UTC: ", 1)[1].splitlines()[0]
        text = text.replace(old, manifest["generated_utc"], 1)
    STATUS_INDEX.write_text(text, encoding="utf-8")


def update_manifest(triage: dict) -> None:
    manifest = load_json(STATUS_MANIFEST)
    manifest["generated_utc"] = now_utc()
    manifest["manual_source_review_triage"] = {
        "status": triage["status"],
        "artifact_markdown": OUT_MD.name,
        "artifact_json": OUT_JSON.name,
        "manual_source_review_rows": triage["totals"]["manual_source_review_rows"],
        "high_priority_rows": triage["totals"]["high_priority_rows"],
        "medium_priority_rows": triage["totals"]["medium_priority_rows"],
        "cache_missing_sources": triage["totals"]["cache_missing_sources"],
        "hash_mismatch_sources": triage["totals"]["hash_mismatch_sources"],
        "no_network_actions_performed": True,
        "credentials_or_tokens_copied": False,
        "source_text_copied": False,
        "source_language_terms_copied": False,
        "native_review_status": "not_reviewed",
        "current_approved_terms": 0,
        "current_accepted_corrections": 0,
    }
    upsert_artifact(manifest, "json", OUT_JSON, "manual_source_review_triage_not_review_result_not_approval")
    upsert_artifact(manifest, "markdown", OUT_MD)
    upsert_artifact(manifest, "scripts", pathlib.Path(__file__))
    update_status_index(triage, manifest)
    write_json(STATUS_MANIFEST, manifest)


def main() -> None:
    triage = build_triage()
    write_json(OUT_JSON, triage)
    write_markdown(triage)
    update_manifest(triage)
    print(
        json.dumps(
            {
                "triage_json": str(OUT_JSON),
                "manual_source_review_rows": triage["totals"]["manual_source_review_rows"],
                "cache_missing_sources": triage["totals"]["cache_missing_sources"],
                "hash_mismatch_sources": triage["totals"]["hash_mismatch_sources"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
