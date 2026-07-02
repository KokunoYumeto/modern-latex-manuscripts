import datetime
import hashlib
import json
import pathlib
import re


BASE = pathlib.Path(__file__).resolve().parents[1]
STATUS_MANIFEST = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_MANIFEST_20260629.json"
STATUS_INDEX = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_INDEX_20260629.md"
SELECTION_MATRIX_JSON = BASE / "LOCAL_SOURCE_WITNESS_SELECTION_MATRIX_20260630.json"
FILESYSTEM_VALIDATION_JSON = BASE / "SELECTED_SOURCE_WITNESS_FILESYSTEM_VALIDATION_20260630.json"
SOURCE_CORE_SNAPSHOT_JSON = BASE / "NOETHER_SOURCE_CORE_TEXT_TEX_WORKBOOKS_SNAPSHOT_20260629.json"
SPLIT_PLAN_JSON = BASE / "SOURCE_CORE_SPLIT_UPLOAD_STAGING_PLAN_20260630.json"
OUT_JSON = BASE / "SELECTED_SOURCE_WITNESS_SOURCE_CORE_COVERAGE_GAP_20260630.json"
OUT_MD = BASE / "SELECTED_SOURCE_WITNESS_SOURCE_CORE_COVERAGE_GAP_20260630.md"
SELF_PATH = pathlib.Path(__file__).resolve()

STATUS = "selected_source_witness_source_core_coverage_gap_no_network_no_archive_created"


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


def matrix_witnesses_by_path(matrix: dict) -> dict[str, list[dict]]:
    rows: dict[str, list[dict]] = {}
    for lane_row in matrix.get("matrix_rows", []):
        for witness in lane_row.get("selected_witnesses", []):
            rows.setdefault(witness["path"], []).append(
                {
                    "lane_or_cohort": lane_row.get("lane_or_cohort"),
                    "source_gate_use": lane_row.get("source_gate_use"),
                    "selected_rank": witness.get("selected_rank"),
                    "source_core_files": int(witness.get("source_core_files") or 0),
                    "source_core_included": bool(witness.get("source_core_included")),
                }
            )
    return rows


def coverage_status(source_core_files: int, text_source_like_files: int) -> str:
    if source_core_files <= 0 and text_source_like_files > 0:
        return "local_only_source_core_gap"
    if source_core_files <= 0:
        return "no_text_source_core_candidate_found"
    if source_core_files >= text_source_like_files:
        return "source_core_text_coverage_complete_or_exceeds_local_text_count"
    return "partial_source_core_text_coverage"


def upload_priority(source_gate_uses: list[str], status: str, text_gap: int) -> str:
    if status == "local_only_source_core_gap":
        if "selected_for_manual_source_review_resolution" in source_gate_uses:
            return "high_delta_candidate_for_manual_review_lane"
        if "selected_for_page_context_note_entry" in source_gate_uses:
            return "high_delta_candidate_for_ready_note_lane"
        return "medium_delta_candidate_for_support_or_discovery"
    if status == "partial_source_core_text_coverage" and text_gap > 100:
        return "medium_partial_delta_candidate"
    if status == "partial_source_core_text_coverage":
        return "low_partial_delta_candidate"
    return "no_delta_needed_for_current_text_core"


def build_shelf_rows(matrix: dict, filesystem: dict) -> list[dict]:
    by_path = matrix_witnesses_by_path(matrix)
    rows = []
    for fs_row in filesystem.get("unique_witness_shelf_rows", []):
        path = fs_row["path"]
        witnesses = by_path.get(path, [])
        source_core_files = max((row.get("source_core_files") or 0 for row in witnesses), default=0)
        text_files = int(fs_row.get("filesystem", {}).get("text_source_like_files") or 0)
        tex_files = int(fs_row.get("filesystem", {}).get("tex_files") or 0)
        pdf_files = int(fs_row.get("filesystem", {}).get("pdf_files") or 0)
        image_files = int(fs_row.get("filesystem", {}).get("image_files") or 0)
        archive_files = int(fs_row.get("filesystem", {}).get("archive_files") or 0)
        text_gap = max(0, text_files - source_core_files)
        status = coverage_status(source_core_files, text_files)
        uses = sorted({row.get("source_gate_use") for row in witnesses})
        rows.append(
            {
                "path": path,
                "batch": fs_row.get("batch"),
                "bucket": fs_row.get("bucket"),
                "lanes_or_cohorts": fs_row.get("lanes_or_cohorts", []),
                "source_gate_uses": uses,
                "selected_slot_count": fs_row.get("selected_slot_count"),
                "path_validation_status": fs_row.get("path_validation_status"),
                "text_source_like_files": text_files,
                "tex_files": tex_files,
                "pdf_files_counted_not_packaged": pdf_files,
                "image_files_counted_not_packaged": image_files,
                "archive_files_counted_not_packaged": archive_files,
                "source_core_files_currently_represented": source_core_files,
                "source_core_text_like_gap_estimate": text_gap,
                "coverage_status": status,
                "delta_upload_priority": upload_priority(uses, status, text_gap),
                "recommended_next_action": (
                    "stage_text_tex_delta_manifest_when_network_or_upload_window_allows"
                    if text_gap > 0
                    else "keep_existing_source_core_reference"
                ),
                "archive_or_binary_upload_recommended_now": False,
                "actual_delta_archive_created": False,
                "actual_remote_upload_performed": False,
                "source_text_copied": False,
                "source_language_terms_copied": False,
            }
        )
    return rows


