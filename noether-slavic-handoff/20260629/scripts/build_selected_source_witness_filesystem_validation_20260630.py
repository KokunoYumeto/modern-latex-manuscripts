import datetime
import hashlib
import json
import pathlib
import re
from collections import Counter, defaultdict


BASE = pathlib.Path(__file__).resolve().parents[1]
STATUS_MANIFEST = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_MANIFEST_20260629.json"
STATUS_INDEX = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_INDEX_20260629.md"
SELECTION_MATRIX_JSON = BASE / "LOCAL_SOURCE_WITNESS_SELECTION_MATRIX_20260630.json"
INSPECTION_PACKET_JSON = BASE / "SELECTED_SOURCE_WITNESS_INSPECTION_PACKET_20260630.json"
OUT_JSON = BASE / "SELECTED_SOURCE_WITNESS_FILESYSTEM_VALIDATION_20260630.json"
OUT_MD = BASE / "SELECTED_SOURCE_WITNESS_FILESYSTEM_VALIDATION_20260630.md"
SELF_PATH = pathlib.Path(__file__).resolve()

STATUS = "selected_source_witness_filesystem_validation_no_network_no_source_passage_copy"

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
PDF_EXTENSIONS = {".pdf"}
IMAGE_EXTENSIONS = {".bmp", ".gif", ".jpeg", ".jpg", ".png", ".svg", ".tif", ".tiff", ".webp"}
ARCHIVE_EXTENSIONS = {".7z", ".bz2", ".gz", ".rar", ".tar", ".tgz", ".xz", ".zip"}


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


def normalize_extension(path: pathlib.Path) -> str:
    return path.suffix.lower() or "[no-extension]"


def count_files(path: pathlib.Path) -> dict:
    counts = {
        "path_exists": path.exists(),
        "is_directory": path.is_dir(),
        "is_file": path.is_file(),
        "directories_scanned": 0,
        "files": 0,
        "bytes": 0,
        "text_source_like_files": 0,
        "tex_files": 0,
        "pdf_files": 0,
        "image_files": 0,
        "archive_files": 0,
        "other_files": 0,
        "unreadable_entries": 0,
        "extension_counts": {},
    }
    if not path.exists():
        return counts

    extension_counts: Counter[str] = Counter()
    paths_to_scan = [path]
    if path.is_dir():
        try:
            iterator = path.rglob("*")
        except OSError:
            counts["unreadable_entries"] += 1
            iterator = iter(())
        paths_to_scan = list(iterator)
        counts["directories_scanned"] = sum(1 for item in paths_to_scan if item.is_dir())

    for item in paths_to_scan:
        if not item.is_file():
            continue
        try:
            stat = item.stat()
        except OSError:
            counts["unreadable_entries"] += 1
            continue
        ext = normalize_extension(item)
        extension_counts[ext] += 1
        counts["files"] += 1
        counts["bytes"] += stat.st_size
        if ext in TEXT_SOURCE_EXTENSIONS:
            counts["text_source_like_files"] += 1
        if ext in TEX_EXTENSIONS:
            counts["tex_files"] += 1
        if ext in PDF_EXTENSIONS:
            counts["pdf_files"] += 1
        elif ext in IMAGE_EXTENSIONS:
            counts["image_files"] += 1
        elif ext in ARCHIVE_EXTENSIONS:
            counts["archive_files"] += 1
        elif ext not in TEXT_SOURCE_EXTENSIONS:
            counts["other_files"] += 1

    counts["extension_counts"] = dict(sorted(extension_counts.items()))
    return counts


def selected_witness_slots(matrix: dict) -> list[dict]:
    slots = []
    for row in matrix.get("matrix_rows", []):
        for witness in row.get("selected_witnesses", []):
            slots.append(
                {
                    "slot_id": f"{row.get('lane_or_cohort')}::selected-{witness.get('selected_rank')}",
                    "lane_or_cohort": row.get("lane_or_cohort"),
                    "kind": row.get("kind"),
                    "source_gate_use": row.get("source_gate_use"),
                    "selected_rank": witness.get("selected_rank"),
                    "batch": witness.get("batch"),
                    "bucket": witness.get("bucket"),
                    "path": witness.get("path"),
                    "matrix_text_source_like_files": witness.get("text_source_like_files"),
                    "matrix_tex_files": witness.get("tex_files"),
                    "matrix_pdf_files": witness.get("pdf_files"),
                    "matrix_source_core_files": witness.get("source_core_files"),
                    "source_core_included": witness.get("source_core_included"),
                }
            )
    return slots


