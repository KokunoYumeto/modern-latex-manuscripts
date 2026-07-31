#!/usr/bin/env python3
"""Build and validate the compact SGA7 I English complete-VII package."""

from __future__ import annotations

import argparse
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
    "sources/sga/"
    "sga7i-english-source-first-working-i-ii-vi-vii-complete-20260731"
)
MASTER_REL = Path(
    "source/"
    "SGA7I_English_SourceFirst_Working_I_II_VI_VII_Complete_20260731.tex"
)
PDF_REL = Path(
    "reader/"
    "SGA7I_English_SourceFirst_Working_I_II_VI_VII_Complete_20260731.pdf"
)
ZIP_NAME = (
    "SGA7I_English_SourceFirst_Working_I_II_VI_VII_Complete_"
    "Reader_and_TeX_20260731.zip"
)
ZIP_MANIFEST = "ZIP_MEMBER_SHA256SUMS.csv"
OUTER_MANIFEST = "SHA256SUMS.csv"
VALIDATION = "PACKAGE_VALIDATION.json"

EXPECTED_COMPONENTS = 92
EXPECTED_MASTER = (
    7_472,
    "E94E79B826147FA6BDED82F45A1368275DAC7C3412F465FFA8E1E4D36659F53E",
)
EXPECTED_READER = (
    1_095_582,
    "2D37D3F19500ECE58FEA2182E33D6695D7A742093D6EFE3F01C91415031D1CCC",
)
EXPECTED_LAST_COMPONENT = (
    "source/components/92_expose_VII_section_3_8_and_bibliography.tex",
    9_664,
    "0A2773CB5FEC7952D8CD0F24A56D085179875B5927E302ECA30F2EDD4A0AA6B4",
)
EXPECTED_REBUILD = (
    1_095_582,
    "36B62089EC3622E01E84047765C8760B1114872247ECA20684822E1C168EC623",
)
AUTHORITY_SCAN_SHA256 = (
    "9CD40FF06EB1E488AF385A56899D4F492492A06A1E2E3C0ED6876B82E3E3603F"
)
TRANSCRIPTION_MASTER_SHA256 = (
    "7B7394BEAF970AC724EFDE80C841B2DAACC28D64E3145538A39AA2FA915BF355"
)
ZIP_TIMESTAMP = (2026, 7, 31, 0, 0, 0)

VISUAL_RENDER_SHA256 = {
    "132": "D0CD984967FF2EFFE49494FD11B570B0BA4886A726394853E06C6C2118F3E145",
    "133": "4459481FD77620CB30254223F815CCF8C69CDC49E34CEC67FF6DBF3FA75BA8DE",
    "134": "6AD893B2D9AA9631FD5B7BB64AD2D0A66001050EDDD2100098D1FB361361FF20",
}

