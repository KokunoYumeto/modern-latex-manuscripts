#!/usr/bin/env python3
"""Freeze private and privacy-clean public snapshots for Korean Noether papers.

The builder is bounded to five explicit producer roots.  It performs no render,
compile, OCR, or source correction.  Every source byte is preserved in a private
deterministic ZIP.  The public projection minimally replaces private machine
path/name tokens in text and excludes one explicitly private P42 coordination
screenshot while retaining its exact identity and exclusion rationale.
"""

from __future__ import annotations

import csv
import hashlib
import json
import os
import re
import shutil
import zipfile
from datetime import datetime, timezone
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
USER_PROFILE_ROOT = Path.home()
DOCUMENTS_ROOT = USER_PROFILE_ROOT / "Documents"
PAPERS_ROOT = DOCUMENTS_ROOT / "Papors"
INTERLANGUAGE_ROOT = Path(
    os.environ.get(
        "INTERLANGUAGE_ROOT",
        str(DOCUMENTS_ROOT / "interlanguage"),
    )
)
LANGUAGE_MANAGEMENT_ROOT = (
    INTERLANGUAGE_ROOT / "03_projects" / "language_management"
)
SOURCE_BASE = LANGUAGE_MANAGEMENT_ROOT / "cjk" / "03_working_translations"
CJK_CONTROL = LANGUAGE_MANAGEMENT_ROOT / "cjk" / "00_lane_control"
METHODOLOGY_SOURCE = (
    INTERLANGUAGE_ROOT
    / "04_handoffs"
    / "methodology_lessons_20260718"
    / "CJK_KOREAN_PRODUCTION_LESSONS_20260718.md"
)
NOETHER_CONTROL_ROOT = (
    INTERLANGUAGE_ROOT / "03_projects" / "noether" / "07_german_canon_control"
)
POINTER_SOURCE = (
    NOETHER_CONTROL_ROOT
    / "pointers"
    / "NOETH_DE_AUTHORITY_POINTER_v003_20260804.json"
)
P41_BINDER_SOURCE = (
    NOETHER_CONTROL_ROOT
    / "receipts"
    / "KOREAN_P41_U01_U12_BINDER_20260804.json"
)
ARCHIVE_WIDE_POLICY = (
    REPO_ROOT
    / "manifests"
    / "source-intake"
    / "20260804_archive_wide_immediate_mathematics_publication_no_hold_policy.md"
)
PRIVATE_ROOT = (
    LANGUAGE_MANAGEMENT_ROOT
    / "cjk"
    / "90_logs"
    / "private_archive_custody"
    / "KOREAN_NOETHER_P01_P05_P07_P41_P42_SNAPSHOT_20260804_r2"
)
PUBLIC_ROOT = (
    REPO_ROOT
    / "sources"
    / "noether"
    / "korean-unchecked-papers-01-05-07-41-42-20260804"
)

PAPERS = {
    "P01": {
        "root": "noether_paper01_ko_translation_001_20260804",
        "targets": 3,
        "structural": "evidence/structural_index/PRODUCER_STRUCTURAL_INDEX.jsonl",
        "difficulty": "evidence/difficulty_ledger/DIFFICULTY_LEDGER.jsonl",
    },
    "P05": {
        "root": "noether_paper05_ko_translation_001_20260804",
        "targets": 4,
        "structural": "evidence/structural_index/PRODUCER_STRUCTURAL_INDEX.jsonl",
        "difficulty": "evidence/difficulty/DIFFICULTY_LEDGER.jsonl",
    },
    "P07": {
        "root": "noether_paper07_ko_translation_001_20260804",
        "targets": 8,
        "structural": "reproducibility/structural/STRUCTURAL_INDEX.jsonl",
        "difficulty": "reproducibility/difficulty/DIFFICULTY_LEDGER.jsonl",
    },
    "P41": {
        "root": "noether_paper41_ko_translation_001_20260804",
        "targets": 12,
        "structural": "evidence/structural_index/PRODUCER_STRUCTURAL_INDEX.jsonl",
        "difficulty": "evidence/difficulty/difficulty_ledger.jsonl",
    },
    "P42": {
        "root": "noether_paper42_ko_translation_001_20260804",
        "targets": 12,
        "structural": "evidence/structural_index/PRODUCER_STRUCTURAL_INDEX.jsonl",
        "difficulty": "evidence/difficulty_ledger/DIFFICULTY_LEDGER.jsonl",
    },
}

