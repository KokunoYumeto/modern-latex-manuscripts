#!/usr/bin/env python3
"""Build the compact EGA IV Sections 1-2 source-aligned custody ZIP."""

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
    "ega4-sections1-2-source-aligned-custody-20260729"
)
PACKAGE_ROOT = REPO_ROOT / PACKAGE_REL
ZIP_NAME = "10d_EGA4_Sections1_2_SourceAligned_Inputs_20260729.zip"

SECTION1_ROOT = Path(
    r"C:\Users\Floris\Documents\interlanguage\03_projects"
    r"\language_management\english_germanic\03_working_translations"
    r"\ega4_section01_source_aligned_successor_r1_20260728"
)
SECTION2_ROOT = Path(
    r"C:\Users\Floris\Documents\interlanguage\03_projects"
    r"\language_management\english_germanic\03_working_translations"
    r"\ega4_section02_source_aligned_successor_r1_20260729"
)

SECTION_INPUTS = {
    "section01": {
        "source": SECTION1_ROOT
        / "source"
        / "ega4-1.source_aligned_r1.tex",
        "source_expected": (
            103_000,
            "90B6C4A37CB2CE60A830FCC38D0664655B7AC25980B89E5568BF159A12F846D2",
        ),
        "reader": SECTION1_ROOT
        / "build_section110_r2"
        / "ega4_section01_source_aligned_r1.pdf",
        "reader_expected": (
            337_715,
            "62E2BBFA110D4CFFDC5F90143665EF5A73F3D6CC8047FB709668DF3B51E65307",
            21,
        ),
        "control_root": SECTION1_ROOT / "controls",
        "excluded_controls": {"PREDECESSOR_SHA256.csv"},
        "scope": "EGA IV Section 1, subsections 1.1-1.10",
    },
    "section02": {
        "source": SECTION2_ROOT
        / "source"
        / "ega4-2.source_aligned_r1.tex",
        "source_expected": (
            125_678,
            "E5A5FAC2A678E4A7A000699AE310449520E0185E62E17AE7BE446D2583EA5FEB",
        ),
        "reader": SECTION2_ROOT
        / "build_harness"
        / "build_section28_r1c"
        / "ega4_section02_source_aligned_r1.pdf",
        "reader_expected": (
            195_761,
            "2D90857B016F25AE3F1B4A1775885ECE72E15A6CEC96C9BCE4F75ACA71C729F7",
            27,
        ),
        "control_root": SECTION2_ROOT / "controls",
        "excluded_controls": {"BASELINE_IDENTITY.json"},
        "scope": "EGA IV Section 2, subsections 2.1-2.8",
    },
}

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
    return (
        json.dumps(value, indent=2, ensure_ascii=True).encode("utf-8")
        + b"\n"
    )


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
    for path in sorted(SECTION2_ROOT.rglob("*.png")):
        relative = path.relative_to(SECTION2_ROOT).as_posix()
        lower = relative.casefold()
        authority_derived = "authority" in lower
        with Image.open(path) as image:
            width, height = image.size
            mode = image.mode
            dpi = png_dpi(image)
        rows.append(
            {
                "visual_id": f"EGA4-S2-VIS-{len(rows) + 1:04d}",
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
                    else SECTION_INPUTS["section02"]["reader_expected"][1]
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


def assert_identity(
    path: Path,
    expected: tuple[int, str],
    label: str,
) -> None:
    if identity(path) != expected:
        raise RuntimeError(f"{label} identity mismatch")


def source_members() -> tuple[dict[str, bytes], dict[str, object]]:
    members: dict[str, bytes] = {}
    summary: dict[str, object] = {}
    for section, row in SECTION_INPUTS.items():
        source = row["source"]
        reader = row["reader"]
        assert_identity(source, row["source_expected"], f"{section} source")
        assert_identity(
            reader,
            row["reader_expected"][:2],
            f"{section} reader",
        )
        pages = len(PdfReader(str(reader)).pages)
        if pages != row["reader_expected"][2]:
            raise RuntimeError(f"{section} reader page-count mismatch")

        members[f"{section}/source/{source.name}"] = source.read_bytes()
        reader_name = (
            f"EGA4_{section.title()}_English_SourceAligned.pdf"
        )
        members[f"{section}/reader/{reader_name}"] = reader.read_bytes()

        control_paths = sorted(
            path
            for path in row["control_root"].iterdir()
            if path.is_file()
            and path.suffix.casefold() in {".csv", ".json"}
            and path.name not in row["excluded_controls"]
        )
        for path in control_paths:
            members[
                f"{section}/controls/{path.name}"
            ] = path.read_bytes()

        summary[section] = {
            "scope": row["scope"],
            "source": {
                "bytes": row["source_expected"][0],
                "sha256": row["source_expected"][1],
            },
            "reader": {
                "pages": row["reader_expected"][2],
                "bytes": row["reader_expected"][0],
                "sha256": row["reader_expected"][1],
            },
            "control_files": len(control_paths),
        }
    return members, summary


def assert_text_hygiene(members: dict[str, bytes]) -> dict[str, object]:
    hits: list[dict[str, str]] = []
    scanned = 0
    for name, data in members.items():
        if Path(name).suffix.casefold() not in {
            ".csv",
            ".json",
            ".md",
            ".tex",
        }:
            continue
        scanned += 1
        text = data.decode("utf-8-sig", errors="replace")
        for pattern in PRIVACY_PATTERNS:
            if pattern.casefold() in text.casefold():
                hits.append({"path": name, "pattern": pattern})
    if hits:
        raise RuntimeError(f"Text hygiene hits: {hits}")
    return {"text_members_scanned": scanned, "hits": [], "hit_count": 0}


def build() -> dict[str, object]:
    if PACKAGE_ROOT.exists():
        shutil.rmtree(PACKAGE_ROOT)
    PACKAGE_ROOT.mkdir(parents=True)

    members, sections = source_members()
    ledger, visual_counts = visual_ledger()
    members["VISUAL_EVIDENCE_DISPOSITION.csv"] = ledger

    provenance = "\n".join(
        [
            "# Provenance and rights",
            "",
            "The controlling authority is the NUMDAM EGA IV Part 2 French PDF.",
            f"- bytes: {AUTHORITY['bytes']}",
            f"- SHA-256: `{AUTHORITY['sha256']}`",
            "",
            "The authority PDF and authority-derived crops are not included.",
            "The editable English files are source-aligned working successors.",
            "This package grants no new rights in the underlying French work.",
            "Pre-existing user-supplied OCR was used only as a read-only locator",
            "and drafting witness; the source image remained authoritative.",
            "",
            "This is a bounded Sections 1-2 integration input, not a complete",
            "EGA IV edition or a critical edition. Section 3 is the next cursor.",
            "",
        ]
    ).encode("utf-8")
    members["PROVENANCE_AND_RIGHTS.md"] = provenance

    readme = "\n".join(
        [
            "# EGA IV Sections 1-2 source-aligned integration inputs",
            "",
            "This archive preserves the completed source-aligned English",
            "successors for EGA IV Sections 1 and 2 in one compact package.",
            "",
            "- Section 1: subsections 1.1-1.10, 21-page bounded reader.",
            "- Section 2: subsections 2.1-2.8, 27-page bounded reader.",
            "- Editable TeX and exact machine validation controls are included.",
            "- Six native diagrams have direct lead high-zoom authority review.",
            "- Authority scans and redundant target renders are not included.",
            "- The visual ledger preserves all 76 on-disk PNG identities and",
            "  records their rights or redundancy disposition.",
            "- Continuation: EGA IV Section 3.",
            "",
            "The package is an off-PC integration input. It is not a complete",
            "EGA IV reader, rights determination, or critical-edition claim.",
            "",
        ]
    ).encode("utf-8")
    members["README.md"] = readme

    member_rows = [
        {
            "relative_path": name,
            "bytes": len(data),
            "sha256": sha256_bytes(data),
        }
        for name, data in sorted(
            members.items(),
            key=lambda item: item[0].casefold(),
        )
    ]
    members["SHA256SUMS.csv"] = csv_bytes(
        ["relative_path", "bytes", "sha256"],
        member_rows,
    )
    hygiene = assert_text_hygiene(members)

    validation = {
        "schema": "ega4_sections1_2_source_aligned_custody_v1",
        "status": "PASS_GITHUB_CUSTODY_READY",
        "errors": [],
        "scope": "EGA IV Sections 1-2",
        "continuation": "EGA IV Section 3",
        "sections": sections,
        "authority": AUTHORITY,
        "visual_evidence": {
            **visual_counts,
            "pixels_included": 0,
            "ledger": "VISUAL_EVIDENCE_DISPOSITION.csv",
        },
        "text_hygiene": hygiene,
        "complete_ega_iv_claim": False,
        "critical_edition_claim": False,
        "new_rights_grant": False,
    }
    members["PACKAGE_VALIDATION.json"] = json_bytes(validation)

    zip_path = PACKAGE_ROOT / ZIP_NAME
    deterministic_zip(zip_path, members)
    first_identity = identity(zip_path)

    with tempfile.TemporaryDirectory() as temp:
        second = Path(temp) / ZIP_NAME
        deterministic_zip(second, members)
        if identity(second) != first_identity:
            raise RuntimeError("Deterministic ZIP replay mismatch")

    with zipfile.ZipFile(zip_path, "r") as archive:
        if archive.testzip() is not None:
            raise RuntimeError("ZIP CRC failure")
        names = archive.namelist()
        if names != sorted(members, key=str.casefold):
            raise RuntimeError("ZIP member order mismatch")
        for name, data in members.items():
            if archive.read(name) != data:
                raise RuntimeError(f"ZIP member readback mismatch: {name}")

    outer_readme = "\n".join(
        [
            "# EGA IV Sections 1-2 source-aligned custody",
            "",
            "One deterministic ZIP preserves the completed bounded Section 1",
            "and Section 2 English source-aligned inputs without adding loose",
            "fragment readers to the public landing surface.",
            "",
            f"- ZIP: `{ZIP_NAME}`",
            f"- ZIP bytes: {first_identity[0]}",
            f"- ZIP SHA-256: `{first_identity[1]}`",
            f"- ZIP members: {len(members)}",
            f"- Uncompressed bytes: {sum(len(data) for data in members.values())}",
            "",
            "EGA IV Section 3 is active. A later cumulative reader should",
            "consume these exact inputs and replace the current reader only",
            "after its own build and public readback.",
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
            "uncompressed_bytes": sum(
                len(data) for data in members.values()
            ),
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
        csv_bytes(
            ["relative_path", "bytes", "sha256"],
            outer_rows,
        )
    )

    return {
        "status": "PASS_GITHUB_CUSTODY_READY",
        "package_root": str(PACKAGE_ROOT),
        "zip": {
            "bytes": first_identity[0],
            "sha256": first_identity[1],
            "members": len(members),
            "uncompressed_bytes": sum(
                len(data) for data in members.values()
            ),
        },
        "visual_evidence": visual_counts,
        "outer_files": len(list(PACKAGE_ROOT.iterdir())),
    }


if __name__ == "__main__":
    print(json.dumps(build(), indent=2))
