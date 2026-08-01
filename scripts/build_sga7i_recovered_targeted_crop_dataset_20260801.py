#!/usr/bin/env python3
"""Build exact SGA7 I targeted-crop archives from the surviving temp cache."""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
import shutil
import sys
import zipfile
from collections import Counter
from pathlib import Path, PurePosixPath


PARENT_SCAN_SHA256 = (
    "9CD40FF06EB1E488AF385A56899D4F492492A06A1E2E3C0ED6876B82E3E3603F"
)
METADATA_ARCHIVE_SHA256 = (
    "33B87235BCECB8274D18FCE0B7B2952A8301AD16E1C61C3825FACDB97BDFCEC4"
)
FIXED_ZIP_TIME = (2026, 8, 1, 0, 0, 0)
IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".tif", ".tiff", ".jpx", ".pnm"}
PRIVATE_PATTERNS = (
    re.compile(r"(?i)[A-Z]:[\\/]+Users[\\/]+Floris"),
    re.compile(r"(?i)AppData[\\/]+Local[\\/]+Temp"),
    re.compile(r"(?i)C--Users-Floris"),
    re.compile(r"(?i)[A-Z]:[\\/]+w[\\/]"),
)
CHUNKS = {
    "I_II_VI": {"I", "II", "VI"},
    "VII_IX": {"VII", "VIII", "IX", "unmapped_front_matter_or_unresolved"},
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--metadata-dir", type=Path, required=True)
    parser.add_argument("--metadata-archive", type=Path, required=True)
    parser.add_argument("--public-index-cache", type=Path, required=True)
    parser.add_argument("--scratch-root", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--github-dir", type=Path, required=True)
    return parser.parse_args()


def sha256_path(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(4 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, indent=2, ensure_ascii=True) + "\n").encode("utf-8")


def csv_bytes(rows: list[dict[str, object]], fields: list[str]) -> bytes:
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\r\n")
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue().encode("utf-8")


def zip_info(name: str) -> zipfile.ZipInfo:
    info = zipfile.ZipInfo(name, FIXED_ZIP_TIME)
    info.compress_type = zipfile.ZIP_STORED
    info.external_attr = 0o100644 << 16
    return info


def safe_member(name: str) -> bool:
    pure = PurePosixPath(name)
    return (
        name == name.replace("\\", "/")
        and not pure.is_absolute()
        and ".." not in pure.parts
        and not re.match(r"^[A-Za-z]:", name)
    )


def write_file_member(bundle: zipfile.ZipFile, name: str, source: Path) -> None:
    info = zip_info(name)
    info.file_size = source.stat().st_size
    with source.open("rb") as src, bundle.open(info, "w", force_zip64=True) as dst:
        shutil.copyfileobj(src, dst, length=8 * 1024 * 1024)


def public_hashes(path: Path) -> tuple[set[str], dict]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    return {value.upper() for value in payload["hashes"]}, payload["summary"]


def read_index(metadata_dir: Path) -> list[dict[str, str]]:
    path = metadata_dir / "SGA7I_VISUAL_EVIDENCE_INDEX.csv"
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def select_rows(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    return [
        row
        for row in rows
        if row["parent_pdf_sha256"].upper() == PARENT_SCAN_SHA256
        and row["evidence_class"] == "targeted_crop"
        and row["pixel_scope"] == "targeted_region_or_detail"
    ]


def match_rows(
    rows: list[dict[str, str]], scratch_root: Path
) -> tuple[list[tuple[dict[str, str], Path]], list[dict[str, str]]]:
    needed = {
        (row["relative_path"].casefold(), int(row["bytes"])) for row in rows
    }
    candidates: dict[tuple[str, int], list[Path]] = {}
    for path in scratch_root.iterdir():
        if not path.is_file() or path.suffix.lower() not in IMAGE_SUFFIXES:
            continue
        key = (path.name.casefold(), path.stat().st_size)
        if key in needed:
            candidates.setdefault(key, []).append(path)
    digest_cache: dict[Path, str] = {}
    matched: list[tuple[dict[str, str], Path]] = []
    unmatched: list[dict[str, str]] = []
    for row in rows:
        key = (row["relative_path"].casefold(), int(row["bytes"]))
        exact = []
        for path in candidates.get(key, []):
            digest_cache.setdefault(path, sha256_path(path))
            if digest_cache[path] == row["sha256"].upper():
                exact.append(path)
        if len(exact) == 1:
            matched.append((row, exact[0]))
        elif not exact:
            unmatched.append(row)
        else:
            raise RuntimeError(f"ambiguous exact local matches: {row['visual_id']}")
    return matched, unmatched


def archive_member(row: dict[str, str]) -> str:
    name = PurePosixPath(row["relative_path"].replace("\\", "/")).name
    return f"images/{row['visual_id']}_{name}"


PUBLIC_FIELDS = [
    "archive_member",
    "visual_id",
    "relative_path",
    "bytes",
    "sha256",
    "width_px",
    "height_px",
    "color_mode",
    "image_format",
    "parent_pdf_sha256",
    "parent_pdf_index_0based",
    "parent_pdf_physical_page_1based",
    "book_folio",
    "page_resolution_method",
    "page_resolution_confidence",
    "expose",
    "linked_tex_file",
    "linked_tex_sha256",
    "parent_page_rotation_deg",
    "parent_scan_width_px",
    "parent_scan_height_px",
    "parent_scan_effective_dpi_x",
    "parent_scan_effective_dpi_y",
    "generator_script",
    "generator_script_sha256",
    "generator_match_method",
    "generator_source_class",
    "evidence_class",
    "bbox_fx0",
    "bbox_fy0",
    "bbox_fx1",
    "bbox_fy1",
    "render_parameter",
    "manual_review_link",
    "qa_disposition",
    "read_count",
    "duplicate_instance_count",
]


def public_row(row: dict[str, str]) -> dict[str, object]:
    output: dict[str, object] = {field: row.get(field, "") for field in PUBLIC_FIELDS}
    output["archive_member"] = archive_member(row)
    return output


def unavailable_row(row: dict[str, str]) -> dict[str, object]:
    return {
        "visual_id": row["visual_id"],
        "relative_path": row["relative_path"],
        "bytes": row["bytes"],
        "sha256": row["sha256"],
        "parent_pdf_index_0based": row["parent_pdf_index_0based"],
        "parent_pdf_physical_page_1based": row["parent_pdf_physical_page_1based"],
        "book_folio": row["book_folio"],
        "expose": row["expose"],
        "linked_tex_file": row["linked_tex_file"],
        "generator_source_class": row["generator_source_class"],
        "disposition": "ledgered_targeted_crop_not_present_in_surviving_local_cache",
    }


UNAVAILABLE_FIELDS = [
    "visual_id",
    "relative_path",
    "bytes",
    "sha256",
    "parent_pdf_index_0based",
    "parent_pdf_physical_page_1based",
    "book_folio",
    "expose",
    "linked_tex_file",
    "generator_source_class",
    "disposition",
]


def readme_for_chunk(label: str, rows: list[dict[str, str]]) -> bytes:
    exposes = sorted({row["expose"] for row in rows})
    return (
        "# SGA 7 I targeted high-detail source crops\n\n"
        f"This archive preserves {len(rows):,} exact source-derived targeted crops "
        f"for {', '.join(exposes)} from the SGA 7 I source-audit workspace. "
        "The images are the tight crops used during transcription and diagram checking, "
        "not screenshots of the project reader.\n\n"
        "`IMAGE_MANIFEST.csv` binds each pixel file to the parent scan SHA-256, page "
        "mapping, dimensions, linked TeX unit, and recovered generation/review metadata. "
        "The parent scan and private execution paths are not duplicated here.\n\n"
        "This is reusable source-audit evidence, not a claim that every crop was a final "
        "adjudication or that the corresponding transcription is mathematically certified.\n"
    ).encode("utf-8")


def build_image_archive(
    output_path: Path, label: str, items: list[tuple[dict[str, str], Path]]
) -> dict[str, object]:
    rows = [public_row(row) for row, _ in items]
    manifest = csv_bytes(rows, PUBLIC_FIELDS)
    readme = readme_for_chunk(label, [row for row, _ in items])
    content: dict[str, tuple[int, str]] = {
        "README.md": (len(readme), sha256_bytes(readme)),
        "IMAGE_MANIFEST.csv": (len(manifest), sha256_bytes(manifest)),
    }
    for row, path in items:
        content[archive_member(row)] = (path.stat().st_size, row["sha256"].upper())
    sums = csv_bytes(
        [
            {"path": name, "bytes": size, "sha256": digest}
            for name, (size, digest) in sorted(content.items())
        ],
        ["path", "bytes", "sha256"],
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output_path, "w", allowZip64=True) as bundle:
        bundle.writestr(zip_info("README.md"), readme)
        bundle.writestr(zip_info("IMAGE_MANIFEST.csv"), manifest)
        bundle.writestr(zip_info("SHA256SUMS.csv"), sums)
        for row, path in items:
            write_file_member(bundle, archive_member(row), path)
    expected = dict(content)
    expected["SHA256SUMS.csv"] = (len(sums), sha256_bytes(sums))
    errors = []
    uncompressed = 0
    with zipfile.ZipFile(output_path) as bundle:
        if bundle.testzip():
            errors.append("CRC failure")
        names = [entry.filename for entry in bundle.infolist() if not entry.is_dir()]
        if len(names) != len(set(names)):
            errors.append("duplicate ZIP member")
        if not all(safe_member(name) for name in names):
            errors.append("unsafe ZIP member")
        if set(names) != set(expected):
            errors.append("member set mismatch")
        for entry in bundle.infolist():
            if entry.is_dir():
                continue
            uncompressed += entry.file_size
            payload = bundle.read(entry)
            size, digest = expected[entry.filename]
            if len(payload) != size or sha256_bytes(payload) != digest:
                errors.append(f"identity mismatch: {entry.filename}")
    if errors:
        raise RuntimeError("; ".join(errors[:10]))
    return {
        "label": label,
        "filename": output_path.name,
        "bytes": output_path.stat().st_size,
        "sha256": sha256_path(output_path),
        "members": len(expected),
        "uncompressed_bytes": uncompressed,
        "images": len(items),
        "image_bytes": sum(path.stat().st_size for _, path in items),
        "manifest_rows": len(rows),
        "status": "PASS",
    }


def metadata_readme() -> bytes:
    return (
        "# SGA 7 I targeted-crop dataset controls\n\n"
        "Two image archives preserve every exact SGA 7 I targeted crop that remains in "
        "the inspected local cache and was not already public by SHA-256. The complete "
        "manifest records the included pixels. The unavailable ledger records targeted "
        "crops known to the earlier exact provenance index but no longer present locally.\n\n"
        "The image dataset is deliberately separate from the SGA reader landing page.\n"
    ).encode("utf-8")


def build_metadata_archive(
    output_path: Path,
    included: list[tuple[dict[str, str], Path]],
    unavailable: list[dict[str, str]],
    duplicates: list[dict[str, str]],
    summary: dict[str, object],
) -> dict[str, object]:
    readme = metadata_readme()
    manifest = csv_bytes([public_row(row) for row, _ in included], PUBLIC_FIELDS)
    unavailable_data = csv_bytes(
        [unavailable_row(row) for row in unavailable], UNAVAILABLE_FIELDS
    )
    duplicate_data = csv_bytes(
        [unavailable_row(row) | {"disposition": "already_public_by_sha256"} for row in duplicates],
        UNAVAILABLE_FIELDS,
    )
    summary_data = json_bytes(summary)
    payloads = {
        "README.md": readme,
        "INCLUDED_IMAGE_MANIFEST.csv": manifest,
        "UNAVAILABLE_TARGETED_CROP_LEDGER.csv": unavailable_data,
        "ALREADY_PUBLIC_DUPLICATES.csv": duplicate_data,
        "DATASET_SUMMARY.json": summary_data,
    }
    sums = csv_bytes(
        [
            {"path": name, "bytes": len(data), "sha256": sha256_bytes(data)}
            for name, data in sorted(payloads.items())
        ],
        ["path", "bytes", "sha256"],
    )
    with zipfile.ZipFile(output_path, "w") as bundle:
        for name, data in payloads.items():
            bundle.writestr(zip_info(name), data)
        bundle.writestr(zip_info("SHA256SUMS.csv"), sums)
    with zipfile.ZipFile(output_path) as bundle:
        if bundle.testzip():
            raise RuntimeError("metadata archive CRC failure")
        members = [entry for entry in bundle.infolist() if not entry.is_dir()]
        if len(members) != 6 or not all(safe_member(entry.filename) for entry in members):
            raise RuntimeError("metadata archive member failure")
    return {
        "label": "metadata",
        "filename": output_path.name,
        "bytes": output_path.stat().st_size,
        "sha256": sha256_path(output_path),
        "members": 6,
        "uncompressed_bytes": sum(entry.file_size for entry in members),
        "status": "PASS",
    }


def scan_private(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    return [pattern.pattern for pattern in PRIVATE_PATTERNS if pattern.search(text)]


def main() -> int:
    args = parse_args()
    metadata_archive = args.metadata_archive.resolve()
    if sha256_path(metadata_archive) != METADATA_ARCHIVE_SHA256:
        raise RuntimeError("metadata archive identity mismatch")
    public, public_summary = public_hashes(args.public_index_cache.resolve())
    selected = select_rows(read_index(args.metadata_dir.resolve()))
    matched, unavailable = match_rows(selected, args.scratch_root.resolve())
    duplicates = [row for row, _ in matched if row["sha256"].upper() in public]
    included = [item for item in matched if item[0]["sha256"].upper() not in public]
    if len(selected) != 11_766 or len(included) != 5_855:
        raise RuntimeError(
            f"unexpected selection boundary: selected={len(selected)} included={len(included)}"
        )
    chunked: dict[str, list[tuple[dict[str, str], Path]]] = {
        label: [] for label in CHUNKS
    }
    for item in included:
        labels = [label for label, exposes in CHUNKS.items() if item[0]["expose"] in exposes]
        if len(labels) != 1:
            raise RuntimeError(
                f"unmapped or multiply mapped expose: {item[0]['visual_id']} {item[0]['expose']}"
            )
        chunked[labels[0]].append(item)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    archive_names = {
        "I_II_VI": "00_SGA7I_Targeted_HighDetail_Source_Crops_I_II_VI_20260801.zip",
        "VII_IX": "01_SGA7I_Targeted_HighDetail_Source_Crops_VII_IX_20260801.zip",
    }
    archives = []
    for label in CHUNKS:
        archives.append(
            build_image_archive(
                args.output_dir / archive_names[label], label, chunked[label]
            )
        )
    by_expose = Counter(item[0]["expose"] for item in included)
    summary: dict[str, object] = {
        "schema": "sga7i-targeted-high-detail-source-crops-dataset-v1",
        "created_date": "2026-08-01",
        "parent_scan": {
            "sha256": PARENT_SCAN_SHA256,
            "pages": 540,
            "included": False,
        },
        "source_metadata_archive": {
            "filename": metadata_archive.name,
            "bytes": metadata_archive.stat().st_size,
            "sha256": METADATA_ARCHIVE_SHA256,
        },
        "public_visual_baseline": public_summary,
        "selected_targeted_rows": len(selected),
        "matched_local_rows": len(matched),
        "already_public_rows": len(duplicates),
        "included_rows": len(included),
        "included_image_bytes": sum(path.stat().st_size for _, path in included),
        "unavailable_rows": len(unavailable),
        "included_by_expose": dict(sorted(by_expose.items())),
        "archives": archives,
        "claim_limit": "source-audit pixel evidence, not transcription or mathematical certification",
    }
    metadata_result = build_metadata_archive(
        args.output_dir / "90_SGA7I_Targeted_Source_Crops_Metadata_20260801.zip",
        included,
        unavailable,
        duplicates,
        summary,
    )
    archives.append(metadata_result)
    outer_manifest = csv_bytes(
        [
            {
                "filename": row["filename"],
                "bytes": row["bytes"],
                "sha256": row["sha256"],
                "members": row["members"],
                "uncompressed_bytes": row["uncompressed_bytes"],
                "role": "targeted_source_pixels" if row["label"] != "metadata" else "metadata_and_recovery_ledger",
            }
            for row in archives
        ],
        ["filename", "bytes", "sha256", "members", "uncompressed_bytes", "role"],
    )
    validation = {
        "schema": "sga7i-targeted-high-detail-source-crops-build-validation-v1",
        "status": "PASS",
        "errors": [],
        "summary": summary,
        "outer_manifest_sha256": sha256_bytes(outer_manifest),
        "outer_files": len(archives),
        "outer_bytes": sum(int(row["bytes"]) for row in archives),
        "privacy_hits": 0,
    }
    validation_data = json_bytes(validation)
    github_readme = metadata_readme() + (
        b"\nThe pixel ZIPs are deposited on the dedicated Zenodo visual-evidence dataset; "
        b"GitHub carries the exact controls and reproducible builder without duplicating "
        b"hundreds of megabytes of binary pixels.\n"
    )
    args.github_dir.mkdir(parents=True, exist_ok=True)
    outputs = {
        "README.md": github_readme,
        "ZENODO_UPLOAD_MANIFEST.csv": outer_manifest,
        "DATASET_SUMMARY.json": json_bytes(summary),
        "BUILD_VALIDATION.json": validation_data,
        "INCLUDED_IMAGE_MANIFEST.csv": csv_bytes(
            [public_row(row) for row, _ in included], PUBLIC_FIELDS
        ),
        "UNAVAILABLE_TARGETED_CROP_LEDGER.csv": csv_bytes(
            [unavailable_row(row) for row in unavailable], UNAVAILABLE_FIELDS
        ),
        "ALREADY_PUBLIC_DUPLICATES.csv": csv_bytes(
            [
                unavailable_row(row) | {"disposition": "already_public_by_sha256"}
                for row in duplicates
            ],
            UNAVAILABLE_FIELDS,
        ),
    }
    for name, data in outputs.items():
        (args.github_dir / name).write_bytes(data)
    privacy_hits = {
        path.name: scan_private(path)
        for path in args.github_dir.iterdir()
        if path.is_file() and scan_private(path)
    }
    if privacy_hits:
        raise RuntimeError(f"private path in GitHub controls: {privacy_hits}")
    print(json.dumps(validation, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
