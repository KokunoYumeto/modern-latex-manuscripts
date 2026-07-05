import datetime
import hashlib
import json
import pathlib
import re
from collections import Counter, defaultdict


BASE = pathlib.Path(__file__).resolve().parents[1]
STATUS_MANIFEST = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_MANIFEST_20260629.json"
STATUS_INDEX = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_INDEX_20260629.md"
SOURCE_CORE_SNAPSHOT = BASE / "NOETHER_SOURCE_CORE_TEXT_TEX_WORKBOOKS_SNAPSHOT_20260629.json"
OUT_JSON = BASE / "LOCAL_SOURCE_EVIDENCE_SHELF_INVENTORY_20260630.json"
OUT_MD = BASE / "LOCAL_SOURCE_EVIDENCE_SHELF_INVENTORY_20260630.md"
SELF_PATH = pathlib.Path(__file__).resolve()

STATUS = "local_source_evidence_shelf_inventory_no_network_no_source_passage_copy"
NON_SLAVIC_RELATIVE_MARKER = "sources/non_slavic_reference_corpus/"

TEXT_SOURCE_EXTENSIONS = {
    "",
    ".bib",
    ".cfg",
    ".cls",
    ".csv",
    ".css",
    ".doc",
    ".docx",
    ".htm",
    ".html",
    ".json",
    ".ldf",
    ".ltx",
    ".lua",
    ".md",
    ".odf",
    ".ods",
    ".odt",
    ".py",
    ".source",
    ".sty",
    ".tex",
    ".tex~",
    ".tsv",
    ".txt",
    ".wiki",
    ".wikitext",
    ".xml",
    ".yml",
    ".yaml",
}
PDF_EXTENSIONS = {".pdf"}
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".eps", ".emf", ".wdp"}
ARCHIVE_EXTENSIONS = {".zip", ".tar", ".tgz", ".gz", ".epub", ".mobi", ".jar"}

BUCKET_RULES = [
    (
        "french_spanish_romance",
        [
            "french",
            "spanish",
            "romance",
            "south_american",
            "caribbean",
            "pan_romance",
        ],
    ),
    (
        "simplified_chinese_japanese_cjk",
        ["chinese", "japanese", "cjk"],
    ),
    (
        "persian_family_arabic",
        [
            "persian",
            "farsi",
            "dari",
            "tajik",
            "arabic",
            "persianate",
            "pashto",
            "afghan",
            "arabic_script",
        ],
    ),
    (
        "pan_turkic",
        [
            "pan_turkic",
            "central_asian_turkic",
            "turkic",
            "uzbek",
            "turkmen",
            "tatar",
            "kyrgyz",
            "bashkir",
            "uyghur",
        ],
    ),
    (
        "south_asia_hindustani_indic_dravidian",
        ["south_asia", "hindustani", "indic", "dravidian"],
    ),
    (
        "east_southeast_asia_pacific",
        [
            "east_southeast",
            "asia_wide",
            "pacific",
            "malay",
            "indonesian",
            "philippine",
            "tai",
            "hmong",
            "austroasiatic",
            "tibeto",
            "burman",
        ],
    ),
    (
        "africa_deep_gap",
        [
            "africa",
            "african",
            "nilo",
            "sahel",
            "omotic",
            "horn",
            "great_lakes",
            "southern_african",
            "west_african",
        ],
    ),
    (
        "methodology_interlanguage_access",
        [
            "methodology",
            "intercomprehension",
            "interintelligibility",
            "access_gain",
            "optimal_access",
            "auxlang",
            "comparator",
        ],
    ),
    (
        "source_first_reference_textbooks",
        ["open_logic", "aata", "hefferon"],
    ),
]

