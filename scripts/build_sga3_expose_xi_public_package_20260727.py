#!/usr/bin/env python3
"""Build the compact public package for the bounded SGA3 Expose XI checkpoint."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import shutil
import zipfile
from pathlib import Path, PurePosixPath


EXPECTED_ROOT_NAME = (
    "SGA3_English_Expose_XI_source_audited_"
    "loop2_reference_v2_checkpoint_20260727_r2"
)
EXPECTED_FILES = 124
EXPECTED_BYTES = 18_356_104
EXPECTED_MANIFEST_ROWS = 123
EXPECTED_MANIFEST_SHA256 = (
    "D1C019910959F7E1426088E2634F36A18CCE96F9C86DC403AB302B2388D9EEB3"
)
EXPECTED_PDF_BYTES = 268_282
EXPECTED_PDF_SHA256 = (
    "E849010ADA0D36B3A06CA6DC5D082888E64A918C53A721526CFA2A52411FF553"
)
EXPECTED_TEX_BYTES = 1_731
EXPECTED_TEX_SHA256 = (
    "DBFA66FC0782430159DC01FF6849E58796B425DBC236E8BD7512490F699A1DCE"
)
EXPECTED_TREE_SHA256 = (
    "C0E6C19102EB905483797C9344802F2083288C7FB86DE0DC0E85B9A6D1245517"
)
EXTERNAL_VALIDATION_SHA256 = (
    "178639736D32B1F66C3848FCDFD512A0360D96908A73C7A1E7770858FD872960"
)
EXPECTED_EXTERNAL_VALIDATION_BYTES = 31_031
INDEPENDENT_PREPACKAGE_AUDIT_SHA256 = (
    "3AC91C2D254B0DFE0669274C17ED440A1DFD385110F0AF92A5E920DF0389DDFE"
)
COLD_REVERIFY_RECEIPT_SHA256 = (
    "D852EECC167479848EA85831389A54CC1607B937EBCB3CF9130AE43EF8964F22"
)

PDF_NAME = "SGA3_English_Expose_XI_Loop2_ReferenceV2_R2_20260727.pdf"
TEX_NAME = "SGA3_English_Expose_XI_Loop2_ReferenceV2_R2_Master_20260727.tex"
ZIP_NAME = "SGA3_English_Expose_XI_Loop2_ReferenceV2_R2_Source_QA_20260727.zip"
FIXED_ZIP_TIME = (2026, 7, 27, 0, 0, 0)

TEXT_SUFFIXES = {
    ".bib",
    ".csv",
    ".json",
    ".jsonl",
    ".log",
    ".md",
    ".ndjson",
    ".sty",
    ".tex",
    ".txt",
}
PRIVATE_PATTERNS = (
    b"C:\\Users\\Floris",
    b"C:/Users/Floris",
    b"C:\\\\Users\\\\Floris",
    b"C:\\IL_GitHub",
    b"C:/IL_GitHub",
    b"Papors\\",
    b"Papors/",
    b"Chatnotes\\",
    b"Chatnotes/",
    b"CLAUDE-PLEASE-DONT-DELETE",
    b"source_thread_id",
)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def identity(path: Path) -> dict[str, int | str]:
    data = path.read_bytes()
    return {"bytes": len(data), "sha256": sha256_bytes(data)}


def relpath(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    fields = ["filename", "bytes", "sha256", "role"]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def formula_safe(rows: list[dict[str, str]]) -> bool:
    return all(
        not value.startswith(("=", "+", "-", "@"))
        for row in rows
        for value in row.values()
    )


def safe_member_name(name: str) -> bool:
    path = PurePosixPath(name)
    return (
        bool(name)
        and not name.startswith(("/", "\\"))
        and not (len(name) >= 2 and name[1] == ":")
        and ".." not in path.parts
        and "\\" not in name
    )


def build_readme() -> str:
    return """# SGA3 Expose XI English bounded checkpoint

This compact archive package preserves the complete bounded English SGA3
Expose XI checkpoint prepared on 2026-07-27. It contains:

- a direct 38-page A4 reader;
- the direct editable master TeX; and
- one ZIP containing the exact 124-file source, reference-v2, QA, render,
  provenance, and recursive-checksum checkpoint.

The scope is Expose XI only: authority-local pages 1-34 / combined-reader
pages 723-756, followed by a hard stop before combined page 757 / Expose XII.
It is not a cumulative or complete SGA3 reader. Expose VII and Expose X
remain absent from the public sequence, and Expose XII and later are outside
this package.

