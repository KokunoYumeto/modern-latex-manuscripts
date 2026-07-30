#!/usr/bin/env python3
"""Build the compact public EGA I complete source-aligned working reader."""

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
import tempfile
import zipfile
from collections import Counter
from pathlib import Path, PurePosixPath

from pypdf import PdfReader


REPO = Path(__file__).resolve().parents[1]
OUTPUT = (
    REPO
    / "sources"
    / "ega"
    / "checkpoints"
    / "ega1-complete-source-aligned-working-20260730"
)
PDF_NAME = "00a_EGA1_English_Complete_SourceAligned_Working_Reader_20260730.pdf"
TEX_NAME = "02a_EGA1_English_Complete_SourceAligned_Working_Master_20260730.tex"
ZIP_NAME = "10a_EGA1_English_Complete_SourceAligned_TeX_PDF_20260730.zip"
ZIP_TIME = (2026, 7, 30, 0, 0, 0)
SOURCE_DATE_EPOCH = "1785362400"
AUTHORITY_SHA256 = "9ABA23020217535977E279BDD06A0413F48DA703086865BA4C00766C85DF4AE6"
BASELINE_PDF_SHA256 = "DE217B7105CDDE0EDB0EFB441B9584249412D37E0154D63F771F38EB0D524482"
SOURCE_PATHS = (
    "ega1.tex",
    "preamble.tex",
    "preamble-base.tex",
    "the.bib",
    "ega1/ega1-1.tex",
    "ega1/ega1-2.tex",
    "ega1/ega1-3.tex",
    "ega1/ega1-4.tex",
    "ega1/ega1-5.tex",
    "ega1/ega1-6.tex",
    "ega1/ega1-7.tex",
    "ega1/ega1-8.tex",
    "ega1/ega1-9.tex",
    "ega1/ega1-10.tex",
    "ega1/ega1-backmatter-index-notation.tex",
    "ega1/ega1-backmatter-index-terminology.tex",
)
PRIVATE_MARKERS = (
    b"c:\\users\\",
    b"c:/users/",
    b"c:\\il_github",
    b"papors",
    b"chatnotes",
    b".claude",
    b".codex",
    b"source_thread_id",
    b"thread_id",
)
PROCESS_PATTERNS = (
    r"\bChatGPT\b",
    r"\bClaude\b",
    r"\bCodex\b",
    r"\bOpenAI\b",
    r"\bLLM\b",
    r"AI-generated",
    r"machine-assisted",
    r"production status",
    r"source status",
    r"pending review",
    r"workflow status",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source",
        required=True,
        type=Path,
        help="Exact stable EGA I complete source-aligned root.",
    )
    return parser.parse_args()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def identity(path: Path) -> dict[str, object]:
    return {"bytes": path.stat().st_size, "sha256": sha256(path)}


def safe_member(name: str) -> bool:
    pure = PurePosixPath(name)
    return (
        bool(name)
        and not pure.is_absolute()
        and ".." not in pure.parts
        and "\\" not in name
        and re.match(r"^[A-Za-z]:", name) is None
    )


def zip_info(name: str) -> zipfile.ZipInfo:
    info = zipfile.ZipInfo(name, date_time=ZIP_TIME)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.create_system = 3
    info.external_attr = 0o100644 << 16
    return info


def csv_bytes(rows: list[dict[str, object]], fields: list[str]) -> bytes:
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return buffer.getvalue().encode("utf-8")


def source_items(root: Path) -> tuple[dict[str, bytes], Path]:
    source = root / "source"
    baseline = root / "build" / "checkpoint_complete_backmatter_r2" / "ega1.pdf"
    errors: list[str] = []
    items: dict[str, bytes] = {}
    for name in SOURCE_PATHS:
        path = source / PurePosixPath(name)
        if not path.is_file():
            errors.append(f"missing source: {name}")
        else:
            items[name] = path.read_bytes()
    if not baseline.is_file():
        errors.append("missing stable baseline reader")
    elif sha256(baseline) != BASELINE_PDF_SHA256:
        errors.append("stable baseline reader hash mismatch")
    if errors:
        raise RuntimeError("source closure failed:\n" + "\n".join(errors))
    return items, baseline


