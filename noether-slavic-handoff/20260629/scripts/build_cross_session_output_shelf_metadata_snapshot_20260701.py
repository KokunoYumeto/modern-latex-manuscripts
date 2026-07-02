"""Build a metadata-only snapshot of the cross-session output shelf.

The snapshot records local filenames, hashes, sizes, extensions, timestamps,
and broad workstream categories. It deliberately does not copy file bodies,
source prose, source excerpts, source-language terms, credentials, or binary
payloads into this branch.
"""

from __future__ import annotations

import datetime
import hashlib
import json
import pathlib
import re
from collections import Counter


BASE = pathlib.Path(__file__).resolve().parents[1]
STATUS_MANIFEST = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_MANIFEST_20260629.json"
STATUS_INDEX = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_INDEX_20260629.md"
OUTPUT_ROOT = pathlib.Path(r"C:\Users\memo_\Documents\Codex\2026-06-29\files-mentioned-by-the-user-worked\outputs")
OUT_JSON = BASE / "CROSS_SESSION_OUTPUT_SHELF_METADATA_SNAPSHOT_20260701.json"
OUT_MD = BASE / "CROSS_SESSION_OUTPUT_SHELF_METADATA_SNAPSHOT_20260701.md"
SELF_PATH = pathlib.Path(__file__).resolve()

STATUS = "cross_session_output_shelf_metadata_snapshot_no_body_copy_not_canonical"


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


def category_for(relative_path: str) -> str:
    name = pathlib.PurePosixPath(relative_path).name.upper()
    rel = relative_path.upper()
    if rel.startswith("SOURCE_CACHE/"):
        return "source_cache_metadata_pointer"
    if "SEMI_CONSTRUCTED_RELATION_FUNCTION" in name or "RELATION_FUNCTION" in name:
        return "semi_constructed_relation_function_support"
    if name.startswith("MALAY_INDONESIAN"):
        return "malay_indonesian_support"
    if name.startswith("PAN_ROMANCE"):
        return "pan_romance_support"
    if name.startswith("PAN_TURKIC"):
        return "pan_turkic_support"
    if "ARABIC" in name or "PERSIANATE" in name:
        return "arabic_persianate_support"
    if name.startswith("OLP_") or "OLP_FIRST_PROOF" in name:
        return "open_logic_proof_literacy_support"
    if name.startswith("OPEN_MATH") or name.startswith("OPEN_TRANSLATION") or name.startswith("OPENINTRO"):
        return "open_math_translation_candidate_support"
    if name.startswith("UC"):
        return "undercoverage_world_language_support"
    if name.startswith("WORLD_FAMILY") or name.startswith("INHERITED_WORLD_FAMILY") or name.startswith("UNDERCOVERAGE"):
        return "world_family_methodology_support"
    if "CROSS_SESSION" in name or "COORDINATION" in name:
        return "cross_session_coordination_support"
    return "other_support_output"


def storage_class(extension: str) -> str:
    if extension in {".pdf", ".png", ".jpg", ".jpeg", ".gif", ".webp", ".zip", ".docx"}:
        return "large_or_binary_external_pointer_only"
    if extension in {".json", ".md", ".txt", ".csv", ".sha256", ".yml", ".qmd", ".html", ".ptx"}:
        return "text_or_metadata_external_pointer_only"
    return "external_pointer_only"


