#!/usr/bin/env python3
"""Build compact release controls for the clean SGA2 R9 reader."""

from __future__ import annotations

import csv
import hashlib
import io
import json
import shutil
import zipfile
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
R9_ROOT = (
    REPO_ROOT
    / "sources"
    / "sga"
    / "sga2-english-reader-clean-r9-no-correction-status-notes-20260729"
)
OUTPUT_ROOT = (
    REPO_ROOT
    / "sources"
    / "sga"
    / "sga-reader-clean-r23-sga2-r9-release-controls-20260729"
)
PREDECESSOR_RECEIPT = (
    REPO_ROOT
    / "manifests"
    / "published-zenodo"
    / "20260728_sga3_cumulative_with_x_record_21690335_public_readback.json"
)
PREDECESSOR_CONTROLS = (
    REPO_ROOT
    / "sources"
    / "sga"
    / "sga-reader-clean-r22-release-controls-20260729"
    / "10z_SGA_Current_Release_Controls_20260729.zip"
)

CONTROLS_ZIP = "10z_SGA_Current_Release_Controls_20260729.zip"
README_NAME = "09_README_CURRENT_RELEASE.md"
MANIFEST_NAME = "09a_RELEASE_FILE_MANIFEST.csv"
VALIDATION_NAME = "09b_RELEASE_VALIDATION.json"
PACKED_MANIFEST = "PACKED_CONTROL_SHA256.csv"
OUTER_MANIFEST = "SHA256SUMS.csv"
FIXED_ZIP_TIME = (2026, 7, 29, 0, 0, 0)
SGA2_PDF = "00b_SGA2_English_Reader.pdf"
SGA2_TEX = "02b_SGA2_English_Master.tex"
OLD_SGA2_ZIP = (
    "10b_SGA2_English_Complete_ReferenceLinked_R8_TeX_Ledgers_20260723.zip"
)
NEW_SGA2_ZIP = "10b_SGA2_English_Source_and_History_R9_20260729.zip"
R9_FILES = {SGA2_PDF, SGA2_TEX, NEW_SGA2_ZIP}


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