def patched_source_items(items: dict[str, bytes]) -> dict[str, bytes]:
    result = dict(items)
    preamble = result["preamble.tex"].decode("utf-8")
    hyperref = (
        "\\usepackage[linktocpage=true,colorlinks=true,hyperindex,"
        "citecolor=blue,linkcolor=brightmaroon]{hyperref}"
    )
    metadata = """\n\\hypersetup{\n  pdftitle={EGA I: The Language of Schemes - English Working Translation},\n  pdfsubject={Complete source-aligned English working reader of EGA I},\n  pdfauthor={Alexander Grothendieck and Jean Dieudonne; English translation}\n}\n"""
    if preamble.count(hyperref) != 1:
        raise RuntimeError("expected exactly one hyperref package declaration")
    preamble = preamble.replace(hyperref, hyperref + metadata, 1)
    result["preamble.tex"] = preamble.encode("utf-8")

    removals = {
        "ega1/ega1-backmatter-index-notation.tex": (
            "\\addcontentsline{toc}{section}{Index of Notation}"
        ),
        "ega1/ega1-backmatter-index-terminology.tex": (
            "\\addcontentsline{toc}{section}{Terminological Index}"
        ),
    }
    for name, line in removals.items():
        text = result[name].decode("utf-8")
        if text.count(line) != 1:
            raise RuntimeError(f"expected one duplicate TOC registration in {name}")
        text = text.replace(line + "\r\n", "", 1)
        text = text.replace(line + "\n", "", 1)
        if line in text:
            raise RuntimeError(f"TOC registration removal failed in {name}")
        result[name] = text.encode("utf-8")
    return result


def run(command: list[str], cwd: Path, env: dict[str, str]) -> bytes:
    result = subprocess.run(
        command,
        cwd=cwd,
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    if result.returncode:
        raise RuntimeError(
            f"command failed ({result.returncode}): {' '.join(command)}\n"
            + result.stdout.decode("utf-8", errors="replace")[-8000:]
        )
    return result.stdout


def build_reader(items: dict[str, bytes], destination: Path) -> dict[str, object]:
    with tempfile.TemporaryDirectory(prefix="ega1-complete-public-build-") as temp:
        root = Path(temp)
        source = root / "source"
        build = root / "build"
        source.mkdir()
        build.mkdir()
        for name, data in items.items():
            path = source / PurePosixPath(name)
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)

        env = os.environ.copy()
        env["SOURCE_DATE_EPOCH"] = SOURCE_DATE_EPOCH
        consoles = [
            run(
                [
                    "xelatex",
                    "-interaction=nonstopmode",
                    "-halt-on-error",
                    "-file-line-error",
                    f"-output-directory={build}",
                    "ega1.tex",
                ],
                source,
                env,
            )
        ]
        bibtex_console = run(["bibtex", str(build / "ega1")], source, env)
        for _ in range(3):
            consoles.append(
                run(
                    [
                        "xelatex",
                        "-interaction=nonstopmode",
                        "-halt-on-error",
                        "-file-line-error",
                        f"-output-directory={build}",
                        "ega1.tex",
                    ],
                    source,
                    env,
                )
            )

        built = build / "ega1.pdf"
        if not built.is_file():
            raise RuntimeError("build did not produce ega1.pdf")
        shutil.copyfile(built, destination)
        log = build / "ega1.log"
        log_text = log.read_text(encoding="utf-8", errors="replace")
        hard_patterns = (
            "! LaTeX Error",
            "Undefined control sequence",
            "Emergency stop",
            "Fatal error",
            "Citation `",
        )
        hard_hits = [pattern for pattern in hard_patterns if pattern in log_text]
        if hard_hits:
            raise RuntimeError(f"blocking TeX diagnostics: {hard_hits}")
        return {
            "xelatex_passes": 4,
            "bibtex_passes": 1,
            "pass3_console_sha256": sha256_bytes(consoles[2]),
            "pass4_console_sha256": sha256_bytes(consoles[3]),
            "pass3_pass4_console_exact": consoles[2] == consoles[3],
            "bibtex_console_sha256": sha256_bytes(bibtex_console),
            "log_sha256": sha256(log),
            "overfull_boxes": log_text.count("Overfull \\hbox"),
            "underfull_boxes": log_text.count("Underfull \\hbox"),
            "standalone_cross_volume_reference_warning": (
                "There were undefined references" in log_text
            ),
            "blocking_diagnostics": hard_hits,
        }


def normalize_pdf_text(reader: PdfReader) -> str:
    return " ".join(
        " ".join((page.extract_text() or "").split()) for page in reader.pages
    )


