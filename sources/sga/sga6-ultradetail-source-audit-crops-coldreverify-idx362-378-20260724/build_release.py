#!/usr/bin/env python3
"""Build the SGA6 idx362-378 ultra-detail source-audit crop release.

The release publishes only the tight symbol/formula crops that were actually
used during the cold source re-verification. Full-width page bands are
reproduced and hash-verified, but their pixels remain rights-blocked.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
import zipfile
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import fitz
from PIL import Image, ImageChops, ImageEnhance, ImageOps


DATE_TAG = "20260724"
PACKAGE_TAG = "idx362_378"
TARGET_ZIP = (
    "10v_SGA6_SourceAudit_Targeted_UltraDetail_Crops_"
    f"{PACKAGE_TAG}_{DATE_TAG}.zip"
)
METADATA_ZIP = (
    "10w_SGA6_SourceAudit_Crop_Provenance_RightsBlocked_Metadata_"
    f"{PACKAGE_TAG}_{DATE_TAG}.zip"
)
README_NAME = f"SGA6_UltraDetail_Crops_{PACKAGE_TAG}_README_{DATE_TAG}.md"
PARENT_NAME = f"SGA6_UltraDetail_Crops_{PACKAGE_TAG}_PARENT_SOURCE_{DATE_TAG}.json"
TARGET_MANIFEST_NAME = (
    f"SGA6_Targeted_UltraDetail_Crops_{PACKAGE_TAG}_Manifest_{DATE_TAG}.csv"
)
BLOCKED_MANIFEST_NAME = (
    f"SGA6_PageBands_{PACKAGE_TAG}_RightsBlocked_Manifest_{DATE_TAG}.csv"
)
AUDIT_CONTEXT_NAME = (
    f"SGA6_Targeted_UltraDetail_Crops_{PACKAGE_TAG}_Audit_Context_{DATE_TAG}.csv"
)
VALIDATION_NAME = (
    f"SGA6_Targeted_UltraDetail_Crops_{PACKAGE_TAG}_VALIDATION_{DATE_TAG}.json"
)
UPLOAD_MANIFEST_NAME = (
    f"SGA6_Targeted_UltraDetail_Crops_{PACKAGE_TAG}_"
    f"ZENODO_UPLOAD_MANIFEST_{DATE_TAG}.csv"
)
SHA_NAME = (
    f"SGA6_Targeted_UltraDetail_Crops_{PACKAGE_TAG}_SHA256SUMS_{DATE_TAG}.txt"
)

PARENT_SHA256 = "73FBBAD41340C12ECCDCFCF6C3A1656953FE3D712AA8E391678458CCD17B4BAA"
PARENT_BYTES = 26_833_956
PARENT_PAGES = 720
START_INDEX = 362
END_INDEX = 378
START_ENTRY = 1114
END_ENTRY = 1130
SELECTED_RAW_AUDIT_SHA256 = (
    "F36AE17F28CE851B61F58C9FDE856D406F341AE079859BD3CED74E003DCE8364"
)
KNOWN_CERT_LOG_SHA256_AT_ENTRY_1130 = (
    "B4B25F5FCE8BC586FB3D22F95F1A68868FC241E06556A255E102F18E4F674950"
)
LINKED_TEX_OBJECT = "sga6_fr_workpass.tex"

PRIVATE_MARKERS = (
    "c:\\users\\",
    "c:/users/",
    "floris",
    "chatnotes",
    "claude",
    "codex",
    "source_thread_id",
    "thread_id",
    "@gmail.",
    "@outlook.",
)
FORMULA_PREFIXES = ("=", "+", "-", "@")

COLD_BBOXES = {
    "top": (0.03, 0.98, 0.015, 0.10),
    "a": (0.03, 0.98, 0.03, 0.29),
    "b": (0.03, 0.98, 0.27, 0.53),
    "c": (0.03, 0.98, 0.51, 0.77),
    "d": (0.03, 0.98, 0.75, 0.99),
}

TARGET_SPECS: dict[str, dict[str, Any]] = {
    "zoom363_degn.png": {
        "script": "zoom363i.py",
        "index": 363,
        "bbox": (0.03, 0.30, 0.740, 0.775),
        "dpi": 8000,
        "description": "strict degree comparison near Proposition 6.6.1",
    },
    "zoom363_igtn.png": {
        "script": "zoom363i.py",
        "index": 363,
        "bbox": (0.10, 0.48, 0.628, 0.668),
        "dpi": 8000,
        "description": "lambda superscript and strict i greater than n condition",
    },
    "zoom365_lami.png": {
        "script": "zoom365lam.py",
        "index": 365,
        "bbox": (0.30, 0.80, 0.345, 0.415),
        "dpi": 8000,
        "description": "Corollary 6.6.4 alternating lambda expression",
    },
    "zoom365_lami2.png": {
        "script": "zoom365lam2.py",
        "index": 365,
        "bbox": (0.58, 0.86, 0.345, 0.415),
        "dpi": 12000,
        "description": "tight lambda glyph and argument check in Corollary 6.6.4",
    },
    "zoom368_zbar.png": {
        "script": "zoom368.py",
        "index": 368,
        "bbox": (0.08, 0.60, 0.283, 0.325),
        "dpi": 9000,
        "description": "overline on z in the Proposition 6.9 calculation",
    },
    "zoom368_zinR.png": {
        "script": "zoom368.py",
        "index": 368,
        "bbox": (0.05, 0.75, 0.452, 0.492),
        "dpi": 8000,
        "description": "membership wording around z alpha j and R",
    },
    "zoom368b_zR.png": {
        "script": "zoom368b.py",
        "index": 368,
        "bbox": (0.38, 0.66, 0.452, 0.492),
        "dpi": 14000,
        "description": "symbol-level z alpha j and R gap inspection",
    },
    "zoom369_p611a.png": {
        "script": "zoom369.py",
        "index": 369,
        "bbox": (0.03, 0.92, 0.508, 0.545),
        "dpi": 6000,
        "description": "Proposition 6.11 first statement line and emphasis",
    },
    "zoom369_p611b.png": {
        "script": "zoom369.py",
        "index": 369,
        "bbox": (0.03, 0.92, 0.615, 0.652),
        "dpi": 6000,
        "description": "Proposition 6.11 second statement line and emphasis",
    },
    "zoom369_primes.png": {
        "script": "zoom369.py",
        "index": 369,
        "bbox": (0.42, 0.78, 0.195, 0.235),
        "dpi": 9000,
        "description": "N prime and N notation in Proposition 6.10 proof",
    },
    "zoom369b_primes.png": {
        "script": "zoom369b.py",
        "index": 369,
        "bbox": (0.38, 0.80, 0.082, 0.118),
        "dpi": 9000,
        "description": "alternate tight prime-mark inspection",
    },
    "zoom370_gdisp.png": {
        "script": "zoom370.py",
        "index": 370,
        "bbox": (0.14, 0.68, 0.688, 0.740),
        "dpi": 8000,
        "description": "displayed overlined gamma expression",
    },
    "zoom370_gtext.png": {
        "script": "zoom370.py",
        "index": 370,
        "bbox": (0.20, 0.72, 0.640, 0.688),
        "dpi": 8000,
        "description": "prose-line overline scope on gamma expression",
    },
    "zoom370b_disp2.png": {
        "script": "zoom370b.py",
        "index": 370,
        "bbox": (0.18, 0.66, 0.680, 0.720),
        "dpi": 11000,
        "description": "tight second displayed overline reconstruction",
    },
    "zoom370b_l8222.png": {
        "script": "zoom370b.py",
        "index": 370,
        "bbox": (0.03, 0.55, 0.740, 0.775),
        "dpi": 9000,
        "description": "line 8222 gamma formula glyph check",
    },
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--scratch-dir", type=Path, required=True)
    parser.add_argument("--script-dir", type=Path, required=True)
    parser.add_argument("--parent-pdf", type=Path, required=True)
    parser.add_argument("--cert-log", type=Path, required=True)
    parser.add_argument("--prior-package-root", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--zip-dir", type=Path, required=True)
    return parser.parse_args()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest().upper()


def utc_mtime(path: Path) -> str:
    return datetime.fromtimestamp(path.stat().st_mtime, timezone.utc).isoformat()


def write_text(path: Path, value: str) -> None:
    path.write_bytes(value.encode("utf-8"))


def write_csv(
    path: Path,
    rows: list[dict[str, object]],
    fields: list[str],
) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def privacy_hits(values: list[str]) -> list[str]:
    joined = "\n".join(values).lower()
    return sorted(marker for marker in PRIVATE_MARKERS if marker in joined)


def sanitize_public_text(value: str) -> str:
    sanitized = re.sub(r"(?i)\bfloris\b", "[archive owner]", value)
    sanitized = re.sub(r"(?i)\b(?:claude|codex)\b", "[agent]", sanitized)
    sanitized = re.sub(
        r"(?i)\b[a-z]:\\(?:[^\\\s,;)\]]+\\)*[^,\r\n;)\]]*",
        "[private path]",
        sanitized,
    )
    return sanitized


def formula_triggers(path: Path) -> list[str]:
    triggers: list[str] = []
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        for row_number, row in enumerate(csv.reader(handle), start=1):
            for column_number, cell in enumerate(row, start=1):
                if cell.startswith(FORMULA_PREFIXES):
                    triggers.append(f"R{row_number}C{column_number}:{cell[:40]}")
    return triggers


def png_metadata(path: Path) -> dict[str, object]:
    Image.MAX_IMAGE_PIXELS = None
    with Image.open(path) as image:
        image.verify()
    with Image.open(path) as image:
        dpi = image.info.get("dpi")
        return {
            "width_px": image.width,
            "height_px": image.height,
            "color_mode": image.mode,
            "embedded_dpi_x": round(float(dpi[0]), 4) if dpi else "",
            "embedded_dpi_y": round(float(dpi[1]), 4) if dpi else "",
            "metadata_text": json.dumps(
                {str(key): str(value) for key, value in image.info.items()},
                sort_keys=True,
                ensure_ascii=True,
            ),
        }


def render_crop(
    document: fitz.Document,
    index: int,
    bbox: tuple[float, float, float, float],
    dpi: int,
    contrast: float,
    sharpness: float,
) -> tuple[Image.Image, bytes]:
    page = document[index]
    rect = page.rect
    fx0, fx1, fy0, fy1 = bbox
    clip = fitz.Rect(
        rect.x0 + rect.width * fx0,
        rect.y0 + rect.height * fy0,
        rect.x0 + rect.width * fx1,
        rect.y0 + rect.height * fy1,
    )
    pixmap = page.get_pixmap(
        matrix=fitz.Matrix(dpi / 72.0, dpi / 72.0),
        clip=clip,
        colorspace=fitz.csGRAY,
    )
    image = Image.frombytes(
        "L",
        [pixmap.width, pixmap.height],
        pixmap.samples,
    )
    image = ImageOps.autocontrast(image, cutoff=1)
    image = ImageEnhance.Contrast(image).enhance(contrast)
    image = ImageEnhance.Sharpness(image).enhance(sharpness)
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    return image, buffer.getvalue()


def pixels_equal(left: Image.Image, right: Image.Image) -> bool:
    return (
        left.mode == right.mode
        and left.size == right.size
        and ImageChops.difference(left, right).getbbox() is None
    )


def selected_audit_lines(cert_bytes: bytes) -> list[str]:
    text = cert_bytes.decode("utf-8", errors="replace")
    selected: list[str] = []
    pattern = re.compile(r"^### #(?P<entry>\d+)\b")
    for line in text.splitlines():
        match = pattern.match(line)
        if match and START_ENTRY <= int(match.group("entry")) <= END_ENTRY:
            selected.append(line)
    return selected


def build_audit_rows(cert_bytes: bytes) -> list[dict[str, object]]:
    selected = selected_audit_lines(cert_bytes)
    rows: list[dict[str, object]] = []
    pattern = re.compile(
        r"^### #(?P<entry>\d+).*?\bidx(?P<idx>\d+)\b",
        re.IGNORECASE,
    )
    footer_pattern = re.compile(
        r"footer\s+[«\"](?P<printed>\d+)[»\"]",
        re.IGNORECASE,
    )
    for line in selected:
        match = pattern.match(line)
        if not match:
            continue
        entry = int(match.group("entry"))
        index = int(match.group("idx"))
        footer = footer_pattern.search(line)
        normalized = sanitize_public_text(re.sub(r"\s+", " ", line).strip())
        if len(normalized) > 1200:
            normalized = normalized[:1197] + "..."
        raw = line.encode("utf-8")
        rows.append(
            {
                "audit_entry_number": entry,
                "parent_pdf_index_0based": index,
                "parent_pdf_page_1based": index + 1,
                "printed_page_from_audit": (
                    int(footer.group("printed")) if footer else index - 13
                ),
                "expose": "V" if index <= 377 else "VI",
                "raw_heading_bytes": len(raw),
                "raw_heading_sha256": sha256_bytes(raw),
                "sanitized_audit_heading": normalized,
            }
        )
    rows.sort(key=lambda row: int(row["audit_entry_number"]))
    return rows


def validate_target_scripts(script_dir: Path) -> list[str]:
    errors: list[str] = []
    by_script: dict[str, list[tuple[str, dict[str, Any]]]] = {}
    for name, spec in TARGET_SPECS.items():
        by_script.setdefault(str(spec["script"]), []).append((name, spec))
    for script_name, outputs in by_script.items():
        path = script_dir / script_name
        if not path.is_file():
            errors.append(f"missing target generator: {script_name}")
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        indices = {int(spec["index"]) for _, spec in outputs}
        if len(indices) != 1:
            errors.append(f"mixed target page indices in {script_name}")
            continue
        index = next(iter(indices))
        if not re.search(rf"\bpg\s*=\s*d\[{index}\]", text):
            errors.append(f"target generator page mismatch: {script_name}")
        if "ImageOps.autocontrast(im, cutoff=1)" not in text:
            errors.append(f"target generator autocontrast mismatch: {script_name}")
        if "ImageEnhance.Contrast(im).enhance(2.0)" not in text:
            errors.append(f"target generator contrast mismatch: {script_name}")
        if "ImageEnhance.Sharpness(im).enhance(1.7)" not in text:
            errors.append(f"target generator sharpness mismatch: {script_name}")
        calls: dict[str, tuple[float, float, float, float, int]] = {}
        for match in re.finditer(
            r'crop\(\s*"(?P<tag>[^"]+)"\s*,'
            r"\s*(?P<fx0>[0-9.]+)\s*,\s*(?P<fx1>[0-9.]+)\s*,"
            r"\s*(?P<fy0>[0-9.]+)\s*,\s*(?P<fy1>[0-9.]+)\s*,"
            r"\s*(?P<dpi>\d+)\s*\)",
            text,
        ):
            calls[match.group("tag")] = (
                float(match.group("fx0")),
                float(match.group("fx1")),
                float(match.group("fy0")),
                float(match.group("fy1")),
                int(match.group("dpi")),
            )
        for _name, spec in outputs:
            fx0, fx1, fy0, fy1 = spec["bbox"]
            tag = Path(_name).stem.split("_", 1)[1]
            expected = (
                float(fx0),
                float(fx1),
                float(fy0),
                float(fy1),
                int(spec["dpi"]),
            )
            if calls.get(tag) != expected:
                errors.append(
                    f"target generator call mismatch: {script_name}:{_name}"
                )
    return errors


def validate_cold_scripts(script_dir: Path) -> list[str]:
    errors: list[str] = []
    for index in range(START_INDEX, END_INDEX + 1):
        path = script_dir / f"cve0p{index}.py"
        if not path.is_file():
            errors.append(f"missing cold generator: {path.name}")
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        if not re.search(rf"\bidx\s*=\s*{index}\b", text):
            errors.append(f"cold generator page mismatch: {path.name}")
        if "ImageOps.autocontrast(im, cutoff=1)" not in text:
            errors.append(f"cold generator autocontrast mismatch: {path.name}")
        if "ImageEnhance.Contrast(im).enhance(1.9)" not in text:
            errors.append(f"cold generator contrast mismatch: {path.name}")
        if "ImageEnhance.Sharpness(im).enhance(1.6)" not in text:
            errors.append(f"cold generator sharpness mismatch: {path.name}")
        calls: dict[str, tuple[float, float, float, float, int]] = {}
        for match in re.finditer(
            r'crop\(\s*"(?P<tag>[^"]+)"\s*,'
            r"\s*(?P<fx0>[0-9.]+)\s*,\s*(?P<fx1>[0-9.]+)\s*,"
            r"\s*(?P<fy0>[0-9.]+)\s*,\s*(?P<fy1>[0-9.]+)\s*,"
            r"\s*(?P<dpi>\d+)\s*\)",
            text,
        ):
            calls[match.group("tag")] = (
                float(match.group("fx0")),
                float(match.group("fx1")),
                float(match.group("fy0")),
                float(match.group("fy1")),
                int(match.group("dpi")),
            )
        for tag, bbox in COLD_BBOXES.items():
            fx0, fx1, fy0, fy1 = bbox
            expected = (
                float(fx0),
                float(fx1),
                float(fy0),
                float(fy1),
                2400,
            )
            if calls.get(tag) != expected:
                errors.append(f"cold generator call mismatch: {path.name}:{tag}")
    return errors


def prior_hashes(root: Path, excluded_dir: Path) -> set[str]:
    values: set[str] = set()
    for path in root.rglob("*.csv"):
        try:
            path.resolve().relative_to(excluded_dir.resolve())
            continue
        except ValueError:
            pass
        try:
            with path.open("r", encoding="utf-8-sig", newline="") as handle:
                for row in csv.DictReader(handle):
                    for key, value in row.items():
                        if key and "sha256" in key.lower():
                            normalized = str(value).strip().upper()
                            if re.fullmatch(r"[0-9A-F]{64}", normalized):
                                values.add(normalized)
        except (OSError, UnicodeError, csv.Error):
            continue
    return values


def add_zip_file(
    archive: zipfile.ZipFile,
    source: Path,
    member: str,
) -> None:
    info = zipfile.ZipInfo(member, date_time=(2026, 7, 24, 0, 0, 0))
    info.compress_type = zipfile.ZIP_STORED
    info.create_system = 3
    info.external_attr = 0o100644 << 16
    archive.writestr(info, source.read_bytes())


def build_zip(
    path: Path,
    image_rows: list[dict[str, object]],
    scratch_dir: Path,
    metadata_paths: list[Path],
) -> dict[str, object]:
    expected: dict[str, tuple[int, str]] = {}
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_STORED) as archive:
        for row in image_rows:
            source = scratch_dir / str(row["source_basename"])
            member = str(row["archive_path"])
            add_zip_file(archive, source, member)
            expected[member] = (source.stat().st_size, sha256(source))
        for source in metadata_paths:
            member = f"metadata/{source.name}"
            add_zip_file(archive, source, member)
            expected[member] = (source.stat().st_size, sha256(source))

    errors: list[str] = []
    members: list[dict[str, object]] = []
    with zipfile.ZipFile(path) as archive:
        bad = archive.testzip()
        if bad:
            errors.append(f"bad CRC member: {bad}")
        names = archive.namelist()
        if len(names) != len(set(names)):
            errors.append("duplicate ZIP member")
        if set(names) != set(expected):
            errors.append(
                "ZIP exact-set mismatch: "
                f"missing={sorted(set(expected)-set(names))}; "
                f"extra={sorted(set(names)-set(expected))}"
            )
        for info in archive.infolist():
            name = info.filename
            unsafe = (
                name.startswith("/")
                or name.startswith("\\")
                or re.match(r"^[A-Za-z]:", name) is not None
                or ".." in Path(name).parts
            )
            if unsafe:
                errors.append(f"unsafe ZIP member: {name}")
                continue
            data = archive.read(name)
            observed = (len(data), sha256_bytes(data))
            if name in expected and observed != expected[name]:
                errors.append(f"ZIP member identity mismatch: {name}")
            members.append(
                {
                    "path": name,
                    "bytes": len(data),
                    "sha256": sha256_bytes(data),
                }
            )
    members.sort(key=lambda row: str(row["path"]).lower())
    return {
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "members": len(members),
        "member_bytes": sum(int(row["bytes"]) for row in members),
        "member_identity_aggregate_sha256": sha256_bytes(
            "".join(
                f"{row['path']}\t{row['bytes']}\t{row['sha256']}\n"
                for row in members
            ).encode("utf-8")
        ),
    }


def main() -> int:
    args = parse_args()
    scratch_dir = args.scratch_dir.resolve()
    script_dir = args.script_dir.resolve()
    parent_pdf = args.parent_pdf.resolve()
    cert_log = args.cert_log.resolve()
    prior_root = args.prior_package_root.resolve()
    output_dir = args.output_dir.resolve()
    zip_dir = args.zip_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    zip_dir.mkdir(parents=True, exist_ok=True)

    errors: list[str] = []
    Image.MAX_IMAGE_PIXELS = None

    if (
        not parent_pdf.is_file()
        or parent_pdf.stat().st_size != PARENT_BYTES
        or sha256(parent_pdf) != PARENT_SHA256
    ):
        errors.append("parent PDF identity mismatch")
    document = fitz.open(parent_pdf)
    if document.page_count != PARENT_PAGES:
        errors.append(f"parent page count is {document.page_count}, expected 720")

    cert_bytes = cert_log.read_bytes()
    cert_sha = sha256_bytes(cert_bytes)
    raw_selected = selected_audit_lines(cert_bytes)
    raw_selected_bytes = "\n".join(raw_selected).encode("utf-8")
    raw_selected_sha = sha256_bytes(raw_selected_bytes)
    if len(raw_selected) != 17:
        errors.append(f"selected audit rows are {len(raw_selected)}, expected 17")
    if raw_selected_sha != SELECTED_RAW_AUDIT_SHA256:
        errors.append(
            "selected audit heading aggregate mismatch: "
            f"{raw_selected_sha} != {SELECTED_RAW_AUDIT_SHA256}"
        )
    audit_rows = build_audit_rows(cert_bytes)
    expected_pairs = {
        (entry, START_INDEX + entry - START_ENTRY)
        for entry in range(START_ENTRY, END_ENTRY + 1)
    }
    observed_pairs = {
        (int(row["audit_entry_number"]), int(row["parent_pdf_index_0based"]))
        for row in audit_rows
    }
    if observed_pairs != expected_pairs:
        errors.append(
            "audit entry/index mapping mismatch: "
            f"missing={sorted(expected_pairs-observed_pairs)}; "
            f"extra={sorted(observed_pairs-expected_pairs)}"
        )
    audit_by_index = {
        int(row["parent_pdf_index_0based"]): row for row in audit_rows
    }

    errors.extend(validate_target_scripts(script_dir))
    errors.extend(validate_cold_scripts(script_dir))

    expected_target_names = set(TARGET_SPECS)
    expected_band_names = {
        f"cve0p{index}_{tag}.png"
        for index in range(START_INDEX, END_INDEX + 1)
        for tag in COLD_BBOXES
    }
    source_paths = [
        scratch_dir / name
        for name in sorted(expected_target_names | expected_band_names)
    ]
    generator_paths = [
        script_dir / name
        for name in sorted(
            {str(spec["script"]) for spec in TARGET_SPECS.values()}
            | {f"cve0p{index}.py" for index in range(START_INDEX, END_INDEX + 1)}
        )
    ]
    initial_identities: dict[Path, tuple[int, int, str]] = {}
    for path in source_paths + generator_paths:
        if not path.is_file():
            errors.append(f"missing frozen input: {path.name}")
            continue
        stat = path.stat()
        initial_identities[path] = (stat.st_size, stat.st_mtime_ns, sha256(path))

    previous_hashes = prior_hashes(prior_root, output_dir)
    target_rows: list[dict[str, object]] = []
    blocked_rows: list[dict[str, object]] = []
    replay: dict[str, dict[str, object]] = {}
    target_hashes: set[str] = set()

    for name in sorted(TARGET_SPECS, key=str.lower):
        spec = TARGET_SPECS[name]
        image_path = scratch_dir / name
        if not image_path.is_file():
            continue
        replay_image, replay_bytes = render_crop(
            document,
            int(spec["index"]),
            tuple(spec["bbox"]),
            int(spec["dpi"]),
            2.0,
            1.7,
        )
        with Image.open(image_path) as source:
            source_image = source.convert("L")
            pixel_exact = pixels_equal(replay_image, source_image)
        byte_exact = replay_bytes == image_path.read_bytes()
        if not pixel_exact:
            errors.append(f"target pixel replay mismatch: {name}")
        if not byte_exact:
            errors.append(f"target PNG byte replay mismatch: {name}")
        digest = sha256(image_path)
        if digest in target_hashes:
            errors.append(f"duplicate targeted image content: {name}")
        target_hashes.add(digest)
        if digest in previous_hashes:
            errors.append(f"target hash already represented publicly: {name}")
        meta = png_metadata(image_path)
        hits = privacy_hits([name, str(meta["metadata_text"])])
        if hits:
            errors.append(f"target PNG privacy hit {name}: {hits}")
        index = int(spec["index"])
        generator = script_dir / str(spec["script"])
        fx0, fx1, fy0, fy1 = spec["bbox"]
        audit = audit_by_index[index]
        target_rows.append(
            {
                "archive_path": f"images/targeted_ultradetail/{name}",
                "source_basename": name,
                "bytes": image_path.stat().st_size,
                "sha256": digest,
                "width_px": meta["width_px"],
                "height_px": meta["height_px"],
                "color_mode": meta["color_mode"],
                "embedded_dpi_x": meta["embedded_dpi_x"],
                "embedded_dpi_y": meta["embedded_dpi_y"],
                "modified_utc": utc_mtime(image_path),
                "category": "targeted_symbol_formula_ultradetail_crop",
                "public_disposition": (
                    "public_targeted_source_audit_evidence_no_license_grant"
                ),
                "parent_pdf_index_0based": index,
                "parent_pdf_page_1based": index + 1,
                "printed_page_from_audit": audit["printed_page_from_audit"],
                "expose": audit["expose"],
                "linked_tex_object": LINKED_TEX_OBJECT,
                "linked_audit_entry": audit["audit_entry_number"],
                "generator_script_basename": generator.name,
                "generator_script_bytes": generator.stat().st_size,
                "generator_script_sha256": sha256(generator),
                "generator_script_modified_utc": utc_mtime(generator),
                "bbox_coordinate_system": "fraction_of_parent_page",
                "bbox_fx0": fx0,
                "bbox_fy0": fy0,
                "bbox_fx1": fx1,
                "bbox_fy1": fy1,
                "render_dpi": spec["dpi"],
                "processing_profile": (
                    "grayscale;autocontrast_cutoff_1;contrast_2.0;"
                    "sharpness_1.7"
                ),
                "description": spec["description"],
                "replay_disposition": "pixel_exact_and_png_byte_exact",
                "qa_disposition": (
                    "used_in_cold_source_reverification_not_translation_"
                    "certification"
                ),
                "parent_scan_sha256": PARENT_SHA256,
            }
        )
        replay[name] = {
            "pixel_exact": pixel_exact,
            "png_byte_exact": byte_exact,
            "replay_sha256": sha256_bytes(replay_bytes),
        }

    for index in range(START_INDEX, END_INDEX + 1):
        generator = script_dir / f"cve0p{index}.py"
        audit = audit_by_index[index]
        for tag, bbox in COLD_BBOXES.items():
            name = f"cve0p{index}_{tag}.png"
            image_path = scratch_dir / name
            if not image_path.is_file():
                continue
            replay_image, replay_bytes = render_crop(
                document,
                index,
                bbox,
                2400,
                1.9,
                1.6,
            )
            with Image.open(image_path) as source:
                source_image = source.convert("L")
                pixel_exact = pixels_equal(replay_image, source_image)
            byte_exact = replay_bytes == image_path.read_bytes()
            if not pixel_exact:
                errors.append(f"page-band pixel replay mismatch: {name}")
            if not byte_exact:
                errors.append(f"page-band PNG byte replay mismatch: {name}")
            meta = png_metadata(image_path)
            hits = privacy_hits([name, str(meta["metadata_text"])])
            if hits:
                errors.append(f"page-band PNG privacy hit {name}: {hits}")
            fx0, fx1, fy0, fy1 = bbox
            blocked_rows.append(
                {
                    "archive_path": "",
                    "source_basename": name,
                    "bytes": image_path.stat().st_size,
                    "sha256": sha256(image_path),
                    "width_px": meta["width_px"],
                    "height_px": meta["height_px"],
                    "color_mode": meta["color_mode"],
                    "embedded_dpi_x": meta["embedded_dpi_x"],
                    "embedded_dpi_y": meta["embedded_dpi_y"],
                    "modified_utc": utc_mtime(image_path),
                    "category": "routine_full_width_page_band_derivative",
                    "public_disposition": "rights_blocked_not_public",
                    "parent_pdf_index_0based": index,
                    "parent_pdf_page_1based": index + 1,
                    "printed_page_from_audit": audit[
                        "printed_page_from_audit"
                    ],
                    "expose": audit["expose"],
                    "linked_tex_object": LINKED_TEX_OBJECT,
                    "linked_audit_entry": audit["audit_entry_number"],
                    "generator_script_basename": generator.name,
                    "generator_script_bytes": generator.stat().st_size,
                    "generator_script_sha256": sha256(generator),
                    "generator_script_modified_utc": utc_mtime(generator),
                    "bbox_coordinate_system": "fraction_of_parent_page",
                    "bbox_fx0": fx0,
                    "bbox_fy0": fy0,
                    "bbox_fx1": fx1,
                    "bbox_fy1": fy1,
                    "render_dpi": 2400,
                    "processing_profile": (
                        "grayscale;autocontrast_cutoff_1;contrast_1.9;"
                        "sharpness_1.6"
                    ),
                    "replay_disposition": "pixel_exact_and_png_byte_exact",
                    "qa_disposition": (
                        "used_in_cold_source_reverification_pixels_withheld_"
                        "for_rights"
                    ),
                    "parent_scan_sha256": PARENT_SHA256,
                }
            )
            replay[name] = {
                "pixel_exact": pixel_exact,
                "png_byte_exact": byte_exact,
                "replay_sha256": sha256_bytes(replay_bytes),
            }

    if len(target_rows) != 15:
        errors.append(f"target row count is {len(target_rows)}, expected 15")
    if len(blocked_rows) != 85:
        errors.append(f"blocked row count is {len(blocked_rows)}, expected 85")

    target_manifest = output_dir / TARGET_MANIFEST_NAME
    blocked_manifest = output_dir / BLOCKED_MANIFEST_NAME
    audit_context = output_dir / AUDIT_CONTEXT_NAME
    write_csv(
        target_manifest,
        target_rows,
        list(target_rows[0]) if target_rows else [],
    )
    write_csv(
        blocked_manifest,
        blocked_rows,
        list(blocked_rows[0]) if blocked_rows else [],
    )
    write_csv(
        audit_context,
        audit_rows,
        list(audit_rows[0]) if audit_rows else [],
    )

    parent_identity = {
        "title": "Theorie des intersections et theoreme de Riemann-Roch",
        "series_context": "SGA 6 source-audit parent reader",
        "source_file_basename": parent_pdf.name,
        "bytes": parent_pdf.stat().st_size,
        "sha256": PARENT_SHA256,
        "pages": document.page_count,
        "pdf_metadata": document.metadata,
        "rotation": 0,
        "parent_scan_not_duplicated_in_this_release": True,
        "rights_status": (
            "Underlying French work and scan rights remain with their holders. "
            "No blanket license or rights transfer is asserted."
        ),
        "crop_publication_policy": (
            "Only 15 tight scholarly symbol/formula verification crops are "
            "included. Eighty-five full-width page-band derivatives are "
            "hash-manifested as rights-blocked; their pixels are not "
            "redistributed."
        ),
        "render_resolution_caveat": (
            "Render DPI describes computational rasterization, not new "
            "optical detail beyond the parent scan."
        ),
        "cert_log_basename": cert_log.name,
        "cert_log_bytes_at_packaging_snapshot": len(cert_bytes),
        "cert_log_sha256_at_packaging_snapshot": cert_sha,
        "cert_log_known_sha256_when_entry_1130_was_latest": (
            KNOWN_CERT_LOG_SHA256_AT_ENTRY_1130
        ),
        "selected_audit_entries": {
            "first": START_ENTRY,
            "last": END_ENTRY,
            "count": len(audit_rows),
            "raw_heading_aggregate_sha256_no_terminal_lf": raw_selected_sha,
        },
        "represented_parent_pdf_indices": {
            "distinct_indices": END_INDEX - START_INDEX + 1,
            "minimum_index_0based": START_INDEX,
            "maximum_index_0based": END_INDEX,
            "continuous_source_translation_coverage_claimed": False,
        },
    }
    parent_path = output_dir / PARENT_NAME
    write_text(
        parent_path,
        json.dumps(parent_identity, indent=2, ensure_ascii=True) + "\n",
    )

    counts = Counter(
        int(row["parent_pdf_index_0based"]) for row in target_rows
    )
    count_text = ", ".join(
        f"idx{index}: {counts[index]}" for index in sorted(counts)
    )
    readme = f"""# SGA6 targeted ultra-detail source-audit crops, indices 362-378