def build_lane_rows(shelf_rows: list[dict]) -> list[dict]:
    lanes = sorted({lane for row in shelf_rows for lane in row.get("lanes_or_cohorts", [])})
    rows = []
    for lane in lanes:
        lane_shelves = [row for row in shelf_rows if lane in row.get("lanes_or_cohorts", [])]
        text_gap = sum(row["source_core_text_like_gap_estimate"] for row in lane_shelves)
        rows.append(
            {
                "lane_or_cohort": lane,
                "unique_witness_shelves": len(lane_shelves),
                "shelves_with_any_source_core_files": sum(
                    1 for row in lane_shelves if row["source_core_files_currently_represented"] > 0
                ),
                "local_only_gap_shelves": sum(1 for row in lane_shelves if row["coverage_status"] == "local_only_source_core_gap"),
                "partial_coverage_shelves": sum(
                    1 for row in lane_shelves if row["coverage_status"] == "partial_source_core_text_coverage"
                ),
                "text_source_like_files": sum(row["text_source_like_files"] for row in lane_shelves),
                "tex_files": sum(row["tex_files"] for row in lane_shelves),
                "source_core_files_currently_represented": sum(
                    row["source_core_files_currently_represented"] for row in lane_shelves
                ),
                "source_core_text_like_gap_estimate": text_gap,
                "pdf_files_counted_not_packaged": sum(row["pdf_files_counted_not_packaged"] for row in lane_shelves),
                "image_files_counted_not_packaged": sum(row["image_files_counted_not_packaged"] for row in lane_shelves),
                "archive_files_counted_not_packaged": sum(row["archive_files_counted_not_packaged"] for row in lane_shelves),
                "delta_upload_priority": (
                    "high_delta_candidate_for_manual_review_lane"
                    if any(row["delta_upload_priority"] == "high_delta_candidate_for_manual_review_lane" for row in lane_shelves)
                    else "medium_or_low_delta_candidate"
                    if text_gap > 0
                    else "no_delta_needed_for_current_text_core"
                ),
                "archive_or_binary_upload_recommended_now": False,
                "actual_delta_archive_created": False,
                "actual_remote_upload_performed": False,
                "source_text_copied": False,
                "source_language_terms_copied": False,
            }
        )
    return rows


