import datetime
import hashlib
import json
import math
import pathlib
import re
from collections import Counter, defaultdict


BASE = pathlib.Path(__file__).resolve().parents[1]
STATUS_MANIFEST = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_MANIFEST_20260629.json"
STATUS_INDEX = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_INDEX_20260629.md"
DELTA_FILELIST_JSON = BASE / "SELECTED_SOURCE_WITNESS_TEXT_TEX_DELTA_FILELIST_20260630.json"
REBALANCE_PLAN_JSON = BASE / "SELECTED_SOURCE_WITNESS_TEXT_TEX_DELTA_CHUNK_REBALANCE_PLAN_20260630.json"
SPLIT_PLAN_JSON = BASE / "SOURCE_CORE_SPLIT_UPLOAD_STAGING_PLAN_20260630.json"
OUT_JSON = BASE / "SELECTED_SOURCE_WITNESS_TEXT_TEX_DELTA_DEDUPED_UPLOAD_CANDIDATE_PLAN_20260630.json"
OUT_MD = BASE / "SELECTED_SOURCE_WITNESS_TEXT_TEX_DELTA_DEDUPED_UPLOAD_CANDIDATE_PLAN_20260630.md"
SELF_PATH = pathlib.Path(__file__).resolve()

STATUS = "selected_source_witness_text_tex_delta_deduped_upload_candidate_plan_no_archive_no_network"


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


def estimate_compressed(bytes_uncompressed: int, ratio: float) -> int:
    return int(math.ceil(bytes_uncompressed * ratio))


def rebalance_new_content(rows: list[dict], target_uncompressed: int, ratio: float, max_compressed: int) -> tuple[list[dict], list[dict]]:
    sorted_rows = sorted(rows, key=lambda row: (-int(row["bytes"]), row["file_id"]))
    chunk_work: list[dict] = []
    for row in sorted_rows:
        row_bytes = int(row["bytes"])
        if row_bytes > target_uncompressed:
            chunk_work.append({"rows": [row], "bytes": row_bytes, "singleton_oversize_file": True})
            continue
        placed = False
        for chunk in chunk_work:
            if chunk.get("singleton_oversize_file"):
                continue
            if chunk["bytes"] + row_bytes <= target_uncompressed:
                chunk["rows"].append(row)
                chunk["bytes"] += row_bytes
                placed = True
                break
        if not placed:
            chunk_work.append({"rows": [row], "bytes": row_bytes, "singleton_oversize_file": False})

    chunk_rows = []
    assignments = []
    for index, chunk in enumerate(chunk_work, start=1):
        chunk_id = f"selected-witness-text-tex-delta-deduped-{index:02d}"
        rows_in_chunk = sorted(chunk["rows"], key=lambda row: row["file_id"])
        estimated_compressed = estimate_compressed(chunk["bytes"], ratio)
        lanes = sorted({lane for row in rows_in_chunk for lane in row.get("lanes_or_cohorts", [])})
        chunk_rows.append(
            {
                "deduped_chunk_id": chunk_id,
                "upload_candidate_file_rows": len(rows_in_chunk),
                "bytes": chunk["bytes"],
                "estimated_compressed_bytes": estimated_compressed,
                "estimated_compressed_under_20mb": estimated_compressed <= max_compressed,
                "exceeds_soft_uncompressed_target": chunk["bytes"] > target_uncompressed,
                "singleton_oversize_file_chunk": bool(chunk.get("singleton_oversize_file")),
                "lane_or_cohort_count": len(lanes),
                "lanes_or_cohorts": lanes,
                "tex_family_files": sum(1 for row in rows_in_chunk if row.get("is_tex_family")),
                "extension_counts": dict(sorted(Counter(row["extension"] for row in rows_in_chunk).items())),
                "actual_chunk_archive_created": False,
                "actual_remote_upload_performed": False,
                "source_text_copied": False,
                "source_language_terms_copied": False,
            }
        )
        for row in rows_in_chunk:
            assignments.append(
                {
                    "file_id": row["file_id"],
                    "deduped_chunk_id": chunk_id,
                    "source_filelist_chunk_id": row["chunk_id"],
                    "bytes": row["bytes"],
                    "sha256": row["sha256"],
                    "extension": row["extension"],
                    "is_tex_family": row["is_tex_family"],
                    "lanes_or_cohorts": row.get("lanes_or_cohorts", []),
                    "upload_candidate_reason": "content_hash_not_represented_in_source_core",
                    "source_text_copied": False,
                    "source_language_terms_copied": False,
                    "file_content_copied": False,
                }
            )
    return chunk_rows, sorted(assignments, key=lambda row: row["file_id"])