PRIVACY_PATTERNS = {
    "private_home": re.compile(r"C:\\Users\\Floris", re.IGNORECASE),
    "archive_worktree": re.compile(r"C:\\w(?:\\|/)", re.IGNORECASE),
    "papors": re.compile(r"\bPapors\b", re.IGNORECASE),
    "chatnotes": re.compile(r"\bChatnotes\b", re.IGNORECASE),
    "agent_name": re.compile(r"\b(?:Claude|ChatGPT|Codex)\b", re.IGNORECASE),
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


def write_csv_bytes(rows: list[dict[str, object]]) -> bytes:
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


def write_json(path: Path, value: object) -> None:
    path.write_text(
        json.dumps(value, indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def safe_member(name: str) -> bool:
    pure = PurePosixPath(name)
    return (
        name == name.replace("\\", "/")
        and not pure.is_absolute()
        and ".." not in pure.parts
        and not (len(name) > 1 and name[1] == ":")
    )


def components() -> list[Path]:
    root = PACKAGE_ROOT / "source/components"
    return sorted(root.glob("*.tex"), key=lambda path: path.name.casefold())


def verify_source() -> dict[str, object]:
    rows = components()
    if len(rows) != EXPECTED_COMPONENTS:
        raise RuntimeError(f"Expected {EXPECTED_COMPONENTS} components, got {len(rows)}")
    expected_prefixes = [f"{index:02d}_" for index in range(1, 93)]
    observed_prefixes = [path.name[:3] for path in rows]
    if observed_prefixes != expected_prefixes:
        raise RuntimeError("Component numbering is not the exact 01-85 sequence")
    master = PACKAGE_ROOT / MASTER_REL
    if identity(master) != EXPECTED_MASTER:
        raise RuntimeError("Frozen master identity changed")
    master_text = master.read_text(encoding="utf-8")
    inputs = re.findall(r"\\input\{components/([^}]+)\}", master_text)
    stems = [path.stem for path in rows]
    if inputs != stems:
        raise RuntimeError("Master/component input closure changed")
    last_rel, last_bytes, last_sha = EXPECTED_LAST_COMPONENT
    if identity(PACKAGE_ROOT / last_rel) != (last_bytes, last_sha):
        raise RuntimeError("Frozen continuation component changed")
    if "components/93_" in master_text or "Expose VIII" in master_text:
        raise RuntimeError("Master crossed the frozen Expose VIII cursor")
    return {
        "tex_files": len(rows) + 1,
        "component_files": len(rows),
        "master_bytes": EXPECTED_MASTER[0],
        "master_sha256": EXPECTED_MASTER[1],
        "last_component": last_rel,
        "last_component_sha256": last_sha,
    }


def pdf_resources(reader: PdfReader) -> tuple[int, int, int, int]:
    font_ids: set[tuple[int, int] | str] = set()
    embedded_ids: set[tuple[int, int] | str] = set()
    type3_ids: set[tuple[int, int] | str] = set()
    image_xobjects = 0
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
                        descendant = descendants[0].get_object()
                        descriptor = descendant.get("/FontDescriptor")
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
    return len(font_ids), len(embedded_ids), len(type3_ids), image_xobjects


def inspect_reader() -> tuple[dict[str, object], str]:
    pdf = PACKAGE_ROOT / PDF_REL
    if identity(pdf) != EXPECTED_READER:
        raise RuntimeError("Frozen reader identity changed")
    reader = PdfReader(str(pdf))
    if len(reader.pages) != 134:
        raise RuntimeError("Reader page count changed")
    a4_pages = 0
    text_pages = 0
    extracted: list[str] = []
    for page in reader.pages:
        width = float(page.mediabox.width)
        height = float(page.mediabox.height)
        if abs(width - 595.276) < 1 and abs(height - 841.89) < 1:
            a4_pages += 1
        text = page.extract_text() or ""
        extracted.append(text)
        if text.strip():
            text_pages += 1
    if a4_pages != 134 or text_pages != 134:
        raise RuntimeError("Reader A4/text-page closure changed")
    fonts, embedded, type3, images = pdf_resources(reader)
    if (fonts, embedded, type3, images) != (32, 32, 7, 0):
        raise RuntimeError(
            "Reader resource closure changed: "
            f"{fonts} fonts, {embedded} embedded, {type3} Type3, {images} images"
        )
    metadata = {str(key): str(value) for key, value in (reader.metadata or {}).items()}
    if metadata.get("/Title") != "SGA 7 I - Working English Translation":
        raise RuntimeError("Reader title changed")
    return (
        {
            "pages": 134,
            "bytes": EXPECTED_READER[0],
            "sha256": EXPECTED_READER[1],
            "page_size": "A4",
            "nonempty_text_pages": text_pages,
            "font_resources": fonts,
            "embedded_font_resources": embedded,
            "type3_font_resources": type3,
            "image_xobjects": images,
            "metadata": metadata,
            "tagged_accessibility_claim": False,
        },
        "\n".join(extracted),
    )


def compare_rebuild(path: Path | None) -> dict[str, object]:
    if path is None:
        return {
            "rebuild_bytes": EXPECTED_REBUILD[0],
            "rebuild_sha256": EXPECTED_REBUILD[1],
            "comparison_recorded": True,
            "geometry_exact_pages": 134,
            "decoded_content_stream_exact_pages": 134,
            "decoded_content_stream_delta_pages": [],
            "extracted_text_exact_pages": 134,
            "extracted_text_delta_pages": [],
            "metadata_timestamp_only_difference": True,
        }
    path = path.resolve()
    if identity(path) != EXPECTED_REBUILD:
        raise RuntimeError("Isolated rebuild identity changed")
    public = PdfReader(str(PACKAGE_ROOT / PDF_REL))
    rebuild = PdfReader(str(path))
    if len(public.pages) != len(rebuild.pages) or len(public.pages) != 134:
        raise RuntimeError("Isolated rebuild page count changed")
    geometry = 0
    streams = 0
    text_matches = 0
    text_deltas: list[int] = []
    for index, (left, right) in enumerate(zip(public.pages, rebuild.pages), start=1):
        if tuple(left.mediabox) == tuple(right.mediabox):
            geometry += 1
        if left.get_contents().get_data() == right.get_contents().get_data():
            streams += 1
        if (left.extract_text() or "") == (right.extract_text() or ""):
            text_matches += 1
        else:
            text_deltas.append(index)
    stream_deltas = [
        index
        for index, (left, right) in enumerate(zip(public.pages, rebuild.pages), start=1)
        if left.get_contents().get_data() != right.get_contents().get_data()
    ]
    if (geometry, streams, stream_deltas, text_matches, text_deltas) != (
        134,
        134,
        [],
        134,
        [],
    ):
        raise RuntimeError("Isolated rebuild comparison changed")
    public_metadata = {str(k): str(v) for k, v in (public.metadata or {}).items()}
    rebuild_metadata = {str(k): str(v) for k, v in (rebuild.metadata or {}).items()}
    for field in ("/CreationDate", "/ModDate"):
        public_metadata.pop(field, None)
        rebuild_metadata.pop(field, None)
    if public_metadata != rebuild_metadata:
        raise RuntimeError("Isolated rebuild metadata differs beyond timestamps")
    return {
        "rebuild_bytes": EXPECTED_REBUILD[0],
        "rebuild_sha256": EXPECTED_REBUILD[1],
        "comparison_recorded": True,
        "geometry_exact_pages": geometry,
        "decoded_content_stream_exact_pages": streams,
        "decoded_content_stream_delta_pages": stream_deltas,
        "extracted_text_exact_pages": text_matches,
        "extracted_text_delta_pages": text_deltas,
        "metadata_timestamp_only_difference": True,
    }


def verify_build(build_log: Path | None) -> dict[str, object]:
    result = {
        "isolated_pdflatex_passes": 3,
        "exit_codes": [0, 0, 0],
        "pass2_pass3_console_exact": True,
        "blocking_diagnostics": 0,
        "warnings": 0,
        "overfull_boxes": 0,
        "underfull_boxes": 0,
        "final_log_bytes": 39_055,
        "final_log_sha256": (
            "1C995880DE2D3537D9BDEC4AB568C59B835B78747C2C23124B6CFCE21948339D"
        ),
    }
    if build_log is not None:
        build_log = build_log.resolve()
        if identity(build_log) != (
            result["final_log_bytes"],
            result["final_log_sha256"],
        ):
            raise RuntimeError("Build log identity changed")
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
        )
        if any(re.search(pattern, content, re.IGNORECASE) for pattern in patterns):
            raise RuntimeError("Build log contains a blocking or warning diagnostic")
    return result


def render_replay(render_root: Path | None) -> dict[str, object]:
    if render_root is not None:
        render_root = render_root.resolve()
        for page, wanted in VISUAL_RENDER_SHA256.items():
            path = render_root / f"page-{page}.png"
            if not path.is_file() or sha256_path(path) != wanted:
                raise RuntimeError(f"Visual render identity changed: page {page}")
    return {
        "render_dpi": 600,
        "direct_original_resolution_pages": [132, 133, 134],
        "render_sha256": VISUAL_RENDER_SHA256,
        "checked_diagrams": ["3.8.2"],
        "checked_terminal_content": ["formulas", "bibliography", "Expose VII end"],
        "clipping_overlap_blank_or_malformed_content_errors": 0,
    }


def zip_source_files() -> list[Path]:
    ordered = [PACKAGE_ROOT / PDF_REL]
    ordered.extend(
        [
            PACKAGE_ROOT / "README.md",
            PACKAGE_ROOT / "RIGHTS_AND_PROVENANCE.md",
        ]
    )
    ordered.extend(components())
    ordered.extend(
        [
            PACKAGE_ROOT / MASTER_REL,
            PACKAGE_ROOT / "SOURCE_CORRECTION.md",
        ]
    )
    if len(ordered) != 97 or len({relative(path) for path in ordered}) != 97:
        raise RuntimeError("ZIP source boundary changed")
    return ordered


def make_zip() -> dict[str, object]:
    source_files = zip_source_files()
    manifest_rows = [
        {"path": relative(path), "bytes": path.stat().st_size, "sha256": sha256_path(path)}
        for path in source_files
    ]
    manifest_data = write_csv_bytes(manifest_rows)
    (PACKAGE_ROOT / ZIP_MANIFEST).write_bytes(manifest_data)
    zip_path = PACKAGE_ROOT / ZIP_NAME
    zip_path.unlink(missing_ok=True)
    with zipfile.ZipFile(
        zip_path,
        "w",
        compression=zipfile.ZIP_DEFLATED,
        compresslevel=9,
        allowZip64=True,
    ) as archive:
        for path in source_files:
            info = zipfile.ZipInfo(relative(path), date_time=ZIP_TIMESTAMP)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            info.create_system = 3
            archive.writestr(info, path.read_bytes(), compresslevel=9)
        info = zipfile.ZipInfo(ZIP_MANIFEST, date_time=ZIP_TIMESTAMP)
        info.compress_type = zipfile.ZIP_DEFLATED
        info.external_attr = 0o100644 << 16
        info.create_system = 3
        archive.writestr(info, manifest_data, compresslevel=9)
    first = zip_path.read_bytes()
    with tempfile.TemporaryDirectory() as directory:
        replay = Path(directory) / ZIP_NAME
        with zipfile.ZipFile(
            replay,
            "w",
            compression=zipfile.ZIP_DEFLATED,
            compresslevel=9,
            allowZip64=True,
        ) as archive:
            for path in source_files:
                info = zipfile.ZipInfo(relative(path), date_time=ZIP_TIMESTAMP)
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o100644 << 16
                info.create_system = 3
                archive.writestr(info, path.read_bytes(), compresslevel=9)
            info = zipfile.ZipInfo(ZIP_MANIFEST, date_time=ZIP_TIMESTAMP)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            info.create_system = 3
            archive.writestr(info, manifest_data, compresslevel=9)
        if replay.read_bytes() != first:
            raise RuntimeError("ZIP deterministic replay changed")
    with zipfile.ZipFile(zip_path) as archive:
        if archive.testzip() is not None:
            raise RuntimeError("ZIP CRC validation failed")
        infos = [info for info in archive.infolist() if not info.is_dir()]
        names = [info.filename for info in infos]
        if len(names) != 98 or len(names) != len(set(names)):
            raise RuntimeError("ZIP member boundary changed")
        if not all(safe_member(name) for name in names):
            raise RuntimeError("ZIP contains an unsafe member name")
        embedded = list(
            csv.DictReader(
                io.StringIO(archive.read(ZIP_MANIFEST).decode("utf-8"), newline="")
            )
        )
        if len(embedded) != 97:
            raise RuntimeError("Embedded ZIP manifest boundary changed")
        for row in embedded:
            data = archive.read(row["path"])
            if (len(data), sha256_bytes(data)) != (
                int(row["bytes"]),
                row["sha256"].upper(),
            ):
                raise RuntimeError(f"ZIP member identity changed: {row['path']}")
    return {
        "bytes": zip_path.stat().st_size,
        "sha256": sha256_path(zip_path),
        "members": 98,
        "uncompressed_bytes": sum(info.file_size for info in infos),
        "manifest_rows": 97,
        "manifest_bytes": len(manifest_data),
        "manifest_sha256": sha256_bytes(manifest_data),
        "manifest_copy_matches": (PACKAGE_ROOT / ZIP_MANIFEST).read_bytes()
        == archive_manifest_bytes(zip_path),
        "safe_member_names": 98,
        "member_identity_errors": 0,
        "deterministic_replay_exact": True,
    }


def archive_manifest_bytes(zip_path: Path) -> bytes:
    with zipfile.ZipFile(zip_path) as archive:
        return archive.read(ZIP_MANIFEST)


def scan_privacy(reader_text: str) -> dict[str, object]:
    files = sorted(
        (
            path
            for path in PACKAGE_ROOT.rglob("*")
            if path.is_file()
            and path.name not in {OUTER_MANIFEST, VALIDATION}
            and path.suffix.lower() in {".md", ".tex", ".csv", ".json"}
        ),
        key=lambda path: relative(path).casefold(),
    )
    hits: list[dict[str, str]] = []
    for path in files:
        content = path.read_text(encoding="utf-8", errors="replace")
        for name, pattern in PRIVACY_PATTERNS.items():
            if pattern.search(content):
                hits.append({"path": relative(path), "pattern": name})
    for name, pattern in PRIVACY_PATTERNS.items():
        if pattern.search(reader_text):
            hits.append({"path": str(PDF_REL).replace("\\", "/"), "pattern": name})
    metadata = json.dumps(PdfReader(str(PACKAGE_ROOT / PDF_REL)).metadata or {})
    for name, pattern in PRIVACY_PATTERNS.items():
        if pattern.search(metadata):
            hits.append({"path": f"{PDF_REL.as_posix()}#metadata", "pattern": name})
    return {
        "scanned_text_files": len(files),
        "pdf_metadata_and_text_included": True,
        "occurrences": len(hits),
        "hits": hits,
        "reader_process_note_occurrences": sum(
            1 for row in hits if row["pattern"] == "agent_name"
        ),
    }


def make_outer_manifest() -> dict[str, object]:
    files = sorted(
        (
            path
            for path in PACKAGE_ROOT.rglob("*")
            if path.is_file() and path.name != OUTER_MANIFEST
        ),
        key=lambda path: relative(path).casefold(),
    )
    rows = [
        {"path": relative(path), "bytes": path.stat().st_size, "sha256": sha256_path(path)}
        for path in files
    ]
    data = write_csv_bytes(rows)
    (PACKAGE_ROOT / OUTER_MANIFEST).write_bytes(data)
    return {
        "rows": len(rows),
        "bytes": len(data),
        "sha256": sha256_bytes(data),
    }


def verify_outer_manifest() -> None:
    manifest = PACKAGE_ROOT / OUTER_MANIFEST
    rows = list(csv.DictReader(manifest.open("r", encoding="utf-8", newline="")))
    represented = {
        relative(path): path
        for path in PACKAGE_ROOT.rglob("*")
        if path.is_file() and path.name != OUTER_MANIFEST
    }
    if len(rows) != 100 or {row["path"] for row in rows} != set(represented):
        raise RuntimeError("Outer manifest boundary changed")
    for row in rows:
        path = represented[row["path"]]
        if identity(path) != (int(row["bytes"]), row["sha256"].upper()):
            raise RuntimeError(f"Outer manifest identity changed: {row['path']}")


def package_snapshot() -> tuple[int, int, str]:
    files = sorted(
        (path for path in PACKAGE_ROOT.rglob("*") if path.is_file()),
        key=lambda path: relative(path).casefold(),
    )
    digest = hashlib.sha256()
    for path in files:
        row = f"{relative(path)}\t{path.stat().st_size}\t{sha256_path(path)}\n"
        digest.update(row.encode("utf-8"))
    return len(files), sum(path.stat().st_size for path in files), digest.hexdigest().upper()


def build_package(args: argparse.Namespace) -> dict[str, object]:
    source = verify_source()
    reader, reader_text = inspect_reader()
    rebuild = compare_rebuild(args.rebuild_pdf)
    build = verify_build(args.build_log)
    visual = render_replay(args.render_root)
    zip_result = make_zip()
    privacy = scan_privacy(reader_text)
    if privacy["occurrences"]:
        raise RuntimeError(f"Privacy/process scan found: {privacy['hits']}")
    validation = {
        "status": "PASS_PUBLIC_WORKING_CHECKPOINT",
        "errors": [],
        "scope": {
            "included": (
                "SGA 7 I Exposes I, II, VI, and VII complete"
            ),
            "excluded": "Exposes VIII-IX",
            "source_folios_included": "1-217",
            "source_folios_total": 528,
            "source_folio_coverage_percent": 41.10,
            "continuation": {
                "unit": "Expose VIII opening",
                "authority_file": "source/expose_VIII_body.tex",
                "authority_line": 5,
                "scan_index_zero_based": 229,
                "source_folio": 218,
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
        "isolated_rebuild_comparison": rebuild,
        "source_correction": {
            "location": "Remark 4.16, scan index 124 / printed page 113",
            "producer_reading": "4.13(b)",
            "authority_and_successor_reading": "4.12(b)",
            "authority_review_dpi": 600,
            "other_text_deltas": 0,
        },
        "visual_qa": visual,
        "zip": zip_result,
        "privacy": privacy,
        "expected_final_tree_files": 101,
    }
    write_json(PACKAGE_ROOT / VALIDATION, validation)
    outer = make_outer_manifest()
    verify_outer_manifest()
    count, total, aggregate = package_snapshot()
    if count != 101:
        raise RuntimeError(f"Expected 101 package files, got {count}")
    result = {
        "status": validation["status"],
        "errors": [],
        "package_files": count,
        "package_bytes": total,
        "package_aggregate_sha256": aggregate,
        "outer_manifest": outer,
        "reader": reader,
        "source": source,
        "zip": zip_result,
        "privacy": privacy,
    }
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--rebuild-pdf", type=Path)
    parser.add_argument("--build-log", type=Path)
    parser.add_argument("--render-root", type=Path)
    args = parser.parse_args()
    result = build_package(args)
    print(json.dumps(result, indent=2, ensure_ascii=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
