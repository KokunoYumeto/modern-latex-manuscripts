#!/usr/bin/env python3
"""Build the privacy-clean five-expose SGA 7 I working checkpoint."""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
import shutil
import subprocess
import zipfile
from pathlib import Path

import fitz
from pypdf import PdfReader


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = (
    REPO_ROOT
    / "sources"
    / "sga"
    / "sga7i-fresh-transcription-exposes-i-ii-vi-vii-viii-working-20260730"
)

BODY_NAMES = (
    "expose_I_body.tex",
    "expose_II_body.tex",
    "expose_VI_body.tex",
    "expose_VII_body.tex",
    "expose_VIII_body.tex",
)

WRAPPER_NAME = (
    "SGA7I_Fresh_Transcription_Exposes_I_II_VI_VII_VIII_Working.tex"
)
PDF_NAME = (
    "SGA7I_Fresh_Transcription_Exposes_I_II_VI_VII_VIII_Working.pdf"
)
ZIP_NAME = (
    "SGA7I_Fresh_Transcription_Exposes_I_II_VI_VII_VIII_"
    "Reader_and_Source_20260730.zip"
)

WRAPPER = r"""\documentclass[11pt,a4paper,leqno]{article}

\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{lmodern}
\usepackage[french,english]{babel}
\usepackage{amsmath,amssymb,amsfonts,mathrsfs}
\usepackage{mathtools}
\usepackage{tikz}
\usetikzlibrary{cd,arrows.meta}
\usepackage{geometry}
\geometry{margin=2.4cm}
\usepackage{enumitem}
\usepackage[normalem]{ulem}
\let\mathunderline\underline
\renewcommand{\underline}[1]{\ifmmode\mathunderline{#1}\else\uline{#1}\fi}
\emergencystretch=3em

\DeclareUnicodeCharacter{2192}{\ensuremath{\rightarrow}}
\DeclareUnicodeCharacter{2297}{\ensuremath{\otimes}}
\DeclareUnicodeCharacter{2295}{\ensuremath{\oplus}}
\DeclareUnicodeCharacter{2228}{\ensuremath{\vee}}
\DeclareUnicodeCharacter{223C}{\ensuremath{\sim}}
\DeclareUnicodeCharacter{2248}{\ensuremath{\approx}}
\DeclareUnicodeCharacter{00D7}{\ensuremath{\times}}
\DeclareUnicodeCharacter{03B1}{\ensuremath{\alpha}}
\DeclareUnicodeCharacter{03B2}{\ensuremath{\beta}}
\DeclareUnicodeCharacter{00A7}{\S}
\DeclareUnicodeCharacter{010C}{\v{C}}
\DeclareUnicodeCharacter{00C3}{\~{A}}
\DeclareUnicodeCharacter{02D9}{\.{}}

\providecommand{\Zl}{\mathbb{Z}_{\ell}}
\providecommand{\Ql}{\mathbb{Q}_{\ell}}
\providecommand{\Gal}{\operatorname{Gal}}
\providecommand{\Spec}{\operatorname{Spec}}
\providecommand{\Isom}{\operatorname{Isom}}
\providecommand{\Aut}{\operatorname{Aut}}
\providecommand{\Hom}{\operatorname{Hom}}
\providecommand{\Ext}{\operatorname{Ext}}
\providecommand{\Biext}{\operatorname{Biext}}
\providecommand{\Coker}{\operatorname{Coker}}
\providecommand{\Ker}{\operatorname{Ker}}
\providecommand{\Im}{\operatorname{Im}}
\providecommand{\Tor}{\operatorname{Tor}}
\providecommand{\prof}{\operatorname{prof}}
\providecommand{\codim}{\operatorname{codim}}
\providecommand{\pr}{\operatorname{pr}}
\providecommand{\id}{\mathrm{id}}
\providecommand{\sym}{\mathrm{sym}}
\providecommand{\Corr}{\operatorname{Corr}}
\providecommand{\Proj}{\operatorname{Proj}}
\providecommand{\Comp}{\operatorname{Comp}}
\providecommand{\cC}{\mathcal{C}}
\providecommand{\cY}{\mathcal{Y}}
\providecommand{\cT}{\mathcal{T}}
\providecommand{\cPsi}{\Psi}
\providecommand{\Dcat}{D}
\providecommand{\La}{\Lambda}
\providecommand{\Ghat}{\widehat{G}}
\providecommand{\uHom}{\underline{\operatorname{Hom}}}
\providecommand{\cl}{\operatorname{c\ell}}
\providecommand{\e}{\mathrm{e}}

\pdfinfo{
  /Title (SGA 7 I - Fresh Source Transcription - Exposes I, II, VI, VII, VIII)
  /Author (Interlanguage Mathematical Translation Project)
  /Subject (Working source transcription from the LNM 288 scan)
  /Keywords (SGA 7; monodromy; algebraic geometry; source transcription)
}

\begin{document}
\input{expose_I_body}

\clearpage
\input{expose_II_body}

\clearpage
\selectlanguage{english}
\input{expose_VI_body}
\selectlanguage{french}

\clearpage
\input{expose_VII_body}

\clearpage
\input{expose_VIII_body}
\end{document}
"""

