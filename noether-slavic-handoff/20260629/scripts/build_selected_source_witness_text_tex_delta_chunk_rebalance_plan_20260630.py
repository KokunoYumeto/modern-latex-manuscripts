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
SPLIT_PLAN_JSON = BASE / "SOURCE_CORE_SPLIT_UPLOAD_STAGING_PLAN_20260630.json"
OUT_JSON = BASE / "SELECTED_SOURCE_WITNESS_TEXT_TEX_DELTA_CHUNK_REBALANCE_PLAN_20260630.json"
OUT_MD = BASE / "SELECTED_SOURCE_WITNESS_TEXT_TEX_DELTA_CHUNK_REBALANCE_PLAN_20260630.md"
SELF_PATH = pathlib.Path(__file__).resolve()

STATUS = "selected_source_witness_text_tex_delta_chunk_rebalance_plan_no_archive_no_network"


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


def compact_assignment(row: dict, rebalance_chunk_id: str) -> dict:
    return {
        "file_id": row["file_id"],
        "rebalance_chunk_id": rebalance_chunk_id,
        "source_filelist_chunk_id": row["chunk_id"],
        "bytes": row["bytes"],
        "extension": row["extension"],
        "is_tex_family": row["is_tex_family"],
        "lanes_or_cohorts": row.get("lanes_or_cohorts", []),
        "content_hash_already_represented_in_source_core": row.get("content_hash_already_represented_in_source_core", False),
        "source_text_copied": False,
        "source_language_terms_copied": False,
        "file_content_copied": False,
    }


def rebalance(file_rows: list[dict], target_uncompressed: int, ratio: float, max_compressed: int) -> tuple[list[dict], list[dict]]:
    sorted_rows = sorted(file_rows, key=lambda row: (-int(row["bytes"]), row["file_id"]))
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
    assignment_rows = []
    for index, chunk in enumerate(chunk_work, start=1):
        chunk_id = f"selected-witness-text-tex-delta-rebalanced-{index:02d}"
        rows = sorted(chunk["rows"], key=lambda row: row["file_id"])
        estimated_compressed = estimate_compressed(chunk["bytes"], ratio)
        extension_counts = Counter(row["extension"] for row in rows)
        lanes = sorted({lane for row in rows for lane in row.get("lanes_or_cohorts", [])})
        source_chunks = sorted({row["chunk_id"] for row in rows})
        chunk_rows.append(
            {
                "rebalance_chunk_id": chunk_id,
                "file_rows": len(rows),
                "bytes": chunk["bytes"],
                "estimated_compressed_bytes": estimated_compressed,
                "estimated_compressed_under_20mb": estimated_compressed <= max_compressed,
                "target_uncompressed_bytes_per_chunk": target_uncompressed,
                "exceeds_soft_uncompressed_target": chunk["bytes"] > target_uncompressed,
                "singleton_oversize_file_chunk": bool(chunk.get("singleton_oversize_file")),
                "source_filelist_chunk_ids": source_chunks,
                "lane_or_cohort_count": len(lanes),
                "lanes_or_cohorts": lanes,
                "tex_family_files": sum(1 for row in rows if row.get("is_tex_family")),
                "content_hash_already_represented_rows": sum(
                    1 for row in rows if row.get("content_hash_already_represented_in_source_core")
                ),
                "extension_counts": dict(sorted(extension_counts.items())),
                "actual_chunk_archive_created": False,
                "actual_remote_upload_performed": False,
                "source_text_copied": False,
                "source_language_terms_copied": False,
            }
        )
        for row in rows:
            assignment_rows.append(compact_assignment(row, chunk_id))
    return chunk_rows, sorted(assignment_rows, key=lambda row: row["file_id"])


