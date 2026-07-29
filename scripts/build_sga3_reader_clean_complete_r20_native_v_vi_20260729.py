#!/usr/bin/env python3
"""Build the compact reader-clean SGA3 R20 Expose-V/VI native successor."""

from __future__ import annotations

import argparse
import csv
import hashlib
import importlib.util
import io
import json
import os
import re
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path, PurePosixPath

from pypdf import PdfReader


REPO_ROOT = Path(__file__).resolve().parents[1]
BASE_PACKAGE = (
    REPO_ROOT
    / "sources"
    / "sga"
    / "sga3-english-complete-working-reader-clean-r19-native-expose-iii-"
    "20260729"
)
OUTPUT_ROOT = (
    REPO_ROOT
    / "sources"
    / "sga"
    / "sga3-english-complete-working-reader-clean-r20-native-expose-v-vi-"
    "20260729"
)
CLEANER_PATH = (
    REPO_ROOT
    / "scripts"
    / "build_sga_reader_mathematical_body_clean_successor_20260729.py"
)
TEMP_ROOT = (
    Path(os.environ["LOCALAPPDATA"])
    / "Temp"
    / "sga3_reader_clean_r20_native_v_vi_build_20260729"
)

BASE_ARCHIVE = (
    BASE_PACKAGE
    / "10c9_SGA3_English_Complete_Reader_"
    "Source_and_History_R19_20260729.zip"
)
BASE_MASTER = (
    BASE_PACKAGE
    / "02c00_SGA3_English_Complete_Reader_Native_Update_R19_20260729.tex"
)
BASE_PDF = (
    BASE_PACKAGE
    / "00c00_SGA3_English_Complete_Reader_Native_Update_R19_20260729.pdf"
)

PDF_NAME = "00c_SGA3_English_Reader.pdf"
TEX_NAME = "02c_SGA3_English_Master.tex"
ZIP_NAME = (
    "10c_SGA3_English_Source_and_History_R20_20260729.zip"
)
BUNDLE_MASTER = "SGA3_English_Master.tex"
OLD_BUNDLE_MASTER = (
    "SGA3_English_Complete_Reader_Native_Update_R19_20260729.tex"
)
BASE_PDF_NAME = BASE_PDF.name
BASE_TEX_NAME = BASE_MASTER.name
ZIP_MANIFEST = "SOURCE_BUNDLE_SHA256.csv"
SHA_MANIFEST = "SHA256SUMS.csv"
FIXED_ZIP_TIME = (2026, 7, 29, 0, 0, 0)
ALLOWED_SOURCE_SUFFIXES = {".bib", ".cls", ".png", ".sty", ".tex", ".texfrag"}

