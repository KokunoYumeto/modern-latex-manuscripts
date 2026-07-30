#!/usr/bin/env python3
"""Build the reader-clean SGA3 R25 and SGA4 R8 public packages."""

from __future__ import annotations

import csv
import hashlib
import io
import json
import re
import shutil
import zipfile
from pathlib import Path

from pypdf import PdfReader


REPO_ROOT = Path(__file__).resolve().parent.parent
SGA3_ROOT = Path(
    r"C:\Users\Floris\Documents\interlanguage\03_projects"
    r"\language_management\english_germanic\03_working_translations"
    r"\sga3_english_full_volume_native_cumulative_reader_clean_r25_20260730"
)
SGA4_ROOT = Path(
    r"C:\Users\Floris\Documents\interlanguage\03_projects"
    r"\language_management\english_germanic\03_working_translations"
    r"\sga4_english_reader_clean_r8_20260730"
)
SGA3_PACKAGE = (
    REPO_ROOT
    / "sources"
    / "sga"
    / "sga3-english-reader-clean-r25-no-project-notes-20260730"
)
SGA4_PACKAGE = (
    REPO_ROOT
    / "sources"
    / "sga"
    / "sga4-english-reader-clean-r8-no-project-notes-20260730"
)
SGA3_PDF = SGA3_ROOT / "build_reader_clean_r25" / "02c_SGA3_English_Master.pdf"
SGA4_PDF = (
    SGA4_ROOT
    / "source"
    / "tomes"
    / "SGA4_English_translation_workpass.pdf"
)
SGA3_MASTER = SGA3_ROOT / "02c_SGA3_English_Master.tex"
SGA4_MASTER = (
    SGA4_ROOT
    / "source"
    / "tomes"
    / "SGA4_English_translation_workpass.tex"
)
SGA3_LOG = (
    SGA3_ROOT / "build_reader_clean_r25" / "02c_SGA3_English_Master.log"
)
SGA4_LOG = (
    SGA4_ROOT
    / "source"
    / "tomes"
    / "SGA4_English_translation_workpass.log"
)
ZIP_TIMESTAMP = (2026, 7, 30, 0, 0, 0)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def identity(path: Path) -> dict[str, int | str]:
    return {"bytes": path.stat().st_size, "sha256": sha256_file(path)}


def csv_bytes(rows: list[dict[str, object]], fields: list[str]) -> bytes:
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(
        stream, fieldnames=fields, lineterminator="\n", quoting=csv.QUOTE_ALL
    )
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue().encode("utf-8")


def zip_info(name: str) -> zipfile.ZipInfo:
    info = zipfile.ZipInfo(name, ZIP_TIMESTAMP)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = 0o100644 << 16
    info.create_system = 3
    return info


def safe_relpath(name: str) -> str:
    normalized = name.replace("\\", "/")
    path = Path(normalized)
    if (
        not normalized
        or normalized.startswith("/")
        or re.match(r"^[A-Za-z]:", normalized)
        or ".." in path.parts
    ):
        raise RuntimeError(f"Unsafe archive path: {name}")
    return normalized