## Authority and comparison lineage

The controlling source witness is the Polo-Gille born-digital Expose XI PDF
`Expo11.pdf`, 34 pages / 431,100 bytes, SHA-256
`CDB58EA5518C29E998E12AEA8D958E488C466C3B12FE2ED178A009758A553EAD`.
That authority PDF is not redistributed. It is a PDF authority and page
locator, not recovered editor TeX. OCR is locator/drafting material only.

Jacob C. Reinhold's Expose XI Markdown from `jcreinhold/sga` commit
`e7a259f3f8608ad3edf9bf6eead3fd504dd2d23e` was credited comparison
material, not authority or independent corroboration. Its declared CC BY 4.0
terms apply only to that contribution and do not grant rights in the
underlying French work or this package.

## Validation

The source checkpoint contains 13 editable TeX files, eight native diagrams,
a 38-page reader, and all 38 reviewed page renders. The reference graph
records 214 targets and 728 candidates partitioned into 283 applied edges and
445 residuals, with zero pending actions. The PDF has 297 named destinations,
328 valid internal GoTo actions, 32 embedded non-Type3 fonts, and zero raster
XObjects.

The source ZIP contains 124 safe non-directory members totaling 18,356,104
uncompressed bytes. Its self-excluding `SHA256SUMS.csv` lists the other 123
members and replays exactly. Fresh archive-maintenance extracted-package
validation is included directly and has SHA-256
`178639736D32B1F66C3848FCDFD512A0360D96908A73C7A1E7770858FD872960`.
The package-bound independent prepackage audit has SHA-256
`3AC91C2D254B0DFE0669274C17ED440A1DFD385110F0AF92A5E920DF0389DDFE`.

The Claude-style high-zoom cold-reverify receipt has SHA-256
`D852EECC167479848EA85831389A54CC1607B937EBCB3CF9130AE43EF8964F22`;
the public evidence includes target-only 300 dpi full pages, 600 dpi whole
diagrams, and 1200 dpi detail crops. Authority-derived source pixels and
forensic side-by-side plates remain excluded. Fresh archive-maintenance
custody replay found zero manifest differences, zero private-path hits, and
zero pixel differences on independently rendered pages 1, 19, and 38.

## Rights and claim limits

No blanket license or redistribution right is asserted for the underlying
French source, the English reconstruction, editorial additions, or the
package as a whole. Rights remain with their respective holders. This is a
bounded scholarly working checkpoint, not a complete SGA3 translation,
critical edition, legal rights determination, mathematical certification,
independent human peer review, or accessibility-remediated release.

