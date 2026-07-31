#!/usr/bin/env python3
"""Build the bounded EGA IV Sections 19-21 plus Part 4 backmatter release."""

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

from pypdf import PdfReader


AUTHORITY_SHA256 = "B4277FB99C6EDF8FEEC5B01F54368E4B8521BCD52871316C0EDF6FF4AE69389E"
ARCHIVE_NAME = "EGA4_Sections19_21_Part4_Backmatter_English_Working_20260731"
ZIP_TIMESTAMP = (2026, 7, 31, 0, 0, 0)
HARNESS = "build_harness/ega4_sections19_21_source_aligned_successor_r1.tex"
PRODUCER_PDF = (
    "build_complete_with_backmatter_r4/"
    "ega4_sections19_21_source_aligned_successor_r1.pdf"
)
EXPECTED = {
    HARNESS: (
        686,
        "1C0682E773FE57D17438474D167B98053C12999631CCFC041C44C3EE0F732AC7",
    ),
    "build_harness/preamble-base.tex": (
        2244,
        "15E4C08F216D49D33DE25388D9E84537617BCC904ABFC56A05C0C3729348A1F7",
    ),
    "build_harness/preamble.tex": (
        4624,
        "964F90F04FAC962E5DC4E5D7C116DE51714E15243A90ABD0DBE0FFDB67036FA8",
    ),
    "source/source_aligned/ega4-19.tex": (
        175857,
        "803DD260ED0B988FC95084CE10203C05B1840F7B689919FE25E18C6704120496",
    ),
    "source/source_aligned/ega4-20.tex": (
        114865,
        "D46758217211FD5F33CA3450AEA541F7D99C4E959C505749DA3D54E4F4A169A3",
    ),
    "source/source_aligned/ega4-21-erratum53-insertion.tex": (
        11962,
        "3038FD72AFF7BDFE38F1649BAD8A035CA0BB987A31D975184BF87314AB83A179",
    ),
    "source/source_aligned/ega4-21.tex": (
        339607,
        "86EC9D3EB14798A3E64E47A52D39971C4A724DFF5233612D6AECAE140EF073F3",
    ),
    "source/source_aligned/ega4-backmatter-bibliography.tex": (
        1450,
        "15FA33C093B04EEAF52817091820051FE6D6BB821BDD5E06E73A07165B639B24",
    ),
    "source/source_aligned/ega4-backmatter-contents.tex": (
        6322,
        "F9EFC9C8D57D4FA238731793C931A4F0D5BD8FC28EE1CF3334A82EABC6D00625",
    ),
    "source/source_aligned/ega4-backmatter-notation.tex": (
        8105,
        "97B47C62975FF857D50FA5133C2286698BBAD7F4D4E2403BFF4C231BE0CAF6B6",
    ),
    "source/source_aligned/ega4-backmatter-terminology.tex": (
        14041,
        "7613C9F49790541F2D7D891548A10F2509F72B96D771015DAD9638FC5A61CB61",
    ),
    "source/source_aligned/ega4-errata-addenda-list3.tex": (
        49863,
        "A6B8D9418B4EEFC192CE9B74325B0A0DD32E92E492A4659C716F599A5F7FA6DB",
    ),
    PRODUCER_PDF: (
        861609,
        "AC4031BDB6BA5C4AAC9FA569CD28FDDB477026FB744B04DBACC6F9DFB9F1C108",
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
        r"OpenAI",
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


def pdf_facts(path: Path) -> dict[str, object]:
    reader = PdfReader(path)
    texts = [(page.extract_text() or "") for page in reader.pages]
    streams = [
        hashlib.sha256(page.get_contents().get_data()).hexdigest().upper()
        for page in reader.pages
    ]
    destination_names = set(reader.named_destinations)
    goto_actions = 0
    external_actions = 0
    for page in reader.pages:
        for reference in page.get("/Annots", []):
            annotation = reference.get_object()
            action = annotation.get("/A")
            if not action:
                continue
            action = action.get_object()
            kind = action.get("/S")
            if kind == "/GoTo":
                goto_actions += 1
            elif kind:
                external_actions += 1
    return {
        "pages": len(reader.pages),
        "texts": texts,
        "streams": streams,
        "text_empty_pages": sum(not text.strip() for text in texts),
        "named_destinations": len(destination_names),
        "goto_actions": goto_actions,
        "external_actions": external_actions,
    }


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
        relative: source_root / relative
        for relative in EXPECTED
        if relative != PRODUCER_PDF
    }
    producer_pdf = source_root / PRODUCER_PDF
    for relative, path in {**sources, PRODUCER_PDF: producer_pdf}.items():
        if not path.is_file() or identity(path) != EXPECTED[relative]:
            raise RuntimeError(f"Controlling identity changed: {relative}")
    before = {relative: identity(path) for relative, path in sources.items()}

    destination.mkdir(parents=True)
    for relative, source in sources.items():
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
    reader_path = (
        destination
        / "reader/EGA4_Sections19_21_Part4_Backmatter_English_Working_20260731.pdf"
    )
    reader_path.parent.mkdir(parents=True)
    shutil.copyfile(producer_pdf, reader_path)
    if any(identity(destination / relative) != expected for relative, expected in before.items()):
        raise RuntimeError("Copied source identity mismatch")
    if any(identity(path) != before[relative] for relative, path in sources.items()):
        raise RuntimeError("Producer source changed during capture")

    producer_facts = pdf_facts(reader_path)
    if producer_facts["pages"] != 134 or producer_facts["text_empty_pages"]:
        raise RuntimeError("Producer reader page/text boundary changed")

    with tempfile.TemporaryDirectory(prefix="ega4_19_21_backmatter_release_") as temp_name:
        temp = Path(temp_name)
        shutil.copytree(destination / "build_harness", temp / "build_harness")
        shutil.copytree(destination / "source", temp / "source")
        harness = temp / "build_harness"
        consoles: list[str] = []
        returncodes: list[int] = []
        for _ in range(4):
            result = run(
                [
                    "xelatex",
                    "-interaction=nonstopmode",
                    "-halt-on-error",
                    "-file-line-error",
                    Path(HARNESS).name,
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
        fresh_pdf = harness / "ega4_sections19_21_source_aligned_successor_r1.pdf"
        fresh_facts = pdf_facts(fresh_pdf)
        if (
            fresh_facts["pages"] != producer_facts["pages"]
            or fresh_facts["texts"] != producer_facts["texts"]
            or fresh_facts["streams"] != producer_facts["streams"]
        ):
            raise RuntimeError("Fresh build page text/content differs from producer reader")
        final_console_sha = hashlib.sha256(consoles[-1].encode("utf-8")).hexdigest().upper()
        convergence = consoles[-1] == consoles[-2]
        undefined_hyperrefs = len(re.findall(r"Hyper reference .* undefined", consoles[-1]))

    (destination / ".gitattributes").write_bytes(b"* -text\n")
    (destination / "README.md").write_text(
        """# EGA IV Sections 19-21 and Part 4 backmatter working reader

This bounded source-aligned English package covers Sections 19-21 on printed
pages 185-332 and the Part 4 bibliography, notation index, terminological
index, original contents, and Errata and Addenda List 3 on printed pages
333-343 and 345-361. It contains the 134-page reader and its complete editable
TeX closure.

The controlling authority is the publicly available 360-page NUMDAM EGA IV
Part 4 scan, SHA-256
`B4277FB99C6EDF8FEEC5B01F54368E4B8521BCD52871316C0EDF6FF4AE69389E`.
The authority scan and OCR are excluded from this ZIP. Actual scan-derived
image witnesses are preserved in separate archives on the same EGA concept.

This is a bounded source-aligned working reader, not a cumulative EGA IV
Sections 1-21 integration, critical edition, mathematical or peer
certification, accessibility remediation, or blanket rights decision.
Standalone cross-volume references remain visibly readable but may not be
clickable until a later cumulative EGA IV integration.
""",
        encoding="ascii",
        newline="\n",
    )
    (destination / "STATUS_PUBLIC.md").write_text(
        f"""# Public status

- Scope: EGA IV Sections 19-21 and Part 4 backmatter through printed page 361.
- Reader: 134 US-letter pages / {reader_path.stat().st_size} bytes / SHA-256 `{sha256_path(reader_path)}`.
- Editable TeX closure: 12 files, including one erratum insertion unit.
- Fresh copied-source build: four XeLaTeX passes; return codes 0/0/0/0.
- Fresh/producer page text and decoded content streams: exact on 134/134 pages.
- Hard TeX diagnostics: 0.
- Standalone undefined cross-volume hyperreference warnings: {undefined_hyperrefs}.
- Text-empty pages and reader-facing AI/process notes: 0.
- Classification: bounded source-aligned English working reader.
- Cumulative Sections 1-21, critical-edition, peer-review, accessibility, and rights-clearance claims: no.
""",
        encoding="ascii",
        newline="\n",
    )
    (destination / "BUILD_SUMMARY_PUBLIC.md").write_text(
        f"""# Build summary

- Producer reader: 134 pages / {reader_path.stat().st_size} bytes / SHA-256 `{sha256_path(reader_path)}`.
- Fresh copied-source build: four XeLaTeX passes, return codes 0/0/0/0.
- Pass 3/4 console convergence: {str(convergence).lower()}.
- Final fresh console SHA-256: `{final_console_sha}`.
- Hard TeX diagnostics: 0.
- Standalone undefined cross-volume hyperreference warnings: {undefined_hyperrefs}.
- Fresh and producer page text/content: exact on 134/134 pages.
- Producer named destinations / internal GoTo actions: {producer_facts['named_destinations']} / {producer_facts['goto_actions']}.
- External PDF actions: {producer_facts['external_actions']}.
- Text-empty pages: 0.
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
    privacy_hits.extend(
        scan_forbidden("reader_pdf_text", "\n".join(producer_facts["texts"]))
    )
    if privacy_hits:
        raise RuntimeError(f"Privacy/process scan failed: {privacy_hits}")

    validation = {
        "status": "PASS_BOUNDED_WORKING_READER_READY",
        "checked_at": datetime.now().astimezone().isoformat(),
        "scope": "EGA IV Sections 19-21, printed pages 185-332, plus Part 4 backmatter source on printed pages 333-343 and 345-361",
        "authority_sha256": AUTHORITY_SHA256,
        "source_files": len(sources),
        "editable_content_files": 9,
        "reader_pages": 134,
        "reader_bytes": reader_path.stat().st_size,
        "reader_sha256": sha256_path(reader_path),
        "fresh_build_passes": 4,
        "hard_tex_diagnostics": 0,
        "standalone_undefined_hyperreference_warnings": undefined_hyperrefs,
        "fresh_build_page_text_exact": True,
        "fresh_build_page_content_exact": True,
        "named_destinations": producer_facts["named_destinations"],
        "goto_actions": producer_facts["goto_actions"],
        "external_actions": producer_facts["external_actions"],
        "text_empty_pages": 0,
        "source_copy_mismatches": 0,
        "source_changed_during_capture": 0,
        "privacy_or_process_hits": 0,
        "authority_scan_included": False,
        "source_images_included": False,
        "cumulative_sections_1_21_claimed": False,
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
        (path for path in destination.rglob("*") if path.is_file() and path != manifest_path),
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

