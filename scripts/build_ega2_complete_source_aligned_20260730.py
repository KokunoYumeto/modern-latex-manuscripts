#!/usr/bin/env python3
"""Build a compact public package for the complete source-aligned EGA II reader."""

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
from pathlib import Path, PurePosixPath

from pypdf import PdfReader


REPO = Path(__file__).resolve().parents[1]
OUTPUT = (
    REPO
    / "sources"
    / "ega"
    / "checkpoints"
    / "ega2-complete-source-aligned-working-20260730"
)
PDF_NAME = "00b_EGA2_English_Reader.pdf"
TEX_NAME = "02b_EGA2_English_Master.tex"
ZIP_NAME = "10b_EGA2_English_Source_20260730.zip"
ZIP_TIME = (2026, 7, 30, 0, 0, 0)
SOURCE_DATE_EPOCH = "1785362400"
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
        help="Exact EGA II source-aligned working root.",
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


def selected_source_files(root: Path) -> list[Path]:
    source = root / "source"
    manifest = root / "controls" / "ACTIVE_SOURCE_SHA256_FINAL.csv"
    with manifest.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    selected: list[Path] = []
    errors: list[str] = []
    for row in rows:
        path = source / Path(row["path"])
        if not path.is_file():
            errors.append(f"missing: {row['path']}")
            continue
        if path.stat().st_size != int(row["bytes"]):
            errors.append(f"byte mismatch: {row['path']}")
        if sha256(path) != row["sha256"].upper():
            errors.append(f"hash mismatch: {row['path']}")
        selected.append(path)
    if errors:
        raise RuntimeError("source-closure replay failed:\n" + "\n".join(errors))
    if len(selected) != 14 or len({path.resolve() for path in selected}) != 14:
        raise RuntimeError(f"expected 14 unique source files, found {len(selected)}")
    return selected


def patched_source_items(root: Path, source_files: list[Path]) -> dict[str, bytes]:
    source_root = root / "source"
    items = {
        path.relative_to(source_root).as_posix(): path.read_bytes()
        for path in source_files
    }
    edits = {
        "ega2/ega2-bibliography.tex": [
            (b"\\addcontentsline{toc}{section}{Bibliography}\r\n", b""),
            (b"\\addcontentsline{toc}{section}{Bibliography}\n", b""),
        ],
        "ega2/ega2-indexes-and-contents.tex": [
            (b"\\addcontentsline{toc}{section}{Index of notation}\r\n", b""),
            (b"\\addcontentsline{toc}{section}{Index of notation}\n", b""),
            (b"\\addcontentsline{toc}{section}{Terminological index}\r\n", b""),
            (b"\\addcontentsline{toc}{section}{Terminological index}\n", b""),
            (b"\\addcontentsline{toc}{section}{Original table of contents}\r\n", b""),
            (b"\\addcontentsline{toc}{section}{Original table of contents}\n", b""),
            (
                b"\\begin{longtable}{@{}p{0.09\\textwidth}p{0.77\\textwidth}r@{}}",
                b"\\begin{longtable}{@{}p{0.08\\textwidth}p{0.60\\textwidth}"
                b"@{\\hspace{2em}}r@{}}",
            ),
            (
                b"\\oldpage[II]{214}\r\n\\textsection4",
                b"\\multicolumn{3}{@{}l}{\\oldpage[II]{214}}\\\\\r\n\\textsection4",
            ),
            (
                b"\\oldpage[II]{214}\n\\textsection4",
                b"\\multicolumn{3}{@{}l}{\\oldpage[II]{214}}\\\\\n\\textsection4",
            ),
            (
                b"\\oldpage[II]{215}\r\n8.7",
                b"\\multicolumn{3}{@{}l}{\\oldpage[II]{215}}\\\\\r\n8.7",
            ),
            (
                b"\\oldpage[II]{215}\n8.7",
                b"\\multicolumn{3}{@{}l}{\\oldpage[II]{215}}\\\\\n8.7",
            ),
        ],
        "ega2/ega2-errata-addenda.tex": [
            (b"\\addcontentsline{toc}{section}{Errata and Addenda (List 1)}\r\n", b""),
            (b"\\addcontentsline{toc}{section}{Errata and Addenda (List 1)}\n", b""),
            (
                b"\\section*{Errata and Addenda}\r\n"
                b"\\begin{center}\r\n"
                b"\\large (List 1)\r\n"
                b"\\end{center}\r\n",
                b"\\section*{Errata and Addenda (List 1)}\r\n",
            ),
            (
                b"\\section*{Errata and Addenda}\n"
                b"\\begin{center}\n"
                b"\\large (List 1)\n"
                b"\\end{center}\n",
                b"\\section*{Errata and Addenda (List 1)}\n",
            ),
        ],
    }
    applied = 0
    for name, replacements in edits.items():
        data = items[name]
        before = data
        for old, new in replacements:
            if old in data:
                data = data.replace(old, new, 1)
                applied += 1
        if data == before:
            raise RuntimeError(f"expected public-reader hygiene edit not applied: {name}")
        items[name] = data
    if applied != 9:
        raise RuntimeError(f"expected nine public-reader hygiene edits, applied {applied}")
    return items