Machine-assisted contributors include OpenAI Codex / ChatGPT and Anthropic
Claude under human direction.
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--payload-root", type=Path, required=True)
    parser.add_argument("--output-root", type=Path, required=True)
    parser.add_argument("--external-validation", type=Path, required=True)
    args = parser.parse_args()

    root = args.payload_root.resolve()
    output = args.output_root.resolve()
    errors: list[str] = []

    if root.name != EXPECTED_ROOT_NAME:
        errors.append(f"payload_root_name:{root.name}")
    if not root.is_dir():
        raise SystemExit(f"Payload root does not exist: {root}")
    if output.exists() and any(output.iterdir()):
        raise SystemExit(f"Output root must be absent or empty: {output}")

    files = sorted(
        (path for path in root.rglob("*") if path.is_file()),
        key=lambda path: relpath(path, root),
    )
    total_bytes = sum(path.stat().st_size for path in files)
    if len(files) != EXPECTED_FILES:
        errors.append(f"file_count:{len(files)}")
    if total_bytes != EXPECTED_BYTES:
        errors.append(f"total_bytes:{total_bytes}")

    actual = {
        relpath(path, root): {
            "bytes": path.stat().st_size,
            "sha256": sha256_bytes(path.read_bytes()),
        }
        for path in files
    }
    source_manifest = root / "SHA256SUMS.csv"
    source_manifest_id = identity(source_manifest)
    if source_manifest_id["sha256"] != EXPECTED_MANIFEST_SHA256:
        errors.append("source_manifest_sha256")
    rows = read_csv(source_manifest)
    if len(rows) != EXPECTED_MANIFEST_ROWS:
        errors.append(f"source_manifest_rows:{len(rows)}")
    if not formula_safe(rows):
        errors.append("source_manifest_formula_safety")

    row_paths: set[str] = set()
    for row in rows:
        path = row["path"]
        row_paths.add(path)
        item = actual.get(path)
        if item is None:
            errors.append(f"source_manifest_missing:{path}")
            continue
        if int(row["bytes"]) != item["bytes"]:
            errors.append(f"source_manifest_bytes:{path}")
        if row["sha256"].upper() != item["sha256"]:
            errors.append(f"source_manifest_sha256:{path}")
    expected_paths = set(actual) - {"SHA256SUMS.csv"}
    for path in sorted(expected_paths - row_paths):
        errors.append(f"source_manifest_unlisted:{path}")
    for path in sorted(row_paths - expected_paths):
        errors.append(f"source_manifest_extra:{path}")

    privacy_hits: list[str] = []
    json_files = 0
    csv_files = 0
    for path in files:
        data = path.read_bytes()
        suffix = path.suffix.lower()
        if suffix in TEXT_SUFFIXES:
            for pattern in PRIVATE_PATTERNS:
                if pattern in data:
                    privacy_hits.append(f"{relpath(path, root)}:{pattern!r}")
        if suffix == ".json":
            json.loads(data.decode("utf-8-sig"))
            json_files += 1
        if suffix == ".csv":
            csv_rows = read_csv(path)
            if not formula_safe(csv_rows):
                errors.append(f"formula_safety:{relpath(path, root)}")
            csv_files += 1
    if privacy_hits:
        errors.extend(f"privacy:{hit}" for hit in privacy_hits)

    pdf_source = root / "reader" / "SGA3_Expose_XI_English.pdf"
    tex_source = root / "source" / "tex" / "SGA3_Expose_XI_English.tex"
    external_validation_source = args.external_validation.resolve()
    if identity(pdf_source) != {
        "bytes": EXPECTED_PDF_BYTES,
        "sha256": EXPECTED_PDF_SHA256,
    }:
        errors.append("reader_identity")
    if identity(tex_source) != {
        "bytes": EXPECTED_TEX_BYTES,
        "sha256": EXPECTED_TEX_SHA256,
    }:
        errors.append("master_tex_identity")
    if identity(external_validation_source) != {
        "bytes": EXPECTED_EXTERNAL_VALIDATION_BYTES,
        "sha256": EXTERNAL_VALIDATION_SHA256,
    }:
        errors.append("external_validation_identity")
    else:
        external_receipt = json.loads(
            external_validation_source.read_text(encoding="utf-8-sig")
        )
        if (
            external_receipt.get("status") != "PASS"
            or external_receipt.get("errors") != []
            or external_receipt.get("mutation_performed") is not False
        ):
            errors.append("external_validation_not_clean_pass")

    if errors:
        raise SystemExit(json.dumps({"status": "FAIL", "errors": errors}, indent=2))

    output.mkdir(parents=True, exist_ok=True)
    pdf_target = output / PDF_NAME
    tex_target = output / TEX_NAME
    zip_target = output / ZIP_NAME
    external_validation_target = output / "EXTERNAL_PACKAGE_VALIDATION.json"
    shutil.copyfile(pdf_source, pdf_target)
    shutil.copyfile(tex_source, tex_target)
    shutil.copyfile(external_validation_source, external_validation_target)

    with zipfile.ZipFile(
        zip_target,
        "w",
        compression=zipfile.ZIP_DEFLATED,
        compresslevel=9,
        strict_timestamps=True,
    ) as archive:
        for path in files:
            member = f"{root.name}/{relpath(path, root)}"
            info = zipfile.ZipInfo(member, FIXED_ZIP_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            archive.writestr(info, path.read_bytes(), compresslevel=9)

    zip_rows: list[dict[str, int | str]] = []
    with zipfile.ZipFile(zip_target) as archive:
        infos = [info for info in archive.infolist() if not info.is_dir()]
        if len(infos) != EXPECTED_FILES:
            errors.append(f"zip_members:{len(infos)}")
        if sum(info.file_size for info in infos) != EXPECTED_BYTES:
            errors.append("zip_uncompressed_bytes")
        for info in infos:
            if not safe_member_name(info.filename):
                errors.append(f"unsafe_zip_member:{info.filename}")
            source_rel = info.filename.removeprefix(f"{root.name}/")
            source_id = actual.get(source_rel)
            member_data = archive.read(info)
            member_id = {
                "bytes": len(member_data),
                "sha256": sha256_bytes(member_data),
            }
            if source_id != member_id:
                errors.append(f"zip_member_identity:{info.filename}")
            zip_rows.append(
                {
                    "path": info.filename,
                    "bytes": member_id["bytes"],
                    "sha256": member_id["sha256"],
                }
            )
        if archive.testzip() is not None:
            errors.append("zip_crc")

    readme_path = output / "README.md"
    readme_path.write_text(build_readme(), encoding="utf-8", newline="\n")

    package_validation = {
        "schema": "modern-latex-manuscripts-sga3-xi-custody-v1",
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "scope": {
            "work": "SGA3 Expose XI",
            "complete_within_scope": True,
            "cumulative_sga3": False,
            "combined_pages": "723-756",
            "hard_stop": "before combined page 757 / Expose XII",
        },
        "source_payload": {
            "files": len(files),
            "bytes": total_bytes,
            "reported_independent_tree_sha256": EXPECTED_TREE_SHA256,
            "self_excluding_manifest_rows": len(rows),
            "self_excluding_manifest_sha256": source_manifest_id["sha256"],
            "privacy_hits": privacy_hits,
            "json_files": json_files,
            "csv_files": csv_files,
        },
        "reader": {
            "filename": PDF_NAME,
            "bytes": EXPECTED_PDF_BYTES,
            "sha256": EXPECTED_PDF_SHA256,
            "pages": 38,
            "page_size": "A4",
            "named_destinations": 297,
            "goto_actions": 328,
            "invalid_destinations": 0,
            "embedded_non_type3_fonts": 32,
            "raster_xobjects": 0,
            "fresh_render_pages": [1, 19, 38],
            "fresh_render_pixel_absolute_errors": [0, 0, 0],
        },
        "editable_master": {
            "filename": TEX_NAME,
            "bytes": EXPECTED_TEX_BYTES,
            "sha256": EXPECTED_TEX_SHA256,
            "total_tex_files_in_archive": 13,
        },
        "zip": {
            "filename": ZIP_NAME,
            "members": len(zip_rows),
            "uncompressed_bytes": sum(int(row["bytes"]) for row in zip_rows),
            "safe_paths": not any(
                item.startswith("unsafe_zip_member:") for item in errors
            ),
            "duplicate_paths": len(zip_rows)
            - len({str(row["path"]) for row in zip_rows}),
            "member_replay_matches": not any(
                item.startswith("zip_member_identity:") for item in errors
            ),
        },
        "reference_graph": {
            "targets": 214,
            "candidates": 728,
            "edges": 283,
            "residuals": 445,
            "pending": 0,
            "pre_application_actions": 187,
            "remaining_application_actions": 0,
        },
        "independent_receipts": {
            "archive_extracted_package_validation_sha256":
                EXTERNAL_VALIDATION_SHA256,
            "package_bound_independent_prepackage_audit_sha256":
                INDEPENDENT_PREPACKAGE_AUDIT_SHA256,
            "claude_style_high_zoom_cold_reverify_sha256":
                COLD_REVERIFY_RECEIPT_SHA256,
        },
        "rights": {
            "authority_redistributed": False,
            "comparison_redistributed": False,
            "blanket_license_asserted": False,
            "critical_edition_claimed": False,
            "whole_sga3_claimed": False,
        },
    }
    validation_path = output / "PACKAGE_VALIDATION.json"
    validation_path.write_text(
        json.dumps(package_validation, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )

    outer_rows = [
        {
            "filename": PDF_NAME,
            **identity(pdf_target),
            "role": "direct_reader",
        },
        {
            "filename": TEX_NAME,
            **identity(tex_target),
            "role": "direct_editable_master",
        },
        {
            "filename": ZIP_NAME,
            **identity(zip_target),
            "role": "source_qa_archive",
        },
        {
            "filename": "README.md",
            **identity(readme_path),
            "role": "scope_provenance_rights",
        },
        {
            "filename": "PACKAGE_VALIDATION.json",
            **identity(validation_path),
            "role": "custody_validation",
        },
        {
            "filename": "EXTERNAL_PACKAGE_VALIDATION.json",
            **identity(external_validation_target),
            "role": "fresh_extracted_package_validation",
        },
    ]
    write_csv(output / "SHA256SUMS.csv", outer_rows)

    if errors:
        raise SystemExit(json.dumps(package_validation, indent=2))
    print(
        json.dumps(
            {
                "status": "PASS",
                "output": str(output),
                "outer_files": 7,
                "zip_members": len(zip_rows),
                "zip_uncompressed_bytes": sum(
                    int(row["bytes"]) for row in zip_rows
                ),
                "zip_identity": identity(zip_target),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
