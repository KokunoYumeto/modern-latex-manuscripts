import datetime
import hashlib
import json
import pathlib
import re


BASE = pathlib.Path(__file__).resolve().parents[1]
STATUS_MANIFEST = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_MANIFEST_20260629.json"
STATUS_INDEX = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_INDEX_20260629.md"
SCAFFOLDS_JSON = BASE / "REVIEW_PACKET_SCAFFOLDS_20260629.json"
WORKLIST_JSON = BASE / "PAGE_CONTEXT_NOTE_WORKLIST_20260629.json"
READINESS_JSON = BASE / "PAGE_INSPECTION_REVIEW_PACKET_READINESS_20260629.json"
OUT_JSON = BASE / "LOCAL_REVIEW_HANDOFF_PACKAGE_INDEX_20260630.json"
OUT_MD = BASE / "LOCAL_REVIEW_HANDOFF_PACKAGE_INDEX_20260630.md"


LANE_ARTIFACT_POINTERS = {
    "simplified_chinese": [
        "CHINESE_SOURCE_EVIDENCE_REINFORCEMENT_20260629.json",
        "CHINESE_SOURCE_EVIDENCE_REINFORCEMENT_20260629.md",
        "SIMPLIFIED_CHINESE_TERM_ANCHOR_SEED_20260629.json",
        "SIMPLIFIED_CHINESE_GLOSSARY_RATIONALE_SEED_20260629.md",
        "SIMPLIFIED_CHINESE_PAPER34_SECTION18_PC_CHECKPOINT_20260629.md",
    ],
    "french": [
        "NON_SLAVIC_SOURCE_EVIDENCE_SEED_20260629.json",
        "NON_SLAVIC_SOURCE_EVIDENCE_VALIDATION_SUMMARY_20260629.md",
        "ROMANCE_FRENCH_SPANISH_TERM_ANCHOR_SEED_20260629.json",
        "ROMANCE_FRENCH_SPANISH_GLOSSARY_RATIONALE_SEED_20260629.md",
    ],
    "spanish": [
        "NON_SLAVIC_SOURCE_EVIDENCE_SEED_20260629.json",
        "NON_SLAVIC_SOURCE_EVIDENCE_VALIDATION_SUMMARY_20260629.md",
        "ROMANCE_FRENCH_SPANISH_TERM_ANCHOR_SEED_20260629.json",
        "ROMANCE_FRENCH_SPANISH_GLOSSARY_RATIONALE_SEED_20260629.md",
    ],
    "japanese": [
        "NON_SLAVIC_SOURCE_EVIDENCE_SEED_20260629.json",
        "JAPANESE_TERM_ANCHOR_SEED_20260629.json",
        "JAPANESE_GLOSSARY_RATIONALE_SEED_20260629.md",
    ],
    "fa_IR": [
        "PERSIAN_FAMILY_ARABIC_TERM_ANCHOR_SEED_20260629.json",
        "PERSIAN_FAMILY_ARABIC_GLOSSARY_RATIONALE_SEED_20260629.md",
        "PERSIAN_FAMILY_DARI_TAJIK_REGISTER_GAP_20260629.md",
    ],
    "prs_AF": [
        "PERSIAN_FAMILY_ARABIC_TERM_ANCHOR_SEED_20260629.json",
        "PERSIAN_FAMILY_ARABIC_GLOSSARY_RATIONALE_SEED_20260629.md",
        "PERSIAN_FAMILY_DARI_TAJIK_REGISTER_GAP_20260629.md",
    ],
    "arabic": [
        "ARABIC_SOURCE_EVIDENCE_REINFORCEMENT_20260629.json",
        "ARABIC_SOURCE_EVIDENCE_REINFORCEMENT_20260629.md",
        "PERSIAN_FAMILY_ARABIC_TERM_ANCHOR_SEED_20260629.json",
        "PERSIAN_FAMILY_ARABIC_GLOSSARY_RATIONALE_SEED_20260629.md",
    ],
}

COMMON_REVIEW_ARTIFACTS = [
    "PAGE_INSPECTION_QUEUE_20260629.json",
    "PAGE_INSPECTION_REVIEW_PACKET_READINESS_20260629.json",
    "PAGE_CONTEXT_NOTE_WORKLIST_20260629.json",
    "REVIEW_PACKET_SCAFFOLDS_20260629.json",
    "MULTILINGUAL_REVIEW_PACKET_TEMPLATES_20260629.json",
    "REVIEWER_FACING_GLOSSARY_TABLE_TEMPLATES_20260629.json",
    "ACCEPTED_CORRECTION_LEDGER_TEMPLATE_20260629.json",
    "TERM_ID_REGISTRY_SEED_20260629.json",
]


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
    old_status = by_path.get(rel, {}).get("status")
    by_path[rel] = artifact_item(path, status or old_status)
    manifest["artifacts"][group] = [by_path[key] for key in sorted(by_path)]


