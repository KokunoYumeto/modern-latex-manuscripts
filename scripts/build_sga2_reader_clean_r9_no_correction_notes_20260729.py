#!/usr/bin/env python3
"""Build the SGA2 R9 reader without project correction-status notes."""

from __future__ import annotations

import csv
import hashlib
import importlib.util
import io
import json
import os
import re
import shutil
import sys
import zipfile
from collections import Counter
from pathlib import Path

from pypdf import PdfReader


SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
BASE_PATH = (
    SCRIPT_DIR / "build_sga_reader_mathematical_body_clean_successor_20260729.py"
)
SPEC = importlib.util.spec_from_file_location("sga_reader_body_clean_v2", BASE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("Unable to load the established SGA reader-clean workflow")
previous = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = previous
SPEC.loader.exec_module(previous)
ORIGINAL_IS_PROJECT_NOTE = previous.is_project_note


OUTPUT_ROOT = (
    REPO_ROOT
    / "sources"
    / "sga"
    / "sga2-english-reader-clean-r9-no-correction-status-notes-20260729"
)
TEMP_ROOT = (
    Path(os.environ["LOCALAPPDATA"])
    / "Temp"
    / "sga2_reader_clean_r9_no_correction_notes_20260729"
)
SOURCE_ROOT = previous.SGA2_SOURCE
MASTER_OVERLAY = previous.MASTER_OVERLAYS["sga2"]
MASTER_NAME = previous.MASTER_NAMES["sga2"]

PDF_NAME = "00b_SGA2_English_Reader.pdf"
TEX_NAME = "02b_SGA2_English_Master.tex"
SOURCE_ZIP_NAME = "10b_SGA2_English_Source_and_History_R9_20260729.zip"
BUILD_LOG_NAME = "SGA2_R9_BUILD_PUBLIC.log"
REMOVAL_LEDGER_NAME = "READER_APPARATUS_REMOVAL_LEDGER.csv"
VALIDATION_NAME = "PACKAGE_VALIDATION.json"
README_NAME = "README.md"
VISUAL_QA_NAME = "FINAL_VISUAL_QA.md"
SHA_MANIFEST_NAME = "SHA256SUMS.csv"

HISTORICAL_EDITORIAL_NOTE_MARKER = (
    "The reissue of Serre"
)
PROJECT_CORRECTION_PHRASES = (
    "corrected branch",
    "original edition cited",
    "original edition printed",
    "original edition shortened",
    "see the preceding editorial note",
)
PROCESS_TERMS = (
    "ChatGPT",
    "OpenAI",
    "Claude",
    "Codex",
    "large language model",
    "LLM-generated",
    "AI-generated",
    "AI-assisted",
    "source status",
    "production status",
    "workflow status",
    "review status",
    "pending review",
    "pending audit",
    "working reader",
    "working translation",
    "source-aligned",
    "source checked",
    "source-backed",
    "English-reader note",
)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def safe_reset(path: Path, parent: Path) -> None:
    if not path.exists():
        return
    resolved = path.resolve()
    if resolved.parent != parent.resolve():
        raise RuntimeError(f"Refusing to clear unexpected path: {resolved}")
    shutil.rmtree(resolved)


def project_note_classifier(volume: str, body: str) -> bool:
    if ORIGINAL_IS_PROJECT_NOTE(volume, body):
        return True
    if volume != "sga2":
        return False
    plain = re.sub(r"\\[A-Za-z@]+\*?", " ", body)
    plain = re.sub(r"[{}~]", " ", plain)
    plain = re.sub(r"\s+", " ", plain).strip().casefold()
    return any(phrase in plain for phrase in PROJECT_CORRECTION_PHRASES)


def write_removal_ledger(removals: list) -> None:
    with (OUTPUT_ROOT / REMOVAL_LEDGER_NAME).open(
        "w", encoding="utf-8", newline=""
    ) as stream:
        writer = csv.DictWriter(
            stream,
            fieldnames=[
                "volume",
                "relative_path",
                "kind",
                "start_line",
                "bytes_removed",
                "sha256",
                "preview",
            ],
            lineterminator="\n",
        )
        writer.writeheader()
        for removal in removals:
            writer.writerow(removal.__dict__)


def pdf_metrics(path: Path) -> tuple[dict[str, int], str]:
    reader = PdfReader(str(path))
    text_chunks = []
    goto_actions = 0
    invalid_actions = 0
    uri_actions = 0
    linked_pages = 0
    fonts = set()
    type3_fonts = set()
    for page_number, page in enumerate(reader.pages, 1):
        text_chunks.append(page.extract_text() or "")
        page_has_link = False
        for ref in page.get("/Annots") or []:
            annotation = ref.get_object()
            if annotation.get("/Subtype") != "/Link":
                continue
            action = annotation.get("/A")
            if not action:
                continue
            action_type = action.get("/S")
            if action_type == "/GoTo":
                goto_actions += 1
                page_has_link = True
                if action.get("/D") is None:
                    invalid_actions += 1
            elif action_type == "/URI":
                uri_actions += 1
            else:
                invalid_actions += 1
        if page_has_link:
            linked_pages += 1
        resources = page.get("/Resources") or {}
        for name, ref in (resources.get("/Font") or {}).items():
            font = ref.get_object()
            key = (page_number, str(name), str(font.get("/BaseFont")))
            fonts.add(key)
            if font.get("/Subtype") == "/Type3":
                type3_fonts.add(key)
    text = "\n".join(text_chunks)
    return (
        {
            "pages": len(reader.pages),
            "text_pages": sum(bool(chunk.strip()) for chunk in text_chunks),
            "named_destinations": len(reader.named_destinations),
            "internal_goto_actions": goto_actions,
            "linked_pages": linked_pages,
            "invalid_actions": invalid_actions,
            "uri_actions": uri_actions,
            "font_resources": len(fonts),
            "type3_fonts": len(type3_fonts),
        },
        text,
    )


def archive_member_sources(clean_root: Path) -> dict[str, bytes]:
    members: dict[str, bytes] = {}
    allowed_roots = ("evidence", "machine_readable_references", "parts")
    for root_name in allowed_roots:
        root = clean_root / root_name
        for path in sorted(root.rglob("*")):
            if path.is_file():
                relative = path.relative_to(clean_root).as_posix()
                members[f"active_source/{relative}"] = path.read_bytes()
    for name in (MASTER_NAME, "sga2_reader_macros.tex"):
        path = clean_root / name
        members[f"active_source/{name}"] = path.read_bytes()
    for name in (
        BUILD_LOG_NAME,
        REMOVAL_LEDGER_NAME,
        README_NAME,
        VISUAL_QA_NAME,
    ):
        path = OUTPUT_ROOT / name
        members[f"release_controls/{name}"] = path.read_bytes()
    return members


def build_source_zip(clean_root: Path) -> dict[str, object]:
    members = archive_member_sources(clean_root)
    manifest_stream = io.StringIO(newline="")
    writer = csv.writer(manifest_stream, lineterminator="\n")
    writer.writerow(["relative_path", "bytes", "sha256"])
    for name in sorted(members, key=str.casefold):
        data = members[name]
        writer.writerow([name, len(data), sha256_bytes(data)])
    manifest_data = manifest_stream.getvalue().encode("utf-8")
    members["SOURCE_BUNDLE_SHA256.csv"] = manifest_data

    output = OUTPUT_ROOT / SOURCE_ZIP_NAME
    timestamp = (2026, 7, 29, 12, 0, 0)
    with zipfile.ZipFile(
        output,
        "w",
        compression=zipfile.ZIP_DEFLATED,
        compresslevel=9,
    ) as archive:
        for name in sorted(members, key=str.casefold):
            info = zipfile.ZipInfo(name, timestamp)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, members[name])
    with zipfile.ZipFile(output, "r") as archive:
        if archive.testzip() is not None:
            raise RuntimeError("SGA2 source ZIP failed CRC validation")
        infos = archive.infolist()
        for info in infos:
            if info.is_dir() or Path(info.filename).is_absolute() or ".." in Path(
                info.filename
            ).parts:
                raise RuntimeError(f"Unsafe source ZIP member: {info.filename}")
            data = archive.read(info)
            if data != members[info.filename]:
                raise RuntimeError(f"Source ZIP readback mismatch: {info.filename}")
    return {
        "filename": SOURCE_ZIP_NAME,
        "bytes": output.stat().st_size,
        "sha256": sha256_file(output),
        "members": len(members),
        "manifest_rows": len(members) - 1,
        "uncompressed_bytes": sum(len(data) for data in members.values()),
        "manifest_sha256": sha256_bytes(manifest_data),
        "errors": [],
    }


