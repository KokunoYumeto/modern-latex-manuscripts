import datetime
import hashlib
import json
import pathlib
import re
from collections import defaultdict


BASE = pathlib.Path(__file__).resolve().parents[1]
STATUS_MANIFEST = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_MANIFEST_20260629.json"
STATUS_INDEX = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_INDEX_20260629.md"
SNAPSHOT_JSON = BASE / "NOETHER_SOURCE_CORE_TEXT_TEX_WORKBOOKS_SNAPSHOT_20260629.json"
OUT_JSON = BASE / "SOURCE_CORE_SPLIT_UPLOAD_STAGING_PLAN_20260630.json"
OUT_MD = BASE / "SOURCE_CORE_SPLIT_UPLOAD_STAGING_PLAN_20260630.md"

TARGET_UNCOMPRESSED_BYTES = 40 * 1024 * 1024
MAX_PLANNED_COMPRESSED_BYTES = 20 * 1024 * 1024


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


def archive_ratio(snapshot: dict) -> float:
    archive_bytes = snapshot["archive"]["bytes"]
    uncompressed = snapshot["included_bytes_uncompressed"]
    if not archive_bytes or not uncompressed:
        return 1.0
    return archive_bytes / uncompressed


def root_slug(root_label: str) -> str:
    return root_label.replace("_", "-")


def root_chunks(snapshot: dict) -> list[dict]:
    ratio = archive_ratio(snapshot)
    files_by_root: dict[str, list[dict]] = defaultdict(list)
    for item in snapshot["files"]:
        files_by_root[item["root_label"]].append(item)

    chunks: list[dict] = []
    global_index = 1
    for root in sorted(files_by_root):
        root_files = sorted(files_by_root[root], key=lambda row: row["archive_path"])
        root_part = 1
        current: list[dict] = []
        current_bytes = 0
        for item in root_files:
            item_bytes = item["bytes"]
            if current and current_bytes + item_bytes > TARGET_UNCOMPRESSED_BYTES:
                chunks.append(build_chunk(global_index, root, root_part, current, current_bytes, ratio))
                global_index += 1
                root_part += 1
                current = []
                current_bytes = 0
            current.append(item)
            current_bytes += item_bytes
        if current:
            chunks.append(build_chunk(global_index, root, root_part, current, current_bytes, ratio))
            global_index += 1
    return chunks


def build_chunk(global_index: int, root: str, root_part: int, files: list[dict], bytes_total: int, ratio: float) -> dict:
    estimated_compressed = int(bytes_total * ratio) + 4096
    chunk_id = f"source-core-{global_index:02d}-{root_slug(root)}-{root_part:02d}"
    planned_archive = f"NOETHER_SOURCE_CORE_TEXT_TEX_WORKBOOKS_SNAPSHOT_20260629_{chunk_id}.zip"
    return {
        "chunk_id": chunk_id,
        "root_label": root,
        "root_part": root_part,
        "planned_archive_name": planned_archive,
        "planned_archive_path": f"noether-slavic-handoff/20260629/source-core-staged/{planned_archive}",
        "file_count": len(files),
        "uncompressed_bytes": bytes_total,
        "estimated_compressed_bytes": estimated_compressed,
        "estimated_compressed_under_20mb": estimated_compressed <= MAX_PLANNED_COMPRESSED_BYTES,
        "source_text_copied": False,
        "source_language_terms_copied": False,
        "files": [
            {
                "archive_path": item["archive_path"],
                "root_label": item["root_label"],
                "codex_relative_path": item["codex_relative_path"],
                "sha256": item["sha256"],
                "bytes": item["bytes"],
                "extension": item["extension"],
            }
            for item in files
        ],
    }


def extension_summary(chunks: list[dict]) -> list[dict]:
    counts: dict[str, dict[str, int]] = defaultdict(lambda: {"count": 0, "bytes": 0})
    for chunk in chunks:
        for item in chunk["files"]:
            ext = item["extension"]
            counts[ext]["count"] += 1
            counts[ext]["bytes"] += item["bytes"]
    return [{"extension": key, **counts[key]} for key in sorted(counts)]