def task_lane_link_counts(packet: dict) -> dict[str, int]:
    counts: Counter[str] = Counter()
    for group in [
        "ready_context_note_tasks",
        "manual_source_review_tasks",
        "source_discovery_tasks",
        "support_cohort_tasks",
    ]:
        for task in packet.get(group, []):
            lane = task.get("language_lane") or task.get("lane_or_cohort")
            counts[lane] += int(task.get("selected_witness_count") or 0)
    return dict(sorted(counts.items()))


def build_slot_rows(slots: list[dict]) -> list[dict]:
    rows = []
    for slot in slots:
        path = pathlib.Path(slot["path"])
        fs = count_files(path)
        row = dict(slot)
        row.update(
            {
                "filesystem": fs,
                "path_validation_status": (
                    "exists_directory"
                    if fs["path_exists"] and fs["is_directory"]
                    else "exists_file"
                    if fs["path_exists"] and fs["is_file"]
                    else "missing_path"
                ),
                "validated_without_reading_file_contents": True,
                "source_text_copied": False,
                "source_language_terms_copied": False,
            }
        )
        rows.append(row)
    return rows


def build_unique_rows(slot_rows: list[dict]) -> list[dict]:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for row in slot_rows:
        grouped[row["path"]].append(row)

    unique_rows = []
    for path, rows in sorted(grouped.items()):
        fs = rows[0]["filesystem"]
        unique_rows.append(
            {
                "path": path,
                "batch": rows[0].get("batch"),
                "bucket": rows[0].get("bucket"),
                "lanes_or_cohorts": sorted({row["lane_or_cohort"] for row in rows}),
                "source_gate_uses": sorted({row["source_gate_use"] for row in rows}),
                "selected_slot_count": len(rows),
                "path_validation_status": rows[0]["path_validation_status"],
                "filesystem": fs,
                "validated_without_reading_file_contents": True,
                "source_text_copied": False,
                "source_language_terms_copied": False,
            }
        )
    return unique_rows


def build_lane_rows(slot_rows: list[dict], packet: dict) -> list[dict]:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for row in slot_rows:
        grouped[row["lane_or_cohort"]].append(row)
    task_links = task_lane_link_counts(packet)
    lane_rows = []
    for lane, rows in sorted(grouped.items()):
        lane_rows.append(
            {
                "lane_or_cohort": lane,
                "selected_witness_slots": len(rows),
                "unique_witness_shelves": len({row["path"] for row in rows}),
                "paths_existing": sum(1 for row in rows if row["filesystem"]["path_exists"]),
                "missing_paths": sum(1 for row in rows if not row["filesystem"]["path_exists"]),
                "files": sum(row["filesystem"]["files"] for row in rows),
                "text_source_like_files": sum(row["filesystem"]["text_source_like_files"] for row in rows),
                "tex_files": sum(row["filesystem"]["tex_files"] for row in rows),
                "pdf_files": sum(row["filesystem"]["pdf_files"] for row in rows),
                "image_files": sum(row["filesystem"]["image_files"] for row in rows),
                "archive_files": sum(row["filesystem"]["archive_files"] for row in rows),
                "witness_task_links_from_inspection_packet": task_links.get(lane, 0),
                "path_validation_status": "all_paths_exist" if all(row["filesystem"]["path_exists"] for row in rows) else "missing_path",
                "validated_without_reading_file_contents": True,
                "source_text_copied": False,
                "source_language_terms_copied": False,
            }
        )
    return lane_rows


