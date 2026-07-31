#!/usr/bin/env python3
"""Build the complete EGA IV Sections 16-18 reader/source release archive."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import shutil
import subprocess
import tempfile
import zipfile
from datetime import datetime
from pathlib import Path, PurePosixPath


AUTHORITY_SHA256 = "B4277FB99C6EDF8FEEC5B01F54368E4B8521BCD52871316C0EDF6FF4AE69389E"
ARCHIVE_NAME = "EGA4_Sections16_18_English_SourceAligned_Reader_Source_20260731"
ZIP_TIMESTAMP = (2026, 7, 31, 0, 0, 0)
EXPECTED = {
    "source/source_aligned/ega4-16.tex": (
        177_024,
        "117AA3D848923C3FF849713BA124C5E106FA9A89EBF5557FA6055ACDC7631E2F",
    ),
    "source/source_aligned/ega4-17.tex": (
        194_286,
        "5CFAAA5DF8AF305F49CD7475B67B97586F181854C5751C7454DECE865D994EC0",
    ),
    "source/source_aligned/ega4-18.tex": (
        339_386,
        "3FD14DFB6410BD094F3FE68ED98AEC5BF1DD082E031B1E21AC28949D6364FAB3",
    ),
    "build_harness/ega4_sections16_18_source_aligned_successor_r1.tex": (
        388,
        "1AB44608794C184ABB8BA63BC20AFC1D19B7C9F22196BBA6E022438975E38724",
    ),
    "producer_pdf": (
        912_813,
        "363F3C346F0C77EB10C3F5D69A66BBB99060C3983EFD06F19441CB969BDCC083",
    ),
}
HARD_TEX_PATTERNS = (
    "! LaTeX Error",
    "Undefined control sequence",
    "Emergency stop",
    "Fatal error",
    "Missing character:",
    "destination with the same identifier",
)
FORBIDDEN = tuple(
    re.compile(pattern, re.IGNORECASE)
    for pattern in (
        r"C:\\Users\\",
        r"AppData",
        r"Papors",
        r"Chatnotes",
        r"Claude",
        r"Codex",
        r"ChatGPT",
        r"source_thread_id",
        r"019f[0-9a-f-]{20,}",
    )
)


def sha256_path(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def identity(path: Path) -> tuple[int, str]:
    return path.stat().st_size, sha256_path(path)


def run(command: list[str], cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        command,
        cwd=cwd,
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )


def pdf_pages(path: Path) -> int:
    result = run(["pdfinfo", str(path)], path.parent)
    if result.returncode:
        raise RuntimeError(f"pdfinfo failed: {result.stdout}")
    match = re.search(r"^Pages:\s+(\d+)\s*$", result.stdout, re.MULTILINE)
    if not match:
        raise RuntimeError("Could not parse PDF page count")
    return int(match.group(1))


def pdf_text(path: Path) -> str:
    result = run(["pdftotext", str(path), "-"], path.parent)
    if result.returncode:
        raise RuntimeError(f"pdftotext failed: {result.stdout}")
    return result.stdout


def scan_forbidden(label: str, text: str) -> list[str]:
    return [f"{label}: {pattern.pattern}" for pattern in FORBIDDEN if pattern.search(text)]


def safe_member(name: str) -> bool:
    pure = PurePosixPath(name)
    return (
        name == name.replace("\\", "/")
        and not pure.is_absolute()
        and ".." not in pure.parts
        and not re.match(r"^[A-Za-z]:", name)
    )


def role(relative: str) -> str:
    if relative.startswith("reader/"):
        return "bounded_working_reader"
    if relative.startswith("source/source_aligned/"):
        return "editable_source"
    if relative.startswith("build_harness/"):
        return "build_dependency"
    if relative == "README.md":
        return "reader_source_scope"
    if relative == "STATUS_PUBLIC.md":
        return "public_status"
    if relative == "BUILD_SUMMARY_PUBLIC.md":
        return "sanitized_build_summary"
    if relative == "PACKAGE_VALIDATION.json":
        return "package_validation"
    if relative == ".gitattributes":
        return "byte_preservation_control"
    raise RuntimeError(f"Unclassified release file: {relative}")


def write_zip(package: Path, output: Path) -> dict[str, object]:
    files = sorted(
        (path for path in package.rglob("*") if path.is_file()),
        key=lambda path: path.relative_to(package).as_posix().casefold(),
    )
    expected = {
        f"{ARCHIVE_NAME}/{path.relative_to(package).as_posix()}": identity(path)
        for path in files
    }
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, allowZip64=True) as archive:
        for path in files:
            name = f"{ARCHIVE_NAME}/{path.relative_to(package).as_posix()}"
            info = zipfile.ZipInfo(name, ZIP_TIMESTAMP)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = (0o100644 & 0xFFFF) << 16
            archive.writestr(info, path.read_bytes())
    observed: dict[str, tuple[int, str]] = {}
    with zipfile.ZipFile(output) as archive:
        infos = [item for item in archive.infolist() if not item.is_dir()]
        names = [item.filename for item in infos]
        if len(names) != len(set(names)) or not all(safe_member(name) for name in names):
            raise RuntimeError("Unsafe or duplicate ZIP member")
        if archive.testzip() is not None:
            raise RuntimeError("ZIP CRC failure")
        for item in infos:
            data = archive.read(item)
            observed[item.filename] = (
                len(data),
                hashlib.sha256(data).hexdigest().upper(),
            )
    if observed != expected:
        raise RuntimeError("ZIP member identity replay failed")
    return {
        "filename": output.name,
        "bytes": output.stat().st_size,
        "sha256": sha256_path(output),
        "members": len(observed),
        "uncompressed_bytes": sum(size for size, _digest in observed.values()),
        "safe_paths": True,
        "crc_pass": True,
        "member_identities_exact": True,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-root", type=Path, required=True)
    parser.add_argument("--destination", type=Path, required=True)
    parser.add_argument("--zip-output", type=Path, required=True)
    args = parser.parse_args()
    source_root = args.source_root.resolve()
    destination = args.destination.resolve()
    zip_output = args.zip_output.resolve()
    if destination.exists() or zip_output.exists():
        raise RuntimeError("No-overwrite output already exists")

    sources = {
        "build_harness/ega4_sections16_18_source_aligned_successor_r1.tex": source_root
        / "build_harness/ega4_sections16_18_source_aligned_successor_r1.tex",
        "build_harness/preamble.tex": source_root / "build_harness/preamble.tex",
        "build_harness/preamble-base.tex": source_root / "build_harness/preamble-base.tex",
        "source/source_aligned/ega4-16.tex": source_root / "source/source_aligned/ega4-16.tex",
        "source/source_aligned/ega4-17.tex": source_root / "source/source_aligned/ega4-17.tex",
        "source/source_aligned/ega4-18.tex": source_root / "source/source_aligned/ega4-18.tex",
    }
    producer_pdf = source_root / "build/complete_sections16_18_source_aligned_r42/ega4_sections16_18_source_aligned_successor_r1.pdf"
    for relative, path in sources.items():
        if not path.is_file():
            raise FileNotFoundError(path)
        if relative in EXPECTED and identity(path) != EXPECTED[relative]:
            raise RuntimeError(f"Controlling source identity changed: {relative}")
    if identity(producer_pdf) != EXPECTED["producer_pdf"]:
        raise RuntimeError("Controlling producer PDF identity changed")
    before = {relative: identity(path) for relative, path in sources.items()}

    destination.mkdir(parents=True)
    for relative, source in sources.items():
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
    reader = destination / "reader/EGA4_Sections16_18_English_SourceAligned_Working_Reader_20260731.pdf"
    reader.parent.mkdir(parents=True)
    shutil.copyfile(producer_pdf, reader)
    if any(identity(destination / relative) != expected for relative, expected in before.items()):
        raise RuntimeError("Copied source identity mismatch")
    if any(identity(path) != before[relative] for relative, path in sources.items()):
        raise RuntimeError("Producer source changed during capture")

    with tempfile.TemporaryDirectory(prefix="ega4_16_18_complete_release_") as temp_name:
        temp = Path(temp_name)
        shutil.copytree(destination / "build_harness", temp / "build_harness")
        shutil.copytree(destination / "source", temp / "source")
        harness = temp / "build_harness"
        consoles: list[str] = []
        returncodes: list[int] = []
        for _ in range(3):
            result = run(
                [
                    "xelatex",
                    "-interaction=nonstopmode",
                    "-halt-on-error",
                    "-file-line-error",
                    "ega4_sections16_18_source_aligned_successor_r1.tex",
                ],
                harness,
            )
            returncodes.append(result.returncode)
            consoles.append(result.stdout)
        if any(returncodes):
            raise RuntimeError(f"Fresh build failed: {returncodes}\n{consoles[-1]}")
        combined = "\n".join(consoles)
        hard_hits = [pattern for pattern in HARD_TEX_PATTERNS if pattern in combined]
        if hard_hits:
            raise RuntimeError(f"Fresh build hard diagnostics: {hard_hits}")
        fresh_pdf = harness / "ega4_sections16_18_source_aligned_successor_r1.pdf"
        if pdf_pages(reader) != 136 or pdf_pages(fresh_pdf) != 136:
            raise RuntimeError("Reader page-count mismatch")
        producer_text = pdf_text(reader)
        fresh_text = pdf_text(fresh_pdf)
        if producer_text != fresh_text:
            raise RuntimeError("Fresh build text differs from sealed producer PDF")
        console_sha = hashlib.sha256(consoles[-1].encode("utf-8")).hexdigest().upper()

    (destination / ".gitattributes").write_bytes(b"* -text\n")
    (destination / "README.md").write_text(
        """# EGA IV Sections 16-18 source-aligned English working reader

