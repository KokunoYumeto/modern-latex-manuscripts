import datetime
import hashlib
import json
import math
import pathlib
import re


BASE = pathlib.Path(__file__).resolve().parents[1]
STATUS_MANIFEST = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_MANIFEST_20260629.json"
STATUS_INDEX = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_INDEX_20260629.md"
SOURCE_CORE_GAP_JSON = BASE / "SELECTED_SOURCE_WITNESS_SOURCE_CORE_COVERAGE_GAP_20260630.json"
SOURCE_CORE_SNAPSHOT_JSON = BASE / "NOETHER_SOURCE_CORE_TEXT_TEX_WORKBOOKS_SNAPSHOT_20260629.json"
SPLIT_PLAN_JSON = BASE / "SOURCE_CORE_SPLIT_UPLOAD_STAGING_PLAN_20260630.json"
OUT_JSON = BASE / "SELECTED_SOURCE_WITNESS_TEXT_TEX_DELTA_STAGING_PLAN_20260630.json"
OUT_MD = BASE / "SELECTED_SOURCE_WITNESS_TEXT_TEX_DELTA_STAGING_PLAN_20260630.md"
SELF_PATH = pathlib.Path(__file__).resolve()

STATUS = "selected_source_witness_text_tex_delta_staging_plan_no_archive_no_network"


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


def priority_rank(row: dict) -> tuple[int, int, str]:
    priority = row.get("delta_upload_priority", "")
    if priority == "high_delta_candidate_for_manual_review_lane":
        bucket = 0
    elif priority == "high_delta_candidate_for_ready_note_lane":
        bucket = 1
    elif priority == "medium_partial_delta_candidate":
        bucket = 2
    elif priority == "medium_delta_candidate_for_support_or_discovery":
        bucket = 3
    elif priority == "low_partial_delta_candidate":
        bucket = 4
    else:
        bucket = 5
    return (bucket, -int(row.get("source_core_text_like_gap_estimate") or 0), row.get("path", ""))


def stage_rows(gap: dict, avg_bytes_per_file: float) -> list[dict]:
    rows = []
    for row in gap.get("unique_witness_shelf_coverage_rows", []):
        gap_files = int(row.get("source_core_text_like_gap_estimate") or 0)
        if gap_files <= 0:
            continue
        estimated_uncompressed = int(math.ceil(gap_files * avg_bytes_per_file))
        rows.append(
            {
                "path": row.get("path"),
                "batch": row.get("batch"),
                "bucket": row.get("bucket"),
                "lanes_or_cohorts": row.get("lanes_or_cohorts", []),
                "source_gate_uses": row.get("source_gate_uses", []),
                "coverage_status": row.get("coverage_status"),
                "delta_upload_priority": row.get("delta_upload_priority"),
                "text_source_like_gap_files": gap_files,
                "tex_files_on_shelf": int(row.get("tex_files") or 0),
                "source_core_files_currently_represented": int(row.get("source_core_files_currently_represented") or 0),
                "estimated_uncompressed_bytes": estimated_uncompressed,
                "pdf_files_counted_not_packaged": int(row.get("pdf_files_counted_not_packaged") or 0),
                "image_files_counted_not_packaged": int(row.get("image_files_counted_not_packaged") or 0),
                "archive_files_counted_not_packaged": int(row.get("archive_files_counted_not_packaged") or 0),
                "actual_file_list_created": False,
                "actual_delta_archive_created": False,
                "actual_remote_upload_performed": False,
                "source_text_copied": False,
                "source_language_terms_copied": False,
            }
        )
    return sorted(rows, key=priority_rank)