def build_document() -> dict:
    file_rows = []
    for path in sorted([row for row in OUTPUT_ROOT.rglob("*") if row.is_file()], key=lambda row: row.relative_to(OUTPUT_ROOT).as_posix().lower()):
        relative_path = path.relative_to(OUTPUT_ROOT).as_posix()
        extension = path.suffix.lower() or "<none>"
        stat = path.stat()
        file_rows.append(
            {
                "relative_path": relative_path,
                "extension": extension,
                "bytes": stat.st_size,
                "sha256": sha256_path(path),
                "mtime_utc": datetime.datetime.fromtimestamp(stat.st_mtime, datetime.timezone.utc).isoformat(timespec="seconds"),
                "workstream_category": category_for(relative_path),
                "storage_class": storage_class(extension),
                "file_body_copied": False,
                "source_text_copied": False,
                "source_language_terms_copied": False,
                "credentials_or_tokens_copied": False,
            }
        )

    extension_counts = Counter(row["extension"] for row in file_rows)
    extension_bytes = Counter()
    category_counts = Counter(row["workstream_category"] for row in file_rows)
    category_bytes = Counter()
    storage_counts = Counter(row["storage_class"] for row in file_rows)
    for row in file_rows:
        extension_bytes[row["extension"]] += row["bytes"]
        category_bytes[row["workstream_category"]] += row["bytes"]
        storage_counts[row["storage_class"]] += 0

    source_cache_files = sum(1 for row in file_rows if row["relative_path"].startswith("source_cache/"))
    binary_extensions = {".pdf", ".png", ".jpg", ".jpeg", ".gif", ".webp", ".zip", ".docx"}
    binary_files = sum(1 for row in file_rows if row["extension"] in binary_extensions)

    return {
        "artifact": "cross_session_output_shelf_metadata_snapshot",
        "status": STATUS,
        "generated_date": "2026-07-01",
        "generated_utc": now_utc(),
        "output_root": str(OUTPUT_ROOT),
        "output_root_exists": OUTPUT_ROOT.exists() and OUTPUT_ROOT.is_dir(),
        "snapshot_policy": {
            "metadata_only": True,
            "build_time_hash_snapshot": True,
            "file_bodies_copied": False,
            "source_text_copied": False,
            "source_language_terms_copied": False,
            "credentials_or_tokens_copied": False,
            "binary_payloads_copied": False,
            "network_actions_performed": 0,
            "canonical_rows_resolved": 0,
            "reviewer_packet_rows_populated": 0,
            "terms_confirmed": 0,
            "translations_created": 0,
            "publication_readiness_claim": False,
            "constructed_surface_readiness_claim": False,
            "pilot_readiness_claim": False,
        },
        "totals": {
            "files_indexed": len(file_rows),
            "bytes_indexed": sum(row["bytes"] for row in file_rows),
            "hash_rows": len(file_rows),
            "source_cache_files": source_cache_files,
            "binary_or_heavy_external_pointer_files": binary_files,
            "file_bodies_copied": 0,
            "source_text_copied": 0,
            "source_language_terms_copied": 0,
            "credentials_or_tokens_copied": 0,
            "network_actions": 0,
        },
        "extension_summary": [
            {"extension": key, "files": extension_counts[key], "bytes": extension_bytes[key]}
            for key in sorted(extension_counts)
        ],
        "category_summary": [
            {"category": key, "files": category_counts[key], "bytes": category_bytes[key]}
            for key in sorted(category_counts)
        ],
        "storage_class_summary": [
            {
                "storage_class": key,
                "files": sum(1 for row in file_rows if row["storage_class"] == key),
                "bytes": sum(row["bytes"] for row in file_rows if row["storage_class"] == key),
            }
            for key in sorted(set(row["storage_class"] for row in file_rows))
        ],
        "file_rows": file_rows,
    }


