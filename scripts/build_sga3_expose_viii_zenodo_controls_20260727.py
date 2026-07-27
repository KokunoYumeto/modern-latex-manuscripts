#!/usr/bin/env python3
"""Build same-concept Zenodo controls for the SGA3 Expose VIII checkpoint."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import shutil
import zipfile
from pathlib import Path


CONCEPT_DOI = "10.5281/zenodo.20410947"
PREDECESSOR_RECORD = 21523096
PREDECESSOR_DOI = "10.5281/zenodo.21523096"
GITHUB_COMMIT = "c53b27a9da508cde755a3bbb176ab04dd8fb744a"
GITHUB_PACKAGE = (
    "sources/sga/"
    "sga3-english-expose-viii-loop2-reference-v2-r1-20260724"
)

SOURCE_TO_RELEASE = {
    "SGA3_English_Expose_VIII_Loop2_ReferenceV2_R1_20260724.pdf":
        "00c5_SGA3_English_Expose_VIII_Loop2_ReferenceV2_R1_20260724.pdf",
    "SGA3_English_Expose_VIII_Loop2_ReferenceV2_R1_Source_QA_20260724.zip":
        "10c5_SGA3_English_Expose_VIII_Loop2_ReferenceV2_R1_Source_QA_20260724.zip",
}

CONTROL_NAMES = {
    "09_README_CURRENT_RELEASE.md",
    "09a_RELEASE_FILE_MANIFEST.csv",
    "09b_RELEASE_VALIDATION.json",
}

DEFAULT_PREVIEW = (
    "00a_SGA1_English_CompleteVolume_Working_"
    "NoExhaustiveCertification_20260722.pdf"
)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def identity(path: Path) -> dict[str, int | str]:
    data = path.read_bytes()
    return {"bytes": len(data), "sha256": sha256_bytes(data)}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    fields = ["filename", "bytes", "sha256", "role", "provenance", "status"]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def formula_safe(rows: list[dict[str, object]]) -> bool:
    return all(
        not str(value).startswith(("=", "+", "-", "@"))
        for row in rows
        for value in row.values()
    )


def build_readme() -> str:
    return f"""# Current compact SGA release

This same-concept successor preserves the existing reader-first SGA surface
and adds the independently audited complete bounded SGA 3 Expose VIII
checkpoint as one direct reader and one grouped source/QA archive. All 53
predecessor files outside the three release controls remain byte-identical.

## Reader-first order

1. English SGA 1 complete-volume working reader. Its clickable-reference
   infrastructure is substantial but not exhaustively convention-v2
   certified.
2. English SGA 2 complete archive-curated reference-linked R8 reader.
3. English SGA 3 cumulative working reader through complete Expose IV,
   followed by standalone native-diagram readers for complete Exposes V and
   VI, and the complete bounded Expose VIII checkpoint. Expose VII and
   Exposes IX-XXVI are absent from the current public reader surface.
4. English SGA 4 proper certified reference-v2 r7 reader, covering Exposes
   I-XIX including V bis and excluding SGA 4half.
5. English SGA 5 reference-linked R9 reader.
6. English SGA 6 complete layered terminal reference-linked reader.

Available French workpasses and primary editable TeX follow the English
readers. Recursive source, machine-readable ledgers, QA, bounded checkpoints,
predecessor material, and high-detail visual evidence remain grouped into
coherent ZIP archives. The SGA 1 working reader remains the initial preview.

## SGA 3 Expose VIII

The new 31-page A4 reader covers Sections 1-7, 58 numbered units, 22 equation
tags, notes 0-42 plus five symbolic notes, four native diagrams, and the
terminal bibliography. It stops before the first nonblank page of Expose IX.
Its PDF has 270 named destinations, 248 valid internal GoTo actions, 28
embedded fonts, and no raster-image inclusions.

The grouped ZIP contains 65 exact members totaling 8,833,128 uncompressed
bytes: 10 editable TeX files, the reader, all 31 reviewed page renders,
reference-v2 graph data, translation/correction QA, independent audit
receipts, provenance and rights notices, and recursive checksums. The graph
records 155 targets and 525 candidates partitioned into 188 edges and 337
positive residuals, with zero pending actions. All 31 pages passed direct
visual review.

