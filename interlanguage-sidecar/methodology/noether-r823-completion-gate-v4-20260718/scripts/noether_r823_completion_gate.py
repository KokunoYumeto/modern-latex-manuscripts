#!/usr/bin/env python3
"""Reject incomplete French/Spanish R823 cumulative editions.

This is an evidence gate, not a linguistic-quality oracle.  It verifies that a
candidate has the complete declared R823 scope, a current successful PDF build,
unit-level source-reconciliation evidence, a terminology ledger, and visual-QA
records.  Semantic accuracy and native-language quality still require review.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import subprocess
import sys
import tempfile
from collections import Counter
from dataclasses import dataclass, asdict
from datetime import datetime
from pathlib import Path

from noether_r823_book_structure_audit import audit as audit_book_structure
from noether_r823_paper_structure_audit import audit as audit_paper_structure
from noether_r823_source_unit_manifest import build as build_source_units
from noether_r823_target_unit_manifest import (
    MARKERS,
    build as build_target_units,
    expand_tex,
    locate_any,
)
from noether_sync_audit import mask_tex_comments, slice_papers


R823_TEX_SHA256 = "EE8955BCF7A263917BE57DBC8F682601550CDCB5260D02CA6D486C6A6DFD4F21"
CANONICAL_PROMOTER_SHA256 = "E53C8335BA7EABE5D75EAF3BD75DCEC93CE773B343EDA0BA8442DDACE83A6BC4"
PAPER_MARKER = re.compile(
    r"(?:\{\\Large\\bfseries\s*|\\section\*\{\s*)(\d{1,2})\.\s*",
    re.MULTILINE,
)
PLACEHOLDER = re.compile(
    r"\b(?:TODO|TBD|FIXME|UNTRANSLATED|TRANSLATE[ _-]?ME|PLACEHOLDER)\b|"
    r"(?i:\[\s*(?:translation pending|traduction à faire|traducción pendiente)\s*\])",
)
FATAL_LOG = re.compile(
    r"(?:^! LaTeX Error:|^! Emergency stop\.|Fatal error occurred|"
    r"^! Undefined control sequence\.|no output PDF file produced|"
    r"TeX capacity exceeded|LaTeX Warning: There were undefined references|"
    r"Missing character: There is no|Overfull \\hbox)",
    re.IGNORECASE | re.MULTILINE,
)
BROKEN_TEX_TOKEN = re.compile(r"(?<![\\A-Za-z])(?:qquad|quad)\b")
HEX64 = re.compile(r"^[0-9a-fA-F]{64}$")
STRONG_AUTHORITY_LOCATOR = re.compile(
    r"(?:(?:Noether_R823_cum_de|cum_de)\.tex|"
    r"(?:R823\s+authority|authority\s+R823|autorité\s+R823|"
    r"German\s+authority|autorité\s+allemande))"
    r"[^\n;]{0,180}(?:(?:lines?|lignes?|ligne|l\.?)[\s:]?\d+|:\d+)",
    re.IGNORECASE,
)
STRONG_NATIVE_PAGE_LOCATOR = re.compile(
    r"(?:\.pdf|Numdam|Bourbaki|SGA|SMF|EGA|Annales|doi\b|https?://|ISBN)"
    r"[^\n;]{0,220}\bpp?\.?\s*\d+"
    r"|\bpp?\.?\s*\d+[^\n;]{0,220}"
    r"(?:\.pdf|Numdam|Bourbaki|SGA|SMF|EGA|Annales|doi\b|https?://|ISBN)",
    re.IGNORECASE,
)
STRONG_NATIVE_TEX_LOCATOR = re.compile(
    r"[^;\n]{1,1000}\.tex:\d+(?:-\d+)?\s*;\s*"
    r"sha256=[0-9a-fA-F]{64}\b",
    re.IGNORECASE,
)
TARGET_TEX_LOCATOR = re.compile(
    r"(?:R823_(?:FR|ES)|working[\\/](?:r823_fr|french_canon)|"
    r"[\\/]work[\\/]spanish(?:[\\/]|$)|"
    r"(?:^|[\\/\s])N\d[^;\n]*_fr(?:_body)?\.tex|"
    r"book_[^;\n]*_(?:fr|es)\.tex|paper\d+[^;\n]*_es[^;\n]*\.tex|"
    r"kapferer_noether_fr\.tex|terminal_matter_fr\.tex|"
    r"cum_(?:fr|es)[^;\n]*\.tex)",
    re.IGNORECASE,
)
BUILD_SUCCESS = re.compile(
    r"^Output written on\s+(.+?\.(?:pdf|xdv))\s+\((\d+)\s+pages?[,)]",
    re.IGNORECASE | re.MULTILINE,
)
LOCAL_BUILD_SUFFIXES = {
    ".tex",
    ".sty",
    ".cls",
    ".cfg",
    ".bib",
    ".bst",
    ".png",
    ".jpg",
    ".jpeg",
    ".pdf",
    ".eps",
    ".svg",
}
RENDER_IMAGE_SUFFIXES = {
    ".png",
    ".ppm",
    ".pgm",
    ".jpg",
    ".jpeg",
    ".tif",
    ".tiff",
}
EVIDENCE_MAP_FIELDS = {
    "unit_id",
    "evidence_path",
    "evidence_record",
    "review_scope",
    "notes",
}
UNIT_EVIDENCE_FIELDS = {
    "unit_id",
    "source_sha256",
    "target_sha256",
    "target_document_sha256",
    "source_locator",
    "target_locator",
    "method",
    "reviewed_structures",
    "reviewed_formulas",
    "reviewed_notes",
    "findings",
    "reviewer_provenance",
    "supporting_artifacts",
    "supporting_artifact_sha256",
    "status",
}
RENDER_MANIFEST_FIELDS = {
    "page",
    "render_path",
    "sha256",
    "pdf_sha256",
    "renderer",
}
PINNED_RENDER_DPI = 120
PINNED_RENDER_PROFILE = (
    "Poppler pdftoppm sequential full-document render at 120 dpi"
)
VISUAL_REVIEW_SCHEMA = "noether-r823-visual-review-v1"
VISUAL_REVIEW_FIELDS = {
    "schema",
    "status",
    "language",
    "reviewer_provenance",
    "reviewed_at",
    "pdf_sha256",
    "target_document_sha256",
    "page_count",
    "render_profile",
    "pdftoppm_sha256",
    "reviewed_pages",
    "baseline_kind",
    "baseline_render_manifest",
    "baseline_render_manifest_sha256",
    "baseline_pixel_binding_sha256",
    "review_method",
    "findings",
}

REQUIRED_UNITS = (
    tuple(f"P{number:02d}" for number in range(1, 44))
    + ("BOOK_TITLE_INTRO",)
    + tuple(f"BOOK_S{number:02d}" for number in range(1, 32))
    + (
        "POST45_MAIN",
        "POST45_NOETHER_SUPPLEMENT",
        "BIBLIOGRAPHY",
        "SHORT_NOTICES",
        "BOOK_REVIEWS",
        "BOOKS_WITH_NOETHER",
    )
)

LANGUAGE_MARKERS = {
    "spanish": {
        "book": ("Álgebra de las magnitudes hipercomplejas", "Álgebra de las grandezas hipercomplejas", "Álgebra de las cantidades hipercomplejas"),
        "post45": (
            "Condiciones de multiplicidad necesarias y suficientes",
            "Condiciones necesarias y suficientes de multiplicidad",
        ),
        "bibliography": ("Bibliografía",),
        "terminal": ("Lista de comunicaciones", "Lista de notas breves", "Reseñas de libros"),
    },
    "french": {
        "book": ("Algèbre des grandeurs hypercomplexes",),
        "post45": (
            "Conditions de multiplicité nécessaires et suffisantes",
            "Conditions nécessaires et suffisantes de multiplicité",
        ),
        "bibliography": ("Bibliographie",),
        "terminal": ("Liste des communications", "Liste des notices", "Comptes rendus", "Recensions"),
    },
}


@dataclass
class Check:
    name: str
    passed: bool
    detail: str


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def text_sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest().upper()


def fingerprint(path: Path) -> tuple[int, int, str]:
    stat = path.stat()
    return stat.st_mtime_ns, stat.st_size, sha256(path)


def read_utf8(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="strict")


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def normalized_status(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.strip().lower()).strip("-")


def contains_any(text: str, choices: tuple[str, ...]) -> bool:
    folded = text.casefold()
    return any(choice.casefold() in folded for choice in choices)


def pdf_pages(path: Path) -> int:
    try:
        from pypdf import PdfReader  # type: ignore
    except ImportError as exc:  # pragma: no cover - environment failure
        raise RuntimeError("pypdf is required to count candidate PDF pages") from exc
    return len(PdfReader(str(path)).pages)


def parse_fls(path: Path) -> tuple[Path, set[Path], set[Path], list[str]]:
    """Return recorder PWD, inputs, outputs, and parse warnings."""
    text = read_utf8(path)
    pwd_lines = [line[4:].strip() for line in text.splitlines() if line.startswith("PWD ")]
    warnings: list[str] = []
    if len(pwd_lines) != 1:
        warnings.append(f"expected exactly one PWD line, found {len(pwd_lines)}")
        pwd = path.parent.resolve()
    else:
        raw_pwd = Path(pwd_lines[0])
        pwd = raw_pwd.resolve() if raw_pwd.is_absolute() else (path.parent / raw_pwd).resolve()

    def resolve_record(raw: str) -> Path:
        candidate = Path(raw.strip().strip('"'))
        return candidate.resolve() if candidate.is_absolute() else (pwd / candidate).resolve()

    inputs = {
        resolve_record(line[6:])
        for line in text.splitlines()
        if line.startswith("INPUT ") and line[6:].strip()
    }
    outputs = {
        resolve_record(line[7:])
        for line in text.splitlines()
        if line.startswith("OUTPUT ") and line[7:].strip()
    }
    if not inputs:
        warnings.append("no INPUT records")
    if not outputs:
        warnings.append("no OUTPUT records")
    return pwd, inputs, outputs, warnings


def is_within(path: Path, directory: Path) -> bool:
    try:
        path.resolve().relative_to(directory.resolve())
        return True
    except ValueError:
        return False


def evidence_path_exists(raw: str, ledger: Path) -> bool:
    value = raw.strip().strip('"')
    if not value:
        return False
    candidate = Path(value)
    if not candidate.is_absolute():
        candidate = ledger.parent / candidate
    return candidate.exists()


def page_spec_numbers(value: str) -> tuple[list[int], list[tuple[int, int]]]:
    ranges = [
        (int(match.group(1)), int(match.group(2)))
        for match in re.finditer(r"(?<!\d)(\d+)\s*[-–—]\s*(\d+)(?!\d)", value)
    ]
    singles = [int(number) for number in re.findall(r"(?<!\d)(\d+)(?!\d)", value)]
    return singles, ranges


def resolve_evidence_path(raw: str, anchor: Path) -> Path:
    candidate = Path(raw.strip().strip('"'))
    return candidate.resolve() if candidate.is_absolute() else (anchor / candidate).resolve()


def keyed_by_unit(rows: list[dict[str, str]], label: str) -> dict[str, dict[str, str]]:
    result: dict[str, dict[str, str]] = {}
    for row in rows:
        unit = row.get("unit_id", "").strip()
        if not unit:
            raise ValueError(f"{label}: blank unit_id")
        if unit in result:
            raise ValueError(f"{label}: duplicate unit_id {unit}")
        result[unit] = row
    return result


def bind_unit_evidence(
    evidence_map_path: Path,
    required_support_path: Path | None = None,
) -> tuple[set[Path], int, int, list[str]]:
    """Dereference all 81 direct records and rehash every supporting artifact."""
    bound_files: set[Path] = {evidence_map_path.resolve()}
    errors: list[str] = []
    try:
        map_rows = read_csv(evidence_map_path)
        map_columns = set(map_rows[0]) if map_rows else set()
        if not EVIDENCE_MAP_FIELDS <= map_columns:
            errors.append(
                "evidence map missing columns "
                f"{sorted(EVIDENCE_MAP_FIELDS - map_columns)}"
            )
        map_by_unit = keyed_by_unit(map_rows, "evidence map")
    except Exception as exc:
        return bound_files, 0, 0, [str(exc)]

    required = set(REQUIRED_UNITS)
    if len(map_rows) != len(REQUIRED_UNITS) or set(map_by_unit) != required:
        errors.append(
            f"evidence map rows={len(map_rows)}; "
            f"missing={sorted(required - set(map_by_unit))}; "
            f"extra={sorted(set(map_by_unit) - required)}"
        )

    corpus_cache: dict[Path, dict[str, dict[str, str]]] = {}
    record_count = 0
    support_files: set[Path] = set()
    required_support = (
        required_support_path.resolve() if required_support_path is not None else None
    )
    for unit in REQUIRED_UNITS:
        mapping = map_by_unit.get(unit)
        if mapping is None:
            continue
        raw_evidence = mapping.get("evidence_path", "").strip()
        record_id = mapping.get("evidence_record", "").strip()
        if not raw_evidence or record_id != unit:
            errors.append(
                f"{unit}: evidence_path blank or evidence_record not exact unit id"
            )
            continue
        evidence_path = resolve_evidence_path(raw_evidence, evidence_map_path.parent)
        if not evidence_path.is_file() or evidence_path.suffix.casefold() != ".csv":
            errors.append(f"{unit}: direct evidence is not a live CSV: {evidence_path}")
            continue
        bound_files.add(evidence_path)
        if evidence_path not in corpus_cache:
            try:
                rows = read_csv(evidence_path)
                columns = set(rows[0]) if rows else set()
                if not UNIT_EVIDENCE_FIELDS <= columns:
                    raise ValueError(
                        "missing columns "
                        f"{sorted(UNIT_EVIDENCE_FIELDS - columns)}"
                    )
                corpus_cache[evidence_path] = keyed_by_unit(
                    rows, f"unit evidence {evidence_path}"
                )
            except Exception as exc:
                errors.append(f"{unit}: cannot read direct evidence: {exc}")
                continue
        evidence_row = corpus_cache[evidence_path].get(record_id)
        if evidence_row is None:
            errors.append(f"{unit}: direct evidence record is absent")
            continue
        record_count += 1
        artifact_values = [
            value.strip()
            for value in evidence_row.get("supporting_artifacts", "").split(";")
            if value.strip()
        ]
        artifact_hashes = [
            value.strip().upper()
            for value in evidence_row.get("supporting_artifact_sha256", "").split(";")
            if value.strip()
        ]
        if not artifact_values or len(artifact_values) != len(artifact_hashes):
            errors.append(f"{unit}: supporting artifact path/hash count mismatch")
            continue
        artifact_paths = [
            resolve_evidence_path(raw_artifact, evidence_path.parent)
            for raw_artifact in artifact_values
        ]
        if required_support is not None and required_support not in artifact_paths:
            errors.append(
                f"{unit}: required final audit is not a declared supporting artifact: "
                f"{required_support}"
            )
        for artifact_path, expected_hash in zip(artifact_paths, artifact_hashes):
            if not artifact_path.is_file():
                errors.append(f"{unit}: missing supporting artifact {artifact_path}")
                continue
            if HEX64.fullmatch(expected_hash) is None:
                errors.append(f"{unit}: malformed support hash {expected_hash!r}")
                continue
            live_hash = sha256(artifact_path)
            if live_hash != expected_hash:
                errors.append(
                    f"{unit}: support hash mismatch {artifact_path}: "
                    f"found {live_hash}; expected {expected_hash}"
                )
                continue
            support_files.add(artifact_path)
            bound_files.add(artifact_path)
    return bound_files, record_count, len(support_files), errors


def binding_sha256(paths: set[Path]) -> str:
    records = []
    for path in sorted((item.resolve() for item in paths), key=lambda item: str(item).casefold()):
        if path.is_file():
            records.append(f"{path}|{path.stat().st_size}|{sha256(path)}")
    return text_sha256("\n".join(records))


def bind_final_audit(
    audit_path: Path,
    *,
    language: str,
    authority_sha256: str,
    target_document_sha256: str,
    pdf_sha256: str,
) -> list[str]:
    """Bind the audit's labeled claims to the live authority, target, and PDF."""
    errors: list[str] = []
    try:
        text = read_utf8(audit_path)
    except Exception as exc:
        return [f"cannot read final audit: {exc}"]

    hex_capture = r"`?([0-9A-Fa-f]{64})`?"
    label_patterns = {
        "authority": re.compile(
            rf"^\s*[-*]\s*(?:German\s+)?Authority\s+SHA-256\s*:\s*"
            rf"{hex_capture}\s*$",
            re.IGNORECASE | re.MULTILINE,
        ),
        "target": re.compile(
            rf"^\s*[-*]\s*Expanded\s+{re.escape(language)}\s+target\s+"
            rf"SHA-256\s*:\s*{hex_capture}\s*$",
            re.IGNORECASE | re.MULTILINE,
        ),
        "pdf": re.compile(
            rf"^\s*[-*]\s*Final(?:\s+{re.escape(language)})?\s+PDF\s+"
            rf"SHA-256\s*:\s*{hex_capture}\s*$",
            re.IGNORECASE | re.MULTILINE,
        ),
    }
    expected = {
        "authority": authority_sha256.upper(),
        "target": target_document_sha256.upper(),
        "pdf": pdf_sha256.upper(),
    }
    for label, pattern in label_patterns.items():
        matches = pattern.findall(text)
        if len(matches) != 1:
            errors.append(
                f"final audit {label} hash label count is {len(matches)}; expected exactly 1"
            )
            continue
        found = matches[0].upper()
        if found != expected[label]:
            errors.append(
                f"final audit {label} hash mismatch: found {found}; "
                f"expected {expected[label]}"
            )
    return errors