def alias_rows(rows: list[dict]) -> list[dict]:
    return [
        {
            "file_id": row["file_id"],
            "source_filelist_chunk_id": row["chunk_id"],
            "bytes": row["bytes"],
            "sha256": row["sha256"],
            "extension": row["extension"],
            "is_tex_family": row["is_tex_family"],
            "lanes_or_cohorts": row.get("lanes_or_cohorts", []),
            "alias_reason": "content_hash_already_represented_in_source_core",
            "upload_candidate": False,
            "source_text_copied": False,
            "source_language_terms_copied": False,
            "file_content_copied": False,
        }
        for row in sorted(rows, key=lambda item: item["file_id"])
    ]


def summarize_lanes(rows: list[dict], key_name: str) -> list[dict]:
    lanes: dict[str, dict] = defaultdict(lambda: {"file_rows": 0, "bytes": 0, "tex_family_files": 0})
    for row in rows:
        for lane in row.get("lanes_or_cohorts", []):
            lanes[lane]["file_rows"] += 1
            lanes[lane]["bytes"] += row["bytes"]
            lanes[lane]["tex_family_files"] += 1 if row["is_tex_family"] else 0
    return [
        {"lane_or_cohort": lane, key_name: values["file_rows"], "bytes": values["bytes"], "tex_family_files": values["tex_family_files"]}
        for lane, values in sorted(lanes.items())
    ]


def summarize_extensions(rows: list[dict], key_name: str) -> list[dict]:
    values: dict[str, dict] = defaultdict(lambda: {"file_rows": 0, "bytes": 0})
    for row in rows:
        values[row["extension"]]["file_rows"] += 1
        values[row["extension"]]["bytes"] += row["bytes"]
    return [{"extension": ext, key_name: data["file_rows"], "bytes": data["bytes"]} for ext, data in sorted(values.items())]


def build_summary(filelist: dict, rebalance_plan: dict, chunks: list[dict], upload_assignments: list[dict], aliases: list[dict], target: int, max_compressed: int, ratio: float) -> dict:
    filelist_summary = filelist.get("summary", {})
    rebalance_summary = rebalance_plan.get("summary", {})
    upload_bytes = sum(row["bytes"] for row in upload_assignments)
    alias_bytes = sum(row["bytes"] for row in aliases)
    return {
        "source_filelist_rows": filelist_summary.get("delta_file_rows", 0),
        "source_filelist_bytes": filelist_summary.get("delta_bytes", 0),
        "source_rebalanced_chunks": rebalance_summary.get("rebalanced_chunks", 0),
        "deduped_upload_candidate_rows": len(upload_assignments),
        "deduped_upload_candidate_bytes": upload_bytes,
        "deduped_upload_candidate_tex_family_files": sum(1 for row in upload_assignments if row["is_tex_family"]),
        "path_alias_metadata_rows": len(aliases),
        "path_alias_metadata_bytes": alias_bytes,
        "path_alias_tex_family_files": sum(1 for row in aliases if row["is_tex_family"]),
        "deduped_rows_plus_alias_rows": len(upload_assignments) + len(aliases),
        "deduped_bytes_plus_alias_bytes": upload_bytes + alias_bytes,
        "target_uncompressed_bytes_per_chunk": target,
        "max_planned_compressed_bytes": max_compressed,
        "compression_ratio_estimate_from_existing_archive": ratio,
        "deduped_chunks": len(chunks),
        "deduped_chunks_over_soft_target": sum(1 for row in chunks if row["exceeds_soft_uncompressed_target"]),
        "deduped_singleton_oversize_file_chunks": sum(1 for row in chunks if row["singleton_oversize_file_chunk"]),
        "deduped_individual_files_over_soft_target": sum(1 for row in upload_assignments if row["bytes"] > target),
        "deduped_chunks_estimated_under_20mb": sum(1 for row in chunks if row["estimated_compressed_under_20mb"]),
        "deduped_chunks_estimated_over_20mb": sum(1 for row in chunks if not row["estimated_compressed_under_20mb"]),
        "deduped_estimated_compressed_bytes_total": sum(row["estimated_compressed_bytes"] for row in chunks),
        "deduped_max_chunk_bytes": max((row["bytes"] for row in chunks), default=0),
        "deduped_min_chunk_bytes": min((row["bytes"] for row in chunks), default=0),
        "actual_chunk_archives_created": 0,
        "actual_remote_uploads_performed": 0,
        "network_actions_performed": 0,
        "review_packet_population_performed": False,
        "translation_or_revision_performed": False,
        "canonical_completion_claim": False,
        "publication_completion_claim": False,
        "native_review_status": "not_reviewed",
        "current_approved_terms": 0,
        "current_accepted_corrections": 0,
    }


