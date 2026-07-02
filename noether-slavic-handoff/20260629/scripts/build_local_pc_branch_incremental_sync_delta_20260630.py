import datetime
import hashlib
import json
import pathlib
import re
from collections import Counter


BASE = pathlib.Path(__file__).resolve().parents[1]
STATUS_MANIFEST = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_MANIFEST_20260629.json"
STATUS_INDEX = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_INDEX_20260629.md"
SYNC_LEDGER_JSON = BASE / "GITHUB_PC_BRANCH_SYNC_LEDGER_20260630.json"
OFFLINE_PLAN_JSON = BASE / "OFFLINE_GITHUB_COMMIT_BATCH_PLAN_20260630.json"
OUT_JSON = BASE / "LOCAL_PC_BRANCH_INCREMENTAL_SYNC_DELTA_20260630.json"
OUT_MD = BASE / "LOCAL_PC_BRANCH_INCREMENTAL_SYNC_DELTA_20260630.md"
SELF_PATH = pathlib.Path(__file__).resolve()

STATUS = "local_only_incremental_sync_delta_candidate_not_remote_diff_not_push"


def now_utc() -> str:
    return datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="microseconds")


def sha256_path(path: pathlib.Path) -> str:
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
    item = {"path": artifact_path(path), "sha256": sha256_path(path), "bytes": path.stat().st_size}
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
                updated["sha256"] = sha256_path(path)
                updated["bytes"] = path.stat().st_size
                refreshed.append(updated)
            else:
                refreshed.append(item)
        manifest["artifacts"][group] = refreshed


def self_artifact_paths() -> set[str]:
    return {artifact_path(OUT_JSON), artifact_path(OUT_MD), artifact_path(SELF_PATH)}


def classify_path(path: str, offline_items: dict[str, dict]) -> dict:
    if path in offline_items:
        row = offline_items[path]
        return {
            "delta_class": "offline_commit_plan_item",
            "upload_class": row.get("upload_class"),
            "commit_batch_id": row.get("commit_batch_id"),
            "ready_for_small_text_commit": row.get("ready_for_small_text_commit"),
            "deferred_until_bandwidth_window": row.get("deferred_until_bandwidth_window"),
        }
    if "GITHUB_PC_BRANCH_SYNC_LEDGER_20260630" in path or "build_github_pc_branch_sync_ledger_20260630.py" in path:
        return {
            "delta_class": "github_sync_ledger_self_excluded_from_offline_commit_plan",
            "upload_class": "small_text_local_sync_ledger",
            "commit_batch_id": "sync-ledger-self-excluded",
            "ready_for_small_text_commit": True,
            "deferred_until_bandwidth_window": False,
        }
    if "OFFLINE_GITHUB_COMMIT_BATCH_PLAN_20260630" in path or "build_offline_github_commit_batch_plan_20260630.py" in path:
        return {
            "delta_class": "offline_commit_plan_self_excluded_from_detailed_commit_rows",
            "upload_class": "small_text_offline_plan_self",
            "commit_batch_id": "offline-plan-self-excluded",
            "ready_for_small_text_commit": True,
            "deferred_until_bandwidth_window": False,
        }
    return {
        "delta_class": "unclassified_manifest_artifact",
        "upload_class": "needs_commit_plan_refresh_or_manual_classification",
        "commit_batch_id": "unclassified",
        "ready_for_small_text_commit": False,
        "deferred_until_bandwidth_window": True,
    }