def image_pixel_sha256(path: Path) -> tuple[str, int, int]:
    """Hash image geometry plus normalized RGB pixels, excluding container metadata."""
    from PIL import Image  # type: ignore

    with Image.open(path) as image:
        image.load()
        normalized = image.convert("RGB")
        width, height = normalized.size
        digest = hashlib.sha256()
        digest.update(f"{width}x{height}|RGB|\0".encode("ascii"))
        digest.update(normalized.tobytes())
    return digest.hexdigest().upper(), width, height


def page_pixel_binding_sha256(page_hashes: dict[int, str]) -> str:
    return text_sha256(
        "\n".join(f"{page}:{page_hashes[page]}" for page in sorted(page_hashes))
    )


def rerender_pdf_pixels(
    pdf_path: Path,
    pdftoppm_path: Path,
    page_count: int,
) -> tuple[dict[int, str], str, list[str]]:
    """Freshly render every candidate page with the pinned Poppler profile."""
    errors: list[str] = []
    page_hashes: dict[int, str] = {}
    renderer_version = ""
    if page_count < 1:
        return page_hashes, renderer_version, ["candidate PDF has no renderable pages"]
    if not pdftoppm_path.is_file():
        return page_hashes, renderer_version, [f"missing pdftoppm: {pdftoppm_path}"]

    try:
        version_run = subprocess.run(
            [str(pdftoppm_path), "-v"],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=30,
            check=False,
        )
        version_text = "\n".join(
            part.strip() for part in (version_run.stdout, version_run.stderr) if part.strip()
        )
        version_match = re.search(r"pdftoppm version[^\r\n]*", version_text, re.I)
        if version_run.returncode != 0 or version_match is None:
            errors.append(
                f"pdftoppm identity check failed rc={version_run.returncode}: "
                f"{version_text[:400]}"
            )
            return page_hashes, renderer_version, errors
        renderer_version = version_match.group(0)
    except Exception as exc:
        return page_hashes, renderer_version, [f"pdftoppm identity check failed: {exc}"]

    with tempfile.TemporaryDirectory(prefix="noether-r823-poppler-") as temp_dir:
        prefix = Path(temp_dir) / "fresh-page"
        command = [
            str(pdftoppm_path),
            "-f",
            "1",
            "-l",
            str(page_count),
            "-r",
            str(PINNED_RENDER_DPI),
            "-png",
            str(pdf_path),
            str(prefix),
        ]
        try:
            completed = subprocess.run(
                command,
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                timeout=600,
                check=False,
            )
        except Exception as exc:
            return page_hashes, renderer_version, [f"fresh Poppler render failed: {exc}"]
        if completed.returncode != 0:
            detail = (completed.stderr or completed.stdout).strip()
            return page_hashes, renderer_version, [
                f"fresh Poppler render failed rc={completed.returncode}: {detail[:800]}"
            ]

        indexed: dict[int, Path] = {}
        for path in Path(temp_dir).glob("fresh-page-*.png"):
            match = re.fullmatch(r"fresh-page-(\d+)\.png", path.name, re.I)
            if match is None:
                continue
            page = int(match.group(1))
            if page in indexed:
                errors.append(f"fresh Poppler render duplicated page {page}")
            indexed[page] = path
        expected_pages = set(range(1, page_count + 1))
        if set(indexed) != expected_pages:
            errors.append(
                f"fresh Poppler page set mismatch: found={len(indexed)}; "
                f"expected={page_count}; missing={sorted(expected_pages - set(indexed))[:20]}; "
                f"extra={sorted(set(indexed) - expected_pages)[:20]}"
            )
        for page in sorted(expected_pages & set(indexed)):
            try:
                pixel_hash, width, height = image_pixel_sha256(indexed[page])
                if min(width, height) < 600 or max(width, height) < 800:
                    errors.append(
                        f"fresh Poppler page {page} is too small: {width}x{height}"
                    )
                    continue
                page_hashes[page] = pixel_hash
            except Exception as exc:
                errors.append(f"fresh Poppler page {page} is unreadable: {exc}")
    return page_hashes, renderer_version, errors