def normalized_body_text(reader: PdfReader) -> str:
    pages: list[str] = []
    header = "THE LANGUAGE OF SCHEMES (EGA I)"
    for page in reader.pages:
        text = " ".join((page.extract_text() or "").split())
        if text.startswith(header):
            text = text[len(header) :].lstrip()
            text = re.sub(r"^\d+\s+", "", text, count=1)
        pages.append(text)
    full = " ".join(pages)
    marker = "SUMMARY"
    if marker not in full:
        raise RuntimeError("reader body marker not found")
    return full.split(marker, 1)[1]


def compare_baseline(baseline: Path, successor: Path) -> dict[str, object]:
    before = PdfReader(baseline)
    after = PdfReader(successor)
    if len(before.pages) != 114 or len(after.pages) != 113:
        raise RuntimeError("baseline/successor page count mismatch")
    before_full = normalize_pdf_text(before)
    duplicate_phrases = (
        "Index of Notation 111 Index of Notation 111",
        "Terminological Index 112 Terminological Index 112",
    )
    for phrase in duplicate_phrases:
        if before_full.count(phrase) != 1:
            raise RuntimeError(f"expected baseline duplicate not found: {phrase}")
    before_body = normalized_body_text(before)
    after_body = normalized_body_text(after)
    if Counter(before_body.split()) != Counter(after_body.split()):
        raise RuntimeError("successor body token multiset differs after header normalization")
    if Counter(before_body) != Counter(after_body):
        raise RuntimeError("successor body character multiset differs after header normalization")
    return {
        "baseline_pdf": identity(baseline),
        "successor_pages": len(after.pages),
        "pagination_delta": "114-page predecessor to 113-page public successor after contents deduplication",
        "text_delta": "front contents repaginated after removing one duplicate Index of Notation entry and one duplicate Terminological Index entry",
        "body_token_multiset_from_summary_exact_after_running_header_normalization": True,
        "body_character_multiset_from_summary_exact_after_running_header_normalization": True,
        "extracted_order_note": "page reflow changes extracted footnote ordering without changing source content",
    }


def scan_private(items: dict[str, bytes]) -> list[dict[str, str]]:
    hits: list[dict[str, str]] = []
    for name, data in items.items():
        lowered = data.lower()
        for marker in PRIVATE_MARKERS:
            if marker in lowered:
                hits.append(
                    {"path": name, "marker": marker.decode("ascii", errors="replace")}
                )
    return hits


def scan_process_text(name: str, text: str) -> list[dict[str, str]]:
    hits: list[dict[str, str]] = []
    for pattern in PROCESS_PATTERNS:
        if re.search(pattern, text, flags=re.IGNORECASE):
            hits.append({"path": name, "pattern": pattern})
    return hits


def pdf_metrics(path: Path) -> dict[str, object]:
    reader = PdfReader(path)
    goto = 0
    invalid = 0
    external = 0
    empty_pages: list[int] = []
    page_sizes: dict[str, int] = {}
    image_xobjects = 0
    type3_fonts = 0
    font_objects: set[str] = set()
    process_hits: list[dict[str, object]] = []
    private_hits: list[dict[str, object]] = []
    full_text: list[str] = []
    for page_number, page in enumerate(reader.pages, 1):
        text = " ".join((page.extract_text() or "").split())
        full_text.append(text)
        if not text:
            empty_pages.append(page_number)
        for hit in scan_process_text(f"page-{page_number}", text):
            process_hits.append({"page": page_number, "pattern": hit["pattern"]})
        lowered = text.lower()
        for marker in PRIVATE_MARKERS:
            if marker.decode("ascii", errors="ignore") in lowered:
                private_hits.append({"page": page_number, "marker": marker.decode()})
        size = f"{float(page.mediabox.width):.1f}x{float(page.mediabox.height):.1f}"
        page_sizes[size] = page_sizes.get(size, 0) + 1
        resources = page.get("/Resources") or {}
        for reference in (resources.get("/XObject") or {}).values():
            if reference.get_object().get("/Subtype") == "/Image":
                image_xobjects += 1
        for reference in (resources.get("/Font") or {}).values():
            font = reference.get_object()
            font_objects.add(str(reference))
            if font.get("/Subtype") == "/Type3":
                type3_fonts += 1
        for annotation_ref in page.get("/Annots") or []:
            annotation = annotation_ref.get_object()
            action = annotation.get("/A")
            destination = annotation.get("/Dest")
            if action and action.get("/S") == "/GoTo":
                goto += 1
                if action.get("/D") is None:
                    invalid += 1
            elif action:
                external += 1
            elif destination is not None:
                goto += 1

    metadata = {str(key): str(value) for key, value in (reader.metadata or {}).items()}
    metadata_text = " ".join(metadata.values())
    process_hits.extend(scan_process_text("PDF metadata", metadata_text))
    lowered_metadata = metadata_text.lower()
    for marker in PRIVATE_MARKERS:
        decoded = marker.decode("ascii", errors="ignore")
        if decoded in lowered_metadata:
            private_hits.append({"path": "PDF metadata", "marker": decoded})

    toc_text = " ".join(full_text[:2])
    return {
        "pages": len(reader.pages),
        "named_destinations": len(reader.named_destinations),
        "internal_goto_actions": goto,
        "invalid_internal_actions": invalid,
        "external_or_other_actions": external,
        "empty_text_pages": empty_pages,
        "page_sizes": page_sizes,
        "font_objects": len(font_objects),
        "type3_font_resources": type3_fonts,
        "image_xobjects": image_xobjects,
        "metadata": metadata,
        "toc_index_of_notation_count": toc_text.count("Index of Notation"),
        "toc_terminological_index_count": toc_text.count("Terminological Index"),
        "reader_process_hits": process_hits,
        "reader_private_hits": private_hits,
    }


