#!/usr/bin/env python3
"""Validate and package the SGA7 II English working checkpoint."""

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
PACKAGE_ROOT = REPO_ROOT / (
    "sources/sga/sga7ii-english-through-expose-xviii-5-8-7-20260801"
)
MASTER_REL = Path(
    "source/SGA7II_English_Through_Expose_XVIII_Corollary_5_8_7_20260801.tex"
)
PDF_REL = Path(
    "reader/SGA7II_English_Through_Expose_XVIII_Corollary_5_8_7_20260801.pdf"
)
ZIP_NAME = (
    "SGA7II_English_Through_Expose_XVIII_Corollary_5_8_7_"
    "Reader_and_TeX_20260801.zip"
)
ZIP_MANIFEST = "ZIP_MEMBER_SHA256SUMS.csv"
OUTER_MANIFEST = "SHA256SUMS.csv"
UPLOAD_MANIFEST = "ZENODO_UPLOAD_MANIFEST.csv"
VALIDATION = "PACKAGE_VALIDATION.json"
EXPECTED_COMPONENTS = 126
EXPECTED_PAGES = 186
AUTHORITY_SHA256 = (
    "FA679DEBFC8ADA3232D7E752A1837FC6CE474488E20A44D7641CF296876E1297"
)
ZIP_TIMESTAMP = (2026, 8, 1, 0, 0, 0)
PUBLIC_PDF_NAME = (
    "00i_SGA7II_English_Through_Expose_XVIII_Corollary_5.8.7_"
    "Working_20260801.pdf"
)
PUBLIC_ZIP_NAME = (
    "10g3_SGA7II_English_Through_Expose_XVIII_Corollary_5.8.7_"
    "Reader_and_TeX_20260801.zip"
)
PRIVACY_PATTERNS = {
    "private_home": re.compile(r"C:\\Users\\Floris", re.IGNORECASE),
    "archive_worktree": re.compile(r"C:\\w(?:\\|/)", re.IGNORECASE),
    "papors": re.compile(r"\bPapors\b", re.IGNORECASE),
    "chatnotes": re.compile(r"\bChatnotes\b", re.IGNORECASE),
    "agent_name": re.compile(
        r"\b(?:Claude|ChatGPT|Codex|OpenAI)\b", re.IGNORECASE
    ),
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


def csv_bytes(rows: list[dict[str, object]], fields: list[str]) -> bytes:
    output = io.StringIO(newline="")
    writer = csv.DictWriter(
        output,
        fieldnames=fields,
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


def components() -> list[Path]:
    paths = list((PACKAGE_ROOT / "source/components").glob("*.tex"))
    return sorted(paths, key=lambda path: int(path.name.split("_", 1)[0]))


def verify_source_closure() -> dict[str, object]:
    master = PACKAGE_ROOT / MASTER_REL
    paths = components()
    if len(paths) != EXPECTED_COMPONENTS:
        raise RuntimeError("Component boundary changed")
    text = master.read_text(encoding="utf-8")
    inputs = re.findall(r"\\input\{components/([^}]+)\}", text)
    if inputs != [path.stem for path in paths]:
        raise RuntimeError("Master/component input closure changed")
    if inputs[-1] != "126_expose_XVIII_section_5_8_6_and_corollary_5_8_7":
        raise RuntimeError("Checkpoint continuation changed")
    if "127_expose" in text:
        raise RuntimeError("Master crossed the frozen cursor")
    return {
        "tex_files": EXPECTED_COMPONENTS + 1,
        "components": EXPECTED_COMPONENTS,
        "master_bytes": master.stat().st_size,
        "master_sha256": sha256_path(master),
        "last_component": relative(paths[-1]),
        "last_component_sha256": sha256_path(paths[-1]),
        "input_closure_exact": True,
    }


def page_stream(page) -> bytes:
    contents = page.get_contents()
    return b"" if contents is None else contents.get_data()


def inspect_resources(reader: PdfReader) -> dict[str, int]:
    fonts: set[tuple[int, int] | str] = set()
    embedded: set[tuple[int, int] | str] = set()
    type3: set[tuple[int, int] | str] = set()
    images = 0
    goto = 0
    uri = 0
    for page in reader.pages:
        resources = page.get("/Resources") or {}
        font_map = resources.get("/Font") if hasattr(resources, "get") else None
        if font_map:
            for name, reference in font_map.get_object().items():
                key = getattr(reference, "idnum", None)
                key = (key, getattr(reference, "generation", 0)) if key else str(name)
                font = reference.get_object()
                fonts.add(key)
                if font.get("/Subtype") == "/Type3":
                    type3.add(key)
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
                        embedded.add(key)
                elif font.get("/Subtype") == "/Type3":
                    embedded.add(key)
        xobjects = resources.get("/XObject") if hasattr(resources, "get") else None
        if xobjects:
            for reference in xobjects.get_object().values():
                if reference.get_object().get("/Subtype") == "/Image":
                    images += 1
        for annotation in page.get("/Annots") or []:
            row = annotation.get_object()
            action = row.get("/A")
            if not action:
                continue
            action = action.get_object()
            if action.get("/S") == "/GoTo":
                goto += 1
            elif action.get("/S") == "/URI":
                uri += 1
    return {
        "font_resources": len(fonts),
        "embedded_font_resources": len(embedded),
        "type3_font_resources": len(type3),
        "image_xobjects": images,
        "goto_actions": goto,
        "uri_actions": uri,
    }


def build_and_compare() -> tuple[dict[str, object], str]:
    engine = shutil.which("xelatex")
    if engine is None:
        raise RuntimeError("xelatex is unavailable")
    public_path = PACKAGE_ROOT / PDF_REL
    public = PdfReader(str(public_path))
    if len(public.pages) != EXPECTED_PAGES:
        raise RuntimeError("Reader page count changed")
    with tempfile.TemporaryDirectory(prefix="sga7ii-c126-") as directory:
        root = Path(directory)
        source = root / "source"
        shutil.copytree(PACKAGE_ROOT / "source", source)
        consoles: list[bytes] = []
        for pass_number in range(1, 4):
            result = subprocess.run(
                [
                    engine,
                    "-interaction=nonstopmode",
                    "-halt-on-error",
                    MASTER_REL.name,
                ],
                cwd=source,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                check=False,
            )
            consoles.append(result.stdout)
            if result.returncode != 0:
                raise RuntimeError(f"XeLaTeX pass {pass_number} failed")
        if consoles[1] != consoles[2]:
            raise RuntimeError("XeLaTeX pass 2 and pass 3 did not converge")
        log = (source / f"{MASTER_REL.stem}.log").read_text(
            encoding="utf-8", errors="replace"
        )
        blockers = (
            r"Undefined control sequence",
            r"! LaTeX Error",
            r"Fatal error",
            r"There were undefined references",
            r"Rerun to get",
            r"Missing character",
            r"Overfull \\hbox",
        )
        found = [pattern for pattern in blockers if re.search(pattern, log, re.I)]
        if found:
            raise RuntimeError(f"Build diagnostics found: {found}")
        underfull_boxes = len(re.findall(r"Underfull \\hbox", log))
        textcircled_warnings = len(
            re.findall(r"Command \\textcircled invalid in math mode", log)
        )
        if underfull_boxes != 2 or textcircled_warnings != 4:
            raise RuntimeError(
                "Unexpected nonblocking diagnostic surface: "
                f"underfull={underfull_boxes}, textcircled={textcircled_warnings}"
            )
        rebuild_path = source / f"{MASTER_REL.stem}.pdf"
        rebuild = PdfReader(str(rebuild_path))
        if len(rebuild.pages) != EXPECTED_PAGES:
            raise RuntimeError("Rebuild page count changed")
        geometry = 0
        streams = 0
        texts = 0
        nonempty = 0
        extracted: list[str] = []
        for original, fresh in zip(public.pages, rebuild.pages, strict=True):
            if tuple(original.mediabox) == tuple(fresh.mediabox):
                geometry += 1
            original_text = original.extract_text() or ""
            fresh_text = fresh.extract_text() or ""
            extracted.append(original_text)
            if original_text.strip():
                nonempty += 1
            if original_text == fresh_text:
                texts += 1
            if page_stream(original) == page_stream(fresh):
                streams += 1
    if (geometry, streams, texts, nonempty) != (
        EXPECTED_PAGES,
        EXPECTED_PAGES,
        EXPECTED_PAGES,
        EXPECTED_PAGES,
    ):
        raise RuntimeError("Fresh rebuild comparison changed")
    resources = inspect_resources(public)
    if resources["image_xobjects"] != 0:
        raise RuntimeError("Reader unexpectedly contains raster page content")
    return (
        {
            "pages": EXPECTED_PAGES,
            "page_size": "A4",
            "bytes": public_path.stat().st_size,
            "sha256": sha256_path(public_path),
            "nonempty_text_pages": nonempty,
            **resources,
            "fresh_xelatex_passes": 3,
            "exit_codes": [0, 0, 0],
            "pass2_pass3_console_exact": True,
            "blocking_diagnostics": 0,
            "underfull_boxes": underfull_boxes,
            "overfull_boxes": 0,
            "textcircled_math_mode_warnings": textcircled_warnings,
            "geometry_exact_pages": geometry,
            "decoded_content_stream_exact_pages": streams,
            "extracted_text_exact_pages": texts,
            "tagged_accessibility_claim": False,
        },
        "\n".join(extracted),
    )


def privacy_scan(reader_text: str) -> dict[str, object]:
    paths = sorted(
        path
        for path in PACKAGE_ROOT.rglob("*")
        if path.is_file()
        and path.suffix.lower() in {".md", ".tex", ".csv", ".json"}
        and path.name not in {OUTER_MANIFEST, VALIDATION, UPLOAD_MANIFEST}
    )
    hits: list[dict[str, str]] = []
    for path in paths:
        text = path.read_text(encoding="utf-8", errors="replace")
        for name, pattern in PRIVACY_PATTERNS.items():
            if pattern.search(text):
                hits.append({"path": relative(path), "pattern": name})
    metadata = json.dumps(PdfReader(str(PACKAGE_ROOT / PDF_REL)).metadata or {})
    for surface, text in (
        (PDF_REL.as_posix(), reader_text),
        (f"{PDF_REL.as_posix()}#metadata", metadata),
    ):
        for name, pattern in PRIVACY_PATTERNS.items():
            if pattern.search(text):
                hits.append({"path": surface, "pattern": name})
    return {
        "scanned_text_files": len(paths),
        "pdf_text_and_metadata_scanned": True,
        "occurrences": len(hits),
        "hits": hits,
    }


def zip_sources() -> list[Path]:
    rows = [PACKAGE_ROOT / PDF_REL, PACKAGE_ROOT / "README.md"]
    rows.extend(components())
    rows.append(PACKAGE_ROOT / MASTER_REL)
    if len(rows) != EXPECTED_COMPONENTS + 3:
        raise RuntimeError("Reader/TeX ZIP source boundary changed")
    return rows


def write_zip() -> dict[str, object]:
    files = zip_sources()
    rows = [
        {
            "path": relative(path),
            "bytes": path.stat().st_size,
            "sha256": sha256_path(path),
        }
        for path in files
    ]
    manifest = csv_bytes(rows, ["path", "bytes", "sha256"])
    (PACKAGE_ROOT / ZIP_MANIFEST).write_bytes(manifest)
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
            archive.writestr(info, manifest, compresslevel=9)

    create(zip_path)
    first = zip_path.read_bytes()
    with tempfile.TemporaryDirectory(prefix="sga7ii-zip-") as directory:
        replay = Path(directory) / ZIP_NAME
        create(replay)
        if replay.read_bytes() != first:
            raise RuntimeError("Reader/TeX ZIP deterministic replay changed")
    with zipfile.ZipFile(zip_path) as archive:
        if archive.testzip() is not None:
            raise RuntimeError("Reader/TeX ZIP CRC validation failed")
        infos = [row for row in archive.infolist() if not row.is_dir()]
        names = [row.filename for row in infos]
        if len(names) != EXPECTED_COMPONENTS + 4 or len(names) != len(set(names)):
            raise RuntimeError("Reader/TeX ZIP member boundary changed")
        if not all(safe_member(name) for name in names):
            raise RuntimeError("Reader/TeX ZIP has unsafe names")
        embedded = list(
            csv.DictReader(io.StringIO(archive.read(ZIP_MANIFEST).decode("utf-8")))
        )
        if len(embedded) != EXPECTED_COMPONENTS + 3:
            raise RuntimeError("Reader/TeX ZIP manifest boundary changed")
        for row in embedded:
            data = archive.read(row["path"])
            if (len(data), sha256_bytes(data)) != (
                int(row["bytes"]),
                row["sha256"].upper(),
            ):
                raise RuntimeError(f"ZIP member mismatch: {row['path']}")
    return {
        "bytes": zip_path.stat().st_size,
        "sha256": sha256_path(zip_path),
        "members": len(infos),
        "uncompressed_bytes": sum(row.file_size for row in infos),
        "manifest_rows": len(embedded),
        "manifest_bytes": len(manifest),
        "manifest_sha256": sha256_bytes(manifest),
        "safe_names": True,
        "crc_errors": 0,
        "member_identity_errors": 0,
        "deterministic_replay_exact": True,
    }


def write_public_docs(source: dict[str, object], reader: dict[str, object]) -> None:
    summary = "\n".join(
        [
            "# Build and QA summary",
            "",
            f"- Editable closure: one master plus {source['components']} referenced components; no missing or unreferenced component.",
            f"- Reader: {reader['pages']} A4 pages, {reader['bytes']:,} bytes, SHA-256 `{reader['sha256']}`.",
            "- Fresh isolated build: three XeLaTeX passes, exits 0/0/0; pass 2 and pass 3 console output byte-identical; no blocking diagnostics.",
            f"- Disclosed nonblocking diagnostics: {reader['underfull_boxes']} inherited underfull boxes, {reader['overfull_boxes']} overfull boxes, and {reader['textcircled_math_mode_warnings']} `\\textcircled`-in-math-mode warnings.",
            f"- Fresh comparison: {reader['pages']}/{reader['pages']} page geometries, decoded content streams, and extracted texts exact.",
            f"- PDF resources: {reader['embedded_font_resources']}/{reader['font_resources']} font resources embedded; {reader['type3_font_resources']} Type 3 fonts; zero image XObjects.",
            f"- Links currently present: {reader['goto_actions']} internal GoTo and {reader['uri_actions']} URI actions. Exhaustive reference closure is not claimed.",
            "- The reader begins directly with mathematical content and has no project-status preface.",
            "",
        ]
    )
    (PACKAGE_ROOT / "BUILD_AND_QA_SUMMARY.md").write_text(
        summary, encoding="utf-8", newline="\n"
    )


def write_upload_manifest(reader: dict[str, object], archive: dict[str, object]) -> None:
    rows = [
        {
            "filename": PUBLIC_PDF_NAME,
            "source_path": PDF_REL.as_posix(),
            "bytes": reader["bytes"],
            "sha256": reader["sha256"],
            "role": "direct_current_progress_reader",
        },
        {
            "filename": PUBLIC_ZIP_NAME,
            "source_path": ZIP_NAME,
            "bytes": archive["bytes"],
            "sha256": archive["sha256"],
            "role": "compact_reader_and_buildable_tex_bundle",
        },
    ]
    (PACKAGE_ROOT / UPLOAD_MANIFEST).write_bytes(
        csv_bytes(rows, ["filename", "source_path", "bytes", "sha256", "role"])
    )


def write_outer_manifest() -> dict[str, object]:
    files = sorted(
        (
            path
            for path in PACKAGE_ROOT.rglob("*")
            if path.is_file() and path.name != OUTER_MANIFEST
        ),
        key=lambda path: relative(path).casefold(),
    )
    rows = [
        {
            "path": relative(path),
            "bytes": path.stat().st_size,
            "sha256": sha256_path(path),
        }
        for path in files
    ]
    data = csv_bytes(rows, ["path", "bytes", "sha256"])
    (PACKAGE_ROOT / OUTER_MANIFEST).write_bytes(data)
    return {"rows": len(rows), "bytes": len(data), "sha256": sha256_bytes(data)}


def verify_outer_manifest() -> None:
    rows = list(
        csv.DictReader(
            (PACKAGE_ROOT / OUTER_MANIFEST).open(
                "r", encoding="utf-8", newline=""
            )
        )
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
    return (
        len(files),
        sum(path.stat().st_size for path in files),
        digest.hexdigest().upper(),
    )


def main() -> int:
    source = verify_source_closure()
    reader, reader_text = build_and_compare()
    write_public_docs(source, reader)
    archive = write_zip()
    write_upload_manifest(reader, archive)
    privacy = privacy_scan(reader_text)
    if privacy["occurrences"]:
        raise RuntimeError(f"Privacy/process scan found: {privacy['hits']}")
    validation = {
        "status": "PASS_PUBLIC_WORKING_CHECKPOINT",
        "errors": [],
        "scope": {
            "included": "SGA 7 II Exposes X-XVII complete and Expose XVIII through Corollary 5.8.7",
            "excluded": "the continuation after Corollary 5.8.7 and Exposes XIX-XXI",
            "continuation": "immediately after Expose XVIII Corollary 5.8.7",
            "complete_sga7ii_claim": False,
        },
        "authority": {
            "source_image_sha256": AUTHORITY_SHA256,
            "source_image_redistributed": False,
        },
        "source": source,
        "reader": reader,
        "zip": archive,
        "privacy": privacy,
    }
    write_json(PACKAGE_ROOT / VALIDATION, validation)
    manifest = write_outer_manifest()
    verify_outer_manifest()
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
        "zip": archive,
        "privacy": privacy,
    }
    print(json.dumps(result, indent=2, ensure_ascii=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
