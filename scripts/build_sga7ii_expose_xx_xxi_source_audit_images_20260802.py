#!/usr/bin/env python3
"""Package source images used from SGA7 II Expose XX 4.4 through XXI 4."""

from __future__ import annotations

import csv
import hashlib
import io
import json
import re
import shutil
import zipfile
from pathlib import Path, PurePosixPath

from PIL import Image


Image.MAX_IMAGE_PIXELS = None

REPO_ROOT = Path(__file__).resolve().parents[1]
LIVE_QA_ROOT = Path(
    r"C:\Users\Floris\Documents\interlanguage\03_projects\language_management"
    r"\english_germanic\03_working_translations"
    r"\sga7ii_english_complete_translation_successor_20260801_r1\qa"
)
PACKAGE_ROOT = REPO_ROOT / (
    "sources/sga/sga7ii-expose-xx-xxi-source-audit-images-idx364-391-20260802"
)
PARENT_SCAN_SHA256 = (
    "FA679DEBFC8ADA3232D7E752A1837FC6CE474488E20A44D7641CF296876E1297"
)
ZIP_TIMESTAMP = (2026, 8, 2, 0, 0, 0)

GROUPS = {
    "translated_idx364_391": {
        "zip": (
            "SGA7II_ExposeXX_XXI_SourceAudit_Images_"
            "idx364_391_Through_XXI_4_20260802.zip"
        ),
        "expected": 64,
        "scope": "Expose XX Section 4.4 through complete Expose XX and Expose XXI through Section 4 and bibliography",
        "disposition": "used_for_translated_checkpoint_qa",
        "directories": (
            "expose_XX_idx364_1100dpi",
            "expose_XX_idx364_details_5000dpi",
            "expose_XX_idx365_1100dpi",
            "expose_XX_idx365_details_5000dpi",
            "expose_XX_idx366_1100dpi",
            "expose_XX_idx367_1100dpi",
            "expose_XX_idx367_diagram_5000dpi",
            "expose_XX_idx367_formula_details_5000dpi",
            "expose_XX_idx368_369_1100dpi",
            "expose_XX_idx369_details_9000dpi",
            "expose_XXI_idx370_373_1100dpi",
            "expose_XXI_idx374_375_1100dpi",
            "expose_XXI_idx376_377_1100dpi",
            "expose_XXI_prop1_2_locator_crops_1100dpi",
            "expose_XXI_prop1_2_details_5000dpi",
            "expose_XXI_theorem1_3_idx378_381_1100dpi",
            "expose_XXI_theorem1_3_details_5000dpi",
            "expose_XXI_theorem1_4_idx382_384_1100dpi",
            "expose_XXI_theorem1_4_details_5000dpi",
            "expose_XXI_section2_idx385_386_1100dpi",
            "expose_XXI_section2_details_5000dpi",
            "expose_XXI_section3_idx387_389_1100dpi",
            "expose_XXI_section4_idx390_391_1100dpi",
        ),
    },
}

DIRECTORY_DEFAULT_INDEX = {
    "expose_XXI_prop1_2_details_5000dpi": 376,
    "expose_XXI_theorem1_3_details_5000dpi": 378,
    "expose_XXI_theorem1_4_details_5000dpi": 382,
    "expose_XXI_section2_details_5000dpi": 385,
}

