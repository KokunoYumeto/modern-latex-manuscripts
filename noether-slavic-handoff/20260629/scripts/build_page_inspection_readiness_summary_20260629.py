import datetime
import hashlib
import json
import pathlib
import re
from collections import defaultdict


BASE = pathlib.Path(__file__).resolve().parents[1]
STATUS_MANIFEST = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_MANIFEST_20260629.json"
STATUS_INDEX = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_INDEX_20260629.md"
OUT_JSON = BASE / "PAGE_INSPECTION_REVIEW_PACKET_READINESS_20260629.json"
OUT_MD = BASE / "PAGE_INSPECTION_REVIEW_PACKET_READINESS_20260629.md"


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


def batch_number(path: pathlib.Path) -> int:
    match = re.search(r"BATCH(\d+)", path.name)
    return int(match.group(1)) if match else 0


def batch_files() -> list[pathlib.Path]:
    return sorted(BASE.glob("PAGE_INSPECTION_BATCH*.json"), key=batch_number)


def artifact_item(path: pathlib.Path, status: str | None = None) -> dict:
    item = {"path": artifact_path(path), "sha256": sha256(path), "bytes": path.stat().st_size}
    if status:
        item["status"] = status
    return item


def upsert_artifact(manifest: dict, group: str, path: pathlib.Path, status: str | None = None) -> None:
    by_path = {item["path"]: item for item in manifest["artifacts"][group]}
    rel = artifact_path(path)
    old_status = by_path.get(rel, {}).get("status")
    by_path[rel] = artifact_item(path, status or old_status)
    manifest["artifacts"][group] = [by_path[key] for key in sorted(by_path)]


def collect_records() -> tuple[list[dict], list[str]]:
    records = []
    batch_names = []
    for path in batch_files():
        batch = load_json(path)
        batch_names.append(path.name)
        for record in batch.get("inspection_records", []):
            records.append(
                {
                    "term_id": record["term_id"],
                    "language_lane": record["language_lane"],
                    "english_concept": record["english_concept"],
                    "mathematical_domain": record["mathematical_domain"],
                    "priority": record["priority"],
                    "inspection_batch_id": record["inspection_batch_id"],
                    "pages_checked": record["pages_checked"],
                    "pages_with_exact_term_occurrence": record["pages_with_exact_term_occurrence"],
                    "exact_term_occurrences_total": record["exact_term_occurrences_total"],
                    "source_context_status_after": record["source_context_status_after"],
                    "ready_for_reviewer_packet_after_extraction_check": record[
                        "ready_for_reviewer_packet_after_extraction_check"
                    ],
                    "reviewer_approval_status": record["reviewer_approval_status"],
                    "canonical_approval_status": record["canonical_approval_status"],
                }
            )
    return records, batch_names


def summarize_by_lane(records: list[dict]) -> list[dict]:
    lanes: dict[str, list[dict]] = defaultdict(list)
    for record in records:
        lanes[record["language_lane"]].append(record)
    rows = []
    for lane in sorted(lanes):
        lane_records = lanes[lane]
        ready = [row for row in lane_records if row["ready_for_reviewer_packet_after_extraction_check"]]
        needs_review = [row for row in lane_records if not row["ready_for_reviewer_packet_after_extraction_check"]]
        rows.append(
            {
                "lane": lane,
                "tasks": len(lane_records),
                "ready_after_extraction_check": len(ready),
                "manual_or_source_review_required": len(needs_review),
                "pages_checked": sum(row["pages_checked"] for row in lane_records),
                "pages_with_exact_term_occurrence": sum(
                    row["pages_with_exact_term_occurrence"] for row in lane_records
                ),
            }
        )
    return rows