def build_document(manifest: dict) -> dict:
    matrix = load_json(SELECTION_MATRIX_JSON)
    packet = load_json(INSPECTION_PACKET_JSON)
    slots = selected_witness_slots(matrix)
    slot_rows = build_slot_rows(slots)
    unique_rows = build_unique_rows(slot_rows)
    lane_rows = build_lane_rows(slot_rows, packet)
    slot_paths_existing = sum(1 for row in slot_rows if row["filesystem"]["path_exists"])
    unique_paths_existing = sum(1 for row in unique_rows if row["filesystem"]["path_exists"])
    return {
        "artifact": "selected_source_witness_filesystem_validation",
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
            "selected_source_witness_inspection_packet": INSPECTION_PACKET_JSON.name,
            "status_manifest": STATUS_MANIFEST.name,
        },
        "validation_policy": {
            "metadata_only": True,
            "read_file_contents": False,
            "copy_file_names": False,
            "copy_source_passages": False,
            "copy_source_language_terms": False,
            "network_access_used": False,
            "registers_native_review": False,
            "fills_review_outputs": False,
        },
        "summary": {
            "selected_witness_slots": len(slot_rows),
            "slot_paths_existing": slot_paths_existing,
            "slot_missing_paths": len(slot_rows) - slot_paths_existing,
            "unique_witness_shelves": len(unique_rows),
            "unique_paths_existing": unique_paths_existing,
            "unique_missing_paths": len(unique_rows) - unique_paths_existing,
            "lane_or_cohort_count": len(lane_rows),
            "files_counted_across_slots": sum(row["filesystem"]["files"] for row in slot_rows),
            "text_source_like_files_counted_across_slots": sum(row["filesystem"]["text_source_like_files"] for row in slot_rows),
            "tex_files_counted_across_slots": sum(row["filesystem"]["tex_files"] for row in slot_rows),
            "pdf_files_counted_across_slots": sum(row["filesystem"]["pdf_files"] for row in slot_rows),
            "image_files_counted_across_slots": sum(row["filesystem"]["image_files"] for row in slot_rows),
            "archive_files_counted_across_slots": sum(row["filesystem"]["archive_files"] for row in slot_rows),
            "files_counted_unique_shelves": sum(row["filesystem"]["files"] for row in unique_rows),
            "text_source_like_files_counted_unique_shelves": sum(row["filesystem"]["text_source_like_files"] for row in unique_rows),
            "tex_files_counted_unique_shelves": sum(row["filesystem"]["tex_files"] for row in unique_rows),
            "pdf_files_counted_unique_shelves": sum(row["filesystem"]["pdf_files"] for row in unique_rows),
            "image_files_counted_unique_shelves": sum(row["filesystem"]["image_files"] for row in unique_rows),
            "archive_files_counted_unique_shelves": sum(row["filesystem"]["archive_files"] for row in unique_rows),
            "witness_task_links_from_inspection_packet": packet.get("summary", {}).get("witness_task_links", 0),
            "inspection_outputs_filled": False,
            "review_packet_population_performed": False,
            "translation_or_revision_performed": False,
            "native_review_status": "not_reviewed",
            "current_approved_terms": 0,
            "current_accepted_corrections": 0,
        },
        "lane_validation_rows": lane_rows,
        "selected_witness_slot_rows": slot_rows,
        "unique_witness_shelf_rows": unique_rows,
        "boundaries": [
            "This validation checks filesystem metadata only and does not read source file contents.",
            "No source-language passages, source-language term strings, or file-name inventories are copied.",
            "PDF/image/archive files are counted only, not packaged.",
            "This is not native/external review and not canonical terminology approval.",
            "No network action was performed.",
        ],
    }


