import datetime
import hashlib
import json
import pathlib
import re


BASE = pathlib.Path(__file__).resolve().parents[1]
STATUS_MANIFEST = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_MANIFEST_20260629.json"
STATUS_INDEX = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_INDEX_20260629.md"
OUT_JSON = BASE / "PREVIOUS_SESSION_ORIENTATION_AND_GITHUB_SYNC_QUEUE_20260630.json"
OUT_MD = BASE / "PREVIOUS_SESSION_ORIENTATION_AND_GITHUB_SYNC_QUEUE_20260630.md"

USER_HOME = pathlib.Path.home()
PREDECESSOR_SESSION = (
    USER_HOME
    / ".codex"
    / "sessions"
    / "2026"
    / "06"
    / "09"
    / "rollout-2026-06-09T20-13-49-019ead97-38c8-7112-9b9c-e8c176d526a1.jsonl"
)
PARALLEL_HANDOFF_SESSION = (
    USER_HOME
    / ".codex"
    / "sessions"
    / "2026"
    / "06"
    / "28"
    / "rollout-2026-06-28T22-58-58-019f1007-406b-7cc3-a3cf-ac23517cd8a6.jsonl"
)
CURRENT_TAKEOVER_SESSION = (
    USER_HOME
    / ".codex"
    / "sessions"
    / "2026"
    / "06"
    / "29"
    / "rollout-2026-06-29T08-41-13-019f121c-5214-7042-a218-4fd204bd333c.jsonl"
)
PASTED_ORIENTATION_ATTACHMENT = (
    USER_HOME
    / ".codex"
    / "attachments"
    / "44cff06e-e7e0-4f48-9e4f-e60d9abd7892"
    / "pasted-text.txt"
)
LEGACY_NOETHER_WORKSPACE = (
    USER_HOME
    / "Documents"
    / "Codex"
    / "2026-06-09"
    / "could-you-look-online-for-me"
    / "work"
    / "noether-slavic-canonical"
)


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


def local_file_evidence(role: str, path: pathlib.Path, thread_id: str | None = None) -> dict:
    item = {
        "role": role,
        "thread_id": thread_id,
        "path": str(path),
        "exists": path.exists(),
        "source_excerpt_copied": False,
        "credentials_or_tokens_copied": False,
    }
    if path.exists() and path.is_file():
        item["bytes"] = path.stat().st_size
        item["sha256"] = sha256(path)
    return item


def local_path_status(label: str, path: pathlib.Path) -> dict:
    return {
        "label": label,
        "path": str(path),
        "exists": path.exists(),
        "is_directory": path.is_dir(),
    }