def make_source_zip(
    output: Path, members: dict[str, bytes]
) -> dict[str, int | str | bool]:
    clean = {safe_relpath(name): data for name, data in members.items()}
    if len(clean) != len(members):
        raise RuntimeError("Duplicate normalized ZIP member")
    privacy_patterns = (
        rb"C:\\Users\\Floris",
        rb"C:/Users/Floris",
        rb"C:\\IL_GitHub",
        rb"thread[_ -]?id",
        rb"\.codex",
    )
    text_suffixes = {
        ".bib",
        ".cls",
        ".csv",
        ".json",
        ".jsonl",
        ".md",
        ".sty",
        ".tex",
        ".texfrag",
        ".txt",
    }
    privacy_hits = []
    for name, data in clean.items():
        if Path(name).suffix.lower() not in text_suffixes:
            continue
        for pattern in privacy_patterns:
            if re.search(pattern, data, re.IGNORECASE):
                privacy_hits.append({"path": name, "pattern": pattern.decode()})
    if privacy_hits:
        raise RuntimeError(f"Private-path hits in source ZIP: {privacy_hits[:5]}")
    rows = [
        {
            "path": name,
            "bytes": len(data),
            "sha256": sha256_bytes(data),
        }
        for name, data in sorted(clean.items(), key=lambda item: item[0].casefold())
    ]
    manifest = csv_bytes(rows, ["path", "bytes", "sha256"])
    clean["SOURCE_SHA256SUMS.csv"] = manifest
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(
        output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9
    ) as archive:
        for name, data in sorted(clean.items(), key=lambda item: item[0].casefold()):
            archive.writestr(zip_info(name), data)

    with zipfile.ZipFile(output, "r") as archive:
        if archive.testzip() is not None:
            raise RuntimeError(f"CRC failure in {output}")
        infos = archive.infolist()
        if len(infos) != len(clean):
            raise RuntimeError(f"ZIP member boundary mismatch in {output}")
        for info in infos:
            safe_relpath(info.filename)
        replay_rows = list(
            csv.DictReader(
                io.StringIO(
                    archive.read("SOURCE_SHA256SUMS.csv").decode("utf-8"),
                    newline="",
                )
            )
        )
        if len(replay_rows) != len(rows):
            raise RuntimeError(f"ZIP manifest row mismatch in {output}")
        for row in replay_rows:
            data = archive.read(row["path"])
            if (len(data), sha256_bytes(data)) != (
                int(row["bytes"]),
                row["sha256"].upper(),
            ):
                raise RuntimeError(f"ZIP member mismatch: {row['path']}")

    result = identity(output)
    result.update(
        {
            "file_members": len(clean),
            "manifest_rows": len(rows),
            "uncompressed_bytes": sum(len(data) for data in clean.values()),
            "manifest_bytes": len(manifest),
            "manifest_sha256": sha256_bytes(manifest),
            "safe_paths": True,
            "identity_errors": 0,
            "privacy_hits": 0,
        }
    )
    return result


def resolve_object(value):
    try:
        return value.get_object()
    except Exception:
        return value


def pdf_metrics(path: Path, patterns: dict[str, str]) -> dict:
    reader = PdfReader(path)
    hits = {key: [] for key in patterns}
    links = goto = uri = invalid = 0
    raster_pages: list[int] = []
    font_refs: set[tuple[int, int] | str] = set()
    type3 = 0
    a4_pages = 0
    for page_number, page in enumerate(reader.pages, 1):
        width = float(page.mediabox.width)
        height = float(page.mediabox.height)
        if abs(width - 595.276) < 1.0 and abs(height - 841.89) < 1.0:
            a4_pages += 1
        text = page.extract_text() or ""
        for key, pattern in patterns.items():
            if re.search(pattern, text, re.IGNORECASE):
                hits[key].append(page_number)

        resources = resolve_object(page.get("/Resources") or {})
        fonts = resolve_object(resources.get("/Font") or {})
        for ref in fonts.values():
            obj = resolve_object(ref)
            key = (
                (ref.idnum, ref.generation)
                if hasattr(ref, "idnum")
                else repr(obj)
            )
            if key not in font_refs:
                font_refs.add(key)
                if obj.get("/Subtype") == "/Type3":
                    type3 += 1
        xobjects = resolve_object(resources.get("/XObject") or {})
        if any(resolve_object(ref).get("/Subtype") == "/Image" for ref in xobjects.values()):
            raster_pages.append(page_number)

        for annotation_ref in page.get("/Annots") or []:
            annotation = resolve_object(annotation_ref)
            if annotation.get("/Subtype") != "/Link":
                continue
            links += 1
            action = annotation.get("/A")
            destination = annotation.get("/Dest")
            if action is not None:
                action = resolve_object(action)
                kind = action.get("/S")
                if kind == "/GoTo":
                    goto += 1
                elif kind == "/URI":
                    uri += 1
                else:
                    invalid += 1
            elif destination is not None:
                goto += 1
            else:
                invalid += 1

    return {
        **identity(path),
        "pages": len(reader.pages),
        "a4_pages": a4_pages,
        "named_destinations": len(reader.named_destinations),
        "link_annotations": links,
        "internal_goto_actions": goto,
        "uri_actions": uri,
        "invalid_or_other_actions": invalid,
        "font_resources": len(font_refs),
        "type3_fonts": type3,
        "raster_image_pages": raster_pages,
        "hygiene_hits": hits,
        "metadata": {str(k): str(v) for k, v in (reader.metadata or {}).items()},
    }


