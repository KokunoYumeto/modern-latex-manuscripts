#!/usr/bin/env python3
"""Build reader-facing SGA3 R26 and SGA6 R10 hygiene successors."""

from __future__ import annotations

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
from pathlib import Path

from pypdf import PdfReader


REPO_ROOT = Path(__file__).resolve().parent.parent
PREVIOUS_SCRIPT = (
    REPO_ROOT / "scripts" / "build_sga_reader_hygiene_r25_r8_packages_20260730.py"
)
SPEC = importlib.util.spec_from_file_location("reader_hygiene_r25", PREVIOUS_SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("Unable to load the established reader-package helpers")
previous = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = previous
SPEC.loader.exec_module(previous)

WORK_ROOT = Path(
    os.environ.get(
        "INTERLANGUAGE_WORKING_TRANSLATIONS",
        Path.home()
        / "Documents"
        / "interlanguage"
        / "03_projects"
        / "language_management"
        / "english_germanic"
        / "03_working_translations",
    )
)
SGA3_R25_ROOT = (
    WORK_ROOT / "sga3_english_full_volume_native_cumulative_reader_clean_r25_20260730"
)
SGA3_R26_ROOT = (
    WORK_ROOT / "sga3_english_full_volume_reader_pure_r26_20260730"
)
SGA6_R9_ROOT = (
    REPO_ROOT
    / "sources"
    / "sga"
    / "sga6-english-cumulative-through-idx702-reference-linked-20260723"
    / "working"
)
SGA6_R10_ROOT = (
    WORK_ROOT / "sga6_english_complete_reader_pure_r10_20260730"
)

SGA3_PACKAGE = (
    REPO_ROOT
    / "sources"
    / "sga"
    / "sga3-english-reader-pure-r26-no-project-notes-20260730"
)
SGA6_PACKAGE = (
    REPO_ROOT
    / "sources"
    / "sga"
    / "sga6-english-reader-pure-r10-no-project-notes-20260730"
)

SGA3_MASTER_NAME = "02c_SGA3_English_Master.tex"
SGA3_BUILD_DIR = "build_reader_pure_r26"
SGA3_PDF_NAME = "00c_SGA3_English_Reader.pdf"
SGA3_ZIP_NAME = "10c_SGA3_English_Source_R26_20260730.zip"

SGA6_MASTER_NAME = "02f_SGA6_English_Master.tex"
SGA6_BUILD_DIR = "build_reader_pure_r10"
SGA6_PDF_NAME = "00f_SGA6_English_Reader.pdf"
SGA6_ZIP_NAME = "10f_SGA6_English_Source_R10_20260730.zip"
SGA6_FRAGMENT_NAME = (
    "SGA6_sourcePDF001_525_English_Inherited_PartiallySourceSynchronized_fragment.tex"
)
ZIP_TIMESTAMP = (2026, 7, 30, 0, 0, 0)


SGA3_COMMAND_MARKERS: tuple[tuple[str, str], ...] = (
    (
        r"VII\tex\components\51_expose_VIIB_section26_lie_algebra_opening_en.tex",
        r"The French authority prints",
    ),
    (
        r"VII\tex\components\56_expose_VIIB_section29_pointed_cocommutative_hopf_algebras_en.tex",
        r"The French prints \(C_0\)",
    ),
    (
        r"VIII\tex\components\06_expose_VIII_section7_part2_and_bibliography.tex",
        "English editor's note: the source prints",
    ),
    (
        r"VIII\tex\components\06_expose_VIII_section7_part2_and_bibliography.tex",
        r"the source prints \(p\operatorname{id}_{G}\)",
    ),
    (
        r"VIII\tex\components\delegated_sections2_4\01_expose_VIII_s2_s4_pp007_013.tex",
        r"The source prints \(\mu_i(k)\)",
    ),
    (
        r"VIII\tex\components\delegated_sections5_6\05_expose_VIII_section5_en.tex",
        r"The source prints \(\ker(\bar\phi)=K'\)",
    ),
    (
        r"VIII\tex\components\delegated_sections5_6\05_expose_VIII_section5_en.tex",
        r"the source prints \(P'\)",
    ),
    (
        r"VIII\tex\components\delegated_sections5_6\05_expose_VIII_section5_en.tex",
        r"the source prints \(J_p=A_0\)",
    ),
    (
        r"VIII\tex\components\delegated_sections5_6\06_expose_VIII_section6_en.tex",
        "the source prints 6.3(b)",
    ),
    (
        r"IX\tex\components\03_expose_IX_sections_4_5.tex",
        r"The source prints \(B''\)",
    ),
    (
        r"IX\tex\components\03_expose_IX_sections_4_5.tex",
        r"The source appends",
    ),
    (
        r"IX\tex\components\03_expose_IX_sections_4_5.tex",
        r"The source prints ``of \(K\)''",
    ),
    (
        r"IX\tex\components\03_expose_IX_sections_4_5.tex",
        r"The source prints the undefined local ring \(B\)",
    ),
    (
        r"IX\tex\components\04_expose_IX_sections_6_7.tex",
        r"The source prints \(C=C\otimes_AA_n\)",
    ),
    (
        r"XI\tex\components\01_expose_XI_opening_through_remark_1_5.tex",
        r"The source prints \(\mathscr O_{X,s}\)",
    ),
    (
        r"XI\tex\components\03_expose_XI_remarks_1_7_1_8.tex",
        r"The source says that \(k''\)",
    ),
    (
        r"XI\tex\components\08_expose_XI_proposition_3_12_and_remark_3_13.tex",
        r"requires the explicit factor",
    ),
    (
        r"XI\tex\components\08_expose_XI_proposition_3_12_and_remark_3_13.tex",
        r"the source marks this final reference",
    ),
    (
        r"XI\tex\components\09_expose_XI_section_4.tex",
        "The printed source says ``affine",
    ),
    (
        r"XI\tex\components\09_expose_XI_section_4.tex",
        r"The printed source abruptly writes",
    ),
    (
        r"XI\tex\components\09_expose_XI_section_4.tex",
        r"The printed source gives only",
    ),
    (
        r"XI\tex\components\09_expose_XI_section_4.tex",
        "The printed source says ``over",
    ),
    (
        r"XIII\source\tex\components\02_expose_XIII_section1_remainder_and_section2.tex",
        r"\SGARefLink{sga3:xiii:lemma:1:1:diagram:01}{The printed diagram}",
    ),
    (
        r"XIII\source\tex\components\02_expose_XIII_section1_remainder_and_section2.tex",
        r"The source reverses this composition",
    ),
    (
        r"XIII\source\tex\components\02_expose_XIII_section1_remainder_and_section2.tex",
        r"The source prints the tautological",
    ),
    (
        r"XIII\source\tex\components\02_expose_XIII_section1_remainder_and_section2.tex",
        r"only the inclusion \(C\subset H\)",
    ),
    (
        r"XIII\source\tex\components\02_expose_XIII_section1_remainder_and_section2.tex",
        r"The source cites the final assertion",
    ),
    (
        r"XIII\source\tex\components\02_expose_XIII_section1_remainder_and_section2.tex",
        r"The source prints ``regular in",
    ),
    (
        r"XIII\source\tex\components\03_expose_XIII_sections3_4.tex",
        r"exponent \(n-r-1\)",
    ),
    (
        r"XIII\source\tex\components\03_expose_XIII_sections3_4.tex",
        r"undefined base field \(\overline K\)",
    ),
    (
        r"XIII\source\tex\components\03_expose_XIII_sections3_4.tex",
        r"the endomorphism here is",
    ),
    (
        r"XIII\source\tex\components\03_expose_XIII_sections3_4.tex",
        r"the inverse image",
    ),
    (
        r"XIV\tex\components\00_expose_XIV_section1_opening_en.tex",
        "The source prints ``1.3''",
    ),
    (
        r"XIV\tex\components\15_expose_XIV_theorem318_corollary319_en.tex",
        r"The re-edition replaces \(\widehat T\)",
    ),
    (
        r"XIV\tex\components\18_expose_XIV_remarks46_through_remarks481_en.tex",
        "There is no item numbered 4.7 in the source",
    ),
    (
        r"XIV\tex\components\19_expose_XIV_proposition49_corollary410_en.tex",
        "the intended reference is 4.9",
    ),
    (
        r"XV\tex\components\03_expose_XV_section3.tex",
        r"The French edition prints \(r^n\)",
    ),
    (
        r"XV\tex\components\09_expose_XV_section8_remainder_and_end.tex",
        r"The final sentence of the printed French",
    ),
)

SGA3_PLAIN_REPLACEMENTS: tuple[tuple[str, str, str], ...] = (
    (
        r"II\tex\components\13_expose_II_s45_s411_lie_structure.tex",
        (
            r"The re-edition prints \(\operatorname{Aut}(F)\) at"
            "\n"
            r"this point, but \(\operatorname{End}(F)\) is the type-correct object"
            "\n"
            r"used by the ensuing endomorphism calculation."
        ),
        (
            r"\SGAArchiveOnly{The re-edition prints "
            r"\(\operatorname{Aut}(F)\) at"
            "\n"
            r"this point, but \(\operatorname{End}(F)\) is the type-correct object"
            "\n"
            r"used by the ensuing endomorphism calculation.}"
        ),
    ),
    (
        r"XXIV\tex\components\13_expose_XXIV_remark631_continuation_through_bibliography_en.tex",
        (
            r"(the French prints \(G\) here; the argument"
            "\n"
            r"and the following sentence require \(K\))"
        ),
        (
            r"\SGAArchiveOnly{(the French prints \(G\) here; the argument"
            "\n"
            r"and the following sentence require \(K\))}"
        ),
    ),
)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def identity(path: Path) -> dict[str, int | str]:
    return {"bytes": path.stat().st_size, "sha256": sha256_file(path)}


def copytree_once(source: Path, target: Path, ignore=None) -> None:
    if target.exists():
        raise RuntimeError(f"No-overwrite target already exists: {target}")
    shutil.copytree(source, target, ignore=ignore)


def command_end(text: str, brace_start: int) -> int:
    depth = 0
    index = brace_start
    while index < len(text):
        if text[index] == "\\":
            index += 2
            continue
        if text[index] == "{":
            depth += 1
        elif text[index] == "}":
            depth -= 1
            if depth == 0:
                return index + 1
        index += 1
    raise RuntimeError("Unbalanced TeX command")


def command_spans(text: str) -> list[tuple[int, int, str]]:
    pattern = re.compile(r"\\(footnote|emph|textit)(?:\[[^\]]*\])?\s*\{")
    spans = []
    for match in pattern.finditer(text):
        spans.append((match.start(), command_end(text, match.end() - 1), match.group(1)))
    return spans


def wrap_command_containing(text: str, marker: str) -> str:
    marker_index = text.find(marker)
    if marker_index < 0:
        raise RuntimeError(f"Missing reader-hygiene marker: {marker}")
    if text.find(marker, marker_index + 1) >= 0:
        raise RuntimeError(f"Non-unique reader-hygiene marker: {marker}")
    enclosing = [
        span
        for span in command_spans(text)
        if span[0] <= marker_index < span[1]
    ]
    if not enclosing:
        raise RuntimeError(f"No enclosing TeX command for marker: {marker}")
    start, end, _ = max(enclosing, key=lambda span: span[0])
    prefix = text[max(0, start - 40) : start]
    if r"\SGAArchiveOnly{" in prefix:
        raise RuntimeError(f"Marker is already archive-only: {marker}")
    return text[:start] + r"\SGAArchiveOnly{" + text[start:end] + "}" + text[end:]


def apply_sga3_hygiene() -> dict[str, int]:
    changed_files: set[Path] = set()
    for relative, marker in SGA3_COMMAND_MARKERS:
        path = SGA3_R26_ROOT / "inputs" / Path(relative)
        text = path.read_text(encoding="utf-8")
        updated = wrap_command_containing(text, marker)
        path.write_text(updated, encoding="utf-8", newline="\n")
        changed_files.add(path)
    for relative, old, new in SGA3_PLAIN_REPLACEMENTS:
        path = SGA3_R26_ROOT / "inputs" / Path(relative)
        text = path.read_text(encoding="utf-8")
        if text.count(old) != 1:
            raise RuntimeError(f"Plain reader-hygiene marker mismatch: {relative}")
        path.write_text(text.replace(old, new), encoding="utf-8", newline="\n")
        changed_files.add(path)
    wrappers = 0
    wrapper_files = 0
    for path in (SGA3_R26_ROOT / "inputs").rglob("*.tex"):
        text = path.read_text(encoding="utf-8", errors="replace")
        count = text.count(r"\SGAArchiveOnly")
        wrappers += count
        wrapper_files += int(count > 0)
    return {
        "new_wrappers": len(SGA3_COMMAND_MARKERS) + len(SGA3_PLAIN_REPLACEMENTS),
        "changed_files": len(changed_files),
        "total_wrappers": wrappers,
        "wrapper_files": wrapper_files,
    }


def apply_sga6_hygiene() -> dict[str, int]:
    fragment = SGA6_R10_ROOT / SGA6_FRAGMENT_NAME
    master = SGA6_R10_ROOT / SGA6_MASTER_NAME
    tail = SGA6_R10_ROOT / "SGA6_idx532_702_and_backmatter_English_Synchronized_body.tex"
    terminal = (
        SGA6_R10_ROOT
        / "fragments"
        / "SGA6_XIV_idx693_702_English_SourceChecked_body.tex"
    )
    history = SGA6_R10_ROOT / "history"
    history.mkdir()
    history_copy = history / (
        "SGA6_sourcePDF001_525_English_R9_with_project_source_prose.tex"
    )
    shutil.copyfile(fragment, history_copy)
    text = fragment.read_text(encoding="utf-8")
    replacements = (
        (
            "Under the local Koszul hypotheses stated in the source, one has",
            "Under the local Koszul hypotheses of this proposition, one has",
        ),
        (
            (
                " The source records the standard consequences for the operation "
                "of direct image under a regular immersion."
            ),
            "",
        ),
        (
            "where the two displayed squares are those denoted (1) and (2) in the source.",
            (
                "where the left and right displayed squares are denoted "
                "(1) and (2), respectively."
            ),
        ),
    )
    for old, new in replacements:
        if text.count(old) != 1:
            raise RuntimeError(f"SGA6 reader-hygiene marker mismatch: {old}")
        text = text.replace(old, new)
    fragment.write_text(text, encoding="utf-8", newline="\n")

    master_text = master.read_text(encoding="utf-8")
    macro_anchor = r"\providecommand{\Gr}{\operatorname{G}}"
    if master_text.count(macro_anchor) != 1:
        raise RuntimeError("SGA6 archive-only macro anchor mismatch")
    master_text = master_text.replace(
        macro_anchor,
        macro_anchor + "\n" + r"\long\def\SGAArchiveOnly#1{}",
    )
    master.write_text(master_text, encoding="utf-8", newline="\n")

    terminal_text = terminal.read_text(encoding="utf-8")
    terminal_text = wrap_command_containing(
        terminal_text,
        "The printed French note",
    )
    terminal.write_text(terminal_text, encoding="utf-8", newline="\n")

    tail_text = tail.read_text(encoding="utf-8")
    editorial_input = (
        r"\input{fragments/SGA6_XIV_idx685_702_Editorial_Source_Notes.tex}"
    )
    if tail_text.count(editorial_input) != 1:
        raise RuntimeError("SGA6 terminal source-notes input mismatch")
    tail_text = tail_text.replace(
        editorial_input,
        r"\SGAArchiveOnly{" + editorial_input + "}",
    )
    tail.write_text(tail_text, encoding="utf-8", newline="\n")
    return {"replacements": len(replacements) + 2, "history_files": 1}


def run_latex(
    root: Path,
    master: str,
    build_dir_name: str,
    engine: str,
    passes: int = 4,
) -> Path:
    build_dir = root / build_dir_name
    build_dir.mkdir()
    for _ in range(passes):
        result = subprocess.run(
            [
                engine,
                "-interaction=nonstopmode",
                "-halt-on-error",
                f"-output-directory={build_dir}",
                master,
            ],
            cwd=root,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
        if result.returncode != 0:
            tail = "\n".join((result.stdout + result.stderr).splitlines()[-80:])
            raise RuntimeError(f"{engine} failed for {master}:\n{tail}")
    return build_dir


def measure_sga3_hygiene() -> dict[str, int]:
    wrappers = 0
    wrapper_files = 0
    for path in (SGA3_R26_ROOT / "inputs").rglob("*.tex"):
        text = path.read_text(encoding="utf-8", errors="replace")
        count = text.count(r"\SGAArchiveOnly")
        wrappers += count
        wrapper_files += int(count > 0)
    return {
        "new_wrappers": len(SGA3_COMMAND_MARKERS) + len(SGA3_PLAIN_REPLACEMENTS),
        "changed_files": len(
            {relative for relative, _ in SGA3_COMMAND_MARKERS}
            | {relative for relative, _, _ in SGA3_PLAIN_REPLACEMENTS}
        ),
        "total_wrappers": wrappers,
        "wrapper_files": wrapper_files,
    }


def measure_sga6_hygiene() -> dict[str, int]:
    fragment = SGA6_R10_ROOT / SGA6_FRAGMENT_NAME
    master = SGA6_R10_ROOT / SGA6_MASTER_NAME
    tail = SGA6_R10_ROOT / "SGA6_idx532_702_and_backmatter_English_Synchronized_body.tex"
    terminal = (
        SGA6_R10_ROOT
        / "fragments"
        / "SGA6_XIV_idx693_702_English_SourceChecked_body.tex"
    )
    text = fragment.read_text(encoding="utf-8")
    forbidden = (
        "Under the local Koszul hypotheses stated in the source",
        "The source records the standard consequences",
        "those denoted (1) and (2) in the source",
    )
    if any(value in text for value in forbidden):
        raise RuntimeError("SGA6 successor still contains superseded source prose")
    if not (SGA6_R10_ROOT / "history").is_dir():
        raise RuntimeError("SGA6 source-history copy is missing")
    if r"\long\def\SGAArchiveOnly#1{}" not in master.read_text(encoding="utf-8"):
        raise RuntimeError("SGA6 archive-only macro is missing")
    if (
        r"\SGAArchiveOnly{\input{fragments/SGA6_XIV_idx685_702_Editorial_Source_Notes.tex}}"
        not in tail.read_text(encoding="utf-8")
    ):
        raise RuntimeError("SGA6 terminal source-note input is not archived")
    terminal_text = terminal.read_text(encoding="utf-8")
    if (
        r"\SGAArchiveOnly{\footnote{\textbf{Source note"
        not in terminal_text
    ):
        raise RuntimeError("SGA6 terminal correction footnote is not archived")
    return {"replacements": 5, "history_files": 1}


def extracted_hygiene_hits(path: Path) -> dict[str, list[dict[str, str | int]]]:
    patterns = {
        "ai_or_workflow": re.compile(
            r"(?i)\b(?:Claude|Codex|ChatGPT|OpenAI|LLM|AI-generated|workpass|"
            r"pending (?:fresh )?(?:independent )?review|production status|"
            r"source status|project status)\b"
        ),
        "project_note_label": re.compile(
            r"(?i)(?:translator[’']s note|source-reading note|source note|"
            r"English editor[’']s note|source PDF)"
        ),
        "project_source_sentence": re.compile(
            r"(?i)(?:\[the source\b|the French authority\b|"
            r"the printed source\b|the final sentence of the printed French\b|"
            r"the re-edition prints \b|the source "
            r"(?:prints?|says?|gives?|appends?|cites?|reverses?|marks?|records?)\b)"
        ),
    }
    hits = {name: [] for name in patterns}
    reader = PdfReader(path)
    for page_number, page in enumerate(reader.pages, 1):
        for line in (page.extract_text() or "").splitlines():
            for name, pattern in patterns.items():
                if pattern.search(line):
                    hits[name].append(
                        {"page": page_number, "text": " ".join(line.split())}
                    )
    return hits


def pdf_metrics(path: Path) -> dict:
    reader = PdfReader(path)
    links = goto = uri = invalid = 0
    raster_pages = []
    for page_number, page in enumerate(reader.pages, 1):
        resources = previous.resolve_object(page.get("/Resources") or {})
        xobjects = previous.resolve_object(resources.get("/XObject") or {})
        if any(
            previous.resolve_object(ref).get("/Subtype") == "/Image"
            for ref in xobjects.values()
        ):
            raster_pages.append(page_number)
        for ref in page.get("/Annots") or []:
            annotation = previous.resolve_object(ref)
            if annotation.get("/Subtype") != "/Link":
                continue
            links += 1
            action = annotation.get("/A")
            destination = annotation.get("/Dest")
            if action is not None:
                action = previous.resolve_object(action)
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
        "named_destinations": len(reader.named_destinations),
        "link_annotations": links,
        "internal_goto_actions": goto,
        "uri_actions": uri,
        "invalid_or_other_actions": invalid,
        "raster_image_pages": raster_pages,
        "hygiene_hits": extracted_hygiene_hits(path),
    }


def text_bytes(text: str) -> bytes:
    return text.strip().replace("\r\n", "\n").encode("utf-8") + b"\n"


def source_members(root: Path, generated_docs: dict[str, bytes]) -> dict[str, bytes]:
    excluded_roots = {SGA3_BUILD_DIR, SGA6_BUILD_DIR}
    members: dict[str, bytes] = {}
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        relative = path.relative_to(root)
        if relative.parts and relative.parts[0] in excluded_roots:
            continue
        if path.suffix.lower() in {".aux", ".log", ".out", ".toc", ".pdf"}:
            continue
        members[relative.as_posix()] = path.read_bytes()
    members.update(generated_docs)
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
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(
        stream,
        fieldnames=["path", "bytes", "sha256"],
        lineterminator="\n",
        quoting=csv.QUOTE_ALL,
    )
    writer.writeheader()
    writer.writerows(rows)
    manifest = package / "SHA256SUMS.csv"
    manifest.write_bytes(stream.getvalue().encode("utf-8"))
    return {**identity(manifest), "rows": len(rows)}


def reset_package(path: Path) -> None:
    expected_parent = (REPO_ROOT / "sources" / "sga").resolve()
    if path.resolve().parent != expected_parent:
        raise RuntimeError(f"Unexpected package path: {path}")
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True)


