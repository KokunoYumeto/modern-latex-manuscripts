#!/usr/bin/env python3
"""Build the public Noether Interslavic working-corpus snapshot.

The script reads the frozen Latin/Cyrillic v001 corpus, compiles every unit
with XeLaTeX, creates reader PDFs, and packages the bounded normalization
evidence without modifying the live production tree.
"""

from __future__ import annotations

import csv
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import time
import zipfile
from datetime import datetime
from pathlib import Path

from pypdf import PdfReader, PdfWriter


LIVE_ROOT = Path(r"C:\Users\Floris\Documents\interlanguage")
CORPUS = LIVE_ROOT / "03_projects/noether/02_slavic_working_corpus"
TRANSLATIONS = CORPUS / "translations"
NORMALIZATION = (
    LIVE_ROOT
    / "03_projects/language_management/slavic_interslavic/normalization_20260718"
)
STAGE = Path(
    r"C:\Users\Floris\Documents\Codex\2026-05-26"
    r"\there-is-currently-an-ongoing-process\publish_curated"
    r"\20260718_noether_interslavic_002ab"
)
PACKAGE_NAME = "Noether_Interslavic_WorkingCorpus_Normalization_002A_002B_20260718"
PACKAGE = STAGE / PACKAGE_NAME
WORK = Path(r"C:\tmp\noether-interslavic-public-20260718")
LATIN_READER = STAGE / "02b_Noether_Interslavic_Latin_WorkingReader_20260718.pdf"
CYRILLIC_READER = STAGE / "02c_Noether_Interslavic_Cyrillic_WorkingReader_20260718.pdf"
ZIP_PATH = STAGE / "11_Noether_Interslavic_WorkingCorpus_Normalization_002A_002B_20260718.zip"
REPORT_PATH = STAGE / "build_release_report.json"
GERMAN_AUTHORITY = Path(
    r"C:\Users\Floris\Documents\Codex\2026-05-26"
    r"\there-is-currently-an-ongoing-process\publish_curated"
    r"\20260718_noether_spanish_r823"
    r"\Noether_Spanish_R823_WorkingTranslation_20260718"
    r"\03_source_authority\Noether_R823_German_Authority.tex"
)