def build_document(manifest: dict) -> dict:
    source_core = manifest.get("source_core_upload", {})
    archive = source_core.get("archive", {})
    capture_forms = manifest.get("page_context_note_capture_forms", {})
    review_index = manifest.get("local_review_handoff_package_index", {})
    github = manifest.get("github", {})
    artifacts = manifest.get("artifacts", {})

    orientation_sources = [
        local_file_evidence(
            "primary_predecessor_session_log",
            PREDECESSOR_SESSION,
            "019ead97-38c8-7112-9b9c-e8c176d526a1",
        ),
        local_file_evidence(
            "parallel_handoff_prompt_session_log",
            PARALLEL_HANDOFF_SESSION,
            "019f1007-406b-7cc3-a3cf-ac23517cd8a6",
        ),
        local_file_evidence(
            "current_takeover_session_log",
            CURRENT_TAKEOVER_SESSION,
            "019f121c-5214-7042-a218-4fd204bd333c",
        ),
        local_file_evidence(
            "user_pasted_orientation_attachment",
            PASTED_ORIENTATION_ATTACHMENT,
            None,
        ),
    ]

    return {
        "artifact": "previous_session_orientation_and_github_sync_queue",
        "status": "local_orientation_sync_queue_not_remote_update_not_completion_claim",
        "generated_date": "2026-06-30",
        "generated_utc": now_utc(),
        "bandwidth_mode": "local_only_no_network_actions",
        "no_network_actions_performed": True,
        "source_text_copied": False,
        "source_language_terms_copied": False,
        "credentials_or_tokens_copied": False,
        "current_pc_branch": {
            "repo": github.get("repo"),
            "branch": github.get("branch"),
            "base_branch": github.get("base_branch"),
            "draft_pr": github.get("draft_pr"),
            "last_successfully_pushed_head_before_local_only_work": "db7ffc6ca62116d9f8dd8c5ba156e7e2c7c953a2",
            "manifest_head_before_manifest": github.get("head_before_manifest"),
            "sync_status": "local_queue_ready_remote_update_deferred_due_to_bandwidth",
        },
        "local_paths": [
            local_path_status("pc_payload_workspace", BASE),
            local_path_status("legacy_noether_artifact_workspace", LEGACY_NOETHER_WORKSPACE),
        ],
        "previous_session_orientation": {
            "orientation_source_count": len(orientation_sources),
            "orientation_sources": orientation_sources,
            "predecessor_interpretation": (
                "The prior Noether workstream is anchored in the June 9 noether-slavic-canonical "
                "workspace and later June 28/29 session logs. This artifact records pointers and hashes "
                "only; it does not copy prior chat/source passages."
            ),
            "checkpoint_references": [
                {
                    "role": "pasted_checkpoint_named_by_user",
                    "package": "packages/Noether_Slavic_Post44_Papers01_45PlusBibliography_Update_20260628T194100Z.zip",
                    "sha256": "71F4710EE050142B199BE73A897FADD204551AA7737482B6637A295E56C9936D",
                    "status": "superseded_oriented_checkpoint_from_pasted_attachment",
                },
                {
                    "role": "latest_prior_local_slavic_checkpoint_found_in_session_logs",
                    "package": "packages/Noether_Slavic_Post44_Papers01_45PlusBibliography_Update_20260628T203324Z.zip",
                    "sha256": "4F9A629F42C8292BF4CC5FB43E58EBB951EC2A383E01D0812A20E6644E0999C9",
                    "independent_validation": "overall_pass_true_per_prior_session_log_pointer",
                },
                {
                    "role": "latest_prior_local_external_review_bundle_found_in_session_logs",
                    "package": "review_bundles/Noether_Slavic_ExternalReview_RolePackets_SelfContained_20260628T200514Z.zip",
                    "sha256": "A2985DA390620A8982A8BFA526CC9C5CD2EF3FEB63AF9E8E369BFC2F58550799",
                    "independent_validation": "overall_pass_true_per_prior_session_log_pointer",
                },
            ],
        },
        "github_sync_queue": {
            "queue_status": "deferred_no_remote_update_this_turn",
            "deferred_reason": (
                "User reported phone data/rate constraint. Avoid fetch, push, clone, or large uploads "
                "until explicit approval or a suitable network."
            ),
            "payload_artifact_counts": {
                "json": len(artifacts.get("json", [])),
                "markdown": len(artifacts.get("markdown", [])),
                "scripts": len(artifacts.get("scripts", [])),
                "status_manifest_in_addition_to_json_count": True,
                "status_index_in_addition_to_markdown_count": True,
            },
            "sync_items": [
                {
                    "id": "pc_payload_json_markdown_scripts",
                    "status": "local_ready_not_pushed",
                    "json_artifacts_indexed": len(artifacts.get("json", [])),
                    "markdown_artifacts_indexed": len(artifacts.get("markdown", [])),
                    "scripts_indexed": len(artifacts.get("scripts", [])),
                },
                {
                    "id": "source_core_text_tex_workbook_snapshot",
                    "status": source_core.get("status"),
                    "github_upload_status": source_core.get("github_upload_status"),
                    "archive_committed": source_core.get("archive_committed"),
                    "archive_path": archive.get("path"),
                    "archive_sha256": archive.get("sha256"),
                    "archive_bytes": archive.get("bytes"),
                    "contains_pdf_image_or_archive_payloads": archive.get("contains_pdf_image_or_archive_payloads"),
                },
                {
                    "id": "review_packet_capture_and_handoff_scaffolds",
                    "status": "local_scaffolded_not_sendable_not_populated",
                    "blank_capture_forms": capture_forms.get("forms"),
                    "forms_filled": capture_forms.get("forms_filled"),
                    "packet_rows_blocked": capture_forms.get("packet_rows_blocked"),
                    "local_review_handoff_upload_status": review_index.get("upload_status"),
                },
            ],
            "network_actions_allowed_later_only_after_approval": [
                "fetch current PR branch head and compare against db7ffc6ca62116d9f8dd8c5ba156e7e2c7c953a2",
                "push small text/json/md/script payload updates before attempting any archive transfer",
                "use Git LFS or release/Drive/Zenodo handoff for the source-core archive if approved",
                "update draft PR notes with local-only manifest and deferred-source-core status",
            ],
        },
        "boundaries": [
            "This is not a GitHub update and not a remote synchronization claim.",
            "This is not native/external review and not term approval.",
            "This records session and artifact pointers only; no source-language passages are copied.",
            "This records no user credentials, tokens, or secrets.",
            "The active Noether multilingual goal remains open.",
        ],
    }