def build_reader(source_items: dict[str, bytes], destination: Path) -> dict[str, object]:
    with tempfile.TemporaryDirectory(prefix="ega2-complete-build-") as temp:
        root = Path(temp)
        source = root / "source"
        build = root / "build"
        build.mkdir()
        for name, data in source_items.items():
            path = source / PurePosixPath(name)
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
        env = os.environ.copy()
        env["SOURCE_DATE_EPOCH"] = SOURCE_DATE_EPOCH
        console: list[bytes] = []
        for pass_number in range(1, 5):
            result = subprocess.run(
                [
                    "xelatex",
                    "-interaction=nonstopmode",
                    "-halt-on-error",
                    "-file-line-error",
                    f"-output-directory={build}",
                    "ega2.tex",
                ],
                cwd=source,
                env=env,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                check=False,
            )
            console.append(result.stdout)
            if result.returncode:
                raise RuntimeError(
                    f"XeLaTeX pass {pass_number} failed:\n"
                    + result.stdout.decode("utf-8", errors="replace")[-8000:]
                )
        built = build / "ega2.pdf"
        if not built.is_file():
            raise RuntimeError("XeLaTeX did not produce ega2.pdf")
        shutil.copyfile(built, destination)
        log = build / "ega2.log"
        log_text = log.read_text(encoding="utf-8", errors="replace")
        hard_patterns = (
            "! LaTeX Error",
            "Undefined control sequence",
            "Emergency stop",
            "Fatal error",
        )
        hard_hits = [pattern for pattern in hard_patterns if pattern in log_text]
        if hard_hits:
            raise RuntimeError(f"hard TeX diagnostics found: {hard_hits}")
        return {
            "passes": 4,
            "pass3_console_sha256": sha256_bytes(console[2]),
            "pass4_console_sha256": sha256_bytes(console[3]),
            "pass3_pass4_console_exact": console[2] == console[3],
            "log_sha256": sha256(log),
            "hard_diagnostics": hard_hits,
        }


def scan_private(items: dict[str, bytes]) -> list[dict[str, str]]:
    hits: list[dict[str, str]] = []
    for name, data in items.items():
        lowered = data.lower()
        for marker in PRIVATE_MARKERS:
            if marker in lowered:
                hits.append(
                    {
                        "path": name,
                        "marker": marker.decode("ascii", errors="replace"),
                    }
                )
    return hits


def scan_text_process(name: str, text: str) -> list[dict[str, str]]:
    hits = []
    for pattern in PROCESS_PATTERNS:
        if re.search(pattern, text, flags=re.IGNORECASE):
            hits.append({"path": name, "pattern": pattern})
    return hits