This bounded package covers EGA IV Sections 16-18 continuously from printed
page 5 through the final two paragraphs of Section 18 on printed page 185. It
stops before the Section 19 heading and body. The package contains the
136-page reader and its complete editable TeX closure.

The controlling authority is the 360-page NUMDAM EGA IV Part 4 scan, SHA-256
`B4277FB99C6EDF8FEEC5B01F54368E4B8521BCD52871316C0EDF6FF4AE69389E`.
The authority scan and OCR are excluded. Actual scan-derived image witnesses
are preserved in separate archives on the same EGA concept.

This is a complete source-aligned working reader for the stated bounded scope,
not a cumulative EGA IV Sections 1-21 reader, critical edition, mathematical or
peer certification, accessibility remediation, or blanket rights decision.
""",
        encoding="ascii",
        newline="\n",
    )
    (destination / "STATUS_PUBLIC.md").write_text(
        """# Public status

- Scope: EGA IV Sections 16-18, printed pages 5-185.
- Boundary: complete through Corollary 18.12.17; Section 19 excluded.
- Editable TeX closure: included.
- Reader: 136 letter pages.
- Fresh package build: three XeLaTeX passes; zero hard diagnostics.
- Fresh/package reader extracted text: exact.
- Authority scan, OCR, raw logs, auxiliaries, and caches: excluded.
- Classification: bounded source-aligned English working reader.
- Whole-EGA IV, critical-edition, peer-review, accessibility, and rights-clearance claims: no.
""",
        encoding="ascii",
        newline="\n",
    )
    (destination / "BUILD_SUMMARY_PUBLIC.md").write_text(
        f"""# Build summary

