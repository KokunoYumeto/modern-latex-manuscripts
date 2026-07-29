#!/usr/bin/env python3
"""Build a compact public custody package for the paused EGA II work."""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
import shutil
import zipfile
from pathlib import Path, PurePosixPath

from pypdf import PdfReader


REPO = Path(__file__).resolve().parents[1]
OUTPUT = (
    REPO
    / "sources"
    / "ega"
    / "checkpoints"
    / "ega2-source-aligned-through-4-4-5-working-20260729"
)
PDF_NAME = "00a_EGA2_English_Layered_Working_Reader_Through_4_4_5_20260729.pdf"
TEX_NAME = "02a_EGA2_English_Layered_Working_Master_Through_4_4_5_20260729.tex"
ZIP_NAME = "10a_EGA2_English_Layered_Working_Source_Through_4_4_5_20260729.zip"
ZIP_TIME = (2026, 7, 29, 0, 0, 0)
PRIVATE_MARKERS = (
    b"c:\\users\\",
    b"c:/users/",
    b"c:\\il_github",
    b"papors",
    b"chatnotes",
    b".claude",
    b".codex",
    b"source_thread_id",
    b"thread_id",
)
PROCESS_PATTERNS = (
    r"\bChatGPT\b",
    r"\bClaude\b",
    r"\bCodex\b",
    r"\bOpenAI\b",
    r"\bLLM\b",
    r"AI-generated",
    r"machine-assisted",
    r"production status",
    r"source status",
    r"pending review",
    r"workflow status",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source",
        required=True,
        type=Path,
        help="Exact EGA II source-aligned working root.",
    )
    return parser.parse_args()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def identity(path: Path) -> dict[str, object]:
    return {"bytes": path.stat().st_size, "sha256": sha256(path)}


def safe_member(name: str) -> bool:
    pure = PurePosixPath(name)
    return (
        bool(name)
        and not pure.is_absolute()
        and ".." not in pure.parts
        and "\\" not in name
        and re.match(r"^[A-Za-z]:", name) is None
    )


def zip_info(name: str) -> zipfile.ZipInfo:
    info = zipfile.ZipInfo(name, date_time=ZIP_TIME)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.create_system = 3
    info.external_attr = 0o100644 << 16
    return info


def csv_bytes(rows: list[dict[str, object]], fields: list[str]) -> bytes:
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return buffer.getvalue().encode("utf-8")


def selected_source_files(root: Path) -> list[Path]:
    source = root / "source"
    selected = [
        source / "ega2.tex",
        source / "preamble-base.tex",
        source / "preamble.tex",
        source / "the.bib",
    ]
    selected.extend(sorted((source / "ega2").glob("ega2-*.tex")))
    missing = [path for path in selected if not path.is_file()]
    if missing:
        raise FileNotFoundError(f"missing source dependencies: {missing}")
    if len(selected) != 12:
        raise RuntimeError(f"expected 12 source files, found {len(selected)}")
    return selected


def scan_private(items: dict[str, bytes]) -> list[dict[str, str]]:
    hits: list[dict[str, str]] = []
    for name, data in items.items():
        lowered = data.lower()
        for marker in PRIVATE_MARKERS:
            if marker in lowered:
                hits.append(
                    {
                        "path": name,
                        "marker": marker.decode("ascii", errors="replace"),
                    }
                )
    return hits


def scan_text_process(name: str, text: str) -> list[dict[str, str]]:
    hits = []
    for pattern in PROCESS_PATTERNS:
        if re.search(pattern, text, flags=re.IGNORECASE):
            hits.append({"path": name, "pattern": pattern})
    return hits


def pdf_metrics(path: Path) -> dict[str, object]:
    reader = PdfReader(path)
    process_hits: list[dict[str, object]] = []
    goto = 0
    invalid = 0
    for page_number, page in enumerate(reader.pages, 1):
        text = " ".join((page.extract_text() or "").split())
        for hit in scan_text_process(f"page-{page_number}", text):
            process_hits.append({"page": page_number, "pattern": hit["pattern"]})
        for annotation_ref in page.get("/Annots") or []:
            annotation = annotation_ref.get_object()
            action = annotation.get("/A")
            destination = annotation.get("/Dest")
            if action and action.get("/S") == "/GoTo":
                goto += 1
                if action.get("/D") is None:
                    invalid += 1
            elif destination is not None:
                goto += 1
    return {
        "pages": len(reader.pages),
        "named_destinations": len(reader.named_destinations),
        "internal_goto_actions": goto,
        "invalid_actions": invalid,
        "reader_process_hits": process_hits,
    }