The ten `SGA3-VIII-SOURCE-*` identifiers that occur in both source-closure
tables are intentional relational join keys; stable-ID uniqueness is checked
within each table.

This is complete Expose VIII, not complete SGA 3. It is a bounded
source-audited working translation and reference-linked reader, not a critical
edition, mathematical certification, independent human peer review, rights
determination, or tagged/accessibility-remediated PDF.

## Authority, attribution, and rights

The Polo-Gille Expose VIII PDF `Exp8-8nov09.pdf`, SHA-256
`06E43E0571D411CC5579975778FCC03C8ECAA67189248D1A053E61DC653AF510`,
is the controlling prose, formula, page, and diagram witness. It is not
redistributed. OCR and external English material are locator or comparison
controls, not authority.

No new blanket license or rights clearance is asserted. Rights in the
underlying French work and Polo-Gille re-edition remain with their holders.
Machine-assisted contributors include OpenAI Codex / ChatGPT and Anthropic
Claude under human direction.

Existing concept DOI: {CONCEPT_DOI}.
Predecessor version preserved: {PREDECESSOR_DOI}.
GitHub package commit: {GITHUB_COMMIT}.
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--predecessor-manifest", type=Path, required=True)
    parser.add_argument("--predecessor-readback", type=Path, required=True)
    parser.add_argument("--package-root", type=Path, required=True)
    parser.add_argument("--output-root", type=Path, required=True)
    parser.add_argument("--successor-record", type=int, required=True)
    args = parser.parse_args()

    predecessor_rows = read_csv(args.predecessor_manifest)
    predecessor_readback = json.loads(
        args.predecessor_readback.read_text(encoding="utf-8-sig")
    )
    package_validation = json.loads(
        (args.package_root / "PACKAGE_VALIDATION.json").read_text(
            encoding="utf-8-sig"
        )
    )
    package_rows = read_csv(args.package_root / "SHA256SUMS.csv")

    errors: list[str] = []
    if len(predecessor_rows) != 54:
        errors.append(f"predecessor_manifest_rows:{len(predecessor_rows)}")
    if predecessor_readback.get("status") != "PASS":
        errors.append("predecessor_readback_not_pass")
    if predecessor_readback.get("record", {}).get("id") != PREDECESSOR_RECORD:
        errors.append("predecessor_readback_record")
    if len(predecessor_readback.get("outer_files", [])) != 56:
        errors.append("predecessor_readback_files")
    if package_validation.get("status") != "PASS":
        errors.append("package_validation_not_pass")
    if len(package_rows) != 2:
        errors.append(f"package_manifest_rows:{len(package_rows)}")

    readback_by_name = {
        row["filename"]: row
        for row in predecessor_readback.get("outer_files", [])
    }
    for row in predecessor_rows:
        remote = readback_by_name.get(row["filename"])
        if remote is None:
            errors.append(f"predecessor_readback_missing:{row['filename']}")
            continue
        if (
            int(row["bytes"]) != int(remote["bytes"])
            or row["sha256"] != remote["sha256"]
        ):
            errors.append(f"predecessor_identity:{row['filename']}")

    package_by_name = {row["filename"]: row for row in package_rows}
    for source_name in SOURCE_TO_RELEASE:
        source = args.package_root / source_name
        row = package_by_name.get(source_name)
        if row is None:
            errors.append(f"package_manifest_missing:{source_name}")
            continue
        actual = identity(source)
        if (
            int(row["bytes"]) != actual["bytes"]
            or row["sha256"] != actual["sha256"]
        ):
            errors.append(f"package_identity:{source_name}")

    if errors:
        raise SystemExit(json.dumps({"status": "FAIL", "errors": errors}, indent=2))

    args.output_root.mkdir(parents=True, exist_ok=True)
    for child in args.output_root.iterdir():
        if child.is_file():
            child.unlink()
        elif child.is_dir():
            shutil.rmtree(child)

    for source_name, release_name in SOURCE_TO_RELEASE.items():
        shutil.copyfile(args.package_root / source_name, args.output_root / release_name)

    readme_path = args.output_root / "09_README_CURRENT_RELEASE.md"
    readme_path.write_text(build_readme(), encoding="utf-8", newline="\n")

    retained = [
        row for row in predecessor_rows
        if row["filename"] != "09_README_CURRENT_RELEASE.md"
    ]
    if len(retained) != 53:
        raise SystemExit(f"Expected 53 retained rows, found {len(retained)}")

    def new_row(
        filename: str, role: str, provenance: str, status: str
    ) -> dict[str, object]:
        current = identity(args.output_root / filename)
        return {
            "filename": filename,
            "bytes": current["bytes"],
            "sha256": current["sha256"],
            "role": role,
            "provenance": provenance,
            "status": status,
        }

    new_rows = [
        new_row(
            "00c5_SGA3_English_Expose_VIII_Loop2_ReferenceV2_R1_20260724.pdf",
            "english_reader",
            (
                "complete bounded SGA3 Expose VIII source-audited "
                f"Loop2/reference-v2 reader; GitHub commit {GITHUB_COMMIT}"
            ),
            "bounded_working_reader_sga3_incomplete_expose_viii_complete",
        ),
        new_row(
            "09_README_CURRENT_RELEASE.md",
            "manifest_status",
            "current compact release note adding bounded complete Expose VIII",
            "current_release_control",
        ),
        new_row(
            "10c5_SGA3_English_Expose_VIII_Loop2_ReferenceV2_R1_Source_QA_20260724.zip",
            "grouped_source_and_evidence",
            (
                "65-member privacy-clean editable source, reference graph, "
                "all-page render QA, audit, rights, and identity archive"
            ),
            "bounded_working_package_sga3_incomplete_expose_viii_complete",
        ),
    ]
    final_rows = sorted(retained + new_rows, key=lambda row: row["filename"])
    if len(final_rows) != 56:
        raise SystemExit(f"Expected 56 content rows, found {len(final_rows)}")
    if not formula_safe(final_rows):
        raise SystemExit("Formula-unsafe manifest value")

    manifest_path = args.output_root / "09a_RELEASE_FILE_MANIFEST.csv"
    write_csv(manifest_path, final_rows)
    manifest_id = identity(manifest_path)

    zip_name = (
        "10c5_SGA3_English_Expose_VIII_Loop2_ReferenceV2_R1_"
        "Source_QA_20260724.zip"
    )
    zip_path = args.output_root / zip_name
    member_rows: list[tuple[str, int, str]] = []
    internal_manifest: list[dict[str, str]] = []
    with zipfile.ZipFile(zip_path) as archive:
        infos = [info for info in archive.infolist() if not info.is_dir()]
        unsafe = [
            info.filename for info in infos
            if info.filename.startswith(("/", "\\"))
            or (len(info.filename) >= 2 and info.filename[1] == ":")
            or ".." in Path(info.filename.replace("\\", "/")).parts
        ]
        manifest_info = next(
            info for info in infos if info.filename.endswith("/SHA256SUMS.csv")
        )
        internal_manifest = list(
            csv.DictReader(
                archive.read(manifest_info).decode("utf-8-sig").splitlines()
            )
        )
        for info in sorted(infos, key=lambda item: item.filename):
            member_rows.append(
                (
                    info.filename,
                    info.file_size,
                    sha256_bytes(archive.read(info)),
                )
            )
    zip_uncompressed = sum(row[1] for row in member_rows)
    if (
        len(member_rows) != 65
        or zip_uncompressed != 8_833_128
        or len(internal_manifest) != 64
        or unsafe
    ):
        raise SystemExit(
            json.dumps(
                {
                    "zip_members": len(member_rows),
                    "zip_uncompressed_bytes": zip_uncompressed,
                    "internal_manifest_rows": len(internal_manifest),
                    "unsafe_entries": unsafe,
                },
                indent=2,
            )
        )

    validation = {
        "status": "PASS",
        "errors": [],
        "concept_doi": CONCEPT_DOI,
        "predecessor_record": PREDECESSOR_RECORD,
        "predecessor_doi": PREDECESSOR_DOI,
        "reserved_successor_record": args.successor_record,
        "same_concept_only": True,
        "duplicate_concept_authorized": False,
        "retained_predecessor_files": 53,
        "replaced_files": sorted(CONTROL_NAMES),
        "new_sga3_expose_viii_files": sorted(SOURCE_TO_RELEASE.values()),
        "content_manifest_rows": 56,
        "release_manifest_file": manifest_path.name,
        "release_manifest_bytes": manifest_id["bytes"],
        "release_manifest_sha256": manifest_id["sha256"],
        "final_upload_file_count": 58,
        "final_upload_bytes": 0,
        "default_preview": DEFAULT_PREVIEW,
        "github": {
            "commit": GITHUB_COMMIT,
            "package": GITHUB_PACKAGE,
            "outer_files": 5,
            "zip_members": 65,
            "readback_files": 5,
            "readback_zip_members": 65,
            "readback_errors": [],
        },
        "sga3_expose_viii": {
            "scope": "complete bounded SGA3 Expose VIII",
            "sga3_complete": False,
            "excluded_scope": "Expose VII and Exposes IX-XXVI",
            "reader_pages": 31,
            "reader_sha256": (
                "255A62C74E5A9900AC92DFCD5379A730C12B86DF7727336AF2E04282BF14D230"
            ),
            "editable_tex_files": 10,
            "native_diagrams": 4,
            "active_raster_image_inclusions": 0,
            "reference_targets": 155,
            "reference_edges": 188,
            "reference_candidates": 525,
            "positive_residuals": 337,
            "pdf_named_destinations": 270,
            "pdf_goto_actions": 248,
            "visual_qa_pages": 31,
            "source_archive_members": 65,
            "source_archive_uncompressed_bytes": zip_uncompressed,
            "member_manifest_rows": 64,
            "member_manifest_sha256": (
                "AE814BD842CC0EA3BE771DA7C22BA4CD32D93FCEA3F00296013ABEE211A1A0AA"
            ),
            "independent_receipt_sha256": (
                "C9D12B9DB631A7FF2FD7D14B92FDA84BBDF8C291616872B9D6E135E25ED9E0BE"
            ),
        },
        "zip_archive_count": 32,
        "zip_member_count": 3393,
        "zip_uncompressed_bytes": 357_369_191,
        "rights": {
            "new_license_grant": False,
            "rights_clearance_claimed": False,
            "authority_pdf_redistributed": False,
            "underlying_french_rights_retained": True,
            "polo_gille_rights_retained": True,
        },
        "contributors": [
            "OpenAI Codex / ChatGPT",
            "Anthropic Claude",
        ],
        "privacy_hits": [],
    }

    validation_path = args.output_root / "09b_RELEASE_VALIDATION.json"
    content_bytes = sum(int(row["bytes"]) for row in final_rows) + int(
        manifest_id["bytes"]
    )
    encoded = b""
    for _ in range(10):
        encoded = (json.dumps(validation, indent=2) + "\n").encode("utf-8")
        total = content_bytes + len(encoded)
        if validation["final_upload_bytes"] == total:
            break
        validation["final_upload_bytes"] = total
    validation_path.write_bytes(encoded)

    staged = sorted(path for path in args.output_root.iterdir() if path.is_file())
    if len(staged) != 5:
        raise SystemExit(f"Expected 5 staging files, found {len(staged)}")
    final_bytes = content_bytes + validation_path.stat().st_size
    if final_bytes != validation["final_upload_bytes"]:
        raise SystemExit("Final upload byte count mismatch")

    print(
        json.dumps(
            {
                "status": "PASS",
                "staging_files": len(staged),
                "staging_bytes": sum(path.stat().st_size for path in staged),
                "retained_files": len(retained),
                "final_zenodo_files": 58,
                "final_zenodo_bytes": final_bytes,
                "manifest_rows": len(final_rows),
                "manifest_sha256": identity(manifest_path)["sha256"],
                "validation_sha256": identity(validation_path)["sha256"],
                "zip_members": len(member_rows),
                "zip_uncompressed_bytes": zip_uncompressed,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
