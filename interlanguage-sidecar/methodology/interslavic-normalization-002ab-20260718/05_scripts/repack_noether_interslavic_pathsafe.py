#!/usr/bin/env python3
"""Repack the Noether Interslavic release with short internal paths."""

from __future__ import annotations

import csv
import hashlib
import os
import shutil
import zipfile
from pathlib import Path


STAGE = Path(
    r"C:\Users\Floris\Documents\Codex\2026-05-26"
    r"\there-is-currently-an-ongoing-process\publish_curated"
    r"\20260718_noether_interslavic_002ab"
)
SOURCE = STAGE / "Noether_Interslavic_WorkingCorpus_Normalization_002A_002B_20260718"
DEST = STAGE / "Noether_ISV_002AB_20260718"
ZIP_PATH = STAGE / "11_Noether_Interslavic_WorkingCorpus_Normalization_002A_002B_20260718.zip"
TEMP_ZIP = STAGE / "11_Noether_Interslavic_WorkingCorpus_Normalization_002A_002B_20260718.pathsafe.tmp.zip"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def bounded_name(index: int, source: Path, limit: int = 100) -> str:
    name = f"{index:04d}_{source.name}"
    if len(name) <= limit:
        return name
    suffix = source.suffix
    digest = hashlib.sha256(source.as_posix().encode("utf-8")).hexdigest()[:10]
    room = limit - len(f"{index:04d}__{digest}{suffix}")
    stem = source.stem[: max(room, 20)]
    return f"{index:04d}_{stem}_{digest}{suffix}"


def copy_preserved(relative: str) -> None:
    source = SOURCE / relative
    target = DEST / relative
    if source.is_dir():
        shutil.copytree(source, target)
    elif source.is_file():
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)


def flatten_tree(source: Path, target: Path, rows: list[dict[str, str]]) -> None:
    files = sorted(path for path in source.rglob("*") if path.is_file())
    target.mkdir(parents=True, exist_ok=True)
    for index, path in enumerate(files, start=1):
        destination = target / bounded_name(index, path)
        shutil.copy2(path, destination)
        rows.append(
            {
                "package_path": destination.relative_to(DEST).as_posix(),
                "original_package_path": path.relative_to(SOURCE).as_posix(),
                "bytes": str(destination.stat().st_size),
                "sha256": sha256(destination),
            }
        )


def write_path_map(rows: list[dict[str, str]]) -> None:
    path = DEST / "PATH_MAP.csv"
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["package_path", "original_package_path", "bytes", "sha256"],
        )
        writer.writeheader()
        writer.writerows(rows)


def write_hashes() -> None:
    path = DEST / "SHA256SUMS.csv"
    files = sorted(item for item in DEST.rglob("*") if item.is_file() and item != path)
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["relative_path", "bytes", "sha256"])
        for item in files:
            writer.writerow([item.relative_to(DEST).as_posix(), item.stat().st_size, sha256(item)])


def main() -> None:
    if not SOURCE.is_dir():
        raise RuntimeError(f"Missing source package: {SOURCE}")
    if DEST.exists() or TEMP_ZIP.exists():
        raise RuntimeError("Path-safe destination already exists; refusing to overwrite")
    DEST.mkdir(parents=True)
    for relative in (
        "00_README_STATUS.md",
        "UNIT_BUILD_MANIFEST.csv",
        "00_readers",
        "01_unit_pdfs",
        "02_tex",
        "05_build_logs",
        "06_workflow_scripts",
        "07_source_authority",
    ):
        copy_preserved(relative)

    path_map: list[dict[str, str]] = []
    support = SOURCE / "03_corpus_support"
    for category in sorted(path for path in support.iterdir() if path.is_dir()):
        flatten_tree(category, DEST / "03_support" / category.name, path_map)

    norm = SOURCE / "04_normalization_evidence"
    global_files = [path for path in norm.iterdir() if path.is_file()]
    global_target = DEST / "04_norm" / "global"
    global_target.mkdir(parents=True, exist_ok=True)
    for index, path in enumerate(sorted(global_files), start=1):
        destination = global_target / bounded_name(index, path)
        shutil.copy2(path, destination)
        path_map.append(
            {
                "package_path": destination.relative_to(DEST).as_posix(),
                "original_package_path": path.relative_to(SOURCE).as_posix(),
                "bytes": str(destination.stat().st_size),
                "sha256": sha256(destination),
            }
        )
    for tranche_name, short in (
        ("tranche_002a_orthography", "2a"),
        ("tranche_002b_lexical_exact", "2b"),
    ):
        tranche = norm / tranche_name
        for category in sorted(path for path in tranche.iterdir() if path.is_dir()):
            flatten_tree(category, DEST / "04_norm" / short / category.name, path_map)

    write_path_map(path_map)
    write_hashes()

    with zipfile.ZipFile(TEMP_ZIP, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as archive:
        for path in sorted(DEST.rglob("*")):
            if path.is_file():
                archive.write(path, f"{DEST.name}/{path.relative_to(DEST).as_posix()}")
    with zipfile.ZipFile(TEMP_ZIP, "r") as archive:
        bad = archive.testzip()
        if bad:
            raise RuntimeError(f"ZIP test failed at {bad}")
        names = [entry.filename for entry in archive.infolist()]
    longest = max(map(len, names))
    if longest > 200:
        raise RuntimeError(f"Longest internal path remains too long: {longest}")
    os.replace(TEMP_ZIP, ZIP_PATH)
    print(
        f"entries={len(names)} max_internal_path={longest} "
        f"bytes={ZIP_PATH.stat().st_size} sha256={sha256(ZIP_PATH)}"
    )


if __name__ == "__main__":
    main()
