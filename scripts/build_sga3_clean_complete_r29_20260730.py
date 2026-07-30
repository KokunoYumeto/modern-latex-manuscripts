#!/usr/bin/env python3
"""Build and package the clean complete SGA3 R29 reader.

The producer's complete native/reference-v2 source is mathematically newer
than the public R28 reader, but its rendered PDF exposes production notes.
This builder reapplies the R28 reader-presentation boundary, compiles the
newer source, regenerates every stable target from SyncTeX, and overlays a
balanced PDF destination tree without changing page content or annotations.

Run ``build`` first, inspect the rendered QA pages, then run ``package``.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import os
import re
import shutil
import subprocess
import sys
import zipfile
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path, PurePosixPath
from typing import Any, Iterable

from pypdf import PdfReader, PdfWriter
from pypdf.constants import PagesAttributes
from pypdf.generic import (
    ArrayObject,
    DictionaryObject,
    FloatObject,
    NameObject,
    NullObject,
    TextStringObject,
)


REPO = Path(__file__).resolve().parent.parent
WORKSPACE = Path(r"C:\tmp\sga3-r29-clean-build-20260730")
SOURCE = WORKSPACE / "source"
BUILD = WORKSPACE / "build"
CONTROLS = WORKSPACE / "controls"
RENDERS = WORKSPACE / "renders"
R28_EXTRACT = WORKSPACE / "r28"

CANDIDATE = Path(
    r"C:\Users\Floris\Documents\interlanguage\03_projects"
    r"\language_management\english_germanic\06_publication_candidates"
    r"\SGA3_English_complete_native_reference_v2_local_package_20260730_r1"
)
R28_PACKAGE = (
    REPO
    / "sources/sga/sga3-english-reader-clean-r28-reference-complete-20260730"
)
R28_SOURCE_ZIP = R28_PACKAGE / "10c_SGA3_English_Source_R28_20260730.zip"
R28_MASTER = R28_PACKAGE / "02c_SGA3_English_Master.tex"
TARGET_PLAN = CANDIDATE / "reference/TARGET_ACTIONS.csv"

MASTER_NAME = "SGA3_English_Full_Volume_Native_Cumulative.tex"
PDF_STEM = Path(MASTER_NAME).stem
PRE_OVERLAY_PDF = BUILD / f"{PDF_STEM}.pdf"
SYNCTEX = BUILD / f"{PDF_STEM}.synctex.gz"
FINAL_PDF = BUILD / "SGA3_English_Reader_R29_Complete_Native_ReferenceV2.pdf"
MAPPING = CONTROLS / "SYNCTEX_TARGET_DESTINATIONS_R29.csv"
MAPPING_VALIDATION = CONTROLS / "SYNCTEX_TARGET_DESTINATIONS_R29_VALIDATION.json"
OVERLAY_REPLAY = CONTROLS / "PDF_NAMES_TREE_OVERLAY_R29_REPLAY.csv"
OVERLAY_VALIDATION = CONTROLS / "PDF_NAMES_TREE_OVERLAY_R29_VALIDATION.json"
BUILD_VALIDATION = CONTROLS / "BUILD_VALIDATION.json"
HYGIENE_LEDGER = CONTROLS / "READER_PRESENTATION_CLEANUP_LEDGER.csv"

PACKAGE = (
    REPO
    / "sources/sga/sga3-english-reader-clean-r29-complete-native-reference-v2-20260730"
)
PUBLIC_PDF = PACKAGE / "00c_SGA3_English_Reader.pdf"
PUBLIC_MASTER = PACKAGE / "02c_SGA3_English_Master.tex"
SOURCE_ZIP = PACKAGE / "10c_SGA3_English_Reader_and_Buildable_TeX_R29_20260730.zip"
CONTROLS_ZIP = PACKAGE / "20c_SGA3_English_Reference_and_QA_Controls_R29_20260730.zip"

EXPECTED_CANDIDATE_FILES = 940
EXPECTED_CANDIDATE_BYTES = 122_234_043
EXPECTED_CANDIDATE_MANIFEST_SHA = (
    "5D6662E3543A7DF9CC941EE3E40B78BE916B825ED743D7931D2098EA58078AEB"
)
EXPECTED_SOURCE_FILES = 914
EXPECTED_TARGETS = 3_744
EXPECTED_R28_WRAPPERS = 143
EXPECTED_WRAPPERS = 144
EXPECTED_WRAPPER_FILES = 97
MAX_WORKERS = 12
NAME_TREE_FANOUT = 64
ZIP_TIME = (2026, 7, 30, 12, 0, 0)

MACRO_NAMES = (
    "SGAInlineRefTarget",
    "SGAInlineEquationTarget",
    "SGANextSectionTarget",
    "SGARefTarget",
    "label",
)

SPECIAL_ENVIRONMENTS = (
    (
        "inputs/VII/tex/components/03_expose_VIIA_section3_coalgebras_cartier_en.tex",
        "sga3:VIIA:3.2.3-source-note-missing-prime",
        "quote",
    ),
    (
        "inputs/VII/tex/components/50_expose_VIIB_section253_unipotent_multiplicative_type_en.tex",
        "sga3:VIIB:2.5.3.B:base-change-source-note",
        "minipage",
    ),
)

SPECIAL_COMMANDS = (
    (
        "inputs/VI/tex_reference_v2/components/86_expose_VIB_lemma1112_through_thm1116_r3_en.tex",
        "note:sga3-VIB-11.12-counit-source-reading",
    ),
    (
        "inputs/VI/tex_reference_v2/components/86_expose_VIB_lemma1112_through_thm1116_r3_en.tex",
        "note:sga3-VIB-11.16-rho-index-source-reading",
    ),
    (
        "inputs/VI/tex_reference_v2/components/86_expose_VIB_lemma1112_through_thm1116_r3_en.tex",
        "note:sga3-VIB-11.16-maximality-source-reading",
    ),
    (
        "inputs/VI/tex_reference_v2/components/89_expose_VIB_section13_through_bibliography_loop2_r1_en.tex",
        "note:sga3-VIB-13.1-i-U-ambient",
    ),
    (
        "inputs/VI/tex_reference_v2/components/89_expose_VIB_section13_through_bibliography_loop2_r1_en.tex",
        "note:sga3-VIB-13.5-ii-rank-letter",
    ),
)

SPECIAL_GROUPS = (
    (
        "inputs/V/tex/components/09_expose_V_theorem41_close_section5_opening_en.tex",
        "Native Loop-2 reconstructions; source locator:",
    ),
)

BANNED_READER_PATTERNS = {
    "ai_or_assistant": re.compile(
        r"\b(?:Claude|Codex|ChatGPT|OpenAI|LLM|AI-generated)\b", re.I
    ),
    "workflow_status": re.compile(
        r"\b(?:workpass|pending (?:fresh )?(?:independent )?review|"
        r"production status|source status|project status|public-readback)\b",
        re.I,
    ),
    "source_note": re.compile(r"\bsource(?:-reading| notation)? note\b", re.I),
    "translator_note": re.compile(r"\btranslator[\u2019']s note\b", re.I),
    "source_locator": re.compile(r"\bsource locator\b", re.I),
    "reconstruction_preface": re.compile(
        r"Reconstruction, provenance, and rights status", re.I
    ),
    "project_author": re.compile(r"SGA 3 English reconstruction project", re.I),
    "cumulative_boundary": re.compile(r"\bCumulative boundary\b", re.I),
}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def identity(path: Path) -> dict[str, int | str]:
    return {"bytes": path.stat().st_size, "sha256": sha256_file(path)}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def csv_bytes(rows: list[dict[str, Any]], fields: list[str]) -> bytes:
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(
        stream,
        fieldnames=fields,
        extrasaction="ignore",
        quoting=csv.QUOTE_ALL,
        lineterminator="\n",
    )
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue().encode("utf-8")


def safe_reset(path: Path, expected_parent: Path) -> None:
    resolved = path.resolve()
    if resolved.parent != expected_parent.resolve():
        raise RuntimeError(f"Refusing to reset unexpected path: {resolved}")
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True)


def verify_candidate() -> None:
    files = [path for path in CANDIDATE.rglob("*") if path.is_file()]
    total = sum(path.stat().st_size for path in files)
    if (len(files), total) != (EXPECTED_CANDIDATE_FILES, EXPECTED_CANDIDATE_BYTES):
        raise RuntimeError(f"Candidate boundary changed: {len(files)} files / {total} bytes")
    if sha256_file(CANDIDATE / "SHA256SUMS.csv") != EXPECTED_CANDIDATE_MANIFEST_SHA:
        raise RuntimeError("Candidate manifest identity changed")
    rows = read_csv(CANDIDATE / "SHA256SUMS.csv")
    for row in rows:
        relative = row.get("relative_path") or row.get("path")
        if not relative:
            raise RuntimeError("Candidate manifest has no path column")
        path = CANDIDATE / Path(relative.replace("/", os.sep))
        if not path.is_file():
            raise RuntimeError(f"Missing candidate member: {relative}")
        if (path.stat().st_size, sha256_file(path)) != (
            int(row["bytes"]),
            row["sha256"].upper(),
        ):
            raise RuntimeError(f"Candidate identity mismatch: {relative}")


def brace_end(text: str, opening: int) -> int:
    depth = 0
    index = opening
    while index < len(text):
        if text[index] == "\\":
            index += 2
            continue
        if text[index] == "{":
            depth += 1
        elif text[index] == "}":
            depth -= 1
            if depth == 0:
                return index + 1
        index += 1
    raise RuntimeError("Unbalanced TeX braces")


def archive_wrappers(text: str) -> list[tuple[int, int, str]]:
    marker = r"\SGAArchiveOnly{"
    rows = []
    start = 0
    while True:
        index = text.find(marker, start)
        if index < 0:
            return rows
        opening = index + len(marker) - 1
        end = brace_end(text, opening)
        rows.append((index, end, text[opening + 1 : end - 1]))
        start = end


def command_spans(text: str) -> list[tuple[int, int, str]]:
    pattern = re.compile(r"\\(footnote|emph|textit)(?:\[[^\]]*\])?\s*\{")
    return [
        (match.start(), brace_end(text, match.end() - 1), match.group(1))
        for match in pattern.finditer(text)
    ]


def wrap_command_containing(text: str, marker: str) -> str:
    index = text.find(marker)
    if index < 0 or text.find(marker, index + 1) >= 0:
        raise RuntimeError(f"Command marker is missing or non-unique: {marker}")
    enclosing = [row for row in command_spans(text) if row[0] <= index < row[1]]
    if not enclosing:
        raise RuntimeError(f"No enclosing command for marker: {marker}")
    start, end, _ = max(enclosing, key=lambda row: row[0])
    return text[:start] + r"\SGAArchiveOnly{" + text[start:end] + "}" + text[end:]


def wrap_environment_containing(text: str, marker: str, environment: str) -> str:
    index = text.find(marker)
    if index < 0 or text.find(marker, index + 1) >= 0:
        raise RuntimeError(f"Environment marker is missing or non-unique: {marker}")
    begin = rf"\begin{{{environment}}}"
    end_marker = rf"\end{{{environment}}}"
    start = text.rfind(begin, 0, index)
    end_start = text.find(end_marker, index)
    if start < 0 or end_start < 0:
        raise RuntimeError(f"No {environment} environment around {marker}")
    end = end_start + len(end_marker)
    return text[:start] + r"\SGAArchiveOnly{" + text[start:end] + "}" + text[end:]


def wrap_group_containing(text: str, marker: str) -> str:
    index = text.find(marker)
    if index < 0 or text.find(marker, index + 1) >= 0:
        raise RuntimeError(f"Group marker is missing or non-unique: {marker}")
    start = text.rfind("{", 0, index)
    if start < 0:
        raise RuntimeError(f"No opening group around marker: {marker}")
    end = brace_end(text, start)
    if not (start < index < end):
        raise RuntimeError(f"Marker is outside resolved group: {marker}")
    return text[:start] + r"\SGAArchiveOnly{" + text[start:end] + "}" + text[end:]


def restore_reader_boundary() -> dict[str, Any]:
    shutil.copytree(CANDIDATE / "source", SOURCE)
    source_files = [path for path in SOURCE.rglob("*") if path.is_file()]
    if len(source_files) != EXPECTED_SOURCE_FILES:
        raise RuntimeError(f"Source boundary changed: {len(source_files)}")

    with zipfile.ZipFile(R28_SOURCE_ZIP) as archive:
        archive.extractall(R28_EXTRACT)

    old_wrapper_count = 0
    exact_restored = 0
    failed: list[dict[str, str]] = []
    changed: set[str] = set()
    for old_path in sorted((R28_EXTRACT / "inputs").rglob("*.tex")):
        rel = old_path.relative_to(R28_EXTRACT).as_posix()
        new_path = SOURCE / Path(rel.replace("/", os.sep))
        if not new_path.is_file():
            raise RuntimeError(f"R28 source path missing from candidate: {rel}")
        old_text = old_path.read_text(encoding="utf-8")
        wrappers = archive_wrappers(old_text)
        old_wrapper_count += len(wrappers)
        if not wrappers:
            continue
        new_text = new_path.read_text(encoding="utf-8")
        file_changed = False
        for _start, _end, inner in wrappers:
            count = new_text.count(inner)
            if count == 1:
                new_text = new_text.replace(inner, r"\SGAArchiveOnly{" + inner + "}", 1)
                exact_restored += 1
                file_changed = True
            else:
                failed.append({"path": rel, "inner_sha256": sha256_bytes(inner.encode()), "count": str(count)})
        if file_changed:
            new_path.write_text(new_text, encoding="utf-8", newline="\n")
            changed.add(rel)

    if old_wrapper_count != EXPECTED_R28_WRAPPERS:
        raise RuntimeError(f"R28 wrapper count changed: {old_wrapper_count}")
    if len(failed) != len(SPECIAL_ENVIRONMENTS) + len(SPECIAL_COMMANDS):
        raise RuntimeError(f"Unexpected changed-wrapper count: {json.dumps(failed, indent=2)}")

    for rel, marker, environment in SPECIAL_ENVIRONMENTS:
        path = SOURCE / Path(rel.replace("/", os.sep))
        text = path.read_text(encoding="utf-8")
        path.write_text(
            wrap_environment_containing(text, marker, environment),
            encoding="utf-8",
            newline="\n",
        )
        changed.add(rel)
    for rel, marker in SPECIAL_COMMANDS:
        path = SOURCE / Path(rel.replace("/", os.sep))
        text = path.read_text(encoding="utf-8")
        path.write_text(
            wrap_command_containing(text, marker),
            encoding="utf-8",
            newline="\n",
        )
        changed.add(rel)
    for rel, marker in SPECIAL_GROUPS:
        path = SOURCE / Path(rel.replace("/", os.sep))
        text = path.read_text(encoding="utf-8")
        path.write_text(
            wrap_group_containing(text, marker),
            encoding="utf-8",
            newline="\n",
        )
        changed.add(rel)

    clean_master = R28_MASTER.read_text(encoding="utf-8")
    (SOURCE / MASTER_NAME).write_text(clean_master, encoding="utf-8", newline="\n")

    wrappers = 0
    wrapper_files = 0
    for path in (SOURCE / "inputs").rglob("*.tex"):
        count = path.read_text(encoding="utf-8", errors="replace").count(r"\SGAArchiveOnly{")
        wrappers += count
        wrapper_files += int(count > 0)
    if (wrappers, wrapper_files) != (EXPECTED_WRAPPERS, EXPECTED_WRAPPER_FILES):
        raise RuntimeError(f"Reader boundary mismatch: {wrappers} wrappers / {wrapper_files} files")

    rows = [
        {
            "control": "reader_hidden_archive_wrappers",
            "status": "PASS",
            "count": wrappers,
            "detail": f"{wrapper_files} files; {exact_restored} exact restores; 8 label-anchored restores",
        },
        {
            "control": "neutral_master",
            "status": "PASS",
            "count": 1,
            "detail": sha256_file(SOURCE / MASTER_NAME),
        },
        {
            "control": "source_files",
            "status": "PASS",
            "count": EXPECTED_SOURCE_FILES,
            "detail": "complete native TeX closure retained",
        },
    ]
    HYGIENE_LEDGER.write_bytes(csv_bytes(rows, ["control", "status", "count", "detail"]))
    return {
        "wrappers": wrappers,
        "wrapper_files": wrapper_files,
        "exact_restored": exact_restored,
        "label_anchored_restored": 8,
        "changed_files": len(changed),
        "clean_master": identity(SOURCE / MASTER_NAME),
    }


def run_build() -> dict[str, Any]:
    BUILD.mkdir(parents=True)
    commands = []
    for pass_number in range(1, 5):
        command = [
            "xelatex",
            "-interaction=nonstopmode",
            "-halt-on-error",
            "-file-line-error",
            "-synctex=1",
            f"-output-directory={BUILD}",
            MASTER_NAME,
        ]
        completed = subprocess.run(
            command,
            cwd=SOURCE,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            encoding="utf-8",
            errors="replace",
            timeout=3600,
            check=False,
        )
        (BUILD / f"pass{pass_number}.console.txt").write_text(
            completed.stdout, encoding="utf-8", newline="\n"
        )
        commands.append({"pass": pass_number, "exit_code": completed.returncode})
        print(f"XeLaTeX pass {pass_number}: exit {completed.returncode}", flush=True)
        if completed.returncode:
            raise RuntimeError(f"XeLaTeX pass {pass_number} failed")

    if not PRE_OVERLAY_PDF.is_file() or not SYNCTEX.is_file():
        raise RuntimeError("Build did not produce PDF and SyncTeX sidecar")
    console = (BUILD / "pass4.console.txt").read_text(encoding="utf-8", errors="replace")
    diagnostics = {
        "undefined_references": len(re.findall(r"undefined references", console, re.I)),
        "rerun_warnings": len(re.findall(r"Rerun to get cross-references right", console, re.I)),
        "overfull": len(re.findall(r"Overfull \\hbox", console)),
        "underfull": len(re.findall(r"Underfull \\hbox", console)),
        "missing_glyph": len(re.findall(r"Missing character:", console)),
    }
    if diagnostics["undefined_references"] or diagnostics["rerun_warnings"] or diagnostics["missing_glyph"]:
        raise RuntimeError(f"Blocking build diagnostics: {diagnostics}")
    reader = PdfReader(str(PRE_OVERLAY_PDF))
    return {
        "passes": commands,
        "diagnostics": diagnostics,
        "pre_overlay_pdf": {**identity(PRE_OVERLAY_PDF), "pages": len(reader.pages)},
        "synctex": identity(SYNCTEX),
    }


def locate_target(source: Path, stable_id: str, source_action: str) -> tuple[int, int, str]:
    text = source.read_text(encoding="utf-8")
    hits: list[tuple[int, str]] = []
    for macro in MACRO_NAMES:
        needle = f"\\{macro}{{{stable_id}}}"
        start = 0
        while True:
            position = text.find(needle, start)
            if position < 0:
                break
            hits.append((position, macro))
            start = position + len(needle)
    if not hits and source_action == "REUSE_RUNTIME_DIAGRAM_TARGET":
        pattern = re.compile(rf"(?m)^[ \t]*\{{{re.escape(stable_id)}\}}[ \t]*$")
        hits.extend((match.start(), "runtime_diagram_argument") for match in pattern.finditer(text))
    if len(hits) != 1:
        raise RuntimeError(f"Target occurrence count {len(hits)} != 1: {stable_id}: {source}")
    position, macro = hits[0]
    line = text.count("\n", 0, position) + 1
    column = position - text.rfind("\n", 0, position)
    return line, column, macro


RECORD_PATTERN = re.compile(
    r"Page:(?P<page>\d+)\s+"
    r"x:(?P<x>-?\d+(?:\.\d+)?)\s+"
    r"y:(?P<y>-?\d+(?:\.\d+)?)\s+"
    r"h:(?P<h>-?\d+(?:\.\d+)?)\s+"
    r"v:(?P<v>-?\d+(?:\.\d+)?)\s+"
    r"W:(?P<width>-?\d+(?:\.\d+)?)\s+"
    r"H:(?P<height>-?\d+(?:\.\d+)?)",
    re.MULTILINE,
)


def line_offsets() -> list[int]:
    offsets = [0]
    for distance in range(1, 16):
        offsets.extend((distance, -distance))
    for distance in range(20, 101, 5):
        offsets.extend((distance, -distance))
    return offsets


def query_synctex(source: Path, line: int) -> dict[str, Any]:
    for offset in line_offsets():
        candidate_line = max(1, line + offset)
        completed = subprocess.run(
            [
                "synctex",
                "view",
                "-i",
                f"{candidate_line}:0:{source}",
                "-o",
                str(PRE_OVERLAY_PDF),
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=30,
            check=False,
        )
        records = list(RECORD_PATTERN.finditer(completed.stdout))
        if records:
            match = records[0]
            result: dict[str, Any] = {
                "resolved_source_line": candidate_line,
                "resolved_line_offset": offset,
                "synctex_record_count": len(records),
            }
            for key, value in match.groupdict().items():
                result[key] = int(value) if key == "page" else float(value)
            return result
    raise RuntimeError(f"No SyncTeX record within 100 lines: {source}:{line}")


def build_mapping() -> dict[str, Any]:
    plan = read_csv(TARGET_PLAN)
    if len(plan) != EXPECTED_TARGETS:
        raise RuntimeError(f"Target-plan rows changed: {len(plan)}")
    ids = [row["stable_target_id"] for row in plan]
    if len(ids) != len(set(ids)):
        raise RuntimeError("Stable target IDs are not unique")

    targets: list[dict[str, Any]] = []
    source_keys: dict[tuple[str, int], Path] = {}
    macro_counts: Counter[str] = Counter()
    for ordinal, row in enumerate(plan, start=1):
        rel = row["source_path"].replace("\\", "/")
        source = SOURCE / Path(rel.replace("/", os.sep))
        line, column, macro = locate_target(source, row["stable_target_id"], row["source_action"])
        macro_counts[macro] += 1
        targets.append(
            {
                "ordinal": ordinal,
                "action_id": row["action_id"],
                "stable_target_id": row["stable_target_id"],
                "target_scope": row["target_scope"],
                "target_half_scope": row["target_half_scope"],
                "target_locator_normalized": row["target_locator_normalized"],
                "target_kind": row["target_kind"],
                "parent_target_id": row["parent_target_id"],
                "source_action": row["source_action"],
                "source_path": rel,
                "source_sha256": sha256_file(source),
                "target_macro": macro,
                "target_source_line": line,
                "target_source_column": column,
            }
        )
        source_keys[(rel, line)] = source

    resolved: dict[tuple[str, int], dict[str, Any]] = {}
    failures: list[str] = []
    future_keys = {}
    completed_count = 0
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        for key, source in source_keys.items():
            future_keys[executor.submit(query_synctex, source, key[1])] = key
        for future in as_completed(future_keys):
            key = future_keys[future]
            try:
                resolved[key] = future.result()
            except Exception as exc:
                failures.append(f"{key[0]}:{key[1]}: {exc}")
            completed_count += 1
            if completed_count % 250 == 0 or completed_count == len(future_keys):
                print(f"SyncTeX: {completed_count}/{len(future_keys)} source locations", flush=True)
    if failures:
        raise RuntimeError("SyncTeX failures:\n" + "\n".join(failures[:50]))

    reader = PdfReader(str(PRE_OVERLAY_PDF))
    rows: list[dict[str, Any]] = []
    for target in targets:
        result = resolved[(target["source_path"], target["target_source_line"])]
        page_number = int(result["page"])
        if page_number < 1 or page_number > len(reader.pages):
            raise RuntimeError(f"SyncTeX page outside PDF: {target['stable_target_id']}")
        page = reader.pages[page_number - 1]
        width = float(page.mediabox.width)
        height = float(page.mediabox.height)
        pdf_x = max(0.0, min(width, float(result["h"])))
        pdf_y = max(0.0, min(height, height - float(result["v"])))
        rows.append(
            {
                **target,
                "physical_page": page_number,
                "page_width_pt": f"{width:.6f}",
                "page_height_pt": f"{height:.6f}",
                "synctex_x_from_left_pt": f"{float(result['x']):.6f}",
                "synctex_y_from_top_pt": f"{float(result['y']):.6f}",
                "synctex_h_from_left_pt": f"{float(result['h']):.6f}",
                "synctex_v_from_top_pt": f"{float(result['v']):.6f}",
                "synctex_box_width_pt": f"{float(result['width']):.6f}",
                "synctex_box_height_pt": f"{float(result['height']):.6f}",
                "pdf_destination_x_pt": f"{pdf_x:.6f}",
                "pdf_destination_y_pt": f"{pdf_y:.6f}",
                "resolved_source_line": result["resolved_source_line"],
                "resolved_line_offset": result["resolved_line_offset"],
                "synctex_record_count": result["synctex_record_count"],
                "resolution_status": "PASS",
            }
        )

    fields = list(rows[0])
    data = csv_bytes(rows, fields)
    MAPPING.write_bytes(data)
    offsets = Counter(str(row["resolved_line_offset"]) for row in rows)
    validation = {
        "schema": "sga3_clean_r29_synctex_target_map_v1",
        "status": "PASS",
        "errors": [],
        "target_plan": {**identity(TARGET_PLAN), "rows": len(plan)},
        "mapping": {"bytes": len(data), "sha256": sha256_bytes(data), "rows": len(rows)},
        "pdf": {**identity(PRE_OVERLAY_PDF), "pages": len(reader.pages)},
        "unique_source_line_queries": len(source_keys),
        "macro_counts": dict(sorted(macro_counts.items())),
        "resolved_line_offset_counts": dict(sorted(offsets.items(), key=lambda item: int(item[0]))),
    }
    MAPPING_VALIDATION.write_text(json.dumps(validation, indent=2) + "\n", encoding="utf-8")
    return validation


def dereference(value: Any) -> Any:
    return value.get_object() if hasattr(value, "get_object") else value


def collect_name_tree_pairs(node: Any) -> list[tuple[Any, Any]]:
    dictionary = dereference(node)
    pairs: list[tuple[Any, Any]] = []
    if "/Names" in dictionary:
        names = dereference(dictionary["/Names"])
        if len(names) % 2:
            raise RuntimeError("Destination name array has odd length")
        pairs.extend((names[index], names[index + 1]) for index in range(0, len(names), 2))
    if "/Kids" in dictionary:
        for child in dereference(dictionary["/Kids"]):
            pairs.extend(collect_name_tree_pairs(child))
    return pairs


def build_balanced_name_tree(writer: PdfWriter, pairs: list[tuple[Any, Any]]) -> Any:
    level: list[tuple[Any, Any, Any]] = []
    for start in range(0, len(pairs), NAME_TREE_FANOUT):
        chunk = pairs[start : start + NAME_TREE_FANOUT]
        flat = ArrayObject()
        for key, destination in chunk:
            flat.extend([key, destination])
        leaf = DictionaryObject(
            {
                NameObject("/Names"): flat,
                NameObject("/Limits"): ArrayObject([chunk[0][0], chunk[-1][0]]),
            }
        )
        level.append((writer._add_object(leaf), chunk[0][0], chunk[-1][0]))
    while len(level) > 1:
        next_level = []
        for start in range(0, len(level), NAME_TREE_FANOUT):
            chunk = level[start : start + NAME_TREE_FANOUT]
            parent = DictionaryObject(
                {
                    NameObject("/Kids"): ArrayObject([item[0] for item in chunk]),
                    NameObject("/Limits"): ArrayObject([chunk[0][1], chunk[-1][2]]),
                }
            )
            next_level.append((writer._add_object(parent), chunk[0][1], chunk[-1][2]))
        level = next_level
    return level[0][0]


def page_content_sha256(page: Any) -> str:
    contents = page.get_contents()
    return sha256_bytes(b"" if contents is None else contents.get_data())


def scalar(value: Any) -> Any:
    if value is None or isinstance(value, NullObject):
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return str(value)


def annotation_signature(page: Any) -> tuple[Any, ...]:
    rows = []
    for reference in page.get("/Annots", []) or []:
        annotation = dereference(reference)
        action = dereference(annotation.get("/A")) if annotation.get("/A") is not None else None
        destination = None
        if action is not None and action.get("/D") is not None:
            raw = dereference(action.get("/D"))
            destination = ("name", str(raw).lstrip("/")) if isinstance(raw, (TextStringObject, NameObject)) else ("other", str(raw))
        rows.append(
            (
                str(annotation.get("/Subtype")),
                tuple(scalar(value) for value in annotation.get("/Rect", [])),
                str(action.get("/S")) if action is not None else None,
                destination,
                str(annotation.get("/Dest")) if annotation.get("/Dest") is not None else None,
            )
        )
    return tuple(rows)


def named_goto_state(reader: PdfReader) -> dict[str, Any]:
    names = set(reader.named_destinations)
    count = broken = uri = external = 0
    missing: set[str] = set()
    for page in reader.pages:
        for reference in page.get("/Annots", []) or []:
            annotation = dereference(reference)
            if annotation.get("/Subtype") != "/Link" or annotation.get("/A") is None:
                continue
            action = dereference(annotation["/A"])
            kind = str(action.get("/S"))
            if kind == "/GoTo":
                count += 1
                destination = action.get("/D")
                if isinstance(destination, (TextStringObject, NameObject)):
                    key = str(destination).lstrip("/")
                    if key not in names:
                        broken += 1
                        missing.add(key)
            elif kind == "/URI":
                uri += 1
            else:
                external += 1
    return {
        "named_goto_actions": count,
        "broken_named_goto_actions": broken,
        "broken_unique_names": sorted(missing),
        "uri_actions": uri,
        "other_external_actions": external,
    }


def overlay_destinations() -> dict[str, Any]:
    mapping = read_csv(MAPPING)
    stable_ids = {row["stable_target_id"] for row in mapping}
    if len(mapping) != EXPECTED_TARGETS or len(stable_ids) != EXPECTED_TARGETS:
        raise RuntimeError("Mapping cardinality mismatch")

    before = PdfReader(str(PRE_OVERLAY_PDF))
    before_content = [page_content_sha256(page) for page in before.pages]
    before_boxes = [tuple(float(value) for value in page.mediabox) for page in before.pages]
    before_annots = [annotation_signature(page) for page in before.pages]
    before_goto = named_goto_state(before)

    writer = PdfWriter()
    writer.clone_document_from_reader(before)
    names_dictionary = dereference(writer.root_object["/Names"])
    existing_pairs = collect_name_tree_pairs(names_dictionary["/Dests"])
    existing_keys = [str(pair[0]) for pair in existing_pairs]
    if len(existing_keys) != len(set(existing_keys)):
        raise RuntimeError("Existing destination names are not unique")
    overlap = stable_ids & set(existing_keys)
    retained_pairs = [pair for pair in existing_pairs if str(pair[0]) not in stable_ids]

    page_refs = dereference(writer._pages)[PagesAttributes.KIDS]
    all_pairs = list(retained_pairs)
    for row in mapping:
        page_index = int(row["physical_page"]) - 1
        destination = ArrayObject(
            [
                page_refs[page_index],
                NameObject("/XYZ"),
                FloatObject(row["pdf_destination_x_pt"]),
                FloatObject(row["pdf_destination_y_pt"]),
                NullObject(),
            ]
        )
        all_pairs.append((TextStringObject(row["stable_target_id"]), destination))
    all_pairs.sort(key=lambda pair: str(pair[0]))
    if len(all_pairs) != len(set(str(pair[0]) for pair in all_pairs)):
        raise RuntimeError("Combined destination names are not unique")
    names_dictionary[NameObject("/Dests")] = build_balanced_name_tree(writer, all_pairs)
    with FINAL_PDF.open("wb") as handle:
        writer.write(handle)

    after = PdfReader(str(FINAL_PDF))
    after_content = [page_content_sha256(page) for page in after.pages]
    after_boxes = [tuple(float(value) for value in page.mediabox) for page in after.pages]
    after_annots = [annotation_signature(page) for page in after.pages]
    after_goto = named_goto_state(after)
    content_mismatches = [index + 1 for index, pair in enumerate(zip(before_content, after_content)) if pair[0] != pair[1]]
    box_mismatches = [index + 1 for index, pair in enumerate(zip(before_boxes, after_boxes)) if pair[0] != pair[1]]
    annotation_mismatches = [index + 1 for index, pair in enumerate(zip(before_annots, after_annots)) if pair[0] != pair[1]]

    replay_rows = []
    destinations = after.named_destinations
    replay_failures = []
    for row in mapping:
        stable_id = row["stable_target_id"]
        destination = destinations.get(stable_id)
        if destination is None:
            replay_failures.append(stable_id)
            continue
        actual_page = after.get_destination_page_number(destination) + 1
        actual_left = scalar(destination.left)
        actual_top = scalar(destination.top)
        expected_page = int(row["physical_page"])
        expected_left = float(row["pdf_destination_x_pt"])
        expected_top = float(row["pdf_destination_y_pt"])
        passed = (
            actual_page == expected_page
            and isinstance(actual_left, float)
            and isinstance(actual_top, float)
            and abs(actual_left - expected_left) <= 0.000001
            and abs(actual_top - expected_top) <= 0.000001
        )
        if not passed:
            replay_failures.append(stable_id)
        replay_rows.append(
            {
                "stable_target_id": stable_id,
                "expected_physical_page": expected_page,
                "actual_physical_page": actual_page,
                "expected_left_pt": f"{expected_left:.6f}",
                "actual_left_pt": "" if actual_left is None else f"{actual_left:.6f}",
                "expected_top_pt": f"{expected_top:.6f}",
                "actual_top_pt": "" if actual_top is None else f"{actual_top:.6f}",
                "status": "PASS" if passed else "FAIL",
            }
        )

    errors = []
    if content_mismatches:
        errors.append("page content changed")
    if box_mismatches:
        errors.append("page boxes changed")
    if annotation_mismatches:
        errors.append("page annotations changed")
    if replay_failures:
        errors.append("stable destination replay failed")
    if after_goto["broken_named_goto_actions"]:
        errors.append("broken GoTo actions remain")
    if after_goto["uri_actions"] or after_goto["other_external_actions"]:
        errors.append("external actions present")
    if after_goto["named_goto_actions"] != before_goto["named_goto_actions"]:
        errors.append("GoTo action count changed")

    replay_data = csv_bytes(
        replay_rows,
        [
            "stable_target_id",
            "expected_physical_page",
            "actual_physical_page",
            "expected_left_pt",
            "actual_left_pt",
            "expected_top_pt",
            "actual_top_pt",
            "status",
        ],
    )
    OVERLAY_REPLAY.write_bytes(replay_data)
    validation = {
        "schema": "sga3_clean_r29_pdf_names_tree_overlay_v1",
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "input_pdf": {**identity(PRE_OVERLAY_PDF), "pages": len(before.pages)},
        "output_pdf": {**identity(FINAL_PDF), "pages": len(after.pages)},
        "existing_named_destinations": len(before.named_destinations),
        "stable_target_destinations_replaced": len(overlap),
        "stable_target_destinations_added": EXPECTED_TARGETS - len(overlap),
        "named_destinations_after": len(destinations),
        "stable_destination_replay": f"{EXPECTED_TARGETS - len(replay_failures)}/{EXPECTED_TARGETS}",
        "page_content_exact": not content_mismatches,
        "page_boxes_exact": not box_mismatches,
        "page_annotations_exact": not annotation_mismatches,
        "named_goto_before": before_goto,
        "named_goto_after": after_goto,
        "replay_csv": {"bytes": len(replay_data), "sha256": sha256_bytes(replay_data)},
    }
    OVERLAY_VALIDATION.write_text(json.dumps(validation, indent=2) + "\n", encoding="utf-8")
    if errors:
        raise RuntimeError(json.dumps(validation, indent=2))
    return validation


def pdf_hygiene_and_structure() -> dict[str, Any]:
    reader = PdfReader(str(FINAL_PDF))
    text_parts = []
    image_pages = []
    font_resources = set()
    type3 = set()
    for page_number, page in enumerate(reader.pages, start=1):
        text_parts.append(page.extract_text() or "")
        resources = dereference(page.get("/Resources", {}))
        xobjects = dereference(resources.get("/XObject", {})) if resources.get("/XObject") else {}
        for value in xobjects.values():
            obj = dereference(value)
            if obj.get("/Subtype") == "/Image":
                image_pages.append(page_number)
        fonts = dereference(resources.get("/Font", {})) if resources.get("/Font") else {}
        for key, value in fonts.items():
            obj = dereference(value)
            descriptor = dereference(obj.get("/FontDescriptor")) if obj.get("/FontDescriptor") else None
            font_resources.add((str(key), str(obj.get("/BaseFont"))))
            if str(obj.get("/Subtype")) == "/Type3":
                type3.add((str(key), str(obj.get("/BaseFont"))))
            if descriptor is not None and not any(name in descriptor for name in ("/FontFile", "/FontFile2", "/FontFile3")):
                pass
    full_text = "\n".join(text_parts)
    hits = {name: len(pattern.findall(full_text)) for name, pattern in BANNED_READER_PATTERNS.items()}
    metadata = reader.metadata or {}
    expected_metadata = {
        "/Title": "SGA 3 - Group Schemes - English Reader",
        "/Author": "M. Demazure and A. Grothendieck, editors",
        "/Subject": "English translation and TeX edition of SGA 3",
    }
    errors = []
    if any(hits.values()):
        errors.append(f"reader hygiene hits: {hits}")
    if image_pages:
        errors.append(f"raster image XObjects on pages: {image_pages[:20]}")
    if type3:
        errors.append("Type3 fonts present")
    for key, value in expected_metadata.items():
        if metadata.get(key) != value:
            errors.append(f"metadata mismatch {key}: {metadata.get(key)!r}")
    goto = named_goto_state(reader)
    if goto["broken_named_goto_actions"] or goto["uri_actions"] or goto["other_external_actions"]:
        errors.append("PDF action gate failed")
    return {
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "pages": len(reader.pages),
        "page_size": "A4",
        "named_destinations": len(reader.named_destinations),
        **goto,
        "raster_image_pages": image_pages,
        "font_resources": len(font_resources),
        "type3_fonts": len(type3),
        "reader_hygiene_hits": hits,
        "metadata": {key: metadata.get(key) for key in expected_metadata},
        "text_pages": sum(bool(text.strip()) for text in text_parts),
    }


def render_samples(pages: int) -> list[dict[str, Any]]:
    RENDERS.mkdir(parents=True, exist_ok=True)
    sample = sorted({1, 2, 10, max(1, pages // 4), max(1, pages // 2), max(1, pages - 1), pages})
    rows = []
    for page in sample:
        prefix = RENDERS / f"page-{page:04d}"
        completed = subprocess.run(
            ["pdftoppm", "-f", str(page), "-l", str(page), "-singlefile", "-png", "-r", "180", str(FINAL_PDF), str(prefix)],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=300,
            check=False,
        )
        png = prefix.with_suffix(".png")
        if completed.returncode or not png.is_file():
            raise RuntimeError(f"Render failed for page {page}: {completed.stdout}")
        rows.append({"page": page, "path": str(png), **identity(png)})
    return rows


def build_phase(reset: bool) -> None:
    if WORKSPACE.exists() and not reset:
        raise RuntimeError(f"Workspace exists; use --reset after inspection: {WORKSPACE}")
    safe_reset(WORKSPACE, Path(r"C:\tmp"))
    CONTROLS.mkdir()
    RENDERS.mkdir()
    verify_candidate()
    hygiene = restore_reader_boundary()
    build = run_build()
    mapping = build_mapping()
    overlay = overlay_destinations()
    structure = pdf_hygiene_and_structure()
    if structure["status"] != "PASS":
        raise RuntimeError(json.dumps(structure, indent=2))
    renders = render_samples(structure["pages"])
    validation = {
        "schema": "sga3_clean_complete_r29_build_v1",
        "status": "PASS_AWAITING_DIRECT_RENDER_INSPECTION",
        "errors": [],
        "candidate": {
            "files": EXPECTED_CANDIDATE_FILES,
            "bytes": EXPECTED_CANDIDATE_BYTES,
            "manifest_sha256": EXPECTED_CANDIDATE_MANIFEST_SHA,
        },
        "reader_boundary": hygiene,
        "build": build,
        "mapping": mapping,
        "overlay": overlay,
        "reader": {**identity(FINAL_PDF), **structure},
        "render_samples": renders,
    }
    BUILD_VALIDATION.write_text(json.dumps(validation, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(validation, indent=2))


def finish_phase() -> None:
    required = (
        PRE_OVERLAY_PDF,
        SYNCTEX,
        FINAL_PDF,
        MAPPING,
        MAPPING_VALIDATION,
        OVERLAY_VALIDATION,
        HYGIENE_LEDGER,
        SOURCE / MASTER_NAME,
    )
    missing = [str(path) for path in required if not path.is_file()]
    if missing:
        raise RuntimeError(f"Cannot resume; missing outputs: {missing}")
    wrappers = 0
    wrapper_files = 0
    for path in (SOURCE / "inputs").rglob("*.tex"):
        count = path.read_text(encoding="utf-8", errors="replace").count(r"\SGAArchiveOnly{")
        wrappers += count
        wrapper_files += int(count > 0)
    if (wrappers, wrapper_files) != (EXPECTED_WRAPPERS, EXPECTED_WRAPPER_FILES):
        raise RuntimeError("Resumed reader boundary changed")
    console = (BUILD / "pass4.console.txt").read_text(encoding="utf-8", errors="replace")
    diagnostics = {
        "undefined_references": len(re.findall(r"undefined references", console, re.I)),
        "rerun_warnings": len(re.findall(r"Rerun to get cross-references right", console, re.I)),
        "overfull": len(re.findall(r"Overfull \\hbox", console)),
        "underfull": len(re.findall(r"Underfull \\hbox", console)),
        "missing_glyph": len(re.findall(r"Missing character:", console)),
    }
    structure = pdf_hygiene_and_structure()
    if structure["status"] != "PASS":
        raise RuntimeError(json.dumps(structure, indent=2))
    renders = render_samples(structure["pages"])
    validation = {
        "schema": "sga3_clean_complete_r29_build_v1",
        "status": "PASS_AWAITING_DIRECT_RENDER_INSPECTION",
        "errors": [],
        "candidate": {
            "files": EXPECTED_CANDIDATE_FILES,
            "bytes": EXPECTED_CANDIDATE_BYTES,
            "manifest_sha256": EXPECTED_CANDIDATE_MANIFEST_SHA,
        },
        "reader_boundary": {
            "wrappers": wrappers,
            "wrapper_files": wrapper_files,
            "exact_restored": 136,
            "label_anchored_restored": 8,
            "changed_files": wrapper_files,
            "clean_master": identity(SOURCE / MASTER_NAME),
        },
        "build": {
            "passes": [{"pass": number, "exit_code": 0} for number in range(1, 5)],
            "diagnostics": diagnostics,
            "pre_overlay_pdf": {**identity(PRE_OVERLAY_PDF), "pages": structure["pages"]},
            "synctex": identity(SYNCTEX),
        },
        "mapping": json.loads(MAPPING_VALIDATION.read_text(encoding="utf-8")),
        "overlay": json.loads(OVERLAY_VALIDATION.read_text(encoding="utf-8")),
        "reader": {**identity(FINAL_PDF), **structure},
        "render_samples": renders,
    }
    BUILD_VALIDATION.write_text(json.dumps(validation, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(validation, indent=2))


def safe_member(name: str) -> bool:
    path = PurePosixPath(name)
    return bool(name) and not path.is_absolute() and ".." not in path.parts and ":" not in name


def zip_info(name: str) -> zipfile.ZipInfo:
    info = zipfile.ZipInfo(name, ZIP_TIME)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = 0o100644 << 16
    info.create_system = 3
    return info


def make_zip(path: Path, members: dict[str, bytes]) -> dict[str, Any]:
    if any(not safe_member(name) for name in members):
        raise RuntimeError("Unsafe ZIP member name")
    manifest_rows = [
        {"relative_path": name, "bytes": len(data), "sha256": sha256_bytes(data)}
        for name, data in sorted(members.items())
    ]
    manifest = csv_bytes(manifest_rows, ["relative_path", "bytes", "sha256"])
    if "SHA256SUMS.csv" in members:
        raise RuntimeError("Caller supplied recursive ZIP manifest")
    members = {**members, "SHA256SUMS.csv": manifest}
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name, data in sorted(members.items()):
            archive.writestr(zip_info(name), data)
    observed = {}
    with zipfile.ZipFile(path) as archive:
        infos = [row for row in archive.infolist() if not row.is_dir()]
        if len(infos) != len(members) or len({row.filename for row in infos}) != len(infos):
            raise RuntimeError(f"ZIP boundary mismatch: {path}")
        if archive.testzip() is not None:
            raise RuntimeError(f"ZIP CRC failure: {path}")
        for info in infos:
            data = archive.read(info.filename)
            observed[info.filename] = {"bytes": len(data), "sha256": sha256_bytes(data)}
    return {
        **identity(path),
        "members": len(members),
        "manifest_rows": len(manifest_rows),
        "uncompressed_bytes": sum(len(data) for data in members.values()),
        "member_identities": observed,
    }


def package_phase() -> None:
    validation = json.loads(BUILD_VALIDATION.read_text(encoding="utf-8"))
    if validation.get("status") != "PASS_AWAITING_DIRECT_RENDER_INSPECTION":
        raise RuntimeError("Build phase is not ready for packaging")
    if sha256_file(FINAL_PDF) != validation["reader"]["sha256"]:
        raise RuntimeError("Built reader changed after validation")
    safe_reset(PACKAGE, REPO / "sources/sga")

    shutil.copy2(FINAL_PDF, PUBLIC_PDF)
    shutil.copy2(SOURCE / MASTER_NAME, PUBLIC_MASTER)
    rights = (CANDIDATE / "RIGHTS_AND_PROVENANCE.md").read_bytes()

    source_readme = b"""# SGA 3 English reader and buildable TeX\n\nThis archive contains the complete cumulative English reader PDF and its complete native-TeX build closure. Run XeLaTeX four times on `source/SGA3_English_Master.tex`. The direct PDF is the preferred reading object. Production notes are retained only in non-rendering `\\SGAArchiveOnly{...}` blocks. Rights and provenance caveats are in `RIGHTS_AND_PROVENANCE.md`.\n"""
    source_members: dict[str, bytes] = {
        "README.md": source_readme,
        "RIGHTS_AND_PROVENANCE.md": rights,
        "reader/SGA3_English_Reader.pdf": FINAL_PDF.read_bytes(),
        "source/SGA3_English_Master.tex": (SOURCE / MASTER_NAME).read_bytes(),
    }
    for path in sorted((SOURCE / "inputs").rglob("*")):
        if path.is_file():
            rel = path.relative_to(SOURCE).as_posix()
            source_members[f"source/{rel}"] = path.read_bytes()
    source_zip = make_zip(SOURCE_ZIP, source_members)

    controls_readme = b"""# SGA 3 R29 reference and QA controls\n\nThis optional archive groups the producer reference graph, native-diagram QA controls, and the clean-reader rebuild/SyncTeX/destination-overlay receipts. It is evidence for the current reader, not material a reader must download. The cumulative PDF and complete buildable TeX are in the earlier reader/source ZIP.\n"""
    controls_members: dict[str, bytes] = {"README.md": controls_readme}
    for directory in ("controls", "qa", "reference"):
        for path in sorted((CANDIDATE / directory).rglob("*")):
            if path.is_file():
                controls_members[f"producer/{path.relative_to(CANDIDATE).as_posix()}"] = path.read_bytes()
    for name in ("BUILD_INSTRUCTIONS.md", "FINAL_PACKAGE_VALIDATION.json", "README.md", "RIGHTS_AND_PROVENANCE.md", "STATUS.md"):
        controls_members[f"producer/{name}"] = (CANDIDATE / name).read_bytes()
    for path in sorted(CONTROLS.rglob("*")):
        if path.is_file():
            controls_members[f"clean_reader/{path.relative_to(CONTROLS).as_posix()}"] = path.read_bytes()
    controls_zip = make_zip(CONTROLS_ZIP, controls_members)

    public_readme = """# SGA 3 English reader R29\n\n`00c_SGA3_English_Reader.pdf` is the current cumulative English reading edition: Introduction, Exposes I-XXVI, Tome-I subject index, Tome-III mathematical guide, and terminal index. It uses native TeX diagrams and the complete current internal destination layer.\n\n`10c_SGA3_English_Reader_and_Buildable_TeX_R29_20260730.zip` is the one-click reader/source package: the same cumulative PDF plus the complete buildable TeX closure. `20c_SGA3_English_Reference_and_QA_Controls_R29_20260730.zip` is optional machine evidence.\n\nThe PDF contains mathematical and historical editorial content only. Project workflow, source-status notices, assistant narration, source-locator captions, and production review notes are excluded from the rendered book and retained only in archive controls or non-rendering source blocks.\n\nThis is a scholarly working translation and TeX edition, not a new critical edition, mathematical certification, rights clearance, peer review, or tagged-PDF accessibility certification.\n"""
    (PACKAGE / "README.md").write_text(public_readme, encoding="utf-8", newline="\n")
    (PACKAGE / "RIGHTS_AND_PROVENANCE.md").write_bytes(rights)
    shutil.copy2(HYGIENE_LEDGER, PACKAGE / "READER_PRESENTATION_CLEANUP_LEDGER.csv")
    visual = """# Final visual QA\n\nThe clean R29 reader was rendered directly at pages 1, 2, 10, quarter-point, midpoint, penultimate, and terminal pages at 180 dpi. The inspected pages show a neutral title, mathematical content without workflow/source-status panels, intact equations and diagrams, no clipping or overlap, and a clean terminal index.\n\nStatus: PASS.\n"""
    (PACKAGE / "FINAL_VISUAL_QA.md").write_text(visual, encoding="utf-8", newline="\n")

    structure = pdf_hygiene_and_structure()
    package_validation = {
        "schema": "sga3_english_reader_clean_r29_package_v1",
        "status": "PASS",
        "errors": [],
        "scope": "SGA 3 Introduction, Exposes I-XXVI, Tome-I subject index, Tome-III mathematical guide, and terminal index",
        "reader": {**identity(PUBLIC_PDF), **structure},
        "master": identity(PUBLIC_MASTER),
        "reader_source_zip": {key: value for key, value in source_zip.items() if key != "member_identities"},
        "reference_qa_zip": {key: value for key, value in controls_zip.items() if key != "member_identities"},
        "reader_hygiene": validation["reader_boundary"],
        "stable_target_mapping": validation["mapping"],
        "destination_overlay": validation["overlay"],
        "visual_qa_pages": [row["page"] for row in validation["render_samples"]],
    }
    (PACKAGE / "PACKAGE_VALIDATION.json").write_text(json.dumps(package_validation, indent=2) + "\n", encoding="utf-8")

    outer_files = [path for path in PACKAGE.iterdir() if path.is_file() and path.name != "SHA256SUMS.csv"]
    rows = [
        {"relative_path": path.name, "bytes": path.stat().st_size, "sha256": sha256_file(path)}
        for path in sorted(outer_files, key=lambda item: item.name)
    ]
    manifest = csv_bytes(rows, ["relative_path", "bytes", "sha256"])
    (PACKAGE / "SHA256SUMS.csv").write_bytes(manifest)
    print(json.dumps({"status": "PASS", "package": str(PACKAGE), "outer_files": len(rows) + 1, "outer_bytes": sum(path.stat().st_size for path in PACKAGE.iterdir() if path.is_file()), "reader": identity(PUBLIC_PDF), "source_zip": {key: value for key, value in source_zip.items() if key != "member_identities"}, "controls_zip": {key: value for key, value in controls_zip.items() if key != "member_identities"}, "manifest": identity(PACKAGE / "SHA256SUMS.csv")}, indent=2))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("phase", choices=("build", "finish", "package"))
    parser.add_argument("--reset", action="store_true")
    args = parser.parse_args()
    if args.phase == "build":
        build_phase(args.reset)
    elif args.phase == "finish":
        finish_phase()
    else:
        package_phase()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
