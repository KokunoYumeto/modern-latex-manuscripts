#!/usr/bin/env python3
"""Render bounded cumulative-reader QA pages serially and build contact sheets."""

from __future__ import annotations

import hashlib
import json
import math
import re
import shutil
import subprocess
from datetime import datetime
from pathlib import Path

from PIL import Image, ImageDraw
from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]
PDF_DIR = ROOT / "release" / "pdf"
VISUAL = ROOT / "release" / "visual"
RIGHTS_BLOCKED = ROOT / "release" / "rights_blocked" / "source_visual"
EVIDENCE = ROOT / "release" / "evidence"
BUILD_MANIFEST = EVIDENCE / "build_manifest.json"
TARGETS = ("ru", "uk", "isv", "isv-cy")
DPI = 144
SOURCE_DPI = 200
POST45_SOURCE_PDF = Path(
    r"C:\Users\Floris\Downloads\codex backup dump 7-4\$germanOut\sources\endmatter\source_blocks\noether_pages_751_798.pdf"
)
POST45_BERTINI_SOURCE_PAGE = 46


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def file_record(path: Path) -> dict:
    return {"path": path.resolve().as_posix(), "bytes": path.stat().st_size, "sha256": sha256(path)}


def pdf_pages_text(path: Path) -> list[str]:
    completed = subprocess.run(
        ["pdftotext", "-layout", str(path.resolve()), "-"],
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if completed.returncode:
        raise RuntimeError(f"pdftotext failed for {path}: {completed.stderr}")
    return completed.stdout.split("\f")


def book_page_units(path: Path, pages: int) -> list[str]:
    texts = pdf_pages_text(path)
    current = "BOOK_TITLE_INTRO"
    units = []
    import re

    for page_index in range(pages):
        text = texts[page_index] if page_index < len(texts) else ""
        matches = [int(value) for value in re.findall(r"§\s*([1-9]|[12][0-9]|3[01])\b", text)]
        if matches:
            current = f"BOOK_S{max(matches):02d}"
        units.append(current)
    return units


def render_page(pdf: Path, page: int, output: Path, dpi: int = DPI) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    prefix = output.with_suffix("")
    completed = subprocess.run(
        [
            "pdftoppm",
            "-f",
            str(page),
            "-l",
            str(page),
            "-r",
            str(dpi),
            "-png",
            "-singlefile",
            str(pdf.resolve()),
            str(prefix.resolve()),
        ],
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if completed.returncode:
        raise RuntimeError(f"pdftoppm failed for {pdf} page {page}: {completed.stderr}")
    if not output.exists():
        raise FileNotFoundError(output)


def find_p06_formula_page(pdf: Path, pages: int) -> int:
    """Locate the accepted ED0005 P06 Psi formula without loading a full reader at once."""
    for start in range(1, pages + 1, 50):
        end = min(start + 49, pages)
        completed = subprocess.run(
            ["pdftotext", "-f", str(start), "-l", str(end), "-layout", str(pdf.resolve()), "-"],
            text=True,
            encoding="utf-8",
            errors="replace",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        if completed.returncode:
            raise RuntimeError(f"pdftotext failed for {pdf} pages {start}-{end}: {completed.stderr}")
        for offset, page_text in enumerate(completed.stdout.split("\f")):
            compact = re.sub(r"\s+", "", page_text)
            if "Ψ(z" in compact and "x1" in compact and "u1" in compact and "x2" in compact:
                return start + offset
    raise RuntimeError(f"could not locate accepted P06 Psi formula in {pdf}")


def contact_sheet(target: str, renders: list[dict]) -> Path:
    thumb_width = 260
    label_height = 34
    columns = 4
    thumbs = []
    for item in renders:
        path = Path(item["image"]["path"])
        with Image.open(path) as original:
            ratio = thumb_width / original.width
            resized = original.convert("RGB").resize(
                (thumb_width, max(1, round(original.height * ratio))), Image.Resampling.LANCZOS
            )
        thumbs.append((item, resized))
    thumb_height = max(image.height for _item, image in thumbs)
    rows = math.ceil(len(thumbs) / columns)
    sheet = Image.new("RGB", (columns * thumb_width, rows * (thumb_height + label_height)), "white")
    draw = ImageDraw.Draw(sheet)
    for index, (item, thumb) in enumerate(thumbs):
        column = index % columns
        row = index // columns
        x = column * thumb_width
        y = row * (thumb_height + label_height)
        sheet.paste(thumb, (x, y))
        label = f"p.{item['page']}  {','.join(item['roles'])}  {item['linked_work_unit']}"
        draw.text((x + 4, y + thumb_height + 4), label[:44], fill="black")
    output = VISUAL / f"contact-{target}.png"
    sheet.save(output, format="PNG", dpi=(DPI, DPI), optimize=True)
    return output


def main() -> int:
    if not BUILD_MANIFEST.exists():
        raise FileNotFoundError(BUILD_MANIFEST)
    VISUAL.mkdir(parents=True, exist_ok=True)
    manifest = json.loads(BUILD_MANIFEST.read_text(encoding="utf-8"))
    cumulative = {record["target"]: record for record in manifest["cumulative_records"]}
    render_records = []
    contact_records = []
    source_records = []
    for target in TARGETS:
        record = cumulative[target]
        inputs = record["inputs"]
        base_pages = inputs[0]["pages"]
        book_pages = inputs[1]["pages"]
        post45_pages = inputs[2]["pages"]
        postbib_pages = inputs[3]["pages"]
        total_pages = record["pdf"]["pages"]
        book_path = PDF_DIR / f"44-book-{target}.pdf"
        book_units = book_page_units(book_path, book_pages)
        base_pdf = PDF_DIR / f"base-papers1-43-{target}.pdf"
        p06_page = find_p06_formula_page(base_pdf, base_pages)
        candidates = [
            (1, "reader_first", "PAPERS_1_43_BASE"),
            (p06_page, "p06_ed0005_formula_correction", "P06"),
            (base_pages, "numbered_paper_base_last", "PAPERS_1_43_BASE"),
            (base_pages + 1, "book_first", book_units[0]),
            (base_pages + math.ceil(book_pages / 2), "book_middle", book_units[math.ceil(book_pages / 2) - 1]),
            (base_pages + book_pages, "book_last", book_units[-1]),
            (base_pages + book_pages + 1, "post45_first", "POST45"),
            (base_pages + book_pages + post45_pages + 1, "postbib_first", "POSTBIB"),
            (total_pages, "reader_last", "POSTBIB"),
        ]
        pages: dict[int, dict] = {}
        for page, role, unit in candidates:
            entry = pages.setdefault(page, {"roles": [], "units": []})
            entry["roles"].append(role)
            entry["units"].append(unit)
        target_records = []
        pdf = PDF_DIR / f"noether-{target}-v038.pdf"
        for page in sorted(pages):
            output = VISUAL / "renders" / target / f"page-{page:04d}.png"
            render_page(pdf, page, output)
            with Image.open(output) as image:
                width, height = image.size
            item = {
                "target": target,
                "page": page,
                "roles": sorted(set(pages[page]["roles"])),
                "linked_work_unit": sorted(set(pages[page]["units"]))[0]
                if len(set(pages[page]["units"])) == 1
                else "|".join(sorted(set(pages[page]["units"]))),
                "parent_pdf": {**file_record(pdf), "pages": total_pages},
                "page_coordinates_points": [0, 0, None, None],
                "render": {"dpi": DPI, "rotation_degrees": 0, "width_px": width, "height_px": height},
                "image": file_record(output),
                "qa_state": "rendered_pending_visual_review",
                "rights_basis": "project-generated QA render; underlying-text redistribution status not independently reassessed",
                "publication_disposition": "include_in_owner_handoff_for_rights_and_publication_decision",
            }
            target_records.append(item)
            render_records.append(item)
        contact = contact_sheet(target, target_records)
        with Image.open(contact) as image:
            width, height = image.size
        contact_records.append(
            {
                "target": target,
                "child_images": [item["image"]["sha256"] for item in target_records],
                "render": {"dpi": DPI, "rotation_degrees": 0, "width_px": width, "height_px": height},
                "image": file_record(contact),
                "qa_state": "generated_pending_visual_review",
                "rights_basis": "project-generated contact sheet; underlying-text redistribution status not independently reassessed",
                "publication_disposition": "include_in_owner_handoff_for_rights_and_publication_decision",
            }
        )

    if not POST45_SOURCE_PDF.exists():
        raise FileNotFoundError(POST45_SOURCE_PDF)
    source_pages = len(PdfReader(str(POST45_SOURCE_PDF)).pages)
    if source_pages < POST45_BERTINI_SOURCE_PAGE:
        raise RuntimeError(
            f"source scan has {source_pages} pages; expected page {POST45_BERTINI_SOURCE_PAGE}"
        )
    source_output = RIGHTS_BLOCKED / "post45-bertini-source-page-0046.png"
    render_page(
        POST45_SOURCE_PDF,
        POST45_BERTINI_SOURCE_PAGE,
        source_output,
        dpi=SOURCE_DPI,
    )
    with Image.open(source_output) as source_image:
        source_width, source_height = source_image.size
    source_records.append(
        {
            "target": "de-source",
            "page": POST45_BERTINI_SOURCE_PAGE,
            "roles": ["source_backed_german_authority_discrepancy_locator"],
            "linked_work_unit": "POST45",
            "parent_pdf": {**file_record(POST45_SOURCE_PDF), "pages": source_pages},
            "page_coordinates_points": [0, 0, None, None],
            "render": {
                "dpi": SOURCE_DPI,
                "rotation_degrees": 0,
                "width_px": source_width,
                "height_px": source_height,
            },
            "image": file_record(source_output),
            "source_locator": (
                "PDF page 46; printed page 46; Bertini example visually reads "
                "phi=x^3+y^4, psi=x^2-y^5"
            ),
            "qa_state": "rendered_pending_visual_review",
            "rights_basis": (
                "local source scan used as research evidence; redistribution rights unresolved"
            ),
            "publication_disposition": (
                "rights_blocked_preserve_file_handoff_public_safe_metadata_only"
            ),
        }
    )

    output_document = {
        "schema": "noether-slavic-v038-visual-render-manifest/1.0",
        "generated_at": datetime.now().astimezone().isoformat(),
        "scope": (
            "bounded renders of final four cumulative readers at input boundaries, the accepted P06 "
            "formula locus, representative Work 44 pages, and one rights-blocked source-scan page "
            "supporting the Post45 German-authority discrepancy"
        ),
        "render_records": render_records,
        "contact_records": contact_records,
        "source_records": source_records,
        "review_state": "pending human/model visual reopening",
    }
    output = EVIDENCE / "visual_render_manifest.json"
    output.write_text(json.dumps(output_document, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "renders": len(render_records),
                "contacts": len(contact_records),
                "source_renders": len(source_records),
                "manifest": {**file_record(output)},
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