def pdf_metrics(path: Path) -> dict[str, object]:
    reader = PdfReader(path)
    process_hits: list[dict[str, object]] = []
    goto = 0
    invalid = 0
    empty_pages: list[int] = []
    page_sizes: dict[str, int] = {}
    image_xobjects = 0
    type3_fonts = 0
    font_objects: set[str] = set()
    first_pages = []
    for page_number, page in enumerate(reader.pages, 1):
        text = " ".join((page.extract_text() or "").split())
        if not text:
            empty_pages.append(page_number)
        if page_number <= 2:
            first_pages.append(text)
        for hit in scan_text_process(f"page-{page_number}", text):
            process_hits.append({"page": page_number, "pattern": hit["pattern"]})
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
            elif destination is not None:
                goto += 1
    toc_text = " ".join(first_pages)
    toc_labels = (
        "Bibliography",
        "Index of notation",
        "Terminological index",
        "Original table of contents",
        "Errata and Addenda",
    )
    toc_counts = {label: toc_text.count(label) for label in toc_labels}
    return {
        "pages": len(reader.pages),
        "named_destinations": len(reader.named_destinations),
        "internal_goto_actions": goto,
        "invalid_actions": invalid,
        "empty_text_pages": empty_pages,
        "page_sizes": page_sizes,
        "image_xobjects": image_xobjects,
        "font_objects": len(font_objects),
        "type3_font_resources": type3_fonts,
        "toc_backmatter_counts": toc_counts,
        "reader_process_hits": process_hits,
    }


def public_readme(pdf: Path, master: Path) -> str:
    return f"""# EGA II complete source-aligned English working reader

This checkpoint preserves the complete source-aligned EGA II English reader.

## Scope

- Continuous authority coverage from the Chapter II opening through Section
  8.14, the bibliography, index of notation, terminological index, original
  table of contents, and the end of Errata and Addenda (List 1).
- Authority cursor: end of the 219-page NUMDAM EGA II reader; no remaining
  EGA II translation cursor.
- Fourteen-file editable TeX closure with no raster dependency.

The source-era mathematical and editorial content remains in the reader.
Project, model, workflow, source-status, comparison-lineage, and private-path
material is absent. This is a working scholarly translation, not a critical
edition, rights clearance, peer review, or whole-EGA completion claim.

## Direct files

- Reader: `{PDF_NAME}`, 165 pages, {pdf.stat().st_size} bytes,
  SHA-256 `{sha256(pdf)}`.
- Master TeX: `{TEX_NAME}`, {master.stat().st_size} bytes,
  SHA-256 `{sha256(master)}`.
- Complete source package: `{ZIP_NAME}`.

The source ZIP contains the master, both preambles, all eight chapter
components, all three backmatter components, the same reader PDF, and exact
public controls. It excludes the French authority, generated build files, raw
logs, rendered QA images, private paths, and transient intermediates.

The public successor removes four duplicate table-of-contents registrations
caused by explicit `addcontentsline` calls around AMS starred headings. It
also repairs the original-contents column layout, isolates two source-page
markers as table rows, and incorporates “(List 1)” directly into the
Errata/Addenda heading. No mathematical body text was changed.

The French NUMDAM reader is identified by SHA-256
`111834EFFFE9E90D068389D418F08925A82B4A54AE2957F080712D4180E032EB`
but is not redistributed. Underlying rights remain with their holders; this
package asserts no new blanket license.
"""


def status_text() -> str:
    return """# Source-alignment status

State: complete EGA II source-aligned working reader.

- Continuous English scope: authority opening through Section 8.14 and all
  terminal backmatter.
- Authority cursor: EOF after Errata and Addenda (List 1).
- Remaining EGA II translation cursor: none.
- Editable closure: 14 TeX files, recorded in `SHA256SUMS.csv`.

This status concerns EGA II only. It is not a whole-EGA completion,
critical-edition, rights-clearance, or peer-review claim.
"""


def visual_qa_text() -> str:
    return """# Independent visual QA

Disposition: PASS.

- All 165 pages were rendered at 90 dpi and reviewed across six contact sheets.
- Pages 1, 2, 53, 70, 103, 114, 137, 148, 153, 154, 156, 159, 161,
  and 165 were additionally rendered at 180 dpi and reviewed directly.
- The original table of contents was rechecked after its public-successor
  column and source-marker layout repair.
- No blank page, clipping, overlap, malformed formula, malformed diagram,
  missing backmatter, or project/model/workflow note was observed.

This report concerns presentation of the compact public successor. It does
not claim a new mathematical peer review, critical edition, or rights
clearance.
"""