def public_readme(pdf: Path, master: Path) -> str:
    return f"""# EGA II English layered working reader

This checkpoint preserves the paused EGA II English source-alignment work at
an exact, buildable boundary.

## Admitted source-aligned scope

- Opening of EGA II through Corollary 4.4.5, inclusive.
- Exact continuation: Proposition 4.4.6.
- Authority position at the continuation: NUMDAM physical page 77, printed
  page 80.
- Editable continuation: `source/ega2/ega2-4.tex`, line 529.

The inherited English beyond that cursor remains in the layered reader so the
volume can be read and built, but it is not admitted as source-aligned by this
checkpoint. This is a working scholarly reader, not a critical edition,
rights clearance, peer review, or whole-volume source-fidelity claim.

## Direct files

- Reader: `{PDF_NAME}`, 151 pages, {pdf.stat().st_size} bytes,
  SHA-256 `{sha256(pdf)}`.
- Master TeX: `{TEX_NAME}`, {master.stat().st_size} bytes,
  SHA-256 `{sha256(master)}`.
- Complete source package: `{ZIP_NAME}`.

The source ZIP contains the master, both preambles, bibliography, all eight
chapter components, the same reader PDF, and exact public controls. It
excludes the French authority, generated `$out` files, raw logs, rendered
page PNGs, private paths, and transient build files.

The French NUMDAM reader is identified by SHA-256
`111834EFFFE9E90D068389D418F08925A82B4A54AE2957F080712D4180E032EB`
but is not redistributed. Underlying rights remain with their holders; this
package asserts no new blanket license.
"""


def status_text() -> str:
    return """# Source-alignment status

State: paused at a clean source-aligned checkpoint.

- Admitted English scope: opening through Corollary 4.4.5, inclusive.
- Resume cursor: Proposition 4.4.6.
- Authority coordinate: physical page 77 / printed page 80.
- Editable coordinate: `source/ega2/ega2-4.tex`, line 529.

Later inherited English is retained for layered reading and build continuity
but has not yet passed the source-alignment gate.
"""


def build_summary(root: Path, pdf: Path) -> str:
    log = root / "build" / "through_4_4_5_r29" / "ega2.log"
    pass3 = root / "build" / "through_4_4_5_r29" / "console_pass3.txt"
    return f"""# Public build summary

- XeLaTeX passes: three consecutive successful passes.
- Fatal or error-pattern count: zero.
- Reader pages: 151.
- Reader SHA-256: `{sha256(pdf)}`.
- Internal build-log SHA-256: `{sha256(log)}`.
- Internal final-console SHA-256: `{sha256(pass3)}`.
- Manual seam review: reader pages 59-60 through Corollary 4.4.5 and the
  intact transition into Proposition 4.4.6.

Raw logs and rendered page PNGs are excluded from this compact public
package because they add no mathematical content and can expose local build
details.
"""


def build_source_zip(
    destination: Path,
    root: Path,
    source_files: list[Path],
    pdf: Path,
    readme: str,
) -> dict[str, object]:
    members: dict[str, bytes] = {}
    source_root = root / "source"
    for path in source_files:
        name = "source/" + path.relative_to(source_root).as_posix()
        members[name] = path.read_bytes()
    members["reader/" + PDF_NAME] = pdf.read_bytes()
    members["README.md"] = readme.encode("utf-8")
    members["SOURCE_ALIGNMENT_STATUS.md"] = status_text().encode("utf-8")
    members["BUILD_SUMMARY_PUBLIC.md"] = build_summary(root, pdf).encode("utf-8")

    privacy_hits = scan_private(
        {name: data for name, data in members.items() if not name.endswith(".pdf")}
    )
    process_hits: list[dict[str, str]] = []
    for name, data in members.items():
        if name.endswith((".tex", ".bib", ".md")):
            process_hits.extend(
                scan_text_process(name, data.decode("utf-8", errors="replace"))
            )
    if privacy_hits or process_hits:
        raise RuntimeError(
            f"public text scan failed: privacy={privacy_hits}, process={process_hits}"
        )

    manifest_rows = [
        {
            "relative_path": name,
            "bytes": len(data),
            "sha256": sha256_bytes(data),
        }
        for name, data in sorted(members.items(), key=lambda item: item[0].casefold())
    ]
    members["SHA256SUMS.csv"] = csv_bytes(
        manifest_rows, ["relative_path", "bytes", "sha256"]
    )

    with zipfile.ZipFile(destination, "w", allowZip64=True) as archive:
        for name, data in sorted(members.items(), key=lambda item: item[0].casefold()):
            if not safe_member(name):
                raise RuntimeError(f"unsafe ZIP member: {name}")
            archive.writestr(
                zip_info(name),
                data,
                compress_type=zipfile.ZIP_DEFLATED,
                compresslevel=9,
            )

    errors: list[str] = []
    with zipfile.ZipFile(destination) as archive:
        if archive.testzip():
            errors.append("CRC failure")
        names = archive.namelist()
        if len(names) != len(set(names)):
            errors.append("duplicate member")
        if set(names) != set(members):
            errors.append("member-set mismatch")
        for name in names:
            if not safe_member(name):
                errors.append(f"unsafe member: {name}")
            if sha256_bytes(archive.read(name)) != sha256_bytes(members[name]):
                errors.append(f"member hash mismatch: {name}")
        uncompressed = sum(info.file_size for info in archive.infolist())
    if errors:
        raise RuntimeError("\n".join(errors))

    return {
        "filename": destination.name,
        "bytes": destination.stat().st_size,
        "sha256": sha256(destination),
        "members": len(members),
        "uncompressed_bytes": uncompressed,
        "manifest_rows": len(manifest_rows),
        "manifest_sha256": sha256_bytes(members["SHA256SUMS.csv"]),
        "privacy_hits": privacy_hits,
        "process_hits": process_hits,
        "member_readback": "PASS",
    }