def log_counts(path: Path) -> dict[str, int | float]:
    text = path.read_text(encoding="utf-8", errors="replace")
    overfull = [
        float(value)
        for value in re.findall(r"Overfull \\hbox \(([\d.]+)pt too wide\)", text)
    ]
    return {
        "hard_errors": len(re.findall(r"^!", text, re.MULTILINE)),
        "undefined_references": len(
            re.findall(r"undefined references", text, re.IGNORECASE)
        ),
        "rerun_warnings": len(
            re.findall(
                r"Label\(s\) may have changed|Rerun to get", text, re.IGNORECASE
            )
        ),
        "overfull_boxes": len(overfull),
        "max_overfull_pt": max(overfull, default=0.0),
        "underfull_boxes": len(
            re.findall(r"Underfull \\hbox", text, re.IGNORECASE)
        ),
    }


def text_file_bytes(path: Path) -> bytes:
    return path.read_bytes()


def sga3_source_members(
    generated_docs: dict[str, bytes],
) -> dict[str, bytes]:
    members: dict[str, bytes] = {}
    for path in sorted((SGA3_ROOT / "inputs").rglob("*")):
        if path.is_file():
            members[path.relative_to(SGA3_ROOT).as_posix()] = path.read_bytes()
    for name in (
        "02c_SGA3_English_Master.tex",
        "README.md",
        "PROVENANCE_AND_RIGHTS.md",
        "READER_HYGIENE_R25.md",
    ):
        members[name] = (SGA3_ROOT / name).read_bytes()
    for name in (
        "BUILD_SUMMARY_PUBLIC.md",
        "FINAL_VISUAL_QA.md",
        "PUBLICATION_READINESS.md",
    ):
        members[name] = generated_docs[name]
    return members


def sga4_source_members(
    generated_docs: dict[str, bytes],
) -> dict[str, bytes]:
    allowed = {".texfrag", ".tex", ".cls", ".sty", ".bib"}
    members: dict[str, bytes] = {}
    source_files = [
        path
        for path in (SGA4_ROOT / "source").rglob("*")
        if path.is_file() and path.suffix.lower() in allowed
    ]
    if len(source_files) != 300:
        raise RuntimeError(f"SGA4 source boundary mismatch: {len(source_files)}")
    for path in sorted(source_files):
        members[path.relative_to(SGA4_ROOT).as_posix()] = path.read_bytes()
    for name in (
        "README_BUILD.md",
        "RIGHTS_AND_PROVENANCE.md",
        "MACHINE_READABLE_INTERNAL_REFERENCES_CONVENTION_v2_EXHAUSTIVE.md",
        "READER_HYGIENE_R8.md",
    ):
        members[name] = (SGA4_ROOT / name).read_bytes()
    for name in (
        "BUILD_SUMMARY_PUBLIC.md",
        "FINAL_VISUAL_QA.md",
        "PUBLICATION_READINESS.md",
    ):
        members[name] = generated_docs[name]
    return members


def write_package_manifest(package: Path) -> dict[str, int | str]:
    rows = []
    for path in sorted(package.iterdir(), key=lambda item: item.name.casefold()):
        if path.is_file() and path.name != "SHA256SUMS.csv":
            rows.append(
                {
                    "path": path.name,
                    "bytes": path.stat().st_size,
                    "sha256": sha256_file(path),
                }
            )
    data = csv_bytes(rows, ["path", "bytes", "sha256"])
    manifest = package / "SHA256SUMS.csv"
    manifest.write_bytes(data)
    for row in rows:
        path = package / str(row["path"])
        if (path.stat().st_size, sha256_file(path)) != (
            int(row["bytes"]),
            str(row["sha256"]),
        ):
            raise RuntimeError(f"Outer package mismatch: {path}")
    return {**identity(manifest), "rows": len(rows)}


