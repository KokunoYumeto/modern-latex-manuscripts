#!/usr/bin/env python3
"""Build the compact SGA3 Expose VI freeze4 archive package."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import shutil
import zipfile
from pathlib import Path, PurePosixPath
from typing import Any, Iterable

from pypdf import PdfReader


RELEASE_DATE = "2026-07-24"
EXPECTED_TREE_FILES = 133
EXPECTED_TREE_BYTES = 25_834_446
EXPECTED_MANIFEST_ROWS = 131
EXPECTED_MANIFEST_BYTES = 45_197
EXPECTED_MANIFEST_SHA256 = (
    "FCAB1D5D5ACB297544EAA331DAE128663C580C08707183499F5FB6D51A806490"
)
EXPECTED_VALIDATION_BYTES = 6_705
EXPECTED_VALIDATION_SHA256 = (
    "EDFF8E8A49E01CA0EBA718D54E64BB6483EE19BEB24CFD4F65C38918B7352CF0"
)
EXPECTED_MASTER_BYTES = 8_926
EXPECTED_MASTER_SHA256 = (
    "F5388E9978FD1D33CEA905EE892ED859089F8D0329005031033B414593E299B4"
)
EXPECTED_PDF_BYTES = 965_557
EXPECTED_PDF_SHA256 = (
    "4891908E423F933B36E61295BDC0CC77948B60B64B727F6B3592AB73332CC5CF"
)
EXPECTED_PDF_PAGES = 185
EXPECTED_DESTINATIONS = 1_224
EXPECTED_GOTO_ACTIONS = 948

PAYLOAD_MANIFEST = "ZENODO_PAYLOAD_MANIFEST.csv"
PAYLOAD_VALIDATION = "PUBLIC_PROJECTION_VALIDATION.json"
MASTER_REL = "tex_reference_v2/SGA3_Expose_VI_English_ReferenceV2.tex"
PDF_REL = "build_reference_v2_r1/SGA3_Expose_VI_English_ReferenceV2.pdf"

PDF_NAME = "SGA3_English_Expose_VI_Native_ReferenceV2_R4_20260724.pdf"
TEX_NAME = "SGA3_English_Expose_VI_Native_ReferenceV2_R4_Master_20260724.tex"
ZIP_NAME = (
    "SGA3_English_Expose_VI_Native_ReferenceV2_R4_"
    "Source_Evidence_20260724.zip"
)

DOCUMENT_IDENTITIES = {
    "handoff": (
        6_757,
        "7EF0D2485F05C1162537F6AAD084393440A55AA080023E0FD722A519B1F25D57",
    ),
    "correction_receipt": (
        2_265,
        "D996EADEB121F8259B2CBBE2A70EAF711D18956E14D3BDE847C5966817758D77",
    ),
    "status": (
        46_659,
        "FA238FBE86620B6128537B261800D16F0C02138ABA70AB365A334BE00903AC24",
    ),
    "audit_report": (
        3_816,
        "8496B6641AC3996D98B67B8111DF765277308E25B5C3C8D396D792147A244918",
    ),
    "audit_validation": (
        13_410,
        "ED52AEEA10DD4656D31D6DB3124F6EA10068E8A30F40DE75F571A0448E633B2C",
    ),
    "audit_manifest": (
        46_359,
        "3E5E4C4B8151BA2B219FB9E60DCA0FAC3AF5947417DC50B826B48DD3073392EA",
    ),
}

PRIVACY_MARKERS = (
    b"C:\\Users\\Floris",
    b"C:/Users/Floris",
    b"C:\\IL_GitHub",
    b"C:/IL_GitHub",
    b"AppData\\Local\\Temp",
    b"AppData/Local/Temp",
    b"019f70c0-",
    b"019f711e-",
    b"CLAUDE-PLEASE-DONT-DELETE",
    b"Papors\\Chatnotes",
)

TEXT_SUFFIXES = {
    ".bib",
    ".cls",
    ".csv",
    ".json",
    ".jsonl",
    ".log",
    ".md",
    ".ndjson",
    ".ps1",
    ".sty",
    ".tex",
    ".txt",
}


def sha256_path(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def identity(path: Path) -> dict[str, Any]:
    return {"bytes": path.stat().st_size, "sha256": sha256_path(path)}


def assert_identity(path: Path, expected_bytes: int, expected_sha256: str) -> None:
    actual = identity(path)
    if (
        actual["bytes"] != expected_bytes
        or actual["sha256"] != expected_sha256
    ):
        raise RuntimeError(
            f"Identity mismatch for {path}: {actual}; expected "
            f"bytes={expected_bytes}, sha256={expected_sha256}"
        )


def collect_files(root: Path) -> list[Path]:
    return sorted(
        (path for path in root.rglob("*") if path.is_file()),
        key=lambda path: path.relative_to(root).as_posix(),
    )


def safe_relative_path(value: str) -> str:
    path = PurePosixPath(value.replace("\\", "/"))
    if path.is_absolute() or not path.parts or ".." in path.parts:
        raise RuntimeError(f"Unsafe relative path: {value}")
    return path.as_posix()


def write_text(path: Path, text: str) -> None:
    path.write_text(text.rstrip() + "\n", encoding="utf-8", newline="\n")


def write_json(path: Path, value: Any) -> None:
    write_text(path, json.dumps(value, ensure_ascii=True, indent=2))


def safe_csv_cell(value: Any) -> str:
    text = str(value)
    return "'" + text if text.startswith(("=", "+", "-", "@")) else text


def write_csv(
    path: Path,
    fieldnames: list[str],
    rows: Iterable[dict[str, Any]],
) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=fieldnames,
            lineterminator="\r\n",
        )
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {key: safe_csv_cell(row.get(key, "")) for key in fieldnames}
            )


def canonical_member_aggregate(root: Path, files: Iterable[Path]) -> str:
    digest = hashlib.sha256()
    for path in files:
        rel = path.relative_to(root).as_posix()
        digest.update(
            f"{rel}\t{path.stat().st_size}\t{sha256_path(path)}\n".encode(
                "utf-8"
            )
        )
    return digest.hexdigest().upper()


def validate_document(path: Path, label: str) -> dict[str, Any]:
    expected_bytes, expected_sha256 = DOCUMENT_IDENTITIES[label]
    assert_identity(path, expected_bytes, expected_sha256)
    return {
        "label": label,
        "bytes": expected_bytes,
        "sha256": expected_sha256,
    }


def validate_payload(root: Path) -> dict[str, Any]:
    files = collect_files(root)
    total_bytes = sum(path.stat().st_size for path in files)
    if len(files) != EXPECTED_TREE_FILES or total_bytes != EXPECTED_TREE_BYTES:
        raise RuntimeError(
            f"Payload boundary mismatch: files={len(files)}, bytes={total_bytes}"
        )

    manifest_path = root / PAYLOAD_MANIFEST
    validation_path = root / PAYLOAD_VALIDATION
    assert_identity(
        manifest_path,
        EXPECTED_MANIFEST_BYTES,
        EXPECTED_MANIFEST_SHA256,
    )
    assert_identity(
        validation_path,
        EXPECTED_VALIDATION_BYTES,
        EXPECTED_VALIDATION_SHA256,
    )
    assert_identity(
        root / MASTER_REL,
        EXPECTED_MASTER_BYTES,
        EXPECTED_MASTER_SHA256,
    )
    assert_identity(
        root / PDF_REL,
        EXPECTED_PDF_BYTES,
        EXPECTED_PDF_SHA256,
    )

    with manifest_path.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    if len(rows) != EXPECTED_MANIFEST_ROWS:
        raise RuntimeError(f"Expected 131 manifest rows, found {len(rows)}")

    represented: set[str] = set()
    replay_errors: list[str] = []
    for row in rows:
        rel = safe_relative_path(row["path"])
        if rel in represented:
            replay_errors.append(f"duplicate:{rel}")
            continue
        represented.add(rel)
        path = root / Path(*PurePosixPath(rel).parts)
        if not path.is_file():
            replay_errors.append(f"missing:{rel}")
            continue
        if path.stat().st_size != int(row["bytes"]):
            replay_errors.append(f"bytes:{rel}")
        if sha256_path(path) != row["sha256"].upper():
            replay_errors.append(f"sha256:{rel}")

    actual_relatives = {
        path.relative_to(root).as_posix()
        for path in files
        if path.name not in {PAYLOAD_MANIFEST, PAYLOAD_VALIDATION}
    }
    if represented != actual_relatives:
        replay_errors.extend(
            f"manifest_missing:{path}"
            for path in sorted(actual_relatives - represented)
        )
        replay_errors.extend(
            f"manifest_extra:{path}"
            for path in sorted(represented - actual_relatives)
        )
    if replay_errors:
        raise RuntimeError(f"Manifest replay failed: {replay_errors}")

    validation = json.loads(validation_path.read_text(encoding="utf-8-sig"))
    if (
        validation.get("status") != "PASS_READY_FOR_EXACT_EXTERNAL_REPLAY"
        or validation.get("errors") != []
    ):
        raise RuntimeError("Packaged validation is not PASS/errors[].")

    privacy_hits: list[dict[str, str]] = []
    for path in files:
        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        data = path.read_bytes()
        for marker in PRIVACY_MARKERS:
            if marker in data:
                privacy_hits.append(
                    {
                        "path": path.relative_to(root).as_posix(),
                        "marker": marker.decode("ascii", errors="replace"),
                    }
                )
    if privacy_hits:
        raise RuntimeError(f"Privacy hits found: {privacy_hits}")

    prohibited = [
        path.relative_to(root).as_posix()
        for path in files
        if path.suffix.lower() in {".aux", ".out", ".synctex", ".toc"}
        or "Exp6A" in path.name
        or "Exp6B" in path.name
    ]
    if prohibited:
        raise RuntimeError(f"Prohibited payload files found: {prohibited}")

    reader = PdfReader(root / PDF_REL)
    goto_actions = 0
    uri_actions = 0
    other_actions = 0
    invalid_links = 0
    for page in reader.pages:
        for ref in page.get("/Annots") or []:
            annotation = ref.get_object()
            if annotation.get("/Subtype") != "/Link":
                continue
            action = annotation.get("/A")
            destination = annotation.get("/Dest")
            if action:
                subtype = action.get("/S")
                if subtype == "/GoTo":
                    goto_actions += 1
                elif subtype == "/URI":
                    uri_actions += 1
                else:
                    other_actions += 1
            elif destination is not None:
                goto_actions += 1
            else:
                invalid_links += 1
    pdf_replay = {
        "pages": len(reader.pages),
        "named_destinations": len(reader.named_destinations),
        "goto_actions": goto_actions,
        "uri_actions": uri_actions,
        "other_actions": other_actions,
        "invalid_links": invalid_links,
    }
    if pdf_replay != {
        "pages": EXPECTED_PDF_PAGES,
        "named_destinations": EXPECTED_DESTINATIONS,
        "goto_actions": EXPECTED_GOTO_ACTIONS,
        "uri_actions": 0,
        "other_actions": 0,
        "invalid_links": 0,
    }:
        raise RuntimeError(f"PDF replay mismatch: {pdf_replay}")

    return {
        "files": len(files),
        "bytes": total_bytes,
        "manifest_rows": len(rows),
        "manifest_sha256": EXPECTED_MANIFEST_SHA256,
        "validation_sha256": EXPECTED_VALIDATION_SHA256,
        "member_aggregate": canonical_member_aggregate(root, files),
        "privacy_hits": privacy_hits,
        "pdf_replay": pdf_replay,
        "file_list": files,
    }


def add_zip_member(archive: zipfile.ZipFile, root: Path, path: Path) -> None:
    rel = safe_relative_path(path.relative_to(root).as_posix())
    info = zipfile.ZipInfo(rel, date_time=(2026, 7, 24, 0, 0, 0))
    info.compress_type = zipfile.ZIP_DEFLATED
    info.create_system = 3
    info.external_attr = 0o100644 << 16
    archive.writestr(
        info,
        path.read_bytes(),
        compress_type=zipfile.ZIP_DEFLATED,
        compresslevel=9,
    )


def build_release(args: argparse.Namespace) -> dict[str, Any]:
    payload = args.payload.resolve()
    output = args.output.resolve()
    if not payload.is_dir():
        raise RuntimeError(f"Payload does not exist: {payload}")
    if output.exists() and any(output.iterdir()):
        raise RuntimeError(f"Output must not already contain files: {output}")
    output.mkdir(parents=True, exist_ok=True)

    documents = [
        validate_document(args.handoff.resolve(), "handoff"),
        validate_document(
            args.correction_receipt.resolve(), "correction_receipt"
        ),
        validate_document(args.status.resolve(), "status"),
        validate_document(args.audit_report.resolve(), "audit_report"),
        validate_document(
            args.audit_validation.resolve(), "audit_validation"
        ),
        validate_document(args.audit_manifest.resolve(), "audit_manifest"),
    ]
    audit_validation = json.loads(
        args.audit_validation.read_text(encoding="utf-8-sig")
    )
    if audit_validation.get("status") != "PASS" or audit_validation.get(
        "errors"
    ) != []:
        raise RuntimeError("Independent audit is not PASS/errors[].")

    payload_result = validate_payload(payload)
    pdf_out = output / PDF_NAME
    tex_out = output / TEX_NAME
    zip_out = output / ZIP_NAME
    shutil.copyfile(payload / PDF_REL, pdf_out)
    shutil.copyfile(payload / MASTER_REL, tex_out)

    with zipfile.ZipFile(
        zip_out, "x", compression=zipfile.ZIP_DEFLATED, compresslevel=9
    ) as archive:
        for path in payload_result["file_list"]:
            add_zip_member(archive, payload, path)

    zip_errors: list[str] = []
    zip_member_rows: list[dict[str, Any]] = []
    with zipfile.ZipFile(zip_out, "r") as archive:
        names = archive.namelist()
        if len(names) != EXPECTED_TREE_FILES or len(set(names)) != len(names):
            zip_errors.append("member_count_or_duplicate")
        for info in archive.infolist():
            safe_relative_path(info.filename)
            data = archive.read(info.filename)
            source = payload / Path(*PurePosixPath(info.filename).parts)
            if not source.is_file():
                zip_errors.append(f"missing_source:{info.filename}")
                continue
            digest = hashlib.sha256(data).hexdigest().upper()
            if len(data) != source.stat().st_size:
                zip_errors.append(f"bytes:{info.filename}")
            if digest != sha256_path(source):
                zip_errors.append(f"sha256:{info.filename}")
            zip_member_rows.append(
                {
                    "path": info.filename,
                    "bytes": len(data),
                    "sha256": digest,
                }
            )
    if zip_errors:
        raise RuntimeError(f"ZIP replay failed: {zip_errors}")

    readme = f"""# SGA 3 English Expose VI - native-diagram reference-v2 freeze4