def meaningful_review_text(value: str) -> bool:
    text = value.strip()
    return len(text) >= 80 and len(re.findall(r"\b\w+\b", text)) >= 10


def bind_visual_review_record(
    record_path: Path,
    *,
    language: str,
    pdf_sha256: str,
    target_document_sha256: str,
    page_count: int,
    pdftoppm_sha256: str,
    full_manifest_path: Path,
    expected_pixel_binding_sha256: str,
) -> tuple[set[Path], list[str]]:
    """Bind a structured review decision to the live candidate and full render."""
    bound: set[Path] = {record_path.resolve()}
    errors: list[str] = []
    try:
        data = json.loads(read_utf8(record_path))
    except Exception as exc:
        return bound, [f"cannot read visual review record: {exc}"]
    if not isinstance(data, dict):
        return bound, ["visual review record must be a JSON object"]
    missing_fields = sorted(VISUAL_REVIEW_FIELDS - set(data))
    if missing_fields:
        errors.append(f"visual review record missing fields {missing_fields}")

    expected_scalars = {
        "schema": VISUAL_REVIEW_SCHEMA,
        "status": "pass",
        "language": language,
        "pdf_sha256": pdf_sha256,
        "target_document_sha256": target_document_sha256,
        "page_count": page_count,
        "render_profile": PINNED_RENDER_PROFILE,
        "pdftoppm_sha256": pdftoppm_sha256,
        "baseline_kind": "reviewed-current-render",
        "baseline_pixel_binding_sha256": expected_pixel_binding_sha256,
    }
    for field, expected in expected_scalars.items():
        found = data.get(field)
        if isinstance(expected, str) and field.endswith("sha256"):
            found = str(found or "").upper()
            expected = expected.upper()
        elif field in {"status", "language"}:
            found = normalized_status(str(found or ""))
            expected = normalized_status(str(expected))
        if found != expected:
            errors.append(
                f"visual review {field} mismatch: found {found!r}; expected {expected!r}"
            )

    reviewed_pages, page_error = exact_page_spec(
        str(data.get("reviewed_pages", "")), page_count
    )
    all_pages = set(range(1, page_count + 1))
    if page_error is not None or reviewed_pages != all_pages:
        errors.append(
            f"visual review pages are not the full candidate: error={page_error}; "
            f"found={len(reviewed_pages)}; expected={page_count}"
        )

    raw_manifest = str(data.get("baseline_render_manifest", "")).strip()
    if raw_manifest:
        baseline_manifest = resolve_evidence_path(raw_manifest, record_path.parent)
        bound.add(baseline_manifest)
        if baseline_manifest != full_manifest_path.resolve():
            errors.append(
                f"visual review baseline manifest is {baseline_manifest}; "
                f"full-cumulative manifest is {full_manifest_path.resolve()}"
            )
        if not baseline_manifest.is_file():
            errors.append(f"visual review baseline manifest is missing: {baseline_manifest}")
        else:
            found_manifest_hash = sha256(baseline_manifest)
            expected_manifest_hash = str(
                data.get("baseline_render_manifest_sha256", "")
            ).upper()
            if found_manifest_hash != expected_manifest_hash:
                errors.append(
                    f"visual review baseline manifest hash mismatch: "
                    f"found {found_manifest_hash}; expected {expected_manifest_hash}"
                )
    else:
        errors.append("visual review baseline_render_manifest is blank")

    provenance = str(data.get("reviewer_provenance", "")).strip()
    if len(provenance) < 20 or len(re.findall(r"\b\w+\b", provenance)) < 3:
        errors.append("visual review reviewer_provenance is not substantive")
    reviewed_at = str(data.get("reviewed_at", "")).strip()
    try:
        parsed_time = datetime.fromisoformat(reviewed_at.replace("Z", "+00:00"))
        if parsed_time.tzinfo is None:
            raise ValueError("timezone is required")
    except Exception as exc:
        errors.append(f"visual review reviewed_at is not timezone-aware ISO-8601: {exc}")
    for field in ("review_method", "findings"):
        if not meaningful_review_text(str(data.get(field, ""))):
            errors.append(f"visual review {field} must be at least 80 characters/10 words")
    return bound, errors