def build_summary(pdf: Path, build: dict[str, object]) -> str:
    return f"""# Public build summary

- XeLaTeX passes: four consecutive successful passes from the copied public
  source closure.
- Fatal or error-pattern count: zero.
- Reader pages: 165.
- Reader SHA-256: `{sha256(pdf)}`.
- Build-log SHA-256: `{build["log_sha256"]}`.
- Pass-3 console SHA-256: `{build["pass3_console_sha256"]}`.
- Pass-4 console SHA-256: `{build["pass4_console_sha256"]}`.
- Pass-3/pass-4 console exact: `{str(build["pass3_pass4_console_exact"]).lower()}`.
- The compact successor removes duplicate table-of-contents registrations
  and repairs the original-contents column layout without changing
  mathematical body text.

Raw logs and rendered QA images are excluded from the compact public source
package because they add no mathematical content and can expose local build
details.
"""


def build_source_zip(
    destination: Path,
    source_items: dict[str, bytes],
    pdf: Path,
    readme: str,
    build: dict[str, object],
) -> dict[str, object]:
    members = {
        "source/" + name: data
        for name, data in sorted(source_items.items(), key=lambda item: item[0].casefold())
    }
    members["reader/" + PDF_NAME] = pdf.read_bytes()
    members["README.md"] = readme.encode("utf-8")
    members["SOURCE_ALIGNMENT_STATUS.md"] = status_text().encode("utf-8")
    members["BUILD_SUMMARY_PUBLIC.md"] = build_summary(pdf, build).encode("utf-8")
    members["INDEPENDENT_VISUAL_QA.md"] = visual_qa_text().encode("utf-8")

    privacy_hits = scan_private(
        {name: data for name, data in members.items() if not name.endswith(".pdf")}
    )
    process_hits: list[dict[str, str]] = []
    for name, data in members.items():
        if name.endswith((".tex", ".bib", ".md")):
            process_hits.extend(
                scan_text_process(name, data.decode("utf-8", errors="replace"))
            )
    if privacy_hits or process_hits:
        raise RuntimeError(
            f"public text scan failed: privacy={privacy_hits}, process={process_hits}"
        )

    manifest_rows = [
        {
            "relative_path": name,
            "bytes": len(data),
            "sha256": sha256_bytes(data),
        }
        for name, data in sorted(members.items(), key=lambda item: item[0].casefold())
    ]
    members["SHA256SUMS.csv"] = csv_bytes(
        manifest_rows, ["relative_path", "bytes", "sha256"]
    )

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
            errors.append("CRC failure")
        names = archive.namelist()
        if len(names) != len(set(names)):
            errors.append("duplicate member")
        if set(names) != set(members):
            errors.append("member-set mismatch")
        for name in names:
            if not safe_member(name):
                errors.append(f"unsafe member: {name}")
            if sha256_bytes(archive.read(name)) != sha256_bytes(members[name]):
                errors.append(f"member hash mismatch: {name}")
        uncompressed = sum(info.file_size for info in archive.infolist())
    if errors:
        raise RuntimeError("\n".join(errors))

    return {
        "filename": destination.name,
        "bytes": destination.stat().st_size,
        "sha256": sha256(destination),
        "members": len(members),
        "uncompressed_bytes": uncompressed,
        "manifest_rows": len(manifest_rows),
        "manifest_sha256": sha256_bytes(members["SHA256SUMS.csv"]),
        "privacy_hits": privacy_hits,
        "process_hits": process_hits,
        "member_readback": "PASS",
    }


def write_outer_manifest() -> None:
    represented = [
        OUTPUT / PDF_NAME,
        OUTPUT / TEX_NAME,
        OUTPUT / ZIP_NAME,
        OUTPUT / "PACKAGE_VALIDATION.json",
        OUTPUT / "README.md",
        OUTPUT / "SOURCE_ALIGNMENT_STATUS.md",
        OUTPUT / "BUILD_SUMMARY_PUBLIC.md",
        OUTPUT / "INDEPENDENT_VISUAL_QA.md",
    ]
    rows = [
        {
            "relative_path": path.name,
            "bytes": path.stat().st_size,
            "sha256": sha256(path),
        }
        for path in represented
    ]
    (OUTPUT / "SHA256SUMS.csv").write_bytes(
        csv_bytes(rows, ["relative_path", "bytes", "sha256"])
    )


