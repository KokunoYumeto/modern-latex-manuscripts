#!/usr/bin/env python3
"""Package the Kimi 7 continuation drop as a non-scan web-session delta."""

from __future__ import annotations

import csv
import hashlib
import json
import re
import shutil
import zipfile
from collections import Counter
from datetime import datetime
from io import BytesIO
from pathlib import Path


SOURCE_ZIP = (
    Path.home()
    / "Documents"
    / "Papors"
    / "Chatnotes"
    / "CHat translates and clean"
    / "Kimi"
    / "kimi 7"
    / "Kimi_Agent_Continue LaTeX Typesetting Work.zip"
)
BASELINE_MANIFESTS = [
    Path.home()
    / "Downloads"
    / "KIMI7_NONSCAN_REFINED_FOR_WEB_CURRENT"
    / "kimi7_nonscan_selected_manifest.csv"
]
OUT = Path.home() / "Downloads" / "KIMI7_CONTINUE_NONSCAN_DELTA_FOR_WEB_CURRENT"
CHUNKS = OUT / "WEB_UPLOAD_CHUNKS"

MAX_CHUNK_BYTES = 500_000_000
TARGET_UNCOMPRESSED_BYTES = 380_000_000

IMAGE_EXT = {
    ".png",
    ".jpg",
    ".jpeg",
    ".tif",
    ".tiff",
    ".webp",
    ".jp2",
    ".j2k",
    ".bmp",
    ".gif",
    ".pgm",
}
TEXTLIKE_EXT = {
    ".tex",
    ".txt",
    ".md",
    ".json",
    ".csv",
    ".py",
    ".sty",
    ".cls",
    ".bib",
    ".html",
    ".htm",
    ".log",
    ".aux",
    ".out",
    ".toc",
    ".cfg",
    ".def",
    ".yml",
    ".yaml",
    ".xml",
    ".rst",
    ".bak",
    ".backup",
}
KNOWN_PLACEHOLDER_PDFS = {
    "test_math.pdf",
    "test_ytotech.pdf",
    "lie_vol3_pages_801_872.pdf",
    "blank_pages_257_258.pdf",
}


def now_iso() -> str:
    return datetime.now().isoformat(timespec="seconds")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load_baseline_hashes() -> set[str]:
    hashes: set[str] = set()
    for manifest in BASELINE_MANIFESTS:
        if not manifest.exists():
            continue
        with manifest.open("r", encoding="utf-8-sig", newline="") as handle:
            for row in csv.DictReader(handle):
                digest = (row.get("sha256") or "").strip().lower()
                if digest:
                    hashes.add(digest)
    return hashes


def source_slug(path: Path) -> str:
    stem = path.stem.lower()
    stem = re.sub(r"[^a-z0-9]+", "_", stem)
    return re.sub(r"_+", "_", stem).strip("_")


def is_scanlike_pdf_path(name: str) -> bool:
    lower = name.lower()
    base = Path(lower).name
    if base in KNOWN_PLACEHOLDER_PDFS:
        return True
    if any(token in lower for token in ["reference_scan", "ocr_reference", "facsimile"]):
        return True
    if re.search(r"(^|/)(scan|page|image|mod_page)[-_0-9]", lower):
        return True
    if any(
        token in lower
        for token in [
            "/scans/",
            "/scan/",
            "/images/",
            "/page_images/",
            "/ocr_images/",
            "/pdf_pages/",
            "/render_checks/",
            "/renders/",
        ]
    ):
        return True
    return False


def should_select_member(name: str) -> tuple[bool, str]:
    path = Path(name)
    ext = path.suffix.lower()
    base = path.name.lower()

    if ext in IMAGE_EXT:
        return False, "excluded_image_or_scan"
    if ext == ".pdf":
        if is_scanlike_pdf_path(name):
            return False, "excluded_scanlike_or_placeholder_pdf"
        return True, "selected_generated_pdf"
    if ext in TEXTLIKE_EXT:
        return True, "selected_textlike_source"
    if base.startswith(("readme", "manifest", "inventory", "makefile", "license")):
        return True, "selected_named_textlike_source"
    return False, "excluded_unsupported_binary_or_tooling"


def iter_zip_members(zip_path: Path, prefix: str):
    with zipfile.ZipFile(zip_path) as zf:
        bad = zf.testzip()
        if bad:
            raise RuntimeError(f"Bad ZIP member {bad} in {zip_path}")
        yield from iter_open_zip(zf, prefix, zip_path.name)


