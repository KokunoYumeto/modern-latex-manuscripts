#!/usr/bin/env python3
"""Inventory and verify the four preserved failed EGA p.138 build roots.

Use ``snapshot`` before the bounded native PowerShell moves and ``verify``
afterward.  The script never deletes or overwrites a source generation.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
PRIVATE_PARENT = Path(
    r"C:\Users\Floris\Documents\interlanguage\03_projects\language_management"
    r"\english_germanic\90_logs\private_archive_custody"
)
PUBLIC_BUILD_PARENT = REPO / "sources/ega/checkpoints"
DESTINATION = PRIVATE_PARENT / "EGA_I_P138_FAILED_BUILD_HISTORY_20260804_r1"
GENERATIONS = DESTINATION / "generations"
MANIFEST = DESTINATION / "FAILED_BUILD_FILE_MANIFEST.csv"
ROOTS_TABLE = DESTINATION / "FAILED_BUILD_ROOTS.csv"

SOURCES = (
    (
        PRIVATE_PARENT / ".EGA_I_P138_R61_R82_PRIVATE_RAW_CUSTODY_20260804_r1.building-hsl45ued",
        PRIVATE_PARENT,
        "private freeze aborted because the sealed R82/R61 control generation changed during the stability boundary",
    ),
    (
        PUBLIC_BUILD_PARENT / ".ega1-p138-diplomatic-prestacks-r1-20260804.building-3k1hgz9t",
        PUBLIC_BUILD_PARENT,
        "public projection rejected because TeX build logs had not yet entered the privacy-transform surface",
    ),
    (
        PUBLIC_BUILD_PARENT / ".ega1-p138-diplomatic-prestacks-r1-20260804.building-zmh7p9gu",
        PUBLIC_BUILD_PARENT,
        "public projection rejected when the toolchain provenance email was first encountered before classification",
    ),
    (
        PUBLIC_BUILD_PARENT / ".ega1-p138-diplomatic-prestacks-r1-20260804.building-ufwog58f",
        PUBLIC_BUILD_PARENT,
        "public projection rejected because its first allowlist gate recounted the classified toolchain address inside generated validation",
    ),
)


def sha256_path(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(4 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def canonical_tree(rows: list[dict[str, object]]) -> str:
    payload = "".join(
        f"{row['generation']}\t{row['relative_path']}\t{row['bytes']}\t{row['sha256']}\n"
        for row in sorted(rows, key=lambda item: (str(item["generation"]), str(item["relative_path"])))
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest().upper()


def list_rows(root: Path, generation: str) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for path in sorted(
        (item for item in root.rglob("*") if item.is_file()),
        key=lambda item: item.relative_to(root).as_posix(),
    ):
        rows.append(
            {
                "generation": generation,
                "relative_path": path.relative_to(root).as_posix(),
                "bytes": path.stat().st_size,
                "sha256": sha256_path(path),
            }
        )
    return rows


def write_json(path: Path, value: object) -> None:
    path.write_text(
        json.dumps(value, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def snapshot() -> None:
    if DESTINATION.exists():
        raise RuntimeError(f"refusing to overwrite existing custody root: {DESTINATION}")
    for source, expected_parent, _reason in SOURCES:
        if not source.is_dir():
            raise RuntimeError(f"missing failed build root: {source}")
        if source.resolve().parent != expected_parent.resolve():
            raise RuntimeError(f"failed build root escaped expected parent: {source}")
    GENERATIONS.mkdir(parents=True)

    rows: list[dict[str, object]] = []
    roots: list[dict[str, object]] = []
    for source, expected_parent, reason in SOURCES:
        generation_rows = list_rows(source, source.name)
        rows.extend(generation_rows)
        roots.append(
            {
                "generation": source.name,
                "original_absolute_path": str(source),
                "verified_parent": str(expected_parent.resolve()),
                "failure_disposition": reason,
                "files": len(generation_rows),
                "bytes": sum(int(row["bytes"]) for row in generation_rows),
                "destination_relative_path": f"generations/{source.name}",
            }
        )

    with MANIFEST.open("w", encoding="utf-8", newline="") as handle:
        fields = ("generation", "relative_path", "bytes", "sha256")
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    with ROOTS_TABLE.open("w", encoding="utf-8", newline="") as handle:
        fields = (
            "generation",
            "original_absolute_path",
            "verified_parent",
            "failure_disposition",
            "files",
            "bytes",
            "destination_relative_path",
        )
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(roots)
    (DESTINATION / "README.md").write_text(
        "# Private adverse build history: EGA I printed p.138\n\n"
        "These four no-overwrite roots are failed builder generations, retained as evidence rather than staged, deleted, or presented as a public package. The exact pre-move file manifest binds every extant byte; one private freeze root is intentionally empty. `FAILED_BUILD_ROOTS.csv` records each rejection reason and original path. After bounded native moves, `POSTMOVE_VALIDATION.json` proves that all represented bytes arrived unchanged and that all four roots, including the empty one, remain present.\n",
        encoding="utf-8",
        newline="\n",
    )
    write_json(
        DESTINATION / "PREMOVE_VALIDATION.json",
        {
            "status": "PASS_PREMOVE_EXACT_FAILED_BUILD_CAPTURE",
            "errors": [],
            "roots": len(roots),
            "files": len(rows),
            "bytes": sum(int(row["bytes"]) for row in rows),
            "canonical_tree_sha256": canonical_tree(rows),
            "empty_roots": sum(1 for row in roots if int(row["files"]) == 0),
            "source_roots_mutated": False,
            "next_action": "move the four exact roots with native PowerShell into their declared destination paths, then run verify",
        },
    )
    print(json.dumps({"status": "PASS_PREMOVE", "destination": str(DESTINATION), "roots": roots}, indent=2))


def verify() -> None:
    if not MANIFEST.is_file() or not ROOTS_TABLE.is_file():
        raise RuntimeError("pre-move custody controls are missing")
    with MANIFEST.open("r", encoding="utf-8-sig", newline="") as handle:
        wanted_rows = list(csv.DictReader(handle))
    with ROOTS_TABLE.open("r", encoding="utf-8-sig", newline="") as handle:
        roots = list(csv.DictReader(handle))
    errors: list[dict[str, object]] = []
    observed_rows: list[dict[str, object]] = []
    for root_row in roots:
        generation = root_row["generation"]
        destination = GENERATIONS / generation
        if not destination.is_dir():
            errors.append({"error": "missing_generation_root", "generation": generation})
            continue
        observed_rows.extend(list_rows(destination, generation))
    wanted = {
        (row["generation"], row["relative_path"]): (int(row["bytes"]), row["sha256"].upper())
        for row in wanted_rows
    }
    observed = {
        (str(row["generation"]), str(row["relative_path"])): (int(row["bytes"]), str(row["sha256"]))
        for row in observed_rows
    }
    if set(wanted) - set(observed):
        errors.append({"error": "missing_files", "count": len(set(wanted) - set(observed))})
    if set(observed) - set(wanted):
        errors.append({"error": "extra_files", "count": len(set(observed) - set(wanted))})
    mismatches = [key for key in set(wanted) & set(observed) if wanted[key] != observed[key]]
    if mismatches:
        errors.append({"error": "identity_mismatches", "count": len(mismatches)})
    if canonical_tree(observed_rows) != canonical_tree(
        [
            {
                "generation": row["generation"],
                "relative_path": row["relative_path"],
                "bytes": int(row["bytes"]),
                "sha256": row["sha256"].upper(),
            }
            for row in wanted_rows
        ]
    ):
        errors.append({"error": "canonical_tree_mismatch"})
    source_roots_remaining = [str(source) for source, _parent, _reason in SOURCES if source.exists()]
    if source_roots_remaining:
        errors.append({"error": "source_roots_not_moved", "paths": source_roots_remaining})
    receipt = {
        "status": "PASS_POSTMOVE_EXACT_FAILED_BUILD_CUSTODY" if not errors else "FAIL",
        "errors": errors,
        "roots": len(roots),
        "files": len(observed_rows),
        "bytes": sum(int(row["bytes"]) for row in observed_rows),
        "canonical_tree_sha256": canonical_tree(observed_rows),
        "empty_roots_preserved": sum(
            1 for row in roots if not any(item["generation"] == row["generation"] for item in observed_rows)
        ),
        "original_source_roots_remaining": len(source_roots_remaining),
    }
    target = DESTINATION / "POSTMOVE_VALIDATION.json"
    if target.exists():
        raise RuntimeError(f"refusing to overwrite post-move receipt: {target}")
    write_json(target, receipt)
    print(json.dumps(receipt, indent=2))
    if errors:
        raise SystemExit(1)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=("snapshot", "verify"))
    args = parser.parse_args()
    if args.action == "snapshot":
        snapshot()
    else:
        verify()


if __name__ == "__main__":
    main()
