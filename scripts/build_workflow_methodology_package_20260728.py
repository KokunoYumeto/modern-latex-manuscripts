#!/usr/bin/env python3
"""Build the compact July 28 workflow methodology package and controls."""

from __future__ import annotations

import csv
import hashlib
import json
import re
import zipfile
from pathlib import Path

from pypdf import PdfReader


REPO_ROOT = Path(__file__).resolve().parent.parent
ROOT = (
    REPO_ROOT
    / "sources"
    / "workflow"
    / "ai-run-modern-latex-workflow-20260728"
)
SOURCE_ZIP = "03_AI_Run_Modern_LaTeX_Workflow_20260728_Source_Packet.zip"
MANIFEST = "98_WORKFLOW_RELEASE_MANIFEST.csv"
VALIDATION = "99_WORKFLOW_RELEASE_VALIDATION.json"

DIRECT_FILES = [
    "00_AI_Run_Modern_LaTeX_Manuscript_Workflow_Current_20260728.md",
    "00_AI_Run_Modern_LaTeX_Manuscript_Workflow_Current_20260728.pdf",
    "01_CLAUDE_DIAGRAM_COLD_REVERIFY_METHOD_20260728.md",
    "02_SGA_TRANSLATION_RESOURCE_EFFICIENCY_INCIDENT_NOTE_20260728.md",
    "04_SGA3_DIAGRAM_HIGH_ZOOM_FINAL_FIDELITY_CORRECTION_20260728.md",
    "99_WORKFLOW_PUBLIC_STATUS_20260728.md",
]
RETAINED_ADDENDA = (
    "01_Workflow_Docs_Addenda_Scripts_and_Cleanup_Log_20260706.zip"
)
EXPECTED_CLAUDE_SHA = (
    "4B12DB3F632CB5F9E69393DCA33DA40256B5A9387C6522ADA831CA7F0367063D"
)
EXPECTED_INCIDENT_SHA = (
    "11D05DC19EA55F568FDB1C2BBD3AD6DB5AA799002EFFD3604A5244BE325C7ACA"
)
EXPECTED_DIAGRAM_CORRECTION_SHA = (
    "D41B84EA82379F23693D5F9944B66D67AAAA2FB99F0A4AA430C40F61BE6FD8BE"
)
EXPECTED_ADDENDA_SHA = (
    "07F46DAC99916117A3499BEA1D651CCE4144B313B423ADB5E59DDC858C602288"
)
ZIP_TIMESTAMP = (2026, 7, 28, 0, 0, 0)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(4 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def identity(path: Path) -> dict:
    return {
        "bytes": path.stat().st_size,
        "sha256": sha256_file(path),
    }


def write_text(path: Path, value: str) -> None:
    path.write_text(value, encoding="utf-8", newline="\n")


def stable_zip_info(name: str) -> zipfile.ZipInfo:
    info = zipfile.ZipInfo(name, date_time=ZIP_TIMESTAMP)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = 0o100644 << 16
    info.create_system = 3
    return info


def scan_public_text() -> list[dict]:
    patterns = {
        "private_windows_path": re.compile(r"[A-Za-z]:\\Users\\", re.I),
        "private_project_path": re.compile(r"\b(?:Papors|Chatnotes)\b", re.I),
        "codex_private_path": re.compile(r"\\.codex(?:\\|/)", re.I),
        "task_id": re.compile(r"\b019f[0-9a-f-]{20,}\b", re.I),
        "profanity_or_slur": re.compile(
            r"\b(?:fuck(?:ing)?|shit|retard(?:ed)?)\b", re.I
        ),
    }
    hits = []
    for name in DIRECT_FILES:
        if not name.lower().endswith(".md"):
            continue
        text = (ROOT / name).read_text(encoding="utf-8-sig")
        for mode, pattern in patterns.items():
            for match in pattern.finditer(text):
                hits.append(
                    {
                        "filename": name,
                        "mode": mode,
                        "offset": match.start(),
                    }
                )
    return hits


def inspect_pdf(path: Path) -> dict:
    reader = PdfReader(str(path), strict=True)
    if len(reader.pages) != 7:
        raise RuntimeError("Workflow PDF must contain exactly seven pages")
    dimensions = []
    for index, page in enumerate(reader.pages, start=1):
        width = float(page.mediabox.width)
        height = float(page.mediabox.height)
        dimensions.append(
            {"page": index, "width_points": width, "height_points": height}
        )
        if abs(width - 595.28) > 0.1 or abs(height - 841.89) > 0.1:
            raise RuntimeError(
                f"Workflow PDF page {index} is not A4: {width} x {height}"
            )
    root = reader.trailer["/Root"]
    tagged = bool(root.get("/MarkInfo", {}).get("/Marked", False))
    xmp = root.get("/Metadata") is not None
    return {
        **identity(path),
        "pages": len(reader.pages),
        "page_size": "A4",
        "page_dimensions_points": dimensions,
        "tagged": tagged,
        "xmp_metadata_stream": xmp,
    }


def build_source_zip() -> dict:
    member_identities = {
        name: identity(ROOT / name)
        for name in DIRECT_FILES
    }
    buffer = []
    for name in sorted(member_identities, key=str.casefold):
        row = member_identities[name]
        buffer.append(
            {
                "relative_path": name,
                "bytes": row["bytes"],
                "sha256": row["sha256"],
            }
        )
    output = []
    stream = csv.DictWriter(
        output := _ListWriter(),
        fieldnames=("relative_path", "bytes", "sha256"),
        lineterminator="\n",
    )
    stream.writeheader()
    stream.writerows(buffer)
    checksums = "".join(output).encode("utf-8")

    path = ROOT / SOURCE_ZIP
    with zipfile.ZipFile(
        path,
        "w",
        compression=zipfile.ZIP_DEFLATED,
        compresslevel=9,
    ) as archive:
        for name in sorted(DIRECT_FILES, key=str.casefold):
            archive.writestr(
                stable_zip_info(name),
                (ROOT / name).read_bytes(),
                compress_type=zipfile.ZIP_DEFLATED,
                compresslevel=9,
            )
        archive.writestr(
            stable_zip_info("SHA256SUMS.csv"),
            checksums,
            compress_type=zipfile.ZIP_DEFLATED,
            compresslevel=9,
        )

    file_members = 0
    uncompressed = 0
    with zipfile.ZipFile(path, "r") as archive:
        if archive.testzip() is not None:
            raise RuntimeError("Source packet ZIP failed CRC")
        names = [row.filename for row in archive.infolist()]
        if names != sorted([*DIRECT_FILES, "SHA256SUMS.csv"], key=str.casefold):
            raise RuntimeError("Source packet ZIP member order or set mismatch")
        for info in archive.infolist():
            if info.is_dir():
                raise RuntimeError("Source packet unexpectedly contains a directory")
            file_members += 1
            uncompressed += info.file_size
            if info.filename in member_identities:
                content = archive.read(info.filename)
                observed = (
                    len(content),
                    hashlib.sha256(content).hexdigest().upper(),
                )
                wanted = (
                    member_identities[info.filename]["bytes"],
                    member_identities[info.filename]["sha256"],
                )
                if observed != wanted:
                    raise RuntimeError(
                        f"Source packet member mismatch: {info.filename}"
                    )
    return {
        "filename": SOURCE_ZIP,
        **identity(path),
        "members": file_members,
        "uncompressed_bytes": uncompressed,
        "internal_manifest_rows": len(DIRECT_FILES),
        "internal_manifest_sha256": hashlib.sha256(checksums).hexdigest().upper(),
    }


class _ListWriter:
    def __init__(self) -> None:
        self.parts: list[str] = []

    def write(self, value: str) -> int:
        self.parts.append(value)
        return len(value)

    def __iter__(self):
        return iter(self.parts)

    def __len__(self) -> int:
        return len(self.parts)

    def __getitem__(self, index):
        return self.parts[index]


def build_manifest(source_zip: dict) -> dict:
    roles = {
        DIRECT_FILES[0]: (
            "current_methodology_markdown",
            "professional July 28 workflow update",
            "current",
        ),
        DIRECT_FILES[1]: (
            "default_preview_pdf",
            "seven-page A4 rendering of the current methodology",
            "current_visual_qa_pass",
        ),
        DIRECT_FILES[2]: (
            "co_current_source_method",
            "exact Claude cold-reverify method artifact",
            "current_exact_source_artifact",
        ),
        DIRECT_FILES[3]: (
            "accountability_incident_note",
            "exact resource-efficiency incident note with scenario caveats",
            "current_exact_source_artifact",
        ),
        DIRECT_FILES[4]: (
            "controlling_diagram_fidelity_correction",
            "additive SGA3 native-TeX 300/5000/9000-dpi final-fidelity control",
            "current_controlling_correction",
        ),
        DIRECT_FILES[5]: (
            "public_status",
            "scope, claim boundary, and artifact-shape notice",
            "current",
        ),
        RETAINED_ADDENDA: (
            "historical_addenda_archive",
            "retained byte-identically from Zenodo record 21424987",
            "retained_history",
        ),
        SOURCE_ZIP: (
            "current_source_packet",
            "six-member deterministic source and checksum packet",
            "current_exact_archive",
        ),
    }
    rows = []
    for name in sorted(roles, key=str.casefold):
        row = identity(ROOT / name)
        role, provenance, status = roles[name]
        rows.append(
            {
                "filename": name,
                "bytes": row["bytes"],
                "sha256": row["sha256"],
                "role": role,
                "provenance": provenance,
                "status": status,
            }
        )
    path = ROOT / MANIFEST
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=(
                "filename",
                "bytes",
                "sha256",
                "role",
                "provenance",
                "status",
            ),
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)
    return {
        "filename": MANIFEST,
        **identity(path),
        "rows": len(rows),
    }


