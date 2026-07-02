import datetime
import hashlib
import json
import pathlib
import re
from collections import Counter, defaultdict


BASE = pathlib.Path(__file__).resolve().parents[1]
CODEX_ROOT = pathlib.Path(r"C:\Users\memo_\Documents\Codex")
STATUS_MANIFEST = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_MANIFEST_20260629.json"
STATUS_INDEX = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_INDEX_20260629.md"
DELTA_STAGING_JSON = BASE / "SELECTED_SOURCE_WITNESS_TEXT_TEX_DELTA_STAGING_PLAN_20260630.json"
SOURCE_CORE_SNAPSHOT_JSON = BASE / "NOETHER_SOURCE_CORE_TEXT_TEX_WORKBOOKS_SNAPSHOT_20260629.json"
OUT_JSON = BASE / "SELECTED_SOURCE_WITNESS_TEXT_TEX_DELTA_FILELIST_20260630.json"
OUT_MD = BASE / "SELECTED_SOURCE_WITNESS_TEXT_TEX_DELTA_FILELIST_20260630.md"
SELF_PATH = pathlib.Path(__file__).resolve()

STATUS = "selected_source_witness_text_tex_delta_filelist_created_no_archive_no_network"

TEXT_SOURCE_EXTENSIONS = {
    ".bib",
    ".cls",
    ".csv",
    ".json",
    ".ltx",
    ".md",
    ".sty",
    ".tex",
    ".txt",
    ".xml",
    ".yaml",
    ".yml",
}
TEX_EXTENSIONS = {".tex", ".ltx", ".sty", ".cls", ".bib"}


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


def rel_to_codex(path: pathlib.Path) -> str:
    try:
        return path.resolve().relative_to(CODEX_ROOT.resolve()).as_posix()
    except ValueError:
        return path.resolve().as_posix()


def shelf_relative_path(shelf: pathlib.Path, path: pathlib.Path) -> str:
    try:
        return path.resolve().relative_to(shelf.resolve()).as_posix()
    except ValueError:
        return path.name


def source_core_indexes(snapshot: dict) -> tuple[set[str], set[str]]:
    paths = set()
    hashes = set()
    for item in snapshot.get("files", []):
        if item.get("codex_relative_path"):
            paths.add(item["codex_relative_path"])
        if item.get("sha256"):
            hashes.add(item["sha256"])
    return paths, hashes


def enumerate_text_source_files(shelf_path: pathlib.Path) -> list[pathlib.Path]:
    if not shelf_path.exists() or not shelf_path.is_dir():
        return []
    files = []
    for path in shelf_path.rglob("*"):
        if path.is_file() and path.suffix.lower() in TEXT_SOURCE_EXTENSIONS:
            files.append(path)
    return sorted(files, key=lambda path: shelf_relative_path(shelf_path, path).lower())


def build_file_rows(delta_staging: dict, snapshot: dict) -> tuple[list[dict], list[dict]]:
    source_core_paths, source_core_hashes = source_core_indexes(snapshot)
    file_rows = []
    shelf_rows = []
    file_id = 0
    for chunk in delta_staging.get("planned_chunks", []):
        for shelf in chunk.get("shelves", []):
            shelf_path = pathlib.Path(shelf["path"])
            all_text_files = enumerate_text_source_files(shelf_path)
            candidate_rows = []
            missing_path_files = []
            for path in all_text_files:
                codex_relative = rel_to_codex(path)
                if codex_relative not in source_core_paths:
                    missing_path_files.append(path)
            for path in missing_path_files:
                file_id += 1
                file_hash = sha256(path)
                stat = path.stat()
                codex_relative = rel_to_codex(path)
                content_hash_already_represented = file_hash in source_core_hashes
                row = {
                    "file_id": f"selected-witness-delta-file-{file_id:05d}",
                    "chunk_id": chunk["chunk_id"],
                    "batch": shelf.get("batch"),
                    "bucket": shelf.get("bucket"),
                    "lanes_or_cohorts": shelf.get("lanes_or_cohorts", []),
                    "source_gate_uses": shelf.get("source_gate_uses", []),
                    "shelf_path": str(shelf_path),
                    "shelf_relative_path": shelf_relative_path(shelf_path, path),
                    "codex_relative_path": codex_relative,
                    "extension": path.suffix.lower() or "[none]",
                    "bytes": stat.st_size,
                    "sha256": file_hash,
                    "is_tex_family": path.suffix.lower() in TEX_EXTENSIONS,
                    "represented_in_source_core_by_path": False,
                    "content_hash_already_represented_in_source_core": content_hash_already_represented,
                    "delta_candidate_reason": (
                        "path_not_in_source_core_but_content_hash_already_represented"
                        if content_hash_already_represented
                        else "path_and_content_not_in_source_core"
                    ),
                    "source_text_copied": False,
                    "source_language_terms_copied": False,
                    "file_content_copied": False,
                }
                candidate_rows.append(row)
                file_rows.append(row)
            represented_by_path = len(all_text_files) - len(missing_path_files)
            shelf_rows.append(
                {
                    "chunk_id": chunk["chunk_id"],
                    "shelf_path": str(shelf_path),
                    "batch": shelf.get("batch"),
                    "bucket": shelf.get("bucket"),
                    "lanes_or_cohorts": shelf.get("lanes_or_cohorts", []),
                    "source_gate_uses": shelf.get("source_gate_uses", []),
                    "planned_text_source_like_gap_files": shelf.get("text_source_like_gap_files", 0),
                    "actual_text_source_like_files_on_disk": len(all_text_files),
                    "represented_in_source_core_by_path": represented_by_path,
                    "delta_file_rows": len(candidate_rows),
                    "delta_tex_family_files": sum(1 for row in candidate_rows if row["is_tex_family"]),
                    "delta_bytes": sum(row["bytes"] for row in candidate_rows),
                    "content_hash_already_represented_rows": sum(
                        1 for row in candidate_rows if row["content_hash_already_represented_in_source_core"]
                    ),
                    "filelist_reconciliation_status": (
                        "matches_planned_gap"
                        if len(candidate_rows) == int(shelf.get("text_source_like_gap_files") or 0)
                        else "differs_from_staging_estimate"
                    ),
                    "actual_delta_archive_created": False,
                    "actual_remote_upload_performed": False,
                    "source_text_copied": False,
                    "source_language_terms_copied": False,
                }
            )
    return file_rows, shelf_rows


