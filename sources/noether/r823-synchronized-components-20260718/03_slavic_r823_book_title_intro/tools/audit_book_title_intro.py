#!/usr/bin/env python3
"""Audit the four R823 BOOK_TITLE_INTRO Slavic deliverables."""

from __future__ import annotations

import csv
import hashlib
import json
import re
import shutil
import subprocess
from datetime import datetime
from pathlib import Path

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]
AUTHORITY_SHA256 = "EE8955BCF7A263917BE57DBC8F682601550CDCB5260D02CA6D486C6A6DFD4F21"
UNIT_SHA256 = "EE0961B423D3DE5325AFF57DDE559CE64817FBE1CB8F1D1A1B290BC9ECA020F6"
LOG_PATTERN = re.compile(
    r"Overfull|Underfull|undefined|LaTeX Error|Package .* Error|^!|Missing character",
    re.IGNORECASE | re.MULTILINE,
)

RECORDS = (
    (
        "ukrainian",
        "Ukrainian",
        "Noether_R823_BOOK_TITLE_INTRO_Ukrainian_v001",
        "Алгебра гіперкомплексних величин",
    ),
    (
        "russian",
        "Russian",
        "Noether_R823_BOOK_TITLE_INTRO_Russian_v001",
        "Алгебра гиперкомплексных величин",
    ),
    (
        "interslavic",
        "Interslavic Latin",
        "Noether_R823_BOOK_TITLE_INTRO_Interslavic_v001",
        "Algebra hiperkompleksnyh veličin",
    ),
    (
        "interslavic-cyrillic",
        "Interslavic Cyrillic",
        "Noether_R823_BOOK_TITLE_INTRO_Interslavic_Cyrillic_v001",
        "Алгебра хиперкомплексных величин",
    ),
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def font_audit(pdf: Path) -> dict[str, object]:
    command = shutil.which("pdffonts")
    if not command:
        return {"available": False, "all_embedded": None, "font_rows": []}
    completed = subprocess.run(
        [command, str(pdf)],
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    rows = []
    for line in completed.stdout.splitlines()[2:]:
        fields = line.split()
        if len(fields) >= 6:
            # pdffonts' type column may contain one or two whitespace-separated
            # fields; the final five columns are stable: emb/sub/uni/object/ID.
            rows.append({"name": fields[0], "embedded": fields[-5], "unicode": fields[-3]})
    return {
        "available": True,
        "all_embedded": bool(rows) and all(row["embedded"] == "yes" for row in rows),
        "font_rows": rows,
    }


def main() -> int:
    authority = ROOT / "authority" / "Noether_R823_cum_de.tex"
    manifest = ROOT / "evidence" / "R823_SOURCE_UNIT_MANIFEST.csv"
    with manifest.open("r", encoding="utf-8-sig", newline="") as handle:
        source_rows = list(csv.DictReader(handle))
    unit = next(row for row in source_rows if row["unit_id"] == "BOOK_TITLE_INTRO")

    authority_check = {
        "path": str(authority),
        "sha256": sha256(authority),
        "expected_sha256": AUTHORITY_SHA256,
    }
    unit_check = {
        "unit_id": unit["unit_id"],
        "start_line": int(unit["start_line"]),
        "end_line": int(unit["end_line"]),
        "chars": int(unit["chars"]),
        "utf8_bytes": int(unit["utf8_bytes"]),
        "source_sha256": unit["source_sha256"],
        "expected_sha256": UNIT_SHA256,
    }

    targets = []
    for directory, label, stem, required_title in RECORDS:
        tex = ROOT / "translations" / directory / f"{stem}.tex"
        pdf = ROOT / "output" / "pdf" / f"{stem}.pdf"
        log = ROOT / "output" / "logs" / f"{stem}.log"
        contact = ROOT / "evidence" / "visual_qa" / f"{stem}_contact_sheet.png"
        tex_text = tex.read_text(encoding="utf-8")
        log_text = log.read_text(encoding="utf-8", errors="replace")
        reader = PdfReader(str(pdf))
        extracted = "\n".join(page.extract_text() or "" for page in reader.pages)
        log_hits = [match.group(0) for match in LOG_PATTERN.finditer(log_text)]
        record = {
            "language": label,
            "tex": {
                "path": str(tex),
                "bytes": tex.stat().st_size,
                "sha256": sha256(tex),
                "toc_section_rows": len(re.findall(r"(?m)^\\tocsec", tex_text)),
                "toc_chapter_rows": len(re.findall(r"(?m)^\\tocline", tex_text)),
                "section_headings": len(re.findall(r"(?m)^\\section\*", tex_text)),
                "required_math_tokens_present": all(
                    token in tex_text
                    for token in ("$Z_1$", "$Z_i$", "$e_i$", "\\mathfrak R_r", "$\\mathfrak{o}$", "$\\mathsf T$")
                ),
            },
            "pdf": {
                "path": str(pdf),
                "bytes": pdf.stat().st_size,
                "sha256": sha256(pdf),
                "pages": len(reader.pages),
                "title_extract_present": required_title in extracted,
                "extracted_characters": len(extracted),
                "fonts": font_audit(pdf),
            },
            "build_log": {
                "path": str(log),
                "bytes": log.stat().st_size,
                "sha256": sha256(log),
                "scan_patterns": LOG_PATTERN.pattern,
                "hits": log_hits,
                "pass": not log_hits,
            },
            "visual_contact_sheet": {
                "path": str(contact),
                "bytes": contact.stat().st_size,
                "sha256": sha256(contact),
            },
        }
        record["pass"] = (
            record["tex"]["toc_section_rows"] == 31
            and record["tex"]["toc_chapter_rows"] == 7
            and record["tex"]["section_headings"] == 2
            and record["tex"]["required_math_tokens_present"]
            and record["pdf"]["pages"] == 3
            and record["pdf"]["title_extract_present"]
            and record["pdf"]["fonts"]["all_embedded"]
            and record["build_log"]["pass"]
        )
        targets.append(record)

    report = {
        "schema": "noether-r823-slavic-book-title-intro-audit-v1",
        "generated_at": datetime.now().astimezone().isoformat(),
        "authority": authority_check,
        "source_unit": unit_check,
        "targets": targets,
        "overall_pass": (
            authority_check["sha256"] == authority_check["expected_sha256"]
            and unit_check["source_sha256"] == unit_check["expected_sha256"]
            and all(target["pass"] for target in targets)
        ),
        "status_limit": "Internal source/build/visual QA only; no external or community certification.",
    }
    output = ROOT / "evidence" / "BUILD_AND_STRUCTURE_AUDIT.json"
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {output}")
    print(f"overall_pass={report['overall_pass']}")
    for target in targets:
        print(
            f"{target['language']}: pass={target['pass']} pages={target['pdf']['pages']} "
            f"log_hits={len(target['build_log']['hits'])}"
        )
    return 0 if report["overall_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