def iter_open_zip(zf: zipfile.ZipFile, prefix: str, source_label: str):
    for info in zf.infolist():
        if info.is_dir():
            continue
        name = info.filename
        ext = Path(name).suffix.lower()
        if ext == ".zip":
            data = zf.read(info)
            nested_prefix = f"{prefix}/__nested_zip__/{Path(name).stem}"
            try:
                with zipfile.ZipFile(BytesIO(data)) as nested:
                    bad_nested = nested.testzip()
                    if bad_nested:
                        yield {
                            "selected": False,
                            "source_zip": source_label,
                            "source_path": name,
                            "archive_path": "",
                            "bytes": info.file_size,
                            "sha256": "",
                            "reason": f"bad_nested_zip:{bad_nested}",
                        }, None
                        continue
                    yield from iter_open_zip(nested, nested_prefix, f"{source_label}!/{name}")
            except zipfile.BadZipFile:
                yield {
                    "selected": False,
                    "source_zip": source_label,
                    "source_path": name,
                    "archive_path": "",
                    "bytes": info.file_size,
                    "sha256": "",
                    "reason": "bad_nested_zip",
                }, None
            continue

        selected, reason = should_select_member(name)
        archive_path = f"{prefix}/{name}"
        if not selected:
            yield {
                "selected": False,
                "source_zip": source_label,
                "source_path": name,
                "archive_path": archive_path,
                "bytes": info.file_size,
                "sha256": "",
                "reason": reason,
            }, None
            continue

        data = zf.read(info)
        yield {
            "selected": True,
            "source_zip": source_label,
            "source_path": name,
            "archive_path": archive_path,
            "bytes": info.file_size,
            "sha256": sha256_bytes(data),
            "reason": reason,
        }, data


def unique_archive_path(existing: set[str], archive_path: str) -> str:
    candidate = archive_path.replace("\\", "/")
    if candidate not in existing:
        existing.add(candidate)
        return candidate
    path = Path(candidate)
    stem = path.with_suffix("").as_posix()
    suffix = path.suffix
    for index in range(2, 100_000):
        candidate = f"{stem}__dup{index}{suffix}"
        if candidate not in existing:
            existing.add(candidate)
            return candidate
    raise RuntimeError(f"Could not allocate unique archive path for {archive_path}")


def readme_text(summary: dict[str, object]) -> str:
    return (
        "# Kimi 7 continuation non-scan delta\n\n"
        "This ZIP is intended for web-session source upload. It contains the useful non-scan "
        "material from `Kimi_Agent_Continue LaTeX Typesetting Work.zip`: TeX, text/OCR, logs, "
        "manifests, and generated PDFs.\n\n"
        "Excluded: page images, scan/render images, obvious scan/reference PDFs, known placeholder "
        "PDFs, unsupported tool binaries, exact duplicates already present in the prior Kimi 7 "
        "170 MB non-scan handoff, and exact duplicates within this continuation drop.\n\n"
        f"Selected files: {summary['selected_file_count']}\n\n"
        f"Selected uncompressed bytes: {summary['selected_total_uncompressed_bytes']}\n\n"
        f"Chunk count: {summary['chunk_count']}\n"
    )


def write_chunk(chunk_index: int, items: list[tuple[str, bytes]]) -> dict[str, object]:
    destination = CHUNKS / f"kimi7_continue_nonscan_delta_for_web_chunk_{chunk_index:03d}.zip"
    with zipfile.ZipFile(destination, "w", compression=zipfile.ZIP_DEFLATED, allowZip64=True) as zf:
        for archive_path, data in items:
            zf.writestr(archive_path, data)
    with zipfile.ZipFile(destination) as zf:
        bad = zf.testzip()
        if bad:
            raise RuntimeError(f"Bad member {bad} in {destination}")
    size = destination.stat().st_size
    if size >= MAX_CHUNK_BYTES:
        raise RuntimeError(f"Chunk exceeds web upload limit: {destination} is {size} bytes")
    return {
        "chunk_index": chunk_index,
        "name": destination.name,
        "bytes": size,
        "sha256": hashlib.sha256(destination.read_bytes()).hexdigest(),
        "file_count": len(items),
        "uncompressed_bytes": sum(len(data) for _, data in items),
    }


