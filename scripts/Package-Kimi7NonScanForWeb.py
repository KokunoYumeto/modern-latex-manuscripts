#!/usr/bin/env python3
"""Package Kimi 7 non-scan/refined source material for web-session upload."""

from __future__ import annotations

import csv
import hashlib
import json
import os
import re
import zipfile
from collections import Counter
from datetime import datetime
from io import BytesIO
from pathlib import Path


KIMI7 = Path(os.environ.get("KIMI7_SOURCE_DIR", Path.home() / "manuscript-work" / "Kimi" / "kimi 7"))
OUT = Path(os.environ.get("KIMI7_NONSCAN_OUT", Path.home() / "Downloads" / "KIMI7_NONSCAN_REFINED_FOR_WEB_CURRENT"))
CHUNKS = OUT / "WEB_UPLOAD_CHUNKS"
MAX_CHUNK_BYTES = 500_000_000
TARGET_UNCOMPRESSED = 380_000_000

IMAGE_EXT = {".png", ".jpg", ".jpeg", ".tif", ".tiff", ".webp", ".jp2", ".j2k", ".bmp", ".gif"}
TEXT_EXT = {
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
}


def now_iso() -> str:
    return datetime.now().isoformat(timespec="seconds")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def outer_slug(path: Path) -> str:
    stem = path.stem.lower()
    stem = re.sub(r"[^a-z0-9]+", "_", stem)
    return re.sub(r"_+", "_", stem).strip("_")


def is_scanlike_name(name: str) -> bool:
    lower = name.lower()
    if re.search(r"(^|/)(page|scan|image|ocr_temp|mod_page)[-_0-9]", lower):
        return True
    if any(token in lower for token in ["/scans/", "/scan/", "/images/", "/render_checks/", "/renders/"]):
        return True
    return False


def include_pdf(name: str) -> bool:
    lower = name.lower()
    if any(token in lower for token in ["scan", "reference_scan", "ocr_reference", "archive", "facsimile"]):
        return False
    if is_scanlike_name(lower):
        return False
    return True


def include_regular(name: str) -> bool:
    p = Path(name)
    ext = p.suffix.lower()
    base = p.name.lower()
    if ext in IMAGE_EXT:
        return False
    if ext == ".pdf":
        return include_pdf(name)
    if ext in TEXT_EXT:
        return True
    if base.startswith(("readme", "manifest", "inventory", "makefile", "license")):
        return True
    return False


def iter_selected_from_zip(zip_path: Path, prefix: str, depth: int = 0):
    with zipfile.ZipFile(zip_path) as zf:
        bad = zf.testzip()
        if bad:
            raise RuntimeError(f"Bad member {bad} in {zip_path}")
        for info in zf.infolist():
            if info.is_dir():
                continue
            name = info.filename
            ext = Path(name).suffix.lower()
            data = zf.read(info)
            if ext == ".zip" and depth < 2:
                nested_prefix = f"{prefix}/__nested_zip__/{Path(name).stem}"
                with BytesIO(data) as bio:
                    with zipfile.ZipFile(bio) as nested:
                        bad_nested = nested.testzip()
                        if bad_nested:
                            yield {
                                "selected": False,
                                "outer_zip": zip_path.name,
                                "source_path": name,
                                "reason": f"bad_nested_zip:{bad_nested}",
                                "bytes": info.file_size,
                            }, None, None
                            continue
                        for nested_info in nested.infolist():
                            if nested_info.is_dir():
                                continue
                            nested_name = nested_info.filename
                            nested_data = nested.read(nested_info)
                            selected = include_regular(nested_name)
                            reason = "selected_non_scan" if selected else "excluded_scan_or_unsupported"
                            row = {
                                "selected": selected,
                                "outer_zip": zip_path.name,
                                "source_path": f"{name}!/{nested_name}",
                                "archive_path": f"{nested_prefix}/{nested_name}",
                                "bytes": nested_info.file_size,
                                "sha256": sha256_bytes(nested_data) if selected else "",
                                "reason": reason,
                            }
                            yield row, nested_data if selected else None, row.get("archive_path")
                continue

            selected = include_regular(name)
            reason = "selected_non_scan" if selected else "excluded_scan_or_unsupported"
            row = {
                "selected": selected,
                "outer_zip": zip_path.name,
                "source_path": name,
                "archive_path": f"{prefix}/{name}",
                "bytes": info.file_size,
                "sha256": sha256_bytes(data) if selected else "",
                "reason": reason,
            }
            yield row, data if selected else None, row.get("archive_path")


def unique_arcname(existing: set[str], arcname: str) -> str:
    candidate = arcname
    if candidate not in existing:
        existing.add(candidate)
        return candidate
    p = Path(arcname)
    for idx in range(2, 10_000):
        candidate = f"{p.with_suffix('').as_posix()}__dup{idx}{p.suffix}"
        if candidate not in existing:
            existing.add(candidate)
            return candidate
    raise RuntimeError(f"Could not create unique archive path for {arcname}")