def reset_package(path: Path) -> None:
    resolved = path.resolve()
    expected_parent = (REPO_ROOT / "sources" / "sga").resolve()
    if resolved.parent != expected_parent:
        raise RuntimeError(f"Refusing to reset unexpected package path: {resolved}")
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True)


def write_text(path: Path, text: str) -> bytes:
    data = text.strip().replace("\r\n", "\n").encode("utf-8") + b"\n"
    path.write_bytes(data)
    return data


def verify_no_private_paths(package: Path) -> None:
    patterns = (
        rb"C:\\Users\\Floris",
        rb"C:/Users/Floris",
        rb"C:\\IL_GitHub",
        rb"thread[_ -]?id",
        rb"\.codex",
    )
    for path in package.iterdir():
        if path.suffix.lower() not in {".md", ".json", ".csv", ".tex"}:
            continue
        data = path.read_bytes()
        for pattern in patterns:
            if re.search(pattern, data, re.IGNORECASE):
                raise RuntimeError(f"Private-path hit in {path.name}: {pattern!r}")


def build_sga3() -> dict:
    reset_package(SGA3_PACKAGE)
    patterns = {
        "translator_note": r"translator[’']s note",
        "source_note": r"source(?:-reading| notation)? note",
        "source_pdf": r"source PDF",
        "french_source_correction": (
            r"French (?:source|re-?edition) "
            r"(?:prints|writes|says|has|uses|reads|gives|places|omits|calls)"
        ),
        "english_project_choice": (
            r"The English (?:uses|adopts|renders|follows|retains|makes)"
        ),
        "ai_names": r"\b(?:Claude|Codex|ChatGPT|OpenAI|LLM|AI-generated)\b",
        "workflow_status": (
            r"\b(?:workpass|pending (?:fresh )?(?:independent )?review|"
            r"production status|source status|project status)\b"
        ),
    }
    metrics = pdf_metrics(SGA3_PDF, patterns)
    if (
        metrics["pages"] != 1471
        or metrics["a4_pages"] != 1471
        or metrics["named_destinations"] != 9405
        or metrics["internal_goto_actions"] != 4949
        or metrics["invalid_or_other_actions"] != 0
        or metrics["uri_actions"] != 0
        or metrics["raster_image_pages"] != []
        or any(metrics["hygiene_hits"].values())
    ):
        raise RuntimeError("SGA3 PDF gate failed")
    log = log_counts(SGA3_LOG)
    if log["hard_errors"] or log["undefined_references"] or log["rerun_warnings"]:
        raise RuntimeError("SGA3 build log gate failed")
    wrappers = 0
    wrapper_files = 0
    for path in (SGA3_ROOT / "inputs").rglob("*.tex"):
        text = path.read_text(encoding="utf-8", errors="replace")
        count = text.count(r"\SGAArchiveOnly")
        wrappers += count
        wrapper_files += int(count > 0)
    if (wrappers, wrapper_files) != (102, 74):
        raise RuntimeError("SGA3 archive-only wrapper boundary mismatch")

    build_summary = f"""
# Public build summary

- Engine: XeLaTeX
- final auxiliary, contents, and outline state: stable
- hard errors: {log['hard_errors']}
- undefined-reference summaries: {log['undefined_references']}
- rerun warnings: {log['rerun_warnings']}
- cumulative pages: {metrics['pages']} A4
- named destinations: {metrics['named_destinations']}
- internal GoTo actions: {metrics['internal_goto_actions']}
- invalid or external actions: 0
- font resources: {metrics['font_resources']}
- Type3 fonts: {metrics['type3_fonts']}
- raster image pages: 0
- overfull boxes: {log['overfull_boxes']}, maximum {log['max_overfull_pt']:.5f} pt
- underfull boxes: {log['underfull_boxes']}
- archive-only source wrappers: {wrappers} across {wrapper_files} files
- direct-reader project/source/AI hygiene hits: 0
"""
    visual = """
# Final visual QA

The final R25 reader was rendered directly at its title, introduction,
changed-note neighborhoods, and terminal index: pages 1, 13, 14, 283, 428,
799, 1091, and 1471.

The rendered pages show no clipping, overlap, malformed diagram, missing
mathematical content, project-status panel, source locator, translator-process
note, or producer commentary. Source-era editorial notes remain visible.

Contact-sheet SHA-256:
`3A5C0E1BC5556EEA51182124CF42DFA7331A756029E5BDF785A9DEEA3504A628`.
"""
    readiness = """
# Publication readiness

Status: `PASS_READER_CLEAN_R25_NO_PROJECT_NOTES`.

The cumulative source closure, converged build, PDF structure, internal links,
native diagrams, reader-text hygiene scan, and rendered sample pass. The
direct PDF is the preferred reading object. Editable source, provenance, and
the complete archive-only correction apparatus are grouped in one ZIP.

This remains an English scholarly edition open to later textual, reference,
diagram, and accessibility correction. It is not a critical-edition or
rights-clearance claim.
"""
    generated_docs = {
        "BUILD_SUMMARY_PUBLIC.md": build_summary.strip().encode("utf-8") + b"\n",
        "FINAL_VISUAL_QA.md": visual.strip().encode("utf-8") + b"\n",
        "PUBLICATION_READINESS.md": readiness.strip().encode("utf-8") + b"\n",
    }
    reader_out = SGA3_PACKAGE / "00c_SGA3_English_Reader.pdf"
    master_out = SGA3_PACKAGE / "02c_SGA3_English_Master.tex"
    source_zip = SGA3_PACKAGE / "10c_SGA3_English_Source_R25_20260730.zip"
    shutil.copyfile(SGA3_PDF, reader_out)
    shutil.copyfile(SGA3_MASTER, master_out)
    for name, data in generated_docs.items():
        (SGA3_PACKAGE / name).write_bytes(data)
    for name in ("README.md", "PROVENANCE_AND_RIGHTS.md", "READER_HYGIENE_R25.md"):
        shutil.copyfile(SGA3_ROOT / name, SGA3_PACKAGE / name)
    source_metrics = make_source_zip(
        source_zip, sga3_source_members(generated_docs)
    )
    validation = {
        "status": "PASS_READER_CLEAN_R25_NO_PROJECT_NOTES",
        "errors": [],
        "scope": (
            "SGA 3 Introduction, Exposes I-XXVI, Tome-I subject index, "
            "Tome-III mathematical guide, and terminal index"
        ),
        "reader": {"path": reader_out.name, **metrics},
        "master": {"path": master_out.name, **identity(master_out)},
        "source_zip": {"path": source_zip.name, **source_metrics},
        "build": log,
        "reader_hygiene": {
            "archive_only_wrappers": wrappers,
            "files_with_archive_only_wrappers": wrapper_files,
            "project_source_ai_workflow_pattern_hits": 0,
        },
        "privacy": {"outer_private_path_hits": 0},
        "visual_qa": {
            "sample_pages": [1, 13, 14, 283, 428, 799, 1091, 1471],
            "contact_sha256": (
                "3A5C0E1BC5556EEA51182124CF42DFA7331A756029E5BDF785A9DEEA3504A628"
            ),
            "status": "PASS",
        },
    }
    write_text(
        SGA3_PACKAGE / "PACKAGE_VALIDATION.json",
        json.dumps(validation, indent=2, ensure_ascii=False),
    )
    manifest = write_package_manifest(SGA3_PACKAGE)
    verify_no_private_paths(SGA3_PACKAGE)
    return {
        "package": str(SGA3_PACKAGE.relative_to(REPO_ROOT)).replace("\\", "/"),
        "outer_files": len(list(SGA3_PACKAGE.iterdir())),
        "manifest": manifest,
        "reader": identity(reader_out),
        "source_zip": source_metrics,
    }