def write_markdown(summary: dict) -> None:
    lines = [
        "# Page inspection reviewer-packet readiness - 2026-06-29",
        "",
        "This artifact summarizes completed local extraction inspections for reviewer-packet preparation. It is not native review, not a populated glossary, and not a term approval ledger.",
        "",
        f"Companion machine-readable file: `{OUT_JSON.name}`",
        "",
        "## Totals",
        "",
        f"- Extraction-inspected rows: {summary['totals']['tasks']}",
        f"- Ready after extraction check: {summary['totals']['ready_after_extraction_check']}",
        f"- Manual/source review required before reviewer packet row: {summary['totals']['manual_or_source_review_required']}",
        f"- Pages checked across batches: {summary['totals']['pages_checked']}",
        "- Approved terms: 0",
        "- Accepted corrections: 0",
        "",
        "## Lane Summary",
        "",
        "| Lane | Tasks | Ready | Manual/source review | Pages checked | Pages with exact hit |",
        "| --- | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in summary["lane_summary"]:
        lines.append(
            f"| {row['lane']} | {row['tasks']} | {row['ready_after_extraction_check']} | "
            f"{row['manual_or_source_review_required']} | {row['pages_checked']} | "
            f"{row['pages_with_exact_term_occurrence']} |"
        )
    lines.extend(
        [
            "",
            "## Manual Or Source Review Rows",
            "",
            "| Term ID | Lane | English concept | Domain | Priority | Batch | Pages checked | Status |",
            "| --- | --- | --- | --- | --- | --- | ---: | --- |",
        ]
    )
    for row in summary["manual_or_source_review_rows"]:
        lines.append(
            f"| `{row['term_id']}` | {row['language_lane']} | {row['english_concept']} | "
            f"{row['mathematical_domain']} | {row['priority']} | {row['inspection_batch_id']} | "
            f"{row['pages_checked']} | {row['source_context_status_after']} |"
        )
    lines.extend(
        [
            "",
            "## Boundaries",
            "",
            "- No source-language term strings or source passages are copied here.",
            "- No credentials or tokens are copied here.",
            "- No network action, GitHub upload, or reviewer send is performed here.",
            "- Ready after extraction check is not reviewer approval.",
            "- Rows requiring manual/source review should not be populated into reviewer packets until a human context note resolves the extraction mismatch.",
            "- Canonical approval remains zero until accepted reviewer corrections are ingested.",
            "",
        ]
    )
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def update_status_index(summary: dict, manifest: dict) -> None:
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
    marker = "- Review packet templates seeded: 8 lane/template groups, 13 ledger fields"
    readiness_line = (
        f"- Review-packet readiness after extraction: {summary['totals']['ready_after_extraction_check']} ready / "
        f"{summary['totals']['manual_or_source_review_required']} manual-source-review required"
    )
    text = re.sub(r"- Review-packet readiness after extraction: .*", readiness_line, text)
    if readiness_line not in text:
        text = text.replace(marker, readiness_line + "\n" + marker)
    text = text.replace(
        "page inspection queue/batch metadata, research publication metadata",
        "page inspection queue/batch/readiness metadata, research publication metadata",
    )
    if "Generated UTC: " in text:
        old = text.split("Generated UTC: ", 1)[1].splitlines()[0]
        text = text.replace(old, manifest["generated_utc"], 1)
    STATUS_INDEX.write_text(text, encoding="utf-8")


def update_manifest(summary: dict) -> None:
    manifest = load_json(STATUS_MANIFEST)
    manifest["generated_utc"] = now_utc()
    manifest["page_inspection_reviewer_packet_readiness"] = {
        "status": summary["status"],
        "artifact_markdown": OUT_MD.name,
        "artifact_json": OUT_JSON.name,
        "tasks": summary["totals"]["tasks"],
        "ready_after_extraction_check": summary["totals"]["ready_after_extraction_check"],
        "manual_or_source_review_required": summary["totals"]["manual_or_source_review_required"],
        "pages_checked": summary["totals"]["pages_checked"],
        "no_network_actions_performed": True,
        "credentials_or_tokens_copied": False,
        "source_text_copied": False,
        "source_language_terms_copied": False,
        "native_review_status": "not_reviewed",
        "current_approved_terms": 0,
        "current_accepted_corrections": 0,
    }
    upsert_artifact(
        manifest,
        "json",
        OUT_JSON,
        "review_packet_readiness_summary_from_extraction_inspections_not_native_review",
    )
    upsert_artifact(manifest, "markdown", OUT_MD)
    upsert_artifact(manifest, "scripts", pathlib.Path(__file__))
    update_status_index(summary, manifest)
    write_json(STATUS_MANIFEST, manifest)


def main() -> None:
    records, batch_names = collect_records()
    ready = [row for row in records if row["ready_for_reviewer_packet_after_extraction_check"]]
    needs_review = [row for row in records if not row["ready_for_reviewer_packet_after_extraction_check"]]
    summary = {
        "artifact": "page_inspection_reviewer_packet_readiness",
        "status": "review_packet_readiness_summary_from_extraction_inspections_not_native_review",
        "generated_date": "2026-06-29",
        "generated_utc": now_utc(),
        "no_network_actions_performed": True,
        "credentials_or_tokens_copied": False,
        "source_text_copied": False,
        "source_language_terms_copied": False,
        "queue_artifact": "PAGE_INSPECTION_QUEUE_20260629.json",
        "batch_artifacts": batch_names,
        "totals": {
            "tasks": len(records),
            "ready_after_extraction_check": len(ready),
            "manual_or_source_review_required": len(needs_review),
            "pages_checked": sum(row["pages_checked"] for row in records),
            "pages_with_exact_term_occurrence": sum(row["pages_with_exact_term_occurrence"] for row in records),
            "current_approved_terms": 0,
            "current_accepted_corrections": 0,
        },
        "lane_summary": summarize_by_lane(records),
        "manual_or_source_review_rows": needs_review,
        "ready_reviewer_packet_seed_rows": ready,
        "next_gates": [
            "add human page-context notes for ready rows",
            "manually revisit extraction-mismatch rows before reviewer-packet population",
            "populate reviewer-facing glossary packet rows only after page-context notes are present",
            "keep native/external review and accepted-correction ledger separate from local extraction readiness",
        ],
    }
    write_json(OUT_JSON, summary)
    write_markdown(summary)
    update_manifest(summary)
    print(
        json.dumps(
            {
                "readiness_json": str(OUT_JSON),
                "tasks": summary["totals"]["tasks"],
                "ready": summary["totals"]["ready_after_extraction_check"],
                "manual_or_source_review_required": summary["totals"]["manual_or_source_review_required"],
                "pages_checked": summary["totals"]["pages_checked"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