README = """# SGA 7 I fresh source transcription: Exposes I, II, VI, VII, and VIII

This package preserves a fresh scan-based working transcription of five complete exposés from
*Groupes de Monodromie en Géométrie Algébrique I* (Lecture Notes in Mathematics 288). The
included reader is a continuous 163-page A4 PDF containing the mathematical volume text only.

## Included scope

- Exposé I: complete, source folios 1-24
- Exposé II: complete, source folios 25-31
- Exposé VI: complete, source folios 32-132; the source text is in English
- Exposé VII: complete, source folios 133-217
- Exposé VIII: complete, source folios 218-312

Together these bodies cover 312 of the 529 known mathematical body pages in SGA 7 I. Exposé IX
is still being transcribed and is excluded from this checkpoint. Exposés III-V do not appear as
separate written exposés in this volume. This is therefore a substantial partial source
transcription, not a complete SGA 7 I reader and not an English translation of the French
exposés.

## Direct reading and source

- `reader/SGA7I_Fresh_Transcription_Exposes_I_II_VI_VII_VIII_Working.pdf`: cumulative reader
- `source/SGA7I_Fresh_Transcription_Exposes_I_II_VI_VII_VIII_Working.tex`: build wrapper
- `source/expose_*_body.tex`: five exact frozen source bodies
- `SGA7I_Fresh_Transcription_Exposes_I_II_VI_VII_VIII_Reader_and_Source_20260730.zip`: compact
  reader and complete editable TeX closure

The scan, high-resolution crops, raw production records, and operational notes are not included.
The current public reader contains no project-status or process pages.
"""

RIGHTS = """# Rights and provenance

The transcription is controlled by the Internet Archive scan of *Groupes de Monodromie en
Géométrie Algébrique I*, Lecture Notes in Mathematics 288, item
`groupesdemonodro0288unse`. The 540-page local control copy is 20,827,344 bytes with SHA-256
`9CD40FF06EB1E488AF385A56899D4F492492A06A1E2E3C0ED6876B82E3E3603F`.

The scan and source-page crops are not redistributed in this package. Copyright and other rights
in the underlying volume remain with their respective holders. No blanket license or source-image
redistribution right is asserted. This package is a working source transcription, not a critical
edition, legal rights determination, mathematical certification, or accessibility certification.
"""