def build_document(manifest: dict) -> dict:
    matrix = load_json(SELECTION_MATRIX_JSON)
    filesystem = load_json(FILESYSTEM_VALIDATION_JSON)
    snapshot = load_json(SOURCE_CORE_SNAPSHOT_JSON)
    split_plan = load_json(SPLIT_PLAN_JSON)
    shelf_rows = build_shelf_rows(matrix, filesystem)
    lane_rows = build_lane_rows(shelf_rows)
    gap_rows = [row for row in shelf_rows if row["source_core_text_like_gap_estimate"] > 0]
    local_only_rows = [row for row in shelf_rows if row["coverage_status"] == "local_only_source_core_gap"]
    partial_rows = [row for row in shelf_rows if row["coverage_status"] == "partial_source_core_text_coverage"]
    return {
        "artifact": "selected_source_witness_source_core_coverage_gap",
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
            "local_source_witness_selection_matrix": SELECTION_MATRIX_JSON.name,
            "selected_source_witness_filesystem_validation": FILESYSTEM_VALIDATION_JSON.name,
            "source_core_snapshot": SOURCE_CORE_SNAPSHOT_JSON.name,
            "source_core_split_upload_plan": SPLIT_PLAN_JSON.name,
            "status_manifest": STATUS_MANIFEST.name,
        },
        "policy": {
            "metadata_only": True,
            "delta_archive_created": False,
            "remote_upload_performed": False,
            "copy_file_names": False,
            "copy_source_passages": False,
            "copy_source_language_terms": False,
            "binary_payloads_recommended_now": False,
            "pdf_image_archive_files_counted_not_packaged": True,
        },
        "source_core_baseline": {
            "included_files": snapshot.get("included_files"),
            "included_bytes_uncompressed": snapshot.get("included_bytes_uncompressed"),
            "planned_chunks": split_plan.get("totals", {}).get("planned_chunks"),
            "uploaded_chunks": split_plan.get("totals", {}).get("uploaded_chunks"),
            "uploaded_bytes": split_plan.get("totals", {}).get("uploaded_bytes"),
        },
        "summary": {
            "selected_unique_witness_shelves": len(shelf_rows),
            "selected_witness_slots": matrix.get("summary", {}).get("selected_witnesses", 0),
            "shelves_with_any_source_core_files": sum(
                1 for row in shelf_rows if row["source_core_files_currently_represented"] > 0
            ),
            "local_only_source_core_gap_shelves": len(local_only_rows),
            "partial_source_core_text_coverage_shelves": len(partial_rows),
            "source_core_text_like_gap_shelves": len(gap_rows),
            "text_source_like_files_unique_shelves": filesystem.get("summary", {}).get(
                "text_source_like_files_counted_unique_shelves", 0
            ),
            "tex_files_unique_shelves": filesystem.get("summary", {}).get("tex_files_counted_unique_shelves", 0),
            "source_core_files_currently_represented_unique_shelves": sum(
                row["source_core_files_currently_represented"] for row in shelf_rows
            ),
            "source_core_text_like_gap_estimate_unique_shelves": sum(
                row["source_core_text_like_gap_estimate"] for row in shelf_rows
            ),
            "pdf_files_counted_not_packaged": filesystem.get("summary", {}).get("pdf_files_counted_unique_shelves", 0),
            "image_files_counted_not_packaged": filesystem.get("summary", {}).get("image_files_counted_unique_shelves", 0),
            "archive_files_counted_not_packaged": filesystem.get("summary", {}).get(
                "archive_files_counted_unique_shelves", 0
            ),
            "high_delta_candidate_shelves": sum(
                1 for row in shelf_rows if row["delta_upload_priority"].startswith("high_delta_candidate")
            ),
            "lane_or_cohort_count": len(lane_rows),
            "actual_delta_archive_created": False,
            "actual_remote_upload_performed": False,
            "inspection_outputs_filled": False,
            "review_packet_population_performed": False,
            "translation_or_revision_performed": False,
            "native_review_status": "not_reviewed",
            "current_approved_terms": 0,
            "current_accepted_corrections": 0,
        },
        "lane_coverage_rows": lane_rows,
        "unique_witness_shelf_coverage_rows": shelf_rows,
        "recommended_commit_or_upload_groups": [
            {
                "id": "selected_witness_text_tex_delta_manifest",
                "status": "planned_not_created_not_uploaded",
                "scope": "text_tex_workbook_only_delta_for_selected_witness_shelves",
                "requires_network": True,
                "performed_now": False,
            },
            {
                "id": "selected_witness_pdf_image_archive_review",
                "status": "deferred_until_specific_review_need",
                "scope": "binary_payloads_counted_only_not_packaged",
                "requires_network": True,
                "performed_now": False,
            },
        ],
        "boundaries": [
            "This artifact is a coverage-gap plan, not a new source-core archive.",
            "No file-name inventory, source-language passage, or source-language term string is copied.",
            "PDF/image/archive payloads are counted only and remain deferred.",
            "No remote upload or GitHub action was performed.",
            "This is not native/external review and not terminology approval.",
        ],
    }