WARNING_PATTERNS = {
    "latex_warning": re.compile(r"LaTeX Warning:", re.IGNORECASE),
    "package_warning": re.compile(r"Package .+ Warning:", re.IGNORECASE),
    "missing_character": re.compile(r"Missing character:", re.IGNORECASE),
    "overfull_box": re.compile(r"Overfull \\.[hv]box", re.IGNORECASE),
    "underfull_box": re.compile(r"Underfull \\.[hv]box", re.IGNORECASE),
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def natural_parts(value: str) -> tuple[object, ...]:
    parts: list[object] = []
    for part in re.split(r"(\d+)", value.casefold()):
        parts.append(int(part) if part.isdigit() else part)
    return tuple(parts)


def unit_sort_key(path: Path) -> tuple[object, ...]:
    parts = path.parts
    first = parts[0].casefold()
    match = re.fullmatch(r"paper(\d+)", first)
    if match:
        group = (0, int(match.group(1)))
    elif first == "endmatter":
        group = (1, 0)
    else:
        group = (2, 0)
    without_language = tuple(
        part
        for part in parts[1:]
        if part.casefold() not in {"interslavic", "interslavic-cyrillic", "v001"}
    )
    return (*group, *(natural_parts("/".join(without_language))))


def discover(language_dir: str) -> list[Path]:
    pattern = f"**/{language_dir}/v001/*.tex"
    paths = [path.relative_to(TRANSLATIONS) for path in TRANSLATIONS.glob(pattern)]
    paths.sort(key=unit_sort_key)
    if len(paths) != 221:
        raise RuntimeError(f"Expected 221 {language_dir} units, found {len(paths)}")
    return paths


def scan_log(path: Path) -> dict[str, int]:
    counts = {name: 0 for name in WARNING_PATTERNS}
    if not path.is_file():
        return counts
    with path.open("r", encoding="utf-8", errors="replace") as handle:
        for line in handle:
            for name, pattern in WARNING_PATTERNS.items():
                if pattern.search(line):
                    counts[name] += 1
    return counts


def compile_unit(index: int, language: str, relative: Path) -> dict[str, object]:
    source = TRANSLATIONS / relative
    numbered_name = f"{index:03d}_{source.name}"
    tex_out = PACKAGE / "02_tex" / language / numbered_name
    pdf_out = PACKAGE / "01_unit_pdfs" / language / numbered_name.replace(".tex", ".pdf")
    log_dir = PACKAGE / "05_build_logs" / language
    console_log = log_dir / f"{index:03d}_{source.stem}.console.log"
    tex_log = log_dir / f"{index:03d}_{source.stem}.tex.log"
    if (
        tex_out.is_file()
        and pdf_out.is_file()
        and sha256(tex_out) == sha256(source)
        and len(PdfReader(str(pdf_out)).pages) > 0
    ):
        findings = scan_log(tex_log if tex_log.is_file() else console_log)
        return {
            "sequence": index,
            "language": language,
            "source_relative_path": relative.as_posix(),
            "source_sha256": sha256(source),
            "package_tex": tex_out.relative_to(PACKAGE).as_posix(),
            "package_tex_sha256": sha256(tex_out),
            "package_pdf": pdf_out.relative_to(PACKAGE).as_posix(),
            "package_pdf_sha256": sha256(pdf_out),
            "pages": len(PdfReader(str(pdf_out)).pages),
            "pdf_bytes": pdf_out.stat().st_size,
            "duration_seconds": 0,
            "findings": findings,
            "resumed": True,
        }
    work_dir = WORK / f"{language[:3]}{index:03d}"
    work_dir.mkdir(parents=True, exist_ok=True)
    log_dir.mkdir(parents=True, exist_ok=True)
    command = [
        "latexmk",
        "-silent",
        "-g",
        "-xelatex",
        "-interaction=nonstopmode",
        "-halt-on-error",
        "-file-line-error",
        f"-outdir={work_dir}",
        source.name,
    ]
    started = time.monotonic()
    env = os.environ.copy()
    env["max_print_line"] = "1000"
    with console_log.open("w", encoding="utf-8", errors="replace") as console:
        completed = subprocess.run(
            command,
            cwd=source.parent,
            env=env,
            stdout=console,
            stderr=subprocess.STDOUT,
            check=False,
            timeout=180,
        )
    built_pdf = work_dir / f"{source.stem}.pdf"
    built_log = work_dir / f"{source.stem}.log"
    if completed.returncode != 0 or not built_pdf.is_file():
        raise RuntimeError(f"Compilation failed for {relative}; see {console_log}")
    reader = PdfReader(str(built_pdf))
    if not reader.pages:
        raise RuntimeError(f"Compiled PDF has no pages: {relative}")
    tex_out.parent.mkdir(parents=True, exist_ok=True)
    pdf_out.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, tex_out)
    shutil.copy2(built_pdf, pdf_out)
    if built_log.is_file():
        shutil.copy2(built_log, tex_log)
    findings = scan_log(tex_log if tex_log.is_file() else console_log)
    return {
        "sequence": index,
        "language": language,
        "source_relative_path": relative.as_posix(),
        "source_sha256": sha256(source),
        "package_tex": tex_out.relative_to(PACKAGE).as_posix(),
        "package_tex_sha256": sha256(tex_out),
        "package_pdf": pdf_out.relative_to(PACKAGE).as_posix(),
        "package_pdf_sha256": sha256(pdf_out),
        "pages": len(reader.pages),
        "pdf_bytes": pdf_out.stat().st_size,
        "duration_seconds": round(time.monotonic() - started, 3),
        "findings": findings,
    }


def make_cover(language: str, script_label: str) -> Path:
    cover_dir = WORK / f"cover-{language}"
    cover_dir.mkdir(parents=True, exist_ok=True)
    tex = cover_dir / "cover.tex"
    tex.write_text(
        "\\documentclass[11pt]{article}\n"
        "\\usepackage[a4paper,margin=28mm]{geometry}\n"
        "\\usepackage{fontspec}\n"
        "\\setmainfont{Times New Roman}\n"
        "\\pagestyle{empty}\n"
        "\\begin{document}\n"
        "\\vspace*{35mm}\n"
        "\\begin{center}\n"
        "{\\LARGE Emmy Noether}\\\\[8mm]\n"
        f"{{\\Large Interslavic Working Translation Reader ({script_label})}}\\\\[8mm]\n"
        "{\\large Canonical v001 unit snapshot, 18 July 2026}\\\\[18mm]\n"
        "\\end{center}\n"
        "\\noindent This reader concatenates 221 independently compiled translation units. "
        "It incorporates bounded orthography Tranche 002A and exact lexical Tranche 002B. "
        "The units are working translations and have not received native-language, community, "
        "peer-review, critical-edition, or complete source-faithfulness certification.\\par\n"
        "\\vfill\n"
        "\\noindent Editable TeX, unit mapping, build evidence, normalization ledgers, diffs, "
        "preimages, and visual-QA material are supplied in the companion archive.\n"
        "\\end{document}\n",
        encoding="utf-8",
    )
    command = [
        "latexmk",
        "-silent",
        "-xelatex",
        "-interaction=nonstopmode",
        "-halt-on-error",
        "-file-line-error",
        "cover.tex",
    ]
    subprocess.run(command, cwd=cover_dir, check=True, timeout=180)
    return cover_dir / "cover.pdf"