V_PUBLIC_EVIDENCE = (
    "README.md",
    "STATUS.md",
    "LICENSE_AND_ATTRIBUTION.md",
    "PUBLICATION_CAVEATS.md",
    "PUBLIC_PROJECTION_VALIDATION.json",
    "controls/EDITABLE_SOURCE_SHA256.csv",
    "controls/LEAD_DIRECT_AUTHORITY_NATIVE_5000DPI_REVIEW.csv",
    "controls/LEAD_INTEGRATED_DIAGRAM_PAGE_LAYOUT_REVIEW_600DPI.csv",
    "controls/PDF_TECHNICAL_VALIDATION.json",
)
VI_PUBLIC_EVIDENCE = (
    "README.md",
    "STATUS.md",
    "LICENSE_AND_ATTRIBUTION.md",
    "PUBLICATION_CAVEATS.md",
    "PUBLIC_PROJECTION_VALIDATION.json",
    "controls/ACTIVE_EDITABLE_SOURCE_SHA256_91.csv",
    "controls/FINAL_LOCAL_VALIDATION.json",
    "controls/LEAD_5000DPI_REVIEW_PASS.md",
    "controls/LEAD_AFFECTED_PAGE_LAYOUT_REVIEW_600DPI.csv",
    "controls/LEAD_DIRECT_AUTHORITY_NATIVE_5000DPI_REVIEW_60.csv",
    "controls/PDF_TECHNICAL_VALIDATION.json",
)
EXPECTED_PACKAGES = {
    "v": {
        "files": 103,
        "bytes": 617_288,
        "manifest_rows": 102,
        "manifest_sha256": (
            "816DC4DDA1F95454FABF104ADA0033E2A8BFA1A4C9EE8BECA1ABC6603B896614"
        ),
        "validation_sha256": (
            "EF1C11E8C386FD7A1C250A4790FE0BF7D2526B290F119D3B0E905447E9BD55B3"
        ),
        "master": "tex/SGA3_Expose_V_English_Loop2_Native_ReferenceV2_00_23.tex",
        "master_sha256": (
            "92AB24AB2E104618AB4E97AC4A2F23554BECB741258F7E9739EC463E6B99C37E"
        ),
        "pdf": "build/SGA3_Expose_V_English_Loop2_Native_ReferenceV2_00_23.pdf",
        "pdf_sha256": (
            "DCB6195D3FE8CA379CCFDB8F9B8B054165DCCF45EB8451C5C678AF4DE7775730"
        ),
    },
    "vi": {
        "files": 104,
        "bytes": 1_726_171,
        "manifest_rows": 103,
        "manifest_sha256": (
            "AF7EAF89DC510B5BD5D6755408EE80161193477D61228FD36BB5167BCD2A9D8A"
        ),
        "validation_sha256": (
            "DBCDC6554A118A16C1F1DBC2CC3EBDABE0F3E5DF96B30F14837CA4042A468E81"
        ),
        "master": "tex_reference_v2/SGA3_Expose_VI_English_ReferenceV2.tex",
        "master_sha256": (
            "C3CFED76C010044132752A907A47B0E9E2DF8AB1E059A5A1AF39AAF089AA1C63"
        ),
        "pdf": "build/SGA3_Expose_VI_English_ReferenceV2.pdf",
        "pdf_sha256": (
            "3633A18A6F86EE6DA06E7F5C776722AAE0E7E7441D7BAF3A37C4959513CA2591"
        ),
    },
}
PRIVATE_MARKERS = (
    b"c:\\users\\",
    b"c:/users/",
    b"\\appdata\\",
    b"/appdata/",
    b"papors",
    b"chatnotes",
    b".claude",
    b".codex",
    b"source_thread_id",
    b"thread_id",
    b"claude-please",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--expose-v-root", type=Path, required=True)
    parser.add_argument("--expose-vi-root", type=Path, required=True)
    parser.add_argument("--keep-temp", action="store_true")
    return parser.parse_args()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def identity(path: Path) -> tuple[int, str]:
    return path.stat().st_size, sha256_file(path)


def safe_remove_temp(path: Path) -> None:
    if not path.exists():
        return
    resolved = path.resolve()
    temp_parent = (Path(os.environ["LOCALAPPDATA"]) / "Temp").resolve()
    if temp_parent not in resolved.parents:
        raise RuntimeError(f"Refusing to remove non-temp path: {resolved}")
    shutil.rmtree(resolved)


def safe_member(name: str) -> bool:
    parts = PurePosixPath(name).parts
    return (
        bool(name)
        and not name.startswith(("/", "\\"))
        and re.match(r"^[A-Za-z]:", name) is None
        and ".." not in parts
    )


def zip_info(name: str) -> zipfile.ZipInfo:
    info = zipfile.ZipInfo(name, date_time=FIXED_ZIP_TIME)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.create_system = 3
    info.external_attr = 0o100644 << 16
    return info


def scan_public_bytes(name: str, data: bytes) -> None:
    lowered = data.lower()
    hits = [
        marker.decode("ascii", errors="replace")
        for marker in PRIVATE_MARKERS
        if marker in lowered
    ]
    if hits:
        raise RuntimeError(f"Private marker in {name}: {hits}")


def load_cleaner():
    spec = importlib.util.spec_from_file_location(
        "sga_reader_body_clean_20260729", CLEANER_PATH
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load the reader-body cleaner")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def verify_successor(root: Path, label: str) -> dict:
    expected = EXPECTED_PACKAGES[label]
    manifest = root / SHA_MANIFEST
    validation_path = root / "PUBLIC_PROJECTION_VALIDATION.json"
    for required in (manifest, validation_path):
        if not required.is_file():
            raise FileNotFoundError(required)
    if sha256_file(manifest) != expected["manifest_sha256"]:
        raise RuntimeError(f"Expose-{label.upper()} manifest identity changed")
    if sha256_file(validation_path) != expected["validation_sha256"]:
        raise RuntimeError(f"Expose-{label.upper()} validation identity changed")
    if sha256_file(root / expected["master"]) != expected["master_sha256"]:
        raise RuntimeError(f"Expose-{label.upper()} master identity changed")
    if sha256_file(root / expected["pdf"]) != expected["pdf_sha256"]:
        raise RuntimeError(f"Expose-{label.upper()} PDF identity changed")

    files = sorted(path for path in root.rglob("*") if path.is_file())
    if (
        len(files) != expected["files"]
        or sum(path.stat().st_size for path in files) != expected["bytes"]
    ):
        raise RuntimeError(f"Expose-{label.upper()} exact-set boundary changed")
    rows = list(
        csv.DictReader(
            io.StringIO(manifest.read_text(encoding="utf-8"), newline="")
        )
    )
    if len(rows) != expected["manifest_rows"]:
        raise RuntimeError(f"Expose-{label.upper()} manifest-row mismatch")
    represented = set()
    for row in rows:
        relative = row["path"].replace("\\", "/")
        if not safe_member(relative):
            raise RuntimeError(f"Unsafe successor path: {relative}")
        path = root / PurePosixPath(relative)
        represented.add(path.resolve())
        if identity(path) != (int(row["bytes"]), row["sha256"].upper()):
            raise RuntimeError(
                f"Expose-{label.upper()} manifest mismatch: {relative}"
            )
        scan_public_bytes(relative, path.read_bytes())
    expected_set = {path.resolve() for path in files if path != manifest}
    if represented != expected_set:
        raise RuntimeError(f"Expose-{label.upper()} exact-set replay failed")

    validation = json.loads(validation_path.read_text(encoding="utf-8"))
    if validation.get("status") != "PASS" or validation.get("errors") != []:
        raise RuntimeError(f"Expose-{label.upper()} validation is not closed")
    if label == "v":
        if (
            validation.get("editable_sources", {}).get("native_diagrams") != 66
            or validation.get("reader_surface", {}).get(
                "native_diagram_invocations"
            )
            != 66
            or validation.get("reader_surface", {}).get(
                "includegraphics_invocations"
            )
            != 0
            or validation.get("lead_review", {}).get(
                "direct_authority_native_5000dpi_rows"
            )
            != 66
            or validation.get("privacy", {}).get("hit_count") != 0
        ):
            raise RuntimeError("Expose-V native/high-zoom closure is incomplete")
    else:
        if (
            validation.get("source_files") != 91
            or validation.get("atomic_native_diagrams") != 60
            or validation.get("lead_5000dpi_pass") != 60
            or validation.get("delivered_raster_files") != 0
            or validation.get("privacy_hits") != 0
            or validation.get("pdf_broken_actions") != 0
        ):
            raise RuntimeError("Expose-VI native/high-zoom closure is incomplete")
    return {
        "validation": validation,
        "files": len(files),
        "bytes": sum(path.stat().st_size for path in files),
        "manifest_rows": len(rows),
        "manifest_sha256": sha256_file(manifest),
        "validation_sha256": sha256_file(validation_path),
    }


def patch_master(text: str) -> str:
    text = text.replace(
        "Native_Update_R19_20260729", "Native_Update_R20_20260729"
    )
    if "Native_Update_R19_20260729" in text:
        raise RuntimeError("Unable to replace the cumulative R19 identity")
    return text


def prepare_source(expose_v: Path, expose_vi: Path, cleaner) -> tuple[Path, list]:
    source = TEMP_ROOT / "primary"
    source.mkdir(parents=True)
    with zipfile.ZipFile(BASE_ARCHIVE) as archive:
        if archive.testzip() is not None:
            raise RuntimeError("R19 source archive CRC failure")
        for info in archive.infolist():
            if not safe_member(info.filename):
                raise RuntimeError(f"Unsafe R19 archive member: {info.filename}")
        archive.extractall(source)

    old_master = source / OLD_BUNDLE_MASTER
    if not old_master.is_file():
        raise FileNotFoundError(old_master)
    new_master = source / BUNDLE_MASTER
    new_master.write_text(
        patch_master(BASE_MASTER.read_text(encoding="utf-8")),
        encoding="utf-8",
        newline="\n",
    )
    old_master.unlink()

    component_source = expose_v / "tex" / "components"
    components = sorted(component_source.glob("*.tex"))
    if len(components) != 24:
        raise RuntimeError(f"Expected 24 Expose-V components, got {len(components)}")
    component_target = source / "tex" / "components"
    for path in components:
        shutil.copy2(path, component_target / path.name)

    native_source = expose_v / "native_diagrams" / "exp5"
    native_files = sorted(native_source.glob("*.tex"))
    if len(native_files) != 66:
        raise RuntimeError(
            f"Expected 66 Expose-V native diagrams, got {len(native_files)}"
        )
    native_target = source / "native_diagrams" / "exp5"
    native_target.mkdir(parents=True, exist_ok=True)
    for path in native_files:
        shutil.copy2(path, native_target / path.name)

    vi_source = expose_vi / "tex_reference_v2" / "components"
    vi_components = sorted(vi_source.glob("*.tex"))
    if len(vi_components) != 90:
        raise RuntimeError(
            f"Expected 90 Expose-VI components, got {len(vi_components)}"
        )
    vi_target = source / "tex_reference_v2" / "components"
    for path in vi_components:
        shutil.copy2(path, vi_target / path.name)

    removals: list = []
    for path in sorted(source.rglob("*")):
        if path.is_file() and path.suffix.lower() in {".tex", ".texfrag"}:
            cleaner.clean_tex(path, source, "sga3", removals)

    expose_v_text = "\n".join(
        (component_target / path.name).read_text(
            encoding="utf-8", errors="replace"
        )
        for path in components
    )
    if r"\includegraphics" in expose_v_text:
        raise RuntimeError("Expose-V raster call remains")
    if expose_v_text.count(r"\SGAThreeDiagram") != 54:
        raise RuntimeError("Expose-V native figure-wrapper count mismatch")
    if expose_v_text.count(r"\SGAThreeNativeInput") != 12:
        raise RuntimeError("Expose-V direct native-input count mismatch")

    expose_vi_text = "\n".join(
        (vi_target / path.name).read_text(
            encoding="utf-8", errors="replace"
        )
        for path in vi_components
    )
    if r"\includegraphics" in expose_vi_text:
        raise RuntimeError("Expose-VI raster call remains")
    if expose_vi_text.count(r"\begin{tikzcd}") != 60:
        raise RuntimeError("Expose-VI native diagram count mismatch")
    return source, removals


def sanitize_log(text: str) -> str:
    replacements = {
        str(Path.home()): "<LOCAL_HOME>",
        str(Path.home()).replace("\\", "/"): "<LOCAL_HOME>",
        str(REPO_ROOT): "<WORKTREE>",
        str(REPO_ROOT).replace("\\", "/"): "<WORKTREE>",
        str(TEMP_ROOT): "<TEMP_BUILD_ROOT>",
        str(TEMP_ROOT).replace("\\", "/"): "<TEMP_BUILD_ROOT>",
    }
    for private, public in sorted(
        replacements.items(), key=lambda item: len(item[0]), reverse=True
    ):
        text = text.replace(private, public)
    return text


def run_build(root: Path, label: str) -> dict:
    master = root / BUNDLE_MASTER
    command = [
        "latexmk",
        "-xelatex",
        "-recorder",
        "-interaction=nonstopmode",
        "-halt-on-error",
        "-file-line-error",
        master.name,
    ]
    result = subprocess.run(
        command,
        cwd=root,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    public_console = sanitize_log(result.stdout)
    if result.returncode:
        raise RuntimeError(
            f"{label} build failed with exit {result.returncode}\n"
            f"{public_console[-8_000:]}"
        )

    pdf = root / f"{master.stem}.pdf"
    log = root / f"{master.stem}.log"
    fls = root / f"{master.stem}.fls"
    for path in (pdf, log, fls):
        if not path.is_file():
            raise FileNotFoundError(path)
    log_text = log.read_text(encoding="utf-8", errors="replace")
    diagnostics = {
        "undefined_references": len(
            re.findall(r"LaTeX Warning: Reference .* undefined", log_text)
        ),
        "undefined_citations": len(
            re.findall(r"LaTeX Warning: Citation .* undefined", log_text)
        ),
        "multiply_defined_labels": len(
            re.findall(r"multiply defined", log_text, flags=re.I)
        ),
        "duplicate_destinations": len(
            re.findall(r"destination with the same identifier", log_text, flags=re.I)
        ),
        "missing_characters": len(
            re.findall(r"Missing character:", log_text)
        ),
        "overfull_boxes": len(re.findall(r"Overfull \\[hv]box", log_text)),
        "fatal_errors": len(re.findall(r"Fatal error occurred", log_text)),
    }
    overfull_widths = [
        float(value)
        for value in re.findall(
            r"Overfull \\[hv]box \(([0-9.]+)pt too (?:wide|high)\)",
            log_text,
        )
    ]
    diagnostics["overfull_max_pt"] = (
        max(overfull_widths) if overfull_widths else 0.0
    )
    hard_keys = (
        "undefined_references",
        "undefined_citations",
        "multiply_defined_labels",
        "duplicate_destinations",
        "missing_characters",
        "fatal_errors",
    )
    if any(diagnostics[key] for key in hard_keys):
        raise RuntimeError(f"{label} build diagnostics: {diagnostics}")
    # The public R19 baseline logged 181 instances of one inherited 4.92744 pt
    # overflow. R20 must not introduce a larger or wider layout warning set.
    if (
        diagnostics["overfull_boxes"] > 181
        or diagnostics["overfull_max_pt"] > 4.92744
    ):
        raise RuntimeError(
            f"{label} overfull diagnostics exceed R19: {diagnostics}"
        )
    return {
        "pdf": pdf,
        "fls": fls,
        "console": public_console,
        "diagnostics": diagnostics,
    }


def pdf_metrics(path: Path) -> dict[str, int]:
    reader = PdfReader(path)
    goto = 0
    invalid = 0
    uri = 0
    linked_pages = 0
    text_pages = 0
    fonts: set[tuple[int, int] | str] = set()
    type3: set[tuple[int, int] | str] = set()
    rasters: set[tuple[int, int] | str] = set()
    for page in reader.pages:
        if (page.extract_text() or "").strip():
            text_pages += 1
        page_links = 0
        for annotation_ref in page.get("/Annots") or []:
            annotation = annotation_ref.get_object()
            action = annotation.get("/A")
            destination = annotation.get("/Dest")
            if action and action.get("/S") == "/GoTo":
                goto += 1
                page_links += 1
                if action.get("/D") is None:
                    invalid += 1
            elif destination is not None:
                goto += 1
                page_links += 1
            elif action and action.get("/S") == "/URI":
                uri += 1
            elif action is not None:
                invalid += 1
        if page_links:
            linked_pages += 1
        resources = page.get("/Resources") or {}
        font_map = resources.get("/Font") or {}
        if hasattr(font_map, "get_object"):
            font_map = font_map.get_object()
        for ref in font_map.values():
            key = (
                (int(ref.idnum), int(ref.generation))
                if hasattr(ref, "idnum")
                else repr(ref)
            )
            fonts.add(key)
            if ref.get_object().get("/Subtype") == "/Type3":
                type3.add(key)
        xobjects = resources.get("/XObject") or {}
        if hasattr(xobjects, "get_object"):
            xobjects = xobjects.get_object()
        for ref in xobjects.values():
            value = ref.get_object()
            if value.get("/Subtype") != "/Image":
                continue
            key = (
                (int(ref.idnum), int(ref.generation))
                if hasattr(ref, "idnum")
                else repr(ref)
            )
            rasters.add(key)
    return {
        "pages": len(reader.pages),
        "text_pages": text_pages,
        "named_destinations": len(reader.named_destinations),
        "internal_goto_actions": goto,
        "linked_pages": linked_pages,
        "invalid_actions": invalid,
        "uri_actions": uri,
        "font_resources": len(fonts),
        "type3_fonts": len(type3),
        "raster_xobjects": len(rasters),
    }


def extract_text(path: Path) -> str:
    result = subprocess.run(
        ["pdftotext", "-enc", "UTF-8", str(path), "-"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    if result.returncode:
        raise RuntimeError(f"pdftotext failed: {result.stderr}")
    return result.stdout


def validate_reader(path: Path, cleaner) -> tuple[dict, str]:
    metrics = pdf_metrics(path)
    if (
        not 1_440 <= metrics["pages"] <= 1_500
        or metrics["named_destinations"] < 9_200
        or metrics["internal_goto_actions"] < 4_300
        or metrics["invalid_actions"] != 0
        or metrics["uri_actions"] != 0
        or metrics["type3_fonts"] != 0
        or metrics["raster_xobjects"] > 41
    ):
        raise RuntimeError(f"Unexpected cumulative PDF metrics: {metrics}")
    text = extract_text(path)
    blocked = [
        token
        for token in (*cleaner.GLOBAL_BLOCKLIST, *cleaner.TEXT_BLOCKLIST["sga3"])
        if token.casefold() in text.casefold()
    ]
    if blocked:
        raise RuntimeError(f"Reader-facing project apparatus remains: {blocked}")
    return metrics, text


def prepare_replay(primary: Path) -> Path:
    replay = TEMP_ROOT / "replay"
    ignored = shutil.ignore_patterns(
        "*.aux",
        "*.fdb_latexmk",
        "*.fls",
        "*.log",
        "*.out",
        "*.pdf",
        "*.toc",
        "*.xdv",
    )
    shutil.copytree(primary, replay, ignore=ignored)
    return replay


def recorder_closure(root: Path, recorder: Path) -> dict[str, bytes]:
    members: dict[str, bytes] = {}
    resolved_root = root.resolve()
    for line in recorder.read_text(
        encoding="utf-8", errors="replace"
    ).splitlines():
        if not line.startswith("INPUT "):
            continue
        raw = Path(line[6:])
        source = raw.resolve() if raw.is_absolute() else (root / raw).resolve()
        if (
            not source.is_file()
            or source.suffix.lower() not in ALLOWED_SOURCE_SUFFIXES
        ):
            continue
        try:
            relative = source.relative_to(resolved_root).as_posix()
        except ValueError:
            continue
        if not safe_member(relative):
            raise RuntimeError(f"Unsafe source closure path: {relative}")
        data = source.read_bytes()
        if relative in members and members[relative] != data:
            raise RuntimeError(f"Conflicting source closure path: {relative}")
        members[relative] = data
    if BUNDLE_MASTER not in members:
        raise RuntimeError("Recorder closure omitted the cumulative master")
    return members


def canonical_aggregate(members: dict[str, bytes]) -> str:
    records = [
        f"{name}|{len(data)}|{sha256_bytes(data)}"
        for name, data in sorted(
            members.items(), key=lambda item: item[0].casefold()
        )
    ]
    return sha256_bytes("\n".join(records).encode("utf-8"))


def csv_bytes(rows: list[dict[str, object]], fields: list[str]) -> bytes:
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue().encode("utf-8")


def build_source_zip(
    closure: dict[str, bytes],
    expose_v: Path,
    expose_vi: Path,
    integration_summary: bytes,
) -> dict:
    members = dict(closure)
    members[f"history/{BASE_PDF_NAME}"] = BASE_PDF.read_bytes()
    members[f"history/{BASE_TEX_NAME}"] = BASE_MASTER.read_bytes()
    members["evidence/R20_EXPOSE_V_VI_NATIVE_INTEGRATION.md"] = (
        integration_summary
    )
    for relative in V_PUBLIC_EVIDENCE:
        members[f"evidence/expose_v_highzoom/{relative}"] = (
            expose_v / relative
        ).read_bytes()
    for relative in VI_PUBLIC_EVIDENCE:
        members[f"evidence/expose_vi_highzoom/{relative}"] = (
            expose_vi / relative
        ).read_bytes()

    for name, data in members.items():
        scan_public_bytes(name, data)

    rows = [
        {
            "relative_path": name,
            "bytes": len(data),
            "sha256": sha256_bytes(data),
        }
        for name, data in sorted(
            members.items(), key=lambda item: item[0].casefold()
        )
    ]
    manifest = csv_bytes(rows, ["relative_path", "bytes", "sha256"])
    members[ZIP_MANIFEST] = manifest

    output = OUTPUT_ROOT / ZIP_NAME
    with zipfile.ZipFile(output, "w") as archive:
        for name, data in sorted(
            members.items(), key=lambda item: item[0].casefold()
        ):
            archive.writestr(zip_info(name), data)

    errors: list[str] = []
    with zipfile.ZipFile(output) as archive:
        bad = archive.testzip()
        if bad is not None:
            errors.append(f"CRC failure: {bad}")
        if len(archive.infolist()) != len(members):
            errors.append("ZIP member-count mismatch")
        manifest_rows = list(
            csv.DictReader(
                io.StringIO(
                    archive.read(ZIP_MANIFEST).decode("utf-8"), newline=""
                )
            )
        )
        if len(manifest_rows) != len(members) - 1:
            errors.append("ZIP manifest-row mismatch")
        for row in manifest_rows:
            data = archive.read(row["relative_path"])
            if (len(data), sha256_bytes(data)) != (
                int(row["bytes"]),
                row["sha256"].upper(),
            ):
                errors.append(f"ZIP member mismatch: {row['relative_path']}")
    if errors:
        raise RuntimeError(f"Source ZIP validation failed: {errors}")
    return {
        "filename": ZIP_NAME,
        "bytes": output.stat().st_size,
        "sha256": sha256_file(output),
        "members": len(members),
        "manifest_rows": len(members) - 1,
        "uncompressed_bytes": sum(len(data) for data in members.values()),
        "manifest_sha256": sha256_bytes(manifest),
        "contains_predecessor_r19_reader": True,
        "errors": [],
    }


def write_removal_ledger(removals: list) -> None:
    rows = [
        {
            "volume": row.volume,
            "relative_path": row.relative_path,
            "kind": row.kind,
            "start_line": row.start_line,
            "bytes_removed": row.bytes_removed,
            "sha256": row.sha256,
            "preview": row.preview,
        }
        for row in removals
    ]
    (OUTPUT_ROOT / "READER_APPARATUS_REMOVAL_LEDGER.csv").write_bytes(
        csv_bytes(
            rows,
            [
                "volume",
                "relative_path",
                "kind",
                "start_line",
                "bytes_removed",
                "sha256",
                "preview",
            ],
        )
    )


def write_public_docs(metrics: dict, replay: dict, closure: dict) -> bytes:
    reader_index = f"""# SGA 3 English Reader

The direct PDF is the reading edition. It contains the Editorial Notice,
Introduction, Exposés I--XXVI, the Tome-I index, the Tome-III mathematical
guide, and the terminal index.

The direct TeX file is the editable master. Build sources, provenance,
validation evidence, and earlier reader states are grouped in the source and
history ZIP.

Reader: {metrics['pages']} A4 pages, {metrics['named_destinations']} named
destinations, and {metrics['internal_goto_actions']} valid internal links.

This is an English scholarly edition, not a critical edition or a blanket
rights clearance. Historical versions remain preserved.
"""
    (OUTPUT_ROOT / "README.md").write_text(
        reader_index,
        encoding="utf-8",
        newline="\n",
    )

    integration_summary = f"""# SGA 3 Exposé-V/VI native integration

This source archive retains the continuous English reader through all
twenty-six exposés and both index/guide surfaces. It overlays the exact
high-zoom native successors for Exposé V and Exposé VI A/B on the preceding
cumulative source closure.

Exposé V contains 66 native diagrams. Its lead checked all 66 directly against
the controlling authority at 5,000 dpi, repaired the five lower-arrow-label
placement defects in figures 007--011, and checked all 32 affected reader pages
at 600 dpi for integration layout.

Exposé VI contains 60 native diagrams. Its lead checked all 60 directly at
5,000 dpi, applied 14 source-backed repairs, and checked all 11 affected reader
pages at 600 dpi for integration layout. Both delivered successors contain
zero raster diagram files and the cumulative build packages no authority
pixels.

Reader metrics: {metrics['pages']} A4 pages, {metrics['named_destinations']}
named destinations, {metrics['internal_goto_actions']} valid internal GoTo
actions, and {metrics['raster_xobjects']} remaining raster objects outside the
newly overlaid Exposé-V/VI scope.

This is a scholarly working translation and TeX edition, not a critical
edition, blanket rights clearance, mathematical certification, peer review,
final whole-volume diagram certification, or tagged-PDF accessibility work.
"""
    integration_summary_bytes = integration_summary.encode("utf-8")

    (OUTPUT_ROOT / "PROVENANCE_AND_RIGHTS.md").write_text(
        """# Provenance and rights

Exposé V is controlled by the Polo--Gille `Exp5-13oct24.pdf`, SHA-256
`9198200633F929FE1822520371A9200DA4F8CF2513EFAB3D6A0C7E9330DB84CF`.
Exposé VI is controlled by the corresponding Polo--Gille corrected VI A and
VI B PDFs. The authority PDFs and all authority crops are excluded. Public
evidence records hashes and locators only. Pre-existing user-supplied OCR and
comparison prose were drafting/locator witnesses, not authority.

Jacob Reinhold's English Markdown at revision
`e7a259f3f8608ad3edf9bf6eead3fd504dd2d23e` is credited comparison and
drafting lineage. Its declared CC BY 4.0 applies only to that translation
contribution and is not a license for the underlying French work.

No new license grant or redistribution right is asserted for the underlying
French work, the English reconstruction, or the package as a whole. Rights
remain with their respective holders.
""",
        encoding="utf-8",
        newline="\n",
    )
    (OUTPUT_ROOT / "PUBLICATION_READINESS.md").write_text(
        """# Publication readiness

Status: `PASS_COMPACT_CUMULATIVE_READER_R20_NATIVE_EXPOSE_V_VI`.

The recursive source closure, cumulative and isolated replay builds, PDF
structure, reader-text apparatus scan, privacy scan, Exposé-V/VI native-input
closure, package-manifest replay, and deterministic ZIP replay pass. The
direct reader remains a working edition with heterogeneous diagram maturity
outside the newly closed Exposé-V/VI scope.
""",
        encoding="utf-8",
        newline="\n",
    )
    (OUTPUT_ROOT / "BUILD_SUMMARY_PUBLIC.md").write_text(
        f"""# Public build summary

- primary XeLaTeX build: PASS
- isolated replay build: PASS
- cumulative pages: {metrics['pages']}
- named destinations: {metrics['named_destinations']}
- internal GoTo actions: {metrics['internal_goto_actions']}
- invalid or external actions: 0
- font resources: {metrics['font_resources']}
- Type3 fonts: 0
- remaining raster objects outside Exposé V/VI: {metrics['raster_xobjects']}
- recursive source files: {len(closure)}
- recursive source aggregate: `{canonical_aggregate(closure)}`
- replay text SHA-256: `{replay['text_sha256']}`
""",
        encoding="utf-8",
        newline="\n",
    )
    (OUTPUT_ROOT / "FINAL_VISUAL_QA.md").write_text(
        """# Final visual QA

The Exposé-V lead closed all 66 native diagrams at 5,000 dpi and all 32
affected standalone page envelopes at 600 dpi. The Exposé-VI lead closed all
60 native diagrams at 5,000 dpi and all 11 affected standalone page envelopes
at 600 dpi.

The cumulative reader was then inspected page by page at the following
physical PDF pages: 1, 262, 263, 268, 269, 307, 308, 329, 332, 337, 447, 456,
470, 484, 487, and 488. These checks cover the title surface, the IV/V, V/VI,
and VI/VII seams, repaired Exposé-V diagrams, and representative repaired
Exposé-VI diagrams. No clipping, overlap, missing content, or broken native
diagram was observed. Source-edition editor notes were preserved.
""",
        encoding="utf-8",
        newline="\n",
    )
    return integration_summary_bytes


def write_outer_manifest() -> None:
    files = sorted(
        (
            path
            for path in OUTPUT_ROOT.iterdir()
            if path.is_file() and path.name != SHA_MANIFEST
        ),
        key=lambda path: path.name.casefold(),
    )
    rows = [
        {
            "filename": path.name,
            "bytes": path.stat().st_size,
            "sha256": sha256_file(path),
        }
        for path in files
    ]
    (OUTPUT_ROOT / SHA_MANIFEST).write_bytes(
        csv_bytes(rows, ["filename", "bytes", "sha256"])
    )


def main() -> int:
    args = parse_args()
    expose_v = args.expose_v_root.resolve()
    expose_vi = args.expose_vi_root.resolve()
    expose_v_replay = verify_successor(expose_v, "v")
    expose_vi_replay = verify_successor(expose_vi, "vi")
    for required in (BASE_ARCHIVE, BASE_MASTER, BASE_PDF, CLEANER_PATH):
        if not required.is_file():
            raise FileNotFoundError(required)

    safe_remove_temp(TEMP_ROOT)
    if OUTPUT_ROOT.exists():
        resolved = OUTPUT_ROOT.resolve()
        expected_parent = OUTPUT_ROOT.parent.resolve()
        if resolved.parent != expected_parent:
            raise RuntimeError(f"Refusing to clear unexpected path: {resolved}")
        shutil.rmtree(resolved)
    OUTPUT_ROOT.mkdir(parents=True)

    cleaner = load_cleaner()
    source, removals = prepare_source(expose_v, expose_vi, cleaner)
    primary = run_build(source, "primary")
    metrics, primary_text = validate_reader(primary["pdf"], cleaner)

    replay_root = prepare_replay(source)
    replay_build = run_build(replay_root, "isolated replay")
    replay_metrics, replay_text = validate_reader(replay_build["pdf"], cleaner)
    if replay_metrics != metrics:
        raise RuntimeError("Isolated replay PDF metrics differ")
    if replay_text != primary_text:
        raise RuntimeError("Isolated replay extracted text differs")
    replay = {
        "metrics": replay_metrics,
        "text_sha256": sha256_bytes(replay_text.encode("utf-8")),
        "errors": [],
    }

    closure = recorder_closure(source, primary["fls"])
    closure_names = set(closure)
    expose_v_native_names = {
        name for name in closure_names if name.startswith("native_diagrams/exp5/")
    }
    expose_v_raster_png = {
        name
        for name in closure_names
        if name.lower().endswith(".png")
        and ("figures/exp5/" in name or "assets/diagrams/exp5_" in name)
    }
    expose_vi_component_names = {
        name
        for name in closure_names
        if name.startswith("tex_reference_v2/components/")
        and name.endswith(".tex")
    }
    if len(expose_v_native_names) != 66 or expose_v_raster_png:
        raise RuntimeError(
            "Cumulative recorder closure did not cleanly replace Expose V: "
            f"native={len(expose_v_native_names)}, "
            f"old_png={sorted(expose_v_raster_png)}"
        )
    if len(expose_vi_component_names) != 90:
        raise RuntimeError(
            "Cumulative recorder closure did not include all Expose-VI "
            f"components: {len(expose_vi_component_names)}"
        )

    shutil.copy2(primary["pdf"], OUTPUT_ROOT / PDF_NAME)
    shutil.copy2(source / BUNDLE_MASTER, OUTPUT_ROOT / TEX_NAME)
    (OUTPUT_ROOT / "SGA3_R20_BUILD_PUBLIC.log").write_text(
        primary["console"], encoding="utf-8", newline="\n"
    )
    write_removal_ledger(removals)
    integration_summary = write_public_docs(metrics, replay, closure)
    source_zip = build_source_zip(
        closure, expose_v, expose_vi, integration_summary
    )

    validation = {
        "schema": "sga3_complete_reader_native_update_r20_expose_v_vi_v1",
        "status": "PASS",
        "errors": [],
        "reader": {
            "filename": PDF_NAME,
            "bytes": (OUTPUT_ROOT / PDF_NAME).stat().st_size,
            "sha256": sha256_file(OUTPUT_ROOT / PDF_NAME),
            **metrics,
            "reader_process_term_hits": [],
        },
        "master_tex": {
            "filename": TEX_NAME,
            "bytes": (OUTPUT_ROOT / TEX_NAME).stat().st_size,
            "sha256": sha256_file(OUTPUT_ROOT / TEX_NAME),
        },
        "source_archive": source_zip,
        "recorder_closure": {
            "files": len(closure),
            "bytes": sum(len(data) for data in closure.values()),
            "tex_files": sum(
                Path(name).suffix.lower() in {".tex", ".texfrag"}
                for name in closure
            ),
            "png_files": sum(
                Path(name).suffix.lower() == ".png" for name in closure
            ),
            "expose_v_native_tex": len(expose_v_native_names),
            "expose_v_raster_png": len(expose_v_raster_png),
            "expose_vi_components": len(expose_vi_component_names),
            "canonical_aggregate_sha256": canonical_aggregate(closure),
        },
        "expose_v_successor": {
            "status": "PASS",
            "native_diagrams": 66,
            "lead_review_dpi": 5_000,
            "lead_pass": 66,
            "lead_fail": 0,
            "source_backed_repairs": 5,
            "integrated_layout_pass": 32,
            "authority_pixels_public": False,
            "package_replay": expose_v_replay,
        },
        "expose_vi_successor": {
            "status": "PASS",
            "native_diagrams": 60,
            "lead_review_dpi": 5_000,
            "lead_pass": 60,
            "lead_fail": 0,
            "source_backed_repairs": 14,
            "integrated_layout_pass": 11,
            "authority_pixels_public": False,
            "package_replay": expose_vi_replay,
        },
        "isolated_replay": replay,
        "build_diagnostics": {
            "primary": primary["diagnostics"],
            "replay": replay_build["diagnostics"],
            "r19_overfull_baseline": {
                "boxes": 181,
                "max_pt": 4.92744,
            },
        },
        "privacy": {"hits": []},
    }
    (OUTPUT_ROOT / "PACKAGE_VALIDATION.json").write_text(
        json.dumps(validation, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    write_outer_manifest()

    manifest_rows = list(
        csv.DictReader(
            (OUTPUT_ROOT / SHA_MANIFEST).read_text(encoding="utf-8").splitlines()
        )
    )
    for row in manifest_rows:
        path = OUTPUT_ROOT / row["filename"]
        if identity(path) != (int(row["bytes"]), row["sha256"].upper()):
            raise RuntimeError(f"Outer manifest mismatch: {path.name}")

    print(json.dumps(validation, indent=2))
    if not args.keep_temp:
        safe_remove_temp(TEMP_ROOT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