def summarize_lanes(assignments: list[dict]) -> list[dict]:
    lanes: dict[str, dict] = defaultdict(lambda: {"file_rows": 0, "bytes": 0, "tex_family_files": 0, "rebalance_chunks": set()})
    for row in assignments:
        for lane in row.get("lanes_or_cohorts", []):
            lanes[lane]["file_rows"] += 1
            lanes[lane]["bytes"] += row["bytes"]
            lanes[lane]["tex_family_files"] += 1 if row["is_tex_family"] else 0
            lanes[lane]["rebalance_chunks"].add(row["rebalance_chunk_id"])
    return [
        {
            "lane_or_cohort": lane,
            "file_rows": values["file_rows"],
            "bytes": values["bytes"],
            "tex_family_files": values["tex_family_files"],
            "rebalance_chunks": len(values["rebalance_chunks"]),
        }
        for lane, values in sorted(lanes.items())
    ]


def summarize_extensions(assignments: list[dict]) -> list[dict]:
    values: dict[str, dict] = defaultdict(lambda: {"file_rows": 0, "bytes": 0})
    for row in assignments:
        values[row["extension"]]["file_rows"] += 1
        values[row["extension"]]["bytes"] += row["bytes"]
    return [{"extension": ext, **data} for ext, data in sorted(values.items())]


