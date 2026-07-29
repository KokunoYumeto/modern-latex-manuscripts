#!/usr/bin/env python3
"""Build compact same-concept release controls for the SGA3 R21 reader."""

from __future__ import annotations

import csv
import hashlib
import io
import json
import shutil
import zipfile
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
R21_ROOT = (
    REPO_ROOT
    / "sources"
    / "sga"
    / "sga3-english-reader-clean-r21-no-project-notes-20260729"
)
OUTPUT_ROOT = (
    REPO_ROOT
    / "sources"
    / "sga"
    / "sga-reader-clean-r21-release-controls-20260729"
)
PREDECESSOR_RECEIPT = (
    REPO_ROOT
    / "manifests"
    / "published-zenodo"
    / "20260728_sga3_cumulative_with_x_record_21686789_public_readback.json"
)
PREDECESSOR_CONTROLS = (
    REPO_ROOT
    / "sources"
    / "sga"
    / "sga-canonical-release-controls-compact-20260729"
    / "10z_SGA_Current_Release_Controls_20260729.zip"
)

CONTROLS_ZIP = "10z_SGA_Current_Release_Controls_20260729.zip"
README_NAME = "09_README_CURRENT_RELEASE.md"
MANIFEST_NAME = "09a_RELEASE_FILE_MANIFEST.csv"
VALIDATION_NAME = "09b_RELEASE_VALIDATION.json"
PACKED_MANIFEST = "PACKED_CONTROL_SHA256.csv"
OUTER_MANIFEST = "SHA256SUMS.csv"
FIXED_ZIP_TIME = (2026, 7, 29, 0, 0, 0)
OLD_SGA3_ZIP = "10c_SGA3_English_Source_and_History_R20_20260729.zip"
NEW_SGA3_ZIP = "10c_SGA3_English_Source_and_History_R21_20260729.zip"
R21_FILES = {
    "00c_SGA3_English_Reader.pdf",
    "02c_SGA3_English_Master.tex",
    NEW_SGA3_ZIP,
}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def csv_bytes(rows: list[dict[str, object]], fields: list[str]) -> bytes:
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue().encode("utf-8")


def zip_info(name: str) -> zipfile.ZipInfo:
    info = zipfile.ZipInfo(name, date_time=FIXED_ZIP_TIME)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.create_system = 3
    info.external_attr = 0o100644 << 16
    return info


def load_r21_identities() -> dict[str, dict[str, object]]:
    rows = list(
        csv.DictReader(
            io.StringIO(
                (R21_ROOT / OUTER_MANIFEST).read_text(encoding="utf-8"),
                newline="",
            )
        )
    )
    identities = {
        row["filename"]: {
            "bytes": int(row["bytes"]),
            "sha256": row["sha256"].upper(),
        }
        for row in rows
    }
    if not R21_FILES.issubset(identities):
        raise RuntimeError("R21 manifest omits a release object")
    for name in R21_FILES:
        path = R21_ROOT / name
        expected = identities[name]
        if (
            path.stat().st_size,
            sha256_file(path),
        ) != (expected["bytes"], expected["sha256"]):
            raise RuntimeError(f"R21 identity mismatch: {name}")
    return identities