def write_chunk(chunk_index: int, items: list[tuple[str, bytes]]) -> dict:
    dest = CHUNKS / f"kimi7_nonscan_refined_for_web_chunk_{chunk_index:03d}.zip"
    with zipfile.ZipFile(dest, "w", compression=zipfile.ZIP_DEFLATED, allowZip64=True) as zf:
        for arcname, data in items:
            zf.writestr(arcname, data)
    with zipfile.ZipFile(dest) as zf:
        bad = zf.testzip()
        if bad:
            raise RuntimeError(f"Bad member {bad} in {dest}")
    if dest.stat().st_size >= MAX_CHUNK_BYTES:
        raise RuntimeError(f"Chunk too large for web upload: {dest} is {dest.stat().st_size} bytes")
    return {
        "chunk_index": chunk_index,
        "path": str(dest),
        "name": dest.name,
        "bytes": dest.stat().st_size,
        "sha256": hashlib.sha256(dest.read_bytes()).hexdigest(),
        "file_count": len(items),
        "uncompressed_bytes": sum(len(data) for _, data in items),
    }


def main() -> int:
    if not KIMI7.exists():
        raise SystemExit(f"Missing Kimi 7 folder: {KIMI7}")
    if OUT.exists():
        import shutil

        shutil.rmtree(OUT)
    CHUNKS.mkdir(parents=True, exist_ok=True)

    selected_rows: list[dict] = []
    skipped_rows: list[dict] = []
    chunks: list[dict] = []
    current: list[tuple[str, bytes]] = []
    current_uncompressed = 0
    seen_hashes: set[str] = set()
    existing_arcnames: set[str] = set()
    duplicate_count = 0

    for zip_path in sorted(KIMI7.glob("*.zip"), key=lambda p: p.stat().st_size, reverse=True):
        prefix = outer_slug(zip_path)
        for row, data, arcname in iter_selected_from_zip(zip_path, prefix):
            if not row.get("selected"):
                skipped_rows.append(row)
                continue
            assert data is not None and arcname is not None
            digest = row["sha256"]
            if digest in seen_hashes:
                duplicate_count += 1
                row = dict(row)
                row["selected"] = False
                row["reason"] = "excluded_exact_duplicate_content_within_kimi7"
                skipped_rows.append(row)
                continue
            seen_hashes.add(digest)
            arcname = unique_arcname(existing_arcnames, arcname)
            row["archive_path"] = arcname
            selected_rows.append(row)
            if current and current_uncompressed + len(data) > TARGET_UNCOMPRESSED:
                chunks.append(write_chunk(len(chunks) + 1, current))
                current = []
                current_uncompressed = 0
            current.append((arcname, data))
            current_uncompressed += len(data)
    if current:
        chunks.append(write_chunk(len(chunks) + 1, current))

    fields = ["selected", "outer_zip", "source_path", "archive_path", "bytes", "sha256", "reason"]
    with (OUT / "kimi7_nonscan_selected_manifest.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(selected_rows)
    with (OUT / "kimi7_nonscan_skipped_manifest.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(skipped_rows)
    with (CHUNKS / "chunk_manifest.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["chunk_index", "path", "name", "bytes", "sha256", "file_count", "uncompressed_bytes"])
        writer.writeheader()
        writer.writerows(chunks)
    (CHUNKS / "UPLOAD_THESE_ZIPS.txt").write_text("\n".join(row["path"] for row in chunks) + "\n", encoding="utf-8")

    selected_by_zip = Counter(row["outer_zip"] for row in selected_rows)
    skipped_by_reason = Counter(row["reason"] for row in skipped_rows)
    summary = {
        "generated_at": now_iso(),
        "source_folder": str(KIMI7),
        "output_folder": str(OUT),
        "chunks_folder": str(CHUNKS),
        "selected_file_count": len(selected_rows),
        "selected_total_uncompressed_bytes": sum(int(row["bytes"]) for row in selected_rows),
        "exact_duplicate_files_skipped": duplicate_count,
        "selected_by_zip": dict(selected_by_zip),
        "skipped_by_reason": dict(skipped_by_reason),
        "chunk_count": len(chunks),
        "chunks": chunks,
        "policy": "Included TeX/text/source/QC files and generated PDFs; excluded render images, page images, obvious scan/reference PDFs, unsupported binaries, and exact duplicate content within Kimi 7.",
    }
    (OUT / "kimi7_nonscan_refined_for_web_summary.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (OUT / "README.md").write_text(
        "# Kimi 7 non-scan refined web handoff\n\n"
        "This folder packages the Kimi 7 resolved downloads for web-session source upload while excluding scans/render images and obvious scan/reference PDFs.\n\n"
        "Use the ZIP files in `WEB_UPLOAD_CHUNKS/`; they are kept under 500 MB each. The manifests list what was selected and what was skipped.\n",
        encoding="utf-8",
    )
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
