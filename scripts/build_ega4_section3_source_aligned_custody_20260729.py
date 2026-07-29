#!/usr/bin/env python3
"""Build the compact EGA IV Section 3 source-aligned custody ZIP."""

from __future__ import annotations

import csv
import hashlib
import io
import json
import shutil
import tempfile
import zipfile
from pathlib import Path
from typing import Iterable

from PIL import Image
from pypdf import PdfReader


REPO_ROOT = Path(__file__).resolve().parent.parent
PACKAGE_REL = Path(
    "sources/ega/checkpoints/"
    "ega4-section3-source-aligned-custody-20260729"
)
PACKAGE_ROOT = REPO_ROOT / PACKAGE_REL
ZIP_NAME = "10e_EGA4_Section3_SourceAligned_Inputs_20260729.zip"

SECTION_ROOT = Path(
    r"C:\Users\Floris\Documents\interlanguage\03_projects"
    r"\language_management\english_germanic\03_working_translations"
    r"\ega4_section03_source_aligned_successor_r1_20260729"
)
SOURCE = SECTION_ROOT / "source" / "ega4-3.source_aligned_r1.tex"
SOURCE_EXPECTED = (
    65_449,
    "E966B5B350237661973C62DDC4DD9350344A6667B53E664B2094CAADDC143C1E",
)
READER = (
    SECTION_ROOT
    / "build_harness"
    / "build_section34_r2"
    / "ega4_section03_source_aligned_r1.pdf"
)
READER_EXPECTED = (
    120_570,
    "28372E459BA09F8C51BB0F467ECA25286189789B247649F73BED39C785D80213",
    13,
)
CONTROL_ROOT = SECTION_ROOT / "controls"
EXCLUDED_CONTROLS = {"BASELINE_IDENTITY.json"}
EXPECTED_CONTROL_FILES = 8

AUTHORITY = {
    "filename": "15 EGA IV Part 2 - French Original (NUMDAM PMIHES 24, 1965).pdf",
    "bytes": 31_819_022,
    "sha256": "C3E960AA1C5C37046E8892D8A3CAC098E2738164136B5CDAA5D5D893F89931DA",
    "disposition": "identity_only_not_redistributed",
}