def main() -> None:
    for name in [*DIRECT_FILES, RETAINED_ADDENDA]:
        if not (ROOT / name).is_file():
            raise FileNotFoundError(ROOT / name)
    if sha256_file(ROOT / DIRECT_FILES[2]) != EXPECTED_CLAUDE_SHA:
        raise RuntimeError("Claude method identity changed")
    if sha256_file(ROOT / DIRECT_FILES[3]) != EXPECTED_INCIDENT_SHA:
        raise RuntimeError("Incident-note identity changed")
    if sha256_file(ROOT / DIRECT_FILES[4]) != EXPECTED_DIAGRAM_CORRECTION_SHA:
        raise RuntimeError("Diagram-correction identity changed")
    if sha256_file(ROOT / RETAINED_ADDENDA) != EXPECTED_ADDENDA_SHA:
        raise RuntimeError("Retained addenda identity changed")
    privacy_hits = scan_public_text()
    if privacy_hits:
        raise RuntimeError(f"Public-text hygiene hits: {privacy_hits}")
    pdf = inspect_pdf(ROOT / DIRECT_FILES[1])
    if pdf["tagged"] or pdf["xmp_metadata_stream"]:
        raise RuntimeError("Workflow PDF metadata/accessibility state changed")

    source_zip = build_source_zip()
    manifest = build_manifest(source_zip)
    validation = {
        "status": "PASS_READY_FOR_GITHUB_AND_SAME_CONCEPT_ZENODO",
        "errors": [],
        "date": "2026-07-28",
        "concept_doi": "10.5281/zenodo.20461174",
        "predecessor_record": 21633426,
        "release_policy": "same-concept successor; no duplicate concept",
        "outer_files": 10,
        "manifest": manifest,
        "default_preview": DIRECT_FILES[1],
        "pdf": {
            **pdf,
            "rendered_pages_reviewed": 7,
            "visual_qa": "PASS",
        },
        "claude_method": {
            **identity(ROOT / DIRECT_FILES[2]),
            "expected_sha256": EXPECTED_CLAUDE_SHA,
        },
        "incident_note": {
            **identity(ROOT / DIRECT_FILES[3]),
            "expected_sha256": EXPECTED_INCIDENT_SHA,
            "claim_boundary": (
                "scenario analysis, not metered OpenAI emissions telemetry"
            ),
        },
        "diagram_final_fidelity_correction": {
            **identity(ROOT / DIRECT_FILES[4]),
            "expected_sha256": EXPECTED_DIAGRAM_CORRECTION_SHA,
            "required_scale": (
                "300-dpi page context; about 5000-dpi default diagram/detail "
                "comparison; 9000-dpi targeted ambiguity crops"
            ),
            "ownership": "disjoint top-level-session range with lead signature",
            "prior_resolution_evidence": (
                "600/1200-dpi evidence remains valid history and context; "
                "reopen 300-only approvals or independently found defects"
            ),
            "public_diagram_format": "native editable TeX only",
            "raster_authority_witnesses": (
                "private; excluded from new public readers and payloads"
            ),
        },
        "retained_addenda": {
            **identity(ROOT / RETAINED_ADDENDA),
            "retained_byte_identically": True,
        },
        "source_packet": source_zip,
        "public_text_privacy_hygiene_hits": privacy_hits,
        "user_supplied_ocr_rule": (
            "read-only locator/drafting witness; do not generate, rerun, "
            "re-extract, or delegate"
        ),
        "new_license_grant": False,
    }
    save_path = ROOT / VALIDATION
    write_text(
        save_path,
        json.dumps(validation, ensure_ascii=True, indent=2) + "\n",
    )

    expected = {
        *DIRECT_FILES,
        RETAINED_ADDENDA,
        SOURCE_ZIP,
        MANIFEST,
        VALIDATION,
    }
    actual = {path.name for path in ROOT.iterdir() if path.is_file()}
    if actual != expected:
        raise RuntimeError(
            f"Package root mismatch: missing={sorted(expected - actual)}, "
            f"extra={sorted(actual - expected)}"
        )
    result = {
        "status": "PASS",
        "errors": [],
        "files": len(actual),
        "bytes": sum((ROOT / name).stat().st_size for name in actual),
        "manifest": manifest,
        "validation": {
            "bytes": save_path.stat().st_size,
            "sha256": sha256_file(save_path),
        },
        "source_packet": source_zip,
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