def verify_no_private_paths(package: Path) -> None:
    patterns = (
        rb"C:\\Users\\Floris",
        rb"C:/Users/Floris",
        rb"C:\\IL_GitHub",
        rb"thread[_ -]?id",
        rb"\.codex",
    )
    text_suffixes = {".md", ".json", ".csv", ".tex", ".txt"}
    for path in package.iterdir():
        if path.suffix.lower() not in text_suffixes:
            continue
        data = path.read_bytes()
        for pattern in patterns:
            if re.search(pattern, data, re.IGNORECASE):
                raise RuntimeError(f"Private-path hit in {path}: {pattern!r}")


def build_sga3_package(hygiene: dict[str, int]) -> dict:
    reset_package(SGA3_PACKAGE)
    build_dir = SGA3_R26_ROOT / SGA3_BUILD_DIR
    built_pdf = build_dir / "02c_SGA3_English_Master.pdf"
    build_log = build_dir / "02c_SGA3_English_Master.log"
    metrics = pdf_metrics(built_pdf)
    if (
        metrics["pages"] != 1470
        or metrics["invalid_or_other_actions"] != 0
        or metrics["uri_actions"] != 0
        or metrics["raster_image_pages"]
        or any(metrics["hygiene_hits"].values())
    ):
        raise RuntimeError(f"SGA3 reader gate failed: {metrics}")
    log = previous.log_counts(build_log)
    if log["hard_errors"] or log["undefined_references"] or log["rerun_warnings"]:
        raise RuntimeError(f"SGA3 build-log gate failed: {log}")

    build_summary = text_bytes(
        f"""
# Public build summary

- engine: XeLaTeX, four passes
- pages: {metrics['pages']} A4
- named destinations: {metrics['named_destinations']}
- internal GoTo actions: {metrics['internal_goto_actions']}
- invalid or external actions: 0
- raster-image pages: 0
- hard errors: 0
- undefined-reference summaries: 0
- rerun warnings: 0
- archive-only source wrappers: {hygiene['total_wrappers']} across
  {hygiene['wrapper_files']} files
- newly archived reader-facing project notes: {hygiene['new_wrappers']}
- rendered project, source-process, AI, and workflow-note hits: 0
"""
    )
    hygiene_doc = text_bytes(
        f"""
# SGA 3 direct-reader hygiene R26

The direct PDF contains the mathematical text and genuine historical
Polo--Gille editorial apparatus. Project-generated translation-process,
source-discrepancy, source-locator, AI/tool, and workflow-status narration is
not printed in the reader.

R26 moves {hygiene['new_wrappers']} additional project notes in
{hygiene['changed_files']} files behind `\\SGAArchiveOnly{{...}}`. The complete
wording remains in the editable source archive for provenance and review.

The rendered 1,470-page PDF was scanned directly for the broader hygiene
patterns after the build. No project-facing note remains.
"""
    )
    readiness = text_bytes(
        """
# Publication readiness

Status: `PASS_DIRECT_READER_PURE_R26`.

The direct reader is suitable for ordinary mathematical reading. Historical
editorial apparatus intrinsic to the Polo--Gille edition remains. Project
provenance and correction discussion is confined to the grouped source ZIP.

This is a working English translation and TeX edition, not a critical-edition,
accessibility, or rights-clearance claim.
"""
    )
    generated = {
        "BUILD_SUMMARY_PUBLIC.md": build_summary,
        "READER_HYGIENE_R26.md": hygiene_doc,
        "PUBLICATION_READINESS.md": readiness,
    }
    reader_out = SGA3_PACKAGE / SGA3_PDF_NAME
    master_out = SGA3_PACKAGE / SGA3_MASTER_NAME
    source_zip = SGA3_PACKAGE / SGA3_ZIP_NAME
    shutil.copyfile(built_pdf, reader_out)
    shutil.copyfile(SGA3_R26_ROOT / SGA3_MASTER_NAME, master_out)
    for name, data in generated.items():
        (SGA3_PACKAGE / name).write_bytes(data)
    for name in ("README.md", "PROVENANCE_AND_RIGHTS.md"):
        shutil.copyfile(SGA3_R26_ROOT / name, SGA3_PACKAGE / name)
    zip_metrics = previous.make_source_zip(
        source_zip, source_members(SGA3_R26_ROOT, generated)
    )
    validation = {
        "status": "PASS_DIRECT_READER_PURE_R26",
        "errors": [],
        "reader": {"path": reader_out.name, **metrics},
        "master": {"path": master_out.name, **identity(master_out)},
        "source_zip": {"path": source_zip.name, **zip_metrics},
        "build": log,
        "reader_hygiene": hygiene,
    }
    (SGA3_PACKAGE / "PACKAGE_VALIDATION.json").write_bytes(
        text_bytes(json.dumps(validation, indent=2, ensure_ascii=False))
    )
    manifest = write_package_manifest(SGA3_PACKAGE)
    verify_no_private_paths(SGA3_PACKAGE)
    return {
        "package": SGA3_PACKAGE.relative_to(REPO_ROOT).as_posix(),
        "outer_files": len(list(SGA3_PACKAGE.iterdir())),
        "manifest": manifest,
        "reader": identity(reader_out),
        "source_zip": zip_metrics,
    }