def write_markdown(document: dict) -> None:
    totals = document["totals"]
    extension_rows = "\n".join(
        f"| `{row['extension']}` | {row['files']} | {row['bytes']} |" for row in document["extension_summary"]
    )
    category_rows = "\n".join(
        f"| `{row['category']}` | {row['files']} | {row['bytes']} |" for row in document["category_summary"]
    )
    storage_rows = "\n".join(
        f"| `{row['storage_class']}` | {row['files']} | {row['bytes']} |" for row in document["storage_class_summary"]
    )
    lines = [
        "# Cross-session output shelf metadata snapshot - 2026-07-01",
        "",
        "Status: metadata-only build-time hash snapshot. This artifact does not copy output file bodies, source prose, source excerpts, source-language terms, credentials, tokens, PDFs, images, archives, or document payloads into the Noether branch.",
        "",
        "## Scope",
        "",
        f"- Output root: `{document['output_root']}`",
        f"- Files indexed: {totals['files_indexed']}",
        f"- Bytes indexed by metadata/hash: {totals['bytes_indexed']}",
        f"- Source-cache files indexed as external pointers: {totals['source_cache_files']}",
        f"- Binary/heavy files indexed as external pointers: {totals['binary_or_heavy_external_pointer_files']}",
        "- File bodies copied: 0",
        "- Source text copied: 0",
        "- Source-language terms copied: 0",
        "- Credentials/tokens copied: 0",
        "- Network actions: 0",
        "",
        "## Extension Summary",
        "",
        "| Extension | Files | Bytes |",
        "| --- | ---: | ---: |",
        extension_rows,
        "",
        "## Category Summary",
        "",
        "| Category | Files | Bytes |",
        "| --- | ---: | ---: |",
        category_rows,
        "",
        "## Storage Summary",
        "",
        "| Storage class | Files | Bytes |",
        "| --- | ---: | ---: |",
        storage_rows,
        "",
        "## Boundaries",
        "",
        "- This is not a canonical-edition update.",
        "- This is not native/external review.",
        "- This is not reviewer packet population.",
        "- This is not term approval.",
        "- This is not translation or revision.",
        "- This is not publication, pilot, or constructed-surface readiness.",
        "- Large and binary external outputs remain outside this branch payload unless a later explicit handoff policy selects them.",
        "",
    ]
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
        "- Cross-session output shelf metadata snapshot: "
        f"{document['totals']['files_indexed']} files / "
        f"{document['totals']['binary_or_heavy_external_pointer_files']} binary-heavy pointers / "
        "0 file bodies copied"
    )
    if re.search(r"^- Cross-session output shelf metadata snapshot: .*", text, flags=re.MULTILINE):
        text = re.sub(r"^- Cross-session output shelf metadata snapshot: .*", line, text, flags=re.MULTILINE)
    else:
        rows = text.splitlines()
        inserted = False
        for offset, row in enumerate(rows):
            if row.startswith("- Semi-constructed relation/function reviewer sheet intake:"):
                rows.insert(offset + 1, line)
                text = "\n".join(rows) + "\n"
                inserted = True
                break
        if not inserted:
            text = text.rstrip() + "\n" + line + "\n"
    if "cross-session-output-shelf-metadata-snapshot" not in text:
        text = text.replace(
            "semi-constructed-relation-function-reviewer-sheet-intake/render-script-preflight",
            "semi-constructed-relation-function-reviewer-sheet-intake/cross-session-output-shelf-metadata-snapshot/render-script-preflight",
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
    totals = document["totals"]
    manifest["cross_session_output_shelf_metadata_snapshot"] = {
        "status": document["status"],
        "artifact_markdown": OUT_MD.name,
        "artifact_json": OUT_JSON.name,
        "output_root": document["output_root"],
        "files_indexed": totals["files_indexed"],
        "bytes_indexed": totals["bytes_indexed"],
        "hash_rows": totals["hash_rows"],
        "source_cache_files": totals["source_cache_files"],
        "binary_or_heavy_external_pointer_files": totals["binary_or_heavy_external_pointer_files"],
        "extension_buckets": len(document["extension_summary"]),
        "category_buckets": len(document["category_summary"]),
        "file_bodies_copied": 0,
        "source_text_copied": False,
        "source_language_terms_copied": False,
        "credentials_or_tokens_copied": False,
        "no_network_actions_performed": True,
        "canonical_rows_resolved": 0,
        "reviewer_packet_rows_populated": 0,
        "terms_confirmed": 0,
        "translations_created": 0,
        "publication_readiness_claim": False,
        "constructed_surface_readiness_claim": False,
        "pilot_readiness_claim": False,
    }
    update_status_index(document, manifest)
    write_json(STATUS_MANIFEST, manifest)


def main() -> None:
    document = build_document()
    write_json(OUT_JSON, document)
    write_markdown(document)
    update_manifest(document)
    print(
        json.dumps(
            {
                "snapshot_json": str(OUT_JSON),
                "files_indexed": document["totals"]["files_indexed"],
                "bytes_indexed": document["totals"]["bytes_indexed"],
                "binary_or_heavy_external_pointer_files": document["totals"]["binary_or_heavy_external_pointer_files"],
                "file_bodies_copied": 0,
                "network_actions": 0,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