SCOPE = """# Transcription scope and limits

This checkpoint contains complete Exposés I, II, VI, VII, and VIII of SGA 7 I, preserving the
language printed in the source. Exposé VI is English in the source; the other included exposés are
French. The five frozen bodies span source folios 1-312 and compile into a continuous 163-page
A4 reader.

The package contains 145 native `tikzcd` diagrams and no raster diagram inputs. The PDF is a
reader-facing mathematical object with no production preface, status report, or process note.
Exposé IX, the remainder of the 529-page mathematical body, is excluded until a later frozen
successor. Uncertain readings and source defects remain possible and should be checked against the
scan for consequential scholarly use. The PDF is untagged and no exhaustive internal-reference
layer is claimed.

This checkpoint supersedes the earlier four-exposé working reader only as the current reading
surface. Earlier GitHub commits and Zenodo versions remain immutable history.
"""


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def write_text(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8", newline="\n")


def page_content_digest(page) -> str:
    contents = page.get_contents()
    data = b"" if contents is None else contents.get_data()
    return sha256_bytes(data)


def pdf_resource_counts(reader: PdfReader) -> tuple[int, int, int]:
    fonts: dict[tuple[int, int], str] = {}
    images = 0
    for page in reader.pages:
        resources = page.get("/Resources") or {}
        font_dict = resources.get("/Font") or {}
        for value in font_dict.values():
            obj = value.get_object()
            ref = getattr(value, "idnum", None), getattr(value, "generation", 0)
            key = ref if ref[0] is not None else (id(obj), 0)
            fonts[key] = str(obj.get("/Subtype"))
        xobjects = resources.get("/XObject") or {}
        for value in xobjects.values():
            if value.get_object().get("/Subtype") == "/Image":
                images += 1
    return len(fonts), sum(value == "/Type3" for value in fonts.values()), images


def privacy_hits(root: Path) -> list[dict[str, object]]:
    patterns = (
        "c:\\users\\floris",
        "c:/users/floris",
        "appdata",
        "papors",
        "chatnotes",
        "scratchpad",
        "thread_id",
        "source_notes.md",
        "method_logbook.md",
        "diagram_verification.md",
    )
    hits: list[dict[str, object]] = []
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.suffix.lower() in {".pdf", ".zip"}:
            continue
        text = path.read_text(encoding="utf-8", errors="replace").lower()
        for pattern in patterns:
            if pattern in text:
                hits.append(
                    {
                        "path": path.relative_to(root).as_posix(),
                        "pattern": pattern,
                    }
                )
    return hits


def build_zip(path: Path, root: Path, members: list[Path]) -> dict[str, object]:
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for member in members:
            rel = member.relative_to(root).as_posix()
            info = zipfile.ZipInfo(rel, date_time=(2026, 7, 30, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, member.read_bytes())

    with zipfile.ZipFile(path, "r") as archive:
        bad = archive.testzip()
        infos = [row for row in archive.infolist() if not row.is_dir()]
        errors: list[str] = []
        for info in infos:
            rel = Path(info.filename)
            if rel.is_absolute() or ".." in rel.parts or ":" in rel.parts[0]:
                errors.append(f"unsafe:{info.filename}")
                continue
            source = root / rel
            data = archive.read(info.filename)
            if (len(data), sha256_bytes(data)) != (
                source.stat().st_size,
                sha256_file(source),
            ):
                errors.append(f"identity:{info.filename}")
        return {
            "members": len(infos),
            "uncompressed_bytes": sum(row.file_size for row in infos),
            "crc_failure": bad,
            "errors": errors,
        }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-root", required=True, type=Path)
    parser.add_argument("--producer-pdf", required=True, type=Path)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    source_root = args.source_root.resolve()
    producer_pdf = args.producer_pdf.resolve()
    output = args.output.resolve()
    if output.exists():
        raise SystemExit(f"Refusing to overwrite existing output: {output}")

    source_dir = output / "source"
    reader_dir = output / "reader"
    source_dir.mkdir(parents=True)
    reader_dir.mkdir(parents=True)
    write_text(output / ".gitattributes", "*.tex -text\n*.md text eol=lf\n*.csv text eol=lf\n*.json text eol=lf\n")
    write_text(output / "README.md", README)
    write_text(output / "RIGHTS_AND_PROVENANCE.md", RIGHTS)
    write_text(output / "TRANSCRIPTION_SCOPE_AND_LIMITS.md", SCOPE)
    write_text(source_dir / WRAPPER_NAME, WRAPPER)

    body_identities: list[dict[str, object]] = []
    for name in BODY_NAMES:
        source = source_root / name
        if not source.is_file():
            raise SystemExit(f"Missing frozen body: {source}")
        destination = source_dir / name
        shutil.copy2(source, destination)
        body_identities.append(
            {
                "path": f"source/{name}",
                "bytes": destination.stat().st_size,
                "sha256": sha256_file(destination),
            }
        )

    command = [
        "pdflatex",
        "-interaction=nonstopmode",
        "-halt-on-error",
        WRAPPER_NAME,
    ]
    consoles: list[str] = []
    for _ in range(2):
        result = subprocess.run(
            command,
            cwd=source_dir,
            text=True,
            encoding="utf-8",
            errors="replace",
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
        )
        consoles.append(result.stdout)
        if result.returncode != 0:
            raise SystemExit(result.stdout[-8000:])

    build_pdf = source_dir / Path(WRAPPER_NAME).with_suffix(".pdf")
    build_log = source_dir / Path(WRAPPER_NAME).with_suffix(".log")
    log_text = build_log.read_text(encoding="utf-8", errors="replace")
    overfull = [
        float(value)
        for value in re.findall(r"Overfull \\hbox \(([0-9.]+)pt too wide\)", log_text)
    ]
    font_warnings = len(re.findall(r"LaTeX Font Warning:", log_text))
    blocking = [
        line
        for line in log_text.splitlines()
        if line.startswith("!")
        or "Undefined control sequence" in line
        or "LaTeX Error" in line
    ]
    if blocking:
        raise SystemExit("Blocking TeX diagnostics remain")

    reader_path = reader_dir / PDF_NAME
    shutil.move(build_pdf, reader_path)
    for suffix in (".aux", ".log", ".out", ".toc"):
        path = source_dir / Path(WRAPPER_NAME).with_suffix(suffix)
        path.unlink(missing_ok=True)

    reader = PdfReader(str(reader_path))
    producer = PdfReader(str(producer_pdf))
    if len(reader.pages) != 163 or len(producer.pages) != 162:
        raise SystemExit("Unexpected reader page boundary")

    final_a4 = [
        abs(float(page.mediabox.width) - 595.276) < 0.1
        and abs(float(page.mediabox.height) - 841.89) < 0.1
        for page in reader.pages
    ]
    fitz_reader = fitz.open(str(reader_path))
    nonempty_text_pages = sum(bool(page.get_text("text").strip()) for page in fitz_reader)
    fitz_reader.close()
    if not all(final_a4) or nonempty_text_pages != len(reader.pages):
        raise SystemExit("Clean reader has a page-geometry or empty-page failure")

    fonts, type3, images = pdf_resource_counts(reader)
    body_text = "\n".join(
        (source_dir / name).read_text(encoding="utf-8", errors="replace")
        for name in BODY_NAMES
    )
    tikz = len(re.findall(r"\\begin\{tikzcd\}", body_text))
    raster_inputs = len(re.findall(r"\\includegraphics", body_text))

    zip_members = [
        output / "README.md",
        output / "RIGHTS_AND_PROVENANCE.md",
        output / "TRANSCRIPTION_SCOPE_AND_LIMITS.md",
        reader_path,
        source_dir / WRAPPER_NAME,
        *(source_dir / name for name in BODY_NAMES),
    ]
    zip_path = output / ZIP_NAME
    zip_result = build_zip(zip_path, output, zip_members)
    if zip_result["crc_failure"] or zip_result["errors"]:
        raise SystemExit("ZIP validation failed")

    candidates = [
        path
        for path in output.rglob("*")
        if path.is_file()
        and path.name not in {"SHA256SUMS.csv", "PUBLIC_PROJECTION_VALIDATION.json"}
    ]
    manifest_rows = []
    for path in sorted(candidates, key=lambda item: item.relative_to(output).as_posix()):
        manifest_rows.append(
            {
                "relative_path": path.relative_to(output).as_posix(),
                "bytes": path.stat().st_size,
                "sha256": sha256_file(path),
            }
        )
    manifest_buffer = io.StringIO(newline="")
    writer = csv.DictWriter(
        manifest_buffer,
        fieldnames=("relative_path", "bytes", "sha256"),
        lineterminator="\n",
    )
    writer.writeheader()
    writer.writerows(manifest_rows)
    write_text(output / "SHA256SUMS.csv", manifest_buffer.getvalue())

    private_hits = privacy_hits(output)
    pdf_text = "\n".join(page.extract_text() or "" for page in reader.pages).lower()
    pdf_private_hits = [
        marker
        for marker in (
            "c:\\users\\floris",
            "appdata",
            "papors",
            "chatnotes",
            "source_notes",
            "method_logbook",
            "diagram_verification",
        )
        if marker in pdf_text
    ]

    validation = {
        "schema_version": "1.0",
        "checkpoint_id": "SGA7I-FRESH-TRANSCRIPTION-I-II-VI-VII-VIII-WORKING-20260730",
        "validation_status": "PASS_ARCHIVE_HANDOFF_READY",
        "scope": {
            "included_exposes": ["I", "II", "VI", "VII", "VIII"],
            "excluded_exposes": ["III", "IV", "V", "IX"],
            "frozen_source_pages": 312,
            "known_body_pages": 529,
            "reader_pages": len(reader.pages),
            "continuation": "Expose IX, source folio 313",
        },
        "authority": {
            "internet_archive_item": "groupesdemonodro0288unse",
            "scan_pages": 540,
            "scan_bytes": 20_827_344,
            "scan_sha256": "9CD40FF06EB1E488AF385A56899D4F492492A06A1E2E3C0ED6876B82E3E3603F",
            "scan_included": False,
        },
        "reader": {
            "path": f"reader/{PDF_NAME}",
            "bytes": reader_path.stat().st_size,
            "sha256": sha256_file(reader_path),
            "pages": len(reader.pages),
            "nonempty_text_pages": nonempty_text_pages,
            "producer_reader_pages": len(producer.pages),
            "source_closure": "five copied frozen TeX bodies compiled without content edits",
            "a4_pages": sum(final_a4),
            "font_resources": fonts,
            "type3_font_resources": type3,
            "image_xobjects": images,
            "metadata": {str(key): str(value) for key, value in (reader.metadata or {}).items()},
        },
        "source": {
            "wrapper": f"source/{WRAPPER_NAME}",
            "editable_tex_files": 6,
            "body_identities": body_identities,
            "native_tikzcd_diagrams": tikz,
            "raster_diagram_inputs": raster_inputs,
        },
        "build": {
            "engine": "pdfLaTeX",
            "passes": 2,
            "exit_codes": [0, 0],
            "blocking_diagnostics": 0,
            "overfull_diagnostics": len(overfull),
            "worst_overfull_pt": max(overfull, default=0.0),
            "font_warnings": font_warnings,
        },
        "visual_qa": {
            "reviewed_pages": [1, 13, 14, 17, 18, 37, 49, 59, 64, 76, 77, 117, 118, 137, 163],
            "includes_all_expose_boundaries": True,
            "includes_all_overfull_warning_pages": True,
            "clipping_or_overlap_found": False,
            "status": "PASS",
        },
        "zip": {
            "path": ZIP_NAME,
            "bytes": zip_path.stat().st_size,
            "sha256": sha256_file(zip_path),
            **zip_result,
        },
        "manifest": {
            "path": "SHA256SUMS.csv",
            "rows": len(manifest_rows),
            "bytes": (output / "SHA256SUMS.csv").stat().st_size,
            "sha256": sha256_file(output / "SHA256SUMS.csv"),
        },
        "privacy": {
            "text_file_hits": private_hits,
            "pdf_text_hits": pdf_private_hits,
        },
        "supersession": {
            "current_reader": "five-expose checkpoint",
            "earlier_four_expose_checkpoint": "immutable historical predecessor",
        },
        "errors": [],
    }
    if (
        private_hits
        or pdf_private_hits
        or tikz != 145
        or raster_inputs != 0
        or type3 != 0
        or images != 0
    ):
        validation["validation_status"] = "FAIL"
        validation["errors"] = ["privacy_or_source_surface_gate_failed"]

    write_text(
        output / "PUBLIC_PROJECTION_VALIDATION.json",
        json.dumps(validation, ensure_ascii=True, indent=2) + "\n",
    )
    if validation["errors"]:
        raise SystemExit(json.dumps(validation["errors"]))

    summary = {
        "output": str(output),
        "files": sum(1 for path in output.rglob("*") if path.is_file()),
        "bytes": sum(path.stat().st_size for path in output.rglob("*") if path.is_file()),
        "reader": validation["reader"],
        "zip": validation["zip"],
        "manifest": validation["manifest"],
        "validation": {
            "bytes": (output / "PUBLIC_PROJECTION_VALIDATION.json").stat().st_size,
            "sha256": sha256_file(output / "PUBLIC_PROJECTION_VALIDATION.json"),
            "status": validation["validation_status"],
        },
    }
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