def artifact_status(name: str) -> dict:
    path = BASE / name
    return {
        "artifact": name,
        "exists": path.exists(),
        "bytes": path.stat().st_size if path.exists() else None,
        "sha256": sha256(path) if path.exists() else None,
    }


def lane_packages(scaffolds: dict) -> list[dict]:
    packages = []
    for lane in scaffolds["lane_scaffolds"]:
        lane_name = lane["lane"]
        lane_artifacts = LANE_ARTIFACT_POINTERS.get(lane_name, [])
        blockers = ["page_context_notes_not_filled"]
        if lane["manual_or_source_review_items"]:
            blockers.append("manual_or_source_review_rows_unresolved")
        packages.append(
            {
                "lane": lane_name,
                "status": "local_handoff_indexed_not_sendable",
                "packet_template_key": lane["packet_template_key"],
                "work_items": lane["work_items"],
                "ready_row_note_items": lane["ready_row_note_items"],
                "manual_or_source_review_items": lane["manual_or_source_review_items"],
                "packet_rows_populated": lane["packet_rows_populated"],
                "packet_rows_blocked_until_notes": lane["packet_rows_blocked_until_notes"],
                "required_reviewer_roles": lane["required_reviewer_roles"],
                "lane_artifacts": [artifact_status(name) for name in lane_artifacts],
                "common_review_artifacts": [artifact_status(name) for name in COMMON_REVIEW_ARTIFACTS],
                "handoff_blockers": blockers,
                "next_action": (
                    "fill_context_notes_then_populate_reviewer_packet"
                    if not lane["manual_or_source_review_items"]
                    else "resolve_manual_source_review_rows_then_fill_context_notes"
                ),
            }
        )
    return packages


def build_index() -> dict:
    manifest = load_json(STATUS_MANIFEST)
    scaffolds = load_json(SCAFFOLDS_JSON)
    worklist = load_json(WORKLIST_JSON)
    readiness = load_json(READINESS_JSON)
    packages = lane_packages(scaffolds)
    return {
        "artifact": "local_review_handoff_package_index",
        "status": "local_review_handoff_index_not_uploaded_not_sendable",
        "generated_date": "2026-06-30",
        "generated_utc": now_utc(),
        "no_network_actions_performed": True,
        "credentials_or_tokens_copied": False,
        "source_text_copied": False,
        "source_language_terms_copied": False,
        "branch": manifest["github"]["branch"],
        "draft_pr": manifest["github"]["draft_pr"],
        "last_successfully_pushed_head_before_local_only_work": "db7ffc6ca62116d9f8dd8c5ba156e7e2c7c953a2",
        "source_core_upload_status": manifest["source_core_upload"]["status"],
        "source_core_archive_committed": manifest["source_core_upload"]["archive_committed"],
        "bandwidth_boundary": "No GitHub upload/push in this local handoff pass; source-core archive remains local until explicit approval or suitable network.",
        "inputs": {
            "manifest": STATUS_MANIFEST.name,
            "readiness": READINESS_JSON.name,
            "context_note_worklist": WORKLIST_JSON.name,
            "review_packet_scaffolds": SCAFFOLDS_JSON.name,
        },
        "totals": {
            "lane_packages": len(packages),
            "work_items": worklist["totals"]["work_items"],
            "ready_after_extraction_check": readiness["totals"]["ready_after_extraction_check"],
            "manual_or_source_review_required": readiness["totals"]["manual_or_source_review_required"],
            "packet_rows_populated": scaffolds["totals"]["packet_rows_populated"],
            "packet_rows_blocked_until_notes": scaffolds["totals"]["packet_rows_blocked_until_notes"],
            "current_approved_terms": 0,
            "current_accepted_corrections": 0,
        },
        "lane_packages": packages,
        "global_artifact_pointers": {
            "slavic_lane_pointer": "PC_BRANCH_MAINTENANCE_20260629.md",
            "source_core_policy": "NOETHER_SOURCE_CORE_UPLOAD_POLICY_20260629.md",
            "source_core_snapshot": "NOETHER_SOURCE_CORE_TEXT_TEX_WORKBOOKS_SNAPSHOT_20260629.md",
            "interlanguage_method_lane": "INTERLANGUAGE_CONSTRUCTED_LANGUAGE_METHOD_LANE_20260629.md",
            "interlanguage_authority_matrix": "INTERLANGUAGE_METHOD_BIBLIOGRAPHY_AUTHORITY_MATRIX_20260629.md",
            "ai_register_publication_outline": "AI_TECHNICAL_REGISTER_PUBLICATION_OUTLINE_20260629.md",
        },
        "not_sendable_reasons": [
            "page_context_notes_not_filled",
            "manual_or_source_review_rows_unresolved",
            "native_external_review_not_started",
            "accepted_correction_ledger_empty",
            "github_upload_deferred_due_to_bandwidth",
        ],
    }