def main() -> int:
    if not SOURCE_ZIP.exists():
        raise SystemExit(f"Missing source ZIP: {SOURCE_ZIP}")
    if OUT.exists():
        if OUT.name != "KIMI7_CONTINUE_NONSCAN_DELTA_FOR_WEB_CURRENT":
            raise SystemExit(f"Refusing to remove unexpected output folder: {OUT}")
        shutil.rmtree(OUT)
    CHUNKS.mkdir(parents=True, exist_ok=True)

    baseline_hashes = load_baseline_hashes()
    selected_rows: list[dict[str, object]] = []
    skipped_rows: list[dict[str, object]] = []
    selected_items: list[tuple[str, bytes]] = []
    seen_hashes: set[str] = set()
    archive_paths: set[str] = set()
    skipped_reason_counts: Counter[str] = Counter()
    selected_reason_counts: Counter[str] = Counter()
    selected_ext_counts: Counter[str] = Counter()

    prefix = source_slug(SOURCE_ZIP)
    for row, data in iter_zip_members(SOURCE_ZIP, prefix):
        if not row["selected"]:
            skipped_rows.append(row)
            skipped_reason_counts[str(row["reason"])] += 1
            continue
        assert data is not None
        digest = str(row["sha256"]).lower()
        if digest in baseline_hashes:
            row = dict(row)
            row["selected"] = False
            row["reason"] = "excluded_exact_duplicate_from_prior_170mb_handoff"
            skipped_rows.append(row)
            skipped_reason_counts[str(row["reason"])] += 1
            continue
        if digest in seen_hashes:
            row = dict(row)
            row["selected"] = False
            row["reason"] = "excluded_exact_duplicate_within_continue_drop"
            skipped_rows.append(row)
            skipped_reason_counts[str(row["reason"])] += 1
            continue
        seen_hashes.add(digest)
        archive_path = unique_archive_path(archive_paths, str(row["archive_path"]))
        row["archive_path"] = archive_path
        selected_rows.append(row)
        selected_reason_counts[str(row["reason"])] += 1
        selected_ext_counts[Path(archive_path).suffix.lower() or "<no_ext>"] += 1
        selected_items.append((archive_path, data))

    summary: dict[str, object] = {
        "generated_at": now_iso(),
        "source_zip_name": SOURCE_ZIP.name,
        "source_zip_bytes": SOURCE_ZIP.stat().st_size,
        "source_zip_sha256": hashlib.sha256(SOURCE_ZIP.read_bytes()).hexdigest(),
        "baseline_hashes_loaded": len(baseline_hashes),
        "selected_file_count": len(selected_rows),
        "selected_total_uncompressed_bytes": sum(int(row["bytes"]) for row in selected_rows),
        "selected_reason_counts": dict(selected_reason_counts),
        "selected_extension_counts": dict(selected_ext_counts),
        "skipped_reason_counts": dict(skipped_reason_counts),
    }
    selected_items.insert((0), ("00_README_KIMI7_CONTINUE_NONSCAN_DELTA.md", readme_text({**summary, "chunk_count": "pending"}).encode("utf-8")))

    chunks: list[dict[str, object]] = []
    current: list[tuple[str, bytes]] = []
    current_uncompressed = 0
    for archive_path, data in selected_items:
        if current and current_uncompressed + len(data) > TARGET_UNCOMPRESSED_BYTES:
            chunks.append(write_chunk(len(chunks) + 1, current))
            current = []
            current_uncompressed = 0
        current.append((archive_path, data))
        current_uncompressed += len(data)
    if current:
        chunks.append(write_chunk(len(chunks) + 1, current))

    summary["chunk_count"] = len(chunks)
    summary["chunks"] = chunks
    summary["policy"] = (
        "Continuation-only non-scan package: includes TeX/text/source/QC files and generated PDFs; "
        "excludes scan/render images, obvious scan/reference PDFs, known placeholder PDFs, unsupported "
        "binaries/tooling, exact duplicates from the already-uploaded Kimi 7 170 MB handoff, and exact "
        "duplicates within the continuation drop."
    )

    fields = ["selected", "source_zip", "source_path", "archive_path", "bytes", "sha256", "reason"]
    with (OUT / "kimi7_continue_nonscan_delta_selected_manifest.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(selected_rows)
    with (OUT / "kimi7_continue_nonscan_delta_skipped_manifest.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(skipped_rows)
    with (CHUNKS / "chunk_manifest.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["chunk_index", "name", "bytes", "sha256", "file_count", "uncompressed_bytes"])
        writer.writeheader()
        writer.writerows(chunks)
    (CHUNKS / "UPLOAD_THESE_ZIPS.txt").write_text("\n".join(row["name"] for row in chunks) + "\n", encoding="utf-8")
    (OUT / "kimi7_continue_nonscan_delta_summary.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (OUT / "README.md").write_text(readme_text(summary), encoding="utf-8")

    print(json.dumps(summary, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
