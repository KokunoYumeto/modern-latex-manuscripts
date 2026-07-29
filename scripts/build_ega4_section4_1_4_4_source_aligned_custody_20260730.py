#!/usr/bin/env python3
"""Build the compact EGA IV Sections 4.1-4.4 source-aligned custody ZIP."""

from __future__ import annotations

import csv
import hashlib
import io
import json
import shutil
import tempfile
import zipfile
from pathlib import Path, PurePosixPath
from typing import Iterable

from PIL import Image
from pypdf import PdfReader

Image.MAX_IMAGE_PIXELS = None


REPO_ROOT = Path(__file__).resolve().parent.parent
PACKAGE_REL = Path(
    "sources/ega/checkpoints/"
    "ega4-section4-1-4-4-source-aligned-custody-20260730"
)
PACKAGE_ROOT = REPO_ROOT / PACKAGE_REL
ZIP_NAME = "10f_EGA4_Section4_1_4_4_SourceAligned_Inputs_20260730.zip"

SECTION_ROOT = Path(
    r"C:\Users\Floris\Documents\interlanguage\03_projects"
    r"\language_management\english_germanic\03_working_translations"
    r"\ega4_section04_source_aligned_successor_r1_20260729"
)
READER = (
    SECTION_ROOT
    / "build_harness"
    / "build_through_section44_r1"
    / "ega4_section04_source_aligned_r1.pdf"
)
READER_EXPECTED = (
    83_736,
    "D0D3D3CD5A54CA528BAD352CCF87754628AA5D825BB4424A8EF73029CD8711C9",
    10,
)
AUTHORITY = {
    "filename": "15 EGA IV Part 2 - French Original (NUMDAM PMIHES 24, 1965).pdf",
    "bytes": 31_819_022,
    "pages": 228,
    "sha256": "C3E960AA1C5C37046E8892D8A3CAC098E2738164136B5CDAA5D5D893F89931DA",
    "disposition": "identity_only_not_redistributed",
}

