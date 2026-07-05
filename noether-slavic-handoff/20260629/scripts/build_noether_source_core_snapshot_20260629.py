import csv
import datetime as dt
import hashlib
import json
import pathlib
import shutil
import zipfile


BASE = pathlib.Path(__file__).resolve().parents[1]
CODEX_ROOT = pathlib.Path(r"C:\Users\memo_\Documents\Codex")

SNAPSHOT_STEM = "NOETHER_SOURCE_CORE_TEXT_TEX_WORKBOOKS_SNAPSHOT_20260629"
POLICY_STEM = "NOETHER_SOURCE_CORE_UPLOAD_POLICY_20260629"
ARCHIVE = BASE / f"{SNAPSHOT_STEM}.zip"
SNAPSHOT_JSON = BASE / f"{SNAPSHOT_STEM}.json"
SNAPSHOT_MD = BASE / f"{SNAPSHOT_STEM}.md"
POLICY_JSON = BASE / f"{POLICY_STEM}.json"
POLICY_MD = BASE / f"{POLICY_STEM}.md"
STATUS_MANIFEST = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_MANIFEST_20260629.json"
STATUS_INDEX = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_INDEX_20260629.md"

MAX_FILE_BYTES = 5 * 1024 * 1024
MAX_ARCHIVE_BYTES = 95 * 1024 * 1024

ROOTS = [
    {
        "label": "slavic_canonical_workspace",
        "path": CODEX_ROOT / "2026-06-09" / "could-you-look-online-for-me" / "work" / "noether-slavic-canonical",
        "purpose": "completed/review-ready Slavic lane, source-core workbooks, logs, manifests, TeX, and non-Slavic continuation work",
    },
    {
        "label": "modern_latex_noether_sources",
        "path": CODEX_ROOT
        / "2026-06-09"
        / "could-you-look-online-for-me"
        / "work"
        / "modern-latex-manuscripts-20260609-174659"
        / "sources"
        / "noether",
        "purpose": "offline LaTeX source tree used by earlier Noether sessions",
    },
    {
        "label": "noether_zenodo_record_pointers",
        "path": CODEX_ROOT
        / "2026-06-09"
        / "could-you-look-online-for-me"
        / "work"
        / "zenodo-records-wget"
        / "20520501_20520501_noether-linked-multilingual",
        "purpose": "Zenodo record metadata, urls, logs, and source-package pointers; existing zip/PDF payloads are indexed but not reuploaded here",
    },
    {
        "label": "translation_working_tree",
        "path": CODEX_ROOT / "2026-06-09" / "could-you-look-online-for-me" / "translations",
        "purpose": "session translation working files",
    },
    {
        "label": "pc_handoff_payload",
        "path": BASE,
        "purpose": "current PC branch handoff payload, manifests, queue artifacts, and scripts",
    },
]

INCLUDE_EXTENSIONS = {
    ".tex",
    ".bib",
    ".sty",
    ".cls",
    ".md",
    ".txt",
    ".csv",
    ".tsv",
    ".json",
    ".yaml",
    ".yml",
    ".xlsx",
    ".ods",
    ".ipynb",
    ".py",
    ".ps1",
    ".diff",
}

EXCLUDED_EXTENSIONS = {
    ".pdf",
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".tif",
    ".tiff",
    ".bmp",
    ".webp",
    ".zip",
    ".7z",
    ".rar",
    ".tar",
    ".gz",
    ".xz",
    ".bz2",
    ".log",
    ".aux",
    ".toc",
    ".out",
    ".synctex",
}

EXCLUDED_PARTS = {
    ".git",
    "__pycache__",
    "node_modules",
    "source-cache",
    "reader-pdfs",
    "combined_pdfs",
    "source_scan_slices",
    "source_scans_for_checking",
    "source_scans",
    "source-scans",
    "scans",
    "images",
    "fig",
    "figs",
    "figures",
    "tmp",
    "python-vendor",
    "extracted_text",
    "txt_20260629",
}