EXCLUDED_RELATIVE_PATHS = {
    "P42": {
        "evidence/visual_evidence/private_coordination/"
        "codex_task_sidebar_context_20260804.png": (
            "private user-supplied coordination screenshot; no mathematical source, "
            "equation, target render, or publication right asserted"
        )
    }
}

TEXT_SUFFIXES = {
    ".csv",
    ".json",
    ".jsonl",
    ".md",
    ".mjs",
    ".ps1",
    ".tex",
    ".txt",
}


def literal_path_pattern(path: Path, forward_slashes: bool) -> re.Pattern[bytes]:
    text = str(path)
    if forward_slashes:
        text = text.replace("\\", "/")
    else:
        text = text.replace("/", "\\")
    return re.compile(re.escape(text.encode("utf-8")), re.IGNORECASE)


REPLACEMENTS = [
    (
        "PRIVATE_INTERLANGUAGE_ROOT_FORWARD_SLASH",
        literal_path_pattern(INTERLANGUAGE_ROOT, True),
        b"${PUBLIC_INTERLANGUAGE_ROOT}",
    ),
    (
        "PRIVATE_PAPERS_ROOT_FORWARD_SLASH",
        literal_path_pattern(PAPERS_ROOT, True),
        b"${PUBLIC_PAPERS_ROOT}",
    ),
    (
        "PRIVATE_DOCUMENTS_ROOT_FORWARD_SLASH",
        literal_path_pattern(DOCUMENTS_ROOT, True),
        b"${PUBLIC_DOCUMENTS_ROOT}",
    ),
    (
        "PRIVATE_USER_ROOT_FORWARD_SLASH",
        literal_path_pattern(USER_PROFILE_ROOT, True),
        b"${PRIVATE_USER_ROOT}",
    ),
    (
        "PRIVATE_INTERLANGUAGE_ROOT",
        literal_path_pattern(INTERLANGUAGE_ROOT, False),
        b"${PUBLIC_INTERLANGUAGE_ROOT}",
    ),
    (
        "PRIVATE_PAPERS_ROOT",
        literal_path_pattern(PAPERS_ROOT, False),
        b"${PUBLIC_PAPERS_ROOT}",
    ),
    (
        "PRIVATE_DOCUMENTS_ROOT",
        literal_path_pattern(DOCUMENTS_ROOT, False),
        b"${PUBLIC_DOCUMENTS_ROOT}",
    ),
    (
        "PRIVATE_USER_ROOT",
        literal_path_pattern(USER_PROFILE_ROOT, False),
        b"${PRIVATE_USER_ROOT}",
    ),
    (
        "OPERATOR_NAME",
        re.compile(
            rb"\b" + re.escape(USER_PROFILE_ROOT.name.encode("utf-8")) + rb"\b",
            re.IGNORECASE,
        ),
        b"PROJECT_COORDINATOR",
    ),
]

PRIVATE_PATTERNS = {
    "windows_user_root": re.compile(rb"(?i)[A-Z]:\\Users\\"),
    "posix_home": re.compile(rb"(?i)(?:/home/|/Users/)[^/\r\n]+"),
    "operator_name": re.compile(
        rb"\b" + re.escape(USER_PROFILE_ROOT.name.encode("utf-8")) + rb"\b",
        re.IGNORECASE,
    ),
    "email": re.compile(
        rb"(?i)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b"
    ),
    "token": re.compile(
        rb"(?i)(?:api[_-]?key|access[_-]?token|authorization\s*:)"
        rb"\s*[=:]?\s*[A-Za-z0-9_-]{20,}"
    ),
}