def build_sga6_package(hygiene: dict[str, int]) -> dict:
    reset_package(SGA6_PACKAGE)
    build_dir = SGA6_R10_ROOT / SGA6_BUILD_DIR
    built_pdf = build_dir / "02f_SGA6_English_Master.pdf"
    build_log = build_dir / "02f_SGA6_English_Master.log"
    metrics = pdf_metrics(built_pdf)
    if (
        not 370 <= metrics["pages"] <= 378
        or metrics["invalid_or_other_actions"] != 0
        or metrics["uri_actions"] != 0
        or metrics["raster_image_pages"]
        or any(metrics["hygiene_hits"].values())
    ):
        raise RuntimeError(f"SGA6 reader gate failed: {metrics}")
    log = previous.log_counts(build_log)
    if log["hard_errors"] or log["undefined_references"] or log["rerun_warnings"]:
        raise RuntimeError(f"SGA6 build-log gate failed: {log}")

    build_summary = text_bytes(
        f"""
# Public build summary

- engine: pdfLaTeX, four passes
- pages: {metrics['pages']} A4
- named destinations: {metrics['named_destinations']}
- internal GoTo actions: {metrics['internal_goto_actions']}
- invalid or external actions: 0
- raster-image pages: 0
- hard errors: 0
- undefined-reference summaries: 0
- rerun warnings: 0
- reader-facing project-source prose removed or neutralized:
  {hygiene['replacements']}
- rendered project, source-process, AI, and workflow-note hits: 0
"""
    )
    hygiene_doc = text_bytes(
        """
# SGA 6 direct-reader hygiene R10

The direct PDF contains the mathematics and source-era prefaces/editorial
material. Three inherited project-facing source-summary phrases were removed
or restated as neutral mathematical prose.

The earlier wording is retained once in the source ZIP under `history/`.
No project, AI/tool, workflow-status, or source-locator prose is printed in
the direct reader.
"""
    )
    readiness = text_bytes(
        """
# Publication readiness

Status: `PASS_DIRECT_READER_PURE_R10`.

The direct reader is suitable for ordinary mathematical reading. Project
provenance and the superseded wording are confined to the grouped source ZIP.

This is a layered working English translation and TeX edition, not a
critical-edition, accessibility, or rights-clearance claim.
"""
    )
    generated = {
        "BUILD_SUMMARY_PUBLIC.md": build_summary,
        "READER_HYGIENE_R10.md": hygiene_doc,
        "PUBLICATION_READINESS.md": readiness,
    }
    reader_out = SGA6_PACKAGE / SGA6_PDF_NAME
    master_out = SGA6_PACKAGE / SGA6_MASTER_NAME
    source_zip = SGA6_PACKAGE / SGA6_ZIP_NAME
    shutil.copyfile(built_pdf, reader_out)
    shutil.copyfile(SGA6_R10_ROOT / SGA6_MASTER_NAME, master_out)
    for name, data in generated.items():
        (SGA6_PACKAGE / name).write_bytes(data)
    zip_metrics = previous.make_source_zip(
        source_zip, source_members(SGA6_R10_ROOT, generated)
    )
    validation = {
        "status": "PASS_DIRECT_READER_PURE_R10",
        "errors": [],
        "reader": {"path": reader_out.name, **metrics},
        "master": {"path": master_out.name, **identity(master_out)},
        "source_zip": {"path": source_zip.name, **zip_metrics},
        "build": log,
        "reader_hygiene": hygiene,
    }
    (SGA6_PACKAGE / "PACKAGE_VALIDATION.json").write_bytes(
        text_bytes(json.dumps(validation, indent=2, ensure_ascii=False))
    )
    manifest = write_package_manifest(SGA6_PACKAGE)
    verify_no_private_paths(SGA6_PACKAGE)
    return {
        "package": SGA6_PACKAGE.relative_to(REPO_ROOT).as_posix(),
        "outer_files": len(list(SGA6_PACKAGE.iterdir())),
        "manifest": manifest,
        "reader": identity(reader_out),
        "source_zip": zip_metrics,
    }