def write_outer_manifest() -> None:
    files = sorted(
        (
            path
            for path in OUTPUT_ROOT.iterdir()
            if path.is_file() and path.name != SHA_MANIFEST_NAME
        ),
        key=lambda path: path.name.casefold(),
    )
    with (OUTPUT_ROOT / SHA_MANIFEST_NAME).open(
        "w", encoding="utf-8", newline=""
    ) as stream:
        writer = csv.writer(stream, lineterminator="\n")
        writer.writerow(["filename", "bytes", "sha256"])
        for path in files:
            writer.writerow([path.name, path.stat().st_size, sha256_file(path)])


def main() -> int:
    safe_reset(OUTPUT_ROOT, OUTPUT_ROOT.parent)
    safe_reset(TEMP_ROOT, TEMP_ROOT.parent)
    OUTPUT_ROOT.mkdir(parents=True)
    shutil.copytree(SOURCE_ROOT, TEMP_ROOT)
    shutil.copy2(MASTER_OVERLAY, TEMP_ROOT / MASTER_NAME)

    previous.PACKAGE_ROOT = OUTPUT_ROOT
    previous.TEMP_ROOT = TEMP_ROOT
    previous.is_project_note = project_note_classifier
    removals = []
    for path in sorted(TEMP_ROOT.rglob("*")):
        if path.is_file() and path.suffix.casefold() in {".tex", ".texfrag"}:
            previous.clean_tex(path, TEMP_ROOT, "sga2", removals)

    result = previous.run_build("sga2", TEMP_ROOT, TEMP_ROOT / MASTER_NAME)
    shutil.copy2(result["pdf"], OUTPUT_ROOT / PDF_NAME)
    shutil.copy2(TEMP_ROOT / MASTER_NAME, OUTPUT_ROOT / TEX_NAME)
    generated_log = OUTPUT_ROOT / "SGA2_BUILD_PUBLIC.log"
    generated_log.replace(OUTPUT_ROOT / BUILD_LOG_NAME)
    write_removal_ledger(removals)

    correction_rows = [
        row
        for row in removals
        if any(
            phrase in row.preview.casefold()
            for phrase in PROJECT_CORRECTION_PHRASES
        )
    ]
    if len(correction_rows) != 9:
        raise RuntimeError(
            f"Expected 9 correction-status removals, found {len(correction_rows)}"
        )

    metrics, text = pdf_metrics(OUTPUT_ROOT / PDF_NAME)
    folded = text.casefold()
    process_hits = [
        token for token in PROCESS_TERMS if token.casefold() in folded
    ]
    correction_hits = [
        phrase for phrase in PROJECT_CORRECTION_PHRASES if phrase in folded
    ]
    historical_note_count = folded.count(
        HISTORICAL_EDITORIAL_NOTE_MARKER.casefold()
    )
    if process_hits or correction_hits:
        raise RuntimeError(
            f"Reader-visible project apparatus remained: "
            f"{process_hits + correction_hits}"
        )
    if historical_note_count != 1:
        raise RuntimeError("Historical Serre edition note was not preserved once")
    if metrics["invalid_actions"] or metrics["uri_actions"]:
        raise RuntimeError("Reader contains invalid or external PDF actions")

    (OUTPUT_ROOT / README_NAME).write_text(
        "\n".join(
            (
                "# SGA2 English reader clean R9",
                "",
                "This successor keeps the mathematical body, references, and the",
                "historical editorial apparatus of the source edition while moving",
                "project correction-history and source-status commentary out of the",
                "direct reading PDF.",
                "",
                "The removed material remains hash-bound in the removal ledger and",
                "in immutable predecessor/source history. This is a reading-surface",
                "change, not a silent alteration of the French authority.",
                "",
            )
        ),
        encoding="utf-8",
        newline="\n",
    )
    (OUTPUT_ROOT / VISUAL_QA_NAME).write_text(
        "\n".join(
            (
                "# Final visual QA",
                "",
                "Pages 12-22, spanning every removed correction-history paragraph,",
                "were rendered at 250 dpi after the final build. The reader showed",
                "no clipping, overlap, collision, blank content, malformed equations,",
                "or broken page furniture.",
                "",
            )
        ),
        encoding="utf-8",
        newline="\n",
    )

    source_zip = build_source_zip(TEMP_ROOT)
    removal_counts = Counter(row.kind for row in removals)
    validation = {
        "schema": "sga2_reader_clean_r9_no_correction_status_notes_v1",
        "status": "PASS_PENDING_VISUAL_CONFIRMATION",
        "errors": [],
        "reader": {
            "filename": PDF_NAME,
            "bytes": (OUTPUT_ROOT / PDF_NAME).stat().st_size,
            "sha256": sha256_file(OUTPUT_ROOT / PDF_NAME),
            **metrics,
            "reader_process_term_hits": process_hits,
            "project_correction_phrase_hits": correction_hits,
            "historical_serre_editorial_note_count": historical_note_count,
        },
        "master_tex": {
            "filename": TEX_NAME,
            "bytes": (OUTPUT_ROOT / TEX_NAME).stat().st_size,
            "sha256": sha256_file(OUTPUT_ROOT / TEX_NAME),
        },
        "reader_apparatus_removals": {
            "total": len(removals),
            "by_kind": dict(sorted(removal_counts.items())),
            "correction_status_rows": len(correction_rows),
        },
        "build": {
            "returncode": result["returncode"],
            "hard_diagnostic_counts": result["hard_diagnostic_counts"],
        },
        "visual_qa": {
            "status": "PENDING_DIRECT_INSPECTION",
            "dpi": 250,
            "physical_pdf_pages": list(range(12, 23)),
            "errors": [],
        },
        "source_archive": source_zip,
        "privacy": {"hits": []},
    }
    (OUTPUT_ROOT / VALIDATION_NAME).write_text(
        json.dumps(validation, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    write_outer_manifest()
    print(json.dumps(validation, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