def summarize_by_extension(file_rows: list[dict]) -> list[dict]:
    counts: dict[str, dict] = {}
    for row in file_rows:
        ext = row["extension"]
        if ext not in counts:
            counts[ext] = {"extension": ext, "files": 0, "bytes": 0}
        counts[ext]["files"] += 1
        counts[ext]["bytes"] += row["bytes"]
    return [counts[key] for key in sorted(counts)]


def summarize_by_lane(file_rows: list[dict]) -> list[dict]:
    lanes: dict[str, dict] = defaultdict(lambda: {"file_rows": 0, "bytes": 0, "tex_family_files": 0})
    for row in file_rows:
        for lane in row.get("lanes_or_cohorts", []):
            lanes[lane]["file_rows"] += 1
            lanes[lane]["bytes"] += row["bytes"]
            if row["is_tex_family"]:
                lanes[lane]["tex_family_files"] += 1
    return [
        {"lane_or_cohort": lane, **values}
        for lane, values in sorted(lanes.items())
    ]


def summarize_chunks(file_rows: list[dict], shelf_rows: list[dict], delta_staging: dict) -> list[dict]:
    by_chunk_files: dict[str, list[dict]] = defaultdict(list)
    by_chunk_shelves: dict[str, list[dict]] = defaultdict(list)
    for row in file_rows:
        by_chunk_files[row["chunk_id"]].append(row)
    for row in shelf_rows:
        by_chunk_shelves[row["chunk_id"]].append(row)
    planned_by_chunk = {chunk["chunk_id"]: chunk for chunk in delta_staging.get("planned_chunks", [])}
    output = []
    for chunk_id in sorted(planned_by_chunk):
        rows = by_chunk_files.get(chunk_id, [])
        shelves = by_chunk_shelves.get(chunk_id, [])
        planned = planned_by_chunk[chunk_id]
        output.append(
            {
                "chunk_id": chunk_id,
                "file_rows": len(rows),
                "shelf_rows": len(shelves),
                "bytes": sum(row["bytes"] for row in rows),
                "tex_family_files": sum(1 for row in rows if row["is_tex_family"]),
                "content_hash_already_represented_rows": sum(
                    1 for row in rows if row["content_hash_already_represented_in_source_core"]
                ),
                "planned_text_source_like_gap_files": planned.get("text_source_like_gap_files", 0),
                "planned_estimated_uncompressed_bytes": planned.get("estimated_uncompressed_bytes", 0),
                "planned_estimated_compressed_bytes": planned.get("estimated_compressed_bytes", 0),
                "estimated_compressed_under_20mb": planned.get("estimated_compressed_under_20mb", False),
                "actual_file_list_created": True,
                "actual_delta_archive_created": False,
                "actual_remote_upload_performed": False,
                "source_text_copied": False,
                "source_language_terms_copied": False,
            }
        )
    return output