def make_chunks(rows: list[dict], target_uncompressed_bytes: int, compression_ratio: float, max_compressed_bytes: int) -> list[dict]:
    chunks = []
    current: list[dict] = []
    current_bytes = 0

    def flush() -> None:
        nonlocal current, current_bytes
        if not current:
            return
        estimated_compressed = int(math.ceil(current_bytes * compression_ratio))
        chunk_id = f"selected-witness-text-tex-delta-{len(chunks) + 1:02d}"
        chunks.append(
            {
                "chunk_id": chunk_id,
                "status": "planned_not_created_not_uploaded",
                "shelf_count": len(current),
                "text_source_like_gap_files": sum(row["text_source_like_gap_files"] for row in current),
                "estimated_uncompressed_bytes": current_bytes,
                "estimated_compressed_bytes": estimated_compressed,
                "estimated_compressed_under_20mb": estimated_compressed <= max_compressed_bytes,
                "delta_archive_created": False,
                "remote_upload_performed": False,
                "pdf_image_archive_payloads_included": False,
                "source_text_copied": False,
                "source_language_terms_copied": False,
                "shelves": current,
            }
        )
        current = []
        current_bytes = 0

    for row in rows:
        row_bytes = int(row["estimated_uncompressed_bytes"])
        if current and current_bytes + row_bytes > target_uncompressed_bytes:
            flush()
        current.append(row)
        current_bytes += row_bytes
    flush()
    return chunks


def lane_rows(rows: list[dict]) -> list[dict]:
    lanes = sorted({lane for row in rows for lane in row.get("lanes_or_cohorts", [])})
    output = []
    for lane in lanes:
        lane_shelves = [row for row in rows if lane in row.get("lanes_or_cohorts", [])]
        output.append(
            {
                "lane_or_cohort": lane,
                "planned_delta_shelves": len(lane_shelves),
                "text_source_like_gap_files": sum(row["text_source_like_gap_files"] for row in lane_shelves),
                "tex_files_on_shelves": sum(row["tex_files_on_shelf"] for row in lane_shelves),
                "estimated_uncompressed_bytes": sum(row["estimated_uncompressed_bytes"] for row in lane_shelves),
                "high_delta_candidate_shelves": sum(
                    1 for row in lane_shelves if row["delta_upload_priority"].startswith("high_delta_candidate")
                ),
                "pdf_files_counted_not_packaged": sum(row["pdf_files_counted_not_packaged"] for row in lane_shelves),
                "image_files_counted_not_packaged": sum(row["image_files_counted_not_packaged"] for row in lane_shelves),
                "archive_files_counted_not_packaged": sum(row["archive_files_counted_not_packaged"] for row in lane_shelves),
                "actual_file_list_created": False,
                "actual_delta_archive_created": False,
                "actual_remote_upload_performed": False,
                "source_text_copied": False,
                "source_language_terms_copied": False,
            }
        )
    return output


