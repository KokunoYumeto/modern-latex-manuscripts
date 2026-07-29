#!/usr/bin/env python3
"""Group loose historical SGA3 checkpoints behind the current cumulative reader."""

from __future__ import annotations

import csv
import hashlib
import io
import json
import urllib.parse
import zipfile
from pathlib import Path

import requests


REPO_ROOT = Path(__file__).resolve().parents[3]
PACKAGE_ROOT = Path(__file__).resolve().parent
RECEIPT = (
    REPO_ROOT
    / "manifests"
    / "published-zenodo"
    / "20260728_sga3_cumulative_with_x_record_21662699_public_readback.json"
)
SOURCE_RECORD = 21662699
FIXED_ZIP_TIME = (2026, 7, 29, 0, 0, 0)

THROUGH_XI = [
    "10c8_SGA3_CurrentProgress_Source_History_Latest_20260728.zip",
    (
        "10c_SGA3_Previous_Public_Component_Readers_and_"
        "Source_Archives_Through_XI_20260728.zip"
    ),
]

BOUNDED_EXPOSES = ("12", "13", "14", "19", "20", "21", "23", "25")
BOUNDED_FILES = [
    name
    for expose in BOUNDED_EXPOSES
    for name in (
        next(
            key
            for key in json.loads(RECEIPT.read_text(encoding="utf-8"))["files"]
            if key.startswith(f"00c{expose}_")
        ),
        next(
            key
            for key in json.loads(RECEIPT.read_text(encoding="utf-8"))["files"]
            if key.startswith(f"02c{expose}_")
        ),
        next(
            key
            for key in json.loads(RECEIPT.read_text(encoding="utf-8"))["files"]
            if key.startswith(f"10c{expose}_")
        ),
    )
]

GROUPS = {
    "10c1_SGA3_Previous_Public_History_Through_XI_20260729.zip": {
        "files": THROUGH_XI,
        "readme": (
            "# SGA3 previous public history through Expose XI\n\n"
            "This archive preserves the two exact predecessor-history archives "
            "removed from the direct Zenodo file list when the clean cumulative "
            "reader became the public reading surface. These bytes are historical "
            "provenance, not a competing current reader.\n"
        ),
        "role": "nested_predecessor_archive",
    },
    "10c2_SGA3_Bounded_Checkpoints_XII_XXV_20260729.zip": {
        "files": BOUNDED_FILES,
        "readme": (
            "# SGA3 bounded checkpoint history, Exposes XII-XXV\n\n"
            "This archive preserves eight exact bounded checkpoint trios: reader "
            "PDF, master TeX, and source/QA ZIP for Exposes XII, XIII, XIV, XIX, "
            "XX, XXI, XXIII, and XXV. The current cumulative reader contains the "
            "mathematical reading surface. These checkpoint bytes remain available "
            "for provenance and audit history rather than as loose front-list "
            "readers.\n"
        ),
        "role": "bounded_checkpoint_historical",
    },
}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def csv_bytes(rows: list[dict[str, object]]) -> bytes:
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(
        stream,
        fieldnames=("filename", "bytes", "sha256", "role"),
        lineterminator="\r\n",
    )
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue().encode("utf-8")


def zip_info(name: str) -> zipfile.ZipInfo:
    info = zipfile.ZipInfo(name, FIXED_ZIP_TIME)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = 0o100644 << 16
    return info


def fetch_exact(
    session: requests.Session,
    name: str,
    expected: dict[str, object],
) -> bytes:
    url = (
        f"https://zenodo.org/records/{SOURCE_RECORD}/files/"
        f"{urllib.parse.quote(name, safe='')}?download=1"
    )
    response = session.get(url, timeout=(30, 1800))
    response.raise_for_status()
    data = response.content
    observed = (len(data), sha256_bytes(data))
    wanted = (int(expected["bytes"]), str(expected["sha256"]).upper())
    if observed != wanted:
        raise RuntimeError(f"Remote identity mismatch: {name}")
    return data