def load_r9_identities() -> tuple[dict[str, dict[str, object]], dict]:
    rows = list(
        csv.DictReader(
            io.StringIO(
                (R9_ROOT / OUTER_MANIFEST).read_text(encoding="utf-8"),
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
    if not R9_FILES.issubset(identities):
        raise RuntimeError("R9 manifest omits a release object")
    for name in R9_FILES:
        path = R9_ROOT / name
        expected = identities[name]
        if (path.stat().st_size, sha256_file(path)) != (
            expected["bytes"],
            expected["sha256"],
        ):
            raise RuntimeError(f"R9 identity mismatch: {name}")
    validation = json.loads(
        (R9_ROOT / "PACKAGE_VALIDATION.json").read_text(encoding="utf-8")
    )
    if validation.get("status") != "PASS" or validation.get("errors"):
        raise RuntimeError("R9 package validation is not PASS")
    return identities, validation


def build() -> None:
    for path in (
        R9_ROOT / OUTER_MANIFEST,
        R9_ROOT / "PACKAGE_VALIDATION.json",
        PREDECESSOR_RECEIPT,
        PREDECESSOR_CONTROLS,
    ):
        if not path.is_file():
            raise FileNotFoundError(path)
    if OUTPUT_ROOT.exists():
        resolved = OUTPUT_ROOT.resolve()
        if resolved.parent != OUTPUT_ROOT.parent.resolve():
            raise RuntimeError(f"Unsafe output path: {resolved}")
        shutil.rmtree(resolved)
    OUTPUT_ROOT.mkdir(parents=True)

    r9, r9_validation = load_r9_identities()
    receipt = json.loads(PREDECESSOR_RECEIPT.read_text(encoding="utf-8-sig"))
    if (
        receipt.get("status") != "PASS"
        or receipt.get("errors")
        or int(receipt.get("record", -1)) != 21690335
        or receipt.get("conceptdoi") != "10.5281/zenodo.20410947"
        or int(receipt.get("file_count", -1)) != 66
    ):
        raise RuntimeError("R22 public-readback receipt is not controlling")
    current = {
        name: {
            "bytes": int(value["bytes"]),
            "sha256": value["sha256"].upper(),
        }
        for name, value in receipt["files"].items()
    }

    with zipfile.ZipFile(PREDECESSOR_CONTROLS) as archive:
        if archive.testzip() is not None:
            raise RuntimeError("R22 controls ZIP CRC failure")
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
    prospective[SGA2_PDF] = r9[SGA2_PDF]
    if prospective[SGA2_TEX] != r9[SGA2_TEX]:
        raise RuntimeError("Direct SGA2 master TeX unexpectedly changed")
    prospective.pop(OLD_SGA2_ZIP)
    prospective[NEW_SGA2_ZIP] = r9[NEW_SGA2_ZIP]
    prospective.pop(CONTROLS_ZIP)
    if len(prospective) != 65:
        raise RuntimeError(
            f"Expected 65 non-control objects, got {len(prospective)}"
        )

    manifest_rows = []
    for name, identity in sorted(
        prospective.items(), key=lambda item: item[0].casefold()
    ):
        if name == NEW_SGA2_ZIP:
            role = "source_and_history_archive"
            provenance = (
                "grouped SGA2 buildable source, apparatus-removal ledger, "
                "replay evidence, and immutable correction history"
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

The SGA2 R9 direct reader preserves the mathematical body, references, and
historical edition apparatus while moving project correction history,
source-status commentary, and production notes into its grouped archive.
The SGA3 R22 reader includes completed native-diagram successors for
Exposes VIII, IX, XI, and XV.

Direct reading PDFs contain mathematics and genuine historical edition
apparatus. Project workflow, model, source-reading, and correction-history
records are kept outside reader pages.

## French texts

Direct French reader and TeX files are present for SGA5 and SGA6.

## Editable sources and archives

The `02*` files are direct English master TeX files. The `03*` files are the
available direct French master TeX files. Supporting source, provenance,
quality-control, and historical material is grouped in the `10*`, `11*`,
and `12*` ZIP archives.

Rights in the underlying works remain with their respective holders.
Historical versions remain available through Zenodo. The corresponding
source packages are mirrored in the project's GitHub repository.
"""
    validation = {
        "schema": "sga_reader_clean_r23_sga2_r9_release_controls_v1",
        "status": "PASS",
        "errors": [],
        "concept_doi": "10.5281/zenodo.20410947",
        "source_record": 21690335,
        "prospective_files": 66,
        "manifest_scope": (
            "65 outer files other than the containing controls ZIP"
        ),
        "retained_files": 63,
        "replaced_same_name_files": [SGA2_PDF, CONTROLS_ZIP],
        "removed_file": OLD_SGA2_ZIP,
        "added_file": NEW_SGA2_ZIP,
        "default_preview": "00a_SGA1_English_Reader.pdf",
        "sga2_reader": {
            "pages": 178,
            **r9[SGA2_PDF],
            "named_destinations": 1514,
            "internal_goto_actions": 1307,
            "invalid_or_external_actions": 0,
            "reader_process_term_hits": 0,
            "project_correction_phrase_hits": 0,
            "historical_serre_editorial_note_count": 1,
            "reader_apparatus_removals": 61,
            "correction_status_rows": 9,
            "isolated_replay": r9_validation["isolated_replay"],
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
            raise RuntimeError("R23 controls ZIP CRC failure")
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
        "schema": "sga_reader_clean_r23_sga2_r9_controls_package_v1",
        "status": "PASS",
        "errors": [],
        "source_record": 21690335,
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
        """# SGA R23 compact release controls

This package updates the compact SGA1-6 release controls for the clean SGA2
R9 reader. Only the controls ZIP is intended for the Zenodo surface; loose
files are GitHub custody and validation aids.
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