def run_exact_promoter(
    *,
    promoter: Path,
    seed_ledger: Path,
    evidence_map: Path,
    parity_ledger: Path,
) -> tuple[bool, str]:
    promoter_hash = sha256(promoter)
    if promoter_hash != CANONICAL_PROMOTER_SHA256:
        return False, (
            f"promoter SHA-256 {promoter_hash}; "
            f"expected {CANONICAL_PROMOTER_SHA256}"
        )
    with tempfile.TemporaryDirectory(prefix="noether-r823-promoter-") as temp_dir:
        reproduced = Path(temp_dir) / "promoted.csv"
        completed = subprocess.run(
            [
                sys.executable,
                str(promoter),
                "--seed-ledger",
                str(seed_ledger),
                "--evidence-map",
                str(evidence_map),
                "--output-csv",
                str(reproduced),
            ],
            cwd=str(promoter.parent),
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=180,
            check=False,
        )
        if completed.returncode != 0 or not reproduced.is_file():
            detail = (completed.stderr or completed.stdout).strip()
            return False, f"canonical promoter failed rc={completed.returncode}: {detail}"
        expected_hash = sha256(reproduced)
        live_hash = sha256(parity_ledger)
        byte_exact = reproduced.read_bytes() == parity_ledger.read_bytes()
        return byte_exact, (
            f"promoter_sha256={promoter_hash}; reproduced_sha256={expected_hash}; "
            f"parity_sha256={live_hash}; byte_exact={byte_exact}"
        )


def has_strong_source_locator(value: str) -> bool:
    text = value.strip()
    for match in STRONG_NATIVE_TEX_LOCATOR.finditer(text):
        if TARGET_TEX_LOCATOR.search(match.group(0)) is None:
            return True
    for segment in re.split(r"[;\n]+", text):
        if STRONG_AUTHORITY_LOCATOR.search(segment):
            return True
        if (
            TARGET_TEX_LOCATOR.search(segment) is None
            and STRONG_NATIVE_PAGE_LOCATOR.search(segment)
        ):
            return True
    return False


def exact_page_spec(value: str, maximum: int) -> tuple[set[int], str | None]:
    text = value.strip()
    if not text:
        return set(), "blank page specification"
    pages: set[int] = set()
    for token in re.split(r"\s*[,;]\s*", text):
        if not token:
            return set(), f"empty page token in {value!r}"
        match = re.fullmatch(r"(\d+)(?:\s*[-–—]\s*(\d+))?", token)
        if match is None:
            return set(), f"noncanonical page token {token!r}"
        start = int(match.group(1))
        end = int(match.group(2) or start)
        if start < 1 or end < start or end > maximum:
            return set(), f"out-of-range page token {token!r} for {maximum} pages"
        pages.update(range(start, end + 1))
    return pages, None