def build_document(manifest: dict) -> dict:
    gap = load_json(SOURCE_CORE_GAP_JSON)
    snapshot = load_json(SOURCE_CORE_SNAPSHOT_JSON)
    split_plan = load_json(SPLIT_PLAN_JSON)
    avg_bytes = snapshot["included_bytes_uncompressed"] / snapshot["included_files"]
    policy = split_plan.get("chunking_policy", {})
    target_uncompressed = int(policy.get("target_uncompressed_bytes_per_chunk") or 40 * 1024 * 1024)
    max_compressed = int(policy.get("max_planned_compressed_bytes") or 20 * 1024 * 1024)
    compression_ratio = float(policy.get("compression_ratio_estimate_from_existing_archive") or 0.253)
    rows = stage_rows(gap, avg_bytes)
    chunks = make_chunks(rows, target_uncompressed, compression_ratio, max_compressed)
    lane_summary_rows = lane_rows(rows)
    estimated_uncompressed = sum(row["estimated_uncompressed_bytes"] for row in rows)
    estimated_compressed = sum(chunk["estimated_compressed_bytes"] for chunk in chunks)
    return {
        "artifact": "selected_source_witness_text_tex_delta_staging_plan",
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
            "selected_source_witness_source_core_coverage_gap": SOURCE_CORE_GAP_JSON.name,
            "source_core_snapshot": SOURCE_CORE_SNAPSHOT_JSON.name,
            "source_core_split_upload_plan": SPLIT_PLAN_JSON.name,
            "status_manifest": STATUS_MANIFEST.name,
        },
        "staging_policy": {
            "metadata_only": True,
            "actual_file_list_created": False,
            "actual_delta_archive_created": False,
            "actual_remote_upload_performed": False,
            "target_uncompressed_bytes_per_chunk": target_uncompressed,
            "max_planned_compressed_bytes": max_compressed,
            "compression_ratio_estimate_from_existing_archive": compression_ratio,
            "average_source_core_bytes_per_file_estimate": avg_bytes,
            "pdf_image_archive_payloads_included": False,
            "copy_file_names": False,
            "copy_source_passages": False,
            "copy_source_language_terms": False,
        },
        "summary": {
            "planned_delta_shelves": len(rows),
            "planned_delta_lanes_or_cohorts": len(lane_summary_rows),
            "planned_text_source_like_gap_files": sum(row["text_source_like_gap_files"] for row in rows),
            "planned_tex_files_on_shelves": sum(row["tex_files_on_shelf"] for row in rows),
            "high_delta_candidate_shelves": sum(
                1 for row in rows if row["delta_upload_priority"].startswith("high_delta_candidate")
            ),
            "planned_chunks": len(chunks),
            "planned_chunks_estimated_under_20mb": sum(1 for chunk in chunks if chunk["estimated_compressed_under_20mb"]),
            "planned_chunks_estimated_over_20mb": sum(1 for chunk in chunks if not chunk["estimated_compressed_under_20mb"]),
            "estimated_uncompressed_bytes": estimated_uncompressed,
            "estimated_compressed_bytes": estimated_compressed,
            "pdf_files_counted_not_packaged": gap.get("summary", {}).get("pdf_files_counted_not_packaged", 0),
            "image_files_counted_not_packaged": gap.get("summary", {}).get("image_files_counted_not_packaged", 0),
            "archive_files_counted_not_packaged": gap.get("summary", {}).get("archive_files_counted_not_packaged", 0),
            "actual_file_list_created": False,
            "actual_delta_archive_created": False,
            "actual_remote_upload_performed": False,
            "inspection_outputs_filled": False,
            "review_packet_population_performed": False,
            "translation_or_revision_performed": False,
            "native_review_status": "not_reviewed",
            "current_approved_terms": 0,
            "current_accepted_corrections": 0,
        },
        "lane_delta_rows": lane_summary_rows,
        "planned_chunks": chunks,
        "deferred_payloads": [
            {
                "id": "selected_witness_pdf_image_archive_payloads",
                "status": "deferred_counted_not_packaged",
                "pdf_files": gap.get("summary", {}).get("pdf_files_counted_not_packaged", 0),
                "image_files": gap.get("summary", {}).get("image_files_counted_not_packaged", 0),
                "archive_files": gap.get("summary", {}).get("archive_files_counted_not_packaged", 0),
                "requires_specific_review_need": True,
                "performed_now": False,
            }
        ],
        "boundaries": [
            "This is a staging plan only; it creates no file list and no archive.",
            "Text/TeX delta sizes are estimates based on current source-core average bytes per file.",
            "PDF/image/archive payloads are counted only and deferred.",
            "No source passages, source-language term strings, or per-file inventories are copied.",
            "No network or GitHub action was performed.",
        ],
    }