def write_markdown(document: dict) -> None:
    current = document["current_pc_branch"]
    previous = document["previous_session_orientation"]
    queue = document["github_sync_queue"]
    lines = [
        "# Previous-session orientation and GitHub sync queue - 2026-06-30",
        "",
        "Status: local orientation and deferred sync queue. This is not a GitHub update, not native review, and not a completion claim.",
        "",
        "## Bandwidth Boundary",
        "",
        f"- Mode: `{document['bandwidth_mode']}`",
        f"- Network actions performed: `{str((not document['no_network_actions_performed'])).lower()}`",
        f"- Deferred reason: {queue['deferred_reason']}",
        "",
        "## Current PC Branch",
        "",
        f"- Repository: `{current['repo']}`",
        f"- Branch: `{current['branch']}`",
        f"- Base branch: `{current['base_branch']}`",
        f"- Draft PR: {current['draft_pr']}",
        f"- Last successfully pushed head before local-only work: `{current['last_successfully_pushed_head_before_local_only_work']}`",
        f"- Sync status: `{current['sync_status']}`",
        "",
        "## Orientation Evidence",
        "",
        f"- Orientation sources recorded: {previous['orientation_source_count']}",
    ]
    for source in previous["orientation_sources"]:
        exists = str(source["exists"]).lower()
        size = source.get("bytes", "missing")
        lines.append(f"- `{source['role']}`: exists `{exists}`, bytes `{size}`")
    lines.extend(
        [
            "",
            "## Prior Checkpoint Pointers",
            "",
            "| Role | Package | SHA-256 | Status |",
            "| --- | --- | --- | --- |",
        ]
    )
    for row in previous["checkpoint_references"]:
        status = row.get("status") or row.get("independent_validation") or ""
        lines.append(f"| {row['role']} | `{row['package']}` | `{row['sha256']}` | `{status}` |")
    lines.extend(
        [
            "",
            "## Deferred Sync Queue",
            "",
            f"- JSON artifacts indexed: {queue['payload_artifact_counts']['json']}",
            f"- Markdown artifacts indexed: {queue['payload_artifact_counts']['markdown']}",
            f"- Scripts indexed: {queue['payload_artifact_counts']['scripts']}",
        ]
    )
    for item in queue["sync_items"]:
        lines.append(f"- `{item['id']}`: `{item['status']}`")
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
        "- Previous-session orientation and GitHub sync queue: "
        f"{document['previous_session_orientation']['orientation_source_count']} local orientation sources / "
        f"{len(document['github_sync_queue']['sync_items'])} deferred sync items / "
        "0 network actions"
    )
    text = re.sub(r"- Previous-session orientation and GitHub sync queue: .*", line, text)
    if line not in text:
        marker = "- Local review handoff index:"
        rows = text.splitlines()
        for offset, row in enumerate(rows):
            if row.startswith(marker):
                rows.insert(offset + 1, line)
                text = "\n".join(rows) + "\n"
                break
    text = text.replace(
        "local-handoff metadata, research publication metadata",
        "local-handoff/orientation-sync-queue metadata, research publication metadata",
    )
    if "Generated UTC: " in text:
        old = text.split("Generated UTC: ", 1)[1].splitlines()[0]
        text = text.replace(old, manifest["generated_utc"], 1)
    STATUS_INDEX.write_text(text, encoding="utf-8")


def update_manifest(document: dict) -> None:
    manifest = load_json(STATUS_MANIFEST)
    manifest["generated_utc"] = now_utc()
    manifest["previous_session_orientation_and_github_sync_queue"] = {
        "status": document["status"],
        "artifact_markdown": OUT_MD.name,
        "artifact_json": OUT_JSON.name,
        "orientation_sources": document["previous_session_orientation"]["orientation_source_count"],
        "sync_items": len(document["github_sync_queue"]["sync_items"]),
        "no_network_actions_performed": document["no_network_actions_performed"],
        "github_sync_status": document["github_sync_queue"]["queue_status"],
        "credentials_or_tokens_copied": False,
        "source_text_copied": False,
        "source_language_terms_copied": False,
    }
    upsert_artifact(
        manifest,
        "json",
        OUT_JSON,
        "local_orientation_sync_queue_not_remote_update_not_completion_claim",
    )
    upsert_artifact(manifest, "markdown", OUT_MD)
    upsert_artifact(manifest, "scripts", pathlib.Path(__file__))
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
                "orientation_json": str(OUT_JSON),
                "orientation_sources": document["previous_session_orientation"]["orientation_source_count"],
                "sync_items": len(document["github_sync_queue"]["sync_items"]),
                "no_network_actions_performed": document["no_network_actions_performed"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