This no-overwrite release preserves the tight symbol, formula, prime-mark,
overline, inequality, and emphasis crops actually generated and read during
the SGA6 cold source re-verification through audit entry #{END_ENTRY}. It does
not include work beginning at idx379.

## Public image archive

- `{TARGET_ZIP}` contains {len(target_rows)} targeted images /
  {sum(int(row['bytes']) for row in target_rows):,} image bytes.
- Per-index image counts: {count_text}.
- Computational render resolutions range from 6,000 to 14,000 DPI.
- Every image replays pixel-for-pixel and PNG-byte-for-PNG-byte from the exact
  parent PDF using the recorded fractional page box, generator identity, and
  enhancement profile.

The targeted checks concern strict inequalities, lambda and gamma notation,
prime marks, overlines, membership wording, and formal-statement emphasis in
Exposé V §§6.6-6.11. Filenames are historical working names; the manifest is
the controlling locator.

## Rights-blocked page bands

`{BLOCKED_MANIFEST_NAME}` records {len(blocked_rows)} full-width 2,400-DPI page
bands / {sum(int(row['bytes']) for row in blocked_rows):,} bytes across
idx362-378. Their exact hashes, dimensions, page mappings, fractional boxes,
generator identities, and audit dispositions are public, but their pixels are
not redistributed. `{METADATA_ZIP}` groups this provenance surface.