This compact package publishes complete Expose VI A and VI B as a bounded
English native-diagram/reference-v2 working reader.

## Direct files

- `{PDF_NAME}`: 185-page A4 reader.
- `{TEX_NAME}`: directly editable master TeX.
- `{ZIP_NAME}`: the exact 133-file frozen payload, including 90 component TeX
  files, machine-readable reference controls, independent render evidence,
  rights and attribution notices, and the original payload manifests.

## Verified surface

- 58/58 diagrams are native TeX/TikZ constructions;
- 60 active `tikzcd` environments and zero `includegraphics` calls;
- 1,224 named PDF destinations and 948 valid internal GoTo actions;
- 987 reference targets, 672 linked edges, 7,629 candidates, and 6,957
  positively classified residuals;
- 185/185 pages independently rebuilt, text-compared, and raster-compared;
- zero public privacy hits and no authority PDF or OCR redistribution.

## Scope and limits

The scope is complete Expose VI A (local pages 1-38) and VI B (local pages
1-111). VI B local page 112 is a terminal blank envelope. Expose VII and later
are excluded. This does not complete SGA 3 and is not a critical edition,
mathematical certification, rights clearance, or tagged-PDF accessibility
certification.

The Polo--Gille Expose VI A and VI B PDFs are fixed authority identity controls
only and are not redistributed. Rights in the underlying French work remain
with their holders.