def build_document(manifest: dict) -> dict:
    sync = load_json(SYNC_LEDGER_JSON)
    offline = load_json(OFFLINE_PLAN_JSON)
    offline_items = {row["path"]: row for row in offline.get("commit_item_rows", [])}
    self_paths = self_artifact_paths()

    rows = []
    for group in ("json", "markdown", "scripts"):
        for item in manifest.get("artifacts", {}).get(group, []):
            path = item["path"]
            if path in self_paths:
                continue
            classification = classify_path(path, offline_items)
            rows.append(
                {
                    "path": path,
                    "artifact_group": group,
                    **classification,
                    "remote_diff_verified": False,
                    "local_payload_candidate": True,
                    "source_text_copied": False,
                    "source_language_terms_copied": False,
                    "credentials_or_tokens_copied": False,
                }
            )
    rows = sorted(rows, key=lambda row: (row["artifact_group"], row["path"]))

    group_counts = Counter(row["artifact_group"] for row in rows)
    delta_class_counts = Counter(row["delta_class"] for row in rows)
    upload_class_counts = Counter(row["upload_class"] for row in rows)
    batch_counts = Counter(row["commit_batch_id"] for row in rows)
    small_ready = sum(1 for row in rows if row["ready_for_small_text_commit"] is True)
    deferred = sum(1 for row in rows if row["deferred_until_bandwidth_window"] is True)

    current_branch = sync.get("current_pc_branch", {})
    github = manifest.get("github", {})
    return {
        "artifact": "local_pc_branch_incremental_sync_delta",
        "status": STATUS,
        "generated_date": "2026-06-30",
        "generated_utc": now_utc(),
        "bandwidth_mode": "local_only_no_network_actions",
        "no_network_actions_performed": True,
        "credentials_or_tokens_copied": False,
        "source_text_copied": False,
        "source_language_terms_copied": False,
        "native_review_status": "not_reviewed",
        "input_artifacts": {
            "status_manifest": STATUS_MANIFEST.name,
            "github_pc_branch_sync_ledger": SYNC_LEDGER_JSON.name,
            "offline_github_commit_batch_plan": OFFLINE_PLAN_JSON.name,
        },
        "branch_context": {
            "repo": current_branch.get("repo", github.get("repo")),
            "branch": current_branch.get("branch", github.get("branch")),
            "base_branch": current_branch.get("base_branch", github.get("base_branch")),
            "draft_pr": current_branch.get("draft_pr", github.get("draft_pr")),
            "last_successfully_pushed_head_before_local_only_work": current_branch.get(
                "last_successfully_pushed_head_before_local_only_work"
            ),
            "manifest_head_before_manifest": github.get("head_before_manifest"),
        },
        "delta_policy": {
            "remote_fetch_performed": False,
            "git_diff_performed": False,
            "remote_branch_state_claim": False,
            "git_commits_created": 0,
            "remote_pushes_performed": 0,
            "pull_requests_opened_or_updated": 0,
            "source_core_archive_deferred": True,
            "source_language_terms_or_passages_copied": False,
            "credentials_or_tokens_copied": False,
        },
        "summary": {
            "candidate_payload_rows_excluding_this_delta": len(rows),
            "json_rows_excluding_this_delta": group_counts.get("json", 0),
            "markdown_rows_excluding_this_delta": group_counts.get("markdown", 0),
            "script_rows_excluding_this_delta": group_counts.get("scripts", 0),
            "delta_self_artifacts_excluded": 3,
            "offline_commit_plan_items_represented": sum(
                count for key, count in delta_class_counts.items() if key == "offline_commit_plan_item"
            ),
            "github_sync_ledger_self_rows": delta_class_counts.get(
                "github_sync_ledger_self_excluded_from_offline_commit_plan", 0
            ),
            "offline_plan_self_rows": delta_class_counts.get(
                "offline_commit_plan_self_excluded_from_detailed_commit_rows", 0
            ),
            "unclassified_manifest_artifacts": delta_class_counts.get("unclassified_manifest_artifact", 0),
            "small_text_ready_or_self_rows": small_ready,
            "bandwidth_deferred_or_unclassified_rows": deferred,
            "large_metadata_deferred_rows_from_offline_plan": offline.get("summary", {}).get(
                "large_metadata_deferred_items", 0
            ),
            "network_actions_performed": 0,
            "remote_fetches_performed": 0,
            "remote_pushes_performed": 0,
        },
        "group_counts": dict(sorted(group_counts.items())),
        "delta_class_counts": dict(sorted(delta_class_counts.items())),
        "upload_class_counts": dict(sorted(upload_class_counts.items())),
        "commit_batch_counts": dict(sorted(batch_counts.items())),
        "delta_rows": rows,
        "boundaries": [
            "This is a local payload inventory candidate, not a remote Git diff.",
            "No remote fetch, push, clone, GitHub API call, commit, or PR update is performed.",
            "No source-language passages, source-language terms, credentials, or tokens are copied.",
            "Source-core archive upload remains deferred until explicit approval or suitable network.",
        ],
    }


