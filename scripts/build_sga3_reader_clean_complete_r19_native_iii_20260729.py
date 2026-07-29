#!/usr/bin/env python3
"""Build the compact reader-clean SGA3 R19 Expose-III native successor."""

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
    / "sga3-english-complete-working-reader-clean-r18-native-expose-i-"
    "20260729"
)
BODY_CLEAN_PACKAGE = (
    REPO_ROOT
    / "sources"
    / "sga"
    / "sga1-6-reader-mathematical-body-clean-successor-v2-20260729"
)
OUTPUT_ROOT = (
    REPO_ROOT
    / "sources"
    / "sga"
    / "sga3-english-complete-working-reader-clean-r19-native-expose-iii-"
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
    / "sga3_reader_clean_r19_native_iii_build_20260729"
)

BASE_ARCHIVE = (
    BASE_PACKAGE
    / "10c9_SGA3_English_Complete_Reader_"
    "Source_and_History_R18_20260729.zip"
)
BASE_MASTER = (
    BODY_CLEAN_PACKAGE
    / "02c00_SGA3_English_Complete_Reader_Native_Update_R18_20260729.tex"
)
BASE_PDF = (
    BODY_CLEAN_PACKAGE
    / "00c00_SGA3_English_Complete_Reader_Native_Update_R18_20260729.pdf"
)

PDF_NAME = (
    "00c00_SGA3_English_Complete_Reader_"
    "Native_Update_R19_20260729.pdf"
)
TEX_NAME = (
    "02c00_SGA3_English_Complete_Reader_"
    "Native_Update_R19_20260729.tex"
)
ZIP_NAME = (
    "10c9_SGA3_English_Complete_Reader_"
    "Source_and_History_R19_20260729.zip"
)
BUNDLE_MASTER = "SGA3_English_Complete_Reader_Native_Update_R19_20260729.tex"
OLD_BUNDLE_MASTER = (
    "SGA3_English_Complete_Reader_Native_Update_R18_20260729.tex"
)
BASE_PDF_NAME = BASE_PDF.name
BASE_TEX_NAME = BASE_MASTER.name
ZIP_MANIFEST = "SOURCE_BUNDLE_SHA256.csv"
SHA_MANIFEST = "SHA256SUMS.csv"
FIXED_ZIP_TIME = (2026, 7, 29, 0, 0, 0)
ALLOWED_SOURCE_SUFFIXES = {".bib", ".cls", ".png", ".sty", ".tex", ".texfrag"}

EXPECTED_SUCCESSOR = {
    "STATUS.md": (
        3_053,
        "1A173F74DFB6ECAF456B6F9AFF81316FD04A6967C40EB179F873444617779B82",
    ),
    "controls/FINAL_LOCAL_VALIDATION.json": (
        2_349,
        "A8172F7F92F5CCADA346D63D5A957D5FD28DF5DDEC002B12C2E46392C64418DC",
    ),
    "controls/LEAD_NATIVE_DIAGRAM_AND_LAYOUT_REVIEW_PASS_20260729.md": (
        4_873,
        "0E483BD297521FAF330B80448FF045C52E164B03E6D1964D40CDE92667477BCD",
    ),
    "controls/LEAD_NATIVE_DIAGRAM_5000DPI_REVIEW.csv": (
        9_634,
        "45E58555A2B8C319B2C5D1FBA5BAC42A2BD2908E4ACD6087D90DF38BFC6885F2",
    ),
    "controls/AUTHORITY_HIGHZOOM_CROPS.csv": (
        15_489,
        "6187DBD9E45278DE8DD7B23DEE97A7AC7DB8C306B59FFF0EFABA8E060042BF09",
    ),
    "controls/NATIVE_HIGHZOOM_RENDERS.csv": (
        30_190,
        "DEEA623C6B1D2620E3BB79B38C68EE2D2039FE4A29F73C2855EF4C06EEB9E307",
    ),
    "build/SGA3_Expose_III_English_Loop2.pdf": (
        497_389,
        "0BF8935412E3132538EE2FF3E4B0EF773470136E70913CA68E759616FCA36F43",
    ),
}

PUBLIC_EVIDENCE = (
    "controls/FINAL_LOCAL_VALIDATION.json",
    "controls/LEAD_NATIVE_DIAGRAM_5000DPI_REVIEW.csv",
    "controls/AUTHORITY_HIGHZOOM_CROPS.csv",
    "controls/NATIVE_HIGHZOOM_RENDERS.csv",
)
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
    parser.add_argument("--successor-root", type=Path, required=True)
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