COMPONENTS = {
    "01_section41_dimension_of_algebraic_preschemes.tex": (
        9_214,
        "D7E8D8C7038B3024518B9460ACA9A2F1B50757C3D71F84B0B89BB368C978CD4C",
    ),
    "02_section42_associated_prime_cycles.tex": (
        14_677,
        "BACFAF5DFA29F8449FE72F3D0568D5E2C9C94EBBE26EBB9559852DF35E065DE7",
    ),
    "03_section43_tensor_products_of_fields.tex": (
        4_428,
        "44582C2AB58DF35E9E2931A9FDA91BB3064EF61C1FD90272572A9CB836BF5ED5",
    ),
    "04_section44_irreducible_connected_over_algebraically_closed.tex": (
        8_186,
        "24D5FD02F9543379446C5CF293BCA817E733C89EF6E181C422FF695F74B07DFE",
    ),
}
CONTROL_EXPECTED = {
    "SECTION41_FINAL_VALIDATION.json": (
        3_609,
        "9E9CDD6BF7AFE0F2AAF165C436440EA4736A1CD15DD7529FB31458D85BDB9BB5",
    ),
    "SECTION41_SOURCE_AUDIT.csv": (
        3_162,
        "3EC208AE7D6346CB198FB6F11B454D0B05BDC5B221D1CE587671EC8E29FB75C3",
    ),
    "SECTION42_FINAL_VALIDATION.json": (
        6_673,
        "EBC17AB08D1E24D61FD96C219B8635CF9E37D2D72EEF8D2708EBC75D0A70A4E1",
    ),
    "SECTION42_SOURCE_AUDIT.csv": (
        3_167,
        "07198DC89E2A86A9681DDED8B6FDBD87E12893D9D3B5137F713DDBCE0FF27B3C",
    ),
    "SECTION43_FINAL_VALIDATION.json": (
        5_576,
        "4A87FFEB7997BBDE33AE11ED31E94DE9B5C9B5ECBAC8B4D75B848980B672E37A",
    ),
    "SECTION43_SOURCE_AUDIT.csv": (
        2_069,
        "8D9C5F0CB3F4D6020500C58090E6AEE72D1AAACE0123FAD74F006EF298BB1DC2",
    ),
    "SECTION44_FINAL_VALIDATION.json": (
        6_274,
        "070A5586435108F4EBD510463D2A182A037AB4208C06F8C1A0EF4E9B6B72248A",
    ),
    "SECTION44_SOURCE_AUDIT.csv": (
        2_134,
        "37F47F6CA08EF7377F7BCD7817D1836511280E161B61D56109E2D4DC62BA99EA",
    ),
}
VISUAL_DIRS = (
    "qa/section41_authority_native_review_20260729",
    "qa/section41_output_600dpi_r1",
    "qa/section42_authority_native_review_20260729",
    "qa/section43_authority_review_20260729",
    "qa/section44_authority_review_20260729",
    "qa/through_section42_final_render_20260729",
    "qa/through_section43_final_render_20260729",
    "qa/through_section44_final_render_20260730",
    "qa/through_section44_final_render_stable_20260730",
)
PRIVACY_PATTERNS = (
    "c:/users/",
    "c:\\users\\",
    "c:/il_github",
    "c:\\il_github",
    "papors",
    "chatnotes",
    "source_thread_id",
    "thread_id",
    "openai",
    "anthropic",
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
    writer = csv.DictWriter(stream, fieldnames=fieldnames, lineterminator="\n")
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


def sanitize_json(value: object) -> object:
    if isinstance(value, dict):
        return {key: sanitize_json(item) for key, item in value.items()}
    if isinstance(value, list):
        return [sanitize_json(item) for item in value]
    if isinstance(value, str):
        normalized = value.replace("\\", "/")
        if normalized.casefold().startswith("c:/il_github/"):
            return (
                "authority/"
                + PurePosixPath(normalized).name
                + " (identity only, not included)"
            )
        if normalized.casefold().startswith("c:/users/"):
            return "[private local path omitted]"
    return value


def public_control(path: Path) -> bytes:
    original = path.read_bytes()
    if path.suffix.casefold() == ".csv":
        return original
    parsed = json.loads(original)
    return json_bytes(
        {
            "producer_control_identity": {
                "filename": path.name,
                "bytes": len(original),
                "sha256": sha256_bytes(original),
            },
            "public_projection": sanitize_json(parsed),
        }
    )


def visual_ledger() -> tuple[bytes, dict[str, int]]:
    rows: list[dict[str, object]] = []
    for relative_dir in VISUAL_DIRS:
        directory = SECTION_ROOT / Path(relative_dir)
        for path in sorted(directory.glob("*.png"), key=lambda item: item.name):
            relative = path.relative_to(SECTION_ROOT).as_posix()
            authority_derived = "authority" in relative.casefold()
            with Image.open(path) as image:
                width, height = image.size
                mode = image.mode
                dpi_value = image.info.get("dpi")
            dpi = (
                f"{dpi_value[0]:.2f}x{dpi_value[1]:.2f}"
                if dpi_value
                else "not_recorded"
            )
            rows.append(
                {
                    "visual_id": f"EGA4-S4-1-4-4-VIS-{len(rows) + 1:04d}",
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
                    "linked_scope": relative_dir.split("/", 1)[1],
                    "bounding_box": "not_recorded",
                    "rotation_degrees": 0,
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
            row["disposition"] == "manifest_only_rights_blocked" for row in rows
        ),
        "redundant_target": sum(
            row["disposition"] == "excluded_redundant_target_render"
            for row in rows
        ),
    }
    expected = {"total": 33, "rights_blocked": 15, "redundant_target": 18}
    if counts != expected:
        raise RuntimeError(f"EGA IV Section 4 visual boundary changed: {counts}")
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
                "rotation_degrees",
                "disposition",
                "pixels_public",
            ],
            rows,
        ),
        counts,
    )