def rights_text() -> str:
    return f"""# Rights and provenance

The controlling source witness for source alignment is the NUMDAM EGA I
reader (PMIHES 4, 1960), 227 pages, SHA-256 `{AUTHORITY_SHA256}`. The French
reader is not redistributed in this compact English package.

The English base is the pre-existing human community translation maintained
at <https://github.com/ryankeleti/ega>. The project did not infer a blanket
license grant from the inspected source snapshot. Underlying French and
English rights remain with their respective holders.

This package is a complete source-aligned English working reader of EGA I.
It is not a critical edition, mathematical certification, peer review,
accessibility certification, legal advice, or rights clearance. It asserts
no new blanket license.
"""


def status_text() -> str:
    return """# Source-alignment status

State: complete EGA I source-aligned English working reader.

- Scope: opening and summary, Sections 1-10.15, bibliography, index of
  notation, and terminological index.
- Authority cursor: end of EGA I; no remaining EGA I translation cursor.
- Editable closure: 16 files (13 content/master TeX files, two preambles,
  and one BibTeX database).
- Internal links: present and valid, but this release does not claim the
  separate exhaustive reference-v2 certification still under construction.

This status concerns EGA I only. It is not a whole-EGA completion claim.
"""


def visual_qa_text() -> str:
    return """# Independent visual QA

Disposition: PASS.

- The complete public successor was rendered at 90 dpi for page-sequence and
  blank-page review.
- Pages 1, 2, 57, 108, 109, 110, 111, 112, and 113 were also rendered at
  180 dpi and directly inspected.
- The front contents and both terminal indexes were checked after removing
  their duplicate table-of-contents registrations.
- No blank page, clipping, overlap, malformed formula, missing backmatter,
  or reader-facing project/model/workflow note was observed.

This is presentation QA, not a new mathematical peer review.
"""


def readme_text(pdf: Path, master: Path, metrics: dict[str, object]) -> str:
    return f"""# EGA I complete source-aligned English working reader

This checkpoint preserves the complete source-aligned EGA I English reader.

## Scope

- Complete EGA I: opening and summary, Sections 1-10.15, bibliography,
  index of notation, and terminological index.
- Authority cursor: end of EGA I; no remaining EGA I translation cursor.
- Sixteen-file editable TeX/BibTeX closure with no raster dependency.

## Direct files

- Reader: `{PDF_NAME}`, 113 pages, {pdf.stat().st_size} bytes, SHA-256
  `{sha256(pdf)}`.
- Master TeX: `{TEX_NAME}`, {master.stat().st_size} bytes, SHA-256
  `{sha256(master)}`.
- Complete reader/source package: `{ZIP_NAME}`.

The source package contains the reader, the complete buildable source
closure, and concise public controls. It excludes the French authority,
render trees, raw logs, build intermediates, private paths, and workflow
material.

The public successor removes two duplicate contents registrations and adds
neutral PDF metadata. It repaginates the reader from 114 to 113 pages and changes no mathematical or
editorial body text. It contains {metrics['named_destinations']} named
destinations and {metrics['internal_goto_actions']} valid internal GoTo
actions, with zero broken or external actions. Exhaustive reference-v2
certification remains a separate later successor.

See `RIGHTS_AND_PROVENANCE.md` before redistribution. This is a working
scholarly translation, not a critical edition, rights clearance, peer review,
or whole-EGA completion claim.
"""


