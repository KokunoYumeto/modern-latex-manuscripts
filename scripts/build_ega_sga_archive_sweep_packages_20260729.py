#!/usr/bin/env python3
"""Build compact EGA and SGA3 archive-sweep packages."""

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


REPO_ROOT = Path(__file__).resolve().parent.parent
EGA_OUTPUT = (
    REPO_ROOT
    / "sources"
    / "ega"
    / "checkpoints"
    / "ega0-iii-and-ega3-source-first-assigned-lane-complete-20260729"
)
SGA_OUTPUT = (
    REPO_ROOT
    / "sources"
    / "sga"
    / "sga3-native-diagram-integration-inputs-x-xvi-xviii-20260729"
)
ZIP_TIME = (2026, 7, 29, 0, 0, 0)
PRIVATE_MARKERS = (
    b"c:\\users\\",
    b"c:/users/",
    b"\\appdata\\",
    b"/appdata/",
    b"papors",
    b"chatnotes",
    b".claude",
    b".codex",
    b"source_thread_id",
    b"thread_id",
    b"claude-please",
)
READER_PROCESS_PATTERNS = (
    r"\bChatGPT\b",
    r"\bClaude\b",
    r"\bCodex\b",
    r"\bOpenAI\b",
    r"\bLLM\b",
    r"AI-generated",
    r"production status",
    r"source status",
    r"pending review",
    r"workflow status",
    r"current-progress",
)

EGA_PDFS = {
    "00a_EGA0_English_Working_Reader_Assigned_SourceFirst_Sections8_13_20260729.pdf": (
        Path("build")
        / "ega0_13_complete_checkpoint_r3"
        / "EGA0_English_complete_through_13.pdf",
        1_190_098,
        "D0454AA8BB79653D9CC97C7973EB54B2038BF8038525022038A29E9628C978F4",
        120,
    ),
    "00b_EGA3_English_Working_Reader_Assigned_SourceFirst_Sections1_7_20260729.pdf": (
        Path("build")
        / "ega3_section7_complete_checkpoint_r2"
        / "EGA3_English_complete_sections_1_through_7_r2.pdf",
        1_284_316,
        "1C2A3F286A02EBBB521D0D4939B0604A7D8000023288F4599322EFC0FA21B886",
        150,
    ),
}
EGA_TEX = {
    "02a_EGA0_English_Working_Master_Assigned_SourceFirst_Sections8_13_20260729.tex": (
        Path("source") / "ega0.tex",
        787,
        "35991ACEB8C7467344198E5B09E725DDD96E692BA1F14DECAE7A55C059FEFEAF",
    ),
    "02b_EGA3_English_Working_Master_Assigned_SourceFirst_Sections1_7_20260729.tex": (
        Path("source") / "ega3.tex",
        3_294,
        "931DDCEBB043AC945AAA5C1D3556458E01ED547C55C02644E864918D48EA33E1",
    ),
}
EGA_ZIP = "10a_EGA0_III_and_EGA3_Assigned_Lane_Source_20260729.zip"

