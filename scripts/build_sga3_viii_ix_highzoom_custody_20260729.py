#!/usr/bin/env python3
"""Build a compact GitHub custody package for SGA3 Exposes VIII and IX."""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
import shutil
import struct
import zipfile
from pathlib import Path, PurePosixPath

from pypdf import PdfReader


REPO = Path(__file__).resolve().parents[1]
OUTPUT = (
    REPO
    / "sources"
    / "sga"
    / "sga3-exposes-viii-ix-highzoom-native-integration-inputs-20260729"
)
ZIP_NAME = "10c_SGA3_Exposes_VIII_IX_HighZoom_Native_Integration_Inputs_20260729.zip"
ZIP_TIME = (2026, 7, 29, 0, 0, 0)
TEXT_EXTENSIONS = {
    ".bib",
    ".cls",
    ".csv",
    ".json",
    ".jsonl",
    ".md",
    ".sty",
    ".tex",
    ".txt",
}
PRIVATE_PATTERNS = {
    "private_home": re.compile(rb"C:\\Users\\Floris", re.IGNORECASE),
    "private_github": re.compile(rb"C:\\IL_GitHub", re.IGNORECASE),
    "papors": re.compile(rb"Papors", re.IGNORECASE),
    "chatnotes": re.compile(rb"Chatnotes", re.IGNORECASE),
    "codex_thread": re.compile(
        rb"\b019[0-9a-f]{5}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b",
        re.IGNORECASE,
    ),
}
AI_PATTERNS = {
    "openai": re.compile(rb"\bOpenAI\b", re.IGNORECASE),
    "chatgpt": re.compile(rb"\bChatGPT\b", re.IGNORECASE),
    "codex": re.compile(rb"\bCodex\b", re.IGNORECASE),
    "claude": re.compile(rb"\bClaude\b", re.IGNORECASE),
    "anthropic": re.compile(rb"\bAnthropic\b", re.IGNORECASE),
}
EXPOSES = {
    "VIII": {
        "prefix": "sga3_expose_viii",
        "manifest": "controls/ACTIVE_SOURCE_SHA256.csv",
        "pdf": "build/SGA3_Expose_VIII_English.pdf",
        "status": "STATUS.md",
        "controls": [
            "controls/ACTIVE_SOURCE_SHA256.csv",
            "controls/FINAL_LOCAL_VALIDATION.json",
            "controls/NATIVE_DIAGRAM_INVENTORY.csv",
            "qa/LEAD_NATIVE_DIAGRAM_5000DPI_REVIEW_PASS.md",
        ],
        "pages": 31,
        "pdf_sha256": (
            "73C33187701407CD15BD081E04E67D7925FBF180D57DBDFDFD28B4600BB1F6EF"
        ),
        "authority_sha256": (
            "06E43E0571D411CC5579975778FCC03C8ECAA67189248D1A053E61DC653AF510"
        ),
        "diagrams": 4,
        "repairs": 3,
    },
    "IX": {
        "prefix": "sga3_expose_ix",
        "manifest": "controls/ACTIVE_SOURCE_SHA256.csv",
        "pdf": "build/SGA3_Expose_IX_English.pdf",
        "status": "STATUS.md",
        "controls": [
            "controls/ACTIVE_SOURCE_SHA256.csv",
            "controls/CONTAMINATION_EXCLUSION.md",
            "controls/LOOP2_NATIVE_VALIDATION.json",
            "controls/NATIVE_DIAGRAM_INVENTORY.csv",
            "qa/LEAD_NATIVE_DIAGRAM_5000DPI_REVIEW_PASS.md",
        ],
        "pages": 36,
        "pdf_sha256": (
            "AD6EC9FA9F6D25EBBD0E914D104F1B765FCD45878FE302DAF853B4AA6331DDBC"
        ),
        "authority_sha256": (
            "7C1E3D5B9D01AD01D0DD7B8B62045D012052E7890FB37ADC3E7934EBB5FD6FC3"
        ),
        "diagrams": 8,
        "repairs": 5,
    },
}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--viii-source", required=True, type=Path)
    parser.add_argument("--ix-source", required=True, type=Path)
    return parser.parse_args()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def csv_bytes(fieldnames: list[str], rows: list[dict[str, object]]) -> bytes:
    output = io.StringIO(newline="")
    writer = csv.DictWriter(output, fieldnames=fieldnames, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return output.getvalue().encode("utf-8")


def active_source_rows(root: Path, expose: str) -> list[dict[str, str]]:
    manifest = root / str(EXPOSES[expose]["manifest"])
    rows = read_csv(manifest)
    path_column = "path" if "path" in rows[0] else "relative_path"
    errors: list[str] = []
    seen: set[str] = set()
    for row in rows:
        relative = row[path_column]
        if relative in seen:
            errors.append(f"{expose}: duplicate active source path: {relative}")
            continue
        seen.add(relative)
        path = root / PurePosixPath(relative)
        if not path.is_file():
            errors.append(f"{expose}: active source missing: {relative}")
            continue
        if path.stat().st_size != int(row["bytes"]):
            errors.append(f"{expose}: active source byte mismatch: {relative}")
        if sha256(path) != row["sha256"].upper():
            errors.append(f"{expose}: active source SHA-256 mismatch: {relative}")
    if errors:
        raise RuntimeError("\n".join(errors))
    return rows


def pdf_image_objects(reader: PdfReader) -> int:
    count = 0
    for page in reader.pages:
        resources = page.get("/Resources")
        if not resources:
            continue
        resources = resources.get_object()
        xobjects = resources.get("/XObject")
        if not xobjects:
            continue
        xobjects = xobjects.get_object()
        for value in xobjects.values():
            obj = value.get_object()
            if obj.get("/Subtype") == "/Image":
                count += 1
    return count


def validate_pdf(path: Path, expose: str) -> dict[str, object]:
    expected = EXPOSES[expose]
    reader = PdfReader(str(path))
    errors: list[str] = []
    if len(reader.pages) != int(expected["pages"]):
        errors.append(f"{expose}: PDF page count mismatch")
    if sha256(path) != str(expected["pdf_sha256"]):
        errors.append(f"{expose}: PDF SHA-256 mismatch")
    images = pdf_image_objects(reader)
    if images:
        errors.append(f"{expose}: PDF contains {images} image XObjects")
    metadata_text = " ".join(
        str(value) for value in (reader.metadata or {}).values() if value is not None
    ).encode("utf-8", errors="ignore")
    for name, pattern in AI_PATTERNS.items():
        if pattern.search(metadata_text):
            errors.append(f"{expose}: PDF metadata contains {name}")
    if errors:
        raise RuntimeError("\n".join(errors))
    return {
        "pages": len(reader.pages),
        "bytes": path.stat().st_size,
        "sha256": sha256(path),
        "image_xobjects": images,
        "ai_metadata_hits": 0,
    }


def png_metadata(path: Path) -> dict[str, object]:
    data = path.read_bytes()
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise RuntimeError(f"not a PNG: {path}")
    offset = 8
    width = height = None
    dpi_x = dpi_y = None
    while offset + 12 <= len(data):
        length = struct.unpack(">I", data[offset : offset + 4])[0]
        kind = data[offset + 4 : offset + 8]
        payload = data[offset + 8 : offset + 8 + length]
        if kind == b"IHDR":
            width, height = struct.unpack(">II", payload[:8])
        elif kind == b"pHYs" and len(payload) == 9:
            x_ppm, y_ppm, unit = struct.unpack(">IIB", payload)
            if unit == 1:
                dpi_x = round(x_ppm * 0.0254, 2)
                dpi_y = round(y_ppm * 0.0254, 2)
        offset += 12 + length
        if kind == b"IEND":
            break
    if width is None or height is None:
        raise RuntimeError(f"PNG has no IHDR: {path}")
    return {
        "width_px": width,
        "height_px": height,
        "embedded_dpi_x": "" if dpi_x is None else dpi_x,
        "embedded_dpi_y": "" if dpi_y is None else dpi_y,
        "review_scale_dpi": 5000,
    }


def diagram_lookup(root: Path, expose: str) -> dict[str, dict[str, str]]:
    rows = read_csv(root / "controls" / "NATIVE_DIAGRAM_INVENTORY.csv")
    result: dict[str, dict[str, str]] = {}
    for row in rows:
        match = re.search(r"(?:D|DIAG-)(\d+)$", row["diagram_id"])
        if not match:
            raise RuntimeError(f"{expose}: cannot parse diagram id {row['diagram_id']}")
        result[f"D{int(match.group(1)):02d}"] = row
    if len(result) != int(EXPOSES[expose]["diagrams"]):
        raise RuntimeError(f"{expose}: diagram inventory row count mismatch")
    return result


def visual_disposition_rows(
    roots: dict[str, Path],
) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for expose, root in roots.items():
        lookup = diagram_lookup(root, expose)
        for path in sorted((root / "qa").rglob("*.png")):
            relative = path.relative_to(root).as_posix()
            id_match = re.search(r"(D\d{2})", path.name)
            if not id_match or id_match.group(1) not in lookup:
                raise RuntimeError(f"{expose}: unbound visual evidence: {relative}")
            diagram = lookup[id_match.group(1)]
            is_authority = "lead_authority_5000dpi" in path.parts
            page_key = (
                "authority_combined_page"
                if "authority_combined_page" in diagram
                else "combined_reader_page"
            )
            source_key = "source_tex" if "source_tex" in diagram else "source_file"
            metadata = png_metadata(path)
            rows.append(
                {
                    "visual_id": f"SGA3-{expose}-{path.stem}",
                    "expose": expose,
                    "diagram_id": diagram["diagram_id"],
                    "kind": "authority_crop" if is_authority else "target_render_crop",
                    "source_relative_path": relative,
                    "bytes": path.stat().st_size,
                    "sha256": sha256(path),
                    **metadata,
                    "authority_sha256": EXPOSES[expose]["authority_sha256"],
                    "authority_local_page": diagram["authority_local_page"],
                    "combined_reader_page": diagram[page_key],
                    "bounding_box": "not_recorded_in_local_control",
                    "linked_tex": diagram[source_key],
                    "linked_source_line": diagram["source_line"],
                    "disposition": (
                        "rights_blocked_not_public"
                        if is_authority
                        else "excluded_redundant_reader_render"
                    ),
                    "public_pixel_included": "false",
                    "qa_disposition": diagram.get("status", "PASS"),
                }
            )
    return rows


def package_readme() -> bytes:
    text = """# SGA 3 Exposes VIII-IX high-zoom native integration inputs

This compact archive preserves the completed Expose VIII and Expose IX inputs
for the next cumulative SGA 3 reader. It contains the exact active editable
sources, final PDFs, validation controls, diagram inventories, and lead-review
receipts.

## Scope

- Expose VIII: 31 A4 pages, 10 active TeX files, 4/4 native diagrams reviewed
  directly at 5,000 dpi, with three source-backed layout repairs.
- Expose IX: 36 A4 pages, 7 active TeX files, 8/8 native diagrams reviewed
  directly at 5,000 dpi, with five source-backed repairs.
- Raster diagram delivery: none.
- PDF image objects: zero in both readers.

Authority PDFs and authority crops are not redistributed. The
`VISUAL_EVIDENCE_DISPOSITION.csv` ledger records every local high-zoom crop by
hash, dimensions, source page, linked TeX location, and disposition. Authority
pixels are rights-blocked; target render crops are excluded because they merely
re-rasterize the supplied PDFs. Raw logs, temporary builds, the accidental
`$build` tree, and superseded reference material are also excluded.

This is a bounded GitHub custody package and cumulative-reader input. It is not
a separate current Zenodo reader, not complete SGA 3, and not a critical
edition. The direct cumulative reader remains the reader-facing object on the
existing SGA Zenodo concept.

Jacob Reinhold's SGA Markdown at revision
`e7a259f3f8608ad3edf9bf6eead3fd504dd2d23e` is comparison and drafting lineage,
not source authority. No blanket license over the underlying French works or
the reconstructed package is asserted.
"""
    return text.encode("utf-8")


def provenance_and_rights() -> bytes:
    text = """# Provenance and rights

The controlling authority identities are:

- Expose VIII: Polo-Gille authority PDF SHA-256
  `06E43E0571D411CC5579975778FCC03C8ECAA67189248D1A053E61DC653AF510`.
- Expose IX: Polo-Gille authority PDF SHA-256
  `7C1E3D5B9D01AD01D0DD7B8B62045D012052E7890FB37ADC3E7934EBB5FD6FC3`.

Those PDFs and their high-zoom crops are excluded. Their hashes, pages, linked
source locations, crop dimensions, and QA dispositions are retained in the
visual-evidence ledger. Bounding boxes were not recorded in the local controls
and are therefore reported as unavailable rather than reconstructed.

OCR and comparison translations are locator and drafting witnesses only.
Jacob Reinhold's SGA Markdown at revision
`e7a259f3f8608ad3edf9bf6eead3fd504dd2d23e` is credited comparison lineage
under his stated CC BY 4.0 terms for his contribution. It is not authority or
independent corroboration. No redistribution right or blanket license for the
underlying French material is asserted here.
"""
    return text.encode("utf-8")


def privacy_and_ai_scan(members: dict[str, bytes]) -> dict[str, object]:
    hits: list[dict[str, str]] = []
    scanned = 0
    for name, data in members.items():
        if Path(name).suffix.lower() not in TEXT_EXTENSIONS:
            continue
        scanned += 1
        for pattern_name, pattern in {**PRIVATE_PATTERNS, **AI_PATTERNS}.items():
            if pattern.search(data):
                hits.append({"member": name, "pattern": pattern_name})
    if hits:
        raise RuntimeError(f"privacy/AI scan failed: {hits}")
    return {"text_members_scanned": scanned, "hits": hits, "hit_count": len(hits)}


def curated_members(
    roots: dict[str, Path],
) -> tuple[dict[str, bytes], dict[str, object]]:
    members: dict[str, bytes] = {}
    source_results: dict[str, object] = {}
    pdf_results: dict[str, object] = {}
    for expose, root in roots.items():
        config = EXPOSES[expose]
        rows = active_source_rows(root, expose)
        path_column = "path" if "path" in rows[0] else "relative_path"
        for row in rows:
            relative = row[path_column]
            member_name = f"{config['prefix']}/{relative}"
            members[member_name] = (root / PurePosixPath(relative)).read_bytes()
        for relative in [str(config["status"]), *list(config["controls"])]:
            path = root / PurePosixPath(relative)
            if not path.is_file():
                raise RuntimeError(f"{expose}: curated control missing: {relative}")
            members[f"{config['prefix']}/{relative}"] = path.read_bytes()
        pdf = root / str(config["pdf"])
        members[f"{config['prefix']}/{config['pdf']}"] = pdf.read_bytes()
        source_results[expose] = {
            "files": len(rows),
            "bytes": sum(int(row["bytes"]) for row in rows),
            "manifest_bytes": (root / str(config["manifest"])).stat().st_size,
            "manifest_sha256": sha256(root / str(config["manifest"])),
        }
        pdf_results[expose] = validate_pdf(pdf, expose)

    visual_rows = visual_disposition_rows(roots)
    visual_fields = [
        "visual_id",
        "expose",
        "diagram_id",
        "kind",
        "source_relative_path",
        "bytes",
        "sha256",
        "width_px",
        "height_px",
        "embedded_dpi_x",
        "embedded_dpi_y",
        "review_scale_dpi",
        "authority_sha256",
        "authority_local_page",
        "combined_reader_page",
        "bounding_box",
        "linked_tex",
        "linked_source_line",
        "disposition",
        "public_pixel_included",
        "qa_disposition",
    ]
    members["VISUAL_EVIDENCE_DISPOSITION.csv"] = csv_bytes(visual_fields, visual_rows)
    members["PACKAGE_README.md"] = package_readme()
    members["PROVENANCE_AND_RIGHTS.md"] = provenance_and_rights()

    content_rows = [
        {
            "relative_path": name,
            "bytes": len(data),
            "sha256": sha256_bytes(data),
        }
        for name, data in sorted(members.items())
    ]
    members["PACKAGE_CONTENT_SHA256.csv"] = csv_bytes(
        ["relative_path", "bytes", "sha256"], content_rows
    )
    return members, {
        "active_source": source_results,
        "pdfs": pdf_results,
        "visual_evidence": {
            "rows": len(visual_rows),
            "authority_crops_rights_blocked": sum(
                row["kind"] == "authority_crop" for row in visual_rows
            ),
            "target_render_crops_excluded": sum(
                row["kind"] == "target_render_crop" for row in visual_rows
            ),
            "public_pixels_included": 0,
        },
    }


def zip_info(name: str) -> zipfile.ZipInfo:
    info = zipfile.ZipInfo(name, date_time=ZIP_TIME)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = 0o100644 << 16
    return info


def build_zip(members: dict[str, bytes], destination: Path) -> dict[str, object]:
    with zipfile.ZipFile(destination, "w", allowZip64=True) as archive:
        for name, data in sorted(members.items()):
            archive.writestr(
                zip_info(name),
                data,
                compress_type=zipfile.ZIP_DEFLATED,
                compresslevel=9,
            )

    errors: list[str] = []
    with zipfile.ZipFile(destination) as archive:
        bad = archive.testzip()
        if bad:
            errors.append(f"CRC failure: {bad}")
        names = archive.namelist()
        if len(names) != len(set(names)):
            errors.append("duplicate ZIP member names")
        if set(names) != set(members):
            errors.append("ZIP member set mismatch")
        for name in names:
            pure = PurePosixPath(name)
            if pure.is_absolute() or ".." in pure.parts or "\\" in name:
                errors.append(f"unsafe ZIP member name: {name}")
                continue
            if sha256_bytes(archive.read(name)) != sha256_bytes(members[name]):
                errors.append(f"ZIP member SHA-256 mismatch: {name}")
        uncompressed = sum(info.file_size for info in archive.infolist())
    if errors:
        raise RuntimeError("\n".join(errors))
    return {
        "filename": destination.name,
        "bytes": destination.stat().st_size,
        "sha256": sha256(destination),
        "members": len(members),
        "uncompressed_bytes": uncompressed,
        "crc_test": "PASS",
        "safe_member_names": True,
        "member_hash_readback": "PASS",
    }


def write_outer_readme(zip_result: dict[str, object]) -> None:
    text = f"""# SGA 3 Exposes VIII-IX cumulative integration inputs

This directory provides one compact off-PC custody archive for the completed
high-zoom native-diagram successors to SGA 3 Exposes VIII and IX.

- ZIP: `{ZIP_NAME}`
- ZIP bytes: {zip_result["bytes"]}
- ZIP SHA-256: `{zip_result["sha256"]}`
- ZIP members: {zip_result["members"]}
- Uncompressed member bytes: {zip_result["uncompressed_bytes"]}

The archive contains exact active TeX source, final PDFs, machine controls, and
lead-review receipts. It contains no authority pixels, reader-raster copies,
raw logs, temporary builds, private paths, or operational contributor notes.
The excluded high-zoom visuals are represented by a hash-and-disposition
ledger inside the ZIP.

This is GitHub custody and cumulative-reader input, not an additional
standalone Zenodo reader. The established SGA concept continues to front the
newest cumulative SGA 3 reader.
"""
    (OUTPUT / "README.md").write_text(text, encoding="utf-8", newline="\n")


def write_validation(
    package_results: dict[str, object],
    privacy: dict[str, object],
    zip_result: dict[str, object],
) -> None:
    validation = {
        "status": "PASS",
        "errors": [],
        "scope": "SGA 3 Exposes VIII and IX high-zoom native integration inputs",
        "package": package_results,
        "privacy_and_ai": privacy,
        "zip": zip_result,
        "disposition": {
            "github_custody": "READY",
            "zenodo_reader_surface": "DEFER_TO_CUMULATIVE_SUCCESSOR",
            "current_direct_reader_replaced": False,
        },
    }
    (OUTPUT / "PACKAGE_VALIDATION.json").write_text(
        json.dumps(validation, indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def write_outer_manifest() -> None:
    represented = [
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
    with (OUTPUT / "SHA256SUMS.csv").open(
        "w", encoding="utf-8", newline=""
    ) as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["relative_path", "bytes", "sha256"],
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    args = parse_args()
    roots = {
        "VIII": args.viii_source.resolve(),
        "IX": args.ix_source.resolve(),
    }
    for expose, root in roots.items():
        if not root.is_dir():
            raise SystemExit(f"{expose} source root does not exist: {root}")
    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    OUTPUT.mkdir(parents=True)

    members, package_results = curated_members(roots)
    privacy = privacy_and_ai_scan(members)
    zip_result = build_zip(members, OUTPUT / ZIP_NAME)
    write_outer_readme(zip_result)
    write_validation(package_results, privacy, zip_result)
    write_outer_manifest()

    result = {
        "output": str(OUTPUT),
        "outer_files": len([path for path in OUTPUT.iterdir() if path.is_file()]),
        "outer_bytes": sum(
            path.stat().st_size for path in OUTPUT.iterdir() if path.is_file()
        ),
        "zip": zip_result,
        "outer_manifest_sha256": sha256(OUTPUT / "SHA256SUMS.csv"),
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