def bind_render_manifest(
    *,
    manifest_path: Path,
    expected_pdf_hash: str,
    expected_pages: set[int],
    expected_pixel_hashes: dict[int, str],
    pixel_cache: dict[Path, tuple[str, int, int]] | None = None,
) -> tuple[set[Path], set[int], list[str]]:
    bound: set[Path] = {manifest_path.resolve()}
    errors: list[str] = []
    rendered_pages: set[int] = set()
    seen_paths: set[Path] = set()
    try:
        rows = read_csv(manifest_path)
        columns = set(rows[0]) if rows else set()
    except Exception as exc:
        return bound, rendered_pages, [str(exc)]
    if not RENDER_MANIFEST_FIELDS <= columns:
        errors.append(
            f"render manifest missing columns {sorted(RENDER_MANIFEST_FIELDS - columns)}"
        )
    for index, row in enumerate(rows, start=2):
        try:
            page = int(row.get("page", "").strip())
        except ValueError:
            errors.append(f"render manifest line {index}: invalid page")
            continue
        if page in rendered_pages:
            errors.append(f"render manifest line {index}: duplicate page {page}")
        rendered_pages.add(page)
        if page not in expected_pages:
            errors.append(f"render manifest line {index}: undeclared page {page}")
        if row.get("pdf_sha256", "").strip().upper() != expected_pdf_hash:
            errors.append(f"render manifest line {index}: wrong PDF hash")
        renderer = row.get("renderer", "").strip()
        if renderer != PINNED_RENDER_PROFILE:
            errors.append(
                f"render manifest line {index}: renderer/profile is not pinned"
            )
        render_path = resolve_evidence_path(
            row.get("render_path", ""), manifest_path.parent
        )
        if render_path in seen_paths:
            errors.append(f"render manifest line {index}: duplicate render path")
        seen_paths.add(render_path)
        if (
            not render_path.is_file()
            or render_path.suffix.casefold() != ".png"
            or render_path.stat().st_size < 1024
        ):
            errors.append(f"render manifest line {index}: invalid render file {render_path}")
            continue
        expected_hash = row.get("sha256", "").strip().upper()
        if HEX64.fullmatch(expected_hash) is None or sha256(render_path) != expected_hash:
            errors.append(f"render manifest line {index}: render hash mismatch")
            continue
        try:
            if pixel_cache is not None and render_path in pixel_cache:
                pixel_hash, width, height = pixel_cache[render_path]
            else:
                pixel_hash, width, height = image_pixel_sha256(render_path)
                if pixel_cache is not None:
                    pixel_cache[render_path] = (pixel_hash, width, height)
            if min(width, height) < 600 or max(width, height) < 800:
                errors.append(
                    f"render manifest line {index}: render too small {width}x{height}"
                )
                continue
        except Exception as exc:
            errors.append(f"render manifest line {index}: unreadable image: {exc}")
            continue
        expected_pixel_hash = expected_pixel_hashes.get(page)
        if expected_pixel_hash is None:
            errors.append(
                f"render manifest line {index}: no fresh candidate pixel hash for page {page}"
            )
            continue
        if pixel_hash != expected_pixel_hash:
            errors.append(
                f"render manifest line {index}: stored pixels do not derive from "
                f"the candidate PDF page {page}"
            )
            continue
        bound.add(render_path)
    if rendered_pages != expected_pages:
        errors.append(
            f"rendered page set mismatch: declared={len(expected_pages)}; "
            f"manifest={len(rendered_pages)}; "
            f"missing={sorted(expected_pages - rendered_pages)[:20]}"
        )
    return bound, rendered_pages, errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--language", choices=("spanish", "french"), required=True)
    parser.add_argument("--authority-tex", type=Path, required=True)
    parser.add_argument("--tex", type=Path, required=True)
    parser.add_argument("--pdf", type=Path, required=True)
    parser.add_argument("--pdftoppm", type=Path, required=True)
    parser.add_argument("--log", type=Path, required=True)
    parser.add_argument("--fls", type=Path, required=True)
    parser.add_argument("--parity-ledger", type=Path, required=True)
    parser.add_argument("--parity-seed-ledger", type=Path, required=True)
    parser.add_argument("--evidence-map", type=Path, required=True)
    parser.add_argument("--parity-promoter", type=Path, required=True)
    parser.add_argument("--terminology-ledger", type=Path, required=True)
    parser.add_argument("--visual-qa-ledger", type=Path, required=True)
    parser.add_argument("--visual-review-record", type=Path, required=True)
    parser.add_argument("--final-audit", type=Path, required=True)
    parser.add_argument(
        "--source-unit-manifest",
        type=Path,
        help="81-row manifest generated from R823; omission is reported as a failed evidence check",
    )
    parser.add_argument(
        "--target-unit-manifest",
        type=Path,
        help="81-row manifest generated from the expanded target; omission is reported as a failed evidence check",
    )
    parser.add_argument("--minimum-pdf-pages", type=int, default=430)
    parser.add_argument("--minimum-terminology-rows", type=int, default=60)
    parser.add_argument("--output-json", type=Path)
    args = parser.parse_args()

    checks: list[Check] = []
    checks.append(
        Check(
            "canonical_minimums",
            args.minimum_pdf_pages >= 430 and args.minimum_terminology_rows >= 60,
            (
                f"pdf_pages={args.minimum_pdf_pages} (floor 430); "
                f"terminology_rows={args.minimum_terminology_rows} (floor 60)"
            ),
        )
    )
    core_files = {
        "authority_tex": args.authority_tex,
        "target_tex": args.tex,
        "target_pdf": args.pdf,
        "pdftoppm": args.pdftoppm,
        "build_log": args.log,
        "recorder_fls": args.fls,
    }
    evidence_files = {
        "parity_ledger": args.parity_ledger,
        "parity_seed_ledger": args.parity_seed_ledger,
        "evidence_map": args.evidence_map,
        "parity_promoter": args.parity_promoter,
        "terminology_ledger": args.terminology_ledger,
        "visual_qa_ledger": args.visual_qa_ledger,
        "visual_review_record": args.visual_review_record,
        "final_audit": args.final_audit,
    }
    if args.source_unit_manifest is not None:
        evidence_files["source_unit_manifest"] = args.source_unit_manifest
    if args.target_unit_manifest is not None:
        evidence_files["target_unit_manifest"] = args.target_unit_manifest
    required_files = core_files | evidence_files
    missing = [f"{name}: {path}" for name, path in required_files.items() if not path.is_file()]
    checks.append(Check("required_files", not missing, "; ".join(missing) if missing else "all required artifacts exist"))
    missing_core = [f"{name}: {path}" for name, path in core_files.items() if not path.is_file()]
    if missing_core:
        return emit(args, checks)

    initial_fingerprints = {
        path.resolve(): fingerprint(path)
        for path in required_files.values()
        if path.is_file()
    }

    bound_evidence_files: set[Path] = set()
    if args.evidence_map.is_file():
        (
            bound_evidence_files,
            bound_evidence_records,
            bound_support_files,
            evidence_binding_errors,
        ) = bind_unit_evidence(
            args.evidence_map,
            required_support_path=args.final_audit,
        )
        for path in bound_evidence_files:
            if path.is_file():
                initial_fingerprints.setdefault(path.resolve(), fingerprint(path))
        evidence_binding_ok = (
            bound_evidence_records == len(REQUIRED_UNITS)
            and not evidence_binding_errors
        )
        checks.append(
            Check(
                "direct_unit_evidence_binding",
                evidence_binding_ok,
                (
                    f"records={bound_evidence_records}; "
                    f"unique_bound_files={len(bound_evidence_files)}; "
                    f"unique_support_files={bound_support_files}; "
                    f"binding_sha256={binding_sha256(bound_evidence_files)}; "
                    f"errors={evidence_binding_errors[:20]}"
                ),
            )
        )
    else:
        checks.append(
            Check(
                "direct_unit_evidence_binding",
                False,
                f"missing evidence map: {args.evidence_map}",
            )
        )

    promoter_inputs_exist = all(
        path.is_file()
        for path in (
            args.parity_promoter,
            args.parity_seed_ledger,
            args.evidence_map,
            args.parity_ledger,
        )
    )
    if promoter_inputs_exist:
        promoter_ok, promoter_detail = run_exact_promoter(
            promoter=args.parity_promoter,
            seed_ledger=args.parity_seed_ledger,
            evidence_map=args.evidence_map,
            parity_ledger=args.parity_ledger,
        )
        checks.append(Check("canonical_promoter_binding", promoter_ok, promoter_detail))
    else:
        checks.append(
            Check(
                "canonical_promoter_binding",
                False,
                "promoter, seed ledger, evidence map, or parity ledger is missing",
            )
        )

    authority_hash = sha256(args.authority_tex)
    checks.append(Check("authority_hash", authority_hash == R823_TEX_SHA256, f"found {authority_hash}; expected {R823_TEX_SHA256}"))
    authority_text = read_utf8(args.authority_tex)
    source_unit_rows = build_source_units(args.authority_tex, authority_text)
    computed_source_units = {row.unit_id: row.source_sha256 for row in source_unit_rows}
    source_chars_by_unit = {row.unit_id: row.chars for row in source_unit_rows}
    if args.source_unit_manifest is None:
        checks.append(Check("source_unit_manifest", False, "--source-unit-manifest was not supplied"))
    elif args.source_unit_manifest.is_file():
        source_manifest = read_csv(args.source_unit_manifest)
        manifest_by_unit = {row.get("unit_id", "").strip(): row for row in source_manifest}
        source_manifest_counts = Counter(row.get("unit_id", "").strip() for row in source_manifest)
        duplicate_manifest_units = sorted(unit for unit, count in source_manifest_counts.items() if unit and count > 1)
        missing_manifest_units = [unit for unit in REQUIRED_UNITS if unit not in manifest_by_unit]
        extra_manifest_units = sorted(set(manifest_by_unit) - set(REQUIRED_UNITS))
        bad_manifest_hashes = [
            unit
            for unit in REQUIRED_UNITS
            if unit in manifest_by_unit
            and manifest_by_unit[unit].get("source_sha256", "").upper()
            != computed_source_units.get(unit, "")
        ]
        source_manifest_ok = (
            len(source_manifest) == len(REQUIRED_UNITS)
            and not duplicate_manifest_units
            and not missing_manifest_units
            and not extra_manifest_units
            and not bad_manifest_hashes
        )
        checks.append(
            Check(
                "source_unit_manifest",
                source_manifest_ok,
                (
                    f"rows={len(source_manifest)}; duplicates={duplicate_manifest_units}; "
                    f"missing={missing_manifest_units}; extra={extra_manifest_units}; "
                    f"hash_mismatches={bad_manifest_hashes}"
                    if not source_manifest_ok
                    else f"all {len(REQUIRED_UNITS)} manifest units match the verified R823 authority"
                ),
            )
        )
    else:
        checks.append(Check("source_unit_manifest", False, f"missing manifest: {args.source_unit_manifest}"))

    try:
        target_text, dependencies, input_warnings = expand_tex(args.tex)
    except (OSError, UnicodeError) as exc:
        checks.append(Check("tex_expansion", False, str(exc)))
        return emit(args, checks)
    checks.append(Check("tex_expansion", not input_warnings, "; ".join(input_warnings) if input_warnings else f"expanded {len(dependencies)} TeX files"))
    target_document_hash = text_sha256(target_text)
    structural_target_text = mask_tex_comments(target_text)
    for dependency in dependencies:
        if dependency.is_file():
            initial_fingerprints.setdefault(dependency.resolve(), fingerprint(dependency))
    checks.append(
        Check(
            "target_document_hash",
            bool(target_text),
            f"expanded target SHA-256 {target_document_hash}",
        )
    )

    computed_target_units: dict[str, str] = {}
    target_chars_by_unit: dict[str, int] = {}
    try:
        target_units = build_target_units(args.tex, target_text, args.language)
        computed_target_units = {row.unit_id: row.target_sha256 for row in target_units}
        target_chars_by_unit = {row.unit_id: row.target_chars for row in target_units}
        checks.append(Check("target_unit_slicing", len(target_units) == len(REQUIRED_UNITS), f"sliced {len(target_units)} target units"))
    except Exception as exc:
        checks.append(Check("target_unit_slicing", False, str(exc)))

    if args.target_unit_manifest is None:
        checks.append(Check("target_unit_manifest", False, "--target-unit-manifest was not supplied"))
    elif args.target_unit_manifest.is_file():
        target_manifest = read_csv(args.target_unit_manifest)
        target_manifest_by_unit = {row.get("unit_id", "").strip(): row for row in target_manifest}
        target_manifest_counts = Counter(row.get("unit_id", "").strip() for row in target_manifest)
        duplicate_target_manifest_units = sorted(unit for unit, count in target_manifest_counts.items() if unit and count > 1)
        missing_target_manifest_units = [unit for unit in REQUIRED_UNITS if unit not in target_manifest_by_unit]
        extra_target_manifest_units = sorted(set(target_manifest_by_unit) - set(REQUIRED_UNITS))
        bad_target_manifest_hashes = [
            unit
            for unit in REQUIRED_UNITS
            if unit in target_manifest_by_unit
            and target_manifest_by_unit[unit].get("target_sha256", "").upper()
            != computed_target_units.get(unit, "")
        ]
        bad_target_document_hashes = [
            unit
            for unit in REQUIRED_UNITS
            if unit in target_manifest_by_unit
            and target_manifest_by_unit[unit].get("target_document_sha256", "").upper()
            != target_document_hash
        ]
        target_manifest_ok = (
            bool(computed_target_units)
            and len(target_manifest) == len(REQUIRED_UNITS)
            and not duplicate_target_manifest_units
            and not missing_target_manifest_units
            and not extra_target_manifest_units
            and not bad_target_manifest_hashes
            and not bad_target_document_hashes
        )
        checks.append(
            Check(
                "target_unit_manifest",
                target_manifest_ok,
                (
                    f"rows={len(target_manifest)}; duplicates={duplicate_target_manifest_units}; "
                    f"missing={missing_target_manifest_units}; extra={extra_target_manifest_units}; "
                    f"unit_hash_mismatches={bad_target_manifest_hashes}; "
                    f"document_hash_mismatches={bad_target_document_hashes}"
                    if not target_manifest_ok
                    else f"all {len(REQUIRED_UNITS)} manifest units match the expanded target"
                ),
            )
        )
    else:
        checks.append(Check("target_unit_manifest", False, f"missing manifest: {args.target_unit_manifest}"))

    compressed_units = [
        f"{unit}={target_chars_by_unit[unit] / source_chars_by_unit[unit]:.2f}"
        for unit in REQUIRED_UNITS
        if unit in target_chars_by_unit
        and unit in source_chars_by_unit
        and target_chars_by_unit[unit] / source_chars_by_unit[unit] < 0.65
    ]
    checks.append(
        Check(
            "no_gross_unit_compression",
            bool(target_chars_by_unit) and not compressed_units,
            (
                f"target/source character ratios below 0.65: {compressed_units}"
                if compressed_units
                else "no target unit falls below the 0.65 gross-compression floor"
            ),
        )
    )

    paper_matches = [
        match
        for match in PAPER_MARKER.finditer(structural_target_text)
        if 1 <= int(match.group(1)) <= 43
    ]
    visible_papers = {int(match.group(1)) for match in paper_matches}
    missing_visible_papers = sorted(set(range(1, 44)) - visible_papers)
    missing_papers = [
        number
        for number in range(1, 44)
        if f"P{number:02d}" not in computed_target_units
    ]
    checks.append(
        Check(
            "papers_1_43_present",
            not missing_papers,
            (
                f"missing logical paper slices: {missing_papers}; visible-number-marker gaps: {missing_visible_papers}"
                if missing_papers
                else (
                    "all 43 logical paper slices found; authority-matched non-numbered boundaries "
                    f"accepted for visible-number-marker gaps {missing_visible_papers}"
                    if missing_visible_papers
                    else "all 43 logical paper slices and visible number markers found"
                )
            ),
        )
    )

    try:
        target_papers = slice_papers(target_text)
        cursor = target_papers[43].start
        for kind in (
            "book",
            "post45",
            "supplement",
            "bibliography",
            "notices",
            "reviews",
            "books",
        ):
            cursor = locate_any(target_text, MARKERS[args.language][kind], cursor, kind)
            checks.append(
                Check(
                    f"terminal_marker_{kind}",
                    True,
                    f"live structural heading at expanded offset {cursor}",
                )
            )
            cursor += 1
    except Exception as exc:
        checks.append(Check("terminal_marker_sequence", False, str(exc)))

    placeholders = sorted(set(match.group(0) for match in PLACEHOLDER.finditer(structural_target_text)))
    checks.append(Check("no_placeholders", not placeholders, f"found: {placeholders}" if placeholders else "no placeholder tokens found"))

    broken_tex = sorted(set(match.group(0) for match in BROKEN_TEX_TOKEN.finditer(structural_target_text)))
    checks.append(Check("no_broken_tex_tokens", not broken_tex, f"found literal math-spacing tokens: {broken_tex}" if broken_tex else "no missing-backslash math-spacing tokens found"))

    try:
        paper_audit = audit_paper_structure(authority_text, target_text, args.language)
        bad_papers = [
            row.paper
            for row in paper_audit
            if row.status != "present-structural-review"
        ]
        checks.append(
            Check(
                "paper_structure_audit",
                len(paper_audit) == 43 and not bad_papers,
                f"rows={len(paper_audit)}; nonpassing_papers={bad_papers}",
            )
        )
    except Exception as exc:
        checks.append(Check("paper_structure_audit", False, str(exc)))

    try:
        target_papers = slice_papers(target_text)
        book_start = locate_any(
            target_text,
            MARKERS[args.language]["book"],
            target_papers[43].start,
            "book",
        )
        post45_start = locate_any(
            target_text,
            MARKERS[args.language]["post45"],
            book_start,
            "post45",
        )
        book_audit = audit_book_structure(
            authority_text,
            target_text[book_start:post45_start],
        )
        bad_sections = [
            row.section
            for row in book_audit
            if row.status != "present-structural-review"
        ]
        checks.append(
            Check(
                "book_structure_audit",
                len(book_audit) == 31 and not bad_sections,
                f"rows={len(book_audit)}; nonpassing_sections={bad_sections}",
            )
        )
    except Exception as exc:
        checks.append(Check("book_structure_audit", False, str(exc)))

    log_text = read_utf8(args.log)
    fatal = FATAL_LOG.findall(log_text)
    checks.append(Check("clean_build_log", not fatal, f"fatal patterns: {fatal}" if fatal else "no fatal TeX patterns"))

    pages = 0
    candidate_pdf_hash = ""
    try:
        pages = pdf_pages(args.pdf)
        candidate_pdf_hash = sha256(args.pdf)
        checks.append(Check("pdf_page_floor", pages >= args.minimum_pdf_pages, f"{pages} pages; minimum {args.minimum_pdf_pages}"))
    except Exception as exc:  # pragma: no cover - dependency/PDF failure
        checks.append(Check("pdf_page_floor", False, str(exc)))

    if args.final_audit.is_file() and candidate_pdf_hash:
        final_audit_errors = bind_final_audit(
            args.final_audit,
            language=args.language,
            authority_sha256=authority_hash,
            target_document_sha256=target_document_hash,
            pdf_sha256=candidate_pdf_hash,
        )
    else:
        final_audit_errors = [f"missing or unusable final audit: {args.final_audit}"]
    checks.append(
        Check(
            "final_audit_hash_binding",
            not final_audit_errors,
            (
                f"audit={args.final_audit}; authority={authority_hash}; "
                f"target={target_document_hash}; pdf={candidate_pdf_hash}; "
                f"errors={final_audit_errors}"
            ),
        )
    )

    pdftoppm_hash = sha256(args.pdftoppm) if args.pdftoppm.is_file() else ""
    fresh_pixel_hashes, poppler_version, poppler_errors = rerender_pdf_pixels(
        args.pdf,
        args.pdftoppm,
        pages,
    )
    expected_pdf_pages = set(range(1, pages + 1))
    poppler_render_ok = (
        not poppler_errors and set(fresh_pixel_hashes) == expected_pdf_pages
    )
    fresh_pixel_binding = page_pixel_binding_sha256(fresh_pixel_hashes)
    checks.append(
        Check(
            "poppler_pdf_derivation",
            poppler_render_ok,
            (
                f"renderer={poppler_version or 'unavailable'}; "
                f"pdftoppm_sha256={pdftoppm_hash}; dpi={PINNED_RENDER_DPI}; "
                f"rendered_pages={len(fresh_pixel_hashes)}; expected_pages={pages}; "
                f"pixel_binding_sha256={fresh_pixel_binding}; "
                f"errors={poppler_errors[:20]}"
            ),
        )
    )

    build_matches = BUILD_SUCCESS.findall(log_text)
    success_output = build_matches[-1][0].strip().strip('"') if build_matches else ""
    success_pages = int(build_matches[-1][1]) if build_matches else 0
    success_stem = Path(success_output).stem.casefold() if success_output else ""
    expected_stem = args.pdf.stem.casefold()
    root_identity_ok = (
        args.tex.stem.casefold()
        == args.pdf.stem.casefold()
        == args.log.stem.casefold()
        == args.fls.stem.casefold()
    )
    build_signature_ok = bool(build_matches) and success_stem == expected_stem and success_pages == pages
    checks.append(
        Check(
            "build_success_signature",
            root_identity_ok and build_signature_ok,
            (
                f"root_stems=({args.tex.stem},{args.pdf.stem},{args.log.stem},{args.fls.stem}); "
                f"log_output={success_output or 'absent'}; log_pages={success_pages}; pdf_pages={pages}"
            ),
        )
    )

    local_build_inputs: set[Path] = set(dependencies)
    try:
        fls_pwd, fls_inputs, fls_outputs, fls_warnings = parse_fls(args.fls)
        missing_expanded_inputs = sorted(
            str(path)
            for path in dependencies
            if path.resolve() not in fls_inputs
        )
        local_build_inputs.update(
            path
            for path in fls_inputs
            if path.is_file()
            and is_within(path, args.tex.parent)
            and path.suffix.casefold() in LOCAL_BUILD_SUFFIXES
            and path.resolve() != args.pdf.resolve()
        )
        success_record = (
            (fls_pwd / success_output).resolve()
            if success_output and not Path(success_output).is_absolute()
            else Path(success_output).resolve()
            if success_output
            else None
        )
        recorder_ok = (
            not fls_warnings
            and args.tex.resolve() in fls_inputs
            and args.log.resolve() in fls_outputs
            and not missing_expanded_inputs
            and success_record is not None
            and success_record in fls_outputs
        )
        if success_record is not None and success_record.suffix.casefold() == ".xdv":
            recorder_ok = (
                recorder_ok
                and success_record.is_file()
                and args.pdf.stat().st_mtime_ns >= success_record.stat().st_mtime_ns
            )
        elif success_record is not None and success_record.suffix.casefold() == ".pdf":
            recorder_ok = recorder_ok and success_record == args.pdf.resolve()
        checks.append(
            Check(
                "fls_build_binding",
                recorder_ok,
                (
                    f"pwd={fls_pwd}; inputs={len(fls_inputs)}; outputs={len(fls_outputs)}; "
                    f"warnings={fls_warnings}; missing_expanded_inputs={missing_expanded_inputs}; "
                    f"success_output={success_record}"
                ),
            )
        )
    except Exception as exc:
        checks.append(Check("fls_build_binding", False, str(exc)))

    for dependency in local_build_inputs:
        if dependency.is_file():
            initial_fingerprints.setdefault(dependency.resolve(), fingerprint(dependency))
    newest_input_ns = max(path.stat().st_mtime_ns for path in local_build_inputs if path.is_file())
    output_times_ok = (
        args.pdf.stat().st_mtime_ns >= newest_input_ns
        and args.log.stat().st_mtime_ns >= newest_input_ns
        and args.fls.stat().st_mtime_ns >= newest_input_ns
    )
    checks.append(
        Check(
            "build_outputs_are_current",
            output_times_ok,
            (
                "PDF, log, and recorder file are at least as new as every local build input"
                if output_times_ok
                else "PDF, log, or recorder file predates a local build input"
            ),
        )
    )

    if args.parity_ledger.is_file():
        parity = read_csv(args.parity_ledger)
        parity_by_unit = {row.get("unit_id", "").strip(): row for row in parity}
        parity_counts = Counter(row.get("unit_id", "").strip() for row in parity)
        duplicate_parity_units = sorted(unit for unit, count in parity_counts.items() if unit and count > 1)
        absent_units = [unit for unit in REQUIRED_UNITS if unit not in parity_by_unit]
        bad_status = [unit for unit in REQUIRED_UNITS if unit in parity_by_unit and normalized_status(parity_by_unit[unit].get("status", "")) != "source-reconciled"]
        missing_review_evidence = [
            unit
            for unit in REQUIRED_UNITS
            if unit in parity_by_unit
            and not parity_by_unit[unit].get("review_evidence", "").strip()
        ]
        bad_hashes = [
            unit
            for unit in REQUIRED_UNITS
            if unit in parity_by_unit
            and (
                not HEX64.fullmatch(parity_by_unit[unit].get("source_sha256", ""))
                or not HEX64.fullmatch(parity_by_unit[unit].get("target_sha256", ""))
                or not HEX64.fullmatch(
                    parity_by_unit[unit].get("target_document_sha256", "")
                )
            )
        ]
        wrong_source_hashes = [
            unit
            for unit in REQUIRED_UNITS
            if unit in parity_by_unit
            and parity_by_unit[unit].get("source_sha256", "").upper()
            != computed_source_units.get(unit, "")
        ]
        wrong_target_hashes = [
            unit
            for unit in REQUIRED_UNITS
            if unit in parity_by_unit
            and parity_by_unit[unit].get("target_sha256", "").upper()
            != computed_target_units.get(unit, "")
        ]
        wrong_target_document_hashes = [
            unit
            for unit in REQUIRED_UNITS
            if unit in parity_by_unit
            and parity_by_unit[unit].get("target_document_sha256", "").upper()
            != target_document_hash
        ]
        parity_ok = (
            bool(computed_target_units)
            and len(parity) == len(REQUIRED_UNITS)
            and not duplicate_parity_units
            and not absent_units
            and not bad_status
            and not missing_review_evidence
            and not bad_hashes
            and not wrong_source_hashes
            and not wrong_target_hashes
            and not wrong_target_document_hashes
        )
        checks.append(
            Check(
                "unit_source_parity",
                parity_ok,
                (
                    f"rows={len(parity)}; duplicates={duplicate_parity_units}; missing={absent_units}; "
                    f"non_reconciled={bad_status}; missing_review_evidence={missing_review_evidence}; "
                    f"bad_hashes={bad_hashes}; wrong_source_hashes={wrong_source_hashes}; "
                    f"wrong_target_hashes={wrong_target_hashes}; "
                    f"wrong_target_document_hashes={wrong_target_document_hashes}"
                    if not parity_ok
                    else f"all {len(REQUIRED_UNITS)} required units source-reconciled against exact R823 and live target hashes"
                ),
            )
        )
    else:
        checks.append(Check("unit_source_parity", False, f"missing ledger: {args.parity_ledger}"))

    if args.terminology_ledger.is_file():
        terminology = read_csv(args.terminology_ledger)
        term_columns = set(terminology[0]) if terminology else set()
        required_term_columns = {"source_term", "target_term", "sense", "status", "source_evidence"}
        term_status_bad = [
            index + 2
            for index, row in enumerate(terminology)
            if normalized_status(row.get("status", ""))
            not in {"approved", "reviewed", "source-supported"}
        ]
        blank_term_lines = [
            index + 2
            for index, row in enumerate(terminology)
            if any(not row.get(column, "").strip() for column in required_term_columns)
        ]
        strict_source_locator_lines = [
            index + 2
            for index, row in enumerate(terminology)
            if has_strong_source_locator(row.get("source_evidence", ""))
        ]
        weak_source_locator_lines = [
            index + 2
            for index, row in enumerate(terminology)
            if row.get("source_evidence", "").strip()
            and not has_strong_source_locator(row.get("source_evidence", ""))
        ]
        term_keys = [
            tuple(
                re.sub(r"\s+", " ", row.get(column, "").strip().casefold())
                for column in ("source_term", "target_term", "sense")
            )
            for row in terminology
        ]
        duplicate_term_keys = sorted(
            key for key, count in Counter(term_keys).items() if count > 1
        )
        terminology_ok = (
            len(terminology) >= args.minimum_terminology_rows
            and required_term_columns <= term_columns
            and not term_status_bad
            and not blank_term_lines
            and len(strict_source_locator_lines) >= args.minimum_terminology_rows
            and not duplicate_term_keys
        )
        checks.append(
            Check(
                "terminology_ledger",
                terminology_ok,
                (
                    f"rows={len(terminology)}; "
                    f"missing_columns={sorted(required_term_columns - term_columns)}; "
                    f"bad_status_lines={term_status_bad[:20]}; "
                    f"blank_required_lines={blank_term_lines[:20]}; "
                    f"strict_source_locator_rows={len(strict_source_locator_lines)} "
                    f"(minimum {args.minimum_terminology_rows}); "
                    f"weak_source_locator_lines={weak_source_locator_lines[:20]}; "
                    f"duplicate_decisions={duplicate_term_keys[:10]}"
                ),
            )
        )
    else:
        checks.append(Check("terminology_ledger", False, f"missing ledger: {args.terminology_ledger}"))

    required_visual_scopes = {"changed-pages", "full-cumulative-spread", "terminal-material"}
    if args.visual_qa_ledger.is_file():
        visual = read_csv(args.visual_qa_ledger)
        visual_columns = set(visual[0]) if visual else set()
        required_visual_columns = {
            "scope",
            "status",
            "language",
            "pdf_sha256",
            "target_document_sha256",
            "pages",
            "renderer",
            "render_path",
            "review_notes",
        }
        scopes = [normalized_status(row.get("scope", "")) for row in visual]
        scope_counts = Counter(scopes)
        duplicate_visual_scopes = sorted(
            scope for scope, count in scope_counts.items() if scope and count > 1
        )
        malformed_visual_lines: list[int] = []
        invalid_page_lines: list[int] = []
        passing_scopes: set[str] = set()
        bound_visual_files: set[Path] = {
            args.visual_qa_ledger.resolve(),
            args.visual_review_record.resolve(),
        }
        visual_errors: list[str] = []
        all_pdf_pages = set(range(1, pages + 1))
        manifest_by_scope: dict[str, Path] = {}
        manifest_cache: dict[
            tuple[Path, frozenset[int]], tuple[set[Path], set[int], list[str]]
        ] = {}
        pixel_cache: dict[Path, tuple[str, int, int]] = {}
        for index, row in enumerate(visual, start=2):
            scope = normalized_status(row.get("scope", ""))
            claimed_pages, page_error = exact_page_spec(row.get("pages", ""), pages)
            page_numbers_valid = page_error is None and bool(claimed_pages)
            if scope == "full-cumulative-spread":
                page_numbers_valid = page_numbers_valid and claimed_pages == all_pdf_pages
            elif scope == "terminal-material":
                page_numbers_valid = page_numbers_valid and pages in claimed_pages
            if not page_numbers_valid:
                invalid_page_lines.append(index)

            render_manifest = resolve_evidence_path(
                row.get("render_path", ""), args.visual_qa_ledger.parent
            )
            if scope:
                manifest_by_scope[scope] = render_manifest
            manifest_errors: list[str] = []
            rendered_pages: set[int] = set()
            if render_manifest.is_file() and render_manifest.suffix.casefold() == ".csv":
                cache_key = (render_manifest.resolve(), frozenset(claimed_pages))
                cached_manifest = manifest_cache.get(cache_key)
                if cached_manifest is None:
                    cached_manifest = bind_render_manifest(
                        manifest_path=render_manifest,
                        expected_pdf_hash=candidate_pdf_hash,
                        expected_pages=claimed_pages,
                        expected_pixel_hashes=fresh_pixel_hashes,
                        pixel_cache=pixel_cache,
                    )
                    manifest_cache[cache_key] = cached_manifest
                manifest_files, rendered_pages, manifest_errors = cached_manifest
                bound_visual_files.update(manifest_files)
            else:
                manifest_errors.append(
                    f"render_path must be a live hashed-render CSV manifest: {render_manifest}"
                )

            renderer = row.get("renderer", "").strip()
            notes = row.get("review_notes", "").strip()
            meaningful_notes = meaningful_review_text(notes)
            row_ok = (
                scope in required_visual_scopes
                and normalized_status(row.get("status", "")) == "pass"
                and normalized_status(row.get("language", ""))
                == normalized_status(args.language)
                and row.get("pdf_sha256", "").upper() == candidate_pdf_hash
                and row.get("target_document_sha256", "").upper()
                == target_document_hash
                and renderer == PINNED_RENDER_PROFILE
                and meaningful_notes
                and page_numbers_valid
                and rendered_pages == claimed_pages
                and not manifest_errors
            )
            if row_ok:
                passing_scopes.add(scope)
            else:
                malformed_visual_lines.append(index)
                visual_errors.extend(
                    f"line {index}: {error}" for error in manifest_errors
                )
                if not meaningful_notes:
                    visual_errors.append(
                        f"line {index}: review_notes must be at least 80 characters/10 words"
                    )

        full_manifest_path = manifest_by_scope.get("full-cumulative-spread")
        if args.visual_review_record.is_file() and full_manifest_path is not None:
            review_bound_files, visual_review_errors = bind_visual_review_record(
                args.visual_review_record,
                language=args.language,
                pdf_sha256=candidate_pdf_hash,
                target_document_sha256=target_document_hash,
                page_count=pages,
                pdftoppm_sha256=pdftoppm_hash,
                full_manifest_path=full_manifest_path,
                expected_pixel_binding_sha256=fresh_pixel_binding,
            )
            bound_visual_files.update(review_bound_files)
        else:
            visual_review_errors = [
                "visual review record or full-cumulative-spread manifest is missing"
            ]
        visual_review_ok = not visual_review_errors
        checks.append(
            Check(
                "visual_review_binding",
                visual_review_ok,
                (
                    f"record={args.visual_review_record}; "
                    f"full_manifest={full_manifest_path}; "
                    f"pixel_binding_sha256={fresh_pixel_binding}; "
                    f"errors={visual_review_errors}"
                ),
            )
        )

        for path in bound_visual_files:
            if path.is_file():
                initial_fingerprints.setdefault(path.resolve(), fingerprint(path))

        visual_ok = (
            required_visual_columns <= visual_columns
            and len(visual) == len(required_visual_scopes)
            and not duplicate_visual_scopes
            and not malformed_visual_lines
            and required_visual_scopes <= passing_scopes
            and poppler_render_ok
            and visual_review_ok
        )
        checks.append(
            Check(
                "visual_qa",
                visual_ok,
                (
                    f"rows={len(visual)}; passing_scopes={sorted(passing_scopes)}; "
                    f"required={sorted(required_visual_scopes)}; "
                    f"missing_columns={sorted(required_visual_columns - visual_columns)}; "
                    f"duplicate_scopes={duplicate_visual_scopes}; "
                    f"malformed_lines={malformed_visual_lines}; "
                    f"invalid_page_lines={invalid_page_lines}; "
                    f"bound_render_files={len(bound_visual_files)}; "
                    f"render_binding_sha256={binding_sha256(bound_visual_files)}; "
                    f"fresh_pixel_binding_sha256={fresh_pixel_binding}; "
                    f"visual_errors={visual_errors[:20]}; pdf_sha256={candidate_pdf_hash}"
                ),
            )
        )
    else:
        checks.append(
            Check(
                "visual_review_binding",
                False,
                "visual-QA ledger is missing, so no full manifest can be review-bound",
            )
        )
        checks.append(Check("visual_qa", False, f"missing ledger: {args.visual_qa_ledger}; required={sorted(required_visual_scopes)}"))

    changed_inputs: list[str] = []
    missing_inputs: list[str] = []
    for path, initial in initial_fingerprints.items():
        if not path.is_file():
            missing_inputs.append(str(path))
        elif fingerprint(path) != initial:
            changed_inputs.append(str(path))
    try:
        final_target_text, final_dependencies, final_warnings = expand_tex(args.tex)
        final_target_hash = text_sha256(final_target_text)
        new_dependencies = sorted(
            str(path)
            for path in final_dependencies
            if path.resolve() not in {item.resolve() for item in dependencies}
        )
    except Exception as exc:
        final_warnings = [str(exc)]
        final_target_hash = ""
        new_dependencies = []
    stable = (
        not changed_inputs
        and not missing_inputs
        and not final_warnings
        and not new_dependencies
        and final_target_hash == target_document_hash
        and sha256(args.authority_tex) == R823_TEX_SHA256
    )
    checks.append(
        Check(
            "evidence_snapshot_stable",
            stable,
            (
                f"changed={changed_inputs}; missing={missing_inputs}; "
                f"new_dependencies={new_dependencies}; final_warnings={final_warnings}; "
                f"initial_target_sha256={target_document_hash}; "
                f"final_target_sha256={final_target_hash}"
            ),
        )
    )

    return emit(args, checks)


def emit(args: argparse.Namespace, checks: list[Check]) -> int:
    passed = all(check.passed for check in checks)
    report = {
        "schema": "noether-r823-completion-gate-v4",
        "language": args.language,
        "passed": passed,
        "checks": [asdict(check) for check in checks],
    }
    rendered = json.dumps(report, ensure_ascii=False, indent=2)
    if args.output_json:
        args.output_json.parent.mkdir(parents=True, exist_ok=True)
        args.output_json.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
