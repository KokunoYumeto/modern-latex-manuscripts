#!/usr/bin/env python3
"""Build the 482-record English/Germanic public decision-log projection v3."""

from __future__ import annotations

import csv
import hashlib
import json
import os
import subprocess
import tempfile
import zipfile
from pathlib import Path

# The reused v2 sanitizer resolves this exact bounded source root at import.
os.environ.setdefault(
    "ENGLISH_GERMANIC_CONTROL_ROOT",
    r"C:\Users\Floris\Documents\interlanguage\03_projects\language_management\english_germanic\00_lane_control",
)
import publish_english_germanic_log_privacy_remediation_dual_doi_20260803 as v2_builder


WORKTREE = Path(
    r"C:\Users\Floris\Documents\Codex\2026-05-26\there-is-currently-an-ongoing-process\wt-sga-global-reader-provisional-20260803"
)
CONTROL_ROOT = Path(
    r"C:\Users\Floris\Documents\interlanguage\03_projects\language_management\english_germanic\00_lane_control"
)
SOURCE_LOG = CONTROL_ROOT / "ENGLISH_GERMANIC_DECISION_LOG_v1.jsonl"
FINAL = WORKTREE / r"interlanguage-sidecar\20260803\english-germanic-decision-log-privacy-v3"

EXPECTED_SOURCE = (
    3_225_532,
    "A4027C630C61ECCF82BD1B5062F0B65A28AE89F43D1923CE680A9D01FB141386",
)
EXPECTED_RECORDS = 482
NEW_IDS = [
    "EG-ARCHIVE-SGA-FAC-GITHUB-CLOSEOUT-20260803-0001",
    "EG-ARCHIVE-EGA-I-P127-R50-CUSTODY-ACCEPTANCE-20260803-0001",
]
V2_DIR = WORKTREE / r"sources\sga\sga1-7ii-presentation-clean-complete-20260803-r2\archive"
V2_GIT_PATH = "sources/sga/sga1-7ii-presentation-clean-complete-20260803-r2/archive/00_ENGLISH_GERMANIC_DECISION_LOG_1_PUBLIC_PRIVACY_CLEAN_v2.jsonl"

CLEAN_NAME = "00_ENGLISH_GERMANIC_DECISION_LOG_PUBLIC_PRIVACY_CLEAN_v3.jsonl"
LEDGER_NAME = "01_ENGLISH_GERMANIC_DECISION_LOG_PRIVACY_TRANSFORMATIONS_v3.csv"
VALIDATION_NAME = "02_ENGLISH_GERMANIC_DECISION_LOG_PRIVACY_VALIDATION_v3.json"
NOTE_NAME = "03_ENGLISH_GERMANIC_DECISION_LOG_PRIVACY_README_v3.md"
MANIFEST_NAME = "04_PACKAGE_PAYLOAD_MANIFEST.csv"
ZIP_NAME = "05_ENGLISH_GERMANIC_DECISION_LOG_PUBLIC_PROVENANCE_v3.zip"
UPLOAD_MANIFEST_NAME = "06_ZENODO_UPLOAD_MANIFEST.csv"
PACKAGE_VALIDATION_NAME = "07_PACKAGE_VALIDATION.json"


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def identity(path: Path) -> tuple[int, str]:
    data = path.read_bytes()
    return len(data), sha256(data)