def build() -> None:
    required = (
        R21_ROOT / OUTER_MANIFEST,
        PREDECESSOR_RECEIPT,
        PREDECESSOR_CONTROLS,
    )
    for path in required:
        if not path.is_file():
            raise FileNotFoundError(path)
    if OUTPUT_ROOT.exists():
        if OUTPUT_ROOT.resolve().parent != OUTPUT_ROOT.parent.resolve():
            raise RuntimeError(f"Unsafe output path: {OUTPUT_ROOT}")
        shutil.rmtree(OUTPUT_ROOT)
    OUTPUT_ROOT.mkdir(parents=True)

    r21 = load_r21_identities()
    receipt = json.loads(PREDECESSOR_RECEIPT.read_text(encoding="utf-8-sig"))
    if (
        receipt.get("status") != "PASS"
        or receipt.get("errors")
        or int(receipt.get("record", -1)) != 21686789
        or receipt.get("conceptdoi") != "10.5281/zenodo.20410947"
        or int(receipt.get("file_count", -1)) != 66
    ):
        raise RuntimeError("Predecessor public-readback receipt is not controlling")
    current = {
        name: {
            "bytes": int(value["bytes"]),
            "sha256": value["sha256"].upper(),
        }
        for name, value in receipt["files"].items()
    }

    with zipfile.ZipFile(PREDECESSOR_CONTROLS) as archive:
        if archive.testzip() is not None:
            raise RuntimeError("Predecessor controls ZIP CRC failure")
        old_rows = list(
            csv.DictReader(
                io.StringIO(
                    archive.read(MANIFEST_NAME).decode("utf-8"),
                    newline="",
                )
            )
        )
    old_by_name = {row["filename"]: row for row in old_rows}

    prospective = dict(current)
    prospective["00c_SGA3_English_Reader.pdf"] = r21[
        "00c_SGA3_English_Reader.pdf"
    ]
    prospective["02c_SGA3_English_Master.tex"] = r21[
        "02c_SGA3_English_Master.tex"
    ]
    prospective.pop(OLD_SGA3_ZIP)
    prospective[NEW_SGA3_ZIP] = r21[NEW_SGA3_ZIP]
    prospective.pop(CONTROLS_ZIP)
    if len(prospective) != 65:
        raise RuntimeError(
            f"Expected 65 non-control objects, got {len(prospective)}"
        )

    manifest_rows = []
    for name, identity in sorted(
        prospective.items(), key=lambda item: item[0].casefold()
    ):
        if name == NEW_SGA3_ZIP:
            role = "source_and_history_archive"
            provenance = (
                "grouped SGA3 source closure, R20 history, and R21 "
                "reader-apparatus cleanup"
            )
            status = "archive"
        else:
            old = old_by_name.get(name)
            if old is None:
                raise RuntimeError(f"No retained release role for {name}")
            role = old["role"]
            provenance = old["provenance"]
            status = old["status"]
        manifest_rows.append(
            {
                "filename": name,
                "bytes": identity["bytes"],
                "sha256": identity["sha256"],
                "role": role,
                "provenance": provenance,
                "status": status,
            }
        )

    readme = """# SGA 1-6

## English readers

- `00a_SGA1_English_Reader.pdf`
- `00b_SGA2_English_Reader.pdf`
- `00c_SGA3_English_Reader.pdf`
- `00d_SGA4_English_Reader.pdf`
- `00e_SGA5_English_Reader.pdf`
- `00f_SGA6_English_Reader.pdf`

The SGA3 reader has 1,459 A4 pages and includes the Editorial Notice,
Introduction, Exposes I-XXVI, the Tome-I index, the Tome-III mathematical
guide, and the terminal index. Its direct reading flow contains mathematical
and legitimate historical editorial content; project production and
source-adjudication apparatus is kept in the grouped source/history archive.

## French texts

Direct French reader and TeX files are present for SGA5 and SGA6.

## Editable sources and archives

The `02*` files are the direct English master TeX files. The `03*` files are
the available direct French master TeX files. Supporting source, provenance,
quality-control, and historical material is grouped in the `10*`, `11*`, and
`12*` ZIP archives.

Rights in the underlying works remain with their respective holders.
Historical versions remain available through Zenodo. The corresponding source
package is mirrored in the project's GitHub repository.
"""
    validation = {
        "schema": "sga_reader_clean_r21_release_controls_v1",
        "status": "PASS",
        "errors": [],
        "concept_doi": "10.5281/zenodo.20410947",
        "source_record": 21686789,
        "prospective_files": 66,
        "manifest_scope": (
            "65 outer files other than the containing controls ZIP"
        ),
        "retained_files": 63,
        "replaced_same_name_files": [
            "00c_SGA3_English_Reader.pdf",
            CONTROLS_ZIP,
        ],
        "removed_file": OLD_SGA3_ZIP,
        "added_file": NEW_SGA3_ZIP,
        "default_preview": "00a_SGA1_English_Reader.pdf",
        "sga3_reader": {
            "pages": 1459,
            **r21["00c_SGA3_English_Reader.pdf"],
            "named_destinations": 9345,
            "internal_goto_actions": 4461,
            "invalid_or_external_actions": 0,
            "reader_process_term_hits": 0,
        },
        "other_direct_readers": {
            "reader_process_term_hits": 0,
            "bytes_changed": False,
        },
        "duplicate_concept_created": False,
        "second_draft_created": False,
        "new_license_grant": False,
    }

    inner = {
        README_NAME: readme.encode("utf-8"),
        MANIFEST_NAME: csv_bytes(
            manifest_rows,
            [
                "filename",
                "bytes",
                "sha256",
                "role",
                "provenance",
                "status",
            ],
        ),
        VALIDATION_NAME: (
            json.dumps(validation, indent=2) + "\n"
        ).encode("utf-8"),
    }
    packed_rows = [
        {
            "filename": name,
            "bytes": len(data),
            "sha256": sha256_bytes(data),
        }
        for name, data in sorted(
            inner.items(), key=lambda item: item[0].casefold()
        )
    ]
    inner[PACKED_MANIFEST] = csv_bytes(
        packed_rows, ["filename", "bytes", "sha256"]
    )

    output_zip = OUTPUT_ROOT / CONTROLS_ZIP
    with zipfile.ZipFile(output_zip, "w") as archive:
        for name, data in sorted(
            inner.items(), key=lambda item: item[0].casefold()
        ):
            archive.writestr(zip_info(name), data)
    with zipfile.ZipFile(output_zip) as archive:
        if archive.testzip() is not None:
            raise RuntimeError("R21 controls ZIP CRC failure")
        replay_rows = list(
            csv.DictReader(
                io.StringIO(
                    archive.read(PACKED_MANIFEST).decode("utf-8"),
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
                raise RuntimeError(
                    f"Packed-control mismatch: {row['filename']}"
                )

    outer_validation = {
        "schema": "sga_reader_clean_r21_controls_package_v1",
        "status": "PASS",
        "errors": [],
        "source_record": 21686789,
        "concept_doi": "10.5281/zenodo.20410947",
        "controls_zip": {
            "filename": CONTROLS_ZIP,
            "bytes": output_zip.stat().st_size,
            "sha256": sha256_file(output_zip),
            "members": len(inner),
            "manifest_rows": len(packed_rows),
        },
        "prospective_zenodo_files": 66,
        "manifest_rows": len(manifest_rows),
    }
    (OUTPUT_ROOT / "README.md").write_text(
        """# SGA R21 compact release controls

This package updates the compact SGA1-6 release controls for the reader-clean
SGA3 R21 successor. Only the controls ZIP is intended for the Zenodo surface;
the loose files here are GitHub custody and validation aids.
""",
        encoding="utf-8",
        newline="\n",
    )
    (OUTPUT_ROOT / "PACKAGE_VALIDATION.json").write_text(
        json.dumps(outer_validation, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    files = sorted(
        path
        for path in OUTPUT_ROOT.iterdir()
        if path.is_file() and path.name != OUTER_MANIFEST
    )
    (OUTPUT_ROOT / OUTER_MANIFEST).write_bytes(
        csv_bytes(
            [
                {
                    "filename": path.name,
                    "bytes": path.stat().st_size,
                    "sha256": sha256_file(path),
                }
                for path in files
            ],
            ["filename", "bytes", "sha256"],
        )
    )
    print(json.dumps(outer_validation, indent=2))


if __name__ == "__main__":
    build()