def merge_reader(language: str, rows: list[dict[str, object]], output: Path) -> None:
    label = "Latin script" if language == "latin" else "Cyrillic script"
    writer = PdfWriter()
    writer.append(str(make_cover(language, label)))
    for row in rows:
        writer.append(str(PACKAGE / str(row["package_pdf"])))
    with output.open("wb") as handle:
        writer.write(handle)
    expected = 1 + sum(int(row["pages"]) for row in rows)
    actual = len(PdfReader(str(output)).pages)
    if actual != expected:
        raise RuntimeError(f"Reader page mismatch for {language}: {actual} != {expected}")


def copy_tree(source: Path, target: Path, include=None) -> None:
    for path in source.rglob("*"):
        if not path.is_file() or (include and not include(path)):
            continue
        destination = target / path.relative_to(source)
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, destination)


def copy_supporting_material() -> None:
    for name in ("glossary", "logs", "segments", "sources", "tools"):
        copy_tree(CORPUS / name, PACKAGE / "03_corpus_support" / name)
    copy_tree(
        TRANSLATIONS,
        PACKAGE / "03_corpus_support" / "unit_metadata",
        include=lambda path: path.suffix.casefold() == ".json",
    )
    for tranche in ("tranche_002a_orthography", "tranche_002b_lexical_exact"):
        source = NORMALIZATION / tranche
        target = PACKAGE / "04_normalization_evidence" / tranche
        for name in ("evidence", "preimage"):
            copy_tree(source / name, target / name)
        for name in ("master_sheets", "contact_sheets"):
            copy_tree(source / "visual_qa" / name, target / "visual_qa" / name)
    audit = NORMALIZATION / "evidence" / "NORMALIZATION_STATUS_AUDIT.json"
    destination = PACKAGE / "04_normalization_evidence" / audit.name
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(audit, destination)
    scripts_out = PACKAGE / "06_workflow_scripts"
    scripts_out.mkdir(parents=True, exist_ok=True)
    for name in (
        "audit_interslavic_normalization_status.py",
        "apply_interslavic_orthography_rollout.py",
        "apply_interslavic_lexical_exact.py",
        "build_interslavic_orthography_rollout.py",
        "verify_interslavic_pdf_render.py",
    ):
        source = LIVE_ROOT / "scripts" / name
        if source.is_file():
            shutil.copy2(source, scripts_out / name)
    if GERMAN_AUTHORITY.is_file():
        authority_out = PACKAGE / "07_source_authority" / GERMAN_AUTHORITY.name
        authority_out.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(GERMAN_AUTHORITY, authority_out)


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "sequence",
        "language",
        "source_relative_path",
        "source_sha256",
        "package_tex",
        "package_tex_sha256",
        "package_pdf",
        "package_pdf_sha256",
        "pages",
        "pdf_bytes",
        "duration_seconds",
        "resumed",
        "latex_warning",
        "package_warning",
        "missing_character",
        "overfull_box",
        "underfull_box",
    ]
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            flat = dict(row)
            findings = flat.pop("findings")
            flat.update(findings)
            writer.writerow(flat)


def write_readme(rows: list[dict[str, object]]) -> None:
    totals = {
        language: {
            "units": sum(1 for row in rows if row["language"] == language),
            "pages": sum(int(row["pages"]) for row in rows if row["language"] == language),
        }
        for language in ("latin", "cyrillic")
    }
    (PACKAGE / "00_README_STATUS.md").write_text(
        "# Emmy Noether Interslavic working corpus\n\n"
        "This package freezes the canonical `v001` Interslavic working translations "
        "after normalization Tranches 002A and 002B. It contains 221 Latin-script "
        f"units ({totals['latin']['pages']} compiled pages) and 221 Cyrillic-script "
        f"units ({totals['cyrillic']['pages']} compiled pages), editable TeX, individual "
        "PDFs, two reader PDFs, unit maps, source/support metadata, and the complete "
        "bounded normalization evidence.\n\n"
        "Tranche 002A applies a reviewed orthography set. Tranche 002B applies only "
        "the explicitly accepted exact lexical switches. Held and unreviewed forms "
        "remain unchanged. Both tranches are idempotent. All 442 frozen TeX units "
        "compiled in this archive pass. The earlier tranche QA rendered every affected "
        "page and reported no machine flags.\n\n"
        "## Status limit\n\n"
        "These are substantial machine-produced working translations. This package "
        "is not a critical edition, a native-language or community certificate, a "
        "peer review, or a complete paper-by-paper source-faithfulness certificate. "
        "The build and render checks establish artifact integrity and bounded change "
        "control; they do not establish linguistic or mathematical correctness.\n",
        encoding="utf-8",
    )


