import datetime
import hashlib
import json
import pathlib
import re
from collections import defaultdict


BASE = pathlib.Path(__file__).resolve().parents[1]
STATUS_MANIFEST = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_MANIFEST_20260629.json"
STATUS_INDEX = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_INDEX_20260629.md"
SYNC_LEDGER_JSON = BASE / "GITHUB_PC_BRANCH_SYNC_LEDGER_20260630.json"
OUT_JSON = BASE / "OFFLINE_GITHUB_COMMIT_BATCH_PLAN_20260630.json"
OUT_MD = BASE / "OFFLINE_GITHUB_COMMIT_BATCH_PLAN_20260630.md"
SELF_PATH = pathlib.Path(__file__).resolve()

STATUS = "offline_github_commit_batch_plan_no_network_no_remote_update"
SELF_ARTIFACT_PATHS = {
    "noether-slavic-handoff/20260629/OFFLINE_GITHUB_COMMIT_BATCH_PLAN_20260630.json",
    "noether-slavic-handoff/20260629/OFFLINE_GITHUB_COMMIT_BATCH_PLAN_20260630.md",
    "noether-slavic-handoff/20260629/scripts/build_offline_github_commit_batch_plan_20260630.py",
}

SMALL_UPLOAD_CLASSES = {
    "script_ready_for_small_text_push",
    "markdown_ready_for_small_text_push",
    "json_ready_for_small_text_push",
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


def batch_for_path(path: str, artifact_group: str, upload_class: str) -> tuple[str, str]:
    name = pathlib.PurePosixPath(path).name
    if upload_class not in SMALL_UPLOAD_CLASSES:
        return ("07_large_metadata_deferred", "Large metadata deferred until bandwidth window")
    if artifact_group == "scripts":
        return ("06_reproducibility_scripts", "Reproducibility scripts and validators")
    if name.startswith("NOETHER_PC_MULTILINGUAL_STATUS") or name.startswith("PC_BRANCH_MAINTENANCE") or name.startswith(
        "PREVIOUS_SESSION_ORIENTATION"
    ) or name.startswith("LOCAL_PC_BRANCH_COORDINATION") or name.startswith("GITHUB_PC_BRANCH_SYNC_LEDGER"):
        return ("01_status_branch_orientation", "Status manifest, branch handoff, and orientation")
    if (
        "SOURCE_WITNESS" in name
        or "SOURCE_CORE" in name
        or name.startswith("LOCAL_SOURCE")
        or name.startswith("SOURCE_CORE_SPLIT")
        or name.startswith("INTEGRATED_LANE_HANDOFF")
        or name.startswith("LANE_PROMOTION")
        or "DELTA" in name
    ):
        return ("02_source_core_packaging_and_lane_handoff", "Source-core packaging and lane handoff metadata")
    if (
        "REVIEW" in name
        or "CORRECTION" in name
        or "PACKET" in name
        or "PAGE_CONTEXT" in name
        or "MANUAL_SOURCE" in name
        or "AUTHORITY" in name
    ):
        return ("03_review_authority_packets", "Review, authority, and correction-ingestion packets")
    if (
        "INTERLANGUAGE" in name
        or "METHODOLOGY" in name
        or "AI_TECHNICAL" in name
        or "TERMINOLOGY_GOVERNANCE" in name
        or "TERM_ID" in name
        or "DRAFT_REVIEWER" in name
        or "LANE_TERM" in name
    ):
        return ("04_methodology_publication_and_terminology_governance", "Methodology publication and terminology governance")
    return ("05_language_evidence_and_term_seeds", "Language evidence shelves, term anchors, and rationale seeds")


def build_commit_rows(sync_ledger: dict) -> list[dict]:
    rows = []
    for item in sync_ledger.get("payload_items", []):
        if item.get("path") in SELF_ARTIFACT_PATHS:
            continue
        batch_id, batch_label = batch_for_path(item["path"], item["artifact_group"], item["upload_class"])
        ready_for_small_text_commit = item["upload_class"] in SMALL_UPLOAD_CLASSES
        rows.append(
            {
                "path": item["path"],
                "artifact_group": item["artifact_group"],
                "bytes": item["bytes"],
                "sha256": item["sha256"],
                "upload_class": item["upload_class"],
                "commit_batch_id": batch_id,
                "commit_batch_label": batch_label,
                "ready_for_small_text_commit": ready_for_small_text_commit,
                "deferred_until_bandwidth_window": not ready_for_small_text_commit,
                "exists_locally": item.get("exists_locally"),
                "contains_source_passages": False,
                "credentials_or_tokens_copied": False,
                "source_text_copied": False,
                "source_language_terms_copied": False,
            }
        )
    return sorted(rows, key=lambda row: (row["commit_batch_id"], row["artifact_group"], row["path"]))


def build_batch_rows(commit_rows: list[dict]) -> list[dict]:
    batches: dict[str, dict] = {}
    for row in commit_rows:
        batch = batches.setdefault(
            row["commit_batch_id"],
            {
                "commit_batch_id": row["commit_batch_id"],
                "commit_batch_label": row["commit_batch_label"],
                "items": 0,
                "bytes": 0,
                "small_text_ready_items": 0,
                "large_metadata_deferred_items": 0,
                "network_required_to_push": True,
                "performed_now": False,
                "source_text_copied": False,
                "source_language_terms_copied": False,
                "credentials_or_tokens_copied": False,
            },
        )
        batch["items"] += 1
        batch["bytes"] += int(row.get("bytes") or 0)
        if row["ready_for_small_text_commit"]:
            batch["small_text_ready_items"] += 1
        else:
            batch["large_metadata_deferred_items"] += 1
    return [batches[key] for key in sorted(batches)]


def upload_class_rows(commit_rows: list[dict]) -> list[dict]:
    values: dict[str, dict] = defaultdict(lambda: {"items": 0, "bytes": 0})
    for row in commit_rows:
        values[row["upload_class"]]["items"] += 1
        values[row["upload_class"]]["bytes"] += int(row.get("bytes") or 0)
    return [{"upload_class": key, **value} for key, value in sorted(values.items())]


def build_summary(commit_rows: list[dict], batch_rows: list[dict], sync_ledger: dict, manifest: dict) -> dict:
    small_rows = [row for row in commit_rows if row["ready_for_small_text_commit"]]
    large_rows = [row for row in commit_rows if row["deferred_until_bandwidth_window"]]
    return {
        "source_sync_payload_items_excluding_ledger": sync_ledger.get("payload_items_excluding_this_ledger"),
        "commit_plan_rows_excluding_this_plan": len(commit_rows),
        "small_text_commit_ready_items_excluding_this_plan": len(small_rows),
        "large_metadata_deferred_items": len(large_rows),
        "commit_plan_bytes_excluding_this_plan": sum(int(row.get("bytes") or 0) for row in commit_rows),
        "small_text_commit_ready_bytes_excluding_this_plan": sum(int(row.get("bytes") or 0) for row in small_rows),
        "large_metadata_deferred_bytes": sum(int(row.get("bytes") or 0) for row in large_rows),
        "commit_batches": len(batch_rows),
        "small_text_batches": sum(1 for row in batch_rows if row["small_text_ready_items"] > 0),
        "large_metadata_batches": sum(1 for row in batch_rows if row["large_metadata_deferred_items"] > 0),
        "manifest_json_artifacts_at_build_time": len(manifest["artifacts"]["json"]),
        "manifest_markdown_artifacts_at_build_time": len(manifest["artifacts"]["markdown"]),
        "manifest_script_artifacts_at_build_time": len(manifest["artifacts"]["scripts"]),
        "validation_commands": 8,
        "network_actions_performed": 0,
        "git_commits_created": 0,
        "remote_pushes_performed": 0,
        "pull_requests_opened_or_updated": 0,
        "review_packet_population_performed": False,
        "translation_or_revision_performed": False,
        "canonical_completion_claim": False,
        "publication_completion_claim": False,
        "native_review_status": "not_reviewed",
        "current_approved_terms": 0,
        "current_accepted_corrections": 0,
    }


def build_document(manifest: dict) -> dict:
    sync_ledger = load_json(SYNC_LEDGER_JSON)
    commit_rows = build_commit_rows(sync_ledger)
    batch_rows = build_batch_rows(commit_rows)
    return {
        "artifact": "offline_github_commit_batch_plan",
        "generated_utc": now_utc(),
        "generated_date": "20260630",
        "status": STATUS,
        "bandwidth_mode": "local_only_no_network_actions",
        "inputs": {
            "status_manifest": STATUS_MANIFEST.name,
            "github_pc_branch_sync_ledger": SYNC_LEDGER_JSON.name,
        },
        "commit_policy": {
            "plan_excludes_its_own_artifacts_to_avoid_self_hash_loop": True,
            "small_text_items_ready_for_future_push_only": True,
            "large_metadata_deferred_until_bandwidth_window": True,
            "source_core_archive_deferred_until_explicit_network_approval": True,
            "no_git_commit_created_by_this_plan": True,
            "no_remote_push_or_pr_update_by_this_plan": True,
            "validation_required_before_future_push": True,
        },
        "summary": build_summary(commit_rows, batch_rows, sync_ledger, manifest),
        "validation_gates": [
            "python scripts/validate_noether_pc_status_manifest_20260629.py",
            "scan for GitHub fine-grained token marker",
            "scan for GitHub classic token marker",
            "scan for private-key block marker",
            "scan for source-passage field marker",
            "scan for copied-credential true flag",
            "scan for copied-source-text true flag",
            "scan for copied-source-language-term true flag",
        ],
        "commit_batch_rows": batch_rows,
        "upload_class_rows": upload_class_rows(commit_rows),
        "commit_item_rows": commit_rows,
        "boundaries": {
            "local_metadata_plan_only": True,
            "git_commit_not_created": True,
            "remote_push_not_performed": True,
            "source_text_not_copied": True,
            "source_language_terms_not_copied": True,
            "credentials_or_tokens_not_copied": True,
            "no_network_actions_performed": True,
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
        "# Offline GitHub Commit Batch Plan - 2026-06-30",
        "",
        f"Status: `{document['status']}`",
        "",
        "This is a local-only commit/handoff plan for the PC branch payload. It creates no commit, performs no push, opens no PR update, and copies no source text or credentials.",
        "",
        "## Summary",
        "",
        f"- Plan rows, excluding this plan's own artifacts: {summary['commit_plan_rows_excluding_this_plan']}",
        f"- Small text-ready rows: {summary['small_text_commit_ready_items_excluding_this_plan']} / {summary['small_text_commit_ready_bytes_excluding_this_plan']} bytes",
        f"- Large metadata deferred rows: {summary['large_metadata_deferred_items']} / {summary['large_metadata_deferred_bytes']} bytes",
        f"- Commit batches: {summary['commit_batches']}",
        "- Commits created: 0; pushes: 0; PR updates: 0",
        "",
        "## Batches",
        "",
        "| Batch | Items | Bytes | Small-ready | Deferred large |",
        "|---|---:|---:|---:|---:|",
    ]
    for row in document["commit_batch_rows"]:
        lines.append(
            f"| {row['commit_batch_id']} | {row['items']} | {row['bytes']} | {row['small_text_ready_items']} | {row['large_metadata_deferred_items']} |"
        )
    lines.extend(
        [
            "",
            "## Upload Classes",
            "",
            "| Upload class | Items | Bytes |",
            "|---|---:|---:|",
        ]
    )
    for row in document["upload_class_rows"]:
        lines.append(f"| {row['upload_class']} | {row['items']} | {row['bytes']} |")
    lines.extend(
        [
            "",
            "## Validation Gates",
            "",
        ]
    )
    for gate in document["validation_gates"]:
        lines.append(f"- `{gate}`")
    lines.extend(
        [
            "",
            "## Boundary Notes",
            "",
            "- The plan excludes its own JSON/Markdown/script rows from detailed counts to avoid a self-hash loop.",
            "- Large metadata remains deferred until an explicit bandwidth window or approval.",
            "- The source-core archive remains deferred.",
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
        "- Offline GitHub commit batch plan: "
        f"{summary['commit_plan_rows_excluding_this_plan']} planned rows / "
        f"{summary['small_text_commit_ready_items_excluding_this_plan']} small text-ready / "
        f"{summary['large_metadata_deferred_items']} large metadata deferred / "
        "0 commits or network actions"
    )
    if re.search(r"^- Offline GitHub commit batch plan: .*", text, flags=re.MULTILINE):
        text = re.sub(r"^- Offline GitHub commit batch plan: .*", line, text, flags=re.MULTILINE)
    else:
        marker = "- GitHub PC branch sync ledger:"
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
        "local-handoff/orientation-sync-queue/github-pc-branch-sync-ledger metadata",
        "local-handoff/orientation-sync-queue/github-pc-branch-sync-ledger/offline-commit-batch-plan metadata",
    )
    text = text.replace(
        "local-handoff/orientation-sync-queue/local-pc-branch-coordination/github-pc-branch-sync-ledger metadata",
        "local-handoff/orientation-sync-queue/local-pc-branch-coordination/github-pc-branch-sync-ledger/offline-commit-batch-plan metadata",
    )
    text = text.replace("offline-commit-batch-plan/offline-commit-batch-plan metadata", "offline-commit-batch-plan metadata")
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
    manifest["offline_github_commit_batch_plan"] = {
        "status": document["status"],
        "artifact_markdown": OUT_MD.name,
        "artifact_json": OUT_JSON.name,
        "source_sync_payload_items_excluding_ledger": summary["source_sync_payload_items_excluding_ledger"],
        "commit_plan_rows_excluding_this_plan": summary["commit_plan_rows_excluding_this_plan"],
        "small_text_commit_ready_items_excluding_this_plan": summary["small_text_commit_ready_items_excluding_this_plan"],
        "large_metadata_deferred_items": summary["large_metadata_deferred_items"],
        "commit_plan_bytes_excluding_this_plan": summary["commit_plan_bytes_excluding_this_plan"],
        "small_text_commit_ready_bytes_excluding_this_plan": summary["small_text_commit_ready_bytes_excluding_this_plan"],
        "large_metadata_deferred_bytes": summary["large_metadata_deferred_bytes"],
        "commit_batches": summary["commit_batches"],
        "validation_commands": summary["validation_commands"],
        "network_actions_performed": 0,
        "git_commits_created": 0,
        "remote_pushes_performed": 0,
        "pull_requests_opened_or_updated": 0,
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
                "offline_github_commit_batch_plan_json": str(OUT_JSON),
                "commit_plan_rows_excluding_this_plan": document["summary"]["commit_plan_rows_excluding_this_plan"],
                "small_text_commit_ready_items_excluding_this_plan": document["summary"][
                    "small_text_commit_ready_items_excluding_this_plan"
                ],
                "large_metadata_deferred_items": document["summary"]["large_metadata_deferred_items"],
                "commit_batches": document["summary"]["commit_batches"],
                "network_actions_performed": document["summary"]["network_actions_performed"],
                "no_network_actions_performed": document["no_network_actions_performed"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