## Boundary and claims

The selected audit boundary is entries #{START_ENTRY}-#{END_ENTRY}, mapping
one-to-one to idx{START_INDEX}-idx{END_INDEX}. Entries through idx377 close
Exposé V; idx378 is the first page of Exposé VI. This image package is
provenance and QA evidence only. It does not certify the French transcription,
English translation, mathematics, completeness, or critical-edition status.

The parent is the 720-page reader `{parent_pdf.name}`, {PARENT_BYTES:,} bytes,
SHA-256 `{PARENT_SHA256}`. The parent PDF is not bundled. Underlying French
work and scan rights remain with their holders. No blanket license or rights
transfer is asserted.
"""
    readme_path = output_dir / README_NAME
    write_text(readme_path, readme)

    metadata_paths = [
        readme_path,
        parent_path,
        target_manifest,
        blocked_manifest,
        audit_context,
    ]
    metadata_privacy: dict[str, list[str]] = {}
    for path in metadata_paths:
        hits = privacy_hits(
            [path.read_text(encoding="utf-8", errors="replace")]
        )
        if hits:
            metadata_privacy[path.name] = hits
    if metadata_privacy:
        errors.append(f"generated metadata privacy hits: {metadata_privacy}")

    formula_errors = {
        path.name: formula_triggers(path)
        for path in (target_manifest, blocked_manifest, audit_context)
    }
    for name, triggers in formula_errors.items():
        if triggers:
            errors.append(f"formula-trigger cells in {name}: {triggers}")

    target_zip_path = zip_dir / TARGET_ZIP
    metadata_zip_path = zip_dir / METADATA_ZIP
    target_zip_result = build_zip(
        target_zip_path,
        target_rows,
        scratch_dir,
        [readme_path, parent_path, target_manifest, audit_context],
    )
    metadata_zip_result = build_zip(
        metadata_zip_path,
        [],
        scratch_dir,
        metadata_paths,
    )
    errors.extend(str(error) for error in target_zip_result["errors"])
    errors.extend(str(error) for error in metadata_zip_result["errors"])

    race_errors: list[str] = []
    for path, initial in initial_identities.items():
        if not path.is_file():
            race_errors.append(f"frozen input disappeared: {path.name}")
            continue
        stat = path.stat()
        current = (stat.st_size, stat.st_mtime_ns, sha256(path))
        if current != initial:
            race_errors.append(f"frozen input changed: {path.name}")
    final_selected = "\n".join(
        selected_audit_lines(cert_log.read_bytes())
    ).encode("utf-8")
    if sha256_bytes(final_selected) != SELECTED_RAW_AUDIT_SHA256:
        race_errors.append("selected audit boundary changed during packaging")
    errors.extend(race_errors)

    validation = {
        "schema": "sga6_targeted_ultradetail_idx362_378_validation_v1",
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "selection": {
            "targeted_public_images": len(target_rows),
            "targeted_public_bytes": sum(
                int(row["bytes"]) for row in target_rows
            ),
            "rights_blocked_page_bands": len(blocked_rows),
            "rights_blocked_page_band_bytes": sum(
                int(row["bytes"]) for row in blocked_rows
            ),
            "parent_indices": list(range(START_INDEX, END_INDEX + 1)),
            "audit_entries": list(range(START_ENTRY, END_ENTRY + 1)),
        },
        "authority": {
            "parent_pdf_bytes": parent_pdf.stat().st_size,
            "parent_pdf_sha256": sha256(parent_pdf),
            "parent_pdf_pages": document.page_count,
            "selected_audit_heading_rows": len(audit_rows),
            "selected_audit_heading_bytes": len(raw_selected_bytes),
            "selected_audit_heading_aggregate_sha256": raw_selected_sha,
            "full_cert_log_bytes_at_packaging_snapshot": len(cert_bytes),
            "full_cert_log_sha256_at_packaging_snapshot": cert_sha,
        },
        "replay": {
            "files": len(replay),
            "pixel_exact": sum(
                bool(item["pixel_exact"]) for item in replay.values()
            ),
            "png_byte_exact": sum(
                bool(item["png_byte_exact"]) for item in replay.values()
            ),
            "details": replay,
        },
        "prior_public_hash_check": {
            "prior_sha256_values_loaded": len(previous_hashes),
            "target_hash_intersection": sorted(target_hashes & previous_hashes),
        },
        "privacy": {
            "generated_metadata_hits": metadata_privacy,
        },
        "csv_formula_safety": formula_errors,
        "source_freeze": {
            "input_files": len(initial_identities),
            "race_errors": race_errors,
        },
        "zip_validation": {
            TARGET_ZIP: target_zip_result,
            METADATA_ZIP: metadata_zip_result,
        },
    }
    validation_path = output_dir / VALIDATION_NAME
    write_text(
        validation_path,
        json.dumps(validation, indent=2, ensure_ascii=True) + "\n",
    )

    upload_rows = [
        {
            "filename": target_zip_path.name,
            "bytes": target_zip_path.stat().st_size,
            "sha256": sha256(target_zip_path),
            "role": "targeted_ultradetail_image_archive",
            "status": "proposed_public",
        },
        {
            "filename": metadata_zip_path.name,
            "bytes": metadata_zip_path.stat().st_size,
            "sha256": sha256(metadata_zip_path),
            "role": "provenance_and_rights_blocked_metadata_archive",
            "status": "proposed_public",
        },
    ]
    upload_manifest = output_dir / UPLOAD_MANIFEST_NAME
    write_csv(
        upload_manifest,
        upload_rows,
        ["filename", "bytes", "sha256", "role", "status"],
    )

    checksum_paths = metadata_paths + [validation_path, upload_manifest]
    checksum_lines = [
        f"{sha256(path)}  {path.name}" for path in checksum_paths
    ]
    checksum_path = output_dir / SHA_NAME
    write_text(checksum_path, "\n".join(checksum_lines) + "\n")

    summary = {
        "status": validation["status"],
        "errors": errors,
        "targeted_images": len(target_rows),
        "rights_blocked_bands": len(blocked_rows),
        "target_zip": {
            "path": target_zip_path.name,
            "bytes": target_zip_path.stat().st_size,
            "sha256": sha256(target_zip_path),
            **target_zip_result,
        },
        "metadata_zip": {
            "path": metadata_zip_path.name,
            "bytes": metadata_zip_path.stat().st_size,
            "sha256": sha256(metadata_zip_path),
            **metadata_zip_result,
        },
        "validation": {
            "path": validation_path.name,
            "bytes": validation_path.stat().st_size,
            "sha256": sha256(validation_path),
        },
        "upload_manifest": {
            "path": upload_manifest.name,
            "bytes": upload_manifest.stat().st_size,
            "sha256": sha256(upload_manifest),
        },
    }
    print(json.dumps(summary, indent=2))
    document.close()
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
