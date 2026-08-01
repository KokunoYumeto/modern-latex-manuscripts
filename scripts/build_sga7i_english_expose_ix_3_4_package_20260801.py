#!/usr/bin/env python3
"""Freeze and validate SGA7 I English through Expose IX section 3.4.0."""

from __future__ import annotations

import csv
import hashlib
import io
import json
import re
import shutil
import subprocess
import tempfile
import zipfile
from pathlib import Path, PurePosixPath

from pypdf import PdfReader


REPO_ROOT = Path(__file__).resolve().parents[1]
WORKING_ROOT = Path(
    r"C:\Users\Floris\Documents\interlanguage\03_projects\language_management"
    r"\english_germanic\03_working_translations"
    r"\sga7i_english_complete_translation_successor_20260731_r1"
)
PACKAGE_ROOT = REPO_ROOT / (
    "sources/sga/"
    "sga7i-english-source-first-working-through-expose-ix-3-4-20260801"
)
WORKING_MASTER = WORKING_ROOT / "source/SGA7_I_English_source_first_workpass.tex"
WORKING_PDF = WORKING_ROOT / (
    "build/checkpoint_expose_IX_sections_3_2_through_3_4_r1/"
    "SGA7_I_English_source_first_workpass.pdf"
)
MASTER_REL = Path(
    "source/SGA7I_English_Working_Through_Expose_IX_3_4_20260801.tex"
)
PDF_REL = Path(
    "reader/SGA7I_English_Working_Through_Expose_IX_3_4_20260801.pdf"
)
ZIP_NAME = (
    "SGA7I_English_Working_Through_Expose_IX_3_4_"
    "Reader_and_TeX_20260801.zip"
)
ZIP_MANIFEST = "ZIP_MEMBER_SHA256SUMS.csv"
OUTER_MANIFEST = "SHA256SUMS.csv"
VALIDATION = "PACKAGE_VALIDATION.json"
EXPECTED_COMPONENTS = 137
EXPECTED_MASTER = (
    10_181,
    "71F2D7A16CCEABEDC4E2E3E1F0612B2CA1895583751EB43C7361C6949CBEC2A4",
)
EXPECTED_READER = (
    1_551_833,
    "BF474B377BBFF5BECB561A0FBDBF8E426842F70FDE3043572687D159F864395F",
)
EXPECTED_REBUILD = (
    1_551_821,
    "5132DD33D600D21F58F3DD7CC579BFAD74D1DACFDBFF4BC79C68A2D244E7DCE8",
)
EXPECTED_BUILD_LOG = (
    42_588,
    "01653D962A0C29221F0099C41F710971366B25B44EE128604D756DB52D70B4DA",
)
AUTHORITY_SCAN_SHA256 = (
    "9CD40FF06EB1E488AF385A56899D4F492492A06A1E2E3C0ED6876B82E3E3603F"
)
TRANSCRIPTION_MASTER_SHA256 = (
    "7B7394BEAF970AC724EFDE80C841B2DAACC28D64E3145538A39AA2FA915BF355"
)
ZIP_TIMESTAMP = (2026, 8, 1, 0, 0, 0)
VISUAL_RENDER_SHA256 = {
    "page-181.png": "D7E0E16D50361C61A348BB77E9BD6602180A64798AC7022254031C72FF3F6514",
    "page-182.png": "398566F1AF6BA271E8C37989420FAEF8C19926C30E1226C8310ECF0FEB43E1DE",
    "page-196.png": "4DE34F4A2E61A9544F627DEAAACAB895B98BD1E51C19C6428435E9F9DE1586AD",
    "page-197.png": "19E3DAB2419BC2BAE52EAFA53EDCBCBD4A19D87435811B9A3B925208ABD14C66",
    "page-198.png": "984B4A9A3FA7ADA2155899DAE2DB93B53023BE4E87F2B8339A28A5B71E9F6C7E",
}
PRIVACY_PATTERNS = {
    "private_home": re.compile(r"C:\\Users\\Floris", re.IGNORECASE),
    "archive_worktree": re.compile(r"C:\\w(?:\\|/)", re.IGNORECASE),
    "papors": re.compile(r"\bPapors\b", re.IGNORECASE),
    "chatnotes": re.compile(r"\bChatnotes\b", re.IGNORECASE),
    "agent_name": re.compile(r"\b(?:Claude|ChatGPT|Codex|OpenAI)\b", re.IGNORECASE),
    "task_id": re.compile(r"\b019f[0-9a-f-]{20,}\b", re.IGNORECASE),
}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def sha256_path(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def identity(path: Path) -> tuple[int, str]:
    return path.stat().st_size, sha256_path(path)


def relative(path: Path) -> str:
    return path.relative_to(PACKAGE_ROOT).as_posix()


def write_json(path: Path, value: object) -> None:
    path.write_text(
        json.dumps(value, indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def csv_bytes(rows: list[dict[str, object]]) -> bytes:
    output = io.StringIO(newline="")
    writer = csv.DictWriter(
        output,
        fieldnames=["path", "bytes", "sha256"],
        lineterminator="\n",
        quoting=csv.QUOTE_ALL,
    )
    writer.writeheader()
    writer.writerows(rows)
    return output.getvalue().encode("utf-8")


def safe_member(name: str) -> bool:
    pure = PurePosixPath(name)
    return (
        name == name.replace("\\", "/")
        and not pure.is_absolute()
        and ".." not in pure.parts
        and not (len(name) > 1 and name[1] == ":")
    )


def numbered_components(root: Path) -> list[Path]:
    rows = list(root.glob("*.tex"))
    return sorted(rows, key=lambda path: int(path.name.split("_", 1)[0]))


def source_snapshot(master: Path, components: list[Path]) -> dict[str, tuple[int, str]]:
    rows = [master, *components]
    return {
        ("master" if path == master else f"components/{path.name}"): identity(path)
        for path in rows
    }


def copy_frozen_source(frozen_root: Path) -> dict[str, object]:
    frozen_master = frozen_root / MASTER_REL.name
    components = numbered_components(frozen_root / "components")
    before = source_snapshot(frozen_master, components)
    if len(before) != EXPECTED_COMPONENTS + 1:
        raise RuntimeError("Frozen source component boundary changed")
    if before["master"] != EXPECTED_MASTER:
        raise RuntimeError("Frozen master identity changed")
    if identity(WORKING_PDF) != EXPECTED_READER:
        raise RuntimeError("Working reader identity changed")
    master_text = frozen_master.read_text(encoding="utf-8")
    inputs = re.findall(r"\\input\{components/([^}]+)\}", master_text)
    if inputs != [path.stem for path in components]:
        raise RuntimeError("Master/component input closure changed")
    if inputs[-1] != "137_expose_IX_sections_3_2_through_3_4":
        raise RuntimeError("Expose-IX-section-3.4 cursor changed")
    if "138_expose" in master_text:
        raise RuntimeError("Master crossed the frozen Proposition 3.5 cursor")

    live_components = {
        path.name: identity(path)
        for path in numbered_components(WORKING_ROOT / "source/components")
        if int(path.name.split("_", 1)[0]) <= EXPECTED_COMPONENTS
    }
    frozen_components = {path.name: identity(path) for path in components}
    if live_components != frozen_components:
        raise RuntimeError("Live components 1-137 diverged from the frozen snapshot")

    if PACKAGE_ROOT.exists():
        raise RuntimeError(f"No-overwrite package already exists: {PACKAGE_ROOT}")
    (PACKAGE_ROOT / "source/components").mkdir(parents=True)
    (PACKAGE_ROOT / "reader").mkdir(parents=True)
    shutil.copy2(frozen_master, PACKAGE_ROOT / MASTER_REL)
    for path in components:
        shutil.copy2(path, PACKAGE_ROOT / "source/components" / path.name)
    shutil.copy2(WORKING_PDF, PACKAGE_ROOT / PDF_REL)
    after = source_snapshot(frozen_master, components)
    if before != after:
        raise RuntimeError("Working source changed during snapshot")
    copied = {
        "master": identity(PACKAGE_ROOT / MASTER_REL),
        **{
            f"components/{path.name}": identity(
                PACKAGE_ROOT / "source/components" / path.name
            )
            for path in components
        },
    }
    if copied != before:
        raise RuntimeError("Copied source is not byte-identical")
    return {
        "tex_files": len(copied),
        "components": EXPECTED_COMPONENTS,
        "master_bytes": EXPECTED_MASTER[0],
        "master_sha256": EXPECTED_MASTER[1],
        "last_component": f"source/components/{components[-1].name}",
        "last_component_sha256": identity(components[-1])[1],
        "pre_post_snapshot_exact": True,
        "copied_source_exact": True,
    }


def page_stream(page) -> bytes:
    contents = page.get_contents()
    return b"" if contents is None else contents.get_data()


def pdf_resources(reader: PdfReader) -> dict[str, int]:
    font_ids: set[tuple[int, int] | str] = set()
    embedded_ids: set[tuple[int, int] | str] = set()
    type3_ids: set[tuple[int, int] | str] = set()
    image_xobjects = 0
    goto_actions = 0
    uri_actions = 0
    for page in reader.pages:
        resources = page.get("/Resources") or {}
        fonts = resources.get("/Font") if hasattr(resources, "get") else None
        if fonts:
            for name, reference in fonts.get_object().items():
                key = getattr(reference, "idnum", None)
                key = (key, getattr(reference, "generation", 0)) if key else str(name)
                font = reference.get_object()
                font_ids.add(key)
                if font.get("/Subtype") == "/Type3":
                    type3_ids.add(key)
                descriptor = font.get("/FontDescriptor")
                if descriptor is None:
                    descendants = font.get("/DescendantFonts")
                    if descendants:
                        descriptor = descendants[0].get_object().get("/FontDescriptor")
                if descriptor:
                    descriptor = descriptor.get_object()
                    if any(
                        descriptor.get(field) is not None
                        for field in ("/FontFile", "/FontFile2", "/FontFile3")
                    ):
                        embedded_ids.add(key)
                elif font.get("/Subtype") == "/Type3":
                    embedded_ids.add(key)
        xobjects = resources.get("/XObject") if hasattr(resources, "get") else None
        if xobjects:
            for reference in xobjects.get_object().values():
                if reference.get_object().get("/Subtype") == "/Image":
                    image_xobjects += 1
        for annotation in page.get("/Annots") or []:
            row = annotation.get_object()
            action = row.get("/A")
            if action:
                action = action.get_object()
                if action.get("/S") == "/GoTo":
                    goto_actions += 1
                elif action.get("/S") == "/URI":
                    uri_actions += 1
    return {
        "font_resources": len(font_ids),
        "embedded_font_resources": len(embedded_ids),
        "type3_font_resources": len(type3_ids),
        "image_xobjects": image_xobjects,
        "goto_actions": goto_actions,
        "uri_actions": uri_actions,
    }


def inspect_and_compare_pdfs(rebuild_pdf: Path) -> tuple[dict[str, object], str]:
    public_path = PACKAGE_ROOT / PDF_REL
    if identity(public_path) != EXPECTED_READER:
        raise RuntimeError("Frozen reader identity changed")
    if identity(rebuild_pdf) != EXPECTED_REBUILD:
        raise RuntimeError("Isolated rebuild identity changed")
    public = PdfReader(str(public_path))
    rebuild = PdfReader(str(rebuild_pdf))
    if len(public.pages) != 198 or len(rebuild.pages) != 198:
        raise RuntimeError("Reader page count changed")
    geometry = 0
    streams = 0
    texts = 0
    text_pages = 0
    extracted: list[str] = []
    for original, fresh in zip(public.pages, rebuild.pages, strict=True):
        if tuple(original.mediabox) == tuple(fresh.mediabox):
            geometry += 1
        original_text = original.extract_text() or ""
        fresh_text = fresh.extract_text() or ""
        extracted.append(original_text)
        if original_text.strip():
            text_pages += 1
        if original_text == fresh_text:
            texts += 1
        if page_stream(original) == page_stream(fresh):
            streams += 1
    if (geometry, streams, texts, text_pages) != (198, 198, 198, 198):
        raise RuntimeError("Isolated rebuild page comparison changed")
    resources = pdf_resources(public)
    if resources["image_xobjects"] != 0:
        raise RuntimeError("Reader unexpectedly contains raster page content")
    metadata = {str(k): str(v) for k, v in (public.metadata or {}).items()}
    if metadata.get("/Title") != "SGA 7 I - Working English Translation":
        raise RuntimeError("Reader metadata title changed")
    return (
        {
            "pages": 198,
            "page_size": "A4",
            "bytes": EXPECTED_READER[0],
            "sha256": EXPECTED_READER[1],
            "nonempty_text_pages": text_pages,
            **resources,
            "decoded_content_stream_exact_pages": streams,
            "extracted_text_exact_pages": texts,
            "geometry_exact_pages": geometry,
            "rebuild_bytes": EXPECTED_REBUILD[0],
            "rebuild_sha256": EXPECTED_REBUILD[1],
            "metadata": metadata,
            "tagged_accessibility_claim": False,
        },
        "\n".join(extracted),
    )


def verify_build(build_log: Path, pass2: Path, pass3: Path) -> dict[str, object]:
    if identity(build_log) != EXPECTED_BUILD_LOG:
        raise RuntimeError("Isolated build log identity changed")
    if pass2.read_bytes() != pass3.read_bytes():
        raise RuntimeError("Isolated build did not converge")
    content = build_log.read_text(encoding="utf-8", errors="replace")
    patterns = (
        r"LaTeX Warning:",
        r"Package .* Warning:",
        r"Overfull \\hbox",
        r"Underfull \\hbox",
        r"Undefined control sequence",
        r"! LaTeX Error",
        r"Fatal error",
        r"Rerun to get",
        r"Missing character",
    )
    if any(re.search(pattern, content, re.IGNORECASE) for pattern in patterns):
        raise RuntimeError("Isolated build log contains a diagnostic")
    warning_count = len(
        re.findall(r"(?:LaTeX(?: Font)?|Package [^\n]+) Warning:", content)
    )
    inherited_warning = re.search(
        r"LaTeX Font Warning: Command \\footnotesize invalid in math mode "
        r"on input line\s+17\s*4\.",
        content,
    )
    if warning_count != 1 or inherited_warning is None:
        raise RuntimeError("Unexpected isolated-build warning surface")
    return {
        "isolated_pdflatex_passes": 3,
        "exit_codes": [0, 0, 0],
        "pass2_pass3_console_exact": True,
        "pass_console_sha256": sha256_path(pass3),
        "blocking_diagnostics": 0,
        "warnings": 1,
        "known_inherited_font_warning": (
            "Command \\footnotesize invalid in math mode in component 97"
        ),
        "overfull_boxes": 0,
        "underfull_boxes": 0,
        "final_log_bytes": EXPECTED_BUILD_LOG[0],
        "final_log_sha256": EXPECTED_BUILD_LOG[1],
    }


def verify_visuals(render_root: Path) -> dict[str, object]:
    for name, wanted in VISUAL_RENDER_SHA256.items():
        path = render_root / name
        if not path.is_file() or sha256_path(path) != wanted:
            raise RuntimeError(f"Visual render identity changed: {name}")
    return {
        "render_dpi": 600,
        "directly_inspected_pages": [181, 182, 196, 197, 198],
        "render_sha256": VISUAL_RENDER_SHA256,
        "checked_boundaries": [
            "Expose VIII bibliography and end",
            "Expose IX title, contents, and opening",
            "Expose IX Proposition 3.2 and Corollary 3.3",
            "Expose IX Definition 3.4 and section 3.4.0 terminal boundary",
        ],
        "clipping_overlap_blank_or_malformed_content_errors": 0,
    }


README = """# SGA 7 I English working reader through Expose IX section 3.4.0

This current-progress reader contains complete English Exposes I, II, VI,
VII, and VIII, followed by Expose IX through section 3.4.0. It covers source
folios 1-349 of the 528-folio SGA 7 I scan. The exact continuation is Expose IX
Proposition 3.5, authority `source/expose_IX_body.tex` line 880, zero-based scan
index 361 / source folio 350 / physical PDF page 362.

This is a bounded working reader, not a complete English SGA 7 I, critical
edition, peer review, mathematical certification, accessibility certification,
or rights-clearance decision.

## Read or build

- `reader/SGA7I_English_Working_Through_Expose_IX_3_4_20260801.pdf`
  is the 198-page A4 reader.
- `source/SGA7I_English_Working_Through_Expose_IX_3_4_20260801.tex`
  is the exact frozen wrapper used for that reader.
- `source/components/` contains the exact 137 editable components used by the
  wrapper.
- `SGA7I_English_Working_Through_Expose_IX_3_4_Reader_and_TeX_20260801.zip`
  groups the reader and complete buildable TeX for one-click use.

The reader begins directly with the mathematics and contains no process
preface. A fresh isolated three-pass pdfLaTeX build reproduces the geometry,
decoded page-content streams, and extracted text of all 198 pages exactly.
Pages 181-182 and 196-198 were rendered at 600 dpi and inspected directly;
the Expose VIII/IX join and terminal section-3.4 pages are clean.
"""

RIGHTS = """# Rights and provenance

The controlling source image is the 540-page SGA 7 I scan with SHA-256
`9CD40FF06EB1E488AF385A56899D4F492492A06A1E2E3C0ED6876B82E3E3603F`.
The complete French working transcription used for page mapping has master
SHA-256
`7B7394BEAF970AC724EFDE80C841B2DAACC28D64E3145538A39AA2FA915BF355`.
The source image controls consequential ambiguities. The working transcription
is an editable and locator witness, not a replacement for the scan.

Expose VI is an originally English contribution by D. S. Rim. Exposes I, II,
VII, VIII, and IX are project English translations. Source-image review was used
to check translated text, formulas, diagrams, page mapping, and the continuation
point. The source scan is not duplicated inside this compact reader package.

This package does not assert a blanket license, transfer ownership, or decide
the rights status of the underlying source. Rights and attribution remain with
their respective holders. It preserves a bounded scholarly working reader and
its editable source; it is not a complete SGA 7 I edition, a critical edition,
or independent mathematical certification.
"""

SOURCE_CORRECTION = """# Source-reference correction

Archive replay found one concrete mismatch in Remark 4.16.

- authority location: zero-based scan index 124, printed page 113;
- authority reading: `which generalizes 4.12(b)`;
- producer checkpoint reading: `which generalizes 4.13(b)`;
- public-successor reading: `which generalizes 4.12(b)`;
- affected file: `source/components/49_expose_VI_remark_4_16.tex`.

The authority page was opened directly at 600 dpi. The correction changes no
formula, theorem statement, page map, or continuation cursor. The current reader
through Expose IX section 3.4.0 retains the corrected reading.
"""


def write_public_docs(source: dict[str, object], reader: dict[str, object], build: dict[str, object]) -> None:
    (PACKAGE_ROOT / "README.md").write_text(README, encoding="utf-8", newline="\n")
    (PACKAGE_ROOT / "RIGHTS_AND_PROVENANCE.md").write_text(
        RIGHTS, encoding="utf-8", newline="\n"
    )
    (PACKAGE_ROOT / "SOURCE_CORRECTION.md").write_text(
        SOURCE_CORRECTION, encoding="utf-8", newline="\n"
    )
    summary = "\n".join(
        [
            "# Build and QA summary",
            "",
            f"- Frozen wrapper: {source['master_bytes']:,} bytes, SHA-256 `{source['master_sha256']}`.",
            f"- Editable closure: one wrapper plus {source['components']} referenced component files, with no missing or unreferenced component.",
            f"- Reader: {reader['pages']} A4 pages, {reader['bytes']:,} bytes, SHA-256 `{reader['sha256']}`.",
            "- Isolated build: three pdfLaTeX passes, exit codes 0/0/0; pass 2 and pass 3 console output byte-identical; no errors, overfull or underfull boxes, undefined references, missing inputs, or rerun requests. One inherited component-97 font-size warning remains disclosed and is visually harmless.",
            f"- Isolated rebuild comparison: {reader['pages']}/{reader['pages']} page geometries, decoded content streams, and extracted texts exact. The rebuilt file differs only in PDF timestamp metadata.",
            f"- Reader inspection: {reader['nonempty_text_pages']}/{reader['pages']} pages contain extractable text; {reader['embedded_font_resources']}/{reader['font_resources']} font resources embedded; {reader['type3_font_resources']} Type 3 resources; zero image XObjects.",
            "- Direct visual review: pages 181-182 and 196-198 rendered at 600 dpi, covering the Expose VIII/IX join and the terminal section-3.4 pages; no blank page, clipping, overlap, or malformed displayed mathematics found.",
            "- Privacy and reader-surface review: no private absolute path, pending-review note, process note, or internal tooling text in the editable source, PDF metadata, or extracted reader text.",
            "",
        ]
    )
    (PACKAGE_ROOT / "BUILD_AND_QA_SUMMARY.md").write_text(
        summary, encoding="utf-8", newline="\n"
    )


def zip_source_files() -> list[Path]:
    rows = [PACKAGE_ROOT / PDF_REL, PACKAGE_ROOT / "README.md"]
    rows.extend(
        sorted(
            (PACKAGE_ROOT / "source/components").glob("*.tex"),
            key=lambda path: int(path.name.split("_", 1)[0]),
        )
    )
    rows.append(PACKAGE_ROOT / MASTER_REL)
    if len(rows) != 140:
        raise RuntimeError("Reader/TeX ZIP source boundary changed")
    return rows


def write_zip() -> dict[str, object]:
    files = zip_source_files()
    rows = [
        {"path": relative(path), "bytes": path.stat().st_size, "sha256": sha256_path(path)}
        for path in files
    ]
    manifest_data = csv_bytes(rows)
    (PACKAGE_ROOT / ZIP_MANIFEST).write_bytes(manifest_data)
    zip_path = PACKAGE_ROOT / ZIP_NAME

    def create(path: Path) -> None:
        with zipfile.ZipFile(
            path,
            "w",
            compression=zipfile.ZIP_DEFLATED,
            compresslevel=9,
            allowZip64=True,
        ) as archive:
            for source in files:
                info = zipfile.ZipInfo(relative(source), date_time=ZIP_TIMESTAMP)
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o100644 << 16
                info.create_system = 3
                archive.writestr(info, source.read_bytes(), compresslevel=9)
            info = zipfile.ZipInfo(ZIP_MANIFEST, date_time=ZIP_TIMESTAMP)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            info.create_system = 3
            archive.writestr(info, manifest_data, compresslevel=9)

    create(zip_path)
    first = zip_path.read_bytes()
    with tempfile.TemporaryDirectory() as directory:
        replay = Path(directory) / ZIP_NAME
        create(replay)
        if replay.read_bytes() != first:
            raise RuntimeError("Reader/TeX ZIP deterministic replay changed")
    with zipfile.ZipFile(zip_path) as archive:
        if archive.testzip() is not None:
            raise RuntimeError("Reader/TeX ZIP CRC validation failed")
        infos = [row for row in archive.infolist() if not row.is_dir()]
        names = [row.filename for row in infos]
        if len(names) != 141 or len(names) != len(set(names)):
            raise RuntimeError("Reader/TeX ZIP member boundary changed")
        if not all(safe_member(name) for name in names):
            raise RuntimeError("Reader/TeX ZIP has unsafe names")
        embedded = list(
            csv.DictReader(io.StringIO(archive.read(ZIP_MANIFEST).decode("utf-8")))
        )
        if len(embedded) != 140:
            raise RuntimeError("Reader/TeX ZIP manifest boundary changed")
        for row in embedded:
            data = archive.read(row["path"])
            if (len(data), sha256_bytes(data)) != (
                int(row["bytes"]),
                row["sha256"].upper(),
            ):
                raise RuntimeError(f"Reader/TeX ZIP member mismatch: {row['path']}")
    return {
        "bytes": zip_path.stat().st_size,
        "sha256": sha256_path(zip_path),
        "members": 141,
        "uncompressed_bytes": sum(row.file_size for row in infos),
        "manifest_rows": 140,
        "manifest_bytes": len(manifest_data),
        "manifest_sha256": sha256_bytes(manifest_data),
        "safe_names": True,
        "crc_errors": 0,
        "member_identity_errors": 0,
        "deterministic_replay_exact": True,
    }


def privacy_scan(reader_text: str) -> dict[str, object]:
    files = sorted(
        path
        for path in PACKAGE_ROOT.rglob("*")
        if path.is_file()
        and path.suffix.lower() in {".md", ".tex", ".csv", ".json"}
        and path.name not in {OUTER_MANIFEST, VALIDATION}
    )
    hits: list[dict[str, str]] = []
    for path in files:
        text = path.read_text(encoding="utf-8", errors="replace")
        for name, pattern in PRIVACY_PATTERNS.items():
            if pattern.search(text):
                hits.append({"path": relative(path), "pattern": name})
    metadata = json.dumps(PdfReader(str(PACKAGE_ROOT / PDF_REL)).metadata or {})
    for surface, text in ((PDF_REL.as_posix(), reader_text), (f"{PDF_REL.as_posix()}#metadata", metadata)):
        for name, pattern in PRIVACY_PATTERNS.items():
            if pattern.search(text):
                hits.append({"path": surface, "pattern": name})
    return {
        "scanned_text_files": len(files),
        "pdf_text_and_metadata_scanned": True,
        "occurrences": len(hits),
        "hits": hits,
    }


def write_outer_manifest() -> dict[str, object]:
    files = sorted(
        (path for path in PACKAGE_ROOT.rglob("*") if path.is_file() and path.name != OUTER_MANIFEST),
        key=lambda path: relative(path).casefold(),
    )
    rows = [
        {"path": relative(path), "bytes": path.stat().st_size, "sha256": sha256_path(path)}
        for path in files
    ]
    data = csv_bytes(rows)
    (PACKAGE_ROOT / OUTER_MANIFEST).write_bytes(data)
    return {"rows": len(rows), "bytes": len(data), "sha256": sha256_bytes(data)}


def package_snapshot() -> tuple[int, int, str]:
    files = sorted(
        (path for path in PACKAGE_ROOT.rglob("*") if path.is_file()),
        key=lambda path: relative(path).casefold(),
    )
    digest = hashlib.sha256()
    for path in files:
        digest.update(
            f"{relative(path)}\t{path.stat().st_size}\t{sha256_path(path)}\n".encode()
        )
    return len(files), sum(path.stat().st_size for path in files), digest.hexdigest().upper()


def verify_manifest() -> None:
    rows = list(
        csv.DictReader((PACKAGE_ROOT / OUTER_MANIFEST).open("r", encoding="utf-8", newline=""))
    )
    represented = {
        relative(path): path
        for path in PACKAGE_ROOT.rglob("*")
        if path.is_file() and path.name != OUTER_MANIFEST
    }
    if {row["path"] for row in rows} != set(represented):
        raise RuntimeError("Outer manifest closure changed")
    for row in rows:
        if identity(represented[row["path"]]) != (
            int(row["bytes"]),
            row["sha256"].upper(),
        ):
            raise RuntimeError(f"Outer manifest mismatch: {row['path']}")


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--rebuild-root", type=Path, required=True)
    parser.add_argument("--render-root", type=Path, required=True)
    args = parser.parse_args()
    rebuild_root = args.rebuild_root.resolve()
    source = copy_frozen_source(rebuild_root)
    rebuild_pdf = rebuild_root / "SGA7I_English_Working_Through_Expose_IX_3_4_20260801.pdf"
    reader, reader_text = inspect_and_compare_pdfs(rebuild_pdf)
    build = verify_build(
        rebuild_root / "SGA7I_English_Working_Through_Expose_IX_3_4_20260801.log",
        rebuild_root / "pass2.console.txt",
        rebuild_root / "pass3.console.txt",
    )
    visual = verify_visuals(args.render_root.resolve())
    write_public_docs(source, reader, build)
    zip_result = write_zip()
    privacy = privacy_scan(reader_text)
    if privacy["occurrences"]:
        raise RuntimeError(f"Privacy/process scan found: {privacy['hits']}")
    validation = {
        "status": "PASS_PUBLIC_WORKING_CHECKPOINT",
        "errors": [],
        "scope": {
            "included": "SGA 7 I Exposes I, II, VI, VII, and VIII complete; Expose IX through section 3.4.0",
            "excluded": "Expose IX Proposition 3.5 and later",
            "source_folios_included": "1-349",
            "source_folios_total": 528,
            "source_folio_coverage_percent": 66.10,
            "continuation": {
                "unit": "Expose IX, Proposition 3.5",
                "authority_file": "source/expose_IX_body.tex",
                "authority_line": 880,
                "scan_index_zero_based": 361,
                "source_folio": 350,
                "physical_pdf_page": 362,
            },
            "complete_sga7i_claim": False,
        },
        "authority": {
            "scan_sha256": AUTHORITY_SCAN_SHA256,
            "working_transcription_master_sha256": TRANSCRIPTION_MASTER_SHA256,
            "scan_redistributed": False,
        },
        "source": source,
        "reader": reader,
        "build": build,
        "visual_qa": visual,
        "zip": zip_result,
        "privacy": privacy,
    }
    write_json(PACKAGE_ROOT / VALIDATION, validation)
    manifest = write_outer_manifest()
    verify_manifest()
    count, total, aggregate = package_snapshot()
    result = {
        "status": validation["status"],
        "errors": [],
        "package_files": count,
        "package_bytes": total,
        "package_aggregate_sha256": aggregate,
        "outer_manifest": manifest,
        "reader": reader,
        "source": source,
        "zip": zip_result,
        "privacy": privacy,
    }
    print(json.dumps(result, indent=2, ensure_ascii=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