def build_sga4() -> dict:
    reset_package(SGA4_PACKAGE)
    patterns = {
        "project_frozen_source": r"frozen source",
        "project_source_status": (
            r"\b(?:source status|production status|project status|workpass|"
            r"pending review|source and rights notice)\b"
        ),
        "ai_names": r"\b(?:Claude|Codex|ChatGPT|OpenAI|LLM|AI-generated)\b",
        "translator_note": r"translator[’']s note",
        "source_pdf": r"source PDF",
        "french_source_correction": (
            r"French source "
            r"(?:prints|writes|says|has|uses|reads|gives|places|omits|calls)"
        ),
    }
    metrics = pdf_metrics(SGA4_PDF, patterns)
    if (
        metrics["pages"] != 864
        or metrics["a4_pages"] != 864
        or metrics["named_destinations"] != 9413
        or metrics["internal_goto_actions"] != 6792
        or metrics["uri_actions"] != 2
        or metrics["invalid_or_other_actions"] != 0
        or metrics["raster_image_pages"] != []
        or any(metrics["hygiene_hits"].values())
    ):
        raise RuntimeError("SGA4 PDF gate failed")
    log = log_counts(SGA4_LOG)
    if log["hard_errors"] or log["undefined_references"] or log["rerun_warnings"]:
        raise RuntimeError("SGA4 build log gate failed")
    frozen_wrappers = 0
    for path in (SGA4_ROOT / "source").rglob("*"):
        if path.is_file() and path.suffix.lower() in {".tex", ".texfrag"}:
            text = path.read_text(encoding="utf-8", errors="replace")
            frozen_wrappers += len(
                re.findall(
                    r"\\SGAArchiveOnly\{\\nde\{The frozen source", text
                )
            )
    if frozen_wrappers != 8:
        raise RuntimeError("SGA4 archive-only note boundary mismatch")

    build_summary = f"""
# Public build summary

- Engine: XeLaTeX
- final auxiliary, contents, and outline state: stable
- hard errors: {log['hard_errors']}
- undefined-reference summaries: {log['undefined_references']}
- rerun warnings: {log['rerun_warnings']}
- cumulative pages: {metrics['pages']} A4
- named destinations: {metrics['named_destinations']}
- internal GoTo actions: {metrics['internal_goto_actions']}
- URI actions: {metrics['uri_actions']}
- invalid actions: {metrics['invalid_or_other_actions']}
- font resources: {metrics['font_resources']}
- Type3 fonts: {metrics['type3_fonts']}
- raster image pages: 0
- overfull boxes: {log['overfull_boxes']}, maximum {log['max_overfull_pt']:.5f} pt
- underfull boxes: {log['underfull_boxes']}
- archived project `The frozen source` notes: {frozen_wrappers}
- direct-reader project/source/AI hygiene hits: 0
"""
    visual = """
# Final visual QA

The final R8 reader was rendered directly at its title, contents, all
project-note neighborhoods, the retained source-era Exposé XVIII editorial
note, and terminal bibliography: pages 1, 2, 3, 489, 500, 531, 537, 635,
636, 642, 773, 863, and 864.

No clipping, overlap, black-bar diagram, malformed formula, source-status
page, project note, or missing mathematical content was found. The Exposé
XVIII note beginning `This translation merits some explanation` remains
because the frozen French authority contains the corresponding
`Cette traduction mérite...` editorial note.

Contact-sheet SHA-256:
`DB366E78ED21BDF64BEFE1B52E1640B453B42027CECCB67A40BBE1F0AD2E15BF`.
"""
    readiness = """
# Publication readiness

Status: `PASS_READER_CLEAN_R8_NO_PROJECT_NOTES`.

The complete SGA 4 proper reader (Exposés I-XIX including V bis, excluding
SGA 4 1/2) passes its converged build, PDF structure, link, reader-hygiene,
and rendered-sample gates. The direct PDF presents the mathematics and
source-era editorial apparatus. Project status, rights narration, and
source-gap commentary remain available only in the grouped source ZIP.

This is an English working edition, not a critical edition or a blanket
rights determination.
"""
    generated_docs = {
        "BUILD_SUMMARY_PUBLIC.md": build_summary.strip().encode("utf-8") + b"\n",
        "FINAL_VISUAL_QA.md": visual.strip().encode("utf-8") + b"\n",
        "PUBLICATION_READINESS.md": readiness.strip().encode("utf-8") + b"\n",
    }
    reader_out = SGA4_PACKAGE / "00d_SGA4_English_Reader.pdf"
    master_out = SGA4_PACKAGE / "02d_SGA4_English_Master.tex"
    source_zip = (
        SGA4_PACKAGE
        / "10d_SGA4_English_Proper_ReaderClean_R8_Source_20260730.zip"
    )
    shutil.copyfile(SGA4_PDF, reader_out)
    shutil.copyfile(SGA4_MASTER, master_out)
    for name, data in generated_docs.items():
        (SGA4_PACKAGE / name).write_bytes(data)
    shutil.copyfile(
        SGA4_ROOT / "RIGHTS_AND_PROVENANCE.md",
        SGA4_PACKAGE / "RIGHTS_AND_PROVENANCE.md",
    )
    shutil.copyfile(
        SGA4_ROOT / "READER_HYGIENE_R8.md",
        SGA4_PACKAGE / "READER_HYGIENE_R8.md",
    )
    write_text(
        SGA4_PACKAGE / "README.md",
        """
# SGA 4 proper English reader

This is the reader-clean R8 successor for SGA 4 proper: Exposés I-XIX,
including Exposé V bis and excluding SGA 4 1/2.

The direct PDF presents the mathematics and genuine source-era editorial
apparatus. Project status, source-gap commentary, and rights narration are
retained in the grouped editable-source archive rather than printed in the
reader.

This is an English working edition, not a new critical edition or a blanket
rights clearance. Earlier public versions remain immutable history.
""",
    )
    source_metrics = make_source_zip(
        source_zip, sga4_source_members(generated_docs)
    )
    validation = {
        "status": "PASS_READER_CLEAN_R8_NO_PROJECT_NOTES",
        "errors": [],
        "scope": (
            "SGA 4 proper, Exposes I-XIX including V bis; SGA 4 1/2 excluded"
        ),
        "reader": {"path": reader_out.name, **metrics},
        "master": {"path": master_out.name, **identity(master_out)},
        "source_zip": {"path": source_zip.name, **source_metrics},
        "build": log,
        "reader_hygiene": {
            "archived_project_frozen_source_notes": frozen_wrappers,
            "project_source_ai_workflow_pattern_hits": 0,
            "source_era_nde_notes_preserved": True,
        },
        "privacy": {"outer_private_path_hits": 0},
        "visual_qa": {
            "sample_pages": [
                1,
                2,
                3,
                489,
                500,
                531,
                537,
                635,
                636,
                642,
                773,
                863,
                864,
            ],
            "contact_sha256": (
                "DB366E78ED21BDF64BEFE1B52E1640B453B42027CECCB67A40BBE1F0AD2E15BF"
            ),
            "status": "PASS",
        },
    }
    write_text(
        SGA4_PACKAGE / "PACKAGE_VALIDATION.json",
        json.dumps(validation, indent=2, ensure_ascii=False),
    )
    manifest = write_package_manifest(SGA4_PACKAGE)
    verify_no_private_paths(SGA4_PACKAGE)
    return {
        "package": str(SGA4_PACKAGE.relative_to(REPO_ROOT)).replace("\\", "/"),
        "outer_files": len(list(SGA4_PACKAGE.iterdir())),
        "manifest": manifest,
        "reader": identity(reader_out),
        "master": identity(master_out),
        "source_zip": source_metrics,
    }


def main() -> None:
    results = {"sga3": build_sga3(), "sga4": build_sga4()}
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