def root_summary(chunks: list[dict]) -> list[dict]:
    counts: dict[str, dict[str, int]] = defaultdict(lambda: {"chunks": 0, "files": 0, "bytes": 0})
    for chunk in chunks:
        root = chunk["root_label"]
        counts[root]["chunks"] += 1
        counts[root]["files"] += chunk["file_count"]
        counts[root]["bytes"] += chunk["uncompressed_bytes"]
    return [{"root_label": key, **counts[key]} for key in sorted(counts)]


def build_document(snapshot: dict) -> dict:
    chunks = root_chunks(snapshot)
    oversized_estimates = [chunk["chunk_id"] for chunk in chunks if not chunk["estimated_compressed_under_20mb"]]
    return {
        "artifact": "source_core_split_upload_staging_plan",
        "status": "split_upload_plan_built_locally_no_chunks_uploaded_not_completion_claim",
        "generated_date": "2026-06-30",
        "generated_utc": now_utc(),
        "bandwidth_mode": "local_only_no_network_actions",
        "no_network_actions_performed": True,
        "basis_snapshot_json": SNAPSHOT_JSON.name,
        "basis_snapshot_archive": snapshot["archive"],
        "source_text_copied": False,
        "source_language_terms_copied": False,
        "credentials_or_tokens_copied": False,
        "chunking_policy": {
            "target_uncompressed_bytes_per_chunk": TARGET_UNCOMPRESSED_BYTES,
            "max_planned_compressed_bytes": MAX_PLANNED_COMPRESSED_BYTES,
            "compression_ratio_estimate_from_existing_archive": archive_ratio(snapshot),
            "root_aware_chunking": True,
            "actual_chunk_archives_created": False,
            "remote_upload_attempted": False,
        },
        "totals": {
            "source_core_files_assigned": sum(chunk["file_count"] for chunk in chunks),
            "source_core_uncompressed_bytes_assigned": sum(chunk["uncompressed_bytes"] for chunk in chunks),
            "planned_chunks": len(chunks),
            "planned_chunks_estimated_under_20mb": sum(
                1 for chunk in chunks if chunk["estimated_compressed_under_20mb"]
            ),
            "planned_chunks_estimated_over_20mb": len(oversized_estimates),
            "uploaded_chunks": 0,
            "uploaded_bytes": 0,
        },
        "root_summary": root_summary(chunks),
        "extension_summary": extension_summary(chunks),
        "planned_upload_order": [
            {
                "step": 1,
                "action": "push_manifest_json_markdown_scripts_first",
                "network_status": "deferred_until_user_approval_or_suitable_network",
            },
            {
                "step": 2,
                "action": "build_planned_chunk_archives_from_snapshot_manifest",
                "network_status": "local_build_only_before_any_remote_upload",
            },
            {
                "step": 3,
                "action": "upload_or_release_source_core_chunks_if_approved",
                "network_status": "deferred_until_user_approval_or_suitable_network",
            },
            {
                "step": 4,
                "action": "update_draft_pr_pointer_after_remote_verification",
                "network_status": "deferred_until_user_approval_or_suitable_network",
            },
        ],
        "chunks": chunks,
        "boundaries": [
            "This is a staging plan only; it creates no source-core split archives.",
            "This performs no fetch, push, clone, download, upload, or GitHub API call.",
            "This assigns files from the existing source-core snapshot by path, size, and hash only.",
            "This does not copy source-language passages or native-register extraction text.",
            "This is not a review result and not a completion claim.",
        ],
    }