def write_outer_manifest() -> None:
    represented = [
        OUTPUT / PDF_NAME,
        OUTPUT / TEX_NAME,
        OUTPUT / ZIP_NAME,
        OUTPUT / "PACKAGE_VALIDATION.json",
        OUTPUT / "README.md",
    ]
    rows = [
        {
            "relative_path": path.name,
            "bytes": path.stat().st_size,
            "sha256": sha256(path),
        }
        for path in represented
    ]
    (OUTPUT / "SHA256SUMS.csv").write_bytes(
        csv_bytes(rows, ["relative_path", "bytes", "sha256"])
    )


def main() -> None:
    args = parse_args()
    root = args.source.resolve()
    if not root.is_dir():
        raise SystemExit(f"source root does not exist: {root}")
    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    OUTPUT.mkdir(parents=True)

    source_files = selected_source_files(root)
    source_pdf = root / "build" / "through_4_4_5_r29" / "ega2.pdf"
    source_master = root / "source" / "ega2.tex"
    if not source_pdf.is_file():
        raise FileNotFoundError(source_pdf)

    pdf_target = OUTPUT / PDF_NAME
    tex_target = OUTPUT / TEX_NAME
    shutil.copyfile(source_pdf, pdf_target)
    shutil.copyfile(source_master, tex_target)

    readme = public_readme(pdf_target, tex_target)
    (OUTPUT / "README.md").write_text(readme, encoding="utf-8", newline="\n")
    zip_result = build_source_zip(
        OUTPUT / ZIP_NAME, root, source_files, pdf_target, readme
    )
    metrics = pdf_metrics(pdf_target)
    if metrics["pages"] != 151 or metrics["invalid_actions"]:
        raise RuntimeError(f"unexpected PDF metrics: {metrics}")
    if metrics["reader_process_hits"]:
        raise RuntimeError(f"reader process text found: {metrics['reader_process_hits']}")

    validation = {
        "status": "PASS",
        "errors": [],
        "scope": "EGA II layered English reader, source-aligned through Corollary 4.4.5",
        "continuation": {
            "unit": "Proposition 4.4.6",
            "authority_physical_page": 77,
            "authority_printed_page": 80,
            "editable_path": "source/ega2/ega2-4.tex",
            "editable_line": 529,
        },
        "direct_reader": {**identity(pdf_target), **metrics},
        "direct_master": identity(tex_target),
        "selected_source_files": len(source_files),
        "selected_source_bytes": sum(path.stat().st_size for path in source_files),
        "source_zip": zip_result,
        "authority": {
            "description": "EGA II French original, NUMDAM PMIHES 8 (1961)",
            "sha256": (
                "111834EFFFE9E90D068389D418F08925A82B4A54AE2957F080712D4180E032EB"
            ),
            "redistributed": False,
        },
        "excluded": [
            "French authority PDF",
            "generated source/$out subtree",
            "raw logs and console output",
            "rendered page PNGs",
            "private paths",
            "transient build files",
        ],
        "disposition": {
            "github_custody": "READY",
            "zenodo_same_concept_successor": "ELIGIBLE_WITH_LAYERED_SCOPE_LABEL",
            "whole_volume_source_alignment": False,
        },
    }
    (OUTPUT / "PACKAGE_VALIDATION.json").write_text(
        json.dumps(validation, indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    write_outer_manifest()

    result = {
        "output": str(OUTPUT),
        "outer_files": len(list(OUTPUT.iterdir())),
        "outer_bytes": sum(path.stat().st_size for path in OUTPUT.iterdir()),
        "reader": identity(pdf_target),
        "master": identity(tex_target),
        "source_zip": zip_result,
        "outer_manifest_sha256": sha256(OUTPUT / "SHA256SUMS.csv"),
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
