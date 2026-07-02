import datetime
import hashlib
import json
import pathlib
import re


BASE = pathlib.Path(__file__).resolve().parents[1]
STATUS_MANIFEST = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_MANIFEST_20260629.json"
STATUS_INDEX = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_INDEX_20260629.md"
OUT_JSON = BASE / "GITHUB_PC_BRANCH_SYNC_LEDGER_20260630.json"
OUT_MD = BASE / "GITHUB_PC_BRANCH_SYNC_LEDGER_20260630.md"
SELF_PATH = pathlib.Path(__file__).resolve()
LOCAL_PC_BRANCH_AUDIT_JSON = BASE / "LOCAL_PC_BRANCH_COORDINATION_AUDIT_20260630.json"
LOCAL_PC_BRANCH_AUDIT_MD = BASE / "LOCAL_PC_BRANCH_COORDINATION_AUDIT_20260630.md"
LOCAL_PC_BRANCH_AUDIT_SCRIPT = BASE / "scripts" / "build_local_pc_branch_coordination_audit_20260630.py"

STATUS = "local_github_pc_branch_sync_ledger_no_network_no_remote_update"
LOCAL_PC_BRANCH_AUDIT_STATUS = "local_only_branch_coordination_audit_not_remote_branch_state_not_completion_claim"
SELF_ARTIFACT_PATHS = {
    "noether-slavic-handoff/20260629/GITHUB_PC_BRANCH_SYNC_LEDGER_20260630.json",
    "noether-slavic-handoff/20260629/GITHUB_PC_BRANCH_SYNC_LEDGER_20260630.md",
    "noether-slavic-handoff/20260629/scripts/build_github_pc_branch_sync_ledger_20260630.py",
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


def register_local_pc_branch_audit(manifest: dict) -> None:
    if LOCAL_PC_BRANCH_AUDIT_JSON.exists():
        upsert_artifact(manifest, "json", LOCAL_PC_BRANCH_AUDIT_JSON, LOCAL_PC_BRANCH_AUDIT_STATUS)
    if LOCAL_PC_BRANCH_AUDIT_MD.exists():
        upsert_artifact(manifest, "markdown", LOCAL_PC_BRANCH_AUDIT_MD)
    if LOCAL_PC_BRANCH_AUDIT_SCRIPT.exists():
        upsert_artifact(manifest, "scripts", LOCAL_PC_BRANCH_AUDIT_SCRIPT)


def target_counts_after_registration(manifest: dict) -> dict:
    paths_by_group = {
        group: {item["path"] for item in manifest["artifacts"][group]}
        for group in ("json", "markdown", "scripts")
    }
    paths_by_group["json"].add(artifact_path(OUT_JSON))
    paths_by_group["markdown"].add(artifact_path(OUT_MD))
    paths_by_group["scripts"].add(artifact_path(SELF_PATH))
    return {group: len(paths) for group, paths in paths_by_group.items()}


def is_real_git_marker(marker: pathlib.Path) -> bool:
    if marker.is_dir():
        return (marker / "HEAD").is_file() and (marker / "objects").is_dir() and (marker / "refs").is_dir()
    if marker.is_file():
        try:
            text = marker.read_text(encoding="utf-8", errors="ignore").strip()
        except OSError:
            return False
        if not text.startswith("gitdir:"):
            return False
        target = (marker.parent / text.split(":", 1)[1].strip()).resolve()
        return is_real_git_marker(target)
    return False


def find_git_root(start: pathlib.Path) -> pathlib.Path | None:
    try:
        current = start.resolve()
    except OSError:
        current = start
    candidates = [current] + list(current.parents)
    for path in candidates:
        if is_real_git_marker(path / ".git"):
            return path
    return None


def upload_class(group: str, item: dict) -> str:
    name = pathlib.PurePosixPath(item["path"]).name
    size = int(item.get("bytes", 0))
    if group == "scripts":
        return "script_ready_for_small_text_push"
    if name.endswith(".md"):
        return "markdown_ready_for_small_text_push"
    if size <= 2_000_000:
        return "json_ready_for_small_text_push"
    if name in {
        "NOETHER_SOURCE_CORE_TEXT_TEX_WORKBOOKS_SNAPSHOT_20260629.json",
        "SOURCE_CORE_SPLIT_UPLOAD_STAGING_PLAN_20260630.json",
    }:
        return "large_json_metadata_ready_when_bandwidth_allows"
    return "large_json_ready_when_bandwidth_allows"


def payload_items(manifest: dict) -> list[dict]:
    rows = []
    for group in ("markdown", "json", "scripts"):
        for item in manifest["artifacts"][group]:
            if item["path"] in SELF_ARTIFACT_PATHS:
                continue
            path = artifact_local_path(item["path"])
            rows.append(
                {
                    "path": item["path"],
                    "artifact_group": group,
                    "bytes": item.get("bytes"),
                    "sha256": item.get("sha256"),
                    "exists_locally": path.exists(),
                    "upload_class": upload_class(group, item),
                    "contains_source_passages": False,
                    "credentials_or_tokens_copied": False,
                }
            )
    return sorted(rows, key=lambda row: (row["artifact_group"], row["path"]))


def class_summary(rows: list[dict]) -> dict:
    summary: dict[str, dict[str, int]] = {}
    for row in rows:
        bucket = summary.setdefault(row["upload_class"], {"items": 0, "bytes": 0})
        bucket["items"] += 1
        bucket["bytes"] += int(row.get("bytes") or 0)
    return dict(sorted(summary.items()))


def build_document(manifest: dict) -> dict:
    counts_after = target_counts_after_registration(manifest)
    rows = payload_items(manifest)
    github = manifest.get("github", {})
    source_core = manifest.get("source_core_upload", {})
    archive = source_core.get("archive", {})
    project_workspace = pathlib.Path(manifest.get("projectless_thread_workspace", BASE.parent))
    git_root = find_git_root(project_workspace)
    source_split = manifest.get("source_core_split_upload_staging_plan", {})
    orientation = manifest.get("previous_session_orientation_and_github_sync_queue", {})

    total_text_bytes = sum(int(row.get("bytes") or 0) for row in rows)
    small_text_rows = [
        row
        for row in rows
        if row["upload_class"]
        in {
            "script_ready_for_small_text_push",
            "markdown_ready_for_small_text_push",
            "json_ready_for_small_text_push",
        }
    ]
    large_text_rows = [row for row in rows if row not in small_text_rows]

    return {
        "artifact": "github_pc_branch_sync_ledger",
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
        "current_pc_branch": {
            "repo": github.get("repo"),
            "branch": github.get("branch"),
            "base_branch": github.get("base_branch"),
            "draft_pr": github.get("draft_pr"),
            "last_successfully_pushed_head_before_local_only_work": orientation.get(
                "last_successfully_pushed_head_before_local_only_work",
                "db7ffc6ca62116d9f8dd8c5ba156e7e2c7c953a2",
            ),
            "sync_status": "local_payload_ready_remote_update_deferred_due_to_bandwidth",
        },
        "local_workspace_git_state": {
            "projectless_thread_workspace": str(project_workspace),
            "current_workspace_git_checkout": git_root is not None,
            "detected_git_root": str(git_root) if git_root else None,
            "payload_workspace": str(BASE),
            "payload_workspace_is_git_checkout": find_git_root(BASE) is not None,
        },
        "payload_artifact_counts_after_registration": counts_after,
        "payload_items_excluding_this_ledger": len(rows),
        "payload_bytes_excluding_deferred_archive": total_text_bytes,
        "small_text_ready_items": len(small_text_rows),
        "small_text_ready_bytes": sum(int(row.get("bytes") or 0) for row in small_text_rows),
        "large_text_metadata_items": len(large_text_rows),
        "large_text_metadata_bytes": sum(int(row.get("bytes") or 0) for row in large_text_rows),
        "upload_class_summary": class_summary(rows),
        "recommended_commit_groups": [
            {
                "id": "01_manifest_status_and_branch_handoff",
                "status": "ready_for_small_text_push_when_network_allowed",
                "contents": [
                    "status manifest and index",
                    "PC branch maintenance note",
                    "orientation and sync queue",
                    "local PC branch coordination audit",
                    "GitHub PC branch sync ledger",
                ],
                "requires_network": True,
                "performed_now": False,
            },
            {
                "id": "02_lane_evidence_terminology_and_research_scaffolds",
                "status": "ready_for_text_push_when_network_allowed",
                "contents": [
                    "source evidence seed/reinforcement artifacts",
                    "term-anchor seeds",
                    "glossary/rationale seeds",
                    "interlanguage and publication-methodology artifacts",
                ],
                "requires_network": True,
                "performed_now": False,
            },
            {
                "id": "03_review_workflow_packets_and_ledgers",
                "status": "ready_as_blank_or_blocked_scaffold_text_when_network_allowed",
                "contents": [
                    "review packet templates",
                    "blank note capture forms",
                    "ready note-entry packet",
                    "manual/source-review packet",
                    "accepted-correction ledger template",
                ],
                "requires_network": True,
                "performed_now": False,
            },
            {
                "id": "04_large_text_metadata",
                "status": "text_ready_but_bandwidth_sensitive",
                "contents": [
                    "source-core snapshot JSON metadata",
                    "source-core split upload plan JSON metadata",
                    "large draft reviewer glossary index JSON",
                ],
                "requires_network": True,
                "performed_now": False,
            },
            {
                "id": "05_source_core_archive",
                "status": "deferred_do_not_push_until_user_approves_suitable_network_or_release_strategy",
                "contents": ["NOETHER_SOURCE_CORE_TEXT_TEX_WORKBOOKS_SNAPSHOT_20260629.zip"],
                "requires_network": True,
                "performed_now": False,
            },
        ],
        "deferred_payloads": [
            {
                "id": "source_core_text_tex_workbooks_snapshot_zip",
                "status": "deferred_due_to_bandwidth_not_committed",
                "path": archive.get("path"),
                "sha256": archive.get("sha256"),
                "bytes": archive.get("bytes"),
                "contains_pdf_image_or_archive_payloads": archive.get("contains_pdf_image_or_archive_payloads"),
                "archive_committed": source_core.get("archive_committed"),
            }
        ],
        "source_core_split_plan": {
            "planned_chunks": source_split.get("planned_chunks"),
            "uploaded_chunks": source_split.get("uploaded_chunks"),
            "actual_chunk_archives_created": source_split.get("actual_chunk_archives_created"),
            "no_network_actions_performed": source_split.get("no_network_actions_performed"),
        },
        "local_pc_branch_coordination_audit": {
            "artifact_json": LOCAL_PC_BRANCH_AUDIT_JSON.name,
            "artifact_markdown": LOCAL_PC_BRANCH_AUDIT_MD.name,
            "artifact_script": "scripts/build_local_pc_branch_coordination_audit_20260630.py",
            "status": LOCAL_PC_BRANCH_AUDIT_STATUS,
            "exists_locally": LOCAL_PC_BRANCH_AUDIT_JSON.exists() and LOCAL_PC_BRANCH_AUDIT_MD.exists(),
        },
        "self_registered_artifacts": sorted(SELF_ARTIFACT_PATHS),
        "payload_items": rows,
        "boundaries": [
            "This ledger is local-only and performs no fetch, push, clone, upload, download, or GitHub API call.",
            "This is not a GitHub synchronization claim and not a remote branch state claim.",
            "This does not copy source-language passages or native-register source terms.",
            "This records no user credentials, tokens, or secrets.",
            "The source-core zip remains deferred until explicit user approval or a suitable network/release strategy.",
            "The active Noether multilingual goal remains open.",
        ],
    }


def write_markdown(document: dict) -> None:
    branch = document["current_pc_branch"]
    counts = document["payload_artifact_counts_after_registration"]
    git_state = document["local_workspace_git_state"]
    deferred = document["deferred_payloads"][0]
    lines = [
        "# GitHub PC branch sync ledger - 2026-06-30",
        "",
        "Status: local sync ledger only. No fetch, push, clone, upload, download, or GitHub API call was performed.",
        "",
        "## Branch",
        "",
        f"- Repository: `{branch['repo']}`",
        f"- Branch: `{branch['branch']}`",
        f"- Base branch: `{branch['base_branch']}`",
        f"- Draft PR: {branch['draft_pr']}",
        f"- Sync status: `{branch['sync_status']}`",
        "",
        "## Local Git State",
        "",
        f"- Current workspace Git checkout: `{str(git_state['current_workspace_git_checkout']).lower()}`",
        f"- Detected Git root: `{git_state['detected_git_root']}`",
        f"- Payload workspace: `{git_state['payload_workspace']}`",
        "",
        "## Payload Counts After Registration",
        "",
        f"- JSON artifacts indexed: {counts['json']}",
        f"- Markdown artifacts indexed: {counts['markdown']}",
        f"- Scripts indexed: {counts['scripts']}",
        f"- Payload items excluding this ledger: {document['payload_items_excluding_this_ledger']}",
        f"- Small text-ready items: {document['small_text_ready_items']}",
        f"- Large text metadata items: {document['large_text_metadata_items']}",
        f"- Network actions performed: `{str((not document['no_network_actions_performed'])).lower()}`",
        "",
        "## Commit Groups",
        "",
        "| Group | Status | Performed now |",
        "| --- | --- | --- |",
    ]
    for group in document["recommended_commit_groups"]:
        lines.append(f"| `{group['id']}` | `{group['status']}` | `{str(group['performed_now']).lower()}` |")
    lines.extend(
        [
            "",
            "## Deferred Payloads",
            "",
            f"- `{deferred['id']}`: `{deferred['status']}`",
            f"- Path: `{deferred['path']}`",
            f"- Bytes: {deferred['bytes']}",
            f"- SHA-256: `{deferred['sha256']}`",
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
    line = (
        "- GitHub PC branch sync ledger: "
        f"{document['payload_items_excluding_this_ledger']} payload items excluding ledger / "
        f"{document['small_text_ready_items']} small text-ready / "
        "source-core archive deferred / 0 network actions"
    )
    audit = {}
    if LOCAL_PC_BRANCH_AUDIT_JSON.exists():
        audit = load_json(LOCAL_PC_BRANCH_AUDIT_JSON)
    audit_line = (
        "- Local PC branch coordination audit: "
        f"{len(audit.get('included_pc_workstreams', []))} workstreams / "
        f"branch `{manifest.get('github', {}).get('branch')}` / "
        "remote branch fetch false / 0 network actions"
    )
    if re.search(r"^- GitHub PC branch sync ledger: .*", text, flags=re.MULTILINE):
        text = re.sub(r"^- GitHub PC branch sync ledger: .*", line, text, flags=re.MULTILINE)
    else:
        marker = "- Previous-session orientation and GitHub sync queue:"
        rows = text.splitlines()
        for offset, row in enumerate(rows):
            if row.startswith(marker):
                rows.insert(offset + 1, line)
                text = "\n".join(rows) + "\n"
                break
    if re.search(r"^- Local PC branch coordination audit: .*", text, flags=re.MULTILINE):
        text = re.sub(r"^- Local PC branch coordination audit: .*", audit_line, text, flags=re.MULTILINE)
    else:
        marker = "- Previous-session orientation and GitHub sync queue:"
        rows = text.splitlines()
        for offset, row in enumerate(rows):
            if row.startswith(marker):
                rows.insert(offset + 1, audit_line)
                text = "\n".join(rows) + "\n"
                break
    text = text.replace(
        "local-handoff/orientation-sync-queue metadata, research publication metadata",
        "local-handoff/orientation-sync-queue/local-pc-branch-coordination/github-pc-branch-sync-ledger metadata, research publication metadata",
    )
    text = text.replace(
        "local-handoff/orientation-sync-queue/github-pc-branch-sync-ledger metadata",
        "local-handoff/orientation-sync-queue/local-pc-branch-coordination/github-pc-branch-sync-ledger metadata",
    )
    text = text.replace(
        "local-pc-branch-coordination/local-pc-branch-coordination",
        "local-pc-branch-coordination",
    )
    text = text.replace(
        "page-context forms, GitHub sync ledger",
        "page-context forms, local PC branch coordination, GitHub sync ledger",
    )
    text = text.replace(
        "page-context forms, local PC branch coordination, local PC branch coordination, GitHub sync ledger",
        "page-context forms, local PC branch coordination, GitHub sync ledger",
    )
    if "Generated UTC: " in text:
        old = text.split("Generated UTC: ", 1)[1].splitlines()[0]
        text = text.replace(old, manifest["generated_utc"], 1)
    STATUS_INDEX.write_text(text, encoding="utf-8")


def update_manifest(document: dict) -> None:
    manifest = load_json(STATUS_MANIFEST)
    manifest["generated_utc"] = now_utc()

    register_local_pc_branch_audit(manifest)
    upsert_artifact(manifest, "json", OUT_JSON, STATUS)
    upsert_artifact(manifest, "markdown", OUT_MD)
    upsert_artifact(manifest, "scripts", SELF_PATH)
    refresh_existing_artifact_hashes(manifest)

    manifest["github_pc_branch_sync_ledger"] = {
        "status": document["status"],
        "artifact_markdown": OUT_MD.name,
        "artifact_json": OUT_JSON.name,
        "payload_artifact_counts_after_registration": {
            "json": len(manifest["artifacts"]["json"]),
            "markdown": len(manifest["artifacts"]["markdown"]),
            "scripts": len(manifest["artifacts"]["scripts"]),
        },
        "payload_items_excluding_this_ledger": document["payload_items_excluding_this_ledger"],
        "small_text_ready_items": document["small_text_ready_items"],
        "large_text_metadata_items": document["large_text_metadata_items"],
        "source_core_archive_deferred": True,
        "source_core_archive_committed": False,
        "current_workspace_git_checkout": document["local_workspace_git_state"]["current_workspace_git_checkout"],
        "no_network_actions_performed": True,
        "credentials_or_tokens_copied": False,
        "source_text_copied": False,
        "source_language_terms_copied": False,
        "native_review_status": "not_reviewed",
        "current_approved_terms": 0,
        "current_accepted_corrections": 0,
    }
    audit = load_json(LOCAL_PC_BRANCH_AUDIT_JSON) if LOCAL_PC_BRANCH_AUDIT_JSON.exists() else {}
    audit_other = audit.get("other_branch_coordination", {})
    manifest["local_pc_branch_coordination_audit"] = {
        "status": audit.get("status", LOCAL_PC_BRANCH_AUDIT_STATUS),
        "artifact_markdown": LOCAL_PC_BRANCH_AUDIT_MD.name,
        "artifact_json": LOCAL_PC_BRANCH_AUDIT_JSON.name,
        "artifact_script": "scripts/build_local_pc_branch_coordination_audit_20260630.py",
        "included_pc_workstreams": len(audit.get("included_pc_workstreams", [])),
        "branch_role": audit.get("current_pc_branch", {}).get("branch_role"),
        "exact_predecessor_thread_id": audit.get("orientation", {}).get("exact_predecessor_thread_id"),
        "remote_branch_fetch_performed": audit_other.get("remote_branch_fetch_performed"),
        "remote_branch_state_claim": audit_other.get("remote_branch_state_claim"),
        "local_other_branch_claim": audit_other.get("local_other_branch_claim"),
        "no_network_actions_performed": True,
        "credentials_or_tokens_copied": False,
        "source_text_copied": False,
        "source_language_terms_copied": False,
        "native_review_status": "not_reviewed",
        "current_approved_terms": 0,
        "current_accepted_corrections": 0,
    }
    document["payload_artifact_counts_after_registration"] = manifest["github_pc_branch_sync_ledger"][
        "payload_artifact_counts_after_registration"
    ]
    write_json(OUT_JSON, document)
    write_markdown(document)

    register_local_pc_branch_audit(manifest)
    upsert_artifact(manifest, "json", OUT_JSON, STATUS)
    upsert_artifact(manifest, "markdown", OUT_MD)
    upsert_artifact(manifest, "scripts", SELF_PATH)
    refresh_existing_artifact_hashes(manifest)
    update_status_index(document, manifest)
    write_json(STATUS_MANIFEST, manifest)


def main() -> None:
    manifest = load_json(STATUS_MANIFEST)
    register_local_pc_branch_audit(manifest)
    refresh_existing_artifact_hashes(manifest)
    document = build_document(manifest)
    write_json(OUT_JSON, document)
    write_markdown(document)
    update_manifest(document)
    print(
        json.dumps(
            {
                "sync_ledger_json": str(OUT_JSON),
                "payload_items_excluding_this_ledger": document["payload_items_excluding_this_ledger"],
                "small_text_ready_items": document["small_text_ready_items"],
                "large_text_metadata_items": document["large_text_metadata_items"],
                "no_network_actions_performed": document["no_network_actions_performed"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