def build_document(manifest: dict) -> dict:
    filelist = load_json(DELTA_FILELIST_JSON)
    rebalance_plan = load_json(REBALANCE_PLAN_JSON)
    split_plan = load_json(SPLIT_PLAN_JSON)
    policy = split_plan.get("chunking_policy", {})
    target = int(policy.get("target_uncompressed_bytes_per_chunk") or 40 * 1024 * 1024)
    max_compressed = int(policy.get("max_planned_compressed_bytes") or 20 * 1024 * 1024)
    ratio = float(policy.get("compression_ratio_estimate_from_existing_archive") or 0.253)
    upload_rows = [row for row in filelist.get("file_rows", []) if not row.get("content_hash_already_represented_in_source_core")]
    represented_rows = [row for row in filelist.get("file_rows", []) if row.get("content_hash_already_represented_in_source_core")]
    chunks, upload_assignments = rebalance_new_content(upload_rows, target, ratio, max_compressed)
    aliases = alias_rows(represented_rows)
    return {
        "artifact": "selected_source_witness_text_tex_delta_deduped_upload_candidate_plan",
        "generated_utc": now_utc(),
        "generated_date": "20260630",
        "status": STATUS,
        "bandwidth_mode": "local_only_no_network_actions",
        "inputs": {
            "status_manifest": STATUS_MANIFEST.name,
            "delta_filelist": DELTA_FILELIST_JSON.name,
            "chunk_rebalance_plan": REBALANCE_PLAN_JSON.name,
            "source_core_split_plan": SPLIT_PLAN_JSON.name,
        },
        "dedupe_policy": {
            "metadata_only_no_file_content": True,
            "new_content_hash_rows_only_are_upload_candidates": True,
            "existing_content_hash_rows_are_path_alias_metadata": True,
            "source_text_or_passages_not_copied": True,
            "source_language_terms_not_copied": True,
            "actual_archives_not_created": True,
            "remote_upload_not_performed": True,
            "first_fit_decreasing_by_file_size_for_upload_candidates": True,
            "single_file_soft_target_exceptions_allowed_when_estimated_compressed_under_cap": True,
        },
        "summary": build_summary(filelist, rebalance_plan, chunks, upload_assignments, aliases, target, max_compressed, ratio),
        "deduped_chunk_rows": chunks,
        "deduped_upload_candidate_lane_rows": summarize_lanes(upload_assignments, "upload_candidate_file_rows"),
        "path_alias_lane_rows": summarize_lanes(aliases, "path_alias_rows"),
        "deduped_upload_candidate_extension_rows": summarize_extensions(upload_assignments, "upload_candidate_file_rows"),
        "path_alias_extension_rows": summarize_extensions(aliases, "path_alias_rows"),
        "deduped_upload_candidate_assignment_rows": upload_assignments,
        "path_alias_metadata_rows": aliases,
        "boundaries": {
            "local_metadata_plan_only": True,
            "file_content_not_copied": True,
            "source_text_not_copied": True,
            "source_language_terms_not_copied": True,
            "credentials_or_tokens_not_copied": True,
            "no_network_actions_performed": True,
            "remote_upload_or_push_not_performed": True,
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
        "# Selected Source-Witness Text/TeX Delta Deduped Upload-Candidate Plan - 2026-06-30",
        "",
        f"Status: `{document['status']}`",
        "",
        "This separates new-content delta rows from path-alias metadata rows already represented by content hash in the source-core snapshot. It is metadata-only and creates no archive or remote upload.",
        "",
        "## Summary",
        "",
        f"- Source filelist: {summary['source_filelist_rows']} rows / {summary['source_filelist_bytes']} bytes",
        f"- Upload candidates: {summary['deduped_upload_candidate_rows']} rows / {summary['deduped_upload_candidate_bytes']} bytes",
        f"- Path aliases retained as metadata: {summary['path_alias_metadata_rows']} rows / {summary['path_alias_metadata_bytes']} bytes",
        f"- Deduped chunks: {summary['deduped_chunks']}; chunks over estimated compressed cap: {summary['deduped_chunks_estimated_over_20mb']}",
        f"- Singleton soft-target exceptions: {summary['deduped_singleton_oversize_file_chunks']}",
        "- Archives created: 0; uploads/pushes/downloads: 0",
        "",
        "## Deduped Chunks",
        "",
        "| Chunk | Upload rows | Bytes | Est. compressed | Over soft target | Singleton exception |",
        "|---|---:|---:|---:|---|---|",
    ]
    for row in document["deduped_chunk_rows"]:
        lines.append(
            f"| {row['deduped_chunk_id']} | {row['upload_candidate_file_rows']} | {row['bytes']} | {row['estimated_compressed_bytes']} | {str(row['exceeds_soft_uncompressed_target']).lower()} | {str(row['singleton_oversize_file_chunk']).lower()} |"
        )
    lines.extend(
        [
            "",
            "## Upload-Candidate Extensions",
            "",
            "| Extension | Rows | Bytes |",
            "|---|---:|---:|",
        ]
    )
    for row in document["deduped_upload_candidate_extension_rows"]:
        lines.append(f"| {row['extension']} | {row['upload_candidate_file_rows']} | {row['bytes']} |")
    lines.extend(
        [
            "",
            "## Alias Metadata Extensions",
            "",
            "| Extension | Rows | Bytes |",
            "|---|---:|---:|",
        ]
    )
    for row in document["path_alias_extension_rows"]:
        lines.append(f"| {row['extension']} | {row['path_alias_rows']} | {row['bytes']} |")
    lines.extend(
        [
            "",
            "## Boundary Notes",
            "",
            "- Upload candidates are new-content hash rows only.",
            "- Path aliases are retained as metadata and point back to the delta filelist.",
            "- This plan creates no archive and performs no network action.",
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
        "- Selected source-witness text/TeX delta deduped upload-candidate plan: "
        f"{summary['deduped_upload_candidate_rows']} upload-candidate rows / "
        f"{summary['path_alias_metadata_rows']} path-alias rows / "
        f"{summary['deduped_chunks']} deduped chunks / "
        "0 archives or network actions"
    )
    if re.search(r"^- Selected source-witness text/TeX delta deduped upload-candidate plan: .*", text, flags=re.MULTILINE):
        text = re.sub(r"^- Selected source-witness text/TeX delta deduped upload-candidate plan: .*", line, text, flags=re.MULTILINE)
    else:
        marker = "- Selected source-witness text/TeX delta chunk rebalance plan:"
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
        "delta-staging/delta-filelist/chunk-rebalance metadata",
        "delta-staging/delta-filelist/chunk-rebalance/deduped-upload-candidate metadata",
    )
    text = text.replace("deduped-upload-candidate/deduped-upload-candidate metadata", "deduped-upload-candidate metadata")
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
    manifest["selected_source_witness_text_tex_delta_deduped_upload_candidate_plan"] = {
        "status": document["status"],
        "artifact_markdown": OUT_MD.name,
        "artifact_json": OUT_JSON.name,
        "source_filelist_rows": summary["source_filelist_rows"],
        "source_filelist_bytes": summary["source_filelist_bytes"],
        "source_rebalanced_chunks": summary["source_rebalanced_chunks"],
        "deduped_upload_candidate_rows": summary["deduped_upload_candidate_rows"],
        "deduped_upload_candidate_bytes": summary["deduped_upload_candidate_bytes"],
        "deduped_upload_candidate_tex_family_files": summary["deduped_upload_candidate_tex_family_files"],
        "path_alias_metadata_rows": summary["path_alias_metadata_rows"],
        "path_alias_metadata_bytes": summary["path_alias_metadata_bytes"],
        "path_alias_tex_family_files": summary["path_alias_tex_family_files"],
        "deduped_rows_plus_alias_rows": summary["deduped_rows_plus_alias_rows"],
        "deduped_bytes_plus_alias_bytes": summary["deduped_bytes_plus_alias_bytes"],
        "target_uncompressed_bytes_per_chunk": summary["target_uncompressed_bytes_per_chunk"],
        "max_planned_compressed_bytes": summary["max_planned_compressed_bytes"],
        "deduped_chunks": summary["deduped_chunks"],
        "deduped_chunks_over_soft_target": summary["deduped_chunks_over_soft_target"],
        "deduped_singleton_oversize_file_chunks": summary["deduped_singleton_oversize_file_chunks"],
        "deduped_individual_files_over_soft_target": summary["deduped_individual_files_over_soft_target"],
        "deduped_chunks_estimated_under_20mb": summary["deduped_chunks_estimated_under_20mb"],
        "deduped_chunks_estimated_over_20mb": summary["deduped_chunks_estimated_over_20mb"],
        "deduped_estimated_compressed_bytes_total": summary["deduped_estimated_compressed_bytes_total"],
        "deduped_max_chunk_bytes": summary["deduped_max_chunk_bytes"],
        "deduped_min_chunk_bytes": summary["deduped_min_chunk_bytes"],
        "actual_chunk_archives_created": 0,
        "actual_remote_uploads_performed": 0,
        "network_actions_performed": 0,
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
                "deduped_upload_candidate_plan_json": str(OUT_JSON),
                "deduped_upload_candidate_rows": document["summary"]["deduped_upload_candidate_rows"],
                "path_alias_metadata_rows": document["summary"]["path_alias_metadata_rows"],
                "deduped_chunks": document["summary"]["deduped_chunks"],
                "deduped_chunks_estimated_over_20mb": document["summary"]["deduped_chunks_estimated_over_20mb"],
                "no_network_actions_performed": document["no_network_actions_performed"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