INDEX_FIELDS = (
    "evidence_id",
    "archive",
    "member_path",
    "bytes",
    "sha256",
    "width_px",
    "height_px",
    "mode",
    "dpi_x",
    "dpi_y",
    "review_scale_dpi",
    "source_scan_index",
    "printed_folio",
    "expose",
    "scope",
    "evidence_role",
    "qa_disposition",
    "parent_scan_sha256",
)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def sha256_path(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def identity(path: Path) -> tuple[int, str]:
    return path.stat().st_size, sha256_path(path)


def csv_bytes(rows: list[dict[str, object]], fields: tuple[str, ...]) -> bytes:
    output = io.StringIO(newline="")
    writer = csv.DictWriter(
        output,
        fieldnames=fields,
        lineterminator="\n",
        quoting=csv.QUOTE_ALL,
    )
    writer.writeheader()
    writer.writerows(rows)
    return output.getvalue().encode("utf-8")


def write_json(path: Path, value: object) -> None:
    path.write_text(
        json.dumps(value, indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def safe_member(name: str) -> bool:
    pure = PurePosixPath(name)
    return (
        name == name.replace("\\", "/")
        and not pure.is_absolute()
        and ".." not in pure.parts
        and not (len(name) > 1 and name[1] == ":")
    )


def infer_index(directory: str, filename: str) -> int:
    number_match = re.fullmatch(r"Number12-(\d+)\.png", filename)
    if number_match:
        return int(number_match.group(1)) - 1
    filename_match = re.search(r"(?:^|_)idx(\d+)(?:_|\.)", filename)
    if filename_match:
        return int(filename_match.group(1))
    folio_match = re.search(r"folio(\d+)", filename)
    if folio_match:
        return int(folio_match.group(1)) + 7
    directory_match = re.search(r"_idx(\d+)(?:_|$)", directory)
    if directory_match:
        return int(directory_match.group(1))
    if directory in DIRECTORY_DEFAULT_INDEX:
        return DIRECTORY_DEFAULT_INDEX[directory]
    raise ValueError(f"Cannot infer source index for {directory}/{filename}")


def declared_dpi(directory: str, filename: str) -> int:
    probe_match = re.search(r"coordinate_probe_(\d{3,4})", filename, re.IGNORECASE)
    if probe_match:
        return int(probe_match.group(1))
    match = re.search(r"(\d{3,4})dpi", filename, re.IGNORECASE)
    if match:
        return int(match.group(1))
    match = re.search(r"(\d{3,4})dpi", directory, re.IGNORECASE)
    if match:
        return int(match.group(1))
    raise ValueError(f"Cannot infer DPI for {directory}/{filename}")


def image_metadata(path: Path) -> tuple[int, int, str, float, float]:
    with Image.open(path) as image:
        width, height = image.size
        mode = image.mode
        dpi = image.info.get("dpi", (0.0, 0.0))
        dpi_x = float(dpi[0]) if dpi else 0.0
        dpi_y = float(dpi[1]) if dpi else 0.0
        image.verify()
    return width, height, mode, dpi_x, dpi_y


def source_files(group: dict[str, object]) -> list[tuple[str, Path]]:
    result: list[tuple[str, Path]] = []
    for directory in group["directories"]:
        root = LIVE_QA_ROOT / str(directory)
        if not root.is_dir():
            raise FileNotFoundError(root)
        for path in sorted(root.iterdir(), key=lambda item: item.name.casefold()):
            if path.is_file() and path.suffix.lower() == ".png":
                result.append((str(directory), path))
    expected = int(group["expected"])
    if len(result) != expected:
        raise ValueError(f"Expected {expected} images, found {len(result)}")
    return result


def build_rows() -> tuple[list[dict[str, object]], dict[str, list[tuple[str, Path]]]]:
    rows: list[dict[str, object]] = []
    selected: dict[str, list[tuple[str, Path]]] = {}
    counter = 0
    for group_name, group in GROUPS.items():
        files = source_files(group)
        selected[group_name] = files
        for directory, path in files:
            counter += 1
            source_index = infer_index(directory, path.name)
            expected_dpi = declared_dpi(directory, path.name)
            width, height, mode, dpi_x, dpi_y = image_metadata(path)
            if width <= 0 or height <= 0:
                raise ValueError(f"Invalid image dimensions for {path}")
            role = "full_source_page" if path.name.startswith("Number12-") else "targeted_source_crop"
            member = f"{group_name}/{directory}/{path.name}"
            rows.append(
                {
                    "evidence_id": f"SGA7II-XX-XXI-SRCIMG-{counter:04d}",
                    "archive": str(group["zip"]),
                    "member_path": member,
                    "bytes": path.stat().st_size,
                    "sha256": sha256_path(path),
                    "width_px": width,
                    "height_px": height,
                    "mode": mode,
                    "dpi_x": f"{dpi_x:.3f}" if dpi_x else "",
                    "dpi_y": f"{dpi_y:.3f}" if dpi_y else "",
                    "review_scale_dpi": expected_dpi,
                    "source_scan_index": source_index,
                    "printed_folio": source_index - 7,
                    "expose": "XXI" if directory.startswith("expose_XXI_") else "XX",
                    "scope": str(group["scope"]),
                    "evidence_role": role,
                    "qa_disposition": str(group["disposition"]),
                    "parent_scan_sha256": PARENT_SCAN_SHA256,
                }
            )
    return rows, selected


def make_zip(
    zip_path: Path,
    group_name: str,
    rows: list[dict[str, object]],
    files: list[tuple[str, Path]],
) -> dict[str, object]:
    row_by_member = {str(row["member_path"]): row for row in rows}
    manifest = csv_bytes(rows, INDEX_FIELDS)
    source_before = {
        f"{group_name}/{directory}/{path.name}": identity(path)
        for directory, path in files
    }
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_STORED) as archive:
        for member, (_, path) in sorted(
            zip(source_before, files), key=lambda pair: pair[0].casefold()
        ):
            info = zipfile.ZipInfo(member, ZIP_TIMESTAMP)
            info.compress_type = zipfile.ZIP_STORED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, path.read_bytes())
        info = zipfile.ZipInfo(f"{group_name}/MANIFEST.csv", ZIP_TIMESTAMP)
        info.compress_type = zipfile.ZIP_STORED
        info.external_attr = 0o100644 << 16
        archive.writestr(info, manifest)

    source_after = {
        f"{group_name}/{directory}/{path.name}": identity(path)
        for directory, path in files
    }
    if source_before != source_after:
        raise RuntimeError("Source images changed while the archive was built")

    with zipfile.ZipFile(zip_path) as archive:
        names = archive.namelist()
        if archive.testzip() is not None or len(names) != len(set(names)):
            raise RuntimeError(f"ZIP integrity failure: {zip_path}")
        if any(not safe_member(name) for name in names):
            raise RuntimeError(f"Unsafe ZIP member: {zip_path}")
        for name in names:
            data = archive.read(name)
            if name.endswith("/MANIFEST.csv"):
                if data != manifest:
                    raise RuntimeError(f"Embedded manifest mismatch: {zip_path}")
                continue
            row = row_by_member[name]
            if len(data) != int(row["bytes"]) or sha256_bytes(data) != row["sha256"]:
                raise RuntimeError(f"ZIP member mismatch: {name}")
    return {
        "file": zip_path.name,
        "bytes": zip_path.stat().st_size,
        "sha256": sha256_path(zip_path),
        "image_members": len(files),
        "total_members": len(files) + 1,
        "uncompressed_bytes": sum(size for size, _ in source_before.values()) + len(manifest),
    }


def package_text() -> tuple[str, str]:
    readme = """# SGA 7 II Exposes XX-XXI source-audit images

This compact evidence package preserves the high-resolution source pages and
targeted symbol, formula, and diagram crops actually used for Expose XX
Section 4.4 through complete Expose XX and Expose XXI through Section 4 and
its bibliography. It deliberately does not contain rendered English or French
reader pages.

The ZIP covers source scan indices 364--391 used for the translated checkpoint.
The separate Expose-XXI Section-5 appendix remains outside this package and is
the next translation cursor.

`VISUAL_EVIDENCE_INDEX.csv` records each image's archive member, exact byte and
SHA-256 identity, dimensions, embedded DPI metadata, declared review scale,
source scan index, printed folio, evidence role, disposition, and parent-scan
identity. Images occur only inside the ZIP, so this package does not create a
second loose copy in the repository.
"""
    rights = """# Provenance and rights

The parent is the publicly available SGA 7 II source scan identified by
SHA-256 `FA679DEBFC8ADA3232D7E752A1837FC6CE474488E20A44D7641CF296876E1297`.
The full parent scan is not duplicated here. These page renders and focused
crops are preserved as scholarly source witnesses so later readers can inspect
the exact print underlying transcription and translation decisions.

This package asserts no new license over the underlying French publication.
Rights in the source remain with their respective holders. The images are
evidence, not an independent edition or a claim of mathematical certification.
"""
    return readme, rights


def main() -> None:
    if not LIVE_QA_ROOT.is_dir():
        raise FileNotFoundError(LIVE_QA_ROOT)
    if PACKAGE_ROOT.exists():
        shutil.rmtree(PACKAGE_ROOT)
    PACKAGE_ROOT.mkdir(parents=True)

    rows, selected = build_rows()
    index_path = PACKAGE_ROOT / "VISUAL_EVIDENCE_INDEX.csv"
    index_path.write_bytes(csv_bytes(rows, INDEX_FIELDS))
    readme, rights = package_text()
    (PACKAGE_ROOT / "README.md").write_text(readme, encoding="utf-8", newline="\n")
    (PACKAGE_ROOT / "RIGHTS_AND_PROVENANCE.md").write_text(
        rights, encoding="utf-8", newline="\n"
    )

    zip_results = []
    for group_name, group in GROUPS.items():
        group_rows = [
            row
            for row in rows
            if row["qa_disposition"] == group["disposition"]
        ]
        zip_results.append(
            make_zip(
                PACKAGE_ROOT / str(group["zip"]),
                group_name,
                group_rows,
                selected[group_name],
            )
        )

    text_paths = (
        PACKAGE_ROOT / "README.md",
        PACKAGE_ROOT / "RIGHTS_AND_PROVENANCE.md",
        index_path,
    )
    text = "\n".join(path.read_text(encoding="utf-8") for path in text_paths)
    private_patterns = ("C:\\Users", "C:/Users", "Chatnotes", ".codex", ".claude")
    privacy_hits = sum(text.casefold().count(item.casefold()) for item in private_patterns)
    if privacy_hits:
        raise RuntimeError("Private-path marker found in public metadata")

    primary_paths = sorted(
        [path for path in PACKAGE_ROOT.iterdir() if path.is_file()],
        key=lambda path: path.name.casefold(),
    )
    validation = {
        "status": "PASS_PUBLIC_SOURCE_IMAGE_ARCHIVES",
        "errors": [],
        "parent_scan_sha256": PARENT_SCAN_SHA256,
        "images": len(rows),
        "translated_checkpoint_images": int(GROUPS["translated_idx364_391"]["expected"]),
        "preparatory_images": 0,
        "privacy_hits": privacy_hits,
        "loose_images": 0,
        "archives": zip_results,
        "artifacts": [
            {"path": path.name, "bytes": path.stat().st_size, "sha256": sha256_path(path)}
            for path in primary_paths
        ],
    }
    validation_path = PACKAGE_ROOT / "PACKAGE_VALIDATION.json"
    write_json(validation_path, validation)

    manifest_rows = []
    for path in sorted(PACKAGE_ROOT.iterdir(), key=lambda item: item.name.casefold()):
        if path.is_file() and path.name != "SHA256SUMS.csv":
            manifest_rows.append(
                {
                    "path": path.name,
                    "bytes": path.stat().st_size,
                    "sha256": sha256_path(path),
                }
            )
    manifest_path = PACKAGE_ROOT / "SHA256SUMS.csv"
    manifest_path.write_bytes(csv_bytes(manifest_rows, ("path", "bytes", "sha256")))

    all_files = sorted(PACKAGE_ROOT.iterdir(), key=lambda item: item.name.casefold())
    aggregate = sha256_bytes(
        "".join(
            f"{path.name}\t{path.stat().st_size}\t{sha256_path(path)}\n"
            for path in all_files
            if path.is_file()
        ).encode("utf-8")
    )
    print(
        json.dumps(
            {
                "status": validation["status"],
                "package_files": len(all_files),
                "package_bytes": sum(path.stat().st_size for path in all_files),
                "package_aggregate_sha256": aggregate,
                "manifest_sha256": sha256_path(manifest_path),
                "validation_sha256": sha256_path(validation_path),
                "archives": zip_results,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