def write_markdown(document: dict) -> None:
    summary = document["summary"]
    lines = [
        "# Selected source-witness source-core coverage gap - 2026-06-30",
        "",
        "Status: metadata-only coverage-gap plan. No archive creation, network action, review, translation, or source-passage copying was performed.",
        "",
        "## Summary",
        "",
        f"- Selected unique witness shelves: {summary['selected_unique_witness_shelves']}",
        f"- Shelves with source-core files: {summary['shelves_with_any_source_core_files']}",
        f"- Local-only source-core gap shelves: {summary['local_only_source_core_gap_shelves']}",
        f"- Partial source-core text coverage shelves: {summary['partial_source_core_text_coverage_shelves']}",
        f"- Text/source-like files in unique selected shelves: {summary['text_source_like_files_unique_shelves']}",
        f"- Source-core files currently represented in selected shelves: {summary['source_core_files_currently_represented_unique_shelves']}",
        f"- Estimated text/source-like gap: {summary['source_core_text_like_gap_estimate_unique_shelves']}",
        f"- PDFs/images/archives counted, not packaged: {summary['pdf_files_counted_not_packaged']} / {summary['image_files_counted_not_packaged']} / {summary['archive_files_counted_not_packaged']}",
        f"- Delta archive created: `{str(summary['actual_delta_archive_created']).lower()}`",
        f"- Remote upload performed: `{str(summary['actual_remote_upload_performed']).lower()}`",
        "",
        "## Lane Coverage",
        "",
        "| Lane/cohort | Shelves | Any source-core | Local-only gaps | Partial | Text/source-like | Source-core files | Gap estimate | Priority |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in document["lane_coverage_rows"]:
        lines.append(
            f"| `{row['lane_or_cohort']}` | {row['unique_witness_shelves']} | {row['shelves_with_any_source_core_files']} | {row['local_only_gap_shelves']} | {row['partial_coverage_shelves']} | {row['text_source_like_files']} | {row['source_core_files_currently_represented']} | {row['source_core_text_like_gap_estimate']} | `{row['delta_upload_priority']}` |"
        )
    lines.extend(["", "## Deferred Groups", ""])
    for group in document["recommended_commit_or_upload_groups"]:
        lines.append(f"- `{group['id']}`: {group['status']} ({group['scope']})")
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
        "- Selected source-witness source-core coverage gap: "
        f"{summary['selected_unique_witness_shelves']} unique shelves / "
        f"{summary['local_only_source_core_gap_shelves']} local-only gaps / "
        f"{summary['source_core_text_like_gap_estimate_unique_shelves']} estimated text-source gap / "
        "0 network actions"
    )
    if re.search(r"^- Selected source-witness source-core coverage gap: .*", text, flags=re.MULTILINE):
        text = re.sub(r"^- Selected source-witness source-core coverage gap: .*", line, text, flags=re.MULTILINE)
    else:
        marker = "- Selected source-witness filesystem validation:"
        rows = text.splitlines()
        for offset, row in enumerate(rows):
            if row.startswith(marker):
                rows.insert(offset + 1, line)
                text = "\n".join(rows) + "\n"
                break
    text = text.replace(
        "local-source-evidence-shelf inventory/source-witness-shortlist/selection-matrix/inspection-packet/filesystem-validation metadata",
        "local-source-evidence-shelf inventory/source-witness-shortlist/selection-matrix/inspection-packet/filesystem-validation/source-core-gap metadata",
    )
    text = text.replace("source-core-gap/source-core-gap metadata", "source-core-gap metadata")
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
    manifest["selected_source_witness_source_core_coverage_gap"] = {
        "status": document["status"],
        "artifact_markdown": OUT_MD.name,
        "artifact_json": OUT_JSON.name,
        "selected_unique_witness_shelves": summary["selected_unique_witness_shelves"],
        "selected_witness_slots": summary["selected_witness_slots"],
        "shelves_with_any_source_core_files": summary["shelves_with_any_source_core_files"],
        "local_only_source_core_gap_shelves": summary["local_only_source_core_gap_shelves"],
        "partial_source_core_text_coverage_shelves": summary["partial_source_core_text_coverage_shelves"],
        "source_core_text_like_gap_shelves": summary["source_core_text_like_gap_shelves"],
        "text_source_like_files_unique_shelves": summary["text_source_like_files_unique_shelves"],
        "tex_files_unique_shelves": summary["tex_files_unique_shelves"],
        "source_core_files_currently_represented_unique_shelves": summary[
            "source_core_files_currently_represented_unique_shelves"
        ],
        "source_core_text_like_gap_estimate_unique_shelves": summary[
            "source_core_text_like_gap_estimate_unique_shelves"
        ],
        "pdf_files_counted_not_packaged": summary["pdf_files_counted_not_packaged"],
        "image_files_counted_not_packaged": summary["image_files_counted_not_packaged"],
        "archive_files_counted_not_packaged": summary["archive_files_counted_not_packaged"],
        "high_delta_candidate_shelves": summary["high_delta_candidate_shelves"],
        "lane_or_cohort_count": summary["lane_or_cohort_count"],
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
                "source_core_coverage_gap_json": str(OUT_JSON),
                "selected_unique_witness_shelves": document["summary"]["selected_unique_witness_shelves"],
                "local_only_source_core_gap_shelves": document["summary"]["local_only_source_core_gap_shelves"],
                "partial_source_core_text_coverage_shelves": document["summary"][
                    "partial_source_core_text_coverage_shelves"
                ],
                "source_core_text_like_gap_estimate_unique_shelves": document["summary"][
                    "source_core_text_like_gap_estimate_unique_shelves"
                ],
                "actual_delta_archive_created": document["summary"]["actual_delta_archive_created"],
                "no_network_actions_performed": document["no_network_actions_performed"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