def write_markdown(document: dict) -> None:
    summary = document["summary"]
    lines = [
        "# Selected source-witness text/TeX delta staging plan - 2026-06-30",
        "",
        "Status: metadata-only staging plan. No file list, archive, network action, review, translation, or source-passage copying was performed.",
        "",
        "## Summary",
        "",
        f"- Planned delta shelves: {summary['planned_delta_shelves']}",
        f"- Planned lanes/cohorts: {summary['planned_delta_lanes_or_cohorts']}",
        f"- Planned text/source-like gap files: {summary['planned_text_source_like_gap_files']}",
        f"- Planned chunks: {summary['planned_chunks']}",
        f"- Chunks estimated under/over 20 MB compressed: {summary['planned_chunks_estimated_under_20mb']} / {summary['planned_chunks_estimated_over_20mb']}",
        f"- Estimated uncompressed bytes: {summary['estimated_uncompressed_bytes']}",
        f"- Estimated compressed bytes: {summary['estimated_compressed_bytes']}",
        f"- Actual file list/archive/upload created: `{str(summary['actual_file_list_created']).lower()}` / `{str(summary['actual_delta_archive_created']).lower()}` / `{str(summary['actual_remote_upload_performed']).lower()}`",
        "",
        "## Lane Delta Rows",
        "",
        "| Lane/cohort | Shelves | Gap files | TeX on shelves | Est. bytes | High-priority shelves |",
        "| --- | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in document["lane_delta_rows"]:
        lines.append(
            f"| `{row['lane_or_cohort']}` | {row['planned_delta_shelves']} | {row['text_source_like_gap_files']} | {row['tex_files_on_shelves']} | {row['estimated_uncompressed_bytes']} | {row['high_delta_candidate_shelves']} |"
        )
    lines.extend(["", "## Planned Chunks", ""])
    lines.extend(
        f"- `{chunk['chunk_id']}`: {chunk['shelf_count']} shelves / {chunk['text_source_like_gap_files']} gap files / estimated compressed {chunk['estimated_compressed_bytes']} bytes / created `{str(chunk['delta_archive_created']).lower()}`"
        for chunk in document["planned_chunks"]
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
        "- Selected source-witness text/TeX delta staging plan: "
        f"{summary['planned_delta_shelves']} shelves / "
        f"{summary['planned_text_source_like_gap_files']} gap files / "
        f"{summary['planned_chunks']} planned chunks / "
        "0 network actions"
    )
    if re.search(r"^- Selected source-witness text/TeX delta staging plan: .*", text, flags=re.MULTILINE):
        text = re.sub(r"^- Selected source-witness text/TeX delta staging plan: .*", line, text, flags=re.MULTILINE)
    else:
        marker = "- Selected source-witness source-core coverage gap:"
        rows = text.splitlines()
        for offset, row in enumerate(rows):
            if row.startswith(marker):
                rows.insert(offset + 1, line)
                text = "\n".join(rows) + "\n"
                break
    text = text.replace(
        "local-source-evidence-shelf inventory/source-witness-shortlist/selection-matrix/inspection-packet/filesystem-validation/source-core-gap metadata",
        "local-source-evidence-shelf inventory/source-witness-shortlist/selection-matrix/inspection-packet/filesystem-validation/source-core-gap/delta-staging metadata",
    )
    text = text.replace("delta-staging/delta-staging metadata", "delta-staging metadata")
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
    manifest["selected_source_witness_text_tex_delta_staging_plan"] = {
        "status": document["status"],
        "artifact_markdown": OUT_MD.name,
        "artifact_json": OUT_JSON.name,
        "planned_delta_shelves": summary["planned_delta_shelves"],
        "planned_delta_lanes_or_cohorts": summary["planned_delta_lanes_or_cohorts"],
        "planned_text_source_like_gap_files": summary["planned_text_source_like_gap_files"],
        "planned_tex_files_on_shelves": summary["planned_tex_files_on_shelves"],
        "high_delta_candidate_shelves": summary["high_delta_candidate_shelves"],
        "planned_chunks": summary["planned_chunks"],
        "planned_chunks_estimated_under_20mb": summary["planned_chunks_estimated_under_20mb"],
        "planned_chunks_estimated_over_20mb": summary["planned_chunks_estimated_over_20mb"],
        "estimated_uncompressed_bytes": summary["estimated_uncompressed_bytes"],
        "estimated_compressed_bytes": summary["estimated_compressed_bytes"],
        "pdf_files_counted_not_packaged": summary["pdf_files_counted_not_packaged"],
        "image_files_counted_not_packaged": summary["image_files_counted_not_packaged"],
        "archive_files_counted_not_packaged": summary["archive_files_counted_not_packaged"],
        "actual_file_list_created": False,
        "actual_delta_archive_created": False,
        "actual_remote_upload_performed": False,
        "inspection_outputs_filled": False,
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
                "delta_staging_plan_json": str(OUT_JSON),
                "planned_delta_shelves": document["summary"]["planned_delta_shelves"],
                "planned_text_source_like_gap_files": document["summary"]["planned_text_source_like_gap_files"],
                "planned_chunks": document["summary"]["planned_chunks"],
                "planned_chunks_estimated_under_20mb": document["summary"]["planned_chunks_estimated_under_20mb"],
                "estimated_compressed_bytes": document["summary"]["estimated_compressed_bytes"],
                "actual_delta_archive_created": document["summary"]["actual_delta_archive_created"],
                "no_network_actions_performed": document["no_network_actions_performed"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