def build_summary(filelist: dict, chunk_rows: list[dict], assignments: list[dict], target_uncompressed: int, ratio: float, max_compressed: int) -> dict:
    filelist_summary = filelist.get("summary", {})
    old_chunks = filelist.get("chunk_rows", [])
    old_chunk_bytes = [int(row.get("bytes") or 0) for row in old_chunks]
    new_chunk_bytes = [int(row.get("bytes") or 0) for row in chunk_rows]
    return {
        "source_filelist_rows": filelist_summary.get("delta_file_rows", 0),
        "source_filelist_bytes": filelist_summary.get("delta_bytes", 0),
        "source_filelist_chunks": filelist_summary.get("filelist_chunks", 0),
        "source_filelist_max_chunk_bytes": max(old_chunk_bytes) if old_chunk_bytes else 0,
        "source_filelist_chunks_over_soft_target": sum(1 for value in old_chunk_bytes if value > target_uncompressed),
        "target_uncompressed_bytes_per_chunk": target_uncompressed,
        "max_planned_compressed_bytes": max_compressed,
        "compression_ratio_estimate_from_existing_archive": ratio,
        "rebalanced_chunks": len(chunk_rows),
        "rebalanced_file_rows": len(assignments),
        "rebalanced_bytes": sum(row["bytes"] for row in assignments),
        "rebalanced_max_chunk_bytes": max(new_chunk_bytes) if new_chunk_bytes else 0,
        "rebalanced_min_chunk_bytes": min(new_chunk_bytes) if new_chunk_bytes else 0,
        "rebalanced_chunks_over_soft_target": sum(1 for row in chunk_rows if row["exceeds_soft_uncompressed_target"]),
        "singleton_oversize_file_chunks": sum(1 for row in chunk_rows if row["singleton_oversize_file_chunk"]),
        "individual_files_over_soft_target": sum(1 for row in assignments if row["bytes"] > target_uncompressed),
        "rebalanced_chunks_estimated_under_20mb": sum(1 for row in chunk_rows if row["estimated_compressed_under_20mb"]),
        "rebalanced_chunks_estimated_over_20mb": sum(1 for row in chunk_rows if not row["estimated_compressed_under_20mb"]),
        "rebalanced_estimated_compressed_bytes_total": sum(row["estimated_compressed_bytes"] for row in chunk_rows),
        "rebalanced_tex_family_files": sum(1 for row in assignments if row["is_tex_family"]),
        "content_hash_already_represented_rows": sum(
            1 for row in assignments if row["content_hash_already_represented_in_source_core"]
        ),
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
    split_plan = load_json(SPLIT_PLAN_JSON)
    policy = split_plan.get("chunking_policy", {})
    target_uncompressed = int(policy.get("target_uncompressed_bytes_per_chunk") or 40 * 1024 * 1024)
    max_compressed = int(policy.get("max_planned_compressed_bytes") or 20 * 1024 * 1024)
    ratio = float(policy.get("compression_ratio_estimate_from_existing_archive") or 0.253)
    chunk_rows, assignments = rebalance(filelist.get("file_rows", []), target_uncompressed, ratio, max_compressed)
    return {
        "artifact": "selected_source_witness_text_tex_delta_chunk_rebalance_plan",
        "generated_utc": now_utc(),
        "generated_date": "20260630",
        "status": STATUS,
        "bandwidth_mode": "local_only_no_network_actions",
        "inputs": {
            "status_manifest": STATUS_MANIFEST.name,
            "delta_filelist": DELTA_FILELIST_JSON.name,
            "source_core_split_plan": SPLIT_PLAN_JSON.name,
        },
        "rebalance_policy": {
            "metadata_only_no_file_content": True,
            "source_text_or_passages_not_copied": True,
            "source_language_terms_not_copied": True,
            "pdf_image_archive_payloads_excluded": True,
            "actual_archives_not_created": True,
            "remote_upload_not_performed": True,
            "first_fit_decreasing_by_file_size": True,
            "soft_target_uncompressed_bytes_per_chunk": target_uncompressed,
            "hard_estimated_compressed_bytes_cap": max_compressed,
            "single_file_soft_target_exceptions_allowed_when_estimated_compressed_under_cap": True,
        },
        "summary": build_summary(filelist, chunk_rows, assignments, target_uncompressed, ratio, max_compressed),
        "rebalance_chunk_rows": chunk_rows,
        "rebalance_lane_rows": summarize_lanes(assignments),
        "rebalance_extension_rows": summarize_extensions(assignments),
        "rebalance_assignment_rows": assignments,
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
        "# Selected Source-Witness Text/TeX Delta Chunk Rebalance Plan - 2026-06-30",
        "",
        f"Status: `{document['status']}`",
        "",
        "This rebalances the concrete delta filelist into upload-sized metadata chunks. It references file IDs from the delta filelist and does not copy file contents, source passages, source-language terms, PDFs, images, archives, credentials, or remote payloads.",
        "",
        "## Summary",
        "",
        f"- Source filelist: {summary['source_filelist_rows']} rows / {summary['source_filelist_bytes']} bytes / {summary['source_filelist_chunks']} old chunks",
        f"- Old max chunk bytes: {summary['source_filelist_max_chunk_bytes']}; old chunks over soft target: {summary['source_filelist_chunks_over_soft_target']}",
        f"- Rebalanced chunks: {summary['rebalanced_chunks']}; max bytes: {summary['rebalanced_max_chunk_bytes']}; min bytes: {summary['rebalanced_min_chunk_bytes']}",
        f"- Soft-target exceptions: {summary['singleton_oversize_file_chunks']} singleton chunks for {summary['individual_files_over_soft_target']} individual oversized files",
        f"- Estimated compressed chunks over 20 MB: {summary['rebalanced_chunks_estimated_over_20mb']}",
        "- Archives created: 0; uploads/pushes/downloads: 0",
        "",
        "## Rebalanced Chunks",
        "",
        "| Chunk | Files | Bytes | Est. compressed | Over soft target | Singleton exception | Source chunks |",
        "|---|---:|---:|---:|---|---|---|",
    ]
    for row in document["rebalance_chunk_rows"]:
        lines.append(
            "| {chunk} | {files} | {bytes} | {compressed} | {over} | {singleton} | {source_chunks} |".format(
                chunk=row["rebalance_chunk_id"],
                files=row["file_rows"],
                bytes=row["bytes"],
                compressed=row["estimated_compressed_bytes"],
                over=str(row["exceeds_soft_uncompressed_target"]).lower(),
                singleton=str(row["singleton_oversize_file_chunk"]).lower(),
                source_chunks=", ".join(row["source_filelist_chunk_ids"]),
            )
        )
    lines.extend(
        [
            "",
            "## Lane Coverage",
            "",
            "| Lane/cohort | Files | Bytes | Rebalanced chunks |",
            "|---|---:|---:|---:|",
        ]
    )
    for row in document["rebalance_lane_rows"]:
        lines.append(
            f"| {row['lane_or_cohort']} | {row['file_rows']} | {row['bytes']} | {row['rebalance_chunks']} |"
        )
    lines.extend(
        [
            "",
            "## Boundary Notes",
            "",
            "- This is a rebalanced plan only; it creates no archive and performs no upload.",
            "- Three individual files exceed the soft uncompressed target, so they are isolated as singleton chunks.",
            "- Every chunk remains under the existing estimated compressed-size cap.",
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
        "- Selected source-witness text/TeX delta chunk rebalance plan: "
        f"{summary['rebalanced_chunks']} chunks / "
        f"{summary['rebalanced_file_rows']} file assignments / "
        f"{summary['rebalanced_chunks_estimated_over_20mb']} chunks over estimated cap / "
        "0 archives or network actions"
    )
    if re.search(r"^- Selected source-witness text/TeX delta chunk rebalance plan: .*", text, flags=re.MULTILINE):
        text = re.sub(r"^- Selected source-witness text/TeX delta chunk rebalance plan: .*", line, text, flags=re.MULTILINE)
    else:
        marker = "- Selected source-witness text/TeX delta filelist:"
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
        "delta-staging/delta-filelist metadata",
        "delta-staging/delta-filelist/chunk-rebalance metadata",
    )
    text = text.replace("chunk-rebalance/chunk-rebalance metadata", "chunk-rebalance metadata")
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
    manifest["selected_source_witness_text_tex_delta_chunk_rebalance_plan"] = {
        "status": document["status"],
        "artifact_markdown": OUT_MD.name,
        "artifact_json": OUT_JSON.name,
        "source_filelist_rows": summary["source_filelist_rows"],
        "source_filelist_bytes": summary["source_filelist_bytes"],
        "source_filelist_chunks": summary["source_filelist_chunks"],
        "source_filelist_max_chunk_bytes": summary["source_filelist_max_chunk_bytes"],
        "source_filelist_chunks_over_soft_target": summary["source_filelist_chunks_over_soft_target"],
        "target_uncompressed_bytes_per_chunk": summary["target_uncompressed_bytes_per_chunk"],
        "max_planned_compressed_bytes": summary["max_planned_compressed_bytes"],
        "rebalanced_chunks": summary["rebalanced_chunks"],
        "rebalanced_file_rows": summary["rebalanced_file_rows"],
        "rebalanced_bytes": summary["rebalanced_bytes"],
        "rebalanced_max_chunk_bytes": summary["rebalanced_max_chunk_bytes"],
        "rebalanced_min_chunk_bytes": summary["rebalanced_min_chunk_bytes"],
        "rebalanced_chunks_over_soft_target": summary["rebalanced_chunks_over_soft_target"],
        "singleton_oversize_file_chunks": summary["singleton_oversize_file_chunks"],
        "individual_files_over_soft_target": summary["individual_files_over_soft_target"],
        "rebalanced_chunks_estimated_under_20mb": summary["rebalanced_chunks_estimated_under_20mb"],
        "rebalanced_chunks_estimated_over_20mb": summary["rebalanced_chunks_estimated_over_20mb"],
        "rebalanced_estimated_compressed_bytes_total": summary["rebalanced_estimated_compressed_bytes_total"],
        "rebalanced_tex_family_files": summary["rebalanced_tex_family_files"],
        "content_hash_already_represented_rows": summary["content_hash_already_represented_rows"],
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
                "chunk_rebalance_plan_json": str(OUT_JSON),
                "rebalanced_chunks": document["summary"]["rebalanced_chunks"],
                "rebalanced_file_rows": document["summary"]["rebalanced_file_rows"],
                "source_filelist_max_chunk_bytes": document["summary"]["source_filelist_max_chunk_bytes"],
                "rebalanced_max_chunk_bytes": document["summary"]["rebalanced_max_chunk_bytes"],
                "rebalanced_chunks_estimated_over_20mb": document["summary"]["rebalanced_chunks_estimated_over_20mb"],
                "no_network_actions_performed": document["no_network_actions_performed"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