Jacob C. Reinhold's `jcreinhold/sga` English comparison lineage at revision
`e7a259f3f8608ad3edf9bf6eead3fd504dd2d23e` is credited under his stated
CC BY 4.0 terms for his translation contribution. It is comparison and
drafting lineage, not French authority or independent corroboration.

The append-only identity-correction receipt and final producer STATUS are bound
in `PACKAGE_VALIDATION.json`. They document this same single handoff and do not
constitute a second transport or publication.
"""
    write_text(output / "README.md", readme)

    validation = {
        "schema": "sga3_expose_vi_native_reference_v2_compact_release_v1",
        "status": "PASS",
        "errors": [],
        "source_payload": {
            key: value
            for key, value in payload_result.items()
            if key != "file_list"
        },
        "reader": {
            "pdf": PDF_NAME,
            "pdf_bytes": pdf_out.stat().st_size,
            "pdf_sha256": sha256_path(pdf_out),
            "pages": EXPECTED_PDF_PAGES,
            "master_tex": TEX_NAME,
            "master_tex_bytes": tex_out.stat().st_size,
            "master_tex_sha256": sha256_path(tex_out),
        },
        "archive": {
            "path": ZIP_NAME,
            "bytes": zip_out.stat().st_size,
            "sha256": sha256_path(zip_out),
            "members": len(zip_member_rows),
            "uncompressed_bytes": sum(row["bytes"] for row in zip_member_rows),
            "member_aggregate": payload_result["member_aggregate"],
            "errors": zip_errors,
        },
        "custody_documentation": documents,
        "independent_audit": {
            "status": audit_validation["status"],
            "errors": audit_validation["errors"],
        },
        "rights": {
            "authority_pdfs_redistributed": False,
            "ocr_redistributed": False,
            "underlying_french_rights_granted": False,
            "reinhold_revision": (
                "e7a259f3f8608ad3edf9bf6eead3fd504dd2d23e"
            ),
            "reinhold_translation_lineage_license": "CC BY 4.0",
        },
        "claims": {
            "whole_sga3_complete": False,
            "critical_edition": False,
            "tagged_accessibility": False,
            "single_handoff_only": True,
        },
    }
    write_json(output / "PACKAGE_VALIDATION.json", validation)

    outer_files = sorted(
        (
            path
            for path in output.iterdir()
            if path.is_file() and path.name != "SHA256SUMS.csv"
        ),
        key=lambda path: path.name,
    )
    role_by_name = {
        PDF_NAME: "reader_pdf",
        TEX_NAME: "primary_editable_tex",
        ZIP_NAME: "grouped_source_and_evidence",
        "README.md": "documentation",
        "PACKAGE_VALIDATION.json": "release_validation",
    }
    rows = [
        {
            "relative_path": path.name,
            "bytes": path.stat().st_size,
            "sha256": sha256_path(path),
            "role": role_by_name[path.name],
            "scope": "SGA3 complete Expose VI A and VI B",
            "status": "bounded_working_reader_not_complete_sga3",
        }
        for path in outer_files
    ]
    write_csv(
        output / "SHA256SUMS.csv",
        ["relative_path", "bytes", "sha256", "role", "scope", "status"],
        rows,
    )

    final_files = sorted(path for path in output.iterdir() if path.is_file())
    if len(final_files) != 6:
        raise RuntimeError(f"Expected six outer files, found {len(final_files)}")

    return {
        "status": "PASS",
        "output_root": str(output),
        "outer_files": len(final_files),
        "outer_bytes": sum(path.stat().st_size for path in final_files),
        "reader_pdf_sha256": sha256_path(pdf_out),
        "reader_tex_sha256": sha256_path(tex_out),
        "archive_sha256": sha256_path(zip_out),
        "archive_members": len(zip_member_rows),
        "archive_uncompressed_bytes": sum(
            row["bytes"] for row in zip_member_rows
        ),
        "member_aggregate": payload_result["member_aggregate"],
        "sha256s_csv_sha256": sha256_path(output / "SHA256SUMS.csv"),
    }


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser()
    result.add_argument("--payload", type=Path, required=True)
    result.add_argument("--output", type=Path, required=True)
    result.add_argument("--handoff", type=Path, required=True)
    result.add_argument("--correction-receipt", type=Path, required=True)
    result.add_argument("--status", type=Path, required=True)
    result.add_argument("--audit-report", type=Path, required=True)
    result.add_argument("--audit-validation", type=Path, required=True)
    result.add_argument("--audit-manifest", type=Path, required=True)
    return result


if __name__ == "__main__":
    print(json.dumps(build_release(parser().parse_args()), indent=2))