def write_hashes() -> None:
    files = sorted(path for path in PACKAGE.rglob("*") if path.is_file())
    with (PACKAGE / "SHA256SUMS.csv").open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["relative_path", "bytes", "sha256"])
        for path in files:
            writer.writerow([path.relative_to(PACKAGE).as_posix(), path.stat().st_size, sha256(path)])


def make_zip() -> None:
    with zipfile.ZipFile(ZIP_PATH, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as archive:
        for path in sorted(PACKAGE.rglob("*")):
            if path.is_file():
                archive.write(path, f"{PACKAGE_NAME}/{path.relative_to(PACKAGE).as_posix()}")
    with zipfile.ZipFile(ZIP_PATH, "r") as archive:
        bad = archive.testzip()
        if bad:
            raise RuntimeError(f"ZIP test failed at {bad}")


def main() -> int:
    if ZIP_PATH.exists() or REPORT_PATH.exists():
        raise RuntimeError("Completed release output already exists; refusing to overwrite it")
    STAGE.mkdir(parents=True, exist_ok=True)
    PACKAGE.mkdir(parents=True, exist_ok=True)
    WORK.mkdir(parents=True, exist_ok=True)
    all_rows: list[dict[str, object]] = []
    language_specs = (
        ("latin", "interslavic"),
        ("cyrillic", "interslavic-cyrillic"),
    )
    for language, language_dir in language_specs:
        paths = discover(language_dir)
        rows: list[dict[str, object]] = []
        for index, relative in enumerate(paths, start=1):
            row = compile_unit(index, language, relative)
            rows.append(row)
            print(
                f"[{language} {index:03d}/221] pages={row['pages']} "
                f"{relative.as_posix()}",
                flush=True,
            )
        all_rows.extend(rows)
        output = LATIN_READER if language == "latin" else CYRILLIC_READER
        merge_reader(language, rows, output)
        reader_copy = PACKAGE / "00_readers" / output.name
        reader_copy.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(output, reader_copy)

    copy_supporting_material()
    write_csv(PACKAGE / "UNIT_BUILD_MANIFEST.csv", all_rows)
    write_readme(all_rows)
    write_hashes()
    make_zip()

    findings = {
        key: sum(int(row["findings"][key]) for row in all_rows)
        for key in WARNING_PATTERNS
    }
    report = {
        "schema": "noether-interslavic-public-release-v1",
        "generated_at": datetime.now().astimezone().isoformat(),
        "corpus_snapshot": str(TRANSLATIONS),
        "normalization_snapshot": str(NORMALIZATION),
        "units": len(all_rows),
        "latin_units": 221,
        "cyrillic_units": 221,
        "unit_pages": sum(int(row["pages"]) for row in all_rows),
        "finding_totals": findings,
        "latin_reader": {
            "path": str(LATIN_READER),
            "bytes": LATIN_READER.stat().st_size,
            "pages": len(PdfReader(str(LATIN_READER)).pages),
            "sha256": sha256(LATIN_READER),
        },
        "cyrillic_reader": {
            "path": str(CYRILLIC_READER),
            "bytes": CYRILLIC_READER.stat().st_size,
            "pages": len(PdfReader(str(CYRILLIC_READER)).pages),
            "sha256": sha256(CYRILLIC_READER),
        },
        "zip": {
            "path": str(ZIP_PATH),
            "bytes": ZIP_PATH.stat().st_size,
            "sha256": sha256(ZIP_PATH),
        },
        "status_limit": (
            "Working translations and bounded normalization evidence; not a critical "
            "edition, native/community certification, peer review, or complete "
            "source-faithfulness certificate."
        ),
    }
    REPORT_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2), flush=True)
    return 0


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    raise SystemExit(main())