def build_summary(file_rows: list[dict], shelf_rows: list[dict], chunk_rows: list[dict], delta_staging: dict) -> dict:
    planned = delta_staging.get("summary", {})
    duplicate_content_rows = sum(1 for row in file_rows if row["content_hash_already_represented_in_source_core"])
    return {
        "source_core_delta_filelist_created": True,
        "planned_delta_shelves": planned.get("planned_delta_shelves", 0),
        "filelist_shelf_rows": len(shelf_rows),
        "shelf_rows_matching_staging_gap": sum(
            1 for row in shelf_rows if row["filelist_reconciliation_status"] == "matches_planned_gap"
        ),
        "shelf_rows_differing_from_staging_gap": sum(
            1 for row in shelf_rows if row["filelist_reconciliation_status"] == "differs_from_staging_estimate"
        ),
        "planned_text_source_like_gap_files": planned.get("planned_text_source_like_gap_files", 0),
        "delta_file_rows": len(file_rows),
        "delta_file_rows_with_new_content_hashes": len(file_rows) - duplicate_content_rows,
        "delta_file_rows_with_existing_content_hashes": duplicate_content_rows,
        "delta_tex_family_files": sum(1 for row in file_rows if row["is_tex_family"]),
        "delta_bytes": sum(row["bytes"] for row in file_rows),
        "planned_delta_chunks": planned.get("planned_chunks", 0),
        "filelist_chunks": len(chunk_rows),
        "chunks_estimated_under_20mb": sum(1 for row in chunk_rows if row["estimated_compressed_under_20mb"]),
        "chunks_estimated_over_20mb": sum(1 for row in chunk_rows if not row["estimated_compressed_under_20mb"]),
        "actual_delta_archive_created": False,
        "actual_remote_upload_performed": False,
        "pdf_files_included": 0,
        "image_files_included": 0,
        "archive_files_included": 0,
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
    delta_staging = load_json(DELTA_STAGING_JSON)
    source_core_snapshot = load_json(SOURCE_CORE_SNAPSHOT_JSON)
    file_rows, shelf_rows = build_file_rows(delta_staging, source_core_snapshot)
    chunk_rows = summarize_chunks(file_rows, shelf_rows, delta_staging)
    return {
        "artifact": "selected_source_witness_text_tex_delta_filelist",
        "generated_utc": now_utc(),
        "generated_date": "20260630",
        "status": STATUS,
        "bandwidth_mode": "local_only_no_network_actions",
        "inputs": {
            "status_manifest": STATUS_MANIFEST.name,
            "delta_staging_plan": DELTA_STAGING_JSON.name,
            "source_core_snapshot": SOURCE_CORE_SNAPSHOT_JSON.name,
        },
        "filelist_policy": {
            "metadata_only_no_file_content": True,
            "source_text_or_passages_not_copied": True,
            "source_language_terms_not_copied": True,
            "text_source_like_extensions_only": sorted(TEXT_SOURCE_EXTENSIONS),
            "pdf_image_archive_payloads_excluded": True,
            "delta_archive_not_created": True,
            "remote_upload_not_performed": True,
            "compare_by_codex_relative_path_against_prior_source_core_snapshot": True,
            "content_hash_duplicate_rows_are_marked_not_removed": True,
        },
        "summary": build_summary(file_rows, shelf_rows, chunk_rows, delta_staging),
        "chunk_rows": chunk_rows,
        "shelf_rows": shelf_rows,
        "lane_rows": summarize_by_lane(file_rows),
        "extension_rows": summarize_by_extension(file_rows),
        "file_rows": file_rows,
        "boundaries": {
            "local_metadata_inventory_only": True,
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
        "# Selected Source-Witness Text/TeX Delta Filelist - 2026-06-30",
        "",
        f"Status: `{document['status']}`",
        "",
        "This is a metadata-only checksum inventory for the selected-witness text/TeX delta. It lists paths, sizes, hashes, chunk assignment, and source-core representation status. It does not copy file contents, source passages, source-language terms, PDFs, images, archives, credentials, or remote payloads.",
        "",
        "## Summary",
        "",
        f"- Planned shelves: {summary['planned_delta_shelves']}; filelist shelves: {summary['filelist_shelf_rows']}",
        f"- Planned text/source-like gap files: {summary['planned_text_source_like_gap_files']}; file rows found: {summary['delta_file_rows']}",
        f"- New-content hash rows: {summary['delta_file_rows_with_new_content_hashes']}; already-represented content-hash rows: {summary['delta_file_rows_with_existing_content_hashes']}",
        f"- TeX-family rows: {summary['delta_tex_family_files']}; metadata bytes represented by file rows: {summary['delta_bytes']}",
        f"- Chunks: {summary['filelist_chunks']} listed / {summary['chunks_estimated_under_20mb']} estimated under 20 MB compressed",
        "- Archives created: 0; uploads/pushes/downloads: 0",
        "",
        "## Chunks",
        "",
        "| Chunk | Files | Shelves | Bytes | TeX-family | Planned gap files | Archive/upload |",
        "|---|---:|---:|---:|---:|---:|---|",
    ]
    for row in document["chunk_rows"]:
        lines.append(
            f"| {row['chunk_id']} | {row['file_rows']} | {row['shelf_rows']} | {row['bytes']} | {row['tex_family_files']} | {row['planned_text_source_like_gap_files']} | not created / not uploaded |"
        )
    lines.extend(
        [
            "",
            "## Lanes",
            "",
            "| Lane/cohort | Files | Bytes | TeX-family |",
            "|---|---:|---:|---:|",
        ]
    )
    for row in document["lane_rows"]:
        lines.append(
            f"| {row['lane_or_cohort']} | {row['file_rows']} | {row['bytes']} | {row['tex_family_files']} |"
        )
    lines.extend(
        [
            "",
            "## Extensions",
            "",
            "| Extension | Files | Bytes |",
            "|---|---:|---:|",
        ]
    )
    for row in document["extension_rows"]:
        lines.append(f"| {row['extension']} | {row['files']} | {row['bytes']} |")
    lines.extend(
        [
            "",
            "## Boundary Notes",
            "",
            "- File rows are metadata and checksums only; no source file contents are included.",
            "- Rows whose content hash is already represented in the prior source-core snapshot are marked rather than silently dropped.",
            "- The previous staging plan remains a planning artifact; this file is the current checksum inventory and still creates no archive.",
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
        "- Selected source-witness text/TeX delta filelist: "
        f"{summary['delta_file_rows']} file rows / "
        f"{summary['filelist_shelf_rows']} shelves / "
        f"{summary['filelist_chunks']} planned chunks / "
        "0 archives or network actions"
    )
    if re.search(r"^- Selected source-witness text/TeX delta filelist: .*", text, flags=re.MULTILINE):
        text = re.sub(r"^- Selected source-witness text/TeX delta filelist: .*", line, text, flags=re.MULTILINE)
    else:
        marker = "- Selected source-witness text/TeX delta staging plan:"
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
        "filesystem-validation/source-core-gap/delta-staging metadata",
        "filesystem-validation/source-core-gap/delta-staging/delta-filelist metadata",
    )
    text = text.replace("delta-filelist/delta-filelist metadata", "delta-filelist metadata")
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
    manifest["selected_source_witness_text_tex_delta_filelist"] = {
        "status": document["status"],
        "artifact_markdown": OUT_MD.name,
        "artifact_json": OUT_JSON.name,
        "source_core_delta_filelist_created": True,
        "planned_delta_shelves": summary["planned_delta_shelves"],
        "filelist_shelf_rows": summary["filelist_shelf_rows"],
        "shelf_rows_matching_staging_gap": summary["shelf_rows_matching_staging_gap"],
        "shelf_rows_differing_from_staging_gap": summary["shelf_rows_differing_from_staging_gap"],
        "planned_text_source_like_gap_files": summary["planned_text_source_like_gap_files"],
        "delta_file_rows": summary["delta_file_rows"],
        "delta_file_rows_with_new_content_hashes": summary["delta_file_rows_with_new_content_hashes"],
        "delta_file_rows_with_existing_content_hashes": summary["delta_file_rows_with_existing_content_hashes"],
        "delta_tex_family_files": summary["delta_tex_family_files"],
        "delta_bytes": summary["delta_bytes"],
        "planned_delta_chunks": summary["planned_delta_chunks"],
        "filelist_chunks": summary["filelist_chunks"],
        "chunks_estimated_under_20mb": summary["chunks_estimated_under_20mb"],
        "chunks_estimated_over_20mb": summary["chunks_estimated_over_20mb"],
        "actual_delta_archive_created": False,
        "actual_remote_upload_performed": False,
        "pdf_files_included": 0,
        "image_files_included": 0,
        "archive_files_included": 0,
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
                "delta_filelist_json": str(OUT_JSON),
                "planned_text_source_like_gap_files": document["summary"]["planned_text_source_like_gap_files"],
                "delta_file_rows": document["summary"]["delta_file_rows"],
                "delta_tex_family_files": document["summary"]["delta_tex_family_files"],
                "filelist_chunks": document["summary"]["filelist_chunks"],
                "actual_delta_archive_created": document["summary"]["actual_delta_archive_created"],
                "no_network_actions_performed": document["no_network_actions_performed"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