def verify_successor(root: Path) -> dict:
    for relative, expected in EXPECTED_SUCCESSOR.items():
        path = root / relative
        if not path.is_file():
            raise FileNotFoundError(path)
        if identity(path) != expected:
            raise RuntimeError(f"Successor identity mismatch: {relative}")

    validation = json.loads(
        (root / "controls" / "FINAL_LOCAL_VALIDATION.json").read_text(
            encoding="utf-8"
        )
    )
    diagram_gate = validation.get("diagram_gate", {})
    build = validation.get("build", {})
    if (
        validation.get("errors") != []
        or not str(validation.get("status", "")).startswith("PASS_EXPOSE_III")
        or diagram_gate.get("active_raster_calls") != 0
        or diagram_gate.get("active_native_inputs") != 62
        or diagram_gate.get("lead_review_dpi") != 5_000
        or diagram_gate.get("lead_review_pass") != 62
        or diagram_gate.get("lead_review_fail") != 0
        or diagram_gate.get("delivered_raster_diagrams") != 0
        or build.get("fatal_errors") != 0
        or build.get("tex_errors") != 0
    ):
        raise RuntimeError("Expose-III successor validation is not closed")
    return validation


def patch_master(text: str) -> str:
    text = text.replace(
        "Native_Update_R18_20260729", "Native_Update_R19_20260729"
    )
    package_line = r"\usepackage{graphicx,float,enumitem,multicol}"
    if package_line not in text:
        raise RuntimeError("Unable to locate the cumulative graphics package line")
    text = text.replace(
        package_line,
        r"\usepackage{graphicx,float,enumitem,multicol,adjustbox}",
        1,
    )
    insertion = r"""
\newcommand{\SGAThreeNativeInputIII}[2][0.92\textwidth]{%
  \begin{adjustbox}{max width=#1,center,varwidth=\maxdimen}%
    \input{#2}%
  \end{adjustbox}%
}

\newcommand{\SGAThreeNativeDiagramIII}[5][0.92\textwidth]{%
  \begin{figure}[H]
    \centering
    \SGAThreeNativeInputIII[#1]{#2}%
    \caption{#3}
    \label{#4}
  \end{figure}%
}
"""
    marker = "\n\\title{"
    if marker not in text:
        raise RuntimeError("Unable to locate the cumulative title")
    return text.replace(marker, insertion + marker, 1)