PRIVACY_PATTERNS = (
    r"C:\Users",
    r"C:\IL_GitHub",
    "Papors",
    "Chatnotes",
    "Claude",
    "Codex",
    "OpenAI",
    "Anthropic",
    "source_thread_id",
    "thread_id",
)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(4 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def identity(path: Path) -> tuple[int, str]:
    return path.stat().st_size, sha256_file(path)


def json_bytes(value: object) -> bytes:
    return json.dumps(value, indent=2, ensure_ascii=True).encode("utf-8") + b"\n"


def csv_bytes(
    fieldnames: list[str],
    rows: Iterable[dict[str, object]],
) -> bytes:
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(
        stream,
        fieldnames=fieldnames,
        lineterminator="\n",
    )
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue().encode("utf-8")


def deterministic_zip(path: Path, members: dict[str, bytes]) -> None:
    with zipfile.ZipFile(
        path,
        "w",
        compression=zipfile.ZIP_DEFLATED,
        compresslevel=9,
    ) as archive:
        for name in sorted(members, key=str.casefold):
            info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            archive.writestr(info, members[name])


def png_dpi(image: Image.Image) -> str:
    value = image.info.get("dpi")
    if not value:
        return "not_recorded"
    return f"{value[0]:.2f}x{value[1]:.2f}"


def visual_ledger() -> tuple[bytes, dict[str, int]]:
    rows: list[dict[str, object]] = []
    for path in sorted(SECTION_ROOT.rglob("*.png")):
        relative = path.relative_to(SECTION_ROOT).as_posix()
        authority_derived = "authority" in relative.casefold()
        with Image.open(path) as image:
            width, height = image.size
            mode = image.mode
            dpi = png_dpi(image)
        rows.append(
            {
                "visual_id": f"EGA4-S3-VIS-{len(rows) + 1:04d}",
                "local_relative_path": relative,
                "bytes": path.stat().st_size,
                "sha256": sha256_file(path),
                "width_px": width,
                "height_px": height,
                "mode": mode,
                "dpi": dpi,
                "parent_sha256": (
                    AUTHORITY["sha256"]
                    if authority_derived
                    else READER_EXPECTED[1]
                ),
                "linked_scope": relative.split("/", 2)[1],
                "bounding_box": "not_recorded",
                "disposition": (
                    "manifest_only_rights_blocked"
                    if authority_derived
                    else "excluded_redundant_target_render"
                ),
                "pixels_public": "false",
            }
        )
    counts = {
        "total": len(rows),
        "rights_blocked": sum(
            row["disposition"] == "manifest_only_rights_blocked"
            for row in rows
        ),
        "redundant_target": sum(
            row["disposition"] == "excluded_redundant_target_render"
            for row in rows
        ),
    }
    if counts != {"total": 51, "rights_blocked": 20, "redundant_target": 31}:
        raise RuntimeError(f"EGA IV Section 3 visual boundary changed: {counts}")
    return (
        csv_bytes(
            [
                "visual_id",
                "local_relative_path",
                "bytes",
                "sha256",
                "width_px",
                "height_px",
                "mode",
                "dpi",
                "parent_sha256",
                "linked_scope",
                "bounding_box",
                "disposition",
                "pixels_public",
            ],
            rows,
        ),
        counts,
    )


def assert_text_hygiene(members: dict[str, bytes]) -> dict[str, object]:
    hits: list[dict[str, str]] = []
    scanned = 0
    for name, data in members.items():
        if Path(name).suffix.casefold() not in {".csv", ".json", ".md", ".tex"}:
            continue
        scanned += 1
        text = data.decode("utf-8-sig", errors="replace")
        for pattern in PRIVACY_PATTERNS:
            if pattern.casefold() in text.casefold():
                hits.append({"path": name, "pattern": pattern})
    if hits:
        raise RuntimeError(f"Text hygiene hits: {hits}")
    return {"text_members_scanned": scanned, "hits": [], "hit_count": 0}


def assert_reader_hygiene() -> dict[str, object]:
    reader = PdfReader(str(READER))
    metadata_text = json.dumps(
        {str(key): str(value) for key, value in (reader.metadata or {}).items()},
        ensure_ascii=True,
    )
    extracted = "\n".join(page.extract_text() or "" for page in reader.pages)
    hits = []
    for surface, text in (("metadata", metadata_text), ("text", extracted)):
        for pattern in PRIVACY_PATTERNS:
            if pattern.casefold() in text.casefold():
                hits.append({"surface": surface, "pattern": pattern})
    if hits:
        raise RuntimeError(f"Reader hygiene hits: {hits}")
    return {
        "pages": len(reader.pages),
        "metadata_and_text_hits": [],
        "hit_count": 0,
    }


def build() -> dict[str, object]:
    if identity(SOURCE) != SOURCE_EXPECTED:
        raise RuntimeError("EGA IV Section 3 source identity mismatch")
    if identity(READER) != READER_EXPECTED[:2]:
        raise RuntimeError("EGA IV Section 3 reader identity mismatch")
    if len(PdfReader(str(READER)).pages) != READER_EXPECTED[2]:
        raise RuntimeError("EGA IV Section 3 reader page count mismatch")
    if len(SOURCE.read_text(encoding="utf-8").splitlines()) != 985:
        raise RuntimeError("EGA IV Section 3 source line count mismatch")
    if "\\includegraphics" in SOURCE.read_text(encoding="utf-8"):
        raise RuntimeError("EGA IV Section 3 source still loads raster artwork")

    control_paths = sorted(
        path
        for path in CONTROL_ROOT.iterdir()
        if path.is_file()
        and path.suffix.casefold() in {".csv", ".json"}
        and path.name not in EXCLUDED_CONTROLS
    )
    if len(control_paths) != EXPECTED_CONTROL_FILES:
        raise RuntimeError("EGA IV Section 3 control boundary changed")
    for path in control_paths:
        if path.name.endswith("_FINAL_VALIDATION.json"):
            value = json.loads(path.read_text(encoding="utf-8"))
            if not str(value.get("status", "")).startswith("PASS") or value.get(
                "errors"
            ) != []:
                raise RuntimeError(f"Non-PASS Section 3 control: {path.name}")

    if PACKAGE_ROOT.exists():
        shutil.rmtree(PACKAGE_ROOT)
    PACKAGE_ROOT.mkdir(parents=True)

    members: dict[str, bytes] = {
        f"source/{SOURCE.name}": SOURCE.read_bytes(),
        "reader/EGA4_Section3_English_SourceAligned.pdf": READER.read_bytes(),
    }
    for path in control_paths:
        members[f"controls/{path.name}"] = path.read_bytes()

    ledger, visual_counts = visual_ledger()
    members["VISUAL_EVIDENCE_DISPOSITION.csv"] = ledger

    members["PROVENANCE_AND_RIGHTS.md"] = "\n".join(
        [
            "# Provenance and rights",
            "",
            "The controlling authority is the NUMDAM EGA IV Part 2 French PDF.",
            f"- bytes: {AUTHORITY['bytes']}",
            f"- SHA-256: `{AUTHORITY['sha256']}`",
            "",
            "The authority PDF and authority-derived crops are not included.",
            "The editable English file is a source-aligned working successor.",
            "This package grants no new rights in the underlying French work.",
            "Pre-existing user-supplied OCR was consulted read-only only as a",
            "locator and drafting witness; the source image remained authority.",
            "",
            "This is bounded Section 3 integration input, not a complete EGA IV",
            "edition or a critical edition. Section 4 is the next cursor.",
            "",
        ]
    ).encode("utf-8")
    members["README.md"] = "\n".join(
        [
            "# EGA IV Section 3 source-aligned integration input",
            "",
            "This archive preserves the completed source-aligned English",
            "successor for EGA IV Section 3 in one compact package.",
            "",
            "- Scope: subsections 3.1-3.4.",
            "- Reader: 13 A4 pages.",
            "- Editable TeX and eight exact machine controls are included.",
            "- The single diagram is native TeX and passed direct authority",
            "  review at native 600 ppi and vector-output 5000 dpi.",
            "- Authority scans and redundant target renders are not included.",
            "- The visual ledger preserves all 51 on-disk PNG identities.",
            "- Continuation: EGA IV Section 4.",
            "",
            "This is an off-PC integration input, not a complete EGA IV reader,",
            "rights determination, or critical-edition claim.",
            "",
        ]
    ).encode("utf-8")

    manifest_rows = [
        {
            "relative_path": name,
            "bytes": len(data),
            "sha256": sha256_bytes(data),
        }
        for name, data in sorted(members.items(), key=lambda item: item[0].casefold())
    ]
    members["SHA256SUMS.csv"] = csv_bytes(
        ["relative_path", "bytes", "sha256"],
        manifest_rows,
    )
    text_hygiene = assert_text_hygiene(members)
    reader_hygiene = assert_reader_hygiene()

    validation = {
        "schema": "ega4_section3_source_aligned_custody_v1",
        "status": "PASS_GITHUB_CUSTODY_READY",
        "errors": [],
        "scope": "EGA IV Section 3, subsections 3.1-3.4",
        "continuation": "EGA IV Section 4",
        "source": {
            "lines": 985,
            "bytes": SOURCE_EXPECTED[0],
            "sha256": SOURCE_EXPECTED[1],
        },
        "reader": {
            "pages": READER_EXPECTED[2],
            "bytes": READER_EXPECTED[0],
            "sha256": READER_EXPECTED[1],
        },
        "controls": {
            "files": len(control_paths),
            "final_validations": 4,
            "errors": [],
        },
        "native_diagrams": 1,
        "raster_loads": 0,
        "authority": AUTHORITY,
        "visual_evidence": {
            **visual_counts,
            "pixels_included": 0,
            "ledger": "VISUAL_EVIDENCE_DISPOSITION.csv",
        },
        "text_hygiene": text_hygiene,
        "reader_hygiene": reader_hygiene,
        "complete_ega_iv_claim": False,
        "critical_edition_claim": False,
        "new_rights_grant": False,
    }
    members["PACKAGE_VALIDATION.json"] = json_bytes(validation)

    zip_path = PACKAGE_ROOT / ZIP_NAME
    deterministic_zip(zip_path, members)
    first_identity = identity(zip_path)
    with tempfile.TemporaryDirectory() as temp:
        replay = Path(temp) / ZIP_NAME
        deterministic_zip(replay, members)
        if identity(replay) != first_identity:
            raise RuntimeError("Deterministic EGA IV Section 3 ZIP mismatch")

    with zipfile.ZipFile(zip_path) as archive:
        if archive.testzip() is not None:
            raise RuntimeError("EGA IV Section 3 ZIP CRC failure")
        if archive.namelist() != sorted(members, key=str.casefold):
            raise RuntimeError("EGA IV Section 3 ZIP member order mismatch")
        for name, data in members.items():
            if archive.read(name) != data:
                raise RuntimeError(f"ZIP member readback mismatch: {name}")

    outer_readme = "\n".join(
        [
            "# EGA IV Section 3 source-aligned custody",
            "",
            "One deterministic ZIP preserves the completed bounded Section 3",
            "English source-aligned integration input without adding a fragment",
            "reader to the public landing surface.",
            "",
            f"- ZIP: `{ZIP_NAME}`",
            f"- ZIP bytes: {first_identity[0]}",
            f"- ZIP SHA-256: `{first_identity[1]}`",
            f"- ZIP members: {len(members)}",
            f"- Uncompressed bytes: {sum(len(data) for data in members.values())}",
            "",
            "EGA IV Section 4 is active. A later cumulative reader should consume",
            "this exact input and replace the current reader only after its own",
            "build and public readback.",
            "",
        ]
    ).encode("utf-8")
    (PACKAGE_ROOT / "README.md").write_bytes(outer_readme)

    outer_validation = {
        **validation,
        "zip": {
            "filename": ZIP_NAME,
            "bytes": first_identity[0],
            "sha256": first_identity[1],
            "members": len(members),
            "uncompressed_bytes": sum(len(data) for data in members.values()),
            "deterministic_rebuild": True,
            "member_readback": "PASS",
        },
    }
    (PACKAGE_ROOT / "PACKAGE_VALIDATION.json").write_bytes(
        json_bytes(outer_validation)
    )
    outer_rows = []
    for path in sorted(PACKAGE_ROOT.iterdir(), key=lambda item: item.name):
        if path.name == "SHA256SUMS.csv":
            continue
        outer_rows.append(
            {
                "relative_path": path.name,
                "bytes": path.stat().st_size,
                "sha256": sha256_file(path),
            }
        )
    (PACKAGE_ROOT / "SHA256SUMS.csv").write_bytes(
        csv_bytes(["relative_path", "bytes", "sha256"], outer_rows)
    )

    return {
        "status": "PASS_GITHUB_CUSTODY_READY",
        "package_root": str(PACKAGE_ROOT),
        "zip": {
            "bytes": first_identity[0],
            "sha256": first_identity[1],
            "members": len(members),
            "uncompressed_bytes": sum(len(data) for data in members.values()),
        },
        "visual_evidence": visual_counts,
        "outer_files": len(list(PACKAGE_ROOT.iterdir())),
    }


if __name__ == "__main__":
    print(json.dumps(build(), indent=2))
