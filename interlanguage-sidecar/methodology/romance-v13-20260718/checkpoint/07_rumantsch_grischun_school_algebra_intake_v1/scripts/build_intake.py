from __future__ import annotations

import hashlib
import html
from html.parser import HTMLParser
import json
import logging
from pathlib import Path
import re
import shutil
import subprocess

from pypdf import PdfReader

logging.getLogger("pypdf").setLevel(logging.ERROR)


INTAKE = Path(__file__).resolve().parent.parent
RAW = INTAKE / "raw"
EXTRACTED = INTAKE / "extracted"
MANIFESTS = INTAKE / "manifests"

RAW_EXPECTED = {
    "matematica_landing.html": "1DE796600DE3E6896E1B662053F950C7EDC4B2BF134AAC6A3B927DD18275451B",
    "MA_1_A_4_terms_equations.html": "26D4A1DE9F897B0139319EC665391126C4CBC8B54054EEA6BACF50F29EA63AFB",
    "MA_1_A_4_terms_equations_printout.pdf": "47402DF6127CA3F18725704DAED58DE5412BAD7D1639CD67FE4D59B0524EEED0",
    "Matematica_full_subject_printout.pdf": "809FA86CEA7AE27DC2DAD0EAF7467F776CBD6303EB54B436E3E087971881FE05",
}
PDF_TEXT_EXPECTED = {
    "MA_1_A_4_terms_equations_printout.txt": "588919211E43F9E5BB0834306B9B25DC146D13057F7EEEB4A0062805C49A6D67",
    "Matematica_full_subject_printout.txt": "8412A95D48113CF58C0BBC145D21D66543AB4C554BB6F0699F34229B67E66513",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


class VisibleText(HTMLParser):
    BREAKS = {"p", "li", "div", "h1", "h2", "h3", "h4", "br", "tr", "td"}

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.hidden = 0
        self.parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in {"script", "style", "noscript"}:
            self.hidden += 1
        if not self.hidden and tag in self.BREAKS:
            self.parts.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "noscript"} and self.hidden:
            self.hidden -= 1
        if not self.hidden and tag in self.BREAKS:
            self.parts.append("\n")

    def handle_data(self, data: str) -> None:
        if not self.hidden:
            self.parts.append(data)

    def text(self) -> str:
        value = html.unescape("".join(self.parts)).replace("\xa0", " ")
        lines = [re.sub(r"\s+", " ", line).strip() for line in value.splitlines()]
        return "\n".join(line for line in lines if line) + "\n"


def extract_html(source: Path, target: Path) -> None:
    parser = VisibleText()
    parser.feed(source.read_text(encoding="utf-8"))
    target.write_text(parser.text(), encoding="utf-8")


def extract_pdf(source: Path, target: Path) -> None:
    executable = shutil.which("pdftotext")
    if not executable:
        fallback = Path.home() / "AppData/Local/Programs/MiKTeX/miktex/bin/x64/pdftotext.exe"
        if fallback.is_file():
            executable = str(fallback)
    if not executable:
        raise SystemExit("pdftotext executable not found")
    subprocess.run([executable, "-layout", str(source), str(target)], check=True)


def pdf_record(path: Path) -> dict[str, object]:
    reader = PdfReader(path)
    metadata = reader.metadata or {}
    return {
        "pages": len(reader.pages),
        "title": metadata.get("/Title"),
        "subject": metadata.get("/Subject"),
        "author": metadata.get("/Author"),
        "creator": metadata.get("/Creator"),
        "producer": metadata.get("/Producer"),
        "creation_date": str(metadata.get("/CreationDate") or ""),
    }