def write_markdown(document: dict) -> None:
    summary = document["summary"]
    lines = [
        "# Selected source-witness filesystem validation - 2026-06-30",
        "",
        "Status: metadata-only filesystem validation. No network action, review, translation, or source-passage copying was performed.",
        "",
        "## Summary",
        "",
        f"- Selected witness slots: {summary['selected_witness_slots']}",
        f"- Slot paths existing/missing: {summary['slot_paths_existing']} / {summary['slot_missing_paths']}",
        f"- Unique witness shelves: {summary['unique_witness_shelves']}",
        f"- Unique paths existing/missing: {summary['unique_paths_existing']} / {summary['unique_missing_paths']}",
        f"- Lane/cohort rows: {summary['lane_or_cohort_count']}",
        f"- Unique-shelf files counted: {summary['files_counted_unique_shelves']}",
        f"- Unique-shelf TeX files counted: {summary['tex_files_counted_unique_shelves']}",
        f"- Unique-shelf text/source-like files counted: {summary['text_source_like_files_counted_unique_shelves']}",
        f"- Unique-shelf PDFs counted/not packaged: {summary['pdf_files_counted_unique_shelves']}",
        f"- Network actions performed: `{str((not document['no_network_actions_performed'])).lower()}`",
        "",
        "## Lane Validation",
        "",
        "| Lane/cohort | Slots | Existing | Missing | Files | TeX | Text/source-like | PDFs | Task links |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in document["lane_validation_rows"]:
        lines.append(
            f"| `{row['lane_or_cohort']}` | {row['selected_witness_slots']} | {row['paths_existing']} | {row['missing_paths']} | {row['files']} | {row['tex_files']} | {row['text_source_like_files']} | {row['pdf_files']} | {row['witness_task_links_from_inspection_packet']} |"
        )
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
        "- Selected source-witness filesystem validation: "
        f"{summary['selected_witness_slots']} selected witness slots / "
        f"{summary['unique_witness_shelves']} unique shelves / "
        f"{summary['slot_missing_paths']} missing slot paths / "
        "0 network actions"
    )
    if re.search(r"^- Selected source-witness filesystem validation: .*", text, flags=re.MULTILINE):
        text = re.sub(r"^- Selected source-witness filesystem validation: .*", line, text, flags=re.MULTILINE)
    else:
        marker = "- Selected source-witness inspection packet:"
        rows = text.splitlines()
        for offset, row in enumerate(rows):
            if row.startswith(marker):
                rows.insert(offset + 1, line)
                text = "\n".join(rows) + "\n"
                break
    text = text.replace(
        "local-source-evidence-shelf inventory/source-witness-shortlist/selection-matrix/inspection-packet metadata",
        "local-source-evidence-shelf inventory/source-witness-shortlist/selection-matrix/inspection-packet/filesystem-validation metadata",
    )
    text = text.replace(
        "filesystem-validation/filesystem-validation metadata",
        "filesystem-validation metadata",
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
    manifest["selected_source_witness_filesystem_validation"] = {
        "status": document["status"],
        "artifact_markdown": OUT_MD.name,
        "artifact_json": OUT_JSON.name,
        "selected_witness_slots": summary["selected_witness_slots"],
        "slot_paths_existing": summary["slot_paths_existing"],
        "slot_missing_paths": summary["slot_missing_paths"],
        "unique_witness_shelves": summary["unique_witness_shelves"],
        "unique_paths_existing": summary["unique_paths_existing"],
        "unique_missing_paths": summary["unique_missing_paths"],
        "lane_or_cohort_count": summary["lane_or_cohort_count"],
        "files_counted_across_slots": summary["files_counted_across_slots"],
        "text_source_like_files_counted_across_slots": summary["text_source_like_files_counted_across_slots"],
        "tex_files_counted_across_slots": summary["tex_files_counted_across_slots"],
        "pdf_files_counted_across_slots": summary["pdf_files_counted_across_slots"],
        "image_files_counted_across_slots": summary["image_files_counted_across_slots"],
        "archive_files_counted_across_slots": summary["archive_files_counted_across_slots"],
        "files_counted_unique_shelves": summary["files_counted_unique_shelves"],
        "text_source_like_files_counted_unique_shelves": summary["text_source_like_files_counted_unique_shelves"],
        "tex_files_counted_unique_shelves": summary["tex_files_counted_unique_shelves"],
        "pdf_files_counted_unique_shelves": summary["pdf_files_counted_unique_shelves"],
        "image_files_counted_unique_shelves": summary["image_files_counted_unique_shelves"],
        "archive_files_counted_unique_shelves": summary["archive_files_counted_unique_shelves"],
        "witness_task_links_from_inspection_packet": summary["witness_task_links_from_inspection_packet"],
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
                "filesystem_validation_json": str(OUT_JSON),
                "selected_witness_slots": document["summary"]["selected_witness_slots"],
                "slot_missing_paths": document["summary"]["slot_missing_paths"],
                "unique_witness_shelves": document["summary"]["unique_witness_shelves"],
                "unique_missing_paths": document["summary"]["unique_missing_paths"],
                "files_counted_unique_shelves": document["summary"]["files_counted_unique_shelves"],
                "tex_files_counted_unique_shelves": document["summary"]["tex_files_counted_unique_shelves"],
                "no_network_actions_performed": document["no_network_actions_performed"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
