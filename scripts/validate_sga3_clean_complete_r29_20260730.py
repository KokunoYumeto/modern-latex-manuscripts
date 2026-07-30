#!/usr/bin/env python3
"""Independently replay the clean complete SGA3 R29 public package."""

from __future__ import annotations

import csv
import hashlib
import io
import json
import re
import shutil
import subprocess
import zipfile
from pathlib import Path, PurePosixPath

from pypdf import PdfReader


REPO = Path(r"C:\w\e620")
PACKAGE = REPO / "sources/sga/sga3-english-reader-clean-r29-complete-native-reference-v2-20260730"
RECEIPT_DIR = REPO / "sources/sga/sga3-english-reader-clean-r29-independent-replay-20260730"
SOURCE_ZIP = PACKAGE / "10c_SGA3_English_Reader_and_Buildable_TeX_R29_20260730.zip"
CONTROLS_ZIP = PACKAGE / "20c_SGA3_English_Reference_and_QA_Controls_R29_20260730.zip"
DIRECT_PDF = PACKAGE / "00c_SGA3_English_Reader.pdf"
DIRECT_MASTER = PACKAGE / "02c_SGA3_English_Master.tex"
WORK = Path(r"C:\tmp\sga3-r29-independent-replay-20260730")
EXPECTED = {
    "pdf_sha256": "FE7211BA4288E66430E64C574E808E9BAD596E99366777D2DDC2349CB9BD427C",
    "pdf_bytes": 11_859_958,
    "pages": 1_470,
    "master_sha256": "B0106C64F7D3FB63F78A2F18C2684B27E14FDAD0D51B923EBA61F2A1980AF988",
    "source_zip_members": 918,
    "source_zip_manifest_rows": 917,
    "controls_zip_members": 32,
    "controls_zip_manifest_rows": 31,
    "targets": 3_744,
    "destinations": 13_119,
    "goto_actions": 12_337,
}
TEXT_SUFFIXES = {
    ".bib",
    ".cls",
    ".csv",
    ".json",
    ".jsonl",
    ".log",
    ".md",
    ".sty",
    ".tex",
    ".texfrag",
    ".txt",
}
PRIVATE_PATTERNS = {
    "windows_user_path": re.compile(rb"(?i)C:(?:[/\\]|\\\\)+Users(?:[/\\]|\\\\)+Floris"),
    "legacy_repo_path": re.compile(rb"(?i)C:(?:[/\\]|\\\\)+IL_GitHub"),
    "codex_private": re.compile(rb"(?i)(?:[/\\]|\\\\)\.codex(?:[/\\]|\\\\)"),
    "papors_private": re.compile(rb"(?i)(?:[/\\]|\\\\)Papors(?:[/\\]|\\\\)"),
    "chatnotes_private": re.compile(rb"(?i)(?:[/\\]|\\\\)Chatnotes(?:[/\\]|\\\\)"),
    "task_id": re.compile(rb"(?i)019f[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"),
}
READER_BANNED = {
    "assistant_narration": re.compile(r"(?i)\b(?:assistant|chatgpt|codex|claude)\b"),
    "workflow_status": re.compile(r"(?i)\b(?:workflow status|production status|pending review|review status)\b"),
    "source_locator": re.compile(r"(?i)\bsource locator\b"),
    "project_preface": re.compile(r"(?i)\b(?:reconstruction preface|project author|source status)\b"),
}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def sha256_path(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(4 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def safe_member(name: str) -> bool:
    path = PurePosixPath(name)
    return (
        bool(name)
        and name == name.replace("\\", "/")
        and not path.is_absolute()
        and ".." not in path.parts
        and not (len(name) >= 2 and name[1] == ":")
    )


def csv_rows(data: bytes) -> list[dict[str, str]]:
    return list(csv.DictReader(io.StringIO(data.decode("utf-8-sig"))))


def scan_text(name: str, data: bytes, hits: list[dict[str, str]]) -> None:
    if Path(name).suffix.lower() not in TEXT_SUFFIXES:
        return
    for label, pattern in PRIVATE_PATTERNS.items():
        match = pattern.search(data)
        if match:
            hits.append(
                {
                    "path": name,
                    "pattern": label,
                    "match_sha256": sha256_bytes(match.group(0)),
                }
            )


def replay_zip(path: Path, expected_members: int, expected_rows: int) -> dict[str, object]:
    privacy_hits: list[dict[str, str]] = []
    with zipfile.ZipFile(path) as archive:
        infos = [info for info in archive.infolist() if not info.is_dir()]
        names = [info.filename for info in infos]
        if len(infos) != expected_members or len(set(names)) != expected_members:
            raise RuntimeError(f"{path.name}: member boundary changed")
        if not all(safe_member(name) for name in names):
            raise RuntimeError(f"{path.name}: unsafe member path")
        if archive.testzip() is not None:
            raise RuntimeError(f"{path.name}: CRC failure")
        if names.count("SHA256SUMS.csv") != 1:
            raise RuntimeError(f"{path.name}: manifest boundary changed")
        rows = csv_rows(archive.read("SHA256SUMS.csv"))
        if len(rows) != expected_rows:
            raise RuntimeError(f"{path.name}: manifest row count changed")
        by_name = {row["relative_path"]: row for row in rows}
        represented = set(names) - {"SHA256SUMS.csv"}
        if len(by_name) != expected_rows or set(by_name) != represented:
            raise RuntimeError(f"{path.name}: manifest exact-set closure failed")
        for name in sorted(represented):
            data = archive.read(name)
            row = by_name[name]
            if (len(data), sha256_bytes(data)) != (
                int(row["bytes"]),
                row["sha256"].upper(),
            ):
                raise RuntimeError(f"{path.name}: member mismatch: {name}")
            scan_text(f"{path.name}:{name}", data, privacy_hits)
        if privacy_hits:
            raise RuntimeError(f"{path.name}: private text: {privacy_hits[:5]}")
        return {
            "bytes": path.stat().st_size,
            "sha256": sha256_path(path),
            "members": len(infos),
            "manifest_rows": len(rows),
            "uncompressed_bytes": sum(info.file_size for info in infos),
            "privacy_hits": privacy_hits,
        }


def replay_outer() -> dict[str, object]:
    manifest = PACKAGE / "SHA256SUMS.csv"
    rows = csv_rows(manifest.read_bytes())
    files = {
        path.name: path
        for path in PACKAGE.iterdir()
        if path.is_file() and path.name != manifest.name
    }
    by_name = {row["relative_path"]: row for row in rows}
    if len(rows) != 9 or len(by_name) != 9 or set(by_name) != set(files):
        raise RuntimeError("outer manifest exact-set closure failed")
    privacy_hits: list[dict[str, str]] = []
    for name, path in sorted(files.items()):
        data = path.read_bytes()
        row = by_name[name]
        if (len(data), sha256_bytes(data)) != (
            int(row["bytes"]),
            row["sha256"].upper(),
        ):
            raise RuntimeError(f"outer identity mismatch: {name}")
        scan_text(name, data, privacy_hits)
    if privacy_hits:
        raise RuntimeError(f"outer private text: {privacy_hits}")
    return {
        "files": len(files) + 1,
        "manifest_rows": len(rows),
        "manifest_sha256": sha256_path(manifest),
        "privacy_hits": privacy_hits,
    }


def pdf_metrics(path: Path) -> tuple[dict[str, object], list[object]]:
    reader = PdfReader(str(path))
    pages = list(reader.pages)
    destination_names = set(reader.named_destinations)
    goto = 0
    broken = 0
    uri = 0
    external = 0
    image_xobjects = 0
    type3_fonts = 0
    text_parts: list[str] = []
    for page in pages:
        text_parts.append(page.extract_text() or "")
        resources = page.get("/Resources") or {}
        xobjects = resources.get("/XObject") or {}
        for ref in xobjects.values():
            obj = ref.get_object()
            if obj.get("/Subtype") == "/Image":
                image_xobjects += 1
        fonts = resources.get("/Font") or {}
        for ref in fonts.values():
            if ref.get_object().get("/Subtype") == "/Type3":
                type3_fonts += 1
        for ref in page.get("/Annots") or []:
            annotation = ref.get_object()
            if annotation.get("/Subtype") != "/Link":
                continue
            action = annotation.get("/A")
            if action:
                subtype = action.get("/S")
                if subtype == "/GoTo":
                    goto += 1
                    destination = action.get("/D")
                    if isinstance(destination, str) and destination not in destination_names:
                        broken += 1
                elif subtype == "/URI":
                    uri += 1
                else:
                    external += 1
    text = "\n".join(text_parts)
    banned = [label for label, pattern in READER_BANNED.items() if pattern.search(text)]
    metadata = reader.metadata or {}
    return (
        {
            "pages": len(pages),
            "destinations": len(destination_names),
            "goto_actions": goto,
            "broken_actions": broken,
            "uri_actions": uri,
            "external_actions": external,
            "image_xobjects": image_xobjects,
            "type3_fonts": type3_fonts,
            "banned_reader_text_hits": banned,
            "metadata": {
                "title": metadata.get("/Title"),
                "author": metadata.get("/Author"),
                "subject": metadata.get("/Subject"),
            },
        },
        pages,
    )


def page_signature(page: object) -> dict[str, object]:
    content = page.get_contents()
    if isinstance(content, list):
        data = b"".join(item.get_data() for item in content)
    elif content is None:
        data = b""
    else:
        data = content.get_data()
    annotations = []
    for ref in page.get("/Annots") or []:
        obj = ref.get_object()
        annotations.append(
            {
                "subtype": str(obj.get("/Subtype")),
                "rect": [float(value) for value in obj.get("/Rect", [])],
                "action": str(obj.get("/A")),
                "destination": str(obj.get("/Dest")),
            }
        )
    return {
        "content_sha256": sha256_bytes(data),
        "mediabox": [float(value) for value in page.mediabox],
        "cropbox": [float(value) for value in page.cropbox],
        "annotations": annotations,
        "text_sha256": sha256_bytes((page.extract_text() or "").encode("utf-8")),
    }


def extracted_build(final_pages: list[object]) -> dict[str, object]:
    resolved = WORK.resolve()
    expected_root = Path(r"C:\tmp").resolve()
    if expected_root not in resolved.parents or resolved.name != "sga3-r29-independent-replay-20260730":
        raise RuntimeError(f"refusing to reset unexpected path: {resolved}")
    if WORK.exists():
        shutil.rmtree(WORK)
    WORK.mkdir(parents=True)
    with zipfile.ZipFile(SOURCE_ZIP) as archive:
        archive.extractall(WORK)
    source = WORK / "source"
    command = [
        "xelatex",
        "-interaction=nonstopmode",
        "-halt-on-error",
        "-file-line-error",
        "SGA3_English_Master.tex",
    ]
    passes = []
    for number in range(1, 5):
        result = subprocess.run(
            command,
            cwd=source,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=1_800,
        )
        console = result.stdout + result.stderr
        (WORK / f"xelatex-pass{number}.console.txt").write_text(console, encoding="utf-8")
        passes.append(
            {
                "pass": number,
                "exit_code": result.returncode,
                "console_sha256": sha256_bytes(console.encode("utf-8")),
            }
        )
        if result.returncode:
            raise RuntimeError(f"independent XeLaTeX pass {number} failed")
    rebuilt = source / "SGA3_English_Master.pdf"
    rebuilt_metrics, rebuilt_pages = pdf_metrics(rebuilt)
    if len(rebuilt_pages) != len(final_pages):
        raise RuntimeError("independent PDF page count differs")
    mismatches = []
    for number, (expected_page, observed_page) in enumerate(
        zip(final_pages, rebuilt_pages, strict=True), start=1
    ):
        if page_signature(expected_page) != page_signature(observed_page):
            mismatches.append(number)
            if len(mismatches) >= 10:
                break
    if mismatches:
        raise RuntimeError(f"independent page-content mismatch: {mismatches}")
    return {
        "passes": passes,
        "pdf": {
            "bytes": rebuilt.stat().st_size,
            "sha256": sha256_path(rebuilt),
            "pages": rebuilt_metrics["pages"],
            "page_content_text_geometry_annotations_exact": len(final_pages),
        },
    }


def main() -> int:
    outer = replay_outer()
    source_zip = replay_zip(
        SOURCE_ZIP,
        EXPECTED["source_zip_members"],
        EXPECTED["source_zip_manifest_rows"],
    )
    controls_zip = replay_zip(
        CONTROLS_ZIP,
        EXPECTED["controls_zip_members"],
        EXPECTED["controls_zip_manifest_rows"],
    )
    if (DIRECT_PDF.stat().st_size, sha256_path(DIRECT_PDF)) != (
        EXPECTED["pdf_bytes"],
        EXPECTED["pdf_sha256"],
    ):
        raise RuntimeError("direct PDF identity changed")
    if sha256_path(DIRECT_MASTER) != EXPECTED["master_sha256"]:
        raise RuntimeError("direct master identity changed")
    with zipfile.ZipFile(SOURCE_ZIP) as archive:
        if archive.read("reader/SGA3_English_Reader.pdf") != DIRECT_PDF.read_bytes():
            raise RuntimeError("source ZIP reader differs from direct PDF")
        if archive.read("source/SGA3_English_Master.tex") != DIRECT_MASTER.read_bytes():
            raise RuntimeError("source ZIP master differs from direct master")
    metrics, final_pages = pdf_metrics(DIRECT_PDF)
    expected_metrics = {
        "pages": EXPECTED["pages"],
        "destinations": EXPECTED["destinations"],
        "goto_actions": EXPECTED["goto_actions"],
        "broken_actions": 0,
        "uri_actions": 0,
        "external_actions": 0,
        "image_xobjects": 0,
        "type3_fonts": 0,
        "banned_reader_text_hits": [],
    }
    for key, value in expected_metrics.items():
        if metrics[key] != value:
            raise RuntimeError(f"PDF metric mismatch: {key}={metrics[key]!r}, expected {value!r}")
    build = extracted_build(final_pages)
    RECEIPT_DIR.mkdir(parents=True, exist_ok=True)
    receipt = {
        "schema": "sga3_clean_complete_r29_independent_archive_replay_v1",
        "status": "PASS",
        "errors": [],
        "package": str(PACKAGE.relative_to(REPO)).replace("\\", "/"),
        "outer": outer,
        "source_zip": source_zip,
        "controls_zip": controls_zip,
        "reader": {
            "bytes": DIRECT_PDF.stat().st_size,
            "sha256": sha256_path(DIRECT_PDF),
            **metrics,
        },
        "master": {
            "bytes": DIRECT_MASTER.stat().st_size,
            "sha256": sha256_path(DIRECT_MASTER),
        },
        "stable_targets": EXPECTED["targets"],
        "independent_build": build,
        "privacy_hits": [],
    }
    json_path = RECEIPT_DIR / "INDEPENDENT_ARCHIVE_REPLAY.json"
    json_path.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8", newline="\n")
    markdown = f"""# SGA3 R29 independent archive replay\n\nStatus: **PASS**.\n\n- Outer package: {outer['files']} files; manifest {outer['manifest_rows']}/{outer['manifest_rows']} exact.\n- Reader/source ZIP: {source_zip['members']} members; {source_zip['manifest_rows']}/{source_zip['manifest_rows']} exact.\n- Optional controls ZIP: {controls_zip['members']} members; {controls_zip['manifest_rows']}/{controls_zip['manifest_rows']} exact.\n- Reader: {metrics['pages']} A4 pages; SHA-256 `{sha256_path(DIRECT_PDF)}`.\n- PDF links: {metrics['destinations']} named destinations; {metrics['goto_actions']} internal GoTo actions; zero broken or external actions.\n- Fresh extracted build: four XeLaTeX passes; all {metrics['pages']} page content streams, text, geometry, and annotations exactly match the public reader.\n- Privacy scan: zero private-path or task-ID hits.\n- Reader presentation scan: zero AI/workflow/source-status/source-locator hits.\n\nThe replay independently validates custody packaging; it does not create a new rights grant or critical-edition claim.\n"""
    md_path = RECEIPT_DIR / "INDEPENDENT_ARCHIVE_REPLAY.md"
    md_path.write_text(markdown, encoding="utf-8", newline="\n")
    summary = {
        "status": "PASS",
        "json": {"bytes": json_path.stat().st_size, "sha256": sha256_path(json_path)},
        "markdown": {"bytes": md_path.stat().st_size, "sha256": sha256_path(md_path)},
        "reader": receipt["reader"],
        "source_zip": source_zip,
        "controls_zip": controls_zip,
    }
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