ZIP_DATE = (1980, 1, 1, 0, 0, 0)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(4 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def inventory(root: Path) -> list[dict]:
    rows = []
    for path in sorted(
        (item for item in root.rglob("*") if item.is_file()),
        key=lambda item: item.relative_to(root).as_posix(),
    ):
        rows.append(
            {
                "relative_path": path.relative_to(root).as_posix(),
                "bytes": path.stat().st_size,
                "sha256": sha256_file(path),
                "path": path,
            }
        )
    return rows


def tree_sha(rows: list[dict], *, hash_key: str = "sha256") -> str:
    material = "".join(
        f"{row['relative_path']}\t{int(row['bytes'])}\t{row[hash_key]}\n"
        for row in sorted(rows, key=lambda item: item["relative_path"])
    ).encode("utf-8")
    return sha256_bytes(material)


def write_text(path: Path, value: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(value, encoding="utf-8", newline="\n")


def write_json(path: Path, value: object) -> None:
    write_text(path, json.dumps(value, ensure_ascii=True, indent=2) + "\n")


def write_csv(path: Path, fields: list[str], rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def deterministic_zip(path: Path, members: list[tuple[str, bytes]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    with zipfile.ZipFile(
        temporary,
        "w",
        compression=zipfile.ZIP_DEFLATED,
        compresslevel=9,
        allowZip64=True,
    ) as archive:
        for name, data in sorted(members, key=lambda item: item[0]):
            info = zipfile.ZipInfo(name, ZIP_DATE)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 0
            info.external_attr = 0
            archive.writestr(info, data, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    temporary.replace(path)


def transform_text(data: bytes) -> tuple[bytes, list[tuple[str, int]]]:
    transformed = data
    applied: list[tuple[str, int]] = []
    for rule_id, pattern, replacement in REPLACEMENTS:
        transformed, count = pattern.subn(replacement, transformed)
        if count:
            applied.append((rule_id, count))
    return transformed, applied


def assert_privacy_clean(path: str, data: bytes) -> None:
    hits = {
        label: len(pattern.findall(data))
        for label, pattern in PRIVATE_PATTERNS.items()
    }
    hits = {label: count for label, count in hits.items() if count}
    if hits:
        raise RuntimeError(f"Public privacy scan failed for {path}: {hits}")


def build_paper(paper: str, config: dict) -> dict:
    source_root = SOURCE_BASE / config["root"]
    if not source_root.is_dir():
        raise RuntimeError(f"Missing bounded producer root: {source_root}")
    before = inventory(source_root)
    source_tree = tree_sha(before)
    private_paper = PRIVATE_ROOT / paper
    public_paper = PUBLIC_ROOT / paper
    private_paper.mkdir(parents=True, exist_ok=False)
    public_paper.mkdir(parents=True, exist_ok=False)

    raw_members = [
        (row["relative_path"], Path(row["path"]).read_bytes()) for row in before
    ]
    raw_zip = private_paper / f"{paper}_EXACT_PRIVATE_SOURCE_SNAPSHOT_20260804.zip"
    deterministic_zip(raw_zip, raw_members)

    private_manifest_rows = [
        {
            "relative_path": row["relative_path"],
            "bytes": row["bytes"],
            "sha256": row["sha256"],
        }
        for row in before
    ]
    write_csv(
        private_paper / "EXACT_SOURCE_MANIFEST.csv",
        ["relative_path", "bytes", "sha256"],
        private_manifest_rows,
    )

    projection_rows: list[dict] = []
    transformation_rows: list[dict] = []
    excluded = EXCLUDED_RELATIVE_PATHS.get(paper, {})
    public_source_files: list[Path] = []
    for row in before:
        relative = row["relative_path"]
        source = Path(row["path"])
        if relative in excluded:
            projection_rows.append(
                {
                    "relative_path": relative,
                    "source_bytes": row["bytes"],
                    "source_sha256": row["sha256"],
                    "public_bytes": "",
                    "public_sha256": "",
                    "privacy_transformations": 0,
                    "disposition": "EXCLUDE_PRIVATE_COORDINATION_IMAGE",
                    "rationale": excluded[relative],
                }
            )
            continue
        data = source.read_bytes()
        applied: list[tuple[str, int]] = []
        if source.suffix.lower() in TEXT_SUFFIXES:
            data, applied = transform_text(data)
            assert_privacy_clean(relative, data)
        destination = public_paper / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(data)
        public_source_files.append(destination)
        projection_rows.append(
            {
                "relative_path": relative,
                "source_bytes": row["bytes"],
                "source_sha256": row["sha256"],
                "public_bytes": len(data),
                "public_sha256": sha256_bytes(data),
                "privacy_transformations": sum(count for _, count in applied),
                "disposition": "PUBLIC_INCLUDE",
                "rationale": (
                    "minimal private-token substitution"
                    if applied
                    else "byte-identical source projection"
                ),
            }
        )
        for rule_id, count in applied:
            transformation_rows.append(
                {
                    "relative_path": relative,
                    "rule_id": rule_id,
                    "occurrences": count,
                    "source_sha256": row["sha256"],
                    "public_sha256": sha256_bytes(data),
                    "semantic_scope": "private path/operator token only; mathematical text unchanged",
                }
            )

    manifest_path = public_paper / "ARCHIVE_PUBLIC_PROJECTION_MANIFEST.csv"
    privacy_path = public_paper / "ARCHIVE_PRIVACY_TRANSFORMATIONS.csv"
    readme_path = public_paper / "ARCHIVE_PUBLICATION_README.md"
    validation_path = public_paper / "ARCHIVE_SNAPSHOT_VALIDATION.json"
    write_csv(
        manifest_path,
        [
            "relative_path",
            "source_bytes",
            "source_sha256",
            "public_bytes",
            "public_sha256",
            "privacy_transformations",
            "disposition",
            "rationale",
        ],
        projection_rows,
    )
    write_csv(
        privacy_path,
        [
            "relative_path",
            "rule_id",
            "occurrences",
            "source_sha256",
            "public_sha256",
            "semantic_scope",
        ],
        transformation_rows,
    )
    exclusion_note = (
        "For P42, the only excluded byte is one private user-supplied coordination "
        "screenshot; its exact identity and exclusion remain in the manifest and "
        "visual index, and it is not mathematical source evidence."
        if paper == "P42"
        else "No producer file is excluded from this bounded public projection."
    )
    write_text(
        readme_path,
        f"""# Korean Noether {paper} bounded public snapshot

This is the exact bounded producer state captured on 2026-08-04, projected for public preservation under the archive-wide immediate-publication/no-hold policy.

State: **UNCHECKED, uncompiled, unrendered, unassembled, and unreviewed**. Those labels are not certification and are not release holds. No mathematical checking, source correction, compilation, rendering, or approval was performed by archive maintenance.

- Source files captured: {len(before)} / {sum(int(row['bytes']) for row in before):,} bytes
- Source tree SHA-256: `{source_tree}`
- Public source files included: {len(public_source_files)}
- Explicit exclusions: {len(excluded)}
- Privacy substitutions: {sum(int(row['occurrences']) for row in transformation_rows)}
- Editable Korean target units: {config['targets']}

Every source identity, public identity, minimal privacy substitution, and exclusion is recorded in the adjacent manifest and privacy ledger. All difficulty/failure, structural, decision, checker, source-custody, and continuation evidence remains included. {exclusion_note}
""",
    )

    represented_files = [
        path
        for path in sorted(
            (item for item in public_paper.rglob("*") if item.is_file()),
            key=lambda item: item.relative_to(public_paper).as_posix(),
        )
        if path.name != validation_path.name
    ]
    represented_rows = [
        {
            "relative_path": path.relative_to(public_paper).as_posix(),
            "bytes": path.stat().st_size,
            "sha256": sha256_file(path),
        }
        for path in represented_files
    ]
    represented_tree = tree_sha(represented_rows)
    validation = {
        "schema": "korean_noether_unchecked_public_snapshot_validation_v1",
        "paper": paper,
        "status": "PASS_PUBLIC_UNCHECKED_SNAPSHOT",
        "errors": [],
        "state_labels": [
            "UNCHECKED",
            "uncompiled",
            "unrendered",
            "unassembled",
            "unreviewed",
        ],
        "source_files": len(before),
        "source_bytes": sum(int(row["bytes"]) for row in before),
        "source_tree_sha256": source_tree,
        "public_source_files": len(public_source_files),
        "explicit_exclusions": len(excluded),
        "privacy_transformation_rows": len(transformation_rows),
        "privacy_transformation_occurrences": sum(
            int(row["occurrences"]) for row in transformation_rows
        ),
        "represented_public_files_excluding_this_validation": len(represented_rows),
        "represented_public_bytes_excluding_this_validation": sum(
            int(row["bytes"]) for row in represented_rows
        ),
        "represented_public_tree_sha256": represented_tree,
        "target_units": config["targets"],
        "compile_performed": False,
        "render_performed": False,
        "review_performed": False,
        "release_hold": False,
    }
    write_json(validation_path, validation)

    zip_members = [
        (
            path.relative_to(public_paper).as_posix(),
            path.read_bytes(),
        )
        for path in sorted(
            (item for item in public_paper.rglob("*") if item.is_file()),
            key=lambda item: item.relative_to(public_paper).as_posix(),
        )
    ]
    public_zip = PUBLIC_ROOT / f"{paper}_Korean_UNCHECKED_Public_Snapshot_20260804.zip"
    deterministic_zip(public_zip, zip_members)
    with zipfile.ZipFile(public_zip) as archive:
        if archive.testzip() is not None or len(archive.infolist()) != len(zip_members):
            raise RuntimeError(f"Public ZIP replay failed for {paper}")

    after = inventory(source_root)
    if [
        (row["relative_path"], row["bytes"], row["sha256"]) for row in after
    ] != [
        (row["relative_path"], row["bytes"], row["sha256"]) for row in before
    ]:
        raise RuntimeError(f"Producer root changed during bounded snapshot: {paper}")

    private_receipt = {
        "schema": "korean_noether_private_exact_snapshot_receipt_v1",
        "paper": paper,
        "captured_utc": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "source_root": str(source_root),
        "source_files": len(before),
        "source_bytes": sum(int(row["bytes"]) for row in before),
        "source_tree_sha256": source_tree,
        "private_zip": raw_zip.name,
        "private_zip_bytes": raw_zip.stat().st_size,
        "private_zip_sha256": sha256_file(raw_zip),
        "source_stable_before_after": True,
        "public_projection_root": str(public_paper),
        "public_zip": public_zip.name,
        "public_zip_bytes": public_zip.stat().st_size,
        "public_zip_sha256": sha256_file(public_zip),
        "public_zip_members": len(zip_members),
        "excluded_relative_paths": excluded,
        "release_hold": False,
    }
    write_json(private_paper / "PRIVATE_SNAPSHOT_RECEIPT.json", private_receipt)
    return {
        "paper": paper,
        "source_files": len(before),
        "source_bytes": sum(int(row["bytes"]) for row in before),
        "source_tree_sha256": source_tree,
        "public_source_files": len(public_source_files),
        "privacy_occurrences": validation["privacy_transformation_occurrences"],
        "excluded_files": len(excluded),
        "public_zip": public_zip.name,
        "public_zip_bytes": public_zip.stat().st_size,
        "public_zip_sha256": sha256_file(public_zip),
        "public_zip_members": len(zip_members),
        "private_zip": str(raw_zip),
        "private_zip_bytes": raw_zip.stat().st_size,
        "private_zip_sha256": sha256_file(raw_zip),
        "target_units": config["targets"],
        "structural_relative_path": config["structural"],
        "difficulty_relative_path": config["difficulty"],
    }


def project_control(source: Path, destination: Path) -> dict:
    data = source.read_bytes()
    transformed, applied = transform_text(data)
    assert_privacy_clean(destination.name, transformed)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(transformed)
    return {
        "filename": destination.name,
        "source_bytes": len(data),
        "source_sha256": sha256_bytes(data),
        "public_bytes": len(transformed),
        "public_sha256": sha256_bytes(transformed),
        "privacy_occurrences": sum(count for _, count in applied),
    }


def main() -> int:
    if PRIVATE_ROOT.exists() or PUBLIC_ROOT.exists():
        raise RuntimeError(
            "Snapshot target already exists; preserve it and use a new revision rather than overwriting"
        )
    PRIVATE_ROOT.mkdir(parents=True)
    PUBLIC_ROOT.mkdir(parents=True)
    paper_results = [build_paper(paper, config) for paper, config in PAPERS.items()]

    common_sources = [
        (
            CJK_CONTROL / "KOREAN_ARCHIVE_PUBLICATION_POLICY_RECEIPT_20260804.md",
            "70_KO_ARCHIVE_PUBLICATION_POLICY_RECEIPT_20260804.md",
        ),
        (
            CJK_CONTROL / "CJK_DECISION_LOGBOOK_20260718.md",
            "70_KO_CJK_DECISION_LOGBOOK_PRIVACY_CLEAN_20260804.md",
        ),
        (
            METHODOLOGY_SOURCE,
            "70_KO_CJK_PRODUCTION_METHODOLOGY_PRIVACY_CLEAN_20260804.md",
        ),
        (
            ARCHIVE_WIDE_POLICY,
            "70_KO_ARCHIVE_WIDE_IMMEDIATE_PUBLICATION_NO_HOLD_POLICY_20260804.md",
        ),
        (
            POINTER_SOURCE,
            "70_KO_NOETH_DE_AUTHORITY_POINTER_v003_20260804.json",
        ),
        (
            P41_BINDER_SOURCE,
            "70_KO_P41_U01_U12_BINDER_20260804.json",
        ),
    ]
    common_results = [
        project_control(source, PUBLIC_ROOT / name) for source, name in common_sources
    ]

    index_path = PUBLIC_ROOT / "70_KO_P01_P05_P07_P41_P42_SNAPSHOT_INDEX_20260804.csv"
    write_csv(
        index_path,
        [
            "paper",
            "source_files",
            "source_bytes",
            "source_tree_sha256",
            "public_source_files",
            "privacy_occurrences",
            "excluded_files",
            "public_zip",
            "public_zip_bytes",
            "public_zip_sha256",
            "public_zip_members",
            "target_units",
            "structural_relative_path",
            "difficulty_relative_path",
            "state",
        ],
        [
            {
                **{key: value for key, value in row.items() if not key.startswith("private_")},
                "state": "UNCHECKED;uncompiled;unrendered;unassembled;unreviewed",
            }
            for row in paper_results
        ],
    )

    readme_path = PUBLIC_ROOT / "README.md"
    write_text(
        readme_path,
        """# Korean Noether papers 1, 5, 7, 41, and 42 — bounded public snapshots

These snapshots preserve every current mathematical target and every structural, difficulty/failure, decision, source-custody, checker, continuation, and validator surface from five bounded Korean producer roots. Their state is **UNCHECKED, uncompiled, unrendered, unassembled, and unreviewed**. Those labels are honest scope metadata, not release holds.

Each paper has one complete privacy-clean ZIP, directly readable status/checker/translation-choice files, direct editable Korean TeX units, and direct structural and difficulty ledgers. Exact raw producer bytes are separately frozen in private custody. Public transformations replace only private local path/operator tokens. P42's one private coordination screenshot is excluded; its exact identity and exclusion remain recorded. No mathematical source image or target render exists in these snapshots.

The archive-wide no-hold rule and Korean-lane adoption receipt are direct controls. No compile, render, OCR, source correction, mathematical review, linguistic review, certification, or approval was performed by archive maintenance.
""",
    )

    public_files = inventory(PUBLIC_ROOT)
    validation = {
        "schema": "korean_noether_five_paper_public_snapshot_closeout_v1",
        "status": "PASS_READY_FOR_SAME_CONCEPT_PUBLICATION",
        "errors": [],
        "papers": paper_results,
        "common_controls": common_results,
        "public_root_files": len(public_files),
        "public_root_bytes": sum(int(row["bytes"]) for row in public_files),
        "public_root_tree_sha256": tree_sha(public_files),
        "private_custody_root": str(PRIVATE_ROOT),
        "public_projection_root": str(PUBLIC_ROOT),
        "total_source_files": sum(int(row["source_files"]) for row in paper_results),
        "total_source_bytes": sum(int(row["source_bytes"]) for row in paper_results),
        "total_target_units": sum(int(row["target_units"]) for row in paper_results),
        "total_explicit_exclusions": sum(int(row["excluded_files"]) for row in paper_results),
        "compile_performed": False,
        "render_performed": False,
        "review_performed": False,
        "release_hold": False,
    }
    validation_path = PUBLIC_ROOT / "SNAPSHOT_VALIDATION.json"
    write_json(validation_path, validation)
    print(json.dumps(validation, ensure_ascii=True, indent=2))
    print(
        json.dumps(
            {
                "validation_path": str(validation_path),
                "validation_bytes": validation_path.stat().st_size,
                "validation_sha256": sha256_file(validation_path),
                "index_path": str(index_path),
                "index_bytes": index_path.stat().st_size,
                "index_sha256": sha256_file(index_path),
                "readme_bytes": readme_path.stat().st_size,
                "readme_sha256": sha256_file(readme_path),
            },
            ensure_ascii=True,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