def write_json(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")


def rows(root: Path, excluded: set[str] | None = None) -> list[dict[str, object]]:
    excluded = excluded or set()
    result: list[dict[str, object]] = []
    for path in sorted((p for p in root.rglob("*") if p.is_file()), key=lambda p: p.relative_to(root).as_posix()):
        rel = path.relative_to(root).as_posix()
        if rel in excluded:
            continue
        data = path.read_bytes()
        result.append({"relative_path": rel, "bytes": len(data), "sha256": sha256(data)})
    return result


def write_manifest(path: Path, manifest_rows: list[dict[str, object]], extra: tuple[str, ...] = ()) -> None:
    fields = ("relative_path", "bytes", "sha256") + extra
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        for row in manifest_rows:
            writer.writerow({field: row.get(field, "") for field in fields})


def canonical_tree_sha(manifest_rows: list[dict[str, object]]) -> str:
    data = "".join(
        f"{row['relative_path']}\t{row['bytes']}\t{row['sha256']}\n"
        for row in sorted(manifest_rows, key=lambda r: str(r["relative_path"]))
    ).encode("utf-8")
    return sha256(data)


def make_zip(path: Path, root: Path, members: list[str]) -> dict[str, object]:
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for rel in sorted(members):
            info = zipfile.ZipInfo(rel, (1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, (root / rel).read_bytes())
    with zipfile.ZipFile(path) as archive:
        if archive.testzip() is not None or archive.namelist() != sorted(members):
            raise RuntimeError("v3 provenance ZIP structural replay failed")
        for rel in archive.namelist():
            if archive.read(rel) != (root / rel).read_bytes():
                raise RuntimeError(f"v3 provenance ZIP member mismatch: {rel}")
    data = path.read_bytes()
    return {"members": len(members), "bytes": len(data), "sha256": sha256(data)}


def build(temp: Path) -> dict[str, object]:
    source_before = identity(SOURCE_LOG)
    if source_before != EXPECTED_SOURCE:
        raise RuntimeError(f"source decision log moved before v3 freeze: {source_before}")

    clean = temp / CLEAN_NAME
    ledger = temp / LEDGER_NAME
    report = v2_builder.sanitize_log(SOURCE_LOG, clean, ledger)
    source_after = identity(SOURCE_LOG)
    if source_after != source_before:
        raise RuntimeError("source decision log moved during v3 projection")
    if report["source_records"] != EXPECTED_RECORDS:
        raise RuntimeError(f"unexpected source record count: {report['source_records']}")

    source_values = [json.loads(line) for line in SOURCE_LOG.read_text(encoding="utf-8").splitlines()]
    clean_values = [json.loads(line) for line in clean.read_text(encoding="utf-8").splitlines()]
    source_ids = [str(value["decision_id"]) for value in source_values]
    clean_ids = [str(value["decision_id"]) for value in clean_values]
    if source_ids != clean_ids or source_ids[-2:] != NEW_IDS:
        raise RuntimeError("v3 decision IDs or exact append order do not match")

    v2_bytes = subprocess.check_output(
        ["git", "show", f"origin/main:{V2_GIT_PATH}"], cwd=WORKTREE
    )
    v2_lines = v2_bytes.decode("utf-8").splitlines()
    v3_lines = clean.read_text(encoding="utf-8").splitlines()
    if len(v2_lines) != 480 or v3_lines[:480] != v2_lines:
        raise RuntimeError("v3 does not preserve the exact first 480 public records")

    validation = {
        "schema": "english-germanic-decision-log-public-privacy-projection-v3",
        "status": "PASS",
        "errors": [],
        "source_custody": {
            "state": "private append-only source; not redistributed verbatim",
            "records": report["source_records"],
            "bytes": report["source_bytes"],
            "sha256": report["source_sha256"],
        },
        "public_projection": {
            "file": CLEAN_NAME,
            "records": report["public_records"],
            "bytes": report["public_bytes"],
            "sha256": report["public_sha256"],
            "decision_ids_exact_order_match": True,
            "records_omitted": 0,
            "first_480_records_byte_identical_to_v2": True,
            "new_record_ids": NEW_IDS,
            "transformation_events": report["transformation_events"],
            "transformation_classes": report["transformation_classes"],
            "residual_private_tokens": 0,
        },
        "transformation_ledger": {
            "file": LEDGER_NAME,
            "bytes": report["ledger_bytes"],
            "sha256": report["ledger_sha256"],
            "one_row_per_replacement_event": True,
            "source_tokens_bound_by_hash_not_disclosed": True,
        },
        "predecessor": {
            "generation": "v2",
            "records": 480,
            "public_log_bytes": len(v2_bytes),
            "public_log_sha256": sha256(v2_bytes),
            "methodology_record": 21780213,
            "replication_record": 21780218,
        },
        "privacy_transforms_only": True,
        "production_content_changed": False,
        "reader_bytes_changed": False,
        "fac_payload_included": False,
        "gaga_payload_included": False,
    }
    write_json(temp / VALIDATION_NAME, validation)
    (temp / NOTE_NAME).write_text(
        "# English/Germanic decision-log privacy projection v3\n\n"
        "This successor preserves all 482 private source decisions in exact order and omits none. Its first 480 public JSONL records are byte-identical to v2. It adds only the final SGA/FAC GitHub closeout decision and the EGA I printed-p.127 custody-acceptance decision.\n\n"
        "The source log remains private and append-only. Public transformation replaces only private user/path roots, Codex-state segments, the private project email, and complete internal task-ID shapes. Each replacement event records its source record, decision ID, JSON path, source-token byte length and SHA-256, and replacement. No reader, translation, mathematical, French authority, FAC, or GAGA payload is contained here.\n",
        encoding="utf-8",
        newline="\n",
    )

    payload_rows = rows(
        temp,
        {MANIFEST_NAME, ZIP_NAME, UPLOAD_MANIFEST_NAME, PACKAGE_VALIDATION_NAME},
    )
    write_manifest(temp / MANIFEST_NAME, payload_rows)
    members = [str(row["relative_path"]) for row in payload_rows] + [MANIFEST_NAME]
    zip_info = make_zip(temp / ZIP_NAME, temp, members)

    upload_names = [CLEAN_NAME, LEDGER_NAME, VALIDATION_NAME, NOTE_NAME, MANIFEST_NAME, ZIP_NAME]
    upload_rows: list[dict[str, object]] = []
    for name in upload_names:
        data = (temp / name).read_bytes()
        upload_rows.append(
            {
                "relative_path": name,
                "bytes": len(data),
                "sha256": sha256(data),
                "methodology_concept": "10.5281/zenodo.21124403",
                "replication_concept": "10.5281/zenodo.20461174",
                "direct_public": "true",
            }
        )
    write_manifest(
        temp / UPLOAD_MANIFEST_NAME,
        upload_rows,
        ("methodology_concept", "replication_concept", "direct_public"),
    )

    before_validation = rows(temp, {PACKAGE_VALIDATION_NAME})
    package_validation = {
        "status": "PASS_READY_FOR_DUAL_DOI_PUBLICATION",
        "errors": [],
        "records": EXPECTED_RECORDS,
        "new_record_ids": NEW_IDS,
        "public_log": {
            "bytes": report["public_bytes"],
            "sha256": report["public_sha256"],
        },
        "ledger": {"bytes": report["ledger_bytes"], "sha256": report["ledger_sha256"]},
        "payload_manifest_rows": len(payload_rows),
        "direct_upload_objects": len(upload_rows),
        "zip": zip_info,
        "files_before_validation": len(before_validation),
        "canonical_tree_sha256": canonical_tree_sha(before_validation),
        "methodology_existing_concept": "10.5281/zenodo.21124403",
        "replication_existing_concept": "10.5281/zenodo.20461174",
        "new_concept_authorized": False,
    }
    write_json(temp / PACKAGE_VALIDATION_NAME, package_validation)
    return package_validation


def main() -> None:
    if FINAL.exists():
        raise RuntimeError(f"refusing to overwrite immutable v3 package: {FINAL}")
    FINAL.parent.mkdir(parents=True, exist_ok=True)
    temp = Path(tempfile.mkdtemp(prefix=f".{FINAL.name}.building-", dir=FINAL.parent))
    try:
        validation = build(temp)
        os.replace(temp, FINAL)
    except Exception:
        print(json.dumps({"status": "FAILED", "preserved_incomplete_temp": str(temp)}, indent=2))
        raise
    print(
        json.dumps(
            {
                "status": "PASS",
                "root": str(FINAL),
                "files": len([p for p in FINAL.rglob("*") if p.is_file()]),
                "bytes": sum(p.stat().st_size for p in FINAL.rglob("*") if p.is_file()),
                "records": validation["records"],
                "public_log": validation["public_log"],
                "ledger": validation["ledger"],
                "zip": validation["zip"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