def build_group(
    session: requests.Session,
    public_files: dict[str, dict[str, object]],
    archive_name: str,
    spec: dict[str, object],
) -> dict[str, object]:
    source_rows: list[dict[str, object]] = []
    source_data: list[tuple[str, bytes]] = []
    for name in spec["files"]:
        data = fetch_exact(session, name, public_files[name])
        source_data.append((name, data))
        source_rows.append(
            {
                "filename": name,
                "bytes": len(data),
                "sha256": sha256_bytes(data),
                "role": spec["role"],
            }
        )

    readme_data = str(spec["readme"]).encode("utf-8")
    manifest_rows = [
        *source_rows,
        {
            "filename": "README.md",
            "bytes": len(readme_data),
            "sha256": sha256_bytes(readme_data),
            "role": "archive_scope_and_disposition",
        },
    ]
    manifest_data = csv_bytes(manifest_rows)

    archive_path = PACKAGE_ROOT / archive_name
    with zipfile.ZipFile(
        archive_path,
        "w",
        compression=zipfile.ZIP_DEFLATED,
        compresslevel=9,
    ) as archive:
        for name, data in source_data:
            archive.writestr(zip_info(name), data)
        archive.writestr(zip_info("README.md"), readme_data)
        archive.writestr(zip_info("GROUP_MANIFEST.csv"), manifest_data)

    errors: list[str] = []
    with zipfile.ZipFile(archive_path) as archive:
        if archive.testzip() is not None:
            errors.append("crc_failure")
        names = archive.namelist()
        expected_names = [row["filename"] for row in manifest_rows]
        expected_names.append("GROUP_MANIFEST.csv")
        if names != expected_names:
            errors.append("entry_order_or_set_mismatch")
        replay_rows = list(
            csv.DictReader(
                io.StringIO(
                    archive.read("GROUP_MANIFEST.csv").decode("utf-8"),
                    newline="",
                )
            )
        )
        for row in replay_rows:
            data = archive.read(row["filename"])
            if (len(data), sha256_bytes(data)) != (
                int(row["bytes"]),
                row["sha256"].upper(),
            ):
                errors.append(f"member_mismatch:{row['filename']}")

    if errors:
        raise RuntimeError(f"{archive_name}: {errors}")
    return {
        "filename": archive_name,
        "bytes": archive_path.stat().st_size,
        "sha256": sha256_file(archive_path),
        "members": len(manifest_rows) + 1,
        "manifest_rows": len(manifest_rows),
        "manifest_sha256": sha256_bytes(manifest_data),
        "uncompressed_bytes": sum(
            int(row["bytes"]) for row in manifest_rows
        )
        + len(manifest_data),
        "errors": [],
    }


def write_outer_controls(groups: list[dict[str, object]]) -> None:
    readme = (
        "# Compact SGA3 historical checkpoint grouping\n\n"
        "The clean cumulative SGA3 PDF and editable master remain direct public "
        "files. This package groups loose bounded checkpoint readers, their "
        "masters and source archives, and two older predecessor-history archives "
        "into two exact ZIPs. Historical bytes are preserved; they no longer "
        "interrupt the reader-first Zenodo file list.\n\n"
        "Three historical bounded PDFs carried a `Loop-1` title on page 1. They "
        "remain exact inside the history archive, but the direct reading surface "
        "is the reader-clean cumulative PDF with no AI, production, source-status, "
        "or workflow commentary.\n"
    )
    (PACKAGE_ROOT / "README.md").write_text(readme, encoding="utf-8")

    validation = {
        "schema": "sga3_compact_bounded_history_v1",
        "status": "PASS",
        "errors": [],
        "source_record": SOURCE_RECORD,
        "removed_loose_files": len(THROUGH_XI) + len(BOUNDED_FILES),
        "removed_loose_bytes": sum(
            int(public_files[name]["bytes"])
            for name in THROUGH_XI + BOUNDED_FILES
        ),
        "group_archives": groups,
        "expected_compact_record_files": 68,
        "direct_sga3_reader_after_compaction": (
            "00c00_SGA3_English_Complete_Reader_"
            "Native_Update_R17_20260729.pdf"
        ),
        "historical_reader_process_hits": [
            {
                "filename": (
                    "00c19_SGA3_Expose_XIX_English_"
                    "NativeDiagram_Loop1_Working_20260728.pdf"
                ),
                "page": 1,
                "term": "Loop-1",
            },
            {
                "filename": (
                    "00c23_SGA3_Expose_XXIII_English_"
                    "NativeDiagram_Loop1_Working_20260728.pdf"
                ),
                "page": 1,
                "term": "Loop-1",
            },
            {
                "filename": (
                    "00c25_SGA3_Expose_XXV_English_"
                    "NativeDiagram_Loop1_Working_20260728.pdf"
                ),
                "page": 1,
                "term": "Loop-1",
            },
        ],
    }
    (PACKAGE_ROOT / "PACKAGE_VALIDATION.json").write_text(
        json.dumps(validation, ensure_ascii=True, indent=2) + "\n",
        encoding="utf-8",
    )

    rows = []
    for path in sorted(PACKAGE_ROOT.iterdir(), key=lambda item: item.name.casefold()):
        if not path.is_file() or path.name == "SHA256SUMS.csv":
            continue
        rows.append(
            {
                "filename": path.name,
                "bytes": path.stat().st_size,
                "sha256": sha256_file(path),
                "role": (
                    "grouped_history_archive"
                    if path.suffix.lower() == ".zip"
                    else "package_control"
                ),
            }
        )
    (PACKAGE_ROOT / "SHA256SUMS.csv").write_bytes(csv_bytes(rows))


if __name__ == "__main__":
    receipt = json.loads(RECEIPT.read_text(encoding="utf-8"))
    public_files = receipt["files"]
    expected_names = set(THROUGH_XI + BOUNDED_FILES)
    if len(expected_names) != 26 or not expected_names <= set(public_files):
        raise RuntimeError("Historical source boundary mismatch")
    session = requests.Session()
    session.headers.update({"User-Agent": "modern-latex-manuscripts/1.0"})
    built = [
        build_group(session, public_files, archive_name, spec)
        for archive_name, spec in GROUPS.items()
    ]
    write_outer_controls(built)
    print(json.dumps({"status": "PASS", "groups": built}, indent=2))