def write_markdown(document: dict) -> None:
    totals = document["totals"]
    lines = [
        "# Source-core split upload staging plan - 2026-06-30",
        "",
        "Status: local staging plan only. No chunk archives were created and no network action was performed.",
        "",
        "## Totals",
        "",
        f"- Source-core files assigned: {totals['source_core_files_assigned']}",
        f"- Source-core uncompressed bytes assigned: {totals['source_core_uncompressed_bytes_assigned']}",
        f"- Planned chunks: {totals['planned_chunks']}",
        f"- Planned chunks estimated under 20 MB compressed: {totals['planned_chunks_estimated_under_20mb']}",
        f"- Planned chunks estimated over 20 MB compressed: {totals['planned_chunks_estimated_over_20mb']}",
        "- Uploaded chunks: 0",
        "- Network actions performed: false",
        "",
        "## Root Summary",
        "",
        "| Root | Chunks | Files | Bytes |",
        "| --- | ---: | ---: | ---: |",
    ]
    for row in document["root_summary"]:
        lines.append(f"| {row['root_label']} | {row['chunks']} | {row['files']} | {row['bytes']} |")
    lines.extend(
        [
            "",
            "## Planned Chunks",
            "",
            "| Chunk | Root | Files | Uncompressed bytes | Estimated compressed bytes | Under 20 MB estimate |",
            "| --- | --- | ---: | ---: | ---: | --- |",
        ]
    )
    for chunk in document["chunks"]:
        under = str(chunk["estimated_compressed_under_20mb"]).lower()
        lines.append(
            f"| `{chunk['chunk_id']}` | {chunk['root_label']} | {chunk['file_count']} | "
            f"{chunk['uncompressed_bytes']} | {chunk['estimated_compressed_bytes']} | `{under}` |"
        )
    lines.extend(
        [
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
        "- Source-core split upload staging plan: "
        f"{document['totals']['planned_chunks']} planned chunks / "
        f"{document['totals']['source_core_files_assigned']} files / 0 uploaded / local-only"
    )
    text = re.sub(r"- Source-core split upload staging plan: .*", line, text)
    if line not in text:
        marker = "- Archive committed: false"
        rows = text.splitlines()
        for offset, row in enumerate(rows):
            if row.startswith(marker):
                rows.insert(offset + 1, line)
                text = "\n".join(rows) + "\n"
                break
    text = text.replace(
        "source-core archive metadata",
        "source-core archive/staged-upload metadata",
    )
    if "Generated UTC: " in text:
        old = text.split("Generated UTC: ", 1)[1].splitlines()[0]
        text = text.replace(old, manifest["generated_utc"], 1)
    STATUS_INDEX.write_text(text, encoding="utf-8")


def update_manifest(document: dict) -> None:
    manifest = load_json(STATUS_MANIFEST)
    manifest["generated_utc"] = now_utc()
    manifest["source_core_split_upload_staging_plan"] = {
        "status": document["status"],
        "artifact_markdown": OUT_MD.name,
        "artifact_json": OUT_JSON.name,
        "basis_snapshot_json": SNAPSHOT_JSON.name,
        "planned_chunks": document["totals"]["planned_chunks"],
        "source_core_files_assigned": document["totals"]["source_core_files_assigned"],
        "source_core_uncompressed_bytes_assigned": document["totals"]["source_core_uncompressed_bytes_assigned"],
        "planned_chunks_estimated_under_20mb": document["totals"]["planned_chunks_estimated_under_20mb"],
        "planned_chunks_estimated_over_20mb": document["totals"]["planned_chunks_estimated_over_20mb"],
        "uploaded_chunks": 0,
        "no_network_actions_performed": True,
        "actual_chunk_archives_created": False,
        "source_text_copied": False,
        "source_language_terms_copied": False,
        "credentials_or_tokens_copied": False,
    }
    upsert_artifact(manifest, "json", OUT_JSON, "split_upload_plan_built_locally_no_chunks_uploaded")
    upsert_artifact(manifest, "markdown", OUT_MD)
    upsert_artifact(manifest, "scripts", pathlib.Path(__file__))
    update_status_index(document, manifest)
    write_json(STATUS_MANIFEST, manifest)


def main() -> None:
    snapshot = load_json(SNAPSHOT_JSON)
    document = build_document(snapshot)
    write_json(OUT_JSON, document)
    write_markdown(document)
    update_manifest(document)
    print(
        json.dumps(
            {
                "staging_plan_json": str(OUT_JSON),
                "planned_chunks": document["totals"]["planned_chunks"],
                "source_core_files_assigned": document["totals"]["source_core_files_assigned"],
                "no_network_actions_performed": document["no_network_actions_performed"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