def write_markdown(index: dict) -> None:
    lines = [
        "# Local review handoff package index - 2026-06-30",
        "",
        "This artifact indexes the local, not-yet-sendable reviewer handoff package. It is not a release, not a populated reviewer packet, and not a GitHub upload record.",
        "",
        f"Companion machine-readable file: `{OUT_JSON.name}`",
        "",
        "## Totals",
        "",
        f"- Lane packages: {index['totals']['lane_packages']}",
        f"- Work items: {index['totals']['work_items']}",
        f"- Ready after extraction check: {index['totals']['ready_after_extraction_check']}",
        f"- Manual/source review required: {index['totals']['manual_or_source_review_required']}",
        f"- Packet rows populated: {index['totals']['packet_rows_populated']}",
        f"- Packet rows blocked until notes: {index['totals']['packet_rows_blocked_until_notes']}",
        f"- Source-core upload status: {index['source_core_upload_status']}",
        f"- Source-core archive committed: {index['source_core_archive_committed']}",
        "",
        "## Lane Packages",
        "",
        "| Lane | Work items | Ready-note items | Manual/source items | Populated rows | Blocked rows | Reviewer roles | Status |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for lane in index["lane_packages"]:
        lines.append(
            f"| {lane['lane']} | {lane['work_items']} | {lane['ready_row_note_items']} | "
            f"{lane['manual_or_source_review_items']} | {lane['packet_rows_populated']} | "
            f"{lane['packet_rows_blocked_until_notes']} | {len(lane['required_reviewer_roles'])} | "
            f"{lane['status']} |"
        )
    lines.extend(
        [
            "",
            "## Blockers",
            "",
        ]
    )
    for reason in index["not_sendable_reasons"]:
        lines.append(f"- {reason}")
    lines.extend(
        [
            "",
            "## Global Pointers",
            "",
        ]
    )
    for key, value in index["global_artifact_pointers"].items():
        lines.append(f"- {key}: `{value}`")
    lines.extend(
        [
            "",
            "## Boundaries",
            "",
            "- No source-language term strings or source passages are copied here.",
            "- No credentials or tokens are copied here.",
            "- No network action, GitHub upload, or push is performed here.",
            "- This index does not populate reviewer packet rows.",
            "- This index does not imply native/external review or term approval.",
            "- GitHub upload remains deferred due to bandwidth.",
            "",
        ]
    )
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def update_status_index(index: dict, manifest: dict) -> None:
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
        f"- Local review handoff index: {index['totals']['lane_packages']} lane packages / "
        f"{index['totals']['packet_rows_blocked_until_notes']} blocked rows / upload deferred"
    )
    text = re.sub(r"- Local review handoff index: .*", line, text)
    if line not in text:
        marker = "- Review-packet scaffolds:"
        rows = text.splitlines()
        for offset, row in enumerate(rows):
            if row.startswith(marker):
                rows.insert(offset + 1, line)
                text = "\n".join(rows) + "\n"
                break
    text = text.replace(
        "page inspection queue/batch/readiness/context-note/reviewer-scaffold metadata",
        "page inspection queue/batch/readiness/context-note/reviewer-scaffold/local-handoff metadata",
    )
    if "Generated UTC: " in text:
        old = text.split("Generated UTC: ", 1)[1].splitlines()[0]
        text = text.replace(old, manifest["generated_utc"], 1)
    STATUS_INDEX.write_text(text, encoding="utf-8")


def update_manifest(index: dict) -> None:
    manifest = load_json(STATUS_MANIFEST)
    manifest["generated_utc"] = now_utc()
    manifest["local_review_handoff_package_index"] = {
        "status": index["status"],
        "artifact_markdown": OUT_MD.name,
        "artifact_json": OUT_JSON.name,
        "lane_packages": index["totals"]["lane_packages"],
        "packet_rows_populated": index["totals"]["packet_rows_populated"],
        "packet_rows_blocked_until_notes": index["totals"]["packet_rows_blocked_until_notes"],
        "upload_status": "deferred_due_to_bandwidth",
        "no_network_actions_performed": True,
        "credentials_or_tokens_copied": False,
        "source_text_copied": False,
        "source_language_terms_copied": False,
        "native_review_status": "not_reviewed",
        "current_approved_terms": 0,
        "current_accepted_corrections": 0,
    }
    upsert_artifact(manifest, "json", OUT_JSON, "local_review_handoff_index_not_uploaded_not_sendable")
    upsert_artifact(manifest, "markdown", OUT_MD)
    upsert_artifact(manifest, "scripts", pathlib.Path(__file__))
    update_status_index(index, manifest)
    write_json(STATUS_MANIFEST, manifest)


def main() -> None:
    index = build_index()
    write_json(OUT_JSON, index)
    write_markdown(index)
    update_manifest(index)
    print(
        json.dumps(
            {
                "handoff_index_json": str(OUT_JSON),
                "lane_packages": index["totals"]["lane_packages"],
                "blocked_rows": index["totals"]["packet_rows_blocked_until_notes"],
                "upload_status": "deferred_due_to_bandwidth",
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