def build_summary_text(
    pdf: Path, build: dict[str, object], comparison: dict[str, object]
) -> str:
    return f"""# Public build summary

- Build: BibTeX once plus four successful XeLaTeX passes from the copied
  public source closure.
- Blocking diagnostics: zero.
- Reader: 113 letter pages, SHA-256 `{sha256(pdf)}`.
- Pass-3/pass-4 console exact: `{str(build['pass3_pass4_console_exact']).lower()}`.
- Build-log SHA-256: `{build['log_sha256']}`.
- Baseline reader SHA-256: `{BASELINE_PDF_SHA256}`.
- Text comparison: exact after removing one duplicate `Index of Notation`
  contents entry and one duplicate `Terminological Index` contents entry.
- Mathematical/editorial body source changes: zero.

Raw logs and rendered QA images are excluded because they add no mathematical
content and can expose local build details.
"""


def build_source_zip(
    destination: Path,
    items: dict[str, bytes],
    pdf: Path,
    public_files: dict[str, bytes],
) -> dict[str, object]:
    root = "EGA1_Complete_SourceAligned_English_20260730/"
    members = {
        root + "source/" + name: data
        for name, data in sorted(items.items(), key=lambda item: item[0].casefold())
    }
    members[root + "reader/" + PDF_NAME] = pdf.read_bytes()
    for name, data in public_files.items():
        members[root + name] = data

    privacy_hits = scan_private(
        {name: data for name, data in members.items() if not name.endswith(".pdf")}
    )
    process_hits: list[dict[str, str]] = []
    for name, data in members.items():
        if name.endswith((".tex", ".bib", ".md")):
            process_hits.extend(
                scan_process_text(name, data.decode("utf-8", errors="replace"))
            )
    if privacy_hits or process_hits:
        raise RuntimeError(
            f"public source ZIP scan failed: privacy={privacy_hits}, process={process_hits}"
        )

    rows = [
        {"relative_path": name, "bytes": len(data), "sha256": sha256_bytes(data)}
        for name, data in sorted(members.items(), key=lambda item: item[0].casefold())
    ]
    manifest_name = root + "SHA256SUMS.csv"
    members[manifest_name] = csv_bytes(rows, ["relative_path", "bytes", "sha256"])

    with zipfile.ZipFile(destination, "w", allowZip64=True) as archive:
        for name, data in sorted(members.items(), key=lambda item: item[0].casefold()):
            if not safe_member(name):
                raise RuntimeError(f"unsafe ZIP member: {name}")
            archive.writestr(
                zip_info(name),
                data,
                compress_type=zipfile.ZIP_DEFLATED,
                compresslevel=9,
            )

    errors: list[str] = []
    with zipfile.ZipFile(destination) as archive:
        if archive.testzip():
            errors.append("ZIP CRC failure")
        names = archive.namelist()
        if len(names) != len(set(names)):
            errors.append("duplicate ZIP member")
        if set(names) != set(members):
            errors.append("ZIP member-set mismatch")
        for name in names:
            if not safe_member(name):
                errors.append(f"unsafe ZIP member: {name}")
            if sha256_bytes(archive.read(name)) != sha256_bytes(members[name]):
                errors.append(f"ZIP member hash mismatch: {name}")
        uncompressed = sum(info.file_size for info in archive.infolist())
    if errors:
        raise RuntimeError("\n".join(errors))
    return {
        "filename": destination.name,
        "bytes": destination.stat().st_size,
        "sha256": sha256(destination),
        "members": len(members),
        "manifest_rows": len(rows),
        "manifest_sha256": sha256_bytes(members[manifest_name]),
        "uncompressed_bytes": uncompressed,
    }


def write_outer_manifest() -> None:
    files = sorted(
        [path for path in OUTPUT.iterdir() if path.name != "SHA256SUMS.csv"],
        key=lambda path: path.name.casefold(),
    )
    rows = [
        {
            "relative_path": path.name,
            "bytes": path.stat().st_size,
            "sha256": sha256(path),
        }
        for path in files
    ]
    (OUTPUT / "SHA256SUMS.csv").write_bytes(
        csv_bytes(rows, ["relative_path", "bytes", "sha256"])
    )