def main() -> None:
    if not SGA3_R26_ROOT.exists():
        copytree_once(
            SGA3_R25_ROOT,
            SGA3_R26_ROOT,
            ignore=shutil.ignore_patterns("build_reader_clean_r25"),
        )
        sga3_hygiene = apply_sga3_hygiene()
        (SGA3_R26_ROOT / "READER_HYGIENE_R26.md").write_bytes(
            text_bytes(
                f"""
# SGA 3 direct-reader hygiene R26

R26 is a no-overwrite successor to R25. It moves
{sga3_hygiene['new_wrappers']} additional project-generated source
discrepancy notes into the archive-only source layer. Genuine historical
Polo--Gille editorial apparatus remains in the reader.
"""
            )
        )
        run_latex(
            SGA3_R26_ROOT,
            SGA3_MASTER_NAME,
            SGA3_BUILD_DIR,
            "xelatex",
        )
    else:
        sga3_hygiene = measure_sga3_hygiene()
    if not (
        SGA3_R26_ROOT
        / SGA3_BUILD_DIR
        / "02c_SGA3_English_Master.pdf"
    ).exists():
        run_latex(
            SGA3_R26_ROOT,
            SGA3_MASTER_NAME,
            SGA3_BUILD_DIR,
            "xelatex",
        )

    if not SGA6_R10_ROOT.exists():
        copytree_once(SGA6_R9_ROOT, SGA6_R10_ROOT)
        shutil.copyfile(
            (
                REPO_ROOT
                / "sources"
                / "sga"
                / "sga1-6-reader-mathematical-body-clean-successor-v2-20260729"
                / "02f_SGA6_English_Complete_ReferenceLinked_Master_20260723.tex"
            ),
            SGA6_R10_ROOT / SGA6_MASTER_NAME,
        )
        sga6_hygiene = apply_sga6_hygiene()
    else:
        sga6_hygiene = measure_sga6_hygiene()
    if not (
        SGA6_R10_ROOT
        / SGA6_BUILD_DIR
        / "02f_SGA6_English_Master.pdf"
    ).exists():
        run_latex(
            SGA6_R10_ROOT,
            SGA6_MASTER_NAME,
            SGA6_BUILD_DIR,
            "pdflatex",
        )

    result = {
        "status": "PASS",
        "sga3": build_sga3_package(sga3_hygiene),
        "sga6": build_sga6_package(sga6_hygiene),
    }
    output = REPO_ROOT / "manifests" / "sga_reader_pure_r26_r10_build_20260730.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes(text_bytes(json.dumps(result, indent=2)))
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