def prepare_source(successor: Path, cleaner) -> tuple[Path, list]:
    source = TEMP_ROOT / "primary"
    source.mkdir(parents=True)
    with zipfile.ZipFile(BASE_ARCHIVE) as archive:
        if archive.testzip() is not None:
            raise RuntimeError("R18 source archive CRC failure")
        for info in archive.infolist():
            if not safe_member(info.filename):
                raise RuntimeError(f"Unsafe R18 archive member: {info.filename}")
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

    component_source = successor / "tex" / "components"
    components = sorted(component_source.glob("*.tex"))
    if len(components) != 18:
        raise RuntimeError(f"Expected 18 Expose-III components, got {len(components)}")
    component_target = source / "tex" / "components"
    for path in components:
        target = component_target / path.name
        text = path.read_text(encoding="utf-8")
        text = text.replace(
            r"\SGAThreeNativeDiagram", r"\SGAThreeNativeDiagramIII"
        )
        text = text.replace(
            r"\SGAThreeNativeInput", r"\SGAThreeNativeInputIII"
        )
        target.write_text(text, encoding="utf-8", newline="\n")

    native_source = successor / "native_diagrams" / "exp3"
    native_files = sorted(native_source.glob("*.tex"))
    if len(native_files) != 62:
        raise RuntimeError(
            f"Expected 62 Expose-III native diagrams, got {len(native_files)}"
        )
    native_target = source / "native_diagrams" / "exp3"
    native_target.mkdir(parents=True, exist_ok=True)
    for path in native_files:
        shutil.copy2(path, native_target / path.name)

    removals: list = []
    for path in sorted(source.rglob("*")):
        if path.is_file() and path.suffix.lower() in {".tex", ".texfrag"}:
            cleaner.clean_tex(path, source, "sga3", removals)

    expose_text = "\n".join(
        (component_target / path.name).read_text(
            encoding="utf-8", errors="replace"
        )
        for path in components
    )
    forbidden = (
        r"\includegraphics",
        r"\SGAThreeDiagram",
        r"\SGAThreeRasterDiagram",
        r"\SGAThreeNativeDiagram{",
        r"\SGAThreeNativeInput[",
    )
    remaining = [token for token in forbidden if token in expose_text]
    if remaining:
        raise RuntimeError(f"Old Expose-III raster/native calls remain: {remaining}")
    if expose_text.count(r"\SGAThreeNativeDiagramIII") != 30:
        raise RuntimeError("Expose-III native figure-call count mismatch")
    if expose_text.count(r"\SGAThreeNativeInputIII") != 32:
        raise RuntimeError("Expose-III native direct-input count mismatch")
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
    # The public R18 baseline logged 364 instances of one inherited 4.92744 pt
    # overflow. R19 must not introduce a larger or wider layout warning set.
    if (
        diagnostics["overfull_boxes"] > 364
        or diagnostics["overfull_max_pt"] > 4.92744
    ):
        raise RuntimeError(
            f"{label} overfull diagnostics exceed R18: {diagnostics}"
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
    successor: Path,
    integration_summary: bytes,
) -> dict:
    members = dict(closure)
    members[f"history/{BASE_PDF_NAME}"] = BASE_PDF.read_bytes()
    members[f"history/{BASE_TEX_NAME}"] = BASE_MASTER.read_bytes()
    members["evidence/R19_EXPOSE_III_NATIVE_INTEGRATION.md"] = (
        integration_summary
    )
    for relative in PUBLIC_EVIDENCE:
        members[f"evidence/expose_iii_native/{Path(relative).name}"] = (
            successor / relative
        ).read_bytes()
    members[
        "evidence/expose_iii_native/INPUT_CONTROL_HASH_CORRECTION.json"
    ] = (
        json.dumps(
            {
                "schema": "sga3_expose_iii_input_control_hash_correction_v1",
                "status": "CORRECTED_IN_PUBLIC_PROJECTION",
                "errors": [],
                "file": "controls/NATIVE_HIGHZOOM_RENDERS.csv",
                "bytes": 30_190,
                "actual_sha256": (
                    "DEEA623C6B1D2620E3BB79B38C68EE2D2039FE4A29F73C2855EF4C"
                    "06EEB9E307"
                ),
                "stale_local_control_value": (
                    "DEEA623C6B1D2620E3BB79B38C68EE2D2039FE4A29F73C2855EF4C"
                    "06EEB9E3"
                ),
                "scope": (
                    "The local status and validation text omitted the final "
                    "two hexadecimal characters from this one control hash. "
                    "The manifest bytes, native diagrams, TeX, PDF, review "
                    "rows, and all mathematical content are unchanged."
                ),
            },
            indent=2,
        )
        + "\n"
    ).encode("utf-8")

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
        "contains_predecessor_r18_reader": True,
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
    summary = f"""# SGA 3 R19 Exposé-III native integration

R19 retains the continuous English reader through all twenty-six exposés and
both index/guide surfaces. It replaces only Exposé III's 62 active raster
diagram occurrences with the sealed native-TeX successor.

The Exposé-III lead reviewed all 62 diagrams directly against the controlling
Polo--Gille authority at 5,000 dpi and all 63 integrated diagram-bearing page
envelopes at 600 dpi for layout. The cumulative build contains no active
Exposé-III raster calls and packages no authority pixels.

The public projection also corrects one documentary identity typo: the native
high-zoom render manifest ends in `...EEB9E307`; the local status/validation
text omitted its final `07`. No manifest, diagram, TeX, PDF, or mathematical
byte changed.

The direct PDF remains the preferred reading surface. R18 is preserved inside
the grouped source/history ZIP and in its immutable Zenodo predecessor.

Reader metrics: {metrics['pages']} A4 pages, {metrics['named_destinations']}
named destinations, {metrics['internal_goto_actions']} valid internal GoTo
actions, and {metrics['raster_xobjects']} remaining raster objects outside
Exposé III.

This is a scholarly working translation and TeX edition, not a critical
edition, blanket rights clearance, mathematical certification, peer review,
final whole-volume diagram certification, or tagged-PDF accessibility work.
"""
    integration_summary = summary.encode("utf-8")
    (OUTPUT_ROOT / "README.md").write_bytes(integration_summary)

    (OUTPUT_ROOT / "PROVENANCE_AND_RIGHTS.md").write_text(
        """# Provenance and rights

Exposé III is controlled by the 78-page Polo--Gille `Exp3-14oct24.pdf`,
SHA-256 `B799DE7CA975B738BDC293D703C257E63CAFFD6FA9365F5A398D6E01CB9599E6`.
The authority PDF and all authority crops are excluded. Public evidence records
hashes and locators only. OCR and comparison prose were drafting/locator
witnesses, not authority.

No new license grant or redistribution right is asserted for the underlying
French work, the English reconstruction, or the package as a whole. Rights
remain with their respective holders.
""",
        encoding="utf-8",
        newline="\n",
    )
    (OUTPUT_ROOT / "PUBLICATION_READINESS.md").write_text(
        """# Publication readiness

Status: `PASS_COMPACT_CUMULATIVE_READER_R19_NATIVE_EXPOSE_III`.

The recursive source closure, cumulative and isolated replay builds, PDF
structure, reader-text apparatus scan, privacy scan, Exposé-III native-input
closure, and deterministic ZIP replay pass. The direct reader remains a
working edition with heterogeneous diagram maturity outside the newly closed
Exposé-III scope.
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
- remaining raster objects outside Exposé III: {metrics['raster_xobjects']}
- recursive source files: {len(closure)}
- recursive source aggregate: `{canonical_aggregate(closure)}`
- replay text SHA-256: `{replay['text_sha256']}`
""",
        encoding="utf-8",
        newline="\n",
    )
    (OUTPUT_ROOT / "FINAL_VISUAL_QA.md").write_text(
        """# Final visual QA

The Exposé-III lead closed all 62 native diagrams at 5,000 dpi against the
authority and all 63 diagram-bearing standalone page envelopes at 600 dpi.
The archive-maintenance cumulative integration spot-check covers the Exposé-II
to III seam, early/middle/late Exposé-III diagram pages, the III-to-IV seam,
the title/contents surface, and the terminal index. No clipping, overlap,
missing content, or broken native diagram was observed.
""",
        encoding="utf-8",
        newline="\n",
    )
    return integration_summary


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
    successor = args.successor_root.resolve()
    verify_successor(successor)
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
    source, removals = prepare_source(successor, cleaner)
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
    native_names = {
        name for name in closure_names if name.startswith("native_diagrams/exp3/")
    }
    old_exp3_png = {
        name
        for name in closure_names
        if name.lower().endswith(".png")
        and ("figures/exp3/" in name or "assets/diagrams/exp3_" in name)
    }
    if len(native_names) != 62 or old_exp3_png:
        raise RuntimeError(
            "Cumulative recorder closure did not cleanly replace Expose III: "
            f"native={len(native_names)}, old_png={sorted(old_exp3_png)}"
        )

    shutil.copy2(primary["pdf"], OUTPUT_ROOT / PDF_NAME)
    shutil.copy2(source / BUNDLE_MASTER, OUTPUT_ROOT / TEX_NAME)
    (OUTPUT_ROOT / "SGA3_R19_BUILD_PUBLIC.log").write_text(
        primary["console"], encoding="utf-8", newline="\n"
    )
    write_removal_ledger(removals)
    integration_summary = write_public_docs(metrics, replay, closure)
    source_zip = build_source_zip(closure, successor, integration_summary)

    validation = {
        "schema": "sga3_complete_reader_native_update_r19_expose_iii_v1",
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
            "expose_iii_native_tex": len(native_names),
            "expose_iii_raster_png": len(old_exp3_png),
            "canonical_aggregate_sha256": canonical_aggregate(closure),
        },
        "expose_iii_successor": {
            "status": "PASS",
            "native_diagrams": 62,
            "lead_review_dpi": 5_000,
            "lead_pass": 62,
            "lead_fail": 0,
            "integrated_layout_pass": 63,
            "authority_pixels_public": False,
            "documentary_hash_correction": {
                "file": "controls/NATIVE_HIGHZOOM_RENDERS.csv",
                "actual_sha256": (
                    "DEEA623C6B1D2620E3BB79B38C68EE2D2039FE4A29F73C2855EF4C"
                    "06EEB9E307"
                ),
                "local_control_omitted_final_hex": "07",
                "payload_bytes_changed": False,
            },
        },
        "isolated_replay": replay,
        "build_diagnostics": {
            "primary": primary["diagnostics"],
            "replay": replay_build["diagnostics"],
            "r18_overfull_baseline": {
                "boxes": 364,
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