- Producer reader: 136 pages / {reader.stat().st_size} bytes / SHA-256 `{sha256_path(reader)}`.
- Fresh copied-source build: three XeLaTeX passes, return codes 0/0/0.
- Hard TeX diagnostics: 0.
- Fresh and producer page counts: 136/136.
- Fresh and producer extracted text: exact.
- Final fresh console SHA-256: `{console_sha}`.
- Producer-reported visual review: terminal reader pages 129-136 plus corrected pages 133 and 136 PASS.
""",
        encoding="ascii",
        newline="\n",
    )

    privacy_hits: list[str] = []
    for path in destination.rglob("*"):
        if path.is_file() and path.suffix.lower() in {".tex", ".md", ".csv", ".json"}:
            privacy_hits.extend(
                scan_forbidden(
                    path.relative_to(destination).as_posix(),
                    path.read_text(encoding="utf-8", errors="replace"),
                )
            )
    privacy_hits.extend(scan_forbidden("reader_pdf_text", pdf_text(reader)))
    if privacy_hits:
        raise RuntimeError(f"Privacy/process scan failed: {privacy_hits}")

    validation = {
        "status": "PASS_ARCHIVE_HANDOFF_READY",
        "checked_at": datetime.now().astimezone().isoformat(),
        "scope": "EGA IV Sections 16-18 / printed pages 5-185 / hard stop before Section 19",
        "authority_sha256": AUTHORITY_SHA256,
        "source_files": 6,
        "editable_content_files": 3,
        "reader_pages": 136,
        "reader_bytes": reader.stat().st_size,
        "reader_sha256": sha256_path(reader),
        "fresh_build_passes": 3,
        "hard_tex_diagnostics": 0,
        "fresh_build_text_exact": True,
        "source_copy_mismatches": 0,
        "source_changed_during_capture": 0,
        "privacy_or_process_hits": 0,
        "authority_scan_included": False,
        "source_images_included": False,
        "errors": [],
    }
    validation_path = destination / "PACKAGE_VALIDATION.json"
    validation_path.write_text(
        json.dumps(validation, ensure_ascii=True, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )

    manifest_path = destination / "SHA256SUMS.csv"
    files = sorted(
        (
            path
            for path in destination.rglob("*")
            if path.is_file() and path != manifest_path
        ),
        key=lambda path: path.relative_to(destination).as_posix().casefold(),
    )
    with manifest_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=("path", "bytes", "sha256", "role", "status"),
            lineterminator="\r\n",
        )
        writer.writeheader()
        for path in files:
            relative = path.relative_to(destination).as_posix()
            writer.writerow(
                {
                    "path": relative,
                    "bytes": path.stat().st_size,
                    "sha256": sha256_path(path),
                    "role": role(relative),
                    "status": "proposed_public_grouped_source_reader_archive",
                }
            )

    zip_output.parent.mkdir(parents=True, exist_ok=True)
    archive = write_zip(destination, zip_output)
    result = {
        **validation,
        "package_files": len(files) + 1,
        "package_bytes": sum(path.stat().st_size for path in destination.rglob("*") if path.is_file()),
        "manifest_rows": len(files),
        "manifest_bytes": manifest_path.stat().st_size,
        "manifest_sha256": sha256_path(manifest_path),
        "zip_archive": archive,
    }
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