def main() -> None:
    for name, expected in RAW_EXPECTED.items():
        path = RAW / name
        if not path.is_file() or sha256(path) != expected:
            raise SystemExit(f"raw source mismatch: {name}")

    EXTRACTED.mkdir(parents=True, exist_ok=True)
    MANIFESTS.mkdir(parents=True, exist_ok=True)
    extract_html(RAW / "matematica_landing.html", EXTRACTED / "matematica_landing.txt")
    extract_html(RAW / "MA_1_A_4_terms_equations.html", EXTRACTED / "MA_1_A_4_terms_equations_html.txt")
    extract_pdf(
        RAW / "MA_1_A_4_terms_equations_printout.pdf",
        EXTRACTED / "MA_1_A_4_terms_equations_printout.txt",
    )
    extract_pdf(
        RAW / "Matematica_full_subject_printout.pdf",
        EXTRACTED / "Matematica_full_subject_printout.txt",
    )
    for name, expected in PDF_TEXT_EXPECTED.items():
        if sha256(EXTRACTED / name) != expected:
            raise SystemExit(f"PDF text extraction mismatch: {name}")

    primary_id = "CURATED-RM-RG-PI21-MATEMATICA-FULL"
    records = [
        {
            "source_id": "CURATED-RM-RG-PI21-MATEMATICA-LANDING",
            "title": "Plan d'instrucziun 21 — Matematica landing page",
            "url": "https://gr-r.lehrplan.ch/index.php?code=b%7C5%7C0&la=yes",
            "local_path": "raw/matematica_landing.html",
            "sha256": RAW_EXPECTED["matematica_landing.html"],
            "bytes": (RAW / "matematica_landing.html").stat().st_size,
            "media_type": "text/html",
            "variety_code": "rm-rg",
            "domain": ["mathematics_curriculum_routing"],
            "representation_status": "routing_context_only",
            "alias_of": None,
            "counting_eligible": False,
            "active_body": False,
        },
        {
            "source_id": "CURATED-RM-RG-PI21-MA1A4-HTML",
            "title": "MA.1.A.4 — terms, equations, laws, and rules",
            "url": "https://gr-r.lehrplan.ch/index.php?code=a%7C5%7C0%7C1%7C1%7C4",
            "local_path": "raw/MA_1_A_4_terms_equations.html",
            "sha256": RAW_EXPECTED["MA_1_A_4_terms_equations.html"],
            "bytes": (RAW / "MA_1_A_4_terms_equations.html").stat().st_size,
            "media_type": "text/html",
            "variety_code": "rm-rg",
            "domain": ["school_algebra", "mathematics_curriculum", "mathematical_terminology"],
            "representation_status": "active_noncounting_html_representation",
            "alias_of": primary_id,
            "counting_eligible": False,
            "active_body": True,
        },
        {
            "source_id": "CURATED-RM-RG-PI21-MA1A4-PDF",
            "title": "MA.1.A.4 printable competency",
            "url": "https://gr-r.lehrplan.ch/lehrplan_printout.php?k=1&fb_id=5&f_id=0&kb_id=1&ha_id=1&k_id=4",
            "local_path": "raw/MA_1_A_4_terms_equations_printout.pdf",
            "sha256": RAW_EXPECTED["MA_1_A_4_terms_equations_printout.pdf"],
            "bytes": (RAW / "MA_1_A_4_terms_equations_printout.pdf").stat().st_size,
            "media_type": "application/pdf",
            "pages": 2,
            "variety_code": "rm-rg",
            "domain": ["school_algebra", "mathematics_curriculum", "mathematical_terminology"],
            "representation_status": "active_noncounting_excerpt_representation",
            "alias_of": primary_id,
            "counting_eligible": False,
            "active_body": True,
        },
        {
            "source_id": primary_id,
            "title": "Plan d'instrucziun 21 — Matematica, full subject",
            "url": "https://gr-r.lehrplan.ch/lehrplan_printout.php?k=1&fb_id=5",
            "local_path": "raw/Matematica_full_subject_printout.pdf",
            "sha256": RAW_EXPECTED["Matematica_full_subject_printout.pdf"],
            "bytes": (RAW / "Matematica_full_subject_printout.pdf").stat().st_size,
            "media_type": "application/pdf",
            "pages": 30,
            "variety_code": "rm-rg",
            "domain": [
                "school_algebra",
                "arithmetic",
                "geometry",
                "functions",
                "statistics",
                "probability",
                "mathematics_curriculum",
                "mathematical_terminology",
            ],
            "representation_status": "primary_counting_body",
            "alias_of": None,
            "counting_eligible": True,
            "active_body": True,
        },
    ]
    manifest = {
        "artifact": "ROMANSH_CURRICULUM_INTAKE_MANIFEST_v1",
        "retrieved_date": "2026-07-18",
        "publisher": "Plan d'instrucziun 21 / official Graubünden Rumantsch school curriculum site",
        "authority_domain": "gr-r.lehrplan.ch",
        "language": "Romansh",
        "variety_code": "rm-rg",
        "rights_status": "public_official_access_reuse_and_redistribution_terms_not_cleared",
        "redistribution_status": "internal_evidence_only_pending_rights_review",
        "server_pdf_replay_boundary": "Printout PDFs embed request-time metadata; future downloads are not expected to be byte-identical. Preserved local bytes are authoritative.",
        "records": records,
        "record_count": len(records),
        "primary_counting_body_count": sum(row["counting_eligible"] for row in records),
        "active_representation_count": sum(row["active_body"] for row in records),
        "pdf_page_count_physical": sum(int(row.get("pages", 0)) for row in records),
        "deduplicated_body_page_count": 30,
        "pdf_metadata": {
            "MA_1_A_4": pdf_record(RAW / "MA_1_A_4_terms_equations_printout.pdf"),
            "full_subject": pdf_record(RAW / "Matematica_full_subject_printout.pdf"),
        },
        "extracted_hashes": {
            path.name: sha256(path) for path in sorted(EXTRACTED.glob("*.txt"))
        },
        "classification": {
            "school_mathematics_body_present": True,
            "specialist_school_algebra_body_present": True,
            "abstract_algebra_ring_field_module_research_body_present": False,
            "non_rm_rg_idiom_proxy_authorized": False,
            "corpus_integration_status": "accepted_intake_pending_successor_corpus_build",
        },
    }
    (MANIFESTS / "intake_manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    (MANIFESTS / "coverage_delta.json").write_text(
        json.dumps(
            {
                "artifact": "ROMANSH_CURRICULUM_COVERAGE_DELTA_v1",
                "variety_code": "rm-rg",
                "new_deduplicated_counting_bodies": 1,
                "new_deduplicated_pages": 30,
                "school_algebra_body_delta": 1,
                "abstract_algebra_body_delta": 0,
                "other_romansh_idiom_body_delta": 0,
                "route_effect": "rm-rg school-algebra evidence can become active after successor corpus integration; abstract-algebra and idiom gaps remain explicit",
                "human_observations": 0,
                "rights_status": manifest["rights_status"],
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    print("PASS build_intake records=4 primary=1 active=3 pages=30_deduplicated school_algebra=1 abstract_algebra=0")


if __name__ == "__main__":
    main()