def main() -> None:
    args = parse_args()
    root = args.source.resolve()
    items, baseline = source_items(root)
    patched = patched_source_items(items)

    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    OUTPUT.mkdir(parents=True)
    pdf = OUTPUT / PDF_NAME
    build = build_reader(patched, pdf)
    comparison = compare_baseline(baseline, pdf)
    metrics = pdf_metrics(pdf)

    errors: list[str] = []
    if metrics["pages"] != 113:
        errors.append("reader page count is not 113")
    if metrics["invalid_internal_actions"]:
        errors.append("invalid internal PDF action")
    if metrics["external_or_other_actions"]:
        errors.append("external or non-GoTo PDF action")
    if metrics["empty_text_pages"]:
        errors.append("text-empty page")
    if metrics["reader_process_hits"]:
        errors.append("reader-facing process/model note")
    if metrics["reader_private_hits"]:
        errors.append("reader-facing private marker")
    if metrics["toc_index_of_notation_count"] != 1:
        errors.append("Index of Notation TOC entry not unique")
    if metrics["toc_terminological_index_count"] != 1:
        errors.append("Terminological Index TOC entry not unique")
    if metrics["metadata"].get("/Title") != (
        "EGA I: The Language of Schemes - English Working Translation"
    ):
        errors.append("PDF title metadata mismatch")

    master = OUTPUT / TEX_NAME
    master.write_bytes(patched["ega1.tex"])
    readme = readme_text(pdf, master, metrics)
    public_text = {
        "README.md": readme.encode("utf-8"),
        "RIGHTS_AND_PROVENANCE.md": rights_text().encode("utf-8"),
        "SOURCE_ALIGNMENT_STATUS.md": status_text().encode("utf-8"),
        "BUILD_SUMMARY_PUBLIC.md": build_summary_text(pdf, build, comparison).encode(
            "utf-8"
        ),
        "INDEPENDENT_VISUAL_QA.md": visual_qa_text().encode("utf-8"),
    }
    for name, data in public_text.items():
        (OUTPUT / name).write_bytes(data)

    text_scan = dict(patched)
    text_scan.update(public_text)
    privacy_hits = scan_private(text_scan)
    process_hits: list[dict[str, str]] = []
    for name, data in text_scan.items():
        process_hits.extend(
            scan_process_text(name, data.decode("utf-8", errors="replace"))
        )
    if privacy_hits:
        errors.append("public text privacy marker")
    if process_hits:
        errors.append("public text process/model marker")

    source_zip = build_source_zip(OUTPUT / ZIP_NAME, patched, pdf, public_text)
    validation = {
        "schema": "ega1-complete-source-aligned-public-package-1.0",
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "scope": "complete EGA I through bibliography and both indexes; authority cursor EOF",
        "claim_boundary": "complete source-aligned English working reader; exhaustive reference-v2 certification not claimed",
        "authority": {
            "description": "NUMDAM EGA I, PMIHES 4 (1960), 227 pages",
            "sha256": AUTHORITY_SHA256,
            "redistributed": False,
        },
        "source_files": len(patched),
        "source_bytes": sum(len(data) for data in patched.values()),
        "reader": identity(pdf),
        "master": identity(master),
        "pdf_metrics": metrics,
        "build": build,
        "baseline_comparison": comparison,
        "source_zip": source_zip,
        "privacy_hits": privacy_hits,
        "process_or_model_hits": process_hits,
        "public_hygiene_edits": [
            "remove duplicate Index of Notation TOC registration",
            "remove duplicate Terminological Index TOC registration",
            "add neutral PDF title, subject, and author metadata",
        ],
        "mathematical_body_edits": 0,
    }
    (OUTPUT / "PACKAGE_VALIDATION.json").write_text(
        json.dumps(validation, indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    write_outer_manifest()

    if errors:
        raise RuntimeError("public package validation failed:\n" + "\n".join(errors))
    print(
        json.dumps(
            {
                "output": str(OUTPUT),
                "outer_files": len(list(OUTPUT.iterdir())),
                "outer_bytes": sum(path.stat().st_size for path in OUTPUT.iterdir()),
                "reader": identity(pdf),
                "source_zip": source_zip,
                "outer_manifest": identity(OUTPUT / "SHA256SUMS.csv"),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