SGA_UNITS = {
    "expose_X": {
        "root_arg": "sga_x_root",
        "pdf": (
            Path("build_loop2_native_r1") / "SGA3_Expose_X_English.pdf",
            310_778,
            "116065B39DC227EA72863ED7C71BC925CC15E0C62AAAE88601B46C648CAF64A7",
            44,
        ),
        "manifest_path_column": "path",
        "expected_source_rows": 9,
        "expected_diagrams": 4,
    },
    "expose_XVI": {
        "root_arg": "sga_xvi_root",
        "pdf": (
            Path("build_loop2_native_r1") / "SGA3_Expose_XVI_English.pdf",
            184_223,
            "C2126756DF0A22A26D37DC5097C6DC723F63C65C21636E1BE9A7886016CBC84A",
            25,
        ),
        "manifest_path_column": "path",
        "expected_source_rows": 11,
        "expected_diagrams": 3,
    },
    "expose_XVIII": {
        "root_arg": "sga_xviii_root",
        "pdf": (
            Path("build_loop2_native_r1") / "SGA3_Expose_XVIII_English.pdf",
            159_832,
            "83E955BD25A92A65507A38F8E697DFC1DA6E46D8BF154C56BE33C9940B57EF6A",
            22,
        ),
        "manifest_path_column": "relative_path",
        "expected_source_rows": 7,
        "expected_diagrams": 2,
    },
}
SGA_ZIP = (
    "10c_SGA3_Exposes_X_XVI_XVIII_"
    "Native_Diagram_Integration_Inputs_20260729.zip"
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ega-root", type=Path, required=True)
    parser.add_argument("--sga-x-root", type=Path, required=True)
    parser.add_argument("--sga-xvi-root", type=Path, required=True)
    parser.add_argument("--sga-xviii-root", type=Path, required=True)
    return parser.parse_args()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def identity(path: Path) -> tuple[int, str]:
    return path.stat().st_size, sha256(path)


def safe_member(name: str) -> bool:
    parts = PurePosixPath(name).parts
    return (
        bool(name)
        and not name.startswith(("/", "\\"))
        and re.match(r"^[A-Za-z]:", name) is None
        and ".." not in parts
    )


def csv_bytes(rows: list[dict[str, object]], fields: list[str]) -> bytes:
    output = io.StringIO(newline="")
    writer = csv.DictWriter(output, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return output.getvalue().encode("utf-8")


def write_text(path: Path, value: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(value, encoding="utf-8", newline="\n")


def save_json(path: Path, value: object) -> None:
    write_text(path, json.dumps(value, ensure_ascii=True, indent=2) + "\n")


def zip_info(name: str) -> zipfile.ZipInfo:
    info = zipfile.ZipInfo(name, date_time=ZIP_TIME)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.create_system = 3
    info.external_attr = 0o100644 << 16
    return info


def build_zip(path: Path, members: dict[str, bytes]) -> None:
    with zipfile.ZipFile(path, "w", allowZip64=True) as archive:
        for name, data in sorted(
            members.items(), key=lambda item: item[0].casefold()
        ):
            if not safe_member(name):
                raise ValueError(f"unsafe ZIP member: {name}")
            archive.writestr(zip_info(name), data)


def scan_private(name: str, data: bytes) -> list[dict[str, str]]:
    lowered = data.lower()
    return [
        {
            "path": name,
            "marker": marker.decode("ascii", errors="replace"),
        }
        for marker in PRIVATE_MARKERS
        if marker in lowered
    ]


def pdf_metrics(path: Path) -> dict[str, object]:
    reader = PdfReader(path)
    process_hits: list[dict[str, object]] = []
    goto = 0
    invalid = 0
    for page_number, page in enumerate(reader.pages, 1):
        text = " ".join((page.extract_text() or "").split())
        for pattern in READER_PROCESS_PATTERNS:
            if re.search(pattern, text, flags=re.IGNORECASE):
                process_hits.append({"page": page_number, "pattern": pattern})
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


def manifest_rows(directory: Path, exclude: set[str]) -> list[dict[str, object]]:
    rows = []
    for path in sorted(
        directory.iterdir(), key=lambda item: item.name.casefold()
    ):
        if not path.is_file() or path.name in exclude:
            continue
        rows.append(
            {
                "filename": path.name,
                "bytes": path.stat().st_size,
                "sha256": sha256(path),
            }
        )
    return rows


def assert_empty_output(path: Path) -> None:
    resolved = path.resolve()
    if resolved.parent not in {
        (REPO_ROOT / "sources" / "ega" / "checkpoints").resolve(),
        (REPO_ROOT / "sources" / "sga").resolve(),
    }:
        raise ValueError(f"unexpected output parent: {resolved.parent}")
    if path.exists():
        raise FileExistsError(f"output already exists: {path}")
    path.mkdir(parents=True)


def build_ega(root: Path) -> dict[str, object]:
    assert_empty_output(EGA_OUTPUT)
    errors: list[str] = []
    privacy_hits: list[dict[str, str]] = []
    reader_metrics: dict[str, dict[str, object]] = {}

    for output_name, (relative, size, digest, pages) in EGA_PDFS.items():
        source = root / relative
        if identity(source) != (size, digest):
            errors.append(f"identity mismatch: {relative.as_posix()}")
            continue
        target = EGA_OUTPUT / output_name
        shutil.copyfile(source, target)
        metrics = pdf_metrics(target)
        reader_metrics[output_name] = metrics
        if metrics["pages"] != pages:
            errors.append(f"page mismatch: {output_name}")
        if metrics["reader_process_hits"]:
            errors.append(f"reader process text: {output_name}")
        privacy_hits.extend(scan_private(output_name, target.read_bytes()))

    for output_name, (relative, size, digest) in EGA_TEX.items():
        source = root / relative
        if identity(source) != (size, digest):
            errors.append(f"identity mismatch: {relative.as_posix()}")
            continue
        target = EGA_OUTPUT / output_name
        shutil.copyfile(source, target)
        privacy_hits.extend(scan_private(output_name, target.read_bytes()))

    source_root = root / "source"
    source_paths = [
        source_root / "preamble.tex",
        source_root / "the.bib",
        source_root / "ega0.tex",
        source_root / "ega3.tex",
        *sorted((source_root / "ega0").glob("*.tex")),
        *sorted((source_root / "ega3").glob("*.tex")),
    ]
    source_members: dict[str, bytes] = {}
    source_rows: list[dict[str, object]] = []
    for source in source_paths:
        relative = source.relative_to(source_root).as_posix()
        data = source.read_bytes()
        source_members[relative] = data
        source_rows.append(
            {
                "path": relative,
                "bytes": len(data),
                "sha256": sha256_bytes(data),
                "role": (
                    "master"
                    if relative in {"ega0.tex", "ega3.tex"}
                    else "build_dependency"
                ),
            }
        )
        privacy_hits.extend(scan_private(relative, data))
    source_manifest = csv_bytes(
        source_rows, ["path", "bytes", "sha256", "role"]
    )
    source_members["SOURCE_MANIFEST.csv"] = source_manifest
    build_zip(EGA_OUTPUT / EGA_ZIP, source_members)

    write_text(
        EGA_OUTPUT / "README.md",
        """# EGA 0/III and EGA III assigned English lane

This compact working checkpoint preserves the completed assigned source-first
lane for EGA 0_III Sections 8-13 and EGA III Sections 1-7. The two readers
and their master TeX files are direct; recursive source is grouped in one ZIP.

The EGA 0 reader is a layered container and retains surrounding inherited
English material. The newly completed assigned source-first range is
Sections 8-13. The EGA III reader contains Sections 1-7 and ends at 7.9.14,
followed by "To be continued."

This is not complete EGA, a critical edition, final reference-v2 closure,
rights clearance, or independent human certification. The standalone builds
retain disclosed cross-volume reference warnings whose visible citation text
is present.
""",
    )
    write_text(
        EGA_OUTPUT / "PROVENANCE_AND_RIGHTS.md",
        """# Provenance and rights

The controlling authorities are the frozen NUMDAM EGA 0_III and EGA III
PDFs. They are not redistributed in this checkpoint. Existing user-supplied
OCR and external English lineages were read-only locator or drafting controls;
no OCR was generated or rerun.

No new license grant is asserted for the French originals, English
translation, or package as a whole. Rights and attribution remain with their
respective holders. Public maintenance should remain on the established EGA
concept DOI `10.5281/zenodo.20414353`, separate from the SGA concept.
""",
    )
    write_text(
        EGA_OUTPUT / "PUBLICATION_READINESS.md",
        """# Publication readiness

Status: `GITHUB_WORKING_CHECKPOINT_READY__ZENODO_SAME_CONCEPT_PENDING`

The two useful readers and master TeX files are privacy-clean and contain no
reader-facing AI, production-status, source-status, or workflow commentary.
The package is suitable for public GitHub preservation as a working
checkpoint. Any Zenodo update must use the existing EGA concept and preserve
the incomplete-working-edition caveats.
""",
    )
    write_text(
        EGA_OUTPUT / "BUILD_SUMMARY_PUBLIC.md",
        """# Build summary

- EGA 0 working reader: 120 US-letter pages.
- EGA III working reader: 150 US-letter pages.
- EGA III final build: four PDFLaTeX passes plus BibTeX, exit 0.
- No fatal TeX diagnostics or visible unresolved-reference markers.
- Newly affected EGA III pages 146-150 were rendered and inspected.
- Reader-facing process-term scan: zero hits in both PDFs.
""",
    )

    for name in (
        "README.md",
        "PROVENANCE_AND_RIGHTS.md",
        "PUBLICATION_READINESS.md",
        "BUILD_SUMMARY_PUBLIC.md",
    ):
        privacy_hits.extend(scan_private(name, (EGA_OUTPUT / name).read_bytes()))
    if privacy_hits:
        errors.append(f"privacy hits: {privacy_hits}")

    validation = {
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "scope": {
            "ega0_iii": "assigned source-first Sections 8-13",
            "ega3": "assigned English Sections 1-7",
        },
        "reader_metrics": reader_metrics,
        "source_zip": {
            "filename": EGA_ZIP,
            "members": len(source_members),
            "source_files": len(source_rows),
            "bytes": (EGA_OUTPUT / EGA_ZIP).stat().st_size,
            "sha256": sha256(EGA_OUTPUT / EGA_ZIP),
        },
        "privacy_hits": privacy_hits,
        "zenodo_concept": "10.5281/zenodo.20414353",
    }
    save_json(EGA_OUTPUT / "PACKAGE_VALIDATION.json", validation)
    rows = manifest_rows(EGA_OUTPUT, {"SHA256SUMS.csv"})
    (EGA_OUTPUT / "SHA256SUMS.csv").write_bytes(
        csv_bytes(rows, ["filename", "bytes", "sha256"])
    )
    if errors:
        raise RuntimeError("EGA package validation failed")
    return validation


def source_manifest_entries(
    root: Path, path_column: str, expected_rows: int
) -> list[tuple[str, bytes]]:
    manifest = root / "NATIVE_SOURCE_SHA256.csv"
    with manifest.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    if len(rows) != expected_rows:
        raise ValueError(f"source row mismatch: {root.name}")
    result = []
    for row in rows:
        relative_raw = row[path_column]
        relative = Path(*PurePosixPath(relative_raw.replace("\\", "/")).parts)
        source = root / relative
        observed = identity(source)
        wanted = (int(row["bytes"]), row["sha256"].upper())
        if observed != wanted:
            raise ValueError(f"source identity mismatch: {source}")
        result.append((relative.as_posix(), source.read_bytes()))
    return result


def build_sga(args: argparse.Namespace) -> dict[str, object]:
    assert_empty_output(SGA_OUTPUT)
    errors: list[str] = []
    privacy_hits: list[dict[str, str]] = []
    members: dict[str, bytes] = {}
    content_rows: list[dict[str, object]] = []
    unit_results: dict[str, object] = {}

    for unit, config in SGA_UNITS.items():
        root = getattr(args, config["root_arg"]).resolve()
        entries = source_manifest_entries(
            root,
            config["manifest_path_column"],
            config["expected_source_rows"],
        )
        includegraphics = 0
        for relative, data in entries:
            name = f"{unit}/source/{relative}"
            members[name] = data
            includegraphics += data.count(b"\\includegraphics")
            privacy_hits.extend(scan_private(name, data))
            content_rows.append(
                {
                    "path": name,
                    "bytes": len(data),
                    "sha256": sha256_bytes(data),
                    "role": "active_editable_source",
                }
            )
        if includegraphics:
            errors.append(f"active raster call in {unit}: {includegraphics}")

        controls = (
            "STATUS.md",
            "NATIVE_DIAGRAM_INVENTORY.csv",
            "LEAD_NATIVE_DIAGRAM_5000DPI_REVIEW_PASS.md",
            "LOOP2_NATIVE_VALIDATION.json",
            "NATIVE_SOURCE_SHA256.csv",
        )
        for control in controls:
            source = root / control
            data = source.read_bytes()
            name = f"{unit}/controls/{control}"
            members[name] = data
            privacy_hits.extend(scan_private(name, data))
            content_rows.append(
                {
                    "path": name,
                    "bytes": len(data),
                    "sha256": sha256_bytes(data),
                    "role": "bounded_validation_control",
                }
            )

        relative_pdf, size, digest, pages = config["pdf"]
        pdf = root / relative_pdf
        if identity(pdf) != (size, digest):
            errors.append(f"PDF identity mismatch: {unit}")
        metrics = pdf_metrics(pdf)
        if metrics["pages"] != pages:
            errors.append(f"PDF page mismatch: {unit}")
        if metrics["reader_process_hits"]:
            errors.append(f"reader process text: {unit}")
        pdf_name = f"{unit}/reader/{pdf.name}"
        pdf_data = pdf.read_bytes()
        members[pdf_name] = pdf_data
        privacy_hits.extend(scan_private(pdf_name, pdf_data))
        content_rows.append(
            {
                "path": pdf_name,
                "bytes": len(pdf_data),
                "sha256": sha256_bytes(pdf_data),
                "role": "standalone_working_reader_inside_grouped_archive",
            }
        )
        unit_results[unit] = {
            "active_source_files": len(entries),
            "native_diagrams": config["expected_diagrams"],
            "active_raster_calls": includegraphics,
            "reader": {
                "pages": pages,
                "bytes": size,
                "sha256": digest,
                "metrics": metrics,
            },
        }

    bundle_manifest = csv_bytes(
        content_rows, ["path", "bytes", "sha256", "role"]
    )
    members["BUNDLE_MEMBER_MANIFEST.csv"] = bundle_manifest
    build_zip(SGA_OUTPUT / SGA_ZIP, members)

    (SGA_OUTPUT / "BUNDLE_CONTENT_MANIFEST.csv").write_bytes(bundle_manifest)
    write_text(
        SGA_OUTPUT / "README.md",
        """# SGA3 native-diagram integration inputs: Exposes X, XVI, XVIII

This grouped archive preserves three post-cumulative native-diagram
successors without placing their small standalone readers ahead of the main
SGA3 cumulative reader. It contains the active editable TeX, native diagrams,
standalone PDFs, and exact bounded controls for Exposes X, XVI, and XVIII.

All nine active raster placeholders across these three exposes have been
replaced by native TeX diagrams. The session leads compared all nine native
diagrams to the controlling authority at 5000 dpi. No active `includegraphics`
call remains in these bounded successors.

These files are integration inputs. They do not yet replace the public
1,473-page cumulative reader because cumulative rebuilding, downstream page
coordinates, reference-v2 regeneration, and whole-reader validation remain
open.
""",
    )
    write_text(
        SGA_OUTPUT / "PROVENANCE_AND_RIGHTS.md",
        """# Provenance and rights

The controlling Polo--Gille authority PDFs are identified by exact hash in
the bundled status files but are not redistributed. Existing OCR and
comparison translations were locator or drafting witnesses only.

No new license grant is asserted. Underlying French rights, English
translation rights, and attribution remain with their respective holders.
This grouped custody package is a bounded integration archive, not a critical
edition or complete SGA3 certification.
""",
    )
    write_text(
        SGA_OUTPUT / "PUBLICATION_READINESS.md",
        """# Publication readiness

Status: `GITHUB_INTEGRATION_ARCHIVE_READY__CUMULATIVE_READER_REFRESH_PENDING`

The grouped archive is privacy-clean and suitable for GitHub custody. It
contains no authority PDF or source raster. The standalone PDFs are inside
the ZIP so the clean cumulative SGA3 reader remains the reader-first object.
Do not use this package alone to claim refreshed whole-volume reference or
diagram closure.
""",
    )
    write_text(
        SGA_OUTPUT / "CURRENT_READER_RELATION.md",
        """# Relation to the current reader

The current direct SGA3 reader remains:

`../sga3-english-complete-working-reader-clean-r15-20260729/00c00_SGA3_English_Complete_Reader_TomeI_Index_20260729.pdf`

This archive is newer only for the bounded native-diagram source of Exposes
X, XVI, and XVIII. A later no-overwrite cumulative successor should consume
these exact inputs, rebuild all downstream pages, regenerate reference
coordinates, and repeat reader-clean validation before it supersedes R15.
""",
    )
    for name in (
        "README.md",
        "PROVENANCE_AND_RIGHTS.md",
        "PUBLICATION_READINESS.md",
        "CURRENT_READER_RELATION.md",
        "BUNDLE_CONTENT_MANIFEST.csv",
    ):
        privacy_hits.extend(scan_private(name, (SGA_OUTPUT / name).read_bytes()))
    if privacy_hits:
        errors.append(f"privacy hits: {privacy_hits}")

    validation = {
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "scope": ["SGA3 Expose X", "SGA3 Expose XVI", "SGA3 Expose XVIII"],
        "units": unit_results,
        "bundle": {
            "filename": SGA_ZIP,
            "members": len(members),
            "content_rows": len(content_rows),
            "bytes": (SGA_OUTPUT / SGA_ZIP).stat().st_size,
            "sha256": sha256(SGA_OUTPUT / SGA_ZIP),
        },
        "privacy_hits": privacy_hits,
        "cumulative_reader_refreshed": False,
    }
    save_json(SGA_OUTPUT / "PACKAGE_VALIDATION.json", validation)
    rows = manifest_rows(SGA_OUTPUT, {"SHA256SUMS.csv"})
    (SGA_OUTPUT / "SHA256SUMS.csv").write_bytes(
        csv_bytes(rows, ["filename", "bytes", "sha256"])
    )
    if errors:
        raise RuntimeError("SGA package validation failed")
    return validation


def main() -> int:
    args = parse_args()
    ega = build_ega(args.ega_root.resolve())
    sga = build_sga(args)
    print(
        json.dumps(
            {
                "status": "PASS",
                "ega": ega,
                "sga": sga,
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