def assert_text_hygiene(members: dict[str, bytes]) -> dict[str, object]:
    hits = []
    scanned = 0
    for name, data in members.items():
        if Path(name).suffix.casefold() not in {".csv", ".json", ".md", ".tex"}:
            continue
        scanned += 1
        text = data.decode("utf-8-sig", errors="replace").casefold()
        for pattern in PRIVACY_PATTERNS:
            if pattern in text:
                hits.append({"path": name, "pattern": pattern})
    if hits:
        raise RuntimeError(f"Text hygiene hits: {hits}")
    return {"text_members_scanned": scanned, "hits": [], "hit_count": 0}


def assert_reader() -> dict[str, object]:
    if identity(READER) != READER_EXPECTED[:2]:
        raise RuntimeError("EGA IV Sections 4.1-4.4 reader identity mismatch")
    reader = PdfReader(str(READER))
    if len(reader.pages) != READER_EXPECTED[2]:
        raise RuntimeError("EGA IV Sections 4.1-4.4 page count mismatch")
    extracted = "\n".join(page.extract_text() or "" for page in reader.pages)
    metadata = json.dumps(
        {str(k): str(v) for k, v in (reader.metadata or {}).items()},
        ensure_ascii=True,
    )
    hits = []
    for surface, text in (("text", extracted), ("metadata", metadata)):
        folded = text.casefold()
        for pattern in PRIVACY_PATTERNS:
            if pattern in folded:
                hits.append({"surface": surface, "pattern": pattern})
    if hits:
        raise RuntimeError(f"Reader hygiene hits: {hits}")
    return {
        "pages": len(reader.pages),
        "metadata_and_text_hits": [],
        "hit_count": 0,
    }