EXCLUDED_NAME_MARKERS = {
    "pdftotext",
    ".pdf.txt",
}


def now_utc() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat()


def sha256(path: pathlib.Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def rel_to_codex(path: pathlib.Path) -> str:
    try:
        return path.resolve().relative_to(CODEX_ROOT.resolve()).as_posix()
    except ValueError:
        return path.resolve().as_posix()


def ascii_safe(value: str) -> str:
    return value.encode("ascii", "backslashreplace").decode("ascii")


def is_excluded_path(path: pathlib.Path) -> tuple[bool, str | None]:
    parts = {part.lower() for part in path.parts}
    for part in sorted(EXCLUDED_PARTS):
        if part.lower() in parts:
            return True, f"excluded_path_part:{part}"
    lower_name = path.name.lower()
    for marker in EXCLUDED_NAME_MARKERS:
        if marker in lower_name:
            return True, f"excluded_name_marker:{marker}"
    ext = path.suffix.lower()
    if ext in EXCLUDED_EXTENSIONS:
        return True, f"excluded_extension:{ext}"
    if ext not in INCLUDE_EXTENSIONS:
        return True, f"not_source_core_extension:{ext or '[none]'}"
    try:
        size = path.stat().st_size
    except OSError:
        return True, "stat_error"
    if size > MAX_FILE_BYTES:
        return True, f"oversize_gt_{MAX_FILE_BYTES}"
    return False, None


def archive_name(root_label: str, root: pathlib.Path, path: pathlib.Path) -> str:
    rel = path.resolve().relative_to(root.resolve()).as_posix()
    return f"{root_label}/{rel}"


def collect() -> tuple[list[dict], list[dict], dict[str, int]]:
    included: list[dict] = []
    excluded: list[dict] = []
    seen_hashes: dict[str, str] = {}
    counters: dict[str, int] = {}

    for root_info in ROOTS:
        root = root_info["path"]
        label = root_info["label"]
        if not root.exists():
            excluded.append(
                {
                    "root_label": label,
                    "codex_relative_path": rel_to_codex(root),
                    "reason": "root_missing",
                    "bytes": None,
                }
            )
            counters["root_missing"] = counters.get("root_missing", 0) + 1
            continue
        for path in root.rglob("*"):
            if not path.is_file():
                continue
            excluded_flag, reason = is_excluded_path(path)
            size = path.stat().st_size
            if excluded_flag:
                excluded.append(
                    {
                        "root_label": label,
                        "codex_relative_path": rel_to_codex(path),
                        "reason": reason,
                        "bytes": size,
                    }
                )
                counters[reason or "excluded"] = counters.get(reason or "excluded", 0) + 1
                continue
            file_hash = sha256(path)
            archive_path = archive_name(label, root, path)
            if file_hash in seen_hashes:
                excluded.append(
                    {
                        "root_label": label,
                        "codex_relative_path": rel_to_codex(path),
                        "reason": "duplicate_content_sha256",
                        "duplicate_of_archive_path": seen_hashes[file_hash],
                        "bytes": size,
                    }
                )
                counters["duplicate_content_sha256"] = counters.get("duplicate_content_sha256", 0) + 1
                continue
            seen_hashes[file_hash] = archive_path
            included.append(
                {
                    "root_label": label,
                    "codex_relative_path": rel_to_codex(path),
                    "archive_path": archive_path,
                    "sha256": file_hash,
                    "bytes": size,
                    "extension": path.suffix.lower() or "[none]",
                }
            )
    return included, excluded, counters


def write_archive(included: list[dict]) -> None:
    if ARCHIVE.exists():
        ARCHIVE.unlink()
    by_archive = sorted(included, key=lambda item: item["archive_path"].lower())
    with zipfile.ZipFile(ARCHIVE, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for item in by_archive:
            source = CODEX_ROOT / item["codex_relative_path"]
            zf.write(source, item["archive_path"])
        zf.writestr(
            "README_SOURCE_CORE_SNAPSHOT.txt",
            "\n".join(
                [
                    "Noether source-core text/TeX/workbook snapshot - 2026-06-29",
                    "",
                    "This archive intentionally excludes PDFs, images, existing archive blobs, LaTeX build logs,",
                    "source scan slices, OCR/PDF text extraction dumps, source-cache PDFs, and vendor caches.",
                    "It is a compact GitHub handoff snapshot, not a Zenodo replacement and not a native review result.",
                    "",
                ]
            ),
        )
    if ARCHIVE.stat().st_size > MAX_ARCHIVE_BYTES:
        raise SystemExit(
            f"archive too large for this GitHub handoff policy: {ARCHIVE.stat().st_size} > {MAX_ARCHIVE_BYTES}"
        )


def summarize_by(items: list[dict], key: str) -> list[dict]:
    summary: dict[str, dict] = {}
    for item in items:
        value = item.get(key) or "[none]"
        bucket = summary.setdefault(value, {"key": value, "count": 0, "bytes": 0})
        bucket["count"] += 1
        bucket["bytes"] += item.get("bytes") or 0
    return sorted(summary.values(), key=lambda item: item["key"])


def write_policy() -> dict:
    policy = {
        "artifact": "noether_source_core_upload_policy",
        "status": "source_core_policy_for_github_handoff_not_completion_claim",
        "generated_date": "2026-06-29",
        "generated_utc": now_utc(),
        "purpose": "Codify the PC branch policy for uploading small rebuild/audit source files while deferring PDFs, images, large archives, and caches.",
        "include_extensions": sorted(INCLUDE_EXTENSIONS),
        "excluded_extensions": sorted(EXCLUDED_EXTENSIONS),
        "excluded_path_parts": sorted(EXCLUDED_PARTS),
        "excluded_name_markers": sorted(EXCLUDED_NAME_MARKERS),
        "max_file_bytes": MAX_FILE_BYTES,
        "max_archive_bytes": MAX_ARCHIVE_BYTES,
        "upload_rule": "Commit compact text/TeX/workbook/script/manifests to GitHub; keep large PDFs/images/source-cache blobs out unless explicitly needed and separately justified.",
        "daily_budget_note": "Respect the user's 20 GB/day practical transfer constraint; avoid large image/PDF batches unless important.",
        "source_text_boundary": "Do not bundle native-register PDF extraction dumps or long source passages in this GitHub handoff snapshot.",
    }
    POLICY_JSON.write_text(json.dumps(policy, ensure_ascii=True, indent=2) + "\n", encoding="utf-8")
    md = [
        "# Noether source-core upload policy - 2026-06-29",
        "",
        "This policy records the PC-branch rule for GitHub handoff of reusable source-core material.",
        "",
        "## Include",
        "",
        "- TeX/BibTeX/style/class files",
        "- Markdown, text notes, CSV/TSV, JSON/YAML manifests",
        "- small workbooks (`.xlsx`, `.ods`)",
        "- local scripts used to rebuild or audit source-core artifacts",
        "",
        "## Exclude By Default",
        "",
        "- PDFs, images, scans, and existing archive blobs",
        "- LaTeX build logs and transient build products",
        "- source-cache PDFs and OCR/PDF text extraction dumps",
        "- vendor caches and dependency directories",
        "- files larger than 5 MiB in this GitHub snapshot lane",
        "",
        "## Boundary",
        "",
        "This source-core snapshot is not a native review result, not a replacement for Zenodo releases, and not a license clearance decision. It is a compact GitHub handoff layer for rebuildable text/TeX/workbook sources.",
        "",
    ]
    POLICY_MD.write_text("\n".join(md), encoding="utf-8")
    return policy


def write_snapshot_manifest(included: list[dict], excluded: list[dict], counters: dict[str, int], policy: dict) -> None:
    archive_hash = sha256(ARCHIVE)
    archive_entries = []
    with zipfile.ZipFile(ARCHIVE, "r") as zf:
        for name in zf.namelist():
            archive_entries.append(name)
    forbidden_in_archive = [
        name
        for name in archive_entries
        if pathlib.Path(name).suffix.lower() in {".pdf", ".png", ".jpg", ".jpeg", ".gif", ".tif", ".tiff", ".zip"}
    ]
    if forbidden_in_archive:
        raise SystemExit("forbidden archive entries: " + ", ".join(forbidden_in_archive[:20]))

    manifest = {
        "artifact": "noether_source_core_text_tex_workbooks_snapshot",
        "status": "source_core_snapshot_built_locally_upload_deferred_not_pdf_release_not_completion_claim",
        "generated_date": "2026-06-29",
        "generated_utc": now_utc(),
        "github_upload_status": "deferred_due_to_bandwidth",
        "archive_committed": False,
        "upload_deferred_reason": "User reported phone data/rate constraint; avoid large GitHub uploads until explicit approval or a suitable network.",
        "archive": {
            "path": f"noether-slavic-handoff/20260629/{ARCHIVE.name}",
            "sha256": archive_hash,
            "bytes": ARCHIVE.stat().st_size,
            "entries": len(archive_entries),
            "contains_pdf_image_or_archive_payloads": False,
        },
        "policy_artifact_json": POLICY_JSON.name,
        "policy_artifact_markdown": POLICY_MD.name,
        "roots": [
            {
                "label": root["label"],
                "codex_relative_path": rel_to_codex(root["path"]),
                "purpose": root["purpose"],
                "exists": root["path"].exists(),
            }
            for root in ROOTS
        ],
        "included_files": len(included),
        "included_bytes_uncompressed": sum(item["bytes"] for item in included),
        "included_by_extension": summarize_by(included, "extension"),
        "included_by_root": summarize_by(included, "root_label"),
        "excluded_files": len(excluded),
        "excluded_reason_counts": [
            {"reason": key, "count": value} for key, value in sorted(counters.items(), key=lambda item: item[0])
        ],
        "duplicate_content_files_deferred": counters.get("duplicate_content_sha256", 0),
        "max_file_bytes": policy["max_file_bytes"],
        "source_text_boundary": policy["source_text_boundary"],
        "files": included,
    }
    SNAPSHOT_JSON.write_text(json.dumps(manifest, ensure_ascii=True, indent=2) + "\n", encoding="utf-8")

    md = [
        "# Noether source-core text/TeX/workbook snapshot - 2026-06-29",
        "",
        "This artifact records a compact source-core snapshot built locally for later GitHub handoff. GitHub upload is deferred due to the user's phone data/rate constraint. It deliberately excludes PDFs, images, existing archive blobs, source-cache PDFs, OCR/PDF text extraction dumps, vendor caches, and transient build products.",
        "",
        f"- Archive: `{ARCHIVE.name}`",
        f"- Archive SHA-256: `{archive_hash}`",
        f"- Archive bytes: {ARCHIVE.stat().st_size}",
        f"- Included files: {len(included)}",
        f"- Included uncompressed bytes: {sum(item['bytes'] for item in included)}",
        f"- Excluded/deferred files: {len(excluded)}",
        f"- Duplicate-content files deferred: {counters.get('duplicate_content_sha256', 0)}",
        "- Contains PDFs/images/archive payloads: false",
        "- GitHub upload status: deferred due to bandwidth; archive remains local until explicit approval or a suitable network.",
        "- Archive committed: false",
        "",
        "## Included By Extension",
        "",
        "| Extension | Files | Bytes |",
        "| --- | ---: | ---: |",
    ]
    for row in summarize_by(included, "extension"):
        md.append(f"| `{ascii_safe(row['key'])}` | {row['count']} | {row['bytes']} |")
    md.extend(["", "## Included By Root", "", "| Root label | Files | Bytes |", "| --- | ---: | ---: |"])
    for row in summarize_by(included, "root_label"):
        md.append(f"| `{ascii_safe(row['key'])}` | {row['count']} | {row['bytes']} |")
    md.extend(["", "## Boundaries", "", "- This is not a native review result.", "- This is not a Zenodo replacement.", "- This is not a license clearance decision.", "- Long native-register source passages and PDF-extraction dumps are not bundled here.", ""])
    SNAPSHOT_MD.write_text("\n".join(md), encoding="utf-8")


def json_artifact_item(path: pathlib.Path, template: dict | None = None) -> dict:
    item = {key: None for key in (template or {}).keys()}
    item.update(
        {
            "path": f"noether-slavic-handoff/20260629/{path.name}",
            "sha256": sha256(path),
            "bytes": path.stat().st_size,
        }
    )
    data = json.loads(path.read_text(encoding="utf-8"))
    item["artifact"] = data.get("artifact")
    item["status"] = data.get("status")
    for key in [
        "entries",
        "sources_analyzed",
        "aggregate_term_hits",
        "sources",
        "project_sources",
        "ethics_open_sources",
        "authority_matrix",
        "scholarly_and_policy_anchors",
        "review_authority_checklists",
        "decision_framework",
        "lane_templates",
        "review_return_schema",
        "case_study_lanes",
        "method_sections",
        "article_outline",
        "term_record_types",
        "decision_states",
        "lane_rules",
        "required_term_ledger_fields",
        "correction_states",
        "issue_types",
        "required_fields",
        "correction_records",
        "lane_summaries",
        "common_columns",
        "population_rules",
        "reserved_ranges",
        "total_reserved_term_ids",
        "draft_rows",
        "rows",
        "inspection_tasks",
        "tasks",
        "tasks_inspected",
        "inspection_records",
        "current_completed_inspections",
        "source_text_copied",
        "source_language_terms_copied",
        "current_approved_terms",
        "current_accepted_corrections",
        "total_term_anchor_rows",
        "total_pages_analyzed_for_term_anchors",
        "total",
        "accessible",
        "inaccessible",
        "included_files",
        "excluded_files",
        "duplicate_content_files_deferred",
    ]:
        if key in data:
            value = data[key]
            item[key] = len(value) if isinstance(value, (list, dict)) else value
    return item


def markdown_artifact_item(path: pathlib.Path) -> dict:
    return {
        "path": f"noether-slavic-handoff/20260629/{path.name}",
        "sha256": sha256(path),
        "bytes": path.stat().st_size,
    }


def refresh_existing_artifacts(manifest: dict) -> None:
    for group in ["json", "markdown", "scripts"]:
        for item in manifest["artifacts"][group]:
            rel = item["path"].split("20260629/", 1)[-1]
            path = BASE / rel
            if path.exists():
                item["sha256"] = sha256(path)
                item["bytes"] = path.stat().st_size


def update_status_manifest_and_index() -> None:
    manifest = json.loads(STATUS_MANIFEST.read_text(encoding="utf-8"))
    refresh_existing_artifacts(manifest)
    json_template = manifest["artifacts"]["json"][0] if manifest["artifacts"]["json"] else {}

    json_by_path = {item["path"]: item for item in manifest["artifacts"]["json"]}
    for path in [POLICY_JSON, SNAPSHOT_JSON]:
        json_by_path[f"noether-slavic-handoff/20260629/{path.name}"] = json_artifact_item(path, json_template)
    manifest["artifacts"]["json"] = [json_by_path[key] for key in sorted(json_by_path)]

    md_by_path = {item["path"]: item for item in manifest["artifacts"]["markdown"]}
    for path in [POLICY_MD, SNAPSHOT_MD]:
        md_by_path[f"noether-slavic-handoff/20260629/{path.name}"] = markdown_artifact_item(path)
    manifest["artifacts"]["markdown"] = [md_by_path[key] for key in sorted(md_by_path)]

    script_rel = f"noether-slavic-handoff/20260629/scripts/{pathlib.Path(__file__).name}"
    scripts_by_path = {item["path"]: item for item in manifest["artifacts"]["scripts"]}
    scripts_by_path[script_rel] = {
        "path": script_rel,
        "sha256": sha256(pathlib.Path(__file__)),
        "bytes": pathlib.Path(__file__).stat().st_size,
    }
    manifest["artifacts"]["scripts"] = [scripts_by_path[key] for key in sorted(scripts_by_path)]

    snapshot = json.loads(SNAPSHOT_JSON.read_text(encoding="utf-8"))
    manifest["source_core_upload"] = {
        "status": "source_core_text_tex_workbook_snapshot_built_locally_upload_deferred_due_to_bandwidth",
        "github_upload_status": "deferred_due_to_bandwidth",
        "archive_committed": False,
        "upload_deferred_reason": "User reported phone data/rate constraint; avoid large GitHub uploads until explicit approval or a suitable network.",
        "policy_markdown": POLICY_MD.name,
        "policy_json": POLICY_JSON.name,
        "snapshot_markdown": SNAPSHOT_MD.name,
        "snapshot_json": SNAPSHOT_JSON.name,
        "archive": snapshot["archive"],
        "included_files": snapshot["included_files"],
        "included_bytes_uncompressed": snapshot["included_bytes_uncompressed"],
        "excluded_files": snapshot["excluded_files"],
        "duplicate_content_files_deferred": snapshot["duplicate_content_files_deferred"],
        "source_text_boundary": snapshot["source_text_boundary"],
    }
    manifest["generated_utc"] = now_utc()
    STATUS_MANIFEST.write_text(json.dumps(manifest, ensure_ascii=True, indent=2) + "\n", encoding="utf-8")

    index_text = STATUS_INDEX.read_text(encoding="utf-8")
    source_section = "\n".join(
        [
            "## Source-Core Snapshot",
            "",
            f"- Archive: `{ARCHIVE.name}`",
            f"- Archive bytes: {ARCHIVE.stat().st_size}",
            f"- Included files: {snapshot['included_files']}",
            f"- Included uncompressed bytes: {snapshot['included_bytes_uncompressed']}",
            f"- Excluded/deferred files: {snapshot['excluded_files']}",
            f"- Duplicate-content files deferred: {snapshot['duplicate_content_files_deferred']}",
            "- PDFs/images/existing archive payloads bundled: false",
            "- GitHub upload status: deferred due to bandwidth; archive remains local until explicit approval or a suitable network.",
            "- Archive committed: false",
            "- Purpose: local compact source-core snapshot of TeX/text/workbook material from Noether sessions for later GitHub handoff.",
            "",
        ]
    )
    if "## Source-Core Snapshot" not in index_text:
        index_text = index_text.replace("## Boundaries\n", source_section + "## Boundaries\n")
    index_text = index_text.replace(
        "Term ID registry seeded: 8 ranges, 153 reserved IDs, 0 approved terms, 0 accepted corrections",
        "Term ID registry seeded: 8 ranges, 153 reserved IDs, 0 approved terms, 0 accepted corrections",
    )
    index_text = index_text.replace(
        "See `NOETHER_PC_MULTILINGUAL_STATUS_MANIFEST_20260629.json` for artifact hashes",
        "See `NOETHER_PC_MULTILINGUAL_STATUS_MANIFEST_20260629.json` for source-core archive metadata, artifact hashes",
    )
    index_text = index_text.replace(
        index_text.split("Generated UTC: ", 1)[1].splitlines()[0],
        manifest["generated_utc"],
    )
    STATUS_INDEX.write_text(index_text, encoding="utf-8")


def main() -> None:
    policy = write_policy()
    included, excluded, counters = collect()
    if not included:
        raise SystemExit("no source-core files selected")
    write_archive(included)
    write_snapshot_manifest(included, excluded, counters, policy)
    update_status_manifest_and_index()
    print(
        json.dumps(
            {
                "archive": str(ARCHIVE),
                "archive_bytes": ARCHIVE.stat().st_size,
                "included_files": len(included),
                "included_bytes_uncompressed": sum(item["bytes"] for item in included),
                "excluded_files": len(excluded),
                "snapshot_json": str(SNAPSHOT_JSON),
                "policy_json": str(POLICY_JSON),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