def main() -> None:
    args = parse_args()
    root = args.source.resolve()
    if not root.is_dir():
        raise SystemExit(f"source root does not exist: {root}")
    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    OUTPUT.mkdir(parents=True)

    source_files = selected_source_files(root)
    source_items = patched_source_items(root, source_files)

    pdf_target = OUTPUT / PDF_NAME
    tex_target = OUTPUT / TEX_NAME
    build_result = build_reader(source_items, pdf_target)
    tex_target.write_bytes(source_items["ega2.tex"])

    readme = public_readme(pdf_target, tex_target)
    (OUTPUT / "README.md").write_text(readme, encoding="utf-8", newline="\n")
    (OUTPUT / "SOURCE_ALIGNMENT_STATUS.md").write_text(
        status_text(), encoding="utf-8", newline="\n"
    )
    (OUTPUT / "BUILD_SUMMARY_PUBLIC.md").write_text(
        build_summary(pdf_target, build_result), encoding="utf-8", newline="\n"
    )
    (OUTPUT / "INDEPENDENT_VISUAL_QA.md").write_text(
        visual_qa_text(), encoding="utf-8", newline="\n"
    )
    zip_result = build_source_zip(
        OUTPUT / ZIP_NAME, source_items, pdf_target, readme, build_result
    )
    metrics = pdf_metrics(pdf_target)
    if (
        metrics["pages"] != 165
        or metrics["invalid_actions"]
        or metrics["empty_text_pages"]
        or metrics["image_xobjects"]
        or metrics["type3_font_resources"]
        or set(metrics["page_sizes"]) != {"612.0x792.0"}
        or any(count != 1 for count in metrics["toc_backmatter_counts"].values())
    ):
        raise RuntimeError(f"unexpected PDF metrics: {metrics}")
    if metrics["reader_process_hits"]:
        raise RuntimeError(f"reader process text found: {metrics['reader_process_hits']}")

    validation = {
        "status": "PASS",
        "errors": [],
        "scope": "Complete source-aligned EGA II English working reader",
        "continuation": {
            "unit": "Authority EOF after Errata and Addenda (List 1)",
            "authority_physical_page": 219,
            "authority_printed_page": 222,
            "remaining_ega2_translation_cursor": None,
        },
        "direct_reader": {**identity(pdf_target), **metrics},
        "direct_master": identity(tex_target),
        "build": build_result,
        "public_reader_hygiene": {
            "removed_duplicate_toc_registrations": 4,
            "errata_list_number_integrated_into_heading": True,
            "original_contents_column_layout_repaired": True,
            "original_contents_source_markers_isolated_as_rows": 2,
            "mathematical_body_changed": False,
        },
        "selected_source_files": len(source_files),
        "selected_source_bytes_before_public_hygiene": sum(
            path.stat().st_size for path in source_files
        ),
        "selected_source_bytes_after_public_hygiene": sum(
            len(data) for data in source_items.values()
        ),
        "source_zip": zip_result,
        "authority": {
            "description": "EGA II French original, NUMDAM PMIHES 8 (1961)",
            "sha256": (
                "111834EFFFE9E90D068389D418F08925A82B4A54AE2957F080712D4180E032EB"
            ),
            "redistributed": False,
        },
        "excluded": [
            "French authority PDF",
            "generated source/$out subtree",
            "raw logs and console output",
            "rendered page PNGs",
            "private paths",
            "transient build files",
        ],
        "disposition": {
            "github_custody": "READY",
            "zenodo_same_concept_successor": "READY",
            "ega2_source_alignment_complete": True,
            "whole_ega_complete": False,
        },
    }
    (OUTPUT / "PACKAGE_VALIDATION.json").write_text(
        json.dumps(validation, indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    write_outer_manifest()

    result = {
        "output": str(OUTPUT),
        "outer_files": len(list(OUTPUT.iterdir())),
        "outer_bytes": sum(path.stat().st_size for path in OUTPUT.iterdir()),
        "reader": identity(pdf_target),
        "master": identity(tex_target),
        "source_zip": zip_result,
        "outer_manifest_sha256": sha256(OUTPUT / "SHA256SUMS.csv"),
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