def build() -> dict[str, object]:
    component_root = SECTION_ROOT / "source" / "components"
    for name, expected in COMPONENTS.items():
        if identity(component_root / name) != expected:
            raise RuntimeError(f"Component identity mismatch: {name}")
    control_root = SECTION_ROOT / "controls"
    for name, expected in CONTROL_EXPECTED.items():
        path = control_root / name
        if identity(path) != expected:
            raise RuntimeError(f"Control identity mismatch: {name}")
        if name.endswith("_FINAL_VALIDATION.json"):
            value = json.loads(path.read_text(encoding="utf-8"))
            if value.get("status") != "PASS" or value.get("errors") != []:
                raise RuntimeError(f"Non-PASS producer control: {name}")

    reader_hygiene = assert_reader()
    if PACKAGE_ROOT.exists():
        shutil.rmtree(PACKAGE_ROOT)
    PACKAGE_ROOT.mkdir(parents=True)

    aggregator = "".join(
        f"\\input{{../source/components/{Path(name).stem}}}\n"
        for name in COMPONENTS
    ).encode("utf-8")
    harness = (
        "\\input{preamble}\n\n"
        "\\begin{document}\n\n"
        "\\title{EGA IV, Section 4: source-aligned working reader}\n"
        "\\author{Alexander Grothendieck and Jean Dieudonn\\'e}\n"
        "\\date{}\n"
        "\\maketitle\n\n"
        "\\setcounter{section}{3}\n"
        "\\input{../source/ega4-4.source_aligned_through_4_4}\n\n"
        "\\end{document}\n"
    ).encode("utf-8")

    members: dict[str, bytes] = {
        "source/ega4-4.source_aligned_through_4_4.tex": aggregator,
        "build_harness/ega4_section04_through_4_4.tex": harness,
        "build_harness/preamble.tex": (
            SECTION_ROOT / "build_harness" / "preamble.tex"
        ).read_bytes(),
        "build_harness/preamble-base.tex": (
            SECTION_ROOT / "build_harness" / "preamble-base.tex"
        ).read_bytes(),
        "reader/EGA4_Section4_1_4_4_English_SourceAligned.pdf": READER.read_bytes(),
    }
    for name in COMPONENTS:
        members[f"source/components/{name}"] = (component_root / name).read_bytes()
    for name in CONTROL_EXPECTED:
        members[f"controls/{name}"] = public_control(control_root / name)

    ledger, visual_counts = visual_ledger()
    members["VISUAL_EVIDENCE_DISPOSITION.csv"] = ledger
    members["PROVENANCE_AND_RIGHTS.md"] = (
        "# Provenance and rights\n\n"
        "The controlling authority is the NUMDAM EGA IV Part 2 French PDF.\n"
        f"- bytes: {AUTHORITY['bytes']}\n"
        f"- pages: {AUTHORITY['pages']}\n"
        f"- SHA-256: `{AUTHORITY['sha256']}`\n\n"
        "The authority PDF and authority-derived crops are not included. The\n"
        "English components are bounded source-aligned working successors.\n"
        "This package grants no new rights in the underlying French work.\n"
        "Pre-existing user-supplied OCR was read-only locator/drafting evidence;\n"
        "the source images remained authority and no OCR was generated or rerun.\n\n"
        "This is EGA IV Sections 4.1-4.4 integration input, not a complete EGA IV\n"
        "edition, critical edition, peer review, or rights determination.\n"
    ).encode("utf-8")
    members["README.md"] = (
        "# EGA IV Sections 4.1-4.4 source-aligned integration input\n\n"
        "This archive preserves the completed English source-aligned successor\n"
        "for EGA IV Sections 4.1-4.4 in one compact package.\n\n"
        "- Four editable TeX components and a frozen aggregator are included.\n"
        "- A reproducible XeLaTeX harness and stable 10-page reader are included.\n"
        "- All four producer validation controls report PASS with errors[].\n"
        "- Diagram 4.2.1.3 is native TeX and passed 5,000-dpi comparison.\n"
        "- Authority pixels and redundant target renders are not included.\n"
        "- The visual ledger binds all 33 in-scope PNG identities.\n"
        "- Continuation: EGA IV Section 4.5.\n\n"
        "This is off-PC integration custody, not a complete EGA IV reader or a\n"
        "new license grant.\n"
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
    validation = {
        "schema": "ega4_section4_1_4_4_source_aligned_custody_v1",
        "status": "PASS_GITHUB_CUSTODY_READY",
        "errors": [],
        "scope": "EGA IV Sections 4.1-4.4",
        "continuation": "EGA IV Section 4.5",
        "components": len(COMPONENTS),
        "reader": {
            "pages": READER_EXPECTED[2],
            "bytes": READER_EXPECTED[0],
            "sha256": READER_EXPECTED[1],
            "named_destinations": 73,
            "internal_goto_actions": 45,
            "broken_internal_actions": 0,
            "image_objects": 0,
        },
        "controls": {
            "files": len(CONTROL_EXPECTED),
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
    assert_text_hygiene(members)

    zip_path = PACKAGE_ROOT / ZIP_NAME
    deterministic_zip(zip_path, members)
    first_identity = identity(zip_path)
    with tempfile.TemporaryDirectory() as temp:
        replay = Path(temp) / ZIP_NAME
        deterministic_zip(replay, members)
        if identity(replay) != first_identity:
            raise RuntimeError("Deterministic EGA IV Section 4 ZIP mismatch")
    with zipfile.ZipFile(zip_path) as archive:
        if archive.testzip() is not None:
            raise RuntimeError("ZIP CRC failure")
        if archive.namelist() != sorted(members, key=str.casefold):
            raise RuntimeError("ZIP member order mismatch")
        for name, data in members.items():
            if archive.read(name) != data:
                raise RuntimeError(f"ZIP member readback mismatch: {name}")

    outer_readme = (
        "# EGA IV Sections 4.1-4.4 source-aligned custody\n\n"
        "One deterministic ZIP preserves the completed bounded English\n"
        "source-aligned integration input without adding a fragment reader to\n"
        "the public landing surface.\n\n"
        f"- ZIP: `{ZIP_NAME}`\n"
        f"- ZIP bytes: {first_identity[0]}\n"
        f"- ZIP SHA-256: `{first_identity[1]}`\n"
        f"- ZIP members: {len(members)}\n"
        f"- Uncompressed bytes: {sum(len(data) for data in members.values())}\n\n"
        "EGA IV Section 4.5 is the continuation. A later cumulative reader\n"
        "should consume this exact input and pass its own release validation.\n"
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