def write_markdown(document: dict) -> None:
    summary = document["summary"]
    branch = document["branch_context"]
    lines = [
        "# Local PC branch incremental sync delta - 2026-06-30",
        "",
        "Status: local-only payload inventory candidate. This is not a remote Git diff and performs no fetch, push, commit, PR update, upload, or download.",
        "",
        "## Branch Context",
        "",
        f"- Repository: `{branch['repo']}`",
        f"- Branch: `{branch['branch']}`",
        f"- Base branch: `{branch['base_branch']}`",
        f"- Draft PR: {branch['draft_pr']}",
        f"- Last successfully pushed head before local-only work: `{branch['last_successfully_pushed_head_before_local_only_work']}`",
        "",
        "## Summary",
        "",
        f"- Candidate payload rows excluding this delta artifact: {summary['candidate_payload_rows_excluding_this_delta']}",
        f"- JSON/Markdown/Script rows: {summary['json_rows_excluding_this_delta']} / {summary['markdown_rows_excluding_this_delta']} / {summary['script_rows_excluding_this_delta']}",
        f"- Offline commit-plan rows represented: {summary['offline_commit_plan_items_represented']}",
        f"- GitHub sync ledger self rows: {summary['github_sync_ledger_self_rows']}",
        f"- Offline plan self rows: {summary['offline_plan_self_rows']}",
        f"- Unclassified manifest artifacts: {summary['unclassified_manifest_artifacts']}",
        f"- Small text-ready or self rows: {summary['small_text_ready_or_self_rows']}",
        f"- Bandwidth-deferred or unclassified rows: {summary['bandwidth_deferred_or_unclassified_rows']}",
        "",
        "## Delta Classes",
        "",
        "| Class | Rows |",
        "| --- | ---: |",
    ]
    for key, count in document["delta_class_counts"].items():
        lines.append(f"| `{key}` | {count} |")
    lines.extend(["", "## Boundaries", ""])
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
        "- Local PC branch incremental sync delta: "
        f"{document['summary']['candidate_payload_rows_excluding_this_delta']} candidate rows / "
        f"{document['summary']['unclassified_manifest_artifacts']} unclassified / no remote diff or push"
    )
    if re.search(r"^- Local PC branch incremental sync delta: .*", text, flags=re.MULTILINE):
        text = re.sub(r"^- Local PC branch incremental sync delta: .*", line, text, flags=re.MULTILINE)
    else:
        rows = text.splitlines()
        inserted = False
        for offset, row in enumerate(rows):
            if row.startswith("- GitHub PC branch sync ledger:"):
                rows.insert(offset + 1, line)
                text = "\n".join(rows) + "\n"
                inserted = True
                break
        if not inserted:
            text = text.rstrip() + "\n" + line + "\n"
    if "local-pc-branch-incremental-sync-delta" not in text:
        text = text.replace(
            "github-pc-branch-sync-ledger/offline-commit-batch-plan",
            "github-pc-branch-sync-ledger/local-pc-branch-incremental-sync-delta/offline-commit-batch-plan",
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
    manifest["local_pc_branch_incremental_sync_delta"] = {
        "status": document["status"],
        "artifact_markdown": OUT_MD.name,
        "artifact_json": OUT_JSON.name,
        "candidate_payload_rows_excluding_this_delta": summary["candidate_payload_rows_excluding_this_delta"],
        "json_rows_excluding_this_delta": summary["json_rows_excluding_this_delta"],
        "markdown_rows_excluding_this_delta": summary["markdown_rows_excluding_this_delta"],
        "script_rows_excluding_this_delta": summary["script_rows_excluding_this_delta"],
        "delta_self_artifacts_excluded": 3,
        "offline_commit_plan_items_represented": summary["offline_commit_plan_items_represented"],
        "github_sync_ledger_self_rows": summary["github_sync_ledger_self_rows"],
        "offline_plan_self_rows": summary["offline_plan_self_rows"],
        "unclassified_manifest_artifacts": summary["unclassified_manifest_artifacts"],
        "network_actions_performed": 0,
        "remote_fetches_performed": 0,
        "remote_pushes_performed": 0,
        "no_network_actions_performed": True,
        "credentials_or_tokens_copied": False,
        "source_text_copied": False,
        "source_language_terms_copied": False,
        "native_review_status": "not_reviewed",
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
                "local_pc_branch_incremental_sync_delta_json": str(OUT_JSON),
                "candidate_payload_rows_excluding_this_delta": document["summary"][
                    "candidate_payload_rows_excluding_this_delta"
                ],
                "unclassified_manifest_artifacts": document["summary"]["unclassified_manifest_artifacts"],
                "network_actions_performed": document["summary"]["network_actions_performed"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