NAMED_TARGET_COVERAGE = {
    "french": ["french"],
    "spanish": ["spanish"],
    "simplified_chinese": ["chinese"],
    "japanese": ["japanese"],
    "persian_farsi": ["persian", "farsi"],
    "dari": ["dari", "afghan"],
    "tajik": ["tajik"],
    "arabic": ["arabic"],
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


def batch_bucket(name: str) -> str:
    lowered = name.lower()
    for bucket, markers in BUCKET_RULES:
        if any(marker in lowered for marker in markers):
            return bucket
    return "other_adjacent_gap_tracking"


def extension_key(path: pathlib.Path) -> str:
    suffix = path.suffix.lower()
    return suffix if suffix else "<none>"


def counter_to_rows(counter: Counter[str]) -> list[dict]:
    return [{"extension": key, "files": counter[key]} for key in sorted(counter)]


def summarize_directory(path: pathlib.Path) -> dict:
    extension_counts: Counter[str] = Counter()
    total_files = 0
    total_bytes = 0
    text_source_files = 0
    tex_files = 0
    pdf_files = 0
    image_files = 0
    archive_files = 0
    for file_path in path.rglob("*"):
        if not file_path.is_file():
            continue
        ext = file_path.suffix.lower()
        total_files += 1
        try:
            total_bytes += file_path.stat().st_size
        except OSError:
            pass
        extension_counts[extension_key(file_path)] += 1
        if ext in TEXT_SOURCE_EXTENSIONS or not ext:
            text_source_files += 1
        if ext == ".tex":
            tex_files += 1
        if ext in PDF_EXTENSIONS:
            pdf_files += 1
        if ext in IMAGE_EXTENSIONS:
            image_files += 1
        if ext in ARCHIVE_EXTENSIONS:
            archive_files += 1
    return {
        "files": total_files,
        "bytes": total_bytes,
        "text_source_like_files": text_source_files,
        "tex_files": tex_files,
        "pdf_files": pdf_files,
        "image_files": image_files,
        "archive_files": archive_files,
        "extension_counts": counter_to_rows(extension_counts),
    }


def non_slavic_source_core_batch_counts(snapshot: dict) -> dict[str, dict]:
    by_batch: dict[str, dict] = {}
    for item in snapshot.get("files", []):
        rel = item.get("codex_relative_path", "")
        if NON_SLAVIC_RELATIVE_MARKER not in rel:
            continue
        tail = rel.split(NON_SLAVIC_RELATIVE_MARKER, 1)[1]
        batch = tail.split("/", 1)[0]
        if not batch:
            continue
        stats = by_batch.setdefault(batch, {"files": 0, "bytes": 0, "extensions": Counter()})
        stats["files"] += 1
        stats["bytes"] += int(item.get("bytes") or 0)
        stats["extensions"][item.get("extension") or "<none>"] += 1
    return {
        batch: {
            "files": stats["files"],
            "bytes": stats["bytes"],
            "extension_counts": counter_to_rows(stats["extensions"]),
        }
        for batch, stats in by_batch.items()
    }


def named_target_coverage(batch_names: list[str]) -> dict:
    coverage = {}
    lowered = {name: name.lower() for name in batch_names}
    for target, markers in NAMED_TARGET_COVERAGE.items():
        matches = [name for name, low in lowered.items() if any(marker in low for marker in markers)]
        coverage[target] = {
            "status": "local_shelf_present" if matches else "not_found_in_local_batch_names",
            "matching_batches": sorted(matches),
            "batch_count": len(matches),
        }
    return coverage


def build_document(manifest: dict) -> dict:
    snapshot = load_json(SOURCE_CORE_SNAPSHOT)
    legacy_workspace = pathlib.Path(manifest["local_artifact_workspace"])
    corpus_root = legacy_workspace / "sources" / "non_slavic_reference_corpus"
    top_dirs = sorted([path for path in corpus_root.iterdir() if path.is_dir()], key=lambda path: path.name.lower())
    source_core_by_batch = non_slavic_source_core_batch_counts(snapshot)

    batches = []
    bucket_totals: dict[str, dict] = defaultdict(
        lambda: {
            "batches": 0,
            "disk_files": 0,
            "disk_bytes": 0,
            "text_source_like_files": 0,
            "tex_files": 0,
            "pdf_files": 0,
            "image_files": 0,
            "archive_files": 0,
            "source_core_files": 0,
            "source_core_bytes": 0,
        }
    )
    total_ext: Counter[str] = Counter()

    for directory in top_dirs:
        disk = summarize_directory(directory)
        source_core = source_core_by_batch.get(directory.name, {"files": 0, "bytes": 0, "extension_counts": []})
        bucket = batch_bucket(directory.name)
        row = {
            "batch": directory.name,
            "bucket": bucket,
            "path": str(directory),
            "disk_files": disk["files"],
            "disk_bytes": disk["bytes"],
            "text_source_like_files": disk["text_source_like_files"],
            "tex_files": disk["tex_files"],
            "pdf_files": disk["pdf_files"],
            "image_files": disk["image_files"],
            "archive_files": disk["archive_files"],
            "source_core_files": source_core["files"],
            "source_core_bytes": source_core["bytes"],
            "source_core_included": source_core["files"] > 0,
            "status": "local_evidence_shelf_present_not_reviewed",
            "source_text_copied": False,
            "source_language_terms_copied": False,
        }
        batches.append(row)
        totals = bucket_totals[bucket]
        totals["batches"] += 1
        for key in [
            "disk_files",
            "disk_bytes",
            "text_source_like_files",
            "tex_files",
            "pdf_files",
            "image_files",
            "archive_files",
            "source_core_files",
            "source_core_bytes",
        ]:
            totals[key] += row[key]
        for ext in disk["extension_counts"]:
            total_ext[ext["extension"]] += ext["files"]

    bucket_rows = [
        {"bucket": bucket, **dict(values), "status": "local_shelf_bucket_present_not_reviewed"}
        for bucket, values in sorted(bucket_totals.items())
    ]
    disk_totals = {
        "batches": len(batches),
        "files": sum(row["disk_files"] for row in batches),
        "bytes": sum(row["disk_bytes"] for row in batches),
        "text_source_like_files": sum(row["text_source_like_files"] for row in batches),
        "tex_files": sum(row["tex_files"] for row in batches),
        "pdf_files": sum(row["pdf_files"] for row in batches),
        "image_files": sum(row["image_files"] for row in batches),
        "archive_files": sum(row["archive_files"] for row in batches),
        "extension_counts": counter_to_rows(total_ext),
    }
    source_core_totals = {
        "non_slavic_reference_corpus_files": sum(row["source_core_files"] for row in batches),
        "non_slavic_reference_corpus_bytes": sum(row["source_core_bytes"] for row in batches),
        "batches_with_source_core_files": sum(1 for row in batches if row["source_core_files"] > 0),
    }

    return {
        "artifact": "local_source_evidence_shelf_inventory",
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
        "corpus_root": str(corpus_root),
        "source_core_snapshot_json": SOURCE_CORE_SNAPSHOT.name,
        "disk_totals": disk_totals,
        "source_core_totals": source_core_totals,
        "bucket_totals": bucket_rows,
        "named_target_language_coverage": named_target_coverage([row["batch"] for row in batches]),
        "batch_inventory": batches,
        "next_gates": [
            "select lane-specific source witnesses from local shelves before translation or revision",
            "separate source-code/text/workbook witnesses from PDFs and images before GitHub upload",
            "promote only reviewed source witnesses into terminology rationales",
            "record missing or weak lanes as discovery gaps rather than filling them from model memory",
            "keep native/external authority review separate from local mechanical validation",
        ],
        "boundaries": [
            "This inventory is path/count/hash oriented and copies no source passages.",
            "This is not a source download, GitHub update, review result, term approval, or completion claim.",
            "PDF/image/archive counts are inventory signals only; those payloads remain excluded from text-first GitHub handoff unless explicitly approved.",
            "Local corpus presence is not native or community authority.",
            "The active Noether multilingual goal remains open.",
        ],
    }


def write_markdown(document: dict) -> None:
    disk = document["disk_totals"]
    source_core = document["source_core_totals"]
    lines = [
        "# Local source-evidence shelf inventory - 2026-06-30",
        "",
        "Status: local inventory only. No network action was performed, and no source passages are copied.",
        "",
        "## Totals",
        "",
        f"- Corpus batches: {disk['batches']}",
        f"- Disk files under non-Slavic corpus: {disk['files']}",
        f"- Text/source-like files: {disk['text_source_like_files']}",
        f"- TeX files: {disk['tex_files']}",
        f"- PDFs inventoried but not packaged for text handoff: {disk['pdf_files']}",
        f"- Image files inventoried but not packaged for text handoff: {disk['image_files']}",
        f"- Archive files inventoried but not packaged for text handoff: {disk['archive_files']}",
        f"- Source-core included non-Slavic corpus files: {source_core['non_slavic_reference_corpus_files']}",
        f"- Source-core batches with included files: {source_core['batches_with_source_core_files']}",
        f"- Network actions performed: `{str((not document['no_network_actions_performed'])).lower()}`",
        "",
        "## Bucket Totals",
        "",
        "| Bucket | Batches | Disk files | Source-like files | TeX files | PDFs | Source-core files | Status |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in document["bucket_totals"]:
        lines.append(
            "| {bucket} | {batches} | {disk_files} | {text_source_like_files} | {tex_files} | {pdf_files} | {source_core_files} | `{status}` |".format(
                **row
            )
        )
    lines.extend(["", "## Named Target Coverage", "", "| Target | Status | Matching batches |", "| --- | --- | ---: |"])
    for target, row in sorted(document["named_target_language_coverage"].items()):
        lines.append(f"| {target} | `{row['status']}` | {row['batch_count']} |")
    lines.extend(["", "## Next Gates", ""])
    lines.extend(f"- {gate}" for gate in document["next_gates"])
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
    line = (
        "- Local source-evidence shelf inventory: "
        f"{document['disk_totals']['batches']} corpus batches / "
        f"{document['disk_totals']['text_source_like_files']} source-like local files / "
        f"{document['source_core_totals']['non_slavic_reference_corpus_files']} source-core included files / "
        "0 network actions"
    )
    if re.search(r"^- Local source-evidence shelf inventory: .*", text, flags=re.MULTILINE):
        text = re.sub(r"^- Local source-evidence shelf inventory: .*", line, text, flags=re.MULTILINE)
    else:
        marker = "- Source seed entries:"
        rows = text.splitlines()
        for offset, row in enumerate(rows):
            if row.startswith(marker):
                rows.insert(offset + 1, line)
                text = "\n".join(rows) + "\n"
                break
    text = text.replace(
        "source-core archive/staged-upload metadata",
        "source-core archive/staged-upload/local-source-evidence-shelf inventory metadata",
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
    manifest["local_source_evidence_shelf_inventory"] = {
        "status": document["status"],
        "artifact_markdown": OUT_MD.name,
        "artifact_json": OUT_JSON.name,
        "corpus_batches": document["disk_totals"]["batches"],
        "disk_files": document["disk_totals"]["files"],
        "text_source_like_files": document["disk_totals"]["text_source_like_files"],
        "tex_files": document["disk_totals"]["tex_files"],
        "pdf_files_inventoried_not_packaged": document["disk_totals"]["pdf_files"],
        "image_files_inventoried_not_packaged": document["disk_totals"]["image_files"],
        "archive_files_inventoried_not_packaged": document["disk_totals"]["archive_files"],
        "source_core_non_slavic_files": document["source_core_totals"]["non_slavic_reference_corpus_files"],
        "source_core_batches_with_files": document["source_core_totals"]["batches_with_source_core_files"],
        "bucket_count": len(document["bucket_totals"]),
        "target_language_coverage_count": len(document["named_target_language_coverage"]),
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
                "inventory_json": str(OUT_JSON),
                "corpus_batches": document["disk_totals"]["batches"],
                "disk_files": document["disk_totals"]["files"],
                "text_source_like_files": document["disk_totals"]["text_source_like_files"],
                "source_core_non_slavic_files": document["source_core_totals"]["non_slavic_reference_corpus_files"],
                "bucket_count": len(document["bucket_totals"]),
                "no_network_actions_performed": document["no_network_actions_performed"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
